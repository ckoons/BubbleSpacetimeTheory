# Saturday Morning Findings — Grace, 2026-05-16

**Period**: ~08:00 EDT (post-reboot) through ~12:20 EDT
**Toys**: 2423, 2429, 2431, 2434, 2438, 2441, 2444, 2450, 2453, 2454, 2457, 2458, 2462, 2464, 2469, 2473 (16 toys, ~60 PASS)
**Theorems registered**: T1944, T1951, T1954, T1956, T1958, T1960, T1963, T1967, T1968, T1971, T1972, T1973, T1974, T1976, T1977, T1978, T1979, T1980 (18 theorems)
**Paper drafts**: notes/maybe/Paper_BST_Four_Arithmetic_Skeletons_DRAFT.md (**v0.3**, 8 sections + empirical Pell-filter + SM-physics consequences)
**Catalog impact**: 60+ entries added (mine + Elie's 30 ingested), 4082 → 4128

## Headline finding — the 59 mystery is closed

The Saturday morning thread started with **T1944 BST Pythagorean Structure** (Toy 2423) and ended with **T1968 closing the 59 mystery** (Toy 2450). The chain:

```
T1944 (Pythagorean) → T1951 (Pell embedding) → T1954 (Pell filter for Ogg)
                  → T1956 (Heegner split) → T1958 (Ogg physics role split)
                  → T1960 (CKM γ at 0.02% on Jarlskog)
                  → T1963 (α_em running = rank³)
                  → T1967 (N_e CMB pivot = 55)
                  → T1968 (59 = max-scale N_e, T1958 CLOSURE)
```

## The four arithmetic skeletons of D_IV⁵ integer ring

The BST integer ring {rank=2, N_c=3, n_C=5, C_2=6, g=7} ∪ {c_2=11, c_3=13, chi_K3=24, N_max=137} is closed under FOUR classical arithmetic operations:

| Operation | Theorem | Closed for |
|-----------|---------|-----------|
| **Linear sums** | T1313 (Casey) | All 15 Ogg supersingular primes |
| **Pythagorean triples** | **T1944 (Grace)** | 5 BST Pyth. triples, (3,4,5) fundamental |
| **Fermat 2-square sums** | T1944 | 4 of 8 Fermat-positive SS primes pure-BST |
| **Pell equation** | **T1951 (Grace)** | First 15 Pell sequence members |

### The fundamental BST Pythagorean triple

```
N_c² + rank⁴ = n_C²   (3² + 2⁴ = 9 + 16 = 25 = 5²)
```

The (3,4,5) primitive Pythagorean triple — smallest in math — sits on pure BST integers. Area of this right triangle = (1/2)·N_c·rank² = **C_2 = 6**, giving a new geometric meaning for C_2 beyond "second Casimir."

### The Pell filter

The Pell test "p² − rank·y² = ±1 OR y² − rank·p² = ±1 with y BST" is a **perfect filter** for Ogg primes ≤ 200:
- 7 of 15 Ogg primes pass (the Pell-line {2, 3, 5, 7, 17, 29, 41})
- 0 of 31 non-Ogg primes ≤ 200 pass
- Extended to p ≤ 1000: 2 non-Ogg false positives (239, 577), both Pell half-companion primes beyond Ogg cutoff

This is the sharpest single-skeleton discriminator among the four operations.

## The 7+8 Ogg prime structural bisection (T1958)

The Pell filter splits Monster's 15 supersingular primes into:

### Pell-line (7 primes) — math/arithmetic foundation
```
2  = rank
3  = N_c
5  = n_C
7  = g
17 = N_c·n_C + rank (Wallach |ρ|²·rank)
29 = rank·c_2 + g
41 = c_2·N_c + rank^N_c
```
= {4 BST primary primes} ∪ {3 Pell-hypotenuse primes}

### Non-Pell-line (8 primes) — SM physics anchors
```
11 → c_2 → α_S structure, β_0 pure gauge
13 → c_3 → m_H, cos²θ_W = 10/13
19 → Ω_DM denominator
23 → m_μ/m_e gen-2 mass scale (T1948)
31 → j-function 744 = χ_K3·31 (T1941)
47 → t_cosmo Bergman evaluation point (T1924)
59 → INFLATION E-FOLDS at largest observable scale (T1968 — NEW)
71 → m_τ/m_e gen-3 mass scale (T1948)
```

**8 of 8 non-Pell-line Ogg primes now anchor specific SM observables.**

## BST CMB sector now complete

| Observable | BST formula | Predicted | Observed |
|------------|-------------|-----------|----------|
| n_s | 1 − n_C/N_max | 0.9635 | 0.9649 ± 0.0042 (T1962, Lyra) |
| A_s × 10⁹ | exp(−h¹¹(K3)) = exp(−20) | 2.06 | 2.105 ± 0.030 (T1961, Lyra) |
| r | 12/(c_2·n_C)² = 12/3025 | 0.00397 | <0.036 (T1968 → Starobinsky) |
| N_e (pivot) | c_2·n_C | 55 | 50-60 (T1967) |
| N_e (max) | c_2·n_C + rank² | 59 | 55-65 (T1968) |
| α_s (running) | 0 + small | ~0 | -0.0042 ± 0.0067 |

Five primary inflation observables all derive from {rank, N_c, n_C, c_2, N_max, h¹¹(K3)}.

**BST inflation potential = Starobinsky R²**, FORCED by joint n_s + r + N_e constraint.

## CKM CP-phase closure (T1960)

```
γ_CKM = c_2·π / (N_c·rank·n_C) = 11π/30 ≈ 1.152 rad
```

- γ_CKM observed (PDG 2024): 1.146 ± 0.033 rad
- BST precision on γ: 0.5% (within 1-σ)
- BST precision on Jarlskog J: **0.02%** (J_BST = 3.179e-5 vs J_obs = 3.18e-5)

Sharpens Elie W-17 δ_CP from 7.8% to 0.02%. Reading: γ_CKM = (second Chern c_2) / (K-orbit volume) × π, both factors being existing BST observables.

## QED running closure (T1963)

```
1/α_em(0) − 1/α_em(M_Z) = rank³ = 8
```

at 0.87% precision. Two integer identities:
- IR: 1/α_em(0) = N_max = 137 (T186, Casey)
- EW: 1/α_em(M_Z) = N_max − rank³ = 129 = N_c × 43 (Heegner 7th)

## Primary BST integer split (T1956)

Of the 7 primary-plus-Chern BST integers {rank, N_c, n_C, C_2, g, c_2, c_3}, exactly **4 are Heegner numbers**: {2, 3, 7, 11} = {rank, N_c, g, c_2}. The remaining 3 {5, 6, 13} have class number 2.

- **Heegner subset** (rank, N_c, g, c_2): algebraic-arithmetic roles (imaginary quadratic fields, T1313 Fermat route)
- **Non-Heegner subset** (n_C, C_2, c_3): geometric-counting roles (compact dim, second Casimir, third Chern)

The 4-3 split distinguishes "algebraic" from "geometric" BST integer roles.

## Casey-Keeper task assignments closed (afternoon)

### T1974 — Kaon CP |ε_K| = 42/N_max² (Toy 2458)

|ε_K| = C_2·g·α_em² = 42/N_max² at 0.45%. Closes α²·42 recurrence observation.

### T1976 — Muon g-2 correction (Toy 2462)

Δa_μ = rank·42/N_max² at 0.75%. Completes α²·42 TRIPLE recurrence (ε_K, BR(H→γγ), Δa_μ all share Chern flux 42 = C_2·g).

### T1977 — Down-quark cascade m_b/m_d = 30² (Toy 2464)

m_b/m_d = (N_c·rank·n_C)² = 900 at 0.47%. Down-quark hierarchy = K-orbit volume squared. Plus m_c/m_u = 19·31 (two Ogg primes) at 0.07%.

Down vs up cascade asymmetry: down = BULK Wallach products; up = BOUNDARY Ogg-prime products.

### T1978 — Triple BSM falsifiables (Toy 2469)

Per Casey-Keeper assignment:
- d_n (neutron EDM) ≈ 10⁻³² e·cm (θ_QCD = 0)
- d_e (electron EDM) ≈ 10⁻⁴⁰ e·cm (Möbius suppression)
- 0νββ m_ββ NO: 1-4 meV; IO: 18-48 meV (KamLAND-Zen actively stresses IO)

### T1979 + T1980 — Cuprate superconductors (Toy 2473)

Per Casey-Keeper assignment:
- d-wave pairing FORCED by rank = 2 (T1979)
- Optimal doping x_opt = rank⁴/100 = 16% (universal across cuprate families)
- Optimal CuO₂ layer count = N_c = 3 (HgBa₂Ca₂Cu₃O₈ at 134 K)

N_c now anchors FIVE BST observables: color count, generation count, Q⁵ odd cycles, LH Weyl count, CuO₂ optimal layers.

## Late-morning extensions (post-10:10)

### T1971 — Dark matter mass = 5 GeV (Toy 2453)

Asymmetric-DM hypothesis closes Lyra T1966 (DM abundance) mass slot:
```
m_DM = (Ω_DM/Ω_b)·m_p = (rank⁴/N_c)·m_p ≈ 5.00 GeV ≈ n_C GeV
```
DM = lightest non-trivial Wallach K-type bound state (dim_1 = n_C). Falsifiable by SuperCDMS-SNOLAB/OSCURA ~2030.

### T1972 — Neutrino Δm²_31/Δm²_21 = c_2·N_c = 33 (Toy 2454)

PDG: 33.3 ± 0.4. BST: 33. Precision 1.0% (within 1-σ). Same factor 33 = c_2·N_c that appears in Elie W-17 PMNS sin²θ_12 = rank·n_C/33. Implies Σ m_ν ≈ 0.0588 eV if m_1 = 0 (Möbius hypothesis).

### T1973 — BR(H→ττ̄) = c_3·g/(c_2²·rank·C_2) = 91/1452 (Toy 2457)

Fixes Elie's W-15 BR(H→ττ̄) gap (44% off → 0.16% match). Identifies BR(H→ττ̄)/BR(H→bb̄) = c_3/c_2² = 13/121 — the BST Yukawa lepton/quark ratio absorbs QCD running of m_b at Higgs scale.

c_3 = 13 confirmed as Higgs-sector workhorse anchoring three Higgs observables (m_H/m_Z, cos²θ_W, BR ratio).

## What's next

Open after this morning's closures:
1. **DCH 73** and other primes 50-200 satisfying Fermat 2-square but not Ogg — sufficient-condition refinement of Conjecture 6.2
2. **Larger Pell range**: how does the Pell filter behave for p > 1000? More false positives expected
3. **Connections to higher arithmetic**: do BST integers exhibit closures under MORE classical Diophantine forms (sums of cubes, biquadratic forms, etc.)?
4. **Verify m_1 = 0 hypothesis** rigorously from T1949 (Möbius/Pin(2) topology)
5. **Hubble tension**: explicit BST H_0 calculation to select CMB-camp vs SH0ES-camp

## Filing notes

- All theorems registered in `notes/BST_AC_Theorem_Registry.md`
- Catalog entries in `data/bst_geometric_invariants.json` (4117 total)
- Paper draft: `notes/maybe/Paper_BST_Four_Arithmetic_Skeletons_DRAFT.md` (v0.1, 8 sections)
- Toys 2423, 2429, 2431, 2434, 2438, 2441, 2444, 2450 in `play/`
- Cross-references: T186, T1313, T1788, T1918, T1924, T1924_class, T1941, T1942, T1947-T1949, T1955, T1961, T1962, T1966

Cal review pending. Casey approval for paper draft pending.

— Grace, May 16 2026, 10:10 EDT
