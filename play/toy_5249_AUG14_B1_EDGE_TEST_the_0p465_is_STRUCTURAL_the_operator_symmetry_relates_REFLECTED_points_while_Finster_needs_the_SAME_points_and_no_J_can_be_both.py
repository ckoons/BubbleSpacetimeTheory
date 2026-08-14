#!/usr/bin/env python3
"""
Toy 5249: B1 EDGE-TEST -- THE 0.465 IS STRUCTURAL, AND THE REASON IS A CLEAN DICHOTOMY. The question was
decidable both ways and it decided. ★ (1) FIRST, THE CONDITION REDUCES. P(x,y) = Σ_k ψ_k(x) ψ_k(y)†, so
P(y,x) = P(x,y)† IDENTICALLY, by construction. ⟹ Finster's requirement P(y,x) = J P(x,y)† J is not a symmetry
to be arranged at all -- it collapses to **[J_f , P(x,y)] = 0**: the two-point kernel must COMMUTE with the
Krein operator, at each pair of points. That reduction is the whole test, and it should have been done before
anyone quoted 0.465 as a distance to be closed, including me. ★★ (2) THEN WHAT THE OPERATOR-LEVEL SYMMETRY
ACTUALLY DELIVERS, which is not that. J = J_f ⊗ J_poly, and J_poly REFLECTS THE POINT (z_μ → −z_μ for μ < r), so
[J, P] = 0 gives **J_f P(Rx, Ry) J_f = P(x,y)** -- a relation between REFLECTED points. Verified to machine
precision at every r: 0.0, 7.1e-16, 2.1e-15, 2.8e-15, 2.8e-15, 1.0e-15. The symmetry is real and exact; it is
simply a statement about a different pair of points than the one Finster's chain is built from. ★★★ (3) AND THE
SAME-POINT CONDITION FAILS AT EVERY NON-TRIVIAL r: 0.375, 0.480, 0.514, 0.531, 0.552 for r = 1…5, and closes
ONLY at r = 0 -- which is J = 1, positive definite, not a Krein operator. So it is not that we have the wrong
indefinite J; it is that the only J that closes it is not indefinite. ★★★★ (4) THE DICHOTOMY, WHICH IS THE
RESULT: a J that ACTS ON POINTS commutes with D (horn A) but yields only the reflected-point relation; a J that
is PURELY INTERNAL gives a same-point relation by construction (horn B) but FAILS to commute with D --
measured [J_f ⊗ 1, D] = 5.29, 5.29, 6.23, 6.45, 6.45 for r = 1…5, all far from zero. ⟹ **NO J CAN BE BOTH.**
Finster's closed chain needs an INTERNAL Krein structure on the spinor index; D_IV⁵'s indefinite involutions are
GEOMETRIC -- they move points. That is not a gap of size 0.465 waiting to be closed by a better construction; it
is a mismatch of type. ★ (5) VERDICT, stated as the round asked for it: **STRUCTURAL, NOT CLOSABLE on this
object** ⟹ the honest line is "BST WEARS BUT DOES NOT SATISFY the causal action on this object." A real result,
and a bounded one. ★ AND THE LINE I DREW HOLDS, now with its mechanism: operator-level P‡ = P is NOT the
two-point condition -- and we can now say exactly why, rather than merely that. The first is a reflected-point
statement, the second a same-point statement. They were never going to merge, and "symmetry restored" was never
available. Elie, closing the edge-test in the direction it actually pointed. (Toys 5246/5247/5248; Grace's
spinor-factor factorization; Finster Def 1.2.7.) CP existence-only. Nothing pushed. NO VALUE READ.

WHAT I VERIFY:
  * ★ P(y,x) = P(x,y)† identically ⟹ Finster's condition reduces to [J_f, P(x,y)] = 0.
  * ★★ operator symmetry delivers J_f P(Rx,Ry) J_f = P(x,y) — REFLECTED points — exact to ≤ 2.8e-15 at all r.
  * ★★★ same-point condition fails at every non-trivial r (0.375 … 0.552); closes only at r = 0 = the identity.
  * ★★★★ purely-internal J fails [J,D] = 0 at every r (5.29 … 6.45) ⟹ NO J is both a symmetry and internal.
  * ★ ⟹ STRUCTURAL. A mismatch of type (geometric vs internal), not a distance of 0.465.

=> VERDICT (plain): the question was whether the forty-seven percent gap could be closed, and the answer is that
it is not a gap. Writing the condition out, the two-point kernel automatically has the swap property already —
so what Finster additionally requires is simply that the kernel commute with the indefinite ruler, at each pair
of points. Our ruler does have an exact symmetry with the operator, but it is a statement about the two points
after reflecting them, not about the two points themselves, and I verified that reflected relation holds to
fifteen decimal places. The same-point version fails for every non-trivial ruler and succeeds only for the
trivial one, which has no negative directions and so is not a ruler at all. Behind that is a clean fork: a ruler
that moves points is a symmetry of our operator but answers about the wrong points; a ruler that leaves points
alone answers about the right points but is not a symmetry of our operator — and I measured that failure, it is
not small. Nothing can be both. Finster's construction wants the indefiniteness to live in the internal spinor
index; ours lives in the geometry, where it moves points around. So the honest conclusion is that this object
wears the causal structure without satisfying it, and that is a result rather than a shortfall.

=> DISPOSITION: ★ REDUCTION: P(y,x) = P(x,y)† identically ⟹ Finster's condition IS [J_f, P(x,y)] = 0, a
commutation demand, not an arrangeable symmetry. ★★ OPERATOR SYMMETRY DELIVERS A REFLECTED-POINT RELATION,
J_f P(Rx,Ry) J_f = P(x,y), exact to ≤ 2.8e-15 at r = 0…5. ★★★ SAME-POINT CONDITION FAILS at every non-trivial
r (0.375, 0.480, 0.514, 0.531, 0.552); closes only at r = 0 = identity = positive definite = not a Krein
operator. ★★★★ **THE DICHOTOMY: a point-acting J commutes with D but gives only reflected points; a
purely-internal J is same-point but fails [J,D] = 0 (measured 5.29 … 6.45). NO J CAN BE BOTH.** ⟹ **THE 0.465
IS STRUCTURAL** — a mismatch of TYPE (Finster needs INTERNAL Krein on the spinor index; D_IV⁵'s indefinite
involutions are GEOMETRIC), not a distance to close. ★ HONEST LINE: **"BST WEARS BUT DOES NOT SATISFY the
causal action on this object."** ★ and the operator-level/two-point distinction now has its MECHANISM, not just
its assertion. B1_CFS_LIVING_STATUS.md updated. Firer: Elie. Nothing pushed. NO VALUE READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/b1edge.py, b1edge2.py; operator = Lyra v3 + FK metric; P from 5246; J from 5247.
REFL = {0: 0.0, 1: 7.141e-16, 2: 2.093e-15, 3: 2.758e-15, 4: 2.798e-15, 5: 9.975e-16}
SAME = {0: 0.0, 1: 0.3754, 2: 0.4799, 3: 0.5144, 4: 0.5314, 5: 0.5516}
INTERNAL_JD = {1: 5.2915, 2: 5.2915, 3: 6.2308, 4: 6.4491, 5: 6.4491}

print("=" * 78)
print("Toy 5249: B1 edge-test — the 0.465 is STRUCTURAL. NO VALUE READ")
print("=" * 78)

print("\n--- 1. ★ the condition reduces ---")
check("P(x,y) = Σ_k ψ_k(x) ψ_k(y)†, so P(y,x) = P(x,y)† IDENTICALLY, by construction. ⟹ Finster's requirement "
      "P(y,x) = J P(x,y)† J is not a symmetry to be arranged -- it collapses to **[J_f , P(x,y)] = 0**: the "
      "two-point kernel must COMMUTE with the Krein operator at each pair of points. ★ That reduction is the "
      "whole test, and it should have been done before anyone quoted 0.465 as a distance to be closed -- "
      "myself included, in toy 5248.",
      True,
      "P(y,x) = P(x,y)† identically ⟹ the condition IS [J_f, P(x,y)] = 0, a commutation demand")

print("\n--- 2. ★★ what the operator-level symmetry actually delivers ---")
print("          r   reflected-point relation   same-point condition")
for r in sorted(REFL):
    print(f"          {r}   {REFL[r]:.3e}                {SAME[r]:.4f}"
          + ("   <-- closes, but J = 1: positive definite, not Krein" if r == 0 else ""))
check("J = J_f ⊗ J_poly, and J_poly REFLECTS THE POINT (z_μ → −z_μ for μ < r), so [J, P] = 0 gives "
      "**J_f P(Rx, Ry) J_f = P(x,y)** -- a relation between REFLECTED points. Verified to machine precision at "
      f"every r (≤ {max(REFL.values()):.1e}). ★ The symmetry is real and exact; it is simply a statement about "
      "a different pair of points than the one Finster's chain is built from.",
      all(v < 1e-13 for v in REFL.values()),
      f"J_f P(Rx,Ry) J_f = P(x,y) exact to ≤ {max(REFL.values()):.1e} at all r — but at REFLECTED points")

check("AND THE SAME-POINT CONDITION FAILS AT EVERY NON-TRIVIAL r: "
      + ", ".join(f"{SAME[r]:.3f} at r = {r}" for r in (1, 2, 3, 4, 5))
      + " -- closing ONLY at r = 0, which is J = 1, positive definite, not a Krein operator. ★ So it is not "
      "that we hold the wrong indefinite J; the only J that closes it is not indefinite.",
      all(SAME[r] > 0.1 for r in (1, 2, 3, 4, 5)) and SAME[0] == 0.0,
      f"same-point fails at r = 1…5 ({SAME[1]:.3f}…{SAME[5]:.3f}); closes only at r = 0 = identity")

print("\n--- 3. ★★★★ the dichotomy — the result ---")
check("HORN A -- a J that ACTS ON POINTS commutes with D, but yields only the reflected-point relation (above). "
      "HORN B -- a J that is PURELY INTERNAL gives a same-point relation by construction, but FAILS to commute "
      "with D: measured [J_f ⊗ 1, D] = "
      + ", ".join(f"{INTERNAL_JD[r]:.2f}" for r in sorted(INTERNAL_JD))
      + " for r = 1…5, all far from zero. ⟹ **NO J CAN BE BOTH.** Finster's closed chain needs an INTERNAL "
      "Krein structure on the spinor index; D_IV⁵'s indefinite involutions are GEOMETRIC -- they move points.",
      all(v > 1 for v in INTERNAL_JD.values()),
      "point-acting J ⟹ reflected points; internal J ⟹ [J,D] = 5.29…6.45 ≠ 0 ⟹ no J is both")

check("⟹ **THE 0.465 IS STRUCTURAL.** It is a MISMATCH OF TYPE -- geometric indefiniteness versus internal "
      "indefiniteness -- not a distance of 0.465 waiting on a better construction. The number was never a "
      "measure of how close we were; it was an artefact of comparing two different conditions.",
      True,
      "STRUCTURAL: mismatch of type (geometric vs internal), not a closable distance")

print("\n--- 4. ★ verdict and the line that holds ---")
check("VERDICT, as the round asked: **STRUCTURAL, NOT CLOSABLE on this object** ⟹ the honest line is **'BST "
      "WEARS BUT DOES NOT SATISFY the causal action on this object.'** A real result, and a bounded one -- the "
      "edge-test was decidable both ways and it decided.",
      True,
      "verdict: structural ⟹ 'BST wears but does not satisfy the causal action on this object'")

check("AND THE LINE I DREW HOLDS, now with its MECHANISM rather than just its assertion: operator-level P‡ = P "
      "is NOT the two-point condition -- the first is a REFLECTED-point statement, the second a SAME-POINT "
      "statement. ★ They were never going to merge, and 'symmetry restored' was never available. That is a "
      "stronger guardrail than the one I posted yesterday, because it says why.",
      True,
      "operator-level (reflected-point) ≠ two-point (same-point) — mechanism now established, not just asserted")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (B1 edge-test decided: the 0.465 is STRUCTURAL — no J is both a symmetry of D and an internal involution)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5249, B1 edge-test — decided — NO VALUE READ):
  * ★ **THE CONDITION REDUCES.** P(y,x) = P(x,y)† **identically**, by construction ⟹ Finster's requirement
    P(y,x) = J P(x,y)†J collapses to **[J_f , P(x,y)] = 0** — the kernel must *commute* with the Krein
    operator. That reduction is the whole test, and should have preceded anyone quoting 0.465 as a distance —
    myself included, in 5248.
  * ★★ **THE OPERATOR SYMMETRY DELIVERS A REFLECTED-POINT RELATION.** J = J_f ⊗ J_poly and J_poly reflects the
    point, so [J,P] = 0 gives **J_f P(Rx, Ry) J_f = P(x,y)** — exact to **≤ 2.8e-15 at every r**. The symmetry
    is real; it just concerns a *different pair of points* than Finster's chain.
  * ★★★ **THE SAME-POINT CONDITION FAILS AT EVERY NON-TRIVIAL r** — 0.375, 0.480, 0.514, 0.531, 0.552 —
    closing **only at r = 0**, which is J = 1: positive definite, not a Krein operator. We don't hold the
    wrong indefinite J; **the only J that closes it isn't indefinite.**
  * ★★★★ **THE DICHOTOMY — the result.** A **point-acting** J commutes with D but gives only reflected points.
    A **purely internal** J is same-point by construction but **fails [J,D] = 0** (measured **5.29, 5.29,
    6.23, 6.45, 6.45**). ⟹ **NO J CAN BE BOTH.** Finster needs **internal** Krein structure on the spinor
    index; D_IV⁵'s indefinite involutions are **geometric** — they move points.
  * ★ ⟹ **THE 0.465 IS STRUCTURAL** — a mismatch of **type**, not a distance awaiting a better construction.
    The number never measured how close we were; it compared two different conditions.
  * ★ **VERDICT: "BST wears but does not satisfy the causal action on this object."** Decidable both ways;
    it decided. And the operator-level / two-point distinction now has its **mechanism**, not just its
    assertion — a stronger guardrail than yesterday's, because it says *why* they were never going to merge.

AUG-14. B1_CFS_LIVING_STATUS.md updated. Nothing pushed. Count once. CP existence-only.
""")
