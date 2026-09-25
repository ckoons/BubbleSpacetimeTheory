#!/usr/bin/env python3
"""Keeper K1926 -- Casey's 'the record keeps the measurement; the potential values are forgotten', as linear algebra on V1 = C^3.

Record of a write-state v in V1 = its measurement record, the density matrix rho = v v^dagger / |v|^2 (phase forgotten).
  R1  q(v,v) = v^T v is NOT a function of rho: v and e^{i theta} v give the same rho and different q  (the record loses q)
  R2  the magnitude |q|^2 = tr(rho rho^T) IS a function of rho (it survives unless the record also forgets V1's real structure)
  R3  the Lie algebra acting faithfully on records (rho -> [X, rho], X in u(3)) has dim 8 = su(3) (the u(1) acts trivially)
  R4  requiring it to preserve tr(rho rho^T) for all rho cuts it to dim 3 = so(3)  -> SU(3) iff the record forgets the real structure
  R5  the geometry's own triple algebra on V1 (K1925) acting on records: so(3)+u(1) -> faithful dim 3 (so(3)); the u(1) is invisible on records
  CONTROL: a random fixed rho0 as extra structure cuts su(3) below 8
"""
import numpy as np, itertools
rng = np.random.default_rng(7)
def rho_of(v): v = v / np.linalg.norm(v); return np.outer(v, v.conj())
def rand_v(): return rng.normal(size=3) + 1j * rng.normal(size=3)
ok = {}
v = rand_v(); th = 0.7
r1, r2 = rho_of(v), rho_of(np.exp(1j * th) * v)
q1, q2 = (v @ v) / np.vdot(v, v), (np.exp(2j * th) * (v @ v)) / np.vdot(v, v)
ok["R1"] = np.allclose(r1, r2) and not np.isclose(q1, q2)
ok["R2"] = np.isclose(abs(q1) ** 2, np.trace(r1 @ r1.T).real)
print(f"R1 same rho: {np.allclose(r1, r2)}, q differs: {not np.isclose(q1, q2)}   R2 |q|^2 = tr(rho rho^T): {ok['R2']}")

# u(3) basis (anti-Hermitian), 9 real generators
B = []
for i in range(3):
    M = np.zeros((3, 3), complex); M[i, i] = 1j; B.append(M)
for i, j in itertools.combinations(range(3), 2):
    M = np.zeros((3, 3), complex); M[i, j] = 1; M[j, i] = -1; B.append(M)
    M = np.zeros((3, 3), complex); M[i, j] = 1j; M[j, i] = 1j; B.append(M)
samples = [rho_of(rand_v()) for _ in range(12)]
def flat(M): return np.concatenate([M.real.ravel(), M.imag.ravel()])
def faithful_dim(gens, extra=None):
    # kernel of X -> ([X,rho] for all samples); plus optional extra linear constraints; returns rank of the action map
    rows = []
    for X in gens:
        col = [flat(X @ r - r @ X) for r in samples]
        if extra is not None: col.append(np.array([extra(X, r) for r in samples]))
        rows.append(np.concatenate(col))
    A = np.array(rows).T
    return np.linalg.matrix_rank(A, tol=1e-9)
d_all = faithful_dim(B)
ok["R3"] = d_all == 8
# preserving f(rho) = tr(rho rho^T): d/dt f = tr([X,rho] rho^T + rho [X,rho]^T) = 2 tr([X,rho] rho^T)
def keeps_f(X, r): return (2 * np.trace((X @ r - r @ X) @ r.T)).real, (2 * np.trace((X @ r - r @ X) @ r.T)).imag
# solve: generators whose action preserves f on all samples, then faithful dim of that subalgebra
C = np.array([[c for r in samples for c in keeps_f(X, r)] for X in B]).T
_, s, Vt = np.linalg.svd(C); null = Vt[(s > 1e-9).sum():] if (s > 1e-9).sum() < len(B) else np.zeros((0, len(B)))
sub = [sum(c * X for c, X in zip(vec, B)) for vec in null]
d_sub = faithful_dim(sub) if sub else 0
ok["R4"] = d_sub == 3
print(f"R3 faithful algebra on records: dim {d_all} (su(3)=8)   R4 also keeping tr(rho rho^T): dim {d_sub} (so(3)=3)")
# R5: K1925's so(3)+u(1) on V1 acting on records
so3 = [B[3], B[5], B[7]]           # real antisymmetric generators E_ij - E_ji
u1 = [1j * np.eye(3)]
d5 = faithful_dim(so3 + u1)
ok["R5"] = d5 == 3
print(f"R5 geometry's so(3)+u(1) acting on records: faithful dim {d5} (the u(1) is invisible)")
rho0 = rho_of(rand_v())
def keeps_rho0(X, r): return np.linalg.norm(X @ rho0 - rho0 @ X)
C2 = np.array([flat(X @ rho0 - rho0 @ X) for X in B]).T
_, s2, Vt2 = np.linalg.svd(C2); k = (s2 > 1e-9).sum(); sub2 = [sum(c * X for c, X in zip(vec, B)) for vec in Vt2[k:]]
ok["CONTROL"] = faithful_dim(sub2) < 8
print(f"CONTROL fixing a generic rho0 leaves faithful dim {faithful_dim(sub2)} < 8")
for kk, vv in ok.items(): print(("PASS " if vv else "FAIL ") + kk)
print(f"SCORE: {sum(ok.values())}/{len(ok)}")
