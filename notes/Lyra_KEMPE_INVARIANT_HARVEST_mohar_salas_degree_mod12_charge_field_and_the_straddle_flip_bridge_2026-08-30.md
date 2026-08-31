---
title: "L1 harvest — the known Kempe invariant is the degree of the coloring mod 12 (Mohar–Salas 2009, on Fisk's foundations); its scope excludes our gallery by hypothesis; Straddle-Flip computes its violation exactly, and the residue hunt is the new instrument"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 11:32 EDT at round start)"
status: "ROUND 4, LANE L1. Web-verified this session: Mohar & Salas, J. Phys. A 42 (2009) 225204 = arXiv 0901.1010 (title, venue, main theorem statement). Fisk I/II primary read still owed — the degree-of-a-coloring construction is stated here from the standard definition, flagged for primary confirmation. Nothing banks."
---

# L1 HARVEST — THE KNOWN INVARIANT, AND WHAT IT BECOMES ON OUR SIDE OF THE PARITY AXIS

## 1. WHAT THE FIELD HAS (verified statement)

**Mohar–Salas 2009 (arXiv 0901.1010):** for THREE-COLORABLE (= Eulerian = all-even)
triangulations of a closed oriented surface, **the degree of a 4-coloring modulo 12 is invariant
under Kempe changes.** Built explicitly on Fisk's algebraic-topology theory of colorings. Used to
prove WSK non-ergodicity on torus triangulations T(3L, 3M) — at least two Kempe classes.

**The degree.** A proper 4-coloring f of an oriented triangulation T is a simplicial map
T → ∂Δ³ ≅ S² (each face carries 3 distinct colors = one face of the tetrahedron). Each face maps
with an orientation sign — **and that sign is exactly our Heawood sign z_t** (the cyclic order of
the label triple is the pullback orientation). The degree is the signed face count over any one
target face; summing over all four target faces:

  **Σ_t z_t = 4 · deg(f).**

**Consequence: my "charge field" from the L2 note is the local density of THEIR degree.** The
charge c(w) = Σ_{t∋w} z_t is the degree density at w; Σ_w c(w) = 12·deg(f). We did measure the
dynamical shadow of Fisk's static theory, and the dictionary is now literal, not metaphorical.

## 2. SCOPE ANSWER TO KEEPER'S QUESTION — computable yes, separating no (as stated)

- **Is their invariant computable on our gallery? The QUANTITY, yes** — deg(f) is defined for any
  4-colored oriented triangulation, and E-instruments can compute it as Σz/4 with machinery
  already built (E4's sign vectors).
- **Does their INVARIANCE apply? No — by hypothesis.** The theorem's class is Eulerian; every
  stuck witness we hold is odd-rich (that is the round-3 density law). The field's invariant
  lives at the density-0 endpoint of exactly the axis E3 measured. It cannot separate stuck from
  unstuck on FCW because its conservation law does not hold there.

## 3. THE BRIDGE — Straddle-Flip computes the violation exactly (NEW, candidate)

Under a Kempe swap on chain S, Straddle-Flip gives z ↦ −z on straddling faces, so

  **Δdeg = −½ · Σ_{t ∈ straddle(S)} z_t.**

The degree is NOT conserved in general; the swap carries a computable **degree current** supported
on the chain boundary. Consistency check that doubles as a mini-lemma: Δdeg must be an integer,
and for a singleton chain S = {b} the sum is c(b) — half-integer violation would occur exactly
when c(b) is odd, i.e., at odd-degree b. **But odd-degree vertices have no singleton chains: a
singleton swap at b needs b's link properly 2-colored, and an odd cycle has no proper
2-coloring.** The obstruction to local rotation at odd vertices and the integrality of the degree
are the same fact. (General chains: integrality forces Σ_straddle z_t even; direct proof of
evenness for arbitrary chains is owed — one of the two proof debts of this note.)

On Eulerian triangulations Mohar–Salas says more: Δdeg ≡ 0 mod 12 under any swap. Our formula
must reproduce that (every chain-boundary sum ≡ 0 mod 24 there) — a nontrivial and FREE positive
control for the instrument: run the Δdeg meter on an Eulerian control and check ≡ 0 mod 12 per
swap. If it fails, the meter (or my sign convention) is wrong, not the theorem.

## 4. THE NEW INSTRUMENT — the residue hunt (pre-registered, can fail)

The invariant did not die at positive density; it DEGRADED. The question is by how much:

**For each gallery graph, compute the set of achievable Δdeg over all legal swaps from all
reachable colorings (BFS window as in the depth measurements), and take the gcd.** Call it the
**degree stiffness** δ(G).

- Eulerian controls: δ ≡ 0 mod 12 (theorem — positive control).
- Pre-registered prediction (mine, can fail): δ degrades with odd density but does NOT collapse
  to 1 immediately — **on the akempic-4 imports (X4) and the Birkhoff-diamond cases (X1), a
  nontrivial residue survives (δ ∈ {2, 3, 4, 6}), and stuck configurations sit in residue classes
  that unstuck ones cannot reach.** If true: a NEW Kempe invariant at minimal positive density —
  the interpolation between Fisk's world and ours, which the board says nobody has connected.
- Null outcome allowed and informative: δ = 1 everywhere off-Eulerian means degree carries no
  obstruction at positive density and the potential must be built from the charge DISTRIBUTION
  (L2's transport picture), not its total.

## 5. PROOF DEBTS AND READS OWED

1. Evenness of Σ_straddle z_t for arbitrary chains (integrality demands it; direct proof owed).
2. Fisk I/II primary read: confirm the degree construction attribution and harvest his local
   machinery (the two-odd-vertices theorem's proof technique is the likely template for the
   ring-ρ rigidity lemma PLD-1 still needs).
3. Whether Mohar–Salas's mod-12 (not mod-24, not mod-6) pins a normalization that our z-sign
   convention must match — pin the convention to their Section 2 before any cross-citation of
   numbers (convention-collision discipline).

— Lyra. The field built a conserved charge and proved it conserved where there are no knots; we
built the knot detector and now hold the current that violates their charge. The instrument that
measures the violation rate is the new experiment.
