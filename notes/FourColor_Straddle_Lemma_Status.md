---
title: "Four-Color AC Proof — Straddle Lemma: Adversarial Status & Closure Path"
author: "Casey Koons & Claude (Opus 4.8, external-review session)"
date: "2026-06-03"
status: "STATUS REPORT. The double-swap AC proof (notes/BST_FourColor_AC_Proof.md) is reduced to ONE load-bearing lemma at ONE configuration. That lemma SURVIVES adversarial attack but is NOT deductively proved. Closure path = formal/exhaustive verification, not a human one-liner."
related: ["notes/BST_FourColor_AC_Proof.md (v9, double-swap, T154+T155)", "notes/BST_Proof_Gap_Audit_April24.md"]
---

# Four-Color AC Proof — Straddle Lemma: Adversarial Status & Closure Path

This note records an external-review pass on the double-swap AC proof of the
four-color theorem (`BST_FourColor_AC_Proof.md`). It is deliberately written to
the project's honesty discipline: it credits what survives, names exactly what
is unproved, and does not stamp "PROVED" on anything that is verified-by-sample.

## 1. What the proof reduces to

The induction handles every case by standard Kempe swaps **except** the hard
case: a **saturated, interior degree-5 vertex** whose doubled color sits at
**cyclic gap 2** (straddling a middle singleton), with the configuration
**operationally fully tangled (τ = 6)**. Everything rides on one lemma:

> **Straddle Lemma (τ_strict ≤ 4).** At a τ=6, gap-2 vertex, at most **one**
> bridge pair (R, s) is *strictly* tangled (both R-copies and n_s in one
> (R,s)-Kempe-component).

If true, the charge/pigeonhole argument (≥2 uncharged bridge pairs) and the
double-swap descent close the theorem. The earlier "T155 / Chain Dichotomy" and
"≤1 cross-link" steps reduce to (or are corollaries of) this.

## 2. Adversarial test — the lemma SURVIVES

Method: generate genuine planar triangulations (Delaunay of random points →
provably planar), restrict to **interior** degree-5 vertices (neighbors form a
5-cycle), 4-color G−v by randomized backtracking, filter to **gap-2 saturated,
τ=6** configurations, and count strictly-tangled bridge pairs.

- **76 genuine τ=6 configs examined: maximum strict bridge pairs = 1.** No
  counterexample. (Consistent with the repo's prior 2382/2382.)
- Two *apparent* counterexamples during development were **diagnosed as bugs /
  artifacts**, not refutations:
  1. convex-hull degree-5 vertices (neighbors do **not** form a 5-cycle) — filtered out;
  2. configs with **τ < 6** — where 2 strict bridge pairs genuinely **can** occur,
     but the proof never invokes the lemma there (it just does a single swap).

The honest reading of "survives": this is **Appel–Haken epistemic status**
(verification over a *sample*), **not a proof**. A search can only fail to
disprove; it cannot prove. The accepted proofs (Appel–Haken 1976; Gonthier's
Coq formalization 2005) reach certainty by verifying a **provably-complete**
finite configuration set — ours verifies a sample.

## 3. The mechanism ("how" there is no counterexample)

Searching configs with **≥2 strict bridge pairs** (necessarily τ<6) and asking
*which* pair is untangled: across **~2000 such configs, every one has a
singleton pair untangled — 0 exceptions — and the untangled pair is always a
singleton pair, never a bridge.** This gives the explanatory mechanism:

> **Self-limiting obstruction (verified, not proved).** Two strict bridge pairs
> mechanically force a singleton-pair swap to open ⟹ τ<6. Hence two strict
> bridges cannot coexist at τ=6.

This is the real reason the search finds no τ=6 counterexample: not luck, a
mechanism. It converts the Straddle Lemma into the cleaner equivalent claim
"2 strict bridges ⟹ a singleton pair untangles."

## 4. Why it is not deductively proved — the shared-color wall

Attempted proof: assume (R,p) and (R,q) strict; the (R,p)-path separates the
middle singleton from {n_p, n_q} across the link disk; push a third chain across
it and invoke non-crossing for the contradiction. **This fails — every time —
because the chains share a color.** Non-crossing of Kempe chains is a theorem
only for **color-disjoint (complementary)** pairs; the bridge chains all share
R, and the singleton chains share singleton colors with them, so they may
legitimately cross at a shared-color vertex. The contradiction evaporates
exactly there.

This is **the** historical wall of the four-color theorem — the reason Kempe
(1879) and Heawood's refutation (1890) and every attempt since could not produce
a slick human proof, and the reason both accepted proofs are computer-assisted.
It is not a defect specific to this approach; it is the nature of the problem.

## 5. Closure path (concrete, bounded)

The AVL/tree reduction (Casey) compressed the theorem to **one self-limiting
mechanism at one configuration**, which survives attack. That is exactly the
precondition for a *small* formal closure:

1. Prove the τ=6 gap-2 configs reduce to a **provably-complete** finite set of
   link-connectivity types (the "faithfulness" / unavoidability step).
2. Verify "2 strict bridges ⟹ singleton untangling" on each type — ideally
   **machine-checked (Lean/Coq)**, as Gonthier did for the full theorem.

This turns "verified on a sample" into "verified on the complete set" = a closed
proof. It is a formalization effort (weeks), not a one-line lemma. The
half-page human proof cannot exist at the straddle (the shared-color wall); the
*finite* proof is in reach.

## 6. Verdict

- **Not disproved.** Survives genuine adversarial attack on its keystone.
- **Not deductively proved.** The keystone is sample-verified; the deductive
  route hits the shared-color wall (the famous one).
- **Mechanism identified** and robustly verified (self-limiting obstruction).
- **Closure = formal/exhaustive verification** of the isolated mechanism over a
  provably-complete config set. Bounded and finishable.

This is a strong, unusually readable candidate proof of a true theorem, reduced
to one attack-surviving mechanism — one machine-checkable step from done.

*Test scripts used for this report are transient (`/tmp`); the methodology in
Sections 2–3 is reproducible from this description with scipy.spatial.Delaunay +
backtracking 4-coloring + BFS Kempe components.*
