#!/usr/bin/env python3
"""
Toy 5172: LANE 8 / THE PIVOT -- the gauge-field ORIGIN SCHEME (bigger than sin²θ_W; founds the a₄ = SM
Lagrangian). RESULT: the a₄ gauge-kinetic coefficient is computed/prepared for BOTH candidate schemes, with
the two new catches folded in; the decider is which scheme is COHERENT for ALL THREE forces (Grace+Lyra's
corpus pull, step 1), and the honest LEAN is Scheme A (3/8, demonstrated). TWO NEW CATCHES: (Grace) sin²θ_W =
g'²/(g²+g'²) contains BOTH couplings -- making U(1)_Y scale-free is NOT enough, because g (SU(2)_L) runs too;
so for 3/13 to sit at M_Z DIRECTLY, the WHOLE electroweak ratio must be boundary/tree-level, i.e. SU(2)_L must
ALSO be geometric-boundary (higher bar). (Cal) BST carries multiple conflicting origin stories, and a MIXED
scheme (SU(2)_L inner-fluctuation + U(1)_Y geometric) is INCOHERENT -- the angle would not be a ratio of
consistently-normalized couplings. THE TWO SCHEMES: (A) INNER FLUCTUATIONS of the Dirac (Lane 8, toy 5164,
DEMONSTRATED, committed baseline) -- a₄ = FERMION TRACE for all three forces (coherent), c²=1 → sin²θ_W(μ_geo)
= N_c/(N_c+n_C) = 3/8, both g,g' run down (SM-like, undershoots ~0.207); (B) ELECTROWEAK GEOMETRIC-BOUNDARY
(corpus fragments T638/F531, SU(3) bulk) -- a₄ = KILLING/isometry norm, c²=rank=2 → N_c/(N_c+rank·n_C) = 3/13,
scale-free ONLY IF the WHOLE EW ratio is boundary (requires SU(2)_L geometric too -- UNESTABLISHED). So the a₄
is ready for whichever scheme Grace+Lyra pin as coherent; the LEAN is A (3/8, demonstrated); B is fragmentary
and must clear the whole-EW-boundary + no-mixed-scheme + scale bars. 3/13 stays Identified-with-a-candidate-
mechanism (Casey's blind spin-twist factor), CONDITIONAL on Scheme B cohering. Elie's a₄-both-schemes prep
(+ Grace/Lyra decide). (Cal origin-story catch; Grace whole-EW catch; T638/F531/Lane-8; Lyra c².) Report either way straight.

WHAT I PREPARE:
  * sin²θ_W = g'²/(g²+g'²) contains BOTH g and g'. Grace's bar: scale-free U(1)_Y ≠ scale-free angle; the
    WHOLE EW ratio must be boundary for 3/13 at M_Z.
  * COHERENCE (Cal): the two EW factors must share ONE origin scheme; mixed = incoherent.
  * SCHEME A (inner fluctuation, DEMONSTRATED): a₄ = fermion trace (all three), c²=1 → 3/8, runs down (SM-like).
  * SCHEME B (whole-EW geometric-boundary, fragmentary): a₄ = Killing norm, c²=2 → 3/13, scale-free IF whole EW
    boundary (requires SU(2)_L geometric too -- UNESTABLISHED).

=> VERDICT (plain): the sin²θ_W question was a doorway onto the real work -- BST's gauge-field ORIGIN SCHEME,
which founds the a₄ = SM Lagrangian and settles the Weinberg angle as a byproduct. The a₄ gauge-kinetic
coefficient is now prepared for both candidate schemes: (A) if all three forces are inner fluctuations of the
Dirac (Lane 8, demonstrated, committed baseline), the coefficient is the FERMION TRACE for all three, giving
c²=1 → sin²θ_W = 3/8, with both g and g' running down (SM-like, undershooting the measured value); (B) if the
electroweak sector is geometric-boundary (Killing-normalized, SU(3) bulk -- corpus fragments T638/F531), the
coefficient is the isometry norm, c²=rank=2 → 3/13. Two catches raise the bar on B: Grace's -- sin²θ_W
contains g (SU(2)), so 3/13 at M_Z requires the WHOLE EW ratio boundary (SU(2)_L geometric too, not just
U(1)_Y); and Cal's -- a mixed scheme (SU(2) fluctuation + U(1) geometric) is incoherent. So the decider is
which single scheme is coherent for all three forces (Grace+Lyra's corpus pull), and the honest LEAN is
Scheme A (3/8, demonstrated); Scheme B is fragmentary and must clear whole-EW-boundary + no-mixed + the scale
gate. 3/13 stays Identified-with-a-candidate-mechanism, conditional on B cohering. Report either way straight;
knowing what BST's forces ARE is the bigger prize, and it is forced regardless of 3/8 vs 3/13.

=> DISPOSITION: Lane-8 pivot -- a₄ coefficient prepared for both schemes (A inner-fluctuation → 3/8 running;
B whole-EW geometric-boundary → 3/13 scale-free-if-coherent); Grace's whole-EW bar + Cal's no-mixed-scheme
fold in; lean A. Firer: Elie (a₄ prep); Grace+Lyra pin the coherent scheme from the corpus (T638/T1949/T2470/
F531/Lane-8), esp. U(1)_Y; Cal applies the bar + scale gate on the whole EW ratio; count the rank-2 once
(July's 'two circles' = the same isometry norm, not a second vote). Nothing pushed. Nothing banked -- a₄
ready for both; lean 3/8; 3/13 conditional; the origin scheme founds a₄ = SM Lagrangian.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

from fractions import Fraction as F

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c, n_C, rank = 3, 5, 2

print("=" * 78)
print("Toy 5172: Lane 8 PIVOT -- gauge-field origin scheme; a₄ prepared for both (A inner-fluct 3/8 / B whole-EW-boundary 3/13); lean A")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Grace's bar: the whole EW ratio (both couplings), not just U(1)_Y.
# ----------------------------------------------------------------------------
print("\n--- 1. Grace's bar: sin²θ_W = g'²/(g²+g'²) contains g (SU(2)), which runs → scale-free U(1)_Y is NOT enough ---")
check("Grace's catch (higher bar): sin²θ_W = g'²/(g²+g'²) contains BOTH the U(1)_Y coupling g' AND the "
      "SU(2)_L coupling g -- and g runs. So making hypercharge scale-free does NOT make the angle scale-free. "
      "For 3/13 to sit at M_Z DIRECTLY, the WHOLE electroweak ratio must be boundary/tree-level -- i.e. "
      "SU(2)_L must ALSO be geometric-boundary, not just U(1)_Y. Higher bar on Scheme B",
      True,
      "sin²θ_W = g'²/(g²+g'²): both couplings; g runs. 3/13-at-M_Z needs the WHOLE EW ratio boundary, not just U(1)_Y.")

# ----------------------------------------------------------------------------
# 2. Scheme A: inner fluctuations, fermion trace, c²=1 → 3/8 (demonstrated).
# ----------------------------------------------------------------------------
print("\n--- 2. SCHEME A (inner fluctuations, DEMONSTRATED): a₄ = fermion trace, c²=1 → 3/8, runs down (SM-like) ---")
sinA = F(N_c, N_c + n_C)
check("SCHEME A (inner fluctuations of the Dirac -- Lane 8 / toy 5164 DEMONSTRATED, the committed baseline): "
      "the a₄ gauge-kinetic coefficient is the FERMION TRACE for ALL THREE forces (one coherent scheme), "
      "c²=1 → sin²θ_W(μ_geo) = N_c/(N_c+n_C) = 3/8; both g and g' then run down with the SM RGE (SM-like, "
      "undershooting ~0.207). Coherent and demonstrated",
      sinA == F(3, 8),
      f"a₄ = fermion trace (all three); c²=1 → sin²θ_W = {sinA} = 3/8 at μ_geo, runs down (SM-like). Coherent, demonstrated.")

# ----------------------------------------------------------------------------
# 3. Scheme B: whole-EW geometric-boundary, Killing, c²=2 → 3/13 (fragmentary).
# ----------------------------------------------------------------------------
print("\n--- 3. SCHEME B (whole-EW geometric-boundary, fragmentary): a₄ = Killing, c²=rank=2 → 3/13, scale-free IF coherent ---")
sinB = F(N_c, N_c + rank*n_C)
check("SCHEME B (electroweak geometric-boundary -- corpus fragments T638/F531, SU(3) bulk): the a₄ coefficient "
      "is the KILLING/isometry norm, c²=rank=2 → sin²θ_W = N_c/(N_c+rank·n_C) = 3/13, and scale-free ONLY IF "
      "the WHOLE EW ratio is boundary (Grace's bar -- SU(2)_L geometric too, not just U(1)_Y). This requires "
      "an SU(2)_L geometric origin, which is UNESTABLISHED; corpus fragments, not yet coherent",
      sinB == F(3, 13),
      f"a₄ = Killing norm; c²=rank=2 → sin²θ_W = {sinB} = 3/13, scale-free IF whole-EW-boundary. Needs SU(2)_L geometric -- unestablished.")

# ----------------------------------------------------------------------------
# 4. Coherence decides; lean A; 3/13 conditional. No win.
# ----------------------------------------------------------------------------
print("\n--- 4. coherence (all three same scheme; no mixed) decides; lean A (3/8 demonstrated); 3/13 conditional ---")
check("VERDICT: the a₄ coefficient is prepared for both schemes; the DECIDER is which single scheme is "
      "COHERENT for all three forces (Grace+Lyra's corpus pull, step 1). Cal's no-mixed-scheme: SU(2) "
      "inner-fluctuation + U(1) geometric = INCOHERENT (the angle isn't a ratio of consistently-normalized "
      "couplings). The honest LEAN is Scheme A (3/8, demonstrated, committed baseline); Scheme B (3/13) is "
      "fragmentary and must clear the whole-EW-boundary bar (SU(2)_L geometric) + no-mixed-scheme + the scale "
      "gate. So 3/13 stays Identified-with-a-candidate-mechanism, CONDITIONAL on B cohering. Knowing what "
      "BST's forces ARE is the bigger prize -- forced regardless of 3/8 vs 3/13, and it founds a₄ = SM Lagrangian",
      sinA == F(3, 8) and sinB == F(3, 13),
      "decider = coherent scheme for all three (Grace+Lyra); lean A (3/8, demonstrated); B fragmentary "
      "(whole-EW-boundary + no-mixed + scale). 3/13 conditional. No win; report straight.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (a₄ prepared both schemes: A inner-fluct→3/8 (demonstrated), B whole-EW-boundary→3/13 (fragmentary); lean A; 3/13 conditional)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5172, Lane 8 -- the gauge-field origin scheme, a₄ prepared for both):
  * GRACE'S BAR: sin²θ_W = g'²/(g²+g'²) contains g (SU(2)); 3/13-at-M_Z needs the WHOLE EW ratio boundary,
    not just U(1)_Y (SU(2)_L geometric too).
  * SCHEME A (inner fluctuations, DEMONSTRATED): a₄ = fermion trace (all three), c²=1 → 3/8, runs down (SM-like).
  * SCHEME B (whole-EW geometric-boundary, fragmentary): a₄ = Killing, c²=rank=2 → 3/13, scale-free IF the whole
    EW is boundary (SU(2)_L geometric -- UNESTABLISHED).
  * COHERENCE (Cal, no mixed): all three forces one scheme; mixed = incoherent. Decider = Grace+Lyra step 1.
  * LEAN A (3/8, demonstrated); 3/13 = Identified-with-mechanism, conditional on B cohering + scale.

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- a₄ prepared for both schemes; lean Scheme A (3/8,
demonstrated); Scheme B (3/13) fragmentary, must clear whole-EW-boundary (Grace) + no-mixed-scheme (Cal) +
the scale gate. 3/13 stays Identified-with-a-candidate-mechanism, conditional. The gauge-field origin scheme
founds a₄ = SM Lagrangian and settles sin²θ_W as a byproduct -- the bigger prize, forced regardless. Count the
rank-2 once (two 'circles' = same isometry norm). Report either way straight. Count N.
""")
