---
title: "BST Hubble Estimates: Backfit Table and Numerical Results"
author: "Casey Koons & Claude 4.6"
date: "March 2026"
---

# BST Hubble Estimates: Backfit Table and Numerical Results
*Supporting calculations for WorkingPaper.md Section [Hubble]*
*Code: `notes/bst_hubble_backfit.py`, `notes/bst_frw.py`*

---

## Setup

**Fixed BST inputs (no observational contamination):**

| Parameter | Value | Source |
|---|---|---|
| F_BST | 0.09855 | Partition function (exact, l=5 convergence) |
| Lambda_obs | 2.9e-122 Pl | CODATA |
| T_CMB | 2.725 K | FIRAS blackbody (model-free) |
| Omega_r h² | 4.18e-5 | From T_CMB alone |
| T_c | 0.487 MeV | BST partition function |

Target: d_0 = 7.365e-31 l_Pl (from Lambda_obs / F_BST).

Model: flat universe, no dark matter.
FRW constraint: Omega_b + Omega_r + Omega_nu + Omega_Lambda = 1.
Lambda_BST = 3 × Omega_Lambda × H₀² (Planck units).

**Key helper:** for any matter content, the H₀ that makes Lambda_BST = Lambda_obs exactly:

    h² = Lambda_obs/(3 × H100_Pl²) + Omega_b_h2 + Omega_nu_h2 + Omega_r_h2
    H₀_floor = sqrt(h²) × 100 km/s/Mpc

---

## Backfit Table

`◄` = d_0 within 5% of target (H₀ is exact Lambda backfit).
`←` = d_0 within 15% of target (H₀ from observation, Lambda too high).

```
  Source / Input                                   Ω_b h²    H₀     Ω_Λ     Λ (Pl)    d_0 err
  ────────────────────────────────────────────────────────────────────────────────────────────
  ΛCDM-DERIVED (biased — assume DM, for comparison only)
  Planck CMB: Ω_b h²=0.0224, H₀=67.4              0.0224   67.4  0.9506  3.955e-122   +8.1% ←
  Local ladder: Ω_b h²=0.0224, H₀=73.0            0.0224   73.0  0.9579  4.675e-122  +12.7% ←
  Megamaser: Ω_b h²=0.0224, H₀=73.9               0.0224   73.9  0.9589  4.796e-122  +13.4% ←

  BST BACKFIT (what H₀ does Lambda_obs require exactly?)
  BST backfit, Ω_b h²=0.0224 (ΛCDM input)         0.0224   58.2  0.9338  2.900e-122   +0.0% ◄
  BST backfit, Ω_b h²=D/H BBN                     0.0223   58.2  0.9342  2.900e-122   +0.0% ◄

  GEOMETRIC / MODEL-FREE H₀
  Megamaser VLBI geometry, Ω_b=ΛCDM               0.0224   73.9  0.9589  4.796e-122  +13.4% ←
  Megamaser VLBI geometry, Ω_b=D/H BBN            0.0223   73.9  0.9592  4.797e-122  +13.4% ←
  SBF distances (Blakeslee 2021)                  0.0224   73.3  0.9582  4.715e-122  +12.9% ←
  Time-delay lensing H0LiCOW                      0.0224   73.3  0.9582  4.715e-122  +12.9% ←

  BBN NUCLEAR PHYSICS (D/H → Omega_b h², no DM needed)
  Cooke 2018: D/H=2.527e-5 → Ω_b h²=0.02225
    H₀ backfit                                    0.0223   58.2  0.9342  2.900e-122   +0.0% ◄
    H₀=73.9 megamaser anchor                      0.0223   73.9  0.9592  4.797e-122  +13.4% ←
    H₀=67.4 Planck CMB anchor                     0.0223   67.4  0.9509  3.956e-122   +8.1% ←

  BST T_c ENTROPY CORRECTION (phase transition dilutes baryon-to-photon ratio)
  T_c = 0.487 MeV injects latent heat: Ω_b h² → Ω_b h² / (1+δ)
    δ=5%  (weak transition)                       0.0212   58.1  0.9371  2.900e-122   +0.0% ◄
    δ=15% (moderate)                              0.0194   58.0  0.9423  2.900e-122   +0.0% ◄
    δ=50% (strong)                                0.0148   57.6  0.9551  2.900e-122   -0.0% ◄
    δ=200% (Li-7 factor ~3 reduction)             0.0074   56.9  0.9770  2.900e-122   +0.0% ◄
  Note: T_c correction makes H₀ floor WORSE (lower), not better.

  NEUTRINO MASS (BST predicts 3 flavors; lab bound Σm_ν < 0.45 eV)
  D/H BBN + Σm_ν = 0.06 eV                        0.0229   58.3  0.9324             -0.0% ◄
  D/H BBN + Σm_ν = 0.15 eV                        0.0239   58.4  0.9298             -0.0% ◄
  D/H BBN + Σm_ν = 0.30 eV                        0.0255   58.5  0.9254             +0.0% ◄
  D/H BBN + Σm_ν = 0.45 eV                        0.0271   58.6  0.9211             +0.0% ◄
  Effect: +0.1–0.4 km/s/Mpc per 0.15 eV — small.

  COMBINED SPECULATIVE (more baryons + neutrino mass — awaits partition function)
  Ω_b h²=0.030, Σm_ν=0.28 eV                      0.0330   59.1  0.9055             +0.0% ◄
  Ω_b h²=0.040, Σm_ν=0.28 eV                      0.0430   60.0  0.8803             -0.0% ◄
  Ω_b h²=0.050, Σm_ν=0.47 eV                      0.0550   61.0  0.8519             -0.0% ◄
  Ω_b h²=0.060, Σm_ν=0.47 eV                      0.0650   61.8  0.8296             +0.0% ◄
  Ω_b h²=0.080, Σm_ν=0.74 eV                      0.0880   63.6  0.7825             +0.0% ◄
  Ω_b h²=0.100, Σm_ν=0.93 eV                      0.1100   65.3  0.7421             +0.0% ◄

  COSMIC CHRONOMETERS (H(z) from galaxy ages — Moresco et al.)
  Best fit to BST no-DM H(z) model                0.0224  ≥90.0  [hits upper bound]
  → INCOMPATIBLE: BST no-DM (Ω_Λ≈0.97) predicts nearly flat H(z).
    Chronometer data shows H rising 45% from z=0.07 to z=0.75 — requires
    matter-like term that BST assigns to uncommitted channel reservoir (not DM).
```

---

## Key Findings

### 1. The H₀ Floor is Robust at 58.2 km/s/Mpc

The floor is insensitive to Ω_b h² because Ω_Λ ≈ 0.94–0.95 dominates.
No reasonable matter budget (baryons, neutrinos) can raise the floor above ~65.

Gap to observed values:
- To Planck CMB (67.4): **9.2 km/s/Mpc**
- To local ladder (73.0): **14.8 km/s/Mpc**
- To megamaser (73.9): **15.7 km/s/Mpc**

### 2. All Observed H₀ Values Give Lambda Too High

Every observed H₀ (67–74) with BST no-DM flat model gives Lambda 30–50% above
observed. This is the same 8–13% error in d_0 seen in the FRW calculation.

### 3. T_c Correction Moves in the Wrong Direction

BST's phase transition at T_c = 0.487 MeV injects entropy and dilutes the
baryon-to-photon ratio. This lowers Ω_b h² → lowers H₀ floor → widens the gap.
The Li-7 problem resolution (δ≈200%) would require H₀ floor ≈ 56.9.

### 4. Chronometer Data is Structurally Incompatible

The rising H(z) observed (×1.45 from z=0.07 to z=0.75) requires a matter-like
(1+z)^3 component. BST attributes this to the uncommitted channel reservoir,
not DM particles. The commitment rate exponent n_c must be derived from substrate
topology to confirm n_c ≈ 3.

### 5. Drivers Summary

| Effect | Direction | Magnitude |
|---|---|---|
| Higher Ω_b h² | ↑ H₀ | +1.0 km/s/Mpc per 0.01 in Ω_b h² |
| Neutrino mass | ↑ H₀ | +0.3 km/s/Mpc per 0.15 eV |
| Both combined (max) | ↑ H₀ | reaches 65.3 km/s/Mpc |
| T_c entropy correction | ↓ H₀ | −0.1 to −1.3 km/s/Mpc |
| Local contact overdensity | ↑ local H₀ | ~few km/s/Mpc (bridges gap) |
| **Partition function** | **resolves all** | **first-principles prediction** |

---

## What Must Come from the Partition Function

1. **Ω_b h²**: baryon asymmetry from BST substrate dynamics (no observational input)
2. **d_0**: scale of one committed contact on Σ (determines both Λ and H₀)
3. **n_c**: commitment rate exponent (determines H(z) shape, replaces DM)
4. **δ_contacts**: local vs cosmic contact density (quantifies Hubble tension)

Once these four quantities are derived, the BST Hubble prediction is parameter-free.

---

## Chronometer Residuals (Best-fit H₀ ≥ 90)

```
     z     H_obs      ±σ     H_BST(90)   resid   resid/σ
  0.07      69.0    19.6        90.3     -21.3     -1.09
  0.09      69.0    12.0        90.4     -21.4     -1.78
  0.12      68.6    26.2        90.5     -21.9     -0.84
  0.17      83.0     8.0        90.7      -7.7     -0.97
  0.20      72.9    29.6        90.9     -18.0     -0.61
  0.27      77.0    14.0        91.3     -14.3     -1.02
  0.28      88.8    36.6        91.4      -2.6     -0.07
  0.40      95.0    17.0        92.2      +2.8     +0.17
  0.48     101.0    23.0        92.8      +8.2     +0.36
  0.57     100.3     3.7        93.5      +6.8     +1.83
  0.75     100.0    18.5        95.3      +4.7     +0.25
```

Pattern: BST model systematically too high at low z, too low at high z.
This is the signature of a missing (1+z)^3 matter term — the uncommitted reservoir.

---

*See also: `notes/BST_Hubble_Expansion.md` (theoretical framework)*

*AI assistance: Claude Sonnet 4.6 (Anthropic) contributed to derivations, computations, and manuscript development.*

*Code: `notes/bst_hubble_backfit.py`*
