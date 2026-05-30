---
title: "Calibration candidate — Source-Verification Tier (RECALLED vs VERIFIED-CITED)"
author: "Keeper"
date: "2026-05-28 Thursday EDT"
status: "CANDIDATE, pending Cal cold-read + Casey. Number deferred to registry (suggest #33; Cal #22 numbered-artifact discipline). Motivated by a 2-recurrences-in-2-days sourcing failure on the deepest-gate claim — recording the lesson did NOT prevent recurrence, so a hard gate is proposed."
pairs_with: ["Cal #27 (forward-vs-identified)", "feedback_pin_conventions_to_primary_sources", "Cal #22 (numbered-artifact)", "Cal #32 candidate (parameter-role verification)"]
---

# Calibration candidate — Source-Verification Tier

## The rule
A claim that rests on a specific value or statement **from the literature** — a classification entry, a tabulated invariant, the exact statement *or scope* of a cited theorem — must be tagged one of:
- **VERIFIED-CITED** — the actual source text was checked/quoted *this session*.
- **RECALLED** — stated from memory, even when the citation is known.

**A load-bearing claim CANNOT advance past MATCHED on a RECALLED value.** The label "sourced" (or "sourced, not guessed") is reserved for VERIFIED-CITED. Knowing the citation is not the same as having checked it.

## Why (the recurrence that forces a hard gate)
Two failures in two days, both on the *deepest-gate* claim, both the same mechanism:
1. **FK genus** (last week): the genus name flipped 3× in one day from relabeling-from-memory; pinned only after deriving from the multiplicity formula. Recorded as `feedback_pin_conventions_to_primary_sources`.
2. **B̂₂ tube count** (today): Elie's E1b cited Dlab–Ringel but **stated the rule from memory** and labeled it "sourced, not guessed" — and it was wrong: the **simply-laced D̃/Ẽ "non-Ã → 3 tubes" theorem (≥5 vertices) was applied out of scope** to the 3-vertex non-simply-laced B̂₂ species. Cal #27 + the #407 audit caught it; Elie retracted cleanly.

**Recording the lesson did not prevent recurrence within a day.** A lesson is a soft norm; this needs a hard tier gate.

## How to apply
- When a claim invokes "by [theorem / classification / table]," the asserter states **whether the source text was checked this session.** If not → **RECALLED → the claim is capped at MATCHED** until VERIFIED-CITED.
- **Scope is part of the value.** The failure mode today was not a wrong number recalled — it was a *correct theorem applied outside its hypotheses* (D̃/Ẽ vs B̃₂). So VERIFIED-CITED requires checking that the cited theorem's hypotheses actually cover the case at hand, not just that the theorem exists.
- Especially binding on: Dynkin/classification data (tubular types, genus tables, Coxeter numbers), and any "standard theorem" invoked on a non-generic object (non-simply-laced, small rank, boundary cases).
- In-environment honesty: if the source cannot be opened here (e.g., a Memoir/monograph not extractable), the claim is **RECALLED by default** and stays MATCHED — exactly the disposition the B̂₂ tube count now carries.

## Disposition
Candidate. If ratified: it sits alongside Cal #27 (result-level forward-vs-identified) and Cal #29 (design-level) as the **sourcing-level** gate. It would have caught both recurrences at assertion time rather than at audit time.

— Keeper, 2026-05-28. The audit chain caught the miss; this is the structural fix so the *next* deepest-gate claim can't repeat it.
