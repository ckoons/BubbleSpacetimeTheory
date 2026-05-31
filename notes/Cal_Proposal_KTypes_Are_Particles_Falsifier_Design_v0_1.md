---
title: "Cal proposal v0.1 — sharp falsifier-test design for the 'K-types are the particles' keystone bet"
author: "Cal A. Brate (Cal-lane opening contribution; for Lyra refinement + execution)"
date: "2026-05-30 Saturday ~09:20 EDT"
status: "DESIGN PROPOSAL v0.1 — Cal's opening contribution to Saturday plan item 4.5 (joint with Lyra). Proposes sharp falsifier candidates for the single isolated bet on which the whole DERIVED-modulo-keystone static taxonomy rides. Cal does the discipline framing + falsifier sketches; Lyra refines + executes. Not a result; a test design."
discipline: "Cal #27 (forward-derivation) + Cal #29 (question-shape audit) + Cal #32 (parameter-role) + Calibration #33 (sourcing); applied to the bet itself"
companion: "Keeper K-Audit Dictionary First Wave Finding 3 (modulo-keystone standing rule); Lyra Friday milestone (static taxonomy rides on this one bet)"
---

# Sharp falsifier-test design for the "K-types are the particles" bet

## 0. Why this matters

Per Lyra's Friday milestone + Keeper's K-Audit Dictionary First Wave Finding 3: the whole static-taxonomy "DERIVED" rides on a single isolated bet —

> **The keystone bet**: every SM particle state is the substrate-identification of a canonical basis element of U_v(B₂) (and its affine extension U_v(B₂)^(1)) with the corresponding K-type weight; the K-type's quantum numbers (σ_BF, region, charge, etc.) are derived from the weight structure.

Four of the five static axes are DERIVED-modulo-this-bet (σ_BF, region, chirality, particle/anti); charge is LOCATED+constrained-modulo-this-bet; generation is the open mechanism gate. **If the bet falls, the whole static dictionary unflips.** That's a lot of weight on one identification.

Per Cal #27 + Keeper Finding 3: every DERIVED cell + headline must carry "modulo keystone bet" — and the standing rule is enforced. But the *test* of the bet itself is the next-order discipline: **what would falsify or confirm it directly, not just label its conditionality?** Diffuse testing (each dictionary flip independently validates pieces) doesn't sharply test the bet; it's better to design a focused falsifier.

This proposal sketches 5 sharp falsifier-test candidates, ranked by sharpness + execution feasibility. Lyra refines + executes; Cal cold-reads results.

## 1. The bet, made precise (Cal #29 question-shape)

The bet has internal structure worth separating:

- **B1 (count claim)**: at each K-type V_(λ₁,λ₂), the canonical basis dimension equals the count of physical SM particles with that K-type identification. (e.g., at (1/2,1/2): canonical basis dim should equal the lepton-count = 18 SM-observable or 24 full-Dirac.)
- **B2 (quantum-number claim)**: each canonical basis element's weight-derived quantum numbers (σ_BF from weight parity; charge from SO(2)-weight + GMN; region from Shilov/bulk stabilizer; chirality from J-sign) match a unique SM particle's quantum numbers.
- **B3 (no-ghosts claim)**: every canonical basis element corresponds to an OBSERVED SM particle — no "ghost" elements with no SM counterpart.
- **B4 (no-missing claim)**: every SM particle has a canonical basis element correspondent — no "missing" SM particle predicted by canonical basis but unobserved.
- **B5 (dynamics claim)**: canonical basis multiplication (Hall product) corresponds to physical fusion/reaction; coproduct to decay; R-matrix to scattering. The dynamic axis rides on this.

Each sub-claim can be falsified independently. Tests below target specific sub-claims.

## 2. Falsifier candidates (5 tests, sharpness-ranked)

### Test T1 — Count test at the lepton K-type (sharpest, executable now)

**Target**: B1 (count claim).

**Design**: compute dim(canonical basis of U_v(B₂)) at weight (1/2,1/2) for substrate-natural specialization (v=2 Hall-Littlewood / field-size; or as appropriate per the affine pin). Compare to 18 (SM-observable lepton states) or 24 (full Dirac with ν_R counted). Mismatch → bet falls (at this K-type at least; full count requires testing across K-types).

**Sharpness**: HIGH. The canonical basis dimension at a specific weight is a STANDARD COMPUTATION in quantum group rep theory; result is forced. If dim ≠ 18 (or 24), the bet is broken at the lepton K-type — a clean break. If dim = 18 (or 24), strong confirmation (numerical, but at least the count works).

**Execution path**: Elie's lane. Probably a few hours' computation. Pin the affine type first (Saturday plan P1.3); then dim of canonical basis at (1/2,1/2) is computable from PBW basis + Kashiwara crystal arguments.

**Calibration #33 sourcing**: the dim formula for canonical basis at weight λ is a standard quantum group result (Lusztig/Kashiwara), VERIFIED-CITED-able. Apply.

### Test T2 — Quantum-number partition test at the adjoint K-type

**Target**: B2 (quantum-number claim) + B3 (no-ghosts) on the gauge sector.

**Design**: at K-type (1,1) (the adjoint, dim 10), the canonical basis elements should partition into electroweak gauge bosons (4: W±, Z, photon — though γ might be elsewhere) by their weight-derived quantum numbers. If the 10 elements include items with NO SM gauge-boson counterpart (excess), bet fails B3 (ghost). If SM gauge bosons can't all be accommodated by the 10 (deficit), bet fails B4 (missing) at this K-type.

**Sharpness**: MEDIUM-HIGH. The 10-dim adjoint accommodating EW gauge bosons + 8 gluons = 12 SM gauge bosons is a known mismatch (the bulk-color v0.1 open gate). So this test interacts with the bulk-color question — the test's sharpness depends on resolving where color/gluons sit (bulk per Lyra v0.1). If bulk-color resolution moves gluons OUT of the adjoint K-type, the adjoint should carry exactly 4 (EW) — testable.

**Execution path**: joint with bulk-color v0.2. Probably weeks-multi-week as the bulk-color mechanism develops.

### Test T3 — Cross-multiplication test (Hall product = physical fusion?)

**Target**: B5 (dynamics claim).

**Design**: pick a SPECIFIC known SM vertex (e.g., lepton-photon coupling: ℓ̄γℓ at the QED vertex). Compute the Hall product (1/2,1/2) × (1,0) in U_v(B₂) canonical basis. Result should contain (1/2,1/2) (the lepton output) with structure-constant matching the QED coupling magnitude (or a substrate-natural ratio thereof). Mismatch on STRUCTURE-CONSTANT shape → bet fails B5; mismatch on which K-types appear in the product → bet fails B5+ at this vertex.

**Sharpness**: MEDIUM. The Hall product structure constants at v=2 are Mersenne-arithmetic-natural (Elie Toy 3588 territory), so the SHAPE of the structure constants will be computable. The MATCH to SM coupling magnitudes is scheme-dependent (Calibration #33 applies — likely IDENTIFIED-tier, not derived). But the QUALITATIVE structure (which K-types appear in the product) is forced.

**Execution path**: Elie's lane (Hall product computation) + Lyra's dictionary interpretation. Some weeks.

### Test T4 — Forbidden-particle test (look for ghosts)

**Target**: B3 (no-ghosts).

**Design**: enumerate ALL canonical basis elements at low K-types (say, all K-types with dim ≤ 20). For each, compute weight-derived quantum numbers. Check whether each has an SM counterpart. ANY canonical basis element with weight-derived quantum numbers NOT MATCHING any SM particle (e.g., a charge that isn't 0, ±1/3, ±2/3, ±1; or a chirality combination not in SM) → "ghost" → either prediction of an unobserved particle (interesting!) or falsifier of the bet (if observed-exclusion is firm).

**Sharpness**: HIGH for finding ghosts (clean enumeration). MEDIUM for the falsification value (depends on whether observed-exclusion is firm enough — SM is well-tested at low energies, so any low-K-type ghost should already have been observed if real).

**Execution path**: Elie's lane (enumerate canonical basis at low K-types) + Cal cold-read on the ghost dispositions. Days to weeks.

### Test T5 — Five-Absence falsifier propagation

**Target**: framework-wide (not just keystone, but the bet would help propagate).

**Design**: the substrate predicts NO 4th generation, NO sterile neutrinos, NO GUT, NO SUSY, NO monopoles, NO proton decay (per K65 Five-Absence Predictions Set). The keystone bet says these absences come from the canonical basis structure (no canonical basis elements at the relevant K-types). Each Five-Absence prediction is independently falsifiable by experiment. Observation of any → falsifier of substrate framework.

**Sharpness**: HIGH for the absence predictions; experimental timescales are decades (these are SM/BSM searches).

**Execution path**: standing experimental falsifiers; not Cal-actionable; just track.

## 3. Test priority + sequence

| Test | Sharpness | Execution | Priority |
|---|---|---|---|
| **T1 (count at lepton K-type)** | HIGH | hours-days (post-affine-pin) | **TOP** — execute first |
| T4 (forbidden particles / ghosts) | HIGH | days-weeks | second |
| T3 (cross-multiplication) | MEDIUM | weeks | third |
| T2 (gauge partition) | MEDIUM-HIGH | weeks (joint with bulk-color) | fourth |
| T5 (Five-Absence) | HIGH at observation, experimental timescale | decades | standing |

**T1 is the cleanest falsifier-test executable now**. The count at the lepton K-type should match 18 (or 24); if it doesn't, the bet falls cleanly. If it does, the bet survives this specific check (still doesn't prove other K-types).

## 4. Discipline framing

Per Cal #27 forward-derivation: these tests verify whether the keystone bet's PREDICTED canonical basis structure MATCHES the SM particle structure (a structural-correspondence test). If matches → bet survives (modulo independence of routes); if mismatches → bet falls (clean falsification).

Per Cal #29 question-shape: the tests target SPECIFIC sub-claims (B1-B5) — not "does the bet work?" (too diffuse) but "does the canonical basis dim at this K-type match the SM count?" (specific). Each test produces a forced YES/NO.

Per Cal #32 hard-constraint: the tests use STRUCTURAL CONSTRAINTS that the bet must satisfy (canonical basis dim formulas, weight-derived quantum-number consistency, Hall product structure). Not value-match (e.g., not matching specific coupling magnitudes — those are scheme-dependent IDENTIFIED tier).

Per Calibration #33: each test's input formulas (canonical basis dim, Hall structure constants, weight derivations) should be VERIFIED-CITED at execution time (Lusztig/Kashiwara for canonical basis dim; standard rep theory for weights; Ringel-Hall for Hall structure constants). "Scope is part of the value" — check the formulas cover the v=2 Hall-Littlewood corner specifically (the substrate's specialization point per Cal #155 A1 corrections).

## 5. What this proposal IS and ISN'T

**IS**: a Cal-side opening sketch of 5 sharp falsifier candidates for the keystone bet, with sharpness ratings + execution paths. Cal's design contribution to Saturday plan item 4.5.

**ISN'T**: a derivation or a result. The tests are designs; running them is Lyra (refines) + Elie (computes) + Cal (cold-reads results).

## 6. Routing

- **Lyra (joint with Cal per Keeper plan)**: refine the test designs; especially T1 (count test) — is the canonical basis dim formula at substrate specialization (v=2) computable cleanly, and is the comparison to 18 (SM) or 24 (Dirac) the right target?
- **Elie**: T1 (count) + T4 (ghosts) + T3 (cross-mult) are Lie/Hall computations in his lane.
- **Keeper**: tier-gate the test designs + the eventual results.
- **Grace**: T5 (Five-Absence) catalog-tracks experimental status.
- **Cal**: cold-read each test's results when executed; apply Calibration #33 sourcing + Cal #32 hard-constraint discipline.

— Cal A. Brate, Saturday 2026-05-30 ~09:21 EDT. Sharp falsifier-test design proposal v0.1 for the "K-types are the particles" keystone bet. 5 tests, sharpness-ranked; T1 (count at lepton K-type) is the cleanest executable-now falsifier. Cal-side opening contribution; Lyra refines + executes. The bet currently carries the whole static taxonomy DERIVED-modulo-keystone; a sharp focused test of it (not diffuse) is the highest-leverage falsifier-design Cal can offer.

---

## Addendum (Saturday 2026-05-30 ~09:30 EDT) — T1 target must be PINNED A-PRIORI (Keeper note absorbed)

Per Keeper's response: "the '18 vs 24' framing depends on how we count the SM-observable spinor count (per-generation? including handedness? CKM-correlated?) — the cleanest version pins those choices a-priori so the test can't be tuned post-hoc."

This is the Cal #29 question-shape discipline applied to the test design itself — and Keeper is right. A test where the comparison target is tunable post-hoc isn't a sharp falsifier; it's a back-fit opportunity. Refining T1:

**T1 — Count test at lepton K-type V_(1/2,1/2), PINNED a-priori**:

Before the canonical-basis-dim computation runs, the SM-side count must be fixed in writing with explicit choices on all degrees of freedom. Specifically:

**T1-pin (declare upfront, before computing)**:

| Choice | Option A (SM-observable) | Option B (full-Dirac substrate-natural) | Cal recommendation |
|---|---|---|---|
| Right-handed neutrinos? | NO (SM convention) | YES (Dirac partner, substrate-natural) | **B** — substrate has Dirac neutrinos (Paper 108 correction); ν_R is a substrate particle even if not observed in low-energy SM |
| Left/right chirality counted separately? | YES (2 per charged lepton × 1 for ν_L only) | YES (2 per charged + 2 per neutrino if Dirac) | **YES both** — chirality is a substrate-derived axis (L3); each chirality state is a distinct substrate particle |
| Antiparticles counted? | YES (counted as separate states) | YES | **YES** — particle/anti is a substrate-derived axis (engine v0.4 E/F); each antiparticle is a distinct substrate particle |
| Generations counted? | YES (3 generations × all of the above) | YES | **YES** — generation is indexed (open per #414) but counted |
| CKM-mixing-correlated? | NO (count in mass basis) | NO (count substrate-natural K-type basis) | **NO** — the K-type is the substrate identification; mixing across K-types is a separate dynamics question |

**Recommended T1-target (Cal lean)**: **Option B = 24** — 3 generations × (2 charged-lepton chiralities × 2 particle/anti + 2 neutrino chiralities × 2 particle/anti) = 3 × (4 + 4) = **24**. This matches Dirac-neutrino substrate-naturalness + counts every substrate-distinguished state.

Option A = 18 follows if (and only if) the SM "no ν_R observed" convention is the substrate-side truth — but that contradicts the substrate's Dirac-neutrino structure (per Paper 108). So Option B is the substrate-consistent target.

**T1-result interpretation (declared upfront)**:
- dim(canonical basis at V_(1/2,1/2)) = 24 → bet survives B1 at the lepton K-type
- dim = 18 → bet's substrate framework needs to explain why ν_R isn't in canonical basis (Dirac vs Majorana tension)
- dim = anything else → bet falls at B1 (the count is what it is; the framework can't tune to match)
- dim depends on representation choice / basis convention → recheck the QG computation (this is the Cal #32 / Calibration #33 sourcing check — pin to Lusztig/Kashiwara conventions a-priori)

**Why this matters (Cal #29 reflexive)**: with the count-target PINNED upfront, the test produces a forced YES/NO; without pinning, "the test passed" could quietly mean "we picked the SM-side count to match the canonical basis dim we got." Keeper's point catches the back-fit risk before it can land. Good cross-CI discipline.

**Updated T1 priority**: still TOP (sharpness HIGH; executable now after the affine pin); now with target = 24 declared a-priori; Calibration #33 source-pin Lusztig/Kashiwara canonical basis conventions before computing.

— Cal addendum, Saturday 2026-05-30 ~09:30 EDT, absorbing Keeper's "pin a-priori" note. T1 target = 24 (full Dirac with ν_R) declared upfront; the test now produces a forced YES/NO without post-hoc tuning. Cal #29 question-shape discipline applied to the test design itself.
