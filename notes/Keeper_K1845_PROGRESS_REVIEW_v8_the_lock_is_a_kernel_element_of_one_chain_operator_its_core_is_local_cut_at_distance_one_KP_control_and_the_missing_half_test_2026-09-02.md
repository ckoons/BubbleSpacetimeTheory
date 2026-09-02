---
title: "K1845 — PROGRESS REVIEW v8 (12:19): the far-chain condition is necessary for a lock, NOT implied by bridge failure (93% of the 1,211), and exits do not break it (92%); Cal's exact trajectory type fragments (1,259 classes) and its one theorem-class is mixed — purity by fragmentation is not classification; the LOCK IS A KERNEL ELEMENT of one chain operator (rank of X₃ minus the cut) whose CORE IS LOCAL (the cut at distance exactly one from the link) and whose sufficiency is global. Two cheap tests from Theorem KP decide what 'necessity' is; Round 103."
author: "Keeper"
date: "2026-09-02, Wednesday (clock-verified 12:19 EDT)"
status: "Review + Round 103. The consolidation recommendation (K1843 §3) stands; this round adds the two KP tests and the kernel reading. Nothing banks."
---

# 0. Ledger 12:08–12:2x
- **Cal's decisive test (Elie 5620; Grace 5621 second instrument running):** the far-chain condition holds on
  349/349 locks, on **93% of the 1,211 bridge-fail set**, and on 35% of generic stuck colorings. **Necessary for a
  lock; NOT implied by bridge failure** (7% of bridge-fail configurations lack it) — so a derivation of necessity
  must cite the failure of words beyond the two bridge words (Cal's referee question (a), answered by data).
  Grace's 14,279/14,279 was on bridge-stuck IMAGES of exiting words, a different population; reconcile.
- **Exits do not break the condition:** 92% of exiting first words land in images that still have it (Grace).
- **The exact trajectory type (68 bits) fragments into 1,259 classes;** the single class every lock shares (Lemma T's
  own bits) is mixed; the 9 small pure-locked classes hold 23/401 locks — **purity by fragmentation is not
  classification** (Cal's "what mixed implies" fires: the lock is not first-order in chain incidence at any fixed
  family). Fifth bit: 349/349 locks, 89% of unlocked.
- **Theorem KP (Lyra)** stands for Cal's read; its two cells need one count: **does any lock admit a two-swap Kempe
  exit?** Predicted 0 (no lock has the far bit off) — a positive control that comes free; one exception reopens
  the theorem or the measurement.
- Fourth counter collision (Grace); the guard now aborts the launch. Gallery 377 witnesses.

# 1. The reading that reconnects to the linearization order
Grace's sentence — "sufficiency is the rank of X₃ minus the cut, a connectivity statement inside one chain" — is a
statement about ONE OPERATOR: the Laplacian of the chain X₃ with the cut C removed. **The lock is a kernel
element:** removing C splits X₃ so that the near copy and the far singleton lie in different components — an
extra vector in ker L(X₃ − C). That is target-innocent, computable, and it is the linear-algebra form of Lemma T.
Two measured facts sharpen it. (i) **The core is LOCAL:** on every witness measured the cut vertices sit at
distance exactly 1 from the link, never on it (Grace 5610), and |C| is 1–4. (ii) **The exit is generic:** any
non-bridge legal word exits 96–98% of the time, flat across orbits, below the 99.7% null. Together: *a lock is a
1–4-vertex defect in the second neighborhood of v whose LOCK-ness is a global connectivity fact about one chain;
almost any recoloring that touches the defect's neighborhood destroys the kernel element.* The observer lives in
the connectivity; the defect lives at radius 2 — the Context-Finiteness object named on 08-31 as "the true
summit," now with a precise reason it could only ever be half of a proof.

# 2. Two cheap tests that decide what "necessity" is (from KP)
- **T1 — the two-swap count on the 349:** zero Kempe-pairing exits predicted. Zero ⟹ KP's control passes and
  "locked" is consistent with the coloring, not only with the commutator shape. Nonzero ⟹ "two-word-locked" is
  RELATIVE TO THE SHAPE (the shape hides its own prefix) — a finding, not a defeat; Cal's position-vs-value on the
  shape lands there.
- **T2 — the missing half, on the ~85 bridge-fail configurations WITHOUT the far bit:** they are not locks, so some
  family word exits; which? If a fixed word (Lyra's named guess: KP's prefix carried by a non-commutator family
  word) exits on all of them, then "far bit off ⟹ that word exits ⟹ not locked" is derivable and the far-chain
  NECESSITY becomes a theorem with a constructive half. If the exiting words scatter, necessity stays measured.

# 3. Round 103 — investigation, not gating
The kernel instrument (Grace) · T1 and T2 (Elie) · cut-at-distance-one DERIVED from the stage structure (Lyra:
the cut is X₃ ∩ X₄ at r; both chains are seeded at copies; why must the intersection sit on N(link)?) · KP's cold
read and the "fragmentation is not classification" ruling (Cal) · reconcile 14,279 vs 93% (Grace + Elie) ·
n = 25 · the paper. The recommendation to Casey (K1843 §3) stands: close at the floor at EOD unless a depth-3
witness, a nonzero T1, or a clean T2 reopens it. Each of those three is a genuinely new object.
— Keeper

**NAMING POINTER 12:41 (K1846, Cal §824):** every 'lock' / 'two-word-locked' in this artifact means COMMUTATOR-LOCKED AT DEPTH ONE — relative to the fixed-seed 186-menu (link seeds only). 27/349 have a plain Kempe swap exit seeded off the link; Kempe's pairing inserts on 2. Not a property of the Kempe landscape. Verdicts unchanged; the noun is corrected here, not silently.
