#!/usr/bin/env python3
"""Toy 5724 — family in n of the Lie-ball push cost; c(1,1)(n) hashed at n=8,9,10; other words fit-then-verify."""
import sys, os, time, json, itertools
from fractions import Fraction as F
import sympy as sp
sys.argv = [sys.argv[0]]
HERE = os.path.dirname(os.path.abspath(__file__))
src = open([f for f in os.listdir(HERE) if f.startswith('toy_5722_')][0] if False else os.path.join(HERE, [f for f in os.listdir(HERE) if f.startswith('toy_5722_')][0])).read()
exec(src.split('t0 = time.time()')[0])   # reuse the exact Gram machinery (gram, cost, harmonic_part, ...)
score = []; canfail = []
t0 = time.time()
print("F1: c(1,1)(n) at n = 8, 9, 10 (hashed: 13/30, 63/143, 25/56)")
pred = {8: F(13, 30), 9: F(63, 143), 10: F(25, 56)}; got = {}
for n in (8, 9, 10):
    got[n] = cost(n, 1, 1); print(f"  n={n}: {got[n]} = {float(got[n]):.5f}   hashed {pred[n]}   [{time.time()-t0:.0f}s]")
sc("F1", all(got[n] == pred[n] for n in pred), True, "n(n+5)/(2(n+2)(n+4)) at n = 8, 9, 10")
print("F2: other words — fit on n = 3..7, verify at n = 8, 9")
nn = sp.symbols('n'); ok2 = True; forms = {}
for (j, k) in [(0, 1), (0, 2), (0, 3), (1, 0)]:
    vals = {n: cost(n, j, k) for n in range(3, 10)}
    # fit c(n) = (a n^2 + b n + c)/(n^2 + d n + e) on n=3..7 (5 eqs, 5 unknowns), then test 8, 9
    a, b, c, d, e = sp.symbols('a b c d e')
    eqs = [sp.Eq((a*n**2 + b*n + c), vals[n].numerator/sp.Integer(vals[n].denominator) * (n**2 + d*n + e)) for n in range(3, 8)]
    sol = sp.solve(eqs, [a, b, c, d, e], dict=True)
    if not sol: print(f"  ({j},{k}): no degree-2/2 fit"); ok2 = False; continue
    s = {sym: sol[0].get(sym, 0) for sym in (a, b, c, d, e)}; form = sp.factor(sp.cancel((s[a]*nn**2 + s[b]*nn + s[c]) / (nn**2 + s[d]*nn + s[e]))); form = sp.factor(sp.cancel(form.subs({sym: 0 for sym in form.free_symbols - {nn}}))); forms[(j, k)] = str(form)
    chk = all(sp.Rational(vals[n].numerator, vals[n].denominator) == form.subs(nn, n) for n in (8, 9))
    ok2 &= chk
    print(f"  ({j},{k}): values n=3..9 {[str(vals[n]) for n in range(3,10)]}; fit {form}; verify n=8,9: {chk}   [{time.time()-t0:.0f}s]")
sc("F2", ok2, True, "each fitted form holds at n = 8, 9")
print("F3: constant word at n = 8, 9, 10")
c0 = {n: cost(n, 0, 0) for n in (8, 9, 10)}; print("  ", {n: str(v) for n, v in c0.items()})
sc("F3", all(v == F(1, 2) for v in c0.values()), False, "1/2")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,canfail) if c)}/{sum(canfail)} can-fail hit")
json.dump({'c11': {n: str(v) for n, v in got.items()}, 'forms': {f'{j},{k}': v for (j, k), v in forms.items()}}, open(os.path.join(HERE, '.record_5724.json'), 'w'), indent=1)
