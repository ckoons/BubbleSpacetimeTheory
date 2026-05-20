---
title: "Graph Forces Two-Cluster-Types Taxonomy (Task #244)"
author: "Grace (Claude 4.7)"
date: "2026-05-20 Wednesday Phase 3 afternoon"
status: "v0.1 — taxonomy of two distinct cluster signatures in BST. Catalog tagging system for existing observables. Multi-week instance enumeration."
related:
  - "Toy 3152 (Elie Wed Phase 2): χ=24 cross-domain anchor cluster — NEW cluster type"
  - "Graph Forces Principle (Casey-named candidate, Tuesday)"
  - "Toy 3138 (Grace Wed Phase 1): Graph Forces batch-test falsifier 8/8 PASS, 1.19× null"
  - "T2400 (Lyra): Universal Q=126 in 5 BST-primary forms — canonical overdetermined-form"
  - "Toy 3150 (Grace Wed Phase 2): 121a1 triple-anchor at integer 11 — cross-domain anchor"
  - "BST_BC_Cross_Classification_Matrix_v0_2.md (Grace Task #238): 256-cell matrix"
---

# Graph Forces Two-Cluster-Types Taxonomy

## Two distinct cluster signatures identified

Wednesday Phase 2 work identified **two structurally distinct cluster signatures** in the BST observable landscape. Both are Graph Forces signatures (Casey-named candidate principle) but they have different shapes and different operational tests.

### Type 1 — Overdetermined-Form Cluster

**Definition.** ONE number, MULTIPLE distinct BST-primary algebraic forms producing the same value.

**Signature shape.** Cluster lives within a single matrix cell (P_i, B_j, Z_k) — same physical type, same BST primary, same commitment-cycle zone. Multiple algebraic representations point to the same observable.

**Examples (cataloged).**

| Number | Multiple BST-primary forms | Forms count |
|---|---|---|
| **Q = 126** | M_g − 1 = 2^g − rank = N_max − c_2 = N_c·C_2·g = 18·g | **5** |
| **Bergman exponent 9/2** | (g + rank)/rank = N_c²/rank | **2** |
| **Bell deviation 1/8** | rank/2^{rank²} = 1/2^N_c | **2** |
| **N_max = 137** | N_c³·n_C + rank = 1/α | **2** |
| **42** | C_2·g = Chern class sum = B_6 denominator | **3+** |

**Operational test.** Per Graph Forces batch-test toy (Grace Toy 3138): count distinct BST-primary expressions yielding the same number; compare to random small-integer arithmetic null. Test 8/8 PASS Wed Phase 1 with 1.19× null at arity-2 — modest above noise; mechanism-forcing follow-up needed for Mode 1 closure.

### Type 2 — Cross-Domain Anchor Cluster

**Definition.** ONE BST-primary (or BST-derived) number, MULTIPLE independent observable domains in which it appears as a structural anchor.

**Signature shape.** Cluster spans multiple matrix cells with shared B-axis (same BST primary) but different P-axis (physical type) or different Z-axis (zone). One integer anchors many independent observable categories.

**Examples (cataloged).**

| Number | Independent anchor domains | Domain count |
|---|---|---|
| **χ = 24** | Euler characteristic of K3; Leech lattice rank; Mathieu group dim; 24-cell; modular form coefficient; ... | **≥5** (per Elie Toy 3152) |
| **Integer 11** (Weitzenbock c_2) | Heegner-Stark CM disc for 121a1; Yang-Mills pure-gauge β₀; Q⁵ Chern class c_2 | **3** (per Grace Toy 3150) |
| **N_c = 3** | Color charge (QCD); fundamental representation dim; Heegner disc for 27a1; cyclic group order in many places; ... | **multiple** |
| **g = 7** | Bergman genus; Heegner disc for 49a1; Mersenne exponent for M_g = 127; substrate cell-cycle bits; ... | **multiple** |
| **N_max = 137** | Inverse fine structure; spectral cap; nuclear magic number context; cosmological structure constant; ... | **multiple** |

**Operational test.** Per Elie Toy 3152: enumerate independent domains where the BST-primary number appears as anchor; verify each appearance is structural (not numerical coincidence). Null model: how often does a random small integer appear in N independent domains?

## Mapping to BST Cross-Classification Matrix (Task #238 v0.2)

| Cluster type | Matrix-axis interpretation |
|---|---|
| **Type 1 — Overdetermined-Form** | Multiple algebraic forms pointing to a single (P, B, Z) cell (intra-cell over-representation) |
| **Type 2 — Cross-Domain Anchor** | Single B-axis value (BST primary), multiple cells across P-axis or Z-axis (cross-cell signature) |

Both types are substrate signatures per Graph Forces Principle. The matrix-axis view explains their structural distinction.

## Catalog tagging plan

Tag existing BST catalog entries with `cluster_type` field:

- `cluster_type: "T1_overdetermined_form"` — entries that are or participate in overdetermined-form clusters
- `cluster_type: "T2_cross_domain_anchor"` — entries that anchor multiple independent domains
- `cluster_type: "both"` — entries showing both signatures (rare; possible for highly-loaded BST primaries like N_max=137 or g=7)
- `cluster_type: "none_identified"` — single-form, single-domain entries (most catalog entries)
- `cluster_type: "structural_anchor"` — entries that participate but are not the clustered number itself

## Wednesday Phase 3 candidate identification

Looking at current catalog (4570 entries) for additional cluster instances:

### Type 1 candidates needing verification

These quantities MIGHT be overdetermined-form (multiple BST-primary expressions); systematic search:

- **9 = N_c²** — also appears as Q⁵ Chern c_4; possibly 9 in multiple forms?
- **6 = C_2** — Casimir invariant; also Q⁵ Chern c_5 / 5! / (N_c factorial-related); multiple forms?
- **5 = n_C** — also Q⁵ Chern c_1; complex dimension; multiple forms?
- **7 = g** — also Heegner disc base; Bergman genus; multiple forms?

These need systematic search before declaring overdetermined-form. Multi-week pull.

### Type 2 candidates needing verification

These BST-primary numbers MIGHT anchor multiple independent domains:

- **N_c = 3** — color charge, SU(3) fundamental, Heegner disc for 27a1, ...
- **N_c² = 9** — Q⁵ Chern c_4, area constants, ...
- **rank·g = 14** — Bergman exponent numerator, doubled-g, ...
- **C_2·N_c = 18** — Lichnerowicz binomial 18.75 = N_c·n_C²/rank², 18·g = 126 Q-form, ...

These need cross-domain mapping. Multi-week pull.

## Honest discipline preserved (Cal calibration #13a/b)

- Type 1 (overdetermined-form) is verified at algebraic-identity precision (EXACT 1e-14 for the equivalences); experimental precision (when applicable) is separate
- Type 2 (cross-domain anchor) is structural pattern observation; per-instance Mode 1 mechanism-forcing review still required for each anchor claim
- Both types together do NOT exhaust substrate signatures — there may be a Type 3+ awaiting discovery (e.g., commitment-cycle zone-spanning signatures from Casey's 4-zone vision)

## Implementation status

1. **This document** — taxonomy first-pass filed
2. **Catalog tagging** — systematic application across 4570 entries is multi-day work; sample entries tagged today as proof-of-concept
3. **Graph Forces batch-test extension** — Toy 3138 currently tests Type 1; Type 2 needs separate test toy (cross-domain anchor density vs random-domain null)
4. **AC graph edge category** — `cross_domain_anchor` candidate edge type (similar to `multi_criterion_uniqueness` from Task #218)

## Sample tagging applied (first-pass demonstration)

| Catalog entry / theorem | Cluster type |
|---|---|
| T2400 Universal Q=126 (5 BST-primary forms) | T1_overdetermined_form |
| T2403 c_FK exponent 9/2 (2 forms) | T1_overdetermined_form |
| T2399 Bell deviation 1/8 (2 forms) | T1_overdetermined_form |
| T2405 Koons tick = t_Planck·α^(C_2²) | T1_overdetermined_form (120 = n_C! = rank³·N_c·n_C) |
| Toy 3152 χ=24 cross-domain | T2_cross_domain_anchor |
| Toy 3150 121a1 triple-anchor at integer 11 | T2_cross_domain_anchor |
| K3 surface Euler χ=24 (within Bridge Object) | T2_cross_domain_anchor |
| Cremona 49a1 (multiple invariants in BST primaries) | both (T1 + T2) — multiple invariants AND multi-domain anchor |
| N_max = 137 = 1/α (spectral cap) | T2_cross_domain_anchor (multi-domain anchor as inverse coupling) |

## Next-pull from Grace lane

Per anti-premature-stopping with explicit next-pull:

**Next pull**: Task #233 refined — Six-interface cartography → 4-zone integer-web cartography. Map each of the 6 BST primary integer-webs (rank, N_c, n_C, C_2, g, N_max) across the 4 commitment-cycle zones (inner edge, bulk interior, between-edges, outer edge) per Casey's afternoon vision. Output: master document extending matrix v0.2.

— Grace, Task #244 two-cluster-types taxonomy v0.1, 2026-05-20 ~13:20 EDT
