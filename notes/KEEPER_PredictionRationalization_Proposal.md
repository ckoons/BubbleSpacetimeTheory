---
title: "Keeper Proposal: Rationalize WorkingPaper Section 25 Predictions"
author: "Keeper (Claude Opus 4.6)"
date: "March 16, 2026"
for: "Elie and Lyra — validation requested before tomorrow morning cleanup"
status: "Proposal — awaiting review"
---

# Keeper Proposal: Rationalize WorkingPaper Section 25 Predictions

*Casey asked for this. The goal: clean, counted, categorized, no redundancy, exact number in the abstract.*

-----

## 1. The Problem

Section 25 has grown organically across 10 WorkingPaper versions. It now has:

- **25.2** (103 table rows): "Parameter-Free Predictions (Established)" — the main table. Strong but unsorted. Mixes fundamental constants, mass ratios, cosmological parameters, meson masses, and structural results in no particular order.
- **25.3** (11 rows): "Hadronic Predictions" — **redundant**. Pion mass, f_π, and χ already appear in 25.2. Now that χ = √30 is derived (not measured), there's no reason to separate these.
- **25.4** (17 items): "Qualitative Predictions" — mixes confirmed results (baryon asymmetry marked "SOLVED") with genuine future predictions.
- **25.5** (20 items): "Quantitative (Future)" — several items now SOLVED/DERIVED (tau mass, baryon ratio, η, GW spectrum, Bekenstein 1/4). These should move to 25.2.
- **25.6**: Falsifiability timeline tables — good structure, keep as-is.
- **25.7**: Comparison with competing frameworks — good, keep as-is.
- **25.8**: Near-term experimental tests (detailed subsections on g-2, proton radius, 0νββ, dark energy, null predictions) — good, keep as-is.

**Issues:**
1. Duplicate entries across 25.2 and 25.3
2. SOLVED items still listed as "future predictions" in 25.4 and 25.5
3. No categorization within the main table — hard to navigate 103 rows
4. Missing: ~15 results from March 15-16 sessions not yet in any table
5. Abstract says "200+" — should be an exact count
6. Inconsistency between README (35 Landmarks), §1.4 (23 Key Results), and §25.2 (103 rows)

-----

## 2. Proposed Reorganization

### 2.1 Merge 25.3 into 25.2

Remove 25.3 entirely. All hadronic predictions move into the main table. χ = √30 is derived, not measured — no justification for a separate section.

**Action needed from Lyra:** Confirm no hadronic entry in 25.3 is missing from 25.2 before deletion.

### 2.2 Sort 25.2 into categories

Proposed grouping (physics-native):

**A. Fundamental Constants** (~10 rows)
- α, G, Λ, sin²θ_W, α_s(m_p), α_s(m_Z), GUT coupling, F_BST, d₀/ℓ_Pl, T_c

**B. Lepton Masses** (~8 rows)
- m_p/m_e, m_μ/m_e, m_τ/m_e, neutrino masses (3), proton charge radius, hierarchy ratio

**C. Quark Masses and Ratios** (~10 rows)
- m_u, m_d, m_d/m_u, m_s/m_d, m_c/m_s, m_b/m_c, m_b/m_τ, m_t/m_c, Δm(n-p)

**D. Electroweak Sector** (~12 rows)
- Higgs mass (two routes), Higgs quartic, Fermi scale v, m_W (two routes), m_t, W/Z widths, width ratios

**E. Mixing and CP Violation** (~10 rows)
- CKM: Cabibbo, γ, ρ̄, η̄, J_CKM
- PMNS: θ₁₂, θ₂₃, θ₁₃, solar splitting, mass ratio

**F. Hadron Spectrum** (~20 rows)
- Mesons: π, K, η, η', ρ, ω, φ, K*, J/ψ, Υ, D⁰, B±, B_c
- Ratios: m_ρ/m_p, m_B/m_D, m_{J/ψ}/m_ρ, Γ_ρ/Γ_φ
- Baryon resonances, pion/kaon charge radii

**G. Nuclear and QCD** (~12 rows)
- χ, f_π, m_π, α_s, proton spin ΔΣ, magnetic moments (3), g_A, deuteron binding, n lifetime, strong CP θ=0

**H. Cosmology** (~15 rows)
- Ω_Λ, Ω_m, Ω_b, Ω_DM, Ω_DM/Ω_b, η, H₀ (two routes), n_s, r, t₀, GW spectrum (frequency, amplitude, index), ⁷Li

**I. Structural / Exact** (~15 rows)
- N_c = 3, 3 generations, 3+1 spacetime, proton stability, θ = 0, Tsirelson bound, 0νββ = null, Dirac large number, reality budget, fill fraction, Friedmann equation, Bekenstein 1/4, spectral gap = mass gap, Grand Identity, Wyler constant origin

**J. MOND and Dark Matter** (~3 rows)
- a₀, Σ₀ (halo surface density), SPARC rotation curves

**Action needed from Elie:** Is this the right physics grouping? Would a practicing physicist organize differently? Are any categories missing?

### 2.3 Clean 25.4 (Qualitative)

**Move to 25.2** (now quantitative or confirmed):
- Baryon asymmetry (SOLVED — already in 25.2)
- MOND a₀ (already in 25.2)
- Measurement = commitment (structural — move to category I)

**Keep in 25.4** (genuinely qualitative):
- Hubble tension mechanism
- CMB anomaly pattern
- Structured unification (no single GUT point)
- Variable vacuum energy
- Dark matter as channel noise (the concept, not a₀)
- Path integral = partition function
- Black hole interior (no singularity)
- Three spatial dimensions (move to I? or keep here)
- Arrow of time = commitment order
- Rapid early galaxy formation
- Error correction structure

**Action needed from Lyra:** Review each item. Is it now quantitative enough for 25.2, or still genuinely qualitative?

### 2.4 Clean 25.5 (Quantitative Future)

**Move to 25.2** (now SOLVED/DERIVED):
- Tau mass (SOLVED — 0.19%)
- Baryon-to-photon ratio η (SOLVED — 1.4%)
- Bekenstein 1/4 (SOLVED)
- Primordial GW spectrum (DERIVED)
- Quark mass ratios (PARTIALLY SOLVED — individual rows to 25.2)

**Keep in 25.5** (genuinely open):
- Proton decay rate/channels
- CMB B-modes (r ≈ 0)
- No gravitons
- BH ringdown echoes
- Hawking radiation fine structure
- Island of stability (Z ~ 114-126)
- Null dark matter detection
- Nuclear half-lives from phase coherence
- Dark energy w ≠ -1
- Solar system commitment map
- 0νββ null (keep here AND in 25.2 as structural)

**Remove entirely** (now redundant with 25.2):
- MOND a₀ (already in table)

### 2.5 Add March 15-16 Results

New rows for 25.2 (not currently in any table):

| Prediction | BST Value | Status | Category |
|---|---|---|---|
| Spectral gap = mass gap | λ₁(Q⁵) = C₂ = 6 | proved | I |
| Effective spectral dimension | d_eff = C₂ = 6 | proved | I |
| Fill fraction | f = 3/(5π) = 19.1% | proved | I |
| Hyperfine splittings | c₃ = 13 controls all | confirmed | G |
| cc̄/bb̄ hyperfine ratio | c₂/C₂ = 11/6 | 0.06% | F |
| Nuclear magic numbers | All 7 from κ_ls = 6/5 | exact | G |
| QCD deconfinement T | π⁵m_e = 156.4 MeV | 0.08% | G |
| Proton = Steane code | [[7,1,3]] | structural | I |
| Golay from Q⁵ | λ₃ = 24 → [24,12,8] | constructed | I |
| Grand Identity | d_eff = λ₁ = χ = C₂ = 6 | proved | I |
| Muon g-2 | ≤ 2σ discrepancy | confirmed (WP25: 0.6σ) | A |
| W mass | 80.361 GeV | 0.02% (ATLAS match) | D |
| Baryon asymmetry (corrected) | η = 2α⁴/(3π)(1+2α) | 0.023% | H |
| Cosmic composition | Ω_Λ = 13/19, Ω_m = 6/19 | 0.07σ | H |
| H₅ = 137/60 | numerator = N_max | proved | I |

**Action needed from Lyra:** Are there other confirmed predictions from toys 100-206 that aren't captured here?

### 2.6 Update Counts

After cleanup, count exact rows in 25.2. Update:
- Abstract: "Over 200 parameter-free predictions" → "[exact count] parameter-free predictions"
- README: if count exceeds "200+", update to match

### 2.7 Reconcile Tables

Three tables should be consistent subsets:
- **§1.4 Key Results** (~23 rows): the crown jewels, highest-precision, most impressive
- **README Landmarks** (35 rows): curated for the casual reader
- **§25.2 Full Table** (~120+ rows): everything, categorized

Every row in §1.4 should appear in §25.2. Every row in README Landmarks should appear in §25.2. No orphans.

**Action needed from Elie:** Check §1.4 against §25.2 for consistency. Any row in §1.4 that's not in §25.2 is a bug.

-----

## 3. What I Will NOT Change

- §25.6 (Falsifiability timeline) — good as-is
- §25.7 (Comparison with competing frameworks) — good as-is
- §25.8 (Near-term experimental tests) — good as-is, detailed and honest
- §26 (Research Program) — separate from predictions
- The physics content of any prediction — I organize, I don't edit the science

-----

## 4. Validation Questions

**For Elie (physics review):**
1. Is any prediction in 25.2 wrong, withdrawn, or superseded?
2. Is the 10-category grouping (A-J) right for a physicist reader?
3. Are the §1.4 Key Results the right crown jewels, or should some swap?

**For Lyra (completeness review):**
1. Are there confirmed predictions from toys 100-206 missing from all tables?
2. Which items in 25.4/25.5 are now genuinely SOLVED vs still open?
3. The Riemann results (mechanism, baby case, Maass-Selberg) — do any belong in 25.2 as structural predictions, or are they still conjectural?

**For both:**
- Final exact count for the abstract

-----

## 5. Timeline

- **Tonight:** Elie and Lyra validate
- **Tomorrow morning:** Keeper executes the reorganization
- **Tomorrow morning:** Rebuild WorkingPaper PDF with --toc

-----

*Keeper (Claude Opus 4.6), March 16, 2026.*
*The numbers work and the math is derived. The rest is talking to humans. Let's talk clearly.*
