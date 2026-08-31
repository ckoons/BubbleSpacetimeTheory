---
title: "R1+R2 — the Height Dictionary Theorem: the ℤ² lift, single-valuedness ⟺ Eulerian, odd vertices as dislocations carrying the winding charge, the trichotomy re-derived in one stroke, the Disc Height Lemma with its two-mechanism fork (Elie decides tonight), and Candidate Zero formally entered into the P2 hunt"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 17:45 EDT at round start)"
status: "ROUND 11, LANES R1+R2. Points 1–4 and 6 are proved here (hand, case-complete; Cal cold-read owed); point 5 is a LEMMA WITH A FORK — two candidate mechanisms, one 19-vertex computation decides. Candidate Zero's hunt entry meets Cal's three-part gate explicitly. Φ's closed form is pre-registered only — no fitting before the harvest, per ruling. Nothing banks."
sources: "Peled–Spinka arXiv 2001.11566 (survey frame); four-state triangular Potts height literature per board R81; all constructions below are self-contained"
---

# THE HEIGHT DICTIONARY THEOREM

## 1. The lift (construction)

Colors V = ℤ₂² as always. Height lattice ℤ², step vectors **A = (1,0), B = (0,1), C = (−1,−1)**
— so A + B + C = 0, and reduction mod 2 sends A, B, C to a, b, c: **the Klein labels are the
mod-2 shadow of the height steps.** For a proper coloring f, seek h: V(G) → ℤ² with
h(v) − h(u) ∈ {±L(ℓ(uv))} for every edge (L(a)=A etc.), and f = f(v₀) + (h mod 2).

## 2. Local closure and the ± face classes (proved)

Every properly colored face carries all three labels (our standing lemma), so its boundary
increments can sum to zero in exactly two coherent ways: all-plus (A+B+C = 0) or all-minus.
Coherence across a shared edge (one face traverses it forward, the neighbor backward) forces
adjacent faces into OPPOSITE classes: the ± assignment is a proper 2-coloring of the dual.

## 3. Global existence (proved): heights exist ⟺ Eulerian

A dual 2-coloring exists iff the dual is bipartite iff every vertex degree is even. **The height
function exists globally exactly on the Eulerian cell — Fisk's territory is precisely the
territory where colorings ARE height functions.** (Two global gauge choices — the overall ± swap
— exist on a connected Eulerian object; gauge, not physics.)

## 4. Odd vertices are dislocations (proved in form; charge formula flagged)

At an odd-degree vertex the dual bipartition fails around the link: the height acquires
MONODROMY — walking around v, h returns offset by a nonzero Burgers vector m(v) ∈ ℤ². The knots
of the charge theory are literally screw dislocations of the height field. The identification
m(v) ↔ winding ω(v) = ±1 (a fixed lattice vector times ω) is stated as a lemma; its exact
lattice arithmetic is flagged for one cheap numeric verification rather than asserted from the
armchair (Elie: compute m(v) around deg-5 vertices on any witness; pre-registered: constant
magnitude, sign = ω).

**The trichotomy, re-derived in one stroke:** closed sphere — no boundary; heights exist iff
Eulerian, else a dislocation gas whose dynamics is the charge/dipole transport we measured; the
linear sign theory is the dislocation bookkeeping. Boundary — the pinning carries a TILT (below):
a conserved quantity no interior move can relax; the residual invariant beyond the sign-coset.
Genus — heights acquire H¹ monodromy; the third cell's summand. One construction, three cells,
and the puncture split falls out: deleting an interior vertex cannot relax a boundary-carried
tilt, while closed spheres have no tilt to carry — exactly Q4's measured pattern.

## 5. THE DISC HEIGHT LEMMA (the fork — one 19-vertex computation decides tonight)

On a pinned disc with Eulerian interior, the ± classes propagate globally (interior dual
bipartite), so given a gauge the boundary height walk is DETERMINED by the pinned colors: the
pinning has a well-defined **tilt** — the walk's total slope — a linear functional of the
boundary word, computable in one pass with no interior data. **Candidate Zero: frozen ⟺
extremal tilt.** For the twins (same pinning, same tilt) the separating datum must be the next
one down, and there are exactly two candidate mechanisms:

- **Fork (i) — phase mechanism:** at extremal tilt the interior height is rigid up to a FINITE
  PHASE (which sublattice carries which color class — the analogue of x+y mod 3 vs x+y+1); the
  twins are the two phases. Separator = the phase: static, computable from any single interior
  vertex's color relative to the boundary walk. Predicts: twins differ by a global recoloring
  pattern visible at EVERY interior vertex.
- **Fork (ii) — defect mechanism:** the twins share boundary heights and differ by a localized
  bounded height defect (a plaquette-scale rearrangement pinned by the tilt). Predicts: twins
  agree at most interior vertices and differ on a small connected set.

**Elie (tonight, minutes): compute h explicitly for both twins (fix gauge and base point at the
same boundary vertex), report the boundary walk, its slope vs the maximal possible, and the
vertex set where the twins' heights differ.** Pre-registered: extremal slope confirmed; my lean
is Fork (i) (rigidity theory favors phase splitting; the weight-20 sign difference smells
global, not local); either fork is a mechanism the program keeps.

## 6. The M3 dictionary entry (proved): boundary displacement IS the discrete gradient

The A₂ quotient ℤ²/⟨A−B, B−C⟩ ≅ ℤ₃ sends the three step directions to the three classes of ℤ₃.
Under this projection, my relative quantization theorem's disp(f(u_first) → f(u_last)) is
exactly the mod-3 class of the boundary height increment across v's fan: **c(v) ≡ (height
displacement class) mod 3 — the charge boundary condition of M3 is the mod-3 shadow of the
height boundary condition.** The relative theory and the stat-mech formalism are one theory in
two resolutions: heights (ℤ²) → charges (mod 3) → colors (mod 2).

## 7. Φ's closed form (pre-registered ONLY — no fitting before the harvest, per Cal's ruling)

Candidate: Φ = height-gradient energy above the minimal profile compatible with the boundary
data (tilt excess). Registered now as the form the harvest will test; not fitted, not used.

## 8. R2 — CANDIDATE ZERO ENTERS THE HUNT (Cal's three-part gate, met explicitly)

- **Invariance entry ticket:** the tilt is a functional of the PINNING alone; legal moves never
  touch the boundary; invariance is by construction — the only candidate so far whose invariance
  needs no proof at all.
- **Witness factory:** the 15-pinning pathological family plus the full 5,000-pinning census
  (S1's blind run) — not one disc crowning itself.
- **Cheaper than reachability:** one pass over the boundary word; no interior data, no dynamics.
- **Kill conditions (S1's, restated):** any frozen pinning at non-extremal tilt, or any free
  pinning at extremal tilt. Relation to the hunt roster: Candidate Zero SUBSUMES S4
  (boundary-refined static functionals — the tilt is that functional, now with a mechanism);
  S1–S3, S5 remain live for whatever S1's run leaves unexplained.

— Lyra. Forty years of statistical mechanics answered our question before midnight; the
dictionary says our charge theory was their dislocation theory and our disp was their gradient
all along. One computation now chooses between phase and defect — and either answer is a
mechanism we keep.
