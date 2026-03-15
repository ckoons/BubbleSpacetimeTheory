#!/usr/bin/env python3
"""
Cross-check the corrected a₃ formula on CP² (non-sphere symmetric space).

CP² spectrum (Killing metric): λ_k = k(k+2), d_k = (k+1)³
Known: a₁ = 1 → R = 6, a₂ = 31/60

Also check: S³ and S⁵ (ODD dimensions) to confirm.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import comb
from mpmath import mp, mpf, exp, pi, nstr, gamma


def spectral_a3(eigenvalues_gen, d, name, K_max=100000):
    """Compute spectral a₃ from eigenvalue generator.
    eigenvalues_gen(k) -> (eigenvalue, degeneracy)
    """
    mp.dps = 80

    # First compute a₀, a₁, a₂ from small-t behavior
    t_vals = [mpf(1) / mpf(10**k) for k in [2, 3, 4, 5, 6, 7]]

    # Compute Z(t) for each t, then F(t)
    results = {}
    for coeff_idx in range(4):  # a₀, a₁, a₂, a₃
        g_vals = []
        for t in t_vals:
            Z = mpf(0)
            for k in range(K_max):
                lam, deg = eigenvalues_gen(k)
                term = deg * exp(-lam * t)
                Z += term
                if abs(term) < mpf(10)**(-70) and k > 10:
                    break

            # Need volume normalization
            # For now, compute raw (4πt)^{d/2} Z(t)
            F = (4 * pi * t)**(d / mpf(2)) * Z
            g_vals.append(F)

        results[coeff_idx] = g_vals

    # The normalization: F(t) → Vol × [a₀ + a₁t + a₂t² + ...]
    # Identify Vol × a₀ from the leading term
    F_vals = results[0]

    # Vol × a₀ is the t→0 limit
    # Use Richardson on F_vals
    levels = [F_vals]
    for _ in range(len(F_vals) - 1):
        prev = levels[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels.append(curr)

    Vol_a0 = levels[min(2, len(levels)-1)][-1]
    print(f"\n  {name} (d={d}):")
    print(f"    Vol×a₀ = {nstr(Vol_a0, 18)}")

    # Now compute G₁(t) = [F(t) - Vol×a₀] / t
    g1_vals = [(F - Vol_a0) / t for F, t in zip(F_vals, t_vals)]
    levels1 = [g1_vals]
    for _ in range(len(g1_vals) - 1):
        prev = levels1[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels1.append(curr)
    Vol_a1 = levels1[min(2, len(levels1)-1)][-1]
    print(f"    Vol×a₁ = {nstr(Vol_a1, 18)}")

    # G₂(t) = [F(t) - Vol×a₀ - Vol×a₁×t] / t²
    g2_vals = [(F - Vol_a0 - Vol_a1 * t) / t**2 for F, t in zip(F_vals, t_vals)]
    levels2 = [g2_vals]
    for _ in range(len(g2_vals) - 1):
        prev = levels2[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels2.append(curr)
    Vol_a2 = levels2[min(2, len(levels2)-1)][-1]
    print(f"    Vol×a₂ = {nstr(Vol_a2, 18)}")

    # G₃(t) = [F(t) - Vol×a₀ - Vol×a₁×t - Vol×a₂×t²] / t³
    g3_vals = [(F - Vol_a0 - Vol_a1 * t - Vol_a2 * t**2) / t**3
               for F, t in zip(F_vals, t_vals)]
    levels3 = [g3_vals]
    for _ in range(len(g3_vals) - 1):
        prev = levels3[-1]
        curr = [(10 * prev[i+1] - prev[i]) / 9 for i in range(len(prev)-1)]
        if not curr:
            break
        levels3.append(curr)
    Vol_a3 = levels3[min(2, len(levels3)-1)][-1]
    print(f"    Vol×a₃ = {nstr(Vol_a3, 18)}")

    # Identify ratios
    a1_over_a0 = Vol_a1 / Vol_a0
    a2_over_a0 = Vol_a2 / Vol_a0
    a3_over_a0 = Vol_a3 / Vol_a0
    print(f"    a₁/a₀ = {nstr(a1_over_a0, 18)}")
    print(f"    a₂/a₀ = {nstr(a2_over_a0, 18)}")
    print(f"    a₃/a₀ = {nstr(a3_over_a0, 18)}")

    # Try fraction identification for a₃/a₀
    val = float(a3_over_a0)
    found = None
    for den in range(1, 20000):
        num = round(val * den)
        if abs(num / den - val) < 1e-6:
            found = Fraction(num, den)
            break
    if found:
        print(f"    → a₃/a₀ = {found} = {float(found):.15f}")
    else:
        print(f"    → a₃/a₀ ≈ {val:.15f} (fraction not found)")

    return a3_over_a0, found


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  CROSS-CHECK: corrected a₃ formula on CP² and odd spheres")
    print("  ══════════════════════════════════════════════════════")

    # ── CP² ──
    # Killing metric: λ_k = k(k+2), d_k = (k+1)³
    def cp2_eigen(k):
        return (k * (k + 2), (k + 1)**3)

    a3_cp2, frac_cp2 = spectral_a3(cp2_eigen, 4, "CP²")

    # ── S³ (odd-dimensional sphere) ──
    def s3_eigen(ell):
        d = 3
        dk = comb(d + ell, d)
        if ell >= 2:
            dk -= comb(d + ell - 2, d)
        return (ell * (ell + d - 1), dk)

    a3_s3, frac_s3 = spectral_a3(s3_eigen, 3, "S³")

    # ── S⁵ ──
    def s5_eigen(ell):
        d = 5
        dk = comb(d + ell, d)
        if ell >= 2:
            dk -= comb(d + ell - 2, d)
        return (ell * (ell + d - 1), dk)

    a3_s5, frac_s5 = spectral_a3(s5_eigen, 5, "S⁵")

    # ══════════════════════════════════════════════════════
    # CHECK CORRECTED FORMULA ON ODD SPHERES
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  CORRECTED FORMULA CHECK ON ODD SPHERES")
    print(f"  ══════════════════════════════════════════════════════")

    # Corrected coefficients (from even spheres):
    alpha = Fraction(35, 9)
    beta = Fraction(-14, 3)
    gamma = Fraction(34, 9)
    delta = Fraction(0)
    epsilon = Fraction(8, 3)

    for d, frac, label in [(3, frac_s3, "S³"), (5, frac_s5, "S⁵")]:
        R = d * (d - 1)
        Ric_sq = (d - 1)**2 * d
        Rm_sq = 2 * d * (d - 1)
        Ric3 = (d - 1)**3 * d
        I6 = 4 * d * (d - 1)

        a3_formula = (alpha * R**3 + beta * R * Ric_sq
                      + gamma * R * Rm_sq + delta * Ric3
                      + epsilon * I6) / 5040

        print(f"\n  {label} (d={d}):")
        print(f"    Spectral a₃  = {frac} = {float(frac):.15f}" if frac else f"    Spectral a₃ ≈ ?")
        print(f"    Corrected a₃ = {a3_formula} = {float(a3_formula):.15f}")
        if frac:
            print(f"    Match: {frac == a3_formula}")

    # ══════════════════════════════════════════════════════
    # CP² ANALYSIS
    # ══════════════════════════════════════════════════════
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  CP² CURVATURE INVARIANT EXTRACTION")
    print(f"  ══════════════════════════════════════════════════════")

    if frac_cp2:
        # CP² Killing metric: R = 6, Ric = (3/2)g, d = 4
        R_cp2 = 6
        Ric_sq_cp2 = Fraction(9)  # (3/2)² × 4
        Ric3_cp2 = Fraction(27, 2)  # (3/2)³ × 4

        # a₃_spectral = [α R³ + β R|Ric|² + γ R|Rm|² + δ Ric³ + ε I₆] / 5040
        # We know all except |Rm|² and I₆

        # From a₂ = (5R² - 2|Ric|² + 2|Rm|²) / 360
        # a₂ = 31/60 (confirmed spectrally)
        # 31/60 = (180 - 18 + 2|Rm|²) / 360 = (162 + 2|Rm|²) / 360
        # 31 × 6 = 162 + 2|Rm|² → 186 = 162 + 2|Rm|² → |Rm|² = 12
        Rm_sq_cp2 = 12

        known_terms = (alpha * R_cp2**3 + beta * R_cp2 * Ric_sq_cp2
                       + gamma * R_cp2 * Rm_sq_cp2 + delta * Ric3_cp2)

        # 5040 a₃ = known_terms + ε I₆
        # ε I₆ = 5040 a₃ - known_terms
        I6_needed = (5040 * frac_cp2 - known_terms) / epsilon
        print(f"    R = {R_cp2}")
        print(f"    |Ric|² = {Ric_sq_cp2}")
        print(f"    |Rm|² = {Rm_sq_cp2}")
        print(f"    Ric³ = {Ric3_cp2}")
        print(f"    Known terms = {known_terms} = {float(known_terms):.10f}")
        print(f"    5040 × a₃ = {5040 * frac_cp2} = {float(5040 * frac_cp2):.10f}")
        print(f"    → I₆ = {I6_needed} = {float(I6_needed):.10f}")

        # Verify: compute I₆ analytically for CP²
        # For CP² (Fubini-Study with H):
        # R_{abcd} = (H/4)(g_{ac}g_{bd} - g_{ad}g_{bc} + J_{ac}J_{bd} - J_{ad}J_{bc} + 2J_{ab}J_{cd})
        # In Killing normalization with R=6 on CP² (d=4):
        # R = n(n+1)H/2 = 2×3×H/2 = 3H, so H = 2.
        #
        # |Rm|² = H²/16 × (g⊗g terms)²
        # This requires careful computation...
        # Already verified |Rm|² = 12 from a₂.
        #
        # I₆ for CP^n is known: I₆ = (3n²+3n-2)H³/(4×n×something)
        # Let me just check if I₆ = 36 or some other nice number.
        print(f"\n    Check: is I₆ a nice number? I₆ = {I6_needed}")

        # Also compute Vassilevich a₃ for CP²
        alpha_V = Fraction(35, 9)
        beta_V = Fraction(-14, 3)
        gamma_V = Fraction(14, 3)
        delta_V = Fraction(-208, 9)
        epsilon_V = Fraction(64, 3)

        a3_V = (alpha_V * R_cp2**3 + beta_V * R_cp2 * Ric_sq_cp2
                + gamma_V * R_cp2 * Rm_sq_cp2 + delta_V * Ric3_cp2
                + epsilon_V * I6_needed) / 5040

        print(f"\n    With this I₆:")
        print(f"    Vassilevich a₃ = {a3_V} = {float(a3_V):.15f}")
        print(f"    Spectral a₃   = {frac_cp2} = {float(frac_cp2):.15f}")
        print(f"    Corrected a₃  = {frac_cp2} (by construction)")

        # What I₆ does Vassilevich need to match spectral?
        V_known = (alpha_V * R_cp2**3 + beta_V * R_cp2 * Ric_sq_cp2
                   + gamma_V * R_cp2 * Rm_sq_cp2 + delta_V * Ric3_cp2)
        I6_for_V = (5040 * frac_cp2 - V_known) / epsilon_V
        print(f"\n    I₆ needed by Vassilevich to match = {I6_for_V} = {float(I6_for_V):.10f}")
        print(f"    I₆ from corrected formula = {I6_needed} = {float(I6_needed):.10f}")


if __name__ == '__main__':
    main()
