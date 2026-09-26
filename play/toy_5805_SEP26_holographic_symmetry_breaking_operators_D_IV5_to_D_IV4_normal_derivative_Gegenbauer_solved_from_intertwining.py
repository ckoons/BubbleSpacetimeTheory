#!/usr/bin/env python3
"""
Toy 5805 — symmetry-breaking (holographic) operators H_λ(D_IV^5) -> H_{λ+k}(D_IV^4) (Elie, 2026-09-26, round 6 item 2).
Prereg 20bca7b4. Model: holomorphic polynomials on the tube over the future cone of R^{1,4} (Šilov = compactified R^{1,4}).
so(2,5) with parameter λ:  P_μ = ∂_μ,  M_μν = z_μ∂_ν - z_ν∂_μ,  D = z·∂ + λ,  K^μ = Q(z) ∂^μ - 2 z^μ (z·∂) - 2λ z^μ.
Subgroup SO(2,4) = the part preserving z4 = 0 (μ = 0..3). Ansatz D_k f = [Σ_j a_j (Δ')^j ∂_4^{k-2j} f]_{z4=0}.
The a_j are SOLVED from intertwining with the tangential K^μ (not assumed), then compared to inflated Gegenbauer
coefficients to read off μ_G. Exact (sympy).
"""
import sympy as sp
from itertools import combinations_with_replacement as cwr
from math import factorial
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
Z = sp.symbols('z0:5'); eta = [-1, 1, 1, 1, 1]
lam = sp.Symbol('lam')
def Q(vs): return sum(eta[i]*v**2 for i, v in enumerate(vs))
def euler(f, vs): return sum(v*sp.diff(f, v) for v in vs)
def P(mu, f, vs, L): return sp.diff(f, vs[mu])
def Dg(f, vs, L): return euler(f, vs) + L*f
def Mg(m, n, f, vs, L): return eta[m]*vs[m]*sp.diff(f, vs[n]) - eta[n]*vs[n]*sp.diff(f, vs[m])
def Kg(mu, f, vs, L):
    return sp.expand(Q(vs)*eta[mu]*sp.diff(f, vs[mu]) - 2*vs[mu]*euler(f, vs) - 2*L*vs[mu]*f)
def monos(vs, deg):
    out = [sp.Integer(1)]
    for d in range(1, deg+1):
        out += [sp.Mul(*c) for c in cwr(vs, d)]
    return out
# ---- self-check of the representation (5 variables) ----
test = monos(Z, 3)
ok = True
for mu in range(5):
    for nu in range(5):
        for f in test[::7]:
            kk = sp.expand(Kg(mu, Kg(nu, f, Z, lam), Z, lam) - Kg(nu, Kg(mu, f, Z, lam), Z, lam))
            if kk != 0: ok = False
check("model self-check: [K^μ, K^ν] = 0 on polynomials (deg ≤ 3)", ok)
ok = True
for mu in range(5):
    for nu in range(5):
        for f in test[::5]:
            c = sp.expand(Kg(mu, P(nu, f, Z, lam), Z, lam) - P(nu, Kg(mu, f, Z, lam), Z, lam))
            target = 2*Dg(f, Z, lam) if mu == nu else 2*Mg(mu, nu, f, Z, lam)
            target = sp.expand(target if mu != nu else target)
            if not (sp.expand(c - target) == 0 or sp.expand(c + target) == 0): ok = False
check("model self-check: [K^μ, P_ν] = ±2(δ D + M) (closes on D and M)", ok)
# ---- the operator ----
Zp = Z[:4]
def lap_p(f): return sum(eta[i]*sp.diff(f, Z[i], 2) for i in range(4))
def Dk(f, a, k):
    g = 0
    for j, aj in enumerate(a):
        h = sp.diff(f, Z[4], k-2*j) if k-2*j > 0 else f
        for _ in range(j): h = lap_p(h)
        g += aj*h
    return sp.expand(g.subs(Z[4], 0))
def solve_k(k, L):
    J = k//2
    a = [sp.Integer(1)] + list(sp.symbols(f'a1:{J+1}'))
    eqs = []
    for f in monos(Z, k+3):
        for mu in range(4):
            lhs = Dk(Kg(mu, f, Z, L), a, k)
            rhs = Kg(mu, Dk(f, a, k), Zp, L + k)
            d = sp.expand(lhs - rhs)
            if d != 0:
                eqs += sp.Poly(d, *Zp).coeffs()
    if J == 0:
        return a, all(sp.simplify(e) == 0 for e in eqs)
    sol = sp.solve(eqs, a[1:], dict=True)
    return sol, bool(sol)
def gegen_coeffs(k, m, s):
    """inflated Gegenbauer: coefficient of (∂4)^{k-2j} (s·Δ')^j normalised to j = 0"""
    c = [(-1)**j * sp.gamma(k-j+m)/(sp.factorial(j)*sp.factorial(k-2*j)) * 2**(k-2*j) for j in range(k//2+1)]
    return [sp.simplify(x*s**j/c[0]) for j, x in enumerate(c)]
L = sp.Rational(5, 2)
results = {}
for k in range(5):
    sol, ok = solve_k(k, L)
    if k < 2:
        check(f"k={k}: D_k = restriction∘∂_4^{k} intertwines H_5/2(D^5) -> H_{L+k}(D^4) (no free coefficient)", ok)
        results[k] = [1]
    else:
        ok1 = ok and len(sol) == 1 and all(v.is_number for v in sol[0].values())
        a = [sp.Integer(1)] + [sol[0][s] for s in sorted(sol[0], key=str)] if ok else None
        results[k] = a
        check(f"k={k}: unique intertwining solution{' (extra, not required)' if k > 2 else ''}", ok1, f"a = {a}")
# read μ_G from a_1 at k = 2..4 for both signs of the y-variable
mu = sp.Symbol('mu')
for s in (1, -1):
    ms = []
    for k in range(2, 5):
        if results.get(k):
            ms += sp.solve(sp.Eq(gegen_coeffs(k, mu, s)[1], results[k][1]), mu)
    print(f"   sign s = {s:+d}: μ_G from a_1 at k = 2,3,4 -> {ms}")
    if ms and all(m == ms[0] for m in ms):
        muG, sG = ms[0], s
print(f"   => μ_G = {muG} with y = {sG:+d}·Δ'  (prereg candidates: λ-(n-2)/2 = 1, λ-1 = 3/2)")
check("the solved operators are inflated Gegenbauer C_k^{μ_G} with ONE μ_G for all k = 2..4 (k = 4 checks the j = 2 term too)",
      all(results[k] == gegen_coeffs(k, muG, sG) for k in range(2, 5)))
check("μ_G equals one of the two prereg candidates", muG in (1, sp.Rational(3, 2)), f"μ_G = {muG}")
# control: wrong μ fails intertwining at k = 2
def intertwines(a, k, L):
    for f in monos(Z, k+3):
        for m_ in range(4):
            if sp.expand(Dk(Kg(m_, f, Z, L), a, k) - Kg(m_, Dk(f, a, k), Zp, L+k)) != 0: return False
    return True
bad = [intertwines(gegen_coeffs(2, muG + d, sG), 2, L) for d in (sp.Rational(1, 2), -sp.Rational(1, 2))]
check("CONTROL: μ_G ± 1/2 FAILS intertwining at k = 2", not any(bad))
# general λ: μ_G as a function of λ (k = 2)
Ls = sp.Symbol('L')
solL, _ = solve_k(2, Ls)
a1L = list(solL[0].values())[0]
muL = sp.solve(sp.Eq(gegen_coeffs(2, mu, sG)[1], a1L), mu)
print(f"   general λ: a_1(k=2) = {sp.simplify(a1L)}  ->  μ_G(λ) = {muG_L if (muG_L:=muL) else None}")
check("μ_G(λ) = λ - 1 = λ - (n-3)/2 for n = 5 (reported as computed)", len(muL) == 1 and sp.simplify(muL[0] - (Ls - 1)) == 0, f"{muL}")
print(f"\nSCORE: {sum(score)}/{len(score)}")
