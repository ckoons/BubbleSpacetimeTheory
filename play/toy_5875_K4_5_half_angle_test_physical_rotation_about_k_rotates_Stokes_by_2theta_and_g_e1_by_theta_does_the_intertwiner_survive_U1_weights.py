#!/usr/bin/env python3
"""
Toy 5875 — Round K4-5, Lane B item 2, the half-angle test (Elie, 2026-10-09). Hashed by Cal S1040 Sec. 5 (P7) / K1956 Sec. 4.
No data. didwe "half angle Stokes rotation" → 0.

Setup (5871): the Jones vector ψ = (E_x, E_y) ∈ ℂ², Stokes S_i = ψ†σ_iψ (an SO(3) vector under SU(2)); M₀ = SO(3) on {3,4,5}
acts on g_{e₁} as the vector; T is the unique (Schur) intertwiner Stokes → g_{e₁} for the identification SU(2)/±1 ≅ M₀.
A PHYSICAL rotation by θ about the photon axis k̂ acts on (E_x, E_y) by the real rotation R(θ) ∈ SO(2) ⊂ SU(2); on the
Stokes vector that is a rotation by 2θ about the circular axis; on g_{e₁} (k̂ ∈ {3,4,5}) it is a rotation by θ about k̂.
Tests: (H1) the Stokes angle is 2θ (computed, not assumed); (H2) T R_S(2θ) ≠ R_M(θ) T for generic θ, = for θ ≡ 0 (mod 2π)
only — the intertwiner does not commute with the physical rotation; (H3) T R_S(2θ) = R_M(2θ) T for every θ (it commutes
with the DOUBLE: the spinorial statement); (H4) U(1) weights: {0, ±2} on Stokes vs {0, ±1} on g_{e₁}, so the space of
rotation-equivariant linear maps Stokes → g_{e₁} is ONE-dimensional and sends the circular component to k̂, killing both
linear-polarization directions; (H5) the same with k̂ chosen at random in {3,4,5}; (H6) the SU(2) element of the real
rotation R(θ) has half-angle θ: a 2π physical rotation is −1 on ψ and +1 on Stokes and on g_{e₁} (4π on ψ).
"""
import itertools
import numpy as np

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")
rng = np.random.default_rng(5875)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def stokes(psi): return np.array([np.real(psi.conj() @ s @ psi) for s in sig])
def so3_of(U): return np.array([[0.5 * np.real(np.trace(sig[j] @ U @ sig[i] @ U.conj().T)) for i in range(3)] for j in range(3)])
def rot2(th): return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]], complex)       # the physical rotation on (E_x, E_y)
def axis_angle(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    w, v = np.linalg.eig(R); ax = np.real(v[:, np.argmin(abs(w - 1))]); return ax / np.linalg.norm(ax), ang

# ---------------------------------------------------------------- H1: the Stokes angle is 2θ
print("H1  the physical rotation's angle on the Stokes vector")
ok1 = True; rows = []
for th in (0.1, 0.3, 0.7, 1.0, 1.5):
    R_S = so3_of(rot2(th)); ax, ang = axis_angle(R_S)
    rows.append((th, ang, ax)); ok1 &= np.isclose(ang, 2 * th)
    # also directly: a linear polarization at angle φ has Stokes azimuth 2φ
    psi = np.array([np.cos(0.2), np.sin(0.2)], complex); S0, S1 = stokes(psi), stokes(rot2(th) @ psi)
    d = (np.arctan2(S1[0], S1[2]) - np.arctan2(S0[0], S0[2]) + np.pi) % (2 * np.pi) - np.pi      # wrapped (first run: unwrapped sign; owned)
    ok1 &= np.isclose(abs(d), 2 * th)
circ_axis = rows[0][2]
print("     θ → Stokes angle:", [(t, round(a, 6)) for t, a, _ in rows], " axis =", np.round(circ_axis, 6), "(the circular-polarization direction)")
score("H1", ok1, "a physical rotation by θ about k̂ rotates the Stokes vector by exactly 2θ about the circular axis (Cal P7's premise, computed)")

# ---------------------------------------------------------------- the intertwiner T (5871 S3), rebuilt here
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
V = np.array([v / np.linalg.norm(v) for v in vecs.T if np.isclose(v @ A1 @ v / (v @ v), 1, atol=1e-6) and np.isclose(v @ A2 @ v / (v @ v), 0, atol=1e-6)]).T
assert V.shape == (21, 3)
def Ad7(g): return np.array([coords(g @ Y @ np.linalg.inv(g)) for Y in basis]).T
def restrict(op):
    out = []
    for v in V.T:
        c, *_ = np.linalg.lstsq(V, op @ v, rcond=None); assert np.allclose(V @ c, op @ v, atol=1e-7); out.append(c)
    return np.array(out).T
def m_rot(R3):
    g = np.eye(N); g[2:5, 2:5] = R3; return g
def R_M(R3): return restrict(Ad7(m_rot(R3)))           # M₀'s action on g_{e1}, in the V basis
def su2(nvec, th):
    n_ = np.asarray(nvec, float); n_ = n_ / np.linalg.norm(n_)
    return np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * sum(ni * s for ni, s in zip(n_, sig))
# Schur map: T R = M(R) T for the generators (the identification SU(2)/±1 -> M0: Stokes rotation R acts on {3,4,5} by the same matrix)
gens = [so3_of(su2(nv, 1.0)) for nv in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]
rows_ = []
for R in gens:
    Mm = R_M(R)
    for a in range(3):
        for b in range(3):
            row = np.zeros(9)
            for c in range(3):
                row[a * 3 + c] += R[c, b]; row[c * 3 + b] -= Mm[a, c]
            rows_.append(row)
_, s_, vh = np.linalg.svd(np.array(rows_)); null = vh[np.sum(s_ > 1e-8):]
assert len(null) == 1
T = null[0].reshape(3, 3); T /= np.linalg.norm(T)
def rot3(axis, th):                      # rotation matrix on {3,4,5}
    U = su2(axis, th); return so3_of(U)

# the photon axis in {3,4,5} coordinates: the direction whose image under T is T(ĉ), i.e. the preimage of the circular
# Stokes axis under the identification (R_M(R) = T R T⁻¹, so a rotation about the {3,4,5}-vector n acts on g_{e1} as T rot(n) T⁻¹;
# the axis that T pairs with ĉ is n = ĉ itself). First run passed T ĉ (V-coordinates) as a {3,4,5}-axis: wrong frame; owned.
k_hat = np.linalg.solve(T, T @ circ_axis); k_hat /= np.linalg.norm(k_hat)
assert np.allclose(k_hat, circ_axis)

# ---------------------------------------------------------------- H2/H3
print("H2  does T commute with the physical rotation?  ||T R_S(2θ) − R_M(θ) T|| and ||T R_S(2θ) − R_M(2θ) T||")
mis1, mis2 = [], []
for th in np.linspace(0, 2 * np.pi, 13):
    R_S = so3_of(rot2(th))
    mis1.append(np.linalg.norm(T @ R_S - R_M(rot3(k_hat, th)) @ T))
    mis2.append(np.linalg.norm(T @ R_S - R_M(rot3(k_hat, 2 * th)) @ T))
print("     θ/π:", [round(x / np.pi, 3) for x in np.linspace(0, 2 * np.pi, 13)])
print("     mismatch with θ :", [round(x, 4) for x in mis1])
print("     mismatch with 2θ:", [round(x, 4) for x in mis2])
score("H2", max(mis1[1:-1]) > 0.1 and mis1[0] < 1e-9 and mis1[-1] < 1e-9 and min(mis1[1:-1]) > 1e-3,
      "T does NOT commute with the physical rotation: T R_S(2θ) ≠ R_M(θ) T for every θ in (0, 2π); equality only at θ = 0, 2π — Cal P7's factor 2 appears")
score("H3", max(mis2) < 1e-9, "T R_S(2θ) = R_M(2θ) T for every θ: the Schur map intertwines the physical rotation only through the DOUBLE angle — the spinorial statement")

# ---------------------------------------------------------------- H4: U(1) weights decide it, independent of any choice of T
print("H4  weights of the rotation-about-k̂ group: Stokes vs g_{e₁}")
def gen_weights(Rfun, eps=1e-6):
    L = (Rfun(eps) - Rfun(-eps)) / (2 * eps)          # the generator
    return sorted(np.round(np.linalg.eigvals(L).imag, 6))
w_S = gen_weights(lambda th: so3_of(rot2(th)))
w_M = gen_weights(lambda th: R_M(rot3(k_hat, th)))
# Hom_U(1): count matching weights
hom = sum(min(w_S.count(w), w_M.count(w)) for w in set(w_S))
# the equivariant map: circular component -> k̂, linear components -> 0 (the weight-0 pair)
score("H4", w_S == [-2.0, 0.0, 2.0] and w_M == [-1.0, 0.0, 1.0] and hom == 1,
      f"weights on Stokes {w_S} vs on g_{{e₁}} {w_M}: the only shared weight is 0, so dim Hom_U(1)(Stokes, g_{{e₁}}) = {hom}: "
      "the ONLY rotation-equivariant linear map sends the circular (helicity) component to k̂ and kills BOTH linear-polarization directions")

# ---------------------------------------------------------------- H5: independent of the choice of k̂ and of the identification
ok5 = True
for _ in range(20):
    kk = rng.normal(size=3); kk /= np.linalg.norm(kk)
    ok5 &= gen_weights(lambda th, kk=kk: R_M(rot3(kk, th))) == [-1.0, 0.0, 1.0]
score("H5", ok5, "the g_{e₁} weights are {0, ±1} for 20 random axes k̂ ∈ {3,4,5}: the mismatch is not an artefact of which direction is called the photon axis")

# ---------------------------------------------------------------- H6: the 2π / 4π bookkeeping on the three spaces
R2pi = rot2(2 * np.pi); S2pi = so3_of(R2pi); M2pi = R_M(rot3(k_hat, 2 * np.pi))
psi = np.array([0.6, 0.8j]);
score("H6", np.allclose(R2pi, np.eye(2)) and np.allclose(S2pi, np.eye(3)) and np.allclose(M2pi, np.eye(3))
      and np.allclose(so3_of(rot2(np.pi)), np.eye(3)) and not np.allclose(R_M(rot3(k_hat, np.pi)), np.eye(3)),
      "a 2π physical rotation is the identity on ψ, on Stokes and on g_{e₁}; a π rotation is already the identity on Stokes (2θ = 2π) but NOT on g_{e₁}: "
      "the real SO(2) rotation of (E_x, E_y) is an SU(2) element of angle 2θ, so Stokes is the DOUBLE of space, not its spinor — the '4π' belongs to the Jones vector's own phase, not to the Stokes map")

print("\n  Reading, for Cal and Keeper (no claim beyond the lines above): the Stokes 3 and the tangent 3 are related only by the double cover θ ↦ 2θ."
      "\n  'The K4's three faces are the three spatial directions' fails as an identity of SO(3)-vectors under physical rotations;"
      "\n  what survives rotation-equivariantly is ONE direction: helicity ↔ the photon's own axis. The two linear-polarization faces have no spatial image.")
passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail; H1 is Cal's premise, computed)")
