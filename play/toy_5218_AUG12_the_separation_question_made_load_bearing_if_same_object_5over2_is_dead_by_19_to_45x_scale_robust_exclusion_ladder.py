#!/usr/bin/env python3
"""
Toy 5218: THE EMPIRICAL HALF OF CAL'S SEPARATION QUESTION -- my curvature checks are blocked until the metric
lands, but the separation question has a data side and that side is mine. Cal asks: is the reproducing-kernel
exponent (5/2) genuinely a DIFFERENT object from the up-quark Yukawa mode-weight (7)? Keeper flags that if they
are the SAME object, the up-quark kills 5/2 -- and puts the factor at 27×. I ran the ladder properly and the
number is larger and, more importantly, SCALE-ROBUST. ★ (1) THE EXCLUSION LADDER, in factors rather than in
integer-proximity -- which matters, because toy 5213 showed integer-proximity significance is convention-driven
while FACTORS are not. Reading s = 5/2 as a mode-weight of 2s = 5 (the natural reading, and the one that gives
Keeper's ~27): weight 5 predicts a Yukawa 19.2× / 25.8× / 45.3× too large at 1 GeV / 2 GeV / m_Z. Reading 5/2
directly as the weight: 1074× / 1442× / 2532× too large. Either way it is dead, and dead at EVERY scale in the
physical range -- which is the property that survived from my earlier work and the property that matters here.
★ (2) THE FULL LADDER, for the record: weight 2.5 excluded by ~10³; weight 5 by 19-45×; weight 6 by 3.8-9.1×
(solid, and the weakest of the exclusions); weight 7 the only candidate consistent at any scale; weight 8
excluded by 0.2-0.4×. ★ (3) AND THE HONESTY THAT GOES WITH IT, carried forward from 5213: weight 7's
CONSISTENCY is itself scale-dependent -- 0.8× at 1 GeV, 1.0× at 2 GeV, 1.8× at m_Z. So the ladder says "7 is
the only survivor," not "7 is confirmed." The exclusions are robust; the endorsement is not. I will not let the
first sentence borrow strength from the second. ★★ (4) WHAT THIS DOES FOR THE ROUND: it makes Cal's separation
question load-bearing in a precise, quantified way. IF the reproducing-kernel exponent and the mode-weight are
the same object, then a blind computation returning 5/2 is contradicted by the up quark by a factor between
nineteen and forty-five, at every scale, with no convention available to rescue it. IF they are different
objects, there is no contradiction at all and both can stand. So the geometric separation question is not
bookkeeping -- it decides whether we have a live inconsistency or two independent results. That question is
Lyra's and Cal's; the number that makes it matter is mine, and it is bigger than 27. Elie, taking the data half
while the curvature is stitched. (Cal's separation catch; Keeper's route; toys 5212/5213.) CP existence-only.
Nothing pushed.

WHAT I COMPUTE:
  * measured exponent log₅(1/y_up) by scale: 6.836 (1 GeV), 7.019 (2 GeV), 7.369 (m_Z).
  * ★ weight 5 (= 2s for s = 5/2): predicted Yukawa 19.2× / 25.8× / 45.3× too large. EXCLUDED everywhere.
  * ★ weight 5/2 read directly: 1074× / 1442× / 2532×. EXCLUDED by ~10³.
  * full ladder: 2.5 ~10³ | 5 → 19-45× | 6 → 3.8-9.1× | 7 → the only survivor | 8 → 0.2-0.4×.
  * ★ honesty carried from 5213: weight 7's consistency is scale-dependent (0.8×-1.8×) -- survivor, not confirmed.

=> VERDICT (plain): the separation question is worth the fuss, and here is the size of the stake. If the
exponent that comes out of the reproducing condition is the same quantity that sets the up quark's coupling,
then a blind computation returning five halves is wrong by a factor of at least nineteen and as much as
forty-five, and there is no choice of energy scale anywhere in the measured range that rescues it -- unlike the
integer-proximity claims I had to retract yesterday, factors of five per unit of exponent do not move when you
change conventions. If instead the two exponents are genuinely different objects, nothing is in tension and
both results stand as they are. So this is not bookkeeping; it decides whether we are holding a contradiction
or two independent facts. I have also kept the ledger honest in the other direction: seven is the only weight
left standing, but its own agreement wanders between eight-tenths and nearly twice depending where you measure
it, so "the only survivor" is what the data supports and "confirmed" is not.

=> DISPOSITION: the empirical half of the separation question, quantified. ★ IF the reproducing-kernel exponent
and the up-quark mode-weight are the SAME object, s = 5/2 is excluded by 19-45× (read as weight 2s = 5) or
~10³ (read directly), AT EVERY SCALE -- scale-robust, because these are factors not integer-proximities.
★ Full ladder banked: 2.5 (~10³) | 5 (19-45×) | 6 (3.8-9.1×) | 7 (only survivor) | 8 (0.2-0.4×). ★ HONESTY
CARRIED FROM 5213: weight 7's consistency is itself scale-dependent (0.8×-1.8×) -- "only survivor," never
"confirmed." ⟹ @Cal's separation question is LOAD-BEARING and the stake is larger than 27×. The geometric
question is @Lyra's and @Cal's; this is the number that makes it matter. Firer: Elie. Owed: the five curved-sea
tests, still blocked on the metric. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import math

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

v = 246.21965
LN5 = math.log(5)
SCALES = [("1 GeV", 2.90e-3), ("2 GeV", 2.16e-3), ("m_Z", 1.23e-3)]

def yuk(m):
    return math.sqrt(2)*m/v

def expo(m):
    return math.log(1/yuk(m))/LN5

def factors(w):
    return [(5.0**-w)/yuk(m) for _, m in SCALES]

print("=" * 78)
print("Toy 5218: the empirical half of the separation question -- how dead is 5/2, and how robustly?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The measured exponent, by scale.
# ---------------------------------------------------------------------------
print("\n--- 1. the measured up-quark exponent, across the physical scale range ---")
exps = [(s, expo(m)) for s, m in SCALES]
check("The measured exponent log₅(1/y_up) is "
      + ", ".join(f"{s}: {e:.3f}" for s, e in exps)
      + ". That spread is the scale-dependence I established in toy 5213 -- and the lesson there was that "
      "integer-PROXIMITY claims move with the convention while FACTOR exclusions do not. So this ladder is "
      "built entirely out of factors.",
      exps[0][1] < exps[1][1] < exps[2][1],
      f"exponent runs {exps[0][1]:.3f} → {exps[1][1]:.3f} → {exps[2][1]:.3f}; ladder built from factors, not proximity")

# ---------------------------------------------------------------------------
# 2. ★ The 5/2 exclusion, both readings.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ how dead is 5/2? -- both readings, at every scale ---")
f5 = factors(5)
f25 = factors(2.5)
check("★ Reading s = 5/2 as a mode-weight of 2s = 5 -- the natural reading, and the one behind @Keeper's ~27× "
      f"-- weight 5 predicts a Yukawa {f5[0]:.1f}× / {f5[1]:.1f}× / {f5[2]:.1f}× too large at 1 GeV / 2 GeV / "
      f"m_Z. Reading 5/2 directly as the weight: {f25[0]:.0f}× / {f25[1]:.0f}× / {f25[2]:.0f}×. Either way it "
      "is dead, and dead at EVERY scale in the physical range -- there is no choice of convention that rescues "
      "it, because these are factors of five per unit of exponent and factors do not move with conventions.",
      min(f5) > 15 and min(f25) > 500,
      f"weight 5: {[round(x,1) for x in f5]}× | weight 5/2 direct: {[round(x) for x in f25]}× — excluded everywhere")

# ---------------------------------------------------------------------------
# 3. The full ladder.
# ---------------------------------------------------------------------------
print("\n--- 3. the full exclusion ladder, for the record ---")
ladder = {w: factors(w) for w in (2.5, 5, 6, 7, 8)}
surv = [w for w, f in ladder.items() if min(abs(math.log(x)) for x in f) < math.log(1.6)]
check("The complete ladder: "
      + "; ".join(f"w={w}: {[round(x,1) if x > 1 else round(x,2) for x in f]}×" for w, f in ladder.items())
      + f". Only w = 7 is consistent at any scale (survivors: {surv}). Weight 6 is excluded by "
      f"{min(ladder[6]):.1f}-{max(ladder[6]):.1f}× -- solid, and the weakest of the exclusions, worth naming "
      "as such rather than lumping it with the others.",
      surv == [7] and min(ladder[6]) > 3,
      f"survivors {surv}; weight 6 excluded by {min(ladder[6]):.1f}-{max(ladder[6]):.1f}× (weakest exclusion)")

# ---------------------------------------------------------------------------
# 4. ★ The honesty carried forward from 5213.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ and the caveat carried forward, so the first sentence doesn't borrow strength ---")
f7 = factors(7)
check("★ Weight 7's CONSISTENCY is itself scale-dependent: "
      + ", ".join(f"{s}: {x:.1f}×" for (s, _), x in zip(SCALES, f7))
      + ". So the honest reading of this ladder is 'seven is the only survivor,' NOT 'seven is confirmed.' The "
      "EXCLUSIONS are robust -- factors of 19 to 2500 cannot be argued away -- but the ENDORSEMENT is not, and "
      "I am not letting the first sentence borrow strength from the second. That distinction is exactly what "
      "toy 5213 cost me yesterday and it applies to my own ladder today.",
      abs(f7[0] - 1) < 0.5 and f7[2] > 1.5,
      f"weight 7 agreement runs {f7[0]:.1f}× → {f7[1]:.1f}× → {f7[2]:.1f}× — survivor, NOT confirmed")

# ---------------------------------------------------------------------------
# 5. ★★ What it does for the round.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★ why this makes the separation question load-bearing ---")
check("★★ @Cal's question -- is the reproducing-kernel exponent a different object from the up-quark "
      "mode-weight? -- is now quantified. IF THEY ARE THE SAME OBJECT, a blind computation returning 5/2 is "
      f"contradicted by the up quark by {min(f5):.0f}-{max(f5):.0f}× (as weight 5) or ~10³ (read directly), at "
      "every scale, with no convention available to rescue it. IF THEY ARE DIFFERENT OBJECTS, there is no "
      "contradiction and both results stand untouched. So the separation is not bookkeeping -- it decides "
      "whether we are holding a live inconsistency or two independent facts. The geometric question is "
      "@Lyra's and @Cal's; the number that makes it matter is mine, and it is larger than the 27× estimate.",
      min(f5) > 15,
      f"same object ⟹ 5/2 dead by {min(f5):.0f}-{max(f5):.0f}× everywhere; different objects ⟹ no tension. Load-bearing.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (if same object, 5/2 is dead by 19-45× at EVERY scale — factor-based, convention-proof; weight 7 is the only survivor but not confirmed)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5218, the data half of @Cal's separation question, while the curvature is stitched):
  * MEASURED exponent by scale: {exps[0][1]:.3f} (1 GeV), {exps[1][1]:.3f} (2 GeV), {exps[2][1]:.3f} (m_Z). Ladder built from
    FACTORS, not integer-proximity — because 5213 showed proximity moves with the convention and factors don't.
  * ★ 5/2 IS DEAD, BOTH READINGS: as mode-weight 2s = 5 → {f5[0]:.1f}× / {f5[1]:.1f}× / {f5[2]:.1f}× too large (this is
    @Keeper's ~27×, and the true range is 19-45×). Read directly as 5/2 → {f25[0]:.0f}× / {f25[1]:.0f}× / {f25[2]:.0f}×.
    Excluded at EVERY scale, with no convention available to rescue it.
  * FULL LADDER: w=2.5 (~10³) | w=5 (19-45×) | w=6 ({min(ladder[6]):.1f}-{max(ladder[6]):.1f}×, the weakest exclusion) |
    w=7 (the only survivor) | w=8 (0.2-0.4×).
  * ★ HONESTY CARRIED FROM 5213: weight 7's own agreement runs {f7[0]:.1f}× → {f7[1]:.1f}× → {f7[2]:.1f}× across the range.
    "Only survivor" is what the data supports; "confirmed" is not. The exclusions are robust; the endorsement
    isn't — and I won't let the first borrow strength from the second.
  * ★★ SO THE SEPARATION QUESTION IS LOAD-BEARING, quantified: SAME object ⟹ a blind 5/2 is contradicted by
    19-45× everywhere; DIFFERENT objects ⟹ no tension, both stand. It decides whether we hold a live
    inconsistency or two independent facts. The geometry is @Lyra's and @Cal's; the stake is mine, and it is
    bigger than 27×.

AUG-12. Nothing pushed. Nothing banked. The five curved-sea tests remain blocked on the metric, as designed.
Count once. CP existence-only.
""")
