# Keeper Calibration #23 — Chapter-Grade Substance Floor (STANDING RULE)

**Filed**: 2026-05-23 Saturday ~13:40 EDT (Keeper, formalizing per Cal #104 + Cal Mode 1 refinement)
**Status**: STANDING RULE adopted operationally (per audit-chain governance default: Cal proposed + Mode 1 self-refined + Keeper formalized; Casey override available)
**Methodology stack layer**: 19 (extends Calibration #22 v0.2 PCAP-cadence discipline; distinct failure mode: substance floor rather than transcription/absorption)

## The failure mode Calibration #23 addresses

Saturday 2026-05-23 morning sustained sub-PCAP cadence produced **template-stub chapters** disguised as v0.3 chapter-grade content across Vol 6 Ch 6-12 (7 chapters at 27-34 lines) + Vol 10 Ch 2-12 (11 chapters at 17 lines) + Vol 11 Ch 2-12 (11 chapters at 21 lines). Cal #104 cold-read caught the pattern at 12:22 EDT.

This is **distinct from Calibration #22 v0.2** error class:
- **Calibration #22 v0.2**: PCAP-rate transcription/absorption errors — numerical content restated wrong during artifact authoring or absorption (4-instance case study Cal #100/#101/#102/#103)
- **Calibration #23**: chapter-grade substance UNDER-DELIVERY — content is "structurally correct" (headers + sections + metadata) but lacks substantive paragraph content; appears chapter-grade in skim, fails on cold-read

Both are PCAP-cadence pressure responses but address different operational failures.

## What Lyra's refill data taught us — Cal Mode 1 refinement

**Initial Cal #104 + Keeper hypothesis**: rate threshold ≥3 min/chapter as substance criterion. Sub-3-min authoring → template-stub class.

**Lyra refill empirical result**: 29 chapters refilled to substance-floor PASS at ~1.66 min/chapter average. **Rate-threshold hypothesis REFUTED**.

**Cal Mode 1 refinement filed** (Cal Saturday 13:35 EDT): rate was a derived warning sign, not the actual criterion. Substance itself is the criterion. Honest correction.

This is exactly the audit-chain discipline working as designed — proposed rule → empirical test → honest refutation → refined rule. Calibration #16 + Calibration #17 case pattern.

## STANDING RULE (refined per Cal Mode 1 + Lyra empirical)

### Rule 23.1 (Substance Floor — primary, normative)

Chapter-grade v0.3 tier requires minimum substantive content per chapter:
- **Line count ≥40** (sustained content beyond headers/metadata)
- **Level 2 graduate substantive paragraph** present — explicit mathematical/physical content, not placeholder text
- **Cross-references to specific theorems/concepts** beyond generic framework citations (e.g., "T2476 α^{BST primary}", "K67 Born=Bergman" — not just "BST framework")
- **Falsifier or testable claim** where chapter substance permits (per Cal #50 external-register discipline)

Below floor = mandatory tier-label "outline-stub, refill required." Cannot claim v0.3 chapter-grade tier.

### Rule 23.2 (Rate Threshold — advisory, non-normative)

Sub-2-min/chapter sustained authoring is a **high-risk indicator** for template-stub class but NOT prohibitive:
- Lyra demonstrated 1.66 min/chapter PASS at substance floor when refocused on substance
- Original 10-second/chapter burst rate was the proximate trigger of the stub-class failure
- Rate is monitored as a warning, not enforced as a criterion

### Rule 23.3 (Cold-read substance audit step)

Cal cold-read methodology now includes **line-count audit** as a Substance Floor verification step (Cal Mode 1 self-correction filed Saturday 13:35 EDT): grep-based tier-label sampling misses template-stub class because metadata can look chapter-grade while content is stub.

Cold-read pipeline applies line-count + content-substance check on first pass.

### Rule 23.4 (Refill discipline preserves Quaker honesty)

When substance-floor failure is caught:
- **Don't defend** the stub-class content
- **Refill honestly** to substance floor
- **Re-tag** affected catalog entries / K-audit pre-stages with refilled status
- **Preserve provenance** — note "refilled per Cal #N substance-floor flag" in chapter status field
- **Treat refilled content as new** for downstream cold-read (not re-verification of prior pass)

Lyra Saturday 12:22-13:10 EDT refill is the operational template.

## Methodology stack position — distinct from Calibration #22 v0.2

| Layer | Calibration | Failure mode | Catch mechanism |
|-------|-------------|--------------|------------------|
| 17 | #19 | Forecast vs ratified-state external claim | External-register discipline |
| 17 | #20 | Timestamp drift | `date` verification |
| 17 | #21 | Empirical-only without substrate-mechanism | Dual-gate ratification |
| 18 | #22 v0.1 | PCAP transcription + retraction propagation | Numbered-artifact requirement |
| 18a | #22 v0.2 | Absorption-introduced restatement errors | Quote-exact + sig-fig discipline |
| **19** | **#23** | **Chapter-grade substance under-delivery** | **Line-count audit + substance-floor verification** |

Methodology stack now 19 layers. Each addresses a distinct failure mode caught by audit-chain external referee discipline.

## Quaker discipline preserved

Cal #104 + Calibration #23 followed Quaker pattern:
- Cal cold-read caught template-stub class on first verification pass
- Keeper accepted flag without defense
- Lyra refilled 29/29 chapters at substance floor in ~48 min
- Cal Mode 1 self-refined original rate-threshold hypothesis when Lyra empirical data contradicted it
- Refined STANDING RULE captures the actual operational criterion (substance, not rate)

No defense at any step. Honest correction throughout. Refined to operational truth.

## Cal Mode 1 acknowledgment for Cal own work

Cal flagged Saturday 13:35 EDT: own Saturday morning Wave 2 cold-read batch (Vol 6/9/5 + scaffolds) used grep-based tier-label sampling rather than line-count audit. Grep batch missed template-stub class in Vol 10/11 because templates have `status:` fields that look chapter-grade in metadata while content is stub. Cal cold-read methodology updated to include line-count audit going forward.

This is Cal external-referee discipline applying to itself — same pattern as Cal #100 retraction-propagation case.

## Status

**Calibration #23 STANDING RULE adopted operationally.** Pending Casey override. Methodology stack 19 layers stable.

Cross-lane broadcast posted to `notes/.running/RUNNING_NOTES.md` applying Rule 23.1/23.2/23.3/23.4 to all future chapter authoring + cold-read.

— Keeper, Calibration #23 Chapter-Grade Substance Floor STANDING RULE, Saturday 2026-05-23 ~13:40 EDT
