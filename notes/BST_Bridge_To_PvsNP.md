---
title: "The Bridge to P vs NP: Certified Backbone -> IPS -> Algebraic Circuits, the Reachable Rung and the Walls"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "BRIDGE MAP (honest, cited). Draws the complete path from our certified-backbone hardness to P != NP: zero-cascade reduction climbs proof systems; the top (all systems) is P != NP via Cook-Reckhow (NP != coNP => P != NP). The algebraic spine: IPS p-simulates EF and IPS lower bounds = algebraic circuit lower bounds (VP vs VNP). Reachable next plank: CONSTANT-DEPTH IPS, where lower bounds now exist (LST 2021; low-depth IPS lower bounds 2022+) -- the carry needs a constant-depth IPS lower bound for the random expander residual phi'. Walls: full IPS/EF = VP vs VNP (algebraic P != NP); all-systems (Cook's program). Barriers on BOTH routes: natural proofs / algebrization (Boolean) and algebraic natural proofs (Forbes-Shpilka-Volk; Grochow-Kumar-Saks-Saraf)."
related: ["notes/BST_ProofSystems_As_LinearAlgebra.md","notes/BST_Certified_Backbone_ResK_Proof.md","notes/BST_PvsNP_Roadmap_Frontier.md"]
---

# The bridge to P vs NP

Casey: go after IPS, find the bridge to P vs NP. Here it is, end to end, with each
plank marked **have / reachable / wall**, and the barriers on both routes.

## The bridge, drawn

```
 certified-backbone hardness for a proof system P
   ===(zero-cascade reduction)===   refuting the residual expander phi' is P-hard
        |
        |  climb P upward (each rung = import a known refutation lower bound):
        v
 Resolution  ->  Res(k)  ->  SoS / PC      [HAVE]
        ->  Cutting Planes                 [reachable, free-ish]
        ->  constant-depth IPS             [REACHABLE FRONTIER: LST 2021 + low-depth IPS LBs]
        ->  IPS  ( p-simulates EF )        [WALL = VP vs VNP, algebraic P!=NP]
        ->  Frege, ..., ALL proof systems  [WALL = Cook's program]
        |
        v   (Cook-Reckhow)
 lower bounds for ALL proof systems  <=>  NP != coNP   =>   P != NP
```

Two facts make the top of the bridge:

- **Cook-Reckhow.** `NP = coNP` iff some propositional proof system is polynomially
  bounded. So superpolynomial lower bounds for **every** proof system `<=>` `NP != coNP`,
  and `NP != coNP => P != NP` (since `P = coP`; `P = NP` would force `NP = coNP`). This
  is **Cook's program**; EF/IPS is its current frontier.
- **Algebraic spine (Grochow-Pitassi 2014).** The **Ideal Proof System** `IPS`
  p-simulates `EF`, and a superpolynomial `IPS` lower bound **implies an algebraic
  circuit lower bound** (`VP != VNP`, the algebraic analog of `P vs NP`, Valiant). So
  the upper bridge is, in disguise, **algebraic `P vs NP`**.

## Where we are, and the reachable next plank

**Have.** Certified-backbone hardness for resolution, `Res(k)`, SoS/PC -- the
bounded-degree linear-algebra rungs (dual certificate = pseudo-distribution; expansion
gives the bound). See `BST_Certified_Backbone_ResK_Proof.md`.

**Reachable next plank: constant-depth IPS.** This is the genuine frontier, not the
mountain. Two real ingredients now exist:
- **LST 2021** (Limaye-Srinivasan-Tavenas): the first superpolynomial lower bounds for
  **constant-depth algebraic circuits** (for iterated matrix multiplication / explicit
  polynomials).
- **Low-depth IPS lower bounds** (Govindasamy-Hakoniemi-Tzameret 2022 and successors):
  these convert constant-depth algebraic lower bounds into **constant-depth IPS** lower
  bounds for explicit unsatisfiable instances.

> **The carry (intermediary lemma we need).** Show that refuting the random expander
> residual `phi'` requires a **superpolynomial constant-depth IPS** proof. Concretely:
> the IPS refutation circuit of `phi'` must compute a polynomial encoding the expander's
> structure; show that polynomial is **constant-depth-hard** (LST-style functional /
> partial-derivative measure), exploiting expansion. Then zero-cascade carries it to
> certified-backbone hardness for constant-depth IPS.

This is the same "free-ride on a known lower bound" pattern as the SoS rung -- but now
the imported bound is an **algebraic-circuit** lower bound, and the open piece is a
**random-formula** constant-depth IPS lower bound (LST-type bounds are for *explicit*
polynomials; transferring to random `phi'` is the precise research gap). It is a real
rung **above SoS, toward EF**, and -- unlike EF -- the machinery exists.

## The walls (named, not hidden)

1. **Full IPS = EF `<=>` `VP` vs `VNP`** (algebraic `P vs NP`). Major open problem, but
   *algebraic* and with live progress (GCT; constant-depth breakthroughs). This is the
   first true wall above the reachable plank.
2. **All proof systems (Cook's program).** Beyond EF, superpolynomial lower bounds for
   *every* system `=>` `NP != coNP => P != NP`. Wide open.

## Barriers on BOTH routes (the honest constraint)

- **Boolean route:** natural proofs (Razborov-Rudich) and algebrization
  (Aaronson-Wigderson) rule out broad techniques for strong systems.
- **Algebraic route:** an **algebraic natural proofs barrier** exists too
  (Forbes-Shpilka-Volk 2017; Grochow-Kumar-Saks-Saraf 2017): under hardness assumptions
  about `VNP`, the "nice" methods for algebraic circuit lower bounds also face an
  obstruction. So crossing the `VP` vs `VNP` wall is barrier-constrained as well.

Any successful crossing -- Boolean or algebraic -- must evade its barrier. None
currently does.

## Honest assessment

- **The bridge is real and well-defined.** Our certified-backbone reduction is a
  *vehicle* on it: every new proof-system lower bound for `phi'` becomes a new rung,
  and the top of the tower is `P != NP` (via Cook-Reckhow). This is not hand-waving;
  it is the standard structure of Cook's program, with the zero-cascade reduction as
  the satisfiable-side connector.
- **What is genuinely reachable now:** the constant-depth IPS rung, via LST +
  low-depth-IPS machinery, modulo a **random-formula constant-depth IPS lower bound**
  -- the precise next theorem to chase. That is at the active frontier.
- **What remains the open problem:** `VP` vs `VNP` (algebraic `P vs NP`, the IPS/EF
  wall) and then the full Cook program -- both barrier-constrained. The reduction
  cannot manufacture these; it can only carry them once proven.

So "the bridge to P vs NP" is: **certified backbone hardness, escalated through the
proof-system / algebraic-circuit hierarchy, topped by Cook-Reckhow.** We hold the
lower rungs; the next reachable plank is constant-depth IPS (a real, active target);
the summit is `VP` vs `VNP` then all-systems -- the famous open problems, with barriers
guarding both the Boolean and algebraic approaches.

---

## The regime change at IPS (the precise reason the carry stops — and what crossing needs)

Working the IPS carry exposes *why* the bridge is not a smooth climb. There is a sharp
**regime change** at IPS, and naming it is the honest answer to "what intermediary
steps do we need."

**Below IPS — the degree regime (we have it, for free).**
Resolution, `Res(k)`, PC, SoS are all **bounded-degree / linear-algebra** systems. For
them the relevant resource is **degree**, and **expansion is exactly the lower-bound
mechanism**: an `(Omega(n), delta)`-boundary expander forces refutation
width/PC-degree/SoS-degree `Omega(n)`. Our zero-cascade reduction delivers an expander
residual `phi'`, so the carry is *free* across this entire regime.

**At and above IPS — the size/circuit regime (a NEW resource is required).**
IPS (= EF) is **not** degree-bounded: an IPS refutation is a **small algebraic
circuit** that may compute a high-degree certificate. So the resource is **circuit
size/depth**, not degree. And here is the crux:

> **High degree does NOT imply small-circuit-hardness.** A formula can require
> `Omega(n)` PC degree (from expansion) yet have a *small* IPS refutation, if the
> high-degree certificate is computable by a small circuit. **Expansion bounds degree;
> it does not bound circuit size.**

Therefore our reduction -- whose only lower-bound currency is expansion (a *degree*
resource) -- **cannot carry past SoS by itself.** Crossing to constant-depth IPS
requires a genuinely new ingredient:

> **The missing plank:** an **algebraic-circuit (size/depth) lower bound** for the
> refutation polynomial of the expander residual `phi'` -- *not* implied by `phi'`'s
> expansion. Bridging **expansion -> constant-depth-algebraic-hardness** is the precise
> open step. (LST-type bounds give constant-depth algebraic hardness for *explicit
> structured* polynomials; whether the *random expander* `phi'` is constant-depth-hard
> is the frontier question, and it does not follow from expansion alone.)

**Why this is the wall, made precise.** The degree->size regime change is exactly
where circuit complexity begins, and circuit lower bounds (Boolean *or* algebraic) are
the open problems guarded by the natural-proofs barriers (Razborov-Rudich; and the
algebraic analog, Forbes-Shpilka-Volk / Grochow-Kumar-Saks-Saraf). So:

- **EF is the wall because it is the first size/circuit-regime system** -- where
  expansion (our currency) stops paying, and circuit hardness (the open, barrier-
  guarded resource) takes over.
- **The bridge to P vs NP** is therefore: free climb through the **degree regime**
  (have, via expansion), then a **regime change at IPS** requiring **circuit lower
  bounds** (the open problem), topped by Cook-Reckhow.

This is the sharpest honest statement the linear-algebra framing yields: we own the
degree regime; the size regime is the famous open problem; the boundary between them is
EF/IPS, and the intermediary step is precisely *converting expansion into algebraic-
circuit hardness for `phi'`* -- a real, named, currently-open research target, with the
constant-depth case (LST machinery) the first place to attempt it.
