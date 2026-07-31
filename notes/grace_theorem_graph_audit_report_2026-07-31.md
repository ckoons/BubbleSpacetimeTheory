---
id: grace_theorem_graph_audit_report_2026-07-31
date: 2026-07-31
program: TEGMARK
status: current
topic_tags: [audit, theorem-graph, registry, duplicates, tier-mismatch, citation-integrity, desync, charter-deliverable]
claims:
  - id: this-a
    topic: systematic theorem-graph + registry audit (Keeper's charter) — findings by severity, fixes applied vs needing-ruling
    status: current
    superseded_by: null
    date: 2026-07-31
---

# [TEGMARK] Theorem-graph audit report (Keeper's charter, 2026-07-31) — findings + proposed fixes for Keeper to rule

*Grace | 2026-07-31 | Keeper's charter: systematic sweep, not a spot-check, because the defects are structural. I produce the report; Keeper verifies + rules. Gates the papers' external citations → first-in-line. Two defects fixed on sight (unambiguous); the rest flagged with proposed fixes + counts.*

## SUMMARY (severity-ranked)
| # | Finding | Count | Severity | Status |
|---|---|---|---|---|
| 1 | Duplicate registry IDs | 12 | HIGH | needs Keeper ruling (which row canonical) |
| 2 | Superseded-still-Proved (graph) | 2 | MED | ✅ FIXED (status→superseded) |
| 3 | Tier-column "Proved" masking body "Tier I/S" | 152 | HIGH | needs reconciliation pass (mechanical) |
| 4 | Registry↔graph desync | ~600 + 619 | HIGH | needs reconciliation |
| 5 | Counter integrity (.next_theorem drift) | 1 | MED | ✅ FIXED (2539→2538) |
| 6 | Data-layer↔graph sync gaps | 3 | LOW | needs registration |
| 7 | Citation refs above max (typos/future) | 3 | LOW | needs correction |
| 8 | Cosmology cluster (post w=−1) | 0 | — | ✅ CLEAN |

## Findings

### 1. Duplicate registry IDs (HIGH — 12)
Registry has two rows sharing one T-id: **T57, T58, T59, T60, T61, T62, T2030, T2041, T2050, T2058, T2074, T2076**. (T1959 which you flagged this morning — verify it's in this class or a 13th.) Each needs Keeper's ruling on which row is canonical + renumber the other (from `.next_theorem`) or merge. **Gates citations** — a paper citing "T2050" is ambiguous today.

### 2. Superseded-still-Proved (MED — 2, FIXED)
Graph nodes **T2079, T2117** carried `status: proved` alongside a `superseded_note` (K1040 DE change). **Fixed:** status → `superseded`. Hunt the rest against the retraction record: I scanned the graph and these were the only two; the registry may hold more (see #3/#4 reconciliation).

### 3. Tier-column "Proved" masking I/S-tier body (HIGH — 152 genuine)
The registry tier-column is a legacy **"Proved" default** (1428 "Proved" + 132 "PROVED" + 28 "Proved (external)" = 1588 of 1691 rows). Of these, **152 have an explicit "Tier I" (136) or "Tier S" (16) declaration in their own body** — a genuine tier-column ↔ body mismatch (e.g. T1966 Dark-Matter Ω, T1972 neutrino Δm² ratio, T1961 A_s — all body-declared Tier I but column "Proved"). **This is the widespread one, and it directly threatens external citations** — a paper citing these as "Proved" over-claims. Proposed fix: mechanical reconciliation pass — set the tier-column to the body-declared tier for the 152 (Keeper rules the K962 mapping: registry "Tier I"→IDENTIFIED, "Tier S"→STRUCTURAL). *(My earlier crude count of 213 was inflated by name-word false positives — "Structural Isomorphism", "Conditional Expectation"; 152 is the honest count from explicit "Tier X" declarations.)*

### 4. Registry↔graph desync (HIGH)
- Registry has **1691 T-rows**; the graph has **2314 nodes** (max_tid 2537). ~600 theorems in the graph are **not** registry table-rows (may be in registry prose sections, or genuinely unregistered — needs confirmation).
- **619 T-ids referenced in registry bodies are not themselves registered rows** (T43, T46, T134, …) — some are real theorems present in the graph but missing from the registry table; some may be dangling. Needs a graph↔registry reconciliation to split "in-graph-not-in-registry-table" (desync, fixable) from "truly dangling" (broken citation).
- **3 refs above max_tid** (T2842, T2849, T2897 > 2537) — typos or future-refs; correct or remove.

### 5. Counter integrity (MED — 1, FIXED)
`.next_theorem` had drifted to **2539** while max_tid = 2537 (should be 2538). **Fixed → 2538.** (The sweep caught this live.) Graph now ALL PASS on the verifier.

### 6. Data-layer↔graph sync (LOW — 3)
`data/bst_constants.json` cites theorem_ids **T749, T750, T824** not present as graph nodes. Register or correct the citations.

### 7 & 8
Above-max refs (#7): 3, see #4. Cosmology cluster (#8): **clean** — 0 residual dynamical-DE / w₀=−0.949 refs in graph nodes after yesterday's w=−1 change (the propagation was complete); the only DE-dynamical nodes are T2079/T2117, correctly superseded.

## Proposed order of fixes (for Keeper's ruling)
1. **Tier-column reconciliation (152)** — highest citation-risk; mechanical once Keeper approves the registry-tier→K962 mapping.
2. **Duplicate IDs (12)** — Keeper rules canonical + renumber.
3. **Registry↔graph reconciliation** — script the graph↔registry-row diff; split desync from dangling.
4. Data-sync (3) + above-max (3) — mechanical.
- **Done on sight:** superseded-status (2), counter drift (1), cosmology-clean confirmed.

## What I verified is CLEAN
Graph structural integrity (verifier ALL PASS: unique tids, no dangling edges, theorems==nodes, counts match, checksum current); cosmology cluster post-w=−1; the 9 fermion theorems T2527–T2535 + today's T2536/T2537 all registered.

— Grace, 2026-07-31 [TEGMARK]. Audit: 12 dup IDs, 152 genuine tier-mismatches (Proved-masking-I/S), registry↔graph desync (1691 rows vs 2314 nodes, 619 body-refs unregistered), 3 data-sync gaps. FIXED on sight: 2 superseded-status, 1 counter drift. Cosmology clean. Keeper verifies + rules the fix order; gates the papers' external citations.

## ADDENDUM — 2026-07-31 NOTATION-COLLISION HAZARD (for the lint)
**c_2 (lowercase) = 11 (Weitzenböck gap) ≠ C_2 (uppercase) = 6 (Casimir).** A real collision: K1048's glueball form c_2·π⁵·m_e = 1720 MeV is CORRECT (11·π⁵·m_e = 1720, the 0⁺⁺ glueball, 1710±50±80 band), but Elie read bare 'c₂' as C_2=6 and flagged it as 'the proton' (6·π⁵·m_e = 938). The value was right; the glyph is the hazard. ★ LINT RULE: flag any bare 'c_2/c₂' near a physics value and disambiguate — c_2=11 (Weitzenböck) vs C_2=6 (Casimir) are both live and one glyph apart. (Verified: 11·π⁵·m_e=1720 glueball ✓, 6·π⁵·m_e=938 proton ✓.)

## ADDENDUM — 2026-07-31 COUNTER lint rule + provenance-11 (Grace owns the counter now)
**Counter (single-writer = Grace):** `.next_theorem` = **max REGISTRY ROW tid + 1**, computed from `^| T#### |` rows ONLY — NOT from any T#### string in prose (the 'registry max 2897' scare was a toy-cluster prose match 'T2849–T2897'; no theorem row exists above 2538). Correct state: registry max row = **T2538 (η_B)** → `.next_theorem` = **2539**. η_B was registry-only (another writer); backfilled to the graph (max_tid now 2538, consistent). The recurring drift was a non-Grace writer bumping the counter — single-writer lock routed to Grace.
**Provenance-11 (not arithmetic):** the decoy-11 (T1791 Weitzenböck c_2) and the gauge-11 are NUMERICALLY IDENTICAL ((11/3)C_A = 11 = c_2). The lint CANNOT catch a weld by value — only by provenance (which operator). Flag any '11' wired to the β-function that doesn't trace to the gauge-determinant a₂ coefficient.
