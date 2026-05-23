---
title: "Vol 6 Chapter 7 — Quantum Statistical Mechanics"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 7
---

# Chapter 7 — Quantum Statistical Mechanics

Quantum statistical mechanics treats systems whose particles obey Bose-Einstein (bosons) or Fermi-Dirac (fermions) statistics. The distribution functions

$$\langle n_\epsilon \rangle_{BE} \;=\; \frac{1}{e^{\beta(\epsilon - \mu)} - 1}, \qquad \langle n_\epsilon \rangle_{FD} \;=\; \frac{1}{e^{\beta(\epsilon - \mu)} + 1}$$

govern the occupation numbers at energy $\epsilon$, chemical potential $\mu$, inverse temperature $\beta$.

In BST, both distributions emerge from the substrate's Pin(2) $\mathbb{Z}_2$ grading (Volume 5 Chapter 9) — bosons in the trivial sector with symmetric multi-particle states, fermions in the non-trivial sector with antisymmetric states.

## 7.1 Bose-Einstein distribution

Bosons occupy the trivial Pin(2) sector. Multi-boson states are symmetric tensor products of K-types; the substrate partition function for non-interacting bosons gives the Bose-Einstein distribution via standard grand-canonical methods.

Notable consequences: **Bose-Einstein condensation** (the macroscopic occupation of the ground state at low temperature) is the substrate's natural ground-state preference at $C_2 = 6$ when temperature drops below the substrate's natural condensation scale.

## 7.2 Fermi-Dirac distribution

Fermions occupy the non-trivial Pin(2) sector. Multi-fermion states are antisymmetric tensor products; **Pauli exclusion** prevents multiple fermions from occupying the same K-type. The Fermi-Dirac distribution emerges, with the Fermi energy $\epsilon_F$ set by the substrate's K-type filling at zero temperature.

## 7.3 Photon and phonon gases

The classical Planck radiation distribution $\langle n_\epsilon \rangle \propto 1/(e^{\beta\epsilon} - 1)$ for photons emerges as a special case (Bose-Einstein at chemical potential zero). Phonons in solids similarly. The substrate-mechanism reading: massless bosonic K-types with thermal substrate distribution.

## 7.4 What comes next

Chapter 8 develops phase transitions.

---

**Where to look this up**: Pin(2) Z_2 grading: Volume 0 Chapter 4 §4.1. For standard quantum statistical mechanics: Pathria.
