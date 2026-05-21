---
title: "BST Cross-Classification Matrix v0.3 — auto-populated from full-tagged catalog (Task #238)"
author: "Grace (Claude 4.7)"
date: "2026-05-21 Thursday midday (~12:17 EDT actual)"
status: "v0.3 — auto-populated 60/256 cells from full-coverage data (zone-tag 100% + integer_set 100%)"
purpose: "Cross-classification matrix v0.3 leveraging Thursday midday integer_set 100% + zone-tag 100% coverage milestones to auto-populate cells substantively rather than v0.2 hand-curated ~50 cells"
related:
  - "Task #238 v0.2 hand-populated (Wed Phase 3 prep)"
  - "Toy 3246 AC graph zone-tag 100% (zone-axis feed)"
  - "Toy 3247+3248+3249 catalog integer_set 100% (BST-axis feed)"
  - "Toy 3250 v0.3 auto-population implementation"
  - "Casey afternoon visions Wed PM: Integer Web + 2-Face + 4-Zone + 3-Scale Cognition"
  - "Strong-Uniqueness Theorem v0.9.1 (substrate-comprehensive backbone reference)"
supersedes: "v0.2 (notes/BST_BC_Cross_Classification_Matrix_v0_2.md, Wed PM)"
---

# BST Cross-Classification Matrix v0.3

## What changed since v0.2

v0.2 was hand-populated (~50 cells, Wed Phase 3 prep). v0.3 leverages Thursday midday catalog hygiene milestones to auto-populate from full-coverage data:

| Metric | v0.2 | v0.3 |
|---|---:|---:|
| Cells populated | ~50 (hand) | **60 (auto)** from full-tagged catalog |
| Fully-classified entries (P+B+Z) | (n/a) | **524** of 4705 (11.1%) |
| Axis saturation | partial | **P: 8/8 + B: 8/8 + Z: 3/4** |
| Method | hand-curated | algorithmic from catalog integer_set + AC graph zone-tag |

## Auto-population top 15 cells

| Cell (P, B, Z) | Count | Interpretation |
|---|---:|---|
| (P1, B2, Z4) | 98 | mass × N_c × emission — QCD particle masses |
| (P1, B4, Z4) | 65 | mass × C_2 × emission — Casimir-weighted masses |
| (P1, B1, Z4) | 53 | mass × rank × emission — rank-2 mass observables |
| (P4, B2, Z4) | 24 | coupling × N_c × emission — strong-sector coupling |
| (P4, B4, Z4) | 22 | coupling × C_2 × emission — Casimir-derived coupling |
| (P2, B2, Z4) | 19 | length × N_c × emission — three-color length scales |
| (P2, B1, Z4) | 19 | length × rank × emission — rank-anchored lengths |
| (P4, B1, Z4) | 15 | coupling × rank × emission |
| (P6, B1, Z4) | 15 | geometric × rank × emission — Chern/Hodge invariants |
| (P5, B2, Z4) | 14 | spin × N_c × emission — quark spins |
| (P2, B4, Z4) | 14 | length × C_2 × emission |
| (P3, B2, Z4) | 13 | time × N_c × emission — decay rates |
| (P5, B1, Z4) | 13 | spin × rank × emission |
| (P1, B8, Z4) | 12 | mass × transcendental × emission (π appearances in masses) |
| (P4, B6, Z4) | 10 | coupling × N_max × emission — fine-structure couplings |

## Distribution observations

- **Z4 emission dominance**: 1983 entries Z4-tagged in catalog vs 418 Z3 vs 0 Z1 vs (Z2 ~missing). Catalog tracks emitted observables, not absorbed inputs.
- **B2 N_c + B1 rank + B4 C_2 dominance**: Strong-sector triplet covers most populated cells.
- **B8 substrate-external transcendental** populated at level of B5 (g) and B6 (N_max) — π appears explicitly in many observables.
- **P1 mass + P4 coupling** combined account for ~50% of populated cell volume.

## Empty-cell observations (substrate engineering targets)

196 of 256 cells empty. Subset of structurally-interesting empty cells:
- **Z1 absorb × any** (32 cells): no catalog observable corresponds to absorption — substrate-input experiments
- **P7 information × any × Z2** (8 cells): substrate computation as information-theoretic observable
- **P8 cognition × any × any** (32 cells): cognition-substrate observables not yet identified
- **B7 Bridge × P3 time × Z2** (1 cell): Bridge-object time-scale at commit phase

These empty cells are honest substrate-engineering hunting targets per SP-30.

## Honest residual / next-step refinement

- **524 fully-classified** out of 4705 catalog entries = 11.1% — most entries have B (integer_set 100%) and Z (via domain mapping), but lack explicit P (physical type) keyword.
- v0.4 refinement: per-entry physical-type assignment via deeper name+expression+notes parsing.
- v0.5 refinement: integrate AC graph theorem-level classification (theorems span Z1 absorb + Z2 commit which catalog rarely covers).

## Year 1 Curriculum cross-reference

This matrix v0.3 supports curriculum navigation:
- **Vol 0 Substrate Foundation**: focus on B1-B6 × Z1-Z2 (substrate inputs + commits)
- **Vol 1 QFT**: focus on B1-B7 × Z2-Z3 (commit + coherence with Bridge Objects)
- **Vol 2 Particle Physics**: focus on B1-B6 × Z4 (emission observables) — dominant in catalog
- **Vol 3-10**: variable; each volume has dominant cells

## Cross-Lane References

- **Substrate-Comprehensive Backbone Reference v0.2**: 406 legitimate substrate-comprehensive entries provide top-tier curriculum backbone
- **Strong-Uniqueness Theorem v0.9.1**: matrix v0.3 implicitly supports C11 multi-family Bridge Object verification (B7 column) + C12 operator zoo (P-axis spans)
- **K-audit chain K1-K97**: each audit ratifies a specific (P, B, Z) cell or set of cells

## Standing for direction

v0.3 is auto-population first-pass. Multi-week refinement:
- Per-entry physical-type assignment (push 11% → 60%+ fully-classified)
- AC graph theorem-level integration (Z1 + Z2 coverage)
- Empty-cell per-experiment substrate engineering target identification

— Grace, Cross-Classification Matrix v0.3 auto-populated from Thursday midday integer_set + zone-tag 100% milestones, 2026-05-21 ~12:17 EDT (actual)

---

## v0.4 update (12:18 EDT) — physical_type catalog tagging adds substantial cell coverage

Toy 3251 added physical_type field to 3883/4705 entries (82.5%) via extended keyword set + domain-implied defaults. Matrix v0.4 re-population:

| Metric | v0.3 | v0.4 |
|---|---:|---:|
| Catalog physical_type tagged | 11.1% (524) | **82.5% (3883)** |
| Matrix fully-classified entries | 524 (11.1%) | **2148 (45.7%)** |
| Cells populated | 60/256 (23.4%) | **84/256 (32.8%)** |

**v0.4 top 5 cells**:
1. (P6, B1, Z4) geometric × rank × emission = **317** ← new dominant cell (was 15 in v0.3)
2. (P1, B2, Z4) mass × N_c × emission = 184
3. (P1, B4, Z4) mass × C_2 × emission = 173
4. (P2, B1, Z4) length × rank × emission = 155
5. (P6, B4, Z3) geometric × C_2 × coherence = 145

**Structural observation**: P6 geometric dominance reflects BST's character — most catalog entries are geometric/topological/algebraic invariants of D_IV⁵. The (P6, B1, Z4) = 317 cell is the **matrix structural backbone**.

**Z3 coherence emerges with P6 geometric**: (P6, B1, Z3) = 118 + (P6, B4, Z3) = 145 + (P6, B2, Z3) = 64 — coherence-phase observables are dominantly geometric/topological (theorem-level number-theoretic harmonics).

**v0.4 → v0.5 next step** (multi-week): improve P-type assignment for the 822 still-untagged entries (mostly empty-domain catch-all) via per-entry name parsing. Also: integrate AC graph theorem-level Z1/Z2 entries to populate the absorbed-zone column.

— Grace, v0.4 update post Toy 3251 physical_type extension, 2026-05-21 12:18 EDT (actual)
