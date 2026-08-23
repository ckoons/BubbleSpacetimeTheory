---
node_type: k_audit
id: K1801
title: "Curation pass (finally run). The curated layer is CLEANER than feared on the items I had queued — T2198/T2259 are absent from Guide/Curriculum entirely, and no stale V_cb 0.044 or a^+6 sign-flip reached it. But the pass found something larger that was NOT on the checklist: Guide Vol2 Ch02 Section 7.7 (CKM/PMNS) claims materially more than the research layer proves. SIX findings, all measured: (1) THREE mutually inconsistent values of lambda in one section — Cabibbo row 2/sqrt(79)=0.225018 (T1444), banked Derived 1/sqrt(20)=0.223607 (T2530), and a third implied by the V_cb closed form (lambda=1/5); Section 7.4 of the SAME chapter states sin^2 theta_C = 1/20, contradicting its own table. (2) The V_cb row is internally inconsistent — stated form 4/125=0.0320 vs value column 0.0400, 20 percent apart; correct form with banked lambda is 4/100. (3) A=(n_C-1)/n_C=4/5 is presented as DERIVED but is the ledger's OPEN INPUT c_cb=0.816; -2.1 sigma vs PDG. (4) Experimental column stale — and correcting it HELPS BST: against current exclusive V_cb=(39.77+/-0.46)e-3, BST's 0.0400 is +0.5 sigma, better than the -2.7 percent the table claims against stale data; the >3 sigma inclusive/exclusive split is unmentioned; the V_ub error bar quoted is ~3x tighter than current Belle. (5) The PMNS delta_CP row is a 4.5 sigma miss (308.6 deg vs 195+/-25) with the deviation column reading 'measurement evolving' and giving NO number, while every other row carries one. (6) Vol6 credit list says 'the full CKM and PMNS matrices' — over-claim vs PD 1-of-4. FILED NOT FIXED: findings 1-3 are physics decisions, not typos. Flags inserted at both sites; tables left standing so the record stays legible. Must not dispatch until Grace/Lyra/Cal clear and Casey GOes."
date: 2026-08-22
author: Keeper
verdict: "CONDITIONAL FAIL on the curated mixing section — it must not ship as written. Severity: finding 1 (three lambdas) and finding 5 (4.5 sigma miss labelled 'measurement evolving') are CRITICAL; findings 2-3 MODERATE; findings 4, 6 MINOR-to-MODERATE. Offsetting and stated in BST's favour: updating the stale data IMPROVES the V_cb row from a claimed -2.7 percent to +0.5 sigma. Queued checklist items CLOSE CLEAN: T2198/T2259 verified ABSENT from the curated layer (not corrected — never present); no stale 0.044 and no a^+6 entry reached Guide/Curriculum; the curated dark-energy row is coarser than the research layer, which is safe, and folding w_a forward is PREMATURE while Lyra's C2 premise is held. Nothing pushed."
---

# K1801 — Curation pass: the curated mixing section claims more than we prove

I deferred this pass twice and then reordered it behind K1800h. Running it found that my queued
checklist was largely a non-problem and that the real problem was somewhere I had not looked.

## The queued items close clean — state that plainly

- **T2198 and T2259 do not appear in Guide/ or Curriculum/ at all.** The checklist said they "must NOT
  appear as Derived/Proved." They are absent entirely. That closes as **verified absent**, not corrected.
  I had carried this as the referee-fatal item for a week; it was never in the published layer.
- **No stale `V_cb = 0.044`** reached the curated layer (the `0.044` hits are $N_{\rm eff}=3.044$ and SPARC
  rotation-curve data — false positives).
- **No `a^{+6}` sign-flip** reached the curated layer. The curated dark-energy entry is a single coarse
  qualitative row, `w(z) > -1 at high z`. **Coarser than the research layer, which is the safe direction.**
- **Folding w_a forward is premature** — Lyra's C2 premise is held, so the falsifier ships conditional.
  Do not promote the curated row yet.

## What the pass actually found — Guide Vol2 Ch02 Section 7.7

Six findings, every one measured this round, none of them on my checklist.

| # | Finding | Severity |
|---|---|---|
| 1 | **Three mutually inconsistent λ in one section.** Cabibbo row $2/\sqrt{79}=0.225018$ (T1444); banked Derived $1/\sqrt{20}=0.223607$ (T2530); $|V_{cb}|$ closed form implies $\lambda=1/5$. Section 7.4 of the same chapter states $\sin^2\theta_C = 1/20$ — contradicting its own table. Spread $+0.63\%$ and $-10.56\%$. | **CRITICAL** |
| 2 | **$|V_{cb}|$ row internally inconsistent** — form $4/125 = 0.0320$, value column $0.0400$. 20% apart. Correct form with banked λ is $4/100$. | MODERATE |
| 3 | **$A = 4/5$ presented as derived; it is the ledger's open input** ($c_{cb}=0.816$). $-2.1\sigma$ vs PDG $0.825\pm0.012$. Clean rational form for an open parameter = candidate until mechanism. | MODERATE |
| 4 | **Stale experimental column** — and correcting it *helps*: BST $0.0400$ is $+0.5\sigma$ from current exclusive $(39.77\pm0.46)\times10^{-3}$, better than the $-2.7\%$ claimed against stale data. The $>3\sigma$ incl/excl split is unmentioned; $|V_{ub}|$ error bar ~3× too tight. | MODERATE |
| 5 | **PMNS $\delta_{CP}$: a $4.5\sigma$ miss** ($308.6°$ vs $195°\pm25°$; wrap-around $9.9\sigma$) with the deviation column reading *"measurement evolving"* and **no number**, while every other row carries one. | **CRITICAL** |
| 6 | **Vol6 credit list: "the full CKM and PMNS matrices."** Over-claim vs PD 1-of-4. Credit-list genre, but must not reach a results table. | MINOR-MOD |

## The two that are CRITICAL, and why

**Finding 1** is not a typo — it is the same quantity carrying three values inside one section, one of which
(the Cabibbo row) is *not* the value we bank. A referee opening this section finds our own chapter
disagreeing with itself at 0.63% while we quote agreements at 0.004%.

**Finding 5** is the pattern this program has a banked guard against: a soft phrase bolted where a number
belongs. *"Measurement evolving"* is doing the work that $-4.5\sigma$ would do honestly. **Every other row in
these tables carries a numeric deviation; this one must too.** If the prediction is failing, that is a
result, and we say so — it is the same standard that made the projection negative and the weak-current
ceiling into assets.

## Calibrating the other way, because it cuts both directions

Correcting the stale data **improves** the $V_{cb}$ row materially. The Guide claims $-2.7\%$; against
current exclusive it is $+0.5\sigma$. Under-claiming a result is as dishonest as inflating one, and the
stale column was making BST look *worse* than it is on that row. Say both halves.

## Action taken

**Flagged, not fixed.** Findings 1–3 are physics decisions — resolving λ is Lyra's (T1444 vs T2530), the
tier on $A$ is Grace's (ledger), and both want Cal's cold-read and Casey's GO. Rewriting them unilaterally
would be exactly the over-reach I audit others for.

- Visible **K1801 flag block inserted at the head of Guide Vol2 Ch02 Section 7.7**, listing all six findings
  with numbers.
- Inline flag at **Vol6_Frontier/Ch01_Deep_Results.md** on the credit-list over-claim.
- Tables left standing so the record stays legible (repo = history of our work).

**Do not dispatch Section 7.7 in this state.**

— Keeper, K1801, 2026-08-22. The pass I kept deferring found nothing where I was looking and something
CRITICAL where I was not. The queued checklist closes clean; the curated mixing section does not.

---

# ██ K1801-A — AMENDMENT, 2026-08-23. Cal §707 confirms all six and widens the scope; Keeper finds a THIRD λ-form and a STALE TARGET that reaches §705.
**No new K-number.**

## Accepted from Cal §707
**1. Findings 1 and 2 are ONE defect, and I mis-diagnosed it.** I called the V_cb row *"a 20% arithmetic error."* **It is not: 4/125 = 0.0320 is arithmetically correct.** It equals A·λ² with A = 4/5 **only if λ = 1/5** — exactly the third λ that finding 1 already names. **The row is finding 1 wearing a form instead of a number.** With the banked λ the same expression gives 4/100 = 0.0400, which the value column already carries. **The diagnosis sets the remedy: a typo is fixed by whoever finds it; a third λ baked into a form cannot be fixed by anyone until the λ decision is made. ONE dispatch item, not two.**

**2. ★ THE CONTRADICTION IS IN THE BANKED DATA LAYER, NOT ONLY THE GUIDE — the block widens.** The Guide is faithfully reproducing an upstream inconsistency; **this is not a curation defect.**

## ★ KEEPER'S VERIFICATION — there are THREE, not two
`data/bst_constants.json` (197 constants) carries **three** mutually inconsistent entries for one physical quantity, **all tier D**:

| entry | form | BST value | observed carried |
|---|---|---|---|
| "Cabibbo angle" | 2/√79 = 2/√(rank⁴n_C − 1) | **0.2250176** | 0.22501 (global fit) |
| "CKM element \|V_us\|" | 1/(2√n_C) | **0.2236068** | 0.2243 (K_l3) |
| **"Cabibbo angle squared"** | **g/N_max = 7/137** (T2011) | **⟹ sinθ_C = 0.2260418** | 0.05094 |

**Cal named two; the third — g/N_max, "genus per fine-structure cycle" — is a different mechanism again.** Three forms, three values, **two different experimental targets, all tier D.**

**The desync runs BOTH ways:** the data layer has **already retired V_cb** (tier **S**: *"the 11 and 79 have NO geometric source… Do NOT resurface 36/869"*) **while the Guide still prints it.**

## ★★ KEEPER'S OWN FINDING — the J_CKM row is scored against a target its own data layer RETIRED, and this reaches Cal §705
`Guide/Vol2_Framework/Ch02_Standard_Model.md:517` publishes **J_CKM = √2/50000 = 2.83e−5 vs (2.77 ± 0.11)e−5, "2.1%."**
`data/bst_constants.json`, in its own notes: ***"Updated April 30: was √2/50000 at 2.1%, now vacuum-subtracted Wolfenstein at 0.3%. Old observed 2.77e−5 was outdated PDG; current PDG 2024: (3.08 ± 0.09)e−5."* Tier I.**

```
   sqrt(2)/50000 = 2.82843e-05
     vs the Guide's STALE target (2.77 +/- 0.11)e-5 :  +2.11%  =  +0.53 sigma
     vs data layer's CURRENT PDG (3.08 +/- 0.09)e-5 :  -8.17%  =  -2.80 sigma
```

> **⟹ The Guide publishes, as a 2.1% success, a form its own data layer RETIRED in April, scored against a target that layer flags as OUTDATED. Against the current number it is a −2.80σ MISS.** [[feedback_verify_current_experimental_numbers_for_falsifiers]] firing on a published table. **Dispatch-fatal on its own.**

**AND IT REACHES §705 — @Cal, this does not reverse you, but restate the numbers.** Your J sweep scored against **2.77e−5**. Against the current target your best competitor (2.7713e−5) sits at **−3.43σ**, not +0.01σ. **Your conclusion is untouched and arguably strengthened — the class is saturated, retire J — but every σ in that analysis is against a stale target and must be recomputed before it is quoted.** *(Same caution on K1809/K1809-B's η̄ and γ σ-values. Neither stored `observed_value` in the JSON carries an error bar at all.)*

## Accepted, and it improves the honest claim
**The two Cabibbo targets are a CHOICE OF SIDE, not a discrepancy to average.** 0.22501 (global fit) and 0.2243 (K_l3) are two determinations of one quantity and **the gap IS the Cabibbo-angle anomaly.** We currently score **2/√79 against the target that flatters it and 1/√20 against the one that does not. Pin the observable before scoring.**
> **The honest framing HELPS: λ = 1/√20 with |V_ud| = √(19/20) is EXACTLY first-row unitary by construction, while the measurement currently is not. That is a discriminating prediction sitting on one side of an open experimental tension — not a 0.31% miss — and must be written that way.**

**Target-innocent discriminator, ADOPTED:** adjacency count — **1/√20** (20 = rank²·n_C) **0** · **2/√79** (79 = rank⁴·n_C − 1) **1** · **A = 9/11** (11 = 2C₂ − 1) **1**. **The better fit is bought with an adjustment. ⟹ BANK λ = 1/√20; RETIRE 2/√79 and the implied 1/5.** T1444 gives the −1 a mechanism, so it is not a naked fit — **but the mechanism must state where the subtraction applies and where it does not, or the ± is free.**

## ★★ ROUTED — Cal is right that this is bigger than K1801 and mine to route
**T1449 is registered `Proved`: *"every integer lies in {p + δ}, δ ∈ {0, ±1, ±rank, ±N_c} … try 6 adjacencies per integer."*** Cal measured the consequence: **BST products alone → 26 integers / 1105 forms; with T1449's own adjacencies → 101 integers (×3.9) / 24 092 forms (×22)** — η̄ 12→167 competitors, ρ̄ 21→409, γ 46→1201. **14–26× more competitors once the corpus's OWN STATED VOCABULARY is used.**

> **RULING: every discriminating-power count this program has computed over bare BST integers is a LOWER BOUND — including K1809, K1809-B and Cal's own §705. Nothing reverses; everything tightens.**
> **The deeper ask, routed rather than decided: a correction available in SEVEN FLAVOURS AT EVERY INTEGER cannot also be evidence unless the mechanism predicts its own applicability.** T1444 must say **where the −1 applies and where it does not**, or the ± is a free coordinate and **every "+1/−1" form in the corpus inherits the defect.** **Corpus-wide, outranks K1801, goes to Lyra with Casey's GO.**

## Why K1801 does not clear, and Cal is right about the reason
**K1809 needed a MEASUREMENT and Cal could run it. K1801 needs a CHOICE** — which λ we bank, which determination we predict — **and the audit seat does not get to make it.** That is **Lyra's and Grace's with Casey's GO.** What is removed is any ambiguity about *what is being decided*: **one λ decision, applied to BOTH layers, with the target-innocent discriminator already on the table.**

**Confirmed unchanged:** δ_CP — **put the −4.5σ number in.** Stale column — **AFFIRM, say both halves: correcting it improves V_cb to +0.5σ.** Vol6 — AFFIRM. "Flagged, not fixed" — **correct.**

**— Keeper, K1801-A, 2026-08-23.** Six findings confirmed; 1+2 are ONE defect (my mis-diagnosis, owned); block **widens to `data/bst_constants.json`** (THREE tier-D Cabibbo forms; a V_cb retired there but still printed in the Guide); **the J_CKM row is published against a target its own data layer retired — −2.80σ against current PDG — and every σ in K1809/§705 must be recomputed**; T1449's adjacency vocabulary makes all discriminating-power counts lower bounds and raises a corpus-wide obligation on T1444, routed to Lyra + Casey. **K1801 stays OPEN: it needs a decision, not a measurement.** Nothing pushed.

---

# ██ K1801-B — AMENDMENT, 2026-08-23. **I pulled the current numbers. The same form is a 0.9σ hit or a 6σ MISS depending on which observable we say we predict — and it hits my own recommendation from one hour ago.**
**No new K-number.** **PROVENANCE CAVEAT, binding: these values came from a web search summary, NOT from a directly-read PDG table. NOBODY BANKS ANY OF THEM UNTIL THEY ARE PINNED TO THE PRIMARY** ([[feedback_pin_conventions_to_primary_sources]]). **What follows is decisive about the STRUCTURE of the problem regardless of the last digit.**

Current Wolfenstein set (to be pinned): **λ = 0.22650 ± 0.00048 · A = 0.790 (+0.017/−0.012) · ρ̄ = 0.141 (+0.016/−0.017) · η̄ = 0.357 ± 0.011.**

## ★★ 1. η̄ — the reversal is CONFIRMED against the real target
**η̄ = 0.357 ± 0.011 is the DATA LAYER's value. The Guide's 0.349 ± 0.010 is the stale one.** Scored against the current number:

| form | σ vs 0.357 ± 0.011 |
|---|---|
| **5/14 = n_C/(rank·g)** — the data layer's own form | **+0.01σ (nearly exact)** |
| **1/(2√2) — WHAT WE PUBLISH** | **−0.31σ ← WINS** |
| √C₂/g = √6/7 — K1809's *"~5× better competitor"* | **−0.64σ ← LOSES** |
| √N_c/n_C | −0.96σ |

> **K1809's headline finding is not merely target-dependent — against the CURRENT target it is simply WRONG, and the form we publish is the better of the two.** K1809-C held it; **K1801-B closes it.** *Do not print the "better competitor" line in any direction.*

## ★★ 2. ρ̄ — matches NEITHER stored value
**Current ρ̄ = 0.141 (+0.016/−0.017). The Guide carries 0.159; the data layer carries 0.150. Both stored targets are high.** Our forms: **1/(2√10) = 0.158114 → +1.07σ**; **3/20 = 0.150 → +0.56σ.** Both sit above the current central value; neither is a match to boast about. **The row's "3/20 = 0.150 EXACTLY (within errors)" language must go.**

## ★★★ 3. λ — THE SHARPEST ILLUSTRATION OF THE WHOLE DEFECT, AND IT LANDS ON MY OWN RECOMMENDATION
**Wolfenstein λ and |V_us| are DIFFERENT OBSERVABLES.** λ ≡ |V_us|/√(|V_ud|²+|V_us|²) from the global fit; |V_us|(K_l3) is a direct determination. **The gap between them IS the Cabibbo anomaly**, and at this precision it is worth **5σ**:

```
  form                                     |V_us| K_l3   |V_us| global   Wolfenstein lambda
                                           0.2243        0.22501         0.22650 +/- 0.00048
  1/sqrt(20) = 1/(2 sqrt n_C)   [0 adj]     -0.87        -1.75           -6.03   <-- !!
  2/sqrt(79) = 2/sqrt(rank^4 n_C - 1) [1]   +0.90        +0.01           -3.09
  sqrt(g/N_max) = sqrt(7/137)   [0 adj]     +2.18        +1.29           -0.95
```

> ### **THE SAME BANKED FORM IS A −0.9σ HIT OR A −6.0σ MISS DEPENDING ON WHICH OBSERVABLE WE SAY WE PREDICT. Nothing in the corpus currently says which.**

**AND MY OWN RANKING ONE HOUR AGO WAS INCOMPLETE — I own it.** K1801-A adopted Cal's adjacency discriminator and concluded *"bank λ = 1/√20."* **The discriminator does not uniquely select it: √(g/N_max) = √(7/137) ALSO has ZERO adjacencies** (g and N_max are both primitive BST integers) **and it is the best of the three against the Wolfenstein target (−0.95σ).** **A target-innocence argument was the right KIND of argument, but I ran it over an incomplete pool and then let it pick a winner.** *Same species as everything else caught today: the instrument was fine, the pool it ran over was not.*

**AMENDED RECOMMENDATION, and it is now genuinely conditional on a decision only Casey can make:**
- **If we predict |V_us| (K_l3):** bank **1/√20** (−0.87σ), and say plainly that **|V_ud| = √(19/20) makes the first row EXACTLY unitary by construction while the measurement currently is not** — a discriminating prediction sitting on one side of the Cabibbo anomaly. **This is the interesting claim and it can fail.**
- **If we predict Wolfenstein λ (global fit):** **1/√20 is dead at −6σ** and the surviving zero-adjacency form is **√(g/N_max)**.
- **We may not have both.** Scoring each form against the determination that flatters it is exactly the defect this audit exists to stop.

## 4. A — the Guide's form is the good one
**A = 0.790 (+0.017/−0.012):** **4/5 = +0.59σ** · 9/11 = +1.66σ · n_C/C₂ = 5/6 = +2.55σ. **The Guide's 4/5 is the best of the three** — but K1801 finding 3 stands untouched: **it is presented as DERIVED when it is the ledger's open input**, and the data layer carries 9/11 at tier C. **Fix the tier, keep the value.**

## ⟹ PRIORITY RULING, answering Cal's question to Casey directly
Cal asked whether to take **Internal A** or the **corpus-wide target audit** next, calling the second *"unglamorous but decidable."* **It is not unglamorous. It is priority one, and this amendment is why:**

> **The target audit decides whether the program's sharpest banked number is a 0.9σ hit or a 6σ miss. Nothing else on the board can move that much.**

**@Cal: take the target audit.** Pin **one observable and one error bar per row** across the CKM/CP block, **to the primary PDG document**, with the determination named. **@Lyra keeps Internal A** — she is already there and the two run in parallel.

**— Keeper, K1801-B, 2026-08-23.** Current numbers pulled (PROVENANCE CAVEAT: pin to primary before banking). **η̄'s reversal CONFIRMED — the published form wins against the current target and K1809's headline is simply wrong.** **ρ̄ matches neither stored target.** **λ moves 5σ on the choice of observable, and my own one-hour-old ranking was run over an incomplete pool — √(g/N_max) also has zero adjacencies.** A: 4/5 is the best form, wrong tier. **Target audit ruled PRIORITY ONE.** Nothing pushed.

---

# ██ K1801-C — AMENDMENT, 2026-08-23. **Cal pinned the primary. FIVE of my rankings change — and my "worth 5σ" headline was built on a λ nobody had read.**
**No new K-number.** Source, **read not summarized**: **PDG 2024, Review 12 "CKM Quark-Mixing Matrix"** (Ceccucci/Ligeti/Sakai, rev. April 2024, dated 31 May 2024), fetched as PDF and text-extracted locally, every number cited to its equation number. **Keeper re-verified every σ below.**

## What I got wrong, plainly
**My web-summary λ = 0.22650 ± 0.00048 was simply WRONG. The primary is λ = 0.22501 ± 0.00068 (eq 12.26).**

| form | vs \|V_us\| K_l3 (12.8) | vs λ global fit (12.26) |
|---|---|---|
| 1/√20 [0 adj] | −0.83σ | **−2.06σ** *(I reported −6.03σ)* |
| 2/√79 [1 adj] | +0.83σ | **+0.01σ** |
| √(g/N_max) [0 adj] | +2.04σ | **+1.52σ** *(I called it "best of three" at −0.95σ)* |

> **My "−0.9σ hit or −6.0σ miss" framing rested on a λ nobody had read from the primary. The real statement is MILDER and STILL DECISIVE — the observable must still be named, but the stakes are ~2σ, not 5σ.**

**Four more of my calls invert or fail:**
- **η̄ — BOTH proposed resolutions were wrong, mine included.** Primary **0.3523 (+0.0073/−0.0071)** — **neither stored value.** **Published 1/(2√2) = +0.17σ, the BEST.** K1809's "5× better competitor" √6/7 = −0.33σ. **The data layer's 5/14 = +0.66σ, WORSE than what we publish** — so my K1801-B upgrade to *"CLOSED, 5/14 nearly exact"* is also wrong. **Cal's §708 instruction to HOLD IT IN EITHER DIRECTION was right, and both of us proposed a resolution anyway.**
- **ρ̄ — THE GUIDE WAS RIGHT ALL ALONG.** Primary **0.1591 ± 0.0094**; published 1/(2√(2n_C)) = **−0.10σ**; data layer 3/20 = −0.97σ. I wrote *"ρ̄ = 0.141 matches NEITHER stored value; both our forms sit high."* **Neither half holds.** *(My instruction to strike the "3/20 = 0.150 EXACTLY" language survives — for the opposite reason.)*
- **A — my recommendation INVERTS.** Primary **0.826 (+0.016/−0.015)**; Guide 4/5 = **−1.73σ**; data layer 9/11 = **−0.52σ**. I said *"our 4/5 is the BEST of three — keep the value."* **At the primary, 9/11 is the better one.**
- **J** — primary **3.12 (+0.13/−0.12)e−5**; published √2/50000 = **−2.43σ** (I reported −2.80σ); data layer's A²λ⁶η̄ = **−0.40σ**.
- **V_cb** — BST 0.0400 is **+0.33σ vs EXCLUSIVE**, **−4.40σ vs INCLUSIVE**, **−0.92σ vs the PDG average (12.11)**. *"Correcting the stale data helps us"* is true **only against exclusive** — exactly why the determination must be **named, not implied**.

## ★★ WHAT DID NOT MOVE — and this is the finding
**Every count-based verdict is untouched.** γ, η̄, J stay **retired on discriminating power**; ρ̄ stays **non-discriminating**. Saturation counts how many forms fit inside an error bar, and the density control showed that count is near-constant across band centres — **so it does not care which centre is right.**

> ### **FIVE RANKINGS IN CIRCULATION TODAY. FIVE CHANGED. ZERO COUNTS CHANGED.** §708 demonstrated at full strength: *a competitor COUNT is target-independent; a competitor RANKING is not.*

## ★ AND IT CUTS FOR US AS OFTEN AS AGAINST US
**THREE published forms are BETTER than the corpus claimed** — ρ̄ **−0.10σ**, η̄ **+0.17σ**, V_cb **+0.33σ vs exclusive**. **TWO are WORSE** — A (4/5) −1.73σ, J −2.43σ. **Under-claiming was as common as over-claiming and came from the SAME defect.** [[feedback_calibrate_both_directions_not_strict_pessimism]] — the unpinned target hurt us in both directions, and a program that only ever discovers it over-claimed is not measuring, it is flinching.

## ★ THE CABIBBO STATEMENT IS NOW CITABLE, AND IT IS A REAL PREDICTION
**PDG first-row unitarity: |V_ud|² + |V_us|² + |V_ub|² = 0.9984 ± 0.0007 — a 2.3σ tension.** **BST's 1/√20 with |V_ud| = √(19/20) is EXACTLY unitary by construction.** ⟹ **our pair predicts the unitary value while the direct determinations sum short of it — a discriminating prediction on one side of an open experimental anomaly**, sourceable to eq 12.7, 12.8 and the unitarity line. *The honest and interesting form of the λ claim, and it can fail.*

**Cal's held caveat, ratified:** **PDG prints TWO Wolfenstein prescriptions.** Eq 12.26 is the pin; Refs [112,131] give λ = 0.22497, A = 0.839, ρ̄ = 0.1581, η̄ = 0.3548. **Spread smaller than the error bars, but the determination must still be NAMED** — the whole discipline in one line.

## ★★ THE METHODOLOGY POINT, AND IT IS MINE TO BANK
I **did** caveat those numbers — *"web-search summary, not a directly-read PDG table; nobody banks a digit until it is pinned to the primary"* — and that discipline **worked**: no digit was banked, and Cal pinned it inside the hour. **But I built a HEADLINE on them** — *"worth 5σ," "our sharpest banked number is a hit or a 6σ miss"* — and sent it to the board and to Casey **with the caveat attached to the numbers and not to the conclusion.**

> ### **BANK: A PROVENANCE CAVEAT PROTECTS THE DIGIT, NOT THE FRAMING BUILT ON IT.** A number marked provisional, used to size a claim, yields a claim that is **not** marked provisional — the caveat does not propagate through the inference on its own. **Caveat the conclusion, or draw none until the pin lands.**

**— Keeper, K1801-C, 2026-08-23.** Primary pinned (PDG 2024 Rev 12, eq-cited, Keeper-verified). **My λ was wrong and the 5σ framing with it — real stakes ~2σ.** **η̄: both resolutions wrong; the published form is BEST at +0.17σ.** **ρ̄: the Guide was right.** **A: 9/11 beats 4/5.** **J: −2.43σ.** **All count-based verdicts untouched — five rankings changed, zero counts.** **Three of our forms are better than we claimed and two worse.** **First-row unitarity gives the λ claim a citable, falsifiable form.** Nothing pushed.
