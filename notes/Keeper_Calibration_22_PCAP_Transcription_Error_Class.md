# Keeper Calibration #22 — PCAP-Rate Transcription Error Class + Numbered-Artifact Discipline (STANDING RULE proposal)

**Filed**: 2026-05-22 Friday 15:31 EDT (Keeper, `date`-verified actual)
**Status**: STANDING RULE proposal pending Casey approval (audit-chain governance default applies — Cal proposed in Cal #100; Keeper concurs and consolidates)
**Methodology stack layer**: 18th (extends Cal #99 META-theorem discipline + Calibration #19 ratified-state count + Calibration #21 substrate-mechanism gate)

## The error class

Under sustained sub-PCAP cadence (~25/hour to ~5×/baseline acceleration), transcription errors emerge as a systematic risk class. Friday May 22 produced TWO independent instances on the same day, demonstrating the class is not lane-specific:

### Case 1: K142 (Keeper-lane numerical error)

**Incident** (Friday 08:42 EDT filing): K142 PRE-STAGE line 15 wrote "k=6: catalog entries with coefficient 6π⁶ ≈ 1837 (interesting near m_p/m_e numerically)" — but 6π⁶ = 5768.34, NOT 1837. The 1837 value belongs to 6π⁵ at line 8 of the same document (the canonical m_p/m_e identity).

**Detection** (Friday ~14:11 EDT, ~5.5 hours later): Cal Tier 2 K140-K149 batch verification caught the arithmetic error during K-audit cold-read.

**Resolution** (Friday ~14:15 EDT, ~4 minutes after Cal flag): Keeper K142 v0.2 fix posted with full provenance preservation. Tier preserved (STRONG 3.65/4) since the k=6 catalog-extension structural claim is independent of the misattributed numerical comparison.

**Error type**: PCAP-cadence transcription — exponent k=5 vs k=6 conflated under sustained-cadence writing.

### Case 2: Cal #98 → Cal #100 (Cal-lane retraction propagation failure)

**Incident** (Friday morning Cal #98 cold-read): Cal flagged T190 (24/π²)⁶ precision as "0.05-0.06% actual" — but the correct precision is ~0.004%. Cal-side arithmetic error: 24/π² = 2.4317084 (correct) was computed as 2.43197 (incorrect), propagating ~10× precision miss.

**Self-correction failure** (Friday morning, undocumented): Cal verbally self-corrected mid-session but did NOT file a numbered referee log entry. The verbal-only retraction did not propagate.

**Propagation** (Friday afternoon, ~14:11 EDT): Elie absorbed the erroneous "0.05-0.06%" flag across 8+ inline references in Vol 2 Ch 3 + Ch 5 v0.4. Lyra inherited the wrong figure into Vol 1 Ch 11 v0.7 canonical-form selection (joint Lyra+Elie sweep). Grace catalog INV entry reflects the wrong figure.

**Detection** (Friday 15:28 EDT, ~6-7 hours after original error): Cal #100 filed with full arithmetic re-verification — 24/π² = 2.4317084, (2.4317084)^6 = 206.760, deviation from observed 206.7682830 = 4.0×10⁻⁵ = 0.004%. Original Vol 2 Ch 3 v0.3 was correct; Cal #98 flag was wrong; verbal retraction failed; absorption propagated the wrong figure.

**Resolution path** (in progress, Friday afternoon): Vol 2 Ch 3 + Ch 5 v0.4 → v0.5 find/replace sweep; Vol 1 Ch 11 v0.7 → v0.8; Grace catalog correction.

**Error type**: PCAP-cadence retraction-propagation failure — verbal-only self-correction without numbered artifact under sustained sub-PCAP team coordination.

## Systemic risk pattern

Both cases share structural features:
- **Sustained sub-PCAP cadence**: ~25/hour discrete artifact production
- **Cross-lane propagation amplification**: errors flow forward to absorption lanes (Cal → Elie → Lyra → Grace catalog chain)
- **Detection lag ~hours**: external referee discipline catches errors, but only after material propagation has occurred
- **Resolution requires multi-document sweep**: not just the originating artifact

The error class is **bidirectional**: errors can originate in any lane (Keeper Case 1, Cal Case 2). The detection mechanism (external referee discipline) is robust, but the propagation amplification under PCAP cadence multiplies the cleanup cost.

## STANDING RULE proposal (Calibration #22)

**Rule 1 (Cal-side, per Cal #100 proposal)**: ALL Cal Mode 1 self-corrections and numerical flags must be filed as numbered referee log entries (not verbal). Absorption requests must reference the LATEST numbered entry. Verbal-only retractions are forbidden under PCAP cadence — they create propagation risk.

**Rule 2 (Keeper-side, K142 case study)**: K-audit pre-stage documents with numerical content must include explicit cross-checks at filing. Specifically: any "X ≈ Y" form must include either (a) computational verification path or (b) explicit "approximate-only, verify before promotion" tier-label.

**Rule 3 (all-lane, cross-cutting)**: Absorption requests under PCAP cadence must reference originating-artifact ID + LATEST artifact version. Cross-lane handoffs cite specific commits/timestamps. No "per my earlier note" absorptions — explicit numbered references only.

**Rule 4 (Keeper consolidation)**: When PCAP-cadence transcription error is detected, the resolution chain is mandatory:
- Originating artifact v0.X+1 fix with provenance preservation
- Numbered Calibration entry capturing the error class
- Cross-lane propagation audit (which documents absorbed the wrong figure?)
- Multi-document sweep correction with version-bumps across affected artifacts
- Cross-references to all corrected artifacts in the Calibration entry

## Detection-vs-propagation asymmetry

The audit chain functions in two modes:
- **Detection mode**: external referee (Cal) catches errors in any lane within hours. Functioning well — Cal #99/#100 demonstrates this.
- **Propagation mode**: under PCAP cadence, errors propagate forward to absorption lanes faster than detection catches them. Multi-document sweep cost grows linearly with absorption depth.

**Calibration #22 addresses the asymmetry by reducing propagation risk via numbered-artifact discipline.** Detection mode is already robust; propagation mode needs structural improvement.

## Methodology stack position

Calibration #22 extends:
- **Calibration #19 (ratified-state count)**: external register discipline — what counts as RATIFIED in external docs
- **Calibration #20 (timestamp drift)**: time-discipline under sustained cadence — `date` verification rule
- **Calibration #21 (mechanism-vs-empirical)**: ratification requires both empirical + substrate-mechanism closure
- **Calibration #22 (PCAP-transcription)**: numerical/artifact discipline under sustained cadence — numbered-artifact rule

The four PCAP-cadence calibrations form a coherent operational discipline for sub-PCAP team coordination:
- #19: what we claim (ratified vs forecast)
- #20: when we claim it (timestamp accuracy)
- #21: how strongly we claim it (empirical + mechanism)
- #22: how we record claims (numbered artifacts + propagation discipline)

## Quaker discipline preservation

Both K142 and Cal #100 cases preserved honest scope:
- K142 v0.2 fix retains the original PRE-STAGE date + adds correction provenance
- Cal #100 explicitly documents Cal's own retraction-propagation failure rather than burying it
- No tier inflation in either case
- Resolution chains documented for cross-lane absorption

This is the Quaker method functioning under sustained cadence: near misses get scrutiny, not defense; corrections are strength.

## Audit-chain governance

Per Casey's audit-chain governance default (Cal + Keeper consensus → automatic promotion unless Casey overrides): Cal #100 proposed the standing rule; Keeper concurs and consolidates as Calibration #22. Default disposition: STANDING RULE adopted operationally; Casey can override.

**Casey approval explicitly requested for Rule 1** (forbidding verbal-only retractions) since it constrains Cal lane operation under sustained cadence. Rules 2-4 follow operationally from Rule 1 + existing discipline.

## Cross-lane impact assessment

**Cal lane**: Rule 1 increases per-cycle overhead by 30-90 seconds per Mode 1 correction (filing a numbered referee log entry rather than verbal note). Net negative under PCAP cadence pressure; net positive under propagation-risk reduction.

**Keeper lane**: Rule 2 increases K-audit PRE-STAGE filing overhead by 1-2 min per numerical claim (computational verification or tier-label discipline). Net positive under audit-chain integrity preservation.

**Lyra/Elie/Grace lanes**: Rule 3 increases per-absorption overhead by ~30 seconds per request (numbered-artifact reference). Net positive under cross-lane consistency preservation.

**Net assessment**: ~5-10% additional overhead at PCAP cadence in exchange for propagation-risk elimination. Worth it given the K142 + Cal #100 cleanup costs (~30-60 min combined for two cases).

## Status

**Calibration #22 FILED as STANDING RULE proposal.** Default disposition: adopted operationally pending Casey override. Cal #100 + K142 dual-case study constitutes sufficient evidence per Quaker discipline.

Cross-lane broadcast posted to `notes/.running/RUNNING_NOTES.md` flagging:
1. Calibration #22 adopted operationally
2. Vol 2 Ch 3 + Ch 5 v0.4 → v0.5 correction sweep needed (Elie primary)
3. Vol 1 Ch 11 v0.7 → v0.8 correction needed (Lyra primary)
4. Grace catalog INV correction needed for m_μ/m_e precision
5. Future Mode 1 retractions filed as numbered referee log entries (Cal commitment)

— Keeper, Calibration #22 PCAP-Transcription Error Class STANDING RULE, Friday 2026-05-22 15:31 EDT (`date`-verified actual)
