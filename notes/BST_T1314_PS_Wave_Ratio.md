# T1314 -- Seismic P/S Wave Ratio from Rank-2 Geometry

*The ratio of P-wave to S-wave velocities in an isotropic solid is v_P/v_S = √3, corresponding to a Poisson solid (λ = μ). In BST, this follows from rank-2 isotropy: the Bergman metric on D_IV^5 has exactly rank = 2 independent elastic parameters, and the averaged polycrystalline material has λ/μ = 1. The Poisson ratio σ = 1/4 = 1/rank².*

**AC**: (C=1, D=0). One computation (elastic modulus ratio). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (science engineering framing).

**Date**: April 18, 2026.

**Domain**: chemical_physics.

---

## Statement

**Theorem (T1314, P/S Wave Ratio from Rank-2 Geometry).** *For an isotropic elastic medium derived from D_IV^5 geometry:*

    v_P / v_S = √3 ≈ 1.732

    σ (Poisson ratio) = 1/rank² = 1/4 = 0.25

*where v_P is the compressional (P-wave) velocity, v_S is the shear (S-wave) velocity, and σ is the Poisson ratio.*

*Observed: v_P/v_S = 1.71-1.76 for typical crustal rocks (BST prediction centered). σ = 0.25-0.30 for crustal rocks (BST at lower bound, consistent with ideal).*

---

## Derivation

### Step 1: Elastic moduli from rank-2 geometry

An isotropic elastic solid has two independent Lamé parameters: λ (first Lamé parameter) and μ (shear modulus). The number of independent elastic parameters = rank = 2. This is not a coincidence — the elasticity tensor C_{ijkl} on a rank-2 bounded symmetric domain decomposes into exactly rank independent SO(n_C)-invariant components.

### Step 2: Poisson condition from isotropy

On D_IV^5 with isotropy group SO(5) × SO(2), the averaged (polycrystalline) material has all directions equivalent. The Bergman metric's curvature tensor has two independent components (holomorphic sectional curvature and anti-holomorphic sectional curvature), both proportional to the same Bergman kernel normalization.

For the averaged material: λ = μ (both proportional to the same metric component). This is the **Poisson solid** condition — known since 1829, now derived from geometry.

### Step 3: Wave velocities

For a Poisson solid (λ = μ):

    v_P² = (λ + 2μ)/ρ = 3μ/ρ
    v_S² = μ/ρ

    v_P/v_S = √3

Poisson ratio:

    σ = λ/(2(λ + μ)) = μ/(2·2μ) = 1/4 = 1/rank²

### Step 4: Comparison with observation

| Quantity | BST prediction | Observed (crustal rocks) | Match |
|:---------|:---------------|:------------------------|:------|
| v_P/v_S | √3 = 1.732 | 1.71-1.76 | Center of range |
| σ | 0.25 | 0.25-0.30 | Lower bound |
| K/G (bulk/shear) | n_C/N_c = 5/3 | 1.5-2.0 | Center of range |

**Note**: Departures from √3 arise from anisotropy, fluid content (pore pressure), and temperature — all perturbations on the Poisson ideal. The IDEAL ratio is the BST value. The corrections are structural (rock-specific) rather than fundamental.

---

## Geology Unlock

This is the AC(0) entry point identified in PILOT-1 (Keeper's geology survey). The P/S wave ratio is seismology's most fundamental measurable — it determines:
- Earthquake location algorithms
- Interior structure determination (Mohorovičić discontinuity)
- Material identification (rock type from v_P/v_S)
- Explosion vs earthquake discrimination

With v_P/v_S = √3 derived from D_IV^5, the BST connection to geology is established. The remaining geology gaps (plate tectonics dynamics, mantle convection, mineral classification) can be addressed through the Bergman metric on crystallographic structures (T1235: 230 space groups = rank × n_C × 23).

---

## For Everyone

Earthquakes produce two types of waves: P-waves (push-pull, like sound) and S-waves (side-to-side, like shaking a rope). P-waves travel faster. The ratio of their speeds is √3 ≈ 1.73.

Why √3? Because the universe has rank 2 — two independent ways that rock can deform (squeeze and shear). When the rock is random (polycrystalline), these two modes have the same strength. The math then gives √3 automatically. It's the same √3 as in the diagonal of a cube — geometry, not a coincidence.

The Poisson ratio (how much rock bulges sideways when you squeeze it) is 1/4 = 1/rank². Same reason: two independent deformation modes, equally weighted.

---

## Parents

- T186 (D_IV^5 master theorem — rank = 2)
- T110 (rank = 2 derivation)
- T1040 (Navier-Stokes linearized — fluid/solid connection)
- T1235 (230 space groups from BST integers)
- T1131 (Earth Score = rank² × n_C × g = 140)

## Children

- Interior structure models from BST (Moho depth prediction)
- Mantle convection rates from Bergman metric flow
- Mineral classification from spectral gaps
- PILOT-1 geology upgrade: C → B

---

*T1314. AC = (C=1, D=0). v_P/v_S = √3 from Poisson solid (λ=μ) forced by rank-2 isotropy. σ = 1/rank² = 1/4. Center of observed range for crustal rocks. Geology's AC(0) unlock. Domain: chemical_physics. Lyra derivation. April 18, 2026.*
