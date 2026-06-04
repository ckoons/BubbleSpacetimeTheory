---
title: "Swaps as Ring Operations, and Where the Real Wall Is"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "FRAMING + honest hardness analysis. (1) PROVEN: Kempe swaps are F_4 additions (the 'ring' is F_4 = Z2 x Z2). (2) Clean separation of what fell vs what didn't: the realizability/characterization results (deg-4, type-set, completeness, single-swap locality) are NOT colorability-hard and fell; the residual kernel (R) (<=2-swap reducibility) IS four-color-equivalent given the reduction, so no short algebraic proof is expected. (3) Honest caveat: the reduction's 'paths <=5' bound is not justified by the stated '(Euler bound)' reason and is not yet proven."
related: ["notes/FourColor_Path_Reduction_Paper.md","notes/FourColor_Locality_Status.md","notes/FourColor_Enclosure_Law_Proof.md","play/fourcolor_ring_operations.py","Tutte F_4 tensions","Fisk geometric coloring"]
---

# Swaps are operations on the ring F_4

Take the four colors as **F_4 = Z2 x Z2 = {0,1,2,3}** with addition = **bitwise
XOR** (the Klein four-group). Then every Kempe `(a,b)`-swap on a component is
exactly **"add the fixed element `g = a⊕b` to every vertex of that component."**

- The `(a,b)`-subgraph is the set of vertices colored in the coset `a + ⟨g⟩` of
  the order-2 subgroup `⟨g⟩ = {0, g}`.
- A swap picks a nonzero `g ∈ F_4`, a connected component of that coset-subgraph,
  and adds `g` to it. Properness is preserved (adjacent colors differ ⇒ after
  adding `g` to one side of an edge they still differ).

(Verified: `play/fourcolor_ring_operations.py`, 4/4 — swap == XOR-add on the
component, additions stay proper.) This is Casey's "operations on the ring," made
literal. It is the same `F_4 / S_4` structure that runs through the rest of the
program: a proper 4-coloring is an `F_4`-tension (Tutte); color relabeling is
`S_4` acting on `F_4`; the conserved **Fisk ℤ₂ charge** is the swap-invariant; and
the realizable path-deg-5 types decomposed into clean `S_4 × reflection` orbits.

# Why some things fell and one thing didn't

The program made real, honest progress — but it is important to see *which* parts
were ever going to fall, because they share a property the residual does not.

**Fell (not colorability-hard).** These are statements about *which local
configurations exist* and *how a single swap acts locally* — realizability and
one-step locality, not "is `G` colorable":

- deg-4 reducible (closed form);
- the deg-5 type set is a finite closed-form predicate;
- **completeness** — the realizable set is exactly 104 (necessity proven via
  Jordan curve + Kempe separation);
- **single-swap locality** — whether 1 swap frees `v` is a function of the type.

None of these asserts that a coloring *exists*; they characterize the local
combinatorics of colorings that are already given. The `F_4 / S_4` ring structure
is exactly why they have clean closed forms.

**Did not fall — the residual kernel (R).** *Every stuck path-deg-5 type is
≤2-swap reducible.* This is a colorability-extension statement, and here is the
barrier, stated plainly:

> **(R), together with the reduction (Euler → bounded path-links) and the proven
> deg-4 case, implies the four-color theorem.** If every stuck insertion can be
> freed by ≤2 swaps, incremental coloring never fails, so every planar
> triangulation is 4-colorable.

Therefore **(R) is four-color-equivalent** (given the reduction): a closed-form /
human proof of (R) would *be* a closed-form human proof of four-color — the famous
problem with no known surveyable proof (Appel-Haken and Gonthier are both
machine-checked). The ring framing is the right language and it dissolved
everything that was *not* colorability — but it cannot dissolve (R), because (R)
carries the full colorability content. This is not a defect of the approach; it is
the approach correctly **localizing the entire difficulty of four-color into one
sharp ≤2-swap reducibility statement** on ~100 rigid `F_4`-orbit types.

That is the honest value: not a shortcut around four-color, but a clean
reformulation that says *exactly* what the hard core is and shows the rest is
ring-structured and tractable.

# Honest caveat on the reduction itself

Section 1 of the path-reduction paper bounds the stuck-path length by "≤ 5 (Euler
bound)." **That justification is incorrect:** Euler gives a vertex of minimum
*total* degree ≤ 5, whereas the canonical (dFPP) ordering's *back-degree* (the
stuck-path length at insertion) is a different quantity and is not bounded by
Euler. The two coincide only under an ordering that removes a boundary vertex of
current degree ≤ 5 at every step.

- Whether such an ordering always exists is **not proven here.** Experiments are
  *suggestive but inconclusive*: a greedy min-degree boundary removal never was
  *forced* above degree 5 on clean instances, but the test harness is not a
  faithful dFPP and stalled on a fraction of cases. A crude canonical-order
  computation produced a back-degree 6 once.
- **Consequence:** the claim "the reduction tiles four-color via paths ≤ 5" needs
  either (a) a proof that a ≤5 path-link elimination ordering always exists, or
  (b) extension of the deg-≤5 analysis to longer stuck paths. Until then, the
  reduction is rigorous *for boundary path-links of degree ≤ 5* (the verified
  class), and its sufficiency for general triangulations is **open**.

This caveat does not touch the proven results above (deg-4, type-set,
completeness, single-swap locality, ring structure); it bounds the scope of the
overall "candidate four-color proof" claim, which the paper now states explicitly.
