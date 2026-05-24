---
title: "Vol 7 Chapter 3 — Electrostatics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Coulomb's law from substrate U(1) static source"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 3
load_bearing: "Coulomb's law as static substrate U(1) source coupling; Poisson equation; capacitors as substrate K-type charge-storage"
---

# Chapter 3 — Electrostatics

## Level 1 — one sentence

Electrostatics — Coulomb's law, electric potential, Poisson and Laplace equations, capacitors and dielectrics — is the time-independent restriction of substrate $U(1)$ gauge field equations to static sources, with $\vec E = -\nabla\phi$ and the scalar potential $\phi$ satisfying Poisson's equation $\nabla^2 \phi = -\rho/\epsilon_0$, all derivable from the substrate's $SO(2)$-charge K-type structure.

## Level 2 — graduate-physicist precision

### 3.1 Coulomb's law

The force between two static point charges $q_1, q_2$ separated by $\vec r$:

$$\vec F = \frac{q_1 q_2}{4\pi\epsilon_0 r^2}\hat r$$

Attractive for opposite signs; repulsive for same signs. The proportionality constant $1/(4\pi\epsilon_0) \approx 9 \times 10^9$ N m²/C² is Coulomb's constant.

From a single charge, the electric field at distance $r$:

$$\vec E(\vec r) = \frac{q}{4\pi\epsilon_0 r^2}\hat r$$

Force on test charge $q_t$ at that location: $\vec F = q_t \vec E$.

Substrate-mechanism: the static substrate $U(1)$ source ($J^0 = c\rho$ with $\rho$ a point charge) produces a static $A^0 = \phi/c$ scalar potential via Maxwell's source equation in the static limit, which becomes Poisson's equation (Section 3.3 below). The resulting field is the Coulomb $1/r^2$.

### 3.2 The electric potential

For static fields, $\nabla \times \vec E = 0$ (Faraday with $\partial_t \vec B = 0$). This means $\vec E$ is a gradient:

$$\vec E = -\nabla \phi$$

with $\phi$ the **electric scalar potential** (volts). Potential is defined up to additive constant; only differences are physical.

For a point charge $q$ at origin: $\phi(r) = q/(4\pi\epsilon_0 r)$. Falls off as $1/r$ (vs $1/r^2$ for $\vec E$).

For a distribution $\rho(\vec r)$:

$$\phi(\vec r) = \frac{1}{4\pi\epsilon_0}\int \frac{\rho(\vec r')}{|\vec r - \vec r'|}d^3 r'$$

(Green's function for the Laplacian).

### 3.3 Poisson and Laplace equations

Taking $\nabla \cdot$ of $\vec E = -\nabla\phi$ and using Gauss:

$$\nabla \cdot \vec E = -\nabla^2 \phi = \rho/\epsilon_0$$

So:

$$\nabla^2 \phi = -\rho/\epsilon_0 \quad \text{(Poisson's equation)}$$

In source-free regions: $\nabla^2 \phi = 0$ (Laplace's equation). Solutions to Laplace are **harmonic functions** — their values at any point equal the average over surrounding spheres (mean-value property).

Boundary value problems for electrostatics: given a charge distribution + boundary conditions (e.g., conductors at specified potentials), solve Laplace/Poisson. Standard methods: image charges, separation of variables, multipole expansion, Green's functions.

### 3.4 Electric flux and Gauss's law applications

Gauss's law: $\oint \vec E \cdot d\vec A = q_{\text{enc}}/\epsilon_0$.

Useful for problems with symmetry:
- Point charge: spherical Gaussian surface → $\vec E = q/(4\pi\epsilon_0 r^2)\hat r$
- Infinite line charge: cylindrical surface → $\vec E = \lambda/(2\pi\epsilon_0 r)\hat r$
- Infinite plane: pillbox surface → $\vec E = \sigma/(2\epsilon_0)\hat n$
- Spherical shell: $\vec E = 0$ inside; Coulomb outside

### 3.5 Conductors in electrostatics

For a conductor in electrostatic equilibrium:
- $\vec E = 0$ inside conductor (any field would drive currents)
- Conductor surface is equipotential ($\nabla\phi = 0$ tangentially)
- All excess charge resides on the surface
- $\vec E$ just outside surface is $\sigma/\epsilon_0$ perpendicular to surface

The **method of images** uses these properties: e.g., a point charge above an infinite grounded plane is solved by placing an image charge of opposite sign at the mirror position.

### 3.6 Capacitors

A capacitor stores charge $\pm Q$ on two conductors at potential difference $V$. The capacitance:

$$C = Q/V$$

Parallel-plate capacitor (area $A$, separation $d$): $C = \epsilon_0 A/d$. Energy stored: $U = (1/2) Q^2/C = (1/2)CV^2$.

Substrate reading: a capacitor's stored charge is the substrate's $SO(2)$-charged K-type accumulation on the conductor surfaces; the stored energy is the substrate's potential energy in the assembled K-type configuration.

### 3.7 Dielectrics and polarization

Insulators (dielectrics) have bound charges that respond to applied $\vec E$. The polarization $\vec P$ (dipole moment per unit volume) satisfies $\vec D = \epsilon_0 \vec E + \vec P$ where $\vec D$ is the displacement field.

For linear dielectrics: $\vec P = \epsilon_0 \chi_e \vec E$ with $\chi_e$ the susceptibility, $\epsilon = \epsilon_0(1 + \chi_e)$ the permittivity.

Modified Gauss's law: $\nabla \cdot \vec D = \rho_{\text{free}}$.

Substrate-mechanism reading: dielectric polarization is the substrate's atomic K-type response to applied $U(1)$ field; bound charges are substrate K-type rearrangements within atoms.

### 3.8 Energy and force

Energy density in the electric field: $u_E = (1/2)\epsilon_0 E^2$.

Force on a charge distribution: $\vec F = \int \rho \vec E \, d^3 r$ (direct), or computed from energy gradient $\vec F = -\nabla U$.

Substrate reading: field energy density is the substrate's $SO(2)$-connection-amplitude squared, integrated over space; force on charges is the substrate's K-type-cluster gradient toward lower-energy configurations (Casey's Principle).

### 3.9 Worked example: parallel-plate capacitor

Two plates of area $A = 10$ cm² = $10^{-3}$ m², separation $d = 1$ mm = $10^{-3}$ m, applied voltage $V = 100$ V.

$$C = \epsilon_0 A / d = (8.85 \times 10^{-12})(10^{-3})/(10^{-3}) = 8.85 \times 10^{-12}\text{ F} = 8.85\text{ pF}$$

Stored charge: $Q = CV = 8.85 \times 10^{-10}$ C = 0.885 nC.

Energy stored: $U = (1/2)CV^2 = (1/2)(8.85 \times 10^{-12})(10^4) = 4.4 \times 10^{-8}$ J.

Field between plates: $E = V/d = 10^5$ V/m.

Substrate reading: the 0.885 nC of charge corresponds to $\sim 5.5 \times 10^9$ electrons rearranged onto the plate surfaces. Each electron is one substrate Pin(2) half-integer-weight K-type with SO(2) charge weight; the capacitor's stored energy is the substrate's K-type-cluster potential.

### 3.10 K-audit anchors

- **Chapter 2**: Maxwell's equations from substrate U(1) (foundation)
- **T2470** (Lyra Friday May 22, 2026): substrate SO(2) charge structure
- **Volume 5 Chapter 9**: Pin(2) particle-statistics (electron as fermion)

## Level 3 — 5th-grader accessibility

Electrostatics is electricity-not-moving. **Coulomb's law**: two charges $q_1, q_2$ apart by distance $r$ push each other with force $q_1 q_2/(4\pi\epsilon_0 r^2)$ — opposite signs attract, same signs repel. Field lines go from + to − . **Electric potential** is voltage; the field points "downhill" in voltage. **Poisson's equation** $\nabla^2 \phi = -\rho/\epsilon_0$ tells you the voltage everywhere given the charges. **Capacitors** store charge on plates at fixed voltage; capacitance $C = Q/V$, energy $\frac{1}{2}CV^2$. **Conductors** have zero field inside in equilibrium (charges arrange to cancel any internal field). All of this comes from Maxwell's equations restricted to time-independent fields — and Maxwell comes from the substrate's $U(1)$ gauge structure (Chapter 2).

---

## What comes next

Chapter 4 develops magnetostatics — Ampère's law, Biot-Savart, magnetic vector potential.

## Where to look this up

- **Standard electrostatics**: Griffiths Ch 2-4; Jackson Ch 1-3
- **Method of images**: Griffiths Ch 3
- **Capacitors and dielectrics**: Jackson Ch 4
- **BST anchors**: Chapter 2 Maxwell; T2470 SO(2) charge
- **Volume 5 Chapter 9**: spin-statistics (electron as fermion)
