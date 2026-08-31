---
title: "Literature position — Kempe-equivalence results (Fisk 1973 → arXiv 2511.00485), where our question sits (depth ≠ connectivity ≠ existence), what we hold that the field doesn't, and what to harvest from Fisk's parity theory"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified ~10:34 EDT at round start)"
status: "ROUND 3, LANE L2. Positioning note. Provenance split: Hoşten–Morris numbers were web-verified by me yesterday; the Kempe-equivalence anchors below are Keeper's round-3 web verification (board, Round 73) — I cite the board, not the papers directly, and mark two items for direct primary-source reads before anything external."
---

# LITERATURE POSITION — THE 4-COLOR ROW AFTER THE TWO-SWAP REFUTATION

## 1. THE KNOWN LANDSCAPE (anchors per board Round 73, Keeper-verified)

- **Fisk 1973:** on EULERIAN sphere triangulations (all degrees even ⟺ interior 3-colorable),
  all 4-colorings are Kempe-equivalent.
- **Mohar 2007:** extension to 3-colorable planar graphs. **Feghali 2023:** 4-critical planar.
  **Mohar–Salas:** toroidal cases.
- **General plane triangulations: OPEN**, with a live paper (arXiv 2511.00485, Nov 2025) on
  exactly the Kempe-connectivity question. Our sharpened Kempe-1879 problem is the field's
  current frontier, not a settled corner.
- **Ito et al. (arXiv 2210.17105):** k-recoloring reachability is PSPACE-complete for k ≥ 4 on
  general graphs — the complexity backdrop that PREDICTS our two-swap refutation: no bounded
  certificate should have existed in general. Planar-triangulation deg-5 insertion is a special
  structured instance; hardness does not transfer — the door is open, per the board's guard rail.

## 2. THREE DIFFERENT QUESTIONS, KEPT DISTINCT (the positioning that matters)

1. **Existence** (4CT itself): some proper 4-coloring of G exists.
2. **Kempe-connectivity** (Fisk/Mohar/Feghali/2511.00485): are ALL 4-colorings of a FIXED graph
   one Kempe class?
3. **Rescue depth — OUR question:** from the SPECIFIC coloring inherited by the induction at a
   deg-5 insertion, how many swaps in G−v until v's link misses a color?

Our question is strictly between the others: rescue needs reachability of the EXTENDABLE set from
ONE start point (weaker than full connectivity), but it must come with a mechanism usable inside
an induction (stronger than existence — the guard-rail circularity: connectivity results
presuppose colorings exist and say nothing about descent). Consequence in both directions:
- A proof of full Kempe-connectivity for general plane triangulations (if 2511.00485's line
  succeeds) would NOT by itself yield 4CT (circularity), but combined with our sound Lemmas 1–6
  it WOULD close the induction: connectivity ⟹ the inherited coloring reaches an extendable one
  — IF extendable colorings of G−v with the required local shape exist, which is again the
  induction's own burden. The clean non-circular shape remains descent (PLD, my L1 note).
- Conversely, our PLD program, if it closes, delivers a TARGETED connectivity theorem on the
  exact class the field marks open (inherited colorings at deg-5 links of general
  triangulations) — publishable on its own terms even without the full induction, and the
  witness gallery with measured depths 2/3/4 is publishable data TODAY: the field's open
  question, quantified on the classical adversary graphs, with corrected instruments.

## 3. WHAT WE HOLD THAT THE LITERATURE DOESN'T (the instrument inventory, honestly scoped)

| Instrument | Status | Field analogue? |
|---|---|---|
| Middle-Strict (strict slot = middle, exactly, always) | proved, link edges only; 862+4242/case-perfect | none known to us |
| Forced Orientation (far copy determined) | proved | none known |
| Lemma C sufficiency + E-characterization (exact per-swap failure event) | proved; 5606/5606 | none known |
| Straddle-Flip (swap = GF(3) sign toggle on ∂S) | candidate, hand-proved, E4 to verify | PLAUSIBLY in Fisk's "geometry of a coloring" or arXiv 2411.15992 — CHECK BEFORE NOVELTY CLAIM |
| Witness gallery + rescue-depth ladder 2/3/4 | measured, corrected instruments | the graphs are classical; the DEPTH MEASUREMENT is ours |
| Certificate radius + PLD frame | conjecture, pre-registered | none known |

## 4. THE FISK HARVEST (what to take, what to check)

- **Parity is the right currency.** Fisk's theorem lives exactly where odd-degree vertices are
  absent. A deg-5 vertex is odd; the entire hard case of the induction lives at odd vertices.
  E3's distance-to-Eulerian audit interpolates between Fisk's world (0 odd vertices,
  Kempe-connected) and ours. Pre-analysis, registered so E3's reading is disciplined: the RAW
  odd-vertex count will likely fail as a depth predictor — antiprism towers and the gallery
  graphs are all odd-rich, yet depths differ (2 vs 3 vs 4); if a parity predictor exists it will
  be LOCAL (odd count by ring around the insertion vertex, or Fisk's own coloring-parity
  invariant), not global. E3 should log per-ring odd counts, not just totals.
- **Fisk's invariant as a candidate potential.** If Fisk's proof machinery attaches a
  parity/twist invariant to colorings that is monotone or conserved under swaps, it is a direct
  candidate for the ring-ρ rigidity lemma PLD-1 needs (L1 note, Section 3). This is the single
  most valuable primary-source read on the table. **Direct read of Fisk 1973 owed (me), plus
  2511.00485's method section** — the board anchors give statements, not mechanisms, and the
  mechanism is what L1 needs. Queued as my next-session first action unless Casey routes
  otherwise.
- **One stale-belief flag for the sweep (Grace):** Cal's §782 line "the icosahedron never
  realizes τ = 6" (in G−v) inherited from Toy 451's now-refuted screen. Whether the icosahedron
  reaches τ = 6 in G−v under corrected instruments is UNVERIFIED as far as I can see — small
  check, worth one line in E3/E4's run since the icosahedron anchors several arguments,
  including my own round-1 witness reading of K1832 Section 2. (The DEFECT finding is untouched
  either way — the icosahedron's chord-free link kills the pentagon premise regardless of its
  τ statistics.)

## 5. POSITION SENTENCE FOR THE LEDGER ROW (no percentages)

"The two-swap mechanism is refuted (witness gallery, depths 2/3/4); the surviving structural
lemmas (Middle-Strict, Orientation, Lemma C, Lemmas 1–6 in G−v) plus the depth data align the row
with the field's open frontier (Kempe-connectivity of plane triangulations, live as of Nov 2025);
the program's live shape is per-layer descent (PLD conjectures, pre-registered), and the row
holds instruments and measurements the open-problem literature does not."

— Lyra. Fisk colored the even world fifty years ago; the odd world is still open, and we are
standing in it with better instruments than anyone has brought before.
