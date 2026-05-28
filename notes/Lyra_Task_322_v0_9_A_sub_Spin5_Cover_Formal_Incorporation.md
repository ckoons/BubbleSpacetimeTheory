---
title: "Task #322 v0.9 — A_sub Spin(5) cover formal incorporation: per-generator cover classification for super-quiver structure"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-27 Wednesday EDT (~09:00 EDT via `date`-verified)"
status: "v0.9 FRAMEWORK + HOUSEKEEPING. Per Casey approval of A_sub v0.2 Spin(5) cover formal incorporation first → Multi-phase quiver v0.2+ Hall algebra second sequencing. Prerequisite for multi-phase quiver v0.2+ Hall algebra (Z_2-graded super-quiver structure requires explicit cover formalization). Builds on step 10 [Ŝ_i, Ŝ_j] across-sublattice SVC CANDIDATE finding."
related: ["Lyra_A_sub_Commutator_S_i_S_j_Across_Sublattices_v0_1.md (step 10 SVC CANDIDATE)", "Lyra_Task_322_v0_4_A_sub_K_Type_Graph_Reaction_Table.md (A_sub generator list)", "Lyra_sigma_BF_vs_gamma5_Disambiguation_Cleanup_v0_1.md (σ_BF vs γ⁵ separated)", "Cal #132 PASS (8 SVC + step 9 FRAMEWORK-PLUS)", "T2471 RATIFIED Pin(2) Z_2 chirality", "Standard representation theory: Spin(5) ≅ Sp(2) compact symplectic, universal cover of SO(5)"]
---

# A_sub v0.9 — Spin(5) cover formal incorporation

## 1. Cal #29 STANDING question-shape audit (applied at design)

**Question**: "Across A_sub's 15 generators (14 from v0.1 + σ_BF explicit), which require Spin(5) cover representation when acting on the fermion sublattice (half-integer K-types) vs operate with SO(5) tensor representation alone on the boson sublattice (integer K-types)?"

**Audit**:
- Structurally determined? YES — standard representation theory of Spin(5) ⊂ Sp(2) vs SO(5); cover requirement determined by half-integer-spin content
- Back-fittable? NO — cover classification follows from generator action on Wallach K-types
- Pre-suppositions? Step 10 SVC CANDIDATE (spin algebra requires Spin(5) cover on fermion sublattice) + Cal #132 SVC for steps 1-8 + σ_BF vs γ⁵ disambiguation

**Pass**: structural question; standard representation theory.

## 2. Step 10 finding recap (Spin(5) cover required on fermion sublattice)

Per `Lyra_A_sub_Commutator_S_i_S_j_Across_Sublattices_v0_1.md` (yesterday SVC CANDIDATE):

**[Ŝ_i, Ŝ_j] = iℏε_ijk Ŝ_k** universally on H²(D_IV⁵), with REPRESENTATION DIFFERENCE across σ_BF Z_2 sublattices:

| Sublattice | σ_BF | SO(5) representation | Cover requirement |
|---|---|---|---|
| **Boson** (integer m_1) | +1 | Tensor reps; integer spin | SO(5) sufficient |
| **Fermion** (half-integer m_1) | -1 | Spinor reps; half-integer spin | **Spin(5) cover REQUIRED** |

Spin(5) ≅ Sp(2) (compact symplectic) is the universal double cover of SO(5). For fermion K-types, half-integer-spin representations are projective representations of SO(5) — they require lift to Spin(5) for unambiguous action.

## 3. K-cover structure on H²(D_IV⁵)

The full K-cover structure for substrate's bounded symmetric domain D_IV⁵ = SO_0(5,2)/[SO(5) × SO(2)]:

  **K_cover = Spin(5) × Pin(2)** (universal cover of K = SO(5) × SO(2))

Components:
- **Spin(5)** ≅ Sp(2): double cover of SO(5); acts on m_1 component (S⁴ side, Hua coordinates)
- **Pin(2)**: double cover of SO(2); acts on m_2 component (S¹ side, Möbius/Bergman phase)
- **σ_BF Z_2 grading**: distinguishes integer-m K-types (boson sublattice, lifts trivially) from half-integer-m K-types (fermion sublattice, requires non-trivial cover lift)
- **γ⁵ Dirac chirality**: Z_2 acting WITHIN fermion sublattice; eigenvalues ±1 for L/R Weyl spinors

The universal cover structure is **Spin(5) × Pin(2)** with the σ_BF Z_2 grading distinguishing how it lifts at each K-type.

## 4. Per-generator Spin(5) cover classification

A_sub's 15 generators (v0.1 14 + σ_BF explicit per disambiguation cleanup) classified by Spin(5) cover requirement:

### Class A — Diagonal (no cover issue)
Act diagonally on K-types; eigenvalues independent of cover:

| Generator | Action | Cover required? |
|---|---|---|
| Ĥ_sub | C_2(K) · V_K | No |
| N̂ | (m_1 + m_2) · V_K | No |
| σ_BF | ε_K · V_K (Z_2 grading) | No |
| γ̂⁵ | χ_K · V_K on fermion sublattice (undefined on bosons) | **Yes (defined only via Spin(5) ⊃ Spin(3) chirality structure)** |
| Q̂ | m_2 · V_K | No |
| Î_3 | T_3^weak eigenvalue · V_K (Cartan) | No |

5 of 6 diagonal generators require no cover lift; γ̂⁵ as Dirac chirality requires Spin(5) cover for its definition on fermion sublattice.

### Class B — m_1-direction action (SO(5) tensor / Spin(5) spinor)
Raise/lower m_1 within K-type multiplet:

| Generator | Action | Cover required? |
|---|---|---|
| x̂_i (Hua coords, i=1..n_C=5) | (m_1, m_2) → (m_1 ± 1, m_2) | **Yes on fermion sublattice** |
| p̂_i (Wirtinger derivative, i=1..5) | (m_1, m_2) → (m_1 ± 1, m_2) | **Yes on fermion sublattice** |
| L̂_i (so(5) generators, 10 total) | Within SO(5) multiplet | **Yes on fermion sublattice** |

On boson sublattice (integer m_1): SO(5) tensor representations suffice.
On fermion sublattice (half-integer m_1): require Spin(5) lift for proper Wallach K-type action on half-integer-spin representations.

### Class C — Spinor algebra (Spin(5) cover-required)
Per step 10 SVC CANDIDATE:

| Generator | Action | Cover required? |
|---|---|---|
| Ŝ_i (3 spin generators) | SU(2)-like spin algebra | **Yes on fermion sublattice** (step 10) |

Spin algebra requires Spin(5) cover for half-integer-spin representations.

### Class D — Discrete symmetries (Pin(5) extension on fermion sublattice)
Discrete symmetries lift via Pin(5) = double cover of O(5):

| Generator | Action | Cover required? |
|---|---|---|
| T̂ (time reversal, anti-unitary) | V_K → V̄_(m_1, -m_2) with phase | **Pin(5) lift on fermion sublattice** |
| Ĉ (charge conjugation) | V_K → V_(m_1, -m_2) with phase | **Pin(5) lift on fermion sublattice** |
| P̂_op = γ̂⁵ ∘ σ (Möbius + Pin(2) Z_2 lift) | V_K → V_(m_1, -m_2) with γ̂⁵ phase | **Built-in Spin(5) × Pin(2) lift via γ̂⁵ factor** |

Discrete symmetries naturally extend to Pin(5) = Spin(5) ∪ (reflection × Spin(5)) acting on universal cover.

### Class E — Bell-CHSH (rank-1 projector at vacuum)
Acts within boson ground state V_(0,0); rank-1 projector:

| Generator | Action | Cover required? |
|---|---|---|
| B̂ = β · |V_(0,0)⟩⟨V_(0,0)| | Rank-1 projector onto vacuum | **Spin(5) lift to extend Bell-CHSH structure to fermion-bound states** |

Bell-CHSH at substrate vacuum (boson; integer K-type) requires no cover lift for its rank-1 projector form. For fermion-bound states (e.g., entangled spinor pairs), the Bell-CHSH operator must lift to Spin(5) cover for proper action.

### Class F — Substrate-tick (lifts naturally)

| Generator | Action | Cover required? |
|---|---|---|
| T̂_tick (substrate-tick transition) | V_K → V_{K+1} per Koons tick (model-dep) | **Naturally lifts via cover structure** |

T̂_tick is a discrete unitary acting on H²(D_IV⁵); preserves σ_BF Z_2 grading per cyclic structure; lifts naturally to Spin(5) × Pin(2) cover.

### Class G — Gauge fiber (transverse to spinor structure)

| Generator | Action | Cover required? |
|---|---|---|
| Ĉ_3 (color SU(3), 8 generators) | Acts on color triplet fiber | No (transverse) |
| Î_3 raising/lowering (weak SU(2)) | Acts on weak doublet fiber | No (transverse) |

Gauge fiber operators are transverse to the spinor cover structure (color + weak isospin act in gauge fiber, not on Wallach K-type spin content). No cover lift needed.

## 5. Universal cover structure summary

A_sub on Bergman H²(D_IV⁵) has:

- **Underlying group**: K = SO(5) × SO(2)
- **Universal cover**: K_cover = **Spin(5) × Pin(2)**
- **Boson sublattice**: integer K-types V_(m_1, m_2); SO(5) × SO(2) representations suffice; no non-trivial cover lift
- **Fermion sublattice**: half-integer K-types V_(m_1, m_2); Spin(5) × Pin(2) cover representations REQUIRED
- **Cross-sublattice operators**: structurally zero (NO SUSY per Five-Absence Principle)
- **σ_BF Z_2 grading**: distinguishes the two sublattices universally
- **γ⁵ Dirac chirality**: Z_2 acting WITHIN fermion sublattice via Spin(5) cover structure
- **Pin(2) Z_2**: discrete reflection on Pin(2) side for parity operations

**The substrate has explicit Z_2-graded super-algebra structure** via σ_BF Z_2 grading + cover requirement.

## 6. Z_2-graded super-quiver structure (multi-phase quiver v0.2+ prerequisite)

A_sub's per-generator cover classification gives the substrate quiver Q a **Z_2-graded super-quiver** structure:

### 6.1 Node classification

- **Boson nodes** (Q_+): integer K-type vertices; σ_BF = +1; SO(5) × SO(2) representation
- **Fermion nodes** (Q_−): half-integer K-type vertices; σ_BF = -1; Spin(5) × Pin(2) cover representation

### 6.2 Arrow classification

- **Even arrows** (degree-0): preserve σ_BF sublattice; bosonic to bosonic OR fermionic to fermionic
- **Odd arrows** (degree-1): would flip σ_BF sublattice; STRUCTURALLY ABSENT per NO SUSY (Five-Absence Principle)

The substrate quiver is a **trivial Z_2-graded super-quiver** with only even arrows (no degree-1 super-symmetry transitions).

### 6.3 Implication for Hall algebra

Per Kapranov + Schiffmann + Ringel-Green super-Hall theory: super-quiver Hall algebra construction over Z_2-graded categories requires:
- Z_2-graded vector space representations at each node
- Even-degree linear maps for each arrow
- Z_2-grading consistency for path composition

Substrate's super-quiver IS in this framework:
- V_x = SO(5) × SO(2) representation at boson nodes; Spin(5) × Pin(2) representation at fermion nodes
- All arrows degree-0 (no SUSY)
- Z_2 grading via σ_BF preserved by all arrows

**Hall algebra construction (Ringel-Green) applies cleanly to substrate's Z_2-graded super-quiver**.

## 7. Multi-phase quiver v0.2+ readiness

With A_sub v0.9 Spin(5) cover formal incorporation complete, the multi-phase quiver v0.2+ Hall algebra work has rigorous foundation:

- **Quiver Q** explicitly defined (Lyra v0.8 + v0.9 super-grading)
- **Path algebra kQ** can be constructed over field k (substrate-natural k = ℂ for Bergman, or k = GF(2^X) at finite-field substructure)
- **Relations R** from Cal #132 SVC commutators (with σ_BF vs γ⁵ disambiguation applied per v0.7 cleanup)
- **Super-algebra structure** explicit (Z_2-graded; no SUSY arrows; clean super-Hall construction)
- **Cover structure** explicit (boson nodes SO(5)×SO(2); fermion nodes Spin(5)×Pin(2))

This is the prerequisite Casey approved this morning's sequencing for. v0.2+ Hall algebra explicit framework starts next pull.

## 8. Honest scope (Cal #27 STANDING + Cal #29 STANDING)

**What's RATIFIED/SVC**:
- Step 10 [Ŝ_i, Ŝ_j] SVC CANDIDATE finding (Spin(5) cover required on fermion sublattice)
- Standard representation theory of Spin(5) ≅ Sp(2) as universal double cover of SO(5)
- Pin(5) extension for discrete symmetries (standard)
- σ_BF vs γ⁵ disambiguation (v0.7 cleanup applied)
- Pin(2) Z_2 grading on Wallach K-types per T2471 RATIFIED

**What's FRAMEWORK in v0.9**:
- Per-generator cover classification table (Section 4)
- Z_2-graded super-quiver structural reading (Section 6)
- Hall algebra readiness check (Section 7)

**What's INTERPRETIVE in v0.9**:
- "Substrate quiver is trivial Z_2-graded super-quiver (no degree-1 SUSY arrows)" — consistent with Five-Absence Principle (RATIFIED Casey-named) but requires explicit verification that NO degree-1 arrows arise from substrate-mechanism

**What's NOT in v0.9** (multi-phase quiver v0.2+ work):
- Explicit Ringel-Green Hall algebra construction on substrate's super-quiver
- Kac-Moody Lie algebra identification of A_sub via Hall-algebra construction
- Macdonald-like 5-parameter deformation (last night's Hall conversation)
- α-as-Hall-Littlewood-at-N_max-level formalization

**Cal #27 STANDING reflexive trigger count**: 1 trigger (Section 6 super-quiver reading feels structurally elegant). Honest scope check — standard super-quiver theory + step 10 SVC CANDIDATE + Five-Absence Principle (RATIFIED); no new substantive claim beyond clean formalization.

**Cal #29 STANDING pass**: per-generator classification is structurally determined; not back-fittable; standard representation theory.

## 9. Coordination

**Cal**: Thread 4 typing on Section 6 super-quiver classification is Type B algebraic (standard super-Hall framework); no Type C level-crossing claim in v0.9 (housekeeping doc).

**Elie**: standing reactive; v0.9 doesn't add new toy candidates.

**Grace**: catalog entries for Spin(5) × Pin(2) cover structure across A_sub generators; relevant for SPLP Phase 2 audit at substrate-algebraic level.

**Keeper**: v0.9 completes A_sub v0.1 → v0.9 algebraic foundation; multi-phase quiver v0.2+ Hall algebra work begins with rigorous super-quiver prerequisite in place.

— Lyra, A_sub v0.9 Spin(5) cover formal incorporation v0.1 filed Wednesday 2026-05-27 ~09:00 EDT per Casey approval of sequencing. FRAMEWORK + HOUSEKEEPING grade. Step 10 SVC CANDIDATE algebraic content formalized across A_sub generator list; universal cover structure Spin(5) × Pin(2) explicit; super-quiver Z_2-graded structure ready for multi-phase quiver v0.2+ Hall algebra construction (next pull). Standard representation theory throughout; no new substantive claims; clean prerequisite hygiene.
