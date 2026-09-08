#!/usr/bin/env python3
import itertools, math, json
from fractions import Fraction as F
score=[]
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
base={'rank':2,'N_c':3,'n_C':5,'C2':6,'g':7,'N_max':137}; fc=F(9,47)
print(f"as written: f_c*C2 = {fc*6} = {float(fc*6):.3f}")
def hits(target):
    lo,hi=target/3,target*3; found={}
    for exps in itertools.product(range(3), repeat=6):
        for s in (-1,0,1):
            v=F(1)
            for (k,b),e in zip(base.items(),exps): v*=F(b)**e
            v*= fc**s
            if lo<=float(v)<=hi: found.setdefault(v, (exps,s))
    return found
h=hits(1e4); print(f"BST monomials in [1e4/3, 3e4]: {len(h)} distinct values; examples:", sorted((float(v), dict(zip(base, e)), s) for v,(e,s) in h.items())[:8])
sc("L1", len(h)>=20, f"{len(h)} >= 20: the window is reached by dozens of products; the fragment selects none")
hc=hits(7919); print(f"control target 7919: {len(hc)} distinct values")
sc("L2", len(hc)>=20, f"{len(hc)} >= 20: the window does the work")
print(f"\nSCORE {sum(score)}/{len(score)}, both can-fail")
json.dump({'hits_1e4':len(h),'hits_7919':len(hc)}, open('.record_5728.json','w'))
