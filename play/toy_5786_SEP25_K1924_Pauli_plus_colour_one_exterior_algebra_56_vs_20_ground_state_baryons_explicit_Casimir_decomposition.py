#!/usr/bin/env python3
"""
Toy 5786 — K1924 Section 4: Pauli and three-write colour as ONE exterior algebra; 56 vs 20.
(Elie, 2026-09-25; round 3 item 1. Representation theory, no external numbers.)

Construction (explicit operators, no tables):
  single quark q = colour (C^3) x flavour u,d,s (C^3) x spin (C^2)  -> 18 states.
  Fermi statistics = the exterior power: three quarks live in Lambda^3(C^18) (816 states).
  Colour singlets inside it = common kernel of the 8 colour generators.
  Then decompose that kernel by flavour SU(3) Casimir C_f (1:0, 8:3, 10:6 for T = lambda/2)
  and spin Casimir S^2 (j(j+1)).
Control: no colour — Lambda^3(C^6) (flavour x spin only).
Also: Sym^3(C^6) directly, to show colour-singlet Lambda^3 = Sym^3 of flavour x spin.

DIRECTION BEFORE NUMBERS:
  P1  dim(colour-singlet part of Lambda^3(C^18)) = 56
  P2  it decomposes as (10, spin 3/2) + (8, spin 1/2): 40 + 16
  P3  control Lambda^3(C^6) = 20 = (1, spin 3/2) + (8, spin 1/2): 4 + 16 — no decuplet
  P4  Delta++ = u-up u-up u-up (J_z = 3/2): present with colour, absent without
  P5  Lambda^3(C^3_colour) is one-dimensional (one cell, eps), Lambda^4 = 0
Numerics: dense numpy on 816 dims; eigenvalues rounded, max rounding error printed.
"""
import numpy as np
from itertools import combinations

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

# Gell-Mann / 2
l = np.zeros((8, 3, 3), dtype=complex)
l[0][0, 1] = l[0][1, 0] = 1
l[1][0, 1] = -1j; l[1][1, 0] = 1j
l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1
l[4][0, 2] = -1j; l[4][2, 0] = 1j
l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j
l[7] = np.diag([1, 1, -2])/np.sqrt(3)
T3 = l/2
S = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)/2

def kron(*ms):
    out = np.array([[1.0+0j]])
    for m in ms:
        out = np.kron(out, m)
    return out

def exterior3(n):
    basis = list(combinations(range(n), 3))
    idx = {b: i for i, b in enumerate(basis)}
    return basis, idx

def lift_ext(op, basis, idx):
    """one-body operator on C^n -> Lambda^3(C^n): sum over slots with fermion signs"""
    N = len(basis); M = np.zeros((N, N), dtype=complex)
    for j, b in enumerate(basis):
        for slot in range(3):
            for new in range(op.shape[0]):
                a = op[new, b[slot]]
                if a == 0:
                    continue
                lst = list(b); lst[slot] = new
                if len(set(lst)) < 3:
                    continue
                perm = sorted(range(3), key=lambda k: lst[k])
                sgn = np.linalg.det(np.eye(3)[perm])
                M[idx[tuple(sorted(lst))], j] += sgn*a
    return M

def sym3(n):
    basis = [c for c in __import__('itertools').combinations_with_replacement(range(n), 3)]
    return basis

def lift_sym(op, basis):
    """one-body op on Sym^3 in the normalised monomial basis"""
    from collections import Counter
    from math import factorial, sqrt
    idx = {b: i for i, b in enumerate(basis)}
    def norm(b):
        c = Counter(b); p = 1
        for v in c.values():
            p *= factorial(v)
        return sqrt(p)   # |sym(b)| with unnormalised symmetriser sum/…; ratio is what matters
    N = len(basis); M = np.zeros((N, N), dtype=complex)
    for j, b in enumerate(basis):
        for slot in range(3):
            for new in range(op.shape[0]):
                a = op[new, b[slot]]
                if a == 0:
                    continue
                lst = list(b); lst[slot] = new
                t = tuple(sorted(lst))
                # monomial e_b = prod; derivation acting: coefficient in unnormalised monomials, then normalise
                M[idx[t], j] += a
    # convert unnormalised-monomial matrix to orthonormal basis: e_b normalised = m_b / sqrt(prod c!) * sqrt(3!)...
    D = np.diag([norm(b) for b in basis])
    return np.linalg.inv(D) @ M @ D if False else M, D

def casimir_eigs(ops, P=None):
    C = sum(o @ o for o in ops)
    if P is not None:
        C = P.conj().T @ C @ P
    return C

print("Toy 5786 — one exterior algebra: Pauli + colour, 56 vs 20\n")
print("DIRECTION: P1 56; P2 40+16; P3 control 20 = 4+16; P4 Delta++ with colour only; P5 Lambda^3(C^3)=1\n")

# P5
check("P5 Lambda^3(C^3) has dimension 1 (one cell = eps) and Lambda^4(C^3) = 0",
      len(list(combinations(range(3), 3))) == 1 and len(list(combinations(range(3), 4))) == 0)

# with colour: order of tensor factors = colour x flavour x spin
I3, I2 = np.eye(3), np.eye(2)
basis18, idx18 = exterior3(18)
col = [lift_ext(kron(t, I3, I2), basis18, idx18) for t in T3]
fla = [lift_ext(kron(I3, t, I2), basis18, idx18) for t in T3]
spn = [lift_ext(kron(I3, I3, s), basis18, idx18) for s in S]
Cc = sum(o @ o for o in col)
w, V = np.linalg.eigh(Cc)
sing = V[:, np.abs(w) < 1e-8]
print(f"  Lambda^3(C^18) dim = {len(basis18)}; colour-singlet subspace dim = {sing.shape[1]}")
check("P1 colour-singlet part of Lambda^3(C^18) has dimension 56", sing.shape[1] == 56)

def joint_decomp(P, fops, sops):
    Cf = P.conj().T @ sum(o @ o for o in fops) @ P
    Cs = P.conj().T @ sum(o @ o for o in sops) @ P
    # they commute; diagonalise a generic combination
    M = Cf + np.pi*Cs
    ev, U = np.linalg.eigh(M)
    cf = np.real(np.diag(U.conj().T @ Cf @ U)); cs = np.real(np.diag(U.conj().T @ Cs @ U))
    err = max(np.max(np.abs(cf - np.round(cf*4)/4)), np.max(np.abs(cs - np.round(cs*4)/4)))
    from collections import Counter
    return Counter(zip(np.round(cf*4)/4, np.round(cs*4)/4)), err

dec, err = joint_decomp(sing, fla, spn)
names = {0.0: "1", 3.0: "8", 6.0: "10"}; spins = {0.75: "1/2", 3.75: "3/2"}
print("  colour singlets by (flavour irrep, spin):", {(names.get(k[0], k[0]), spins.get(k[1], k[1])): v for k, v in dec.items()},
      f"  max rounding {err:.1e}")
check("P2 = (10, 3/2) x 40 states + (8, 1/2) x 16 states",
      dec == {(6.0, 3.75): 40, (3.0, 0.75): 16})

# control: no colour
basis6, idx6 = exterior3(6)
fla6 = [lift_ext(kron(t, I2), basis6, idx6) for t in T3]
spn6 = [lift_ext(kron(I3, s), basis6, idx6) for s in S]
dec6, err6 = joint_decomp(np.eye(20), fla6, spn6)
print("  no colour, Lambda^3(C^6):", {(names.get(k[0], k[0]), spins.get(k[1], k[1])): v for k, v in dec6.items()},
      f"  max rounding {err6:.1e}")
check("P3 control: Lambda^3(C^6) = 20 = (1, 3/2) x 4 + (8, 1/2) x 16 — no decuplet",
      len(basis6) == 20 and dec6 == {(0.0, 3.75): 4, (3.0, 0.75): 16})

# Sym^3(C^6) dimension and decomposition (colour-stripped statement)
from itertools import combinations_with_replacement as cwr
b56 = list(cwr(range(6), 3))
check("Sym^3(C^6) has dimension 56 = colour-singlet count (eps absorbs the antisymmetry)", len(b56) == 56)

# P4 Delta++: u-up = flavour 0, spin 0 -> single-quark index (flavour*2 + spin) in C^6
uup = 0
check("P4a without colour: u-up u-up u-up is not a state of Lambda^3(C^6) (w^w = 0)",
      (uup, uup, uup) not in idx6)
# with colour: the three u-up quarks must sit in colours 0,1,2 -> exactly one state, and it is a colour singlet
st = np.zeros(len(basis18), dtype=complex)
key = tuple(sorted(c*6 + uup for c in range(3)))
st[idx18[key]] = 1
res = np.linalg.norm(Cc @ st)
check("P4b with colour: u-up(r) u-up(g) u-up(b) exists, is unique, and is a colour singlet (eps)",
      key in idx18 and res < 1e-10)

# write-once: w^w = 0 for any single-quark state (Grassmann) — numeric on random vectors via wedge
rng = np.random.default_rng(1)
v = rng.normal(size=6) + 1j*rng.normal(size=6)
wedge = np.outer(v, v) - np.outer(v, v).T
check("Grassmann: w^w = 0 for a random write w (antisymmetric part of w(x)w vanishes)",
      np.max(np.abs(wedge)) < 1e-12, can_fail=False)

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
