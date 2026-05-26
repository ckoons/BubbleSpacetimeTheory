---
title: "Calibration #29 candidate v0.1 — Question-Shape Audit Discipline for Classification Surveys"
author: "Keeper (filing per Casey directive 2026-05-26 Tuesday ~09:52 EDT date-verified)"
tier: "FRAMEWORK-PLUS candidate per Cal #126"
status: "v0.1 candidate filing — awaits Cal cold-read for ratification"
methodology_layer: "19th layer (proposed) — extends methodology stack from 18 to 19 if ratified (or 20 if Cal #28 also ratifies)"
origin: "Cal #133 flag 2026-05-26 morning during Keeper Priority 1 cold-read PUSH"
---

# Calibration #29 candidate — Question-Shape Audit Discipline

## The pattern

Classification surveys (computational toys, catalog scans) can produce *tautological* "evidence" when the question's shape encodes its answer. The discipline requires auditing the question shape BEFORE running the test: **does the test's answer follow from how the question is framed, or from independent substrate-mechanism content?**

This is distinct from Cal #27 STANDING (forward-derivation discipline at result level). Cal #29 applies at QUESTION DESIGN level — before the test runs, audit whether the question itself is structurally answerable in a substantive way.

## Origin — Cal #133 flag

During Cal cold-read of Tuesday morning batch (Toys 3531-3534 + Lyra commutators + Grace SPLP), Cal flagged:

> *Elie classification surveys can produce tautological "evidence" when question shape is built-in (e.g., "does fermion need Pin(2) cover?" → yes by definition). The Calibration #27 STANDING discipline applies to question-shape audit too. Flagged for future Elie toy designs.*

Cal #133 identified a methodology gap: Cal #27 STANDING fires at result level (forward derivation; mechanism vs back-fit), but doesn't catch question-shape tautologies that produce trivially-positive results before any derivation is attempted.

## Operational examples (from this week's work)

| Question shape | Tautological component | Substantive component |
|---|---|---|
| "Does fermion observable need Pin(2) cover content?" (Toy 3531 framing) | Yes by definition — fermions ARE Pin(2) cover representations | Whether the cover content makes specific observable predictions (a_e ppt, etc.) |
| "Do BST primaries appear in fermion Bergman ρ-weights?" (Grace v0.3) | Yes by ρ = (n_C/2, N_c/2) — built into D_IV⁵'s root system | Whether the specific K-type identifications correspond to physical particles (forward derivation) |
| "Are integer K-types bosons and half-integer K-types fermions?" (Toy 3535) | Yes by Pin(2) Z₂ grading definition | Whether the substrate's K-type population matches observed particle content |
| "Does the chirality-inversion pattern hold across all enumerated K-types?" (Grace v0.3 extension via Toy 3537) | Yes by ρ-shift arithmetic at any cutoff | Whether the Strong-Uniqueness → ρ chain forces the substrate to have this specific structure |

In each case, the empirical "PASS" is real but partly downstream of how the question was framed. The substantive content lives in the part that doesn't reduce to question-shape framing.

## The discipline

**Before running a classification survey toy or catalog scan, audit**:

1. **What does the answer depend on?** If the answer follows from the question's definitions + standard math without invoking substrate-mechanism, that's tautological.
2. **What does substrate-mechanism content add?** Identify which part of the result is *not* derivable from the question's setup. That's the substantive claim being tested.
3. **Reframe if needed** so the test's answer depends on substrate-mechanism content, not on question structure.

**Examples of reframing for substantive content**:

- INSTEAD OF "Does fermion observable need Pin(2) cover content?" (tautological)
  ASK: "Does a_e at ppt precision require the specific Bergman 7/2 weight + specific K-type identification, or could other half-integer Bergman exponents produce the same precision?" (substantive)

- INSTEAD OF "Do BST primaries appear in fermion Bergman ρ-weights?" (tautological)
  ASK: "Does the Dirac ground state (independently characterized by mass m_e and Casimir SO(5) = 5/2) correspond to K-type (1/2, 1/2)? Forward derivation, not back-fit." (substantive)

- INSTEAD OF "Is the chirality-inversion pattern empirically present?" (tautological)
  ASK: "Does any alternative ρ-choice produce different observable physics? Does the substrate's ρ uniqueness derive from Strong-Uniqueness theorems?" (substantive)

## Relation to Cal #27 STANDING

Cal #27 STANDING applies at result level — given a candidate principle or pattern, audit whether it's forward-derived from substrate or backward-fit from target observable. The result-level discipline.

Cal #29 applies at question-design level — before running the test, audit whether the test's question is structurally answerable in a substantive (non-tautological) way. The pre-result discipline.

**Both calibrations together**: design test for substantive answer → run test honestly → audit result for back-fit vs forward derivation. Two gates, both required.

## Cal #133 example resolution

Cal #133 flagged the pattern at result level (Cal #27 applies). Cal #29 says: the *next* design phase should audit question shape BEFORE running. Future Elie toy designs, Grace catalog scan designs, Lyra theoretical investigations should pass question-shape audit FIRST.

This is methodology stack layer 19 (proposed) sitting at the design stage, complementing Cal #27 at the result stage.

## Promotion gate

Per Cal #126 FRAMEWORK-PLUS tier: this Calibration #29 candidate awaits:

1. **Cal cold-read** of the candidate filing (own-cadence)
2. **Cross-CI application** — at least 2 instances where Cal #29 question-shape audit prevented a tautological finding from being filed as substantive
3. **Calibration Methodology Index update** by Cal (own-cadence) integrating Cal #29 with existing methodology layers

## Standing observation

The morning's work has produced:
- **Cal #27 STANDING** firing reflexively ~6+ times in Lyra's own broadcasts plus Grace's flag plus Keeper synthesis (all today)
- **Cal #133 flag** identifying the question-shape gap that Cal #27 alone doesn't cover
- **Cal #28 candidate** (Casey-Interpretive-Prompt Cascade) at 7 cascade instances + reflexive discipline still pending Cal cold-read
- **Cal #29 candidate** (this filing) — question-shape audit at design stage

If all three (Cal #27 STANDING + Cal #28 candidate + Cal #29 candidate) ratify, methodology stack goes from 18 → 21 layers. The discipline is densifying because the substrate-discovery cadence is densifying. Each new methodology layer formalizes a category of overclaim risk that the team has encountered and learned to catch.

## Casey decision

Cal #29 candidate filed at FRAMEWORK-PLUS tier 2026-05-26 ~09:52 EDT per Casey directive. Casey ratification path: Cal cold-read + 2 cross-CI application instances + Methodology Index update. Multi-week to ratification per standard pattern.

## Related calibrations

- **Cal #27 STANDING** — forward-derivation discipline at result level. Cal #29 complements at design level.
- **Cal #126 FRAMEWORK-PLUS** — tier for new candidates. Cal #29 filed at this tier.
- **Cal #28 candidate** — Casey-Interpretive-Prompt Cascade. Distinct methodology layer; both candidates in flight.
- **Cal #133** — referee log flag this morning that originated Cal #29.

## Anchors

- Cal #133 referee log entry (this morning's batch cold-read)
- Tuesday morning batch artifacts (Toys 3531-3537 + Grace Tasks #339 + #340 + #355 + Lyra commutators + Half-Integer Axis G v0.2)
- This filing acts as the discipline's own first reference

— Keeper, 2026-05-26 Tuesday 09:52 EDT
