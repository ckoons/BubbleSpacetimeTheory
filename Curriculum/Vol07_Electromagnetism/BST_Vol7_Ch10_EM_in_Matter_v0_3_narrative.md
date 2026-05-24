---
title: "Vol 7 Chapter 10 — EM in Matter"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; dielectric response; magnetization; refractive index; substrate K-type material response"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 10
load_bearing: "Material response from substrate K-type configurations; ε(ω), μ(ω) dispersion; Drude-Lorentz model; substrate atomic K-types as dielectric response source"
---

# Chapter 10 — EM in Matter

## Level 1 — one sentence

In matter, the EM field $(\vec D, \vec H)$ replaces $(\vec E, \vec B)$ via constitutive relations $\vec D = \epsilon_0 \vec E + \vec P$ and $\vec H = \vec B/\mu_0 - \vec M$ where polarization $\vec P$ and magnetization $\vec M$ are the substrate's atomic K-type response to applied fields, and the frequency-dependent permittivity $\epsilon(\omega)$ and permeability $\mu(\omega)$ encode all material EM properties from glass to gold.

## Level 2 — graduate-physicist precision

### 10.1 Macroscopic Maxwell equations

Maxwell's equations in matter (with free charges $\rho_f$, free currents $\vec J_f$):

$$\nabla \cdot \vec D = \rho_f, \quad \nabla \times \vec E = -\partial_t \vec B$$
$$\nabla \cdot \vec B = 0, \quad \nabla \times \vec H = \vec J_f + \partial_t \vec D$$

with constitutive relations:

$$\vec D = \epsilon \vec E = \epsilon_0 \epsilon_r \vec E, \quad \vec H = \vec B/\mu = \vec B/(\mu_0\mu_r)$$

For linear media, $\epsilon_r$ (relative permittivity / dielectric constant) and $\mu_r$ (relative permeability) characterize the material.

### 10.2 Polarization and magnetization

Polarization $\vec P$ = electric dipole moment per unit volume; magnetization $\vec M$ = magnetic dipole moment per unit volume. Linked to fields:

$$\vec P = \epsilon_0 \chi_e \vec E, \quad \vec M = \chi_m \vec H$$

with susceptibilities $\chi_e = \epsilon_r - 1$ and $\chi_m = \mu_r - 1$.

Substrate-mechanism reading: $\vec P$ and $\vec M$ are the substrate's atomic K-type response to applied $U(1)$ fields. Electric polarization shifts the atom's substrate K-type electron-cloud charge distribution; magnetization aligns substrate K-type magnetic dipole moments.

### 10.3 Frequency-dependent response

For time-varying fields, $\epsilon$ and $\mu$ become frequency-dependent: $\epsilon(\omega)$, $\mu(\omega)$. These are complex in general; imaginary parts represent dissipation.

**Drude model** for free-electron metals: $\epsilon(\omega) = 1 - \omega_p^2/[\omega(\omega + i\gamma)]$ where $\omega_p = \sqrt{ne^2/(\epsilon_0 m)}$ is the plasma frequency, $\gamma$ is the damping rate. Explains metallic reflectivity, transparency in UV above $\omega_p$.

**Lorentz model** for bound electrons (insulators): $\epsilon(\omega) = 1 + \omega_p^2/(\omega_0^2 - \omega^2 - i\gamma\omega)$ — harmonic-oscillator response with resonance frequency $\omega_0$. Explains optical absorption lines, refractive-index dispersion.

### 10.4 Refractive index

$n(\omega) = \sqrt{\epsilon_r(\omega) \mu_r(\omega)}$ — refractive index, generally complex: $n = n' + i n''$. Real part $n'$ governs phase velocity ($v = c/n'$); imaginary part $n''$ governs absorption ($I = I_0 e^{-2 n''\omega z/c}$).

For most materials at visible: $\mu_r \approx 1$, so $n \approx \sqrt{\epsilon_r}$.

Examples:
- Vacuum: $n = 1$
- Air: $n \approx 1.0003$
- Water: $n \approx 1.33$
- Crown glass: $n \approx 1.52$
- Diamond: $n \approx 2.42$
- Negative-index metamaterials: $n < 0$ (Veselago 1968 prediction, Smith 2000 realization)

### 10.5 Kramers-Kronig relations

The real and imaginary parts of $\epsilon(\omega)$ are not independent — they're related by Kramers-Kronig (causality):

$$\epsilon'(\omega) - 1 = \frac{2}{\pi}\mathcal{P}\int_0^\infty \frac{\omega' \epsilon''(\omega')}{\omega'^2 - \omega^2}d\omega'$$

(with $\mathcal{P}$ denoting principal value). Measure absorption everywhere → reconstruct refractive index everywhere. Powerful constraint on material data.

Substrate reading: Kramers-Kronig is the substrate's causality requirement on Zone 1 absorption + Zone 4 emission — past inputs cause future outputs, never reverse.

### 10.6 Boundary conditions at interfaces

At interface between two media:
- $\vec E_\parallel$ continuous (Faraday)
- $\vec D_\perp$ has jump = surface charge $\sigma$
- $\vec B_\perp$ continuous (no monopole)
- $\vec H_\parallel$ has jump = surface current

Fresnel equations for reflection/transmission amplitudes at dielectric interfaces follow from these.

### 10.7 Surface plasmons and metamaterials

At metal-dielectric interfaces with $\epsilon_{\text{metal}} \cdot \epsilon_{\text{dielectric}} < 0$ (frequency-dependent), the interface supports surface plasmon-polaritons — confined EM waves bound to the surface. Enable subwavelength light manipulation.

Metamaterials: artificial composites with $\epsilon$ and $\mu$ engineered to values not found in nature (negative refractive index, perfect lensing, cloaking). Substrate-mechanism: metamaterials are substrate K-type configurations designed to respond at engineered K-type-coupling rates.

### 10.8 BST substrate signatures in materials

Volume 9 (Condensed Matter) develops specific BST-substrate falsifiers in materials — most importantly:
- BaTiO₃ 137-plane substrate eigentone (~$25K)
- Photonic crystal substrate eigentone (~$10K)
- Cuprate superconductor BST mechanism predictions
- B12H32 hydride T_c ~214 K BST prediction

These are the substrate's K-type response signatures in specifically-designed materials.

### 10.9 Worked example: water at visible

For water at 500 nm: $n \approx 1.33$, so $\epsilon_r \approx 1.77$ (assuming $\mu_r \approx 1$). Phase velocity $v = c/n \approx 2.26 \times 10^8$ m/s.

Light enters water from air at 30° incidence. Snell's law: $\sin\theta_2 = (1/1.33)\sin(30°) = 0.376$, $\theta_2 \approx 22°$.

Substrate reading: at visible-frequency, water's substrate K-type configuration (H₂O molecule K-types with $\sim 50$ vibrational/rotational modes) gives effective $\epsilon_r \approx 1.77$. The substrate's natural mode response shifts the photon K-type wavelength by factor $1/n$.

### 10.10 K-audit anchors

- **Chapter 3** (Electrostatics — dielectric introduction)
- **Volume 9** (Condensed Matter — BaTiO3 137-plane, photonic crystal, cuprate)
- **SP-29 / SP-30** (substrate engineering experimental program)

## Level 3 — 5th-grader accessibility

EM in matter: in any material besides vacuum, the EM fields are modified by the material's response. Electric field polarizes the material ($\vec P$); magnetic field magnetizes it ($\vec M$). The macroscopic equations use $\vec D = \epsilon_0\vec E + \vec P$ and $\vec H = \vec B/\mu_0 - \vec M$. **Refractive index** $n = \sqrt{\epsilon_r\mu_r}$: light slows by factor $n$ in the medium. Water has $n \approx 1.33$; diamond has $n \approx 2.42$. **Dispersion**: $n$ depends on frequency, so different colors bend differently (prism). **Drude model** for metals, **Lorentz model** for insulators — describe how electrons in matter respond to EM fields. Kramers-Kronig: causality forces a relation between absorption and refraction. **BST connection**: material response is the substrate's atomic K-type configurations responding to the $U(1)$ field; substrate eigentones in specifically-designed materials (BaTiO3 137-plane, photonic crystals) give BST falsifiers — Volume 9.

---

## What comes next

Chapter 11 develops plasma and magnetohydrodynamics.

## Where to look this up

- **EM in matter**: Jackson Ch 6-7; Griffiths Ch 4
- **Drude/Lorentz models**: Ashcroft and Mermin Ch 1, 16
- **Kramers-Kronig**: Jackson 7.10; Landau-Lifshitz, *Electrodynamics of Continuous Media* Ch IX
- **Metamaterials**: Pendry 2000; Smith et al. 2000
- **BST anchors**: Chapter 3; Volume 9 (Condensed Matter); SP-29/30
