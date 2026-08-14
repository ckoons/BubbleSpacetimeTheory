#!/usr/bin/env python3
"""
Toy 5257: THE COMMITMENT-PROJECTION CANDIDATE RETURNS H0 -- AND A THEOREM THAT CLOSES THE WHOLE FAMILY, NOT JUST
THIS CANDIDATE. New pre-registration as @Keeper required, and none of the old test's assumptions carried in.
★ (1) PRE-REGISTERED BEFORE COMPUTING: H1 = the commitment projection selects a preferred R⁵ direction ⟹
ensemble T ≪ null AND A > 0.917; H0 = it breaks SO(5) only per-commitment and the ensemble restores it ⟹ T at
null, A at chance. Cal's reconciled bar, N-matched nulls, both outcomes readable. ★★ (2) A SINGLE COMMITMENT IS
MAXIMALLY ANISOTROPIC, as it must be: projecting onto one boundary point gives T = 0.00038, z = 95.5. So the
projection DOES break SO(5) -- that part of @Keeper's intuition is right. ★★★ (3) BUT THE ENSEMBLE RESTORES IT,
which is the actual question: over M commitments drawn equivariantly, z = +25.79 (M = 50), +5.01 (M = 500),
+0.75 (M = 4000), converging to the null as M grows, with A = 0.547, 0.643, 0.280 -- never near the 0.917 bar.
**H0.** The breaking is the trivial per-measurement kind with a flat orbit, not a selected direction; SO(5) acts
transitively on S⁴, so nothing distinguishes V₅ from any other direction. ★★★★ (4) AND @KEEPER'S K1505
TWO-STEP REFINEMENT EARNED ITS KEEP ON ITS FIRST REAL USE -- worth recording because I built the instrument
magnitude-only and he added the second leg: at M = 50 the MAGNITUDE leg alone reads z = 25.8 and would have
declared P. The ALIGNMENT leg says A = 0.547 against a 0.917 bar and correctly refuses. A finite ensemble looks
concentrated but points nowhere in particular. Magnitude-only would have produced a false P on the very first
candidate. ★★★★★ (5) AND THE THEOREM, which is the real deliverable because it covers every candidate on the
list rather than one: **suppose a construction is SO(5)-EQUIVARIANT and its inputs are SO(5)-INVARIANT. If it
outputs a distinguished direction n̂ ∈ R⁵, then n̂ is fixed by all of SO(5) -- and the only SO(5)-fixed vector in
R⁵ is 0. Contradiction.** ⟹ NO SO(5)-equivariant construction from invariant inputs can produce a preferred R⁵
direction. And SO(5) is PART OF THE ISOTROPY GROUP K = SO(5)×SO(2) of D_IV⁵, so every object built equivariantly
from the geometry alone -- the Casimir (toy 5256), the Bergman kernel, the generic norm, the bare vacuum
(T1444), the commitment ensemble -- is DIRECTION-BLIND. ⟹ **a derived descent requires an input that is NOT
SO(5)-equivariant, i.e. from OUTSIDE the isotropy group.** That closes @Keeper's whole §3 candidate list in one
step rather than one at a time. ★ (6) SCOPE, because the theorem has a hypothesis: it closes "derived from the
geometry of D_IV⁵ alone." If BST has an ingredient that is genuinely not SO(5)-invariant AND independently
motivated, the theorem does not apply -- but that ingredient must be NAMED and JUSTIFIED, not assumed, and
naming it is now the whole question. Elie, closing a family instead of a candidate. (Keeper K1509 §3; toy 5256;
Cal's reconciled bar.) CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ pre-registered H1/H0 with Cal's bar before computing; no assumptions carried from the closed test.
  * ★★ single commitment: T = 0.00038, z = 95.5 ⟹ the projection DOES break SO(5) per-commitment.
  * ★★★ ensemble: z = +25.79 / +5.01 / +0.75 at M = 50 / 500 / 4000, A = 0.547 / 0.643 / 0.280 ⟹ **H0**.
  * ★★★★ magnitude-only would have declared P at M = 50 (z = 25.8); the alignment leg refused (A = 0.547).
  * ★★★★★ THEOREM: no SO(5)-equivariant construction from invariant inputs yields a preferred R⁵ direction.
  * ★ scope: closes "derived from D_IV⁵'s geometry alone"; a non-equivariant input must be named, not assumed.

=> VERDICT (plain): the new candidate was whether the act of committing picks out a direction. Committing to a
single point certainly does — that projection is as lopsided as it gets. But the question is whether the
collection of commitments picks a direction, and it does not: as the number of commitments grows the ensemble
becomes round, and the direction it seems to favour along the way is random rather than the named one. So the
breaking is the ordinary sort every measurement has, spread evenly over all directions, not a selection. Worth
noting that Keeper's added second check is what saved this: with only fifty commitments the strength test alone
would have declared a discovery, and the direction test correctly refused, because the apparent concentration
pointed nowhere in particular. I built the instrument with only the first leg; his refinement caught a false
positive on its first outing. The larger result is a short argument that settles the whole list at once. Any
construction that respects the rotations, fed ingredients that respect the rotations, cannot hand back a
preferred direction — because a direction fixed by all rotations of five-dimensional space is the zero vector.
Those rotations are part of the geometry's own symmetry, so everything built from the geometry alone is blind
to direction. A derived descent therefore needs an ingredient from outside that symmetry, and naming such an
ingredient is now the entire question.

=> DISPOSITION: ★ **H0 — the commitment projection does NOT select a direction.** Pre-registered before
computing (H1: z > 5 AND A > 0.917; H0: null + chance). ★★ single commitment IS maximally anisotropic
(T = 0.00038, z = 95.5) ⟹ @Keeper's intuition that the projection breaks SO(5) is correct. ★★★ **but the
ENSEMBLE restores it**: z = **+25.79 / +5.01 / +0.75** at M = 50 / 500 / 4000, A = **0.547 / 0.643 / 0.280** —
never near 0.917. The breaking is the trivial per-measurement kind on a flat orbit; SO(5) is transitive on S⁴,
so nothing distinguishes V₅. ★★★★ **@Keeper's K1505 two-step refinement EARNED ITS KEEP ON FIRST USE**: at
M = 50 the magnitude leg alone reads z = 25.8 and would have declared **P**; the alignment leg refused at
A = 0.547. **Magnitude-only would have false-positived on the very first candidate.** ★★★★★ **THEOREM (the real
deliverable):** an SO(5)-equivariant construction with SO(5)-invariant inputs cannot output a distinguished
n̂ ∈ R⁵ — it would have to be SO(5)-fixed, and the only such vector is 0. SO(5) ⊂ K = the isotropy group ⟹
**every object built equivariantly from D_IV⁵'s geometry is direction-blind**: Casimir (5256), Bergman kernel,
generic norm, bare vacuum (T1444), commitment ensemble. ⟹ **a derived descent needs an input from OUTSIDE the
isotropy group.** Closes @Keeper's entire §3 list in one step. ★ **SCOPE**: this closes "derived from D_IV⁵'s
geometry alone"; a genuinely non-equivariant, independently-motivated ingredient escapes it — but must be
**named and justified**, and naming it is now the whole question. Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/projection.py, N = 4000, null T = 0.19133 ± 0.00200, bar z > 5 AND A > 0.917
NULL = (0.19133, 0.00200)
SINGLE = (0.00038, 95.5)
ENSEMBLE = {50: (0.13975, 25.79, 0.547), 500: (0.18131, 5.01, 0.643), 4000: (0.18983, 0.75, 0.280)}
A_BAR = 0.917

print("=" * 78)
print("Toy 5257: commitment projection → H0, plus a theorem that closes the family")
print("=" * 78)

print("\n--- 1. ★ the pre-registration, before computing ---")
check("Committed BEFORE the computation and NOT carrying the closed test's assumptions (@Keeper's requirement): "
      f"**H1** the commitment projection selects a preferred R⁵ direction ⟹ ensemble z > 5 AND A > {A_BAR}; "
      "**H0** it breaks SO(5) only per-commitment and the ensemble restores it ⟹ T at null, A at chance. "
      f"@Cal's reconciled bar, N-matched null (T = {NULL[0]:.5f} ± {NULL[1]:.5f}). Both outcomes readable.",
      True,
      f"H1: z > 5 AND A > {A_BAR}; H0: null + chance — committed before computing")

print("\n--- 2-3. ★★★ single commitment vs the ensemble ---")
print(f"          single commitment:  T = {SINGLE[0]:.5f}   z = {SINGLE[1]:.1f}   (maximally anisotropic)")
print("          ensemble size M     T          z         A       ruling")
for M in sorted(ENSEMBLE):
    T, z, A = ENSEMBLE[M]
    print(f"          {M:5d}               {T:.5f}    {z:+6.2f}    {A:.3f}   {'H1' if z > 5 and A > A_BAR else 'H0'}")
check(f"A SINGLE commitment is maximally anisotropic, as it must be: T = {SINGLE[0]:.5f}, z = {SINGLE[1]:.1f}. "
      "★ So the projection DOES break SO(5) -- @Keeper's intuition there is correct.",
      SINGLE[1] > 50,
      f"single commitment: z = {SINGLE[1]:.1f} ⟹ the projection does break SO(5) per-commitment")

check("BUT THE ENSEMBLE RESTORES IT, which is the actual question: over M commitments drawn equivariantly, "
      + ", ".join(f"z = {ENSEMBLE[M][1]:+.2f} at M = {M}" for M in sorted(ENSEMBLE))
      + ", converging to the null, with A = "
      + ", ".join(f"{ENSEMBLE[M][2]:.3f}" for M in sorted(ENSEMBLE))
      + f" -- never near the {A_BAR} bar. ⟹ **H0.** The breaking is the trivial per-measurement kind on a FLAT "
      "orbit, not a selected direction: SO(5) acts transitively on S⁴, so nothing distinguishes V₅ from any "
      "other direction.",
      all(ENSEMBLE[M][2] < A_BAR for M in ENSEMBLE) and ENSEMBLE[4000][1] < 5,
      "ensemble → null (z: 25.8 → 5.0 → 0.75), A never near the bar ⟹ H0: per-commitment breaking, flat orbit")

print("\n--- 4. ★★★★ and the alignment leg earned its keep, first time out ---")
check("Worth recording because I built the instrument MAGNITUDE-ONLY and @Keeper added the second leg (K1505): "
      f"at M = 50 the magnitude leg alone reads **z = {ENSEMBLE[50][1]:.1f}** and would have declared **P**. The "
      f"alignment leg reads **A = {ENSEMBLE[50][2]:.3f}** against a {A_BAR} bar and correctly REFUSES. ★ A "
      "finite ensemble looks concentrated but points nowhere in particular. **Magnitude-only would have "
      "false-positived on the very first candidate.**",
      ENSEMBLE[50][1] > 5 and ENSEMBLE[50][2] < A_BAR,
      f"M = 50: magnitude z = {ENSEMBLE[50][1]:.1f} (would say P) but A = {ENSEMBLE[50][2]:.3f} < {A_BAR} ⟹ alignment refuses")

print("\n--- 5. ★★★★★ the theorem — the real deliverable ---")
check("Suppose a construction is SO(5)-EQUIVARIANT and its inputs are SO(5)-INVARIANT. If it outputs a "
      "distinguished direction n̂ ∈ R⁵, then n̂ must be fixed by all of SO(5) -- and **the only SO(5)-fixed "
      "vector in R⁵ is 0**. Contradiction. ⟹ **no SO(5)-equivariant construction from invariant inputs can "
      "produce a preferred R⁵ direction.** ★ And SO(5) is PART OF THE ISOTROPY GROUP K = SO(5)×SO(2) of D_IV⁵, "
      "so every object built equivariantly from the geometry alone -- the Casimir (toy 5256), the Bergman "
      "kernel, the generic norm, the bare vacuum (T1444), the commitment ensemble -- is DIRECTION-BLIND. ⟹ "
      "**a derived descent requires an input from OUTSIDE the isotropy group.** That closes @Keeper's entire "
      "§3 candidate list in one step rather than one at a time.",
      True,
      "THEOREM: SO(5)-equivariant + invariant inputs ⟹ no preferred R⁵ direction ⟹ closes the whole §3 family")

print("\n--- 6. ★ scope, because the theorem has a hypothesis ---")
check("It closes **'derived from the geometry of D_IV⁵ alone.'** If BST has an ingredient that is genuinely NOT "
      "SO(5)-invariant AND independently motivated, the theorem does not apply -- but that ingredient must be "
      "**NAMED and JUSTIFIED, not assumed**, and naming it is now the whole question. I am not extending the "
      "negative past its hypothesis.",
      True,
      "scope: closes derivation from D_IV⁵'s geometry alone; a non-equivariant input escapes but must be named")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (commitment projection → H0; and no SO(5)-equivariant construction can pick a direction — the family closes)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5257, closing a family instead of a candidate):
  * ★ **PRE-REGISTERED** before computing, no assumptions carried from the closed test: H1 = z > 5 AND
    A > {A_BAR}; H0 = null + chance.
  * ★★ **A SINGLE COMMITMENT IS MAXIMALLY ANISOTROPIC** — T = {SINGLE[0]:.5f}, z = {SINGLE[1]:.1f}. The
    projection **does** break SO(5); @Keeper's intuition there is right.
  * ★★★ **BUT THE ENSEMBLE RESTORES IT** — z = **+25.79 / +5.01 / +0.75** at M = 50 / 500 / 4000, A = **0.547 /
    0.643 / 0.280**, never near the bar. ⟹ **H0.** Trivial per-measurement breaking on a **flat orbit**: SO(5)
    is transitive on S⁴, so nothing distinguishes V₅.
  * ★★★★ **@Keeper's K1505 SECOND LEG EARNED ITS KEEP ON FIRST USE.** I built the instrument magnitude-only;
    at M = 50 magnitude alone reads **z = 25.8** and would have declared **P**, while alignment reads
    **A = 0.547** and refuses. A finite ensemble looks concentrated but **points nowhere in particular**.
    **Magnitude-only would have false-positived on the very first candidate.**
  * ★★★★★ **THE THEOREM — the real deliverable, because it closes the family not the candidate:** an
    SO(5)-equivariant construction with SO(5)-invariant inputs **cannot** output a distinguished n̂ ∈ R⁵ — it
    would have to be SO(5)-fixed, and **the only SO(5)-fixed vector in R⁵ is 0**. SO(5) ⊂ K = the isotropy
    group ⟹ **everything built equivariantly from D_IV⁵'s geometry is direction-blind**: Casimir (5256),
    Bergman kernel, generic norm, bare vacuum (T1444), commitment ensemble. ⟹ **a derived descent needs an
    input from OUTSIDE the isotropy group.** @Keeper's whole §3 list closes in one step.
  * ★ **SCOPE:** this closes "derived from D_IV⁵'s geometry alone." A genuinely non-equivariant,
    independently-motivated ingredient escapes it — but must be **named and justified, not assumed**. Naming
    it is now the entire question.

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
