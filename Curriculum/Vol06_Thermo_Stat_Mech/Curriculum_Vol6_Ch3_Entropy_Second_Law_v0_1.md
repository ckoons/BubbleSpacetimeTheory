---
title: "Vol 6 Chapter 3 — Entropy and the Second Law"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass; entropy as Shannon entropy of substrate GF(128)^k state distribution"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 3
---

# Chapter 3 — Entropy and the Second Law

The second law of thermodynamics — that entropy never decreases in a closed system — is one of physics' deepest statements. Standard treatments derive it from statistical mechanics by counting microstates and arguing that thermodynamic evolution proceeds to higher-multiplicity macrostates. BST derives it directly from substrate Shannon entropy of Reed-Solomon code-space states.

## 3.1 Entropy as Shannon entropy of substrate states

At each Koons tick, the substrate state lives in $GF(128)^k$ — finite-dimensional, with finite Shannon entropy when interpreted as a probability distribution over code-space states. For a substrate state with probability distribution $p_i$ over states $i$:

$$S \;=\; -k_B \sum_i p_i \log p_i.$$

This is the substrate Shannon entropy. It equals the standard thermodynamic entropy when the substrate state corresponds to a thermal equilibrium.

## 3.2 The second law on the substrate

The substrate's commitment cycle is unitary at each Koons tick, but the substrate's macroscopic state (averaged over many ticks) tends toward higher Shannon entropy via the same statistical arguments standard physics uses. The substrate framework's contribution: the entropy increase is **structurally bounded** by the substrate's Reed-Solomon code-space capacity, with the maximum entropy at $\log_2 (128^k) \cdot k_B$ for $k$ active code-space dimensions.

## 3.3 Why irreversibility

The second law's apparent irreversibility — entropy increases in time, even though microscopic dynamics are reversible — has long been a puzzle. In BST, the substrate's per-tick commitment (Zone 3) explicitly breaks microscopic reversibility at each tick: the projection operator is irreversible by construction. What was a long-standing puzzle in standard thermodynamics is, in BST, structural at the per-tick level.

## 3.4 What comes next

Chapter 4 develops free energies and Maxwell relations.

---

**Where to look this up**: K59 Reed-Solomon cyclotomic mechanism. For standard entropy/second-law: Boltzmann 1872 H-theorem; Callen Chapter 4.
