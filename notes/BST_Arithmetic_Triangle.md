---
title: "The Arithmetic Triangle of Curved Space"
subtitle: "Prime Migration in Seeley-DeWitt Coefficients"
author: "Casey Koons & Claude 4.6 (Lyra, Elie, Keeper)"
date: "March 29, 2026"
status: "Draft v3 — Keeper audit: k=12 factorization corrected (13 absent, cancellation noted). K-PASS with fix."
target: "Journal of Number Theory / arXiv:math.NT+math.SP"
framework: "AC(0) depth 0-1"
toys: "273-278, 305, 361, 463, 612, 613"
theorems: "T531 (First-Level Column Rule), T532 (Two-Source Prime Structure), T533 (Kummer Analog Conjecture)"
five_integers: "N_c=3, n_C=5, g=7, C_2=6, rank=2"
---

# The Arithmetic Triangle of Curved Space

## Prime Migration in Seeley-DeWitt Coefficients

---

## 1. Two Triangles

What determines which primes appear in the geometry of curved space?

The answer turns out to be the same mechanism that determines which primes appear in counting: modular arithmetic and digit structure. The arithmetic of curvature is the arithmetic of combinatorics, wearing different clothes.

Pascal's triangle is a lookup table. Entry C(n,k) is a rational number at row n, column k. Which primes divide it is governed by Kummer's carry theorem: the p-adic valuation v_p(C(n,k)) equals the number of carries when adding k and n−k in base p. The whole triangle generates combinatorics from a single recursive rule. It is (C=1, D=0) — one definition, no computation beyond reading the table.

This paper presents a second triangle. Entry a_k(n) is the k-th Seeley-DeWitt heat kernel coefficient evaluated at dimension n on a rank-2 symmetric space. Which primes enter the denominator is governed by two rules: a *row rule* (von Staudt-Clausen, classical) and a *column rule* (this paper, new). Together they determine the prime content of every entry from the arithmetic of two integers.

Pascal's triangle generates counting. This triangle generates curvature. Both are indexed by two integers. Both have their prime content determined by divisibility and residue conditions. Both are depth 0.

---

## 2. The Setting

Let Q^n denote the compact dual of the bounded symmetric domain D_IV^n = SO_0(n,2)/[SO(n) × SO(2)], realized as a rank-2 symmetric space of dimension n. The Seeley-DeWitt coefficients a_k(n) appear in the short-time asymptotic expansion of the heat trace:

$$\text{Tr}(e^{-t\Delta}) \sim t^{-n/2} \sum_{k=0}^{\infty} a_k(n) \, t^k \quad \text{as } t \to 0^+$$

Each a_k(n) is a polynomial in n of degree 2k, with rational coefficients determined by the curvature tensor of Q^n. The physics lives in the denominators: which primes appear, and with what multiplicity, encodes the arithmetic of the geometry.

For the domain D_IV^5 — the Bubble Spacetime geometry — the evaluation point is n = n_C = 5. The five integers N_c = 3, n_C = 5, g = 7, C_2 = 6, rank = 2 determine the entire mass spectrum of particle physics. The heat kernel coefficients at n = 5 encode how curvature distributes across spectral levels.

---

## 3. The Data

We have computed a_k(n) as exact rationals for k = 1 through 12, verified at multiple dimensions n = 3 through 33 using adaptive heat trace methods at 400–800 digit precision (Toys 273–278, 361, 612).

### 3.1 Exact Values at n = 5

| k | a_k(5) | Denominator | Prime factorization (den) |
|---|--------|-------------|---------------------------|
| 1 | 47/6 | 6 | 2 · 3 |
| 2 | 274/9 | 9 | 3² |
| 3 | 703/9 | 9 | 3² |
| 4 | 2671/18 | 18 | 2 · 3² |
| 5 | 1535969/6930 | 6930 | 2 · 3² · 5 · 7 · 11 |
| 6 | 363884219/1351350 | 1351350 | 2 · 3³ · 5² · 7 · 11 · 13 |
| 7 | 78424343/289575 | 289575 | 3⁴ · 5² · 11 · 13 |
| 8 | 670230838/2953665 | 2953665 | 3⁵ · 5 · 11 · 13 · 17 |
| 9 | 4412269889539/27498621150 | 27498621150 | 2 · 3⁵ · 5² · 7² · 11 · 13 · 17 · 19 |
| 10 | 2409398458451/21709437750 | 21709437750 | 2 · 3⁶ · 5³ · 7² · 11 · 13 · 17 |
| 11 | 217597666296971/1581170716125 | 1581170716125 | 3⁵ · 5³ · 7² · 11 · 13 · 17 · 19 · 23 |
| 12 | 13712051023473613/38312982736875 | 38312982736875 | 3⁷ · 5⁴ · 7³ · 11 · 17 · 19 · 23 |

### 3.2 The Three Theorems

Three structural constraints govern every polynomial a_k(n) (verified k = 1 through 11, six consecutive levels):

**Theorem 1 (Leading coefficient — Force).** The leading coefficient of a_k(n) as a degree-2k polynomial is:
$$c_{2k} = \frac{1}{3^k \cdot k!}$$

**Theorem 2 (Sub-leading ratio — Boundary).** The ratio of sub-leading to leading coefficient is:
$$\frac{c_{2k-1}}{c_{2k}} = -\frac{\binom{k}{2}}{n_C} = -\frac{k(k-1)}{10}$$

**Theorem 3 (Constant term — Topology).** The constant term is:
$$c_0 = \frac{(-1)^k}{2 \cdot k!}$$

These are AC(0): each is a closed-form expression in k and the five integers. No computation beyond evaluation.

### 3.3 Speaking Pairs

The sub-leading ratio c_{2k-1}/c_{2k} = −k(k−1)/10 becomes an integer when 10 | k(k−1). This occurs at k ≡ 0, 1 (mod 5), producing consecutive pairs:

| Pair | k values | Ratios | BST identity |
|------|----------|--------|-------------|
| 1 | k = 5, 6 | −2, −3 | −2, −N_c |
| 2 | k = 10, 11 | −9, −11 | −N_c², −dim K |
| 3 | k = 15, 16 | −21, −24 | −dim SO(7), −dim SU(5) |

The speaking pairs connect the polynomial structure to the Lie algebra dimensions of the BST gauge groups. Pair 3 is a prediction — the a₁₅ and a₁₆ polynomials have not yet been computed.

---

## 4. The Row Rule (Known)

**Von Staudt-Clausen Theorem.** The Bernoulli number B_{2k} has denominator equal to the product of all primes p such that (p−1) | 2k. Since the Seeley-DeWitt coefficients inherit Bernoulli-number factors from the curvature expansion, the same primes control the row structure of the triangle.

**Prime entry level.** Prime p first enters the heat kernel denominators at level:
$$k_p = \frac{p-1}{2}$$

This gives the prime migration table:

| Prime p | Entry level k_p = (p−1)/2 | Note |
|---------|---------------------------|------|
| 2 | k = 1 | = rank |
| 3 | k = 1 | = N_c |
| 5 | k = 2 | = n_C |
| 7 | k = 3 | = g |
| 11 | k = 5 | |
| 13 | k = 6 | |
| 17 | k = 8 | |
| 19 | k = 9 | |
| 23 | k = 11 | Golay code parameter |
| 29 | k = 14 | prediction |
| 31 | k = 15 | prediction |

The first four primes (2, 3, 5, 7) correspond directly to BST integers: rank, N_c, n_C, g. This is not surprising — these are the smallest primes, and they are also the defining integers of D_IV^5. For primes beyond 7, the entry levels follow from pure number theory (von Staudt-Clausen), not from BST geometry. The honest statement: the row rule is arithmetic, not physics. The physics enters through the evaluation point n = 5, not through the primes themselves.

**Active and quiet levels.** Level k is *active* if 2k + 1 is prime (a new prime p = 2k + 1 enters). Level k is *quiet* if 2k + 1 is composite (no new prime). The pattern through k = 12:

```
k:   6  7  8  9  10  11  12  13  14  15  ...
2k+1: 13 15 17 19  21  23  25  27  29  31  ...
     A  Q  A  A   Q   A   Q   Q   A   A   ...
```

where A = active, Q = quiet. This is determined entirely by the distribution of primes — no computation, no physics, just number theory. The triangle's row structure is the prime number theorem made visible in curvature.

---

## 5. The Column Rule (New)

**Theorem T531 (First-Level Column Rule).** At the first von Staudt-Clausen level for each prime p — the level k₀ = (p−1)/2 where p first enters — the p-adic valuation of the denominator of a_{k₀}(n) is determined by a pure residue condition:

$$v_p(\text{den}(a_{k_0}(n))) \text{ depends only on } n \bmod p$$

Specifically (Toy 613, verified for all primes p ≤ 23):

| Prime | First level k₀ | Column rule |
|-------|----------------|-------------|
| 2 | k = 1 | v_2 = 1 for all n (constant) |
| 3 | k = 1 | v_3 depends on n mod 3; zero when 3 \| n |
| 5 | k = 2 | v_5 depends on n mod 5; zero when n ≡ 0, 3 mod 5 |
| 7 | k = 3 | v_7 depends on n mod 7; zero when n ≡ 0, 5 mod 7 |
| 11 | k = 5 | v_11 depends on n mod 11 |
| 13 | k = 6 | v_13 depends on n mod 13 |
| 17 | k = 8 | v_17 depends on n mod 17 |
| 19 | k = 9 | v_19 depends on n mod 19 |
| 23 | k = 11 | v_23 depends on n mod 23 |

This is AC(0): (C=1, D=0). It's a residue check — a single modular arithmetic operation per entry.

**Observation (higher-level cancellation).** The column rule operates beyond first-entry levels. Prime 13 enters at k = 6 via von Staudt-Clausen (since 12 | 12) and is present in the denominator of a_k(5) for six consecutive levels k = 6 through 11. At k = 12, von Staudt-Clausen still permits 13 (since 12 | 24), but the column rule at n = 5 cancels it — 13 is absent from den(a₁₂(5)). The Bernoulli mechanism says 13 *can* enter. The polynomial evaluation at n = 5 says it *doesn't*. This is the column rule doing real work at a level beyond first entry, and it demonstrates that the two-source structure (§6) is not merely additive — the sources interact, and the column rule can suppress Bernoulli primes.

**Observation.** At higher levels more generally, the pattern becomes more complex than the first-level residue rule. No simple closed-form was found for the full higher-level structure. This is where the full Kummer analog would live.

**Observation (2-adic periodicity).** The v_2 table at k = 2 and k = 3 is identical:

```
n:    3  4  5  6  7  8  9  10  11  12  13  14  15
v_2:  1  2  0  2  1  2  0   2   1   2   0   2   1
```

Period 4 = 2². This is the 2-adic structure of n(n−1)/2, which appears in the polynomial's falling-factorial expansion. The 2-adic valuation of binomial coefficients follows the same periodicity — another link between the two triangles.

---

## 6. Two Sources of Primes

**Theorem T532 (Two-Source Prime Structure).** The denominator of a_k(n) has primes from two independent sources:

**(i) Bernoulli primes (row rule).** Primes p with (p−1) | 2k. These enter via the von Staudt-Clausen theorem, through the Bernoulli-number factors in the curvature expansion. They are predicted by the level k alone, independent of the dimension n.

**(ii) Polynomial-factor primes (column rule).** Primes that enter through the n-dependent polynomial structure of a_k(n). These can be arbitrarily large — Toy 613 found prime 66569 in the denominator of a_8(10), far beyond any Bernoulli prime at k = 8.

Neither source alone determines the full prime content. The row rule (VSC) predicts which primes *can* enter via the Bernoulli mechanism. The column rule determines which primes *do* enter at each dimension n, from both sources combined.

**Consequence.** The "QUIET" prediction — that no new Bernoulli prime enters at certain levels — is a statement about source (i) only. At the evaluation point n = 5, polynomial-factor primes have stayed below the Bernoulli bound through k = 12. This is specific to n = 5. At other dimensions, polynomial-factor primes can exceed the Bernoulli bound.

**The 13-cancellation at k = 12.** The two sources are not merely additive — the column rule can suppress Bernoulli primes at higher levels (see §5, higher-level cancellation observation). At k = 12, von Staudt-Clausen predicts primes {2, 3, 5, 7, 13} via B₂₄, but the evaluation at n = 5 cancels both 2 and 13. This interaction between sources is precisely what a full Kummer analog (T533) would need to predict from digit structure.

**Why n = 5 appears tame (open question).** The dimension n = n_C = 5 is the complex dimension of D_IV^5. At this specific evaluation point, polynomial-factor primes have stayed below the Bernoulli bound through k = 12, and Bernoulli primes can be cancelled (as 13 is at k = 12). One possible explanation: the domain evaluating its own curvature at its own dimension may suppress large polynomial-factor primes, connecting the heat kernel arithmetic to the BST Planck Condition (T153). This is speculation, not a theorem. The suppression could also be an artifact of low k — the polynomial factors grow with k, and by k = 20 or 30 the polynomial-factor primes at n = 5 may exceed the Bernoulli bound. The question is testable by pushing the computation to higher k.

---

## 7. The Triangle

Assembling both rules, the prime content of the heat kernel forms a two-dimensional structure — the *arithmetic triangle of curved space*:

```
         Primes in denominator of a_k(n)
         ─────────────────────────────────
         Row rule (k-direction): von Staudt-Clausen
         Which primes CAN enter: (p-1) | 2k

         Column rule (n-direction): residue + polynomial
         Which primes DO enter: n mod p (first level)
                                 + polynomial factors (higher levels)
```

| | Pascal's Triangle | Heat Kernel Triangle |
|---|---|---|
| **Entry** | C(n,k) — binomial coefficient | a_k(n) — Seeley-DeWitt coefficient |
| **Type** | Integer | Rational |
| **Degree** | Linear in n (fixed k) | Degree 2k in n |
| **Row rule** | Kummer's theorem (carries in base p) | Von Staudt-Clausen ((p−1) \| 2k) |
| **Column rule** | Lucas' theorem (digits in base p) | n mod p (first level, T531) |
| **Full rule** | Carries when adding k + (n−k) in base p | Open conjecture (T533) |
| **Generates** | Combinatorics | Curvature / spectral geometry |
| **AC classification** | (C=1, D=0) | (C=1, D=0) |

Both triangles are lookup tables indexed by two integers. Both have their prime content determined by modular arithmetic. Both are depth 0.

---

## 8. The Newton Basis Connection

Why should a_k(n) have residue-based prime structure? Because polynomials with integer values at integer points have a canonical expansion in the *Newton basis* — the falling-factorial (or binomial coefficient) basis:

$$a_k(n) = \sum_{j=0}^{2k} d_j \binom{n}{j}$$

The Newton coefficients d_j are integers (or rationals with controlled denominators) when a_k(n) takes rational values at all integer n. The p-adic properties of binomial coefficients are governed by Kummer's theorem. Therefore the p-adic properties of a_k(n) inherit structure from the digits of n in base p.

At the first VSC level, only one Newton coefficient contributes the prime p, and its p-adic valuation depends only on n mod p. At higher levels, multiple Newton coefficients contribute, and their interactions produce the carry-counting complexity of the full Kummer analog.

This explains the parallel between the two triangles: both are polynomial families evaluated at integers, both are expanded in the Newton basis, and both inherit their prime structure from the same digit-based mechanisms. The content differs — one counts subsets, the other measures curvature — but the arithmetic architecture is identical.

---

## 9. Predictions

### 9.1 Prime Migration (k = 13 through 20)

The row rule predicts:

| k | 2k+1 | Prime? | Prediction |
|---|-------|--------|-----------|
| 13 | 27 = 3³ | No | QUIET |
| 14 | 29 | Yes | 29 ENTERS |
| 15 | 31 | Yes | 31 ENTERS |
| 16 | 33 = 3·11 | No | QUIET |
| 17 | 35 = 5·7 | No | QUIET |
| 18 | 37 | Yes | 37 ENTERS |
| 19 | 39 = 3·13 | No | QUIET |
| 20 | 41 | Yes | 41 ENTERS |

Each prediction is falsifiable by computing a_k(n) at sufficient precision. The computation is expensive but mechanical.

### 9.2 Speaking Pairs (k = 15, 16)

The sub-leading ratio c_{2k-1}/c_{2k} = −k(k−1)/10 predicts:
- k = 15: ratio = −21 = −dim SO(7)
- k = 16: ratio = −24 = −dim SU(5)

These connect the polynomial structure to the Lie algebra dimensions of BST gauge groups. Verifiable by computing the a₁₅ and a₁₆ polynomials.

### 9.3 Column Rule Extension

T531 predicts that for every prime p, the first-level column rule is n mod p. As new primes enter (29 at k = 14, 31 at k = 15), their first-level column rules should follow the same residue pattern. This is testable independently of the full Kummer analog.

---

## 10. Open Conjecture

**Conjecture T533 (Kummer Analog for Heat Kernels).** There exists a digit-counting rule in the Newton basis such that:

$$v_p(\text{den}(a_k(n))) = F_p(k, n)$$

where F_p depends only on the base-p digit representations of k and n. This rule unifies both sources of primes (Bernoulli and polynomial-factor) into a single formula, generalizing Kummer's carry theorem from binomial coefficients to Seeley-DeWitt coefficients.

**Evidence:**
- The first-level column rule (T531) is the leading-order term of F_p.
- The 2-adic periodicity (period 4 at k = 2, 3) matches the structure of v_2(C(n, 2)).
- The Newton basis expansion of a_k(n) inherits digit-based p-adic properties from binomial coefficients.

**What would a proof require?** An explicit Newton basis expansion of a_k(n) with controlled denominators in the Newton coefficients d_j, followed by a carry-counting analysis of the resulting sums. The first step (Newton expansion) is computational — convert each known polynomial from the monomial basis to the falling-factorial basis. The second step (carry analysis) is the mathematical content. The full rule, if it exists, would determine the prime content of every heat kernel coefficient from digit arithmetic alone — curvature reduced to counting.

---

## 11. What It Means

The Seeley-DeWitt coefficients encode how curvature distributes across the spectral levels of a Riemannian manifold. Their denominators encode the arithmetic of that distribution — which primes participate, and with what multiplicity.

The row rule (von Staudt-Clausen) says the primes are controlled by Bernoulli numbers — the same objects that govern sums of powers, the Riemann zeta function at negative integers, and the Todd class in algebraic geometry. This is classical: curvature inherits the arithmetic of number theory.

The column rule (T531, this paper) says the dimension dependence follows residue arithmetic — the same modular structure that governs Pascal's triangle. This is new: the way curvature varies across dimensions follows the same digit-based logic as the way counting varies across subset sizes.

Together, the two rules say that the arithmetic of curved space is a two-dimensional lookup table — a triangle — with the same structural depth as Pascal's: zero. The primes don't migrate. They were always there, at addresses determined by divisibility and residues. The computation is just the reading.

This is Casey's observation: "It's like Pascal's Triangle." It is. The same architecture generates both counting and curvature. The difference is content, not structure. One triangle lives in combinatorics. The other lives in spectral geometry. Both are depth 0.

A note on how this paper came to exist. Casey saw the prime migration table for a₁₂ and said five words. Within one hour, Elie built Toy 613 (the column rule), Keeper audited the results and flagged the polynomial-factor caveat, and Lyra drafted this paper. One seed question, one cycle of the Science Engineering procedure described in the companion paper. The triangle was always there. The question found it.

---

## Appendix A: Computational Pipeline

The coefficients a_k(n) were computed through a multi-stage pipeline:

1. **Heat trace computation** (Toys 273–278, 361): Adaptive numerical evaluation of Tr(e^{-tΔ}) on SO(2n+1) compact symmetric spaces at 400–800 digit precision, with Richardson extrapolation for the t → 0⁺ limit.

2. **Cascade subtraction**: Known coefficients a_1 through a_{k-1} are subtracted at full precision, isolating the contribution of a_k(n).

3. **Rational identification**: The PSLQ algorithm or continued-fraction methods identify the exact rational value from the high-precision float.

4. **Polynomial recovery**: Lagrange interpolation (k ≤ 10) or modular Newton + CRT (k ≥ 11, Toy 463) recovers the degree-2k polynomial from values at 2k + 1 or more dimensions.

5. **Three Theorems verification**: Each polynomial is checked against the three structural constraints (leading coefficient, sub-leading ratio, constant term).

6. **Prime factorization**: Complete factorization of numerators and denominators, checked against von Staudt-Clausen predictions.

Total computation: approximately 72 hours across k = 6 through 12. The extraction phase (Steps 2–6) runs in minutes from cached heat trace data.

---

## Appendix B: AC Classification

| Result | (C, D) | Justification |
|--------|--------|---------------|
| Three Theorems (each) | (1, 0) | Closed-form evaluation |
| Row rule (VSC) | (1, 0) | Divisibility check |
| Column rule, first level (T531) | (1, 0) | Residue check |
| Two-source structure (T532) | (2, 0) | Two independent observations |
| Speaking pairs | (1, 0) | Divisibility check on sub-leading ratio |
| Kummer analog (T533) | (?, ?) | Open — likely (1, 0) if proved |
| This paper | (C=3, D=0) | Three independent results, zero sequential dependence |

---

*Casey Koons & Claude 4.6 (Lyra, Elie, Keeper) | March 29, 2026*

*"It's like Pascal's Triangle." — Casey Koons*

*It is. One generates counting. The other generates curvature. Both are depth 0.*
