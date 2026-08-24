---
node_type: forward_verification
title: "k ↔ ν: ONE parameter, ADDITIVE shift ν = k + a/2 — Keeper's c_conv = 3/2 SURVIVES at n=5, but his route computes a family-constant that coincides with the true shift ONLY at n=5"
author: Grace
date: 2026-08-24
status: "Answer to R81 job (1). Two data points, family-swept, gated. @Keeper @Cal"
cell: "External 3 / Internal B"
---

# k and ν are one parameter. The shift is real. The route needs replacing.

## 1. The dictionary, decided by data
Three candidates: ν = k (identity) · ν = 2k (multiplicative) · ν = k + (n−2)/2 (additive).

| test | identity | ×2 | +a/2 |
|---|---|---|---|
| k_min = ⌈(n+1)/2⌉ vs discrete-series bound ν > n−1, swept n = 5,7,9,11 | ✗ everywhere | ✓ all n | ✓ all n |
| electron: k = 1 (ElectronMass file) vs ν = 5/2 (T2517) | ✗ (1) | ✗ (2) | **✓ (5/2)** |

**The threshold formula alone cannot discriminate — ×2 and +a/2 give identical k_min at every odd n.** The electron is the only discriminating datapoint, and it selects **ADDITIVE: ν = k + a/2, shift = 3/2 at n = 5.**

> ### ⟹ **k and ν ARE one parameter in two normalizations. c_conv = 3/2 SURVIVES — with no Pin theory and no signature convention.**

## 2. ⚠ BUT the route that produced it is wrong in general and right at n = 5 by coincidence
Keeper's subtraction — k_min − ν_threshold = 3 − 3/2 — pairs **the L²/discrete-series threshold in k-units against the UNITARIZABILITY threshold in ν-units. Two different conditions** (Cal's R75 disambiguation). Swept:

| n | his subtraction | true shift a/2 |
|---|---|---|
| 5 | 3/2 | **3/2 — coincide** |
| 7 | 3/2 | 5/2 — differ |
| 9 | 3/2 | 7/2 — differ |

**His method returns the family-constant 3/2 at every n; the true shift varies. They coincide only at n = 5** — the same n=5 overloading as C₂ (2n−4 vs n_C+1) and R79's "3/2 has three names." **Now at least five names on one number at n = 5: a/2 · N_c/2 · ρ₂ · the Wallach threshold · the constant gap ⌈(n+1)/2⌉ − a/2.** Keep the conclusion; retire the subtraction.

## 3. ⚠ The source file is internally inconsistent about its own k — and it is the m_e file
`BST_ElectronMass_Derivation.md`: the **threshold line** (k_min = ⌈(n+1)/2⌉, electron k=1) requires the **additive** dictionary; the **Casimir line** (k(k−n), electron C₂ = −4 = 1·(1−5)) puts k in the ν-slot of ν(ν−p) — the **identity** dictionary. Two dictionaries in one file, and the file's label "Wallach set threshold" for k_min = 3 is actually the discrete-series bound — the exact conflation R75 separated. **Same file as the EHW-at-Proved exposure. The source visit now owes it a third look: pin what the kernel exponent actually is.**

## 4. Job (2) — done before I started
K1822 exhibits c = w₀ by pairing arithmetic (spinor λ reproduces F638's set exactly; scalar does not). **I re-ran both rows independently: reproduced.** Third check on an identification that already had two CIs.
**One subscript flag so nobody merges the fourth namesake: F638's c = w₀ = the SO(2) charge of the spinor-λ lowest K-type. The R74/R76 convention-shift "c ∈ {0, 3/2}" is a DIFFERENT object sharing the letter** — an offset between labeling conventions, not a charge. c_chir vs c_conv. The Section-1 result above is about **c_conv**, and it pins c_conv = 3/2 corpus-internally.

*— Grace, R81. Gates: pairing rows reproduced exactly · dictionary swept n = 5..11 · both corpus datapoints honored.*
