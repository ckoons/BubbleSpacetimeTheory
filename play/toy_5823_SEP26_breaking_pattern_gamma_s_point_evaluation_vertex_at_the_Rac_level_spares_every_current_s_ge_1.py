#!/usr/bin/env python3
"""
Toy 5823 — breaking pattern γ_s (s = 0..6) of the point-evaluation vertex at the Rac level (Elie, 2026-09-26, R10 item 2).
Prereg 5d4ce093 (labels repaired). Antecedent (prompt): "for each candidate Lyra writes as an operator, compute whether the
spin-s current stays at 3 + s (γ_s = 0) or moves … Start with the point-evaluation vertex (your 5821) acting at the Rac level."
INVARIANT: the vertex V = R†R with R the diagonal restriction F(z1,z2) ↦ F(z,z) — G-COVARIANT (an intertwiner), i.e. 'a write at
every point'. NOT the same object as a write at ONE fixed point z0 (F ↦ F(z0,z0)), which breaks translations and hence T (Cal S999).
Rac⊗Rac primaries (5822 Test B): h_s(u), u = z1 − z2, harmonic, one per spin s at weight 3 + s.
"""
import sympy as sp
from itertools import combinations_with_replacement as cwr
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
A = sp.symbols('a0:5'); B = sp.symbols('b0:5'); Zs = sp.symbols('z0:5'); eta = [-1, 1, 1, 1, 1]
lam = sp.Rational(3, 2)
def gens(V, L):
    Q = sum(eta[i]*V[i]**2 for i in range(5)); eul = lambda f: sum(v*sp.diff(f, v) for v in V)
    G = {}
    for mu in range(5):
        G[('P', mu)] = lambda f, mu=mu: sp.diff(f, V[mu])
        G[('K', mu)] = lambda f, mu=mu: Q*eta[mu]*sp.diff(f, V[mu]) - 2*V[mu]*eul(f) - 2*L*V[mu]*f
    G[('D',)] = lambda f: eul(f) + L*f
    for m in range(5):
        for n in range(m + 1, 5):
            G[('M', m, n)] = lambda f, m=m, n=n: eta[m]*V[m]*sp.diff(f, V[n]) - eta[n]*V[n]*sp.diff(f, V[m])
    return G
G1, G2, G0 = gens(A, lam), gens(B, lam), gens(Zs, 2*lam)
R = lambda F: sp.expand(sp.expand(F).subs({**{a: z for a, z in zip(A, Zs)}, **{b: z for b, z in zip(B, Zs)}}, simultaneous=True))
test = [sp.Integer(1), A[0], B[1], A[0]*B[0], A[1]*A[2], A[2]*B[3]*B[4], A[4]**2*B[0]]
ok = all(sp.expand(R(G1[k](F) + G2[k](F)) - G0[k](R(F))) == 0 for k in G0 for F in test)
check("R intertwines Rac⊗Rac (3/2, 3/2) with the one-body scalar at weight 3 (P, K, D, M exact)", ok)
# a harmonic spin-s primary in u for s = 0..6: (u1 + i u2)^s is harmonic for Q = -u0² + Σu_i² (null vector in the (1,2) plane)
u = [a - b for a, b in zip(A, B)]
def prim(s): return sp.expand((u[1] + sp.I*u[2])**s)
Qd = lambda f, V: sum(eta[i]*sp.diff(f, V[i], 2) for i in range(5))
harm_ok = all(sp.expand(Qd(prim(s), A)) == 0 and sp.expand(Qd(prim(s), B)) == 0 for s in range(7))
low_ok = all(sp.expand(G1[('P', mu)](prim(s)) + G2[('P', mu)](prim(s))) == 0 for s in range(7) for mu in range(5))
check("primaries h_s = (u1 + i u2)^s, s = 0..6: in Rac⊗Rac (each factor harmonic) and lowest (total P kills them)", harm_ok and low_ok)
gam = []
for s in range(7):
    v = R(prim(s))
    desc = [R(G1[('K', mu)](prim(s)) + G2[('K', mu)](prim(s))) for mu in (0, 1, 3)]
    gam.append((s, v != 0 or any(d != 0 for d in desc)))
print("   s:  ", [s for s, _ in gam]); print("   γ_s ≠ 0:", [int(g) for _, g in gam])
check("PATTERN: γ_0 ≠ 0 (the scalar at 3, not a current); γ_s = 0 for s = 1..6 — every conserved current is SPARED",
      gam[0][1] and not any(g for _, g in gam[1:]))
check("KILL for this candidate as the breaker FIRES (prereg): γ_s = 0 for all s ≥ 3 — the G-covariant point evaluation cannot break higher spin",
      not any(g for s, g in gam if s >= 3))
print("\nREADING: a G-covariant vertex commutes with the conformal algebra, so it can shift a module only by Schur; the diagonal")
print("restriction sees only the scalar. 'Commit = a write at every point' spares every current, so it cannot be the s > 2 breaker.")
print("A write at ONE fixed point is a different, non-covariant object; it breaks translations and so T (Cal S999) — it breaks s = 2")
print("too, i.e. the wrong pattern in the other direction. Other candidates: OWED until Lyra writes them as operators.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
