#!/usr/bin/env python3
"""R13 instrument: test Harris Thm 1.1's condition on nilpotent orbits of su(2,2).

Harris (arXiv:1209.4123) Thm 1.1: if O occurs in WF(pi) for tempered pi, nu in O,
L = Levi factor of Z_G(nu), then L/Z(G) is compact.
For a nilpotent X with sl2-triple (X,H,Y), the Levi factor of Z_g(X) is z_g(X,H,Y)
(standard; PIN OWED: Collingwood-McGovern Lemma 3.7.3 / Barbasch-Vogan).
su(2,2) = {A in gl(4,C): A^* J + J A = 0, tr A = 0}, J = diag(1,1,-1,-1).
Compactness test: l = z(X,H,Y) is compact iff the Killing-proportional form tr(AB)
is negative definite on l (su(2,2) is semisimple, Z(G) finite).
Cases:
  min_plus / min_minus : X = +/- i v v^* J with v null  -> Jordan type [2,1,1] (minimal)
  hol22               : X = i(v1 v1^* + v2 v2^*)J, isotropic plane -> [2,2], rows same sign
  mixed22             : X = i(v1 v1^* - v2 v2^*)J              -> [2,2], rows opposite sign
Expected (Harris Example 5.1 rule): min_* noncompact; hol22 compact; mixed22 noncompact.
"""
import numpy as np
J = np.diag([1, 1, -1, -1]).astype(complex)

def basis_su22():
    # real basis of su(2,2): A = i*J*S with S Hermitian (then A^*J + JA = 0), trace zero
    B = []
    for a in range(4):
        for b in range(a, 4):
            for part in ([1] if a == b else [1, 1j]):
                S = np.zeros((4, 4), complex)
                S[a, b] = part; S[b, a] = np.conj(part)
                B.append(1j * J @ S)
    # impose trace zero: project
    M = np.array([[np.trace(A).real, np.trace(A).imag] for A in B])
    # null space of trace map
    _, s, vt = np.linalg.svd(M.T)
    ns = vt[np.sum(s > 1e-12):]
    return [sum(c * A for c, A in zip(row, B)) for row in ns]

BAS = basis_su22()  # 15 elements
def vec(A): return np.concatenate([A.real.ravel(), A.imag.ravel()])
BM = np.array([vec(A) for A in BAS]).T  # 32 x 15
def coords(A):
    c, *_ = np.linalg.lstsq(BM, vec(A), rcond=None); return c
def ad_matrix(X):
    return np.array([coords(X @ A - A @ X) for A in BAS]).T  # 15x15

def check_su22(X):
    assert np.allclose(X.conj().T @ J + J @ X, 0) and abs(np.trace(X)) < 1e-12

def sl2_triple(X):
    # find H in [X, g] with [H,X]=2X, then Y with [X,Y]=H, [H,Y]=-2Y (Jacobson-Morozov, numeric)
    adX = ad_matrix(X); x = coords(X)
    # solve [X, Z] = -2X ... H = [X, Z0] with [H,X]=2X; direct least squares over H:
    # unknown h (15): [H,X] = -adX h = 2x
    h, *_ = np.linalg.lstsq(-adX, 2 * x, rcond=None)
    # refine: need H = [X,Y] and [H,Y] = -2Y: solve for Y linear: adX y = h, and ad_H y = -2y
    adH = sum(c * ad for c, ad in zip(h, [ad_matrix(A) for A in BAS]))
    Mstack = np.vstack([adX, adH + 2 * np.eye(15)])
    rhs = np.concatenate([h, np.zeros(15)])
    y, res, *_ = np.linalg.lstsq(Mstack, rhs, rcond=None)
    ok = np.allclose(Mstack @ y, rhs, atol=1e-9)
    if not ok:  # adjust H within solution space: H must lie in image of adX; iterate
        # general: choose H = [X, Y0] where Y0 solves [H,X]=2X with H=[X,Y0] -> adX^2 y0 = -2x
        y0, *_ = np.linalg.lstsq(adX @ adX, -2 * x, rcond=None)
        h = adX @ y0
        adH = sum(c * ad for c, ad in zip(h, [ad_matrix(A) for A in BAS]))
        Mstack = np.vstack([adX, adH + 2 * np.eye(15)])
        rhs = np.concatenate([h, np.zeros(15)])
        y, *_ = np.linalg.lstsq(Mstack, rhs, rcond=None)
        ok = np.allclose(Mstack @ y, rhs, atol=1e-8)
    return h, y, ok

def levi_signature(X):
    h, y, ok = sl2_triple(X)
    H = sum(c * A for c, A in zip(h, BAS)); Y = sum(c * A for c, A in zip(y, BAS))
    assert ok, "sl2 triple not found"
    assert np.allclose(H @ X - X @ H, 2 * X, atol=1e-8)
    assert np.allclose(X @ Y - Y @ X, H, atol=1e-8)
    assert np.allclose(H @ Y - Y @ H, -2 * Y, atol=1e-8)
    M = np.vstack([ad_matrix(X), ad_matrix(H), ad_matrix(Y)])
    _, s, vt = np.linalg.svd(M)
    null = vt[np.sum(s > 1e-9):]            # basis of l = z(X,H,Y)
    L = [sum(c * A for c, A in zip(row, BAS)) for row in null]
    G = np.array([[np.trace(A @ B).real for B in L] for A in L])
    ev = np.linalg.eigvalsh(G) if len(L) else np.array([])
    npos = int(np.sum(ev > 1e-9)); nneg = int(np.sum(ev < -1e-9)); nz = len(ev) - npos - nneg
    jordan = [int(np.linalg.matrix_rank(np.linalg.matrix_power(X, k), tol=1e-9)) for k in (1, 2)]
    return len(L), npos, nneg, nz, jordan

v = np.array([1, 0, 1, 0], complex)          # null: |v1|^2 - |v3|^2 = 0
v1 = np.array([1, 0, 1, 0], complex); v2 = np.array([0, 1, 0, 1], complex)
cases = {
    "min_plus":  1j * np.outer(v, v.conj()) @ J,
    "min_minus": -1j * np.outer(v, v.conj()) @ J,
    "hol22":     1j * (np.outer(v1, v1.conj()) + np.outer(v2, v2.conj())) @ J,
    "mixed22":   1j * (np.outer(v1, v1.conj()) - np.outer(v2, v2.conj())) @ J,
}
print("dim su(2,2) basis =", len(BAS))
for name, X in cases.items():
    check_su22(X)
    dimL, npos, nneg, nz, (r1, r2) = levi_signature(X)
    compact = (npos == 0 and nz == 0)
    print(f"{name:10s} rank X={r1} rank X^2={r2}  dim l={dimL}  tr(AB) signature (+{npos},-{nneg},0:{nz})  l compact: {compact}")
