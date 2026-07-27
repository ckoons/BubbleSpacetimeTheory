---
id: grace_TEGMARK_third_prong_condition2_gate_passes_E7_closed_by_data_2026-07-27
date: 2026-07-27
program: TEGMARK
status: partially-superseded
supersedes: []
superseded_by: null
topic_tags: [forcing-chain, inverse-forcing, well-posedness, rigidity, E7, Koranyi-Wolf, generations, K943, K944]
claims:
  - id: this-a
    topic: strata COUNT = rank+1 is uniform (Koranyi-Wolf) — condition-2 count-check
    status: current
    superseded_by: null
    date: 2026-07-27
  - id: this-b
    topic: "E7 exclusion 'legitimate / closes the hole / well-posedness' conclusion"
    status: superseded
    superseded_by: K944
    date: 2026-07-27
    note: "OVER-REACH (Grace, owned) — the exclusion needs the OCCUPANCY BIJECTION (each stratum hosts exactly one generation), which is un-derived. Premise REDUCED (minimality traded for generations=strata identification), NOT eliminated. See K944."
---

> ⚠ SUPERSEDED (in part), 2026-07-27 by **K944** — the **count-check (claim-a) stands** (strata=rank+1 is derived/uniform, Korányi-Wolf ✓). But the **conclusion (claim-b) that the E7 exclusion 'closes the hole' / achieves 'well-posedness' is SUPERSEDED**: the exclusion silently assumed the **occupancy bijection** (each of the r+1 strata hosts *exactly one* generation), which is an ASSERTED identification (F86/T2525), not derived. So the rank=2 premise is **REDUCED** (traded for generations=strata), **not eliminated**. Well-posedness is the TARGET, not yet the claim. Prior audits already tiered this identification (K881, K876, F88 §5, F340). Current view: [[Keeper_K944_AUDIT_Cal_93_generations_strata_is_MATCH_not_bijection_premise_REDUCED_not_eliminated_2026-07-27]].

# [TEGMARK] Third-prong gate check: condition 2 PASSES — "generations = rank+1 strata" is uniform (Korányi-Wolf), and it closes the E7 hole with data

*Grace | 2026-07-27 Mon | Keeper's K943 flagged the load-bearing gate on Casey's third prong (inverse-forcing/well-posedness): is "generations = rank+1 strata" the GENERAL Korányi-Wolf fact (uniform functor, condition 2), or D_IV⁵-specific (which would rig the inverse)? My lane (rep-theory sourcing + target-innocence). Verdict: gate passes; the E7 exclusion is legitimate.*

## ★ Condition-2 gate: PASSES
**Korányi-Wolf (standard, Wolf 1972):** a bounded symmetric domain of rank r has its boundary in exactly **r+1** G-orbits (the support-flag strata), from maximal to the Shilov minimum. This is a **uniform** theorem — *every* domain, its *own* rank r → r+1 strata. Not D_IV⁵-specific.

BST's identification **"generations = boundary strata"** (T2525) rests on this *general* KW structure, not on any D_IV⁵-specific relation. Applied uniformly — each candidate domain: generations = its own rank+1 — it is **condition-2-clean** (same rule, no D_IV⁵ machinery leaking). **⇒ the E7-predicts-4-generations exclusion is legitimate.**

Honest caveat (state it): "generations = strata" is BST's physics *identification*, not a proven theorem — but condition 2 only requires it be applied *uniformly*, which it is.

## The uniform functor (each domain its OWN integers; no D_IV⁵ machinery)
Rules, uniform: generations = rank+1 (KW); N_c = rank²−1 (T1829, physics-free); N_max = N_c³·dim + rank; α⁻¹ = N_max. Selectors = **measured** generation-count (3) and α⁻¹ (137).

| domain | rank | dim | gens=r+1 | N_c=r²−1 | N_max | verdict |
|---|---|---|---|---|---|---|
| **D_IV⁵ (BST)** | 2 | 5 | **3 ✓** | 3 | **137 ✓** | **SELECTED** |
| D_IV⁴ | 2 | 4 | 3 ✓ | 3 | 110 | excl: α⁻¹ |
| D_IV⁶ | 2 | 6 | 3 ✓ | 3 | 164 | excl: α⁻¹ |
| D_III² (Sp(2)) | 2 | 3 | 3 ✓ | 3 | 83 | excl: α⁻¹ |
| I₂,₂ | 2 | 4 | 3 ✓ | 3 | 110 | excl: α⁻¹ |
| E_III (E6) | 2 | 16 | 3 ✓ | 3 | 434 | excl: α⁻¹ |
| **E_VII (E7)** | 3 | 27 | **4 ✗** | 8 | 13827 | **excl: generations** |

**Measured SM (3 generations, α⁻¹ = 137) lands ONLY on D_IV⁵.** The rank-2 neighbors are excluded by α⁻¹ (110/164/83/434 ≠ 137); E7 — the census co-solution of N_c = rank²−1 — is excluded by the **data**: rank 3 → 4 generations ≠ observed 3.

## ★ Why this matters (the K943 Node-1 residual)
The structural census picks D_IV⁵ over E7 by the **asserted** rank=2 minimality premise (K943's remaining soft spot). The third prong closes that hole with **observed data**: E7 predicts 4 generations, the universe shows 3, so E7 is *refuted*, not merely deprioritized — **without invoking the minimality premise.** Forward (existence) + inverse (identifiability) = **well-posedness**, the obstinacy-resistant word for the panel.

## Honest condition-guards (for Keeper's blind pre-registration + Elie's toy)
- **Condition 1 (full set):** the table is the ~6 nearest of the classification; Elie's rigidity toy extends to all six families + neighbors. Not cherry-picked.
- **Condition 2 (uniform functor):** ✓ each domain its own (rank, dim, N_c); KW strata-rule general; N_max form applied uniformly. *Caveat:* the α⁻¹ selector presupposes the N_max = N_c³·dim+rank *form* (Elie's census flag) — the generation-count selector does NOT (pure KW), so **the E7 closure is the cleaner of the two** (no formula presupposition).
- **Condition 3 (data selector):** generation-count (3) and α⁻¹ (137) are measured. ✓
- **Condition 4 (not the integers):** the selectors are observables, not "the integers match." ✓

## Handoffs
- **Keeper:** condition 2 passes → the rigidity toy is sound to build; the E7-by-generations row is the cleanest (KW-only, no N_max form). Pre-register the "miss" thresholds blind; the generation-count exclusion of E7 is integer-exact (4≠3), not a σ-threshold.
- **Elie:** the uniform functor + candidate table above is your rigidity-toy spec (extends task #28). Each domain its own integers; no D_IV⁵ formula leaks. The generation-count column is condition-2-cleanest.

— Grace, 2026-07-27 [TEGMARK]. Third-prong condition-2 gate: PASSES. Korányi-Wolf "r+1 strata" is a general/uniform theorem (Wolf 1972), so "generations = rank+1 strata" applied uniformly is condition-2-clean → the E7-predicts-4-generations exclusion is legitimate. Uniform functor across 7 candidate domains (each its own rank/dim/N_c): measured SM (3 gens, α⁻¹=137) lands ONLY on D_IV⁵; rank-2 neighbors excluded by α⁻¹, E7 (census co-solution) excluded by DATA (rank 3→4 gens≠3). Closes K943's E7/rank=2-premise hole with observed data, not the asserted minimality premise → well-posedness. Cleanest exclusion = E7-by-generation-count (pure KW, no N_max-form presupposition). Feeds Keeper's blind thresholds + Elie's rigidity toy.
