---
title: "Vol 6 Chapter 8 — Phase Transitions"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Ising; mean-field; Landau; order parameters; substrate K-type cluster reorganization"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 8
load_bearing: "Phase transitions as substrate K-type cluster reorganization; Ising model; mean-field theory; Landau symmetry-breaking framework"
---

# Chapter 8 — Phase Transitions

## Level 1 — one sentence

Phase transitions — water boiling, iron magnetizing, helium becoming superfluid — are substrate K-type reorganizations at critical points where the system's macroscopic state changes qualitatively (order parameter switches from zero to nonzero, or vice versa), and Landau's symmetry-breaking framework describes the universal phenomenology while substrate-mechanism identifies which K-type cluster restructuring is happening at each transition.

## Level 2 — graduate-physicist precision

### 8.1 What is a phase transition

A **phase transition** is a singular change in the thermodynamic state of a system as a control parameter (typically temperature, pressure, or magnetic field) crosses a critical value.

Two main types:
- **First-order**: discontinuous change in first derivatives of free energy (entropy, volume). Has latent heat. Examples: solid-liquid, liquid-gas at non-critical points.
- **Second-order (continuous)**: continuous order parameter that vanishes at $T_c$; divergent susceptibilities. No latent heat. Examples: ferromagnet at Curie temp, superfluid transition, liquid-gas at critical point.

The Ehrenfest classification (1933) labels transitions by which derivative becomes discontinuous; modern usage emphasizes the order parameter structure.

### 8.2 Order parameters

An **order parameter** $\phi$ is a quantity that:
- Vanishes in the high-symmetry "disordered" phase
- Becomes nonzero in the low-symmetry "ordered" phase
- Approaches zero continuously (second-order) or jumps (first-order) at the transition

Examples:
- Ferromagnet: magnetization $\vec M$
- Liquid-gas: density difference $\rho_l - \rho_g$
- Superfluid: complex condensate wavefunction $\psi$
- Superconductor: BCS gap $\Delta$
- Crystallization: structure factor amplitude

Substrate-mechanism reading: order parameter is the substrate's K-type cluster amplitude. Above $T_c$: substrate K-types fluctuate independently; cluster amplitude averages to zero. Below $T_c$: substrate K-types correlate into clusters with macroscopic amplitude.

### 8.3 The Ising model

The Ising model is the canonical lattice model of phase transitions. Spins $s_i = \pm 1$ on a lattice, with Hamiltonian:

$$H = -J \sum_{\langle i,j\rangle} s_i s_j - h \sum_i s_i$$

$J > 0$ favors aligned neighbors (ferromagnetic); $h$ is external field.

Order parameter: magnetization $m = (1/N)\sum_i \langle s_i\rangle$.

In 1D: no phase transition at finite $T$ (Ising 1925 — thermal fluctuations destroy long-range order).

In 2D: phase transition at $k_BT_c/J = 2/\ln(1+\sqrt 2) \approx 2.269$ (Onsager 1944 — exact solution, one of the most celebrated results in stat mech).

In 3D: phase transition at $k_BT_c/J \approx 4.512$ (numerical; no exact solution).

Substrate reading: the Ising spins are substrate Pin(2) K-types coupled to nearest-neighbor substrate K-types via $J$. Below $T_c$, the substrate's K-type couplings dominate over thermal fluctuations; spins align macroscopically.

### 8.4 Mean-field theory (Curie-Weiss)

For the Ising model: replace neighbor interactions with their mean. Each spin sees an effective field $h_{\text{eff}} = h + J z m$ where $z$ is the number of neighbors.

Self-consistency: $m = \tanh(\beta h_{\text{eff}}) = \tanh(\beta(h + Jzm))$.

For $h = 0$: $m = \tanh(\beta J z m)$. Solutions:
- $T > T_c^{MF} = Jz/k_B$: only $m = 0$ (disordered)
- $T < T_c^{MF}$: nonzero $\pm m$ solutions (ordered)

Near $T_c$: $m \propto (T_c - T)^{1/2}$ — mean-field critical exponent $\beta = 1/2$.

Mean-field is exact for infinite-range models, qualitatively correct for high dimensions, but quantitatively wrong for low-D systems with strong fluctuations. Renormalization group (Chapter 9) systematically corrects mean-field.

### 8.5 Landau theory: symmetry-breaking

Landau 1937: phenomenological framework for phase transitions. Free energy expansion in powers of order parameter $\phi$:

$$F(\phi, T) = F_0(T) + \frac{1}{2}a(T)\phi^2 + \frac{1}{4}b\phi^4 + \ldots$$

with $a(T) = a_0(T - T_c)$ changing sign at $T_c$.

For $T > T_c$: $a > 0$, minimum at $\phi = 0$ (disordered).
For $T < T_c$: $a < 0$, minimum at $\phi = \pm\sqrt{-a/b}$ (ordered, symmetry broken).

Landau's framework gives the universal mean-field critical exponents and provides a phenomenological basis for understanding broad classes of transitions.

Substrate reading: Landau's $\phi^4$ theory is the substrate's K-type cluster amplitude effective theory near $T_c$. The cubic-quartic balance is universal because it's the substrate's natural low-order expansion structure.

### 8.6 First-order transitions

For first-order transitions, the order parameter jumps from one value to another at $T_c$. Two phases coexist along the transition line (e.g., water and steam coexist at 100°C, 1 atm).

**Clausius-Clapeyron** (Chapter 4 Section 4.8): $dP/dT = L/(T \Delta V)$ along the coexistence curve.

**Latent heat**: $L = T(S_2 - S_1)$ — the energy needed to convert one phase to the other at constant $T, P$.

Substrate reading: first-order is the substrate's K-type cluster *discontinuous* reorganization — the two phases correspond to distinct K-type configurations with finite energy gap; thermodynamic potential has two equal minima at $T_c$.

### 8.7 Critical point: where first-order becomes second-order

For liquid-gas: the coexistence line ends at a critical point $(T_c, P_c)$ where liquid and gas become indistinguishable. Beyond the critical point: continuous transition (no phase separation).

For water: $T_c = 647$ K, $P_c = 22.1$ MPa.
For CO₂: $T_c = 304$ K, $P_c = 7.4$ MPa.

Near the critical point: critical phenomena dominate (Chapter 9). Density fluctuations diverge; correlation length $\xi \to \infty$; substance becomes opalescent (critical opalescence).

### 8.8 Universality classes

Different physical systems can share critical exponents if they share:
- Order parameter dimensionality
- Spatial dimensionality
- Range of interactions (short vs long)
- Underlying symmetries

**Universality classes**:
- 2D Ising: scalar order parameter, $d=2$ — exponents $\beta = 1/8$, $\gamma = 7/4$, $\nu = 1$
- 3D Ising: scalar order parameter, $d=3$ — exponents $\beta \approx 0.326$, $\gamma \approx 1.237$, $\nu \approx 0.630$
- 3D XY: 2-component order parameter — superfluid helium, superconductors
- 3D Heisenberg: 3-component order parameter — ferromagnets

Liquid-gas critical point belongs to 3D Ising class (scalar density order parameter).

Substrate reading: universality is the substrate's K-type cluster behavior being insensitive to microscopic details — what matters is the cluster symmetry and dimensionality.

### 8.9 Worked example: 2D Ising critical exponents

For 2D Ising:
- Order parameter: $m \propto (T_c - T)^{1/8}$ as $T \to T_c^-$ (Onsager 1944)
- Susceptibility: $\chi \propto |T - T_c|^{-7/4}$
- Specific heat: $C \propto -\ln|T - T_c|$ (logarithmic divergence)
- Correlation length: $\xi \propto |T - T_c|^{-1}$

These exponents are exact (Onsager). Mean-field would give $\beta = 1/2$, $\gamma = 1$, etc. — completely different from the true 2D values. Mean-field fails because 2D has strong fluctuations not captured by neighbor-mean averaging.

Substrate reading: in 2D the substrate's K-type cluster fluctuations are strong and non-Gaussian; mean-field's neighbor-averaging misses them. The RG (Chapter 9) systematically incorporates fluctuations.

### 8.10 Spontaneous symmetry breaking

When the order parameter is multi-component (e.g., 3D ferromagnet $\vec M$), the ordered phase chooses a specific direction in order-parameter space — the symmetry is *spontaneously broken*. The system's microscopic Hamiltonian has full rotational symmetry, but the ground state breaks it.

Consequences:
- **Goldstone bosons**: massless excitations for continuous broken symmetries (spin waves in ferromagnets, phonons in crystals — though phonons are subtler)
- **Topological defects**: vortices, domain walls, monopoles — singularities in the order parameter

Substrate reading: spontaneous symmetry breaking is the substrate's K-type cluster choosing one of multiple equivalent ground states. The Goldstone modes are the substrate's residual continuous K-type-cluster degrees of freedom.

### 8.11 K-audit anchors

- **Casey's Principle**: phase transitions are substrate counting transitions
- **Chapter 5 of this volume**: partition function (computational engine for $F$, hence for phase boundaries)
- **Chapter 9 of this volume**: critical phenomena and RG (next step)
- **Volume 9 Chapter 5**: topological phases (special class of phase transitions)

## Level 3 — 5th-grader accessibility

Water at 100°C boils. Iron at 770°C loses its magnetism (Curie point). Helium at 2.17 K becomes a superfluid. These are **phase transitions** — sudden changes in how matter is organized. **Order parameters** track the change: magnetization for ferromagnets, density difference for liquid-gas, condensate amplitude for superfluids. **First-order** transitions (like boiling water) have latent heat — energy is absorbed without temperature change. **Second-order** transitions (like ferromagnetic Curie point) have no latent heat but show critical phenomena (next chapter). The amazing thing: very different systems can share the same critical behavior (universality classes). Water near its critical point and a 3D Ising magnet near $T_c$ behave identically. In BST, phase transitions are the substrate's K-type clusters reorganizing — and universality reflects the substrate's indifference to microscopic details.

---

## What comes next

Chapter 9 develops critical phenomena and the renormalization group — including BST's 7-step cyclotomic cascade reading of RG (K59 ratified).

## Where to look this up

- **Ising model**: Ising 1925; Onsager 1944
- **Landau theory**: Landau 1937; Landau and Lifshitz, *Statistical Physics*
- **Universality**: Kadanoff 1966; Stanley, *Introduction to Phase Transitions and Critical Phenomena*
- **BST anchors**: Casey's Principle; Volume 9 topological phases
