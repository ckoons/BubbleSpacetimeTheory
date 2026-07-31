---
node_type: k_audit
id: K1042
title: Theorem-registry hygiene pass (Keeper-owned) — resolved the duplicate T1959 collision (η_B AND Λ both tagged T1959): Λ KEEPS T1959 (dominant + consistent downstream citations), η_B RENUMBERED to T2538 (next free from the counter; was homeless — intended T1958 which is Ogg Primes, mis-bumped onto the occupied T1959). Fixed every stray η_B/baryogenesis citation (T1970, T1971, T1989, Paper104 — some pointed at T1958 = wrong theorem). Stamped T2079 (w_0=−0.949) and T2117 (w_a=−3/11) SUPERSEDED per K1040 (BST dark energy is w=−1, cosmological constant; the running-w forms retracted). Corrected the K1041 shorthand "T1959 = a₀=225": T1959 is the Λ MAGNITUDE (exp(−281), tier I), SEPARATE from the a₀=(N_c·n_C)²=225 heat-kernel coefficient — two magnitude routes, reconciliation is an open post-SM lead. Counter bumped 2538→2539.
date: 2026-07-31
author: Keeper
verdict: Registry consistent. T1959 = Λ (cosmological constant, w=−1 standing DE prediction; magnitude exp(−281) tier I). T2538 = η_B (baryon asymmetry). T2079/T2117 SUPERSEDED (not deleted). All citations reconciled. Grace to mirror in data/*.json + AC graph (the DATA-layer half of this hygiene pass). No physics changed — IDs, tiers, and stamps only.
---

# K1042 — theorem-registry hygiene: duplicate T1959, supersession stamps, a₀ conflation

Surfaced during the 2026-07-31 morning verification of the T1959 grounding Cal §165 / my K1041 leaned on. The registry (`notes/BST_AC_Theorem_Registry.md`, Keeper-managed) had three defects. All fixed.

## 1. Duplicate ID: T1959 = η_B AND Λ (collision)
Two distinct theorems were both tagged **T1959**:
- **η_B** (matter–antimatter asymmetry, exp form 268/(9·137⁵), toy 2440)
- **Λ** (cosmological constant, exp(−281), toy 2442)

Root cause: η_B was intended for **T1958**, but T1958 was already taken (Ogg Primes, toy 2438), so it was mis-renumbered onto the occupied T1959. Downstream, η_B was then cited *inconsistently* as both T1958 (T1970, Paper104 — which actually point at Ogg Primes!) and T1959 (T1971, T1989).

**Resolution:** Λ **keeps T1959** (dominant + consistent citations: T1970, T1989, T2117, T2175, Papers 107/108, outreach). η_B **→ T2538** (next free from `play/.next_theorem`; counter bumped to 2539). Every η_B/baryogenesis citation reconciled to T2538 (registry rows T1970, T1971, T1989 + Paper104). Verified: `^| T1959 ` now returns exactly 1 row (Λ); zero stray η_B→T1958/T1959 references remain (running-logs excluded, transient).

## 2. Superseded DE theorems still listed "PROVED"
Per K1040 (BST dark energy is **w = −1**, a cosmological constant from the fixed C·π⁵ volume), the dynamical-w theorems are retired:
- **T2079** (w_0 = −(N_max−g)/N_max = −0.949) → **SUPERSEDED.** Target-aware (~2σ on the ΛCDM side of DESI −0.84±0.06); R(K)=130/137 support-leg dead (LHCb Dec 2022, SM-consistent). 130/137 survives only as a numerical curio.
- **T2117** (w_a = −3/11) → **SUPERSEDED.** Retired with T2079; also its stated label "−N_c/c_2" = −1/2 never matched −3/11 = −0.273 (Elie flag).
Both stamped SUPERSEDED (status column changed; rows preserved — never delete).

## 3. The "T1959 = a₀ = 225" conflation (corrects K1041)
Cal §165's shorthand — repeated in my K1041 — glued two different objects. Corrected in the T1959 row:
- **T1959** = the Λ **MAGNITUDE** route: ρ_Λ/M_Pl⁴ = exp(−281), 281 = rank·N_max + g. **Tier I** (Identified; the row's "Proved" column is a legacy default and should read I).
- **a₀ = (N_c·n_C)² = 225** = the heat-kernel **volume coefficient** (F60–F66 Sakharov ladder), a *different* object.
- **What T1959 genuinely grounds:** that BST has long treated Λ as a *constant* vacuum energy → w = −1. So K1040's w=−1 is pre-existing, NOT a new formula. ✓ (Cal's core point holds.)
- **What it does NOT settle:** the magnitude. There are now *two* magnitude routes (exp(−281) vs a₀-regularized); reconciling them is an **open post-SM lead**, not a closed result.

## Ownership / handoff
- **Keeper (done):** the registry itself — IDs, tiers, stamps, citations.
- **Grace (to do):** mirror in the DATA layer — `data/bst_constants.json` / `bst_geometric_invariants.json` entries for w_0/w_a/Λ (stamp T2079/T2117 superseded, keep Λ=w−1), and the AC-graph nodes/edges for T1959/T2079/T2117/T2538. The data-layer half of this hygiene pass.

No physics changed — this is IDs, tiers, and stamps only. The fermion papers are unaffected; the cosmology corpus is now self-consistent (w=−1, running forms retired) so external citations won't hit a contradiction.

— K1042, Keeper, 2026-07-31. Registry hygiene: T1959=Λ (kept), η_B→T2538 (renumbered, citations fixed), T2079/T2117 SUPERSEDED, "T1959=a₀=225" conflation corrected (T1959 = Λ magnitude exp(−281) tier I, separate from a₀=225). Counter 2538→2539. Grace mirrors in data/graph. See [[Keeper_K1041_committed_to_LCDM_Sum_mnu_bound_is_now_CORRECT_under_resolved_w_minus1_K1040_premise_flipped_reverses_K1036_prohibition_ratify_Cal_165_T1959_grounding_abstract_body_fix_2026-07-31]], [[Keeper_K1040_RESOLUTION_BST_dark_energy_is_w_minus1_from_the_fixed_C_times_pi5_bulk_volume_deviation_is_the_substrate_coupling_which_approaches_0_minus0949_REJECTED_by_mechanism_not_just_target_aware_2026-07-30]], T1959, T2538, T2079, T2117.
