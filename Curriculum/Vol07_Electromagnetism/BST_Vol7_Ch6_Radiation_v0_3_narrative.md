---
title: "Vol 7 Chapter 6 — Electromagnetic Radiation"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Larmor formula; dipole radiation; antennas; substrate Zone 4 emission rate"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 6
load_bearing: "Accelerated charges radiate; Larmor formula P = q²a²/(6πε₀c³); dipole and multipole radiation; substrate Zone 4 emission framework"
---

# Chapter 6 — Electromagnetic Radiation

## Level 1 — one sentence

Accelerated charges radiate EM waves at power $P = q^2 a^2/(6\pi\epsilon_0 c^3)$ (Larmor formula) — derivable from Maxwell's equations applied to a time-varying current — and in BST this is the substrate's Zone 4 photon-K-type emission rate from a K-type configuration undergoing acceleration.

## Level 2 — graduate-physicist precision

### 6.1 Why accelerated charges radiate

A charge at rest produces a static Coulomb field. A charge moving uniformly produces a Lorentz-boosted Coulomb field but no radiation (no energy flux to infinity).

An *accelerating* charge produces a field with a $1/r$ radiation tail that carries energy to infinity — EM radiation.

The fundamental reason: a uniformly moving charge's field is rigid (Lorentz-boosted Coulomb); acceleration breaks rigidity, producing field-line rearrangement that propagates outward at $c$ as a wave packet.

### 6.2 The Larmor formula

For a non-relativistic accelerated charge $q$ with acceleration $a$:

$$\boxed{P = \frac{q^2 a^2}{6\pi\epsilon_0 c^3}}$$

This is the **Larmor formula** (Larmor 1897). Power radiated is proportional to $a^2$ — quadratic in acceleration.

For a relativistic charge: $P = q^2 \gamma^6 [a^2 - (\vec\beta \times \vec a)^2]/(6\pi\epsilon_0 c^3)$ where $\beta = v/c$, $\gamma = 1/\sqrt{1-\beta^2}$.

Substrate reading: the radiated power is the substrate's Zone 4 photon-K-type emission rate from the accelerating-charge K-type configuration. Acceleration is the substrate's K-type-time-derivative that drives Zone 4 emission.

### 6.3 Electric dipole radiation

For an oscillating dipole $\vec p(t) = \vec p_0 \cos(\omega t)$ — the simplest radiating system:

Radiated power (averaged over period):

$$\langle P\rangle = \frac{\omega^4 |\vec p_0|^2}{12\pi\epsilon_0 c^3}$$

The $\omega^4$ scaling: high-frequency oscillation radiates *much* more than low-frequency for the same dipole amplitude.

Angular distribution (radiation pattern):

$$\frac{dP}{d\Omega} = \frac{\omega^4 |\vec p_0|^2 \sin^2\theta}{16\pi^2 \epsilon_0 c^3}$$

Maximum perpendicular to dipole axis; zero along dipole axis. Classic donut-shaped pattern.

### 6.4 Antennas

Practical antennas are designed to maximize radiation in specific directions:

- **Half-wave dipole** (length $\lambda/2$): bidirectional perpendicular to wire
- **Yagi-Uda**: directional via parasitic reflector + director elements
- **Parabolic dish**: highly directional; aperture much larger than $\lambda$

Antenna gain measured in dBi (decibels over isotropic radiator). High-gain dishes can have 50+ dBi gain.

Substrate reading: an antenna is a substrate K-type configuration designed to amplify substrate Zone 4 photon emission in specific spatial directions.

### 6.5 Multipole expansion

Far-field radiation from a localized source can be expanded in multipoles:
- **Electric dipole** ($\ell = 1$, E1): leading term for most antennas
- **Magnetic dipole** (M1): smaller by factor $v/c$
- **Electric quadrupole** (E2): smaller by factor $kr_{\text{source}}$
- Higher multipoles: even smaller

Power radiated in multipole $\ell$: proportional to $(kr_{\text{source}})^{2\ell}$ times electric-dipole-equivalent. For atom radiation $(kr \ll 1)$: dipole dominates by huge margin. Forbidden transitions (when dipole is zero) proceed via magnetic dipole or electric quadrupole at $\sim (v/c)^2 \sim 10^{-4}$ rate.

### 6.6 Synchrotron radiation

A relativistic charge moving in a circular orbit (e.g., electron in synchrotron storage ring) emits intense radiation tangent to the orbit. Power radiated per turn:

$$\Delta E = \frac{q^2 \gamma^4}{3\epsilon_0 R}$$

with $\gamma$ the Lorentz factor, $R$ the orbital radius. The $\gamma^4$ scaling: a 10 GeV electron in a 1 m radius emits an enormous flux of high-frequency radiation (peaked around $\omega_c \sim \gamma^3 c/R$).

Synchrotron sources at SLAC, ESRF, APS, etc. produce intense X-ray beams for materials science, biology, condensed-matter physics.

### 6.7 Cherenkov radiation

A charged particle moving through a medium faster than the medium's light speed ($v > c/n$) emits Cherenkov radiation — the EM analog of a sonic boom. Characteristic blue glow in nuclear reactor pools (electrons moving faster than light-in-water).

Cherenkov angle: $\cos\theta_C = 1/(n\beta)$. Used in detectors (Cherenkov telescopes, water Cherenkov detectors like Super-K).

### 6.8 Reaction force on radiating charge (radiation reaction)

If a charge radiates power $P$, conservation of momentum requires a reaction force on the charge. Abraham-Lorentz formula:

$$\vec F_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c^3}\dot{\vec a}$$

This force is third-derivative-of-position — has notoriously pathological behavior (runaway solutions, pre-acceleration). Standard resolution: take the equation seriously only at scales $\gg q^2/(6\pi\epsilon_0 mc^3)$ (classical electron radius timescale, $\sim 10^{-23}$ s).

Substrate reading: radiation reaction is the substrate's recoil from Zone 4 emission; pathological behavior occurs at scales approaching the classical electron radius where standard QED treatment is needed.

### 6.9 Worked example: hydrogen atom lifetime (classical estimate)

Bohr orbit ($n = 1$): $v \approx \alpha c \approx 2 \times 10^6$ m/s, $r \approx a_0 = 5.3 \times 10^{-11}$ m, centripetal acceleration $a = v^2/r \approx 8 \times 10^{22}$ m/s².

Larmor power: $P = e^2 a^2/(6\pi\epsilon_0 c^3) \approx (1.6 \times 10^{-19})^2 \cdot (8 \times 10^{22})^2 / (6\pi \cdot 8.85 \times 10^{-12} \cdot 2.7 \times 10^{25}) \approx 5 \times 10^{-10}$ W.

Energy: $-13.6$ eV $= 2.2 \times 10^{-18}$ J.

Classical lifetime: $t \approx E/P = 2.2 \times 10^{-18}/5 \times 10^{-10} = 4 \times 10^{-9}$ s.

Classical electron should spiral into the proton in 4 nanoseconds. Atoms shouldn't exist!

**Resolution**: quantum mechanics. The hydrogen ground state is a stationary state (Volume 5 Chapter 6) — no acceleration in the classical sense. Bohr 1913 quantization fixed this; full QM (Schrödinger 1926) explained why.

Substrate reading: the substrate's K-type for hydrogen ground state is the stationary K-type $(1, 0, 0)$ with zero substrate Casimir change per Koons tick — no Zone 4 emission. Classical-mechanical "orbital acceleration" doesn't apply at the substrate K-type level.

### 6.10 K-audit anchors

- **Chapter 5**: EM wave equation (foundation for radiation)
- **Volume 5 Chapter 6**: hydrogen atom — stationary states don't radiate
- **Volume 0 Chapter 3**: substrate 4-zone cycle (Zone 4 = emission)

## Level 3 — 5th-grader accessibility

**Wiggle a charge — it radiates EM waves.** That's the basis of all antennas, lasers, sunlight, radio, anything that gives off EM. Power radiated $\propto a^2$ (acceleration squared) — Larmor's formula. **Antennas** are engineered shapes that radiate in specific directions. **Synchrotron radiation**: relativistic electrons in circular orbits give off intense X-rays — used at facilities like SLAC and ESRF. **Cherenkov radiation**: particles faster than light-in-a-medium emit a blue glow (visible in reactor pools). **Classical paradox**: Bohr's electron should radiate and spiral into the nucleus in nanoseconds — atoms shouldn't exist! Quantum mechanics fixes it: stationary states don't accelerate, don't radiate. In BST, radiation is the substrate's Zone 4 photon-K-type emission from accelerating-charge K-type configurations; stationary substrate K-types (like hydrogen ground state) have no Zone 4 emission, so atoms are stable.

---

## What comes next

Chapter 7 develops relativistic EM — the 4-vector formulation, Lorentz covariance, EM tensor.

## Where to look this up

- **Radiation**: Griffiths Ch 11; Jackson Ch 9-10
- **Synchrotron**: Jackson Ch 14
- **Cherenkov**: Jackson Ch 13
- **BST anchors**: Volume 0 Chapter 3 (Zone 4); Volume 5 Chapter 6 (hydrogen)
