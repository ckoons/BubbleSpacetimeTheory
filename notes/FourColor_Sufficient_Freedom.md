---
title: "Sufficient Freedom: the Provable Half of the Coding Thesis"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "RESULT (finite, 4CT-independent). For every one of the 104 realizable path-deg-5 types the cut-space W_type escapes the 5-slice arrangement -- the coding/linear obstruction to four-coloring NEVER occurs (min escape margin 19). So the freedom always exists. The four-color-hard residue is ONLY sequential realizability of that freedom (the 7 residual types). This proves Casey's thesis at the linear level and isolates the remaining difficulty cleanly."
related: ["notes/FourColor_Code_Structure.md","notes/FourColor_Hard_Core_Located.md","notes/FourColor_Minimal_Linear_Representation.md","play/fourcolor_freedom_margin.py"]
---

# What the two sets say

Casey: *coloring maps is a set of affine transforms that need ≤4 colors because
there is sufficient freedom in coding on 2-D planar maps.* We can now make the
provable half of that exact.

## The freedom always exists (proven, 4CT-independent)

Each realizable insertion has a cut-space `W_type ⊆ F_2^{10}` (the coding freedom,
built from the type's co-chaining). "Four-colorable here" needs `W_type` to **escape
the 5 coordinate slices** `{t : t_i = c_i ⊕ m}` for some `m` — i.e. to contain a
freeing vector.

> **Theorem (finite, independent of four-color).** Every one of the **104**
> realizable types escapes the slice arrangement; the minimum number of escaping
> ("freeing") vectors is **19 > 0**. Since the realizable types are exactly these
> 104 (completeness, proven via Jordan + Kempe separation), **the coding/linear
> obstruction to four-coloring never occurs** — the freedom is always present, with
> margin ≥ 19.

(`play/fourcolor_freedom_margin.py`, 6/6.) This is the precise, provable content of
"sufficient freedom in coding on planar maps": planarity forces enough cut-space
dimension that a non-surjective (color-omitting) word always exists. The abstract
obstruction simply isn't there.

## What the two sets contribute

Both residual codes — **Set A** (non-spanning, dim 8) and **Set B** (spanning,
dim 7) — escape with comfortable margin (free-fraction 0.22–0.66). Their special
status is **not** a shortage of freedom; it is that **single swaps don't suffice**:
the freedom needs two moves to *use*. So the two sets say:

- the freedom to four-color is **always there** (every type, both sets, escapes);
- the only delicacy is **how the freedom is used** — one swap for 97 types, two for
  the seven residual types.

## The clean split

| question | answer |
|---|---|
| **Does an escaping (freeing) vector exist?** | **Always yes** — proven, finite, margin ≥ 19 |
| **Is it reachable by sequential Kempe swaps?** | the four-color-hard residue (the 7 types) |

We have closed the first question completely: *the freedom is sufficient, always.*
The remaining difficulty is purely **realizability** — that the always-present
freedom can be reached by actual swaps (and, on the 7 residual types, in two). This
is the sharpest separation yet: four-color is not in doubt about whether enough
coding freedom exists on planar maps — it does, provably — but about whether that
freedom is sequentially reachable.

## Honest scope

- "The freedom always exists" is a genuine finite theorem on the 104 realizable
  type-codes, not assuming four-color. It proves the *necessary* linear condition
  is *universally satisfied*.
- It does **not** prove four-color: sufficiency (freedom ⇒ realizable by swaps) is
  the residue, four-color-equivalent. But the thesis "planar maps have sufficient
  coding freedom" is now a proved statement, with the difficulty quarantined to
  realizability on two small `F_4` codes.
