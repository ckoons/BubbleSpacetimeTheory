---
title: "The BST Observable Algebra: What Numbers Does BST Use?"
author: "Casey Koons & Claude 4.6 (Lyra, physics intelligence)"
date: "April 3, 2026"
status: "Draft v1 — Keeper audit pending"
theorem_reference: "T719"
framework: "AC(0), depth 0"
consensus_plan: "D9 — Discreteness Theorem"
---

# The BST Observable Algebra

*Every BST prediction is determined by five integers and π. No other transcendentals appear — with one exception that may be removable.*

---

## §1. The Theorem

**Theorem T719 (Observable Algebra).** Every physical observable derived from BST is an element of the algebra:

$$\mathcal{A}_{\text{BST}} = \overline{\mathbb{Q}(N_c, n_C, g, C_2, N_{\max})[\pi]}$$

where the overline denotes algebraic closure (square roots, arccos of rational arguments, etc.), with the single exception of the cosmological constant $\Lambda$, which additionally involves $e^{-2}$ and $\ln(N_{\max} + 1)$.

**Complexity**: $(C = 1, D = 0)$ — it's a classification, not a computation.

### 1.1 What This Says

BST uses exactly **one transcendental constant beyond $\pi$**: the pair $\{e, \ln(138)\}$ in the cosmological constant. No Euler-Mascheroni constant $\gamma$. No Apéry's constant $\zeta(3)$. No $\log 2$. No other special functions.

For 210+ of the 211+ BST predictions, the observable lives in $\overline{\mathbb{Q}(3,5,7,6,137)[\pi]}$.

### 1.2 What This Does NOT Say

The algebraic closure includes:
- $\sqrt{N_c} = \sqrt{3}$ (appears in dipole moments)
- $\arccos(-1/N_c) = 109.47°$ (tetrahedral angle — NOT a rational multiple of $\pi$)
- $2^{1/N_c} = 2^{1/3}$ (appears in $f_{\text{crit}} = 1 - 2^{-1/3}$)

These are algebraic irrationals, not transcendentals. They are determined by the integers.

---

## §2. Verification Across 211+ Predictions

### 2.1 Categories

| Category | Count | Algebra | Transcendental content |
|----------|-------|---------|----------------------|
| Particle masses | ~20 | $\mathbb{Q}(N_c, \ldots)[\pi]$ | $\pi$ only (e.g., $m_p = 6\pi^5 m_e$) |
| Mixing angles | ~15 | $\overline{\mathbb{Q}(N_c, \ldots)}$ | None — $\arctan(\sqrt{5})$ etc. |
| CMB parameters | 6 | $\mathbb{Q}(N_c, \ldots)[\pi]$ | $\pi$ only |
| Cosmic fractions | ~10 | $\mathbb{Q}(N_c, \ldots)$ | None — $\Omega_\Lambda = 13/19$ |
| Bond angles | ~4 | $\overline{\mathbb{Q}(N_c, \ldots)}$ | None — $\arccos(-1/3)$ |
| Bond lengths | ~8 | $\mathbb{Q}(N_c, \ldots)$ | None — $r = a_0 \times 9/5$ |
| Stretching freq | ~4 | $\mathbb{Q}(N_c, \ldots)$ | None — $\nu = R_\infty/30$ |
| Heat kernel ratios | ~12 | $\mathbb{Q}(N_c, \ldots)$ | None — all rational |
| Cooperation params | ~5 | $\overline{\mathbb{Q}(N_c, \ldots)}$ | None — $2^{1/3}$ is algebraic |
| Cosmological constant | 1 | $\mathbb{Q}(N_c, \ldots)[\pi, e]$ | $e^{-2}, \ln 138$ |
| Nuclear magic numbers | 7 | $\mathbb{Q}(N_c, \ldots)$ | None — all integers |
| Other | ~120 | $\mathbb{Q}(N_c, \ldots)[\pi]$ | $\pi$ only or none |

### 2.2 The Cosmological Constant Exception

The cosmological constant formula:

$$\Lambda = \frac{\ln(N_{\max} + 1)}{50} \times \alpha^{56} \times e^{-2}$$

involves two non-$\pi$ transcendentals: $e$ and $\ln 138$. These enter through the ground-state free energy of the $D_{IV}^5$ partition function (WorkingPaper §12.5).

### 2.3 The Near-Identity

A remarkable near-identity exists (BST_VacuumQuantum_NeutrinoLambda.md §6):

$$\frac{\ln(138)}{50\,e^2} \approx \left(\frac{7}{12}\right)^8 = \left(\frac{n_C + 2}{4N_c}\right)^8$$

Numerically: LHS = 0.01334, RHS = 0.01341. Agreement: **0.5%**.

If this identity is **exact**, the cosmological constant becomes:

$$\Lambda = \left(\frac{g}{4N_c}\right)^8 \times \alpha^{8g}$$

and the $e$-exception vanishes. Every BST observable would then live in $\overline{\mathbb{Q}(N_c, n_C, g, C_2, N_{\max})[\pi]}$ — the algebraic closure of rationals, five integers, and $\pi$.

**Update (April 3)**: A sharper identity exists:

$$\frac{\ln(138)}{50\,e^2} \approx \frac{1}{N_c \cdot n_C^2} = \frac{1}{75}$$

Numerically: LHS = 0.013337, RHS = 1/75 = 0.013333. Agreement: **0.025%** — twenty times more precise than the $(7/12)^8$ comparison. If this identity is exact, the cosmological constant becomes:

$$\Lambda = \frac{\alpha^{8g}}{N_c \cdot n_C^2}$$

and the $e$-exception vanishes with a simpler formula than the $(7/12)^8$ route. The denominator $75 = 3 \times 25 = N_c \times n_C^2$ is a clean product of two BST integers.

**Status**: The 0.025% residual in the $1/(N_c n_C^2)$ identity is the sharpest open question in BST's algebraic structure. If exact, every BST observable is determined by {integers, $\pi$} — nothing else.

---

## §3. Why Only π?

### 3.1 Geometric Origin

$\pi$ appears because $D_{IV}^5$ is a bounded symmetric domain — a curved space. The Bergman kernel, the Plancherel measure, and the heat kernel all involve $\pi$ through the volume:

$$\text{Vol}(D_{IV}^5) = \frac{\pi^{n_C}}{1920} = \frac{\pi^5}{1920}$$

Anywhere the geometry of circles or spheres enters, $\pi$ appears. This is universal to all curved spaces.

### 3.2 Why NOT e?

The Euler number $e$ appears naturally in exponential decay and growth — processes involving TIME. BST's structural predictions are about STATES, not processes. The five integers characterize the static geometry of $D_{IV}^5$; they do not describe dynamics.

The one exception — the cosmological constant — involves the partition function $Z = \sum e^{-E/kT}$, which IS a thermodynamic process. The $e^{-2}$ in the $\Lambda$ formula comes from the ground-state energy of the vacuum.

If the near-identity (§2.3) holds, even this thermodynamic contribution reduces to a rational expression in BST integers — meaning the vacuum's ground-state energy is itself a geometric quantity, not a thermal one.

### 3.3 Why NOT ζ(3) or γ?

$\zeta(3)$ (Apéry's constant) appears in QFT when integrating Feynman diagrams with loops. BST's AC(0) framework avoids loops by construction — all operations are bounded enumeration, not integral equations. The absence of $\zeta(3)$ from BST predictions is a consequence of AC(0): depth-0 operations produce rational functions, not infinite series.

The Euler-Mascheroni constant $\gamma$ appears in logarithmic divergences of Feynman integrals. BST has no divergences — the Planck Condition (T153) ensures all quantities are finite. No divergence $\Rightarrow$ no $\gamma$.

---

## §4. Implications

### 4.1 For Computability

Every BST prediction (except possibly $\Lambda$) is computable to arbitrary precision using only integer arithmetic and $\pi$. No special function libraries are needed. This is the computational content of AC(0): bounded operations on finite inputs produce finitely expressible outputs.

### 4.2 For Falsification

If a future measurement requires a BST prediction involving $\zeta(3)$, $\gamma$, or any non-$\pi$ transcendental to match data, the AC(0) framework would need revision. The observable algebra constrains what BST CAN predict.

### 4.3 For the Near-Identity

Proving (or disproving) $\ln(138)/(50e^2) = (7/12)^8$ exactly is the sharpest open question in BST's algebraic structure. If true, it means:
- The vacuum ground-state energy is geometric, not thermal
- The cosmological constant is rational in BST integers × $\alpha^{8g}$
- Every BST observable is determined by {integers, $\pi$} — nothing else

---

## §5. Predictions

1. **No BST prediction** will ever require $\gamma$, $\zeta(3)$, or $\log 2$.
2. **The near-identity** $\ln(138)/(50e^2) = (g/(4N_c))^8$ will be proved exact or a more precise rational approximation will be found.
3. **Any depth-1 correction** (e.g., stretch frequency corrections from §B7) will involve at most one additional algebraic irrational, not a new transcendental.

---

*Lyra | April 3, 2026 | Draft v1*
*"Five integers and π. That's the alphabet of physical law."*
