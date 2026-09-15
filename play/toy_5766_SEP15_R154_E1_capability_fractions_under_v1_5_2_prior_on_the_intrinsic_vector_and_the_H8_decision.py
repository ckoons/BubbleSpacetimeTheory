#!/usr/bin/env python3
"""Toy 5766 — R154 E1 (K1909 §5 (a)–(d); v1.5.2 8013d959 §4.3 (i), §5 (j), §7.1 (iii) (k), §4.4 (l)): the capability fractions under v1.5.2.
Fit (the (vi) design): count moments D_i = f_i b + w_i a (LS dipole per bin — exact response on the synthetic), redshift moments R_k = −g_k b + ζ_k a
for the full window and the four G-quartile windows (ζ, ζ_k on bin MEANS by the frozen recipe, from the synthetic's own table), six unknowns, plus
the ΛCDM prior on a: N(0, σ_A² 1), σ_A = 10 σ_c = 3.4e-3 per component (CRITERION); the fits at σ_A = σ_c = 3.4e-4 and with NO prior posted beside.
Landing (v1.5.2): Section 5's χ² clauses; Landing A also needs every non-null bin's residual D_i − w_i â − f_i b_CMB with p ≥ 0.01 under the
PROPAGATED covariance C_i + w_i² Σ_aa − w_i(M_i + M_iᵀ), M_i = cov(â, D_i) = f_i Σ_ab + w_i Σ_aa (item (j); the 4.4a null-bin check uses the same
propagation), and A′ = the amplitude clause of fit (a) (redshift-only b with ζ_k a_c subtracted, a_c the COUNT-ONLY intrinsic vector, its covariance
propagated); C-triggers: profile-alternative > 2σ_β, null-bin fail, C′; region → report; H7 = the run's σ_β within 2 per-run scatters of THIS toy's
P1-true a = 0 band (reported); hatch PASS by construction; a null lands C.
Arms (100 seeds each; Quaia depth; intrinsic on Cal's piecewise profile toward (300, 20), amplitude a = |a| on bin 1): P1 true at a = 0, 6e-4 (ΛCDM's
D_cls), 3.4e-3 (10×), 0.008, 0.024; null at a = 0 and 6e-4.
PREDICTIONS (σ printed; bands ±2.5σ):
 P1 design σ_β (criterion fit, P1 true, a = 0, along û_CMB) = 135 ± 15 km/s — Cal's referee expectation, an interpolation of 5765's prior table
    (σ_A 0.002 → 110, 0.005 → 158); the ±15 is the interpolation's honest width, not a measured σ.
 P2 A | P1 at a = 0 (criterion) within ±2.5·√(p(1−p)/100) of 0.60 = 0.72 (Section 5 alone at σ_eff ≈ 135 on the anisotropic Σ, scaled from 5763's
    0.666 at 145) × 0.87 (per-bin residual survival) × 0.95 (A′ amplitude survival).
 P3 A | P1 at a = 6e-4 within ±2.5·√2·σ_bin of the a = 0 value (a ΛCDM intrinsic dipole is 0.1 of the per-bin Poisson σ_D).
 P4 B | P1 ≤ 0.05 at a = 0, 6e-4 and 3.4e-3 (K1909 §5 (c) — the gate condition as a prediction).
 P5 B | P1 at a = 0.024 > 0.05 (7 σ_A beyond the prior: the fit pulls a to ≈ 0.07 of its value and the count channel's residual intrinsic
    w_i a goes into b̂ through the near-collinear design — the H8 case).
Reported, not predicted: B | P1 at 0.008; null B rates; the σ_c-width and no-prior landings beside each; leak b̂·d̂_int; Â; region-report; H7."""
import sys, math, json, time, resource, hashlib
import numpy as np
sys.path.insert(0,'.'); import r145_eb_lib as L; import partB_v151_lib as V
from r145_eb_lib import C_KMS
from scipy.stats import chi2 as chi2dist
TOY='5766'; N_SEED=int(sys.argv[1]) if len(sys.argv)>1 else 100
CHI2_95, CHI2_3SIG, DCHI2_A, CHI2_2_95 = 7.815, 14.156, 3.84, 5.991
SIG_A_CRIT=3.4e-3; SIG_C=3.4e-4; PRIORS={'criterion σ_A=3.4e-3':SIG_A_CRIT,'σ_c=3.4e-4':SIG_C,'no prior':None}
vc=L.lb_to_vec(264.02,48.25); BC=369.82/C_KMS; b_cmb=BC*vc; DINT=L.lb_to_vec(300.0,20.0); SIG_CMB=0.11/C_KMS
ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; mask=L.make_mask(30.0); EDGES=[0.0,0.8,1.3,1.8,2.4,np.inf]; NGEN=int(913_899/0.32)
W_PW=np.array(L.profile_w([0.57,1.06,1.54,2.06,2.71])); CHI=L.chi_table()
print(f"toy {TOY}; lib {L.lib_hash()} (frozen 4ce873ce); v151 {V.v151_hash()}; file {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; N_SEED {N_SEED}; σ_A criterion {SIG_A_CRIT}, σ_c {SIG_C}")
def chi2(b,c,S): d=b-c; return float(d@np.linalg.solve(S,d))
def region_frac(b,S):
    Si=np.linalg.inv(S); U=L.CELLS.center; num=U@(Si@b); den=np.einsum('ij,jk,ik->i',U,Si,U); bs=np.maximum(num/den,0.0); r=bs[:,None]*U-b; c2=np.einsum('ij,jk,ik->i',r,Si,r); return float((c2<=CHI2_2_95).mean())
def fit_prior(Ds,Cs,fs,w,Rs,CRs,gs,zetas,sigA):
    G=np.zeros((6,6)); r=np.zeros(6)
    for D,C,f,wi in zip(Ds,Cs,fs,w): W=np.linalg.inv(C); J=np.hstack([f*np.eye(3),wi*np.eye(3)]); G+=J.T@W@J; r+=J.T@W@D
    for R,CR,g,z in zip(Rs,CRs,gs,zetas): W=np.linalg.inv(CR); J=np.hstack([g*np.eye(3),-z*np.eye(3)]); G+=J.T@W@J; r+=J.T@W@(-R)
    if sigA: G[3:,3:]+=np.eye(3)/sigA**2
    cov=np.linalg.inv(G); p=cov@r; return p[:3],p[3:],cov
def sky(seed,boost,A):
    rng=np.random.default_rng(5000+seed); n,z,zp,S=L.synth_sky_full(NGEN,BC if boost else 0.0,vc,rng,ZEG,XG,AL,1.0,sigma_z=0.04,A_int=A,int_dir=DINT,chi_tab=CHI,piecewise_w=(np.array(ZEG),W_PW) if A>0 else None)
    idx=L.CELLS.index(n); G=-2.5*np.log10(S)+20.5; rows=[]
    for i in range(5):
        sel=(zp>=EDGES[i])&(zp<EDGES[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask)
        x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,EDGES[i],EDGES[i+1],sel.sum()); f=2+x*(1+AL)+B
        rows.append(dict(D=D,cov=cov,f=f,zmean=float(zp[sel].mean()),N=int(sel.sum()),null=abs(f)<0.3))
    Ds=[r['D'] for r in rows]; Cs=[r['cov'] for r in rows]; fs=[0.0 if r['null'] else r['f'] for r in rows]; Ns=[r['N'] for r in rows]; zm=[r['zmean'] for r in rows]; w=list(W_PW)
    chis=[L.comoving(zz) for zz in zm]; w_alt=[chis[0]/c for c in chis]
    R,CR=L.redshift_dipole(idx,zp,mask); g=1+float(zp.mean()); zeta,_=V.zeta_from_table(Ns,w,zm); Rs=[R]; CRs=[CR]; gs=[g]; zs=[zeta]
    q=np.quantile(G,[0,.25,.5,.75,1.0]); q[-1]=np.inf
    for k in range(4):
        sq=(G>=q[k])&(G<q[k+1]); Rk,CRk=L.redshift_dipole(idx[sq],zp[sq],mask); Rs.append(Rk); CRs.append(CRk); gs.append(1+float(zp[sq].mean()))
        Nk=[int((sq&(zp>=EDGES[i])&(zp<EDGES[i+1])).sum()) for i in range(5)]; zk=[float(zp[sq&(zp>=EDGES[i])&(zp<EDGES[i+1])].mean()) if Nk[i]>0 else zm[i] for i in range(5)]; zs.append(V.zeta_from_table(Nk,w,zk)[0])
    bc_,ac_,covc=L.joint_two_channel(Ds,Cs,fs,w,[],[],[]); bec,sbc,uc,_,_=L.fit_summary(bc_,ac_,covc)
    # fit (a): redshift-only with ζ_k a_c subtracted, a_c covariance propagated
    Gz=sum((gg**2)*np.linalg.inv(c) for gg,c in zip(gs,CRs)); rz=sum(gg*np.linalg.inv(c)@(-(r-zk*ac_)) for gg,r,c,zk in zip(gs,Rs,CRs,zs)); bz=np.linalg.solve(Gz,rz); Sz=np.linalg.inv(Gz); Jz=np.linalg.solve(Gz,sum(gg*zk*np.linalg.inv(c) for gg,c,zk in zip(gs,CRs,zs))); Sz=Sz+Jz@covc[3:,3:]@Jz.T
    bez=np.linalg.norm(bz); uz=bz/bez; sbz=math.sqrt(uz@Sz@uz); aprime=abs(bez-bec)<=2*math.hypot(sbz,sbc)
    out={}
    for pname,sigA in PRIORS.items():
        b,a,cov=fit_prior(Ds,Cs,fs,w,Rs,CRs,gs,zs,sigA); be,sb,u,Ahat,sA=L.fit_summary(b,a,cov); Sb=cov[:3,:3]+SIG_CMB**2*np.eye(3)
        c_cmb=chi2(b,b_cmb,Sb); c_zero=chi2(b,np.zeros(3),Sb); reg=region_frac(b,cov[:3,:3])
        b2,a2,cov2=fit_prior(Ds,Cs,fs,w_alt,Rs,CRs,gs,zs,sigA); t_prof=abs(np.linalg.norm(b2)-be)>2*sb
        Saa=cov[3:,3:]; Sab=cov[3:,:3]; pres=[]; null_ok=True
        for i,r in enumerate(rows):
            M=fs[i]*Sab+w[i]*Saa; Cr=r['cov']+w[i]**2*Saa-w[i]*(M+M.T)
            if r['null']: res=r['D']-w[i]*a; null_ok&=chi2dist.sf(float(res@np.linalg.solve(Cr,res)),3)>=0.01
            else: res=r['D']-w[i]*a-r['f']*b_cmb; pres.append(chi2dist.sf(float(res@np.linalg.solve(Cr,res)),3))
        bin_ok=all(p>=0.01 for p in pres)
        if t_prof or (not aprime) or (not null_ok): lab='C'
        elif c_cmb>=CHI2_3SIG: lab='B'
        elif c_cmb<=CHI2_95 and c_zero-c_cmb>=DCHI2_A and bin_ok: lab='A'
        else: lab='C'
        out[pname]=dict(lab=lab,sb=sb*C_KMS,rec=(b@vc)*C_KMS,leak=((b@DINT)-(BC*float(DINT@vc) if boost else 0.0))*C_KMS,Ahat=Ahat,reg=reg,prof=t_prof,bin_ok=bin_ok,null_ok=null_ok,c_cmb=c_cmb,c_zero=c_zero)
    out['aprime']=aprime; out['zeta']=zeta; return out
arms=[("P1 true, a = 0",True,0.0),("P1 true, a = 6e-4 (ΛCDM)",True,6e-4),("P1 true, a = 3.4e-3 (10×)",True,3.4e-3),("P1 true, a = 0.008",True,0.008),("P1 true, a = 0.024",True,0.024),("null, a = 0",False,0.0),("null, a = 6e-4",False,6e-4)]
t0=time.time(); res={}; band=None
for name,boost,A in arms:
    rs=[sky(s,boost,A) for s in range(N_SEED)]; o={}
    for pname in PRIORS:
        v=[r[pname] for r in rs]; fr={c:round(sum(x['lab']==c for x in v)/N_SEED,3) for c in 'ABC'}; sbm=float(np.mean([x['sb'] for x in v])); sbs=float(np.std([x['sb'] for x in v],ddof=1))
        o[pname]=dict(frac=fr,sb=sbm,sb_spread=sbs,rec=float(np.mean([x['rec'] for x in v])),s_rec=float(np.std([x['rec'] for x in v],ddof=1)/math.sqrt(N_SEED)),leak=float(np.mean([x['leak'] for x in v])),s_leak=float(np.std([x['leak'] for x in v],ddof=1)/math.sqrt(N_SEED)),Ahat=float(np.mean([x['Ahat'] for x in v])),region_report=float(np.mean([x['reg']>0.25 for x in v])),prof=float(np.mean([x['prof'] for x in v])),bin_fail=float(1-np.mean([x['bin_ok'] for x in v])),null_fail=float(1-np.mean([x['null_ok'] for x in v])))
    o['cprime']=float(1-np.mean([r['aprime'] for r in rs])); o['zeta']=float(np.mean([r['zeta'] for r in rs]))
    if band is None: band=(o['criterion σ_A=3.4e-3']['sb'],o['criterion σ_A=3.4e-3']['sb_spread'])
    o['h7_outside']=float(np.mean([abs(r['criterion σ_A=3.4e-3']['sb']-band[0])>2*band[1] for r in rs])); res[name]=o
    c=o['criterion σ_A=3.4e-3']; print(f"   {name:26}: ζ {o['zeta']:+.4f}; C′ {o['cprime']:.2f}; H7 outside {o['h7_outside']:.2f}")
    for pname in PRIORS: x=o[pname]; print(f"      {pname:22}: {x['frac']} | σ_β {x['sb']:.0f} ± {x['sb_spread']:.0f}; recovery {x['rec']:.0f} ± {x['s_rec']:.0f}; leak {x['leak']:.0f} ± {x['s_leak']:.0f}; Â {x['Ahat']:.4f}; region-report {x['region_report']:.2f}; prof {x['prof']:.2f}; per-bin fail {x['bin_fail']:.2f}; null fail {x['null_fail']:.2f}")
K='criterion σ_A=3.4e-3'; a0=res["P1 true, a = 0"][K]; aL=res["P1 true, a = 6e-4 (ΛCDM)"][K]; a10=res["P1 true, a = 3.4e-3 (10×)"][K]; a8=res["P1 true, a = 0.008"][K]; a24=res["P1 true, a = 0.024"][K]
bs=lambda p: 2.5*math.sqrt(max(p*(1-p),1e-6)/N_SEED)
P={'P1':abs(a0['sb']-135)<=15,'P2':abs(a0['frac']['A']-0.60)<=bs(0.60),'P3':abs(aL['frac']['A']-a0['frac']['A'])<=math.sqrt(2)*bs(max(a0['frac']['A'],0.05)),'P4':all(x['frac']['B']<=0.05 for x in (a0,aL,a10)),'P5':a24['frac']['B']>0.05}
print(f"\nSCORING: P1 design σ_β = {a0['sb']:.0f} (band 135 ± 15) → {'HIT' if P['P1'] else 'MISS'} | P2 A|P1(a=0) = {a0['frac']['A']} vs 0.60 ± {bs(0.60):.3f} → {'HIT' if P['P2'] else 'MISS'} | P3 A|P1(ΛCDM) = {aL['frac']['A']} vs {a0['frac']['A']} ± {math.sqrt(2)*bs(max(a0['frac']['A'],0.05)):.3f} → {'HIT' if P['P3'] else 'MISS'}")
print(f"         P4 B|P1 at a ≤ 10×: {a0['frac']['B']}, {aL['frac']['B']}, {a10['frac']['B']} (≤ 0.05 each) → {'HIT' if P['P4'] else 'MISS'} | P5 B|P1 at 0.024 = {a24['frac']['B']} (> 0.05) → {'HIT' if P['P5'] else 'MISS'}")
print(f"SCORE {sum(P.values())}/5  (5 can fail)")
print(f"\nK1909 §5 GATE: (b) A|P1 at ΛCDM = {aL['frac']['A']} {'≥' if aL['frac']['A']>=0.40 else '<'} 0.40 → {'PASS' if aL['frac']['A']>=0.40 else 'FAIL'}; (c) B|P1 ≤ 0.05 at a ≤ 10×: {'PASS' if P['P4'] else 'FAIL'}; H8: B|P1 at 0.008 = {a8['frac']['B']}, at 0.024 = {a24['frac']['B']} → {'H8 ADDED (v1.5.3)' if max(a8['frac']['B'],a24['frac']['B'])>0.05 else 'H8 not added'}; H7 band = {band[0]:.0f} ± {band[1]:.0f} km/s (design σ_β {band[0]:.0f})")
json.dump(dict(res=res,score={k:bool(v) for k,v in P.items()},band=band),open(f'.record_{TOY}.json','w'),indent=1,default=float); print(f"time {time.time()-t0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
