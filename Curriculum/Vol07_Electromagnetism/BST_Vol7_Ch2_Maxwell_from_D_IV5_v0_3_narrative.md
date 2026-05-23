---
title: "Vol 7 Chapter 2 — Maxwell's Equations from D_IV⁵"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 2
---

# Chapter 2 — Maxwell's Equations from D_IV⁵

Maxwell's four equations — Gauss's law for electric fields, Gauss's law for magnetism, Faraday's law, Ampère-Maxwell law — are the central equations of classical electromagnetism. Standard physics derives them from experiment over the nineteenth century (Coulomb, Ampère, Faraday) and unifies them into a single framework via Maxwell's introduction of the displacement current.

In BST, Maxwell's equations follow from the substrate's $U(1)$ bundle connection $A^\mu$ and its curvature $F^{\mu\nu}$ via the standard differential-geometric framework, with the substrate providing the natural $U(1)$ structure.

## 2.1 The field tensor

The electromagnetic field tensor is $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, the curvature of the substrate's $U(1)$ bundle connection. Its components encode the electric and magnetic fields:

$$F_{0i} = E_i, \qquad F_{ij} = -\epsilon_{ijk} B_k.$$

## 2.2 Maxwell's equations

The substrate-side derivation gives:

- $\nabla \cdot \vec{E} = \rho/\epsilon_0$ (Gauss)
- $\nabla \cdot \vec{B} = 0$ (Gauss for magnetism — no monopoles per Five-Absence)
- $\nabla \times \vec{E} = -\partial \vec{B}/\partial t$ (Faraday)
- $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \epsilon_0 \partial \vec{E}/\partial t$ (Ampère-Maxwell)

Standard Maxwell. The substrate reproduces every equation; what changes is the *origin*: the equations follow from substrate bundle-curvature consistency, not from inductive empirical observation.

## 2.3 The substrate's no-monopole prediction

Volume 2 Chapter 11's Five-Absence set includes "no magnetic monopoles." This is structural: the substrate's $U(1)$ bundle on $D_{IV}^5$ is trivial at the relevant topology, so $\nabla \cdot \vec{B} = 0$ holds exactly with no monopole correction. Experimental searches for monopoles have produced no positive results; BST predicts none ever.

## 2.4 What comes next

Chapter 3 develops electrostatics. Chapter 4 covers magnetostatics.

---

**Where to look this up**: T2477 substrate gauge connection. For standard Maxwell: Jackson Chapter 1.
