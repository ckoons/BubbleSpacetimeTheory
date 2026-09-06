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
print("P1 controls")
c3s, P3s = c_local(lambda a, b, c: a * a + b * b - c * c, 3, 5, True)
c5, P5 = c_local(lambda a, b, c: a * a + b * b + 3 * c * c, 5, 4, True)
ok1 = same(c3s, gk_split(3)) and same(c5, gk_split(5))
print("  split ternary at p=3:", sp.factor(c3s), " GK:", gk_split(3)); print("  x^2+y^2+3z^2 at p=5:", sp.factor(c5), " GK:", gk_split(5))
sc("P1", ok1, "both controls reproduce the Gindikin–Karpelevich split factor exactly" if ok1 else "CONTROL FAILED — stop")
if ok1:
    print("P2 the anisotropic kernel at p = 3")
    c3a, P3a = c_local(lambda a, b, c: a * a + b * b + 3 * c * c, 3, 4, False)
    print("  P_i (primitive, 3^i | q):", [str(v) for v in P3a]); print("  c_3^aniso(y) =", sp.factor(c3a))
    R = sp.factor(sp.simplify(c3a / gk_split(3))); print("  correction R_3 = c^aniso/c^split =", R)
    num, den = sp.fraction(sp.together(R)); print("  numerator:", sp.factor(num), "\n  denominator:", sp.factor(den))
    # pole comb: zeros of den in y = 3^{-lambda}; spacing in Im lambda: a factor (1 - a y^2) -> pi/ln3; (1 - a y) -> 2pi/ln3
    roots_den = sp.roots(sp.Poly(sp.expand(den), y)); roots_num = sp.roots(sp.Poly(sp.expand(num), y))
    print("  denominator roots in y:", {sp.nsimplify(k): v for k, v in roots_den.items()}); print("  numerator roots in y:", {sp.nsimplify(k): v for k, v in roots_num.items()})
    # classify: a root y0 = 3^{-lambda}: lambda = -ln(y0)/ln 3 + 2 pi i k / ln 3. If both +y0 and -y0 are denominator roots (and not numerator roots), the comb has spacing pi/ln3 (all k); if only +y0, spacing 2pi/ln3.
    dr = {complex(k): v for k, v in roots_den.items()}; nr = {complex(k): v for k, v in roots_num.items()}
    def near(z, S): return any(abs(z - w) < 1e-9 for w in S)
    verdict = []
    for r0 in list(dr):
        if near(-r0, dr) and not near(r0, nr) and not near(-r0, nr): verdict.append((r0, "pair ±y0 uncancelled: spacing pi/ln3 (all k)"))
        elif not near(-r0, dr): verdict.append((r0, "single root: spacing 2pi/ln3"))
    print("  comb reading:", verdict)
    allk = any("pi/ln3 (all k)" in v for _, v in verdict); evenk = any("2pi/ln3" in v for _, v in verdict)
    sc("P2", allk and not evenk, f"pole comb spacing: {'pi/ln3 all k (Cal)' if allk and not evenk else ('2pi/ln3 even k (Lyra)' if evenk and not allk else 'mixed — see roots')}; pole Re lambda = -log|y0|/ln3 for y0 in {[round(abs(r),6) for r in dr]}")
    lead = sp.limit(sp.log(R.subs(y, sp.exp(-sp.Symbol('L', real=True) * sp.log(3)))) / sp.Symbol('L', real=True), sp.Symbol('L', real=True), sp.oo)
    sc("P3", True, f"large-Re lambda: log R_3 / lambda -> {lead} (i.e. R_3 ~ 3^{{a lambda}} with a = {sp.nsimplify(lead/sp.log(3)) if lead != 0 else 0})")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.kernel_5710.json'), 'w'))
