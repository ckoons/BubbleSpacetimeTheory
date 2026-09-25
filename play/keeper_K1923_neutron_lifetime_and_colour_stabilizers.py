#!/usr/bin/env python3
"""Keeper K1923 -- two exact/linear-algebra instruments for the 2026-09-25 team prompt.

PART A. What register row A2 (|V_us| = 1/sqrt(20), first row exactly unitary) says about the FREE NEUTRON.
  Master formula (neutron beta decay, radiative corrections included):
      |V_ud|^2 * tau_n * (1 + 3 lambda^2) = K
  K = 4905.7(1.7) s  (arXiv:2501.17916 master formula)   and   K = 4908(4) s (Czarnecki-Marciano-Sirlin, PRL 120 202002, 2018)
  lambda = g_A/g_V:  PERKEO III  1.27641(56)  [stat 45, sys 33 in quadrature];  PDG  1.2756(13).
  BST row A2: |V_ud|^2 = 1 - 1/20 = 19/20 (|V_ub|^2 ~ 1.5e-5 shown as a sensitivity only).
  Measured: UCNtau (bottle) 877.75(34) s; beam method ~ 887.7 s  (for the COMPARE line only; not an input).

PART B. Linear algebra on V12 (the Peirce 1/2-space of D_IV^5, complex dim n_C - 2 = 3): real dimension of the
  Lie algebra of gl(3,C) preserving each combination of
      eps  : the volume form  (three writes -> one cell; the determinant)        -> tr X = 0
      h    : the Hermitian (Bergman) form                                         -> X^dagger + X = 0
      q    : the complex-bilinear Jordan form on V12 (the one F4's group keeps)    -> X^T + X = 0
  Expected: {eps}=sl(3,C) 16 | {h}=u(3) 9 | {eps,h}=su(3) 8 | {q}=o(3,C) 6 | {q,h}=o(3) 3 | {eps,h,q}=so(3) 3.
  Invariant tensors of the {eps,h} group: delta (from h: the meson pairing q-bar q) and eps (the baryon).
"""
import itertools
import numpy as np

# ---------------- PART A ----------------
def tau(K, lam, vud2):
    return K / (vud2 * (1 + 3 * lam * lam))

def dtau(K, dK, lam, dlam, vud2):
    t = tau(K, lam, vud2)
    rel = np.hypot(dK / K, (6 * lam * lam / (1 + 3 * lam * lam)) * dlam / lam)
    return t * rel

VUD2 = 19 / 20
print("PART A -- tau_n implied by row A2 (|V_ud|^2 = 19/20) and measured g_A")
for kname, K, dK in [("K=4905.7(1.7) [2501.17916]", 4905.7, 1.7), ("K=4908(4) [CMS 2018]", 4908.0, 4.0)]:
    for lname, lam, dlam in [("PERKEO III 1.27641(56)", 1.27641, 0.00056), ("PDG 1.2756(13)", 1.2756, 0.0013)]:
        t, e = tau(K, lam, VUD2), dtau(K, dK, lam, dlam, VUD2)
        print(f"  {kname:28s} {lname:24s} tau_n = {t:7.2f} +- {e:4.2f} s")
t_vub = tau(4905.7, 1.27641, VUD2 - 1.5e-5) - tau(4905.7, 1.27641, VUD2)
print(f"  sensitivity to |V_ub|^2 = 1.5e-5: {t_vub:+.3f} s")
t_super = tau(4905.7, 1.27641, 0.97373 ** 2)
print(f"  for comparison, superallowed |V_ud| = 0.97373 gives tau_n = {t_super:.2f} s (same K, PERKEO III)")
print("  COMPARE (measured, read last): UCNtau bottle 877.75(34) s; beam ~887.7 s")

tA, eA = tau(4905.7, 1.27641, VUD2), dtau(4905.7, 1.7, 1.27641, 0.00056, VUD2)
a1 = abs(tA - 877.75) / np.hypot(eA, 0.34) < 2.0          # consistent with the bottle
a2 = abs(tA - 887.7) / np.hypot(eA, 2.2) > 3.0            # beam value excluded at >3 sigma (beam error ~2.2 s, Grace pins)
a3 = tA < t_super                                          # BST's V_ud is larger -> shorter lifetime than superallowed

# ---------------- PART B ----------------
def basis_gl3C():
    B = []
    for i, j in itertools.product(range(3), range(3)):
        E = np.zeros((3, 3), complex); E[i, j] = 1; B.append(E)
        E = np.zeros((3, 3), complex); E[i, j] = 1j; B.append(E)
    return B  # 18 real generators

def real_rows(M):
    return np.concatenate([M.real.ravel(), M.imag.ravel()])

CONSTRAINTS = {
    "eps": lambda X: np.array([np.trace(X)]),
    "h":   lambda X: X.conj().T + X,
    "q":   lambda X: X.T + X,
}

def stab_dim(keys):
    B = basis_gl3C()
    cols = []
    for X in B:
        cols.append(np.concatenate([real_rows(np.atleast_2d(CONSTRAINTS[k](X))) for k in keys]))
    A = np.array(cols).T
    return 18 - np.linalg.matrix_rank(A, tol=1e-9)

print("\nPART B -- real dimension of the stabilizer in gl(3,C) of structures on V12 (C^3)")
expect = {("eps",): 16, ("h",): 9, ("eps", "h"): 8, ("q",): 6, ("h", "q"): 3, ("eps", "h", "q"): 3}
bok = True
for keys, e in expect.items():
    d = stab_dim(keys)
    name = {16: "sl(3,C)", 9: "u(3)", 8: "su(3)", 6: "o(3,C)", 3: "o(3)/so(3)"}[e]
    print(f"  {'+'.join(keys):10s} dim {d:2d}  (expected {e:2d} = {name})  {'PASS' if d == e else 'FAIL'}")
    bok &= (d == e)

# control: a random extra constraint (preserve a generic vector) must cut su(3) below 8
v = np.array([1, 2j, -1 + 0.5j]); v /= np.linalg.norm(v)
CONSTRAINTS["v"] = lambda X: (X @ v)
ctrl = stab_dim(("eps", "h", "v")) < 8
print(f"  control: su(3) fixing a generic vector has dim {stab_dim(('eps','h','v'))} < 8  {'PASS' if ctrl else 'FAIL'}")

checks = [("A1 row-A2 tau_n within 2 sigma of the bottle value", a1),
          ("A2 row-A2 tau_n excludes the beam value at >3 sigma", a2),
          ("A3 row-A2 V_ud gives a shorter lifetime than the superallowed V_ud", a3),
          ("B  stabilizer dimensions (6 structures) as expected", bok),
          ("CONTROL extra structure cuts su(3)", ctrl)]
fails = 0
for n, ok in checks:
    print(("PASS " if ok else "FAIL ") + n); fails += (not ok)
print(f"SCORE: {len(checks) - fails}/{len(checks)}")
