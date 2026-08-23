---
node_type: k_audit
id: K1804
title: "REFINEMENT AND PARTIAL SELF-DOWNGRADE of K1802 ruling 3. I ruled the graph 'not a DAG' with 1210 theorems in derivation cycles and asserted, without testing it, that the probable cause was a flipped edge-direction convention. I then tested my own assertion and it is CONFIRMED and far more localized than I claimed — and the consequence is much better news than my ruling stated. THE DECISIVE TEST: keep ONLY prerequisite->consequent derived edges (low-tid -> high-tid) and the largest strongly-connected component drops to 1 — a PERFECT DAG, no cycles anywhere. So tid order IS a valid topological order for the derivation relation, and 100 percent of the cyclicity is caused by 2410 backwards-oriented 'derived' edges (35.3 percent of 6833). THE CORPUS IS NOT CIRCULAR; ONLY ITS EDGE BOOKKEEPING IS. THE FLIP IS ERA-LOCALIZED, NOT RANDOM: backwards fraction by tid band runs T0-500 ~12 percent, T1000-1250 45 percent, T1250-1500 56 percent, T1500-1750 **95.3 percent** (281 backwards vs 14 forward), T1750-2000 65 percent, and T2000-2250 **0.0 percent** (268 forward, 0 backwards). A 95-vs-0 contrast between adjacent bands is a convention that was inverted for a period of authorship and later corrected — not noise. Also 472 explicit 2-cycles (A->B and B->A both tagged 'derived'); removing them alone only drops the largest SCC 1207 -> 865, so they are a symptom, not the cause. CONSTRUCTIVE DELIVERABLE — the true derivation spine, computed on the sane orientation: max depth 64, mean 17.71, 656 roots, longest chain 65 steps from T1 'AC Dichotomy' to T1393 'BST Rationals Are Optimal'. That is the spine Casey's linear-algebra directive asks to see, and it exists. CAVEAT I MUST STATE: tid order is mostly but not strictly chronological — renumbering has happened (K1042 moved T1958 to T2538) — so tid-order is a strong heuristic for the sane orientation, NOT a proof of it. Grace must confirm the convention per era against registry rows, NOT blanket-flip 2410 edges."
date: 2026-08-22
author: Keeper
verdict: "K1802 ruling 3 DOWNGRADED from 'no derivation-order statistic is trustworthy' to 'the derivation STRUCTURE is sound; the stored ORIENTATION is corrupted in identifiable eras.' The corpus is acyclic under the sane orientation — largest SCC = 1. K1802 rulings 1 (retire `depth`) and 2 (demote 2185 bare `proved`) STAND UNCHANGED: the stored depth field is still invalid (stored max 2 vs true 64), and `proved` is still a default, still published as '98.4% proved'. New severity: ruling 3 MODERATE (was CRITICAL) — a localized bookkeeping fault with a known signature and a constructive fix. Grace's task is now precise: confirm the convention PER ERA against registry rows and re-orient by era; do NOT blanket-flip. Nothing pushed."
---

# K1804 — The corpus is not circular. Only its bookkeeping is.

I filed K1802 ruling 3 as CRITICAL and asserted a cause I had not tested. Testing it downgrades my own
ruling and produces something useful.

## The decisive test

Keep **only** prerequisite→consequent `derived` edges (low-tid → high-tid):

> **largest strongly-connected component = 1. A perfect DAG. No cycles anywhere.**

So **tid order is a valid topological order** for the derivation relation, and **100% of the cyclicity is
caused by the 2410 backwards-oriented `derived` edges** (35.3% of 6833).

**The corpus is not circular. Only its edge bookkeeping is.** That is a materially better state than I ruled.

## The flip is era-localized, not random

| tid band | backwards | forward | % backwards |
|---|---|---|---|
| T0–500 | 306 | 2229 | ~12% |
| T1000–1250 | 214 | 264 | 44.8% |
| T1250–1500 | 692 | 539 | 56.2% |
| **T1500–1750** | **281** | **14** | **95.3%** |
| T1750–2000 | 410 | 216 | 65.5% |
| **T2000–2250** | **0** | **268** | **0.0%** |

**A 95.3%-vs-0.0% contrast between nearby bands is a convention that was inverted for a period of
authorship and later corrected.** Not noise, and not genuine circularity.

The 472 explicit 2-cycles (A→B and B→A both tagged `derived`) are a **symptom, not the cause** — removing
them alone drops the largest SCC only 1207 → 865.

## Constructive deliverable — the true derivation spine

Computed on the sane orientation:

- **max derivation depth = 64** (the stored field says 2)
- **mean depth = 17.71**
- **656 roots** — theorems nothing derives
- **longest chain = 65 steps, from T1 "AC Dichotomy" → T1393 "BST Rationals Are Optimal"**
- first steps from the root: T1 → T9 → T20 → T42 → T47 → T48 → T49 → T59 → …

**That is the derivation spine Casey's linear-algebra directive asks to see, and it exists.** It was
invisible because the orientation noise buried it.

## The caveat I must state, and it constrains the fix

**tid order is mostly but not strictly chronological — renumbering has happened** (K1042 moved T1958 →
T2538). So tid-order is a **strong heuristic** for the sane orientation, **not a proof of it**. The
95-vs-0 structure is far too strong to be renumbering noise, but that argues for the *mechanism*, not for
any individual edge.

⟹ **Grace: confirm the convention PER ERA against registry rows, then re-orient by era. Do NOT
blanket-flip 2410 edges on my tid heuristic.** The instrument that found the signature is not the
instrument that should execute the repair.

## What stands from K1802

- **Ruling 1 (retire `depth`): STANDS**, and is now sharper — stored max 2 vs **true max 64**.
- **Ruling 2 (demote 2185 bare `proved`): STANDS unchanged.** Still a default, still 93.0%, still
  published as "98.4% proved" in `Guide/INDEX.md`.
- **Ruling 3: DOWNGRADED CRITICAL → MODERATE.** A localized bookkeeping fault with a known signature and
  a constructive fix — not a corpus that cannot be trusted.

— Keeper, K1804, 2026-08-22. I asserted a cause in a CRITICAL ruling without testing it. Testing it made
the ruling milder and the corpus healthier than I said. Both halves belong in the record.
