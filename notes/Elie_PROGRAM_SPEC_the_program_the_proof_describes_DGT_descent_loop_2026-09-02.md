---
title: "PROGRAM SPEC (draft) — the program the proof describes: the family-word descent loop (DGT). One page. Inputs, the 186-word family, the loop, the halting bound, the output; which toy IS the program and which are instruments about it; the floor, named."
author: "Elie"
date: "2026-09-02, Wednesday (clock-verified 08:14 EDT, stamp copied from a separate render)"
status: "DRAFT v2 (08:34, amended after 5587–5593) under frame (d3) per Keeper's K1835 ruling: 4CT(T) is an INPUT. Nothing here is a proof. The measured program is ONE WORD LONG (Section 8)."
---

# LINE ONE (frame, stated as an input)

T a sphere triangulation, **4-colorable (4CT, Appel–Haken/RSST) — stated as an input, not derived.**
v of degree 5. Every d_gate quantity below is finite only because of this input (Lyra's Lemma, 08:06;
Keeper confirmed 08:10). As a 4-COLORING algorithm the program is dominated by its own target-finding
step: any member of 𝒯(T,v) inserts v directly. **The program's content is the bounded, family-restricted
Kempe PATH from a stuck coloring to the gate phase — a Kempe-connectivity statement — not a coloring
algorithm.** That is what "proof plus program" honestly means today.

# 1. Inputs

| input | definition | source of record |
|---|---|---|
| c | proper 4-coloring of T−v with τ_v(c) = 6 (stuck) | Definition 5 (K1832) |
| canonical context | forced by stuckness: roles B₁, n_sM, B₂, n_si, n_sj on the link; colors r, s_M, s_i, s_j | One-Context Lemma (proved, T-registered) |
| 𝒯̂ | a SAMPLE of 𝒯(T,v) = {τ_v ≤ 5 colorings of T−v} (backtrack seeds + Kempe walks) | F1.stuck_harvest / G5.exhaustive_colorings (Fritsch) |
| 𝒜 | the 186 family words | Toy 5570 (15 context-moves × ordered distinct pairs; 93 mirror orbits) |

Sample dependence, owned: d̂_gate(c) := min over 𝒯̂ of H(c, c*) is an UPPER bound on the true d_gate.
A "no-descent" against 𝒯̂ is a shallow-sample event FIRST (5583 and 5585 each dissolved the same one);
the true program runs against 𝒯, which is exhaustively computable only on small T (Fritsch), not on
the flip objects (4^65).

# 2. The family (the alphabet)

A context-move m = (role, {x, y}) with the role's own color in the pair: a Kempe swap of the (x,y)-chain
seeded at the role's vertex, T−v, v excluded. A word w = (m₁, m₂), m₁'s pair ≠ m₂'s pair, applied as the
commutator m₁ m₂ m₁ m₂ (four stages; swaps are involutions). **Legality (K1835 A2): a stage is legal iff
its seed carries a pair color at that stage; a word is fully legal iff 4/4.** Instrument fact: the
laboratory's apply_move is a silent NO-OP on an illegal stage, so every count before 5587 admitted
words with a vacuous stage (3-swap words — not in 𝒜). 5587 re-counts under legality.

# 3. The loop (one round)

```
loop(c):
  if τ_v(c) ≤ 5 or some color absent at v:      EXIT (gate phase reached)
  roles ← role_map(c)                            # canonical context, forced
  C ← { w·c : w ∈ 𝒜, fully legal, supp(w) ≠ ∅, proper on T−v }
  choose w with d̂_gate(w·c) < d̂_gate(c)          # strict descent; nearest if several
  if none:                                       REFUSE (report; deepen 𝒯̂ first)
  c ← w·c
```
The target is chosen PER ROUND, implicitly, by the min: 5585 measured that a target held fixed from the
outset stalls on 1/54 where per-round choice recovers, and the potential that certifies halting is
d̂_gate = min over the menu, not H to one c*. Menu depth measured: the first target admitting a
per-target descending word sits within the nearest 3 on all 54 (no theorem).

# 4. Halting bound and output

d̂_gate is a non-negative integer and strictly decreases each round: **≤ d̂_gate(c₀) rounds, plus the
phase boundary's one freeing swap (the seam's +1).** Measured on the 54: 1 round (37) or 2 rounds (16)
under a fixed target; 50 of 53 in one round under the switching loop (5582). Output: a coloring c′ of
T−v with a color absent at v after ≤ 1 swap, hence a 4-coloring of T after inserting v; **plus the
certificate — the word sequence and the d̂-trajectory** (the object a referee can replay).

# 5. What the program certifies (DGT) and what it does not

**DGT (the theorem the machinery proves, frame (d3)):** given 𝒯 ≠ ∅, every stuck c has a fully-legal
family word with d_gate(w·c) < d_gate(c); hence the loop exits in ≤ d_gate + 1 words. Evidence: 54/54
(5582/5583/5585, shallow 𝒯̂), cage-off-carrier 54/54 in all three readings (5585); 1,801 and legality
pending (5586, 5587). **It does NOT certify 4CT:** its potential is defined through 𝒯, whose
nonemptiness is 4CT(T) (Lyra's Lemma). The consumption line into the induction is STRUCK.

# 6. Which toy IS the program; which are instruments about it

- **IS the program:** `toy_5582 … iterate_chain` (the switching loop; potential d̂_gate; 186-family;
  halt on τ ≤ 5 / freeable; cap d̂+1) on top of `toy_5570 role_map + context_family`,
  `toy_5521 (X3) commutator/support`, `toy_5512 (G5) kempe_chain/do_swap/is_proper/operational_tau`;
  target sample from `toy_5565 (F1) stuck_harvest`. **The legality-restricted form the Assembly
  actually consumes is `toy_5587 legal_iterate`** (same loop, fully-legal words only).
- **Instruments ABOUT it:** 5570 (alphabet enumeration + joint witness) · 5574/5579 (tranche commit,
  Family Exclusion falsifier) · 5580 (stability census, staging) · 5581 (anatomy, edit-order, cascade
  census) · 5583 (deep-freed probe) · 5584 (cage-predicate tagging, Barrier) · 5585 (target-menu sweep)
  · 5586 (DGT on the 1,801) · 5587 (legality re-count, stage-table control).

# 7. The floor (the missing piece, named)

A PROOF-program needs a potential Φ(c) ≥ 0 defined WITHOUT 𝒯 with (stuck ⟹ some fully-legal w descends Φ)
and (Φ minimal ⟹ not stuck) — door (d2). Five candidates died this week (S1–S5, frustration, height).
The instrument cannot existence-check (d2) on real triangulations (both Φ and d_gate exist there);
it CAN kill any written-down Φ on the 54 + 1,801 within the hour. That is the battery's standing job.

— Elie

# 8. AMENDMENT (after 5587–5593): the measured program is one word long, and the loop is a fallback

With every stage's legality tagged (5587) and the potential valued by definition — 0 on any image that
is itself in the gate phase (5590/5591) — the measured program never iterates: **at every stuck
configuration in the census (54 + 1,801 + the whole stuck sets of five populations incl. Fritsch
exhaustive: 1,072/1,072), some fully-legal family word's image has a color absent at v.** So the
program as measured is:

```
one_word(c):  for w in A (fully legal, supported, proper):  if some color is absent at v in w·c: return w·c
              REFUSE  # never happened in 2,927 measured stuck configurations
```
and Section 3's descent loop is the FALLBACK the theorem would need if REFUSE ever fired. The
statement the one-word program certifies is target-innocent: no metric, no 𝒯. Its truth for all T IMPLIES 4CT (sufficient, NOT equivalent — corrected 08:51 per Keeper K1836: 4CT does not give OWL back) — the honest target, not a circular one. Base rate (5592): a single random Kempe
swap already clears 1,846/1,855; the family clears 9 more (all inside the stability-failure set) and
is never beaten by the null. Mechanism (5593): the dominant word (B1,(r,s_i))(B2,(r,s_j)) returns its
seeds to r and recolors n_sM (freeing s_M) or rotates B1/n_si (freeing s_i), through the interior —
the commutator's support is what Kempe's two bare swaps lacked. **Which toy IS this program:
5593's loop (one word, direct-exit check); 5591's corrected_legal_iterate is the program with the
fallback attached.** The floor (Section 7) now reads: prove REFUSE never fires — that is (d2) in its
smallest form, and the nine configurations no single swap clears are where to look first.
