---
title: "Vol 5 Chapter 5 — Heisenberg Picture and the Path Integral"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 5
---

# Chapter 5 — Heisenberg Picture and the Path Integral

Quantum mechanics admits three equivalent formulations: the Schrödinger picture (states evolve, operators fixed), the Heisenberg picture (operators evolve, states fixed), and the Feynman path integral (amplitudes summed over histories). All three give the same physical predictions for the same questions, and a working physicist switches between them as the problem demands. BST inherits all three from substrate structure.

## 5.1 The Heisenberg picture on the substrate

Heisenberg evolution: $\hat{O}(t) = \hat{U}^\dagger(t)\, \hat{O}(0)\, \hat{U}(t)$ with $\hat{U}(t) = \exp(-i\hat{H} t/\hbar)$. The infinitesimal version:

$$\frac{d \hat{O}}{dt} \;=\; \frac{i}{\hbar}[\hat{H}, \hat{O}].$$

On the substrate Hilbert space, each operator in Volume 1 Chapter 6's zoo has a Heisenberg evolution. Position rotates within the coset $\mathfrak{m}$. Angular momentum is constant by $SO(5)$ rotational invariance of the substrate Hamiltonian. Chirality oscillates with mass scale on massive fermion states. The substrate Lie-algebra structure determines all evolutions analytically.

The Heisenberg picture is the most natural framing for the substrate's per-tick representation: operators on $GF(128)^k$ evolve by Reed–Solomon-preserving transformations per tick, with the continuous Heisenberg evolution emerging as the coarse-grained limit.

## 5.2 The Feynman path integral on the substrate

The path-integral formulation expresses amplitudes as sums over substrate-cycle histories:

$$\langle z_f | \hat{U}(t) | z_i \rangle \;=\; \int_{\text{paths}} \mathcal{D}[z(\tau)]\, e^{(i/\hbar) S[z(\tau)]}.$$

On the substrate, the measure $\mathcal{D}[z(\tau)]$ is supported on holomorphic trajectories of the Bergman geometry, with boundary conditions inherited from the substrate's commitment cycle (Volume 0 Chapter 5).

A technical convenience of the substrate path integral: it does not require the $i\varepsilon$ prescription standard QFT needs for convergence. The Bergman kernel is positive-definite by Bergman 1922; the substrate-side propagator inherits positivity directly (Lyra T2457, Volume 1 Chapter 10). Path-integral contour rotations and Wick analytic continuations, which take chapters of standard QFT treatments to set up properly, simply do not arise on the substrate.

## 5.3 Equivalence of the three pictures

Standard QM proves equivalence of Schrödinger, Heisenberg, and path-integral formulations by direct manipulation of the time-evolution operator $\hat{U}(t)$. The same equivalence holds on the substrate, with all three pictures expressing the same substrate-cycle evolution at different levels of abstraction.

The choice among pictures is operational. Use Schrödinger when state evolution is the question of interest. Use Heisenberg when operator algebra is more transparent. Use path integral when summing over histories simplifies a calculation. The substrate accommodates all three.

## 5.4 What comes next

Chapter 6 derives the hydrogen atom spectrum from substrate principles.

---

**Where to look this up**: Heisenberg picture and path integral on substrate: T2438. Bergman positive-definiteness: T2457 + Bergman 1922. For standard treatments: Sakurai Chapter 2; Feynman and Hibbs, *Quantum Mechanics and Path Integrals*.
