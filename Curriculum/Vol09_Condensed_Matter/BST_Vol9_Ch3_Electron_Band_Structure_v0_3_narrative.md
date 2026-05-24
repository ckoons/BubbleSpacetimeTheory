---
title: "Vol 9 Chapter 3 — Electron Band Structure"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 9 Condensed Matter from D_IV⁵"
chapter: 3
load_bearing: "Band structure E(k); tight-binding + nearly-free electron; metals/semiconductors/insulators; effective mass; substrate K-type spectrum on periodic lattice"
---

# Chapter 3 — Electron Band Structure

## Level 1 — one sentence

Electrons in periodic crystals have energy bands $E_n(\vec k)$ instead of discrete atomic levels, with band-filling determining whether the material is a metal (partially filled), semiconductor (small gap), or insulator (large gap), and BST identifies the bands as the substrate's K-type spectrum on the periodic ionic boundary condition.

## Level 2 — graduate-physicist precision

### 3.1 Bands from periodicity

Bloch's theorem (Ch 2) gives wave functions $\psi_{n\vec k}(\vec r)$ with energies $E_n(\vec k)$ — energy is a function of crystal momentum $\vec k$ (restricted to first Brillouin zone), labeled by band index $n$.

**Tight-binding** approach: start from atomic orbitals, allow hopping between sites. Gives bands as $E(\vec k) = E_0 - 2t\sum_i \cos(\vec k \cdot \vec a_i)$ for nearest-neighbor hopping with amplitude $t$. Bandwidth $\sim 4 z t$ for coordination number $z$.

**Nearly-free electron** approach: start from plane waves, treat periodic potential as perturbation. Gives bands with gaps at Brillouin zone boundaries (Bragg reflection mixes degenerate plane waves).

Both approaches give equivalent qualitative pictures; quantitative numerical methods include DFT, GW, dynamical mean-field theory.

### 3.2 Metals, semiconductors, insulators

The **Fermi level** $E_F$ separates filled from empty states at $T = 0$. Position relative to bands distinguishes material types:

- **Metal**: $E_F$ in a band → partial filling → free electrons → high conductivity. Examples: Cu, Al, Na.
- **Semiconductor**: $E_F$ in a small gap (~0.1-3 eV) → thermal excitation gives some conduction at finite T. Examples: Si (1.1 eV gap), Ge (0.7 eV), GaAs (1.4 eV).
- **Insulator**: $E_F$ in a large gap (>3 eV) → essentially no conduction. Examples: diamond (5.5 eV), SiO₂ (~9 eV).

For semiconductors: doping with electron donors (n-type, e.g., P in Si) or acceptors (p-type, e.g., B in Si) shifts Fermi level — basis of transistors and all modern electronics.

### 3.3 Effective mass and density of states

Near a band extremum, expand: $E(\vec k) \approx E_0 + \hbar^2 |\vec k|^2/(2m^*)$ with $m^*$ the **effective mass** (can be negative for hole-like bands).

$m^*$ ranges widely: ~$0.067 m_e$ in GaAs conduction band; ~$10 m_e$ in narrow-band materials like heavy fermions.

**Density of states** $g(E)$: number of states per energy per volume. For 3D parabolic band: $g(E) \propto \sqrt{E - E_0}$. Crucial for transport, optical, magnetic properties.

### 3.4 Fermi surface

At $T = 0$, the **Fermi surface** is the constant-energy surface $E(\vec k) = E_F$ in $\vec k$-space. Determines low-temperature electronic properties:
- Free-electron metals: sphere
- Cu, Ag, Au: nearly spherical with "necks" touching Brillouin zone faces
- Layered materials (graphene, cuprates): 2D-like Fermi surfaces

Quantum oscillations (de Haas-van Alphen, Shubnikov-de Haas) probe Fermi surface geometry experimentally.

### 3.5 Graphene as model

Graphene (single-layer graphite, 2D honeycomb lattice of carbon): nearly free 2D electron system with **massless Dirac dispersion** $E(\vec k) = \pm \hbar v_F |\vec k|$ near K, K' points of Brillouin zone. $v_F \approx c/300$ — relativistic-like dispersion!

Discovered Novoselov-Geim 2004 (Nobel 2010). Enabled the entire 2D materials field.

### 3.6 BST substrate-mechanism reading

The substrate's K-type structure on a periodic ionic lattice produces the band structure $E_n(\vec k)$. Specific predictions BST makes for materials (Volume 9 catalog):
- Iron pnictide T_c predictions (Task #105)
- Topological insulator classification (Task #106)
- Quantum Hall plateau corrections (Task #108)

### 3.7 K-audit anchors

- **Vol 5 Ch 1**: substrate Hilbert space (parent for band structure)
- **Vol 5 Ch 9**: spin-statistics (electron Pauli filling)

## Level 3 — 5th-grader accessibility

In a single atom, electrons have **discrete energy levels**. In a solid with billions of atoms, those levels broaden into **energy bands** — continuous (or nearly so) bands of allowed electron energies. The **Fermi level** is the "water line": all states below filled, all above empty (at zero temperature). Position of Fermi level relative to bands determines material type:
- **Metal**: Fermi level inside a band → conducts
- **Semiconductor**: Fermi level in small gap → conducts when warmed or doped
- **Insulator**: Fermi level in big gap → doesn't conduct

This is the foundation of all electronics. Transistors, LEDs, lasers, solar cells — all rely on engineering the band structure with dopants and heterojunctions.

---

## What comes next

Chapter 4 develops superconductivity — including BST predictions for cuprates and B12H32.

## Where to look this up

- Ashcroft and Mermin Ch 8-11
- Kittel; Marder, *Condensed Matter Physics*
- BST: tasks #105-108
