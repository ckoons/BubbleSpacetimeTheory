#!/usr/bin/env python3
"""Toy 5758 — R146 E1 (prereg 2b6d0936): the observed-redshift bin-membership term T_i in the per-bin model, and control S4 —
a boosted synthetic sky binned on OBSERVED redshift under Cal's frozen-v1 bins / mask / model, fitted with and without the term.
Synthetic only. Library: play/r145_eb_lib.py (hash printed)."""
import math, json
import numpy as np
from scipy.stats import chi2, gamma as gamma_dist
import r145_eb_lib as L
from r145_eb_lib import C_KMS
print(f"lib hash {L.lib_hash()}")
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
ZE=[0.0,0.8,1.3,1.8,2.4,np.inf]; ZE_GEN=[0.0,0.8,1.3,1.8,2.4,4.0]; ALPHA=1.0; S_LIM=1.0; S_MIN=S_LIM/1.5
xz=lambda z: np.minimum(0.9+0.1*np.asarray(z),1.3)            # smooth x(z): no artificial jumps in dN/dz at the edges
mask=L.make_mask(30.0); print(f"mask |b|>30 + LMC/SMC: {mask.sum()} of {L.CELLS.n} cells, {100*L.CELLS.area[mask].sum()/(4*math.pi):.1f}% of sky")
# ---- analytic T_i from the generating dN/dz (gamma(3,0.55) truncated at 4, times the flux-cut fraction 1.5^-x(z)) ----
zz=np.linspace(0,4,4001); pdf=gamma_dist.pdf(zz,3.0,scale=0.55)*1.5**(-xz(zz)); pdf/=np.trapz(pdf,zz)
def n_of(z): return float(np.interp(z,zz,pdf)) if z<4 else 0.0
T_an=[]
for i in range(5):
    z1,z2=ZE[i],ZE[i+1]; Ni=np.trapz(pdf[(zz>=z1)&(zz<min(z2,4))],zz[(zz>=z1)&(zz<min(z2,4))])
    T_an.append(((1+z2)*n_of(z2) if np.isfinite(z2) else 0.0)-(1+z1)*n_of(z1))
    T_an[-1]/=Ni
print("analytic T_i from the generating dN/dz:",[round(t,4) for t in T_an])
def run(beta,vhat,N_gen,rng,label,nboot_cov='ls'):
    n,z,zo,S=L.synth_sky(N_gen,beta,vhat,rng,ZE_GEN,[0.9,1.0,1.1,1.2,1.3],ALPHA,S_LIM,S_MIN,'gamma',boost_z=True)
    # per-bin x from the generating law is replaced by MEASURED x in the OBSERVED bin, as the freeze prescribes
    idx=L.CELLS.index(n); rows=[]
    for i in range(5):
        sel=(zo>=ZE[i])&(zo<ZE[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0
        D,cov=L.dipole_ls(cnt,mask); x=L.measure_x(S[sel],S_LIM); f=2+x*(1+ALPHA); N=int(cnt[mask].sum())
        T=L.membership_term(zo,ZE[i],ZE[i+1],sel.sum())            # from the observed-z histogram of the whole sample, edge windows
        zmed=float(np.median(zo[sel]))
        rows.append(dict(bin=(ZE[i],ZE[i+1]),N=N,x=x,f=f,T=T,zmed=zmed,D=D,cov=cov))
    w=L.profile_w([r['zmed'] for r in rows])
    out={}
    for tag,coef in (("with T",[r['f']+r['T'] for r in rows]),("without T",[r['f'] for r in rows])):
        b,a,cov6,chi2v=L.joint_fit([r['D'] for r in rows],[r['cov'] for r in rows],coef,w); be,sb,u,A,sA=L.fit_summary(b,a,cov6)
        # per-bin residual test against the INJECTED boost (Landing A's third clause, with the truth in place of the CMB)
        pv=[]
        for i,r in enumerate(rows):
            res=r['D']-coef[i]*beta*vhat-w[i]*a; pv.append(1-chi2.cdf(res@np.linalg.solve(r['cov'],res),3))
        ang=math.degrees(math.acos(np.clip(u@vhat,-1,1)))
        out[tag]=dict(beta=be,sb=sb,ratio=be/beta,A=A,sA=sA,ang=ang,chi2=chi2v,pmin=min(pv),coef=coef)
        print(f"   {label} [{tag:9}]: β̂c = {be*C_KMS:7.1f} ± {sb*C_KMS:5.1f} km/s (β̂/β_inj = {be/beta:.4f}), direction off {ang:5.2f}°, A = {A:.5f} ± {sA:.5f} ({A/sA:.1f}σ), χ² = {chi2v:.1f}/9, min per-bin residual p = {min(pv):.3f}")
    return rows,w,out,(n,zo,S)
rng=np.random.default_rng(5758)
print("\nRUN 1 — β = 0.01 (2998 km/s), 13 M generated, binned on z_obs:")
d1=rng.normal(size=3); d1/=np.linalg.norm(d1)
rows1,w1,out1,_=run(0.01,d1,13_000_000,rng,"β=0.01")
print(f"   {'bin':12}{'N':>9}{'x_meas':>8}{'f':>7}{'T_meas':>9}{'T_an':>9}{'T/f':>7}{'w_i':>7}")
for r,t in zip(rows1,T_an): print(f"   {str(r['bin']):12}{r['N']:9d}{r['x']:8.3f}{r['f']:7.3f}{r['T']:9.4f}{t:9.4f}{r['T']/r['f']:7.3f}{w1[rows1.index(r)]:7.3f}")
okT=all((abs(r['T']-t)/abs(t)<0.25) for r,t in zip(rows1,T_an) if abs(t)>0.05) and rows1[0]['T']>0 and rows1[4]['T']<0
sc("P1", okT, True, f"measured T_i vs analytic within 25% where |T|>0.05; signs T₁ = {rows1[0]['T']:+.3f}, T₅ = {rows1[4]['T']:+.3f}")
wi,wo=out1["with T"],out1["without T"]
mis=(not 0.97<wo['ratio']<1.03) or wo['A']>3*wo['sA'] or wo['pmin']<0.01
sc("P2", 0.97<wi['ratio']<1.03 and mis, True, f"with T: β̂/β = {wi['ratio']:.4f}; WITHOUT T: β̂/β = {wo['ratio']:.4f}, A/σ_A = {wo['A']/wo['sA']:.1f}, min p = {wo['pmin']:.4f} -> {'mis-lands' if mis else 'still lands'}")
print("\nRUN 2 — the CMB boost, Quaia-like depth (4 M generated), binned on z_obs:")
vc=L.lb_to_vec(264.02,48.25); bc=369.82/C_KMS
rows2,w2,out2,sky2=run(bc,vc,4_000_000,rng,"CMB β")
wi2=out2["with T"]; dbeta=abs(wi2['beta']-bc)/wi2['sb']
sc("P3", dbeta<=2 and wi2['pmin']>=0.01, True, f"with T at 1.3 M: |Δβ| = {dbeta:.2f}σ, σ_β c = {wi2['sb']*C_KMS:.0f} km/s (Landing-C threshold 185), min per-bin p = {wi2['pmin']:.3f}; without T: β̂/β = {out2['without T']['ratio']:.3f}")
sizes=[abs(r['T'])*bc for r in rows2]; ratios=[abs(r['T'])/r['f'] for r in rows2]
print(f"   term sizes at Quaia depth: β_CMB·|T_i| = {[f'{100*s:.3f}%' for s in sizes]} (Keeper's envelope 0.2%); |T_i|/f_i = {[round(q,3) for q in ratios]}")
sc("P4", max(sizes)<=0.003 and max(ratios)<=0.5, True, f"max β_CMB|T_i| = {100*max(sizes):.3f}%, max |T_i|/f_i = {max(ratios):.3f}")
n,zo,S=sky2; idx=L.CELLS.index(n); agree=True; line=[]
for i,r in enumerate(rows2):
    sel=(zo>=ZE[i])&(zo<ZE[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0
    Du,covu=L.dipole_unitvec(cnt,mask,1000,rng); d=r['D']-Du; s=math.sqrt(max(d@np.linalg.solve(covu,d),0)); agree&=(s<math.sqrt(chi2.ppf(0.68,3))); line.append(round(s,2))
sc("P5", agree, False, f"Cal's 4.1 unit-vector estimator (mask-mode corrected, 1000 mocks) vs LS: Mahalanobis distances per bin {line} (68% of χ²₃: 1.88)")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({"lib":L.lib_hash(),"T_an":T_an,"run1":{k:{kk:(vv if not isinstance(vv,np.ndarray) else vv.tolist()) for kk,vv in v.items()} for k,v in out1.items()},"rows1":[{k:(v if not isinstance(v,np.ndarray) else v.tolist()) for k,v in r.items()} for r in rows1],"run2":{k:{kk:(vv if not isinstance(vv,np.ndarray) else vv.tolist()) for kk,vv in v.items()} for k,v in out2.items()},"rows2":[{k:(v if not isinstance(v,np.ndarray) else v.tolist()) for k,v in r.items()} for r in rows2]},open(".record_5758.json","w"),indent=1,default=float)
