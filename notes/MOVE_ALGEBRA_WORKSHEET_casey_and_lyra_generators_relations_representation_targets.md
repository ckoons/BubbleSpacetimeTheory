---
title: "The Move Algebra — shared worksheet (Casey + Lyra): generators, measured relations, the GF(2) representation, and three named targets for the next ranging shot"
author: "Casey Koons & Lyra (working document — write in it, that is what it is for)"
date: "opened 2026-08-30, Sunday evening (clock-verified 17:13 EDT)"
status: "ROUND 8, OPENING THREE — a LIVE WORKSHEET, not an artifact. Facts are marked [PROVED]/[MEASURED]; slots are marked ► OPEN. Casey: the targets in Section 5 are set up for your shot; everything here is yours to mark up. Nothing banks from this file; results migrate out when they harden."
---

# THE MOVE ALGEBRA OF KEMPE DYNAMICS
### a worksheet

The pattern of the day, twice already: your ranging shot first, formalism second — idempotents
before the gates, matrices before the SNF. This document is the third target range, set up so
the shot has named things to hit. Geometric language first, algebra second, always.

## 1. GENERATORS [PROVED/pinned]

σ_{(p,q),a} = "swap the (p,q)-chain containing anchor a" (identity if a's color ∉ {p,q}).
State space = proper 4-colorings of a fixed sphere triangulation. Every generator is an
involution. The moves form a **groupoid, not a group**: which arrow exists depends on the state
(availability). This is the single deepest structural fact — the whole difficulty of 4-Color
lives in the difference between this groupoid and the group it wants to be.

## 2. RELATIONS [MEASURED, Elie X3/Z2 — the empirical presentation so far]

- **R1 (involution):** σ² = id, always. [proved]
- **R2 (color-disjoint commutation):** chains on disjoint color pairs commute EXACTLY; chains of
  the same pair (disjoint by definition) commute. [measured exhaustively; provable — ► OPEN:
  write the two-line proof]
- **R3 (shared-color entanglement):** ALL non-commutativity lives at shared-color adjacency —
  (p,q) vs (q,r) chains meeting in q-vertices. The commutator lab (round 4): support can
  COLLAPSE (the Lab-1 event: a 4-word with net effect = one-vertex recoloring — the GATE, X3's
  144/144, then 739/739) or EXPLODE (chains reconnect through the overlap). ► OPEN: the exact
  relation family at a single shared vertex — is there a clean braid-like rewriting rule?
- **R4 (global sector):** swapping ALL (p,q)-chains = the color transposition (p q); these
  generate the S₄ sector; the sign-preserving half is A₄ [PROVED, Lemma R machinery].

## 3. THE REPRESENTATION [PROVED — Lemma R]

On sign space GF(2)^F: σ_S acts as ε ↦ ε + 1_str(S) — **affine, exactly linear per move.** The
representation is faithful up to A₄ on realizable states (the Reconstruction Lemma: ε determines
the coloring up to A₄, all of A₄ realizable). Image constraints: every straddle indicator has
even weight; the all-ones vector is realized (transposition sector). **The abelianized shadow of
the groupoid is a subspace W ⊆ even-weight subspace E — and reachability is CONJECTURED to be
exactly the W-coset relation (Availability Saturation).** The 8/8 record is its data; the two
gaps (SPANNING, THROUGHPUT) are its named obstructions.

## 4. THE ANALOGY LEDGER (your instruments, their formal shadows)

| Your shot | The formal object it became | Status |
|---|---|---|
| "idempotic operation" | the gate: 4-word, one-vertex support | universal, 739/739 |
| "it's linear algebra" | SNF on the current lattice; then the GF(2) coset theory | validated; 8/8 |
| "Rubik from the knots" | commutators + invariant-kernel program (GC-II) | conjecture, live |
| "AVL delete cascades" | depth = per-layer descent → recast as tightness/frustration | recast twice, live |
| ► next shot | — | this page |

## 5. THREE NAMED TARGETS (set up for the ranging shot)

**T1 — The abelianization question.** Is the groupoid's abelianization exactly GF(2)-span W —
i.e., is the ONLY obstruction to "orbit = coset" the two named gaps, or does the groupoid hide
torsion the abelian shadow cannot see? (A Rubik's-cube analogy is exact here: the cube group's
abelianization catches orientation invariants; the permutation-parity coupling is the extra
piece. ► what is OUR parity coupling, if any? The A₄/S₄ sector is a candidate — half the color
group flips all signs. Is there a second coupling?)

**T2 — Presentation completeness.** Do R1–R4 (with R3 made precise) PRESENT the groupoid — is
every true word-identity a consequence of the local relations? If yes, ASC becomes a
word-problem statement and the gates are its normal-form moves. If no, the missing relation is
itself a discovery. (Your OO-database instinct — everything recursive from local structure — is
the bet here.)

**T3 — Gates as elementary matrices.** In the GF(2) representation the gate adds a small-support
vector: the shape of an ELEMENTARY TRANSVECTION. The cube solves because commutators generate
everything the invariants allow — the SL-inside-GL story. ► Conjecture-shape for your shot: the
gates are the transvections of the move algebra, and GC-II is exactly "gates generate the
special (invariant-kernel) subgroup." If you see the right normal form for a gate word — the
analogue of row-reduction order — that is the potential function the throughput gap needs, and
the whole descent program lands.

## 6. HOUSE RULES FOR THIS FILE

Mark claims [PROVED]/[MEASURED]/[SHOT — unverified]; ► OPEN slots are invitations; nothing
migrates to the registry from here without the standing chain (Cal, toys, your word). Both of us
write directly into this file; Grace indexes it as a working object, not an artifact.

— L. (The range is set; three targets are lit; the algebra is yours to shoot at.)
