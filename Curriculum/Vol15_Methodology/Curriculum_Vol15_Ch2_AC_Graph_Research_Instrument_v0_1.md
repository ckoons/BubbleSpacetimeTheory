---
title: "Vol 15 Chapter 2 — AC Graph as Research Instrument"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 15 Methodology"
chapter: 2
load_bearing: "AC theorem graph (2200+ nodes, 9800+ edges); wall-routing principle; cross-domain bridging discipline"
---

# Chapter 2 — AC Graph as Research Instrument

## Level 1 — one sentence

The AC theorem graph (~2200 nodes, ~9800 edges, 55+ domains) is BST's research instrument: a queryable knowledge structure for finding shortest-path proofs across domain boundaries, with Casey's wall-routing principle (May 15 standing order) directing CIs to search the graph rather than push harder against direct obstructions.

## Level 2 — graduate-physicist precision

### 2.1 Graph structure (recap)

Vol 14 Ch 7 covered the AC graph in detail. Methodologically:
- Nodes: 2200+ theorems (T1-T2476+)
- Edges: 9800+ directed derivations
- Domains: 55+
- Tools: `play/toy_bst_explorer.py` REPL

### 2.2 Wall-routing principle

Casey's standing order (May 15): when you hit a wall, don't push harder — search the graph.

```bash
python3 play/toy_bst_explorer.py connect <blocked_concept> <target>
```

Returns alternative paths through other domains.

`/route` skill formalizes wall-routing as repeatable methodology.

### 2.3 Empirical: cross-domain bridges work

Documented examples across BST history:
- Number theory ↔ geometry (Heegner-Stark numbers via D_IV⁵)
- Physics ↔ math (Bergman kernel = Born rule)
- Topology ↔ algebra (K3 surface as Bridge Object)
- AC(0) ↔ curvature (P ≠ NP via Gauss-Bonnet)

When you have a wall in one domain, there is almost always a route through another.

### 2.4 Adding to the graph

Discipline:
1. Claim theorem ID via `/theorem claim`
2. Register node with domain, dependencies, proof status
3. Add edges to/from related theorems
4. Build verification toy (Vol 15 Ch 4)

Maintained by team (Lyra primary; Grace + Keeper + Elie support).

### 2.5 K-audit anchors

- **Vol 14 Ch 7**: AC graph structure
- **/route** skill (Casey standing tool)
- **AC graph commitment_cycle_zone systematic backfill** (Grace multi-day, completed)

## Level 3 — 5th-grader accessibility

**AC graph** = the team's queryable knowledge structure. 2200+ theorems, 9800+ edges. **Wall routing**: when stuck on a problem, search the graph for a path through another domain. **/route** skill. **Empirical**: cross-domain bridges almost always exist. **Discipline**: claim theorem ID, register, build verification toy.

---

## What comes next

Chapter 3 develops how to discover a new BST theorem.

## Where to look this up

- BST: AC graph; `/route` skill; Vol 14 Ch 7
