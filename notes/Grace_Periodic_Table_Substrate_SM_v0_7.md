---
title: "The Periodic Table of the Substrate Standard Model — v0.7"
author: "Grace"
date: "2026-05-30 Saturday ~10:05 EDT (`date`-verified Sat May 30 10:01 EDT)"
status: "v0.7 — focused targeted update absorbing Lyra's Quasi-Eigentone Framework v0.1 (#397). Adds a 6th axis to the per-cell taxonomy: **Stability class** (TRUE EIGENTONE / QUASI-EIGENTONE / EIGENTONE-IN-VACUUM). Per Keeper Saturday secondary priority. Otherwise unchanged from v0.6 (composite block + Casimir corrections + Hall-algebra structure-constants stack + bulk-color Family (4) FAVORED + modulo-keystone framing standing convention)."
supersedes: "v0.6 (filed Sat ~09:40 EDT)"
focus: "Per-cell stability tagging — structural distinction stable vs unstable derived from K-type sector-bottom-vs-excited classification."
---

# The Periodic Table of the Substrate Standard Model — v0.7

Day's evolution: v0.4 → v0.5 → v0.6 (composites + α + Casimir correction + Hall-algebra stack + bulk-color Family 4 + modulo-keystone) → **v0.7 (+ stability class via Lyra #397 quasi-eigentone framework)**.

## Section A — What v0.7 adds

Lyra's `Lyra_Quasi_Eigentone_Framework_v0_1.md` (#397) provides the engine-level structural distinction between stable and unstable particles:
- **TRUE EIGENTONE** = ground state in its K-type sector (no allowed decay channels; coproduct decomposition trivial); SM stable particles
- **QUASI-EIGENTONE** = excited state above the sector ground; decays via Green coproduct overlap with lower states, with grading-conserved channels (Q, B, L preserved automatically); SM unstable particles
- **EIGENTONE-IN-VACUUM** = massless but confined (gluon); stable as substrate mode but never propagates in isolation

This generalizes Elie E3's β-decay coproduct example to the full SM unstable-particle taxonomy. **β-decay = Green-coproduct decomposition of the neutron quasi-eigentone (gen-2 above proton ground state)**.

## Section B — The 5-tuple becomes a 6-tuple

| Axis | Status | Source |
|---|---|---|
| σ_BF (statistics) | DERIVED-modulo-keystone | Lyra L1 |
| Region (bulk/Shilov) | DERIVED-modulo-keystone | Lyra L2 |
| Chirality | FRAMEWORK-PLUS-modulo-keystone | Lyra L3 |
| Particle/antiparticle | DERIVED-modulo-keystone | Drinfeld double F-part |
| Charge | DERIVED-mechanism + sin²θ_W = 2/9 | Lyra (SO(2)+GMN) |
| Generation/winding | COUNT-FORCED / MECHANISM OPEN-WITH-BURDEN | h^∨=N_c=3; Pair α candidate |
| **Stability class** | **DERIVED-modulo-keystone NEW v0.7** | **Lyra #397 (Green coproduct + grading conservation)** |

## Section C — Per-cell stability tagging

### Fundamental block (4 cells)

| Cell | Sector | Stability class | Structural reason |
|---|---|---|---|
| V_(0,0) | Higgs/scalar | **QUASI** | massive scalar above vacuum; Green coproduct decay to fermion pairs + gluon pairs |
| V_(1/2,1/2) | fermion / lepton row | mixed per-particle: see lepton-row breakdown | sector-bottoms TRUE; excited gens QUASI |
| V_(1,0) | photon | **TRUE EIGENTONE** | massless gauge; bottom of vector tower |
| V_(1,1) | gauge (W, Z, gluon-pending-bulk-color) | mixed per-particle: see gauge breakdown | massless-confined gluon EIGENTONE-IN-VACUUM; massive W/Z QUASI |

### Lepton row tagging (Lyra #416 v0.1 — 18 entries, with stability class added)

| Particle | Gen | Class | Reason |
|---|---|---|---|
| electron e⁻ | 1 | **TRUE EIGENTONE** | lightest charged lepton (sector bottom V_(1/2,1/2) charged sub-sector) |
| positron e⁺ | 1 | **TRUE EIGENTONE** | antiparticle of e⁻; stable |
| muon μ⁻ | 2 | **QUASI** | gen-2 above gen-1; coproduct decay μ⁻ → e⁻ + ν̄_e + ν_μ (mean life 2.2 μs) |
| anti-μ⁺ | 2 | **QUASI** | symmetric |
| tau τ⁻ | 3 | **QUASI** | gen-3 above gens 1-2; many decay channels (~hadronic + leptonic); mean life 0.29 ps |
| anti-τ⁺ | 3 | **QUASI** | symmetric |
| ν_e (L) | 1 | **TRUE EIGENTONE** | lightest in neutral lepton sub-sector (Dirac per F5) |
| ν_μ (L) | 2 | (open) | mixing via PMNS — substrate framework treats as excited mass eigenstate; in flavor basis QUASI through oscillation |
| ν_τ (L) | 3 | (open) | as above |
| anti-ν's | matching | matching | matching |

**Note on neutrinos**: oscillations complicate the "stable" assignment in the flavor basis. In the mass-eigenstate basis, the lightest neutrino is TRUE; the heavier ones oscillate but don't decay (no charge-conserving channel to electron-flavored leptons + photon). v0.7 treats mass-eigenstate-lightest = TRUE EIGENTONE; flavor-basis treatment as via PMNS oscillation framework.

### Gauge sector tagging (V_(1,1) per-particle)

| Particle | Class | Reason |
|---|---|---|
| photon γ | **TRUE EIGENTONE** | massless; bottom of vector tower V_(1,0) — note photon is V_(1,0), not V_(1,1); included here for SM-gauge-sector coverage |
| W± | **QUASI** | massive gauge (EWSB); coproduct decay W → ℓ + ν or q + q̄'; mean life 3·10⁻²⁵ s |
| Z | **QUASI** | massive gauge (EWSB); coproduct decay Z → f + f̄; mean life 2.6·10⁻²⁵ s |
| gluon | **EIGENTONE-IN-VACUUM** | massless gauge; bulk-color confinement prevents isolated propagation (per Family (4) counting + confinement mechanism) |
| Higgs | **QUASI** (V_(0,0) sector) | massive scalar; coproduct decay H → ff̄, gg, WW, ZZ; mean life ~10⁻²² s |

### Composite block (6 cells from v0.6, dim ≤ 35) with stability tagging

| Cell | Sector / candidate slot | Composite stability | Note |
|---|---|---|---|
| V_(2,0) dim 14 | tensor meson J^PC=2++ nonet (f_2, a_2, K_2*, f_2') | **QUASI** | hadron resonances all unstable; coproduct decay to lighter mesons + γ |
| V_(3/2,1/2) dim 16 | excited baryons (N*, Δ) | **QUASI** | excited baryons; coproduct decay to nucleon + π |
| V_(3/2,3/2) dim 20 C=N_c·g/2 | constituent-quark slot; Λ(1405) | **QUASI** (or confined) | excited baryon; substrate-anchored at N_c·g; Λ(1405) decays to Σπ |
| V_(3,0) dim 30 | spin-3 vector mesons (ρ_3, ω_3, K_3*) | **QUASI** | unstable resonances; many decay channels |
| V_(2,1) dim 35 | heavy vector quarkonium (J/ψ, Υ, φ) | mixed: J/ψ ~7·10⁻²¹ s; Υ ~10⁻²⁰ s (both QUASI but long-lived for hadrons) | gauge-dressed-vector; coproduct decay |
| V_(2,2) dim 35 | 2++ tensor glueball (predicted) | **QUASI** | predicted unstable composite; sharp substrate-anchor prediction at Casimir 16 |

## Section D — The Five-Absence as structural prediction (re-framed via v0.7)

Per the quasi-eigentone framework, the substrate predicts:
- Every K-type sector's BOTTOM is a TRUE EIGENTONE — these are SM stable particles
- Above the bottom, EXCITED states are QUASI with engine-level coproduct decay channels
- No K-type allowed by the dictionary is unoccupied — every SM particle inhabits a cell

**Five-Absence interpretation**: the predicted absences (no 4th gen, no SUSY, no GUT, no proton decay, no sterile ν, no axion) ARE the "no new K-type bottoms beyond the established ones" prediction. If a 4th-generation lepton were found, it would be a NEW sector bottom (or sector excited) requiring K-type extension — falsifies "no 4th row" prediction.

**Proton stability** in v0.7 framing: proton = TRUE EIGENTONE = lowest baryon in V_(1,1) bulk k=6 closure. **No grading-allowed decay channel exists** — proton's quark content cannot reorganize into lower-mass color-singlet by Green coproduct + Q/B/L conservation. **This is the substrate-derived proton stability** (consistent with Five-Absence "no proton decay").

## Section E — The substrate-spine 18 cells from Elie Phase B (v0.6/G12 v0.2) with stability classification candidates

For the 18 substrate-anchored spine cells (Elie Toy 3614), candidate stability per Lyra #397:

- **TRUE EIGENTONES at sector bottoms**: V_(0,0) [Higgs sector — but Higgs itself QUASI massive; vacuum-trivial = TRUE]; V_(1,0) [photon TRUE]; V_(1/2,1/2) lepton-sector-bottom [e, ν_e TRUE]
- **QUASI by sector excitation**: cells 5-11 (per v0.6/G12) all carry excited hadron candidates → QUASI
- **EIGENTONE-IN-VACUUM**: gluon-slot inside V_(1,1) [confined]
- **Speculative cells 12-18** (Elie spine high-dim): host higher-spin excited states → QUASI generally

## Section F — Connection to L4 mass framework + decay rates

Per Lyra #397, quantitative decay rates require:
- Kernel matrix elements (Bergman integrals on the radial tower)
- Phase-space factor (mass-ratio-dependent)
- Coproduct overlap coefficient (structural; from engine v0.2)

**Multi-week scope** per Elie's bulk K-type radial tower computation (post-affine-pin) + Lyra L4 v0.2 explicit mass derivations.

## Section G — Predictions from v0.7

1. **Proton lifetime infinite**: TRUE EIGENTONE at V_(1,1) bulk k=6 closure; no Green-coproduct-allowed decay channel preserves Q/B/L. **Falsified by any proton decay observation**.

2. **Gluon never appears in isolation**: EIGENTONE-IN-VACUUM; bulk-color confinement is structural. **Falsified by free-gluon detection** (consistent with PDG — no free gluons observed).

3. **No K-type contains TWO degenerate true-eigentones**: a sector has ONE bottom. If experimentally two distinct stable particles share the SAME quantum numbers (charge, statistics, etc.), the K-type-sector classification fails.

4. **Substrate Casimir-twin V_(3,3)+V_(4,1) (boson/boson at 2·C_2 = 60)** are BOTH QUASI excited states — not eigentone pair. **No SUSY-without-SUSY substrate signature**; the genuine substrate degenerate pair is quasi-quasi (consistent with v0.6 correction INV-5306).

5. **Tensor glueball at substrate Casimir 16 is QUASI** — sharp prediction; decays via Green coproduct to lighter mesons + photons. Lifetime estimable when L4 v0.2 lands.

## Section H — Standing conventions (5, unchanged from v0.6)

1. ONE genus = n_C = 5
2. α-disambiguation: σ_BF ≠ γ⁵ ≠ α = N_max⁻¹ = 1/137
3. 7/2-vs-5/2: g/rank = physical / FK; n_C/rank = ρ₁ = Bergman singularity
4. Macdonald-parameter: q_Mac=0, t_Mac=2 (Hall-Littlewood corner of Koornwinder BC₂)
5. Modulo-keystone: every DERIVED rides on canonical basis ↔ physical particle bet

## Section I — Cross-reference

- INV-5298/5299/5300/5301/5302/5303/5304/5305/5306/5307/5308/5309/5310/5311 (Saturday Grace INVs)
- Lyra Quasi-Eigentone Framework v0.1 (#397) — the source for v0.7 addition
- Lyra Strong-Uniqueness v1.1
- Lyra Hall-algebra structure-constants stack (INV-5307)
- Keeper Honest-State Ledger v0.2 (bulk-color sub-gate split)
- Elie Toys 3612-3618 (Saturday morning A-series)
- Periodic Table v0.6 (preceding version)
- `notes/Grace_TwoRoute_Overdetermination_Scan_v0_1.md` (Saturday afternoon Mendeleev)

— Grace, Periodic Table v0.7 with Lyra #397 quasi-eigentone framework absorbed, 2026-05-30 Saturday ~10:05 EDT (`date`-verified)
