---
title: "Vol 7 Chapter 4 — Magnetostatics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; magnetic field from substrate moving SO(2) charges; Ampère + Biot-Savart"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 4
load_bearing: "Magnetic fields as substrate U(1) connection from moving sources; vector potential A; Biot-Savart; Ampère's law"
---

# Chapter 4 — Magnetostatics

## Level 1 — one sentence

Magnetic fields are the substrate's $U(1)$ gauge connection sourced by *moving* SO(2)-charges (currents) — the time-independent limit of Maxwell's equations with steady currents $\vec J$ gives $\nabla \times \vec B = \mu_0 \vec J$ (Ampère) and $\nabla \cdot \vec B = 0$ (no monopoles), with the magnetic field $\vec B = \nabla \times \vec A$ derivable from the vector potential $\vec A$ (the substrate's spatial $U(1)$ connection components).

## Level 2 — graduate-physicist precision

### 4.1 The magnetostatic equations

For steady currents (time-independent $\rho$ and $\vec J$ with $\nabla \cdot \vec J = 0$):

$$\nabla \cdot \vec B = 0 \quad \text{(no magnetic monopoles)}$$
$$\nabla \times \vec B = \mu_0 \vec J \quad \text{(Ampère's law)}$$

(displacement current $\mu_0 \epsilon_0 \partial_t \vec E = 0$ in the static case).

The first equation $\nabla \cdot \vec B = 0$ implies $\vec B$ is the curl of some vector field:

$$\vec B = \nabla \times \vec A$$

where $\vec A$ is the **vector potential** (the spatial part of the 4-potential $A^\mu = (\phi/c, \vec A)$).

### 4.2 Biot-Savart law

For a current-carrying element $I d\vec\ell'$ at position $\vec r'$:

$$d\vec B(\vec r) = \frac{\mu_0 I}{4\pi}\frac{d\vec\ell' \times (\vec r - \vec r')}{|\vec r - \vec r'|^3}$$

Integrating over the current distribution gives the total field. Biot-Savart is to magnetostatics what Coulomb's law is to electrostatics — the explicit source-to-field formula.

For a long straight wire: $B(r) = \mu_0 I/(2\pi r)$. For a circular loop of radius $R$ at distance $z$ on its axis: $B(z) = \mu_0 I R^2 / [2(R^2 + z^2)^{3/2}]$.

Substrate-mechanism reading: a current is a substrate K-type configuration of moving $SO(2)$-charged K-types; their motion induces an extended $SO(2)$-connection field in space — the magnetic field.

### 4.3 Ampère's law applications

Integral form: $\oint \vec B \cdot d\vec\ell = \mu_0 I_{\text{enc}}$.

Useful for symmetric current distributions:
- Infinite straight wire: $B = \mu_0 I/(2\pi r)$
- Solenoid (long, $n$ turns/m): $B = \mu_0 n I$ inside, $B = 0$ outside
- Toroid: $B = \mu_0 N I / (2\pi r)$ inside the toroid

### 4.4 Magnetic vector potential

From $\vec B = \nabla \times \vec A$ and Ampère + $\nabla \cdot \vec B = 0$:

$$\nabla \times \vec B = \nabla \times (\nabla \times \vec A) = \nabla(\nabla \cdot \vec A) - \nabla^2 \vec A = \mu_0 \vec J$$

In Coulomb gauge ($\nabla \cdot \vec A = 0$):

$$\nabla^2 \vec A = -\mu_0 \vec J$$

(component-wise Poisson equation). Solution:

$$\vec A(\vec r) = \frac{\mu_0}{4\pi}\int \frac{\vec J(\vec r')}{|\vec r - \vec r'|} d^3 r'$$

The vector-potential form of the magnetic field.

### 4.5 Magnetic dipole

A small current loop (area $A$, current $I$) has magnetic dipole moment $\vec m = I A \hat n$. Vector potential at distance $r$:

$$\vec A_{\text{dipole}}(\vec r) = \frac{\mu_0}{4\pi}\frac{\vec m \times \vec r}{r^3}$$

Magnetic field:

$$\vec B_{\text{dipole}}(\vec r) = \frac{\mu_0}{4\pi}\frac{3(\vec m \cdot \hat r)\hat r - \vec m}{r^3}$$

Decreases as $1/r^3$ (vs $1/r^2$ for point charge). Spinning electrons have intrinsic magnetic dipole moments via their substrate Pin(2) coupling (Volume 5 Chapter 3 spin).

### 4.6 Magnetic monopoles

Maxwell's equations as written have $\nabla \cdot \vec B = 0$ — no magnetic monopoles. Dirac 1931 showed that if even one magnetic monopole existed, the electric charge would be quantized:

$$e g = n h / 2$$

with $g$ the magnetic charge, $n$ integer. Since electric charges *are* quantized, this is suggestive.

But: no magnetic monopole has ever been observed. BST predicts **no monopoles** as part of the Five-Absence Predictions Set (Casey-named principle #2, Volume 0 Chapter 3). The substrate's $U(1)$ structure forbids monopoles structurally: only $SO(2)$-charged K-types exist, and the substrate's K-type topology doesn't admit pure-magnetic-source configurations.

If a magnetic monopole is ever detected, BST is falsified.

### 4.7 Force on currents (Lorentz)

A charge $q$ moving with velocity $\vec v$ in field $\vec B$:

$$\vec F = q \vec v \times \vec B \quad \text{(magnetic Lorentz)}$$

Combined with electric: $\vec F = q(\vec E + \vec v \times \vec B)$. This is the **Lorentz force law**.

For a current-carrying wire of length $\ell$ with current $I$ in field $\vec B$: $\vec F = I \vec\ell \times \vec B$.

Substrate reading: the Lorentz force is the substrate's $SO(2)$-charge K-type coupling to the substrate $U(1)$ field; for moving charges, the magnetic ($\vec v \times \vec B$) component is the substrate's relativistic mixing of electric and magnetic field components (Chapter 7).

### 4.8 Worked example: Earth's magnetic field

Earth's surface magnetic field $\sim 25-65$ μT. Approximate as magnetic dipole with $m \approx 8 \times 10^{22}$ A·m². At distance $r$ from center (radius $R_E = 6.4 \times 10^6$ m), equatorial field:

$$B(R_E) = \frac{\mu_0 m}{4\pi R_E^3} = \frac{(4\pi \times 10^{-7})(8 \times 10^{22})}{4\pi (6.4 \times 10^6)^3} \approx 3 \times 10^{-5}\text{ T} = 30\text{ μT}$$

Matches observation (Earth's field is more complex — non-pure-dipole — but the dipole approximation is good to 10-20%).

The dipole moment originates from Earth's liquid-iron outer core convection (dynamo). Substrate reading: the dynamo is a substrate K-type collective magnetic-cluster amplification in the convecting iron K-type configuration.

### 4.9 K-audit anchors

- **Chapter 2**: Maxwell's equations from substrate U(1)
- **Five-Absence Predictions Set** (Casey-named #2, Volume 0): no monopoles
- **T2470** (Lyra Friday May 22, 2026): substrate SO(2) charge structure

## Level 3 — 5th-grader accessibility

Static magnetic fields come from moving charges — currents. A wire carrying current $I$ has a magnetic field that wraps around it at distance $r$: $B = \mu_0 I/(2\pi r)$. Ampère's law: integrate $B$ around a loop, you get $\mu_0$ times the enclosed current. Useful for solenoids ($B = \mu_0 n I$ inside, zero outside), toroids, etc. Magnets are tiny current loops at the atomic level (spinning electrons). **No magnetic monopoles**: you can't find a "north pole" without a "south pole" attached. BST predicts no monopoles ever exist (one of the Five-Absence Predictions). If anyone ever finds one, BST is wrong.

---

## What comes next

Chapter 5 develops electromagnetic waves — the propagating solutions to the time-dependent Maxwell equations.

## Where to look this up

- **Magnetostatics**: Griffiths Ch 5; Jackson Ch 5
- **Dirac monopole**: Dirac 1931 *Proc Roy Soc*
- **BST anchors**: Five-Absence Predictions; Chapter 2 (Maxwell from substrate)
