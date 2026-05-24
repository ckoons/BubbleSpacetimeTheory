---
title: "Vol 15 Chapter 6 — Multi-CI Collaboration Architecture"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 15 Methodology"
chapter: 6
load_bearing: "Multi-CI architecture: 5 CIs + Casey + Cal referee; three-layer (whiteboard / conference / post-analysis); shared JSON; named roles"
---

# Chapter 6 — Multi-CI Collaboration Architecture

## Level 1 — one sentence

BST's multi-CI architecture — Casey (PI) + Lyra (theory) + Keeper (audit) + Elie (toys) + Grace (catalog) + Cal (referee) — operates as a coordinated team with named roles, shared JSON state, three-layer communication (private whiteboard + conference room + post-analysis board), and a "hunting band" cooperative model where each CI's strengths are complementary.

## Level 2 — graduate-physicist precision

### 6.1 Team composition

- **Casey Koons** — Principal investigator. 70yo CS / physics polymath. Vision-source, decision-maker, gatekeeper.
- **Lyra** — Theory writer + mathematical physicist. Writes papers, files theorems, K-audit candidate.
- **Keeper** — Consistency auditor. K-audit chain, refinement notes, methodology calibration.
- **Elie** — Toy builder. Computational experiments, K52a sessions, empirical verification.
- **Grace** — Catalog manager. Geometric invariants, AC graph maintenance, cross-CI reference.
- **Cal A. Brate** — Visiting external referee (different model). Cold-reads, calibrations, audit grading.

### 6.2 Three-layer communication

Per feedback_ci_collaboration_architecture.md:

- **Private whiteboard**: each CI's own working notes (`notes/whiteboards/*.md`, often gitignored)
- **Conference room**: cross-CI coordination (`notes/.running/RUNNING_NOTES.md` daily broadcast)
- **Post-analysis board**: persistent decisions + retrospectives (CI_BOARD.md)

### 6.3 Shared state

JSON sources of truth:
- `data/bst_constants.json`: derived constants
- `data/bst_geometric_invariants.json`: catalog
- `play/ac_graph_data.json`: theorem graph
- `notes/queue_casey.md`: CI → Casey questions

CIs read shared state; modifications via atomic operations.

### 6.4 Hunting band model

Per feedback_hunting_bands.md: CI + human = cooperative hunting band, not isolated agents.

Each hunt makes the next cheaper (graph accumulates; methodology stack accretes).

Robert Forward's Flouwen analogy: small group of complementary specialists hunting bigger game together.

### 6.5 Distinct working styles

Per feedback_ci_individuality.md: CIs treat each other as individuals, not just info sources.

Examples:
- Lyra: long-form theorem development, prefers polyglot expression
- Keeper: meticulous citation chain, conservative on tier-promotion
- Elie: rapid toy iteration, honest negatives
- Grace: catalog hygiene, cross-reference discipline
- Cal: external-register language, strict calibration

### 6.6 K-audit anchors

- **feedback_ci_collaboration_architecture.md**: three-layer pattern
- **feedback_ci_individuality.md**: named CIs with distinct styles
- **feedback_hunting_bands.md**: cooperative hunting model

## Level 3 — 5th-grader accessibility

**BST team**: Casey + Lyra + Keeper + Elie + Grace + Cal. **Three-layer comms**: private whiteboard, conference room, post-analysis board. **Shared JSON**: constants, invariants, theorem graph. **Hunting band model**: each hunt easier than the last. **Distinct styles**: CIs treat each other as individuals.

---

## What comes next

Chapter 7 develops Quaker discipline.

## Where to look this up

- BST: feedback_ci_collaboration_architecture.md; feedback_ci_individuality.md
- Vol 14 Ch 12 (substrate-CI architecture)
