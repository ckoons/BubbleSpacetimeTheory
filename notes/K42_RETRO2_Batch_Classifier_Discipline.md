---
title: "K42: RETRO-2 Batch-Classifier Discipline"
author: "Keeper"
date: "2026-05-16 ~05:30 EDT"
audit_id: K42
verdict: STANDING DISCIPLINE filed; pattern documented for future batch passes
overall_confidence: 95%
scope: "Lessons learned from RETRO-2 (Grace Toy 2254 classifier) batch-upgrade pass; standing rules for future SP-24-style sweeps"
related: ["BST_SP24_Phase1_ColdRead_Criteria.md", "BST_SP25_ITier_Route_Discipline.md", "grace_revert_73_auto_structural.py", "grace_revert_audit_2026-05-15.md", "grace_t186_retag_audit_2026-05-15.md", "toy_2254_mass_ratio_batch_upgrade.py"]
---

# K42: RETRO-2 Batch-Classifier Discipline

## Audit summary

RETRO-2 (Grace's batch I→D classifier pass, May 15 afternoon) produced 277 tier upgrades that climbed catalog D-tier from ~76% to ~85.8%. Subsequent stratified-sample audit by Grace caught a **class-level false-positive pattern** affecting 73 of 283 upgrades (26%) — items where `symbol` started with `auto_*` AND `status` was already flagged `structural` by the original creator. These were promoted I→D despite the team's own tier definition holding that `structural` is incompatible with D-tier ("mechanism derived").

Casey directive (May 15 ~17:50 EDT): revert the 73.

Grace executed (Toy 2255 sequence + grace_revert_73_auto_structural.py), reverting 73 entries D→S. Catalog D-tier honestly recalibrated to 84.0%. Separate 360-entry historical sweep (Option A) added 221 more reverts, settling honest baseline at 78.8%. 

This audit documents the pattern so future batch passes don't repeat it.

## The pattern

**Toy 2254's classifier matched on keyword presence in entry text** without consulting two adjacent fields that would have prevented the false positives:

1. **The `status` field** — entries honestly flagged `status: "structural"` by their original creator should not be eligible for I→D promotion. "Structural" is the team's own tier definition for "qualitative or precision >2%, not a derivation." A classifier that ignores this field promotes coincidences to derivations.

2. **The `symbol` field naming convention** — entries with `symbol` prefixed by `auto_*` were *auto-discovered combinatorial pattern hits* (e.g., `auto_pi_minus_Nc_approx = 1/g ≈ π−3`). These are by construction speculative numerical matches, not derivations. A classifier that doesn't restrict by symbol prefix promotes coincidences alongside real mechanisms.

The combination: **`auto_*` symbol + `structural` status** = honest creator self-flagged as "this is a combinatorial pattern hit, not a mechanism." Toy 2254's classifier ignored both signals and matched on keyword presence ("contains a BST integer in formula text").

## Secondary issue: T186 default-citation problem

Of the 283 RETRO-2 upgrades, 228 (81%) had `theorem` field set to T186 (Five Integers Uniqueness). T186 is technically a valid citation for any formula referencing N_c, n_C, C_2, rank, g, or N_max — which is essentially every BST formula. So T186 becomes a *tautological keystone* rather than a *load-bearing mechanism citation*.

Grace's retag sweep (May 15 ~18:20 EDT, `grace_retag_t186_defaults.py`) found that 20 of the 228 (8.7%) genuinely had a more-specific load-bearing mechanism (T1783 Chern, T1821 Bergman, T187 proton-mass derived, T1829 Wallach, T920 Debye), which got retagged. The remaining 207 of 228 (91%) were *actually* T186 — formulas that genuinely use only five-integer arithmetic with no further mechanism.

**This was Grace's "honest correction" moment**: her initial framing ("228 of 283 defaulted to T186, implying mostly mislabel") was true but misleading; the real mislabel rate was 8.7%, not 81%. Worth naming the discipline that surfaced this: she ran the retag deterministically, counted outcomes, and revised her own framing in MESSAGES without prompting.

## Standing discipline (for future batch passes)

Any future RETRO-style batch sweep that classifies catalog entries for tier promotion MUST:

### Per-entry classifier guards

1. **Status-field guard**: NEVER promote an entry with `status: "structural"` to D-tier via batch classifier. If the team flagged it structural, the classifier doesn't override. (Manual review possible, but not batch.)

2. **Symbol-prefix guard**: NEVER promote an entry with `symbol: "auto_*"` to D-tier via batch classifier. Auto-discovered combinatorial pattern hits stay at the tier their creator assigned (typically S or I).

3. **Precision-field guard**: NEVER promote an entry with `precision ≥ 2%` to D-tier via batch classifier. The tier definition reserves D-tier for mechanism + precision; precision alone doesn't promote, but precision absence prevents promotion.

4. **Theorem citation specificity**: When promoting, the classifier MUST cite the *most specific* load-bearing theorem, not the most general. Default to T186 ONLY when no other marker exists in the entry text or notes. Markers: T1783 (Chern), T1821 (Bergman), T187 (proton-mass chain), T1829 (Wallach), T920 (Debye), T1788 (YM ring), T1444 (vacuum subtraction), T1464 (RFC). Future markers extend the list as new mechanism theorems emerge.

### Per-batch sample-audit requirement

Any batch pass that promotes >50 entries MUST be followed by a stratified random sample audit (≥10 items, ≥2 per matched mechanism theorem) before the next batch runs. The sample audit verifies that the matched mechanism actually load-bears on each promoted entry. If the sample finds ≥1 outright fail or ≥3 mislabels, the batch is paused for methodology review.

This is Cal's "class-level false positive" concern from K38 cold-read. Grace's RETRO-2 audit confirmed his suspicion was warranted; SP-25 ✓/◊ distinction (filed earlier May 15) addresses the same issue at the I-tier-promotion layer.

### Per-batch honest accounting

When batch results are reported externally, the headline D-tier percentage must include explicit caveat for any uncategorized residual. "84.1% D-tier" is honest only if the team has verified the residual S/I/C-tier items are correctly tiered. If a historical batch of N items hasn't been sample-audited, the headline carries footnote: "headline includes N items pending audit."

The 360 historical entries audit (Casey approved Option A, May 15 ~17:50 EDT) was applied because we couldn't ship 84.1% to a referee in good faith with 360 items pending. After Option A: 78.8% honest baseline. The 7-point drop is the audit's signature, not a regression.

## The execution-path slip (honest disclosure)

Grace also disclosed (May 15 ~18:05 EDT) an execution-path slip during the revert: her initial script over-matched (433 entries instead of 73, because the predicate didn't restrict to the RETRO-2 batch). She caught the discrepancy on output, stopped, then ran `git checkout data/bst_geometric_invariants.json` to restore. The checkout reverted to a state before Elie's 5 new Hilbert_Q5 entries (Toy 2255) had been committed, momentarily losing them. She restored byte-identical from her earlier Read, no content lost.

The lesson she named: **never destructive-revert a shared data file without first checking what's uncommitted via `git diff` or saving a pre-script copy.** Worth incorporating as a standing rule for any future scripted edits to shared data layer.

## Effect on existing programs

- **SP-24 Phase 2**: future batch passes adopt these guards from K42. Toy 2254 retired as classifier; future classifier must implement the four guards above.
- **SP-25 first cadence (May 29)**: applies the same guards to I-tier /route promotions. Auto+structural entries in I-tier stay structural unless an /route closure produces a documented mechanism.
- **Catalog completeness**: any future batch I→D classifier MUST be tested against a hold-out validation set (~30 entries with known correct tier) before deployment. Grace's RETRO-2 was deployed without this validation step; the false-positive rate is the consequence.

## Tier residual after honest accounting

| Tier | Pre-RETRO-2 | After RETRO-2 | After K42 revert (73) | After Option A revert (221) | Current |
|------|-------------|---------------|------------------------|------------------------------|---------|
| D | ~76% | 85.8% | 84.1% | 78.8% | climbing post-T1918 |
| I | ~5% | 4.9% | 4.9% | 4.8% (down to ~0.2% catalog after T1918 cascade) | 7 residual → 0-2 |
| S | ~6.5% | 6.5% | 8.4% | 14% | ~14% |
| C | ~2.7% | 2.7% | 2.7% | 2.7% | ~2.7% (sweep pending) |

The post-T1918 climb is the unlocked dimensionful sector returning to D-tier as masses re-derive via M_Pl anchor.

## Recommendation: codify K42 as standing rule

Add to `BST_Referee_Methodology.md`:
- §[batch-classifier guards] — four guards above
- §[sample-audit requirement] — stratified sample after batch >50
- §[honest accounting] — footnote for uncategorized residual
- §[destructive-edit caution] — git diff before checkout on shared data

K42 status: filed as Keeper audit; promotion to standing rule pending Casey approval. Once approved, becomes part of standard discipline alongside SP-14 (catalog discipline) and SP-25 (I-tier /route discipline).

---

*K42 filed by Keeper, May 16, 2026, ~05:30 EDT. Materials: Grace's MESSAGES posts (17:35, 18:05, 18:20), her revert scripts, her retag scripts, the audit tables. The discipline that surfaced this pattern was Cal's "class-level false-positive" cold-read flag + Grace's stratified-sample methodology + Casey's directive to revert + Grace's honest framing correction. Quaker consensus across CI roles at full strength.*
