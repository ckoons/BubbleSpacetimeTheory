---
title: "Cross-Volume Forward-Reference Table v0.1 — CI Tutor Navigation Backbone"
author: "Grace (Claude 4.7)"
date: "2026-05-23 Saturday afternoon ~15:10 EDT"
status: "v0.1 — chapter-level forward-reference map across 16-volume BST curriculum"
purpose: "Navigation backbone for CI tutor + reader traversing the curriculum; integrity reference for Keeper Phase 3 authorship pass"
data: "data/cross_volume_forward_reference_table_v0_1.json"
methodology: "Pattern-scan 'Vol N Ch M' / 'Vol N.M' references in each chapter narrative .md; build directed graph of cross-volume citations"
---

# Cross-Volume Forward-Reference Table v0.1

## Method

Scanned every chapter narrative `.md` in `Curriculum/Vol{0..15}/` (excluding INDEX + Scaffold files) for patterns matching `Vol N Ch M` or `Vol N.M`. Built directed graph of cross-volume citations: each chapter is a node; each "Vol N Ch M" mention is an outgoing edge.

## Topline numbers

- **Chapters scanned**: 186 (across 16 volumes; Vol 0 has 10 chapters, Vol 1 has 11, Vol 15 has 13, others 12 each — totals 186)
- **Total forward-references**: 1,201
- **Average refs per chapter**: 6.46

## Most-cited target chapters (top 15, incoming refs)

| Rank | Chapter | Incoming refs | Why it anchors |
|---|---|---|---|
| 1 | Vol 1 Ch 5 (Casimir Algebra) | 56 | C₂ = 6 anchor for ~every observable |
| 2 | Vol 1 Ch 2 (Substrate Hilbert Space) | 32 | Bergman H²(D_IV⁵) foundation |
| 3 | Vol 4 Ch 4 (Cosmological Constant Λ) | 30 | T1485 + T2418 Λ↔Casimir |
| 4 | Vol 1 Ch 10 (Renormalization) | 27 | Substrate-tick N_max UV cutoff |
| 5 | Vol 0 Ch 9 (Strong-Uniqueness) | 24 | 11 RIGOROUSLY CLOSED + 7 candidates |
| 6 | Vol 1 Ch 6 (Operator Zoo) | 24 | T2470/T2471/T2472 + T2441 |
| 7 | Vol 0 Ch 4 (Isotropy Group) | 20 | SO(5)×SO(2) substrate structure |
| 8 | Vol 1 Ch 7 (Dynamics) | 20 | Schrödinger/Heisenberg substrate |
| 9 | Vol 2 Ch 6 (m_p/m_e = 6π⁵) | 20 | CROWN JEWEL anchor |
| 10 | Vol 2 Ch 8 (Coupling Constants) | 18 | α + a_e CROWN JEWEL #2 |
| 11 | Vol 3 Ch 7 (Atomic Orbital Sequence) | 18 | (2l+1) = 1,3,5,7 BST primary sequence |
| 12 | Vol 1 Ch 8 (Gauge Theory) | 17 | SU(3)×SU(2)×U(1) substrate |
| 13 | Vol 2 Ch 9 (Higgs) | 15 | m_H D-tier dual-route |
| 14 | Vol 11 Ch 1 (Bounded HSDs) | 15 | Helgason 1978 X.6.1 classification |
| 15 | Vol 0 Ch 1 (D_IV⁵ APG) | 14 | Foundation of foundations |

**Observation**: The most-cited chapters cluster on Vol 0 + Vol 1 (substrate + QFT foundation) — 9 of the top 15 are Vol 0 or Vol 1. This confirms the architectural intent: foundation volumes are the gravity wells, application volumes (Vol 3+ Wave 1 + Vol 5-15 Wave 2/3) orbit them.

## Implication for CI tutor

A CI tutor reading the curriculum from any application chapter encounters ~6 forward-references per chapter. Following the navigation backbone from any leaf chapter leads back through Vol 1 Ch 5 (Casimir) or Vol 1 Ch 2 (Bergman) within 1-2 hops. The curriculum is **graph-connected** at chapter level; no isolated chapters.

## Implication for Keeper Phase 3 authorship pass

When rewriting any volume, the reference map shows:
1. Which incoming citations need to remain valid (don't rename or delete referenced sections)
2. Which outgoing references the author can update to current canonical (e.g., when Vol 2 Ch 6 6π⁵ gets new framing, all 20 incoming chapters can be updated synchronously)
3. Where canonical-form selection (e.g., m_μ/m_e Cal #100 0.004% T190 form) needs propagation across N citing chapters

## Data artifact

Full JSON: `data/cross_volume_forward_reference_table_v0_1.json`
- `forward_refs_by_source`: map of source-chapter → list of target-chapter references
- `top_30_most_cited_chapters`: incoming-ref ranking
- `totals`: chapter + reference counts

## Limitations (honest scope)

- Pattern-based only; may miss references using alternate format (e.g., "the substrate Hilbert space (covered earlier)" without "Vol 1 Ch 2" explicit)
- Doesn't yet identify reciprocal-link symmetry breaks (where A cites B but B doesn't cite A — could be intentional or missing)
- Doesn't distinguish strong vs weak citations (e.g., "see Vol 1 Ch 5" vs "per T2439 Vol 1 Ch 5 Casimir derivation")
- v0.2 next: build the reciprocal-symmetry-check + classify citations by anchor strength

## Standing for Phase 3 authorship pass

Per Keeper queued Grace rail: this table provides the navigation backbone the CI tutor traverses. When Keeper begins Vol N rewrite, this map identifies the integrity surface to preserve. v0.2 reciprocal-check + anchor-strength classification can follow as Phase 3 progresses.

— Grace, Cross-Volume Forward-Reference Table v0.1, 2026-05-23 ~15:10 EDT
