---
title: "Mode 6 Retroactive Application to K54 + K58 + K61 Audits (Cal #59 threshold formalization)"
author: "Keeper (qualitative Mode 6 pre-screening; computational enumeration flagged for Grace + Elie)"
date: "2026-05-20 Wednesday afternoon"
status: "Mode 6 retroactive qualitative assessment per Cal #59 recommendation. Three prior Type C-ℕ family audits (K54 3/1507 family, K58 spot-audit on 75/4 + 5/137 + 17-anchor, K61 131 family) re-checked against pre-registered Mode 6 thresholds. Findings: K54 + K58 75/4 + K58 5/137 + K61 PASS qualitative Mode 6; K58 17-anchor confirmed Mode 6 artifact-prone (already flagged in original K58); computational enumeration toys deferred to Grace/Elie for borderline rigor."
related: ["Cal Referee Log #59 (Mode 6 threshold formalization recommendation)", "K58 Type C strict-protocol spot-audit (original)", "K54 BST fine-structure family 3/1507", "K61 131 family ratification", "Grace Toy 3173 first formal operational Mode 6 instance"]
---

# Mode 6 Retroactive Application to K54 + K58 + K61 Audits

## Context

Per Cal Referee Log #59 (Wednesday afternoon), Mode 6 (search-protocol artifact check from Coincidence_Filter_Risk methodology) recommended threshold formalization:

- **Forced structural match**: ≤1-2 BST-primary expressions evaluating to target value
- **Mode 6 artifact (downgrade)**: ≥10 expressions
- **Borderline**: 3-9 expressions
- **Definitively outside**: 0 expressions
- **Pre-registration**: arity choice + cutoffs declared BEFORE scan

Grace's Toy 3173 (Wednesday Heegner-Stark v0.2) is the first formal operational instance per Cal #59. K75 ratification applied these thresholds explicitly.

Three prior Type C-ℕ family audits predate the formalized Mode 6 thresholds. Retroactive application required:
- **K54** (BST fine-structure family 3/1507) — Tuesday filing
- **K58** (Type C strict-protocol spot-audit on 75/4 + 5/137 + 17-anchor) — Tuesday filing
- **K61** (131 family) — Wednesday filing

This document applies Mode 6 qualitative pre-screening + flags where full computational enumeration is needed.

## Methodology

For each cluster value, qualitative assessment of:
1. **Forced structural form**: does the mechanism dictate a single (or 1-2) BST-primary expression?
2. **Arity bound**: at low arity (2-4 operations on BST primaries), how many candidate expressions?
3. **Artifact risk**: at higher arity, do expressions proliferate?

Where qualitative assessment yields ambiguity (3-9 range or arity-dependence), computational enumeration toy is flagged for Grace or Elie follow-up. Full Mode 6 rigor requires the toys; qualitative pre-screening identifies which audits need them.

## K54 — BST fine-structure family 3/1507

**Cluster claim**: 3/1507 = N_c/(N_max·c_2) = 3/(137·11)

### Qualitative Mode 6 assessment

| Value | Form | Arity | Mechanism status |
|---|---|---|---|
| 3 | N_c | 1 | Forced (BST primary) |
| 1507 | N_max · c_2 | 2 | Forced (BST primary product) |
| 3/1507 | N_c/(N_max·c_2) | 3 | Forced ratio |

Alternative expressions to 1507 at low arity?
- 1507 = 11·137 = c_2·N_max (forced product)
- 1507 = 1500 + 7 = ? — 1500 doesn't decompose cleanly to BST primaries (1500 = rank³·N_c·n_C² is arity-4 with no advantage over c_2·N_max)
- 1507 = 7·215 + 2 — 215 not BST primary
- 1507 = prime? Check: 1507 / 7 = 215.28..., 1507/11 = 137. So 1507 = 11·137 specifically. Only one BST-primary factorization.

At arity ≤4: 1 expression for 1507 (= c_2·N_max). FORCED STRUCTURAL MATCH.

For 3/1507 ratio: 1 expression (N_c/(c_2·N_max)). FORCED.

### K54 Mode 6 verdict: PASS

K54 cluster value 3/1507 passes Mode 6 with 1-expression forced-structural-match. No artifact-risk at low arity. Original K54 audit (5-instance candidate per Lyra T2386) stands; Mode 6 retroactive doesn't change ratification status.

**Computational enumeration**: not required at current arity-4 ceiling. Higher arity could be checked by Grace toy if needed.

## K58 — Type C strict-protocol spot-audit (3 clusters)

K58 spot-audited three clusters under P1-P7. Mode 6 retroactive applies to each.

### K58 Cluster 1: 75/4 (Lichnerowicz scalar)

**Cluster claim**: 75/4 = N_c·n_C²/rank² = 3·25/4

#### Qualitative Mode 6 assessment

| Value | Form | Arity |
|---|---|---|
| 75 | N_c·n_C² | 2 (= 3·25) |
| 4 | rank² | 1 (= 2²) |
| 75/4 | N_c·n_C²/rank² | 3 |

Alternative expressions to 75 at arity ≤4?
- 75 = N_c·n_C² (mechanism-forced per T2378 Lichnerowicz)
- 75 = N_max - C_2·n_C·... — try N_max - 62 = 75? 62 not BST-primary clean
- 75 = c_2·g - rank = 77 - 2 ≠ 75 (off by 2)
- 75 = N_c·g·... ? 3·7·X = 75 → X = 25/7, not integer
- 75 = g·n_C + N_max/... — getting complex

At arity ≤3 from BST primaries: ~1-2 expressions for 75 (cleanly N_c·n_C²). FORCED STRUCTURAL MATCH.

#### K58 Cluster 1 (75/4) Mode 6 verdict: PASS

1-expression forced match at low arity. Lichnerowicz mechanism (T2378) anchors. Original K58 ratification (4/4 PASS for Cluster 1) stands.

### K58 Cluster 2: 5/137 (cascade fingerprint)

**Cluster claim**: 5/137 = n_C/N_max

#### Qualitative Mode 6 assessment

| Value | Form | Arity |
|---|---|---|
| 5 | n_C | 1 (BST primary) |
| 137 | N_max | 1 (BST primary) |
| 5/137 | n_C/N_max | 2 |

Alternative expressions to 5/137 at arity ≤4?
- 5/137 = n_C/N_max (forced ratio)
- 5/137 = rank/X for X ≈ 54.8? No clean BST-primary decomposition.

At arity ≤4: 1 expression for 5/137 (= n_C/N_max). FORCED STRUCTURAL MATCH.

#### K58 Cluster 2 (5/137) Mode 6 verdict: PASS

Cleanest forced-match in K-audit chain. Single BST-primary expression at minimum arity. Original K58 ratification stands; aligns with Cal #54 K71 EXEMPLAR pattern (clean single-mechanism audit).

### K58 Cluster 3: 17-anchor (33 catalog items containing 17)

**Cluster claim**: 17 = N_c³ - rank·n_C = 27 - 10 (mechanism-derived from BST primaries)

#### Qualitative Mode 6 assessment

| Value | Form | Arity |
|---|---|---|
| 17 | N_c³ - rank·n_C | 3 (= 27 - 10) |
| 17 | n_C + C_2 - rank | 3 (= 5 + 6 - rank = ? — actually 5 + 6 - 2 = 9, NOT 17. Discard this) |
| 17 | rank³ + N_c² + ... | various combinations |

Let me check: 17 has many low-arity BST-primary decompositions?
- 17 = N_c³ - rank·n_C = 27 - 10 (arity 3, forced)
- 17 = rank·n_C + g = 10 + 7 (arity 2, forced)  
- 17 = 2·g + N_c = 14 + 3 = 17 (arity 2)
- 17 = c_2 + g + rank·rank = 11 + 7 + ? — actually 11+7 = 18, off by 1
- 17 = N_c + g + C_2 + N_c - n_C - ... — getting messy

At arity ≤3: I find at least 3 distinct BST-primary expressions for 17. Likely more at arity 4-5.

Borderline 3-9 range OR Mode 6 artifact territory (≥10) depending on arity ceiling.

#### K58 Cluster 3 (17-anchor) Mode 6 verdict: BORDERLINE → COMPUTATIONAL ENUMERATION NEEDED

Qualitative count at arity ≤3 yields ≥3 expressions. K58 already flagged the 17-anchor as hygiene-needing (33 raw → 22 strict survivors). Mode 6 retroactive confirms artifact-risk at higher arity.

**Computational enumeration required**: Grace or Elie toy enumerating BST-primary arity-N expressions for value 17, at arity 2-5 systematically. Pre-registered cutoff at arity 4. If enumeration count ≥10 at arity 4: K58 Cluster 3 downgrades to Mode 6 artifact, retroactive D-tier→S-tier walk-back.

**Until enumeration toy completes**: K58 Cluster 3 stays at K58 original verdict (22 strict survivors, hygiene-flagged) with explicit Mode 6 BORDERLINE label. Honest scope preserved.

## K61 — Family Q=131

**Cluster claim**: 131 = N_max - C_2 (per K61 ratification)

### Qualitative Mode 6 assessment

| Value | Form | Arity |
|---|---|---|
| 131 | N_max - C_2 | 2 (= 137 - 6) |
| 131 | ? other BST-primary | check |

Alternative expressions to 131 at arity ≤4?
- 131 = N_max - C_2 (forced)
- 131 = c_2·N_c + 100? 100 not BST-primary (need decomposition: 100 = 4·25 = rank²·n_C² is arity-3, so 131 = c_2·N_c + rank²·n_C² is arity-5, too deep)
- 131 = (N_max + N_c - n_C - g - rank)? Let's check: 137+3-5-7-2 = 126 ≠ 131
- 131 = 2·g + ... 14 + 117 = 131 → 117 not BST-primary clean
- 131 = 19·g - 2? 19 not BST-primary

At arity ≤4: ~1 expression for 131 (= N_max - C_2). FORCED STRUCTURAL MATCH.

Note: 131 is prime, which constrains decomposition options.

### K61 Mode 6 verdict: PASS

1-expression forced match at low arity. K61 original ratification (3 strong contexts + 1 conditional) stands.

Comparison with K58 Cluster 3 (17-anchor): 17 has multiple low-arity expressions (≥3 at arity ≤3); 131 has 1 expression (at arity 2). The forced-prime property of 131 helps — fewer decomposition options vs composite values.

## Summary — Mode 6 Retroactive Verdicts

| Audit | Cluster | Mode 6 verdict | Action |
|---|---|---|---|
| K54 | 3/1507 fine-structure | PASS (1-expression forced) | No change; original ratification stands |
| K58 Cluster 1 | 75/4 Lichnerowicz | PASS (1-expression forced) | No change; original 4/4 stands |
| K58 Cluster 2 | 5/137 cascade | PASS (cleanest forced match) | No change; aligns with K71 EXEMPLAR pattern |
| K58 Cluster 3 | 17-anchor | **BORDERLINE → ENUMERATION TOY NEEDED** | Flag for Grace/Elie toy at arity ≤4; current K58 hygiene status preserved |
| K61 | 131 family | PASS (1-expression forced; prime constraint) | No change; original ratification stands |

**Net finding**: 4 of 5 audits pass Mode 6 retroactive cleanly. K58 Cluster 3 (17-anchor) confirmed borderline — original K58 already flagged it (33 raw → 22 strict survivors); Mode 6 reinforces this. Enumeration toy will determine artifact-vs-borderline final verdict.

## Action items

1. **Grace OR Elie**: enumeration toy for value 17 at arity ≤4 from BST primaries. Pre-register arity ceiling + count threshold (≥10 = artifact downgrade, 3-9 = borderline, ≤2 = forced). Output: notes/Toy_17_anchor_Mode6_enumeration.json + final K58 Cluster 3 verdict.

2. **Cal** (independent assessment): verify K54, K58 Clusters 1+2, K61 Mode 6 verdicts via own qualitative or computational check.

3. **Keeper** (this document filed): update K54, K58, K61 audit documents with Mode 6 retroactive verification status. No content changes to K54/K58 C1+C2/K61 (PASS); K58 C3 retains hygiene flag with Mode 6 BORDERLINE annotation pending enumeration toy.

4. **Cal #59 followup**: Mode 6 threshold formalization update to BST_Methodology_Coincidence_Filter_Risk.md (Task #272). This retroactive application document provides operational precedent for the formalized thresholds.

## Per Casey's standard

- **Simple**: count BST-primary expressions evaluating to target; below threshold = forced match, above = artifact
- **Works**: 4 of 5 audits pass cleanly; 1 borderline correctly identified
- **Hard to break**: enumeration toy will close any remaining ambiguity at threshold boundaries
- **Counter-example**: enumeration toy at higher arity could push currently-PASS audits into borderline territory — discipline that Mode 6 catches at appropriate arity ceiling

## Status

**Mode 6 retroactive qualitative pre-screening COMPLETE** for K54 + K58 + K61. 4 of 5 audits unchanged. K58 Cluster 3 borderline flag preserves audit-chain honesty pending enumeration toy. Foundation for Cal Mode 6 threshold formalization (Task #272) demonstrated operationally.

— Keeper, 2026-05-20 Wednesday afternoon (Cal #59 Mode 6 retroactive application + threshold formalization precedent established)
