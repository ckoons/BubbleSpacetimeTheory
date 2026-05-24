---
title: "Vol 10 Chapter 11 — Asymptotic Analysis and WKB"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 11
load_bearing: "Asymptotic expansions; WKB semiclassical; saddle-point; stationary-phase methods"
---

# Chapter 11 — Asymptotic Analysis and WKB

## Level 1 — one sentence

Asymptotic analysis treats expansions valid in some limit (small parameter, large argument), with WKB as the canonical example (semiclassical expansion in powers of $\hbar$), saddle-point/Laplace methods for $\int e^{f(z)/\hbar}\, dz$, and stationary-phase for oscillatory integrals — all foundational for path integrals (Ch 10), turning points in QM, and asymptotic limits of special functions.

## Level 2 — graduate-physicist precision

### 11.1 Asymptotic expansions

A formal series $\sum a_n/x^n$ is asymptotic to $f(x)$ as $x \to \infty$ if for each $N$:

$$\left|f(x) - \sum_{n=0}^N a_n/x^n\right| = o(1/x^N)$$

May not converge — but partial sums approximate well.

Stirling: $\ln \Gamma(s+1) \sim s\ln s - s + (1/2)\ln(2\pi s) + 1/(12s) - 1/(360 s^3) + ...$

### 11.2 Laplace's method (saddle-point)

For $I(\lambda) = \int_a^b e^{\lambda f(t)} g(t)\, dt$ with $\lambda$ large and $f$ having a unique maximum at $t_0 \in (a,b)$:

$$I(\lambda) \sim g(t_0) e^{\lambda f(t_0)}\sqrt{\frac{2\pi}{\lambda |f''(t_0)|}}$$

Generalizes to complex contour integrals (steepest descent).

### 11.3 Stationary phase

For oscillatory integrals $I(\lambda) = \int g(t) e^{i\lambda f(t)}\, dt$ with $\lambda$ large:

$$I(\lambda) \sim g(t_0) e^{i\lambda f(t_0)} \sqrt{\frac{2\pi}{\lambda |f''(t_0)|}} e^{i\pi/4 \cdot \text{sgn}(f''(t_0))}$$

at stationary points $f'(t_0) = 0$. Foundation for path-integral saddle-point.

### 11.4 WKB approximation

For Schrödinger equation $\hbar^2 \psi'' = -[E - V(x)]\psi$: try $\psi = \exp(iS/\hbar)$, expand $S = S_0 + \hbar S_1 + ...$. At leading order:

$$S_0(x) = \pm \int^x p(x')\, dx', \quad p(x) = \sqrt{2m[E - V(x)]}$$

The WKB wave function: $\psi_{\text{WKB}}(x) \sim p(x)^{-1/2} e^{\pm i\int p\, dx/\hbar}$.

Gives semiclassical quantization (Bohr-Sommerfeld): $\oint p\, dx = 2\pi\hbar(n + 1/2)$.

Connection formulas across turning points $V(x) = E$: Airy function asymptotics.

### 11.5 Substrate connection

WKB is the small-$\hbar$ limit of the path integral (Ch 10): saddle-point + Gaussian fluctuations. In BST: substrate's many-Koons-tick coherent sum concentrates on classical-stationary path as $\hbar$-effective becomes small — Scale-2 emergence of classical mechanics.

### 11.6 K-audit anchors

- **Vol 5 Ch 5**: path integral semiclassical limit
- **Vol 8 Ch 3**: classical Lagrangian as WKB leading order

## Level 3 — 5th-grader accessibility

**Asymptotic analysis**: how do functions behave in some limit (small parameter, large argument)? **Laplace's method**: integrals like $\int e^{\lambda f(t)} dt$ are dominated by the peak of $f$ as $\lambda \to \infty$. **Stationary phase**: oscillatory integrals are dominated by where the phase is stationary. **WKB**: Schrödinger equation in semiclassical limit gives $\psi \sim p^{-1/2} e^{\pm i\int p dx/\hbar}$. Quantization: $\oint p dx = 2\pi\hbar (n + 1/2)$. These methods bridge quantum to classical and reveal universal asymptotic forms of special functions.

---

## What comes next

Chapter 12 develops numerical methods.

## Where to look this up

- Bender-Orszag, *Advanced Mathematical Methods*
- BST: Vol 5 Ch 5
