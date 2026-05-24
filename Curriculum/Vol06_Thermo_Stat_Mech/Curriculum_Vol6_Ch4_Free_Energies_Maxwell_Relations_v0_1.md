---
title: "Vol 6 Chapter 4 — Free Energies and Maxwell Relations"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Legendre transforms on substrate Casimir"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 4
load_bearing: "Helmholtz F = U − TS, Gibbs G = H − TS as Legendre transforms; Maxwell relations as substrate boundary-condition exchange symmetries"
---

# Chapter 4 — Free Energies and Maxwell Relations

## Level 1 — one sentence

Free energies (Helmholtz $F = U - TS$, Gibbs $G = H - TS$, enthalpy $H = U + PV$, grand potential $\Phi = F - \mu N$) are Legendre transforms of the substrate's per-Koons-tick internal energy adapted to different externally-fixed boundary conditions, and Maxwell relations are exchange symmetries between the resulting second partial derivatives.

## Level 2 — graduate-physicist precision

### 4.1 The Legendre transform

Given a function $U(S, V, N)$ — internal energy as function of natural variables — the Legendre transform exchanges one independent variable for its conjugate. Define:

- $T = (\partial U/\partial S)_{V, N}$ (temperature)
- $P = -(\partial U/\partial V)_{S, N}$ (pressure)
- $\mu = (\partial U/\partial N)_{S, V}$ (chemical potential)

Legendre transforms:

- **Helmholtz free energy**: $F(T, V, N) = U - TS$, useful when $T$ is controlled by thermal contact
- **Enthalpy**: $H(S, P, N) = U + PV$, useful when $P$ is controlled (constant pressure)
- **Gibbs free energy**: $G(T, P, N) = U - TS + PV = H - TS$, useful for $T$ and $P$ both controlled
- **Grand potential**: $\Phi(T, V, \mu) = U - TS - \mu N = F - \mu N$, useful when $\mu$ controlled (open system)

The natural variables for each potential are the ones held fixed in the relevant experimental ensemble.

### 4.2 Substrate-mechanism reading of free energies

In BST: the substrate's per-tick energy bookkeeping is internal energy $U$. The free energies are bookkeeping forms adapted to which boundary conditions the substrate is exchanging with at each Zone.

- $U(S, V, N)$ — substrate isolated; full microcanonical accounting
- $F(T, V, N) = U - TS$ — substrate in thermal contact with environment at $T$; the $-TS$ subtracts environmental entropy contribution
- $H(S, P, N) = U + PV$ — substrate in volume contact (expanding against pressure $P$); $PV$ work is part of effective energy
- $G(T, P, N) = U - TS + PV$ — both thermal and volume contact; the most-used potential for chemistry and condensed-matter equilibria

Each Legendre transform corresponds to a different way the substrate's Zone 1-4 cycle interfaces with the environment.

### 4.3 First-derivative relations

From the definitions:

$$dU = T dS - P dV + \mu dN$$
$$dF = -S dT - P dV + \mu dN$$
$$dH = T dS + V dP + \mu dN$$
$$dG = -S dT + V dP + \mu dN$$
$$d\Phi = -S dT - P dV - N d\mu$$

Each gives first-derivative relations like $(\partial F/\partial T)_{V,N} = -S$, $(\partial G/\partial T)_{P,N} = -S$, $(\partial G/\partial P)_{T,N} = V$, etc.

### 4.4 Maxwell relations

The second-derivative cross terms must commute (equality of mixed partials for smooth thermodynamic potentials). Applying to $G(T, P, N)$:

$$\left(\frac{\partial S}{\partial P}\right)_{T,N} = -\left(\frac{\partial V}{\partial T}\right)_{P,N}$$

This is one of the **Maxwell relations**. The full set (four classical Maxwell relations from $U, F, H, G$):

$$\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V \quad \text{(from } U\text{)}$$

$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V \quad \text{(from } F\text{)}$$

$$\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P \quad \text{(from } H\text{)}$$

$$\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P \quad \text{(from } G\text{)}$$

Substrate-mechanism reading: each Maxwell relation expresses the substrate's exchange symmetry between two boundary conditions. Mixed partials commute because the substrate's K-type counting is path-independent at the equilibrium level.

### 4.5 Equilibrium criteria

For a system in contact with environment, the equilibrium condition minimizes the appropriate free energy:

- **Isolated** ($U$ fixed): maximize $S$
- **Constant $T, V$**: minimize $F$
- **Constant $T, P$**: minimize $G$
- **Constant $T, \mu$**: minimize $\Phi$

Substrate-mechanism: equilibrium is the substrate's K-type configuration that maximizes count of substrate-environment combined microstates compatible with the imposed boundary conditions. The free-energy formula is the bookkeeping that makes this maximization condition simplest in each ensemble.

### 4.6 Worked example: ideal gas free energies

For monatomic ideal gas: $U = (3/2) N k_B T$, $PV = N k_B T$, so $H = (5/2) N k_B T$.

Entropy (Sackur-Tetrode, Chapter 3 Section 3.10): $S = N k_B [5/2 + \ln(V/N (2\pi m k_B T / h^2)^{3/2})]$.

Helmholtz free energy:

$$F = U - TS = N k_B T \left[1 - \ln\left(\frac{V}{N}\left(\frac{2\pi m k_B T}{h^2}\right)^{3/2}\right)\right]$$

Pressure from $F$: $P = -(\partial F/\partial V)_{T, N} = N k_B T / V$ — recovers ideal gas law.

Chemical potential from $F$: $\mu = (\partial F/\partial N)_{T, V} = -k_B T \ln(V/N (2\pi m k_B T / h^2)^{3/2})$.

Gibbs free energy: $G = F + PV = -N k_B T \ln(V/N (2\pi m k_B T / h^2)^{3/2}) = N \mu$ — exposes the relation $G = N \mu$ for single-component systems (Euler's equation for thermodynamic potentials).

### 4.7 Chemical equilibrium and the law of mass action

For a reaction $aA + bB \rightleftharpoons cC + dD$ at constant $T, P$: equilibrium minimizes $G$, giving

$$\frac{(P_C/P^\circ)^c (P_D/P^\circ)^d}{(P_A/P^\circ)^a (P_B/P^\circ)^b} = K_p(T)$$

with $K_p = \exp(-\Delta G^\circ / RT)$ the equilibrium constant. Standard chemistry; the substrate-mechanism is the Gibbs-energy minimization principle expressing the substrate's count-maximization in the chemical-K-type configuration space.

### 4.8 Worked example: Clausius-Clapeyron equation

For two phases (e.g., liquid-vapor) in equilibrium: chemical potentials equal, $\mu_l(T, P) = \mu_g(T, P)$. Along the coexistence curve, $d\mu_l = d\mu_g$:

$$-S_l dT + V_l dP = -S_g dT + V_g dP$$

$$\frac{dP}{dT} = \frac{S_g - S_l}{V_g - V_l} = \frac{L}{T \Delta V}$$

where $L = T(S_g - S_l)$ is the latent heat of vaporization. The Clausius-Clapeyron equation gives the slope of the coexistence curve.

For water at boiling: $L \approx 2260$ J/g, $T = 373$ K, $\Delta V \approx 1671$ cm³/g (vapor much larger than liquid). $dP/dT \approx 2.7 \times 10^4$ Pa/K — boiling temperature increases by ~3.7°C per atmosphere of additional pressure. Substrate reading: the latent heat is the substrate's K-type-restructuring energy in going from liquid (correlated K-types) to vapor (uncorrelated K-types).

### 4.9 K-audit anchors

- **Casey's Principle**: equilibrium is substrate counting at depth 0
- **Volume 0 Chapter 3**: 4-zone commitment cycle (substrate-environment exchange basis)
- **Volume 5 Chapter 4 Section 4.2**: substrate Hamiltonian (basis for $U$)
- **Chapter 5 of this volume**: partition function (computational engine for free energies)

## Level 3 — 5th-grader accessibility

Internal energy $U$ tells you the substrate's total energy. But you don't always control all the variables — sometimes the temperature is set by a thermostat, sometimes the pressure is fixed at atmosphere. **Free energies** are reformulations of $U$ adapted to different experimental setups. Think of them like different currencies: dollars, euros, yen — same value, different units depending on which country (boundary condition) you're in. **Helmholtz $F = U - TS$** is the currency for "fixed temperature." **Gibbs $G = H - TS$** is the currency for "fixed temperature AND fixed pressure" — most chemistry uses this one. **Maxwell relations** are equations that say "if you swap two of these conversions, you get the same answer either way." Useful because they let you compute one thing (like entropy change with pressure) from a measurable thing (like volume change with temperature). All of it boils down to the substrate counting K-type configurations — the free energies just reorganize the counting for different boundary conditions.

---

## What comes next

Chapter 5 develops the partition function — the load-bearing chapter of this volume, where $Z(\beta) = \text{Tr}\,e^{-\beta H_{\text{sub}}}$ on the Bergman Hilbert space equals the heat kernel on $D_{IV}^5$, anchoring Paper #9's arithmetic-triangle structure.

## Where to look this up

- **Free energies**: Callen, Ch 5-6
- **Maxwell relations**: Callen, Ch 7
- **Clausius-Clapeyron**: Callen, Ch 9
- **BST anchors**: Casey's Principle; Volume 0 Chapter 3
