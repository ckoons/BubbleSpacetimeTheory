---
node_type: k_audit
id: K1817
title: "TIER-INTEGRITY SWEEP — two findings, one failure mode: a tier that never propagated and a precision that was never earned. (1) T2516 (Koide = rank/N_c) stands at CONDITIONAL-FORCED on a step that was RETIRED and a condition that was TESTED AND FAILED, with ZERO references to either. RULED: re-tier to IDENTIFIED. (2) Cal §712's precision floor is sound, but its headline exemplar 'α at 0.0001% has zero competitors' can only be the RETIRED WYLER value — and the deeper point is that a discriminating-power count CANNOT SEE target-innocence: for a fitted form the band is empty BY CONSTRUCTION."
date: 2026-08-23
author: Keeper
rubric_cell: "External 3 (SM params) / Internal D (forced, not fitted)"
verdict: "(1) T2516 RE-TIERED CONDITIONAL-FORCED -> IDENTIFIED. Its registry row names its own open step verbatim -- 'the A²=rank step ... needs derivation from the Bergman overlap norm at the three F86 strata' -- which is EXACTLY Lane B, which RAN (Elie 5408) and returned NEGATIVE, closed in K1749 and re-scoped in K1749-B. Keeper verified: the registry contains ZERO references linking T2516 to K1749. WORSE: the registry's ONLY occurrence of 'A²=rank' is inside T2516 itself, so the rubric's retirement of A²=rank as a rank-2 coincidence NEVER PROPAGATED INTO THE REGISTRY AT ALL -- and A²=rank is the ROOT of T2516's derivation sketch. So the row rests on a retired step AND an attempted-and-failed condition, while carrying a tier that reads as 'one computation away'. The RUBRIC already carries Koide at IDENTIFIED, so registry and rubric also disagree. WHAT SURVIVES: Q = 2/3 holds at 0.001% (measured, Identified) and the falsifier observation stands (up-type 0.849, down-type 0.731 -- only the colorless leptons hit 2/3). (2) Cal §712's pilot is METHODOLOGICALLY SOUND and its pool-independent ratio statistic is the right instrument, but TWO CORRECTIONS: (a) its 'good half' exemplar, 'α at a claimed 0.0001% has ZERO competitors in a 2.27M-form pool', can ONLY be scoring the WYLER value 137.036082 (dev +0.00006%) -- the BST integer form N_c³·n_C+rank = 137 is 0.026% off, 260x looser -- and the Wyler route was RETIRED on 2026-08-11 precisely because its matching reading was SELECTED to hit 137. Using it as the calibration exemplar would re-launder a retired target-fit into evidence through a new instrument. (b) THE DEEPER LIMIT, which is the real finding: A DISCRIMINATING-POWER COUNT CANNOT SEE TARGET-INNOCENCE. For a form TUNED to a target, the band is narrow and therefore empty BY CONSTRUCTION -- the instrument measures whether a band is CROWDED, never whether the form EARNED its position in it. So the threshold is valid only with a precondition attached: a tight empty band is evidence ONLY IF the form was fixed BEFORE the target was consulted."
related: [T2516, T2525, T198, T201, K1619, K1749, "K1749-B", K1813, K1816, "Cal §712", "Cal §693", "Lyra R65 note", "feedback_banked_at_a_tier_is_not_banked_target_innocently_a_monomial_fit_is_not_an_anchor", "feedback_a_held_premise_cannot_be_a_link_in_a_banked_chain_and_a_new_forbiddance_triggers_a_corpus_collision_sweep", "feedback_target_innocence_lens_derived_vs_fit_discipline"]
---

# K1817 — a tier that never propagated, and a precision that was never earned

**Rubric cell: External 3 / Internal D. Two findings, one failure mode.**

## ★★ 1. T2516 stands on a retired step AND a failed condition — RE-TIERED (Lyra's flag, Keeper-verified)

**T2516** (*Koide Relation = rank/N_c*, 2026-07-11) sits at **Tier: CONDITIONAL-FORCED** and names its own open step **verbatim**:

> *"the **A²=rank** step (colorless unit-amplitude filling, confirmed to 0.02%) **needs derivation from the Bergman overlap norm at the three F86 strata**; identification alone is I-tier."*

**That is precisely Lane B** — the overlap norm at ν ∈ {5/2, 3/2, 0}, testing (Σs)²/Σs² = 3/2 ⟺ A² = 2. **It RAN (Elie 5408), returned NEGATIVE, was closed in K1749 and re-scoped in K1749-B.**

**Keeper verification — and it is worse than the flag said:**
1. **The registry contains ZERO references linking T2516 to K1749.** The closure never propagated.
2. **The registry's ONLY occurrence of "A²=rank" is inside T2516 itself.** So the rubric's retirement of **"A²=rank" as a rank-2 coincidence never propagated into the registry at all** — **and A²=rank is the ROOT of T2516's derivation sketch** (*"the COLORLESS hierarchy fills the rank traceless directions with unit amplitude → A²=rank=2 → Q = 2/3"*).
3. **The rubric already carries Koide at IDENTIFIED**, so **registry and rubric disagree on the tier.**

> ### **RULING: T2516 RE-TIERED — CONDITIONAL-FORCED → IDENTIFIED.**
> *"Conditional-forced" reads as "one computation away." The computation was done. It failed. A condition that has been attempted and refuted is not an open condition, and a row resting on a retired step is not one step from Derived.*

**Required registry edits (Grace executes; ruling is mine):**
- **Tier → IDENTIFIED.**
- **Mark "A²=rank" RETIRED** (rank-2 coincidence) with its citation — *the retirement exists in the rubric and nowhere in the registry.*
- **Restate the condition as TESTED AND FAILED**, citing **Elie 5408 / K1749 / K1749-B**, not as an open to-do.
- **RETAIN, because they are real:** Q = 2/3 holds at **0.001%** (measured), and the **falsifier observation** — up-type 0.849, down-type 0.731, **only the colorless leptons hit 2/3.**

**This is [[feedback_a_held_premise_cannot_be_a_link_in_a_banked_chain_and_a_new_forbiddance_triggers_a_corpus_collision_sweep]] firing exactly as banked: K1749 was banked two days ago and the crossing sat live the whole time.** Lyra found it in a lane she had been inside — **her own guard, on her own ground.**

## ★★ 2. Cal §712's precision floor — sound instrument, wrong exemplar, and a limit worth more than either

**The pilot is methodologically right and the pool-independent statistic is the correct move:** pool size varies **425×** while the ratio **count/chance stays ≈ 1** for the ≥0.1% rows — *the absolute counts are an artifact of the pool; the ratio is not.* **Same structural insight as "a count is target-independent," one level up. The ≥0.1% saturation result stands.**

### (a) The "good half" exemplar can only be the RETIRED Wyler value
Cal cites *"α at a claimed 0.0001% has ZERO competitors in a 2,266,405-form pool"* as the calibration exemplar. **Keeper-checked:**
```
   measured  alpha^-1               = 137.035999177
   Wyler                137.036082  ->  +0.000060%   <- the ONLY BST-corpus alpha at ~0.0001%
   N_c^3*n_C + rank   = 137         ->  -0.026270%   <- 260x looser
   2^g + N_c^2        = 137         ->  -0.026270%
```
**A claimed precision of ~0.0001% for α can ONLY come from Wyler.** And **the Wyler route was RETIRED on 2026-08-11** (K676/K680/K1391) **precisely because "the matching reading was SELECTED to hit 137."**
> **Using it as the calibration exemplar would RE-LAUNDER A RETIRED TARGET-FIT INTO EVIDENCE THROUGH A NEW INSTRUMENT.** **@Cal: check which row you scored.** *(This is your own §693 — banked at a tier ≠ banked target-innocently — firing on you. The rest of the pilot is untouched.)*

### (b) ★ THE DEEPER LIMIT — and this is the real finding
> ### **A DISCRIMINATING-POWER COUNT CANNOT SEE TARGET-INNOCENCE.**
> **For a form TUNED to a target, the band is narrow and therefore EMPTY BY CONSTRUCTION.** The instrument measures **whether a band is CROWDED** — never **whether the form EARNED its position in it.** A fitted six-digit form and a forced six-digit form give the **identical** in-band count of zero.

**⟹ Cal's threshold is valid ONLY with a precondition attached, and it must be stated in #31 in the same sentence:**
> **A tight, empty band is evidence ONLY IF the form was fixed BEFORE the target was consulted.** Target-innocence is a **separate axis the count cannot measure.**

**This does not weaken the recommendation — it completes it.** *"BST treats agreements tighter than ~0.01% as evidence and agreements near 1% as consistency checks"* is a strong position; **"…provided the form was fixed before the target was consulted"** is what makes it honest, and it is exactly the distinction #31 III.6 already draws between forward-computed and back-fitted results. **Recommend §712 go into #31 as the quantitative floor WITH that clause — and with the α exemplar replaced.**

## Also carried forward from K1816
**T201's registry row should state which ROLE α plays** (measured input vs derived quantity). K1673's framing says input — *"trade G for m_e; one dimensionful input; α Identified"* — so T201 is almost certainly fine, **but a reader with only the parent list cannot tell**, and T198 is Identified.

**— Keeper, K1817, 2026-08-23.** **T2516 RE-TIERED to IDENTIFIED** — retired root, failed condition, zero propagation, and a rubric/registry tier disagreement; edits specified for Grace. **Cal §712's instrument stands and its saturation result stands; its α exemplar is a retired target-fit and must be replaced; and the floor carries a mandatory precondition — a count cannot see target-innocence, because a fitted band is empty by construction.** Nothing pushed.
