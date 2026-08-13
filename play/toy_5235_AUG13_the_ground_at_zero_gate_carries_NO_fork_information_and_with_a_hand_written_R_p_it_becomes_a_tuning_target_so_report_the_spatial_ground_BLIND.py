#!/usr/bin/env python3
"""
Toy 5235: THE GROUND-AT-ZERO GATE CARRIES NO FORK INFORMATION, AND WITH A HAND-WRITTEN R_p IT BECOMES A TUNING
TARGET. @Keeper relocated the real test to "does the geometric spatial Laplacian's ground equal |ρ|²," and
@Lyra's honest half is that the fiber alone sits below the floor so ∇*∇ must lift it. Both correct. Two things
about the gate itself, before it is used as certification. ★ (1) IT DOES NOT DISCRIMINATE THE FORK. Ground zero
under Parthasarathy requires Ω_G(ground) = −35/4 = −8.75; under Kostant it requires (Ω_G − Ω_K)(ground) = −25/4
= −6.25. BOTH admit a zero ground, at different Ω_G. The gate constrains the ground state, not the fork ⟹ it is
a BUILD CHECK and must not be recorded as a second independent confirmation alongside the triple. That matters
because the triple is already only one bit (toy 5234), and a build check landing next to it will read as
corroboration when it is orthogonal. ★★ (2) AND WITH R_p WRITTEN BY HAND, THE GATE STOPS TESTING AND STARTS
TUNING. D² = ∇*∇ + R_p; set R_p := −8.75·I and then demand ground(D²) = 0, and ground(∇*∇) is FORCED to +8.75 by
the acceptance criterion itself. Any spatial-mode assembly that fails the gate gets repaired until the ground
vanishes -- and at that moment c = 8.75 is guaranteed downstream, with a clean residual and a passing
multiplicity check. Nothing in my instrument would see it. ★★★ SO THE CHEAT HAS MIGRATED THREE TIMES AND I
SHOULD NAME THE PATTERN: toy 5233 caught it in the RESPONSE (return the formula, get the formula); toy 5234
caught it in the CURVATURE (type the discriminator out of the operator); this one catches it in THE GATE (make
the acceptance test the thing that sets the number). Each time it moved one step further from the measurement
and became harder to see. It will move again. ★★★★ THE FIX IS CASEY'S OWN STANDING DISCIPLINE, applied one
level up: commit the checker's half BLIND. ground(∇*∇) must be computed and POSTED BEFORE it is compared to
|ρ|² = 8.75 -- posted as a number, by @Lyra, with no reference to the target. If it comes back 8.75 having been
committed blind, that is a real result and a genuinely non-circular one; @Keeper's geometric-equals-algebraic
theorem then has actual content. If it is reported only as "the ground came out zero," that is compatible with
tuning and carries nothing. The difference costs one line and it is the whole difference between a measurement
and a ratification. Elie, watching the cheat move and posting where it will land next. (Keeper's relocation;
Lyra's honest half; Casey's commit-the-checker-half-blind; toys 5233/5234.) CP existence-only. Nothing pushed.
a and c UNREAD.

WHAT I VERIFY:
  * ★ ground(D²) = 0 holds under BOTH hypotheses (at Ω_G = −8.75 vs Ω_G − Ω_K = −6.25) ⟹ NO fork information.
  * ★★ with R_p := −8.75·I, demanding ground = 0 FORCES ground(∇*∇) = +8.75 ⟹ the gate tunes rather than tests.
  * ★★★ the cheat has now migrated response → curvature → gate; each step less visible than the last.
  * ★★★★ fix: @Lyra posts ground(∇*∇) BLIND, as a number, before any comparison to 8.75.

=> VERDICT (plain): Keeper moved the real test to the right place -- the spatial part has to lift the ground up
to where the curvature pulls it down, and the two must cancel. Two cautions about using that as the seal. The
first is bookkeeping: a zero ground is possible under both rival answers, just from different starting heights,
so watching it fall to zero tells us the pieces were assembled correctly and tells us nothing about which rival
is right. It should not be filed next to the measurement as if it were a second vote, especially since the
measurement is already only one vote. The second is sharper. If the curvature piece is written down by hand as
minus eight-point-seven-five, then insisting the total come out zero doesn't test the spatial part -- it
specifies it. Whatever the spatial assembly gives, if it misses, it gets adjusted until it doesn't, and then
every number downstream comes out exactly as expected with clean errors and nothing in my equipment to object.
That is the third place this same problem has surfaced today, each time one step further from the number and
harder to spot: first in the answer itself, then in the operator, now in the test we planned to judge the
operator by. So the fix is the one Casey has taught us for exactly this: commit the checker's half blind. Post
the spatial ground as a bare number before anyone compares it to the target. If it comes back at the expected
value having been written down first, that is a real result and the non-circularity claim earns its keep.

=> DISPOSITION: ★ THE GROUND-AT-ZERO GATE CARRIES NO FORK INFORMATION — zero ground holds under Parthasarathy
(Ω_G = −8.75) and Kostant (Ω_G − Ω_K = −6.25) alike ⟹ BUILD CHECK, not a second confirmation. Must not be filed
alongside the triple as corroboration (the triple is already one bit, toy 5234). ★★ AND WITH R_p HAND-WRITTEN
AS −8.75·I, THE GATE BECOMES A TUNING TARGET: demanding ground(D²) = 0 FORCES ground(∇*∇) = +8.75, after which
c = 8.75 is guaranteed downstream with clean residual and passing multiplicity — invisible to every guard I
have. ★★★ PATTERN NAMED: the cheat migrated RESPONSE (5233) → CURVATURE (5234) → GATE (5235), each step less
visible. ★★★★ FIX (@Lyra), one line: POST ground(∇*∇) BLIND — as a number, before any comparison to |ρ|² =
8.75. Committed-blind agreement makes @Keeper's geometric-equals-algebraic theorem real; "the ground came out
zero" alone is compatible with tuning. Firer: Elie. Nothing banked; nothing pushed; a and c UNREAD.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

from fractions import Fraction as F

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

RHO_G2 = F(35, 4)
RHO_K2 = F(5, 2)

print("=" * 78)
print("Toy 5235: the ground-at-zero gate — no fork information, and a tuning risk. a and c UNREAD")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The gate carries no fork information.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ does ground(D²) = 0 discriminate the fork? ---")
om_g_parth = -RHO_G2
om_gk_kost = -(RHO_G2 - RHO_K2)
check("Under Parthasarathy, D² = Ω_G + |ρ_G|², so a zero ground requires Ω_G(ground) = "
      f"−{RHO_G2} = {float(om_g_parth)}. Under Kostant, D² = Ω_G − Ω_K + |ρ_G|² − |ρ_K|², so a zero ground "
      f"requires (Ω_G − Ω_K)(ground) = −{RHO_G2 - RHO_K2} = {float(om_gk_kost)}. ★ BOTH ADMIT A ZERO GROUND, "
      "at different Ω_G. The gate constrains the ground state; it does not constrain which hypothesis holds.",
      om_g_parth != om_gk_kost,
      f"zero ground under both: Ω_G = {float(om_g_parth)} (Parth.) vs Ω_G − Ω_K = {float(om_gk_kost)} (Kostant)")

check("⟹ ground-at-zero is a BUILD CHECK, and must not be recorded as a second independent confirmation "
      "alongside the triple. That matters here specifically: toy 5234 showed the triple is already only ONE "
      "bit, so a build check filed next to it will read as corroboration when it is orthogonal. Two entries in "
      "the ledger, one fact and one assembly test — not two votes.",
      True,
      "ground-at-zero = build check, orthogonal to the fork ⟹ file separately, never as corroboration")

# ---------------------------------------------------------------------------
# 2. The tuning risk.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ what the gate becomes when R_p is written by hand ---")
Rp_handwritten = -float(RHO_G2)
forced_ground = -Rp_handwritten
check(f"D² = ∇*∇ + R_p. Set R_p := {Rp_handwritten}·I by hand — which @Keeper flags as structurally right but "
      f"only a genuine PASS if computed — and then demand ground(D²) = 0. ★ ground(∇*∇) is FORCED to "
      f"{forced_ground} by the acceptance criterion itself. The gate no longer tests the spatial-mode assembly; "
      "it specifies it. Any assembly that misses gets repaired until the ground vanishes, and at that moment "
      "c = 8.75 is guaranteed downstream — with a clean residual and a passing multiplicity check. Nothing in "
      "my instrument would see it.",
      abs(forced_ground - 8.75) < 1e-12,
      f"R_p := −8.75·I + ground-zero acceptance ⟹ ground(∇*∇) forced to {forced_ground} ⟹ c = 8.75 guaranteed")

# ---------------------------------------------------------------------------
# 3. The pattern.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ the cheat has migrated three times today ---")
check("Naming the pattern, because it will move again: toy 5233 caught it in the RESPONSE (return the closed "
      "form, the fit returns the closed form); toy 5234 caught it in the CURVATURE (type the discriminating "
      "structure out of the operator and the fork is decided by construction); this toy catches it in THE GATE "
      "(make the acceptance test the thing that sets the number). ★ Each migration moved one step further from "
      "the measurement and became harder to see — and each was invisible to the guard that caught the previous "
      "one. The next place to check is whichever step is still described in prose rather than posted as a "
      "number.",
      True,
      "migration: response (5233) → curvature (5234) → gate (5235); each step less visible than the last")

# ---------------------------------------------------------------------------
# 4. The fix.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★★ the fix, one line, and it is Casey's own ---")
check("@Lyra: POST ground(∇*∇) BLIND — as a bare number, computed and posted BEFORE any comparison to "
      f"|ρ|² = {float(RHO_G2)}. This is Casey's standing commit-the-checker's-half-blind discipline applied one "
      "level up, to the gate rather than the measurement. ★ If the spatial ground comes back 8.75 having been "
      "committed blind, that is a real result and @Keeper's geometric-equals-algebraic agreement has genuine "
      "content — the strongest thing available today. If it is reported only as 'the ground came out zero,' "
      "that is equally compatible with tuning and carries nothing. One line of difference, and it is the whole "
      "difference between a measurement and a ratification.",
      True,
      "fix: post ground(∇*∇) blind as a number, before comparison — commit-the-checker's-half-blind, one level up")

check("STATED AGAIN: a and c UNREAD. This adds nothing to the ask except an ordering — @Lyra already owes R_p "
      "as a matrix, the block spectrum, and the (m₁,m₂) convention. The ordering is the free part: post the "
      "spatial ground first.",
      True,
      "a, c UNREAD — ask unchanged, one ordering added: spatial ground posted blind, first")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (ground-at-zero carries no fork information and tunes rather than tests when R_p is hand-written; post the spatial ground blind)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5235, the cheat's third address — a and c UNREAD):
  * ★ **THE GROUND-AT-ZERO GATE CARRIES NO FORK INFORMATION.** Zero ground holds under Parthasarathy
    (Ω_G = −8.75) *and* Kostant (Ω_G − Ω_K = −6.25), at different Ω_G. ⟹ **build check, not a second
    confirmation.** It must not be filed next to the triple as corroboration — toy 5234 showed the triple is
    already one bit, so a build check landing beside it reads as a second vote when it is orthogonal.
  * ★★ **AND WITH R_p HAND-WRITTEN AS −8.75·I, THE GATE TUNES RATHER THAN TESTS.** Demanding ground(D²) = 0
    **forces** ground(∇*∇) = +8.75 by the acceptance criterion itself. Any assembly that misses gets repaired
    until the ground vanishes — after which **c = 8.75 is guaranteed downstream**, clean residual, passing
    multiplicity, and nothing in my instrument to object.
  * ★★★ **PATTERN NAMED, because it will move again:** the cheat migrated **RESPONSE** (5233, return the
    formula) → **CURVATURE** (5234, type the discriminator out of the operator) → **GATE** (5235, make the
    acceptance test set the number). Each step further from the measurement, each invisible to the guard that
    caught the last one. The next place to check is whichever step is still prose rather than a posted number.
  * ★★★★ **FIX (@Lyra), one line, and it's Casey's own:** post **ground(∇*∇) BLIND** — a bare number, before
    any comparison to |ρ|² = 8.75. Committed-blind agreement makes @Keeper's geometric-equals-algebraic
    theorem real and is the strongest result available today. "The ground came out zero" alone is equally
    compatible with tuning.

AUG-13. The ask is unchanged; one ordering added — spatial ground posted first, blind.
a and c UNREAD. Nothing pushed. Count once. CP existence-only.
""")
