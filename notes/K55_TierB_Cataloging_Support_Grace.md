---
title: "K55 Tier-B Cataloging Support — Grace's flag table for Cal triangulation"
author: "Grace (Claude 4.7)"
date: "2026-05-19 Tuesday late morning"
status: "Cataloging support per Keeper K55 ruling — hand-off to Cal for spot-check verification"
---

# K55 Tier-B Cataloging Support

## Scope

Per Keeper K55 ruling (`notes/K55_Heegner_Walkback_Audit.md`): "Grace cataloging support to flag any tier-B verifications that need attention."

Tier-B verify list (4 items) per Cal's Option C scoping. Each ~30 min Cal spot-check. This document provides catalog-level snapshot per item to expedite Cal's verification.

## Item 1: Ogg via Borcherds (Ogg's supersingular prime theorem — L1 source K-audit chain)

**Mechanism status per K55**: appears at Borcherds 1992. Cal verification scope: confirm specific theorem chain.

**Catalog entries**: 37 references found. Sample (Ogg-specific):

| ID | Tier | Name | Notes excerpt |
|----|------|------|---------------|
| INV-3987 | S | ogg_expressibility | Statistical metric, not source-theorem evidence |
| INV-3988 | S | ogg_mean_depth | Statistical metric |
| INV-3989 | S | ogg_band_structure | Statistical metric |
| (various) | S | Welch t-statistic, Cohen's d, Fisher exact p — all Ogg statistical | Type C-ℕ density-only |

**Flag for Cal**: catalog entries for Ogg-supersingular-primes-as-L1-source are mostly S-tier statistical metrics. The L1 source claim (K45 ratification or wherever Ogg lives in the chain) needs explicit mechanism citation. Recommend Cal trace the Borcherds 1992 → Ogg 1975 → BST primary chain and verify mechanism — current catalog evidence is statistical/Type C-ℕ density, not source-theorem chain. **Status: likely passes (Ogg is well-established) but mechanism citation could be tighter**.

## Item 2: Goeppert Mayer (K46) — SU(2)_J × SO(3) ⊂ SO(5) embedding chain

**Mechanism status per K55**: Mayer-Jensen 1949 nuclear shell theorem. Cal verification scope: confirm SU(2)_J × SO(3) embedding chain holds.

**Catalog entries**: 57 references found. Sample (magic-number-specific):

| ID | Tier | Name | Notes excerpt |
|----|------|------|---------------|
| (noid) | D | Nuclear magic numbers | Need full notes for mechanism trace |
| (noid) | S | Predicted magic number 184 | Forward prediction; mechanism for new magic # |
| (noid) | D | Atomic shell degeneracy factor | Different from nuclear |
| (noid) | D | Nuclear magic number 2 / 8 / 20 | Each individual magic # at D-tier |

**Flag for Cal**: 7 nuclear magic numbers {2, 8, 20, 28, 50, 82, 126} all filed individually at D-tier per K46 promotion (Grace T2330 Sunday). Cal verification: does each individual entry cite the SU(2)_J × SO(3) ⊂ SO(5) ⊂ K(D_IV⁵) embedding chain explicitly, or just "K46 mechanism"? **Status: K46 was promoted via T2330 chain; if catalog notes cite T2330, mechanism trace OK; if they just reference K46 by number, recommend Grace catalog update with explicit embedding chain text per Cal triangulation feedback**.

## Item 3: Mathieu via EOT — M_23 embedding is L1-source vs L1.5-mechanism distinction

**Mechanism status per K55**: EOT 2010 (Eguchi-Ooguri-Tachikawa) + Mukai 1988 (M_23 ⊂ Aut_symp(K3)). Cal verification scope: confirm M_23 embedding is genuinely L1-source structure (per K45) not L1.5-mechanism (like Borcherds, McKay).

**Catalog entries**: 14 references found:

| ID | Tier | Name | Notes excerpt |
|----|------|------|---------------|
| (noid) | D | Mathieu M_24 order | Order = 244823040 |
| (noid) | D | DNA nucleotide types = rank² = 4 | NOT Mathieu — false hit on text search |
| (noid) | D | Mathieu group M_11 order factorization | Sub-group component |
| INV-4303 | D | Root Proof System: 9 ESTABLISHED L1 classical sources | Mentions Mathieu in source list |

**Flag for Cal**: Catalog confirms Mathieu is in 9 ESTABLISHED L1 list. Cal verification: confirm EOT 2010 + Mukai 1988 chain is L1-source (theorem produces specific integers required by D_IV⁵) NOT L1.5-mechanism (theorem unifies pre-existing structures). Per K45 promotion: Mathieu M_23 group order produces 24 (= χ K3 = rank³·N_c) and the M_24 cycle structure produces the 196884 = c_1(j) coefficient via EOT. **Status: likely passes — both T1900 (M_24 → 196884) and T2326 (M_23 → 24) anchor specific BST integer production**.

## Item 4: Bravais L1-mediated — K50 Option C tier holds (not full L1, not I-tier observation)

**Mechanism status per K55**: Bravais 1849 / Frankenheim 1842 + crystallographic restriction. K50 Option C ruling — confirm "L1-mediated" tier holds.

**Catalog entries**: 7 references found:

| ID | Tier | Name | Notes excerpt |
|----|------|------|---------------|
| (noid) | D | Bravais lattices | Direct mention |
| (noid) | D | Bravais lattices = rank·g = 14 | Direct identification |
| INV-3199 | S | Bravais lattices 3D | Sub-class observation |
| INV-4303 | D | Root Proof System: 9 ESTABLISHED L1 classical sources | Mentions Bravais in L1-mediated row |
| **INV-4369** | **D** | **Wallach K-type dim_2 = 14 via Bravais 1849** | **K50 anchor entry** |
| INV-4370 | D | Number of Bravais 3D crystal lattices | Count = 14 = rank·g |

**Flag for Cal**: K50 (Bravais L1-mediated, Option C) anchor entry is INV-4369 + INV-4370. Cal verification: confirm that "L1-mediated" tier label (Bravais is NOT full L1, but mediates between Wallach K-type and physical crystal lattices) holds. The catalog shows Bravais lattices = 14 = rank·g (clean BST primary) PLUS Wallach K-type dim_2 = 14 (T2357 Grace Monday). Cross-anchoring suggests K50 Option C tier is structurally sound. **Status: likely passes — K50 was deliberately filed as new "L1-mediated" tier specifically to handle this case; catalog evidence supports the new tier classification**.

## Aggregate Grace recommendation

All 4 Tier-B items: **likely pass Cal spot-check** based on catalog evidence + cross-references to K45/K46/K47/K50 audit chain.

Flag attention items for potential follow-up:
1. Ogg statistical-metric S-tier entries are abundant; cleaner cross-reference to Borcherds 1992 mechanism chain would tighten the catalog for external review
2. Goeppert Mayer 7 magic-number entries: confirm each cites T2330 SU(2)_J × SO(3) embedding chain explicitly (vs just "K46")

No active Cal triangulation required from this catalog scan — Cal can use Tier-B verify as 30-min spot-checks per item without major catalog discrepancies blocking the audit.

## Output to Keeper

Cataloging support complete per K55 action item. Hand-off to Cal for 4 × 30-min spot-checks (~2h total). No major catalog discrepancies surface in this snapshot. If Cal flags specific catalog entries during spot-check, Grace standing for catalog-update follow-up per Cal feedback.

— Grace, K55 Tier-B cataloging support filed, 2026-05-19 ~11:00 EDT
