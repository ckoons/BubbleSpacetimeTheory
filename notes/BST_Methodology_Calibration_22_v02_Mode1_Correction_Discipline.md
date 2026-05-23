---
title: "BST Methodology — Calibration #22 v0.2 STANDING RULE: Mode 1 Correction Discipline + Absorption-Pipeline Extension"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-23 Saturday Wave 2 morning EDT (`date`-verified)"
status: "v0.2 — Formalization of Calibration #22 STANDING RULE per Cal #100 + Cal #101 + Cal #103 series. Extends Keeper Friday EOD #22 v0.1 (numbered referee log entries for Mode 1 corrections) with v0.2 absorption-pipeline rule (description-text quoting + sig-fig comparison discipline). 18th methodology stack layer."
companion: "BST_Methodology_Index.md (Cal v0.4+); Cal #100 + #101 + #103 referee log entries; Keeper Friday EOD Calibration #22 proposal"
target: "BST team (Lyra, Elie, Grace, Keeper) — operational discipline under sustained sub-PCAP cadence"
---

# Calibration #22 v0.2 STANDING RULE — Mode 1 Correction Discipline

## Why this v0.2 extension

Calibration #22 v0.1 (Keeper Friday EOD per Cal #100 origin) established the basic rule: **no verbal-only retractions; numbered referee log entries for all Mode 1 corrections**.

Saturday morning empirically tested the v0.1 rule across 4 instances (Cal #98 origin → Cal #100 self-correction → Cal #101 Grace INV-4890 catch → Cal #103 Grace INV-4897 catch). The v0.1 rule worked for the verbal-only retraction failure class but did **NOT** prevent a new failure class: **absorption-introduced errors during description-text restatement**.

v0.2 extension addresses the absorption-pipeline class via explicit absorption-text quoting + numerical comparison discipline.

## The four-instance error chain (Cal #100 + #101 + #103 case study)

| Level | Event | Error class | Caught by |
|---|---|---|---|
| L1 | Vol 1 Ch 11 v0.7 pre-Cal-#100 | Original arithmetic error (24/π² ≈ 2.432 incorrect; gave 206.85 instead of 206.761) | Cal #100 |
| L2 | Cal #98 erroneous flag | Cal-side arithmetic error (claimed 0.05-0.06% instead of correct 0.003-0.004%) | Cal Mode 1 verbal self-correction |
| L3 | Verbal-only retraction propagation failure | Absorption pipeline picked up wrong flag, not retraction; Elie + Lyra + Grace propagated 0.05-0.06% across Vol 2 Ch 3/5 + Vol 1 Ch 11 + Grace INV-4890 | Calibration #22 v0.1 (Keeper Friday EOD); Cal #100 retroactive |
| L4 | Absorption-introduced error during description-text restatement (Grace INV-4890 v0.1) | Description text claimed "(24/π²)^6 = 206.7682... matches PDG to 9 sig figs" — fabricated value + wrong sig-fig count | Cal #101 Saturday morning |
| L5 | Same error class re-introduced in NEW catalog entry (Grace INV-4897 Saturday) | Same "9 sig figs match" claim re-introduced when filing new Saturday entry referencing Cal #100 | Cal #103 Saturday |

**Pattern**: even after numbered referee log entries (v0.1 rule), absorption can introduce NEW errors in description text by restating numerical claims that aren't in the referenced Cal entry verbatim.

## v0.2 STANDING RULE Extension

When absorbing a numbered Cal correction into catalog/chapter/paper/data layer:

### Rule 22.2a — Direct Quote Discipline

**Absorption text MUST quote exact numerical figures from the referenced Cal entry**, NOT re-derive or restate during absorption.

Bad pattern (Cal #103 case):
```
"Cal #100 verified figure: (24/π²)^6 precision = 0.004% D-tier 
 (matches PDG 2024 m_μ/m_e to 9 significant figures)"
```
The "9 significant figures" claim was NOT in Cal #100 — it was introduced during absorption. The Cal #100 verified figure was 0.004% deviation; sig-fig count is derived, not asserted.

Good pattern:
```
"Cal #100 verified figure: (24/π²)^6 = 206.7612 (computed); 
 m_μ/m_e measured = 206.7682830 (PDG 2024); 
 fractional deviation 0.0071/206.7683 = 3.4×10⁻⁵ = 0.004% (D-tier)"
```
Includes explicit numerical comparison; sig-fig match is derivable by reader, not asserted.

### Rule 22.2b — Reference Numbered Entry Explicitly

Absorption text MUST mark the absorption with the referee log entry number explicitly (e.g., "per Cal #100"). This enables reverse-traceability — any reader can navigate to the referenced entry to verify the absorption claim against the source.

### Rule 22.2c — Sig-Fig Match Claims Derived, Not Asserted

If absorption text includes "matches to N significant figures" claim, the N MUST be derived from explicit numerical comparison (computed value vs measured value), not asserted in a description.

Bad: "matches to 9 significant figures"
Good: "matches: 206.7612 (BST) vs 206.7682830 (measured); deviation 0.0071/206.7683 = 0.004% (D-tier 4-sig-fig match)"

### Rule 22.2d — Numerical Recomputation Step or Reference

When absorption involves numerical values, EITHER:
1. Include the numerical recomputation step in the absorption text (preferred for catalog entries), OR
2. Mark as "value derived per Cal #N, see entry for arithmetic" (acceptable for non-canonical references)

NEVER restate numerical figures without including the computation path or explicit Cal-entry citation.

## Operational guidance

For each team CI lane:

- **Cal**: when filing Mode 1 corrections, include explicit numerical computation in the entry (not just verbal explanation). The entry IS the authoritative source for absorption.
- **Lyra**: when absorbing Cal corrections into chapters, quote the Cal-verified numerical figure exactly. If the chapter needs additional precision context (sig-fig match claim), derive it from the explicit comparison rather than asserting it.
- **Elie**: when absorbing Cal corrections into chapter/paper text + PDFs, run the numerical recomputation against the Cal-entry figure before regenerating PDFs. Catches PCAP-rate transcription errors before they propagate.
- **Grace**: when absorbing Cal corrections into catalog entries, the description text must include the explicit numerical comparison (computed vs measured + derived precision). Catalog descriptions are the most-quoted source — get them right.
- **Keeper**: when filing K-audit pre-stages absorbing Cal flags, reference numbered Cal entries explicitly + apply Rule 22.2a-d during description-text writing.

## Why v0.2 is needed in addition to v0.1

v0.1 (numbered referee log entries) eliminated verbal-only retraction failures. v0.2 (absorption-pipeline discipline) addresses the new failure class that emerged: even with numbered entries, absorption restatement during description-writing introduced new errors.

This is a **specific class of PCAP-rate transcription error** — under sustained sub-PCAP cadence, CIs writing description text for catalog/chapter absorption tend to paraphrase rather than quote, introducing arithmetic errors during paraphrase.

v0.2 rule: paraphrase is banned in absorption description-text; direct quote + numerical recomputation is required.

## Methodology stack position

Calibration #22 v0.2 is the **18th methodology stack layer** (per Vol 0 Ch 10 v0.4 + Keeper Friday EOD synthesis):

1-10. Original 10 layers
11. RIGOROUSLY CLOSED tier (Cal #77)
12. Within-session calibration discipline (Calibrations #18-#22)
13. Reframing-insight cadence
14. F1-F4 Bridge Object family-member criteria (Cal #63)
15. B1-B4 Bridge criteria
16. PCAP — Pre-Specification Cadence Acceleration Pattern (Cal #85)
17. Calibration #19 STANDING RULE — forecast-arithmetic vs ratified-state count (Cal #90(c))
18. **Calibration #22 v0.2 STANDING RULE — Mode 1 Correction + Absorption-Pipeline discipline (Cal #100 origin + Cal #103 v0.2 extension)**

## Cross-references

- **Cal #100** (Friday): origin of the four-instance error chain analysis
- **Cal #101** (Saturday): Grace INV-4890 absorption-introduced error catch
- **Cal #103** (Saturday): Grace INV-4897 same error class re-introduced; v0.2 extension recommended
- **Keeper Friday EOD Calibration #22 v0.1 proposal**: numbered referee log entries for Mode 1 corrections (the base rule)
- **BST_Methodology_Index.md** (Cal v0.4+): navigation infrastructure — Calibration #22 v0.2 added as 18th layer

## Filing status

**v0.2 FILED Saturday 2026-05-23 ~11:50 EDT per Cal own-cadence per Cal #103 recommendation.** Extends Keeper Friday EOD #22 v0.1 with absorption-pipeline rule. Standing for Casey + Keeper ratification.

— Cal A. Brate, Saturday 2026-05-23 11:50 EDT
