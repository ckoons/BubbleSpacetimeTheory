#!/usr/bin/env python3
"""Toy 5763 — R152 E1 (K1907 @Elie): the synthetic landing fractions under v1.5's Section 5, on my own instrument, P1 true and no boost.
Two instruments, in order. (1) FAST: Gaussian draws b̂ ~ N(b_true, σ²·1) at σ_β c = 166 km/s, 200,000 draws per arm — the same population
Keeper's instrument drew, written independently (no import of his code for the numbers; his land_v15 is called once per draw-set only as a
CROSS-CHECK that the two rule implementations agree on identical inputs). (2) SKY: full synthetic Quaia (G < 20.5 depth, 913,899 in the mask,
σ_z = 0.04(1+z), five observed-z bins, joint two-channel fit of 5760/5762 — the retained lib), N_SEED seeds per arm, boost injected =
369.82 km/s toward (264.02, 48.25); arms: P1 true (A_int = 0 and 0.05), no boost (A_int = 0 and 0.05). Hatch checks PASS by construction on a
synthetic sky (no systematics are injected), so Section 5's B requires only χ²₃ ≥ 14.156 here.
Section 5 (v1.5, K1907 declared; Cal's hash pending): A = χ²₃(b,b_CMB) ≤ 7.815 AND Δχ² = χ²₃(b,0) − χ²₃(b,b_CMB) ≥ 3.84 (AND per-bin p ≥ 0.01 AND A′);
B = χ²₃(b,b_CMB) ≥ 14.156 (+ hatch); C otherwise. 4.4's computable triggers are ALSO measured on the sky arms: σ_β ≥ β_CMB/2; the 95 %
positional region of û > 25 % of the sphere (EXACT: profile-χ² over β ≥ 0 on the 3,616 equal-area cells, region = cells with χ² ≤ 5.991);
the profile-alternative fit moving β by > 2σ_β; C′ (A′ of 4.5(a): count-only vs redshift-only β within 2σ and each direction inside the other's
95 % region). The 4.4a null-bin check (top bin) and Landing A's per-bin residual test (D_i − a w_i − f_i b_CMB, χ²₃ p ≥ 0.01, non-null bins)
are computed from the synthetic sky's own measured f_i.
PREDICTIONS, σ printed BEFORE the band, bands = ±2.5σ of the test's own binomial σ (the 09-14 rule):
 P1 FAST P1-true: A fraction = 0.57 ± 0.01 (Keeper's two-decimal report; the binomial σ at 200k is 0.001, so the band is the rounding).
 P2 FAST no-boost: B fraction = 0.12 ± 0.01; C = 0.86 ± 0.01 (same reason).
 P3 FAST P1-true under the v1.4 text (zero clause present): B fraction = 0.56 ± 0.01 (K1907's false-fire number).
 P4 SKY P1-true A_int = 0, Section 5 alone (C-triggers off, as Keeper's instrument had them): A fraction within ±2.5·√(p(1−p)/N_SEED) of the FAST
    value at the SKY arm's OWN mean σ_β (the fast instrument re-run at that σ) — the sky's σ_β need not be 166 exactly (5762: 166 mean).
 P5 SKY no-boost A_int = 0, Section 5 alone: B fraction within ±2.5·binomial σ of the FAST value at the arm's own σ_β.
 P6 SKY P1-true A_int = 0: mean σ_β c within 166 ± 2.5·(seed spread/√N_SEED) (5762's number on the same lib, 913.5k → 913.9k).
 P7 the rule cross-check: my land() and Keeper's land_v15() agree on 100 % of the FAST draws' dicts (identical inputs; C-triggers off).
 MEASURED, not predicted (reported): the 4.4 region-trigger fraction (flat-sky estimate at σ/β = 0.449: 95 % region ≈ π·5.991·0.449² = 3.79 sr =
 30 % of the sphere — if it fires on a large fraction of P1-true seeds it is a K1907-class finding: a clause fired by a confirmation);
 the full-v1.5 landing fractions with every computable clause on; the A_int = 0.05 arms.
Memory: one sky = 573 MB peak (timed); arms run sequentially in ONE process; peak RSS printed at the end.
ADDENDUM (09:5x, after the 2-seed smoke test, prereg 1798217b unchanged): A′ sub-condition diagnostics added (amplitude test; u_z inside the count-only
region; u_c inside the redshift-only region) and the per-component σ of the fit, because C′ fired on both smoke seeds and the reason must be named. No prediction changed."""
import sys, os, math, json, time, resource, hashlib
import numpy as np
sys.path.insert(0,'.'); import r145_eb_lib as L
from r145_eb_lib import C_KMS
TOY='5763'; N_SEED=int(sys.argv[1]) if len(sys.argv)>1 else 100; NDRAW=200_000
CHI2_95, CHI2_3SIG, DCHI2_A, CHI2_2_95 = 7.815, 14.156, 3.84, 5.991
vc=L.lb_to_vec(264.02,48.25); BC=369.82/C_KMS; b_cmb=BC*vc; SIG_CMB=0.11/C_KMS          # Planck's ±0.11 km/s on the amplitude; isotropic here
print(f"toy {TOY}; lib {L.lib_hash()}; file {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; N_SEED {N_SEED}; NDRAW {NDRAW}")
def chi2(b,c,S): d=b-c; return float(d@np.linalg.solve(S,d))
def land(chi2_cmb,chi2_zero,hatch=True,triggers=(),bin_ok=True,aprime=True,v14=False,sigma_beta=None):
    """my implementation of Section 5 (v1.5; v14=True restores the zero clause of v1.4)."""
    for t in triggers:
        if t: return 'C'
    if v14 and chi2_zero<=CHI2_95 and sigma_beta is not None and sigma_beta<BC/2: return 'B' if hatch else 'C'
    if chi2_cmb>=CHI2_3SIG: return 'B' if hatch else 'C'
    if chi2_cmb<=CHI2_95 and (chi2_zero-chi2_cmb)>=DCHI2_A and bin_ok and aprime: return 'A'
    return 'C'
def frac(labels): n=len(labels); return {k:round(labels.count(k)/n,4) for k in 'ABC'}
def region_frac(b,S):
    """exact 95 % positional region of û: fraction of the 3,616 equal-area cells whose direction u has min_{β≥0} χ²(βu − b) ≤ 5.991."""
    Si=np.linalg.inv(S); U=L.CELLS.center; Sb=Si@b; num=U@Sb; den=np.einsum('ij,jk,ik->i',U,Si,U); bs=np.maximum(num/den,0.0)
    r=bs[:,None]*U-b; c2=np.einsum('ij,jk,ik->i',r,Si,r); return float((c2<=CHI2_2_95).mean())
def in_region(u,b,S):
    Si=np.linalg.inv(S); bs=max(float(u@Si@b)/float(u@Si@u),0.0); r=bs*u-b; return float(r@Si@r)<=CHI2_2_95
# ---------------- (1) FAST instrument ----------------
def fast(sigma_kms,boost,seed=0,ndraw=NDRAW):
    rng=np.random.default_rng(seed); s=sigma_kms/C_KMS; S=s*s*np.eye(3)+SIG_CMB**2*np.eye(3); Si=np.linalg.inv(S)
    bt=b_cmb if boost else np.zeros(3); bh=bt+rng.normal(size=(ndraw,3))*s
    d=bh-b_cmb; c_cmb=np.einsum('ij,jk,ik->i',d,Si,d); c_zero=np.einsum('ij,jk,ik->i',bh,Si,bh)
    lab15=[land(a,b) for a,b in zip(c_cmb,c_zero)]; lab14=[land(a,b,v14=True,sigma_beta=s) for a,b in zip(c_cmb,c_zero)]
    return frac(lab15),frac(lab14),c_cmb,c_zero
t0=time.time()
f15_p1,f14_p1,cc_p1,cz_p1=fast(166.0,True); f15_n,f14_n,cc_n,cz_n=fast(166.0,False)
print(f"\n(1) FAST at σ_β c = 166 km/s, {NDRAW:,} draws:  P1 true → v1.5 {f15_p1} | v1.4 text {f14_p1}   ||   no boost → v1.5 {f15_n} | v1.4 text {f14_n}")
# region trigger under the Gaussian population (2,000 draws each; region_frac is 3,616 cells per draw)
S166=(166.0/C_KMS)**2*np.eye(3)
reg_p1=[region_frac(b_cmb+np.random.default_rng(7).normal(size=3)*166/C_KMS if False else b, S166) for b in (b_cmb+np.random.default_rng(7).normal(size=(2000,3))*166/C_KMS)]
reg_n=[region_frac(b,S166) for b in (np.random.default_rng(8).normal(size=(2000,3))*166/C_KMS)]
print(f"    4.4 region trigger (exact 95 % region > 25 % of the sphere) in the Gaussian population: P1 true fires {np.mean(np.array(reg_p1)>0.25):.3f} (median region {np.median(reg_p1):.3f} of the sphere; at the exact CMB vector {region_frac(b_cmb,S166):.3f}); no boost fires {np.mean(np.array(reg_n)>0.25):.3f} (median {np.median(reg_n):.3f})")
# P7 cross-check against Keeper's land_v15 on identical dicts (rule agreement only)
try:
    import keeper_partB_landing as K
    base=dict(bin_resid_p=[0.5]*5,C_triggers=dict(sigma_ge_half_beta=False,region_gt_quarter_sky=False),hatch={f'H{i}':True for i in range(1,7)})
    idx=np.random.default_rng(3).choice(NDRAW,5000,replace=False)
    agree=sum(K.land_v15(dict(base,chi2_cmb=float(cc_p1[i]),chi2_zero=float(cz_p1[i])))[0]==land(cc_p1[i],cz_p1[i]) for i in idx)+sum(K.land_v15(dict(base,chi2_cmb=float(cc_n[i]),chi2_zero=float(cz_n[i])))[0]==land(cc_n[i],cz_n[i]) for i in idx)
    p7=agree==10000; print(f"    P7 rule cross-check vs keeper_partB_landing.land_v15 on 10,000 identical inputs: agree {agree}/10000")
except Exception as e: p7=False; print("    P7 cross-check could not run:",e)
# ---------------- (2) SKY instrument ----------------
ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; mask=L.make_mask(30.0); EDGES=[0.0,0.8,1.3,1.8,2.4,np.inf]; CHI=L.chi_table(); INT_DIR=L.lb_to_vec(300.0,20.0)
NGEN=int(913_899/0.32)
def one_sky(seed,boost,A_int):
    rng=np.random.default_rng(3000+seed); n,z,zp,S=L.synth_sky_full(NGEN,BC if boost else 0.0,vc,rng,ZEG,XG,AL,1.0,sigma_z=0.04,A_int=A_int,int_dir=INT_DIR,chi_tab=CHI)
    idx=L.CELLS.index(n); rows=[]
    for i in range(5):
        sel=(zp>=EDGES[i])&(zp<EDGES[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask)
        x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,EDGES[i],EDGES[i+1],sel.sum()); f=2+x*(1+AL)+B
        rows.append(dict(D=D,cov=cov,f=f,zmed=float(np.median(zp[sel])),N=int(cnt[mask].sum())))
    Ds=[r['D'] for r in rows]; Cs=[r['cov'] for r in rows]; fs=[r['f'] for r in rows]; zm=[r['zmed'] for r in rows]
    w=L.profile_w(zm); chis=[L.comoving(zz) for zz in zm]; w_alt=[chis[0]/c for c in chis]
    R,CR=L.redshift_dipole(idx,zp,mask); g=1+float(zp.mean())
    b,a,cov=L.joint_two_channel(Ds,Cs,fs,w,[R],[CR],[g]); be,sb,u,A,sA=L.fit_summary(b,a,cov); Sb=cov[:3,:3]+SIG_CMB**2*np.eye(3)
    c_cmb=chi2(b,b_cmb,Sb); c_zero=chi2(b,np.zeros(3),Sb)
    # 4.4 triggers
    t_sigma=sb>=BC/2; reg=region_frac(b,cov[:3,:3]); t_region=reg>0.25
    b2,a2,cov2=L.joint_two_channel(Ds,Cs,fs,w_alt,[R],[CR],[g]); be2=np.linalg.norm(b2); t_prof=abs(be2-be)>2*sb
    # A′ (4.5a): count-only vs redshift-only
    bc_,ac_,covc=L.joint_two_channel(Ds,Cs,fs,w,[],[],[]); bec,sbc,uc,_,_=L.fit_summary(bc_,ac_,covc); bz=-R/g; Sz=CR/g**2; bez=np.linalg.norm(bz); uz=bz/bez; sbz=math.sqrt(uz@Sz@uz)
    ap_amp=abs(bez-bec)<=2*math.hypot(sbz,sbc); ap_uz=in_region(uz,bc_,covc[:3,:3]); ap_uc=in_region(uc,bz,Sz); aprime=ap_amp and ap_uz and ap_uc; t_cprime=not aprime; sig_comp=math.sqrt(np.trace(cov[:3,:3])/3)*C_KMS
    # 4.4a null bin (|f| < 2σ_f; σ_f from the membership-term edge counts — here: top bin by construction, f ≈ 0) and per-bin residuals vs b_CMB
    null=[abs(f)<0.3 for f in fs]   # synthetic: f_5 ≈ 0.03 (5762); the 0.3 stands in for 2σ_f, which the sky close computes from the data
    from scipy.stats import chi2 as chi2dist
    pres=[]; null_ok=True
    for i,r in enumerate(rows):
        if null[i]: res=r['D']-w[i]*a; null_ok&=chi2dist.sf(float(res@np.linalg.solve(r['cov'],res)),3)>=0.01
        else: res=r['D']-w[i]*a-fs[i]*b_cmb; pres.append(chi2dist.sf(float(res@np.linalg.solve(r['cov'],res)),3))
    bin_ok=all(p>=0.01 for p in pres)
    lab_s5=land(c_cmb,c_zero); lab_full=land(c_cmb,c_zero,triggers=(t_sigma,t_region,t_prof,t_cprime,not null_ok),bin_ok=bin_ok,aprime=aprime); lab_14=land(c_cmb,c_zero,v14=True,sigma_beta=sb)
    lab_noreg=land(c_cmb,c_zero,triggers=(t_sigma,t_prof,t_cprime,not null_ok),bin_ok=bin_ok,aprime=aprime)
    return dict(sb=sb*C_KMS,be=be/BC,c_cmb=c_cmb,c_zero=c_zero,reg=reg,t_sigma=t_sigma,t_region=t_region,t_prof=t_prof,t_cprime=t_cprime,null_ok=null_ok,bin_ok=bin_ok,minp=min(pres),f=fs,N=sum(r['N'] for r in rows),
                lab_s5=lab_s5,lab_full=lab_full,lab_noreg=lab_noreg,lab_14=lab_14,ap_amp=ap_amp,ap_uz=ap_uz,ap_uc=ap_uc,sig_comp=sig_comp,sbc=sbc*C_KMS,sbz=sbz*C_KMS)
arms=[("P1 true, A_int 0",True,0.0),("no boost, A_int 0",False,0.0),("P1 true, A_int 0.05",True,0.05),("no boost, A_int 0.05",False,0.05)]
out=dict(fast=dict(p1_v15=f15_p1,p1_v14=f14_p1,null_v15=f15_n,null_v14=f14_n,region_fire_p1=float(np.mean(np.array(reg_p1)>0.25)),region_fire_null=float(np.mean(np.array(reg_n)>0.25))),sky={})
print(f"\n(2) SKY: {N_SEED} seeds per arm, N_gen {NGEN:,}, σ_z 0.04(1+z), five bins, joint two-channel fit")
for name,boost,A in arms:
    rs=[one_sky(s,boost,A) for s in range(N_SEED)]; sbm=np.mean([r['sb'] for r in rs]); sbs=np.std([r['sb'] for r in rs],ddof=1)
    fr=lambda k: frac([r[k] for r in rs]); trig=lambda k: np.mean([r[k] for r in rs])
    print(f"   {name:22}: N in mask {np.mean([r['N'] for r in rs]):,.0f}; σ_β c = {sbm:.1f} ± {sbs:.1f} (spread), β̂/β_CMB {np.mean([r['be'] for r in rs]):.3f}; f (seed 0) {[round(f,2) for f in rs[0]['f']]}")
    print(f"      Section 5 alone {fr('lab_s5')} | v1.4 text {fr('lab_14')} | full v1.5 (all computable clauses) {fr('lab_full')} | full minus the region clause {fr('lab_noreg')}")
    print(f"      A′ sub-conditions FAIL: amplitude {1-trig('ap_amp'):.2f}; u_z outside count-only region {1-trig('ap_uz'):.2f}; u_c outside redshift-only region {1-trig('ap_uc'):.2f}; count-only σ_β {np.mean([r['sbc'] for r in rs]):.0f}, redshift-only σ_β {np.mean([r['sbz'] for r in rs]):.0f}, joint per-component σ {np.mean([r['sig_comp'] for r in rs]):.0f} km/s")
    print(f"      4.4 triggers fired: σ_β ≥ β/2 {trig('t_sigma'):.2f}; region > 25 % {trig('t_region'):.2f} (median region {np.median([r['reg'] for r in rs]):.3f}); profile-alt > 2σ {trig('t_prof'):.2f}; C′ {trig('t_cprime'):.2f}; null-bin fail {1-trig('null_ok'):.2f}; per-bin residual fail {1-trig('bin_ok'):.2f}")
    out['sky'][name]=dict(sigma_beta=float(sbm),spread=float(sbs),s5=fr('lab_s5'),v14=fr('lab_14'),full=fr('lab_full'),noreg=fr('lab_noreg'),triggers={k:float(trig(k)) for k in ('t_sigma','t_region','t_prof','t_cprime')},null_fail=float(1-trig('null_ok')),bin_fail=float(1-trig('bin_ok')),seeds=[{k:(float(v) if not isinstance(v,(list,str,bool)) else v) for k,v in r.items()} for r in rs])
# ---------------- scoring ----------------
sk=out['sky']; a0=sk["P1 true, A_int 0"]; n0=sk["no boost, A_int 0"]
fp1_at,_ ,_,_=fast(a0['sigma_beta'],True,seed=11); fn_at,_,_,_=fast(n0['sigma_beta'],False,seed=12)
bs=lambda p: 2.5*math.sqrt(max(p*(1-p),1e-6)/N_SEED)
P={}
P['P1']=abs(f15_p1['A']-0.57)<=0.01; P['P2']=abs(f15_n['B']-0.12)<=0.01 and abs(f15_n['C']-0.86)<=0.01; P['P3']=abs(f14_p1['B']-0.56)<=0.01
P['P4']=abs(a0['s5']['A']-fp1_at['A'])<=bs(fp1_at['A']); P['P5']=abs(n0['s5']['B']-fn_at['B'])<=bs(fn_at['B'])
P['P6']=abs(a0['sigma_beta']-166.0)<=2.5*a0['spread']/math.sqrt(N_SEED); P['P7']=p7
print(f"\nSCORING (σ then band):")
print(f"   P1 fast A|P1 = {f15_p1['A']} vs 0.57 ± 0.01 → {'HIT' if P['P1'] else 'MISS'}")
print(f"   P2 fast B|null = {f15_n['B']}, C|null = {f15_n['C']} vs 0.12/0.86 ± 0.01 → {'HIT' if P['P2'] else 'MISS'}")
print(f"   P3 fast v1.4 B|P1 = {f14_p1['B']} vs 0.56 ± 0.01 → {'HIT' if P['P3'] else 'MISS'}")
print(f"   P4 sky A|P1 (Section 5 alone) = {a0['s5']['A']} vs fast at the arm's σ_β {a0['sigma_beta']:.0f}: {fp1_at['A']} ± {bs(fp1_at['A']):.3f} → {'HIT' if P['P4'] else 'MISS'}")
print(f"   P5 sky B|null (Section 5 alone) = {n0['s5']['B']} vs fast at {n0['sigma_beta']:.0f}: {fn_at['B']} ± {bs(fn_at['B']):.3f} → {'HIT' if P['P5'] else 'MISS'}")
print(f"   P6 sky σ_β c = {a0['sigma_beta']:.1f} vs 166 ± {2.5*a0['spread']/math.sqrt(N_SEED):.1f} → {'HIT' if P['P6'] else 'MISS'}")
print(f"   P7 rule cross-check → {'HIT' if P['P7'] else 'MISS'}")
print(f"SCORE {sum(P.values())}/{len(P)}  ({len(P)} can fail)")
out['score']={k:bool(v) for k,v in P.items()}; out['fast_at_sky_sigma']=dict(p1=fp1_at,null=fn_at)
json.dump(out,open(f'.record_{TOY}.json','w'),indent=1,default=float)
print(f"time {time.time()-t0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
