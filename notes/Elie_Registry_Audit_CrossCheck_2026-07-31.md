# Elie — Independent Registry Audit Cross-Check (2026-07-31)

Independent scan of `BST_AC_Theorem_Registry.md` (1710 theorem rows parsed), built as a cross-check for Grace's audit sweep. Purpose: rule Grace's report fast when it lands, and catch anything the sweep misses. **Discipline note:** I separate CONFIRMED defects from NEEDS-CLASSIFICATION — a raw count is not a defect count (the over-flag trap).

## CONFIRMED defects (high confidence, citation-relevant)

### 1. Six genuine ID COLLISIONS — a contiguous batch-filing block (HIGH priority, citation-breaking)
Each ID below carries **two entirely different theorems** on adjacent lines — a citation to the ID is ambiguous:

| ID | Line A (original) | Line B (collision) |
|----|-------------------|--------------------|
| T2030 | Deuteron magnetic moment μ_d/μ_N=C_2/g | Pion mass m_π=N_c·g·c_3·m_e |
| T2041 | Universe age = Wallach dim_6=140 | Light meson cascade m_K=(g/rank)·m_π |
| T2050 | Tritium β endpoint Q_β=(n_C/N_max)·m_e | CMB acoustic peaks ℓ_1=rank²·n_C·c_2 |
| T2058 | Cosmic log-scale ladder | Heavy quarkonium m_J/ψ=rank·c_2·m_π |
| T2074 | α_s(Q) running cascade | K3 Hodge numbers in BST integers |
| T2076 | BR(H→cc̄)=g²/(rank·C_2·…) | Gravitational α_G=exp(−rank³·c_2) |

All six sit in lines 2754–2795 — a **single batch** of new theorems filed reusing IDs 2030–2076 already assigned. **Fix:** renumber the Line-B theorem of each pair to fresh IDs (Grace/Keeper). This is the T1959-class defect (T1959 itself is already fixed — confirmed clean, appears once at L2693). **Confirms Casey's "structural, not one-off" thesis.**

### 2. T57–T62 block re-duplication + tier-column pollution (6 rows)
T57–T62 appear twice: original at lines 80–85 (["Proved"/"Empirical"]) and re-listed at lines 802–807 with the tier column reading **"Elie"** (my name leaked into the tier slot). Same theorems, duplicated, with a malformed tier cell. **Fix:** drop the L802–807 duplicates (or reconcile if the later versions are intended revisions).

### 3. Tier-label case inconsistency (normalize)
`Proved` (1430) vs `PROVED` (132) — same tier, two casings. Plus stray tier cells from pipe-in-formula splits (`V_cb`, `M_24` appear as "tiers" — formula `|` breaking the row). **Fix:** normalize casing; escape/wrap formula pipes in affected rows.

## NEEDS-CLASSIFICATION (flagged, NOT claimed as defects — avoid over-flagging)

### 4. Legacy-"Proved" masking (Casey's suspected item — likely widespread, needs body pass)
**91% of rows (1562/1710) are tier "Proved."** That is implausibly high given the I/S-tier reality of much of the cosmology/particle catalog — e.g. the DE rows we just retiered (T2079/T2117 dynamical DE → superseded by w=−1 K1040; M_TOV → Structural). This is the **tier-column-vs-body mismatch** Casey flagged: a legacy "Proved" default masking Identified/Structural content. **Not a mechanical fix** — needs a tier-vs-body pass (Grace's sweep item), ruling each against its actual derivation status. High-value, high-effort.

### 5. ~1530 rows in 5-cell format — classify, do NOT blanket-flag
Many rows parse to 5 cells vs the canonical 6 (id|name|tier|source|edges|date). This is *probably* a legitimate alternate format (omitted edges/date column), NOT 1530 defects. Needs a format-classification pass before any are called defects.

### 6. 845 ID gaps in T1..T2538 — informational, not defect
Gaps are expected (claimed-but-unfiled IDs). Counter integrity check: max ID = T2538 → `.next_theorem` should be ≥2539 (verify against the counter file). Not a defect per se.

## PENDING (second pass)
- **Superseded-still-PROVED** full sweep: T2079/T2117 handled (K1040); the registry has 13 internal supersede markers — cross-check the retraction record against every "Proved" row touching a retracted result (the DE/cosmology cluster is the freshest risk).
- **Citation integrity** (η_B→T1958=Ogg-Primes class): references pointing at the wrong theorem — needs the edge/citation cross-scan.

## Ruling posture
When Grace's audit report lands, I cross-check her findings against this scan: confirmed defects (1–3) should appear in both; if she surfaces items 4/6 (tier/citation), I verify each against the body/retraction record before ruling. I do **not** rubber-stamp — independent scan first, then reconcile. The 6 ID collisions (item 1) are the citation-breaking priority and should be fixed before any paper's external citations ship.

*Scan tool: `scratchpad/registry_audit.py` (Elie, 2026-07-31). Independent of Grace's sweep. Repo-internal, not pushed.*

---

## SECOND PASS (2026-07-31) — superseded + citation integrity (the papers-gating pass)

### A. CITED-BUT-UNREGISTERED (0 registry rows) — confirms + extends Grace's backfill list
Independent scan of the four papers' T-citations against the registry:

| Cited ID | Registry rows | Where cited | Severity |
|----------|---------------|-------------|----------|
| **T2534** | **0** | Falsifiable (color-duality headline) | **HIGH — central theorem** |
| **T2535** | **0** | Falsifiable (color-duality headline) | **HIGH — central theorem** |
| **T2526** | **0** | FLAGSHIP (sign-derivation + semigroup + T2526→Λ_QCD→T1271 keystone) | **HIGH — load-bearing keystone** |
| **T190** | **0** | muon (24/π²)⁶ ratio, heavily referenced across corpus | **HIGH — headline result unregistered** |
| T2530, T2524, T2521, T2525 | 0 each | Grace's own-row checks | confirm-and-backfill |

**This is the papers blocker, independently confirmed:** we were one GO from shipping a flagship whose central theorem (T2534/T2535) and a keystone (T2526) have no registry row. I add **T190** (the muon ratio) as a notable one — a headline result with no row.

### B. CITED-BUT-SUPERSEDED — inside the papers (freshest risk, DE cluster)
- **T2079** (w₀=−130/137=−0.949, dynamical DE) and **T2117** (wₐ, "dark energy evolution") are tier **Proved** in the registry AND cited in **BST_Color_Mixing_Duality** (T2079) and **BST_Falsifiable_Predictions** (T2079, T2117).
- Both are **SUPERSEDED by K1040** (dark energy = cosmological constant, w=−1 derived from the fixed C·π⁵ bulk volume, deviation→0).
- **Two fixes required:** (1) registry — stamp T2079/T2117 **superseded** (Grace's task); (2) papers — **drop the −0.949 DE citations** (Lyra's color-duality DE-line fix + the Falsifiable DE row). A paper citing a superseded theorem is the citation-integrity defect this pass is for.

### C. Superseded-still-PROVED (broader)
T2079/T2117 are the confirmed DE-cluster hit. The registry's ~13 internal supersede markers + the retraction record need the full steady-state sweep (Grace) — but the DE cluster is the only one touching the four live papers, so it's the only citation-gating one.

## Reconcile-with-Grace posture (task #4)
When Grace's audit report + backfills land: (1) confirm T2534/T2535/T2526/T190 now have rows with honest K962 tiers (I verify each tier against the graph/body, not rubber-stamp); (2) confirm T2079/T2117 stamped superseded; (3) confirm the papers' DE citations dropped/updated. The 6 ID collisions (first pass) run in parallel and don't gate the papers. Line-for-line reconcile pending her report.

---

## LIVE RECONCILE (2026-07-31, updating against Grace's in-progress backfill)

Grace backfilled the cited set **while this scan ran** — re-checking against the current file:

### A′. Cited set now REGISTERED — tiers spot-checked against my own toy work
| ID | Tier (Grace) | Elie reconcile |
|----|--------------|----------------|
| T2534 | DERIVED (maximal; 4/7-deviation Identified) | ✅ **matches my work exactly** (toys 4935/4938, K1029: maximal doubly-Derived, 4/7 Identified) |
| T2530 | DERIVED | ✅ matches (toy 4915, V_us Gatto blind 0.31%) |
| T2535 | DERIVED | ⚠️ **load-bearing central theorem** — DERIVED rests on the color-duality forcing (Lyra's); **Keeper rules** |
| T2526 | DERIVED | ⚠️ load-bearing FLAGSHIP keystone (K936 sign/semigroup); **Keeper rules** |
| T2525 | DERIVED | Keeper rules |
| T2524, T2521 | DERIVED [Keeper-confirm] | already flagged for Keeper — good |

The two I can verify from my own derivations (T2534, T2530) are **honestly tiered**. The load-bearing DERIVED claims (T2535 color-duality, T2526 keystone) are Keeper's ruling — I flag them as the tiers the papers' headlines rest on.

### B′. CORRECTION — I over-flagged T190 (owning it)
T190 is **NOT** a missing headline result. The muon (24/π²)⁶ ratio **is registered** — under **T2003** (lepton mass mechanism) and **T2091** (Möbius source), plus T1948. "T190" is a colloquial cross-reference token with no dedicated row; it's an **own-row/citation-consistency check** (Grace's list), not a missing result. My first-pass "HIGH — headline unregistered" was the over-flag trap — caught by verifying before ruling. Downgraded to: **own-row token check, low severity.**

### C′. Counter integrity — PASSES
Max registered ID = T2538; `.next_theorem` = 2539. Correct. Not a defect.

### D′. STILL OPEN (not fixed by the backfill) — superseded DE citations *in the papers*
The backfill added rows but did **not** touch the papers' body. **Color-Mixing** still cites **T2079**; **Falsifiable** still cites **T2079 + T2117** — the dynamical-DE theorems superseded by K1040 (w=−1). These are the remaining citation-integrity items: Grace stamps T2079/T2117 superseded in the registry; **Lyra/Grace drop the −0.949 DE citations from the two papers' bodies**. This is the last citation-gating fix before Cal's re-read.

### Net for the papers gate
- ✅ Cited-but-unregistered: resolved (Grace backfilled all 7; tiers spot-checked, two match my work, load-bearing ones to Keeper).
- ✅ Counter integrity: passes.
- ⚠️ **Remaining before Cal:** drop the superseded T2079/T2117 DE citations from Color-Mixing + Falsifiable bodies (Lyra/Grace).
- ↪ Parallel (non-gating): 6 ID collisions, tier-masking body pass, format/gap classification.

---

## THIRD PASS (2026-07-31) — K/F-citation integrity (task #4 completion)

Parity-checked every K-audit and F-note citation in the four papers against the corpus (the T2511-class check: cited-but-dropped/dangling).

- **74 unique K/F citations, 74 resolve, 0 dangling.** No dropped-citation defect for K/F references (unlike the T-layer, which had the unregistered + superseded issues). The K/F citation layer is healthy.
- **Spot-checked resolution quality:** the load-bearing recent K-audits resolve to **formal filings**, not just running-note mentions — K1040→Keeper K1042 note; K994→Keeper V_us note; K936→registry; K763→Lyra F697 note. Properly filed.
- **Bonus finding:** **K1042 (Keeper, filed today) already stamps T2079/T2117 SUPERSEDED** in the registry. So the registry side of the superseded-DE item (Second-Pass D′) is **done** — the only remaining piece is the paper *bodies* still citing T2079/T2117 (Lyra/Grace strip those).

### Net (all three passes)
| Layer | Result |
|-------|--------|
| T-citations (unregistered) | ✅ resolved — Grace backfilled 7; tiers reconciled (T2521→Identified, T2511 restored per K1045) |
| T-citations (superseded) | ⚠️ registry stamped (K1042); **paper bodies still cite T2079/T2117 — strip (Lyra/Grace)** |
| K/F-citations | ✅ clean — 74/74 resolve, 0 dangling, formal filings |
| Duplicate IDs | ↪ 6 collisions (parallel, non-gating) |
| Counter integrity | ✅ passes |
| My own over-flag (T190) | ✅ caught + corrected |

**Task #4 complete.** The only citation item still gating the papers is stripping the superseded T2079/T2117 citations from the two paper bodies. Everything else in my remit is verified clean or handed to the right owner.
