---
title: "Vol 10 Chapter 3 — ODEs and Sturm-Liouville Theory"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 3
load_bearing: "ODEs; existence + uniqueness; Sturm-Liouville eigenvalue problems; orthogonality of eigenfunctions"
---

# Chapter 3 — ODEs and Sturm-Liouville Theory

## Level 1 — one sentence

Ordinary differential equations describe physical systems with one independent variable, and Sturm-Liouville theory gives the spectral framework for boundary-value problems whose eigenfunctions form complete orthogonal bases — the foundation for separation-of-variables solutions to many physics PDEs (Schrödinger, heat, wave).

## Level 2 — graduate-physicist precision

### 3.1 First-order ODEs

$y' = f(x, y)$. Picard-Lindelöf: if $f$ is Lipschitz in $y$, unique solution exists locally.

Linear: $y' + p(x) y = q(x)$ — integrating factor solution.

Separable: $y' = g(x)h(y)$ — $\int dy/h = \int g(x) dx$.

### 3.2 Second-order linear ODEs

$y'' + p(x) y' + q(x) y = r(x)$. General solution = particular + homogeneous.

**Constant-coefficient**: $y'' + ay' + by = 0$. Characteristic equation $\lambda^2 + a\lambda + b = 0$; solutions $e^{\lambda_1 x}, e^{\lambda_2 x}$ (or $e^{\lambda x}, xe^{\lambda x}$ for repeated root).

**Frobenius method** for regular singular points.

### 3.3 Sturm-Liouville problems

Self-adjoint form: $[p(x) y']' + [q(x) + \lambda w(x)] y = 0$ on interval $[a, b]$ with boundary conditions.

Sturm-Liouville theorem:
- Eigenvalues $\lambda_n$ are real, discrete, bounded below
- Eigenfunctions $\phi_n$ are orthogonal with weight $w$: $\int_a^b \phi_m \phi_n w \, dx = 0$ for $m \neq n$
- Eigenfunctions form complete basis (any function expandable as $f = \sum c_n \phi_n$)

Examples:
- Fourier series: $-y'' = \lambda y$, periodic BC → $\sin(n\pi x/L), \cos(n\pi x/L)$
- Legendre: $((1-x^2)y')' = -\lambda y$ on $[-1,1]$ → Legendre polynomials $P_\ell(x)$, $\lambda = \ell(\ell+1)$
- Bessel: gives Bessel functions
- Hermite: gives Hermite polynomials (HO eigenfunctions, Vol 5 Ch 2)

### 3.4 Connection to substrate spectral theory

The substrate Hamiltonian (Vol 5 Ch 4) is the Casimir on $L^2(D_{IV}^5; L_\lambda)$ — a Sturm-Liouville-type spectral problem in higher dimensions. K-types are the eigenfunctions; Casimir eigenvalues are the $\lambda_n$; substrate K-type orthogonality is the higher-dimensional Sturm-Liouville orthogonality.

### 3.5 K-audit anchors

- **Vol 5 Ch 4**: substrate Casimir as Sturm-Liouville analog

## Level 3 — 5th-grader accessibility

**ODEs**: equations involving derivatives of an unknown function. **Linear constant-coefficient**: solve by guessing $e^{\lambda x}$. **Sturm-Liouville** problems: special class of eigenvalue ODEs whose eigenvalues are discrete real numbers and whose eigenfunctions form a complete orthogonal set. Examples: Fourier, Legendre, Bessel, Hermite functions. These are the building blocks for separation-of-variables solutions to physics PDEs.

---

## What comes next

Chapter 4 develops PDEs.

## Where to look this up

- Courant and Hilbert *Methods of Mathematical Physics*
- BST: Vol 5 Ch 4
