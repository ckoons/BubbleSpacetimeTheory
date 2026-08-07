# Grace — Pointer-Integrity Audit (task #84): the theorem_id provenance column is systematically stale (2026-08-07)

**Scope (Keeper/Casey-approved): every constant→theorem link, orphans, competing forms, mis-tiers. Report → plan → approve → apply. NOTHING applied here — this is the plan.**

## Headline finding (verified, independently)
**Only 29 of 197 constants in `bst_constants.json` have a theorem_id that actually points to the matching theorem.** The `theorem_id` provenance column is **systematically stale** — it cites an early theorem numbering (mostly T176–T400) that has since been overwritten by *different* theorems. Confirmed against **two independent sources** (graph `tid` AND the registry markdown), so it is not an artifact of my tooling:

| constant | cites | that tid is actually… | should be (by name) |
|---|---|---|---|
| const_011 Weinberg angle | T280 | **Lagrange's Theorem** | T197 (Weinberg, now RUNNER) |
| const_040 Top quark mass | T220 | **Doppler Effect** | T2009 (Top quark mass) |
| const_024 θ₁₃ reactor | T332 | **Molecular Bond Energy** | (PMNS sector, T329/T2018) |
| const_046 MOND scale | T197 | **Weinberg Angle** | T191 (MOND Acceleration) |
| const_016 CMB n_s | T196 | Bekenstein-Hawking Entropy | T1962 (CMB Spectral Index) |

## Root cause (hypothesis, well-supported)
At some reorganization, low tids (T176–T400) were reassigned to foundational-math theorems (Lagrange, Sylow, Doppler, Coulomb…), and the physics-constant theorems were re-registered at **high tids (T1900s–T2000s)**. The constants' `theorem_id` column was **never migrated**. Evidence: the correct match for a physics constant is almost always a *high* tid with a near-identical name (top quark → T2009, proton charge radius → T1992, CMB n_s → T1962, neutron-proton diff → T2022).

## Scope breakdown (197 constants)
- **29 CONFIRMED-OK** — cited tid name matches the constant.
- **~75 REPOINT candidates** — cited tid is unrelated; a name-matching theorem exists (score ≥0.5).
- **~19 HIGH-CONFIDENCE** (exact name-set match, subset of the 75) — safe starter set (e.g. const_016→T1962, const_040→T2009, const_045→T1992, const_041→T2022, const_082→T275, const_017→T705).
- **~14 AMBIGUOUS** (weak match) + **~79 NO-MATCH** — need per-entry investigation (constant may have no registered theorem, or names diverge).

## ⚠ The auto-match is NOT auto-applicable (false positives found)
Name-matching alone mis-fires: e.g. const_036 (electron g-2) → "**Proton** Anomalous Magnetic Moment"; const_027 (proton lifetime) → "**Tau** lifetime"; const_083 (W width) → "Spin-statistics". **Every repoint needs a human confirm.** This is why I am reporting a plan, not applying edits.

## What is NOT wrong (precise framing — avoid alarm)
The constants' **formulas, values, and tiers are intact.** This is a **provenance-pointer** failure (which theorem backs each constant), not a physics error. But it IS load-bearing: it's *why* "sin²θ_W = 3/13, Proved" could sit unreconciled — the links that should have caught it were pointing at Lagrange's Theorem.

## Also surfaced
- **Orphans (14):** cited theorem_id not in the graph at all (T196b, T198c, T2363a×5, K-32, …).
- **Competing forms (→ Casey tier call, task #83):** θ₁₃ = 1/45 (const_024) vs 3/137 (registry T329/T2018, Proved) — two Proved values for one angle; at most one is a real derivation.
- **T197/T1919 already retired to RUNNER** in the registry (Keeper's lane — done).

## Recommended approach (for Casey + Keeper approval)
1. Apply the **19 high-confidence repoints** after a one-line eyeball each (I'll table them cited→proposed with the theorem's full name for sign-off).
2. Work the **~75 candidates** in reviewed batches (10–15/batch), each confirmed against the registry before writing.
3. **Orphans + no-match**: investigate individually — some constants may genuinely lack a registered theorem (→ create, or mark provenance-pending).
4. θ₁₃ competing-form: Casey's tier call first (task #83), then repoint to the winner.
- **Guardrail:** every batch backed up; nothing applied without the plan approved. The rate-signal lesson applies at scale — verify each pointer, don't bulk-write a name-match.

**Nothing applied. Backup `.bak.2026-08-07_governance_apply` stands. Nothing pushed.**
