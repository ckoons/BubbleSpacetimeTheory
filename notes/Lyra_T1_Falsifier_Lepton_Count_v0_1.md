---
title: "Falsifier T1 design v0.1 — lepton-sector COUNT (24 components) from canonical-basis dim 4 × SU(2)_L doublet × 3 generations (with Cal, Keeper Saturday plan P4.5 extension). Forced YES/NO via standard QG computation: dim V_(1/2,1/2) of U_q(B_2) = 4 (Dirac 4-spinor); SM observed 24 lepton components matches substrate prediction (Dirac); falsifier triggers on 4th generation, 0νββ (Majorana), non-doublet structures, or SUSY partners."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 15:10 EDT"
status: "FALSIFIER DESIGN T1 v0.1 (Keeper Saturday plan P4.5 extension; co-design with Cal). Concrete quantitative test of the keystone bet: the canonical basis dim at V_(1/2,1/2) of U_q(B_2) = 4 (rigorous QG), and the substrate predicts 24 lepton components total (4 × 2 doublet × 3 generations) — matching observed SM (with Dirac neutrinos per F5). Falsifier triggers on multiple positive detections of forbidden configurations."
---

# Falsifier T1 — lepton-sector count from canonical-basis dim

## 0. The design intent

Keeper requested a sharp QUANTITATIVE falsifier of the keystone bet — beyond P4.5's PMNS angle channel (F1) — that compares the dim of the canonical basis at V_(1/2,1/2) against pinned-a-priori SM counts, computable via standard quantum-group theory with no dictionary-bet leakage in the QG step.

## 1. The QG-rigorous input (no dictionary leakage)

**Canonical basis of V_(1/2,1/2) of U_q(B_2) at q=2**:
- Standard Lusztig-Kashiwara canonical basis on the spinor module.
- The spinor module of U_q(B_2) at any q is the 4-dimensional fundamental rep (the Dirac 4-spinor).
- **dim = 4** (Weyl dim formula: (a-b+1)(a+b+2)(2a+3)(2b+1)/6 at (a,b)=(1/2,1/2) gives 4).
- The 4 basis elements correspond to the 4 spinor weights (±1/2, ±1/2) of B_2.

This is **rigorous representation theory**, no dictionary bet involved.

## 2. The substrate prediction (with dictionary inputs)

The keystone bet says: K-types ARE particles. The dictionary places the lepton at V_(1/2,1/2) (4 components). The physical lepton sector also has:
- **SU(2)_L doublet** structure (electroweak): per generation, leptons come as (ν, e) doublet → factor of 2.
  - Justification: L2 derived the Shilov stabilizer SO(4) = SU(2)_L × SU(2)_R; SU(2)_L organizes the doublet.
- **3 generations** (Route II of #414): per dictionary, generations = h^∨ = N_c = 3.

So the substrate-predicted lepton-sector count:

  **N_lepton = (dim V_(1/2,1/2)) × (doublet factor) × (generation count) = 4 × 2 × 3 = 24 components**

This includes particles + antiparticles + chiralities + generations, with Dirac neutrinos (per F5 prediction).

## 3. The SM observed count

With Dirac neutrinos (substrate prediction per F5):
- Per generation: 1 charged lepton (Dirac, 4 components: ψ_L, ψ_R, ψ̄_L, ψ̄_R) + 1 neutrino (Dirac, 4 components) = 8 lepton components.
- 3 generations × 8 = **24 lepton components total**.

**MATCHES substrate prediction = 24.**

With Majorana neutrinos (alternative scenario):
- Per generation: charged lepton (4 components) + neutrino (2 components: self-conjugate) = 6 lepton components.
- 3 generations × 6 = **12 lepton components total**.
- This would NOT match substrate's 24 prediction.

## 4. The falsifier T1 — explicit YES/NO

**Current status: YES (CONFIRMED, modulo neutrino Dirac/Majorana question)**

**Triggers (falsifier NO):**

| Observation | Substrate predicted | If observed |
|---|---|---|
| **4th generation discovered** | 3 generations × 8 = 24 | 4 × 8 = 32 (8 over substrate; CONTRADICTS) |
| **0νββ observed → Majorana neutrinos** | Dirac, 24 components | Majorana, 12 components (substrate Dirac assumption fails) |
| **Non-doublet lepton multiplet (e.g., triplet)** | 2-doublet → 24 | triplet → extra components → falsifies SU(2)_L organization |
| **SUSY lepton partners** | 24 components (no SUSY per F5) | 48 components (doubled) — refutes F5 + T1 |
| **K-type beyond V_(1/2,1/2) hosts a charged lepton** | dim 4 fits | extra K-type → extra components → falsifies K-type-as-particle mapping |

Any single positive observation in the right column → T1 fails → keystone bet challenged.

## 5. CD caveats (Cal #27 honest framing)

The QG dim=4 step is RIGOROUS (Weyl formula, no dictionary). The 24 count multiplies in TWO dictionary outputs:
- Doublet factor (2) — from L2 Shilov stabilizer SO(4) → SU(2)_L (dictionary structural).
- Generation factor (3) — from route II h^∨ = N_c = 3 (dictionary mechanism, currently open with burden).

So:
- **Cleanest pure-QG falsifier**: dim 4 (per K-type V_(1/2,1/2)) MUST match observed 4-component Dirac structure of ONE lepton (charged or neutrino) — verified ✓.
- **Combined falsifier**: 24 = 4 × 2 × 3 = total lepton component count — multiplies dictionary outputs; falsification on this channel could indicate either keystone failure OR dictionary-mechanism failure (need to disambiguate).

Per Cal #27: state explicitly which level (per-K-type dim 4 = pure QG; total 24 = dictionary-combined).

## 6. Honest scope + tier

**RIGOROUS (QG, no dictionary bet)**:
- dim V_(1/2,1/2) of U_q(B_2) at q=2 = 4 (Weyl formula).
- The Dirac 4-spinor structure matches this dim.

**DICTIONARY-DEPENDENT**:
- doublet factor 2 from L2 (Shilov stabilizer).
- generation count 3 from route II.
- 24 total prediction.

**FALSIFIER CHANNELS (T1)**:
- Per-K-type (pure QG): dim 4 = observed Dirac-spinor structure ✓.
- Total (dictionary-combined): 24 = observed lepton components (Dirac scenario) ✓.
- NO triggers: 4th generation; 0νββ; non-doublet; SUSY partners; extra-K-type leptons.

**Cal #27 / honesty**: T1 is a SHARP quantitative falsifier — but with explicit CD layering (pure-QG core + dictionary-multiplied total). The "24 = observed lepton count" match is genuine but multiplies in dictionary outputs; the cleanest pure-QG falsifier is the per-K-type dim 4 matching Dirac-spinor structure. Both layers MATCH currently; falsifier is LIVE for multiple channels.

**Co-design with Cal**: this v0.1 frames the test; Cal's input — pre-write referee questions; identify additional disambiguation steps; sharpen the CD layering — would advance it to v0.2.

**Routed**: → Cal: cold-read this v0.1 falsifier design; sharpen the dictionary-leakage layering; pre-write referee questions on the YES/NO channels. → Casey: T1 + F5 together (Majorana 0νββ + 4th-generation absence) are the cleanest near-term tests of the keystone bet — both have explicit experimental programs (LEGEND-1000, nEXO; HL-LHC). → me: T1 closes the falsifier suite; continuing to EOD prep.

— Lyra, Falsifier T1 v0.1 — lepton-sector count from canonical-basis dim. RIGOROUS (QG): dim V_(1/2,1/2) = 4 (Dirac 4-spinor). DICTIONARY-COMBINED: 24 = 4 × 2 doublet × 3 generations matches observed Dirac SM. NO triggers: 4th generation, 0νββ→Majorana, non-doublet lepton, SUSY partners, extra-K-type leptons. Pure-QG dim 4 matches observed Dirac-spinor structure ✓ — cleanest layer. Combined 24-count match also ✓ — dictionary-layered. Currently the YES-match holds at both layers; falsifier LIVE.
