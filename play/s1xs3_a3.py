#!/usr/bin/env python3
"""
Compute curvature invariants and spectral a₃ on S¹ × S³.
This is a non-Einstein symmetric space needed to break the degeneracy
between J₁, I₆_A, I₆_B in the a₃ formula.

S¹ × S³: d = 4, R = 6, Ric = diag(0, 2, 2, 2), NOT Einstein.
Spectrum: λ = n² + ℓ(ℓ+2), deg = d_n × (ℓ+1)² where d₀=1, d_{n>0}=2.
Vol = 2π × 2π² = 4π³.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from mpmath import mp, mpf, exp, pi, nstr


def compute_invariants():
    """Compute all 7 cubic curvature invariants on S¹ × S³."""
    d = 4

    # Riemann tensor: only S³ part is nonzero.
    # S³ indices: 1, 2, 3 (mapping to our 0-indexed 1,2,3)
    # S¹ index: 0
    # R_{abcd} = δ_{ac}δ_{bd} - δ_{ad}δ_{bc} for a,b,c,d ∈ {1,2,3}

    def R(a, b, c, dd):
        if a == 0 or b == 0 or c == 0 or dd == 0:
            return Fraction(0)
        return ((Fraction(1) if a == c else Fraction(0)) *
                (Fraction(1) if b == dd else Fraction(0)) -
                (Fraction(1) if a == dd else Fraction(0)) *
                (Fraction(1) if b == c else Fraction(0)))

    rng = range(d)

    # Ricci tensor
    Ric = [[Fraction(0)]*d for _ in range(d)]
    for a in rng:
        for b in rng:
            for c in rng:
                Ric[a][b] += R(a, c, b, c)

    R_scalar = sum(Ric[a][a] for a in rng)
    Ric_sq = sum(Ric[a][b]**2 for a in rng for b in rng)
    Rm_sq = sum(R(a,b,c,dd)**2 for a in rng for b in rng for c in rng for dd in rng)

    print("  S¹ × S³ curvature:")
    print(f"    R = {R_scalar}")
    print(f"    Ric = diag({Ric[0][0]}, {Ric[1][1]}, {Ric[2][2]}, {Ric[3][3]})")
    print(f"    |Ric|² = {Ric_sq}")
    print(f"    |Rm|² = {Rm_sq}")

    # I1 = R³
    I1 = R_scalar**3
    # I2 = R|Ric|²
    I2 = R_scalar * Ric_sq
    # I3 = R|Rm|²
    I3 = R_scalar * Rm_sq
    # I4 = Ric³
    I4 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                I4 += Ric[a][b] * Ric[b][c] * Ric[c][a]
    # I5 = J₁ = Ric_{ab} R_{acde} R_{bcde}
    I5 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for dd in rng:
                    for e in rng:
                        I5 += Ric[a][b] * R(a,c,dd,e) * R(b,c,dd,e)
    # I6 = I₆_A = R_{abcd}R_{cdef}R_{efab}
    I6 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for dd in rng:
                    for e in rng:
                        for f in rng:
                            I6 += R(a,b,c,dd) * R(c,dd,e,f) * R(e,f,a,b)
    # I7 = I₆_B = R_{abcd}R_{aecf}R_{bedf}
    I7 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for dd in rng:
                    for e in rng:
                        for f in rng:
                            I7 += R(a,b,c,dd) * R(a,e,c,f) * R(b,e,dd,f)

    print(f"    I1 = R³ = {I1}")
    print(f"    I2 = R|Ric|² = {I2}")
    print(f"    I3 = R|Rm|² = {I3}")
    print(f"    I4 = Ric³ = {I4}")
    print(f"    I5 = J₁ = {I5}")
    print(f"    I6 = I₆_A = {I6}")
    print(f"    I7 = I₆_B = {I7}")

    # Check: is J₁ = 2I7 + I6/2 here?
    check = 2 * I7 + I6 / 2
    print(f"\n    2·I₆_B + I₆_A/2 = {check} vs J₁ = {I5}: {'EQUAL' if check == I5 else 'DIFFERENT!'}")

    return [I1, I2, I3, I4, I5, I6, I7]


def spectral_a3_s1xs3():
    """Extract spectral a₃ on S¹ × S³ from product spectrum."""
    mp.dps = 80

    d = 4
    Vol = 4 * pi**3  # 2π × 2π²

    # Known: R = 6, a₁ = R/6 = 1
    # a₂ = (5R² - 2|Ric|² + 2|Rm|²)/360 = (180 - 24 + 24)/360 = 1/2
    a0 = mpf(1)
    a1 = mpf(1)
    a2 = mpf(1) / mpf(2)

    t_vals = [mpf(1) / mpf(10**k) for k in [2, 3, 4, 5, 6, 7]]

    # Z(t) = Z_S1(t) × Z_S3(t)
    # Z_S1(t) = 1 + 2 Σ_{n=1}^∞ e^{-n²t}
    # Z_S3(t) = Σ_{ℓ=0}^∞ (ℓ+1)² e^{-ℓ(ℓ+2)t}

    g_vals = []
    for t in t_vals:
        # S¹ factor
        Z1 = mpf(1)
        for n in range(1, 100000):
            term = 2 * exp(-n**2 * t)
            Z1 += term
            if abs(term) < mpf(10)**(-70):
                break

        # S³ factor
        Z3 = mpf(0)
        for ell in range(100000):
            dk = (ell + 1)**2
            lk = ell * (ell + 2)
            term = dk * exp(-lk * t)
            Z3 += term
            if abs(term) < mpf(10)**(-70) and ell > 5:
                break

        Z = Z1 * Z3
        F = (4 * pi * t)**(d / mpf(2)) * Z / Vol
        G = (F - a0 - a1 * t - a2 * t**2) / t**3
        g_vals.append(G)

    # Richardson extrapolation
    levels = [g_vals]
    for _ in range(len(g_vals) - 1):
        prev = levels[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels.append(curr)

    best = levels[min(2, len(levels)-1)][-1]

    print(f"\n  Spectral a₃ on S¹ × S³:")
    print(f"    Level 0 (last 3): {[nstr(v, 15) for v in g_vals[-3:]]}")
    print(f"    Level 1 (last 3): {[nstr(v, 15) for v in levels[1][-3:]]}")
    print(f"    Level 2 (last 3): {[nstr(v, 15) for v in levels[2][-3:]]}")

    val = float(best)
    found = None
    for den in range(1, 50000):
        num = round(val * den)
        if abs(num / den - val) < 1e-6:
            found = Fraction(num, den)
            break
    if found:
        print(f"    → a₃ = {found} = {float(found):.15f}")
    else:
        print(f"    → a₃ ≈ {val:.15f} (fraction not found)")

    return found


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  S¹ × S³: NON-EINSTEIN SYMMETRIC SPACE")
    print("  ══════════════════════════════════════════════════════")

    invs = compute_invariants()
    a3 = spectral_a3_s1xs3()

    if a3:
        rhs = 5040 * a3
        print(f"\n  5040 × a₃ = {rhs}")
        print(f"  Invariant vector: {invs}")

        # Now solve the full system including this data
        # Known spectral a₃ values:
        spectral = {
            2: Fraction(4, 315),
            3: Fraction(1, 6),
            4: Fraction(74, 63),
            5: Fraction(16, 3),
            6: Fraction(1139, 63),
        }
        a3_cp2 = Fraction(241, 1260)

        # Sphere invariants
        def sphere_invs(dim):
            d = dim
            I7_formula = d * (d - 1) * (d - 2)  # I₆_B on S^d
            return [
                Fraction(d**3 * (d-1)**3),
                Fraction(d**2 * (d-1)**3),
                Fraction(2 * d**2 * (d-1)**2),
                Fraction(d * (d-1)**3),
                Fraction(2 * d * (d-1)**2),
                Fraction(4 * d * (d-1)),
                Fraction(I7_formula),
            ]

        # CP² invariants (from earlier computation)
        cp2_invs = [
            Fraction(216), Fraction(54), Fraction(72),
            Fraction(27, 2), Fraction(18), Fraction(30), Fraction(3, 2)
        ]

        # Build 7×7 system: S², S³, S⁴, S⁵, S⁶, CP², S¹×S³
        manifolds = []
        for dim in [2, 3, 4, 5, 6]:
            manifolds.append((f"S^{dim}", sphere_invs(dim), 5040 * spectral[dim]))
        manifolds.append(("CP²", cp2_invs, 5040 * a3_cp2))
        manifolds.append(("S¹×S³", invs, 5040 * a3))

        # Solve
        n = 7
        A_mat = [row[:] for _, row, _ in manifolds]
        b_vec = [rhs_val for _, _, rhs_val in manifolds]
        M = [A_mat[i] + [b_vec[i]] for i in range(n)]

        for col in range(n):
            pivot = None
            for row in range(col, n):
                if M[row][col] != 0:
                    pivot = row
                    break
            if pivot is None:
                print(f"\n  SINGULAR at column {col}!")
                return
            M[col], M[pivot] = M[pivot], M[col]
            for row in range(col + 1, n):
                factor = M[row][col] / M[col][col]
                for j in range(col, n + 1):
                    M[row][j] -= factor * M[col][j]

        x = [Fraction(0)] * n
        for i in range(n - 1, -1, -1):
            x[i] = M[i][n]
            for j in range(i + 1, n):
                x[i] -= M[i][j] * x[j]
            x[i] /= M[i][i]

        labels = ['c₁ (R³)', 'c₂ (R|Ric|²)', 'c₃ (R|Rm|²)',
                  'c₄ (Ric³)', 'c₅ (J₁)', 'c₆ (I₆_A)', 'c₇ (I₆_B)']

        print(f"\n  ══════════════════════════════════════════════════════")
        print(f"  COMPLETE a₃ FORMULA")
        print(f"  ══════════════════════════════════════════════════════")
        print(f"  5040 a₃ = c₁R³ + c₂R|Ric|² + c₃R|Rm|² + c₄Ric³")
        print(f"          + c₅J₁ + c₆I₆_A + c₇I₆_B")
        print(f"  (plus derivative terms that vanish on symmetric spaces)")
        print()
        for label, coeff in zip(labels, x):
            print(f"    {label} = {coeff} = {float(coeff):.10f}")

        # Verify on ALL manifolds
        print(f"\n  VERIFICATION:")
        for name, row, rhs_val in manifolds:
            val = sum(x[i] * row[i] for i in range(n))
            print(f"    {name}: formula = {val / 5040}, expected = {rhs_val / 5040}, "
                  f"match = {val == rhs_val}")

        # Predict S⁷, S⁸, S¹⁰
        print(f"\n  PREDICTIONS:")
        for dim in [7, 8, 10]:
            expected = {7: Fraction(501, 10), 8: Fraction(120), 10: Fraction(1522, 3)}
            row = sphere_invs(dim)
            val = sum(x[i] * row[i] for i in range(n)) / 5040
            print(f"    S^{dim}: predicted = {val} = {float(val):.10f}, "
                  f"expected = {expected[dim]} = {float(expected[dim]):.10f}, "
                  f"match = {val == expected[dim]}")

        # Compare with Vassilevich (correcting for our invariant basis)
        print(f"\n  ══════════════════════════════════════════════════════")
        print(f"  COMPARISON WITH LITERATURE")
        print(f"  ══════════════════════════════════════════════════════")
        print(f"  Standard Vassilevich formula (hep-ph/0306138):")
        print(f"  7! a₃ = (35/9)R³ - (14/3)R·Ric² + (14/3)R·Rm²")
        print(f"        + (208/9)Ric³ - (64/3)J₁ + (16/3)I₆_A + (44/9)I₆_B")
        print(f"  Our formula:")
        for label, coeff in zip(labels, x):
            print(f"    {label} = {coeff}")


if __name__ == '__main__':
    main()
