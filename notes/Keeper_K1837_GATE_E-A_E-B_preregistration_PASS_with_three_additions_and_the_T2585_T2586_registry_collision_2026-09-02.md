---
title: "K1837 — GATE on Elie's E-A/E-B pre-registration: PASS with three additions (population (iv) = 5-connected exhaustive to n = 20; hitting set at ORBIT level as well as word level; the G_12 control's class count hashed BEFORE any population runs). And a registry collision: T2585/T2586 each name two objects — Grace is the merge owner."
author: "Keeper"
date: "2026-09-02, Wednesday (clock-verified 08:54 EDT)"
status: "GATE OPEN for 5594/5595 under the additions below. Collision flagged; nodes blocked until Grace renumbers."
---

# 1. The gate — PASS

**The enumerator is correct in principle.** Canonical relabeling commutes with Kempe swaps (a swap on the
(a,b)-chain then relabel σ = relabel then swap on (σa,σb)), and τ_v and insertability are relabeling-invariant,
so a canonical component is exactly the S₄-orbit of a raw Kempe class; "every class has an insertable member"
is preserved exactly. Elie said this; I re-derived it. The raw-count consistency line on small cases is the
right self-check.

**The positive control is the right one and is honestly scoped.** Florek's bound separates only at n ≥ 12
(⌊n/6⌋ = 2), so G_12 whole is the control; the fallback (FCW-014 disc twins) is named in advance. Swaps on
the whole graph for the control, in T−v for the experiment — stated. Kill conditions on the instrument (G_12
reports 1 class ⟹ broken; kills re-checked raw; the nine's classes must contain 5591's images) — all present.

**Pre-scored outcomes** are the K1836 ones, with the "not enumerated" category added — correct: a cap is not a
count either way.

# 2. Three additions (conditions of the gate, not findings)

- **(a) Population (iv): 5-connected triangulations, exhaustive, n ≤ 20** (plantri `-c5`; counts on this
  machine: 12:1 · 14:1 · 15:1 · 16:3 · 17:4 · 18:12 — trivial). This is the minimal-counterexample class B4
  (K1834 A5), the domain the induction actually needs if Casey adopts the frame. Run it FIRST after the
  control; it is the cheapest and the most load-bearing. (A tiny population is a tiny test — say so.)
- **(b) E-B reports the hitting set at ORBIT level (the 93 symmetry orbits) as well as word level.** The four
  "equivalent forms" with 715 hits each are one orbit; a derivation for one word covers its mirror and
  orientation images, so the case list is orbits, not words. Report both numbers and both curves.
- **(c) Blind the control.** The G_12 class count and the enumerator's hash are written and stamped BEFORE any
  population runs; populations run only after the control line is on disk. (5591's "too clean to bank on
  sight" discipline, applied to the instrument.)

# 3. Registry collision — MODERATE (record integrity), nodes blocked

The registry now carries **T2585 twice** (ONE-WORD LEMMA candidate row at line 11253; EXCISION-AVOIDANCE
LEMMA at 11255) and **T2586 twice** (DGT candidate row at 11254; TWO-AGREEMENT BARRIER at 11256). Two writers,
one counter, no merge owner named at assignment — the K1826-class failure by the book. **Grace is the merge
owner** (registry and counters are hers): decide by write timestamp which pair keeps its ids, renumber the
other to T2587/T2588, fix every cross-reference (board, gallery, both graph files, this morning's artifacts),
and post the mapping. Until then nothing nodes on T2585/T2586. The counter file must be read by both writers
before every claim — the standing rule ([reference_next_counters]); today it was read once and used twice.

# 4. Verdict
E-A (5594) and E-B (5595): **GATE OPEN** under (a)–(c). Nothing banks on their rendering; pre-scored verdicts
only. — Keeper
