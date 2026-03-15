#!/usr/bin/env python3
"""
BST — Find the CORRECT a₃ formula
===================================
The Vassilevich a₃ formula disagrees with exact spectral computation on ALL
spheres tested. The a₂ formula is correct. Something is wrong with the
published a₃ coefficients (or our transcription of them).

Strategy: compute exact spectral a₃ on S^d for d=2,4,6,8,10, fit the
polynomial, and reverse-engineer the correct formula.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import factorial, comb
from mpmath import mp, mpf, exp, pi, nstr, gamma
import numpy as np


def spectral_a3_sphere(d, K_max=80000, verbose=True):
    """Compute exact a₃ on S^d (K=1) from spectrum.

    Returns Fraction (exact rational).
    """
    mp.dps = 60

    # Volume
    Vol = 2 * pi**((d + 1) / mpf(2)) / gamma((d + 1) / mpf(2))

    # Degeneracies
    def deg(ell):
        v = comb(d + ell, d)
        if ell >= 2:
            v -= comb(d + ell - 2, d)
        return v

    # Known exact a₀, a₁, a₂
    R = d * (d - 1)  # scalar curvature
    a0 = mpf(1)
    a1 = mpf(R) / 6
    # a₂ = (5R² - 2|Ric|² + 2|Rm|²) / 360
    Ric_sq = (d - 1)**2 * d
    Rm_sq = 2 * d * (d - 1)
    a2_num = 5 * R**2 - 2 * Ric_sq + 2 * Rm_sq
    a2 = mpf(a2_num) / 360

    # Compute G(t) = [F(t) - a₀ - a₁t - a₂t²] / t³ → a₃
    # F(t) = (4πt)^{d/2} Z(t) / Vol

    t_vals = [mpf(1) / mpf(10**k) for k in [3, 4, 5, 6]]
    g_vals = []

    for t in t_vals:
        Z = mpf(0)
        for ell in range(K_max):
            dk = deg(ell)
            lk = ell * (ell + d - 1)
            term = dk * exp(-lk * t)
            Z += term
            if abs(term) < mpf(10)**(-50) and ell > 10:
                break

        F = (4 * pi * t)**(d / mpf(2)) * Z / Vol
        G = (F - a0 - a1 * t - a2 * t**2) / t**3
        g_vals.append(G)

    # Richardson extrapolation
    rich_vals = []
    for i in range(len(g_vals) - 1):
        rich = (10 * g_vals[i + 1] - g_vals[i]) / 9
        rich_vals.append(rich)

    # Second Richardson
    if len(rich_vals) >= 2:
        rich2 = (10 * rich_vals[1] - rich_vals[0]) / 9
        best = rich2
    elif rich_vals:
        best = rich_vals[-1]
    else:
        best = g_vals[-1]

    if verbose:
        print(f"    d={d}: G values = {[nstr(g, 15) for g in g_vals]}")
        print(f"    Richardson = {[nstr(r, 15) for r in rich_vals]}")
        if len(rich_vals) >= 2:
            rich2 = (10 * rich_vals[1] - rich_vals[0]) / 9
            print(f"    Richardson² = {nstr(rich2, 18)}")

    # Try to identify as a simple fraction
    best_float = float(best)
    found = None
    for den in range(1, 5000):
        num = round(best_float * den)
        if abs(num / den - best_float) < 1e-10:
            found = Fraction(num, den)
            break

    if found and verbose:
        print(f"    → a₃(S^{d}) = {found} = {float(found):.15f}")

    return found, best


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  FINDING THE CORRECT a₃ FORMULA")
    print("  ══════════════════════════════════════════════════════")

    # Compute spectral a₃ for all even dimensions 2-10
    results = {}
    for d in [2, 4, 6, 8, 10]:
        print(f"\n  S^{d}:")
        frac, _ = spectral_a3_sphere(d)
        results[d] = frac

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SPECTRAL a₃ VALUES")
    print(f"  ══════════════════════════════════════════════════════")

    for d, frac in sorted(results.items()):
        P = 5040 * frac
        Q = P / (d * (d - 1))
        print(f"    S^{d}: a₃ = {frac} = {float(frac):.15f}")
        print(f"           5040×a₃ = {P}, Q(d) = 5040a₃/[d(d-1)] = {Q}")

    # Now fit the polynomial R(x) = 3 × Q(x)
    # R(x) should be degree ≤ 4 in x = d
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  POLYNOMIAL FIT: R(d) = 3 × 5040 × a₃ / [d(d-1)]")
    print(f"  ══════════════════════════════════════════════════════")

    dims = sorted(results.keys())
    R_vals = []
    for d in dims:
        R_val = 3 * 5040 * results[d] / (d * (d - 1))
        R_vals.append(R_val)
        print(f"    R({d}) = {R_val} = {float(R_val):.6f}")

    # Fit degree-4 polynomial (5 unknowns, 5 data points)
    # R(x) = c₄x⁴ + c₃x³ + c₂x² + c₁x + c₀
    A = np.array([[d**k for k in range(5)] for d in dims], dtype=float)
    b = np.array([float(R) for R in R_vals])
    coeffs = np.linalg.solve(A, b)

    print(f"\n  Polynomial coefficients:")
    for k, c in enumerate(coeffs):
        # Try to identify as fraction
        frac = Fraction(c).limit_denominator(1000)
        print(f"    c_{k} = {c:.10f} ≈ {frac} = {float(frac):.10f}")

    # Verify
    print(f"\n  Verification:")
    for d in dims:
        R_fit = sum(coeffs[k] * d**k for k in range(5))
        R_exact = float(3 * 5040 * results[d] / (d * (d - 1)))
        print(f"    R({d}): fit = {R_fit:.6f}, exact = {R_exact:.6f}, diff = {abs(R_fit - R_exact):.2e}")

    # Now reconstruct the a₃ formula
    # R(x) = 3[αx⁴ + (-2α+β)x³ + (α-2β+2γ+δ)x² + (β-2γ-2δ+2ε+η)x + (δ-2ε+4ζ-2η)]
    #       = 3αx⁴ + 3(-2α+β)x³ + 3(α-2β+2γ+δ)x² + 3(β-2γ-2δ+2ε+η)x + 3(δ-2ε+4ζ-2η)
    #
    # where 5040 a₃ = αR³ + βR|Ric|² + γR|Rm|² + δRic³ + εI₆ + ζT₁ + ηT₂

    # The Vassilevich coefficients give:
    alpha_V = Fraction(35, 9)
    beta_V = Fraction(-14, 3)
    gamma_V = Fraction(14, 3)
    delta_V = Fraction(-208, 9)
    epsilon_V = Fraction(64, 3)
    zeta_V = Fraction(16, 3)
    eta_V = Fraction(44, 9)

    # Vassilevich polynomial:
    R_V = [
        3 * (delta_V - 2 * epsilon_V + 4 * zeta_V - 2 * eta_V),  # c₀
        3 * (beta_V - 2 * gamma_V - 2 * delta_V + 2 * epsilon_V + eta_V),  # c₁
        3 * (alpha_V - 2 * beta_V + 2 * gamma_V + delta_V),  # c₂
        3 * (-2 * alpha_V + beta_V),  # c₃
        3 * alpha_V,  # c₄
    ]

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  VASSILEVICH vs SPECTRAL POLYNOMIAL")
    print(f"  ══════════════════════════════════════════════════════")

    print(f"\n  Vassilevich R(x) coefficients:")
    for k, c in enumerate(R_V):
        print(f"    c_{k} = {c} = {float(c):.10f}")

    print(f"\n  Spectral R(x) coefficients:")
    for k, c in enumerate(coeffs):
        frac = Fraction(c).limit_denominator(1000)
        print(f"    c_{k} = {frac} = {float(frac):.10f}")

    print(f"\n  Differences (spectral - Vassilevich):")
    for k in range(5):
        diff = coeffs[k] - float(R_V[k])
        frac_d = Fraction(diff).limit_denominator(1000)
        print(f"    Δc_{k} = {diff:.10f} ≈ {frac_d}")

    # Check: what polynomial do we need?
    # Compare coefficient by coefficient
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  USING EXACT FRACTIONS FOR POLYNOMIAL")
    print(f"  ══════════════════════════════════════════════════════")

    # Solve with exact fractions
    from fractions import Fraction
    dims_f = [Fraction(d) for d in dims]
    R_vals_f = [3 * 5040 * results[d] / (d * (d - 1)) for d in dims]

    # Build Vandermonde matrix with Fractions
    A_f = [[d**k for k in range(5)] for d in dims_f]
    # Solve by Gaussian elimination
    n = 5
    M = [row + [rhs] for row, rhs in zip(A_f, R_vals_f)]

    # Forward elimination
    for col in range(n):
        # Find pivot
        pivot_row = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            print("  Singular matrix!")
            return
        M[col], M[pivot_row] = M[pivot_row], M[col]
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

    print(f"\n  EXACT spectral polynomial R(d) = Σ c_k d^k:")
    for k in range(n):
        print(f"    c_{k} = {x[k]} = {float(x[k]):.15f}")

    # Verify
    print(f"\n  Verification with exact fractions:")
    for d in dims:
        R_val = sum(x[k] * Fraction(d)**k for k in range(n))
        R_expected = 3 * 5040 * results[d] / (d * (d - 1))
        print(f"    R({d}): computed = {R_val}, expected = {R_expected}, match = {R_val == R_expected}")

    print(f"\n  EXACT differences (spectral - Vassilevich):")
    for k in range(5):
        diff = x[k] - R_V[k]
        print(f"    Δc_{k} = {diff} = {float(diff):.15f}")

    # The correction polynomial is:
    # ΔR(d) = Σ Δc_k d^k
    # 5040 Δa₃ = d(d-1)/3 × ΔR(d)
    print(f"\n  Correction: 5040 × Δa₃ = d(d-1) × ΔR(d) / 3")
    for d in dims:
        da3 = Fraction(d * (d - 1), 3) * sum((x[k] - R_V[k]) * Fraction(d)**k for k in range(5))
        a3_corrected = float(results[d])
        a3_vassilevich = float(da3 / 5040 + results[d]) - float(da3 / 5040)
        print(f"    d={d}: 5040×Δa₃ = {da3}, a₃_correct = {results[d]}")

    # FINAL: what is the corrected formula?
    # The spectral polynomial gives coefficients c_k.
    # These correspond to:
    # c₄ = 3α
    # c₃ = 3(-2α + β)
    # c₂ = 3(α - 2β + 2γ + δ)
    # c₁ = 3(β - 2γ - 2δ + 2ε + η)
    # c₀ = 3(δ - 2ε + 4ζ - 2η)
    #
    # 5 equations, 7 unknowns. Two free parameters.
    # From c₄: α = c₄/3
    # From c₃: β = c₃/3 + 2α = c₃/3 + 2c₄/3
    # From c₂: 2γ + δ = c₂/3 - α + 2β = c₂/3 - c₄/3 + 2(c₃+2c₄)/3
    #           = c₂/3 + 2c₃/3 + c₄
    # From c₁: -2γ - 2δ + 2ε + η = c₁/3 - β = c₁/3 - c₃/3 - 2c₄/3
    # From c₀: δ - 2ε + 4ζ - 2η = c₀/3

    alpha_corr = x[4] / 3
    beta_corr = x[3] / 3 + 2 * alpha_corr

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  CORRECTED COEFFICIENTS (partial)")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"  From R³ coefficient: α = {alpha_corr} = {float(alpha_corr):.15f}")
    print(f"  Vassilevich α = {alpha_V} = {float(alpha_V):.15f}")
    print(f"  From R|Ric|² coefficient: β = {beta_corr} = {float(beta_corr):.15f}")
    print(f"  Vassilevich β = {beta_V} = {float(beta_V):.15f}")

    rhs_c2 = x[2] / 3 - alpha_corr + 2 * beta_corr
    print(f"\n  2γ + δ = {rhs_c2} = {float(rhs_c2):.10f}")
    print(f"  Vassilevich: 2(14/3) + (-208/9) = {2*gamma_V + delta_V} = {float(2*gamma_V + delta_V):.10f}")


if __name__ == '__main__':
    main()
