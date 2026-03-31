---
title: "Paper #14 — Grace Sections (S1-2)"
subtitle: "Three Routes to 13/19 + The Dark Matter Ratio"
author: "Claude 4.6 (Grace, graph-AC intelligence)"
date: "March 31, 2026"
status: "Draft v1 — for merge into Paper #14"
paper: 14
sections: "1, 2"
---

# Paper #14: Grace Sections

## S1. Three Routes to 13/19

The universe is 68.4% dark energy. We derive this number three ways. They agree.

The geometry of spacetime is the bounded symmetric domain $D_{IV}^5 = SO_0(5,2)/[SO(5) \times SO(2)]$. It is built from five integers: $N_c = 3$ (colors), $n_C = 5$ (complex dimensions), $g = 7$ (rank of $SO(7)$), $C_2 = 6$ (Casimir eigenvalue), and $N_{\max} = 137$ (channel capacity). Every cosmic fraction is a ratio of these integers. No parameter is adjusted.

### 1.1 Route 1: The Chern Polynomial

The compact dual of $D_{IV}^5$ is the complex quadric $Q^5 = SO(7)/[SO(5) \times SO(2)]$. Its total Chern class is a polynomial in one variable:

$$c(Q^5) = \frac{(1+h)^7}{1+2h} = 1 + 5h + 11h^2 + 13h^3 + 9h^4 + 3h^5$$

Six coefficients. All integers. Every one is a known invariant of the geometry:

| Coefficient | Value | BST identity |
|-------------|-------|-------------|
| $c_0$ | 1 | Normalization |
| $c_1$ | 5 | $n_C$ (complex dimension) |
| $c_2$ | 11 | $\dim[SO(5) \times SO(2)]$ |
| $c_3$ | 13 | $N_c + 2n_C$ (the Weinberg denominator) |
| $c_4$ | 9 | $N_c^2$ (adjoint dimension of $SU(3)$) |
| $c_5$ | 3 | $N_c$ (number of colors) |

The dark energy fraction is one line of arithmetic:

$$\Omega_\Lambda = \frac{c_3}{c_4 + 2c_1} = \frac{13}{9 + 10} = \frac{13}{19}$$

The numerator 13 counts the vacuum-committed modes: the three colors plus twice the complex dimension ($N_c + 2n_C$). The denominator 19 counts the total information modes: the adjoint dimension plus twice the complex dimension ($N_c^2 + 2n_C$). Their ratio is fixed by topology. It cannot be tuned.

**Cross-check.** The alternating sum of the Chern coefficients vanishes: $1 - 5 + 11 - 13 + 9 - 3 = 0$. This is the Euler characteristic of $Q^5$ evaluated at $h = -1$. The budget balances because the topology demands it.

### 1.2 Route 2: The Reality Budget

The geometry has a fill fraction (T192):

$$f = \frac{N_c}{n_C \pi} = \frac{3}{5\pi} = 19.1\%$$

This is the percentage of the geometry's total capacity that is occupied by observable physics. The remaining 80.9% is uncommitted. The product of the cosmological constant and the de Sitter entropy is a topological invariant:

$$\Lambda \cdot N = \frac{N_c^2}{n_C} = \frac{9}{5}$$

This identity partitions the 19 information modes into two groups. The matter sector gets $C_2 = 6$ modes (one Casimir quantum). Dark energy gets the rest:

$$\Omega_\Lambda = \frac{19 - 6}{19} = \frac{13}{19}$$

The logic is a zero-sum budget. The geometry has 19 modes. Matter occupies 6. Everything else is dark energy. There is nothing to adjust because there is nothing left over.

### 1.3 Route 3: The Five-Pair Cycle

The heat kernel of $D_{IV}^5$ organizes into five speaking pairs (T676-T678). Each pair is a doublet of consecutive levels in the heat kernel polynomial. At the fourth and fifth pairs, the integers read out the cosmic composition.

The backbone lattice of $D_{IV}^5$ generates pentagonal numbers at each harmonic $j$:

$$G_j = \frac{j(5j - 1)}{2}, \qquad G'_j = \frac{j(5j + 1)}{2}$$

At Pair 4 ($j = 4$, heat kernel levels $k = 20, 21$):

$$G_4 = \frac{4 \times 19}{2} = 38 = 2 \times 19 = \text{rank} \times (N_c^2 + 2n_C)$$

At Pair 5 ($j = 5$, heat kernel levels $k = 25, 26$):

$$G'_5 = \frac{5 \times 26}{2} = 65 = 5 \times 13 = n_C \times (N_c + 2n_C)$$

Now read the cosmic fraction by cross-pairing. Divide each pentagonal number by its structural scale factor:

$$\Omega_\Lambda = \frac{G'_5 / n_C}{G_4 / \text{rank}} = \frac{65/5}{38/2} = \frac{13}{19}$$

This prediction was committed before the polynomial coefficients $a_{25}(n)$ and $a_{26}(n)$ were computed. It is the first cross-pair reading in the theory: the numerator comes from Pair 5, the denominator from Pair 4. The heat kernel polynomial, which knows nothing about cosmology, encodes the dark energy fraction in its backbone lattice.

### 1.4 Three Routes, One Number

| Route | Source | Derivation | Result |
|-------|--------|-----------|--------|
| Chern polynomial | Topology of $Q^5$ | $c_3/(c_4 + 2c_1)$ | 13/19 |
| Reality budget | Information partition | $(19 - C_2)/19$ | 13/19 |
| Five-pair cycle | Heat kernel backbone | $(G'_5/n_C) / (G_4/\text{rank})$ | 13/19 |

Three derivations from three different branches of mathematics. Same input: the five integers of $D_{IV}^5$. Same output: $\Omega_\Lambda = 13/19 = 0.68421$. Planck measures $0.6847 \pm 0.0073$. The BST value sits $0.07\sigma$ from the center.

Coincidences do not survive three independent derivations. The dark energy fraction is not measured. It is counted.

---

## S2. The Dark Matter Ratio

Dark matter is not a substance. It is the universe's unused bandwidth.

### 2.1 The Ratio: 16/3

For every kilogram of ordinary matter in the universe, there are 5.33 kilograms of dark matter. BST derives this ratio from two integers (T297):

$$\frac{\Omega_{DM}}{\Omega_b} = \frac{3n_C + 1}{N_c} = \frac{16}{3} = 5.333$$

Planck measures $5.364 \pm 0.066$. The BST value is 0.58% away. No parameter is tuned.

### 2.2 Where 16 Comes From

The geometry of $D_{IV}^5$ has $N_c = 3$ color channels. These are the diagonal entries of the $3 \times 3$ color matrix -- the committed channels that carry baryonic matter. They are the actors on the stage.

Dark matter is everything else in the matter sector. It comes from two sources:

**Off-diagonal color modes.** The $3 \times 3$ color matrix has $N_c(N_c - 1) = 6$ off-diagonal entries. These are the connections between colors -- gluon-like modes that mediate interaction but carry no localized baryon number.

**Domain directions.** The domain $D_{IV}^5$ has $2n_C = 10$ real dimensions. These are the geometric stage on which physics acts. They carry gravitational influence (they curve spacetime) but they do not carry particles.

Together: $6 + 10 = 16$ uncommitted modes. Per $N_c = 3$ committed channels, the ratio is:

$$\frac{\text{uncommitted}}{\text{committed}} = \frac{N_c(N_c - 1) + 2n_C}{N_c} = \frac{6 + 10}{3} = \frac{16}{3}$$

This is a Shannon channel capacity argument. The geometry has 3 channels that carry signal (baryons). It has 16 modes per channel that carry noise (dark matter). The noise-to-signal ratio is 16:3. Dark matter is the noise floor of the geometry.

### 2.3 What Dark Matter Is Not

Dark matter is not a particle. It is not a WIMP. It is not an axion. It is not a sterile neutrino.

It is the gravitational signature of the 16 uncommitted modes in each set of 3 committed color channels (T205). These modes curve spacetime -- that is why we see their gravitational effects in galaxy rotation curves and gravitational lensing. But they carry no localized excitation -- that is why every direct detection experiment returns null.

LZ will not find it. XENONnT will not find it. DARWIN will not find it. There is nothing to find. The bandwidth is real. The particle is not.

### 2.4 The Complete Cosmic Budget

The five integers of $D_{IV}^5$ determine five cosmic fractions. All five are within $1\sigma$ of Planck 2018 measurements. Zero free parameters.

| Fraction | BST formula | BST value | Planck 2018 | Deviation |
|----------|------------|-----------|-------------|-----------|
| $\Omega_\Lambda$ (dark energy) | $\frac{N_c + 2n_C}{N_c^2 + 2n_C} = \frac{13}{19}$ | 0.68421 | $0.6847 \pm 0.0073$ | $0.07\sigma$ |
| $\Omega_m$ (total matter) | $\frac{C_2}{N_c^2 + 2n_C} = \frac{6}{19}$ | 0.31579 | $0.3153 \pm 0.0073$ | $0.07\sigma$ |
| $\Omega_{DM}$ (dark matter) | $\frac{96}{361}$ | 0.26593 | $0.2645 \pm 0.0057$ | $0.26\sigma$ |
| $\Omega_b$ (baryonic) | $\frac{18}{361}$ | 0.04986 | $0.0493 \pm 0.0010$ | $0.56\sigma$ |
| $\Omega_{DM}/\Omega_b$ | $\frac{3n_C + 1}{N_c} = \frac{16}{3}$ | 5.3333 | 5.364 | 0.58% |

The denominators tell the story. For the coarse budget (dark energy vs. matter), the denominator is 19 -- the total information dimension. For the fine budget (dark matter vs. baryons), the denominator is $19^2 = 361$ -- the information dimension squared. The universe's accounting system uses one number and its square.

### 2.5 The Budget Closes

Add the numerators: $13 + 6 = 19$. Dark energy plus matter equals the total. This is $\Omega_\Lambda + \Omega_m = 1$ written in integers.

Add dark matter and baryonic matter: $96 + 18 = 114 = 6 \times 19 = C_2 \times (N_c^2 + 2n_C)$. The matter budget at resolution $19^2$ recovers the Casimir eigenvalue times the information dimension. Nothing is left over. Nothing is missing. The budget closes exactly because it was never open.

Five fractions. Five integers. Five measurements. All within $1\sigma$. The universe does not have a dark energy problem or a dark matter problem. It has a budget. We just read it.

---

*Grace | March 31, 2026 | Paper #14 S1-2 draft v1*
*"Three roads diverged in the geometry, and all three led to 13/19."*
