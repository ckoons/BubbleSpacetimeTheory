#!/usr/bin/env python3
"""Toy 5723 — matter/light split of a coordinate write on S^{d-1}, exact, d = 2..7, k = 1..3."""
import sympy as sp, itertools, math, json, os
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__)); score = []; canfail = []
def sc(n, ok, cf, d=""): score.append(ok); canfail.append(cf); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if cf else ' (control)'}  {d}")
def sphere_moment(alpha):
    """∫_{S^{d-1}} x^alpha dσ / ∫ 1 dσ, exact rational (zero if any odd exponent)."""
    if any(a % 2 for a in alpha): return F(0)
    d = len(alpha); bs = [F(a + 1, 2) for a in alpha]
    # = Γ(d/2) ∏Γ(b_i) / (Γ(1/2)^d Γ(Σb_i)); ratio of half-integer gammas is rational up to π-powers that cancel
    num = sp.gamma(sp.Rational(d, 2)) * sp.prod([sp.gamma(sp.Rational(b.numerator, b.denominator)) for b in bs])
    den = sp.gamma(sp.Rational(1, 2))**d * sp.gamma(sp.Rational(sum(bs).numerator, sum(bs).denominator))
    r = sp.nsimplify(sp.simplify(num / den)); return F(int(r.p), int(r.q))
def sph_ip(p, q, xs):
    P = sp.Poly(sp.expand(p * q), *xs); return sum(F(int(c.p), int(c.q)) * sphere_moment(tuple(int(e) for e in mon)) for mon, c in zip(P.monoms(), P.coeffs()))
def harmonic_part(poly, k, xs):
    r2 = sum(v**2 for v in xs)
    if k < 2: return sp.expand(poly)
    d = len(xs); mons = [sp.Mul(*[v**e for v, e in zip(xs, ex)]) for ex in itertools.product(range(k - 1), repeat=d) if sum(ex) == k - 2]
    cs = sp.symbols(f'c0:{len(mons)}'); q = sum(c * mm for c, mm in zip(cs, mons))
    lap = lambda f: sum(sp.diff(f, v, 2) for v in xs)
    sol = sp.solve(sp.Poly(sp.expand(lap(poly - r2 * q)), *xs).coeffs(), cs, dict=True)[0]
    return sp.expand(poly - r2 * q.subs(sol))
def matter_fraction(d, k, Y, xs):
    r2 = sum(v**2 for v in xs); tot_w = F(0); tot = F(0)
    for i in range(d):
        w = sp.expand(r2 * sp.diff(Y, xs[i]) / (2 * k + d - 2)); h = sp.expand(xs[i] * Y - w)
        # sanity: h harmonic
        assert sp.expand(sum(sp.diff(h, v, 2) for v in xs)) == 0
        tot_w += sph_ip(w, w, xs); tot += sph_ip(xs[i] * Y, xs[i] * Y, xs)
    return tot_w / tot
import random; random.seed(5723)
res = {}; ok1 = ok2 = True
for d in range(3, 8):
    xs = sp.symbols(f'x0:{d}')
    for k in range(1, 4):
        Y = harmonic_part(xs[0]**k, k, xs)
        mons = [sp.Mul(*[v**e for v, e in zip(xs, ex)]) for ex in itertools.product(range(k + 1), repeat=d) if sum(ex) == k]
        Yr = harmonic_part(sum(random.randint(-3, 3) * mm for mm in mons) + xs[1]**k, k, xs)
        mf = matter_fraction(d, k, Y, xs); mfr = matter_fraction(d, k, Yr, xs); pred = F(k, 2 * k + d - 2)
        res[(d, k)] = (mf, mfr); ok1 &= (mf == pred and mfr == pred); ok2 &= (1 - mf == F(k + d - 2, 2 * k + d - 2))
        print(f"  d={d} k={k}: matter {mf} (random harmonic {mfr})  predicted k/(2k+d-2) = {pred}   light {1-mf}")
sc("S1", ok1, True, "matter = k/(2k+d-2) exactly, both representatives, d=3..7, k=1..3")
sc("S2", ok2, True, "light = (k+d-2)/(2k+d-2) exactly")
xs = sp.symbols('x0:2'); c2 = [matter_fraction(2, k, harmonic_part(xs[0]**k, k, xs), xs) for k in range(1, 4)]
print("  d=2:", [str(c) for c in c2]); sc("S3", all(c == F(1, 2) for c in c2), False, "circle gives 1/2 for every k")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,canfail) if c)}/{sum(canfail)} can-fail hit")
json.dump({f"{d},{k}": (str(a), str(b)) for (d, k), (a, b) in res.items()}, open(os.path.join(HERE, '.record_5723.json'), 'w'), indent=1)
