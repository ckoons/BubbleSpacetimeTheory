#!/usr/bin/env python3
"""Keeper K1927 instrument: scalar holomorphic reps of SO(n,2) restricted to SO(n-1,2), by K-types.
K-types of H_lam(D_IV^n): S(C^n) (x) C_lam, S^d = sum_j H^{d-2j} Q^j, SO(2)-weight lam+d.
Full-range module (lam > (n-2)/2): all (m=d-2j, w=lam+m+2j).  Wallach point lam=(n-2)/2: harmonics only (m, lam+m).
SO(n)->SO(n-1) (Gelfand-Tsetlin): H^m(C^n) -> sum_{l=0}^m H^l(C^{n-1}).
Types for the subgroup are labelled (l, w) with l = SO(n-1) harmonic degree, w = SO(2) weight (Fractions)."""
from fractions import Fraction as F
from collections import Counter
W=40  # weight cutoff above base
def module(lam, wallach, cut):
    c=Counter()
    for m in range(cut+1):
        for j in range(0 if not wallach else 0, (cut-m)//2+1 if not wallach else 1):
            w=lam+m+2*j
            if w<=lam+cut: c[(m,w)]+=1
    return c
def restrict(mod):  # SO(n) harmonic degree m -> SO(n-1) degrees l<=m, same weight
    c=Counter()
    for (m,w),k in mod.items():
        for l in range(m+1): c[(l,w)]+=k
    return c
def direct_sum(parts):
    c=Counter()
    for p in parts: c.update(p)
    return c
def trunc(c,top): return Counter({k:v for k,v in c.items() if k[1]<=top})
ok=True
def check(name,a,b):
    global ok; r=(a==b); ok&=r; print(f"[{'PASS' if r else 'FAIL'}] {name}")
# 1. Hardy space of D_IV^5 (lam=5/2, full range) restricted = sum_k H_{5/2+k}(D_IV^4)
lam=F(5,2); top=lam+W
A=trunc(restrict(module(lam,False,W)),top)
B=trunc(direct_sum(module(lam+k,False,W) for k in range(W+1)),top)
check("H^2(D_IV^5)=H_{5/2} restricts to sum_k H_{5/2+k}(D_IV^4)",A,B)
# 2. Negative control: dropping one summand must FAIL
B2=trunc(direct_sum(module(lam+k,False,W) for k in range(W+1) if k!=3),top)
r=(A==B2); print(f"[{'PASS' if not r else 'FAIL'}] control: omitting k=3 is detected"); ok&=(not r)
# 3. Hydrogen = Wallach point of D_IV^4 (lam=1): K-types harmonics only, (l+1)^2 at weight n=l+1
H=module(F(1),True,W)
dims=[(l+1)**2 for (l,w) in sorted(H) ][:6]; print("   hydrogen K-types (SO(4) dim at weight n):",[(int(w),(l+1)**2) for (l,w) in sorted(H)][:6])
check("hydrogen shell n has dim n^2 and SO(2)-weight n", H, Counter({(n-1,F(n)):1 for n in range(1,W+2)}))
# 4. Does weight 1 (hydrogen) occur in the restriction of any unitary scalar module of SO(5,2)?
# Wallach set of D_IV^5: {0} U [3/2, inf). Summands have weights lam+k >= lam >= 3/2 > 1.
print("   Wallach set D_IV^5 = {0} U [3/2,oo); summand weights lam+k >= 3/2 > 1 => hydrogen (lam=1) never a summand (lam=0 is the trivial rep)")
# 5. Minimal rep of SO(5,2) (lam=3/2, harmonics only) restricts to H_{3/2}(D^4) + H_{5/2}(D^4)
lam=F(3,2); top=lam+W
A=trunc(restrict(module(lam,True,W)),top)
B=trunc(direct_sum([module(F(3,2),False,W),module(F(5,2),False,W)]),top)
check("minimal rep of SO(5,2) restricts to H_{3/2}(D^4) + H_{5/2}(D^4)",A,B)
# 6. Recapitulation: the minimal rep of D_IV^5 at weight 3/2+m holds exactly the spinless hydrogen states n<=m+1
for m in range(6):
    s=sum((l+1)**2 for l in range(m+1)); d=(m+1)*(m+2)*(2*m+3)//6
    assert s==d
print("[PASS] SO(5) harmonic degree m = hydrogen shells n=1..m+1 filled: dims",[(m+1)*(m+2)*(2*m+3)//6 for m in range(6)])
print("VERDICT:", "ALL PASS" if ok else "FAILURE")
