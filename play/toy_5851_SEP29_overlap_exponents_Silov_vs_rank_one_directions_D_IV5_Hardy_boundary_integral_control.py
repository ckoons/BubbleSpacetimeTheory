#!/usr/bin/env python3
"""
Toy 5851 — overlap exponents along the Šilov and rank-one directions of D_IV^5 (Elie, 2026-09-29, round 23). Prereg 04625f5c.
Family: scalar holomorphic module at weight ν, kernel h(z,w)^{−ν} (FK; at ν = 5/2 CHECKED here by the boundary integral).
A_ν(z) = |K(z,0)|/sqrt(K(z,z)K(0,0)) = h(z,z)^{ν/2}. Šilov direction z = t·x (x real unit); rank-one z = t·c, c = (e1+ie2)/2.
"""
import sympy as sp, numpy as np
from scipy import integrate
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
t, nu = sp.symbols('t nu', positive=True)
def h(z, w):   # z holomorphic, w given as the CONJUGATE vector w̄
    return 1 - 2*sum(a*b for a, b in zip(z, w)) + sum(a*a for a in z)*sum(b*b for b in w)
x = [1, 0, 0, 0, 0]; zS = [t*v for v in x]
c = [sp.Rational(1, 2), sp.I/2, 0, 0, 0]; zR = [t*v for v in c]
hS = sp.factor(sp.expand(h(zS, [sp.conjugate(v) for v in zS])))
hR = sp.factor(sp.expand(h(zR, [sp.conjugate(v) for v in zR])))
print(f"   h(z,z): Šilov {hS};  rank-one {hR}")
check("(1) Šilov direction: h = (1 − t²)² ⇒ A_ν = (1 − t²)^ν exactly (general ν)", sp.simplify(hS - (1 - t**2)**2) == 0)
check("(1) rank-one direction: h = 1 − t² ⇒ A_ν = (1 − t²)^{ν/2} exactly (general ν)", sp.simplify(hR - (1 - t**2)) == 0)
check("(1) primitive idempotent: |c|² = 1/2, c·c = 0 (rank-one), x·x = 1 (Šilov)",
      sum(abs(complex(v))**2 for v in c) == 0.5 and sum(v*v for v in c) == 0)
# (2) CONTROL at the Hardy point: ∫_{Šilov} |S(ζ,z)|² dσ(ζ) = S(z,z) = h(z,z)^{−5/2}; ζ = e^{iθ} x, x ∈ S⁴, θ uniform
def hardy_norm_silov(tv):
    # h(ζ, z̄) = 1 − 2 e^{iθ} t x1 + e^{2iθ} t² ; x1 marginal on S⁴: (3/4)(1 − u²)
    f = lambda th, u: 0.75*(1 - u*u)*abs(1 - 2*np.exp(1j*th)*tv*u + np.exp(2j*th)*tv**2)**(-5)/(2*np.pi)
    return integrate.dblquad(f, -1, 1, 0, 2*np.pi, epsabs=1e-12, epsrel=1e-11)[0]
def hardy_norm_rank1(tv):
    # h(ζ, z̄) = 1 − t e^{iθ}(x1 − i x2) = 1 − t r e^{iψ}; (x1,x2) marginal on S⁴: (3/2π)(1 − r²)^{1/2} ⇒ radial 3 r (1 − r²)^{1/2}
    f = lambda ps, r: 3*r*np.sqrt(1 - r*r)*abs(1 - tv*r*np.exp(1j*ps))**(-5)/(2*np.pi)
    return integrate.dblquad(f, 0, 1, 0, 2*np.pi, epsabs=1e-12, epsrel=1e-11)[0]
okS = okR = True; rows = []
for tv in (0.2, 0.5, 0.7):
    nS, nR = hardy_norm_silov(tv), hardy_norm_rank1(tv)
    eS, eR = (1 - tv**2)**(-5), (1 - tv**2)**(-2.5)
    rows.append((tv, round(nS/eS, 10), round(nR/eR, 10)))
    okS &= abs(nS/eS - 1) < 1e-8; okR &= abs(nR/eR - 1) < 1e-8
print("   Hardy boundary integral / h(z,z)^{-5/2}  (t, Šilov, rank-one):", rows)
check("(2) CONTROL Hardy point: the Šilov-boundary L² norm of S(·,z) reproduces h(z,z)^{−5/2} along the Šilov direction", okS)
check("(2) CONTROL Hardy point: … and along the rank-one direction (the kernel and both direction definitions are right)", okR)
nm = integrate.dblquad(lambda th, u: 0.75*(1 - u*u)/(2*np.pi), -1, 1, 0, 2*np.pi)[0]
check("(2) the boundary measure is normalised (S(z,0) = 1, ‖1‖ = 1)", abs(nm - 1) < 1e-12)
# so at the Hardy point: A = (1 − t²)^{5/2} (Šilov) vs (1 − t²)^{5/4} (rank-one)
E = sp.Rational(7, 2)
check("(3) inversion: an observed exponent E = 7/2 means ν = 7/2 on a Šilov direction, ν = 7 on a rank-one direction",
      sp.solve(sp.Eq(nu, E), nu) == [E] and sp.solve(sp.Eq(nu/2, E), nu) == [7])
print("\nREADING: Lyra's two exponents are exact: A_ν = (1−t²)^ν along a Šilov direction and (1−t²)^{ν/2} along a rank-one direction; the")
print("Hardy control (a genuine boundary integral) confirms the kernel and both directions. Which direction the condensate occupies is Lyra's.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
