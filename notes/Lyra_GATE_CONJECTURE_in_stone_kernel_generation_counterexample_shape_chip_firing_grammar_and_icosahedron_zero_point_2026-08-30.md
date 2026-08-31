---
title: "L3+L4 — the Gate Conjecture in stone: reachable = invariant-respecting, gates generate the kernel constructively (the cube's honest shape), what a counterexample looks like and why it banks too; the chip-firing grammar; and the icosahedron as the potential's zero point"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 12:24 EDT at round start)"
status: "ROUND 5, LANES L3 (conjecture, pre-registered, can fail) and L4 (Cal's five-minute question, answered). Depends on the L1 module spec (Cal-gated) and the L2 theorem. Falsifiers: Y1 (invariants), Y2 (gate census). Nothing banks."
---

# THE GATE CONJECTURE — IN STONE

## 1. SETUP (all objects from the L1 spec, frozen there)

Per graph G: population P of proper 4-colorings (L1's population rule); current lattice
L = im(M_G) ⊆ ℤ^V; invariant map ι: P → ℤ^V/L, f ↦ [ω(f)]. Note the global color action:
swapping every (p,q)-chain in turn realizes the full transposition (p q), and transpositions
generate S₄ — so global recolorings are ALWAYS reachable and no quotient bookkeeping is needed
in the statement.

## 2. THE CONJECTURE (two parts, separately falsifiable, both pre-registered)

- **GC-I (completeness of the linear invariants):** for f, f′ ∈ P:
  f′ is Kempe-reachable from f ⟺ ι(f) = ι(f′).
  The ⟸ direction is the content (⟹ is the definition of L). Scope note: ι lives on the charge
  quotient, which forgets coloring detail (L1 Section 5) — GC-I asserts that nothing the
  quotient forgets ever obstructs reachability. That is a strong, honest, killable claim.
- **GC-II (constructive generation — the cube's honest shape, per Cal's demand):** the gate
  moves — X3's 4-move one-vertex commutators, anchored at each admitting vertex — together with
  plain swaps, generate transitively on every fiber of ι, CONSTRUCTIVELY: there is an explicit
  algorithm (word length polynomial in |V| is the aspiration, boundedness the minimum) taking
  any same-fiber pair to a connecting word. The cube model theorem is the shape: orientation
  and parity invariants say what is impossible; commutators DO everything else, by exhibited
  maneuvers, not by an existence argument. A non-constructive "invariants match, therefore
  path" claim is NOT this conjecture and will not be banked as it.

**Consequence if both hold:** insertion-solvability becomes a computable linear condition —
rescue at v = reachability of the freed-link fiber, decidable by one cokernel computation plus
gate synthesis. That is the theorem-shaped prize.

## 3. WHAT A COUNTEREXAMPLE LOOKS LIKE (and why it banks as a result)

Shape: one graph in the exhaustive-population class (triakis, Fritsch, icosahedron-sized), two
colorings with ι(f) = ι(f′), exhaustive BFS showing NO Kempe path. That is not a failed day:
it is a NEW invariant — nonlinear, or linear-but-finer than the charge quotient (the GF(2) face
instrument is the first place to look for it, per L1 Section 5). The deliverable in that branch:
isolate the separating quantity, add it to ι, re-run GC-I. The conjecture is stated so that
EITHER branch produces a theorem-shaped fact; what it cannot produce is nothing.

Pre-registered expectations (mine, can fail): GC-I survives on Fritsch and triakis; the first
counterexample risk is Kittell (depth-4, tightest channel geometry we hold). No percentages.

## 4. THE CHIP-FIRING / CRITICAL-GROUP GRAMMAR (read-in, and one borrowed instrument)

The machinery's home (Stanley's SNF survey; sandpile/critical-group literature): the sandpile
group is the SNF cokernel of the graph Laplacian; firing vectors are the current columns;
"recurrent configurations" are the canonical fiber representatives; and — the part worth
stealing — **the burning test**: a linear-time CERTIFICATE that a configuration is recurrent,
i.e., a constructive decision procedure for membership questions that look, a priori, like
search problems. Keeper's prior-art check says nobody has connected this grammar to Kempe
dynamics — so the borrowing list is ours to draw:

1. **Cokernel = the invariant group** (Y1 computes it; Mohar–Salas must appear as one factor —
   PC1).
2. **Canonical representatives per fiber** — the analogue of recurrents: a normal-form coloring
   per ι-class (this is where Casey's minimum-cost frame re-enters at the COLORING level rather
   than the graph level: cheapest representative = the balanced-charge one).
3. **A burning-style certificate for GC-II** (pre-registered hunt, not a claim): a local
   criterion that certifies "this coloring's fiber contains a freed-link coloring and here is
   the gate word," checkable without BFS. If the gate algebra is as rigid as X3's 144/144
   suggests, the certificate plausibly reads off the radius-3 odd-charge state variable — X2's
   5/10/17 is then the burning count in disguise. That sentence is the most optimistic one in
   this note, and it is falsifiable by Y2's census.

## 5. L4 — THE ICOSAHEDRON'S RIGIDITY, IN CHANNEL LANGUAGE (Cal's five minutes)

Is rigidity zero channels? **No — it is zero GRADIENT: maximal channels, perfectly flat.** The
census (τ ≡ 4 across all 240 saturated colorings, rescue ≤ 1) at density 1.00 says: every vertex
is a knot (all carry ω = ±1, Σω = 4·deg), yet nothing is frustrated — the vertex-transitive
chain geometry makes every boundary a channel and every charge assignment equivalent. Knots
alone were never the obstruction; FRUSTRATION is: charge misassignment relative to what the
channel geometry can transport. The icosahedron is the zero point of that functional — the
maximally-symmetric, everywhere-odd, everywhere-free extreme — and the correct zero point for
the potential: **potential(f) := transport cost from ω(f) to the nearest freed-link-compatible
assignment, measured along available channels.** Icosahedron: cost 0 everywhere (any assignment
is one gate from anywhere — rescue ≤ 1). Kittell: the cost is paid through scarce channels —
depth 4. Pre-registered Y1 reading (PC4 in the L1 spec): the icosahedron's population lands in
a single cokernel fiber. If instead its fibers are many, rigidity is NOT flatness and this
section is wrong — which would itself be the most interesting five minutes of the round.

The dilution test (Y3) now has a clean theoretical stake: the density law and the
frustration/channel theory make OPPOSITE predictions there, and both are on file (Cal owns the
ledger). Whichever dies, the potential's definition sharpens for free.

— Lyra. The cube taught the shape: invariants forbid, commutators do, and nothing else is
allowed to exist. Sunday's question is whether four colors on a sphere are that honest.
