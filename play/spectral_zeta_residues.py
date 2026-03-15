#!/usr/bin/env python3
"""
BST — Spectral zeta function residues from corrected a₃

The spectral zeta function ζ_Δ(s) = Σ λ_k^{-s} on a compact manifold M^d
has poles at s = d/2 - k (k = 0, 1, 2, ...) with residues determined by
the Seeley-DeWitt coefficients a_k:

  Res_{s=d/2-k} ζ_Δ(s) = a_k(M) × Vol(M) / [(4π)^{d/2} Γ(d/2-k)]

For Q⁵ (d=10) and Q³ (d=6), compute these residues with the corrected a₃.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import factorial


def gamma_at_integer(n):
    """Γ(n) for positive integer n."""
    return Fraction(factorial(n - 1))


def gamma_at_half_integer(n_half):
    """Γ(n/2) for positive integer n, via Γ(1/2)=√π, Γ(n/2)=(n/2-1)Γ(n/2-1)."""
    # Returns (rational part, power of √π)
    # Γ(1/2) = √π
    # Γ(3/2) = (1/2)√π
    # Γ(5/2) = (3/4)√π ... wait, Γ(5/2) = (3/2)(1/2)√π = 3√π/4
    # Γ(n/2) = [(n-2)/2]! × √π / 2^{(n-2)/2} for odd n... not quite.
    # Let me use the recurrence directly.
    if n_half == 1:  # Γ(1/2) = √π
        return Fraction(1), 1
    elif n_half % 2 == 0:  # integer
        return Fraction(factorial(n_half // 2 - 1)), 0
    else:  # half-integer
        rat, pi_pow = gamma_at_half_integer(n_half - 2)
        return rat * Fraction(n_half - 2, 2), pi_pow


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  SPECTRAL ZETA RESIDUES FROM CORRECTED a₃")
    print("  ══════════════════════════════════════════════════════")

    # ──────────────────────────────────────────────────────
    # Q⁵: d = 10, poles at s = 5, 4, 3, 2, 1, ...
    # ──────────────────────────────────────────────────────
    print("\n  ── Q⁵ (d = 10, Killing metric) ──")
    d = 10
    # Vol(Q⁵) in Killing metric: Vol = 8π⁵/15
    Vol_Q5 = Fraction(8, 15)  # × π⁵
    print(f"  Vol(Q⁵) = {Vol_Q5}π⁵")

    # Seeley-DeWitt coefficients (Killing metric)
    a_Q5 = {
        0: Fraction(1),
        1: Fraction(5, 6),     # R/6 = 5/6
        2: Fraction(7, 54),    # Wait, need to recompute for Killing
        3: Fraction(437, 4500),  # corrected a₃
    }

    # Actually, a₂ for Q⁵ in Killing metric:
    # a₂ = (5R² - 2|Ric|² + 2|Rm|²)/360
    # R = 5, |Ric|² = 5/2, |Rm|² = 13/5
    R5 = Fraction(5)
    Ric2_5 = Fraction(5, 2)
    Rm2_5 = Fraction(13, 5)
    a2_Q5 = (5 * R5**2 - 2 * Ric2_5 + 2 * Rm2_5) / 360
    a_Q5[2] = a2_Q5

    print(f"  a₀ = {a_Q5[0]}")
    print(f"  a₁ = {a_Q5[1]} = R/6")
    print(f"  a₂ = {a_Q5[2]} = {float(a_Q5[2]):.10f}")
    print(f"  a₃ = {a_Q5[3]} = {float(a_Q5[3]):.10f}")

    # Residues: Res_{s=5-k} ζ(s) = a_k × Vol / [(4π)^5 Γ(5-k)]
    # (4π)^5 = 4⁵π⁵ = 1024π⁵
    four_pi_5 = Fraction(1024)  # × π⁵

    print(f"\n  Residues of ζ_Δ(s) on Q⁵:")
    print(f"  Res = a_k × Vol / [(4π)^5 × Γ(5-k)]")
    print(f"      = a_k × (8/15)π⁵ / [1024π⁵ × Γ(5-k)]")
    print(f"      = a_k / [1920 × Γ(5-k)]")

    for k in range(4):
        s = 5 - k
        gamma_val = gamma_at_integer(s)
        res = a_Q5[k] * Vol_Q5 / (four_pi_5 * gamma_val)
        print(f"\n  s = {s}: Res = {a_Q5[k]} × 8/15 / (1024 × {gamma_val})")
        print(f"        = {res}")
        print(f"        = {float(res):.12f}")
        # Factor nicely
        num = res.numerator
        den = res.denominator
        print(f"        = {num}/{den}")

    # ──────────────────────────────────────────────────────
    # The key residue at s = 2 (from a₃)
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  THE KEY RESIDUE AT s = 2")
    print(f"  ══════════════════════════════════════════════════════")

    res_2 = a_Q5[3] * Vol_Q5 / (four_pi_5 * gamma_at_integer(2))
    print(f"\n  Res_{{s=2}} ζ_Δ(s) = a₃ × Vol / [(4π)⁵ × Γ(2)]")
    print(f"                    = (437/4500) × (8/15) / (1024 × 1)")
    print(f"                    = {res_2}")
    print(f"                    = {float(res_2):.12f}")

    # Factor the result
    num = res_2.numerator
    den = res_2.denominator
    print(f"\n  = {num}/{den}")

    # Factorize numerator and denominator
    def factorize(n):
        if n <= 1:
            return {n: 1}
        factors = {}
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors

    print(f"  {num} = {factorize(abs(num))}")
    print(f"  {den} = {factorize(den)}")

    print(f"\n  BST content:")
    print(f"  437 = 19 × 23 (dark energy × Golay prime)")
    print(f"  The denominator encodes powers of 2, 3, 5")

    # ──────────────────────────────────────────────────────
    # Q³: d = 6, poles at s = 3, 2, 1, 0, ...
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Q³ SPECTRAL ZETA RESIDUES (d = 6, Killing metric)")
    print(f"  ══════════════════════════════════════════════════════")

    # Vol(Q³) in Killing metric
    # Q³ ⊂ CP⁴, degree 2 quadric hypersurface
    # Vol(CP^n, FS) = π^n/n!, Vol(Q^n, FS) = 2π^n/n! (degree 2)
    # Killing metric = (1/6) × FS metric? No... Killing metric has R = 3.
    # FS metric on Q³: R = n(n+1) = 12 for Q³ (standard FS on CP⁴ restricted)
    # Actually for Q³ ⊂ CP⁴ with induced FS metric: R = 2n(n+1)/(n+2)...
    # Let me use a different approach.
    #
    # Vol(Q³, Killing) from the Lie algebra:
    # The Killing metric has g = 6δ on the 6-dim tangent space.
    # Vol(Q³, Killing) = (√6)^6 × Vol(Q³, unit metric) = 6³ × Vol(Q³, unit)
    # Actually, if g_{Killing} = 6 × g_{unit}, then
    # √det(g_K) = 6^3 √det(g_unit), so Vol_K = 6³ × Vol_unit
    #
    # For Q³ = SO(5)/[SO(3)×SO(2)]:
    # Vol(G/K, Killing) = Vol(G, Killing) / Vol(K, Killing)
    # This is a standard computation. For now, let's parametrize.
    #
    # Actually, the zeta residue formula uses POINTWISE a_k:
    # Res_{s=d/2-k} = (1/(4π)^{d/2}) × (1/Γ(d/2-k)) × ∫_M a_k dvol
    # For symmetric spaces, a_k is constant, so ∫ a_k = a_k × Vol.
    #
    # Let me just compute the ratio a_k/[(4π)^{d/2} Γ(d/2-k)] × Vol
    # without fixing Vol for now.

    R3 = Fraction(3)
    Ric2_3 = Fraction(3, 2)
    Rm2_3 = Fraction(7, 3)

    a_Q3 = {
        0: Fraction(1),
        1: Fraction(3, 6),  # R/6 = 1/2
        2: (5 * R3**2 - 2 * Ric2_3 + 2 * Rm2_3) / 360,
        3: Fraction(179, 7560),
    }

    print(f"  a₀ = {a_Q3[0]}")
    print(f"  a₁ = {a_Q3[1]} = R/6 = 1/2")
    print(f"  a₂ = {a_Q3[2]} = {float(a_Q3[2]):.10f}")
    print(f"  a₃ = {a_Q3[3]} = {float(a_Q3[3]):.10f}")

    # (4π)^3 = 64π³
    four_pi_3 = Fraction(64)  # × π³
    print(f"\n  Residue ratios (× Vol/π³):")
    for k in range(4):
        s = 3 - k
        gamma_val = gamma_at_integer(s) if s > 0 else None
        if gamma_val is None:
            print(f"  s = {s}: pole of Γ — need regularization")
            continue
        ratio = a_Q3[k] / (four_pi_3 * gamma_val)
        print(f"  s = {s}: a_{k}/[(4π)³ Γ({s})] = {ratio} = {float(ratio):.12f}")

    # ──────────────────────────────────────────────────────
    # The s = 0 residue on Q³ (from a₃)
    # ──────────────────────────────────────────────────────
    print(f"\n  Key: s = 0 residue from a₃:")
    # Γ(0) has a pole, so Res_{s=0} = 0 from a₃ alone.
    # But the spectral zeta has s = 0 as a regular point (for even d).
    # Actually for d = 6: poles at s = 3, 2, 1 (from a₀, a₁, a₂).
    # s = 0 is determined by a₃ through ζ(0) = (-1)^{d/2} a_{d/2}.
    # For d = 6: ζ(0) = -a₃.
    # This gives the functional determinant: log det Δ = -ζ'(0).

    print(f"  For d = 6: ζ_Δ(0) = -a₃ × Vol = -(179/7560) × Vol(Q³)")
    print(f"  This determines the functional determinant of Δ on Q³.")

    # ──────────────────────────────────────────────────────
    # Summary
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SUMMARY: KEY SPECTRAL ZETA RESIDUES")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"\n  Q⁵ (d = 10):")
    res_s2 = a_Q5[3] * Vol_Q5 / (four_pi_5 * Fraction(1))
    print(f"    Res_{{s=2}} ζ_Δ(s) = {res_s2}")
    print(f"                     = 437/(1024 × 15 × 4500/8)")
    print(f"                     = {res_s2.numerator}/{res_s2.denominator}")
    fac_num = factorize(abs(res_s2.numerator))
    fac_den = factorize(res_s2.denominator)
    print(f"                     numerator: {fac_num}")
    print(f"                     denominator: {fac_den}")

    print(f"\n  Q³ (d = 6):")
    print(f"    ζ_Δ(0) = -a₃ × Vol = -(179/7560) × Vol(Q³)")
    print(f"    The prime 179 controls the functional determinant")

    print(f"\n  Both spectral zeta functions carry BST primes:")
    print(f"    Q⁵: 19 × 23 = 437 (from a₃ = 437/4500)")
    print(f"    Q³: 179 (prime, from a₃ = 179/7560)")


if __name__ == '__main__':
    main()
