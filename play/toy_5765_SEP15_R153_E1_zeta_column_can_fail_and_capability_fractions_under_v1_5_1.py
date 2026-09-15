#!/usr/bin/env python3
"""Toy 5765 — R153 E1 (K1908 @Elie): (1) THE CAN-FAIL: the ζ column (partB_v151_lib.joint_two_channel_zeta; ζ = Σ p_i w_i (z̃_i − z̄) from the
synthetic's OWN (v)-style table — N_i, w_i, bin medians of observed z, exactly the frozen recipe) into 5764's synthetic redshift channel: the
intrinsic leak b̂·d̂_int must fall to 0 ± σ. (2) The capability fractions under v1.5.1 as K1908 §4 recommends (Cal's hash pending; re-keyed to
his file when it lands): (a) region clause → report only; (b) σ_β ≥ 185 → not a per-run trigger (H7: the run's σ_β vs the synthetic band,
reported); (c) ζ column in the joint fit; (d) A′ = amplitude clause + û_z inside the count-only 95 % region; (e) the count moments are the LS
dipole (exact response — the synthetic's estimator, as in 5757–5763); (f) a null lands C; profile-alternative trigger, 4.4a null-bin check and
Landing A's per-bin residual test unchanged; hatch PASS by construction. Section 5's χ² clauses as v1.5. Redshift channel: the full-sample window
(as 5763/5764; the quartile windows carry their own ζ_w in the (vi) script).
Arms (100 seeds each unless stated; Quaia depth 913,899 in the mask; Cal's piecewise intrinsic on TRUE z toward (300, 20)):
 can-fail: (c1) P1 true, A 0.05, σ_z 0 (30 seeds — 5764's arm (a)); (c2) P1 true, A 0.05, σ_z 0.04 (30 seeds — 5764's (c)).
 fractions: (f1) P1 true A 0; (f2) null A 0; (f3) P1 true A 0.005; (f4) P1 true A 0.01; (f5) null A 0.01.
PREDICTIONS (σ printed, bands ±2.5σ; binomial σ = √(p(1−p)/N)):
 P1 (c1) leak with ζ = 0 ± 2.5σ_leak (5764 without ζ: 980 ± 48).      P2 (c2) leak with ζ = 0 ± 2.5σ_leak (5764: 1013 ± 45).
 P3 (c1) recovery b̂·û_CMB = 369.82 ± 2.5σ (5764: 1069 ± 41).
 P4 (f1) A|P1 under v1.5.1 within ±2.5σ_bin of 0.53 = 0.666 (fast instrument on the anisotropic Σ, 5763) × (1 − 0.08 A′-amplitude/û_z fails) × (1 − 0.13 per-bin fails).
 P5 (f2) B|null under v1.5.1 within ±2.5σ_bin of 0.185 (5763's anisotropic fast value; hatch passes by construction).
 P6 (f4) A|P1 at A = 0.01 with ζ within ±2.5·√(σ²_f1 + σ²_f4) of (f1)'s A|P1 (the leak absorbed → same capability).
 P7 (f4) recovery b̂·û_CMB at A = 0.01 = 369.82 ± 2.5σ.
Reported, not predicted: ζ_median vs ζ_mean (bin means) residual leak; the region-clause report fraction; the H7 band fraction; C′ under (d)."""
import sys, math, json, time, resource, hashlib
import numpy as np
sys.path.insert(0,'.'); import r145_eb_lib as L; import partB_v151_lib as V
from r145_eb_lib import C_KMS
from scipy.stats import chi2 as chi2dist
TOY='5765'; N_SEED=int(sys.argv[1]) if len(sys.argv)>1 else 100; N_CF=int(sys.argv[2]) if len(sys.argv)>2 else 30
CHI2_95, CHI2_3SIG, DCHI2_A, CHI2_2_95 = 7.815, 14.156, 3.84, 5.991
vc=L.lb_to_vec(264.02,48.25); BC=369.82/C_KMS; b_cmb=BC*vc; DINT=L.lb_to_vec(300.0,20.0); SIG_CMB=0.11/C_KMS
ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; mask=L.make_mask(30.0); EDGES=[0.0,0.8,1.3,1.8,2.4,np.inf]; NGEN=int(913_899/0.32)
W_PW=np.array(L.profile_w([0.57,1.06,1.54,2.06,2.71])); CHI=L.chi_table()
print(f"toy {TOY}; lib {L.lib_hash()} (frozen 4ce873ce); v151 {V.v151_hash()}; file {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; N_SEED {N_SEED}; N_CF {N_CF}")
def chi2(b,c,S): d=b-c; return float(d@np.linalg.solve(S,d))
def region_frac(b,S):
    Si=np.linalg.inv(S); U=L.CELLS.center; num=U@(Si@b); den=np.einsum('ij,jk,ik->i',U,Si,U); bs=np.maximum(num/den,0.0); r=bs[:,None]*U-b; c2=np.einsum('ij,jk,ik->i',r,Si,r); return float((c2<=CHI2_2_95).mean())
def in_region(u,b,S):
    Si=np.linalg.inv(S); bs=max(float(u@Si@b)/float(u@Si@u),0.0); r=bs*u-b; return float(r@Si@r)<=CHI2_2_95
def sky(seed,boost,A,sig_z,zeta_mode='median'):
    rng=np.random.default_rng(4000+seed); n,z,zp,S=L.synth_sky_full(NGEN,BC if boost else 0.0,vc,rng,ZEG,XG,AL,1.0,sigma_z=sig_z,A_int=A,int_dir=DINT,chi_tab=CHI,piecewise_w=(np.array(ZEG),W_PW) if A>0 else None)
    idx=L.CELLS.index(n); rows=[]
    for i in range(5):
        sel=(zp>=EDGES[i])&(zp<EDGES[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask)
        x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,EDGES[i],EDGES[i+1],sel.sum()); f=2+x*(1+AL)+B
        rows.append(dict(D=D,cov=cov,f=f,zmed=float(np.median(zp[sel])),zmean=float(zp[sel].mean()),N=int(cnt[mask].sum()),null=abs(f)<0.3))
    Ds=[r['D'] for r in rows]; Cs=[r['cov'] for r in rows]; fs=[0.0 if r['null'] else r['f'] for r in rows]; zm=[r['zmed'] for r in rows]; Ns=[r['N'] for r in rows]
    w=list(W_PW); chis=[L.comoving(zz) for zz in zm]; w_alt=[chis[0]/c for c in chis]
    R,CR=L.redshift_dipole(idx,zp,mask); g=1+float(zp.mean())
    zeta,zbar=V.zeta_from_table(Ns,w,zm if zeta_mode=='median' else [r['zmean'] for r in rows])
    b,a,cov=V.joint_two_channel_zeta(Ds,Cs,fs,w,[R],[CR],[g],[zeta]); be,sb,u,Ahat,sA=L.fit_summary(b,a,cov); Sb=cov[:3,:3]+SIG_CMB**2*np.eye(3)
    c_cmb=chi2(b,b_cmb,Sb); c_zero=chi2(b,np.zeros(3),Sb); reg=region_frac(b,cov[:3,:3])
    b2,a2,cov2=V.joint_two_channel_zeta(Ds,Cs,fs,w_alt,[R],[CR],[g],[V.zeta_from_table(Ns,w_alt,zm)[0]]); t_prof=abs(np.linalg.norm(b2)-be)>2*sb
    bc_,ac_,covc=L.joint_two_channel(Ds,Cs,fs,w,[],[],[]); bec,sbc,uc,_,_=L.fit_summary(bc_,ac_,covc)
    bz=-(R-zeta*a)/g; Sz=CR/g**2; bez=np.linalg.norm(bz); uz=bz/bez; sbz=math.sqrt(uz@Sz@uz)      # redshift-only with the fitted intrinsic column removed
    aprime=(abs(bez-bec)<=2*math.hypot(sbz,sbc)) and in_region(uz,bc_,covc[:3,:3]); t_cprime=not aprime
    pres=[]; null_ok=True
    for i,r in enumerate(rows):
        if r['null']: res=r['D']-w[i]*a; null_ok&=chi2dist.sf(float(res@np.linalg.solve(r['cov'],res)),3)>=0.01
        else: res=r['D']-w[i]*a-r['f']*b_cmb; pres.append(chi2dist.sf(float(res@np.linalg.solve(r['cov'],res)),3))
    bin_ok=all(p>=0.01 for p in pres)
    if t_prof or t_cprime or not null_ok: lab='C'
    elif c_cmb>=CHI2_3SIG: lab='B'
    elif c_cmb<=CHI2_95 and c_zero-c_cmb>=DCHI2_A and bin_ok: lab='A'
    else: lab='C'
    s5='B' if c_cmb>=CHI2_3SIG else ('A' if (c_cmb<=CHI2_95 and c_zero-c_cmb>=DCHI2_A) else 'C')
    leak=(b@DINT-BC*float(DINT@vc))*C_KMS if boost else (b@DINT)*C_KMS; rec=(b@vc)*C_KMS
    return dict(leak=leak,rec=rec,sb=sb*C_KMS,lab=lab,s5=s5,reg=reg,t_prof=t_prof,t_cprime=t_cprime,bin_ok=bin_ok,null_ok=null_ok,zeta=zeta,A_fit=Ahat,h7=abs(sb*C_KMS-175)>2*21)
t0=time.time(); out={}
def arm(name,boost,A,sz,nseed,zm='median'):
    rs=[sky(s,boost,A,sz,zm) for s in range(nseed)]; lk=np.array([r['leak'] for r in rs]); rc=np.array([r['rec'] for r in rs]); fr=lambda k: {c:round(sum(r[k]==c for r in rs)/nseed,3) for c in 'ABC'}
    o=dict(leak=float(lk.mean()),s_leak=float(lk.std(ddof=1)/math.sqrt(nseed)),rec=float(rc.mean()),s_rec=float(rc.std(ddof=1)/math.sqrt(nseed)),sb=float(np.mean([r['sb'] for r in rs])),sb_spread=float(np.std([r['sb'] for r in rs],ddof=1)),
           v151=fr('lab'),s5=fr('s5'),zeta=float(np.mean([r['zeta'] for r in rs])),A_fit=float(np.mean([r['A_fit'] for r in rs])),region_report=float(np.mean([r['reg']>0.25 for r in rs])),h7_outside=float(np.mean([r['h7'] for r in rs])),
           cprime=float(np.mean([r['t_cprime'] for r in rs])),prof=float(np.mean([r['t_prof'] for r in rs])),bin_fail=float(1-np.mean([r['bin_ok'] for r in rs])),null_fail=float(1-np.mean([r['null_ok'] for r in rs])),n=nseed)
    print(f"   {name:34}: ζ = {o['zeta']:+.4f}; LEAK b̂·d_int = {o['leak']:6.0f} ± {o['s_leak']:3.0f}; RECOVERY b̂·û_CMB = {o['rec']:5.0f} ± {o['s_rec']:3.0f}; σ_β {o['sb']:.0f} ± {o['sb_spread']:.0f}; Â {o['A_fit']:.4f}; v1.5.1 {o['v151']} | Section 5 alone {o['s5']}; region-report {o['region_report']:.2f}; H7 outside {o['h7_outside']:.2f}; C′ {o['cprime']:.2f}; prof {o['prof']:.2f}; per-bin fail {o['bin_fail']:.2f}; null fail {o['null_fail']:.2f}")
    out[name]=o; return o
print("(1) CAN-FAIL — the ζ column:")
c1=arm("(c1) P1 true, A 0.05, σ_z 0",True,0.05,0.0,N_CF); c2=arm("(c2) P1 true, A 0.05, σ_z 0.04",True,0.05,0.04,N_CF)
c1m=arm("(c1m) same, ζ on bin MEANS",True,0.05,0.0,N_CF,'mean')
print("(2) FRACTIONS under v1.5.1 (K1908 §4 as recommended):")
f1=arm("(f1) P1 true, A 0",True,0.0,0.04,N_SEED); f2=arm("(f2) null, A 0",False,0.0,0.04,N_SEED); f3=arm("(f3) P1 true, A 0.005",True,0.005,0.04,N_SEED); f4=arm("(f4) P1 true, A 0.01",True,0.01,0.04,N_SEED); f5=arm("(f5) null, A 0.01",False,0.01,0.04,N_SEED)
bs=lambda p,n: 2.5*math.sqrt(max(p*(1-p),1e-6)/n)
P={}
P['P1']=abs(c1['leak'])<=2.5*c1['s_leak']; P['P2']=abs(c2['leak'])<=2.5*c2['s_leak']; P['P3']=abs(c1['rec']-369.82)<=2.5*c1['s_rec']
P['P4']=abs(f1['v151']['A']-0.53)<=bs(0.53,N_SEED); P['P5']=abs(f2['v151']['B']-0.185)<=bs(0.185,N_SEED)
sA=math.sqrt(f1['v151']['A']*(1-f1['v151']['A'])/N_SEED+f4['v151']['A']*(1-f4['v151']['A'])/N_SEED); P['P6']=abs(f4['v151']['A']-f1['v151']['A'])<=2.5*max(sA,0.02)
P['P7']=abs(f4['rec']-369.82)<=2.5*f4['s_rec']
print(f"\nSCORING: P1 leak {c1['leak']:.0f} ± {c1['s_leak']:.0f} → {'HIT' if P['P1'] else 'MISS'} | P2 leak {c2['leak']:.0f} ± {c2['s_leak']:.0f} → {'HIT' if P['P2'] else 'MISS'} | P3 recovery {c1['rec']:.0f} ± {c1['s_rec']:.0f} → {'HIT' if P['P3'] else 'MISS'}")
print(f"         P4 A|P1 = {f1['v151']['A']} vs 0.53 ± {bs(0.53,N_SEED):.3f} → {'HIT' if P['P4'] else 'MISS'} | P5 B|null = {f2['v151']['B']} vs 0.185 ± {bs(0.185,N_SEED):.3f} → {'HIT' if P['P5'] else 'MISS'}")
print(f"         P6 A|P1 at A 0.01 = {f4['v151']['A']} vs A 0: {f1['v151']['A']} ± {2.5*max(sA,0.02):.3f} → {'HIT' if P['P6'] else 'MISS'} | P7 recovery at A 0.01 = {f4['rec']:.0f} ± {f4['s_rec']:.0f} → {'HIT' if P['P7'] else 'MISS'}")
print(f"SCORE {sum(P.values())}/7  (7 can fail)"); out['score']={k:bool(v) for k,v in P.items()}
json.dump(out,open(f'.record_{TOY}.json','w'),indent=1,default=float); print(f"time {time.time()-t0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
