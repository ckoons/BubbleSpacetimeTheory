---
title: "Where Four-Color's Difficulty Lives: One Linear Implication on Seven Flats"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "CAPSTONE of the reduction arc. The type-flat lemma splits into a PROVABLE forward direction (freeable => the type-flat meets the free-set) and an irreducible four-color-hard residue (the flat meeting the free-set => actually freeable). On the 7 residual types the type-flat equals the true achievable span exactly (0% slack), so the entire residual difficulty of four-color is localized to a single linear implication on 7 explicit affine flats. Honest: this LOCATES the hardness, it does not remove it (still four-color-equivalent)."
related: ["notes/FourColor_Type_Flat.md","notes/FourColor_Cutspace_Linear_Form.md","notes/FourColor_R_Decomposition.md","play/fourcolor_direction_split.py"]
---

# Where the difficulty lives

This closes the linear-algebra arc with an honest, precise statement of *exactly*
where four-color's difficulty sits — and what is provable around it.

## The containment

For a stuck path-deg-5 insertion, the true achievable cut-vectors span `true_W`,
and the type-flat (built from co-chaining alone) is `W_type`. A true `(a,b)`-
component restricted to the link is a **union of whole distinct-co-chaining
blocks** (each recorded co-chained pair forces one block; same-color merges only
union whole blocks), and `emb` is `F_2`-linear on disjoint supports. Hence

> **`true_W ⊆ W_type`** — verified with **0 violations / 60,881 instances**.

## The split

- **Forward — PROVABLE.** If `v` is freeable, a freeing ≤2-swap is the sum of two
  achievable cut-vectors, a vector of `true_W ⊆ W_type` that misses a color. So
  **freeable ⇒ `W_type` meets the free-set.** (Necessity of the flat condition.)
- **Reverse — the four-color-hard residue.** `W_type` meets the free-set ⇒ `v`
  freeable. Because `W_type` can be strictly larger than `true_W`, this is not
  automatic: it asserts the flat's *extra* freedom is always realizable.

## The seven flats carry it with no slack

The strict enlargement `W_type ⊋ true_W` happens **only among the 97 single-swap
types** (~9% of their instances) — where freeing happens anyway. On the **7
residual (2-swap) types**, measured:

> **`W_type = true_W` exactly — 0% strict enlargement / 1,682 residual instances.**

So for the seven types the type-flat *is* the true achievable span. Combining:

- 97 single-swap types: **freeable** (one Kempe swap; type-determined, settled).
- 7 residual types: `W_type = true_W`, and the finite check shows `W_type` meets
  the free-set for all 7. The only thing between this and a proof is the **reverse
  implication on these 7 flats**:

> **(THE CORE) For each of the 7 residual types: the achievable cut-vector span
> containing a freeing vector implies two Kempe swaps actually free `v`.**

Equivalently: the span meeting the free-set ⇒ the meet is realized at swap-depth 2.
This single linear implication, on 7 explicit affine flats of `F_2^{10}` (dim 7–8),
is **four-color-equivalent** (it, with the proven reduction, yields the theorem).

## What was actually achieved (honest ledger)

| Step | Status |
|---|---|
| Euler → canonical order → bounded path-links | open scope caveat (≤5 ordering unproven) |
| deg-4 reducible | proven (closed form) |
| deg-5 realizable type set = 104 | proven (Jordan + Kempe separation) |
| single-swap layer (97 types) | proven type-local + linear (`F_2` feasibility) |
| swaps = `F_2^2` additions; `S_4 = AGL(2,2)` | proven |
| freeing = cut-vector span meets free-set | verified exact (0/67,550) |
| a fixed flat per type decides freeing | verified exact (0/90,929); 104/104 finite check |
| `true_W ⊆ W_type`; forward implication | **proven** (containment) |
| `W_type = true_W` on the 7 residual types | verified (0% slack) |
| **(THE CORE) reverse implication on 7 flats** | open; **four-color-equivalent** |

We did not beat four-color. We **located all of its remaining difficulty** in one
linear-algebra implication on seven explicit flats, proved everything around it,
and gave the colors–as–vectors / swaps–as–translations (`AGL(2,2)`) picture that
makes the statement clean. That is "four-color in human focus": a single, sharp,
surveyable question for graph theory and representation theory — *do the seven
residual type-flats realize their freedom?*
