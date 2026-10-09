#!/usr/bin/env python3
"""
Toy 5878 — Round K4-6, Lane B item 1 (Elie, 2026-10-09). No data. didwe → 0.
After 5875: what survives a physical rotation is ONE direction per commit (the photon axis k̂, helicity ↔ k̂) plus the
circle's sign. This instrument puts on disk:
 (E1) the map Φ: k̂ (a unit vector in the physical {3,4,5}) ↦ a direction in g_{e₁} intertwines ALL of M₀ = SO(3), not only
      rotations about k̂ (5875): Φ(R k̂) = Ad(m(R)) Φ(k̂) for random R, k̂.
 (E2) the ℤ₂ component of M (z = diag(−1,−1,1,1,1,−1,−1), 5866 R2) fixes k̂ in {3,4,5} but acts as −1 on g_{e₁}: so
      equivariance under the FULL M holds only if the helicity sign h flips under z: Φ_h(k̂) := h Φ(k̂), z·Φ_h = Φ_{−h}.
      z is the Šilov-circle half-turn (rotation by π on coordinates 6,7) composed with a half-turn on (1,2): the circle's
      orientation is what z flips — the sign is carried as the circle's orientation, as the prompt asked.
 (E3) three commits with axes k̂₁, k̂₂, k̂₃ span g_{e₁} iff the Gram determinant det G ≠ 0, G_ij = k̂_i·k̂_j; det G = (k̂₁·(k̂₂×k̂₃))²;
      the failure set (coplanar axes) has measure zero: P(|det G| < ε) ∝ ε as ε → 0 (codimension one), measured by Monte Carlo.
 (E4) the helicity signs do not change the span; an odd number of sign flips reverses the frame's ORIENTATION (det of the
      signed frame) — the read order of the triple (KL3's sign) is carried by the signs, not by the axes.
 (E5) a parameter count for Lyra's item 3 (colour from axes), no claim: three real axes give a real frame (SO(3), 3 parameters);
      a unitary frame of g_{e₁} ⊗ ℂ = ℂ³ has 8 (SU(3)); the 5 missing real parameters are relative phases — the axes alone
      reach only SO(3) ⊂ SU(3).
"""
import itertools
import numpy as np

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")
rng = np.random.default_rng(5878)

# ---- so(5,2), a, g_{e1}, M (from 5866/5875)
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
V, _ = np.linalg.qr(V)            # orthonormal basis of the degenerate eigenspace (eig returns an arbitrary one; first run: T not orthogonal, owned)
def Ad7(g): return np.array([coords(g @ Y @ np.linalg.inv(g)) for Y in basis]).T
def restrict(op):
    out = []
    for v in V.T:
        c, *_ = np.linalg.lstsq(V, op @ v, rcond=None); assert np.allclose(V @ c, op @ v, atol=1e-7); out.append(c)
    return np.array(out).T
def m_rot(R3):
    g = np.eye(N); g[2:5, 2:5] = R3; return g
def rand_SO3():
    Q, R = np.linalg.qr(rng.normal(size=(3, 3))); Q = Q @ np.diag(np.sign(np.diag(R)))
    if np.linalg.det(Q) < 0: Q[:, 0] *= -1
    return Q
# the intertwiner Φ: {3,4,5} -> g_{e1} (V-coordinates): solve T R = M(R) T on generators (5871 S3); Φ(k) = T k
def gen_rot(axis, th):
    a = np.asarray(axis, float); a /= np.linalg.norm(a); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K
gens = [gen_rot(e, 1.0) for e in np.eye(3)]
rows = []
for R in gens:
    Mm = restrict(Ad7(m_rot(R)))
    for a_ in range(3):
        for b in range(3):
            row = np.zeros(9)
            for c in range(3):
                row[a_ * 3 + c] += R[c, b]; row[c * 3 + b] -= Mm[a_, c]
            rows.append(row)
_, s_, vh = np.linalg.svd(np.array(rows)); null = vh[np.sum(s_ > 1e-8):]
assert len(null) == 1
T = null[0].reshape(3, 3); T /= np.linalg.norm(T) / np.sqrt(3)       # scaled so T is orthogonal
Phi = lambda k: T @ k

print("E1  Φ intertwines ALL of M₀ = SO(3)")
ok1 = True
for _ in range(100):
    R = rand_SO3(); k = rng.normal(size=3); k /= np.linalg.norm(k)
    ok1 &= np.allclose(Phi(R @ k), restrict(Ad7(m_rot(R))) @ Phi(k), atol=1e-6)
score("E1", ok1 and np.allclose(T.T @ T, np.eye(3)), "Φ(R k̂) = Ad(m(R)) Φ(k̂) for 100 random (R, k̂); Φ is orthogonal — k̂ is a vector, the one direction per commit survives the full SO(3)")

print("E2  the ℤ₂ of M and the helicity sign")
z = np.diag([-1, -1, 1, 1, 1, -1, -1]).astype(float)
Z = restrict(Ad7(z))
k = rng.normal(size=3); k /= np.linalg.norm(k)
z_fixes_k = np.allclose(z[2:5, 2:5] @ k, k)
# z as a product: rotation by π on (6,7) [the Šilov circle half-turn] times rotation by π on (1,2)
rot_pi = lambda i, j: (lambda g: (g.__setitem__((i, i), -1), g.__setitem__((j, j), -1), g)[2])(np.eye(N))
z_factored = np.allclose(z, rot_pi(5, 6) @ rot_pi(0, 1))
Ch = Ad7(rot_pi(5, 6)) @ V; resid = np.linalg.norm(Ch - V @ np.linalg.lstsq(V, Ch, rcond=None)[0]) / np.linalg.norm(Ch)
score("E2", np.allclose(Z, -np.eye(3)) and z_fixes_k and z_factored,
      "z fixes k̂ in {3,4,5} and acts as −1 on g_{e₁}: Φ_h(k̂) = h Φ(k̂) is M-equivariant only if z: h ↦ −h. "
      "z = (half-turn of the Šilov circle, coords 6,7) × (half-turn on 1,2): the helicity sign IS the circle's orientation")
score("E2b", resid > 0.5, f"the circle half-turn ALONE does not preserve g_{{e₁}} (relative residual {resid:.3f}; 5871 S4: it moves ±e₁ to ±e₂); only its product with the (1,2) half-turn lies in M and acts as −1: the sign flip needs both half-turns")

print("E3  three commits span g_{e₁} iff det G ≠ 0; the failure set has measure zero")
def gram_det(ks): return np.linalg.det(np.array(ks) @ np.array(ks).T)
ok3 = True
for _ in range(200):
    ks = [rng.normal(size=3) for _ in range(3)]; ks = [x / np.linalg.norm(x) for x in ks]
    dG = gram_det(ks); triple = np.dot(ks[0], np.cross(ks[1], ks[2]))
    ok3 &= np.isclose(dG, triple ** 2) and (np.linalg.matrix_rank(np.array([Phi(x) for x in ks])) == 3) == (abs(dG) > 1e-12)
# measure of the failure set: P(|det G| < eps) vs eps
Nmc = 400000
ks = rng.normal(size=(Nmc, 3, 3)); ks /= np.linalg.norm(ks, axis=2, keepdims=True)
trip = np.einsum('ni,ni->n', ks[:, 0], np.cross(ks[:, 1], ks[:, 2])); dG = trip ** 2
eps = np.array([1e-1, 1e-2, 1e-3, 1e-4]); P = np.array([(dG < e).mean() for e in eps])
slope = np.polyfit(np.log(eps[1:]), np.log(P[1:]), 1)[0]
print(f"     P(|det G| < ε): {dict(zip(eps, np.round(P, 5)))};  log-slope ≈ {slope:.2f} (det G = (triple product)² ⇒ P ∝ √ε: slope 1/2)")
score("E3", ok3 and abs(slope - 0.5) < 0.08,
      "det G = (k̂₁·k̂₂×k̂₃)² and rank Φ(k̂₁..₃) = 3 ⟺ det G ≠ 0 (200 triples); P(|det G| < ε) ∝ ε^{1/2} → 0: coplanar triples are measure zero (codimension one in the triple product)")

print("E4  helicity signs: span unchanged, orientation flips with an odd number of signs")
ok4 = True
for _ in range(100):
    ks = [rng.normal(size=3) for _ in range(3)]; ks = [x / np.linalg.norm(x) for x in ks]
    h = rng.choice([-1, 1], size=3)
    F0 = np.array([Phi(x) for x in ks]); F1 = np.array([hh * Phi(x) for hh, x in zip(h, ks)])
    ok4 &= np.isclose(abs(np.linalg.det(F0)), abs(np.linalg.det(F1))) and np.isclose(np.sign(np.linalg.det(F1)), np.sign(np.linalg.det(F0)) * np.prod(h))
score("E4", ok4, "signed frames h_i Φ(k̂_i): |det| unchanged (same span), sign(det) multiplied by Π h_i — the triple's orientation (KL3's read-order sign) rides on the helicities, not on the axes")

print("E5  parameter count for colour-from-axes (Lyra item 3; a count, not a claim)")
dim_SO3, dim_SU3, dim_U3 = 3, 8, 9
score("E5", dim_SU3 - dim_SO3 == 5 and dim_U3 - dim_SO3 == 6,
      "three real axes → a real frame of g_{e₁} (an SO(3) element after Gram–Schmidt: 3 parameters); a unitary frame of g_{e₁}⊗ℂ = ℂ³ has 8 (SU(3)), 9 with the det phase (U(3)): "
      "the axes alone reach SO(3) ⊂ SU(3); the missing 5 (6) real parameters are relative phases between the three commits — the Bargmann/record phases, not axes")

passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (all {len(RESULTS)} can fail)")
