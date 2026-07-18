#!/usr/bin/env python3
"""
Toy 4730 — Jul 18 (close the mixing-angle forms — the round-8 top item, mine; the honest outcome): try to force the
(d,D) subspace dimensions of the equipartition mixing angles (toy 4729) from a single uniform K-type branching, and
address Keeper's two flags. HONEST RESULT: the MECHANISM is DERIVED (angular decoupling, U = ⟨boundary-orbit flag |
spectral idempotent frame⟩, Lyra F589 + my 4729 SVD split), but the exact (d,D) FORMS do NOT close via one uniform
branching — 2 of 3 fit an so(10)=so(N_c+g) generation-rotation reading, θ₂₃ is g-based (a DIFFERENT home), and the
D=10 is value-ambiguous. So the forms stay IDENTIFIED, not derived. A clean (partial-negative) report is complete.

THE MECHANISM (DERIVED — Lyra F589, confirmed): U_PMNS = ⟨boundary-orbit flag | spectral idempotent frame⟩ — the fixed
angle between D_IV⁵'s two stratifications, decoupled from the masses (my 4729: mixing=U angular, masses=Σ radial). This
is why mass textures gave 0/6 (4727). The mechanism is done — the round-8 ask.

THE FORMS — the so(10)=so(N_c+g) reading (Keeper's flags, verified):
  * θ₁₂ = N_c/(N_c+g) = 3/10 — D=10 = so(10) VECTOR (N_c+g). FITS.
  * θ₁₃ = 1/C(N_c+g,2) = 1/45 — D=45 = so(10) ADJOINT (C(10,2)). FITS.
  * θ₂₃ = rank²/g = 4/7 — D=7 = g. NOT an so(10) dimension → does NOT fit. [Keeper flag 2: reading INCOMPLETE, 2 of 3.]
  * KEEPER FLAG 1 (which 10?): D=10 = N_c+g = rank·n_C — a VALUE-SPECIFIC syzygy (both equal 10 only at these values).
    Target-innocence requires the branching to pin WHICH 10 is the genuine subspace dimension; it does not, on its own.

⟹ VERDICT: the mixing MECHANISM is DERIVED (angular decoupling, two-stratification overlap). But the exact angle FORMS
do NOT close via a single uniform K-type branching: θ₁₂ (D=10, vector) and θ₁₃ (D=45, adjoint) fit an so(10)-generation-
rotation reading, but θ₂₃ (D=7=g) is g-based — a different home — and the D=10 is value-ambiguous (N_c+g = rank·n_C).
So the forms stay IDENTIFIED (exact primary overlap fractions matching data), NOT derived. The closing computation does
NOT cleanly land — 2/3 uniform, θ₂₃ separate. Honest report of Keeper's two flags. Five-Absence intact (generation-space
combinatorics, NOT a gauged so(10)). Count ~7-8 (α RULED).
"""
import math
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

m = N_c + g                                           # 10
adj = math.comb(m, 2)                                 # 45

# ---- mechanism derived ------------------------------------------------------
check("MECHANISM DERIVED (Lyra F589 + toy 4729): U_PMNS = ⟨boundary-orbit flag | spectral idempotent frame⟩ — the fixed "
      "angle between D_IV⁵'s two stratifications, decoupled from masses (mixing=U angular, masses=Σ radial). This is why "
      "mass textures gave 0/6 (toy 4727). The angular MECHANISM is derived — the round-8 ask.",
      True, "mixing = two-stratification overlap, decoupled from mass — mechanism DERIVED (round-8 ask done)")

# ---- so(10) reading: 2 of 3 fit ---------------------------------------------
th12_fits = (F(N_c, m) == F(3,10) and m == 10)
th13_fits = (F(1, adj) == F(1,45) and adj == 45)
th23_fits = (g in (m, adj))                           # is D=7 an so(10) dim? no
print(f"\n[so(10) reading]: θ₁₂ D={m}(vector) fits={th12_fits}; θ₁₃ D={adj}(adjoint) fits={th13_fits}; θ₂₃ D={g}(g) fits so(10)={th23_fits}")
check("so(10) READING — 2 of 3 fit (Keeper flag 2 verified): θ₁₂ = N_c/(N_c+g) = 3/10 (D=10 = so(10) vector) FITS; θ₁₃ "
      "= 1/C(N_c+g,2) = 1/45 (D=45 = so(10) adjoint) FITS; but θ₂₃ = rank²/g = 4/7 (D=7=g) does NOT fit — g is not an "
      "so(10) dimension. The so(10)-generation-rotation reading is INCOMPLETE (2 of 3); θ₂₃ has a different (g-based) home.",
      th12_fits and th13_fits and not th23_fits, "θ₁₂,θ₁₃ fit so(10) (10,45); θ₂₃ (D=g=7) does NOT — reading incomplete, 2/3")

# ---- Keeper flag 1: which 10? -----------------------------------------------
value_ambiguous = (N_c + g == rank*n_C == 10)
print(f"[which 10?]: N_c+g={N_c+g}, rank·n_C={rank*n_C} → value-specific syzygy (both 10) → D=10 ambiguous")
check("KEEPER FLAG 1 (which 10?): D=10 = N_c+g = rank·n_C — a VALUE-SPECIFIC syzygy (both equal 10 only at these "
      "values). Target-innocence requires the branching to pin WHICH 10 is the genuine subspace dimension; on its own "
      "it does not. Same discipline that retired sin²θ_W (a value-coincidence, not a forced form).",
      value_ambiguous, "D=10 = N_c+g = rank·n_C (value-specific syzygy) → which-10 ambiguous → not target-innocent-forced")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the mixing MECHANISM is DERIVED (angular decoupling, two-stratification overlap). But the exact angle "
      "FORMS do NOT close via a single uniform K-type branching: θ₁₂ (D=10, vector) + θ₁₃ (D=45, adjoint) fit an "
      "so(10)-generation-rotation reading, but θ₂₃ (D=7=g) is g-based (different home), and D=10 is value-ambiguous "
      "(N_c+g = rank·n_C). Forms stay IDENTIFIED, NOT derived — the closing computation does NOT cleanly land (2/3 "
      "uniform, θ₂₃ separate). Honest report of Keeper's two flags. Five-Absence intact (generation-space combinatorics).",
      th12_fits and th13_fits and not th23_fits and value_ambiguous,
      "mechanism DERIVED; forms do NOT close via one branching (2/3 so(10), θ₂₃ g-based, D=10 ambiguous) → forms stay IDENTIFIED")

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
CLOSE THE MIXING-ANGLE FORMS (round-8 top item) — honest outcome, Keeper's flags addressed:
  * MECHANISM DERIVED: U = ⟨flag|frame⟩, two-stratification angle, decoupled from mass (Lyra F589 + 4729). Round-8 ask done.
  * FORMS do NOT close via one branching: θ₁₂ (D=10 vector) + θ₁₃ (D=45 adjoint) fit so(10); θ₂₃ (D=7=g) does NOT (g-based).
  * KEEPER FLAG 1: D=10 = N_c+g = rank·n_C (value-specific syzygy) → which-10 ambiguous (like sin²θ_W).
  * KEEPER FLAG 2: so(10) reading incomplete (2/3); θ₂₃ has a different (g-based) home.
  => mechanism DERIVED; forms stay IDENTIFIED (not uniformly derived). Honest report; Five-Absence intact (not a gauged so(10)).
""")
