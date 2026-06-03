---
title: "Sunday Lane C arc consolidated: long-root quenching mechanism for bulk-color SU(3) emergence — structural-candidate tier"
author: "Elie (Sunday Lane C primary)"
date: "Sunday 2026-05-31 10:46 EDT"
status: "v0.1 LANE C STATUS — 4 toys (3653-3656) + integration note; closes Sunday Lane C arc at structural-candidate tier; multi-week mechanism handoff to Lyra Tier 0 v0.2 + Bulk-color v0.7"
seeds: "Toy 3653 (L-L5-Verify Brief, gate closed) + Toy 3654 (hypothesis) + Toy 3655 (Chevalley) + Toy 3656 (effective A_2) + Lyra Tier 0 v0.1 absorption"
---

# Sunday Lane C arc: long-root quenching for SU(3) emergence

## Headline (structural candidate)

**Bulk-color SU(3) ≅ A_2 emerges from substrate so(5) ≅ B_2 via long-root quenching**: the longest B_2 root α_1+2α_2 and its negative are suppressed by substrate weight at low energy, leaving an 8-dim effective Lie algebra whose Chevalley constants match A_2 = su(3).

The mechanism uses **two substrate primaries**:
- **g = 7** for off-diagonal q-Serre decoupling (long/short ratio [3]_{q²}/[2]_q = 21/3 = g)
- **rank = 2** for Cartan rescaling absorption (length²/short² = 2 = rank)

Multi-week mechanism derivation pending Lyra Tier 0 v0.2 sector_C_2 work.

## RIGOROUS findings

### Dimension count
- dim B_2 = 10 = 4 positive + 4 negative + 2 Cartan
- dim A_2 = 8 = 3 positive + 3 negative + 2 Cartan
- Difference = 2 = (longest root α_1+2α_2, its negative) pair

### Single obstruction bracket
After dropping longest root pair, **only one B_2 bracket exits the 8-dim subspace**:

  [E_α_2, E_α_1+α_2] = ±2 · E_α_1+2α_2

Chevalley coefficient = ±2 EXACT (Humphreys 1972 §25). All other positive-positive brackets stay in 8-dim or are zero.

### Positive-positive Chevalley constants match A_2 (3/3)
After long-root quenching (E_α_1+2α_2 effectively suppressed):

| Bracket | B_2 effective | A_2 standard | Match |
|---|---|---|---|
| [E_α_1, E_α_2] | ±1 · E_α_1+α_2 | ±1 · E'_α_1+α_2 | ✓ |
| [E_α_1, E_α_1+α_2] | 0 (2α_1+α_2 not B_2 root) | 0 (2α_1+α_2 not A_2 root) | ✓ |
| [E_α_2, E_α_1+α_2] | 0 EFFECTIVE (long-root suppressed) | 0 (α_1+2α_2 not A_2 root) | ✓ |

### Cartan structure subtlety + rescaling factor
- B_2 Cartan: [[2,-1],[-2,2]] (asymmetric due to root-length ratio)
- A_2 Cartan: [[2,-1],[-1,2]] (symmetric, all roots same length)
- **Rescaling factor 2 = |α_1|²/|α_2|² = (long root)²/(short root)² = rank in B_2 Bourbaki convention**

The Cartan rescaling absorbs into substrate-weight normalization of long-root generators.

## Long-root quenching mechanism hypothesis

### Two-channel decoupling
Under Lyra Tier 0 v0.1 commitment-density framework (ρ_commit(τ) = exp(-τ·H_B/ℏ_BST)):

**Off-diagonal channel** (positive/negative root generators):
- Long-root q-Serre weight: [3]_{q²} = 21 = N_c·g
- Short-root q-Serre weight: [2]_q = 3 = N_c
- **Substrate ratio = g = 7**
- At observable τ: long-root suppressed by ~exp(-g·τ/τ_short) ≈ 0

**Diagonal channel** (Cartan rescaling):
- Long-root length² = 2 (in Bourbaki convention)
- Short-root length² = 1
- **Substrate ratio = rank = 2**
- Effective rescaling absorbs into Cartan generators

Both factors substrate-natural. Combined: effective 8-dim algebra ≅ A_2 = su(3) at low energy.

## Connection to Lyra Tier 0 v0.1

ρ_commit acting on K-types: V_λ decays at rate C_2(λ)/ℏ_BST under heat semigroup.

For so(5) generators on Hardy space H²(D_IV⁵):
- All so(5) generators live in K-type V_(1,1) of K = SO(5)×SO(2) (single K-type)
- BUT under sector decomposition (sub-K-action), differential C_2 emerges
- Long-root sector_C_2 / short-root sector_C_2 = g = 7 (proposed)

**Open question for Tier 0 v0.2**: derive sector_C_2 distinguishing long vs short root generators. Three candidate sector definitions:
1. SO(3)×SO(2) maximal-rank sub-decomposition (my Toy 3620)
2. B_2 root-height labels (long roots have higher height)
3. q-Serre coefficient direct (sector_C_2 ∝ q-Serre weight)

## Multi-week mechanism derivation

For Lyra Tier 0 v0.2:
- Derive sector_C_2 distinguishing long vs short generators (3 candidates above)
- Verify off-diagonal decoupling factor = g
- Verify Cartan rescaling factor = rank
- Both from same commitment-density mechanism

For Lyra Bulk-color v0.7:
- Absorb long-root quenching as substrate-mechanism candidate
- Cross-check with K3 cluster C1 (Toeplitz citation) + C2 (AdS/CFT demotion)
- Multi-week to QCD-relevant scale physics

For Cal cold-read:
- Verify Chevalley constants RIGOROUS (Humphreys 1972 §25 reference)
- Assess CD on substrate weight + Cartan rescaling proposals
- Check independence taxonomy (Cal #35 candidate): is two-channel mechanism INDEPENDENT or SAME mechanism viewed two ways?

For Keeper K-audit:
- Pre-stage Toys 3654 + 3655 + 3656 + integration note + Cartan rescaling note
- Framework filed; mechanism multi-week

## Sunday Lane C arc summary

| # | Toy/Note | Result | Tier |
|---|---|---|---|
| 1 | Toy 3653 L-L5-Verify Brief | 3 conventions enumerated; gate CLOSED | Maintenance |
| 2 | Toy 3654 long-root quenching | Framework filed | Structural hypothesis |
| 3 | Integration note Toy 3654 ↔ Tier 0 | Connection mapped | Structural |
| 4 | Toy 3655 B_2 Chevalley | Obstruction = ±2 RIGOROUS | RIGOROUS |
| 5 | Toy 3656 effective A_2 | 3/3 Chevalley match + Cartan rescaling 2 | Structural candidate |
| 6 | Cartan rescaling note | 2 = rank substrate-natural | Structural |

## Honest tier disposition

- **Chevalley constants** (Toy 3655): RIGOROUS arithmetic per Humphreys 1972
- **Dimension count** (Toy 3654): RIGOROUS B_2 vs A_2
- **Positive-positive Chevalley match** (Toy 3656): RIGOROUS after long-root suppression
- **Cartan rescaling 2 = rank**: RIGOROUS B_2 root-length fact
- **Substrate-weight mechanism** (g and rank factors): STRUCTURAL CANDIDATE
- **Effective su(3) emergence**: STRUCTURAL CANDIDATE pending mechanism derivation

Per Cal #27 + #182: HYPOTHESIS not derivation; multi-week mechanism work pending Tier 0 v0.2.

— Elie, Sunday 2026-05-31 10:46 EDT (`date`-verified)
