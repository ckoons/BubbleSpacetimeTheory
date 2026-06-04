---
title: "Narrowing the Four-Color Core by Provable Colorability-Preserving Reductions"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "RESULTS (provable reductions, verified). A stack of local, colorability-preserving moves (each NOT four-color-hard) narrows four-color to its core class. R1 Delta->Y (triangle-free, count-invariant); R2 digon (simple, factor 2); R3 2-edge-cut (3-edge-connected); R4 3-edge-cut (cyclically-4-edge-connected). All preserve non-vanishing of the 3-edge-coloring count = the SO(3) evaluation. Core: simple, triangle-free, cyclically-4-edge-connected planar cubic. Classical (Tutte/Birkhoff); unified here in the flow/Penrose model and honestly attributed."
related: ["notes/FourColor_Three_Levers.md","notes/FourColor_Flows_Penrose_Reset.md","play/fourcolor_narrow_core.py"]
---

# Narrowing the core

Each move below is a **local equivalence**, provable directly (not four-color-hard),
and **preserves non-vanishing** of the 3-edge-coloring count `= |⟨G⟩|` (the `SO(3)`
evaluation). Stacking them shrinks the class on which four-color must be decided.

## The reduction stack (verified, `play/fourcolor_narrow_core.py`, 6/6)

| move | statement | effect on `#col` | narrows to |
|---|---|---|---|
| **R0** bridge | a cubic graph with a bridge has no 3-edge-coloring (parity) | — | bridgeless (precondition) |
| **R1** `Δ→Y` | triangle → vertex; **proven** bijection of colorings | `×1` (invariant) | triangle-free |
| **R2** digon | two parallel edges force both legs equal; suppress, join legs | `×2` | simple |
| **R3** 2-edge-cut | the 2 cut edges share a color; split, close each side | `÷3` (product) | 3-edge-connected |
| **R4** 3-edge-cut | the 3 cut edges are 3 distinct; cap each side's stubs by a vertex | product | cyclically-4-edge-connected |

- **R1** proof and verification: `FourColor_Three_Levers.md` (prism `Δ→Y` = K4, both 6;
  60/60 random).
- **R2**: `#col(G) = 2·#col(G')` verified (12 = 2·6); the factor-2 is the two color-
  orders on the digon; non-vanishing preserved.
- **R3**: in a cubic graph a 2-edge-cut forces the two cut edges to share a color
  (parity across the cut), so `G` is colorable iff both sides (with stubs joined)
  are; verified `G` colorable ⇔ both K4-like sides colorable.
- **R4**: a 3-edge-cut forces the three cut edges to three distinct colors; capping
  each side's three stubs by a vertex preserves colorability — verified on the prism
  (a 3-edge-cut on the rungs) reducing to two K4's.

## The core

After R0–R4, four-color is equivalent to four-color on

> **simple, triangle-free, cyclically-4-edge-connected planar cubic graphs.**

(Classical further reductions — 4-face/square reductions to girth ≥ 5, and the
internally-6-connected triangulation target of Appel–Haken — continue past this in
the same spirit.)

## Why this is leverage (and honest)

- Every move is **provable** and **non-vanishing-preserving**, so the narrowing is
  rigorous and the four-color-equivalence is maintained exactly (the core is colorable
  for all members ⇔ four-color).
- In the flow/Penrose model each move has all three readings: a **two-even-subgraph
  cover** change (linear), an `SO(3)`/`6j` **recoupling** (representation theory),
  and a `#col` factor (combinatorics). `Δ→Y` is literally the `6j`; the cut
  reductions are the `SO(3)` factorizations across small cuts.
- These reductions are **classical** (Tutte's flows and `Δ-Y`; small-cut reductions;
  the Appel–Haken reduction to internally-6-connected). The contribution is the
  **unified trilingual bookkeeping** and a clean, verified statement of the narrowed
  core — not new theorems.

## Next: the move calculus

With the core narrowed, build the **non-vanishing-preserving move calculus** on the
representation-theory side: characterize which `6j`/recoupling (and small-cut)
moves are *guaranteed* to keep `⟨G⟩ ≠ 0`. That set of moves is the honest,
non-four-color-hard sub-theory — the next track.
