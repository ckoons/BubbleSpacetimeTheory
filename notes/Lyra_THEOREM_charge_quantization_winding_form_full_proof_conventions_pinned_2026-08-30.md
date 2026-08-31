---
title: "L2 — THEOREM (Charge Quantization, winding form): full proof, conventions pinned, citable. Odd vertices carry unit winding; deg-4 vertices are neutral; the global sum is four times the Fisk/Mohar–Salas degree"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 12:24 EDT at round start)"
status: "ROUND 5, LANE L2. Theorem-candidate with complete proof — promoted from the round-4 hand notes. Registration (/theorem claim) deferred until Cal's cold-read PASS per round discipline. Two external pins owed and named in Section 4; neither affects the proof, only cross-citation of numbers."
---

# THEOREM (Charge Quantization, winding form)

## 0. CONVENTIONS (pinned; every sign in this note refers here)

- T: a simple triangulation of the oriented 2-sphere, with a fixed orientation; faces read
  counterclockwise.
- f: a proper 4-coloring, colors identified with the Klein group V = ℤ₂×ℤ₂ = {0, a, b, c}; a
  fixed reference cyclic order (a, b, c) on the nonzero elements.
- Every face carries three distinct colors (properness on a triangle). **Face sign z_t ∈ {±1}:**
  +1 if the three edge labels (sums of endpoint colors), read counterclockwise, form an even
  permutation of (a, b, c); −1 otherwise. Equivalently (and used below): fix f(w) at a vertex w
  of t; then z_t = +1 iff the ordered pair of the other two colors is a positive step in the
  cyclic order induced on V ∖ {f(w)} — the two readings agree face-by-face (three distinct
  colors determine both signs from the same permutation datum).
- **Charge c(v) := Σ_{t ∋ v} z_t ∈ ℤ. Winding ω(v) := c(v)/3** (integrality is part (i) below).
- **Degree of the coloring:** f is a simplicial map T → ∂Δ³ (each face onto the tetrahedron face
  named by its color triple), and z_t is its local orientation sign; deg(f) is its topological
  degree.

## 1. THEOREM

Let T, f be as above. Then:
1. **(Integrality / Heawood)** c(v) ≡ 0 (mod 3) at every vertex; ω(v) ∈ ℤ.
2. **(Parity and bound)** c(v) ≡ deg(v) (mod 2) and |c(v)| ≤ deg(v).
3. **(Quantization)** ω(v) = 0 for deg(v) = 4; ω(v) ∈ {−1, +1} for deg(v) ∈ {5, 7};
   ω(v) ∈ {0, ±2} for deg(v) = 6; in general ω ranges over integers with 3ω ≡ deg (mod 2),
   |3ω| ≤ deg.
4. **(Global sum)** Σ_v c(v) = 3 Σ_t z_t = 12·deg(f); equivalently Σ_v ω(v) = 4·deg(f).
5. **(No local rotation at odd vertices)** an odd-degree vertex admits no singleton Kempe chain;
   in particular no single swap recolors an odd vertex alone.

## 2. PROOF

**(i)** Fix v with degree d and link cycle u₁, …, u_d (counterclockwise). The link colors avoid
f(v): they lie in the 3-element set V ∖ {f(v)}, cyclically ordered by the reference order. For
the face t_i = (v, u_i, u_{i+1}): z_{t_i} = +1 iff f(u_i) → f(u_{i+1}) is a positive step in
that cyclic order (convention, Section 0). The sequence f(u₁), …, f(u_d), f(u₁) is a closed walk
on the 3-cycle of colors; each consecutive pair is a ±1 step (properness of the link edge
u_i u_{i+1} forbids a null step — consecutive link vertices are adjacent in a triangulation).
A closed walk on a 3-cycle has (#positive − #negative) ≡ 0 (mod 3). But that difference is
exactly Σ_i z_{t_i} = c(v). ∎(i)

**(ii)** c(v) is a sum of d terms ±1: parity d, absolute value ≤ d. ∎(ii)

**(iii)** Arithmetic of (i)+(ii): the multiples of 3 with parity d and modulus ≤ d are: d=4:
{0}; d=5: {±3}; d=6: {0, ±6}; d=7: {±3}; general as stated. Divide by 3. ∎(iii)

**(iv)** Each face has 3 vertices, so Σ_v c(v) = 3 Σ_t z_t. The degree of a simplicial map to
∂Δ³ ≅ S² is the signed count of preimages of any one of the four target faces; summing the four
counts, Σ_t z_t = 4·deg(f). ∎(iv)

**(v)** A singleton (x,y)-chain at v (f(v) = x, no neighbor colored y) requires the link to be
properly colored from V ∖ {x, y} — two colors on an odd cycle when deg(v) is odd: impossible.
∎(v)

## 3. REMARKS (what the theorem does and does not say)

- The GRAPH fixes the knot sites (odd vertices — forced |ω| ≥ 1); the COLORING chooses only the
  signs (and any deg-6 excitations). By (iv) the sign choice is globally constrained:
  Σω = 4·deg. By (v) the signs cannot be adjusted one vertex at a time. Dipole transport (the
  L2 round-4 note, and X3's measured gate) is the only legal dynamics — that reading is
  interpretation, not part of the theorem.
- Under a Kempe swap, the change of charge is supported on the chain boundary (Straddle-Flip —
  a separate candidate, verified 144/144 by X3 on Fritsch but still awaiting the full E4 pass;
  THIS note does not depend on it).
- Item (i) is classical in substance (Heawood's condition); (iv)'s degree identity is the
  Fisk/Mohar–Salas object. The PACKAGE — quantization at odd vertices in winding units, with the
  no-local-rotation lemma making knots dynamical — is, as far as our literature pass shows, the
  new part; the novelty claim stays soft until the Fisk primaries are read (Section 4).

## 4. EXTERNAL PINS OWED (convention checks, not proof dependencies)

1. **Mohar–Salas Section 2:** confirm their degree sign convention matches Section 0 (a global
   sign flip changes nothing internally but must be pinned before quoting their mod-12 with our
   Σω mod 48 side by side — the PC1 control in the L1 spec).
2. **Fisk I/II:** locate the winding/local-degree object in his machinery (expected present in
   some form); adjust the novelty remark accordingly, either way without changing the theorem.

— Lyra. Four small facts and one arithmetic table; the physics was already in the room — this
note just makes it citable.
