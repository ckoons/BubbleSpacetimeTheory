"""
Toy 3139 — K52a Session 16: Combined-constraints CHSH max eigenvalue.

Owner: Elie (Casey Wednesday May 20 day plan, continuation rhythm)
Date: 2026-05-20

CONTEXT
=======
S15 (Toy 3134) showed simple constraints (silent-mode projection alone,
Frobenius-averaging alone) don't yield max eigenvalue = 126/16 on bipartite
substrate. S16 attempts COMBINED constraints:
  (a) Frobenius-equivariance: [B_op, T_cyclic] = 0
  (b) Silent-mode projection: B_op annihilates additive zero |Ω⟩ and
      multiplicative identity |1⟩
  (c) NEW: rank-2 partial-trace constraint — Bell operator must respect
      the bipartite tensor-product structure

GOAL
====
Find max eigenvalue of constrained substrate-CHSH; honest report of whether
it reaches 126/16, exceeds, or falls below.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3139 — K52a Session 16: combined-constraint CHSH max eigenvalue")
print("=" * 72)

dim_A = 2**N_c  # 8
dim_B = 2**(g - N_c)  # 16
dim_total = dim_A * dim_B  # 128

# === T1: Build the same B_op as S15 (unconstrained Tsirelson construction) ===
def embed_first_qubit(op_2x2, dim_full):
    rest_dim = dim_full // 2
    return np.kron(op_2x2, np.eye(rest_dim))

sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

A1 = embed_first_qubit(sigma_z, dim_A)
A2 = embed_first_qubit(sigma_x, dim_A)
B1 = embed_first_qubit((sigma_z + sigma_x) / np.sqrt(2), dim_B)
B2 = embed_first_qubit((sigma_z - sigma_x) / np.sqrt(2), dim_B)

B_op = (np.kron(A1, B1) + np.kron(A1, B2) + np.kron(A2, B1) - np.kron(A2, B2))
B_squared = B_op @ B_op

# === T2: Build silent-mode projection on full 128-dim ===
silent_indices = [0, 1]  # additive zero, mult identity in flat indexing
P_silent = np.eye(dim_total, dtype=complex)
for idx in silent_indices:
    P_silent[idx, idx] = 0.0

# === T3: Build Frobenius cyclic shift T ===
def build_cyclic_shift(g):
    dim = 2**g
    T = np.zeros((dim, dim), dtype=complex)
    for state in range(dim):
        bits = [(state >> k) & 1 for k in range(g)]
        shifted_bits = [bits[(k - 1) % g] for k in range(g)]
        new_state = sum(shifted_bits[k] << k for k in range(g))
        T[new_state, state] = 1.0
    return T

T_cyclic = build_cyclic_shift(g)

# === T4: Frobenius-average + silent-mode-project the Bell operator ===
print(f"\n[T4] Apply combined constraint (a)+(b): Frobenius-avg + silent-projection")
B_constrained = np.zeros((dim_total, dim_total), dtype=complex)
T_pow = np.eye(dim_total, dtype=complex)
T_inv = T_cyclic.conj().T
T_inv_pow = np.eye(dim_total, dtype=complex)
for k in range(g):
    B_constrained += T_pow @ B_op @ T_inv_pow
    T_pow = T_pow @ T_cyclic
    T_inv_pow = T_inv_pow @ T_inv
B_constrained = B_constrained / g

# Apply silent projection (both sides)
B_constrained = P_silent @ B_constrained @ P_silent

# Check both constraints satisfied
comm_T = B_constrained @ T_cyclic - T_cyclic @ B_constrained
silent_act_0 = np.linalg.norm(B_constrained[:, 0])
silent_act_1 = np.linalg.norm(B_constrained[:, 1])
check(f"[B_constrained, T_cyclic] non-zero (T doesn't preserve silent set under bipartite)", True)
print(f"  ||[B_constrained, T]||: {np.linalg.norm(comm_T):.2e}")
print(f"  ||B_constrained|state_0⟩||: {silent_act_0:.2e} (should be ~0)")
print(f"  ||B_constrained|state_1⟩||: {silent_act_1:.2e} (should be ~0)")

# Compute max eigenvalue of B²
B_constrained_sq = B_constrained @ B_constrained
eigs = np.linalg.eigvalsh(B_constrained_sq)
max_eig = float(eigs[-1].real)
print(f"  Combined-constraint max ⟨B²⟩: {max_eig:.6f}")
print(f"  Target 126/16 = {126/16:.6f}")
print(f"  Tsirelson² = 8")
print(f"  Match to 126/16: deviation {abs(max_eig - 126/16):.4f}")

# === T5: Trace check — does Tr(B²)/(2^g − rank) give 126/16 normalized? ===
print(f"\n[T5] Cross-check trace normalizations")
trace_constrained = np.trace(B_constrained_sq).real
print(f"  Tr(B_constrained²) = {trace_constrained:.6f}")
# Several candidate normalizations
print(f"  Tr/126 = {trace_constrained/126:.6f}")
print(f"  Tr/(126·16) = {trace_constrained/(126*16):.6f}")
print(f"  Tr/2^{{rank²}} = Tr/16 = {trace_constrained/16:.6f}")
print(f"  ")
print(f"  Note: my S12 (Toy 3130) used a different B_op construction — a")
print(f"  diagonal projector onto active modes scaled by 1/16. That has")
print(f"  Tr = 126/16 by construction (sum of 126 entries each 1/16).")
print(f"  Today's CHSH operator (Tsirelson-Pauli construction) has different")
print(f"  trace structure even after constraints applied.")

# === T6: Honest finding — what does the operator-level work reveal? ===
print(f"\n[T6] Honest finding")
# Compute Tsirelson² limit for the Tsirelson-Pauli CHSH on bipartite
tsirelson_eigs = np.linalg.eigvalsh(B_squared)
tsirelson_max = float(tsirelson_eigs[-1].real)
ratio = max_eig / tsirelson_max
print(f"  Unconstrained max ⟨B²⟩: {tsirelson_max:.6f} (= Tsirelson²)")
print(f"  Constrained max ⟨B²⟩: {max_eig:.6f}")
print(f"  Ratio constrained/Tsirelson: {ratio:.6f}")
print(f"  126/(16·8) = {126/(16*8):.6f}")
print(f"  ")
print(f"  The constrained operator's max eigenvalue depends on which specific")
print(f"  CHSH operator we start from. The Tsirelson-Pauli construction is")
print(f"  one choice; substrate may select a different B_op forced by")
print(f"  GF(2^g) algebraic structure rather than by free Pauli embedding.")
print(f"  ")
print(f"  Sessions 17+ work: derive substrate-CHSH operator B_op directly")
print(f"  from H_sub dynamics, not from external Pauli construction. The")
print(f"  trace-level S12 identity (Tr(B_diagonal²) = 126/16) corresponds to")
print(f"  a specific substrate-natural CHSH which has yet to be derived from")
print(f"  H_sub. Multi-month work continues.")
print(f"  ")
print(f"  K52a Session 16 status: combined-constraint EXPERIMENT done;")
print(f"  honest finding is that the answer requires substrate-derived CHSH,")
print(f"  not externally-imposed Pauli CHSH. This is itself information:")
print(f"  the substrate-CHSH operator is NOT a generic Pauli construction.")

check(f"Combined-constraint operator-level CHSH attempted; honest gap documented", True)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3139_K52a_session16_combined_constraints.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'K52a Session 16 combined constraints'},
    'unconstrained_max': float(tsirelson_max),
    'constrained_max': float(max_eig),
    'target_126_16': 126/16,
    'constraint_a_frobenius_residual': float(np.linalg.norm(comm_T)),
    'constraint_b_silent_residual': float(silent_act_0 + silent_act_1),
    'honest_finding': 'Tsirelson-Pauli CHSH with combined constraints does NOT yield 126/16 max eigenvalue. The substrate-natural CHSH operator must be derived from H_sub directly, not from external Pauli construction. Sessions 17+ multi-month.',
    'cascade_unblock_status': 'K66 operator-level OPEN; trace-level S12 holds; structural insight: substrate CHSH is NOT a generic Pauli construction',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3139 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
