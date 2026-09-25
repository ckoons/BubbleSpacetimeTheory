#!/usr/bin/env python3
"""
Toy 5787 — K1924 Section 3, the act and the record, as linear algebra (Elie, 2026-09-25; round 3 item 2).

Setup: W = V_live (+) V_rec, each C^3. Rotations so(3) = stab(q,h) on V_live (the live spatial space).
Colour = stab(eps_rec, h_rec) acting on V_rec only (su(3), from toy 5782).
Two cases:
  UNTIED: rotations act on V_live only: R -> diag(R, I).
  TIED:   the record is a copy of the live space through the real structure, so rotations also act
          on it: R -> diag(R, R) (the induced action).
Exact computation (sympy rationals): dimension of the commutant of the rotation action inside colour,
  {X in su(3)_rec : [X, rho(L_k)] = 0 for all k}, and the spin carried by V_rec under rho.

DIRECTION BEFORE NUMBERS:
  P1 UNTIED: commutant = all of su(3) (dim 8); V_rec carries spin 0 (three singlets) -> colour
     commutes with rotations (Coleman-Mandula compatible).
  P2 TIED: commutant = 0; V_rec carries spin 1 -> the spin-1 kill, and colour does not commute
     with rotations.
  P3 A tie through a DIFFERENT intertwiner (any g in GL(3) conjugating R on V_rec) gives the same
     numbers as P2 — so the kill depends only on whether rotations act on the record, not how.
  P4 (control) su(3)_rec has dim 8 in the doubled space.
"""
import sympy as sp

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

def Lgen():
    out = []
    for (i, j) in [(1, 2), (2, 0), (0, 1)]:
        M = sp.zeros(3); M[i, j] = -1; M[j, i] = 1   # real antisymmetric (rotation generator)
        out.append(M)
    return out
Ls = Lgen()

def block(A, B):
    Z = sp.zeros(6)
    Z[:3, :3] = A; Z[3:, 3:] = B
    return Z

# su(3) on V_rec: 8 real params, X = A + iB traceless antihermitian
p = sp.symbols('p0:8', real=True)
def su3(pv):
    a, b, c, d, e, f, g, h = pv
    X = sp.Matrix([[sp.I*a, b + sp.I*c, d + sp.I*e],
                   [-b + sp.I*c, sp.I*g, f + sp.I*h],
                   [-d + sp.I*e, -f + sp.I*h, -sp.I*(a + g)]])
    return X
Xr = su3(p)
Xfull = block(sp.zeros(3), Xr)

def commutant_dim(rho):
    eqs = []
    for L in rho:
        C = Xfull*L - L*Xfull
        for e in C:
            e = sp.expand(e)
            eqs += [sp.re(e), sp.im(e)]
    eqs = [e for e in eqs if e != 0]
    if not eqs:
        return 8
    A = sp.Matrix([[sp.diff(e, v) for v in p] for e in eqs])
    return 8 - A.rank()

def spin_on_rec(rho):
    # Casimir of the Hermitian generators i*rho restricted to V_rec block
    C = sum((((sp.I*L)[3:, 3:])**2 for L in rho), sp.zeros(3))
    C = sp.simplify(C)
    return C

print("Toy 5787 — act vs record\n")
print("DIRECTION: P1 untied commutant 8, spin 0; P2 tied commutant 0, spin 1; P3 any intertwiner = P2; P4 control dim 8\n")

# P4 control
chk = sp.Matrix([[sp.diff(e, v) for v in p] for e in sum(([sp.re(sp.expand(x)), sp.im(sp.expand(x))] for x in Xr), [])])
check("P4 su(3)_rec has real dimension 8 (param map injective)", chk.rank() == 8, can_fail=False)

untied = [block(L, sp.zeros(3)) for L in Ls]
tied = [block(L, L) for L in Ls]
cu, ct = commutant_dim(untied), commutant_dim(tied)
Su, St = spin_on_rec(untied), spin_on_rec(tied)
print(f"  UNTIED: commutant dim = {cu}; Casimir on V_rec = {Su.tolist()}")
print(f"  TIED:   commutant dim = {ct}; Casimir on V_rec = {St.tolist()}")
check("P1 untied: colour commutes with rotations (commutant = 8) and V_rec is spin 0", cu == 8 and Su == sp.zeros(3))
check("P2 tied: commutant = 0 and V_rec is spin 1 (Casimir 2*I)", ct == 0 and St == 2*sp.eye(3))

g = sp.Matrix([[1, 2, 0], [0, 1, 3], [1, 0, 1]])   # a generic intertwiner (det != 0)
tied_g = [block(L, g*L*g.inv()) for L in Ls]
cg, Sg = commutant_dim(tied_g), spin_on_rec(tied_g)
check("P3 tie through a generic intertwiner: commutant 0, Casimir eigenvalues all 2 (spin 1)",
      cg == 0 and set(Sg.eigenvals().keys()) == {2})

# also: record frozen at commit time t0, rotations applied later act on live only — equals UNTIED
# a partial tie (record rotated by R^0 for 'archived') is UNTIED; the only other option is TIED
print("\n  Reading: 'the record is fixed at commit; later rotations act on the live space' IS the untied case.")
print("  The kill returns exactly when any induced rotation reaches the record (P2/P3), whatever the map.")

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
