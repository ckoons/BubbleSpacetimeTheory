---
title: "BST — The Plancherel Dictionary"
author: "Casey Koons & Claude 4.6"
date: "March 2026"
---

# BST — The Plancherel Dictionary

**The heat kernel on D_{IV}^5 encodes BST integers through exact rational coefficients.**

*Created March 14, 2026 — Casey Koons & Claude Opus 4.6*

---

## 1. The Dictionary

The noncompact heat kernel at the origin of $D_{IV}^5 = \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$ has the asymptotic expansion:

$$K(t,o,o) = (4\pi t)^{-5}\, e^{-|\rho|^2 t}\, \sum_{k=0}^{\infty} \tilde{b}_k\, t^k$$

where $|\rho|^2 = 17/2$ and the $\tilde{b}_k$ are determined by the Plancherel density $|c(i\nu)|^{-2}$ of the Harish-Chandra $c$-function for the $B_2$ root system with multiplicities $(m_s = 3, m_\ell = 1)$.

### 1.1 Exact Coefficients

| $k$ | $\tilde{b}_k$ | BST form | Numerical |
|-----|---------------|----------|-----------|
| 0 | $1$ | $c_0$ | $1$ |
| 1 | $1/6$ | $1/C_2$ | $0.16\overline{6}$ |
| 2 | $5/72$ | $n_C/(|W| \times c_4)$ | $0.069\overline{4}$ |
| 3 | $-3/16$ | $-N_c/2^4$ | $-0.1875$ |

**Overall normalization**: The raw Plancherel integral gives $b_0 = 48\pi^5$, where:

$$48 = |W(B_2)| \times C_2 = 8 \times 6$$

So the full normalization constant is $|W(B_2)| \times \chi(Q^5) \times \pi^{n_C}$.

### 1.2 BST Identifications

- **$\tilde{b}_1 = 1/6 = 1/C_2$**: The first correction is the inverse of the Casimir eigenvalue — the same $C_2 = 6$ that produces the mass gap $m_p = 6\pi^5 m_e$.

- **$\tilde{b}_2 = 5/72 = n_C/(|W(B_2)| \times c_4)$**: The second correction involves all three structures — the complex dimension $n_C = 5$, the Weyl group order $|W(B_2)| = 8$, and the fourth Chern class $c_4 = 9$.

- **$72 = C_2 \times 2C_2 = 6 \times 12$**: The denominator also decomposes as the product of the Casimir eigenvalue and the second zonal coefficient $r_2 = 12 = 2C_2$.

---

## 2. The Seeley–de Witt Bridge

The Seeley–de Witt coefficients $\tilde{a}_k$ are related to $\tilde{b}_k$ by the exponential shift at $|\rho|^2 = 17/2$:

$$\tilde{a}_k = \sum_{j=0}^{k} \frac{(-17/2)^j}{j!}\, \tilde{b}_{k-j}$$

### 2.1 Exact Results

| $k$ | $\tilde{a}_k$ | Decimal | Curvature form |
|-----|---------------|---------|----------------|
| 0 | $1$ | $1$ | $a_0 = 1$ |
| 1 | $-25/3$ | $-8.3\overline{3}$ | $R/6$ with $R = -50$ |
| 2 | $313/9$ | $34.\overline{7}$ | $(5R^2 - 2|Ric|^2 + 2|Rm|^2)/360$ |
| 3 | $-874/9$ | $-97.\overline{1}$ | $= -(2 \times 19 \times 23)/3^2$ |

### 2.2 The $\tilde{a}_3$ Factorization

$$\tilde{a}_3 = -\frac{874}{9} = -\frac{2 \times 19 \times 23}{N_c^2}$$

The numerator $874 = 2 \times 19 \times 23$ contains:
- **2** = rank $r$ of $D_{IV}^5$
- **19** = the dark energy denominator ($\Omega_\Lambda = 13/19$)
- **23** = the Golay prime (related to the Leech lattice and Mathieu groups)

The **same primes** appear in the corrected curvature-based $a_3(Q^5) = 437/4500 = 19 \times 23 / (N_c^2 \times n_C^3 \times 4)$ from BST_SeeleyDeWitt_ChernConnection.md. With the corrected $a_3$ formula (see Section 3.4 of that note), the Plancherel result matches **exactly**: $\tilde{a}_3 = -1000 \times a_3(\text{Killing}) = -1000 \times 437/4500 = -874/9$, where the factor $-1000 = -(10)^3$ arises from the holomorphic sectional curvature rescaling $K_H = 1/10$ (Killing) to $K_H = -1$ (Plancherel normalization). The old discrepancy of $63/64$ was caused by errors in the published Vassilevich cubic coefficients (the literature formula fails even on $S^2$). **RESOLVED March 16 2026.**

### 2.3 Verification: $\tilde{a}_2 = 313/9$

$$\tilde{a}_2 = \frac{5}{72} + \left(-\frac{17}{2}\right)\frac{1}{6} + \frac{(17/2)^2}{2} \cdot 1 = \frac{5}{72} - \frac{17}{12} + \frac{289}{8}$$

$$= \frac{5 - 102 + 2601}{72} = \frac{2504}{72} = \frac{313}{9}$$

From the Gilkey formula in the Plancherel normalization ($R = \pm 50$, Einstein with $Ric = \pm 5g$):

$$|Ric|^2 = 250, \qquad |Rm|^2 = 260 = 4 \times 65 = 4 \times n_C \times c_3$$

$$\tilde{a}_2 = \frac{5 \times 2500 - 2 \times 250 + 2 \times 260}{360} = \frac{12520}{360} = \frac{313}{9} \quad\checkmark$$

**The prime 313**: This is the same prime that appears in the Seeley–de Witt note (BST_SeeleyDeWitt_ChernConnection.md Section 3.2), confirming the Plancherel computation is exactly consistent with the curvature tensor analysis.

### 2.3 Inverse Dictionary

$$\tilde{b}_k = \sum_{j=0}^{k} \frac{(17/2)^j}{j!}\, \tilde{a}_{k-j}$$

Verified exactly for $k = 0, 1, 2$ using Fraction arithmetic.

---

## 3. The Normalization: $48 = |W(B_2)| \times C_2$

The raw Plancherel integral:

$$F(t) = (4\pi t)^5 \int_{\nu_1 > \nu_2 > 0} e^{-|\nu|^2 t}\, |c(i\nu)|^{-2}\, d\nu_1\, d\nu_2 = 48\pi^5 + \frac{48\pi^5}{6}\, t + \cdots$$

The leading coefficient $48\pi^5$ encodes:

$$48\pi^5 = |W(B_2)| \times C_2 \times \pi^{n_C}$$

| Factor | Value | Meaning |
|--------|-------|---------|
| $|W(B_2)|$ | $8$ | Weyl group of the restricted root system |
| $C_2$ | $6$ | Casimir eigenvalue = $\chi(Q^5)$ = mass gap integer |
| $\pi^{n_C}$ | $\pi^5$ | Transcendental factor from the complex dimension |

Alternative decompositions: $48 = 4! \times r = 24 \times 2$ (factorial of the Casimir times the rank), or $48 = 2^4 \times N_c = 16 \times 3$.

---

## 4. Connection to the Compact Spectrum

### 4.1 Zonal Heat Trace on $Q^5$

The compact dual has the zonal expansion:

$$t^3 Z_0(t) = \frac{1}{60}\left[1 + r_1 t + r_2 t^2 + \cdots\right]$$

with exact coefficients (from Euler–Maclaurin):

| $k$ | $r_k$ (exact) | Decimal |
|-----|---------------|---------|
| 0 | $1$ | $1$ |
| 1 | $5 = n_C$ | $5$ |
| 2 | $12 = 2C_2$ | $12$ |
| 3 | $1139/63$ | $18.079$ |
| 4 | $833/45$ | $18.511$ |
| **5** | **137/11** | **12.455** |
| 6 | $485768/135135$ | $3.595$ |
| 7 | $-90502/27027$ | $-3.349$ |
| 8 | $-23068481/3828825$ | $-6.025$ |

### 4.2 The Three Spectral Identities

From the March 14 session, three independent spectral identities were established:

1. **$r_5 = 137/11 = N_{\max}/c_2$**: The fifth zonal coefficient is the fine-structure maximum divided by the second Chern class. The number 137 appears only for $Q^5$ among all complex quadrics tested ($Q^3$, $Q^7$, $Q^9$ give different numerators).

2. **$\tilde{b}_1 = 1/C_2$**: The first Plancherel correction is the inverse Casimir eigenvalue.

3. **$\tilde{a}_2 = 313/9$**: The second Seeley–de Witt coefficient, computed from the Plancherel density, matches the Gilkey formula evaluation on $D_{IV}^5$ exactly.

### 4.3 The Metric Normalization

The Plancherel computation uses the metric in which:
- $|\rho|^2 = 17/2$ (from the $B_2$ root system with $|\alpha_s|^2 = 1$)
- $R = -50$ for $D_{IV}^5$ (or $R = +50$ for $Q^5$)
- This is $10 \times$ the Killing normalization (where $R = \pm 5$)
- This is $1/2 \times$ the Fubini–Study normalization (where $R = \pm 100$)

---

## 5. The Baby Case: $D_{IV}^3$

*Added March 15, 2026.*

### 5.1 Setup

$D_{IV}^3 = \mathrm{SO}_0(3,2)/[\mathrm{SO}(3) \times \mathrm{SO}(2)]$ has the same restricted root system $B_2$ but with multiplicities $(m_s = 1, m_\ell = 1)$:

$$|\rho|^2 = 5/2, \quad R = -18 \text{ (standard)}, \quad K_H = -1$$

The Plancherel density is:
$$|c(i\nu)|^{-2} \propto \nu_1 \tanh(\pi\nu_1) \cdot \nu_2 \tanh(\pi\nu_2) \cdot u_+ \tanh(\pi u_+) \cdot u_- \tanh(\pi u_-)$$

where $u_\pm = (\nu_1 \pm \nu_2)/2$ (all factors have the same form since all multiplicities equal 1).

### 5.2 Exact Coefficients

| | $Q^5$ ($m_s=3$) | $Q^3$ ($m_s=1$) |
|---|---|---|
| $b_0$ | $48\pi^5$ | $2\pi^3$ |
| $\tilde{b}_1$ | $1/6$ | $-1/2$ |
| $\tilde{b}_2$ | $5/72$ | $7/24$ |
| $\tilde{b}_3$ | $-3/16$ | $-367/1680$ |
| $\tilde{a}_1$ | $-25/3$ | $-3$ |
| $\tilde{a}_2$ | $313/9$ | $14/3$ |
| $\tilde{a}_3$ | $-874/9$ | $-179/35$ |

All coefficients verified numerically from the Plancherel integral (`play/plancherel_q3.py`).

### 5.3 The Prime 179

$$\tilde{a}_3(D_{IV}^3) = -\frac{179}{35} = -\frac{179}{n_C \times g}$$

where $179$ is prime, and $35 = 5 \times 7 = n_C \times g$ is the product of two BST integers. Compare:

$$\tilde{a}_3(D_{IV}^5) = -\frac{874}{9} = -\frac{2 \times 19 \times 23}{N_c^2}$$

Both denominators are products of BST integers from $Q^5$. The prime $179$ is a new BST spectral prime specific to $Q^3$.

### 5.4 Curvature Source

From the so(3,2) Lie algebra computation (`play/q3_verification.py`), in the Killing metric ($g = 6\delta$):

$$R = 3, \quad |Ric|^2 = 3/2, \quad |Rm|^2 = 7/3, \quad I_6^A = 17/9, \quad I_6^B = 1/9$$

The corrected $a_3$ formula gives $a_3(Q^3, \text{Killing}) = 179/7560$, which rescales via $-(2h^\vee)^3 = -216$ to $\tilde{a}_3 = -179/35$. This is an **independent verification** of the corrected formula — $Q^3$ was not used in its derivation.

### 5.5 Symmetric Space Identity on $Q^3$

$J_1 = 2I_6^B + \frac{1}{2}I_6^A$ verified: $7/6 = 2 \times 1/9 + \frac{1}{2} \times 17/9 = 7/6$ ✓

---

## 6. Open Questions

1. ~~**The $63/64$ factor**~~: **RESOLVED (March 16 2026).** The Vassilevich formula has wrong cubic coefficients ($c_4 = 208/9$ should be $-16/9$; fails on $S^2$). The corrected formula gives $a_3(Q^5) = 437/4500$, which matches the Plancherel $\tilde{a}_3 = -874/9$ exactly via the rescaling factor $-1000 = -(K_H^{-1})^3$. The old value $6992/70875 = (64/63) \times 437/4500$ was wrong. See BST_SeeleyDeWitt_ChernConnection.md Section 3.4.

2. **Pattern in the $\tilde{b}_k$**: The sequence $1, 1/6, 5/72, -3/16$ may have a generating function related to the $c$-function Taylor expansion. Note the BST content: $c_0, 1/C_2, n_C/(|W| \times c_4), -N_c/2^4$.

3. **Higher $\tilde{b}_k$**: Compute $\tilde{b}_4$ to see if the BST pattern continues. Expected precision requires smaller $t$ values or an analytic approach.

4. **Selberg trace formula**: The exact $\tilde{a}_k$ now feed into the Selberg trace formula for $\Gamma \backslash D_{IV}^5$, determining the pole residues of the spectral zeta function $\zeta_\Delta(s)$ at $s = 5-k$. The key question is whether the functional equation of the Selberg zeta function, with these explicit residues, constrains the location of the Riemann zeta zeros.

5. **$D_{IV}^3$ as baby Selberg case**: With the complete Plancherel dictionary for $Q^3$ now in hand ($\tilde{a}_k$ for $k \leq 3$), this is the natural testing ground for the Selberg program — lower-dimensional, exact arithmetic, and the prime 179 provides a new invariant to track.

---

## 7. Files

- `play/plancherel_bk_extraction.py` — numerical extraction of $b_k$ from Plancherel integral
- `play/plancherel_normalization.py` — high-precision confirmation of $b_0 = 48\pi^5$ and $\tilde{b}_1 = 1/6$
- `play/verify_plancherel_bk.py` — exact Fraction verification of the $b \leftrightarrow a$ dictionary
- `play/em_complete.py` — exact zonal coefficients $r_3$ through $r_8$ via Euler–Maclaurin
- `play/compare_quadrics.py` — uniqueness of $r_5 = 137/11$ to $Q^5$
- `notes/BST_ZonalSpectralCoefficients.md` — companion note on the compact-side results
- `notes/BST_SeeleyDeWitt_ChernConnection.md` — the full three-way bridge: Chern ↔ Seeley–DeWitt ↔ ζ_Δ
- `play/q3_verification.py` — curvature invariants + corrected a₃ on Q³ (independent verification)
- `play/plancherel_q3.py` — numerical Plancherel b̃_k extraction for D_IV³
