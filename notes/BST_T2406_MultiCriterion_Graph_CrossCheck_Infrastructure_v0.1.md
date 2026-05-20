---
title: "Task #206 D_IV⁵ Multi-Criterion Uniqueness — Graph-Side Cross-Check Infrastructure (Task #218 / Grace)"
author: "Grace (Claude 4.7)"
date: "2026-05-20 Wednesday Phase 2 cartography sweep"
status: "v0.1 — infrastructure pre-spec ready for Lyra C8 advance. Waiting for trigger; meanwhile build catalog format + edge category + cross-reference template."
related:
  - "T2406 / Toy 3135 (C2 + C3, Lyra)"
  - "T2407 / Toy 3137 (C2+C3+C4, Lyra)"
  - "T2408 / Toy 3140 (FIVE criteria, Q⁵ Chern structural fact, Lyra)"
  - "T2409 / Toy 3144 (SIX criteria, C7 Faraut-Koranyi, Lyra)"
  - "BST_DIV5_Strong_Uniqueness_Theorem_Framework_v0_1.md (Lyra paper-grade consolidation)"
  - "BST_substrate_operational_output_edge_prespec_v0.1.md (Grace Task #216 — related edge taxonomy)"
---

# Task #206 Multi-Criterion Uniqueness — Graph-Side Cross-Check Infrastructure

## Motivation

Lyra's Task #206 enumeration produces a multi-criterion uniqueness theorem for D_IV⁵. Each criterion (C1-C8) is an independent boundary in the space of small irreducible Hermitian symmetric domains. D_IV⁵ uniquely satisfies the intersection.

The graph-side question: how do we represent this in the AC graph + catalog so that:
1. Each criterion is a node with edges to D_IV⁵ uniqueness
2. The intersection structure (multi-criterion convergence) is queryable
3. When new criteria are added (e.g., C8 multi-week pending), the graph extends without restructuring
4. Cross-reference template lets external readers verify each criterion independently

## Criterion catalog format (proposed)

Each criterion C_i gets a structured catalog entry:

```json
{
  "id": "CRIT-C2",
  "criterion_name": "Rank equals BST rank = 2",
  "test": "HSD must have rank = 2",
  "candidates_passing": ["D_IV_5"],
  "candidates_failing": ["D_I_{1,5}", "D_I_{5,1}", "D_II_n", "D_III_n", "D_V", "D_VI"],
  "verification_toy": "Toy 3135",
  "registered_in_theorem": "T2406",
  "tier": "D",
  "multi_week_pending": false
}
```

This format applies to C1-C7 (all v0.1-v0.4 in Lyra's framework) and C8 when it lands.

## AC graph edge category (proposed)

Add new edge category `multi_criterion_uniqueness` to the existing edge taxonomy:

```json
{
  "from": <CRITERION_NODE>,
  "to": <D_IV5_UNIQUENESS_NODE (T1427 APG)>,
  "source": "multi_criterion_uniqueness"
}
```

The semantics: each criterion node points to the D_IV⁵ uniqueness anchor (T1427 APG / Autogenic Proto-Geometry). The COUNT of incoming edges = strength of uniqueness claim. When C8 closes, the count goes from 7 → 8 and the theorem promotes from "6/8 criteria, multi-week pending" to "8/8 criteria — full multi-criterion convergence."

## Cross-reference template (proposed)

For each criterion, the catalog entry should cross-reference:

| Field | Description |
|---|---|
| Criterion statement | One-line statement (e.g., "Bergman exponent (n+2)/2 = 7/2 at n = 5") |
| BST primary involved | Which primaries (g, rank, N_c, etc.) appear in the criterion |
| Mathematical foundation | Classical reference (Cartan classification, Faraut-Koranyi 1994, etc.) |
| BST integration | How this criterion connects to BST framework |
| Toy reference | The verification toy (Toy 3135, 3137, 3140, 3144, ...) |
| Theorem reference | The registry entry (T2406-T2409, T2410+ for C8) |
| Independent candidates | List of HSDs tested |
| Verdict | UNIQUE / NON-UNIQUE / MULTI-WEEK PENDING |
| Mode 1 status | Cal Mode 1 mechanism-forcing assessment per calibration #13b |
| Bridge to other criteria | Cross-link to overlapping criteria (e.g., C6 + C7 both involve Chern data) |

## Six criteria currently registered (snapshot before C8)

Based on Lyra T2406-T2409:

| Criterion | Statement | Verification | Status |
|---|---|---|---|
| **C1** | Complex dimension = n_C = 5 | (implicit in HSD enumeration) | UNIQUE up to type |
| **C2** | Rank = 2 | Toy 3135 (T2406) | UNIQUE |
| **C3** | Bergman exponent (n+2)/2 = g/rank = 7/2 | Toy 3137 (T2407) | UNIQUE |
| **C4** | GF(2^g) Mersenne compatibility (g = 7) | Toy 3137 (T2407) | UNIQUE |
| **C5** | BST primaries forced by structure | Toy 3140 (T2408) | UNIQUE |
| **C6** | Q-quadric Chern classes ARE small BST-family integers (1, n_C, 11, 13, N_c², N_c) | Toy 3140 (T2408) | UNIQUE |
| **C7** | c_FK = (N_c·n_C)²/π^(9/2) reproduces classical Faraut-Koranyi volume | Toy 3144 (T2409) | UNIQUE |
| **C8** | Möbius cohomology Z/2 spectral parity (Wallach K-type) | pending Lyra LAG-1 S10 Step 5.2 | MULTI-WEEK PENDING |

**Six independent criteria all uniquely select D_IV⁵.** When C8 closes, eight.

## Connection to Graph Forces Principle

Each criterion is a separate boundary in HSD-space. D_IV⁵ at the intersection of multiple boundaries is the **substrate-selection analog** of overdetermined-identity clusters at the theorem level (Graph Forces signature, Casey-named candidate).

The relationship:
- **At theorem level**: same quantity in multiple BST-primary forms (Q=126 in 5 forms, etc.) — overdetermined IDENTITY
- **At substrate-selection level**: same substrate selected by multiple independent uniqueness criteria — overdetermined SUBSTRATE

If Graph Forces holds at both levels, the principle is universally diagnostic. Lyra's six-criterion convergence is direct evidence at substrate-selection level.

## Implementation status

This document files the **infrastructure pre-spec**. When Lyra advances C8 (T2410+), the implementation steps:

1. Add CRIT-C1 through CRIT-C8 catalog entries (template ready above)
2. Add `multi_criterion_uniqueness` edge category to AC graph
3. Backfill edges from each criterion node to T1427 APG uniqueness anchor
4. Update `data/bst_geometric_invariants.json` with full multi-criterion catalog
5. Cross-reference template applied to each criterion entry
6. Lyra's Strong-Uniqueness Theorem Framework v0.2 cites this infrastructure as the graph-side complement

## Cross-link to T2408 Chern-class structural finding

Lyra's T2408 result deserves special attention: the Chern classes of Q⁵ Bridge Object are (1, n_C, 11, 13, N_c², N_c) — small BST-family integers, NOT external numbers. This means:

**The BST primaries don't just describe D_IV⁵; they ARE the Chern data of the natural bridge object connecting D_IV⁵ to gauge symmetry.**

In graph terms: the Bridge Object Q⁵ has a topology forcing-relation to BST primaries. Adds a new edge category candidate: `chern_class_forcing` — node A (BST primary integer) ← node B (Q⁵ Chern class), with source = "topology forces primary".

This is structural ammunition for Casey's question about substrate selection: D_IV⁵'s BST primaries aren't free parameters; they're forced by the topology of the natural bridge object. Multi-criterion uniqueness (Task #206) + Q⁵ Chern-forcing (T2408) together close the substrate-selection question at the meta-uniqueness level.

## Waiting-for-trigger items

- Lyra C8 (Möbius cohomology + Wallach K-type sketch) — multi-week
- When C8 closes: implement multi-criterion catalog + graph edges
- When C8 closes: Lyra ships Strong-Uniqueness Theorem v0.2 with graph-side citation

Meanwhile, this infrastructure pre-spec is ready. No idle.

— Grace, Task #218 multi-criterion graph-side cross-check infrastructure v0.1, 2026-05-20 ~10:45 EDT
