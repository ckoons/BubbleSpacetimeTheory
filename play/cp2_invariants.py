#!/usr/bin/env python3
"""
CP² curvature invariants and spectral heat kernel coefficients.
Compute EVERYTHING from the spectrum, then match to formula.

CP² = SU(3)/U(2), Killing metric.
Spectrum: λ_k = k(k+2), d_k = (k+1)³, Vol = 8π².

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from mpmath import mp, mpf, exp, pi, nstr
import numpy as np


def compute_cp2_heat_coeffs():
    """Extract a₀, a₁, a₂, a₃ from CP² spectrum."""
    mp.dps = 100
    K_max = 100000

    Vol = 8 * pi**2

    def eigen(k):
        return (k * (k + 2), (k + 1)**3)

    d = 4  # real dimension

    # Use 8 t values for robust extraction
    t_vals = [mpf(1) / mpf(10**k) for k in range(1, 9)]

    # Compute F(t) = (4πt)^{d/2} Z(t) / Vol for each t
    F_vals = []
    for t in t_vals:
        Z = mpf(0)
        for k in range(K_max):
            lam, deg = eigen(k)
            term = deg * exp(-lam * t)
            Z += term
            if abs(term) < mpf(10)**(-90) and k > 10:
                break
        F = (4 * pi * t)**(d / mpf(2)) * Z / Vol
        F_vals.append(F)

    # Extract coefficients sequentially
    # F(t) = a₀ + a₁t + a₂t² + a₃t³ + ...
    def richardson(vals):
        levels = [vals]
        for _ in range(len(vals) - 1):
            prev = levels[-1]
            curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
            if not curr:
                break
            levels.append(curr)
        # Use level 2 if available
        best_level = min(2, len(levels) - 1)
        return levels[best_level][-1], levels

    print("  ══════════════════════════════════════════════════════")
    print("  CP² SPECTRAL HEAT KERNEL COEFFICIENTS")
    print("  ══════════════════════════════════════════════════════")

    # a₀ = F(0)
    a0_val, a0_levels = richardson(F_vals)
    print(f"\n  a₀ = {nstr(a0_val, 20)}")
    # Should be 1
    a0 = mpf(1)

    # G₁(t) = [F(t) - a₀] / t → a₁
    G1_vals = [(F - a0) / t for F, t in zip(F_vals, t_vals)]
    a1_val, a1_levels = richardson(G1_vals)
    print(f"  a₁ = {nstr(a1_val, 20)}")

    # Try fraction
    a1_frac = None
    for den in range(1, 1000):
        num = round(float(a1_val) * den)
        if abs(num / den - float(a1_val)) < 1e-8:
            a1_frac = Fraction(num, den)
            break
    if a1_frac:
        print(f"       = {a1_frac} (R/6 → R = {6 * a1_frac})")
        a1 = mpf(a1_frac.numerator) / mpf(a1_frac.denominator)
    else:
        a1 = a1_val

    # G₂(t) = [F(t) - a₀ - a₁t] / t² → a₂
    G2_vals = [(F - a0 - a1 * t) / t**2 for F, t in zip(F_vals, t_vals)]
    a2_val, a2_levels = richardson(G2_vals)
    print(f"  a₂ = {nstr(a2_val, 20)}")
    print(f"       Level 1 (last 3): {[nstr(v, 15) for v in a2_levels[1][-3:]]}")
    print(f"       Level 2 (last 3): {[nstr(v, 15) for v in a2_levels[2][-3:]]}")

    a2_frac = None
    for den in range(1, 10000):
        num = round(float(a2_val) * den)
        if abs(num / den - float(a2_val)) < 1e-8:
            a2_frac = Fraction(num, den)
            break
    if a2_frac:
        print(f"       = {a2_frac} = {float(a2_frac):.15f}")
        a2 = mpf(a2_frac.numerator) / mpf(a2_frac.denominator)
    else:
        print(f"       fraction not found")
        a2 = a2_val

    # G₃(t) = [F(t) - a₀ - a₁t - a₂t²] / t³ → a₃
    G3_vals = [(F - a0 - a1 * t - a2 * t**2) / t**3 for F, t in zip(F_vals, t_vals)]
    a3_val, a3_levels = richardson(G3_vals)
    print(f"  a₃ = {nstr(a3_val, 20)}")
    print(f"       Level 0 (last 3): {[nstr(v, 15) for v in a3_levels[0][-3:]]}")
    print(f"       Level 1 (last 3): {[nstr(v, 15) for v in a3_levels[1][-3:]]}")
    print(f"       Level 2 (last 3): {[nstr(v, 15) for v in a3_levels[2][-3:]]}")

    a3_frac = None
    for den in range(1, 50000):
        num = round(float(a3_val) * den)
        if abs(num / den - float(a3_val)) < 1e-6:
            a3_frac = Fraction(num, den)
            break
    if a3_frac:
        print(f"       = {a3_frac} = {float(a3_frac):.15f}")
    else:
        print(f"       fraction not found, best = {float(a3_val):.15f}")

    return a1_frac, a2_frac, a3_frac


def compute_cp2_riemann():
    """Compute all curvature invariants of CP² from explicit Riemann tensor."""
    print("\n  ══════════════════════════════════════════════════════")
    print("  CP² CURVATURE INVARIANTS (explicit computation)")
    print("  ══════════════════════════════════════════════════════")

    d = 4  # real dimension
    H = Fraction(1)  # holomorphic sectional curvature in Killing metric

    # Kähler form in orthonormal frame {e₁, e₂, e₃, e₄}
    # J(e₁) = e₂, J(e₃) = e₄
    J = [[Fraction(0)] * d for _ in range(d)]
    J[0][1] = Fraction(1)
    J[1][0] = Fraction(-1)
    J[2][3] = Fraction(1)
    J[3][2] = Fraction(-1)

    # Riemann tensor
    # R_{abcd} = (H/4)(g_{ac}g_{bd} - g_{ad}g_{bc} + J_{ac}J_{bd} - J_{ad}J_{bc} + 2J_{ab}J_{cd})
    def R(a, b, c, dd):
        return H / 4 * (
            (1 if a == c else 0) * (1 if b == dd else 0)
            - (1 if a == dd else 0) * (1 if b == c else 0)
            + J[a][c] * J[b][dd]
            - J[a][dd] * J[b][c]
            + 2 * J[a][b] * J[c][dd]
        )

    # Ricci tensor: Ric_{ab} = Σ_c R_{acbc}
    Ric = [[Fraction(0)] * d for _ in range(d)]
    for a in range(d):
        for b in range(d):
            for c in range(d):
                Ric[a][b] += R(a, c, b, c)

    print("\n  Ricci tensor (should be (3H/2)delta_ab = (3/2)delta):")
    for a in range(d):
        for b in range(d):
            if Ric[a][b] != 0:
                print(f"    Ric[{a}][{b}] = {Ric[a][b]}")

    # Scalar curvature
    R_scalar = sum(Ric[a][a] for a in range(d))
    print(f"\n  R = {R_scalar} (expect 6)")

    # |Ric|²
    Ric_sq = sum(Ric[a][b] * Ric[a][b] for a in range(d) for b in range(d))
    print(f"  |Ric|² = {Ric_sq} (expect 9)")

    # |Rm|²
    Rm_sq = sum(R(a,b,c,dd)**2 for a in range(d) for b in range(d)
                for c in range(d) for dd in range(d))
    print(f"  |Rm|² = {Rm_sq}")

    # Ric³ = R_{ab}R^{bc}R_{ca} = Σ_{abc} Ric[a][b]Ric[b][c]Ric[c][a]
    Ric3 = Fraction(0)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                Ric3 += Ric[a][b] * Ric[b][c] * Ric[c][a]
    print(f"  Ric³ = {Ric3}")

    # I₆ = R_{abcd}R^{cd}_{ef}R^{ef}_{ab} (all lower indices in ortho frame)
    # = Σ_{abcdef} R(a,b,c,d) R(c,d,e,f) R(e,f,a,b)
    I6 = Fraction(0)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    for e in range(d):
                        for f in range(d):
                            I6 += R(a,b,c,dd) * R(c,dd,e,f) * R(e,f,a,b)
    print(f"  I₆ = {I6}")

    # Covariant derivative terms: on symmetric space, ∇R = 0
    # T₁ = |∇Rm|² = 0
    # T₂ = |∇Ric|² = 0
    print(f"  T₁ = 0 (symmetric space)")
    print(f"  T₂ = 0 (symmetric space)")

    # a₂ from formula
    a2_formula = (5 * R_scalar**2 - 2 * Ric_sq + 2 * Rm_sq) / 360
    print(f"\n  a₂ = (5R² - 2|Ric|² + 2|Rm|²)/360 = {a2_formula} = {float(a2_formula):.15f}")

    # a₃ from CORRECTED formula (spheres gave α=35/9, β=-14/3, γ=34/9, δ=0, ε=8/3)
    alpha = Fraction(35, 9)
    beta = Fraction(-14, 3)
    gamma = Fraction(34, 9)
    delta = Fraction(0)
    epsilon = Fraction(8, 3)

    a3_corrected = (alpha * R_scalar**3 + beta * R_scalar * Ric_sq
                    + gamma * R_scalar * Rm_sq + delta * Ric3
                    + epsilon * I6) / 5040
    print(f"  a₃ (corrected) = {a3_corrected} = {float(a3_corrected):.15f}")

    # a₃ from Vassilevich formula
    alpha_V = Fraction(35, 9)
    beta_V = Fraction(-14, 3)
    gamma_V = Fraction(14, 3)
    delta_V = Fraction(-208, 9)
    epsilon_V = Fraction(64, 3)

    a3_vass = (alpha_V * R_scalar**3 + beta_V * R_scalar * Ric_sq
               + gamma_V * R_scalar * Rm_sq + delta_V * Ric3
               + epsilon_V * I6) / 5040
    print(f"  a₃ (Vassilevich) = {a3_vass} = {float(a3_vass):.15f}")

    return R_scalar, Ric_sq, Rm_sq, Ric3, I6


if __name__ == '__main__':
    R, Ric_sq, Rm_sq, Ric3, I6 = compute_cp2_riemann()
    a1_frac, a2_frac, a3_frac = compute_cp2_heat_coeffs()

    print("\n  ══════════════════════════════════════════════════════")
    print("  COMPARISON")
    print("  ══════════════════════════════════════════════════════")
    if a2_frac:
        a2_formula = (5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360
        print(f"  a₂ (spectral) = {a2_frac} = {float(a2_frac):.15f}")
        print(f"  a₂ (formula)  = {a2_formula} = {float(a2_formula):.15f}")
        print(f"  Match: {a2_frac == a2_formula}")
    if a3_frac:
        alpha = Fraction(35, 9)
        beta = Fraction(-14, 3)
        gamma = Fraction(34, 9)
        delta = Fraction(0)
        epsilon = Fraction(8, 3)
        a3_corr = (alpha * R**3 + beta * R * Ric_sq
                   + gamma * R * Rm_sq + delta * Ric3
                   + epsilon * I6) / 5040
        print(f"  a₃ (spectral)   = {a3_frac} = {float(a3_frac):.15f}")
        print(f"  a₃ (corrected)  = {a3_corr} = {float(a3_corr):.15f}")
        print(f"  Match: {a3_frac == a3_corr}")
