#!/usr/bin/env python3
"""Toy 5759 — R147 E2 (the redshift channel, v1.1 4.5) + E3 (the null bin, S5). Prereg e3d1e2d6. Synthetic only; no catalogue."""
import math, json
import numpy as np
from scipy.stats import chi2
import r145_eb_lib as L
from r145_eb_lib import C_KMS
print(f"lib hash {L.lib_hash()}")
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
ZE=[0.0,0.8,1.3,1.8,2.4,np.inf]; ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; S_LIM=1.0
mask=L.make_mask(30.0); CHI=L.chi_table(); rng=np.random.default_rng(5759)
def channels(n,zp,S,label):
    """both channels per bin + Cal's joint fits; returns rows, w, fits."""
    idx=L.CELLS.index(n); rows=[]
    for i in range(5):
        sel=(zp>=ZE[i])&(zp<ZE[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0
        D,cov=L.dipole_ls(cnt,mask); x=L.measure_x(S[sel],S_LIM); B=L.membership_term(zp,ZE[i],ZE[i+1],sel.sum()); f=2+x*(1+AL)+B
        g=L.g_factor(zp,zp[sel],ZE[i],ZE[i+1]); R,covR=L.redshift_dipole(idx[sel],zp[sel],mask)
        rows.append(dict(bin=(ZE[i],ZE[i+1]),N=int(cnt[mask].sum()),x=x,B=B,f=f,g=g,zmed=float(np.median(zp[sel])),s=float(np.std(zp[sel])),D=D,cov=cov,R=R,covR=covR))
    w=L.profile_w([r['zmed'] for r in rows])
    bC,aC,covC,chiC=L.joint_fit([r['D'] for r in rows],[r['cov'] for r in rows],[r['f'] for r in rows],w)
    bZ,aZ,covZ,chiZ=L.joint_fit([-r['R'] for r in rows],[r['covR'] for r in rows],[r['g'] for r in rows],w)   # -R = g beta u
    fc=L.fit_summary(bC,aC,covC); fz=L.fit_summary(bZ,aZ,covZ)
    print(f"   {label}: COUNT channel β̂c = {fc[0]*C_KMS:7.1f} ± {fc[1]*C_KMS:5.1f} km/s, A = {fc[3]:.4f} ± {fc[4]:.4f}, χ² {chiC:.1f}/9 | REDSHIFT channel β̂_z c = {fz[0]*C_KMS:7.1f} ± {fz[1]*C_KMS:5.1f} km/s, A_z = {fz[3]:.4f} ± {fz[4]:.4f}, χ² {chiZ:.1f}/9")
    return rows,w,(fc,covC),(fz,covZ)
def landing_prime(fc,covC,fz,covZ):
    """4.5: A' iff |β_z − β| ≤ 2 sqrt(σ_z² + σ²) AND each direction inside the other's 95% region (approximated by the 95% cone from the perpendicular covariance)."""
    db=abs(fz[0]-fc[0])/math.sqrt(fz[1]**2+fc[1]**2); ang=math.degrees(math.acos(np.clip(fc[2]@fz[2],-1,1)))
    def cone(fit,cov):
        u=fit[2]; P=np.eye(3)-np.outer(u,u); Cp=P@cov[:3,:3]@P; ev=np.linalg.eigvalsh(Cp)[1:]; return math.degrees(math.sqrt(5.99*ev.mean())/fit[0])
    c1,c2=cone(fc,covC),cone(fz,covZ); ok=db<=2 and ang<=c1 and ang<=c2
    return ('A′' if ok else 'C′'),db,ang,c1,c2
# ---------------- E2 P1: g_i at β = 0.01, 13 M ----------------
print("\nE2 P1 — g_i and the redshift-channel amplitude at β = 0.01, 13 M generated (no z errors):")
d1=rng.normal(size=3); d1/=np.linalg.norm(d1); n,z,zp,S=L.synth_sky_full(13_000_000,0.01,d1,rng,ZEG,XG,AL,S_LIM)
rows1,w1,(fc1,cC1),(fz1,cZ1)=channels(n,zp,S,"β=0.01")
ok1=True; print(f"   {'bin':12}{'N':>9}{'g_meas':>8}{'|R|/β':>8}{'β̂_z/β':>9}{'σ':>7}{'dir off':>9}")
for r in rows1:
    Rn=np.linalg.norm(r['R']); u=-r['R']/Rn; sR=math.sqrt(max(u@r['covR']@u,0)); ratio=Rn/r['g']/0.01; sig=sR/r['g']/0.01
    ang=math.degrees(math.acos(np.clip(u@d1,-1,1))); ok1&=abs(ratio-1)<=2.5*sig
    print(f"   {str(r['bin']):12}{r['N']:9d}{r['g']:8.3f}{Rn/0.01:8.3f}{ratio:9.4f}{sig:7.4f}{ang:8.2f}°")
sc("P1", ok1, True, "β̂_z/β_inj within ±2.5σ of 1 in every bin — g_i as derived is the redshift channel's factor")
# ---------------- E2 P2/P3: CMB β at Quaia depth with z errors ----------------
print("\nE2 P2/P3 — CMB boost, Quaia-like depth, photo-z errors 0.01(1+z):")
vc=L.lb_to_vec(264.02,48.25); bc=369.82/C_KMS
n,z,zp,S=L.synth_sky_full(4_000_000,bc,vc,rng,ZEG,XG,AL,S_LIM,sigma_z=0.01)
rows2,w2,(fc2,cC2),(fz2,cZ2)=channels(n,zp,S,"CMB β ")
hits_v=0; hits_d=0; sv=[]
print(f"   {'bin':12}{'N':>9}{'g':>7}{'v̂_z [km/s]':>12}{'σ_v':>6}{'Neyman 95% v':>17}{'dir off':>9}{'cone95':>8}")
for r in rows2:
    Rn=np.linalg.norm(r['R']); u=-r['R']/Rn; Dlo,Dhi,cone=L.neyman(Rn,r['covR'],u); v=Rn/r['g']*C_KMS; s=math.sqrt(max(u@r['covR']@u,0))/r['g']*C_KMS
    lo,hi=Dlo/r['g']*C_KMS,Dhi/r['g']*C_KMS; ang=math.degrees(math.acos(np.clip(u@vc,-1,1))); hits_v+=(lo<=369.82<=hi); hits_d+=(ang<=cone); sv.append(s)
    print(f"   {str(r['bin']):12}{r['N']:9d}{r['g']:7.3f}{v:12.1f}{s:6.0f}   [{lo:5.0f},{hi:5.0f}]   {ang:6.1f}°{cone:8.1f}°")
print(f"   per-bin σ_v (redshift channel) = {[round(s) for s in sv]} km/s — Cal's envelope 55–110; my prereg band [40, 150]")
sc("P2", hits_v>=4 and hits_d>=4 and all(40<=s<=150 for s in sv), True, f"CMB β recovered in {hits_v}/5 bins (v) and {hits_d}/5 (direction) at Quaia depth; σ_v in band")
land,db,ang,c1,c2=landing_prime(fc2,cC2,fz2,cZ2)
sc("P3", land=='A′', True, f"boosted sky, no contaminant: Landing {land} — |Δβ| = {db:.2f}σ_comb, directions {ang:.1f}° apart vs cones {c1:.1f}° (count) / {c2:.1f}° (redshift)")
# ---------------- E2 P4: bulk-flow negative control ----------------
print("\nE2 P4 — NEGATIVE control: local bulk flow 600 km/s e^(−z/0.3) toward (200°, −30°), no observer boost:")
bd=L.lb_to_vec(200.0,-30.0); n,z,zp,S=L.synth_sky_full(4_000_000,0.0,None,rng,ZEG,XG,AL,S_LIM,sigma_z=0.01,bulk_v0=600.0,bulk_dir=bd)
rows3,w3,(fc3,cC3),(fz3,cZ3)=channels(n,zp,S,"bulk  ")
land3,db3,ang3,c13,c23=landing_prime(fc3,cC3,fz3,cZ3)
print(f"   count channel reads a 'boost' of {fc3[0]*C_KMS:.0f} ± {fc3[1]*C_KMS:.0f} km/s toward {tuple(round(float(x),1) for x in L.vec_to_lb(fc3[2]))}; redshift channel {fz3[0]*C_KMS:.0f} ± {fz3[1]*C_KMS:.0f} km/s toward {tuple(round(float(x),1) for x in L.vec_to_lb(fz3[2]))}; injected flow toward (200, −30)")
sc("P4", land3=='C′', True, f"bulk flow lands {land3}: |Δβ| = {db3:.2f}σ_comb, directions {ang3:.1f}° apart vs cones {c13:.1f}°/{c23:.1f}°" + ("" if land3=='C′' else " — the negative control FAILS at this amplitude: a 600 km/s local flow passes A′"))
# ---------------- E3 S5: the null bin ----------------
print("\nE3 S5 — null bin: CMB boost + intrinsic dipole A = 0.05 with Cal's profile toward (90°, 20°), binned on z_obs:")
wd=L.lb_to_vec(90.0,20.0); res5={}
z0=rng.gamma(3.0,0.55,size=2_000_000); z0=z0[z0<4]; zmed0=[float(np.median(z0[(z0>=ZEG[i])&(z0<ZEG[i+1])])) for i in range(5)]; W_INJ=(ZEG,L.profile_w(zmed0))
print(f"   injected intrinsic profile: Cal's w_i at the generating bin medians {[round(z,2) for z in zmed0]} -> w = {[round(float(x),3) for x in W_INJ[1]]}, A = 0.05 per bin")
for lab,Ngen in (("13 M",13_000_000),("Quaia depth",4_000_000)):
    n,z,zp,S=L.synth_sky_full(Ngen,bc,vc,rng,ZEG,XG,AL,S_LIM,sigma_z=0.01,A_int=0.05,int_dir=wd,chi_tab=CHI,piecewise_w=W_INJ)
    rows,w,(fc,cC),(fz,cZ)=channels(n,zp,S,lab)
    r5=rows[4]; D5=r5['D']; cov5=r5['cov']; D5n=np.linalg.norm(D5); u5=D5/D5n; _,_,cone5=L.neyman(D5n,cov5,u5)
    ang5=math.degrees(math.acos(np.clip(u5@wd,-1,1))); kin=abs(r5['f'])*bc; Aw5=0.05*w[4]
    Adb=math.sqrt(max(D5n**2-np.trace(cov5),0))/w[4]; sA=math.sqrt(max(u5@cov5@u5,0))/w[4]
    # other bins: residual after subtracting fitted boost (count channel) and fitted intrinsic
    b,a,cov6,_=L.joint_fit([r['D'] for r in rows],[r['cov'] for r in rows],[r['f'] for r in rows],w)
    pv=[]
    for i,r in enumerate(rows[:4]):
        e=r['D']-r['f']*b-w[i]*a; pv.append(1-chi2.cdf(e@np.linalg.solve(r['cov'],e),3))
    print(f"   {lab}: null bin f₅+B₅ = {r5['f']:+.3f} (kinematic share {kin:.5f} vs A w₅ = {Aw5:.5f}, ratio {kin/Aw5:.2f}); D₅ toward {tuple(round(float(x),1) for x in L.vec_to_lb(D5))}, {ang5:.1f}° from ŵ, cone95 {cone5:.1f}°; Â_null = {Adb:.4f} ± {sA:.4f} (injected 0.0500, {abs(Adb-0.05)/sA:.1f}σ); other bins' residual p = {[round(p,3) for p in pv]}")
    res5[lab]=(ang5<=cone5, kin<0.2*Aw5, abs(Adb-0.05)<=2.5*sA, min(pv)>0.01, Adb, sA)
ok5=all(res5["13 M"][:4])
sc("P5", ok5, True, f"S5 at 13 M: direction/kinematic-share/Â_null/other-bins = {res5['13 M'][:4]}; at Quaia depth Â_null = {res5['Quaia depth'][4]:.4f} ± {res5['Quaia depth'][5]:.4f}")
# ---------------- ADDENDUM (5fd27764): the redshift channel binned on observed FLUX ----------------
print("\nADDENDUM P6/P7 — redshift channel in five FLUX-quantile bins (a boost shifts flux by only ~0.25 %):")
def flux_channel(n,zp,S,beta,vhat,label,depth=False):
    idx=L.CELLS.index(n); q=np.quantile(S,[0,0.2,0.4,0.6,0.8,1.0]); q[-1]=np.inf; rows=[]
    for i in range(5):
        sel=(S>=q[i])&(S<q[i+1]); m=float(zp[sel].mean()); g=1+m; R,covR=L.redshift_dipole(idx[sel],zp[sel],mask)
        Rn=np.linalg.norm(R); u=-R/Rn; sR=math.sqrt(max(u@covR@u,0)); v=Rn/g*C_KMS; sv=sR/g*C_KMS; ang=math.degrees(math.acos(np.clip(u@vhat,-1,1)))
        Dlo,Dhi,cone=L.neyman(Rn,covR,u) if depth else (0,0,0)
        rows.append(dict(N=int(sel.sum()),m=m,g=g,gmeas=Rn/beta,v=v,sv=sv,ang=ang,lo=Dlo/g*C_KMS,hi=Dhi/g*C_KMS,cone=cone,R=R,covR=covR))
        print(f"   {label} flux bin {i+1}: N {rows[-1]['N']:8d}  1+m = {g:.3f}  |R|/β = {Rn/beta:.3f}  v̂_z = {v:7.1f} ± {sv:5.1f} km/s  dir off {ang:5.1f}°"+(f"  Neyman [{Dlo/g*C_KMS:5.0f},{Dhi/g*C_KMS:5.0f}] cone {cone:5.1f}°" if depth else ""))
    return rows
n,z,zp,S=L.synth_sky_full(13_000_000,0.01,d1,rng,ZEG,XG,AL,S_LIM); rf1=flux_channel(n,zp,S,0.01,d1,"β=0.01")
sc("P6a", all(abs(r['gmeas']/r['g']-1)<0.10 for r in rf1), True, f"g_i(flux bins) = 1 + m_i within 10 %: measured/predicted = {[round(r['gmeas']/r['g'],3) for r in rf1]}")
n,z,zp,S=L.synth_sky_full(4_000_000,bc,vc,rng,ZEG,XG,AL,S_LIM,sigma_z=0.01); rf2=flux_channel(n,zp,S,bc,vc,"CMB β ",depth=True)
svf=[r['sv'] for r in rf2]; print(f"   per-bin σ_v (redshift channel, flux bins, Quaia depth) = {[round(x) for x in svf]} km/s — Cal's envelope 55–110")
sc("P6b", all(40<=x<=150 for x in svf), True, f"σ_v in [40, 150] km/s in every flux bin")
hv=sum(r['lo']<=369.82<=r['hi'] for r in rf2); hd=sum(r['ang']<=r['cone'] for r in rf2)
# joint: count channel in z bins (rows from the same sky) + redshift channel in flux bins, same profile model on the flux bins' median z
idx=L.CELLS.index(n); rowsC=[]
for i in range(5):
    sel=(zp>=ZE[i])&(zp<ZE[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask); x=L.measure_x(S[sel],S_LIM); B=L.membership_term(zp,ZE[i],ZE[i+1],sel.sum())
    rowsC.append(dict(D=D,cov=cov,f=2+x*(1+AL)+B,zmed=float(np.median(zp[sel]))))
wC=L.profile_w([r['zmed'] for r in rowsC]); bC_,aC_,cC_,_=L.joint_fit([r['D'] for r in rowsC],[r['cov'] for r in rowsC],[r['f'] for r in rowsC],wC); fcC=L.fit_summary(bC_,aC_,cC_)
q=np.quantile(S,[0,0.2,0.4,0.6,0.8,1.0]); q[-1]=np.inf; zmf=[float(np.median(zp[(S>=q[i])&(S<q[i+1])])) for i in range(5)]; wZ=L.profile_w(zmf)
bZ_,aZ_,cZ_,_=L.joint_fit([-r['R'] for r in rf2],[r['covR'] for r in rf2],[r['g'] for r in rf2],wZ); fzZ=L.fit_summary(bZ_,aZ_,cZ_)
landF,dbF,angF,c1F,c2F=landing_prime(fcC,cC_,fzZ,cZ_)
print(f"   joint: COUNT (z bins) β̂c = {fcC[0]*C_KMS:.0f} ± {fcC[1]*C_KMS:.0f} km/s; REDSHIFT (flux bins) β̂_z c = {fzZ[0]*C_KMS:.0f} ± {fzZ[1]*C_KMS:.0f} km/s toward {tuple(round(float(x),1) for x in L.vec_to_lb(fzZ[2]))} (CMB (264.0, 48.2)); |Δβ| = {dbF:.2f}σ, directions {angF:.1f}° apart, cones {c1F:.0f}°/{c2F:.0f}° -> {landF}")
sc("P7", hv>=4 and hd>=4 and landF=='A′', True, f"CMB β recovered in {hv}/5 flux bins (v), {hd}/5 (direction); boosted sky lands {landF}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({"lib":L.lib_hash(),"g_13M":[r['g'] for r in rows1],"sigma_v_z":sv,"landing_boosted":land,"landing_bulk":land3,"S5":{k:list(map(float,v[4:]))+list(map(bool,v[:4])) for k,v in res5.items()}},open(".record_5759.json","w"),indent=1)
