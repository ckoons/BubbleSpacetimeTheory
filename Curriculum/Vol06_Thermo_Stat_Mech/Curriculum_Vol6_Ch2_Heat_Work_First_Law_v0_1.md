---
title: "Vol 6 Chapter 2 — Heat, Work, and the First Law"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; first law as Zone 1 + Zone 4 substrate exchanges"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 2
load_bearing: "First law dU = δQ − δW as substrate Zone 1 absorption + Zone 4 emission; exact differentials vs path functions"
---

# Chapter 2 — Heat, Work, and the First Law

## Level 1 — one sentence

The first law of thermodynamics $dU = \delta Q - \delta W$ is the substrate's energy conservation between cycle zones: $\delta Q$ is what comes in via Zone 1 absorption (plus Zone 3's environmental backflow), $\delta W$ is what goes out via Zone 4 emission, and $dU$ is the internal substrate K-type energy change.

## Level 2 — graduate-physicist precision

### 2.1 The first law: standard statement

For any closed system undergoing a process from state 1 to state 2:

$$\Delta U = Q - W$$

where $\Delta U = U_2 - U_1$ is the internal energy change (a state function), $Q$ is heat absorbed by the system, and $W$ is work done by the system on the environment. In infinitesimal form:

$$dU = \delta Q - \delta W$$

The $\delta$ notation (rather than $d$) emphasizes that heat $Q$ and work $W$ are *path functions*, not state functions — their values depend on the process, not just on the initial and final states. Only $U$ is a state function.

For quasi-static processes with simple compressive work:

$$\delta W = P \, dV$$

so $dU = \delta Q - P \, dV$. For irreversible processes, $\delta W \le P \, dV$ (with strict inequality for friction, viscous dissipation, etc.).

### 2.2 First law from the 4-zone substrate cycle

In the BST 4-zone commitment cycle per Koons tick (Volume 0 Chapter 3):

1. **Zone 1 (absorption)**: external boundary data → substrate K-type amplitude. Energy flowing into substrate from environment.
2. **Zone 2 (bulk)**: K-type amplitudes evolve unitarily under substrate Casimir. Internal energy redistribution, no net exchange with environment.
3. **Zone 3 (commitment)**: Bergman-kernel projection. Discards orthogonal components → environmental K-types (entropy production); commits to one outcome.
4. **Zone 4 (emission)**: K-type amplitudes → external boundary observables. Energy flowing out of substrate to environment.

Total energy balance per tick:

$$\Delta U_{\text{substrate}} = \underbrace{E_{\text{Zone 1}}^{\text{in}}}_{\text{heat absorbed }} + \underbrace{E_{\text{Zone 3}}^{\text{discard}}}_{\text{also heat-like}} - \underbrace{E_{\text{Zone 4}}^{\text{out}}}_{\text{work done}}$$

Identifying:
- $\delta Q = E_{\text{Zone 1}}^{\text{in}} + E_{\text{Zone 3}}^{\text{discard}}$ (heat absorbed = direct environmental absorption + discarded-branch backflow)
- $\delta W = E_{\text{Zone 4}}^{\text{out}}$ (work done = controlled emission to environment)

So:

$$\Delta U_{\text{substrate}} = \delta Q - \delta W$$

The first law of thermodynamics is the substrate's per-Koons-tick energy bookkeeping, averaged over many ticks at Scale 2.

### 2.3 Why $Q$ and $W$ are path functions (not state functions)

The first law's notation $\delta Q$ and $\delta W$ (not $dQ$ and $dW$) reflects that $Q$ and $W$ depend on the *process*, not just the endpoints. The same $\Delta U$ can be reached via different combinations of $Q$ and $W$.

Substrate-mechanism reading: each Koons tick's substrate cycle has Zone 1 absorption and Zone 4 emission split according to the cycle's *specific* boundary-condition timing. Different processes (slow vs fast, adiabatic vs isothermal) produce the same net $\Delta U$ but redistribute it across $Q$ and $W$ differently because they engage Zones 1-4 in different ratios.

This is why heat and work are path functions: they record the cycle-by-cycle Zone 1/Zone 4 partitioning history, not just the endpoint substrate K-type energies.

### 2.4 Heat as energy transfer via random K-type couplings

Heat $Q$ corresponds to energy transfer between substrate and environment that comes via *uncoordinated* K-type couplings — environmental K-types that the substrate cannot anticipate or control. This is the substrate's Zone 1 absorption from a thermal bath.

Formally: for a system in contact with environment at temperature $T$, the substrate absorbs energy from environmental K-types whose distribution is Boltzmann-thermal ($e^{-E/k_BT}$). The expected energy absorbed per Koons tick is

$$\langle \delta Q \rangle_{\text{per tick}} = \sum_\lambda E_\lambda \cdot P_{\text{env}}(\lambda) \cdot \gamma_\lambda$$

where $P_{\text{env}}(\lambda)$ is the environmental K-type population at the substrate-environment interface and $\gamma_\lambda$ is the substrate's coupling rate to K-type $\lambda$.

### 2.5 Work as energy transfer via coordinated K-type emission

Work $W$ corresponds to energy transfer that is *coordinated* — substrate Zone 4 emission to specific environmental K-types (e.g., piston pushing on gas wall, current flowing through resistor). The substrate Zone 4 emits to controllable environmental modes.

Formally: $\delta W = -\sum_i F_i \, dx_i$ where $x_i$ are macroscopic configuration variables and $F_i$ are conjugate forces (pressure × volume, surface tension × area, etc.). The substrate Zone 4 emission selects one configurational degree of freedom and transfers energy through it.

### 2.6 The PV work integral

For a gas expanding from volume $V_1$ to $V_2$ against external pressure $P_{\text{ext}}$:

$$W = \int_{V_1}^{V_2} P_{\text{ext}} \, dV$$

For quasi-static reversible processes, $P_{\text{ext}} = P_{\text{gas}}$ throughout, so $W = \int P \, dV$. For isothermal ideal gas expansion ($PV = nRT$, $T$ constant):

$$W_{\text{isothermal}} = nRT \ln(V_2 / V_1)$$

Substrate reading: each Koons tick of the gas-substrate emits to the piston wall's K-types with intensity proportional to the pressure; summing over all ticks during the expansion gives the integrated work.

### 2.7 Cyclic processes and engine efficiency

A cyclic process returns the system to its initial state, so $\oint dU = 0$. The first law gives:

$$\oint \delta Q = \oint \delta W$$

Net heat absorbed = net work done over the cycle. This is the basic principle of heat engines.

The Carnot cycle: reversible engine operating between hot reservoir at $T_h$ and cold at $T_c$. Carnot efficiency:

$$\eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h}$$

This is the maximum possible efficiency; no real engine can exceed it. Substrate-mechanism reading: $\eta_{\text{Carnot}} = 1$ would require zero entropy production (Zone 3 commitment with zero information loss), which is impossible because Zone 3 is the substrate's irreversible step.

### 2.8 Worked example: isothermal vs adiabatic ideal gas

Consider 1 mole of monoatomic ideal gas expanding from $(P_1, V_1, T_1) = (1\text{ atm}, 22.4\text{ L}, 273\text{ K})$ to volume $V_2 = 44.8\text{ L}$:

**Isothermal** ($T$ constant via heat absorption):
- $W = nRT \ln(V_2/V_1) = (1)(8.314)(273)\ln(2) \approx 1573$ J
- $\Delta U = 0$ (ideal gas, $T$ constant)
- $Q = W \approx 1573$ J (all work done by absorbing heat)
- Substrate reading: substrate maintains thermal coupling to environment throughout; Zone 1 absorption equals Zone 4 emission, no net $\Delta U$.

**Adiabatic** ($Q = 0$, no heat exchange):
- $T_2 = T_1 (V_1/V_2)^{\gamma - 1}$ where $\gamma = 5/3$ for monoatomic; $T_2 = 273 \cdot (1/2)^{2/3} \approx 172$ K
- $\Delta U = (3/2)nR(T_2 - T_1) = (3/2)(8.314)(-101) \approx -1260$ J
- $W = -\Delta U \approx 1260$ J (all work done by reducing internal energy)
- Substrate reading: substrate is decoupled from thermal environment (no Zone 1 absorption); Zone 4 emission draws on Zone 2 internal energy; substrate cools.

Different processes, same volume change, very different $Q$ and $W$. State function $\Delta U$ depends only on $\Delta T$.

### 2.9 K-audit anchors and connections

- **Casey's Principle** (memory `feedback_caseys_principle.md`): entropy = force = counting at depth 0 — first law's $dU$ is the substrate's count-of-microstates energy change
- **Volume 0 Chapter 3**: 4-zone commitment cycle (foundation for energy bookkeeping)
- **Volume 5 Chapter 4 Section 4.2**: substrate Hamiltonian; per-tick energy evolution

## Level 3 — 5th-grader accessibility

**Energy is conserved**: if you take heat in and do work out, the difference is what's left over inside. That's the first law. In BST, the substrate has a 4-step cycle every Koons tick. **Heat** ($Q$) is energy flowing in through step 1 (absorption) from random environmental jostles. **Work** ($W$) is energy flowing out through step 4 (emission) in a controlled way, like pushing on a piston. The difference is what's left in the substrate's internal energy ($\Delta U$). Heat and work are "path functions": how much heat vs. how much work depends on *how* you change the system, not just where you start and end. Same gas, expanded the same amount, gives different heat-vs-work numbers depending on whether you keep the temperature constant (isothermal) or insulate it (adiabatic). The substrate is doing different Zone 1 vs Zone 4 work in each case.

---

## What comes next

Chapter 3 develops entropy and the second law — including the BST reading of entropy as the substrate's information-discard rate in Zone 3 commitment.

## Where to look this up

- **First law**: Callen Ch 1-2; Fermi, *Thermodynamics*
- **Carnot cycle**: Carnot 1824, *Reflections on the Motive Power of Fire*
- **Casey's Principle**: memory `feedback_caseys_principle.md`
- **Volume 0 Chapter 3**: 4-zone commitment cycle
- **Volume 5 Chapter 4**: substrate Hamiltonian per-tick energy
