#!/usr/bin/env python3
"""
Toy 5228: STOP -- THE DISCRIMINATOR IS DEGENERATE WITH ITS OWN GRADING. @Keeper told me to specify Ω correctly
up front, using the full K = SO(5)×SO(2) Casimir rather than SO(5) alone. Checking that instruction turned up
something worse than a specification error: SPECIFYING Ω *IS* THE ANSWER. ★★★ (1) THE TWO CANDIDATES DIFFER BY
EXACTLY THE SO(2) WEIGHT. |ρ_so(7)|² = (5/2)² + (3/2)² + (1/2)² = 35/4 = 8.75; |ρ_rank-2|² = (5/2)² + (3/2)² =
17/2 = 8.50. The difference is 1/4 = (1/2)² -- precisely the THIRD component, which is the SO(2)/spinor weight.
So the entire gap my discriminator was built to resolve is the square of the very charge whose inclusion in Ω
is the open specification question. ★★★★ (2) AND A GRADING CONVENTION ALONE CONVERTS ONE ANSWER INTO THE OTHER.
Built synthetic data whose truth is SO(5)-graded with c = 8.50, then fitted it with the FULL-K grading (q = 1/2):
the fit returns c = 8.7500 -- the exact confirmation we are waiting for -- with slope 1.000000 and residual
8.9×10⁻¹⁵. The reverse runs equally cleanly: truth full-K at 8.75, fitted SO(5)-only, returns 8.5000. ⟹ THE
DISCRIMINATOR'S ENTIRE DISCRIMINATING POWER (0.25) EQUALS THE AMBIGUITY IN ITS OWN GRADING DEFINITION (q² =
0.25). ★★ (3) AND NONE OF MY THREE GUARDS SEES IT. The slope is exactly 1, the residual is at machine
precision, and Hermiticity is irrelevant to it. I built the slope guard yesterday precisely against "a broken
model returns 8.750 on target" -- and here is the same nightmare arriving through a channel the guard cannot
watch, because the grading shift is a CONSTANT and a constant is exactly what an intercept cannot separate from
the intercept. ★ (4) THE UNCOMFORTABLE COROLLARY, which I want stated plainly because it points at the answer
we want: if the full-K grading correctly includes q = 1/2 -- and for a spinor that is the physically right
choice -- then a fit returning 8.75 is GUARANTEED BY CONSTRUCTION and carries no information. The more
physically correct the grading, the more the expected answer is baked in. That is the crux, and it does not go
away by specifying Ω more carefully; specifying Ω more carefully is what determines the output. ★★ (5) SO THE
REDESIGN CRITERION, offered constructively: the two hypotheses currently differ by a CONSTANT, and a constant
is precisely what an intercept measurement cannot distinguish from a convention. To discriminate them we need
an observable on which they differ NON-CONSTANTLY -- a shape difference across K-types, a ratio, or a place
where one hypothesis predicts a different slope or a different multiplicity rather than a different offset.
Until such an observable exists, no intercept fit can separate 8.50 from 8.75, however carefully Ω is pinned.
★ I have still not measured c, and this is now a second reason not to: the number would not mean what we would
want to say about it. Elie, stopping a measurement that could not have failed. (Keeper's grading instruction;
toys 5221/5226/5227.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * ★★★ |ρ_so(7)|² − |ρ_rank-2|² = 1/4 = (1/2)² = exactly the SO(2)/spinor weight squared.
  * ★★★★ truth SO(5)-graded at c = 8.50, fitted with full-K grading → c = 8.7500, slope 1.000000, resid 9e-15.
  * reverse: truth full-K at 8.75, fitted SO(5)-only → c = 8.5000, equally clean.
  * ★★ neither the slope guard, the residual guard, nor the Hermiticity guard detects the shift.
  * ★★ redesign criterion: the hypotheses differ by a CONSTANT ⟹ an intercept cannot separate them.

=> VERDICT (plain): I was asked to fix how the grading is defined, and the fix turns out to be the answer. The
two numbers we are trying to choose between differ by one quarter, and one quarter is exactly the square of the
half-unit of charge that the spinor carries in the circle direction -- the very thing whose inclusion in the
grading was the open question. So I built data that genuinely means eight and a half, graded it the other way,
and the fit reported eight and three quarters: perfect straight line, no residual worth the name, and the exact
number we have been hoping to see. It works in reverse too. Which means the instrument, as designed, reports
whichever convention I feed it rather than anything about the operator, and none of the three tripwires I built
yesterday can tell -- because the difference between the two conventions is a constant, and separating a
constant from an intercept is the one thing an intercept fit cannot do. The uncomfortable part is that the
physically correct grading is the one that hands back the answer we want, which means a confirmation would be
guaranteed rather than earned. To actually decide between these two invariants we need somewhere they disagree
by something other than a constant.

=> DISPOSITION: MEASUREMENT HELD ON A SECOND, INDEPENDENT GROUND. ★★★ The candidate gap (8.75 − 8.50 = 0.25)
EQUALS the SO(2) weight squared ((1/2)² = 0.25), which is exactly the open grading choice. ★★★★ Demonstrated:
a grading convention alone converts 8.50 → 8.75 (slope 1.000000, residual 9e-15) and 8.75 → 8.50 in reverse.
★★ NONE of my three guards detects it -- the shift is a constant, and an intercept cannot separate a constant
from itself. ★ COROLLARY: if the physically correct full-K grading includes q = 1/2, then a fit returning 8.75
is guaranteed BY CONSTRUCTION and carries no information. ★★ REDESIGN CRITERION: the two hypotheses differ by a
CONSTANT; we need an observable where they differ NON-constantly (shape across K-types, a ratio, a
multiplicity, a slope) before any measurement can discriminate them. Firer: Elie. Owed: a discriminating
observable, or the honest statement that the intercept cannot decide this. Nothing banked; nothing pushed;
c NOT measured.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

from fractions import Fraction as F
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_C, NC3 = 5, 3
KTYPES = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1)]

def omega5(m1, m2):
    """SO(5)-only grading, as my toy-5227 instrument used it."""
    return m1*(m1 + N_C) + m2*(m2 + NC3)

def fit_intercept(Y, C):
    A = np.vstack([C, np.ones_like(C)]).T
    (slope, inter), *_ = np.linalg.lstsq(A, Y, rcond=None)
    resid = float(np.abs(Y - (slope*C + inter)).max())
    return -float(inter), float(slope), resid

print("=" * 78)
print("Toy 5228: STOP -- the discriminator is degenerate with its own grading. c NOT measured.")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. ★★★ The gap IS the SO(2) weight.
# ---------------------------------------------------------------------------
print("\n--- 1. ★★★ the two candidates differ by exactly the SO(2) weight squared ---")
rho3 = [F(5, 2), F(3, 2), F(1, 2)]
rho2 = [F(5, 2), F(3, 2)]
n3 = sum(x*x for x in rho3)
n2 = sum(x*x for x in rho2)
check(f"|ρ_so(7)|² = (5/2)² + (3/2)² + (1/2)² = {n3} = {float(n3)}; |ρ_rank-2|² = (5/2)² + (3/2)² = {n2} = "
      f"{float(n2)}. The difference is {n3-n2} = {float(n3-n2)} = (1/2)² -- precisely the THIRD component, "
      "which is the SO(2)/spinor weight. ⟹ the entire gap my discriminator was built to resolve IS the square "
      "of the very charge whose inclusion in Ω was the open specification question @Keeper just raised.",
      n3 - n2 == F(1, 4),
      f"gap = {n3-n2} = (1/2)² = the SO(2) weight squared — the same quantity as the open grading choice")

# ---------------------------------------------------------------------------
# 2. ★★★★ The convention converts one answer into the other.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★★★ and a grading convention alone converts 8.50 into 8.75 ---")
q = 0.5
C5 = np.array([omega5(*k) for k in KTYPES], float)
CK = C5 + q*q
c_fwd, s_fwd, r_fwd = fit_intercept(C5 - 8.50, CK)     # truth SO(5)-graded at 8.50, fitted full-K
c_rev, s_rev, r_rev = fit_intercept(CK - 8.75, C5)     # truth full-K at 8.75, fitted SO(5)-only
check("Built synthetic data whose TRUTH is SO(5)-graded with c = 8.50, then fitted it with the FULL-K grading "
      f"(q = 1/2): the fit returns c = {c_fwd:.4f} -- the exact confirmation we are waiting for -- with slope "
      f"{s_fwd:.6f} and residual {r_fwd:.1e}. The reverse runs equally cleanly: truth full-K at 8.75, fitted "
      f"SO(5)-only, returns {c_rev:.4f} (slope {s_rev:.6f}, residual {r_rev:.1e}). ⟹ THE DISCRIMINATOR'S "
      "ENTIRE DISCRIMINATING POWER (0.25) EQUALS THE AMBIGUITY IN ITS OWN GRADING DEFINITION (q² = 0.25).",
      abs(c_fwd - 8.75) < 1e-9 and abs(c_rev - 8.50) < 1e-9,
      f"8.50 →(grading)→ {c_fwd:.4f}; 8.75 →(grading)→ {c_rev:.4f}; slopes 1.000000, residuals ~1e-14")

# ---------------------------------------------------------------------------
# 3. ★★ And no guard sees it.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ and none of my three guards detects it ---")
check("The slope is exactly 1.000000, the residual is at machine precision, and Hermiticity is irrelevant to "
      "the shift. I built the slope guard yesterday (toy 5227) precisely against 'a broken model returns 8.750 "
      "on target' -- and here is the same nightmare arriving through a channel the guard CANNOT watch, because "
      "the grading shift is a CONSTANT, and separating a constant from the intercept is the one thing an "
      "intercept fit cannot do. The tripwire was right; it is simply on the wrong wall.",
      abs(s_fwd - 1) < 1e-9 and r_fwd < 1e-12,
      "slope 1.000000, residual 9e-15, Hermiticity unaffected — the shift is invisible to all three guards")

# ---------------------------------------------------------------------------
# 4. ★ The uncomfortable corollary.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ the uncomfortable corollary, stated plainly ---")
check("If the full-K grading correctly includes q = 1/2 -- and for a spinor that is the physically RIGHT "
      "choice -- then a fit returning 8.75 is GUARANTEED BY CONSTRUCTION and carries no information. The more "
      "physically correct the grading, the more the expected answer is baked in. I want that said plainly "
      "because it points at the number we want: this does not go away by specifying Ω more carefully. "
      "Specifying Ω more carefully is what DETERMINES the output.",
      abs(c_fwd - 8.75) < 1e-9,
      "physically-correct grading (q=1/2) ⟹ 8.75 by construction ⟹ a confirmation would be guaranteed, not earned")

# ---------------------------------------------------------------------------
# 5. ★★ The redesign criterion.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★ what would actually discriminate -- offered constructively ---")
check("The two hypotheses currently differ by a CONSTANT, and a constant is precisely what an intercept "
      "measurement cannot distinguish from a convention. To separate them we need an observable on which they "
      "differ NON-CONSTANTLY: a shape difference across K-types, a ratio, a multiplicity, or a place where one "
      "hypothesis predicts a different SLOPE rather than a different offset. Until such an observable exists, "
      "no intercept fit can separate 8.50 from 8.75 however carefully Ω is pinned -- and saying so now is "
      "cheaper than saying it after a number has been announced.",
      True,
      "need an observable where the hypotheses differ non-constantly; an intercept cannot decide a constant offset")

check("STATED AGAIN: I have NOT measured c, and this is now a SECOND independent reason not to -- separate "
      "from @Cal's outstanding certification and @Lyra's open minimal-K-type gate. The number would not mean "
      "what we would want to say about it.",
      True,
      "c NOT measured; held on Cal's certification, Lyra's K-type gate, AND now the degeneracy")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (the candidate gap 0.25 IS the SO(2) weight squared; a grading convention alone turns 8.50 into 8.75 with slope 1.000000 and no guard detecting it)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5228, stopping a measurement that could not have failed — c NOT measured):
  * ★★★ THE GAP IS THE GRADING: |ρ_so(7)|² − |ρ_rank-2|² = 1/4 = **(1/2)² = the SO(2)/spinor weight squared**.
    The entire difference my discriminator was built to resolve is the square of the very charge whose
    inclusion in Ω was @Keeper's open specification question.
  * ★★★★ A CONVENTION ALONE CONVERTS ONE ANSWER INTO THE OTHER: truth SO(5)-graded at **8.50**, fitted with
    the full-K grading → **c = 8.7500**, slope **1.000000**, residual **9e-15**. Reverse: truth full-K at 8.75,
    fitted SO(5)-only → **8.5000**. ⟹ the discriminator's whole discriminating power (0.25) EQUALS the
    ambiguity in its own grading definition (q² = 0.25).
  * ★★ AND NO GUARD SEES IT. Slope exactly 1, residual at machine precision, Hermiticity irrelevant. I built
    the slope guard yesterday against exactly "a broken model returns 8.750 on target" — and this is the same
    nightmare through a channel the guard **cannot** watch, because the shift is a CONSTANT and separating a
    constant from the intercept is the one thing an intercept fit cannot do.
  * ★ THE UNCOMFORTABLE COROLLARY: if the full-K grading correctly includes q = 1/2 — physically right for a
    spinor — then **a fit returning 8.75 is guaranteed by construction and carries no information.** The more
    correct the grading, the more the expected answer is baked in. Specifying Ω more carefully doesn't fix
    this; it **determines the output**.
  * ★★ REDESIGN CRITERION: the hypotheses differ by a **constant**, and an intercept cannot separate a constant
    from a convention. We need an observable where they differ **non-constantly** — a shape across K-types, a
    ratio, a multiplicity, a slope. Until then no intercept fit can decide 8.50 vs 8.75, however carefully Ω
    is pinned.
  * c NOT MEASURED — now held on three independent grounds: @Cal's certification, @Lyra's minimal-K-type gate,
    and this degeneracy.

AUG-13. Nothing pushed. Count once. CP existence-only.
""")
