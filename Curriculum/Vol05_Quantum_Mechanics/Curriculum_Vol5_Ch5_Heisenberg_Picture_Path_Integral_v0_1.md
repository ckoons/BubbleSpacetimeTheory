---
title: "Vol 5 Chapter 5 — The Heisenberg Picture and the Path Integral"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-23 Saturday"
status: "v0.3 — substantive content; replaces narrative-only v0.2"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 5
load_bearing: "Heisenberg vs Schrödinger equivalence; Feynman path integral as substrate many-tick concentration on classical path; Z = Tr e^{-βH} = heat kernel on D_IV⁵ (Paper #9 anchor)"
---

# Chapter 5 — The Heisenberg Picture and the Path Integral

## Level 1 — one sentence

The Heisenberg picture and the Feynman path integral are two equivalent descriptions of substrate Zone 2 evolution: Heisenberg keeps K-type operators time-dependent under the substrate Casimir flow, and the path integral is what many substrate Koons ticks look like when their cumulative amplitudes concentrate on the classical-stationary trajectory via constructive interference.

## Level 2 — graduate-physicist precision

### 5.1 The Heisenberg picture

In the Schrödinger picture (Chapter 4), states evolve and operators are fixed:

$$|\psi_S(t)\rangle = e^{-i\hat H t/\hbar} |\psi_S(0)\rangle, \quad \hat A_S = \text{const}$$

In the Heisenberg picture, operators evolve and states are fixed:

$$\hat A_H(t) = e^{i\hat H t/\hbar} \hat A_S e^{-i\hat H t/\hbar}, \quad |\psi_H\rangle = |\psi_S(0)\rangle = \text{const}$$

The two pictures give identical expectation values: $\langle\psi_S(t)|\hat A_S|\psi_S(t)\rangle = \langle\psi_H|\hat A_H(t)|\psi_H\rangle$. The choice is a matter of convenience.

The Heisenberg equation of motion:

$$i\hbar \frac{d\hat A_H}{dt} = [\hat A_H, \hat H] + i\hbar \frac{\partial \hat A_S}{\partial t}$$

For time-independent $\hat A_S$, this reduces to $i\hbar \, d\hat A_H/dt = [\hat A_H, \hat H]$.

### 5.2 Bohr correspondence: classical limit

For the substrate position operator $\hat x$ and momentum operator $\hat p$ (Chapter 2):

$$\frac{d\hat x_H}{dt} = \frac{1}{i\hbar}[\hat x, \hat H] = \frac{\hat p_H}{m}$$

$$\frac{d\hat p_H}{dt} = \frac{1}{i\hbar}[\hat p, \hat H] = -\nabla V(\hat x_H)$$

These are Hamilton's equations of classical mechanics, with $\hat x, \hat p$ replacing $x, p$. The classical Poisson bracket $\{A, B\}_{\text{PB}}$ corresponds to the quantum commutator $[\hat A, \hat B]/(i\hbar)$ — this is Bohr's correspondence principle.

BST substrate-mechanism: the classical mechanics of Volume 8 is the substrate's Heisenberg evolution at Scale 2 (many-tick averaged). The substrate's Zone 2 evolution at Scale 1 is full quantum mechanics; coarse-graining to Scale 2 recovers Hamilton's classical equations.

### 5.3 The Feynman path integral

Feynman 1948: the propagator $\langle x_f | e^{-i\hat H T/\hbar} | x_i \rangle$ (amplitude for a particle to go from $x_i$ at $t = 0$ to $x_f$ at $t = T$) is expressible as a "sum over paths":

$$\langle x_f | e^{-i\hat H T/\hbar} | x_i \rangle = \int_{x_i}^{x_f} \mathcal{D}x(t)\, e^{iS[x(t)]/\hbar}$$

where $S[x(t)] = \int_0^T L(x, \dot x) \, dt$ is the classical action functional and $\mathcal{D}x$ denotes integration over all paths from $x_i$ to $x_f$.

The classical path is the one that extremizes $S$ (Euler-Lagrange equation). For $\hbar$ small, paths with $S \gg \hbar$ contribute oscillating phases that cancel; only paths near the classical-stationary path interfere constructively. As $\hbar \to 0$, the integral concentrates on the classical trajectory.

### 5.4 The path integral from substrate

The BST substrate-mechanism derivation: between $t = 0$ and $t = T$, the substrate completes $N = T/t_K$ Koons-tick commitment cycles. Each cycle includes Zone 1-4; the full amplitude factors as

$$\langle x_f | e^{-i\hat H T/\hbar} | x_i \rangle = \prod_{n=1}^{N} \langle x_n | e^{-i\hat H t_K/\hbar} | x_{n-1}\rangle$$

Insert complete sets of position and momentum eigenstates between each tick. After standard manipulation:

$$\langle x_f | e^{-i\hat H T/\hbar} | x_i \rangle = \int \prod_n dx_n\, dp_n \, e^{i\sum_n [p_n(x_n - x_{n-1}) - H(x_n, p_n) t_K]/\hbar}$$

In the continuum limit $t_K \to 0$, the discrete sum $\sum_n[p \dot x - H] t_K$ becomes the Lagrangian action $\int (p\dot x - H) dt = \int L \, dt$. The path integral emerges.

The substrate framework reads this transparently: the path integral is the *many-tick coherent sum* of substrate Zone 2 evolution amplitudes. Each tick contributes an infinitesimal action; the sum over all sequences of intermediate substrate K-type configurations is the path integral.

### 5.5 The classical-stationary path

For paths with action $S \gg \hbar$, neighboring paths differ in $S$ by amounts that wash out the phase factor through destructive interference. Only paths within $\Delta S \sim \hbar$ of the stationary path survive.

The stationary path satisfies $\delta S = 0$ — the Euler-Lagrange equations of classical mechanics. The substrate-mechanism: at Scale 2 (many-tick averaged), the substrate's Zone 2 evolution is dominated by the path that minimizes the cumulative action, recovering classical-Lagrangian mechanics from the substrate's Schrödinger-picture quantum mechanics.

### 5.6 Worked example: free-particle propagator

For a free particle $\hat H = \hat p^2/2m$, the propagator is

$$\langle x_f | e^{-i\hat H T/\hbar} | x_i \rangle = \sqrt{\frac{m}{2\pi i \hbar T}} \exp\left[\frac{im(x_f - x_i)^2}{2\hbar T}\right]$$

The classical path is $x(t) = x_i + (x_f - x_i)t/T$, with classical action $S_{\text{cl}} = m(x_f - x_i)^2/(2T)$. The propagator equals the WKB amplitude $\sqrt{m/(2\pi i \hbar T)} \, e^{iS_{\text{cl}}/\hbar}$ — exact for the free particle (no higher-loop corrections).

Substrate reading: the free particle's substrate K-types are the translation-generated K-types; the path integral is the substrate's coherent sum across all intermediate K-type configurations, dominated by the classical path with action $S_{\text{cl}}$.

### 5.7 Wick rotation and the partition function

Rotate $t \to -i\tau$ (Wick rotation). The propagator becomes the imaginary-time evolution $e^{-\hat H \tau/\hbar}$ — the heat-kernel-like operator. The trace at "temperature" $\beta = 1/(k_B T)$:

$$Z(\beta) = \text{Tr}\, e^{-\beta \hat H} = \int dx \, \langle x | e^{-\beta \hat H} | x \rangle$$

This is the **canonical partition function** of statistical mechanics (Volume 6 Chapter 5). For the substrate on $D_{IV}^5$:

$$Z(\beta) = \text{Tr}_{H^2(D_{IV}^5; L_\lambda)} \, e^{-\beta \mathcal{C}_{\mathfrak{so}(5,2)}}$$

This trace equals the heat kernel on $D_{IV}^5$. Paper #9 "The Arithmetic Triangle of Curved Space" develops the Seeley-DeWitt expansion of this heat kernel through $k = 20$ with three theorems characterizing the arithmetic structure (speaking-pair period $n_C = 5$, column rule, two-source prime structure).

The Bohr-Sommerfeld / Wick-rotation connection: **quantum mechanics in real time = statistical mechanics in imaginary time**, both expressible as substrate Casimir traces on $L^2(D_{IV}^5; L_\lambda)$.

### 5.8 K-audit anchors

- **Paper #9** "The Arithmetic Triangle of Curved Space" v10 (Lyra+Elie, current): heat kernel on $D_{IV}^5$ through $k = 20$; speaking-pair period $n_C = 5$ confirmed
- **T531-T533**: column rule, two-source prime structure, Kummer analog conjecture for $D_{IV}^5$ heat kernel
- **Toy 639**: $k = 16$ ratio = $-24 = -\dim SU(5)$ confirmed
- **K52a Session 29** (Elie May 22, 2026): substrate Hamiltonian = Casimir framework-complete

## Level 3 — 5th-grader accessibility

There are two ways to do quantum mechanics. **One**: keep the wave function moving in time, and the operators (position, momentum) stay put. **Two (Heisenberg)**: keep the wave function frozen, and let the operators move in time. They agree. Feynman invented a **third** way: sum over every possible path the particle could take, with each path weighted by $e^{iS/\hbar}$. When $\hbar$ is small (it always is, for everyday objects), only the classical path counts — that's why a baseball travels in a parabola, not a cloud. In BST, the path integral is what happens when you add up many Koons ticks of the substrate's quantum evolution: substrate "tries" all paths, and the one with the smallest action wins by constructive interference. Trick: if you replace $t$ with $-i\tau$ (Wick rotation), you get statistical mechanics for free. Same equation, different name.

---

## What comes next

Chapter 6 develops the hydrogen atom — using the substrate machinery to recover the Bohr radius, ionization energy, and orbital spectrum.

## Where to look this up

- **Heisenberg picture**: Sakurai and Napolitano, Ch 2
- **Feynman path integral**: Feynman and Hibbs, *Quantum Mechanics and Path Integrals*
- **Heat kernel on symmetric spaces**: Heat-Kernel Asymptotics from Symmetric Spaces literature
- **Paper #9**: BST "Arithmetic Triangle of Curved Space" v10, J. Spectral Theory submission target
- **Toys 273-278, 305, 361, 463, 612-614, 620, 622, 632, 639**: heat-kernel BST coefficients verified through k=20
- **Wick rotation**: Standard QFT textbooks, e.g., Peskin and Schroeder Ch 9
- **Volume 6 Chapter 5**: substrate partition function (Wick-rotated path integral)
- **Volume 11 Chapter 2**: Bergman kernel and heat kernel connection
