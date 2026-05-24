---
title: "Vol 12 Chapter 3 — Molecular Orbital Theory"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 12 Chemistry from D_IV⁵"
chapter: 3
load_bearing: "MO theory; LCAO-MO; bonding + antibonding; Hückel theory for π systems; DFT modern computational chemistry"
---

# Chapter 3 — Molecular Orbital Theory

## Level 1 — one sentence

Molecular orbital (MO) theory treats electrons in molecules as occupying delocalized orbitals spanning the whole molecule (LCAO-MO construction), with bonding/antibonding/non-bonding orbitals organizing molecular spectroscopy and reactivity — and modern computational quantum chemistry (DFT, post-HF) extends this to quantitative predictions for arbitrary molecules.

## Level 2 — graduate-physicist precision

### 3.1 LCAO-MO

Molecular orbitals built from linear combinations of atomic orbitals:

$$\psi_{MO} = \sum_i c_i \phi_i^{AO}$$

For H₂: two atomic 1s orbitals $\phi_A, \phi_B$ combine into:
- **Bonding** $\sigma_g = (\phi_A + \phi_B)/\sqrt{2(1+S)}$: lower energy
- **Antibonding** $\sigma_u^* = (\phi_A - \phi_B)/\sqrt{2(1-S)}$: higher energy

With overlap integral $S = \langle\phi_A|\phi_B\rangle$.

Two electrons fill $\sigma_g$, none in $\sigma_u^*$: bonding net.

### 3.2 Bond order

Bond order = (bonding − antibonding)/2.

H₂: bond order 1. He₂: bond order 0 (equal filling) → He₂ unstable.

For O₂: bond order 2 with 2 unpaired electrons in $\pi^*$ — explains paramagnetism (one of MO's early triumphs over valence-bond theory).

### 3.3 Hückel theory for π systems

For planar conjugated systems (benzene, polyenes, porphyrins): π electrons in MOs built from p_z orbitals.

Benzene: 6 π MOs from 6 carbon $2p_z$. Lowest 3 (3 pairs of electrons): filled. Aromatic stabilization energy $\sim 36$ kcal/mol.

**Hückel 4n+2 rule**: $4n+2$ π electrons → aromatic (stable). Examples: benzene ($n=1$), naphthalene ($n=2$), [18]annulene ($n=4$).

### 3.4 Density Functional Theory (DFT)

Kohn-Sham 1965 (Nobel 1998): the ground-state energy is a functional of the electron density alone. Exact in principle; approximate exchange-correlation functionals in practice (LDA, GGA, hybrid B3LYP, etc.).

DFT enables routine quantum chemistry on molecules with hundreds of atoms. Standard codes: Gaussian, VASP, Quantum ESPRESSO, NWChem.

### 3.5 Substrate-mechanism reading

MOs are substrate K-type configurations on multi-atom boundary conditions (Vol 9 Ch 3 band-structure analog at finite molecule).

Each MO is a substrate K-type with definite symmetry under molecular point group; filling Pauli-respecting.

### 3.6 K-audit anchors

- **Vol 5 Ch 9** (Pauli, spin-statistics)
- **Vol 9 Ch 3** (band structure)

## Level 3 — 5th-grader accessibility

**Molecular orbital theory**: electrons in molecules live in orbitals spread across the whole molecule. **LCAO-MO**: combine atomic orbitals → molecular orbitals. **Bonding** (lower energy) vs **antibonding** (higher) vs **non-bonding**. **H₂**: 2 electrons fill bonding → bond. **He₂**: 4 electrons fill bonding + antibonding → no bond. **Benzene aromatic** (6 π electrons): special stability from Hückel 4n+2 rule. **DFT**: modern computational chemistry handles 100s of atoms via density-functional approach. In BST: MOs are substrate K-types on multi-atom configurations.

---

## What comes next

Chapter 4 develops chemical reactions and thermodynamics.

## Where to look this up

- Atkins-Friedman, *Molecular Quantum Mechanics*
- Parr-Yang, *Density-Functional Theory of Atoms and Molecules*
- BST: Vol 5 Ch 9; Vol 9 Ch 3
