#!/usr/bin/env python3
"""Toy 5760 — R148 E1 (combined σ_β from the joint two-channel fit, 20 seeds) + E2 (S6, the flux-cut derivative). Prereg 5aa35790. Synthetic only."""
import math, json
import numpy as np
import r145_eb_lib as L
from r145_eb_lib import C_KMS
print(f"lib hash {L.lib_hash()}")
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
ZE=[0.0,0.8,1.3,1.8,2.4,np.inf]; ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; S_LIM=1.0
mask=L.make_mask(30.0); vc=L.lb_to_vec(264.02,48.25); bc=369.82/C_KMS
def count_rows(n,zp,S,S_lim=S_LIM):
    idx=L.CELLS.index(n); rows=[]
    for i in range(5):
        sel=(zp>=ZE[i])&(zp<ZE[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask)
        x=L.measure_x(S[sel],S_lim); B=L.membership_term(zp,ZE[i],ZE[i+1],sel.sum()); rows.append(dict(D=D,cov=cov,f=2+x*(1+AL)+B,x=x,B=B,zmed=float(np.median(zp[sel])),N=int(cnt[mask].sum())))
    return rows,idx
def z_moments(idx,zp,S,variant):
    if variant=='full':
        R,CR=L.redshift_dipole(idx,zp,mask); return [R],[CR],[1+float(zp.mean())]
    q=np.quantile(S,[0,0.2,0.4,0.6,0.8,1.0]); q[-1]=np.inf; Rs=[];CRs=[];gs=[]
    for k in range(5):
        sel=(S>=q[k])&(S<q[k+1]); R,CR=L.redshift_dipole(idx[sel],zp[sel],mask); Rs.append(R); CRs.append(CR); gs.append(1+float(zp[sel].mean()))
    return Rs,CRs,gs
print("\nE1 — joint two-channel fit for one βû, CMB boost, Quaia-like depth, 20 seeds:")
res={'full':[],'quant':[],'count':[]}
for sd in range(20):
    rng=np.random.default_rng(1000+sd); n,z,zp,S=L.synth_sky_full(4_000_000,bc,vc,rng,ZEG,XG,AL,S_LIM,sigma_z=0.01)
    rows,idx=count_rows(n,zp,S); w=L.profile_w([r['zmed'] for r in rows])
    for variant in ('full','quant'):
        Rs,CRs,gs=z_moments(idx,zp,S,variant); b,a,cov=L.joint_two_channel([r['D'] for r in rows],[r['cov'] for r in rows],[r['f'] for r in rows],w,Rs,CRs,gs)
        be,sb,u,A,sA=L.fit_summary(b,a,cov); res[variant].append((be,sb,math.degrees(math.acos(np.clip(u@vc,-1,1)))))
    b,a,cov=L.joint_two_channel([r['D'] for r in rows],[r['cov'] for r in rows],[r['f'] for r in rows],w,[],[],[]); be,sb,u,A,sA=L.fit_summary(b,a,cov); res['count'].append((be,sb,0))
    if sd<3: print(f"   seed {sd}: N = {sum(r['N'] for r in rows):,};  count-only {res['count'][-1][0]*C_KMS:6.0f} ± {res['count'][-1][1]*C_KMS:4.0f};  +full-sample z {res['full'][-1][0]*C_KMS:6.0f} ± {res['full'][-1][1]*C_KMS:4.0f} km/s ({res['full'][-1][2]:.0f}° off);  +flux-quantile z {res['quant'][-1][0]*C_KMS:6.0f} ± {res['quant'][-1][1]*C_KMS:4.0f} ({res['quant'][-1][2]:.0f}° off)")
summ={}
for variant in ('count','full','quant'):
    a=np.array(res[variant]); q_sig=a[:,1].mean()*C_KMS; scat=a[:,0].std(ddof=1)*C_KMS; ratio=a[:,0].mean()/bc; sm=(a[:,1].mean()/bc)/math.sqrt(20)
    summ[variant]=(q_sig,scat,ratio,sm); print(f"   {variant:6}: quoted σ_β c = {q_sig:5.0f} km/s (seed spread of the quote {a[:,1].std(ddof=1)*C_KMS:.0f});  scatter of β̂ over seeds = {scat:5.0f} km/s (ratio {scat/q_sig:.2f});  mean β̂/β_inj = {ratio:.3f} (σ_mean {sm:.3f});  mean direction offset {a[:,2].mean():.0f}°")
sc("P1", all(120<=summ[v][0]<=210 for v in ('full','quant')), True, f"combined σ_β c = {summ['full'][0]:.0f} (full-sample z) / {summ['quant'][0]:.0f} (flux quantiles) km/s — vs Cal's 4.4 bar 185: {'A/B-capable' if summ['full'][0]<185 else 'C by construction'} (full), {'A/B-capable' if summ['quant'][0]<185 else 'C by construction'} (quantiles)")
sc("P2", all(0.7<=summ[v][1]/summ[v][0]<=1.35 for v in ('full','quant')), True, f"quoted σ_β calibrated: scatter/quote = {summ['full'][1]/summ['full'][0]:.2f} (full), {summ['quant'][1]/summ['quant'][0]:.2f} (quantiles)")
sc("P3", all(abs(summ[v][2]-1)<=2.5*summ[v][3] for v in ('full','quant')), True, f"mean β̂/β_inj = {summ['full'][2]:.3f} (full), {summ['quant'][2]:.3f} (quantiles), σ_mean ≈ {summ['full'][3]:.3f}")
print("\nE2 — S6, the flux-cut derivative: broken power law (x 0.6 faint / 1.2 bright, knee 1.3), boost + intrinsic A = 0.05 toward (90°, 20°):")
wd=L.lb_to_vec(90.0,20.0)
def s6(beta,vhat,Ngen,rng,label):
    z0=rng.gamma(3.0,0.55,size=2_000_000); z0=z0[z0<4]; zm=[float(np.median(z0[(z0>=ZEG[i])&(z0<ZEG[i+1])])) for i in range(5)]; W=(ZEG,L.profile_w(zm))
    # generate with the standard sampler, then REPLACE fluxes by the broken law before the boost: re-implement the pipeline inline
    g=1/math.sqrt(1-beta**2); z=rng.gamma(3.0,0.55,size=int(Ngen*1.05)); z=z[z<4.0][:Ngen]; m=len(z)
    n=rng.normal(size=(m,3)); n/=np.linalg.norm(n,axis=1)[:,None]
    ed,wv=W; amp=0.05*np.asarray(wv)[np.clip(np.searchsorted(ed,z,side='right')-1,0,4)]; keep=rng.uniform(size=m)<(1+amp*(n@wd))/(1+amp); n=n[keep]; z=z[keep]; m=len(z)
    S=L.broken_powerlaw_flux(m,rng,S_LIM/1.5); zp=z.copy()
    mu=n@vhat; delta=g*(1+beta*mu); n=(n+((g-1)*mu+g*beta)[:,None]*vhat)/(g*(1+beta*mu))[:,None]; S=S*delta**(1+AL); zp=(1+z)/delta-1
    zp=zp+rng.normal(size=m)*0.01*(1+zp); cut=S>=S_LIM; n,zp,S=n[cut],zp[cut],S[cut]
    idx=L.CELLS.index(n); out={}
    for lab,lim in (("deep G<20.5",1.0),("bright G<20.0",10**0.2)):
        sel=S>=lim; cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask); x=L.measure_x(S[sel],lim)
        B=L.membership_term(zp[sel],0.0,np.inf,sel.sum()); out[lab]=dict(D=D,cov=cov,x=x,B=B,N=int(cnt[mask].sum()),sel=sel)
    dp,br=out["deep G<20.5"],out["bright G<20.0"]; dD=dp['D']-br['D']
    # covariance of the difference from the NON-SHARED sources: D_deep = (N_b D_b + N_add D_add)/N_deep -> dD = (N_add/N_deep)(D_add - D_b)
    add=dp['sel']&~br['sel']; cnt=np.bincount(idx[add],minlength=L.CELLS.n); cnt[~mask]=0; Da,cova=L.dipole_ls(cnt,mask); fr=cnt[mask].sum()/dp['N']
    covd=fr**2*(cova+br['cov']); coef=(dp['x']-br['x'])*(1+AL)+(dp['B']-br['B']); pred=coef*beta*vhat
    dn=np.linalg.norm(dD); u=dD/dn; s_par=math.sqrt(max(u@covd@u,0)); ratio=dn/abs(coef*beta); sr=s_par/abs(coef*beta)
    ang=math.degrees(math.acos(np.clip(u@vhat,-1,1))); _,_,cone=L.neyman(dn,covd,u); wperp=wd-(wd@vhat)*vhat; wperp/=np.linalg.norm(wperp); leak=(dD@wperp)/math.sqrt(max(wperp@covd@wperp,1e-30))
    print(f"   {label}: x(deep) = {dp['x']:.3f}, x(bright) = {br['x']:.3f}, ΔB = {dp['B']-br['B']:+.4f}, coefficient Δ(x(1+α)) + ΔB = {coef:+.3f};  |ΔD| = {dn:.5f} vs predicted {abs(coef*beta):.5f} (ratio {ratio:.3f} ± {sr:.3f});  direction {ang:.1f}° from û (cone95 {cone:.0f}°);  leak along ŵ⊥ = {leak:+.2f}σ;  S/N = {abs(coef*beta)/s_par:.2f}")
    return ratio,sr,ang,cone,leak,abs(coef*beta)/s_par
rng=np.random.default_rng(5760); d1=rng.normal(size=3); d1/=np.linalg.norm(d1)
r4=s6(0.01,d1,13_000_000,rng,"β=0.01, 13 M")
sc("P4", abs(r4[0]-1)<=2.5*r4[1] and r4[2]<=r4[3] and abs(r4[4])<2, True, f"derivative isolates the boost: amplitude ratio {r4[0]:.3f} ± {r4[1]:.3f}, direction {r4[2]:.1f}° inside cone {r4[3]:.0f}°, intrinsic leak {r4[4]:+.2f}σ")
r5=s6(bc,vc,4_000_000,rng,"CMB β, Quaia depth")
print(f"   P5 (reported): at Quaia depth the whole-sample derivative has S/N = {r5[5]:.2f}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({"lib":L.lib_hash(),"E1":{k:list(map(float,v)) for k,v in summ.items()},"S6_13M":list(map(float,r4)),"S6_quaia":list(map(float,r5))},open(".record_5760.json","w"),indent=1)
