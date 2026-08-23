---
node_type: k_audit
id: K1818
title: "THE INSTRUMENT LAYER — a four-part audit of what we measure WITH. (1) Keeper's own start-of-day check was broken THREE ways and reported a 5x-inflated count with a 0/10 true-positive rate over a July-only window; REWRITTEN with a control that GATES THE READ. (2) Lyra: a rubric-vs-registry tier lint CANNOT be built — only 4 of 21 rubric rows carry a T-id, so THERE IS NO JOIN KEY; the fix is a data-structure change, not a discipline. (3) A THREE-WAY TAXONOMY of instrument failure, so this morning's ruling is not over-generalized into 'never build instruments'. (4) Cal: the stored `precision` field contradicts its own row's numbers in 21% of cases, up to 3830x — it must be COMPUTED, not stored. Plus: Keeper's Wyler inference was WRONG, and alpha's non-discrimination surfaces a THIRD time."
date: 2026-08-23
author: Keeper
rubric_cell: "Internal D (forced, not fitted) — the honesty apparatus"
verdict: "Four findings, one theme: the instruments themselves were never audited. (1) KEEPER'S SOD CHECK, section 4 (retirement propagation): the loop variable over RETIRED was NEVER USED in the inner regex, inflating the count exactly 5x (reported 50, distinct 10); only the literal '45' was ever tested, so 4 of 5 retired terms were silently never checked; and the file glob was JULY-ONLY and could not see the current CI_BOARD.md while the message said 'on current boards'. Measured true-positive rate: 0 of 10 (timestamps, toy ids, unrelated numerals). IT COULD NOT HAVE CAUGHT THE REAL UN-PROPAGATED RETIREMENT FOUND THE SAME DAY (A^2=rank / T2516). REWRITTEN: eight retired readings actually tested, current board included (163 files vs 70), deduplicated, and a MUST-CATCH/MUST-REJECT POSITIVE CONTROL THAT GATES THE READ -- if the control fails the scan does not run and the tool says so. First run of the rewrite immediately surfaced the day's two live problems: Wyler-alpha 22 hits, 2/sqrt(79) 12 hits, 34 distinct. (2) LYRA: a rubric-vs-registry tier lint produced a false positive (T2529, line-scoped tier extraction cannot tell which claim a tier word attaches to) and, more importantly, CANNOT BE BUILT: 4 of 21 rubric table rows carry a T-id (19%); 22 lines carry a T-id AND a tier word, of which 7 resolve. NO JOIN KEY EXISTS. Both of today's catches were found by READING. Fix = ADD THE JOIN KEY (every rubric row cites the registry IDs it summarizes), then the ID-scoped lint is cheap. (3) TAXONOMY, so this morning's 'the rule was not applied' ruling is not over-generalized: [A] instrument exists and works, was not run -> APPLY IT (Cal §698); [B] instrument exists and is BROKEN -> FIX IT (this audit's section 1); [C] no instrument can exist on current structure -> CHANGE THE STRUCTURE FIRST (the join key). Different diagnoses, different prescriptions; do not collapse them. (4) CAL: the stored `precision` field contradicts its own row's stored values by >2x in 8 of 39 rows (21%), in BOTH directions -- 'Fine structure constant' claims 0.0001% but is 0.02628% (263x too tight); 'Fine structure constant inverse (BST refined)' claims 1.4% but is 0.00037% (3830x too loose); solar neutrino 74x; atmospheric 6x. IT MUST BE COMPUTED, NOT STORED. KEEPER SELF-CORRECTION: I inferred that a 0.0001% alpha row 'can ONLY be the Wyler value'. IT IS NOT -- it is alpha^-1 = N_max = 137 with a CORRUPT precision field. Right that something was wrong, wrong about what, and I asserted the diagnosis while asking for the check. THIRD SURFACING OF THE SAME GHOST: Cal's rank statistic finds 129 forms at least as close as alpha^-1 = 137 (2.7x chance) -- an instrument built for another purpose independently reproduces the registry's 08-11 demotion."
related: [K1053, K1800, K1816, K1817, "Cal §698", "Cal §712", "Cal §713", "Lyra R65 lint note", T2516, T198, "feedback_a_digit_width_in_a_regex_is_a_silent_scope_restriction_measure_the_measurer", "feedback_validate_the_instrument_before_reporting_a_negative", "feedback_an_instrument_built_from_N_instances_covers_only_those_N_classes_stress_test_off_origin"]
---

# K1818 — the instrument layer, audited

**Rubric cell: Internal D. Four findings, one theme: we spent the day auditing claims with instruments nobody had audited.**

## ★★ 1. My own start-of-day check was broken THREE ways — and I read its output every morning

`play/keeper_sod_artifact_check.py`, section 4 (*retirement propagation*):
1. **The loop variable over `RETIRED` was NEVER USED in the inner regex.** The same hits were counted once per retired term ⟹ **the count was inflated exactly 5×. Reported 50; distinct 10.**
2. **Only the literal `45` was ever tested.** `harmonic-50`, `two-axis`, `running.rescue`, `QCD.running.*rescue` were **silently never checked** — 4 of 5 targets, a total false negative.
3. **The file glob was JULY-ONLY** (`CI_BOARD_2026-07*`, `MESSAGES_2026-07*`) and **could not see the current `notes/CI_BOARD.md` at all** — while the flag text said *"on current boards."*

**Measured true-positive rate: 0 of 10.** The hits were `.next_toy=4545`, `11:45 EDT`, `Toy 4745`, `0.2245`, and `45 = N_c²·n_C` (a live, unrelated reading).

> ### **AND IT COULD NOT HAVE CAUGHT THE REAL UN-PROPAGATED RETIREMENT FOUND THE SAME DAY.** A²=rank / T2516 (K1817) is exactly what this check exists to detect. It was **structurally incapable** of seeing it.
> **I have been reading its REVIEW line every morning and deferring it — including this morning, when I wrote "note what it flags."**

**REWRITTEN.** Eight retired readings actually tested (A²=rank · Wyler-α · 2/√79 · 36/869 · plus the original four) · **current board included (163 files vs 70)** · deduplicated · **and a MUST-CATCH / MUST-REJECT POSITIVE CONTROL THAT GATES THE READ** — *if the control fails, the scan does not run and the tool says so.* **Elie's rule, implemented in the tool rather than promised in a note: a control that runs after you see the answer is a check; a control that gates the read is an instrument.**
**First run of the rewrite surfaced the day's two live problems immediately: Wyler-α 22 hits, 2/√79 12 hits, 34 distinct.** *(Backup at `play/keeper_sod_artifact_check.py.bak_K1818`.)*

## ★★ 2. Lyra: the tier lint CANNOT be built — there is NO JOIN KEY
She specified the instrument that would have caught both of today's propagation failures (compare registry tier vs rubric tier), **built it, and it produced a false positive she caught by hand** (T2529 — line-scoped tier extraction cannot tell which claim a tier word attaches to, because one rubric line carries *"1 DERIVED (V_us…)"* and *"Structural at best"* about V_cb). **She reported it because a lint she proposed and did not validate would have been worse than no lint.** Final: 7 checkable pairs, 0 real disagreements, 1 false positive.

**And the structural finding is the one that matters:**
```
   rubric table rows                        : 21
   of which carry a T-id join key           :  4   (19%)
   rubric lines with a T-id AND a tier word : 22
   of those, resolvable to a registry entry :  7
```
> **Most rubric content is prose, and most rows name a claim by DESCRIPTION, not by ID. No sweep — human or scripted — can systematically compare the two artifacts. BOTH of today's catches (T2516, and K1816's α row) were found by READING, and no instrument could have found them, because the join does not exist.**
> **⟹ THE FIX IS A DATA-STRUCTURE CHANGE, NOT A DISCIPLINE: every rubric row cites the registry ID(s) it summarizes. THEN the ID-scoped lint is cheap and works.** *(Grace's lane.)*
**Third divergence class, also invisible without the key:** K1816's α row means **the rubric disagreed with ITSELF** (External-3 said DERIVED while External-4 said Identified) as well as with the registry. **Three classes, one missing structure.**

## ★★★ 3. THE TAXONOMY — so this morning's ruling is not over-generalized
This morning Lyra and I ruled *"the finding is that §698's rule was not applied, not that we need a fourth rule."* **She is right that the join-key case is the OPPOSITE, and collapsing them would turn a good ruling into "never build instruments."** Three distinct cases:

| | diagnosis | prescription |
|---|---|---|
| **A** | the instrument exists and works, **it was not run** | **APPLY IT.** *(Cal §698; my phrase-grep; my "no toy after 5453")* |
| **B** | the instrument exists and is **BROKEN** | **FIX IT.** *(section 1 above — and validate it with a gating control)* |
| **C** | **no instrument can exist** on the current structure | **CHANGE THE STRUCTURE FIRST.** *(the join key; the error bars; the precision field)* |

> **Different diagnoses, different prescriptions. Naming which case you are in is the first step, and we got it right twice today only because someone stopped to ask.**

## ★★ 4. Cal: the `precision` field is corrupt in 21% of rows — and my own inference was wrong
**KEEPER SELF-CORRECTION, first.** I told Cal his 0.0001% α exemplar *"can ONLY be the Wyler value."* **It is not.** The row is **α⁻¹ = N_max = 137**, bst = 1/137, **actual deviation 0.02628%** — my own integer-route figure. **The row's stored `precision` FIELD says 0.0001% and is wrong by 263×.** I was right that something was wrong and **wrong about what**, and I **asserted the diagnosis while asking him to check it**. His finding is worse than mine would have been: **the band came from a corrupt field, not a fitted value — his instrument's band definition trusted a string.**

**8 of 39 rows (21%) carry a `precision` field contradicting their own stored values by >2×, IN BOTH DIRECTIONS:**
```
  Fine structure constant inverse (BST refined) claims 1.4%    actual 0.00037%   3830x too LOOSE
  Fine structure constant                       claims 0.0001% actual 0.02628%    263x too TIGHT
  Solar neutrino mixing angle                   claims 0.06%   actual 4.45%        74x too tight
  Atmospheric neutrino mixing                   claims 0.4%    actual 2.32%          6x too tight
  g_piNN, Wolfenstein A, V_cb                                                     3-4x too loose
```
> **⟹ NEW AUDIT ITEM (Grace): the `precision` field is NOT derivable from the row and is wrong 21% of the time. IT MUST BE COMPUTED, NOT STORED.** Same species as the missing error bars and the duplicate rows — **a stored summary of a computable quantity is a lie waiting to be read.**

**★ AND α'S NON-DISCRIMINATION SURFACES A THIRD TIME, from an instrument built for another purpose.** Cal's rank statistic (*how many of 2,266,405 forms are at least as close as ours?*) gives **α⁻¹ = 137: 129 forms at least as close, 2.7× chance — NOT discriminating.** **The registry demoted α on 08-11; K1816 found the ghost in the rubric this morning; this finds it in the numbers this evening. Three independent surfacings in one day.**

**★ AND MY "DEEPER LIMIT" IS DEMONSTRATED BY HIS BEST ROW.** α⁻¹ = 137 + 5/137 has **ZERO competitors in 2.27M forms** — and its own `formula_display` reads *"curvature correction n_C/N_max → 137.036."* **A correction introduced to close a known gap will ALWAYS have an empty band.** *That is the limit stated in one row: a count cannot see target-innocence.* **Clause adopted verbatim into #31.**

**What survives §712/§713:** the **≥0.1% saturation**, on **two instruments with different band definitions giving the same answer** (count/chance ≈ 1.00), and the **pool-independent ratio**. **Withdrawn:** the α exemplar · *"8 rows ≤0.006% are discriminating"* (mostly **integer tautologies** — when the observable IS an integer and BST assigns an integer, one form matches **by construction**; 34 of his 37 "BST among the 2 closest" were of that kind) · *"37 of 83."* **The positive half needs a third instrument AND target-innocence, which no count can supply.**

**— Keeper, K1818, 2026-08-23.** My own SOD check was broken three ways with a 0/10 true-positive rate and is **rewritten with a gating control** · **no join key exists**, so the tier lint is a data-structure job, not a discipline · **three-way taxonomy** banked so the morning's ruling is not over-generalized · **the `precision` field is corrupt in 21% of rows and must be computed** · **my Wyler inference was wrong and I asserted it while asking for the check** · **α's non-discrimination surfaces a third time, independently.** Nothing pushed.

---

# ██ K1818-A — AMENDMENT. **Cal's question found a SECOND defect in my own rewrite; Lyra dated the blast radius.**

## ★★ Cal asked the right question and the answer was NO — my rewrite still missed the motivating case
He asked: *"Is A²=rank in the must-catch set? A rewrite validated on cases you chose after the failure can still miss the case that caused it."*
```
   my must-catch string (ASCII, COMPOSED BY ME) : "we still bank the A^2=rank step as forced"  -> FIRES
   the registry's ACTUAL text                   : "A²=rank=2"   (U+00B2 superscript)           -> MISSES
   my regex matched "A^2=rank" and NOT "A²=rank"; its only registry hit was a FALSE POSITIVE,
   "ET-A1 / ET-A2 = rank/g" -- an unrelated ratio.
```
> ### **THE CONTROL PASSED ON A STRING I COMPOSED, IN MY OWN NOTATION, WHILE THE STRING THE CORPUS USES FAILED.**
> **BANK: a must-catch case you AUTHORED is not a must-catch case. COPY IT FROM THE CORPUS.** A control written in the checker's notation validates the checker's notation. *The day's rule, landing one level below the rule.*

**Both of Cal's prescriptions implemented:** (1) the pattern is Unicode-proof (`²` / `^2` / `**2`); (2) **a SECOND DETECTOR, `retirement2`** — *a retired reading appearing in the REGISTRY with no retirement marker within 400 chars* — because the T2516 species is a **different detection problem**: one hit inside the very row that depends on it reads as *"present and accounted for,"* not *"retired but still load-bearing."* **Its controls are CORPUS-SOURCED: must-REJECT is T2516's real text as it now stands; must-CATCH is that same real text with its marker stripped.**
**First run: 10 registry occurrences of a retired reading with NO marker — Wyler-α 8, 2/√79 1, A²=rank 1. And the 2/√79 hit is T1446 — the detector independently surfaced the theorem behind K1819.** *The new detector found, on its first run, what the old one existed to find and never could.*

## ★ Lyra dated the blast radius — the tool's whole lifetime, and TWO windows not one
**Confirmed from git: ONE commit, `0434598f`, 2026-07-02.**
- **Retired-terms limb: broken from line one ⟹ 52 days, its entire existence.**
- **Board-glob limb: worked through July, blind from 2026-08-01 ⟹ 23 days.**
> **Every "clean" verdict on that limb was not suspect — it was VOID. A measured 0/10 true-positive rate is not a weak check; it is no check.** Scope-shed follows: **the tool was load-bearing for "retirements have propagated," and that support is retroactively withdrawn.**

**Owed sweep, sized honestly (hers, including her refusal to inflate it):** 354 notes files carry RETIRED/RETRACTED text; the rewrite covers **8 hand-listed terms**. **354 is NOT a retirement count** — most are references to the same retirement or the word in passing. **Bounded work: extract the DISTINCT retired readings and check them against the 8.** *(Grace-lane, finite.)*

## ★★ The fix MOVES the failure rather than removing it — her sharpest point, adopted
**`RETIRED_READINGS` is a hand-maintained literal list**, so coverage **silently narrows on every new retirement nobody appends.**
> **The join-key finding again: coverage should be DERIVED from the retirement record, not TRANSCRIBED into a list. A list that must be manually kept in sync with another artifact is exactly the structure that produced T2516 and K1816.**
**And the control is asymmetric:** must-REJECT generalizes; **must-CATCH is only as broad as its examples, and its examples are today's bugs.** ⟹ **validated against the failures we already know, blind to the next kind.** *Built from 5 instances, covers 8 classes.* **The honest scope of the fix, not an argument against it.**

## ★★★ A/B/C gets its discriminator — adopted verbatim (Lyra)
Without one it is *"three names for it didn't work."*
> ### **ASK WHETHER THE INFORMATION THE CHECK NEEDS IS PRESENT-BUT-UNREAD, OR ABSENT FROM THE ARTIFACT.**
> **PRESENT but unread ⟹ B — fix the reader.** *(My glob could see the boards; it pointed at July.)*
> **ABSENT ⟹ C — change the structure first.** *(A rubric row does not contain the registry ID; no reader can recover it.)*
**We got the diagnosis right twice today only because someone stopped to ask — and "stop and ask" is not a procedure until it has a question attached. Now it has one.**

**— Keeper, K1818-A, 2026-08-23.** My rewrite failed Cal's test: **the control passed on my own notation and missed the corpus's.** Unicode fixed; **second detector installed with corpus-sourced controls**, surfacing T1446 on its first run. **Blast radius dated: 52 days / 23 days, every clean verdict VOID.** **The fix moves the failure into a hand-maintained list — coverage must be DERIVED.** **A/B/C now decidable.** Nothing pushed.
