---
title: "Cross-Volume Forward-Reference Table v0.2 — Reciprocal-Symmetry + Anchor-Strength Classification"
author: "Grace (Claude 4.7)"
date: "2026-05-23 Saturday ~16:28 EDT"
status: "v0.2 — extends v0.1 with reciprocal-symmetry check + 4-category chapter classification"
data: "data/cross_volume_forward_reference_table_v0_2.json"
parent: "v0.1 (notes/grace_Cross_Volume_Forward_Reference_Table_v0_1.md)"
---

# Cross-Volume Forward-Reference Table v0.2

## v0.1 → v0.2 extension

v0.1 mapped chapter-level forward-references (186 chapters, 992 unique edges).
v0.2 adds: **reciprocal-symmetry check** + **4-category chapter classification by anchor strength**.

## Reciprocal-symmetry findings

- **Total edges**: 992
- **Reciprocal pairs (A→B AND B→A)**: 108 (216 edges)
- **One-way edges (A→B but not B→A)**: 776
- **Reciprocity rate**: 21.8%

**Interpretation**: most cross-volume relationships are **one-way** (foundation → application flow). Reciprocal pairs are typically cross-domain integrator chapters (Vol N Ch 12 bridges) or peer-volume cross-citations (e.g., Vol 5 QM ↔ Vol 1 QFT).

The 21.8% reciprocity rate is structurally consistent with a hierarchical curriculum where:
- Foundation chapters (Vol 0, Vol 1) are cited downstream but don't cite back
- Application chapters (Vol N Ch 12 bridges) cite many but are rarely cited
- Workhorse chapters (Vol 4 Λ, Vol 2 m_p/m_e) sit in the middle

## 4-Category chapter classification

| Category | Definition | Count | Examples |
|---|---|---|---|
| **HUB** (foundation) | incoming ≥ 10, outgoing ≤ 3 | 3 | Vol 1 Ch 2 (32/1), Vol 1 Ch 5 (56/2), Vol 0 Ch 8 (9/1) |
| **APPLICATION** (synthesis) | outgoing ≥ 10, incoming ≤ 3 | 10 | Vol 12 Ch 12 (0/21), Vol 5 Ch 12 (0/19), Vol 0 Ch 10 (1/16) |
| **WORKHORSE** (cross-domain) | incoming ≥ 8 AND outgoing ≥ 8 | 13 | Vol 4 Ch 4 (30/7), Vol 2 Ch 6 (20/4), Vol 1 Ch 11 (11/16) |
| **LEAF** (peripheral) | incoming ≤ 3, outgoing ≤ 3 | 30 | Vol 8 Ch 1, Vol 13 Ch 11, Vol 11 Ch 6 (mostly Wave 2/3 specialized chapters) |

**Observations**:

1. **Vol 1 Ch 5 (Casimir Algebra) is the most extreme hub**: 56 incoming refs, 2 outgoing (28× ratio). It IS the substrate's Casimir; nothing else has anything to say to it.

2. **Vol 1 Ch 2 (Bergman Hilbert Space) is the second extreme hub**: 32 incoming, 1 outgoing (32× ratio). The Bergman H²(D_IV⁵) IS the substrate's Hilbert space; doesn't cite outward.

3. **Bridge chapters (Vol N Ch 12) are pure applications**: Vol 12 Ch 12 has 0 incoming, 21 outgoing. Synthesis chapters reach out to integrate; nothing reaches them.

4. **Vol 1 Ch 11 (Observables Reference) is the top workhorse**: 11 incoming, 16 outgoing. Cross-volume index; central navigation point.

## Implications for Keeper Phase 3 authorship

### HUBs (3 chapters: Vol 1 Ch 2, Vol 1 Ch 5, Vol 0 Ch 8)
- Highest-stakes for canonical correctness; an error here propagates to 9-56 downstream chapters
- Phase 3 rewriting must preserve section anchors that incoming citations depend on
- Worth Phase 3 priority effort (small chapter count, max leverage)

### APPLICATIONs (10 chapters: mostly Vol N Ch 12 bridges)
- Lowest reverse-impact; rewriting these doesn't cascade
- Phase 3 can revise freely without breaking incoming citations
- Good for stylistic experimentation in the authorship pass

### WORKHORSEs (13 chapters: Vol 4 Ch 4 Λ, Vol 2 Ch 6 m_p/m_e, Vol 1 Ch 11 etc.)
- Cross-domain integrators; balance preserving incoming refs while updating outgoing
- Substantive Phase 3 attention needed (medium leverage, medium stakes)

### LEAFs (30 chapters)
- Peripheral; usable for Phase 3 experimentation
- Honest scope: some may actually be under-cited because they're new (Vol 8 Wave 3 chapters likely fall here)

## Honest scope (v0.2 limitations)

- Classification thresholds (incoming/outgoing cutoffs) are heuristic; tuned to current 186-chapter state
- "One-way edge" doesn't always indicate a missing reciprocal — sometimes one-way is correct (foundation → application asymmetry intended)
- Doesn't yet identify SECTION-level references (only chapter-level); v0.3 next: section-granularity
- Doesn't yet classify reference WEIGHT (single mention vs load-bearing dependency)

## Strategic finding

**The curriculum is structurally hierarchical**, not flat. 21.8% reciprocity rate + 3 HUBs + 10 APPLICATIONs confirms designed-hierarchy:

- Vol 0 + Vol 1 are the FOUNDATION (gravity wells; 9 of top 15 most-cited)
- Vol 2-14 are APPLICATION volumes (cite foundation but synthesize own domains)
- Vol N Ch 12 bridges are SYNTHESIS endpoints (pure outgoing)

This validates Casey's choice to launch Vol 0 + Vol 1 + Vol 2 as the v1.0 declaration triple — they ARE the load-bearing substrate of the curriculum's citation graph.

— Grace, Cross-Volume Forward-Reference Table v0.2, 2026-05-23 ~16:28 EDT
