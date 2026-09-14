#!/usr/bin/env python3
"""Part B step (v) — per-bin quantities from the catalogue itself, BEFORE any dipole (v1.3 §2–4). Computes NO dipole and NO ℓ = 1 moment.
Posts: N_i (frozen mask, both magnitude samples), x_i (quadratic derivative at the limit; linear secant as diagnostic), B_i (sharp Eq. 14 and smooth Eq. 21
with redshift_quaia_err), g (full sample) and g_w (G quartiles), χ̄_i (median comoving), f_i and null-bin membership for a given α_i.
Weights: the per-bin selection functions of §2.3 are NOT yet generated (code pin pending) — everything here is UNWEIGHTED and labelled so."""
import sys, math, json, hashlib, datetime
import numpy as np
from astropy.io import fits
from scipy.special import erf
sys.path.insert(0,'.'); import r145_eb_lib as L
ZE=[0.0,0.8,1.3,1.8,2.4,np.inf]; MLIM={'G20.5':20.5,'G20.0':20.0}
alpha_in=float(sys.argv[1]) if len(sys.argv)>1 else None
print(f"lib hash {L.lib_hash()}; this file sha256 {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; {datetime.datetime.now():%Y-%m-%d %H:%M}")
def x_quad_lin(mags,mlim):
    grid=np.linspace(mlim-0.5,mlim,11); logN=np.log10([(mags<g).sum() for g in grid])
    q=np.polyfit(grid,logN,2); lin=np.polyfit(grid,logN,1)[0]/0.4; quad=(2*q[0]*mlim+q[1])/0.4
    # derivative uncertainty from the quadratic fit's covariance
    A=np.vstack([grid**2,grid,np.ones_like(grid)]).T; resid=logN-A@q; s2=(resid@resid)/max(len(grid)-3,1); cov=s2*np.linalg.inv(A.T@A); J=np.array([2*mlim,1,0]); return quad,lin,math.sqrt(max(J@cov@J,0))/0.4
def B_sharp(z_all,z1,z2,N,win=0.05):
    def dens(ze):
        if ze<=0 or not np.isfinite(ze): return 0.0
        return float(((z_all>=ze-win)&(z_all<ze+win)).sum()/(2*win))
    return ((1+z2)*dens(z2) if np.isfinite(z2) else 0.0)/N-(1+z1)*dens(z1)/N
def B_smooth(z_all,sig_all,z1,z2,ngrid=1600):
    """Eq. 21: B = -∫ f_b(z) dlogW_b/dlog(1+z) dz, W_b(z) = ∫ top-hat(z') P(z'|z) dz' with P Gaussian of the per-source sigma; f_b ∝ n(z) W_b(z).
    n(z) from the histogram of reported z (a proxy for true z at first order); sigma(z) = the median redshift_quaia_err in narrow z slices."""
    zz=np.linspace(0.0,max(6.0,float(np.percentile(z_all,99.9))+1.0),ngrid); n,_=np.histogram(z_all,bins=np.append(zz,zz[-1]+(zz[1]-zz[0]))); n=n.astype(float)
    sig=np.array([np.median(sig_all[(z_all>=a-0.05)&(z_all<a+0.05)]) if ((z_all>=a-0.05)&(z_all<a+0.05)).sum()>50 else np.nan for a in zz]); sig=np.where(np.isnan(sig),np.nanmedian(sig),sig); sig=np.maximum(sig,1e-4)
    hi=z2 if np.isfinite(z2) else zz[-1]+50; W=0.5*(erf((hi-zz)/(math.sqrt(2)*sig))-erf((z1-zz)/(math.sqrt(2)*sig))); W=np.maximum(W,1e-300)
    fb=n*W; fb/=np.trapz(fb,zz); dlogW=np.gradient(np.log(W),zz)*(1+zz); return float(-np.trapz(fb*dlogW,zz))
out={}
for tag in ('G20.5','G20.0'):
    with fits.open(f'../data/quaia/quaia_{tag}.fits',memmap=True) as h: t=h[1].data; l=np.array(t['l'],float); b=np.array(t['b'],float); z=np.array(t['redshift_quaia'],float); ze=np.array(t['redshift_quaia_err'],float); G=np.array(t['phot_g_mean_mag'],float)
    v=L.lb_to_vec(l,b); cell=L.CELLS.index(v); mask=L.make_mask(30.0); keep=mask[cell]; z,ze,G,v=z[keep],ze[keep],G[keep],v[keep]
    print(f"\n=== sample {tag}: {len(keep):,} sources; {keep.sum():,} inside the frozen mask (|b|>30° + LMC 5° + SMC 3°) = {100*keep.mean():.1f}% ===")
    print(f"   redshift_quaia: min {z.min():.3f} max {z.max():.3f} median {np.median(z):.3f}; redshift_quaia_err median {np.median(ze):.4f}, median err/(1+z) {np.median(ze/(1+z)):.4f}")
    m=float(z.mean()); g_full=1+m
    q=np.quantile(G,[0,0.25,0.5,0.75,1.0]); q[-1]=np.inf; g_w=[1+float(z[(G>=q[k])&(G<q[k+1])].mean()) for k in range(4)]
    print(f"   redshift channel factors (UNWEIGHTED): g(full sample) = 1 + ⟨z⟩ = {g_full:.4f};  G quartile edges {np.round(q[:4],3).tolist()};  g_w = {[round(x,4) for x in g_w]}")
    rows=[]
    print(f"   {'bin':12}{'N_i':>9}{'x_quad':>8}{'±':>6}{'x_lin(diag)':>12}{'B_sharp':>9}{'B_smooth':>9}{'ΔB':>8}{'χ̄_i [Mpc]':>11}{'w_i':>7}")
    for i in range(5):
        sel=(z>=ZE[i])&(z<ZE[i+1]); N=int(sel.sum()); xq,xl,sx=x_quad_lin(G[sel],MLIM[tag]); Bs=B_sharp(z,ZE[i],ZE[i+1],N); Bm=B_smooth(z,ze,ZE[i],ZE[i+1])
        zmed=float(np.median(z[sel])); rows.append(dict(bin=(ZE[i],ZE[i+1]),N=N,x_quad=xq,sx=sx,x_lin=xl,B_sharp=Bs,B_smooth=Bm,zmed=zmed))
    chis=[L.comoving(r['zmed']) for r in rows]; w=[(chis[0]/c)**2 for c in chis]
    for r,c,wi in zip(rows,chis,w):
        r['chi']=c; r['w']=wi; print(f"   {str(r['bin']):12}{r['N']:9d}{r['x_quad']:8.3f}{r['sx']:6.3f}{r['x_lin']:12.3f}{r['B_sharp']:9.3f}{r['B_smooth']:9.3f}{r['B_smooth']-r['B_sharp']:8.3f}{c:11.0f}{wi:7.3f}")
    if alpha_in is not None:
        print(f"   with α = {alpha_in} in every bin (PLACEHOLDER until §3.2's zero points are pinned): f_i = 2 + x(1+α) + B_smooth = {[round(2+r['x_quad']*(1+alpha_in)+r['B_smooth'],3) for r in rows]}; null-bin rule |f_i| < 2σ_f -> {[abs(2+r['x_quad']*(1+alpha_in)+r['B_smooth'])<2*r['sx']*(1+alpha_in) for r in rows]}")
    out[tag]=dict(N_mask=int(keep.sum()),g_full=g_full,g_w=g_w,G_quartiles=q[:4].tolist(),rows=rows)
json.dump(out,open('.partB_v_table.json','w'),indent=1,default=float)
