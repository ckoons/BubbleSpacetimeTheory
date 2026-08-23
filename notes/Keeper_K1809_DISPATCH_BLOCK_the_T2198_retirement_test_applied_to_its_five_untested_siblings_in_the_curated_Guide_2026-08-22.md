---
node_type: k_audit
id: K1809
title: "DISPATCH BLOCK. Elimination-sweep discipline applied: T2198/T2259 were retired because 'the experimental band admits four consecutive integers, three of them BST integers, all indistinguishable.' That retirement is a loaded string — the same standard must sweep everything that shares it. Guide Vol2 Ch02 Sec 7.7 carries FIVE MORE CKM/CP formulas that have never been through that test. Ran it. THREE FAIL OUTRIGHT: gamma = arctan(sqrt(n_C)) = 65.91 deg against 65.5 +/- 2.5 deg admits TEN competing BST-integer forms inside the same band (arctan sqrt of rank*rank, rank*N_c, n_C, c_3/N_c, sqrt(N_max)/rank, and five more); rho-bar = 1/(2 sqrt(2 n_C)) admits 2 competitors (rank/(2 C_2), rank/c_3); eta-bar = 1/(2 sqrt 2) admits 4. THE SHARPEST DETAIL, and it is the one a referee finds first: for eta-bar a competing BST form fits BETTER than the one we publish — sqrt(C_2)/g = sqrt(6)/7 = 0.34993 sits at +0.09 sigma against the published 1/(2 sqrt 2) = 0.35355 at +0.46 sigma. Same integer vocabulary, same simplicity class, roughly FIVE TIMES closer to the measurement. Publishing the worse-fitting member of an indistinguishable family is the exact defect that retired T2198. HONEST CALIBRATION AGAINST MYSELF: J_CKM = sqrt(2)/50000 returned ZERO competitors, and that is NOT a pass — it is UNTESTED. My pool generates simple forms only (a, sqrt a, a/b, sqrt(a/b), a*b, 1/(2 sqrt a)); J's published form is compound, 50000 = n_C^5 * (2^rank)^2, which my pool never reaches. An instrument built for simple forms cannot clear a compound one, and reporting its silence as a pass would be the false-negative error I audit others for. J is UNTESTED at its own complexity class. Also recorded: the PD ledger artifact (grace_CKM_PARTIALLY_DERIVED_explicit_split_ledger_2026-08-22.md) now predates this session's results and is stale in four places — its 2.0-2.6 sigma inclusive/exclusive caveat (V_cb split has WIDENED past 3 sigma, V_ub tension has largely RESOLVED), its epsilon ~ 0.11 and chi-spread [0.36,3.33] (superseded by the forced-complex-chi pin to ~0.090 and [1.09,3.33]), its exclusion list (stops at R55; R57's P=1+epsilon Q and the five sealed candidates are now added), and its DERIVED section (missing today's ORDER result)."
date: 2026-08-22
author: Keeper
verdict: "DISPATCH BLOCKED on the CKM/CP sector until Guide Sec 7.7 is reconciled. Three published formulas FAIL the same test that retired T2198: gamma (10 competing BST forms in band), eta-bar (4), rho-bar (2). eta-bar is the acute case — a competing BST form of equal simplicity fits ~5x better than the published one. J_CKM is UNTESTED, not passed; my pool cannot reach its compound complexity class and I am recording that as a limitation of my instrument rather than a clearance. Severity CRITICAL for dispatch, MODERATE for the corpus — this does not touch the sector's genuine results (lambda = 1/sqrt20, the ORDER, flavor-universality, CP existence, the sealed negative), all of which stand and are unaffected. Recommended action: either retire the three failing rows as T2198 was retired, or re-state them as 'smallest-of-N-indistinguishable BST forms' with N reported — the honest form. The PD ledger also needs a forward-fold on four stale points. Nothing pushed."
---

# K1809 — The retirement that was never swept

**A retirement is a loaded string.** T2198/T2259 were retired because *"the band admits four consecutive
integers, three of them BST integers, all indistinguishable."* That standard was never applied to the
five sibling formulas sitting in the same curated section.

## The sweep — three fail outright

| quantity | published BST form | value | observed | σ | **competing BST forms in the same band** |
|---|---|---|---|---|---|
| **γ (CP phase)** | arctan(√n_C) | 65.91° | 65.5 ± 2.5° | +0.2 | **10** |
| **ρ̄** | 1/(2√(2n_C)) | 0.15811 | 0.159 ± 0.010 | −0.1 | **2** |
| **η̄** | 1/(2√2) | 0.35355 | 0.349 ± 0.010 | +0.5 | **4** |
| J_CKM | √2/50000 | 2.83e−5 | 2.77 ± 0.11e−5 | +0.5 | *(see below — untested)* |

γ's competitors include arctan√(rank·rank), arctan√(rank·N_c), arctan√(c_3/N_c), arctan√(√N_max/rank).
**Ten indistinguishable readings inside one error bar. That is T2198's failure mode exactly.**

## The sharpest detail — and it's the one a referee finds first

> **For η̄, a competing BST form fits BETTER than the one we publish.**

| form | value | deviation |
|---|---|---|
| **published** 1/(2√2) | 0.35355 | **+0.46σ** |
| **competing** √C₂/g = √6/7 | 0.34993 | **+0.09σ** |

**Same integer vocabulary, same simplicity class, roughly five times closer to the measurement.**
Publishing the worse-fitting member of an indistinguishable family is precisely the defect that retired
T2198 — and here it is visible without any BST knowledge at all. A referee only needs a calculator.

## Calibration against myself — J_CKM is UNTESTED, not passed

J returned **zero** competitors. **That is not a clearance.** My pool generates only simple forms
(`a`, `√a`, `a/b`, `√(a/b)`, `a·b`, `1/(2√a)`). J's published form is **compound** —
50000 = n_C⁵·(2^rank)² — a complexity class **my pool never reaches**.

**An instrument built for simple forms cannot clear a compound one.** Reporting its silence as a pass
would be the false-negative error I audit other people for. **J_CKM is untested at its own complexity
class**, and clearing it requires a pool built to that class.

## What this does NOT touch

**Nothing in today's genuine results.** λ = 1/√20 (blind, forward, 0.4%), the ORDER result (corner opens
two rungs later — derived from graph distance, no fitting anywhere), flavor-universality = the
partial-isometry condition, CP *existence*, and the pre-registered sealed negative all stand
**completely unaffected.** This is a defect in older, un-swept curated rows, not in the sector's spine.

**And the contrast is the argument for the new work:** the ORDER result cannot fail this test, because it
uses no fitted integer at all — it comes from counting rungs on P₆.

## Recommended action — two honest options

1. **Retire the three failing rows** as T2198 was retired, or
2. **Re-state them as "smallest-of-N indistinguishable BST forms" with N reported** — the honest form this
   corpus already uses for contested uniqueness claims.

**Option 2 is preferable** where the form is otherwise motivated: it keeps the observation while telling
the truth about its discriminating power.

## Also recorded — the PD ledger is now stale in four places

`grace_CKM_PARTIALLY_DERIVED_explicit_split_ledger_2026-08-22.md` predates this session's results:

- **caveat 1** cites a 2.0–2.6σ inclusive/exclusive tension. **Superseded both ways:** the V_cb split has
  **widened past 3σ**; the V_ub tension has **largely resolved** (Belle ratio 0.97 ± 0.12).
- **caveat 4** quotes **ε ≈ 0.11** and χ-spread **[0.36°, 3.33°]** — superseded by the forced-complex-χ
  pin to **≈ 0.090** and **[1.09°, 3.33°]**.
- **the exclusion list** stops at R55. R57's P = 1+εQ (dead — Q parity-odd) and the **five sealed
  candidates** now join it.
- **the DERIVED section** is missing today's **ORDER** result.

Grace's artifact, Grace's fold. Flagged, not edited.

— Keeper, K1809, 2026-08-22. We retired two rows for admitting indistinguishable siblings and left five
siblings standing in the published layer. The sweep took twenty minutes and one of them fits worse than
its own competitor.

---

# ██ K1809-A — AMENDMENT, 2026-08-23. Grace is right; my staleness finding was itself stale.
**No new K-number.** K1809 recorded Grace's PD ledger as **"stale in four places."** **All four were already folded.** The closing ledger artifact is timestamped **16:39**; **I read the 14:39 checkpoint, which the closing artifact had overwritten two minutes before I opened it.** The other three items were absorbed. **WITHDRAWN in full — Grace owed nothing on that line.**

> **★ BANK THIS (Grace's formulation, adopted verbatim): a staleness audit is itself timestamped, and the artifact underneath it can move inside the same session.** An audit that reads a checkpoint and reports on the artifact is reporting on a *snapshot*, not the object. **Fix: stamp the read, and re-stat the file at write-time before publishing a staleness finding.** This is the same family as today's authored-predicate failures — the checker's own instrument carried an unstated scope, here a *temporal* one rather than a lexical one.

**What K1809 got right and still stands:** the T2198 retirement standard was never swept across its siblings — **γ = arctan(√n_C) admits TEN competing BST-integer forms in the band; η̄ = 1/(2√2) admits FOUR, one (√6/7, +0.09σ) fitting ~5× BETTER than the published form (+0.46σ); ρ̄ admits TWO; J_CKM = √2/50000 is UNTESTED, not passed.** Those remain dispatch-blocking until retired or re-stated as *"smallest-of-N indistinguishable BST forms," N reported.*

**Also cleared 2026-08-23:** Grace has filed the **T2198/T2259 retirement markers** in the registry and the graph (both duplicated arrays marked; backups taken) — **owed four rounds, now paid.** And her elimination sweep caught a live namesake: **T2265's "BR(ψ(2S)→J/ψππ) = 7/20 — SECOND multi-role appearance"** loses its first appearance (T2259's η̄ row) to the retirement, so **7/20 has ONE appearance and is not multi-role**; re-scoped to a single observational coincidence whose band has never been swept. **Second firing in a week of [[feedback_a_retirement_is_a_loaded_string_sweep_both_directions_and_geometry_forces_a_contingent_fact_is_its_own_class]] — killing a string voids its live namesakes.** Clean work, correctly bounded.

**— Keeper, K1809-A, 2026-08-23.** My "stale in four places" WITHDRAWN (I read a checkpoint two minutes after it was superseded); the sibling-sweep block STANDS; Grace's retirement markers and namesake sweep ACCEPTED. Nothing pushed.

---

# ██ K1809-B — AMENDMENT, 2026-08-23. Cal §705 CLEARS the block, and CORRECTS my remedy. Accepted in full.
**No new K-number.** K1809 offered two remedies: **retire, or re-state as "smallest-of-N indistinguishable BST forms" with N reported.** **Cal is right that Option 2 is not available here, and the reason is exact:**

> **"Smallest-of-N indistinguishable forms, N reported" presupposes an ENUMERABLE FAMILY and a MEANINGFUL CHOICE. Both are false when N is simply what CHANCE supplies. Naming N then dresses noise as bounded ambiguity.**

**That is a real defect in my own ruling and I withdraw Option 2 for saturated bands.** It remains valid where the family is genuinely small and enumerable — which is precisely what a null model is needed to establish, and K1809 did not run one.

## What Cal added that K1809 lacked: THE NULL
My sweep counted competitors. **A competitor count is not a verdict until you know how many competitors chance supplies.** Cal reconstructed my 219-value simple pool (reproducing my counts within one: γ 11 vs my 10, ρ̄ 2 vs 2, η̄ 3 vs 4), then swept **five sampling ranges plus an independent local-density estimator** sharing none of the first one's free choices:

| row | in band | chance | local density | surprising? |
|---|---|---|---|---|
| γ | 11 | 6.9–10.9 | 8.3 | no |
| ρ̄ | 2 | 3.1–5.2 | 3.3 | **below chance** |
| η̄ | 3 | 1.4–2.4 | 2.3 | no |
| J_CKM | 41 | 35.7 | — | no |

**★ J_CKM IS NOW TESTED** — Cal built the compound class my pool could not reach (numerator {1, a, √a, a·b}; denominator c^d·e^f over the BST integers plus N_max; **5458 distinct values**), **positive-controlled so that the published form is in the pool** (it catches its must-catch case). **41 in-band competitors vs chance 35.7; 11% of random bands do as well or better.** Best competitor **√N_c/(rank^rank·n_C^C₂) = 2.7713e−5 at +0.01σ** against the published **+0.53σ**. **K1809's "untested, not passed" was the right call; it is now tested, and it is saturated.**

## ★ THE DISTINCTION THAT RESOLVES IT — two different questions a count answers (Cal, adopted)
- **SURPRISING?** (count vs chance) — **no, all four.**
- **DISCRIMINATING?** (absolute count; ~1 form is informative, 2/3/11/41 are not) — **no, all four.**

> **⟹ The defect belongs to the COMPLEXITY CLASS, not to any individual row.** At J's own complexity class, **~36 BST forms sit inside every error bar in that decade.**

## AMENDED VERDICT — uniform, not per-row
- **RETIRE γ, η̄, J_CKM.** Option 2 unavailable (saturated bands).
- **ρ̄ comes OFF the fail list** — 2 where chance gives ~3. **But two is not one: describe it as NON-DISCRIMINATING, not failed.** *(A narrowing that removes a row from a fail list does not promote it to evidence.)*
- **η̄'s decisive indictment needs no null at all:** **√C₂/g = 0.349927 at +0.09σ beats the published 1/(2√rank) at +0.46σ.** A referee needs a calculator, not a model.
- **UNTOUCHED, and stated so it travels:** λ = 1/√20 (blind) · **the ORDER result — it cannot fail this test, there is no fitted integer in it** · flavour-universality · CP existence · the sealed negative.

## ★ Cal's self-catch, and the rule it earns
His first pass fixed one null sampling range and reported *"η̄ is the one real anomaly, +1.41 sd."* **It did not survive varying the range.** He stated the self-catch **before** the result it corrects.

> **BANK: a null with a free sampling range is not a null until you sweep it. A null you built this session is a candidate false-negative machine exactly like an instrument you built this session — cross-check it with an estimator sharing none of its free choices.**

**This is the day's rule arriving at a third door.** Cal put the free-parameter objection to me on the Lane-B exponent in the morning and found the same error in his own null within the hour. **Keeper, Elie, and Cal each shipped one this round; each was caught by someone else, and one — Elie's — was caught by its own author first.**

**— Keeper, K1809-B, 2026-08-23. K1809 CLEARED for Casey GO with the amended verdict: RETIRE γ/η̄/J_CKM; ρ̄ non-discriminating, off the fail list; Option 2 withdrawn for saturated bands; the defect is the complexity class, not the rows.** Cal's scripts remain his; counters are the toy-owner's authority and nothing is claimed as a toy. Nothing pushed.

---

# ██ K1809-C — AMENDMENT, 2026-08-23. **K1809's HEADLINE FINDING REVERSES.** Cal caught it; Keeper verified; the root cause is duplicate rows in the data layer.

**No new K-number.** **The single most-quoted line of K1809 is target-dependent and it flips.**

## The finding that reverses
K1809 said, and it has since travelled into the rubric, the board, MEMORY.md and Grace's flagship v1.0: ***"for η̄ a competing BST form fits ~5× BETTER than the published one."*** **That holds ONLY against the Guide's 0.349 ± 0.010 and REVERSES against the data layer's 0.357 ± 0.011.** Keeper-verified:

| form | vs 0.349 ± 0.010 (Guide/K1809) | vs 0.357 ± 0.011 (data layer) |
|---|---|---|
| √C₂/g = √6/7 = 0.349927 | **+0.09σ ← "the better competitor"** | −0.64σ ← **LOSES** |
| √N_c/n_C = √3/5 = 0.346410 | −0.26σ | −0.96σ |
| **1/(2√2) = 0.353553 — PUBLISHED** | +0.46σ | **−0.31σ ← WINS** |
| 5/14 = n_C/(rank·g) = 0.357143 | +0.81σ | **+0.01σ ← nearly exact** |

**Against the data layer's own target the PUBLISHED form beats the competitor, and the data layer's own form 5/14 is nearly exact.** ⟹ **THE LINE CANNOT BE PUBLISHED UNTIL THE TARGET IS PINNED to a named PDG determination with an error bar. HELD out of the flagship in both directions.**

**Same disease on ρ̄** (Guide 0.159 vs data layer 0.150: against 0.159, 1/(2√10) is −0.56% and 3/20 is −5.66%; against 0.150, 3/20 is 0.00% and 1/(2√10) is +5.41%) **and on J** (published +0.53σ → **−2.80σ**; best competitor +0.01σ → **−3.43σ** — the ordering reverses there too, and at the current target the published form is the better of two bad ones). **In every case each form is paired with the target that flatters it.**

## ★ THE ROOT CAUSE, found and quantified — duplicate rows in `data/bst_constants.json`
Not "two stored values" — **the file carries DUPLICATE ENTRIES FOR THE SAME OBSERVABLE. 10 duplicate groups; 5 with CONFLICTING TARGETS:**

```
  "Wolfenstein eta-bar"     obs 0.349     tier S  |  "CKM Wolfenstein eta-bar"  n_C/(rank*g)=0.3571  obs 0.357  tier S
  "Wolfenstein rho-bar"     obs 0.159     tier I  |  "CKM Wolfenstein rho-bar"  N_c/(rank^2 n_C)=0.15 obs 0.150 tier I
  "CP phase"                obs 1.15      tier I  |   N_c*pi/g = 1.3464          obs 3.44   tier C   <-- differ by ~3x
  "proton magnetic moment"  obs 2.7928474 tier D  |   rank*g/n_C = 2.8           obs 2.793  tier I
  "alpha particle binding"  obs 28.2957   tier I  |   c_2*n_C*m_e = 28.1         obs 28.3   tier I
```
plus the **three tier-D Cabibbo forms** (K1801-A) and a **V_cb retired in the data layer but still printed in the Guide.**

> **AND: 193 of 197 constants carry NO ERROR BAR on `observed_value` at all. No one — me first — may quote a σ from that file until they do.**

**This is a bounded, fixable, five-row defect that is actively producing contradictory published claims. It is NOT the whole-graph cleanup K1043 ruled out of the papers gate, and I am scoping it IN on that basis.** Grace's lane.

## ★★ WHAT SURVIVES, AND WHY — this bounds how much has to be redone
**Cal's saturation verdicts are COUNT-based, and his density control measured that in-band counts are near-constant across band centres in that decade.** ⟹ **SATURATION IS TARGET-INDEPENDENT BY CONSTRUCTION.**

- **STANDS UNCHANGED:** γ, η̄, J are **saturated**; ρ̄ is **non-discriminating**; **retire the three.** *The retirements rest on the counts and do not need the σ's.*
- **FALLS:** **every σ and every "competitor X beats published Y" ordering** in K1809, K1809-B and §705. **Re-quote with the target NAMED, or drop.**
- **TIGHTENS FURTHER, unchanged:** §707/T1449 — all counts are **lower bounds** (adjacency vocabulary, ×14–26).

> ### **THE LOOK-ELSEWHERE IS THREE-DIMENSIONAL: {form} × {adjacency} × {target}. K1809 found the first, §707 the second, §708 the third. THEY MULTIPLY.**

## ★ BANKED — the day's cleanest rule
> **A competitor COUNT is target-independent; a competitor RANKING is not. Any finding that compares two forms by FIT QUALITY inherits every uncertainty in the target — so PIN THE TARGET BEFORE THE COMPARISON, not after.**
> **Corollary, and it is why so little had to be redone: count-based instruments survive a target revision; fit-quality instruments do not. Prefer the count.**

**Cal's own accounting, recorded because it is the same lesson one level up:** he checked η̄'s independence from **his null's sampling range** and never from **the target** — *one round after* telling me that **the invariance exhibited is not the invariance at risk** (§706 item 1). Same error class, his own document. **Mine is worse: I wrote the finding, and it travelled into four artifacts before anyone checked which target it stood on.**

**— Keeper, K1809-C, 2026-08-23.** K1809's headline η̄ finding **REVERSES** and is **HELD** pending a pinned target; ρ̄ and J reverse likewise; root cause is **5 conflicting-target duplicate rows** in `data/bst_constants.json` plus **193/197 rows with no error bar**; **the saturation verdicts and the three retirements STAND on the counts**; every σ in K1809/K1809-B/§705 must be re-quoted with its target named or dropped. Nothing pushed.
