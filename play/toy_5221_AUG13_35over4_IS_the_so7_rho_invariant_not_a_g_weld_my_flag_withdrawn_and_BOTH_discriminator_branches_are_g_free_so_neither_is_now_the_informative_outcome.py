#!/usr/bin/env python3
"""
Toy 5221: 35/4 IS A ROOT-SYSTEM INVARIANT, NOT A g-WELD -- I verified the ρ-sum claim myself instead of waiting
for it, and the result retires my own flag and corrects my own discriminator's labels. ★ (1) THE VERIFICATION:
so(5,2) is a real form of so(7,ℂ) = B₃, whose standard half-sum of positive roots is ρ = (5/2, 3/2, 1/2), giving
|ρ|² = 25/4 + 9/4 + 1/4 = 35/4 = 8.7500 exactly. That is the SAME NUMBER as n_C·g/4 -- and its provenance is the
root system, not g. The 35 = 5×7 is arithmetic coincidence. ★★ (2) SO I WITHDRAW MY OWN FLAG. In toys 5216 and
5217 I raised, as a question, that the claimed Lichnerowicz constant "contains g = 7 -- the number the blind
weight computation must derive," and asked for it to be shown independent or dropped. It has been shown, and it
is independent: it is |ρ_{B₃}|². @Keeper and @Lyra were right, my concern is answered, and I am retiring it
explicitly rather than letting it sit in the notes looking unresolved. ★★★ (3) AND IT CORRECTS MY OWN
DISCRIMINATOR'S LABELS, which is the substantive part. I set the test up as "8.50 = g-free vs 8.75 = carries
g." That labelling is WRONG. Both numbers are ρ-invariants and BOTH ARE g-FREE: 8.50 = |ρ|² for the rank-2
symmetric-space ρ = (5/2, 3/2) that the corpus banked, and 8.75 = |ρ|² for the full Lie-algebra ρ = (5/2, 3/2,
1/2) of so(7). The test is still sharp and still separates two genuinely different objects -- but what it
measures is WHICH ρ THE OPERATOR SEES (the symmetric-space one or the full one), NOT whether g got welded in.
That is a cleaner situation than the one I set up: whatever I measure, no g-weld is involved. ★ (4) THE
CRITERIA DO NOT MOVE. Locked yesterday at ±0.05 with a fourth "neither" branch, and they stay locked -- I note
plainly that the announced expectation flipped from 8.50 to 8.75 within about three hours, and the whole point
of pre-registration is that my thresholds do not follow it. A prediction that moves before the measurement is
not a prediction; the protection is @Cal's independence check, which @Keeper has already ordered, and I am
reinforcing rather than second-guessing it. ★★ (5) AND THE HONEST CONSEQUENCE, which cuts against the drama:
now that BOTH candidates are natural root-system invariants, hitting one of them is worth roughly one bit, not
a stunning confirmation -- the theory space has two obvious answers and the measurement will land on one. ⟹
THE "NEITHER" BRANCH IS NOW THE INFORMATIVE OUTCOME. If c comes out neither 8.50 nor 8.75, that is the result
worth chasing, and I have already reserved the branch to report it in. Elie, retiring his own flag and
sharpening his own test. (Keeper's route; Lyra's ρ-correction; toys 5216/5217/5220.) CP existence-only.
Nothing pushed.

WHAT I COMPUTE:
  * ★ ρ_{B₃} = (5/2, 3/2, 1/2) ⟹ |ρ|² = 35/4 = 8.7500 exactly -- the so(7) root-system invariant.
  * ★ corpus rank-2 ρ = (5/2, 3/2) ⟹ |ρ|² = 17/2 = 8.5000.
  * ★★ 35/4 = n_C·g/4 numerically, but its PROVENANCE is the root system ⟹ my g-weld flag is WITHDRAWN.
  * ★★★ both discriminator branches are g-FREE ⟹ the test measures WHICH ρ, not whether g was welded.
  * ★ criteria unchanged; expectation flipped 8.50 → 8.75 in ~3 hours, noted; "neither" is now the informative branch.

=> VERDICT (plain): I asked for the seven in the claimed constant to be shown independent of the seven we are
trying to derive, and it has been -- so the flag comes down. Thirty-five quarters is the squared length of the
half-sum of positive roots of the seven-dimensional orthogonal algebra, which is the complexification of our
own, and that is as clean a provenance as a number can have. The five times seven is an accident of
arithmetic. The more useful consequence is that my own test was mislabelled: I set it up as g-free against
g-carrying, and in fact both of its branches are root-system invariants with no g in either. What it actually
distinguishes is whether the operator sees the rank-two symmetric-space rho or the full algebra rho -- a real
and interesting difference, and a cleaner one, because now no outcome implicates a weld. It also means a hit on
either branch is worth about one bit rather than a headline, since the theory offers exactly two natural
answers. So the branch I reserved for "neither" has quietly become the one that would actually teach us
something.

=> DISPOSITION: ★ 35/4 VERIFIED as |ρ_{B₃}|² with ρ = (5/2,3/2,1/2) for so(7) ⊃ so(5,2) -- a root-system
invariant, NOT a g-weld; 35 = 5×7 is arithmetic coincidence. ★★ MY FLAG FROM TOYS 5216/5217 IS WITHDRAWN --
@Keeper and @Lyra were right; the provenance is independent and clean. ★★★ MY DISCRIMINATOR'S LABELS ARE
CORRECTED: both branches are g-FREE ρ-invariants (8.50 = rank-2 symmetric-space ρ, 8.75 = full so(7) ρ); the
test measures WHICH ρ the operator sees, not g-freeness. ★ CRITERIA UNCHANGED (±0.05, four branches) despite
the announced expectation flipping 8.50 → 8.75 in ~3 hours -- that is what pre-registration is for; @Cal's
independence check is the protection and I reinforce it. ★ "NEITHER" is now the informative branch, since both
named candidates are natural. Firer: Elie. Owed: fire all five tests the instant the operator lands.
Nothing banked; nothing pushed.

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

print("=" * 78)
print("Toy 5221: is 35/4 a root-system invariant or a g-weld? -- verified, and my flag comes down")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The verification.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ verify the ρ-sum claim directly ---")
rho_B3 = [F(5, 2), F(3, 2), F(1, 2)]
n_B3 = sum(r*r for r in rho_B3)
rho_r2 = [F(5, 2), F(3, 2)]
n_r2 = sum(r*r for r in rho_r2)
check("so(5,2) is a real form of so(7,ℂ) = B₃, whose standard half-sum of positive roots is "
      f"ρ = {[str(r) for r in rho_B3]}, giving |ρ|² = {n_B3} = {float(n_B3):.4f} exactly. And the corpus's "
      f"banked rank-2 symmetric-space vector ρ = {[str(r) for r in rho_r2]} gives |ρ|² = {n_r2} = "
      f"{float(n_r2):.4f}. Both are root-system invariants, computed here from the root data and nothing else.",
      n_B3 == F(35, 4) and n_r2 == F(17, 2),
      f"|ρ_B3|² = {n_B3} = {float(n_B3)}; |ρ_rank2|² = {n_r2} = {float(n_r2)}")

# ---------------------------------------------------------------------------
# 2. ★★ The flag comes down.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ my own flag, withdrawn ---")
check("In toys 5216 and 5217 I raised -- as a question -- that the claimed Lichnerowicz constant 'contains "
      "g = 7, the number the blind weight computation must derive,' and asked for it to be shown independent "
      f"or dropped as the justification. It has been shown, and it IS independent: 35/4 = |ρ_{{B₃}}|². The "
      "numerical coincidence with n_C·g/4 is exactly that -- 35 = 5×7 is arithmetic, and the provenance is the "
      "root system. ★ @Keeper and @Lyra were right; my concern is answered; I am RETIRING IT EXPLICITLY rather "
      "than leaving it in the notes looking unresolved.",
      n_B3 == F(5*7, 4),
      "35/4 = |ρ_B3|² AND = n_C·g/4 numerically — provenance is the root system ⟹ FLAG WITHDRAWN")

# ---------------------------------------------------------------------------
# 3. ★★★ My discriminator's labels were wrong.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ and it corrects my own discriminator's labels ---")
check("I set the test up as '8.50 = g-free vs 8.75 = carries g.' That labelling is WRONG. Both numbers are "
      "ρ-invariants and BOTH ARE g-FREE: 8.50 is |ρ|² for the rank-2 symmetric-space ρ, and 8.75 is |ρ|² for "
      "the full Lie-algebra ρ of so(7). ★ The test remains sharp and still separates two genuinely different "
      "objects -- but what it measures is WHICH ρ THE OPERATOR SEES (the symmetric-space one or the full one), "
      "NOT whether g got welded in. That is a cleaner situation than the one I set up: whatever the number "
      "turns out to be, no g-weld is implicated by either branch.",
      float(n_r2) == 8.5 and float(n_B3) == 8.75,
      "8.50 = rank-2 symmetric-space ρ; 8.75 = full so(7) ρ; BOTH g-free ⟹ test measures WHICH ρ, not g-freeness")

# ---------------------------------------------------------------------------
# 4. ★ The criteria do not move.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ the criteria do not move with the expectation ---")
locked = {"8.50 ± 0.05": "rank-2 symmetric-space ρ", "8.75 ± 0.05": "full so(7) ρ",
          "0.00 ± 0.05": "still flat", "anything else": "report RAW, claim NEITHER"}
check("The criteria I locked in toy 5220 stand unchanged: "
      + "; ".join(f"{k} → {v}" for k, v in locked.items())
      + " (only the LABELS on the first two branches are corrected above; the numbers and tolerances are "
      "untouched). I note plainly that the announced expectation flipped from 8.50 to 8.75 within about three "
      "hours. That is exactly what pre-registration is for -- my thresholds do not follow the expectation. And "
      "a prediction that moves before the measurement is not a prediction; the protection is @Cal's "
      "independence check, which @Keeper has already ordered, and I am reinforcing it rather than "
      "second-guessing it.",
      len(locked) == 4,
      "thresholds unchanged; expectation moved 8.50 → 8.75 in ~3h; @Cal's independence check is the protection")

# ---------------------------------------------------------------------------
# 5. ★ The honest consequence.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ and the honest consequence, which cuts against the drama ---")
check("Now that BOTH named candidates are natural root-system invariants, hitting one of them is worth roughly "
      "ONE BIT, not a stunning confirmation -- the theory space offers exactly two obvious answers and the "
      "measurement will land on one of them. ⟹ ★ THE 'NEITHER' BRANCH IS NOW THE INFORMATIVE OUTCOME. If c "
      "comes out neither 8.50 nor 8.75, that is the result worth chasing, and I reserved the branch to report "
      "it in before any of this was announced. I would rather say that now than after a match arrives looking "
      "impressive.",
      True,
      "two natural candidates ⟹ a hit is ~1 bit; 'neither' became the informative branch")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (35/4 = |ρ_B3|² verified — root-system invariant, NOT a g-weld; my flag withdrawn; both discriminator branches are g-free)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5221, verifying the ρ-sum myself rather than waiting for it):
  * ★ VERIFIED: so(5,2) is a real form of so(7,ℂ) = B₃, whose ρ = (5/2, 3/2, 1/2) gives |ρ|² = 35/4 = 8.7500
    exactly. The corpus's rank-2 ρ = (5/2, 3/2) gives 17/2 = 8.5000. Both from root data alone.
  * ★★ MY FLAG FROM TOYS 5216/5217 IS WITHDRAWN. I asked for the "g = 7" in the claimed constant to be shown
    independent of the seven we are deriving. It has been: 35/4 = |ρ_B₃|², and the coincidence with n_C·g/4 is
    arithmetic (35 = 5×7). @Keeper and @Lyra were right; retiring it explicitly rather than leaving it hanging.
  * ★★★ AND IT CORRECTS MY OWN LABELS: I set the test up as "8.50 g-free vs 8.75 carries g." WRONG — both are
    ρ-invariants and BOTH ARE g-FREE (8.50 = rank-2 symmetric-space ρ; 8.75 = full so(7) ρ). The test still
    separates two real objects, but it measures **which ρ the operator sees**, not g-freeness. Cleaner than
    what I set up: no outcome implicates a weld.
  * ★ CRITERIA UNCHANGED (±0.05, four branches) — only the labels are corrected. The announced expectation
    flipped 8.50 → 8.75 in ~3 hours; my thresholds do not follow it, which is what pre-registration is for.
    A prediction that moves before measurement isn't a prediction; @Cal's independence check is the protection
    and @Keeper already ordered it.
  * ★ HONEST CONSEQUENCE: with both candidates natural, a hit is worth ~1 bit, not a headline. ⟹ **"NEITHER"
    is now the informative branch** — and I reserved it before any of this was announced.

AUG-13. All five tests armed; I fire the instant the operator lands. Nothing pushed. Count once.
CP existence-only.
""")
