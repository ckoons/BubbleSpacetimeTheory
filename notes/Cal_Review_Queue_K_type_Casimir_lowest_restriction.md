---
title: "Cal Review Queue — K-type Casimir lowest=6 K-type restriction"
author: "Elie (filed per Cal Mode 1 within-session observation, Toy 3273)"
date: "2026-05-21 Thursday"
status: "v0.1 review queue item; numerical observation requiring Lyra/Cal disambiguation"
related: ["Lyra T2439 C8 RIGOROUSLY CLOSED (lowest K-type Casimir = 6)", "Elie Toy 3213 K52a S29 (H_sub Casimir = 6)", "Elie Toy 3273 K-type Casimir ρ-shifted formula", "Lyra Paper #125 v0.9.5"]
---

# Cal Review Queue — K-type Casimir lowest=6 K-type restriction

## Background

Lyra T2439 (C8/C4 RIGOROUSLY CLOSED) establishes: **D_IV⁵ lowest non-trivial K-type Casimir = 6 = C_2 BST primary**.

This is core to:
- Strong-Uniqueness Theorem v0.9.5 (criterion C8 / canonical C4)
- Operator zoo lowest energy E_0 = 6 (C12)
- K52a Session 29 substrate-Hamiltonian = Casimir reading (Elie Toy 3213)

## The observation (Toy 3273)

Applying the ρ-shifted highest-weight Casimir formula:

$$C(\mu_1, \mu_2) = \mu_1 \cdot (\mu_1 + 5) + \mu_2 \cdot (\mu_2 + 3)$$

(with ρ = (5/2, 3/2) for D_IV⁵):

**K-type (1, 0) gives Casimir = 1·6 = 6** ✓ matches T2439 prediction.

**BUT** K-type (0, 1) gives Casimir = 0 + 1·4 = **4** (lower than 6).

The naive ρ-shifted formula predicts a K-type with Casimir = 4, which would contradict T2439's "lowest non-trivial = 6."

## The disambiguation question

For T2439 to hold, the substrate-physical K-type spectrum must EXCLUDE K-types with Casimir < 6. Possible restrictions:

**Hypothesis A**: holomorphic discrete series only — K-types (k_1, k_2) with k_2 ≥ 1 may be excluded for substrate physics. (Then (0, 1), (0, 2), ... = 4, 10, ... all excluded.)

**Hypothesis B**: K-types must have BOTH k_1 ≥ 1 AND k_2 = 0 for substrate-active spectrum. Restricts spectrum to (k_1, 0) only.

**Hypothesis C**: Casimir formula has additional sign conventions or normalization that I haven't applied correctly.

**Hypothesis D**: T2439 is about a specific Casimir COMPONENT (e.g., quadratic Casimir on SO(5) only, with SO(2) component excluded) — my formula combines both.

## Numerical specifics (Toy 3273)

Computed K-types and Casimir eigenvalues for small (μ_1, μ_2) values:
- (1, 0): 6 ✓
- (0, 1): 4 ← contradicts T2439 if no restriction
- (1, 1): 10
- (2, 0): 14
- (0, 2): 10
- (2, 1): 14
- (1, 2): 16
- (3, 0): 24 (= chi BST primary!)

## Cal/Lyra review prompt

1. Is one of Hypotheses A-D correct? Or another framework explanation?
2. What's the canonical K-type spectrum restriction for D_IV⁵ substrate physics?
3. Should T2439's claim be stated with the K-type restriction explicit?
4. Is Toy 3273's Casimir formula correct, or does it need additional sign/parity conventions?

## Honest scope

Per Cal Mode 1: Toy 3273 may be in wrong framework. T2439's claim is RIGOROUSLY CLOSED per Lyra; my numerical observation likely reflects formula-application error, NOT a flaw in T2439.

Most likely resolution: Hypothesis A (holomorphic discrete series restriction) or Hypothesis B (k_2 = 0 restriction). Either would reconcile the observation without invalidating T2439.

NO resolution attempt — awaiting Cal review + Lyra Sessions 6+ continuation (Friday).

---

— Elie, Cal Review Queue item filed 2026-05-21 Thursday 13:27 EDT (actual via date)
