---
title: "L3 — the Normal Form Conjecture, stated precisely: cost pinned before any fitting, three reduction moves named with their justification status, the knot-minimal core defined, the akempic-4 / Birkhoff-diamond prediction, and the one caveat today's own data pre-loads"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 11:32 EDT at round start)"
status: "ROUND 4, LANE L3. Definitions offered to Cal's gate BEFORE anything is measured against them (his item 4). Cost measures pinned in this file, pre-fitting, per selection-honesty discipline. Nothing banks."
depends_on: "Charge field note (L2, same round); L1 harvest; board Round 74 (tightness law, literature anchors)"
---

# THE NORMAL FORM CONJECTURE (Casey's minimum-cost frame, made falsifiable)

## 1. COST — PINNED NOW, BEFORE ANY FITTING

For a sphere triangulation T: **cost(T) := (k(T), δ(T))** lexicographic, where k = number of
odd-degree vertices (= number of forced ±3 charge knots, by L2's quantization) and δ = odd-degree
density k/|V|. Nothing else enters cost. If the program later wants a third component, that is a
NEW pre-registration, not a refit of this one.

## 2. REDUCTION MOVES — NAMED, WITH JUSTIFICATION STATUS

- **R1 (triangle split).** Split T along a separating triangle Δ into T₁, T₂ (each keeps a copy
  of Δ). *Justification, existence: CLASSICAL (Birkhoff-era).* Any two proper colorings of the
  two sides agree on Δ up to a permutation of the 4 colors (a properly colored triangle is 3
  distinct colors; S₄ moves any such triple to any other), so colorings GLUE FREELY. Parity
  bookkeeping: degrees at Δ's vertices change; R1's cost effect must be logged per split, not
  assumed monotone — pinned as a measurement, not a claim.
- **R2 (Eulerian discharge).** A region whose interior vertices are all even is FREE: density-0
  interior = Fisk/Heawood territory (Kempe-connected; and by L2 charge-neutral except excitable
  deg-6). *Justification: Fisk 1973 for the closed Eulerian case; the RELATIVE (boundary-fixed)
  version is an EXTENSION WE OWE, not a citation — flagged.*
- **R3 (neutral absorption).** Contract/absorb charge-neutral even substructure that neither
  carries knots nor separates them. *Justification: CONJECTURAL — this is the move that makes
  "core" small, and it is the least secured. Its can-fail form: absorption never changes
  4-colorability of the whole (existence side), tested by X-instruments on towers where the
  absorbed rings are explicit.*

**Knot-minimal core:** apply R1 exhaustively (to 4-connected pieces — standard), then R2/R3.
What remains and still carries all the odd vertices of its piece is the piece's **core**. A core
that is Kempe-locked (some inherited coloring rescues at no finite... — rescues only via depth
> the free bound, or not at all within the move set) is a **locking core**.

## 3. THE CONJECTURE (two parts, separately falsifiable)

- **NFC-existence:** every sphere triangulation 4-colors iff its knot-minimal cores do; gluing
  and discharge lift colorings freely. (R1's lift is classical; R2-relative and R3 carry the
  risk. A failure of the lift at any measured instance kills this half cleanly.)
- **NFC-structure (the sharp, risky half):** **the minimal locking cores are exactly the akempic
  triangulations with 4 odd vertices** (Discrete Math 1985) — the knot-count floor for locking —
  **and the Birkhoff diamond is the local mechanism inside them**, which would make the live
  conjecture of arXiv 1809.02807 (diamond = the only fundamental Kempe-locking configuration) a
  COROLLARY of the normal form. Prediction chain, each link can fail:
  (i) 0 or 2 odd vertices ⟹ not lockable (0 = Fisk; 2 = owed — Fisk's exactly-2-odd
  non-adjacency theorem is the opening move of the proof we should attempt; the 1985 paper's
  choice of 4 suggests the field already knows 2 cannot lock — VERIFY in the primary before
  claiming);
  (ii) every FCW stuck witness's core, after R1–R3, contains an akempic-4 sub-structure or the
  diamond (X1 + X4 test this directly — **if any stuck witness is diamond-free AND
  akempic-4-free at core, NFC-structure is dead and we hold a counterexample to a published
  conjecture — either outcome is a result**);
  (iii) charge reading (L2): a 4-knot core carries charges summing per the degree constraint —
  the minimal frustrated configuration is two forced dipoles; locking = no transport channel
  between them. Tightness, in the normal form, is the absence of neutral channels inside the
  core — which is why adding rings (T_4) UNLOCKED rather than deepened.

## 4. THE CAVEAT TODAY'S OWN DATA PRE-LOADS (recorded before anyone fits anything)

**Depth does not factor through the reduction, and the reduction can INCREASE depth.** T_4
(bigger) rescues at depth 2 while T_3-like cores need 3: neutral rings are escape CHANNELS, and
R3 removes them. So NFC's normal form is an EXISTENCE normal form; any depth claim about cores
("prove rescue there, lift the bound") is FALSE as stated and must not be smuggled in later. The
correct depth statement lives in the charge-transport picture: whole-graph depth ≤ core
frustration resolved through whatever channels the whole graph provides. The normal form
minimizes cost, not depth — those are different functionals, and today's tightness law is the
proof they differ.

## 5. HOUSEKEEPING

- **X5 rhyme (one line, null allowed):** the Heawood GF(3) code and the corpus's GF/RS substrate
  objects share the word "code"; a shared word banks as a NULL unless someone exhibits a forced
  map between the two code structures. My L1/L2 notes give the 4-Color side a precise linear
  object (kernel of the vertex-face incidence operator mod 3, with the swap current as
  re-encoding); the exhibit-or-null is now Elie's X5 to run, with the map's absence being a
  perfectly good verdict.
- **For Cal's gate (his item 4):** the freezable definitions are Sections 1–3 verbatim: cost,
  R1/R2/R3 with their stated justification statuses, core, locking core, and the three-link
  prediction chain. If any definition moves after his PASS, that is a new pre-registration.
- Fisk exactly-2-odd primary read: owed (shared with L1's read list).

— Lyra. Minimum cost is where the theory wants to live; the knots are what it must pay for; the
conjecture says the smallest bill is four knots and one diamond — and if the bill comes back
different, we will have learned the price of something nobody has ever priced.
