---
title: "Keeper Textbook Reading Notes v0.1 — Cross-Volume Substance Observations"
author: "Keeper"
date: "2026-05-23 Saturday ~14:46 EDT"
status: "v0.1 — Keeper-lane reading pass; sampled strategically across 16 volumes, NOT line-by-line full read"
purpose: "Drive a team prompt for text-update work that addresses real substance issues, not process management"
---

# Keeper Textbook Reading Notes v0.1

## Scope of this reading pass (honest disclosure)

I sampled the curriculum strategically — I did NOT read all 216 markdown files line-by-line. Concretely:

- **Deep reads**: Vol 0 Ch 1, 2, 7, 8 (substrate-foundation density check); Vol 1 Ch 1 (entry framing); Vol 2 Ch 6 (Crown Jewel m_p/m_e); Vol 15 Ch 8, 10, 11, 12 (chapters I co-authored)
- **INDEX file reads**: Vol 3, 4, 6, 11 (scope + cross-link structure)
- **Directory scans**: Vol 5, 7, 13 (chapter inventory + filename conventions)
- **Already in Keeper context from prior sessions**: Vol 0 INDEX + Architectural Scaffold + Vol 3+4+14+15 INDEX/Scaffold (Keeper-authored)

This is sufficient to identify **substantive cross-volume patterns** but not sufficient to catch every per-chapter line-level issue. Phase 2 Cal cold-read sweep (Calibration #24 8-dimension checklist) is the right tool for line-level catches; this Keeper pass is for the structural patterns Cal's per-chapter mode cannot easily see.

## Quality state — honest baseline

Where I read in depth, the substance is **genuinely strong**:

- **Vol 0 chapters** (Lyra-led): 3-level pedagogy applied, tier discipline visible, ratified-state count compliant with Calibration #19, cross-volume references functional
- **Vol 2 Ch 6 Crown Jewel**: lead-with-theorem structure, match precision explicit, calibration_compliance metadata in front matter, tier label honest
- **Vol 15 chapters** (Keeper+Lyra+Cal-authored): substance floor compliant per Calibration #23 Rule 23.1, falsifier sections present, cross-volume bridges explicit

The curriculum is NOT at template-stub state for the chapters I sampled. Cal #104 caught the template-stub failure mode in Vol 10+11; Lyra refilled at 1.66 min/chapter PASS substance floor; subsequent Cal #105/#106/#107 cold-reads validated.

**This means the team prompt should NOT be "write more substance" — it should be "address specific cross-volume drift + pedagogy consistency + reader-onramp gaps that the rapid sub-PCAP build accumulated."**

## Observations (substantive, actionable)

### Observation 1 — Status field bloat is reader-hostile

Front-matter `status:` fields now carry full version history strings like `"v0.1 chapter-grade content draft per Calibration #23 Rule 23.1 substance floor"` plus inline references to Cal #99 + Cal Mode 7 + Calibration #19. This is **excellent provenance for Keeper + Cal but distracting for a reader**.

**Recommendation**: Move version-history strings to a per-volume `VERSION_HISTORY.md` appendix. Front matter keeps a clean `status: "v0.1 first-draft chapter content"` plus `last_audit: K169 Lyra+Keeper 2026-05-22`. The K-audit reference is the audit trail; the verbose status line is not.

### Observation 2 — Reader-grade pedagogy depth varies across volumes

Vol 2 Ch 6 reads cleanly at three levels. Vol 0 Ch 7 (Operator Zoo) is dense graduate-level throughout with Level 3 (5th-grader) section thin or absent. Vol 15 chapters (mine) consistently have Level 1/2/3 split but Level 3 quality varies — Vol 15 Ch 12 Level 3 is good, Vol 15 Ch 8 Level 3 is shorter.

**Recommendation**: Pass over Level 3 sections specifically. Each Level 3 should be 50-150 words explaining the chapter's essence to a bright high-schooler without jargon. This is Casey's "Write for 5th graders too" standing rule (`feedback_fifth_graders.md`). Lyra Tier 2 sweep target.

### Observation 3 — "BST primary integer" language re-explained per chapter

The five integers + their meanings get re-introduced in many chapters. This was probably correct when chapters were drafted independently — each had to stand alone. Now that there are 16 volumes with 192 chapters, **re-introduction in every chapter is friction**.

**Recommendation**: Vol 0 Ch 2 (Five Integers + N_max) becomes the canonical reference. Other chapters cite "Five BST primaries: rank=2, N_c=3, n_C=5, C_2=6, g=7 (Vol 0 Ch 2)" once at chapter top + assume reader has the binding from here on. Saves space + standardizes the citation.

### Observation 4 — Crown jewel showcases need explicit "why this matters" pedagogy

Vol 2 Ch 6 (m_p/m_e = 6π⁵, 0.002% precision) IS the crown jewel — it's the result that converts physicists. But the chapter doesn't open with "this is the result that makes everything else worth reading." It opens with the formula + match precision, which is mathematically clean but pedagogically understated.

**Recommendation**: Vol 2 Ch 6 + Vol 0 Ch 9 (Strong-Uniqueness) + Vol 4 Ch 1 (Newton's G from Bergman curvature) + a_e ppt chapter wherever it lives should each carry an explicit "Why this chapter matters" opening paragraph that names the crown-jewel status. Lyra+Elie lane Tier 1 — these are the chapters that recruit readers.

### Observation 5 — Cross-volume forward references work; back references are thinner

Vol 0 references Vol 4, Vol 7 (forward). Vol 2 references Vol 0 prerequisites (back). But Vol 6 (Thermodynamics) is supposed to load-bear Vol 1 Ch 10 (substrate-tick GF(128)^k) — does Vol 1 Ch 10 have a "see Vol 6 for thermodynamic register" forward reference? My sampling did not confirm this. Likely many forward references are missing because newer volumes (3-15) reference older volumes (0-2), but older volumes pre-date the newer ones and don't yet point forward.

**Recommendation**: Grace catalog backbone pass over Vol 0+1+2 to add forward references to Vol 3-15 where applicable. This is mechanical but high-value for reader navigation.

### Observation 6 — Calibration #19 ratified-state count drift risk persists

Cal #106 caught 17 stale Strong-Uniqueness count instances across Vol 0+1+2. Lyra absorbed. But the curriculum was built in waves; later-wave chapters may have inherited the canonical count from in-flight references, while earlier-wave chapters had the stale count baked in. Phase 2 cross-volume audit (Calibration #24 Dimension D) should sweep this specifically.

**Recommendation**: Grace + Cal joint pass — `grep -r "Strong-Uniqueness" Curriculum/` and verify every count instance reads "11 RIGOROUSLY CLOSED + 7 candidates" (or current canonical). Mechanical sweep.

### Observation 7 — Vol 15 Methodology has self-referential gaps

Vol 15 Ch 10 (Calibration Stack) documents 19 layers. Calibration #24 (Cross-Volume Audit) was filed Saturday and is layer #20 — Vol 15 Ch 10 references "19 layers" in its title and content. Vol 15 Ch 11 + Ch 12 reference "Calibration stack 1-23" but Ch 10 itself is at 19.

**Recommendation**: Vol 15 Ch 10 update to "20 Layers" (or whatever the count reaches by v1.0 publication). Add Calibration #24 entry. Keeper-lane self-fix; ~10 minutes.

### Observation 8 — Vol 7 + Vol 13 filename convention drift

Vol 7 + Vol 13 use `BST_Vol7_Ch1_..._v0_3_narrative.md` naming. Other volumes use `Curriculum_Vol5_Ch1_..._v0_1.md`. Vol 13 has BOTH naming patterns in its directory listing — some `BST_Vol13_Ch*_narrative.md` (older draft) + some `Curriculum_Vol13_Ch*_v0_1.md` (newer).

**Recommendation**: Standardize filename convention. Decide canonical: `Curriculum_Vol<N>_Ch<M>_<Title>_v<X_Y>.md`. Sweep with `git mv` to rename. Mechanical but matters for reader + future-CI navigation. Grace-lane.

### Observation 9 — Architectural Scaffold files exist but no clear reader-visible role

Each volume has a `Curriculum_Vol<N>_Architectural_Scaffold_v0_1.md` file. These were drafted during scaffolding phase. Now that chapters exist, the Scaffold files are either (a) redundant with INDEX.md, or (b) serving as Keeper/Cal-internal planning documents.

**Recommendation**: Decide their canonical role. If reader-facing, link from INDEX.md and describe purpose. If team-internal, move to `notes/` or rename `Vol<N>_Internal_Scaffold.md` to make team-internal status explicit. Keeper proposal: team-internal, move to `notes/curriculum_scaffolds/`. Casey-decision item.

### Observation 10 — Tier labels in chapter status fields use multiple conventions

I see `tier: "structural — methodology chapter"` (Vol 15) and `tier: "D-tier ratified ..."` (Vol 0/2) and other variants. The Quaker tier discipline (D/I/C/S) is well-defined for theorems + observables. Applying it to **chapters** is a different question — chapters contain multiple claims at different tiers.

**Recommendation**: Either (a) drop chapter-level tier labels and rely on per-claim tier labels within the chapter, or (b) define a chapter-tier convention (e.g., "D-chapter = all primary claims D-tier", "Mixed = D + I + C", "Structural = methodology"). Cal-decision item; Calibration #25 candidate if formalization needed.

## What this reading pass does NOT cover

- Line-level math errors within chapters I didn't read deeply (Cal Phase 2 cold-read is the right tool)
- PDF rendering / typesetting issues (Elie sweep)
- Theorem citation existence in AC graph (Grace mechanical sweep)
- Cross-volume observable precision consistency at scale (Phase 2 Calibration #24 Dimension B)

These are real and important but require different tooling than Keeper structural sampling.

## Priority ranking for team text-update work

**Tier 1 (recruiter chapters — Lyra+Elie joint, Saturday-Monday)**:
- Vol 2 Ch 6 m_p/m_e: add "Why this chapter matters" opener (Observation 4)
- Vol 0 Ch 9 Strong-Uniqueness: add "Why this chapter matters" opener
- Vol 4 Ch 1 Newton's G: add "Why this chapter matters" opener
- a_e ppt chapter (Vol 2 Ch 8?): same

**Tier 2 (cross-volume consistency — Grace+Cal joint, Saturday afternoon)**:
- Calibration #19 ratified-state count sweep across all 192 chapters (Observation 6)
- Filename convention standardization Vol 7 + Vol 13 + others (Observation 8)
- Forward-reference additions in Vol 0+1+2 to Vol 3-15 (Observation 5)

**Tier 3 (pedagogy depth — Lyra-lane, Saturday-Sunday)**:
- Level 3 (5th-grader) pass across chapters where it's thin (Observation 2)
- "BST primary integer" re-introduction reduction (Observation 3)

**Tier 4 (front-matter hygiene — Keeper-lane, ~30 min total)**:
- Status field cleanup (Observation 1) — defer to Phase 3 if too disruptive now
- Vol 15 Ch 10 calibration count update (Observation 7) — quick
- Architectural Scaffold canonical role decision (Observation 9) — Casey-call
- Chapter-tier convention decision (Observation 10) — Cal-call

## What Keeper does NOT recommend doing right now

- Do NOT do another full substance pass on Vol 3-15 — substance floor is met
- Do NOT renumber theorems or restructure chapter ordering
- Do NOT add new content; pure consistency + pedagogy + navigation work
- Do NOT block on Architectural Scaffold + chapter-tier decisions; those are Casey/Cal-call items

## Calibration discipline applied to this notes file

Per Quaker discipline: I am being honest that I sampled rather than fully read. The observations above are pattern-level and would be strengthened by Cal's per-chapter cold-read pass. Where my observations conflict with Cal's findings, **Cal's per-chapter mode wins** for substance issues — Keeper's pattern-level mode wins for cross-volume structural issues.

— Keeper, Textbook Reading Notes v0.1, Saturday 2026-05-23 ~14:46 EDT
