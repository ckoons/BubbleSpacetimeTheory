#!/usr/bin/env python3
"""
Toy 5821 — γ_{n,l}: which G-invariant vertices shift which double traces (Elie, 2026-09-26, round 9 item 2). Prereg 9175decb.
Antecedent (prompt): "reproduce the HPPS structural statement that a non-derivative quartic contact interaction gives γ_{n,l} ≠ 0
only for l = 0 (the pin comes from Grace; do not use a remembered formula)". At run time (16:0x) Grace's HPPS pin has NOT landed:
the HPPS control is scored 'owed' (a FAIL line), not reproduced from memory. Lyra's su(3) vertex: not yet written → owed.
Model: 5805's tube model on C^5 (x2 for two bodies), so(2,5) at λ = 5/2; the two-body action is the sum.
(a) Schur: H⊗H multiplicity-free (5816/5820) ⇒ every G-invariant Hermitian V = Σ c_{n,l} Π_{n,l}; γ_{n,l} = c_{n,l} (first order).
(b) BST-native contact = evaluation at a point of the Hermitian domain = diagonal restriction R: F(z1,z2) ↦ F(z,z).
    Checked: R intertwines the two-body so(2,5) action at (5/2, 5/2) with the one-body action at λ = 5 (all generators, exact).
    Every double-trace primary except (0,0) is a polynomial in u = z1 − z2 with no constant term (5820) ⇒ R kills it, and (R
    intertwining) its whole module ⇒ R†R = c·Π_{0,0}: the holomorphic contact shifts ONLY [φφ]_{0,0}.
"""
import sympy as sp
from itertools import combinations_with_replacement as cwr
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
A = sp.symbols('a0:5'); B = sp.symbols('b0:5'); Zs = sp.symbols('z0:5'); eta = [-1, 1, 1, 1, 1]
lam = sp.Rational(5, 2)
def gens(V, L):
    Q = sum(eta[i]*V[i]**2 for i in range(5))
    eul = lambda f: sum(v*sp.diff(f, v) for v in V)
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
R = lambda F: sp.expand(F.subs({**{a: z for a, z in zip(A, Zs)}, **{b: z for b, z in zip(B, Zs)}}, simultaneous=True))
def monos(N):
    out = [sp.Integer(1)]
    for d in range(1, N + 1): out += [sp.Mul(*c) for c in cwr(A + B, d)]
    return out
test = monos(2) + [A[0]*A[1]*B[2], A[3]**2*B[0], B[1]*B[4]*A[4]]
ok = True; bad = None
for key in G0:
    for F in test:
        lhs = R(sp.expand(G1[key](F) + G2[key](F)))
        rhs = sp.expand(G0[key](R(F)))
        if sp.expand(lhs - rhs) != 0: ok = False; bad = (key, F); break
    if not ok: break
check("(b) diagonal restriction R intertwines two-body so(2,5) at (5/2,5/2) with one-body at λ = 5 (P, K, D, M; exact)", ok, str(bad))
# primaries (lowest vectors) are polynomials in u = a − b (5820); R(u-polynomial without constant term) = 0
u = [a - b for a, b in zip(A, B)]
Qu = sum(eta[i]*u[i]**2 for i in range(5))
prim = {(0, 0): sp.Integer(1), (0, 1): u[1], (0, 2): u[1]*u[2], (1, 0): Qu, (1, 1): Qu*u[3], (0, 3): u[1]*u[2]*u[3], (2, 0): Qu**2}
vals = {k: R(sp.expand(v)) for k, v in prim.items()}
print("   R(primary [φφ]_{n,l}) for sample (n,l):", {k: v for k, v in vals.items()})
check("(b) R kills every sampled double-trace primary except (0,0); R(1) = 1", all((v == 0) == (k != (0, 0)) for k, v in vals.items()))
# lowest-vector check: sampled primaries are annihilated by the total lowering P1+P2
okP = all(sp.expand(G1[('P', mu)](sp.expand(v)) + G2[('P', mu)](sp.expand(v))) == 0 for v in prim.values() for mu in range(5))
check("(b) the sampled primaries are lowest vectors (total P annihilates them)", okP)
# ⇒ R†R ∝ Π_{0,0}; descendants of (n,l) ≠ (0,0) stay in ker R (intertwining): test on K-raised descendants
okDesc = True
for k, v in prim.items():
    if k == (0, 0): continue
    for mu in (0, 2):
        dsc = sp.expand(G1[('K', mu)](sp.expand(v)) + G2[('K', mu)](sp.expand(v)))
        if R(dsc) != 0: okDesc = False
check("(b) K-raised descendants of every (n,l) ≠ (0,0) primary also vanish under R ⇒ R†R = c·Π_{0,0}: γ_{0,0} ≠ 0, all other γ_{n,l} = 0", okDesc)
# (a) Schur, stated with its input: multiplicity-free (5816, 5820) ⇒ G-invariant V diagonal; any profile c_{n,l} realisable
print("   [statement, not scored — run 1 scored it as a hard-coded True, removed] (a) Schur: with H⊗H multiplicity-free (5816, 5820 — both computed), every G-invariant vertex is Σ c_{n,l}Π_{n,l}; "
      "representation theory allows EVERY γ-profile — it constrains nothing until a vertex is named")
check("HPPS CONTROL: OWED — Grace's numbered-equation pin had not landed at run time; not reproduced from memory", False)
check("su(3) VERTEX (Lyra): OWED — not written at run time", False)
print("\nCALIBRATION (prereg): a point of D_IV^5 has compact stabilizer K = SO(5)xSO(2); a point of AdS_6 = SO(5,2)/SO(5,1) has")
print("noncompact stabilizer. The holomorphic contact (b) is NOT HPPS's AdS contact; that it shifts only (0,0) is a DIFFERENCE, to be")
print("set against HPPS's own statement once pinned. (b) is a named vertex, not a forced one: the kill 'γ ≡ 0 for every BST-named vertex'")
print("does not fire, and whether BST FORCES any vertex is not answered here (Cal S997: the colour bit picks the group, not whether γ ≠ 0).")
print(f"\nSCORE: {sum(score)}/{len(score)}")
