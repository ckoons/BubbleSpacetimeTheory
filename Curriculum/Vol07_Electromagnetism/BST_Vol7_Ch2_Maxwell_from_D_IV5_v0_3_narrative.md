---
title: "Vol 7 Chapter 2 — Maxwell's Equations from D_IV⁵"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — LOAD-BEARING; Maxwell from substrate U(1) gauge action; F = dA structure on D_IV⁵"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 2
load_bearing: "Maxwell's equations from substrate U(1) Yang-Mills gauge structure; F_{μν} = ∂_μ A_ν − ∂_ν A_μ on D_IV⁵; Gauss + Faraday + Ampère + no-monopole all from substrate gauge invariance"
---

# Chapter 2 — Maxwell's Equations from $D_{IV}^5$

## Level 1 — one sentence

Maxwell's four equations — Gauss's law for E, Faraday's law, Gauss for B, Ampère-Maxwell — are not independent empirical findings but the substrate's $U(1)$ gauge-field equations in tensor form $\partial_\mu F^{\mu\nu} = J^\nu$ and $\partial_{[\mu} F_{\nu\rho]} = 0$, where $F = dA$ is the gauge curvature 2-form built from the substrate $SO(2)$ connection 1-form $A$, and the equations follow directly from substrate gauge invariance and the variational principle.

## Level 2 — graduate-physicist precision

### 2.1 The four classical Maxwell equations

Standard form (SI units):

$$\nabla \cdot \vec E = \rho/\epsilon_0 \quad \text{(Gauss's law)}$$
$$\nabla \cdot \vec B = 0 \quad \text{(no magnetic monopoles)}$$
$$\nabla \times \vec E = -\partial_t \vec B \quad \text{(Faraday)}$$
$$\nabla \times \vec B = \mu_0 \vec J + \mu_0 \epsilon_0 \, \partial_t \vec E \quad \text{(Ampère-Maxwell)}$$

These four equations, plus the Lorentz force law and conservation of charge ($\nabla \cdot \vec J + \partial_t \rho = 0$, which follows from Maxwell's equations), describe all classical EM.

### 2.2 Tensor formulation

The electric and magnetic fields combine into the **field strength tensor** (a 2-form):

$$F^{\mu\nu} = \begin{pmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0 \end{pmatrix}$$

The four-current $J^\mu = (c\rho, \vec J)$.

Maxwell's equations in tensor form:

$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu \quad \text{(source equations: Gauss + Ampère-Maxwell)}$$
$$\partial_{[\mu} F_{\nu\rho]} = 0 \quad \text{(source-free equations: no-monopole + Faraday)}$$

Two tensor equations; eight component equations. The second equation (Bianchi identity) is automatically satisfied if $F = dA$ for some 4-vector potential $A^\mu = (\phi/c, \vec A)$:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

So Maxwell's eight equations reduce to: define $F$ from $A$; impose source equation $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$. The Bianchi identity is automatic.

### 2.3 Maxwell from substrate $U(1)$ gauge action

In BST, the substrate's $U(1)$ gauge sector is the natural $SO(2) \subset K$ factor (Chapter 1). The gauge field $A^\mu$ is the substrate's $SO(2)$ connection 1-form. The field strength $F = dA$ is its curvature 2-form.

The Yang-Mills action (Volume 1 Chapter 8) restricted to $U(1)$:

$$S_{EM} = -\frac{1}{4\mu_0}\int d^4 x \, F_{\mu\nu} F^{\mu\nu} = \frac{1}{2}\int d^4 x \, (\epsilon_0 E^2 - B^2/\mu_0)$$

Variational principle: $\delta S_{EM}/\delta A^\nu = 0$ → $\partial_\mu F^{\mu\nu} = 0$ (vacuum) or $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ (with source).

The Bianchi identity $\partial_{[\mu} F_{\nu\rho]} = 0$ holds automatically because $F = dA$ and $d^2 = 0$.

All of Maxwell's equations are recovered from the substrate $U(1)$ gauge variational principle.

### 2.4 Why this is a derivation, not a postulate

Standard EM postulates Maxwell's equations as empirical findings. Faraday's law from experiment. Ampère's law from experiment. Maxwell's correction (displacement current) from theoretical consistency. The vacuum speed of light $c = 1/\sqrt{\mu_0\epsilon_0}$ as another empirical fit.

BST derives all four equations from the substrate's natural $U(1)$ gauge structure plus the variational principle on $D_{IV}^5$. The constants $\epsilon_0$ and $\mu_0$ have substrate-derivable values (their ratio is $c^2$ — substrate's natural light-speed); the structure $F = dA$ with the Yang-Mills action $-F^2/4$ is forced by gauge invariance.

This is what "Maxwell from $D_{IV}^5$" means: the equations aren't independent inputs; they follow from substrate $U(1) = SO(2) \subset K$ together with the substrate variational principle.

### 2.5 Gauge invariance

The 4-potential $A^\mu$ is not directly observable; only $F = dA$ is. Under a gauge transformation $A^\mu \to A^\mu + \partial^\mu \Lambda$ for arbitrary scalar function $\Lambda$:

$$F_{\mu\nu} \to \partial_\mu(A_\nu + \partial_\nu \Lambda) - \partial_\nu(A_\mu + \partial_\mu \Lambda) = F_{\mu\nu}$$

(since partial derivatives commute). So $F$ is gauge-invariant. The physical content of EM is in $F$, not $A$.

Substrate-mechanism reading: gauge invariance is the substrate's $SO(2)$ symmetry — the substrate's $SO(2)$ phase doesn't enter physical observables; only the $SO(2)$ curvature (gradient) does.

Common gauge choices:
- **Lorenz gauge**: $\partial_\mu A^\mu = 0$ — manifestly covariant
- **Coulomb gauge**: $\nabla \cdot \vec A = 0$ — useful for non-relativistic limit
- **Temporal gauge**: $\phi = 0$ — useful for canonical quantization

### 2.6 Charge conservation

Taking $\partial_\nu$ of the source equation $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$:

$$\partial_\nu \partial_\mu F^{\mu\nu} = \mu_0 \partial_\nu J^\nu$$

The left side is zero (antisymmetric $F$ contracted with symmetric $\partial \partial$). So:

$$\partial_\nu J^\nu = 0 \quad \Leftrightarrow \quad \partial_t \rho + \nabla \cdot \vec J = 0$$

Charge is conserved. This is **automatic** from Maxwell's equations — not a separate postulate. Substrate-mechanism: charge conservation is the substrate's $SO(2)$ Noether current (Volume 0 Chapter 8 conservation laws). T2473 (Lyra Friday May 22, 2026) formalizes substrate energy conservation; the EM-charge case is the U(1) analogue.

### 2.7 Worked example: Gauss's law for a point charge

For a point charge $q$ at origin: integrate Gauss's law over a sphere of radius $r$:

$$\oint \vec E \cdot d\vec A = \frac{q_{\text{enc}}}{\epsilon_0} \implies E(r) \cdot 4\pi r^2 = q/\epsilon_0$$

$$E(r) = \frac{q}{4\pi\epsilon_0 r^2}$$

The Coulomb field. From Maxwell ↔ Gauss for $\vec E$. Standard derivation.

Substrate reading: the point charge is a substrate $SO(2)$-charged K-type configuration; its $SO(2)$ connection field $A_0(r) = q/(4\pi\epsilon_0 r)$ falls off as $1/r$; the electric field $\vec E = -\nabla \phi$ falls off as $1/r^2$ (the substrate's natural Coulomb K-type radial dependence).

### 2.8 EM waves from Maxwell

Combining Maxwell's source-free equations in vacuum: $\nabla \times \vec E = -\partial_t \vec B$, $\nabla \times \vec B = \mu_0\epsilon_0 \partial_t \vec E$. Taking curl of Faraday:

$$\nabla \times (\nabla \times \vec E) = -\partial_t(\nabla \times \vec B) = -\mu_0\epsilon_0 \partial_t^2 \vec E$$

Using $\nabla \times (\nabla \times \vec E) = \nabla(\nabla \cdot \vec E) - \nabla^2 \vec E = -\nabla^2 \vec E$ (vacuum, $\rho = 0$):

$$\nabla^2 \vec E - \frac{1}{c^2}\partial_t^2 \vec E = 0$$

with $c = 1/\sqrt{\mu_0 \epsilon_0}$. Wave equation; speed of light $c$. Same for $\vec B$.

This is the foundation of EM waves (Chapter 5).

Substrate reading: EM waves are substrate photon K-type wave packets; the wave-equation derivation falls out of Maxwell, which falls out of substrate $U(1)$ gauge action — all substrate-mechanism.

### 2.9 K-audit anchors

- **T2470** (Lyra Friday May 22, 2026): charge Q from substrate SO(2) weight
- **T2473** (Lyra Friday May 22, 2026): energy conservation from substrate Noether (extends to charge for U(1))
- **K57 RATIFIED**: Bridge Objects (anchor for EM-gauge structure)
- **Volume 1 Chapter 8**: Yang-Mills gauge action for general G; U(1) is the abelian case

## Level 3 — 5th-grader accessibility

Maxwell's four equations describe everything classical electricity and magnetism does:
- **Gauss for E**: electric field lines start on positive charges, end on negative
- **No magnetic monopole**: magnetic field lines have no starts or ends; they always loop
- **Faraday**: a changing magnetic field creates an electric field (how generators work)
- **Ampère-Maxwell**: a current OR a changing electric field creates a magnetic field

In BST, these four equations aren't independent rules. They all follow from **one thing**: the substrate has a built-in $U(1)$ symmetry (it's the $SO(2)$ part of the substrate's structure), and the equations are what you get when you write down "what's the simplest field theory consistent with that symmetry?" Answer: Maxwell's. The substrate doesn't choose Maxwell — it *forces* Maxwell. As a bonus, charge conservation drops out automatically and the speed of light $c = 1/\sqrt{\mu_0\epsilon_0}$ becomes the substrate's natural EM propagation speed.

---

## What comes next

Chapter 3 develops electrostatics — Coulomb's law, potential, Gauss's law applications.

## Where to look this up

- **Standard Maxwell**: Jackson, Ch 1, 6
- **Differential-form treatment**: Misner-Thorne-Wheeler, *Gravitation*, Ch 4
- **Gauge theory**: Peskin and Schroeder Ch 15; Quigg, *Gauge Theories*
- **BST anchors**: T2470 charge, T2473 conservation, K57 Bridge Objects
- **Volume 0 Chapter 8**: substrate Noether currents
- **Volume 1 Chapter 8**: Yang-Mills gauge action
