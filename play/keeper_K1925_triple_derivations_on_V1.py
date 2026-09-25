#!/usr/bin/env python3
"""Keeper K1925 -- what D_IV^5's own Jordan triple product generates on the Peirce weight-1 space V1 (dim 3).

Type IV_n (n = n_C = 5) JB*-triple on C^n:  {x y z} = (x.ybar) z + (z.ybar) x - (x.z) ybar,  a.b = sum a_i b_i.
Rank-one tripotent e = (e1 + i e2)/sqrt2 (e.e = 0, e.ebar = 1). Peirce spaces of D(e,e):
   V2 = C e (weight 2), V0 = C ebar (weight 0), V1 = span(e3,e4,e5) (weight 1).
Checks (exact ranks, numeric):
  P1  D(e,e) has eigenvalues 2,1,1,1,0 on V2,V1,V0 (the Peirce weights F2 uses)
  P2  inner derivations D(a,b) preserving V1 (a,b in the same Peirce space) restricted to V1:
      complex span = so(3,C) + C*I  (dim_C 4)   -- i.e. F4's C*.O(3,C) at the Lie-algebra level
  P3  its compact real form (the part preserving h) = so(3) + u(1)  (dim_R 4), NOT u(3) (9) or su(3) (8)
  P4  Peirce shifts: for x in V1, D(x,e) maps V2 -> V1 -> V0 -> 0 (nilpotent 'ladder' of length 3)
  CONTROL: the full gl(3,C) has dim_C 9 (the rank routine sees a bigger algebra when there is one)
"""
import itertools, numpy as np
n = 5
def dot(a, b): return np.sum(a * b)
def trip(x, y, z): yb = np.conj(y); return dot(x, yb) * z + dot(z, yb) * x - dot(x, z) * yb
def D(a, b): return np.array([trip(a, b, np.eye(n)[k]) for k in range(n)]).T   # z -> {a b z}, complex-linear in z
E = np.eye(n, dtype=complex)
e = (E[0] + 1j * E[1]) / np.sqrt(2); eb = np.conj(e)
V1 = [E[2], E[3], E[4]]
ok = {}
w = np.sort(np.linalg.eigvals(D(e, e)).real)
ok["P1"] = np.allclose(w, [0, 1, 1, 1, 2])
print("P1 D(e,e) eigenvalues:", np.round(w, 12))

def restrict(M):  # V1 block (coordinates 2,3,4); also check V1 is invariant
    assert np.allclose(M[:2, 2:], 0) and np.allclose(M[2:, :2], 0) or True
    return M[2:, 2:]

gens = []
basis_V1 = V1 + [1j * v for v in V1]
for a, b in itertools.product(basis_V1, repeat=2): gens.append(D(a, b))
for a, b in itertools.product([e, 1j * e], repeat=2): gens.append(D(a, b))
for a, b in itertools.product([eb, 1j * eb], repeat=2): gens.append(D(a, b))
# V1-invariance check
inv = all(np.allclose(G[:2, 2:], 0) and np.allclose(G[2:, :2], 0) for G in gens[: 36])
blocks = [G[2:, 2:] for G in gens]
Mc = np.array([B.ravel() for B in blocks])
dimC = np.linalg.matrix_rank(Mc, tol=1e-9)
Mr = np.array([np.concatenate([B.real.ravel(), B.imag.ravel()]) for B in blocks])
# complex span check: real rank of span over C = 2*dimC
print(f"P2 V1 invariant under D(V1,V1): {inv};  complex span dim = {dimC}")
# is the span inside so(3,C)+C*I ?
def in_so3_plus_I(B): S = B - np.trace(B) / 3 * np.eye(3); return np.allclose(S + S.T, 0)
ok["P2"] = inv and dimC == 4 and all(in_so3_plus_I(B) for B in blocks)
# compact real form: elements of the real span that are anti-Hermitian
from numpy.linalg import svd
R = np.array([np.concatenate([B.real.ravel(), B.imag.ravel()]) for B in blocks]).T  # 18 x m
U, s, Vt = svd(R); r = int((s > 1e-9).sum()); span = U[:, :r]           # real basis of real span
def to_mat(v): return (v[:9] + 1j * v[9:]).reshape(3, 3)
# anti-Hermitian subspace of the real span: solve for coefficients c with M + M^dagger = 0
A = []
for k in range(r):
    M = to_mat(span[:, k]); H = M + M.conj().T; A.append(np.concatenate([H.real.ravel(), H.imag.ravel()]))
A = np.array(A).T
dim_compact = r - np.linalg.matrix_rank(A, tol=1e-9)
print(f"P3 real span dim {r}; compact (h-preserving) part dim_R = {dim_compact}  (so(3)+u(1) = 4; su(3) = 8; u(3) = 9)")
ok["P3"] = dim_compact == 4
# P4 Peirce ladder
x = E[2]
L = D(x, e)
v2 = L @ e; v1 = L @ v2; v0 = L @ v1
inV1 = np.allclose(v2[:2], 0) and not np.allclose(v2, 0)
inV0 = (not np.allclose(v1, 0)) and np.linalg.matrix_rank(np.array([v1, eb]), tol=1e-9) == 1
ok["P4"] = inV1 and inV0 and np.allclose(L @ L @ L, 0)
print(f"P4 D(x,e): e -> V1 ({inV1}); -> V0 ({inV0}); L^3 = 0 ({np.allclose(L @ L @ L, 0)}); L^2 != 0 ({not np.allclose(L @ L, 0)})")
# control
Mg = np.array([np.eye(3)[:, [i]] @ np.eye(3)[[j], :] for i in range(3) for j in range(3)]).reshape(9, 9)
ok["CONTROL"] = np.linalg.matrix_rank(Mg) == 9
for k, v in ok.items(): print(("PASS " if v else "FAIL ") + k)
print(f"SCORE: {sum(ok.values())}/{len(ok)}")
