#!/usr/bin/env python3
"""Toy 5764 — R152 E1b (follow-up to 5763): an intrinsic dipole A = 0.05 on the FROZEN piecewise profile (Cal 4.2: A w_i, w_i at the bin median)
leaks into the joint fit's b̂ at Quaia depth (5763: β̂/β_CMB = 3.6 under P1 true, 2.8 under no boost; Section 5 alone lands B on a TRUE P1; the
full v1.5 lands C through C′). 5759 S5 ("intrinsic cancels") ran at σ_z = 0.01(1+z) and 13 M; Quaia is σ_z = 0.04(1+z). HYPOTHESIS: the leak is
photo-z MIXING of the piecewise profile — the intrinsic amplitude is a step in TRUE z, the bins are cut in OBSERVED z, so the effective w̃_i of an
observed bin differs from the frozen w_i, and the near-collinear design (f_i and w_i both fall with i) amplifies (w̃_i − w_i)·a into b̂.
Instrument: synthetic Quaia (913,899 in the mask), P1 true (369.82 toward (264.02, 48.25)), intrinsic toward (300, 20), N_SEED seeds per arm;
b̂ from the joint two-channel fit; LEAK = b̂·d̂_int (km/s) — the component along the intrinsic direction, which a boost alone does not produce
(d̂_int·û_CMB = −0.32, so the CMB contributes −119 km/s to that projection and is subtracted); RECOVERY = b̂·û_CMB (km/s) vs 369.82.
Arms: (a) A 0.05, σ_z 0 [control: no mixing]; (b) A 0.05, σ_z 0.01 [5759's]; (c) A 0.05, σ_z 0.04 [Quaia]; (d) A 0.02, σ_z 0.04; (e) A 0.01, σ_z 0.04;
(f) A 0.05, σ_z 0.04 with the fit's w_i REPLACED by the observed bins' true-z composition (w̃_i measured from the synthetic's true z — an oracle,
not available on the sky; it tests the mechanism, not a fix).
PREDICTIONS (σ = seed spread/√N, printed first; band ±2.5σ):
 P1 (a) σ_z 0: LEAK = 0 within ±2.5σ (no mixing → no leak) AND RECOVERY = 369.82 within ±2.5σ.
 P2 (c) σ_z 0.04: LEAK ≠ 0 at > 2.5σ (the 5763 effect reproduced on the leak projection).
 P3 leak is linear in A: LEAK(d)/LEAK(c) = 0.4 and LEAK(e)/LEAK(c) = 0.2, each within ±2.5σ of the ratio (σ by propagation).
 P4 (f) oracle profile: LEAK returns to 0 within ±2.5σ (the mechanism is the profile mismatch, nothing else).
 P5 (b) σ_z 0.01: |LEAK(b)| < |LEAK(c)|/2 (mixing scales with σ_z; 5759's control was not wrong, it was at a smaller σ_z).
Reported, not predicted: Section-5-alone and full-v1.5 landings per arm; C′ rate; the A_int at which full-v1.5 A-capability under P1 true collapses."""
import sys, math, json, time, resource, hashlib
import numpy as np
sys.path.insert(0,'.'); import r145_eb_lib as L
from r145_eb_lib import C_KMS
TOY='5764'; N_SEED=int(sys.argv[1]) if len(sys.argv)>1 else 30
CHI2_95, CHI2_3SIG, DCHI2_A, CHI2_2_95 = 7.815, 14.156, 3.84, 5.991
vc=L.lb_to_vec(264.02,48.25); BC=369.82/C_KMS; b_cmb=BC*vc; DINT=L.lb_to_vec(300.0,20.0); SIG_CMB=0.11/C_KMS
print(f"toy {TOY}; lib {L.lib_hash()}; file {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; N_SEED {N_SEED}; d_int·u_CMB = {float(DINT@vc):.3f} (CMB's own projection on d_int = {float(DINT@vc)*369.82:.0f} km/s)")
ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; mask=L.make_mask(30.0); EDGES=[0.0,0.8,1.3,1.8,2.4,np.inf]; NGEN=int(913_899/0.32)
W_PW=np.array(L.profile_w([0.57,1.06,1.54,2.06,2.71]))
def chi2(b,c,S): d=b-c; return float(d@np.linalg.solve(S,d))
def in_region(u,b,S):
    Si=np.linalg.inv(S); bs=max(float(u@Si@b)/float(u@Si@u),0.0); r=bs*u-b; return float(r@Si@r)<=CHI2_2_95
def one(seed,A,sig_z,oracle=False):
    rng=np.random.default_rng(4000+seed); n,z,zp,S=L.synth_sky_full(NGEN,BC,vc,rng,ZEG,XG,AL,1.0,sigma_z=sig_z,A_int=A,int_dir=DINT,chi_tab=L.chi_table(),piecewise_w=(np.array(ZEG),W_PW) if A>0 else None)
    idx=L.CELLS.index(n); rows=[]; wt=[]
    for i in range(5):
        sel=(zp>=EDGES[i])&(zp<EDGES[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask)
        x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,EDGES[i],EDGES[i+1],sel.sum()); rows.append(dict(D=D,cov=cov,f=2+x*(1+AL)+B,zmed=float(np.median(zp[sel]))))
        jt=np.clip(np.searchsorted(ZEG,z[sel],side='right')-1,0,4); wt.append(float(W_PW[jt].mean()))     # oracle: the observed bin's mean TRUE-z profile weight
    w=list(W_PW) if not oracle else wt; R,CR=L.redshift_dipole(idx,zp,mask); g=1+float(zp.mean())
    Ds=[r['D'] for r in rows]; Cs=[r['cov'] for r in rows]; fs=[r['f'] for r in rows]
    b,a,cov=L.joint_two_channel(Ds,Cs,fs,w,[R],[CR],[g]); Sb=cov[:3,:3]+SIG_CMB**2*np.eye(3); c_cmb=chi2(b,b_cmb,Sb); c_zero=chi2(b,np.zeros(3),Sb); be,sb,u,Aa,sA=L.fit_summary(b,a,cov)
    bc_,ac_,covc=L.joint_two_channel(Ds,Cs,fs,w,[],[],[]); bec,sbc,uc,_,_=L.fit_summary(bc_,ac_,covc); bz=-R/g; Sz=CR/g**2; bez=np.linalg.norm(bz); uz=bz/bez; sbz=math.sqrt(uz@Sz@uz)
    aprime=(abs(bez-bec)<=2*math.hypot(sbz,sbc)) and in_region(uz,bc_,covc[:3,:3]) and in_region(uc,bz,Sz)
    s5='B' if c_cmb>=CHI2_3SIG else ('A' if (c_cmb<=CHI2_95 and c_zero-c_cmb>=DCHI2_A) else 'C')
    full='C' if (sb>=BC/2 or not aprime) else s5
    leak=(b@DINT-BC*float(DINT@vc))*C_KMS; rec=(b@vc)*C_KMS
    return dict(leak=leak,rec=rec,s5=s5,full=full,cprime=not aprime,A_fit=Aa,wt=wt)
arms=[("(a) A 0.05, σ_z 0",0.05,0.0,False),("(b) A 0.05, σ_z 0.01",0.05,0.01,False),("(c) A 0.05, σ_z 0.04",0.05,0.04,False),("(d) A 0.02, σ_z 0.04",0.02,0.04,False),("(e) A 0.01, σ_z 0.04",0.01,0.04,False),("(f) A 0.05, σ_z 0.04, ORACLE w̃",0.05,0.04,True)]
t0=time.time(); out={}
for name,A,sz,orc in arms:
    rs=[one(s,A,sz,orc) for s in range(N_SEED)]; lk=np.array([r['leak'] for r in rs]); rc=np.array([r['rec'] for r in rs]); fr=lambda k: {c:round(sum(r[k]==c for r in rs)/N_SEED,2) for c in 'ABC'}
    out[name]=dict(leak=float(lk.mean()),s_leak=float(lk.std(ddof=1)/math.sqrt(N_SEED)),rec=float(rc.mean()),s_rec=float(rc.std(ddof=1)/math.sqrt(N_SEED)),s5=fr('s5'),full=fr('full'),cprime=float(np.mean([r['cprime'] for r in rs])),A_fit=float(np.mean([r['A_fit'] for r in rs])),wt=np.mean([r['wt'] for r in rs],0).round(3).tolist())
    o=out[name]; print(f"   {name:32}: LEAK b̂·d_int = {o['leak']:7.0f} ± {o['s_leak']:4.0f} km/s; RECOVERY b̂·u_CMB = {o['rec']:5.0f} ± {o['s_rec']:3.0f} (369.82); Â {o['A_fit']:.3f}; Section 5 alone {o['s5']}; full v1.5 {o['full']}; C′ {o['cprime']:.2f}; observed bins' true-z w̃ = {o['wt']} vs frozen {W_PW.round(3).tolist()}")
a,b_,c,d,e,f=[out[k] for k in [x[0] for x in arms]]
P={}
P['P1']=abs(a['leak'])<=2.5*a['s_leak'] and abs(a['rec']-369.82)<=2.5*a['s_rec']
P['P2']=abs(c['leak'])>2.5*c['s_leak']
def ratio(x,y): r=x['leak']/y['leak']; s=abs(r)*math.hypot(x['s_leak']/abs(x['leak']),y['s_leak']/abs(y['leak'])); return r,s
r_d,s_d=ratio(d,c); r_e,s_e=ratio(e,c); P['P3']=abs(r_d-0.4)<=2.5*s_d and abs(r_e-0.2)<=2.5*s_e
P['P4']=abs(f['leak'])<=2.5*f['s_leak']
P['P5']=abs(b_['leak'])<abs(c['leak'])/2
print(f"\nSCORING: P1 (σ_z 0: leak {a['leak']:.0f} ± {a['s_leak']:.0f}, recovery {a['rec']:.0f} ± {a['s_rec']:.0f}) → {'HIT' if P['P1'] else 'MISS'}")
print(f"         P2 (σ_z 0.04 leak {c['leak']:.0f} ± {c['s_leak']:.0f}, {abs(c['leak'])/c['s_leak']:.1f}σ) → {'HIT' if P['P2'] else 'MISS'}")
print(f"         P3 (ratios {r_d:.2f} ± {s_d:.2f} vs 0.4; {r_e:.2f} ± {s_e:.2f} vs 0.2) → {'HIT' if P['P3'] else 'MISS'}")
print(f"         P4 (oracle leak {f['leak']:.0f} ± {f['s_leak']:.0f}) → {'HIT' if P['P4'] else 'MISS'}")
print(f"         P5 (|leak| at σ_z 0.01 = {abs(b_['leak']):.0f} vs half of {abs(c['leak']):.0f}) → {'HIT' if P['P5'] else 'MISS'}")
print(f"SCORE {sum(P.values())}/5  (5 can fail)"); out['score']={k:bool(v) for k,v in P.items()}
json.dump(out,open(f'.record_{TOY}.json','w'),indent=1,default=float); print(f"time {time.time()-t0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
