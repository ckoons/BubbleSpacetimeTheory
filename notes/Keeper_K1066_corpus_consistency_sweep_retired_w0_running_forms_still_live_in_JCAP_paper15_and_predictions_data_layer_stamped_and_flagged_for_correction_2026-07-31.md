---
node_type: k_audit
id: K1066
title: Corpus-consistency sweep for the RETIRED running-w₀ dark-energy forms (w₀=−1+n_C/N_max²=−0.99973 and the −0.949 variant), now superseded by the committed w=−1 position (K1040) + the blind ε(a)=0 derivation (K1064). RESULT: the GO'd papers + the position doc + the ladder paper are CLEAN (all use w=−1 correctly). TWO live artifacts still carry the retired forms as active predictions: (1) BST_JCAP_CMB_Five_Integers.md (Paper #15, JCAP-target) presents w₀=−0.99973 in four places (results table line 74, a whole Section 6.2 lines 228-234, falsifier F11 line 294, summary line 305) — EXTERNAL-RISK; STAMPED with a NOT-FOR-EXTERNAL superseded-DE banner today (correction owner Lyra); (2) data/bst_predictions.json carries w=−0.99973 as an alternative prediction (line 857) + the K1033 "dynamical breathing mode" lead (lines 873, 127) that Elie's blind ε(a)=0 derivation explicitly REFUSED as the target-aware trap — data-layer, correction owner Grace. Severity MODERATE (external-risk on the JCAP paper; live data-layer inconsistency). This is the "grep the retraction before citing corpus" discipline applied proactively — it found real drift.
date: 2026-07-31
author: Keeper
verdict: Sweep done. Live cosmology-facing corpus is MOSTLY clean on w=−1; two artifacts still present the retired running-w₀ forms as live. JCAP Paper #15 STAMPED (non-destructive superseded-DE banner, external-risk closed pending Lyra's rewrite). Data layer bst_predictions.json flagged for Grace (lines 857/873/127 → w=−1; retire the dynamical-breathing lead per K1064's refusal). w=−1 (K1040) + ε(a)=0 (K1064) is the single committed position; the −0.99973/−0.949 running forms are fits, retired.
---

# K1066 — Corpus sweep: retired w₀ running forms still live in two artifacts

Proactive application of *grep-the-retraction-before-citing-corpus*: with w=−1 committed (K1040) and ε(a)=0 derived blind (K1064, the (1−f)/breathing-mode dynamical form explicitly refused as the −0.949 trap), I swept the live cosmology-facing corpus for any artifact still presenting the retired running forms — `w₀ = −1 + n_C/N_max² = −0.99973` and the `−0.949` variant — as a current BST prediction.

## Clean (correct w=−1 — no action)
- `BST_Falsifiable_Predictions_Paper_v0.1` (GO'd) — w=−1, committed; DESI w₀≈−0.84 shown as tension. ✓
- `BST_Color_Mixing_Duality_PAPER_DRAFT` (GO'd) — "BST derives a cosmological constant (w=−1)"; the Σm_ν edge-kill correctly leans on the tight bound w=−1 commits to. ✓
- `BST_Cosmology_Position_Geometric_Lambda_from_Fixed_Volume...` — w=−1, deviation ≤10⁻⁴ → 0; interstasis reconciliation (breathing is *inter-cycle*, not the intra-cycle EOS). ✓
- `BST_Heat_Trace_Ladder_Unification_PAPER_DRAFT` — "w=−1 forced… Forcing beat two fits (−0.99973 and −0.949) in real time." ✓

## Inconsistent — retired forms still live (findings)

**Finding 1 (MODERATE, external-risk) — `BST_JCAP_CMB_Five_Integers.md` (Paper #15, target: JCAP).**
Still presents `w₀ = −0.99973` as its live DE prediction in four places:
- results table (line 74): `w₀ | −1 + n_C/N_max² | −0.99973 | consistent`
- Section 6.2 (lines 228-234): "w₀ = −0.99973: not exactly −1" — derives it from "the residual breathing mode of the n_C=5 complex dimensions."
- falsifier F11 (line 294): `w₀ = −0.99973`
- summary (line 305): "w₀ = −0.99973 (not exactly −1)"
This is a *journal-target* paper carrying the retired form. **Action taken:** stamped a **NOT-FOR-EXTERNAL-DISTRIBUTION superseded-DE banner** at the top today (non-destructive; the "stamp superseded, never delete" discipline). **Correction owner: Lyra** — rewrite the DE section to w=−1 (fixed C·π⁵ volume, K1040; ε(a)=0 blind, K1064) before any external consideration. The CMB content is unaffected.

**Finding 2 (MODERATE, live data layer) — `data/bst_predictions.json`.**
- line 857: `"prediction": "Dark energy equation of state w = -1 exactly (or w = -1 + n_C/N_max^2 = -0.99973)..."` — presents the retired form as a live alternative.
- lines 873 + 127: the **K1033 "dynamical breathing mode" lead** (written 2026-07-30, *before* K1040/K1064) — "static BST w₀=−0.99973 already tilts w₀>−1, same direction DESI favors… make the breathing mode dynamical (wₐ≠0, quintom)… fixes DE + Σm_ν at once." This is precisely the ρ_DE ∝ (1−f(a)) breathing-mode dynamical form that **Elie's blind ε(a) derivation named and refused as the −0.949 relapse (K1064)** — target-aware, chosen because it matches DESI's direction.
**Correction owner: Grace** — reconcile lines 857/873/127 to w=−1 (retire −0.99973 as the prediction; the dynamical-breathing lead is superseded by the blind ε(a)=0, not a live lead). Note the honest nuance: the *substrate-coupling* correction to w=−1 remains a legitimate open forward piece (K1064 scope note), but it is NOT the DESI-matching breathing mode — that specific form was refused.

## Disposition
- Single committed position: **w = −1 (K1040) + ε(a)=0 blind (K1064)**; the −0.99973 and −0.949 running forms are **fits, retired**.
- JCAP Paper #15 external-risk **closed** by the banner pending Lyra's rewrite; data-layer inconsistency **flagged** for Grace.
- Added to team prompt 2026-07-31r hygiene lane.
- README already reconciled today (separate record).

— K1066, Keeper, 2026-07-31. Sweep found the retired running-w₀ forms still live in JCAP Paper #15 (stamped, external-risk closed, Lyra to rewrite) + bst_predictions.json (flagged for Grace: 857/873/127). w=−1 + ε(a)=0 is the committed position. See K1040, K1064, K1063, feedback_grep_retraction_before_citing_corpus.
