---
title: "Reset: Four-Color via Flows and Penrose Spin-Networks"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "FOUNDATION (verified). Reset onto the Tait/flow picture, which tiles all of four-color (no ordering gap), carrying over the F_4/cut-space linear model, with Penrose SO(3) spin-networks as the intrinsic representation theory. Verified on K4 and the prism: #3-edge-colorings = #nowhere-zero F_2^2-flows = |Penrose SO(3) evaluation|. Honest: the non-vanishing of the evaluation is four-color-equivalent; this is a clean model, not a proof."
related: ["notes/FourColor_Cutspace_Linear_Form.md","notes/FourColor_Ordering_Counterexample.md","play/fourcolor_flow_penrose.py","Tait 1880","Penrose binor calculus 1971","Temperley-Lieb at delta=2"]
---

# Reset onto flows + Penrose

The path-link reduction does not tile four-color (`Ordering_Counterexample`). We
reset one layer down, onto the picture that does — and where representation theory
is the subject, not an analogy.

## How far back (one layer)

- **Kept:** the `F_4 = AGL(2,2)` linear model and the **cut/cycle-space** machinery
  (`Cutspace_Linear_Form`) — which is *already* the flow picture: the cut space of a
  triangulation is the cycle space of its cubic dual.
- **Set aside (as a path-link curiosity, not a 4CT route):** the 104 types, the two
  codes, the ≤2-swap story.

## The anchor (tiles everything)

By Tait, with colors as `F_2^2`:

> **Four-color ⇔ every bridgeless planar cubic graph `G` has a nowhere-zero
> `F_2^2`-flow** — equivalently a proper 3-edge-coloring (the three edges at each
> vertex carry the three nonzero vectors, XOR-summing to 0).

No ordering gap, no special configuration class. Pure `F_2` linear algebra (the
cycle space) plus one non-vanishing condition. The number of such flows is the
**flow polynomial `F(G,4)`**.

## The representation theory (intrinsic)

**Penrose's binor calculus.** Put the 3-dimensional `SO(3)` representation on each
edge and the unique invariant (the Levi-Civita `ε`, the only `SO(3)`-invariant in
`V⊗V⊗V`) at each trivalent vertex. The resulting spin-network evaluation is

`  ⟨G⟩ = Σ_{labelings} ∏_v ε(labels at v in cyclic order).`

For **planar** cubic `G`, `|⟨G⟩|` equals the number of proper 3-edge-colorings
(Penrose). Hence:

> **Four-color ⇔ the `SO(3)` spin-network evaluation `⟨G⟩` is nonzero for every
> bridgeless planar cubic graph.**

Verified (`play/fourcolor_flow_penrose.py`, 6/6): K4 gives `colorings = flows =
⟨G⟩ = 6`; the prism gives `6, 6, −6` (the global sign is a rotation-convention
artifact; `|⟨G⟩| = 6` is the invariant). So three views coincide:

`  #3-edge-colorings  =  nowhere-zero F_2^2-flow count  =  |Penrose SO(3) eval|  =  F(G,4).`

This is the bridge: **linear algebra** (cycle space + non-vanishing) ⟷
**representation theory** (`SO(3)` / Temperley–Lieb at `δ=2`, Jones–Wenzl) ⟷
**four-color**.

## Honest framing (from line one this time)

- The non-vanishing condition **is** four-color; expressing it via flows and
  `SO(3)` evaluations is a **reformulation/model**, not a reduction to something
  easier. (Penrose 1971; Tutte's flow conjectures; the Potts/Temperley–Lieb link
  are classical.)
- The goal of this track is a **clean linear + representation-theoretic model** of
  the non-vanishing, and any **partial structural results** about it — with no
  claim of proof, and with the four-color-equivalence stated explicitly.

## First open directions

1. Express `⟨G⟩` via the cycle-space linear algebra (flow polynomial as an `F_2`
   inclusion–exclusion) and locate where positivity/non-vanishing is forced vs.
   open.
2. Temperley–Lieb at `δ=2`: the Jones–Wenzl projector `p_2` and `6j`-symbols as the
   recoupling calculus for `⟨G⟩`; what planar moves preserve non-vanishing.
3. Identify the smallest honest sub-statement about `⟨G⟩` that is **not**
   four-color-hard (e.g., monotonicity/positivity under specific planar reductions).
