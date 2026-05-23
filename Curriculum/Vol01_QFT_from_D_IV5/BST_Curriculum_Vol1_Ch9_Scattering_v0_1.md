---
title: "Vol 1 Chapter 9 — Scattering and the S-Matrix"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; substrate-side scattering on H²(D_IV⁵), LSZ reduction via Bergman kernel, in/out states from substrate cycle"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 9
---

# Chapter 9 — Scattering and the S-Matrix

Most of what experimental particle physics measures is scattering — collisions in which incoming particles meet, interact, and emerge as outgoing particles. The theoretical apparatus is the **S-matrix**, the unitary operator from free in-states to free out-states. Standard QFT develops it via the LSZ reduction formula, perturbative Feynman diagrams, and renormalized amplitude calculations.

BST's substrate framework offers a parallel apparatus with structural advantages. The substrate Hilbert space $H^2(D_{IV}^5)$ replaces Fock space; the Bergman reproducing kernel replaces the Feynman propagator (Volume 1 Chapter 2 §2.4); the substrate-cycle commitment phases of Volume 0 Chapter 3 supply natural in/out state preparation. The S-matrix is unitary, ultraviolet-complete by substrate structure, and computable on the substrate's per-tick $GF(128)^k$ discretization without standard-QFT renormalization machinery.

## 9.1 In-states and out-states from substrate cycle

Standard QFT defines in/out states by adiabatic switching: $H_0$ in the asymptotic past, $H$ during interaction, $H_0$ in the asymptotic future. Subtleties occupy several chapters of standard texts.

In BST, in/out states are defined by the substrate commitment cycle. **In-state**: substrate state at Zone 1 (absorption — received from environment). **Out-state**: substrate state at Zone 4 (active edge emission — broadcast to environment). The S-matrix integrates across the cycle:

$$\hat{S} \;=\; \hat{U}_{Z_4 \leftarrow Z_3} \cdot \hat{P}_{Z_3} \cdot \hat{U}_{Z_3 \leftarrow Z_2} \cdot \hat{U}_{Z_2 \leftarrow Z_1},$$

with each $\hat{U}$ a per-zone substrate evolution and $\hat{P}_{Z_3}$ the Bergman-kernel projector (Volume 1 Chapter 7 §7.4). Unitary on $H^2(D_{IV}^5)$ by the cycle's structural unitarity.

The adiabatic-switching subtlety disappears. The substrate has a definite cycle; in/out separation is the cycle's natural structure.

## 9.2 LSZ reduction on the substrate

Standard LSZ expresses S-matrix elements as products of propagators times amputated Green's functions. Lyra T2457's substrate identification gives the Bergman-kernel realization:

$$\langle z_f | \hat{S} | z_i \rangle \;=\; K_B(z_f, \bar{z}_i) \cdot (\text{commitment-phase corrections}),$$

with leading term the Bergman kernel and higher orders from substrate-cycle structure. For tree-level scattering, direct kernel evaluation. For higher orders, finite sums over K-type Casimir eigenspaces (Volume 1 Chapter 10 §10.1 ultraviolet completeness).

The structural machinery is in place; explicit multi-loop QED amplitudes on the substrate side are active research.

## 9.3 The optical theorem

Unitarity of $\hat{S}$ implies the optical theorem (total cross-section relates to imaginary part of forward elastic amplitude). On the substrate, unitarity is structural — the commitment cycle is unitary (Born=Bergman), so $\hat{S}^\dagger \hat{S} = \hat{1}$ on $H^2(D_{IV}^5)$ automatically. The optical theorem holds in substrate-derived form, with the forward elastic amplitude's imaginary part computed as Bergman-kernel evaluation on coincident arguments.

The substrate-side version preserves the standard relation while inheriting substrate ultraviolet completeness. No divergent integrals to regulate.

## 9.4 What comes next

Chapter 10 explains why BST does not need standard renormalization. Chapter 11 closes the volume with the consolidated observables reference. Volume 2 begins particle-physics applications.

---

**Where to look this up**: Substrate scattering anchor T2438 + T2457. For standard-QFT scattering: Peskin & Schroeder Chapters 4 and 7. Optical theorem: Weinberg, *Quantum Theory of Fields*, Volume 1, Chapter 3. Multi-loop substrate-side calculations: Elie K52a Sessions 10+ rail.
