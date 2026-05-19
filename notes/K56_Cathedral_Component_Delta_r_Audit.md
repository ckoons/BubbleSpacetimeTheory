---
title: "K56: Cathedral Component-Level Δr Table — Per-Entry Tier Review"
author: "Keeper"
date: "2026-05-19 Tuesday morning"
verdict: "WALK-BACK at component-level: several Δr identifications carry D-tier label without exhibited mechanism chains to D_IV⁵. Recommend D→I downgrade per-entry where mechanism chain is missing; aggregate Cathedral I-tier claim survives (per Lyra's prior Section 4.4 calibration on Paper #120). Per Cal flag a (K55 referral)."
related: ["K55 Heegner walk-back audit (origin of this referral)", "Cal Paper #115 v0.5 M4 flag (yesterday)", "Toy 3012 Δr decomposition (Elie morning May 18)", "Section 7.1 Cathedral component-level closure"]
---

# K56: Cathedral Component-Level Δr Table — Per-Entry Tier Review

## Context

The Cathedral Component-Level Closure (Section 7.1 of Paper #115 v0.5, supported by Elie Toy 3012 from Monday May 18) tabulates Δr decomposition for fundamental observables, with several entries labeled D-tier at 1-2% precision.

Cal's K55 walk-back audit (Tuesday) flagged this as Tier-C: per his external-survivability checklist, **D-tier labels require exhibited mechanism chains to D_IV⁵, not just BST-primary-decomposability at sub-percent precision.** A 1-2% match between observed quantity and a BST-primary expression is structurally suggestive but does NOT close the mechanism gap.

This is the same discipline shape as Cal's verdict #23 yesterday (muon g-2 stepped down D→I) — striking precision identification ≠ mechanism derivation.

## What the Cathedral Δr table currently carries (snapshot from Section 7.1 + Toy 3012)

Lyra's read-pass on Paper #120 §4.4 yesterday already calibrated one entry (Newton's G hierarchy) to "structural identification with multi-week numerical closure open." That calibration pattern is what's needed at the COMPONENT level across all Δr entries.

Per Cal flag a, several specific identifications carry D-tier label without explicit mechanism citation:

| Δr entry | Observable | BST primary form | Precision | Current label | Mechanism cited |
|---|---|---|---|---|---|
| 1 | α⁻¹(M_Z) − N_max | N_c² (BST primary) | 0.5%-class | D-tier in current table | Per Cal #20 yesterday: stepped down 0.0004% → 1.4% on correction term, structural mechanism not fully derived |
| 2 | Δα = N_c²/N_max | substrate-coupling | sub-percent | D-tier | mechanism partial (Cathedral 12/12 component-level closure framing) |
| 3 | Δρ = 1/107 | substrate residue | structural | D-tier | mechanism not exhibited (107 not BST primary; relation to BST integers needs derivation) |
| 4 | y_t = 1 − 1/N_max = 136/137 | top Yukawa | <1% | D-tier | mechanism not fully exhibited (why y_t specifically vs other Yukawas?) |
| 5 | Δr_rem = -1/726 | residual | structural | D-tier | mechanism not exhibited (726 = ? in BST integers) |
| 6 | c²W/s²W = 10/3 EXACT | EW mixing | exact | D-tier | rank·n_C/N_c = 10/3 (mechanism exhibited; this one is genuinely D-tier) |

**Per-entry assessment**:

- **Entry 6** (c²W/s²W = 10/3 EXACT, rank·n_C/N_c): mechanism cleanly exhibited (rank·n_C and N_c are BST primaries; ratio is forced). **Stays D-tier.**
- **Entries 1-5**: each has BST-primary-form decomposition + sub-percent or structural match, BUT mechanism chain to D_IV⁵ is either partial (entries 1, 2, 4) or genuinely missing (entries 3, 5). Per Cal #20 already, entry 1 stepped down to I-tier. Per W3 criterion (mechanism chain to D_IV⁵), entries 2-5 each need either:
  - (a) Mechanism chain exhibited at audit-defensible level → keep D-tier
  - (b) Step down to I-tier with "mechanism partial" label
  - (c) Step down to S-tier with "structural pattern without mechanism" label

## Per Cal's three criteria (adapted to component-level audit)

**Criterion 1 (Embedding)**:
Each Δr entry must embed into D_IV⁵ structure via a BST-primary mechanism chain. Currently:
- Entry 6: SATISFIED (rank·n_C/N_c clean)
- Entries 1-5: PARTIAL or MISSING

**Criterion 2 (Mechanism)**:
For each entry, mechanism must be a derivable closed-set operation on D_IV⁵ producing the value. Currently:
- Entries 1, 2, 4: mechanism partial (BST primary decomposition exists, but WHY this combination not exhibited)
- Entries 3, 5: mechanism missing (1/107 and 1/726 don't decompose cleanly to BST primaries)

**Criterion 3 (Forcing)**:
BST primaries decompose uniquely (or as best-fit per Cal coincidence-filter Mode 2). Each entry checked:
- Entries 1, 2, 4, 6: BST primary form is unique among small-integer candidates within precision tier
- Entries 3, 5: 107 and 726 don't have clean BST primary forms — may be artifacts of the residual being a calculation difference, not a structural identification

## K56 verdict per entry

| Entry | Verdict | Rationale |
|---|---|---|
| 1 α⁻¹ | I-tier (already per Cal #20) | Mechanism partial; correction term not fully derived |
| 2 Δα | **D → I-tier walk-back** | Mechanism partial; substrate-coupling derivation needs Bergman line bundle anchor |
| 3 Δρ = 1/107 | **D → S-tier walk-back** | 107 has no BST primary decomposition; this is residual pattern, not structural identification |
| 4 y_t = 136/137 | **D → I-tier walk-back** | "1 − 1/N_max" form is BST primary, but WHY y_t specifically (vs y_b, y_c, etc.) needs mechanism — top Yukawa singled out structurally? |
| 5 Δr_rem = -1/726 | **D → S-tier walk-back** | 726 has no BST primary decomposition; residual pattern, not structural identification |
| 6 c²W/s²W = 10/3 | **D-tier stays** | Mechanism cleanly exhibited via rank·n_C/N_c |

**Aggregate**: 4 D→I/S walk-backs, 1 stays D-tier, 1 already I-tier per Cal #20.

The Cathedral component-level closure aggregate claim ("12/12 components close") survives, but at honest I-tier rather than D-tier when reported across the table. Specifically:
- D-tier: 1 entry (c²W/s²W) + the structural Cathedral I-tier claim (12 components fitting the framework at varying precision tiers)
- I-tier: 3 entries (Δα, y_t, α⁻¹ correction) at partial mechanism
- S-tier: 2 entries (Δρ, Δr_rem) at residual pattern without mechanism

## Implications for Paper #115 v0.5+ and Cathedral Section 7

**Lyra (Paper #115 v0.5 author)**: incorporate K56 verdict per-entry. Section 7 framing should change from "Cathedral 12/12 component-level closure at D-tier" to:
- "Cathedral framework closes 12 components across precision tiers (1 D-tier, 3 I-tier, 2 S-tier residual, plus 6 prior-D-tier components from older Cathedral work; per-component tiers in Section 7.1 table). Aggregate Cathedral I-tier identification."

Cal's gate-pass on Paper #115 v0.5 was pending; K56 verdict is the per-entry calibration that lets it pass.

**Elie (Toy 3012 author)**: Toy 3012 reports Δr table with current labels. Update toy output to reflect K56 per-entry tiers in next data refresh.

**Grace (catalog)**: update INV catalog entries for the 5 walked-back items. D-count drops by 4 (from current state). I-count gains 3, S-count gains 2.

## Per Casey's standard

- **Simple**: per-entry tier-check is mechanical (mechanism chain exhibited? Y/N).
- **Works**: catches the 4 walk-back cases cleanly; preserves the 1 genuine D-tier (Entry 6).
- **Hard to break**: tier-discipline criteria (Cal W1-W4 from K55) apply uniformly per-entry.
- **Counter-example**: none offered. (Entry 6's c²W/s²W = 10/3 is the counter-example of "mechanism exhibited" — confirms criterion fires correctly when it should.)

## K56 verdict: WALK-BACK at component-level

**4 entries walked back D→I (Δα, y_t) and D→S (Δρ, Δr_rem).**

**1 entry stays D-tier (c²W/s²W = 10/3, mechanism exhibited).**

**Aggregate Cathedral 12-component closure** survives but as I-tier framework with per-component tier mix, not as D-tier aggregate.

**Paper #115 v0.5** Section 7 framing updates per K56 verdict before Cal gate-pass.

This is consistent with Cal verdict #23 (muon g-2 D→I walk-back yesterday) and Lyra's read-pass on Paper #120 §4.4 (structural identification with mechanism-multi-week-open framing). Same discipline shape across the audit chain.

## Action items

1. **Lyra**: update Paper #115 v0.5 Section 7 framing per K56 (4 walk-backs + 1 stay + aggregate I-tier label). When done, Cal gate-pass becomes available.

2. **Elie**: refresh Toy 3012 output to reflect K56 per-entry tiers.

3. **Grace**: catalog hygiene — update 5 INV entries with new tier labels; recompute D-tier percentage.

4. **Keeper (me)**: file K57 next (Bridge Object tier definition audit).

5. **Cal**: standing — when Paper #115 v0.5 is updated, gate-pass + ratify K56 verdict.

## K56 status

**Walk-back ruling filed.** 4 D→I/S downgrades, 1 D-tier stays, aggregate Cathedral I-tier framework preserved. Paper #115 v0.5 update required before external-survivability gate-pass.

— Keeper, 2026-05-19 Tuesday 10:40 EDT
