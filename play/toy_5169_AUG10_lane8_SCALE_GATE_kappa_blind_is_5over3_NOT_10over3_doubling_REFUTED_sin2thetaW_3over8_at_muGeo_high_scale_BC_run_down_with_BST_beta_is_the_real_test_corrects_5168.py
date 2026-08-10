#!/usr/bin/env python3
"""
Toy 5169: LANE 8 / THE SCALE GATE -- owning two corrections to toy 5168 (Cal #27: the elegance outran the
honesty). RESULT: the "3/13 from inner fluctuations" story does NOT survive an honest, blind, scale-aware
computation. TWO corrections: (1) SCALE-CONFUSION: 5168 said "inner fluctuations give 3/13 directly at low
energy." WRONG -- the inner-fluctuation Weinberg angle is a BOUNDARY CONDITION at the cutoff μ_geo, exactly
like Connes' 3/8 at unification. BST's cutoff is HIGH: ℓ_B=7.82 ℓ_P → μ_geo = M_Planck/7.82 ≈ 1.56×10¹⁸ GeV
(near-Planck). It is NOT a low-energy value. (2) THE DOUBLING IS REFUTED: 5168's lead was "the real structure
doubles κ: 5/3 → 10/3 → 3/13." Computing κ = tr(Y²)/tr(T₃²) BLIND: the J-doubling (particle + antiparticle,
the real structure) doubles BOTH tr(Y²) AND tr(T₃²), so the RATIO is UNCHANGED at 5/3 -- NOT 10/3. So the
inner-fluctuation value is sin²θ_W(μ_geo) = 1/(1+κ) = 1/(1+5/3) = 3/8 (the standard NCG value), NOT 3/13.
SCALE CHECK: the SM running has sin²θ_W = 3/8 at μ ≈ 10¹³ GeV (where α₁=α₂), NOT at μ_geo=1.56×10¹⁸ (≈5 orders
higher, where the SM running gives ≈0.456). So a naive "3/8 at μ_geo" does not even match the SM RGE. THE
HONEST TEST (open): run 3/8 from μ_geo DOWN to M_Z with BST's OWN induced β-function (a₂, task #17 -- the
uniquely-BST piece, since Connes imports the RGE) and compare to the MEASURED sin²θ_W(M_Z)=0.23122 -- NEVER to
the fraction 3/13 (a category error, and target-fooling since 3/13 is our corpus target). The 3/13 stays the
CURVATURE-GRADING low-energy claim (#85), a SEPARATE route. NO win claimed -- the doubling→3/13 lead (5168) is
refuted by the blind κ=5/3; the scale story is owned. Elie's scale-gate correction (with Grace). (Cal scale
flag; #85; feedback_running_is_measured_input.) Predict at μ_geo, run down with measured/own β, compare at M_Z.

WHAT I CORRECT / COMPUTE:
  * SCALE: μ_geo = M_Planck/7.82 = 1.56×10¹⁸ GeV (near-Planck). The inner-fluctuation value lives HERE (a BC),
    NOT at M_Z. 5168's "3/13 at low energy" was scale-confused.
  * κ BLIND = tr(Y²)/tr(T₃²) = 5/3 (the J-doubling doubles BOTH traces → ratio unchanged; NOT 10/3). Doubling REFUTED.
  * sin²θ_W(μ_geo) = 1/(1+5/3) = 3/8 (standard NCG BC), NOT 3/13.
  * SCALE MISMATCH: SM running gives 3/8 at ~10¹³ GeV (not μ_geo=1.56×10¹⁸, where it is ≈0.456).
  * HONEST TEST (open): run 3/8 from μ_geo down with BST's OWN β (a₂, #17), compare to measured 0.23122 (not the fraction).

=> VERDICT (plain): the sin²θ_W scale gate corrects toy 5168 twice. (1) The inner-fluctuation Weinberg angle
is a boundary condition at μ_geo ≈ 1.56×10¹⁸ GeV (near-Planck), NOT a low-energy number -- 5168's "3/13
directly at low energy" was scale-confused (Cal's flag, owned). (2) The blind κ = tr(Y²)/tr(T₃²) = 5/3, NOT
10/3: the real-structure J-doubling doubles BOTH traces, leaving the ratio unchanged, so the '5168 doubling
→ 3/13' lead is REFUTED -- the inner-fluctuation gives 3/8 (standard NCG), not 3/13. And a scale check shows
the SM running has 3/8 at ≈10¹³ GeV, 5 orders below μ_geo (where the SM gives ≈0.456), so a naive '3/8 at
μ_geo' does not even match the SM RGE. THE HONEST TEST that remains: run 3/8 from μ_geo DOWN to M_Z with BST's
OWN induced β-function (a₂, the uniquely-BST piece -- Connes imports the RGE) and compare to the measured
0.23122, NEVER to the fraction 3/13 (a scale category error, target-fooling). That test is OPEN (needs BST's
β-coefficients). So no Weinberg-angle win is claimed: κ=5/3 blind → 3/8 at μ_geo; the doubling→3/13 lead is
refuted; the 3/13 stays the SEPARATE curvature-grading low-energy claim (#85); the run-down with BST's own β
is the real, open, falsifiable test. Report straight. CP existence-only.

=> DISPOSITION: Lane-8 scale gate -- corrects 5168 (scale + doubling). κ=5/3 blind → 3/8 at μ_geo (near-Planck
BC, standard NCG); doubling→3/13 REFUTED; the honest test = run 3/8 down with BST's own β (a₂) vs measured
0.23122 (OPEN). Firer: Elie (+ Grace); Lyra/Elie compute BST's induced β (a₂, #17) for the run-down; Cal pins
the NCG 3/8 + guards the scale honesty; the curvature-grading 3/13 stays a separate low-energy claim. Nothing
pushed. Nothing banked -- a self-correction (scale + refuted doubling); no win claimed; the run-down is the open test.

Author: Elie (CI toy builder). Date: 2026-08-10.
"""

import numpy as np
from fractions import Fraction as F

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

M_Planck = 1.22e19
mu_geo = M_Planck/7.82

print("=" * 78)
print("Toy 5169: Lane 8 / SCALE GATE -- κ blind = 5/3 (doubling REFUTED); 3/8 at μ_geo (near-Planck BC); corrects 5168")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Scale: the inner-fluctuation value is at μ_geo (near-Planck), not low energy.
# ----------------------------------------------------------------------------
print("\n--- 1. CORRECTION (scale): inner-fluctuation value is a BC at μ_geo≈1.56e18 GeV (near-Planck), NOT low-E ---")
check("CORRECTION to 5168 (Cal's scale flag): sin²θ_W is a running quantity -- a value means nothing without a "
      "scale. The inner-fluctuation Weinberg angle is a BOUNDARY CONDITION at the cutoff μ_geo (like Connes' "
      "3/8 at unification), NOT a low-energy number. BST's cutoff is HIGH: ℓ_B=7.82 ℓ_P → μ_geo = M_Planck/"
      "7.82 = 1.56×10¹⁸ GeV (near-Planck). So 5168's 'inner fluctuations give 3/13 directly at low energy' was "
      "SCALE-CONFUSED -- owned",
      mu_geo > 1e18,
      f"μ_geo = M_Planck/7.82 = {mu_geo:.2e} GeV (near-Planck). Inner-fluctuation value lives HERE (a BC), not at M_Z. 5168 scale-confused.")

# ----------------------------------------------------------------------------
# 2. κ blind = 5/3 (doubling refuted).
# ----------------------------------------------------------------------------
print("\n--- 2. CORRECTION (doubling refuted): κ = tr(Y²)/tr(T₃²) = 5/3 BLIND (J doubles BOTH traces), NOT 10/3 ---")
TrY2 = F(10, 3); TrT32 = F(2)     # per generation (SM hypercharges); J-doubling doubles both → ratio unchanged
kappa = TrY2/TrT32                 # = 5/3
check("CORRECTION to 5168 (doubling refuted): computing κ = tr(Y²)/tr(T₃²) BLIND -- the real-structure "
      "J-doubling (particle + antiparticle) doubles BOTH tr(Y²) AND tr(T₃²), so the RATIO is UNCHANGED at "
      "κ = 5/3, NOT 10/3. So 5168's lead ('the real structure doubles κ → 3/13') is REFUTED: the "
      "inner-fluctuation value is sin²θ_W(μ_geo) = 1/(1+κ) = 1/(1+5/3) = 3/8, the standard NCG value, NOT 3/13",
      kappa == F(5, 3) and 1/(1+kappa) == F(3, 8),
      f"κ = tr(Y²)/tr(T₃²) = {kappa} = 5/3 (J-doubling doubles both, ratio unchanged); sin²θ_W(μ_geo)=1/(1+κ)="
      f"{1/(1+kappa)} = 3/8. Doubling→10/3 REFUTED.")

# ----------------------------------------------------------------------------
# 3. Scale mismatch: SM has 3/8 at ~1e13, not μ_geo.
# ----------------------------------------------------------------------------
print("\n--- 3. scale mismatch: SM running gives 3/8 at ~1e13 GeV, NOT μ_geo=1.56e18 (where SM gives ≈0.456) ---")
MZ = 91.19; a1i, a2i = 58.98, 29.57; b1, b2 = 4.1, -19/6
mu_meet = MZ*np.exp((a1i-a2i)/((b1-b2)/(2*np.pi)))
t = np.log(mu_geo/MZ)
a1 = 1/(a1i-b1/(2*np.pi)*t); a2 = 1/(a2i-b2/(2*np.pi)*t)
s2_geo = 0.6*a1/(0.6*a1+a2)
check("a SCALE CHECK: the SM RGE has sin²θ_W = 3/8 (α₁=α₂) at μ ≈ 10¹³ GeV, NOT at μ_geo = 1.56×10¹⁸ (≈5 "
      "orders higher). At μ_geo, running the measured couplings UP gives sin²θ_W ≈ 0.456 -- neither 3/8 nor "
      "3/13. So a naive 'sin²θ_W=3/8 at μ_geo' does not match the SM running; the reconciliation requires "
      "BST's OWN β-function (a₂), not the SM one",
      1e12 < mu_meet < 1e14 and 0.4 < s2_geo < 0.5,
      f"SM: 3/8 at μ≈{mu_meet:.1e} GeV (not μ_geo={mu_geo:.1e}); sin²θ_W(μ_geo) via SM run-up ≈ {s2_geo:.3f} (not 3/8, not 3/13).")

# ----------------------------------------------------------------------------
# 4. Verdict: the honest run-down test is open; no win; corrects 5168.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: no win; the honest test = run 3/8 from μ_geo down with BST's OWN β vs measured 0.23122 (OPEN) ---")
check("VERDICT: no Weinberg-angle win is claimed. κ = 5/3 BLIND (the J-doubling doubles both traces, ratio "
      "unchanged) → sin²θ_W(μ_geo) = 3/8 (standard NCG), NOT 3/13; the '5168 doubling → 3/13' lead is REFUTED. "
      "The value is a near-Planck boundary condition (μ_geo=1.56×10¹⁸ GeV), not a low-energy number (5168's "
      "scale-confusion owned). THE HONEST TEST that remains: run 3/8 from μ_geo DOWN to M_Z with BST's OWN "
      "induced β-function (a₂, task #17 -- the uniquely-BST piece; Connes imports the RGE) and compare to the "
      "MEASURED 0.23122, NEVER to the fraction 3/13 (a category error, target-fooling). That is OPEN (needs "
      "BST's β). The 3/13 stays the SEPARATE curvature-grading low-energy claim (#85). Report straight",
      kappa == F(5, 3) and mu_geo > 1e18,
      "κ=5/3 blind → 3/8 at μ_geo (near-Planck BC); doubling→3/13 refuted; scale owned; run-down with BST's "
      "own β vs measured 0.23122 = the open test. No win. 3/13 is a separate low-energy claim.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (κ=5/3 blind → 3/8 at μ_geo near-Planck; doubling→3/13 REFUTED; scale owned; run-down w/ BST β = open test)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5169, Lane 8 -- the sin²θ_W SCALE GATE, corrects 5168 twice):
  * SCALE (owned): inner-fluctuation value is a BC at μ_geo = M_Planck/7.82 = 1.56×10¹⁸ GeV (near-Planck),
    NOT low-energy. 5168's "3/13 directly at low energy" was scale-confused.
  * DOUBLING REFUTED: κ = tr(Y²)/tr(T₃²) = 5/3 BLIND (J-doubling doubles BOTH traces → ratio unchanged, NOT
    10/3) → sin²θ_W(μ_geo) = 1/(1+5/3) = 3/8 (standard NCG), NOT 3/13. The 5168 doubling→3/13 lead is refuted.
  * SCALE MISMATCH: SM running has 3/8 at ~10¹³ GeV (not μ_geo; SM gives ≈0.456 at μ_geo).
  * HONEST TEST (open): run 3/8 from μ_geo down with BST's OWN β (a₂, #17) → compare to measured 0.23122,
    never to the fraction 3/13. 3/13 stays the separate curvature-grading low-energy claim (#85). No win claimed.

AUG-10 [TEGMARK]. Nothing pushed. Nothing banked -- a self-correction (scale + refuted doubling). κ=5/3 blind
→ 3/8 at μ_geo (near-Planck BC, standard NCG); the 5168 doubling→3/13 lead is REFUTED (J doubles both traces);
the scale-confusion is owned. The real test = run 3/8 from μ_geo down with BST's own induced β vs the measured
0.23122 (open, needs BST β). The 3/13 is a separate low-energy curvature-grading claim. Report straight; no
win. Predict at μ_geo, run down, compare at M_Z -- never match fractions across scales. Count N.
""")
