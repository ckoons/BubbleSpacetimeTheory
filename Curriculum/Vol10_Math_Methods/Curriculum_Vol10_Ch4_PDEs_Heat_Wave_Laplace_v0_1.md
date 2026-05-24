---
title: "Vol 10 Chapter 4 — PDEs: Heat, Wave, Laplace"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 4
load_bearing: "Three canonical PDEs (heat, wave, Laplace); separation of variables; heat kernel on D_IV⁵ (BST Paper #9 connection)"
---

# Chapter 4 — PDEs: Heat, Wave, Laplace

## Level 1 — one sentence

The three canonical second-order PDEs — heat (parabolic), wave (hyperbolic), Laplace (elliptic) — span the classification of linear second-order PDEs and underlie much of mathematical physics; the heat kernel on the BST substrate domain $D_{IV}^5$ is Paper #9's arithmetic-triangle subject.

## Level 2 — graduate-physicist precision

### 4.1 The three canonical PDEs

**Heat equation** (parabolic): $\partial_t u = \alpha \nabla^2 u$. Models diffusion, heat conduction. Smoothing: rough initial data becomes smooth instantly.

**Wave equation** (hyperbolic): $\partial_t^2 u = c^2 \nabla^2 u$. Finite propagation speed $c$. Preserves discontinuities along characteristics.

**Laplace equation** (elliptic): $\nabla^2 u = 0$. Harmonic functions: equal to mean value over surrounding spheres. Maximum principle: maxima on boundary.

### 4.2 Separation of variables

For PDE on rectangular domain with appropriate BCs: try $u(x, y, t) = X(x)Y(y)T(t)$, get separate ODEs (often Sturm-Liouville). Sum up eigenfunction expansion.

For heat equation on $[0, L]$ with $u(0) = u(L) = 0$: $u(x, t) = \sum_n c_n \sin(n\pi x/L) e^{-\alpha (n\pi/L)^2 t}$.

For wave equation: $u(x, t) = \sum_n [a_n \cos(\omega_n t) + b_n \sin(\omega_n t)]\sin(n\pi x/L)$ with $\omega_n = n\pi c/L$.

### 4.3 Heat kernel on D_IV⁵

The substrate's heat kernel — solution of $\partial_\tau K = \Delta K$ on $D_{IV}^5$ — has the BST-canonical Seeley-DeWitt expansion (Vol 6 Ch 5, Paper #9):

$$K(z, z; \tau) \sim (4\pi\tau)^{-5} \sum_k a_k(z) \tau^k$$

with Paper #9's arithmetic triangle giving the coefficient structure: speaking-pair period $n_C = 5$, column rule (T531), two-source primes (T532), Kummer-analog conjecture (T533). Verified through $k = 20$.

### 4.4 Green's functions

For inhomogeneous PDEs $L u = f$: Green's function $G$ satisfies $L G(\vec r, \vec r') = \delta(\vec r - \vec r')$. Solution: $u(\vec r) = \int G(\vec r, \vec r') f(\vec r') d^n r'$.

For Poisson equation in 3D: $G(\vec r, \vec r') = -1/(4\pi|\vec r - \vec r'|)$ → Coulomb-like Green's function.

### 4.5 Fundamental solutions

- Heat: $G_{\text{heat}}(\vec r, t) = (4\pi\alpha t)^{-n/2} e^{-r^2/(4\alpha t)}$ — Gaussian
- Wave (3D): $G_{\text{wave}}(\vec r, t) = \delta(r - ct)/(4\pi c^2 r)$ — sharp pulse on light cone
- Laplace (3D): $G = -1/(4\pi r)$

### 4.6 K-audit anchors

- **Paper #9** "Arithmetic Triangle of Curved Space" (Vol 6 Ch 5)
- **T531-T533**: column rule, two-source primes, Kummer conjecture

## Level 3 — 5th-grader accessibility

**Three canonical PDEs**: heat (diffusion), wave (light, sound), Laplace (electrostatics). **Separation of variables**: guess $u = X(x) Y(y) T(t)$, get separate ODEs, solve each by Sturm-Liouville. **Heat kernel** on $D_{IV}^5$ encodes substrate structure — Paper #9 found an arithmetic triangle pattern with BST primary $n_C = 5$ as the natural period, verified through 20 coefficient orders.

---

## What comes next

Chapter 5 develops Fourier analysis.

## Where to look this up

- Evans, *Partial Differential Equations*
- BST Paper #9; Vol 6 Ch 5
