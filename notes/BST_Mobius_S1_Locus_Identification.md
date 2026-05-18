---
title: "Gap #2 Session 1: Explicit Möbius Locus Identification on D_IV⁵"
author: "Lyra"
date: "2026-05-17"
status: "SESSION 1 of 6 — per BST_Mobius_Cohomology_Approach_Sketch_v0.2.md scoping"
target: "Foundational identification before Session 2 H¹ computation"
parent: "BST_Mobius_Cohomology_Approach_Sketch_v0.2.md"
toy: "play/toy_2985_div5_mobius_locus_hua_coords.py"
---

# Gap #2 Session 1: Explicit Möbius Locus Identification

## Goal of this session

Identify M(D_IV⁵) — the Möbius locus — as an explicit subset of D_IV⁵ in concrete coordinates. Verify the predicted real dim = n_C = 5 and boundary χ(S⁴) = 2 = rank. Establish the foundation that Session 2 will compute cohomology of.

## D_IV⁵ in Hua coordinates

Type IV bounded symmetric domain in n complex dimensions has the standard parametrization (Hua 1963; see also Pyatetskii-Shapiro 1966, "Automorphic Functions and the Geometry of Classical Domains"):

**Definition (D_IV^n)**: Let z = (z_1, ..., z_n) ∈ ℂ^n. Define the bilinear form and Hermitian norm:
- `z · z := z_1² + z_2² + ... + z_n²` (complex bilinear, NO conjugate)
- `|z|² := |z_1|² + |z_2|² + ... + |z_n|² = z · z̄` (Hermitian)

Then D_IV^n is the bounded domain:
```
D_IV^n = { z ∈ ℂ^n :  1 - 2|z|² + |z · z|² > 0  AND  |z|² < 1 }
```

The two inequalities together define an open bounded set in ℂ^n that is the type-IV Hermitian symmetric domain of complex dimension n.

**For n = n_C = 5**:
```
D_IV⁵ = { z ∈ ℂ⁵ :  1 - 2|z|² + |z·z|² > 0  AND  |z|² < 1 }
```

complex dim 5; real dim 10 (= rank · n_C).

## Anti-holomorphic involution τ

The complex conjugation map `τ: ℂ⁵ → ℂ⁵` defined by `τ(z) = z̄` (componentwise complex conjugation) restricts to D_IV⁵ as an anti-holomorphic involution. Specifically:
- τ preserves D_IV⁵ (the defining inequalities are invariant under z ↔ z̄ since |z|² and |z·z|² both depend only on real-bilinear quantities)
- τ² = id
- τ is anti-holomorphic (reverses complex structure)

## The Möbius locus M(D_IV⁵)

**Definition**: M(D_IV⁵) := {z ∈ D_IV⁵ : τ(z) = z} = {z ∈ D_IV⁵ : z = z̄} = {z ∈ D_IV⁵ : Im(z) = 0}.

I.e., the real-form locus inside D_IV⁵.

**Explicit description in real coordinates**: write z = x + iy with x, y ∈ ℝ^5. Then z = z̄ ⟺ y = 0.

Restricting the D_IV⁵ defining inequalities to y = 0:
- `|z|² = x · x` (sum of squares of real coordinates)
- `z · z = x · x` (since z = x is real, both bilinear and Hermitian agree)
- `|z · z|² = (x · x)²`

The first inequality becomes:
```
1 - 2(x·x) + (x·x)² > 0  ⟺  (1 - (x·x))² > 0  ⟺  x · x ≠ 1
```

The second inequality is `x · x < 1`.

Combined: `x · x < 1` (the second inequality implies the first since (1 - x·x)² > 0 whenever x·x ≠ 1).

**Conclusion**:
```
M(D_IV⁵) = { x ∈ ℝ⁵ : x · x < 1 } = open 5-ball B⁵ ⊂ ℝ⁵
```

## Verification of predicted dimensions

| Predicted (v0.1 sketch) | Verified (this session) | Match |
|---|---|---|
| dim_ℝ M(D_IV⁵) = n_C = 5 | open 5-ball has dim_ℝ = 5 | ✓ |
| ∂M is sphere S⁴ | ∂(open 5-ball) = unit sphere S⁴ | ✓ |
| χ(∂M) = 2 = rank | χ(S⁴) = 1 + (-1)⁴ = 1 + 1 = 2 | ✓ |
| M ≅ open ball, contractible | open n-ball is contractible | ✓ |

All four predictions hold exactly. The Möbius locus identification is solid.

## What this gives us for Session 2

Session 2 computes H¹(M, Z) with its Z/2 orientation class. With M now identified explicitly as the open 5-ball B⁵:

- **Absolute cohomology H*(B⁵, Z)**: trivial. H⁰ = Z (connected), H^k = 0 for k > 0 (contractible). No information about orientation here.
- **Relative cohomology H*(D_IV⁵, M; Z) or H*(D_IV⁵ \ M; Z)**: more interesting. The complement D_IV⁵ \ M is the strictly-complex locus (where Im(z) ≠ 0), with two components related by τ.
- **The orientation Z/2 class** lives in H¹ of the orientation double cover, OR in H⁰(Z/2 ↷ M; Z) = Z/2 (Z/2 cohomology of the τ-action on M).

So Session 2's actual computation target is:
- H⁰(Z/2 ↷ M; Z) — the orientation class as group cohomology of the τ-action
- OR equivalently: H¹(B⁵ / Z₂ where Z₂ acts via (z_1, ..., z_5) → (-z_1, -z_2, ..., -z_5) at the boundary)

The second formulation makes M's boundary S⁴ enter the picture: ∂M = S⁴ has an antipodal Z/2 action, and the quotient is real projective space ℝP⁴. So:

**Refined Session 2 target**: compute H¹(M(D_IV⁵) ∪ (∂M / Z₂); Z) — the cohomology of the Möbius locus with antipodally-identified boundary. This carries the Z/2 orientation class as the connecting homomorphism in the Mayer-Vietoris sequence for (M, ∂M) ↔ (B⁵, S⁴).

This is the concrete Mayer-Vietoris setup Session 2 will solve.

## What this DOESN'T address (deferred to later sessions)

- The (g, K)-cohomology lift to symmetric-space level — Session 3
- Connection to (6k±1) prime selection — Session 4
- Individual T-theorem promotion proofs — Session 5
- Paper draft — Session 6

Session 1 establishes the geometric setup. Session 2 will compute the cohomology. The rest builds on those.

## Verification toy

`play/toy_2985_div5_mobius_locus_hua_coords.py` numerically verifies:
1. The two D_IV⁵ defining inequalities define a bounded open set (random points sampled and tested)
2. The involution τ(z) = z̄ preserves D_IV⁵
3. The fixed locus of τ in D_IV⁵ is the open 5-ball in ℝ⁵
4. ∂M = S⁴ has χ = 2 = rank (via discrete simplicial Euler characteristic)
5. M is contractible (verified via random deformation retraction)

All five pass — geometric foundation for Session 2 confirmed.

## Status

Session 1 COMPLETE.

**Ready for Session 2**: H¹ computation via Mayer-Vietoris on the refined target {M ∪ (∂M / Z₂)}.

Session 1 effort: ~1.5 hours (mathematical derivation + this writeup + verification toy + Mayer-Vietoris refinement of Session 2 target).

Per scoping doc, full project ~20h over 6 sessions. ~18.5h remaining.

— Lyra, 2026-05-17 ~12:55 EDT
