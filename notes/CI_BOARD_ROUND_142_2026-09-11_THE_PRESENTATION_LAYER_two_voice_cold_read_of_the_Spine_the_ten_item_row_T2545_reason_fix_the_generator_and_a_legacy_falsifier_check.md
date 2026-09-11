# ROUND 142 — THE PRESENTATION LAYER: cold-read the Spine in both voices, register or retire the ten-item count, fix T2545's reason, re-key the generator, and check one legacy falsifier before anyone quotes it.

**Keeper, 2026-09-11 (Friday) 11:45 EDT.** Casey's assignment this morning: bring Curriculum/ and Guide/ up to date with the corpus, in the BST voice. The audit is K1892 (FAIL as a presentation; one cause — the register moved and the consumer layer did not). The first pass is committed: `BST_VOICE_AND_STYLE_GUIDE.md`; both front doors; a single-source state block; the Spine (`Curriculum/Spine_DIV5_QM_GR_SM/`, Lectures 1, 2, 3, 8 drafted, six scaffolded); 26 legacy chapters corrected in place; SOD section 5. Rubric cell: **External 1–4 as PRESENTED; Internal D on the presentation.** Nothing here goes external until this round's gates clear. NO EOD before 5pm.

**Read first, all of you:** `BST_VOICE_AND_STYLE_GUIDE.md` (one page), then `notes/BST_PRESENTATION_STATE_BLOCK.md` (the single source — if you find a fact wrong in a front matter, fix it THERE and run `python3 play/sync_presentation_state.py`; never in the consumer).

## Assignments

**Cal — C1, C2, C3. Your gate is the one that matters today.**
- **C1 — the two-voice cold-read, Section 455, on Lectures 1, 2, 3 and 8.** Read each narrative lecture against the vetted core (the registry rows and K-audits its `sources:` line names) with your pre-registered tier-inflation checklist (Section 456). The question per sentence: *does the warm sentence claim more than the row it rests on?* Report per lecture: PASS / CONDITIONAL / FAIL, with the sentence quoted and the row it over-runs. Two places I expect you to look hardest: Lecture 2's "unmechanisable within the geometry" (your own §946 words — confirm the lecture's paraphrase of the two obstructions and the maximal-compact argument is exact) and Lecture 3's Born-from-the-edge passage (your §935 tautology caveat is carried — confirm it is carried *undiluted*).
- **C2 — the ten-item count (your §945 ruling).** Lecture 3 quotes "ten of ten" at the tier of its rows, not as a headline, pending your registry row. Either write the row today — ten items, each with tier and dependencies, T2632 candidate — or rule that the count stops being quoted, and say which sentence in Lecture 3 and in the state block must change. One or the other; not a third day of "owed."
- **C3 — the falsifier register vs the Spine's falsifier lines.** Each drafted lecture ends with "what would make this lecture wrong." Check each against the falsifier register v0.4: is every falsifier the Spine names IN the register, and is every register entry that belongs to that lecture's material named? Report gaps both ways.

**Grace — G1, G2, G3.**
- **G1 — T2545 reason-fix (owed since §946).** Right conclusion, wrong ground: the (3,1) signature argument must rest on V₁₂ being the *real* SO(3) vector, irreducible by Jordan structure theory, with the Frobenius–Schur argument that it is not any SU(3) fundamental — not on the real-space premise the row currently states. Annotate the row; hash the text before you post it; edit nothing else.
- **G2 — the register-to-presentation generator.** `data/bst_26_tier_map.json` is dated 07-17 and is itself stale (alpha_inv LAW+ANCHOR; gauge_SU3 SUPPORTED; V_cb 0.044; delta_PMNS). Re-key its 26 rows to the register as of Cal §946 — tier word per the four-word vocabulary (derived / identified / floored / open, with "input" where the ledger says input), row id, date of last re-tier — and emit a markdown table from it. The state block's "8 of 26 sourced clean" must fall out of the file, not be typed. Positive control first: the generator must reproduce your v0.54 count of 8 before it is trusted. When it does, I wire it into `play/sync_presentation_state.py`.
- **G3 — the sub-Tsirelson check (flag, not ruling — yours to rule).** Registry ~line 10603: "SCMP predicts sub-Tsirelson deviation 1/2^N_c = 1/8 = 0.125 in Bell experiments … if measured deviation < 0.125 reliably, SCMP refuted." This falsifier is in Vol 14 and the Curriculum README's old principles list; it is in neither the rubric nor the 08-26 one-pager. Published loophole-free CHSH values sit at the Tsirelson bound $2\sqrt2$ to four digits (pin the primary — Poh et al. 2015 is the one I remember, and I am not quoting its number from memory). If a deviation of 0.125 is excluded by data, the falsifier has FIRED and belongs in Section E (fired and lost) with the same ceremony as K1826 — and every sentence in Vol 14 / Vol 15 that quotes SCMP as standing needs the sweep. Report: fired / not fired / not decidable, with the source pinned.

**Lyra — L1, L2.**
- **L1 — the two theorem-number pins** (owed since 09-08): Stein–Weiss Ch. III §2 theorem number; Zimmer 2.2.20. T2625/T2626 carry them as PIN OWED; Lecture 4's sources will cite them. From the book, not from memory.
- **L2 — read Lectures 1–3 and 8 as the theory author, for FACT not voice** (Cal has the voice). Any sentence where my paraphrase of a theorem is loose — the Peirce split, the multiplicity definition via the roots ½(e_i ± e_j), the genus formula (r−1)a+b+2, Hua's form of the Lie ball, the row-isometry identity — quote the sentence and give the exact one. You have right of dissent on the Lecture 2 sentence naming the one input; if you would write it differently, write both versions and choose neither (the L1 discipline of Round 141).

**Elie — E1.**
- **E1 — one toy, three checks, exact arithmetic:** (i) rebuild the genus of D_IV⁵ from (r, a, b) = (2, 3, 0) and confirm the Bergman kernel exponent by the Round-130 Monte-Carlo route or a closed form — the Guide's Section 7.4 used to say n_C + 1 = 6 and now says 5; make it a posted number, not a sentence; (ii) confirm Lecture 3's branching table (k+3)/(2k+3), k/(2k+3) for k = 0..5 and the chained 3/7 from your 5747 record, not recomputed from the lecture; (iii) the Lie-ball inequalities as Lecture 1 states them (|z·z| < 1 and 1 − 2|z|² + |z·z|² > 0) — sample points and confirm they describe the same set as the corpus's D_IV⁵ definition (T944). Post numbers first, readings second. `/toy claim` before you start.

**Keeper (me) — K1.** Prose for Lectures 4, 5, 6, 7, 9, 10; the 83-line legacy debt (Journey, Predictions Ch01, Forces Ch03 first); dated headers on the untouched core chapters; the Wyler-critique pin. I audit nothing of my own — Cal does.

## Refusal list
- No new tier table typed by hand anywhere. If you need one, it comes from G2's generator or waits.
- No banner. A retired sentence gets rewritten, dated, in the text.
- No "10/10" in any new sentence until C2 lands one way or the other.
- No number from memory in any lecture, correction, or table — pin it or point at it.
- The section sign does not appear in any Curriculum/ or Guide/ file. (Cal's log keeps its own convention.)

— Keeper. Prompt file for Round 142. Board post to follow when the first result lands.
