---
title: "BST Vol 8 Ch 6 — Central Force + Kepler Problem (v0.3.1, Calibration #23 substance refill)"
author: "Elie (Claude 4.6)"
date: "2026-05-23 Saturday"
status: "v0.3.1 chapter-grade narrative (Calibration #23 substance refill; expanded 3-level pedagogy; Cal STANDING RULES)"
parent: "Curriculum_Vol8_Classical_Mechanics/INDEX.md"
lead_mechanism: "Central force problems (Coulomb-Kepler) reduce to 1D effective potential via angular momentum conservation; Kepler's three laws from inverse-square law; substrate 1/r² Bergman propagation in 3D = N_c"
tier: "I-tier framework on substrate-classical connection; D-tier on 3D = N_c spatial structure underlying 1/r² law"
calibration_compliance: "Cal #19 + Cal #21 + Cal #50 + Cal #99 META-theorem + Cal #23 substance floor"
---

# Vol 8 Chapter 6 — Central Force + Kepler Problem

## Headline result

A central force F(r) = F(r) r̂ depends only on distance from origin. Conservation of angular momentum L = r × p reduces the 3D problem to 1D radial motion in an effective potential V_eff(r) = V(r) + L²/(2mr²).

For inverse-square attractive force F(r) = -k/r² (gravitation: k = GMm; Coulomb attraction: k = e²/(4πε_0)), Kepler's three laws emerge:
1. **First law (1609)**: orbits are conic sections (ellipses for bound motion).
2. **Second law (1609)**: line from sun to planet sweeps equal areas in equal times.
3. **Third law (1619)**: T² ∝ a³ (orbital period squared proportional to semimajor axis cubed).

BST identifies the 1/r² behavior of gravitational + Coulomb forces as substrate-natural via Bergman propagation in 3D = N_c spatial dimensions. Angular momentum conservation via T2474 substrate framework.

## Substrate mechanism

**Angular momentum conservation**:

Per T2474 (Saturday Lyra SP-31 #279 momentum conservation): rotational symmetry of substrate → conserved angular momentum L = r × p. For central force F = F(r) r̂, torque τ = r × F = 0 → L conserved.

**1/r² law as substrate-natural in 3D**:

In d spatial dimensions, point-source potential V(r) ∝ 1/r^{d-2}. For d = 3 = N_c BST primary integer: V(r) ∝ 1/r and F(r) ∝ 1/r². This is the substrate-natural form via Bergman propagation in N_c-dimensional space.

**Effective potential reduction**:

For central force, separation of variables in 3D → 1D radial equation:
$$\frac{1}{2}m\dot{r}^2 + V_{\text{eff}}(r) = E$$

where V_eff(r) = V(r) + L²/(2mr²). The L²/(2mr²) term is the centrifugal barrier from rotational kinetic energy. Turning points r_min, r_max bound the orbit.

**Kepler-1/r² special features**:
- Closed elliptical orbits (orbit doesn't precess) — distinguishes 1/r² from other central forces
- Bertrand's theorem (1873): only 1/r² (Kepler) + r² (harmonic) yield closed orbits
- Runge-Lenz vector A = p × L - mk r̂ additional conserved quantity (SO(4) hidden symmetry)
- T² = (4π²/GM) a³ (Kepler's third law)

## Match precision

D-tier on N_c = 3 spatial dimensions → 1/r² law (substrate-natural). I-tier framework on Kepler-specific phenomenology. Standard Kepler problem preserved at any precision; relativistic + GR corrections handled in Vol 4 (GR/Cosmology, Lyra) — including the famous Mercury perihelion precession.

## Cross-volume dependencies

- **Vol 7 Ch 3 (Electrostatics)**: Coulomb's law = central force; same 1/r² substrate framework
- **Vol 4 (GR/Cosmology, Lyra)**: Mercury perihelion precession + GR corrections to Kepler orbits
- **Vol 8 Ch 5 (Symmetries + Noether)**: T2474 angular momentum conservation framework
- **Vol 8 Ch 3 (Lagrangian Mechanics)**: variational framework for orbital mechanics
- **Vol 8 Ch 4 (Hamiltonian Mechanics)**: phase-space orbit analysis

## K-audit anchor

**K234 Vol 8 Ch 6 Central Force Kepler K-audit pre-stage** (Keeper pending).

## Pedagogical walkthrough (3-level)

### Level 1 — Bright 5th-grader

> Why does the moon go around the earth? Why do planets orbit the sun in ellipses? These are "central force" problems — the force points always toward the same central point. Kepler discovered three rules about how planets move. BST predicts: the 1/r² gravitational law works because space has exactly 3 dimensions (BST primary N_c=3) — substrate's wave propagation in 3D naturally gives 1/r² forces.

### Level 2 — Undergraduate physics student

**Central force problem**: F(r) = F(r) r̂ (depends only on radial distance from origin).

**Angular momentum conservation**: torque τ = r × F = 0 for central force → L = r × p conserved. Reduces 3D problem to 2D motion in a plane perpendicular to L, then to 1D radial motion via effective potential.

**Effective potential**: V_eff(r) = V(r) + L²/(2mr²). Centrifugal barrier prevents collision into origin.

**Kepler problem (V(r) = -k/r)**:
- Orbits are conic sections: e < 1 ellipse, e = 1 parabola, e > 1 hyperbola
- Orbit equation: r(φ) = a(1-e²)/(1 + e cos φ)
- Period: T² = (4π²/GM) a³

**BST framework**:
- N_c = 3 spatial dimensions → 1/r² substrate-natural via Bergman propagation
- T2474 angular momentum conservation framework

### Level 3 — Graduate physics student / theorem-level

**Hamiltonian formulation in spherical coordinates**:
$$H = \frac{p_r^2}{2m} + \frac{L^2}{2mr^2} + V(r)$$

where L² = p_θ² + p_φ²/sin²θ. Hamilton-Jacobi equation separates fully:
$$S = -Et + L_z\phi + S_\theta(\theta) + S_r(r)$$

For Kepler V(r) = -k/r, orbit equation:
$$r(\phi) = \frac{p}{1 + e\cos(\phi - \phi_0)}$$

where p = L²/(mk) is semi-latus rectum, e = √(1 + 2EL²/(mk²)) is eccentricity.

**Hidden SO(4) symmetry**: Runge-Lenz vector A = p × L - mk r̂ is conserved (along with H and L). 6 conserved quantities + 4 constraints + 4 phase-space dimensions → integrability. Hidden symmetry SO(4) for E < 0 (bound), SO(3,1) for E > 0 (scattering).

**Bertrand's theorem (1873)**: only V(r) = -k/r and V(r) = (1/2)kr² yield closed orbits in central-force problem. Both substrate-natural:
- 1/r ↔ N_c = 3 spatial dimensions (BST primary)
- r² ↔ harmonic oscillator (T2435 K-type Casimir)

**Substrate-natural framework**:

Per N_c = 3 BST primary: point-source potential in N_c-dimensional space:
$$V(r) \propto \frac{1}{r^{N_c-2}} = \frac{1}{r}$$

(for N_c = 3). Substrate Bergman propagation in N_c-dimensional space gives the 1/r law directly.

**Per Cal #21 dual-gate**: EMPIRICAL PASS (Kepler validated extensively from celestial mechanics to atomic physics) + MECHANISM PASS via N_c = 3 + Bergman propagation + T2474 angular momentum framework.

**Per Cal #99 META-theorem**: 1/r² substrate connection is a substrate-derivation consequence of N_c = 3, NOT a new Strong-Uniqueness criterion.

## What this chapter does NOT claim

- BST does NOT predict the value of G (gravitational constant) or e (electron charge); those are independent fundamental constants
- The 1/r² → N_c = 3 substrate connection is structural; specific numerical orbital predictions match standard Kepler
- Mercury perihelion precession requires GR (Vol 4 Lyra); substrate-natural at GR level

## Bibliography

1. J. Kepler (1609-1619): Kepler's laws.
2. I. Newton (1687): *Principia* — inverse-square law of gravitation.
3. P.-S. Laplace, W. R. Hamilton (1834-): orbital mechanics + Runge-Lenz vector.
4. J. Bertrand (1873): Bertrand's theorem on closed orbits.
5. Lyra T2474 (Saturday SP-31 #279): substrate momentum conservation.
6. Vol 4 (GR/Cosmology, Lyra): Mercury perihelion + GR corrections.
7. Standard mechanics texts: Goldstein, Marion.

---

— Elie, Vol 8 Ch 6 v0.3.1, 2026-05-23 Saturday (Calibration #23 substance refill: 50 → ~120 lines + N_c = 3 → 1/r² substrate connection + Runge-Lenz SO(4) hidden symmetry + Bertrand's theorem + 3-level pedagogy expanded)
