#!/usr/bin/env python3
"""Part B step (v) ADDENDUM (v1.5.1 §7.1 (v), Cal 12:26): the (v)-type quantities the ζ term and the response-corrected estimator need, posted
BEFORE (vi): per-bin weighted MEANS of observed z (the lib fits the per-cell mean of z, so ζ is on means), ζ (full window) and ζ_q (four G-quartile
windows) by the frozen recipe ζ = Σ p_i w_i (z̄_i − z̄) with p_i = N_w,i/N_w, w_i from the (v) record; D_corr = the §4.1 unit-vector sum on the
Zenodo randoms under the same footprint and weights (first moment of the uniform sky), and R_foot = its second moment 3⟨n nᵀ⟩ (the response).
NO catalogue position enters any dipole here: the catalogue contributes z, G and sf only; the randoms contribute both moments. Chunked; no SkyCoord."""
import sys, os, math, json, hashlib, datetime, resource
import numpy as np
from astropy.io import fits; from astropy.table import Table
sys.path.insert(0,'.'); import r145_eb_lib as L; import partB_v151_lib as V
import healpy as hp
Q='../data/quaia'; NSIDE=64; NPIX=12*NSIDE*NSIDE; CH=1_000_000
RG=np.array([[-0.0548755604162154,-0.8734370902348850,-0.4838350155487132],[0.4941094278755837,-0.4448296299600112,0.7469822444972189],[-0.8676661490190047,-0.1980763734312015,0.4559837761750669]])
def icrs_to_gal_vec(ra,dec):
    c=np.radians(dec); a=np.radians(ra); return np.stack([np.cos(c)*np.cos(a),np.cos(c)*np.sin(a),np.sin(c)],-1)@RG.T
vL=L.lb_to_vec(280.5,-32.9); vS=L.lb_to_vec(302.8,-44.3); cL=math.cos(math.radians(5)); cS=math.cos(math.radians(3))
def in_mask(vg): return (np.abs(vg[:,2])>math.sin(math.radians(30)))&(vg@vL<cL)&(vg@vS<cS)
print(f"partB_v_addendum.py {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; lib {L.lib_hash()}; v151 {V.v151_hash()}; {datetime.datetime.now():%Y-%m-%d %H:%M}")
rec=json.load(open('.partB_v_closed.json')); out={}
for tag,edges in (("G20.5",[0.0,0.8,1.3,1.8,2.4,np.inf]),("G20.0",[0.0,1.3,1.8,np.inf])):
    t=Table.read(f'{Q}/partB_{tag}_masked.fits'); ra=np.array(t['ra'],float); dec=np.array(t['dec'],float); z=np.array(t['redshift_quaia'],float); G=np.array(t['phot_g_mean_mag'],float)
    sf_pub=np.array(fits.open(f'{Q}/selection_function_NSIDE64_{tag}.fits')[1].data.field(0)).reshape(-1).astype(float); s=sf_pub[hp.ang2pix(NSIDE,np.radians(90-dec),np.radians(ra))]; ok=s>=0.5; w=np.where(ok,1/np.maximum(s,1e-3),0.0)
    rows=rec[tag]['rows']; wprof=[r['w'] for r in rows]; nb=len(edges)-1
    def table(sel):
        Nw=[float(w[sel&(z>=edges[i])&(z<edges[i+1])].sum()) for i in range(nb)]; zm=[float((w*z)[sel&(z>=edges[i])&(z<edges[i+1])].sum()/max(Nw[i],1e-9)) for i in range(nb)]; return Nw,zm
    Nw,zmean=table(ok); zeta,zbar=V.zeta_from_table(Nw,wprof,zmean); zeta_med,_=V.zeta_from_table([r['N_w'] for r in rows],wprof,[r['zmed'] for r in rows])
    q=np.quantile(G[ok],[0,.25,.5,.75,1.0]); q[-1]=np.inf; zq=[]; zq_tab=[]
    for k in range(4):
        Nk,zk=table(ok&(G>=q[k])&(G<q[k+1])); zq.append(V.zeta_from_table(Nk,wprof,zk)[0]); zq_tab.append(dict(N_w=Nk,zmean=zk))
    # randoms: first and second weighted moments under the same footprint + weights
    Dr=np.zeros(3); Wr=0.0; Rr=np.zeros((3,3)); nin=0
    with fits.open(f'{Q}/random_{tag}_10x.fits',memmap=True) as h:
        d=h[1].data
        for s0 in range(0,len(d),CH):
            rra=np.array(d['ra'][s0:s0+CH],float); rdec=np.array(d['dec'][s0:s0+CH],float); rv=icrs_to_gal_vec(rra,rdec); rs=sf_pub[hp.ang2pix(NSIDE,np.radians(90-rdec),np.radians(rra))]; rk=in_mask(rv)&(rs>=0.5)
            rw=1/np.maximum(rs[rk],1e-3); Dr+=3*(rw[:,None]*rv[rk]).sum(0); Wr+=rw.sum(); Rr+=3*(rv[rk].T*rw)@rv[rk]; nin+=int(rk.sum())
    Dcorr=Dr/Wr; Rfoot=Rr/Wr; ev,evec=np.linalg.eigh(Rfoot)
    print(f"\n=== {tag} (v) ADDENDUM: N_w in footprint {sum(Nw):,.0f} ===")
    print(f"   bin weighted MEANS of z: {np.round(zmean,4).tolist()} (medians on the record: {[round(r['zmed'],4) for r in rows]}); z̄ = {zbar:.4f}")
    print(f"   ζ (means) = {zeta:+.4f}   [ζ on medians = {zeta_med:+.4f}; Keeper K1908 −0.1535 / −0.1799 on the 09:19 record]; ζ_q (G quartiles, edges {np.round(q[:4],3).tolist()}) = {np.round(zq,4).tolist()}")
    print(f"   D_corr (unit-vector sum on {nin:,} randoms in the footprint) = {np.round(Dcorr,5).tolist()}, |D_corr| = {np.linalg.norm(Dcorr):.5f} toward (l,b) = ({float(L.vec_to_lb(Dcorr)[0][0]):.1f}, {float(L.vec_to_lb(Dcorr)[1][0]):.1f})")
    print(f"   R_foot = 3<n nᵀ>_footprint: eigen {np.round(ev,4).tolist()} along (l,b) = {[(round(float(L.vec_to_lb(evec[:,k])[0][0])),round(float(L.vec_to_lb(evec[:,k])[1][0]))) for k in range(3)]}")
    out[tag]=dict(N_w=Nw,zmean=zmean,zbar=zbar,zeta=zeta,zeta_median=zeta_med,G_quartiles=q[:4].tolist(),zeta_q=zq,quartile_tables=zq_tab,Dcorr=Dcorr.tolist(),Rfoot=Rfoot.tolist(),N_randoms_in_footprint=nin)
json.dump(out,open('.partB_v_addendum.json','w'),indent=1,default=float); print(f"\npeak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
