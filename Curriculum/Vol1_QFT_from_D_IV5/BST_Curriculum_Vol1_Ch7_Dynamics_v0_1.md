---
title: "Vol 1 Chapter 7 — Substrate Dynamics"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; Schrödinger + Heisenberg + path-integral framework on H²(D_IV⁵) with substrate-tick GF(128)^k discretization; Born=Bergman derivation (K67)"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 7
---

# Chapter 7 — Substrate Dynamics

Time evolution in quantum mechanics has three equivalent formulations: Schrödinger (states evolve), Heisenberg (operators evolve), path integral (sum amplitudes over histories). BST inherits all three from substrate structure: the Hamiltonian is the $SO_0(5,2)$ Casimir of Chapter 6, the Hilbert space is $H^2(D_{IV}^5)$ of Chapter 2, the path integral runs over substrate-cycle states at the Koons-tick scale.

## 7.1 The substrate Schrödinger equation

$$i\hbar\, \partial_t |\psi(t)\rangle \;=\; \hat{H}\, |\psi(t)\rangle, \qquad |\psi(t)\rangle \in H^2(D_{IV}^5).$$

$\hat{H}$ is the Casimir of $SO_0(5,2)$ on $L^2(D_{IV}^5; L_\lambda)$ (Elie K52a Session 29). The time-evolution operator $\hat{U}(t) = \exp(-i\hat{H}t/\hbar)$ is unitary on the substrate Hilbert space — probability conservation built in.

At the substrate-discrete level, the evolution factorizes into per-tick steps on the Reed–Solomon code-space $GF(128)^k$. The continuous Schrödinger evolution is the long-time-averaged limit, with the substrate's Koons tick of $\sim 5 \times 10^{-120}$ seconds setting the temporal granularity. Lyra T2438 framework-grade closure (May 2026).

## 7.2 The Heisenberg picture

$$\hat{O}(t) \;=\; \hat{U}^\dagger(t)\, \hat{O}(0)\, \hat{U}(t), \qquad \frac{d\hat{O}}{dt} \;=\; \frac{i}{\hbar}[\hat{H}, \hat{O}].$$

Each operator from the Chapter 6 zoo has a substrate-mechanical Heisenberg evolution. Position rotates within coset directions; angular momentum is constant by $SO(5)$ rotational invariance; chirality oscillates with the mass scale on massive fermions. Per-tick representation evolves by Reed–Solomon-preserving transformations on $GF(128)^k$.

## 7.3 The substrate path integral

$$\langle z_f | \hat{U}(t_f - t_i) | z_i \rangle \;=\; \int_{\text{paths}} \mathcal{D}[z(\tau)]\, e^{(i/\hbar) S[z(\tau)]},$$

with measure supported on holomorphic trajectories of the Bergman geometry, boundary conditions inherited from the substrate commitment cycle (Volume 0 Chapter 5).

A technical economy: the substrate path integral does *not* require the $i\varepsilon$ prescription standard QFT uses for convergence. The Bergman kernel is positive-definite by Bergman 1922; the substrate-side propagator inherits positivity directly (Lyra T2457, Volume 1 Chapter 10 §10.1).

## 7.4 The Born rule, derived

In standard quantum mechanics, the Born rule $P = |\langle\lambda|\psi\rangle|^2$ is an axiom. In BST, it is *derived* from substrate structure via the K67 audit ratification: the Born-rule projection is exactly the **Bergman-kernel projection** acting on the substrate's commitment-phase state (Zone 3 of Volume 0 Chapter 3's four-phase cycle).

The Bergman kernel is positive-definite, normalized by $c_{FK} \cdot \pi^{9/2} = 225$, and its diagonal action on the substrate state gives exactly the Born probabilities. The "measurement problem" of standard QM — what does projection mean, when does it apply — is replaced by the substrate's deterministic commitment cycle. Measurement is Zone 3 of the substrate tick.

This is one of BST's most consequential foundational results.

## 7.5 Decoherence and the classical limit

Standard QM treats decoherence as environmental — interactions cause off-diagonal density-matrix elements to decay. In BST, decoherence is *structural*: the substrate's per-tick commitment cycle (Zone 3) projects onto definite outcomes every Koons tick. At macroscopic scales (many ticks), the substrate has commitment-projected so often that the state is effectively classical. The three-scale substrate operation of Volume 0 Chapter 3 §3.4 is the structural origin: Scale 1 quantum (intra-cycle), Scale 2 classical (inter-cycle local averaging).

Lyra T2480 (May 2026, SP-31 #284) provides the substrate-mechanism derivation. No external environment required.

## 7.6 What comes next

Chapter 8 derived the Standard Model gauge group $SU(3) \times SU(2) \times U(1)$ from BST primaries. The dynamics framework of this chapter applies to gauge sectors via Lyra T2477's gauge-fields-as-Bergman-bundle-connections result.

Chapter 9 develops scattering. Chapter 10 explains why renormalization is unnecessary. Chapter 11 closes with the observables reference.

---

**Where to look this up**: Substrate dynamics anchor T2438; Hamiltonian completion Elie K52a S29; Born=Bergman the K67 audit; substrate decoherence T2480. For standard QM dynamics: Sakurai, *Modern Quantum Mechanics*. Path integrals: Feynman & Hibbs. Decoherence: Zurek 2003, *Reviews of Modern Physics* 75:715.
