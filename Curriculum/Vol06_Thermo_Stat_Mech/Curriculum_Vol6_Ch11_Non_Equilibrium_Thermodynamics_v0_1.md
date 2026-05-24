---
title: "Vol 6 Chapter 11 — Non-Equilibrium Thermodynamics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; entropy production; Onsager reciprocity; fluctuation theorems; substrate Zone 3 directional flow"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 11
load_bearing: "Non-equilibrium thermo as substrate cycle running in directed flow; Onsager reciprocity from substrate Zone 3 microreversibility; fluctuation theorems"
---

# Chapter 11 — Non-Equilibrium Thermodynamics

## Level 1 — one sentence

Non-equilibrium thermodynamics — entropy production, Onsager reciprocal relations, Jarzynski/Crooks fluctuation theorems, dissipation-fluctuation symmetry — is the substrate's 4-zone commitment cycle running in directed flow (with net Zone 1 input ≠ net Zone 4 output), and the central result is that the substrate's Zone 3 commitment is the *source* of all entropy production while the substrate's microreversibility at Scale 1 imposes the symmetries that Onsager (1931) noticed in macroscopic flows.

## Level 2 — graduate-physicist precision

### 11.1 Beyond equilibrium

Equilibrium thermodynamics (Chapters 1-9 of this volume) describes systems with no net flow — no temperature gradients, no chemical-potential gradients, no work being extracted. Real systems are usually *out of equilibrium*: heat conducts down gradients, currents flow, chemical reactions proceed.

Non-equilibrium thermodynamics describes:
- **Linear response**: small departures from equilibrium → linear relations between forces and flows (Ohm's law, Fick's diffusion, Fourier heat conduction)
- **Onsager reciprocal relations** (1931): symmetries in the linear coefficients
- **Far-from-equilibrium**: nonlinear, possibly with pattern formation, oscillations, chaos
- **Fluctuation theorems**: Jarzynski 1997, Crooks 1999 — exact non-perturbative relations connecting work distributions to free-energy differences

### 11.2 Entropy production

For a system out of equilibrium, the entropy production rate $\sigma > 0$ is the rate at which entropy is being created internally. Decompose total entropy change:

$$\frac{dS}{dt} = \sigma + \Phi$$

where $\sigma \ge 0$ is internal entropy production and $\Phi$ is entropy flow with the environment.

Substrate-mechanism reading: $\sigma$ is the substrate's Zone 3 commitment information-discard *rate* — the integral of Zone 3 commitment-completion across all substrate K-types undergoing commitment per unit time. Equilibrium: $\sigma = 0$ (no net Zone 3 commitment-completion at the macroscopic level). Non-equilibrium: $\sigma > 0$ (continuous Zone 3 commitment-completion driven by external boundary conditions).

### 11.3 Linear response: forces and flows

Near equilibrium, generalized forces $X_i$ (gradient of temperature, of chemical potential, electric field, etc.) drive generalized flows $J_i$ (heat current, particle current, electric current):

$$J_i = \sum_j L_{ij} X_j$$

with $L_{ij}$ the linear-response (Onsager) coefficients. Entropy production:

$$\sigma = \sum_i J_i X_i = \sum_{ij} L_{ij} X_i X_j$$

For $\sigma \ge 0$, the matrix $L_{ij}$ must be positive-semidefinite.

### 11.4 Onsager reciprocal relations

Onsager 1931 (Nobel 1968): for systems with microscopic reversibility (time-reversal symmetric microscopic dynamics), the linear-response coefficients satisfy

$$L_{ij} = L_{ji}$$

This is **Onsager reciprocity**. It connects seemingly unrelated transport coefficients (e.g., thermoelectric Seebeck and Peltier effects).

Substrate-mechanism derivation: substrate Zone 2 evolution is unitary (time-reversal symmetric at Scale 1). The macroscopic linear-response coefficients inherit this symmetry through the substrate's Scale 1 → Scale 2 averaging. Zone 3 commitment is the only non-reversible step; it doesn't affect the *coefficients* of linear response — it only affects the overall entropy production rate $\sigma > 0$.

### 11.5 Worked example: thermoelectric effects

Apply temperature gradient → electric current (Seebeck effect). Apply electric current → heat flow (Peltier effect). Onsager reciprocity: $L_{eT} = L_{Te}$ — the thermoelectric coupling is symmetric. Modern thermoelectric materials engineering relies on this.

Numerically: Seebeck coefficient $S = -L_{eT}/L_{ee}$, Peltier coefficient $\Pi = L_{Te}/L_{ee}$, with Kelvin relation $\Pi = ST$ — derivable from Onsager.

### 11.6 Fluctuation-dissipation theorem

The same coefficients $L_{ij}$ that govern macroscopic linear response also govern equilibrium fluctuations:

$$\langle J_i J_j\rangle_{\text{equilibrium}} = 2 k_B L_{ij}$$

(Green-Kubo formula). The substrate's K-type fluctuations and its dissipative response are two faces of the same K-type structure.

Substrate-mechanism: fluctuation ↔ dissipation is the substrate's K-type equilibrium symmetry; the substrate doesn't distinguish "spontaneous fluctuation" from "response to perturbation" at Scale 1.

### 11.7 Far from equilibrium: pattern formation

Sufficiently far from equilibrium, systems can exhibit:
- **Pattern formation**: Rayleigh-Bénard convection cells, Belousov-Zhabotinsky chemical waves, Turing patterns in reaction-diffusion
- **Oscillations**: limit cycles, period-doubling, chaos
- **Self-organization**: dissipative structures (Prigogine 1977 Nobel)

Substrate-mechanism: far-from-equilibrium systems have substrate K-type configurations that lock into self-sustaining cycles, where Zone 3 commitment outputs feed back into Zone 1 absorption inputs. The "structure" is the substrate's stable K-type cluster pattern under the imposed flow.

### 11.8 Fluctuation theorems

Jarzynski 1997, Crooks 1999: for a system driven away from equilibrium by an arbitrary protocol that ends at temperature $T$:

**Jarzynski equality**: $\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$ where $W$ is the work done in the process, $\Delta F$ is the equilibrium free energy difference between final and initial states.

**Crooks theorem**: $P(W) / P(-W)_{\text{reverse}} = e^{\beta(W - \Delta F)}$ — the forward and reverse work distributions are related by an exponential factor.

These are *exact, non-perturbative* relations valid arbitrarily far from equilibrium. Astonishing because they let you extract equilibrium $\Delta F$ from non-equilibrium experiments.

Substrate-mechanism reading: fluctuation theorems are the substrate's microreversibility expressed at the macroscopic-work level. Zone 2 unitarity preserves microreversibility; Zone 3 commitment-completion direction gives the "forward vs reverse" asymmetry.

### 11.9 Worked example: Brownian motion

A pollen grain in water exhibits Brownian motion — random diffusive walk due to molecular bombardment. Einstein 1905 derived the diffusion coefficient:

$$D = \frac{k_B T}{6\pi\eta r}$$

(for a sphere of radius $r$ in fluid of viscosity $\eta$). Mean-square displacement: $\langle x^2\rangle = 2Dt$ (1D).

This is the simplest non-equilibrium process: thermal forces drive diffusion; Einstein's formula relates the diffusion coefficient to viscous response — a fluctuation-dissipation result. Perrin 1908 confirmed experimentally and got Nobel for it.

Substrate reading: Brownian motion is the substrate's environmental K-type coupling driving the pollen-grain K-type to random K-type configurations. The substrate's commitment-completion under thermal coupling produces diffusive trajectories.

### 11.10 Second law strengthened

The fluctuation theorems strengthen the standard second law: not only $\langle \Delta S\rangle \ge 0$, but the probability of $\Delta S < 0$ events is exponentially suppressed:

$$\frac{P(\Delta S = -|s|)}{P(\Delta S = +|s|)} = e^{-|s|/k_B}$$

So entropy decreases are possible in microscopic systems for short times, but the larger or longer-time the event, the more exponentially unlikely it is. This is what reconciles microreversibility with macroscopic irreversibility.

Substrate reading: Zone 3 commitment-completion is statistically biased toward entropy increase, but not deterministically forbidden in reverse for short times / few substrate K-types. The bias scales with substrate K-type count, giving the exponential factor.

### 11.11 K-audit anchors

- **Casey's Principle**: entropy production = substrate counting under directed flow
- **Onsager 1931** (Nobel 1968): foundational microreversibility result
- **Jarzynski 1997, Crooks 1999**: modern non-equilibrium milestones
- **Volume 0 Chapter 3**: 4-zone commitment cycle (Zone 3 = entropy-production source)
- **DCCP** (Chapter 3 Section 3.5): multi-tick commitment-completion as entropy generator

## Level 3 — 5th-grader accessibility

Equilibrium thermodynamics is about systems at rest — same temperature everywhere, no flows, no work being done. **Non-equilibrium** thermodynamics is the much more common case: there's a temperature gradient driving heat flow, or a chemical gradient driving diffusion, or a voltage driving current. Two beautiful results:
- **Onsager reciprocity** (1931): if you apply force A and get flow B, and you apply force B and get flow A, the cross-coefficients are *equal*. Connects Seebeck (temp gradient → current) to Peltier (current → heat flow) — the basis of modern thermoelectric coolers.
- **Fluctuation theorems** (Jarzynski 1997, Crooks 1999): you can extract equilibrium free-energy differences from out-of-equilibrium experiments. The second law is *probabilistic* — entropy can decrease for short times in small systems, but the probability is exponentially small.

In BST: non-equilibrium is the substrate's 4-zone cycle running with directed flow. Entropy production = substrate Zone 3 commitment-completion rate. Onsager reciprocity comes from substrate Zone 2 microreversibility. Far from equilibrium, the substrate can lock into self-organizing patterns (Bénard cells, oscillating chemical reactions, even life).

---

## What comes next

Chapter 12 closes the volume: information theory and thermodynamics — Shannon-Boltzmann unification, Landauer's principle, substrate as information channel.

## Where to look this up

- **Onsager**: Onsager 1931 *Phys Rev*; de Groot and Mazur, *Non-Equilibrium Thermodynamics*
- **Jarzynski equality**: Jarzynski 1997 *Phys Rev Lett*
- **Crooks theorem**: Crooks 1999 *Phys Rev E*
- **Prigogine**: Prigogine 1977 Nobel lecture; Nicolis and Prigogine, *Self-Organization in Non-Equilibrium Systems*
- **BST anchors**: Casey's Principle; DCCP; Volume 0 Chapter 3
