---
title: "Vol 7 Chapter 8 — Lagrangian Formulation of EM"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; EM Lagrangian L = -F²/4 from substrate Yang-Mills"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 8
load_bearing: "EM Lagrangian L = -F_{μν}F^{μν}/(4μ_0) from substrate U(1) Yang-Mills action; Maxwell as Euler-Lagrange of this Lagrangian"
---

# Chapter 8 — Lagrangian Formulation of Electromagnetism

## Level 1 — one sentence

The EM Lagrangian $\mathcal{L}_{EM} = -F_{\mu\nu} F^{\mu\nu}/(4\mu_0) - J^\mu A_\mu$ is the substrate's $U(1)$ Yang-Mills action restricted to the abelian case, and Maxwell's equations are the Euler-Lagrange equations of this Lagrangian with $A^\mu$ as field variable — the variational principle is the substrate's natural way of selecting which field configurations the substrate K-types support.

## Level 2 — graduate-physicist precision

### 8.1 The EM Lagrangian density

For the EM field plus a source current $J^\mu$:

$$\mathcal{L}_{EM} = -\frac{1}{4\mu_0} F_{\mu\nu} F^{\mu\nu} - J^\mu A_\mu$$

with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$.

In terms of $\vec E$ and $\vec B$:

$$\mathcal{L}_{EM} = \frac{1}{2}(\epsilon_0 E^2 - B^2/\mu_0) - \rho\phi + \vec J \cdot \vec A$$

Action: $S = \int d^4 x \, \mathcal{L}_{EM}$.

### 8.2 Maxwell from Euler-Lagrange

Variational principle: $\delta S / \delta A^\nu = 0$.

$$\frac{\partial \mathcal{L}}{\partial A_\nu} - \partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu A_\nu)} = 0$$

Computing: $\partial \mathcal{L}/\partial A_\nu = -J^\nu$. $\partial \mathcal{L}/\partial(\partial_\mu A_\nu) = -(1/\mu_0) F^{\mu\nu}$.

So Euler-Lagrange gives:

$$-J^\nu + \partial_\mu \frac{1}{\mu_0} F^{\mu\nu} = 0 \implies \partial_\mu F^{\mu\nu} = \mu_0 J^\nu$$

The source-equation form of Maxwell's equations.

The other Maxwell equation (Bianchi: $\partial_{[\mu} F_{\nu\rho]} = 0$) is automatic from $F = dA$.

Substrate-mechanism reading: the Lagrangian is the substrate's natural $U(1)$ Yang-Mills action. The variational principle is the substrate's "select stationary configurations" rule.

### 8.3 Gauge invariance of the action

Under $A^\mu \to A^\mu + \partial^\mu \Lambda$:
- $F^{\mu\nu}$ is invariant
- $J^\mu A_\mu \to J^\mu A_\mu + J^\mu \partial_\mu \Lambda = J^\mu A_\mu + \partial_\mu(J^\mu \Lambda) - \Lambda \partial_\mu J^\mu$

For conserved current ($\partial_\mu J^\mu = 0$), the action changes by a boundary term, leaving equations of motion invariant. Gauge invariance of EM is consistent with charge conservation (Noether's theorem).

### 8.4 Stress-energy tensor of EM

From the Lagrangian, the symmetric energy-momentum tensor:

$$T^{\mu\nu}_{EM} = \frac{1}{\mu_0}\left( F^{\mu\alpha} F^\nu{}_\alpha - \frac{1}{4} g^{\mu\nu} F_{\alpha\beta} F^{\alpha\beta}\right)$$

Components:
- $T^{00} = u = $ energy density $= (\epsilon_0/2)E^2 + (1/(2\mu_0))B^2$
- $T^{0i} = c \cdot$ Poynting vector $\vec S = \vec E \times \vec B / \mu_0$
- $T^{ij} = $ Maxwell stress tensor (force per area between EM fields)

Conservation: $\partial_\mu T^{\mu\nu}_{EM} = -F^{\nu\lambda} J_\lambda$ — exchange of energy-momentum between field and matter.

### 8.5 Trace of stress-energy tensor

$T^\mu_\mu = (1/\mu_0)(F^{\mu\alpha}F_{\mu\alpha} - F^{\alpha\beta}F_{\alpha\beta}) = 0$ — the EM stress-energy is traceless. This is a consequence of the conformal invariance of free EM (Section 8.6).

Substrate reading: tracelessness reflects the substrate's $SO(4,2)$ conformal symmetry inherited by the $U(1)$ gauge sector. Conformal invariance is broken only when we add masses (matter Lagrangians); the free EM Lagrangian is conformally invariant.

### 8.6 Conformal invariance

The free EM Lagrangian (no sources) is invariant under conformal transformations in 4D — the larger group including Lorentz transformations + dilations + special conformal. This is the $SO(4,2)$ structure from Volume 7 Chapter 7.

Substrate reading: conformal invariance of EM is the substrate's natural symmetry of its $U(1)$ gauge sector — the substrate-K-type structure of the photon respects the full conformal group.

### 8.7 Canonical quantization

Treating $A^\mu$ as a field operator with conjugate momenta $\pi^\mu = \partial \mathcal{L}/\partial(\partial_t A_\mu)$: Gauss law constraint, gauge fixing, ghost fields, BRST quantization — the full QED quantization story (Volume 1 Chapter 8 of this curriculum, or Peskin and Schroeder Ch 4-5).

Substrate reading: QED is the quantization of the substrate $U(1)$ gauge field; the photon as quantized excitation of $A^\mu$ corresponds to the substrate's Pin(2) integer-weight K-type creation operator.

### 8.8 K-audit anchors

- **Chapter 2**: Maxwell from substrate U(1) (Lagrangian foundation)
- **Volume 1 Chapter 8**: Yang-Mills gauge action (general G; abelian U(1) is the EM case)
- **Volume 7 Chapter 7**: SO(4,2) conformal symmetry

## Level 3 — 5th-grader accessibility

Lagrangian formulation: write down one number, the Lagrangian density $\mathcal{L}$, that depends on the field $A^\mu$ and its derivatives. Then find the field configurations that make the integrated action $S = \int \mathcal{L} d^4 x$ stationary (Euler-Lagrange equations). For EM: $\mathcal{L} = -F^2/4 - J \cdot A$. Out come Maxwell's equations. **Why bother**: the variational form is the natural framework for relativistic field theory, gauge invariance, and quantization. **In BST**: this is the substrate's $U(1)$ Yang-Mills action — the substrate's natural-action form for the abelian gauge sector. Same physics, more elegant math.

---

## What comes next

Chapter 9 develops multipole expansion and scattering.

## Where to look this up

- **Lagrangian EM**: Jackson Ch 12; Goldstein Ch 13
- **QED quantization**: Peskin and Schroeder Ch 4-5
- **BST anchors**: Chapter 2; Volume 1 Chapter 8
