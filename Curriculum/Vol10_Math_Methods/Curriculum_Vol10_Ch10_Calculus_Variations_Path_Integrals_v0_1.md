---
title: "Vol 10 Chapter 10 — Calculus of Variations and Path Integrals"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 10
---

# Chapter 10 — Calculus of Variations and Path Integrals

The calculus of variations finds functions that extremize functionals. Classical mechanics (Lagrangian and Hamiltonian), classical field theory, and Feynman path integrals all use this framework. The mathematical apparatus underlies action principles throughout physics.

## 10.1 Euler-Lagrange equations

For functional $S[\phi] = \int L(\phi, \phi')\,dx$, stationarity gives Euler-Lagrange:

$$\frac{d}{dx}\frac{\partial L}{\partial \phi'} - \frac{\partial L}{\partial \phi} = 0.$$

Standard derivation; underlies classical mechanics (Volume 8) and field theory (Volume 1).

## 10.2 Path integrals

Feynman path integral: $\langle x_f | e^{-iHt/\hbar} | x_i \rangle = \int \mathcal{D}\phi\, e^{iS[\phi]/\hbar}$. The integral over field configurations weighted by $e^{iS}$ produces quantum amplitudes. In BST, the substrate's many-tick concentration on the classical trajectory recovers this construction (Volume 5 Chapter 5).

## 10.3 What comes next

Chapter 11 develops asymptotic analysis.

---

**Where to look this up**: For standard calculus of variations: Gelfand and Fomin, *Calculus of Variations*. For path integrals: Feynman and Hibbs, *Quantum Mechanics and Path Integrals*.
