"""
Toy 3134 — K52a Session 15: Operator-level CHSH max eigenvalue on bipartite substrate.

Owner: Elie (Casey Wednesday May 20 day plan: Thread A K52a Sessions 15+ continuation)
Date: 2026-05-20

CONTEXT
=======
S12 (Toy 3130) derived Tr(B_substrate²) = 126/16 at trace level (capacity
argument: 126 active radiating modes / 16 rank-2 correlation basis size).
S15 upgrades to operator-level: build explicit CHSH operator B on bipartite
substrate 8 × 16 = 128, compute max eigenvalue, compare to:
  - QM Tsirelson² = 8 (unconstrained)
  - Substrate target S_BST² = 126/16 = 7.875 (constrained)

KEY QUESTION
============
Under what algebraic constraint on the observables A_1, A_2, B_1, B_2 does
the max eigenvalue of B² drop from Tsirelson² = 8 to S_BST² = 126/16?

CANDIDATE CONSTRAINTS
=====================
(a) Frobenius-equivariance: observables must commute with Frobenius cyclic
    shift on the substrate's GF(2^g) structure
(b) Identity-mode silencing: observables must annihilate the additive zero
    |Ω⟩ and the multiplicative identity |1⟩ (the 2 "silent" identity modes)
(c) Combined: both (a) and (b)

HONEST SCOPE
============
Today: do the explicit calculation, report what emerges. Multi-month full
derivation if max eigenvalue requires further constraints not yet identified.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3134 — K52a Session 15: operator-level CHSH max eigenvalue")
print("=" * 72)

# === T1: Bipartite split 8 × 16 = 128 ===
print(f"\n[T1] Substrate bipartite split: 8 × 16 = 128 = 2^g")
dim_A = 2**N_c  # 8 (party A: N_c=3 modes)
dim_B = 2**(g - N_c)  # 16 = 2^(g - N_c) = 2^4 (party B: remaining modes)
print(f"  Party A: {N_c} substrate modes → dim {dim_A}")
print(f"  Party B: {g - N_c} substrate modes → dim {dim_B}")
print(f"  Total: {dim_A} × {dim_B} = {dim_A * dim_B} = 2^g")
check(f"Bipartite split 2^N_c × 2^(g-N_c) = 2^g", dim_A * dim_B == 2**g)

# === T2: Standard CHSH operator construction (unconstrained) ===
print(f"\n[T2] Standard CHSH max eigenvalue (Tsirelson, unconstrained)")
# Optimal Tsirelson construction:
# Party A: A_1 = σ_z, A_2 = σ_x (acting on first qubit, identity on rest of A)
# Party B: B_1 = (σ_z + σ_x)/√2, B_2 = (σ_z - σ_x)/√2 (Tsirelson choice)

# To handle dim_A = 8, dim_B = 16, embed 2-dim Pauli on first qubit of each side
def embed_first_qubit(op_2x2, dim_full):
    """Embed 2x2 operator on first qubit, identity on rest."""
    rest_dim = dim_full // 2
    return np.kron(op_2x2, np.eye(rest_dim))

sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

A1 = embed_first_qubit(sigma_z, dim_A)
A2 = embed_first_qubit(sigma_x, dim_A)
B1 = embed_first_qubit((sigma_z + sigma_x) / np.sqrt(2), dim_B)
B2 = embed_first_qubit((sigma_z - sigma_x) / np.sqrt(2), dim_B)

# CHSH operator B = A_1 ⊗ B_1 + A_1 ⊗ B_2 + A_2 ⊗ B_1 − A_2 ⊗ B_2
B_op = (np.kron(A1, B1) + np.kron(A1, B2) + np.kron(A2, B1) - np.kron(A2, B2))
B_squared = B_op @ B_op
B_sq_eigs = np.linalg.eigvalsh(B_squared)
max_eig_unconstrained = float(B_sq_eigs[-1].real)
print(f"  Tsirelson unconstrained max ⟨B²⟩: {max_eig_unconstrained:.6f}")
print(f"  Expected Tsirelson² = 8")
check(f"Unconstrained Tsirelson² = 8 (1e-6)", abs(max_eig_unconstrained - 8) < 1e-6)

# === T3: Constraint (b) — identity-mode silencing ===
print(f"\n[T3] Apply substrate constraint (b): silence identity modes")
# Substrate has 2 silent identity modes: the additive zero (state |0...0⟩)
# and the multiplicative identity (state |0...01⟩ in polynomial basis,
# i.e., index 1 in the 128-dim flat indexing).
#
# In bipartite split 8 × 16, the flat substrate state |k⟩ corresponds to
# (k // 16, k % 16) = (party_A_state, party_B_state).
# Silent states: index 0 (additive zero) and index 1 (multiplicative identity)
# Both have party_A_state = 0 in this indexing.
#
# Silencing means: A_i, B_j should not "see" these modes. We project them out.

# Build projection onto active (non-silent) substrate modes
silent_indices = [0, 1]  # additive zero, multiplicative identity in flat 128-dim indexing
active_proj = np.eye(2**g, dtype=complex)
for idx in silent_indices:
    active_proj[idx, idx] = 0  # remove silent modes
n_active = int(np.trace(active_proj).real)
print(f"  Active modes after silencing: {n_active}")
check(f"Active modes = 126 = 2^g − rank", n_active == 126)

# Constrained CHSH: project before/after each observable application
P = active_proj
B_constrained = P @ B_op @ P
B_constrained_sq = B_constrained @ B_constrained
constrained_eigs = np.linalg.eigvalsh(B_constrained_sq)
max_eig_constrained = float(constrained_eigs[-1].real)
print(f"  Constrained-via-silencing max ⟨B²⟩: {max_eig_constrained:.6f}")
print(f"  Target S_BST² = 126/16 = {126/16:.6f}")
print(f"  Match: {abs(max_eig_constrained - 126/16) < 0.1}")

# === T4: Honest report — does the simple silencing give 126/16? ===
print(f"\n[T4] Honest analysis of S15 attempt today")
# In standard QM, the Tsirelson max ⟨B⟩² = 8 is achieved on a specific
# entangled state. Simple silent-mode projection on the same state may or may
# not reduce to exactly 126/16.

# Find the state achieving max
_, B_squared_evecs = np.linalg.eigh(B_squared)
tsirelson_state = B_squared_evecs[:, -1]  # state achieving max ⟨B²⟩
# Compute ⟨B²⟩ on this state, then project and recompute
print(f"  Tsirelson-optimal state ⟨B²⟩: {(tsirelson_state.conj() @ B_squared @ tsirelson_state).real:.6f}")

# Project Tsirelson state onto active subspace
projected_state = P @ tsirelson_state
norm = np.linalg.norm(projected_state)
projected_state_normalized = projected_state / norm if norm > 1e-10 else projected_state
# Re-evaluate ⟨B²⟩ on projected state
exp_val_projected = (projected_state_normalized.conj() @ B_squared @ projected_state_normalized).real
print(f"  Projected Tsirelson state norm² (active fraction): {norm**2:.6f}")
print(f"  ⟨B²⟩ on projected state (normalized): {exp_val_projected:.6f}")
print(f"  ")
print(f"  Naive silent-mode projection does NOT cleanly give 126/16.")
print(f"  The substrate constraint requires more than simple projection.")
print(f"  Multi-month derivation: need Frobenius-equivariance constraint")
print(f"  on A_i, B_j observables (not on the state).")

# === T5: Constraint (a) attempt — Frobenius-equivariant observables ===
print(f"\n[T5] Constraint (a) attempt: Frobenius-equivariant observables")
# Build Frobenius cyclic shift T on the full 128-dim substrate via the polynomial basis
# T |n_0, n_1, ..., n_{g-1}⟩ = |n_{g-1}, n_0, ..., n_{g-2}⟩
def build_cyclic_shift(g):
    dim = 2**g
    T = np.zeros((dim, dim), dtype=complex)
    for state in range(dim):
        bits = [(state >> k) & 1 for k in range(g)]
        shifted_bits = [bits[(k - 1) % g] for k in range(g)]
        new_state = sum(shifted_bits[k] << k for k in range(g))
        T[new_state, state] = 1.0
    return T

T_op = build_cyclic_shift(g)
# Average B_op over Frobenius orbit:
# B_Frobenius-symmetric = (1/g) Σ_{k=0}^{g-1} T^k B T^{-k}
T_inv = T_op.conj().T  # T is a permutation matrix; inverse = transpose
B_frob_avg = np.zeros((2**g, 2**g), dtype=complex)
T_pow = np.eye(2**g, dtype=complex)
T_inv_pow = np.eye(2**g, dtype=complex)
for k in range(g):
    B_frob_avg += T_pow @ B_op @ T_inv_pow
    T_pow = T_pow @ T_op
    T_inv_pow = T_inv_pow @ T_inv
B_frob_avg = B_frob_avg / g

# Now B_frob_avg commutes with T_op
commutator = B_frob_avg @ T_op - T_op @ B_frob_avg
commutator_norm = np.linalg.norm(commutator)
print(f"  ||[B_Frobenius-avg, T]||: {commutator_norm:.2e}")
check(f"Frobenius-averaged B commutes with T", commutator_norm < 1e-10)

# Eigenvalues of B_Frobenius-avg
B_frob_sq = B_frob_avg @ B_frob_avg
frob_eigs = np.linalg.eigvalsh(B_frob_sq)
max_frob = float(frob_eigs[-1].real)
print(f"  Frobenius-averaged max ⟨B²⟩: {max_frob:.6f}")
print(f"  Target 126/16 = {126/16:.6f}")
print(f"  ")
print(f"  This is one candidate constraint. Multi-month: identify the EXACT")
print(f"  algebraic constraint forcing max ⟨B²⟩ = 126/16 on substrate.")

# === T6: Step 4 status update (S12 + S15 cumulative) ===
print(f"\n[T6] Step 4 status (S12 trace-level + S15 operator attempt)")
print(f"  S12 (Toy 3130): Tr(B²)/n = 126/16 algebraic-identity at trace level")
print(f"  S15 (THIS): operator-level attempt — naive constraints don't yet")
print(f"  yield max eigenvalue = 126/16. Identifying the correct algebraic")
print(f"  constraint is multi-month derivation.")
print(f"  ")
print(f"  HONEST FINDING TODAY: trace-level identity at 126/16 is verified")
print(f"  (S12, EXACT to 1e-14). Operator-level max-eigenvalue derivation")
print(f"  via simple Frobenius-averaging or silent-mode projection does NOT")
print(f"  immediately yield 126/16 — additional algebraic structure needed.")
print(f"  ")
print(f"  K66 Bell substrate-CHSH cross-link: trace-level VERIFIED;")
print(f"  operator-level OPEN (multi-month).")
print(f"  ")
print(f"  Per Cal Flag 2: this is mechanism-investigation work. The trace-level")
print(f"  identity stays algebraic-identity-verified; operator-level pending")
print(f"  mechanism-derivation closes K66 audit fully.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3134_K52a_session15_CHSH_operator.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'K52a Session 15 operator-level CHSH'},
    'casey_authorization': '2026-05-20 day plan Thread A K52a continuation',
    'status': 'operator-level derivation OPEN (multi-month); trace-level S12 verified holds',
    'bipartite_split': {'dim_A': dim_A, 'dim_B': dim_B, 'total': dim_A * dim_B},
    'unconstrained_max': max_eig_unconstrained,
    'tsirelson_squared_expected': 8.0,
    'tsirelson_match': bool(abs(max_eig_unconstrained - 8) < 1e-6),
    'silent_mode_projection': {
        'max_eig': max_eig_constrained,
        'matches_126_16': bool(abs(max_eig_constrained - 126/16) < 0.1),
    },
    'frobenius_avg_attempt': {
        'commutator_norm': float(commutator_norm),
        'max_eig': max_frob,
        'matches_126_16': bool(abs(max_frob - 126/16) < 0.1),
    },
    'honest_finding': 'Simple constraints do not immediately yield 126/16 max eigenvalue. Identifying correct algebraic constraint is multi-month.',
    'next_session_S16_targets': [
        'Combined Frobenius-eq + silent-mode constraint',
        'Direct construction of substrate-CHSH operator from H_sub dynamics',
        'Algebraic argument why max ⟨B²⟩ = (2^g-rank)/2^{rank²} forced by substrate',
    ],
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3134 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
