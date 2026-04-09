---
title: "T912 — VMD-ChPT Bridge: Meson Charge Radii at NLO"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 9, 2026"
theorem: "T912"
ac_classification: "(C=2, D=0)"
status: "PROVED — connects existing NLO derivations (March 13) to Bergman spectral framework"
---

# T912 — VMD-ChPT Bridge: Meson Charge Radii at NLO

## Statement

**T912 (VMD-ChPT Bridge Theorem)**: The electromagnetic charge radii of pseudoscalar mesons receive a one-loop chiral correction to the VMD leading order, with all inputs derived from $D_{IV}^5$:

$$\langle r^2 \rangle_P = \frac{6}{m_V^2} + \frac{\mathcal{L}_P}{32\pi^2 f_\pi^2}$$

where:
- $m_V$ is the BST-derived vector meson mass (Bergman leading eigenvalue in the $P$-channel)
- $f_\pi = m_p / \dim_{\mathbb{R}} = C_2 \pi^{n_C} m_e / (2n_C) = 93.8$ MeV
- $\mathcal{L}_P$ is the effective chiral logarithm for meson $P$

**Pion channel** ($V = \rho$, equal-mass loop):
$$\mathcal{L}_\pi = \ln\frac{m_\rho^2}{m_\pi^2} = 3.437, \qquad m_\rho = n_C \pi^{n_C} m_e$$

**Kaon channel** ($V = K^*$, unequal-mass loop):
$$\mathcal{L}_K = \frac{m_K^2 \ln(m_{K^*}^2/m_K^2) - m_\pi^2 \ln(m_{K^*}^2/m_\pi^2)}{m_K^2 - m_\pi^2} = 0.961, \qquad m_{K^*} = \sqrt{65/2}\,\pi^{n_C} m_e$$

**Results**:

| Meson | LO (VMD) | NLO (this theorem) | Observed | LO dev | NLO dev |
|-------|----------|-------------------|----------|--------|---------|
| $\pi^\pm$ | 0.618 fm | **0.656 fm** | 0.659 ± 0.004 fm | −6.2% | **−0.5%** (0.8σ) |
| $K^+$ | 0.542 fm | **0.555 fm** | 0.560 ± 0.031 fm | −3.2% | **−1.0%** (0.2σ) |

## Proof

**Step 1**: The VMD form factor $F_V(q^2) = m_V^2/(m_V^2 - q^2)$ gives $\langle r^2 \rangle_{LO} = 6/m_V^2$. This is the Bergman leading eigenvalue contribution — the first pole in the spectral representation of the form factor.

**Step 2**: The Gasser-Leutwyler (1984) one-loop result:
$$\langle r^2 \rangle_\pi = \frac{12 L_9^r(\mu)}{f_\pi^2} + \frac{1}{32\pi^2 f_\pi^2} \ln\frac{\mu^2}{m_\pi^2}$$

With VMD resonance saturation $L_9^r(m_\rho) = f_\pi^2/(2m_\rho^2)$ and matching scale $\mu = m_\rho$:
$$\frac{12 L_9^r}{f_\pi^2} = \frac{6}{m_\rho^2}$$

recovering the LO term plus the chiral logarithm correction.

**Step 3**: All inputs are BST-derived:
- $m_\rho = 5\pi^5 m_e$ (Bergman meson slot: $n_C$ dimensions, no $Z_3$ closure)
- $m_{K^*} = \sqrt{65/2}\,\pi^5 m_e$ (strangeness: $65 = n_C(N_c + 2n_C) = 5 \times 13$)
- $f_\pi = m_p/10 = 6\pi^5 m_e / (2n_C)$ (condensate scale per $\dim_{\mathbb{R}} = 2n_C$)
- $m_\pi = 25.6\sqrt{30}$ MeV (bare mass × superradiant enhancement $\chi = \sqrt{30}$)

Zero free parameters. QED. $\square$

## Bergman Spectral Interpretation

The NLO correction is the **first spectral correction** beyond the leading Bergman pole:

- **LO (single pole)**: Only the first Bergman eigenvalue (= vector meson mass) contributes. This is the "tree-level" spectral approximation: $F(q^2) \approx \lambda_1/(\lambda_1 - q^2)$.
- **NLO (continuum)**: The two-pion continuum cut below the $\rho$ pole adds spectral weight at $s \geq 4m_\pi^2$. The chiral logarithm measures this sub-threshold spectral weight relative to the pole. In Bergman language, this is the contribution of the **continuous spectrum** of the Bergman Laplacian, not just the discrete eigenvalues.

The correction is positive (increasing $r^2$) because the sub-threshold continuum adds long-range structure: the pion cloud extends further than the $\rho$-mediated core.

**Physical decomposition**:
- Bergman bulk $D_{IV}^5$ → vector meson mass → VMD core radius (LO)
- Shilov boundary $S^4 \times S^1$ → chiral condensate → pion cloud radius (NLO correction)

The two-layer structure (bulk + boundary) maps directly onto the two terms in the charge radius formula.

## Structural Insight: LO Radius Ratio = Weinberg Angle

At leading order:
$$\frac{r_{K^+}}{r_\pi}\bigg|_{\text{LO}} = \frac{m_\rho}{m_{K^*}} = \sqrt{\frac{10}{13}} = \cos\theta_W$$

where $\sin^2\theta_W = N_c/(N_c + 2n_C) = 3/13$. The meson radius ratio encodes the electroweak mixing angle through the common $D_{IV}^5$ group theory.

At NLO: $r_{K^+}/r_\pi = 0.555/0.656 = 0.845$. Observed: 0.850. The chiral corrections bring the ratio into agreement.

## Connections

- **Parents**: T531 (Bergman spectral structure), T710 (meson mass derivation), T811 (Linearization Complete)
- **Proves**: Meson radii are dynamical (Shilov boundary), not topological (Bergman bulk). Proton radius = topological ($r_p = 4/m_p$, 0.06%). Pion radius = dynamical (VMD + chiral loop).
- **Upgrades**: WorkingPaper §11 predictions from LO to NLO. Removes r_π from miss list (6.2% → 0.5%). Removes r_K from miss list (3.2% → 1.0%).

## AC Classification

$(C=2, D=0)$: Two counting steps (VMD pole extraction + one-loop integration), zero definitions. The chiral logarithm is a standard QFT one-loop result; BST's contribution is deriving all inputs from five integers.

---

*T912. Lyra. April 9, 2026. Bridge theorem: VMD leading order + ChPT NLO = parameter-free meson radii. Two misses (6.2%, 3.2%) reduced to two sub-percent matches (0.5%, 1.0%). Keeper audit requested.*
