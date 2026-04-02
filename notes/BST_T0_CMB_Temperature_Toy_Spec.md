---
title: "Toy Spec: CMB Temperature T₀ from D_IV^5"
author: "Keeper (spec) — Elie (build)"
date: "2026-04-02"
status: "SPEC — for Elie, April 3"
toy_number: "681 (claim from play/.next_toy)"
---

# Can BST Derive T₀ = 2.725 K?

## The Problem

Paper #15 currently uses 4 external inputs: G, ℏ, c, and **T₀** (CMB temperature today). If BST can derive T₀ from the five integers + fundamental constants, external inputs drop to 3. If T₀ AND A_s (scalar amplitude) are both derivable, external inputs drop to 2 — approaching a zero-input CMB.

Measured: **T₀ = 2.7255 ± 0.0006 K** (FIRAS, Fixsen 2009).

## Candidate Derivations

### Route A: Stefan-Boltzmann + BST Energy Density

The CMB energy density today is:
$$\rho_\gamma = \frac{\pi^2}{15} T_0^4$$
(natural units, ℏ=c=k_B=1)

If BST predicts the photon energy fraction of the total budget:
$$\Omega_\gamma = \frac{\rho_\gamma}{\rho_{\rm crit}} = \frac{\pi^2 T_0^4}{15 \times 3H_0^2/(8\pi G)}$$

From BST: Ω_γ h² = (4σ/c)T₀⁴/(3H₁₀₀²) where σ = Stefan-Boltzmann. If BST fixes both H₀ and the total budget (Ω_Λ=13/19, Ω_m=6/19), then T₀ is determined by the photon contribution to the radiation budget.

**Test**: Using BST's H₀=67.29, Ω_γ h² ≈ 2.47×10⁻⁵ (standard), solve for T₀.

### Route B: Recombination Temperature + Redshift

BST derives z_rec from α (Toy 676: z_rec = 1091.6). If BST also derives the recombination temperature T_rec:
$$T_0 = T_{\rm rec} / (1 + z_{\rm rec})$$

T_rec is the temperature at which hydrogen recombines. The Saha equation gives:
$$T_{\rm rec} \approx \frac{B_H}{k_B \ln(\eta^{-1} (m_e T)^{3/2}/n_\gamma)}$$

where B_H = 13.6 eV = α²m_e/2 is the hydrogen binding energy (already BST-derived).

The question: can BST derive T_rec purely from five integers + α + m_e?

### Route C: Dimensional Analysis from BST Scales

BST has natural energy scales:
- m_e = 0.511 MeV (derived from geometry)
- m_p = 6π⁵m_e = 938.272 MeV
- α = 1/137

A temperature scale from these:
- α²m_e/2 = 13.6 eV (hydrogen ionization)
- α²m_e/(2×z_rec) ≈ 13.6/(1092) ≈ 12.45 meV ≈ 144.5 K ← too high by 53×

Or:
- T₀ in eV: 2.725 K × k_B = 2.349×10⁻⁴ eV
- Ratio: T₀/m_e = 4.60×10⁻¹⁰
- Is this a BST ratio? 4.60×10⁻¹⁰ ≈ α⁴/(2×N_c×n_C) = α⁴/30 ≈ 9.4×10⁻¹⁰... factor of 2 off

Let me try: T₀ = α²m_e/(2(1+z_rec)) with z_rec from Saha
- = 13.6 eV / (1092 × k_B) = 144.7 K / k_B... no, this is the photon temperature at recombination divided by (1+z_rec), which SHOULD give T₀ = T_rec/(1+z_rec) ≈ 3000 K / 1092 ≈ 2.748 K.

Wait — that's close! T_rec ≈ 0.26 eV ≈ 3000 K. Then T₀ = 3000/1092 = 2.747 K (0.8% from measured).

The question is whether T_rec = 0.26 eV can be derived from BST without external inputs.

### Route D: Direct Integer Formula

Try combinations:
- 2.725 K × k_B = 2.349×10⁻⁴ eV = 0.2349 meV
- m_e × α⁴ = 0.511 MeV × (1/137)⁴ = 0.511/3.53×10⁸ = 1.448×10⁻⁹ MeV = 1.448×10⁻³ eV
- m_e × α⁴ / C₂ = 1.448×10⁻³ / 6 = 2.413×10⁻⁴ eV ≈ 2.80 K... **2.8% off!**

Check: m_e α⁴/C₂ = 0.511×10⁶ / (137⁴ × 6) eV = 511000 / (2.117×10⁹) eV = 2.414×10⁻⁴ eV
In Kelvin: 2.414×10⁻⁴ / 8.617×10⁻⁵ = 2.802 K. Measured: 2.7255 K. That's 2.8%.

Try: m_e α⁴/(C₂+1) = m_e α⁴/g = 2.414×10⁻⁴ × 6/7 = 2.069×10⁻⁴ eV = 2.401 K. Too low.

Try: m_e α⁴ × n_C/(C₂(C₂+n_C)) = m_e α⁴ × 5/(6×11) = m_e α⁴ × 5/66 = 1.829×10⁻⁵ eV. Too low.

Try Route B more carefully: T₀ = T_rec/(1+z_rec) where both are BST-derivable.

## Toy Specification

### Inputs
- Five BST integers: N_c=3, n_C=5, g=7, C₂=6, N_max=137
- Fundamental: m_e, ℏ, c, k_B, G (BST derives G from α and m_e)
- BST-derived: α=1/137.036, H₀=67.29 km/s/Mpc, z_rec=1091.6

### Compute

**Block 1 — Route A: From Ω_γ h²**:
1. Standard: Ω_γ h² = 2.47×10⁻⁵ (known relationship)
2. BST H₀ = 67.29 → h = 0.6729
3. Solve T₀ from Stefan-Boltzmann + BST radiation fraction
4. Compare to 2.7255 K

**Block 2 — Route B: T_rec/z_rec**:
1. BST z_rec from Toy 676 (Saha equation with BST α)
2. T_rec from BST: what determines recombination temperature?
3. Attempt: T_rec ≈ B_H/ln(η⁻¹) where B_H = α²m_e/2, η = BST baryon asymmetry
4. T₀ = T_rec/(1+z_rec)
5. Compare to 2.7255 K

**Block 3 — Route C: Integer formula search**:
1. Scan T₀ = m_e × α^p × (integer combo) for p=2,3,4,5
2. Integer combos from {N_c, n_C, g, C₂, N_max, rank, |W|, π}
3. Report all candidates within 3% of measured T₀
4. Rank by simplicity (fewer integers = better)

**Block 4 — Route D: Dimensional consistency**:
1. T₀ must have dimensions of energy (in natural units)
2. The only BST energy scales are m_e, m_p, α, and their combinations
3. Systematic: T₀/m_e = f(α, integers). What is f?

### Test Cases (5 total)

| # | Test | Target | Tolerance | Type |
|---|------|--------|-----------|------|
| T1 | Route A gives T₀ | 2.7255 K | ±1% | PASS/FAIL |
| T2 | Route B gives T₀ | 2.7255 K | ±1% | PASS/FAIL |
| T3 | Best integer formula < 1% | 2.7255 K | ±1% | PASS/FAIL |
| T4 | z_rec consistent with Toy 676 | 1091.6 | ±0.5% | PASS/FAIL |
| T5 | Formula uses only BST integers + α + m_e | Yes | Boolean | PASS/FAIL |

**PASS criteria**: At least ONE route gives T₀ within 1% using only BST-derivable quantities.

### Output

Standard toy format. Report all routes, their T₀ predictions, and which external inputs each requires. The goal is to find a route that needs ZERO external inputs beyond what BST already derives.

## Why This Matters

1. **External inputs 4→3** for Paper #15 CMB predictions
2. **The radiation budget is the last piece**: BST already derives H₀, Ω_Λ, Ω_m, Ω_b, z_rec. If T₀ follows, the entire FLRW cosmology is BST-derived.
3. **T₀ + A_s = zero-input CMB**: If both are derivable, BST predicts the full CMB power spectrum from pure geometry.

## AC Depth

Unknown until derivation found. Likely (C=3-5, D=0) — multiple integer inputs, zero depth.

---

*"The temperature of the universe 13.8 billion years after the Big Bang — from the same five integers that build the proton."*
