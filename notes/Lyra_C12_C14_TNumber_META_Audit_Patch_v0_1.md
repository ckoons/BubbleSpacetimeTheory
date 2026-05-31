---
title: "C12-C14 T-number / META audit patch v0.1 (P5.2, Cal #156 Flags A+B) — Strong-Uniqueness v1.1 label correction: C13 mis-attributes SCMP to T2468 (SCMP is T2469); Cal #99 META distinction on T2467 (Rigidity-as-Singleton is a META-theorem, not an operational null-model criterion). Corrected attributions filed for Keeper update."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 11:50 EDT"
status: "AUDIT PATCH v0.1 (P5.2, gates external citation of Strong-Uniqueness v1.1). Label-level fixes; substance unchanged."
---

# C12-C14 T-number / META audit patch

## 0. Cal's flags

Cal #156 Flags A+B on Strong-Uniqueness v1.1:
- **Flag A**: C13 currently labeled "SCMP coherence (T2468)" — SCMP is **T2469**, not T2468. T2468 is Rigidity-as-Unification.
- **Flag B**: Cal #99 distinguished T2467 as a **META-theorem** (Rigidity-as-Singleton — about the uniqueness *frame*) from operational criteria (which contribute to null-model factors). C12 currently treats T2467 as an operational criterion; should be marked META-tier separately.

Both flags are correct. Filing the patch.

## 1. Corrected attributions

From CLAUDE.md memory:
- **T2467 = D_IV⁵ Rigidity-as-Singleton (META-theorem per Cal #99)** — about the uniqueness/closure of the substrate framework, not a per-property uniqueness criterion.
- **T2468 = D_IV⁵ Rigidity-as-Unification (operational, multiverse loophole closed)** — operational criterion: D_IV⁵ unifies; no parallel substrates needed.
- **T2469 = SCMP coherence (Bell sub-Tsirelson 1/2^N_c = 1/8 falsifier)** — operational criterion: substrate coherence maintained, with explicit Bell falsifier.

Current v1.1 (incorrect):

| C# | label | T# |
|---|---|---|
| C12 | D_IV⁵ Rigidity | T2467 |
| C13 | SCMP coherence | T2468 ← WRONG |
| C14 | Bell sub-Tsirelson 1/8 | T2469 ← duplicates C13 content |

Corrected v1.2:

| C# | label | T# | tier note |
|---|---|---|---|
| **(META-C12)** | **D_IV⁵ Rigidity-as-Singleton** | T2467 | **META-theorem per Cal #99** — about the uniqueness frame, does NOT contribute to null-model count |
| **C12** | **D_IV⁵ Rigidity-as-Unification** | T2468 | operational; multiverse loophole closed |
| **C13** | **SCMP coherence (Bell 1/2^N_c=1/8 falsifier)** | T2469 | operational; explicit falsifier |
| **C14** | (vacant; reassign or close v1.2 at C13) | — | — |

OR keep numbering by re-anchoring the META separately:

| C# | label | T# |
|---|---|---|
| C12 | D_IV⁵ Rigidity-as-Unification | T2468 |
| C13 | SCMP coherence (Bell 1/8 falsifier) | T2469 |
| **META-flag** | T2467 Rigidity-as-Singleton: META-theorem (Cal #99), NOT a null-model factor |

(Recommend the second form — preserves C-numbering continuity.)

## 2. What changes downstream

- **Null-model count**: T2467 (META) does NOT contribute as an independent (1/3) factor. The independent operational criteria from this cluster are T2468 (C12) and T2469 (C13). One slot is removed from the null-model factor count.
- **External citation**: v1.1 currently cites "13 criteria + 4 candidates"; corrected v1.2 cites "12 operational criteria + 1 META-theorem + N candidates" — accurate per Cal #99.
- **Substance**: unchanged. The MATH of T2467/T2468/T2469 is intact; only the C-numbering and META-vs-operational tier marking are corrected.

## 3. Honest scope + tier

**RIGOROUS** (label / attribution): T2469 = SCMP (CLAUDE.md memory + multiple Friday CI docs); T2467 = Rigidity-as-Singleton META (Cal #99); T2468 = Rigidity-as-Unification operational (Casey-named #7 dispatched Friday afternoon).

**PATCH (this doc)**: re-attribute C13 from T2468 to T2469; flag T2467 as META separately (not in null-model count); update external-citation count accordingly.

**Substance unchanged**: the Strong-Uniqueness theorem stands; only the label-level attributions corrected.

**Cal #27 / honesty**: this is a label patch, not a substantive change. Cal correctly caught a mis-attribution that would have miscounted the null-model factor and confused external readers about which theorem is META vs operational. Routine discipline.

**Routed**: → Keeper: update Strong-Uniqueness v1.1 → v1.2 with the corrected attributions; null-model count adjusts by removing T2467's (1/3) factor (operational count drops by 1, but the META-theorem strengthens the framing). → Cal: confirm corrected attribution matches your #156 + #99; close Flag A+B. → Grace: update master ledger to reflect META-tier on T2467 (separate from operational criteria).

— Lyra, C12-C14 T-number/META audit patch v0.1. Correction: C13 was mis-attributed to T2468 (T2468 = Rigidity-as-Unification operational, not SCMP); SCMP is T2469 (Bell 1/8 falsifier). T2467 is META-theorem per Cal #99 (uniqueness frame, not operational null-model factor). Recommended v1.2 attributions: C12 = T2468 (Rigidity-as-Unification), C13 = T2469 (SCMP), META-flag T2467 separate (not in null-model count). Substance unchanged; routine label patch.
