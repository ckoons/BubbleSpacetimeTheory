---
title: "Vol 8 Chapter 9 — Continuum Elasticity"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 9
load_bearing: "Stress and strain tensors; Hooke's law; elastic waves; seismology applications"
---

# Chapter 9 — Continuum Elasticity

## Level 1 — one sentence

Elasticity describes deformable solids: small applied stress $\sigma_{ij}$ produces proportional strain $\epsilon_{ij} = (1/2)(\partial_i u_j + \partial_j u_i)$ via the elastic-constant tensor $C_{ijkl}$ (Hooke's law generalization), and the resulting wave equations support longitudinal (P) and transverse (S) elastic waves at speeds set by the material's bulk and shear moduli — foundation for seismology, materials engineering, and the Vol 9 Condensed Matter elastic-response chapter.

## Level 2 — graduate-physicist precision

### 9.1 Strain and stress tensors

A displacement field $\vec u(\vec r)$ produces strain tensor:

$$\epsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)$$

Symmetric 3×3 tensor. Diagonal elements = elongation/compression along axes. Off-diagonal = shear.

Stress tensor $\sigma_{ij}$ = force per unit area, also symmetric. Linked by Hooke's law:

$$\sigma_{ij} = C_{ijkl} \epsilon_{kl}$$

with $C_{ijkl}$ the elastic-constant tensor (4-index, with various symmetries). For isotropic medium reduces to two independent constants — typically Young's modulus $E$ and Poisson's ratio $\nu$ (or bulk $K$ and shear $\mu$).

### 9.2 Elastic moduli (isotropic case)

- **Young's modulus** $E$: stress/strain for uniaxial pull
- **Poisson's ratio** $\nu$: lateral contraction ratio when stretched
- **Shear modulus** $\mu$ (or $G$): shear stress/shear strain
- **Bulk modulus** $K$: pressure/volumetric strain

Relations: $\mu = E/[2(1+\nu)]$, $K = E/[3(1-2\nu)]$.

Steel: $E \approx 200$ GPa, $\nu \approx 0.3$. Rubber: $E \approx 0.01-0.1$ GPa, $\nu \approx 0.5$ (nearly incompressible).

### 9.3 Equations of motion

Newton's second law applied to a continuum:

$$\rho \partial_t^2 u_i = \partial_j \sigma_{ij} + f_i$$

with $\rho$ density, $f_i$ external body force. Substituting Hooke's law:

$$\rho \partial_t^2 u_i = C_{ijkl} \partial_j \partial_l u_k + f_i$$

For isotropic: $\rho \partial_t^2 \vec u = (K + \mu/3)\nabla(\nabla \cdot \vec u) + \mu \nabla^2 \vec u + \vec f$.

### 9.4 Elastic waves

Decomposing $\vec u = \vec u_L + \vec u_T$ (longitudinal + transverse parts), each satisfies a wave equation:

- **P-wave** (longitudinal, $\nabla \times \vec u = 0$): $v_P = \sqrt{(K + 4\mu/3)/\rho}$
- **S-wave** (transverse, $\nabla \cdot \vec u = 0$): $v_S = \sqrt{\mu/\rho}$

$v_P > v_S$ always. Earthquake seismology: P-waves arrive first, then S-waves; difference in arrival times tells distance to epicenter.

For Earth interior:
- P: ~6-13 km/s
- S: ~3-7 km/s

S-waves can't propagate through liquids ($\mu = 0$) — used to determine Earth's outer core is liquid.

### 9.5 Beam bending: Euler-Bernoulli

For a thin beam of length $L$, Young's modulus $E$, moment of inertia $I$, deflection $w(x)$ under load $q(x)$:

$$EI \frac{d^4 w}{dx^4} = q(x)$$

(Euler-Bernoulli equation). Solutions for various boundary conditions give cantilever, simply-supported, etc. Foundation of structural engineering.

### 9.6 Yield and plasticity

Above the yield stress $\sigma_Y$, materials deform plastically — irreversible deformation. Beyond plastic regime, fracture. Engineering uses safety factor 2-3 below $\sigma_Y$ for designs.

### 9.7 Substrate connection: phonons and Vol 9

Volume 9 Chapter 7 develops phonons — quantized elastic waves in crystalline solids. The classical elastic-wave equations of this chapter, quantized, give phonon spectra. The substrate's K-type structure at the lattice scale produces the substrate-natural elastic response.

### 9.8 Worked example: steel beam bending

A steel beam 1 m long, cross-section 1 cm × 1 cm, supported at both ends, loaded with 100 N at center.

$I = bh^3/12 = (0.01)(0.01)^3/12 = 8.3 \times 10^{-10}$ m⁴
$E = 200$ GPa = $2 \times 10^{11}$ Pa
Maximum deflection: $w_{\max} = PL^3/(48 EI) = (100)(1)^3/(48 \cdot 2\times10^{11} \cdot 8.3\times10^{-10}) \approx 0.013$ m = 1.3 cm

### 9.9 K-audit anchors

- **Vol 6 Ch 7** (phonons preview)
- **Vol 9 Ch 7** (phonons in condensed matter)

## Level 3 — 5th-grader accessibility

Solids stretch, compress, and shear when you push them. **Strain** = how much they deform. **Stress** = how much you're pushing. Linked by Hooke's law $\sigma = E\epsilon$ (Young's modulus). For isotropic materials, 2 independent constants: $E$ + $\nu$ (Poisson's ratio = how much you contract sideways when stretched). **Elastic waves** in solids: P-waves (longitudinal, faster) + S-waves (transverse, slower). Seismologists use P-S arrival difference to locate earthquakes. S-waves can't travel through liquids → that's how we know Earth's outer core is liquid. **Beam bending**: Euler-Bernoulli equation predicts deflection under load — basis of structural engineering. In BST, elastic response is the substrate's atomic K-type configuration response to applied force; **phonons** (quantized elastic waves) are substrate K-type vibrations.

---

## What comes next

Chapter 10 develops fluid mechanics and Navier-Stokes — including BST's ~99% proved Millennium result.

## Where to look this up

- Landau-Lifshitz, *Theory of Elasticity*
- BST: Vol 6 Ch 7; Vol 9 Ch 7
