---
title: "Grace — 132 Option A Excluded Items: Sample Review + Recommendation"
author: "Grace (Claude 4.7)"
date: "2026-05-16 01:40 EDT (post-burn-window phase 1)"
status: "Recommendation pending Casey decision"
out_of: "Casey directive 23:35 EDT: 108 Option A excluded → individual review"
---

# 132 Option A Excluded Items: Sample Review + Recommendation

## Background

Today's Option A wholesale revert (D→S) on auto_+structural+D items ≥2% precision had two exclusion rules:
1. Items with non-default theorem field (mechanism citation present) — 0 found
2. Items with existing `toy` reference (potentially real mechanisms) — 108 found

Keeper's instructed action: "Individual review, 10-15 min each. Most should promote to D once the mechanism is verified or reclassify to S."

**Current state**: 132 auto_+structural+D items with toy refs (rose from 108 because Elie/Lyra registered more entries since the original revert).

## Sample inspection (3 items reviewed)

### Item 1: `auto_2D_Ising_beta__1_rank_N_c__1_8`
- Claim: 2D Ising β exponent = 1/8 = 1/rank^N_c
- Precision: EXACT
- Toy: 1841 (`play/toy_1841_ising_2d_exponents.py`)
- **Toy 1841 docstring**: "Map all 6 exponents to BST integer expressions. Verify all 4 scaling relations." (Grace overnight observation, "they look like BST fractions").
- **Mechanism analysis**: 2D Ising critical exponents are derived by Onsager (1944) from the 2D Ising universality class via conformal field theory. The values (1/8, 7/4, 15, ...) are CFT results, NOT derived from D_IV⁵. Toy 1841 verifies BST integer combinations *match* the Onsager values — numerical identification, not derivation.
- **Verdict**: structural identification → S-tier appropriate.

### Item 2: `auto_Gottfried_sum__1_N_c__1_3`
- Claim: Gottfried sum = 1/3 = 1/N_c
- Precision: EXACT
- Toy: 1860
- **Mechanism analysis**: The Gottfried sum rule (1/3) follows from isospin symmetry and the parton-model expectation that valence quarks share momentum equally among N_c = 3 colors. The factor of 3 in the rule IS the QCD color number. BST has N_c = 3 from D_IV⁵, so the chain is real: D_IV⁵ → N_c = 3 → Gottfried sum = 1/N_c = 1/3.
- **Verdict**: D-tier defensible — N_c IS the load-bearing BST integer, and Gottfried sum legitimately equals 1/N_c via parton model.

### Item 3: `auto_2D_Ising_CFT_central_charge_c__1_rank`
- Claim: 2D Ising CFT central charge c = 1/2 = 1/rank
- Precision: EXACT
- Toy: 1841
- **Mechanism analysis**: 2D Ising c = 1/2 is a CFT result, derived from the chiral algebra of the Ising model. The "1/2" is the conformal central charge, not BST rank. Numerical match: 1/2 = 1/rank, but no mechanism connecting Ising CFT to D_IV⁵ rank.
- **Verdict**: structural identification → S-tier appropriate.

## Pattern

Inspection of 3 representative items: 2 should reclassify (S-tier), 1 is genuinely D-tier (Gottfried sum where N_c IS the load-bearing BST integer).

Extrapolating to the 132 set: **probably 70-90% are structural identifications (S-tier appropriate), 10-30% have genuine BST-derivative mechanism (keep D-tier)**.

## Why this is hard to bulk-process

The discriminator between "identification" and "derivation" is whether **the BST integer in the formula IS the mechanism-load-bearing quantity from D_IV⁵**, or just a coincidental factorization.

- `1/N_c` for Gottfried sum → N_c IS QCD color → BST D_IV⁵ → load-bearing. **Real.**
- `1/rank^N_c = 1/8` for 2D Ising β → 2D Ising β IS 1/8 by Onsager CFT, completely independent of D_IV⁵. Just happens to equal 1/2³. **Coincidence.**

Without reading each toy file and understanding the physics behind each external constant, I can't auto-classify. The 132 items split unevenly by domain:

| Domain | Count | Likely pattern |
|--------|-------|----------------|
| statistical_mechanics (Ising etc.) | ~20 | mostly structural identification (CFT exponents) |
| particle_physics | ~30 | mixed — color/parton items may be real; loop coefficients usually structural |
| condensed_matter | ~25 | mostly material-specific structural |
| fluid_dynamics (Kolmogorov) | ~10 | structural (turbulence universality) |
| biology | ~10 | mostly structural (codon, enzyme classes) |
| nuclear_physics | ~10 | mixed |
| other | ~27 | varied |

## Recommendation to Casey

Three options:

**Option A2 (RECOMMENDED): Stratified sweep with domain heuristics**
- Particle physics items where claim involves N_c or color factor → keep D (real mechanism)
- Statistical mechanics CFT exponents → reclassify S (external mechanism)
- Condensed matter material-specific → reclassify S
- Fluid dynamics turbulence → reclassify S
- Biology codon/enzyme counts → reclassify S
- Nuclear binding terms → individually review (mixed)

Estimated outcome: ~30 stay D, ~100 reclassify S. D-tier 79.2% → ~76.7%. Cleaner.

**Option B: Status quo (no action)**
Leave the 132 at D-tier; they're "structural identifications honestly tagged" and Casey already approved the Option A boundary. Headline 79.2% stands.

**Option C: Wholesale revert all 132**
Same as original Option A logic — auto_+structural is incompatible with D-tier by team convention. D-tier → ~76.0%. Most aggressive cleanup.

## My recommendation: Option A2 (stratified)

This honors the team's tier convention while preserving the items that genuinely DO have BST-mechanism load-bearing on color/parton/Bergman quantities. Implementation is ~1h of domain-by-domain review.

Casey decides. I'll execute whichever path he picks.

— Grace, 01:40 EDT
