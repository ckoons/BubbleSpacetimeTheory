---
title: "The TRIPLE LEMMA — statement in stone, the wall-distance metric pinned (two options, Cal picks one, before any check), the letter-context spec for Elie's enumeration, and the local-decidability question that decides whether the check fits an afternoon"
author: "Lyra"
date: "2026-08-31, Monday (clock-verified 07:48 EDT at round start)"
status: "ROUND 17, ACT ONE. The last deep piece of Gate Existence, specced so the enumeration can start today and tomorrow starts mid-stride if it can't finish. Cal gates the metric and the context semantics before anything runs. Nothing banks."
---

# THE TRIPLE LEMMA

## 1. Statement (in stone, one-letter dynamics per J3)

**Triple Lemma (target).** At every stuck insertion configuration (τ = 6 at a deg-5 hole in
G−v, unpinned), some TRIPLE — the alphabet's one letter: a three-vertex pure-curl patch
re-signing, realizable as a bounded Kempe composite — applies with its patch within bounded
radius of the hole's link, and its application STRICTLY REDUCES the wall-distance to the freed
set. Iterating: Gate Existence, with descent, by one letter.

## 2. The metric, pinned BEFORE any check (Cal picks; single pre-registration)

- **Option M1 (Hamming-to-freed):** d(f) := min over freed f* of #{v : f(v) ≠ f*(v)}. Simple,
  cheap, blunt (ignores wall geometry).
- **Option M2 (interface length):** d(f) := min over freed f* of the wall graph's edge count in
  𝒲(f, f*). Truer to the wall picture (the lemma is ABOUT wall motion), slightly costlier.
My recommendation: M2 primary, M1 logged alongside as a free diagnostic; but the pick is Cal's
and it freezes before the first context is scored. A lemma that gets to choose its metric after
seeing the data is not a lemma.

## 3. The context spec (what Elie enumerates)

A CONTEXT is the data that determines whether a given triple applies and what it does locally:
1. The radius-2 colored pattern around the hole (the link 5-ring + second ring), up to the
   color symmetry group and the dihedral symmetry of the hole.
2. **The chain-crossing type at the patch boundary:** the partition data of how each relevant
   pair's chains enter/exit the radius-2 ball (which boundary arcs are chain-connected
   outside). This is the part that makes the check honest — see Section 4.
Empirical phase first (today-sized): for every stored stuck case (739 + tranche), log (pattern,
crossing-type, which triple fired, Δd under M1 and M2). This yields the REALIZED context list
and tests strict descent on everything we hold. Exhaustive phase (the theorem check): enumerate
abstract contexts (pattern × crossing-type), verify per context that some triple applies and
descends; a soundness argument that the context classification is COMPLETE (every possible
stuck configuration falls in an enumerated class) then converts the finite check into the
lemma. That soundness argument is mine to write, not Elie's to compute.

## 4. The local-decidability question (the honest hinge, stated before it bites)

A triple is a NET effect; its availability as a composite depends a priori on chain structure
that may leave any bounded ball. If availability is determined by the radius-2 pattern PLUS the
boundary crossing-type — a finite datum — the check is finite and the lemma is provable by
enumeration. If some stored gate's availability provably depended on structure beyond the
crossing-type classification, the context space must grow by exactly the discovered dependency.
**Elie's cheapest decisive glance: for each stored gate word, did the realizing composite's
chains exit radius 2, and when they did, is the (pattern, crossing-type) pair still a function
of success?** Same-context-different-outcome pairs are the kill; their absence at scale is the
license for the exhaustive phase. Pre-registered both ways.

## 5. Sizing (per the routing's instruction)

The empirical phase and the decisive glance fit the afternoon. The exhaustive phase almost
certainly does not (the crossing-type enumeration wants care, and my completeness argument
wants a fresh morning). Filed accordingly: today ends with the realized-context table and the
decidability verdict; tomorrow starts mid-stride at the completeness argument — the last deep
piece of Gate Existence, with its shape already drawn.

— Lyra. One letter, one metric, one honest hinge; if the contexts close, the 739 miracles
become a theorem by counting — which is how this program has preferred its miracles all along.
