---
title: "Backlog: Linearization of Heat Kernel Coefficients on Symmetric Spaces"
author: "Casey Koons & Lyra (Claude Opus 4.6)"
date: "March 17, 2026"
status: "Partially verified — structural proof complete, explicit eigenvalue construction remains"
target: "Algebraic Complexity paper (Section 3); WorkingPaper addendum"
---

# Backlog: Linearization of Heat Kernel Coefficients

## The Insight

The Seeley-DeWitt coefficients a_k on symmetric spaces are computed today as quartic (or higher) curvature tensor contractions — Gilkey formulas involving index gymnastics over Rm⊗Rm⊗...⊗Rm. This is method noise. The objects themselves are eigenvalues.

## The Program

1. **Lift**: The curvature tensor Rm is a fixed element of Λ²𝔭 ⊗ Λ²𝔭 on a symmetric space (∇R = 0). The quartic invariants live in Sym⁴(Rm), which is a vector space. In that space, each Gilkey invariant is a **projection** — a linear map, not a polynomial.

2. **Diagonalize**: On G/K, the curvature is determined by the Lie bracket [·,·]: 𝔭×𝔭 → 𝔨. The invariant quartic contractions decompose under K into irreducible representations. Each a_k is a sum over these irreducibles with known multiplicities. This is an eigenvalue problem on the root system.

3. **Project**: The root multiplicities (m_s, m_l, m_{2s}) = (n−2, 1, 1) for Q^n parameterize everything. Express a_k as a linear form on the monomial basis of root multiplicities. The degree-8 polynomial in n is the shadow of this linear structure in a particular coordinate system.

## What Changes

- **Old method**: Compute Rm explicitly (10×10×10×10 tensor for Q⁵), contract four copies, sum ~100 quartic invariants, get a rational number. 23+ minutes.
- **New method**: Write the eigenvalue equation on the root system, diagonalize a finite matrix, read off a_k as eigenvalues. One step.

## Why It Works on Symmetric Spaces

- ∇R = 0 → curvature is a fixed vector, not a field
- Harish-Chandra isomorphism linearizes the invariant differential operators onto the Cartan subalgebra
- Everything is determined by finite root data — no integration, no limits, no approximation

## Why It Matters for BST

The complexity of the Gilkey formula obscures a simple truth: a₄(Q⁵) ≈ 147 because the quartic curvature eigenvalue of Q⁵ nearly equals the dimension of 𝔰𝔬(7) ⊗ V₁. In the linear formulation, this is a near-coincidence of two eigenvalues in the same space — visible at a glance, not after pages of tensor calculus.

More broadly: BST claims the Standard Model is linear in the right basis. The Gilkey linearization is a concrete example. The "right basis" is the root system. The complexity was in the method, not the physics.

## For the Algebraic Complexity Paper

Core example for Section 3 ("Method Noise"):

> The same object — the fourth heat kernel coefficient of Q⁵ — is a quartic tensor contraction in one basis and a single eigenvalue in another. The complexity was never in the physics. It was in the projection.

One-line thesis: *Lift, diagonalize, project. The rest is bookkeeping.*

## For the Working Paper

Add to the Seeley-DeWitt section (§8.2 or new subsection): the linearization reformulation, noting that a_k on symmetric spaces should be computable as eigenvalues of operators on the root system, bypassing explicit tensor construction. Reference the rank-1 case (where this is essentially known) and note that rank-2 (our case) is the natural frontier.

## Progress (Toys 248–250, March 17, 2026)

### What's been verified

1. **Linear framework confirmed** (Toy 249–250): Lyra's insight that a_k = ⟨w_k|d⟩ — heat kernel coefficient as inner product of multiplicity polynomial |d⟩ and heat kernel weights ⟨w_k| — is structurally correct. Toy 250 (Elie, fixed from Lyra's Toy 249) scores 5/5.

2. **Multiplicity polynomial extracted** (Toy 250): d(p,q) for Q⁵ expressed as a degree-12 polynomial in (p,q) with 38 monomials, all rational coefficients verified to 10⁻⁹. This IS the "right basis" — the group theory data separated cleanly from the heat kernel weights.

3. **Spectral completeness** (Toy 254 correction): On Q^n (rank 2), ALL (p,q) reps with p ≥ q ≥ 0 are spherical — Helgason's theorem for rank-r symmetric spaces. The full (p,q) sum IS the heat trace; there are no non-spherical corrections. (An earlier claim from Toy 250 was incorrect.) This means a₄(n) values from Toy 248 for ALL n are correct as computed — no decontamination needed.

4. **a₄(Q⁵) = 2671/18 confirmed** (Toy 248): Exact rational identification from numerical heat trace, independently of Gilkey tensor contractions. No free parameters, no fitting.

5. **Cross-family uniqueness**: a₄(Q^n)/N_c g² crosses 1 only at n=5 (verified n=3..10). The "near-coincidence" described in the BST section above is now quantified: 2671/18 = 147 + 25/18.

### What remains

- The explicit eigenvalue construction on the root system — expressing a₄ as a single eigenvalue of an operator on C₂ root data — is not yet done
- The degree-8 polynomial a₄(n) as a closed rational function: Lagrange interpolation from Toy 248 values (n=3..8+) is the preferred route. All values are correct as computed (no decontamination needed — Toy 254 correction).
- The Harish-Chandra route (step 2 of The Program) awaits explicit computation
- **a₅(Q⁵) ≈ 221.641 ± 0.004** (Toys 254-255): candidates 14185/64 (den=2^{C₂}), 5541/25 (den=n_C²), 7979/36 (den=C₂²). Needs precision push.

## Status

- Partially verified — the linear structure is confirmed (Toy 250), spectral completeness established (Toy 254), but the explicit eigenvalue construction on the root system remains open
- Simpler than a conjecture: it's a reformulation, not a claim about new mathematics
- Next step: a₄(n) closed form via Lagrange interpolation from Toy 248 values; a₅ precision push
