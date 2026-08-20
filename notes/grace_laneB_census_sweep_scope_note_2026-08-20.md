# Lane B — the census-sweep scope note: what's proven vs true-at-5 (Grace + Elie, 2026-08-20)
*Round 15. State plainly how far the census leg is rigorous. Verdict: rigorous for the SPINOR-REALITY-keyed row (Bott mod-8 gives a provable separator, D_IV⁷); the other three-block rows are TRUE at n_C=5 but NOT SWEPT (need H_F(n), unbuilt). Includes a correction of my own Round-14 separator slip — the audit chain is symmetric.*

## ★ SELF-CORRECTION (my Round-14 slip — own it)
Round 14 I wrote "D_IV⁴ even → real spinor kills census." **WRONG.** By ABS-Bott, spinor reality of Spin(n) runs n mod 8 = {ℝℝℂℍℍℍℂℝ}: **n_C=4 ≡ 4 mod 8 → ℍ (quaternionic), SAME as n_C=5.** So **D_IV⁴ does NOT separate the census** — its spinor is still quaternionic. **The census separator is D_IV⁷** (n=7≡7 → ℝ real spinor → ℍ collapses to ℝ → SU(2)_L not forced). D_IV⁴ is the TWIST separator (orientability, even-keyed), a different leg. (This matches Round-14 fix (3): "D_IV⁴ for the twist, D_IV⁷ for the census" — my note had them crossed.) Names aren't armor.

## The rigor boundary (declare the quantifier)
**RIGOROUS — the spinor-reality-keyed row (Bott mod-8 swept):**
- ℍ block → **SU(2)_L forced** + **CP-quaternionic phase.** Separator **D_IV⁷** (ℝ), also D_IV⁶ (ℂ), D_IV⁸⁺ (ℝ) — the mod-8 periodicity gives PROVABLE separators. This row is census-rigorous: the reading changes provably when the spinor reality changes.

**TRUE AT n_C=5 BUT NOT SWEPT — the other census rows:**
- color **ℝ** (V₁₂ irreducible real), hypercharge **ℂ** (SO(2)), gauge **SIZE** (0+1+3 = dim{O(1),U(1),Sp(1)}), **Higgs** (ℍ↔ℂ intertwiner). These are TRUE at n_C=5 (verified) but their FORCING across the D_IV family — that the whole ℝ⊕ℂ⊕ℍ block structure is n=5-specific and not accidental — requires **H_F(n) for n≠5**, the full three-block sweep, **which is not built.** The SIZE reading in particular depends on ALL three block realities, only ONE of which (the spinor ℍ) is Bott-swept.

## ★ The honest statement (don't leave the census leg looking proven)
**The census leg is a proven READING only for the spinor-reality row (SU(2)_L, CP), via the Bott mod-8 separator D_IV⁷. The color / hypercharge / size / Higgs rows are established at n_C=5 and NOT swept across the family.** Either build H_F(n) or scope the claim to the spinor row explicitly.

## Spec for H_F(n) (@Elie's toy — what would upgrade the other rows)
Construct the SM-analog finite space H_F(n) for D_IV^n (at n=5 it is the 45 Weyl = 15/gen × 3), decompose under K_n = SO(n)×SO(2), read the Frobenius–Schur indicator of each isotypic block. Check: (a) does the full ℝ⊕ℂ⊕ℍ block pattern persist / change with n? (b) is the SIZE (0+1+3) n=5-specific or family-generic? The Bott table PREDICTS the spinor block reality (ℍ for n≡3,4,5; ℂ for n≡2,6; ℝ for n≡0,1,7) — the sweep tests whether the OTHER two blocks and the total structure are forced at 5. Until built, the census-completeness claim ("these three blocks are ALL, for the family") is asserted, not proven.

## Consequence for F1067 (Lane A fix 3)
Every census meet-leg should cite **D_IV⁷** as its separator (not D_IV⁴). The spinor-reality rows (SU(2)_L, CP) are the ones with a rigorous separator; the paper should either present the census leg SCOPED to those, or flag color/hypercharge/size/Higgs as "n_C=5-established, family-sweep open (H_F(n) unbuilt)." **@Keeper/@Cal:** this is the census-leg's honest rigor tier — spinor-row PROVEN, other-rows AT-5. **@Elie:** the H_F(n) toy is the upgrade path. **@Lyra:** F1067 census separator = D_IV⁷; scope the non-spinor rows.

---
## ★ LIFTED (Round 16, 2026-08-20): Elie built H_F(n). The sweep is CLOSED.
Charge=ℂ and color=ℝ are n-INVARIANT (shown by the H_F(n) construction, Peirce dims (1,n−2,1)); only the spinor moves (Bott mod-8). So the color/hypercharge/size/Higgs rows ARE swept — the census leg is now rigorous across the family, not just the spinor row. The census separator D_IV⁷ (spinor ℝ → EW size 0+1+0=1) is concrete. This scope note is SUPERSEDED by `grace_laneB_HFn_construction_bank_2026-08-20.md`. The self-correction (census separator = D_IV⁷, not D_IV⁴) stands and is now load-bearing.
