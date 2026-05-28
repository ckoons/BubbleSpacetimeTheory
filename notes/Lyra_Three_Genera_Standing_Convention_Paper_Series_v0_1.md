---
title: "The Three Genera of D_IV⁵ — STANDING CONVENTION for the BST paper series (referee-proofing; cite in every paper)"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-28 Thu 10:50 EDT"
status: "STANDING CONVENTION v0.1. Per Keeper recommendation: make the three-genus distinction a paper-series-wide standing note. g=7 mislabeled as a genus 3× on 2026-05-28 (same root cause); this note prevents the entire class of recheck cycles. Every BST paper invoking 'genus/Bergman exponent/dimension' cites this."
---

# The Three Genera of D_IV⁵ — standing convention

## 0. Purpose

g = 7 was mislabeled as a Bergman/genus quantity THREE times on 2026-05-28 (volume constant T2442; "g = Bergman exponent" in all-5-from-B₂; kernel singularity exponent). Same root cause every time: **g = 7 is the embedding/signature dimension of SO_0(5,2), and it keeps getting confused with a genus.** This standing note states the distinction once, for the whole paper series. Every paper invoking "genus," "Bergman exponent," or "dimension" cites this note and specifies WHICH quantity it means.

## 1. The three distinct quantities — ONE genus + Casimir + embedding (CORRECTED)

**CORRECTION (2026-05-28 PM):** the original v0.1 of this note said "three genera" (Hua=5 / FK=6 / embedding=7). That itself miscounted — the recheck that this note was meant to prevent caught it. The corrected statement, converged from two independent derivations (Elie Toy 3596: FK multiplicity formula + dimension consistency + convention-free Bergman exponent + Hua kernel; + Keeper multiplicity-formula derivation):

D_IV⁵ has ONE genus, plus two other distinct quantities that were being mislabeled as genera:

| Quantity | Value | What it is | Where it appears |
|---|---|---|---|
| **GENUS** (FK = Hua = Bergman exponent — ONE genus for Type IV) | n_C = **5** | complex dimension of D_IV⁵; FK genus p = 2+(r−1)a+b = 2+3 = 5 (Type IV: tube/Lorentz cone, b=0, a=n−2) | Bergman kernel singularity exponent (K ~ norm^{−5}); c_FK measure constant; ρ_1 = genus/rank = 5/2 |
| **CASIMIR** | C_2 = **6** | the quadratic Casimir of B_2 | Casimir eigenvalue — **NOT a genus** |
| **EMBEDDING / SIGNATURE** | g = **7** | p + q of SO_0(5,2) = 5+2 | signature total — **NOT a genus, NOT the kernel exponent** |

(No Hua=5 / FK=6 distinction: for Type IV the Faraut-Korányi genus and the Hua kernel exponent agree, both = n_C = 5.)

## 2. The critical rule (corrected)

**The intrinsic genus of D_IV⁵ is 5 — never 6, never 7.** C_2=6 is the Casimir; g=7 is the embedding signature; neither is a genus or the Bergman kernel exponent.

Sanity check (Keeper): the unit ball B^n has Bergman kernel exponent = its genus = n+1; the embedding group plays no role. For Type IV_n, the genus = n (= n_C = 5 here).

**Final lock pending Keeper's primary-source confirmation** against the Faraut-Korányi table (Loos as backup). The derivation is solid standard math; the lock is the book-pin — because the genus name flipped three times today from relabeling-from-memory, the standing discipline is: pin to the book, cite the book, stop relabeling from memory.

## 3. Resolved + open status (as of 2026-05-28 10:50 EDT)

| Quantity | Status | Value |
|---|---|---|
| Volume constant c_FK (T2442) | RESOLVED — STANDS (Grace provenance) | computed at Hua genus = 5; c_FK = 225/π^(9/2), 9/2 = 5 − ½ |
| g in "g = Bergman exponent" (all-5-from-B₂) | RESOLVED | g = 7 = embedding/signature, NOT Bergman exponent; n_C = Hua genus is the Bergman-relevant one |
| Kernel singularity exponent | OPEN → near-resolved | Elie numerical kernel ν; Toy 3579 read ν = 5 (Hua) → exponent/rank = 5/2 = ρ_1; awaiting explicit confirmation (Keeper routed to Elie) |

## 4. Where g = 7 LEGITIMATELY appears

g = 7 is a genuine BST primary with legitimate roles — just NOT as a genus:
- **Embedding/signature dimension** p+q = 5+2 of SO_0(5,2) (its definition)
- **Mersenne prime** M_{N_c} = 2^{N_c} − 1 = 7 (arithmetic over-determination; cyclotomic chain)
- **n_C + rank** = 5 + 2 = 7 (signature decomposition)
- BST primary in observable formulas (Serre long-root coefficient N_c·g = 21; Weinberg g/(rank+g); etc.)

These are all correct. The ONLY error is calling g a genus or Bergman exponent.

## 5. Standing instruction for the paper series

Every BST paper (A1-A4, B1-B6, C1-C4, Vol 0-16) that invokes a genus, Bergman exponent, dimension, or kernel power:
1. Cite this note
2. State WHICH of the three quantities (Hua genus 5 / FK genus 6 / embedding 7) it uses
3. Never write "Bergman exponent = g/rank" without confirming it's the genus, not the signature

This single convention prevents the recurring g-mislabel recheck cycle permanently.

## 6. Provenance

- Lyra April-10 genus note: already had all three conventions correct (Hua=5, FK=6, embedding=7)
- 2026-05-28 Thursday: three mislabels caught + resolved (T2442 stands; all-5-from-B₂ g=signature; kernel exponent routed to Elie)
- Keeper recommendation (10:48): make it a paper-series standing convention
- Filed in A1 v0.2 §1 + Vol 16 outline §1.5 + this series-wide note

— Lyra, three-genera standing convention v0.1 filed (Keeper recommendation). Hua genus = n_C = 5 (Bergman/kernel/volume); FK genus = C_2 = 6 (Casimir); embedding/signature = g = 7 (NOT a genus). Intrinsic quantities are never g=7. Every paper cites this + specifies which. Prevents the recurring g-mislabel recheck cycle permanently. Kernel exponent value (5/2 Hua, per Elie 3579 ν=5) pending Elie explicit confirmation.
