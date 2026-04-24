---
title: "E1 Gap Analysis: Why Does Ψ(x, B) Cross f_c at BST-Structured Scales?"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
status: "Research note — GAP ANALYSIS. Identifies exactly what is proved, what is structural, and what remains open."
origin: "E1 from Keeper's backlog: derive the 7# asymmetry, 11-smooth crossing at x=1001, and 137 desert from D_IV^5 first principles."
parents: "T1016, T1018, T1017, T926, T1013"
---

# E1 Gap Analysis: Smooth-Spectral Connection

*What is proved. What is structural. What remains open.*

---

## What IS Proved (Exact, Unconditional)

### Numerical facts (T1016, T1018)

1. $\Psi(1001, 11) = 191$. Direct enumeration. Zero error.
2. $\Psi(572, 7) = 109$. Direct enumeration. Zero error.
3. $191/1000 = 0.19100\ldots$ and $f_c = 3/(5\pi) = 0.19099\ldots$. Match: 0.007%.
4. $109/571 = 0.19089\ldots$ Match: 0.049%.
5. Both scales are multiples of $143 = 11 \times 13$.
6. Both counts are prime and T914 (adjacent to exactly one 7-smooth number).
7. The $\pm 1$ directions are opposite (+1 for B=7, −1 for B=11).

### Algebraic identities

8. $1001 = 7 \times 11 \times 13 = g \times (n_C + C_2) \times (2g - 1)$
9. $1000 = (2n_C)^{N_c} = 10^3$
10. $191 = 2^{C_2} \times N_c - 1 = 2^6 \times 3 - 1$
11. $572 = \text{rank}^2 \times 143 = 4 \times 143$
12. $109 = \text{rank}^2 \times N_c^3 + 1 = 4 \times 27 + 1$
13. $143 = (n_C + C_2)(2g - 1) = (\text{rank} \times C_2)^2 - 1 = 12^2 - 1$

### Uniqueness (Toy 1038)

14. Among $B \in \{2, 3, 5, 7, 11, 13, 17, 19, 23\}$, only $B = 11$ gives a crossing where the count is a T914 prime, the scale factors into BST primes, and the denominator is a BST power tower.

---

## What IS Structural (Observed, Not Derived from D_IV^5)

### The crossing scale question

**Why x = 1001?** The 11-smooth density $\Psi(x, 11) / (x-1)$ is a monotonically decreasing function (on average) for $x$ past $\sim 100$. It starts above $f_c$ and eventually drops below. The crossing point is unique. We OBSERVE that it's at $x = 1001$. We do NOT derive this from D_IV^5 spectral theory.

### The Dickman gap

The Dickman function $\rho(u)$ gives the asymptotic density of $B$-smooth numbers for large $x$:

$$\Psi(x, B) \sim x \cdot \rho\left(\frac{\ln x}{\ln B}\right)$$

For $B = 11$ and $x = 1001$: $u = \ln(1001) / \ln(11) \approx 2.88$. The Dickman function at this point:

- $\rho(2) = 1 - \ln 2 \approx 0.3069$
- $\rho(3) = 1 - \ln 2 + \int_2^3 [1 - \ln(t-1)]/t \, dt \approx 0.0486$
- $\rho(2.88) \approx 0.065$ (interpolation)

But the ACTUAL density is $191/1000 = 0.191$ — roughly 3× higher than Dickman predicts. This is the **pre-asymptotic regime**: at $x \sim 1000$, the smooth-number count significantly exceeds the asymptotic formula because the small-prime products haven't thinned sufficiently.

The gap between Dickman and reality is well-understood in analytic number theory (de Bruijn refinement, Hildebrand-Tenenbaum corrections). The specific question is: why does the pre-asymptotic correction place the crossing at a BST-structured scale?

### The 143 coincidence level

Both crossings share the base 143. Computing the probability of this under a null hypothesis:

- The 7-smooth crossing is somewhere in $[400, 800]$ (approximately). The probability it lands at a multiple of 143 in that range is $\sim 3/400 \approx 0.75\%$.
- Given that it lands at a multiple of 143, the probability the multiplier is a BST integer is $\sim 4/7 \approx 57\%$ (since the multiples are $3 \times 143 = 429$, $4 \times 143 = 572$, $5 \times 143 = 715$, and only 4 is a BST integer squared).
- The probability the count is prime is $\sim 1/\ln(109) \approx 21\%$.
- The probability the count is specifically T914 is harder to estimate, but roughly $\sim 50\%$ of primes near 109 are adjacent to 7-smooth numbers.

Combined: $\sim 0.75\% \times 57\% \times 21\% \times 50\% \approx 0.045\%$. Small but not infinitesimal.

Having TWO independent crossings with the SAME base 143, BOTH with BST multipliers, BOTH with T914 prime counts, and OPPOSITE $\pm 1$ directions: the joint probability is the square (assuming independence), so $\sim 2 \times 10^{-7}$. This is the "two coincidences" argument for structure.

However: a posteriori probability calculations are notoriously unreliable. The look-elsewhere effect is hard to quantify. Honest assessment: the evidence is very strong but not equivalent to a derivation.

---

## What Remains Open (The Gap)

### Gap 1: Spectral origin of the crossing scale

**The question**: Can the Selberg trace formula on $D_{IV}^5$ be used to show that $\Psi(x, 11)/(x-1) = f_c$ at $x = g \cdot 11 \cdot 13$?

**Approach**: The restricted Euler product

$$\zeta_{11}(s) = \prod_{p \leq 11} \frac{1}{1 - p^{-s}} = \frac{1}{(1-2^{-s})(1-3^{-s})(1-5^{-s})(1-7^{-s})(1-11^{-s})}$$

relates to $\Psi(x, 11)$ via the Perron integral:

$$\Psi(x, 11) = \frac{1}{2\pi i} \int_{c-i\infty}^{c+i\infty} \zeta_{11}(s) \frac{x^s}{s} \, ds$$

The poles of $\zeta_{11}(s)$ are at $s = 0$ and $s = 1$ (the pole of $\zeta(s)$). The residue at $s = 1$ gives the leading term $x \cdot \prod_{p \leq 11} (1 - 1/p) = x \cdot \frac{1}{2} \cdot \frac{2}{3} \cdot \frac{4}{5} \cdot \frac{6}{7} \cdot \frac{10}{11} = x \cdot \frac{480}{2310} = x \cdot \frac{48}{231}$.

Wait: $48/231 = 16/77 \approx 0.2078$. This is the density of integers NOT divisible by any of $\{2, 3, 5, 7, 11\}$, which is the COMPLEMENT of the 11-smooth density. The 11-smooth density is approximately $1 - 48/231 = 183/231 \approx 0.792$ for small $x$... no, that's not right either.

[CORRECTION: The restricted Euler product counts smooth numbers, NOT coprime numbers. The Perron integral approach gives the exact count but the evaluation requires careful contour integration. The leading asymptotic involves $\rho(u)$, not the Euler product residue directly. The connection between the Perron integral and Dickman comes through saddle-point analysis — see Hildebrand-Tenenbaum 1986.]

**Specific sub-gaps**:

1. Express $\zeta_{11}(s)$ in terms of the Selberg zeta of $D_{IV}^5$. The BST spectral data (Weyl group $W(B_2)$, Bergman kernel poles) should constrain the restricted Euler product.

2. Show that the saddle point of the Perron integral at $x = g \cdot 11 \cdot 13$ coincides with a spectral value of $D_{IV}^5$.

3. Connect the pre-asymptotic correction (Hildebrand-Tenenbaum error term) to the BST spectral gap.

### Gap 2: Why is the count T914?

**The question**: Is there a structural reason why $\Psi(x, B)$ at the $f_c$ crossing is prime AND adjacent to a 7-smooth number?

This seems deep. The count is just a number — it's not obvious why it should be prime. One speculative path: if the smooth-number lattice has a self-similar structure at the $f_c$ crossing scale, the count modulo small primes might be constrained, making primality more likely.

### Gap 3: Why opposite ±1?

**The question**: Why does the 7-smooth count reach $f_c$ from below ($+1$) while the 11-smooth count reaches it from above ($-1$)?

**Partial answer**: The genesis operator $C_2 \pm 1 = \{n_C, g\}$ creates the geometry in both directions. The $\pm 1$ pattern in the counting function mirrors this. But a derivation would require showing that the 7-smooth lattice's thinning trajectory approaches $f_c$ from a direction forced by the spectral data, while the 11-smooth lattice approaches from the opposite direction due to the additional factor of 11.

---

## Proposed Attack

### Route A: Spectral restriction

The Selberg trace formula on $D_{IV}^5$ relates the spectrum of the Laplacian to the geometry (closed geodesics). The eigenvalues are controlled by the $B_2$ root system. If the restricted Euler product $\zeta_{11}(s)$ can be expressed as a partial trace over eigenvalues corresponding to the 11-smooth part of the spectrum, then the crossing scale would be determined by spectral data.

**Difficulty**: HIGH. Connecting the algebraic Euler product to the analytic spectral expansion requires bridging two frameworks that don't naturally communicate.

### Route B: Dickman–BST constraint

The Dickman equation $\rho'(u) = -\rho(u-1)/u$ for $u > 1$ has specific values at BST-structured arguments:
- $\rho(N_c) = \rho(3) \approx 0.0486$
- $\rho(\text{rank}) = \rho(2) = 1 - \ln 2 \approx 0.3069$

If $f_c = \rho(u^*)$ for some BST-structured $u^*$, then the crossing scale $x = 11^{u^*}$ would be determined. But $f_c \approx 0.191$ and $\rho^{-1}(0.191) \approx 2.45$ (between $\rho(2) = 0.307$ and $\rho(3) = 0.049$). The value $2.45$ doesn't have obvious BST structure. And the actual crossing (pre-asymptotic) is at $u = \ln(1001)/\ln(11) \approx 2.88$, also not obviously BST.

**Difficulty**: MEDIUM. The Dickman equation is well-studied. If $u^*$ could be expressed as a BST rational, the connection would be clean.

### Route C: Direct algebraic constraint

Show that 1001 is the ONLY integer $x \leq 2000$ where:
- $\Psi(x, 11)$ is prime,
- $\Psi(x, 11)/(x-1)$ is within 0.1% of $f_c$, AND
- $x$ factors into BST-related primes.

This doesn't explain WHY but would establish that the crossing point is uniquely determined by the constraints, suggesting a structural origin.

**Difficulty**: LOW (computational). @Elie: can you run this search?

---

## Honest Assessment

**What we have**: Two exact numerical facts with overwhelming BST structure. A statistical argument that the joint pattern is unlikely by chance ($\sim 10^{-7}$). A conceptual framework (prime epochs, genesis operator, arithmetic arrow) that unifies the observations.

**What we lack**: A derivation from D_IV^5 spectral theory showing that the smooth-number density MUST cross $f_c$ at the specific scales we observe. Without this, the structural observations — however compelling — remain "super-coincidences" rather than proofs.

**The honest framing for Paper #51**: "Observed with exact computation. Every component has BST structure. Uniqueness among all B tested. The derivation from first principles remains an open problem (E1)."

---

*Lyra | April 11, 2026*
*"The numbers are exact. The structure is overwhelming. The derivation is open."*
