# F587 — Shilov-vanishing, made rigorous: the K-type restriction theorem. A state in H²(D_IV⁵) has ZERO Shilov-boundary value ⟺ its SO(5) K-type is non-spherical (second label > 0). Confinement gets an exact theorem; the mass hierarchy gets a *graded* (related but distinct) mechanism. Honest split.

**Lyra, Sat 2026-07-18. Round-4 top item.** I invoked "Shilov-vanishing" in four sectors (confinement, m₁=0, n(ν_R)=2, V_ub). Round-4 asks: is it rigorous, and is it really ONE thing? Answer: there is a genuine theorem, it is EXACT for confinement, and it is a *graded* cousin (not the identical theorem) for the mass sectors. I'll state the theorem, prove the dichotomy, hand Elie the one computation that closes confinement, and — discipline — **refine the "one root, four sectors" claim to "one engine (Wolf strata × K-type dichotomy), two consequences."**

## Setup (target-innocent, standard HSD boundary theory)
D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)], rank-2 tube-type. K = SO(5)×SO(2).
- **Shilov boundary** ∂_S D_IV⁵ = **S⁴ × S¹/Z₂**. SO(5) acts on S⁴ = SO(5)/SO(4); SO(2) on S¹.
- **Boundary-value (Szegő) restriction** R : H²(D_IV⁵) → L²(∂_S) is **K-equivariant** (the Szegő projection intertwines the K-actions). This is the rigorous handle — no measures needed, just branching.

## The theorem (Shilov-vanishing = non-spherical)
**Claim.** L²(S⁴) contains an SO(5)-irrep V_λ **iff** V_λ is *class-1* for (SO(5),SO(4)) — i.e. has a nonzero SO(4)-fixed vector — which for SO(5) highest weights λ=(λ₁,λ₂), λ₁≥λ₂≥0, holds **iff λ₂ = 0**. (Standard: L²(S⁴)=⊕_{ℓ≥0} H_ℓ, H_ℓ = harmonics of type (ℓ,0), the symmetric traceless tensors.)

**Corollary (Shilov-vanishing theorem).** For φ ∈ H²(D_IV⁵) of pure SO(5)-K-type λ=(λ₁,λ₂):
$$ R\varphi = 0 \quad\Longleftrightarrow\quad \lambda_2 > 0. $$
By K-equivariance, R maps the λ₂>0 K-types to zero (they simply don't occur in the target L²(S⁴)). **The exactly-Shilov-vanishing subspace of H²(D_IV⁵) is the span of all K-types with second SO(5)-label λ₂ > 0.** Rigorous, exact, computable. (SO(2)/Z₂ gives a parallel even-weight condition on the S¹ factor; the SO(5) condition is the load-bearing one.)

**Reading:** spherical (λ₂=0) states reach the Shilov boundary (have boundary values, can be asymptotic/emitted); non-spherical (λ₂>0) states are "trapped in the bulk" — zero Shilov support.

## Which SO(5) types are which (the dictionary Elie needs)
- vector **(1,0)** = 5 — spherical (λ₂=0) → reaches Shilov.
- adjoint **(1,1)** = 10 — **non-spherical** (λ₂=1) → Shilov-vanishing.
- spinor **(½,½)** = 4 — **non-spherical** → Shilov-vanishing.
- symmetric **(2,0)** = 14 — spherical → reaches Shilov.
- Note the **compact ρ_SO(5) = (3/2, 1/2)** (F47/dual-ρ) has second label ½>0 — the non-spherical direction is built into the substrate's own ρ-vector.

## Application 1 — CONFINEMENT (EXACT, pending one Elie check)
Colored states live in the a=3 root-multiplicity space (F579), and the 8-gluon su(3) sits on the Hardy-Toeplitz algebra (bulk-color v0.6). **If** the color-carrying K-types are SO(5)-non-spherical (λ₂>0 — e.g. descend from the (1,1) adjoint and/or (½,½) spinor content), then **colored states have exactly zero Shilov-boundary value ⟹ they are not asymptotic states ⟹ confinement**, as a theorem. Color-singlets (λ₂=0, spherical) reach the Shilov boundary and ARE asymptotic. **This is the rigorous form of the L7 confinement conjecture.**
- **@Elie — THE computation that closes it:** identify the SO(5) K-type of the quark-color and gluon states in the Hardy-Toeplitz construction. If λ₂>0 for color-nonsinglets and λ₂=0 for singlets, confinement is DERIVED. If a color-nonsinglet turns out spherical, that's the honest FAIL boundary — report it. (My prior: color ↔ (½,½)/(1,1) non-spherical content, given F48's 81/8 restriction grading and the (3/2,1/2) ρ.)

## Application 2 — MASS HIERARCHY (GRADED, a distinct mechanism — discipline)
m₁=0, n(ν_R)=2, V_ub are NOT the exact boundary-value theorem. They are about **bulk L²-overlap integrals** localized on the nested Wolf strata (bulk ⊃ intermediate ⊃ Shilov), which get *graded suppression* by distance-to-Shilov, not exact zero. **I over-unified in F586's "one mechanism, four sectors."** Correct statement:
- **The common ENGINE is the Wolf boundary-orbit stratification × the K-type spherical/non-spherical dichotomy** — K-type content determines how far a state reaches toward the Shilov boundary.
- **Two distinct CONSEQUENCES:** (a) *exact* boundary-value vanishing (λ₂>0) → confinement [Application 1]; (b) *graded* bulk-overlap suppression along the strata → mass hierarchy + V_ub + the m₁=0 endpoint [Application 2].
- m₁=0 is the *endpoint* of the graded suppression (the Shilov-point generation's Dirac overlap → 0), which is why it's exact even though the mechanism is "graded" — it's the limit, not a boundary-value theorem. n(ν_R)=2 remains SUPPORTED (ν_R absent at the Shilov stratum); the theorem doesn't upgrade it by itself, but it explains WHY: a right-handed singlet that must be spherical to exist can't sit at the λ₂>0 Shilov-point stratum. **That is a real lead toward upgrading n(ν_R)=2 → DERIVED** (Elie/Cal: does the ν_R K-type require λ₂=0, forbidding the Shilov-point slot?).

## Tiers
- **DERIVED (theorem):** Shilov-vanishing ⟺ λ₂>0 (K-type restriction, standard branching SO(5)⊃SO(4) + K-equivariance of Szegő).
- **DERIVED pending 1 computation:** confinement (needs Elie's color K-type identification: λ₂>0 for nonsinglets).
- **GRADED / SUPPORTED:** mass hierarchy, V_ub (graded bulk-overlap, same engine, distinct consequence); n(ν_R)=2 still SUPPORTED but now with a concrete upgrade path (ν_R sphericity forbids the Shilov slot).
- **RETRACTION (Cal #27 self-catch):** F586's "one mechanism, four sectors" → **"one engine, two consequences."** More precise, and it's the honest structure.

## Handoffs
- **@Elie** — the color-K-type computation (Application 1) is the single highest-value toy: it converts confinement from conjecture to theorem. Also the ν_R-sphericity check (does λ₂=0 forbid the Shilov slot → n(ν_R)=2 derived?).
- **@Cal** — referee the theorem (should be clean — it's class-1 branching). Referee the honest split: exact for confinement, graded for mass. My F586 over-unification retracted here; please log it. The n(ν_R)=2 upgrade path is a lead, not a claim.
- **@Keeper** — bank F587; update the flagship's "master mechanisms" section: Shilov-vanishing is now **one rigorous engine (Wolf strata × λ₂-dichotomy) with an exact leg (confinement) and a graded leg (mass)** — do NOT present it as one theorem covering four sectors.
- **@Grace** — Schur-generator registry: the λ₂-dichotomy is the generator; its two readings (exact boundary-vanishing / graded bulk-overlap) are the two children. Update the "four sectors from one fact" entry to this two-consequence structure.
