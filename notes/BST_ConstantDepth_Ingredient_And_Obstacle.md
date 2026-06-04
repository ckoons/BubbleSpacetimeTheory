---
title: "Building a Constant-Depth Algebraic-Hardness Ingredient into the Vehicle: the SPD Measure and the Sparse-Fuel Obstacle"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "MIXED: ingredient computed; honest obstacle identified. The constant-depth-hardness currency (shifted partial derivatives, SPD) is real and computable, and separates a low-depth polynomial from a hard one. But building it into the RANDOM-3-SAT vehicle is genuinely in doubt: the formula's natural polynomials are sparse/product-structured (low SPD = low-depth-leaning), and high PC/SoS DEGREE (what our expander gives) does NOT imply circuit-SIZE hardness. So the carry to constant-depth IPS may FAIL for random fuel; LIFTING a dense hard polynomial works but yields a CONSTRUCTED instance, not random 3-SAT."
related: ["notes/BST_Bridge_To_PvsNP.md","notes/BST_ProofSystems_As_LinearAlgebra.md"]
---

# The ingredient, and whether it fits the vehicle

The bridge's regime change said: to cross to constant-depth IPS we need an
**algebraic-circuit (size/depth) lower bound** for the refutation polynomial of `phi'`,
which expansion does not give. So we tried to *build that ingredient in*.

## The ingredient is real and computable (SPD)

The lower-bound currency for constant-depth algebraic circuits is the **shifted partial
derivatives (SPD)** measure: `SPD_{k,l}(f) = dim span{ (deg-l monomial) * (order-k
partial of f) }`. A small low-depth circuit forces small SPD; a hard polynomial has SPD
near the maximum. Computed over `GF(10007)`, `N=6`, `D=3`:

| polynomial | SPD(1,1) / max | SPD(1,2) / max |
|---|---|---|
| `x0x1x2 + x3x4x5` (2 products) | 32 / 56 | 93 / 126 |
| 4 products | 23 / 56 | 67 / 126 |
| **dense generic deg-3** | **36 / 56** | **111 / 126** |

The dense/hard polynomial sits near the ceiling; structured (few-product) ones do not.
So the **constant-depth-hardness ingredient is in hand and computable** -- exactly the
currency the IPS rung needs.

## The obstacle: the random fuel may not carry it

Here is the honest catch. To "build it into the vehicle" for **random 3-SAT** we need
the *refutation object of `phi'`* to be constant-depth-hard. Two reasons this is in
genuine doubt:

1. **Degree != circuit-size.** Our expander gives `phi'` high PC/SoS *degree*. But a
   high-degree certificate can be computed by a *small* circuit. Expansion bounds
   degree, not SPD/circuit-size. So we have **no tool** that delivers SPD-hardness from
   expansion -- the regime change, restated.
2. **Sparse fuel leans low-SPD.** Random 3-SAT's natural polynomials are **sparse,
   product-structured** (each clause is a product of 3 literals). The SPD computation
   shows product-structured polynomials have *lower* SPD than dense ones -- i.e. they
   lean **low-depth-easy**. The refutation *certificate* need not be sparse, but there
   is no reason it must be dense/hard, and the sparsity of the fuel is a warning sign.

So it is genuinely possible that **random 3-SAT has small constant-depth IPS
refutations** (the certificate, though high-degree, computed by a small low-depth
circuit) -- in which case the carry **fails because it is false**, not because we lack
a proof. This is open both ways, and the SPD sparsity signal leans toward "easy."

## Lifting works, but changes the fuel

We *can* guarantee the ingredient by **lifting**: encode an explicit SPD-hard
(dense / IMM-type) polynomial's refutation as a CNF whose IPS refutation must compute
it; then constant-depth IPS hardness follows (LST/SPD), and zero-cascade carries it to
certified-backbone hardness **of that constructed formula**. But this instance is
*engineered*, not random 3-SAT -- a weaker, less natural statement (one can encode many
hard objects into *some* SAT instance). It does not establish the framework's claim
about the natural random distribution.

## Honest conclusion

- **Ingredient:** found and computable (SPD), separates low-depth from hard. Yes, we
  can exhibit a constant-depth-hard algebraic circuit object.
- **Building it into the random-3-SAT vehicle:** genuinely uncertain and possibly
  false -- expansion gives degree not circuit-size, and the sparse fuel leans
  low-SPD/low-depth-easy. This is the real frontier and the honest place the carry may
  not go.
- **Lifting:** gives the ingredient but on a constructed instance, not random 3-SAT.

So the precise next research question is sharp and two-sided: **Is the refutation
object of a random expander 3-CNF constant-depth-algebraically hard (high SPD), or is
it constant-depth-easy (small circuit despite high degree)?** Settling that -- either
direction -- is the genuine content. Our vehicle carries iff the answer is "hard," and
the current evidence (sparse fuel, degree!=size) does not promise it.
