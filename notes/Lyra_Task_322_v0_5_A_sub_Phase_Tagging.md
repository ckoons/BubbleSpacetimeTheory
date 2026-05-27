---
title: "Task #322 v0.5 — A_sub phase-tagging: 9 commutator-edges + Wallach K-types per substrate region structure"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-26 Tuesday EDT (~09:50 EDT via `date`; date-verified)"
status: "v0.5 FRAMEWORK with Cal #132 SVC backing for 8/9 commutators + 1 FRAMEWORK-PLUS + minor §1.3 cleanup applied. Phase A Lyra-lane contribution per Casey depth-increase directive + Keeper Task #352. Integrates morning's cross-CI convergence: Grace 4-region classifier + Elie Toy 3534 gauge-region mapping + Elie Toy 3535 21-K-type enumeration. Substrate algebra UNIVERSAL; operational content REGION-DEPENDENT."
related: ["Lyra_Task_322_v0_4_A_sub_K_Type_Graph_Reaction_Table.md (v0.4 graph framing)", "Cal #132 (cold-read PASS 8/9 SVC + 1 FRAMEWORK-PLUS)", "Lyra_A_sub_Commutator_Q_P_op_v0_1.md (step 1 with §1.3 cleanup applied today)", "Lyra_A_sub_Commutators_Gamma5_with_TCP_v0_1.md (steps 3-5)", "Lyra_A_sub_Commutators_Zero_Batch_Steps_6_8_v0_1.md (steps 6-8)", "Lyra_A_sub_Commutator_B_T_tick_v0_1.md (step 9, FRAMEWORK-PLUS)", "Grace Task #340 v0.2 (region classifier: DIRECT 57%, COMPOSITION 10%+, MATERIAL 20%, COMBINATORIAL 13%)", "Elie Toy 3534 (gauge group ↔ region mapping)", "Elie Toy 3535 (21 K-type nodes; 12 bosons + 9 fermions; 0 mixed-forbidden)"]
---

# A_sub v0.5 — Phase-tagging the K-type graph

## 1. Reframe — algebra is universal; operational content is region-dependent

Cal #132 PASS verified 8 of 9 morning commutator closures at SVC tier (one at FRAMEWORK-PLUS). The substrate algebra A_sub holds **universally** on H²(D_IV⁵) — every commutator-relation is true everywhere in the K-type graph.

But the morning's cross-CI work revealed structural depth: the K-type graph has **4 operational phase regions** (Grace Task #340 v0.2 classifier). Different regions activate different commutator-edges as observable substrate mechanisms:

| Region | % catalog | Operational rule | Substrate principle |
|---|---|---|---|
| **DIRECT projection** | 57% | Single K-type → observable via Born=Bergman | SPLP (Casey-named candidate; scope-bounded here) |
| **COMPOSITION** | 10%+ | Multi-K-type via RG-flow + gauge/Yukawa couplings | Sister principle: composition rules (Elie Toy 3533/3534) |
| **MATERIAL-contextual** | 20% | Substrate framework + per-material external BC | Sister principle: external-BC dependent (pending) |
| **COMBINATORIAL** | 13% | Algebraic identities on K-type combinations | Sister principle: algebraic-identity (pending) |

This is a substantive structural deepening: substrate algebra reproduces standard physics (CPT, NO-GUT, spin-statistics, CP-violation source) **universally**, but the manifestation of these algebraic relations as observable physics differs by region.

## 2. Per-commutator phase-tagging

Each of the 9 commutators activates with primary operational content in specific regions:

### 2.1 Step 1 — {Q̂, P̂_op} = 0 (Cal #132 SVC; §1.3 cleanup applied)

**Primary region**: DIRECT projection + COMPOSITION.

- **DIRECT**: substrate-parity P̂_op contains charge-flip via Möbius σ on SO(2). Observable manifestation: substrate-CP-correlation in chirality-resolved measurements. Bell-CHSH compatible (B̂ vacuum-localized commutes with Q̂ in DIRECT phase per step 6).
- **COMPOSITION**: anti-commutation contributes to QED + QCD anomalous-dimension structure. T2476 α^{BST primary} substrate-mechanism likely sources here.
- **MATERIAL / COMBINATORIAL**: not operationally manifest (P̂_op as substrate-operator doesn't act on per-material parameters or pure-algebraic identities).

### 2.2 Step 2 — [T̂_tick, Ĥ_sub] = 2(Q̂ + N_c - 1)·T̂_tick (Cal #132 SVC, model-dependent)

(Cleanup note: v0.1 had `−(2Q̂ + N_c − 1)·T̂_tick`; sign depends on operator-order convention. Cal #132 verified algebra correctness; one of the two equivalent operator-order forms gives the +(2Q̂+N_c−1) form. Substrate discreteness signature direction is robust either way.)

**Primary region**: DIRECT + COMPOSITION.

- **DIRECT**: per-tick substrate discreteness; charge-modulated. Manifests in tree-level observables as the substrate's "minimum-action quantum" per Koons tick. The N_c − 1 = 2 baseline ensures neutral K-types still have non-zero substrate-tick activity.
- **COMPOSITION**: discreteness composes via RG-flow to continuous-limit observables. Multi-tick aggregation produces observable continuous-time physics (per SWPP one-way commitment cycle).
- **MATERIAL / COMBINATORIAL**: not operationally manifest at this level.

### 2.3 Steps 3-5 — γ̂⁵ × discrete symmetries (Cal #132 SVC)

**{γ̂⁵, T̂} = 0**, **{γ̂⁵, Ĉ} = 0**, **[γ̂⁵, P̂_op] = 0**

**Primary region**: DIRECT + COMPOSITION + COMBINATORIAL.

- **DIRECT**: discrete symmetry transformations of K-type observables; substrate-CPT theorem manifests as CPT-conjugate observables having same Casimir spectrum.
- **COMPOSITION**: γ̂⁵ enters anomaly generation in loop calculations (Elie ABJ Toy 3534 finding: γ̂⁵ required even for pure-boson observable framing via triangle diagram).
- **COMBINATORIAL**: CPT preservation appears in number-relation identities (e.g., CP-conjugate constants like masses of particle-antiparticle pairs equal at integer-arithmetic level).

### 2.4 Step 6 — [B̂, Q̂] = 0 (Cal #132 SVC)

**Primary region**: DIRECT only.

- **DIRECT**: Bell-CHSH operates as rank-1 projector onto vacuum V_(0,0); commutes with charge because vacuum has Q = 0. Substrate Bell-test is charge-blind (consistent with experimental Bell tests on charge-neutral systems).
- **COMPOSITION / MATERIAL / COMBINATORIAL**: not operationally manifest.

### 2.5 Step 7 — [L̂_i, γ̂⁵] = 0 (Cal #132 SVC)

**Primary region**: DIRECT.

- **DIRECT**: S⁴ × S¹ axis orthogonality at algebra level. Orbital angular momentum L̂_i (S⁴ side) and chirality γ̂⁵ (S¹ Pin(2) side) commute on direct K-type observables.
- **COMPOSITION**: still hold at one-loop level (spin-orbit coupling involves Ŝ_i × γ̂⁵, not L̂_i × γ̂⁵).
- **MATERIAL**: spin-orbit coupling in materials follows substrate algebra; explicit BC modulates.
- **COMBINATORIAL**: not directly relevant.

### 2.6 Step 8 — [Ĉ_3, Î_3] = 0 (Cal #132 SVC)

**Primary region**: ALL phases.

- **DIRECT**: SU(3) × SU(2) × U(1) factorize as direct-product gauge in tree-level observables; NO-GUT structural.
- **COMPOSITION**: gauge factors STILL commute at loop level (gauge group structure preserved by RG flow); QED vs QCD asymmetry per Elie Toy 3534 (abelian → COVER-REQUIRED, non-abelian → MIXED) reflects sub-region structure but doesn't break [Ĉ_3, Î_3] = 0.
- **MATERIAL**: gauge factorization preserved in material physics.
- **COMBINATORIAL**: combinatorial K-type identities respect gauge factorization (e.g., 8 = 2^N_c, 12 = N_c · g - g = ... gauge-group-dimension content).

This is the **universal phase activation** — [Ĉ_3, Î_3] = 0 is the most universally-active algebraic relation in the substrate.

### 2.7 Step 9 — [B̂, T̂_tick] = β·|V_(1,0)⟩⟨V_(0,0)| (Cal #132 FRAMEWORK-PLUS)

**Primary region**: DIRECT (Track DC primary).

- **DIRECT**: vacuum kicker; per-tick substrate dynamical mechanism for Bell-CHSH measurement. Track DC candidate (b) — 3 Cartan × {±1} = 8 paths with one violating {Q̂, P̂_op} = 0 simultaneous-diagonalizability — operates here.
- **COMPOSITION**: per-tick dynamics composes across many ticks → integrated Bell-CHSH operator probability.
- **MATERIAL**: experimental Bell test apparatuses (SP-30-1 Vienna SPDC) introduce per-material K-types.
- **COMBINATORIAL**: not directly relevant.

**Cal #132 FRAMEWORK-PLUS tier** held per Cal flag — "1-dim vs 2-dim → 1/8" is analogy not derivation. Multi-week Track DC explicit derivation pending.

## 3. K-type-to-region tagging (per Elie Toy 3535 21-node enumeration)

### 3.1 The 21 enumerated K-types

Elie Toy 3535 produced 21 K-type nodes at cutoff m_1 + m_2 ≤ 5:
- **12 bosons** (integer K-types; γ̂⁵ = +1)
- **9 fermions** (half-integer K-types; γ̂⁵ = -1)
- **0 mixed-forbidden** (empirical confirmation of A_sub v0.4 Section 2.2 spin-statistics-from-substrate prediction)

Elie's structural observation (pending Cal Thread 4): spinor K-type (1/2, 1/2) has Bergman ρ-weight (3, 2) = (N_c, rank) — Pin(2) cover Z_2 grading translates half-integer K-type highest weights to integer Bergman weights via ρ-translation.

(v0.5 honest scope: this is FRAMEWORK observation; Cal #27 STANDING reflexive — feels substrate-natural; Cal Thread 4 verification pending.)

### 3.2 Phase-tagging methodology for K-types

Each K-type V_K can appear in multiple phase regions depending on which observable derives from it:

- **DIRECT-only K-type**: low-Casimir K-types directly identifying observables (V_(0,0) substrate vacuum; V_(1/2, 1/2) electron spinor; V_(1,0) first-excited boson).
- **COMPOSITION K-type**: K-types appearing in RG-flow expansions of running couplings (e.g., V_(electron) in α(Q²) loop expansion).
- **MATERIAL K-type**: K-types parameterizing per-material observables (e.g., crystal K-types per material lattice symmetry).
- **COMBINATORIAL K-type**: K-types appearing in pure-arithmetic identities (e.g., V_(N_c, rank) in BST-primary-ratio relations).

Most K-types appear in multiple regions — phase-tagging is per-(K-type, observable) pair, not per-K-type globally.

### 3.3 v0.5 mapping (Elie's 21 K-types per primary phase region)

Without Grace's Task #355 v0.2 node-to-observable lookup (in-flight), exhaustive K-type-to-region mapping is premature. v0.5 phase-tagging methodology established; explicit per-K-type mapping is Task #355 v0.2 + Lyra v0.6 work.

**Lowest-Casimir anchor mappings** (subject to Task #355 v0.2 verification):

| K-type | Bose/Fermi | Primary phase | Observable identification (provisional) |
|---|---|---|---|
| V_(0, 0) | Boson | DIRECT | Substrate vacuum / cosmological constant Λ at Zone-4 |
| V_(1, 0) | Boson | DIRECT | First-excited substrate boson / massless gauge boson candidate |
| V_(1, 1) | Boson | DIRECT | C_2 = 6 substrate Casimir anchor (T2435 RATIFIED); higher gauge boson candidate |
| V_(1/2, 1/2) | Fermion | DIRECT | Electron spinor (lowest fermionic K-type with non-zero Casimir) |
| V_(3/2, 1/2) | Fermion | DIRECT + COMPOSITION | Proton-like K-type (composite-3-quark structure) — pending Grace v0.2 |
| V_(2, 0) | Boson | DIRECT + COMPOSITION | Higgs-like scalar K-type (pending verification) |
| V_(2, 2) | Boson | COMBINATORIAL | Possibly 8 = 2^N_c gauge identity content (pending) |

(v0.5 honest scope: these are TENTATIVE identifications subject to Grace Task #355 v0.2 lookup + Lyra v0.6+ Track P closure. Cal #27 STANDING applied — forward-derivation discipline preserved; no back-fitting.)

## 4. Region-specific substrate principles

### 4.1 DIRECT projection — SPLP (Casey-named candidate)

**Operational rule**: substrate K-type V_K → observable via Bergman projection on Shilov boundary; observable eigenvalue = substrate operator eigenvalue under physical BC.

**Scope**: 57% of catalog (Grace v0.2); 88% CLEAN within scope.

**Activates**: Steps 1-9 of morning A_sub commutators ALL operate primarily in DIRECT phase.

**Promotion status**: HOLD per Casey directive 2026-05-26 PM. Awaits Grace random-sample audit + Cal Thread 4 typing.

### 4.2 COMPOSITION — Sister Principle 1 (pending naming)

**Operational rule**: multi-K-type composition via RG-flow + gauge couplings; substrate K-type "graph paths" determine observable through composition algebra.

**Scope**: 10%+ of catalog (Grace v0.2; preliminary estimate, likely higher with refinement).

**Activates**: Loop-corrected observables (α(Q²), α_s(Q²), running masses); Bose-Fermi separation breaks via fermion-loop contributions; gauge-group sub-region structure (Elie Toy 3534 abelian vs non-abelian).

**Structural finding**: Elie's ABJ anomaly observation — γ̂⁵ required even for pure-boson observable framing via triangle diagram — suggests the COMPOSITION region has internal structure where bosonic and fermionic substrate content mix via anomaly cancellation. Multi-week ABJ-anomaly-as-structural-unifier hypothesis (Track A_sub v0.6+ post-Cal).

### 4.3 MATERIAL-contextual — Sister Principle 2 (pending naming)

**Operational rule**: substrate framework provides K-type structure; per-material external boundary conditions modulate observable values; substrate constrains but doesn't determine.

**Scope**: 20% of catalog.

**Activates**: material-specific observables (Pt Debye 240K, T_c values, lattice parameters). Substrate's K-type graph is "embedded" in per-material BC space.

**Open**: explicit substrate-mechanism for how external materials specify Shilov BC. Multi-month Track BC continuation work.

### 4.4 COMBINATORIAL — Sister Principle 3 (pending naming)

**Operational rule**: BST primary integer combinations + Mersenne ladder + Bergman normalization 225 produce closed-form arithmetic identities; substrate operates via algebraic identity, NOT eigenvalue projection.

**Scope**: 13% of catalog.

**Activates**: pure-arithmetic ratios (4/3, 7/6, gauge-group dimension ratios); Mersenne ladder identities; closed-form BST primary expressions.

**Open**: explicit substrate-mechanism for why BST primary arithmetic encodes physical content. This may connect to Grace's Graph Forces Principle candidate (over-determined identities as substrate diagnostic).

## 5. The substrate's "shape" updated (v0.5)

Per Casey's standing meta-program (A_sub v0.4 Section 7) — "what KIND of math object is the graph?":

After v0.5 phase structure incorporation, the substrate's K-type graph is:

**A Z_2-graded *-algebra (universal level) with operationally-distinct phase regions (4 identified) on a discrete-time substrate**

Math-object type candidates (refined from v0.4 Section 7):

| Candidate | Universal level | Phase-region level |
|---|---|---|
| **Quiver representation with Z_2 grading** | Universal *-algebra structure | Per-region quiver-arrow subsets activate |
| **Discrete Lie groupoid** | Universal Lie-algebra structure | Per-region groupoid-functor sub-categories |
| **Tensor network with Bergman-weighted contractions** | Universal Bergman kernel structure | Per-region tensor-contraction patterns |
| **Higher category with regional sub-categories** | Universal categorical structure | Per-region 2-morphism structures |

Refined Lyra prior (after v0.5; Cal #27 STANDING applied): the substrate IS a **multi-phase quiver representation** with universal Z_2 grading and 4 distinct phase-region sub-quivers. Cal Thread 4 + multi-week Phase B + C work resolves the math-object type.

## 6. v0.5 substantive structural finding

**The substrate algebra A_sub is universal but operationally manifests through 4 phase regions.** Standard physics (CPT, NO-GUT, spin-statistics, CP-violation source) emerges from the universal algebra; observable physics manifests through phase-region-specific operational rules.

This is consistent with the morning's three-lane convergence:
- Lyra theoretical: 9 commutator-closures producing standard-physics structural readouts
- Elie empirical: Bose-Fermi separation clean at tree-level (DIRECT region), breaks at loop (COMPOSITION); QED-vs-QCD asymmetry
- Grace catalog: 4 region classifier with SPLP scope-bounded to DIRECT

The substrate's structural picture is **deeper than universal SPLP** would suggest — it has region-specific operational rules with universal algebraic underpinnings. This is substrate-discovery, not classification.

## 7. Honest scope (Cal #27 STANDING)

**What's STRUCTURALLY VERIFIED in v0.5**:
- 8 of 9 commutator closures at SVC tier (Cal #132 PASS)
- Step 9 [B̂, T̂_tick] at FRAMEWORK-PLUS (per Cal #132)
- Grace's 4-region classifier (Task #340 v0.2 88% in-scope for DIRECT)
- Elie's 21-K-type enumeration with 0 mixed-forbidden (Toy 3535)
- §1.3 sign cleanup applied to step 1 doc

**What's FRAMEWORK in v0.5**:
- The phase-tagging methodology (Section 2 + 3.2): structured but not exhaustive
- Region-specific substrate principle naming (SPLP for DIRECT; pending names for sisters)
- Provisional K-type identifications (Section 3.3): subject to Grace Task #355 v0.2 verification
- Math-object type refinement (Section 5): multi-week + Cal Thread 4 work

**What's INTERPRETIVE in v0.5**:
- Spinor ρ-weight (3, 2) = (N_c, rank) — Elie observation pending Cal Thread 4 verification
- ABJ anomaly as bosonic-fermionic structural unifier — Track A_sub v0.6+ work
- "Multi-phase quiver representation" math-object candidate — multi-week resolution

**What's NOT in v0.5** (multi-week+):
- Track DC explicit Bell 1/8 derivation (per Casey HOLD + Keeper Priority 3)
- [Ŝ_i, Ŝ_j] across-sublattice spinor commutator (multi-week)
- Track BC hydrogen 1s explicit Bergman integral evaluation (multi-week)
- ABJ anomaly explicit substrate-mechanism (v0.6+)
- Material-region + Combinatorial-region sister principles explicit naming + derivation (multi-month)
- Phase B + C reaction-table closure (months to year+)

**Cal #27 STANDING reflexive trigger count**: 2 triggers this doc (Section 5 quiver-representation feeling substrate-natural + Section 6 unification claim feeling substrate-natural). Both flagged INTERPRETIVE in honest scope; framework-level claims with multi-week resolution.

**Casey directive compliance (2026-05-26 PM)**: SPLP filing HOLD acknowledged; no RATIFIED promotion for 8 SVC commutator closures. v0.5 stays at FRAMEWORK + SVC component closures; no principle promotion.

## 8. Coordination

**Cal**: Thread 4 cold-read on Section 3.1 spinor ρ-weight pattern + Section 5 math-object type refinement + Section 4.2 ABJ-anomaly-as-structural-unifier candidate (v0.6+ work). Type C level-crossing per Cal #122 likely for region-specific principle promotion.

**Elie**: Toy 3536 candidate — edges between the 21 K-type nodes via verified Cal-cleared commutators (steps 1-8 SVC; step 9 FRAMEWORK-PLUS). Phase A reaction-table edge set. Or alternative: gauge-group ↔ region mapping continuation per Toy 3534. Multi-day.

**Grace**: Task #355 v0.2 node-to-observable lookup with Elie's 21 K-type data; refines Section 3.3 provisional identifications. ~1-2 hours. Then SPLP Phase 2 random-sample scale-up with region classifier.

**Keeper**: Vol 15 Ch 9 case study draft integration of morning's three-lane convergence + v0.5 phase-tagging structure.

— Lyra, A_sub v0.5 phase-tagging filed Tuesday 2026-05-26 ~09:50 EDT per Casey 2026-05-26 PM directive (SPLP filing HOLD + no RATIFIED promotion) + Keeper Task #352 + Cal #132 PASS unblocks Phase A continuation. v0.5 FRAMEWORK grade with 8 SVC component closures (per Cal #132). Substantive structural finding: substrate algebra UNIVERSAL but operational content REGION-DEPENDENT; 4 phase regions identified with substrate-specific operational rules. Cross-CI three-lane convergence (Lyra theoretical + Elie empirical + Grace catalog) structurally consistent at the region-tagged level.
