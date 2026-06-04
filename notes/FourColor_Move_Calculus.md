---
title: "The Non-Vanishing Move Calculus: Scaling Moves vs the Binor"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "RESULT (computed/verified) + sharp localization. The Penrose SO(3) skein moves split cleanly: SCALING moves (loop x3, bubble x2, theta x6, triangle->Y/6j x(-1), small-cut factorizations) are all non-vanishing-preserving (multiply <G> by a nonzero/unit factor) and are exactly the reductions that narrow a planar cubic graph to its core; the BINOR move H = I - swap is the unique EXPANDING move (a minus sign) and the sole source of cancellation. On a core graph (cube witness) no scaling move applies. Four-color <=> on every core graph the accumulated binor sign-sum is nonzero. Classical skein theory (Penrose/Kauffman); the contribution is the explicit non-vanishing classification."
related: ["notes/FourColor_Narrowed_Core.md","notes/FourColor_Three_Levers.md","notes/FourColor_Flows_Penrose_Reset.md","play/fourcolor_move_calculus.py"]
---

# The move calculus

For the Penrose `SO(3)` evaluation `⟨G⟩` (vertex = Levi-Civita `ε`, loop = 3), every
local move is one of two kinds. The split is exact and it pins the four-color content.

## Scaling moves — provably non-vanishing-preserving

Each multiplies `⟨G⟩` by a **nonzero constant** (computed values):

| move | coefficient | effect |
|---|---|---|
| loop | `3` | `⟨G⟩ → 3·⟨G∖loop⟩` |
| bubble (2 parallel edges) | `2·δ` | `×2` |
| theta (3 parallel edges) | `6` | closed value |
| **triangle → vertex** (`6j`) | `−1·ε` | `×(−1)`; this is `Δ→Y` (`|⟨G⟩|` invariant) |
| `k`-edge-cut (`k≤3`) | product / `÷3` | factorize across the cut |

All are multiplicative by a positive or unit factor, so they **cannot create or
destroy a zero**: applying any of them keeps `⟨G⟩ ≠ 0` iff it was. These are exactly
the narrowing reductions R1–R4 (`Narrowed_Core`).

## The binor — the unique expanding move

`Σ_k ε_{ijk} ε_{lmk} = δ_{il}δ_{jm} − δ_{im}δ_{jl}` (verified): an internal edge
between two vertices (`H`) rewrites as `I − (swap)`. This is the **only** move with a
**minus sign**, hence the **only** source of cancellation. Every other relation in
the calculus is positive scaling.

## The boundary is exactly the core

> **The scaling moves reduce any planar cubic graph precisely to its core**
> (simple, triangle-free, cyclically-4-edge-connected). On a core graph **no scaling
> move applies** — only the binor remains.

Witness (verified, `play/fourcolor_move_calculus.py`, 7/7): the **cube** is
triangle-free, simple, has no `≤3`-edge-cut — no scaling move fires — yet `#col = 24
> 0`. So its non-vanishing is carried entirely by binor terms whose `(I − swap)`
signs **fail to cancel**. (The dodecahedron is the girth-5 analogue.)

## The sharp statement

> **Four-color ⇔ on every core graph, the accumulated binor `(I − swap)` sign-sum is
> nonzero.**

- The **scaling calculus is the honest, non-four-color-hard sub-theory**: fully
  computed, every move provably non-vanishing-preserving, and it disposes of
  everything outside the core.
- The **binor minus sign is the entire four-color content**: the question is purely
  whether signed cancellation can drive `⟨G⟩` to `0` on a core graph. By Penrose
  (planar) `⟨G⟩ = ±#3-edge-colorings`, so the sign-sum is in fact a count and never
  cancels to zero — but *proving* that non-cancellation directly is four-color
  itself.

## Honest scope

- The skein relations (loop `=3`, bubble `=2`, theta `=6`, `6j`, binor) are
  classical (Penrose 1971; Kauffman; the `SO(3)`/Temperley–Lieb calculus). What is
  made explicit here is the **non-vanishing classification**: scaling vs expanding,
  and that the scaling moves stall exactly at the narrowed core.
- This does not prove four-color. It **localizes** the difficulty to a single,
  precisely-stated phenomenon — binor-sign cancellation on core graphs — with
  everything else (the scaling calculus and the narrowing) proven and verified.
