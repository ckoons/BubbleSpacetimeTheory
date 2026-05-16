---
title: "K39: χ(Q⁵) Convention Sweep"
author: "Keeper"
date: "2026-05-15"
audit_id: K39
verdict: PASS
overall_confidence: 95%
scope: "Cal TOP-1 finding: χ(Q⁵) = 6 = C_2, NOT 7 = g"
related: ["BST_TOP1_Classical_Topological_Study_DIV5.md", "BST_TOP2_Property_Result_Mapping.md", "CAL_PHASE1_UPDATE_2026-05-15.md"]
---

# K39: χ(Q⁵) Convention Sweep — Verdict PASS

## Background

Cal's TOP-1 finding (2026-05-15, Section "Discrepancies"): The classical Euler characteristic of Q⁵ (the compact dual of D_IV^5, a smooth quadric hypersurface in ℂP⁶) is **χ(Q⁵) = 6 = C_2**. Some BST documents conflated this with g = 7, which is the SO(7) embedding dimension, not the Euler characteristic.

WorkingPaper is correct. Some toy-level documentation needed cleanup.

## Sweep scope

Grep patterns across `play/`, `notes/`, `data/`:
- `chi(Q^5) = 7` (literal)
- `chi(Q^5) = g`
- `χ(Q⁵) = 7`
- `Euler.*Q^5.*7`
- `Euler.*= g\b` near Q^5 references
- `chi_Q5 = 7` or `chi_Q5 = g`

Plus targeted re-read of Paper SP19-2 Poincaré (Cal's named source).

## Findings

### Already actioned this afternoon (per Cal's update note)

This-afternoon-me ran a sweep across 9 files and fixed them. WorkingPaper was already correct. The Poincaré paper now contains an explicit disambiguation line:

> `notes/BST_Paper_SP19_2_Poincare_BST_Native.md:74`:
> Euler characteristic: chi(Q^5) = C_2 = 6 (= c_5[Q^5] = N_c * deg(Q^5) = 3 * 2; g = n_C + rank = 7 is SO(7) embedding dim, not chi)

### One remaining offender (fixed this session)

`play/ac_graph_data.json:85576` — T1827 node "name" description string. Stated `chi(Q^5)=g=7`.

**Fixed (this session)** to:
> `chi(Q^5)=C_2=6 (Cal TOP-1 fix; g=7 is SO(7) embedding dim, not Euler char)`

### Correct references confirmed across the codebase

The dominant pattern across BST toys and notes is correct:
- `play/toy_1664_proton_bulk_geodesic.py:250` — `chi(Q^5) = 6 = C_2` ✓
- `play/toy_1675_proton_plancherel_spectral.py:572` — `chi_Q5 = C_2  # Euler characteristic` ✓
- `play/toy_1676_proton_spectral_geodesic.py:218` — `chi_Q5 = n_C + 1  # = C_2` ✓
- `play/toy_1419_kim_sarnak_bst_reading.py:103` — `T4: Euler characteristic chi(Q^5) = 6 = C_2` ✓
- `play/toy_1865_hodge_ecology_climate.py:59` — `Euler characteristic chi(Q^5) = C_2 = 6` ✓
- `play/toy_2181_exotic_r4_exclusion.py:283` — `chi_Q5 = C_2` ✓
- `notes/BST_Riemann_UnifiedProof.md:20` — uses χ in correct context ✓
- `notes/BST_TOP1_Classical_Topological_Study_DIV5.md:441` — Cal flagging the issue (correct)
- `notes/BST_TOP2_Property_Result_Mapping.md:69, 213` — Cal documenting the discrepancy (correct)

### Final grep verification

After fix, the targeted search:
```
grep -rn "chi(Q^5)=g=7\|chi(Q^5) = g\b\|χ(Q⁵) = g\b\|χ(Q^5) = g\b" .
```
Returns ZERO hits across the entire BST tree. PASS.

## Verdict: **PASS**

Sweep complete. WorkingPaper was already correct. One residual graph-data-layer offender fixed this session. Convention is now consistent across the codebase: **χ(Q⁵) = 6 = C_2** everywhere. The `g = 7` value is SO(7) embedding dimension, not topological Euler characteristic — and this distinction is now explicitly documented in the Poincaré paper.

## Recommendations for future

1. **Standing rule**: When writing about Q⁵ topology, use the disambiguation phrase "χ(Q⁵) = 6 = C_2 (g = 7 is the SO(7) embedding dim)" when first introducing the Euler characteristic in any new paper.
2. **CI onboarding note**: New CIs sometimes see g = 7 listed as a "Q⁵ invariant" because the embedding dim is 7. Add to onboarding: g is the SO(N) embedding parameter (N = n_C + rank + 2), not a topological invariant of Q⁵.
3. **Toy template**: When defining `chi_Q5` in a toy, prefer the form `chi_Q5 = C_2  # = 6, Euler characteristic of Q^5` to make the identity explicit at point-of-use.

— Keeper, K39, 2026-05-15
