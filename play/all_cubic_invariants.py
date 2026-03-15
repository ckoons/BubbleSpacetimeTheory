#!/usr/bin/env python3
"""
Compute ALL independent cubic Riemann invariants on CP² and S^d.
Identify which invariants appear in the a₃ formula.

The 8 independent cubic Riemann invariants (d ≥ 6) are:
  I1 = R³
  I2 = R·|Ric|²
  I3 = R·|Rm|²
  I4 = Ric³ = R_{ab}R^{bc}R_{ca}
  I5 = R_{ab}R^{acde}R^{b}_{cde}  ("J₁")
  I6 = R_{abcd}R^{abef}R^{cd}_{ef}  ("I₆_A")
  I7 = R_{abcd}R^{acef}R^{bd}_{ef}  ("I₆_B")
  (I8 is dependent in d=4)

Plus derivative terms (vanish on symmetric spaces):
  T1 = |∇Rm|², T2 = |∇Ric|², T3 = |∇R|²

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import comb
from mpmath import mp, mpf, exp, pi, nstr


def build_cp2_riemann(H=Fraction(1)):
    """Build Riemann tensor of CP² in orthonormal Kähler frame."""
    d = 4
    # J: complex structure
    J = [[Fraction(0)]*d for _ in range(d)]
    J[0][1], J[1][0] = Fraction(1), Fraction(-1)
    J[2][3], J[3][2] = Fraction(1), Fraction(-1)

    def R(a, b, c, dd):
        return H * Fraction(1, 4) * (
            (Fraction(1) if a == c else Fraction(0)) * (Fraction(1) if b == dd else Fraction(0))
            - (Fraction(1) if a == dd else Fraction(0)) * (Fraction(1) if b == c else Fraction(0))
            + J[a][c] * J[b][dd]
            - J[a][dd] * J[b][c]
            + 2 * J[a][b] * J[c][dd]
        )
    return R, d


def build_sphere_riemann(dim):
    """Build Riemann tensor of S^dim (unit curvature)."""
    def R(a, b, c, dd):
        if a == c and b == dd:
            return Fraction(1) if a != b else Fraction(0)
        elif a == dd and b == c:
            return Fraction(-1) if a != b else Fraction(0)
        else:
            return Fraction(0)
    return R, dim


def compute_all_invariants(R, d, name):
    """Compute all 7 cubic curvature invariants."""
    rng = range(d)

    # Ricci tensor
    Ric = [[Fraction(0)]*d for _ in range(d)]
    for a in rng:
        for b in rng:
            for c in rng:
                Ric[a][b] += R(a, c, b, c)

    # Scalar curvature
    R_scalar = sum(Ric[a][a] for a in rng)

    # |Ric|²
    Ric_sq = sum(Ric[a][b]**2 for a in rng for b in rng)

    # |Rm|²
    Rm_sq = sum(R(a,b,c,dd)**2 for a in rng for b in rng for c in rng for dd in rng)

    # I1 = R³
    I1 = R_scalar**3

    # I2 = R × |Ric|²
    I2 = R_scalar * Ric_sq

    # I3 = R × |Rm|²
    I3 = R_scalar * Rm_sq

    # I4 = Ric³ = Ric_{ab}Ric_{bc}Ric_{ca}
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

    # I6 = R_{abcd}R_{cdef}R_{efab}  ("type A": chain contraction)
    I6 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for dd in rng:
                    for e in rng:
                        for f in rng:
                            I6 += R(a,b,c,dd) * R(c,dd,e,f) * R(e,f,a,b)

    # I7 = R_{abcd}R_{aecf}R_{bedf}  ("type B": interleaved contraction)
    I7 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for dd in rng:
                    for e in rng:
                        for f in rng:
                            I7 += R(a,b,c,dd) * R(a,e,c,f) * R(b,e,dd,f)

    print(f"\n  {name} (d={d}):")
    print(f"    R = {R_scalar}")
    print(f"    |Ric|² = {Ric_sq}")
    print(f"    |Rm|² = {Rm_sq}")
    print(f"    I1 = R³ = {I1}")
    print(f"    I2 = R|Ric|² = {I2}")
    print(f"    I3 = R|Rm|² = {I3}")
    print(f"    I4 = Ric³ = {I4}")
    print(f"    I5 = J₁ = {I5}")
    print(f"    I6 = I₆_A = {I6}")
    print(f"    I7 = I₆_B = {I7}")

    return {
        'R': R_scalar, 'Ric_sq': Ric_sq, 'Rm_sq': Rm_sq,
        'I1': I1, 'I2': I2, 'I3': I3, 'I4': I4,
        'I5': I5, 'I6': I6, 'I7': I7,
    }


def spectral_a3_sphere(d, K_max=100000):
    """Extract spectral a₃ on S^d."""
    mp.dps = 80
    Vol = 2 * pi**((d + 1) / mpf(2)) / mpf(1).__class__(1)

    from mpmath import gamma as gam
    Vol = 2 * pi**((d + 1) / mpf(2)) / gam((d + 1) / mpf(2))

    def deg(ell):
        v = comb(d + ell, d)
        if ell >= 2:
            v -= comb(d + ell - 2, d)
        return v

    R = d * (d - 1)
    a0 = mpf(1)
    a1 = mpf(R) / 6
    Ric_sq = (d-1)**2 * d
    Rm_sq = 2 * d * (d-1)
    a2 = mpf(5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360

    t_vals = [mpf(1) / mpf(10**k) for k in [2, 3, 4, 5, 6, 7]]
    g_vals = []
    for t in t_vals:
        Z = mpf(0)
        for ell in range(K_max):
            dk = deg(ell)
            lk = ell * (ell + d - 1)
            term = dk * exp(-lk * t)
            Z += term
            if abs(term) < mpf(10)**(-70) and ell > 10:
                break
        F = (4 * pi * t)**(d / mpf(2)) * Z / Vol
        G = (F - a0 - a1 * t - a2 * t**2) / t**3
        g_vals.append(G)

    levels = [g_vals]
    for _ in range(len(g_vals) - 1):
        prev = levels[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels.append(curr)
    best = levels[min(2, len(levels)-1)][-1]

    val = float(best)
    for den in range(1, 50000):
        num = round(val * den)
        if abs(num / den - val) < 1e-6:
            return Fraction(num, den)
    return None


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  ALL CUBIC CURVATURE INVARIANTS")
    print("  ══════════════════════════════════════════════════════")

    # Compute on CP²
    R_cp2, d_cp2 = build_cp2_riemann()
    inv_cp2 = compute_all_invariants(R_cp2, d_cp2, "CP²")

    # Compute on S⁴ for comparison
    R_s4, d_s4 = build_sphere_riemann(4)
    inv_s4 = compute_all_invariants(R_s4, d_s4, "S⁴")

    # Verify S⁴ invariants match formulas
    d = 4
    print(f"\n  S⁴ formula check:")
    print(f"    R³ = {d**3*(d-1)**3} (expect {inv_s4['I1']})")
    print(f"    R|Ric|² = {d**2*(d-1)**3} (expect {inv_s4['I2']})")
    print(f"    R|Rm|² = {2*d**2*(d-1)**2} (expect {inv_s4['I3']})")
    print(f"    Ric³ = {d*(d-1)**3} (expect {inv_s4['I4']})")
    print(f"    J₁ = {2*d*(d-1)**2} (expect {inv_s4['I5']})")
    print(f"    I₆_A = {4*d*(d-1)} (expect {inv_s4['I6']})")

    # ══════════════════════════════════════════════════════
    # SPECTRAL a₃ VALUES
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SPECTRAL a₃ VALUES")
    print(f"  ══════════════════════════════════════════════════════")

    # Known from previous computation
    spectral_a3 = {
        2: Fraction(4, 315),
        3: Fraction(1, 6),
        4: Fraction(74, 63),
        5: Fraction(16, 3),
        6: Fraction(1139, 63),
        7: Fraction(501, 10),
        8: Fraction(120),
        10: Fraction(1522, 3),
    }

    # CP² spectral
    a3_cp2 = Fraction(241, 1260)

    for d, a3 in sorted(spectral_a3.items()):
        print(f"    S^{d}: a₃ = {a3} = {float(a3):.10f}")
    print(f"    CP²:  a₃ = {a3_cp2} = {float(a3_cp2):.10f}")

    # ══════════════════════════════════════════════════════
    # SOLVE: 5040 a₃ = c1·I1 + c2·I2 + c3·I3 + c4·I4 + c5·I5 + c6·I6 + c7·I7
    # On symmetric spaces: T₁ = T₂ = 0
    # Use S² through S⁸ (6 spheres, but polynomially only 5 independent)
    # Plus CP² for 6th equation
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SOLVING FOR FORMULA COEFFICIENTS")
    print(f"  ══════════════════════════════════════════════════════")

    # On S^d (even or odd), the invariants are:
    # I1 = d³(d-1)³, I2 = d²(d-1)³, I3 = 2d²(d-1)²
    # I4 = d(d-1)³, I5 = 2d(d-1)², I6 = 4d(d-1), I7 = ? (need to compute on each S^d)

    # First compute I7 on S^d for several d
    print(f"\n  Computing I₆_B on spheres...")
    I7_sphere = {}
    for dim in [2, 3, 4, 5, 6]:
        R_s, d_s = build_sphere_riemann(dim)
        I7_val = Fraction(0)
        rng = range(dim)
        for a in rng:
            for b in rng:
                for c in rng:
                    for dd in rng:
                        for e in rng:
                            for f in rng:
                                I7_val += R_s(a,b,c,dd) * R_s(a,e,c,f) * R_s(b,e,dd,f)
        I7_sphere[dim] = I7_val
        print(f"    S^{dim}: I₆_B = {I7_val}")

    # Check if I7 = a*d(d-1) + b*d(d-1)^2 + ... (polynomial in d)
    # From d=2: I7(2) = ?
    # Let me see the pattern
    print(f"\n  I₆_B values on spheres:")
    for dim, val in sorted(I7_sphere.items()):
        R_d = dim * (dim - 1)
        ratio = val / R_d if R_d != 0 else None
        print(f"    S^{dim}: I₆_B = {val}, I₆_B/[d(d-1)] = {ratio}")

    # Now set up the linear system
    # On S^d: 5040 a₃ = c1 d³(d-1)³ + c2 d²(d-1)³ + c3 2d²(d-1)²
    #                  + c4 d(d-1)³ + c5 2d(d-1)² + c6 4d(d-1) + c7 I7(d)
    #
    # On CP²: 5040 a₃ = c1×216 + c2×54 + c3×72 + c4×27/2 + c5×18 + c6×30 + c7×I7_CP2

    # We have 7 unknowns (c1..c7) and we need 7 equations.
    # Use S² through S⁶ (5 spheres) + CP² = 6 equations. Need one more.
    # Actually, let's check: are the 7 invariants linearly independent on our test set?

    # Build matrix: each row is [I1, I2, I3, I4, I5, I6, I7] for a manifold
    # RHS is 5040 × a₃

    manifolds = []
    for dim in [2, 3, 4, 5, 6]:
        R_d = dim * (dim - 1)
        row = [
            Fraction(dim**3 * (dim-1)**3),        # I1 = R³
            Fraction(dim**2 * (dim-1)**3),        # I2 = R|Ric|²
            Fraction(2 * dim**2 * (dim-1)**2),    # I3 = R|Rm|²
            Fraction(dim * (dim-1)**3),            # I4 = Ric³
            Fraction(2 * dim * (dim-1)**2),        # I5 = J₁
            Fraction(4 * dim * (dim-1)),            # I6 = I₆_A
            I7_sphere[dim],                         # I7 = I₆_B
        ]
        rhs = 5040 * spectral_a3[dim]
        manifolds.append((f"S^{dim}", row, rhs))

    # Add CP²
    cp2_row = [
        inv_cp2['I1'], inv_cp2['I2'], inv_cp2['I3'],
        inv_cp2['I4'], inv_cp2['I5'], inv_cp2['I6'], inv_cp2['I7'],
    ]
    cp2_rhs = 5040 * a3_cp2
    manifolds.append(("CP²", cp2_row, cp2_rhs))

    print(f"\n  Linear system (7 unknowns, {len(manifolds)} equations):")
    for name, row, rhs in manifolds:
        print(f"    {name}: {row} = {rhs}")

    # We have 6 equations, 7 unknowns. Need one more manifold.
    # Options: S⁷ (already computed spectral a₃ = 501/10)
    # But need I₆_B on S⁷ — expensive (7^6 = 117649 terms).
    # Use the formula: I₆_B on S^d = ? (fit from d=2..6)

    # Actually, let me check if I7 follows a simple polynomial in d
    print(f"\n  Fitting I₆_B(d) as polynomial:")
    dims_fit = sorted(I7_sphere.keys())
    I7_vals_fit = [I7_sphere[dim] for dim in dims_fit]

    # I7 should be degree ≤ 3 (product of 3 deltas gives at most d³ after summation)
    # Actually, |Rm|² = 2d(d-1) = degree 2, and I6_A = 4d(d-1) = degree 2.
    # I7 involves 3 Riemann tensors contracted in a different pattern.
    # Each R contributes at most 1 delta per pair → at most d³ from the sums.

    # Fit degree-4 polynomial (5 points, degree 4)
    n = 5  # 5 data points, fit degree 4
    A = [[Fraction(dim)**k for k in range(n)] for dim in dims_fit]
    M = [row + [rhs] for row, rhs in zip(A, I7_vals_fit)]

    for col in range(n):
        pivot = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot = row
                break
        M[col], M[pivot] = M[pivot], M[col]
        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    poly = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        poly[i] = M[i][n]
        for j in range(i + 1, n):
            poly[i] -= M[i][j] * poly[j]
        poly[i] /= M[i][i]

    print(f"    I₆_B(d) = ", end="")
    terms = []
    for k in range(n):
        if poly[k] != 0:
            terms.append(f"({poly[k]})d^{k}")
    print(" + ".join(terms))

    # Verify
    for dim in dims_fit:
        val = sum(poly[k] * Fraction(dim)**k for k in range(n))
        print(f"    I₆_B({dim}) = {val} (expect {I7_sphere[dim]}), match = {val == I7_sphere[dim]}")

    # Now compute I7 for d=7 from polynomial
    I7_s7 = sum(poly[k] * Fraction(7)**k for k in range(n))
    print(f"    I₆_B(7) = {I7_s7} (predicted)")

    # Add S⁷ to the system
    dim = 7
    row_s7 = [
        Fraction(dim**3 * (dim-1)**3),
        Fraction(dim**2 * (dim-1)**3),
        Fraction(2 * dim**2 * (dim-1)**2),
        Fraction(dim * (dim-1)**3),
        Fraction(2 * dim * (dim-1)**2),
        Fraction(4 * dim * (dim-1)),
        I7_s7,
    ]
    rhs_s7 = 5040 * spectral_a3[7]
    manifolds.append(("S⁷", row_s7, rhs_s7))

    # Now we have 7 equations, 7 unknowns. Solve!
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SOLVING 7×7 SYSTEM")
    print(f"  ══════════════════════════════════════════════════════")

    n = 7
    A_mat = [row[:] for _, row, _ in manifolds]
    b_vec = [rhs for _, _, rhs in manifolds]
    M = [A_mat[i] + [b_vec[i]] for i in range(n)]

    for col in range(n):
        pivot = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            print("  SINGULAR! Column", col)
            # Check rank
            print("  Matrix rows:")
            for r in M:
                print("   ", r[:n])
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

    labels = ['α (R³)', 'β (R|Ric|²)', 'γ (R|Rm|²)', 'δ (Ric³)',
              'ε (J₁)', 'ζ (I₆_A)', 'η (I₆_B)']

    print(f"\n  CORRECTED a₃ FORMULA COEFFICIENTS:")
    print(f"  5040 a₃ = α R³ + β R|Ric|² + γ R|Rm|² + δ Ric³ + ε J₁ + ζ I₆_A + η I₆_B")
    print()
    for i, (label, coeff) in enumerate(zip(labels, x)):
        print(f"    {label}: {coeff} = {float(coeff):.10f}")

    # Verify on all manifolds
    print(f"\n  VERIFICATION:")
    for name, row, rhs in manifolds:
        val = sum(x[i] * row[i] for i in range(n))
        a3_val = val / 5040
        a3_exp = rhs / 5040
        print(f"    {name}: formula = {a3_val} = {float(a3_val):.10f}, "
              f"expected = {a3_exp} = {float(a3_exp):.10f}, match = {a3_val == a3_exp}")

    # Also check S⁸ and S¹⁰
    print(f"\n  PREDICTIONS:")
    for dim in [8, 10]:
        I7_pred = sum(poly[k] * Fraction(dim)**k for k in range(len(poly)))
        row = [
            Fraction(dim**3 * (dim-1)**3),
            Fraction(dim**2 * (dim-1)**3),
            Fraction(2 * dim**2 * (dim-1)**2),
            Fraction(dim * (dim-1)**3),
            Fraction(2 * dim * (dim-1)**2),
            Fraction(4 * dim * (dim-1)),
            I7_pred,
        ]
        a3_pred = sum(x[i] * row[i] for i in range(n)) / 5040
        a3_spectral = spectral_a3[dim]
        print(f"    S^{dim}: predicted = {a3_pred} = {float(a3_pred):.10f}, "
              f"spectral = {a3_spectral} = {float(a3_spectral):.10f}, "
              f"match = {a3_pred == a3_spectral}")

    # Compare with Vassilevich
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  COMPARISON WITH VASSILEVICH")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"  Vassilevich uses 5 invariants: R³, R|Ric|², R|Rm|², Ric³, I₆")
    print(f"  (where I₆ might be I₆_A or I₆_B or a combination)")
    print()
    print(f"  Vassilevich coefficients: α=35/9, β=-14/3, γ=14/3, δ=-208/9, ε=64/3")
    print()

    alpha_V = Fraction(35, 9)
    beta_V = Fraction(-14, 3)
    gamma_V = Fraction(14, 3)
    delta_V = Fraction(-208, 9)
    epsilon_V = Fraction(64, 3)

    # Our 7 coefficients. Vassilevich might be using a different basis.
    # If Vassilevich's "I₆" = I₆_A, then his J₁ coefficient is 0.
    # Or he might have a different definition.
    print(f"  Our coefficients:")
    for label, coeff in zip(labels, x):
        print(f"    {label}: {coeff}")


if __name__ == '__main__':
    main()
