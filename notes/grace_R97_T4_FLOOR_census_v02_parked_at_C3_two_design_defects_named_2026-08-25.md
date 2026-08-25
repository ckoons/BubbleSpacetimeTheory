---
node_type: final_state_floor
title: "T4 FINAL STATE = FLOOR: census v0.2 implemented faithfully, 4/5 controls PASS, C3 FAILS structurally — instrument PARKED, not tuned. Two v0.3 design defects named exactly, one of them an instrument at war with the house discipline."
author: Grace
date: 2026-08-25
status: "Per the R97 contract: a named floor IS a final state. play/collision_census_v02.py exists and gates itself; data/collision_census_v02.json was NOT written — the gate refused, as built."
cell: "Internal D (instrument layer)"
---

# The run (2026-08-25, clock-verified)
Implemented exactly as the filed design specifies — subject-anchored attribution with NO radius parameter, the alias-table face, five corpus-sourced controls, gate-before-live.

| control | result |
|---|---|
| C1 must-catch — "address" attributed in the Item-3 ledger | **PASS** |
| **C2 must-reject — "commit" NOT attributed in the A2 artifact** | **PASS — the structural rule fixed v0.2-draft's original failure** |
| C3 must-reject — "address" NOT attributed in the R92 stratum flag | **FAIL — attributed** |
| C4 must-catch — alias(gauge normalization) ∋ gauge-kinetic | **PASS** |
| C5 must-reject — no stopword-only merges | **PASS** |

**GATE VERDICT: PARKED. The instrument refused to go live, as built. Nothing was tuned.**

# The diagnosis (understanding, not tuning) — TWO design defects, named exactly
**D1 — the attribution unit is ill-defined on markdown prose.** The design says "one sentence"; the corpus's sentences run through em-dashes, bold markers and parentheticals that a [.!?]-splitter cannot see. The offending chunk (383 chars) merges the stratum-collision clause with the address-mention clause into one "sentence." **Fix class: clause-level segmentation or a real sentence model — a v0.3 DESIGN change requiring its own review, not an in-run adjustment.**
**D2 — the between-check is blind to SUBSCRIPTED forms.** "stratum" was present between "address" and the marker — as **stratum_KW**, which the bare-name check does not match. **The irony is the finding: subscripting is the house fix for collisions, so the better the team's hygiene, the blinder this check becomes. An instrument at war with the house discipline is mis-designed by definition.** Fix class: a name's subscripted forms ARE the name (the alias table's own logic, applied to the attribution face — the two faces need each other).

# ★ THE AUTHORIZED v0.3 ATTEMPT (same day, Keeper's ruling, strict terms) — RUN, AND THE FLOOR STANDS
**Prediction filed BEFORE the run:** the offending clause's real blocker is the ANAPHOR "it" (referring to "stratum"); D2's forms-resolution cannot see an anaphor and D1-typographic splitting leaves the clause intact — predicted C3 FAILS AGAIN. **Run: C1 PASS · C2 PASS · C3 FAIL — prediction CONFIRMED.** The typographic split even isolated the minimal proving clause: *"but unsubscripted **it** is a collision waiting to fire, and it feeds census prediction #3 ('address')"* — the subject is an anaphor, and no forms-resolution can resolve a pronoun.
**⟹ THE FLOOR STANDS as T4's final state, per the ruling's own term (3). And the diagnosis SHARPENS: D3 (subsuming D1) — the design's "grammatical subject" requires ANAPHORA RESOLUTION, i.e., a real sentence model — exactly what term (2) defers to its own review. v0.3-with-a-sentence-model is the named future work; no v0.4 today.**
**The D2 fix (forms-are-the-name) is REAL and KEPT for that future version — it is correct on its own terms and C2's pass under it confirms the structural approach; it simply is not the C3 blocker.**

# WATCH ENTRY (K1829, entered under the frozen rule — post-closure; the prediction experiment remains MISS)
**Fired collision: "no Higgs channel" is overloaded — channel_k0 (the even grid, neutrino/up; 5461's object) vs channel_νW0 (the tau's Wallach ν = 0; the K1749-B pile).** One phrase, two addresses, caught by the T6 audit before any lane composed across it. **Scores by its name: not among the predicted three — one more elsewhere, after closure. The experiment's MISS is unchanged.**

# What stands
The alias-table face (C4/C5 green) is sound but ships only with the whole instrument — no partial go-live. v0.1's screen remains available AS A SCREEN (its MISS-scored prediction record untouched). **The v0.3 design owes: D1 + D2, and the observation that Face 2's alias logic is the repair for Face 1's D2 — one more instance of the two faces being one map.**

*— Grace, T4 floor. Two versions, two gate-refusals, zero tuned controls. The instrument that will eventually ship will have earned it.*
