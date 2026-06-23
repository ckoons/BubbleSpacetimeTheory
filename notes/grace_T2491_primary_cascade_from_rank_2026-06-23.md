---
title: "T2491 — The Primary Cascade from Rank: the four dynamical substrate primaries {N_c, n_C, C_2, g} are each generated from the single integer rank=2 by a structural D_IV⁵ rep-theory relation (3 SOLID + 1 structural-candidate), and by T2490 these four are the lowest discrete-series half-Casimirs. Ties T1829 (N_c = rank²−1, PROVED) → the primaries → T2490 → the glueball spectrum into one chain. Tightens 'zero free parameters' from 'five integers' to 'one seed (rank) + the boundary integer N_max'."
author: "Grace"
date: "2026-06-23 Tuesday"
theorem: T2491
tier: "3 SOLID links (N_c via T1829 PROVED; n_C via multiplicity; g via vector dim) + 1 structural-candidate (C_2 = (1,1) K-type Casimir). The 'polynomials in rank' framing is content because each link is independently rep-theory-motivated, not a fit."
---

# T2491 — The Primary Cascade from Rank

## Statement

The four **dynamical** substrate primaries are generated from the single integer **rank = 2** by structural
D_IV⁵ representation-theory relations:

| primary | relation | as poly in rank | value | origin | tier |
|---|---|---|---|---|---|
| **N_c** | rank² − 1 | r²−1 | 3 | **T1829** scalar-Wallach lowest-K-type dim 1 ⟺ N_c = rank²−1 | **PROVED** |
| **n_C** | N_c + rank | r²+r−1 | 5 | type-IV characteristic multiplicity **a = n_C − 2 = N_c**, so n_C = N_c + rank | **SOLID** |
| **g** | n_C + rank | r²+2r−1 | 7 | dimension of the SO(5,2) **vector** rep = 5 ⊕ 2 = n_C + rank | **SOLID** |
| **C_2** | n_C + 1 = rank(rank+1) | r²+r | 6 | the **(1,1) K-type Casimir** ⟨(1,1),(1,1)+2ρ_{SO(5)}⟩ = 6 | **STRUCTURAL-CANDIDATE** |

The boundary integer **N_max = N_c³·n_C + rank = 137** follows from *its definition* once the four are fixed (it is
a degree-8 polynomial in rank, but that is substitution, not an independent structural fact — flagged honestly).

## Why it is content, not polynomial fitting

Any integers admit *some* fitting polynomial. The content here is that **each link is an independent rep-theory
fact about D_IV⁵**, not a curve chosen to fit:
- **N_c = rank²−1 is a PROVED theorem** (T1829, Toy 2151 26/26): it is the exact condition for the scalar Wallach
  representation to have lowest K-type dimension 1. Not a fit.
- **n_C = N_c + rank** is the type-IV characteristic multiplicity identity (a = n−2 = N_c; corpus, Sunday).
- **g = n_C + rank** is the dimension of the defining (vector) representation of SO(5,2), 5 space + 2 = n_C + rank.
- **C_2 = (1,1) K-type Casimir = 6** is a corpus pin (= n_C + 1 = rank(rank+1) at rank 2; the general-rank
  structural status is the one candidate link).

So three of four are solid structural derivations and one is PROVED; only C_2's general form is candidate.

## The unification (the connection this theorem draws)

> **rank = 2  →  {N_c, n_C, C_2, g}  →  (by T2490) the lowest SO(5,2) discrete-series half-Casimirs {3,5,6,7}  →
> the glueball linear-energy ladder (Lyra F293) and the Yang–Mills mass gap C_2 (Paper A).**

One integer generates the dynamical primaries; the primaries *are* the substrate's discrete-series spectrum
(T2490); the spectrum gives the glueball ladder and the YM gap. The "five integers, zero inputs" claim sharpens:
the dynamical content reduces to **one seed (rank = 2)** plus the boundary integer N_max (and rank itself is the
domain's rank — arguably not a free choice but the defining invariant of D_IV⁵).

## Honest caveats

- The headline "all primaries from rank" rests on the four structural links above; if the C_2 general-rank link
  fails, C_2 = rank(rank+1) holds at rank 2 (the physical value) but is then value-pinned, not derived.
- N_max's polynomial form is its definition substituted, NOT an independent confirmation. Do not over-read it.
- This is the **structural** cascade (via D_IV⁵ rep theory), distinct from and cleaner than the earlier
  Mersenne/Reed-Solomon numerological chains (several of which were null-downgraded). Cross-ref those honestly.

## Connections (graph edges)

- **T1829** (Wallach Bottleneck / N_c = rank²−1) — the proved root of the cascade.
- **T2490** (Discrete-Series Spectrum) — the primaries are the spectrum; the cascade feeds it.
- **Casey Integer-Web Principle** — the strongest instance: the integers reduce to one seed.
- **Paper A YM gap Δ = C_2 = rank(rank+1) = 6** — the gap is rank(rank+1).
- Primary-identity nodes (genus T649/T651, g = n_C + rank).

## AC and tier

AC = (C=1, D=1), depth 0 (finite rep-theory identities). Tier: 3 SOLID + 1 candidate per the table; the *synthesis*
(cascade → spectrum) is the registered connection.

— T2491, registered by Grace, 2026-06-23. For Keeper registry + K-audit (esp. the C_2 general-rank link) and
Cal cold-read. Builds on Elie's n_C = N_c + rank (root multiplicity) and T1829.

---
## CLOSURE (2026-06-23, addendum) — rank=2 is FORCED; the cascade reduces to ONE physical input

rank = 2 is not a free input. It is forced two independent ways:
- **N_c = rank²−1 = 3** (T1829 PROVED) ⟹ rank² = 4 ⟹ **rank = 2**, from the physical fact of **three colors**.
- **n_C = rank²+rank−1 = 5** (dim_ℂ D_IV⁵) ⟹ (rank+3)(rank−2) = 0 ⟹ **rank = 2**.

So the full chain closes to a single physical handle:

> **N_c = 3 (three colors) —T1829→ rank = 2 —T2491→ {n_C=5, C_2=6, g=7} —T2490→ discrete-series spectrum →
> glueball ladder + Yang–Mills gap (C_2 = rank(rank+1) = 6).**

The dynamical substrate primaries reduce to the **single physical fact: three colors.** (N_max = 137 is the one
remaining boundary integer, definitional from the four.)

## Honest scope of the Casey #17 linear/quadratic unification

Does the boundary-linear / bulk-quadratic ladder reach proton/lepton masses (the Casey #17 candidate)?
- glueball **ratios** are pure integers/half-integers — the Bergman volume and χ_top **cancel in the ratio**.
- proton m_p/m_e = 6π⁵ and lepton m_μ/m_e = (24/π²)⁶ **carry π** (the Bergman volume K(0,0) = 1920/π⁵).
- ⟹ the ladder plausibly governs the **integer quantum-number structure** of all masses, but the **absolute**
  proton/lepton masses also need the π-volume factor. So Casey #17 should be scoped as governing the *integer
  structure* (the rungs), with the absolute scale carried by the separate volume factor — **not** as a claim that
  the bare ladder is the proton/lepton mass formula. Honest tier: structural-unification CANDIDATE at the
  quantum-number level; the volume-dressed absolute masses are a distinct (already-derived) layer.

— Grace, closure addendum 2026-06-23.

---
## CORRECTION to the C_2 link (2026-06-23, from the general-rank computation Casey requested)

The C_2 cascade link is **C_2 = 2·N_c** (general-n structural), NOT rank(rank+1) and NOT n_C+1. The (1,1) K-type
Casimir of SO(n) computes to **2(n−2)** in closed form (SO(5)→6, SO(7)→10, SO(9)→14, …), so for D_IV⁵
C_2 = 2(n_C−2) = 2·N_c = 6. Both "rank(rank+1)" and "n_C+1" equal 6 only by the rank-2 coincidence N_c = rank+1.
This **upgrades the link to SOLID** with the corrected form. Final cascade:
**N_c = rank²−1 (T1829) · n_C = N_c + rank · C_2 = 2·N_c · g = n_C + rank.** All four now SOLID (one PROVED).
See `grace_three_tasks_rungs_generalrank_coincidences_2026-06-23.md`.
