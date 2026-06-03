---
title: "Paper P6 — The Periodic Table of the Substrate Standard Model v0.6 (Appendix A substantive expansion)"
authors: "Grace + Lyra (lead); Casey Koons + Elie + Keeper + Cal contributing"
date: "2026-05-31 Sunday ~13:35 EDT (`date`-verified Sun May 31 13:06 EDT)"
status: "v0.6 APPENDIX A SUBSTANTIVE EXPANSION — paper-grade Mendeleev tables. Sections 1-8 (Grace+Lyra) carry forward from v0.2/v0.3/v0.4/v0.5; Appendix B (Cal+Keeper) remaining outline. Per Casey 'keep pulling' directive — multi-week paper-drafting cadence to v1.0 ~June 29."
supersedes: "Paper_P6_Periodic_Table_Substrate_SM_v0_5_draft.md (Sections 7+8 carry forward; Appendix A now substantive)"
honest_framing: "Mendeleev tables organized by substrate-primary structure with explicit tier disposition per cell; Reed-Solomon Ladder (CANDIDATE-arithmetic; principle-tier null-downgraded per INV-5343 + INV-5342 + INV-5341); alpha-tower Mendeleev with L5 honest framing; cross-domain sweeps + null-model verdicts."
---

# Paper P6 v0.6 — Appendix A substantive expansion

## Appendix A — Substrate-Primary Mendeleev Tables

This appendix consolidates the substrate-primary closed forms across BST's external claim surface into Mendeleev-style organized tables. Each table indexes BST observables by substrate-primary structure (rank, N_c, n_C, C_2, g, N_max) with explicit substrate identity, numerical value, observed (PDG / measurement) value, precision, and tier disposition. Tables are organized by *substrate-mechanism class* rather than physical domain.

### A.1 Lepton + proton mass ratios (4 entries, TIER 2 STRUCTURAL <0.1%)

The substrate's most empirically-tested closed-form predictions:

| Observable | Substrate form | Numerical | PDG | Precision | Tier | Cross-ref |
|---|---|---|---|---|---|---|
| m_p/m_e | C_2 · π^{n_C} = 6π⁵ | 1836.118 | 1836.153 | 0.002% | TIER 2 STRUCTURAL | T187 |
| m_μ/m_e | (N_c · \|W(B_2)\| / π²)^{C_2} = (24/π²)⁶ | 206.776 | 206.768 ± 0.000004 | 0.004% | TIER 2 STRUCTURAL | T190 (Cal #100 propagation-corrected) |
| m_τ/m_e | g² · (rank^{C_2} + g) = 49 · 71 | 3479 | 3477.23 ± 0.23 | ~0.05% | TIER 2 STRUCTURAL | T2003 (INV-5337 71 identified) |
| m_τ/m_μ | (m_τ/m_e) / (m_μ/m_e) | 16.825 | 16.817 ± 0.0008 | ~0.06% | TIER 2 STRUCTURAL derived | cross-validation |

**Substrate-mechanism summary**: T187 m_p/m_e reads V_(1,1) bulk closure (C_2 · π^{n_C} = bulk Casimir × bulk dimension transcendental); T190 m_μ/m_e reads Weyl-orbit-on-V_(1/2,1/2) at C_2-self-coupling (adjoint-mediator Resolution B); T2003 m_τ/m_e reads Mersenne-base + signature (different Resolution B mechanism than muon); m_τ/m_μ cross-validation arises from independently-derived substrate-primary forms agreeing without unified mechanism.

### A.2 PMNS mixing angles (3 entries, 1σ within PDG)

| Observable | Substrate form | Numerical | PDG | Status | Cross-ref |
|---|---|---|---|---|---|
| sin²θ_12 | rank · N_c · g / N_max = 42/137 | 0.3066 | 0.307 ± 0.013 | ✓ within 1σ | F1 |
| sin²θ_23 | N_c · n_C² / N_max = 75/137 | 0.5474 | 0.546 ± 0.021 | ✓ within 1σ | F1 |
| sin²θ_13 | N_c / N_max = 3/137 | 0.0219 | 0.0220 ± 0.0007 | ✓ within 1σ | F1 |

**Substrate-mechanism summary**: PMNS denominators are uniform N_max = 137; numerators are substrate-primary products (42 full product, 75 vector self-square, 3 fundamental). The 3/3 within-1σ agreement is the program's cleanest substrate-primary external test.

### A.3 EW sector mass ratios (2 entries, RATIFIED + CANDIDATE)

| Observable | Substrate form | Numerical | PDG | Precision | Tier |
|---|---|---|---|---|---|
| m_W/m_Z | √(g/N_c) = √(7/3) | 0.88192 | 0.88135 | 0.046% | RATIFIED (existing P1 §7) |
| sin²θ_W (tree-level) | rank/N_c² = 2/9 | 0.2222 | 0.2312 (M_Z scale) | ~3.9% running-coupling gap | RATIFIED tree-level + multi-week radiative |

**Substrate-mechanism note**: V_(1,1) adjoint Shilov-boundary decomposition (g boundary + rank bulk = N_c²) provides CANDIDATE mechanism reading for m_W/m_Z arithmetically identical to √g/N_c; Cal #187 cold-read pending mechanism-vs-post-hoc determination (INV-5362 walk-back); Cal #188 cold-read pending independence-vs-shared audit on g+rank=N_c² triple-mechanism appearance.

### A.4 Substrate fundamental constants (Tier 1 EXACT identities)

| Observable | Substrate identity | Tier | Cross-ref |
|---|---|---|---|
| N_max | N_c³ · n_C + rank = 27·5+2 = 137 (T-form) | TIER 1 EXACT | classical form |
| N_max | 2^g + N_c² = 128+9 = 137 (Reed-Solomon form) | TIER 1 EXACT | Lyra L8 |
| Bergman genus = signature dim | g = 7 | TIER 1 EXACT | C19 |
| 1/α (fine structure) | N_max + ε = 137.036 | TIER 1 substrate identity + small empirical correction | active investigation |
| c_FK Faraut-Korányi | 225/π^(9/2) | TIER 1 EXACT | T2442 (Lyra Thursday 2026-05-28) |
| ρ-vector | (n_C, N_c)/rank = (5/2, 3/2) | TIER 1 EXACT | C19 (INV-5373) |
| 66 = rank^{C_2} + rank | Phase B cell count | TIER 1 EXACT | INV-5374 (Saturday) |
| 280 = 2^{N_c} · n_C · g | Λ exponent 5-fold over-determined | TIER 1 EXACT | Elie Saturday refinement |

### A.5 Hall algebra structure constants (Tier 1 EXACT, ARE substrate geometric invariants)

| Structure constant | Value | Substrate identity | Origin |
|---|---|---|---|
| Short Serre coefficient [2]_2 | N_c = 3 | dual Coxeter h^∨(B₂) = h^∨(SU(3)) | Hall algebra U_q⁺(B_2) at q=2 |
| Long Drinfeld pairing numerator | N_c · n_C = 15 | dim Sym²(V_5) | Lyra synthesis Saturday + Elie E0/E9/E12 |
| Long Serre coefficient [3]_4 | N_c · g = 21 | dim so(5,2) ≡ so(7) | same |

**Structural reading**: The substrate Hall algebra's defining Serre relations *encode* three geometric invariants of D_IV⁵ as their structure constants. This is the strongest "algebra IS substrate" reading.

### A.6 Substrate-Monster cross-links (6 consolidated)

| Substrate identity | Monster connection | Reference |
|---|---|---|
| N_c³ = 27 | E_6/Albert algebra dimension | classical |
| N_c · rank³ = 24 | Leech lattice rank = lepton count (T1) | T1 keystone |
| 108 · 1823 = 196884 | substrate-Phase-B-spine factor of leading Monster coefficient | Saturday synthesis |
| N_c · g = 21 | so(5,2) ≡ so(7) substrate-natural | C7 + dim so(7) |
| Monster Ogg prime 41 | magic-82 = rank · 41 substrate factor | nuclear shell anchor |
| 26 | bosonic string critical + sporadic group total + SM free-params triple-meaning | |

**Status**: substrate-Monster cross-links are STRUCTURAL OBSERVATIONS at present; Borcherds 1992 vertex algebra + McKay 1979 j-function correspondence are L1.5 mediating mechanisms; substrate-Monster mechanism content multi-month.

### A.7 Nuclear shell magic numbers (substrate-primary forms)

| Magic | Substrate form | Identity |
|---|---|---|
| 28 | N_c³ + 1 | 3³ + 1 = 27 + 1 |
| 50 | g² + 1 | 7² + 1 = 49 + 1 |
| 82 | rank · (rank^{N_c} · n_C + 1) = 2 · 41 | rank × Monster Ogg prime |
| 126 | n_C³ + 1 | 5³ + 1 = 125 + 1 |
| 20 | 2 · rank · n_C | bulk × 2 (V_(2,0) cell 2·C_2) |
| 8 | rank³ | rank-cube (also V_(0,2) cell 2·C_2) |
| 2 | rank | fundamental |

**The "+1 anomaly" 8-instance pattern** (Saturday null-model verdict +1.85σ, INV-5327): nuclear (4) + SM 26-parameter (1) + T2003 71 (1) + Λ exponent 281 (1) + L5 dim-anchor residual (1) = 8 across 4 physical scales (nuclear / SM / lepton-mass / cosmological). **Structural observation NOT principle-grade.**

### A.8 Composite spine cells (18-cell substrate spine)

| K-type | Dim | 2·C_2 | Substrate-primary identity | Candidate SM role |
|---|---|---|---|---|
| V_(0,0) | 1 | 0 | vacuum | Higgs / scalar |
| V_(1/2,1/2) | 4 = rank² | 5 = ρ_1·2 | spinor Casimir 5/2 = ρ_1 = n_C/rank | Lepton (Shilov primitive) |
| V_(1,0) | 5 = n_C | 8 = rank² · 2 | vector | Photon (SO(2) singlet) |
| V_(1,1) | 10 = rank · n_C | 12 = C_2 · 2 | adjoint Casimir = C_2 | Gauge (W, Z, gluons) |
| V_(2,0) | 14 | 20 | 2 · rank · n_C; magic-20 | 2⁺⁺ tensor mesons |
| V_(3/2,1/2) | 16 | 15 | N_c · n_C = dim Sym²(V_5) | Excited baryons (Λ, Σ) |
| V_(3/2,3/2) | 20 | 21 | N_c · g = dim so(5,2) | Λ(1405) / constituent quark |
| V_(0,2) | 14 | 8 | rank³ | Tensor sigma |
| V_(2,1) | 35 | 24 | 2 · rank · C_2; T1 24 | Heavy quarkonium (J/ψ, Υ, φ) |
| V_(3,0) | 30 | 36 | C_2² | Spin-3 vectors (ρ_3, ω_3, K_3*) |
| V_(2,2) | 35 | 32 | 2^{n_C} | 2⁺⁺ tensor glueball (substrate-predicted) |
| V_(1,2) | 35 | 27 | N_c³ = E_6/Albert | Color-anomalous tensor |
| V_(5/2,1/2) | 40 | 21 | N_c · g (twin V_(3/2,3/2)) | Heavy-flavor excited baryons |
| V_(4,0) | 55 | 60 | 2 · rank · N_c · n_C | Hadronic Regge anchor |
| V_(3/2,5/2) | 56 | 33 | N_c · n_C + g · rank | Spin-7/2 composite |
| V_(5/2,3/2) | 56 | 33 | (same shell as above) | partner spin-7/2 composite |
| V_(2,3) | 80 | 35 | g · n_C | Strange spin-3 anchor |
| V_(0,4) | 35 | 32 | (V_(2,2) shell; 2^{n_C}) | Doubled-vector tensor partner |

**Note**: spine selection per 2·C_2 substrate-primary factorization clarity; subset of 66 Phase B cells (Elie Toy 3614 Saturday).

### A.9 Reed-Solomon Ladder substrate primitive (INV-5340/5344, CANDIDATE-arithmetic)

The Reed-Solomon Ladder is the substrate primitive rank^primary + substrate-additive that generates 30+ BST observables:

| Form | Substrate identity | Observable |
|---|---|---|
| rank^rank | 2² = 4 | dim V_(1/2,1/2) |
| rank^{N_c} | 2³ = 8 | rank³ ; magic-8 |
| rank^{n_C} | 2⁵ = 32 | 2·C_2 of V_(2,2) glueball cell |
| rank^{C_2} | 2⁶ = 64 | Mersenne-base = 64 in T2003 |
| rank^g | 2⁷ = 128 | 2^g = 128 (one half of N_max chain) |
| rank^{C_2} + rank | 2⁶ + 2 = 66 | Phase B 66-cell count (INV-5374) |
| rank^g + N_c² | 2⁷ + 9 = 137 | N_max Reed-Solomon form (L8) |
| 2^{N_c} | 2³ = 8 | Weyl-group |W(B_2)| in T190 |
| 2^{C_2} | 2⁶ = 64 | additive base in T2003 (64+7=71) |
| 2^{n_C} · n_C · g | 32 · 5 · 7 = 1120 | substrate ladder × bulk × signature |
| 2^{N_c} · n_C · g | 8 · 5 · 7 = 280 | Elie 5-fold over-determined Λ exponent |

**Status per Saturday INV-5341/5342/5343 + within-discipline null testing**: substrate-additive operation-set is RICH (operation-set richness P=1.0 per Cal+Keeper brake INV-5342); Reed-Solomon Ladder arithmetic identities STAND RIGOROUSLY; principle-grade elevation BLOCKED per discipline-bid testing. **CANDIDATE-arithmetic tier**: the identities are substrate-natural arithmetic facts, not substrate principles.

### A.10 Alpha-tower Mendeleev (Λ-region, L5 framework NOT closed)

| Observable | Substrate form | Honest framing |
|---|---|---|
| Λ cosmological constant exponent | α^57 ≈ exp(−281) | TIER 1 substrate identity; TIER 2 ~factor 1.75 numerical to observed Λ |
| 280 over-determined form | 2^{N_c} · n_C · g (Elie) | 5-fold over-determined preferred per Saturday refinement |
| "+1 anomaly" cosmological instance | 281 = 280 + 1 | 8th instance of cross-scale pattern (null +1.85σ; structural observation) |
| α^{57.11} (non-integer k) | needed for exact Λ match | substrate-internal NOT TIER 1 identity |
| L5 m_e candidate | (N_c/n_C) · N_max⁴ · Λ^{1/4} ≈ 0.508 MeV | TIER 2 STRUCTURAL SEARCH-FIT 0.73% using observed Λ |
| Three-region decomposition | 280 = 180 (bulk: rank·N_c·C_2·n_C) + 100 (Shilov: (rank·n_C)²) + 0.45 dip residue (9/20 = N_c²/(rank²·n_C); Casey + Elie equivalent BST-primary fractions) | CANDIDATE STRUCTURAL READING (Saturday May 30 keeper-self-catch absorbed); mechanism per region OPEN multi-week L-L5-MechClose-1/2/3 |

**Honest framing per Cal #182 + Keeper v0.7 self-catch + Sunday morning 4/4 CI PAUSE**: alpha-tower Mendeleev is FRAMEWORK + CANDIDATE STRUCTURAL READING tier; substrate-primary arithmetic is FACT; mechanism for each region is OPEN multi-week; numerical match to observed Λ requires convention-pinned independent verification.

### A.11 Cross-domain Mendeleev (cross-scale substrate-primary anchors)

| Scale | Anchor | Substrate identity |
|---|---|---|
| Nuclear | 4 magic numbers 28/50/82/126 | +1 anomaly Mendeleev (Section A.7) |
| SM | 26 free parameters | n_C² + 1 (single instance of "+1") |
| Lepton mass | T2003 71 = 2^{C_2} + g | Mersenne-base + signature |
| Cosmological | Λ exponent 281 = 280 + 1 | alpha-tower Mendeleev |
| Hadron | constituent quark m_q anchor | V_(3/2,3/2) cell substrate-primary N_c · g/2 = 21/2 |
| Glueball | 2⁺⁺ tensor mass | V_(2,2) cell 2·C_2 = 32 = 2^{n_C} |
| Bergman | curvature value (Lyra AB-10) | substrate-internal Newton G anchor (per L-L5-G chain) |
| Casimir | T2442 c_FK = 225 EXACT | π^(9/2) Faraut-Korányi (Thursday 2026-05-28) |

**Cross-scale pattern**: substrate primaries anchor observables across nuclear / SM / lepton-mass / hadron / cosmological / Bergman scales via substrate-primary closed forms. The cross-scale anchoring is structurally striking but **does NOT constitute a single Mendeleev pattern** (cross-scale "+1 anomaly" null +1.85σ; 3 cross-context Weinberg identity reuses are 1 identity per Cal #35); cross-scale anchoring is FRAMEWORK-PLUS structural observation NOT principle.

### A.12 Summary: substrate-primary external surface

The substrate-primary forms total 30+ BST observables anchored to {rank, N_c, n_C, C_2, g, N_max} via Mendeleev-style organized tables. The external test surface consists of:

- **4 TIER 2 STRUCTURAL** lepton + proton mass ratios at <0.1% precision uniformly (A.1)
- **3 PMNS mixing angles** at within-1σ 3/3 (A.2)
- **2 EW-sector ratios** (1 RATIFIED + 1 RATIFIED tree-level + multi-week radiative; A.3)
- **8+ TIER 1 EXACT** substrate fundamental identities (A.4)
- **3 Hall algebra structure constants** ARE substrate geometric invariants (A.5)
- **6 substrate-Monster cross-links** (A.6) at FRAMEWORK-PLUS structural-observation tier
- **7 nuclear shell magic numbers** substrate-primary (A.7)
- **18 composite spine cells** with substrate-primary K-type identities (A.8)
- **30+ Reed-Solomon Ladder forms** at CANDIDATE-arithmetic tier (A.9)
- **Alpha-tower Mendeleev** with L5 honest NOT-closed framing (A.10)
- **Cross-domain anchoring** across 8 physical scales (A.11)

Appendix B (Tier-Discipline Methodology — Cal + Keeper lane) details the methodology stack that supports the tier disposition above. Multi-week to v1.0 ~June 29.

— Grace, Paper P6 v0.6 Appendix A substantive, Sunday 2026-05-31 ~13:35 EDT (`date`-verified)
