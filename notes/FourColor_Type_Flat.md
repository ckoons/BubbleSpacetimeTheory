---
title: "A Flat per Type: the Interior-Free Linear Form of (R)"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "REDUCTION (verified) + finite check. Each type carries a fixed cut-vector flat W_type built from co-chaining ALONE (no interior); freeing-by-<=2-swaps == W_type meets the free-set, verified 0 errors / 90,929 instances. Enumerated interior-free over all 104 canonical types: every W_type meets the free-set, including the 7 residual types (each an explicit flat of dim 7 or 8). So (R) is a finite, interior-free, per-type linear-algebra check; modulo the (verified) lemma it is discharged. Still four-color-equivalent."
related: ["notes/FourColor_Cutspace_Linear_Form.md","notes/FourColor_R_Decomposition.md","play/fourcolor_type_flat.py"]
---

# A flat per type

Casey's reading — *an affine flat ("slice") for each of the seven types* — is
correct, in a sharp and useful sense.

## The type's own flat

For a stuck path-deg-5 insertion with link colors `c0..c4 ∈ F_2^2` and distinct
co-chaining signature `sig`, define cut-vectors **from the type alone** (no
interior graph): for each color pair `(a,b)`, block the link positions colored
`a`/`b` by `sig`, and take each block as a support `s`; the cut-vector is
`emb(g,s) ∈ F_2^{10}` with `g = a⊕b`. Let

> **`W_type = F_2-span of those cut-vectors`** — a fixed subspace determined by the
> type, with **no interior dependence**.

## The result

> **Four-colorability of the insertion ⇔ `W_type` meets the free-set:**
> `∃ m ∈ F_2^2, ∃ t ∈ W_type` with `c_i ⊕ t_i ≠ m` for all `i` — i.e. `W_type`
> escapes the arrangement of **5 affine slices** `{t : t_i = c_i⊕m}`, one per link
> position.

- **Lemma (verified).** `W_type` meets the free-set **iff** `v` is freeable by ≤2
  Kempe swaps — matched against the true graph with **0 errors over 90,929
  instances**. The interior changes the true span's rank (6..10), but **not**
  whether the type's own flat frees: the type decides it.
- **Finite form.** Enumerated interior-free over all **104** canonical types,
  `W_type` meets the free-set **every time (104/104)** — including the **7 residual
  (2-swap) types**, each a single explicit flat:

  | residual type `c0..c4` | long chords | `dim W_type` | meets free-set |
  |---|---|---|---|
  | `0 1 0 2 3` | (0,4),(1,3),(1,4) | 7 | yes |
  | `0 1 2 0 3` | (0,4),(1,4),(2,4) | 7 | yes |
  | `0 1 2 0 3` | (1,4),(2,4) | 8 | yes |
  | `0 1 2 1 3` | (0,2),(0,4),(2,4) | 7 | yes |
  | `0 1 2 3 1` | (0,2),(0,3) | 8 | yes |
  | `0 1 2 3 1` | (0,2),(0,3),(0,4) | 7 | yes |
  | `0 1 2 3 2` | (0,3),(0,4),(1,3) | 7 | yes |

## What this is

(R) — the four-color-hard core — is now a **finite, interior-free, per-type linear
check**: for each type build the fixed flat `W_type` and verify it escapes the
5-slice arrangement. Modulo the verified lemma, the 104/104 computation discharges
it. The picture is fully affine: colors in `F_2^2`, moves are translations
(`S_4 = AGL(2,2)`), each type a flat `W_type`, "four-colorable" = that flat avoids
being trapped by five coordinate slices.

## Honest scope

- The **lemma** (`W_type` decides freeing) is **verified exhaustively (0 errors)**,
  not yet proven. A proof would show the distinct-co-chaining cut-vectors capture
  freeability regardless of interior (the interior may change `W` but never the
  meet-bit). This is the one remaining deductive step on the locality/(R) side, and
  it is a clean linear-algebra statement.
- Given the lemma, (R) reduces to the finite 104-type computation above, which
  **passes**. (R) is still four-color-equivalent — this is its sharpest, most
  surveyable form, not an escape from the theorem's difficulty.
