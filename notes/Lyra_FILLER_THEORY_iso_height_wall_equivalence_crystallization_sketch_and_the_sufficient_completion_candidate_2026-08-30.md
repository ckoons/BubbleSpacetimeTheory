---
title: "U1 — filler theory: the Filler ⟺ Iso-Height Wall equivalence (PROVED), the crystallization mechanism for necessity (sketch, with its missing lemma named and instantly testable), and the sufficient-completion candidate: filler + monotone winding"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 18:05 EDT at round start)"
status: "ROUND 12, LANE U1. One equivalence proved; one mechanism sketched with its gap named and pre-registered testable; one sufficient-completion candidate with kill conditions, filed BEFORE slope-v2 or the fork render. Cal's rubric note honored: 15/15 at ~1/9 base is Elie's statistic; nothing here calls it a law. Nothing banks."
---

# FILLER THEORY

## 1. WHAT A FILLER IS, IN HEIGHT LANGUAGE (proved equivalence)

Setting: pinned disc boundary cycle (even length; vertices alternate between the two parity
classes), the proved Height Dictionary, a fixed gauge.

**Lemma F1 (Filler ⟺ Iso-Height Wall).** One color occupies an entire parity class of the
boundary ⟺ the boundary height is CONSTANT on that parity class.

*Proof.* (⟹) With even-class vertices all colored x, the two boundary edges at any odd-class
vertex y_i carry the same label x + f(y_i); the dual ± classes alternate along the boundary fan,
so the two steps at y_i cancel: every two-step excursion returns. The even-class heights all
equal h₀. (⟸) If h is constant on the even class, each two-step excursion cancels, so the two
edges at y_i carry equal labels: f(x_{i−1}) + f(y_i) = f(y_i) + f(x_{i+1}), giving
f(x_{i−1}) = f(x_{i+1}); propagating around the cycle, the even class is monochromatic. ∎

This retroactively explains S1's double anomaly with no epicycle: frozen pinnings sat at
disp-sum slope ZERO because a filler boundary is a zigzag — flat in NET slope while maximally
rigid in STRUCTURE. The rigidity variable was never the tilt (gradient); it is the WALL — half
the boundary crystallized onto one height level. "Half-crystallized" is now a theorem-grade
description, not a metaphor.

## 2. WHY FREEZING NEEDS A WALL — the crystallization mechanism (sketch; missing lemma NAMED)

Mechanism: a frozen completion is height-rigid; in the stat-mech dictionary rigid states are the
crystalline ones — locally 3-colored rainbow patterns (the four-coloring's analogue of
f = x+y mod 3), which use THREE colors in the bulk and exile the fourth. A rigid interior over a
disc must meet its boundary through a flat wall — the iso-height class — which by Lemma F1 IS a
filler. Sketch status: the load-bearing step is:

**Crystallization Lemma (named, unproved, instantly testable):** a relatively frozen completion
uses only three colors on its interior — the filler color appears on the boundary alone.
*Test tonight (Elie, one glance at objects already in hand): do the twins' interiors omit the
filler color? Pre-registered: YES.* If the glance refutes it, the mechanism needs a fourth-color
excitation theory and Section 3's candidate changes shape — cheap to learn now.

(Necessity's logical status, kept straight: Lemma F1 is proved; filler-necessity itself is
Elie's 15/15 measurement plus this mechanism sketch — Cal's rubric owns what it may be called.)

## 3. THE SUFFICIENT COMPLETION — the candidate, pre-registered before slope v2 renders

Filler is necessary-shaped but not sufficient (~1/9 of FREE pinnings have one). What
distinguishes the frozen fillers? In the rigid rainbow, the non-filler boundary colors are not
free: reading the odd-parity class around the boundary, the three remaining colors must advance
CONSISTENTLY with the interior crystal's winding.

**Candidate (Filler + Monotone Winding ⟺ Frozen):** a pinning freezes iff (i) it has a filler,
and (ii) the complement class's colors, read cyclically, wind MONOTONICALLY in a single ℤ₃
orientation (each step advances the 3-cycle of non-filler colors by the same sense — the
staircase condition; total winding then = ±(boundary length)/2 in the ℤ₃ count, matching a
rainbow interior's screw structure).

Kill conditions, both directions, filed now: any frozen pinning whose complement class breaks
monotonicity; any free pinning satisfying (i) + (ii). Test population: the 15 frozen + the
free-with-filler subclass of the census (the ~1/9). Prediction detail worth logging: among
free-with-filler pinnings, the winding should be NON-monotone (at least one reversal), and the
number of reversals may correlate with how far from frozen the pinning sits (class count /
move richness) — logged as a secondary axis, not a claim.

## 4. WHAT THIS HANDS THE OTHER LANES

- To U2 (torsor-cocycle): the wall is the static boundary datum; the residual dynamical
  invariant lives in the interior height sector OVER a fixed wall — the fork (phase vs defect)
  decides its shape.
- To Cal's twin-datum clause: filler is a PINNING property and both twins share it; the Rosetta
  datum must be the interior height structure — exactly what the fork computation reads.
- To the paper (U4, when stable): Lemma F1 + the crystallization mechanism are the "frozen
  boundary conditions" section the stat-mech audience has wanted a finite-graph handle on;
  v0.4 waits for the fork and slope-v2 verdicts rather than absorbing a moving target.

— Lyra. The boundary was never tilted; it was half-frozen into a wall, and the wall equivalence
is two paragraphs of height algebra. What makes the other half of the boundary conspire — the
staircase — is now a candidate with kill conditions on both doors.
