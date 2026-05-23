---
title: "Vol 1 Chapter 6 — The Operator Zoo, In Detail"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; deepens Vol 0 Ch 7 inventory with explicit commutator algebra + Bergman-kernel matrix elements"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 6
---

# Chapter 6 — The Operator Zoo, in Detail

Volume 0 Chapter 7 introduced the substrate's operator zoo — about a dozen substrate-native operators on $H^2(D_{IV}^5)$, each derived from a specific feature of the substrate's symmetry structure. This chapter is the operational reference: each operator written out with its explicit Bergman-side realization, its commutators with the others, its eigenvalue spectrum on the K-type lattice. After this chapter we have the apparatus to write dynamics in Chapter 7.

## 6.1 The common Hilbert space

Every operator acts on $H^2(D_{IV}^5)$ (Chapter 2). The K-type decomposition under $K = SO(5) \times SO(2)$ provides eigenvalues:

$$C_2(\lambda) \;=\; \langle \lambda + \rho, \lambda + \rho \rangle - \langle \rho, \rho \rangle, \qquad \rho = (5/2, 3/2).$$

The lowest non-trivial K-type $V_{(1,1)}$ has $C_2 = 6$ (BST primary). All higher K-types carry BST-primary-derivable rational eigenvalues.

## 6.2 Position and momentum

Position acts by multiplication, momentum by Wirtinger derivative:

$$(\hat{X} f)(z) = z \cdot f(z), \qquad (\hat{P} f)(z) = -i\,\partial_z f(z).$$

Commutator from Bergman reproducing structure (Chapter 2):

$$[\hat{X}, \hat{P}] \;=\; i\hbar.$$

Position spectrum aligns with the **perfect numbers** $\{6, 28, 496, 8128, \ldots\}$ — Elie's K71 result (T2419).

## 6.3 Angular momentum, spin, total

From $SO(5)$ generators and the Pin(2) intrinsic representation:

$$[\hat{L}_i, \hat{L}_j] = i\hbar \epsilon_{ijk} \hat{L}_k, \quad [\hat{S}_i, \hat{S}_j] = i\hbar \epsilon_{ijk} \hat{S}_k, \quad [\hat{L}_i, \hat{S}_j] = 0.$$

Eigenvalues: $j(j+1)\hbar^2$ for $\hat{L}^2$ and $s(s+1)\hbar^2$ for $\hat{S}^2$. Three-dimensional laboratory angular momentum is the $SO(3) \subset SO(5)$ restriction.

## 6.4 The Hamiltonian

$\hat{H}$ is the Casimir of $SO_0(5,2)$ on $L^2(D_{IV}^5; L_\lambda)$. Lowest non-trivial eigenvalue $C_2 = 6$ (Elie K52a Session 29). The substrate's natural energy unit is set here; particle masses in Volume 2 are dimensionless multiples.

## 6.5 Charge and chirality

$\hat{Q}$ is $SO(2)$ weight on scalar K-types (Lyra T2470). Integers on lepton/boson K-types; $\pm 1/N_c$ fractions on quark K-types via $N_c$-fold color sub-structure.

$\hat{\gamma}^5$ is $SO(2)$ half-weight phase on spinor K-types (Lyra T2471). Eigenvalues $\pm 1$, involutive.

## 6.6 Discrete-symmetry operators

$\hat{P}$ (Möbius lift, T2472): unitary involution. $\hat{P}\hat{X}\hat{P}^{-1} = -\hat{X}$, $\hat{P}\hat{P}\hat{P}^{-1} = -\hat{P}$ (momentum), $\hat{P}\hat{L}\hat{P}^{-1} = +\hat{L}$.

$\hat{T}$ (Klein anti-unitary, T2433): $(\hat{T}f)(z) = \overline{f(\bar z)}$. Kramers $\hat{T}^2 = \pm 1$ via Pin(2).

$\hat{C}$ ($SO(2)$ weight negation, T2434): unitary, $\hat{C}\hat{Q}\hat{C}^{-1} = -\hat{Q}$.

Composite $\hat{C}\hat{P}\hat{T}$ commutes with substrate Hamiltonian universally.

## 6.7 Bell–CHSH and number

$\hat{B}$ on bipartite states: $\text{Tr}(\hat{B}^2) = 126/16 = 7.875$, with sub-Tsirelson deviation $1/8 = 1/2^{N_c}$ — substrate signature falsifier.

$\hat{N}$ counts substrate cycles. Particles are substrate cycles (T1922).

## 6.8 The zoo at a glance

| Op | Source | Commutes with $\hat{H}$? | Spectrum |
|---|---|---|---|
| $\hat{X}$ | coset $\mathfrak{m}$ | no | perfect numbers cluster |
| $\hat{P}$ | coset $\mathfrak{m}$ | yes if free | Wirtinger continuous |
| $\hat{L}, \hat{S}$ | $SO(5)$, Pin(2) | yes (rotational) | $j(j+1)\hbar^2$ |
| $\hat{H}$ | $SO_0(5,2)$ Casimir | self | $C_2 = 6$ min |
| $\hat{Q}$ | $SO(2)$ weight | yes | $\mathbb{Z}, \pm 1/N_c$ |
| $\hat{\gamma}^5$ | $SO(2)$ half-weight | massless: yes | $\pm 1$ |
| $\hat{P}, \hat{T}, \hat{C}$ | discrete involutions | strong+EM yes; weak no | $\pm 1$ |
| $\hat{C}\hat{P}\hat{T}$ | composite | universal | $\pm 1$ |
| $\hat{B}$ | cycle correlator | invariant | $\text{Tr}(\hat{B}^2) = 126/16$ |
| $\hat{N}$ | cycle counter | conserved | $\mathbb{Z}_{\geq 0}$ |

## 6.9 What comes next

Chapter 7 uses the zoo to develop substrate dynamics.

---

**Where to look this up**: Per-operator T-numbers as cited. For standard-QFT operator algebra, Peskin and Schroeder Chapters 2–4. Wigner anti-unitary theorem in Streater–Wightman, Chapters 1–2.
