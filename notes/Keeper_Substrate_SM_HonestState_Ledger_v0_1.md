---
title: "Substrate SM Program — honest-state ledger (claim-by-claim derived/assigned/matched scorecard) v0.1"
author: "Keeper"
date: "2026-05-28 Thursday EDT"
status: "K4 / the living program scorecard. Every major claim with its TIER (D/I/C/S) + STATUS (DERIVED / IDENTIFIED / MATCHED / ASSIGNED / FRAMEWORK / RETRACTED / UNBUILT) + what it RESTS ON + what would FLIP it. Held against the team's 'engine complete' reports. Tier-honest; this is the artifact that says exactly what BST claims at what confidence."
companions: ["Keeper_Reconciled_SM_Table_v0_1.md", "Substrate_SM_Program_Workplan_v0_2_LongQueues.md", "Keeper_3Tube_Gate_Verification_v0_1.md"]
---

# Honest-state ledger v0.1

**Status legend:** DERIVED (mechanism proved) · IDENTIFIED (matches <1%, mechanism partial) · MATCHED (value coincides, mechanism not forced) · ASSIGNED (hand-labeled; not yet derived) · FRAMEWORK (structure stated, not closed) · RETRACTED · UNBUILT.

## L1 — The algebra (engine)

| Claim | Tier | Status | Rests on | Flips when |
|---|---|---|---|---|
| Substrate Hall algebra = U_q⁺(B₂) at q=2; Serre constants = primaries {N_c, n_C, g, N_c·g} | D | **DERIVED / RIGOROUS** | E0 (Toy 3597) + A1 §3, integrality | — (stands; the strongest result in the engine) |
| "Substrate IS this algebra" (B₂ from D_IV⁵ type-IV) | I | IDENTIFIED | A1 geometry→B₂ | the canonical basis + dictionary ground it |
| 4/4 Hopf pieces (mult+coproduct, canonical basis, R-matrix, negative part) = Drinfeld double | D | **RIGOROUS AS ALGEBRA** | standard quantum-group theory (Lyra) | — (math stands; ≠ physics derived) |
| **"Goal 1 structurally complete"** | — | **WARRANTED, with caveat** | the 4 pieces exist | caveat: "structure complete ≠ physics derived" must travel with it |

## L2 — Kinematics (what particles are)

| Claim | Tier | Status | Flips when |
|---|---|---|---|
| 5-tuple particle taxonomy | partial D / partial ASSIGNED | **LEPTON SECTOR DERIVED** (Lyra #416 v0.1, 18 entries — every static axis derived: σ_BF/region/chirality/charge/particle-anti; generation indexed but per #414); photon/Higgs single-particle clean; **quark + gauge sectors still ASSIGNED** pending the bulk-color mechanism (see Gates) | quark/gauge flip together with bulk-color resolution |
| 3 colors = h^∨(B₂) = N_c = 3 | D | **DERIVED** (solid) | — |
| 3 generations = h−1 = 3 | — | **MATCHED** (the gate) | see "Gates" below |
| charge = S¹ winding / SO(2) weight; fractional charge forced by Z₃ closure | D | **DERIVED** (mechanism) | — (per-particle assignment is ASSIGNED) |
| **chirality / parity violation** = D_IV⁵ Hermitian → complex structure J = SO(2) factor of K → holomorphic Hardy space picks one sign of J → SU(2)_L = J-compatible half of Shilov stabilizer SO(4) → left-handed weak coupling, right-handed weak singlets | I | **FRAMEWORK-PLUS** — Lyra L3 geometric mechanism; the substrate's *complex orientation* IS the parity choice ("Nature doesn't waste the i" — one SO(2) does four jobs: Hermitian / U(1) charge / Shilov direction / parity) | per-particle L/R labeling pending SO(5,2)→Lorentz embedding pin (Lyra honestly flagged) |
| confinement (no Shilov value for non-singlets) | I | **DERIVED, FRAMEWORK-PLUS** | coupling map multi-week |

## L3 — Dynamics (the process engine)

| Claim | Tier | Status | Flips when |
|---|---|---|---|
| fusion = Hall product (extension-counting, GF(2)) | D | **DERIVED AS ALGEBRA** (E2/3600) | physics ID (which product = which reaction) is the dictionary bet |
| decay = Green coproduct; β-decay conserves Q/B/L via grading | D | **DERIVED AS ALGEBRA** (E3/3601) | the identification "this coproduct = real β-decay" rides on the dictionary |
| conservation = grading | D | **DERIVED AS ALGEBRA** | full-charge-set check pending (E4/L2) |
| scattering = R-matrix | — | **FRAMEWORK** (structure exists; amplitudes not extracted) | Lyra L6 extracts amplitudes |
| absolute mass scale, Higgs/EWSB, RGE, cross-sections | — | **UNBUILT** | Lyra L4/L5 + Elie numerics |
| **"Goal 2 mechanism built"** | — | **WARRANTED for the mechanism** | the *mechanism* is real; the *physical model* needs the dictionary |

## L4 — Composites / nuclear

| Claim | Tier | Status | Flips when |
|---|---|---|---|
| proton = bulk k=6 (C₂=6) = YM mass gap; m_p = 6π⁵·m_e | D | **DERIVED (0.01%)** | — (anchor) |
| nuclear shells = SO(5) K-type closures (SO(5) = compact factor of D_IV⁵) | I | **STRUCTURAL / HYPOTHESIS** | the SO(5) shell-closure computation (E8): does branching give 2,8,20,28,50,82,126? |
| magic-number forms (rank·products); 126 = Universal-Q; spin-orbit = C₂/n_C | S | **SUGGESTIVE** (Grace-flagged) | E8 derivation; small-target/coincidence-denominator caveat until then |

## L5 — Engineering
SP-30 falsifier designs: EXIST. Control theory: UNBUILT. (Same open dynamics layer as L3.)

## L6 — Periodic Table

| Claim | Tier | Status | Flips when |
|---|---|---|---|
| v0.2 structure (3 rows × 4 families + boson block) | — | **BUILT** | — |
| Fundamental-sector selection (the 4-backbone) | FRAMEWORK-PLUS | Grace #413 found 4 of 66 cells Casimir-anchor; Lyra's dictionary (#408, first output) selects the SAME four — **reframed to REP-ROLE**: they are exactly {trivial + ω₁ vector + ω₂ spinor + adjoint} of B₂=so(5), the canonical building-block set (rank=2 → 2 fundamentals + trivial + adjoint = 4). Rep-theory part RIGOROUS (fundamental weights / adjoint of B₂; Casimirs 0, 5/2, 4, 6). **so(5)-SPECIFIC strengthener: matter = the 4-dim spinor ω₂ = the Dirac 4-spinor (not a generic Lie fact);** σ_BF → spinor = unique fermion, trivial/vector/adjoint = bosons (matter/force split). | per-sector PHYSICAL identification (reps = Higgs/photon/lepton/gauge) is the dictionary bet. Lyra's honest reframe: SELECT by rep-role (no tunable freedom); Casimir-anchoring is a CORRELATED consistency check (small reps→small Casimirs), NOT independent confirmation. Promoted speculative→rep-grounded; DERIVED when the dictionary closes the identifications. |
| per-particle cell assignments | — | **ASSIGNED** | the dictionary (#408) flips them to DERIVED |
| gaps = predictions (no 4th row, no GUT/SUSY/steriles) | — | **MATCHED→prediction** | the row-count forcing closes the no-4th-row gap |

## The gates (open work)

| Gate | Status | Detail |
|---|---|---|
| **A_sub↔Hall dictionary** (THE bottleneck) | **UNBUILT, in progress** (Lyra L1/#408) | flips L2/L3/L6 from ASSIGNED→DERIVED; everything physical rides here |
| **Generation-forcing** | **TENSION RELIEVED, NOT CLOSED** (Lyra #412+#414 reframe) | The "4 routes → 3" was over-counting; really TWO independent B₂ 3's: **(I)** Coxeter h−1 = \|Φ⁺\|−1 = 3 — **UNDERCUT** (its δ-tube realization leans ≤2). **(II)** dual-Coxeter h^∨ = N_c = 3 — a FORCED B₂ invariant. Lyra re-leaned (I)→(II), reversing her own prior: color-blindness rules out generations *carrying* color, not the count *equaling* N_c via a colorless projection (= Grace's Track P). So the count-**NUMBER** 3 is over-determined/forced (h^∨=N_c=3); the **IDENTIFICATION** "h^∨ counts generations" is the OPEN mechanism (Track P), carrying a real burden: produce TWO *independent* 3-fold structures (colors AND generations) from ONE invariant. **Keeper hold:** tension relieved (favored route no longer leans toward 2), but NOT closed — count-number forced, generation-mechanism open. This SUPERSEDES the earlier "two independent 3's (h^∨ + h−1)" framing → now "one 3 (h^∨) double-duty." Tube count #409 now matters less (route I no longer favored). |
| **Generation-forcing — mechanism** | **MATCHED, leans Coxeter/δ** | gen in affine δ-direction vs N_c-color; degenerate at B₂ (h−1=h^∨=3); Lyra L3 (#412) to turn lean→argument |
| **α-placement** | **OPEN** | coupling/evaluation at affine level (A1 §5.1) |
| **Bulk-color mechanism — v0.2 candidate (Saturday)** | **CANDIDATE / FRAMEWORK** — two-structures burden structurally addressed; SU(3)≠SO(3) burden NEW | Lyra v0.2 Direction (A) sharpened: **COLOR = SO(3) sub-vector of the SO(5) bulk holomorphic tangent** via rigorous standard branching 5(SO(5)) ↓ SO(3)×SO(2) = (3,0)+(1,±1). 3-fold is **GEOMETRIC** (substructure of the bulk K-type's SO(5)-vector content, accessed by further branching — *refinement of the v0.1 "must come from bulk" framing*: SO(3) IS in K via SO(3) ⊂ SO(5) ⊂ K, just not surfaced by first-level K-type labels). **Two-structures burden ADDRESSED at structural level**: color (SO(3) geometric) ≠ generations (h^∨/spinor-tower algebraic) — independent mathematical mechanisms (both B₂/SO(5)-rooted, but distinct structures). Directions (B) reassigned to generations (E7 spinor³-3 ≠ manifestly h^∨); (C) abandoned (no clean Z/3 in D_IV⁵). **NEW LOAD-BEARING BURDEN — the load-bearing open work**: SO(3) ≠ SU(3) (3-dim rotation vs 8-dim gauge). Lyra's "counting-not-symmetry" hypothesis (Track P) says SU(3) phenomenology must EMERGE from 3-direction counting — must derive confinement, asymptotic freedom, 8 gluons, running coupling from substrate SO(3). Multi-week open. Until emergence demonstrated: CANDIDATE only. Joint gate with #414's burden remains valid. |
| **baryogenesis α⁴** | **OPEN** (located, not sized) | E↔F asymmetry; Lyra L7 + #399 |

## Standing predictions (falsifiable)
- **ν mass ordering = NORMAL** (conditional on shared-W_n) — JUNO/DUNE.
- **Dirac neutrinos, m_ββ = 0, no 0νββ at any scale** — LEGEND-1000/nEXO. (Resolved this session vs the Majorana contradiction.)
- **No 4th generation, no GUT, no SUSY, no steriles** (table closure / Five-Absence).
- **B̂₂ tube count** — if Elie's E2 returns ≠3, that's an informative break (tubes ≠ generations → cyclotomic carries it).

## Consistency fixes (committed ee35f15)
- gravity = S¹/EM boundary condition, not a force.
- neutrino character = Dirac (Paper 108 corrected).

## Methodology guard (this session)
- **Source-Verification Tier calibration** (candidate, pending Cal): RECALLED vs VERIFIED-CITED; load-bearing claims capped at MATCHED on a recalled literature value. Motivated by the genus + tube-count sourcing failures (2 in 2 days).

## The honest one-line verdict
**The engine is real and rigorous as algebra; the dynamics mechanism is built; the proton/charge/confinement/mixing-spine results are genuinely DERIVED — but the bulk of the particle spectrum is still ASSIGNED pending the one dictionary, the generation gate is open on both count and mechanism, and the absolute-scale/Higgs/amplitude/nuclear-derivation work is UNBUILT.** We are one dictionary from "physical model," one computation (E2) from the generation count, and a known list of UNBUILT items from "complete." That is a strong, honest place — not a finished one.

— Keeper, 2026-05-28 v0.1. Update as the dictionary lands (mass ASSIGNED→DERIVED), as E2 resolves the tube count, and as the SO(5) shell-closure decides the nuclear tier.
