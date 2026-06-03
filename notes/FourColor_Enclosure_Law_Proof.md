---
title: "Necessity of the Path-deg-5 Realizability Conditions (closing completeness's upper bound)"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-03"
status: "PROOF of necessity of (2a)&(2b), modulo the classical Kempe-chain separation lemma. Establishes realizable-type-set ⊆ {predicate types} = 104, i.e. the completeness UPPER BOUND (the hard direction / 'the plateau is final'). The matching lower bound (all 104 occur) holds by exhibition. Structural lemmas (only-center-free; surrounding-chain conclusion; no equal/disjoint crossing) computer-checked, 0 violations over the realized set."
related: ["notes/FourColor_Path_Reduction_Paper.md","play/fourcolor_path_realizability_characterization.py","de Fraysseix-Pach-Pollack canonical ordering","Kempe-chain separation (classical)"]
---

# Necessity of the realizability conditions for path-deg-5 types

This note upgrades condition **(2b)** of the realizability characterization
(`notes/FourColor_Path_Reduction_Paper.md`, Sec. 5) from a *verified* law to a
*proven* one, and with it (2a), establishing the **completeness upper bound**:
the realizable path-deg-5 type set is contained in the closed-form predicate set,
which enumerates to exactly **104**. The lower bound (each of the 104 occurs) is
by exhibition. So — modulo the single classical lemma cited below — the realizable
set is exactly 104, and the empirical "hard plateau" is a theorem.

## Setup (the topology is forced by canonical ordering)

Color `G` incrementally in a de Fraysseix-Pach-Pollack canonical order. At the
step that colors a path-link degree-5 vertex `v`, the already-placed graph `H`
(`= G_k`) is an internally-triangulated 2-connected plane graph whose outer face
is a cycle `O`, and `v`'s already-colored neighbors `u0,u1,u2,u3,u4` lie on `O`
as a **contiguous arc** (the "near arc"), in this order; `v` sits in the outer
face, outside the disk `D` bounded by `O`, joined to each `u_i`. All of `H` and
all Kempe chains live in `D`. The rest of `O` (from `u4` back to `u0`) is the
"far arc."

`H` is properly 4-colored; `c_i := color(u_i)`; the path is *stuck* (4 colors on
5 vertices), so one color is doubled at a non-adjacent position pair. Write
`P = {c0, c4}` for the color-pair of the endpoints, and `Pᶜ` for the
complementary pair (the other two colors). The four **consecutive pairs**
`(0,1),(1,2),(2,3),(3,4)` are always co-chained (adjacent ⇒ a 2-vertex Kempe
component) — this is automatic, not a constraint.

We must show every *realizable* type satisfies:

- **(2a)** no two co-chained chords with **equal or disjoint** color-pairs cross;
- **(2b)** if `(0,4)` is co-chained, every interior `u_k` (`k∈{1,2,3}`) colored
  in `P` is endpoint-tied (same-pair) or complement-shielded.

## Lemma 0 (only the center can be a free `P`-vertex)

Suppose `(0,4)` is co-chained and `u_k` (`k∈{1,2,3}`) has color in `P`.

- `k=1`: `u1` is adjacent to `u0` (consecutive). If `c1=c0` they'd share a color
  on an edge — impossible. So `c1=c4`, whence edge `(0,1)` has colors
  `{c0,c4}=P`: a `P`-edge, so `u1` is `P`-co-chained to `u0` — **endpoint-tied**.
- `k=3`: symmetric, `c3=c0`, edge `(3,4)` is a `P`-edge, `u3` tied to `u4`.
- `k=2`: `u2`'s consecutive edges are `(1,2)` and `(2,3)`, whose color-pairs need
  not equal `P`; so `u2` can be a **free** `P`-vertex.

Hence the only possible free interior `P`-vertex is the **center `u2`**.
(Computer-checked: 0 violations over all 936 realized `(0,4)`-co-chained
instances; `play` support script.) ∎

## (2a) necessity (planarity of Kempe chains)

Two co-chained chords `(i,j)` and `(k,l)` with `i<k<j<l`. If their color-pairs
are **disjoint**, the two chains are vertex-disjoint subgraphs of `H`; drawn in
the disk with endpoints interleaved on `O`, by the Jordan curve theorem they must
intersect — contradiction. If their color-pairs are **equal**, co-chaining is an
equivalence relation, so interleaved co-chained pairs force `i,j,k,l` into one
component, i.e. `(i,k)` etc. are *also* co-chained — there is no "crossing of two
distinct chords," only a single component (not the forbidden pattern). Either way
the forbidden configuration cannot occur. (Computer-checked: 0 crossing
equal/disjoint pairs over the realized set.) ∎

## (2b) necessity (Jordan curve + Kempe separation)

Assume `(0,4)` co-chained and, by Lemma 0, let the center `u2` be a free
`P`-vertex (else nothing to prove). Let `χ` be the `(c0,c4)`-component containing
`u0,u4`, and `χ'` the `(c0,c4)`-component containing `u2`; by hypothesis `χ≠χ'`.

**The Jordan curve.** The chain `χ` runs from `u0` to `u4` inside `D`. Together
with the two outer edges `v–u0` and `u4–v` it forms a closed curve `J`. The four
triangles `v–u_i–u_{i+1}` lie between `v` and the near arc, so `J` encloses a
region whose closure contains the near-arc vertices `u1,u2,u3`; in particular the
free vertex `u2` lies **strictly inside `J`** (it is not on `χ`). The far arc lies
**outside `J`**.

**Confinement of `χ'`.** `χ'` is vertex-disjoint from `χ` (distinct components of
the same 2-color subgraph) and contains neither `u0` nor `u4` (those are in `χ`)
nor `v` (∉`H`). It cannot meet `J`: it cannot touch `χ` (color-class component
boundary), and it cannot cross the edges `v–u0,v–u4` (those are outside `D`, `χ'`
is inside). Since `u2∈χ'` is inside `J`, **all of `χ'` is strictly inside `J`**,
confined to the region `Ω` bounded by `χ` and the near arc.

**The separating complementary chain.** Apply the classical **Kempe-chain
separation lemma**: in an internally triangulated plane graph, the vertices
adjacent to a connected `(c0,c4)`-component `χ'`, and colored in the complementary
pair `Pᶜ`, contain a connected `Pᶜ`-subgraph `ψ` that *separates* `χ'` from the
rest of the graph. Because `χ'` reaches the boundary of region `Ω` only along the
near arc (at `u2`, and possibly other near-arc `P`-vertices), `ψ` is an arc whose
two ends lie on the boundary of `Ω`. That boundary is `χ ∪ (near arc)`. The ends
of `ψ` are colored in `Pᶜ`, while `χ` is colored in `P` (disjoint) — so neither
end lies on `χ`. **Both ends lie on the near arc.** The near-arc vertices colored
in `Pᶜ` are among `{u1,u2,u3}` (since `u0,u4` are colored in `P`), and to separate
`u2` from `u0` and `u4` the arc `ψ` must reach the near arc on **both sides** of
`u2`. Hence `ψ` connects `u1` and `u3` (the only `Pᶜ`-positions flanking the
center): the chord `(1,3)` is co-chained and `1<2<3` — a **complementary-pair
chord enclosing `k=2`**. This is exactly the shield required by (2b).
(Computer-checked: in all 936 realized `(0,4)`-co-chained instances with `u2`
free, `(1,3)` is co-chained — the surrounding-chain conclusion — 0 violations.) ∎

## Consequence: completeness upper bound

Every realizable type satisfies (2a)&(2b) (and the forced base). The abstract
enumeration of long-chord sets satisfying (2a)&(2b) yields exactly **2,496 raw =
24·104 canonical** types. Therefore:

> **The realizable path-deg-5 type set has at most 104 canonical members.**

This is the hard direction of completeness — the proof that *no further type can
ever appear* in any larger triangulation, which the empirical 1.5M-instance
plateau could only suggest. The matching lower bound (all 104 are realizable)
holds by exhibition: each of the 104 was realized by an explicit planar
triangulation in the verification. Hence the realizable set is **exactly 104**.

## Honest scope

- The proof rests on **one** external ingredient, the classical **Kempe-chain
  separation lemma** (a connected two-color component in an internally
  triangulated plane graph is separated from the rest by a connected chain in the
  complementary two colors). This is standard in the four-color literature; we
  invoke rather than re-derive it, and we have computer-verified the specific
  topological conclusion it yields here (the `(1,3)` shield) on the entire
  realized sample with zero exceptions.
- This closes **completeness** (the type-set count). It does **not** address
  **locality** of double-swap reducibility, which remains the other standard
  obligation (`FourColor_Path_Reduction_Paper.md`, Sec. 5.2).
- Four-color is already a theorem (Appel-Haken; Gonthier). The contribution here
  is that *this particular reduction's* completeness obligation is now proven
  (modulo a classical lemma), leaving only locality between the reduction and a
  self-contained proof on ~100 rigid path-types.
