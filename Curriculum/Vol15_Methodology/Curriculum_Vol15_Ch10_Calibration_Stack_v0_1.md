---
title: "Vol 15 Chapter 10 — The Calibration Stack: 19 Layers of Operational Discipline"
author: "Keeper + Cal (Vol 15 Methodology)"
date: "2026-05-23 Saturday"
status: "v0.1 chapter-grade content draft per Calibration #23 Rule 23.1 substance floor"
volume: "Vol 15 Methodology"
chapter: 10
tier: "structural — methodology chapter; full operational rules catalog"
---

# Vol 15 Chapter 10 — The Calibration Stack: 19 Layers of Operational Discipline

## Level 1 — Essence

**The calibration stack records every methodology lesson learned the hard way — 19 layers as of Saturday 2026-05-23, each addressing a specific failure mode, each empirically derived from a real mistake, each made STANDING RULE after operational testing — it's BST's institutional memory for how to do this work without repeating errors.**

## Level 2 — Graduate technical content

The calibration stack functions as **distilled operational wisdom**. Each Calibration entry is named after the specific incident that produced it, captures the lesson in STANDING RULE form, and stays accessible for future application. Unlike abstract methodology textbooks, the calibration stack is **empirical**: rules are added when a mistake happens, not designed in advance.

**The 19-layer stack as of Saturday 2026-05-23**:

- **#1-#13** — early calibrations (pre-Friday 2026-05-22) addressing register conflations, framing slips, methodology-tier discipline. See `notes/Keeper_Calibration_*.md` files for individual specifications.
- **#14-#17** — Wednesday 2026-05-20 + Thursday 2026-05-21 calibrations including Lyra T2419 within-session self-correction (#14), Keeper K72 framing self-correction per Cal #55 (#16), Elie K66 S22 trace-level vs max-eigenvalue (#17 — sub-Tsirelson 126/16).
- **#18 STRUCTURALLY VERIFIED tier ADOPTED** (Cal #66, Thursday 2026-05-21 08:43 EDT): tenth methodology layer between candidate and RATIFIED in audit-chain governance.
- **#19 — Ratified-State Count vs Forecast Endpoint** (Cal #90, STANDING RULE Friday 2026-05-22): external-facing docs use current ratified-state count (e.g., 11 RIGOROUSLY CLOSED + 7 candidates), NOT forecast endpoint. Caught Keeper position docs + Lyra Paper #128 v0.1 simultaneously — systematic risk pattern under PCAP cadence.
- **#20 — Timestamp Drift** (Friday 2026-05-22): `date` command verification mandatory; CIs drift ~10-15 min projection-forward under sustained work. Solution: always query system clock for explicit timestamps.
- **#21 — Mechanism-vs-Empirical Gate** (Friday 2026-05-22 per Toy 3448 honest FAIL): K-audit ratification requires BOTH empirical PASS AND substrate-mechanism closure. K141 PRE-STAGE empirical 4.0/4 retained; substrate-mechanism gate OPEN multi-week.
- **#22 v0.1 — PCAP-Transcription Error Class** (Friday EOD 2026-05-22): numbered-artifact discipline; verbal-only retractions forbidden; Keeper numerical content verification required. Dual case study K142 (Keeper-lane numerical error) + Cal #100 (Cal-lane retraction-propagation failure).
- **#22 v0.2 — Absorption-Introduced Errors** (Saturday 2026-05-23): Rule 3a (absorption text quotes exact figures), Rule 3b (sig-fig discipline), Rule 4a (write-time verification under sustained cadence). 4-instance case study Cal #100/#101/#102/#103.
- **#23 — Chapter-Grade Substance Floor** (Saturday 2026-05-23 per Cal #104 + Cal Mode 1 refinement): substance floor is the primary criterion (≥40 lines + Level 2 graduate substantive paragraph + cross-refs); rate threshold is advisory warning sign (sub-2-min/chapter high-risk but not prohibitive). Lyra's empirical refill at 1.66 min/chapter PASS substance floor refuted initial rate-threshold framing.

**Three patterns visible in the stack**:

1. **PCAP-cadence cluster (#19+#20+#21+#22+#23)**: the calibrations adopted Friday-Saturday cluster around the failure modes that emerged when the team hit sustained sub-PCAP cadence. The faster the team moves, the more discipline needed. Cluster represents 5 of the 19 layers in 2 days — operational pressure produced operational discipline.

2. **Empirical-before-normative**: Calibration #23's initial framing (rate threshold) was REFUTED by Lyra empirical data and REFINED to substance floor. The audit chain itself debugs its own rules. Cal Mode 1 self-correction is a calibration on calibrations.

3. **Bidirectional risk**: Calibration #22 v0.1 originated from Cal #100 (Cal-side failure) + K142 (Keeper-side failure). The stack assumes no lane is immune to its failure modes. Every CI applies every rule.

**Calibration entry structure** (template per Keeper_Calibration_NN_*.md files):
- **Filed**: timestamp + Keeper signature
- **Status**: STANDING RULE adopted operationally, pending Casey override
- **Methodology stack layer**: nth layer with brief framing
- **The error class**: specific incident + characterization
- **The lesson**: what was learned
- **STANDING RULE**: explicit rule statement
- **Cross-lane impact**: how rule affects each CI lane
- **Cross-references**: connected K-audits + prior calibrations + future implications

**Operational maintenance**: the stack is **append-only**. Calibrations don't get removed; if a rule turns out wrong, it's superseded by a new calibration that supersedes the prior (Calibration #23 superseded the rate-threshold framing within the v0.1 → v0.2 framework). The institutional memory grows.

**Casey's role**: Casey-override authority retained. If a calibration STANDING RULE conflicts with Casey's direction, Casey wins. But by default, audit-chain governance default applies: Cal + Keeper consensus → STANDING RULE without per-rule Casey ratification.

**The calibration stack as research instrument**: when a new CI joins the team, the stack is the most efficient onboarding tool. Read Calibration #1-#23 + the canonical case study per layer + the operational rule statements; the new CI now has the team's accumulated operational wisdom in compressed form. This is Vol 15 Chapter 11's primary onboarding artifact.

## Level 3 — 5th-grader accessibility

The team keeps a numbered list of mistakes they made and how to avoid them next time. There are 19 rules on the list right now. Each rule has a story attached to it — what went wrong, who caught it, how they fixed it. When a new helper joins the team, they read the list to learn from everyone's past mistakes. The list keeps growing because every time the team works really fast, they find a new way to almost-mess-up — and that becomes rule #20 (whenever that one happens).

## Cross-volume bridges

- **Vol 15** Methodology: Ch 5 Audit Chain Governance (calibrations close the K-audit chain) + Ch 7 Quaker Discipline (calibrations as honest-correction artifacts) + Ch 11 How to Continue (calibration stack as onboarding tool)
- **Operational artifacts**: `notes/Keeper_Calibration_*.md` files (Calibration #1-#23+); cross-referenced in every Cal referee log
- **Memory entries**: `feedback_calibration_19_external_discipline.md` + `feedback_calibration_22_pcap_transcription.md` + `feedback_timestamp_discipline.md` (Calibration #20 memory form)

## Falsifier

The calibration stack is falsified if: (a) rules accumulate without operational application (counter: every K-audit applies relevant Calibrations); (b) new failure modes recur despite STANDING RULES (some recurrence has happened — that's how Cal #103 caught Grace INV-4897 same error class as Cal #101; led to Calibration #22 v0.2 refinement; meta-discipline working); (c) Casey override is required so frequently that audit-chain governance default fails (no such pattern observed — Casey override is rare). Falsification path: rule-application audit + failure-mode recurrence statistics + Casey-override frequency tracking.

## Next chapter

Ch 11 — How to Continue the Work — covers post-current-team continuation procedures.

— Vol 15 Ch 10 v0.1 — Keeper + Cal, Saturday 2026-05-23
