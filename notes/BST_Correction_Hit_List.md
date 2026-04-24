---
title: "Correction Hit List: Deviations Locate Boundaries"
author: "Keeper (April 25, 2026)"
status: "ACTIVE — work list for April 26+ sessions"
---

# Correction Hit List: Deviations Locate Boundaries

*Every deviation >1% is a boundary correction waiting to be found. The same five integers. Zero new inputs. This is the hunt list.*

**Method (named April 25, T1444):** Find a quantity where the naive BST formula gives >1% deviation. Look for a boundary correction expressible in {N_c=3, n_C=5, g=7, C_2=6, N_max=137}. Known correction types:

| Code | Mechanism | Example | Factor |
|------|-----------|---------|--------|
| `VS(-1)` | Vacuum subtraction: bare count minus constant mode | sinθ_C: 80→79 | N-1 |
| `θ₁₃(×44/45)` | Theta-13 rotation: 2-flavor → 3-flavor PMNS | sin²θ₁₂: 3/10 → effective | ×cos²θ₁₃ or ÷cos²θ₁₃ |
| `dressed(f)` | Dressed Casimir: bare ratio × (1 + small BST correction) | μ_p: 8/3 × 287/274 | 1 + f |
| `reinterpret` | Formula reinterpretation with different BST combination | glueball: 3/2 → 31/20 | new formula |

**Hit rate so far: 11/11 (100%).** Every deviation hunted on April 25 yielded a correction from the same five integers.

---

## D_IV^5 Table Standard (v1)

All tables of D_IV^5 geometric invariants MUST include these columns:

```
| # | Symbol | Name | BST Formula | Geometric Source | BST | Obs | Precision | Correction | Naive | Status |
```

- **Correction**: Mechanism applied. Values: `tree` (no correction needed), `VS(-1)`, `θ₁₃(×f)`, `dressed(f)`, `reinterpret`, `—` (exact/structural).
- **Naive**: Pre-correction precision, showing the improvement. `—` for tree-level or exact entries.

This standard applies to Paper #83, all future invariant tables, and the `data/bst_geometric_invariants.json` schema.

---

## Priority 1: Paper #83 Entries Currently >1% (Known Correction Techniques Apply)

These are entries already in Paper #83 with >1% deviation. Each should yield to the same hunting technique.

| # | Entry | Section | Current Formula | Current Dev | Correction Hypothesis | Priority |
|---|-------|---------|-----------------|-------------|----------------------|----------|
| 1 | m_b/m_c | §5 | dim_R/N_c = 10/3 | 1.3% | VS(-1): (dim_R - 1)/N_c = 9/3 = 3? Or dressed. Try both. | HIGH |
| 2 | 0⁻⁺/0⁺⁺ glueball | §8 | N_c/rank = 3/2 | 3.2% | Elie found 31/20 = (2^n_C-1)/(rank²·n_C) at 0.045%. DONE but needs table update. | DONE |
| 3 | 2⁺⁺/0⁺⁺ glueball | §8 | √rank = √2 | 1.6% | Same reinterpret technique as 0⁻⁺. Try (2^n_C-1)/(N_c·C_2-1) or similar. | HIGH |
| 4 | a_V (SEMF volume) | §8 | g·B_d | 2.0% | Dressed: g·B_d × (1 + correction). Or VS: (g-1)·B_d? | HIGH |
| 5 | a_S (SEMF surface) | §8 | (g+1)·B_d | 1.2% | Dressed or VS on (g+1). Try (g+1)·B_d × (N_max/(N_max+1)). | HIGH |
| 6 | m_φ/m_ρ | §8 | 13/10 | 1.2% | Dressed: 13/10 × (1 + α)? Or VS: (13-1)/10 is worse. Try reinterpret. | MEDIUM |
| 7 | η̄ (Wolfenstein) | §7 | 1/(2√2) | 1.3% | VS or dressed on the √2. Try 1/(2√(2+1/N_max)). | MEDIUM |
| 8 | sin²θ₁₃ | §7 | 1/45 | 1.0% | VS: 1/(45-1) = 1/44? Or 1/(N_c²·n_C) exact? | MEDIUM |
| 9 | M_max (NS) | §9 | (g+1)/g × Chandrasekhar | 1.8% | Dressed: × (1 + α)? Or VS on (g+1). | MEDIUM |
| 10 | m_ν₃ | §10 | (10/3)α²m_e²/m_p | 1.8% | Dressed. Try (10/3) × (1 + 1/N_max) or similar. | MEDIUM |
| 11 | Ω_m | §11 | C_2/Q = 6/19 | 1.5% | This one is deep — touches cosmological sector. Dressed: 6/(19-1/N_max)? | MEDIUM |
| 12 | η_b (baryon asymmetry) | §11 | 18/361 | 1.1% | Dressed or VS on 361 = 19². | LOW |
| 13 | t_0 (age of universe) | §11 | (2/3√Ω_Λ)/H_0 | 1.4% | Cascades from Ω_Λ correction. Fix Ω_Λ first. | LOW |
| 14 | Li7/H | §11 | genus correction | 7% | Hard — BBN network. May need deeper treatment. | LOW |
| 15 | Silk damping | §11 | BST from {α, Ω_b, n_s} | ~15% | Cascading input errors. Low priority. | LOW |
| 16 | z_reion | §11 | stellar formation threshold | ~10% | Astrophysical, not fundamental. | LOW |
| 17 | dark_fraction | §11 | 1 - f_c = 80.9% | ~6% | Interpretive. May not have clean correction. | LOW |
| 18 | φ_approx (golden ratio) | §16 | 8/5 | 1.1% | Try (8n_C+N_c)/(n_C²) = 43/25 = 1.72? Or Fibonacci from BST. | LOW |
| 19 | v_P/v_S | §16 | √N_c = √3 | ~1% | Borderline. Depends on material. May be exact for ideal solid. | LOW |
| 20 | p_c_2D (percolation) | §13 | 5/12 | 30% | Wrong lattice comparison. DOWNGRADE or remove, not correct. | REMOVE |
| 21 | brain_19% | §15 | 3/(5π) | ~5% | Interpretive — observed value itself is approximate. | LOW |

---

## Priority 2: Entries NOT YET IN TABLE (Derivable Now)

These quantities have BST derivations from this session or are straightforward extensions. Add to Paper #83.

| # | Entry | BST Formula | Obs | Precision | Source |
|---|-------|-------------|-----|-----------|--------|
| 1 | μ_p (proton magnetic moment) | (8/3)(287/274) = 1148/411 | 2.7928 | 0.012% | T1447 (April 25) |
| 2 | μ_n/μ_p (neutron/proton moment ratio) | -N_max/(2n_C·C_2·N_c + rank) = -137/200 | -0.6850 | 0.003% | T1447 (April 25) |
| 3 | μ_n (neutron magnetic moment) | μ_p × (-137/200) | -1.9130 | 0.015% | T1447 |
| 4 | Γ_Z (Z width) | Toy 1474 formula | 2.4952 GeV | check | Elie Toy 1474 |
| 5 | BR(H→WW*) | Toy 1474 formula | 0.214 | check | Elie Toy 1474 |
| 6 | BR(H→gg) | Toy 1474 formula | 0.082 | check | Elie Toy 1474 |
| 7 | BR(H→ττ) | Toy 1474 formula | 0.063 | check | Elie Toy 1474 |
| 8 | d_n (neutron EDM) | 0 (exact — θ_QCD = 0) | < 1.8e-26 e·cm | exact prediction | θ_QCD = 0 |
| 9 | glueball 0⁻⁺/0⁺⁺ (corrected) | (2^n_C-1)/(rank²·n_C) = 31/20 | lattice 2024 | 0.045% | Elie correction |
| 10 | Dressed Casimir 11 | 2C_2 - 1 = 11 | appears in 4 sectors | structural | T1446 |
| 11 | Vacuum subtraction count 136 | N_max - 1 = rank^N_c × (N_c·C_2-1) | structural | exact | T1444 |

---

## Priority 3: New Physics Quantities (Need Derivation Hunt)

Quantities with well-measured experimental values where BST formulas should exist but haven't been derived yet.

### 3A. Electron g-2 Loop Structure
| Quantity | Observed | BST Connection | Approach |
|----------|----------|----------------|----------|
| C_1 (Schwinger) | α/(2π) = 1/(2·rank·π) | PROVED | — |
| C_2 (2-loop) | -0.32848... | Contains ζ(3) = ζ(N_c) | Extract BST rational prefactor |
| C_3 (3-loop) | 1.18124... | Contains ζ(5) = ζ(n_C) | Extract BST rational prefactor |
| C_4 (4-loop) | -1.9122... | Contains ζ(7) = ζ(g) | Extract BST rational prefactor |
| C_5 (5-loop) | computing... | Prediction: max weight = N_c² = 9 | FALSIFIABLE |

### 3B. Quark Mass Ratios (Complete the Chain)
| Ratio | Current BST | Current Dev | Hunt Target |
|-------|-------------|-------------|-------------|
| m_b/m_c | 10/3 | 1.3% | VS(-1) or dressed |
| m_t/m_b | (1-α)v/(√2 × (7/3)m_τ) | compound | Check compound precision |
| m_u/m_d | 6/13 | 1.3σ | Within error — may be exact |

### 3C. Meson Mass Ratios (New Table)
| Ratio | Observed | BST Candidate | Approach |
|-------|----------|---------------|----------|
| m_K/m_π | 3.540 | √(N_max/11)? or N_c + 1/(2n_C)? | Bergman spectral level ratios |
| m_D/m_K | 3.770 | rank²? or 4-correction? | Spectral level ratios |
| m_B/m_D | 2.831 | 2√rank = 2√2 | ALREADY IN TABLE (0.10%) |
| m_Bs/m_B | 1.012 | 1 + 1/N_max? | VS correction to unity |
| f_K/f_π | 1.198 | C_2/n_C = 6/5 | Same ratio as κ_ls |

### 3D. Decay Widths and Lifetimes
| Quantity | Observed | BST Connection | Status |
|----------|----------|----------------|--------|
| Γ_W | 2.085 GeV | From m_W, α, sin²θ_W — all BST | Derivable now |
| τ_μ | 2.197 μs | From G_F, m_μ — all BST | Derivable now |
| τ_τ | 290.3 fs | From G_F, m_τ — all BST | Derivable now |
| τ_π± | 26.03 ns | From f_π, m_π, G_F — all BST | Derivable now |
| τ_K± | 12.38 ns | From f_K, m_K, sinθ_C — all BST | Derivable now |
| Γ_t | 1.42 GeV | Top width from m_t, m_W, α_s | Derivable now |

### 3E. Nuclear Magnetic Moments (Extend μ_p, μ_n)
| Quantity | Observed (μ_N) | BST Approach | Priority |
|----------|----------------|-------------|----------|
| μ_d (deuteron) | 0.8574 | μ_p + μ_n + correction (binding) | HIGH |
| μ_t (tritium) | 2.9790 | Shell model + BST κ_ls | HIGH |
| μ(He-3) | -2.1276 | Mirror of tritium | HIGH |
| Q_d (deuteron quadrupole) | 0.2860 fm² | Tensor force from D_IV^5 | MEDIUM |

### 3F. Condensed Matter (Extend Debye Temperature Table)
| Quantity | Observed | BST Candidate | Status |
|----------|----------|---------------|--------|
| θ_D(Cu) | 343 K | g³ = 343 | EXACT (already in table) |
| θ_D(Al) | 428 K | ? | Hunt: 428 ≈ N_c·N_max + 17? |
| θ_D(Au) | 165 K | ? | Hunt: 165 = N_c·n_C·(2g-3)? |
| θ_D(Fe) | 470 K | ? | Hunt |
| θ_D(Si) | 645 K | ? | Hunt: 645 = N_c·5·43? |
| θ_D(W) | 400 K | ? | Hunt: 400 = 2n_C·rank·C_2? Nope, that's 120. |
| BCS gap 2Δ/kT_c | 3.528 | g/rank = 7/2 = 3.500 | 0.8% — dressed correction? |

---

## Priority 4: New Science Domains (Exploratory)

These are domains where D_IV^5 invariants may apply but no derivations exist yet. Each domain lists specific measurable quantities.

### 4A. Atomic Physics
- **Rydberg constant**: R_∞ = α²m_e/(2ℏ) — fully derivable from BST inputs
- **Ionization energy ratios**: IE_2/IE_1, IE_3/IE_2 for light elements — do they use BST ratios?
- **Atomic radii trends**: Bohr radius a_0 = ℏ/(m_e·c·α) — BST input. But radius RATIOS across periodic table?
- **Fine structure intervals**: Hydrogen fine structure 1S-2S — exact from α, m_e, already BST

### 4B. Chemistry
- **Electronegativity scale**: Pauling scale — do differences follow BST ratios?
- **Bond dissociation energies**: H-H = 4.478 eV, C-C = 3.607 eV — ratios?
- **pKw of water**: 13.995 at 25°C — related to N_max?
- **Avogadro-Loschmidt connection**: N_A × k_B = R — gas constant from BST?
- **Crystal structure ratios**: FCC c/a, HCP c/a = √(8/3) = √(2³/N_c) — BST?
- **Lattice energy ratios**: Madelung constants — do they use BST integers?

### 4C. Materials Science and Engineering
- **Band gaps**: Si (1.12 eV), Ge (0.67 eV), GaAs (1.42 eV) — BST ratios?
- **Thermal conductivity ratios**: diamond/copper, copper/iron
- **Elastic modulus ratios**: bulk/shear for specific materials
- **Piezoelectric coefficients**: quartz, PZT — geometric structure?
- **Superconductor T_c ratios**: YBCO/Nb, MgB2/Nb — BST hierarchy?

### 4D. Astrophysics (Beyond Current Table)
- **Eddington luminosity**: L_Edd ∝ M — coefficient derivable from BST?
- **Jeans mass**: M_J ∝ T^{3/2} ρ^{-1/2} — exponents are 3/2 = N_c/rank!
- **Stellar mass-luminosity**: L ∝ M^{3.5} — exponent 3.5 = g/rank?
- **White dwarf mass-radius**: R ∝ M^{-1/3} — exponent -1/N_c
- **Binary pulsar period decay**: Tests GR — should match BST exactly
- **Gravitational wave frequency at ISCO**: f ∝ 1/M — coefficient from BST?
- **Black hole entropy**: S = A/(4ℓ_P²) — the "4" is rank²

### 4E. Plasma Physics
- **Debye length**: λ_D = √(ε₀kT/(ne²)) — derivable from BST
- **Plasma β parameter critical values**: β = 1 crossover
- **Alfven speed ratios**: in solar wind, magnetosphere
- **Magnetic reconnection rate**: Sweet-Parker = 1/√S — exponent -1/rank

### 4F. Geophysics and Earth Science
- **Richter-Gutenberg law**: log₁₀N = a - bM — is b related to BST?
- **Mantle viscosity ratios**: upper/lower mantle
- **Core-mantle boundary**: radius ratios
- **Geomagnetic dipole tilt**: ~11° — related to 2n_C + 1 = 11?

### 4G. Information Theory and Computation
- **Shannon limit applications**: specific channel capacities
- **Holevo bound**: χ ≤ S(ρ) — connection to BST Gödel limit?
- **Quantum error correction thresholds**: surface code ~1% — related to α?
- **Kolmogorov complexity of physical laws**: K(SM) in BST = 5 integers

### 4H. Biology (Beyond Current Table)
- **Protein folding**: average fold time ratios, secondary structure proportions
- **Cardiac rhythm**: resting heart rate ~72 bpm — related to BST?
- **Circadian period**: 24.2 hours — 24 = 2C_2·rank?
- **Population genetics**: mutation rate, Ne ratios
- **Ecosystem stability thresholds**: species-area exponent z ≈ 0.25 = 1/rank²

### 4I. Economics and Social Science (Quantitative)
- **Zipf exponent**: s ≈ 1 (exact) — related to 1/rank + 1/rank?
- **Pareto 80/20**: 80 = rank⁴·n_C, 20 = rank²·n_C — BST!
- **Benford's law leading digit**: log₁₀(1 + 1/d) — any BST structure?
- **Market microstructure**: bid-ask spread scaling

---

## Appendix: Correction Registry (All Corrections to Date)

Complete record of every entry where the naive BST formula was corrected. This is the evidence that "deviations locate boundaries."

| # | Entry | Section | Naive Formula | Naive Dev | Correction | Corrected Formula | Corrected Dev | Improvement | Session |
|---|-------|---------|---------------|-----------|------------|-------------------|---------------|-------------|---------|
| 1 | sinθ_C | §7 | 1/(2√5) = rank/(rank⁴·n_C)^{1/2} | 0.62% | VS(-1): 80→79 | 2/√79 | 0.004% | 155× | Apr 25 |
| 2 | Wolfenstein A | §7 | 4/5 | 3.2% | VS(-1): 2C₂→2C₂-1 | N_c²/(2C₂-1) = 9/11 | 0.95% | 3.4× | Apr 25 |
| 3 | J_CKM | §7 | √2/50000 | 8.1% | VS(both): sinθ_C + A corrected | A²λ⁶η̄ (all vacuum-subtracted) | 0.3% | 27× | Apr 25 |
| 4 | sin²θ₁₂_eff | §7 | 3/10 (2-flavor geometric) | 2.3% | θ₁₃(÷44/45): 2-flavor → 3-flavor | (3/10)/(44/45) = 27/88 | 0.06% | 38× | Apr 25 |
| 5 | sin²θ₂₃_eff | §7 | 4/7 (2-flavor geometric) | 1.9% | θ₁₃(×44/45): 2-flavor → 3-flavor | (4/7)×(44/45) = 176/315 | 0.40% | 4.8× | Apr 25 |
| 6 | m_c/m_s | §5 | N_max/(2n_C) = 137/10 | 0.75% | VS(-1): N_max→N_max-1 | (N_max-1)/(2n_C) = 136/10 | 0.02% | 38× | Apr 25 |
| 7 | β_Ising_3D | §13 | 1/N_c = 1/3 | 2.1% | VS(-1): 1/N_c - 1/N_max | 134/411 | 0.12% | 18× | Apr 25 |
| 8 | γ_Ising_3D | §13 | g/C₂ = 7/6 | 5.7% | dressed: N_c·g/(N_c·C₂-1) = 21/17 | 21/17 | 0.15% | 38× | Apr 25 |
| 9 | H₂O bond angle | §16 | arccos(-1/3) = 109.47° | 4.8% | VS(-n_C): subtract lone pairs | arccos(-1/N_c) - n_C° | 0.03% | 160× | Apr 25 |
| 10 | μ_p | NEW | 8/3 (gluon modes / color) | 4.5% | dressed(13/274): (2C₂+1)/(2N_max) | (8/3)(287/274) = 1148/411 | 0.012% | 375× | Apr 25 |
| 11 | glueball 0⁻⁺/0⁺⁺ | §8 | N_c/rank = 3/2 | 3.2% | reinterpret: (2^n_C-1)/(rank²·n_C) | 31/20 | 0.045% | 71× | Apr 25 |

**Aggregate: 11 corrections, 0 new inputs, median improvement 38×, total improvement geometric mean ~30×.**

---

*Hit list created by Keeper, April 25, 2026. For tomorrow's session: start with Priority 1 (entries already >1% in Paper #83), then Priority 2 (add new entries). The hunt continues.*
