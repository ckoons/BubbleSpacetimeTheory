#!/usr/bin/env python3
"""Toy 5749 — R139 E2: C3 re-run as a selection with side A = the TRUE genus/rank."""
import json
from fractions import Fraction as F
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
def domains(maxdim=12, maxrank=3):
    out=[]
    for p in range(1,13):
        for q in range(p,13):
            if p*q<=maxdim and min(p,q)<=maxrank: out.append((f"I_{{{p},{q}}}", p*q, min(p,q), p+q))
    for n in range(2,13):
        d=n*(n-1)//2
        if 0<d<=maxdim and n//2<=maxrank and n//2>=1: out.append((f"II_{n}", d, n//2, 2*n-2))
    for n in range(1,13):
        d=n*(n+1)//2
        if d<=maxdim and n<=maxrank: out.append((f"III_{n}", d, n, n+1))
    for n in range(1,13):
        if n<=maxdim: out.append((f"IV_{n}", n, 2, n))
    return out
D=domains()
print("Side A = genus/rank, genus = (r-1)a + b + 2 from root data (I: p+q, II: 2n-2, III: n+1, IV: n). No BST integer anywhere.")
print(f"{'domain':12} {'dim':>4} {'rank':>5} {'genus':>6}  genus/rank")
for name,d,r,g in sorted(D,key=lambda t:(t[1],t[0])):
    mark=""
    if F(g,r)==F(5,2): mark="  <== 5/2"
    if F(g,r)==F(7,2): mark="  <== 7/2 (the row's target)"
    print(f"{name:12} {d:>4} {r:>5} {g:>6}  {str(F(g,r)):>6}{mark}")
five=[n for n,d,r,g in D if F(g,r)==F(5,2)]; seven=[n for n,d,r,g in D if F(g,r)==F(7,2)]
print(f"\n  genus/rank = 5/2 (D_IV^5's true value): {five}")
print(f"  genus/rank = 7/2 (the row's target, built as (n_C+rank)/rank = g/rank): {seven}")
sc("S1", set(five)=={'I_{2,3}','IV_5'}, True, "5/2 is achieved by TWO domains: D_IV^5 (dim 5) and D_I_{2,3} (dim 6, genus 5, rank 2)")
sc("S2", set(seven)=={'I_{2,5}','IV_7'}, True, "7/2 is achieved by TWO domains: D_IV^7 (dim 7) and D_I_{2,5} (dim 10, genus 7, rank 2)")
print("  the row's own D_IV line wrote side A as (n+2)/2, i.e. (n_C + rank)/rank = g/rank, while its competitor column used the")
print("  TRUE type I genus (p+q)/min(p,q). Two kinds of object across two domains — Cal's finding, priced here:")
print(f"   under the row's target 7/2: D_IV^5 is EXCLUDED (its true value is 5/2) and {len(seven)} other domains are admitted")
print(f"   under the honest target 5/2: D_IV^5 is admitted together with {len(five)-1} other domain(s)")
sc("S3", len(five)>1 and len(seven)>1, True, "under NEITHER target does C3 uniquely select anything — the criterion has no discriminating power at rank 2")
print("\n  REFUSAL CARRIED: this is a fact about one broken criterion. It is not a proposal to change domains and I make none.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'five_halves':five,'seven_halves':seven,'table':[[n,d,r,g,str(F(g,r))] for n,d,r,g in D]}, open('.record_5749.json','w'), indent=1)
