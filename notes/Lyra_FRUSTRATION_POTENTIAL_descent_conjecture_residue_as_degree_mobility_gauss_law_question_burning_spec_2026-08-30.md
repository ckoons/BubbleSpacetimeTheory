---
title: "M1+M2+M4 — the frustration potential formalized (kinematic vs dynamic cost, Descent Conjecture in can-fail form); the residue ladder as DEGREE MOBILITY with a Gauss-law question; and the burning correspondence pinned for Z3"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 12:41 EDT at round start)"
status: "ROUND 6, LANES M1, M2, M4. Conjectures pre-registered, can-fail; falsifiers named per section (Z2, Z3, Z4, Y1 check-fields). Nothing banks."
depends_on: "SNF module spec + Charge Quantization theorem (round 5); Y1/Y2 results (board Round 76); Cal §786 realizability-gap construction drawings"
---

# M1 — THE FRUSTRATION POTENTIAL, FORMALIZED

## 1.1 Two costs, kept apart (Cal's realizability gap, built into the definitions)

Fix G and apex v. On the invariant fiber (colorings with equal ι):
- **Kinematic cost** κ(ω, ω′): minimum word length expressing ω′ − ω in columns of the SUPERSET
  matrix M_G (formal application, realizability ignored). A genuine metric on the fiber lattice;
  computable; a LOWER-bound object.
- **Dynamic cost** δ(f, f′): Kempe-BFS word length — the real thing. Always κ ≤ δ.
Z2's measured realizability gap is exactly the κ-vs-δ discrepancy at lattice level; every claim
below states WHICH cost it uses.

**Frustration at the apex:** Φ(f, v) := κ(ω(f), Ω_free(v)), where Ω_free(v) := {ω(f′) : f′
proper, v's link misses a color} — the kinematic distance from f's charge state to the
freed-link-compatible set. (Ω_free is defined by image, not by a formula; on gallery graphs it
is enumerable. A formula characterizing it is a named open sub-problem — the freed-link charge
characterization.)

## 1.2 THE DESCENT CONJECTURE (pre-registered, can fail)

- **DC-1 (gate descent):** from any stuck f, some available gate (X3's one-vertex commutator)
  strictly decreases Φ; an optimal rescue can be realized gate-by-gate, one quantum per gate.
- **DC-2 (no dynamic surcharge):** depth(f, v) = Φ(f, v) — the realizability gap, whatever it is
  latticewise (Z2), VANISHES on the distance-to-freed functional.

Calibration pins:
- **Zero point:** icosahedron — Φ ≤ 1 everywhere (rescue ≤ 1, single fiber, PC4 passed).
- **Calibration pair:** T_3 ≡ Errera. They agree in ALL linear data (rank 11, [2¹⁰,4], same
  Δ-residues) and in depth (3). Since Φ is a linear-data functional, Φ(T_3) = Φ(Errera)
  automatically — the three-level twinning is the first nontrivial consistency check DC-2 passes
  for free, and it is evidence, not proof.
- **Stress case:** Kittell — DC-2 predicts Φ = 4 for its depth-4 colorings. This is the
  computation most likely to kill DC-2 (my round-5 registration already names Kittell the first
  counterexample risk for GC-I; the two risks are the same risk).

Falsifiers: Z4 directly (identical linear data, different depth kills DC-2 by construction);
Z2 (a large lattice-level gap makes DC-2's exactness implausible and demands the surcharge be
characterized); Y2's census re-read gate-by-gate (any stuck f where NO gate decreases Φ kills
DC-1).

# M2 — THE RESIDUE LADDER 6 / 2 / 0: DEGREE MOBILITY

## 2.1 What the residue measures

r(G) := gcd of achievable Δdeg (degree units; gcd{0} := 0). Then deg mod r is the surviving
conservation law, and **r is the graph's DEGREE MOBILITY — the quantum by which chain currents
can pump the topological degree.** r = 0: degree FROZEN (perfect conservation); r = 2: degree
moves in steps of 2; r = 6: in steps of 6. Mohar–Salas is the statement r ≡ 0 (mod 12) on
Eulerian graphs. (Graph-to-residue assignment below awaits Elie's table read; the note's
interpretation does not depend on which graph holds which rung, only the Fritsch/0 line, which
the board states.)

## 2.2 Fritsch r = 0 is a theorem-shaped fact demanding a mechanism

gcd{0} = 0 means EVERY column has Δdeg = 0: **every Kempe chain on Fritsch has sign-balanced
boundary** (Σ_straddle z = 0 for every chain of every proper coloring). A non-Eulerian graph
conserving degree EXACTLY — a second conservation mechanism, geometric rather than parity-based:
- Eulerian conservation (Fisk/M–S): parity mechanism, mod 12.
- Balanced-boundary conservation (Fritsch): exact, mechanism UNKNOWN. That is the clue the round
  assignment flagged, and here is its can-fail form: **check in existing Y1 check-fields that
  all Fritsch columns are individually zero (strong form)** — if instead nonzero columns exist
  in some population corner, the gcd convention is doing hidden work and this section re-opens.

## 2.3 The Gauss-law question (registered as a question, not a claim)

For a chain S with straddle sums A (1-in faces) and B (2-in): Δdeg = −½(A+B), and the enclosed
charge is Q_S = A + 2B + 3C (C = 3-in sum). Heawood gives A + 2B ≡ 0 (mod 3). **Question: for a
chain with a single boundary cycle, is A + B determined (mod a fixed modulus) by the enclosed
charge Q_S and the boundary length?** If yes, degree mobility is literally a Gauss law — the
current through a boundary reads the charge inside — and r(G) becomes computable from the charge
landscape without enumerating swaps. Empirical test is nearly free on Y1's stored columns
(each column already carries its straddle set and Δdeg; add Q_S per column). If no clean
relation appears, the null banks and the mobility stays an empirical ladder.

## 2.4 Mobility vs depth (pre-registered reading, can fail)

If the ladder's assignment tracks depth (deeper ⟹ larger r), the reading is: high mobility ⟹
degree flows freely ⟹ fibers merge ⟹ LINEAR invariants explain less ⟹ stuckness on deep graphs
is less linear-visible. This aligns independently with Kittell's coarse factors ([2²⁰, 8]) and
with both of my Kittell risk registrations. Falsifier: any assignment where r anti-tracks depth
kills the reading; either way the ladder gets a mechanism sentence instead of a mystery.

# M4 — THE BURNING CORRESPONDENCE, PINNED FOR Z3 (before the run)

Root: **the apex v** (the insertion site), pinned. Monotone burning (burned set only grows).
Two candidate rules, both run, divergence is data:
- **Rule A (charge-weighted):** u burns when #burned neighbors ≥ θ_A(u) :=
  ⌈(deg(u) − |3ω(u)|)/2⌉ — frustrated (high-|charge|) sites resist burning.
- **Rule B (parity):** θ_B(u) := ⌈deg(u)/2⌉ + [deg(u) odd] — odd sites resist by parity alone.
Outputs per witness: firing rounds to full burn; unburned-core size if stalled; both compared to
the 5/10/17 radius-3 ladder and to measured depth. **Specificity control (mandatory, Cal's
broken-control discipline): re-run from a wrong root (antipodal vertex); the correspondence must
DEGRADE or the count is decorative and the conjecture dies regardless of the right-root fit.**
My registered conjecture stands as stated in round 5: the radius-3 odd-charge ladder is a
burning count in disguise; Rule A is my committed candidate, Rule B the control alternative.

— Lyra. A potential with two honest price tags, a ladder that finally says what it is a ladder
OF, and a burning rule that has to fail from the wrong root before anyone may celebrate it
passing from the right one.
