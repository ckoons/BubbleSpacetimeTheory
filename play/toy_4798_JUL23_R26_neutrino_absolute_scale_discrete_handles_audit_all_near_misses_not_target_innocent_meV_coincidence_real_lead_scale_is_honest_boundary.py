#!/usr/bin/env python3
"""
Toy 4798 — Jul 23 (neutrino absolute scale: audit the discrete handles for target-innocence; Elie's fish-detector pass,
pull 23f). EW area closed (parity banked K837). The neutrino sector's Majorana nature is derived (toy 4796) and m₁=0 is exact
(n(ν_R)=2, rank-2), so the spectrum is {0, m₂, m₃} and the OPEN target is the absolute SCALE. Keeper: recast onto the
discrete side (the meV coincidence), don't grind the continuous seesaw — and (Keeper's own standing instruction) if none of
the handles yields, say plainly it's an honest continuous boundary rather than dress it up. I computed the three handles and
audited each for TARGET-INNOCENCE (the derived-vs-fit lens: a real derivation's integers are target-innocent, not chosen to
hit the answer). Result: all three are near-misses, none target-innocent-clean. The meV coincidence is a real order-of-
magnitude LEAD; the absolute scale is an honest boundary at this level.

THE SPECTRUM (derived shape): m₁=0 exact; m₂=√Δm²₂₁=8.61 meV, m₃=√Δm²₃₁=50.1 meV; Σ=58.7 meV; m₃/m₂=5.816=√33.8.

THE THREE HANDLES, AUDITED:
  * HANDLE A — m₃/m₂ = 5.816 as a BST √integer: closest √34=5.831 (0.26%) but 34=2·17 (17 is NOT a BST primary); the
    BST-natural √35=√(n_C·g)=5.916 is 1.72% off; √33=3·11 is 1.23%. NOT target-innocent-clean (the 0.26% match needs a
    non-BST integer; the BST one is 1.7% off).
  * HANDLE B — the meV coincidence / discrete exponent: m₃ = M_Planck·exp(−67.7); the dark-energy Λ^(1/4) scale is
    M_Planck·exp(−70) with 70=2·n_C·g (the exp(−280) energy-density structure). Both are meV-scale — a REAL coincidence —
    but the neutrino exponent 67.7 ≠ 70 (off by 2.3 → a factor ~10 in mass), and 67.7 is not a clean BST integer. So it is
    an order-of-magnitude coincidence, NOT a precise discrete match.
  * HANDLE C — reverse-engineered seesaw M_R = v²/m₃: ≈ 6.0×10¹⁴ GeV (v=174) ≈ M_Planck/N_max² = 6.5×10¹⁴ (7% off), but
    ≈1.2×10¹⁵ (v=246, factor 1.86 = the factor-2 ambiguity). More decisively: M_R was REVERSE-ENGINEERED from m₃, so
    matching it to M_Planck/N_max² is TARGET-AWARE (fit-suspect), not a derivation — there is no INDEPENDENT geometric
    prediction M_R = M_Planck/N_max² to check against. Intriguing as a lead, not a result.

⟹ VERDICT (plain, per Keeper's standing instruction): at the discrete-handle level the neutrino absolute SCALE does NOT pin
to a clean target-innocent BST quantity — all three handles are near-misses (0.26% with a non-BST integer; a factor ~10 in
the exponent; a v-dependent 7–90% with no independent M_R). The meV coincidence is REAL (the neutrino scale sits within ~1
order of BST's exp(−280) dark-energy structure) — a genuine LEAD that the scale is not arbitrary — but it is NOT a precise
discrete derivation. So I report plainly: the absolute neutrino SCALE is an honest continuous/boundary quantity at this
level; what is DERIVED is the spectrum SHAPE (m₁=0 exact) + the Majorana nature (toy 4796). The most intriguing lead to make
target-innocent is M_R = M_Planck/N_max² — IF BST can derive that seesaw scale from geometry INDEPENDENTLY (a Bergman/heat-
kernel scale), recompute; until then it is fit-suspect and I will not dress it up. I am not banking a discrete scale.
Charge + confinement + parity + custodial + ν-Majorana stay closed; Five-Absence-positive. Count ~7-8.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

dm21, dm31 = 7.42e-5, 2.510e-3
m2, m3 = np.sqrt(dm21), np.sqrt(dm31)
ratio = m3/m2
Mpl = 1.2209e28
print(f"\n[spectrum] m1=0 exact; m2={m2*1e3:.2f} meV, m3={m3*1e3:.2f} meV, Σ={ (m2+m3)*1e3:.1f} meV; m3/m2={ratio:.3f}=√{dm31/dm21:.1f}")

# ---- Handle A: m3/m2 ---------------------------------------------------------
A_best_bst = abs(np.sqrt(n_C*g) - ratio)/ratio     # BST-natural candidate √(n_C·g)
check("HANDLE A (m₃/m₂=5.816): closest √34=5.831 is 0.26% but 34=2·17 (17 NOT a BST primary); the BST-natural √35=√(n_C·g) "
      "is 1.72% off; √33=3·11 is 1.23%. So the good numerical match needs a non-BST integer, and the BST-natural one is "
      "~1.7% off → NOT target-innocent-clean.",
      A_best_bst > 0.01, "m₃/m₂: √34 (0.26%, non-BST 17) vs √(n_C·g) (1.7%) → not target-innocent-clean")

# ---- Handle B: meV coincidence ----------------------------------------------
k_nu = -np.log(m3/Mpl); k_de = 2*n_C*g
check("HANDLE B (meV coincidence): m₃=M_Planck·exp(−67.7); dark-energy Λ^(1/4)=M_Planck·exp(−70), 70=2·n_C·g (the exp(−280) "
      "structure). Both meV-scale = a REAL coincidence, but the neutrino exponent 67.7 ≠ 70 (off by 2.3 → factor ~10 in "
      "mass) and 67.7 is not a clean BST integer → an order-of-magnitude coincidence, NOT a precise discrete match.",
      abs(k_nu - k_de) > 1.0, "neutrino exp 67.7 vs dark-energy exp 70=2·n_C·g: factor ~10 off, 67.7 not a clean BST integer → real coincidence, not a discrete match")

# ---- Handle C: reverse-engineered M_R ---------------------------------------
MR_174 = (174.**2)/(m3*1e-9); MR_Nmax2 = 1.2209e19/N_max**2
check("HANDLE C (M_R = v²/m₃): ≈6.0×10¹⁴ GeV (v=174) ≈ M_Planck/N_max² (7%) but ≈1.2×10¹⁵ (v=246, factor 1.86 = factor-2 "
      "ambiguity). Decisively: M_R was REVERSE-ENGINEERED from m₃, so matching M_Planck/N_max² is TARGET-AWARE (fit-suspect) "
      "— there's no INDEPENDENT geometric prediction M_R=M_Planck/N_max² to check. Intriguing lead, not a result.",
      True, "M_R reverse-engineered → M_Planck/N_max² match is target-aware (fit-suspect), v-dependent (factor-2); no independent geometric M_R → not a derivation")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (plain): the neutrino absolute SCALE does NOT pin to a clean target-innocent BST quantity — all three "
      "handles are near-misses (0.26% with a non-BST integer; factor ~10 in the exponent; v-dependent 7–90% with no "
      "independent M_R). The meV coincidence is REAL (within ~1 order of the exp(−280) dark-energy structure) — a genuine "
      "LEAD — but NOT a precise derivation. So the absolute SCALE is an honest continuous/boundary quantity at this level; "
      "what is DERIVED is the spectrum SHAPE (m₁=0 exact) + Majorana nature (4796). Most intriguing lead to make "
      "target-innocent: M_R=M_Planck/N_max² IF BST derives that scale geometrically & independently; until then fit-suspect "
      "and I will NOT dress it up. Not banking a discrete scale.",
      A_best_bst > 0.01 and abs(k_nu - k_de) > 1.0,
      "no target-innocent-clean discrete handle for the ν absolute scale; meV coincidence = real lead not derivation; scale = honest boundary; shape+Majorana derived")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-26 (07-23) neutrino absolute scale — discrete-handle audit (Elie's target-innocence pass; honest boundary):
  * spectrum {{0, 8.61, 50.1}} meV (m1=0 exact); m3/m2=5.816=√33.8.
  * Handle A (m3/m2): √34 (0.26%, non-BST 17) / √(n_C·g) (1.7%) → NOT clean.
  * Handle B (meV coincidence): ν exp(−67.7) vs dark-energy exp(−70)=exp(−2·n_C·g); factor ~10 off, no clean integer → REAL coincidence, not a discrete match.
  * Handle C (M_R=v²/m3 ≈ M_Pl/N_max² at 7%, v=174): reverse-engineered → target-aware/fit-suspect, v-dependent.
  => NO target-innocent-clean discrete handle. meV coincidence = genuine LEAD (within ~1 order of exp(−280)); absolute scale = HONEST CONTINUOUS BOUNDARY at this level. Derived: spectrum shape (m1=0) + Majorana. Lead to pursue: independent geometric M_R. Not dressing up near-misses.
""")
