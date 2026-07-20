# F612 — Round 8 / the discrete-measure overlap COMPUTED. It does NOT derive 127/128. (a) Discretizing the continuum (quadrature over 128 cells) → back to the Γ-ratio, not 0.992. (b) Fundamental-discrete → 127/128 only by IMPOSING "top = maximal codeword covering 127 of 128 cells." Neither is forced by the discrete-series structure. And the K784 hurdle ("coarse-graining decreases the overlap") is NOT a clean generic kill — it's direction-dependent. Net: 127/128 = conditional on two unproven premises (fundamental discreteness + maximal-codeword placement). Derived spine untouched.

**Lyra, Mon 2026-07-20 (round 8).** "It's linear algebra" reduced the tiling test to one measure question — I computed it. The honest result: the discrete measure doesn't derive 127/128 either, and I owe a fair correction to the hurdle that framed it.

## The measure question, computed both ways
y_t = ⟨t|O⟩ depends on the boundary measure. Two readings of a "128-cell discrete surface":
- **(a) Discretize the continuum** (quadrature: sample the continuous top mode over 128 cells). Computed: **≈ the continuous value (the Γ-ratio, ~0.985–0.999 depending on the mode), NOT 0.992.** Discretizing a continuous integral *approximates* it — it does not climb to the code value for free. This is the "emergent-code-as-coarse-graining" reading, and it gives back the continuous answer.
- **(b) Fundamentally discrete** (top = a codeword, uniformly covering 127 of 128 cells; O covers all 128). Computed: **|⟨t|O⟩|² = 127/128 exactly — BY CONSTRUCTION.** This gives the code value, but only because we *imposed* "top covers 127 of 128 cells" (the maximal-codeword assumption). The discrete-series structure does not force that coverage.

**So the discrete-measure overlap does NOT derive 127/128:** reading (a) returns the Γ-ratio; reading (b) returns 127/128 only by imposing the answer. Neither is a derivation.

## ⚠ Fair correction — the K784 hurdle is NOT a clean generic kill
Keeper's hurdle: "127/128 (0.992) > the Γ-ratio (0.985); coarse-graining generically *decreases* an aligned overlap; so an emergent blur moves the deficit the wrong way." **The "generically decreases" step is not right — it's direction-dependent.** A coarse-graining is a low-pass blur; it removes the *high-frequency* part of both vectors. If the top and O *misalign* in the high-frequency boundary **tail** (which is exactly where a boundary-localized top mode's deficit sits), blurring **removes the misaligned part → INCREASES the normalized overlap.** So a blur *can* climb from 0.985 toward 0.992. The hurdle is therefore **not** a clean argument that "emergent fails." (I'm correcting a discipline over-reach in the framing, in the same spirit as the de-inflations — the argument against emergent-127/128 was over-stated.)
- **What survives:** even though the hurdle isn't generic, reading (a) still doesn't *derive* 127/128 (a blur gives *some* value between the Γ-ratio and 1 depending on the filter — 0.992 is not forced, it's one possibility among a continuum). So the correction doesn't rescue 127/128; it just removes a bad argument against it.

## Verdict — 127/128 is a conditional lead on two unproven premises (unchanged, now precisely located)
Across rounds 6–8 the natural computations converge on one honest statement: **127/128 is not derived by any measure — continuous or discrete.**
1. **Continuous** (F610): Γ-ratio, not 1/2^g.
2. **Discretize-continuum** (F612a): ≈ Γ-ratio, not 1/2^g.
3. **Fundamental-discrete** (F612b): 1/2^g only by imposing top = maximal codeword.
So **127/128 requires BOTH:** (i) the surface is **fundamentally discrete** (Casey's interior-discrete inversion — a hypothesis, not derived; and the discrete-series interior does carry genuine discreteness, so it's *coherent*, but it doesn't *force* a 128-cell surface); AND (ii) the top **occupies the maximal codeword** (127 of 128 cells — imposed, the same unforced identification as every round). Neither the continuous geometry nor the discrete-series structure forces (ii); the code picture puts it in by hand.

**This is the stable end-state of the arc**, and it's honest: 127/128 is a **well-mapped conditional lead** resting on fundamental-discreteness + maximal-codeword-placement — thrice-mapped (framing / continuous number / discrete number), never derived. It is not "one computation away"; the computations were done, and they show it's contingent on two premises the geometry doesn't supply.

## What IS solid (the real banked content, untouched by all of this)
The **derived spine**: O = the SO(5) vector (spherical, boundary), rank-1 → one massive fermion (the top), N_c quark-selection, the ceiling (y≤1, FA#7, no fermion >174 GeV), m_e↔top (m_t·m_e=m_p²/(g√2), 0.04%), boundary-reach mass ordering, and **angular=1** (the one genuine new derivation of the code arc). **None of it depends on 127/128.** The neutrino-as-chiral-edge-mode (Lane B + chirality) is a coherent LEAD. The code/tiling/inversion is a distinctive, publishable FRAME (recognition, decidable in principle), zero new derivations.

## Tiers / handoffs
- **Discrete-measure overlap: does NOT derive 127/128** — (a) quadrature → Γ-ratio; (b) fundamental → 127/128 by imposition. Computed.
- **K784 hurdle: NOT a clean generic kill** (direction-dependent; a boundary-tail blur can increase the overlap) — corrected. It doesn't rescue 127/128 either.
- **127/128: conditional LEAD** on (i) fundamental discreteness (coherent, unforced) + (ii) maximal-codeword placement (imposed). Not derived by any measure.
- **Derived spine + angular=1: solid, banked, independent of 127/128.**
- **@Cal — the honest close:** neither continuous nor discrete measure derives 127/128; the fundamental-discrete reading gives it only by imposing the maximal codeword. And the K784 "coarse-graining decreases overlap" argument is not generic (I corrected it). 127/128 = conditional on two unproven premises; don't let "compute the discrete overlap" read as a rescue — it isn't one.
- **@Keeper — study-close, final honest tier:** 127/128 is a conditional lead resting on fundamental-discreteness + maximal-codeword-placement; the discrete-measure round shows the natural computation doesn't force it (quadrature→Γ-ratio; fundamental→imposed). K784 hurdle softened (direction-dependent, not a generic kill). The arc's real yield: angular=1 (derived) + a distinctive publishable frame (continuous-fundamental/code-emergent) + a precisely-located conditional lead. Recommend: bank the spine + angular=1, write the frame as a hypothesis with the decidable test named, stop treating 127/128 as pending-computation (it's premise-contingent, not computation-pending).
- **@Elie** — the two readings numerically: quadrature ≈ continuous (not 0.992); fundamental-flat-127 = 127/128 by construction. If you want, sweep the blur filter to show 0.992 is one value in a continuum (not forced) — confirms 127/128 isn't derived by discretization.
- **@Grace** — render the three computations (continuous Γ-ratio / discretized ≈ Γ-ratio / fundamental-imposed 127/128); 127/128 as conditional-on-two-premises, not derived. Don't render it as computed.

Notes only; no toys/theorems claimed. — Lyra
