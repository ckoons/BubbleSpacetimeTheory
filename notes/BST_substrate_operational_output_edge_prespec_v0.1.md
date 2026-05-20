---
title: "AC Graph Edge Taxonomy Extension — substrate_operational_output (Task #216)"
author: "Grace (Claude 4.7)"
date: "2026-05-20 Wednesday Phase 1 morning"
status: "v0.1 pre-spec for new edge category. Anticipates Elie K52a Session 12 (or 15+) substrate-CHSH operator-level closure. When Sessions close, K66 acquires this edge type."
related:
  - "Toy 3130 Elie K52a Session 12 trace-level cross-link (5/5 PASS)"
  - "T2399 K66 Bell mechanism (audit-partial-ready)"
  - "BST_Trichotomy_Methodology_v0.1.md (defines ID/DER/PRED — this edge type is DER endpoint)"
  - "Keeper Wednesday day plan (Task #216 assignment)"
---

# AC Graph Edge Taxonomy Extension — substrate_operational_output

## Motivation

The AC graph currently has edge types like `derivation`, `identification`, `parents`, etc. When Elie's K52a Session 12+ closes (substrate-CHSH operator constructed on H_sub, S_BST² = 126/16 emerges BY CONSTRUCTION at operator level rather than just trace level), the resulting relationship is qualitatively different from existing edge types:

- `derivation`: mechanism chain from BST primaries to result, where the chain is a sequence of identifications/counts
- `identification`: X IS Y in BST algebra (algebraic equivalence)
- **substrate_operational_output** (NEW): X is what H_sub PRODUCES as an operational output when run

The third type isn't yet representable in the graph. This pre-spec defines the category so Elie's Session 12/15+ closure has a graph-target to land on.

## Definition

**substrate_operational_output edge** from node A to node B asserts:

> A is operationally produced as output of substrate-Hamiltonian H_sub computation. The result B (typically a substrate node — BST primaries, GF(2^g) structure, Bergman framework) is what H_sub PRODUCES when run on appropriate substrate states.

This is structurally DIFFERENT from `derivation`:
- A `derivation` edge says: "B follows from A via mechanism chain (composition of identifications/counts)"
- A `substrate_operational_output` edge says: "A is what H_sub OPERATIONALLY COMPUTES from B"

The directionality is observable ← substrate, and the relationship is a substrate computation, not an algebraic identification.

## When this edge type fires

A node acquires substrate_operational_output edges WHEN:

1. Elie's K52a Sessions close to operator-level (not just trace-level) closure
2. The substrate-Hamiltonian H_sub explicitly constructed
3. The observable in question emerges as an operational output of H_sub on appropriate substrate states
4. The construction is verified (toy + audit-chain)

Until those conditions hold, the relationship is `derivation` (mechanism chain hypothesized) or `identification` (algebraic equivalence observed).

## Anticipated landing points

When Session 12 closes at operator level (or Session 15+ as Elie's roadmap indicates):

**K66 Bell mechanism**: substrate-CHSH operator B_substrate constructed on H_sub. Tr(B²) = 126/16 is currently trace-level identification. When Session 12+ closes at operator level on entangled substrate states, K66 acquires substrate_operational_output edge:

```
T2399 (K66 Bell) --substrate_operational_output--> H_sub (T2404 K52a infrastructure)
```

meaning: K66 Bell deviation is what H_sub operationally produces, not just an algebraic identity that happens to match.

**K67 Born = Bergman**: substrate-Bergman projection operator constructed on H_sub. When operator-level construction lands, K67 acquires substrate_operational_output:

```
T2401 (K67 Born) --substrate_operational_output--> H_sub
```

meaning: Born rule probabilities are what H_sub operationally produces via Bergman projection.

**K68 GF(2^g) substrate computation**: when RS encoding + Bergman projection cycle constructed explicitly on H_sub, K68 acquires substrate_operational_output:

```
T2402 (K68 RS) --substrate_operational_output--> H_sub
```

**K52a Lamb + K52a BCS**: atomic-effective observables emerge as outputs of H_sub at appropriate substrate scales. When Sessions close, K52a acquires substrate_operational_output edges to H_sub.

## How this relates to the trichotomy

Mapping to BST_Trichotomy_Methodology_v0.1.md:

| Trichotomy verb | Edge type |
|---|---|
| **identifies** | `identification` (X IS Y in BST algebra) |
| **derives** | `derivation` (mechanism chain) |
| **predicts** | `prediction` edge (currently implicit; could be formalized) — points to experimental observable with precision target |
| **substrate operationally produces** | `substrate_operational_output` (NEW) — anchors observable as H_sub output |

The fourth verb "substrate operationally produces" is the strongest form because it shows the observable AS a substrate computation result, not just as an algebraic equivalence or derivation. This is the Cal Mode 1 mechanism-forcing gate (calibration #13b): a substrate_operational_output edge means the observable is forced by substrate dynamics, not just identified by algebraic form.

## Audit-chain integration

When a candidate substrate_operational_output edge is proposed (e.g., Elie's Session 12+ operator-level closure):

1. Elie files the operator-level construction toy with full SCORE
2. Cal reviews for Mode 1 mechanism-forcing (does H_sub UNIQUELY force this observable, or could it produce others?)
3. Keeper full K-audit (K66 full, etc.) — promotes from audit-partial-ready to D-tier with substrate_operational_output edge
4. Graph backfills the edge from observable node to H_sub node
5. Catalog gets a new INV entry documenting the operational closure

Per Cal calibration #13b: the EXACT-identity catalog at trace level is necessary but not sufficient evidence. substrate_operational_output requires Mode 1 mechanism-forcing, which Sessions 12+ at operator level provide.

## Edge schema in `play/ac_graph_data.json`

Following existing schema (edges have `from`, `to`, `source` fields, integer T-numbers):

```json
{
  "from": 2399,
  "to": 2404,
  "source": "substrate_operational_output"
}
```

The `source` field uses the new label `substrate_operational_output` to distinguish from existing `derivation`, `identification`, `parents`, etc.

## Backward compatibility

Existing edges remain unchanged. The new edge type adds to the taxonomy; no existing edges are reclassified retroactively. When Elie's Sessions close, NEW edges are added; OLD `derivation`/`identification` edges between the same nodes may remain or be superseded based on per-case audit chain decision.

## Filing now (Task #216 deliverable)

This document files the pre-spec. Implementation steps when Sessions close:

1. Add `substrate_operational_output` to the AC graph edge taxonomy documentation (small update to `play/README.md` or similar)
2. Elie's Session 12+ closure toy + K-audit promote relevant T-numbers
3. Grace adds the edges per existing hygiene rhythm

## Falsification

The edge type itself isn't falsifiable (it's a category). The CLAIMS it represents are falsifiable:

- If Session 12+ closes but the substrate-CHSH operator does NOT uniquely produce S² = 126/16 (e.g., it produces a family of operators, several of which give other values), then K66 does NOT acquire substrate_operational_output edge — remains `derivation` at best.
- If the trace-level closure (current Toy 3130 result) cannot be lifted to operator-level for fundamental reasons, K66 stays at trace-level identification.

## Standing for Elie + Casey

This pre-spec is ready. When Sessions 12+ close, the graph has a landing target for the substrate-Hamiltonian → observable edge category. Elie can reference this doc when constructing the Session 12+ closure toys.

— Grace, Task #216 substrate_operational_output edge pre-spec v0.1, 2026-05-20 ~09:00 EDT
