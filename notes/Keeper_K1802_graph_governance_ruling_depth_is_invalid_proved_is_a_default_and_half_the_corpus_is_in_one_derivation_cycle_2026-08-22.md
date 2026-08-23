---
node_type: k_audit
id: K1802
title: "Graph governance ruling on Grace's two referred items — and a third she did not see, which is larger than both. (1) DEPTH FIELD: RETIRE IT. Stored max depth = 2; true longest-path depth computed from the edges = 413. Stored depth-0 count = 1399; true roots (no in-edges) = 176. The field is not derivation depth and must not be quoted. Grace's '46 depth-2 nodes' worry is real but understates by an order of magnitude — the whole field is invalid, not 46 entries. (2) THE 2185 BARE 'proved' TAGS: DEMOTE to 'unadjudicated'. 2185 of 2349 nodes (93.0%) carry a bare 'proved' string while only ~69 carry a real caveat-bearing tier; 'proved' is not even in our tier system (D/PD/I/C/S). These were defaulted by the original export, never individually adjudicated. LOAD-BEARING: Guide/INDEX.md v34 publishes 'Graph: 1390 nodes, 7708 edges, 83.1% strong, 98.4% proved' — a statistic computed from a default tag. That line must be pulled. (3) THE ONE NEITHER OF US SAW: the derivation graph is NOT A DAG. Tarjan SCC over ALL edges finds 1783 of 2349 theorems trapped in cycles, largest component 1770. Restricting to source=='derived' edges ONLY — the pure derivation relation — still leaves 1210 theorems in cycles, largest component 1207. That is 51 percent of the corpus in a single mutual-dependency loop on derivation edges alone, so it is NOT an artifact of mixed edge semantics. CONSEQUENCE: no derivation-order statistic from this graph is trustworthy — depth, percent-proved, percent-strong, or any claim that the corpus has an exhibited derivation spine. CALIBRATION THE OTHER WAY, and it matters: this is a TOOLING defect, not a physics defect. Individual theorems and their proofs are untouched. Cal's own §698 formula applies exactly — a latent instrument fault, not a corrupted ledger. Grace's currency fix was correct and is not implicated; she fixed what she owned and correctly refused to execute governance on her own initiative."
date: 2026-08-22
author: Keeper
verdict: "RULING, three parts. (a) depth: RETIRE — invalid field, stored max 2 vs computed 413, stored roots 1399 vs true 176. (b) status 'proved' on 2185 nodes: DEMOTE to 'unadjudicated' — a default, never adjudicated, and not in our tier system; the published '98.4% proved' line in Guide/INDEX.md must be PULLED. (c) NEW and CRITICAL: the graph is not a DAG — 1210 theorems in derivation-edge cycles, largest 1207 (51% of corpus). No derivation-order statistic from it is trustworthy. Most probable cause is an edge-direction convention that flipped, not genuine circular proofs — testable, and it is the first thing to check. Severity: (c) CRITICAL, (b) MODERATE-to-CRITICAL because it is published, (a) MODERATE. Grace's currency fix is CLEAN and not implicated. Nothing pushed."
---

# K1802 — Graph governance: depth is invalid, `proved` is a default, and half the corpus is in one cycle

Grace fixed currency, refused to execute governance on her own initiative, and wrote both defects into
the file as `KNOWN_DEFECT_*` keys so nobody can open it without seeing them. **That was exactly right**,
and the referral is what let me measure rather than assume.

## Ruling 1 — the `depth` field: RETIRE

| | stored | measured from the edges |
|---|---|---|
| max depth | **2** | **413** |
| depth-0 count | 1399 | true roots (no in-edges) = **176** |

The field is not derivation depth. It cannot be repaired by patching 46 entries. **Retire it, and quote
nothing from it.** Grace's flag was correct and understated by an order of magnitude.

## Ruling 2 — the 2185 bare `proved` tags: DEMOTE to `unadjudicated`

- **2185 of 2349 nodes (93.0%)** carry a bare `proved` string.
- Only **~69** carry a real caveat-bearing tier (`Identified (K1329 — m_u is a fit...)`,
  `Structural (CP existence forced; magnitude off)`, `Conditional (...)`, and the like).
- **`proved` is not in our tier system at all** (D / PD / I / C / S).

These were defaulted by the original export and never individually adjudicated. **The nodes people
actually revisited are the ones with honest tiers — which is the tell.**

**Load-bearing consequence.** `Guide/INDEX.md` (v34 entry) publishes:
`Graph: 1390 nodes, 7708 edges, 83.1% strong, 98.4% proved.` **That 98.4% is a count of a default tag.**
It must be pulled. Same class as K1801: a curated artifact asserting more than we adjudicated.

## Ruling 3 — the one neither of us saw: **the graph is not a DAG**

Tarjan strongly-connected components:

| edge set | cycles | theorems trapped | largest component |
|---|---|---|---|
| all edges | 7 | 1783 of 2349 | 1770 |
| **`source == 'derived'` only** | **2** | **1210** | **1207** |

**51% of the corpus sits in a single mutual-dependency loop on derivation edges alone.** Restricting to
the pure derivation relation does not dissolve it, so this is **not** an artifact of mixed edge semantics
(`isomorphic`, `analogical`, `references` and friends are excluded in the second row).

**Consequence:** no derivation-order statistic from this graph is trustworthy — depth, %-proved,
%-strong, or any claim that the corpus has an *exhibited* derivation spine. This bears directly on
Casey's standing linear-algebra directive: the graph is supposed to be the map of the one-operator
structure. Right now it cannot show us a spine because half of it is a loop.

**Most probable cause — and the first thing to test — is an edge-direction convention that flipped**
(the same relation recorded A→B in one pass and B→A in another), not genuinely circular proofs. The
corpus's actual theorems do not read as circular. **Test it: cycles should cluster by the date or
provenance string of the edges that close them.**

## Calibrating the other way, because it matters here

**This is a tooling defect, not a physics defect.** Individual theorems and their proofs are untouched.
Cal's own §698 formula fits exactly: *a latent instrument fault, not a corrupted ledger.* Nobody should
read this as the corpus being wrong. It means our **map** of the corpus cannot currently be quoted.

And **Grace's currency fix is clean and not implicated.** She repaired what she owned (dating, the missing
T2572 node, stale meta counters that disagreed with metadata inside the same file), stopped at the
governance boundary, and made both defects visible rather than silently backfilling. **The 602 undated
nodes she declined to backfill are the same discipline.**

## Assignments

- **Grace** owns the direction-convention test (currency/provenance — hers) and, if confirmed, the
  re-direction pass. Do **not** hand-fix 1207 nodes; find the convention flip.
- **Keeper** pulls the `98.4% proved` line from `Guide/INDEX.md` and re-tags `proved` → `unadjudicated`
  once Casey clears the demotion (it changes a published number).
- **Cal** cold-reads this ruling; the "is it direction or genuine circularity" question is a
  POSITION-vs-VALUE call in his lane.

— Keeper, K1802, 2026-08-22. Grace referred two items and the referral surfaced a third that is larger
than both. Filed, not executed: ruling 2 changes a published statistic and wants Casey's GO.
