#!/usr/bin/env python3
"""Toy — R149 E2 (S6 with ΔA·ŵ from the z-mix between cuts) + E3 (x_i: linear 0.5-mag fit vs quadratic-at-the-edge). Synthetic only; no freeze line, no catalogue."""
import math, json, sys, os
import numpy as np
import r145_eb_lib as L
from r145_eb_lib import C_KMS
TOY=os.path.basename(__file__).split('_')[1]; print(f"toy {TOY}; lib hash {L.lib_hash()}")
ZE=[0.0,0.8,1.3,1.8,2.4,np.inf]; ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; mask=L.make_mask(30.0)
def x_two_ways(S,lim):
    """x from the cumulative counts N(<m) in the 0.5-mag window below the limit: linear LS slope, and quadratic LS with the derivative AT the edge."""
    m=-2.5*np.log10(S); mlim=-2.5*math.log10(lim); grid=np.linspace(mlim-0.5,mlim,11); logN=np.log10([(m<g).sum() for g in grid])
    lin=np.polyfit(grid,logN,1)[0]/0.4; q=np.polyfit(grid,logN,2); quad=(2*q[0]*mlim+q[1])/0.4; return lin,quad
print("\nE3 — x per z-bin, linear 0.5-mag slope vs quadratic derivative at the edge, and the β̂/β_inj each gives (β = 0.01, 13 M):")
rng=np.random.default_rng(5761); d1=rng.normal(size=3); d1/=np.linalg.norm(d1)
for law in ("pure power law (the 5757–5760 synthetic)","curved counts (broken law, x 0.6 faint / 1.2 bright, knee at 1.3)"):
    g=1/math.sqrt(1-1e-4); z=rng.gamma(3.0,0.55,size=int(13_000_000*1.05)); z=z[z<4.0][:13_000_000]; m=len(z); n=rng.normal(size=(m,3)); n/=np.linalg.norm(n,axis=1)[:,None]
    if law.startswith("pure"):
        xb=np.array(XG)[np.clip(np.searchsorted(ZEG,z,side='right')-1,0,4)]; S=(1/1.5)*rng.uniform(size=m)**(-1/xb)
    else: S=L.broken_powerlaw_flux(m,rng,1/1.5)
    mu=n@d1; delta=g*(1+0.01*mu); n=(n+((g-1)*mu+g*0.01)[:,None]*d1)/(g*(1+0.01*mu))[:,None]; S=S*delta**(1+AL); zp=(1+z)/delta-1
    cut=S>=1.0; n,zp,S=n[cut],zp[cut],S[cut]; idx=L.CELLS.index(n); print(f"   {law}:")
    tot={'lin':[], 'quad':[]}
    for i in range(5):
        sel=(zp>=ZE[i])&(zp<ZE[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask); B=L.membership_term(zp,ZE[i],ZE[i+1],sel.sum())
        xl,xq=x_two_ways(S[sel],1.0); Dn=np.linalg.norm(D); u=D/Dn; sD=math.sqrt(max(u@cov@u,0))
        for k,x in (('lin',xl),('quad',xq)):
            f=2+x*(1+AL)+B; tot[k].append((Dn/f/0.01, sD/f/0.01))
        print(f"      bin {str((ZE[i],ZE[i+1])):12} x_lin = {xl:.3f}  x_quad = {xq:.3f}  (Δ = {xq-xl:+.3f})  β̂/β: linear {tot['lin'][-1][0]:.3f} ± {tot['lin'][-1][1]:.3f}, quadratic {tot['quad'][-1][0]:.3f} ± {tot['quad'][-1][1]:.3f}")
    for k in ('lin','quad'):
        a=np.array(tot[k]); wgt=1/a[:,1]**2; print(f"      weighted mean β̂/β_inj ({k}) = {(wgt*a[:,0]).sum()/wgt.sum():.4f} ± {1/math.sqrt(wgt.sum()):.4f}")
print("\nE2 — S6 with the intrinsic amplitude DIFFERING between the cuts through the z-mix (x rises with z, so the bright cut keeps fewer high-z sources):")
wd=L.lb_to_vec(90.0,20.0); rng=np.random.default_rng(5762); d1=rng.normal(size=3); d1/=np.linalg.norm(d1); beta=0.01
z0=rng.gamma(3.0,0.55,size=2_000_000); z0=z0[z0<4]; zm=[float(np.median(z0[(z0>=ZEG[i])&(z0<ZEG[i+1])])) for i in range(5)]; wv=L.profile_w(zm)
g=1/math.sqrt(1-beta**2); z=rng.gamma(3.0,0.55,size=int(13_000_000*1.05)); z=z[z<4.0][:13_000_000]; m=len(z); n=rng.normal(size=(m,3)); n/=np.linalg.norm(n,axis=1)[:,None]
wsrc=np.asarray(wv)[np.clip(np.searchsorted(ZEG,z,side='right')-1,0,4)]; amp=0.05*wsrc; keep=rng.uniform(size=m)<(1+amp*(n@wd))/(1+amp); n=n[keep]; z=z[keep]; wsrc=wsrc[keep]; m=len(z)
xb=np.array(XG)[np.clip(np.searchsorted(ZEG,z,side='right')-1,0,4)]; S=(1/1.5)*rng.uniform(size=m)**(-1/xb)
mu=n@d1; delta=g*(1+beta*mu); n=(n+((g-1)*mu+g*beta)[:,None]*d1)/(g*(1+beta*mu))[:,None]; S=S*delta**(1+AL); zp=(1+z)/delta-1
cut=S>=1.0; n,zp,S,wsrc=n[cut],zp[cut],S[cut],wsrc[cut]; idx=L.CELLS.index(n); out={}
for lab,lim in (("deep",1.0),("bright",10**0.2)):
    sel=S>=lim; cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask); xl,xq=x_two_ways(S[sel],lim); B=L.membership_term(zp[sel],0.0,np.inf,sel.sum())
    out[lab]=dict(D=D,cov=cov,x=xq,B=B,sel=sel,wmean=float(wsrc[sel].mean()),N=int(cnt[mask].sum()))
dp,br=out['deep'],out['bright']; dD=dp['D']-br['D']; add=dp['sel']&~br['sel']; cnt=np.bincount(idx[add],minlength=L.CELLS.n); cnt[~mask]=0; Da,cova=L.dipole_ls(cnt,mask); fr=cnt[mask].sum()/dp['N']; covd=fr**2*(cova+br['cov'])
coef=(dp['x']-br['x'])*(1+AL)+(dp['B']-br['B']); wperp=wd-(wd@d1)*d1; wperp/=np.linalg.norm(wperp); sperp=math.sqrt(max(wperp@covd@wperp,1e-30))
dA_pred=0.05*(dp['wmean']-br['wmean'])           # the intrinsic difference from the profile's z-mix, predicted from each cut's own dN/dz
leak_before=(dD@wperp)/sperp; leak_after=((dD-dA_pred*wd)@wperp)/sperp
print(f"   x_quad deep {dp['x']:.3f}, bright {br['x']:.3f}; ⟨w⟩ deep {dp['wmean']:.4f}, bright {br['wmean']:.4f} -> predicted ΔA = A(⟨w⟩_deep − ⟨w⟩_bright) = {dA_pred:+.5f} along ŵ")
print(f"   ΔD along ŵ⊥: {dD@wperp:+.5f} (σ {sperp:.5f}) -> leak BEFORE the ΔA correction {leak_before:+.2f}σ; AFTER subtracting ΔA·ŵ {leak_after:+.2f}σ;  kinematic part |ΔD − ΔA ŵ| = {np.linalg.norm(dD-dA_pred*wd):.5f} vs coef·β = {abs(coef*beta):.5f} (coef {coef:+.3f})")
json.dump({"leak_before":leak_before,"leak_after":leak_after,"dA_pred":dA_pred},open(f".record_{TOY}.json","w"),indent=1)
