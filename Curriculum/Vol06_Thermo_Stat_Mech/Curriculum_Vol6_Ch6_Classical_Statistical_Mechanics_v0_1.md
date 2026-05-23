---
title: "Vol 6 Chapter 6 — Classical Statistical Mechanics"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 6
---

# Chapter 6 — Classical Statistical Mechanics

Classical statistical mechanics, developed by Boltzmann and Gibbs in the 19th century, derives thermodynamics from the statistics of classical particle ensembles. The Boltzmann distribution $p_i \propto e^{-\beta E_i}$ and the Maxwell-Boltzmann velocity distribution emerge as the equilibrium distributions of energy and momentum.

In BST, classical statistical mechanics is the substrate's Scale-2 behavior (Volume 0 Chapter 3 §3.4) — many substrate ticks averaged over a small spatial region, producing effective classical thermodynamics.

## 6.1 The Boltzmann distribution

In thermal equilibrium, the probability of a microstate of energy $E_i$ is $p_i \propto e^{-\beta E_i}$. The substrate-mechanism: the substrate's per-tick state distribution at thermal equilibrium has each K-type weighted by $\exp(-\beta C_2(\lambda))$, giving the standard Boltzmann distribution when coarse-grained over Scale-2 averages.

## 6.2 The Maxwell-Boltzmann velocity distribution

The classical velocity distribution $f(v) \propto v^2 e^{-\beta m v^2 / 2}$ emerges from the substrate's momentum eigenstate distribution at thermal equilibrium. Substrate-side: momentum eigenvalues are the Wirtinger derivative eigenvalues weighted by the Casimir energy at each K-type.

## 6.3 Equipartition

The classical equipartition theorem — each quadratic degree of freedom carries $k_B T / 2$ of energy — emerges from the substrate's K-type energy distribution at thermal equilibrium. Substrate-mechanism: K-types with quadratic Casimir contribution receive equal thermal weighting.

## 6.4 What comes next

Chapter 7 develops quantum statistical mechanics (Bose-Einstein, Fermi-Dirac).

---

**Where to look this up**: Substrate Scale-2 operation: Volume 0 Chapter 3 §3.4. For standard treatments: Pathria.
