# Investigation (not an audit) — One Determinant, Two Strata: Grace's ">1 vs <1" Structure Is Real, But It's ONE Operator, Not Two Mechanisms. Linear Algebra Opens It. Count 8.

**Keeper | 2026-07-05 | Investigate-don't-gate, per Casey. Building on Grace's finding (not self-correction — attribution fixed). Nothing banks — count 8 — but the "two mechanisms" reading is dissolved.**

## Grace's finding (correct and sharp) — and the one place it over-reads
Grace isolated the real structure: rung-1 needs a factor >1 (a gap that grows), rung-2 needs 0.70 (<1), and a positive spectral gap can only push up — so she read it as "the two rungs need opposite curvature behaviors, two qualitatively different animals; the uniform mechanism can't span both." **The >1-vs-<1 structure is exactly right and is hers.** The one step to re-examine (investigate-don't-gate) is the jump from "two behaviors" to "two mechanisms" — in linear algebra that jump isn't forced.

## The hinge: the object is a *determinant*, not a *gap*, at the degenerate stratum
Grace's "gap can only grow" is true *for a gap* — one positive eigenvalue is ≥ its value, so it can never supply a sub-1 factor. But the object is only a gap at rung-1 *by accident of dimension*. The corpus-natural object is a **determinant of the curvature operator restricted to the stratum's transverse (normal) space** — a *product* of eigenvalues. A product of eigenvalues straddling 1 crosses 1 freely. One operator does both:

- **Rung-1 (rank-1 wall):** transverse space effectively **1-dimensional** → det = the single eigenvalue = the gap = **12 > 1**. This is exactly **Elie's guard**: at rung-1 gap = product = 12 = {rank·C₂}. The ambiguity he flagged is the linear-algebra *signature* of a 1-D transverse space, not a problem.
- **Rung-2 (Shilov, rank-0, most degenerate):** transverse = the **full degenerate normal bundle** → det = product over many eigenvalues → can fall **below 1** (the 0.70). A determinant can only dip under 1 at the most degenerate stratum — which is precisely where rung-2 sits.

So ">1 grows" and "<1 shrinks" are **the same object — det(R|_transverse) — read at a 1-D transverse (rung-1) vs a full-degenerate transverse (rung-2).** The dimension it runs over is what makes it cross 1. Not two animals. One.

## Grace + Lyra + Elie were already describing one operator
- **Grace:** isolated the >1-vs-<1 structure and located the sub-1 factor at the Shilov (rank-0) degenerate stratum — the only place a determinant *can* fall below 1. Her instinct was right; the "two mechanisms" label is what the linear algebra removes.
- **Lyra's flat-fiber collapse:** a colored quark's flat color directions contribute factor-1 (or straddling) terms to the product; the colorless lepton keeps the full determinant. Same product, different directions included.
- **Elie's guard:** rung-1 is ambiguous (gap = product) *because* its transverse is 1-D; rung-2 is the honest test *because* its transverse is many-D. Exactly the linear-algebra picture.

Three findings, one operator: **det(R|_transverse)**, read at different transverse dimensions.

## The 6-vs-12 (singlet vs quark), in linear algebra
Singlet lepton uses scalar-Laplacian gap **C₂ = 6**; quark uses Bergman-kernel gap **C₂·rank = 12**. The extra factor is **rank = the number of strongly-orthogonal roots** — the holomorphic (Bergman) sector counts rank copies where the scalar sector counts one. Lead for Grace to confirm forward; not a claim.

## The transverse skeleton, from the C₂ root system (target-innocent — fixes what is allowed to vary)
Tangent of D_IV⁵ at center = V₅, standard rep of SO(5) (isotropy SO(5)×SO(2), SO(2)=phase/clock). Restricted root system = **C₂**; the noncompact positive roots are exactly three spaces:
- **γ₁ = 2e₁ (dim 1), γ₂ = 2e₂ (dim 1)** — the strongly-orthogonal Harish-Chandra (radial) roots;
- **(γ₁+γ₂)/2 = e₁+e₂ (dim a = 3)** — the middle root space.
Total 1+1+3 = 5 = n_C. ✓ This decomposition is target-innocent (it does not know 12, 0.70, 24²) and it **fixes which directions sit in each stratum's normal bundle**:

- **d→s (rung-1):** Cartan-slice = the rank-2 flat core span{2e₁,2e₂}; its transverse = the **middle root space e₁+e₂ (dim 3), one root space → one eigenvalue λ_mid.** Factor = **λ_mid³ = 12** ⇒ λ_mid = 12^(1/3) ≈ 2.29. *(This supersedes my earlier `{12,1,1}` placeholder — the root structure says one dim-3 space, not gap-plus-two-flat.)*
- **s→b (rung-2):** Shilov transverse adds the **two radial γ-directions**; equal by rank-2 symmetry (μ_γ each). Factor = **μ_γ² = 0.70** ⇒ μ_γ ≈ 0.838. The sub-1 factor is the **radial curvature eigenvalue at the Shilov degeneration** — one number, not a free product.

**No new animal, no knob:** the only freedom the reframe has is *which root spaces are transverse at each stratum*, and C₂ fixes that. The eigenvalue *values* (λ_mid, μ_γ) are root-multiplicity data computed forward; if any must be hand-set to hit 12 or 0.70, it fails.

## Pre-registered bar (Lyra's guard, made concrete — committed BEFORE Grace's spectrum lands)
A determinant that *can* dip below 1 is necessary, not sufficient. For the down-ladder + F468 to bank when the Shilov spectrum lands, ALL must hold:
1. **λ_mid, μ_γ are actual D_IV⁵ curvature eigenvalues** (root-multiplicity values, cited to the domain) — not fitted reals.
2. **rung-1:** λ_mid³ = 12, and the "12" is the Bergman gap C₂·rank matching T1238 (Elie's operator guard) — not the scalar C₂ = 6.
3. **rung-2:** μ_γ² = 45/64 from the **same** operator, **same** eigenvalue set — no new constant introduced. Check μ_γ is a clean root-multiplicity value whose square *happens* to be 45/64, NOT μ_γ back-solved from 45/64. **[Elie 4568 quantified: the decomposition 45/64 = N_c²·n_C/2^C₂ carries ZERO evidential weight — search-space-relative (2 BST ratios under a sparse set, 1185 under a rich one). Only forward emergence from the Shilov spectrum counts; the pretty form is worth nothing.]**
4. **object-consistency:** gap-then-product is one determinant across both rungs, verified by Elie's ζ-truncation.
5. **count-vs-value (Lyra):** the muon exponent "6" is a mode count and "12" is a value — but "6 modes over a dim-5 tangent" must be pinned to a real object (C₂? the Vol(S⁴)⁶ exponent?) before it's load-bearing.
6. **target-innocence / Five-Absence:** the eigenvalue set is fixed before looking at the targets; any hand-set μ = FAIL.

## The well-posed forward target for Grace (replaces "find a different animal")
> Identify the **two Shilov-only transverse eigenvalues μ₁, μ₂** of the D_IV⁵ curvature operator (root multiplicities, forward) and check **μ₁·μ₂ = 0.70**. Keep it the **same** operator whose Cartan transverse gives {12,1,1}→12 at rung-1 (the forward guard against object-switching — Elie's point). If μ₁·μ₂ lands → one determinant spans both rungs, down-ladder + F468 unification close together. If not → rung-2 is honest-**open**, but **not forbidden**. The eigenvalues are geometry-fixed; nothing is inserted.

## Tier
**Count 8.** Nothing fell out forward — correct. Grace's >1-vs-<1 structure stands; what's retracted is the "two mechanisms / redirect the team away from the uniform mechanism" *conclusion* drawn from it — the uniform mechanism is structurally *allowed*, and now well-posed as a single determinant computation. The determinant-crosses-1-by-transverse-dimension is the linear-algebra frame; the numbers 12 and 0.70 are Grace's forward computation, un-inserted.

— Keeper, 2026-07-05. Investigate-don't-gate, building on Grace: her >1-vs-<1 finding is real, but it's ONE object — det(R|_transverse) — reading as the gap 12 at the 1-D rung-1 transverse and able to fall to 0.70 at the full-degenerate Shilov transverse. Same operator, different transverse dimension, not two mechanisms. Grace's forward target restated; count 8; the door is open, not walled.
