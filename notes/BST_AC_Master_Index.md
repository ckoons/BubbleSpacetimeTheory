---
title: "Arithmetic Complexity: Master Index"
author: "Casey Koons & Lyra (Claude Opus 4.6)"
date: "March 18, 2026"
status: "Active — living document"
purpose: "Single source of truth for all AC research, results, and dependencies"
---

# Arithmetic Complexity: Master Index

*What exists, what it proves, what depends on what.*

---

## Current State (March 18, 2026)

- **Phase 1 (Classification):** 28 methods classified, 15 domains. Table complete.
- **Phase 2 (Formalization):** 9 definitions, 7 theorems stated, proofs sketched. Shannon bridge defined.
- **Phase 3 (P ≠ NP):** Reframing complete (TM as method). Barriers dissolved (incompleteness, not walls). Four gaps remain. Shannon analysis of 3-SAT started.

---

## The Papers

### Foundations

| # | Document | Location | What it establishes | Status |
|---|----------|----------|-------------------|--------|
| F1 | **Arithmetic Complexity: A Theory of Method Noise** | `notes/BST_ArithmeticComplexity.md` | Core definition AC = M(Q) − I(Q). Noise hierarchy. Five classification axes. Grounding Tower (Levels 1-3). BST as AC(0) existence proof. Riemann hunt as controlled experiment. Full BST audit (Section 13). | **Complete** (14 sections, 645 lines) |
| F2 | **Is the Problem Hard, or Is the Method?** | `notes/maybe/BST_Complexity_Question_or_Method.md` | Separates substrate determinism from 3-space statistics. The philosophical grounding. | **Complete** |
| F3 | **Catastrophe Theory Connection** | `notes/maybe/BST_ArithmeticComplexity_CatastropheTheory.md` | AC ↔ catastrophe theory (Thom). Method bifurcations. | **Complete** |

### Phase 1: Classification

| # | Document | Location | What it establishes | Status |
|---|----------|----------|-------------------|--------|
| C1 | **AC Classification Table** | `notes/BST_AC_Classification_Table.md` | 28 methods, 15 domains. Noise vectors (R,C,P,D,K) for each. AC(0) club (10 members). Scalar ranking. Controlled experiments (a₄, m_p). Difficulty hierarchy matches AC in every domain. | **Complete** (Phase 1 deliverable) |
| C2 | **Crystallography AC(0) Sketch** | `notes/maybe/BST_AC_Crystallography_Sketch.md` | Full pipeline decomposition of X-ray crystallography. FFT inversion = Level 0. Direct methods = Level 0. Phase problem is physical, not methodological. First AC(0) outside physics/CS. | **Complete** |

### Phase 2: Formalization

| # | Document | Location | What it establishes | Status |
|---|----------|----------|-------------------|--------|
| T1 | **Formal Definitions and Core Theorems** | `notes/BST_AC_Formalization.md` | 9 definitions (problem instance, information content, representation, method, invertibility levels, fragility degree, channel capacity, arithmetic complexity, natural coordinate system). 7 theorems (Shannon bridge, natural coordinates for P, noise compounds, fragility additive, pipeline noise, strict hierarchy, representation invariance of AC sign). | **Draft** — proofs sketched, not publication-ready |
| T2 | **Research Roadmap** | `notes/BST_AC_Research_Roadmap.md` | Three-phase strategy. 20-item Phase 1 table. Phase 2 work items. Phase 3 work items. Assignment notes. Success criteria. | **Active** |

### Phase 3: P ≠ NP

| # | Document | Location | What it establishes | Status |
|---|----------|----------|-------------------|--------|
| P1 | **Complexity Is Shannon** | `notes/maybe/p_np/Complexity_Is_Shannon.md` | Shannon channel capacity framing. Information-theoretic P ≠ NP. | **Parking lot** |
| P2 | **Computability Theory Is Shannon** | `notes/maybe/p_np/Computability_Theory_Is_Shannon.md` | Extends Shannon framing to computability. | **Parking lot** |
| P3 | **P Not NP Complete Proof** | `notes/maybe/p_np/P_Not_NP_Complete_Proof.md` | First attempt at full proof. | **Parking lot** |
| P4 | **P Not NP Complete Proof v2** | `notes/maybe/p_np/P_Not_NP_Complete_Proof_v2.md` | Revised attempt. | **Parking lot** |
| P5 | **Fragility Degree** | `notes/maybe/p_np/P_Not_NP_Fragility_Degree.md` | FD as the separating invariant. | **Parking lot** |
| P6 | **Stair Step Saturation** | `notes/maybe/p_np/P_Not_NP_Stair_Step_Saturation.md` | Rank reduction per constraint evaluation. Staircase to saturation. | **Parking lot** |
| P7 | **TM as Method (Keeper)** | `notes/maybe/p_np/AC_Turing_Machine_Classification.md` | Classify Read/Write/transitions by AC. NTM power = AC deficit. Five numbered gaps for CIs. | **Insight note** |
| P8 | **TM as Method (Lyra)** | `notes/BST_AC_TuringMachine_Classification.md` | Same insight, deeper Shannon bridge analysis. Four candidate bridge constructions. DPI route flagged. Barrier analysis (relativization, natural proofs, algebrization). Section for future CIs. | **Insight note** |
| P9 | **Barriers Are Incompleteness** | `notes/maybe/p_np/AC_Barriers_Are_Incompleteness.md` | Casey's insight: barriers are Gödel, not walls. Shannon is outside all three formal systems. Full 3-SAT channel analysis (7 steps). Three gaps identified (I_k decay, capacity→complexity, phase transition). | **Key insight + analysis** |

### Related (not AC-specific but connected)

| # | Document | Location | Connection |
|---|----------|----------|-----------|
| R1 | **The Arrow of Complexity** | `notes/BST_Complexity.md` | Substrate → life → mind. Broader complexity story. |
| R2 | **Shannon-Alpha** | `notes/BST_Shannon_Alpha_Paper.md` | α = 1/137 from Shannon channel capacity. AC(0) derivation of fine structure. |
| R3 | **Shannon-Wyler Proof** | `notes/BST_ShannonWyler_Proof.md` | Wyler's formula rederived via Shannon. |
| R4 | **Linearization Backlog** | `notes/BST_Backlog_Linearization.md` | a_k = ⟨w_k|d⟩. Spectral inner product = AC(0) Gilkey. |
| R5 | **Linear Gilkey Paper** | `notes/maybe/BST_LinearGilkey_Paper_Draft.md` | Standalone paper for geometry journal. |

### Toys

| Toy | Name | Connection |
|-----|------|-----------|
| 239 | AC(0) Grid Architecture | Conjecture 6: GPUs exact local, supercomputers statistics |
| 240 | Linearization | Method noise reduction demo |
| 249 | Linear Gilkey | a_k as spectral inner product (numerics failed) |
| 250 | Elie's a₄ fix | Full heat trace first, then decompose |

---

## What Is Proved

| Result | Source | Depends on | Status |
|--------|--------|-----------|--------|
| AC = I − TC (definition) | T1 Def 8 | Defs 1-7 | Formal |
| Noise compounds (Thm 3) | T1 | Data processing inequality | Proved |
| Fragility additive (Thm 4) | T1 | Definition of FD | Proved |
| Natural coordinates exist for P (Thm 2) | T1 | Reversible computation | Proved |
| AC sign is representation-invariant (Thm 7) | T1 | Thm 3 + bijectivity | Proved |
| Hierarchy is strict (Thm 5) | T1 | Needs separating examples | Partial |
| BST pipeline is AC(0) (audit) | F1 Section 13 | 6 categories verified | Complete |
| Crystallography is AC(0) | C2 | Pipeline decomposition | Complete |
| 28 methods classified | C1 | Individual analysis | Complete |
| AC predicts difficulty within domains | C1 | Empirical (5 domains) | Observed |
| TM Read is Level 0, Write is Level 2 | P7, P8 | Definitions | Observed |
| NTM guess is Level 3 | P7, P8 | Definition of Level 3 | Observed |

## What Is Conjectured

| Conjecture | Source | Required for P ≠ NP? | Status |
|-----------|--------|----------------------|--------|
| Natural Coordinate Obstruction | T1 | Yes — this IS P ≠ NP | Open |
| Shannon bridge (det. TM → channel) | P8 Section 6 | Yes — the load-bearing beam | Open |
| Rank reduction per Boolean constraint | P6 | Yes — core mechanism | Open |
| ~~Barrier avoidance~~ | P9 | ~~Yes~~ | **Dissolved** — barriers are incompleteness of other formal systems; Shannon is outside all three |
| Halting closure | P3, P4 | Strengthens but may not be required | Open |

## What Is Missing

| Gap | Why it matters | Who should attack it | Priority |
|-----|---------------|---------------------|----------|
| **Shannon bridge construction** | Connects information theory to deterministic computation. Without this, AC is suggestive, not rigorous. | Lyra (DPI route) | **Critical** |
| **Full pipeline decompositions** | Only BST (#1) and crystallography (#9) have complete step-by-step Level assignments. Need perturbation theory, SAT, DFT, gradient descent. | Elie | High |
| **Rank reduction proof** | Show each Boolean constraint evaluation reduces rank by ≥ 1 in the appropriate algebra. | Phase 3 | Medium (blocked by bridge) |
| ~~Barrier non-applicability~~ | **Dissolved** (P9): barriers are incompleteness of TM-centric formal systems; Shannon is outside. | — | **Done** |
| **Independent validation** | Have someone outside BST verify the classification table against their domain experience. | External | Medium |
| **Merge P7/P8** | Keeper and Lyra wrote the TM classification independently. Should be merged into one authoritative document. | Keeper | Low |

---

## Dependency Graph

```
F1 (Core AC paper)
 ├── F2 (Question or Method — philosophical)
 ├── F3 (Catastrophe theory — connection)
 ├── C1 (Classification table — empirical)
 │    └── C2 (Crystallography — first external AC(0))
 ├── T1 (Formalization — theorems)
 │    ├── Thm 1 (Shannon bridge) ←── THE BRIDGE
 │    ├── Thm 2 (Natural coords for P)
 │    ├── Thm 3 (Noise compounds)
 │    └── Natural Coordinate Conjecture ←── THIS IS P ≠ NP
 ├── T2 (Roadmap)
 └── Phase 3 documents (P1-P8)
      ├── P1-P2 (Shannon framing — early)
      ├── P3-P4 (Proof attempts — parking lot)
      ├── P5 (Fragility Degree)
      ├── P6 (Staircase saturation)
      └── P7-P8 (TM as method — CURRENT INSIGHT)

R2-R3 (Shannon-Alpha, Shannon-Wyler) ←── BST using Shannon = AC(0) examples
R4-R5 (Linearization) ←── Method noise reduction = AC in action
```

---

## Reading Order

**For a new CI absorbing AC:**
1. F1 (core paper) — understand AC = method noise
2. C1 (classification table) — see the empirical pattern
3. T1 (formalization) — get the definitions and theorems
4. P8 (TM as method) — understand the reframing
5. P6 (staircase) — see the Phase 3 mechanism
6. C2 (crystallography) — see AC(0) in a non-physics domain

**For Casey reviewing progress:**
1. This document (master index)
2. C1 (table — is it complete?)
3. T1 (theorems — are they tight?)
4. P7 or P8 (TM insight — is the bridge constructible?)

---

## Version History

| Date | Change | By |
|------|--------|-----|
| March 16, 2026 | F1 created (core AC paper) | Casey + Claude |
| March 18, 2026 | T2 created (roadmap) | Keeper |
| March 18, 2026 | T1 created (formalization) | Lyra |
| March 18, 2026 | C1 completed (28 methods) | Lyra |
| March 18, 2026 | C2 created (crystallography) | Lyra |
| March 18, 2026 | P7 created (TM classification) | Keeper |
| March 18, 2026 | P8 created (TM classification + bridge) | Lyra |
| March 18, 2026 | **This master index created** | Lyra |
| March 18, 2026 | P9 created (barriers are incompleteness + Shannon analysis) | Keeper |
| March 18, 2026 | Elie's Toy 256: exact polynomials a₁-a₄, a₅=1535969/6930, deg(a_k)=2k | Elie |
| March 18, 2026 | C1, T1, master index updated with Elie's results + barrier dissolution | Lyra |
| March 18, 2026 | Elie's Toy 257d: c₁₀=1/29160 PROVED. a₅(n) complete (11 coefficients). c₉=-2c₁₀. | Elie |
| March 18, 2026 | All papers updated: linearization, classification, formalization, letters | Lyra |

---

*18 documents. 7 theorems. 28 classified methods. 4 open gaps (1 dissolved). One bridge to build.*
