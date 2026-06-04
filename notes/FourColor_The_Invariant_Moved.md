---
title: "The Invariant Moved: What Four-Color Is Really About"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "SYNTHESIS (capstone of the flow/Penrose arc). The conserved Euler charge 12 = 6*chi can be chased around the map by discharging but never eliminated. The four-color theorem is not the discovery that some map resists coloring -- no map does. It is the demonstration that the conserved invariant, no matter where it is chased, always lands on a configuration that carries no coloring obstruction. The computer enumeration (Appel-Haken) constricts the invariant's movement to a finite set of resting places and verifies each is harmless. The 'problem' was never a bad map; it was accounting for the invariant that had to move. Honest: this is the conceptual reframing of the discharging/reducibility method, not a new proof."
related: ["notes/FourColor_Conserved_Charge_NoGo.md","notes/FourColor_Even_2Factor_Endpoint.md","notes/FourColor_Move_Calculus.md","notes/FourColor_Three_Levers.md","play/fourcolor_discharging_demo.py"]
---

# The invariant moved

After carrying four-color down through flows, the `SO(3)` evaluation, matchings, the
narrowing reductions, and the move calculus, the whole arc resolves into one
sentence:

> **You can chase the invariant around the map, but you cannot eliminate it — and
> four-color is the proof that wherever it goes, there is no coloring problem there.**

This note states that precisely.

## The invariant

Give each face `f` the charge `6 − |f|`. For any planar cubic graph the total is a
conserved topological quantity:

`  Σ_faces (6 − |f|) = 6F − 2E = 6·χ = 12   (sphere, χ = 2).`

It does not depend on size or embedding. Discharging — any local rule that pushes
charge between faces and vertices — **moves** the charge but **conserves** it. The
demonstration (`play/fourcolor_discharging_demo.py`): after ten thousand arbitrary
redistributions the total is still `12`, and because `12 > 0` no rule can drive every
face to `≤ 0`. A positive concentration — a face of size `≤ 5`, an unavoidable
configuration — always remains *somewhere*. **The invariant moved; it did not vanish.**

On the **torus** (`χ = 0`) the charge is `0`; you *can* zero it, and four-color is
*false* there (seven colors). The nonzero `12` is the genus-0 boundary condition: it
is what makes the sphere special and the problem non-trivial.

## What four-color actually claims

Here is the reframing. A "problem" map would be a planar map that cannot be
4-colored — equivalently a bridgeless planar cubic graph with **no even 2-factor**,
**no nowhere-zero `F_2^2`-flow**, `⟨G⟩ = 0`. The four-color theorem says:

> **No such map exists.**

So four-color is **not** the discovery of an obstruction. It is the demonstration of
the **absence** of one. And the absence is governed entirely by the conserved
invariant:

- **Unavoidability.** Discharging cannot spread the `12` so thin that no recognized
  configuration appears. Wherever you chase it, it must rest on one of a **finite,
  unavoidable set** of local configurations. (You constrict its movement.)
- **Reducibility.** Each configuration in that finite set, if it sat inside a
  *minimal* uncolorable map, could be re-colored from a smaller map — contradiction.
  So **every resting place of the invariant carries no coloring obstruction.**

Together: the invariant must land somewhere (unavoidability), and every place it can
land is harmless (reducibility). Therefore no minimal counterexample exists, and
**every planar map is four-colorable.**

## What the computer enumeration is doing

In this light Appel–Haken's computation is not a search for a bad map — there are
none. It is the act of **constricting the invariant's movement** and **certifying
each resting place**:

- the discharging rules **constrict** the conserved `12` into a finite list of
  configurations it cannot avoid;
- the reducibility checks **certify** that each of those configurations, where the
  invariant comes to rest, presents no obstruction to coloring.

The ~600 configurations are the **resting places of the invariant**, and the
machine's job is to confirm, one by one, that the invariant being *there* never
stops the map from being colored. The "problem" was never a map that resists color.
The problem was purely **accounting for the invariant that had to move** — and
showing that its every destination is safe.

## Why it cannot be made to dissolve

This is the honest content of the no-go (`Conserved_Charge_NoGo`):

- the invariant is `6·χ`, a **topological** quantity; every reduction preserves the
  sphere, so it preserves `12`;
- `12 ≠ 0` forces an unavoidable configuration at **every** scale — the
  self-similar persistence (the "fractal");
- so the problem **never reduces to vacuity**: there is always an invariant to place.

What four-color adds on top of this no-go is the *other* half: that placing it is
always possible. The no-go says the invariant cannot be eliminated; the theorem says
it never needs to be — every destination is colorable. Both halves are needed, and
they are different in kind: one is a one-line topological identity, the other is the
finite, computational verification that the invariant's resting places are harmless.

## Honest scope

- The conserved charge and its irremovability are **proven** (a one-line Euler
  identity); the discharging-conserves-it demonstration is exact.
- The reframing — four-color as *the invariant always lands somewhere harmless* — is
  the **conceptual content of the discharging + reducibility (unavoidability) method**
  (Heesch; Appel–Haken; Robertson–Sanders–Seymour–Thomas). It is a way of *seeing*
  the proof, not a new proof. The reducibility certifications remain the irreducible,
  computer-assisted core.
- The contribution of this arc is the clean, trilingual route (flows / `SO(3)` /
  matchings) to this picture, with every surrounding step proven and honestly
  attributed, and the central object named: **the conserved Euler charge of the
  sphere, which can be chased but not eliminated, and whose every resting place
  four-color certifies as colorable.**
