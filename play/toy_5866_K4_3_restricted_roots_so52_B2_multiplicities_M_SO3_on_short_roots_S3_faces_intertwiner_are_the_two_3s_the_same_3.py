#!/usr/bin/env python3
"""
Toy 5866 — Round K4-3, B-new-1 (Elie, 2026-10-09). Prereg: notes/Elie_K4-3_prereg_toys_5864-5867_* (976951e1).

so(5,2) as 7x7 real matrices X = eta A, A antisymmetric, eta = diag(+1^5, -1^2). Cartan: k = block-diagonal, p = off-diagonal.
a = span{E16+E61, E27+E72}. Restricted roots and multiplicities by simultaneous diagonalisation of ad(a).
M = Z_K(a): its Lie algebra, its component group, its action on each root space (Casimir, traces).
The frame vertex: S3 on three faces, as permutation matrices (1 + 2) and as D3 in SO(3) (2 + sign); dim Hom_S3 into g_{e1}.
The closure face as a label (trivial) and as the vertex axis (sign) against g_long (M-trivial). Killing signature on p.
No data. Every number here is linear algebra.
"""
import itertools
import numpy as np
from fractions import Fraction as Fr

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok))); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

N = 7
eta = np.diag([1, 1, 1, 1, 1, -1, -1]).astype(float)
def E(i, j):
    m = np.zeros((N, N)); m[i, j] = 1; return m
pairs = list(itertools.combinations(range(N), 2))
basis = [eta @ (E(i, j) - E(j, i)) for i, j in pairs]           # 21 generators
assert all(np.allclose(X.T @ eta + eta @ X, 0) for X in basis)
G = np.array([X.ravel() for X in basis]).T                        # 49 x 21
def coords(X):
    c, res, *_ = np.linalg.lstsq(G, X.ravel(), rcond=None)
    assert np.allclose(G @ c, X.ravel(), atol=1e-10), "not in g"
    return c
def ad(X):
    return np.array([coords(X @ Y - Y @ X) for Y in basis]).T    # 21 x 21 in the basis
def is_k(X): return np.allclose(eta @ X @ eta, X)
k_idx = [n for n, (i, j) in enumerate(pairs) if is_k(basis[n])]
p_idx = [n for n in range(21) if n not in k_idx]
print(f"dim g = 21, dim k = {len(k_idx)}, dim p = {len(p_idx)}")

X1, X2 = E(0, 5) + E(5, 0), E(1, 6) + E(6, 1)
assert np.allclose(X1 @ X2 - X2 @ X1, 0) and all(not is_k(X) for X in (X1, X2))
A1, A2 = ad(X1), ad(X2)
assert np.allclose(A1 @ A2, A2 @ A1)

# ---------------------------------------------------------------- R1 restricted roots
rng = np.random.default_rng(5866)
t = rng.normal(size=2)
vals, vecs = np.linalg.eig(t[0] * A1 + t[1] * A2)
assert np.allclose(vals.imag, 0); vecs = vecs.real
roots = {}
for v in vecs.T:
    v = v / np.linalg.norm(v)
    l1, l2 = (v @ A1 @ v) / (v @ v), (v @ A2 @ v) / (v @ v)
    key = (round(l1, 6) + 0.0, round(l2, 6) + 0.0)
    roots.setdefault(key, []).append(v)
mult = {kk: len(vv) for kk, vv in roots.items()}
print("  restricted roots (lambda(X1), lambda(X2)) : multiplicity")
for kk in sorted(mult): print(f"    {kk}: {mult[kk]}")
short = {kk for kk in mult if sorted(abs(x) for x in kk) == [0.0, 1.0]}
long_ = {kk for kk in mult if sorted(abs(x) for x in kk) == [1.0, 1.0]}
zero = (0.0, 0.0)
r1 = (len(short) == 4 and all(mult[s] == 3 for s in short) and len(long_) == 4 and all(mult[l] == 1 for l in long_)
      and mult[zero] == 5 and sum(mult.values()) == 21)
score("R1", r1, f"B2: 4 short roots x mult {sorted(mult[s] for s in short)}, 4 long roots x mult {sorted(mult[l] for l in long_)}, "
                f"zero weight space dim {mult[zero]} = a (2) + m (3)")

# ---------------------------------------------------------------- R2 m and M
# m = z_k(a): X in k with [X, X1] = [X, X2] = 0
Kmat = np.array([coords(basis[n]) for n in k_idx]).T                 # 21 x 11
S = np.vstack([A1 @ Kmat, A2 @ Kmat])
_, sv, vh = np.linalg.svd(S)
null = vh[np.sum(sv > 1e-9):]                                         # rows: kernel coords in k-basis
m_gens = [sum(c * basis[k_idx[i]] for i, c in enumerate(row)) for row in null]
m_support = sorted({pairs[n] for n in k_idx for row in null for i, c in enumerate(row) if abs(c) > 1e-9 and k_idx[i] == n})
# the Z2: diag(-1,-1,1,1,1,-1,-1) in K (det +1 on both blocks), commuting with a
z = np.diag([-1, -1, 1, 1, 1, -1, -1]).astype(float)
z_in_K = np.allclose(eta @ z @ eta, z) and np.isclose(np.linalg.det(z[:5, :5]), 1) and np.isclose(np.linalg.det(z[5:, 5:]), 1)
z_centralises = np.allclose(z @ X1 @ z.T, X1) and np.allclose(z @ X2 @ z.T, X2)
r2 = len(m_gens) == 3 and m_support == [(2, 3), (2, 4), (3, 4)] and z_in_K and z_centralises
score("R2", r2, f"dim m = {len(m_gens)}, m supported on coordinate pairs {m_support} = so(3) on {{3,4,5}}; "
                f"z = diag(-1,-1,1,1,1,-1,-1) in K and centralises a: M = SO(3) x Z2 (component group Z2)")

# ---------------------------------------------------------------- R3 M on the root spaces
# orthonormalise m so that the Casimir on the vector rep is -2 (generators E_ij - E_ji)
m_std = [basis[n] for n in k_idx if pairs[n] in [(2, 3), (2, 4), (3, 4)]]
def restrict(op_mats, space):
    """matrix of a linear map (given in g-coords) restricted to span(space), by least squares."""
    Vs = np.array(space).T
    out = []
    for v in Vs.T:
        w = op_mats @ v
        c, *_ = np.linalg.lstsq(Vs, w, rcond=None)
        assert np.allclose(Vs @ c, w, atol=1e-8), "root space not M-invariant"
        out.append(c)
    return np.array(out).T
cas = {}
for kk, vv in roots.items():
    C = sum(restrict(ad(m) @ ad(m), vv) for m in m_std)
    cas[kk] = sorted(np.round(np.linalg.eigvals(C).real, 6))
def rot(theta, i, j):
    R = np.eye(N); R[i, i] = R[j, j] = np.cos(theta); R[i, j] = -np.sin(theta); R[j, i] = np.sin(theta); return R
def Ad(g):
    return np.array([coords(g @ Y @ np.linalg.inv(g)) for Y in basis]).T
R120 = Ad(rot(2 * np.pi / 3, 2, 3)); R180 = Ad(rot(np.pi, 3, 4)); Zc = Ad(z)
tr = {kk: (np.trace(restrict(R120, vv)), np.trace(restrict(R180, vv)), np.trace(restrict(Zc, vv))) for kk, vv in roots.items()}
r3 = (all(cas[s] == [-2.0, -2.0, -2.0] for s in short) and all(cas[l] == [0.0] for l in long_)
      and all(np.allclose(tr[s], (1 + 2 * np.cos(2 * np.pi / 3), -1, -3)) for s in short)
      and all(np.allclose(tr[l], (1, 1, 1)) for l in long_))
print("    short root space: Casimir eigenvalues", cas[next(iter(short))], " traces (C3, C2, z) =", np.round(tr[next(iter(short))], 6))
print("    long  root space: Casimir eigenvalues", cas[next(iter(long_))], " traces (C3, C2, z) =", np.round(tr[next(iter(long_))], 6))
score("R3", r3, "M acts on EVERY short root space as the SO(3) vector (Casimir -2, chi(C3) = 0, chi(C2) = -1; z = -1) and on every long root space trivially (z = +1)")

# ---------------------------------------------------------------- R4/R5 the frame vertex's S3
def perm_matrix(p):
    P = np.zeros((3, 3))
    for i, j in enumerate(p): P[j, i] = 1
    return P
S3 = list(itertools.permutations(range(3)))
sign = lambda p: round(np.linalg.det(perm_matrix(p)))
chi_perm = {p: np.trace(perm_matrix(p)) for p in S3}
chi_twist = {p: sign(p) * chi_perm[p] for p in S3}
chi_triv = {p: 1 for p in S3}; chi_sign = {p: sign(p) for p in S3}
inner = lambda c1, c2: Fr(int(round(sum(c1[p] * c2[p] for p in S3))), 6)
r4 = inner(chi_perm, chi_triv) == 1 and inner(chi_perm, chi_sign) == 0 and inner(chi_perm, chi_perm) == 2
score("R4", r4, f"faces as permutation matrices: <chi,1> = {inner(chi_perm, chi_triv)}, <chi,sign> = {inner(chi_perm, chi_sign)} -> 1 + 2; the opposite face is a singlet (trivially)")

# D3 in SO(3) on coordinates {3,4,5}: C3 about axis 5 (coords 2,3 rotate), C2 about axis 3 (coords 3,4 rotate by pi)
c3 = rot(2 * np.pi / 3, 2, 3)[2:5, 2:5]; c2 = rot(np.pi, 3, 4)[2:5, 2:5]
# build the group explicitly and match to S3 by its action on three equally spaced unit vectors in the (3,4) plane
pts = [c3 @ np.linalg.matrix_power(c3, kk) @ np.array([1.0, 0, 0]) for kk in range(3)]
elems = [np.eye(3), c3, c3 @ c3, c2, c3 @ c2, c3 @ c3 @ c2]
chi_D3_vec, chi_D3_axis = {}, {}
for g in elems:
    p = tuple(int(np.argmin([np.linalg.norm(g @ pts[i] - q) for q in pts])) for i in range(3))
    chi_D3_vec[p] = np.trace(g); chi_D3_axis[p] = (g @ np.array([0, 0, 1.0]))[2]
assert set(chi_D3_vec) == set(S3)
in_M = all(np.isclose(np.linalg.det(g), 1) for g in elems)
hom_perm = inner(chi_perm, chi_D3_vec); hom_twist = inner(chi_twist, chi_D3_vec)
# the same numbers from the actual root space: traces of Ad(D3 elements) on g_{e1}
e1 = next(s for s in short if abs(s[0]) == 1.0 and s[1] == 0.0 and s[0] > 0)
g7 = lambda g: np.block([[np.eye(2), np.zeros((2, 3)), np.zeros((2, 2))], [np.zeros((3, 2)), g, np.zeros((3, 2))], [np.zeros((2, 2)), np.zeros((2, 3)), np.eye(2)]])
chi_root_vals = sorted(round(np.trace(restrict(Ad(g7(g)), roots[e1])), 6) for g in elems)
chi_vec_vals = sorted(round(v, 6) for v in chi_D3_vec.values())
r5 = (in_M and chi_root_vals == chi_vec_vals and hom_perm == 1 and hom_twist == 2
      and inner(chi_twist, chi_sign) == 1 and inner(chi_D3_vec, chi_sign) == 1)
score("R5", r5, f"D3 in M = SO(3) acts on g_e1 with the vector character (traces {chi_root_vals} = {chi_vec_vals}) = 2 + sign; "
                f"dim Hom_S3(faces -> g_e1) = {hom_perm} for the plain permutation action, {hom_twist} (an isomorphism) for (perm)(x)sign = 5859's std(x)sign")

# ---------------------------------------------------------------- R6 the closure face
axis_char = {p: round(v) for p, v in chi_D3_axis.items()}
r6 = (inner(axis_char, chi_sign) == 1 and inner(axis_char, chi_triv) == 0
      and all(np.allclose(tr[l][:2], (1, 1)) for l in long_))
score("R6", r6, f"vertex AXIS under D3: character {sorted(axis_char.values())} = sign; g_long under the same D3: trivial. "
                "closure face <-> g_long is consistent as a LABEL (trivial <-> trivial), inconsistent as the AXIS (sign <-> trivial)")

# ---------------------------------------------------------------- R7 Killing form signature
ads = [ad(X) for X in basis]
B = np.array([[np.trace(ads[i] @ ads[j]) for j in range(21)] for i in range(21)])
sig = lambda idx: tuple(int(x) for x in (np.sum(np.linalg.eigvalsh(B[np.ix_(idx, idx)]) > 1e-9), np.sum(np.linalg.eigvalsh(B[np.ix_(idx, idx)]) < -1e-9)))
long_dirs = [v for l in long_ for v in roots[l]]
r7 = sig(p_idx) == (10, 0) and sig(k_idx) == (0, 11)
score("R7", r7, f"Killing form: on p signature {sig(p_idx)} (positive definite), on k {sig(k_idx)}. 'Timelike' in K1228 is m_long = 1 as the '1' of 3+1, not a sign of B on p")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail; R4 is the trivial check Keeper named)")
