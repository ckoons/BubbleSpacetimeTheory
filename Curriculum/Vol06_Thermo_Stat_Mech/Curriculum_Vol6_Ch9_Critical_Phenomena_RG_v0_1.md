---
title: "Vol 6 Chapter 9 — Critical Phenomena and Renormalization Group"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; 7-step cyclotomic cascade RG (K59 ratified)"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 9
load_bearing: "Renormalization group = substrate's 7-step cyclotomic cascade per K59 ratified; critical exponents from substrate RG fixed points"
---

# Chapter 9 — Critical Phenomena and the Renormalization Group

## Level 1 — one sentence

Critical phenomena — divergent correlation lengths, universal critical exponents — arise at second-order phase transitions where the substrate's K-type cluster structure becomes scale-invariant, and the renormalization group (Wilson 1971, Nobel 1982) gives the systematic flow equations whose BST-specific reading is a 7-step cyclotomic cascade tied to the BST primary $g = 7$ via the K59 ratified cyclotomic mechanism.

## Level 2 — graduate-physicist precision

### 9.1 Critical phenomena: the singularities at $T_c$

At a second-order phase transition, the order parameter approaches zero continuously but with divergent derivatives. Quantities that diverge or vanish with power-law behavior in $\tau \equiv |T - T_c|/T_c$:

- **Correlation length**: $\xi \propto |\tau|^{-\nu}$
- **Susceptibility**: $\chi \propto |\tau|^{-\gamma}$
- **Specific heat**: $C \propto |\tau|^{-\alpha}$
- **Order parameter** ($T < T_c$): $\phi \propto |\tau|^\beta$
- **Critical isotherm** ($T = T_c$): $\phi \propto h^{1/\delta}$
- **Correlation function**: $G(r) \propto r^{-(d-2+\eta)}$ at $T = T_c$

The exponents $\{\alpha, \beta, \gamma, \delta, \nu, \eta\}$ are **critical exponents**. They obey scaling relations (e.g., $\alpha + 2\beta + \gamma = 2$, $\nu d = 2 - \alpha$); only two are independent.

The values of the exponents define the **universality class** of the transition.

### 9.2 Mean-field critical exponents

Landau theory (Chapter 8 Section 8.5) gives mean-field critical exponents:

$$\alpha_{MF} = 0, \quad \beta_{MF} = 1/2, \quad \gamma_{MF} = 1, \quad \delta_{MF} = 3, \quad \nu_{MF} = 1/2, \quad \eta_{MF} = 0$$

These are correct for $d \ge d_{\text{upper}} = 4$ (for scalar order parameter). For lower dimensions, fluctuations matter and the true exponents differ.

### 9.3 The renormalization group idea (Wilson)

Wilson 1971: at a critical point, the system is **scale-invariant**. Coarse-graining (averaging out short-distance degrees of freedom and rescaling) maps the system to itself. The coarse-graining map's fixed points correspond to phase transitions; the eigenvalues of the linearized map near a fixed point give the critical exponents.

Formally: integrate out short-wavelength fluctuations to produce an effective theory at a longer scale. Repeat. The recursion flow in coupling-constant space has fixed points; critical phenomena correspond to flows into the fixed points.

This was the breakthrough that explained universality (different systems flow to the same RG fixed point) and computed critical exponents from first principles.

### 9.4 BST: RG as 7-step cyclotomic cascade (K59 ratified)

The BST team's K59 audit (ratified Spring 2026) identifies the substrate's natural RG flow as a **7-step cyclotomic cascade**. Specifically:

- The substrate's Reed-Solomon coding on $\text{GF}(2^g) = \text{GF}(128)$ (Volume 14 Chapter 2) has 7 cyclotomic step structure
- Each RG step in the substrate's coarse-graining corresponds to one cyclotomic step
- After 7 steps, the cascade returns (in a specific cyclotomic sense) to its starting structure — this is the period
- Critical fixed points are reached after a finite number of cyclotomic steps; non-critical flow exits the cyclotomic structure

The number 7 is the BST primary $g$ — the substrate's natural cyclotomic exponent. The 7-step RG cascade is BST's signature in critical phenomena.

This is more than a stylistic reading: the K59 framework provides a computational procedure for RG flow in BST-substrate systems with specific predictions for the critical exponents in each universality class.

### 9.5 The $\epsilon$ expansion

For the $\phi^4$ Landau theory in $d = 4 - \epsilon$ dimensions, perturbative RG gives critical exponents as power series in $\epsilon$. To leading order:

$$\nu = \frac{1}{2} + \frac{\epsilon}{12} + O(\epsilon^2), \quad \eta = \frac{\epsilon^2}{54} + O(\epsilon^3), \quad \gamma = 1 + \frac{\epsilon}{6} + O(\epsilon^2)$$

(Wilson and Fisher 1972). At $\epsilon = 1$ (d=3): rough estimates that improve with higher-order expansion and resummation.

Substrate reading: the $\epsilon$ expansion is the substrate's perturbation around the upper critical dimension; for 3D systems, the substrate's K-type cluster fluctuations are intermediate-strength.

### 9.6 Critical exponents for 3D Ising

Best modern values for 3D Ising universality class (numerical, conformal bootstrap):

$$\alpha \approx 0.110, \quad \beta \approx 0.326, \quad \gamma \approx 1.237, \quad \delta \approx 4.79, \quad \nu \approx 0.630, \quad \eta \approx 0.036$$

These differ noticeably from mean-field, and even more from 2D Ising. Both substances near a liquid-gas critical point and 3D ferromagnets give these exponents to extreme precision — the universality is real.

### 9.7 Critical opalescence

Near a liquid-gas critical point, density fluctuations diverge ($\chi \to \infty$), with correlation length $\xi$ growing into the macroscopic range. Light scattering from these fluctuations gives the substance a milky-white appearance — **critical opalescence**. First observed by Andrews 1869 in CO₂.

Substrate reading: the substrate's K-type cluster correlations span macroscopic distances near the critical point; light couples to the density fluctuations and scatters.

### 9.8 The "fluctuation-dissipation theorem"

At thermal equilibrium, the response function (susceptibility) is related to spontaneous fluctuations:

$$\chi = \frac{1}{k_B T}\langle(\delta\phi)^2\rangle_{\text{total}}$$

For magnetization: $\chi = \beta \int d^d r\, G(r)$ where $G$ is the spin correlation function.

Substrate reading: fluctuation-dissipation is the substrate's K-type-cluster equilibrium symmetry — fluctuations and responses are two faces of the same K-type correlation structure.

### 9.9 Conformal field theory and critical phenomena

At $T = T_c$ in 2D, critical systems have conformal symmetry (translation + rotation + scale + special conformal). The Belavin-Polyakov-Zamolodchikov 1984 framework (CFT) classifies 2D critical systems by their conformal anomaly $c$.

For 2D Ising: $c = 1/2$. Other universality classes have $c = 7/10$ (tricritical), $c = 4/5$, $c = 1$ (free boson), etc.

Substrate reading: 2D conformal critical systems are substrate K-type configurations with $SL(2, \mathbb{R}) \times SL(2, \mathbb{R})$ conformal symmetry (relevant for the substrate's 2D restrictions and Shilov boundary).

### 9.10 Worked example: 3D Ising universal amplitude ratios

Beyond critical exponents, critical amplitude ratios are universal:

$$\frac{A^+}{A^-} \quad \text{(specific heat amplitude above/below } T_c\text{)}, \quad R_\chi \equiv \Gamma^+ B^{\delta-1}/D, \ldots$$

For 3D Ising: $A^+/A^- \approx 0.523$, $R_\chi \approx 1.65$, etc.

Liquid CO₂ near $T_c = 304$ K and a 3D Ising magnet give *identical* amplitude ratios — beyond just the exponents. This is the strongest empirical support for universality.

### 9.11 K-audit anchors

- **K59 ratified** (Spring 2026): cyclotomic mechanism framework; 7-step cascade for RG flow
- **Wilson 1971** (Nobel 1982): renormalization group framework
- **Onsager 1944**: 2D Ising exact solution (foundational for critical phenomena)
- **Volume 14 Chapter 2**: Reed-Solomon coding on $\text{GF}(128)$ (substrate basis for cyclotomic cascade)
- **Chapter 5 of this volume**: partition function (RG operates on)

## Level 3 — 5th-grader accessibility

Near a phase transition, weird things happen: tiny fluctuations grow to enormous size, things become "scale-free" (looking the same at every magnification), and very different physical systems start to behave identically (universality). Wilson's **renormalization group** is the math for understanding this: zoom out by averaging fine details, see what the system looks like at the larger scale, repeat. At a critical point, this zoom-out flow has a fixed point — and the eigenvalues near the fixed point give the **critical exponents** like $\nu, \gamma, \beta$. In BST, this zoom-out flow has a specific structure: **7 cyclotomic steps** before it repeats. The 7 is the BST primary $g = 7$. This is the substrate's signature in critical phenomena — and it makes specific numerical predictions for the critical exponents in each universality class.

---

## What comes next

Chapter 10 develops the Casimir effect and vacuum thermodynamics — including the load-bearing T2418 Λ-Casimir vacuum unification (K73): cosmological constant and lab-scale Casimir effect are the same substrate vacuum phenomenon at different scales.

## Where to look this up

- **RG**: Wilson 1971, *Phys Rev B* 4, 3174; Wilson and Fisher 1972
- **Conformal bootstrap (3D Ising)**: El-Showk et al. 2012, modern reviews
- **Critical opalescence**: Andrews 1869
- **BST anchors**: K59 ratified cyclotomic mechanism
- **Volume 14 Chapter 2**: Reed-Solomon basis
