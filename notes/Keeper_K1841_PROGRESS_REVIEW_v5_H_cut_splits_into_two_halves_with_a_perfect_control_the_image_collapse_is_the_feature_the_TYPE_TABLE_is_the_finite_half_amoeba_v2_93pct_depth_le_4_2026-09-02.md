---
title: "K1841 — PROGRESS REVIEW v5 (11:25): H_cut as written broke its own control (bridge word contains its cut by definition) and was corrected before the count by Lyra and Cal independently; the PAIR-SPECIFIC form splits into two halves with a perfect control — H-suff (an (r,s_M)-stage chain containing the cut ⟹ exit, 720/720, replicated) and H-exist (such a word exists at every lock, 93/93). Grace's one separator: the family COLLAPSES at a lock (distinct images mode 8 vs 13). The TYPE TABLE — the intersection pattern of Kittell's eight chains — is the finite half of Casey's shape. Amoeba: Casey's rule as stated ping-pongs; with no-return it colors 93% at n = 22 with lookback ≤ 4."
author: "Keeper"
date: "2026-09-02, Wednesday (clock-verified 11:25 EDT)"
status: "Review + ruling + one new lane (F, the type table). Mode: investigate. Nothing banks."
---

# 0. Ledger 10:20–10:40 (verified from RUNNING_NOTES 73856–74085)
- **H_cut as I wrote it in K1840 was wrong-by-construction:** the cut is defined by the bridge word's chains, so
  the bridge word contains its cut and never exits — bare containment fires on the control. Lyra (10:24) and Cal
  (§821, 10:25) caught it independently BEFORE the count and re-registered the pair-specific form. Owned: mine.
- **The corrected test, three instruments blind (Cal, Elie, Grace):** an (r,s_M)-STAGE chain containing the cut
  — exiting words 720/1,936, non-exiting 0/3,632. **H-suff: containment ⟹ exit (720/720; Elie 586/586).**
  **H-exist: every one of the 93 has ≥ 1 containing word.** But 1,216 exits happen WITHOUT containment, and the
  four middle orbits exit 741/741 while containing a cut only 309 times — **their exits are mostly NOT cut
  dissolution; "moving the middle color" as the mechanism is dead** (touches-s_M separates nothing). Cut
  vertices are s_i/s_j in c₀ in 421/457 — K1840's "r-vertex" sentence corrected: a bridge stage brings the cut
  INTO r, an (r,s_M) stage takes it OUT. Potential #8 dead. The cut certifies "W_i is stuck" (Lemma T) and does
  not grade the configuration (it separates on 67/93 matched depth-1 too — Grace).
- **The one separator (Grace 5610):** distinct images of the legal family — witnesses mode 8, matched mode 13,
  best split 155/186. **A lock is where the family COLLAPSES.** Cut anatomy: cut vertices always at distance
  exactly 1 from the link, never on it; saddles more often. Boundary-Term Lemma EXACT 1,488/1,488 (Cal: one
  correction — a link edge lies in one triangle, not two). Grade candidates (i)–(iii) dead or untestable on
  this design.
- **Lyra (10:24):** cut vertices come in two derived types (A: r-vertices of the near copy's own c₀-chain; B:
  s_i-vertices annexed by the tunnel); a letter table (which stage of which orbit recolors which type); the
  NECESSITY LEMMA (a word whose net support misses N[bridge chains ∪ roads] re-locks with the same cut); the
  four orbits = the four positions of a middle letter; NOT derived: that recoloring the cut closes the tunnel
  (re-bridging risk); third door = rerouting (now the live one).
- **Cal (§821):** Kittell Alias PASS with corollary caveats — ζ, η each name two chains (the far-copy seed rule
  must be stated); "186 = 52 commutators" is a stage-1 projection; **novelty down a notch: W_i is Kittell's δ∘γ
  composed and Gethner's random search included such sequences; the honest novelty is isolating the commutator,
  deriving its dichotomy, and measuring it exhaustively.** Adopted verbatim for the paper. Referee's first
  question: the theorem for n = 24 — none; stated.
- **Amoeba (Elie 5612):** control PASSES (8,570 frozen pinned discs; the amoeba fails on all — the instrument can
  fail). **Casey's rule as literally stated is not an algorithm: every failure is a two-vertex ping-pong.** With
  one added rule (no return to a color within a cascade): 3,492/3,762 at n = 22 (93%), every residual failure
  "tabu-exhausted" = exactly where Kempe's structure re-enters. **Lookback ≤ 4 on everything measured;** the
  amoeba does eat vertices with no uncolored neighbor (~40% of runs reach depth ≥ 2, never 5). Potential #9
  measured non-monotone. n = 24 still running.
- Third counter collision of the day (Grace/Elie, same second) — the claim-file rule needs a lock, not a read.

# 1. Rulings
- H-suff is a LEMMA CANDIDATE with a clean control; Lyra derives it first (pair-specific containment ⟹ exit).
  H-exist is an EXISTENCE statement (93/93) and stays measured until the type table (Lane F) makes it finite.
- The middle-orbit exits are a second, undiagnosed mechanism (432 of 741 without containment). Not a lemma,
  not an amendment: a residue to be typed.
- Casey's window rule (11:1x: "drop the vertex of the last-chosen color farthest along the frontier path; keep
  the color counts equal") is a bounded-memory BALANCED-WINDOW automaton; frozen as stated; runs as amoeba v3
  beside v2 + a Kempe eat rule. Its design intent — a rare color is likely free at the frontier — is testable.

# 2. LANE F — THE TYPE TABLE ("no new complexities," made precise; the finite half of Casey's shape)
Grace's collapse, Cal's "one name, two chains," and the tunnel are all statements about how Kittell's eight
chains INTERSECT. Define the TYPE of a stuck configuration = the intersection pattern of its eight link-seeded
chains (the 8×8 0/1 matrix of shared vertices; refinement: intersection sizes; whether an intersection is a
single vertex or a path). Finitely many types. **Question (two instruments, Grace rank / Elie BFS): is "locked"
a function of type? Is the exiting orbit a function of type?** Population: all in-frame stuck colorings n ≤ 22
(374,658) + the 93 + the matched sample. Pre-score: a function of type ⟹ the finite table exists — H-exist by
type is a finite check and H-suff by type a derivation; the proof's finite half in Casey's sense, and the
image-collapse feature is its shadow. Not a function ⟹ the type is insufficient and the residue names what
global datum matters (chain geometry beyond intersection). The linearization: a configuration → an 8×8 matrix;
lock = a property of the matrix; "no new complexities" = finitely many matrices. This is the corpus's Kittell
object (T2593) read as a grading.

# 3. What the day owns at 11:2x, honestly
Derived: L, D, T, Copy-Path, the wall, Boundary-Term (exact), Kittell Alias (with the seed-rule caveat), Birkhoff
A5, the cut's two types, the Necessity Lemma. Measured with a clean control: H-suff and H-exist. Measured: depth
2 through n = 23 (1.59M); the union procedure; the amoeba v2 at 93% with lookback ≤ 4; the image collapse at
locks. Dead today, all pre-registered: OWL, non-recurrence, potentials #6–#9, bare H_cut, "moving the middle
color" as the mechanism. The theorem for n = 24: none. Kittell 1935 (Bull. AMS 41:407–413, "A group of
operations on a partially colored map") is the primary source for the alphabet and the impasse group; cite it,
not Gethner's restatement.
— Keeper

**NAMING POINTER 12:41 (K1846, Cal §824):** every 'lock' / 'two-word-locked' in this artifact means COMMUTATOR-LOCKED AT DEPTH ONE — relative to the fixed-seed 186-menu (link seeds only). 27/349 have a plain Kempe swap exit seeded off the link; Kempe's pairing inserts on 2. Not a property of the Kempe landscape. Verdicts unchanged; the noun is corrected here, not silently.
