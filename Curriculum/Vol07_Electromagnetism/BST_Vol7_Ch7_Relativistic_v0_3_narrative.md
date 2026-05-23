---
title: "Vol 7 Chapter 7 — Relativistic Electrodynamics"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 7
---

# Chapter 7 — Relativistic Electrodynamics

Special relativity — Einstein 1905 — and electromagnetism are intimately related. The Lorentz transformations preserve Maxwell's equations; electric and magnetic fields transform into one another under boosts; the four-potential $A^\mu = (\phi/c, \vec{A})$ and the field tensor $F^{\mu\nu}$ make electromagnetism manifestly covariant.

In BST, special relativity is the substrate's Scale-1 behavior (Volume 4 Chapter 3), and electromagnetism's covariance follows from the substrate $SO_0(5,2)$ symmetry containing the Lorentz subgroup $SO_0(3,1)$ (Volume 0 Chapter 4 §4.5).

## 7.1 The four-potential and the field tensor

The four-potential $A^\mu = (\phi/c, \vec{A})$ combines the scalar and vector potentials. The field tensor $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ encodes the electric and magnetic fields. Both transform as tensors under Lorentz transformations.

Substrate-mechanism: the four-potential is the $U(1)_{em}$ bundle connection on the substrate's coset geometry, with Lorentz covariance inherited from the substrate's $SO_0(3,1) \subset SO_0(5,2)$ structure.

## 7.2 Maxwell's equations in covariant form

$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu, \qquad \partial_{[\mu} F_{\nu\rho]} = 0.$$

Two equations replace the four non-covariant Maxwell equations. The first is the inhomogeneous Maxwell equations (Gauss + Ampère-Maxwell); the second is the Bianchi identity (Gauss for magnetism + Faraday).

## 7.3 The Lorentz transformations of $\vec{E}$ and $\vec{B}$

Under a boost in the $x$ direction with velocity $v$, the field components transform as:

- $E_x \to E_x$, $B_x \to B_x$ (parallel components unchanged)
- $E_y \to \gamma(E_y - v B_z)$, $B_y \to \gamma(B_y + v E_z/c^2)$ (perpendicular components mix)
- $E_z \to \gamma(E_z + v B_y)$, $B_z \to \gamma(B_z - v E_y/c^2)$

This is the famous mixing of electric and magnetic fields under boosts — a moving observer sees a different combination of $\vec{E}$ and $\vec{B}$ than a stationary one.

## 7.4 What comes next

Chapter 8 develops the Lagrangian and Hamiltonian formulations.

---

**Where to look this up**: For standard relativistic EM: Jackson Chapter 11.
