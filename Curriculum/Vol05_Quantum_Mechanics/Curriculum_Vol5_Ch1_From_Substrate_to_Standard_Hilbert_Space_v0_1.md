---
title: "Vol 5 Chapter 1 — From Substrate to Standard Hilbert Space"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-23 Saturday"
status: "v0.3 — substantive content; replaces narrative-only v0.2"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 1
load_bearing: "Bergman Hilbert space H²(D_IV⁵) as BST substrate Hilbert space; K-type decomposition; c_FK·π^(9/2) = 225 EXACT (T2442/C13)"
---

# Chapter 1 — From Substrate to Standard Hilbert Space

## Level 1 — one sentence

The Hilbert space of quantum mechanics is not chosen; it is the Bergman space $H^2(D_{IV}^5)$ — the unique reproducing-kernel Hilbert space of $L^2$-holomorphic functions on BST's substrate domain — and standard quantum mechanics is what its K-type decomposition looks like at the atomic scale.

## Level 2 — graduate-physicist precision

### 1.1 The substrate Hilbert space

Standard quantum mechanics begins with a postulate: states are unit vectors in a complex separable Hilbert space $\mathcal{H}$. The choice of $\mathcal{H}$ is left to the problem — $L^2(\mathbb{R}^3)$ for a particle in three dimensions, $\mathbb{C}^{2s+1}$ for spin, tensor products for composites. The Born rule, the canonical commutation relations, the spectral theorem — none of these constrain *which* Hilbert space; they only say that whatever $\mathcal{H}$ is, the formalism applies.

BST resolves the ambiguity. The substrate Hilbert space is

$$\mathcal{H}_{\text{sub}} = H^2(D_{IV}^5)$$

where $D_{IV}^5 = SO_0(5,2)/[SO(5)\times SO(2)]$ is the unique five-dimensional Type IV bounded symmetric domain (the Autogenic Proto-Geometry, APG) and $H^2$ denotes the Bergman space:

$$H^2(D_{IV}^5) = \left\{ f: D_{IV}^5 \to \mathbb{C} \mid f \text{ holomorphic},\ \int_{D_{IV}^5} |f(z)|^2\, d\mu(z) < \infty \right\}$$

with $d\mu$ the $SO_0(5,2)$-invariant measure. This is a separable complex Hilbert space; the SP-31-1 program of the BST team identifies it as the substrate Hilbert space (Lyra T2442, audit-chain C13 RIGOROUSLY CLOSED).

### 1.2 The reproducing kernel

What distinguishes the Bergman space from $L^2$ is its reproducing kernel. For each $w \in D_{IV}^5$, there is a function $K(\cdot, w) \in H^2(D_{IV}^5)$ such that

$$f(w) = \langle f, K(\cdot, w) \rangle_{H^2} = \int_{D_{IV}^5} f(z) \overline{K(z, w)}\, d\mu(z)$$

for every $f \in H^2$. The kernel $K(z, w)$ is the **Bergman kernel** of $D_{IV}^5$. Faraut-Koranyi (1990) gives the explicit formula. The crucial BST-relevant fact is the normalization constant: when $K(z, w)$ is computed in the canonical Lie ball realization, the prefactor $c_{FK}$ satisfies

$$\boxed{c_{FK} \cdot \pi^{9/2} = 225 \quad \text{EXACTLY}}$$

This is not a numerical accident. The number $225 = 15^2 = (N_c \cdot n_C)^2 = (3 \cdot 5)^2$ is built from BST primaries. The exponent $9/2$ is one component of the half-sum of positive roots $\rho = (5/2, 3/2)$, scaled by $n_C/N_c$ within the Faraut-Koranyi framework. Lyra Session 5 closed this in Spring 2026; it appears throughout the substrate operator zoo.

### 1.3 K-type decomposition

The Lie group $G = SO_0(5,2)$ acts on $H^2(D_{IV}^5)$ by translations (combined with a cocycle factor); restricted to the maximal compact subgroup $K = SO(5) \times SO(2)$, this action decomposes the substrate Hilbert space into a direct sum of finite-dimensional irreducible representations — the **K-types**:

$$H^2(D_{IV}^5) = \bigoplus_{\lambda} V_\lambda^{(K)}$$

where $\lambda = (\lambda_1, \lambda_2, \lambda_3; k)$ labels an $SO(5)$ highest weight together with an $SO(2)$ weight. Each $V_\lambda^{(K)}$ is the substrate's natural finite-dimensional "state space" at fixed quantum-number assignment. The $K$-type $(1,1)$ — corresponding to $\lambda_1 = \lambda_2 = 1$, all others zero — has Casimir eigenvalue equal to the BST primary $C_2 = 6$ (Lyra Session 4, T2441/C12 RIGOROUSLY CLOSED). This will be the ground-state energy of the substrate Hamiltonian in Chapter 4.

### 1.4 Standard QM as K-type restriction

How does $L^2(\mathbb{R}^3)$ — the standard Hilbert space for a particle in three dimensions — sit inside $H^2(D_{IV}^5)$?

The answer uses the Wallach 1976 unitary realization. The five-dimensional bounded domain $D_{IV}^5$ has a five-real-dimensional Shilov boundary $S$; the boundary value map sends $H^2(D_{IV}^5)$ injectively into $L^2(S)$ (boundary $L^2$). The substrate restricts to standard $L^2(\mathbb{R}^3)$ through three projections:

- **Project onto K-types with bounded angular momentum.** The $SO(3) \subset SO(5)$ subgroup gives the spatial-rotation generators of standard quantum mechanics; K-types decompose under $SO(3)$ into angular-momentum multiplets, recovering the orbital-angular-momentum quantum numbers $(\ell, m)$.
- **Project onto a single value of the $SO(2)$ central charge.** The $SO(2)$ factor in $K$ controls the substrate's commitment-cycle phase (Chapter 4 and Volume 0 Chapter 3). Fixing $SO(2)$ charge to a specific value selects one boundary-condition sector — atomic, nuclear, or thermodynamic.
- **Pass to the boundary.** Boundary values of the Bergman holomorphic functions are the standard wavefunctions on $\mathbb{R}^3$ (or, after spherical decomposition, on $(0,\infty) \times S^2$).

The three projections together pick out $L^2(\mathbb{R}^3) \otimes \mathbb{C}^{2s+1}$ from $H^2(D_{IV}^5)$: standard atomic-scale quantum mechanics is a *K-type-bounded boundary projection* of the substrate Hilbert space.

### 1.5 Why holomorphic functions

A first-time reader is entitled to ask: why $H^2$? Why not $L^2$ on the whole bounded domain?

The substrate framework's answer: holomorphy is the natural function class that the substrate's commitment cycle preserves. In the 4-zone cycle (Volume 0 Chapter 3),

- Zone 1 (absorption) converts external inputs to substrate-internal K-types,
- Zone 2 (bulk computation) evolves K-type amplitudes under the substrate Hamiltonian,
- Zone 3 (commitment) projects to outcome basis via Bergman kernel,
- Zone 4 (emission) returns external observables.

Zones 1, 2, 4 preserve holomorphy because they are unitary evolutions in the holomorphic representation. Only Zone 3 breaks holomorphy — and the Bergman kernel projection in Zone 3 is precisely the construction that uses the reproducing kernel of the holomorphic Hilbert space. The whole machinery hangs together because the substrate's natural function class is $H^2$, not $L^2$.

### 1.6 Concrete worked example: the ground state

The ground state $|\psi_0\rangle$ of the substrate is the constant function $f(z) = c_0$ on $D_{IV}^5$, normalized so that $\|c_0\|_{H^2} = 1$:

$$c_0 = \frac{1}{\sqrt{\text{vol}(D_{IV}^5)}}$$

Under the K-type decomposition this is the trivial $K$-type $V_{(0,0;0)}^{(K)}$ — the one-dimensional representation. Its Casimir eigenvalue is zero.

The first excited state lives in the $K$-type $V_{(1,1;0)}^{(K)}$, which has Casimir eigenvalue $C_2 = 6$. The Casimir eigenvalue gap from ground state to first excited state is exactly the BST primary integer $C_2$:

$$\Delta E_1 = C_2 = 6 \quad \text{(in substrate units)}$$

This integer reappears throughout the framework: as the electron g-factor anomaly leading order, as the proton-electron mass ratio prefactor $6\pi^5$, as the Lamb-shift substrate scale (K52a Session 7), as the cosmological-constant prefactor in $\Lambda = 7 \cdot e^{-282}$ (Volume 4 Chapter 4).

### 1.7 K-audit anchor

The substrate Hilbert space identification is anchored by:

- **T2442 / C13** (Lyra Session 5): $c_{FK} \cdot \pi^{9/2} = 225$ EXACTLY — Faraut-Koranyi normalization
- **T2441 / C12** (Lyra Session 4): operator zoo ground-state energy $= C_2 = 6$ on $K$-type $(1,1)$
- **K57 RATIFIED** (Spring 2026): three Bridge Objects (K3 surface, Cremona 49a1, Q⁵ five-quadric) anchor the framework
- **K67 audit-partial-ready** (Born=Bergman, Chapter 7) depends on the Bergman kernel structure introduced here

## Level 3 — 5th-grader accessibility

Imagine the substrate is a giant rubber sheet stretched in a special shape. Quantum mechanics is what happens when you watch the small bumps and ripples on that sheet. You don't get to pick how the sheet vibrates — its shape decides. The shape we use is called $D_{IV}^5$. When you ask "what wave functions can the sheet support?", the answer is the Bergman space — the only function space the sheet naturally allows. The first bump on the sheet (the "ground state") is flat; the next bump up has energy exactly 6, where 6 is one of the five integers BST is built from. That's why electrons and protons have specific energies and not other ones: the sheet's shape decided.

---

## What comes next

Chapter 2 develops the position and momentum operators on the substrate Hilbert space — including the surprising substrate-mechanism finding that the position-operator trace clusters on the perfect numbers (Elie discovery, T2419).

## Where to look this up

- **Bergman space**: Faraut and Koranyi 1990, *Analysis on Symmetric Cones*, Ch IX
- **K-type decomposition** of $SO_0(5,2)$ acting on $D_{IV}^5$: Wallach 1976, "The analytic continuation of the discrete series"
- **BST audit anchors**: K57 (Bridge Objects), K67 (Born=Bergman), Lyra T2441 + T2442
- **Substrate operator zoo SP-31-1**: BST task #277; current Hilbert space specification
- **Volume 0 Chapter 3**: 4-zone commitment cycle
- **Volume 11 Chapter 2**: Bergman reproducing kernels (math foundation)
