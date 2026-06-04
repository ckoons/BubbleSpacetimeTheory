---
title: "Decomposition of the Residual Kernel (R): 7 Types, 4 Ring-Orbits, and a Representation-Theory Bridge"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "DECOMPOSITION (verified) + stated open puzzle. (R) -- the four-color-hard core of the path reduction -- reduces to <=2-swap reducibility of exactly 7 explicit canonical types (4 reflection orbits), seed-independent. Each is robustly 2-swap-freeable on sampled instances; the obligation is non-emptiness of a freeing 2-swap for ALL instances of these 7. A representation-theory route (F_4 additions / Temperley-Lieb at Q=4 / Penrose su(2) spin-network recoupling) is proposed as the candidate closed-form substitute, clearly labeled conjectural."
related: ["notes/FourColor_Path_Reduction_Paper.md","notes/FourColor_Locality_Status.md","notes/FourColor_Ring_Operations_And_Hardness.md","play/fourcolor_R_seven_types.py","Penrose binor / spin networks","Temperley-Lieb algebra TL_n at delta=2","Tait 3-edge-coloring"]
---

# (R) decomposes to seven types

Single-swap freeability is a function of the local type (Lemma B,
`FourColor_Locality_Status.md`). So the 104 canonical path-deg-5 types split into
**single-swap-freeable (settled)** and **two-swap-only (the residual of (R))**.
Measured, seed-independently:

> **97 single-swap / 7 two-swap-only.** (Toy `play/fourcolor_R_seven_types.py`, 7/7.)

The residual of the entire four-color-hard core is **seven explicit types**,
folding under path-reflection to **four ring-orbits**:

| # | coloring `c0..c4` | doubled @ | long chords | spanning `(0,4)` |
|---|---|---|---|---|
| 1 | `0 1 0 2 3` | {0,2} | (0,4),(1,3),(1,4) | yes |
| 1' | `0 1 2 3 2` | {2,4} | (0,3),(0,4),(1,3) | yes |
| 2 | `0 1 2 0 3` | {0,3} | (1,4),(2,4) | no |
| 2' | `0 1 2 3 1` | {1,4} | (0,2),(0,3) | no |
| 3 | `0 1 2 0 3` | {0,3} | (0,4),(1,4),(2,4) | yes |
| 3' | `0 1 2 3 1` | {1,4} | (0,2),(0,3),(0,4) | yes |
| 4 | `0 1 2 1 3` | {1,3} | (0,2),(0,4),(2,4) | yes (refl-self) |

Orbits: {1,1'}, {2,2'}, {3,3'}, {4}. **5 of the 7 carry the spanning chord**
`(0,4)` — the same "key" that controlled completeness. Each of the 7 is **richly
co-chained** (2-3 long chords) and **robustly 2-swap-freeable** (each sampled
instance had 2-6 distinct working 2-swaps). So fragility is not the issue; the
obligation is:

> **(R) ≡ for each of the 7 types, EVERY instance admits at least one freeing
> 2-swap** (the freeing recipe is not type-determined — it varies with hidden
> interior structure — but is conjecturally never empty).

This is the four-color theorem, localized to seven rigid configurations. It is the
small, human-surveyable verification set we sought — and a clean puzzle for graph
theory.

## The 2-swap as two ring additions sharing a pivot

Swaps are `F_4 = Z2 x Z2` additions (`FourColor_Ring_Operations_And_Hardness.md`):
a swap adds a nonzero `g = a⊕b` to a connected component. A freeing 2-swap is
`g1` then `g2` with **`{a,b} ∩ {c,d} ≠ ∅`** — the two pairs **share a color**
(complementary pairs provably never suffice). Write the shared color as the
**pivot** `b`: swap 1 is `(a,b)` (adds `a⊕b`), swap 2 is `(b,c)` (adds `b⊕c`). The
pivot is exactly the doubled color in the cases observed. So each residual type's
freeing is a *pivoted pair of `F_4`-additions*.

## Representation-theory bridge (the candidate closed-form substitute)

This is the direction Casey flagged — *find a parallel operation, perhaps solvable
in closed form, that substitutes for the double-swap*. The pointers are concrete
and the structure is suggestive, but **this section is a research program, not a
result.**

1. **4-colorings are a tensor invariant.** By Tait, proper 4-colorings of a planar
   triangulation correspond to proper 3-edge-colorings of its cubic planar dual.
   By **Penrose's binor calculus**, the *number* of proper 3-edge-colorings of a
   planar cubic graph equals an `su(2)/SO(3)` **spin-network evaluation** — a
   closed-form tensor contraction. Equivalently, the chromatic structure at `Q=4`
   lives in the **Temperley-Lieb algebra `TL_n` at loop value `δ = √Q = 2`**
   (the Jones-Wenzl / `SO(3)` point).

2. **Swaps ↔ recoupling.** A pivoted pair of `F_4`-additions (swap 2 sharing the
   pivot color of swap 1) is, in the spin-network picture, a **change of coupling
   basis at the shared index — a `6j`-recoupling move.** The conjecture: the
   ≤2-swap reducibility of a residual type is equivalent to a **non-vanishing /
   recoupling identity** at the pivot, in `TL_5` (the 5-path) at `δ = 2`.

3. **Why this could close in closed form.** If the seven types' reducibility is a
   recoupling identity in `TL_5`, it is an algebraic statement about a
   finite-dimensional algebra at a fixed parameter — the kind that *does* admit
   closed-form evaluation (Jones-Wenzl projectors, `6j`-symbols at `δ=2` are
   explicit). The four-color-hardness would then be concentrated in whether the
   relevant `TL_5`/spin-network quantity is nonzero on these seven inputs — a
   sharp, finite, representation-theoretic question.

**Honest status of the bridge.** (1) is classical and rigorous (Penrose; Tait).
(2)–(3) are *conjectural correspondences* we have not verified: we have not
exhibited the `TL_5` element of a co-chaining type, nor shown the double-swap is
the `6j` move, nor that reducibility = non-vanishing. The value of stating it is
to point the residual (R) at the algebra where a closed-form substitute could
live, and to give representation theory a precise target: **express the 7 residual
co-chaining types as `TL_5` (`δ=2`) elements and decide ≤2-swap reducibility as a
recoupling non-vanishing.**

## Where this leaves the program

| Layer | Status |
|---|---|
| deg-4 | proven (closed form) |
| deg-5 type set + completeness | proven (modulo classical Kempe separation) |
| single-swap locality | proven |
| **(R) residual** | **7 types / 4 ring-orbits**, verified 2-swap, *non-emptiness for all instances* open |
| `≤5` path-elimination ordering | open (caveat, `Ring_Operations` note) |
| rep-theory closed-form substitute | proposed program (Penrose / `TL_5` at `δ=2` / `6j`) |

(R) is four-color-equivalent, so proving it is proving four-color — but it is now
**seven rigid, ring-structured configurations** with an algebraic target, which is
exactly "four-color in human focus."
