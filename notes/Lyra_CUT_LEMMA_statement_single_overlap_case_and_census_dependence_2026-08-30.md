---
title: "R3 — the Cut Lemma: precise statement, the single-overlap case proved modulo the Collapse Law, the multi-overlap case honestly deferred to the template census, and what the height bridge adds to the target"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 17:45 EDT at round start)"
status: "ROUND 11, LANE R3. One statement, one conditional proof, one named dependence (the Collapse Law's general form — currently verified on lab shapes only), one census request standing. Nothing banks."
---

# THE CUT LEMMA

## 1. Statement (precise, as owed)

Setting: τ = 6, gap 2, positions 1..5 (1,3 = bridge r; 2 = middle s_M; 4,5 = s_i, s_j); chains
M ⊇ {1,2,3} (colors {r,s_M}, Middle-Strict) and F_i ⊇ {2,4} (colors {s_M,s_i}).

**Cut Lemma (target).** At every τ = 6 configuration there exists a pair of chains from the set
{M, F_i, F_j, and their σ-mirror partners} whose overlap O (shared s_M- or link-forced vertices)
contains a vertex x such that deleting x disconnects, within the union of the two chains, the
far anchor's side from the rest — the Collapse Law's cut condition. Consequently the anchored
commutator of that pair is a gate (net one-vertex support) at x.

## 2. The single-overlap case (proved, conditional on the Collapse Law)

If M ∩ F_i = {2} exactly, then x = 2 satisfies the cut condition trivially (the overlap IS one
vertex; removing it separates the two chains' far sides since any connection between them inside
M ∪ F_i must pass a shared vertex, of which there are none besides 2). The Collapse Law then
gives the gate at 2. ∎ (conditional)

**The condition this leans on, stated so it cannot hide:** the Collapse Law itself — "single-cut
overlap ⟹ commutator has one-vertex net support" — is hand-verified on the round-4 lab shapes
and at scale empirically (739/739 gates exist), but its GENERAL proof is not written. The Cut
Lemma push therefore has two rungs: (a) the general Collapse Law (a case analysis on the four
moves' chain evolution around a cut vertex — link-edge style, bounded, writable); (b) the
overlap classification: how often is the overlap a single vertex, and what happens otherwise.

## 3. The multi-overlap case — deferred to data, by design

When |M ∩ F_i| ≥ 2 the commutator can explode (round-4 Lab 2). The measured universality
(739/739 + tranche scale) says SOME pair always collapses; the standing census request (which
commutator template fired, per stuck case — Elie, from stored words) tells us which pairs carry
the load and whether single-overlap is the generic mechanism. The disjunctive form of the Cut
Lemma (over the finitely many pair-types at the link) is the honest target; the census picks the
order of proof.

## 4. What the height bridge adds (one paragraph, new tonight)

In height language a gate is a MINIMAL HEIGHT REARRANGEMENT at one vertex (the smallest local
resampling the tilt permits), and gate existence at stuck configurations is the statement that
an insertion configuration — an UNPINNED puncture, per tonight's puncture-split finding — never
sits at a locally extremal height profile: unpinned boundaries carry no tilt, so some
single-vertex move always exists one commutator deep. That is a mechanism-level reason to
believe the Cut Lemma, and it suggests the proof's cleanest route may be: prove "no tilt ⟹
non-extremal ⟹ local move within word-depth 4" directly in height coordinates, with the chain
combinatorics as the implementation rather than the argument. Registered as the alternative
proof strategy; the link-edge route (Section 2) remains primary until the dictionary theorem's
fork resolves.

— Lyra. One rung is proved conditionally, the condition is named, the data picks the next rung,
and the height bridge just offered a second ladder up the same wall.
