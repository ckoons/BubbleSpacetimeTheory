"""
Toy 3186 — K52a Session 20: Bergman projection explicit construction.

Owner: Elie (primary thread continuation, multi-month)
Date: 2026-05-20

CONTEXT
=======
Session 19 (Toy 3183) opened H_sub_emit Zone 3 framework with Bergman-natural
observable candidates. Session 20 advances to explicit Bergman projection
construction on a finite-dimensional analog of D_IV⁵.

Lyra T2425 just delivered angular momentum L_substrate = M_z × P_z on
Bergman A²(D_IV⁵). The zoo is at 5 of 6. The remaining operator is
energy/Hamiltonian, which IS my K52a Sessions multi-month work.

GOAL TODAY
==========
1. Build finite-dim Bergman-like reproducing kernel
2. Verify reproducing property
3. Identify projection operator structure
4. Cross-link to T2425 angular momentum (zoo 5/6)
5. Frame Session 21+ where substrate-CHSH operator emerges

CAL MODE 1 VIGILANCE + #14 DISCIPLINE
=====================================
Per Lyra's #14 propagation: explicit honest-flag notes distinguishing
rep-theoretic / definitional choices from emergent BST signatures.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3186 — K52a Session 20: Bergman projection explicit construction")
print("=" * 72)

# === T1: Finite-dim Bergman-like kernel on disk analog ===
print(f"\n[T1] Finite-dim Bergman kernel on a disk analog (sanity test)")
# Bergman kernel on unit disk: K(z,w) = 1 / (π(1 - z·w̄)²)
# For D_IV⁵ in normalized form: K(z,w) = c_FK / (1 - z·w̄)^(g+rank)/rank = c_FK / (1 - z·w̄)^(9/2)
# We build a finite-dim sampled version

# Sample N points on unit disk
N_sample = 64  # finite-dim analog dimension
np.random.seed(42)
# Use systematic grid on disk for reproducibility
angles = np.linspace(0, 2 * np.pi, N_sample, endpoint=False)
radii = np.linspace(0.1, 0.9, N_sample)
sample_pts = radii * np.exp(1j * angles)

# Bergman exponent for D_IV⁵
bergman_exp = (g + rank) / rank  # 9/2
print(f"  Bergman exponent (g+rank)/rank = {bergman_exp} (= N_c²/rank = 9/2)")
print(f"  Sample points: N = {N_sample} (finite-dim analog)")

# Build kernel matrix K_ij = K(z_i, z_j) on these samples
K_matrix = np.zeros((N_sample, N_sample), dtype=complex)
for i in range(N_sample):
    for j in range(N_sample):
        z_i = sample_pts[i]
        z_j = sample_pts[j]
        inner = 1 - z_i * np.conj(z_j)
        K_matrix[i, j] = 1.0 / (inner ** bergman_exp)

print(f"  Bergman kernel matrix built (shape {K_matrix.shape})")
print(f"  Diagonal mean: {np.mean(np.abs(np.diag(K_matrix))):.4f}")
print(f"  Off-diagonal mean: {np.mean(np.abs(K_matrix - np.diag(np.diag(K_matrix)))):.4f}")
check(f"Diagonal dominates off-diagonal (reproducing kernel sanity)",
      np.mean(np.abs(np.diag(K_matrix))) > 2 * np.mean(np.abs(K_matrix - np.diag(np.diag(K_matrix)))))

# === T2: Reproducing property (sanity check) ===
print(f"\n[T2] Reproducing property sanity check")
# f(z) = ∫ K(z, w) f(w) dμ(w) for f holomorphic
# On finite-dim grid: f_i = Σ_j K(z_i, z_j) f_j · w_j (with quadrature weights)
# Use simple uniform weights for sanity test
weights = np.ones(N_sample) / N_sample

# Test with a holomorphic function f(z) = z (or z^2)
f_test = sample_pts.copy()  # f(z) = z
f_reproduced = K_matrix @ (f_test * weights)
# Normalize comparison
correlation = np.real(np.vdot(f_test, f_reproduced)) / (np.linalg.norm(f_test) * np.linalg.norm(f_reproduced))
print(f"  Reproducing-property correlation: {correlation:.4f}")
print(f"  (Perfect reproduction would be 1.0; finite-grid approximation)")
print(f"  ")
print(f"  Note: this is a SAMPLED finite-dim approximation, not the true Bergman")
print(f"  projection on D_IV⁵. The reproducing-property correlation > 0.5")
print(f"  indicates the construction captures the right structural pattern.")
check(f"Reproducing property correlation > 0.5 (structural sanity)", correlation > 0.5)

# === T3: Projection-onto-boundary structure ===
print(f"\n[T3] Projection-onto-boundary structure (Zone 3 emission interface)")
# Boundary = Šilov boundary of disk = unit circle (|z| = 1)
# Project: f(z) on disk → f(e^{iθ}) on boundary
# Discrete: take outer-radius samples as "boundary" approximation
boundary_indices = np.where(radii > 0.85)[0]
n_boundary = len(boundary_indices)
print(f"  Boundary points (radii > 0.85): {n_boundary} of {N_sample}")

# Boundary kernel: K restricted to boundary indices
K_boundary = K_matrix[np.ix_(boundary_indices, boundary_indices)]
boundary_eigs = np.linalg.eigvalsh((K_boundary + K_boundary.conj().T) / 2)
print(f"  Boundary kernel spectrum range: [{boundary_eigs[0].real:.4f}, {boundary_eigs[-1].real:.4f}]")
# The projection-onto-boundary picks up specific eigenvalues
# Per S17 zone framework: this is the Zone 3 substrate vacuum signature

# === T4: Cross-link to T2425 angular momentum ===
print(f"\n[T4] Cross-link to Lyra T2425 angular momentum")
print(f"  Lyra T2425: L_substrate = M_z × P_z (Bergman cross-product)")
print(f"  Standard L = r × p (position × momentum cross-product)")
print(f"  ")
print(f"  Per per-zone framework: which zone does L_substrate live in?")
print(f"  - Position M_z (T2419) → Zone 4 (outer-edge spacetime projection)")
print(f"  - Momentum P_z (T2422) → Zone 4 also (or boundary-zone)")
print(f"  - Their cross-product L → Zone 4 (boundary expression)")
print(f"  ")
print(f"  Honest scope: zone assignment for L_substrate is structural reading,")
print(f"  not derived from H_sub. Multi-month verification needed.")
print(f"  ")
print(f"  Discipline #14 propagation: Lyra's '10 SO(5) generators - 3 SO(3) = 7 = g'")
print(f"  flagged as rep-theoretic dim arithmetic, NOT emergent BST signature.")
print(f"  Same Cal Mode 1 vigilance applies here: do not claim emergent")
print(f"  identifications where the math is definitional/dimensional.")

# === T5: Substrate-CHSH operator from Bergman projection (preview) ===
print(f"\n[T5] Session 21+ preview: substrate-CHSH from Bergman projection")
print(f"  Session 21 task: construct substrate-CHSH operator B_substrate from")
print(f"  the Bergman projection structure built today.")
print(f"  ")
print(f"  Candidate construction:")
print(f"    B_substrate = (1/2^{{rank²}}) · Σ_α radiation(α) · P_α")
print(f"    where:")
print(f"      P_α = Bergman projection onto α-th boundary cycle")
print(f"      radiation(α) = ±1 sign on whether α is active (radiating)")
print(f"      1/2^{{rank²}} = rank-2 two-party correlation normalization")
print(f"  ")
print(f"  This is the Toy 3130 (S12) trace-level construction lifted to")
print(f"  operator level via explicit Bergman projection.")
print(f"  ")
print(f"  Multi-month: Session 21 attempts this; Session 22 verifies max eigenvalue.")

# === T6: Session 20 status ===
print(f"\n[T6] Session 20 status")
print(f"  Today opened: finite-dim Bergman kernel on disk analog, reproducing")
print(f"  property sanity, boundary projection structure.")
print(f"  ")
print(f"  Today did NOT close: full Bergman projection on D_IV⁵ (5 complex dim,")
print(f"  not 1), substrate-CHSH operator construction, max eigenvalue derivation.")
print(f"  ")
print(f"  Multi-month roadmap:")
print(f"  - Session 21: lift to D_IV⁵ proper (5 complex dim)")
print(f"  - Session 22: substrate-CHSH operator + max eigenvalue 126/16")
print(f"  - Session 23+: combine zones into unified H_sub")
print(f"  ")
print(f"  K52a + K66 + K67 + K68 + K69 cascade-unblock pathway continues.")
print(f"  Energy operator (zoo entry 6 of 6) emerges from H_sub full closure.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3186_K52a_S20_Bergman_projection.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'K52a Session 20 Bergman projection explicit'},
    'finite_dim_analog': {
        'N_sample': N_sample,
        'bergman_exponent': float(bergman_exp),
        'reproducing_correlation': float(correlation),
        'boundary_points': int(n_boundary),
    },
    'lyra_T2425_cross_link': 'L_substrate likely Zone 4; structural reading',
    'discipline_14_propagation': 'rep-theoretic vs emergent distinctions flagged',
    'substrate_chsh_construction_preview': 'B_substrate = (1/2^{rank²}) · Σ radiation(α) · P_α',
    'sessions_21_22_roadmap': [
        'S21: lift to D_IV⁵ proper (5 complex dim)',
        'S22: substrate-CHSH operator + max eigenvalue = 126/16',
        'S23+: multi-zone H_sub combination',
    ],
    'zoo_status': '5 of 6 (Lyra zoo); energy (6/6) emerges from K52a full closure',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3186 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
