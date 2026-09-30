#!/usr/bin/env python3
"""
Toy 5855 — Rac⊗Di of SO(5,2) by K-type counting (Elie, 2026-09-30, round 25). Prereg 68892228.
Families: Rac₅ (K-types H_m(C^5) at 3/2+m), Di₅ (SO(5) (m+½,½) at 2+m); K = SO(5)xSO(2); SO(5) weights by Freudenthal (5792).
"""
import glob, io, contextlib
from fractions import Fraction as Fr
from collections import Counter
from itertools import combinations_with_replacement as cwr
src = open(glob.glob('play/toy_5792_*.py')[0]).read(); ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("def spin_peel")], ns)   # run 1 stopped before peel (KeyError)
weights, peel = ns['weights'], ns['peel']
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
V5 = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
def sym(L):
    C = Counter()
    for combo in cwr(range(5), L): C[tuple(Fr(sum(V5[k][i] for k in combo)) for i in range(2))] += 1
    return C
def harm(m):
    C = sym(m)
    if m >= 2: C.subtract(sym(m - 2))
    return +C
def chi(hw): return Counter(weights(tuple(Fr(x) for x in hw)))
def mul(A, B):
    C = Counter()
    for a, x in A.items():
        for b, y in B.items(): C[(a[0] + b[0], a[1] + b[1])] += x*y
    return C
DEPTH = 5
RAC = {Fr(3, 2) + m: harm(m) for m in range(DEPTH + 1)}
DI = {Fr(2) + m: chi((Fr(2*m + 1, 2), Fr(1, 2))) for m in range(DEPTH + 1)}
SYM = [sym(L) for L in range(DEPTH + 1)]
def tensor(A, B, top):
    T = {}
    for w1, C1 in A.items():
        for w2, C2 in B.items():
            if w1 + w2 <= top: T.setdefault(w1 + w2, Counter()).update(mul(C1, C2))
    return T
w0 = Fr(7, 2); top = w0 + DEPTH
RD = tensor(RAC, DI, top)
low = min(RD); comps = peel(+RD[low], 2)
print(f"   Rac⊗Di lowest weight {low}; SO(5) content there: {[(tuple(map(str, h)), d) for h, d in comps]}")
check("(1) lowest K-type of Rac⊗Di: weight 7/2, SO(5) spinor (½,½), multiplicity 1 — exactly K1653's electron K-type V_(1/2,1/2)",
      low == Fr(7, 2) and len(comps) == 1 and comps[0][0] == (Fr(1, 2), Fr(1, 2)))
def module(D, hw, conserved_prev=None):
    G = {}
    for L in range(DEPTH + 1):
        w = D + L
        if w > top: break
        G.setdefault(w, Counter()).update(mul(chi(hw), SYM[L]))
        if conserved_prev is not None and w + 1 <= top:
            G.setdefault(w + 1, Counter()).subtract(mul(chi(conserved_prev), SYM[L]))
    return G
def predicted(conserve=True):
    P = {}
    s = Fr(1, 2)
    while 3 + s <= top:
        prev = (s - 1, Fr(1, 2)) if (conserve and s >= Fr(3, 2)) else None
        for w, c in module(3 + s, (s, Fr(1, 2)), prev).items(): P.setdefault(w, Counter()).update(c)
        s += 1
    return P
def same(A, B):
    return all(+Counter({k: v for k, v in A.get(w, Counter()).items()}) == +Counter({k: v for k, v in B.get(w, Counter()).items() if v}) and
               all(v >= 0 for v in B.get(w, Counter()).values()) for w in set(A) | set(B) if w <= top)
check("(2) character identity to depth 5: Rac⊗Di = [generic spin-½ at 7/2] ⊕ Σ_{s≥3/2} [conserved spin-s at 3+s] (half-integer Flato–Fronsdal)",
      same(RD, predicted(True)))
check("(2) NEGATIVE: with GENERIC characters for every s the identity FAILS (conservation is real for s ≥ 3/2)", not same(RD, predicted(False)))
# (3) control: 5822's Rac⊗Rac identity, re-run silently
s22 = open(glob.glob('play/toy_5822_*.py')[0]).read(); n22 = {}
with contextlib.redirect_stdout(io.StringIO()): exec(s22[:s22.index('check("CONTROL so(3,2)')], n22)
check("(3) CONTROL Rac⊗Rac (5822): scalar at 3 + conserved currents at 3 + s, identity holds (d = 5, depth 6)", n22['test'](5, 6, True))
# (4) negative control: Di⊗Di has no half-integer-spin K-type at all
DD = tensor(DI, DI, Fr(4) + DEPTH)
halfspin = any(any(k[0].denominator == 2 for k, v in C.items() if v) for C in DD.values())
lowDD = min(DD); compsDD = peel(+DD[lowDD], 2)
print(f"   Di⊗Di lowest weight {lowDD}; content {[(tuple(map(str, h)), d) for h, d in compsDD]}")
check("(4) NEGATIVE CONTROL Di⊗Di: no half-integer-spin K-type anywhere (no electron K-type); lowest weight 4 = (1,1)⊕(1,0)⊕(0,0)",
      not halfspin and lowDD == 4 and sorted(h for h, _ in compsDD) == sorted([(Fr(1), Fr(1)), (Fr(1), Fr(0)), (Fr(0), Fr(0))]))
print("   [arithmetic, not scored] (5) the lowest summand is not at a conservation bound: 7/2 > 2 (spinor endpoint, 5853) ⇒ generic irreducible module")
print("\nREADING: Rac⊗Di's lowest summand is ONE spinor module at weight 7/2, lowest K-type (½,½) with multiplicity one — K1653's electron")
print("K-type — generic (not conserved); the higher pieces s ≥ 3/2 are conserved at 3+s. Di⊗Di carries no spinor at all. Cal rules the identification.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
