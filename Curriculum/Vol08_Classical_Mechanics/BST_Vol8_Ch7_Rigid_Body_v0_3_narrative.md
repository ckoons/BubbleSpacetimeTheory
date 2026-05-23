---
title: "Vol 8 Chapter 7 — Rigid Body Dynamics"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 7
---

# Chapter 7 — Rigid Body Dynamics

Rigid body dynamics treats extended objects whose internal structure is held fixed by constraint forces. Euler angles, the inertia tensor, Euler's equations of motion, gyroscopic precession — the rigid-body apparatus is foundational for engineering mechanics and gyroscope-based navigation.

In BST, rigid bodies are substrate's bound-state K-types at Scale 2 with rotational degrees of freedom.

## 7.1 The inertia tensor

A rigid body has nine moment-of-inertia components $I_{ij}$ packed into the symmetric inertia tensor. Diagonalization gives the principal axes and principal moments of inertia.

## 7.2 Euler's equations

In the body frame, the angular momentum components evolve as

$$I_1 \dot\omega_1 - (I_2 - I_3) \omega_2 \omega_3 = N_1,$$

and cyclic. The substrate-mechanism: the angular momentum dynamics inherit from the substrate's $SO(3)$ structure with the inertia tensor characterizing the rigid body's substrate-K-type rotational eigenvalues.

## 7.3 Precession and nutation

Gyroscopes precess under applied torque at the precession rate $\Omega = \tau/L \omega$. Nutation is the secondary oscillation. Both standard rigid-body phenomena have substrate-mechanism readings via angular momentum evolution under perturbation.

## 7.4 What comes next

Chapter 8 develops oscillations.

---

**Where to look this up**: For standard rigid-body dynamics: Goldstein Chapter 5; Marion and Thornton, *Classical Dynamics*.
