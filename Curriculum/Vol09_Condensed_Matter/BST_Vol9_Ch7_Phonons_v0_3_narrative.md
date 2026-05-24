---
title: "Vol 9 Chapter 7 — Phonons"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 9 Condensed Matter from D_IV⁵"
chapter: 7
load_bearing: "Phonons = quantized lattice vibrations; acoustic + optical branches; Debye + Einstein models; phonon-mediated superconductivity (BCS link); substrate vibrational K-types"
---

# Chapter 7 — Phonons

## Level 1 — one sentence

Phonons are quantized lattice vibrations — substrate vibrational K-types of the periodic ionic configuration — with acoustic branches (linear dispersion at low $\vec k$, governing sound and elasticity) and optical branches (gapped at $\vec k = 0$, governing IR absorption), and they mediate the BCS Cooper-pair attraction for conventional superconductors (Ch 4).

## Level 2 — graduate-physicist precision

### 7.1 Lattice vibrations

For a 1D chain of identical atoms with nearest-neighbor spring constant $K$ and lattice spacing $a$:

$$\omega(k) = 2\sqrt{K/M}|\sin(ka/2)|$$

Linear at small $k$ (sound waves with speed $v_s = a\sqrt{K/M}$); maximum at zone boundary $k = \pi/a$.

For diatomic chain (two atoms per unit cell): two branches — **acoustic** (gapless at $k=0$) and **optical** (gapped at $k=0$).

In 3D: 3 acoustic branches (longitudinal + 2 transverse) + (3N-3) optical branches for N atoms per unit cell.

### 7.2 Quantization: phonons

Each normal mode is a quantum harmonic oscillator (Vol 5 Ch 4). Quantum excitations are **phonons** with energy $\hbar\omega$, momentum $\hbar k$. Bosons (integer spin).

Total energy of crystal: $E = \sum_{n,k}\hbar\omega_n(\vec k)[n_{nk} + 1/2]$ with $n_{nk}$ occupation numbers (Bose-Einstein distributed at temperature $T$).

### 7.3 Debye and Einstein models

**Einstein model** (1907): all phonons at single frequency $\omega_E$. Specific heat $C_V = 3R(\hbar\omega_E/k_BT)^2 e^{\hbar\omega_E/k_BT}/(e^{\hbar\omega_E/k_BT}-1)^2$. Reduces to $3R$ at high T (Dulong-Petit); drops as $e^{-\hbar\omega_E/k_BT}$ at low T.

**Debye model** (1912): linear acoustic dispersion up to Debye cutoff $\omega_D$, $k_BT_D = \hbar\omega_D$. Gives:
- Low T: $C_V \propto T^3$ (matches experiment for non-metals)
- High T: $C_V \to 3R$ (Dulong-Petit limit)

Debye temperatures: Pb ~88 K (soft), diamond ~2230 K (stiff).

### 7.4 Phonon-electron coupling

Phonons scatter electrons → resistivity in metals ($\rho \propto T$ above Debye T; $\rho \propto T^5$ at low T from acoustic phonons).

Phonons mediate Cooper-pair attraction in BCS superconductors (Ch 4): two electrons exchange a virtual phonon → effective attraction overcoming Coulomb repulsion below $T_c$.

### 7.5 Anharmonic effects

Beyond harmonic approximation: thermal expansion, phonon-phonon scattering (thermal conductivity at high T), Grüneisen parameter, Mössbauer effect — all anharmonic phenomena.

### 7.6 K-audit anchors

- **Vol 5 Ch 4**: quantum harmonic oscillator (single phonon mode)
- **Vol 6 Ch 7**: Debye model in stat mech
- **Vol 8 Ch 9**: continuum elasticity (long-wavelength phonons)
- **Ch 4 of this volume**: phonon-mediated BCS superconductivity

## Level 3 — 5th-grader accessibility

**Phonons** are quantized lattice vibrations — sound waves in crystals come in discrete quanta, just like light comes in photons. Two types of branches:
- **Acoustic phonons**: long-wavelength = sound waves; gapless at $k = 0$
- **Optical phonons**: high-frequency vibrations of unit cell; gapped at $k = 0$ (absorb IR light)

**Debye model**: gives specific heat $C_V \propto T^3$ at low T (matches experiment); reduces to Dulong-Petit $3R$ at high T. Phonons scatter electrons (causing resistivity). Phonons mediate **Cooper pairing** in conventional superconductors (BCS).

---

## What comes next

Chapter 8 develops the BaTiO3 137-plane substrate eigentone — BST's signature condensed-matter falsifier.

## Where to look this up

- Ashcroft and Mermin Ch 22-24
- BST: Ch 4 (phonon-BCS link); Vol 5 Ch 4
