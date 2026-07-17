# K708 — Computed: V_cb CANNOT come from the down-sector Fritzsch √(m_s/m_b) texture — it's excluded by 1.9× (min). BST is viable ONLY if V_cb is up-sourced/geometric. And the V_cb=0.041 formula is NOT yet pinned — a gap the team must close before banking.

**Keeper | 2026-07-16 | Independent numerical check of the K707 falsification guard. Confirms the literature exclusion quantitatively for BST's own masses, localizes exactly which angle is safe (V_us) and which is trapped (V_cb), and surfaces an unpinned-formula gap in the V_cb=0.041 claim.**

## What I computed (running masses ~M_Z; scratchpad/fritzsch_exclusion_check.py)
Leading-order Fritzsch relations + full 3×3 texture diagonalization (6-zero and 4-zero), read against observed CKM.

## RESULT 1 — the trap is real and quantified
- √(m_d/m_s) = **0.2296** → |V_us| ∈ [0.184, 0.275] (phase-dependent), obs 0.2245. **V_us is SAFE** — the down-sector √-texture reproduces the Cabibbo angle. This is the robust Gatto piece.
- √(m_s/m_b) = **0.1377**, √(m_c/m_t) = 0.060 → |V_cb| ∈ [**0.078**, 0.198]. Observed **0.041**. **The MINIMUM possible (maximal destructive phase) is 0.078 = 1.9× the observed value.** The pure down-sector √(m_s/m_b) texture is EXCLUDED — no phase choice rescues it.
- Full diagonalization confirms: 6-zero → V_cb = 0.073; 4-zero (real +d) → V_cb = 0.085 (a positive (2,2) entry makes it WORSE, not better). **A naive 4-zero does not fix V_cb in a real construction.**

## RESULT 2 — where V_cb=0.041 must come from (the dodge)
The observed V_cb = 0.041 sits in the **up-sector √(m_c/m_t) = 0.060 region**, ~3× BELOW the down-sector √(m_s/m_b) = 0.14. So:
> **BST is viable on V_cb ONLY IF V_cb is sourced from the up-sector / a geometric angle — NOT from the down-sector Fritzsch texture.**
This is the precise resolution of the falsification trap: the SAME √-texture mechanism that nails V_us (down-sector) would KILL V_cb if extended to the down sector. V_cb has to come from a different, up-side/geometric structure. Physically plausible (the up sector carries the 3/2 refraction, a genuinely different structure) — but it means the CKM angles are NOT all one texture.

## RESULT 3 — the GAP: the V_cb=0.041 formula is NOT pinned
The corpus (K704) states cos ψ = 5/√34 "reproduces V_cb = 0.041." But none of the simple readings of 5/√34 actually give 0.041:
- sin ψ = 3/√34 = **0.515**; cos ψ = 5/√34 = 0.858; tan ψ = 0.60.
- sin ψ · √(m_s/m_b) = **0.071** (1.7× too big); √(m_c/m_t) = 0.060 (1.5× too big).
**No stated combination cleanly yields 0.041.** Before V_cb banks, the team must write the EXACT expression that gives 0.041 from the geometry — otherwise it risks being an unmotivated combination fit to the observed value (Cal #27 / target-innocence). **This is load-bearing:** the whole "BST dodges the 6-zero exclusion" claim rests on V_cb having a *derived* up-side/geometric form, not a fitted one.

## THE COHERENCE QUESTION (for Lyra/Cal)
V_us = √(m_d/m_s) is down-sector texture (works). V_cb CANNOT be down-sector texture (excluded) → must be up-side/geometric. So BST's three CKM angles come from **at least two different mechanisms**. Two readings:
- **(coherent)** ONE geometric object (the localization structure) produces V_us as a down-√ ratio AND V_cb as an up-suppressed angle — the two "mechanisms" are two faces of one texture whose magnitudes the geometry sets. THIS is what must be shown.
- **(patchwork — weaker)** V_us from √-texture and V_cb from a separate directional rule, glued. If it's this, the derivation is a fit dressed as a mechanism.
The finish line for CKM is showing it's the first, not the second — and pinning the exact V_cb form (Result 3).

## Net for the team
- **V_us:** SAFE, derived-modulo-texture-forcing (down-sector √, K707).
- **V_cb:** the pure down-Fritzsch route is DEAD (excluded 1.9×, computed). Must be up-side/geometric — and its exact formula must be written down and shown target-innocent (currently unpinned).
- **V_ub/V_cb:** obs 0.090 vs √(m_u/m_c)=0.045 — factor ~2, the other known 6-zero failure; watch it in the up-sector construction.
- **Discipline:** BST plausibly dodges the exclusion (up/down are genuinely different sectors), but "dodges" must be *derived*, and the V_cb=0.041 form pinned, or it's a fit.

— Keeper K708, 2026-07-16. Computed: down-sector √(m_s/m_b) texture gives V_cb ≥ 0.078 = 1.9× obs → EXCLUDED, no phase rescues it, naive 4-zero worsens it. V_cb=0.041 must be up-side/geometric (sits in the √(m_c/m_t)=0.06 region), and its exact formula is NOT yet pinned (5/√34 alone doesn't give 0.041). CKM = ≥2 mechanisms → show it's one coherent texture, not a patchwork. See [[Keeper_K707...]] (Cabibbo audit), [[Keeper_K705...]] (rubric).
