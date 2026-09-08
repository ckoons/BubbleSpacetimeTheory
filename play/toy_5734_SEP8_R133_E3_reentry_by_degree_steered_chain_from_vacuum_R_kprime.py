#!/usr/bin/env python3
import numpy as np, json
exec(open('.r133_lib.py').read())
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
rng=np.random.default_rng(5734); kenv=68; nwalk=300; K=8
us,th=sample_dirs(kenv,nwalk*K,rng); Ecos2=float(np.mean(np.cos(th)**2))
R=np.zeros((nwalk,K))
for t in range(nwalk):
    Y=np.ones(1); k=0
    for s in range(K):
        u=us[t*K+s]; Y=harmonic_part(mult_lin(u,Y,k),k+1); k+=1; Y/=np.sqrt(ip(Y,Y,k)); R[t,s]=zonal_weight(Y,k)
m=R.mean(0); e=R.std(0)/np.sqrt(nwalk)
def dimH(k): return (2*k+3)*(k+1)*(k+2)//6
print(f"  E[cos^2 θ] under |Z_68|^2 density = {Ecos2:.4f}")
for kp in range(1,K+1): print(f"  k'={kp}: R = {m[kp-1]:.3f} ± {e[kp-1]:.3f}    (env norm share 1-1/d = {1-1/dimH(kp):.4f} — NOT a re-entry fraction)")
mono=all(m[i+1] <= m[i] + 2*(e[i]+e[i+1]) for i in range(K-1)); r1ok=abs(m[0]-Ecos2)<3*e[0]+0.01
sc("E3", mono and r1ok, True, f"R(1) = {m[0]:.3f} vs E[cos^2θ] = {Ecos2:.3f}; monotone non-increasing (within 2σ): {mono}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'R':m.tolist(),'err':e.tolist(),'Ecos2':Ecos2}, open('.record_5734.json','w'))
