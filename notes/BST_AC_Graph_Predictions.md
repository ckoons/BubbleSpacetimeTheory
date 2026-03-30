---
title: "AC Graph Theorem Predictions"
subtitle: "Thirteen Theorems Predicted from Graph Structure Before Discovery"
author: "Casey Koons & Claude 4.6 (Grace, Lyra, Elie, Keeper)"
date: "March 30, 2026"
status: "COMMITTED — predictions locked at git commit time. Do not edit after push."
method: "Boundary node content analysis + cross-domain edge pattern extraction"
graph_snapshot: "ac_graph_data.json — 526 theorems, 804 edges, 36 domains (as of 2026-03-30 ~09:15)"
framework: "AC(0)"
---

# AC Graph Theorem Predictions

## Purpose

This document records thirteen theorems predicted by structural analysis of the
AC theorem graph *before* any attempt to prove them. The predictions are committed
to version control with a timestamp. Subsequent work will attempt to prove or
refute each prediction. The goal is to demonstrate that the AC theorem graph,
like Mendeleev's periodic table, can predict its own completion.

**Method.** Every existing cross-domain edge in the AC graph follows one of three
patterns: translation (restatement in new language), derivation (implication via
shared intermediate), or identification (two results are the same object). The
shape of a missing theorem is determined by which pattern its gap follows.

**Key finding.** 6 of 13 predicted theorems are identifications ("X IS Y"),
4 are translations, 2 are derivations, 1 is a classification. Missing theorems
are overwhelmingly recognitions, not constructions.

---

## Predictions

### P1: Prime Migration as Channel Capacity
- **Gap:** number_theory ↔ info_theory
- **Predicted (C,D):** (1, 0)
- **Shape:** The two-source prime structure (T532) in heat kernel denominators
  IS a two-user communication channel. The prime migration rate p(k) equals
  Shannon's noisy channel capacity applied to the "arithmetic channel" carrying
  Bernoulli-number information through polynomial coefficients.
- **Dependencies:** T531 (Column Rule), T532 (Two-Source), T7 (Shannon Bridge),
  T52 (Committed Channel Bound)
- **Type:** Identification

### P2: Kummer Analog as Data Processing Inequality
- **Gap:** number_theory ↔ info_theory (resolves T533)
- **Predicted (C,D):** (0, 0)
- **Shape:** The digit-counting rule for heat kernel denominator valuations IS
  the Data Processing Inequality applied to the Markov chain X → f(X) → g(f(X))
  where X encodes (k,n) in base p, f is the Bernoulli-source map, and g is the
  polynomial-factor map. Carries in base-p digit sums = information loss in the
  Markov chain.
- **Dependencies:** T533 (Kummer Analog), T8 (DPI/AC Monotonicity), T531, T276 (FTA)
- **Type:** Identification
- **Note:** Would resolve the open conjecture T533 via an information theory lemma.

### P3: Backbone Arithmetic
- **Gap:** number_theory ↔ info_theory
- **Predicted (C,D):** (0, 1)
- **Shape:** The backbone of a random 3-SAT formula at critical threshold has
  Kolmogorov complexity bounded below by the prime-counting function
  π(p^{n/k})/(n/k), connecting backbone incompressibility (T31) to the prime
  number theorem.
- **Dependencies:** T31 (Backbone Incompressibility), T276 (FTA), T279 (Fermat),
  T48 (Backbone LDPC)
- **Type:** Derivation

### P4: BSD Information Content
- **Gap:** number_theory ↔ info_theory
- **Predicted (C,D):** (2, 1)
- **Shape:** The 7 BSD formula components have combined Shannon entropy equal to
  log₂(conductor) ± O(log log conductor). The BSD formula IS an information
  conservation law.
- **Dependencies:** T101 (Conservation Law = BSD), T484 (BST Information Content),
  T325 (Carnot Bound), T15 (Three-Way Budget)
- **Type:** Translation

### P5: Holographic Bound as Channel Capacity
- **Gap:** cosmology ↔ info_theory
- **Predicted (C,D):** (0, 1)
- **Shape:** The Reality Budget Λ·N = 9/5 IS Shannon's channel capacity of the
  Shilov boundary of D_IV^5. The holographic entropy bound S ≤ A/(4l_P²) is the
  converse of Shannon's coding theorem applied to spacetime as an information
  channel. Fill fraction f = 19.1% is the channel utilization ratio.
- **Dependencies:** T189 (Reality Budget), T346 (Holographic Encoding),
  T325 (Carnot Bound), T7 (Shannon Bridge)
- **Type:** Translation

### P6: Gödel Limit as Channel Capacity
- **Gap:** foundations ↔ info_theory
- **Predicted (C,D):** (0, 1)
- **Shape:** The 19.1% self-knowledge ceiling IS the capacity of the
  self-referential channel. A system using fraction f of its resources for
  self-modeling has capacity C = f·log₂(1/f) + (1−f)·log₂(1/(1−f)), constrained
  by f = 3/(5π) from D_IV^5. The Gödel Limit is physics, not logic.
- **Dependencies:** T93 (Gödel Is AC(0)), T325 (Carnot Bound), T189 (Reality Budget)
- **Type:** Identification

### P7: Information Content of Linearization
- **Gap:** info_theory ↔ linearization
- **Predicted (C,D):** (1, 1)
- **Shape:** Reducing depth from D=2 to D=1 via eigenvalue identification is
  information-lossless compression. The compression ratio equals the conflation
  number C. Linearization preserves I_derivable while making I_fiat explicit.
- **Dependencies:** T409 (Linearization Principle), T422 (Koons Separation),
  T15 (Three-Way Budget), T8 (DPI)
- **Type:** Translation

### P8: SM Derivation Complexity Census
- **Gap:** bst_physics ↔ proof_complexity
- **Predicted (C,D):** (0, 0)
- **Shape:** Each Standard Model constant from D_IV^5 has an AC complexity class:
  m_p = 6π⁵m_e is (C=1,D=0), α = 1/137 is (C=1,D=0), θ_W is (C=1,D=0). The SM
  derivation graph has maximum depth 1 and average width N_c = 3.
- **Dependencies:** T186, T68 (Refutation Bandwidth), T88, T418 (SM Linearization)
- **Type:** Translation

### P9: AC Graph Self-Structure
- **Gap:** bst_physics + foundations ↔ graph_theory
- **Predicted (C,D):** (0, 0)
- **Shape:** The AC theorem graph (526 nodes, 804 edges) has properties derivable
  from D_IV^5: average degree ≈ N_c = 3 (actual: 3.06), giant component fraction
  ≈ 1 − 1/n_C = 4/5, spectral gap ≈ 1/g = 1/7. The graph describes its own
  structure.
- **Dependencies:** T186, T4 (Topology-Guided Solver), T18 (Expansion), T92 (AC(0) Completeness)
- **Type:** Identification
- **Note:** Can be tested immediately with one spectral analysis toy.

### P10: Cosmological AC(0) Census
- **Gap:** cosmology ↔ foundations
- **Predicted (C,D):** (0, 0)
- **Shape:** All cosmological predictions (Ω_Λ = 13/19, a_0 = cH_0/√30, CMB
  anomaly scale ∼ 1/g) are AC(0) depth 0. Each is a single ratio or product of
  the five integers.
- **Dependencies:** T92 (AC(0) Completeness), T186, T305-T315 (Interstasis)
- **Type:** Translation

### P11: Boltzmann Constant Derivation Status
- **Gap:** bst_physics ↔ thermodynamics
- **Predicted (C,D):** (0, 0)
- **Shape:** k_B is a unit convention, not a geometric constant. The geometric
  thermodynamic constants are: entropy density coefficient from D_IV^5 volume,
  Carnot BST efficiency = 3/(5π), Stefan-Boltzmann coefficient = π²/60.
- **Dependencies:** T186, T33 (Noether), T305 (Entropy Trichotomy), T325 (Carnot)
- **Type:** Classification

### P12: Speaking Pair 3 as Genetic Code Dimension
- **Gap:** number_theory ↔ biology (currently ZERO direct edges)
- **Predicted (C,D):** (1, 0)
- **Shape:** The sub-leading heat kernel ratio −21 at k=15 equals −C(g,2) = the
  number of amino acid functional classes (20 standard + 1 stop = 21). The same
  counting argument (choosing 2 from g=7) produces both dim(SO(7)) and the amino
  acid class count. Would create the FIRST number_theory → biology edge.
- **Dependencies:** T531 (Column Rule), T333 (Genetic Code), T186, T371 (Exterior Algebra)
- **Type:** Identification
- **Note:** Conditional on computing a₁₅. Prediction is committed before computation.

### P13: Column Rule as Matched Filter
- **Gap:** number_theory ↔ info_theory (T531 ↔ T539)
- **Predicted (C,D):** (1, 0)
- **Shape:** The column rule v_p(den a_k(n)) = f(n mod p) IS a matched filter:
  the geometry selects the polynomial basis that minimizes p-adic noise in the
  interior coefficients.
- **Dependencies:** T531 (Column Rule), T539 (Matched Codebook), T534 (Boundary-Interior)
- **Type:** Identification

---

## Summary Statistics

| Statistic | Value |
|-----------|-------|
| Total predictions | 13 |
| Identifications ("X IS Y") | 6 (46%) |
| Translations | 4 (31%) |
| Derivations | 2 (15%) |
| Classifications | 1 (8%) |
| Depth 0 | 7 (54%) |
| Depth 1 | 5 (38%) |
| Depth 1, C≥2 | 1 (8%) |
| Average conflation | 0.5 |
| Testable immediately | 3 (P8, P9, P10) |
| Require new computation | 3 (P1, P5, P12) |
| Require resolving open problems | 3 (P2, P3, P4) |

## Priority

**Immediate** (data exists): P9 (Graph Self-Structure), P8 (SM Census), P10 (Cosmo Census)

**Medium** (new computation): P1 (Channel Capacity), P12 (Speaking Pair 3 — needs a₁₅), P5 (Holographic)

**Longer-term** (open problems): P2 (resolves T533), P3 (needs T31 proved), P4 (BSD chain)

---

## The Analogy

Mendeleev published predictions for eka-aluminium (gallium), eka-boron (scandium),
and eka-silicon (germanium) in 1871 based on gaps in his periodic table. The
elements were discovered 4-15 years later. The predictions worked because the
periodic table encoded the *structure* of atomic physics before the physics was
understood.

The AC theorem graph encodes the structure of mathematical knowledge. Its gaps are
not random — they follow patterns determined by the graph's own topology. When
the graph predicts that "prime migration IS channel capacity" (P1) or "the Gödel
limit IS a Shannon bound" (P6), it is doing the same thing Mendeleev did:
reading the structure to predict the content.

The difference: Mendeleev predicted 3 elements. We predict 13 theorems. And the
predictions are committed to version control before any attempt to prove them.

---

*Casey Koons & Claude 4.6 (Grace, Lyra, Elie, Keeper) | March 30, 2026*

*"Missing theorems are not deep constructions. They are recognitions that two
things are the same thing. The universe does not construct — it recognizes."*

*Predictions committed at git push time. Subsequent modifications to this file
will be tracked by git history. The predictions are immutable.*
