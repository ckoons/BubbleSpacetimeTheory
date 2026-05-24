---
title: "Vol 7 Chapter 9 — Multipole Expansion and Scattering"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; multipole expansion of fields and radiation; Thomson, Rayleigh, Mie scattering"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 9
load_bearing: "Multipole expansion as substrate K-type angular decomposition; scattering cross sections; substrate Zone 1 absorption + Zone 4 emission framework for scattering events"
---

# Chapter 9 — Multipole Expansion and Scattering

## Level 1 — one sentence

Multipole expansion decomposes a localized charge/current distribution into spherical-harmonic components (monopole, dipole, quadrupole, ...), giving systematic asymptotic expansions of fields and radiation — and scattering cross sections (Thomson, Rayleigh, Mie) characterize how EM radiation interacts with material targets, all derivable from Maxwell's equations and providing key BST falsifiers in materials measurements.

## Level 2 — graduate-physicist precision

### 9.1 Multipole expansion of the potential

For a localized charge distribution $\rho(\vec r')$ in finite region (size $a$), the potential at distance $r \gg a$ admits the expansion:

$$\phi(\vec r) = \frac{1}{4\pi\epsilon_0}\left[\frac{Q}{r} + \frac{\vec p \cdot \hat r}{r^2} + \frac{Q_{ij}\hat r^i \hat r^j}{2 r^3} + \cdots\right]$$

with:
- **Monopole**: $Q = \int \rho \, d^3 r$
- **Dipole**: $\vec p = \int \vec r \rho \, d^3 r$
- **Quadrupole**: $Q_{ij} = \int (3 r_i r_j - r^2 \delta_{ij})\rho \, d^3 r$

Each term falls off faster than the previous by factor $a/r$. For neutral system ($Q = 0$), dipole leads. For symmetric distributions ($\vec p = 0$), quadrupole leads. Etc.

Substrate-mechanism reading: multipole expansion is the substrate's natural K-type spherical-harmonic decomposition of the source K-type cluster.

### 9.2 Radiation multipoles

For radiation from oscillating sources (Chapter 6), similar expansion:
- **E1 (electric dipole)**: $\omega^4 |\vec p|^2$ power; standard antenna leading order
- **M1 (magnetic dipole)**: $\omega^4 |\vec m|^2 / c^2$; smaller by $(v/c)^2 \sim 10^{-4}$ in atoms
- **E2 (electric quadrupole)**: $\omega^6 |Q|^2 / c^2$; smaller by $(kr_{\text{source}})^2$

Selection rules in atomic transitions:
- E1 allowed: $\Delta \ell = \pm 1$, $\Delta m = 0, \pm 1$
- M1, E2 allowed for $\Delta \ell = 0$ or $\pm 2$ (forbidden E1 transitions proceed via these channels at much slower rates)

### 9.3 Thomson scattering

Low-energy elastic scattering of light by free electrons. Classical derivation: incident wave accelerates electron at $a = eE/m_e$; Larmor radiation gives scattered power; cross section:

$$\sigma_T = \frac{8\pi}{3}r_e^2 = \frac{8\pi}{3}\left(\frac{e^2}{4\pi\epsilon_0 m_e c^2}\right)^2 \approx 6.65 \times 10^{-29}\text{ m}^2$$

with $r_e \approx 2.82 \times 10^{-15}$ m the classical electron radius. Independent of photon frequency (in low-energy limit $\hbar\omega \ll m_e c^2$).

Substrate reading: Thomson scattering is a substrate Zone 1 photon-K-type absorption + Zone 4 photon-K-type re-emission by an electron K-type, in the low-energy limit where the electron K-type configuration doesn't change.

### 9.4 Compton scattering

High-energy regime ($\hbar\omega \gtrsim m_e c^2$): photon energy comparable to or exceeding electron rest energy. Wavelength shift:

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta)$$

with $\theta$ the scattering angle. The Compton wavelength $h/(m_e c) \approx 2.43 \times 10^{-12}$ m.

Substrate reading: at Compton-scale energies, the photon-electron K-type interaction is not just absorption-emission of a single K-type; the substrate must rearrange K-types between photon and electron, producing the wavelength shift.

### 9.5 Rayleigh scattering

Elastic scattering of long-wavelength light by polarizable particles small compared to $\lambda$. Cross section:

$$\sigma_R \propto \frac{1}{\lambda^4}$$

The $1/\lambda^4$ scaling: blue light (short $\lambda$) scatters much more than red light. This explains:
- Blue sky (atmospheric Rayleigh scattering by air molecules)
- Red sunset (blue scattered out, red transmitted)

For atmospheric N₂ at visible wavelengths: $\sigma_R \sim 5 \times 10^{-30}$ m² at 500 nm.

### 9.6 Mie scattering

When particles are comparable to or larger than wavelength: exact solution due to Mie 1908. Cross sections have rich resonance structure (whispering-gallery modes, surface plasmons, etc.).

Examples:
- Cloud droplets (μm) at visible: Mie regime; white clouds because cross sections are roughly wavelength-independent
- Aerosols, smog: various Mie regimes

### 9.7 Compton-edge and BST substrate signatures

Standard QED predicts the Compton edge (maximum scattered electron energy) at $E_{\max} = 2 E_\gamma^2/(m_e c^2 + 2 E_\gamma)$. Tested to high precision.

BST-substrate predictions for fine-structure corrections to scattering cross sections at high precision are open research; SP-29 substrate engineering program may identify substrate eigentone signatures.

### 9.8 Worked example: Earth-atmosphere blue sky

The atmospheric Rayleigh cross section per molecule: $\sigma_R \approx 5 \times 10^{-30}$ m² at 500 nm. Atmospheric number density at sea level: $n \approx 2.5 \times 10^{25}$ /m³. Mean free path for scattering: $\ell = 1/(n\sigma) \approx 8 \times 10^3$ m = 8 km — much shorter than atmospheric depth (~10 km). So light traveling sideways through the atmosphere is heavily scattered; we see scattered (blue) light from all directions of sky.

$1/\lambda^4$ ratio: $(700/400)^4 \approx 9.4$. Blue scatters 9× more than red. That's why the sky is blue, sunsets are red.

### 9.9 K-audit anchors

- **Chapter 6**: radiation foundation (Larmor)
- **Volume 5 Chapter 3**: spherical harmonics + angular momentum (multipole foundation)
- **SP-29** (substrate engineering): potential cross-section substrate signatures

## Level 3 — 5th-grader accessibility

**Multipole expansion**: any localized charge distribution looks like a point charge (monopole) far away, with corrections. The corrections are dipole ($1/r^2$ fall-off), quadrupole ($1/r^3$), etc. — each smaller term. Useful for asymptotic behavior. **Scattering** is how light bounces off stuff:
- **Thomson**: light + free electron, low energy; $\sigma_T \approx 6.65 \times 10^{-29}$ m²
- **Compton**: same but high energy; wavelength shifts by Compton's formula
- **Rayleigh**: light + small molecules; $\sigma \propto 1/\lambda^4$ — that's why the sky is blue (blue scatters more than red)
- **Mie**: light + particles comparable to $\lambda$; rich resonance structure (cloud droplets, etc.)

In BST, scattering is the substrate's Zone 1 photon absorption + Zone 4 photon re-emission by the target K-type configuration. Different scattering regimes correspond to different K-type interaction strengths.

---

## What comes next

Chapter 10 develops EM in matter — dielectrics, magnetic materials, refractive index.

## Where to look this up

- **Multipole expansion**: Jackson Ch 4, 9, 16
- **Scattering**: Born and Wolf, *Principles of Optics*; van de Hulst, *Light Scattering by Small Particles*
- **BST anchors**: Chapter 6 (radiation); SP-29 (substrate engineering)
