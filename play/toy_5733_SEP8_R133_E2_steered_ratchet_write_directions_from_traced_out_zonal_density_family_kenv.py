#!/usr/bin/env python3
import numpy as np, json
exec(open('.r133_lib.py').read())
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
rng=np.random.default_rng(5733)
def run(kenv, nwalk=200, nw=6, k0=2):
    W=np.zeros((nwalk,nw))
    for t in range(nwalk):
        Y=zonal(k0); k=k0; us,_=sample_dirs(kenv,nw,rng)
        for s in range(nw):
            Y=harmonic_part(mult_lin(us[s],Y,k),k+1); k+=1; Y/=np.sqrt(ip(Y,Y,k)); W[t,s]=zonal_weight(Y,k)
    return W.mean(0), W.std(0)/np.sqrt(nwalk)
out={}
m,e=run(0); out[0]=(m.tolist(),e.tolist()); print(f"  Haar: after 1..6 writes: {[f'{x:.3f}±{y:.3f}' for x,y in zip(m,e)]}")
sc("S1", abs(m[0]-0.244)<3*(e[0]+0.037) and m[-1]<0.05, False, "5731 reproduced (0.24 / ~0.01)")
for kenv in (2,5,10,20,68):
    m,e=run(kenv); out[kenv]=(m.tolist(),e.tolist()); print(f"  k_env={kenv}: after 1..6 writes: {[f'{x:.3f}±{y:.3f}' for x,y in zip(m,e)]}")
sc("S2", out[68][0][-1]>0.5, True, f"k_env=68 six-write weight {out[68][0][-1]:.3f} > 0.5")
six=[out[k][0][-1] for k in (2,5,10,20,68)]
sc("S3", all(six[i]<six[i+1] for i in range(4)), True, f"six-write weight vs k_env: {[f'{x:.3f}' for x in six]} monotone rising")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({str(k):v for k,v in out.items()}, open('.record_5733.json','w'))
