#!/usr/bin/env python3
"""Part B step (vi) — THE DIPOLES, on v1.5 (ff8c7e13...), TARGET WITHHELD: this file contains NO CMB vector and compares against nothing.
Estimator = v1.5 §4.1 verbatim: the weighted unit-vector sum D_i = (3/W_i) Σ w_s n̂_s over the footprint (§2.2 per-source mask ∧ sf ≥ 0.5, w = 1/sf,
published NSIDE64 map = the K1906 §1 FALLBACK, H5 mandatory), corrected by the SAME estimator applied to the uniform sky under the same mask+weights
(the Zenodo randoms, chunked). Covariance: 1,000 isotropic Poisson mocks under the same mask, weights and N_i (uniform points in the footprint,
weighted by 1/sf at their position). Redshift channel (§4.5, re-windowed): full-sample moment R and the four G-quartile moments R_w, covariances
from 1,000 redshift-permutation mocks. Fits (§4.3, §4.5(b)): joint two-channel for one b; count-only; redshift-only; the profile alternative.
f_i, g, g_w, w_i, null-bin membership are READ from the (v) record (.partB_v_closed.json), never recomputed here.
OUTPUT (JSON + stdout): b̂ in galactic Cartesian, Σ_b, σ_β, debiased norm, per-bin D_i and covariances, R/R_w and covariances, the count-only and
redshift-only vectors, the profile-alternative β, the 95 %/99 % region fractions of û (exact profile-χ² on the 3,616 cells), and the §972
DIAGNOSTIC pixel-LS vector labelled as such. Keeper's keeper_partB_vii_compare.py takes this file for (vii).
RUN ONLY on Keeper's gate word for (vi). --selftest runs the identical code path on a SYNTHETIC sky with an injected boost (no catalogue touched)
and must recover the injected vector within its own covariance (χ²₃ ≤ 7.815) — the license to run, posted before the run.
Library: r145_eb_lib.py must be sha256 b87a8b085780 (commit 4ce873ce; Cal §972) — asserted below.
v1.5.1 (K1908 §4 (c), pending Cal's hash): the redshift channel carries the intrinsic column, R_k = −g_k b + ζ_k a, ζ from the frozen (v) recipe
(full window from the (v) record; quartile windows ζ_w from the sample's per-quartile bin tables computed here — table quantities, no dipole).
Optional --prior SIGMA_A[,CENTRE_A] (Gaussian on the intrinsic vector, per component) — used ONLY if v1.5.1 names it; the v1.5 fit (no ζ) is posted beside."""
import sys, os, math, json, hashlib, datetime, resource
import numpy as np
sys.path.insert(0,'.'); import r145_eb_lib as L; import partB_diag_pixls as DG; import partB_v151_lib as V
from r145_eb_lib import C_KMS
assert L.lib_hash()=='b87a8b085780', L.lib_hash()
PRIOR=None
if '--prior' in sys.argv: _v=sys.argv[sys.argv.index('--prior')+1].split(','); PRIOR=(float(_v[0]),float(_v[1]) if len(_v)>1 else 0.0)
Q='../data/quaia'; NSIDE=64; NPIX=12*NSIDE*NSIDE; NMOCK=1000; CH=1_000_000; CHI2_2_95, CHI2_2_99 = 5.991, 9.210
RG=np.array([[-0.0548755604162154,-0.8734370902348850,-0.4838350155487132],[0.4941094278755837,-0.4448296299600112,0.7469822444972189],[-0.8676661490190047,-0.1980763734312015,0.4559837761750669]])
def icrs_to_gal_vec(ra,dec):
    c=np.radians(dec); a=np.radians(ra); return np.stack([np.cos(c)*np.cos(a),np.cos(c)*np.sin(a),np.sin(c)],-1)@RG.T
vL=L.lb_to_vec(280.5,-32.9); vS=L.lb_to_vec(302.8,-44.3); cL=math.cos(math.radians(5)); cS=math.cos(math.radians(3))
def in_mask(vg): return (np.abs(vg[:,2])>math.sin(math.radians(30)))&(vg@vL<cL)&(vg@vS<cS)
def uvsum(v,w):
    """§4.1: D = (3/W) Σ w n̂ (uncorrected)."""
    W=w.sum(); return 3*(w[:,None]*v).sum(0)/W
def region_frac(b,S,q):
    Si=np.linalg.inv(S); U=L.CELLS.center; num=U@(Si@b); den=np.einsum('ij,jk,ik->i',U,Si,U); bs=np.maximum(num/den,0.0); r=bs[:,None]*U-b; c2=np.einsum('ij,jk,ik->i',r,Si,r); return float((c2<=q).mean())
def mock_cov(N,wmap_sf,footprint_test,rng,nmock=None):
    nmock=nmock or NMOCK
    """covariance of the uncorrected unit-vector sum for N isotropic Poisson points in the footprint with weights 1/sf(position)."""
    Ds=[]
    for m in range(nmock):
        n=rng.poisson(N); v=rng.normal(size=(int(n*2.2),3)); v/=np.linalg.norm(v,axis=1)[:,None]; ok=footprint_test(v); v=v[ok][:n]; w=wmap_sf(v); Ds.append(uvsum(v,w))
    Ds=np.array(Ds); return Ds.mean(0),np.cov(Ds.T)
def zdipole(v,zp,w,rng,nmock=NMOCK):
    """ℓ=1 moment of the weighted observed-redshift field on the cells (lib convention: R from <z'>_c = m + R·n_c), covariance by z-permutation mocks."""
    idx=L.CELLS.index(v); mask=L.make_mask(30.0)
    def one(z):
        n=np.bincount(idx,weights=w,minlength=L.CELLS.n); sz=np.bincount(idx,weights=w*z,minlength=L.CELLS.n); ok=mask&(n>0); mean=sz[ok]/n[ok]; s2=float(np.var(z)); ww=n[ok]/s2
        X=np.column_stack([np.ones(ok.sum()),L.CELLS.center[ok]]); XtW=X.T*ww; G=XtW@X; p=np.linalg.solve(G,XtW@mean); return p[1:]
    R=one(zp); Rs=np.array([one(rng.permutation(zp)) for _ in range(nmock)]); return R,np.cov(Rs.T)
def run(tag,edges,rec,selftest=None):
    import healpy as hp
    from astropy.io import fits; from astropy.table import Table
    rng=np.random.default_rng(20260915)
    if selftest is None:
        t=Table.read(f'{Q}/partB_{tag}_masked.fits'); ra=np.array(t['ra'],float); dec=np.array(t['dec'],float); z=np.array(t['redshift_quaia'],float); G=np.array(t['phot_g_mean_mag'],float)
        sf_pub=np.array(fits.open(f'{Q}/selection_function_NSIDE64_{tag}.fits')[1].data.field(0)).reshape(-1).astype(float)
        pix=hp.ang2pix(NSIDE,np.radians(90-dec),np.radians(ra)); s=sf_pub[pix]; vg=icrs_to_gal_vec(ra,dec)
        pl,pb=hp.pix2ang(NSIDE,np.arange(NPIX),lonlat=True); pvg=icrs_to_gal_vec(pl,pb); foot_pix=in_mask(pvg)&(sf_pub>=0.5)
        def wmap_sf(v):   # v galactic -> icrs pixel -> 1/sf
            vi=v@RG; ra_=np.degrees(np.arctan2(vi[:,1],vi[:,0]))%360; dec_=np.degrees(np.arcsin(np.clip(vi[:,2],-1,1))); return 1/np.maximum(sf_pub[hp.ang2pix(NSIDE,np.radians(90-dec_),np.radians(ra_))],1e-3)
        def footprint_test(v):
            vi=v@RG; ra_=np.degrees(np.arctan2(vi[:,1],vi[:,0]))%360; dec_=np.degrees(np.arcsin(np.clip(vi[:,2],-1,1))); return in_mask(v)&(sf_pub[hp.ang2pix(NSIDE,np.radians(90-dec_),np.radians(ra_))]>=0.5)
        # the correction vector: the same estimator on the randoms, chunked
        Dr=np.zeros(3); Wr=0.0; Rr=np.zeros((3,3))
        with fits.open(f'{Q}/random_{tag}_10x.fits',memmap=True) as h:
            d=h[1].data
            for s0 in range(0,len(d),CH):
                rra=np.array(d['ra'][s0:s0+CH],float); rdec=np.array(d['dec'][s0:s0+CH],float); rv=icrs_to_gal_vec(rra,rdec); rp=hp.ang2pix(NSIDE,np.radians(90-rdec),np.radians(rra)); rs=sf_pub[rp]; rk=in_mask(rv)&(rs>=0.5)
                rw=1/np.maximum(rs[rk],1e-3); Dr+=3*(rw[:,None]*rv[rk]).sum(0); Wr+=rw.sum(); Rr+=3*(rv[rk].T*rw)@rv[rk]
        Dcorr=Dr/Wr; Rfoot=Rr/Wr       # first and second weighted moments of the uniform sky under the mask+weights: the offset AND the response 3<n n^T>
    else:
        vg,z,G,s,Dcorr,foot_pix,pvg,wmap_sf,footprint_test=selftest; pix=None; m=L.make_mask(30.0); U=L.CELLS.center[m]; Rfoot=3*(U.T@U)/len(U)
    ok=s>=0.5; w=np.where(ok,1/np.maximum(s,1e-3),0.0)
    rows=[]
    for i in range(len(edges)-1):
        sel=ok&(z>=edges[i])&(z<edges[i+1]); Di=uvsum(vg[sel],w[sel])-Dcorr; mmean,C=mock_cov(int(sel.sum()),wmap_sf,footprint_test,rng)
        Dlit=Di-(mmean-Dcorr); Ri=np.linalg.inv(Rfoot); Dres=Ri@Dlit; Cres=Ri@C@Ri.T      # LITERAL §4.1 (offset only) and RESPONSE-corrected (offset + 3<n n^T>^-1); Cal rules which is the criterion
        rows.append(dict(bin=(edges[i],edges[i+1]),N=int(sel.sum()),D=Dres.tolist(),cov=Cres.tolist(),D_literal=Dlit.tolist(),cov_literal=C.tolist(),D_raw=Di.tolist(),mock_mean_minus_corr=(mmean-Dcorr).tolist()))
    # redshift channel
    R,CR=zdipole(vg[ok],z[ok],w[ok],rng); q=np.quantile(G[ok],[0,.25,.5,.75,1.0]); q[-1]=np.inf; Rw=[]; CRw=[]
    for k in range(4):
        sq=ok&(G>=q[k])&(G<q[k+1]); r_,c_=zdipole(vg[sq],z[sq],w[sq],rng,nmock=400); Rw.append(r_); CRw.append(c_)
    fs=[r['f'] for r in rec['rows']]; wprof=[r['w'] for r in rec['rows']]; walt=[r['w_alt'] for r in rec['rows']]; g=rec['g']; gw=rec['g_w']; null=[r['null'] for r in rec['rows']]
    if 'zeta' in rec: zetas=[rec['zeta']]+list(rec['zeta_q'])          # from the (v) ADDENDUM record (bin MEANS, v1.5.1 §7.1 (v)); never recomputed here
    else:
        Nw=[r.get('N_w',r.get('N')) for r in rec['rows']]; zmean=[r.get('zmean',r['zmed']) for r in rec['rows']]; zeta_full,zbar=V.zeta_from_table(Nw,wprof,zmean); zetas_w=[]
        for k in range(4):
            sq=ok&(G>=q[k])&(G<q[k+1]); Nk=[float(w[sq&(z>=edges[i])&(z<edges[i+1])].sum()) for i in range(len(edges)-1)]; zk=[float((w*z)[sq&(z>=edges[i])&(z<edges[i+1])].sum()/Nk[i]) if Nk[i]>0 else zmean[i] for i in range(len(edges)-1)]; zetas_w.append(V.zeta_from_table(Nk,wprof,zk)[0])
        zetas=[zeta_full]+zetas_w
    Ds=[np.array(r['D']) for r in rows]; Cs=[np.array(r['cov']) for r in rows]
    fs_fit=[0.0 if nl else f for f,nl in zip(fs,null)]     # 4.4a: a null bin enters through the intrinsic term only
    b15,a15,cov15=L.joint_two_channel(Ds,Cs,fs_fit,wprof,[R]+Rw,[CR]+CRw,[g]+list(gw)); be15,sb15,_,_,_=L.fit_summary(b15,a15,cov15)     # v1.5 fit (no ζ), posted beside
    b,a,cov=V.joint_two_channel_zeta(Ds,Cs,fs_fit,wprof,[R]+Rw,[CR]+CRw,[g]+list(gw),zetas)                                              # v1.5.1 fit (ζ columns)
    if PRIOR is not None:
        sA_,cA_=PRIOR; Gm=np.linalg.inv(cov); rhs=Gm@np.concatenate([b,a]); Gm[3:,3:]+=np.eye(3)/sA_**2; rhs[3:]+=cA_*np.ones(3)/sA_**2*0.0; cov=np.linalg.inv(Gm); pp=cov@rhs; b,a=pp[:3],pp[3:]   # prior centred on 0 in vector form; a centre on |a| is not a linear prior — flagged
    be,sb,u,A,sA=L.fit_summary(b,a,cov)
    bc,ac,covc=L.joint_two_channel(Ds,Cs,fs_fit,wprof,[],[],[]); bec,sbc,uc,_,_=L.fit_summary(bc,ac,covc)
    bz,az,covz=L.joint_two_channel([],[],[],[],[R]+Rw,[CR]+CRw,[g]+list(gw)) if False else (None,None,None)
    # fit (a), v1.5.1 (d): redshift-only b from R_k + ζ_k a_c with a_c = the COUNT-ONLY fit's intrinsic vector (clean of the leak), its covariance propagated
    Rall=[R]+Rw; Call=[CR]+CRw; Gz=sum((gg**2)*np.linalg.inv(c) for gg,c in zip([g]+list(gw),Call)); rz=sum(gg*np.linalg.inv(c)@(-(r-zk*ac)) for gg,r,c,zk in zip([g]+list(gw),Rall,Call,zetas)); bz=np.linalg.solve(Gz,rz); Sz=np.linalg.inv(Gz)
    Jz=np.linalg.solve(Gz,sum(gg*zk*np.linalg.inv(c) for gg,c,zk in zip([g]+list(gw),Call,zetas))); Sz=Sz+Jz@covc[3:,3:]@Jz.T; bez=np.linalg.norm(bz); uz=bz/bez; sbz=math.sqrt(uz@Sz@uz)
    balt,aalt,covalt=L.joint_two_channel(Ds,Cs,fs_fit,walt,[R]+Rw,[CR]+CRw,[g]+list(gw)); bealt=np.linalg.norm(balt)
    blit,alit,covlit=L.joint_two_channel([np.array(r['D_literal']) for r in rows],[np.array(r['cov_literal']) for r in rows],fs_fit,wprof,[R]+Rw,[CR]+CRw,[g]+list(gw)); belit,sblit,ulit,_,_=L.fit_summary(blit,alit,covlit)
    Sb=cov[:3,:3]; deb=math.sqrt(max(be**2-np.trace(Sb),0.0)); lb=L.vec_to_lb(b); lbc=L.vec_to_lb(bc); lbz=L.vec_to_lb(bz)
    out=dict(tag=tag,weights_mode=rec['mode'],N_mask=rec['N_mask'],Dcorr=Dcorr.tolist(),Rfoot=Rfoot.tolist(),zetas=zetas,prior=PRIOR,v15_fit_no_zeta=dict(b=b15.tolist(),cov=cov15[:3,:3].tolist(),beta_c=be15*C_KMS,sigma_c=sb15*C_KMS),estimator_in_fit='RESPONSE-corrected (offset + 3<n n^T>^-1) — pending Cal v1.5.1; literal §4.1 rows kept as D_literal',rows=rows,R=R.tolist(),CR=CR.tolist(),Rw=[r.tolist() for r in Rw],CRw=[c.tolist() for c in CRw],G_quartiles=q[:4].tolist(),
             b=b.tolist(),cov_b=Sb.tolist(),cov_full=cov.tolist(),beta_c=be*C_KMS,sigma_beta_c=sb*C_KMS,u_lb=(float(lb[0][0]),float(lb[1][0])),debiased_norm_c=deb*C_KMS,A_int=A,sigma_A=sA,
             region95=region_frac(b,Sb,CHI2_2_95),region99=region_frac(b,Sb,CHI2_2_99),count_only=dict(b=bc.tolist(),cov=covc[:3,:3].tolist(),beta_c=bec*C_KMS,sigma_c=sbc*C_KMS,u_lb=(float(lbc[0][0]),float(lbc[1][0]))),
             redshift_only=dict(b=bz.tolist(),cov=Sz.tolist(),beta_c=bez*C_KMS,sigma_c=sbz*C_KMS,u_lb=(float(lbz[0][0]),float(lbz[1][0]))),profile_alt=dict(beta_c=bealt*C_KMS,shift_sigma=(bealt-be)/sb),
             literal_estimator_joint=dict(b=blit.tolist(),cov=covlit[:3,:3].tolist(),beta_c=belit*C_KMS,sigma_c=sblit*C_KMS),sigma_ge_half_beta_trigger=None)   # the 4.4 trigger needs β_CMB — Keeper applies it at (vii)
    print(f"   {tag}: weights {rec['mode'][:8]}; correction vector |Dcorr| = {np.linalg.norm(Dcorr):.5f} toward {tuple(round(float(x[0]),1) for x in L.vec_to_lb(Dcorr))}; footprint response eigen {np.round(np.linalg.eigvalsh(Rfoot),3).tolist()}")
    for r in rows: print(f"      bin {r['bin']}: N {r['N']:,}; D_literal = {np.round(r['D_literal'],5).tolist()} (σ {math.sqrt(r['cov_literal'][0][0]):.5f}); D_resp = {np.round(r['D'],5).tolist()} (σ/comp {math.sqrt(r['cov'][0][0]):.5f})")
    print(f"      ζ (full, quartiles) = {np.round(zetas,4).tolist()}; prior on a = {PRIOR}; v1.5 fit without ζ: β c = {be15*C_KMS:.0f} ± {sb15*C_KMS:.0f}")
    print(f"      JOINT b̂ (v1.5.1, ζ columns): β c = {be*C_KMS:.0f} ± {sb*C_KMS:.0f} km/s toward (l,b) = ({out['u_lb'][0]:.1f}, {out['u_lb'][1]:.1f}); debiased norm {deb*C_KMS:.0f}; Â = {A:.4f} ± {sA:.4f}; 95 % region {out['region95']:.3f} of the sphere, 99 % {out['region99']:.3f}; eigen-σ {[round(math.sqrt(e)*C_KMS) for e in np.linalg.eigvalsh(Sb)]} km/s")
    print(f"      count-only: {bec*C_KMS:.0f} ± {sbc*C_KMS:.0f} toward ({out['count_only']['u_lb'][0]:.1f}, {out['count_only']['u_lb'][1]:.1f}); redshift-only: {bez*C_KMS:.0f} ± {sbz*C_KMS:.0f} toward ({out['redshift_only']['u_lb'][0]:.1f}, {out['redshift_only']['u_lb'][1]:.1f}); profile-alt β = {bealt*C_KMS:.0f} ({(bealt-be)/sb:+.2f} σ_β)")
    print(f"      literal-§4.1 joint (offset only, no response): β c = {belit*C_KMS:.0f} ± {sblit*C_KMS:.0f} toward {tuple(round(float(x[0]),1) for x in L.vec_to_lb(blit))}")
    return out,b,Sb,blit,covlit[:3,:3]
if __name__=='__main__':
    print(f"partB_vi_dipoles.py {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; lib {L.lib_hash()}; diag {DG.diag_hash()}; {datetime.datetime.now():%Y-%m-%d %H:%M}")
    if '--selftest' in sys.argv:
        # synthetic skies, same code path; sf = 1 inside the §2.2 mask (no holes) so the offset correction is 0 by symmetry and the response is the mask's 3<n n^T>;
        # injected 500 km/s toward (120, −50) — NOT the CMB direction, |b| well inside the caps. Five seeds; mocks 200 per bin here (1,000 on the sky).
        NMOCK=200; ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; vinj=L.lb_to_vec(120.0,-50.0); binj=500.0/C_KMS; edges=[0.0,0.8,1.3,1.8,2.4,np.inf]; c2r=[]; c2l=[]; bs=[]
        for seed in range(5):
            rng=np.random.default_rng(100+seed); n,z,zp,S=L.synth_sky_full(int(913_899/0.32),binj,vinj,rng,ZEG,XG,1.0,1.0,sigma_z=0.04); km=in_mask(n); n=n[km]; zp=zp[km]; S=S[km]; G=-2.5*np.log10(S)+20.5
            s_=np.ones(len(n)); wmap=lambda v: np.ones(len(v)); ftest=lambda v: in_mask(v); rows=[]
            for i in range(5):
                sel=(zp>=edges[i])&(zp<edges[i+1]); x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,edges[i],edges[i+1],sel.sum()); rows.append(dict(f=2+2*x+B,zmed=float(np.median(zp[sel])),null=abs(2+2*x+B)<0.3,N_w=int(sel.sum())))
            wv=L.profile_w([r['zmed'] for r in rows]); chis=[L.comoving(r['zmed']) for r in rows]
            for r,wi,c in zip(rows,wv,chis): r['w']=wi; r['w_alt']=chis[0]/c
            qe=np.quantile(G,[0,.25,.5,.75]); rec=dict(mode='SELFTEST (sf=1)',N_mask=len(n),rows=rows,g=1+float(zp.mean()),g_w=[1+float(zp[(G>=a)&(G<b_)].mean()) for a,b_ in zip(qe,list(qe[1:])+[np.inf])])
            out,b,Sb,bl,Sl=run(f'SELFTEST seed {seed}',edges,rec,selftest=(n,zp,G,s_,np.zeros(3),None,None,wmap,ftest))
            d=b-binj*vinj; c2r.append(float(d@np.linalg.solve(Sb,d))); dl=bl-binj*vinj; c2l.append(float(dl@np.linalg.solve(Sl,dl))); bs.append(b)
        bm=np.mean(bs,0)*C_KMS; print(f"   SELFTEST (5 seeds, injected 500 km/s toward (120, −50)): χ²₃ response-corrected = {np.round(c2r,2).tolist()} (≤ 7.815 expected in ≥ 4 of 5); literal §4.1 = {np.round(c2l,2).tolist()}; mean b̂ (response) = {np.round(bm,0).tolist()} km/s vs injected {np.round(500*vinj,0).tolist()}")
        ok=sum(c<=7.815 for c in c2r)>=4; print(f"   SELFTEST → {'PASS' if ok else 'FAIL'}"); print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB"); sys.exit(0 if ok else 1)
    if '--run' not in sys.argv: print("   (vi) is not run without --run (Keeper's gate word for (vi) on v1.5's hash)."); sys.exit(0)
    rec=json.load(open('.partB_v_closed.json')); add=json.load(open('.partB_v_addendum.json')); outs={}
    for tag,edges in (("G20.5",[0.0,0.8,1.3,1.8,2.4,np.inf]),("G20.0",[0.0,1.3,1.8,np.inf])):
        r_=dict(rec[tag]); r_.update(zeta=add[tag]['zeta'],zeta_q=add[tag]['zeta_q']); outs[tag],_,_,_,_=run(tag,edges,r_)
    json.dump(outs,open('.partB_vi_dipoles.json','w'),indent=1,default=float); print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
