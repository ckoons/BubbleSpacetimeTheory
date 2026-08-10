# Grace — LANE A: V_cb as the Clebsch-Gordan off-diagonal of the one operator (mechanism + corrected + blind score)
*2026-08-09. Casey's redirect: mixing off-diagonals are Clebsch-Gordan, not radial — no radius to pick. Confirmed the frame, corrected my own error, armed the blind score.*

## The frame is right: V_cb ≠ the norm-ratio (the 1/√42 trap)
V_cb is the off-diagonal of the **diagonalized** Y = G^½·diag(w)·G^½, where G's off-diagonal **s = the SO(5) Clebsch-Gordan overlap** between the two modes (group theory, no radius). This is a genuinely different object from the norm-ratio √(w₂/w₃) = √(60/2520) = **1/√42 = 0.154** (the trap, overshoots obs 0.041 by 3.8×). The trap dresses a mass-norm ratio as an angle; the real mixing is the rotation that diagonalizes Y.

## ★ Correction I own (the number caught it)
I first said the diagonalization "gap-suppresses" the off-diagonal (V_cb ≈ s/gap). **Wrong** — I ran it: Y₁₂ = ab(w₂+w₃) rides the **large** weight w₃, so
**V_cb ≈ s·(w₂+w₃)/(2(w₃−w₂)) = 0.524·s** — *not* gap-suppressed. A clean CG s does NOT automatically give a tiny angle. Owned; the phantom-lesson guard did its job (run the number before confirming).

## Honest net (compute-don't-fit held)
- obs V_cb = 0.041 needs CG overlap **s ≈ 0.078**.
- Clean CG candidates (reported, NOT fit): s=1/c₃=1/13→V_cb=0.040 (−2%); 1/(2g)=1/14→0.038 (−9%); 1/g=1/7→0.075 (+83%); rank/g=2/7→0.151; n_C/N_max→0.019 (−53%).
- **No clean s trivially lands 0.041.** s = 1/c₃ = 1/(N_c²+rank²) = 1/13 is the closest (−2%), and c₃=13 is a real corpus number (sin²θ_W=3/13, θ₁₂=4/13). **But it is a CANDIDATE to CHECK, NOT banked** — I tried ~5 forms (look-elsewhere risk), and picking the s that lands 0.041 IS reverse-engineering the coefficient. The FORCED s is the SO(5) CG value Elie/Lyra compute from group theory; if their computation independently gives 1/13, it's real, else 1/13 was a coincidence.

## ★ Blind score (refined for the CG picture, armed)
When @Elie fires the one evaluation (V_cb + up-12 + PMNS from one diagonalization of Y):
1. **Gate 0** (down same-ν slice → {3,60,2520}=(N_c)_λ, V_us=1/√20) still first.
2. **V_cb PASS = the FORCED SO(5) CG coefficient** (computed from the group, not picked) is the s the diagonalization needs → V_cb ≈ 0.041, AND the SAME CG structure gives up-12 and the PMNS angles. The **1/√42 norm-ratio is RULED OUT** (it's the trap; if the evaluation returns 1/√42, it computed the wrong object).
3. **Derive-vs-imported:** DERIVED = s is a forced SO(5) CG coefficient (rational/algebraic, no free radius); IMPORTED = s picked to land 0.041 (e.g. me choosing 1/13). Report which.
4. **Discipline:** one operator, one diagonalization, all off-diagonals together; a single V_cb on a hand-picked s banks nothing. CP magnitude stays OFF.

## Status
No node (mechanism + blind score + owned correction). The frame (CG off-diagonal, not norm-ratio) is confirmed and 1/√42 is the trap; the forced CG coefficient is Elie/Lyra's to compute — my score is armed to fire blind on it. Cross-refs: F877 (Y=G^½diag(w)G^½), K1012 (the operator), grace_flavor_is_linear_algebra (the SVD frame), Cal §21 (CP branch). Nothing pushed.
