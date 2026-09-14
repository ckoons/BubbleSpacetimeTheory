#!/usr/bin/env python3
"""Toy — R151 E1: joint-fit σ_β on synthetic Quaia at σ_z = 0.04(1+z), for the two samples: G<20.5 (913.5k in the mask, five bins) and
G<20.0 (528.3k, bins 1+5 merged into their neighbours per §2.6 -> three bins). 20 seeds each. No freeze line; synthetic only."""
import math, json, os
import numpy as np
import r145_eb_lib as L
from r145_eb_lib import C_KMS
TOY=os.path.basename(__file__).split('_')[1]; print(f"toy {TOY}; lib hash {L.lib_hash()}")
ZEG=[0.0,0.8,1.3,1.8,2.4,4.0]; XG=[0.9,1.0,1.1,1.2,1.3]; AL=1.0; mask=L.make_mask(30.0); vc=L.lb_to_vec(264.02,48.25); bc=369.82/C_KMS
def run(N_target,edges,label,sig_z=0.04):
    res=[]; Ngen=int(N_target/0.32)                     # 0.64 survive the flux cut × 0.50 of the sky in the mask
    for sd in range(20):
        rng=np.random.default_rng(2000+sd); n,z,zp,S=L.synth_sky_full(Ngen,bc,vc,rng,ZEG,XG,AL,1.0,sigma_z=sig_z)
        idx=L.CELLS.index(n); rows=[]
        for i in range(len(edges)-1):
            sel=(zp>=edges[i])&(zp<edges[i+1]); cnt=np.bincount(idx[sel],minlength=L.CELLS.n); cnt[~mask]=0; D,cov=L.dipole_ls(cnt,mask)
            x=L.measure_x(S[sel],1.0); B=L.membership_term(zp,edges[i],edges[i+1],sel.sum()); rows.append(dict(D=D,cov=cov,f=2+x*(1+AL)+B,zmed=float(np.median(zp[sel])),N=int(cnt[mask].sum())))
        w=L.profile_w([r['zmed'] for r in rows]); R,CR=L.redshift_dipole(idx,zp,mask); g=1+float(zp.mean())
        b,a,cov=L.joint_two_channel([r['D'] for r in rows],[r['cov'] for r in rows],[r['f'] for r in rows],w,[R],[CR],[g]); be,sb,u,A,sA=L.fit_summary(b,a,cov)
        bC,aC,covC=L.joint_two_channel([r['D'] for r in rows],[r['cov'] for r in rows],[r['f'] for r in rows],w,[],[],[]); beC,sbC,_,_,_=L.fit_summary(bC,aC,covC)
        res.append((sum(r['N'] for r in rows),sb*C_KMS,sbC*C_KMS,be/bc,[r['f'] for r in rows]))
    a=np.array([(r[0],r[1],r[2],r[3]) for r in res]); print(f"   {label}: N in mask = {a[:,0].mean():,.0f}; quoted σ_β c JOINT = {a[:,1].mean():.0f} km/s (seed spread {a[:,1].std(ddof=1):.0f}); count-only {a[:,2].mean():.0f}; mean β̂/β_inj {a[:,3].mean():.3f}; f_i (seed 0) = {[round(f,2) for f in res[0][4]]}")
    return float(a[:,1].mean()),float(a[:,2].mean())
print("E1 — joint σ_β at Quaia's σ_z = 0.04(1+z):")
s205=run(913_551,[0.0,0.8,1.3,1.8,2.4,np.inf],"G < 20.5, five bins  ")
s200=run(528_297,[0.0,1.3,1.8,np.inf],"G < 20.0, bins 1+5 merged (3 bins)")
print(f"\n   Cal's 4.4 bar: 185 km/s.  G<20.5: {'A/B-capable' if s205[0]<185 else 'C by construction'} ({s205[0]:.0f});  G<20.0: {'A/B-capable' if s200[0]<185 else 'C by construction'} ({s200[0]:.0f})")
print("   control: the same at σ_z = 0.01(1+z), G<20.5:"); s_ctl=run(913_551,[0.0,0.8,1.3,1.8,2.4,np.inf],"G < 20.5, σ_z 0.01    ",0.01)
json.dump({"G20.5":s205,"G20.0_merged":s200,"G20.5_sigz0.01":s_ctl},open(f".record_{TOY}.json","w"),indent=1)
