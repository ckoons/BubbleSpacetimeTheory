---
node_type: referee_verdict
id: Cal-K1809-clearance
title: "K1809 honesty debt CLEARED, and the verdict is simpler and harsher than the sweep's. A competitor count needs a null before it can mean anything, and the null must itself be swept -- my first pass picked one sampling range and produced an 'eta-bar is the one real anomaly' finding that did NOT survive varying it. Swept the range and cross-checked against an independent local-density estimator: gamma 11 in band against 6.9-10.9 by chance, eta-bar 3 against 1.4-2.4, J_CKM 41 against 35.7, rho-bar 2 against 3.1-5.2. EVERY ROW IS AT OR BELOW CHANCE. No row is anomalous, and no row is discriminating -- the defect belongs to the complexity class, not to any one quantity. J_CKM, which K1809 honestly recorded as UNTESTED because the simple-form pool cannot reach 50000 = n_C^5 (2^rank)^2, is now tested at its own class (5458-value compound pool, positive-controlled: the published form is in it) and comes back the same way, with a same-class competitor sqrt(N_c)/(rank^rank n_C^C_2) at +0.01 sigma against the published +0.53 sigma. eta-bar's real indictment is the range-independent one Keeper already found by eye: sqrt(C_2)/g fits five times better than the published form."
date: 2026-08-23
author: Cal
verdict: "K1809 CLEARED for Casey GO. Recommended action is UNIFORM, not per-row: none of gamma, rho-bar, eta-bar, J_CKM has discriminating power at its own complexity class, so none of the four may stand as evidence. For gamma, eta-bar and J the honest disposition is RETIREMENT, not Keeper's Option 2 -- 'smallest-of-N indistinguishable forms, N reported' implies an enumerable family and a meaningful choice, which is false when the band holds a chance number of members. rho-bar is not indicted by its count (2 where chance gives ~3) but is equally not evidence, and should be described that way rather than listed as a FAIL. Keeper's instrument is sound and reproduces closely; what it lacked was the null. The J gap he declined to read as a pass is now closed, and it closes against the row. SELF-CATCH ON RECORD: my first draft of this verdict claimed eta-bar was anomalously dense at +1.41 sd and singled it out as the one genuine anomaly; that result came from a single choice of null sampling range and evaporated when I swept it. Corrected before filing. Nothing pushed."
related: [K1809, K1801, T2198, T2259]
---

# Cal — K1809 cleared. A count needs a null, and the null needs a sweep.

Keeper ran the T2198 retirement test across five sibling rows, reported competitor counts, and recorded
honestly that J_CKM was **untested rather than passed** because his pool could not reach its complexity
class. Both halves were right. What the sweep lacked is the null: **how many BST forms land in a band of
that width anywhere at that scale?**

Without it a count cannot separate two defects with two different remedies — *wrong pick from a small
family* (in-band count above chance; restate as smallest-of-N) versus *saturated vocabulary* (in-band
count at chance; retire, because the quantity cannot be evidence at this class). Option 2 applied to a
saturated row is misleading: naming N dresses noise as a bounded ambiguity.

## Instrument check — my reconstruction of Keeper's pool reproduces his counts

Forms `a`, `√a`, `a/b`, `√(a/b)`, `√a/b`, `a/√b`, `a·b`, `1/(2√a)`, `1/(2√(a·b))`, `√(√a/b)` over
{rank, N_c, n_C, C_2, g, N_max}, ratios and products with repeats. **219 distinct values.**

| row | Keeper | mine |
|---|---|---|
| γ | 10 | **11** |
| ρ̄ | 2 | **2** |
| η̄ | 4 | **3** |

Close, not identical — so **every number below is computed on my reconstruction, not his exact pool.**

## ★ The self-catch, stated before the result it corrects

My first pass fixed one null sampling range per row and reported: *"η̄ is the one genuinely anomalous row,
3 in band against a chance 1.42, +1.41 sd."* **That finding does not survive varying the range.** I had
done to my own control exactly what I spent this morning telling Keeper not to do — left a free parameter
in a test and read the result off one setting of it.

**Swept ranges, plus an independent estimator** (count pool values in a factor-2 window around the target,
convert to a log-uniform in-band expectation — no sampling at all):

| row | actual in band | chance across 5 ranges | local estimator | surprising? |
|---|---|---|---|---|
| **γ** | 11 | 6.9 – 10.9 | 8.3 | **no** |
| **ρ̄** | 2 | 3.1 – 5.2 | 3.3 | **no — below chance** |
| **η̄** | 3 | 1.4 – 2.4 | 2.3 | **no** (the +1.41 sd was the most favourable range) |
| **J_CKM** | 41 | 35.7 | — | **no** |

**Every row sits at or below what the vocabulary supplies by chance.** The "one real anomaly" was an
artifact of my null's free parameter, and I am recording it here rather than quietly shipping the
corrected table.

## The two questions a count answers, and they are different

- **Is the count surprising?** Compare to chance. **Answer for all four rows: no.**
- **Is the match discriminating?** Look at the absolute count. A band holding ~1 form is informative; a
  band holding 2, 3, 11 or 41 is not. **Answer for all four rows: no.**

> **Together: all four rows fail on discriminating power, and none of them fails in a way that says
> anything special about that particular quantity. The defect belongs to the complexity class, not to
> the row.**

## Per row

**γ = arctan√n_C, 65.905° (+0.16σ).** Eleven arctan forms inside one error bar; chance supplies ~8–11.
**No arctan-of-a-BST-ratio can be evidence at this precision** — the vocabulary tiles the interval more
finely than the measurement resolves. **Retire.**

**ρ̄ = 1/(2√(rank·n_C)), 0.15811 (−0.09σ).** Two in band where chance gives ~3. **Not indicted by its
count** — and it should not be listed as a FAIL beside γ. But two is still not one: **it is equally not
evidence.** The honest description is "non-discriminating," not "failed."

**η̄ = 1/(2√rank), 0.35355 (+0.46σ).** Three in band against a chance ~1.4–2.4 — **not anomalous once the
range is swept.** Its real indictment is the one Keeper found by eye and it is range-independent:

| form | value | deviation |
|---|---|---|
| **√C_2/g** | 0.349927 | **+0.09σ** |
| √N_c/n_C | 0.346410 | −0.26σ |
| **published 1/(2√rank)** | 0.353553 | **+0.46σ** |

**A same-class sibling fits five times better than the form we publish.** That needs no null model and a
referee needs only a calculator. **Retire, or restate naming √C_2/g** — but restating still asserts a
three-member family, so retirement is cleaner.

**J_CKM = √rank/(rank⁴·n_C⁵) = 2.828e−5 (+0.53σ).** Keeper's pool generates simple forms; J's is compound,
50000 = n_C⁵·(2^rank)². **He was right not to read its silence as a pass.** Built the pool at J's own class
— numerator ∈ {1, a, √a, a·b}, denominator c^d·e^f over the BST integers plus N_max, **5458 distinct
values** — and positive-controlled it: **the published form is in the pool**, so the instrument catches its
must-catch case. **41 in-band competitors against a chance 35.7 (sd 3.9); 11% of random bands do as well.**
Best competitor **√N_c/(rank^rank·n_C^C_2) = 2.7713e−5 at +0.01σ.**

> **At J's complexity class the BST vocabulary places ~36 forms inside every error bar in that decade.
> Landing in the band carries no information.** **Retire.**

## What this does not touch

Unchanged, exactly as K1809 says: **λ = 1/√20** (blind, forward), **the ORDER result** (graph distance on
P₆, no fitted integer — and it **cannot fail this test**, which is the argument for the new work),
flavour-universality, CP existence, the sealed negative. A defect in four older curated rows, not in the
sector's spine.

## Owed to Grace — v1.0 absorbed K1809 cleanly, and now needs a small fold

`BST_Forcing_and_Evidence_FLAGSHIP_v1_0` genuinely carries the standard, the counts, η̄'s better-fitting
competitor and the J-untested calibration, and it correctly marks the reconciliation as a dispatch gate
rather than claiming it closed. **That is a real absorption, not a claimed one — credit.** Three lines now
need updating, and they are hers to fold, not mine to edit:

1. the sibling table's **ρ̄ row** — 2 competitors is below chance; it does not belong in a FAIL list;
2. **J_CKM "UNTESTED"** (table, Section III.5, and the standing-obligations list) — now tested, saturated;
3. **"either retired, or re-stated as smallest-of-N"** — for γ, η̄ and J, smallest-of-N is not an available
   honest option.

## The methodology, banked twice

> **A competitor count is not a verdict until you know how many competitors chance supplies —
> and a null model with a free sampling range is not a null until you sweep it.**

The first half is C6's shape (report the can-fail count, not the denominator) applied to the *background*
instead of the instrument. The second half is this morning's own lesson arriving at my door within the
hour: **an instrument you built this session is a candidate false-negative machine, and so is a null you
built this session.** Positive-control both, and cross-check with an estimator that shares none of the
first one's free choices.

**Scripts:** session scratchpad — `jsweep.py` (compound class, J), `simple2.py` (simple class, γ/ρ̄/η̄),
`robust.py` (range sweep + local estimator). Not claimed as toys; `/toy claim` is Elie's lane and the
counters are Keeper's authority. Claim numbers and I hand the code over unchanged.

— Cal, 2026-08-23. K1809's counts are sound and its J-limitation was honestly recorded. With the null
added and swept, the four rows collapse to one verdict: none discriminates, none is surprising, and the
first version of this note over-claimed η̄ off a single unswept range.
