---
title: "Vol 10 Chapter 1 — Linear Algebra and Hilbert Spaces"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 1
load_bearing: "Hilbert space axioms; bounded vs unbounded operators; spectral theorem; Bergman space H²(D_IV⁵) load-bearing for BST"
---

# Chapter 1 — Linear Algebra and Hilbert Spaces

## Level 1 — one sentence

Hilbert spaces — complex inner-product spaces that are Cauchy-complete — are the natural setting for quantum mechanics (Vol 5) and the BST substrate Hilbert space $H^2(D_{IV}^5)$ (Bergman space) specifically; this chapter develops the operator-theoretic machinery (spectral theorem, self-adjoint operators, projection-valued measures) underlying the physics volumes.

## Level 2 — graduate-physicist precision

### 1.1 Vector spaces and inner products

A complex vector space $V$ with sesquilinear inner product $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{C}$ satisfying:
- $\langle x, y\rangle = \overline{\langle y, x\rangle}$
- $\langle x, \alpha y + \beta z\rangle = \alpha\langle x, y\rangle + \beta\langle x, z\rangle$
- $\langle x, x\rangle \ge 0$ with equality iff $x = 0$

gives a normed space via $\|x\| = \sqrt{\langle x, x\rangle}$. If complete (Cauchy sequences converge), it's a **Hilbert space**.

Cauchy-Schwarz: $|\langle x, y\rangle| \le \|x\|\|y\|$.

### 1.2 Examples

- $\mathbb{C}^n$: finite-dimensional Hilbert space; standard QM for spin systems
- $\ell^2$: square-summable sequences; abstract separable Hilbert space
- $L^2(\mathbb{R}^n, d\mu)$: square-integrable functions on a measure space; QM wave functions
- $H^2(D)$: holomorphic $L^2$ functions on a domain $D$ — the **Bergman space**; BST substrate Hilbert space for $D = D_{IV}^5$ (Vol 5 Ch 1, Vol 11 Ch 2)

### 1.3 Orthonormal bases

A countable subset $\{e_n\}$ of $\mathcal{H}$ is an **orthonormal basis** if $\langle e_m, e_n\rangle = \delta_{mn}$ and $\overline{\text{span}}\{e_n\} = \mathcal{H}$.

Parseval: $\|x\|^2 = \sum_n |\langle e_n, x\rangle|^2$.

Every separable Hilbert space has a countable ONB.

### 1.4 Bounded operators

A linear operator $T: \mathcal{H} \to \mathcal{H}$ is **bounded** if $\|T\| = \sup_{\|x\| = 1}\|Tx\| < \infty$.

Adjoint $T^*$ defined by $\langle T^* x, y\rangle = \langle x, T y\rangle$.

- $T$ **self-adjoint**: $T = T^*$ (observable in QM)
- $T$ **unitary**: $T^*T = TT^* = I$ (time evolution)
- $T$ **projection**: $T^2 = T = T^*$ (measurement)

### 1.5 Spectral theorem

For self-adjoint $T$ on Hilbert space, there exists a projection-valued measure $E(\cdot)$ on $\sigma(T)$ (spectrum) such that

$$T = \int_{\sigma(T)} \lambda \, dE(\lambda)$$

Equivalent: $T$ has eigenvectors (discrete spectrum) and/or generalized eigenfunctions (continuous spectrum) spanning $\mathcal{H}$.

Spectral theorem is the foundation of quantum measurement: observables have spectra, outcomes are eigenvalues, probabilities come from projections (Vol 5 Ch 7).

### 1.6 Unbounded operators

Position $\hat x$ and momentum $\hat p$ are unbounded — densely defined on a domain. Spectral theorem extends with care (von Neumann's theorem on self-adjoint extensions).

### 1.7 Bergman space and BST

The Bergman space $H^2(D)$ has a **reproducing kernel** $K(z, w)$: $f(w) = \langle f, K(\cdot, w)\rangle$ for all $f \in H^2$. The Bergman kernel of $D_{IV}^5$ with normalization $c_{FK} \cdot \pi^{9/2} = 225$ (Vol 5 Ch 1) is the substrate's K-type-projection mechanism.

### 1.8 K-audit anchors

- **Vol 5 Ch 1**: Bergman H²(D_IV⁵) = substrate Hilbert space
- **Vol 11 Ch 2**: Bergman reproducing kernels (deep treatment)
- **Faraut-Koranyi 1990**: Bergman spaces on symmetric cones

## Level 3 — 5th-grader accessibility

A **Hilbert space** is a generalized vector space with infinite dimensions, a notion of length and angle (via inner product), and completeness (Cauchy sequences converge). Examples: $\mathbb{C}^n$ (finite), $\ell^2$ (sequences), $L^2$ (functions). **Operators** act on the vectors; self-adjoint operators are observables in QM; unitary operators are time evolutions; projections are measurements. The **spectral theorem**: any self-adjoint operator can be diagonalized (in a generalized sense). In BST, the substrate Hilbert space is the **Bergman space** $H^2(D_{IV}^5)$ — holomorphic, $L^2$, with a reproducing kernel built from BST primaries.

---

## What comes next

Chapter 2 develops complex analysis.

## Where to look this up

- Reed and Simon, *Methods of Modern Mathematical Physics* Vol 1
- Conway, *A Course in Functional Analysis*
- BST: Vol 5 Ch 1, Vol 11 Ch 2
