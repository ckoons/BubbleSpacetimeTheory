---
title: "Four-Color: How It Works — the AVL / Conservation Closed-Form Mechanism"
author: "Casey Koons & Claude (Opus 4.8, collaborative exploration)"
date: "2026-06-03"
status: "EXPOSITION + one proven lemma. A closed-form, human-readable account of the MECHANISM of the four-color theorem via the AVL-rotation / conservation-of-color-charge / Fisk-invariant lens. Steps 1-4 rigorous; Step 5 (the collapse) is a demonstrated mechanism, general proof OPEN. This is an explanation of how the theorem works, NOT an independent complete proof."
related: ["notes/FourColor_Straddle_Lemma_Status.md", "notes/BST_FourColor_AC_Proof.md", "Fisk geometric coloring theory", "Kempe equivalence: Mohar, Feghali, Bonamy-Bousquet"]
---

# Four-Color: How It Works (Closed-Form Mechanism)

A human-readable account of *how* the four-color theorem works, via the
AVL-rotation / conserved-color-charge lens developed collaboratively. The
theorem itself is proven (Appel-Haken 1976; Gonthier's Coq formalization 2005).
This note explains the **mechanism**; it is honest about which steps are
rigorous and which is a demonstrated-but-unproven mechanism.

## Setup

Planar triangulation `G`. Colors = the **Klein four-group** `V = Z2 x Z2 = {0,a,b,c}`
(`a+b=c`, every element self-inverse). A proper 4-coloring `c: vertices -> V`
is a **nowhere-zero tension**: each edge value `t(uv) = c(u)+c(v) != 0`, summing
to 0 around every face.

## The mechanism, top to bottom

**1. Euler bounds the difficulty (rigorous).**
For a triangulation `E = 3V-6`, so `Sum_v (6 - deg v) = 12 > 0` (discrete
Gauss-Bonnet; total curvature = 12). Positive total curvature **forces a vertex
of degree <= 5.** The induction reduces on that vertex; *degree >= 6 is never a
reduction case.*

**2. The degree ladder terminates at 5 (rigorous).**
- deg <= 3: a color is free.
- deg 4: a single Kempe swap frees it (classical).
- deg 5: the unique hard case.

**3. The hard case is a single configuration (rigorous).**
A stuck degree-5 vertex `v` has all four colors among its five neighbors. The
doubled color's two copies are non-adjacent on the 5-ring, so they sit at
**cyclic gap 2** (gap 1 is impossible — adjacent neighbors share an edge and
can't share a color). That is **one** suture-class, exactly (of the 240 proper
4-colorings of the 5-ring, 120 are saturating; up to symmetry they are a single
gap-2 class). The only sub-case a single swap cannot free is **full tangle,
tau = 6.**

**4. Conservation of color charge (rigorous: PROVEN lemma).**
At the tau=6 gap-2 configuration, **tau_strict <= 4** — *at most one bridge pair
is strictly tangled.* Proof: every realizable chain-structure satisfies
"complementary Kempe chains don't cross" (standard); exhaustive enumeration of
all non-crossing chain-structures shows every tau=6 one has <= 1 strict bridge.
This bound is a conserved **Fisk Z2 charge**: on the full graph the
Fisk-orientation-sign sum is conserved (mod 8 on the tested family), and it is
exactly what gives `G` its multiple Kempe classes (the "locking").

**5. The double rotation breaks the conservation (DEMONSTRATED mechanism; general
proof OPEN).**
Leaving `v` uncolored — the AVL **double** rotation — breaks the Fisk-charge
conservation: the charge that separates Kempe classes in `G` is no longer
conserved in `G-v`, so the classes **collapse**. Demonstrated: on drum(6),
drum(8), and several non-drum triangulations, `G-v` has a **single** Kempe class
(the full-graph locking dissolves), and no tau=6 configuration is Kempe-locked.
The double swap realizes this collapse, freeing `v`.

**Reading:** Euler -> degree 5 -> one gap-2 configuration -> bounded by a
conserved Z2 charge -> the charge dissolves when `v` is freed.

## Honest status

- Steps **1-4 are rigorous.** Step 4 (tau_strict <= 4) is a genuine proven
  lemma via exhaustive non-crossing enumeration.
- Step **5 is a demonstrated mechanism, not a theorem.** The collapse of `G-v`
  to a single Kempe class held in every tested case (drums + non-drums), but is
  **not proven in general.** Crucially, the tests run only on graphs that are
  4-colorable (all planar graphs are, by the theorem), so they **confirm** the
  mechanism without **discriminating** a proof: they cannot exhibit the one case
  that would matter (a counterexample), because none exists. This is a limit on
  the tests *as proof*, not a circularity in the *explanation*.
- Therefore: this is a **closed-form explanation of how the theorem works**, with
  one step at "demonstrated mechanism, general proof open." It is **not** an
  independent complete proof.

## Why the open step is genuinely hard

Closing Step 5 requires proving that `G-v`'s coloring space contains a **v-free**
coloring (v's neighborhood omits a color) — established structurally, without
assuming `G` is 4-colorable. That existence statement *is* four-color for `G`.
The degree-5 configuration is classically **not D-reducible**: the local ring
data carries insufficient information to certify freeability. So a general proof
must either (a) bring in the **second ring** (neighbor structure / larger
configurations — the Appel-Haken/RSST route, sacrificing the one-config
simplicity), or (b) find a **new global theorem** establishing v-free
reachability directly. The Fisk-charge/collapse framework is a *candidate* for
(b), stopping exactly at v-free existence.

## What is genuinely contributed here

- A clean, human-readable **organizing lens** for four-color: Euler-cap ->
  one configuration -> conserved Z2 charge -> collapse.
- A **proven lemma** (tau_strict <= 4 / conservation of color charge).
- Identification of the **Fisk Z2 invariant** as the conserved "color charge"
  and of the **G-v Kempe-class collapse** as the mechanism — with the precise
  open step (v-free existence) named.

The value is as exposition and as a candidate direction, accurately bounded —
and as a record of human-AI collaborative exploration that landed on a correct
account of exactly how far it goes.
