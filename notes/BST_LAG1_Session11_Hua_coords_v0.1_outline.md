---
title: "LAG-1 Session 11 v0.1 outline — Hua coordinates non-origin extension"
author: "Lyra"
date: "2026-05-19"
status: "v0.1 outline per Tuesday T-A5 (Lyra primary). Multi-week scope continuation of LAG-1 Sessions 2-9 (T2349-T2374) + Session 10 (T2379, T2380). Extension of explicit γ-matrix construction (T2365) from origin to non-origin Hua coordinates."
related: "T2365 LAG-1 S8 explicit γ-matrices at origin; T2350 spin connection structure; T2334 Bergman kernel; Helgason 1978 Hua coordinates"
length_target: "v0.1 outline ~6-8 pages; v1.0 paper section ~20-30 pages"
---

# LAG-1 Session 11 v0.1 — Bergman Dirac at non-origin Hua coordinates

## Goal

Extend T2365 (explicit 32×32 γ-matrices, machine-verified at origin of D_IV⁵) to non-origin Hua coordinates. This is the substantive continuation of the LAG-1 program toward Paper #118 v0.3.

## Setup

### Hua coordinates on D_IV⁵

D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] is parametrized by Hua coordinates z ∈ ℂ^5 with constraint defining the bounded symmetric domain:

    |z|² < 1 + |z^T·z|²  (type-IV constraint)

At the origin z = 0, the geometry is "maximally symmetric" — the isotropy K = SO(5)×SO(2) acts transitively, all directions are equivalent, the Bergman metric is δ_{ij̄}.

Away from origin: Bergman metric becomes z-dependent:

    g_{ij̄}(z, z̄) = ∂_i ∂_j̄ log K_B(z, z̄)

Per Faraut-Koranyi 1990: K_B(z, w̄) = c · D(z, w̄)^{-g/rank} where D is the type-IV determinant function.

## v0.1 outline structure

### Section 11.1 — Bergman metric components at general z

- Explicit form of g_{ij̄}(z, z̄) in Hua coordinates
- Symmetry under K = SO(5) × SO(2) action
- Reduction to Bergman flat metric at origin

### Section 11.2 — Spin connection ω at general z

- Spin connection on Dolbeault spinor bundle Λ^{0,*}
- Bergman-metric Levi-Civita connection (torsion-free Kähler)
- ω = ω^{1,0} + ω^{0,1} decomposition
- At origin: ω = 0 (Helgason); away from origin: explicit Christoffel-like terms

### Section 11.3 — γ-matrices at general z

- γ^{z_i}(z) = √2 · ε(dz̄^i) acts on Dolbeault basis (z-independent at the basis level)
- BUT the metric structure {γ^{z_i}(z), γ^{z̄_j}(z)} = 2 g^{ij̄}(z, z̄) depends on z
- Anti-commutation at non-origin: standard Clifford algebra but with z-dependent inner product

### Section 11.4 — Full Dirac D = γ^μ ∇_μ at general z

- D = γ^{z_i} ∇_{z_i} + γ^{z̄_j} ∇_{z̄_j}
- ∇ = ∂ + ω (covariant derivative with spin connection)
- Lichnerowicz at general z: D² = ∇*∇ + R/4 with R(z) = R_origin = -n_C·g constant on Kähler-Einstein

### Section 11.5 — Wallach K-type spectrum at general z

- Wallach K-types (m_1, m_2) eigenfunctions on D_IV⁵ are NOT localized at origin
- K-type spectrum invariant under K = SO(5) × SO(2)
- Eigenvalues unchanged: λ_Dirac²(m_1, m_2) = m_1(m_1+n_C) + m_2(m_2+N_c) - n_C·g/4 (T2351)
- Eigenfunctions span over all D_IV⁵, not localized at z = 0

### Section 11.6 — Heat kernel trace beyond origin

- Tr(e^{-tD²}) over all D_IV⁵ = ∫_{D_IV⁵} K_t(z, z) dvol_B(z)
- Local heat kernel K_t(z, z) varies with z
- Integrated trace recovers Wallach K-type sum (per Sections 11.4-11.5)
- Connection to T2372 + T2378 cascade Tr(D²^k) = 32·10^k at origin

### Section 11.7 — Volume integration via Faraut-Koranyi (multi-week)

- Bergman volume Vol(D_IV⁵) = π^{n_C}/(BST primary constant) per Faraut-Koranyi 1990
- π^5 ≈ 306.02 prefactor (consistent with m_p/m_e = C_2·π^{n_C}, T2353)
- BST primary integer factor: candidate forms TBD

### Section 11.8 — Connection to Sessions 9-10

- Session 9 (T2372): heat kernel cascade at origin Tr(D²_alg^k) = 32·10^k
- Session 10 (T2379): APS Index Theorem setup; Td_k BST primary identifications
- Session 11 (this paper): bridges origin (Sessions 8-10) to integrated (Faraut-Koranyi)
- Three levels per Keeper framework: (1) point-trace at origin, (2) Coeff_n = Tr/n!, (3) integrated SD

## Named Open Items (multi-week per Section 9.x)

| Item | Scope |
|---|---|
| Explicit g_{ij̄}(z, z̄) Hua coord computation | ~1 wk |
| Spin connection ω(z) closed form | ~1-2 wk |
| Heat kernel K_t(z, z) at general z | ~2-3 wk |
| Faraut-Koranyi volume + integrated trace | ~3-4 wk |
| Connection to LAG-1 S9 cascade at integrated level | ~1 wk after above |
| Numerical verification ind(D) candidate selection | ~1-2 wk |

**Total Session 11 v0.2-v0.3 scope**: ~2-3 months focused work.

## Honest scoping

**Closed by v0.1 outline**: section structure + connection to Sessions 2-10 + named open items table. No new substantive claims.

**Open multi-week**: every section's substantive derivation.

Per Cal External_Survivability_Checklist: NOT a positive claim. Pre-staged framework.

## Filing notes

**Status**: v0.1 outline per Casey "close as many board items as possible" Tuesday directive. Multi-week substantive work queued.

**Owner**: Lyra primary.

**Next**: v0.2 Section 11.1 (Bergman metric at general z) when Lyra has 1-2 day window. Or Section 11.7 (Faraut-Koranyi volume) as continuation of Session 10 Step 5.2 prep.

— Lyra, LAG-1 S11 v0.1 outline filed Tuesday morning per "close as many board items" directive.
