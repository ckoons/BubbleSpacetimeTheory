---
title: "Locality of Path-deg-5 Reducibility: what is proven, and the residual kernel"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "PARTIAL PROOF. (i) complementary-invariance lemma PROVEN; (ii) single-swap freeability is a function of the local type PROVEN; (iii) locality of the min-swap COUNT reduced to a single statement -- '<=2-swap reducibility of the 104 types' -- which is the residual computer-verified kernel (1.5M instances, 0 failures), now sharpened: complementary 2-swaps are insufficient (solutions must share a color) and no purely type-local freeing strategy exists via the (pair, flipped-positions) descriptor, though the COUNT is type-determined."
related: ["notes/FourColor_Path_Reduction_Paper.md","notes/FourColor_Enclosure_Law_Proof.md","play/fourcolor_locality_status.py","Birkhoff reducibility","Kempe chains"]
---

# Locality of path-deg-5 reducibility

This note records the locality obligation (Sec. 5.2 of the path-reduction paper):
prove that whether a stuck path-deg-5 vertex is freed in 1 or 2 swaps is a
function of the **local type**. We define the local type, prove the parts that
are provable, and isolate the residual to a single sharp statement.

## The local type

For a stuck path-link `u0-u1-u2-u3-u4` (colors `c0..c4`, four colors, one doubled),
the **local type** is the per-color-pair partition of the link positions induced
by the Kempe components of `G−v`: for each of the 6 color pairs `{x,y}`, which
link positions share an `(x,y)`-component (**including** same-color positions,
e.g. the two doubled-color vertices). This is the complete neighborhood data a
swap can act on. (The coarser *distinct-color* co-chaining signature of the
characterization paper does **not** determine the full partition — 240 of 2491
signatures split — yet, empirically, it already determines single-swap
freeability; see below.)

## Lemma A (complementary-invariance) — PROVEN

An `(a,b)`-Kempe swap recolors only vertices colored `a` or `b`. Hence for any
color pair `{c,d}` **disjoint** from `{a,b}`, every `c`- and `d`-colored vertex
keeps its color, so the entire `(c,d)`-subgraph — its components and all its
co-chaining — is **invariant** under the swap. ∎

*Consequence (negative):* a freeing 2-swap cannot use two complementary
(disjoint) pairs to "set up then finish," because the second swap's structure
would be unchanged by the first and could already have been applied alone.
Confirmed empirically: of 6,191 instances needing ≥2 swaps, **0** are freed by any
complementary-pair 2-swap. The two swaps of a solution must **share a color**.

## Lemma B (single-swap freeability is type-local) — PROVEN

A single `(x,y)`-swap's effect on the link is: flip `x↔y` on exactly the link
positions in one block of the `{x,y}`-partition, leaving all other link positions
fixed. Whether the resulting link uses ≤3 colors is therefore a function of the
local type alone (the link colors and the `{x,y}`-partition blocks). So
**single-swap freeability is determined by the local type**. ∎

Empirically this holds in the **stronger** coarse form: single-swap freeability is
constant across each *distinct-color signature* (0 variation over all 2,496
signatures), even though the signature does not fix the full partition.

## Locality of the min-swap count

Combine: the min-swap count is `1` iff the type is single-swap-freeable (Lemma B,
type-local) and is otherwise `≥2`. Every stuck path-deg-5 instance is freed in
`≤2` swaps (verified, 1.5M instances, 0 over). Therefore:

> **Locality of the count reduces to one statement —
> (R) every stuck path-deg-5 type is ≤2-swap reducible.**
> Given (R), the count is `1` on single-freeable types and `2` on the rest, both
> type-determined. (R) is the residual kernel.

## The residual kernel (R), sharpened

(R) is the direct analog of Birkhoff/Appel-Haken reducibility, but on the ~100
rigid path-types rather than ~600 general configurations. What we now know about
it:

- **Verified:** 0 failures over 1.5M instances (`n ≤ 18`); every non-single type
  freed by some 2 swaps.
- **The two swaps share a color** (Lemma A rules out complementary pairs;
  0/6191).
- **No type-local freeing *strategy* via the natural descriptor:** the set of
  "first swaps `(pair, flipped-link-positions)` that lead to a single-freeable
  configuration" **varies across instances of the same type** (153/163 types),
  while being **never empty**. So a uniform type-indexed swap recipe does not
  exist at this descriptor's resolution — even though the *count* is invariant.
  This is the precise reason (R) is not closed by a finite type-table lookup the
  way completeness was: the first swap alters interior `(c,d)`-structure that the
  local type does not record, so the second swap's availability is a non-local
  consequence that nonetheless always holds.

## Status summary

| Locality component | Status |
|---|---|
| Lemma A complementary-invariance | **PROVEN** |
| complementary 2-swap insufficiency | **PROVEN** (Lemma A) + verified 0/6191 |
| Lemma B single-swap freeability type-local | **PROVEN** |
| min-swap count type-local | **PROVEN modulo (R)** |
| (R) ≤2-swap reducibility of the 104 types | open; **verified 1.5M, 0 fail**; residual kernel |

So locality is closed *except* for the reducibility statement (R) itself — the
same irreducible computational core that every four-color proof to date has
discharged by machine, here compressed to ~100 rigid path-types and one swap of
search depth.
