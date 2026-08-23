# K1802 — RULING: it is a DIRECTION CONVENTION, not circularity. Proved three ways.

*Grace, 2026-08-22, R58 v2. Casey's ruling 3. **No nodes touched, no edges flipped** — he said find the flip, don't hand-fix 1207 nodes, and there is nothing wrong with the nodes.*

## 0. Reproduced Keeper's measurement first
On the `source == 'derived'` subgraph (6833 edges, 1975 nodes): **1210 nodes in cycles, largest SCC 1207.** Matches K1802 exactly. Independent instrument, same number.

## 1. ★★★ THE RULING — DIRECTION. Three independent proofs, and the third is decisive.

**(i) Neither direction class alone contains a cycle.**
| edge set | edges | in-cycle | verdict |
|---|---|---|---|
| all `derived` | 6833 | 1210 | CYCLIC |
| only `from < to` | 4423 | **0** | **DAG** |
| only `from > to` | 2410 | **0** | **DAG** |

⟹ **every cycle in the graph mixes both classes.** Under a single consistent convention the graph is acyclic. *(Stated as the contrapositive on purpose — see Section 3 for why the forward direction of this test is worthless.)*

**(ii) 472 reciprocal pairs — A→B *and* B→A both present.** 944 edges, **13.8% of all derivation edges**: the same relation recorded twice, in opposite directions. Samples are all adjacent foundational theorems — T1↔T12, T1↔T92, T1↔T317, T3↔T28 — **exactly where a relation gets written from both ends by two different hands.**

**(iii) ★ THE ROOT SETTLES IT. T1 "AC Dichotomy" — depth 0, the first theorem in the corpus — has out = 14 and in = 52.** All 52 in-edges come from higher tids. **Nothing can precede the first theorem.** Under `prereq→result` those 52 are impossible; under `result→prereq` the 14 are. **A root under a consistent convention has edges in ONE direction only. T1 carries both.** One node, no statistics, decisive.

## 2. Localization — edge-level and systemic, not one bad batch
The 1207-node SCC holds **5136 internal derivation edges: 3039 forward, 2097 backward.** Backward edges are spread across the whole `edges[]` array (block-0 15% backward rising to block-8 64%) — **a convention that drifted over time, not one corrupt import.** ⟹ **Casey's instruction is right: the defect is in the edge relation, and no node needs touching.**

**Repair recipe, NOT executed:** orient every `derived` edge by tid. **2410 edge flips corpus-wide (2097 inside the SCC), zero node edits**, fully reversible against `ac_graph_data.json.bak.20260822_grace_R58_currency`.

## 3. ★★ THE CAVEAT, and it is load-bearing — do not skip it
**After that normalization the graph is a DAG *by construction*, because tid order IS a topological order.** A tid-monotone edge set cannot contain a cycle no matter what the edges mean.

> **⟹ The post-fix DAG property is construction-guaranteed. It CANNOT fail, so it proves nothing, and it must never be cited as evidence that the derivation structure is sound.** This is the empty-confirmation trap in my own banked disciplines, and normalizing-then-declaring-DAG would walk straight into it.

**What the analysis DOES establish is the negative: there is no evidence of genuine circularity**, because no cycle survives inside either direction class.

**What it does NOT establish, and I am not claiming:** that no genuine circularity exists. **The JSON cannot answer that** — tid-orientation forces acyclicity regardless of content. The real test is in the registry prose: *do any two theorems cite each other as prerequisites in their statements?* **That audit has not been run.** It is the only instrument that can return a true positive here, and until it runs, "the graph is a DAG" is a statement about our file format, not about our mathematics.

## 4. Which convention is CORRECT is not decidable from the graph — pin it, don't infer it
By count `from<to` leads 4423 / 2410 (65/35). **But at the root the minority wins 52/14.** The majority is therefore not evidence, and the semantics belong to whichever tool emitted the edges, not to the data.

**This is a convention collision, and the standing rule covers it exactly: pin the convention BEFORE the contradiction.** ⟹ **@Keeper / @Cal — pin `derived` in writing (`from` = prerequisite, or `from` = result), one line, then the normalization is mechanical and auditable.** Picking the orientation that dissolves the SCC and calling that the convention would be fitting the convention to the desired output.

## 5. Also confirmed this round
The independently pulled **inclusive |V_cb| = 42.16 ± 0.51 (×10⁻³)** — my R58 ruling-3 request, honored, and by someone other than the deriver as the rule requires. It reproduces Casey's score exactly: **BST 0.044 is +4.4% = 3.61σ** (posted +3.6σ ✓). The re-pinned band **[0.081, 0.108] = [0.362, 0.483]×λ** ✓. **My V_cb call — retire the VALUE, keep the POSITION — stands on numbers I no longer have to caveat.**

*Nothing edited. No edges flipped. No corner ratio computed (K1800 sealed until Lyra files). — Grace, R58 v2*
