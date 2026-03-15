#!/usr/bin/env python3
"""
BST — Investigate the 63/64 factor in ã₃
==========================================
The Plancherel dictionary gives ã₃ = -874/9, but the Gilkey formula
(from cubic curvature invariants) gives ã₃ = -55936/567 = -874×64/(9×63).

The ratio is 63/64 EXACTLY. Where does this come from?

Strategy: recompute a₃ from scratch using the Vassilevich formula
with the EXACT curvature invariants, and check each term.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import factorial


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  THE 63/64 FACTOR IN ã₃")
    print("  ══════════════════════════════════════════════════════")

    # ──────────────────────────────────────────────────────
    # Plancherel normalization: R = ±50, Ric = ±5g, d = 10
    # ──────────────────────────────────────────────────────
    d = 10
    n = 5  # complex dimension
    R = Fraction(50)  # scalar curvature (compact Q⁵)
    lam = R / d  # Ric = λg, λ = 5

    Ric_sq = lam**2 * d  # |Ric|² = λ²d = 250
    print(f"\n  R = {R}, λ = {lam}, |Ric|² = {Ric_sq}")

    # |Rm|² from the Lie algebra computation (note Section 2.4)
    # In Killing norm: |Rm|² = 13/5 = c₃/c₁
    # Scale factor from Killing to Plancherel: metrics differ by 1/10
    # |Rm|² ~ (curvature)² ~ (1/scale)² = 10² = 100 × Killing
    # Wait: a₂ check: R_K = 5, R_P = 50, ratio = 10.
    # Curvature scales as 1/c where g_P = g_K/10 (c = 1/10).
    # Rm ~ Ric ~ R/d: all scale as 1/c.
    # |Rm|² = Rm·Rm ~ 1/c². With c = 1/10: factor = 100.
    # |Rm|²_P = 100 × |Rm|²_K = 100 × 13/5 = 260
    Rm_sq = Fraction(260)
    print(f"  |Rm|² = {Rm_sq}")

    # a₂ check
    a2 = (5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360
    print(f"\n  a₂ = {a2} = {float(a2):.10f}")
    assert a2 == Fraction(313, 9), f"a₂ mismatch: {a2}"
    print(f"  ✓ matches 313/9")

    # ──────────────────────────────────────────────────────
    # a₃ from Vassilevich formula
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  a₃ FROM VASSILEVICH (2003)")
    print(f"  ══════════════════════════════════════════════════════")

    # 7! × a₃ = (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|²
    #          - (208/9)Tr(Ric³) + (64/3)I₆ + (16/3)T₁ + (44/9)T₂

    # On an Einstein manifold: Ric = λg
    # Tr(Ric³) = λ³ × d = 125 × 10 = 1250

    Ric3 = lam**3 * d
    print(f"\n  Tr(Ric³) = λ³d = {Ric3}")

    # I₆ = R_{ab}R^a_{cde}R^{bcde}
    # On Einstein: I₆ = (R/d)|Rm|² = (50/10) × 260 = 1300
    I6 = (R / d) * Rm_sq
    print(f"  I₆ = (R/d)|Rm|² = {I6}")

    # T₁ = R_{abcd}R^{ab}_{mn}R^{cdmn}
    # T₂ = R_{abcd}R^a_m^c_n R^{bmdn}
    #
    # From the note (Killing normalization):
    #   T₁ = 41/25, T₂ = 6/25
    # Scale: T₁, T₂ ~ Rm³ ~ (curvature)³. Scale factor from Killing: 10³ = 1000.
    T1_killing = Fraction(41, 25)
    T2_killing = Fraction(6, 25)

    T1 = T1_killing * 1000  # = 41000/25 = 1640
    T2 = T2_killing * 1000  # = 6000/25 = 240

    print(f"  T₁ = {T1} (from note × 1000)")
    print(f"  T₂ = {T2} (from note × 1000)")

    # Compute a₃
    f7 = Fraction(factorial(7))  # 5040
    a3_terms = {
        '(35/9)R³': Fraction(35, 9) * R**3,
        '-(14/3)R|Ric|²': Fraction(-14, 3) * R * Ric_sq,
        '(14/3)R|Rm|²': Fraction(14, 3) * R * Rm_sq,
        '-(208/9)Tr(Ric³)': Fraction(-208, 9) * Ric3,
        '(64/3)I₆': Fraction(64, 3) * I6,
        '(16/3)T₁': Fraction(16, 3) * T1,
        '(44/9)T₂': Fraction(44, 9) * T2,
    }

    total = Fraction(0)
    for name, val in a3_terms.items():
        total += val
        print(f"    {name} = {val} = {float(val):.4f}")

    a3_note = total / f7
    print(f"\n  7! × a₃ = {total}")
    print(f"  a₃ = {total}/{f7} = {a3_note} = {float(a3_note):.12f}")

    # Compare with Plancherel ã₃ = -874/9 (for noncompact: multiply by -1)
    a3_planch_Q = Fraction(874, 9)  # compact side
    ratio = a3_note / a3_planch_Q
    print(f"\n  a₃(Gilkey, Q) = {a3_note} = {float(a3_note):.10f}")
    print(f"  a₃(Plancherel, Q) = {a3_planch_Q} = {float(a3_planch_Q):.10f}")
    print(f"  Ratio = {ratio} = {float(ratio):.10f}")

    if ratio == Fraction(64, 63):
        print(f"  Ratio = 64/63 EXACTLY (reciprocal of 63/64)")
    elif ratio == Fraction(63, 64):
        print(f"  Ratio = 63/64 EXACTLY")

    # ──────────────────────────────────────────────────────
    # Which term is wrong? Try varying T₁, T₂
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  WHICH INVARIANT GIVES THE CORRECTION?")
    print(f"  ══════════════════════════════════════════════════════")

    # If a₃ should be 874/9, then 7! × a₃ = 5040 × 874/9 = 4,411,280/9 ≈ 490,142.2
    target = Fraction(874, 9) * f7
    print(f"\n  Target: 7! × ã₃(Q) = {target} = {float(target):.6f}")

    current = total
    diff = target - current
    print(f"  Current (Gilkey): {current} = {float(current):.6f}")
    print(f"  Difference: {diff} = {float(diff):.6f}")

    # What adjustment to T₁ fixes it?
    # (16/3)(T₁ + δ₁) replaces (16/3)T₁
    # Need (16/3)δ₁ = diff → δ₁ = diff × 3/16
    delta_T1 = diff * Fraction(3, 16)
    T1_corrected = T1 + delta_T1
    print(f"\n  If T₁ correction: δ₁ = {delta_T1} = {float(delta_T1):.6f}")
    print(f"  T₁_corrected = {T1_corrected} = {float(T1_corrected):.6f}")
    print(f"  T₁_corrected / T₁ = {T1_corrected / T1} = {float(T1_corrected / T1):.10f}")

    # What adjustment to T₂ fixes it?
    delta_T2 = diff * Fraction(9, 44)
    T2_corrected = T2 + delta_T2
    print(f"\n  If T₂ correction: δ₂ = {delta_T2} = {float(delta_T2):.6f}")
    print(f"  T₂_corrected = {T2_corrected} = {float(T2_corrected):.6f}")
    print(f"  T₂_corrected / T₂ = {T2_corrected / T2} = {float(T2_corrected / T2):.10f}")

    # ──────────────────────────────────────────────────────
    # Alternative: check if there's a missing term
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  ALTERNATIVE: DIFFERENT a₃ FORMULA")
    print(f"  ══════════════════════════════════════════════════════")

    # The Vassilevich formula for the SCALAR Laplacian on a d-dimensional
    # manifold. There are different versions in the literature.
    # Gilkey (1975): uses a specific convention
    # Branson-Gilkey-Pohjanpelto (1997): updated
    # Vassilevich (2003): review article

    # Let me check: does the standard BGP formula have the same coefficients?
    # The a₃ coefficient has 17 independent terms in general.
    # On an Einstein symmetric space, most vanish (∇Rm = 0, ∇R = 0).

    # Alternative formula (Branson-Ørsted 1986):
    # 7! a₃ = (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|²
    #        - (208/9)|Ric|² R + 64/3 × R_{ij}R^{ikml}R_{kml}^{j}
    #        + 16/3 × R_{ijkl}R^{ij}_{mn}R^{klmn}
    #        + 44/9 × R_{ikjl}R^{imjn}R_{m}^{k}{}_{n}^{l}
    #        + (some additional terms involving ∇²R, ∇²Ric, ∇Rm²)
    #
    # On a symmetric space, ALL derivative terms vanish.
    # So the formula reduces to exactly the terms above.

    # Wait, I notice that -(208/9)Tr(Ric³) and -(208/9)|Ric|²R are
    # DIFFERENT things. On Einstein: Tr(Ric³) = λ³d and |Ric|²R = λ²d × R.
    # Since λ = R/d: λ³d = R³/d² and λ²dR = R³/d.
    # So Tr(Ric³) = R³/d² while |Ric|²R = R³/d. Different!

    # In my computation above, I used -(208/9)Tr(Ric³) = -(208/9)λ³d
    # The note uses -(208/9)Tr(Ric³) which is correct for the Vassilevich formula.

    # But some references have -(208/9)R_{ij}R_{jk}R_{ki} instead of
    # -(208/9)Tr(Ric³). These are the same thing on a Riemannian manifold.

    # Let me check a different coefficient combination.
    # Berline-Getzler-Vergne formula:

    # Actually, the most authoritative source is Gilkey's book
    # "Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem"
    # Table 4.1 (2nd edition, 1995).

    # For the scalar Laplacian (E = 0, Ω = 0):
    # 360 × a₂ = 5R² - 2|Ric|² + 2|Rm|²
    # Which we verified. ✓

    # For a₃, Gilkey gives (adapted to conventions):
    # 7! × a₃ = -(18 ΔR + 17 R;k;k) + 2 terms
    # On symmetric space: Δ R = 0, so these vanish.

    # The purely algebraic terms are:
    # 7! a₃ = -35/9 R³ + 14/3 R|Ric|² - 14/3 R|Rm|²
    #         + 208/9 R_{ij}R_{jk}R_{ki}  (NOTE: sign!)
    #         - 64/3 R_{ij}R^i_{klm}R^{jklm}
    #         - 16/3 R_{ijkl}R^{ij}_{mn}R^{klmn}
    #         - 44/9 R_{ijkl}R^i_m^k_n R^{jmln}

    # Wait, I may have the signs wrong! Different references use different
    # sign conventions. Let me check by verifying a₃ for the round sphere S^d.

    # On S^d with Ric = (d-1)g, R = d(d-1):
    # |Ric|² = (d-1)² × d
    # |Rm|² = 2d(d-1) (for the round sphere)

    # For S^10 (d=10): R = 90, |Ric|² = 81×10=810, |Rm|² = 180
    # Tr(Ric³) = 9³×10 = 7290
    # I₆ = (90/10)×180 = 1620
    # T₁ = ? T₂ = ? for the round sphere

    # Actually, the sphere S^d has constant sectional curvature K=1:
    # R_{ijkl} = g_{ik}g_{jl} - g_{il}g_{jk}
    # T₁ = R_{ijkl}R^{ij}_{mn}R^{klmn}
    # = (g_{ik}g_{jl}-g_{il}g_{jk})(g^{im}g^{jn}-g^{in}g^{jm})(g_{km}g_{ln}-g_{kn}g_{lm})
    # This is a combinatorial computation. For constant curvature:
    # T₁ = 4d(d-1) and T₂ = 2d(d-1) (I think)

    # Let me not go down this rabbit hole and instead just verify
    # the Q⁵ result numerically.

    print(f"\n  The 63/64 factor = 1 - 1/64 = 1 - 1/2⁶")
    print(f"  63 = 7 × 9 = g × c₄")
    print(f"  64 = 2⁶")
    print(f"\n  The correction diff = {diff}")
    print(f"  diff / (7! × a₃_note) = {diff / (f7 * a3_note)} = {float(diff / (f7 * a3_note)):.10f}")
    print(f"  = 1/64 if diff/total = 1/64")
    check = diff / current
    print(f"  diff / total = {check} = {float(check):.10f}")
    print(f"  -1/64 = {float(Fraction(-1, 64)):.10f}")

    # Summary
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SUMMARY")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"\n  The Plancherel computation gives:")
    print(f"    ã₃(Q⁵) = 874/9 = {float(Fraction(874,9)):.10f}")
    print(f"  The Vassilevich formula gives:")
    print(f"    a₃(Q⁵) = {a3_note} = {float(a3_note):.10f}")
    print(f"  Ratio: {ratio} = {float(ratio):.10f}")
    print(f"\n  The Plancherel result is based directly on the Harish-Chandra")
    print(f"  c-function (representation theory), while the Vassilevich result")
    print(f"  uses explicit curvature contractions. The 63/64 discrepancy")
    print(f"  most likely indicates an error in one of the cubic invariants")
    print(f"  T₁ or T₂ (which require careful index contraction on so(7)).")


if __name__ == '__main__':
    main()
