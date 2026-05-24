---
title: "Vol 9 Chapter 6 — Magnetism"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 9 Condensed Matter from D_IV⁵"
chapter: 6
load_bearing: "Diamagnetism, paramagnetism, ferromagnetism, antiferromagnetism; exchange interactions; Curie/Néel temperatures; substrate Pin(2) spin coupling"
---

# Chapter 6 — Magnetism

## Level 1 — one sentence

Magnetic phenomena — dia/para/ferro/antiferromagnetism — arise from electron spin and orbital angular momentum responding to applied fields, with exchange interactions (Heisenberg, Dzyaloshinskii-Moriya, anisotropy) producing the characteristic ordering temperatures (Curie, Néel) and order parameters; in BST these are substrate Pin(2) K-type-cluster alignments under exchange-coupling boundary conditions.

## Level 2 — graduate-physicist precision

### 6.1 Types of magnetic response

- **Diamagnetism**: induced magnetic moment opposes applied field ($\chi < 0$). All materials have this; usually weak. Bismuth, water, organic compounds. Superconductors: $\chi = -1$ (perfect diamagnetism).
- **Paramagnetism**: aligned moments with applied field ($\chi > 0, T$-dependent). Curie law: $\chi = C/T$. Cu²⁺, transition metal ions.
- **Ferromagnetism**: spontaneous parallel alignment below Curie temperature $T_C$. Fe ($T_C = 1043$ K), Co (1394 K), Ni (627 K), Gd (293 K). Hysteresis, domain structure.
- **Antiferromagnetism**: spontaneous antiparallel alignment below Néel temperature $T_N$. MnO ($T_N = 122$ K), Cr (308 K). Zero net magnetization.
- **Ferrimagnetism**: antiparallel sublattices with unequal moments. Net magnetization. Fe₃O₄ (magnetite), garnets, ferrites.

### 6.2 Heisenberg exchange

Quantum-mechanical exchange interaction between spins:

$$H_{\text{Heis}} = -\sum_{\langle i,j\rangle} J_{ij} \vec S_i \cdot \vec S_j$$

$J > 0$: ferromagnetic (favors parallel). $J < 0$: antiferromagnetic. Originates from Coulomb exchange + Pauli exclusion.

Mean-field theory (Curie-Weiss): $\chi = C/(T - T_C)$ for ferromagnet above $T_C$. Below $T_C$: spontaneous magnetization $M(T) \propto (T_C - T)^{1/2}$ in mean-field; actual exponent ~0.32 in 3D Ising universality class (Vol 6 Ch 9).

### 6.3 Spin-wave excitations (magnons)

Ferromagnet's low-energy excitations: collective spin precessions called **magnons** (quantized spin waves). Dispersion $\omega \propto k^2$ for ferromagnets; $\omega \propto k$ for antiferromagnets (gapless Goldstone modes).

### 6.4 Magnetic anisotropy

Crystal-field effects + spin-orbit coupling produce direction-dependent magnetic response. Easy-axis: preferred magnetization direction. Anisotropy energy scale ~$\mu$eV-meV per atom for most materials.

Critical for permanent magnets (NdFeB, SmCo) — strong anisotropy holds magnetization against demagnetizing fields.

### 6.5 Frustration and spin liquids (Ch 11 preview)

Geometric frustration: triangular/kagome lattice antiferromagnets can't satisfy all $J < 0$ bonds simultaneously. Leads to spin liquid states with no magnetic order even at $T = 0$.

### 6.6 Worked example: iron magnetization

Iron (BCC, FCC at high T): $M_{\text{sat}}$(0 K) ~ 1750 kA/m, corresponds to ~2.2 $\mu_B$ per Fe atom. $T_C = 1043$ K.

Above $T_C$: $\chi = C/(T - T_C)$ with $C \approx 2.4$ emu·K/mol. Paramagnetic susceptibility ~ $10^{-4}$ at room T (well above magnetic Fe is paramagnetic).

### 6.7 Substrate Pin(2) reading

In BST: magnetic moments are substrate Pin(2)-charged K-type configurations. Exchange interactions couple substrate K-types via overlap of electronic K-type configurations. Ferromagnetic ordering = collective substrate K-type Pin(2)-alignment below $T_C$.

### 6.8 K-audit anchors

- **Vol 5 Ch 3**: substrate Pin(2) spin structure
- **Vol 6 Ch 8**: phase transitions framework (applies to magnetic ordering)

## Level 3 — 5th-grader accessibility

**Magnetism** comes from electron spins and orbital motion. Five types:
- **Diamagnetism**: weak repulsion from B field (all materials)
- **Paramagnetism**: moments align with B but lose order at high T
- **Ferromagnetism**: spontaneous alignment below Curie temperature (Fe, Ni, Co)
- **Antiferromagnetism**: spontaneous anti-alignment (zero net magnetization)
- **Ferrimagnetism**: anti-alignment but unequal — net magnetization (magnetite)

The **Heisenberg exchange interaction** $H = -J\vec S_i \cdot \vec S_j$ between neighboring spins drives ordering. **Spin waves** (magnons) are the collective excitations. **Magnetic anisotropy** picks easy axis. In BST: magnetism = substrate Pin(2) K-type alignment.

---

## What comes next

Chapter 7 develops phonons.

## Where to look this up

- Ashcroft and Mermin Ch 31-33
- Blundell, *Magnetism in Condensed Matter*
- BST: Vol 5 Ch 3
