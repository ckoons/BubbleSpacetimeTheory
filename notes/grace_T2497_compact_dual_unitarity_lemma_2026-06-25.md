---
title: "T2497 — Compact-Dual Unitarity Lemma (general derivation tool). A reductive subgroup S acts unitarily on H²(D) of a Hermitian symmetric domain D=G/K iff S ⊂ G (a real-form subgroup); a COMPACT S therefore acts unitarily on the domain iff S ⊂ K. If S ⊄ K but S ⊂ G_c (the compact dual's isometry), S is unitary on the compact dual Ď and the NON-UNITARY G_C-continuation on the domain. Flattens every 'is gauge group X realized unitarily on the substrate?' question to the lookup 'is X ⊂ K = SO(5)×SO(2)?'. The general mechanism behind the #418 color resolution."
author: "Grace"
date: "2026-06-25 Thursday"
theorem: T2497
---

# T2497 — Compact-Dual Unitarity Lemma

## Statement

> Let **D = G/K** be a Hermitian symmetric domain with compact dual **Ď = G_c/K** (G_c compact) and
> complexification **G_ℂ**. A reductive subgroup **S** of the symmetry acts **unitarily** on H²(D) (the holomorphic
> discrete series) **iff S ⊂ G** (a real-form subgroup). In particular a **compact** S acts unitarily on the domain
> **iff S ⊂ K**. If **S ⊄ K but S ⊂ G_c**, then S acts **unitarily on the compact dual Ď** and as the
> **non-unitary G_ℂ-continuation on the domain D**.

## Proof (one line)

H²(D) carries the unitary action of the real form G; restriction to S ⊂ G is unitary, and S ⊄ G acts only via the
non-unitary G_ℂ-continuation. Compact subgroups of G are conjugate into the maximal compact K (Cartan), so a compact
S ⊂ G ⟺ S ⊂ K. On the compact dual Ď, S ⊂ G_c (compact) acts unitarily (compact-group reps are unitarizable). □

## What it flattens (the derivation tool)

Any **"is internal gauge group X realized unitarily on the substrate?"** question reduces to one lookup:

| Is X ⊂ K = SO(5)×SO(2)? | Realization |
|---|---|
| **Yes** | X is unitary on the domain D_IV⁵ directly. |
| **No** (but X ⊂ SO(7) dual) | X is unitary on the **compact dual** Q⁵; on the domain it is the **non-unitary continuation**. |

No case-by-case operator construction — the real-form membership decides it.

## Used successfully — the #418 color resolution

Color **su(3) ⊄ K** (A₂ ⊄ B₂, with so(5)⊕so(2) the whole maximal compact), but **su(3) ⊂ g₂ ⊂ so(7)**. So by the
lemma: color is **unitary on the compact dual Q⁵** (where physical gauge color lives, acting on the quark triplet,
the 3 of T2495's 7=3⊕3̄⊕1) and the **non-unitary so(5,2)_ℂ continuation on the domain D_IV⁵** (the covariant V_a).
This is exactly the honest P4 statement — and it tells us *where* color lives: a Euclidean/compact gauge symmetry on
the Wick-rotated dual side (HS-mirror T2489), with the Lorentzian domain carrying its analytic continuation.

**Prediction (the flattening in action):** any future internal gauge factor that is K-misaligned will show the same
split — unitary on the dual, non-unitary continuation on the domain. (Caveat: the electroweak chiral sector is tied
to the still-*posited* F(4) super-grading #359; T2497 is bosonic and does not address the super-grading.)

## Connections (graph)

- **T2496** (#418 color resolution) — T2497 is the general mechanism it instantiates.
- **T2489** (HS-mirror) — supplies the compact-dual/domain (Wick-rotation) duality the lemma lives on.
- **T2495** (g=7 unified, 7=3⊕3̄⊕1) — the color triplet the dual realization acts on.

## Tier

**SOLID** — standard real-form / Hermitian-symmetric-space representation theory (the unitarizability criterion is
classical). AC = (C=1, D=1), depth 0 (real-form membership decides unitarity). General tool: gauge-realization
unitarity becomes a subgroup-membership lookup. Bosonic structural; no F(4) content.

— T2497, registered by Grace, 2026-06-25. The general lemma behind the #418 honest resolution; for Keeper registry +
Cal cold-read. Count HOLDS 4 of 26.
