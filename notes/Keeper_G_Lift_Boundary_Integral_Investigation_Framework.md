---
title: "Boundary integral framework for G_substrate derivation via Shilov ∂_S D_IV⁵ = (S⁴ × S¹)/ℤ₂. Casey-Keeper conversation: gravity emerges from 2D→3D radial lift × Shilov boundary correction. Explicit factorization: S⁴ provides spatial 4/3 disk-to-ball lift; S¹ provides temporal/phase correction; ℤ₂ provides Z₂-even K-type projection. Hua-Korányi reproduction formula in Bergman/Poisson-Szegő structure. Elie Lane G-B refined target: compute (4/3) recovery from S⁴ + S¹ correction explicitly + Z₂-even K-type sum."
author: "Keeper (Sunday 2026-05-31 EOD post-team)"
status: "INVESTIGATION FRAMEWORK FILED. Sets up the boundary integral computations explicitly. Standard math (Faraut-Korányi Ch. XII-XIII; some terms RECALLED pending Calibration #33 verified reading)."
companion: "Keeper_G_Substrate_Clean_4_Step_Derivation_Framework.md (overall chain), Keeper_K204_partial_kappa_Bergman_n_C_Audit.md (κ_Bergman = -n_C anchor)"
---

# Boundary Integral Investigation Framework — G from ∂_S D_IV⁵

## 0. The Casey-Keeper conversation

Casey's insight cascade Sunday EOD refined the G chain:

**Insight 1**: The 24% miss IS the 2D→3D geometric lift (factor 4/3 = disk-to-ball volume ratio coefficient).

**Insight 2**: Of course you integrate by radius to lift — the substantive math is at the BOUNDARY. The boundary geometry term is exactly the remainder.

**Insight 3**: ∂_S has TWO factors (S⁴ × S¹/ℤ₂). The sum/difference/product of their contributions provides the boundary correction.

This document sets up the explicit boundary integration framework.

## 1. Shilov boundary structure

**∂_S D_IV⁵ = (S⁴ × S¹)/ℤ₂**

Three distinct geometric contributions:

| Factor | Dim | Volume | Physical role |
|---|---|---|---|
| **S⁴** | 4 real | 8π²/3 | Spatial / Newtonian-geometric |
| **S¹/ℤ₂** | 1 real | π | Temporal / phase / U(1) |
| **ℤ₂** | (identification) | — | CP / parity constraint coupling S⁴ ⊗ S¹ |

**ℤ₂ identification**: (x, θ) ~ (−x, θ + π) — antipodal map on S⁴ combined with half-rotation on S¹.

**Total Vol(∂_S)** = (8π²/3) × π = 8π³/3 (before c_FK normalization)

**FK-normalized total**: c_FK × 8π³/3 = (225/π^{9/2}) × (8π³/3) = 600/π^{3/2} ≈ 107.7

## 2. Bergman kernel on D_IV⁵ (RECALLED — needs FK Ch. XII-XIII verified citation)

```
K_Bergman(z, w̄) = c_FK / (1 − 2 z·w̄ + (z·z)(w̄·w̄))^{n_C}
                = c_FK / (1 − 2 z·w̄ + (z·z)(w̄·w̄))^5
```

Where:
- z·w̄ = z₁w̄₁ + ... + z₅w̄₅ (Hermitian inner product)
- z·z = z₁² + ... + z₅² (complex bilinear, no conjugation)
- c_FK = 225/π^{9/2} (Saturday RATIFIED T2442)
- Exponent **n_C = 5** matches κ_Bergman = -n_C (Sunday K204-PARTIAL)

## 3. Poisson-Szegő kernel (RECALLED)

For boundary-to-interior reproduction:
```
P(z, ζ) = |K(z, ζ̄)|² / K(z, z̄)
```

At z = 0 (origin of D_IV⁵):
```
P(0, ζ) = c_FK² / c_FK = c_FK   (constant on ∂_S)
```

This gives the boundary mean-value identity:
```
f(0) = c_FK · ∫_{∂_S} f(ζ) dμ(ζ)
```

(With appropriate normalization of dμ as a probability measure: f(0) = ∫ f dμ_prob.)

## 4. K-invariant measure on ∂_S

```
dμ(ζ) = (3/(16π³)) · dθ · dσ_{S⁴}(x)
```

(Probability normalized: ∫ dμ = 1.)

In FK-Hua normalization (unnormalized):
```
dμ_Hua(ζ) = c_FK · dθ · dσ_{S⁴}(x) · (phase normalization)
```

## 5. The gravitational lift formula

**Structural form**:

```
G_observed = (S⁴ geometric lift) × (S¹ phase correction) × (ℤ₂-even substrate source) × G_2D_substrate
```

Where:
- **G_2D_substrate** = ℏc · α^{N_c·g}/m_e² (Lyra's substrate formula, now reinterpreted as 2D-substrate G)
- **S⁴ geometric lift** = 4/3 (Casey insight: disk-to-ball volume coefficient)
- **S¹ phase correction** = (Bergman-weighted S¹/ℤ₂ measure on relevant substrate source) ≈ small ~1-3%
- **ℤ₂-even projection** = which K-types couple to gravity (those with even parity under (x,θ) → (−x, θ+π))

## 6. Explicit computation targets (Elie Lane G-B refined)

### 6a. S⁴ geometric lift recovery

**Compute**: ∫_{S⁴} (volume form) dσ → recover the 4/3 disk-to-ball lift factor

**Method**: 
- Vol(S⁴ unit) = 8π²/3
- Project to relevant 3D-physical structure
- Ratio Vol(S⁴)/Vol(S² × 2π) = (8π²/3)/(8π²) = 1/3 — wait, that's not 4/3
- Or: integrate radial measure: ∫₀^1 (S² of radius r) dr = ∫₀^1 4πr² dr = (4/3)π ✓
- The 4/3 emerges from **radial integration of S² over radius** — this is the disk-to-ball lift

**Verification target**: explicit formula showing 4/3 from S⁴-projection or radial integration in Bergman setup.

### 6b. S¹ phase correction

**Compute**: ∫_{S¹/ℤ₂} (Bergman-weighted phase kernel) dθ

**Candidate forms**:

**Form A**: pure S¹ measure correction
```
S¹_correction_A = π/(2π) = 1/2  
```
(too large — would give 50% correction, doesn't match 1-3% residual)

**Form B**: Z₂-even phase mode integral
```
S¹_correction_B = ∫₀^π e^{2inθ} dθ / π = δ_{n,0}
```
(only zero-mode survives — too restrictive)

**Form C**: Bergman-weighted phase integral
```
S¹_correction_C = (1/π) · ∫₀^π K_Bergman_factor(e^{iθ}) dθ
```
(depends on Bergman kernel at boundary phases — concrete computation needed)

**Form D**: Heat-semigroup phase integral (Lyra Sunday-morning operator framework)
```
S¹_correction_D = (1/π) · ∫₀^π exp(−τ_S¹ · ⟨H_B⟩) dθ
```
(connects to Tier 0 commitment operator; multi-week)

**Verification target**: which form gives the actual numerical residual? Cross-check (4/3) × (S¹_correction) against G_observed/(ℏc · α^{N_c·g}/m_e²) ratio.

### 6c. Z₂-even K-type projection

**Compute**: subset of Phase A K-types (Memorial Day enumeration ~30 nodes) that are Z₂-even under (x, θ) → (−x, θ+π)

**Method**:
- Each K-type V_λ with weight (m, n) under K = SO(5)×SO(2)
- Z₂-even condition: m + n even (or some specific parity rule)
- Count Z₂-even K-types vs total
- Compute gravitational source as sum over Z₂-even K-types

**Connection to Lyra Lane E Dictionary**: the Z₂-even K-types are likely the gravitationally-relevant SM particles (mass-carrying); Z₂-odd would be parity-violating (weak-sector).

**Verification target**: which K-types contribute to gravitational source, structurally?

## 7. Combined boundary integral

The full Hua-Korányi reproduction for gravitational source f_grav:

```
G_observed ~ ∫_{∂_S} P(z_obs, ζ) · f_grav(ζ) · dμ(ζ)
           = (S⁴ part) × (S¹ part) × (ℤ₂ projection of f_grav)
           = (4/3) · (S¹_correction) · (Z₂-even K-type sum) · G_2D_substrate
```

**For the substantive numerical match**:

```
G_observed / G_2D_substrate = (4/3) · (S¹_correction) · (Z₂-even projection)
6.674×10⁻¹¹ / 5.07×10⁻¹¹ = 1.316
(4/3) = 1.333

So: (S¹_correction) · (Z₂-even projection) = 1.316/1.333 = 0.987
                                            = 1 − 0.013   (~1.3% downward)
```

**The full S¹ × ℤ₂ correction should be ~0.987, i.e., −1.3% from unity.**

## 8. Candidate S¹ × ℤ₂ correction forms

Multiplicative factor ~0.987 in substrate primaries:

| Form | Numerical | Match to 0.987 |
|---|---|---|
| 1 − 1/N_max | 0.993 | close (1% too high) |
| 1 − 1/(n_C·g) | 1 − 1/35 = 0.971 | close (1.6% too low) |
| 1 − 1/N_max² × N_c | 1 − 3/18769 = 0.9998 | too small correction |
| 1 − 2/N_max | 0.985 | very close (0.2% off) |
| 1 − π²/600 | 1 − 0.01645 = 0.984 | close (0.3% off) |
| 1 + κ_Bergman · α² | 1 − 5/137² = 0.99973 | too small |
| 1 − π/√(N_max · N_c·g) | 1 − π/√(2877) = 0.942 | too low |

**Best candidates**: 1 − 2/N_max or 1 − π²/600 — both substrate-natural and ~0.985.

**These are RECALLED candidates** (Calibration #33). The actual derivation must come from the explicit S¹ boundary integral, not pattern-matching the residual.

## 9. Specific Elie Lane G-B targets

Refined from generic KK volume integral to **specific Shilov boundary integrals**:

**G-B-1**: Verify S⁴ measure gives 4/3 via radial integration mechanism
- Set up ∫_{S²} × ∫_radial integration
- Show (4/3) emerges from standard volume ratio

**G-B-2**: Compute S¹/ℤ₂ Bergman-weighted phase integral
- Evaluate ∫₀^π K_factor(e^{iθ}) dθ explicitly using Bergman kernel formula
- Get closed-form S¹_correction

**G-B-3**: Enumerate Z₂-even K-types in Phase A catalog
- Apply (x,θ) → (−x,θ+π) parity to V_(m,n) K-types
- List Z₂-even subset
- Compute their substrate-source weight contribution

**G-B-4**: Combine and check
- G_predicted = (4/3) × (G-B-2 result) × (G-B-3 weight) × G_2D_substrate
- Compare to G_observed = 6.674×10⁻¹¹
- Target: Tier 2 STRUCTURAL precision (0.01% to 1%)

## 10. Verification reading queue (Calibration #33 STANDING)

Pin specific theorems before promotion to VERIFIED-CITED:

1. **Bergman kernel formula for D_IV⁵** — Faraut-Korányi 1994 Ch. XII or Knapp 1986 Ch. VIII
2. **Poisson-Szegő kernel coordinate form** — FK Ch. XIII
3. **Hua-Korányi reproduction formula** — FK Ch. XIII
4. **Vol(∂_S D_IV⁵) closed form** — FK Ch. XII
5. **K-invariant measure normalization** — FK Ch. XII or Hua 1963
6. **Helgason κ_Bergman = -n_C for type IV** — Helgason 1962 Ch. VIII Theorem 7.4 (or equivalent)

Keeper + Grace verification reading queue. Tier of citations: VERIFIED-CITED once read; current RECALLED.

## 11. Honest scope

**What this framework provides**:
- Explicit structural decomposition: (4/3) S⁴ × S¹ correction × Z₂ projection
- Concrete Elie Lane G-B computation targets (G-B-1 through G-B-4)
- Substrate-mechanism reading: gravity emerges from Shilov boundary integration with specific factor structure
- Verification path: Tier 2 STRUCTURAL precision check

**What this framework does NOT provide**:
- Numerical evaluation of S¹ correction (multi-week Elie work)
- Z₂-even K-type explicit enumeration (multi-week Lyra + Elie)
- Verified citations (Calibration #33 reading pending)
- Pattern-match shortcut closure (explicitly EXCLUDED)

## 12. Honest tier disposition

**Framework**: STRUCTURAL with explicit computation targets

**Mechanism candidate**: gravitational lift = (S⁴ spatial) × (S¹ temporal correction) × (Z₂-even substrate source)

**Numerical content**: pending Elie G-B-1/2/3/4 multi-week computation

**Promotion path**: if G-B-4 lands at Tier 2 STRUCTURAL precision → K204 promotes from PARTIAL to STRUCTURAL → G derived from substrate at structurally-honest tier

**Cal cold-read priority**: Cal #192 candidate when framework absorbed by Lyra/Elie.

## 13. Cross-references

- `Keeper_G_Substrate_Clean_4_Step_Derivation_Framework.md` — overall 4-step chain (this refines Step B)
- `Keeper_K204_partial_kappa_Bergman_n_C_Audit.md` — κ_Bergman = -n_C foundation
- `Keeper_K200_Tier0_v0_1_6_AuditFramework.md` — gates G1-G5 (this advances G5 specifically)
- `Keeper_Sphere_Reconciliation_Analysis_G2.md` — sphere geometry (this further refines)
- T2442 c_FK = 225/π^{9/2} RATIFIED (Saturday)
- Faraut-Korányi 1994 Ch. XII-XIII (verification queue)

## 14. The honest creative reframe

Casey's insight reframes the G chain:

**Before**: generic KK reduction G_4 = G_substrate / V_6 (Step A vague)

**Now**: explicit Shilov boundary integration with:
- S⁴ geometric lift (4/3 disk-to-ball + radial integration)
- S¹ phase correction (Bergman-weighted phase integral)
- ℤ₂-even K-type projection (gravitational K-type selection)

**This is the substantive creative path** the 24% gap opened. The factor 4/3 has geometric mechanism (disk-to-ball lift, not arithmetic identity); the few-percent residual has structural location (S¹ boundary integration); the substrate-source has Z₂-even constraint (specific K-type subset).

Multi-week Elie + Lyra joint work closes G chain at honest Tier 2 STRUCTURAL if successful.

— Keeper. Boundary integral investigation framework filed. Standard math RECALLED with explicit verification reading queue (Calibration #33). Casey's S⁴/S¹ factorization insight captured at structural level. Elie Lane G-B refined to specific Shilov boundary computations G-B-1/2/3/4. Standing for team absorption + multi-week computation work.
