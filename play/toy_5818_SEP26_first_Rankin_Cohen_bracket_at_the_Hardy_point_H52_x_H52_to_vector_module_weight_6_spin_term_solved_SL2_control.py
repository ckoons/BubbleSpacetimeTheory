#!/usr/bin/env python3
"""
Toy 5818 — the first (k = 1) Rankin–Cohen bracket at the Hardy point (Elie, 2026-09-26, round 8 item 3). Prereg 75daf52b.
Model: 5805's tube model (holomorphic polynomials on C^5, η = diag(−1,1,1,1,1)), so(2,5) at parameter λ:
  P_μ = ∂_μ, D = z·∂ + λ, K^μ = Q(z) η^{μμ}∂_μ − 2 z^μ (z·∂) − 2λ z^μ, M_mn = η_m z_m ∂_n − η_n z_n ∂_m.
5816 fixed the target: H_5/2 ⊗ H_5/2 ⊃ the vector (1,0) module at clock weight 6 (once).
Candidate: B_a(f,g) = f ∂_a g − g ∂_a f. Target action on C^5-valued F: scalar part at Λ = 2λ+1 = 6 plus spin terms with constants
(c1, c2) for K and s for M, SOLVED by linear algebra (not assumed). Control: SL(2,R) RC_1; symmetric bracket fails for all constants.
"""
import sympy as sp
from itertools import combinations_with_replacement as cwr
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# ---- SL(2,R) control (n = 1: Q = z², K = −z²∂ − 2λz) ----
z = sp.Symbol('z'); a_, b_ = sp.symbols('a b'); l1, l2 = sp.symbols('l1 l2', positive=True)
K1 = lambda f, L: sp.expand(-z**2*sp.diff(f, z) - 2*L*z*f)
RC = lambda f, g: a_*sp.diff(f, z)*g + b_*f*sp.diff(g, z)
eqs = []
for i in range(4):
    for j in range(4):
        f, g = z**i, z**j
        eqs += sp.Poly(sp.expand(RC(K1(f, l1), g) + RC(f, K1(g, l2)) - K1(RC(f, g), l1 + l2 + 1)), z).coeffs()
sol = sp.solve(eqs, [a_], dict=True)
print("   SL(2) RC_1 solution:", sol)
check("CONTROL SL(2,R): RC_1 = λ2 f′g − λ1 fg′ (up to scale) intertwines D_λ1⊗D_λ2 → D_{λ1+λ2+1}",
      len(sol) == 1 and sp.simplify(sol[0][a_]/b_ + l2/l1) == 0)
bad = sp.expand(RC(K1(z, l1), z**2).subs({a_: 1, b_: 1}) + RC(z, K1(z**2, l2)).subs({a_: 1, b_: 1}) - K1(RC(z, z**2).subs({a_: 1, b_: 1}), l1 + l2 + 1))
check("CONTROL SL(2,R): the wrong ratio (a = b) fails at λ1 = λ2 = 5/2", sp.simplify(bad.subs({l1: sp.Rational(5, 2), l2: sp.Rational(5, 2)})) != 0)
# ---- D_IV^5 ----
Z = sp.symbols('z0:5'); eta = [-1, 1, 1, 1, 1]
lam = sp.Rational(5, 2); Lam = 2*lam + 1
def euler(f): return sum(v*sp.diff(f, v) for v in Z)
def Qz(): return sum(eta[i]*Z[i]**2 for i in range(5))
def Ks(mu, f, L): return sp.expand(Qz()*eta[mu]*sp.diff(f, Z[mu]) - 2*Z[mu]*euler(f) - 2*L*Z[mu]*f)
def Ms(m, n, f): return sp.expand(eta[m]*Z[m]*sp.diff(f, Z[n]) - eta[n]*Z[n]*sp.diff(f, Z[m]))
c1, c2, s = sp.symbols('c1 c2 s')
def Kvec(mu, F, L):
    zF = sum(Z[b]*F[b] for b in range(5))
    return [sp.expand(Ks(mu, F[a], L) + c1*eta[a]*Z[a]*eta[mu]*F[mu]*0 + c1*(Z[a]*F[mu] if False else 0)) for a in range(5)], zF
def Kvec_full(mu, F, L):
    zF = sum(Z[b]*F[b] for b in range(5))           # z^b F_b
    out = []
    for a in range(5):
        # two covariant structures for a vector index a (lower) and direction mu (upper):
        #   S1 = η_aa z^a F_mu η^{mu mu}   ~ z_a F^mu      S2 = δ^mu_a (z·F)
        S1 = eta[a]*Z[a]*eta[mu]*F[mu]
        S2 = zF if a == mu else 0
        out.append(sp.expand(Ks(mu, F[a], L) + c1*S1 + c2*S2))
    return out
def Mvec(m, n, F):
    out = []
    for a in range(5):
        spin = (eta[m]*F[n] if a == m else 0) - (eta[n]*F[m] if a == n else 0)
        out.append(sp.expand(Ms(m, n, F[a]) + s*spin))
    return out
def B(f, g, sign=-1): return [sp.expand(f*sp.diff(g, Z[a]) + sign*g*sp.diff(f, Z[a])) for a in range(5)]
def monos(deg):
    out = [sp.Integer(1)]
    for d in range(1, deg + 1): out += [sp.Mul(*c) for c in cwr(Z, d)]
    return out
test = monos(2)
def eqs_for(sign):
    E = []
    for i, f in enumerate(test):
        for g in test[i:i + 6]:
            for mu in range(5):
                lhs = [x + y for x, y in zip(B(Ks(mu, f, lam), g, sign), B(f, Ks(mu, g, lam), sign))]
                rhs = Kvec_full(mu, B(f, g, sign), Lam)
                for u, v in zip(lhs, rhs):
                    d = sp.expand(u - v)
                    if d != 0: E += sp.Poly(d, *Z).coeffs()
    return E
EK = eqs_for(-1)
solK = sp.solve(EK, [c1, c2], dict=True)
print(f"   antisymmetric bracket: K-intertwining equations {len(EK)}, solution {solK}")
check("D_IV^5: f∂g − g∂f intertwines the K^μ with a UNIQUE nonzero spin term (c1, c2) at target weight 6",
      len(solK) == 1 and len(solK[0]) == 2 and any(v != 0 for v in solK[0].values()))
# rotations: B must be covariant with a vector spin term
EM = []
for f in test[:8]:
    for g in test[3:10]:
        for m in range(5):
            for n in range(m + 1, 5):
                lhs = [x + y for x, y in zip(B(Ms(m, n, f), g), B(f, Ms(m, n, g)))]
                rhs = Mvec(m, n, B(f, g))
                for u, v in zip(lhs, rhs):
                    d = sp.expand(u - v)
                    if d != 0: EM += sp.Poly(d, *Z).coeffs()
solM = sp.solve(EM, [s], dict=True)
check("rotations M_mn: covariant with a unique vector spin term s (the target is the VECTOR (1,0) K-type, as 5816 says)",
      len(solM) == 1, f"{solM}")
# D and P: translation and dilation (weight) — P trivially; D: degree drops by 1, weight 2λ → 2λ+1
okD = True
for f in test[:6]:
    for g in test[:6]:
        lhs = [x + y for x, y in zip(B(euler(f) + lam*f, g), B(f, euler(g) + lam*g))]
        rhs = [euler(u) + Lam*u for u in B(f, g)]
        if any(sp.expand(u - v) != 0 for u, v in zip(lhs, rhs)): okD = False
check("dilation D: weight 2λ → 2λ + 1 = 6 exactly", okD)
ES = eqs_for(+1)
solS = sp.solve(ES, [c1, c2], dict=True)
check("CONTROL: the symmetric f∂g + g∂f fails for EVERY (c1, c2)", solS == [], f"{solS}")
print(f"\nSCORE: {sum(score)}/{len(score)}")
