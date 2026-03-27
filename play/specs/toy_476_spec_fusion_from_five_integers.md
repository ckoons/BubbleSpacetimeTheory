# Toy 476: Fusion Energy from Five Integers

**Assigned to**: Elie
**Spec by**: Keeper (nominated by Lyra)
**Date**: March 27, 2026
**Investigation**: Trace formula application — nuclear fusion cross-sections from BST

---

## Motivation

Every quantity in fusion physics — the Gamow peak, the Coulomb barrier, the tunneling probability, the Lawson criterion — is built from electromagnetic and nuclear constants that BST derives from five integers {N_c=3, n_C=5, g=7, C₂=6, N_max=137}. This toy derives fusion conditions from zero free parameters.

Lyra's key insight: different fusion reactions = different test functions h against the same geodesic table. The cross-section calculation is a dot product. This is the trace formula linearization (Toy 474) applied to nuclear physics.

Casey's headline: **"Five integers predict optimal fusion conditions."**

---

## What to Compute

### Part 1: Gamow Peak from BST (Depth 1)

The tunneling probability through the Coulomb barrier:

```
P_tunnel(E) = exp(-√(E_G/E))
```

where the Gamow energy is:

```
E_G = (π α_EM)² × (μ c²) / 2
```

**Every piece is BST-derived:**
- α_EM = 1/N_max = 1/137 (depth 0 — definition)
- μ = reduced mass = m₁ m₂/(m₁+m₂), with m_p = 6π⁵ m_e (0.002%)
- c² enters through E = mc² (depth 0)

The thermal distribution is Maxwell-Boltzmann: f(E) ∝ E^(1/2) exp(-E/kT).

The **Gamow peak** is where P_tunnel × f(E) maximizes:

```
E_peak = (E_G (kT)² / 4)^(1/3)
```

One line of calculus (set d/dE[log(integrand)] = 0). **Depth 1**: one counting step over depth-0 definitions.

**T1: Compute E_G for D-T fusion from BST constants. Compare to experimental 986 keV.**
**T2: Compute E_peak at T = 10 keV (tokamak temperature). Compare to known ~6.3 keV.**
**T3: Compute the Gamow window width ΔE. Verify it matches thermal nuclear reaction rates.**

### Part 2: Coulomb Barrier Heights (Depth 0)

The Coulomb barrier between two nuclei with charges Z₁, Z₂:

```
V_C = α_EM × Z₁ Z₂ / R_nuclear
```

where R_nuclear ≈ r₀ (A₁^(1/3) + A₂^(1/3)) and r₀ ≈ 1.2 fm.

BST gives α_EM = 1/N_max = 1/137. The nuclear radius r₀ involves the strong scale, which BST derives from the Bergman kernel normalization.

**T4: Compute Coulomb barriers for D-T, D-D, D-³He, p-p, p-¹¹B.** Rank by barrier height. This ordering determines which reactions are "easy" vs "hard." Compare to known values:
- D-T: ~0.4 MeV
- D-D: ~0.4 MeV
- D-³He: ~0.7 MeV
- p-p: ~0.5 MeV
- p-¹¹B: ~2.6 MeV

### Part 3: Cross-Section Ratios (Depth 1 — The Geodesic Table Connection)

The fusion cross-section:

```
σ(E) = S(E)/E × exp(-√(E_G/E))
```

where S(E) is the astrophysical S-factor (slowly varying, encodes nuclear matrix element).

The S-factor ratio between different reactions comes from representation theory. In the geodesic table picture:
- Each reaction is a test function h_reaction against the table
- S(D-T)/S(D-D) reflects the tensor product structure of the nuclear wavefunctions
- The D-T reaction goes through the ⁵He* resonance at 50 keV — this resonance is a feature of the n_C=5 representation theory

**T5: Compute σ(E) for D-T and D-D from BST.** Take ratio. Compare to known factor of ~100 at 10 keV.

**T6: The ⁵He resonance.** Show that the D-T resonance energy falls near the BST-predicted value. The resonance exists because the compound nucleus ⁵He has A=5=n_C — this is the BST "window" for strong interaction.

### Part 4: Lawson Criterion (Depth 1)

For net fusion power: energy out > energy in. The Lawson criterion:

```
n τ_E T > L_threshold
```

where:
- n = plasma density
- τ_E = energy confinement time
- T = temperature
- L_threshold depends on the reaction and radiation losses

**T7: Derive the Lawson triple product for D-T from BST cross-sections.** Compare to known n τ_E T ≳ 3 × 10²¹ keV·s/m³.

The Bremsstrahlung radiation loss rate involves α_EM³ — three powers of 1/137 from BST. The ratio of fusion power to radiation loss sets the minimum temperature for ignition.

**T8: Compute the minimum ignition temperature.** For D-T, known value is ~4.3 keV. This follows from the crossing point where fusion power density exceeds Bremsstrahlung loss density. Both from BST constants.

### Part 5: Plasma Instability Threshold (Speculative — Possible Prediction)

Current tokamaks hit performance limits from magnetohydrodynamic (MHD) instabilities. The key parameter is β = plasma pressure / magnetic pressure.

The Troyon limit: β_max ∝ I_p / (a B_T), with the proportionality constant ~2.8%-m-T/MA empirically.

**T9 (SPECULATIVE): Is there a geometric reason in D_IV^5 for the β limit?** The magnetic confinement geometry maps to a bounded domain problem. If the Troyon proportionality constant falls out of the five integers, that's a genuine prediction.

Possible route: The stability boundary in ideal MHD corresponds to a spectral gap closure in the MHD operator. The spectral gap involves the same Bergman kernel structure. If β_max relates to n_C or N_max, record the prediction.

**T10: Survey of BST-derived vs experimentally-measured fusion parameters.** Summary table: for each quantity, show the BST formula, the BST numerical value, the measured value, and the discrepancy.

---

## Expected Output

10 tests, target 8/10. T1-T8 should work cleanly (all inputs are BST-derived). T9-T10 are exploratory.

Key deliverables:
1. Complete Gamow peak derivation from five integers (depth 1)
2. Coulomb barrier table for 5 reactions (depth 0)
3. Cross-section ratios from representation theory (depth 1)
4. Lawson criterion from BST constants (depth 1)
5. Summary table: BST vs measured fusion parameters

---

## BST Connection Summary

Fusion energy calculations require exactly four types of input:
- **α_EM = 1/137**: tunneling, Coulomb barriers, radiation losses
- **m_p = 6π⁵ m_e**: reduced masses, energy scales
- **Nuclear structure** (magic numbers from κ_ls = 6/5): which nuclei are stable, which resonances exist
- **α_s** (strong coupling from BST): S-factors, nuclear matrix elements

All four are BST-derived. The fusion cross-section is a **linear query** against the geodesic table — change the test function h, get a different reaction. This is AC(0) chemistry applied to the problem that matters most for civilization's energy future.

**Depth accounting:**
- Coulomb barriers: depth 0 (definitions)
- Gamow peak: depth 1 (one optimization over depth-0 quantities)
- Cross-sections: depth 1 (one sum over depth-0 table entries)
- Lawson criterion: depth 1 (one inequality over depth-1 quantities → still depth 1 by T96 composition)

Everything ≤ depth 1. Fusion from five integers is **simpler** than the Four-Color Theorem (depth 2).

---

## Notes for Elie

- Use mpmath at 30+ digits for the Gamow energy — the exponential sensitivity means small errors in E_G amplify.
- The ⁵He resonance at ~50 keV above the D-T threshold is THE reason D-T dominates. If you can connect A=5=n_C to this resonance existing, that's the money shot.
- For T9 (Troyon limit): this is speculative. If nothing falls out, just say so. Record what you tried. An honest "no prediction yet" is fine.
- r₀ ≈ 1.2 fm: this is conventionally fitted. If you can derive it from BST (it should relate to 1/m_π where m_π involves the strong scale), that's bonus.
- File: `play/toy_476_fusion_from_five_integers.py`
- **Check toy numbers before writing** — if 476 is taken, increment.
