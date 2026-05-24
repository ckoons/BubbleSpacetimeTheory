---
title: "Vol 12 Chapter 5 — Reaction Kinetics and Transition States"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 12 Chemistry from D_IV⁵"
chapter: 5
load_bearing: "Arrhenius rate law; transition state theory; Eyring equation; activation energy as substrate K-type saddle"
---

# Chapter 5 — Reaction Kinetics and Transition States

## Level 1 — one sentence

Reaction kinetics describes how fast chemical reactions proceed, with Arrhenius rate law $k = A e^{-E_a/RT}$ giving exponential temperature dependence and Eyring transition state theory $k = (k_B T/h)\exp(-\Delta G^\ddagger/RT)$ providing the substrate-K-type-saddle interpretation: the substrate K-type configuration passes through a transient saddle-point (transition state) to reach products.

## Level 2 — graduate-physicist precision

### 5.1 Rate laws

Empirical rate law: $r = k [A]^a [B]^b$ with reaction order $a + b$.

First-order: $r = k[A]$ → exponential decay $[A](t) = [A]_0 e^{-kt}$. Half-life $t_{1/2} = \ln 2/k$.

Second-order: $r = k[A]^2$ → $1/[A] - 1/[A]_0 = kt$. Half-life depends on $[A]_0$.

### 5.2 Arrhenius equation

$$k(T) = A \exp(-E_a/RT)$$

with $A$ pre-exponential factor (related to collision frequency, orientation), $E_a$ activation energy.

Empirical: most reactions show Arrhenius behavior over moderate T range. Plot $\ln k$ vs $1/T$ → slope $= -E_a/R$.

For $E_a \sim 100$ kJ/mol (typical organic chemistry): rate doubles per ~10 K temperature increase near room temperature.

### 5.3 Transition state theory (Eyring)

Eyring 1935: reaction passes through activated complex (transition state) at saddle point of potential energy surface.

$$k = \kappa \cdot \frac{k_B T}{h} \exp(-\Delta G^\ddagger/RT)$$

with $\kappa$ transmission coefficient (often ~1), $\Delta G^\ddagger$ activation free energy.

Decomposing: $\Delta G^\ddagger = \Delta H^\ddagger - T \Delta S^\ddagger$. Different from Arrhenius $E_a$ by $\Delta S^\ddagger$ contribution.

### 5.4 Substrate-mechanism reading

Transition state = substrate K-type saddle-point configuration. Activation energy = substrate K-type energy gap from reactant to saddle.

Catalysts work by providing alternative substrate K-type path with lower saddle. Enzymes (next chapter) lower activation energy by ~$10^7$ vs uncatalyzed.

### 5.5 K-audit anchors

- **Vol 6 Ch 11**: non-equilibrium thermodynamics
- **Vol 8 Ch 11**: chaos/dynamical systems (related transition state perspective)

## Level 3 — 5th-grader accessibility

**Reaction kinetics**: how fast reactions go. **Arrhenius**: $k = A e^{-E_a/RT}$ — exponential T dependence. Higher T → faster. Activation energy $E_a$ = barrier. **Transition state theory** (Eyring): reaction passes through high-energy saddle point. **Catalysts** lower the saddle → speed up reaction. **Enzymes** are biological catalysts that speed reactions by $\sim 10^7$. In BST: transition state = substrate K-type saddle configuration; catalyst = alternative substrate K-type path.

---

## What comes next

Chapter 6 develops spectroscopy as substrate cartography.

## Where to look this up

- Steinfeld-Francisco-Hase, *Chemical Kinetics and Dynamics*
- BST: Vol 6 Ch 11
