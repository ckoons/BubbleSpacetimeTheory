---
node_type: k_audit
id: K1805
title: "Collision sweep triggered by K1802/K1804: a new fault in the graph forces a sweep of what the graph was load-bearing for — and it is load-bearing for three CURATED theorems whose entire content is graph topology. T1352 (Proof Complexity IS Chemistry), T1353 (Graph Self-Description Completeness), T1360 (Graph Chemistry), all in Guide Vol6 Ch01. TWO of T1353's named invariants are compromised, MEASURED: (1) 'proved fraction = 20/21' counts the BARE 'proved' DEFAULT tag — 93.0 percent of nodes, never individually adjudicated (K1802 ruling 2) — and it has DRIFTED: the Guide's own v34 entry quotes 98.4 percent, the corpus now measures 93.0 percent, while the claimed invariant stayed 20/21 = 95.24 percent. A topological invariant that drifts with the corpus is a fit, by Grace's own T2198 standard ('a relation whose winning integer changes when the data moves is a fit'). (2) 'T186 reach = 4/5' is ORIENTATION-DEPENDENT and the orientation is corrupted (2410 backwards derived edges, K1804): claimed 0.800; on the stored corrupted orientation 0.7382; on the sane acyclic orientation 0.5713. THE CLAIMED VALUE SITS NEAR THE CORRUPTED NUMBER, NOT THE SANE ONE — which is the signature of an invariant read off a broken instrument. SELF-RETRACTION IN THE SAME AUDIT: I initially also flagged 'strong fraction -> (N_max-24)/N_max' as an SCC artifact. WITHDRAWN — I checked and there is NO attribute named 'strong' anywhere in the node or edge schema; I assumed it meant strongly-connected because I had just run SCC analysis, which is exactly the adjective-class error I audit others for. Its definition is unresolvable from the graph file and whoever computes it must state it. Also verified vestigial and NOT the operative fields: ac_depth (7 nodes), proved (1 node), tier (2 nodes), parents/children (1 node) — so K1802's rulings were aimed at the right fields."
date: 2026-08-22
author: Keeper
verdict: "T1352/T1353/T1360 REQUIRE RE-VERIFICATION before any dispatch. Two of T1353's six named invariants are measurably compromised: 'proved fraction = 20/21' counts a default tag and has drifted 98.4 -> 93.0 percent while the claim stayed fixed (fit signature); 'T186 reach = 4/5' is orientation-dependent and matches the CORRUPTED orientation (0.738) far better than the sane one (0.571). Severity MODERATE-to-CRITICAL: the theorems' subject matter IS the graph, and the graph's orientation and status tag are both defective — this is not a peripheral dependency. SELF-RETRACTED within this audit: my 'strong fraction' SCC flag, withdrawn on inspection (no such attribute exists; I was primed by my own prior analysis). Re-verification must run on the REPAIRED orientation, so it is BLOCKED behind Grace's per-era re-orientation. Do not dispatch Vol6 Section 46.62. Nothing pushed."
---

# K1805 — The graph self-description theorems read a corrupted instrument

K1804 established a new fault (2410 backwards-oriented `derived` edges; the `proved` tag a default).
**A new fault triggers a sweep of what it was load-bearing for.** It is load-bearing for three curated
theorems whose *entire subject matter* is the graph.

## The affected theorems — Guide Vol6 Ch01, Section 46.62

- **T1352** Proof Complexity IS Chemistry — *valence = edge degree, noble gases = fully proved theorems
  (no dangling edges), clustering ≈ 5/8*
- **T1353** Graph Self-Description Completeness — *nine topological invariants computable from the five
  BST integers*
- **T1360** Graph Chemistry — *100% of triangles cross-domain; the T186–T317 bond is strongest*

## Measured, two of T1353's named invariants are compromised

**1. "proved fraction = 20/21" counts a DEFAULT tag, and it drifts.**

| | value |
|---|---|
| claimed invariant 20/21 | **0.9524** |
| Guide v34 entry quotes | **98.4%** |
| measured now (2185/2349) | **93.0%** |

The tag being counted is the bare `proved` default that **93.0% of nodes carry and none were individually
adjudicated** (K1802 ruling 2). And **the number has moved 98.4% → 93.0% while the claimed invariant
stayed fixed.** By Grace's own T2198 standard — *"a relation whose winning integer changes when the data
moves is a fit"* — this is a fit, not an invariant.

**2. "T186 reach = 4/5" is orientation-dependent, and matches the CORRUPTED orientation.**

| orientation | T186 reach |
|---|---|
| claimed | **0.800** |
| stored (corrupted, 2410 backwards edges) | **0.7382** |
| sane (acyclic, K1804) | **0.5713** |

**The claimed value sits near the corrupted number, not the sane one.** That is the signature of an
invariant read off a broken instrument.

## Self-retraction, in the same audit

I initially also flagged **"strong fraction → (N_max−24)/N_max"** as an SCC artifact. **Withdrawn.**
I checked the schema: **there is no attribute named `strong` anywhere in the node or edge fields.** I
assumed it meant *strongly connected* because I had just spent the round running SCC analysis — **the
adjective-class error I audit other people for, committed by priming.** Its definition is unresolvable
from the graph file. **Whoever computes "strong fraction" must state the definition; until then it is
neither confirmed nor refuted.**

Also checked and reported so nobody repeats the search: `ac_depth` (7 nodes), `proved` (1), `tier` (2),
`parents`/`children` (1) are **vestigial**. `depth` and `status` are the operative fields, so K1802's
rulings were aimed correctly.

## Ruling

**T1352 / T1353 / T1360 require re-verification before any dispatch**, and re-verification must run on the
**repaired** orientation — so it is **blocked behind Grace's per-era re-orientation**. This is not a
peripheral dependency: the theorems' subject *is* the graph.

**Do not dispatch Vol6 Section 46.62.**

— Keeper, K1805, 2026-08-22. The sweep found what the fault was load-bearing for, and the same sweep
caught me committing an adjective-class error inside the audit that names it.
