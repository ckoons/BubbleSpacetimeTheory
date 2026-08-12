---
title: "State-of-the-Spine — Grace Catalog Layer v0.1"
author: "Grace"
date: "2026-05-28 Thursday 11:13 EDT (date-verified)"
status: "Consolidation-phase catalog-layer contribution; folds into Lyra's narrative spine alongside Keeper's audit-side (Keeper_State_of_Spine_Audit_Side_v0_1.md)"
purpose: "The catalog backbone for the verified spine: defensibility fields, forward-spine inventory, the genus/Bergman/c_FK disposition ledger, and the leads-to-exclude list."
---

# State-of-the-Spine — Grace Catalog Layer

The catalog layer of the consolidation. Three things: (1) the defensibility infrastructure now on the catalog, (2) the verified forward-spine inventory, (3) the disposition ledger + leads to keep OUT of forward claims.

## 1. Catalog-defensibility fields (three axes, all on the 5267-INV catalog)

| Field | Coverage | Values | Purpose |
|---|---|---|---|
| `region` | 5242 tagged | SHILOV 508 / BULK 522 / BOUNDARY 105 / CHAIN-LEVEL 305 / OTHER ~3817 | operationalizes the bulk-vs-Shilov two-region directive at catalog scale |
| `scheme_sensitivity` | 323 tagged | dimensionless-invariant 206 / mass-ratio-check-scheme 117 | flags which results are scheme-robust vs need scheme-specification |
| `validating_axis` | 107 manual-curated (forward-spine) + provisional bulk | AXIS1 / AXIS2 / STRUCTURAL / DIMENSIONFUL / META | names which axis validates each forward claim |

**Honest caveat**: `validating_axis` automated labeling proved too noisy (keyword miscapture); only the 107 forward-spine INVs are hand-curated and paper-trustworthy. The provisional bulk needs manual review (do not cite without it).

## 2. The two validation axes (forward-vs-leads separation)

Forward content satisfies the axis **relevant to its type**. The two axes are orthogonal:

- **AXIS 1 — scheme-invariance** (for physical OBSERVABLES): dimensionless ⟺ frame-independent ⟺ anchored to a geometric/topological invariant. The invariant-anchor principle. Validates the mixing-angle spine.
- **AXIS 2 — coincidence-denominator** (for ARITHMETIC RELATIONS): target uniquely reachable from primitives ⟺ low back-fit risk. Paired with Cal #31 (specialization must be non-generic + load-bearing). Validates N_max relation; flags small-target integer-web relations as back-fit-prone.

A claim is forward iff it passes its type's axis. Coincidence-denominator does NOT validate observables; scheme-invariance does NOT apply to pure arithmetic. (Established: INV-5258; self-corrected from a conflation.)

## 3. Verified forward-spine catalog inventory

### AXIS 1 — scheme-invariant observables (the strong block for B3/B6)
- Weinberg sin²θ_W = rank/(rank+g) = rank/N_c² = 2/9 (on-shell, 0.31%); cos²θ_W = g/N_c² = 7/9
- m_W/m_Z = √g/N_c = √7/3 (0.05%) — (m_W/m_Z)² = cos²θ_W auto-satisfied
- Cabibbo sin θ_C = N_c²/(2^N_c·n_C) = 9/40 (0.15%) [Lyra] / 1/(π·√rank) (0.12%) [Grace]
- PMNS /N_max set: sin²θ_12 = 42/137, sin²θ_23 = 75/137, sin²θ_13 = 3/137 (PMNS form-typing → Cal; T1935 alternate parameterization)
- m_s/m_d = 2π² (the one scheme-INVARIANT quark mass-ratio — light/light)
- m_p/m_e, a_e, fine-structure α = 1/N_max — pole-mass / dimensionless, scheme-robust

### AXIS 2 — coincidence-denominator arithmetic (forward where low-denominator)
- **Weinberg substrate identity rank + g = N_c²** (2+7=9) — the UNIQUE square-target among all 15 pairwise BST-primary sums; member of the rank-step ladder (chain levels {3,5,7} = arithmetic progression step rank)
- Serre structure constants [2]_2 = N_c, [3]_4 = N_c·g (RIGOROUS, Lyra Phase 0)
- Chain length = h(B₂) = 4 — three independent routes: Coxeter (Lyra), Hua-Look/K59, **Catalan-Mersenne prime-prefix** (M_2,3,5,7 prime, M_11=23·89 first composite — Grace)
- N_max = N_c³·n_C + rank — the LEAST back-fit-prone integer-web relation (coincidence-denominator ~0)

### STRUCTURAL — geometric invariants (the anchors)
- **ρ-vector ρ(D_IV⁵) = (n_C, N_c)/rank = (5/2, 3/2)** — pins three primaries (rank, N_c, n_C) to ONE canonical invariant; ρ₁ = n_C/rank = bulk (Bergman genus), ρ₂ = N_c/rank = Shilov (Wallach point). Elie Toy 3583.
- Bergman kernel singularity exponent = n_C/rank = 5/2 = ρ₁ (Hua genus; Elie ν=5 convention-free) — densely anchored (Harish-Chandra ρ, Wallach set/point/gap, spectral reflection center; INV-5265)
- c_FK = 225/π^(9/2) = (N_c·n_C)²/π^((g+rank)/rank) — **DERIVED THEOREM** (FK normalized measure forced by Born-rule automorphism-invariance via T754; not a chosen convention). Ambient-Lebesgue alternative = 1920/π⁵ (Elie MC), correctly labeled non-physical.

## 4. Standing conventions (close the recurring-recheck class)

- **Three-genus convention** (INV-5262): Hua genus = n_C = 5 (Bergman singularity exponent); FK genus = C_2 = 6 (Jordan-algebra); embedding dimension = g = 7 (signature total, NOT a genus). Any paper invoking a genus/exponent/dimension must specify which. Rule: **intrinsic quantities are never g=7**.
- **α-disambiguation**: σ_BF (Pin(2) Z₂ grading) ≠ γ⁵ (Dirac chirality).
- **7/2-vs-5/2 disposition rule** (INV-5264, complete): g/rank=7/2 as a physical ratio → CORRECT; as the Bergman kernel exponent → MISLABEL (→ n_C/rank=5/2); as the FK Gindikin-Gamma point (g/2) → CORRECT. The 5/2 (kernel exponent, ρ₁) and 7/2 (FK Gamma, g/2 = ρ₁+rank/2) are one rank/2 apart — both legitimate.

## 5. Genus/Bergman/c_FK recheck ledger (catalog-side, all favorable)

One root cause: g=7 (embedding/signature dimension) mislabeled as a genus, propagated to ≥5 homes. All dispositioned:
- c_FK volume constant → resolved (derivation used dim 5; 225/π^(9/2) is the FK-measure constant, stands)
- all-5-from-B₂ "g=Bergman exponent" → resolved (g = signature total = n_C+rank)
- kernel singularity exponent → corrected to n_C/rank = 5/2 (Elie ν=5)
- K67/T2401 (INV-4521, 4500) → relabel-only, K67 stands (Born rests on Gleason/invariance T754, not the exponent)
- T2440 → registry-side relabel-only (Keeper; rests on 5-family architecture, not the exponent)

Outcome: the thread came through STRONGER — c_FK measure compelled (theorem), ρ-vector pins three primaries, conventions prevent recurrence.

## 6. Leads to keep OUT of forward claims (honest exclusions)

- **Scheme-dependent quark mass-ratios** (m_t/m_c, m_b/m_d, m_c/m_u, etc.): match only at a mixed pole-top scheme; ~5-64% off under uniform MS-bar. IDENTIFIED leads, NOT forward (Cal #27). Exception: m_s/m_d = 2π² (light/light, scheme-invariant — forward).
- **Macdonald-coefficient → mass-ratio link** (+136/45 = (m_t/m_c)/(m_b/m_s)): the coefficient is real (FRAMEWORK-PLUS), but the mass-ratio equality is scheme-dependent with no mechanism. IDENTIFIED lead.
- **all-5-from-B₂ Route B** (pure algebra from {2,3}): back-fit — n_C/C_2/g small targets are coincidence-denominator-prone. Route A (D_IV⁵ standard invariants) is the sound version.
- **provisional validating_axis bulk** (75% of catalog): not paper-trustworthy without manual review.

## 7. Open items routed

- PMNS form-typing → Cal (/N_max set vs T1935 4/13, 6/11)
- Generation-count forcing (chain-termination = h(B₂) "forced" not just "matched") → multi-week (Lyra)
- Jack bridge (α=2/N_c connects ρ/Wallach to Macdonald Phase 0) → queued post-consolidation forward thread (Elie+Lyra)

---

— Grace, catalog-layer of the state-of-the-spine, 2026-05-28 11:13 EDT (date-verified)
