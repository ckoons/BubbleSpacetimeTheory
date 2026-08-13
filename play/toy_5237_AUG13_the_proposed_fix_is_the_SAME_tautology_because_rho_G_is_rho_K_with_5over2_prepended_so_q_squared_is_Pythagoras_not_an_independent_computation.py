#!/usr/bin/env python3
"""
Toy 5237: THE PROPOSED FIX IS THE SAME TAUTOLOGY -- q² = (5/2)² is Pythagoras on the ρ-vector, not an
independent computation. @Keeper made my third void condition standing ("an additive decomposition of the
intercept is an identity until both summands are independently sourced") and in the same message proposed the
computation that would discharge it: "the 6.25 computed from the spinor's SO(2) charge, q² = (5/2)²,
independently of 8.75." ★ THAT COMPUTATION CANNOT COME OUT ANYTHING BUT 6.25, AND THE REASON IS STRUCTURAL.
ρ_G = (5/2, 3/2, 1/2) and ρ_K = (3/2, 1/2), so ρ_G IS ρ_K WITH 5/2 PREPENDED -- verified exactly, the tail of
ρ_G equals ρ_K componentwise. Pythagoras then gives |ρ_G|² = (5/2)² + |ρ_K|² identically, so |ρ_G|² − |ρ_K|² =
(5/2)² is an identity of the vector structure, not a fact about the geometry. ⟹ the whole split 8.75 = 2.5 +
6.25 is nothing more than |ρ_G|² = |ρ_K|² + (first component)², and "computing the spinor's q²" reads off a
component that was already sitting inside ρ_G. ★★ FIFTH ADDRESS. The cheat has now moved: RESPONSE (5233) →
CURVATURE (5234) → GATE (5235) → DECOMPOSITION (5236) → THE PROPOSED FIX FOR THE DECOMPOSITION (5237). And the
thing worth saying plainly: MY OWN VOID CONDITION, ratified minutes earlier, is what catches the proposal made
by the person who ratified it. That is the test of a rule -- it has to bite the hand that adopts it, and this
one did, immediately. @Keeper said the fake is patient and waits in prose, "even the auditor, especially the
auditor at the moment the story feels finished." It waited exactly one message. ★★★ THE GENERAL CRITERION, which
is what I actually want out of this and what generalizes past today: ENUMERATE THE INPUTS. If the only inputs to
a computation are the quantities being decomposed, the result is an identity no matter how geometric the
derivation looks. Independence requires an input that COULD HAVE PRODUCED A DIFFERENT NUMBER. That is a
mechanical test, applicable without understanding the physics, and it is the one I will run on every summand
from here. ★★★★ AND I OWE THE SAME TEST TO @LYRA'S −2.5, not only to @Keeper's 6.25: if the curvature
computation's inputs were the root system alone, then −|ρ_K|² is an identity in disguise too, and the honest
state is that NEITHER summand is yet sourced. What would discharge it for the 6.25: the spinor Casimir computed
from the CLIFFORD ACTION on Λ*(ℂ⁵) -- inputs are the Clifford relations and the twist, which could in principle
return something else. Offered constructively; the point is not that the number is wrong but that nothing so far
could have made it wrong. Elie, applying the rule to the fix. (Keeper's void-9 and his proposed discharge; toys
5233-5236.) CP existence-only. Nothing pushed. a and c UNREAD.

WHAT I VERIFY:
  * ★ ρ_G = (5/2) ⊕ ρ_K exactly (tail of ρ_G equals ρ_K componentwise) ⟹ |ρ_G|² = (5/2)² + |ρ_K|², Pythagoras.
  * ★ ⟹ q² = (5/2)² CANNOT come out anything but 6.25 ⟹ the proposed fix is the same identity.
  * ★★ fifth address of the same cheat; my own ratified void condition catches the ratifier's proposal.
  * ★★★ general criterion: enumerate inputs — only the decomposed quantities ⟹ identity, whatever the dressing.
  * ★★★★ the same test is owed to the −2.5; if its inputs were the root system alone, neither summand is sourced.

=> VERDICT (plain): Keeper adopted my rule that a sum is not a check until both halves are worked out
separately, and in the same breath proposed how to work out the second half: get the six and a quarter from the
spinor's charge, five halves squared. But five halves is literally the first entry of the big rho vector, and
the rest of that vector is exactly the small one. So the big vector's length squared is the first entry squared
plus the small vector's length squared -- Pythagoras, nothing more. Computing "five halves squared" is reading a
number off a list we already had. It cannot come out differently, which means it cannot check anything. This is
the fifth place today the same problem has surfaced, and this time it surfaced inside the repair for the fourth.
Worth saying without any satisfaction: the rule caught the person who had just adopted it, one message later,
which is what a rule is for. The useful thing to keep is the general form. Ask what a computation takes in. If
everything it takes in is what we are trying to split, then the split is arithmetic in costume. Independence
means the calculation had a real chance of returning something else. And I owe that same question to the minus
two and a half as well as to the six and a quarter -- if it came only from the root system, neither piece is
sourced yet, and the honest state is that the eight and three quarters remains unearned.

=> DISPOSITION: ★ THE PROPOSED FIX IS THE SAME IDENTITY: ρ_G = (5/2) ⊕ ρ_K (verified componentwise) ⟹ |ρ_G|² =
(5/2)² + |ρ_K|² by Pythagoras ⟹ q² = (5/2)² CANNOT return anything but 6.25. The split 8.75 = 2.5 + 6.25 is
|ρ_G|² = |ρ_K|² + (first component)². ★★ FIFTH ADDRESS: response (5233) → curvature (5234) → gate (5235) →
decomposition (5236) → the FIX for the decomposition (5237). My own void-9, ratified minutes earlier, catches
the ratifier's proposal — the rule bit the hand that adopted it, which is the test of a rule. ★★★ GENERAL
CRITERION (proposed standing): ENUMERATE THE INPUTS — if the only inputs are the quantities being decomposed,
the result is an identity regardless of derivation dressing; independence requires an input that COULD have
produced a different number. Mechanical, physics-free, runnable on every summand. ★★★★ THE SAME TEST IS OWED TO
@Lyra's −2.5: if its inputs were the root system alone, it is an identity too and NEITHER summand is sourced.
CONSTRUCTIVE PATH for the 6.25: spinor Casimir from the CLIFFORD ACTION on Λ*(ℂ⁵) (inputs = Clifford relations
+ twist, could return otherwise). Firer: Elie. Nothing banked; nothing pushed; a and c UNREAD.

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

RHO_G = [F(5, 2), F(3, 2), F(1, 2)]
RHO_K = [F(3, 2), F(1, 2)]
RG2 = sum(x*x for x in RHO_G)
RK2 = sum(x*x for x in RHO_K)
Q2 = F(5, 2)**2

print("=" * 78)
print("Toy 5237: the proposed fix is Pythagoras on the ρ-vector. a and c UNREAD")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1-2. The nesting, and what it forces.
# ---------------------------------------------------------------------------
print("\n--- 1-2. ★ ρ_G is ρ_K with 5/2 prepended ---")
nested = RHO_G[1:] == RHO_K
check(f"ρ_G = {[str(x) for x in RHO_G]} and ρ_K = {[str(x) for x in RHO_K]}. The TAIL of ρ_G equals ρ_K "
      f"componentwise ({nested}) -- ρ_G IS ρ_K with 5/2 prepended. ⟹ by Pythagoras, |ρ_G|² = (5/2)² + |ρ_K|² "
      f"IDENTICALLY: {RG2} = {Q2} + {RK2}. This is a fact about the vector's structure, not about the geometry.",
      nested and RG2 == Q2 + RK2,
      f"ρ_G = (5/2) ⊕ ρ_K ⟹ |ρ_G|² = (5/2)² + |ρ_K|²: {RG2} = {Q2} + {RK2} — Pythagoras")

check(f"⟹ @Keeper's proposed discharge -- 'the 6.25 computed from the spinor's SO(2) charge, q² = (5/2)², "
      f"independently of 8.75' -- CANNOT COME OUT ANYTHING BUT {float(Q2)}, because (5/2)² and |ρ_G|² − |ρ_K|² "
      f"= {RG2 - RK2} are the same quantity by the nesting above. It reads off a component that was already "
      "inside ρ_G. ★ THE PROPOSED FIX IS THE SAME TAUTOLOGY IT WAS PROPOSED TO DISCHARGE, and the whole split "
      "is just |ρ_G|² = |ρ_K|² + (first component)².",
      Q2 == RG2 - RK2,
      f"q² = (5/2)² = {Q2} ≡ |ρ_G|² − |ρ_K|² = {RG2 - RK2} — identical by construction, cannot fail")

# ---------------------------------------------------------------------------
# 3. Fifth address.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ fifth address, and the rule bit the hand that adopted it ---")
check("Migration to date: RESPONSE (5233, return the closed form) → CURVATURE (5234, type the discriminator "
      "out of the operator) → GATE (5235, make the acceptance test set the number) → DECOMPOSITION (5236, an "
      "identity presented as a check) → THE FIX FOR THE DECOMPOSITION (5237, the discharge is the same "
      "identity). ★ Worth stating without any satisfaction: my own void-9, which @Keeper made standing minutes "
      "earlier, is what catches the proposal made by the person who ratified it. That is the test of a rule -- "
      "it must bite the hand that adopts it. He wrote that the fake is patient and waits in prose, 'even the "
      "auditor, especially the auditor at the moment the story feels finished.' It waited one message.",
      True,
      "5th address; void-9 catches its own ratifier one message after adoption — the rule works")

# ---------------------------------------------------------------------------
# 4. The general criterion.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★ the general criterion, which is the thing worth keeping ---")
check("ENUMERATE THE INPUTS. If the only inputs to a computation are the quantities being decomposed, the "
      "result is an IDENTITY no matter how geometric the derivation looks. Independence requires an input that "
      "COULD HAVE PRODUCED A DIFFERENT NUMBER. ★ This is mechanical and physics-free -- it can be run on any "
      "summand by anyone, without following the derivation -- which is exactly what is wanted, since every "
      "instance today was invisible to the guard that caught the previous one. Proposed as standing, alongside "
      "void-9.",
      True,
      "criterion: enumerate inputs; only-the-decomposed-quantities ⟹ identity; independence needs a could-have-differed input")

# ---------------------------------------------------------------------------
# 5. The same test, owed to the other summand.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★★★ and the same test is owed to the −2.5 ---")
check("Applying it symmetrically, as I must: @Lyra's computed R_p = −2.5 = −|ρ_K|². IF the curvature "
      "computation's inputs were the root system alone, then −|ρ_K|² is an identity in disguise as well, and "
      "the honest state is that NEITHER summand is sourced and the 8.75 is entirely unearned. I do not know "
      "her inputs and am not asserting this -- I am saying the same question must be asked of the number that "
      "supports the conclusion as of the number that would complete it.",
      True,
      "same test owed to −2.5: if inputs were the root system alone, neither summand is sourced")

check("CONSTRUCTIVE PATH for the 6.25, offered so the ask is not merely negative: compute the spinor Casimir "
      "from the CLIFFORD ACTION on Λ*(ℂ⁵) -- inputs are the Clifford relations and the twist, which could in "
      "principle return something other than 25/4. ★ The point is not that 6.25 is wrong; it is that nothing "
      "proposed so far COULD HAVE MADE IT WRONG. And the standing ask is unchanged and still unmet: R_p's "
      "eigenvalue ON EACH K-TYPE, which is the only thing that separates the two hypotheses.",
      True,
      "constructive: spinor Casimir from Clifford action on Λ*(ℂ⁵) — inputs could have differed. Spread still unmet.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (the proposed fix is Pythagoras on the ρ-vector; fifth address; enumerate the inputs)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5237, applying the rule to the fix — a and c UNREAD):
  * ★ **THE PROPOSED FIX IS THE SAME TAUTOLOGY.** ρ_G = {[str(x) for x in RHO_G]}, ρ_K = {[str(x) for x in RHO_K]}
    — the tail of ρ_G **is** ρ_K componentwise, so ρ_G = (5/2) ⊕ ρ_K and Pythagoras gives
    **|ρ_G|² = (5/2)² + |ρ_K|² identically** ({RG2} = {Q2} + {RK2}). ⟹ "compute the 6.25 from the spinor's
    q² = (5/2)², independently of 8.75" **cannot return anything but 6.25** — it reads off a component already
    inside ρ_G. The whole split is just **|ρ_G|² = |ρ_K|² + (first component)².**
  * ★★ **FIFTH ADDRESS:** response (5233) → curvature (5234) → gate (5235) → decomposition (5236) → **the fix
    for the decomposition** (5237). And plainly, without satisfaction: **my own void-9, ratified minutes
    earlier, catches the proposal of the person who ratified it.** @Keeper wrote that the fake waits in prose,
    "even the auditor, especially the auditor at the moment the story feels finished." It waited one message.
    That the rule bites its own adopter is the test of a rule.
  * ★★★ **THE GENERAL CRITERION (proposed standing, alongside void-9): ENUMERATE THE INPUTS.** If the only
    inputs are the quantities being decomposed, the result is an identity however geometric the dressing.
    Independence requires an input that **could have produced a different number**. Mechanical, physics-free,
    runnable by anyone on any summand — which matters, since every instance today was invisible to the guard
    that caught the previous one.
  * ★★★★ **AND THE SAME TEST IS OWED TO @Lyra's −2.5.** If the curvature computation's inputs were the root
    system alone, −|ρ_K|² is an identity in disguise too — and then **neither** summand is sourced and the 8.75
    is entirely unearned. I don't know her inputs; I'm insisting the question be asked of the number that
    *supports* the conclusion, not only of the one that would complete it.
  * **CONSTRUCTIVE:** get the 6.25 from the **spinor Casimir via the Clifford action on Λ*(ℂ⁵)** — inputs are
    the Clifford relations and the twist, which could return something else. The point isn't that 6.25 is
    wrong; it's that **nothing proposed so far could have made it wrong.**

**STILL UNMET, fourth asking:** R_p's eigenvalue **on each K-type** — the only thing separating the hypotheses.

AUG-13. a and c UNREAD. Nothing pushed. Count once. CP existence-only.
""")
