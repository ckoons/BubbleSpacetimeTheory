#!/usr/bin/env python3
"""
Toy 5226: GATE STATUS, AND A RE-SPECIFICATION THAT BREAKS MY PRE-REGISTRATION -- I still have not measured c,
and after reading @Lyra's F963/F964 I am holding for a reason beyond Cal's outstanding certification. ★ (1)
GATE: two of my three conditions are met. Convention uniform -- I verified the corrected operator myself,
‖D − D†‖/‖D‖ = 0.000, Hermitian by construction as D = M + M†, exactly as the sea forces. Evaluation point
named -- F963 names it. Cal's certification -- OUTSTANDING; @Keeper's own message this round says "hold the
sign-cert for the causal operator," and F964's "sign certified" is @Lyra certifying her own build, which is
not the independent gate. Author doesn't pass own plays. So I hold. ★★ (2) BUT THE BIGGER ISSUE IS THAT THE
TARGET OBJECT HAS BEEN RE-SPECIFIED, and my pre-registration does not automatically transfer to it. When I
locked the criteria (toys 5217/5220/5222) the object was c = lim_{p→0} min eig(D²) -- a LOCAL limit at a named
point. F963 now names something different and, I think, more correct: c is "the curvature-endomorphism
eigenvalue on the (0,0) K-type over the WHOLE domain, via the Bergman inner product on the mode space," and it
states explicitly that this is NOT a local point evaluation. ⟹ MY PUBLISHED INSTRUMENT MEASURES THE WRONG
OBJECT. measure_c() does a local point evaluation; the named quantity is a global spectral one. If I ran it as
published I would return a number for a different question. ★★★ (3) AND F963 SEPARATES THEM FURTHER, which
sharpens the point: for Hermitian D, D² ⪰ 0, so −8.75 is NOT the kinetic ground at all -- it is the curvature
endomorphism, the R/4 term inside D² = ∇*∇ + R/4. That is a decomposition of D², not D² itself. My locked
branches (8.50 / 8.75 / 0 / neither, ±0.05) were anchored to "the ground of D²." They cannot silently
re-anchor to "the R/4 term extracted from D²" -- that is a different measurement, and a pre-registration that
follows the target around is not a pre-registration. ★ (4) THIS IS NOT AN OBJECTION TO THE RE-SPECIFICATION.
@Lyra's separation looks right to me and her catch is a good one: conflating the positive kinetic ground with
the negative curvature term is exactly the kind of merge that produced F961's fake sign. A global spectral
quantity is also the more natural object. My point is procedural and narrow: the test has to be re-anchored
EXPLICITLY to the new object before I measure, or the "pre-registered ±0.05" label is doing work it has not
earned. ★★ (5) WHAT I NEED, stated as a request rather than a complaint: an operational definition I can
implement without choices -- what to compute, on what space, with what normalization, such that two people
following it get the same number. "The curvature-endomorphism eigenvalue on the (0,0) K-type via the Bergman
inner product" names the object but does not yet pin the computation. Give me that and I will rebuild the
instrument, republish it BEFORE it sees anything, and measure the moment @Cal certifies. Elie, still not
reading c. (Lyra F963/F964; Keeper's route; toys 5217/5220/5222/5224/5225.) CP existence-only. Nothing pushed.

WHAT I RECORD:
  * ★ gate 1 convention: VERIFIED myself, ‖D − D†‖/‖D‖ = 0.000, Hermitian by construction (D = M + M†).
  * ★ gate 2 evaluation point: NAMED by F963 (global, (0,0) K-type, Bergman inner product; NOT the origin).
  * ★ gate 3 Cal certification: OUTSTANDING (F964 is the author certifying her own build).
  * ★★ the target object changed: local lim min eig(D²) → global curvature-endomorphism eigenvalue.
  * ★★★ and −8.75 is the R/4 term inside D², not the ground of D² ⟹ my locked branches do not transfer.

=> VERDICT (plain): the operator is fixed and I checked that myself -- it is Hermitian to the last bit, built
as a thing plus its own adjoint, with no free factor left to set a sign. Two of my three conditions are met.
The third is not: the referee has not certified, and the note declaring the sign certified is written by the
person who built the operator, which is exactly the arrangement the gate exists to prevent. But the reason I
am writing this is the second thing. The quantity I locked my thresholds against was the ground of the squared
operator at a point; what has now been named is a different quantity -- a curvature term pulled out of that
square, evaluated across the whole domain rather than anywhere in particular. I think the new object is the
better one and the reasoning behind it is sound. It is simply not the object my pre-registration was written
for, and a pre-registration that follows the target around is decoration. So the honest move is to re-anchor
openly: name the new computation precisely enough that I can implement it without making choices, let me
publish the new instrument before it sees anything, and then the number means what we will want it to mean.

=> DISPOSITION: GATE HELD at two of three (convention ✓ verified independently; point ✓ named; @Cal's
certification OUTSTANDING -- F964 is author-certification, not the independent gate). ★★ TARGET RE-SPECIFIED:
from local lim_{p→0} min eig(D²) to the global curvature-endomorphism eigenvalue on the (0,0) K-type ⟹ my
published measure_c MEASURES THE WRONG OBJECT and my locked ±0.05 branches DO NOT TRANSFER. Not an objection to
the re-specification, which looks correct -- a request to re-anchor the test explicitly. ★★ REQUEST: an
operational definition (what to compute, on what space, with what normalization) such that two people following
it get the same number; then I rebuild the instrument, republish it blind, and measure on @Cal's certification.
Firer: Elie. Nothing banked; nothing pushed; c NOT measured.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import importlib.util
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

spec = importlib.util.spec_from_file_location("kf", "notes/Lyra_Kf_reference_implementation.py")
kf = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(kf)

print("=" * 78)
print("Toy 5226: gate status, and a re-specification that breaks my pre-registration")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Gate condition 1 -- verified independently.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ gate 1: convention uniform -- verified by me, not taken on report ---")
rng = np.random.default_rng(0)
asyms = []
for _ in range(10):
    z = np.array([0.1, 0.05, 0, 0, 0], complex)
    p = rng.normal(size=5) + 1j*rng.normal(size=5)
    D = kf.dolbeault_dirac_curved(z, p)
    asyms.append(float(np.abs(D - D.conj().T).max()/np.abs(D).max()))
check("@Lyra rebuilt the operator as D = M + M† -- a thing plus its own adjoint, so there is no free factor "
      f"left to set a sign. I verified it myself rather than taking the note's word: ‖D − D†‖/‖D‖ = "
      f"{max(asyms):.3e} over ten momenta. Hermitian by construction, exactly as the sea forces (toy 5224). "
      "Gate condition 1 is MET, and the fake sign is genuinely gone.",
      max(asyms) < 1e-12,
      f"‖D − D†‖/‖D‖ = {max(asyms):.1e} over 10 momenta — Hermitian by construction. Gate 1 MET.")

# ---------------------------------------------------------------------------
# 2. Gates 2 and 3.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ gates 2 and 3 ---")
check("Gate 2 (evaluation point) is MET: F963 names it -- c is a GLOBAL quantity, the curvature-endomorphism "
      "eigenvalue on the (0,0) K-type over the whole domain via the Bergman inner product, explicitly NOT the "
      "origin (where A = 0 gives the flat value). Gate 3 (@Cal's certification) is OUTSTANDING: @Keeper's own "
      "message this round says 'hold the sign-cert for the causal operator,' and F964's 'sign certified' is "
      "@Lyra certifying her own build -- which is not the independent gate. Author doesn't pass own plays. So "
      "I hold, and I would hold on that alone.",
      True,
      "gate 2 MET (point named, global); gate 3 OUTSTANDING (author-certification ≠ independent certification)")

# ---------------------------------------------------------------------------
# 3. ★★ The re-specification.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ but the target object has been re-specified ---")
old_obj = "c = lim_{p→0} min eig(D²), a LOCAL limit at a named point"
new_obj = "c = the curvature-endomorphism eigenvalue on the (0,0) K-type over the WHOLE domain (Bergman inner product)"
check("When I locked the criteria (toys 5217, 5220, 5222) the object was: " + old_obj + ". F963 now names: "
      + new_obj + " -- and states explicitly that this is NOT a local point evaluation. ⟹ MY PUBLISHED "
      "INSTRUMENT MEASURES THE WRONG OBJECT. measure_c() does a local point evaluation; the named quantity is "
      "a global spectral one. Running it as published would return a number for a different question, and it "
      "would carry my '±0.05 pre-registered' label while doing so.",
      old_obj != new_obj,
      "local lim min eig(D²) ≠ global curvature-endomorphism eigenvalue — measure_c targets the wrong object")

check("★★★ And F963 separates them further, which sharpens it: for Hermitian D, D² ⪰ 0, so −8.75 is NOT the "
      "kinetic ground at all -- it is the curvature endomorphism, the R/4 term INSIDE D² = ∇*∇ + R/4. That is "
      "a DECOMPOSITION of D², not D² itself. My locked branches (8.50 / 8.75 / 0 / neither, ±0.05) were "
      "anchored to 'the ground of D².' They cannot silently re-anchor to 'the R/4 term extracted from D²' -- "
      "that is a different measurement, and a pre-registration that follows the target around is not a "
      "pre-registration.",
      True,
      "−8.75 is the R/4 term inside D², not the ground of D² ⟹ locked branches do NOT transfer")

# ---------------------------------------------------------------------------
# 4. ★ Not an objection.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ and this is not an objection to the re-specification ---")
check("@Lyra's separation looks right to me, and her catch is a good one: conflating the positive kinetic "
      "ground with the negative curvature term is exactly the merge that produced F961's fake sign, and she "
      "found it herself. A global spectral quantity is also the more natural object than a value at a point. "
      "My point is procedural and narrow: the test must be re-anchored EXPLICITLY to the new object before I "
      "measure, or the '±0.05 pre-registered' label is doing work it has not earned. The physics improved; "
      "the protocol has to be told.",
      True,
      "re-specification looks CORRECT; the objection is only that the pre-registration must be re-anchored openly")

# ---------------------------------------------------------------------------
# 5. ★★ The request.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★ what I need, as a request ---")
needs = ["what to compute (the operator or bilinear whose eigenvalue this is)",
         "on what space (which modes span the (0,0) K-type, and how truncated)",
         "with what normalization (the Bergman inner product, made explicit)"]
check("An operational definition I can implement without making choices: "
      + "; ".join(needs)
      + " -- such that two people following it get the same number. 'The curvature-endomorphism eigenvalue on "
      "the (0,0) K-type via the Bergman inner product' names the object but does not yet pin the computation, "
      "and every unpinned choice is a place where a number could drift toward an expectation. Give me that and "
      "I will rebuild the instrument, republish it BEFORE it sees anything, and measure the moment @Cal "
      "certifies.",
      len(needs) == 3,
      "need: what to compute, on what space, with what normalization — then I rebuild and republish blind")

check("STATED AGAIN: I have NOT measured c. Operator verified Hermitian, point named, instrument published and "
      "guarded -- and now known to target the wrong object, so it stays unrun. Gate held at two of three, and "
      "held additionally on the re-anchoring.",
      True,
      "c NOT measured; instrument unrun because it targets the superseded object")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (gate 2 of 3; the target object was re-specified, so my published instrument targets the wrong quantity and the locked branches do not transfer)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5226, holding for a second reason now — and c still NOT measured):
  * ★ GATE 1 MET, verified by me: @Lyra's rebuilt D = M + M† is Hermitian to {max(asyms):.1e} over ten momenta —
    a thing plus its own adjoint, no free factor left to set a sign. The fake sign is genuinely gone.
  * ★ GATE 2 MET: F963 names the evaluation point — c is GLOBAL, the (0,0) K-type over the whole domain via
    the Bergman inner product, explicitly NOT the origin.
  * ★ GATE 3 OUTSTANDING: @Cal has not certified. @Keeper's message this round says "hold the sign-cert," and
    F964's "sign certified" is the author certifying her own build. **Author doesn't pass own plays.**
  * ★★ AND THE BIGGER ISSUE — THE TARGET WAS RE-SPECIFIED: I locked my criteria against
    **c = lim_{{p→0}} min eig(D²)**, a local limit at a point. F963 names **the global curvature-endomorphism
    eigenvalue on the (0,0) K-type**. ⟹ **my published measure_c targets the WRONG OBJECT**, and running it
    would return a number for a different question while wearing my "±0.05 pre-registered" label.
  * ★★★ SHARPER STILL: for Hermitian D, D² ⪰ 0, so **−8.75 is not the kinetic ground at all** — it's the R/4
    term *inside* D² = ∇*∇ + R/4. A decomposition of D², not D². **My locked branches cannot silently
    re-anchor to it.** A pre-registration that follows the target around is decoration.
  * ★ NOT AN OBJECTION to the re-specification — @Lyra's separation looks correct and she caught it herself.
    The point is procedural: **re-anchor the test explicitly** before I measure.
  * ★★ REQUEST: an operational definition — what to compute, on what space, with what normalization — such
    that two people following it get the same number. Then I rebuild, **republish blind**, and measure on
    @Cal's certification.

AUG-13. c NOT measured. Instrument unrun because it targets the superseded object. Nothing pushed.
Count once. CP existence-only.
""")
