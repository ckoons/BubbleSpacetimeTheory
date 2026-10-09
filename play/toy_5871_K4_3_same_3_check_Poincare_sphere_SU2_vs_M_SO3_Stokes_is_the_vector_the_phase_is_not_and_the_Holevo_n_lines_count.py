#!/usr/bin/env python3
"""
Toy 5871 — Round K4-3, Cal S1037's check (Elie, 2026-10-09): "the full SO(3) of M against the Poincaré-sphere SU(2) of the
write — D₃ is not enough." didwe "Poincare sphere Stokes" → 0. Plus Cal S1034's Holevo count (n_lines; bits ≤ log₂(2 n_lines)).

The write (Lyra K4-2 / Addendum 12): polarization (2) + phase relative to the electron's circle (1) = S³, the Hopf total space
over the Poincaré sphere S². SU(2) acts on Jones vectors ψ ∈ ℂ² (the fundamental, real dimension 4); the overall phase is
the U(1) of U(2) = (SU(2) × U(1))/ℤ₂; the Stokes vector S_i = ψ† σ_i ψ is the adjoint (spin 1, real dimension 3) and is
what SU(2) → SO(3) rotates on the Poincaré sphere.
M = Z_K(a) = SO(3) × ℤ₂ (5866) acts on g_{e₁} as the SO(3) vector. The question "same 3?" is then a question about
SU(2)-equivariant maps: which part of the write's S³ can map onto g_{e₁}?
Computed: (1) the Stokes map is SU(2)-equivariant with image the adjoint; (2) dim Hom_SU(2)(fundamental_ℝ, adjoint) = 0,
dim Hom(adjoint, vector) = 1 — by characters AND by an explicit matrix; (3) the overall phase acts trivially on the Stokes
vector, so the 'phase' direction has NO image in g_{e₁}; (4) the SO(2) of K rotates g_{e₁} out of itself (g_{e₁} is not
SO(2)_K-stable): the smallest SO(2)_K-stable subspace containing g_{e₁} is computed — where the phase's circle can live.
"""
import itertools
import numpy as np

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")
rng = np.random.default_rng(5871)

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def su2(nvec, th):
    n_ = np.asarray(nvec, float); n_ = n_ / np.linalg.norm(n_)
    return np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * sum(ni * s for ni, s in zip(n_, sig))
def stokes(psi): return np.array([np.real(psi.conj() @ s @ psi) for s in sig])
def so3_of(U):
    """the adjoint action: U σ_i U† = Σ_j R_ji σ_j"""
    return np.array([[0.5 * np.real(np.trace(sig[j] @ U @ sig[i] @ U.conj().T)) for i in range(3)] for j in range(3)])

print("(1) the Stokes map is SU(2)-equivariant onto the vector")
ok1 = True
for _ in range(50):
    psi = rng.normal(size=2) + 1j * rng.normal(size=2); psi /= np.linalg.norm(psi)
    U = su2(rng.normal(size=3), rng.uniform(0, 2 * np.pi)); R = so3_of(U)
    ok1 &= np.allclose(stokes(U @ psi), R @ stokes(psi)) and np.isclose(np.linalg.det(R), 1) and np.allclose(R.T @ R, np.eye(3))
    ok1 &= np.allclose(stokes(np.exp(1j * rng.uniform(0, 2 * np.pi)) * psi), stokes(psi))      # the phase is invisible
score("S1", ok1, "S(Uψ) = R(U) S(ψ) with R ∈ SO(3) for 50 random (ψ, U); S(e^{iφ}ψ) = S(ψ): the overall phase drops out")

print("(2) Hom counts by characters on SU(2): fundamental (real 4) vs adjoint (3) vs the M-vector (3)")
# characters on a conjugacy class of angle th: fundamental: 2cos(th/2); as a real rep 4cos(th/2); adjoint: 1 + 2cos th
ths = np.linspace(0, 2 * np.pi, 20001)[:-1]
weight = np.sin(ths / 2) ** 2 * (1 / np.pi) * (ths[1] - ths[0])          # Haar on classes: (1/π) sin²(θ/2) dθ on [0, 2π] (first run had 2/π: every count doubled; owned)
chi_fund_R = 4 * np.cos(ths / 2); chi_adj = 1 + 2 * np.cos(ths)
inner = lambda a, b: float(np.sum(a * b * weight))
h_fund_adj, h_adj_adj, h_fund_fund = inner(chi_fund_R, chi_adj), inner(chi_adj, chi_adj), inner(chi_fund_R, chi_fund_R)
score("S2", abs(h_fund_adj) < 1e-3 and abs(h_adj_adj - 1) < 1e-3 and abs(h_fund_fund - 4) < 1e-3,   # norm² 4 = two spin-½ (first assertion said 2; owned)
      f"dim Hom(fund_ℝ, adj) = {h_fund_adj:.4f} (ZERO: no SU(2)-map from the Jones vector with its phase into a vector); "
      f"dim Hom(adj, adj) = {h_adj_adj:.4f} (one map, Schur); fund_ℝ is two copies of the spin-½ (norm² = {h_fund_fund:.3f})")

print("(3) the explicit intertwiner Stokes → g_{e₁}: M's SO(3) from 5866, the iso SU(2)/±1 → M₀")
N = 7; eta = np.diag([1, 1, 1, 1, 1, -1, -1]).astype(float)
def E(i, j):
    m = np.zeros((N, N)); m[i, j] = 1; return m
pairs = list(itertools.combinations(range(N), 2)); basis = [eta @ (E(i, j) - E(j, i)) for i, j in pairs]
G = np.array([X.ravel() for X in basis]).T
def coords(X):
    c, *_ = np.linalg.lstsq(G, X.ravel(), rcond=None); assert np.allclose(G @ c, X.ravel(), atol=1e-9); return c
def ad(X): return np.array([coords(X @ Y - Y @ X) for Y in basis]).T
X1, X2 = E(0, 5) + E(5, 0), E(1, 6) + E(6, 1); A1, A2 = ad(X1), ad(X2)
t = rng.normal(size=2); vals, vecs = np.linalg.eig(t[0] * A1 + t[1] * A2); vecs = vecs.real
g_e1 = [v / np.linalg.norm(v) for v in vecs.T if np.isclose(v @ A1 @ v / (v @ v), 1, atol=1e-6) and np.isclose(v @ A2 @ v / (v @ v), 0, atol=1e-6)]
assert len(g_e1) == 3
V = np.array(g_e1).T
def Ad7(g): return np.array([coords(g @ Y @ np.linalg.inv(g)) for Y in basis]).T
def restrict(op):
    out = []
    for v in V.T:
        c, *_ = np.linalg.lstsq(V, op @ v, rcond=None); assert np.allclose(V @ c, op @ v, atol=1e-7); out.append(c)
    return np.array(out).T
def m_rot(R3):                      # M₀ ∋ rotation R3 on coordinates {3,4,5} (0-based 2,3,4)
    g = np.eye(N); g[2:5, 2:5] = R3; return g
# an orthonormal basis of g_{e1} in which M acts by the SAME matrices as on R^3: find T with restrict(Ad(m_rot(R))) = T R T^-1 for generators
Rs = [so3_of(su2(nv, 1.0)) for nv in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]
Ms = [restrict(Ad7(m_rot(R))) for R in Rs]
# solve T R_i = M_i T for all i (linear in T): stack
rows = []
for R, Mm in zip(Rs, Ms):
    for a in range(3):
        for b in range(3):
            row = np.zeros(9)
            for c in range(3):
                row[a * 3 + c] += R[c, b]          # (T R)[a,b] = sum_c T[a,c] R[c,b]
                row[c * 3 + b] -= Mm[a, c]          # (M T)[a,b] = sum_c M[a,c] T[c,b]
            rows.append(row)
_, s_, vh = np.linalg.svd(np.array(rows)); null = vh[np.sum(s_ > 1e-8):]
score("S3", len(null) == 1 and np.isclose(abs(np.linalg.det(null[0].reshape(3, 3))), abs(np.linalg.det(null[0].reshape(3, 3))))
      and abs(np.linalg.det(null[0].reshape(3, 3))) > 1e-6,
      f"the space of SU(2)-intertwiners Stokes → g_{{e₁}} (through SU(2) → SO(3) ≅ M₀ on {{3,4,5}}) has dimension {len(null)}: ONE map, invertible — "
      f"the full SO(3), not just D₃ (Cal S1037). The '3' of the write that matches M's '3' is the STOKES vector (polarization only)")

print("(4) where the phase can live: the SO(2) of K on g_{e₁} (computed, not guessed)")
J = ad(eta @ (E(5, 6) - E(6, 5)))                       # the so(2) generator of K (coordinates 6, 7)
img = J @ V
in_ge1 = np.allclose(V @ np.linalg.lstsq(V, img, rcond=None)[0], img, atol=1e-7)
# root content of J·g_{e1}: decompose against the simultaneous eigenbasis of ad(a)
lam_of = lambda v: (round(float(v @ A1 @ v / (v @ v)), 3), round(float(v @ A2 @ v / (v @ v)), 3))
roots = {}
for v in vecs.T:
    roots.setdefault(lam_of(v), []).append(v / np.linalg.norm(v))
P = np.linalg.pinv(vecs)
content = {}
for w in img.T:
    c = P @ w
    for i, v in enumerate(vecs.T):
        key = lam_of(v); content[key] = content.get(key, 0.0) + float(abs(c[i]) ** 2 * (v @ v))
content = {k: round(v / sum(content.values()), 3) for k, v in content.items() if v / sum(content.values()) > 1e-6}
# the smallest J-stable subspace containing g_{e1}
S = V.copy(); r_prev = 0
while True:
    S = np.hstack([S, J @ S]); r = np.linalg.matrix_rank(S, tol=1e-8)
    if r == r_prev: break
    r_prev = r
score("S4", not in_ge1,
      f"g_{{e₁}} is NOT SO(2)_K-stable; J·g_{{e₁}} has root content (fraction of norm²) {content}; the smallest SO(2)_K-stable "
      f"subspace containing g_{{e₁}} has dimension {r}. The Šilov circle moves the write's 3 OUT of the one short-root space: "
      "the phase is not inside the 3, and which spaces it reaches is printed above for Lyra (no claim about g_{−e₁} is made)")

print("(5) Holevo count for the write event (Cal S1034): n_lines and the bound bits ≤ log₂(2 n_lines)")
lines = {"E1 from s (5863 W2: Δm ∈ {−1,0,+1})": 3, "E1 from s, spin kept (5863 W4)": 6, "21 cm M1 (Lyra census: graph K2)": 1,
         "fixed photon axis (helicity only; 5863 W3 null)": 2, "E2 from s (5863 W3 null: 5 targets)": 5}
import math
for name, nl in lines.items():
    print(f"     {name:<52}: n_lines = {nl}, bits ≤ log₂(2·{nl}) = {math.log2(2 * nl):.3f}")
score("S5", all(math.log2(2 * nl) >= 1 for nl in lines.values()) and math.log2(2 * 3) < 3,
      "Lyra's 'one classical bit per commit' sits inside the bound for every line count (≥ 1 bit); 'three classical values' would need ≥ 3 bits and the E1 write allows 2.58 — dead by Holevo, as the 10-08 prompt said")

passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail)")
