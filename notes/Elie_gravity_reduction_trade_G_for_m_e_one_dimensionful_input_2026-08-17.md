---
title: "Trading G for the electron: BST's gravitational constant from one atomic input"
author: "Elie (Claude Opus 5), BST program"
date: "2026-08-17 Monday (date-verified)"
status: "v0.1 draft — gravity thread #94. Two guards carried in the text: exactly one dimensionful input; alpha is Identified, not derived."
---

# Trading G for the electron

## The story first

Every physical theory has to be told, once, how big things are. You can write down all the
rules you like about how a swing works, but until somebody tells you the length of the rope,
you cannot say how long a swing takes. Physics is the same. General relativity does not
predict Newton's constant *G* — it takes it. The Standard Model does not predict the
electroweak scale *v* — it takes it.

The question this note asks is narrow and answerable: **how many such numbers does BST have
to be told?**

The answer is **one**, and the one it needs is the mass of the electron — a number measured
in a table-top ion trap, with no reference to gravity anywhere in the measurement. Once BST
is told the electron's mass, Newton's constant comes out to **0.065%** and the electroweak
scale to **0.046%**.

That is the whole claim. It is a *reduction*, not a free lunch: we traded a constant we could
only measure by weighing the Earth for one we can measure by watching a single trapped
electron go round in a circle.

## The chain

Every line below takes **m_e** as the only dimensionful input.

| quantity | BST form | predicted | observed | deviation |
|---|---|---|---|---|
| m_p/m_e | 6π⁵ = N_c!·π^{n_C} | 1836.1181 | 1836.1527 | **0.0019%** |
| m_Planck | m_e/(6π⁵·α^{2C₂}) | 2.175727×10⁻⁸ kg | 2.176434×10⁻⁸ | **0.0325%** |
| **G** | ħc/m_Planck² | 6.678640×10⁻¹¹ | 6.674300×10⁻¹¹ | **0.0650%** |
| v (electroweak) | (6π⁵)²·m_e/g | 246.107 GeV | 246.220 | **0.0459%** |

Four dimensionful quantities, one input, everything under 0.1%.

**But that table is four *quantities*, not four *results*, and the difference matters.** See Guard 3.

## The count, honestly

In natural units (ħ = c = 1):

| theory | dimensionful inputs | count |
|---|---|---|
| Standard Model + GR | v and G | **2** |
| BST | m_e | **1** |

**The reduction is 2 → 1.** Both *v* and *G* become outputs of a single atomic anchor.

## Guard 1 — exactly one input, and that is the floor

**m_e is an input, not a prediction.** Any statement that BST has "zero free parameters"
refers to its **dimensionless** content only, and must never be written unqualified.

It is worth being precise about why this is not a shortfall. BST's content is five integers,
a geometry, and dimensionless ratios — every one of them a pure number. **A dimensionless set
cannot produce a quantity with units.** No combination of pure numbers has units of
kilograms. So nothing internal to BST can ever fix m_e in absolute terms, and asking it to is
asking for something dimensional analysis forbids.

The minimum number of dimensionful inputs for *any* theory that predicts a dimensionful
quantity is **one**. **BST takes one. It is at the floor.**

This reframes the open question rather than answering it. "m_e is an input" is not a gap
waiting to be closed by a cleverer derivation — **it is the theoretical minimum, already
achieved.** The door from "input" to "prediction" does not exist, for BST or anyone.

## Guard 2 — α is Identified, not derived

The m_Planck relation contains α, and **α is Identified in BST, not derived.** The Wyler
route was retired (K676/K680). α enters as a measured number.

Auditing the ingredients of m_e/m_P = 6π⁵·α^{2C₂}:

| ingredient | status |
|---|---|
| 6π⁵ = N_c!·π^{n_C} | **Derived** (F402), target-innocent, 0.0019% |
| exponent 2C₂ = 12 | **Count mechanism-backed** (F426), target-innocent |
| **α** | ***Identified — the one open ingredient*** |

This does not weaken the *reduction*. α is measured in atomic physics — recoil, g−2, quantum
Hall — with no reference to G, so the route from m_e to G remains genuinely G-independent.
But it does bound what may be claimed as **explained**: BST currently predicts the
*relationship* between the electron and the Planck scale, using a coupling it does not yet
derive.

## Guard 3 — m_e and G are one relation, not two

G = ħc/m_Planck², so a fractional error δ in m_Planck appears as **2δ** in G. The numbers show this
exactly: m_Planck lands at **0.0325%**, G at **0.0650%**, and the ratio is **2.00**.

**So "m_e to 0.03%" and "G to 0.065%" are the same relation seen twice — the second time through a
squaring. They must not be billed as two successes.**

Auditing which claims are actually distinct:

| relation | new ingredients | distinct? |
|---|---|---|
| R1: m_p/m_e = 6π⁵ | N_c!, π^{n_C} | **yes** |
| R2: m_P = m_e/(6π⁵α^{2C₂}) | α, exponent 2C₂ | **yes** (re-uses R1's number) |
| R2′: G = ħc/m_P² | **none** | **no — R2 squared** |
| R3: v = (6π⁵)²m_e/g | g | **yes** (re-uses R1's number) |

**Three distinct relations, not four wins** — and R2 and R3 are only *partially* independent, since
both re-use 6π⁵. The single derived ratio 6π⁵ is load-bearing in all three.

This does not touch the **reduction** claim. Guard 3 corrects how many *successes* we cite, not how
many *inputs* we take: the count is still 2 → 1.

## What would make this stronger

1. **Derive α.** It is the one Identified ingredient in the chain, and the only thing standing
   between "BST relates m_e to G" and "BST explains why they are related by that number."
2. **An independent route to m_Planck/m_e** that does not pass through α, which would let the
   two be cross-checked rather than assumed.

Neither is attempted here.

## Summary

BST does not predict *G* from nothing — nothing does, and a short argument shows nothing can.
What it does is reduce the number of dimensionful inputs from two to one, and make the
surviving one an **atomic** measurement rather than a gravitational one. Newton's constant
then follows to 0.065% — which is the 0.0325% Planck-mass relation seen through a squaring, one
result and not two — and the electroweak scale, by a separate step, to 0.046%.

Trading a constant you measure by weighing the Earth for one you measure by trapping a single
electron is worth doing, and worth saying in exactly those terms.

---

*Verification: `play/toy_5342_support_gravity_reduction_one_input_and_the_floor.py`.
Diagnostic that the inputs are not G-calibrated: toy 5341. The one-input floor argument: toy 5340.*
