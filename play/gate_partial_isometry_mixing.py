import numpy as np, math
from math import factorial as fact
KMAX = 120

def poch(v, k):
    r = 1.0
    for i in range(k):
        r *= (v + i)
    return r

def Aeven(r, nu, kmax=KMAX):
    ms = [m for m in range(0, kmax + 1, 2)]
    w = np.array([math.sqrt(poch(nu, m) / fact(m)) * r ** m for m in ms])
    w /= np.linalg.norm(w)
    return ms, w

def r_mode(s, nu):
    return ((s + 1) * (s + 2) / ((nu + s) * (nu + s + 1))) ** 0.25

# THE STRUCTURAL GATE
# CKM unitarity (a THEOREM of 3-generation quark field redefinition -- and BST derives
# 3 generations from the Q^5 truncation, so this is in-corpus, not a fitted number):
#   V = A^dag J B unitary, with A,B orthonormal bases of the up 3-space U and down 3-space D
#   <=>  J restricted to D is an ISOMETRY onto U  <=>  all 3 singular values of P_U J|_D equal.
# So: compute sing. values of P_U J|_D.  If they are not all equal, the one-insertion
# ansatz CANNOT be unitary, and any SVD/polar "unitarization" is a falsification patch,
# not a convention.

print("STRUCTURAL GATE: is J_W a partial isometry from the down 3-space onto the up 3-space?")
print("  (CKM unitarity requires all three singular values of P_U J|_D to be EQUAL.)\n")
print(f"{'nu':>7}{'s1':>10}{'s2':>10}{'s3':>10}{'s1/s3':>10}   verdict")

for nu in (3.0, 5.0, 10.0, 30.0):
    N = KMAX // 2 + 1
    idx = {m: i for i, m in enumerate(range(0, KMAX + 1, 2))}
    # full even+odd index space
    dim = KMAX + 1
    # down basis: f_k, k=1,3,5 (unit vectors in the k-grid)
    D = np.zeros((dim, 3))
    for j, k in enumerate([1, 3, 5]):
        D[k, j] = 1.0
    # up basis: parity-even coherent states at the mode-forced radii, orthonormalized (QR)
    U = np.zeros((dim, 3))
    for i, s in enumerate([0, 2, 4]):
        ms, w = Aeven(r_mode(s, nu), nu)
        for m, c in zip(ms, w):
            U[m, i] = c
    Uq, _ = np.linalg.qr(U)          # orthonormal basis of the SAME 3-space U
    # J = M + M^dag in the nu-orthonormal basis
    J = np.zeros((dim, dim))
    for k in range(dim - 1):
        c = math.sqrt((k + 1) / (nu + k))
        J[k + 1, k] += c             # M
        J[k, k + 1] += c             # M^dag
    Vfull = Uq.T @ J @ D             # P_U J|_D expressed in orthonormal bases
    sv = np.linalg.svd(Vfull, compute_uv=False)
    ratio = sv[0] / sv[2]
    verdict = "ISOMETRY" if ratio < 1.01 else "NOT an isometry -> unitary CKM UNREACHABLE"
    print(f"{nu:>7.1f}{sv[0]:>10.4f}{sv[1]:>10.4f}{sv[2]:>10.4f}{ratio:>10.2f}   {verdict}")

print("\nControl: a genuine partial isometry must give ratio = 1.00 exactly.")
Q, _ = np.linalg.qr(np.random.default_rng(0).normal(size=(20, 3)))
R, _ = np.linalg.qr(np.random.default_rng(1).normal(size=(20, 3)))
Jiso = Q @ R.T                       # by construction an isometry R-space -> Q-space
sv = np.linalg.svd(Q.T @ Jiso @ R, compute_uv=False)
print(f"  constructed isometry singular values: {sv.round(6)}  ratio = {sv[0]/sv[2]:.6f}  <- positive control")
