---
node_type: k_audit
id: K1043
title: RULING on the theorem-graph audit (Grace report + Elie cross-check + Cal §166, three independent sweeps converged). VERIFIED by Keeper directly. (1) SIX genuine ID collisions — T2030/T2041/T2050/T2058/T2074/T2076, one contiguous batch-filing error (block ~2754-2795), each 2 rows, 2 different theorems; T2050 = Tritium β-endpoint vs CMB acoustic peaks (Cal-confirmed). (2) T57–T62 are NOT collisions (retire from the defect list) — same theorem in the formal registry table AND an auxiliary status-tracker table ("Elie" is that table's owner column, not a tier); audit script must exclude the status table. (3) Counter was UNSAFE (read 2538, but T2538=η_B exists → next claim would collide); fixed to 2539, Grace to set authoritative = true global max(registry∪graph)+1 after renumbers. (4) 152 tier-column mismatches: BODY-declared tier is authoritative; reconcile the column to the body; legacy "Proved"-with-no-body-tier is "registered", NOT externally citable as Proved/Derived without a K962 check. (5) Registry↔graph desync (619 unregistered ids) = background reconciliation, NOT a papers blocker. ★ PAPERS-READY GATE = the CITED-THEOREM SUBSET clean (no cited theorem in a collision or tier-mismatch) + T2079/T2117 superseded [done] + Cal's final gate — NOT the whole-graph cleanup.
date: 2026-07-31
author: Keeper
verdict: Canonical-choice rule for the 6 collisions: the row with more downstream citations keeps the ID; tie → earlier toy number keeps it; the other renumbers from the counter (2539+). Grace executes, escalates ties to Keeper. Fix ORDER: (a) cited-subset tier + collision reconciliation FIRST (citation risk → unblocks papers), (b) the 6 collisions in full, (c) counter authoritative, (d) background: full tier pass + 619 desync. Elie's second pass (superseded + citation integrity) feeds the cited-subset priority; Cal rules the executed fixes against his pre-registered 5-class tests. Daily-hygiene procedure filed alongside (standing lint). No physics touched.
---

# K1043 — Ruling on the theorem-graph audit; the papers gate is the cited subset, not the whole graph

Three independent sweeps (Grace's report, Elie's cross-check, Cal §166) converged on "structural, not one-off" — Casey's morning instinct. I verified the load-bearing claims directly (grep, not rubber-stamp) before ruling.

## ★ THE DEFECTS (verified + ruled)
1. **6 genuine ID collisions — CONFIRMED.** T2030, T2041, T2050, T2058, T2074, T2076 — each 2 rows, 2 *different* theorems, in one contiguous block (~2754–2795): a single batch-filing error, not six typos (Elie's read, correct). Spot-verified T2050 = Tritium β-decay endpoint (row 2771) vs CMB acoustic peaks (row 2772). **Citation-breaking; fix before any external cite.**
   - **Canonical-choice rule (Grace applies from citation data):** the row with more downstream citations keeps the ID; tie → the earlier toy number keeps it; the other **renumbers from the counter (2539+)**. Escalate genuine ties to Keeper.
2. **T57–T62 are NOT collisions — retire from the defect list.** Verified: each is the *same* theorem (e.g. T57 = "Gallager Decoding Bound") appearing in the **formal registry table** (line ~80) AND an **auxiliary status-tracker table** (line ~800, schema: name | owner | domain | status — "Elie" is the *owner* column, not a tier). One theorem, two tables — not two theorems, one ID. **No renumber.** The audit script must scope collision-detection to the canonical registry table and exclude auxiliary tables. (This retires 6 of Grace's "12"; the genuine collision count is **6**.)
3. **Counter — was UNSAFE, fixed.** Read `2538`, but T2538 exists (η_B renumber, K1042) → the next claim would collide with η_B. Grace's earlier fix computed max_tid=2537 without seeing my renumber. **Set to 2539 now** (immediate hazard cleared). **Grace to set the authoritative value = true global max(registry ∪ graph) + 1** after the 6 collision renumbers consume 2539–2544.
4. **152 tier-column mismatches — the citation risk.** The registry tier-column is a legacy "Proved" default (Grace: 1588/1691 rows; Elie: ~91%). 152 rows explicitly declare "Tier I / Tier S" in their *body* while the column says "Proved". **Ruling: the body-declared tier is AUTHORITATIVE.** Reconcile the column to the body for all 152 (Grace mechanical). For the ~1436 "Proved"-with-no-body-tier rows: they are **"registered," not proof-verified** — and **no external citation may present one as Proved/Derived without a per-item K962 tier check.** (Grace's honest 213→152 refinement — dropping name-word false positives like "Structural Isomorphism" — is exactly right; hand Keeper the accurate figure.)
5. **Registry↔graph desync (619 unregistered ids; 1691 rows vs 2314 nodes) — background, NOT a papers blocker.** The registry is the canonical tier source; graph nodes lacking registry rows are backfilled over time. Does not gate the papers *provided* every CITED theorem is registered + clean (verify in the cited-subset pass).

## ★★ THE PAPERS-READY GATE (answers "when are we ready for papers")
The papers do NOT wait on the whole-graph cleanup. Ready when **all three hold**:
1. **Cited-theorem subset clean** — every theorem cited by the four papers is (a) not in a collision, (b) tier-correct (body-authoritative), (c) registered. This is a *small, fast* subset, not 1691 rows.
2. **T2079/T2117 superseded** — done (K1042).
3. **Cal's final gate re-read** clears (corrected DE framing + abstract↔body pass).
The full cleanup (152 tiers, 6 collisions in full, 619 desync) continues in the background and does **not** hold the papers, *except* wherever it intersects the cited subset.

### ★★ ADDENDUM (Keeper ran the cited-subset check directly, 2026-07-31) — the ACTUAL papers blocker
Extracted every T-citation from the four external papers (flagship, color-duality, Falsifiable, fermion-sector) and intersected with the defects. Result:
- **The 6 collisions are cited by NO external paper** (the earlier "all 6 cited" was contamination from a Cal *referee* note, not a paper). → collisions are background, confirmed **not a papers blocker.**
- **T2079/T2117 (superseded) are cited only in the "these are the retired forms" supersession notes** (Falsifiable line 39, color-duality status) — correct, honest usage. **Not a blocker.**
- **★★ THE REAL BLOCKER — cited-but-UNREGISTERED theorems.** The registry's formal rows lag the recent work; several load-bearing cited theorems have **zero** registry occurrences (verified present in the AC graph — real theorems, just never backfilled): **T2534, T2535 (the ENTIRE Color–Mixing Duality result — the headline of that paper), T2526**, and low-mention/own-row-suspect **T2530 (1), T2524 (2), T2521 (3), T2525 (3), T190 (own-row check)**. A referee cannot look up a cited theorem that isn't in the registry. **This must be fixed before ship.**

**So the papers-ready gate resolves to a BOUNDED backfill (not the whole 619):** register the cited-but-absent theorems (≥ T2526/T2534/T2535, + verify own-rows for T2530/T2524/T2521/T2525/T190) into the canonical registry with proper K962 tiers, sourced from the AC graph + origin notes. **Grace backfills; Keeper rules the tiers** (esp. the color-duality T2534/T2535 tier — cited as DERIVED, verify against the K962 ladder). Then Cal's gate → GO. Estimate: a handful of theorems, today/tomorrow — NOT a multi-day graph cleanup.

## ★ FIX ORDER (ruled, per Grace/Cal's instinct)
(a) **Cited-subset first** — reconcile tiers + resolve any collision among cited theorems (the citation risk; unblocks papers). Elie's second pass (superseded-still-PROVED + citation integrity) + Grace's cited-theorem extraction feed this.
(b) **The 6 collisions in full** — canonical rule above; renumber 2539+.
(c) **Counter authoritative** — Grace sets true global max+1.
(d) **Background** — full 152 tier reconciliation + 619 desync backfill.
Cal rules each executed batch against his pre-registered 5-class tests (§166); Keeper rules escalated ties + the tier-mapping edge cases.

## ★ Endorsements
- **Elie's cross-check** (independent scanner, 6 collisions confirmed, disciplined non-over-claim on the 91%/5-cell/gaps) — exactly the "commit the checker's half blind" method; it makes Grace's report *verifiable*, not rubber-stampable. Continue the second pass.
- **Cal §166** (pre-registered 5-class tests, T2050 proactive find, T57-63 false-positive filter) — the right gate posture; rule the executed fixes against it.
- **Grace's report** — accurate (213→152 honest refinement), the headline "structural not one-off" is correct and verified.

## Daily hygiene
The recurrence is the real lesson: a duplicate ID and a tier-drift hid for *months*. Standing procedure filed alongside — `BST_Theorem_Hygiene_Daily_Procedure_v0.1_2026-07-31.md` (a scripted lint at EOD, co-owned Grace/Keeper). This audit becomes routine, not an event.

— K1043, Keeper, 2026-07-31. RULED: 6 genuine collisions (canonical = dominant-citation/earlier-toy, renumber other 2539+); T57-62 false positives (one theorem, two tables); counter fixed 2539 (Grace → true global max+1); tier-column body-authoritative (reconcile 152, legacy-Proved not externally citable without K962 check); desync = background. PAPERS GATE = cited-subset clean + supersede [done] + Cal gate, NOT whole graph. See K1042, [[BST_Theorem_Hygiene_Daily_Procedure_v0.1_2026-07-31]], Grace report, Elie cross-check, Cal §166.
