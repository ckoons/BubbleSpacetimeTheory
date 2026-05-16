"""
Toy 2340 — Box-diagram analog (1): Closed Mersenne cycle residual.

Owner: Elie
Date: 2026-05-15
Out of: Casey directive — try (1) closed Mersenne cycle even though
        (2) already found ε_K = α² · chern_sum.

THE STRUCTURE
=============
BST 4-step chain:
    rank → M(rank) = N_c
         → M(N_c)  = g
         → M(g)    = 127 = M_g
         → (+ rank·n_C) = N_max = 137

The 4th "step" is NOT a Mersenne iteration but the **closing shift**
+ rank·n_C = +10. The cycle CLOSES at N_max via this shift.

QUESTION: does the residual / closing structure give ε_K?

Three plausible readings of the "residual":

(A) Residual ratio: rank·n_C / N_max = 10/137
    Square: (rank·n_C / N_max)² = 100/18769 = 0.00533

(B) Log-residual: log(N_max/M_g) = log(137/127) = 0.0758
    Square: 0.00574

(C) Chern-Mersenne identity:
    Cycle closure forces rank·n_C = N_max - M_g.
    Combined with chern_sum = C_2 · g, ratio gives
    chern_sum · (rank·n_C)² / N_max² · (1/(rank·n_C)²)
    = chern_sum / N_max² = 42/18769 = 0.002238 = ε_K ✓

Reading (C) is structurally identical to Toy 2338's α² · chern_sum
result, just dressed in cycle language.
"""

import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
N_max = 137
M_g = 127
chern_sum = C_2 * g  # 42
eps_K_obs = 2.228e-3

tests = []
def check(label, condition, note=""):
    tests.append((bool(condition), label, note))


print("Closed Mersenne cycle reading of ε_K:")
print()
print(f"  Cycle: rank={rank} → N_c={N_c} → g={g} → M_g={M_g} → +rank·n_C → N_max={N_max}")
print(f"  Closing shift: rank·n_C = {rank*n_C} = {N_max} - {M_g}")
print()

# Reading A: residual ratio squared
A = (rank * n_C / N_max) ** 2
print(f"(A) (rank·n_C / N_max)² = {rank*n_C}/{N_max} squared = {A:.4e}")
print(f"    vs ε_K = {eps_K_obs:.3e} — ratio {A/eps_K_obs:.2f}x")

# Reading B: log residual squared
B = math.log(N_max / M_g) ** 2
print(f"(B) log²(N_max/M_g) = log²({N_max}/{M_g}) = {B:.4e}")
print(f"    vs ε_K = {eps_K_obs:.3e} — ratio {B/eps_K_obs:.2f}x")

# Reading C: Chern over N_max² (= Toy 2338 finding, re-expressed)
C = chern_sum / N_max ** 2
print(f"(C) chern_sum / N_max² = {chern_sum}/{N_max**2} = {C:.4e}")
print(f"    vs ε_K = {eps_K_obs:.3e} — ratio {C/eps_K_obs:.2f}x  ✓")

# Check (C) precision
err_C = abs(C - eps_K_obs) / eps_K_obs * 100
check("(C) Chern-Mersenne form matches ε_K at <1%", err_C < 1.0)

# Connect (A) and (C) algebraically
# (rank·n_C)² = 100. chern_sum = 42. 100/42 = 50/21 ≈ 2.38
# Reading A = (rank·n_C)²/N_max² = chern_sum/N_max² · (rank·n_C)²/chern_sum
#           = C · (100/42) = C · 50/21
print()
print(f"Algebraic bridge: Reading A = Reading C · (rank·n_C)²/chern_sum")
print(f"  = {C:.4e} · ({rank*n_C}²/{chern_sum}) = {C * (rank*n_C)**2 / chern_sum:.4e}")
print(f"  (which equals reading A = {A:.4e})")
print()

# ============================================================
# INSTINCT: which reading is "the" answer?
# ============================================================

print(f"=" * 65)
print("INSTINCT")
print(f"=" * 65)
print(f"""
Reading (C) — chern_sum/N_max² — matches ε_K at 0.4%.
Reading (A) — (rank·n_C/N_max)² — is bigger by factor ~2.4.
Reading (B) — log²(N_max/M_g) — is bigger by factor ~2.6.

The cycle structure gives the FRAMEWORK for ε_K: a 4-step closure
where the residual lands in N_max² denominator. The numerator
42 = chern_sum could come from EITHER:
  - the Chern characteristic class (Toy 2338 interpretation)
  - or the "loop function" evaluated at the cycle's anchor points

Both readings are consistent. The cycle picture says:
  "ε_K = (cycle's Chern-class invariant) / (cycle's spectral cap²)"

This is the same identity (2) found, just dressed in cycle language.
The cycle is a 4-step Mersenne-closure walk on BST's integer lattice;
the box-diagram is a 4-step closed propagator loop. They live at the
same abstract structure: "closed 4-step path on the geometric base
with topological invariant in numerator and cap² in denominator."

(1) and (2) give the SAME answer via different visualizations.
""")

# Score
passed = sum(1 for ok, *_ in tests if ok)
total = len(tests)
print(f"Toy 2340 score: {passed}/{total}")
print()
print(f"VERDICT: Closed Mersenne cycle (1) confirms (2) Bergman 4-point")
print(f"finding. Same identity, two pictures. ε_K = chern_sum/N_max² = α²·42.")
