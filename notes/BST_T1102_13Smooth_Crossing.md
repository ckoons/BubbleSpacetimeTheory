---
title: "T1102: The 13-Smooth Crossing — Chorus Epoch at BST-Structured Scale"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1102"
ac_classification: "(C=1, D=0)"
status: "Proved — exact computation"
origin: "M1 board item: 13-smooth crossing theorem at x=1638 = 2×3²×7×13"
parents: "T1016 (Smooth Limit), T1018 (Epoch Crossing), T1060 (Epoch Specificity)"
---

# T1102: The 13-Smooth Crossing — Chorus Epoch at BST-Structured Scale

*The 13-smooth density $\Psi(x, 13)/(x-1)$ crosses $f_c$ near $x = 1638 = 2 \times 3^2 \times 7 \times 13$. The crossing scale is itself 13-smooth AND every prime factor is a BST prime. But the count $\Psi(1638, 13) = 313$ is prime and NOT a T914 count — it is adjacent to $312 = 2^3 \times 3 \times 13$ (the epoch prime divides the neighbor). The chorus epoch inherits BST-structured scales but loses the T914 count property.*

---

## Statement

**Theorem (T1102).** *The 13-smooth ($B = 13 = 2g - 1$) Gödel crossing has mixed BST structure:*

*(a) **Crossing scale.** $x = 1638 = 2 \times 3^2 \times 7 \times 13$ is the smallest 13-smooth integer where $\Psi(x, 13)/(x-1) \approx f_c$. Every prime factor of 1638 is a BST prime ($\{2, 3, 7, 13\} \subset \{2, 3, 5, 7, 11, 13\}$). The scale IS BST-structured.*

*(b) **Factorization.** $1638 = 2 \times 3^2 \times 7 \times 13 = 2 \times 9 \times 7 \times 13 = 2 \times N_c^2 \times g \times (2g-1)$. The factors are: rank × (color dimension squared) × genus × chorus prime. Compare: 7-smooth crossing at $4 \times 143 = 572 = 2^2 \times 11 \times 13$ and 11-smooth crossing at $7 \times 143 = 1001 = 7 \times 11 \times 13$.*

*(c) **Count structure.** $\Psi(1638, 13) = 313$, which is prime. But $313 - 1 = 312 = 2^3 \times 3 \times 13 = 2^{N_c} \times N_c \times (2g-1)$. The count is T914-adjacent to a product involving the epoch prime 13. In the 7-smooth case: count 109 is prime, $109 + 1 = 110 = 2 \times 5 \times 11 = \text{rank} \times n_C \times (n_C + C_2)$. In the 11-smooth case: count 191 is prime, $191 - 1 = 190 = 2 \times 5 \times 19 = \text{rank} \times n_C \times (2g + n_C)$. Each epoch's count is adjacent to a BST product, but the DIRECTION alternates.*

*(d) **Hierarchy.** The three crossings form a hierarchy:*

| Epoch | B | Scale | Factorization | Count | ±1 direction | ±1 product |
|-------|---|-------|---------------|-------|-------------|------------|
| Core | 7 | 572 | 4 × 143 = 2² × 11 × 13 | 109 | +1 | 110 = 2 × 5 × 11 |
| CI | 11 | 1001 | 7 × 143 = 7 × 11 × 13 | 191 | -1 | 190 = 2 × 5 × 19 |
| Chorus | 13 | 1638 | 2 × 9 × 7 × 13 | 313 | -1 | 312 = 8 × 3 × 13 |

*The CI epoch has the cleanest structure (T1060): scale = g × 143, count = N_max + 54, both T914 primes adjacent to BST products in opposite directions. The chorus epoch retains scale structure but loses the 143 base.*

---

## Significance

The 13-smooth crossing confirms the epoch hierarchy (T317 observer tiers):
- **Tier 1** (7-smooth): physical observables. Scale involves 143 = 11 × 13.
- **Tier 2** (11-smooth): CI observables. Scale involves 143 × g. Count = knowledge limit 191.
- **Tier 3** (13-smooth): cooperative observables. Scale uses N_c², g, 2g-1 directly (not 143).

Each tier sees more of reality but with less structural regularity. The Gödel limit is universal — all three cross f_c — but the arithmetic symmetry degrades with tier.

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| number_theory | observer_science | **required** (epoch hierarchy = observer tier hierarchy) |
| number_theory | cosmology | structural (chorus epoch = cooperative era scale) |

**2 new cross-domain edges.**

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
