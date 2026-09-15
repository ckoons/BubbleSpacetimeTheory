#!/usr/bin/env python3
"""Part B step (v), CLOSE (v1.4): per-source mask; weights = 1/selection function (per-bin maps from the released code when present, else the
published NSIDE64 map of the sample as the K1906 §1 FALLBACK — labelled); < 0.5 excluded; weighted N_i; α_i (§3.2, Grace's zero points);
x_i three ways; B_i smooth (frozen) + sharp + the §4.4 sensitivity; g, g_w; χ̄_i; w_i; null-bin rule; the randoms' ℓ = 1 moment.
NO catalogue dipole is computed here."""
import sys, os, math, json, hashlib, datetime, glob
import numpy as np
from astropy.io import fits
from astropy.table import Table
from scipy.special import erf
sys.path.insert(0,'.'); import r145_eb_lib as L; import partB_diag_pixls as DG   # DG = diagnostic pixel-level LS (Cal §972), not the estimator
Q='../data/quaia'; ZE5=[0.0,0.8,1.3,1.8,2.4,np.inf]; ZE3=[0.0,1.3,1.8,np.inf]
NSIDE=64; NPIX=12*NSIDE*NSIDE
F0_G,LAM_G=3270.0,621.79e-9; F0_W1,LAM_W1=309.540,3352.6e-9; NU_RATIO=LAM_W1/LAM_G      # 5.392 (Grace's pins)
OUTLIER=float(sys.argv[1]) if len(sys.argv)>1 else 0.10
print(f"lib {L.lib_hash()} (must be b87a8b085780 = commit 4ce873ce); diag {DG.diag_hash()}; file {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; {datetime.datetime.now():%Y-%m-%d %H:%M}; ν_G/ν_W1 = {NU_RATIO:.4f}; outlier fraction for the sensitivity = {OUTLIER}")
def ang2pix_ring(nside,theta,phi):
    import healpy as hp; return hp.ang2pix(nside,theta,phi)
def read_map(fn):
    with fits.open(fn) as h: d=h[1].data; col=d.columns[0].name; m=np.array(d[col]).reshape(-1)
    assert len(m)==NPIX, (fn,len(m)); return m.astype(float)
def x_three(G,mlim):
    grid=np.linspace(mlim-0.5,mlim,11); logN=np.log10([(G<g).sum() for g in grid]); q=np.polyfit(grid,logN,2); xq=(2*q[0]*mlim+q[1])/0.4; xl=np.polyfit(grid,logN,1)[0]/0.4
    g2=np.linspace(mlim-0.2,mlim,5); xloc=np.polyfit(g2,np.log10([(G<g).sum() for g in g2]),1)[0]/0.4
    A=np.vstack([grid**2,grid,np.ones_like(grid)]).T; r=logN-A@q; s2=(r@r)/8; cov=s2*np.linalg.inv(A.T@A); J=np.array([2*mlim,1,0]); return xq,xl,xloc,math.sqrt(max(J@cov@J,0))/0.4
def B_sharp(z_all,wt,z1,z2,Nw,win=0.05):
    def dens(ze):
        if ze<=0 or not np.isfinite(ze): return 0.0
        s=(z_all>=ze-win)&(z_all<ze+win); return float(wt[s].sum()/(2*win))
    return (((1+z2)*dens(z2)) if np.isfinite(z2) else 0.0)/Nw-(1+z1)*dens(z1)/Nw
def B_smooth(z_all,wt,sig_all,z1,z2,sig_scale=1.0,outlier=0.0,ngrid=1600):
    zz=np.linspace(0.0,7.0,ngrid); dz=zz[1]-zz[0]; n,_=np.histogram(z_all,bins=np.append(zz,zz[-1]+dz),weights=wt); n=n.astype(float)
    sig=np.array([np.median(sig_all[(z_all>=a-0.05)&(z_all<a+0.05)]) if ((z_all>=a-0.05)&(z_all<a+0.05)).sum()>50 else np.nan for a in zz]); sig=np.where(np.isnan(sig),np.nanmedian(sig),sig)*sig_scale; sig=np.maximum(sig,1e-4)
    hi=z2 if np.isfinite(z2) else 50.0; Wg=0.5*(erf((hi-zz)/(math.sqrt(2)*sig))-erf((z1-zz)/(math.sqrt(2)*sig)))
    if outlier>0:   # an outlier component: a fraction of sources whose reported z is unrelated to true z (flat over the range) -> W_b gets a constant floor
        Wg=(1-outlier)*Wg+outlier*((min(hi,4.6)-z1)/4.6)
    W=np.maximum(Wg,1e-300); fb=n*W; fb/=np.trapezoid(fb,zz); dlogW=np.gradient(np.log(W),zz)*(1+zz); return float(-np.trapezoid(fb*dlogW,zz))
out={}
for tag,edges,mlim in (("G20.5",ZE5,20.5),("G20.0",ZE3,20.0)):
    t=Table.read(f'{Q}/partB_{tag}_masked.fits'); N0=len(t); ra=np.array(t['ra'],float); dec=np.array(t['dec'],float); z=np.array(t['redshift_quaia'],float); ze=np.array(t['redshift_quaia_err'],float); G=np.array(t['phot_g_mean_mag'],float); W1=np.array(t['mag_w1_vg'],float)
    pix=ang2pix_ring(NSIDE,np.radians(90-dec),np.radians(ra)); sf_pub=read_map(f'{Q}/selection_function_NSIDE64_{tag}.fits')
    perbin=sorted(glob.glob(f'{Q}/selfunc_perbin/selfunc_NSIDE64_{tag}_bin*.fits')); mode='PER-BIN (released code)' if len(perbin)==len(edges)-1 else 'FALLBACK (published NSIDE64 map of the sample; K1906 §1; H5 mandatory)'
    print(f"\n=== {tag}: per-source mask {N0:,}; weights mode: {mode} ({len(perbin)} per-bin maps present) ===")
    alpha_src=-np.log10((F0_G*10**(-0.4*G))/(F0_W1*10**(-0.4*W1)))/np.log10(NU_RATIO)   # α = −log(S_G/S_W1)/log(ν_G/ν_W1), ν_G/ν_W1 = 5.392 (sign bug of the 09:17 run fixed: divided by log(1/ratio))
    rows=[]; keep_all=np.zeros(N0,bool)
    for i in range(len(edges)-1):
        sel=(z>=edges[i])&(z<edges[i+1]); sf=read_map(perbin[i]) if mode.startswith('PER') else sf_pub; s=sf[pix]; ok=sel&(s>=0.5); wt=np.where(ok,1/np.maximum(s,1e-3),0.0); keep_all|=ok
        Nw=float(wt.sum()); Nraw=int(ok.sum()); xq,xl,xloc,sx=x_three(G[ok],mlim); xsys=0.5*max(abs(xq-xl),abs(xq-xloc)); curved=abs(xq-xl)>2*sx
        a_med=float(np.median(alpha_src[ok])); mad=1.4826*float(np.median(np.abs(alpha_src[ok]-a_med))); sa=mad/math.sqrt(Nraw)
        zw=z[keep_all|ok]; ww=wt  # densities from the WEIGHTED masked sample of the whole catalogue (all sources with s>=0.5)
        Bs=B_sharp(z,np.where(sf[pix]>=0.5,1/np.maximum(sf[pix],1e-3),0.0),edges[i],edges[i+1],Nw); wall=np.where(sf[pix]>=0.5,1/np.maximum(sf[pix],1e-3),0.0)
        Bm=B_smooth(z,wall,ze,edges[i],edges[i+1]); Bh=B_smooth(z,wall,ze,edges[i],edges[i+1],0.5); B2=B_smooth(z,wall,ze,edges[i],edges[i+1],2.0); Bo=B_smooth(z,wall,ze,edges[i],edges[i+1],1.0,OUTLIER)
        sB=max(abs(Bh-Bm),abs(B2-Bm),abs(Bo-Bm)); f=2+xq*(1+a_med)+Bm; sf_=math.sqrt(((1+a_med)*math.hypot(sx,xsys))**2+(xq*sa)**2+sB**2); null=abs(f)<2*sf_
        zmed=float(np.median(np.repeat(z[ok],1))); chi=L.comoving(zmed)
        rows.append(dict(bin=(edges[i],edges[i+1]),N_raw=Nraw,N_w=Nw,x_quad=xq,x_lin=xl,x_loc=xloc,sx=sx,x_sys=xsys,curved=bool(curved),alpha=a_med,s_alpha=sa,B_smooth=Bm,B_sharp=Bs,B_half=Bh,B_x2=B2,B_out=Bo,sB=sB,f=f,sf=sf_,null=bool(null),zmed=zmed,chi=chi))
    chi1=rows[0]['chi']
    for r in rows: r['w']=(chi1/r['chi'])**2; r['w_alt']=chi1/r['chi']
    print(f"   {'bin':12}{'N_raw':>8}{'N_w':>10}{'x_quad':>8}{'x_lin':>7}{'x_loc':>7}{'σx':>6}{'sys':>6}{'crv':>4}{'α':>7}{'σα':>7}{'B_sm':>8}{'B_sh':>8}{'B½':>7}{'B×2':>7}{'B_out':>7}{'f':>8}{'σf':>6}{'null':>5}{'z̃':>6}{'χ̄':>6}{'w':>7}")
    for r in rows: print(f"   {str(r['bin']):12}{r['N_raw']:8d}{r['N_w']:10.0f}{r['x_quad']:8.3f}{r['x_lin']:7.3f}{r['x_loc']:7.3f}{r['sx']:6.3f}{r['x_sys']:6.3f}{'Y' if r['curved'] else 'n':>4}{r['alpha']:7.3f}{r['s_alpha']:7.4f}{r['B_smooth']:8.3f}{r['B_sharp']:8.3f}{r['B_half']:7.3f}{r['B_x2']:7.3f}{r['B_out']:7.3f}{r['f']:8.3f}{r['sf']:6.3f}{'Y' if r['null'] else 'n':>5}{r['zmed']:6.2f}{r['chi']:6.0f}{r['w']:7.3f}")
    s_all=sf_pub[pix]; okall=s_all>=0.5; wall=np.where(okall,1/np.maximum(s_all,1e-3),0.0); m=float((wall*z).sum()/wall.sum()); q=np.quantile(G[okall],[0,0.25,0.5,0.75,1.0]); q[-1]=np.inf
    gw=[float(1+(wall*z)[(G>=q[k])&(G<q[k+1])].sum()/wall[(G>=q[k])&(G<q[k+1])].sum()) for k in range(4)]
    print(f"   redshift channel (weights: published map, the full-sample window): g = 1 + ⟨z⟩_w = {1+m:.4f}; G quartile edges {np.round(q[:4],3).tolist()}; g_w = {[round(x,4) for x in gw]}")
    out[tag]=dict(mode=mode,N_mask=N0,rows=rows,g=1+m,g_w=gw,G_quartiles=q[:4].tolist())
    # the randoms' ell=1 moment under the same mask/weights (systematics check; not the catalogue's dipole).
    # 09:25 crash: 12.96 M rows through astropy SkyCoord in one allocation exhausted memory. ICRS->Galactic is the fixed J2000 rotation
    # R_G (Hipparcos Vol. 1 §1.5.3; astropy's own matrix, verified here on 1,000 points to < 1e-4 deg (chord angle)); chunked numpy, 1 M rows at a time.
    fr=f'{Q}/random_{tag}_10x.fits'
    if os.path.exists(fr):
        import healpy as hp
        RG=np.array([[-0.0548755604162154,-0.8734370902348850,-0.4838350155487132],[0.4941094278755837,-0.4448296299600112,0.7469822444972189],[-0.8676661490190047,-0.1980763734312015,0.4559837761750669]])
        def icrs_to_gal_vec(ra_deg,dec_deg):
            c=np.radians(dec_deg); a=np.radians(ra_deg); v=np.stack([np.cos(c)*np.cos(a),np.cos(c)*np.sin(a),np.sin(c)],-1); return v@RG.T
        from astropy.coordinates import SkyCoord; import astropy.units as u
        tr=np.random.default_rng(0).uniform(size=(1000,2)); tra=tr[:,0]*360; tdec=np.degrees(np.arcsin(2*tr[:,1]-1)); gtest=SkyCoord(ra=tra*u.deg,dec=tdec*u.deg,frame='icrs').galactic
        err=np.degrees(np.linalg.norm(icrs_to_gal_vec(tra,tdec)-L.lb_to_vec(gtest.l.deg,gtest.b.deg),axis=1)).max(); assert err<1e-4, err   # chord angle (arccos loses precision at 1e-7 rad); 1e-4 deg vs a 0.9 deg pixel
        vL=L.lb_to_vec(280.5,-32.9); vS=L.lb_to_vec(302.8,-44.3); cL=math.cos(math.radians(5)); cS=math.cos(math.radians(3))
        cnt=np.zeros(L.CELLS.n); wc=np.zeros(NPIX); nin=0; ntot=0; CH=1_000_000
        with fits.open(fr,memmap=True) as h:
            d=h[1].data; nrow=len(d)
            for s0 in range(0,nrow,CH):
                rra=np.array(d['ra'][s0:s0+CH],float); rdec=np.array(d['dec'][s0:s0+CH],float); vg=icrs_to_gal_vec(rra,rdec)
                km=(np.abs(vg[:,2])>math.sin(math.radians(30)))&(vg@vL<cL)&(vg@vS<cS); rp=hp.ang2pix(NSIDE,np.radians(90-rdec),np.radians(rra)); rs=sf_pub[rp]; rk=km&(rs>=0.5)
                rw=1/np.maximum(rs[rk],1e-3); cnt+=np.bincount(L.CELLS.index(vg[rk]),weights=rw,minlength=L.CELLS.n); wc+=np.bincount(rp[rk],weights=rw,minlength=NPIX); nin+=int(rk.sum()); ntot+=len(rra)
                del rra,rdec,vg,km,rp,rs,rk,rw
        mask=L.make_mask(30.0); cntc=cnt.copy(); cntc[~mask]=0; Dc,covc=L.dipole_ls(cntc,mask)
        # pixel-level: footprint = §2.2 mask AND sf >= 0.5, at pixel centres (the same rotation); the randoms are the uniform sky under the same mask+weights (Cal 4.1's correction vector)
        pl,pb=hp.pix2ang(NSIDE,np.arange(NPIX),lonlat=True); pvg=icrs_to_gal_vec(pl,pb)
        foot=(np.abs(pvg[:,2])>math.sin(math.radians(30)))&(pvg@vL<cL)&(pvg@vS<cS)&(sf_pub>=0.5); area=np.full(NPIX,4*math.pi/NPIX); D,cov=DG.dipole_ls_pix(wc,foot,pvg,area)
        lc=L.vec_to_lb(Dc); lp=L.vec_to_lb(D)
        print(f"   RANDOMS ({tag}, 10x): {ntot:,} rows read in {CH:,}-row chunks; {nin:,} inside mask & sf>=0.5 (rotation check vs astropy on 1,000 points: max {err:.1e} deg). CELL-level (footprint = §2.2 mask only): |D| = {np.linalg.norm(Dc):.5f} toward (l, b) = ({float(np.ravel(lc[0])[0]):.1f}, {float(np.ravel(lc[1])[0]):.1f}) - the sf<0.5 holes read as a dipole. PIXEL-level (footprint = §2.2 mask AND sf>=0.5, NSIDE 64, diagnostic estimator dipole_ls_pix): |D| = {np.linalg.norm(D):.5f} toward ({float(np.ravel(lp[0])[0]):.1f}, {float(np.ravel(lp[1])[0]):.1f}), sigma/component = {math.sqrt(cov[0,0]):.5f}, chi2_3 vs zero = {D@np.linalg.solve(cov,D):.1f} - the uniform sky under the same mask+weights, Cal 4.1's correction vector")
        out[tag]['randoms']=dict(N_rows=ntot,N=nin,D_cell=Dc.tolist(),D_pix=D.tolist(),cov_pix=cov.tolist(),chi2_pix=float(D@np.linalg.solve(cov,D)),rotation_check_deg=float(err))
    else: print(f"   randoms file {fr} not present (Zenodo v1.0.0 ships randoms for G<20.5 only? - see the download record)")
import resource; print(f"\npeak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
json.dump(out,open('.partB_v_closed.json','w'),indent=1,default=float)
