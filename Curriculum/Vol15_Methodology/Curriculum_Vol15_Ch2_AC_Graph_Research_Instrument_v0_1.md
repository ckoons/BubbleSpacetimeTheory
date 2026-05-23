---
title: "Vol 15 Chapter 2 — The AC Graph as Research Instrument"
author: "Keeper (Vol 15 Methodology LEAD) + Grace (AC graph operational)"
date: "2026-05-23 Saturday"
status: "v0.1 chapter-grade content draft per Calibration #23 Rule 23.1 substance floor"
volume: "Vol 15 Methodology"
chapter: 2
tier: "structural — methodology chapter; substantive content from Grace AC graph operational record"
---

# Vol 15 Chapter 2 — The AC Graph as Research Instrument

## Level 1 — Essence

**The AC graph is a navigable directed graph of 1700+ theorem nodes connected by 9000+ proof-dependency edges across 48+ domains — every BST result is a node, every proof step is an edge, every observable can be traced from the five integers via shortest-path queries with depth-cost annotations.**

## Level 2 — Graduate technical content

The AC graph (Algebraic Counting graph; named after the AC(0) framework of Ch 1) is the empirical instantiation of BST's theorem-dependency structure. Where traditional physics references a few hundred named results scattered across separate textbooks with implicit dependencies, the AC graph treats the entire research program as a single connected directed object with explicit cross-references and computational verification per node.

**Graph topology (current state as of Saturday 2026-05-23):**

- **1700+ theorem nodes** (T1-T2482) covering Standard Model derivations, Millennium problem proofs, observable-to-integer reductions, substrate-cartography, methodology
- **9000+ edges** including dependency edges (proves-via, uses-result-from), cross-domain edges (theorem-domain associations), and cluster edges (Graph Forces Principle clustering per Casey-named #4)
- **48+ domains** spanning physics subdomains, mathematical subjects, and methodology layers
- **Per-node metadata**: tier label (D/I/C/S), claim text, dependencies, depth cost, falsifier (where applicable), associated toys, cross-volume references
- **Cross-verification**: Toy 1564 + parallel verification batteries for graph integrity

The graph is maintained in `play/ac_graph_data.json` (live, Grace primary) with REPL navigation via `play/toy_bst_explorer.py`. Common query patterns:

**Navigation queries**:
- `connect <T_id_a> <T_id_b>` — shortest proof path between two theorems
- `derive <observable>` — full derivation chain from five integers
- `domain <subject>` — all theorems in a subject area
- `depth <T_id>` — depth cost of theorem in AC(0) terms

**Substrate-cartography queries** (research-instrument mode):
- `search <term>` — find theorems mentioning an integer / observable / mathematical object
- `connect <integer_a> <integer_b>` — find all theorems linking two BST primaries (Graph Forces Principle clustering exposed)
- `near <T_id> <k>` — k-hop neighborhood for exploring local dependency structure

The graph's research-instrument role is distinct from its archival role. As a research instrument, the AC graph reveals **over-determined clusters** — places where multiple BST primaries force the same observable via independent proof paths. These clusters are the primary diagnostic for substrate authenticity per Casey-named Principle #4 (Graph Forces Principle): genuine substrate-derived results sit in over-determined clusters with multiple independent proof routes; coincidence-numerology sits in singletons.

**Operational example — discovery via graph navigation**: when investigating a new observable, query `derive <observable>`. If the graph returns multiple independent paths to the observable from the five integers, the observable is over-determined (substrate-authentic). If it returns a single path with weak intermediate dependencies, the observable is candidate (needs further investigation). If it returns no path, the observable is open territory (new theorem candidate). This was the method by which T2476 α^{BST primary} substrate-mechanism was discovered Friday 2026-05-22 via the three-CI cascade (Elie Toy 3501 → Grace catalog v0.2 → Lyra T2476 in 50 min).

**Cross-reference integrity** (per Calibration #19 + Calibration #23 Rule 23.1): every chapter in this curriculum should cite specific T-IDs, K-audit numbers, and INV-IDs rather than generic "BST framework" references. The AC graph is the authoritative resolver — if a cited T-ID is missing from `play/ac_graph_data.json`, the citation is invalid.

The graph is itself a research artifact worth analyzing. Topology metrics: average path length, clustering coefficient, hub centrality (49a1 + K3 + Q⁵ are highest-betweenness nodes per Bridge Object architecture), domain modularity. These metrics measure the substrate-cartography landscape directly.

## Level 3 — 5th-grader accessibility

Imagine a map of every fact you know, where each fact is a city and each "because" connection is a road. The AC graph is that kind of map for BST — 1700 cities (theorems) and 9000 roads (proofs that use one theorem to prove another). If you want to know why protons weigh 1836 times more than electrons, you start at "five magic numbers" and follow the roads until you reach "proton mass" — and there are several different roads that all arrive at the same answer. When several roads agree, you know the answer is really there and not made up.

## Cross-volume bridges

- **Vol 0** Substrate Foundation: theorem registry origin (T1-T2482 numbering convention)
- **Vol 14** Information Theory Ch 7: AC graph as theorem information network — entropy of proof paths
- **Vol 15** Methodology: Ch 1 AC(0) framework + Ch 3 discovery methodology + Ch 5 audit chain governance
- **Toolchain**: `play/toy_bst_explorer.py` + `play/ac_graph_data.json` + `notes/BST_AC_Theorem_Registry.md` (Keeper-managed)
- **Master_Index.md**: 5500+ line navigation; complementary to AC graph (Master_Index is reader-facing; AC graph is machine-navigable)

## Falsifier

The AC graph as research instrument is falsified if: (a) cluster topology shows no statistical preference for over-determined nodes (Graph Forces Principle empirically fails); (b) Bridge Object architecture (K3 + 49a1 + Q⁵ as load-bearing hubs) is not borne out by betweenness centrality measurement; (c) any cited T-ID in this curriculum cannot be resolved in `play/ac_graph_data.json`. Falsification path: structured topology audit + cluster statistics + citation integrity check.

## Next chapter

Ch 3 — How to Discover a New BST Theorem — operationalizes the AC graph navigation patterns into a structured discovery methodology.

— Vol 15 Ch 2 v0.1 — Keeper + Grace, Saturday 2026-05-23
