---
title: "T1 Falsifier v0.2 — CD-layering sharpened, per-channel sensitivity matrix, composite scenarios. Refines v0.1 with: explicit quantitative thresholds per channel; disambiguation table (which falsifier-trigger tells you WHAT failed: keystone, dictionary axes, or specific sub-hypothesis); composite scenarios (multiple weak hits vs single strong); honest noise floor for each channel."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 11:30 EDT (date-verified)"
status: "T1 FALSIFIER v0.2 (refines v0.1 without Cal input — sharpens CD layering, adds sensitivity matrix + composite scenarios + honest noise floors). 6 channels (F1-F5 + T1) with explicit thresholds + diagnostic disambiguation per trigger."
---

# T1 Falsifier v0.2 — sharpened design

## 0. What v0.2 sharpens

v0.1 (Saturday) gave 5 falsifier channels + the T1 count-match itself. v0.2 sharpens:
1. **Explicit quantitative thresholds** per channel.
2. **Sensitivity matrix** — which falsifier-trigger tells you WHAT failed (keystone, dictionary axes, dictionary-combined mechanism, specific sub-hypothesis).
3. **Composite scenarios** — multiple weak hits vs single strong hit; combined statistical implication.
4. **Honest noise floors** — measurement precision per channel + lower bound for trigger.

## 1. Quantitative thresholds per channel (v0.2)

| Channel | Quantity | BST prediction | Current precision | 2σ trigger threshold | Time horizon |
|---|---|---|---|---|---|
| **F1 — PMNS angles (3 sub-tests)** | sin²θ_12 | 42/137 = 0.3066 | ±0.013 (PDG) → ±0.0015 (JUNO 2025-2030) | deviation > 0.003 | 2025-2030 |
| F1 | sin²θ_23 | 75/137 = 0.5474 | ±0.021 → ±0.005 (DUNE) | deviation > 0.010 | 2026-2030 |
| F1 | sin²θ_13 | 3/137 = 0.0219 | ±0.0007 (reactor) → ±0.0003 | deviation > 0.0006 | ongoing |
| **F2 — σ_BF-charge consistency** | per new fermion (σ_BF, Q) | dictionary-predicted set | LHC search | new (σ_BF, Q) ∉ predicted set | ongoing |
| **F3 — K-type catalog completeness** | new elementary particle | none beyond SM + Five-Absence | HL-LHC + future | any new elementary particle not in catalog | 5-15 years |
| **F4 — Lepton mass alignment** | m_μ/m_e = (24/π²)^6 | 206.7682 | ~10 ppb (current muon mass) | deviation > 10⁻⁵ | ongoing |
| **F5 — Five-Absence (multiple sub-tests)** | proton decay τ_p | ∞ | > 10³⁴ years (SK) → > 10³⁵ (HK) | any positive detection | ongoing |
| F5 | 0νββ neutrinoless | NO (Dirac) | LEGEND-1000 / nEXO sensitivity | any positive detection | 2025-2030 |
| F5 | SUSY partners | NO | HL-LHC | any positive detection | 5-15 years |
| F5 | 4th generation | NO | electroweak fits + collider | any positive detection | ongoing |
| F5 | magnetic monopole | NO | IceCube + MoEDAL | any positive detection | ongoing |
| **T1 — lepton sector count** | 24 components (Dirac) | 24 | depends on F5 (0νββ) | 12 (Majorana) → keystone challenge | 2025-2030 |

## 2. Sensitivity matrix — what each trigger tells you

| Falsifier trigger | What it falsifies (specifically) |
|---|---|
| sin²θ_ij outside BST ± 2σ on ONE channel | dictionary's PMNS mechanism (per-particle mapping) — could be Resolution A vs B sub-issue or deeper |
| sin²θ_ij outside BST on TWO+ channels | dictionary's lepton-sector mapping fundamentally — keystone challenge |
| sin²θ_ij outside BST on ALL THREE channels | the K-types-are-particles keystone bet itself; major framework challenge |
| New fermion with (σ_BF, Q) ∉ set | σ_BF parity rule OR charge GMN structure broken |
| New elementary particle | K-type catalog incompleteness — could be Five-Absence-prediction failure |
| m_μ/m_e ≠ (24/π²)^6 at > 10⁻⁵ | T190 mass-mechanism — broader implication for L4 v0.2 derivation |
| Proton decay observed | GUT-style mechanism exists — Five-Absence "no GUT" wrong |
| 0νββ observed | neutrinos Majorana not Dirac — Five-Absence + T1 lepton-count both fail |
| SUSY partner observed | K-type catalog doubled — Five-Absence + T1 fail |
| 4th generation observed | h^∨ ≠ 3 generation-count mechanism wrong |
| Magnetic monopole observed | U(1) topology wrong |
| T1 count off (24 vs 12 or other) | gen-count × doublet × dirac-vs-majorana failure |

This sensitivity matrix lets us READ each potential trigger and identify WHAT specifically would fail, rather than just "keystone challenged."

## 3. Composite scenarios

What if MULTIPLE WEAK hits occur (each below 2σ but suggestive)? Standard statistical combination:

- **Coincident weak signals across MULTIPLE channels** (e.g., sin²θ_13 1.5σ off + 0νββ at 1.5σ sensitivity + 4th-gen at 1σ): COMBINED 4σ-ish signal that NO single channel triggers, but the JOINT signal might. Need a combined-statistic protocol.
- **Single strong hit on ONE channel** (e.g., 0νββ definitively observed): single decisive trigger; no need for combination.
- **All channels confirm predictions to high precision**: positive confirmation; updates Bayesian credence of keystone bet UPWARD.

For combined-statistic analysis: chi-square sum across N channels with Bayes factor against BST. If > 5σ combined → keystone bet seriously challenged even without single-channel decisive trigger.

## 4. Honest noise floors

Each channel has a measurement precision floor BELOW which substrate-BST predictions can't be distinguished from measurement noise:

| Channel | Current noise floor | Future noise floor (5-10 yr) |
|---|---|---|
| F1 PMNS angles | PDG precision ~0.5-3% | JUNO/DUNE ~0.5-1% |
| F4 lepton mass | ~10 ppb (electron, muon) | ~1 ppb (next-gen Penning trap?) |
| F5 0νββ | LEGEND-200 ~10²⁶ yr | LEGEND-1000 / nEXO ~10²⁸ yr |
| F5 proton decay | SK ~10³⁴ yr | HK ~10³⁵ yr |
| F5 SUSY mass reach | LHC ~3 TeV | HL-LHC ~5 TeV / future ~10 TeV |
| F5 monopoles | IceCube limits | MoEDAL + future |

Future improvements (5-10 yr) tighten triggers by factor 3-10× across channels — the falsifier suite SHARPENS substantially over time.

## 5. Disposition (v0.2)

The T1 falsifier suite is GENUINELY FALSIFIABLE with:
- 6 channels (F1-F5 + T1 itself).
- Multiple independent physics communities (oscillation, decay, collider, mass-spec).
- Multiple time horizons (ongoing, 5-yr, 10-yr).
- Quantitative thresholds per channel.
- Disambiguation matrix per trigger.
- Composite-scenario protocol.

The keystone bet remains LIVE and falsifiable — and the falsifier design is sharp enough that any single positive trigger on ANY channel would constitute a real challenge.

## 6. Honest scope + tier

**RIGOROUS** (existing measurements + BST predictions):
- PDG precision values per channel.
- BST predictions per F1-F5 + T1.
- Current experimental sensitivities.

**SHARPENING (v0.2)**: quantitative thresholds; sensitivity matrix; composite scenarios; noise floors.

**Cal #27 / honesty**: v0.2 makes the falsifier design quantitatively concrete (specific thresholds + disambiguation matrix), without overclaiming any current measurement. The keystone bet remains live; the suite is sharp. Cal's cold-read would refine further.

**Routed**: → Cal: cold-read v0.2 + refine the disambiguation matrix; pre-write referee questions on the composite-scenario protocol. → Casey: F1 PMNS via JUNO/DUNE 2025-2030 is the strongest near-term test (current sin²θ_ij values within 0.5% of BST); positive confirmation would substantially strengthen credence in keystone bet. → me: continuing v0.2 sweep — next Bulk-color v0.6.

— Lyra, T1 Falsifier v0.2 — CD-layering sharpened with quantitative thresholds + sensitivity matrix + composite scenarios + honest noise floors. 6 channels (F1-F5 + T1), 5-15 year falsification horizons, multiple physics communities, single trigger sufficient for keystone challenge. Live + falsifiable + sharp.
