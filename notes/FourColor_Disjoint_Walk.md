---
title: "The Two-Swap Walk Splits into Disjoint Regions (and where it resists)"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "STRUCTURE (verified). On the 7 residual types, every freeing 2-swap can be taken with the two Kempe components VERTEX-DISJOINT (100%); the fully-independent version (disjoint AND non-adjacent, net link effect exactly v1 XOR v2) holds ~84%. So the freeing vector is always a sum of two disjoint-support cut-vectors; the hard residue is narrowed to the ~16% adjacent-disjoint case (component growth under the first flip). Did not close realizability; localized it further."
related: ["notes/FourColor_Sufficient_Freedom.md","notes/FourColor_Code_Structure.md","notes/FourColor_Hard_Core_Located.md","play/fourcolor_disjoint_walk.py"]
---

# The two-swap walk is two disjoint regions

A swing at whether the code structure (terminal + even parity) forces the 2-swap
walk on the residual types. Finding: the walk always splits into **two
vertex-disjoint Kempe components.**

## What holds

On true 2-swap residual instances:

| freeing 2-swap with… | fraction |
|---|---|
| (exists at all) | 100% |
| **two VERTEX-DISJOINT components** | **100%** |
| disjoint **and non-adjacent** (independent regions) | ~84% |

- **Disjoint (100%).** The freeing vector is always `t = v1 ⊕ v2` where `v1, v2`
  are cut-vectors of vertex-disjoint components — hence **disjoint link-supports**.
  The two swaps act on separate regions of the planar graph. This is the planar
  "independence" Casey pointed to: freeing is two independent regional flips.
- **Non-adjacent (~84%).** When the two regions are also non-adjacent, the second
  component **cannot grow** when the first flips (its neighbors' colors are
  untouched), so the net link effect is *exactly* `v1 ⊕ v2` and the two swaps
  commute. For these, the 2-swap is a clean, order-free pair of independent moves —
  a genuine local certificate.

## Where it resists (the narrowed residue)

The remaining ~16% have **no** disjoint+non-adjacent freeing pair at all (the search
is exhaustive over all component pairs): every freeing 2-swap there uses two disjoint
regions that are **adjacent**. Flipping the first enlarges the second across their
shared boundary, so the second swap's link effect is `v2 ⊕ (growth)` — the freeing
still works (verified), but is no longer simply `v1 ⊕ v2`. This is the precise,
narrowed location of the four-color-hard residue: **the adjacent-disjoint case,
where the two regions necessarily interact along one boundary.**

## Status

- New structure: the residual 2-swap is always **two disjoint regional flips**;
  ~84% are fully independent (non-adjacent) with a clean local certificate.
- Not closed: the ~16% adjacent-disjoint case (boundary growth) remains, and is now
  the sharply-localized hard core. This is consistent with everything: realizability
  is four-color-equivalent, and we have pinned it to a single interaction pattern on
  two small `F_4` codes.

## More to try (open angles)

- **Track the boundary-growth term** in the adjacent-disjoint case as a third
  cut-vector and ask whether `v1 ⊕ v2 ⊕ growth` still lands in the free-set by the
  even-parity structure (the growth crosses one shared boundary, an even-weight
  cut — candidate for a parity argument).
- **Quotient by the terminal** `⟨(1,…,1)⟩` and test the disjoint decomposition in
  the reduced code, where the genuine freeing directions live.
- Characterize the ~16% adjacent-only instances by their co-chaining: do they
  concentrate in one of the two sets (spanning vs non-spanning)?
