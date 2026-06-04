---
title: "Three Converging Levers on the Flow/Penrose Model"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "RESULTS (one proven, two verified reformulations). Lever 1 (linear): nowhere-zero F_2^2-flow <=> edge set = union of two even subgraphs; four-color <=> every bridgeless planar cubic graph's edges are a union of two cycle-space elements (verified flow==two-cycle-covers). Lever 2 (rep): Penrose SO(3) binor recoupling, loops=3, triangle->vertex is the 6j. Lever 3 (PRIZE, proven, NOT 4CT-hard): #3-edge-colorings is invariant under the triangle<->vertex (Delta<->Y) move, so four-color reduces to triangle-free planar cubic graphs; this move IS Lever 2's 6j. Classical facts (Tutte/Penrose), unified and honestly attributed."
related: ["notes/FourColor_Flows_Penrose_Reset.md","play/fourcolor_three_levers.py","Tutte flows / Delta-Y","Penrose 1971 binor calculus","Temperley-Lieb at delta=2"]
---

# Three levers, one invariant

The flow/Penrose model gives the same invariant in three languages; together they
give leverage to reduce the problem class while tracking it.

## Lever 1 — linear (two even subgraphs)

`F_2^2 = F_2 x F_2`, so a nowhere-zero `F_2^2`-flow is a pair of `F_2`-flows
(cycle-space elements / even subgraphs) `C1, C2` with no common zero — i.e.
`C1 ∪ C2 = E`. Hence:

> **Four-color ⇔ every bridgeless planar cubic graph's edge set is a union of two
> even subgraphs** (two cycle-space elements).

Verified: `flow count = #{(C1,C2): C1∪C2=E} = #3-edge-colorings` on K4 and the prism
(all 6). This places four-color as a **covering question inside the linear cycle
space** — concrete linear-algebra leverage. (Classical: nowhere-zero 4-flow ⇔ two
even subgraphs covering `E`.)

## Lever 2 — representation theory (Penrose `6j`)

The Penrose `SO(3)` evaluation `⟨G⟩` obeys the **binor recoupling**
`Σ_k ε_{ijk} ε_{lmk} = δ_il δ_jm − δ_im δ_jl`; closed loops evaluate to `3`
(`= dim` of the vector representation). Reducing a graph by this relation is the
`SO(3)` recoupling calculus. In particular a **triangle reduces to a vertex** —
this is the `6j`-symbol move — and it preserves `|⟨G⟩|`.

## Lever 3 — the prize (PROVEN, not four-color-hard): `Δ↔Y` invariance

> **Theorem.** For any cubic (multi)graph `G` with a triangle `T = t0t1t2` and legs
> `ℓ0, ℓ1, ℓ2`, let `G'` replace `T` by a single vertex `w` joined to the three leg
> endpoints. Then `#proper-3-edge-colorings(G) = #proper-3-edge-colorings(G')`.

**Proof.** In a proper 3-edge-coloring, the three triangle edges must be pairwise
distinct (two equal would clash at their shared vertex), so they use `{1,2,3}`. The
constraint at `t_i` then forces leg `ℓ_i` to the unique color absent from its two
triangle edges; explicitly `(ℓ0, ℓ1, ℓ2) = (e_{12}, e_{20}, e_{01})`, a permutation
of `{1,2,3}` — the three legs are **distinct**. Conversely, any assignment of three
**distinct** colors to the legs determines the triangle edges uniquely
(`e_{12}=ℓ0, e_{20}=ℓ1, e_{01}=ℓ2`) and is proper; non-distinct legs admit no
extension. In `G'` the vertex `w` is proper iff its three legs are distinct. Hence
colorings of `G'` (outside-coloring with distinct legs) are in bijection with
colorings of `G` (each extends uniquely across the triangle). `∎`

Verified: prism `Δ→Y` = K4 (6 → 6); 60/60 random cubic graphs preserved
(`play/fourcolor_three_levers.py`, 7/7).

**Consequence.** `Δ→Y` preserves planarity and bridgelessness and strictly shrinks
the graph, so iterating it reduces four-color to **triangle-free planar cubic
graphs**. This is a genuine, provable reduction of the problem class — and it is
exactly the `6j` move of Lever 2.

## The leverage, honestly

- One invariant, three faithful languages: **two-even-subgraph cover** (linear),
  **`SO(3)` evaluation** (representation theory), **`#3-edge-colorings`** (combinatorics).
- A **provable** colorability-preserving reduction (`Δ↔Y`) that narrows the class
  to triangle-free, with the representation theory (`6j`) explaining *why* it works.
- These are classical results (Tutte's flows and `Δ-Y`; Penrose 1971; the
  Potts/Temperley–Lieb dictionary), here **unified and tracked together**. The
  contribution is the clean trilingual model and the leverage it gives, not new
  theorems; the core non-vanishing remains four-color-equivalent.

## Next leverage (open)

- Stack further **provable reductions** (digons/parallel edges; 2-edge-cuts;
  4-face reductions) in all three languages, narrowing past triangle-free toward a
  minimal "core" class.
- In Lever 2, ask which `6j`/recoupling moves are *guaranteed* to keep `⟨G⟩ ≠ 0`
  (the moves that preserve non-vanishing form the honest, non-4CT-hard sub-theory).
