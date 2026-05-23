# Keeper Calibration #22 v0.2 Extension — Absorption-Introduced Errors in Description Text (STANDING RULE update)

**Filed**: 2026-05-23 Saturday ~11:00 EDT (Keeper, formalizing Cal #101 + Cal #103 reinforcement)
**Status**: STANDING RULE v0.2 extension adopted operationally (per Cal-proposed + Keeper-formalized; Casey override available)
**Companion to**: `Keeper_Calibration_22_PCAP_Transcription_Error_Class.md` (v0.1 Friday EOD)
**Methodology stack layer**: 18a (extension of layer 18)

## Four-instance case study (Friday-Saturday 2026-05-22 → 2026-05-23)

Friday Calibration #22 v0.1 captured PCAP-rate transcription error class via two cases: K142 (Keeper-lane) + Cal #98→#100 (Cal-lane retraction-propagation). Saturday extension captures a third structural variant: **absorption-introduced errors in description text during artifact authoring or absorption**.

### Case 1 (original Cal #100, Friday): Cal retraction-propagation failure
- Cal #98 erroneous "0.05-0.06%" flag → verbal self-correction → not filed as numbered entry → Elie absorbed wrong figure across 8+ Vol 2 references
- Calibration #22 v0.1 Rule 1: forbid verbal-only retractions

### Case 2 (Cal #101, Saturday morning): Grace INV-4890 absorption-introduced error
- Grace absorbed Cal #100 precision (0.004% ✓ correct) but introduced NEW value-field error during description-text writing ("206.7682830 = 9 sig figs match" — wrong sig-fig count)
- v0.1 doesn't cover this: it caught the upstream verbal retraction but not the downstream restatement error during absorption

### Case 3 (Cal #103, Saturday morning ~70 min later): Grace INV-4897 same error class
- Grace re-introduced "matches to N significant figures" assertion in NEW catalog entry without explicit numerical computation
- Same error class repeated within 70 minutes → pattern is structural, not isolated incident

### Case 4 (extends Case 2-3): Elie Vol 3.4 SEMF Cal #102 substantive flag
- Elie chapter authoring at ~2 min/chapter pace introduced 3 formula errors:
  - a_S formula √60·B_d (wrong) instead of (g+1)·B_d (correct per README)
  - a_C value 0.711 (wrong) instead of 0.694 (correct per README)
  - a_V formula "(?)" placeholder (incomplete)
- Same error class: description-text content restated from memory rather than quoted from authoritative source

**Four instances in ~24 hours**: K197/Cal #102 + Cal #103/Grace INV-4897 + Cal #101/Grace INV-4890 + Cal #100/Elie absorption.

## Pattern characterization

The error class is **absorption-or-authoring-introduced numerical/formula error in description text**, distinct from upstream retraction-propagation (v0.1 Case 1). It occurs when:
- An artifact's description text restates numerical content (formulas, values, sig-fig counts) rather than quoting verified source
- Speed of authoring (~2 min/chapter, sustained sub-PCAP) introduces transcription/memory errors
- Detection requires later cold-read step rather than write-time discipline

**Detection mode functioning well**: Cal external-referee discipline catches these reliably at cold-read.
**Propagation prevention failing**: write-time discipline (the v0.1 rules) doesn't catch absorption restatements or chapter-authoring restatements.

## STANDING RULE additions (v0.2 extension)

**Existing v0.1 rules (preserved):**
- Rule 1: Cal Mode 1 self-corrections + numerical flags filed as numbered referee log entries (no verbal-only retractions)
- Rule 2: K-audit pre-stages with numerical content include computational verification or tier-label discipline
- Rule 3: Cross-lane absorption requests reference originating-artifact ID + LATEST artifact version
- Rule 4: Multi-document sweep correction on detection

**NEW v0.2 rules:**

**Rule 3a (absorption text discipline)**: When absorbing a Cal entry or other authoritative source into a downstream artifact (catalog entry, chapter narrative, paper text, position document), **quote exact numerical figures from the referenced entry**. No restatement, no re-derivation, no "= N sig fig match" assertions without explicit numerical computation.

**Rule 3b (sig-fig discipline)**: Catalog descriptions, chapter narratives, and paper text that include "matches to N significant figures" or similar precision-claim language must include:
1. **Explicit numerical comparison** — both BST value and observed value with full available precision
2. **Derived sig-fig count** — computed from the actual numerical comparison, NOT asserted from memory
3. **Tier label** — D-tier / I-tier / S-tier per Calibration #21

Example (correct, per Cal #103 recommendation):
> m_μ/m_e candidate substrate-natural form (24/π²)^6 = 206.7612 vs measured 206.7682830(46) = match to 4 significant figures (0.004% deviation per Cal #100 verification)

Example (wrong — Cal #103 caught this):
> m_μ/m_e (24/π²)^6 → 9 sig figs match measured value [no explicit numerical comparison; sig-fig count asserted, not derived]

**Rule 4a (write-time verification)**: When authoring numerical content at sustained sub-PCAP cadence (≥1 chapter/3 min or ≥1 catalog entry/2 min), include computational verification step **before commit**, either:
- Inline numerical evaluation matching the formula (toy verification)
- Explicit reference to authoritative source (README line / catalog INV / Cal entry) with exact quotation
- Tier label "approximate-only, verify before promotion" if neither (a) nor (b) is feasible

## Methodology stack position

Calibration #22 v0.1 + v0.2 together form the PCAP-cadence numerical discipline:
- **v0.1**: catches upstream retraction-propagation + Keeper-side numerical errors at filing + cross-lane absorption-reference discipline
- **v0.2**: catches absorption-introduced restatement errors + chapter-authoring restatement errors + sig-fig assertion-without-derivation

**Combined operational test**: 4 instances caught in 24 hours by external-referee discipline (Cal #100, #101, #102, #103). Detection mode robust. Write-time discipline needs Rule 3a + 3b + 4a addition.

## Cross-lane impact

**Cal lane**: cold-read absorption-return step now formalized as the catch mechanism. Cal #101/#103 demonstrate this is working. Cal own-cadence implementation: every absorption-return cold-read checks description-text restatements specifically.

**Grace lane**: catalog description text now disciplined. INV-4890 v0.2 + INV-4897 v0.2 cleanups operationalize Rule 3a/3b.

**Elie lane**: chapter narrative authoring at sustained ~2 min/chapter rate must apply Rule 4a — pull exact formulas from README/bst_constants.json/data layer rather than recall. Vol 3.4 SEMF v0.3.1 fix is the operational template.

**Lyra lane**: chapter narrative authoring at sustained ~4 min/chapter rate similarly subject to Rule 4a. Vol 4 12/12 v0.3 narratives delivered Saturday morning ~4 min/chapter — Cal #103 batch confirms no chapter-level errors at Lyra cadence (different lane risk profile than Elie's 2 min/chapter rate).

**Keeper lane**: K-audit pre-stage filing must apply Rule 4a — K142 case Friday morning was the precedent, now generalized.

## Promotion path

**Calibration #22 v0.2 STANDING RULE adopted operationally** (per audit-chain governance default: Cal + Keeper consensus → automatic promotion unless Casey overrides). Casey override available; otherwise Rule 3a/3b/4a apply immediately to all lanes.

**Methodology stack now 18a layers** (Calibration #22 v0.2 as extension of layer 18 = 18a).

## Quaker discipline preserved

All 4 cases preserved honest scope:
- Cal #100 explicitly documented Cal's own retraction-propagation failure
- Cal #101 + Cal #103 honestly caught Grace's absorption restatement errors
- Cal #102 honestly caught Elie's chapter authoring formula errors
- All corrections filed as numbered referee log entries (Rule 1 working)
- All resolution chains documented for cross-lane absorption
- No tier inflation; honest tier-downgrade applied where flagged

## Status

**Calibration #22 v0.2 extension FILED as STANDING RULE.** Operationalized immediately. Pending Casey override.

Cross-lane broadcast to `notes/.running/RUNNING_NOTES.md` flagging Rule 3a + 3b + 4a as STANDING RULES.

— Keeper, Calibration #22 v0.2 extension formalization, Saturday 2026-05-23 ~11:00 EDT
