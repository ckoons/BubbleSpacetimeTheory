#!/usr/bin/env python3
"""
Extract spectral a₃ on CP² and odd spheres, using known a₀, a₁, a₂.
Then check against corrected formula.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import comb
from mpmath import mp, mpf, exp, pi, nstr, gamma


def extract_a3(name, d, Vol, a0, a1, a2, eigen_gen, K_max=100000):
    """Extract a₃ from spectrum using known a₀, a₁, a₂."""
    mp.dps = 80

    t_vals = [mpf(1) / mpf(10**k) for k in [2, 3, 4, 5, 6, 7]]
    g_vals = []

    for t in t_vals:
        Z = mpf(0)
        for k in range(K_max):
            lam, deg = eigen_gen(k)
            term = deg * exp(-lam * t)
            Z += term
            if abs(term) < mpf(10)**(-70) and k > 10:
                break

        F = (4 * pi * t)**(d / mpf(2)) * Z / Vol
        G = (F - a0 - a1 * t - a2 * t**2) / t**3
        g_vals.append(G)

    # Multi-level Richardson
    levels = [g_vals]
    for _ in range(len(g_vals) - 1):
        prev = levels[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels.append(curr)

    best = levels[min(2, len(levels)-1)][-1]

    print(f"\n  {name} (d={d}):")
    print(f"    Level 0 (last 3): {[nstr(v, 15) for v in g_vals[-3:]]}")
    print(f"    Level 1 (last 3): {[nstr(v, 15) for v in levels[1][-3:]]}")
    print(f"    Level 2 (last 3): {[nstr(v, 15) for v in levels[2][-3:]]}")

    # Identify fraction
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
    return found, best


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  SPECTRAL a₃ EXTRACTION WITH KNOWN a₀, a₁, a₂")
    print("  ══════════════════════════════════════════════════════")

    # ── CP² (Killing metric) ──
    # λ_k = k(k+2), d_k = (k+1)³
    # R = 6, Ric = (3/2)g, |Ric|² = 9, |Rm|² = 12
    # Vol = 8π²
    Vol_cp2 = 8 * pi**2
    a0_cp2 = mpf(1)
    a1_cp2 = mpf(1)  # R/6 = 6/6
    a2_cp2 = mpf(31) / 60  # (5×36 - 2×9 + 2×12)/360 = 186/360

    def cp2_eigen(k):
        return (k * (k + 2), (k + 1)**3)

    frac_cp2, val_cp2 = extract_a3("CP²", 4, Vol_cp2, a0_cp2, a1_cp2, a2_cp2, cp2_eigen)

    # ── S³ ──
    d = 3
    Vol_s3 = 2 * pi**2
    R = d * (d - 1)  # 6
    Ric_sq = (d-1)**2 * d  # 12
    Rm_sq = 2 * d * (d-1)  # 12
    a0_s3 = mpf(1)
    a1_s3 = mpf(R) / 6  # 1
    a2_s3 = mpf(5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360  # 1/2

    def s3_eigen(ell):
        dk = comb(d + ell, d) - (comb(d + ell - 2, d) if ell >= 2 else 0)
        return (ell * (ell + d - 1), dk)

    frac_s3, val_s3 = extract_a3("S³", 3, Vol_s3, a0_s3, a1_s3, a2_s3, s3_eigen)

    # ── S⁵ ──
    d = 5
    Vol_s5 = pi**3  # Vol(S⁵) = π³
    R = d * (d - 1)  # 20
    Ric_sq = (d-1)**2 * d  # 80
    Rm_sq = 2 * d * (d-1)  # 40
    a0_s5 = mpf(1)
    a1_s5 = mpf(R) / 6  # 10/3
    a2_s5 = mpf(5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360  # 16/3

    def s5_eigen(ell):
        dk = comb(d + ell, d) - (comb(d + ell - 2, d) if ell >= 2 else 0)
        return (ell * (ell + d - 1), dk)

    frac_s5, val_s5 = extract_a3("S⁵", 5, Vol_s5, a0_s5, a1_s5, a2_s5, s5_eigen)

    # ── S⁷ ──
    d = 7
    Vol_s7 = pi**3 * mpf(16) / 15  # Vol(S⁷) = π³ × 16/15... actually
    # Vol(S^n) = 2π^{(n+1)/2} / Γ((n+1)/2)
    Vol_s7 = 2 * pi**(mpf(4)) / gamma(mpf(4))  # = 2π⁴/6 = π⁴/3
    R = d * (d - 1)  # 42
    Ric_sq = (d-1)**2 * d  # 252
    Rm_sq = 2 * d * (d-1)  # 84
    a0_s7 = mpf(1)
    a1_s7 = mpf(R) / 6  # 7
    a2_s7 = mpf(5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360

    def s7_eigen(ell):
        dk = comb(d + ell, d) - (comb(d + ell - 2, d) if ell >= 2 else 0)
        return (ell * (ell + d - 1), dk)

    frac_s7, val_s7 = extract_a3("S⁷", 7, Vol_s7, a0_s7, a1_s7, a2_s7, s7_eigen)

    # ══════════════════════════════════════════════════════
    # CHECK CORRECTED FORMULA ON ODD SPHERES
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  CORRECTED FORMULA CHECK ON ODD SPHERES")
    print(f"  ══════════════════════════════════════════════════════")

    alpha = Fraction(35, 9)
    beta = Fraction(-14, 3)
    gamma_c = Fraction(34, 9)
    delta = Fraction(0)
    epsilon = Fraction(8, 3)

    for d_val, frac, label in [(3, frac_s3, "S³"), (5, frac_s5, "S⁵"), (7, frac_s7, "S⁷")]:
        R = d_val * (d_val - 1)
        Ric_sq = (d_val - 1)**2 * d_val
        Rm_sq = 2 * d_val * (d_val - 1)
        Ric3 = (d_val - 1)**3 * d_val
        I6 = 4 * d_val * (d_val - 1)

        a3_formula = (alpha * R**3 + beta * R * Ric_sq
                      + gamma_c * R * Rm_sq + delta * Ric3
                      + epsilon * I6) / 5040

        print(f"\n  {label} (d={d_val}):")
        if frac:
            print(f"    Spectral:  {frac} = {float(frac):.15f}")
        print(f"    Corrected: {a3_formula} = {float(a3_formula):.15f}")
        if frac:
            diff = frac - a3_formula
            print(f"    Match: {frac == a3_formula}")
            if diff != 0:
                print(f"    Difference: {diff} = {float(diff):.15f}")

    # ══════════════════════════════════════════════════════
    # CP² ANALYSIS
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  CP² ANALYSIS")
    print(f"  ══════════════════════════════════════════════════════")
    if frac_cp2:
        # Known CP² invariants (Killing metric, R=6):
        R_cp2 = Fraction(6)
        Ric_sq_cp2 = Fraction(9)
        Rm_sq_cp2 = Fraction(12)

        known = (alpha * R_cp2**3 + beta * R_cp2 * Ric_sq_cp2
                 + gamma_c * R_cp2 * Rm_sq_cp2)
        # δ = 0, so Ric³ doesn't contribute
        # 5040 a₃ = known + ε I₆
        # I₆ = (5040 a₃ - known) / ε

        I6_val = (5040 * frac_cp2 - known) / epsilon
        print(f"    5040 × a₃ = {5040 * frac_cp2}")
        print(f"    Known terms (α,β,γ) = {known}")
        print(f"    → I₆(CP²) = {I6_val} = {float(I6_val):.10f}")

        # Verify this I₆
        a3_check = (known + epsilon * I6_val) / 5040
        print(f"    Verify: a₃ = {a3_check} = {float(a3_check):.15f}")
        print(f"    Spectral:   {frac_cp2} = {float(frac_cp2):.15f}")

        # What should I₆ be for CP² analytically?
        # For CP^n: I₆ = R_{abcd}R^{cd}_{ef}R^{ef}_{ab}
        # With R = (H/4)(g⊗g + J⊗J + 2J⊗J) and H = 2 (for R_K=6, n=2):
        # This is 4 + 2×3 = 10 terms... complex computation
        # But we expect a nice rational answer.
        print(f"\n    I₆(CP²) = {I6_val}")


if __name__ == '__main__':
    main()
