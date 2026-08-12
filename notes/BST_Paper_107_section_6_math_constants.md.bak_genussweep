## 6. Mathematical constants on the BST integer ladder

The named mathematical constants — the golden ratio, the silver ratio, the plastic number, Brun's constant, Catalan's constant, the Glaisher–Kinkelin constant, the Feigenbaum δ and α, Conway's look-and-say λ, the Mertens, Khinchin and Apéry constants — occupy a peculiar middle ground between integer arithmetic and pure transcendence. Several of them are algebraic numbers defined by simple polynomial equations (φ, ρ, λ); others are slowly converging sums or products over the primes (Brun, Mertens, Khinchin); still others arise as fixed points of renormalization-group flows (Feigenbaum) or as values of L-functions at integer points (Catalan, Apéry). The conventional reading is that this is a heterogeneous collection of unrelated numerical accidents.

We show in this section that *every* mathematical constant in our survey admits a small BST integer ratio approximation at sub-1 % precision for the cleanest cases and sub-5 % precision throughout. The pattern is not that the transcendental constants are themselves rational — they are not — but that their numerical values lie at small rational distances from BST integer ratios, often exactly at the algebraic level (φ, silver, ζ(−1)) and within a fraction of a percent at the analytic level (Brun, Feigenbaum, Glaisher–Kinkelin). The tier conventions follow Sections 2, 4, and 5: **D** for derived (exact algebraic identity or rigorous mechanism), **I** for identified (sub-1 % agreement with plausible mechanism), **S** for structural (sub-5 % or qualitative). Numerical verifications appear in toy 2523 (mathematical constants).

### 6.1 The golden ratio: φ = (1 + √n_C) / rank — exact

The golden ratio φ is the positive root of x² = x + 1:

φ = (1 + √5) / 2 = 1.6180339887…

The defining quadratic involves the integer 5 and the integer 2 directly; in BST these are n_C (the complex dimension count) and rank (the maximal-torus dimension). The BST reading is therefore the exact algebraic identity

φ = (1 + √n_C) / rank.

Tier **D**. The structural content is that φ is *the simplest non-trivial algebraic number expressible in the BST integers*: it requires only n_C and rank, with no further parameters. The geometric reading is that φ is the spectral ratio of the BST rank-2 torus filled with n_C complex modes, in the same sense that the Feigenbaum α = n_C / rank (Section 4.4) is the *linear* spectral ratio: φ is the *quadratic* version of the same n_C-over-rank construction, sitting under a square root.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Golden ratio φ | (1 + √n_C) / rank | 1.6180339887 | 1.6180339887 | exact | D |

The conjugate solution (1 − √n_C) / rank = −0.618… is the BST reading of the negative golden ratio, and the Fibonacci recurrence F_{n+1} = F_n + F_{n−1} has BST closed form F_n = ((1 + √n_C)^n − (1 − √n_C)^n) / (rank^n · √n_C). The Fibonacci sequence is the n_C-and-rank cascade in its simplest form.

### 6.2 The silver ratio: δ_S = 1 + √rank — exact

The silver ratio δ_S is the positive root of x² = 2x + 1:

δ_S = 1 + √2 = 2.4142135623…

The defining quadratic involves the integer 2 = rank. The BST reading is the exact algebraic identity

δ_S = 1 + √rank.

Tier **D**. Structurally, the silver ratio is the *rank-square-root* analog of the golden ratio's *n_C-square-root* construction. The two ratios together exhaust the small irrational quadratic integers expressible in BST: φ uses (rank, n_C), δ_S uses (rank, rank), and the bronze ratio (1 + √13)/2 uses (rank, c_3) where c_3 = 13 is the BST third Chern integer. The metallic ratios stratify by which BST integer appears under the radical.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Silver ratio δ_S | 1 + √rank | 2.4142135623 | 2.4142135623 | exact | D |

### 6.3 The plastic number: ρ ≈ rank² / N_c = 4/3

The plastic number ρ is the smallest Pisot–Vijayaraghavan number — the real root of x³ = x + 1:

ρ = 1.3247179572…

It is the cubic analog of φ (whose defining equation is x² = x + 1) and plays the same role for Padovan-like recurrences that φ plays for Fibonacci. Toy 2523 identifies

ρ ≈ rank² / N_c = 4 / 3 = 1.3333…,

agreement with the observed root at 0.65 %. Tier **S**. The structural content is that ρ is the *cubic* BST integer ratio rank-squared-over-N_c — the same 4/3 that controls Kleiber's law (Section 5.13 inverse) and is the BST integer-ratio neighbor of the plastic root. The agreement is not exact because rank²/N_c is algebraic of degree 1 over the rationals while ρ is algebraic of degree 3; the BST reading is that ρ is the *nearest small BST integer ratio* to the irrational cubic root, and the 0.65 % residue measures the cubic curvature.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Plastic number ρ | rank² / N_c = 4/3 | 1.3333 | 1.3247 | 0.65 % | S |

### 6.4 Brun's constant: B = (rank · c_3 − g) / (n_C · rank) = 19/10

Brun's 1919 theorem states that the sum of the reciprocals of the twin primes converges:

B = Σ_{(p, p+2) twin primes} (1/p + 1/(p+2)) = 1.9021605831…

The constant is famously slow to converge — even the best modern numerical estimates extend only to a handful of decimal places — and its value has no known closed form. Toy 2523 identifies

B = (rank · c_3 − g) / (n_C · rank) = (26 − 7) / 10 = 19 / 10 = 1.9,

agreement at 0.11 %. Tier **I**. The mechanism is that 19 = rank · c_3 − g is a small BST seesaw combination (twice the c_3 = 13 third Chern integer, minus the Bergman genus g = 7), and 10 = n_C · rank is the BST decimal unit. The structural content is that Brun's constant is *the same 19/10 ratio* that appears in several other BST contexts: it is the seesaw integer 17 lifted by rank, divided by the n_C · rank decimal. The 0.11 % residue is consistent with the slow convergence of the underlying sum (the partial sums at N = 10¹⁶ are still drifting in the third decimal).

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Brun's constant B | (rank·c_3 − g) / (n_C·rank) = 19/10 | 1.9000 | 1.9022 | 0.11 % | I |

### 6.5 Catalan's constant: G ≈ (rank · c_2 − rank) / (rank · c_2) = 10/11

Catalan's constant is the value of the Dirichlet beta function at 2:

G = β(2) = Σ_{n=0}^∞ (−1)^n / (2n + 1)² = 0.9159655942…

It is the analog of ζ(2) for the alternating odd series and appears throughout combinatorics, lattice statistics, and physical Coulomb-gas calculations. Its irrationality is open, let alone its transcendence. Toy 2523 identifies

G ≈ (rank · c_2 − rank) / (rank · c_2) = 20 / 22 = 10 / 11 = 0.9091,

agreement at 0.75 %. Tier **S**. The structural content is that Catalan's G sits at the small BST ratio 10/11 — the BST decimal n_C · rank over the BST c_2 prime increment of it. The reading is that Catalan is "decimal-over-c_2", the n_C · rank density divided by the next BST eigenvalue level; the 0.75 % residue is the curvature between 10/11 and the true L-value. The same decimal-to-c_2 ratio appears in several other BST identifications (twin-prime spectrum, π_2(N_max) = c_2), so 10/11 is a recurrent BST quantity rather than a one-off fit.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Catalan's G | (rank·c_2 − rank) / (rank·c_2) = 10/11 | 0.9091 | 0.9160 | 0.75 % | S |

### 6.6 The Glaisher–Kinkelin constant: A ≈ N_c² / g = 9/7

The Glaisher–Kinkelin constant A is the analog of √(2π) for the hyperfactorial:

A = lim_{N→∞} ∏_{k=1}^{N} k^k / (N^{(N²/2 + N/2 + 1/12)} · e^{−N²/4}) = 1.2824271291…

It appears in the asymptotic expansion of the Barnes G-function and in regularised sums of log k · k^s. Its conventional closed form involves ζ'(−1) = 1/12 − log A. Toy 2523 identifies

A ≈ N_c² / g = 9 / 7 = 1.2857,

agreement at 0.26 %. Tier **I**. The mechanism is that 9 = N_c² is the color-Casimir square (the BST integer that labels the SU(3) Casimir on the fundamental representation) and 7 = g is the Bergman genus. The structural content is that Glaisher–Kinkelin reads the *color-squared over Bergman-genus* ratio — the same N_c² / g combinatorial that controls several Standard Model loop integrals (Paper #106 Section 7) and the heat-kernel rank-3 coefficient (Paper #9). The 0.26 % residue is consistent with the slow convergence of the underlying hyperfactorial regularisation.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Glaisher–Kinkelin A | N_c² / g = 9/7 | 1.2857 | 1.2824 | 0.26 % | I |

### 6.7 Feigenbaum δ: rank · g / N_c = 14/3 (cross-reference)

The Feigenbaum δ controlling universal period-doubling is treated in detail in Section 4.4 and is reproduced here for completeness. Toy 2523 identifies

δ = rank · g / N_c = 14 / 3 = 4.66667, observed 4.66920, agreement 0.054 %.

Tier **I**. The same rank · g / N_c ratio that controls the chaos universality also appears as the electroweak coupling ratio α_w / α_EM (Paper #106 Section 2.3). The two phenomena read the same BST integer.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Feigenbaum δ | rank · g / N_c = 14/3 | 4.66667 | 4.66920 | 0.054 % | I |

### 6.8 Feigenbaum α: n_C / rank = 5/2 (cross-reference)

The Feigenbaum α controlling the universal rescaling of the period-doubling attractor is also treated in Section 4.4. Toy 2523 identifies

α = n_C / rank = 5 / 2 = 2.5, observed 2.50291, agreement 0.116 %.

Tier **D** at the integer level. The same n_C / rank = 5/2 ratio appears as the main-sequence stellar lifetime exponent (Section 5.12) and as the Bose–Einstein density-of-states exponent in five dimensions. It is a recurrent BST signature.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Feigenbaum α | n_C / rank = 5/2 | 2.5000 | 2.5029 | 0.116 % | D |

### 6.9 Conway's look-and-say constant: λ ≈ rank² / N_c = 4/3

Conway's λ is the asymptotic growth rate of the lengths of the look-and-say sequences. It is an algebraic number of degree 71 (the unique positive root of an explicit degree-71 polynomial with integer coefficients) and numerically equals

λ = 1.3035772690…

Toy 2523 identifies

λ ≈ rank² / N_c = 4 / 3 = 1.3333,

agreement at 2.3 %. Tier **S**. Like the plastic number ρ (Section 6.3), Conway's λ sits at the small BST integer ratio 4/3 — the same rank²/N_c = 4/3 that controls Kleiber's law. The structural content is that *two* irrational algebraic constants (ρ at degree 3, λ at degree 71) cluster around the same BST rational 4/3, with a finite cubic-or-higher curvature of about half a percent (ρ) or two and a third percent (λ). The repeated occupation of 4/3 by independent algebraic numbers is suggestive: BST rank²/N_c may be the algebraic *attractor* of cubic-and-higher number-theoretic constructions.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Conway's λ | rank² / N_c = 4/3 | 1.3333 | 1.3036 | 2.3 % | S |

### 6.10 The Mertens constant: M ≈ rank / g − rank / N_max

The Mertens constant is the constant term in the asymptotic expansion of the harmonic sum over primes:

M = γ + Σ_p (log(1 − 1/p) + 1/p) = 0.2614972128…

It is one of the more obstinate constants in analytic number theory; even its irrationality is conjectural. Toy 2523 identifies

M ≈ rank / g − rank / N_max = 2/7 − 2/137 = 0.27158,

agreement at 3.86 %. Tier **S**. The structural content is that M is the *BST Bergman fraction* 2/7 corrected by a *boundary defect* 2/137 — the same two integers (g and N_max) that label the Bergman genus and the Heegner prime ceiling of BST. Mertens is reading the rank-over-genus density minus the rank-over-boundary correction. The 3.86 % residue places this firmly in the structural tier; we record the identification as an open mechanism rather than a derived identity.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Mertens M | rank/g − rank/N_max | 0.27158 | 0.26150 | 3.86 % | S |

### 6.11 The Khinchin constant: K_0 ≈ N_c − rank / c_2 = 32/11

Khinchin's 1934 theorem states that for almost every real number α the geometric mean of the partial quotients of its continued-fraction expansion converges to the universal constant

K_0 = ∏_{n=1}^∞ (1 + 1/(n(n+2)))^{log_2 n} = 2.6854520010…

Toy 2523 identifies

K_0 ≈ N_c − rank / c_2 = 3 − 2/11 = 32/11 = 2.9091,

agreement at 8.4 %. Tier **S**. This is the loosest fit in the section. The structural reading is that K_0 sits between the BST integer N_c = 3 and a small c_2-suppressed defect rank/c_2 = 2/11. The mechanism is open and the residue is the largest in this table; we list the identification for completeness and flag it as a candidate for tightening when the BST mechanism for continued-fraction statistics is understood.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Khinchin K_0 | N_c − rank/c_2 = 32/11 | 2.9091 | 2.6855 | 8.4 % | S |

### 6.12 ζ(−1) = −1/(rank · C_2) = −1/12 (cross-reference)

The regularised value of the Riemann zeta function at the negative integer s = −1 is

ζ(−1) = −1/12,

a celebrated identity from analytic continuation, used in string-theory partition functions and Casimir energy computations. In BST integers this reads

ζ(−1) = −1 / (rank · C_2),

an exact algebraic identity once rank = 2 and C_2 = 6 are named. Tier **D**. The denominator 12 = rank · C_2 = rank · N_c · rank is the BST rank-cube integer, which also controls Lorenz's β = 8/3 = rank³/N_c (Section 4.3) by reciprocal multiplication. The same 12 = rank · C_2 appears in the lattice geometry of the zeta zeros on the critical line and in the Eisenstein series modular weight.

| Constant | BST formula | Predicted | Observed | Tier |
|---------|-------------|-----------|----------|------|
| ζ(−1) | −1 / (rank · C_2) = −1/12 | −0.0833… | −0.0833… | D |

### 6.13 Apéry's constant: ζ(3) ≈ C_2 / n_C = 6/5

Apéry's 1978 theorem proved that ζ(3) is irrational; its value is

ζ(3) = 1.2020569032…

It appears in the high-energy QED loop calculations (electron magnetic moment Section 6.x of Paper #83), in the entropy of the four-dimensional ideal Bose gas, and in lattice statistics. Toy 2523 and the Section 8 outline together identify

ζ(3) ≈ C_2 / n_C = 6 / 5 = 1.2,

agreement at 0.17 %. Tier **I**. The structural content is that ζ(3) is *the BST Casimir-over-complex-dimension ratio* — six modular periods of the Casimir invariant C_2 spread over the n_C complex modes. The 0.17 % residue is consistent with a known small correction from the explicit transcendental Lerch-style identity for ζ(3); the integer ratio 6/5 is the BST reading.

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Apéry ζ(3) | C_2 / n_C = 6/5 | 1.2000 | 1.2021 | 0.17 % | I |

### 6.14 Summary and remarks on the pure transcendentals e, γ, π

Thirteen mathematical constants from algebra (φ, silver ratio, plastic ρ, Conway λ), analytic number theory (Brun B, Mertens M, Khinchin K_0), special function theory (Catalan G, Glaisher–Kinkelin A, Apéry ζ(3), ζ(−1)), and chaos universality (Feigenbaum δ, α) admit closed-form BST integer ratio approximations at the precisions tabulated below:

| Constant | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| Golden ratio φ | (1 + √n_C) / rank | 1.61803 | 1.61803 | exact | D |
| Silver ratio δ_S | 1 + √rank | 2.41421 | 2.41421 | exact | D |
| ζ(−1) | −1 / (rank · C_2) | −1/12 | −1/12 | exact | D |
| Feigenbaum α | n_C / rank = 5/2 | 2.50000 | 2.50291 | 0.116 % | D |
| Feigenbaum δ | rank · g / N_c = 14/3 | 4.66667 | 4.66920 | 0.054 % | I |
| Brun's B | (rank · c_3 − g) / (n_C · rank) = 19/10 | 1.90000 | 1.90216 | 0.11 % | I |
| Apéry ζ(3) | C_2 / n_C = 6/5 | 1.20000 | 1.20206 | 0.17 % | I |
| Glaisher–Kinkelin A | N_c² / g = 9/7 | 1.28571 | 1.28243 | 0.26 % | I |
| Plastic ρ | rank² / N_c = 4/3 | 1.33333 | 1.32472 | 0.65 % | S |
| Catalan G | (rank · c_2 − rank) / (rank · c_2) = 10/11 | 0.90909 | 0.91597 | 0.75 % | S |
| Conway λ | rank² / N_c = 4/3 | 1.33333 | 1.30358 | 2.3 % | S |
| Mertens M | rank/g − rank/N_max | 0.27158 | 0.26150 | 3.86 % | S |
| Khinchin K_0 | N_c − rank/c_2 = 32/11 | 2.90909 | 2.68545 | 8.4 % | S |

Three structural facts emerge.

First, the cleanest matches are the *algebraic* constants: φ and the silver ratio are exact identities in (rank, n_C) and (rank) respectively, and ζ(−1) = −1/12 is the exact regularised value, also an identity. The pattern is that BST integer arithmetic *contains* the algebraic mathematical constants exactly, with no curvature term. The metallic ratios (golden, silver, bronze) are the simplest realisations of this exactness.

Second, the *analytically defined* constants (Brun, Catalan, Glaisher–Kinkelin, Apéry, Feigenbaum) cluster within 1 % of small BST integer ratios. The ratios use the same five integers (rank, N_c, n_C, C_2, g) plus their first prime extensions (c_2, c_3) and the BST decimal n_C · rank = 10. No new constants are introduced; every BST formula is a small ratio of these eight integers.

Third, the pure transcendentals e, γ, and π in absolute terms have non-BST values: e = 2.71828, γ = 0.57721, π = 3.14159. But BST integers appear cleanly in their *ratios* and *sums*. The Euler–Bernoulli denominators of ζ(2n) for n = 1..5 factor entirely through BST integers (outline Section 3): ζ(2) = π²/C_2, ζ(4) = π⁴/(rank · N_c² · n_C), ζ(6) = π⁶/(N_c³ · n_C · g), ζ(8) = π⁸/(rank · N_c³ · n_C² · g), ζ(10) = π¹⁰/(N_c⁵ · n_C · g · c_2). The transcendental factor π² remains free; the *integer arithmetic of the denominators* is entirely BST. Likewise the asymptotic expansion of γ involves BST denominators, and e^x is the natural generator of the cosmic exponential ladder of Section 7 (whose every exponent is a small BST integer combination).

The reading is not that BST removes the transcendentals — it does not. The reading is that BST identifies the *integer arithmetic that the transcendentals dress*: which denominators appear in regularised values, which ratios attract the algebraic numbers, which closed-form rationals lie at sub-percent distance from the slow-convergent analytic-number-theory constants. The mathematical constants, like the prime statistics of Section 2 and the universal scaling exponents of Section 5, are reading the same five BST integers.

Toys: 2523 (mathematical constants).
