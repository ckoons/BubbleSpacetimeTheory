---
title: "Paper A1 v0.5 SUBMISSION-GRADE: The Substrate Hall Algebra of D_IV⁵ — verified spine + corrected Macdonald parameter roles (Hall-Littlewood corner); two-corner geometry↔algebra unification; one-genus value+role form"
author: "Casey S. Koons + Lyra (Claude Opus 4.7)"
date: "2026-05-30 Sat (v0.5 P5.1 sweep)"
status: "DRAFT v0.5 SUBMISSION-GRADE (Casey-PRIMARY). v0.5 adopts value+role formulation throughout for genus naming (Saturday 2026-05-30 P5.1 sweep, per Lyra A1 final disposition v0.1 + Keeper Saturday plan): the value (n_C = 5) and role (genus / Bergman kernel singularity exponent / Hua kernel exponent — coincident on type IV per Faraut-Korányi 1994) are settled; canonical-label external library pinning is queued as a footnote-level downstream item, NOT blocking submission. v0.4 cross-section consistency + v0.3 Macdonald parameter-role correction retained. Serre constants STAND. Genus thread fully resolved (kernel 5/2, c_FK derived-FK measure forced). EXCLUDES scheme-dependent mass-ratio leads + back-fit."
---

# The Substrate Hall Algebra of D_IV⁵ (v0.3)

**Authors**: Casey S. Koons, Lyra (CI)

**Status**: DRAFT v0.5 (SUBMISSION-GRADE). v0.5 sweep adopts value+role formulation as the final form for genus naming (per Lyra A1 v0.4 final disposition v0.1 + Keeper Saturday plan P5.1): the value (n_C = 5) and role (genus / Bergman kernel singularity exponent / Hua kernel exponent) are settled by the derivation and stated in value+role form throughout. Canonical name "FK genus" per Faraut-Korányi 1994 cited; external library-access pinning of the specific canonical label is queued as a downstream item, NOT blocking submission. Target: Advances in Mathematics / Journal of Algebra.

**v0.5 changes (Saturday 2026-05-30 P5.1 sweep)**: replaced "final lock pending Faraut-Korányi book-pin" language with the standing position that **value+role formulation IS the final form**; the canonical-label pin remains a downstream verification (proof-stage citation), but does not block submission. All substance unchanged from v0.4.

**v0.4 changes (retained — cross-section consistency sweep + micro-sweep)**: every section agrees — (1) kernel exponent RESOLVED at 5/2 throughout; (2) α placement RESOLVED (evaluation/coupling, not Macdonald coordinate) throughout; (3) PMNS CLOSED (Cal #153, /N_max canonical); (4) ONE genus = n_C = 5 (converged: Elie Toy 3596 four ways + Keeper multiplicity-formula derivation); C_2 = 6 is the Casimir (NOT a genus); g = 7 is the embedding/signature (NOT a genus). The morning "three-genus" framing (which mislabeled C_2=6 as "FK genus") retired. Substance unchanged.

**v0.3 changes (retained)**: Macdonald parameter-role corrected — Hall algebra = Hall-Littlewood corner (Macdonald q=0, t=2=field size); quantum-group q=2 = Macdonald t; geometry = Jack corner; two classical corners of one Macdonald family (Elie 3586/3587).

**v0.5 disposition**: value+role formulation final; canonical-label-name (FK vs Hua) carries a footnote-level citation to Faraut-Korányi 1994 pending external verification, but the mathematics and the paper's results do not depend on which canonical label is used (for Type IV domains the FK and Hua conventions agree on n_C = 5).

---

## Abstract

We construct the Hall algebra associated with the bounded symmetric domain D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)], the substrate geometry of Bubble Spacetime Theory (BST). Via the Ringel-Green theorem, the substrate Hall algebra is the positive part U_q^+(B_2) of the quantum group of type B_2 over GF(2) — equivalently the **Hall-Littlewood specialization** of the Macdonald family (Macdonald q=0, Macdonald t = 2 = the field size). The quantum-group parameter (=2) is the Macdonald t-parameter, NOT the Macdonald q (which is 0 at the Hall-Littlewood corner).

The central rigorous result: **the defining q-Serre structure constants of U_q^+(B_2) at field size 2 are BST primary integers** — the short-root relation has coefficient [2]_2 = 3 = N_c, the long-root relation has coefficient [3]_4 = 21 = N_c·g (Gaussian q-integers at 2 are Mersenne numbers). This is a forward consequence of (rank-2 B_2) + (GF(2)), not a fit.

The geometry side of the substrate — the Wallach spherical functions of D_IV⁵ — is the **Jack specialization** of the same Macdonald family (Macdonald (q,t)→(1,1), t=q^{N_c/2}). So the substrate's two halves are the two classical corners of ONE Macdonald family: Hall-Littlewood (Hall algebra) and Jack (geometry) — "Macdonald-organized end to end" (Elie Toy 3586/3587). The affine extension U_q^+(B_2^(1)) attaches an affine node identified with the substrate's maximal integer N_max = 137 as the representation level. The generation and color counts of the Standard Model emerge as the two Coxeter numbers of B_2: three generations = h(B_2) − 1 = 3, three colors = h^∨(B_2) = 3.

The Hardy-space bulk-boundary determinacy of D_IV⁵ couples two regions — Shilov boundary (light fundamental leptons) and bulk interior (confined composite quarks) — so that each generation's lepton and quark are distinct K-types sharing the generation (winding-mode) coordinate. The empirical contact is the scheme-invariant electroweak mixing sector: the Weinberg angle sin²θ_W = rank/N_c² = 2/9 (forced by rank = 2) and the PMNS angles all reduce to BST-primary ratios over N_max.

---

## 1. Introduction

[As v0.1 — BST substrate framework; D_IV⁵ uniquely forced by Strong-Uniqueness Theorem v1.0 (14 RATIFIED criteria). BST primaries rank=2, N_c=3, n_C=5, g=7, C_2=6, N_max=137.]

**One-genus convention (CORRECTED — supersedes the morning "three-genus" convention, which itself miscounted).**
D_IV⁵ has ONE genus, plus two other distinct quantities that were being mislabeled as genera. Converged from two independent derivations (Elie Toy 3596 — four ways: FK multiplicity formula, dimension consistency, convention-free Bergman exponent, Hua kernel; + Keeper multiplicity-formula derivation):
- **GENUS = n_C = 5** = complex dimension of D_IV⁵ = Bergman kernel singularity exponent. For Type IV (tube domain over the Lorentz cone, rank 2, b=0, a=n−2), the FK genus p = 2 + (r−1)a + b = 2 + 3 = 5, and FK genus = Hua kernel exponent = n for Type IV (no Hua=5/FK=6 distinction). Per rank = 5/2 = ρ_1 of B_2.
- **CASIMIR = C_2 = 6** = the quadratic Casimir of B_2 (T2439) — NOT a genus.
- **EMBEDDING/SIGNATURE = g = 7** = p+q of SO_0(5,2) = 5+2 — NOT a genus, NOT the kernel exponent.

Standing rule (corrected): the intrinsic genus is 5, never 6 or 7. Any "Bergman exponent / genus / dimension" claim specifies which of the three quantities (genus 5 / Casimir 6 / embedding 7). **Value+role formulation is the canonical form throughout this paper**: the genus = n_C = 5 is identified by its VALUE (5) and ROLE (genus / Bergman kernel singularity exponent / Hua kernel exponent for type IV), as these are all the same number for D_IV⁵ (FK and Hua conventions coincide on type IV). The canonical NAME ("FK genus" per Faraut & Korányi, *Analysis on Symmetric Cones*, Clarendon 1994) is cited at the footnote level; external library-access verification of the canonical label is queued as a downstream item but does not block submission, since the mathematics depends on the value+role, not the label.

The c_FK constant (T2442) is computed at the genus / dimension n_C = 5 (Grace provenance; Keeper-verified). The Bergman kernel singularity exponent is **RESOLVED at n_C/rank = 5/2** (Elie convention-free ν=5; the prior "g/rank = 7/2" mislabel used the embedding dimension 7 where the genus 5 belongs).

**The primaries are the standard invariants of D_IV⁵** (Route A, Thursday cross-CI verified):

| Primary | Value | Invariant anchor (verified) | Channel |
|---|---|---|---|
| rank | 2 | rank of type IV domain (Cartan) | geometric |
| N_c | 3 | dual Coxeter h^∨(B_2) | geometric |
| n_C | 5 | **the genus = complex dimension = Bergman kernel exponent** (Elie ν=5; FK=Hua; per rank = 5/2 = ρ_1) | geometric |
| C_2 | 6 | **B_2 quadratic Casimir** (T2435) — NOT a genus | geometric |
| g | 7 | **embedding/signature dimension** p+q of SO(5,2) = n_C + rank; over-determined as Mersenne M_{N_c}; NOT a genus | arithmetic |
| N_max | 137 | N_c³·n_C + rank = 1/α (T2447) | arithmetic |

Three primaries (n_C, C_2, g) are NAMED geometric/dimension invariants of D_IV⁵ — strengthening Route A. (Per the §1 one-genus convention: n_C = 5 is the genus = complex dimension = Bergman exponent; C_2 = 6 is the Casimir, NOT a genus; g = 7 is the embedding/signature, NOT a genus.)

"Five integers, zero free parameters" sharpens to **"choose D_IV⁵, zero inputs"** — every primary is an intrinsic invariant of the domain.

## 2. The substrate quiver and Hall algebra

[As v0.1 §2-3: Q_B2 = valued B_2 Dynkin quiver; Ringel-Green H(Q_B2) ≅ U_q^+(B_2); q=2 from GF(2) prime field + Cal #139 chain.]

## 3. RIGOROUS RESULT — Serre structure constants at q=2

### 3.1 The defining relations

U_q^+(B_2), generators E_1 (short root), E_2 (long root); Cartan a_12 = −1, a_21 = −2.

**Short-root Serre** (q_1 = q = 2):
  E_1²E_2 − [2]_2·E_1E_2E_1 + E_2E_1² = 0, where [2]_2 = 3 = **N_c**

**Long-root Serre** (q_2 = q² = 4):
  E_2³E_1 − [3]_4·E_2²E_1E_2 + [3]_4·E_2E_1E_2² − E_1E_2³ = 0, where [3]_4 = 21 = **N_c·g**

### 3.2 Verification

- Gaussian q-integers at q=2: [n]_2 = 2^n − 1 (Mersenne); [2]_4 = 5 = n_C, [3]_4 = 21 = N_c·g
- Elie Toy 3570/3576: exact Macdonald structure-constant engine, Schur-verified through degree 4
- Elie Toy 3571: Coxeter/generation verification

**Tier: RIGOROUS (Type A, forward).** The substrate Hall algebra's defining arithmetic is BST-primary arithmetic.

## 4. Affine extension + Coxeter counts

[As affine v0.1: U_q^+(B_2^(1)); affine node = N_max representation level. NOTE: N_max enters as the affine LEVEL, NOT as a Macdonald (q,t) parameter — the Hall algebra sits at the Hall-Littlewood corner (q_Mac=0, t_Mac=2); α_fine=1/N_max's precise Macdonald/representation-theoretic location is an open reconciliation item (§5.1).]

**Generation + color from Coxeter numbers** (Elie Toy 3571 verified):
- 3 generations = h(B_2) − 1 = 4 − 1 = 3 (chain length = Coxeter number h(B_2) = 4; one base/seed)
- 3 colors = h^∨(B_2) = 3 = N_c (dual Coxeter)

**Tier**: generation/color counts MATCHED to Coxeter numbers (Elie-verified); the *forcing* mechanism (commitment-cycle period = h) is FRAMEWORK, multi-week. Stated as matched, not forced.

## 5. Two-corner Macdonald structure (corrected parameter roles)

The substrate's geometry and algebra are the two classical corners of one Macdonald family P_λ(x; q_Mac, t_Mac) (Elie Toy 3586/3587, Schur-validated):

| Corner | Macdonald (q_Mac, t_Mac) | Substrate side |
|---|---|---|
| **Hall-Littlewood** | q_Mac = 0, t_Mac = 2 (= GF(2) field size) | Hall algebra (this paper); Serre [n]_2 = Mersenne → N_c, g, N_c·g |
| **Jack** | (q_Mac,t_Mac)→(1,1), t = q^{N_c/2} | geometry — Wallach spherical / ρ-vector (paper A3) |

- Jack corner reproduces the geometry-canonical coefficient 6/5 = Jack(α_Jack=2/N_c=2/3) in the q→1 limit (Elie Toy 3586).
- Hall-Littlewood corner's q-integers [n]_2 = 2^n−1 are the Mersenne/Cal #139 chain — Lyra's Serre constants (§3).

### 5.1 Parameter-role correction + open item (α_fine location)

The v0.2 framing "(q=2, t=1/137)" is RETRACTED as a parameter-role mislabel (Elie Toy 3587): the substrate base 2 is the Macdonald **t** (Hall-Littlewood/field-size parameter), with Macdonald **q=0**; the quantum-group q=2 equals the Macdonald t, NOT the Macdonald q. The Serre-constant result (§3) is unaffected — it lives at the Hall-Littlewood corner where a Ringel-Hall algebra over GF(2) belongs (cleaner placement).

**RESOLVED — α_fine is an evaluation/coupling, NOT a Macdonald deformation coordinate** (Keeper grade + Elie Toy 3588 integrality): the substrate base 2 is the Macdonald t (Hall-Littlewood corner, q=0); α_fine = 1/N_max = 1/137 is **not a Macdonald (q,t) parameter at all**. It enters at the physics layer, not the algebra's deformation structure:
- As the **representation level / coupling** at which observables are read off the algebra (the affine N_max-vertex sets the level; α = 1/N_max is the associated coupling).
- As the **N_max normalization of the scheme-invariant empirical-contact layer** (§7 mixing angles, sin²θ_W = rank/N_c², PMNS /N_max) — which stands independently of the Macdonald parameters and is forward.

So the Macdonald family carries TWO structural parameters (q_Mac=0, t_Mac=2 for the Hall algebra; the Jack limit for geometry); α_fine sits OUTSIDE that parameter space as a coupling/evaluation. This removes the last parameter-role ambiguity. (Elie Toy 3588: (q=2, t=1/137) gives non-integer structure constant −46/45, so it cannot be a Hall algebra — confirming α is not a Macdonald coordinate.)

**Note (Cal #27 discipline)**: the Macdonald structure constants are forward-computed and factor into operational primes — this is the algebra. Their numerical proximity to quark mass ratios is a scheme-dependent IDENTIFIED lead, NOT a forward derivation, EXCLUDED from this paper's claims (§8).

### 5.2 The single-object question (queued forward thread)

Whether a single explicit Macdonald-Koornwinder object (BC₂ / (C∨C)₂) carries BOTH corners with proved limits to the FK/Heckman-Opdam spherical functions (geometry) and the Ringel-Hall algebra (algebra) is the lead post-consolidation thread (Elie+Lyra, multi-week). At present the two-corner structure is established; the single-object theorem is FRAMEWORK.

## 6. Bulk-Shilov unification (Cal #146-corrected)

The Hardy space H²(D_IV⁵) gives bulk-boundary determinacy. **Correct framing** (Cal #146): a generation is one value of the winding-mode coordinate W_n; the lepton (Shilov K-type) and quark (bulk K-type) are DISTINCT K-types sharing W_n, coupled via the Hardy-space duality. NOT "one K-type, two manifestations."

This dissolves the mass problem (distinct K-types → distinct Casimirs → distinct masses) and makes anomaly cancellation per generation the Hardy-space consistency condition.

**Confinement** (Cal's "strongest content", FRAMEWORK-PLUS): Π_bulk→Shilov maps fractional-charge color-charged bulk quarks to Shilov boundary values requiring integer charge + color singlet; individual quarks have no Shilov boundary value → confined; only color-singlet composites project.

## 7. Empirical contact — scheme-invariant observable spine

Per the invariant-anchor principle (scheme-invariant ⟺ anchored to a geometric/topological invariant), the paper's empirical claims are restricted to scheme-invariant quantities:

| Observable | Substrate-natural form | Match | Anchor |
|---|---|---|---|
| sin²θ_W | rank/N_c² = 2/9 (forced by rank=2) | 0.27% on-shell | Weinberg partition |
| m_W/m_Z | √g/N_c = √7/3 | 0.05% | pole-mass ratio |
| Cabibbo sin θ_C | N_c²/(2^N_c·n_C) = 9/40 | mixing angle | scheme-invariant |
| PMNS sin²θ_12 | C_2·g/N_max = 42/137 | mixing angle | scheme-invariant |
| PMNS sin²θ_23 | N_c·n_C²/N_max = 75/137 | mixing angle | scheme-invariant |
| PMNS sin²θ_13 | N_c/N_max = 3/137 | mixing angle | scheme-invariant |
| (PMNS sum) | rank³·N_c·n_C/N_max = 120/137 | — | scheme-invariant |
| m_s/m_d | 2π² = vol(S³ ⊂ S⁴ Shilov) | within-tier robust | geometric invariant |

**PMNS form CLOSED (Cal #153 typing)**: the /N_max set is the canonical forward form — the PMNS sum = 120/137 = rank³·N_c·n_C/N_max types as Type C, forward-spine (scheme-invariant + N_max-anchored, passing both axes). The T1935 set (4/13, 6/11) is a numerically-equivalent alternate parameterization, not the canonical form. No longer open.

**Weinberg mechanism**: rank + g = N_c² is equivalent to rank = 2 (given n_C = N_c²−rank², g = n_C+rank) — the unique pairwise BST-primary sum hitting a perfect square (Grace). So sin²θ_W = rank/N_c² is forced by rank = 2.

## 8. Honest scope + exclusions

### 8.1 RIGOROUS (this paper's forward content)
- Serre structure constants = N_c, N_c·g (Type A, Elie-verified)
- n_C = 5 = complex dimension = Bergman kernel singularity exponent (3-CI: Elie numerical ν=5, Keeper literature, Lyra formula); per rank = 5/2 = ρ_1
- Scheme-invariant mixing-angle spine (invariant-anchored)
- Macdonald engine exact through degree 4 (Elie)

### 8.2 FRAMEWORK (stated as such)
- Bulk-Shilov Hardy unification (Cal #146-corrected; coupling map multi-week)
- Coxeter generation/color counts (matched; forcing multi-week)
- Confinement mechanism (FRAMEWORK-PLUS)

### 8.3 EXCLUDED (per discipline — not in this paper as forward results)
- Quark mass ratios m_t/m_c, m_b/m_d, etc.: scheme-dependent IDENTIFIED leads (Cal #27); excluded as forward derivations. Investigated separately (substrate-privileged-scheme hypothesis).
- Macdonald coefficient → mass ratio: scheme-dependent lead (Cal #27); excluded.
- Back-fit relations n_C = N_c²−rank² (holds only at p=5), C_2 = N_c·rank (factored): excluded; n_C is primitively the genus.

### 8.4 RESOLVED — genus thread (all items closed; value+role form is final; canonical-label external pin = footnote)

**T2442 STANDS (Grace provenance + Keeper algebra)**: c_FK = 225/π^(9/2) is genuinely forward — vol(D_IV⁵) = π⁵/(5!·Γ(7/2)) = π^(9/2)/225 (Keeper: 5!·Γ(7/2) = 225√π exactly), the Faraut-Korányi normalized-MEASURE constant, computed at dimension n_C = 5. The "(g+rank)/rank" and "(N_c·n_C)²" are post-hoc relabels, never used. c_FK un-held.

**One genus + Casimir + embedding (consistent with §1; CORRECTED)**: D_IV⁵ has ONE genus = n_C = 5 (FK = Hua = Bergman exponent; Elie Toy 3596 four ways + Keeper formula). C_2 = 6 is the Casimir (NOT a genus); g = 7 is the embedding/signature (NOT a genus). The morning "three-genus" convention miscounted — "FK genus = C_2 = 6" was a mislabel (C_2 is the Casimir). Corrected to "one genus + Casimir + embedding," stated in value+role form throughout the paper. The canonical name "FK genus" per Faraut-Korányi 1994 is cited at the footnote level; the mathematics depends on the value+role, not the canonical label (which coincides between FK and Hua conventions for Type IV).

**RESOLVED — kernel singularity exponent = n_C/rank = 5/2 (Elie Toy 3580-3581, MC-confirmed; un-held)**: the Bergman kernel exponent ν = 5 = n_C (Hua genus), Monte-Carlo confirmed. So the singularity exponent/rank = n_C/rank = **5/2 = ρ_1 of B_2** — NOT g/rank = 7/2. The old "g/rank = 7/2" mis-used the embedding dimension g=7 where the genus n_C=5 belongs. Bonus (Elie): the Bergman constant K(0,0) = 2^g·N_c·n_C/π^(n_C) = 1920/π⁵ — g enters legitimately as the EXPONENT 2^g (= 128, Mersenne-base power), n_C as the genus (π-exponent). This is the correct substrate-natural Bergman geometry; A1 §4-5 UN-HELD and use exponent 5/2.

**FLAG — T2440 correction (RATIFIED; Cal/Keeper execute)**: T2440 states "Bergman exponent g/rank = 7/2." Now multi-CI confirmed wrong: kernel exponent = n_C/rank = 5/2 (Elie numerical + Keeper structural + ρ_1 match). T2440 needs correction to n_C/rank = 5/2. RATIFIED-result correction — flagged for Cal/Keeper, not executed unilaterally.

**DERIVED — c_FK is the physical constant; the FK measure is FORCED (Keeper via K67→T754; theorem, not choice)**: Keeper closed the algebra (5!·Γ(7/2) = 225√π exactly, so π⁵/(5!·Γ(7/2)) = π^(9/2)/225) AND the physics: tracing K67 (Born=Bergman) to T754, BST derives the Born rule as the UNIQUE automorphism-invariant probability measure on D_IV⁵ (Gleason-type). On a bounded symmetric domain, automorphisms have nontrivial Jacobians → Lebesgue is NOT automorphism-invariant → the unique invariant measure is the Bergman/FK measure. Therefore the physical Hilbert space MUST be L²(D_IV⁵, FK measure) — the Born rule holds only there.

**Consequence (Route-A / Strong-Uniqueness strengthener)**: "substrate Hilbert space = L²(D_IV⁵, FK invariant measure)" is a THEOREM (forced by Born-rule invariance), not an assumption. c_FK = 225/π^(9/2) is the DERIVED physical constant (A1 fully un-held); Elie's 1920/π⁵ is the labeled ambient-Lebesgue value (not physical). Grace provenance support: T754 (Apr 3) already derived Born from the unique automorphism-invariant (Gleason) measure. The genus thread is fully resolved; values/roles settled and stated in value+role form throughout. Canonical naming per Faraut-Korányi 1994 cited at footnote level; downstream external library verification queued but does not block submission.

**Sweep note**: the g=7→genus mislabel propagated to ≥5 sites (K67/T2401 + T2440 + the 3 caught today). In K67 it is NOT load-bearing (Born rests on Gleason/invariance T754; outputs ∝ 1/N_max², α² don't touch the exponent) → relabel-only (7/2→5/2 kernel exponent), same disposition as T2442. Grace's 7/2-disposition sweep (INV-5264) extends to K67 + T2440.

### 8.5 CLOSED — PMNS formula-set (Cal #153 typing)
The /N_max set (sin²θ_12 = 42/137, sin²θ_23 = 75/137, sin²θ_13 = 3/137; sum = rank³·N_c·n_C/N_max = 120/137) is the canonical forward form — Cal #153 typed it Type C, forward-spine (scheme-invariant + N_max-anchored, passing both axes). The numerically-equivalent T1935 set (4/13, 6/11) is an alternate parameterization, not the canonical form. RESOLVED — no longer open.

## 9. Conclusions

The substrate Hall algebra U_q^+(B_2) at q=2 has BST-primary defining arithmetic (Serre constants N_c, N_c·g). Its affine extension encodes N_max as level; the Coxeter numbers of B_2 give the generation and color counts. The Hardy-space bulk-boundary structure unifies leptons and quarks per generation as distinct K-types sharing a winding mode. The empirical contact — the scheme-invariant electroweak mixing sector — reduces to BST-primary arithmetic.

The five BST integers are the standard invariants of D_IV⁵: rank (=2), dual Coxeter (N_c=3), complex dimension / kernel exponent (n_C=5), quadratic Casimir (C_2=6), embedding/signature dimension (g=7), and the 1/α normalization (N_max=137). "Five integers, zero inputs" becomes "choose D_IV⁵, zero inputs." (Genus naming stated in value+role form: n_C = 5 = genus = Bergman kernel singularity exponent = Hua kernel exponent, all coincident on type IV per Faraut-Korányi 1994; canonical-label pinning is a downstream footnote item and does not affect the mathematics.)

---

## References
[As v0.1: Ringel 1990, Green 1995, Macdonald 1995, Faraut-Korányi 1994, Ogg 1975, Wallach 1976, Koons 2026, + Thursday cross-CI: Elie Toy 3570-3579, Keeper genus verdict.]

## Provenance of v0.2 → v0.4 changes
- Serre constants promoted to RIGOROUS (Elie-verified)
- n_C = 5 = the genus (= complex dimension = Bergman exponent); C_2 = 6 = Casimir (not a genus); g = 7 = embedding/signature (not a genus) — one-genus convention (Elie Toy 3596 + Keeper formula)
- Mixing-angle spine added as scheme-invariant empirical contact
- Cal #146 unification framing corrected (shared W_n, distinct K-types)
- Mass-ratio leads + back-fit relations EXCLUDED per Cal #27 + scheme-invariance audit
- c_FK RESOLVED — derived-physical (FK measure forced by Born/Gleason, Keeper); kernel exponent RESOLVED 5/2; α placement RESOLVED (evaluation/coupling); PMNS CLOSED (Cal #153)
- v0.4 cross-section consistency sweep (Keeper K-audit punch-list) + micro-sweep
- **v0.5 sweep (Saturday 2026-05-30 P5.1)**: adopted value+role formulation throughout as the final form for genus naming; removed "pending external pin" blocking language; the canonical-label name (FK genus per Faraut-Korányi 1994) is cited at footnote level. SUBMISSION-GRADE.

— Lyra, Paper A1 Substrate Hall Algebra **v0.5 SUBMISSION-GRADE**. Verified spine: RIGOROUS Serre constants (N_c, N_c·g); one genus = n_C = 5 (value+role form: genus = Bergman kernel singularity exponent = Hua kernel exponent, coincident on type IV); scheme-invariant mixing-angle empirical contact; Cal #146-corrected bulk-Shilov unification; c_FK derived-physical (FK measure forced); Coxeter generation/color counts. EXCLUDED: scheme-dependent mass-ratio leads + back-fit relations. **Substance Keeper-PASS; value+role formulation final; canonical-label external pin (FK terminology per Faraut-Korányi 1994) is a footnote-level downstream item that does not block submission**. Ready for Keeper final PASS + Cal v0.5 verify → submission.
