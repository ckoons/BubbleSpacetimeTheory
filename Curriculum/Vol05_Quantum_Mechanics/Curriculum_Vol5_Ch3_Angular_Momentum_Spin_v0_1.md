---
title: "Vol 5 Chapter 3 — Angular Momentum and Spin"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 3
---

# Chapter 3 — Angular Momentum and Spin

Angular momentum and spin organize the rotational structure of quantum mechanics. Orbital angular momentum $\hat{L}$ generates spatial rotations; spin $\hat{S}$ is an intrinsic property of particles unrelated to spatial motion; total angular momentum $\hat{J} = \hat{L} + \hat{S}$ is what is conserved when a quantum system is rotationally invariant. Standard QM postulates each piece with its own commutation algebra.

In BST, all three come from the substrate's isotropy structure.

## 3.1 Orbital angular momentum from $SO(5)$

The substrate's $SO(5)$ factor of the isotropy (Volume 0 Chapter 4 §4.2) has ten independent rotation generators. These generators, acting on the Bergman Hilbert space, are the substrate's orbital angular momentum operators. Lyra T2425 (Task #247).

The familiar three-dimensional angular momentum of laboratory physics is the restriction to the $SO(3) \subset SO(5)$ subgroup that rotates the three physical spatial dimensions — the dimensions controlled by $N_c = 3$ (Volume 0 Chapter 4 §4.5). The standard angular-momentum algebra $[\hat{L}_i, \hat{L}_j] = i\hbar \epsilon_{ijk} \hat{L}_k$ follows from the $SO(3)$ Lie-algebra structure; eigenvalues are the standard $\hbar^2 j(j+1)$ for integer $j$.

## 3.2 Spin from Pin(2)

Spin is the substrate's *intrinsic* representation index. Lyra T2421. Volume 0 Chapter 4 §4.2's Pin(2) double cover of the isotropy carries a $\mathbb{Z}_2$ grading; half-integer-spin states (fermions) sit in the non-trivial sector of the cover, integer-spin states (bosons) in the trivial sector.

This is structurally important: spin is not added to the framework as an additional postulated structure. It is the substrate's intrinsic K-type weight under the Pin(2) lift, and the half-integer-vs-integer distinction comes directly from whether the Pin(2) covering acts non-trivially on the relevant K-type. The substrate is *required* to admit half-integer spin because rank-2 forces the Pin(2) double cover; the substrate cannot have integer-spin-only physics.

The spin algebra $[\hat{S}_i, \hat{S}_j] = i\hbar \epsilon_{ijk} \hat{S}_k$ follows from the $SU(2)$ that lies inside Pin(2) as the connected component of the double cover. Standard half-integer eigenvalues $\hbar^2 s(s+1)$ with $s = 0, 1/2, 1, 3/2, \ldots$ emerge directly.

## 3.3 Total angular momentum

$\hat{J} = \hat{L} + \hat{S}$ has its standard algebra $[\hat{J}_i, \hat{J}_j] = i\hbar \epsilon_{ijk} \hat{J}_k$, derived from the commutation of $\hat{L}$ and $\hat{S}$ with each other (orbital and spin angular momenta commute, $[\hat{L}_i, \hat{S}_j] = 0$). Conservation of total angular momentum for substrate states in rotationally-invariant settings follows from the $SO(5)$ rotational invariance of the substrate Hamiltonian.

## 3.4 Clebsch-Gordan and angular-momentum addition

The standard Clebsch–Gordan coefficient framework for combining angular momenta of two subsystems is in BST the K-type tensor-product decomposition under $SO(5) \times SO(2)$. The substrate's natural bipartite K-type structure produces the standard Clebsch-Gordan formulas; the coefficients are the substrate's K-type-multiplicities.

## 3.5 What comes next

Chapter 4 develops the substrate Schrödinger equation, using the Hamiltonian from Volume 1 Chapter 6 §6.4 (the $SO_0(5,2)$ Casimir on the appropriate K-types).

---

**Where to look this up**: Angular momentum T2425. Spin T2421. Pin(2) double cover at rank=2: T1925 Argument D. For standard angular-momentum: Sakurai Chapter 3.
