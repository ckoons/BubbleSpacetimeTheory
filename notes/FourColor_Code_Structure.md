---
title: "The Residual Core as a Tiny Code: Even-Parity Duals, a Terminal, and Swaps"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "STRUCTURE (verified). The 7 residual type-flats are a coding-theory object Casey identified by eye: each W_type is swap-generated, contains the all-ones TERMINAL, has an even-weight dual (all parity checks even) and an even-subcode of codimension 1 with a thin set of weight-1 'single' codewords. The 7 collapse to 2 weight classes over F_4 (3 binary). Freeing = the affine code c+W_type contains a symbol-omitting word. Honest: a minimal coding re-description; the realizability implication remains four-color-equivalent."
related: ["notes/FourColor_Minimal_Linear_Representation.md","notes/FourColor_Hard_Core_Located.md","play/fourcolor_code_structure.py","even-weight (parity) codes","F_4 codes of length 5"]
---

# The residual core is a tiny code

Casey, reading the seven flats: *"all even parity except one single 1 in each set;
all point to swaps, and a terminal."* Verified — that is exactly the structure.

## The F_4 reformulation

Substitute the final coloring `u = c ⊕ w`. Then freeing becomes pure coding: with
`A = c ⊕ W_type` an affine `F_2`-code in `F_4^5` (length 5 over the alphabet
`F_4 = F_2^2`),

> **`v` is freeable ⇔ `A` contains a word that OMITS a symbol** (a non-surjective
> word). "Stuck" = `c` itself uses all four symbols.

## The signature (each of the 7 `W_type`)

| feature | value |
|---|---|
| generators | **swaps** (cut-vectors of single Kempe moves) |
| **terminal** `(1,…,1) ∈ W` | **yes, all 7** — the global `F_4` relabel by 3 |
| even-weight subcode | **codimension 1** (even parity + one odd generator) |
| **dual code** | **all even weight** — `{0,4,6,8}` (dim-7) / `{0,4}` (dim-8) |
| weight-1 "single" codewords | 1 (R1,R6,R7), 2 (R3,R4), 4 (R2,R5) |

So each `W_type` is a swap-generated code whose parity checks are all even, which
contains the all-ones terminal, sitting one odd generator above its even subcode,
with a thin set of single-coordinate ("single 1") directions. (Toy
`play/fourcolor_code_structure.py`, 7/7.)

## The collapse

The seven residual types are not seven different problems. They collapse to

> **2 weight classes over `F_4`** — `{R1,R3,R4,R6,R7}` (dim 7) and `{R2,R5}`
> (dim 8) — refining to **3 binary classes** `{R1,R6,R7}`, `{R3,R4}`, `{R2,R5}`.

The residual of four-color (via this reduction) is, up to equivalence, **two or
three small `F_4` codes of length 5**, each carrying the even-dual / terminal /
swap-generated signature above.

## The two sets (Casey's through-line)

The two `F_4` classes are not arbitrary — they are split by the **spanning chord
`(0,4)`**, the same "key" that governed completeness and the enclosure law:

| set | code | residual types | spanning `(0,4)`? |
|---|---|---|---|
| **Set A** | dim 8, `|W|=256`, 168 omitting words | `R2, R5` | **no** |
| **Set B** | dim 7, `|W|=128`, 76 omitting words | `R1,R3,R4,R6,R7` | **yes** |

These are *the two sets* that ran through the whole arc — first as the two escape
mechanisms of the enclosure law (same-pair tie vs complement shield, the two blocks
of an `F_4` partition), then as the reflection-paired geometries, and now as the
two residual codes: **the non-spanning code (Set A) and the spanning code (Set B)**
— "different but very similar behavior," exactly as predicted. The spanning chord
is what raises Set B's freedom (smaller `W`, fewer omitting words) versus Set A.

## Honest scope

- This is a **minimal coding re-description** of the residual, and it is the
  structure Casey spotted directly from the bases. It makes the object as small
  and recognizable as it gets: a handful of length-5 `F_4` codes.
- It does **not**, by itself, settle the four-color-equivalent core. The hard
  implication is now phrased in coding terms: *do these swap-generated codes
  realize their symbol-omitting freedom by ≤2 actual Kempe swaps?* The codes
  **contain** a symbol-omitting word (the meet, computed); whether that word is
  reachable by sequential swaps (not merely present in the span) is the residue.
- The terminal `(1,…,1)` is the global relabel — a "do-nothing for freeing"
  absorbing direction; the freeing lives in the swap directions modulo the
  terminal. That quotient (`W_type / ⟨terminal⟩`) on these 2–3 codes is the
  sharpest place to look for whether the freedom is forced.
