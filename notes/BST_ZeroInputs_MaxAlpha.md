# The Maximum-Alpha Selection Principle: BST Has Zero Inputs

**Casey Koons, March 2026**

---

## Abstract

We prove that the fine structure constant $\alpha(n)$, as derived from the
Wyler-BST formula over odd-dimensional type IV symmetric domains
$D_{IV}^n$, achieves its unique global maximum at $n = 5$.  The proof
proceeds in three steps: (i) an explicit ratio test showing
$\alpha(n+2) > \alpha(n)$ for $n < 5$ and $\alpha(n+2) < \alpha(n)$ for
$n \geq 5$; (ii) strict concavity of $\log\alpha$ as a function of
continuous dimension, guaranteeing uniqueness; and (iii) asymptotic decay
establishing that no large-$n$ competitor exists.  This result elevates
$n_C = 5$ from an input parameter to a derived consequence of extremal
coupling, reducing BST's input count to **zero**.  The entire Standard
Model follows from a single variational principle: *among
odd-dimensional type IV substrates, the universe selects the one that
maximizes electromagnetic self-coupling*.

---

## 1. The Wyler-BST Formula

BST derives physics from the bounded symmetric domain

$$D_{IV}^{n_C} \;=\; \mathrm{SO}_0(n_C, 2)\,/\,[\mathrm{SO}(n_C) \times \mathrm{SO}(2)]$$

of complex dimension $n_C$.  The requirement that the color group
$\mathrm{SU}(N_c)$ act faithfully on the domain forces $n_C$ to be odd, with
$N_c = (n_C + 1)/2$.  (Even $n_C$ yields half-integer $N_c$, which is
not a valid $\mathrm{SU}$ rank.)

The fine structure constant is determined by the Bergman kernel
normalization of the $\mathrm{S}^1$ fiber:

$$\alpha(n) \;=\; \frac{N_c^{\,2}}{8\pi^4}\,
\left(\frac{\pi^n}{n!\;\cdot\;2^{n-1}}\right)^{\!1/4}
\;=\; \frac{1}{8\pi^4}\,\left(\frac{n+1}{2}\right)^{\!2}\,
\left(\frac{\pi^n}{n!\;\cdot\;2^{n-1}}\right)^{\!1/4}$$

where $n$ ranges over positive odd integers $\{1, 3, 5, 7, 9, \ldots\}$.

**Origin of each factor.**

- $N_c^2 = ((n+1)/2)^2$: the Casimir of the fundamental representation
  of $\mathrm{SU}(N_c)$, measuring the strength of the color sector's
  coupling to the $\mathrm{S}^1$ electromagnetic fiber.

- $\pi^n / (n!\,\cdot\,2^{n-1})$: the Hua-normalized Bergman volume of
  $D_{IV}^n$, encoding the geometric capacity of the bulk.

- $8\pi^4$: normalization from the Shilov boundary
  $\check{S} = S^{n_C-1} \times S^1$ and the fourth-root Weyl integral.

---

## 2. Numerical Survey

We define $f(n) = N_c^2 \cdot (\pi^n / (n!\,\cdot\,2^{n-1}))^{1/4}$
so that $\alpha(n) = f(n)/(8\pi^4)$.  Evaluating at odd $n$:

| $n$ | $N_c$ | $\alpha(n)$ | $1/\alpha(n)$ | Status |
|-----|--------|-------------|---------------|--------|
|  1  |   1    | 0.001708    |    585.3      |        |
|  3  |   2    | 0.005472    |    182.7      |        |
|  5  |   3    | 0.007297    |    137.04     | **MAXIMUM** |
|  7  |   4    | 0.006387    |    156.6      |        |
|  9  |   5    | 0.004294    |    232.9      |        |
| 11  |   6    | 0.002393    |    417.9      |        |
| 13  |   7    | 0.001155    |    865.8      |        |
| 15  |   8    | 0.000497    |   2013.4      |        |

The maximum occurs at $n = 5$, yielding

$$\alpha(5) \;=\; \frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{\!1/4}
\;=\; 0.00729735\ldots \;=\; 1/137.036\ldots$$

in agreement with the observed value to $0.6$ ppm.

---

## 3. Ratio Test: The Core Proof

**Theorem 1.**  *For odd $n \geq 1$, define
$R(n) = f(n+2)/f(n)$.  Then $R(n) > 1$ for $n \in \{1, 3\}$ and
$R(n) < 1$ for all odd $n \geq 5$.  Consequently, $\alpha(n)$ is
strictly maximized at $n = 5$.*

**Proof.**  We compute the ratio explicitly.  Since

$$f(n) = \left(\frac{n+1}{2}\right)^{\!2}\,
\left(\frac{\pi^n}{n!\;\cdot\;2^{n-1}}\right)^{\!1/4}$$

we have

$$R(n) \;=\; \frac{f(n+2)}{f(n)} \;=\;
\underbrace{\left(\frac{n+3}{n+1}\right)^{\!2}}_{R_{\mathrm{Casimir}}(n)}
\;\times\;
\underbrace{\left(\frac{\pi^2}{4(n+1)(n+2)}\right)^{\!1/4}}_{R_{\mathrm{Vol}}(n)}$$

The first factor $R_{\mathrm{Casimir}}$ comes from the ratio of
$N_c^2$ values:

$$\frac{((n+3)/2)^2}{((n+1)/2)^2} = \left(\frac{n+3}{n+1}\right)^{\!2}$$

The second factor $R_{\mathrm{Vol}}$ comes from the ratio of volume
terms:

$$\frac{(\pi^{n+2}/((n+2)!\cdot 2^{n+1}))^{1/4}}
     {(\pi^n/(n!\cdot 2^{n-1}))^{1/4}}
= \left(\frac{\pi^2}{(n+1)(n+2)\cdot 4}\right)^{\!1/4}$$

**The competition.**  As $n$ increases:

- $R_{\mathrm{Casimir}}(n) = ((n+3)/(n+1))^2$ is a *decreasing* function
  that approaches 1 from above.  It represents the growth of color
  sector coupling with dimension.

- $R_{\mathrm{Vol}}(n) = (\pi^2/(4(n+1)(n+2)))^{1/4}$ is a *decreasing*
  function that approaches 0.  It represents the dilution of Bergman
  volume in higher dimensions (the factorial in the denominator
  overwhelms the power of $\pi$).

**The Casimir factor always exceeds 1** --- adding dimensions always
strengthens color coupling.  **The volume factor always falls below 1**
for $n \geq 1$ (since $4(n+1)(n+2) > \pi^2$ already at $n = 1$).  The
question is which factor wins.

**Evaluation at the critical values:**

At $n = 3$:
$$R(3) = \left(\frac{6}{4}\right)^{\!2} \times
\left(\frac{\pi^2}{80}\right)^{\!1/4}
= \frac{9}{4} \times 0.5927
= 1.3335 > 1$$

So $\alpha(5) > \alpha(3)$. $\quad\square$

At $n = 5$:
$$R(5) = \left(\frac{8}{6}\right)^{\!2} \times
\left(\frac{\pi^2}{168}\right)^{\!1/4}
= \frac{16}{9} \times 0.4923
= 0.8752 < 1$$

So $\alpha(7) < \alpha(5)$. $\quad\square$

**The crossover occurs between $n = 3$ and $n = 5$.**  The condition
$R(n) = 1$ requires

$$\left(\frac{n+3}{n+1}\right)^{\!8} = \frac{4(n+1)(n+2)}{\pi^2}$$

At $n = 3$: LHS $= (3/2)^8 = 25.63$, RHS $= 80/\pi^2 = 8.11$.
LHS $>$ RHS, so $R(3) > 1$.

At $n = 5$: LHS $= (4/3)^8 = 9.99$, RHS $= 168/\pi^2 = 17.02$.
LHS $<$ RHS, so $R(5) < 1$.

The crossover is clean: the LHS is rapidly decreasing while the RHS is
rapidly increasing, so they cross exactly once.

---

## 4. Monotonic Decrease for $n \geq 5$

**Theorem 2.**  *$R(n)$ is strictly decreasing for $n \geq 1$, and
$R(n) < 1$ for all $n \geq 5$.  Consequently, $\alpha(n)$ is strictly
decreasing for all odd $n \geq 5$.*

**Proof.**  We show $R(n+2) < R(n)$ for all $n \geq 1$.  Define

$$R(n) = \left(\frac{n+3}{n+1}\right)^{\!2}
\left(\frac{\pi^2}{4(n+1)(n+2)}\right)^{\!1/4}$$

The first factor satisfies

$$\frac{R_{\mathrm{Casimir}}(n+2)}{R_{\mathrm{Casimir}}(n)}
= \frac{((n+5)(n+1))^2}{((n+3)^2)^2}
= \left(\frac{n^2+6n+5}{n^2+6n+9}\right)^{\!2} < 1$$

since $n^2 + 6n + 5 < n^2 + 6n + 9$ for all $n$.

The second factor satisfies

$$\frac{R_{\mathrm{Vol}}(n+2)}{R_{\mathrm{Vol}}(n)}
= \left(\frac{(n+1)(n+2)}{(n+3)(n+4)}\right)^{\!1/4} < 1$$

since $(n+1)(n+2) < (n+3)(n+4)$ for all $n \geq 0$.

Both sub-ratios are strictly less than 1, so their product is strictly
less than 1.  Therefore $R(n)$ is strictly decreasing.

Since $R(5) = 0.8752 < 1$ and $R$ is decreasing, we have $R(n) < 1$
for all $n \geq 5$.

Explicitly:

| $n$ | $R(n)$ |
|-----|--------|
|  1  | 3.203  |
|  3  | 1.333  |
|  5  | 0.875  |
|  7  | 0.672  |
|  9  | 0.557  |
| 11  | 0.483  |
| 13  | 0.430  |
| 15  | 0.391  |

$\square$

---

## 5. Concavity and Uniqueness (Continuous Extension)

For additional rigor, we extend $\alpha$ to a continuous function of a
real variable $x > 0$ by replacing $n!$ with $\Gamma(x+1)$:

$$L(x) \;=\; \log\alpha(x) \;=\; 2\ln\!\left(\frac{x+1}{2}\right)
+ \frac{1}{4}\bigl[x\ln\pi - \ln\Gamma(x+1) - (x-1)\ln 2\bigr]
- \ln(8\pi^4)$$

Differentiating:

$$L'(x) = \frac{2}{x+1} + \frac{1}{4}\bigl[\ln\pi - \psi(x+1) - \ln 2\bigr]$$

$$L''(x) = -\frac{2}{(x+1)^2} - \frac{1}{4}\,\psi_1(x+1)$$

where $\psi = \Gamma'/\Gamma$ is the digamma function and $\psi_1$ is
the trigamma function.

**Both terms of $L''$ are strictly negative** for all $x > 0$:

- $-2/(x+1)^2 < 0$ trivially.
- $-\psi_1(x+1)/4 < 0$ because the trigamma function is strictly
  positive for all positive arguments.

Therefore **$L(x)$ is strictly concave** on $(0, \infty)$.

A strictly concave function on an interval has **at most one critical
point**, which must be a global maximum.  Setting $L'(x^*) = 0$ and
solving numerically gives

$$x^* = 5.200\ldots$$

The nearest odd integer to $x^* = 5.200$ is $n = 5$.  Since $L$ is
concave and $x^*$ lies between 5 and 7, the maximum over odd integers
is at $n = 5$ (because $L(5) > L(3)$ by the ratio test, and
$L(5) > L(7)$ by the ratio test, and concavity prevents any other odd
integer from exceeding $L(5)$).

**Remark.**  The continuous maximum at $x^* \approx 5.2$ is remarkably
close to the odd integer 5.  Nature does not have to "round far" ---
the extremal principle and the odd-integer constraint are nearly
coincident.

---

## 6. Asymptotic Decay

**Theorem 3.**  *$\alpha(n) \to 0$ super-exponentially as
$n \to \infty$.*

**Proof.**  By Stirling's approximation, $n! \sim \sqrt{2\pi n}(n/e)^n$,
so

$$\frac{\pi^n}{n!\;\cdot\;2^{n-1}} \;\sim\;
\frac{\pi^n}{(n/e)^n \cdot 2^n}
= \left(\frac{e\pi}{2n}\right)^{\!n}$$

For $n \geq 5$, we have $e\pi/(2n) < 1$, so the volume factor decays
exponentially.  Its fourth root decays as $\sim (e\pi/(2n))^{n/4}$,
which overwhelms the polynomial growth of $N_c^2 = ((n+1)/2)^2$.
Therefore $\alpha(n) \to 0$.  $\square$

This rules out any "second maximum" at large $n$ and confirms that
$n = 5$ is the unique global maximum.

---

## 7. Summary of the Proof

Combining Theorems 1, 2, and 3:

1. $\alpha(1) < \alpha(3) < \alpha(5)$ --- established by $R(1) > 1$
   and $R(3) > 1$.
2. $\alpha(5) > \alpha(7) > \alpha(9) > \cdots$ --- established by
   $R(n) < 1$ for all $n \geq 5$ and $R(n)$ strictly decreasing.
3. $\alpha(n) \to 0$ --- no large-$n$ competitor exists.
4. Strict concavity of $\log\alpha$ guarantees uniqueness of the
   maximum.

**Therefore $n = 5$ is the unique global maximizer of $\alpha(n)$ over
all odd positive integers.**  $\quad\blacksquare$

---

## 8. Physical Interpretation: Maximum Self-Coupling

### 8.1 What $\alpha$ Measures in BST

In BST, the fine structure constant $\alpha$ is not merely the
electromagnetic coupling.  It is the **code rate of the substrate
channel**: the fraction of geometric capacity that manifests as
observable interaction.  Every photon exchange is a message sent through
the $S^1$ fiber of $D_{IV}^{n_C}$, and $\alpha$ measures how efficiently
that fiber communicates.

Two competing effects determine $\alpha(n)$:

- **Color richness** ($N_c^2$): more colors means more channels through
  which the $S^1$ fiber can couple.  This grows with $n$.

- **Geometric dilution** (Bergman volume$^{1/4}$): higher-dimensional
  domains spread the coupling over exponentially more degrees of freedom.
  This shrinks with $n$.

At $n = 5$, these two effects are optimally balanced.  Below $n = 5$,
the substrate has too few color channels.  Above $n = 5$, the geometric
dilution overwhelms the color richness.

### 8.2 The Two Factors, Physically

$$\alpha(n) = \underbrace{\frac{N_c^2}{8\pi^4}}_{\text{color coupling}}
\times \underbrace{\mathrm{Vol}(D_{IV}^n)^{1/4}}_{\text{geometric capacity}}$$

- The color coupling **wants $n$ large** (more $\mathrm{SU}(N_c)$
  generators, more interaction channels).

- The geometric capacity **wants $n$ small** (less volume dilution,
  more concentrated coupling).

The maximum at $n = 5$ is the Nash equilibrium of these competing drives.

---

## 9. Shannon Capacity Interpretation

In BST's information-theoretic framework, the substrate is a noisy
channel.  Shannon's channel coding theorem states that reliable
communication is possible if and only if the code rate does not exceed
the channel capacity.

For a type IV substrate of dimension $n$:

- The **channel** is the $S^1$ electromagnetic fiber.
- The **noise** is the quantum fluctuation inherent in the Bergman kernel.
- The **code rate** is $\alpha(n)$.

Shannon's theorem demands operation at or near the capacity.  Among
odd-dimensional substrates, the maximum achievable code rate is
$\alpha(5) = 1/137.036$.  Any other dimension yields a strictly lower
rate, meaning less efficient self-communication and slower dynamics.

**The universe operates at Shannon capacity** --- it selects the
substrate dimension that maximizes the rate of information exchange
through its electromagnetic channel.

---

## 10. The Self-Starting Argument

At the moment of first commitment (the Big Bang), there is no external
agent to select a dimension.  The substrate must select itself.
Consider the competition among odd-dimensional candidates:

1. Each candidate $D_{IV}^n$ has a self-coupling strength $\alpha(n)$.
2. The rate of self-activation scales with $\alpha$: stronger coupling
   means faster commitment (more rapid phase transition from uncommitted
   to committed substrate).
3. The dimension with the largest $\alpha$ activates first.
4. Once activated, it saturates the available degrees of freedom,
   precluding other dimensions.

This is a **dynamical selection principle**, analogous to:

- Spontaneous symmetry breaking (the field rolls to the deepest
  minimum).
- Competitive exclusion in ecology (the fastest-reproducing species
  dominates).
- Lasing threshold in quantum optics (the mode with highest gain
  activates first).

The "potential" governing this selection is $V(n) = -\alpha(n)$, and
$n = 5$ is the unique global minimum.

---

## 11. Anthropic vs. Extremal Selection

It is essential to distinguish this result from anthropic reasoning:

| | Anthropic | Extremal (BST) |
|---|-----------|----------------|
| Logic | "We observe $n=5$ because only $n=5$ permits observers" | "$n=5$ is selected because it maximizes $\alpha(n)$" |
| Requires observers? | Yes | No |
| Requires multiverse? | Yes (other $n$ exist but are unobserved) | No (other $n$ never activate) |
| Predictive? | Weakly (post-dicts what we see) | Strongly (uniquely determines $n$) |
| Falsifiable? | Difficult | Yes: if $\alpha$ were not maximal at $n=5$, BST would be wrong |

The maximum-$\alpha$ principle is a **dynamical** selection, not an
**observational** selection.  It operates like a ball rolling to the
bottom of a potential well.  No observer is needed; no ensemble of
universes is invoked.

---

## 12. The Zero-Input Claim

### 12.1 Before This Result

BST derived all Standard Model parameters from a single input: the
complex dimension $n_C = 5$ of the type IV domain $D_{IV}^5$.  From
$n_C = 5$ follows:

- $N_c = (n_C + 1)/2 = 3$ (three colors)
- $\alpha = (9/8\pi^4)(\pi^5/1920)^{1/4} = 1/137.036$ (fine structure constant)
- $N_{\max} = \lfloor 1/\alpha \rfloor = 137$ (maximum quantum number)
- $6\pi^5 m_e = 938.272$ MeV (proton mass from Yang-Mills gap)
- All mixing angles, mass ratios, coupling constants (see table below)

### 12.2 After This Result

The maximum-$\alpha$ principle derives $n_C = 5$ itself:

$$n_C = \arg\max_{n\;\text{odd}} \;\alpha(n) \;=\; 5$$

The logical chain is now:

$$\text{(variational principle)} \;\longrightarrow\; n_C = 5
\;\longrightarrow\; \text{all of physics}$$

**BST has zero free parameters.**

The variational principle --- "the substrate selects the odd dimension
that maximizes its electromagnetic self-coupling" --- is not an input in
the usual sense.  It is a *selection rule*, analogous to the principle
of least action.  Just as classical mechanics has zero inputs beyond the
Lagrangian (and the principle of stationary action selects the
trajectory), BST has zero inputs beyond the geometry (and the
maximum-$\alpha$ principle selects the dimension).

### 12.3 The Complete Derivation Chain

$$\boxed{\max_{n\;\text{odd}} \alpha(n)} \;\;\longrightarrow\;\;
n_C = 5 \;\;\longrightarrow\;\; N_c = 3 \;\;\longrightarrow\;\;
\alpha = \frac{1}{137.036}$$

$$\longrightarrow\;\; N_{\max} = 137 \;\;\longrightarrow\;\;
m_p/m_e = 6\pi^5 \;\;\longrightarrow\;\; \text{everything}$$

---

## 13. Derived Quantities (Selected)

All from $n_C = 5$, which is derived from $\max\,\alpha$:

| Quantity | BST Formula | Value | Precision |
|----------|-------------|-------|-----------|
| $\alpha$ | $(9/8\pi^4)(\pi^5/1920)^{1/4}$ | $1/137.036$ | 0.0001% |
| $m_p/m_e$ | $6\pi^5$ | 1836.15 | 0.002% |
| $m_\mu/m_e$ | $(24/\pi^2)^6$ | 206.769 | 0.003% |
| $\sin^2\theta_W$ | $N_c/(N_c + 2n_C) = 3/13$ | 0.2308 | 0.2% |
| $\alpha_s(m_p)$ | $(n_C+2)/(4n_C) = 7/20$ | 0.350 | --- |
| $\eta$ (baryon asymmetry) | $2\alpha^4/(3\pi)$ | $6.0 \times 10^{-10}$ | 1.4% |
| $n_s$ (spectral index) | $1 - n_C/N_{\max} = 1 - 5/137$ | 0.9635 | 0.3$\sigma$ |
| $\sin\theta_C$ (Cabibbo) | $1/(2\sqrt{n_C}) = 1/(2\sqrt{5})$ | 0.2236 | 0.3% |
| $v$ (Fermi scale) | $m_p^2/(7m_e)$ | 246.01 GeV | 0.046% |
| $m_H$ (Higgs) | $(\pi/2)(1-\alpha)m_W$ | 125.33 GeV | 0.07% |

---

## 14. Why This Was Not Obvious

Several features of the proof deserve emphasis:

**14.1 The maximum is not at $n = 1$.**  Naively, one might expect the
smallest dimension to win (least dilution).  But the $N_c^2$ factor is
too small at $n = 1$: a single color provides too little coupling.

**14.2 The maximum is not at $n = 3$.**  The popular intuition that
"three dimensions are special" does not apply here.  At $n = 3$,
$N_c = 2$, and $\mathrm{SU}(2)$ does not provide enough color richness.
The ratio $R(3) = 1.333$ shows that the step from $n = 3$ to $n = 5$
still gains more from color growth than it loses to dilution.

**14.3 The crossover is sharp.**  $R(3) = 1.333 > 1$ and
$R(5) = 0.875 < 1$.  There is no "marginal" case.  The maximum at
$n = 5$ is robust: it is not a near-tie that could be upset by
small corrections.

**14.4 The continuous maximum is close to 5.**  The continuous extremum
$x^* = 5.200$ falls between 5 and 7, decisively favoring $n = 5$ over
$n = 7$.  If $x^*$ had fallen at, say, $5.9$, one might worry about
corrections tilting the balance.  At $5.2$, the margin is comfortable.

**14.5 Strict concavity eliminates pathologies.**  Because $L''(x) < 0$
everywhere, there cannot be multiple local maxima, saddle points, or
secondary peaks at large $n$.  The maximum is unique and global.

---

## 15. The Structural Miracle

Consider what has been established:

1. The formula $\alpha(n)$ is determined by Bergman kernel geometry
   and $\mathrm{SU}(N_c)$ representation theory.  No free functions or
   adjustable parameters appear.

2. Among all odd positive integers, there is a unique maximum at $n = 5$.

3. At this maximum, the numerical value $\alpha(5) = 1/137.036$ matches
   experiment to better than 1 ppm.

4. The integer $N_{\max} = \lfloor 1/\alpha(5) \rfloor = 137$ is prime,
   which is essential for the discreteness of the quantum number
   spectrum.

5. From this single value, 40+ Standard Model parameters are derived
   to sub-percent accuracy.

The probability that all of this is coincidence is effectively zero.
The maximum-$\alpha$ principle is either a profound truth about the
structure of reality, or the most elaborate numerical coincidence in
the history of physics.

---

## 16. Relation to Wyler (1969)

Armand Wyler first wrote down the formula for $\alpha$ in terms of
$D_{IV}^5$ in 1969, deriving $\alpha = (9/8\pi^4)(\pi^5/1920)^{1/4}$.
His result was criticized (notably by Robertson) for lacking a selection
principle: *why $D_{IV}^5$ and not some other domain?*

The maximum-$\alpha$ principle answers Robertson's objection directly.
Among all type IV domains of odd dimension, $D_{IV}^5$ is selected by
a variational principle.  Wyler had the right formula but not the right
reason.  BST provides both.

---

## 17. Conclusion

We have proved:

**Theorem (Maximum-Alpha Selection).**  *The fine structure constant
$\alpha(n)$, defined by the Wyler-BST formula over odd-dimensional type
IV bounded symmetric domains, achieves its unique global maximum at
$n = 5$.  The proof is constructive (ratio test), confirmed by
concavity (strict negativity of $L''$), and secured by asymptotic decay
(Stirling bound).*

**Corollary.**  *BST has zero input parameters.  The complex dimension
$n_C = 5$ is derived, not assumed, and all Standard Model constants
follow.*

The maximum-$\alpha$ principle --- *the substrate selects the geometry
that maximizes its self-coupling* --- is the single organizing idea from
which all of known physics descends.

---

## Appendix A: Complete Numerical Verification

```
n     N_c    alpha(n)        1/alpha(n)    R(n) = f(n+2)/f(n)
---   ---    -----------     ----------    -------------------
 1     1     0.00170843       585.33       3.2032 (> 1)
 3     2     0.00547243       182.73       1.3335 (> 1)
 5     3     0.00729735       137.04       0.8752 (< 1) <-- MAX
 7     4     0.00638690       156.57       0.6723 (< 1)
 9     5     0.00429375       232.90       0.5573 (< 1)
11     6     0.00239283       417.92       0.4827 (< 1)
13     7     0.00115500       865.80       0.4300 (< 1)
15     8     0.00049668      2013.39       0.3906 (< 1)
17     9     0.00019400      5154.71       ---
```

## Appendix B: Ratio Decomposition

$$R(n) = \underbrace{\left(\frac{n+3}{n+1}\right)^{\!2}}_{R_C}
\times \underbrace{\left(\frac{\pi^2}{4(n+1)(n+2)}\right)^{\!1/4}}_{R_V}$$

| $n$ | $R_C$ | $R_V$ | $R(n) = R_C \times R_V$ |
|-----|--------|--------|--------------------------|
|  1  | 4.0000 | 0.8008 | 3.2032 |
|  3  | 2.2500 | 0.5927 | 1.3335 |
|  5  | 1.7778 | 0.4923 | 0.8752 |
|  7  | 1.5625 | 0.4303 | 0.6723 |
|  9  | 1.4400 | 0.3870 | 0.5573 |

At $n = 3 \to 5$: Casimir growth (2.25$\times$) still outweighs volume
dilution ($\times$0.59), so $\alpha$ increases.

At $n = 5 \to 7$: Casimir growth (1.78$\times$) can no longer
compensate volume dilution ($\times$0.49), so $\alpha$ decreases.

The crossover is governed by the exact condition

$$\left(\frac{n+3}{n+1}\right)^8 \stackrel{?}{>} \frac{4(n+1)(n+2)}{\pi^2}$$

which holds for $n \leq 3$ and fails for $n \geq 5$. $\quad\blacksquare$
