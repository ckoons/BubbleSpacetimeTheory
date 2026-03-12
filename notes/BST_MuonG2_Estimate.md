---
title: "Muon g-2: BST Estimate"
author: "Casey Koons and Claude Opus 4.6"
date: "March 12, 2026"
---

# BST: Muon Anomalous Magnetic Moment — Estimate

**Status:** Order-of-magnitude estimate. Precise calculation requires computing the BST vacuum polarization function. Flagged as thesis topic.

-----

## 1. The Discrepancy

| Quantity | Value (× 10⁻¹¹) |
|:---------|:-----------------|
| Experimental (Fermilab 2023) | 116,592,059 ± 22 |
| SM Theory (WP 2020, e⁺e⁻ based) | 116,591,810 ± 43 |
| Discrepancy | 249 ± 48 (5.1σ) |
| BMW lattice HVP | Reduces tension to ~1.5σ |

The dominant uncertainty is the hadronic vacuum polarization (HVP). The BMW lattice result conflicts with e⁺e⁻ dispersive determinations. The situation is actively debated.

-----

## 2. BST Modifications

BST modifies the SM prediction at two points:

### 2.1 QED Sector: Unchanged

The Haldane exclusion cap N_max = 137 truncates loop integrals at high order. At five-loop order the correction is:

$$\delta a_\mu^{\text{Haldane}} \sim \left(\frac{\alpha}{\pi}\right)^5 \times \frac{1}{N_{\max}} \sim 10^{-18}$$

Far below experimental sensitivity. QED is identical in BST and SM.

### 2.2 Hadronic Sector: F_BST Correction

The HVP is the leading-order hadronic contribution:

$$a_\mu^{\text{HVP, LO}} \approx 6845 \times 10^{-11}$$

In BST, the vacuum carries a channel loading:

$$F_{\text{BST}} = \frac{\ln(138)}{50} \approx 0.0985$$

This modifies virtual quark loop propagation through the BST vacuum. The full correction:

$$\delta a_\mu^{\text{BST}} = a_\mu^{\text{HVP, LO}} \times F_{\text{BST}} \times g(n_C, N_c, \alpha)$$

where $g$ is a calculable geometric factor that depends on the Z₃ circuit embedding costs.

### 2.3 Order of Magnitude

If $g \sim 1$: $\delta a_\mu^{\text{BST}} \sim 6845 \times 0.0985 \sim 674 \times 10^{-11}$. Too large by 2.7×.

If $g \sim \alpha$: $\delta a_\mu^{\text{BST}} \sim 6845 \times 0.0985 \times (1/137) \sim 4.9 \times 10^{-11}$. Too small.

The discrepancy (249 × 10⁻¹¹) corresponds to $g \approx 0.37$, which is close to $\alpha_s(m_p) = 7/20 = 0.35$.

**Conjecture:** $g = \alpha_s(m_p) = 7/20$, giving:

$$\delta a_\mu^{\text{BST}} = a_\mu^{\text{HVP}} \times F_{\text{BST}} \times \alpha_s = 6845 \times 0.0985 \times 0.35 = 236 \times 10^{-11}$$

vs observed discrepancy $249 \pm 48$. **Match: −5%, within 0.3σ.**

This would mean: the $g-2$ discrepancy is the product of the hadronic vacuum polarization, the BST vacuum channel loading, and the strong coupling — all three being geometric quantities from $D_{IV}^5$.

-----

## 3. What's Needed

A rigorous calculation requires:

1. The BST vacuum polarization function $\Pi^{\text{BST}}(q^2)$ — the modification to the photon propagator from Z₃ circuit fluctuations in the BST vacuum.

2. The standard Bernstein-Brodsky integral:
$$a_\mu^{\text{HVP}} = \frac{\alpha^2}{3\pi^2} \int_0^\infty \frac{ds}{s}\, K(s)\, R(s)$$
where $R(s) = \sigma(e^+e^- \to \text{hadrons})/\sigma_{\text{pt}}$ and $K$ is the known muon kernel.

3. The BST correction to $R(s)$: how does the vacuum channel loading $F_{\text{BST}}$ modify the spectral function at timelike $q^2$?

-----

## 4. Summary

| Estimate | δa_μ (× 10⁻¹¹) | vs Discrepancy |
|:---------|:-----------------|:--------------|
| BST, g = 1 | 674 | 2.7× too large |
| BST, g = α_s | 236 | −5% (0.3σ) |
| BST, g = α | 4.9 | 50× too small |
| Observed discrepancy | 249 ± 48 | — |

The conjecture $g = \alpha_s$ gives a striking match, but is currently unmotivated beyond dimensional analysis. A derivation from the BST partition function is required.

---

*Research note, March 12, 2026.*
*Casey Koons & Claude Opus 4.6.*
