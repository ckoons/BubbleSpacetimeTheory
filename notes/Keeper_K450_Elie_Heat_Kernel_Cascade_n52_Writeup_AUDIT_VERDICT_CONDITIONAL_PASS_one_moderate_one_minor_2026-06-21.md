# K450 — Audit Verdict: Elie's Heat-Kernel Cascade n=52 Write-Up

**Date:** 2026-06-21 (Sunday, 08:45 EDT `date`-verified) · **Auditor:** Keeper · **Target:** `notes/Elie_Heat_Kernel_Cascade_n52_Writeup_2026-06-21.md`

## Verdict — **CONDITIONAL PASS**

- Mathematical content: **SOLID** (every numerical claim spot-checked independently passes).
- Tier discipline: **HONEST** (SOLID / IMPOSED / LEAD / INTERPRETIVE used cleanly throughout).
- **One MODERATE refinement** required: the stated justification for the `KNOWN_AK5[17]` constant-fix is weak; the *correct* justification is the independent cross-file match Elie also cites. Replace the weak argument; the fix itself stands.
- **One MINOR action** recommended: add a precision caveat to the stored JSON for high-k interior coefficients (Elie's own audit target #5).
- Count impact: **0 newly banked**; **4 of 26 holds** as Elie framed. Concurred.

## Independent verifications performed (Keeper, against stored JSON)

All checks done directly against `play/toy_671_checkpoint/coefficients_n52_dps3200.json` — not via Elie's toys.

| Check | Result |
|---|---|
| Leading `1/(3ᵏ·k!)` at k∈{2,5,10,17,26} | **5/5 PASS** |
| Constant `(−1)ᵏ/(2·k!)` at k∈{2,5,10,17,26} | **5/5 PASS** |
| Subleading `−k(k−1)/(2n_C) · leading` at k∈{2,5,10,17,26} | **5/5 PASS** |
| Speaking-pair ratios v(k) = −k(k−1)/10 at the 10 stated k | **10/10 PASS** (all integers, all match Elie's table) |
| Within-pair gaps v(5m) − v(5m+1) = m for m=1…5 | **5/5 PASS** |
| Between-pair second-difference = −n_C = −5 | **3/3 PASS** (jumps −7,−12,−17,−22) |
| a₁₇(5) computed by direct polynomial evaluation at n=5 | **6964243457/59604** ✓ matches stored; stale `KNOWN_AK5[17] = 20329084105/173988` does NOT match → fix justified |
| Q⁵ scalar Laplacian spectrum λ_k = k(k+5) ⇒ gap = 6 = C₂ | PASS (Casimir of SO(7) on symmetric-tensor rep π_k: (k+5/2)² − 25/4 = k(k+5); dim π_1 = 7 = SO(7) vector) |

Cascade fingerprints all reproduce. The speaking-pair ladder is exactly what `v(k)` predicts; n_C = 5 organizes the levels *three* ways (period mod n_C, within-pair counter, between-pair step) — concur with the Schur-generator-signature read **as a consequence of the imposed subleading form**, not as a free discovery (Elie tiered this honestly).

## Answers to Elie's five audit targets

**(1) Skeleton vs output tiering — PASS.** The framing "leading/subleading/const are IMPOSED, ladder is a *consequence*" is correct and the write-up's tier tags reflect this. Concur with Section 3's "**SOLID** that the patterns hold and derive from v(k); **IMPOSED** that v(k) itself is the three-theorems subleading form (so the ladder is a clean *consequence*, not a new degree of freedom — flagged honestly)." Good discipline.

**(2) VSC smoothness horizon LEAD-tagging — PASS.** The k ≈ 14 horizon is stated; the k ≥ 15 regime is correctly flagged as showing large primes (e.g. 3907 at k=17, 60889 at k=20); the k=26 incidental return to maxprime 11 is *not* claimed as structural. LEAD tag is the right tier — the von-Staudt–Clausen connection is a Bernoulli-denominator shadow, not a proven identity. No leakage to SOLID.

**(3) "Downstream pairs correct ⇒ a₁₇ correct" — INSUFFICIENT (MODERATE).** Elie's cited self-consistency argument does not bear weight. The downstream "speaking pairs" are the subleading-over-leading ratios, which are *imposed* at every k by the three-theorems constraint, not derived from a₁₇'s interior content. A wrong a₁₇ would not corrupt the speaking-pair integers at k=18…26 because those pairs only test the imposed-form pipeline, which is reset at each k.

The *correct* justification — also cited by Elie — is the **independent cross-file match**: the computed a₁₇(5) = 6964243457/59604 reproduces the value stored in the prior `results_hybrid_3200.json` (a separate run, with its own extrapolation history, predating the new n=52 checkpoint). That cross-file agreement is independent of `toy_671d`'s hardcoded reference constant. **The fix stands** on that ground.

**Action for Elie:** in the audit-target answer or the toy_671d comment, replace "downstream speaking pairs all correct ⇒ a₁₇ correct" with "computed a₁₇(5) matches prior official run `results_hybrid_3200.json` independently of toy_671d's hardcoded `KNOWN_AK5[17]`." Same fix, honest reasoning.

**(4) Interpretive claims contained — PASS.** Gap-as-filter (INTERPRETIVE framing on SOLID spectrum), protected-vacuum thermodynamics (SOLID identification with INTERPRETIVE reading), and "permanent operation" (OBJECTIVE measured profile vs INTERPRETIVE teleology) are correctly tagged. The OBJECTIVE / INTERPRETIVE split for "permanent operation" is the cleanest part of the write-up — separating what the math says ("gapped, integer-spectrum, modular, rigid") from the single word it does not decide ("for"). That is how Keeper would have framed it.

**(5) Interior-coefficient precision at high k — RECOMMEND ACT.** Yes. Add an explicit precision caveat to `coefficients_n52_dps3200.json` for k ≥ 20, ideally as a `precision_caveat` field per entry (or a `precision_floor_k` field in `meta`). The speaking-pair invariants are theorem-pinned and remain SOLID regardless; the interior coefficients at high k are bounded by the per-dimension Richardson/Neville extrapolation match-rate, and a downstream reader should not silently consume them at face value. One sentence in `meta` is enough.

## Additional Keeper observations (not in Elie's audit targets)

- **(a) Multiplicity-2-per-voice = rank fit (INTERPRETIVE/LEAD).** Elie tagged this correctly. Concur it is "fits, not banked"; the doublet structure at (5m, 5m+1) is forced by `v(k)` being a degree-2 polynomial in k, which produces consecutive integer values around its integer-period crossings. The rank=2 match is real-but-circumstantial. Keep at LEAD.

- **(b) Spectrum-side independent check.** The Q⁵ Laplacian eigenvalues k(k+5) follow from the SO(7) Casimir on symmetric-tensor scalar reps via ρ_SO(7) = (5/2, 3/2, 1/2): Casimir(π_k) = (k+5/2)² − 25/4 = k² + 5k. Casey's compact dual is SO(7)/[SO(5)×SO(2)] which carries the same scalar spectrum as the harmonic-on-quadric calculation. This is a clean substrate-independent cross-anchor for the gap = C₂ = 6 reading. **No action**, but worth noting in the Vol 16 chapter when it absorbs this material — the gap = C₂ identity is *triply* anchored now (heat-trace + Casimir + curvature-equivalent).

## Ratification disposition

- Heat-kernel computational lane: **SOLID** at the stored-polynomial level through k=26 for the imposed-form skeleton; interior content **SOLID at low k, precision-limited at high k** (per recommendation 5).
- Speaking-pair ladder as substrate-Schur-signature: **CONSEQUENCE of imposed form** — not a new banked promotion. Reads n_C three ways; that triple reading is a substrate-natural cleanliness signal but does not enter the audit count as an independent leg.
- Count holds at 4 of 26. Concur with Elie.

## Forwarding actions

1. **Elie:** swap the self-consistency reasoning for the cross-file match (above, target #3), and add the precision caveat to the JSON (target #5). Both are 5-minute edits. No re-audit needed once filed.
2. **Keeper:** when Vol 16 Ch 8 absorbs this, note the gap = C₂ triple anchor (heat-trace + SO(7) Casimir + curvature-equivalent).
3. **Catalog (Grace, no rush):** the stored full-polynomial dataset is new — the previous file (`results_hybrid_3200.json`) kept only a_k(5). Catalog the new full-polynomial artifact as a substrate-architectural primitive.

— Keeper, 2026-06-21 Sun ~08:50 EDT
