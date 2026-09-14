#!/usr/bin/env python3
"""Toy 5757 — R145 E1/E2 (prereg 20539fe5): a per-bin Ellis–Baldwin dipole estimator (amplitude, direction, propagated + bootstrap
uncertainties) and its two synthetic controls. NO CATALOGUE IS TOUCHED; every sky here is drawn from a seed.
The boost in the positive control is applied PHYSICALLY (aberration of directions + Doppler flux boost + flux cut), so the
Ellis–Baldwin amplitude 2 + x(1+alpha) that the estimator uses is tested against the synthetic, not assumed by it."""
import math, json, hashlib
import numpy as np
from scipy.stats import ncx2
C_KMS=299792.458
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
# ---------------------------------------------------------------- sky geometry ----------------------------------------------------------------
def lb_to_vec(l,b):
    l=np.radians(l); b=np.radians(b); return np.stack([np.cos(b)*np.cos(l),np.cos(b)*np.sin(l),np.sin(b)],-1)
def vec_to_lb(v):
    v=np.atleast_2d(v); l=np.degrees(np.arctan2(v[:,1],v[:,0]))%360; b=np.degrees(np.arcsin(np.clip(v[:,2]/np.linalg.norm(v,axis=1),-1,1))); return l,b
class Cells:
    """equal-area cells: rings uniform in sin b, cells uniform in l within a ring."""
    def __init__(self,n_rings=48,per_ring_eq=96):
        edges=np.linspace(-1,1,n_rings+1); self.rows=[]
        for j in range(n_rings):
            s0,s1=edges[j],edges[j+1]; bc=math.asin((s0+s1)/2); m=max(1,int(round(per_ring_eq*math.cos(bc))))
            self.rows.append((s0,s1,m))
        self.offsets=np.cumsum([0]+[m for _,_,m in self.rows]); self.n=int(self.offsets[-1])
        self.area=np.concatenate([np.full(m,2*math.pi*(s1-s0)/m) for s0,s1,m in self.rows])   # steradian per cell
        ctr=[]
        for s0,s1,m in self.rows:
            bc=math.asin((s0+s1)/2)
            for k in range(m): ctr.append((2*math.pi*(k+0.5)/m, bc))
        ctr=np.array(ctr); self.center=np.stack([np.cos(ctr[:,1])*np.cos(ctr[:,0]),np.cos(ctr[:,1])*np.sin(ctr[:,0]),np.sin(ctr[:,1])],-1)
        self.ring_edges=edges
    def index(self,v):
        s=np.clip(v[:,2],-1,1-1e-12); j=np.minimum((np.searchsorted(self.ring_edges,s,side='right')-1),len(self.rows)-1)
        m=np.array([r[2] for r in self.rows])[j]; l=np.arctan2(v[:,1],v[:,0])%(2*math.pi)
        return self.offsets[j]+np.minimum((l/(2*math.pi)*m).astype(int),m-1)
CELLS=Cells()
def make_mask(b_cut=15.0,exclusions=((280.5,-32.9,5.0),(302.8,-44.3,3.0))):
    ok=np.abs(np.degrees(np.arcsin(CELLS.center[:,2])))>b_cut
    for l,b,r in exclusions: ok&=(CELLS.center@lb_to_vec(l,b))<math.cos(math.radians(r))
    return ok
# ---------------------------------------------------------------- E1: the estimator ----------------------------------------------------------------
def dipole_from_counts(n,mask,nboot=200,rng=None):
    """weighted linear LS of n_c = A_c [a + b.n_c] on unmasked cells; returns D=b/a, cov(D) (Poisson), bootstrap draws of D."""
    A=CELLS.area[mask]; X=np.column_stack([A,A[:,None]*CELLS.center[mask]]); y=n[mask].astype(float); N=y.sum()
    a0=N/A.sum(); w=1/(A*a0); XtW=X.T*w; M=np.linalg.solve(XtW@X,XtW)                      # M: 4 x cells
    p=M@y; a,b=p[0],p[1:]; D=b/a
    covp=np.linalg.inv(XtW@X); J=np.zeros((3,4)); J[:,0]=-b/a**2; J[:,1:]=np.eye(3)/a; covD=J@covp@J.T
    boots=None
    if nboot:
        rng=rng or np.random.default_rng(0); draws=rng.multinomial(int(N),y/N,size=nboot).astype(float); pb=draws@M.T; boots=pb[:,1:]/pb[:,:1]
    return D,covD,boots
NEY_COV='analytic'                       # addendum 3 (e16c19e4): switched to 'bootstrap' only if the analytic pull fails P10
NEY_RNG=np.random.default_rng(8917)     # the Neyman simulation has its OWN stream so the sky realisations of runs 1-2 are reproduced exactly
def neyman(obs,covD,u,nsim=4000,ngrid=80):
    """95% Neyman interval on the true amplitude D by Monte Carlo with the FULL covariance: for each trial D_true (along the
    estimated direction u) simulate D_hat = D_true u + L N(0,I), take the central 95% of |D_hat|; the interval is the set of D_true
    whose central band contains |D_hat|_obs. The 95% direction cone is the 95th percentile of the offset angle at D_true = D_lo
    (the conservative end; full sky when D_lo = 0)."""
    L=np.linalg.cholesky(covD); smax=math.sqrt(np.trace(covD)); grid=np.linspace(0,obs+6*smax,ngrid)
    noise=NEY_RNG.normal(size=(nsim,3))@L.T
    lo_q=np.empty(ngrid); hi_q=np.empty(ngrid)
    for k,Dt in enumerate(grid):
        amp=np.linalg.norm(Dt*u+noise,axis=1); lo_q[k],hi_q[k]=np.percentile(amp,[2.5,97.5])
    ok=(lo_q<=obs)&(obs<=hi_q); idx=np.where(ok)[0]
    if len(idx)==0: Dlo,Dhi=obs,obs
    else: Dlo,Dhi=grid[idx[0]],grid[idx[-1]]
    if Dlo==0: cone=180.0
    else:
        sim=Dlo*u+noise; sim/=np.linalg.norm(sim,axis=1)[:,None]; cone=float(np.percentile(np.degrees(np.arccos(np.clip(sim@u,-1,1))),95))
    return Dlo,Dhi,cone
def eb_estimate(vecs,z,S,z_edges,x_alpha,mask,S_lim=1.0,nboot=200,rng=None,measure_x=True):
    """per-bin Ellis–Baldwin: D, v (km/s), direction (l,b), analytic and bootstrap uncertainties, 95% positional cone, measured x."""
    out=[]
    for i in range(len(z_edges)-1):
        sel=(z>=z_edges[i])&(z<z_edges[i+1]); v=vecs[sel]; Si=S[sel]; x,al=x_alpha[i]
        idx=CELLS.index(v); n=np.bincount(idx,minlength=CELLS.n); n[~mask]=0
        D,covD,boots=dipole_from_counts(n,mask,nboot,rng); amp=2+x*(1+al)
        Dn=np.linalg.norm(D); u=D/Dn; sD_par=math.sqrt(max(u@covD@u,0)); v_kms=Dn/amp*C_KMS; sv_an=sD_par/amp*C_KMS
        Ddb=math.sqrt(max(Dn**2-np.trace(covD),0)); v_db=Ddb/amp*C_KMS                       # noise-debiased amplitude (addendum, ac942988)
        covB=np.cov(boots.T) if boots is not None else covD
        Dlo,Dhi,cone_ney=neyman(Dn,covD if NEY_COV=='analytic' else covB,u)                              # Neyman 95% interval + cone (addendum 2, 8917b8fb; MC with full covariance)
        l,b=vec_to_lb(D)
        res=dict(bin=(z_edges[i],z_edges[i+1]),N=int(n[mask].sum()),x=x,alpha=al,D=Dn,v=v_kms,v_db=v_db,sv_an=sv_an,l=float(l[0]),b=float(b[0]),
                 v_lo_ney=Dlo/amp*C_KMS,v_hi_ney=Dhi/amp*C_KMS,cone95_ney=cone_ney,Dvec=D.tolist(),covA=covD.tolist(),covB=covB.tolist())
        if boots is not None:
            bn=np.linalg.norm(boots,axis=1); res['sv_boot']=float(bn.std()/amp*C_KMS)
            ang=np.degrees(np.arccos(np.clip((boots/bn[:,None])@u,-1,1))); res['cone95']=float(np.percentile(ang,95)); res['v_lo'],res['v_hi']=[float(q/amp*C_KMS) for q in np.percentile(bn,[2.5,97.5])]
        if measure_x:
            above=Si[Si>=S_lim]; res['x_meas']=float(math.log((above>=S_lim).sum()/max((above>=2*S_lim).sum(),1))/math.log(2))
        out.append(res)
    return out
# ---------------------------------------------------------------- synthetic skies ----------------------------------------------------------------
Z_EDGES=[0,0.75,1.25,1.75,2.5,4.0]; X_GEN=[0.9,1.0,1.1,1.2,1.3]; ALPHA=1.0; XA=[(x,ALPHA) for x in X_GEN]; S_LIM=1.0; S_MIN=S_LIM/1.5
def synth_sky(N_gen,beta,vhat,rng,D_int=None,int_dir=None,int_scale=0.5):
    """isotropic population in its own frame; PHYSICAL boost (aberration + Doppler + flux cut); optional intrinsic density dipole (no boost)."""
    vecs=[];zs=[];Ss=[]
    g=1/math.sqrt(1-beta**2)
    for i in range(len(Z_EDGES)-1):
        m=N_gen//5
        z=rng.uniform(Z_EDGES[i],Z_EDGES[i+1],m)                      # bin-uniform z (the bins are what matter here)
        n=rng.normal(size=(m,3)); n/=np.linalg.norm(n,axis=1)[:,None]
        if D_int is not None:                                           # intrinsic dipole: density modulation 1 + D_int(z) cos(theta), by rejection
            amp=D_int*np.exp(-z/int_scale); keep=rng.uniform(size=m)<(1+amp*(n@int_dir))/(1+amp); n=n[keep]; z=z[keep]; m=len(z)
        S=S_MIN*rng.uniform(size=m)**(-1/X_GEN[i])                    # N(>S) ∝ S^-x in the population frame
        if beta>0:
            mu=n@vhat; delta=g*(1+beta*mu)
            n=(n+((g-1)*mu+g*beta)[:,None]*vhat)/(g*(1+beta*mu))[:,None]   # aberration: apparent direction in the observer's frame
            S=S*delta**(1+ALPHA)                                           # Doppler: S'(nu) = delta^(1+alpha) S(nu)
        cut=S>=S_LIM; vecs.append(n[cut]); zs.append(z[cut]); Ss.append(S[cut])
    return np.concatenate(vecs),np.concatenate(zs),np.concatenate(Ss)
def report(res,title):
    print(f"\n{title}")
    print(f"   {'bin':12}{'N':>9}{'x_gen':>7}{'x_meas':>8}{'D':>10}{'v [km/s]':>11}{'v_db':>7}{'±an':>6}{'±boot':>6}{'boot 95% v':>16}{'NEYMAN 95% v':>16}{'(l, b)':>17}{'cone_boot':>10}{'cone_Ney':>9}")
    for r in res: print(f"   {str(r['bin']):12}{r['N']:9d}{r['x']:7.2f}{r.get('x_meas',float('nan')):8.3f}{r['D']:10.5f}{r['v']:11.1f}{r['v_db']:7.0f}{r['sv_an']:6.0f}{r.get('sv_boot',float('nan')):6.0f}   [{r.get('v_lo',0):5.0f},{r.get('v_hi',0):5.0f}]   [{r['v_lo_ney']:5.0f},{r['v_hi_ney']:5.0f}]  ({r['l']:6.1f},{r['b']:6.1f}){r.get('cone95',float('nan')):9.1f}°{r['cone95_ney']:8.1f}°")
def compare(res,v_inj,dir_inj):
    hits=[]
    for r in res:
        dv_ok=r['v_lo']<=v_inj<=r['v_hi']; ang=math.degrees(math.acos(np.clip(lb_to_vec(r['l'],r['b'])@dir_inj,-1,1))); d_ok=ang<=r['cone95']
        hits.append((dv_ok,d_ok,ang)); print(f"      bin {r['bin']}: v in 95% range: {dv_ok};  direction offset {ang:.1f}° vs cone95 {r['cone95']:.1f}°: {d_ok}")
    return hits
rng=np.random.default_rng(5757); mask=make_mask()
print(f"cells: {CELLS.n} equal-area; unmasked {mask.sum()} ({100*CELLS.area[mask].sum()/(4*math.pi):.1f}% of the sky) — mask |b|>15° + LMC + SMC")
# ------------------------------------------------ E2 positive control, BLIND (sealed injection) ------------------------------------------------
seal=np.random.default_rng(int(hashlib.sha256(b"prereg 20539fe5 sealed injection").hexdigest()[:8],16))
v_inj=seal.uniform(200,600); d=seal.normal(size=3); dir_inj=d/np.linalg.norm(d); beta_inj=v_inj/C_KMS
sealed=hashlib.sha256(f"{v_inj:.6f} {dir_inj.round(8).tolist()}".encode()).hexdigest()[:12]
print(f"\nSEALED injection hash {sealed} — values revealed only after the estimates are printed")
vecs,z,S=synth_sky(2_600_000,beta_inj,dir_inj,rng); resA=eb_estimate(vecs,z,S,Z_EDGES,XA,mask,S_LIM,200,rng)
report(resA,f"E2 POSITIVE CONTROL (BLIND), Quaia-like depth: {len(z):,} sources after cut, {sum(r['N'] for r in resA):,} unmasked")
vecs,z,S=synth_sky(26_000_000,beta_inj,dir_inj,rng); resA10=eb_estimate(vecs,z,S,Z_EDGES,XA,mask,S_LIM,200,rng)
report(resA10,f"E2 POSITIVE CONTROL (BLIND), 10x depth: {len(z):,} sources after cut, {sum(r['N'] for r in resA10):,} unmasked")
li,bi=vec_to_lb(dir_inj); print(f"\n   REVEAL: injected v = {v_inj:.1f} km/s toward (l, b) = ({li[0]:.1f}, {bi[0]:.1f})")
print("   1.3 M:"); hA=compare(resA,v_inj,dir_inj); print("   13 M:"); hA10=compare(resA10,v_inj,dir_inj)
sc("P1", all(abs(r['x_meas']-r['x'])<0.05 for r in resA+resA10), True, f"measured x within 0.05 of generating x in all bins (max |Δx| = {max(abs(r['x_meas']-r['x']) for r in resA+resA10):.3f})")
n_ok=sum(1 for a,b_,_ in hA if a and b_); n_ok10=sum(1 for a,b_,_ in hA10 if a and b_)
ratio_sig=np.mean([r['sv_boot'] for r in resA])/np.mean([r['sv_boot'] for r in resA10])
sc("P2", n_ok>=4 and n_ok10==5 and 2.5<ratio_sig<4.0, True, f"blind recovery: {n_ok}/5 bins at 1.3 M, {n_ok10}/5 at 13 M inside the 95% intervals (v and direction); σ_v ratio 1.3M/13M = {ratio_sig:.2f} (√10 = 3.16)")
wm=sum(r['N']*r['v'] for r in resA10)/sum(r['N'] for r in resA10)/v_inj
sc("P3", 0.95<wm<1.05, True, f"count-weighted mean v̂/v_inj at 13 M = {wm:.4f} — the Ellis–Baldwin amplitude 2 + x(1+α) is unbiased against a physical boost")
# ------------------------------------------------ E2 positive control, NAMED (the Planck 2018 numbers of the draft) ------------------------------------------------
v_cmb=369.82; dir_cmb=lb_to_vec(264.02,48.25)
vecs,z,S=synth_sky(2_600_000,v_cmb/C_KMS,dir_cmb,rng); resB=eb_estimate(vecs,z,S,Z_EDGES,XA,mask,S_LIM,200,rng)
report(resB,"E2 POSITIVE CONTROL (NAMED: 369.82 km/s toward (264.02, 48.25)), Quaia-like depth"); hB=compare(resB,v_cmb,dir_cmb)
print(f"   per-bin σ_v at Quaia-like depth: {[round(r['sv_boot']) for r in resB]} km/s — what a per-bin comparison with 369.82 ± 0.11 can decide at 1.3 M sources")
# ------------------------------------------------ E2 negative control: intrinsic dipole, no boost; the separation step ------------------------------------------------
int_dir=lb_to_vec(90.0,20.0); D0=0.03; scale=0.5
vecs,z,S=synth_sky(2_600_000,0.0,int_dir,rng,D_int=D0,int_dir=int_dir,int_scale=scale)
resN=[]; Ds=[]; Cs=[]
for i in range(5):
    sel=(z>=Z_EDGES[i])&(z<Z_EDGES[i+1]); idx=CELLS.index(vecs[sel]); n=np.bincount(idx,minlength=CELLS.n); n[~mask]=0
    D,covD,_=dipole_from_counts(n,mask,0); Ds.append(D); Cs.append(covD)
    l,b=vec_to_lb(D); zb=0.5*(Z_EDGES[i]+Z_EDGES[i+1]); print(f"   NEG bin {Z_EDGES[i]}-{Z_EDGES[i+1]}: |D| = {np.linalg.norm(D):.5f} (injected {D0*math.exp(-zb/scale):.5f} at bin centre) toward ({l[0]:.1f},{b[0]:.1f}); σ_D = {math.sqrt(covD[0,0]):.5f}")
def separate(Ds,Cs,g):
    """fit D_b = K + I g(z_b) with per-bin covariances; returns K, I, their σ, and corr(K_i, I_i)."""
    zc=[0.5*(Z_EDGES[i]+Z_EDGES[i+1]) for i in range(5)]; gz=np.array([g(zz) for zz in zc])
    W=np.linalg.inv(np.array(Cs)); # 5 x 3 x 3
    # unknowns p = (K(3), I(3)); model_b = K + I g_b; normal equations
    A=np.zeros((6,6)); r=np.zeros(6)
    for b_ in range(5):
        Jb=np.hstack([np.eye(3),gz[b_]*np.eye(3)]); A+=Jb.T@W[b_]@Jb; r+=Jb.T@W[b_]@Ds[b_]
    cov=np.linalg.inv(A); p=cov@r; K,I=p[:3],p[3:]; sK=np.sqrt(np.diag(cov)[:3]); sI=np.sqrt(np.diag(cov)[3:])
    corr=[cov[i,3+i]/math.sqrt(cov[i,i]*cov[3+i,3+i]) for i in range(3)]
    chi2=sum((Ds[b_]-K-I*gz[b_])@W[b_]@(Ds[b_]-K-I*gz[b_]) for b_ in range(5))
    return K,sK,I,sI,corr,chi2
print("\n   SEPARATION D_b = K + I·g(z_b):")
outN={}
for lab,g in (("matched template g = exp(-z/0.5)",lambda zz: math.exp(-zz/0.5)),("MISMATCHED template g = (1+z)^-2",lambda zz: (1+zz)**-2)):
    K,sK,I,sI,corr,chi2=separate(Ds,Cs,g); outN[lab]=(K,sK,I,sI,corr,chi2)
    print(f"   {lab}: K = {np.round(K,5).tolist()} ± {np.round(sK,5).tolist()} (|K| = {np.linalg.norm(K):.5f}, ≙ {np.linalg.norm(K)/(2+1.1*2)*C_KMS:.0f} km/s at x=1.1)")
    print(f"      I = {np.round(I,4).tolist()} ± {np.round(sI,4).tolist()}  (|I|/σ = {np.linalg.norm(I)/np.mean(sI):.1f});  corr(K_i,I_i) = {np.round(corr,3).tolist()};  χ² = {chi2:.1f} for 9 dof")
Km,sKm,Im,sIm,_,_=outN["matched template g = exp(-z/0.5)"]; Kx,sKx,Ix,_,corrx,chi2x=outN["MISMATCHED template g = (1+z)^-2"]
leak=np.linalg.norm(Kx)/D0
sc("P4", all(abs(Km)<2*sKm) and np.linalg.norm(Im)/np.mean(sIm)>5, True, f"matched: |K_i| < 2σ in every component and I at {np.linalg.norm(Im)/np.mean(sIm):.1f}σ; mismatched: leaked |K| = {np.linalg.norm(Kx):.5f} = {100*leak:.0f}% of D_int(0) ≙ {np.linalg.norm(Kx)/(4.2)*C_KMS:.0f} km/s, χ² = {chi2x:.1f}/9 — the template is a freeze item")
agree=[abs(r['sv_boot']/r['sv_an']-1) for r in resA+resA10+resB]
sc("P5", max(agree)<0.25, False, f"analytic vs bootstrap σ_v agree within {100*max(agree):.0f}% (worst bin)")
# ------------------------------------------------ ADDENDUM (prereg ac942988): coverage over 20 blind seeds; amplitude at beta = 0.01 ------------------------------------------------
print("\nADDENDUM P6 — coverage of the 95% intervals over 20 blind seeds at Quaia-like depth (100 bin-trials)")
cov_v=0; cov_d=0; trials=0; cov_vn=0; cov_dn=0; pullA=[]; pullB=[]; store=[]
for sd in range(20):
    r2=np.random.default_rng(100+sd); vv=r2.uniform(200,600); dd=r2.normal(size=3); dd/=np.linalg.norm(dd)
    vecs,z,S=synth_sky(2_600_000,vv/C_KMS,dd,r2); rr=eb_estimate(vecs,z,S,Z_EDGES,XA,mask,S_LIM,200,r2,measure_x=False)
    for r in rr:
        trials+=1; cov_v+=(r['v_lo']<=vv<=r['v_hi']); ang=math.degrees(math.acos(np.clip(lb_to_vec(r['l'],r['b'])@dd,-1,1))); cov_d+=(ang<=r['cone95'])
        cov_vn+=(r['v_lo_ney']<=vv<=r['v_hi_ney']); cov_dn+=(ang<=r['cone95_ney'])
        Dtrue=(vv/C_KMS)*(2+r['x']*(1+r['alpha']))*dd; e=np.array(r['Dvec'])-Dtrue
        pullA.append(float(e@np.linalg.solve(np.array(r['covA']),e))); pullB.append(float(e@np.linalg.solve(np.array(r['covB']),e))); store.append((r,vv,dd))
fv,fd=cov_v/trials,cov_d/trials
print(f"   coverage: v in 95% range {cov_v}/{trials} = {fv:.3f};  direction in cone95 {cov_d}/{trials} = {fd:.3f}   (binomial 2σ band around 0.95 for 100 trials: [0.906, 0.994])")
sc("P6", 0.89<=fv<=0.99 and 0.89<=fd<=0.99, True, f"bootstrap-percentile 95% intervals: coverage {fv:.2f} (v), {fd:.2f} (direction) over 100 blind bin-trials")
fvn,fdn=cov_vn/trials,cov_dn/trials
print(f"   NEYMAN coverage: v {cov_vn}/{trials} = {fvn:.3f};  direction {cov_dn}/{trials} = {fdn:.3f}")
sc("P8", 0.89<=fvn<=0.99 and 0.89<=fdn<=0.99, True, f"Neyman 95% intervals (addendum 2): coverage {fvn:.2f} (v), {fdn:.2f} (direction) over the same 100 blind bin-trials")
mA,mB=float(np.mean(pullA)),float(np.mean(pullB)); print(f"   pull χ²₃ mean over 100 trials: analytic cov {mA:.2f}, bootstrap cov {mB:.2f} (expected 3.00 ± 0.24)")
sc("P10", 2.4<=mA<=3.6, True, f"analytic Poisson-LS covariance is calibrated: pull mean {mA:.2f} (bootstrap {mB:.2f})")
use='analytic' if 2.4<=mA<=3.6 else 'bootstrap'
cv=0
for r,vv,dd in store:
    D=np.array(r['Dvec']); cov=np.array(r['covA'] if use=='analytic' else r['covB']); amp=2+r['x']*(1+r['alpha'])
    Dlo,Dhi,_=neyman(np.linalg.norm(D),cov,D/np.linalg.norm(D)); cv+=(Dlo/amp*C_KMS<=vv<=Dhi/amp*C_KMS)
print(f"   P11: Neyman rebuilt on the {use} covariance: v-coverage {cv}/100")
sc("P11", 0.89<=cv/100<=0.99, True, f"Neyman on the {use} covariance: v-coverage {cv/100:.2f}")
print("\nADDENDUM P7 — the Ellis–Baldwin amplitude tested where the noise bias is negligible: beta = 0.01 (2998 km/s), 13 M sources")
r3=np.random.default_rng(777); d3=r3.normal(size=3); d3/=np.linalg.norm(d3); v3=0.01*C_KMS
vecs,z,S=synth_sky(26_000_000,0.01,d3,r3); rr=eb_estimate(vecs,z,S,Z_EDGES,XA,mask,S_LIM,0,r3)
ratios=[]
for r in rr:
    ang=math.degrees(math.acos(np.clip(lb_to_vec(r['l'],r['b'])@d3,-1,1))); ratios.append(r['v_db']/v3)
    print(f"   bin {str(r['bin']):12} N {r['N']:8d}  x_meas {r['x_meas']:.3f}  v̂_raw {r['v']:7.1f}  v̂_db {r['v_db']:7.1f}  ± {r['sv_an']:.1f} km/s  ->  v̂_db/v_inj = {r['v_db']/v3:.4f};  direction offset {ang:.2f}°")
sc("P7", all(0.98<q<1.02 for q in ratios), True, f"v̂_db/v_inj per bin = {[round(q,4) for q in ratios]} — 2 + x(1+α) is the right amplitude for aberration + Doppler + flux cut" if all(0.98<q<1.02 for q in ratios) else f"v̂_db/v_inj per bin = {[round(q,4) for q in ratios]} — the amplitude is NOT 2 + x(1+α) at this precision; see the diagnosis below")
wq=np.array([1/r['sv_an']**2 for r in rr]); wm7=float((wq*np.array(ratios)).sum()/wq.sum()); sm7=float(1/math.sqrt(wq.sum())/v3)
sc("P9", 0.97<wm7<1.03, True, f"weighted mean v̂_db/v_inj at β = 0.01 = {wm7:.4f} ± {sm7:.4f} — the Ellis–Baldwin amplitude holds at the {100*sm7:.1f}% level the instrument reaches at 13 M")
print("\n   diagnosis of run 1's +14.5% at 13 M: the noise-bias-corrected count-weighted mean there is", end=" ")
wm_db=sum(r['N']*r['v_db'] for r in resA10)/sum(r['N'] for r in resA10)/v_inj; print(f"v̂_db/v_inj = {wm_db:.4f} (raw was 1.1454); per-bin raw/db: {[ (round(r['v']), round(r['v_db'])) for r in resA10]}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({"sealed_hash":sealed,"injected":{"v":v_inj,"l":float(li[0]),"b":float(bi[0])},"blind_1p3M":resA,"blind_13M":resA10,"named_cmb":resB,"negative":{k:{"K":v_[0].tolist(),"sK":v_[1].tolist(),"I":v_[2].tolist(),"sI":v_[3].tolist(),"corr":list(map(float,v_[4])),"chi2":float(v_[5])} for k,v_ in outN.items()}},open(".record_5757.json","w"),indent=1,default=float)
