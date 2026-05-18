---
title: "LAG-1 Scoping: Explicit Bergman Dirac Operator γ_B^μ on D_IV⁵"
author: "Lyra"
date: "2026-05-17"
status: "SCOPING — Casey-approved per Keeper-filed task; ~1-2 weeks multi-session"
target: "Multi-session work; explicit γ_B^μ + Dirac spectrum + mass-gap verification"
herve_response: "Closes part of Herve Carruzzo's 'explicit operator forms' critique"
---

# LAG-1: Explicit Bergman Dirac Operator on D_IV⁵

## What this is

Construct the explicit Dirac operator γ_B^μ ∂_μ on D_IV⁵ in Hua coordinates, compute its low-K-type spectrum, and verify the BST mass-gap structure (m_p = 6π^{n_C} m_e per T1316) emerges from the spectral eigenvalues.

## What this closes

- **Herve Carruzzo critique part 1**: "BST has the action principle but lacks explicit operator forms." The Bergman Dirac is the canonical fermionic operator that pairs with the six-term Lagrangian S_BST.
- **Existing BST work strengthened**: T1316 mass gap (6π^{n_C} factor), the Wallach K-type spectrum (T1830 + my T2334 Bergman kernel), Möbius cohomology (Sessions 1-3, T2328+T2329+T2335).
- **Foundation for LAG-2**: dimensional reduction needs the fermionic action; Dirac operator is the first piece.

## Classical theorem inventory needed

### 1A — Bergman kernel as starting point (DONE, T2334)

My T2334 (Sunday afternoon) gave the explicit Bergman kernel
```
K_B(z, w̄) = c · D(z, w̄)^{-g/rank}
```
on D_IV⁵ in Hua coordinates. The Dirac operator follows from K_B via the standard reproducing-kernel construction.

### 1B — Dirac operator on bounded symmetric domains (Helgason 1962 / Wong 1995)

Citation: Wong, P.-M.W. "The Dirac operator on bounded symmetric domains," Compositio Math 95 (1995); Helgason, "Differential Geometry, Lie Groups, and Symmetric Spaces," Chapter II.

What we use: explicit construction of γ^μ matrices for type IV domain, plus the Bergman-metric Dirac D_B = γ^μ ∂_μ + Γ-terms (spin connection).

Gap to bridge: most literature is for type I (Grassmannian) or type III (antisymmetric); type IV has been worked but is less standard. The D_IV⁵ specific computation may need to be assembled from general formulas.

### 1C — Hua's integral formula (Hua 1963)

Citation: Hua, L.K. "Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains," Translations Math. Monographs 6.

What we use: the explicit reproducing kernels for type IV, the orthogonality of holomorphic polynomials on D_IV⁵, the inner product 〈f, g〉 = ∫_{D_IV⁵} f g̅ K_B^{-1} dV.

### 1D — Lichnerowicz formula (Lichnerowicz 1963)

D^2 = ∇*∇ + R/4 where R is scalar curvature. For D_IV⁵, R is a BST integer multiple of the Bergman metric trace.

Verification target: D_B^2 - ∇*∇ should equal (R/4) · I, where R is a known BST integer combination. Toy-verifiable.

## Multi-session breakdown (8 sessions, ~12-16 hours total)

| Session | Deliverable | Effort |
|---------|------------|--------|
| 1 (TODAY) | Skeleton + Hua-coord candidate γ_B^μ + Lichnerowicz first check | ~1 h |
| 2 | Full γ^μ matrix construction for D_IV⁵ (4×4 Dirac on real-10 manifold) | ~2 h |
| 3 | Spin connection Γ from Bergman metric | ~2 h |
| 4 | Spectral decomposition: Dirac eigenvalues on Wallach K-types | ~2-3 h |
| 5 | Mass-gap verification: lowest eigenvalue × dimensional factor = m_p/m_e ratio | ~2 h |
| 6 | Lichnerowicz formula explicit: D² = ∇*∇ + R/4 with R as BST integer | ~1-2 h |
| 7 | Connection to fermionic action S_fermion in Lagrangian S_BST | ~1-2 h |
| 8 | Paper draft v0.1 — "The Bergman Dirac Operator on D_IV⁵" | ~3 h |

Decision points after Sessions 2, 4, 6.

## What today (Session 1) closes

- Skeleton + framework set up
- Candidate γ_B^μ matrices identified (4×4, real-10 setup)
- First Lichnerowicz check: dim consistency of D² vs ∇*∇ + R/4
- Toy verifying the structural setup (not full computation)

Tomorrow continues with Sessions 2-3 (full matrix construction + spin connection).

## Promotion targets

Sessions 1-8 close LAG-1 to D-tier. Specific theorem promotions:
- T1316 (mass gap 6π^{n_C}) — currently D-tier; LAG-1 gives it a Dirac-spectral derivation (D-tier strengthened)
- T2334 (Bergman kernel) — currently D-tier; LAG-1 extends to the Dirac on the same kernel structure
- T2335 (Möbius S3) — currently D-tier; the Dirac on M(D_IV⁵) connects to lepton mass formulas

## Connection to LAG-2

LAG-1 provides the fermionic Dirac operator. LAG-2 dimensional reduction needs:
- The Dirac action ∫ ψ̄ D_B ψ as one of the six S_BST terms
- The 4+6 split applied to spinor representations
- Verification that 4D Dirac emerges from the 10D D_IV⁵ Dirac under reduction

So LAG-1 must close before LAG-2 Phase 3 (extending reduction to all six terms).

— Lyra, 2026-05-17 ~15:40 EDT
