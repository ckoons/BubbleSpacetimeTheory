---
title: "Vol 7 Chapter 5 — Electromagnetic Waves"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; EM waves as photon K-type wave packets; speed of light c from substrate"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 5
load_bearing: "EM waves = substrate photon K-type wave packets; c = 1/√(μ₀ε₀) is substrate's natural light speed; transverse polarization from Pin(2) integer-weight K-type"
---

# Chapter 5 — Electromagnetic Waves

## Level 1 — one sentence

Electromagnetic waves — radio, microwave, infrared, visible light, UV, X-ray, gamma — are propagating wave-packet solutions of the source-free Maxwell equations with speed $c = 1/\sqrt{\mu_0\epsilon_0}$, and in BST they are substrate photon K-type wave packets traveling at the substrate's natural massless-K-type group velocity (the speed of light).

## Level 2 — graduate-physicist precision

### 5.1 The EM wave equation

In vacuum ($\rho = 0$, $\vec J = 0$): taking $\nabla \times$ of Faraday and using Ampère-Maxwell (Chapter 2 Section 2.8):

$$\nabla^2 \vec E - \frac{1}{c^2}\partial_t^2 \vec E = 0$$

$$\nabla^2 \vec B - \frac{1}{c^2}\partial_t^2 \vec B = 0$$

with $c^2 = 1/(\mu_0\epsilon_0)$. Both fields satisfy the wave equation; both propagate at speed $c$.

Plane wave solution: $\vec E = \vec E_0 \cos(\vec k \cdot \vec r - \omega t)$ with dispersion $\omega = c k$.

For Maxwell's equations to be satisfied: $\vec k \cdot \vec E_0 = 0$ (transverse), $\vec B = \hat k \times \vec E / c$ (perpendicular to $\vec E$ and $\vec k$, with $|\vec B| = |\vec E|/c$).

### 5.2 Substrate-mechanism reading: photon K-type wave packets

In BST: EM waves are substrate photon K-type wave packets. The photon is a Pin(2) integer-weight massless K-type (Volume 5 Chapter 3, Vol 7 Chapter 1). Massless = zero substrate Casimir on this K-type sector = lightlike dispersion $\omega = c k$.

Two transverse polarizations correspond to Pin(2) weights $\pm 1$ (helicity). Longitudinal polarization is gauge-equivalent to zero (no physical content).

### 5.3 The electromagnetic spectrum

| Region | Wavelength | Frequency | Typical sources |
|---|---|---|---|
| Radio | > 10 cm | < 3 GHz | Antennas, AM/FM |
| Microwave | 1 mm − 10 cm | 3 − 300 GHz | Magnetrons, radar |
| Infrared | 700 nm − 1 mm | 0.3 − 430 THz | Thermal emission |
| Visible | 380 − 700 nm | 430 − 790 THz | LEDs, sun |
| UV | 10 − 380 nm | 0.79 − 30 PHz | Sun, UV lamps |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Bremsstrahlung |
| Gamma | < 0.01 nm | > 30 EHz | Nuclear decay |

All have the same speed $c \approx 3 \times 10^8$ m/s in vacuum; differ only in frequency / wavelength.

Substrate reading: the entire EM spectrum is the substrate's photon K-type wave packet spectrum, from very-low-frequency (large wavelength, low energy per photon) to very-high-frequency (small wavelength, high energy per photon). Same K-type, different excitation level.

### 5.4 Energy and momentum

EM energy density: $u = (\epsilon_0/2) E^2 + (1/(2\mu_0)) B^2 = \epsilon_0 E^2$ (for waves where $E$ and $B$ contribute equally).

EM momentum density: $\vec p = \vec S / c^2$ where $\vec S = \vec E \times \vec B/\mu_0$ is the **Poynting vector** (energy flux).

For a wave with field amplitude $E_0$: average intensity $\langle S\rangle = (1/2)c\epsilon_0 E_0^2$.

Photon energy: $E_\gamma = \hbar\omega$. Photon momentum: $p_\gamma = \hbar k = E_\gamma/c$. (Massless particle has $E = pc$.)

### 5.5 Polarization

A plane wave has two independent transverse polarizations. Common bases:
- **Linear**: $\hat x$ and $\hat y$ (for wave traveling along $\hat z$)
- **Circular**: right-handed ($\hat R = (\hat x + i\hat y)/\sqrt 2$) and left-handed ($\hat L$)
- **Elliptical**: superposition of linear with phase difference

Polarized waves carry angular momentum: each circular photon carries $\pm \hbar$ along $\hat k$.

Substrate reading: linear polarization = substrate K-type with definite SO(2) phase axis; circular = substrate K-type with definite Pin(2) weight $\pm 1$.

### 5.6 Reflection and refraction at an interface

Snell's law: $n_1 \sin\theta_1 = n_2 \sin\theta_2$, with $n = c/v_{\text{medium}}$ the refractive index.

Fresnel equations give the reflection and transmission amplitudes for waves at an interface; depend on polarization (s and p — perpendicular and parallel to plane of incidence).

Brewster's angle $\theta_B = \arctan(n_2/n_1)$: at this angle, p-polarized light is fully transmitted (no reflection). Used in polarizers and lasers.

### 5.7 Waves in dielectric media

In a linear dielectric with refractive index $n$:
- Speed: $v = c/n$
- Wavelength: $\lambda = \lambda_0/n$
- Frequency: unchanged (same source)
- $\vec E$, $\vec B$ amplitudes change by factor $1/\sqrt{\epsilon_r}$

Dispersion: $n$ depends on $\omega$ → different frequencies travel at different speeds → prism splits light, optical fiber pulse broadening.

### 5.8 Worked example: visible light wavelength

Yellow-green light (peak of human eye sensitivity): $\lambda \approx 550$ nm, $\nu \approx 5.5 \times 10^{14}$ Hz.

Photon energy: $E_\gamma = h\nu = (6.63 \times 10^{-34})(5.5 \times 10^{14}) \approx 3.6 \times 10^{-19}$ J = 2.25 eV.

For 1 W of yellow-green light (sun-equivalent for ~few cm²): photon flux $= 1 / 3.6 \times 10^{-19} \approx 2.8 \times 10^{18}$ photons/sec.

Substrate reading: every second, about $3 \times 10^{18}$ photon K-types are emitted at this frequency for a 1-W source. The substrate emits these at the Koons-tick rate from the substrate K-type configuration of the emitter atoms.

### 5.9 The constancy of c

Einstein's 1905 postulate: the speed of light is the same in all inertial frames. This is the foundation of special relativity. EM waves don't have a "medium" — they're pure field excitations that propagate at $c$ regardless of source or observer motion.

Substrate reading: $c$ is the substrate's natural massless-K-type group velocity. The substrate's K-type framework is intrinsically Lorentz-covariant via the $SO_0(4,2) \subset SO_0(5,2)$ subgroup (Volume 7 Chapter 7). The constancy of $c$ is the substrate's symmetry, not a separate postulate.

### 5.10 K-audit anchors

- **Chapter 2**: Maxwell from substrate U(1) (foundation)
- **Volume 5 Chapter 3**: photon = Pin(2) integer-weight K-type
- **Volume 7 Chapter 7**: relativistic EM and SO(4,2) ⊂ SO(5,2)

## Level 3 — 5th-grader accessibility

EM waves are how electricity and magnetism *move*. Radio, microwave, light, X-ray, gamma — all the same thing at different frequencies. All travel at speed $c \approx 3 \times 10^8$ m/s in vacuum. **Wavelength × frequency = c**. **Photon energy** = $h\nu$ (Planck): radio photons have very little energy, gamma photons have lots. Wave behavior at interfaces: Snell's law for refraction, Fresnel for reflection, Brewster's angle for polarized transmission. In BST, EM waves are substrate photon K-type wave packets — same K-type for the entire spectrum, just different excitation levels. The speed $c$ is the substrate's natural massless-K-type group velocity; it's the same everywhere because it's a substrate property, not a medium property.

---

## What comes next

Chapter 6 develops EM radiation — how accelerated charges emit electromagnetic waves.

## Where to look this up

- **EM waves**: Griffiths Ch 9; Jackson Ch 7-8
- **Polarization**: Born and Wolf, *Principles of Optics*
- **Fresnel equations**: Jackson Ch 7
- **BST anchors**: Chapter 2 Maxwell; Volume 5 Chapter 3 photon K-type
