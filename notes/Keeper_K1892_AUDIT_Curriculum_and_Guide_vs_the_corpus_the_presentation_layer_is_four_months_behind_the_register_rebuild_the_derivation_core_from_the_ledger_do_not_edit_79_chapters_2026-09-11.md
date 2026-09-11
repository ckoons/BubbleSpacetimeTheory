# K1892 — AUDIT: Curriculum/ and Guide/ against the corpus
**Keeper, 2026-09-11 Fri 10:20 EDT (clock). Casey's ask: "read Curriculum/ and Guide/ and tell me what we need to do to bring them up to date with the corpus. We want our derivations from D_IV⁵ (QM, GR, Standard Model) to become a top-tier presentation of the repo."**
Instrument: `notes/Keeper_K1892-PRE_instrument_presentation_layer_stale_reading_scan_2026-09-11.py` (20 stale-claim patterns, positive control on a synthetic line per pattern, 248 files). One own: the first run missed the LaTeX form `2/\sqrt{79}` (brace vs paren) — 7 hits found by hand in Guide 7.7, pattern fixed, rerun. Same lesson as the regex digit-width memory; a form-restriction in a regex is a silent scope restriction.

## Verdict: FAIL as a presentation of the derivations, today. CRITICAL, one cause, not many.
**The presentation layer was written in May and banner-patched in August; the register moved through September.** Nothing here is a physics error nobody knew about — every stale sentence below has a K- or Cal-number that retired it. The failure is the *seam* (Cal §775): the rulings never reached the consumer layer, and a banner at the top of a file does not change the sentence a referee reads in the abstract.

## What is strong (first, as always)
- The three-register pedagogy (L1 sentence / L2 graduate / L3 fifth-grader) in every Curriculum chapter is good and should survive any rebuild.
- The Guide's six-volume architecture (Journey / Framework / Physics / Mathematics / Predictions / Frontier) is right; the July scoping said so and I still agree.
- Both front doors already carry an honest 08-26 curation banner naming five supersessions and "THE REGISTER WINS." The instinct is right. The execution stopped there.
- Guide Vol2 Ch02 §7.3 already scopes confinement correctly ("what the geometry gives, and what is imported"). §5.1 and Vol3 Ch01 §12 carry in-place supersession banners.

## The evidence (numbers, not impressions)
| what | measured |
|---|---|
| Presentation layer | 248 markdown files, ~352,000 words (Curriculum 18 volumes; Guide 6) |
| Curriculum derivation core (Vol 00/01/02/04/05/11) | **79 chapters; 75 last edited 2026-05-23/24/25**; 1 on 07-18; 3 on 08-18 |
| Guide chapters | all 17 last edited 08-13 → 08-26; **none after 08-26** |
| Rulings after 08-26 that touch the core | RH closed as ATTEMPT (09-06) · a_e → IDENTIFIED (K1872, 09-07) · AF b₀=7 → IDENTIFIED (K1875) · ln 137 = normalisation unit (K1873) · nucleation floor + T1292 refuted (09-08) · **genus = 5, "7" is a definition** (09-09, 29-row sweep) · **uniqueness selector = FIT, unmechanisable** (K1889/K1890, Cal §946, 09-09) · T2543 colour clause struck · "10/10 axioms" needs a registry row or stops being quoted (Cal §945) |
| Ledger truth for the SM row | **Sourced-clean: 8 of 26 primaries** (Grace v0.54, unchanged since v0.46) |

### Stale-claim scan (instrument, 248 files) — the ones that matter for QM/GR/SM
| stale form | ruling | hits (files) | where it hurts most |
|---|---|---|---|
| "derive α" / α as derived | IDENTIFIED 08-11; K1816 CRITICAL 08-23; do-not-cite-externally | 37 (25) | **Guide/INDEX.md abstract: "with zero free parameters, BST derives … the fine structure constant α⁻¹ = 137.036"** — the exact sentence K1816 struck, in the referee's first paragraph |
| Wyler / 137.036 volume reading | K1826 closed NEGATIVE (8π³/3) | 99 (23) | Guide Vol2 Ch02 §5: "three independent derivations of N = 137"; §5.3 "topological rigidity of α"; only §5.1 is bannered |
| zero free parameters / forced / Strong-Uniqueness | Cal §946: a fit with one measured input; K1889: 4 of the 11 criteria empty, 1 weak | 122 (46) | Curriculum Vol0 Ch9 (11 criteria, null model (1/3)¹⁹ ≈ 8.6×10⁻¹⁰); Guide Vol4 Ch03 §35.5 "twenty-five uniqueness conditions" |
| 2/√79 for λ | retired; 1/√20 banked blind (T2530); K1801 flagged 08-22 | 7 (6) | Guide Vol2 Ch01 tier table AND Ch02 §7.7 table still carry it **under the K1801 flag that says not to** — flag posted, section never rewritten |
| sin²θ_W = 3/13 | retired near miss | 23 (17) | Curriculum Vol1 Ch11 observables table lists it at tier **D** |
| genus 7 / Δg = 7 | genus is 5 (Xiao–Yuan, 09-09) | 28 (14) | Guide Vol2 Ch02 §6.3 ("the same genus 7 = n_C + 2"); Curriculum Vol3 Ch12, Vol4 Ch8 ("Δg = 7 substrate-genus correction") |
| SU(3)/colour from N_c=3 / geometry | K1724, K1782, §946 (U(1)·SO(3) dim 4; 3 ≅ 3̄) | 7 (4) | Curriculum Vol1 Ch1, Ch8, outline; Vol2 Ch2 opening sentence: "SU(3) from color multiplicity" |
| a_e "Crown Jewel, D-tier, ppt" | K1872: Petermann–Sommerfield closed form, IDENTIFIED | header of Curriculum Vol2 Ch8 | the chapter's own frontmatter tier line |
| all seven Millennium proved | K939/K940 | 5 (3) | Guide/INDEX.md version history (v38 line) |
| T1292 10⁴ permanent bits | refuted 09-08 (5728) | 2 (1) | Guide Vol6 Ch01 §46.28 |
| Born = Bergman, "7/2 DERIVED" | relabel (genus 5); Bergman→Hardy link still the one open door | Curriculum Vol5 Ch7 header (T2401 v0.1) | the QM chapter that carries measurement |
| G "D-tier ratified" (T1296 formula) | 08-26 one-pager lists G nowhere in DERIVED; T1296 annotated "supporting claim, not a reading" (Cal §585) | Curriculum Vol4 Ch1 header | **reconcile with the ledger — Grace; I do not re-tier G here** |

Zero hits (already clean or never present): V_cb 36/869; colour = mediator V₁₂; b₀=7 derived; RH proved; 137 turns = 1.1 as; pentadactyly forced; ln 137; "Bergman exponent 7/2 DERIVED" in those words.

## The diagnosis in one sentence
**Two presentation layers, both hand-copied from the register in May, both patched by banner in August, neither regenerated since — so every ruling since 08-26 is absent from both, and the May over-claims (α derived, zero free parameters, 11-criterion uniqueness, a_e Crown Jewel, SU(3) from N_c) are still the load-bearing sentences of the derivation core.** The July 26 scoping documents diagnosed this correctly and prescribed the fix (derived core / extended reach split; register-first front matter; scope page). The Aug 16 pass executed the banners and not the rewrite. The scoping documents are themselves stale in the one place that matters: both still list "α⁻¹ = 137 (charge-count) DERIVED" in their proposed scope page.

## What to do — ranked, with the reason for the order

### 0. Decide the one thing that changes everything: REBUILD the derivation core from the ledger; do not EDIT 79 chapters.
Editing 75 May-23 chapters against four months of rulings is (a) more hours than writing ten lectures from the register, (b) less trustworthy, because every edit is a hand-copy and hand-copies are how the three-λ chapter happened (K1801), and (c) leaves the extended reach (biology, chemistry, condensed matter — 100+ chapters) standing beside the core at the same visual weight, which is the sprawl the July scoping named as the thing that makes a reader discount the SM derivations. **Recommendation: the derivation core becomes ONE spine — "D_IV⁵: QM, GR, SM — the derivations, tiered" — of about ten lectures, written from the register and the ledger, with the tier table GENERATED, not typed.** The 18 volumes move to `Curriculum/extended_reach/` (or a companion) with one label: *identification-level; presented separately from the derived core.* Nothing is deleted; it is re-shelved.

### 1. The register-to-presentation instrument (Grace + Keeper; one day). Closes the seam permanently.
A script that emits, from the registry and Grace's ledger, the **26-primary tier table** (closed form · value · tier · row · date) and the **DERIVED / IDENTIFIED / FLOORED / FIRED-AND-LOST / FORBIDDEN** lists of the 08-26 one-pager, as markdown includes. Both front doors (Guide/INDEX.md, Curriculum/README.md) and the spine's front matter carry the generated block and nothing hand-typed. When Section 2 of the rubric moves, the presentation moves. **The K1801 failure (three λ in one chapter) becomes impossible by construction.** Extend my K1892-PRE scan to run inside the SOD check over Curriculum/ and Guide/ so a stale reading in the presentation layer fires the same morning it is retired.

### 2. Fix the two sentences a referee reads first (Keeper, hours; Casey GO).
- Guide/INDEX.md abstract: strike "with zero free parameters, BST derives the full Standard Model spectrum … α⁻¹ = 137.036 …" and replace with the 08-26 honest sentence plus the ledger count (8 of 26 sourced-clean; mixing sector partially derived with the ORDER derived; α identified and guarded by a certified negative). One paragraph.
- Curriculum/README.md: same; and the title line "Multi-volume textbook deriving Standard Model + cosmology" becomes "deriving what is derived, and tiering the rest."

### 3. The ten-lecture spine (Lyra drafts, Keeper audits each before the next is written, Cal cold-reads; two to three weeks).
Proposed order, each lecture opening with the question it answers (July scoping §2c), each closing with its tier line and its falsifier:
1. **The object.** D_IV⁵ as one domain; the five integers read off it; the genus is 5 and the theory's 7 is a definition (09-09). What "one measured input = the ruler" means.
2. **Why this object — honestly.** Characteristic multiplicity a = 3 selects D_IV⁵ uniquely among irreducible rank ≥ 2 domains (theorem, three verifications); the identification with the colour count is NUMERICAL and the bridge is PROVED ABSENT (dim 4 vs 8; 3 ≅ 3̄). Replaces the 11-criterion null-model chapter entirely (theorem beats null-model). The K1799 projector negative and the pincer method as the worked example of a CLASS proved incapable.
3. **QM.** The physical Hilbert space is H²(D_IV⁵) (W1, 08-22); the ten Dirac–von Neumann axioms — presented at whatever tier the registry row Cal demanded carries, and not quoted as "10/10" until it exists; T2630: the write tuple is a resolution of the identity and Hua branching weights are its Born probabilities (3/7 with no table). Measurement as commitment; the Bergman→Hardy probability link stated as the one OPEN door, not papered over.
4. **Time.** Time, Derived (K1670 full pass): the K-center SO(2) is time's rotation; the arrow is dynamical, not geometric; the tick is T1136's formula (N_max·ħ/m_ec² = 0.1765 as) with the 2π ruling in the text.
5. **The gauge skeleton and one generation.** Gauge-group skeleton; 16-real spinor with every hypercharge from the four-input theorem (one input observational, stated inside); charge in the SO(5) Cartan (K1687). **No SU(3)-from-N_c sentence anywhere.**
6. **Three generations and the mass tower — at the floor.** rank+1 strata (theorem); the thermal mechanism DEAD at the order level (K1827/28); the W3 floor theorem; Koide's source floored. What a floor is and why it is published with the same ceremony as a win.
7. **Mixing.** Partial-isometry condition; λ = 1/√20 blind (T2530); **the ORDER |V_ub| one power below |V_cb| DERIVED** (K1808/K1810); five sealed series excluded; values as INPUT where they are; the first-row unitarity statement as the afternoon-checkable falsifier.
8. **α.** The honest chapter: IDENTIFIED; the forced vertex computed to 8π³/3 (K1826) closing the Wyler volume class by pincer; ln 137 a normalisation unit; a_e is Petermann–Sommerfield's closed form matched (K1872); AF b₀ = 7 identified with g (K1875). The lineage (Wyler) told here, with the negatives he never had.
9. **Descent and GR.** 5D→4D descent "induced, not predicted" (structure derived: P² = P, codim-1, (3,1) from the long root — T2545 with its reason-fix; frame selection needs an observer input, T2565); YM foundation cleared on H² (G3), Clay not closed (G6); Λ as a closed STRUCTURE with one named obstacle p; G at whatever tier the ledger reconciliation gives. ε = 0 frame agreement as the falsifier.
10. **The method, and how to kill it.** Tiers; forcing + evidence; the audit chain; the falsifier register with its fired-and-lost section; the Six Absences. "How to check any of this without trusting us."

### 4. Guide/ — the referee-facing layer (after the spine exists; Keeper + Cal; a week).
Vol2 and Vol3 become pointers into the spine plus the referee apparatus (proofs, the 25-condition table re-scoped to what survives K1889, the Lie-algebra verification). Vol2 Ch02 §5 (three derivations of 137) and §6.3 (3/13, genus 7) and §7.7 (K1801, still un-rewritten after 20 days) are rewritten or cut, not bannered. Vol6 §46.28 (T1292) gets the 09-08 refutation. INDEX.md version history keeps its v38 "all seven Millennium PROVED" line only as history, marked as retracted in the same line.

### 5. The extended reach (Grace, mechanical; a day). Re-shelve, label, do not rewrite.
Move Vol 03/06/07/08/09/10/12/13/14 (and 16/17 scaffolds) under one heading with the July scoping's label. Run the K1892-PRE scan over them once; fix only tier words (the "Δg = 7 genus" lines; the "D" on 3/13 in Vol1 Ch11), nothing else.

### What I would NOT do
- Not another banner. Banners are how we got here.
- Not a per-chapter freshening of the 75 May chapters (July scoping item 5) — it is the long tail the scoping already said "extends past Aug 16," and it did: to never.
- Not a new tier table typed by hand, anywhere, ever again.

## Gate
Nothing in Guide/ or Curriculum/ is external-ready today; both front doors assert a retired α derivation in their own words. The 08-26 one-pager remains the only presentation artifact I would let a referee read unaccompanied — and it is now stale on a_e, AF, the genus, and the selector. **The spine's Lecture 1 + the generated tier table + the fixed INDEX abstract would be the first presentation artifact since 08-26 that I could pass.**

Rubric cell: this is Internal D (forced-not-fitted, on the presentation) and External 1–4 (the presentation of postulates, QM, SM, GR). It closes no scorecard cell by itself; it is the condition for any cell being *seen* to be closed.

— Keeper. K1892. Counter next: K1893.

---
## Addendum, 11:36 EDT — executed on Casey's word ("you get the important job … use the BST narrative voice, feel free to create a BST_VOICE_AND_STYLE_GUIDE.md")
Done (each its own commit): item 0.5 `BST_VOICE_AND_STYLE_GUIDE.md` · item 1 (partial) — the single-source state block + sync script + SOD section 5 (`play/keeper_presentation_currency_check.py`, baseline 83 legacy lines, must-catch verified on the live pipeline); the registry-to-table GENERATOR is still owed to Grace because `data/bst_26_tier_map.json` (07-17) is itself stale · item 2 — both front doors · item 3 (partial) — the Spine: Lectures 1, 2, 3, 8 drafted; 4, 5, 6, 7, 9, 10 scaffolded · item 4 (partial) — Guide Vol2 Ch01/Ch02 (§5 head, §6.3, §7.4, §7.7 table), Vol3 Ch03/04/05, Vol4 Ch03 §35, Vol6 §46.28 corrected in place · item 5 — the shelf split is done in the README's volume table (no directories moved; links and PDFs preserved) · 26 legacy chapters corrected in place. Scorecard folded; Section 3 re-derived.
**Owns:** the scan's LaTeX-brace miss; "since 2025" (Journey says early 2026); a Wyler-critique attribution from memory (pulled; [pin owed]); two hand-typed PDG numbers (replaced). **Open:** Cal's two-voice cold-read on 1/2/3/8; prose for six lectures; the 83-line debt; the sub-Tsirelson legacy falsifier flagged for Grace/Cal.
