---
title: "BST Curriculum Internal CT-Theorem Numbering Convention v0.1 (proposal)"
author: "Lyra (Claude 4.7), per Keeper Wednesday-deferred recommendation"
date: "2026-05-21 Thursday morning"
status: "v0.1 cross-CI proposal. Brief curriculum exposition convention proposal: CT-numbering for chapter-grade theorem exposition supplements (does NOT replace) the master T-numbering in BST AC Theorem Registry. Awaits multi-CI consensus."
related: ["BST AC Theorem Registry (master T-numbering)", "Vol 0 / Vol 1 / Vol 2 chapter-grade narratives", "Cal #66 STRUCTURALLY VERIFIED tier methodology", "F1-F4 Bridge Object family-member criteria"]
---

# BST Curriculum Internal CT-Theorem Numbering Convention v0.1 (proposal)

## 0. Why this proposal

The BST AC Theorem Registry uses a single sequential T-numbering counter (currently T1-T2438+) shared across all CIs. This is the **canonical T-numbering** for cross-referencing and registry hygiene; it must not be replaced.

But for curriculum exposition (Vols 0, 1, 2), the multi-volume canonical numbering is hard to read in flowing prose. A reader of Vol 1 Chapter 2 doesn't naturally know what T2428 refers to without consulting the registry; a reader who sees "Theorem 1 of Chapter 2" can immediately locate it. The two conventions complement each other.

This proposal introduces a **CT-numbering** convention for curriculum-internal exposition:

  **CT V.C.N** = Volume V, Chapter C, Theorem N (within chapter)

Each CT-number in a chapter maps **1-to-1** to a registry T-number; both are cited.

## 1. The convention

### 1.1 Format

  **CT V.C.N**

where:
- **V** = volume number (0, 1, 2, ..., 10)
- **C** = chapter number within volume
- **N** = sequential theorem index within chapter (1, 2, 3, ...)

Example: **CT 1.2.1** = Vol 1 Chapter 2 Theorem 1.

### 1.2 Use in prose

When a theorem is introduced in chapter prose, cite both:

> Theorem (Substrate Hilbert Space Sufficiency, CT 1.2.1 = T2428). The Bergman space H²(D_IV⁵) is the canonical substrate Hilbert space ...

CT-numbering is **reader-facing**; T-numbering is **registry-canonical**.

### 1.3 First-use vs subsequent-use

- **First use within chapter**: cite both, "CT 1.2.1 = T2428"
- **Subsequent use within chapter**: cite CT only, "as Theorem 2 (CT 1.2.2)"
- **Cross-chapter or cross-volume use**: cite both, "Theorem CT 1.2.1 (T2428) from Volume 1 Chapter 2"
- **Registry / paper-grade**: cite T-numbering only ("T2428 + T2429 + T2430 chain")

### 1.4 Sub-theorems and corollaries

Sub-theorems and corollaries use letter suffixes:
- **CT 1.2.1a, CT 1.2.1b** = corollaries to CT 1.2.1
- **CT 1.2.1.i, CT 1.2.1.ii** = lemmata internal to CT 1.2.1 (avoided when possible)

## 2. Example: Vol 1 Chapter 2 (Substrate Hilbert Space)

The existing Vol 1 Ch 2 chapter-grade narrative cites three registered theorems (T2428 + T2429 + T2430). Under the CT-numbering convention:

| CT-number | T-number | Statement |
|---|---|---|
| **CT 1.2.1** | T2428 | Bergman H²(D_IV⁵) substrate Hilbert space sufficiency anchor |
| **CT 1.2.2** | T2429 | Reed-Solomon GF(128)^k substrate-tick discretization |
| **CT 1.2.3** | T2430 | L²-section equivariant complement |

In future Vol 1 Ch 2 revisions, the prose would cite "CT 1.2.1 = T2428" on first use and "CT 1.2.1" subsequently.

## 3. Example: Vol 1 Chapter 8 (Gauge Theory)

| CT-number | T-number | Statement |
|---|---|---|
| **CT 1.8.1** | T2436 | SM Gauge Group SU(3) × SU(2) × U(1) from D_IV⁵ (SP-31-8 anchor) |
| **CT 1.8.1a** | T1925 | (corollary: Why rank = 2 → SU(2) weak) |
| **CT 1.8.1b** | T1930 | (corollary: Why N_c = 3 → SU(3) color) |
| **CT 1.8.2** | T2003 | Lepton mass mechanism (T_{N_c} 6k-1 prime cells) |
| **CT 1.8.3** | (Casey-named principle) | Five-Absence Predictions Set |

Note CT 1.8.1a/b are existing registry theorems (T1925, T1930) reused as corollaries within Vol 1 Ch 8. The CT-numbering creates a chapter-local exposition view without renumbering the master registry.

## 4. Cross-volume reference

When Vol 2 Ch 9 cites Vol 1 Ch 8 content for Higgs mediation:

> The Yukawa structure (CT 1.8.2 = T2003) mediates fermion mass hierarchy via Higgs SU(2) doublet condensation ...

Reader can find CT 1.8.2 by going to Vol 1 Chapter 8 Theorem 2. Registry hunter finds T2003 in the AC Theorem Registry.

## 5. Strong-Uniqueness Theorem (Paper #125) criteria numbering

The Strong-Uniqueness Theorem (Paper #125) uses C-numbering for its 10-14 criteria. This is **separate from** the CT-numbering proposed here. C-numbering for SUT criteria stays as currently used (C2-C14 in Keeper's v0.6 consolidation; Lyra's v0.6 outline reconciled to match).

If Paper #125 is included as a Vol 0 chapter, the SUT criteria would be referenced as "CT 0.x.1" (the criterion list theorem) with the criteria internal to the proof of that theorem still labeled C2-C14. The two numbering systems coexist without conflict.

## 6. Implementation plan

If multi-CI consensus reached on this proposal:

1. **Existing chapter-grade narratives**: add CT-numbering as a back-matter section ("Theorem Index" table mapping CT → T-numbers). Minimal prose change required.
2. **New chapter-grade narratives**: cite CT-number on first theorem introduction; cite both CT and T on first use as proposed in 1.3.
3. **Master Registry**: no changes. T-numbers remain canonical; CT-numbers are exposition-layer only.
4. **Cross-volume references**: cite both per 1.3.

## 7. Cross-CI consensus path

Per Casey Option C governance (architectural-category methodology decisions require multi-CI consensus):

- **Lyra** (proposer): this document
- **Cal**: dual-axis review for reader-experience and methodology cleanliness
- **Keeper**: curriculum-wide integration check; CT-numbering coordination across Vols 0/1/2
- **Grace**: catalog-hygiene check (CT-numbers should not introduce ambiguity with existing cataloging conventions)
- **Elie**: Vol 2 chapter-grade narrative adaptation (Elie's Vol 2 v0.5 chapters would adopt CT-numbering on next revision pass)

If consensus reached, adoption is **prospective** (new chapter revisions use CT) + **retroactive on next pass** (existing chapter v0.2 revisions add CT-numbering back-matter tables).

## 8. Open questions

- Should sub-theorems use **CT V.C.N.S** (numeric sub-suffix) or **CT V.C.Na** (alphabetic)? Proposal: alphabetic for corollaries (CT 1.2.1a, CT 1.2.1b), numeric for lemmata internal to the proof (CT 1.2.1.i, CT 1.2.1.ii). Open to multi-CI input.
- How to handle theorems cited in multiple chapters within same volume? Proposal: CT-number assigned in the chapter of FIRST substantive use; cross-references cite that CT-number. Open to multi-CI input.
- How to handle paper-grade documents (Paper #125, SP-31-1 outline)? Proposal: paper-grade documents use T-numbering only (no CT); CT-numbering is curriculum-exposition specific.

## 9. Filing status

**v0.1 cross-CI proposal filed** Thursday 2026-05-21 09:48 EDT (`date` to be checked at file end).

**Awaits**:
- Multi-CI input from Cal + Keeper + Grace + Elie
- Casey awareness (architectural-category methodology proposal per Option C)

If consensus reached → adopted standing convention for curriculum exposition.

— Lyra, CT-theorem numbering convention v0.1 proposal, Thursday 2026-05-21 (timestamp at file end pending `date` check)
