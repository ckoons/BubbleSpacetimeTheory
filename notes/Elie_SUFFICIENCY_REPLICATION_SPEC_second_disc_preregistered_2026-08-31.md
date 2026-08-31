---
title: "SUFFICIENCY REPLICATION SPEC — the three-legged characterization goes to a second disc (pre-registered before construction), plus the exhaustive backfill on the home disc"
author: "Elie"
date: "2026-08-31, Monday (clock-verified 08:03 EDT)"
status: "ROUND 18. SPEC ONLY — nothing here runs today. Predictions filed BEFORE any second-disc object is built. Construction tomorrow. Nothing banks."
---

# What is being replicated

Toy 5560 (with 5557's Gauss law and 5559's wall dichotomy) closed FCW-014's census on:

**FROZEN <=> FILLER and FLUX-NEUTRAL and EXACTLY-TWO-COMPLETIONS** (each leg necessary,
jointly sufficient, on all 5,002 census rows).

Status: candidate — one disc, n = 15 target family. This spec is the factory for the
cross-object test, pre-registered per the commit-the-checker-half-blind discipline: every
choice below (objects, census rule, definitions, predictions, kill conditions) is fixed
TODAY; the first construction run happens TOMORROW. No knob survives contact with the data.

# R0 — the exhaustive backfill on the home disc (closes a sampling caveat)

FCW-014's atlas (Q2, toy 5537) is a SAMPLE: 5,000 uniform proper 12-cycle sequences
(seed 20260830) + the two known twins, out of 3^12 + 3 = 531,444 proper cycle colorings.
The "5002/5002 biconditional" is therefore sample-scope. R0: enumerate ALL 531,444 proper
boundary sequences of FCW-014, compute the availability graph per pinning (Y4/Q2 machinery
unchanged), and re-score the biconditional exhaustively. Pre-registered outcomes:
- R0-P: the biconditional holds exhaustively (the 15 may grow to the full frozen set; every
  frozen row must carry all three legs, every three-leg row must be frozen).
- R0-K (kill): any frozen pinning outside the three legs, or any three-leg free pinning.
  Either way the home disc's answer stops being sample-scope.

# FCW-016 — the second disc: candidate ladder, gate, and census rule

Second geometry = a triangular-lattice patch that is NOT the hexagonally symmetric radius-2
disc. Ladder, tried in order (all axial-coordinate patches, hex adjacency, boundary walked
as a cycle exactly as Y4.disc does):

- **L1 — parallelogram P(4,2)**: {(q,r): 0 <= q <= 4, 0 <= r <= 2}. V = 15, boundary
  cycle 12, interior 3. Exhaustive census = 531,444 sequences (same count as R0).
- **L2 — parallelogram P(5,3)**: {0 <= q <= 5, 0 <= r <= 3}. V = 24, boundary cycle 14?
  (computed at build; must be EVEN for the filler leg to be well-posed; if odd, skip).
  Census exhaustive if <= 5M sequences, else the Q2 sampling rule with seed 20260831
  and >= 20,000 rows.
- **L3 — trapezoid/triangle patch T(5)** (side-5 triangular patch, corners trimmed if
  needed for an even boundary): same rules.

**Instrument-validity gate (before any prediction is scored):** the chosen object must
exhibit BOTH (a) at least one frozen pinning (multi-component availability graph) AND
(b) at least one filler flux-neutral pinning with >= 3 completions. If (a) fails the
object cannot test necessity (positive control absent — a search that cannot succeed
proves nothing); if (b) fails the sufficiency direction risks vacuity. First ladder
object passing the gate = FCW-016. If the whole ladder fails the gate, THAT is the
finding (freezing may require the hexagonal symmetry — report, do not force).

# Definitions ported verbatim (no re-derivation at build time)

- **filler**: one color occupies an entire parity class of the (even) boundary cycle.
- **flux-neutral**: 2·Area(boundary height walk) = 0, walk built with V1's STEP map and
  the checkerboard sigma from H8.orient_faces'd faces (the J1 lesson: UNORIENTED faces
  manufacture false monodromy — orient first, always).
- **Gauss law (P3 below)**: 2·Area = −Σ z_t per completion (5557's exact identity).
- **exactly-two-completions**: the pinning admits exactly 2 proper completions.
- **frozen**: availability graph = 2+ isolated all-frozen nodes (Q2's ALL-FROZEN class).
- **junction face**: a face whose 3 vertices carry 3 distinct height-difference values
  (5559's object), computed per completion pair.

# Pre-registered predictions (scored X/Y at build; both directions pre-scored)

- **P1 (necessity replicates)**: on FCW-016, every frozen pinning is filler AND
  flux-neutral AND exactly-two-completions. KILL: one frozen counterexample names the
  leg that is FCW-014-specific.
- **P2 (sufficiency replicates)**: every filler + flux-neutral + two-completion pinning
  is frozen. KILL: one free three-leg pinning — the characterization loses sufficiency
  off the home disc.
- **P3 (Gauss law is geometry-generic)**: 2·Area = −Σ z_t on EVERY completion of EVERY
  pinning tested (not just fillers). KILL: one violation — the identity picks up a
  geometry-dependent term (report the residue's shape).
- **P4 (wall dichotomy replicates)**: among two-completion pinnings, junction faces
  occur ONLY on frozen pairs. KILL: a free twin wall with a junction, or a frozen wall
  without one.
- **P5 (exploratory, NOT scored)**: filler confinement to a distinguished interior
  vertex — FCW-014's fixed center has no analogue on an asymmetric patch; observed
  structure is logged, no prediction made (target-innocence: we do not know what "center"
  means here, so we refuse to guess one after seeing the data).

Scoring: P1–P4 each X/Y over their populations; the headline is the four-way verdict,
not any single row. A partial replication (e.g., necessity holds, sufficiency fails) is
data — the standing lesson says deviations locate boundaries.

# Runtime plan (so tomorrow starts mid-stride)

R0: ~531k availability graphs, est. 10–30 min (memoized completions; batch by prefix).
L1: same count, 3 interior vertices — cheaper per row than R0. Both fit one morning.
Toys: R0 and FCW-016 census are separate toys (claim two numbers); predictions above are
their test lists, verbatim.

— Elie. The factory is specced with the blinds down; tomorrow it runs with no hands on
the dials.
