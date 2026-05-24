---
title: "Vol 10 Chapter 10 — Calculus of Variations and Path Integrals"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 10
load_bearing: "Euler-Lagrange equations; variational principle; Feynman path integral; substrate many-tick coherent sum"
---

# Chapter 10 — Calculus of Variations and Path Integrals

## Level 1 — one sentence

The calculus of variations finds functions extremizing functionals via the Euler-Lagrange equations, providing the foundation for Lagrangian mechanics (Vol 8 Ch 3), classical field theory, and the Feynman path integral — which BST identifies as the substrate's many-Koons-tick coherent sum over K-type intermediate states (Vol 5 Ch 5).

## Level 2 — graduate-physicist precision

### 10.1 Variational principle

For functional $S[\phi] = \int L(\phi, \phi', x)\, dx$, stationarity $\delta S/\delta \phi = 0$ gives:

$$\frac{d}{dx}\frac{\partial L}{\partial \phi'} - \frac{\partial L}{\partial \phi} = 0$$

The Euler-Lagrange equation. Field-theoretic generalization for $\phi(x^\mu)$:

$$\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} - \frac{\partial \mathcal{L}}{\partial \phi} = 0$$

### 10.2 Lagrangian mechanics + field theory

Lagrangian mechanics (Vol 8 Ch 3): $L = T - V$, action $S = \int L\, dt$, equations of motion are Euler-Lagrange.

Classical field theory: $\mathcal{L}$ Lagrangian density, $S = \int \mathcal{L}\, d^4 x$. Euler-Lagrange gives field equations (Maxwell, Klein-Gordon, Dirac, Einstein, Yang-Mills).

### 10.3 Path integrals

Feynman 1948: quantum amplitude as functional integral:

$$\langle x_f | e^{-i\hat H T/\hbar} | x_i\rangle = \int \mathcal{D}\phi(t)\, e^{iS[\phi]/\hbar}$$

Sum over all paths weighted by $e^{iS/\hbar}$. Classical path is the stationary phase point as $\hbar \to 0$.

### 10.4 Saddle-point / stationary phase

For $\hbar$ small: paths off the classical-stationary path have wildly oscillating phase that destructively interferes. Only paths within $\Delta S \sim \hbar$ of the stationary path survive.

This gives **WKB approximation** and the semiclassical limit (Vol 5 Ch 5 + Vol 8 Ch 3 connection).

### 10.5 Substrate many-tick reading

Vol 5 Ch 5 Section 5.4: in BST, the path integral is the substrate's many-Koons-tick coherent sum:

$$\langle x_f | e^{-i\hat H T/\hbar} | x_i\rangle = \prod_n \langle x_n | e^{-i\hat H t_K/\hbar} | x_{n-1}\rangle$$

with $N = T/t_K$ ticks. Continuum limit ($t_K \to 0$) gives Feynman path integral.

The substrate "tries all paths" in a literal computational sense — Zone 2 evolution evolves all K-type basis elements per tick; only ones whose accumulated phase doesn't destructively interfere survive.

### 10.6 K-audit anchors

- **Vol 5 Ch 5**: path integral from substrate
- **Vol 8 Ch 3**: Lagrangian mechanics
- **DCCP**: discrete-frame substrate interpretation

## Level 3 — 5th-grader accessibility

**Calculus of variations**: find the function that extremizes some integral. Out come **Euler-Lagrange equations**. **Feynman path integral**: quantum amplitudes = sum over all paths × $e^{iS/\hbar}$. As $\hbar \to 0$, only the classical-stationary path survives (saddle point). In BST: path integral = substrate's literal many-Koons-tick sum over K-type intermediate states. The classical path is what the substrate "decides on" through constructive interference.

---

## What comes next

Chapter 11 develops asymptotic analysis.

## Where to look this up

- Gelfand-Fomin, *Calculus of Variations*
- Feynman-Hibbs, *Quantum Mechanics and Path Integrals*
- BST: Vol 5 Ch 5; Vol 8 Ch 3
