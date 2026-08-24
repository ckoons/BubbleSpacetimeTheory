---
node_type: instrument_design
title: "CENSUS v0.2 DESIGN — one pass, two faces: the marker-ATTRIBUTION fix (the failed must-reject's real repair) and the ALIAS TABLE (the search-disease face). Design only; implementation after review."
author: Grace
date: 2026-08-24
status: "Own-time, Casey-authorized. Replaces the parked v0.2 patch. Not implemented until this design survives a read."
---

# Face 1 — the blindness check, repaired by ATTRIBUTION, not window-tuning
**The v0.2 draft failed its must-reject** ("commit" flagged because collision-language about OTHER names sat nearby). The failure named the defect: **proximity is not aboutness.** The repair is structural:
> **A collision-marker attributes to name X only if X is the GRAMMATICAL SUBJECT of the marker clause** — operationalized: the marker phrase and X co-occur within one sentence AND no other census-name sits between X and the marker. Sentence-scoped, subject-anchored — not a distance window (no radius parameter exists, so none can be tuned).
**Controls, corpus-sourced, fixed before implementation:** must-catch: my Item-3 ledger's "the electron's ADDRESS is TWO OBJECTS" (subject = address) · must-reject: my A2 artifact's commit-anatomy passages (subject = the anatomy, marker-language about other names) · second must-reject: R92's stratum flag must NOT attribute to "address". **If any control fails, the design is wrong — report, don't tune.**

# Face 2 — the ALIAS TABLE (the search disease; the dual projection)
The same gloss-cluster harvest, INVERTED: cluster the GLOSSES (by head-noun similarity), and for each cluster list the NAMES that carry it. A cluster with ≥2 names = an alias set — one object, many names.
> **Consumer contract: every "shelf empty / not banked" verdict MUST cite the alias set it swept** (the house guard: a verdict is only as good as its swept name-set). The table makes the guard executable: `alias_of("gauge normalization") → {gauge-kinetic, current-current, Killing-form norm, F² coefficient, …}`.
**Control: the Keystone A miss as must-catch** — the alias set for "gauge normalization" must contain "gauge-kinetic" (the two names that failed to meet on 08-24). Must-reject: two clusters whose glosses share only stopwords must NOT merge.

# One schema, both faces
`data/collision_census.json` gains: per-name `subject_attributed_markers` (face 1) and a top-level `alias_sets` (face 2). The predictions ledger gains the mandatory `blindness_check` block (per-prediction verdict, run at filing, on the filer's same-day artifacts, using face-1 attribution). **v0.2 ships only when all five controls pass in one run, gate-before-read.**

*— Grace. The two diseases are one map's two projections; v0.2 is one instrument reading both directions, with its repair derived from its own failure rather than tuned past it.*
