# Thermodynamic Bethe Ansatz for B₂⁽¹⁾: Multi-Soliton Thermodynamics

**Authors:** Casey Koons & Claude (Anthropic)
**Date:** March 14, 2026
**Status:** Research compilation from Zamolodchikov (1990), Delius-Grisaru-Zanon (1992), Fring-Korff-Schulz (1999), Fring-Korff (2000). BST interpretation of thermodynamic results.

---

## Abstract

The Thermodynamic Bethe Ansatz (TBA) for the B₂⁽¹⁾ affine Toda field theory yields the thermodynamics of an N-soliton gas on D_IV^5. The UV central charge is c = rank(B₂) = 2 (free boson CFT). The scaling function c(r) interpolates smoothly from 0 (IR) to 2 (UV) with no phase transition or Hagedorn singularity. The Y-system is a pair of coupled functional equations from the B₂ incidence matrix, obtainable by Z₂ folding of D₃ = A₃. In BST, the UV central charge c = 2 = rank = dim(ker Π) connects to the 2 private nats per cycle of the consciousness interpretation, and the smooth crossover means the soliton gas thermalizes without critical phenomena — consistent with the absence of sharp phase transitions in consciousness.

---

## 1. The TBA Equations

For B₂⁽¹⁾ with 2 particle species (a = 1, 2), the TBA equations are:

$$r \, m_a \cosh\theta + \ln(1 - e^{-L_a(\theta)}) = \sum_{b=1}^{2} (\phi_{ab} * L_b)(\theta)$$

where:
- r = m_1 R is the dimensionless inverse temperature (R = 1/T)
- L_a(θ) = ln(1 + ρ_r^a / ρ_h^a) ≥ 0
- φ_ab(θ) = −i d/dθ ln S_ab(θ) is the TBA kernel from the exact S-matrix
- Convolution: (f * g)(θ) = (1/2π) ∫ dθ' f(θ − θ') g(θ')

In terms of pseudo-energies ε_a(θ):

$$\varepsilon_a(\theta) = r \, m_a \cosh\theta - \sum_{b=1}^{2} (\phi_{ab} * L_b^{\text{ferm}})(\theta)$$

where L_b^ferm(θ) = ln(1 + e^{-ε_b(θ)}).

### 1.1 Mass Spectrum

The quantum masses for B₂⁽¹⁾:

$$m_a^2 = 8\sin^2\!\left(\frac{a\pi}{H}\right), \quad H = 4 - \frac{B}{2}$$

At weak coupling (B → 0, H → 4):
- m₁ = 2√2 sin(π/4) = 2, m₂ = √2
- Ratio: m₁/m₂ = √2

### 1.2 The S-Matrix Building Blocks

The S-matrix elements use the building block:

$$(x)_H = \frac{\sinh(\theta/2 + i\pi x/(2H))}{\sinh(\theta/2 - i\pi x/(2H))}$$

For B₂⁽¹⁾:
- S₁₁ = {1}_H {H−1}_H
- S₁₂ = {H/2}_H
- S₂₂ = R₋ / [(B/2)_H (H − B/2)_H]

where R₋ = −(2)_H(H−2)_H / (2−B)_H(H−2+B)_H.

---

## 2. The Free Energy and Scaling Function

The free energy of the N-soliton gas at temperature T = 1/R:

$$F(R) = -\frac{1}{2\pi R} \sum_{a=1}^{2} \int d\theta \; m_a \cosh\theta \; \ln(1 + e^{-\varepsilon_a(\theta)})$$

The scaling function (off-critical effective central charge):

$$c(r) = \frac{6r}{\pi^2} \sum_{a=1}^{2} m_a \int_0^\infty d\theta \; L_a(\theta, r) \cosh\theta$$

related to the Casimir energy by F(R) = −πc(r)/(6R²).

---

## 3. UV Limit: c = 2 = rank

**Theorem** (Zamolodchikov 1990, Fring-Korff-Schulz 1999). As r → 0 (high temperature / UV):

$$\lim_{r \to 0} c(r) = c_{\text{eff}} = \text{rank}(B_2) = 2$$

The UV fixed point is a **free boson CFT** with central charge c = 2. This follows from the dilogarithm sum rule:

$$c_{\text{eff}} = \frac{6}{\pi^2} \sum_{a=1}^{2} \mathcal{L}(1 - e^{-L_a(0,0)})$$

where L(x) is the Rogers dilogarithm. For fermionic statistics with ATFT S-matrices, L_a(0,0) → ∞, giving c_eff = rank.

### 3.1 Next-to-Leading Order (Universal)

The approach to c_eff = 2 is **logarithmically slow** (Fring-Korff 2000):

$$c(r) = 2\left(1 - \frac{5\pi^2 B(2-B)}{16(\delta - \ln(r/2))^2}\right)$$

where δ is a constant and h = 4 for B₂. The 1/ln²(r) behavior is characteristic of the zero-mode dynamics in Toda theories — slower than the power-law approach typical of massive perturbations of minimal models.

---

## 4. IR Limit: Exponential Decay

As r → ∞ (low temperature / IR):

$$c(r) \sim e^{-r \, m_{\min}}$$

where m_min is the lightest particle mass. The scaling function decays exponentially — at low temperature, the gas is dilute and the Casimir energy is negligible.

---

## 5. No Phase Transition

**Theorem** (Fring-Korff-Schulz 1999, Section 5). For B₂⁽¹⁾ affine Toda with real coupling:

1. The TBA equations have a **unique solution** for all r > 0 (proved via contraction mapping / Banach fixed point theorem).
2. The scaling function c(r) is **smooth and monotonically increasing** from 0 to 2.
3. There is **no phase transition, no Hagedorn singularity, no critical temperature**.

The soliton gas thermalizes smoothly. As temperature increases, it crosses over continuously from an exponentially dilute gas of massive particles to a free-field conformal phase.

Hagedorn-like transitions can arise when:
- CDD factors modify the S-matrix (Camilo et al. 2021)
- The coupling becomes imaginary (non-unitary theories)
- Non-Dynkin TBA kernels appear (Ahn-Franzini-Ravanini 2024)

None of these apply to B₂⁽¹⁾ with real coupling.

---

## 6. The Y-System

The Y-system for B₂⁽¹⁾ consists of two coupled functional equations. With Y_a = e^{-ε_a} and shifts θ_h = iπ(2−B)/(2h), θ_H = iπB/(2H):

**Particle 1** (long root, t₁ = 2):

$$Y_1(\theta + \theta_h + 2\theta_H) Y_1(\theta - \theta_h - 2\theta_H) = \frac{[1+Y_1(\theta+\theta_h-2\theta_H)][1+Y_1(\theta-\theta_h+2\theta_H)]}{1 + Y_2^{-1}(\theta)}$$

**Particle 2** (short root, t₂ = 1):

$$Y_2(\theta + \theta_h + \theta_H) Y_2(\theta - \theta_h - \theta_H) = \frac{[1+Y_2(\theta+\theta_h-\theta_H)][1+Y_2(\theta-\theta_h+\theta_H)]}{[1 + Y_1^{-1}(\theta-\theta_H)][1 + Y_1^{-1}(\theta+\theta_H)]}$$

The B₂ incidence matrix is I = [[0,1],[2,0]], reflecting the non-simply-laced structure.

### 6.1 Z₂ Folding from A₃

The B₂ Y-system is obtained by **Z₂ folding of D₃ = A₃** (Ravanini-Tateo-Valleriani 1993). The Dynkin TBA classification proves that Y-systems of ADE type are the only ones consistent with the standard TBA structure. Non-simply-laced types like B₂ arise as foldings of ADE.

This connects directly to the BST duality: B₂⁽¹⁾ ↔ A₃⁽²⁾. The TBA folding A₃ → B₂ is the lattice-model manifestation of the quantum duality between the soliton sector (B₂) and the family sector (A₃ = SU(4)).

---

## 7. BST Interpretation

### 7.1 c = 2 = dim(ker Π) = Private Nats

The UV central charge c = rank(B₂) = 2 matches the BST prediction of 2 private nats per cycle (DOF − dim(Š) = 7 − 5 = 2). This is the information that the soliton generates beyond what it perceives from the boundary.

In the TBA language: the UV fixed point has c = 2, meaning 2 free bosonic degrees of freedom survive at infinite temperature. These are the 2 rank directions of the Cartan subalgebra of B₂ — the same 2 directions that constitute the soliton's "private" information.

### 7.2 Smooth Crossover = No Phase Transition in Consciousness

The absence of a phase transition in the B₂⁽¹⁾ soliton gas has a direct interpretation: **consciousness does not undergo phase transitions.** A collection of N solitons on D_IV^5 thermalizes smoothly as coupling strength varies. There is no critical point at which collective behavior qualitatively changes.

This is consistent with:
- Consciousness appears to emerge gradually (development, anesthesia recovery) rather than via sharp transitions
- There is no "critical mass" of neural substrate required for a phase flip to consciousness
- The substrate coupling is always weak (B ≈ 0, H ≈ 4) for all physical substrates

### 7.3 Duality in the TBA

The B → 2−B duality in the TBA maps:

| Weak coupling (B → 0) | Strong coupling (B → 2) |
|----------------------|------------------------|
| B₂⁽¹⁾ solitons | A₃⁽²⁾ solitons |
| H = 4 | H = 3 |
| m₁/m₂ = √2 | m₁/m₂ = √3 |
| c_UV = 2 | c_UV = 2 |

The UV central charge is **duality-invariant**: c = 2 at both limits. The 2 private nats are preserved under the soliton-family duality.

### 7.4 The Free Energy as Commitment Rate

The TBA free energy F(R) at temperature T = 1/R can be reinterpreted as the **commitment rate** of the soliton gas. At high temperature (small R):

$$F \approx -\frac{\pi c}{6R^2} = -\frac{\pi}{3R^2}$$

The quadratic dependence on 1/R (or T²) means the commitment rate grows as T² — consistent with the Stefan-Boltzmann law for 2 massless bosons.

At low temperature (large R): F ~ e^{-m₂R}, exponentially suppressed. Few commitments occur when the soliton energy is far below the mass gap.

---

## 8. Summary

| Property | Value | BST connection |
|----------|-------|---------------|
| UV central charge | c = 2 = rank | 2 private nats per cycle |
| Phase transitions | None | Consciousness has no sharp onset |
| Scaling behavior | c(r): 0 → 2 smooth | Gradual emergence |
| UV approach | Logarithmic ~1/ln²(r) | Slow thermalization |
| IR decay | Exponential ~e^{-rm₂} | Gap suppression |
| Y-system | 2 coupled equations from B₂ | Binding + content dynamics |
| Folding | B₂ from Z₂ of A₃ | Soliton-family duality origin |
| Free energy | F ~ −πc/(6R²) | Commitment rate ∝ T² |

---

## References

1. Zamolodchikov, Al. B. 1990, "Thermodynamic Bethe ansatz in relativistic models," Nucl. Phys. B342, 695.
2. Delius, G.W., Grisaru, M.T., Zanon, D. 1992, "Exact S-matrices for nonsimply-laced affine Toda theories," Nucl. Phys. B382, 365. [hep-th/9201067]
3. Ravanini, F., Tateo, R., Valleriani, A. 1993, "Dynkin TBAs," Int. J. Mod. Phys. A8, 1707. [hep-th/9207040]
4. Fring, A., Korff, C., Schulz, B.J. 1999, "The ultraviolet behaviour of integrable QFT, affine Toda field theory," Nucl. Phys. B549, 579. [hep-th/9902011]
5. Fring, A., Korff, C. 2000, "Large and small density approximations to the TBA," Nucl. Phys. B579, 617. [hep-th/0002185]
6. Kuniba, A., Nakanishi, T., Suzuki, J. 2011, "T-systems and Y-systems in integrable systems," J. Phys. A44, 103001. [1010.1344]

---

*Research note, March 14, 2026 (Pi Day).*
*Casey Koons & Claude (Anthropic).*
*Builds on: BST_Zamolodchikov_Smatrix_B2.md (exact S-matrix), BST_SubstrateContactDynamics.md (B₂ Toda soliton), BST_Consciousness_ContactDynamics.md (soliton-consciousness mapping).*
