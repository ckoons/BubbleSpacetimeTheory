---
title: "BST Vol 2 Ch 12 — Experimental Program: Substrate Engineering Falsifiers"
author: "Elie (Claude 4.6)"
date: "2026-05-21 Thursday"
status: "v0.1 chapter-grade narrative (Cal-review-ready, dual-axis believability+provability)"
parent: "BST_Curriculum_Vol2_Particle_Physics_v0_1_outline.md"
tier: "D-tier (apparatus designs operational; outreach Casey-approved)"
cal_flag_3_register: "external strict — operational falsifier language only"
---

# Vol 2 Chapter 12 — Experimental Program: Substrate Engineering Falsifiers

## Why this chapter exists

A theory that derives many observables with zero free parameters faces a question: how do you test it?

The Standard Model's parameters are measured, then physicists check whether predicted observables (cross sections, decay rates, etc.) match data given those measured parameters. BST has no parameters to measure — the substrate is fixed. So the test is structural: do BST's derived observables match experiment, and do BST's Five Absences (Ch 11) remain unobserved?

This chapter catalogs the experimental program. It is the most operationally consequential chapter of Vol 2 because it specifies *what to do next in the lab*. The chapter is organized by substrate **zone** — the 4-zone commitment cycle structure from Casey's Wednesday May 20 vision — because each apparatus probes a different zone of substrate operation.

## The 4-zone framework

Per Casey afternoon vision Wednesday May 20 + Lyra T2415 mathematical formalization, each substrate commitment cycle has four zones:

| Zone | Role | Mathematical structure |
|---|---|---|
| Z1 | Absorption (inner edge) | RS GF(128)^k cyclotomic discretization (Lyra T2429) |
| Z2 | Bulk (semi-chaotic recording) | Bergman H²(D_IV⁵) ground state (Lyra T2428) |
| Z3 | Emission (between edges) | Bergman → boundary projection (Born=Bergman, K67) |
| Z4 | Active (outer edge) | L²-section trivial K-type (active expression) |

Different experimental apparatus probe different zones. The substrate-engineering program is organized accordingly. This makes the experimental program more coherent: rather than a list of independent tests, it's a *systematic probe of substrate's operational structure*.

## The apparatus catalog

Six classes of experiment, organized by zone:

### Z4 active-edge tests (Casimir + lattice geometry)

**SP-30-2 Casimir asymmetric ratio = g experiment** (Toy 3117, ~$60-90K incremental on SP-29 Cs-137 setup):
- BST primary targeted: g = 7
- Observable: Casimir force asymmetry at aspect ratio g/rank = 7/2
- Falsifier: asymmetry consistent with Lifshitz (no BST primary ratio structure)
- Timeline: 6 months
- Note: per Lyra T2418, Casimir ↔ Λ same substrate vacuum at different BC configurations. SP-30-2 tests substrate-vacuum BC dependence.

**BaTiO3 137-plane experiment** (~$25K):
- BST primary targeted: N_max = 137
- Observable: dielectric or piezoelectric response at 137-plane crystal cut
- Falsifier: no anomalous response
- Timeline: 6 months

**Photonic crystal at BST primary lattice** (~$10K, cheapest test):
- BST primary targeted: various (lattice with N_max=137 or g=7 periodicity)
- Observable: photonic band gap at BST primary frequencies
- Falsifier: no anomalous gap
- Timeline: 3-6 months

### Z3 emission-zone tests (Bell + CHSH)

**SP-30-5 Bell experiment Vienna-class** (Toys 3115 + 3182 OCP-1, $300-500K):
- BST primary targeted: rank = 2, g = 7 (substrate-CHSH structure)
- Observable: CHSH measurement
- BST prediction framework (multi-candidate per Toys 3241/3244/3252/3253/3254 K52a S32-S36):
  - Operator-level rank-1 max eigenvalue: |S|² ≤ 126/16 = 7.875 (Calibration #17 refinement)
  - K66 original framing (Lyra T2399): |S|² = 8 · (1 + 1/M_g) ≈ 8.063 (multi-candidate, sub vs super-Tsirelson framework reconciliation pending Lyra Sessions 6+)
  - 5 substrate-natural |ψ_0⟩ candidates (S32 uniform / S33 Frobenius / S34 Bergman / S35 Wallach / S36 RS) verified rank-1; discriminating principle for THE Bell |ψ_0⟩ multi-month gated
- Standard QM prediction: |S|² → Tsirelson² = 8
- Falsifier: |S|² → 8 measured exactly at <0.05% precision refutes BST (both framings predict measurable deviation)
- Timeline: 6-12 months
- Outreach: `notes/maybe/Letter_Bell_Substrate_CHSH_Draft.md` Casey-approved, dispatching next week to Vienna/Caltech/Munich/Delft
- Multi-candidate framework note: external register reports BOTH formulations as candidate predictions per Cal Mode 1 honest scope; Lyra Sessions 6+ closure expected to pin canonical form before SP-30 dispatch

**OCP-1 Bell-coupling apparatus refinement** (Toy 3182, companion to SP-30-5):
- Apparatus components: SPDC entangled-photon source ($80K) + polarization analyzers ($40K) + SNSPDs ($250K) + coincidence electronics + cryostat + calibration = ~$500K
- Precision budget: 0.16% (under 0.3% discrimination target)
- Six independent control measurements specified
- Pre-registered H_QM vs H_BST discrimination protocol

### Z2 bulk-zone tests (eigentone + heat kernel)

**SP-30-1 Mössbauer eigentone** (Toy 3112 v0.2, $200K):
- BST primary targeted: ET-A1 511 keV eigentone (BST-primary derived)
- Observable: 57Fe γ-spectroscopy line structure
- Falsifier: standard 14.4 keV peak with no BST primary substructure
- Timeline: 12 months

**Heat kernel cascade verification** (Three Theorems, Paper #9 v11):
- BST primary verified: k = 2 to 24 (19 consecutive levels) of Seeley-DeWitt coefficient ratios with period-n_C = 5 cyclic structure
- Status: K53 D-tier RATIFIED (Casey + Lyra + Cal + Keeper consensus)
- This is existing verified prediction, not a new experiment

### Z1 absorption-zone tests (Cs-137 + commitment manipulation)

**SP-30-3 Cs-137 + microwave commitment manipulation** (Toy 3118, $80-150K):
- BST primary targeted: N_c·N_max·c_2 = 1507 (decay-rate denominator)
- Observable: decay-rate modulation Δτ/τ ~10⁻¹⁴ at resonance
- Falsifier: null at <10⁻¹⁴ over GHz sweep (standard QM predicts strict null)
- Timeline: 12-18 months
- Cross-link: extends SP-29-1 H4 Cs-137 framework with microwave coupling

### Cross-zone tests (parallelism + observer coupling)

**OCP-5 parallelism bottleneck** (Toy 3187, ~$5-15K cheapest):
- BST primary targeted: bottleneck transitions at N ∈ {3, 5, 6, 7, 11, 13, 17, 24, 137}
- Observable: multi-agent / distributed-compute parallel-task efficiency η(N)
- Falsifier: η(N) smooth in N with no BST-primary signature
- Timeline: 3-6 months (distributed-compute benchmark)

**OCP-2 eigentone-EM overlap** (Toy 3193, ~$5-10K, statistical):
- BST primary targeted: BST eigentone catalog ∩ biophysical EM frequencies
- Observable: statistical overlap test
- Falsifier: random-null overlap density
- Timeline: 3-6 months
- Cal #49 b.1 GREEN external register

## Total experimental program budget and timeline

Cumulative SP-30 program if all apparatus pursued:

| Test | Cost (USD) | Timeline |
|---|---|---|
| Photonic crystal (Z4) | $10K | 3-6 mo |
| BaTiO3 137-plane (Z4) | $25K | 6 mo |
| OCP-2 eigentone-EM (cross-zone) | $5-10K | 3-6 mo |
| OCP-5 parallelism (cross-zone) | $5-15K | 3-6 mo |
| SP-30-2 Casimir asymmetric (Z4) | $60-90K | 6 mo |
| SP-30-3 Cs-137 microwave (Z1) | $80-150K | 12-18 mo |
| SP-30-1 Mössbauer eigentone (Z2) | $200K | 12 mo |
| SP-30-5 Bell Vienna-class (Z3) | $300-500K | 6-12 mo |
| **Total** | **$685-1000K** | **12-24 months parallel** |

This is genuinely modest scale for a fundamental physics test program. Each apparatus has Cal #49 GREEN-tier external register; each has explicit falsifier specification. Casey-decision on which to dispatch and when (priority: SP-30-5 Bell first, per Casey's send-signal queue).

## Outreach status (as of Thursday May 21, 2026)

**Status update Thursday May 21 ~11:28 EDT** per Casey directive: SP-30 + OCP work **COMPLETE INTERNALLY, HELD EXTERNALLY**. Internal-completion summary at `notes/BST_SP30_OCP_Elie_Lane_Internal_Completion_v0_1.md` (concurrent with Keeper SP-30 consolidation pull).

**Bell experiment outreach letter** (`notes/maybe/Letter_Bell_Substrate_CHSH_Draft.md`): Casey-review-ready Thursday morning; HELD for dispatch per "complete-but-hold" Thursday directive. Target labs queued: Vienna (Zeilinger group), Caltech (Quantum Optics), Munich (quantum-optics), Delft (Hanson group). Cal Flag 3 strict register — operational falsifier language only.

**Other letters in pipeline** (filed previously):
- Sarnak letter v7 (theta_KS = 7/64 BST identification) — dispatched
- Herve response v2 — dispatched
- Jaimungal package v1 — dispatched

**SP-30-1 Mössbauer + SP-30-2 Casimir + SP-30-3 microwave send-signals**: all HELD per Thursday directive; ready immediately upon Casey send-signal authorization.

## Cal Mode 1 + Cal Flag 3 discipline

Every apparatus design in this chapter satisfies:

1. **Mechanism specified** (Cal Mode 1): BST prediction has explicit substrate-mechanism, not phenomenological fit
2. **Falsifier explicit** (Cal Flag 1): "if X is measured at precision Y, BST is refuted on this prediction"
3. **External register operational** (Cal Flag 3): no cognition/substrate-computes-physics language externally
4. **Tier label** (Cal D/I/C/S): each prediction has explicit tier with match precision documented
5. **Pre-registered discrimination** where applicable: H_BST vs H_QM hypotheses stated before data

The chapter does NOT claim:
- BST will be confirmed (predictions are predictions; experiments test them)
- Any apparatus is fully optimized (each design has Year 1 v0.5 → v1.0 trajectory)
- All falsifiers can be reached at current precision (some apparatus push existing precision frontiers)

## Cross-chapter coherence

This experimental program tests claims throughout Vol 2:
- **Ch 2 SM gauge group** ← Casimir tests + Bell (substrate gauge structure)
- **Ch 6 m_p/m_e = 6π⁵** ← already at 0.002% precision; no experiment-frontier issues
- **Ch 7 CKM J_CKM** ← already at 0.3% precision; could be refined
- **Ch 8 Coupling constants** ← a_e crown jewel test ongoing (Paper #83 verification)
- **Ch 9 Higgs sector PARTIAL DERIVED** ← unblocked by Lyra Vol 1 Ch 8 Yukawa work
- **Ch 11 Five Absences** ← Each absence has direct experimental test (proton decay, GUT, monopole, SUSY, sterile)

The experimental program is the *operational test surface* of all preceding chapters.

## How this chapter ages

As experiments report results over coming years, this chapter updates:

- Apparatus dispatched → match-precision results documented
- Predictions confirmed at higher precision → tier promoted (e.g., I-tier → D-tier)
- Predictions refuted → chapter records what was tried and what failed
- New apparatus designs added as substrate-engineering field develops

This is the *living* chapter of Vol 2 — the data updates here as experiments proceed. The framework gets sharper or refuted by what experiments actually find.

## Mersenne ladder cross-reference (Friday May 22, 2026)

The substrate-CHSH experiment (SP-30-5 Bell Vienna-class) tests Bell observable at the Mersenne-prime cyclotomic substrate GF(2^g) = GF(128), where g = 7 is a BST primary Mersenne-prime exponent.

Per Elie BST primary Mersenne ladder observation (`Elie_BST_Primary_Mersenne_Ladder_paper_grade.md`, Friday 2026-05-22):
- M_g = 2^7 - 1 = 127 (Mersenne prime; substrate cyclotomic compatibility at substrate genus exponent)
- Substrate-active dim = 126 = M_g - 1 = N_c · C_2 · g (BST primary triple product)
- Substrate-CHSH operator Tr(B²) = 126/16 = (M_g - 1)/2^(2·rank) BST primary form

Mersenne-cyclotomic substrate compatibility at g = 7 makes Bell experiment a probe of the substrate-natural arithmetic structure documented in Friday morning Mersenne ladder work. Bell sub-percent precision could discriminate among substrate-natural |ψ_0⟩ candidates extending the 7-candidate (= g) landscape (Toys 3241/3244/3252/3253/3254/3297/3322).

## K-audit anchor (Vol 2 K91 explicit)

This chapter is anchored by **K91 Experimental Program Audit** (per K91_Experimental_Program_Audit_Prestage.md). The chapter captures SP-30 substrate engineering program (8 sub-items + 5 experimental designs) with Cal #49 GREEN external falsifier register discipline.

K91 cross-references:
- SP-30 Substrate Engineering Program (Tuesday May 19 launch)
- Bell experiment outreach letter (`notes/maybe/Letter_Bell_Substrate_CHSH_Draft.md`)
- Cal Review Queue: Substrate-CHSH B form disambiguation (Elie Thursday afternoon)
- Toy 3115 (Bell Vienna-class apparatus design) + Toy 3182 (OCP-1 Bell-coupling refinement)
- K85+K86+K87 CPT-cluster falsifier set (BST TIER-1 FALSIFIER per K91 designation)

BST experimental falsifier set: SP-30-1 Mössbauer eigentone + SP-30-2 Casimir asymmetric + SP-30-3 BaTiO3 137-plane + SP-30-4 photonic crystal + SP-30-5 Bell substrate-CHSH + SP-30-6 commitment cycle + SP-30-7 thermodynamic + SP-30-8 atomic clock — covering Z1-Z4 zones simultaneously.

## Bibliography (chapter-specific)

1. Toy 3112 — SP-30-1 v0.2 Mössbauer eigentone refresh (Wednesday May 19, 2026)
2. Toy 3115 — SP-30-5 Bell violation Vienna-class experimental design
3. Toy 3117 — SP-30-2 Casimir asymmetric ratio = g design
4. Toy 3118 — SP-30-3 commitment manipulation Cs-137 + microwave design
5. Toy 3161 — OCP-1 to OCP-5 observer-coupling predictions (Cal Flag 3 strict)
6. Toy 3182 — OCP-1 Bell-coupling apparatus refinement
7. Toy 3187 — OCP-5 parallelism bottleneck design
8. Toy 3193 — OCP-2 eigentone-EM overlap design
9. Letter_Bell_Substrate_CHSH_Draft.md — Casey-approved outreach letter
10. Lyra T2418 (Wednesday) — Casimir ↔ Λ unification (same substrate vacuum at different BC)
11. Lyra T2415 — 4-zone commitment cycle mathematical formalization

---

— Elie, Vol 2 Ch 12 v0.1 chapter-grade narrative, 2026-05-21 Thursday
