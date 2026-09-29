#!/usr/bin/env python3
"""
Toy 5846 — w = z_t·z_s⁻¹ on the corpus's named objects (Elie, 2026-09-29, round 20). Prereg fefd8f62.
Families/sources: H² (λ = 5/2, K-types P_λ), Rac (λ = 3/2, K-types H_m(C^5) at 3/2+m), Di (spinor singleton, K-types SO(5) (m+½,½)
at 2+m — pin OWED), all restricted to SO(4)×SO(2); z_t = (−1)^{2·weight}, z_s = (−1)^{2mL+2mR}, read weight by weight.
"""
import glob, io, contextlib
from fractions import Fraction as Fr
from collections import Counter
from itertools import combinations_with_replacement as cwr
src = open(glob.glob('play/toy_5792_*.py')[0]).read(); ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("def irreps")], ns)
weights = ns['weights']
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
def so4(C):   # SO(5) weight (a,b) -> doubled SU(2)xSU(2) coords (2mL, 2mR) = (a+b, a−b)
    out = Counter()
    for (a, b), v in C.items(): out[(a + b, a - b)] += v
    return out
DEPTH = 5
H2 = {Fr(5, 2) + L: so4(sum((harm(L - 2*l2) for l2 in range(L//2 + 1)), Counter())) for L in range(DEPTH + 1)}
RAC = {Fr(3, 2) + m: so4(harm(m)) for m in range(DEPTH + 1)}
DI = {Fr(2) + m: so4(Counter(weights((Fr(2*m + 1, 2), Fr(1, 2))))) for m in range(DEPTH + 1)}
check("Di model sanity: dim of SO(5) (m+½,½) = 4, 16, 40, 80 (spinor harmonics on S⁴)", [sum(DI[Fr(2) + m].values()) for m in range(4)] == [4, 16, 40, 80],
      str([sum(DI[Fr(2) + m].values()) for m in range(4)]))
def signs(G):
    out = set()
    for w, C in G.items():
        zt = 1 if (2*w) % 2 == 0 else -1
        for (x, y), v in C.items():
            if v: out.add((zt, 1 if (x + y) % 2 == 0 else -1))
    return out
def wval(G):
    s = signs(G); return {zt*zs for zt, zs in s}, s
res = {}
for name, G in (("H² mode", H2), ("Rac", RAC), ("Di", DI)):
    wv, s = wval(G); res[name] = wv
    print(f"   {name:8s}: (z_t, z_s) = {sorted(s)}  ⇒ w = {sorted(wv)}")
check("CONTROL: a single H² mode has w = −1 on every K-type (constant: central)", res["H² mode"] == {-1})
check("DIRECTION: the Rac (single singleton) has w = −1 (via z_t = −1, z_s = +1)", res["Rac"] == {-1})
check("DIRECTION: the Di (single singleton) has w = −1 (via z_t = +1, z_s = −1)", res["Di"] == {-1})
def tensor(G1, G2, depth=3):
    T = {}
    k1 = sorted(G1)[:depth + 1]; k2 = sorted(G2)[:depth + 1]
    for w1 in k1:
        for w2 in k2:
            C = T.setdefault(w1 + w2, Counter())
            for (a, b), u in G1[w1].items():
                for (c, d), v in G2[w2].items(): C[(a + c, b + d)] += u*v
    return T
pairs = [("Rac⊗Rac (photon, K1650)", RAC, RAC), ("Rac⊗Di", RAC, DI), ("Di⊗Di", DI, DI), ("H²⊗H²", H2, H2), ("H²⊗Rac", H2, RAC), ("H²⊗Di", H2, DI)]
okp = True
for name, A, B in pairs:
    wv, s = wval(tensor(A, B))
    print(f"   {name:24s}: (z_t, z_s) = {sorted(s)}  ⇒ w = {sorted(wv)}")
    if wv != {1}: okp = False
    if name.startswith("Rac⊗Rac"): photon = wv
check("CONTROL: the photon (Rac⊗Rac bilinear) has w = +1 (full tensor-product character, every weight)", photon == {1})
check("DIRECTION: EVERY bilinear of singletons / H² modes has w = +1 (6 products, full characters)", okp)
print("\nREADING: w counts the number of singleton / H² constituents mod 2 — every single object (Rac, Di, one H² mode) is w-odd, every")
print("bilinear is w-even. So in BST's own reading: a particle read as ONE H² K-type mode (K1653) is w = −1; a particle read as a TWO-")
print("singleton composite (Time, Derived Section 7) is w = +1. Which a proton/electron/photon/neutrino is, is the corpus's reading (Lyra).")
print(f"\nSCORE: {sum(score)}/{len(score)}")
