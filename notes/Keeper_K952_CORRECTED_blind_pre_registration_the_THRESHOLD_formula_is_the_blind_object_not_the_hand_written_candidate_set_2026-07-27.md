---
id: K952
date: 2026-07-27
program: TEGMARK
status: current
supersedes: [K950-candidate-set]
superseded_by: null
topic_tags: [occupancy-bijection, blind-pre-registration, threshold, k_min, 3-vs-4-fork, unitarity-bound, target-innocence, Cal-catch]
claims:
  - id: K952
    topic: the blind object is the DERIVED threshold formula k_min, not the hand-written candidate set; the candidate set falls out of it
    status: current
    superseded_by: null
    date: 2026-07-27
---

# Keeper K952 — CORRECTED blind pre-registration: the THRESHOLD formula is the blind object, not the hand-written candidate set

> **Cal §104 caught a real bug in K950 — RATIFIED, and it's on me.** K950 hard-coded the candidate set to {k∈{0,1,2}}, which caps the count at 3 by construction and quietly forecloses the 4-generation falsification branch the same note declares open. The root: {0,1,2} silently ASSUMES the threshold k_min=3 — but the threshold IS the 3-vs-4 discriminator (D_IV⁵: k_min=3 → 3 candidates; E7: k_min=4 → 4). I smuggled the fit into the single most target-sensitive step and called it blind. The fix: **the DERIVED threshold formula is the blind object; the candidate set falls out of it.** K950's FORM criterion stands (Cal ratified); only the candidate-set definition is superseded.

*[PROGRAM: TEGMARK] Keeper, 2026-07-27. The auditor's own guard had the defect it exists to catch. Owned, corrected, still before any signature is read.*

## The corrected blind object (committed now, before the number)
**1. DERIVE the threshold k_min for D_IV⁵ from so(5,2) structure — this is the blind object.** k_min = the unitarity / square-integrability bound for the Di spinor singleton, obtained from the k↔ν dictionary + the spinor shift (the §79 dictionary, pinned to a primary source: Enright-Howe-Wallach / Vergne-Rossi threshold for type IV, plus the singleton's spinor weight). Do NOT hand-write the candidate set; do NOT assume k_min=3.

**2. The candidate set FALLS OUT: {k : 0 ≤ k < k_min}.** If k_min derives to 3 → candidates {0,1,2} → max 3, and 4 is honestly EXCLUDED for D_IV⁵ by the threshold (line-55's "4" becomes an E7-only property). If the derivation ADMITS k=3 (k_min ≥ 4) → candidates {0,1,2,3,...} → **4 is genuinely reachable and the falsification branch is live.** Either way, the threshold derivation — not a hand-written set — decides 3-vs-4.

**3. E7 by the IDENTICAL formula.** Apply the same k_min derivation to E7/E_VII (its own real form, its own singleton weight) → E7's k_min → E7's candidate count. Report it; do NOT assume 4.

**4. THEN the signature (the secondary reduction).** On the fallen-out candidate set, compute the regularized contravariant-form signature (K950's structurally-fixed form) and count the surviving NON-NULL normalizable rungs. Per Elie's K951: positivity alone does NOT cap (the bulk form is positive everywhere → infinite); the count is (candidate set from the threshold) reduced by any null/reduction rungs under the fixed continuation. **b = surviving non-null normalizable rungs among the derived candidate set.**

## The two catches, unified (Cal §104 + Elie K951)
- **Elie:** positivity doesn't cap — the bulk formula gives all rungs positive, so "stop at 3" is by-hand. The cap is a truncation.
- **Cal:** the candidate set {0,1,2} IS the assumed cap — it pre-decides 3.
- **Unified:** the 3-vs-4 answer is set PRIMARILY by the threshold k_min (the candidate-set size), refined SECONDARILY by null rungs in the signature. **The threshold must be DERIVED blind; the signature is the check on top.** Both the candidate count and the survivors are computed, neither assumed.

## Retrofitting flags — ADD to K950's list
- Hand-writing the candidate set (the K950 bug) instead of deriving k_min.
- Choosing the k↔ν dictionary, the spinor shift, or the real-form convention to make k_min come out 3.
- Assuming k_min=3 (or the candidate count) from the observed 3 generations — target-aware.
- (Carried from K950/K951:) compact-form swap, free regularization, null-rung-as-generation, electron-position input, data/filtration exclusion, bulk-formula stop-at-3, representation chosen by which yields 3.

## The honest accepted outcomes (all publishable)
- k_min derives to 3, all candidates survive non-null → **3 generations** → premise ELIMINATED (given E7's k_min → 4 by the same rule).
- k_min admits k=3 (or a would-be-excluded rung survives) → **4** → geometry forces 4, observed 3 is a data cut → **LIVE FALSIFICATION**, published.
- fewer survive → the identification needs rethink; say so.
Whichever the DERIVED threshold + the fixed-form signature return is the answer. Premise stays REDUCED until both are read.

## Assignment
**★ LYRA + ELIE — pre-register the blind threshold derivation FIRST** (k_min for D_IV⁵ and E7 from so(5,2)/e7 structure via the primary-sourced k↔ν + spinor-shift dictionary), let the candidate set fall out, THEN run the K950-form signature on it. Pin the singleton weight + dims to a primary source (Cal §104 minor note) so E7's count is by the identical rule. Keeper audits the threshold derivation for target-innocence before the signature is read.

— Keeper K952, 2026-07-27 [TEGMARK]. Corrects K950: the blind object is the DERIVED threshold k_min (the 3-vs-4 discriminator), candidate set falls out, signature reduces on top; hand-writing {0,1,2} was the smuggled fit (Cal §104, ratified). Unifies with Elie K951 (positivity doesn't cap). 4-branch genuinely live. Companion: [[Keeper_K950_BLIND_pre_registration_the_correct_contravariant_form_for_the_rung_count_committed_before_the_signature_2026-07-27]], [[Keeper_K951_RATIFY_Elie_catch_bare_formula_gives_infinity_the_cap_is_a_null_rung_in_the_boundary_rep_not_positive_counting_2026-07-27]].
