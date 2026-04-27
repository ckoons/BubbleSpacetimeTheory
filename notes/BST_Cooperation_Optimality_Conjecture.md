---
title: "Cooperation Optimality Conjecture"
author: "Keeper (from Casey's Board directive)"
date: "April 3, 2026"
status: "CONJECTURE — candidate for T709"
depth: "D=0"
feeds: "Paper #19 Section 4, Paper #8"
---

# Cooperation Optimality: Competition Is a Coordinate Error

## Conjecture Statement

**Competition is not a strategy — it is a coordinate error.** In a system with permanent observers (T319) and nonzero Gödel limit (f > 0, T317), cooperation strictly dominates at AC depth 0.

## Proof Sketch (D=0)

1. **Observers are permanent** (T319): Each observer persists through infinite rounds.
2. **Gödel limit** (T317): Every observer has blind fraction f ≈ 19.1%. No exception.
3. **Coverage under cooperation**: N cooperating observers cover fraction 1 - (1-f)^N → 1 exponentially.
4. **Coverage under competition**: Each defector still covers only f. No improvement from others' work.
5. **Expected return**: Cooperator gains access to (1-f^N) of knowledge space. Defector gains f.
6. Since f < 1 and N ≥ 2, cooperation strictly dominates. QED.

## The Coordinate Error

Competition treats the knowledge space as zero-sum: "if you know more, I know less." But the knowledge commons (T669) is **non-depleting**: sharing a proved theorem costs the sharer nothing and gains the receiver everything. This is not economics — it is counting.

Zero-sum framing is a **coordinate error**: it applies the wrong metric to a compounding space. The error is structural, not moral. A cooperator in the correct coordinate frame; a competitor in the wrong one.

## BST Expression

The cooperation surplus for N observers:

$$\Delta_N = \left(1 - f^N\right) - f = f\left(\frac{1 - f^N}{f} - 1\right)$$

For N=2: Δ₂ = 1 - f² - f = f(1-f) ≈ 0.155 (15.5% surplus)
For N=5: Δ₅ = 1 - f⁵ - f ≈ 0.808 (80.8% surplus)

The surplus is monotone increasing in N. Competition (N=1 effective) gives Δ₁ = 0.

## Depth Analysis

- Step 1: T319 (definition, D=0)
- Step 2: T317 (definition, D=0)
- Step 3: Counting (D=0)
- Step 4: Counting (D=0)
- Step 5: Comparison (D=0)
- Step 6: Inequality (D=0)

**Total depth: 0.** No composition required. The result follows from definitions and counting.

## Falsification

If any bounded system with permanent observers and nonzero blind fraction achieves higher long-run knowledge coverage through competition than cooperation, this conjecture fails.

## Connection to Great Filter

This is why the cooperation gap (T703, Δf = 1.53%) determines survival: civilizations that read the zero-sum coordinate die not because competition is evil, but because it is **wrong** — wrong in the mathematical sense of applying the wrong metric. The Great Filter is a coordinate error.

---

*"Competition doesn't lose — it miscounts."*

**Footer**: Conjecture v1. (C=0, D=0). Keeper. Feeds Paper #19 Section 4 + Paper #8.
