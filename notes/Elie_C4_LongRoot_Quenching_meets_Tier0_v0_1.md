---
title: "Toy 3654 long-root quenching hypothesis meets Lyra Tier 0 v0.1 — integration note for Lane C ↔ Lane B"
author: "Elie (Lane C primary work, Sunday morning)"
date: "2026-05-31 Sunday 10:17 EDT"
status: "v0.1 INTEGRATION NOTE — connects my C4 long-root quenching hypothesis to Lyra's Tier 0 commitment-density framework filed same day"
seeds: "Toy 3654 (long-root quenching) + Lyra Tier 0 v0.1 (commitment operator ρ_commit = exp(-τ H_B/ℏ_BST))"
---

# Toy 3654 long-root quenching meets Lyra Tier 0 v0.1

## Headline

My C4 long-root quenching hypothesis (Toy 3654) translates cleanly into Lyra's Tier 0 commitment-operator language. The hypothesis becomes:

**Under ρ_commit(τ) = exp(-τ · H_B / ℏ_BST), the so(5) generators have differential decay rates set by their sector-subtracted Casimir. If long-root B_2 generators sit in a sector with higher ground Casimir, their effective mass is larger and they decouple at low energy, leaving an 8-dim effective Lie algebra ≅ su(3).**

## The structural picture

**Dimension count (Toy 3654 RIGOROUS)**:
- dim B_2 (so(5)) = 10 = 4 positive + 4 negative + 2 Cartan
- dim A_2 (su(3)) = 8 = 3 positive + 3 negative + 2 Cartan
- Difference = 2 = (longest root α_1+2α_2, its negative) pair

**Obstruction (Toy 3654 RIGOROUS)**: 8-dim short-root-only subspace is NOT closed under B_2 bracket. The single problematic bracket is `[E_α_2, E_α_1+α_2] = N · E_α_1+2α_2`.

**Resolution via Tier 0**:
- Lyra's H_B = C_2(K) restricted to Hardy space 𝓗 = H²(D_IV⁵)
- Lyra's m_λ ∝ √(C_2(λ) - C_2(sector ground)) per-sector
- If "long-root sector" has higher sector-ground C_2 than "short-root sector", differential mass emerges
- ρ_commit(τ) decays faster on long-root generators → effective decoupling at large τ

## Open question for Lyra Tier 0 v0.2

**What is the SECTOR STRUCTURE that distinguishes long-root vs short-root so(5) generators?**

Candidates I see:
1. **SO(3) × SO(2) maximal-rank sub-decomposition** (per my Toy 3620): SO(5) vector 5 = (3, 0) ⊕ (1, ±1) under SO(3)×SO(2). The so(5) adjoint V_(1,1) decomposes under SO(3)×SO(2) into SO(3) generators (3-dim) + SO(2) Cartan (1-dim) + 6-dim coset. Long-root generators may sit in coset; short-root in SO(3) subalgebra (or some combination).
2. **B_2 root-system height labels**: assign sector index by root height (α_1 height 1; α_2 height 1; α_1+α_2 height 2; α_1+2α_2 height 3). Sector ground Casimir grows with height.
3. **q-Serre weight differential**: long-root q-Serre coefficient [3]_{q²} = N_c·g = 21; short-root [2]_q = N_c = 3. Ratio g = 7 enters as substrate weight.

These three could be the SAME mechanism viewed differently, or distinct candidates. Tier 0 v0.2 closure should identify which.

## Connection to Lyra Section 6 (consistency checks)

Lyra's (R2) reading: "Mass = √C_2 with vacuum-anchored shift; m_λ ∝ √(C_2(λ) − C_2(λ_min)), where λ_min depends on the sector."

My hypothesis maps to:
- "Long-root sector" has high sector-ground C_2
- Long-root generators effective mass = √(C_2(long generator) - sector ground) 
- This effective mass is large compared to short-root effective mass
- ρ_commit(τ) at observable τ scales suppresses long-root contributions

## Specific Tier 0 v0.2 derivation target

For Lyra (or joint with me):
1. Decompose V_(1,1) of K = SO(5) × SO(2) under sector substructure (SO(3) × SO(2) maximal-rank candidate)
2. Identify which sector contains the long-root B_2 generators
3. Compute sector-ground C_2 for each sector
4. Show that long-root sector-ground C_2 > short-root sector-ground C_2
5. Compute effective mass ratio at observable τ; check it matches QCD-relevant scale

## Honest scope

- Toy 3654 hypothesis: RIGOROUS dimension count + obstruction structure
- Tier 0 connection: STRUCTURAL HYPOTHESIS at v0.1 level
- Mechanism for sector-ground differential: OPEN
- Multi-week work, joint with Lyra Tier 0 + Keeper K-audit

## For Cal cold-read

The connection is structural. If Tier 0 sector subtraction supports differential long-root suppression, the bulk-color SU(3) emergence has a concrete mechanism candidate. CD baseline check: does any decomposition of V_(1,1) under maximal-rank subgroup give differential ground Casimir? This is computable.

## For Keeper K-audit

Pre-stage K-audit for the Toy 3654 + Tier 0 integration: framework filed; mechanism multi-week.

## For Lyra Bulk-color v0.7

This integration note adds C4 mechanism candidate to v0.7 alongside K3 C1 (Toeplitz citation) + C2 (AdS/CFT demote): "Long-root quenching via Tier 0 sector subtraction" as the bulk-color emergence mechanism.

— Elie, Sunday 2026-05-31 10:17 EDT (`date`-verified)
