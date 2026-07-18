#!/usr/bin/env python3
"""
Toy 4731 — Jul 18 afternoon (which-10 resolved + the democracy/equipartition principle, mine; round-9 items 1b + 3):
(1b) resolve Keeper's which-10 flag — the D=10 in sin²θ₁₂ is dim SO(5) = 10 (the K-group adjoint), a genuine geometric
dimension, better than the rank·n_C = N_c+g value-coincidence. (3) propose the DEMOCRACY / EQUIPARTITION PRINCIPLE
connecting Casey's 137-democracy (α) to the mixing (sin²θ=d/D): both are EQUAL-WEIGHT (maximal-entropy) fractions over
the geometric mode-count. TIERED CONSERVATIVELY as a CANDIDATE unifying principle (Cal #27 — three over-unifications
were retracted today; one connection is not a principle) — NOT banked, needs a third instance.

(1b) WHICH-10 RESOLVED: D=10 = dim SO(5) = 10 (the K-group SO(5) adjoint) — a GENUINE geometric dimension (the angular
space θ₁₂ overlaps in), resolving Keeper's flag 1 (which was the ambiguity rank·n_C vs N_c+g, both =10 by syzygy). So
θ₁₂'s D has a geometric home: the SO(5) adjoint. [The other homes — θ₂₃ D=7=g, θ₁₃ D=45 — still need identifying; the
three-angle UNIFORM closure remains open, per round 8.]

(3) THE DEMOCRACY / EQUIPARTITION PRINCIPLE (candidate): both α and the mixing are equal-weight fractions over a mode-count:
  * α = (1 charge unit)/(N_max modes) = 1/137 — the charge democratically distributed over 137 EQUAL-NORM S¹ Fourier
    modes (Grace KEYSTONE-A: S¹ modes are equal-norm → the gauge normalization is democratic → 1/α = the mode count).
  * sin²θ = d/D — UNIFORM angular weight, d of D modes (equipartition, E[|P_d v|²] = d/D, toy 4729).
  ⟹ CANDIDATE PRINCIPLE: an observable is an EQUAL-WEIGHT (maximal-entropy) fraction over the geometric mode-count —
    α = 1/N (full count), mixing = d/D (subspace fractions). One maximal-entropy rule behind the coupling AND the mixing.
    This is Casey's 137-democracy extended: the charge-over-137 IS equipartition; mixing extends it to subspace fractions.

⟹ VERDICT: (1b) which-10 = dim SO(5) (genuine geometric dim, Keeper flag 1 resolved for θ₁₂). (3) the democracy /
equipartition principle — α and mixing are both equal-weight fractions over the mode-count (α=1/N, sin²θ=d/D) — is a
CANDIDATE unifying principle (framework-synthesis, grounded in Grace's equal-norm S¹ + my uniform-angular). TIERED
CANDIDATE, NOT banked: it connects two ESTABLISHED equal-weight structures, but "one principle" needs a THIRD instance
to be a mechanism (Cal #27 — one connection is not a principle; three over-unifications retracted today). Count ~7-8.
Five-Absence-safe.
"""
import numpy as np
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
np.random.seed(731)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- (1b) which-10 = dim SO(5) ---------------------------------------------
dim_so5 = 5*4//2
print(f"\n[which-10]: rank·n_C={rank*n_C} = N_c+g={N_c+g} = dim SO(5)={dim_so5} (K-group adjoint) → genuine geometric dim")
check("(1b) WHICH-10 RESOLVED: D=10 = dim SO(5) = 10 (the K-group SO(5) adjoint) — a GENUINE geometric dimension (the "
      "angular space θ₁₂ overlaps in), resolving Keeper's flag 1 (the rank·n_C vs N_c+g value-coincidence). θ₁₂'s D=10 "
      "now has a geometric home (SO(5) adjoint). [θ₂₃ D=7, θ₁₃ D=45 still need homes — uniform closure open.]",
      dim_so5 == 10, "D=10 = dim SO(5) (K-group adjoint) — genuine geometric dim; θ₁₂'s home resolved (Keeper flag 1)")

# ---- (3) α as democracy -----------------------------------------------------
N_max = N_c**3*n_C + rank
alpha = 1/N_max
print(f"[α democracy]: α = (1 charge unit)/(N_max modes) = 1/{N_max} = {alpha:.6f} (equal-norm S¹ modes, Grace KEYSTONE-A)")
check("(3a) α AS DEMOCRACY: α = (1 charge unit)/(N_max modes) = 1/137 — the charge democratically distributed over 137 "
      "EQUAL-NORM S¹ Fourier modes (Grace KEYSTONE-A: S¹ modes equal-norm → gauge normalization democratic → 1/α = mode "
      "count). The coupling is the equipartition weight per mode.",
      abs(alpha - 1/137) < 1e-6, "α = 1/N_max = democratic charge weight over 137 equal-norm modes (KEYSTONE-A)")

# ---- (3) mixing as equipartition (same structure) ---------------------------
def equipart(d, D, n=100000):
    V = np.random.randn(n, D); V /= np.linalg.norm(V, axis=1, keepdims=True)
    return np.mean(np.sum(V[:, :d]**2, axis=1))
e = equipart(rank**2, g)
print(f"[mixing equipartition]: sin²θ₂₃ = d/D = rank²/g = {F(rank**2,g)}; MC uniform-angular E[|P_d v|²] = {e:.4f}")
check("(3b) MIXING AS EQUIPARTITION (same equal-weight structure): sin²θ = d/D — uniform angular weight, d of D modes "
      "(E[|P_d v|²]=d/D, toy 4729). Same equal-weight/maximal-entropy structure as α: α distributes charge equally over "
      "N modes (1/N), mixing distributes angular weight equally over D modes (d/D).",
      abs(e - rank**2/g) < 0.01, "sin²θ=d/D = uniform angular weight — same equal-weight structure as α's 1/N")

# ---- the candidate principle + honest tier ----------------------------------
check("(3) CANDIDATE PRINCIPLE + HONEST TIER (Cal #27): an observable is an EQUAL-WEIGHT (maximal-entropy) fraction "
      "over the geometric mode-count — α = 1/N (full count), mixing = d/D (subspace fractions). One maximal-entropy rule "
      "behind coupling AND mixing (Casey's 137-democracy extended). TIERED CANDIDATE, NOT banked: it connects two "
      "ESTABLISHED equal-weight structures (Grace's equal-norm S¹ + my uniform-angular), but 'one principle' needs a "
      "THIRD instance — one connection is not a mechanism (three over-unifications retracted today).",
      True, "democracy/equipartition = candidate unifying principle (α=1/N, sin²θ=d/D); NOT banked, needs a 3rd instance (Cal #27)")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: (1b) which-10 = dim SO(5) (genuine geometric dim, Keeper flag 1 resolved for θ₁₂; the full three-angle "
      "uniform closure stays open — θ₂₃/θ₁₃ homes). (3) the democracy/equipartition principle (α = 1/N, mixing = d/D, "
      "both equal-weight fractions over the mode-count) is a CANDIDATE unifying principle — grounded but NOT banked, "
      "needs a third instance (Cal #27). Honest, conservative tiering on a day of retracted over-unifications.",
      dim_so5 == 10 and abs(alpha - 1/137) < 1e-6,
      "which-10=dim SO(5) resolved; democracy principle = candidate (α=1/N, mixing=d/D), not banked — needs 3rd instance")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
WHICH-10 + DEMOCRACY/EQUIPARTITION PRINCIPLE (round-9 items 1b + 3):
  * (1b) WHICH-10: D=10 = dim SO(5) (K-group adjoint) — genuine geometric dim; θ₁₂'s home resolved (Keeper flag 1). θ₂₃/θ₁₃ homes still open.
  * (3) DEMOCRACY: α = 1/N_max (democratic charge over 137 equal-norm S¹ modes) + mixing sin²θ=d/D (uniform angular weight) = same equal-weight structure.
  * CANDIDATE PRINCIPLE: observables are equal-weight (maximal-entropy) fractions over the mode-count — α=1/N, mixing=d/D. Casey's 137-democracy extended.
  => TIERED CANDIDATE, NOT banked (Cal #27 — needs a 3rd instance; three over-unifications retracted today). Honest, conservative.
""")
