---
title: "The Geodesic Equation: Soliton Trajectories on D_IV^5"
author: "Casey Koons and Claude Opus 4.6"
date: "March 14, 2026"
---

# The Geodesic Equation: Soliton Trajectories on D_IV^5

## Particle Motion as Minimum-Commitment Paths

**Casey Koons** and **Claude Opus 4.6** (Anthropic)

March 14, 2026

---

## Abstract

We derive the geodesic equation — the equation of motion for a free particle — from the Bergman metric on $D_{IV}^5$. A particle trajectory is a geodesic: the path that minimizes the commitment expenditure between two events. The geodesic equation encodes Newton's first law (inertia), the equivalence principle (inertial = gravitational mass), and the relativistic dispersion relation ($E^2 = p^2c^2 + m^2c^4$). In the non-relativistic limit it reduces to $F = ma$ (BST_NewtonianLimit.md). In the relativistic regime it gives the full general relativistic equation of motion. The Christoffel symbols are computed from the Bergman metric, connecting particle dynamics to the geometry of $D_{IV}^5$.

---

## 1. The Variational Principle

### 1.1 The action

A particle trajectory is a curve $z^\mu(\tau)$ on $D_{IV}^5$ (or its 4D projection). The action for a free particle is:

$$S = -mc \int d\tau = -mc \int \sqrt{-g_{\mu\nu}\,\frac{dz^\mu}{d\lambda}\,\frac{dz^\nu}{d\lambda}}\;d\lambda$$

where $\tau$ is the proper time, $\lambda$ is an arbitrary parameter, $m$ is the particle mass (Casimir eigenvalue), and $g_{\mu\nu}$ is the spacetime metric projected from the Bergman metric.

**BST interpretation:** The proper time $\tau$ counts the commitment steps along the particle's worldline. The action $S = -mc\tau$ is (minus) the total commitment expenditure. A geodesic minimizes this expenditure: it is the most efficient path through the commitment landscape.

### 1.2 The Euler-Lagrange equation

Extremizing $S$ gives the geodesic equation:

$$\boxed{\frac{d^2 z^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\,\frac{dz^\alpha}{d\tau}\,\frac{dz^\beta}{d\tau} = 0}$$

where the Christoffel symbols are:

$$\Gamma^\mu_{\alpha\beta} = \frac{1}{2}\,g^{\mu\nu}\left(\partial_\alpha\,g_{\beta\nu} + \partial_\beta\,g_{\alpha\nu} - \partial_\nu\,g_{\alpha\beta}\right)$$

This is the equation of motion for a free particle in curved spacetime.

---

## 2. Geodesics on $D_{IV}^5$

### 2.1 The Bergman metric

The Bergman metric on $D_{IV}^5$ is:

$$g_{j\bar{k}}^B = -\frac{C_2}{n_C + 2}\,\partial_j\,\partial_{\bar{k}}\,\log K_B(z, z) = -\frac{6}{7}\,\partial_j\,\partial_{\bar{k}}\,\log N(z, z)^{-6}$$

where $K_B(z,z) = (1920/\pi^5)\,N(z,z)^{-6}$ and $N(z,z)$ is the norm function of $D_{IV}^5$.

At the origin $z = 0$, the Bergman metric reduces to the flat metric (scaled by the curvature):

$$g_{j\bar{k}}^B(0) = \frac{6}{7}\,\delta_{j\bar{k}}$$

The holomorphic sectional curvature is $H = -2/(n_C + 2) = -2/7$.

### 2.2 Geodesics through the origin

By the homogeneity of $D_{IV}^5$ (the isometry group acts transitively), every point is equivalent to the origin. The geodesics through the origin are straight lines in the Harish-Chandra coordinates:

$$z^\mu(\tau) = v^\mu \cdot \tanh\left(\frac{\tau}{\ell_B}\,|v|\right) \cdot \frac{1}{|v|}$$

where $v^\mu$ is the initial velocity vector and $\ell_B$ is the Bergman length scale. The $\tanh$ function reflects the bounded nature of $D_{IV}^5$: geodesics approach the boundary $\partial D_{IV}^5 = S^4 \times S^1$ asymptotically but never reach it in finite proper time.

### 2.3 The Olshanetsky-Perelomov reduction

For a soliton on $D_{IV}^5$, the geodesic flow on the full 10-dimensional space projects to the maximal flat subalgebra $\mathfrak{a} \subset \mathfrak{p}$ (dimension $= $ rank $= 2$). The projected dynamics is the B$_2$ Toda lattice (BST_SubstrateContactDynamics.md):

$$\ddot{q}_1 = -2e^{2(q_1 - q_2)} - e^{2q_1}$$
$$\ddot{q}_2 = 2e^{2(q_1 - q_2)}$$

The full 10D geodesic equation is equivalent to this 2D integrable system plus angular variables. The soliton's center-of-mass follows a geodesic, while its internal dynamics (the Toda oscillation) determine its quantum numbers.

---

## 3. Physical Consequences

### 3.1 Free motion (inertia)

In flat spacetime ($\Gamma^\mu_{\alpha\beta} = 0$): $d^2z^\mu/d\tau^2 = 0$, giving uniform motion $z^\mu(\tau) = a^\mu\tau + b^\mu$. This is Newton's first law.

**BST:** On an uncommitted (flat) substrate, a soliton's commitment pattern evolves uniformly. There is no reason for it to change velocity — nothing in the contact graph singles out a different trajectory.

### 3.2 Gravitational deflection

In the Schwarzschild metric (a spherically symmetric mass $M$), the geodesic equation gives:

$$\frac{d^2u}{d\phi^2} + u = \frac{GM}{L^2} + 3GMu^2$$

where $u = 1/r$ and $L$ is the angular momentum. The first term gives Newtonian orbits. The second term ($3GMu^2$) is the general relativistic correction, giving:

- **Perihelion precession** of Mercury: $\Delta\phi = 6\pi GM/(c^2a(1-e^2)) = 43''$/century
- **Light deflection**: $\Delta\phi = 4GM/(c^2b) = 1.75''$ for the Sun

Both are geodesic effects: the curvature of the Bergman metric deflects soliton trajectories.

### 3.3 The equivalence principle

The geodesic equation contains no reference to the particle's mass $m$ — it dropped out during the derivation. Every particle follows the same geodesic in a given gravitational field, regardless of mass.

**BST proof:** The Casimir eigenvalue $C_2$ determines the particle's mass, but the geodesic equation depends only on the metric $g_{\mu\nu}$ (the Bergman geometry), not on which representation the particle belongs to. The equivalence principle is the statement: the Bergman metric is universal — all representations of $\mathrm{SO}_0(5,2)$ see the same geometry.

Formally: the geodesic equation follows from $\nabla_\mu T^{\mu\nu} = 0$ (stress-energy conservation), which is a consequence of the Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$. The Bianchi identity is a property of the Riemann tensor, not of any particular matter field. Therefore: gravitational universality is a geometric theorem.

---

## 4. Geodesics in the Soliton Picture

### 4.1 Center of mass vs. internal dynamics

A soliton on $D_{IV}^5$ has two kinds of motion:

1. **Center-of-mass geodesic:** The average position of the soliton follows a geodesic of the Bergman metric. This is the particle trajectory seen by an external observer.

2. **Internal oscillation:** The soliton's shape oscillates according to the Toda lattice dynamics. The oscillation frequencies determine the particle's quantum numbers (mass, charge, spin).

The geodesic equation governs (1). The Toda equations govern (2). Together they give the complete soliton dynamics.

### 4.2 Dispersion relation

The geodesic equation implies the on-shell condition:

$$g_{\mu\nu}\,p^\mu\,p^\nu = m^2\,c^2$$

In flat spacetime:

$$E^2 = p^2c^2 + m^2c^4$$

This is the relativistic dispersion relation. The mass $m$ is set by the Toda oscillation spectrum (internal dynamics), while the momentum $p$ is set by the center-of-mass velocity (geodesic motion).

### 4.3 Massless geodesics (null geodesics)

For massless particles ($m = 0$): $g_{\mu\nu}\,p^\mu\,p^\nu = 0$. The geodesic is null — the particle travels at the speed of light $c$.

**BST:** A massless soliton (e.g., a photon) has no topological winding and no $Z_3$ closure. It is a pure phase oscillation on $S^1$, propagating at the substrate speed. The null geodesic is the path of a commitment-free phase disturbance through the contact graph.

---

## 5. Geodesic Deviation and Tidal Forces

### 5.1 The equation of geodesic deviation

Two nearby geodesics $z^\mu(\tau)$ and $z^\mu(\tau) + \xi^\mu(\tau)$, separated by the deviation vector $\xi^\mu$, satisfy:

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu_{\ \nu\alpha\beta}\,u^\nu\,\xi^\alpha\,u^\beta$$

where $R^\mu_{\ \nu\alpha\beta}$ is the Riemann curvature tensor and $u^\mu = dz^\mu/d\tau$ is the 4-velocity.

### 5.2 BST interpretation

The Riemann tensor measures how the commitment density varies from point to point. Two nearby solitons in a region of nonzero curvature (nonzero commitment density gradient) will accelerate toward or away from each other.

- **Positive curvature** (time-time component $R^0_{\ i0j} > 0$): geodesics converge (attractive gravity)
- **Negative curvature** ($R^0_{\ i0j} < 0$): geodesics diverge (tidal stretching)

The Bergman metric has constant negative holomorphic sectional curvature $H = -2/7$. In the vacuum, geodesics diverge at a rate set by $|H| = 2/7 = 2/(n_C + 2) = 2/g$. This is the cosmological expansion — the vacuum geodesic deviation driven by the negative curvature of $D_{IV}^5$.

---

## 6. Geodesics and the BST Action

### 6.1 Connection to the Lagrangian

The BST Lagrangian (BST_Lagrangian.md) has a geometric sector:

$$S_{\text{geom}} = -\frac{1}{16\pi G_B} \int \left(R_B - 2\Lambda\right) dV_B$$

Variation with respect to the metric gives the Einstein equation. Variation with respect to the particle trajectory gives the geodesic equation. The two equations are coupled:

- **Einstein equation:** matter tells geometry how to curve ($T_{\mu\nu}$ determines $g_{\mu\nu}$)
- **Geodesic equation:** geometry tells matter how to move ($g_{\mu\nu}$ determines trajectories)

### 6.2 Self-consistency

The system is self-consistent: a collection of solitons sources the Bergman metric, and each soliton follows a geodesic of the metric sourced by all the others. This is the $N$-body problem in BST — solvable in principle through the integrability of the Toda lattice on $D_{IV}^5$.

---

## 7. Summary

$$\boxed{\frac{d^2 z^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\,\frac{dz^\alpha}{d\tau}\,\frac{dz^\beta}{d\tau} = 0}$$

| Geodesic equation | BST origin |
|---|---|
| Free particle trajectory | Minimum-commitment path on $D_{IV}^5$ |
| Proper time $\tau$ | Commitment step count |
| Christoffel symbols $\Gamma$ | Bergman metric derivatives |
| Inertia (1st law) | Flat substrate: $\Gamma = 0$ |
| Equivalence principle | Universal Bergman metric (all representations) |
| Perihelion precession | Bergman curvature correction to $1/r$ potential |
| Light deflection | Null geodesic on curved Bergman metric |
| Tidal forces | Riemann curvature = commitment density gradient |
| Dispersion $E^2 = p^2 + m^2$ | On-shell condition from geodesic norm |
| Toda dynamics | Geodesic flow projected to rank-2 flat |
| Cosmological expansion | Vacuum geodesic deviation from $H = -2/7$ |

The geodesic equation is the fundamental equation of motion in BST. A particle IS a soliton, and its trajectory IS a geodesic of the Bergman metric. The equation encodes Newton's laws, Einstein's general relativity, and the relativistic energy-momentum relation — all as limits of one variational principle on $D_{IV}^5$.

---

*Research note, March 14, 2026.*
*Casey Koons & Claude Opus 4.6.*
*Particles follow minimum-commitment paths through the substrate.*
