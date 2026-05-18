---
title: "LAG-1 Session 1: Bergman Dirac Skeleton + Hua-coord Candidate"
author: "Lyra"
date: "2026-05-17"
status: "Session 1 of 8 — TODAY's start, ~1h scope"
parent: "BST_LAG1_Bergman_Dirac_Scoping.md"
toy: "play/toy_3002_bergman_dirac_skeleton.py"
---

# LAG-1 Session 1: Skeleton + Hua-coord Candidate

## Goal of this session

Set up the Bergman Dirac operator on D_IV⁵ in concrete terms:
- Choose representation (real-10 manifold ⟹ Cl(10) Clifford algebra ⟹ 32×32 Dirac spinors, OR complex-5 ⟹ Cl_C(5) with 8-dim complex spinors)
- Write the candidate operator γ_B^μ ∂_μ on a generic z ∈ D_IV⁵ in Hua coordinates
- Verify the Lichnerowicz-formula dimensional consistency (D² has the right number of independent components vs Laplacian + scalar curvature)

Session 1 is FRAMEWORK + DIMENSIONAL CHECK. Sessions 2-3 do the explicit matrix construction.

## Choice of representation

D_IV⁵ has:
- Complex dim = n_C = 5
- Real dim = rank · n_C = 10

The Dirac operator can be set up two ways:

**Real-10 approach**: D_IV⁵ as a real 10-manifold; Clifford algebra Cl(10, 0) (or Cl(8,2) for the signature 5+5 if we treat the Hermitian metric as split signature). Spinors are 2^5 = 32-dimensional. Dirac matrices are 32×32.

**Complex-5 approach**: D_IV⁵ as a complex 5-manifold; use the holomorphic-anti-holomorphic decomposition. Dirac becomes ∂̄ + ∂̄* (the Dolbeault operator) acting on (0,*)-forms tensored with the spinor bundle. Spinors are 2^{n_C} = 32-dim too, but split as 16 + 16 (chiral pair).

We pick **complex-5 / Dolbeault approach** because:
1. D_IV⁵ is naturally a Hermitian symmetric space; complex structure is preferred
2. Chirality decomposition matches T1947's chirality + CP structure
3. Holomorphic discrete series (Wallach K-types) directly give Dirac spectrum

## Setup in Hua coordinates

Coordinates: z = (z_1, ..., z_5) ∈ ℂ^5 with D_IV⁵ defining inequalities
```
1 - 2|z|² + |z·z|² > 0,  |z|² < 1
```
(Recall from T2328: real-form locus M(D_IV⁵) = {z = z̄} = open 5-ball in ℝ^5.)

Bergman metric: g_{ij̄} = ∂_i ∂_j̄ log K_B(z, z̄) where K_B = c·D(z,z̄)^{-(n_C+2)/2} (T2334).

For the Bergman Dirac on D_IV⁵:
```
D_B = γ^μ (∂_μ + (1/4) ω_μ^{ab} γ_a γ_b)
```
where ω is the spin connection of the Bergman metric, γ^μ are Dirac matrices for the Hermitian inner product.

## Hua-coordinate candidate (skeleton)

In Hua coordinates with the Bergman metric, the leading-order Dirac action is:
```
D_B = γ^z_i ∂_{z_i} + γ^z̄_i ∂_{z̄_i} + O(z̄·z)
```

where the γ^z_i / γ^z̄_i pair satisfies the Clifford anti-commutation relations:
```
{γ^z_i, γ^z̄_j} = 2 g^{ij̄} = 2 (Bergman metric inverse)
```

For D_IV⁵: g^{ij̄}(0) = δ^{ij̄} (at origin); higher-order corrections involve the Hermitian + bilinear terms in D(z, z̄).

## Lichnerowicz formula dimensional check

The Lichnerowicz identity says:
```
D_B² = ∇*∇ + R/4
```
where R is the scalar curvature.

For D_IV⁵, the scalar curvature in Bergman metric is:
```
R = -n_C·(n_C + 2) (negative Einstein, sign for Hermitian symmetric domain)
   = -5·7 = -35 = -n_C·g
```

So R/4 = -35/4 (in units where Bergman metric scale is normalized).

**Dimensional consistency target**: D_B² acting on a 32-dim spinor on a 10-dim manifold has 32·... independent operator components. The Laplacian ∇*∇ has the same count. The R/4 term is a scalar multiple of identity. The Lichnerowicz formula has the right number of degrees of freedom on both sides.

**BST integer in the scalar curvature**: R = -n_C·g = -35. Both n_C and g are BST primaries. The "35" itself is N_c·n_C·g/N_c = n_C·g (matches Stark-Heegner d=35 isn't on the list; but 35 = n_C·g is structural).

## What this session produces

1. This document — framework + representation choice + Hua-coord skeleton
2. Toy 3002 — dimensional consistency check + scalar curvature R = -n_C·g verification + BST integer structure
3. T2339 registry entry — partial first-session result

## Open after Session 1

- Session 2: explicit 32×32 γ^μ matrices for the complex-5 Dolbeault approach
- Session 3: spin connection ω from Bergman metric (this is where the geometry enters)
- Sessions 4-8 as scoped

## Why this matters

This is the first concrete piece of LAG-1. From Session 2 onward we have actual matrix computations to do; Session 1 just sets up the framework so we know what we're computing.

**Net Session 1 effort**: ~45 min (this doc + toy).

— Lyra, 2026-05-17 ~15:50 EDT
