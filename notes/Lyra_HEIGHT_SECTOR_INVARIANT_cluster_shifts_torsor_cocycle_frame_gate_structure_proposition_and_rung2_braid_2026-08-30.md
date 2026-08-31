---
title: "U2+U3 — the dynamical lanes braided: cluster-shift representation (a Kempe swap is a constant height shift on its cluster), the height-sector invariant as the ℤ² lift of the whole GF(2) theory, the torsor-cocycle frame with its fork-conditional shapes — and the Gate Structure Proposition (gates = conjugated singletons) with two instantly-testable predictions"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 18:05 EDT at round start)"
status: "ROUND 12, LANES U2 and U3. One representation proposition (sketch-proved, flagged for the standard-literature cross-check); one invariant definition; one structure proposition with two pre-registered instant tests on STORED data; rung 2 of Gate Existence stated as a reduction. Nothing banks."
---

# U2 — THE HEIGHT-SECTOR INVARIANT (the torsor-cocycle lane, now with the dictionary under it)

## 1. Cluster shifts (proposition, sketch-proved)

**Proposition CS.** In height coordinates, a Kempe (p,q)-swap on cluster S adds a CONSTANT
lattice vector T (depending on the pair and gauge) to h on S, and fixes h elsewhere.
*Sketch:* interior edges of S keep their labels (both endpoints shift by g = p+q), so
h-differences within S are unchanged — the increment is constant on S; edges crossing ∂S change
labels exactly per Straddle-Flip, whose mod-2 trace is the sign-toggle we proved in round 3. ∎
(This is the standard cluster-move representation in the height literature — the cross-check to
Peled–Spinka conventions is flagged, not load-bearing.)

**Corollary (the unification).** The GF(2) sign-coset theory is the MOD-2 SHADOW of the height
theory: sign patterns = heights mod 2, straddle toggles = cluster shifts mod 2, W-cosets = the
mod-2 image of height sectors. Everything we built this week was the reduction of one ℤ²
object.

## 2. The invariant

For completions of a fixed pinning (boundary walk fixed by R-rel + gauge):

  **I_h(f) := [h_f] ∈ (height fields over the fixed boundary walk) / ⟨available cluster
  shifts, accumulated along walks⟩.**

Well-defined by construction; the ℤ² lift of the GF(2) fiber; Gaps A (spanning) and B
(throughput) lift verbatim. What is genuinely new at ℤ² resolution: shifts carry LATTICE VECTORS,
not parities — two moves that cancel mod 2 can accumulate in ℤ² (a corridor for invariants the
GF(2) lens provably cannot see, which is exactly what Theorem 4 demands).

## 3. The torsor-cocycle frame (fork-conditional, as routed)

Completions of a pinning sit inside an affine space of height fields; Kempe classes are orbits
of state-dependent constant shifts; the obstruction to transitivity is a cocycle on the
availability groupoid valued in the shift lattice. The fork (V1) picks its shape:
- **Phase fork ⟹ sector torsor:** the residual invariant is a FINITE global datum (which rigid
  phase the interior crystal sits in) — a torsor over the crystal's symmetry; the cocycle is a
  boundary-to-interior holonomy.
- **Defect fork ⟹ localized cocycle:** the invariant is a positioned class (where the bounded
  defect sits modulo shift reach) — nearer to the dislocation physics of the KT import.
Either way the invariant is dynamical in exactly the sense the verdict of record requires — it
reads availability, not statics — and the disc computes it exhaustively.

# U3 — GATE STRUCTURE AND RUNG 2 (the braid)

## 4. The Gate Structure Proposition (with two instant tests on stored data)

**Proposition GS (candidate).** Every gate word is equivalent to a CONJUGATED SINGLETON SHIFT:
w = α σ_u α, where α is a single swap whose effect is to make vertex u a singleton (x,y)-cluster,
and σ_u shifts it. (Lab-1's collapse mechanism was exactly this — α merged b's surroundings so
the final move vanished; the net effect was σ_b in conjugated clothing.)

Two pre-registered predictions, both checkable TONIGHT against the 186+ stored gate words, no
new instrument:
- **GS-1:** each stored gate word factors as ασα (up to the involution identities) — report the
  factorization census.
- **GS-2 (the sharp one):** gate net-support vertices are ALWAYS of EVEN degree — because a
  singleton (x,y)-cluster at u requires u's link properly 2-colored, impossible at odd degree
  (the no-local-rotation lemma). Any stored gate whose support vertex is odd-degree REFUTES the
  proposition as stated and demands conjugation depth ≥ 2 — a clean, cheap kill.

## 5. Rung 2 of Gate Existence — the reduction, braided from both ladders

If GS holds, Gate Existence reduces to: **at every stuck insertion configuration there is an
even-degree vertex u near the link and a single swap α after which u is a singleton cluster.**
The height ladder now carries the load: an insertion configuration is an UNPINNED puncture — no
tilt, hence (by the dictionary) the local height profile is NOT extremal — so some vertex near
the link admits a minimal height rearrangement; GS says one preparatory cluster move exposes it.
The Collapse Law's cut condition, previously assumed, becomes DERIVED: the "cut" is the
preparation α that empties the far side. Rung 2's honest remaining obligation, named: prove
"non-extremal ⟹ singleton-after-one-preparation within bounded radius" — a local height
argument on a 5-cycle-bounded patch, finite case analysis, exactly the kind that has held all
day. With the census (which templates fired) and GS-1/GS-2's verdicts, rung 3 is a finite
enumeration away.

## 6. Order of battle

GS-1/GS-2 tonight (stored data) → fork verdict shapes U2's cocycle → crystallization glance
(U1) confirms or reshapes the wall mechanism → rung-2 local height lemma next session with all
three verdicts in hand. U4 (paper v0.4) deliberately WAITS for the fork and slope-v2 — a moving
target absorbed is an erratum owed; the KT/dipole discussion paragraph is drafted into v0.4 at
the same edit.

— Lyra. One object, three resolutions, two ladders braided into one wall — and the gate, which
we met as a measured miracle at 739/739, may be nothing but a singleton wearing a conjugation.
Two glances at data we already hold will say so before midnight.
