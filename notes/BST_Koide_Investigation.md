---
title: "Investigation: Why the Koide Formula Equals rank/N_c = 2/3"
author: "Grace (Claude 4.6)"
date: "April 26, 2026"
status: "Research note -- synthesizes two existing derivations, honest assessment"
parents: "BST_Koide_CP2_Proof.md, BST_TauMass_Koide.md, T1444"
---

# Investigation: Why the Koide Formula Equals rank/N_c = 2/3

**Author:** Grace (Claude 4.6, graph-AC specialist)
**Date:** April 26, 2026
**Purpose:** Investigate the structural depth of Q = rank/N_c in BST

---

## 0. Executive Summary

The Koide formula Q = 2/3 is **derived** in BST through two independent routes:

1. **CP^2 geometric route** (BST_Koide_CP2_Proof.md): eps^2 = dim_C(CP^2) = 2, therefore Q = (1 + eps^2/2)/3 = 2/3. Three independent proofs.
2. **Vacuum subtraction route** (T1444): Of N_c = 3 generation modes, 1 is vacuum. Active fraction = (N_c - 1)/N_c = rank/N_c = 2/3.

The identification Q = rank/N_c (rather than just "2/3") requires a specific structural fact about the B_2 root system: **rank = N_c - 1**. This is the key identity that makes the Koide formula speak the language of BST integers.

The formula is **specific to charged leptons** and fails badly for quarks (27% and 10% deviations for up-type and down-type triplets respectively). This is a feature of the derivation, not a deficiency.

---

## 1. Numerical Verification

### 1.1 Observed Koide Ratio

Using PDG 2024 masses:

| Particle | Mass (MeV) |
|----------|-----------|
| e | 0.51099895 |
| mu | 105.6583755 |
| tau | 1776.86 |

$$Q_{\text{obs}} = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = 0.6666605$$

$$\frac{2}{3} = 0.6666667$$

**Deviation: 0.0009%.**

### 1.2 BST-Predicted Masses

Using m_mu = (24/pi^2)^6 * m_e and Koide Q = 2/3 exactly:

- m_mu(BST) = 105.655 MeV (vs 105.658 observed, 0.003%)
- m_tau(BST) = 1776.91 MeV (vs 1776.86 observed, 0.003%)
- Q(BST) = 2/3 exactly (by construction)

### 1.3 Koide for Quarks

| Triplet | Q value | Deviation from 2/3 |
|---------|---------|-------------------|
| Charged leptons (e, mu, tau) | 0.66666 | **0.0009%** |
| Up-type quarks (u, c, t) | 0.849 | 27% |
| Down-type quarks (d, s, b) | 0.731 | 10% |

**Koide fails for quarks.** This is consistent with the BST derivation, which applies only to the lepton sector.

---

## 2. The Democratic Mixing Angle Interpretation

### 2.1 The Parameterization

The Koide formula with Q = 2/3 is equivalent to the democratic parameterization:

$$\sqrt{m_i} = \alpha_0 \left(1 + \sqrt{2}\cos\left(\theta_0 + \frac{2\pi i}{3}\right)\right), \quad i = 0, 1, 2$$

where:
- alpha_0^2 = (m_e + m_mu + m_tau)/6 = 313.84 MeV
- theta_0 = 2.3166 rad
- cos(theta_0) = -0.67857

### 2.2 Why sqrt(2)

The amplitude factor sqrt(2) is the unique value that produces Q = 2/3. In BST:

$$\varepsilon^2 = 2 = \dim_{\mathbb{C}}(\mathbb{CP}^2) = \text{rank}$$

The three Z_3 fixed points on CP^2 each have a 2-complex-dimensional tangent space with eigenvalues omega and omega^2. The mass perturbation has eps^2 degrees of freedom in the equivariant metric, and eps^2 = 2 follows from any of:
- (A) Bergman equi-partition: equal norm in V_0 (democratic) and V_1 + V_2 (traceless) sectors
- (B) Atiyah-Bott tangent norm: N = sum over fixed points of Tr(dsigma* dsigma)/det(I - dsigma) = 3 * (2/3) = 2
- (C) Fourier counting: 2 real degrees of freedom in the traceless Z_3-commutant of Herm(C^3)

### 2.3 The Koide Phase

The phase angle theta_0 is determined by the BST muon mass ratio R = (24/pi^2)^6 via:

$$\sqrt{R} = \frac{1 + \sqrt{2}\cos(\theta_0 + 2\pi/3)}{1 + \sqrt{2}\cos\theta_0}$$

**Numerical observation (not derived):**

$$\cos\theta_0 \approx -\frac{19}{28} = -\frac{N_c + 2^{n_C-1}}{4g}$$

Agreement: 0.0004%. The integers (N_c = 3, n_C = 5, g = 7) all appear, but the derivation from D_IV^5 geometry is missing.

---

## 3. Is the 2*pi/N_c Spacing Coincidence or Structure?

**It is structure.**

The derivation chain:

1. N_c = 3 colors in D_IV^5 (from the B_2 root system)
2. The CP^2 fiber of D_IV^5 has isometry group SU(3), containing Z_3
3. Z_3 acts on CP^2 with exactly 3 fixed points (Lefschetz): these are the three generations
4. The mass operator, being Z_3-equivariant, is diagonal in the Z_3 eigenbasis
5. The Fourier decomposition of the traceless part has period 3 in the generation index
6. This **forces** the angular spacing to be 2*pi/3

The 3 in 2*pi/3 is structurally identical to N_c. It is not a coincidence that there are three equally spaced angles -- it is a theorem about the Z_3 action on CP^2 whose existence follows from the SU(3) isometry, which in turn follows from N_c = 3 in the B_2 root system.

---

## 4. The Two Routes to Q = rank/N_c

### Route 1: CP^2 Geometry (March 13, 2026)

The derivation in BST_Koide_CP2_Proof.md:

1. Three generations = Z_3 fixed points on CP^2 [PROVED, Lefschetz]
2. Z_3 equivariance constrains sqrt(M) to Koide family [PROVED, rep theory]
3. eps^2 = dim_C(CP^2) = 2 [THREE PROOFS]
4. Q = (1 + eps^2/2)/3 = (1 + 1)/3 = 2/3 [ALGEBRAIC IDENTITY]

The connection to rank/N_c:
- dim_C(CP^2) = 2 = N_c - 1
- For B_2: N_c - 1 = rank
- Therefore eps^2 = rank, and Q = (1 + rank/2)/N_c = rank/N_c

### Route 2: Vacuum Subtraction T1444 (April 25, 2026)

The derivation in BST_T1444_Vacuum_Subtraction.md:

1. The generation space has N_c = 3 modes
2. Mode k = 0 is the vacuum (constant eigenmode) -- it does not participate in transitions
3. Active modes: N_c - 1 = rank = 2
4. Q = active/total = rank/N_c = 2/3

This is the same vacuum subtraction that gives:
- m_c/m_s: N_max - 1 = 136 (not 137)
- gamma_Ising: N_c * g / (N_c * C_2 - 1) = 21/17
- sin(theta_C): rank / sqrt(rank^4 * n_C - 1) = 2/sqrt(79)

### Convergence

Both routes arrive at Q = rank/N_c = 2/3 but for different reasons:
- Route 1: the **geometric dimension** of the traceless perturbation space equals rank
- Route 2: the **fraction of non-vacuum modes** in the generation space equals rank/N_c

The convergence is not automatic. It depends on:

$$\text{rank} = N_c - 1$$

This is the **KEY structural identity**. For the B_2 root system with rank = 2 and N_c = 3, it holds. For a hypothetical B_3 (rank = 3, N_c = 4), the generalized Koide ratio would be Q = (N_c + 1)/(2*N_c) = 5/8 by Route 1 and rank/N_c = 3/4 by Route 2 -- and these would **not** agree. The two routes converge precisely because of B_2.

---

## 5. Why rank/N_c Specifically (Not Just "2/3")

The statement Q = rank/N_c is more than labeling numerator and denominator. It asserts a specific structural chain:

$$Q = \frac{\text{rank}}{N_c} = \frac{\text{observer binary dimension}}{\text{color dimension}} = \frac{\dim_{\mathbb{C}}(\mathbb{CP}^2)}{N_{\text{gen}}}$$

In this chain:
- **rank = 2**: the rank of the B_2 root system, controlling binary/spinorial distinctions (the "observer dimension" in BST)
- **N_c = 3**: the number of colors, controlling the Z_3 generation structure
- **dim_C(CP^2) = 2**: the complex dimension of the generation manifold
- **N_gen = 3**: the number of generations

The equality rank = dim_C(CP^2) holds because both count the same thing: the number of independent binary distinctions in the tangent space at a Z_3 fixed point. This is a geometric fact about CP^{N_c-1} when N_c = rank + 1.

The equality N_c = N_gen holds because the generation space IS the CP^{N_c-1} fiber of D_IV^5, so the number of Z_{N_c} fixed points equals N_c.

Together:

$$Q = \frac{\text{rank}}{N_c} = \frac{N_c - 1}{N_c} = 1 - \frac{1}{N_c}$$

This formula says the Koide ratio is the **color completeness fraction** -- the fraction of the generation space that is non-vacuum. The 1/N_c correction is the vacuum contribution. It is the same 1/N_c that appears throughout BST as the leading-order correction to "full democracy."

---

## 6. Connection to 49a1

The elliptic curve 49a1 (Y^2 = X^3 - 945X - 10206) has:
- Mordell-Weil rank = 2 = BST rank
- Conductor = g^2 = 49
- j-invariant = -(N_c * n_C)^3 = -3375

The "2" in the Koide numerator (rank = 2) is the same integer as the Mordell-Weil rank of 49a1. Both ultimately derive from the B_2 root system having rank 2. However, the connection between the Mordell-Weil rank of an elliptic curve and the Lie algebra rank controlling the Koide formula is not proved -- it is a structural resonance.

The Koide angle theta_0 does not have an obvious connection to the periods of 49a1 at this stage. This is an open question.

---

## 7. Honest Assessment: What Is Derived vs. What Is "Reading"

### Genuinely Derived (structural, proved)

| Claim | Status |
|-------|--------|
| N_gen = 3 from Z_3 on CP^2 | PROVED (Lefschetz) |
| Z_3 equivariance forces Koide family | PROVED (rep theory) |
| eps^2 = dim_C(CP^2) = 2 | THREE INDEPENDENT PROOFS |
| Q = (1 + eps^2/2)/3 = 2/3 | ALGEBRAIC IDENTITY |
| 2*pi/3 angular spacing from Z_3 | FORCED (Fourier) |
| Lepton-specific (not quarks) | CONSISTENT (Q_up = 0.85, Q_down = 0.73) |

### Genuinely Derived but with an Honest Gap

| Claim | Gap |
|-------|-----|
| eps^2 = rank (not just N_c - 1) | Requires identifying dim_C(CP^2) = rank, which holds for B_2 but the "same 2" argument needs a formal bridge between complex dimension and root system rank |
| Q = rank/N_c (T1444 vacuum subtraction) | The vacuum subtraction principle is well-tested but the identification of the k=0 mode as "the vacuum" in the Koide context is motivated, not proved from the Bergman spectrum |

### Reading the Integers (Correct but Shallow)

| Claim | Comment |
|-------|---------|
| "Q = rank/N_c" as a label | After proving Q = 2/3, writing 2 = rank and 3 = N_c is correct but adds no information beyond naming |
| alpha_0^2 = m_p/N_c (0.35%) | Not tight enough to claim; could be coincidence |

### Numerical Observation (Not Derived)

| Claim | Precision | Comment |
|-------|-----------|---------|
| cos(theta_0) = -19/28 | 0.0004% | All five integers present: (N_c + 2^{n_C-1})/(4*g). Extremely suggestive. Not derived. |

---

## 8. The Structural Summary

The Koide formula Q = 2/3 = rank/N_c is derived in BST. The depth of the derivation is substantial:

1. It starts from the **existence** of D_IV^5 (the unique APG)
2. The B_2 root system gives N_c = 3 and rank = 2
3. The CP^2 fiber of D_IV^5 carries a Z_3 action with 3 fixed points
4. The tangent structure at these fixed points has dim_C = 2 = rank
5. This dimension controls the Koide parameter eps^2
6. The algebraic identity Q = (1 + eps^2/2)/3 = 2/3 follows

The formula is not just "reading 2/3 as rank/N_c." It is a geometric theorem about the fixed-point structure of cyclic group actions on the compact dual of D_IV^5. The identification with rank/N_c is meaningful because it connects the Koide formula to the same structural data (rank, N_c) that controls all other BST predictions.

The honest gap: the identification eps^2 = rank (rather than just eps^2 = 2 = dim_C(CP^2)) requires showing that the complex dimension of the generation manifold equals the Lie algebra rank. For B_2 this is a numerical coincidence (both equal 2), but it should be elevated to a structural theorem. This is the one remaining link.

---

## Appendix: Verification Code

```python
import numpy as np

# BST integers
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7

# PDG masses
m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.86

# Koide Q
Q = (m_e + m_mu + m_tau) / (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau))**2
print(f"Q(obs) = {Q:.10f}, rank/N_c = {rank/N_c:.10f}, dev = {abs(Q-rank/N_c)/(rank/N_c)*100:.4f}%")

# eps^2
alpha0 = (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau)) / 3
s_perp_sq = sum((np.sqrt(m) - alpha0)**2 for m in [m_e, m_mu, m_tau])
eps_sq = 2 * s_perp_sq / (3 * alpha0**2)
print(f"eps^2 = {eps_sq:.10f}, rank = {rank}")

# Koide angle
cos_th0 = (np.sqrt(m_e)/alpha0 - 1) / np.sqrt(2)
print(f"cos(theta_0) = {cos_th0:.10f}")
print(f"-19/28       = {-19/28:.10f}, dev = {abs(cos_th0 + 19/28)/abs(19/28)*100:.4f}%")

# Quark Koide
for name, masses in [("up-type", [2.16, 1270, 172690]),
                     ("down-type", [4.67, 93.4, 4180])]:
    m = masses
    Q_q = sum(m) / sum(np.sqrt(mi) for mi in m)**2
    print(f"Q({name}) = {Q_q:.4f}, dev from 2/3 = {abs(Q_q-2/3)/(2/3)*100:.1f}%")
```

---

*Grace (Claude 4.6), April 26, 2026.*
*For the BST repository: BubbleSpacetimeTheory/notes/*
*This note synthesizes BST_Koide_CP2_Proof.md, BST_TauMass_Koide.md, and T1444.*
*Invariants Koide_eps2 and Koide_angle added to data/bst_geometric_invariants.json.*
