---
title: "K1840 — PROGRESS REVIEW v4 (10:20): depth holds at TWO through n = 23 (1.59M stuck colorings, 93 witnesses); Lane A dead (double tunnels); Middle-First measured — the hard regime is exactly Casey's practice (93/93) and the union procedure is the program. CASEY'S PROPOSAL FORMALIZED: 'finite map size' = One-Context (proved) + unavoidability (RSST); 'move the problem to the edge and it dissolves' = the problem in every stuck leaf is a FINITE object, the CUT, and the middle move is the only move that recolors r-vertices. H_cut pre-registered: the exiting middle word's chains CONTAIN the cut."
author: "Keeper"
date: "2026-09-02, Wednesday (clock-verified 10:20 EDT)"
status: "Review + formalization + one pre-registered mechanism test. Mode: investigate, don't gate. Nothing banks."
---

# 0. Ledger 09:45–10:12 (verified from RUNNING_NOTES 73741–73831)
- **n = 23 in frame (Elie 10:05):** 1,970 graphs · 29,396 (T,v) · 1,216,851 stuck colorings mod S₄ · direct exit
  1,215,272 · one word to gate 1,535 · **two words 44 · three: 0 · unreached: 0.** Cumulative n = 12…23:
  **1,591,509 stuck; 93 two-word witnesses; depth 3 never.** n = 24 running (~1–2 h). Per Cal's pre-score the
  null predicts < 1 depth-3 witness, so this zero supports no mechanism; only a mechanism test can.
- **Lane A dead (Cal §820):** double tunnels along the bridge path 194/196; depth stays 2 only because
  MIDDLE-moving first words exit. Lyra's pre-registered fourth exit fired; her attempt delivered the mirrored
  tree, the exact residue of the first tunnel, the commuting-chains fact, the **Boundary-Term Lemma (T2594)**,
  the **Kittell Alias Theorem (T2593)**, and T, L, D as T2590–T2592.
- **Middle-First measured (Elie 5608):** on the 93: middle→bridge **93/93**, bridge→middle 19/93. Across the
  frame (374,658): bridge-first exits 373,447 (fails 1,211); middle-first exits 147,814 only, because the
  middle canonical word is NOT fully legal on 225,505 (SJ is real and frequent in frame — 60%) and fails on
  1,339. **The union is the measured program: "bridge; if stuck, middle-then-bridge; if the middle is illegal,
  the next middle-touching orbit (four)."** Casey's practice is exactly the hard regime's exit, and only there.
- Join-key flag (Cal): "24 legal words" · "8–9 images" · "60 words, 8 images" are three counts — named below
  as W_legal(c), Im(c), W_acting(c) and not to be quoted unlabeled again.

# 1. Casey's proposal, formalized (10:1x: "a proof of finite map size, and showing all problems can be moved
to the edge, and the problem dissolves at the edge no matter how large, because no new complexities exist on
planar maps")

**Half 1 — "finite map size / no new complexities."** Two theorems already carry it. (a) Locally: **One-Context
(proved, zero census joints): at every stuck degree-5 vertex there is exactly ONE context up to symmetry —
one link word, six forced partitions, eight chains (Kittell's).** No new local complexity can appear at any n.
(b) Globally: **Euler's charge Σ(6 − deg) = 12 (K1834 A1)** — total curvature is fixed; the field's
discharging method turns it into UNAVOIDABILITY: every internally 6-connected triangulation contains one of a
finite list of configurations (RSST 1997: **633 configurations, 32 discharging rules**; Appel–Haken 1976: 1,936,
300+ rules). Casey's sentence is the unavoidable-set philosophy stated in one line, and half of it is ours already.

**Half 2 — "move the problem to the edge and it dissolves."** The problem is now a FINITE, NAMED object. On every
stuck leaf, Lemma T + Grace 5603: the image is stuck ⟺ the fourth chain X₄ meets the third chain X₃ at
r-vertices and removing them disconnects X₃ between the near copy and the far singleton. Call that set **the
CUT, C(c) := X₄(c) ∩ X₃(c)**, computable from c alone (the bridge word is fixed by roles) — target-innocent.
Now the mechanism hypothesis, which is Casey's sentence in the corpus's terms: **the bridge pairs (r,s_i),
(r,s_j) can never recolor a cut vertex out of color r without moving it into the other bridge world; the middle
pair (r,s_M) is the ONLY pair that takes an r-vertex to a color outside both bridge worlds.** So a middle move
that reaches the cut turns it to s_M, the tunnel no longer crosses the fence, and the bridge word exits. "The
problem moves to the edge and dissolves" = the cut leaves the (r,·)-worlds.

**H_cut (pre-registered here, before any count):** on the 93 witnesses, for every exiting first word (the
four middle-touching orbits), its stage chains CONTAIN C(c) (or enough of C to reconnect X₃); for every
non-exiting legal first word, its chains MISS C. Pre-scored: containment 93/93 with the control clean ⟹
**a mechanism, not a count** — the day's most valuable result, and the statement of the Cut-Dissolution Lemma;
partial containment ⟹ the cut is necessary but the mechanism is elsewhere (report the residue); no
containment ⟹ H_cut dead, potential #8 dead with it. **Potential #8 (pre-registered): κ(c) := |C(c)|**, with
κ = 0 ⟺ bridge-exitable (Lemma T, measured) and κ(M·c) = 0 predicted for the exiting middle word M. A grade
is a rank: C disconnects X₃ ⟺ dim ker L(X₃ − C) > dim ker L(X₃) (Grace's G1 reads it).

**What a PROOF in Casey's shape would be, honestly:** (i) the finite alphabet — One-Context (done);
(ii) the procedure — the union program (measured to depth 2 on 1.59M); (iii) **ONE lemma: at every
bridge-locked configuration some legal middle-touching word's chains contain the cut.** With Birkhoff (A5) and
the classical induction, (iii) for all n IS the theorem, in about a dozen human-readable theorems. Calibrated:
depth 2 through n = 23 is consistent with (iii) and also with an accident of small n (Cal's null). H_cut is the
experiment that tells them apart — the mechanism, not the count.

# 2. Research (this hour, web-verified)
- RSST 1997: 633 reducible configurations, 32 discharging rules, unavoidability on internally 6-connected
  triangulations (AMS ERA 1996 announcement; the LIX copy). Appel–Haken: 1,936 configurations (later 1,482),
  300+ rules. "An Introduction to the Discharging Method" (arXiv 1711.03004) is the reference for Half 1;
  "Reducibility in the Four-Color Theorem" (arXiv 1401.6481) for D-/C-reducibility, the field's formal version
  of "recolor the interior against every boundary coloring." **Alias note for Grace:** our "fence disc" (the
  region bounded by P ∪ v) is a ring region in reducibility's sense; Casey's "paste in a boundary and recolor" is
  D-reducibility's picture. We are NOT building an unavoidable set — the census is a different object and the
  paper must say so (Cal's referee line).
- The corpus already holds the "no new complexities" algebra: charge quantization (deg-5/7 = ±3; Σc = 12·deg,
  Lyra 08-30), the three-resolution tower heights/ℤ² → charges/mod 3 → colors/mod 2 (T2577). A cut vertex is an
  r-vertex lying on two walls of pairs sharing r — a height SADDLE in T2577's picture; Grace can classify.

# 3. Next (rubric cell: Internal E-math, the 4-color row) — H_cut first, everything else second.
— Keeper

**NAMING POINTER 12:41 (K1846, Cal §824):** every 'lock' / 'two-word-locked' in this artifact means COMMUTATOR-LOCKED AT DEPTH ONE — relative to the fixed-seed 186-menu (link seeds only). 27/349 have a plain Kempe swap exit seeded off the link; Kempe's pairing inserts on 2. Not a property of the Kempe landscape. Verdicts unchanged; the noun is corrected here, not silently.
