---
node_type: referee_verdict
id: Cal-K1801-verdict
title: "K1801 cold-read. All six findings CONFIRMED, two of them re-characterized, and the scope is larger than the audit states. (a) Findings 1 and 2 are ONE defect, not two: the Guide's V_cb form 4/125 is not a 20% arithmetic error -- 0.0320 is arithmetically correct FOR ITS OWN FORM, which silently carries lambda = 1/5. Mislabelling it a typo prescribes the wrong remedy; it needs the lambda decision, not a recalculation. (b) The contradiction is NOT confined to Guide Vol2 Ch02 Sec 7.7: data/bst_constants.json carries TWO tier-D entries for sin theta_C -- 'Cabibbo angle' = 2/sqrt(79) scored 0.004% against 0.22501, and 'CKM element |V_us|' = 1/(2 sqrt n_C) scored 0.31% against 0.2243 -- different forms, different values, DIFFERENT EXPERIMENTAL TARGETS, both banked Derived. The banked layer disagrees with itself, so this is not a curation defect. (c) The two targets differ because they are different determinations (global CKM fit vs K_l3) and that difference IS the Cabibbo angle anomaly, so choosing a target is choosing a side in a live experimental controversy, not bookkeeping. (d) THE TARGET-INNOCENT DISCRIMINATOR: 20 = rank^2 n_C is a pure BST product, ZERO adjacencies; 79 = rank^4 n_C - 1 and 11 = 2 C_2 - 1 each cost ONE. The better fit is bought with an adjustment, and that is decidable without looking at which fits better. (e) CORPUS-WIDE: T1449 is registered Proved and states the working vocabulary is BST products plus {0, +/-1, +/-rank, +/-N_c}, explicitly calling it a 6-way search per integer. Adding that adjacency set multiplies in-band competitor counts by roughly 14-26x in test. EVERY discriminating-power count in the corpus computed over bare BST integers -- including my own K1809-B -- is a LOWER BOUND."
date: 2026-08-23
author: Cal
verdict: "K1801 CONFIRMED on all six findings; DISPATCH REMAINS BLOCKED on the mixing section until the lambda decision is made, and the block must be widened from Guide Sec 7.7 to data/bst_constants.json, which carries the same contradiction at tier D. Recommended resolutions: (1+2) ONE decision, not two -- bank lambda = 1/(2 sqrt n_C) = 1/sqrt 20 as the zero-adjacency form, retire 2/sqrt(79) and the implied 1/5, and re-derive the V_cb row from the banked lambda; the 4/125 entry is not a typo to correct but a third lambda to remove. (3) A: the Guide's 4/5 and the data layer's 9/11 are different numbers and the data layer's own tier is C, not D -- the 'DERIVED' label contradicts the corpus's own ledger; state A as the open input it is. (4) delta_CP must carry -4.5 sigma; 'measurement evolving' is a decorative clause standing where a number belongs, and a failing prediction stated plainly is a result. (5) AFFIRM and calibrate both ways -- correcting the stale column IMPROVES the V_cb row to +0.5 sigma. (6) AFFIRM. Cannot clear for Casey GO: findings 1-3 are physics decisions and they are Lyra's and Grace's, not mine to make. What I can do is remove the ambiguity about WHICH decision, and that is done. Nothing pushed."
related: [K1801, K1809, T1444, T1449, T1446, T2530, T1444]
---

# Cal — K1801 cold-read. The audit is right, two findings need re-characterizing, and the blast radius is bigger.

## 1+2 — These are ONE defect, and calling it an arithmetic error prescribes the wrong fix

K1801 finding 2: *"the V_cb row is internally inconsistent — stated form 4/125 = 0.0320 vs value column
0.0400, 20 percent apart."*

**0.0320 is arithmetically correct for 4/125.** Nothing was mis-multiplied. Work backwards:
V_cb = A·λ² with A = 4/5 gives 4/125 **only if λ² = 1/25, i.e. λ = 1/5** — which is exactly the *third* λ
that finding 1 identifies. **So the V_cb row is not a typo; it is finding 1 appearing a second time,
wearing a form instead of a number.** With the banked λ = 1/√20 the same expression gives
(4/5)·(1/20) = **4/100 = 0.0400**, which is what the value column already says.

> **Remedy differs by diagnosis.** A typo gets recomputed by whoever finds it. **A third λ baked into a
> form requires the λ decision and cannot be fixed by anyone until that decision is made.** Findings 1
> and 2 are one item on the dispatch list, not two.

## 3 — The contradiction is in the BANKED layer, not only the curated one

K1801 scopes the defect to `Guide Vol2 Ch02 Section 7.7`. **It is also in `data/bst_constants.json`,
which is the layer the Guide is supposed to be downstream of:**

| entry | form | BST value | scored against | precision | **tier** |
|---|---|---|---|---|---|
| **"Cabibbo angle"** | sin θ_C = 2/√(rank⁴·n_C − 1) = 2/√79 | 0.225018 | **0.22501** | 0.004% | **D** |
| **"CKM element \|V_us\|"** | \|V_us\| = sin θ_C = 1/(2√n_C) | 0.223607 | **0.2243** | 0.31% | **D** |

**Both call themselves sin θ_C. Both are banked Derived. They are different numbers, and they are scored
against different experimental values.** That is not a curation slip that a Guide edit fixes — **the
data layer disagrees with itself at tier D**, and the Guide is faithfully reproducing an upstream
contradiction. **The dispatch block has to cover both files.**

The same pattern continues: `V_cb = C_2²/(DC·79) = 36/869` (tier S) — and **869 = 11 × 79**, so the banked
V_cb carries *both* contested integers. The Guide's `A = 4/5` is a **third** value against the data
layer's `A = 9/11 = 0.8182` (tier **C**, not D). **K1801's finding 3 is stronger than stated: A is not
merely an open input shown as derived — it is shown as derived at a value the corpus does not carry, at
a tier the corpus's own ledger contradicts.**

## 4 — ★ The two targets are not interchangeable, and picking one is picking a side

0.22501 and 0.2243 are not a stale number and a fresh one. They are **two different determinations of the
same quantity** — the unitarity-constrained global CKM fit versus the K_l3 extraction — and the gap
between them **is the Cabibbo angle anomaly**, a live ~2–3σ experimental tension.

> **So the corpus currently scores one BST form against the target that flatters it (2/√79 at 0.004%
> against the fit value) and the other against the target that does not (1/√20 at 0.31% against K_l3).**
> That is a tuning channel with an experimental controversy inside it.

**Pin the observable before scoring, and freeze which determination we predict.** *(Both stored `observed_value`s
carry no error bar in the JSON. They need re-verification against current PDG before any σ is quoted —
remembered experimental numbers go stale, and these are load-bearing.)*

**And say the honest thing, which is in BST's favour:** 1/√20 together with the banked
\|V_ud\| = √(19/20) is **exactly first-row unitary by construction** (1/20 + 19/20 = 1), while the measured
first row currently is not. **BST's λ sits on one side of an open experimental discrepancy. That is a
discriminating prediction, not a 0.31% miss** — and it should be written that way rather than apologised for.

## 5 — ★ The target-innocent discriminator, decided without looking at the fit

The two λ do not cost the same:

| form | integer | decomposition | **adjacencies used** |
|---|---|---|---|
| **1/√20** | 20 | rank²·n_C | **0** |
| 2/√79 | 79 | rank⁴·n_C **− 1** | **1** |
| A = 9/11 | 11 | 2C_2 **− 1** | **1** |

**The better fit is bought with an adjustment.** T1444 gives that −1 a mechanism (the k=0 vacuum mode
excluded from vertex sums), so it is not a naked fit — but the mechanism must say **where the subtraction
applies and where it does not**, or the ± is free. **Deciding by adjacency count is target-innocent;
deciding by which fits better, when one has a free adjustment and the other does not, is not.**

**⟹ Bank λ = 1/(2√n_C) = 1/√20. Retire 2/√79 and the implied 1/5.**

## 6 — ★★ CORPUS-WIDE: T1449 multiplies every discriminating-power count we have ever run

`T1449 Integer-Adjacency Theorem` is registered **Proved, D0**:

> *"Every integer in a BST correction or derived formula lies in the adjacency set
> A = {p + δ : p ∈ P, δ ∈ {0, ±1, ±rank, ±N_c}} where P is the set of BST products. 63/68 = 92.6%…
> Dominant mode: −1 (vacuum subtraction). **AC(0) search algorithm: try 6 adjacencies per integer.**"*

Read as a referee: **that is a statement that the corpus's working vocabulary is seven integers wide per
BST product, and it describes itself as a search.** Measured, on a common form-pool:

| | integers | form-pool | η̄ in band | ρ̄ in band | γ in band |
|---|---|---|---|---|---|
| BST products only | 26 | 1105 | 12 | 21 | 46 |
| **+ T1449 adjacencies** | **101 (×3.9)** | **24092 (×22)** | **167** | **409** | **1201** |

**Roughly 14–26× more competitors once the corpus's own stated vocabulary is used.** *(Absolute counts here
are not comparable to K1809-B's — different form list. The **ratio** is the finding.)*

> **Every discriminating-power count in this corpus computed over bare BST integers is a LOWER BOUND —
> including my own K1809-B.** Saturation is worse than measured, never better, so **§705's verdicts
> strengthen and none reverses.** But the general rule now has a number attached: **a sweep that omits the
> adjacency set under-counts its competitor pool by about an order of magnitude.**

**This is not an argument that T1444 is wrong.** It is an argument that **a correction available in seven
flavours at every integer cannot also be evidence**, unless the mechanism predicts its own applicability.
That is the decidable ask, and it is bigger than K1801.

## The rest

- **Finding 4 (δ_CP)** — CONFIRM, and it is the decorative-clause guard exactly: *"measurement evolving"*
  is a soft phrase standing where **−4.5σ** belongs, while every neighbouring row carries a number.
  **Put the number in.** A failing prediction stated plainly is a result; this program has made assets of
  the projection negative and the weak-current ceiling by doing precisely that.
- **Finding 5 (stale column)** — AFFIRM, and it is the both-directions calibration: correcting the data
  **improves** V_cb from a claimed −2.7% to +0.5σ. **Under-claiming is as dishonest as inflating.** Say both halves.
- **Finding 6 (Vol6 credit list)** — AFFIRM. Credit-list genre, must not reach a results table.
- **Keeper's "flagged, not fixed" call** — CORRECT. Findings 1–3 are physics decisions belonging to Lyra
  (λ) and Grace (the ledger tier on A). **I can remove the ambiguity about which decision is owed; I cannot
  make it, and neither should he have.**

## What I cannot do

**I cannot clear K1801 for Casey GO.** K1809 I could clear because it needed a measurement and I could run
it. **K1801 needs a choice** — which λ the corpus banks, and which experimental determination we predict.
Those are Lyra's and Grace's calls with Casey's GO. **What is now removed is the excuse that it is unclear
what is being decided:** one λ decision (not two defects), applied to both the Guide and the data layer,
with the target-innocent discriminator already on the table.

— Cal, 2026-08-23. K1801 is right about all six. Two of them are one. The contradiction is banked, not
merely curated. And T1449 says out loud that our integer vocabulary is four times wider than every
competitor count has assumed — mine included.
