---
title: "Vol 8 Chapter 4 — Hamiltonian Mechanics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 4
load_bearing: "Hamilton's equations; canonical transformations; Poisson brackets; bridge to QM canonical quantization"
---

# Chapter 4 — Hamiltonian Mechanics

## Level 1 — one sentence

Hamiltonian mechanics (Hamilton 1834) is the phase-space formulation of classical mechanics: replace velocities $\dot q$ with canonical momenta $p = \partial L/\partial\dot q$, define the Hamiltonian $H(q, p, t) = \sum p_i \dot q_i - L$, and dynamics is governed by Hamilton's first-order equations $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$ — the foundation for canonical quantization in QM (Vol 5).

## Level 2 — graduate-physicist precision

### 4.1 From Lagrangian to Hamiltonian: Legendre transform

Define canonical momentum: $p_i = \partial L/\partial \dot q_i$.

Hamiltonian: $H(q, p, t) = \sum_i p_i \dot q_i - L(q, \dot q, t)$ where $\dot q_i$ is solved in terms of $p_i$.

For $L = (1/2)m\dot q^2 - V(q)$: $p = m\dot q$, $\dot q = p/m$, $H = p^2/(2m) + V(q) = T + V$ = total energy.

### 4.2 Hamilton's equations

$$\dot q_i = \frac{\partial H}{\partial p_i}, \quad \dot p_i = -\frac{\partial H}{\partial q_i}$$

These are $2n$ first-order ODEs (instead of $n$ second-order from Lagrangian).

### 4.3 Phase space and Liouville's theorem

The system's state is a point in **phase space** $(q_1, \ldots, q_n, p_1, \ldots, p_n)$ of dimension $2n$. Time evolution carries each initial point along a unique trajectory.

**Liouville's theorem**: the phase-space volume is preserved by Hamiltonian flow. $d/dt[\text{vol}] = 0$ along trajectories. Has deep statistical-mechanics consequences (foundation for ergodic hypothesis, Vol 6 Ch 6).

### 4.4 Poisson brackets

For two phase-space functions $f(q, p)$, $g(q, p)$:

$$\{f, g\}_{PB} = \sum_i\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)$$

Properties: antisymmetric, Jacobi identity, Leibniz rule. Hamilton's equations:

$$\dot f = \{f, H\} + \partial_t f$$

If $\{f, H\} = 0$ and $f$ has no explicit time dependence, $f$ is conserved.

Fundamental: $\{q_i, p_j\} = \delta_{ij}$.

### 4.5 Bohr correspondence

Replacement $\{f, g\}_{PB} \leftrightarrow [\hat f, \hat g]/(i\hbar)$ — classical Poisson bracket becomes quantum commutator divided by $i\hbar$. Bohr correspondence principle. The canonical commutator $[\hat q_i, \hat p_j] = i\hbar \delta_{ij}$ (Vol 5 Ch 2) is the quantum version of the classical $\{q_i, p_j\} = \delta_{ij}$.

Substrate reading: the Poisson bracket structure is the substrate's classical-limit Lie algebra of phase-space functions; the quantum commutator structure is the substrate's full operator algebra. They map to each other at Scale 1 ↔ Scale 2 transition.

### 4.6 Canonical transformations

A transformation $(q, p) \to (Q, P)$ is **canonical** if it preserves the symplectic structure (Poisson brackets). Useful for solving problems by choosing coordinates that make the Hamiltonian simpler.

Generating functions (4 types: $F_1(q, Q), F_2(q, P), F_3(p, Q), F_4(p, P)$) give explicit canonical transformations.

### 4.7 Hamilton-Jacobi equation

For action $S(q, t)$:

$$H(q, \partial S/\partial q, t) + \partial S/\partial t = 0$$

Solving gives the action; classical trajectories are characteristics. Hamilton-Jacobi is the closest classical analog of the Schrödinger equation; the substitution $\psi \sim e^{iS/\hbar}$ converts H-J to Schrödinger in the WKB limit.

### 4.8 K-audit anchors

- **Vol 5 Ch 2**: position/momentum commutator from substrate
- **Vol 5 Ch 4**: Schrödinger equation from substrate Casimir
- **Vol 6 Ch 6**: Liouville's theorem foundation for ergodic hypothesis

## Level 3 — 5th-grader accessibility

Hamiltonian mechanics is mechanics rewritten in **phase space** — using positions $q$ AND momenta $p$ as independent variables (instead of $q$ and $\dot q$). Hamilton's equations are first-order: $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$. The **Hamiltonian** $H = T + V$ is usually total energy. **Liouville's theorem**: phase-space volume is preserved by Hamilton's flow. **Poisson brackets** generalize to **quantum commutators** via Bohr correspondence (this is canonical quantization). The Hamiltonian formalism is the natural language for both classical statistical mechanics and quantum mechanics — that's why physicists prefer it for advanced topics.

---

## What comes next

Chapter 5 develops symmetries and Noether's theorem — the substrate's parent symmetry framework.

## Where to look this up

- Goldstein Ch 8; Arnold, *Mathematical Methods of Classical Mechanics*
- BST: Vol 5 Ch 2 + Ch 4; Vol 6 Ch 6
