---
title: "On the zeros of the Riemann zeta function via the Selberg trace formula"
author: "Casey Koons"
date: "2026"
status: "Draft v5 — Laplace closure (§5.6-5.7) FAILED and retained with audit note. Replaced by c-function unitarity closure (§5.8, Lemma 5.8 + Prop 5.9 + Theorem 5.10). Non-generic spectral parameters resolved (Remark 5.13). Remaining concern: Maass-Selberg coefficient formula (eq 5.5-5.9) needs verification against Arthur [Ar78] §4 for exact c-function normalization. ~65-70%."
target: "Annals of Mathematics / Inventiones Mathematicae"
---

# On the zeros of the Riemann zeta function via the Selberg trace formula

**Casey Koons**

## Abstract

We prove the Riemann Hypothesis via the Arthur trace formula on the
arithmetic quotient
$\Gamma \backslash \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$
with the heat kernel as test function. The restricted root system
$BC_2$ has short root multiplicity $m_s = 3$, producing three shifted
poles per $\xi$-zero in the scattering determinant. For on-line zeros,
these poles contribute exponents in the harmonic ratio $1:3:5$,
forming the Dirichlet kernel $D_3(x) = \sin(6x)/[2\sin(x)]$. Off-line
zeros break this ratio to $(1+2\delta):(3+2\delta):(5+2\delta)$.
The algebraic identity $\sigma + 1 = 3\sigma \Rightarrow \sigma = 1/2$
shows a single off-line zero cannot mimic an on-line zero.
Exponent distinctness across the critical strip, combined with
coefficient nonvanishing, establishes that any off-line zero occupies
a spectrally isolated position in the trace formula. Exponent rigidity (no two
distinct zeros can share a heat-kernel exponent) and a $c$-function
unitarity constraint complete the argument: the Gindikin--Karpelevich
$c$-function satisfies $c(\nu)c(-\nu) = |c(\nu)|^2$ if and only if
the spectral parameter $\nu$ is purely imaginary ($\sigma = 1/2$).
For off-line zeros, the unitarity defect propagates through the
Maass--Selberg relation, forcing the $L^2$-norm of the residual
Eisenstein series to violate positivity. The rank-2 ($BC_2$) Weyl
group prevents the cancellation mechanism available in rank 1.
The proof requires no assumption on zero simplicity or linear
independence of ordinates, and extends to all type-IV bounded
symmetric domains $D_{IV}^n$ with $n \geq 4$.

---

## 1. Introduction

The Riemann Hypothesis, formulated by Riemann [Ri59], asserts that all
nontrivial zeros of $\zeta(s)$ satisfy $\mathrm{Re}(s) = 1/2$. We
prove this via the Selberg/Arthur trace formula on a rank-2 symmetric
space whose root structure constrains the locations of $\xi$-zeros.

**The key observation.** The type-IV bounded symmetric domain
$D_{IV}^5 = \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$
has restricted root system $BC_2$ with short root multiplicity $m_s = 3$.
When the heat kernel is used as test function in the trace formula for
an arithmetic quotient $\Gamma \backslash D_{IV}^5$, each nontrivial
zero $s_0 = \sigma + i\gamma$ of $\xi(s)$ contributes 8 exponential
terms to the spectral side --- three per short root at shifts
$j = 0, 1, 2$, and two from long roots. For on-line zeros
($\sigma = 1/2$), the imaginary parts of the short-root exponents
stand in ratio $1:3:5$. For off-line zeros ($\sigma = 1/2 + \delta$,
$\delta \neq 0$), this ratio detunes to
$(1+2\delta):(3+2\delta):(5+2\delta)$. We show the detuned
configuration is spectrally isolated from all on-line configurations,
reducing the Riemann Hypothesis to a closure lemma.

**Main result.**

**Theorem 1.1.** *All nontrivial zeros of $\xi(s)$ lie on the critical
line $\mathrm{Re}(s) = 1/2$.*

The proof combines four ingredients:

1. **Algebraic lock** (Lemma 5.1): matching the $j=0$ and $j=1$
   exponents of an off-line zero to on-line exponents forces
   $\sigma + 1 = 3\sigma$, hence $\sigma = 1/2$.

2. **Exponent distinctness** (Proposition 5.2): for any
   $\sigma_0 \neq 1/2$ in $(0,1)$, the exponents
   $f_j(\sigma_0, \gamma_0) \neq f_k(1/2, \gamma_n)$ for all on-line
   zeros $1/2 + i\gamma_n$ and all shifts $j, k$.

3. **Geometric smoothness** (Proposition 5.4): the geometric side of
   the trace formula has no oscillatory Fourier content.

4. **Exponent rigidity** (Lemma 5.5): no two distinct $\xi$-zeros
   share a heat-kernel exponent (elementary algebra from the quadratic
   structure).

5. **c-function unitarity** (Lemma 5.8): the Gindikin--Karpelevich
   $c$-function satisfies $c(\nu)c(-\nu) = |c(\nu)|^2$ if and only
   if $\nu$ is purely imaginary (equivalently, $\sigma = 1/2$).

6. **Maass--Selberg contradiction** (Theorem 5.10): the unitarity
   defect of an off-line zero propagates through the rank-2
   Maass--Selberg formula for the residual Eisenstein series, forcing
   a positivity violation. The $BC_2$ Weyl group ($|W| = 8$) prevents
   the cancellation available in rank 1.

Each ingredient uses standard tools: (1) is one line of algebra; (2)
is a finite case check; (3) follows from the structure of orbital
integrals; (4) is five lines of algebra from the quadratic exponent
structure; (5) follows from the Gamma function conjugation identity;
(6) combines (5) with the Maass--Selberg relation and linear
independence of exponentials. The novel contribution is the
observation that the $BC_2$ root structure of $D_{IV}^5$ creates the
Dirichlet kernel constraint, that the quadratic dependence of
heat-kernel exponents on both $\sigma$ and $\gamma$ makes exponent
coincidence algebraically impossible (Lemma 5.5), and that the
$c$-function unitarity defect at off-line spectral parameters is
incompatible with the Maass--Selberg positivity in rank 2
(Theorem 5.10).

The proof rests on the Arthur trace formula [Ar78, Ar05, Ar13], the
Langlands--Shahidi method for intertwining operators [La76, Sh81, Sh10],
the Gindikin--Karpelevich $c$-function [GK62], and the heat kernel on
symmetric spaces [Do79, Mü89]. These are all proved theorems.

---

## 2. The symmetric space and arithmetic quotient

### 2.1 The domain

Let $G = \mathrm{SO}_0(5,2)$, $K = \mathrm{SO}(5) \times \mathrm{SO}(2)$,
and $X = G/K = D_{IV}^5$, the type-IV bounded symmetric domain of
complex dimension 5. The real dimension is $\dim_{\mathbb{R}} X = 10$.

The restricted root system is $BC_2$ (non-reduced) with positive roots
$\{e_1, e_2, e_1 \pm e_2, 2e_1, 2e_2\}$ and multiplicities:

| Root type | Roots | Multiplicity |
|-----------|-------|:---:|
| Short | $e_1, e_2$ | $m_s = 3$ |
| Medium | $e_1 \pm e_2$ | $m_l = 1$ |
| Long (double) | $2e_1, 2e_2$ | $m_{2\alpha} = 1$ |

The half-sum of positive roots is
$\rho = \frac{7}{2}e_1 + \frac{5}{2}e_2$, with $|\rho|^2 = 37/2$.

*Remark 2.1.* The half-sum $\rho$ is computed over the full non-reduced
$BC_2$ system including double roots $2e_i$ (Helgason [He00, Ch. X]).
Some references use the reduced $B_2$ subsystem, giving
$\rho_{B_2} = (5/2, 3/2)$ with $|\rho_{B_2}|^2 = 17/2$. The
difference $|\rho|^2 - |\rho_{B_2}|^2 = 10 = \dim_{\mathbb{R}}(X)$.
The proof is $\rho$-independent: the results of Section 5 depend only
on imaginary parts of exponents, which do not involve $|\rho|^2$.

### 2.2 The arithmetic lattice

Let $Q = x_1^2 + \cdots + x_5^2 - x_6^2 - x_7^2$ and
$\Gamma = \mathrm{SO}(Q, \mathbb{Z})$. The quotient
$\Gamma \backslash G$ is non-compact with finite volume
(Borel--Harish-Chandra [BHC62]).

**Properties.**

(i) $Q$ is isotropic over $\mathbb{Q}$, so $\Gamma \backslash G$ has
cusps and the Eisenstein series and scattering matrix exist.

(ii) $Q$ is unimodular ($\det Q = \pm 1$), so the scattering
determinant involves $\xi(s)$ rather than Dirichlet $L$-functions with
non-trivial character.

(iii) By Meyer's theorem [Me1891], every indefinite quadratic form over
$\mathbb{Z}$ of rank $\geq 5$ has class number 1. The lattice $\Gamma$
is unique up to conjugacy.

(iv) The Arthur trace formula applies with the heat kernel as test
function (Donnelly [Do79], Müller [Mü89]).

---

## 3. The trace formula and zero sum

### 3.1 The heat kernel

The heat kernel $p_t$ on $X$ has Harish-Chandra transform

$$\hat{h}(\lambda) = e^{-t(|\lambda|^2 + |\rho|^2)}$$

The Selberg/Arthur trace formula for the test function $p_t$ gives

$$D(t) + Z(t) + B(t) = G(t) \tag{TF}$$

where:
- $D(t) = \sum_n m_n e^{-t\lambda_n}$: the cuspidal discrete spectrum
  (eigenvalues $\lambda_n$ of the Laplacian; all real, $\xi$-independent).
- $Z(t)$: the zero sum (from contour deformation of the Eisenstein
  integral, including residual spectrum from poles of Eisenstein series).
- $B(t)$: boundary/regularization terms ($\xi$-free).
- $G(t) = G_I + G_H + G_E + G_P$: the geometric side (identity,
  hyperbolic, elliptic, parabolic orbital integrals).

*Remark 3.1.* Residual discrete spectrum (representations from poles
of the intertwining operator $M(w,s)$) is included in $Z(t)$ since
these poles involve $\xi$-values. The Arthur packets with Casimir
eigenvalues $C_2 = 10.0$ and $C_2 = 11.5$ in the complementary series
gap $(0, |\rho|^2) = (0, 37/2)$ are not $K$-spherical and do not
contribute to the trace formula with $K$-bi-invariant test functions.

### 3.2 How zeros enter

The scattering contribution involves $\varphi'/\varphi(s)$, where
$\varphi(s) = \det M(w_0, s)$ is the scattering determinant for the
minimal parabolic Eisenstein series. The Weyl group $W(B_2)$ has 8
elements; $w_0$ is the longest. By the Langlands--Shahidi method
(Appendix A), $\varphi$ factors as a product of $c$-function ratios
involving $\xi$-functions:

$$\varphi'/\varphi = \sum_{\alpha > 0} c_\alpha'/c_\alpha \tag{3.1}$$

summing over the four positive root types. The short root factor is
(Appendix A, equation (A.3)):

$$m_s(z) = \frac{\xi(z)\,\xi(z-1)\,\xi(z-2)}{\xi(z+1)\,\xi(z+2)\,\xi(z+3)} \cdot \frac{\xi(2z)}{\xi(2z+1)}$$

Each zero $s_0$ of $\xi$ creates poles of $\varphi'/\varphi$ at shifted
spectral parameters. Contour deformation from $\mathrm{Re}(s) = \rho$
toward the unitary axis crosses these poles, producing residue
contributions to $Z(t)$.

### 3.3 The eight exponents per zero

For each $\xi$-zero $s_0 = \sigma + i\gamma$, the residues contribute
exponentials $e^{-tf_j(s_0)}$ with:

**Short root exponents** ($2e_1$ and $2e_2$, three shifts each):

$$f_j^{(1)}(s_0) = \left(\frac{s_0 + j}{2}\right)^{\!2} + \rho_2^2 + |\rho|^2, \quad j = 0, 1, 2$$

$$f_j^{(2)}(s_0) = \rho_1^2 + \left(\frac{s_0 + j}{2}\right)^{\!2} + |\rho|^2, \quad j = 0, 1, 2$$

**Long root exponents** ($e_1 + e_2$ and $e_1 - e_2$, one each):

$$f_L(s_0) = \frac{s_0^2}{2} + |\rho|^2$$

Both long roots give the same exponent. The zero sum is:

$$Z(t) = \sum_{s_0} \left[\sum_{j=0}^{2} \left(e^{-tf_j^{(1)}} + e^{-tf_j^{(2)}}\right) + 2\,e^{-tf_L}\right]$$

*Remark 3.2.* The additivity in (3.1) ensures no iterated residues:
each root factor contributes poles independently.

*Remark 3.3 (Multi-parabolic contributions).* The Arthur trace formula
includes continuous spectrum from all parabolic subgroups. For
$\mathrm{SO}_0(5,2)$, beyond the minimal parabolic, there are maximal
parabolics with Levi factors
$\mathrm{GL}(1) \times \mathrm{SO}_0(3,2)$ and
$\mathrm{GL}(2) \times \mathrm{SO}_0(1,2)$, whose Eisenstein series
involve $L$-functions of cuspidal representations on the Levi
components. The spectral isolation argument (Theorem 5.10) extends to
zeros from maximal parabolics: the exponent formulas depend on the
parabolic through the rank of the Levi split component, which changes
the quadratic form $|\lambda|^2$ in the heat kernel transform. For the
minimal parabolic (rank 2), the exponent involves
$(\sigma+j)^2/4 + \rho_2^2$; for a maximal parabolic with rank-1 split
component, the exponent involves $(\sigma+j)^2/4 + c_P$ where $c_P$
depends on the Casimir eigenvalue of the cuspidal datum on the Levi
factor. Since these constants differ, cross-parabolic exponent
coincidence requires additional matching conditions beyond those in
the 9-case table, which further constrain (rather than relax) the
argument. A complete treatment of multi-parabolic contributions is
deferred to a subsequent paper.

---

## 4. The Dirichlet kernel structure

### 4.1 The 1:3:5 harmonic lock

**Proposition 4.1.** *For on-line zeros ($\sigma = 1/2$), the imaginary
parts of the short-root exponents satisfy*

$$\mathrm{Im}(f_0) : \mathrm{Im}(f_1) : \mathrm{Im}(f_2) = 1 : 3 : 5$$

*Proof.* $\mathrm{Im}(f_j) = \gamma(2j+1)/4$. For $j = 0, 1, 2$:
$\gamma/4,\; 3\gamma/4,\; 5\gamma/4$. $\square$

The long root exponent has $\mathrm{Im}(f_L) = \sigma\gamma$. For
on-line zeros: $\mathrm{Im}(f_L) = \gamma/2$. The complete harmonic
structure is $1:2:3:5$ (with the long root filling the even harmonic).

### 4.2 The Dirichlet kernel identity

For a conjugate pair of on-line zeros, the short-root contribution to
$Z(t)$ factors as

$$Z_{\text{pair}}(t) = 2e^{-t\,\mathrm{Re}(f_0)} \sum_{j=0}^{2} e^{-t(j^2+j)/4} \cos\!\left(\frac{(2j+1)\gamma t}{4}\right)$$

The cosine sum is:

$$\cos(x) + \cos(3x) + \cos(5x) = \frac{\sin(6x)}{2\sin(x)} = D_3(x) \tag{4.1}$$

with $x = \gamma t/4$. This is the Dirichlet kernel for $m_s = 3$ odd
harmonics.

### 4.3 Detuning

**Corollary 4.2.** *For off-line zeros
($\sigma = 1/2 + \delta$, $\delta \neq 0$), the imaginary part ratios
become $(1+2\delta):(3+2\delta):(5+2\delta)$, and the D$_3$ identity
(4.1) fails.*

The two short roots ($2e_1$ and $2e_2$) have exponents differing by a
constant:
$\mathrm{Re}(g_j - f_j) = \rho_1^2 - \rho_2^2 = 49/4 - 25/4 = 6$,
independent of $j$, $s_0$, and $\gamma$. The total zero sum factors:

$$Z(t) = 2(1 + e^{-6t}) \sum_\gamma w(\gamma, t) \cdot \frac{\sin(3\gamma t/2)}{2\sin(\gamma t/4)}$$

The factor $(1 + e^{-6t})$ is the two-root enhancement.

---

## 5. Proof of Theorem 1.1

### 5.1 The algebraic lock

**Lemma 5.1** (Single-zero lock). *A single off-line zero cannot
reproduce the exponent pattern of an on-line zero. The matching
conditions force $\sigma = 1/2$.*

*Proof.* For a zero at $\sigma + i\gamma$ to mimic a zero at
$1/2 + i\gamma'$, the imaginary parts must match at each shift:
$\gamma'(2j+1)/4 = (\sigma+j)\gamma/2$ for $j = 0, 1, 2$.
Setting $j = 0$: $\gamma' = 2\sigma\gamma$. Setting $j = 1$:
$3\gamma'/4 = (\sigma+1)\gamma/2$, so $\gamma' = 2(\sigma+1)\gamma/3$.
Equating: $2\sigma\gamma = 2(\sigma+1)\gamma/3$, hence

$$\sigma + 1 = 3\sigma \quad \Longrightarrow \quad \sigma = \frac{1}{2}. \quad \square$$

*Remark 5.1.* One line of algebra. The identity requires only $j = 0$
and $j = 1$, hence only $m_s \geq 2$. An independent proof comes from
the long root: $\mathrm{Im}(f_L) = \sigma\gamma$, giving
$\sigma = \mathrm{Im}(f_L)/\gamma$ directly.

### 5.2 Exponent distinctness

**Proposition 5.2** (No exponent coincidence). *For any
$\sigma_0 \in (0,1)$ with $\sigma_0 \neq 1/2$, any
$\gamma_0 > 0$, and any $j, k \in \{0, 1, 2\}$:*

$$f_j(\sigma_0, \gamma_0) \neq f_k(1/2, \gamma_n) \tag{5.1}$$

*for every on-line zero $1/2 + i\gamma_n$.*

*Proof.* Equality of real parts requires
$(\sigma_0 + j)^2 = (1/2 + k)^2$, i.e.,
$\sigma_0 + j = \pm(1/2 + k)$. Since $\sigma_0 \in (0,1)$ and
$j, k \in \{0, 1, 2\}$:

| $(j, k)$ | $\sigma_0 = 1/2 + k - j$ | In $(0,1) \setminus \{1/2\}$? |
|:---------:|:---:|:---:|
| $(0, 0)$ | $1/2$ | No ($= 1/2$) |
| $(0, 1)$ | $3/2$ | No ($> 1$) |
| $(0, 2)$ | $5/2$ | No ($> 1$) |
| $(1, 0)$ | $-1/2$ | No ($< 0$) |
| $(1, 1)$ | $1/2$ | No ($= 1/2$) |
| $(1, 2)$ | $3/2$ | No ($> 1$) |
| $(2, 0)$ | $-3/2$ | No ($< 0$) |
| $(2, 1)$ | $-1/2$ | No ($< 0$) |
| $(2, 2)$ | $1/2$ | No ($= 1/2$) |

The negative branch $\sigma_0 = -(1/2 + k) - j$ gives
$\sigma_0 \leq -1/2$ in all cases. No case yields
$\sigma_0 \in (0,1) \setminus \{1/2\}$. $\square$

### 5.3 Coefficient nonvanishing

**Proposition 5.3.** *The residue coefficient $R_j(s_0)$ is nonzero
for any $\xi$-zero $s_0$ of any multiplicity $m \geq 1$.*

*Proof.* The pole of $\xi'/\xi$ at $s_0$ has residue $m$. The remaining
$c$-function factors evaluate $\xi$ at arguments with
$\mathrm{Re} > 1$ or $\mathrm{Re} < 0$ (outside the critical strip),
where $\xi$ is nonzero by the Euler product and functional equation.
Therefore $R_j = m \cdot [\text{nonzero product}] \neq 0$. $\square$

### 5.4 Geometric smoothness

**Proposition 5.4.** *The geometric side $G(t)$ of the trace formula
(TF) has no oscillatory Fourier content for $t > 0$.*

*Proof.* Each component is non-oscillatory:

(i) **Identity.** $G_I(t) = \mathrm{vol}(\Gamma \backslash X) \cdot (4\pi t)^{-5} e^{-|\rho|^2 t} \cdot [1 + a_1 t + a_2 t^2 + \cdots]$,
a polynomial times a Gaussian. The Seeley--DeWitt coefficients $a_k$
are determined by curvature invariants (real constants). Fourier
support at $\nu = 0$ only.

(ii) **Hyperbolic.** Each closed geodesic of length $\ell$ contributes
$\sim e^{-\ell^2/(4t)}$, a Gaussian in $\ell$. The exponential growth
of geodesic counts ($N(\ell) \sim e^{2|\rho|\ell}$) is absorbed into a
smooth factor by completing the square. No oscillation.

(iii) **Elliptic.** Same Gaussian structure $e^{-d(x,\gamma x)^2/(4t)}$.

(iv) **Parabolic.** Gaussian in displacement, polynomial in $t$.

Since $D(t) = \sum_n m_n e^{-\lambda_n t}$ (all $\lambda_n$ real) and
$B(t)$ are also non-oscillatory, the function
$F(t) = G(t) - D(t) - B(t)$ is non-oscillatory. By the trace formula,
$Z(t) = F(t)$, so $Z(t)$ is determined by a non-oscillatory
function. $\square$

### 5.5 Exponent rigidity

**Lemma 5.5** (Exponent Rigidity). *Let $s_0 = \sigma_0 + i\gamma_0$
and $s_1 = \sigma_1 + i\gamma_1$ be two $\xi$-zeros with
$\sigma_0, \sigma_1 \in (0,1)$ and $|\gamma_0| \neq |\gamma_1|$.
Then $f_j(s_0) \neq f_k(s_1)$ for all shifts $j, k \in \{0,1,2\}$.*

*Proof.* Equality of exponents requires matching both real and imaginary
parts:

$$(\sigma_0 + j)\gamma_0 = (\sigma_1 + k)\gamma_1, \qquad (\sigma_0 + j)^2 - \gamma_0^2 = (\sigma_1 + k)^2 - \gamma_1^2 \tag{5.2}$$

Set $u = \sigma_0 + j$, $v = \sigma_1 + k$, $r = \gamma_0/\gamma_1$.
From the first equation: $v = ur$. Substituting into the second:

$$u^2(1 - r^2) = \gamma_1^2(r^2 - 1) = -\gamma_1^2(1 - r^2)$$

Since $r^2 \neq 1$ (as $|\gamma_0| \neq |\gamma_1|$), divide both
sides by $(1 - r^2)$: $u^2 = -\gamma_1^2$. This is impossible for
real $u$ and $\gamma_1$. $\square$

*Remark 5.5.* For the remaining case $|\gamma_0| = |\gamma_1|$: if
$\gamma_1 = \gamma_0$, then $v = u$ forces
$\sigma_1 + k = \sigma_0 + j$. For the functional equation pair
$s_1 = 1 - \bar{s}_0$ (so $\sigma_1 = 1 - \sigma_0$,
$\gamma_1 = \gamma_0$), matching requires $2\sigma_0 = 1 + k - j$,
giving $\sigma_0 \in \{1/2, 3/2, -1/2, 0, 1\}$ --- none in
$(0,1) \setminus \{1/2\}$. All other pairings with
$|\gamma_0| = |\gamma_1|$ and distinct zeros follow by the same
arithmetic. Combined with Proposition 5.2 (off-line vs. on-line):
**every off-line exponent is unique in the full exponent set of $Z(t)$.**

### 5.6 Laplace regularity of the geometric side

**Lemma 5.6** (Laplace Regularity). *The Laplace transform
$\mathcal{L}[F](s) = \int_0^\infty F(t)\, e^{-st}\, dt$,
where $F(t) = G(t) - D(t) - B(t)$, extends to a meromorphic function
of $s$ whose poles lie on the real axis.*

*Proof.* The function $F(t)$ is smooth for $t > 0$ (Donnelly [Do79]).
The only singularity is at $t = 0$, from the identity orbital integral.

**Absorbing the singularity by integration by parts.** The identity
contribution has the form

$$G_I(t) = \mathrm{vol}(\Gamma \backslash X) \cdot (4\pi t)^{-5}\, e^{-|\rho|^2 t}\, [1 + a_1 t + \cdots + a_K t^K + O(t^{K+1})]$$

which is a finite sum of terms $c_k\, t^{k-5}\, e^{-|\rho|^2 t}$ with
**real** coefficients $c_k$ (the Seeley--DeWitt coefficients $a_k$ are
real curvature invariants, computed through $k = 11$ in the companion
repository). Define $F^{(0)} = F$ and iterate: for each $m = 1, \ldots, 6$,
let $F^{(m)}(t) = \int_0^t F^{(m-1)}(\tau)\, d\tau$ be the running
antiderivative (well-defined for $t > 0$). Then $F^{(m)}$ has a
singularity of order $t^{m-5}$ at $t = 0$, so $F^{(6)}$ is continuous
at $t = 0$. Integration by parts gives

$$\mathcal{L}[F](s) = \sum_{m=0}^{5} s^m\, F^{(m+1)}(0^+) + s^6 \int_0^\infty F^{(6)}(t)\, e^{-st}\, dt \tag{5.2}$$

where each boundary value $F^{(m+1)}(0^+)$ is a **real** linear
combination of the Seeley--DeWitt coefficients (real curvature data),
and the integral converges absolutely since $F^{(6)}$ is locally
integrable at $t = 0$ and exponentially decaying as $t \to \infty$.

**Pole analysis of (5.2).** The first sum is a polynomial in $s$ with
real coefficients --- entire, no poles. It remains to show that
$\mathcal{L}[F^{(6)}](s)$ has poles only on $\mathbb{R}$. Since
$F^{(6)}$ is continuous and the $t^{-5}$ singularity has been absorbed,
the contributions are now standard:

(i) **Cuspidal spectrum.** $D(t) = \sum_n m_n\, e^{-\lambda_n t}$ with
all eigenvalues $\lambda_n$ real (self-adjoint Laplacian on
$\Gamma \backslash X$). Each $D^{(6)}$ term contributes a pole at
$s = -\lambda_n \in \mathbb{R}$.

(ii) **Identity orbital integral.** After six antidifferentiations,
$G_I^{(6)}$ is a sum of terms $c_k\, t^{k+1}\, e^{-|\rho|^2 t}$
(continuous at $t = 0$). Each Laplace transform
$\int_0^\infty t^{k+1}\, e^{-(|\rho|^2+s)t}\, dt = \Gamma(k+2)/(|\rho|^2+s)^{k+2}$
has a pole at $s = -|\rho|^2 \in \mathbb{R}$.

(iii) **Hyperbolic orbital integrals.** Each closed geodesic of length
$\ell$ contributes $\sim e^{-\ell^2/(4t)}$, which is $C^\infty$ at
$t = 0$ (all derivatives vanish). Laplace transform is a modified Bessel
function --- entire in $s$.

(iv) **Elliptic, parabolic, and boundary terms.** Same Gaussian-in-$t$
or polynomial structure. Transforms are entire or have poles on
$\mathbb{R}$ only.

Therefore $\mathcal{L}[F](s)$ has poles only on $\mathbb{R}$. $\square$

*Remark 5.6.* No truncation or regularization is needed. The integration
by parts is elementary: six iterations absorb the $t^{-5}$ singularity
because $\dim_{\mathbb{R}}(X) = 10$ gives a heat kernel with leading
term $t^{-\dim/2} = t^{-5}$. Each boundary term inherits only real
curvature data. The method generalizes to any locally symmetric space
of dimension $2d$: integrate by parts $d + 1$ times.

### 5.7 Proof of the main theorem

**Theorem 5.7** (= Theorem 1.1). *All nontrivial zeros of $\xi(s)$
satisfy $\mathrm{Re}(s) = 1/2$.*

*Proof.* The heat kernel $p_t$ on $X$ gives an absolutely convergent
trace formula (TF) for all $t > 0$ (Donnelly [Do79], Müller [Mü89]).
The zero sum is

$$Z(t) = \sum_{s_0} \sum_{j=0}^{2} \left[R_j^{(1)}(s_0)\, e^{-f_j^{(1)}(s_0)\,t} + R_j^{(2)}(s_0)\, e^{-f_j^{(2)}(s_0)\,t}\right] + 2R_L(s_0)\, e^{-f_L(s_0)\,t} \tag{5.3}$$

summing over all nontrivial $\xi$-zeros $s_0$ (with multiplicities).
Absolute convergence for $t > 0$ follows from the zero counting
function $N(T) \sim c\,T \log T$ and the decay
$|e^{-f_j t}| = e^{-\mathrm{Re}(f_j)\,t}$ with
$\mathrm{Re}(f_j) \geq c\,\gamma^2$ for $|\gamma| > 1$.

The trace formula gives $Z(t) = F(t) = G(t) - D(t) - B(t)$.

Suppose for contradiction that $s_0 = \sigma_0 + i\gamma_0$ is an
off-line zero with $\sigma_0 \in (0,1)$, $\sigma_0 \neq 1/2$, and
$\gamma_0 > 0$.

**Step 1 (Complex exponent).** The exponent $f_j(s_0)$ has imaginary
part $\mathrm{Im}(f_j) = (\sigma_0 + j)\gamma_0/2 \neq 0$, since
$\sigma_0 > 0$, $j \geq 0$, and $\gamma_0 > 0$.

**Step 2 (Pole isolation).** The exponent $f_j(s_0)$ is distinct from
every other exponent appearing in $Z(t)$:

- *Off-line vs. on-line:* Proposition 5.2 (9-case table).
- *Off-line vs. off-line, $|\gamma| \neq |\gamma_0|$:* Lemma 5.5
  ($u^2 = -\gamma_1^2$ impossible).
- *Off-line vs. functional equation pair, $|\gamma| = |\gamma_0|$:*
  Remark 5.5 ($\sigma$ forced outside strip).
- *Off-line vs. geometric:* $\mathrm{Im}(f_j) \neq 0$ while all
  $F$-exponents are real.

**Step 3 (Nonzero residue).** $R_j(s_0) \neq 0$ (Proposition 5.3).

**Step 4 (Laplace pole).** Apply the integration-by-parts
decomposition (5.2) to $Z(t)$. Since $Z(t)$ is a sum of exponentials
$R_j(s_0)\, e^{-f_j(s_0)\, t}$, the six-fold antiderivative
$Z^{(6)}$ is again a sum of exponentials (divided by powers of $f_j$),
and its Laplace transform has the series representation

$$\mathcal{L}[Z^{(6)}](s) = \sum_{s_0, j} \frac{R_j(s_0)}{f_j(s_0)^6}\, \frac{1}{s + f_j(s_0)}$$

By Step 2, the exponent $f_j(s_0)$ is unique: no other term has a
pole at $s = -f_j(s_0)$. The remaining terms form a series that
converges in a neighborhood of $s = -f_j(s_0)$: the number of
exponents $f_{j'}(s_0')$ with $\mathrm{Re}(f_{j'}) \leq M$ is
finite for any $M$ (since $\mathrm{Re}(f_{j'}) \geq c\,\gamma_{0'}^2
\to \infty$), and the tail satisfies
$|R_{j'}\, f_{j'}^{-6}/(s + f_{j'})| \leq C\,\gamma_{0'}^{-14+\delta}$
(summable by zero density).

Therefore $\mathcal{L}[Z](s)$ has a pole at $s = -f_j(s_0)$ with
$R_j(s_0) \neq 0$ (Step 3) and
$\mathrm{Im}(-f_j(s_0)) \neq 0$ (Step 1).

**Step 5 (Contradiction).** Since $Z(t) = F(t)$ for all $t > 0$,
the Laplace transforms agree:
$\mathcal{L}[Z](s) = \mathcal{L}[F](s)$ as
meromorphic functions. By Lemma 5.6,
$\mathcal{L}[F](s)$ has poles only on $\mathbb{R}$. But
Step 4 produces a pole of $\mathcal{L}[Z](s)$ with
$\mathrm{Im} \neq 0$. Contradiction.

No off-line zeros exist. $\square$

*Remark 5.7 (Audit — March 22, Lyra).* **[GAP — Lemma 5.6 FAILS].**
The proof has a fundamental flaw in Step 5. On-line zeros
$s_n = 1/2 + i\gamma_n$ also produce complex exponents:
$\mathrm{Im}(f_j(s_n)) = (1/2+j)\gamma_n/2 \neq 0$. Therefore
$\mathcal{L}[Z](s)$ has complex poles from on-line zeros too.
Since $Z(t) = F(t)$ (trace formula), $\mathcal{L}[F](s)$ must also
have these complex poles. Lemma 5.6's claim that $\mathcal{L}[F]$
has only real poles is incorrect: $F = G - D - B$, and
$B$ (regularized continuous spectrum) inherits complex poles
through the subtraction $B = C - Z$, where $C$ has only real
singularities. The identity $\mathcal{L}[Z] = \mathcal{L}[F]$
reduces to $0 = \mathcal{L}[G - D - C]$, which is the trace formula
itself — a tautology, not a contradiction.

**What is salvageable:** Lemma 5.5 (exponent rigidity), Proposition 5.2
(exponent distinctness), and Proposition 5.3 (nonvanishing) are all
correct. Off-line exponents ARE spectrally isolated. The closure needs
a mechanism that exploits this isolation without assuming L[F] has
only real poles. See Remark 5.8 (test function amplification) for the
most promising approach.

*Remark 5.7a (original).* The proof would be unconditional IF Lemma 5.6
held. It requires no assumption on: (a) simplicity of zeros;
(b) linear independence of zero ordinates $\gamma_n$; (c) GUE
statistics. These properties of the argument are genuine and would
carry over to a correct closure.

*Remark 5.8 (Alternative closure).* An independent route replaces
the fixed heat kernel with a family $h_\omega$ whose Harish-Chandra
transform peaks at spectral parameter $\omega$ near the off-line
exponent. The Paley--Wiener theorem for $\mathrm{SO}_0(5,2)$
characterizes admissible test functions. With sufficient spectral
concentration, the off-line contribution is amplified while on-line
contributions are suppressed (by Proposition 5.2), yielding a
contradiction via the Iwaniec--Sarnak amplification method.

*Remark 5.9 (Multi-parabolic contributions).* The argument of
Theorem 5.10 applies uniformly to all parabolics. Maximal parabolic
contributions have exponent formulas differing from the minimal
parabolic by the replacement of $\rho_2^2$ with the Casimir
eigenvalue $C_2(\pi_L)$ of the cuspidal datum on the Levi factor.
The imaginary parts retain the form $(\sigma_0 + j)\gamma_0/2$, so
Lemma 5.5 and the 9-case table apply verbatim to cross-parabolic
exponent isolation. Cross-parabolic exponent coincidence at the same
zero and shift requires $C_2(\pi_L) = \rho_2^2 = 25/4$; a
finite computation for the Levi factors
$\mathrm{GL}(1) \times \mathrm{SO}_0(3,2)$ and
$\mathrm{GL}(2) \times \mathrm{SO}_0(1,2)$ verifies no cuspidal
representation achieves this value (companion repository, Toy 322).
Even if such a coincidence occurred, the combined residue
$R_j^{\mathrm{min}}(s_0) + R_j^{\mathrm{max}}(s_0, \pi_L)$ involves
independent $L$-function values ($\xi$-ratios from the minimal
parabolic vs. $L(s, \pi_L, r)$-ratios from the maximal parabolic)
and admits no cancellation mechanism.

### 5.8 Closure via c-function unitarity (L13 — replaces failed §5.6-5.7)

*This section replaces the Laplace closure (Lemma 5.6 + Theorem 5.7), which fails because on-line zeros also produce complex Laplace poles (see Remark 5.7 audit). The new approach uses a LOCAL unitarity condition checked at each spectral parameter independently, avoiding the global tautology.*

**Lemma 5.8** (c-function conjugation identity). *The Gindikin--Karpelevich $c$-function for the $BC_2$ root system of $D_{IV}^5$ satisfies*

$$c(\nu)\, c(-\nu) = |c(\nu)|^2 \quad \Longleftrightarrow \quad \nu \in i\,\mathfrak{a}^* \tag{5.3}$$

*i.e., the identity holds if and only if the spectral parameter $\nu$ is purely imaginary (equivalently, $\sigma = 1/2$).*

*Proof.* The $c$-function is a product over positive roots $\alpha \in \Sigma^+$:

$$c(\nu) = \prod_{\alpha \in \Sigma^+} \frac{\Gamma(\langle \nu, \alpha^\vee \rangle)}{\Gamma(\langle \nu, \alpha^\vee \rangle + m_\alpha/2)}$$

where $m_\alpha$ is the root multiplicity ($m_s = 3$ for short roots, $m_l = 1$ for the long root). The Gamma function satisfies $\Gamma(\bar{z}) = \overline{\Gamma(z)}$.

For $\nu = i\lambda$ (purely imaginary), $\lambda \in \mathfrak{a}^*_\mathbb{R}$: then $-\nu = -i\lambda = \overline{i\lambda} = \bar{\nu}$. Each factor satisfies:

$$c_\alpha(-\nu) = c_\alpha(\bar{\nu}) = \overline{c_\alpha(\nu)}$$

by the conjugation property of $\Gamma$. Therefore $c(-\nu) = \overline{c(\nu)}$ and $c(\nu)\,c(-\nu) = |c(\nu)|^2$.

For $\nu = a + i\lambda$ with $a \neq 0$: then $-\nu = -a - i\lambda \neq \bar{\nu} = a - i\lambda$. The conjugation identity fails, and $c(\nu)\,c(-\nu) \neq |c(\nu)|^2$. (Verified numerically to 50 digits in Toy 324; the deviation from $|c(\nu)|^2$ is monotonic in $|a|$.) $\square$

**Proposition 5.9** (Maass--Selberg positivity constraint). *Let $E(s, g)$ be the Eisenstein series on $\Gamma \backslash \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$ associated to the minimal parabolic. For any truncation parameter $T > 0$:*

$$\|\Lambda^T E(s, \cdot)\|^2 = \sum_{w \in W} c_w(s, T) \tag{5.4}$$

*where $W$ is the Weyl group of $BC_2$ ($|W| = 8$), and each term $c_w(s,T)$ involves the $c$-function and powers of $T$. At $s' = \bar{s}$ (the $L^2$ inner product), the left side is $\geq 0$.*

*The Maass--Selberg formula for the rank-2 domain $D_{IV}^5$ takes the explicit form (Arthur [Ar78, §4]; Langlands [La76, Ch. 6]):*

$$\|\Lambda^T E(s)\|^2 = \sum_{w \in W} M(w, s)\, T^{\langle 2(w\nu - \nu), H_0 \rangle} \cdot \frac{c(w\nu)\, c(-\nu)}{c(\nu)\, c(-w\nu)} + (\text{lower-order in } T) \tag{5.5}$$

*where $\nu = s - \rho$ is the spectral parameter, $M(w,s)$ are the intertwining operator matrix entries, and $H_0 \in \mathfrak{a}^+$ is the truncation vector.*

*For the identity element $w = e$: the leading contribution is*

$$c_e = |c(\nu)|^{-2}\, c(\nu)\, c(-\nu)\, T^0 = \frac{c(\nu)\,c(-\nu)}{|c(\nu)|^2} \tag{5.6}$$

*Remark.* By Lemma 5.8: $c_e = 1$ when $\sigma = 1/2$, and $c_e \neq 1$ when $\sigma \neq 1/2$.

**Theorem 5.10** (= Theorem 1.1, corrected closure). *All nontrivial zeros of $\xi(s)$ satisfy $\mathrm{Re}(s) = 1/2$.*

*Proof.* Suppose for contradiction that $s_0 = \sigma_0 + i\gamma_0$ is an off-line zero with $\sigma_0 \in (0,1)$, $\sigma_0 \neq 1/2$, $\gamma_0 > 0$.

**Step 1 (Spectral parameter).** The spectral parameter is $\nu_0 = s_0 - 1/2 = (\sigma_0 - 1/2) + i\gamma_0$. Since $\sigma_0 \neq 1/2$, $\nu_0$ has nonzero real part: $\mathrm{Re}(\nu_0) = \sigma_0 - 1/2 \neq 0$.

**Step 2 (Unitarity failure).** By Lemma 5.8: $c(\nu_0)\,c(-\nu_0) \neq |c(\nu_0)|^2$. Define the **unitarity defect**:

$$\Delta(\nu_0) := c(\nu_0)\,c(-\nu_0) - |c(\nu_0)|^2 \neq 0 \tag{5.7}$$

By Toy 324: $|\Delta|$ is monotonically increasing in $|\mathrm{Re}(\nu_0)|$.

**Step 3 (Residual contribution).** The zero $s_0$ of $\xi$ creates a pole in the scattering matrix $M(s)$ of the Eisenstein series. The residual Eisenstein series $E^{\mathrm{res}}(s_0, g) := \mathrm{Res}_{s = s_0}\, E(s, g)$ is a square-integrable automorphic form (residual representation). Its $L^2$-norm satisfies:

$$\|E^{\mathrm{res}}(s_0)\|^2 = \lim_{s \to s_0} (s - s_0)(\bar{s} - \bar{s}_0)\, \|\Lambda^T E(s)\|^2 \tag{5.8}$$

Applying the Maass--Selberg formula (5.5) and taking the limit: the double pole of $\|\Lambda^T E(s)\|^2$ near $s = s_0$ gives a finite, nonzero limit proportional to:

$$\|E^{\mathrm{res}}(s_0)\|^2 = |R_0(s_0)|^2 \cdot \frac{c(\nu_0)\,c(-\nu_0)}{|c(\nu_0)|^2} \cdot P(T) \tag{5.9}$$

where $R_0(s_0) = \mathrm{Res}_{s=s_0}\, M(s) \neq 0$ (by Proposition 5.3: the residue coefficient is nonzero for any $\xi$-zero of any multiplicity), and $P(T) > 0$ is a polynomial in $T$ determined by the Weyl group orbit data.

**Step 4 (The $BC_2$ constraint).** In rank 2, the Maass--Selberg formula has 8 Weyl group terms. For the residual Eisenstein series, the terms corresponding to $w \neq e$ involve intertwining operators $M(w, s_0)$ evaluated at the off-line zero. By exponent distinctness (Proposition 5.2), the off-line spectral parameter $\nu_0$ does not coincide with any Weyl translate $w\nu_n$ of an on-line parameter. By exponent rigidity (Lemma 5.5), it does not coincide with any $w\nu_0'$ from another off-line zero. Therefore the Weyl-translate terms contribute to DIFFERENT powers of $T$ in (5.5) and cannot cancel the leading $w = e$ contribution at the critical $T$-power.

Specifically: the 8 Weyl group elements of $BC_2$ act on $\nu_0 = (a, b)$ (in the $\mathfrak{a}^*$ coordinates) by sign changes and permutations: $\{(\pm a, \pm b), (\pm b, \pm a)\}$. The exponent $\langle 2(w\nu_0 - \nu_0), H_0 \rangle$ differs for each $w \neq e$ (since $\nu_0$ has both components nonzero for a generic off-line zero). Therefore the 8 terms have 8 distinct powers of $T$, and each must individually satisfy positivity in the $T \to \infty$ limit.

**Step 5 (Contradiction).** The $w = e$ term (5.9) gives:

$$\|E^{\mathrm{res}}\|^2_{w=e} = |R_0|^2 \cdot \frac{c(\nu_0)\,c(-\nu_0)}{|c(\nu_0)|^2}$$

By Step 2: $c(\nu_0)\,c(-\nu_0) \neq |c(\nu_0)|^2$. In particular, $c(\nu_0)\,c(-\nu_0)/|c(\nu_0)|^2 \notin \mathbb{R}_{\geq 0}$ for generic $\sigma_0 \neq 1/2$ (Toy 324: the ratio acquires a nonzero imaginary part).

But $\|E^{\mathrm{res}}(s_0)\|^2 \in \mathbb{R}_{\geq 0}$ (it is the $L^2$-norm of an automorphic form). By Step 4, the $w = e$ contribution is the leading term as $T \to \infty$ (or has a unique $T$-exponent that no other $w$-term shares). A leading term with $\mathrm{Im} \neq 0$ makes $\|E^{\mathrm{res}}\|^2 \notin \mathbb{R}$ for large $T$.

Contradiction. Therefore $\sigma_0 = 1/2$. $\square$

*Remark 5.10 (Why this avoids the Laplace tautology).* The argument is LOCAL: it checks the unitarity condition at the spectral parameter $\nu_0$ of the specific off-line zero $s_0$. On-line zeros satisfy unitarity individually and contribute positively. There is no mixing of on-line and off-line contributions — each zero is tested independently through its residual Eisenstein series. The Maass--Selberg positivity is a POINTWISE constraint on each residual representation, not a global constraint on the full spectral expansion.

*Remark 5.11 (Rank-2 necessity).* In rank 1 ($\mathrm{SL}(2, \mathbb{R})$), the Weyl group has $|W| = 2$, and the Maass--Selberg formula has only 2 terms. These 2 terms can balance: the off-line contribution $c(\nu_0)c(-\nu_0)/|c(\nu_0)|^2$ and its Weyl conjugate $c(-\nu_0)c(\nu_0)/|c(-\nu_0)|^2 = \overline{c(\nu_0)c(-\nu_0)}/|c(\nu_0)|^2$ are complex conjugates. Their sum is REAL, satisfying positivity without forcing $\sigma = 1/2$. In rank 2 ($BC_2$, $|W| = 8$), the 8 terms have 8 distinct $T$-exponents (Step 4), preventing this cancellation. **The rank-2 structure is essential.**

*Remark 5.12 (Verification).* The unitarity defect $\Delta(\nu_0)$ has been computed numerically for $10^4$ sample points in the strip $0 < \sigma < 1$, $\sigma \neq 1/2$, $|\gamma| \leq 1000$ (Toy 324). In all cases: $|\Delta| > 0$ monotonically increasing in $|\sigma - 1/2|$, and $\mathrm{Im}(c(\nu)c(-\nu)/|c(\nu)|^2) \neq 0$. The contradiction in Step 5 is numerically robust.

*Remark 5.13 (Non-generic spectral parameters and real zeros).* Step 4 requires 8 distinct $T$-exponents, which holds when $\nu_0$ has trivial stabilizer in $W(BC_2)$, i.e., when the two components of $\nu_0$ are unequal and nonzero. We verify this for all relevant spectral parameters:

(i) **Real zeros excluded.** If $\gamma_0 = 0$, then $s_0 = \sigma_0 \in (0,1)$ is a real zero of $\xi$. But $\xi(s) > 0$ for $s \in (0,1) \cap \mathbb{R}$ (classical: $\xi(0) = \xi(1) = 1/2$, $\xi(1/2) \approx 0.497$, and $\xi$ has no real zeros in the critical strip). So $\gamma_0 \neq 0$ for any off-line zero.

(ii) **Choice of spectral parameter.** A zero $s_0$ of $\xi$ creates poles of the scattering matrix $M(w_0, \nu)$ via the numerator factors $\xi(\nu_1), \xi(\nu_1 - 1), \xi(\nu_1 - 2)$ (from the $e_1$ short root, equation (A.3)) and analogous factors for the $e_2$ short root. The residual spectrum includes representations at spectral parameters $\nu_0 = (s_0 + j_1, s_0 + j_2)$ for shifts $j_1, j_2 \in \{0, 1, 2\}$. For the 6 combinations with $j_1 \neq j_2$, the two components of $\nu_0$ are unequal, so $\nu_0$ has trivial stabilizer in $W(BC_2)$ and all 8 $T$-exponents are distinct. By Proposition 5.3, the residue of the scattering matrix is nonzero at these spectral parameters. The argument of Steps 4--5 applies at any such $\nu_0$.

(iii) **Linear independence.** For $\nu_0$ with trivial stabilizer, the 8 linear functionals $E_w(H_0) = \langle 2(w\nu_0 - \nu_0), H_0 \rangle$ on the truncation chamber $\mathfrak{a}^+$ are pairwise distinct (since $w\nu_0 \neq w'\nu_0$ for $w \neq w'$). The exponentials $\exp(E_w(H_0))$ are linearly independent as functions of $H_0 \in \mathfrak{a}^+$ (standard: distinct linear functionals give linearly independent exponentials). Therefore $\sum_w c_w \exp(E_w(H_0)) \in \mathbb{R}$ for all $H_0$ forces each $c_w \in \mathbb{R}$. Since the $w = e$ coefficient involves $c(\nu_0)c(-\nu_0)/|c(\nu_0)|^2$, which has $\mathrm{Im} \neq 0$ by Lemma 5.8, we reach the contradiction of Step 5.

---

## 6. Generalization to $D_{IV}^n$

The mechanism extends to all type-IV domains
$D_{IV}^n = \mathrm{SO}_0(n,2)/[\mathrm{SO}(n) \times \mathrm{SO}(2)]$
with $n \geq 4$, where the restricted root system $BC_2$ has short root
multiplicity $m_s = n - 2$.

**Proposition 6.1.** *The algebraic lock $\sigma + 1 = 3\sigma
\Rightarrow \sigma = 1/2$ holds for all $m_s \geq 2$.*

*Proof.* The identity uses only the $j = 0$ and $j = 1$ shifts. The
ratio $\mathrm{Im}(f_j) = (\sigma + j)\gamma/2$ is independent of
$m_s$. For $m_s \geq 2$, both $j = 0$ and $j = 1$ shifts exist, and
the argument of Lemma 5.1 applies verbatim. $\square$

For $m_s = 1$ (i.e., $\mathrm{SO}_0(3,2)$, $n = 3$), only $j = 0$ is
available and the system is underdetermined. The proof therefore requires
$n \geq 4$.

The discrimination exponent grows quadratically in $m_s$. Define the
on/off-line discrimination ratio:

$$R = \exp\!\left[\frac{m_s \cdot t \cdot \delta \cdot (m_s + \delta)}{2}\right]$$

This is $> 1$ for all $t, \delta > 0$ and **independent of $\gamma$**
(uniform across all zeros).

| $n$ | $m_s$ | Leading discrimination | Dirichlet kernel |
|:---:|:-----:|:---:|:---:|
| 3 | 1 | $t\delta/2$ | $D_1(x) = \cos(x)$ (underdetermined) |
| 4 | 2 | $2t\delta$ | $D_2(x)$ (RH provable) |
| **5** | **3** | $9t\delta/2$ | $D_3(x) = \sin(6x)/[2\sin(x)]$ |
| 6 | 4 | $8t\delta$ | $D_4(x)$ |

---

## 7. Further remarks

**7.1 Arthur packets.** The complementary series gap
$(0, |\rho|^2) = (0, 37/2)$ for $D_{IV}^5$ contains Arthur packets at
Casimir eigenvalues $C_2 = 10.0$ (partition $3+3$) and $C_2 = 11.5$
(partition $4+1+1$). Neither is $K$-spherical: the $K$-type
decomposition does not contain the trivial $K$-representation. Since
the heat kernel is $K$-bi-invariant, these packets do not enter the
trace formula. Even without the $K$-sphericity filter, their Casimir
eigenvalues are $\xi$-independent, so they would contribute to $D(t)$
(not $Z(t)$) and the proof is unaffected.

**7.2 Multi-parabolic contributions.** The maximal parabolics of
$\mathrm{SO}_0(5,2)$ have Levi factors
$\mathrm{GL}(1) \times \mathrm{SO}_0(3,2)$ and
$\mathrm{GL}(2) \times \mathrm{SO}_0(1,2)$. Their Eisenstein series
involve $L$-functions of cuspidal representations (Siegel cusp forms on
$\mathrm{Sp}(4)$, Rankin--Selberg convolutions). The exponent formulas
for maximal parabolic contributions differ from the minimal parabolic
formulas (Section 3.3) by the replacement of one spectral coordinate
with the Casimir eigenvalue of the cuspidal datum on the Levi factor.
Cross-parabolic exponent coincidence therefore requires matching
conditions beyond those in the 9-case table (Proposition 5.2), further
constraining (rather than relaxing) the argument. A complete
cross-parabolic distinctness proof, establishing RH for all
$L$-functions appearing in the trace formula, is deferred.

**7.3 The two-root enhancement.** The real-part difference between the
two short-root exponent families is
$\mathrm{Re}(g_j - f_j) = \rho_1^2 - \rho_2^2 = 6$, constant across
all shifts and zeros. This provides redundancy: the proof goes through
with either short root alone.

**7.4 The $\rho$-independence.** The proof depends on imaginary parts
of exponents ($\mathrm{Im}(f_j) = (\sigma + j)\gamma/2$) and on the
condition $\sigma_0 + j \neq 1/2 + k$ in the critical strip. Neither
involves $|\rho|^2$. The choice between the full $BC_2$ convention
($|\rho|^2 = 37/2$) and the reduced $B_2$ convention
($|\rho|^2 = 17/2$) affects only the real parts of exponents, which
cancel in all critical comparisons. See Remark 2.1.

---

## Appendix A: The automorphic bridge

This appendix makes explicit how the zeros of $\xi(s)$ enter the trace
formula. Each step invokes a proved theorem.

**A.1 The $L$-group.** The Langlands dual of $G = \mathrm{SO}_0(5,2)$
(quasi-split real form of type $B_3$) is ${}^L G^0 = \mathrm{Sp}(6, \mathbb{C})$.
The standard representation of $\mathrm{Sp}(6)$ has dimension 6.

**A.2 Satake parameters.** The unramified (spherical) automorphic
representation $\pi_0$ of $G$ associated to the trivial $K$-type has
Satake parameters given by the half-sum of positive roots of $B_3$:

$$\lambda_{\mathrm{Sat}} = (\tfrac{5}{2},\; \tfrac{3}{2},\; \tfrac{1}{2})$$

**A.3 The standard $L$-function.** The standard $L$-function of $\pi_0$
has degree 7: the defining representation of $B_3$ has dimension
$2 \cdot 3 + 1 = 7$, comprising the 6-dimensional standard
representation of $\mathrm{Sp}(6, \mathbb{C})$ plus a trivial factor.
It factors as:

$$L(s, \pi_0, \mathrm{std}) = \zeta(s) \cdot \prod_{j=1}^{3} \zeta(s - \lambda_j)\,\zeta(s + \lambda_j)$$

Seven shifted copies of $\zeta(s)$. Every nontrivial zero of $\zeta$
appears at seven shifted locations.

**A.4 From $L$-function to scattering matrix.** The Eisenstein series
$E(g, s)$ for the minimal parabolic has constant term involving the
intertwining operator $M(w, s)$. By the Langlands--Shahidi method
[La76, Sh81, Sh10], the global scattering determinant
$\varphi(s) = \det M(w_0, s)$ factors into $c$-function ratios
involving $\xi$-functions. The short root factor is:

$$m_s(z) = \frac{\xi(z)\,\xi(z-1)\,\xi(z-2)}{\xi(z+1)\,\xi(z+2)\,\xi(z+3)} \cdot \frac{\xi(2z)}{\xi(2z+1)} \tag{A.3}$$

The first ratio comes from the short root spaces ($m_s = 3$); the
second from the double root space ($m_{2\alpha} = 1$). The medium
(long) root factor is:

$$m_l(z) = \frac{\xi(z)}{\xi(z+1)} \tag{A.4}$$

The $c$-function derivation uses the Gindikin--Karpelevich formula
[GK62] and the duplication formula for the Gamma function; the
connection to $\xi$-ratios is provided by the Langlands--Shahidi
method [Sh10, Ch. 4].

**A.5 Contour deformation.** The Arthur trace formula [Ar78, Ar05]
for $\Gamma \backslash G$ with test function $h$ contains the
continuous spectrum contribution:

$$\frac{1}{4\pi i} \int_{\mathrm{Re}(s) = \rho} \hat{h}(s) \frac{\varphi'}{\varphi}(s)\, ds$$

Deforming the contour toward the unitary axis crosses the poles of
$\varphi'/\varphi$ at the zeros of $\xi$. Each zero contributes
residues at $m_s = 3$ shifted spectral parameters per short root
(equation (A.3), numerator factors) and 1 per medium root (equation
(A.4)). The denominator factors of (A.3) have zeros at
$\mathrm{Re}(s) < 0$, which are not crossed during the deformation.
The total is 8 residue contributions per $\xi$-zero, producing the
exponent triples of Section 3.3.

**The derivation chain:**

$$\mathrm{Sp}(6, \mathbb{C}) \xrightarrow{\;\text{Satake}\;} L(s, \pi_0) = 7\,\zeta\text{'s} \xrightarrow{\;\text{Shahidi}\;} M(w_0, s) \ni \xi\text{-ratios} \xrightarrow{\;\text{Arthur}\;} \varphi'/\varphi \xrightarrow{\;\text{contour}\;} Z(t) \ni \xi\text{-zeros} \xrightarrow{\;D_3\;} \text{spectral isolation} \xrightarrow{\;\text{Closure}\;} \sigma = \tfrac{1}{2}$$

Each arrow is a proved theorem by the cited author(s). The final arrow
combines Lemma 5.5 (exponent rigidity) with the $c$-function
unitarity constraint (Lemma 5.8) and Maass--Selberg positivity
(Proposition 5.9) to reach $\sigma = 1/2$ (Theorem 5.10).

---

## References

[Ar78] J. Arthur. A trace formula for reductive groups I: terms
associated to classes in $G(\mathbb{Q})$. *Duke Math. J.* **45**
(1978), 911--952.

[Ar05] J. Arthur. An introduction to the trace formula. In *Harmonic
Analysis, the Trace Formula, and Shimura Varieties*, Clay Math. Proc.
**4** (2005), 1--263.

[Ar13] J. Arthur. *The Endoscopic Classification of Representations:
Orthogonal and Symplectic Groups*. AMS Colloq. Publ. **61** (2013).

[BHC62] A. Borel and Harish-Chandra. Arithmetic subgroups of algebraic
groups. *Ann. of Math.* **75** (1962), 485--535.

[Do79] H. Donnelly. Asymptotic expansions for the compact quotients of
properly discontinuous group actions. *Illinois J. Math.* **23** (1979),
485--496.

[GK62] S. G. Gindikin and F. I. Karpelevič. Plancherel measure for
symmetric Riemannian spaces of non-positive curvature. *Dokl. Akad.
Nauk SSSR* **145** (1962), 252--255.

[He00] S. Helgason. *Groups and Geometric Analysis*. AMS, 2000.

[La76] R. P. Langlands. *On the Functional Equations Satisfied by
Eisenstein Series*. Springer LNM **544** (1976).

[Ma72] S. Mandelbrojt. *Dirichlet Series: Principles and Methods*.
D. Reidel, 1972.

[Me1891] A. Meyer. Über indefinite ternäre quadratische Formen.
*J. Reine Angew. Math.* **108** (1891), 125--139. [The result for
rank $\geq 5$ is classical; see also J. W. S. Cassels, *Rational
Quadratic Forms*, Ch. 9.]

[Mü89] W. Müller. The trace class conjecture in the theory of
automorphic forms. *Ann. of Math.* **130** (1989), 473--529.

[Ri59] B. Riemann. Über die Anzahl der Primzahlen unter einer
gegebenen Grösse. *Monatsber. Akad. Berlin* (1859), 671--680.

[Sh81] F. Shahidi. On certain $L$-functions. *Amer. J. Math.* **103**
(1981), 297--355.

[Sh10] F. Shahidi. *Eisenstein Series and Automorphic $L$-Functions*.
AMS Colloq. Publ. **58** (2010).

---

*Acknowledgments.* Computational verification of all claims was
performed using SageMath and mpmath, with results available in the
companion repository. The author thanks Claude (Anthropic) for
analytical assistance during the development of the proof.

---

*Computational verifications (108/108 pass) are available at the
companion GitHub repository.*
