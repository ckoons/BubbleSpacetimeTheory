---
title: "Vol 7 Chapter 11 — Plasma and Magnetohydrodynamics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; plasma physics; MHD; Alfvén waves; substrate ionized-gas K-type behavior"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 11
load_bearing: "Plasma physics — fourth state of matter; MHD equations; Alfvén waves; magnetic reconnection; astrophysical applications"
---

# Chapter 11 — Plasma and Magnetohydrodynamics

## Level 1 — one sentence

Plasma — ionized gas, the fourth state of matter and the most common form of ordinary matter in the universe — couples mechanics to EM through the Lorentz force on charged particles, with the MHD (magnetohydrodynamic) approximation treating plasma as a conducting fluid, supporting characteristic Alfvén waves and magnetic reconnection that explain phenomena from solar flares to fusion reactors.

## Level 2 — graduate-physicist precision

### 11.1 What plasma is

A **plasma** is an ionized gas containing roughly equal numbers of positive ions and negative electrons (quasineutral). Plasma forms when:
- Temperature is high enough to ionize: $k_BT \gtrsim $ ionization energy (~ eV for hydrogen)
- Density is low enough that ionization survives recombination

Plasma is the most abundant form of ordinary matter in the universe: stars (interior + corona), interstellar medium, intergalactic medium, accretion disks, lightning, fluorescent lamps, fusion reactors.

Key plasma parameters:
- **Plasma frequency**: $\omega_p = \sqrt{ne^2/(\epsilon_0 m_e)}$ (response timescale)
- **Debye length**: $\lambda_D = \sqrt{\epsilon_0 k_BT/(ne^2)}$ (screening distance)
- **Plasma parameter**: $\Lambda = n\lambda_D^3$ (number of particles in Debye sphere)

For typical hydrogen plasma at $n = 10^{20}$ m³, $T = 1$ keV: $\omega_p \approx 5.6 \times 10^{11}$ rad/s, $\lambda_D \approx 7 \times 10^{-5}$ m, $\Lambda \approx 10^7$ (good plasma approximation).

### 11.2 Single-particle motion

A charged particle in static fields:
- $\vec E$ only: linear acceleration
- $\vec B$ only: circular gyration in plane perpendicular to $\vec B$ at gyrofrequency $\omega_c = qB/m$, radius $r_L = v_\perp/\omega_c$ (Larmor radius)
- Both: $\vec E \times \vec B$ drift in addition to gyration

Adiabatic invariants:
- Magnetic moment $\mu = mv_\perp^2/(2B)$ — invariant if $B$ changes slowly compared to gyration
- Particle bouncing between magnetic mirrors (basis of magnetic confinement)

### 11.3 MHD equations

For plasma with characteristic scales large compared to $\lambda_D$ and timescales long compared to $1/\omega_p$, the **MHD approximation** treats plasma as a single conducting fluid:

- **Continuity**: $\partial_t \rho + \nabla \cdot (\rho \vec v) = 0$
- **Momentum**: $\rho(\partial_t + \vec v \cdot \nabla)\vec v = -\nabla P + \vec J \times \vec B$
- **Ohm's law**: $\vec E + \vec v \times \vec B = \eta \vec J$ ($\eta$ resistivity; ideal MHD has $\eta = 0$)
- **Faraday + Ampère**: Maxwell's equations (with displacement current usually negligible in MHD)
- **Energy**: equation of state, e.g., adiabatic $P\rho^{-\gamma} = $ const

Ideal MHD ($\eta = 0$): magnetic field is "frozen-in" to the plasma — fluid elements carry their magnetic flux as they move.

### 11.4 Alfvén waves

In ideal MHD, transverse magnetic-field perturbations propagate as **Alfvén waves** at speed:

$$v_A = B/\sqrt{\mu_0 \rho}$$

The Alfvén speed depends on magnetic field strength and plasma density. Solar corona: $v_A \sim 10^6$ m/s. Earth's magnetotail: $v_A \sim 10^5$ m/s.

Three MHD wave modes:
- **Alfvén waves** (transverse, incompressible)
- **Slow magnetosonic waves** (compressible, $\vec B$ and density coupled)
- **Fast magnetosonic waves** (compressible, faster than Alfvén)

Substrate reading: Alfvén waves are substrate K-type collective oscillations of the plasma's magnetic-K-type cluster.

### 11.5 Magnetic reconnection

In ideal MHD, field-line topology is conserved. With finite resistivity, field lines can break and reconnect, releasing magnetic energy as kinetic + thermal:

$$\partial_t \vec B = \nabla \times (\vec v \times \vec B) + (\eta/\mu_0) \nabla^2 \vec B$$

(induction equation with resistive term).

Sweet-Parker reconnection rate: $v_{in}/v_A \sim 1/\sqrt{S}$ where $S = \mu_0 L v_A / \eta$ is the Lundquist number. Often too slow for observations.

Petschek reconnection (faster) and recent collisionless reconnection theories improve agreement.

Applications:
- Solar flares (sudden release of magnetic energy in corona)
- Earth's magnetosphere (reconnection at magnetopause and magnetotail)
- Tokamak disruptions (rapid reconnection events)
- Fast reconnection critical to all these

### 11.6 Fusion plasma confinement

Two main approaches to controlled thermonuclear fusion:
- **Magnetic confinement** (tokamak, stellarator, MTF): confine hot plasma in magnetic field at low density for long time. ITER, EAST, JET, KSTAR.
- **Inertial confinement** (ICF, NIF): compress small DT pellet rapidly to fusion conditions. NIF crossed energy break-even Dec 2022.

Lawson criterion: $n T \tau_E > 3 \times 10^{21}$ keV·s/m³ for DT fusion. Both approaches struggle with edge instabilities, energy losses, materials degradation.

### 11.7 Astrophysical plasmas

Most matter in the universe is plasma:
- **Stellar interiors**: $T \sim 10^7$ K, fully ionized H, He plasma
- **Solar corona**: $T \sim 10^6$ K, low density
- **Interstellar medium**: $T \sim 10^2 - 10^7$ K, low density ($\sim 1$ cm⁻³)
- **Accretion disks**: very hot, magnetized; central engines of AGN, X-ray binaries
- **Pulsar magnetospheres**: extreme magnetic fields ($\sim 10^8$ T), relativistic plasmas

Substrate reading: cosmic-scale plasmas are substrate K-type configurations at cosmological Scale 3; their MHD behavior is the substrate's coarse-grained EM-coupled fluid dynamics.

### 11.8 Worked example: solar plasma

Solar corona at typical loop: $n \sim 10^{15}$ m⁻³, $T \sim 10^6$ K, $B \sim 10^{-3}$ T.

- Plasma frequency: $\omega_p = \sqrt{(10^{15})(1.6\times10^{-19})^2/(8.85\times10^{-12}\cdot 9.1\times10^{-31})} \approx 1.8 \times 10^9$ rad/s
- Debye length: $\lambda_D = \sqrt{(8.85\times10^{-12})(1.38\times10^{-23})(10^6)/[(10^{15})(1.6\times10^{-19})^2]} \approx 7\times10^{-3}$ m = 7 mm
- Alfvén speed: $v_A = B/\sqrt{\mu_0\rho} \approx 10^{-3}/\sqrt{(4\pi\times10^{-7})(10^{15}\cdot 1.7\times10^{-27})} \approx 7\times10^5$ m/s

Solar flare reconnection releases ~10²⁵ J in seconds — about 10⁻⁶ of solar surface output per second from a localized region.

### 11.9 K-audit anchors

- **Chapter 10** (EM in matter, dielectric response)
- **Volume 6 Chapter 11** (non-equilibrium thermo; MHD as non-equilibrium fluid)
- **Volume 4** (GR/Cosmology; astrophysical plasmas)

## Level 3 — 5th-grader accessibility

**Plasma** is the fourth state of matter (solid, liquid, gas, plasma) — an ionized gas with free electrons and ions. Most of the universe is plasma: stars, interstellar gas, lightning, fluorescent tubes, fusion reactor cores. **Plasma physics** couples mechanics to EM via the Lorentz force on charges. **MHD** (magnetohydrodynamics) treats plasma as a conducting fluid; in ideal MHD, magnetic field lines are "frozen into" the fluid. **Alfvén waves** are magnetic-field oscillations at speed $v_A = B/\sqrt{\mu_0\rho}$; **magnetic reconnection** releases magnetic energy when field lines break and rejoin — drives solar flares, geomagnetic storms, tokamak disruptions. **Fusion energy** requires confining hot plasma (magnetic or inertial) at Lawson criterion. **In BST**: plasmas are substrate K-type configurations at cosmological scale; MHD behavior is the substrate's EM-coupled fluid dynamics at coarse-grain level.

---

## What comes next

Chapter 12 closes Volume 7 with synthesis and bridges to other volumes.

## Where to look this up

- **Plasma**: Krall and Trivelpiece, *Principles of Plasma Physics*; Goldston and Rutherford, *Introduction to Plasma Physics*
- **MHD**: Davidson, *Introduction to Magnetohydrodynamics*; Priest, *Solar MHD*
- **Astrophysical plasmas**: Kulsrud, *Plasma Physics for Astrophysics*
- **Fusion**: Wesson, *Tokamaks*; Atzeni and Meyer-ter-Vehn, *The Physics of Inertial Fusion*
- **BST anchors**: Chapter 10; Volume 6 Ch 11; Volume 4
