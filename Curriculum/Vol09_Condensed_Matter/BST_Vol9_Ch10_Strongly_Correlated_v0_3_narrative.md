---
title: "Vol 9 Chapter 10 — Strongly Correlated Electron Systems"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 9 Condensed Matter from D_IV⁵"
chapter: 10
load_bearing: "Mott insulators; Hubbard model; heavy fermions; fractional quantum Hall (Laughlin); strongly correlated K-type many-body substrate"
---

# Chapter 10 — Strongly Correlated Electron Systems

## Level 1 — one sentence

Strongly correlated electron systems — Mott insulators, heavy fermions, fractional quantum Hall liquids, doped cuprates — are systems where electron-electron interactions dominate over kinetic energy, breaking single-particle band-theory descriptions and requiring full many-body treatment; in BST these are substrate K-type configurations where K-type-K-type couplings can't be approximated by mean-field.

## Level 2 — graduate-physicist precision

### 10.1 The Hubbard model

The simplest strongly-correlated model: electrons on a lattice with on-site repulsion $U$ and hopping $t$:

$$H = -t\sum_{\langle i,j\rangle, \sigma} c^\dagger_{i\sigma} c_{j\sigma} + U\sum_i n_{i\uparrow} n_{i\downarrow}$$

Two limits:
- $U/t \ll 1$: nearly free electrons → band metal
- $U/t \gg 1$: strong correlations → Mott insulator (no double occupancy)

At half-filling, large $U/t$: insulating despite half-filled band. Conventional band theory predicts metal — wrong because correlation freezes electrons in place.

**Mott metal-insulator transition**: occurs at critical $U_c/t \sim$ few. Driven by correlation, not band-filling.

### 10.2 Heavy fermion materials

Compounds containing f-electron elements (Ce, U, Yb): conduction electrons hybridize with localized f-electrons via Kondo coupling. At low T, **Kondo screening** + RKKY interactions produce effective heavy quasiparticles with $m^* \sim 100-1000 m_e$.

Examples: CeAl₃, UPt₃, CeCoIn₅. Show exotic superconductivity, non-Fermi-liquid metals, quantum critical points.

### 10.3 Fractional quantum Hall liquid

(Discussed Ch 5 Section 5.2): 2D electron gas in strong B field at fractional filling $\nu = 1/3, 2/5, \ldots$ forms a topologically-ordered liquid with fractionally-charged quasiparticles and anyonic statistics.

Laughlin wave function $\Psi_{1/3} \propto \prod(z_i - z_j)^3 \exp(-\sum|z|^2/4)$ for $\nu = 1/3$. Beautifully simple.

### 10.4 High-T_c cuprates as doped Mott insulators

Cuprates (Ch 4) are doped Mott insulators: parent compound (e.g., La₂CuO₄) is antiferromagnetic Mott insulator; doping with holes (Sr substitution) or electrons gives superconductor + various exotic phases.

The cuprate phase diagram (T vs doping) shows:
- Antiferromagnet near zero doping
- Superconductor in dome around optimal doping
- Pseudogap above $T_c$ in underdoped region
- Strange metal in overdoped region

40+ years of work; consensus mechanism remains elusive. BST predicts substrate K-type origin (Ch 4, Task #88).

### 10.5 Quantum spin liquids (Ch 11 preview)

A spin liquid is a Mott insulator with no magnetic ordering even at $T = 0$ — strong correlation prevents single-particle picture; geometric frustration prevents any classical-order ground state. Topological structure: fractionalized spinon excitations + emergent gauge fields.

### 10.6 Numerical methods

Strongly correlated systems are computationally hard:
- DMRG (density matrix renormalization group): exact for 1D ground states
- QMC (quantum Monte Carlo): exact for sign-problem-free models (boson, half-filled, etc.)
- DMFT (dynamical mean-field theory): self-consistent local-correlations approach
- Exact diagonalization: only small systems (up to ~24 sites)

### 10.7 BST predictions

Task #105 (iron pnictide T_c), Task #106 (topological insulator classification), Task #107 (spin liquid order parameters), Task #108 (QHE plateau precision) — BST has filed predictions for various strongly-correlated phenomena. Cuprate Task #88 is the most prominent.

### 10.8 K-audit anchors

- **Ch 4**: cuprate superconductivity (strongly correlated)
- **Ch 5**: topological phases (overlap with FQHE)
- **Ch 11**: spin liquids
- **Tasks #88, #105-108**: BST predictions

## Level 3 — 5th-grader accessibility

**Strongly correlated** = electrons interact with each other so strongly that single-particle band theory fails. **Mott insulators**: insulating despite half-filled band (correlation freezes electrons). **Heavy fermions**: f-electron compounds with effective electron mass 100-1000× free electron. **Fractional QHE**: 2D electrons in strong B field forming exotic quasi-particles with charge $e/3$. **Cuprate high-T_c**: doped Mott insulators; ~40 years of work and still not fully understood. BST predicts mechanism via substrate K-type structure.

---

## What comes next

Chapter 11 develops spin liquids.

## Where to look this up

- Fulde, *Electron Correlations in Molecules and Solids*
- Stewart, "Heavy fermion systems" Rev Mod Phys
- BST: Tasks #88, #105-108
