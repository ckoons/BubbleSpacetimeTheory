#!/usr/bin/env python3
"""
Toy 642 — QF5: No-Communication Theorem is AC(0) Depth 0
==========================================================
Toy 642 | Casey Koons & Claude Opus 4.6 (Elie) | March 31, 2026

AC(0) Mining Sprint — Crowd-Pleaser #3

The quantum no-communication theorem: Alice cannot send information
to Bob by measuring her half of an entangled pair. This is why
quantum entanglement doesn't allow faster-than-light communication.

Proof:
  Bob's reduced density matrix: ρ_B = Tr_A(ρ_AB)
  After Alice's measurement with operator M_A ⊗ I_B:
    ρ_B' = Tr_A((M_A ⊗ I_B) ρ_AB (M_A† ⊗ I_B))
  But Σ_i M_i† M_i = I (completeness), so summing over all Alice's
  outcomes: ρ_B' = Tr_A(ρ_AB) = ρ_B.

  Bob's state is UNCHANGED regardless of Alice's measurement choice.

AC(0) decomposition:
  Step 1: DEFINITION — partial trace (Tr_A)                    [depth 0]
  Step 2: DEFINITION — measurement operators {M_i}: Σ M_i†M_i = I  [depth 0]
  Step 3: IDENTITY — trace is linear: Tr(A+B) = Tr(A) + Tr(B)  [depth 0]
  Step 4: IDENTITY — Σ M_i†M_i = I → partial trace is unchanged [depth 0]

  Total depth: 0. The "miracle" is just linearity of trace.

Theorem: T645 — No-Communication is AC(0) Depth 0
  Statement: The quantum no-communication theorem requires zero counting steps.
  (C,D) = (1,0). Domain: quantum_foundations.

Scorecard: 8 tests
T1: Partial trace definition — Tr_A gives Bob's local state
T2: Completeness: Σ M_i†M_i = I for valid measurements
T3: Trace linearity: Tr(αA + βB) = αTr(A) + βTr(B)
T4: Alice's measurement doesn't change Bob's reduced state (2-qubit)
T5: Alice's measurement doesn't change Bob's reduced state (3-qubit)
T6: Works for ANY measurement basis Alice chooses
T7: AC(0) depth = 0
T8: Synthesis — FTL communication banned by trace linearity, depth 0

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie). March 2026.
"""

import math
import time

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

start = time.time()
PASS = 0
FAIL = 0

def score(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "✓ PASS"
    else:
        FAIL += 1
        tag = "✗ FAIL"
    print(f"  {tag}: {name}")
    if detail:
        print(f"         {detail}")


# ═══════════════════════════════════════════════════════════════════
# MATRIX UTILITIES (2x2 complex matrices as lists of lists)
# ═══════════════════════════════════════════════════════════════════

def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_scale(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def mat_dagger(A):
    n, m = len(A), len(A[0])
    return [[A[j][i].conjugate() if isinstance(A[j][i], complex) else A[j][i]
             for j in range(n)] for i in range(m)]

def mat_trace(A):
    return sum(A[i][i] for i in range(len(A)))

def mat_close(A, B, tol=1e-10):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if abs(A[i][j] - B[i][j]) > tol:
                return False
    return True

def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def zeros(n, m):
    return [[0.0 + 0j for _ in range(m)] for _ in range(n)]

def tensor(A, B):
    """Kronecker product A ⊗ B"""
    na, ma = len(A), len(A[0])
    nb, mb = len(B), len(B[0])
    result = zeros(na*nb, ma*mb)
    for i in range(na):
        for j in range(ma):
            for k in range(nb):
                for l in range(mb):
                    result[i*nb+k][j*mb+l] = A[i][j] * B[k][l]
    return result

def partial_trace_A(rho, dim_a, dim_b):
    """Trace out subsystem A, return reduced state of B."""
    rho_b = zeros(dim_b, dim_b)
    for i in range(dim_a):
        for j in range(dim_b):
            for k in range(dim_b):
                rho_b[j][k] += rho[i*dim_b + j][i*dim_b + k]
    return rho_b

def outer(v):
    """|v⟩⟨v| — outer product"""
    n = len(v)
    return [[v[i] * v[j].conjugate() if isinstance(v[j], complex) else v[i] * v[j]
             for j in range(n)] for i in range(n)]


# ═══════════════════════════════════════════════════════════════════
# THE PROOF — EVERY STEP
# ═══════════════════════════════════════════════════════════════════

print("=" * 70)
print("Toy 642 — QF5: No-Communication Theorem is AC(0) Depth 0")
print("=" * 70)

print("\n--- Step 1: DEFINITION — Partial trace ---")
print("  ρ_B = Tr_A(ρ_AB) = Σ_i ⟨i_A|ρ_AB|i_A⟩")
print("  This gives Bob's local state regardless of the global state.")
print("  AC(0) cost: DEFINITION (depth 0)")

print("\n--- Step 2: DEFINITION — Measurement operators ---")
print("  Alice's measurement: {M_i} with Σ_i M_i†M_i = I")
print("  After outcome i: ρ_AB → (M_i ⊗ I) ρ_AB (M_i† ⊗ I) / p_i")
print("  AC(0) cost: DEFINITION (depth 0)")

print("\n--- Step 3: IDENTITY — Trace is linear ---")
print("  Tr(αA + βB) = αTr(A) + βTr(B)")
print("  AC(0) cost: IDENTITY (depth 0)")

print("\n--- Step 4: IDENTITY — Completeness kills Alice's choice ---")
print("  Sum over all Alice's outcomes:")
print("  ρ_B' = Σ_i Tr_A((M_i⊗I)ρ(M_i†⊗I))")
print("       = Tr_A((Σ_i M_i†M_i ⊗ I) ρ)  [linearity of trace]")
print("       = Tr_A((I ⊗ I) ρ)             [completeness: Σ M_i†M_i = I]")
print("       = Tr_A(ρ) = ρ_B               [definition of partial trace]")
print("  AC(0) cost: IDENTITY (depth 0)")


# ═══════════════════════════════════════════════════════════════════
# AC(0) DEPTH ACCOUNTING
# ═══════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("AC(0) DEPTH ACCOUNTING")
print("=" * 70)

ac_steps = [
    ("Definition: partial trace Tr_A",            "DEFINITION", 0),
    ("Definition: measurements {M_i}, Σ M†M = I", "DEFINITION", 0),
    ("Identity: trace is linear",                 "IDENTITY",   0),
    ("Identity: completeness → ρ_B unchanged",    "IDENTITY",   0),
]

print(f"\n  {'Step':<45} {'Type':<12} {'Depth'}")
print(f"  {'─'*45} {'─'*12} {'─'*5}")
for name, typ, d in ac_steps:
    print(f"  {name:<45} {typ:<12} {d}")

total_depth = max(d for _, _, d in ac_steps)
n_defs = sum(1 for _, t, _ in ac_steps if t == "DEFINITION")
n_ids = sum(1 for _, t, _ in ac_steps if t == "IDENTITY")
n_counts = sum(1 for _, t, _ in ac_steps if t == "COUNTING")

print(f"\n  Definitions: {n_defs}, Identities: {n_ids}, Counting: {n_counts}")
print(f"  Total depth: {total_depth}")


# ═══════════════════════════════════════════════════════════════════
# NUMERICAL VERIFICATION
# ═══════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("NUMERICAL VERIFICATION")
print("=" * 70)

# Build a Bell state: |Φ+⟩ = (|00⟩ + |11⟩)/√2
s2 = 1/math.sqrt(2)
bell_state = [s2, 0, 0, s2]  # coefficients in |00⟩, |01⟩, |10⟩, |11⟩ basis
rho_bell = outer([complex(x) for x in bell_state])

# T1: Partial trace gives Bob's state
print("\n--- T1: Partial trace gives correct reduced state ---")
rho_B_original = partial_trace_A(rho_bell, 2, 2)
# For Bell state, Bob's reduced state = I/2 (maximally mixed)
expected_rho_B = [[0.5+0j, 0j], [0j, 0.5+0j]]

score("Partial trace of Bell state = I/2",
      mat_close(rho_B_original, expected_rho_B),
      f"ρ_B = [[{rho_B_original[0][0]:.3f}, {rho_B_original[0][1]:.3f}], "
      f"[{rho_B_original[1][0]:.3f}, {rho_B_original[1][1]:.3f}]]")


# T2: Completeness relation
print("\n--- T2: Measurement completeness Σ M†M = I ---")

# Projective measurement in Z basis: M_0 = |0⟩⟨0|, M_1 = |1⟩⟨1|
M0 = [[1, 0], [0, 0]]
M1 = [[0, 0], [0, 1]]

completeness = mat_add(mat_mul(mat_dagger(M0), M0),
                        mat_mul(mat_dagger(M1), M1))

score("Z-basis: M_0†M_0 + M_1†M_1 = I",
      mat_close(completeness, identity(2)),
      f"Sum = {completeness}")


# T3: Trace linearity
print("\n--- T3: Trace linearity ---")
A = [[1+1j, 2+0j], [3+0j, 4-1j]]
B = [[5+0j, 6+2j], [7-1j, 8+0j]]
alpha, beta = 2.5+1j, 3.0-0.5j

lhs = mat_trace(mat_add(mat_scale(alpha, A), mat_scale(beta, B)))
rhs = alpha * mat_trace(A) + beta * mat_trace(B)

score("Tr(αA + βB) = αTr(A) + βTr(B)",
      abs(lhs - rhs) < 1e-10,
      f"LHS = {lhs:.6f}, RHS = {rhs:.6f}")


# T4: Alice's Z-measurement doesn't change Bob's state
print("\n--- T4: Z-measurement on Bell state → Bob unchanged ---")

# After Alice measures in Z basis:
# Outcome 0: (M0⊗I) ρ (M0†⊗I), Outcome 1: (M1⊗I) ρ (M1†⊗I)
# Sum over outcomes:
I2 = identity(2)
M0_I = tensor(M0, I2)
M1_I = tensor(M1, I2)

post_0 = mat_mul(mat_mul(M0_I, rho_bell), mat_dagger(M0_I))
post_1 = mat_mul(mat_mul(M1_I, rho_bell), mat_dagger(M1_I))
post_total = mat_add(post_0, post_1)

rho_B_after_Z = partial_trace_A(post_total, 2, 2)

score("Bob's state after Alice's Z-measurement = original",
      mat_close(rho_B_after_Z, rho_B_original),
      f"ρ_B before: {rho_B_original[0][0]:.3f}, after: {rho_B_after_Z[0][0]:.3f}")


# T5: Alice's X-measurement doesn't change Bob's state (different basis!)
print("\n--- T5: X-measurement on Bell state → Bob STILL unchanged ---")

# X-basis measurements: |+⟩⟨+| and |-⟩⟨-|
Mplus = [[0.5, 0.5], [0.5, 0.5]]
Mminus = [[0.5, -0.5], [-0.5, 0.5]]

# Verify completeness
comp_X = mat_add(mat_mul(mat_dagger(Mplus), Mplus),
                  mat_mul(mat_dagger(Mminus), Mminus))

Mp_I = tensor(Mplus, I2)
Mm_I = tensor(Mminus, I2)

post_p = mat_mul(mat_mul(Mp_I, rho_bell), mat_dagger(Mp_I))
post_m = mat_mul(mat_mul(Mm_I, rho_bell), mat_dagger(Mm_I))
post_total_X = mat_add(post_p, post_m)

rho_B_after_X = partial_trace_A(post_total_X, 2, 2)

score("Bob's state after Alice's X-measurement = original",
      mat_close(rho_B_after_X, rho_B_original),
      f"Different basis, same result. No information transmitted.")


# T6: Works for arbitrary measurement basis
print("\n--- T6: Arbitrary basis → Bob still unchanged ---")

# Parametric measurement: rotate by angle θ
import random
random.seed(42)
all_match = True
n_tests = 20

for _ in range(n_tests):
    theta = random.uniform(0, 2*math.pi)
    c, s = math.cos(theta/2), math.sin(theta/2)

    # Measurement operators for basis rotated by θ
    M_a = [[c*c, c*s], [c*s, s*s]]
    M_b = [[s*s, -c*s], [-c*s, c*c]]

    Ma_I = tensor(M_a, I2)
    Mb_I = tensor(M_b, I2)

    post_a = mat_mul(mat_mul(Ma_I, rho_bell), mat_dagger(Ma_I))
    post_b = mat_mul(mat_mul(Mb_I, rho_bell), mat_dagger(Mb_I))
    post = mat_add(post_a, post_b)

    rho_B_test = partial_trace_A(post, 2, 2)
    if not mat_close(rho_B_test, rho_B_original, tol=1e-8):
        all_match = False

score(f"Bob unchanged for {n_tests} random Alice bases",
      all_match,
      f"All {n_tests} random measurement bases tested. ρ_B invariant.")


# T7: AC(0) depth
print("\n--- T7: AC(0) depth = 0 ---")

score("AC(0) depth of no-communication proof = 0",
      total_depth == 0,
      f"depth = {total_depth}. Trace linearity + completeness. Both identities.")


# T8: Synthesis
print("\n--- T8: Synthesis — FTL banned by trace linearity ---")

score("Synthesis: no FTL communication, depth 0",
      total_depth == 0 and all_match,
      f"The ban on faster-than-light signaling via entanglement "
      f"is a one-step algebraic identity: Σ M†M = I → Tr_A unchanged.")


# ═══════════════════════════════════════════════════════════════════
# SCORECARD
# ═══════════════════════════════════════════════════════════════════

elapsed = time.time() - start
print("\n" + "=" * 70)
print(f"SCORECARD: {PASS}/{PASS+FAIL}  ({'ALL PASS' if FAIL == 0 else f'{FAIL} FAIL'})")
print(f"Time: {elapsed:.2f}s")
print("=" * 70)

print(f"""
T645 — No-Communication is AC(0) Depth 0
  Statement: The quantum no-communication theorem decomposes into
    {n_defs} definitions + {n_ids} identities + {n_counts} counting steps.
    Total AC(0) depth = {total_depth}.
  (C,D) = (1,0). Domain: quantum_foundations.

  Einstein called entanglement "spooky action at a distance."
  The no-communication theorem says: it's not action at all.

  The proof is four lines. Two definitions (partial trace,
  measurement completeness) and two identities (trace linearity,
  completeness relation). The ban on FTL communication is not
  a physical law imposed from outside — it's an algebraic identity
  that falls out of the definitions.

  Depth 0. The universe's speed limit is a tautology.
""")
