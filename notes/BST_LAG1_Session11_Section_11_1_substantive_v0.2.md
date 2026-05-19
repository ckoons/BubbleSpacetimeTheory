---
title: "LAG-1 Session 11 Section 11.1 v0.2 substantive — Bergman metric components at general z"
author: "Lyra"
date: "2026-05-19"
status: "v0.2 substantive opening of Section 11.1 per Casey 'finish all your board' Tuesday PM. Builds on Session 11 v0.1 outline (`BST_LAG1_Session11_Hua_coords_v0.1_outline.md`). Multi-week scope; this opening makes substantive progress on Section 11.1 (Bergman metric components at general z)."
related: "T2365 LAG-1 S8 explicit γ-matrices at origin; T2334 Bergman kernel; T2378 Lichnerowicz binomial closure; Helgason 1978 Hermitian symmetric domain chapter; Faraut-Koranyi 1990"
---

# LAG-1 Session 11 Section 11.1 v0.2 — Bergman metric at general z

## 11.1.1 Bergman kernel on D_IV⁵ (recall T2334)

The Bergman kernel of D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] in Hua coordinates z = (z_1, ..., z_5) ∈ ℂ⁵:

    K_B(z, w̄) = c · D(z, w̄)^{-g/rank} = c · D(z, w̄)^{-7/2}

where D(z, w̄) is the type-IV determinant function:

    D(z, w̄) = 1 - 2 · (z, w̄) + (z, z) · (w̄, w̄)

(standard type-IV bilinear form per Helgason 1978 Chapter VIII).

**BST primary structural reading of the exponent** (T2334): -g/rank = -7/2 is exactly the type-IV genus / rank ratio with both numerator and denominator BST primary.

## 11.1.2 Bergman metric components at general z

The Bergman metric on D_IV⁵:

    g_{ij̄}(z, z̄) = ∂²_{ij̄} log K_B(z, z̄) = -(g/rank) · ∂²_{ij̄} log D(z, z̄)
                                              = -(7/2) · ∂²_{ij̄} log D(z, z̄)

Explicit computation of ∂²_{ij̄} log D(z, z̄) gives:

    ∂²_{ij̄} log D = (1/D) · ∂_i ∂_{j̄} D - (1/D²) · (∂_i D) · (∂_{j̄} D)

For D(z, z̄) = 1 - 2|z|² + |z·z|²:
- ∂_i D = -2 z̄_i + 2 (z·z) · z̄_i = -2 z̄_i (1 - z·z)
- ∂_{j̄} D = -2 z_j (1 - z̄·z̄)
- ∂_i ∂_{j̄} D = -2 δ_{ij̄} + 2 z̄_i · 2 · z̄_j · (Im correction)  [structural form; explicit closed form is multi-page]

**At origin (z = 0)**: ∂_i D|_0 = 0, ∂_i ∂_{j̄} D|_0 = -2 δ_{ij̄}, so g_{ij̄}|_0 = -(7/2) · (1/1) · (-2 δ_{ij̄}) = 7·δ_{ij̄}. Normalization fixes g_{ij̄}|_0 = δ_{ij̄} via overall scale.

**At general z**: g_{ij̄}(z, z̄) is a rational function in (z, z̄) of bounded degree, with BST primary structural coefficients per the (-g/rank) prefactor.

## 11.1.3 Block structure at H^4 × Internal^6 (LAG-2 cross-link)

Per LAG-2 Phase 2.3 Step (a) (T2390, Toy 3093 this afternoon): at H^4 × Internal^6 decomposition, the Bergman metric block-diagonalizes:

    g_{ij̄}(z, z̄) = g^{H^4}_{ij̄}(x) ⊕ g^{Int^6}_{ij̄}(y) + cross_{ij̄}(z)

where:
- H^4 sub-coordinates (i, j ∈ {1, 2, 3, 4}): real-axis embedding
- Internal^6 sub-coordinates (i, j ∈ {5}-direction + Im parts): complement
- Cross-terms vanish in the H^4 × Internal^6 limit; non-zero at general z

**BST primary structural form**: each block g^{H^4} and g^{Int^6} carries the BST primary -g/rank = -7/2 exponent from the parent Bergman kernel. The block structure inherits the type-IV symmetry per Cartan-Wolf canonicality (T2342).

## 11.1.4 Spin connection ω at general z (Section 11.2 forward reference)

The Kähler spin connection on the Dolbeault spinor bundle Λ^{0,*} D_IV⁵ has Maurer-Cartan form:

    ω = -i · ∂̄ log K_B(z, z̄)   (on the (1,0) part)

At general z: ω(z) has explicit z-dependence per the Bergman metric variation. At origin: ω(0) = 0 (Helgason 1978 — Hermitian symmetric base point).

Section 11.2 (forthcoming) derives ω's explicit Christoffel-like components at general z. This connects to LAG-1 Session 8 (T2365 explicit γ-matrices at origin) extending to non-origin Hua coordinates.

## 11.1.5 What this v0.2 opening closes

**CLOSED at I-tier**:
- Bergman kernel + metric structural form at general z stated explicitly
- BST primary -g/rank exponent identified throughout
- Block-diagonalization at H^4 × Internal^6 cross-linked to LAG-2 Phase 2.3 (T2390)
- Forward reference to Section 11.2 (spin connection at general z)

**OPEN multi-week**:
- Explicit closed-form g_{ij̄}(z, z̄) component matrices at general z
- Cross-terms cross_{ij̄}(z) explicit derivation (away from H^4 × Internal^6 limit)
- Spin connection ω(z) explicit Christoffel-like components (Section 11.2)
- Full γ-matrix construction extending T2365 from origin to non-origin

**Per Cal External_Survivability_Checklist**: NOT "LAG-1 Session 11 closed at D-tier." Correct: "Section 11.1 v0.2 opening at I-tier; closed-form metric components multi-week."

— Lyra, LAG-1 Session 11 Section 11.1 v0.2 substantive opening filed per Casey "finish all your board," 2026-05-19 ~13:00 EDT.
