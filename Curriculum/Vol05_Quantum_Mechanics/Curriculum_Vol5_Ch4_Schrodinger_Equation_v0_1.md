---
title: "Vol 5 Chapter 4 — The Schrödinger Equation"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 4
---

# Chapter 4 — The Schrödinger Equation

Schrödinger's equation governs the time evolution of quantum states:

$$i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle \;=\; \hat{H} |\psi(t)\rangle.$$

Standard QM postulates this equation as the dynamical law. In BST, it emerges as the continuum limit of the substrate's discrete commitment-cycle evolution on the Bergman Hilbert space.

## 4.1 The substrate Hamiltonian

Volume 1 Chapter 7 §7.1 set out the substrate-derivation of the Schrödinger equation in summary. The Hamiltonian $\hat{H}$ acting on $H^2(D_{IV}^5)$ is the Casimir operator of $SO_0(5,2)$ restricted to the appropriate K-type representation:

$$\hat{H} \;=\; \text{Casimir of } \mathfrak{so}(5,2) \text{ on } L^2(D_{IV}^5; L_\lambda).$$

The lowest non-trivial eigenvalue is $C_2 = 6$ — the BST primary integer — which sets the substrate's natural energy unit. Elie's K52a Session 29 framework-completed this identification.

## 4.2 Discrete-tick evolution to continuum Schrödinger

At each Koons tick of approximately $5 \times 10^{-120}$ seconds, the substrate's state evolves by the unitary operator $\exp(-i \hat{H} \delta t / \hbar)$ where $\delta t$ is the tick interval. The discrete-tick evolution composes to give the continuous Schrödinger evolution $\hat{U}(t) = \exp(-i \hat{H} t/\hbar)$ when one averages over many ticks; this composition is straightforward from the substrate's Reed–Solomon code-space structure (Volume 0 Chapter 3 §3.5).

For ordinary quantum-mechanical applications — atomic transitions, scattering, bound-state spectra — the time scales involved are vastly larger than the Koons tick, so the continuum Schrödinger equation applies essentially exactly. Substrate-discrete corrections enter at scales of order $t / t_{\text{tick}} \cdot $ exponentially small numbers, beyond any experimental precision.

## 4.3 Stationary states

A stationary state $|\psi_n\rangle$ is an eigenstate of $\hat{H}$ with eigenvalue $E_n$: $\hat{H} |\psi_n\rangle = E_n |\psi_n\rangle$. The general time-dependent state is a superposition $|\psi(t)\rangle = \sum_n c_n e^{-i E_n t / \hbar} |\psi_n\rangle$ that evolves by phase rotation of each eigenstate.

For the substrate Hamiltonian, the stationary states are the K-type eigenstates of $H^2(D_{IV}^5)$, labeled by Wallach weights. The substrate's energy spectrum is therefore *discrete* (countably many K-type weights, each with finite multiplicity), with eigenvalues computable from the Casimir formula of Volume 1 Chapter 5 §5.2.

## 4.4 Time-dependent perturbation theory

For a Hamiltonian $\hat{H} = \hat{H}_0 + \hat{V}(t)$ split into an unperturbed and a perturbing piece, standard time-dependent perturbation theory expresses transition amplitudes between $\hat{H}_0$-eigenstates as integrals of $\hat{V}$ matrix elements over time. The substrate-mechanical version of this calculation runs the same way; the only difference is that the matrix elements are Bergman-kernel evaluations on K-types rather than spatial integrals on Minkowski wavefunctions.

For typical applications — atomic transitions induced by electromagnetic fields, scattering by external potentials — the calculation reproduces the standard time-dependent perturbation theory to whatever precision is required.

## 4.5 What comes next

Chapter 5 develops the Heisenberg picture and the path-integral formulation.

---

**Where to look this up**: Substrate dynamics anchor T2438. Hamiltonian framework completion: Elie K52a S29. Substrate-tick discretization T2429. For standard Schrödinger: Sakurai Chapter 2.
