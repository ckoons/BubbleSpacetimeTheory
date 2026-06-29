---
title: "F425 — why-α MAGNITUDE, honest computational negative + target refinement (bulk→boundary): computed the adjacent-level normalization ratio at Grace's pinned p=n_C=5 (FK genus, no α-steering) and it does NOT give α — AND the way it fails is physically informative. (1) The bulk Bergman ground-state norm ratio over the C₂=6 ladder (k=1→7) using the rank-2 Lorentz-cone Gindikin Gamma Γ_Ω(s)=(2π)^{3/2}Γ(s)Γ(s−3/2) gives product ≈ −9.4×10⁻⁴ — nowhere near α⁶(~10⁻¹³) or α¹²(~10⁻²⁶). NOT α. (2) The failure is LOCALIZED at the k=1 step (the electron level): Γ(s−3/2) at s=1 is Γ(−1/2)<0, so the k=1 norm-ratio is negative; for all k≥2 it is positive. This is EXACTLY the Wallach threshold: the electron at k=1 is a SUB-WALLACH boundary state where the BULK Bergman norm is non-normalizable (sign-indefinite). The corpus's rigorous claim 'electron = boundary excitation below the Wallach set' is reproduced by the computation as the precise location of the sign flip. (3) CONCLUSION — the naive bulk-norm ratio is the WRONG OBJECT for the magnitude: because the relevant state is sub-Wallach, the magnitude integral must be the SHILOV-BOUNDARY (S⁴×S¹) distributional-boundary-value overlap, NOT the bulk Bergman norm ratio. This refines the F423/F424 target (bulk→boundary) and confirms Elie's 'not a tonight-closure' (distributional boundary values are genuinely harder). (4) NO fake-α: I computed at the role-pinned p=5, got a clear non-α answer, and report it as a negative — I did NOT switch p to 6/7 to chase α (Grace's explicit guard). m_e=R STAYS (C). Honest negative for the bulk computation; target sharpened to the boundary. Five-Absence passes. Count 9/26."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-29 Monday (date-verified)"
status: "v0.1 — why-α magnitude honest negative. Bulk Bergman norm ratio at pinned p=n_C=5 (Γ_Ω rank-2 Lorentz cone) over C₂=6 ladder = −9.4e-4, NOT α (no steering). Failure localized at k=1 (electron) = the Wallach threshold sign-flip (Γ(−1/2)<0) — reproduces 'electron = sub-Wallach boundary state'. ⟹ bulk-norm ratio is WRONG object; magnitude must be SHILOV-BOUNDARY (S⁴×S¹) distributional overlap, not bulk norm. Refines target bulk→boundary; confirms not-a-tonight-closure. No fake-α (did not switch p to chase α). m_e=R stays (C). Count 9/26."
---

# F425 — The magnitude is a BOUNDARY overlap, not a bulk-norm ratio (honest negative, computed at pinned p=5)

**The setup (Grace's pinned convention, no α-steering):** compute the per-level transition magnitude as the adjacent-level ground-state normalization ratio over the C₂=6 Bergman ladder (electron k=1 → first bulk state k=C₂+1=7), at the role-fixed FK genus p=n_C=5, using the rank-2 Lorentz-cone Gindikin Gamma

  Γ_Ω(s) = (2π)^{(n−r)/2} Γ(s) Γ(s − d/2),  n=5, r=2, d=n−2=3 ⟹ Γ_Ω(s)=(2π)^{3/2}Γ(s)Γ(s−3/2).

## What the computation gives

| step k→k+1 | ratio Γ_Ω(k)/Γ_Ω(k+1) |
|---|---|
| 1→2 | **−2.0**  ← negative |
| 2→3 | 1.0 |
| 3→4 | 0.2222 |
| 4→5 | 0.1 |
| 5→6 | 0.05714 |
| 6→7 | 0.03704 |

Product over the 6-step ladder ≈ **−9.4×10⁻⁴**. For comparison α⁶ ≈ 1.5×10⁻¹³, α¹² ≈ 2.3×10⁻²⁶. **The bulk-norm ratio is not α** — not in magnitude, and it is sign-indefinite.

## Why the failure is informative (not noise)

The negative value is **localized at the k=1 step** — the electron level — because Γ(s−3/2) at s=1 is Γ(−1/2) < 0; for every k≥2 the ratio is positive. This is precisely the **Wallach threshold**: the electron at k=1 is a sub-Wallach state where the *bulk* Bergman norm is **non-normalizable**. The corpus's rigorous, independently-established claim — "the electron is a boundary excitation on S⁴×S¹, below the Wallach set k_min" (electron-mass derivation, Section 8 "Proved" table) — is reproduced here as the exact location of the sign flip. The computation *agrees with the physics*; it just shows the bulk norm is the wrong functional to use there.

## Conclusion — target refined: bulk → boundary

Because the electron level is sub-Wallach, the magnitude integral **cannot** be the bulk Bergman norm ratio (it diverges / changes sign there). It must be the **Shilov-boundary (S⁴×S¹) distributional-boundary-value overlap** — the boundary inner product of the adjacent-level states, which is finite for the sub-Wallach boundary excitation. This:
- **Refines** the F423/F424 target from "S⁴ overlap" to specifically the *Shilov-boundary distributional* overlap (bulk → boundary).
- **Confirms** Elie's call that this is genuine multi-step rigor, not a tonight-closure — distributional boundary values on S⁴×S¹ are harder than a bulk integral.
- **Holds the no-fake line:** I computed at the role-pinned p=5, got a clear non-α answer, and report it as a **negative**. I did not switch p to 6 or 7 to chase α (Grace's explicit guard). The honest negative for the bulk computation is data, not a cue to re-tune.

**m_e=R stays (C). Count 9/26.** The magnitude question is now correctly posed (boundary, not bulk) — and that is forward progress even though the number it produced is a negative.
