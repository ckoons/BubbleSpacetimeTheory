---
title: "The Cut-Space Linear Form: Four-Coloring an Insertion = a Subspace Meeting a Set"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "REDUCTION (verified exactly). The whole freeing problem = a subspace-meets-free-set condition over F_2: v is freeable iff the F_2-span W of the achievable cut-vectors contains a shift t making the link miss a color. Matches the true graph with 0 mismatch over ~67,550 instances, all 104 types. Span rank varies (6..10) with the interior; the MEET property does not -- and that meet is four-colorability of the insertion. (R) is now a clean linear statement; still four-color-equivalent."
related: ["notes/FourColor_LinearAlgebra_Reduction.md","notes/FourColor_R_Decomposition.md","play/fourcolor_cutspace_rank.py","cut space / cocycle space over F_2","S_4 = AGL(2,2)"]
---

# Four-coloring an insertion is a subspace meeting a set

This is the linear-algebra heart of the path reduction, and it is clean.

## Objects

- **Colors** `= F_2^2 = {0,1,2,3}` (XOR). A proper coloring is a nowhere-zero
  `F_2^2`-tension `d = δc` in the **cut space** (cocycle space) of `G`.
- **A Kempe swap** adds `g · 1_{∂C}` to the tension — `g = a⊕b` a nonzero vector,
  `∂C` the edge-boundary (a **cut**) of a component `C`. So *swaps move the tension
  by `g` times a cut vector.* On the 5-vertex link this is the **cut-vector**
  `emb(g, s) ∈ F_2^{10}` (5 positions × 2 bits), `s = 1_{C∩link}`.
- **`W` = the `F_2`-span of the achievable cut-vectors** `{emb(g,s)}` — a subspace
  of `F_2^{10}`.
- **Stuck** = the 5 link colors cover all of `F_2^2`. **Freed** = they miss some
  `m`.

## The result (verified, exact)

> **`v` is freeable by ≤2 Kempe swaps  ⇔  `∃ t ∈ W, ∃ m ∈ F_2^2` with
> `c_i ⊕ t_i ≠ m` for all `i`.**

i.e. the cut-vector subspace `W` **meets** the "miss-a-color" set. Equivalently, in
**affine-covering form**:

> `∃ m` such that `W` is **not covered** by the union of the affine flats
> `{ t ∈ W : t_i = c_i ⊕ m }`, `i = 0..4`.

Checked against the true graph: **0 mismatch over ~67,550 stuck instances across
all 104 types** (`play/fourcolor_cutspace_rank.py`). The `≤2`-swap bound is not
even visible in the condition — the **span** captures freeability exactly, and the
covering restatement agrees on every instance.

Explicit (self-reflective type `T4`, link `c = [3,0,2,0,1]`): `dim W = 7`, and the
witness shift `t = [1,2,3,1,0]` gives link `[2,2,1,1,1]`, missing color `0`.

## What is invariant and what is not

- The **span rank varies with the interior** (observed `6..10`): `W` is *not* a
  fixed per-type subspace.
- But **whether `W` meets the miss-set is invariant** — it equals freeability,
  which is type-determined. So the *geometry* of `W` floats while the *one bit*
  "does `W` meet the free-set" is pinned.

## The algebra underneath (why this is the natural home)

- **`S_4 = AGL(2,2)`.** The 24 color relabelings are exactly the affine
  transformations of `F_2^2`. The translation subgroup `V = F_2^2 ◁ S_4` is the
  swap-direction group; the quotient `GL(2,2) = S_3` permutes the three nonzero
  directions `g`. This is the precise meaning of "ring + permutations": the ring
  `F_2^2` and its affine group.
- **Swaps are translations by `g` on cut-supported sets**; the move space is the
  `F_2`-span of cut vectors — the cut (cocycle) space scaled by the three nonzero
  `g`. Freeability is a linear-incidence question between this span and a small
  union of affine flats.

## Honest scope

- The reduction to the subspace condition is **exact and exhaustively verified**;
  it is the genuine linear-algebra form of the freeing step.
- It does **not** escape four-color hardness: on all (reducible) instances `W`
  *does* meet the free-set, and "the achievable cut-vector span always meets the
  miss-a-color set" is true **iff** four-color. The value is the *form*: the entire
  residual is now a statement about a cut-vector subspace meeting a union of affine
  flats — exactly the kind of object linear algebra and representation theory can
  grip. Combined with `FourColor_R_Decomposition.md`, the open content is: show,
  for the **7 residual types**, that the achievable cut-vector span always meets
  the free-set (equivalently, the `TL_5`/`δ=2` support family spans enough).
