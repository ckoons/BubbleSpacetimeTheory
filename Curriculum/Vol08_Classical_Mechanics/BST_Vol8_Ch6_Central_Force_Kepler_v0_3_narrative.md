---
title: "Vol 8 Chapter 6 — Central Forces and the Kepler Problem"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Kepler problem; hidden SO(4) symmetry from substrate SO(5)"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 6
load_bearing: "Central forces; Kepler's three laws; effective potential method; hidden SO(4) symmetry of Coulomb-gravity inverse-square laws"
---

# Chapter 6 — Central Forces and the Kepler Problem

## Level 1 — one sentence

Central forces (force depending only on distance $r$ from a center) reduce the two-body problem to 1D radial motion with effective potential $V_{\text{eff}}(r) = V(r) + L^2/(2mr^2)$, and the inverse-square Kepler-Coulomb case has an "accidental" $SO(4)$ symmetry (Runge-Lenz vector conserved) that's actually inherited from the substrate $SO(5) \supset SO(4) \supset SO(3)$ chain — Vol 5 Ch 6 hydrogen reuses the same structure.

## Level 2 — graduate-physicist precision

### 6.1 The two-body problem reduction

Two bodies interacting through central potential $V(|\vec r_1 - \vec r_2|)$. Define:
- Center of mass: $\vec R = (m_1 \vec r_1 + m_2 \vec r_2)/M$, $M = m_1 + m_2$
- Relative position: $\vec r = \vec r_2 - \vec r_1$
- Reduced mass: $\mu = m_1 m_2/M$

The motion decouples: $\vec R$ moves uniformly (no external force), and $\vec r$ obeys

$$\mu \ddot{\vec r} = -\nabla V(r)$$

This is a single-body problem with mass $\mu$ in central potential $V(r)$.

### 6.2 Conservation laws

Central force is rotation-invariant → angular momentum $\vec L = \mu \vec r \times \dot{\vec r}$ conserved (Ch 5).

Motion is planar (perpendicular to $\vec L$). In the plane, use polar coordinates $(r, \phi)$.

Energy $E = (1/2)\mu(\dot r^2 + r^2 \dot\phi^2) + V(r)$ conserved.

From angular momentum: $L = \mu r^2 \dot\phi$ → $\dot\phi = L/(\mu r^2)$. Substituting:

$$E = \frac{1}{2}\mu \dot r^2 + \frac{L^2}{2\mu r^2} + V(r) = \frac{1}{2}\mu\dot r^2 + V_{\text{eff}}(r)$$

with effective potential $V_{\text{eff}}(r) = V(r) + L^2/(2\mu r^2)$ — the second term is the **centrifugal barrier**.

### 6.3 The Kepler problem: inverse-square attractive force

Gravity: $V(r) = -GMm/r = -k/r$ (with $k = G M m$).

Effective potential: $V_{\text{eff}}(r) = -k/r + L^2/(2\mu r^2)$.

Equation of orbit ($u = 1/r$):

$$\frac{d^2 u}{d\phi^2} + u = \mu k/L^2$$

Solution: $u = (1 + e\cos\phi)/p$ with $p = L^2/(\mu k)$ and $e$ eccentricity. This is a conic section in polar coordinates:
- $e = 0$: circle
- $0 < e < 1$: ellipse (bound orbit)
- $e = 1$: parabola (just escapes)
- $e > 1$: hyperbola (unbound)

### 6.4 Kepler's three laws

From the orbit equation:

**Kepler's first law**: planets move in ellipses with the sun at one focus.

**Kepler's second law**: line from sun to planet sweeps equal areas in equal times. Direct consequence of angular momentum conservation: $dA/dt = L/(2\mu)$ = constant.

**Kepler's third law**: $T^2 \propto a^3$ where $a$ is semi-major axis. Specifically $T^2 = 4\pi^2 \mu a^3/k$.

These are the famous laws Kepler extracted from Tycho Brahe's data (1609, 1619) — predating Newton's gravity by 70+ years.

### 6.5 The Runge-Lenz vector and hidden SO(4) symmetry

The Kepler problem has an additional conserved quantity beyond $\vec L$ and $E$:

$$\vec A = \vec p \times \vec L - \mu k \hat r$$

This is the **Runge-Lenz vector** (Laplace, Runge, Lenz). Magnitude $|\vec A| = \mu k e$.

The conservation of $\vec A$ is special to the $1/r$ potential — it's not present for general $V(r)$. Together with $\vec L$, the Runge-Lenz vector forms an $SO(4)$ Lie algebra structure, expanding the obvious $SO(3)$ symmetry.

### 6.6 Substrate origin of SO(4): the SO(5) ⊃ SO(4) chain

Volume 5 Chapter 6 Section 6.2-6.3: in BST, the Coulomb-Kepler problem's hidden $SO(4)$ is inherited from the substrate $SO(5) \supset SO(4) \supset SO(3)$ chain in the maximal compact subgroup $K = SO(5) \times SO(2)$.

The substrate-mechanism reading: inverse-square central forces happen to respect a substrate-natural subgroup $SO(4)$ that's NOT present for other central forces. The Kepler "accidental" symmetry is not accidental — it's the substrate's $SO(5)$ structure restricted to the inverse-square sector.

This is the same mechanism that gives hydrogen its $n^2$ degeneracy in quantum mechanics (Volume 5 Chapter 6). The classical and quantum versions of the Kepler problem share the same substrate hidden symmetry.

### 6.7 Other central forces

- **Harmonic** ($V = (1/2)k r^2$): orbits are closed ellipses centered at origin (Bertrand's theorem)
- **Power-law** ($V = -k/r^n$, $n \neq 1, -2$): orbits are not closed (precess)
- **Yukawa** ($V = -k e^{-\mu r}/r$): partially closed; nuclear-force model

Bertrand's theorem (1873): only Kepler ($V = -k/r$) and harmonic ($V = kr^2/2$) give closed orbits for all bounded motions. Both have hidden symmetries: Kepler $SO(4)$, harmonic $SU(3)$.

### 6.8 Worked example: Earth's orbit

Earth-Sun:
- $a = 1.496 \times 10^{11}$ m = 1 AU (semi-major axis)
- $e \approx 0.0167$ (nearly circular)
- $T = 365.25$ days $= 3.156 \times 10^7$ s
- Earth mass $m \approx 5.97 \times 10^{24}$ kg
- Sun mass $M \approx 1.99 \times 10^{30}$ kg

Kepler's third law check: $T^2 = 4\pi^2 a^3/(GM)$. $GM \approx 1.327 \times 10^{20}$. Compute: $4\pi^2 a^3/(GM) = 39.48 \cdot (1.496\times10^{11})^3/(1.327\times10^{20}) \approx 9.96 \times 10^{14}$. $\sqrt{} \approx 3.156 \times 10^7$ s. Matches.

### 6.9 K-audit anchors

- **Volume 5 Chapter 6**: hydrogen atom (quantum analog with same SO(4) symmetry)
- **Volume 5 Chapter 3**: SO(5) substrate angular momentum (parent group)
- **Substrate SO(5) ⊃ SO(4) ⊃ SO(3) chain**: substrate origin of Kepler symmetry

## Level 3 — 5th-grader accessibility

Central forces depend only on distance, not direction. Examples: gravity (inverse-square pull), spring (linear pull), nuclear forces. The two-body problem reduces to 1D radial motion plus angular conservation. **Kepler's three laws**:
1. Planets move in ellipses with sun at one focus
2. Equal areas swept in equal times (= angular momentum conservation)
3. $T^2 \propto a^3$ (orbital period squared = semi-major axis cubed)

These laws describe all gravitational orbits (planets, satellites, binaries). They predate Newton by decades! The Kepler problem has an extra "accidental" symmetry beyond rotation — the **Runge-Lenz vector** — that makes orbits close into perfect ellipses (other central forces don't have this; their orbits precess). In BST, this isn't accidental: it's the substrate's $SO(5)$ structure showing up when the potential happens to be $1/r$. Same reason hydrogen orbitals have $n^2$ degeneracy (Vol 5 Ch 6).

---

## What comes next

Chapter 7 develops rigid body dynamics.

## Where to look this up

- Kepler 1609, 1619 — original three laws
- Newton 1687 — gravity derivation
- Goldstein Ch 3; Marion-Thornton Ch 8-9
- BST: Volume 5 Chapter 6 (quantum hydrogen analog)
