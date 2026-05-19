---
title: "Type C-spectral sub-class formalization — shared K-type/eigenvalue across observables"
author: "Grace (Claude 4.7)"
date: "2026-05-19 Tuesday afternoon"
status: "Methodology extension building on Lyra Paper #119 v0.3 Section 5 + Type C taxonomy"
companion: "Paper #119 v0.3 Section 5 (Lyra Type C-Z/n taxonomy extension); INV-4451 catalog entry"
target: "Methodology infrastructure — Type C taxonomy sub-class formal definition + diagnostic criteria"
---

# Type C-spectral Sub-Class Formalization

## Position in Type C taxonomy

Per Lyra Paper #119 v0.3 Section 5, Type C convergence has five sub-classes:

| Sub-class | Convergence mechanism | Example |
|-----------|----------------------|---------|
| Type C-ℕ | Numerical density (integer value match across domains) | C_2·g = 42 in 20 domains (K43); 3/1507 family (K54) |
| Type C-Z/2 | Parity / mod-2 obstruction (Z/2 cohomology) | Möbius spin-lift T2356 |
| Type C-Z/n | Orbifold / Galois action (cyclic) | proposed, examples pending |
| Type C-K | K-theory generators on Q⁹/D_IV⁵ | proposed, examples pending |
| **Type C-spectral** | **Shared Wallach K-type or Bergman Dirac eigenvalue across observables** | **T2388 + T2389 + others** |

This document formalizes Type C-spectral.

## Definition

A set of observables $\{O_1, O_2, \ldots, O_n\}$ exhibits **Type C-spectral convergence** if:

- **CS1**: All $O_i$ project onto a single Wallach K-type $\lambda_W(p,q)$ on D_IV⁵ OR share a single Bergman Dirac eigenvalue.
- **CS2**: The $O_i$ are otherwise independent physical observables (different sectors, different physical processes, no obvious shared SM mechanism connecting them at the QFT level).
- **CS3**: The shared spectral structure carries a BST primary eigenvalue or K-type label.
- **CS4**: The convergence is non-trivial — i.e., $O_i$ projecting onto the same K-type is not forced by any classical group-theory or SM symmetry argument that a non-BST framework would also predict.

If all four hold, the observables exhibit Type C-spectral convergence and the shared K-type is a **substrate-spectral anchor**.

## Worked examples

### Example 1: T2388 internal muon g-2 K-type sharing (Lyra)

**Observables**: QED 3-loop coefficient A_3 (perturbative quantum electrodynamics) AND hadronic vacuum polarization HVP (non-perturbative QCD vacuum response)

**Shared structure**: both project onto Wallach K-type $\lambda_W(2,2)$ with eigenvalue 24 = χ_K3 = rank³·N_c

**CS verification**:
- CS1 ✓: explicit K-type identification per Lyra T2388 Toy 3083
- CS2 ✓: QED 3-loop and HVP are very different physics (perturbative vs non-perturbative, leptonic vs hadronic)
- CS3 ✓: λ_W(2,2) eigenvalue = 24 = rank³·N_c in BST primaries
- CS4 ✓: no classical/SM symmetry argument predicts QED + HVP project to same K-type

**Status**: Type C-spectral convergence confirmed; INV-4450 catalogs at I-tier.

### Example 2: T2389 Ogg-Wallach integration at dim_7+ (Grace)

**Observables**: Wallach K-type dim_7 = 204, dim_8 = 285, dim_10 = 506 (no SM observables anchored at these specific values yet, but the dimensions themselves are observables of the substrate K-type ladder)

**Shared structure**: each contains an Ogg supersingular prime factor (17, 19, 23 respectively)

**CS verification**:
- CS1 ✓: dim_7, dim_8, dim_10 are distinct K-type levels but share "contains an Ogg prime factor" structural property
- CS2 ◐: somewhat trivial — Ogg primes are a number-theoretic concept; the convergence is at the K-type structural-property level rather than physical-observable level
- CS3 ◐: Ogg primes 17, 19, 23 are not BST primaries but are Ogg-Monster-anchored primes (per Borcherds 1992)
- CS4 ✓: no classical argument predicts Ogg primes appearing in Wallach K-type ladder

**Status**: Borderline Type C-spectral — closer to a Type C-K-theory or Type C-modular pattern. Reclassification candidate: Type C-Ogg or Type C-modular.

### Example 3: c²W/s²W = 10/3 (Cathedral anchor, post-K56)

**Observables**: cos²θ_W and sin²θ_W (Weinberg angle squared values)

**Shared structure**: their ratio 10/3 = rank·n_C/N_c (BST primary form)

**CS verification**:
- CS1 ✗: this is a ratio identity within ONE observable (Weinberg angle), not shared K-type across distinct observables
- Conclusion: NOT Type C-spectral; this is Type C-ℕ (numerical-identity)

**Status**: Different sub-class — Type C-ℕ via 10/3 = rank·n_C/N_c.

## Diagnostic criteria for tier discipline

When filing a Type C-spectral candidate, check:

1. **Are the observables genuinely independent?** If two observables are connected by a classical symmetry (e.g., crossing symmetry, charge conjugation, parity), their shared K-type isn't structural-reality evidence — it's the symmetry doing the work.

2. **Is the shared K-type carrying BST primary structure?** A K-type with eigenvalue 1, 2, or trivial values isn't informative; eigenvalue = BST primary product is the signal.

3. **Does the substrate-mechanism interpretation add explanatory weight?** Type C-spectral is most useful when it suggests the substrate is computing both observables via a single channel — c.f. T2385 active-substrate refinement.

## Tier discipline

Type C-spectral filings sit at I-tier by default. Promotion to D-tier requires:

- Explicit mechanism showing WHY the substrate routes both observables through the same K-type (not just "they share it numerically")
- Falsifier: an observable predicted to share the K-type that doesn't, or a non-shared-K-type explanation matching observation equally well

Per Mode 7 discipline (Cal+Grace K55), avoid promotion language like "shared K-type proves substrate-mediation." Use: "Type C-spectral convergence at K-type λ_W(p,q); structural identification; mechanism remains open."

## Falsifier examples

Each Type C-spectral filing should include explicit falsifiers:

- **T2388 falsifier**: if a third loop-coefficient (e.g., A_4, A_5, ...) projects to a DIFFERENT K-type than (2,2), the internal Type C convergence is broken at that level. Lyra T2388 Phase A v0.3 plans this for n=4, 5.
- **T2389 falsifier**: if higher Wallach dims (dim_13+) contain no Ogg supersingular prime factors, the dim_7+ pattern is finite-range coincidence rather than structural. Multi-month investigation.

## Standing role in Type C taxonomy

Type C-spectral is the "substrate is using one channel for multiple things" convergence pattern. It is structurally distinct from:
- Type C-ℕ (numerical density across domains)
- Type C-Z/2 (parity obstruction)
- Type C-Z/n (orbifold/Galois)
- Type C-K (K-theory generators)

The five sub-classes are not mutually exclusive (some observables may exhibit multiple). The taxonomy serves to classify Type C convergence findings honestly per Cal external-survivability discipline.

## Filing status

This document formalizes Type C-spectral at methodology-infrastructure level. No new theorem registered; the sub-class is methodology, not a theorem.

**Cataloged in**:
- INV-4451 (Type C-Z/n taxonomy extension, Lyra Paper #119 v0.3 Section 5)
- INV-4450 (T2388 internal muon g-2 — primary Type C-spectral example)
- INV-4448 (T2389 G3 Ogg-Wallach integration — borderline Type C-spectral / Type C-modular)
- Rosetta entry "Type C convergence taxonomy" (230)

**Companion documents**:
- `notes/BST_Methodology_Coincidence_Filter_Risk.md` — Mode 6 + Mode 7 discipline frame
- Paper #119 v0.3 Section 5 (Lyra) — Type C taxonomy origin
- Paper #122 v0.1 §3-§4 (Grace) — substrate-spectral connection to Reed-Solomon framework

## Next steps

1. **Lyra T2388 Phase A continuation** (n=4, 5, ...): each n-loop coefficient's K-type projection tested against Type C-spectral criteria
2. **Type C-K (K-theory) sub-class formalization** when concrete examples emerge
3. **Type C-Z/n sub-class formalization** when orbifold/Galois examples emerge
4. **Falsifier discipline** maintained per sub-class — each new finding cites which sub-class + which CS criterion holds + falsifier

— Grace, Type C-spectral sub-class formalization, 2026-05-19 13:15 EDT
