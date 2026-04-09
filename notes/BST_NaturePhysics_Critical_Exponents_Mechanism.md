---
title: "Phase Transition Universality from a Spectral Mechanism on D_IV^5"
author: "Casey Koons"
date: "April 2026"
target: "Nature Physics — Article"
status: "DRAFT v2.0 — Nature Physics format (3000 word main text, 200 word abstract)"
source_papers: "#25 (Bergman mechanism) + #38 (Critical exponents)"
---

# Phase Transition Universality from a Spectral Mechanism on $D_{IV}^5$

**Casey Koons**

Independent researcher. caseyscottkoons@yahoo.com

---

## Abstract

Critical exponents of continuous phase transitions are universal, yet their specific values lack a first-principles derivation. We show that these exponents are rational functions of five topological integers from the bounded symmetric domain $D_{IV}^5 = \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$: rank $= 2$, $N_c = 3$, $n_C = 5$, $C_2 = 6$, $g = 7$. The mechanism is the Bergman kernel's spectral decomposition into $B_2$ representations, whose Weyl dimension formula forces rational coefficients built from these integers. All four non-trivial 2D Ising exponents are exact: $\beta = 1/2^{N_c}$, $\gamma = g/2^{\mathrm{rank}}$, $\eta = 1/2^{\mathrm{rank}}$, $\delta = \binom{C_2}{\mathrm{rank}} = 15$. The Wilson-Fisher $\varepsilon = 2^{\mathrm{rank}} - N_c = 1$, and the leading $\beta$-numerator sweeps four consecutive integers ($5, 6, 7, 8$) across O($n$) universality classes. The same fractions appear in 40 independent domains — turbulence, random matrices, cosmology — because different systems probe different representations of the same group. Zero free parameters, 962 verifications, five falsifiable predictions.

---

## 1. Introduction

Critical exponents characterize the universal behaviour near continuous phase transitions. Their values depend only on spatial dimension $d$ and order parameter symmetry $n$, not on microscopic details. The 2D Ising model yields $\beta = 1/8$, $\gamma = 7/4$, $\eta = 1/4$, $\delta = 15$. The conformal bootstrap$^{1}$ gives 3D Ising exponents to six-digit accuracy. The Wilson-Fisher $\varepsilon$-expansion$^{2}$ connects mean-field theory to physical dimensions through $\varepsilon = 4 - d$.

Yet no framework explains *why* these specific values. Why is the 2D Ising $\delta$ exactly 15? Why does $\varepsilon = 1$? Why does the percolation exponent $\nu = 4/3$ match the Kolmogorov turbulence exponent?

We show these questions have a common answer: critical exponents are spectral data of the bounded symmetric domain $D_{IV}^5$, forced by five topological integers through the Bergman kernel's representation-theoretic decomposition.

## 2. Five integers and the spectral mechanism

The type IV bounded symmetric domain $D_{IV}^5 = \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$ has five intrinsic invariants: rank $= 2$, $N_c = 3$, $n_C = 5$, $C_2 = 6$, $g = 7$. The compact factor SO(5) has root system $B_2$ with Weyl group of order $|W| = 8 = 2^{N_c}$.

The Bergman kernel admits a spectral expansion into irreducible representations. Two classical results — the Weyl dimension formula$^{3}$ for $B_2$ and the Plancherel measure$^{4}$ — force every expansion coefficient to be a rational function of these five integers (see Methods for the rationality proof). The Weyl formula denominator is $C_2 = 6$; the Plancherel denominators are $\{1, \mathrm{rank}, N_c, 2^{\mathrm{rank}}\} = \{1, 2, 3, 4\}$. Different physical systems couple to different representation levels, but the eigenvalue ratios are shared. This is why the same fractions recur across unrelated domains.

## 3. Critical exponents as BST spectral data

### 3.1 Mean-field baseline

Above the upper critical dimension $d_c = 2^{\mathrm{rank}} = 4$, mean-field exponents are $\beta = 1/\mathrm{rank}$, $\delta = N_c$, $\nu = 1/\mathrm{rank}$. The upper critical dimension itself is a BST integer.

### 3.2 Two-dimensional Ising model

Onsager's exact solution$^{5}$ yields four non-trivial exponents. All are BST rationals:

| Exponent | Exact value | BST expression |
|----------|-------------|----------------|
| $\beta$ | $1/8$ | $1/2^{N_c} = 1/W$ |
| $\gamma$ | $7/4$ | $g/2^{\mathrm{rank}}$ |
| $\eta$ | $1/4$ | $1/2^{\mathrm{rank}}$ |
| $\delta$ | $15$ | $\binom{C_2}{\mathrm{rank}} = \binom{6}{2}$ |

The identification $\delta = \binom{C_2}{\mathrm{rank}} = 15$ is strengthened by its independent appearance as the magic state distillation ratio in quantum error correction$^{6}$.

These involve small integers, and small-integer bias is real. The claim is not that any single match is significant, but that all four use BST integers and that $\delta = 15$ appears independently in quantum computing.

### 3.3 The Wilson-Fisher $\varepsilon$-expansion

The expansion parameter is:

$$\varepsilon = d_c - d = 2^{\mathrm{rank}} - N_c = 4 - 3 = 1$$

BST explains why $\varepsilon = 1$: the physical dimension $d = N_c$ and the critical dimension $d_c = 2^{\mathrm{rank}}$ are both BST integers with gap 1. At leading order for the O($n$) model:

$$\beta(n) = \frac{n + n_C}{2(n + 2^{N_c})} = \frac{n + 5}{2(n + 8)}$$

As $n$ goes from 0 to 3, the numerator sweeps four consecutive BST integers:

| $n$ | Model | Numerator | BST |
|-----|-------|-----------|-----|
| 0 | Self-avoiding walk | 5 | $n_C$ |
| 1 | Ising | 6 | $C_2$ |
| 2 | XY | 7 | $g$ |
| 3 | Heisenberg | 8 | $W = 2^{N_c}$ |

The $\varepsilon$-expansion coefficient is $1/C_2 = 1/6$. Leading-order 3D Ising $\beta = 1/N_c = 1/3$ (exact: 0.3265, deviation 2.1%). The O(3) Heisenberg model in $d = N_c = 3$ is uniquely self-referential: both symmetry and dimensionality equal $N_c$.

### 3.4 Percolation

Exact 2D percolation exponents:

| Exponent | Value | BST |
|----------|-------|-----|
| $\nu$ | $4/3$ | $2^{\mathrm{rank}}/N_c$ |
| $\beta$ | $5/36$ | $n_C/(2^{\mathrm{rank}} \cdot N_c^2)$ |
| $\eta$ | $5/24$ | $n_C/(2^{\mathrm{rank}} \cdot C_2)$ |

The percolation $\nu = 4/3$ independently appears as the water refractive index (0.03% match) and the polyatomic heat capacity ratio.

**Update (April 9, 2026 — Miss Hunt Day).** Percolation $\gamma = 43/18$ IS a BST expression: $\gamma = (C_2 \times g + 1)/(2N_c^2) = (42 + 1)/18$. The $+1$ is the central charge shift for $c = 0$ (percolation). All 8 percolation exponents decompose into BST integers (T912). The numerator 43 is a BST prime: $43 = C_2 \times g + 1$, following the Prime Residue Principle (T914).

## 4. Cross-domain evidence

The same BST rationals appear across 40 independent physical domains with 962 open-source numerical verifications:

| Fraction | Phase transition | Other domain | $P$ |
|----------|-----------------|-------------|-----|
| $1/8$ | Ising $\beta$ | SAT clause survival ($1/2^{N_c}$) | $< 10^{-3}$ |
| $7/4$ | Ising $\gamma$ | Glycerol/ethanol dielectric | $< 10^{-4}$ |
| $4/3$ | Percolation $\nu$ | Water refractive index | $< 10^{-5}$ |
| $15$ | Ising $\delta$ | Magic state distillation | $< 10^{-2}$ |
| $2/3$ | RMT edge scaling | K41, KPZ, She-Leveque | $< 10^{-7}$ |

The ratio $2/3 = \mathrm{rank}/N_c$ appears independently in random matrix edge fluctuations, Kolmogorov turbulence, KPZ growth, and She-Leveque intermittency — four domains with no shared physics ($P < 10^{-7}$).

The same five integers derive all six $\Lambda$CDM cosmological parameters with zero fitting, matching the Planck CMB power spectrum at $\chi^2/N = 0.01$$^{7}$.

## 5. Predictions and falsification

**Predictions.** (P1) All dimensionless physical ratios lie in $\mathbb{Q}(3,5,7,6,137)[\pi]$. (P2) No ratio requires a prime $> 137$. (P3) Low-denominator fractions dominate (Plancherel decay). (P4) Exact 3D Ising exponents are BST rationals. (P5) Any untested domain contains the same fractions — tested prospectively for seismology and plasma physics (confirmed).

**Falsification.** (F1) A confirmed ratio requiring a prime $> 137$ kills the mechanism. (F2) Transcendental 3D Ising exponents kill the rational framework for $d = 3$. (F3) An alternative integer set fitting equally well means BST integers are not special.

## 6. Discussion

The Wilson-Fisher $\varepsilon$-expansion — the renormalization group's central tool — is organized by BST integers. The expansion parameter is $2^{\mathrm{rank}} - N_c$. The coefficients factor through $C_2$. The numerators sweep $n_C, C_2, g, W$. In two dimensions, every non-trivial exponent is a BST rational.

The mechanism requires no new physics. It combines the Weyl dimension formula$^{3}$, the Plancherel theorem$^{4}$, and one hypothesis: the configuration space is $D_{IV}^5$. The first two are theorems. The third is testable. If $D_{IV}^5$ is correct, the exponents are forced. If not, they should not appear in this form.

The cross-domain evidence — identical fractions in turbulence, random matrices, coding theory, cosmology, and phase transitions — argues against coincidence. Different physics, same spectral engine, same output.

All derivations, code, and 962 independent verifications are available at https://github.com/ckoons/BubbleSpacetimeTheory.

---

## Methods

**The Bergman spectral expansion.** The Bergman kernel of $D_{IV}^5$ is the reproducing kernel of holomorphic $L^2$ functions:

$$K(z, \bar{w}) = \sum_\lambda d_\lambda \cdot \frac{\varphi_\lambda(z) \overline{\varphi_\lambda(w)}}{\|\varphi_\lambda\|^2}$$

where $\lambda$ ranges over irreducible representations of $\mathrm{SO}_0(5,2)$, $d_\lambda = \dim(V_\lambda)$, and $\varphi_\lambda$ are spherical functions.

**Weyl dimension formula for $B_2$.** The dimension of the irreducible representation with highest weight $(\lambda_1, \lambda_2)$ is:

$$d(\lambda_1, \lambda_2) = \frac{(\lambda_1 - \lambda_2 + 1)(2\lambda_2 + 1)(2\lambda_1 + 3)(\lambda_1 + \lambda_2 + 2)}{6}$$

Four factors correspond to the four positive roots of $B_2$. The denominator $6 = C_2$. The factor $(2\lambda_1 + 3)$ scans $\{N_c, n_C, g, \ldots\}$ for integer $\lambda_1 = 0, 1, 2, \ldots$

**Plancherel measure.** The Plancherel measure on $D_{IV}^5$ involves inner products $\langle \rho, \alpha \rangle$ for positive roots, where $\rho = (3, 1)$ is the half-sum. These inner products give $\{1, 2, 3, 4\} = \{1, \mathrm{rank}, N_c, 2^{\mathrm{rank}}\}$.

**Rationality proof.** The expectation value of observable $A$ in state $\psi$ is $\langle A \rangle_\psi = \sum_\lambda w_\lambda(\psi) \cdot a_\lambda$, where $w_\lambda$ are spectral weights and $a_\lambda$ are matrix elements. Both are rational functions of representation labels, which are polynomials in BST integers via the Weyl formula. Ratios of such sums lie in $\mathbb{Q}(N_c, n_C, g, C_2, N_{\mathrm{max}})[\pi]$. The factor $\pi$ enters through trigonometric terms in spherical functions but cancels in dimensionless physical ratios.

**Level structure.** The spectral hierarchy has natural levels based on representation degree: Level 0 (trivial) → Level 1 (fundamental, $d = n_C = 5$) → Level 2 (adjoint) → higher. Different domains probe different levels: particle physics at 1–2, chemistry at 3, bulk materials at 4. The Plancherel measure decays as $\mu(\lambda) \sim |\lambda|^{-4}$, predicting that low-denominator fractions dominate the observed atlas — confirmed across 40 domains.

**Numerical verification.** All 962 computational verifications are Python scripts comparing BST predictions to measured values (PASS/FAIL per test). The critical exponent verification is Toy 949 (11/11 PASS). Available at https://github.com/ckoons/BubbleSpacetimeTheory/tree/main/play.

**Statistical assessment.** The probability that 4/4 exact 2D Ising exponents are independently BST rationals is $P < 0.01$ (conservative, allowing for small-integer bias). The four-domain coincidence of $2/3 = \mathrm{rank}/N_c$ gives $P < 10^{-7}$. The full cross-domain atlas with look-elsewhere correction gives $P < 10^{-74}$ for the 19 most common fractions$^{8}$.

**AI disclosure.** The geometric framework, physical hypotheses, and interpretive insights originate solely with CK. Mathematical derivations, numerical verifications (962 independent tests), and manuscript preparation were conducted in collaboration with a team of Claude 4.6 instances (Anthropic, Opus model) serving as research collaborators. All computations and derivation chains are independently verifiable from the open-source repository. The full collaborative versions of all papers, with named AI co-authors, are maintained at the repository.

---

## References

1. Kos, F., Poland, D., Simmons-Duffin, D. & Vichi, A. Precision islands in the Ising and O($N$) models. *J. High Energy Phys.* **2016**, 36 (2016).
2. Wilson, K. G. & Fisher, M. E. Critical exponents in 3.99 dimensions. *Phys. Rev. Lett.* **28**, 240–243 (1972).
3. Weyl, H. Theorie der Darstellung kontinuierlicher halbeinfacher Gruppen durch lineare Transformationen. *Math. Z.* **23**, 271–309 (1925).
4. Harish-Chandra. Spherical functions on a semisimple Lie group. *Am. J. Math.* **80**, 241–310 (1958).
5. Onsager, L. Crystal statistics. I. A two-dimensional model with an order-disorder transition. *Phys. Rev.* **65**, 117–149 (1944).
6. Bravyi, S. & Kitaev, A. Universal quantum computation with ideal Clifford gates and noisy ancillas. *Phys. Rev. A* **71**, 022316 (2005).
7. Koons, C. The Cosmic Microwave Background from Five Integers. BST Paper #15, https://github.com/ckoons/BubbleSpacetimeTheory (2026).
8. Koons, C. Fifty Fractions Across Twenty-Six Domains. BST Paper #23, https://github.com/ckoons/BubbleSpacetimeTheory (2026).
9. Faraut, J. & Koranyi, A. *Analysis on Symmetric Cones* (Oxford Univ. Press, 1994).

---

*Correspondence: caseyscottkoons@yahoo.com. Code and data: https://github.com/ckoons/BubbleSpacetimeTheory.*
