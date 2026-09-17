#!/usr/bin/env python3
"""Toy 5767 — R155 E1: does the FALLBACK (one whole-sample selection map as the weight for every bin) produce per-bin moments that RISE with
redshift and point one way, as run 1's did (G<20.5 |D_resp| 0.034 / 0.037 / 0.037 / 0.056 / 0.063, coherent; K1910: Landing C)?
Model of the error: the true per-bin selection is s_i(n̂) = s_all(n̂)^{γ_i} (fainter/higher-z sources more sensitive to the same dust/stars/scanning
templates: γ rises with bin); the fallback weights by 1/s_all, leaving a residual density s_all^{γ_i − 1}, whose ℓ = 1 moment is, to first order,
(γ_i − 1)·d_s with d_s = the LS dipole of ln s_all over the footprint — computed from the PUBLISHED G<20.5 map (a (v)-level object; no catalogue).
Synthetic: Quaia-depth boosted sky (P1 true, 369.82 toward the CMB apex, σ_z 0.04), sources thinned per observed bin by s_all(n̂)^{γ_i}, weighted
1/s_all, footprint mask ∧ s_all ≥ 0.5, LS dipole per bin, joint fit of 5766's design (ζ + prior). γ_i = 1 + 0.35·(i − 1) (i = 1..5; the choice of
slope is the toy's one knob, declared; the SHAPE is the prediction, not the size). 5 seeds.
PREDICTIONS (σ = seed spread/√5, printed; ±2.5σ): P1 the residual moment D_i − f_i b_true − (mock mean) is LINEAR in (γ_i − 1): slope vector
= d_s within ±2.5σ per component (bins 2–5), and bin 1 (γ = 1) residual = 0 within ±2.5σ. P2 all five residuals point within 15° of d_s (γ_i > 1).
P3 the joint fit's profile-alternative shift exceeds 2σ_β (the sky's signature) — the trigger that landed run 1 in C fires on this error too.
MEASURED, not predicted: the angle between d_s and run 1's bin-5 D_resp direction (posted 18:36; NOT the CMB): < 30° would say the fallback
explains the sky's shape and direction; larger says the shape may be explained and the direction is not."""
import sys, math, json, time, resource, hashlib
import numpy as np
sys.path.insert(0,'.'); import r145_eb_lib as L; import partB_v151_lib as V
from r145_eb_lib import C_KMS
from astropy.io import fits; import healpy as hp
TOY='5767'; NSEED=5; NSIDE=64; NPIX=12*NSIDE**2; GAM=np.array([1.0,1.35,1.70,2.05,2.40])
vc=L.lb_to_vec(264.02,48.25); BC=369.82/C_KMS; ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; E=[0,0.8,1.3,1.8,2.4,np.inf]; mask=L.make_mask(30.0); NGEN=int(913_899/0.32)
RG=np.array([[-0.0548755604162154,-0.8734370902348850,-0.4838350155487132],[0.4941094278755837,-0.4448296299600112,0.7469822444972189],[-0.8676661490190047,-0.1980763734312015,0.4559837761750669]])
print(f"toy {TOY}; lib {L.lib_hash()}; file {hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]}; γ = {GAM.tolist()}")
s_all=np.array(fits.open('../data/quaia/selection_function_NSIDE64_G20.5.fits')[1].data.field(0)).reshape(-1).astype(float)
def s_of(v):   # galactic unit vectors -> published map value (ICRS pixel)
    vi=v@RG; ra=np.degrees(np.arctan2(vi[:,1],vi[:,0]))%360; dec=np.degrees(np.arcsin(np.clip(vi[:,2],-1,1))); return s_all[hp.ang2pix(NSIDE,np.radians(90-dec),np.radians(ra))]
# d_s: LS dipole of ln s_all over footprint cells (cell value = mean of ln s over the cell's pixels via the cell centres' map values at 8 sub-points)
sc=s_of(L.CELLS.center); foot=mask&(sc>=0.5); eps=np.log(np.maximum(sc,1e-3)); X=np.column_stack([np.ones(foot.sum()),L.CELLS.center[foot]]); p=np.linalg.lstsq(X,eps[foot],rcond=None)[0]; d_s=p[1:]
lb=L.vec_to_lb(d_s); print(f"d_s (LS dipole of ln s_all over the footprint, {foot.sum()} cells) = {np.round(d_s,4).tolist()}, |d_s| = {np.linalg.norm(d_s):.4f} toward ({float(lb[0][0]):.1f}, {float(lb[1][0]):.1f})")
sky5=np.array([-0.05172,-0.01721,0.03144]); ang_sky=math.degrees(math.acos(float(d_s@sky5)/np.linalg.norm(d_s)/np.linalg.norm(sky5)))
def run(seed):
    rng=np.random.default_rng(6000+seed); n,z,zp,S=L.synth_sky_full(NGEN,BC,vc,rng,ZEG,XG,1.0,1.0,sigma_z=0.04); s=s_of(n); ok=s>=0.5; b_idx=np.clip(np.searchsorted(E,zp,side='right')-1,0,4)
    keep=ok&(rng.uniform(size=len(n))<s**GAM[b_idx]); n=n[keep]; zp=zp[keep]; S=S[keep]; s=s[keep]; w=1/s; idx=L.CELLS.index(n); rows=[]; res=[]
    for i in range(5):
        sel=(zp>=E[i])&(zp<E[i+1]); cnt=np.bincount(idx[sel],weights=w[sel],minlength=L.CELLS.n); cnt[~foot]=0; D,cov=L.dipole_ls(cnt,foot)
        x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,E[i],E[i+1],sel.sum()); f=2+2*x+B
        # mock mean under the same footprint/weights with γ = 1 (the estimator's own offset), 200 mocks
        m=np.zeros(3); Nsel=int(sel.sum())
        for k in range(200):
            v=rng.normal(size=(int(Nsel*2.6),3)); v/=np.linalg.norm(v,axis=1)[:,None]; sv=s_of(v); kk=(np.abs(v[:,2])>0.5)&(sv>=0.5); v=v[kk][:Nsel]; sv=sv[kk][:Nsel]; cm=np.bincount(L.CELLS.index(v),weights=1/sv,minlength=L.CELLS.n); cm[~foot]=0; m+=L.dipole_ls(cm,foot)[0]/200
        rows.append(dict(D=D,cov=cov,f=f,zmed=float(np.median(zp[sel])),N=Nsel)); res.append(D-f*BC*vc-m)
    Ds=[r['D'] for r in rows]; Cs=[r['cov'] for r in rows]; fs=[0.0 if abs(r['f'])<0.3 else r['f'] for r in rows]; zm=[r['zmed'] for r in rows]; w_=list(np.array(L.profile_w([0.57,1.06,1.54,2.06,2.71]))); chis=[L.comoving(zz) for zz in zm]; walt=[chis[0]/c for c in chis]
    R,CR=L.redshift_dipole(idx,zp,mask); g=1+float(zp.mean()); zeta,_=V.zeta_from_table([r['N'] for r in rows],w_,zm)
    def fitp(wv):
        G=np.zeros((6,6)); r=np.zeros(6)
        for D,C,f,wi in zip(Ds,Cs,fs,wv): W=np.linalg.inv(C); J=np.hstack([f*np.eye(3),wi*np.eye(3)]); G+=J.T@W@J; r+=J.T@W@D
        W=np.linalg.inv(CR); J=np.hstack([g*np.eye(3),-zeta*np.eye(3)]); G+=J.T@W@J; r+=J.T@W@(-R); G[3:,3:]+=np.eye(3)/3.4e-3**2; cov=np.linalg.inv(G); pp=cov@r; return pp[:3],cov
    b,cov=fitp(w_); b2,_=fitp(walt); be=np.linalg.norm(b); sb=math.sqrt((b/be)@cov[:3,:3]@(b/be)); shift=(np.linalg.norm(b2)-be)/sb
    return np.array(res),[math.sqrt(c[0,0]) for c in Cs],shift,be*C_KMS,sb*C_KMS
t0=time.time(); R=[run(s) for s in range(NSEED)]; res=np.array([r[0] for r in R]); mean=res.mean(0); se=res.std(0,ddof=1)/math.sqrt(NSEED); shifts=[r[2] for r in R]
print("per-bin residual moment (D_i − f_i b_true − mock offset), mean ± σ_mean over 5 seeds, and its prediction (γ_i − 1)·d_s:")
hits_lin=[]; angs=[]
for i in range(5):
    pred=(GAM[i]-1)*d_s; ok=np.all(np.abs(mean[i]-pred)<=2.5*se[i]); hits_lin.append(ok); a=math.degrees(math.acos(float(mean[i]@d_s)/np.linalg.norm(mean[i])/np.linalg.norm(d_s))); angs.append(a)
    print(f"   bin {i+1} (γ {GAM[i]:.2f}): |res| {np.linalg.norm(mean[i]):.4f} res = {np.round(mean[i],4).tolist()} ± {np.round(se[i],4).tolist()}; predicted {np.round(pred,4).tolist()}; angle to d_s {a:.0f}° → {'in band' if ok else 'OUT'}")
P1=all(hits_lin); P2=all(a<15 for a in angs[1:]); P3=all(abs(s)>2 for s in shifts)
print(f"\nP1 linear in (γ−1) with slope d_s, bin 1 = 0: {'HIT' if P1 else 'MISS'} | P2 directions within 15° of d_s (bins 2–5): {'HIT' if P2 else 'MISS'} (angles {np.round(angs,0).tolist()}) | P3 profile-alt shift > 2σ_β every seed: {'HIT' if P3 else 'MISS'} (shifts {np.round(shifts,2).tolist()}; β̂ {np.mean([r[3] for r in R]):.0f} ± {np.mean([r[4] for r in R]):.0f} vs 370 injected)")
print(f"SCORE {sum([P1,P2,P3])}/3  (3 can fail)")
print(f"MEASURED: angle between d_s and run 1's bin-5 D_resp direction = {ang_sky:.0f}° ({'< 30°: the fallback explains shape AND direction' if ang_sky<30 else '≥ 30°: the shape can be explained by the fallback, the direction is not this map dipole'}); |res| rises with bin: {[round(float(np.linalg.norm(m)),4) for m in mean]} vs the sky's 0.034/0.037/0.037/0.056/0.063")
json.dump(dict(d_s=d_s.tolist(),res_mean=mean.tolist(),res_se=se.tolist(),shifts=shifts,ang_sky=ang_sky,score=[bool(P1),bool(P2),bool(P3)]),open(f'.record_{TOY}.json','w'),indent=1); print(f"time {time.time()-t0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
