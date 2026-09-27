#!/usr/bin/env python3
"""
Toy 5827 — route (b): restrict D_IV^5's Szegő kernel to the sub-Šilov (S³×S¹)/Z2 and read the 4D weight (Elie, 2026-09-27). Prereg 2fac2431.
INVARIANT: reproducing kernel h(z,w)^{-λ}, h = 1 − 2 z·w̄ + (z·z)(w̄·w̄); Szegő = λ = n/2 (5/2 for D_IV^5, 2 for D_IV^4).
On the Šilov boundary z = e^{iθ}x, w = e^{iφ}y (x, y real unit vectors): h = 1 − 2 t q + q², t = x·y, q = e^{i(θ−φ)} (checked), so
h^{-λ} = Σ_n C_n^λ(t) q^n (Gegenbauer generating function): clock weight λ + n; the S^{d-1} content of C_n^λ read in zonal harmonics
C_l^{(d-2)/2} (S³: C_l^1). A module whose kernel has ONLY l = n at every n is the Wallach (ladder) type; all l ≡ n (2) = Hardy/continuous.
"""
import sympy as sp, mpmath as mp
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
z = sp.symbols('z0:5'); w = sp.symbols('w0:5')     # w stands for conj(w) (antiholomorphic variable)
def h(zz, ww): return 1 - 2*sum(a*b for a, b in zip(zz, ww)) + sum(a*a for a in zz)*sum(b*b for b in ww)
h5r = h(z, w).subs({z[4]: 0, w[4]: 0}); h4 = h(z[:4], w[:4])
check("CONTROL (K1927 k = 0): h_5 restricted to z5 = w5 = 0 IS h_4, so h_5^{-5/2}|_{D_IV^4} = h_4^{-5/2} = kernel of H_{5/2}(D_IV^4)",
      sp.expand(h5r - h4) == 0)
th, ph = sp.symbols('theta phi', real=True); xs = sp.symbols('x0:4', real=True); ys = sp.symbols('y0:4', real=True)
zb = [sp.exp(sp.I*th)*x for x in xs]; wb = [sp.exp(-sp.I*ph)*y for y in ys]         # conj(w)
t = sum(a*b for a, b in zip(xs, ys)); q = sp.exp(sp.I*(th - ph))
hs = sp.expand(h(zb, wb)).subs(sum(x**2 for x in xs), 1)
hs = sp.expand(hs.subs({xs[3]**2: 1 - xs[0]**2 - xs[1]**2 - xs[2]**2, ys[3]**2: 1 - ys[0]**2 - ys[1]**2 - ys[2]**2}))
target = sp.expand((1 - 2*t*q + q**2))
check("on the sub-Šilov (unit real x, y ∈ S³): h = 1 − 2 t q + q² exactly (t = x·y, q = e^{i(θ−φ)})",
      sp.simplify(sp.expand(hs - target)) == 0)
# numeric check of the generating function at |q| < 1 (interior approach), λ = 5/2
mp.mp.dps = 30
qq, tt = mp.mpf('0.6')*mp.e**(1j*mp.mpf('0.9')), mp.mpf('0.35')
lhs = (1 - 2*tt*qq + qq**2)**mp.mpf(-2.5); rhs = mp.nsum(lambda n: mp.gegenbauer(n, 2.5, tt)*qq**n, [0, mp.inf])
check("h^{-5/2} = Σ_n C_n^{5/2}(t) q^n (checked numerically, |q| = 0.6): clock weights 5/2 + n, LOWEST 4D weight = 5/2",
      abs(lhs/rhs - 1) < 1e-25)
x = sp.Symbol('x')
def decomp(n, lam, mu):
    Cn = sp.expand(sp.gegenbauer(n, lam, x)); ls = list(range(n, -1, -2)); cs = sp.symbols(f'c0:{len(ls)}')
    sol = sp.solve(sp.Poly(sp.expand(Cn - sum(c*sp.gegenbauer(l, mu, x) for c, l in zip(cs, ls))), x).coeffs(), cs, dict=True)[0]
    return {l: sol[c] for c, l in zip(cs, ls)}
N = 10
r52 = [decomp(n, sp.Rational(5, 2), 1) for n in range(N + 1)]
check("restricted Szegő: every level n carries ALL S³ harmonics l = n, n−2, … with positive coefficients (n ≤ 10) = K′-types of "
      "H_{5/2}(D_IV^4), the k = 0 summand — Hardy-type, not ladder", all(all(v > 0 for v in d.values()) for d in r52))
r2 = [decomp(n, 2, 1) for n in range(N + 1)]
r1 = [decomp(n, 1, 1) for n in range(N + 1)]
check("CONTROL D_IV^4's own Szegő (λ = 2): all l ≡ n with positive coefficients (Hardy of D_IV^4, weights 2 + n)",
      all(all(v > 0 for v in d.values()) for d in r2))
check("CONTROL λ = 1 (the missing module): C_n^1 carries ONLY l = n (ladder: one shell per level) — recognisable, and absent above",
      all(all((v == 0) == (l != n) for l, v in d.items()) for n, d in enumerate(r1)))
print("   [restatement, not scored — run 1 scored it] KILL for route (b) supplying λ = 1 FIRES (prereg): the restricted Szegő data read 4D weight 5/2, lowest; no weight-1 piece")
# corollary: weights of any restricted h^{-λ} are λ + n ≥ λ; λ = 1 in 4D needs λ ≤ 1 in 5D: outside {0} ∪ [3/2, ∞)
wall5 = lambda lam: lam == 0 or lam >= sp.Rational(3, 2)
check("corollary: λ = 1 in 4D by restriction needs λ = 1 in 5D, which is NOT in D_IV^5's Wallach set {0} ∪ [3/2, ∞) — route (c), non-unitary",
      not wall5(sp.Integer(1)) and wall5(sp.Rational(3, 2)) and wall5(sp.Rational(5, 2)))
print(f"\nSCORE: {sum(score)}/{len(score)}")
