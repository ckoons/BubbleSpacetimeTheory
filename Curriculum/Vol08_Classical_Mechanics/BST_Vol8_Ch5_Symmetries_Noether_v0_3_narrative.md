---
title: "Vol 8 Chapter 5 — Symmetries and Noether's Theorem"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; substrate Noether parent for classical conservation laws"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 5
load_bearing: "Noether's theorem: continuous symmetries → conservation laws; classical conservation laws inherit from substrate Noether currents (Vol 0 Ch 8)"
---

# Chapter 5 — Symmetries and Noether's Theorem

## Level 1 — one sentence

Noether's theorem (Emmy Noether 1918): every continuous symmetry of the action gives a conserved quantity — time translation → energy, spatial translation → momentum, rotation → angular momentum, $U(1)$ gauge → charge — and in BST the classical conservation laws are the Scale-2 manifestation of the substrate's $SO_0(5,2) \times U(1)$ Noether currents (Vol 0 Ch 8).

## Level 2 — graduate-physicist precision

### 5.1 Statement of Noether's theorem

For a Lagrangian $L(q_i, \dot q_i, t)$ invariant under a continuous transformation parameterized by $\epsilon$ acting on coordinates as $q_i \to q_i + \epsilon \xi_i(q, t)$ and time as $t \to t + \epsilon \tau(q, t)$, the conserved quantity is:

$$Q = \sum_i \frac{\partial L}{\partial \dot q_i} \xi_i + \left(L - \sum_i \frac{\partial L}{\partial \dot q_i}\dot q_i\right)\tau$$

Time-derivative of $Q$ along trajectories is zero.

### 5.2 The four classical conservation laws

**Time translation invariance** ($\tau = 1, \xi = 0$): conserved $Q = L - \sum p_i \dot q_i = -H$ → energy conservation.

**Spatial translation invariance** ($\xi_i = \hat n_i, \tau = 0$): conserved $Q = \vec p \cdot \hat n$ → momentum conservation along $\hat n$.

**Rotational invariance** (around axis $\hat n$, $\xi_i = (\hat n \times \vec r_i)$): conserved $Q = \hat n \cdot \vec L$ → angular momentum component along $\hat n$.

**Galilean boost invariance**: conserved $Q = \vec P t - \sum m_i \vec r_i$ → center of mass moves uniformly.

For a closed isolated system, all four hold. For systems with explicit time/space dependence (e.g., particle in time-dependent or position-dependent external field), the corresponding conservation breaks.

### 5.3 Internal symmetries

Beyond spacetime symmetries: phase symmetry $\psi \to e^{i\alpha}\psi$ for a complex field gives conserved $U(1)$ charge (in classical field theory and QED). $SU(2)$ symmetry for spinor fields gives conserved isospin. $SU(3)$ symmetry gives color charge. All from Noether.

### 5.4 Substrate-mechanism: the parent Noether structure

In BST, the substrate's symmetry group is $G_{\text{sub}} = SO_0(5,2) \times U(1)$ (the latter for the photon gauge). Its Noether currents are the substrate-level conserved currents.

Restriction to classical-spacetime Galilean → energy, momentum, angular momentum.
Restriction to internal $U(1)$ → electric charge.

Casey-named principle: the substrate's conservation structure is the *parent*; classical conservation laws are the Scale-2 inheritance.

Lyra T2473 / T2474 / T2475 (Friday May 22, 2026): formal substrate-derivations of energy, momentum, and charge conservation from substrate symmetries. The SP-31-18 program (BST task #279) catalogues 12-15 per-conservation-law substrate-derivation theorems.

### 5.5 Worked example: planet around sun

For a planet orbiting the sun under central gravity $V = -GMm/r$:

- $L$ has no explicit time dependence → energy $E$ conserved
- $L$ has no explicit dependence on angular coordinate $\phi$ → angular momentum $L_z = m r^2 \dot\phi$ conserved
- Position-dependence: not translation-invariant → momentum NOT conserved

Energy + angular momentum together uniquely determine orbital shape (next chapter — central forces).

### 5.6 K-audit anchors

- **T2473** (Lyra Friday May 22, 2026): substrate energy conservation Noether
- **T2474** (Lyra Friday May 22, 2026): substrate momentum conservation Noether
- **T2475** (Lyra Friday May 22, 2026): substrate charge conservation Noether (U(1))
- **SP-31-18** (task #279): per-conservation-law substrate-derivation theorems
- **Volume 0 Chapter 8**: substrate Noether currents (foundation)

## Level 3 — 5th-grader accessibility

Emmy Noether's 1918 theorem: every continuous symmetry gives a conservation law.
- Time-translation symmetry (physics same yesterday, today, tomorrow) → **energy** conserved
- Space-translation symmetry (physics same here, there) → **momentum** conserved
- Rotational symmetry (physics same in all orientations) → **angular momentum** conserved
- $U(1)$ phase symmetry → **electric charge** conserved

This is one of the most beautiful results in physics. In BST, these classical conservation laws are inherited from the substrate's own symmetries (the substrate has all these symmetries built in). When you can't see the symmetry being broken in the substrate, you can't see it being broken at the classical scale either.

---

## What comes next

Chapter 6 develops central forces and the Kepler problem.

## Where to look this up

- Noether 1918, "Invariante Variationsprobleme"
- Goldstein Ch 13; Marion-Thornton Ch 8
- BST: T2473-T2475, SP-31-18, Vol 0 Ch 8
