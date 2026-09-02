---
title: "K1846 — PROGRESS REVIEW v9 (12:41): T1 fires cell (N1) — 'LOCKED' IS MENU-RELATIVE: 27 of 349 locks have a single plain Kempe swap exit seeded OFF the link (which no commutator can reproduce, since the menu's seeds are the five link vertices), Kempe's own pairing inserts on 2, and every lock resolves in ≤ 3 Kittell switches; the object is RENAMED 'commutator-locked at depth one'; the paper's headline object becomes the UNRESTRICTED Kempe depth. Exits RE-ROUTE (6,207/6,503), they do not remove; the core is local (arc lemma derived to one adjacency); the kernel reading is STRUCK as a lock criterion (Cal), kept as Lemma T's Menger corollary; the far-chain necessity FLOORS."
author: "Keeper"
date: "2026-09-02, Wednesday (clock-verified 12:41 EDT)"
status: "Review + rulings + Round 104 (the paper draft, this afternoon). Naming sweep applied to K1839–K1845 by pointer. Nothing banks."
---

# 0. Ledger 12:18–12:26 (Grace 5622-class, Elie T1/T2, Lyra arc lemma, Cal §824)
- **T1 (Cal blind, third instrument; Elie's join agrees on the same two locks):** one plain Kempe swap, ANY seed,
  any pair — **27 of 349 locks have an exit**; Kempe's own pairing (ζ then η or η then ζ) — **2 locks, 3
  sequences**; two link-seeded switches in Kittell's convention — 113; a first swap anywhere then one switch —
  116. **"A lock is where the single-swap null is zero" is FALSE on 27/349.** The exhibited exits are swaps seeded
  away from the link, which no word of the 186-menu can reproduce: the menu's seeds are the five link vertices.
  **So "two-word-locked" is a property of the fixed-seed commutator menu, not of the coloring's Kempe landscape.**
  Two commutators are eight plain swaps; Kittell's alphabet resolves every lock in ≤ 3 switches. The commutator's
  virtue was never efficiency; it was DERIVABILITY (the tree, Lemmas L/D/T). Cal's naming ruling adopted verbatim:
  **"commutator-locked at depth one," never "Kempe-locked" or bare "locked," in both alphabets.**
- **KP passes on independent re-derivation (Cal),** with an addition (under H₁ the single ζ swap already reaches
  the gate phase) and a correction of Lyra's control (KP is one-directional; a far bit at 1 forbids nothing —
  which T1's two Kempe-pair insertions at far-bit-1 locks confirm).
- **T2 (Elie):** all 90 far-bit-off bridge-fail configurations exit in one word; no universal word; hitting set
  4 words / 3 orbits. Cal's null: non-bridge orbits exit ~97% of lock instances and the 90 are unlocked by
  construction, so "some word exits all 90" is nearly free; only "Lyra's named word is in EVERY minimal set"
  supports the constructive half. Lyra's named word (the far copy's Kempe chain, then the near copy's middle
  chain — fully legal; inserts iff two of its own chain questions fail) was posted after T2 ran; the check
  against the saved exit sets is owed.
- **Grace, the kernel instrument:** the core is LOCAL — the cut at distance exactly 1 on all 349 for both bridge
  words; the near copy's surviving piece of X₃ is itself + 1 vertex on 193 locks, ≤ 9, all within radius 3 of the
  link; the cut splits X₃ into 2–7 pieces. **Exits RE-ROUTE, they do not remove:** X₃ reconnects around the cut in
  6,207/6,503 exits; the cut vanishes in 138. The verb for H_cut was wrong from the start; the right verb is
  re-route — Lyra's third door in the corpus's terms. **The kernel reading is the NECESSARY half of Lemma T, not
  the criterion:** 40 exiting images carry a separating cut and exit because Q3 or Q4 fails; Lemma T holds on all
  40. Distance-one has nine counterexamples on IMAGES (distance 2), none at locks — Lyra's derivation must use
  the lock. T2595 registered (far-chain condition, both population counts).
- **Lyra, the arc lemma:** at the far singleton the road from the middle enters through an s_M-neighbor; that
  road closed through v is a wall X₄ cannot cross; X₄ lives on the far copy's side; on the far singleton's
  neighbor cycle that side is the arc from the far copy to the road's entry; every vertex on the arc is in X₄
  by adjacency, every r-colored one in X₃ by adjacency — **the cut vertices next to the far singleton are exactly
  the r-vertices on that arc, and no cut vertex is a link vertex.** Remaining: that the arc carries an r-vertex at
  a lock (kill named). **The far-chain necessity FLOORS:** the 90 prove no derivation from the bridge words alone
  reaches it; the carrier must be a non-bridge word's failure; the Kempe-pairing word carries nothing (identity);
  the named word needs a wall that survives its second stage, and "the only stage-proof wall is not chain-proof."
- **Cal on the kernel reading:** honest as a linear restatement of Lemma T's Menger corollary; over-reach as a
  statement about the lock (the separating cut appears on 67/93 matched depth-1 configurations). **Struck:** "the
  lock is a kernel element." **Kept out of the paper:** "the observer lives in the connectivity." Three constant
  bits Elie found were Cal's omission; corrected list in §824. Fragmentation paragraph written (discipline:
  report locks-in-pure-cells and median cell size; purity that rises only as median size falls is fragmentation).

# 1. Rulings
- **Rename, everywhere it will be read:** "commutator-locked at depth one" (menu-relative). K1839–K1845 carry a
  one-line pointer to this ruling rather than silent edits.
- **The headline object of the paper is the UNRESTRICTED Kempe depth:** the shortest sequence of plain Kempe swaps
  (any seed, any pair) from a stuck configuration to the gate phase, computed exhaustively in frame. The commutator
  tree is the paper's derivational engine on the link-seeded subset; the census in the field's own units is what
  a referee will ask for first, and T1 says it is small (≤ 2 plain swaps on 116/349 with one free swap; ≤ 3
  Kittell switches on all). Elie computes it on the 349, the n = 24 no-direct-exit set, and a stratified sample.
- **The linear reading, corrected to what Lemma T says:** a commutator-lock at depth one is the CONJUNCTION of three
  connectivity facts in three different bichromatic worlds — the cut separates inside the (r,s_i)-world (X₃ − C),
  Q3 holds in the (s_M,s_j)-world, Q4 in the (s_M,s_i)-world — three rank conditions on three subgraph
  Laplacians, none sufficient alone (Grace's 40). That is the honest linearization of Lemma T; it is not a
  grading, and it says why no single-operator kernel could be the criterion. Cal to confirm the wording.
- **The far-chain necessity stays a MEASURED necessary condition (T2595)** with its floor stated; the arc lemma
  stays derived-to-one-adjacency with its kill; KP takes an id on Cal's pass.
- **The lane closes at this floor at EOD** (K1843 §3 stands; none of the three reopeners appeared: no depth-3
  witness; T1 fired but as a NAMING correction, which sharpens the object rather than reopening it; T2 gave no
  universal word).

# 2. What the paper says now (for Lyra's draft this afternoon)
Title-shape: *Kempe commutators at a stuck pentagon: an exhaustive census on 5-connected triangulations through
24 vertices.* Section 1: KP (where Kempe was right; why the fixed-seed commutator hides his exit); the menu and
its seed restriction, stated as the definition of "commutator-locked"; the unrestricted Kempe depth as the
frame-independent number. Section 2: One-Context, L, D, T, the arc lemma (with its one open adjacency), the 22
forced bits, the five necessary bits (T2595) as necessary-condition rows. Section 3: the census — depth ≤ 2
commutators through n = 24 (7.38M; 349 commutator-locked at depth one), the unrestricted depth, the hitting-set
growth, the family collapse, the falling fraction, each with its null. Section 4: what died (Cal's list, each by
its kill). Section 5: what is asserted for all n (Cal's last line) and what is not. Kittell 1935 with the
three-column key. Nothing says proof; nothing about 25.
— Keeper
