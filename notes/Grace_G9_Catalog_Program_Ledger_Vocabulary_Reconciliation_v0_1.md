---
title: "G9 — Catalog vs Program Ledger Vocabulary Reconciliation v0.1"
author: "Grace"
date: "2026-05-29 Friday 18:28 EDT (date-verified)"
status: "v0.1 — the catalog-side vocabulary mapping for Keeper's reconciliation. Maps Grace's catalog-INV ledger statuses to Keeper's program-claim ledger statuses, so the two ledgers stay one object."
purpose: "G9 task: prevent vocabulary drift between catalog and program ledgers."
---

# G9 — Catalog ↔ Program Ledger Vocabulary Reconciliation

The catalog ledger (INV-5286, Grace_Master_Derived_vs_Assigned_Ledger_v0_2.md) is the data layer; Keeper's program-claim ledger (K4) is the program-synthesis layer. They must agree.

## Status terms — canonical mapping

| Grace catalog term | Keeper program term | Meaning |
|---|---|---|
| **DERIVED** | **DERIVED** (rigorous) | Forward derivation rigorous as algebra/geometry/rep-theory; referee-grade independent of any open bet |
| **FRAMEWORK-PLUS** | **FRAMEWORK-PLUS** | Mechanism derived rigorously; physical identification rides on the dictionary or another specific bet |
| **TENSION-RELIEVED, NOT CLOSED** | **TENSION-RELIEVED, NOT CLOSED** | A gate moved off "leaning wrong" but explicitly NOT to "closed." Carries a stated burden. |
| **OPEN-WITH-BURDEN** | **OPEN-WITH-BURDEN** | Open gate with a specific, stated burden the would-be closer must satisfy |
| **MATCHED** | **MATCHED** | Multiple routes agree numerically; no route forces the claim |
| **ASSIGNED** | **ASSIGNED** (= dictionary-bet) | Hand-placed; flips DERIVED when the dictionary's relevant flip lands |
| **LEAD** | **LEAD** (= held out of forward claims) | Scheme-dependent or identification-only; specifically excluded from referee-grade content |
| **REFUTED** | **REFUTED** | Caught and corrected this week; recorded as credibility asset (the audit chain working) |
| **PREDICTION** | **PREDICTION** | Falsifiable, with a named test |

## Disposition of the deepest items — both ledgers should read identically

### Generation count + mechanism
- **Count-NUMBER**: DERIVED (h^∨ = N_c = 3, B₂ forced fact) in both ledgers
- **Generation-IDENTIFICATION mechanism**: OPEN-WITH-BURDEN in both ledgers — specific burden: ONE invariant must produce TWO structurally-independent 3-fold structures (3 colors × 3 generations = 9 quark combinations)
- **Framing rule**: use "ONE 3 (h^∨) doing double duty" — supersedes "two independent 3's." E7 candidate is **"two B₂-specific 3s coinciding numerically,"** not "one h^∨ manifesting twice" without explicit mechanism

### c_FK
- **Value 225/π^(9/2) + FK-measure FORCED**: DERIVED in both — derived theorem (Born/Gleason automorphism-invariance; Lebesgue not invariant on bounded symmetric domain)

### Genus convention
- **One genus = n_C = 5**: DERIVED in both (FK multiplicity formula). C_2 = Casimir (not genus); g = embedding (not genus). Rule: intrinsic genus = 5, never 6 or 7.

### Lepton sector (per-particle)
- **18 entries (e/μ/τ × L/R × particle/anti + 3ν_L + 3 anti)**: DERIVED per-particle on every static axis except generation/winding (open per #414). Both ledgers carry this as first per-particle DERIVED row.

### Bulk-color SU(3) mechanism (the program's open frontier)
- Both ledgers: **OPEN** load-bearing gate. SU(3) cannot come from K = SO(5)×SO(2) (clean Lie-algebra fact: B₂ ≠ A₂). Color must come from BULK (non-compact directions of SO(5,2)) or be counting-not-symmetry from h^∨=3.
- Joint with #414's two-structures burden — one mechanism closes both.

### m_p/m_e = 6π⁵ = C_2 · π^(n_C)
- **Numerical equality**: tautology arithmetic (C_2=6, n_C=5 by definition); not a new derivation
- **Structural reading** (adjoint Casimir × Bergman volume = boundary→bulk mass bridge): FRAMEWORK-PLUS, rides on Lyra L4 mass-mechanism story. T187 was already RATIFIED; the dictionary's *reading* is new.

### Tube count (#409)
- **External-blocked**: literature inaccessible in-environment (Keeper/Cal); Elie's first computation failed (wrong affine type, owned honestly)
- **Stakes lowered** post Lyra knot resolution: route I no longer favored; route II carries the count via h^∨. Reopened in-house with the corrected C₂⁽¹⁾ Cartan, but the gate doesn't depend on the outcome.

## Anti-patterns — vocabulary to AVOID

| Avoid | Why | Use instead |
|---|---|---|
| "resolved" (for the generation knot) | implies closed; it isn't | **TENSION-RELIEVED, NOT CLOSED** |
| "two independent routes both giving 3" | over-counts (routes were two representations of one claim) | **"ONE 3 (h^∨) doing double duty"** + the two-structures burden |
| "the cyclotomic fallback carries the count" (if tubes ≠ 3) | category error (positive-root count ≠ δ-category invariant; Lyra #412) | the cyclotomic route is a *separate* mechanism that merely agrees numerically |
| "6π⁵ derives m_p/m_e from substrate" | the numerical equality is tautology arithmetic | "6π⁵ = C_2·π^(n_C) is the dictionary's structural reading of T187" |
| "4 of 66 Casimir-anchored → SM particles = anchored K-types" | coincidence-denominator risk on small targets; routes correlated | "the 4 SM sectors are the canonical SO(5) reps; their Casimirs land on substrate primaries as a *consequence*, not a selection rule" |
| "tubes = generations, forced" | retracted (E1b) | "the tube route is undercut; the count comes from h^∨ via route II" |

## Snapshot tally (Friday EOD)

- **DERIVED**: ~15 program claims + the lepton row per-particle (~18 cells)
- **FRAMEWORK-PLUS**: ~8 (chirality per-particle, charge specifics, mass framework, m_p/m_e reading, E6/E7 physical readings, 4-backbone selection)
- **TENSION-RELIEVED, NOT CLOSED / OPEN-WITH-BURDEN**: 1 (generation mechanism)
- **OPEN (load-bearing)**: 1 (bulk-color SU(3) — joint with the above)
- **MATCHED**: residuals (magic-number forms pending E8)
- **ASSIGNED**: per-particle quark/gauge rows (blocked on bulk-color)
- **LEAD**: ~5 (scheme-dependent quark mass-ratios, Macdonald→mass, gauge clusters)
- **REFUTED this week**: 11 (the credibility column)
- **PREDICTION**: 3 classes (ν=NORMAL, θ_QCD=0, Five-Absence)

## The one-line ledger-sync rule

**Both ledgers should be readable as the same object with different granularities** — Keeper's program-claim ledger as the synthesis, Grace's catalog-INV ledger as the data layer (each INV stamped with the status it deserves). Use the vocabulary above; flag any drift as a sync error to fix immediately.

— Grace, G9 vocabulary reconciliation v0.1, 2026-05-29 18:28 EDT (date-verified)
