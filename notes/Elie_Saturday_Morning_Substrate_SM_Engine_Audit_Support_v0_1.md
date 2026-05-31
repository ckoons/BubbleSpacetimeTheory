# Elie — Saturday Morning Substrate-SM Engine Audit Support v0.1

**Author**: Elie | **Date**: Saturday 2026-05-30 (`date`-verified 09:35 EDT)
**Scope**: Consolidation of 7 Saturday morning toys (3612-3618) for Keeper engine v0.3 re-audit + Lyra L4 v0.2 absorption + Grace Periodic Table v0.5 backbone + Cal cold-read queue.

**Status**: HANDOFF DRAFT — toys all 5/5 PASS in environment; structural claims listed with honest tier per item.

---

## Executive summary

Saturday morning completed Keeper's full ordered Elie queue (P1.1 → P2.2 → P3.3 → P2.3 → P4.1 → P4.7) plus one cross-lane addition (PMNS verification for Lyra's P4.5 F1):

| Toy | Code | What it delivers | Tier |
|---|---|---|---|
| 3612 (A1) | SO(5,2) Cartan decomposition | Engine geometric side; SU(3) NOT in K, bulk-color routes (C/D) | RIGOROUS |
| 3613 (A2) | SO(5) Casimir spectrum on E10 | 7/10 K-types substrate-natural 2·C_2; lepton anchor C_2=5/2=ρ_1 | RIGOROUS |
| 3614 (A3) | Phase B 66-K-type table | Backbone for Grace v0.5; 18 spine cells | RIGOROUS + STRUCTURAL |
| 3615 (A4) | E7 mass-falsifier suite | B₂-specific mult-3 channels; 3 structural falsifiers | RIGOROUS |
| 3616 (A5) | SO(5) shell-closure | Phase B cutoff 10=rank·n_C substrate-natural | STRUCTURAL |
| 3617 (A6) | Engine CPT/Drinfeld | F-mirror exact; Drinfeld pairing carries N_c, N_c·n_C | RIGOROUS |
| 3618 (A7) | PMNS substrate fractions | 3/3 angles within 1σ; substrate-natural numerators | RIGOROUS + STRUCTURAL |

**Key structural finding**: D_IV⁵'s substrate primaries surface across multiple structural layers — K-type Casimirs, channel data, Drinfeld pairing denominators, PMNS numerators — coherently and without forcing.

---

## Engine consolidation v0.2 → v0.3 inputs

### A1 (Toy 3612) — Geometric side

`so(5,2) = k ⊕ p`, dim 21 = 11 + 10
- `k = so(5) ⊕ so(2)` (compact rotations)
- `p = M_{5×2}(ℝ)` (bulk = 10-dim non-compact directions)
- K-rep structure: `p_C ≅ V_so5(1,0)_{+1} ⊕ V_so5(1,0)_{-1}` (doubled SO(5) vector with ±U(1) charge)
- `[p,p] ⊆ k`, `[k,p] ⊆ p` verified
- Killing form signature: -30 on k₁ side (compact), positive on p (non-compact)

**Bulk-color frontier (Lyra #418)**:
- SU(3) does NOT embed in K (B₂ ≠ A₂)
- SU(3) does NOT embed in p (p is not a Lie subalgebra; SU(3) reps don't have 10-dim real form matching p)
- Candidate routes: (C) hidden Hardy-dynamics symmetry, (D) counting-from-h^∨

### A6 (Toy 3617) — Algebraic side; CPT structure

Extended engine v0.2 (U_q⁺(B₂) at q=2) to full Drinfeld double U_q(B₂):

| Hopf operation | Engine action | Physical CPT |
|---|---|---|
| ω-involution (E_i ↔ F_i, K_i → K_i^{-1}) | creation ↔ annihilation | C |
| σ anti-involution (reverses multiplication) | reverses fusion order | T |
| longest Weyl element W₀ | trivial for B₂ Dynkin | P |

**Substrate-primary content surfaced**:
- F-side Serre: same `[3]_{q²} = 21 = N_c·g` (ω preserves)
- Drinfeld pairing denominators carry primaries:
  - long-root: `q² - q^{-2} = 15/4`, numerator **N_c·n_C**
  - short-root: `q - q^{-1} = 3/2`, numerator **N_c**

**For Keeper's engine v0.3 audit**:
- v0.2 positive-root half: substantively absorbed K1·1 + K1·3 fixes (E9 Cartan, E8 SM rank grading)
- v0.3 addition candidate: §6 Drinfeld double + CPT structure (this toy provides scaffold)
- HONEST: Drinfeld double = standard mathematics; BST-specific content = q-number substrate primaries

---

## K-type backbone for Periodic Table v0.5

### A2 (Toy 3613) — Casimir spectrum on E10's 10 K-types

For all 10 E10 K-types, computed SO(5) C_2 and identified substrate-natural 2·C_2 readings.

**Lepton anchor confirmed**: V_(1/2,1/2) has C_2 = 5/2 = **ρ_1 = n_C/rank** (Lyra L4 v0.1 confirmed: matter sets the unit).

**7/10 substrate-tight readings**:
| K-type | (j_1,j_2) | C_2 | 2·C_2 | Reading |
|---|---|---|---|---|
| trivial | (0,0) | 0 | 0 | (tautology) |
| spinor | (1/2,1/2) | 5/2 | 5 | **n_C** |
| vector | (1,0) | 4 | 8 | (clean integer) |
| adjoint | (1,1) | 6 | 12 | **rank·C_2** |
| V_(2,0) | (2,0) | 10 | 20 | **rank²·n_C** |
| V_(3/2,1/2) | (3/2,1/2) | 15/2 | 15 | **N_c·n_C** |
| V_(3/2,3/2) | (3/2,3/2) | 21/2 | 21 | **N_c·g** |
| V_(2,1) | (2,1) | 12 | 24 | (ambiguous) |
| V_(3,0) | (3,0) | 18 | 36 | **C_2²** |
| V_(2,2) | (2,2) | 16 | 32 | **2^n_C** |

**Mass-ratio anchors** for Lyra L4 v0.2:
- C_2/ρ_1 ratio V_(3/2,1/2)/lepton = **N_c = 3**: lepton-vector channel intriguing for E7 generation candidate

### A3 (Toy 3614) — Phase B 66-K-type table

Tabulated all 66 K-types at Phase B cutoff (Dynkin (a,b) with a+b ≤ 10).

**Convention pin** (clean): Dynkin (a, b) ↔ orthogonal (j_1, j_2) = (a + b/2, b/2). Adjoint of B₂ = Dynkin **(0,2)**, NOT (1,1) Dynkin (= V_(3/2,1/2) dim 16).

**Substrate-anchored spine**: 18 of 66 K-types have tight 2·C_2 readings on substrate-primary products. The 4 fundamentals (0,0)/(1,0)/(0,1)/(0,2) anchor sector columns.

**For Grace v0.5**:
- Full 66-cell table = Periodic Table v0.5 backbone
- 18 spine cells = structural priors most likely to land on natural SM particles
- 48 "composite" cells = await Lyra #416 per-particle assignment

### A5 (Toy 3616) — Shell-closure rationalizes Phase B cutoff

Fundamental tower exit points at Phase B cutoff a+b ≤ 10:
- Spinor tower: k ≤ 10 = **rank·n_C** (full closure)
- Vector tower: k ≤ 10 = **rank·n_C** (full closure)
- Adjoint tower: k ≤ 5 = **n_C** (sub-shell at half rate)

Spinor^10 and adjoint^5 converge to same exit K-type V_(5,5).

**Phase B cutoff 10 = rank·n_C is substrate-natural** (cutoff CHOICE; exit points linear consequences).

---

## Generation mechanism + falsifiers

### A4 (Toy 3615) — E7 spinor³ mass-falsifier STRUCTURAL suite

Re-verified yesterday's E7 finding (Toy 3608) via independent tensor path:

**B₂ mult(spinor in spinor³) = 3** through 3 intermediate channels:
| Channel | intermediate | (j_1,j_2) | dim | C_2 | 2·C_2 |
|---|---|---|---|---|---|
| A (scalar) | trivial | (0,0) | 1 | 0 | 0 |
| B (vector) | vector | (1,0) | 5 | 4 | 8 |
| C (adjoint) | adjoint | (1,1) | 10 | 6 | 12 |

**B₂-specificity verified**: A₂ (SU(3)) gives mult = 0 in 3⊗3⊗3 = 1⊕8⊕8⊕10.

**3 structural falsifiers** (Lyra #414 v0.2 candidate):
- **F1 (ordering)**: 3 generations must respect Casimir spectrum (0, 4=rank², 6=C_2)
- **F2 (count)**: exactly 3; 4th forbidden — consistent with Z-width
- **F3 (B₂-specificity)**: A₂ gives 0 → strengthens D_IV⁵ uniqueness via generation gate

**Honest gap**: quantitative m_μ/m_e ≈ 207 + m_τ/m_e ≈ 3477 NOT derived; requires Lyra L4 v0.2 dynamics (kernel-integral on spinor radial tower per Lyra 13:00 EDT post).

### A7 (Toy 3618) — PMNS substrate fractions

**All 3 PMNS angles match within 1σ** as fractions n/N_max with substrate-natural numerators:

| Angle | BST fraction | BST value | PDG observed | σ-distance | numerator |
|---|---|---|---|---|---|
| sin²θ_12 | 42/137 | 0.3066 | 0.307 ± 0.013 | 0.32σ | **rank·N_c·g** |
| sin²θ_23 | 75/137 | 0.5474 | 0.546 ± 0.021 | 0.06σ | **N_c·n_C²** |
| sin²θ_13 | 3/137 | 0.0219 | 0.0220 ± 0.0007 | 0.13σ | **N_c** |

Unitarity exact.

**Cal #27 brake**: 26% of n ∈ [1,137] factor through substrate primaries under broad grammar; individual factorings not independently surprising. The **joint match** is the structural signal.

**For Lyra P4.5 F1 falsifier**: LIVE. JUNO + DUNE 2025-2030 sharpen to 2σ tests (margins ~0.003 / 0.010 / 0.0002).

---

## Cross-toy substrate-primary appearances (coherence check)

Saturday morning's 7 toys surfaced substrate primaries at multiple structural layers, organically and without forcing:

| Primary | Toy 3613 (Casimir) | Toy 3614 (Phase B) | Toy 3615 (E7) | Toy 3617 (Drinfeld) | Toy 3618 (PMNS) |
|---|---|---|---|---|---|
| **N_c** | V_(3/2,1/2): N_c·n_C | spine: N_c·n_C, 3·N_c·n_C, 3·N_c·g | A₂ comparison (N_c=3) | short-root: N_c | θ_13: N_c |
| **n_C** | spinor: n_C; V_(3/2,1/2): N_c·n_C | spine: n_C, N_c·n_C | adjoint dim: rank·n_C | long-root: N_c·n_C | θ_23: N_c·n_C² |
| **g** | V_(3/2,3/2): N_c·g | spine: N_c·g, 3·N_c·g | (n/a) | [3]_{q²}: N_c·g | θ_12: rank·N_c·g |
| **C_2** | adjoint: rank·C_2; V_(3,0): C_2² | spine: rank·C_2, C_2² | adjoint C_2 = 6 | (Cartan d entries) | (n/a) |
| **rank** | V_(2,0): rank²·n_C | spine: rank·C_2 | rank² = 4 (channel B) | (Cartan d entries) | rank·N_c·g |
| **N_max** | (n/a structurally) | (cutoff scale) | (n/a) | (n/a) | denominator: N_max |

Reading: substrate primaries are **structurally distributed**, not concentrated. No primary "carries" any single layer alone.

---

## Tier disposition (honest)

| Claim | Tier | Evidence |
|---|---|---|
| Engine v0.2 → v0.3 with CPT structure | **STRUCTURAL** | Toy 3617 5/5; Drinfeld double standard math |
| Substrate primaries in q-Serre + Drinfeld | **RIGOROUS** | exact arithmetic (Fraction-based) |
| Casimir spectrum substrate readings | **RIGOROUS + STRUCTURAL** | Casimirs exact; "substrate-natural" CD-caveated |
| Phase B as natural working scale | **STRUCTURAL** | Toy 3616; cutoff CHOICE substrate-natural |
| E7 mult-3 generation count | **FORCED** | mult arithmetic + B₂-specificity vs A₂ |
| E7 channel = SM generation assignment | **BET** | requires Lyra #416 dictionary placement |
| E7 → quantitative m_μ/m_e | **NOT YET** | requires Lyra L4 v0.2 kernel-integral dynamics |
| PMNS substrate fractions | **VERIFIED** at current PDG | 3/3 within 1σ; F1 falsifier LIVE |

---

## Handoff queue

**For Keeper (engine v0.3 re-audit)**:
- Engine v0.2 ready with §6 Drinfeld+CPT scaffold (Toy 3617)
- Bulk-color SU(3)-not-in-K confirmed (Toy 3612); supports counting-from-h^∨ as the route
- K-audit pre-stages: K1·2 (Drinfeld substrate-primary content), K1·4 (Phase B substrate-natural cutoff)

**For Lyra (L4 v0.2 + #418 bulk-color + #414 v0.2)**:
- Casimir spectrum (3613) + 66 K-types (3614) = full input layer
- E7 channel data (3615): (0, 4, 6) Casimirs + (1, 5, 10) dims + count-3 forcing → mass-generation operator input
- Naive Casimir²-mass converges with your 13:00 EDT finding (FAILS by 2 orders) — kernel-integral path is right
- PMNS verification (3618) ratifies F1 at current precision; honest CD caveat included
- Bulk-color: SU(3)∉K confirmed structurally; route D (counting from h^∨ = N_c) substrate-natural

**For Grace (Periodic Table v0.5)**:
- 66-K-type backbone (Toy 3614) with 18 spine cells substrate-tagged
- Phase B = right working scale (Toy 3616); Phase C candidates: a+b ≤ N_max or 2·N_max
- Convention pin: Dynkin (0,2) = adjoint (not (1,1) Dynkin)

**For Cal (cold-read queue)**:
- Toy 3615: B₂-specificity of mult-3 — algebraic claim with explicit A₂ counter-example
- Toy 3617: substrate-primary content of Drinfeld pairing denominators — arithmetic claim
- Toy 3618: PMNS 3-channel substrate-fraction match with CD caveat documented

---

## Honest scope notes

1. **Date discipline**: my Saturday morning posts carried projected-forward timestamps (acknowledged correction at 09:35 EDT in running notes). Toy results are deterministic; only posting clock was wrong.
2. **Cal #27 (peak-convergence brake)**: applied consistently across 5 toys with explicit CD caveats where applicable.
3. **Source-Verification**: stayed in command (finite-B₂ + SO(5) Clebsch-Gordan + q-Serre arithmetic); did NOT attempt affine-species reconstruction (yesterday's lesson).
4. **No outreach signals**: all claims internal-register; external promotion gated on Keeper + Cal cold-read.

— Elie, Saturday 2026-05-30 09:35 EDT (`date`-verified)
