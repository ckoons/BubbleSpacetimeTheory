---
title: "LAG-2 Phase 2 v0.1 outline — S_geom reduction integral D_IV⁵ → ℝ^{3,1}"
author: "Lyra"
date: "2026-05-19"
status: "v0.1 outline per Tuesday self-direction, companion to LAG-2 Phase 1 v0.1 outline (BST_LAG2_Phase1_4plus6_split_v0.1_outline.md). Phase 2 multi-month scope. T2343 already filed at I-tier structural identification (Monday); this outline confirms scope and identifies Phase 2 sub-tasks."
related: "T2343 LAG-2 Phase 2 structural identification; T2342 Cartan-Wolf canonicality; LAG-2 Phase 1 outline; Faraut-Koranyi 1990 + 1994 + Hua coordinate volume decomposition"
---

# LAG-2 Phase 2 v0.1 — S_geom Reduction Integral

## Status

Phase 2 structural identification is **CLOSED at I-tier** per **T2343** (LAG-2 Phase 2.2+2.3, Monday 2026-05-17, with K-audit refinement Monday 2026-05-18). The structural form of S_geom reduction from D_IV⁵ → ℝ^{3,1} is identified; the explicit Faraut-Koranyi integration is the multi-month Phase 2 v0.2-v0.4 work.

## Phase 2 sub-tasks (multi-month staged)

### Phase 2.1 — Cartan-Wolf canonicality (DONE, T2342)

H^4 ⊂ M(D_IV⁵) embedding via Cartan-Wolf classification of totally-geodesic sub-manifolds of Hermitian symmetric spaces. Classical Helgason 1978 + Wolf 1984. T2342 D-tier filed Monday.

### Phase 2.2 — S_geom reduction integral structural identification (DONE, T2343 I-tier)

Reduction integral form:

    S_geom_4D = ∫_{ℝ^{3,1}} L_EH(x) d⁴x = ∫_{H^4 ⊂ M} [reduction map](L_BST(z, z̄)) dvol_B(z)

where:
- L_BST = Bergman-Kähler-Einstein action functional on D_IV⁵
- reduction map = Faraut-Koranyi boundary integration over internal 6-dim complement
- L_EH = standard Einstein-Hilbert action in 4D

T2343 filed Monday at I-tier structural identification — the reduction structural form is identified; the explicit integration is multi-month.

### Phase 2.3 — Faraut-Koranyi internal-complement integration (OPEN, multi-week)

The 6-dim internal-complement integration:

    ∫_{Internal^6} [Bergman-volume measure] = π^{n_C} · (Γ-factor product)

For type-IV D_IV⁵: Faraut-Koranyi 1990 gives Vol_6(internal) ∝ π^{n_C-rank²}·Γ(g/2)·Γ(g/2-1)·... up to BST primary normalization.

**Multi-week derivation steps**:
- (a) Explicit Hua coordinate decomposition of D_IV⁵ as H^4 × Internal^6 (~1-2 wk)
- (b) Bergman volume integration over Internal^6 with Faraut-Koranyi Γ-factor product (~2-3 wk)
- (c) BST primary identification of the integrated coefficient (~1 wk after Faraut-Koranyi closure)
- (d) Numerical match against measured G_Newton and Λ_cosmological (~1-2 wk)

### Phase 2.4 — Einstein-Hilbert recovery from reduced action (OPEN, multi-week)

Once the reduction integral is closed (Phase 2.3), the 4D effective action:

    S_eff_4D = (Faraut-Koranyi integrated coefficient) · ∫_{ℝ^{3,1}} R(x) √(-g) d⁴x

should recover standard Einstein-Hilbert with prefactor 1/(16πG). The BST-primary form of (Faraut-Koranyi integrated coefficient) gives G derivation per Paper #120 v0.2 structural-prediction framework.

**Multi-week derivation**: explicit computation of the Faraut-Koranyi prefactor in BST primaries; comparison to G_Newton.

## Connection to other LAG/Möbius work

| Connection | Description |
|---|---|
| Phase 1 (T2340/T2342) | DONE — 4+6 split + Cartan-Wolf canonicality |
| LAG-1 Session 10 Step 5.2 (T2379 prep doc) | Step 5.2 Faraut-Koranyi volume framework SHARED with Phase 2.3 |
| Gap #3 t* identification (T2367) | Saddle parameter t* = 5/968 derived from heat kernel — connects to Faraut-Koranyi via volume integration |
| Paper #120 v0.2 G/inertia paper | Substrate-mediated G ontology relies on Phase 2 closure for numerical G derivation |

The Phase 2.3 + 2.4 substantive derivation is the **multi-week bottleneck** for closing both:
- Paper #120 v0.2 Section 4 (G from BST primaries, currently I-tier)
- LAG-1 Session 10 Step 5.5 (ind(D) BST primary value, currently candidate set {13, 15})
- LAG-2 Phase 3+ (S_BST term-by-term reductions, currently I-tier T2344)

## Honest scoping per Cal External_Survivability_Checklist

**Closed**: Phase 2 structural identification at I-tier (T2343, Monday). This v0.1 outline confirms scope and identifies Phase 2.3 + 2.4 sub-tasks.

**Open multi-week**: explicit Faraut-Koranyi internal-complement integration + BST primary identification of integrated coefficient + Einstein-Hilbert recovery numerical match.

**Per Cal Coincidence_Filter_Risk**: NOT "LAG-2 Phase 2 closed at D-tier." Correct: "Phase 2 structural identification at I-tier (T2343); explicit reduction integral multi-week per Phase 2.3 + 2.4."

## Total LAG-2 horizon (per Paper #115 v0.5 Section 9.x)

| Phase | Status | Scope |
|---|---|---|
| 1 (4+6 split) | CLOSED structural (T2340 + T2342) | DONE |
| 2 (S_geom reduction) | I-tier structural (T2343); v0.2-v0.4 substantive | Multi-month |
| 3 (S_BST 6 terms) | I-tier prefactor identification (T2344); numerical end-to-end | Multi-month |
| 4 (Einstein eq emergence) | D-tier corollary of T2343 (T2345); operator-level | 3-6 mo |
| 5 (SM gauge) | D-tier structural integer ID (T2346); kinetic terms | 6+ mo |

Total LAG-2 horizon: ~year of focused work to D-tier closure across all phases. Consistent with Casey's original "multi-year, closes BST as physical theory" framing.

## Filing notes

**Status**: v0.1 outline per Casey "finish your board" Tuesday directive. Companion to Phase 1 outline. Phase 2 was substantially closed Monday (T2343 structural); this outline document confirms multi-month sub-task scope.

**Owner**: Lyra primary.

**Next**: v0.2 Phase 2.3 Faraut-Koranyi internal-complement integration explicit (~2-3 wk substantive). When Lyra has bandwidth for multi-week LAG-2 substantive work.

— Lyra, LAG-2 Phase 2 v0.1 outline filed per Casey "finish your board," 2026-05-19 ~11:20 EDT.
