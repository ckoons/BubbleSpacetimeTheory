#!/usr/bin/env python3
"""
Toy 5816 — H_{5/2} ⊗ H_{5/2} for SO(5,2) by triangular peeling of K = SO(5)×SO(2) characters (Elie, 2026-09-26, round 8 item 1).
Prereg 75daf52b. Antecedent (prompt, verbatim): "the SL(2,ℝ) case (H_a ⊗ H_b = ⊕_k H_{a+b+2k}, Repka's model)" — weight-2-step
convention; in the J-eigenvalue (unit-step) convention used here it reads ⊕_k D_{a+b+k}.
INVARIANTS: SO(2) clock weight; SO(5) highest weights (Freudenthal, reused verbatim from toy 5792).
H_{5/2} K-character (continuous Wallach region, Schmid): Σ_L t^{5/2+L} Sym^L(C^5).
ASSUMPTION (tested by self-consistency): each summand has character t^w · τ ⊗ Sym(C^5) (generalized Verma module, irreducible).
"""
import glob
from fractions import Fraction as Fr
from collections import Counter
from itertools import product, combinations_with_replacement as cwr
src = open(glob.glob('play/toy_5792_*.py')[0]).read()
ns = {}; exec(src[:src.index("def irreps")], ns)
weights, weyl_dim = ns['weights'], ns['weyl_dim']
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# ---- SL(2,R) control ----
def sl2(a, b, depth):
    T = Counter({a + b + k: k + 1 for k in range(depth)})       # (1-t)^-2 coefficients
    out = []
    for w in sorted(T):
        m = T[w]
        if m < 0: return None
        if m:
            out.append((w, m))
            for j in range(depth):
                if w + j in T: T[w + j] -= m
    return out
c = sl2(Fr(5, 2), Fr(5, 2), 12)
check("CONTROL SL(2,R): D_{5/2}⊗D_{5/2} = ⊕_k D_{5+k}, each once (unit-step convention = the prompt's ⊕ H_{a+b+2k})",
      c == [(5 + k, 1) for k in range(12)], str(c[:4]))
# ---- SO(5) machinery ----
V5 = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
def F(w): return tuple(Fr(x) for x in w)
def sym(L):
    C = Counter()
    for combo in cwr(range(5), L): C[F(tuple(sum(V5[k][i] for k in combo) for i in range(2)))] += 1
    return C
def mul(A, B):
    C = Counter()
    for a, x in A.items():
        for b, y in B.items(): C[(a[0]+b[0], a[1]+b[1])] += x*y
    return C
WC = {}
def irr(hw):
    if hw not in WC: WC[hw] = Counter(weights(hw))
    return WC[hw]
def peel_so5(C):
    C = Counter({k: v for k, v in C.items() if v}); comps = Counter()
    while C:
        if any(v < 0 for v in C.values()): return None
        top = max((w for w in C if w[0] >= w[1] >= 0), key=lambda w: (w[0] + w[1], w[0]))
        comps[top] += 1
        for k, v in irr(top).items():
            C[k] -= v
            if C[k] == 0: del C[k]
    return comps
DEPTH = 5
SYM = [sym(L) for L in range(DEPTH + 1)]
HARM = [SYM[L] - (SYM[L-2] if L >= 2 else Counter()) for L in range(DEPTH + 1)]
def run(module_K, T0):
    T = {w: Counter(c) for w, c in T0.items()}; found = []
    for w in sorted(T):
        comps = peel_so5(T[w])
        if comps is None: return found, ('NEGATIVE', w)
        for hw, m in comps.items():
            found.append((w, hw, m))
            for L in range(DEPTH + 1):
                if w + L in T:
                    T[w + L].subtract(mul(irr(hw), module_K[L]) if m == 1 else Counter({k: m*v for k, v in mul(irr(hw), module_K[L]).items()}))
    return found, None
lam = Fr(5, 2)
T0 = {}
for L1 in range(DEPTH + 1):
    for L2 in range(DEPTH + 1 - L1):
        w = 2*lam + L1 + L2
        T0.setdefault(w, Counter()).update(mul(SYM[L1], SYM[L2]))
found, err = run(SYM, T0)
print("   H_5/2 ⊗ H_5/2 summands (lowest weight w, lowest K-type SO(5) h.w., multiplicity):")
for f in found: print(f"      w = {f[0]}  τ = ({f[1][0]},{f[1][1]})  dim {weyl_dim(f[1])}  mult {f[2]}")
check("self-consistency: no negative multiplicity to depth 5 with τ⊗Sym(C^5) module characters (the assumption survives)", err is None, str(err))
check("all lowest weights integer, in 5 + Z≥0 (two singletons fuse into the even-clock coset)",
      all(f[0].denominator == 1 and f[0] >= 5 for f in found))
lvl = lambda w: sorted((f[1], f[2]) for f in found if f[0] == w)
check("level 5: exactly one scalar module; level 6: exactly one vector (1,0) module", lvl(5) == [((0, 0), 1)] and lvl(6) == [((1, 0), 1)], f"{lvl(5)} | {lvl(6)}")
mf = all(f[2] == 1 for f in found)
check("multiplicity-free to depth 5 (every summand appears once)", mf)
# negative controls
bad = [Counter(x) for x in SYM]; bad[1] = Counter({k: 2*v for k, v in SYM[1].items()})
_, err_bad = run(bad, T0)
check("NEGATIVE CONTROL (wrong multiplicity: Sym^1 doubled in the module character) is DETECTED (negative multiplicity)", err_bad is not None, str(err_bad))
found_rac, err_rac = run(HARM, T0)
print(f"   Rac-type module characters (harmonic K-types only): error = {err_rac}; summands found = {len(found_rac)} vs {len(found)}")
check("NEGATIVE CONTROL (prereg: Rac-type module characters must produce a negative multiplicity)", err_rac is not None, str(err_rac))
print(f"\nSCORE: {sum(score)}/{len(score)}")
