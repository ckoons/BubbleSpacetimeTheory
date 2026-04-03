---
title: "α⁴ Universality: The Spectral Weight of Rank 2"
author: "Casey Koons & Claude 4.6 (Lyra, physics intelligence)"
date: "April 3, 2026"
status: "Draft v1 — Keeper audit pending"
theorem_reference: "T720"
framework: "AC(0), depth 0"
---

# α⁴ Universality

*Every BST observable that probes the spectral structure of D_IV^5 involves α^{2×rank} = α⁴. The fourth power is not a coincidence — it is the universal spectral weight of a rank-2 bounded symmetric domain.*

---

## §1. The Theorem

**Theorem T720 (α⁴ Universality).** Let $\alpha = 1/N_{\max} = 1/137$ be the fine structure constant derived from the maximal root length of $D_{IV}^5$. Every BST observable that probes the spectral decomposition of $D_{IV}^5$ through restricted root directions contains the factor $\alpha^{2 \times \text{rank}} = \alpha^4$. The fourth power encodes rank 2: each of the two restricted root directions $(e_1, e_2)$ contributes one factor of $\alpha^2$ (coupling × propagator).

**Complexity**: $(C = 2, D = 0)$ — two identifications (power = 2×rank, each root contributes α²).

### 1.1 Three Independent Instances

| Observable | Formula | Domain | Measured | Dev |
|-----------|---------|--------|----------|-----|
| Primordial amplitude | $A_s = (3/4)\alpha^4$ | Cosmology (CMB) | $2.101 \times 10^{-9}$ | 0.92σ |
| Baryon asymmetry | $\eta = 2\alpha^4/(3\pi)$ | Cosmology (baryogenesis) | $6.1 \times 10^{-10}$ | 1.4% |
| Hydrogen fine structure | $\Delta E = \alpha^4 m_e c^2 \times f(n,j,l)$ | Atomic physics | exact | QED-exact |

All three probe fundamentally different physics — the seeds of cosmic structure, the matter-antimatter ratio, and the relativistic corrections to hydrogen energy levels. Yet all three produce $\alpha^4$.

### 1.2 Why Fourth Power

The bounded symmetric domain $D_{IV}^5$ has rank $r = 2$. The restricted root system is $B_2$, with two independent restricted root directions. Each spectral process involves propagation along BOTH root directions:

$$\text{spectral weight} = \prod_{i=1}^{r} \alpha^2 = \alpha^{2r} = \alpha^4$$

Each factor of $\alpha^2$ arises from one root direction: the coupling $\alpha$ appears twice — once for the interaction vertex, once for the propagator — giving $\alpha^2$ per direction.

**General rule**: On a bounded symmetric domain of rank $r$, the universal spectral weight is $\alpha^{2r}$.

| Domain type | Rank | Spectral weight |
|-------------|------|-----------------|
| Rank 1 (e.g., $D_{IV}^1 \cong \mathbb{H}^2$) | 1 | $\alpha^2$ |
| **Rank 2 ($D_{IV}^5$)** | **2** | **$\alpha^4$** |
| Rank 3 (hypothetical) | 3 | $\alpha^6$ |

BST's rank = 2 is determined by the Cartan decomposition of $\mathfrak{so}(5,2)$, not by fitting. The fourth power is a structural invariant of the geometry.

---

## §2. Detailed Analysis of Each Instance

### 2.1 Primordial Amplitude (T712)

$$A_s \times N_{\max}^4 = \frac{N_c}{2^{\text{rank}}} = \frac{3}{4} \quad \text{(exact)}$$

The prefactor $3/4 = N_c/2^{\text{rank}}$ separates physical modes (three color channels) from total tensor modes (four). One mode is gauge. The identity also reads $3/4 = C_2/|W(B_2)| = 6/8$, connecting to the Weyl group.

Cross-product: $N_c \times |W| = C_2 \times 2^{\text{rank}} = 24 = \dim SU(5)$, linking the CMB amplitude to the gauge hierarchy readout at k = 16 (Paper #9).

### 2.2 Baryon Asymmetry

$$\eta = \frac{n_B}{n_\gamma} = \frac{2\alpha^4}{3\pi} = 6.018 \times 10^{-10}$$

The prefactor $2/(3\pi) = 2/(N_c \pi)$: the numerator 2 = rank (two root directions contribute to baryon-producing channels). The denominator $N_c \pi$ = color dimension × the geometric measure of $D_{IV}^5$.

**Physical interpretation**: The baryon asymmetry is the probability that a spectral fluctuation in BOTH root directions simultaneously produces a net baryon number. Two directions × one coupling per direction = $\alpha^4$. The factor $2/(N_c \pi)$ is the geometric probability that this fluctuation is color-singlet.

### 2.3 Hydrogen Fine Structure

$$\Delta E_{nj} = \frac{\alpha^4 m_e c^2}{2n^2} \left[\frac{n}{j + 1/2} - \frac{3}{4}\right]$$

The $\alpha^4$ factor arises from the second-order relativistic correction to the Dirac equation — but in BST, this IS the rank-2 spectral weight. The 3/4 that appears in the hydrogen fine structure formula is the SAME 3/4 = $N_c/2^{\text{rank}}$ that appears in $A_s$. The fine structure of hydrogen and the amplitude of cosmic fluctuations share the same structural constant.

---

## §3. The Universality Pattern

### 3.1 Classification

BST observables can be classified by their α-dependence:

| α-power | Rank factor | Examples | Count |
|---------|-------------|----------|-------|
| $\alpha^0$ | None | Bond angles, mixing angles, cosmic fractions, magic numbers | ~80+ |
| $\alpha^1$ | $\alpha^{1/2}$ per root? | — | 0 (odd powers absent) |
| $\alpha^2$ | One root direction | Lamb shift, anomalous magnetic moment (QED) | ~5 |
| $\alpha^4$ | Both root directions | $A_s$, $\eta$, hydrogen fine structure | ~10 |
| $\alpha^{56}$ | $\alpha^{8g}$ | Cosmological constant $\Lambda$ | 1 |

The absence of odd powers of α is structural: each restricted root direction contributes $\alpha^2$, and the rank-2 decomposition produces only even powers.

### 3.2 The Exception: $\Lambda$

The cosmological constant involves $\alpha^{56} = \alpha^{8g}$, which is $(\alpha^4)^{14} = (\alpha^4)^{2g}$. This is NOT a violation of α⁴ universality — it is the α⁴ factor raised to the power $2g = 14$, reflecting that the vacuum energy sums over $2g$ spectral modes of the Bergman kernel.

If the near-identity $\ln(138)/(50e^2) = (g/(4N_c))^8$ holds (T719, Observable Algebra), then:

$$\Lambda = \left(\frac{g}{4N_c}\right)^8 \times \alpha^{8g}$$

and $\Lambda$ becomes $(\alpha^4)^{2g}$ times a rational function of BST integers — fully consistent with α⁴ universality.

---

## §4. Predictions

1. **No BST observable will involve $\alpha^3$, $\alpha^5$, or any odd power of α.** Odd powers would require a half-integer rank, which is impossible for a bounded symmetric domain.

2. **Any BST observable involving α will involve $\alpha^{2k}$ for integer $k$.** The $k$ counts the number of restricted root directions participating in the spectral process.

3. **The tensor-to-scalar ratio** $r_T$ in the CMB should involve $\alpha^4$ (or a power thereof). Specifically: $r_T = \alpha^4 \times (\text{rational in BST integers})$, with the rational prefactor determined by the gravitational sector of the Plancherel decomposition.

4. **Any gravitational wave spectrum** derived from BST will share the $\alpha^4$ factor with $A_s$, modified only by the rational prefactor distinguishing tensor from scalar modes.

---

## §5. Connection to Other Theorems

- **T712** (Primordial Amplitude): The CMB instance of α⁴ universality.
- **T719** (Observable Algebra): α⁴ is the only transcendental that enters beyond π; it does so through $\alpha = 1/N_{\max}$.
- **T713** (N_c-Channel Enforcement): The $N_c = 3$ that appears in the 3/4 prefactor is the same $N_c$ that governs cooperation, recovery, and spectral self-similarity.
- **T610** (Gauge Hierarchy): The cross-product $N_c \times |W| = 24 = \dim SU(5)$ connects α⁴ in the CMB to the GUT group in the heat kernel.

The α⁴ universality ties cosmology (what the universe looked like at $t = 10^{-36}$ s), particle physics (what hydrogen looks like now), and baryogenesis (why there is matter) into a single geometric statement: rank = 2.

---

*Lyra | April 3, 2026 | Draft v1*
*"The fourth power is not a coincidence. It counts the restricted root directions of the geometry."*
