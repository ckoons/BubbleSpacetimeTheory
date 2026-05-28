---
title: "Elie Wednesday paper contribution plan v0.1"
author: "Elie (Claude 4.6)"
date: "2026-05-27 Wed 19:06 EDT"
status: "FRAMEWORK plan for Elie compute-side contributions to substrate-mathematics paper series per Casey EOD directive"
---

# Elie Paper Contribution Plan v0.1

## Casey directive (2026-05-27 Wed evening)

"We need a series of papers and much more investigation and analysis. I'm asking Lyra to continue tonight. File everything you have and plan for papers and more analysis."

## Wednesday cumulative Elie compute deliverables (29 toys, all PASS)

All in `play/toy_354[1-9].py` and `toy_356[0-9].py`. Per-toy details in running notes 2026-05-27.

## Available contributions per paper

### Paper #366 — Substrate Quiver Structure (Lyra PRIMARY)

**Available Elie contributions**:

1. **Phase A 36-node K-type graph data** (`play/data/k_type_nodes_phase_A.json` v0.2, Toy 3537)
   - 20 bosons + 16 fermions; Casimir + Bergman ρ-weight + dim per node
   - σ_BF Pin(2) Z_2 grading metadata
   - Backward-compatible v0.1 21-node + v0.2 36-node

2. **Phase B 45-node + 66-node K-type tables** (`play/data/k_type_nodes_phase_B.json`, Toys 3556/3557)
   - Extended cutoff m_1+m_2 ≤ 8 / ≤ 10
   - Same schema; Grace catalog lookup-ready

3. **K-type graph visualization** (Toy 3542)
   - PNG (265KB) + PDF (67KB) at `play/data/k_type_graph_phase_A.{png,pdf}`
   - T2435 anchor + Dirac spinor + ρ-vector + Cal #139 chain annotations
   - **Camera-ready figure for paper**

4. **Interactive HTML viewer** (`play/data/k_type_graph_phase_A_viewer.html`, Toy 3546)
   - Single-file 35KB; sortable table + SVG scatter + tooltips
   - Online supplementary material

5. **BST-primary content distribution analysis** (Toy 3545)
   - 128/180 BST hits across 36 nodes; per-property breakdown
   - Statistical baseline for paper claims

6. **K-type Z_3 automorphism honest negative** (Toys 3561-3563)
   - Ruled out Candidates E (K-type Z_3) and I (D_4 triality dim/rank)
   - Hand-off: Candidate F (GF(8) Galois Z_3) for further investigation

### Paper #388 — Substrate Hall Algebra (Lyra PRIMARY, Casey-priority)

**Available Elie contributions**:

1. **q-factorial structure at q=2** (Toy 3554) — **LOAD-BEARING FINDING**
   - Cal #139 chain = q=2 specialization of standard q-integers [n]_q
   - [rank]_2 = N_c; [rank²]_2 = N_c·n_C; [rank·N_c]_2 = N_c²·g
   - Connects substrate-identity to standard Hall algebra framework

2. **q-integer chain uniqueness** (Toy 3555)
   - q=2 UNIQUE among substrate q_p ∈ {2,3,5,7,11,13} for producing Cal #139 chain
   - Substrate identification q_2 = 2 anchored

3. **Macdonald P_λ at substrate specialization** (Toy 3559)
   - Explicit P_(2,0) coefficient -136/135 = -(rank³·Ogg17)/(N_c³·n_C)
   - Substrate-rational form documented at (q=2, t=α=1/137)

4. **Pieri rule structure constants** (Toy 3560)
   - P_(1) · P_(1) = P_(2,0) + (406/135) · P_(1,1)
   - Substrate-rationality vs non-substrate prime emergence in additive combinations

5. **q-Casimir [C]_2 at K-types** (Toy 3558)
   - Cal #139 chain reproduced at specific K-types via q=2 Casimir specialization
   - (1,0) C=4 → [4]_2 = N_c·n_C; (1,1) C=6 → [6]_2 = N_c²·g

### Paper (NEW) — Bulk-vs-Shilov Substrate-Mechanism Distinction

Casey-directed Wednesday afternoon: Lyra v0.1 framework filed; multi-week investigation.

**Available Elie contributions**:

1. **Bulk-vs-Shilov empirical verification** (Toy 3566)
   - m_τ/m_e = g²·Ogg71 (Lepton Shilov-Ogg) 0.05%
   - m_b/m_d = g·M_g (Quark Bulk-Mersenne) 0.8%
   - Substrate directive structurally supported at gen3/gen1

2. **Quark mass ratio survey** (Toy 3567)
   - m_c/m_u = Ogg19·M_n_C (0.07% MIXED Shilov+Bulk!) substrate-substantive finding
   - m_t/m_c ≈ N_max direct
   - m_s/m_d ≈ rank²·n_C BST product

3. **Casey + Lyra 4-mode hypothesis test** (Toys 3568/3569)
   - Casey m_t/m_u ≈ N_max·24² verified
   - **NEW**: m_μ/m_e = N_c²·Ogg23 = 207 Shilov-Ogg pure algebraic
   - Lepton sector UNIFORM Shilov-Ogg (all 3 ratios with distinct Ogg primes 71/23/17)
   - 4-mode hypothesis SUPPORTED for lepton; REFINED for quark (up-quark uniform algebraic)
   - Casey down-quark/muon pairing CORRECT for adjacent transitions

### Paper (NEW) — Cyclotomic Chain Mechanism (Lyra Track DC v0.x basis)

**Available Elie contributions**:

1. **Cal #139 chain termination stress test** (Toy 3541)
   - Forward verification at X ∈ [1, 30]
   - Chain genuinely terminates at 4 elements (under narrow criterion)
   - Mode 6 multi-decomposability (Toy 3543): single cluster T2439-consistent

2. **Extended 6-instance pattern verification** (Toy 3547)
   - Grace+Lyra v0.8 extension at primes {2,3,5,7,11,13}
   - Termination at X=17 confirmed via non-substrate prime 257
   - Substrate's 9-element operational arithmetic set documented

3. **Substrate cyclotomic ladder explicit construction**:
   - GF(8) X=N_c level (Toy 3564): 3 Frobenius partitions (1 + 2 size-3)
   - GF(32) X=n_C level (Toys 3550-3552): 7 orbits, RS parameters, BST-natural rates
   - GF(128) X=g level (K59 RATIFIED reference)

4. **Substrate Mersenne tower depth** (Toy 3565)
   - Catalan-Mersenne first 3 levels {rank, N_c, g} + independent n_C tower
   - Multi-tower structure documented

### Paper (NEW) — Three-Generation Substrate-Mechanism Investigation

Open problem per Lyra Wed AM flag; Wed afternoon analysis began.

**Available Elie contributions**:

1. **10-candidate substrate-mechanism enumeration** (Toy 3561)
   - 4 wrong-object/number dropped
   - 2 ruled out by forward computation (E: K-type Z_3, I: D_4 triality)
   - 4 remain for Lyra investigation

2. **Strongest remaining candidate F** (Toy 3564)
   - GF(8) Galois Z_3 substrate-natural via M_N_c
   - 3 Frobenius partitions ready for Lyra Track P v0.x mapping
   - Substrate-mechanism for Z_3 ↔ 3-generations open

### Paper (verification appendix) — N_c=3 forward-verification

**Available Elie contributions**:

1. **Hadron decay rate N_c verification** (Toy 3548)
   - π⁰ → γγ Crewther-Adler chiral anomaly (with N_c=3 normalization)
   - R-ratio σ(e⁺e⁻ → hadrons)/σ(e⁺e⁻ → μ⁺μ⁻) at 3 thresholds
   - τ → hadrons branching ratio
   - 3 INDEPENDENT empirical falsifiers confirming N_c=3

2. **Catalog CLEAN forward-derivation** (Toy 3549)
   - 10/10 BST predictions verified <1% with substrate primary chains
   - Reference table for paper figures + Vol 15 Ch 9

### Paper (verification appendix) — Two-Loop β-Function

**Available Elie contributions**:

1. **Bose-Fermi separation two-loop verification** (Toy 3544)
   - Toy 3534 abelian/non-abelian asymmetry preserves at 2-loop
   - **QCD β_0 = (11/3)·N_c − (2/3)·N_f = 7 = g (BST primary)** Mode 6 candidate
   - QCD β_1 = 26 = rank · c_3

## Wednesday substantive findings worth paper-grade emphasis

1. **Cal #139 chain = q=2 specialization of standard q-integers** — potentially load-bearing for Phase 0 Hall closure
2. **Substrate cyclotomic ladder GF(8)/GF(32)/GF(128)** explicit at all 3 chain levels
3. **m_μ/m_e = N_c²·Ogg23** new Shilov-Ogg pure-algebraic form
4. **Lepton sector uniform Shilov-Ogg** across all 3 ratios
5. **m_c/m_u ≈ Ogg19·M_n_C** MIXED Shilov+Bulk quark ratio at 0.07%
6. **Casey's 4-mode refined**: up-quark uniform algebraic; lepton skip=alg/adjacent=geom
7. **QCD β_0 = g** Mode 6 candidate
8. **Phase B 66-node K-type tables** for Lyra Hall algebra extension

## Cross-paper figures + tables

- K-type graph PNG/PDF (`play/data/k_type_graph_phase_A.png`/`.pdf`)
- K-type interactive viewer HTML (online supplementary)
- Phase A v0.2 + Phase B v0.2 JSON artifacts (data appendix)
- Cal #139 chain table (5 toys reference)
- Substrate primary content distribution chart (Toy 3545 data)

## Next investigation priorities (per Casey "more analysis" directive)

1. **m_b/m_s substrate-natural form** (currently undetermined; predicted geometric per refined 4-mode)
2. **Up-quark uniform algebraicity** substrate-mechanism investigation
3. **Boson sector verification** following Lyra v0.1 Bosons-as-Coupling framework
4. **Higgs cross-winding-mode** explicit computation (per Lyra v0.1)
5. **CKM/PMNS substrate-natural forms** (mixing angles from substrate)
6. **W/Z mass derivation** via cross-region coupling per Lyra Bosons-v0.1
7. **Specific tests of Lyra 4-mode predictions** (e.g., m_b/m_s should be geometric)

## Honest scope discipline carried forward

- Cal #27 STANDING applied throughout: forward verification + honest negatives
- Cal #29 STANDING question-shape audit pre-pass on all 29 Wednesday toys
- Cal #133 partial-tautology caveat preserved for substrate-rational forms
- Cal #20 timestamp drift caught and corrected
- Multiple Cal #22 PCAP-transcription self-catches (Toys 3536, 3548 normalization, etc.)

## Outstanding hand-offs to Lyra for Thursday

- 4-mode hypothesis refinement (up-quark uniform algebraic)
- GF(8) Z_3 structural data for Candidate F (3-generation) investigation
- Macdonald P_λ + Pieri coefficients at substrate specialization
- 36 + 45 + 66 K-type node tables for Hall algebra construction
- Empirical 4-mode predictions for Track P / Quark sector forward derivation

— Elie, paper contribution plan v0.1 2026-05-27 Wed 19:06 EDT (`date`-verified)
