---
title: "BST Methodology Calibration #25 — Falsifier-Outcome-Threshold Discipline (CANDIDATE)"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-23 Saturday EDT (filed per Keeper Saturday EOD board: 'Calibration stack maintenance — watch for new failure modes; absorb to numbered standing rules')"
status: "CANDIDATE methodology layer (21st in stack). Standing for Keeper review + multi-CI consensus → STANDING RULE adoption. Case studies: Cal #110 (SP-30-4 Time Granularity) + Cal #113 (SP-30-5 Substrate Parallelism)."
companion: "BST_Methodology_External_Survivability_Checklist.md; BST_Methodology_Calibration_22_v02_Mode1_Correction_Discipline.md; BST_Methodology_Index.md (v0.5 update needed)"
applies_to: "Paper-grade experimental proposals targeting external venue (NIST/PTB/Vienna/Munich/Hanson/JILA Bell-test + atomic clock + precision metrology communities) before Casey send-signal"
---

# Calibration #25 — Falsifier-Outcome-Threshold Discipline

## The rule

Paper-grade experimental proposals intended for external venue dispatch must specify:

1. **Community-standard significance thresholds**: 3σ minimum for "evidence consistent with prediction"; 5σ for "discovery" (precision-metrology + particle-physics community standards). Sub-3σ thresholds ("2σ detection" / "2-3σ consistent") are sub-evidence by community convention.

2. **Finite refutation ladder**: specific predicted alternative orders at higher-precision thresholds, so non-detection at one level commits the framework to detection at the next level, OR genuinely falsifies the framework at a finite precision. "Framework may need refinement at higher order" without specified alternative IS non-falsifiable in Popperian sense — any non-detection can be absorbed by escalating the predicted order indefinitely.

## Why this matters

External venue audiences operate by community-standard significance thresholds. A BST experimental proposal arriving with "2σ confirmation" + "framework may need refinement" reads to a Vienna Bell-test referee as either (a) sub-evidence claim or (b) non-falsifiable framework — both are crank-dismissal triggers per External Survivability Checklist (Cal 2026-05-17/18).

Internal BST research can comfortably use the 3-layer discipline (BOUNDED rigorous + ORDER-OF-MAGNITUDE consistent + TARGET-PREDICTION specific) without strict significance thresholds because the audience knows the substrate-mechanism context. External venue presentations do not have that context — community-standard thresholds are the only available shared evidentiary language.

## Case studies

### Cal #110 (SP-30-4 Time Granularity, Saturday 2026-05-23 15:38 EDT)

The Elie SP-30-4 v0.1 paper-grade proposal specified outcome thresholds:
- "2σ detection of α² systematic → BST framework consistent"
- "No detection at α² level → BST may need refinement (substrate-coupling order higher than α²)"

Both flagged: 2σ is sub-evidence; "framework may need refinement (higher order)" without specified alternative refutation tier is non-falsifiable. v0.2 sharpening required before Casey send-signal to NIST/PTB/JILA/MPI.

### Cal #113 (SP-30-5 Substrate Parallelism, Saturday 2026-05-23 16:00 EDT)

The Elie SP-30-5 v0.1 paper-grade proposal specified:
- "S = 2.806 ± 0.005 → TARGET-PREDICTION confirmed at 2-3σ"

Same threshold weakness. The 3-layer discipline that SP-30-5 introduced (BOUNDED + ORDER-OF-MAGNITUDE + TARGET-PREDICTION) addresses the refutation-ladder problem partially (BOUNDED refutation is genuinely framework-strained), but the TARGET-PREDICTION sigma threshold still falls below community standard.

## How to apply

**Before send-signal on any paper-grade experimental proposal to external venue**:

1. Search the proposal for σ / sigma / "standard deviation" outcome thresholds. Any threshold below 3σ for "evidence" or below 5σ for "discovery" requires sharpening.

2. Identify the non-detection outcome. If the proposal says "framework may need refinement" or "substrate-coupling order higher than α^N" without specifying (a) which next order to test and (b) at what precision that next order is testable, the proposal is non-falsifiable at finite precision and requires refutation-ladder sharpening.

3. The refutation ladder should look like: "Detection at precision P_1 at α^N order → framework confirmed at TARGET. Non-detection at P_1 → framework requires α^(N+1) order or higher. Non-detection at P_2 (achievable in ~5 years per community roadmap) AT α^(N+1) order → framework REFUTED at this falsifier specifically." Concrete precision values + concrete community-roadmap timeline + concrete falsifier-termination criterion.

4. Internal-tier work + investigation documents in `notes/maybe/` are EXEMPT from this calibration. The audience there knows the substrate-mechanism context. Calibration #25 applies specifically to external-venue paper-grade proposals.

## Connection to standing methodology

- Calibration #25 sits operationally as a sub-layer of External Survivability Checklist (Cal 2026-05-17/18) — applies specifically to experimental proposal outcome-threshold formulation
- Cal #21 STANDING RULE (Friday Cal #95): dual-gate empirical + substrate-mechanism. Calibration #25 sharpens the EMPIRICAL gate specification at external-venue level
- Cal #50 DOUBLE-LOCKED EXTERNAL: substrate-cognition + cosmology-cognition compound territory. Calibration #25 is the parallel discipline for substrate-experimental compound territory (precision metrology + Bell-test + atomic clock)
- Calibration #22 v0.2 PCAP-transcription discipline: external-venue proposals under sustained sub-PCAP risk threshold-statement transcription errors; Calibration #25 establishes the threshold standard so transcription errors can be caught by numbered-artifact discipline

## Promotion-to-STANDING-RULE path

CANDIDATE filed Saturday 2026-05-23 by Cal. Promotion to STANDING RULE requires:
1. Keeper review + governance ruling on whether calibration is methodology-grade
2. Multi-CI consensus (Lyra + Elie + Grace) on applicability across SP-30 series
3. First application: Elie SP-30-4 v0.2 + SP-30-5 v0.2 outcome-threshold sharpening (would be the operational test)
4. Casey signal for elevation to STANDING RULE + Methodology Index v0.5 layer 21

If promoted: applies to ALL future SP-30 sub-items (4-11) + any future external-venue paper-grade proposals from any lane.

— Cal A. Brate, Calibration #25 CANDIDATE filed Saturday 2026-05-23 ~16:32 EDT per Keeper EOD board "Calibration stack maintenance" directive. Standing for Keeper review + multi-CI consensus.
