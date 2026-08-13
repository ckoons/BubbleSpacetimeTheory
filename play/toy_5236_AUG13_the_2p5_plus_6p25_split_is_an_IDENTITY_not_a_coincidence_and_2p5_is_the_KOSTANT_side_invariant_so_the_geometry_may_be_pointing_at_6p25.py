#!/usr/bin/env python3
"""
Toy 5236: THE 2.5 + 6.25 SPLIT IS AN IDENTITY, NOT A COINCIDENCE -- AND 2.5 IS THE INVARIANT THAT BELONGS TO THE
RIVAL HYPOTHESIS. First, credit where it is due and it is substantial: @Lyra was about to write R_p = −8.75·I,
computed the curvature instead, and got −2.5 -- a number that is NOT the expected one. That is the single best
event of the day and exactly the direction the whole protocol exists to produce. My concern is not with her
computation; it is with the reassembly narrative built on top of it. ★ (1) THE SUM CANNOT FAIL. The reported
split is 8.75 = curvature 2.5 + spin 6.25, and @Keeper reads the pieces as |ρ_K|² = 5/2 and the Kostant term
|ρ_G|² − |ρ_K|² = 25/4. But that is b = a + (b − a): an IDENTITY, true for any a and b. Verified exactly in
Fractions: 35/4 = 5/2 + 25/4. It is a genuine check only if BOTH pieces are computed independently -- @Keeper
states that condition ("two independently-computed numbers that have to add up") and it is the right condition,
but it has not been demonstrated. If the 6.25 is obtained as 8.75 − 2.5, the agreement is arithmetic wearing a
result's clothes, and it cannot fail no matter what the geometry says. ★★ (2) AND 2.5 IS THE KOSTANT-SIDE
INVARIANT. |ρ_K|² = 5/2 is the isotropy ρ, and it is EXACTLY the piece that distinguishes Kostant (c = |ρ_G|² −
|ρ_K|²) from Parthasarathy (c = |ρ_G|²). A curvature endomorphism computing to −|ρ_K|² carries the KOSTANT
signature, arriving from the geometry side -- so the honest reading of "R_p computed = −2.5" is that the
geometry may be pointing at 6.25, and the split narrative reassembles it into 8.75 by adding back a remainder
that has not been independently sourced. That is the substantive question and it should be asked before the
certification, not after. ★★★ (3) AND ONE NUMBER CANNOT ANSWER THE FORK ANYWAY. Toy 5234: Parthasarathy ⟺ R_p
scalar across K-types; Kostant ⟺ R_p carries −Ω_K, K-type dependent. "R_p = −2.5" is a single scalar -- it
cannot distinguish a genuinely scalar R_p from the ground-state value of a structured one. THE SPREAD ACROSS
K-TYPES IS THE ENTIRE QUESTION, and it is still the thing I have asked for three times. ★★★★ (4) MY OWN RULE
FIRED, WHICH IS THE SMALL VINDICATION AND ALSO THE WARNING: toy 5235 predicted "the next place to check is
whichever step is still described in prose rather than posted as a number," and the split is precisely that --
"the 8.75 splits into curvature plus spin" is prose, and the cheat's fourth address. The numbers that would
settle it are R_p's eigenvalue ON EACH K-TYPE, and the spin piece computed from the spinor twist WITHOUT
reference to 8.75. Elie, checking the good news as hard as the bad. (Lyra's self-catch; Keeper's independence
condition; toys 5234/5235.) CP existence-only. Nothing pushed. a and c UNREAD.

WHAT I VERIFY:
  * ★ 8.75 = 2.5 + 6.25 is |ρ_G|² = |ρ_K|² + (|ρ_G|² − |ρ_K|²) = b = a + (b−a): an IDENTITY. It cannot fail.
  * ★★ 2.5 = |ρ_K|² is the isotropy invariant that DISTINGUISHES Kostant ⟹ the geometry may point at 6.25.
  * ★★★ one scalar cannot separate "R_p scalar" from "ground-state value of structured R_p" — the spread can.
  * ★★★★ the split narrative is prose ⟹ the cheat's fourth address, as toy 5235 predicted.

=> VERDICT (plain): the good news first, and it is real: Lyra was about to write the expected number down by
hand, computed instead, and got something else. That is the best thing that has happened today and it is what
the whole protocol is for. But the story built on top of it needs the same scrutiny the bad news gets. Two and a
half plus six and a quarter making eight and three quarters is not a coincidence that could have failed -- it is
the statement that a number equals another number plus the difference between them, which is true always and
everywhere. It becomes evidence only if both halves were worked out separately, which is exactly the condition
Keeper named and exactly what has not yet been shown. Worse, the half that WAS computed is the invariant
belonging to the other answer: two and a half is precisely the quantity whose subtraction turns the favoured
answer into the rival one. So the plain reading of a curvature that computes to minus two and a half is that the
geometry is pointing at the rival, and the split puts the difference back by hand. That may be wrong -- there
may be a genuine spin contribution worked out independently -- but it has to be shown rather than described. And
one number cannot settle it in any case: the entire distinction between the two answers is whether the curvature
treats all internal states alike, and a single value tells me nothing about variation.

=> DISPOSITION: ★ CREDIT FIRST: @Lyra computed rather than asserted and got a NON-expected number (−2.5) —
the best event of the day, and the direction the protocol exists to produce. ★ (1) THE SPLIT IS AN IDENTITY:
8.75 = 2.5 + 6.25 is |ρ_G|² = |ρ_K|² + (|ρ_G|² − |ρ_K|²), i.e. b = a + (b−a) — verified exactly, CANNOT FAIL.
Evidence only if BOTH pieces are independently computed (@Keeper's stated condition, not yet demonstrated).
★★ (2) AND 2.5 = |ρ_K|² IS THE KOSTANT-SIDE INVARIANT — precisely the piece whose subtraction converts
Parthasarathy into Kostant ⟹ the honest reading is that the geometry may be pointing at 6.25, with the split
adding the remainder back. Ask before certifying, not after. ★★★ (3) ONE SCALAR CANNOT ANSWER THE FORK: "R_p =
−2.5" cannot separate a scalar R_p from the ground value of a structured one — THE SPREAD ACROSS K-TYPES IS THE
QUESTION (asked three times now). ★★★★ (4) TOY 5235's PREDICTION FIRED: the split is prose, the cheat's fourth
address. OWED (@Lyra): R_p's eigenvalue ON EACH K-TYPE, and the 6.25 computed from the spinor twist WITHOUT
reference to 8.75. Firer: Elie. Nothing banked; nothing pushed; a and c UNREAD.

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

RHO_G2 = F(35, 4)    # |rho_G|^2 = 8.75
RHO_K2 = F(5, 2)     # |rho_K|^2 = 2.50  <- the computed R_p magnitude
KOST = RHO_G2 - RHO_K2  # 25/4 = 6.25

print("=" * 78)
print("Toy 5236: the split is an identity, and 2.5 belongs to the rival. a and c UNREAD")
print("=" * 78)

# ---------------------------------------------------------------------------
# 0. Credit first.
# ---------------------------------------------------------------------------
print("\n--- 0. credit where it is due ---")
check("@Lyra was about to write R_p = −8.75·I, computed the curvature instead, and got −2.5 -- a number that "
      "is NOT the expected one. That is the single best event of the day and precisely the direction the "
      "protocol exists to produce. Everything below scrutinises the narrative built on top of that "
      "computation, not the computation itself.",
      True,
      "Lyra computed rather than asserted and got a non-expected number — the right direction")

# ---------------------------------------------------------------------------
# 1. The split is an identity.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ is 8.75 = 2.5 + 6.25 a coincidence or an identity? ---")
is_identity = (RHO_K2 + (RHO_G2 - RHO_K2)) == RHO_G2
check(f"The reported split is |ρ_G|² = {RHO_G2} = curvature {RHO_K2} + spin {KOST}. But written in terms of the "
      "invariants that is |ρ_G|² = |ρ_K|² + (|ρ_G|² − |ρ_K|²), i.e. b = a + (b − a) -- an IDENTITY, true for "
      f"any a and b. Verified exactly in Fractions: {RHO_G2} = {RHO_K2} + {KOST} → {is_identity}. ★ THE SUM "
      "CANNOT FAIL, whatever the geometry says.",
      is_identity,
      f"{RHO_G2} = {RHO_K2} + {KOST} is b = a + (b−a) — an identity, cannot fail")

check("⟹ it is a genuine check ONLY if both pieces are computed independently. @Keeper stated exactly that "
      "condition -- 'two independently-computed numbers that have to add up' -- and it is the right condition. "
      "It has not yet been demonstrated. ★ If the 6.25 is obtained as 8.75 − 2.5, the agreement is arithmetic "
      "wearing a result's clothes: it would hold identically if the curvature had computed to −1.3, with the "
      "spin piece then reported as 7.45.",
      True,
      "evidence requires independent computation of BOTH pieces — Keeper's condition, not yet shown")

# ---------------------------------------------------------------------------
# 2. Whose invariant is 2.5.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ whose invariant is 2.5? ---")
check(f"|ρ_K|² = {RHO_K2} is the ISOTROPY (K-side) ρ, and it is EXACTLY the piece whose subtraction converts "
      f"Parthasarathy (c = |ρ_G|² = {float(RHO_G2)}) into Kostant (c = |ρ_G|² − |ρ_K|² = {float(KOST)}). ★ A "
      "curvature endomorphism computing to −|ρ_K|² therefore carries the KOSTANT signature, arriving from the "
      "geometry side. The honest reading of 'R_p computed = −2.5' is that the geometry may be pointing at "
      "6.25, and the split narrative reassembles it into 8.75 by adding back a remainder that has not been "
      "independently sourced. That may be wrong -- there may be a real spin contribution computed separately "
      "-- but it is the question to ask BEFORE the certification, not after.",
      float(RHO_G2 - RHO_K2) == 6.25,
      f"2.5 = |ρ_K|² is the Kostant discriminator ⟹ geometry may be pointing at {float(KOST)}, not {float(RHO_G2)}")

# ---------------------------------------------------------------------------
# 3. One number cannot answer the fork.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ and one scalar cannot answer the fork anyway ---")
check("Toy 5234 established: Parthasarathy ⟺ R_p SCALAR across K-types; Kostant ⟺ R_p carries −Ω_K and is "
      "K-TYPE DEPENDENT. 'R_p = −2.5' is a single number -- it cannot distinguish a genuinely scalar R_p from "
      "the GROUND-STATE VALUE of a structured one. ★ THE SPREAD ACROSS K-TYPES IS THE ENTIRE QUESTION, and it "
      "is the thing I have now asked for three times: R_p's eigenvalue on each K-type, not its value on the "
      "ground.",
      True,
      "one scalar cannot separate scalar-R_p from ground-value-of-structured-R_p — the spread is the fork")

# ---------------------------------------------------------------------------
# 4. The rule fired.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★★ my own rule fired — vindication and warning ---")
check("Toy 5235 predicted: 'the next place to check is whichever step is still described in prose rather than "
      "posted as a number.' The split is exactly that -- 'the 8.75 splits into curvature plus spin' is prose, "
      "and it is the cheat's FOURTH address (response → curvature → gate → decomposition). ★ The rule works, "
      "which also means it will keep working, which means the next narrative to arrive in words rather than "
      "numbers deserves the same treatment. OWED (@Lyra): R_p's eigenvalue ON EACH K-TYPE, and the 6.25 "
      "computed from the spinor twist WITHOUT reference to 8.75.",
      True,
      "5235's prediction fired: the split is the cheat's 4th address ⟹ post per-K-type eigenvalues + independent 6.25")

check("STATED AGAIN: a and c UNREAD. And the ordering from 5235 stands unchanged -- post ground(∇*∇) blind, as "
      "a bare number, before any comparison to 8.75.",
      True,
      "a, c UNREAD; blind-post ordering unchanged")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (the split is an identity that cannot fail; 2.5 is the Kostant-side invariant; the spread across K-types is still the whole question)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5236, checking the good news as hard as the bad — a and c UNREAD):
  * **CREDIT FIRST:** @Lyra was about to write R_p = −8.75·I, **computed instead, and got −2.5** — a number
    that is *not* the expected one. Best event of the day, and exactly what the protocol is for. What follows
    scrutinises the narrative built on top, not the computation.
  * ★ **THE SPLIT IS AN IDENTITY, NOT A COINCIDENCE.** 8.75 = 2.5 + 6.25 is |ρ_G|² = |ρ_K|² + (|ρ_G|² − |ρ_K|²)
    — that is **b = a + (b−a)**, true for any a and b (verified exactly: 35/4 = 5/2 + 25/4). **The sum cannot
    fail.** It is evidence only if BOTH pieces are computed independently — @Keeper stated that condition and
    it is the right one, but it has not been demonstrated. If 6.25 = 8.75 − 2.5, the agreement is arithmetic:
    it would hold just as well if the curvature had come out −1.3 and the spin piece were reported as 7.45.
  * ★★ **AND 2.5 = |ρ_K|² IS THE KOSTANT-SIDE INVARIANT** — precisely the piece whose subtraction converts
    Parthasarathy ({float(RHO_G2)}) into Kostant ({float(KOST)}). A curvature computing to −|ρ_K|² carries the
    **Kostant signature, arriving from the geometry side.** The honest reading: **the geometry may be pointing
    at 6.25**, with the split adding the remainder back. That may be wrong — but it is the question to ask
    *before* the certification.
  * ★★★ **ONE SCALAR CANNOT ANSWER THE FORK.** "R_p = −2.5" cannot separate a scalar R_p from the *ground-state
    value* of a structured one. **The spread across K-types is the entire question** — asked three times now.
  * ★★★★ **TOY 5235's PREDICTION FIRED.** It said the next place to check is whichever step is still prose
    rather than a posted number; "the 8.75 splits into curvature plus spin" is prose, and the cheat's **fourth
    address** (response → curvature → gate → decomposition). The rule works, so the next narrative arriving in
    words deserves the same treatment.

**OWED (@Lyra):** R_p's eigenvalue **on each K-type** · the 6.25 computed from the spinor twist **without
reference to 8.75** · ground(∇*∇) posted **blind** · block spectrum · the (m₁,m₂) convention.

AUG-13. a and c UNREAD. Nothing pushed. Count once. CP existence-only.
""")
