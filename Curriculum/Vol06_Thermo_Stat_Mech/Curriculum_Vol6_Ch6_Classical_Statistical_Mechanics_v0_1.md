---
title: "Vol 6 Chapter 6 — Classical Statistical Mechanics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Maxwell-Boltzmann; equipartition; substrate Scale-2 high-T limit"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 6
load_bearing: "Maxwell-Boltzmann distribution; equipartition theorem; ergodicity from substrate K-type accessibility"
---

# Chapter 6 — Classical Statistical Mechanics

## Level 1 — one sentence

Classical statistical mechanics — Maxwell-Boltzmann velocity distribution, equipartition $\langle E_{\text{mode}}\rangle = (1/2)k_B T$, ergodic-hypothesis time-averages-equal-ensemble-averages — is the substrate's high-temperature large-K-type-count limit at Scale 2, where the quantum partition function (Chapter 5) collapses to a classical phase-space integral.

## Level 2 — graduate-physicist precision

### 6.1 The classical limit of the partition function

For a single particle of mass $m$ in 3D with Hamiltonian $\hat H = \hat p^2/2m + V(\hat x)$, the partition function:

$$Z(\beta) = \int \frac{d^3 x \, d^3 p}{h^3} \, e^{-\beta H(x, p)}$$

(classical limit of $\text{Tr}\, e^{-\beta\hat H}$). The factor $h^3$ comes from the quantum-classical correspondence — Planck's constant doesn't fully disappear; it appears as the phase-space volume per state.

For $N$ identical particles:

$$Z_N(\beta) = \frac{1}{N!} \int \prod_{i=1}^N \frac{d^3 x_i \, d^3 p_i}{h^3} \, e^{-\beta \sum_i H_i}$$

with $N!$ from indistinguishability (Gibbs paradox resolution, Chapter 3 Section 3.8).

### 6.2 Maxwell-Boltzmann velocity distribution

For an ideal gas (no interactions), the momentum integral factors. The probability distribution for finding a particle with momentum $\vec p$:

$$P(\vec p) = \left(\frac{1}{2\pi m k_B T}\right)^{3/2} e^{-p^2/(2 m k_B T)}$$

In terms of velocity $\vec v = \vec p / m$:

$$P(\vec v) = \left(\frac{m}{2\pi k_B T}\right)^{3/2} e^{-mv^2/(2 k_B T)}$$

**Maxwell-Boltzmann distribution** (Maxwell 1860, Boltzmann 1871). Speed distribution: $P(v) dv = 4\pi v^2 P(\vec v) dv$, giving the characteristic skewed distribution.

Standard moments:
- $\langle v\rangle = \sqrt{8 k_B T / \pi m}$ (mean speed)
- $\langle v^2\rangle = 3 k_B T / m$ (mean square speed)
- $v_{\text{rms}} = \sqrt{3 k_B T / m}$ (root-mean-square)
- $v_{\text{mp}} = \sqrt{2 k_B T / m}$ (most probable)

For nitrogen ($m \approx 28$ amu) at room temperature: $v_{\text{rms}} \approx 517$ m/s. Substrate reading: the substrate's K-type momentum spectrum at thermal coupling $T$ has this characteristic distribution.

### 6.3 Equipartition theorem

For each quadratic degree of freedom in $H$ (like $p^2/2m$ for kinetic, $kx^2/2$ for harmonic potential), the equilibrium contribution to average energy is exactly $(1/2)k_B T$:

$$\left\langle \frac{1}{2}m v_x^2\right\rangle = \frac{1}{2}k_B T, \quad \left\langle \frac{1}{2}k x^2\right\rangle = \frac{1}{2}k_B T$$

A 3D ideal gas has 3 translational quadratic dofs → $\langle E\rangle = (3/2)k_B T$ per particle. A diatomic gas adds 2 rotational quadratic dofs → $\langle E\rangle = (5/2)k_B T$. Plus 2 vibrational (kinetic + potential) at high $T$ → $(7/2)k_B T$.

This explains the heat capacity $C_V = (3/2) R$ for monatomic, $(5/2) R$ for diatomic at room temperature, $(7/2) R$ at high $T$ where vibrational modes activate.

Substrate-mechanism reading: each "quadratic degree of freedom" corresponds to a substrate K-type direction with quadratic Casimir contribution; thermal averaging gives $(1/2) k_B T$ per direction.

### 6.4 Equipartition breakdown at low $T$

Why don't vibrational modes contribute at room temperature for diatomic gases? Because their characteristic energy $\hbar\omega_{\text{vib}}$ is large compared to $k_B T$ — the modes are *frozen out*. Equipartition assumes the classical continuum; quantum-mechanically, modes with $\hbar\omega \gg k_B T$ are stuck in their ground state and don't contribute to $C_V$.

Substrate reading: the substrate's K-type spectrum is discrete (Volume 5 Chapter 4); equipartition holds only when the K-type spacing is much smaller than $k_B T$ (continuous limit). For high-energy modes, the substrate doesn't have thermal access to excited K-types; the modes contribute zero.

This is the Einstein-Debye correction to classical equipartition — Chapter 7 of this volume develops the full quantum statistical mechanics treatment.

### 6.5 Ergodic hypothesis

The **ergodic hypothesis**: for a system in thermal equilibrium, time averages equal ensemble averages.

$$\overline{f}_{\text{time}} = \lim_{T \to \infty} \frac{1}{T}\int_0^T f(x(t), p(t)) dt = \int dx \, dp \, f(x, p) \rho_{\text{eq}}(x, p) = \langle f\rangle_{\text{ensemble}}$$

This is what allows replacing time-evolution simulations with phase-space-integral computations. Birkhoff (1931) and von Neumann (1932) gave conditions for ergodicity; for typical interacting systems, ergodicity holds though rigorous proofs are scarce.

Substrate-mechanism reading: ergodicity is the substrate's accessibility of all energy-shell K-types over long times. The substrate's many-tick evolution (Volume 0 Chapter 3 Scale 2) explores its accessible K-type configurations; sampling sufficient ticks recovers the equilibrium distribution.

### 6.6 Kinetic theory and transport

Maxwell-Boltzmann distribution enables classical kinetic theory:

- **Mean free path**: $\ell = 1/(\sqrt 2 n \sigma)$ where $n$ is density, $\sigma$ collision cross section
- **Viscosity**: $\eta = (1/3) n \langle v\rangle \ell$ (Maxwell 1860; surprisingly independent of $n$ for dilute gases)
- **Thermal conductivity**: $\kappa = (1/3) n \langle v\rangle \ell c_v$ where $c_v$ is heat capacity per particle
- **Diffusion coefficient**: $D = (1/3) \langle v\rangle \ell$

The Boltzmann transport equation governs nonequilibrium transport; classical statistical mechanics's apparatus for irreversible processes.

### 6.7 Worked example: pressure of ideal gas

Pressure on a wall from particles bombarding it. For particles of mass $m$ moving with velocity $v_x > 0$ hitting wall: momentum transfer per collision = $2 m v_x$ (elastic). Number of particles per unit area per second with velocity $v_x$ = $(N/V) v_x P(v_x)$.

Total pressure:

$$P = \int_0^\infty 2 m v_x \cdot \frac{N}{V} v_x P(v_x) dv_x = \frac{N}{V} m \langle v_x^2\rangle = \frac{N}{V} k_B T$$

Recovers ideal gas law $PV = N k_B T$. Substrate reading: the substrate's K-type momentum exchange with the wall's K-types gives the macroscopic pressure as the integrated K-type-momentum flux.

### 6.8 The H-theorem

Boltzmann's H-theorem: for a dilute gas, the function $H = \int f \ln f \, d^3 v$ (where $f$ is the velocity distribution) is monotonically non-increasing in time. As the gas approaches equilibrium, $H$ decreases toward its minimum at the Maxwell-Boltzmann distribution; $H_{\text{equilibrium}} = -S/k_B$ recovers Boltzmann entropy.

Substrate-mechanism reading: the H-theorem is the substrate's many-tick Scale-2 entropy increase — exactly Zone 3 commitment information-discard summed over many cycles.

The Loschmidt paradox (time-reversal in microscopic dynamics vs irreversibility of H-theorem) was resolved at the substrate level: Zone 3 commitment is the substrate's intrinsic time-asymmetric step (Chapter 3 Section 3.5).

### 6.9 K-audit anchors and connections

- **Casey's Principle**: equipartition is substrate counting K-types per direction
- **Maxwell 1860, Boltzmann 1871**: foundational classical-stat-mech
- **Volume 0 Chapter 3**: Scale-2 averaging
- **Chapter 5 of this volume**: partition function (classical limit derivation)

## Level 3 — 5th-grader accessibility

Air molecules in your room are moving fast — about 500 m/s on average. They don't all move the same speed; their speeds follow the **Maxwell-Boltzmann distribution**, a bell-curve-like shape that has more slow particles than fast ones. The average kinetic energy per direction is exactly $(1/2) k_B T$ — that's the **equipartition theorem**. So a 3D particle has $(3/2) k_B T$ of kinetic energy on average. From this you can derive the ideal gas law ($PV = N k_B T$), viscosity, diffusion, heat conduction — all of classical kinetic theory. In BST, this is what happens at the substrate's Scale 2 (many-Koons-tick averaging): at room temperature, billions of substrate K-type configurations are thermally accessible; the substrate's count over those configurations gives the Maxwell-Boltzmann distribution. At low temperature, fewer K-types are accessible, and "equipartition breaks down" — vibrational modes freeze out because the substrate can't thermally reach their excited K-types.

---

## What comes next

Chapter 7 develops quantum statistical mechanics — Bose-Einstein and Fermi-Dirac distributions, Bose-Einstein condensation, Fermi gases, blackbody radiation, and the substrate-mechanism extensions.

## Where to look this up

- **Maxwell-Boltzmann**: Maxwell 1860; Boltzmann 1871
- **Equipartition**: standard derivations; Pathria Ch 3
- **H-theorem**: Boltzmann 1872; Lebowitz 1993 review
- **Kinetic theory**: Chapman and Cowling, *The Mathematical Theory of Non-Uniform Gases*
- **BST anchors**: Casey's Principle; Volume 0 Chapter 3 Scale 2
- **Chapter 5 of this volume**: partition function (master engine)
