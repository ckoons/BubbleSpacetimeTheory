# Substrate Derivation Table — how D_IV⁵ defines each Standard-Model characteristic

*Companion to `substrate_atlas.html` (interactive). Casey 2026-06-14: "a table that explains how each SM particle characteristic is defined/derived" + the atlas toy that visualizes the substrate in operation. **Honest status throughout — the map explains forms; the count moves only when forced.***

**Status legend:** **FORCED** = zero-input derivation, banked · **DERIVED\*** = derived, one gate pending · **IDENTIFIED** = closed form fits, derivation open · **OPEN** = mechanism not yet built · **FRAMEWORK** = structural/scale, not a dimensionless number.

**Count: 2 of 26 FORCED** (α, θ_QCD) + architecture derived + muon at the gate (→3).

## The weaving (operation)

> Heat energy → the substrate heat-semigroup `exp(−τH_B)` → cascade coefficients: **a₀ = Λ**, **a₁ = gravity (Einstein–Hilbert)**, **a₂ = running couplings**, **boundary terms = masses**. Particles are realized (emitted) at the **boundary**, where the trajectory's accumulated factors either **cancel** (→ π-free rational) or **remain** (→ π^(−1/2)) — the Gindikin tracking. Light = uncommitted boundary energy; matter = committed (concentrated). Mass = concentration.

## Architecture (the construction — the SM skeleton)

| Characteristic | Substrate origin | Math | Status |
|---|---|---|---|
| Gauge group SU(3)×SU(2)×U(1) | Spin(2·n_C) = Spin(10), tangent spin group | n_C=5 → 16 = chiral spinor | **DERIVED** |
| One generation = 16 | chiral spinor 2^(n_C−1) | 2⁴ = 16 = SM + ν_R | **DERIVED** |
| Three generations | three distinguished conformal scalar points | Δ = 0, (d−2)/2, d/2 | **DERIVED** |
| Hypercharges (all 6) | Y/2 = T_3R + (B−L)/2 ; B−L = color fiber | all exact | **DERIVED** |
| Anomaly cancellation | SO(10) has no cubic Casimir | automatic | **DERIVED** |
| Chirality | holomorphicity (parity steer) | SU(2)_R unread | **DERIVED** |
| spin-½ | Di spinor singleton at ν=2 (Flato–Fronsdal) | Δ_Di = 2 | **FRAMEWORK** |

## The 26 parameters

| # | Parameter | Substrate origin / trajectory | Math | Status |
|---|---|---|---|---|
| 1 | α (fine-structure) | projection from EM stratum; N_max=137=N_c³·n_C+rank | α = 1/137 | **FORCED** |
| 2 | θ_QCD | SO(10) marginality (no cubic Casimir) | θ_QCD = 0 | **FORCED** |
| 3 | m_e (reference) | ν=5/2 BF/self-shadow/Hardy; the log/running unit | BF-log 9/16 = N_c²/rank^(n_C−1) | IDENTIFIED |
| 4 | m_μ/m_e | ν=3/2 Rac singleton, □φ=0, Shilov S⁴; spread, dim SO(4)=6 | [(d_τ/d_μ)/vol(S⁴)]^6 = (24/π²)⁶ = 206.77 | **DERIVED\*** (FK=1 gate) |
| 5 | m_τ/m_e | ν=0 trivial rep / cone tip; discrete tiling cell count | g²(g+2^C₂) = 49·71 = 3479 (− ~1.77 odd-Peirce π^(−½)) | IDENTIFIED |
| 6 | sin²θ_W | corkscrew pitch / 3-strata projection | forced pitch (F108) | OPEN |
| 7 | α_s | strata projection + L-R intermediate scale M_R | — | OPEN |
| 8–13 | quark masses u,d,s,c,b,t | trajectory conjecture per sector + bulk-color | — | OPEN (gated on #418) |
| 14–17 | CKM (3 angles + phase) | trajectory-overlap between quark sectors; corkscrew windings | — | OPEN |
| 18–20 | neutrino masses | ν_R forced (in the 16); seesaw/Dirac scale | — | OPEN |
| 21–24 | PMNS (3 angles + phase) | trajectory-overlap, neutrino sector | 3/3 angles within 1σ | IDENTIFIED |
| 25 | Higgs vev v | the dimensionful anchor ℓ_B (cone-tip scale) | the one input scale | FRAMEWORK |
| 26 | Higgs mass m_H | the substrate potential | — | OPEN |

## Beyond the 26 (cosmology / gravity / composites)

| Characteristic | Substrate origin | Math | Status |
|---|---|---|---|
| Λ (cosmological constant) | a₀ heat-kernel coefficient (bulk volume term) | Λ = exp(−280), 280 = 2^N_c·n_C·g | IDENTIFIED |
| gravity / Newton G | a₁ heat-kernel coefficient (Sakharov-induced EH) | G = Bergman curvature | FRAMEWORK |
| photon (light) | U(1) field; Rac⊗Rac two-singleton composite | massless | FRAMEWORK |
| light → matter | boundary emission; committed vs uncommitted | committed light-emission = matter | FRAMEWORK |
| pion / mesons | composite quark–antiquark on the boundary | — | OPEN |
| proton/neutron | baryon trajectory (3 quarks); m_π decay threshold | p=uud, n=udd; ddd = Δ⁻ | OPEN |

## Honest reading

The architecture (the SM skeleton) is **derived**; two parameters (α, θ_QCD) are **forced** and banked; the muon is **derived** pending one gate (FK=1); several others are **identified** (closed forms that fit, sub-percent) but **not yet forced**; the rest are **open** research, much of it gated on #418 (the chiral content). The path from 2 → 26 is the program plan (`project_ALL_program_plan...`): ~4 forced *mechanisms* (concentration=mass, strata-projection, heat-kernel cascade) each forcing a group, cross-checked by over-determination. **The atlas shows how the substrate would produce each piece; the badges keep it honest about which pieces are forced versus mapped.**
