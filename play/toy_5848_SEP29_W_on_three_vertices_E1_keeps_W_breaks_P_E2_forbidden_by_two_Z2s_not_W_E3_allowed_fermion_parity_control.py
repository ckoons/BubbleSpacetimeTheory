#!/usr/bin/env python3
"""
Toy 5848 — round 22 (C): W on three vertices, with a fermion-parity control (Elie, 2026-09-29). Prereg c889deda.
Groups/sources: 5D singletons of SO(5,2) restricted to SO(4)xSO(2) (H², Rac₅, Di₅ — 5846's characters); 4D ladders φ (Δ=1), ψ (Δ=3/2) (5834).
A vertex is ALLOWED iff its full tensor-product character is (z_t, z_s) = (+1, +1) on every weight (both Z2s neutral; Cal S1019).
"""
import glob, io, contextlib
from fractions import Fraction as F
from collections import Counter
from itertools import product
src = open(glob.glob('play/toy_5846_*.py')[0]).read(); ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("res = {}")], ns)
H2, RAC, DI = ns['H2'], ns['RAC'], ns['DI']
src4 = open(glob.glob('play/toy_5834_*.py')[0]).read(); ns4 = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src4[:src4.index("LAD = {}")], ns4)
PHI = ns4['ladder'](0, 1, 5); PSI = ns4['ladder'](1, 1, 5)
PHI = {F(w): c for w, c in PHI.items()}; PSI = {F(w): c for w, c in PSI.items()}
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def tensor(*Gs, depth=2):
    T = {F(0): Counter({(0, 0): 1})}
    for G in Gs:
        new = {}
        for w1, C1 in T.items():
            for w2 in sorted(G)[:depth + 1]:
                C = new.setdefault(w1 + w2, Counter())
                for (a, b), u in C1.items():
                    for (c, d), v in G[w2].items(): C[(a + c, b + d)] += u*v
        T = new
    return T
def signs(G):
    out = set()
    for w, C in G.items():
        zt = 1 if (2*w) % 2 == 0 else -1
        for (x, y), v in C.items():
            if v: out.add((zt, 1 if (x + y) % 2 == 0 else -1))
    return out
cls = {n: signs(G) for n, G in (("H²", H2), ("Rac", RAC), ("Di", DI), ("φ", PHI), ("ψ", PSI))}
print("   field classes (z_t, z_s):", {k: sorted(v) for k, v in cls.items()})
Wf = {k: next(iter(v))[0]*next(iter(v))[1] for k, v in cls.items()}
Pf = {"H²": -1, "Rac": 1, "Di": 1, "φ": 1, "ψ": 1}
Ff = {k: next(iter(v))[1] for k, v in cls.items()}           # fermion parity = z_s
def vertex(names):
    s = signs(tensor(*[{"H²": H2, "Rac": RAC, "Di": DI, "φ": PHI, "ψ": PSI}[n] for n in names]))
    W = 1; P = 1; Fp = 1
    for n in names: W *= Wf[n]; P *= Pf[n]; Fp *= Ff[n]
    return s, W, P, Fp
for name, vs in (("E1 H²·Rac·φ", ["H²", "Rac", "φ"]), ("E2 H²·Di", ["H²", "Di"]), ("E3 H²·Di·ψ", ["H²", "Di", "ψ"]), ("control Di·φ·φ", ["Di", "φ", "φ"])):
    s, W, P, Fp = vertex(vs)
    print(f"   {name:16s}: tensor-product signs {sorted(s)}  W = {W:+d}  P = {P:+d}  (−1)^F = {Fp:+d}  → {'ALLOWED' if s == {(1, 1)} else 'FORBIDDEN'}")
    if name.startswith("E1"): e1 = (s, W, P)
    if name.startswith("E2"): e2 = (s, W, P, Fp)
    if name.startswith("E3"): e3 = (s, W, Fp)
    if name.startswith("control"): ctl = (s, Fp)
check("E1 H²·Rac·φ is ALLOWED (both Z2s neutral), keeps W (+1) and BREAKS P (−1): the label is W, not H²-number", e1[0] == {(1, 1)} and e1[1] == 1 and e1[2] == -1)
check("E2 H²·Di is FORBIDDEN (clock and fermion parity both violated)", e2[0] == {(-1, -1)})
check("E2 NUANCE (prereg, stated in advance): W(H²·Di) = +1 — W ALONE would allow it; the two Z2s (Cal's refinement) forbid it: W is necessary, not sufficient",
      e2[1] == 1)
check("E3 H²·Di·ψ is ALLOWED, W = +1, fermion number even", e3[0] == {(1, 1)} and e3[1] == 1 and e3[2] == 1)
check("CONTROL fermion parity: every allowed vertex has (−1)^F = +1, and a single-fermion vertex Di·φ·φ is FORBIDDEN", ctl[0] != {(1, 1)} and ctl[1] == -1)
print("\nREADING: the full action constraint is the PAIR of Z2s (clock character, fermion parity); W is their product. E1 separates W from P;")
print("E2 shows W alone is not the whole constraint (it is W-even yet forbidden); E3 allowed; fermion parity conserved throughout.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
