---
title: "BST — Zonal Spectral Coefficients of Q⁵"
author: "Casey Koons & Claude 4.6"
date: "March 2026"
---

# BST — Zonal Spectral Coefficients of Q⁵

**The heat trace on the BST quadric encodes BST integers.**

*Created March 14, 2026 — Claude Opus 4.6*

---

## 1. Setup

The zonal heat trace on Q⁵ = SO(7)/[SO(5)×SO(2)] is:

$$Z_0(t) = \sum_{k=0}^{\infty} d(k)\, e^{-k(k+5)t}$$

where $d(k) = \binom{k+4}{4}(2k+5)/5$ is the zonal degeneracy (dimension of the
$(k,0,0)$ representation of SO(7)).

The **effective spectral dimension** is $d_{\text{eff}} = 6$ (not 10), and the
expansion takes the form:

$$t^3 Z_0(t) = \frac{1}{60}\bigl[1 + r_1 t + r_2 t^2 + r_3 t^3 + \cdots\bigr]$$

## 2. Exact Coefficients

| k | $r_k$ (exact) | Decimal | BST identification |
|---|---|---|---|
| 0 | 1 | 1 | trivial |
| 1 | 5 | 5 | $n_C = c_1$ |
| 2 | 12 | 12 | $2C_2 = c_1^2 - c_3$ |
| 3 | 1139/63 | 18.0794 | see §4 |
| 4 | 833/45 | 18.5111 | $(g^2 \times 17)/(9 \times n_C)$ |
| **5** | **137/11** | **12.4545** | **$N_{\max}/c_2$** |
| 6 | 485768/135135 | 3.5947 | (requires B₁₂) |
| 7 | −90502/27027 | −3.3486 | (asymptotic oscillation) |

**All values r₃ through r₅ are exact** (verified with Fraction arithmetic).

## 3. The r₅ = 137/11 Identity

The fifth zonal coefficient equals:

$$\boxed{r_5 = \frac{137}{11} = \frac{N_{\max}}{c_2} = \frac{n_C^3 + 2C_2}{c_2}}$$

where:
- **137** = BST fine structure maximum ($\alpha^{-1} \approx 137.036$)
- **11** = second Chern class $c_2(Q^5)$ = dim(SO(5)×SO(2))
- **137 = 5³ + 12 = r₁³ + r₂**: the cube of the first coefficient plus the second

### 3.1. Emergence of 137

The coefficient EM₂ (which gives r₅ = 60 × EM₂) arises from four Bernoulli-weighted
terms in the Euler-Maclaurin expansion:

| Term | Bernoulli | f-derivative at t² | Value |
|---|---|---|---|
| j=2 | $-B_4/4! = 1/720$ | $f'''(0)\big|_{t^2} = 865/4$ | $173/576$ |
| j=3 | $-B_6/6! = -1/30240$ | $f^{(5)}(0)\big|_{t^2} = 3024$ | $-1/10$ |
| j=4 | $-B_8/8! = 1/1209600$ | $f^{(7)}(0)\big|_{t^2} = 8820$ | $7/960$ |
| j=5 | $-B_{10}/10! = -1/47900160$ | $f^{(9)}(0)\big|_{t^2} = 3024$ | $-1/15840$ |

$$\text{EM}_2 = \frac{173}{576} - \frac{1}{10} + \frac{7}{960} - \frac{1}{15840} = \frac{6576}{31680} = \frac{137}{660}$$

with $\gcd(6576, 31680) = 48$ and $6576 = 48 \times 137$. The prime 137 is irreducible.

Then $r_5 = 60 \times 137/660 = 137/11$.

### 3.2. Uniqueness to Q⁵

Computed r₅ for other complex quadrics Q^n:

| n | r₅ | Numerator | Contains 137? |
|---|---|---|---|
| 3 | 358/3465 | 358 = 2 × 179 | No |
| **5** | **137/11** | **137 (prime)** | **Yes** |
| 7 | 34004/99 | 34004 = 4 × 8501 | No |
| 9 | 2046263/495 | 2046263 | No |

The number 137 appears **only** for Q⁵ — the BST quadric.

## 4. The r₃ Sign Error Resolution

The previous session found r₃ ≈ 18.08 (Richardson) but computed r₃ = 1076/63 ≈ 17.08
from Euler-Maclaurin — a discrepancy of exactly 1.0.

**Root cause**: sign error in the B₄ term. The correct one-sided EM formula:

$$\text{EM} = \frac{f(0)}{2} - \sum_{j \geq 1} \frac{B_{2j}}{(2j)!}\, f^{(2j-1)}(0)$$

Since B₄ = −1/30, the j=2 term is $-B_4/4! = +1/720$ (positive). The previous code
used $-1/720$ (negative), flipping the sign of $d'''(0)/720 = 6/720 = 1/120$.

$$r_3 = 1139/63 = 1076/63 + 60 \times \frac{2}{720} \times 6 = 1076/63 + 1$$

**Corrected**: $r_3 = 1139/63 = 18.079\overline{365079}$

Decomposition: $r_3 = 30 - 149/12 + 1/2 - 1/252$

where $d'(0) = 149/60 = H_4 + 2/5$, $d'''(0) = 6 = C_2$, $d^{(5)}(0) = 2 = r$.

## 5. Structure Theorem

**Integral-EM decomposition**: The expansion $t^3 Z_0(t) = \sum b_k t^k$ splits as:

$$b_k = \begin{cases} c_k^{\text{int}} & k = 0, 1, 2 \\[4pt] \text{EM}_{k-3}(0) & k \geq 3 \end{cases}$$

The **integral contributes nothing** beyond $r_2$. All higher coefficients arise
entirely from the Euler-Maclaurin boundary correction at x = 0. Verified numerically:
$c_k^{\text{int}} < 10^{-10}$ for $k = 3, 4, 5$.

This means:
- $r_0, r_1, r_2$ encode the **bulk geometry** (volume, scalar curvature, quadratic invariants)
- $r_k$ for $k \geq 3$ encode **boundary corrections** — the discreteness of the spectrum
  vs the continuum approximation

## 6. Degeneracy Polynomial

$d(x) = (x+1)(x+2)(x+3)(x+4)(2x+5)/120$

Key values at $x = 0$:
- $d(0) = 1$
- $d'(0) = 149/60 = H_4 + 2/5$ (harmonic number + shift)
- $d''(0) = 55/12$
- $d'''(0) = 6 = C_2$
- $d^{(4)}(0) = 5$
- $d^{(5)}(0) = 2 = r$ (rank of $D_{IV}^5$)

The BST integers C₂ = 6 and r = 2 appear as the third and fifth derivatives of
the zonal degeneracy polynomial at the origin.

## 7. Files

- `play/verify_r3_sign.py` — verification of r₃ = 1139/63, sign error analysis
- `play/em_complete.py` — full EM expansion with proper Bernoulli terms
- `play/em_higher_order.py` — initial higher-order computation
- `play/compare_quadrics.py` — comparison across Q³, Q⁵, Q⁷, Q⁹
- `play/extract_zonal_coefficients.py` — Richardson extrapolation tools
- `play/refine_zonal_b3.py` — numerical refinement of b₃

## 8. Open Questions

1. **Is r₅ = N_max/c₂ a coincidence?** The number 137 is prime and emerges from a
   specific Bernoulli-weighted sum. It appears only for Q⁵ among all quadrics tested.
   The decomposition 137 = n_C³ + 2C₂ connects it to the first two BST integers.

2. **Generating function**: Is there a closed form for $\sum r_k t^k / k!$?
   At $t = 1$: $\sum_0^5 r_k/k! \approx 15.89$.

3. **Asymptotic behavior**: The series $\{r_k\}$ oscillates and diverges for large k
   (characteristic of EM/Bernoulli asymptotic series). What is the optimal truncation
   order? The "superasymptotic" truncation at the smallest term may encode additional
   physics.

4. **Connection to Plancherel measure**: The continuum integral $I(t)$ is related to
   the Plancherel measure on $D_{IV}^5$. The EM corrections encode how the discrete
   spectrum differs from the continuum — this is precisely the "fill fraction" structure.
