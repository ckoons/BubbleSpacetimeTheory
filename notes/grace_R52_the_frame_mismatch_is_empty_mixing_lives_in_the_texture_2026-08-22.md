# R52 — BANKING the headline, and testing the round's premise: the {1,α,α²}↔{1,3,5} frame mismatch is EMPTY (Grace, Round 52, 2026-08-22)

*Assignment: bank the constructive half, pin the up-sector frame from T2547's top-saturation ladder, and size the rank-1 breaking that sets V_cb. **I banked the headline. The premise did not survive the reconnect — and the corpus already said so.***

## PART 1 — ★ THE HEADLINE, BANKED (as asked)
> **FLAVOR-UNIVERSALITY IS THE PARTIAL-ISOMETRY CONDITION.**
> CKM unitarity is a theorem of three-generation field redefinition. Writing any mixing ansatz as V = A†JB with A, B orthonormal bases of the up and down 3-spaces: **V is unitary ⟺ J restricted to the down 3-space is a partial isometry ⟺ the three singular values of P_U J|_D are equal ⟺ J couples all three generations with equal strength — i.e. the weak current is flavor-universal**, which gauge invariance forces.
> **⟹ The gate I built is not an external hurdle. It is the statement "the weak coupling is universal," in operator form. Any ansatz whose current is not flavor-universal cannot produce a unitary CKM — and CKM = U_up†·U_down is the forced survivor, because a flavor-universal current is the identity on generation space and two bases of one space always give a unitary comparison.**
**Tier proposed: DERIVED (structural identity — a two-line proof plus a gauge-theory fact; target-innocent, no number involved).** Gates: `play/gate_partial_isometry_intrinsic.py` (Level 1, U-independent), `play/gate_partial_isometry_mixing.py` (Level 2). @Keeper to tier.

## PART 2 — the premise, tested. **The frame mismatch as posed is EMPTY.**
The round asks for V_cb/V_ub as the mismatch of **up = {1, α, α²}** (T2515/T2547 top-saturation) against **down = {1, 3, 5} → 1:20:840** (T2513/T2529 FK bulk). Three tests:

**TEST 1 — the CKM is identically independent of both mass spectra.**
V = U_up†U_down depends **only on the eigenBASES**, never on the eigenVALUES. Changing both spectra arbitrarily (α² → 10⁻⁹, 840 → 10⁶) while holding the eigenbases fixed changes V by **exactly 0.000e+00**.
> **{1, α, α²} and {1, 20, 840} are EIGENVALUE data. They cannot enter the CKM. Not "weakly" — identically.**

**TEST 2 — the two eigenBASES the corpus actually banks COMMUTE.**
The down FK operator is diagonal in the single-row **degree** basis. Top-saturation is **y = exp(−geodesic distance to the Shilov boundary)** (T2515, "Grace unification") — a **radial** function, therefore **K-invariant**, therefore diagonal in that **same** K-type basis. Two operators diagonal in a common basis commute: **‖[M_up, M_down]‖ = 0.000e+00 ⟹ CKM = IDENTITY. Zero mixing.**
> This is **Casey's K1187 firing on the actual banked operators**: *if the two mass matrices commute, nothing mixes.*

**★ Where the premise slipped (precisely, and it is a small step):** **T2547 leg (A) says the two MECHANISMS are different (boundary vs bulk) — which is what forces CP to be non-zero. It does not say the two EIGENBASES are known and misaligned.** "Different mechanism" ≠ "known relative orientation." The first is banked; the second is what CKM needs and the corpus does not have it. **And T2547 says so itself:** *"three independent J-runs … ~300× spread = **MAGNITUDE stays OFF (reverse-fit); only EXISTENCE banks**."* The route was already marked magnitude-off, by this exact theorem, on 2026-08-09.

## PART 3 — ★ so where DOES the mixing live? The TEXTURE, and the open piece is ONE ANGLE
Mixing lives entirely in the **off-diagonal (non-K-invariant) TEXTURE**, never in the spectra. Status:
- **Down texture: BANKED.** The ℂ³ SVD texture zero → Gatto → **V_us = 1/√20, Derived (T2530)**, frame-independent.
- **Up texture: ABSENT.** The corpus has an up-sector *spectrum* ({1,α,α²}) and **no up-sector texture at all.** ⟹ *"Pin the up-sector frame"* = **"derive the up-sector texture."** That is a different and well-posed target, and it is the real open item — exactly K995, as T2530 flagged.

**And rank-1 (T2519) says how small the open piece is.** With M_u, M_d rank-1: H_u = m_t²|a⟩⟨a|, H_d = m_b²|c⟩⟨c|. Verified over 400 arbitrary choices of the degenerate 1-2 rotations:

| quantity | status |
|---|---|
| **\|V_tb\| = \|⟨a\|c⟩\|** | **DETERMINED** (spread 0.00e+00) |
| **\|V_ub\|² + \|V_cb\|² = sin²θ** | **DETERMINED** (spread 0.00e+00) |
| V_ub, V_cb **individually** | free |
| the whole **1-2 block** | free (the rank-1 kernels are degenerate) |

> ★ **The open half of the CKM is ONE ANGLE θ — the misalignment between the top direction and the bottom direction in generation space.** Target it must hit (stated as **target, never as input**): |V_ub|²+|V_cb|² = 0.001763 ⟹ **sin θ = 0.04199, θ = 2.406°.**

★ **And the complementarity is exact:** rank-1 determines the **third row/column** and leaves the **1-2 block** free — while BST derives **V_us (the 1-2 block)** from the **down texture zero**, a structurally different source. **The two halves of the CKM come from two different places, and BST already holds one of them.** That is why "the frontier is one computation wide" is right — it is **one angle** wide.

## PART 4 — a conditional reading, with its assumption named
Adding the corpus's banked 1-2 rotations (down = Gatto, 12.604°; up = √(m_u/m_c) = 0.04, T2530's own parenthetical) and putting the rank-1 misalignment in the 2-3 plane — **that placement is an ASSUMPTION, not forced, and I flag it as the load-bearing one** — real (CP-free) rotations give
> **V_ub/V_cb = √(m_u/m_c) = 0.0400, exactly and θ-independently** (checked at θ = 1°, 2°, 2.406°, 3°) **vs observed 0.0892 — short by 2.2×.**
That is the **classic Fritzsch relation**, and its ~2× shortfall is a **known** failure of Fritzsch-type textures. **So BST's banked structure lands on a real, named, already-falsified texture relation.** Honest consequences: (i) it is content, not decoration — it *can* fail and it *does*; (ii) the missing factor sits exactly where **CP** lives, and BST has CP at **existence-only** (T2547) — so the split of θ into V_ub vs V_cb is open **precisely as far as the CP magnitude is open**, which is a consistent story rather than a new problem. **No fitting was done and none should be:** θ was set *from* the observed leakage, so |V_cb| ≈ 0.042 in that table is a **definition, not a prediction.** I state that plainly so nobody quotes it as a hit.

## Handoffs
- **@Elie** — before spending the compute: **the {1,α,α²}↔{1,3,5} mismatch cannot produce V_cb** (Tests 1–2, both exactly zero). The live target is the **up-sector TEXTURE**, and specifically **one angle θ** with target 2.406°. Also: rank-1 gives you |V_ub|²+|V_cb|² as a **single** observable — pre-register against **that**, not against V_cb alone; it is the combination the geometry actually determines.
- **@Keeper** — (i) tier the headline (Part 1). (ii) **T2547 is being read one step past what it says** — "different mechanisms" (banked, forces CP existence) is being used as "known misaligned eigenbases" (not banked). T2547's own "magnitude stays OFF, 300× spread" is the guard. A one-line scope note on T2547 would prevent the re-read. (iii) The Fritzsch reading (Part 4) is **conditional on the 2-3 placement** — do not bank it.
- **@Cal** — Part 4 is exactly your can-fail discipline: a relation that **can** fail and **does** (2.2× short), reported with its assumption named and with the circular entry (|V_cb|) flagged as circular by me before anyone quotes it.
- **@Lyra** — your H_{ν_W} atlas rail matters more after this, not less: **the addresses are the texture question**, and the texture is the whole mixing. The spectra are settled and inert.

*Scripts: scratchpad `r52_frame.py`. Nothing pushed. CP existence-only. — Grace, R52, 2026-08-22*
