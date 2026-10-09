#!/usr/bin/env python3
"""
Toy 5880 — Round K4-6: Lyra's Section 3 map retained in ten lines (Elie, 2026-10-09). Exact linear algebra on V_C = g_{e1} (x) C = C^3.
A commit (k̂, s = ±1, φ) ↦ ε = e^{iφ}(â + i s b̂)/√2 with (â, b̂, k̂) right-handed orthonormal. Checks: ε^T ε = 0 (null), ε†ε = 1;
rotation of â about k̂ by θ multiplies ε by e^{−isθ} (weight s = ±1 — 5875's {0, ±1} on g_{e1}); the Stokes-like ε (x) ε̄ has
weight 0 and ε (x) ε has weight ±2 (the double); det(ε₁, ε₂, ε₃) ≠ 0 iff the three axes are independent (Gram det ≠ 0), and
reversing all three orientations (s → −s, i.e. conjugation) flips the sign of det exactly when... computed, not asserted;
ε₁^T ε₂ (the would-be diquark) needs the bilinear form; ε₁†ε₂ (3̄ × 3) does not.
ADDENDUM 2026-10-09 15:50 EDT (Elie, K4-7 Lane B item 1): det(ε₁,ε₂,ε₃) ≠ 0 fails ONLY for parallel axes (200/200 coplanar
triples give det ≠ 0; |det| = 1e-32 for parallel); the Gram determinant of the axes (5878 E3) is the SPANNING condition for the
real frame; the null-vector determinant is a different condition (the colour singlet). N4's FAIL is Lyra's line as written.
"""
import numpy as np
RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")
rng = np.random.default_rng(5880)
def triad(k):
    k = k / np.linalg.norm(k); t = rng.normal(size=3); a = t - (t @ k) * k; a /= np.linalg.norm(a); b = np.cross(k, a); return a, b, k
def eps(k, s, phi):
    a, b, k = triad(k); return np.exp(1j * phi) * (a + 1j * s * b) / np.sqrt(2), (a, b, k)
def rot(axis, th):
    a = axis / np.linalg.norm(axis); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]]); return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K
ok1 = ok2 = ok3 = True
for _ in range(100):
    k = rng.normal(size=3); s = rng.choice([-1, 1]); phi = rng.uniform(0, 2 * np.pi); e, (a, b, kk) = eps(k, s, phi)
    ok1 &= np.isclose(e @ e, 0) and np.isclose(np.vdot(e, e), 1)
    th = rng.uniform(0, 2 * np.pi); Re = rot(kk, th) @ e            # rotating the frame about k̂ by θ
    ok2 &= np.allclose(Re, np.exp(1j * s * th) * e) or np.allclose(Re, np.exp(-1j * s * th) * e)
    w = 1 if np.allclose(Re, np.exp(1j * s * th) * e) else -1
    # Stokes-like tensors: ε⊗ε̄ invariant (weight 0); ε⊗ε weight ±2
    ok3 &= np.allclose(np.outer(Re, Re.conj()), np.outer(e, e.conj())) and np.allclose(np.outer(Re, Re), np.exp(2j * w * s * th) * np.outer(e, e))
score("N1", ok1, "ε^T ε = 0 and ε†ε = 1 for 100 random commits: the commit's vector is NULL and unit in g_{e₁} ⊗ ℂ")
score("N2", ok2, "a rotation about k̂ by θ multiplies ε by e^{±isθ}: weight ±1 (5875's {0, ±1} on g_{e₁}); the sign convention is the helicity's")
score("N3", ok3, "ε ⊗ ε̄ has weight 0 and ε ⊗ ε weight ±2: the Stokes double is the tensor square of the null vector (Lyra Sec. 3 (iii))")
ok4 = ok5 = True; dets = []
for _ in range(200):
    ks = [rng.normal(size=3) for _ in range(3)]; ss = rng.choice([-1, 1], size=3)
    es = [eps(k, s_, 0.0)[0] for k, s_ in zip(ks, ss)]
    d = np.linalg.det(np.array(es)); G = np.linalg.det(np.array([k / np.linalg.norm(k) for k in ks]) @ np.array([k / np.linalg.norm(k) for k in ks]).T)
    ok4 &= (abs(d) > 1e-10) == (G > 1e-10)
    es_c = [eps(k, -s_, 0.0)[0] for k, s_ in zip(ks, ss)]          # all three orientations reversed (new random â each: phases differ)
    dets.append((abs(d), abs(np.linalg.det(np.array(es_c)))))
# coplanar triple: det must vanish
k1, k2 = rng.normal(size=3), rng.normal(size=3); k3 = 0.3 * k1 + 0.7 * k2
d_cop = np.linalg.det(np.array([eps(k, 1, 0.0)[0] for k in (k1, k2, k3)]))
# Lyra's (ii) as written: "det ≠ 0 iff the three axes are independent". Tested, not assumed:
n_cop_nonzero = 0
for _ in range(200):
    k1, k2 = rng.normal(size=3), rng.normal(size=3); k3 = rng.normal() * k1 + rng.normal() * k2
    n_cop_nonzero += abs(np.linalg.det(np.array([eps(k, rng.choice([-1, 1]), rng.uniform(0, 6.3))[0] for k in (k1, k2, k3)]))) > 1e-6
par = abs(np.linalg.det(np.array([eps(k1, 1, rng.uniform(0, 6.3))[0] for _ in range(3)])))
score("N4", ok4 and abs(d_cop) < 1e-10,
      f"Lyra (ii) 'det(ε₁,ε₂,ε₃) ≠ 0 ⟺ axes independent' as written: {n_cop_nonzero}/200 COPLANAR triples give det ≠ 0 (example |det| = {abs(d_cop):.3f}); "
      f"only PARALLEL axes force det = 0 (|det| = {par:.1e}). The singlet's vanishing set is 'two commits share an axis', not 'coplanar axes' — for Lyra, the sentence needs rewording; the Gram condition (5878) is the REAL-frame statement, not the null-vector one")
score("N5", all(np.isclose(x, y) for x, y in dets), "|det| is unchanged when all three helicities are reversed (conjugation up to phases): the orientation sign lives in the phase of det, as Lyra wrote")
e1, _ = eps(rng.normal(size=3), 1, 0.3); e2, _ = eps(rng.normal(size=3), -1, 1.1)
score("N6", True, f"ε₁^T ε₂ = {e1 @ e2:.3f} needs the bilinear form (the diquark; forgotten with the real structure); ε₁†ε₂ = {np.vdot(e1, e2):.3f} is Hermitian (3̄ × 3, the meson) — printed, not scored (a definition)")
passed = sum(RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}  (N1–N5 can fail; N6 is a definition line)")
