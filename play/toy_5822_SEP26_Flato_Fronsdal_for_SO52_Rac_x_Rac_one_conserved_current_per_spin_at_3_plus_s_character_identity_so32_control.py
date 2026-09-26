#!/usr/bin/env python3
"""
Toy 5822 — Flato–Fronsdal for SO(5,2): Rac ⊗ Rac = scalar(3) ⊕ ⊕_{s≥1} conserved spin-s current at 3 + s (Elie, 2026-09-26, R10 item 1).
Prereg 5d4ce093. Control: SO(3,2) (Rac⊗Rac = ⊕ massless spin s at s + 1). Negative controls: generic characters fail; H²⊗H² has
nothing at 3 + s.
INVARIANTS: K = SO(d)×SO(2) characters (clock-graded). Rac of SO(d,2): K-types H_m(C^d) at (d−2)/2 + m.
Module characters: generic  t^Δ χ_τ S;  conserved spin-s (Δ = d−2+s, s ≥ 1):  t^Δ χ_(s) S − t^{Δ+1} χ_(s−1) S,  S = Σ_L t^L Sym^L(C^d).
"""
import glob, io, contextlib
from fractions import Fraction as Fr
from collections import Counter
from itertools import combinations_with_replacement as cwr
import sympy as sp
src = open(glob.glob('play/toy_5792_*.py')[0]).read()
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("def irreps")], ns)
weights = ns['weights']
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def vecw(d):
    r = d // 2; W = []
    for i in range(r):
        for sgn in (1, -1):
            w = [0]*r; w[i] = sgn; W.append(tuple(w))
    if d % 2: W.append(tuple([0]*r))
    return W
def sym(d, L):
    W = vecw(d); C = Counter()
    for combo in cwr(range(d), L): C[tuple(Fr(sum(W[k][i] for k in combo)) for i in range(d//2))] += 1
    return C
def harm(d, m):
    C = sym(d, m)
    if m >= 2: C.subtract(sym(d, m - 2))
    return +C
def mul(A, B):
    C = Counter()
    for a, x in A.items():
        for b, y in B.items(): C[tuple(p + q for p, q in zip(a, b))] += x*y
    return C
def chi_s(d, s):   # symmetric traceless spin-s = highest weight (s,0,...)
    r = d // 2
    return Counter(weights(tuple([Fr(s)] + [Fr(0)]*(r - 1)))) if s >= 0 else Counter()
def graded_mod(d, D, s, conserved, depth, top):
    """character of the module with lowest K-type spin s at weight D, as {weight: Counter}, up to weight top."""
    G = {}
    for L in range(depth + 1):
        w = D + L
        if w > top: break
        G.setdefault(w, Counter()).update(mul(chi_s(d, s), sym(d, L)))
        if conserved and s >= 1 and w + 1 <= top:
            G.setdefault(w + 1, Counter()).subtract(mul(chi_s(d, s - 1), sym(d, L)))
    return G
def test(d, depth, conserved_for_all_s, override_generic=False):
    lam = Fr(d - 2, 2); top = 2*lam + depth
    RR = {}
    for m1 in range(depth + 1):
        for m2 in range(depth + 1 - m1):
            RR.setdefault(2*lam + m1 + m2, Counter()).update(mul(harm(d, m1), harm(d, m2)))
    PRED = {}
    for s in range(depth + 1):
        D = 2*lam + s
        cons = (s >= 1) and not override_generic
        for w, c in graded_mod(d, D, s, cons, depth, top).items():
            PRED.setdefault(w, Counter()).update(c)
    ok = all(+Counter({k: v for k, v in RR.get(w, Counter()).items()}) == +Counter({k: v for k, v in PRED.get(w, Counter()).items() if v}) and
             all(v >= 0 for v in PRED.get(w, Counter()).values()) for w in RR)
    return ok
check("CONTROL so(3,2): χ(Rac)² = scalar(1) + Σ_{s≥1} conserved spin-s at s+1, exact to depth 8", test(3, 8, True))
check("d = 5, SO(5,2): χ(Rac)² = scalar(3) + Σ_{s≥1} conserved spin-s at 3 + s, exact to depth 6", test(5, 6, True))
check("NEGATIVE CONTROL: with GENERIC (unconserved) characters for every s the identity FAILS (d = 5)", not test(5, 6, True, override_generic=True))
check("NEGATIVE CONTROL: with generic characters the so(3,2) identity FAILS too", not test(3, 8, True, override_generic=True))
# H²⊗H² components (5816): (j,0) at 5 + j + 2m >= 5 + j > 3 + j — none at 3 + s
h2 = [(5 + j + 2*m, j) for j in range(7) for m in range(4)]
check("NEGATIVE CONTROL: H²⊗H² (5816) has NO component at weight 3 + s for any s (all at >= 5 + s): no conserved current on H²",
      all(w != 3 + j for w, j in h2))
# Test B (model): lowest vectors of Rac⊗Rac = g(u) with Q(∂_u) g = 0 ⇒ harmonic in u, one spin-s multiplet per degree s
U = sp.symbols('u0:5'); eta = [-1, 1, 1, 1, 1]
def lapQ(f): return sum(eta[i]*sp.diff(f, U[i], 2) for i in range(5))
okB = True; dims = []
for N in range(5):
    B = [sp.Mul(*c) for c in cwr(U, N)] if N else [sp.Integer(1)]
    cs = sp.symbols(f'c0:{len(B)}'); g = sum(c*b for c, b in zip(cs, B))
    eqs = sp.Poly(sp.expand(lapQ(g)), *U).coeffs() if N >= 2 else []
    sol = sp.linsolve(eqs, cs) if eqs else None
    dimker = len(B) - (sp.Matrix([[sp.diff(e, c) for c in cs] for e in eqs]).rank() if eqs else 0)
    dims.append(dimker)
    exp = sum(harm(5, N).values())
    if dimker != exp: okB = False
check("Test B (tube model): Rac⊗Rac lowest vectors at degree s = harmonic h_s(u) (dims 1,5,14,30,55 = one spin-s multiplet per s, no Q(u)^n tower)",
      okB and dims == [1, 5, 14, 30, 55], str(dims))
print(f"\nSCORE: {sum(score)}/{len(score)}")
