#!/usr/bin/env python3
"""
Solve the a₃ formula using 6 independent invariants on symmetric spaces.

On symmetric spaces, J₁ = 2I₆_B + I₆_A/2 (algebraic relation on sym spaces).
So the formula effectively has 6 independent parameters:
  5040 a₃ = c₁R³ + c₂R|Ric|² + c₃R|Rm|² + c₄Ric³ + c₅I₆_A + c₆I₆_B

where c₅ and c₆ are "effective" combinations of the original J₁, I₆_A, I₆_B coefficients.

Use S²..S⁶ (5 spheres) + CP² = 6 manifolds for 6 unknowns.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction


def main():
    # Spectral a₃ values (exact)
    spectral = {
        'S2': (Fraction(4, 315), [8, 4, 8, 2, 8, 0]),
        'S3': (Fraction(1, 6), [216, 72, 72, 24, 24, 6]),
        'S4': (Fraction(74, 63), [1728, 432, 288, 108, 48, 24]),
        'S5': (Fraction(16, 3), [8000, 1600, 800, 320, 80, 60]),
        'S6': (Fraction(1139, 63), [27000, 4500, 1800, 750, 120, 120]),
        'CP2': (Fraction(241, 1260), [216, 54, 72, Fraction(27, 2), 30, Fraction(3, 2)]),
    }

    labels = ['c₁ (R³)', 'c₂ (R|Ric|²)', 'c₃ (R|Rm|²)',
              'c₄ (Ric³)', 'c₅ (I₆_A eff)', 'c₆ (I₆_B eff)']

    # Build 6×6 system
    names = ['S2', 'S3', 'S4', 'S5', 'S6', 'CP2']
    n = 6

    A = []
    b = []
    for name in names:
        a3, invs = spectral[name]
        A.append([Fraction(x) for x in invs])
        b.append(5040 * a3)

    # Augmented matrix
    M = [A[i] + [b[i]] for i in range(n)]

    # Gaussian elimination
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            print(f"SINGULAR at column {col}!")
            return
        M[col], M[pivot] = M[pivot], M[col]
        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    # Back substitution
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for j in range(i + 1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]

    print("  ══════════════════════════════════════════════════════")
    print("  EFFECTIVE a₃ FORMULA (on symmetric spaces)")
    print("  ══════════════════════════════════════════════════════")
    print("  5040 a₃ = c₁R³ + c₂R|Ric|² + c₃R|Rm|² + c₄Ric³ + c₅I₆_A + c₆I₆_B")
    print("  (I₆_A = R_{abcd}R^{abef}R^{cd}_{ef}, I₆_B = R_{abcd}R^{acef}R^{bd}_{ef})")
    print()
    for i, (label, coeff) in enumerate(zip(labels, x)):
        print(f"    {label} = {coeff} = {float(coeff):.10f}")

    # Verify on all 6 training manifolds
    print(f"\n  VERIFICATION (training set):")
    for name in names:
        a3_exp, invs = spectral[name]
        val = sum(x[i] * Fraction(invs[i]) for i in range(n))
        a3_pred = val / 5040
        print(f"    {name}: predicted = {a3_pred}, expected = {a3_exp}, match = {a3_pred == a3_exp}")

    # Predict on S⁷, S⁸, S¹⁰
    print(f"\n  PREDICTIONS (test set):")
    test = {
        'S7': (Fraction(501, 10), 7),
        'S8': (Fraction(120), 8),
        'S10': (Fraction(1522, 3), 10),
    }
    for name, (a3_exp, d) in test.items():
        R = d * (d - 1)
        invs = [
            Fraction(d**3 * (d-1)**3),      # R³
            Fraction(d**2 * (d-1)**3),      # R|Ric|²
            Fraction(2 * d**2 * (d-1)**2),  # R|Rm|²
            Fraction(d * (d-1)**3),          # Ric³
            Fraction(4 * d * (d-1)),          # I₆_A
            Fraction(d * (d-1) * (d-2)),      # I₆_B
        ]
        val = sum(x[i] * invs[i] for i in range(n))
        a3_pred = val / 5040
        print(f"    {name}: predicted = {a3_pred} = {float(a3_pred):.10f}, "
              f"expected = {a3_exp} = {float(a3_exp):.10f}, match = {a3_pred == a3_exp}")

    # Also predict S¹×S³
    print(f"\n  S¹×S³ prediction:")
    invs_s1s3 = [
        Fraction(216), Fraction(72), Fraction(72),
        Fraction(24), Fraction(24), Fraction(6)
    ]
    val_s1s3 = sum(x[i] * invs_s1s3[i] for i in range(n))
    a3_s1s3 = val_s1s3 / 5040
    print(f"    predicted = {a3_s1s3} = {float(a3_s1s3):.10f}")
    print(f"    spectral  = 1/6 = {float(Fraction(1,6)):.10f}")
    print(f"    match = {a3_s1s3 == Fraction(1, 6)}")

    # ══════════════════════════════════════════════════════
    # COMPARE WITH LITERATURE
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  COMPARISON WITH PUBLISHED FORMULAS")
    print(f"  ══════════════════════════════════════════════════════")

    # The standard formula (Gilkey 1975, Vassilevich 2003):
    # 5040 a₃ = (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|²
    #          + (208/9)Ric³ - (64/3)J₁ + (16/3)I₆_A + (44/9)I₆_B
    # On symmetric spaces, J₁ = 2I₆_B + I₆_A/2, so:
    # Effective c₅ = 16/3 + (-64/3)/2 = 16/3 - 32/3 = -16/3
    # Effective c₆ = 44/9 + 2×(-64/3) = 44/9 - 128/3 = 44/9 - 384/9 = -340/9

    c1_lit = Fraction(35, 9)
    c2_lit = Fraction(-14, 3)
    c3_lit = Fraction(14, 3)
    c4_lit = Fraction(208, 9)
    # J₁ coefficient in literature: -64/3
    c_J1 = Fraction(-64, 3)
    c_I6A = Fraction(16, 3)
    c_I6B = Fraction(44, 9)

    # Effective on symmetric spaces (J₁ = 2I₆_B + I₆_A/2):
    c5_lit_eff = c_I6A + c_J1 / 2  # I₆_A effective
    c6_lit_eff = c_I6B + 2 * c_J1  # I₆_B effective

    print(f"  Literature (Gilkey/Vassilevich) effective coefficients:")
    print(f"    c₁ = {c1_lit} vs ours = {x[0]}, diff = {x[0] - c1_lit}")
    print(f"    c₂ = {c2_lit} vs ours = {x[1]}, diff = {x[1] - c2_lit}")
    print(f"    c₃ = {c3_lit} vs ours = {x[2]}, diff = {x[2] - c3_lit}")
    print(f"    c₄ = {c4_lit} vs ours = {x[3]}, diff = {x[3] - c4_lit}")
    print(f"    c₅_eff = {c5_lit_eff} vs ours = {x[4]}, diff = {x[4] - c5_lit_eff}")
    print(f"    c₆_eff = {c6_lit_eff} vs ours = {x[5]}, diff = {x[5] - c6_lit_eff}")

    # Check literature formula on S²
    print(f"\n  Literature formula check on S²:")
    invs_s2 = [8, 4, 8, 2, 8, 0]
    val_lit = sum([c1_lit, c2_lit, c3_lit, c4_lit, c5_lit_eff, c6_lit_eff][i] * invs_s2[i]
                  for i in range(6))
    print(f"    5040 a₃ (lit) = {val_lit} = {float(val_lit):.6f}")
    print(f"    5040 a₃ (spectral) = 64")

    # ══════════════════════════════════════════════════════
    # APPLY TO Q⁵
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  APPLICATION TO Q⁵ = SO(5,2)/[SO(5)×SO(2)]")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"  Q⁵ is a symmetric space (T₁=T₂=0), so the effective formula applies.")
    print(f"  But we need the curvature invariants of Q⁵ in the Killing metric.")
    print(f"  Q⁵ has real dimension 10, is Hermitian symmetric, rank 2.")
    print(f"  (Need separate computation for Q⁵ curvature invariants)")


if __name__ == '__main__':
    main()
