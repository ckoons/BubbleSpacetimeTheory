---
title: "Vol 12 Chapter 4 — Chemical Reactions and Thermodynamics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 12 Chemistry from D_IV⁵"
chapter: 4
load_bearing: "Chemical equilibrium; ΔG and K_eq; standard reduction potentials; substrate K-type rearrangement"
---

# Chapter 4 — Chemical Reactions and Thermodynamics

## Level 1 — one sentence

Chemical reactions are substrate K-type rearrangements with thermodynamic state functions (Δ_rH, Δ_rS, Δ_rG) governing direction and equilibrium — ΔG° < 0 spontaneous; equilibrium constant $K = \exp(-\Delta G^\circ/RT)$ — and BST views the whole process as substrate count-maximization in chemical-K-type configuration space.

## Level 2 — graduate-physicist precision

### 4.1 Thermodynamic state functions

For a reaction $aA + bB \to cC + dD$:
- **Enthalpy** $\Delta_r H = \sum$ products − reactants (heat at constant P)
- **Entropy** $\Delta_r S = $ entropy change (count of microstates)
- **Gibbs free energy** $\Delta_r G = \Delta_r H - T \Delta_r S$ (driving force at constant T, P)

Spontaneous: $\Delta_r G < 0$. Equilibrium: $\Delta_r G = 0$.

### 4.2 Equilibrium constants

For ideal-gas reaction at constant $T$:

$$K_p(T) = \exp(-\Delta G^\circ/RT)$$

with $K_p = \prod (P_i/P^\circ)^{\nu_i}$ over products / reactants with stoichiometric coefficients $\nu_i$.

Le Chatelier: equilibrium shifts to counteract perturbations (add reactant → forward; raise T for endothermic → forward; etc.).

### 4.3 Standard reduction potentials

Half-cell reactions $\text{Ox} + n e^- \to \text{Red}$ have standard reduction potentials $E^\circ$ (relative to SHE = standard hydrogen electrode).

Cell potential: $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$.

Nernst: $E = E^\circ - (RT/nF)\ln Q$ — non-equilibrium concentrations.

Driving voltage of batteries, electrolysis, biochemical electron transport.

### 4.4 Examples

Hydrogen combustion: $H_2 + (1/2)O_2 \to H_2O$. $\Delta_r H = -286$ kJ/mol (highly exothermic). $\Delta_r G = -237$ kJ/mol. Drives fuel cells.

Photosynthesis: $6CO_2 + 6H_2O \to C_6H_{12}O_6 + 6O_2$. $\Delta_r G = +2870$ kJ/mol (non-spontaneous; driven by photon energy).

Glycolysis: glucose → 2 pyruvate + 2 ATP + 2 NADH. Net $\Delta G$ ≈ −146 kJ/mol; couples thermodynamics to biological energy storage.

### 4.5 Substrate-mechanism reading

Per Casey's Principle (Vol 6 Ch 1): entropy = force = counting at depth 0. Chemical reaction directions are substrate's K-type count gradients; equilibrium = substrate count-maximum given constraints.

### 4.6 K-audit anchors

- **Vol 6 Ch 1-4**: thermodynamics foundation
- **Casey's Principle** (memory)

## Level 3 — 5th-grader accessibility

**Chemical reactions**: bonds break, new bonds form. **Thermodynamics tells you direction**: $\Delta G = \Delta H - T \Delta S$ — if $\Delta G < 0$, reaction goes forward. **Equilibrium constant** $K = \exp(-\Delta G^\circ/RT)$. **Le Chatelier**: perturb equilibrium, it shifts to counteract. **Standard reduction potentials**: drive batteries and biology. **In BST**: reactions are substrate K-type rearrangements; thermodynamics is substrate counting.

---

## What comes next

Chapter 5 develops reaction kinetics and transition states.

## Where to look this up

- Atkins, *Physical Chemistry*
- BST: Vol 6 Ch 1-4
