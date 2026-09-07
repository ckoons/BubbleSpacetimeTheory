#!/usr/bin/env python3
"""Toy 5710 — E11. Exact rational functions in y = p^{-lambda} via Fractions; prereg hashed before this run."""
from fractions import Fraction as F
import itertools, json, os, sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
def prim_fracs(q, p, kmax):
    """P_i for i = 0..kmax: fraction of primitive u in (Z/p^kmax)^3 with p^i | q(u)."""
    M = p ** kmax; tot = 0; cnt = [0] * (kmax + 1)
    for u in itertools.product(range(M), repeat=3):
        if all(x % p == 0 for x in u): continue
        tot += 1; v = q(*u) % M
        i = 0
        while i < kmax and v % (p ** (i + 1)) == 0: i += 1
        for t in range(i + 1): cnt[t] += 1
    return [F(c, tot) for c in cnt]
y = sp.symbols('y')     # y = p^{-lambda}
def c_local(q, p, kmax, isotropic):
    P = prim_fracs(q, p, kmax)
    # weights: for primitive u with v(q(u)) = i exactly: P_i - P_{i+1}; height p^{max(j, 2j-i)}; integrand height^{-(lambda+3/2)} = (y * p^{-3/2})^{max(j,2j-i)}
    # we work with Y := y * p^(-3/2) symbolically: height^{-(lambda+3/2)} = Y^{m}; shell measure p^{3j}(1-p^-3)
    Y = y * sp.Rational(1, 1) * sp.Integer(p) ** sp.Rational(-3, 2)
    total = sp.Integer(1)
    if not isotropic:
        assert P[-1] == 0, "anisotropic kernel expected to have a vanishing tail"
        # finite i; sum over j >= 1 in closed form: sum_j p^{3j} (1-p^-3) * sum_i w_i * Y^{max(j, 2j-i)}
        for i in range(kmax):
            w = P[i] - P[i + 1]
            if w == 0: continue
            # for j >= i: exponent 2j - i; for 1 <= j < i: exponent j (only if i > j)
            expr = sp.Integer(0)
            for j in range(1, i):            # j < i: height p^j
                expr += sp.Integer(p) ** (3 * j) * (1 - sp.Integer(p) ** -3) * Y ** j
            # j >= max(1,i): sum_{j>=j0} p^{3j} Y^{2j-i} = Y^{-i} sum (p^3 Y^2)^j
            j0 = max(1, i); r = sp.Integer(p) ** 3 * Y ** 2
            expr += (1 - sp.Integer(p) ** -3) * Y ** (-i) * r ** j0 / (1 - r)
            total += sp.Rational(w.numerator, w.denominator) * expr
    else:
        # isotropic: P_{i+1} = P_i / p for i >= 1 (checked below); weights w_i = P_i - P_{i+1} = P_1 p^{-(i-1)} (1 - 1/p) for i>=1; w_0 = 1 - P_1
        ratio_ok = all(P[i + 1] * p == P[i] for i in range(1, kmax - 1))
        assert ratio_ok, f"Hensel ratio failed: {P}"
        P1 = sp.Rational(P[1].numerator, P[1].denominator)
        w0 = 1 - P1
        r = sp.Integer(p) ** 3 * Y ** 2
        total += w0 * (1 - sp.Integer(p) ** -3) * r / (1 - r)            # i = 0: heights p^{2j}
        # i >= 1: w_i = P1 (1-1/p) p^{-(i-1)}; sum over j>=1, i>=1 of p^{3j}(1-p^-3) w_i Y^{max(j,2j-i)}
        # split: j >= i -> Y^{2j-i}; j < i -> Y^j. Sum in closed form with a symbolic geometric sum over i.
        # closed forms (by hand): w_i = P1 (1-1/p) p^{1-i} for i >= 1
        r = sp.Integer(p) ** 3 * Y ** 2; s_ = sp.Integer(p) ** 2 * Y
        A = P1 * (1 - sp.Integer(p) ** -1) * (1 - sp.Integer(p) ** -3) * sp.Integer(p) / (sp.Integer(p) * Y - 1) * (r / (1 - r) - s_ / (1 - s_))
        B = P1 * (1 - sp.Integer(p) ** -3) * s_ / (1 - s_)
        total += A + B
    return sp.simplify(sp.factor(sp.simplify(total))), P
def gk_split(p):
    return sp.factor((1 - y ** 2 / p) * (1 - y * sp.Integer(p) ** sp.Rational(-3, 2)) / ((1 - y ** 2) * (1 - y * sp.Integer(p) ** sp.Rational(1, 2))))
def same(a, b):
    return all(abs(float((a - b).subs(y, sp.Rational(v, 100)))) < 1e-12 for v in (13, 37, 71))

import json
print("E13 — toy 5717 (prereg hashed before this run)")
K5 = lambda x, y, z: 2*x*x + 2*y*y + 2*z*z - x*y - y*z - z*x
K3 = lambda a, b, d: b*b + b*d + d*d + 3*a*a
L133 = lambda x, y, z: x*x + 3*y*y + 3*z*z
L113 = lambda x, y, z: x*x + y*y + 3*z*z
def analyse(name, q, p, kmax):
    c, P = c_local(q, p, kmax, False)
    R = sp.factor(sp.simplify(c / gk_split(p)))
    num, den = sp.fraction(sp.together(R))
    rd = {complex(k): v for k, v in sp.roots(sp.Poly(sp.expand(den), y)).items()}
    rn = {complex(k): v for k, v in sp.roots(sp.Poly(sp.expand(num), y)).items()}
    def near(z, S): return any(abs(z - w) < 1e-9 for w in S)
    pairs = [r for r in rd if near(-r, rd) and not near(r, rn) and not near(-r, rn)]
    singles = [r for r in rd if not near(-r, rd) and not near(r, rn)]
    spacing = "pi/ln p (all k)" if pairs and not singles else ("2pi/ln p (even k)" if singles and not pairs else "mixed")
    print(f"  {name} at p={p}: P_i = {[str(v) for v in P]};  R = {R};  denominator roots {sorted(rd, key=abs)};  comb: {spacing}")
    return P, R, spacing
res = {}
res['K5@5'] = analyse("K5 = 2x^2+2y^2+2z^2-xy-yz-zx", K5, 5, 3)
res['K3@3'] = analyse("K3 = b^2+bd+d^2+3a^2", K3, 3, 4)
res['133@3'] = analyse("<1,3,3>", L133, 3, 4)
res['113@3'] = analyse("<1,1,3> (rank-2 control)", L113, 3, 4)
score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
sc("P1", str(res['K5@5'][0][1]) == '6/31' and res['K5@5'][0][2] == 0 and str(res['K3@3'][0][1]) == '4/13' and res['K3@3'][0][2] == 0 and str(res['133@3'][0][1]) == '4/13' and str(res['113@3'][0][1]) == '1/13', f"P1: K5 {res['K5@5'][0][1]}, K3 {res['K3@3'][0][1]}, <1,3,3> {res['133@3'][0][1]}, <1,1,3> {res['113@3'][0][1]}")
pred5 = sp.factor((1 - 5 * y**2) / (1 - y**2 / 5)); pred3 = sp.factor((1 - 3 * y**2) / (1 - y**2 / 3))
sc("P2", sp.simplify(res['K5@5'][1] - pred5) == 0 and sp.simplify(res['K3@3'][1] - pred3) == 0, f"K5@5 comb {res['K5@5'][2]}; K3@3 comb {res['K3@3'][2]}; predicted (1 - p^(1-2l))/(1 - p^(-1-2l))")
sc("P3", sp.simplify(res['113@3'][1] - sp.factor((1 - sp.sqrt(3) * y) / (1 - y / sp.sqrt(3)))) == 0 and res['113@3'][2].startswith('2pi'), "<1,1,3> reproduces 5710: Steinberg factor, 2pi/ln 3 — the dichotomy on one instrument")
L = sp.Symbol('L', real=True)
lim = [sp.limit(r[1].subs(y, sp.exp(-L * sp.log(p))), L, sp.oo) for r, p in ((res['K5@5'], 5), (res['K3@3'], 3))]
sc("P4", all(l == 1 for l in lim), f"large-lambda limits {lim}")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({k: {'P': [str(x) for x in v[0]], 'R': str(v[1]), 'comb': v[2]} for k, v in res.items()}, open(os.path.join(HERE, '.kernel_5717.json'), 'w'), indent=1)
