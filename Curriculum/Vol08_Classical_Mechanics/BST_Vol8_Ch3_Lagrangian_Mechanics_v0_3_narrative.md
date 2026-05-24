---
title: "Vol 8 Chapter 3 — Lagrangian Mechanics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 3
load_bearing: "Euler-Lagrange equations; action principle; generalized coordinates; constraints"
---

# Chapter 3 — Lagrangian Mechanics

## Level 1 — one sentence

Lagrangian mechanics (Lagrange 1788) reformulates Newton's laws as a variational principle: a system's trajectory is the one that extremizes the action $S = \int L\, dt$ where $L = T - V$ is the Lagrangian (kinetic minus potential energy), giving Euler-Lagrange equations $\frac{d}{dt}\frac{\partial L}{\partial \dot q_i} = \frac{\partial L}{\partial q_i}$ that are coordinate-free and naturally handle constraints.

## Level 2 — graduate-physicist precision

### 3.1 The action principle

For a system with generalized coordinates $q_i(t)$ and Lagrangian $L(q, \dot q, t) = T - V$:

$$S = \int_{t_1}^{t_2} L(q, \dot q, t)\, dt$$

The classical trajectory between fixed endpoints is the one that makes $S$ stationary: $\delta S = 0$.

### 3.2 Euler-Lagrange equations

Stationarity condition gives:

$$\frac{d}{dt}\frac{\partial L}{\partial \dot q_i} - \frac{\partial L}{\partial q_i} = 0 \quad \text{for each } i$$

These are the Euler-Lagrange equations. For Cartesian coordinates with $L = (1/2)m\dot{\vec r}^2 - V(\vec r)$:

$$\frac{d}{dt}(m\dot{\vec r}) = -\nabla V = \vec F$$

— Newton's second law. Lagrangian mechanics reproduces Newton in Cartesian coordinates, but generalizes to any coordinate system (spherical, cylindrical, body-fixed, etc.) without modification.

### 3.3 Generalized coordinates

Lagrangian formalism works in any coordinates compatible with the system's constraints. For a pendulum: use angle $\theta$ (one DOF) instead of $(x, y)$ with constraint. For a rigid body: use Euler angles. For a double pendulum: $(\theta_1, \theta_2)$.

Number of DOFs = configuration-space dimension after eliminating constraints.

### 3.4 Constraints and Lagrange multipliers

Holonomic constraints $f(q, t) = 0$ reduce DOFs. Non-holonomic constraints (like rolling without slipping) require Lagrange multipliers $\lambda$ added to the action:

$$L \to L + \sum_k \lambda_k f_k(q, \dot q, t)$$

The multipliers turn out to be the constraint forces.

### 3.5 Worked example: spherical pendulum

A mass $m$ on a string of length $\ell$ swinging in 3D, gravity $g$. Use spherical coordinates $(\theta, \phi)$:

$$L = \frac{1}{2}m\ell^2(\dot\theta^2 + \sin^2\theta \, \dot\phi^2) - mg\ell(1 - \cos\theta)$$

Euler-Lagrange in $\theta$:

$$m\ell^2 \ddot\theta - m\ell^2 \sin\theta\cos\theta\, \dot\phi^2 + mg\ell\sin\theta = 0$$

Euler-Lagrange in $\phi$: since $L$ has no explicit $\phi$ dependence (cyclic coordinate),

$$\frac{\partial L}{\partial \dot\phi} = m\ell^2\sin^2\theta \cdot \dot\phi = L_z = \text{const}$$

— angular momentum about vertical is conserved (Noether → next chapter).

### 3.6 D'Alembert's principle

Equivalent formulation of Lagrangian mechanics:

$$\sum_i (F_i - m_i \ddot{\vec r}_i) \cdot \delta\vec r_i = 0$$

for any virtual displacement $\delta\vec r_i$ compatible with constraints. Avoids explicit forces of constraint.

### 3.7 Connection to path integral and substrate

Volume 5 Chapter 5 Section 5.3-5.4: Feynman path integral expresses quantum amplitude as $\int \mathcal{D}q\, e^{iS/\hbar}$. The classical-stationary path (where $\delta S = 0$) dominates by stationary phase as $\hbar \to 0$ — which is the substrate's Scale-2 limit.

Substrate-mechanism reading: Lagrangian classical mechanics is the substrate's many-tick saddle-point selection. The classical trajectory is the one the substrate's Zone 2 evolution concentrates on by destructive-interference of off-classical paths.

### 3.8 K-audit anchors

- **Vol 5 Ch 5 Section 5.3-5.4**: path integral foundation
- **DCCP** memory: many-tick coherent sum → classical saddle point

## Level 3 — 5th-grader accessibility

Instead of writing $F = ma$, Lagrangian mechanics writes one number: $L = T - V$ (kinetic minus potential energy). Then it finds the trajectory that makes the integral $S = \int L \, dt$ extremal (the "action principle"). Out come the same equations of motion as Newton, but in any coordinates you like — Cartesian, polar, spherical, whatever. Big advantage: constraints (like a pendulum's fixed length) are handled naturally. Cyclic coordinates (those that don't appear in $L$) automatically give conservation laws (next chapter). In BST, the Lagrangian principle is the substrate's classical limit of the path integral: the substrate sums over all paths quantum-mechanically; in the classical limit, the action-extremizing path dominates.

---

## What comes next

Chapter 4 develops Hamiltonian mechanics — the canonical phase-space formalism.

## Where to look this up

- Goldstein Ch 2; Landau-Lifshitz Vol 1
- BST: Vol 5 Ch 5 (path integral); DCCP memory
