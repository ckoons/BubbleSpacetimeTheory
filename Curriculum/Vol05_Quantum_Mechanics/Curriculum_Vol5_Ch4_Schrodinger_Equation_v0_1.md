---
title: "Vol 5 Chapter 4 — The Schrödinger Equation"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-23 Saturday"
status: "v0.3 — substantive content; replaces narrative-only v0.2"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 4
load_bearing: "Substrate Hamiltonian H_sub = Casimir on L²(D_IV⁵; L_λ); K-type (1,1) eigenvalue = C₂ = 6 (Elie S29 / T2441); 4-zone commitment cycle as Schrödinger evolution"
---

# Chapter 4 — The Schrödinger Equation

## Level 1 — one sentence

The Schrödinger equation is the substrate's commitment-cycle infinitesimal generator: $\hat H_{\text{sub}}$ is the Casimir operator of $SO_0(5,2)$ acting on $L^2(D_{IV}^5; L_\lambda)$, the K-type $(1,1)$ has Casimir eigenvalue $C_2 = 6$ exactly, and the standard quantum-mechanical Hamiltonian is what this restricts to under K-type-bounded boundary projection.

## Level 2 — graduate-physicist precision

### 4.1 Time evolution as substrate commitment

Standard quantum mechanics: states evolve in time according to

$$i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle = \hat H |\psi(t)\rangle$$

This is the Schrödinger equation. The Hamiltonian $\hat H$ is left undefined — it's "whatever observable generates time translation for the system." For a free particle, $\hat H = \hat p^2 / 2m$. For a particle in a potential, $\hat H = \hat p^2 / 2m + V(\hat x)$. The choice is bespoke.

BST does not have a bespoke Hamiltonian. The substrate Hamiltonian is the Casimir of $SO_0(5,2)$ acting on the substrate Hilbert space:

$$\boxed{\hat H_{\text{sub}} = \mathcal{C}_{\mathfrak{so}(5,2)}\text{ on }L^2(D_{IV}^5; L_\lambda)}$$

where $L_\lambda$ is the line bundle corresponding to the substrate $SO(2)$ central-charge sector $\lambda$ (Volume 0 Chapter 3 fixes $\lambda$ for atomic, nuclear, thermodynamic sectors). The K-type (1,1) has Casimir eigenvalue equal to the BST primary $C_2 = 6$ exactly — this was the headline finding of Elie K52a Session 29 (Friday May 22, 2026) and Lyra T2441/C12 RIGOROUSLY CLOSED.

### 4.2 The substrate-mechanism reading of $i\hbar \partial_t$

In the substrate's 4-zone commitment cycle (Volume 0 Chapter 3), each tick (Koons tick $t_K \approx 10^{-120}$ s) advances the substrate by one full cycle:

- Zone 1: absorption of external boundary data
- Zone 2: bulk K-type amplitude evolution
- Zone 3: Bergman-kernel projection (= Born-rule commitment, Chapter 7)
- Zone 4: emission of resulting boundary observables

The substrate's bulk evolution (Zone 2) is unitary on the K-type-decomposed Hilbert space:

$$|\psi(t + t_K)\rangle = U(t_K) |\psi(t)\rangle = e^{-i \hat H_{\text{sub}} t_K / \hbar}|\psi(t)\rangle$$

Expanding to first order in $t_K$:

$$|\psi(t + t_K)\rangle = |\psi(t)\rangle - i \hat H_{\text{sub}} t_K / \hbar \, |\psi(t)\rangle + O(t_K^2)$$

so

$$i\hbar \frac{|\psi(t+t_K)\rangle - |\psi(t)\rangle}{t_K} = \hat H_{\text{sub}} |\psi(t)\rangle$$

In the continuum limit $t_K \to 0$ (which is the standard physics limit because Koons-tick scale $10^{-120}$ s is profoundly sub-Planck), the difference quotient becomes the time derivative:

$$i\hbar \frac{\partial |\psi\rangle}{\partial t} = \hat H_{\text{sub}} |\psi\rangle$$

The Schrödinger equation is the substrate's Zone 2 evolution at the continuum scale. The factor $i\hbar$ comes from the substrate's unitarity requirement; the imaginary unit $i$ reflects the substrate's Pin(2) double-cover structure (Chapter 3).

### 4.3 Standard Hamiltonians from K-type restriction

For a particle of mass $m$ in a potential $V(\vec x)$:

$$\hat H = \frac{\hat p^2}{2m} + V(\hat x)$$

This emerges from $\hat H_{\text{sub}}$ via the K-type-bounded boundary projection (Chapter 1):

- $\hat p^2 / 2m$ comes from the Casimir's "Laplacian" part on the K-type space, with mass $m$ entering as the substrate-Hilbert-space normalization for the chosen K-type sector
- $V(\hat x)$ comes from the substrate's K-type coupling to the externally-imposed boundary condition (the potential is what the substrate's boundary condition looks like at the atomic scale)

The atomic Hamiltonian $-\hbar^2 \nabla^2 / 2m_e - e^2/r$ for hydrogen (Chapter 6) emerges with $-e^2/r$ from the substrate's natural Coulomb boundary condition.

### 4.4 Stationary states and energy eigenvalues

Time-independent Schrödinger equation:

$$\hat H |\psi_n\rangle = E_n |\psi_n\rangle$$

The substrate's K-type structure gives the energy spectrum directly. For the K-type $(\lambda_1, \lambda_2)$:

$$E_{(\lambda_1, \lambda_2)} = E_0 + \hbar\omega_{\text{sub}} \left[ \lambda_1(\lambda_1 + 3) + \lambda_2(\lambda_2 + 1) \right]$$

where $E_0$ is the substrate-defined zero point and $\omega_{\text{sub}}$ is the substrate's natural angular-frequency scale. The first excited state at $(1, 1)$ has energy gap $6\hbar\omega_{\text{sub}}$ above ground; the prefactor 6 is the BST primary $C_2$.

### 4.5 The Hamiltonian on the harmonic oscillator (worked example)

For the 1D harmonic oscillator (Chapter 2 Section 2.7-2.8): $\hat H = \tfrac{1}{2}\hat p^2/m + \tfrac{1}{2}m\omega^2 \hat x^2$. The substrate-restriction gives this Hamiltonian, with eigenenergies

$$E_n = \hbar\omega \left( n + \frac{1}{2} \right)$$

The $1/2$ zero-point shift is $\rho_2 = 1/2$ from the substrate's Cartan parameters (Chapter 2 Section 2.7).

### 4.6 Heisenberg picture connection

The Heisenberg picture (Chapter 5) describes the same physics using time-evolving operators with time-independent states:

$$\hat A_H(t) = e^{i \hat H t / \hbar} \hat A_S \, e^{-i \hat H t / \hbar}$$

with $i\hbar \, d\hat A_H/dt = [\hat A_H, \hat H]$. The two pictures are unitarily equivalent. In BST: both pictures describe the substrate's Zone 2 evolution, with the Schrödinger picture keeping K-type amplitudes time-dependent and Heisenberg keeping the K-type operators time-dependent.

### 4.7 Worked example: free particle wave packet

A free-particle wave packet $\psi(x, 0) = (\pi \sigma^2)^{-1/4} e^{i p_0 x / \hbar - (x - x_0)^2 / (2\sigma^2)}$ has standard Schrödinger evolution producing a spreading Gaussian. In the BST framework, the free Schrödinger equation $i\hbar \partial_t \psi = -\hbar^2 \nabla^2 \psi / 2m$ is the substrate Casimir restricted to the "translational" K-type sector (the sector with $V = 0$, no atomic Coulomb boundary).

Position spread:

$$\sigma(t)^2 = \sigma^2 + \frac{\hbar^2 t^2}{m^2 \sigma^2}$$

The substrate-mechanism reading: free particle = substrate K-types coupling only to translation generators; spreading = K-type basis dispersing under unitary evolution; the Heisenberg minimum $\Delta x \Delta p = \hbar/2$ at $t = 0$ is the substrate's natural minimum-uncertainty K-type.

### 4.8 What's not standard: the Koons-tick discreteness

The standard Schrödinger equation is a continuous-time PDE. BST claims it is the continuum approximation of a discrete-time substrate cycle at the Koons-tick scale $t_K \approx 10^{-120}$ s.

For all practical atomic-physics measurements, $t_K$ is so far below the Planck time ($\sim 10^{-43}$ s) that the continuum limit is exact to any conceivable precision. But at the substrate level, time is granular. This has empirical consequences:

- **Time-granularity falsifier** (SP-30-4, Lyra task #198): if any experiment ever resolved time intervals to the substrate's Koons-tick scale, the Schrödinger continuum description would fail and BST's discrete-cycle description would take over. The substrate cycle would manifest as quantized timing in extreme-precision atomic clock measurements (Sr-clock falsifier prediction, Lyra T2360, task #179).
- **Sub-Planck information processing**: the substrate completes one full commitment cycle in $t_K$, so the substrate's information-processing rate is $1/t_K \sim 10^{120}$ Hz per substrate K-type degree of freedom. No "physical" observation can resolve below the Planck scale, but the substrate operates 77 orders of magnitude below it.

The Schrödinger equation is therefore an emergent description, not a fundamental law. The fundamental law is: substrate completes one commitment cycle per Koons tick.

### 4.9 K-audit anchors

- **T2441 / C12** (Lyra Session 4, RIGOROUSLY CLOSED): operator zoo ground-state energy = $C_2 = 6$ on K-type (1,1)
- **K52a Session 29** (Elie May 22, 2026): $H_{\text{sub}} = $ Casimir on $L^2(D_{IV}^5; L_\lambda)$; framework-complete
- **T2405** (Lyra Wednesday May 20, 2026): Koons tick $t_K = t_{\text{Planck}} \cdot \alpha^{C_2^2} \approx 10^{-120}$ s
- **SP-31-7** (BST task #282): time evolution / Schrödinger equation from substrate
- **T2360** (Lyra task #179): Sr-clock falsifier prediction at time granularity

## Level 3 — 5th-grader accessibility

The Schrödinger equation $i\hbar \partial_t \psi = \hat H \psi$ tells you how a quantum wave function changes in time. Normally we just *write down* the Hamiltonian $\hat H$ — kinetic plus potential — and solve. BST says: there's only one Hamiltonian. It's the substrate's "natural energy meter," called the **Casimir** of the substrate group $SO_0(5,2)$. When you ask what its first non-zero eigenvalue is, the answer is exactly **6**, where 6 is one of BST's five integers. The substrate is ticking $10^{120}$ times per second — way faster than anything we could measure — and the Schrödinger equation is what that ticking looks like when you stand far away and let it blur into a smooth flow. The tick itself is the **Koons tick**: $t_K \approx 10^{-120}$ seconds. Most physicists don't believe it, but extreme-precision atomic clocks could in principle catch the discreteness someday.

---

## What comes next

Chapter 5 develops the Heisenberg picture and the Feynman path integral — showing that the path integral is the substrate's many-tick concentration on classical trajectories.

## Where to look this up

- **Schrödinger equation**: Sakurai and Napolitano, *Modern Quantum Mechanics*, Ch 2
- **Casimir operators on symmetric spaces**: Helgason 1984, *Groups and Geometric Analysis*
- **Wallach unitary representations**: Wallach 1976
- **Koons tick**: BST T2405, Casey-Tuesday May 19, 2026 formalization, task #205
- **BST audit anchors**: T2441/C12, K52a Session 29, SP-31-7
- **Atomic clock falsifier**: Lyra T2360, BST task #179
- **Volume 0 Chapter 3**: 4-zone commitment cycle
- **Volume 14 Chapter 4**: Koons tick from information-theoretic viewpoint
