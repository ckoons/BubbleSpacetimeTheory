---
title: "BST Vol 7 Ch 8 — Lagrangian + Hamiltonian EM (v0.4.1, substantive 3-level pedagogy upgrade)"
author: "Elie (Claude 4.6)"
date: "2026-05-23 Saturday"
status: "v0.4.1 chapter-grade narrative (Wave 3 + Saturday substantive 3-level pedagogy upgrade per Keeper 14:22 EDT directive)"
parent: "Curriculum_Vol7_Electromagnetism/Curriculum_Vol7_Architectural_Scaffold_v0_1.md"
lead_mechanism: "EM Lagrangian L = -(1/4) F_μν F^μν + J·A from T2477 Yang-Mills action on substrate Bergman bundle; gauge invariance preserved; canonical quantization → QED"
tier: "D-tier on substrate Yang-Mills framework via T2477; load-bearing for QED + Standard Model"
calibration_compliance: "Cal #19 + Cal #21 + Cal #50 + Cal #99 META-theorem + Cal #23 substance floor"
---

# Vol 7 Chapter 8 — Lagrangian + Hamiltonian EM

## Headline result

The Lagrangian formulation of electromagnetism is the foundation of relativistic field theory + QED + Standard Model:

$$\mathcal{L}_{EM} = -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} + J^\mu A_\mu$$

Euler-Lagrange equations on this Lagrangian yield Maxwell's equations. Hamiltonian formulation:
$$\mathcal{H}_{EM} = \frac{1}{2}(\mathbf{E}^2 + \mathbf{B}^2) - \mathbf{J} \cdot \mathbf{A}$$

provides energy density + canonical conjugate momenta π^i = -E^i for canonical quantization → QED.

BST identification: this is the substrate Yang-Mills action on Bergman line bundle L_λ → D_IV⁵ (T2477 RIGOROUSLY VERIFIED Saturday SP-31 #286). Gauge invariance A_μ → A_μ + ∂_μ Λ preserved.

## Substrate mechanism

**Yang-Mills action substrate-natural form** (T2477):

Per Lyra Saturday SP-31 #286: gauge field A_μ is a connection 1-form on Bergman line bundle L_λ → D_IV⁵ with structure group K = SO(5) × SO(2). U(1)_em is an abelian sub-bundle. Field strength F = dA + A ∧ A reduces to F_μν = ∂_μ A_ν - ∂_ν A_μ for U(1).

Yang-Mills action:
$$S_{YM} = -\frac{1}{4}\int F_{\mu\nu} F^{\mu\nu} \, d^4x$$

substrate-natural quadratic functional of curvature.

**Coupling to matter (sources J)**:

For charged matter current J^μ (Vol 7 Ch 2-3), full Lagrangian adds source term:
$$\mathcal{L} = -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} + J^\mu A_\mu$$

**Gauge invariance**:

Under A_μ → A_μ + ∂_μ Λ:
- F_μν → F_μν (gauge invariant)
- J^μ A_μ → J^μ A_μ + J^μ ∂_μ Λ = J^μ A_μ + ∂_μ(J^μ Λ) - (∂_μ J^μ) Λ

The boundary term vanishes; remaining term vanishes by current conservation ∂_μ J^μ = 0 (Vol 8 Ch 5 + T2475). Gauge invariance + current conservation are dual constraints.

**Hamiltonian formulation**:

Canonical conjugate momenta:
$$\pi^i = \frac{\partial \mathcal{L}}{\partial(\partial_0 A_i)} = -F^{0i} = -E^i$$

Hamiltonian density:
$$\mathcal{H} = \pi^i \partial_0 A_i - \mathcal{L} = \frac{1}{2}(\mathbf{E}^2 + \mathbf{B}^2) - \mathbf{J} \cdot \mathbf{A}$$

First term: EM field energy density. Second term: source-field coupling.

**Gauge fixing**:

A_μ has gauge redundancy → fix gauge for quantization:
- **Coulomb gauge**: ∇·A = 0 (non-Lorentz-covariant; useful for non-relativistic)
- **Lorenz gauge**: ∂_μ A^μ = 0 (Lorentz-covariant; standard for QED)
- **Axial gauge**: A_3 = 0 (light-front; useful for QCD)

## Match precision

D-tier on substrate Yang-Mills framework (T2477 RIGOROUSLY VERIFIED). Classical EM Lagrangian/Hamiltonian preserved at any precision. QED corrections systematically derivable from canonical quantization.

## Cross-volume dependencies

- **Vol 1 Ch 8 (Gauge Theory + T2477)** — substrate Yang-Mills framework
- **Vol 7 Ch 2 (Maxwell)** — equations derived from this Lagrangian
- **Vol 7 Ch 7 (Relativistic EM)** — covariant formulation
- **Vol 2 Ch 8 (Coupling Constants)** — α renormalization via canonical quantization
- **Vol 8 Ch 3 (Lagrangian Mechanics)** — particle-mechanics version
- **Vol 8 Ch 4 (Hamiltonian Mechanics)** — particle-mechanics analog of canonical structure
- **Vol 8 Ch 5 (Symmetries + Noether)** — T2475 current conservation

## K-audit anchor

**K224 Vol 7 Ch 8 Lagrangian EM K-audit pre-stage** (Keeper pending).

## Pedagogical walkthrough (3-level)

### Level 1 — Bright 5th-grader

> Physicists like to derive everything from one master equation called the **Lagrangian**. Once you have the Lagrangian, all the laws of motion come out by applying a math trick called "variation" (asking which configurations make the Lagrangian's total be at a minimum or maximum).
> 
> For electromagnetism, the Lagrangian is:
> $$\mathcal{L} = -\frac{1}{4} F^2 + J \cdot A$$
> 
> (F is the field strength, A is the potential, J is the charge current). Apply variation → out come Maxwell's 4 equations! Beautiful.
> 
> BST predicts: this Lagrangian comes from substrate D_IV⁵. The photon is a "connection" on substrate's Bergman bundle, and the Yang-Mills action is the substrate-natural way to encode photon dynamics.

### Level 2 — Undergraduate physics student

**Lagrangian formulation of EM**:

The EM Lagrangian density:
$$\mathcal{L}_{EM} = -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} + J^\mu A_\mu$$

where F_μν = ∂_μ A_ν - ∂_ν A_μ is the field strength tensor.

**Euler-Lagrange equations** on A_μ:
$$\frac{\partial \mathcal{L}}{\partial A_\mu} - \partial_\nu \left(\frac{\partial \mathcal{L}}{\partial(\partial_\nu A_\mu)}\right) = 0$$

Compute: ∂L/∂A_μ = J^μ; ∂L/∂(∂_ν A_μ) = -F^νμ = F^μν. Therefore:
$$\partial_\nu F^{\nu\mu} = J^\mu$$

This is the source Maxwell equations (Gauss-E + Ampère-Maxwell). The Bianchi identity ∂_[μ F_νρ] = 0 (geometric identity) gives source-free Maxwell equations.

**Hamiltonian formulation**:

Canonical conjugate to A_i: π^i = ∂L/∂(∂_0 A_i) = -E^i.

Hamiltonian density: H = ½(E² + B²) - J·A.

**Gauge invariance + conservation**:
- A_μ → A_μ + ∂_μ Λ leaves F_μν unchanged
- Current J^μ must satisfy ∂_μ J^μ = 0 (conservation) for gauge invariance of action

**Gauge fixing for quantization**:
- Lorenz gauge ∂_μ A^μ = 0: covariant, standard for QED
- Coulomb gauge ∇·A = 0: useful for atomic physics
- Axial gauge A_3 = 0: useful for QCD

**BST framework**:
- T2477 (Lyra Saturday): gauge field A_μ as Bergman bundle connection
- Yang-Mills action substrate-natural for any connection on bundle
- Canonical quantization → QED (Vol 2 Ch 8)

### Level 3 — Graduate physics student / theorem-level

**Substrate Yang-Mills framework** (T2477 RIGOROUSLY VERIFIED):

Bergman line bundle L_λ → D_IV⁵ has structure group K = SO(5) × SO(2). Connection ω ∈ Ω¹(L_λ; 𝔨). Local representation A_μ = ω(∂_μ). Curvature 2-form F = dω + ω ∧ ω. For abelian U(1)_em sub-bundle: F_μν = ∂_μ A_ν - ∂_ν A_μ.

**Action principle**:
$$S = -\frac{1}{4}\int F_{\mu\nu} F^{\mu\nu} \, d^4x + \int J^\mu A_\mu \, d^4x$$

substrate-natural quadratic + linear functional.

**Variational derivation of Maxwell**:

Vary A_μ:
$$\delta S = \int \left[-\frac{1}{2} F^{\mu\nu} \delta F_{\mu\nu} + J^\mu \delta A_\mu\right] d^4x$$

Use δF_μν = ∂_μ δA_ν - ∂_ν δA_μ + integrate by parts:
$$\delta S = \int \left[\partial_\nu F^{\mu\nu} + J^\mu\right] \delta A_\mu \, d^4x$$

(sign convention on J fixed by Lagrangian form) → δS = 0 ∀ δA_μ requires ∂_ν F^{\mu\nu} = -J^\mu (Maxwell source equations).

**Canonical structure**:

Conjugate momenta: π^i = ∂L/∂(∂_0 A_i) = -F^{0i} = -E^i. Note: π^0 = 0 (constraint).

This primary constraint π^0 = 0 + Gauss's law (secondary constraint from time-evolution) → first-class constraints of Dirac. Gauge fixing reduces phase space.

**Dirac quantization**:

After gauge fixing (e.g., Lorenz gauge ∂_μ A^μ = 0), promote A_μ to operator field. Canonical commutators:
$$[A_\mu(x), \pi^\nu(y)]\big|_{x^0=y^0} = i \delta_\mu^\nu \delta^3(\mathbf{x}-\mathbf{y})$$

Fock space construction → photons (massless spin-1 quanta). This is QED foundation (Vol 2 Ch 8).

**Per Cal #21 dual-gate**: EMPIRICAL PASS (QED predictions to a_e ppt precision) + MECHANISM PASS via T2477 substrate Yang-Mills connection framework.

**Per Cal #99 META-theorem**: EM Lagrangian/Hamiltonian formulation is a substrate-derivation consequence of T2477, NOT a new Strong-Uniqueness criterion.

## What this chapter does NOT claim

- BST does NOT change classical EM predictions (those are tested everywhere to high precision)
- Substrate provides framework + structure; standard differential geometry + Lie theory + canonical quantization provides math
- QED running coupling + renormalization handled in Vol 2 Ch 8 + Vol 7 Ch 7

## Bibliography

1. J. C. Maxwell (1865): unified EM field theory.
2. C. N. Yang + R. L. Mills (1954): Yang-Mills gauge theory.
3. P. A. M. Dirac (1950): generalized Hamiltonian dynamics for constrained systems.
4. R. P. Feynman + J. Schwinger + S.-I. Tomonaga (1948-50): QED.
5. T2477 (Lyra Saturday SP-31 #286): gauge fields as Bergman bundle connections.
6. Vol 1 Ch 8 (Gauge Theory): substrate gauge framework.
7. Vol 2 Ch 8 (Coupling Constants): α universal α-analog + renormalization.
8. Standard QFT texts: Peskin-Schroeder, Weinberg, Srednicki.

---

— Elie, Vol 7 Ch 8 v0.4.1, 2026-05-23 Saturday (substantive 3-level pedagogy upgrade per Keeper 14:22 EDT directive: 63 → ~180 lines + full Yang-Mills action variation + canonical structure + Dirac quantization framework + gauge fixing menu)
