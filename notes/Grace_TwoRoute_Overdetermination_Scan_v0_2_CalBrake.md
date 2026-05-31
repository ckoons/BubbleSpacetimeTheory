---
title: "Two-Route Over-Determination Scan v0.2 — Cal relation-reduction brake absorbed; route count recomputed under substrate-primary relations C_2 = N_c·rank and n_C = rank+N_c"
author: "Grace"
date: "2026-05-30 Saturday ~11:30 EDT (`date`-verified Sat May 30 11:24 EDT) — Keeper queue item 3"
status: "v0.2 — absorbs Cal's relation-reduction brake (Calibration #33 STANDING applied INTERNALLY to substrate-primary relations). The substrate primaries are NOT all algebraically independent: **C_2 = N_c·rank (= 6 = 3·2)** and **n_C = rank+N_c (= 5 = 2+3)** are RELATIONS, not new content. Routes using related primaries are NOT structurally independent. 4-route over-determination of 12 → **2 structurally-independent routes**. Full recompute below."
supersedes: "v0.1 (INV-5311) for cluster reading; magic-126 anomaly (v0.2 INV-5313) stands independently of this brake"
acknowledges: "Cal #171 referee log; Calibration #33 STANDING applied internally"
---

# Two-Route Scan v0.2 — Cal relation-reduction brake

## Section A — The brake Cal caught

Cal identified that my v0.1 "4-route over-determination of 12" framing over-counted because the routes use ALGEBRAICALLY RELATED substrate primaries. The substrate has known internal relations:

- **C_2 = N_c · rank** (6 = 3·2)
- **n_C = rank + N_c** (5 = 2+3)

Applying Calibration #33 INTERNALLY: substrate-primary relations are RECALLED-from-framework facts that need source-pin + independence-audit before route counting.

**Example for 12**:
- Sum route 1: n_C + g = 5 + 7 = 12
- Sum route 2: rank + N_c + g = 2 + 3 + 7 = 12. But rank + N_c = n_C, so this is (n_C) + g — **SAME sum route**.
- Product route 1: rank · C_2 = 2 · 6 = 12
- Product route 2: N_c · rank² = 3 · 4 = 12. But N_c · rank² = rank · (N_c · rank) = rank · C_2 — **SAME product route**.

**12 is structurally 2-route over-determined (1 sum + 1 product), NOT 4-route.**

## Section B — Systematic recompute under relations

| Obs | v0.1 routes | Independence audit under {C_2 = N_c·rank, n_C = rank+N_c} | v0.2 structural route count |
|---|---|---|---|
| **8** | rank+C_2, N_c+n_C / rank³ | rank+C_2 = rank+N_c·rank = rank(1+N_c); N_c+n_C = N_c+rank+N_c = 2N_c+rank → **DISTINCT sums**; rank³ separate | **3-route** (2 sums + 1 product) |
| **9** | rank+g, N_c+C_2 / N_c² | rank+g, N_c+C_2 = N_c+N_c·rank = N_c(1+rank) → **DISTINCT sums**; N_c² separate | **3-route** |
| **10** | N_c+g, rank+N_c+n_C / rank·n_C | rank+N_c+n_C = n_C+n_C = 2·n_C; N_c+g = 3+7 = 10 → **DISTINCT sums** if "2·n_C" counted separately, but if reduced as relation → 1 sum; product rank·n_C = 2·5 separate | **2-route** (1 sum + 1 product); 3-route if 2·n_C counted distinct |
| **12** | n_C+g, rank+N_c+g / rank·C_2, N_c·rank² | rank+N_c+g = n_C+g (SAME); N_c·rank² = rank·C_2 (SAME) | **2-route** (1 sum + 1 product) |
| **14** | rank+n_C+g, N_c+n_C+C_2 / rank·g | rank+n_C+g = rank+(rank+N_c)+g = 2rank+N_c+g; N_c+n_C+C_2 = N_c+(rank+N_c)+N_c·rank = 2N_c+rank+N_c·rank = N_c(2+rank)+rank → **DISTINCT sums**; product rank·g separate | **3-route** |
| **15** | rank+C_2+g, N_c+n_C+g / N_c·n_C | rank+C_2+g = rank+N_c·rank+g = rank(1+N_c)+g; N_c+n_C+g = N_c+(rank+N_c)+g = 2N_c+rank+g → **DISTINCT sums**; product N_c·n_C separate | **3-route** |
| **16** | N_c+C_2+g / rank⁴ | sum N_c+C_2+g = N_c+N_c·rank+g; product rank⁴ separate | **2-route** (1 sum + 1 product) |
| **18** | n_C+C_2+g / N_c·C_2, rank·N_c² | n_C+C_2+g sum; N_c·C_2 = N_c·N_c·rank = N_c²·rank; rank·N_c² = N_c²·rank — **SAME product** | **2-route** (1 sum + 1 product) |

## Section C — Corrected verdict

| v0.1 framing | v0.2 corrected |
|---|---|
| 12 = SM total gauge dim = **4-route over-determined** | 12 = SM total gauge dim = **2-route structurally-independent** (1 sum + 1 product) |
| Cluster "8-18 is doubly-over-determined zone, SM-gauge-content concentrated there" | Cluster reading still holds qualitatively; specific arithmetic-route-counts mostly reduce to 2-3 under relations |
| 12 is "the most arithmetically-redundant SM observable" | 12 is **structurally-doubly-over-determined like other cluster members** (8, 9, 10, 14, 15, 16, 18) — not uniquely most-redundant |

**Cluster observation STANDS**: SM-gauge dimensional content (dim 8-18) lives in the substrate's sum-product overlap zone. The structural reading is unchanged; only the specific route counts are corrected.

**Magic-126 product-only anomaly STANDS**: independent of this brake (magic-126's substrate forms don't involve the related-primary issue).

**N_max = 137 NEITHER STANDS**: independent of this brake.

**Nuclear shell arithmetic-hierarchy (v0.2 magic-126 work, INV-5313) STANDS**: separate finding, separate verdict.

## Section D — Lyra-engagement flag update

**v0.1 framing**: "12 = SM total gauge dim is 4-route over-determined — strongest substrate-arithmetic finding flagged for Lyra bulk-color theory engagement (#418)."

**v0.2 corrected framing**: "12 = SM total gauge dim is **structurally doubly-over-determined** (1 sum + 1 product after relation-reduction) — supports bulk-color emergence at count level but NOT uniquely-strongest among cluster members."

For Lyra #418: the 12 = SM-gauge-dim 2-route structure is STILL real and supportive, just less arithmetically-redundant than v0.1 framed. The bulk-color mechanism (Toeplitz + SO(3) sub-vector per v0.4/v0.5) doesn't depend on the 4-route framing specifically.

## Section E — Methodological lesson

**Calibration #33 STANDING applies INTERNALLY**: substrate-primary internal relations (C_2 = N_c·rank; n_C = rank+N_c) are RECALLED-from-framework facts requiring source-pin + independence-audit before any structural claim that counts arithmetic routes.

**For future scans**: any Mendeleev-style scan of substrate-arithmetic-vs-observables must:
1. Pin the substrate-primary relations explicitly
2. Run independence-audit on each "route" before counting
3. Default to structural-distinctness criterion (do the routes use algebraically independent expressions?)
4. Honest reporting: state the relations used + verify routes survive

## Section F — Honest verdict + Casey-named-principle update

**Status**: Two-Route Scan v0.1's higher-bar "Substrate Doubly-Over-Determination Principle" Casey-named-principle candidate is FURTHER SOFTENED:
- v0.1 → null-model gave +0.9σ (INV-5316) — already weak
- v0.2 → relation-reduction brake reveals 4-route framing was over-counted → softens further

**Lower-bar "Substrate-Arithmetic SM-Gauge Coincidence" framing is correct disposition** (Cal + Keeper consensus). The substrate doubly-over-determines a cluster of SM-relevant integers in 8-18 including SM gauge content; the cluster is real; the over-determination count per integer is mostly 2-3 (not 4); not principle-grade.

**What stands rigorously**:
- The cluster observation (SM-gauge content lives in substrate sum-product overlap zone)
- The 12 = SM-gauge-dim doubly-over-determined fact (1 sum + 1 product)
- Magic-126 product-only anomaly (separate finding, INV-5313)
- N_max=137 NEITHER (separate)
- Nuclear shell arithmetic-hierarchy (separate, INV-5313)

**What doesn't stand**: "12 is 4-route uniquely-most-redundant" framing.

## Section G — Cross-reference

- INV-5311 (v0.1 source)
- INV-5313 (v0.2 magic-126 anomaly — separate, stands)
- INV-5316 (Two-Route null model — weak signal already)
- Cal referee log #171 (the relation-reduction brake)
- Calibration #33 STANDING (Source-Verification, NOW applied INTERNALLY)
- Calibration #34 STANDING (headline-cap-conditionality)
- Keeper N1 protocol (null-model required before principle elevation)
- Lyra Strong-Uniqueness v1.1 (Route-A: 5 integers as D_IV⁵ invariants)

— Grace, Two-Route Scan v0.2 (Cal-brake-absorbed), 2026-05-30 Saturday ~11:30 EDT (`date`-verified)
