---
title: "The Provably Non-Vanishing Class (and an honest negative on single-step positivity)"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "RESULTS + honest negative. NEGATIVE: the binor is NOT count-additive (#col(G) != #col(G+)+#col(G-): prism 6 vs 18, cube 24 vs 36), so the minus sign is genuine cancellation and there is no cancellation-free single-binor-step positivity. POSITIVE (provable, NOT 4CT-hard) sufficient conditions for <G> != 0: Hamiltonian cubic (explicit 3-coloring), bipartite cubic (Koenig), scaling-reducible (the move calculus). These build a growing provably-colorable class; the four-color difficulty concentrates on non-Hamiltonian, non-bipartite, scaling-irreducible core graphs."
related: ["notes/FourColor_Move_Calculus.md","notes/FourColor_Narrowed_Core.md","play/fourcolor_nonvanishing_class.py"]
---

# Probing single-step positivity, and what is actually provable

## Honest negative: the minus sign is real

We hoped the binor might be **cancellation-free at the count level** —
`#col(G) = #col(G_+) + #col(G_-)` — which would make non-vanishing a positive
recursion. It is **false**: prism gives `6 ≠ 18`, cube `24 ≠ 36`
(`play/fourcolor_nonvanishing_class.py`; K4 coincides only because one resolution
vanishes). So the binor `(I − swap)` minus sign is **genuine cancellation**; the
content lives in the signed `SO(3)` evaluation, and there is **no clean
single-binor-step positivity invariant**. This is the four-color-hard core,
confirmed not to dissolve.

## What is provable: sufficient conditions for `⟨G⟩ ≠ 0`

These force non-vanishing **without** confronting the binor — the honest,
non-four-color-hard sub-theory. Each is a clean theorem.

**(H) Hamiltonian ⇒ 3-edge-colorable.** A cubic graph with a Hamilton cycle (length
`2n`, even) is 3-edge-colorable: 2-color the cycle edges alternately `1,2`; the
remaining edges form a perfect matching, all colored `3`. At each vertex the two
cycle edges give `{1,2}` and the matching edge gives `3` — proper. *(Verified: cube
and prism Hamiltonian 3-colorings are proper.)*

**(B) Bipartite ⇒ 3-edge-colorable.** A bipartite cubic graph is class 1 by König's
edge-coloring theorem. *(Verified: the cube is bipartite.)*

**(S) Scaling-reducible ⇒ non-vanishing.** If the scaling moves (loop, bubble,
theta, `Δ→Y`, small cuts; `Move_Calculus`) reduce `G` to nothing, `⟨G⟩` is a product
of nonzero factors. 

## The boundary, sharpened

The union (H) ∪ (B) ∪ (S) is a large **provably colorable** class. Four-color's
genuine difficulty concentrates on graphs in the **complement**: planar cubic that
are **non-Hamiltonian, non-bipartite, and scaling-irreducible** — exactly the kind
(non-Hamiltonian planar cubic, e.g. Tutte's graph; girth-5 cyclically-5-connected)
that the historical hard instances inhabit. On these only the binor applies, with
real cancellation.

## Honest scope

- (H), (B), (S) are classical sufficient conditions, stated and verified here in the
  flow/Penrose model; they are genuine, provable, and not four-color-hard.
- The negative (binor non-additivity ⇒ no single-step positivity invariant) is the
  honest result of the probe: the minus-sign cancellation is essential and cannot be
  evaded at the count level. The four-color-equivalent core remains exactly the
  binor sign-sum non-vanishing on non-Hamiltonian/non-bipartite core graphs.
