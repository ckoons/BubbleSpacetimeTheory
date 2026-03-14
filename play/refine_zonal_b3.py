#!/usr/bin/env python3
"""
BST — Refine b₂ and b₃ from the zonal heat trace on Q⁵
=========================================================
Uses exact values for b₀ = 1/60 and b₁ = 1/12 to subtract
lower-order terms, then extracts b₂ and b₃ with higher precision.

Also computes the spectral zeta function ζ₀(s) at key points
to verify the pole structure.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import comb

# BST constants
n_C = 5
C2 = 6
c = [1, 5, 11, 13, 9, 3]


def d_k(k):
    """Zonal degeneracy."""
    return comb(k + 4, 4) * (2 * k + 5) // 5


def lam_k(k):
    """k-th eigenvalue."""
    return k * (k + 5)


def Z0(t, K_max=3000):
    """Zonal heat trace with high truncation."""
    total = 0.0
    for k in range(K_max + 1):
        lam = k * (k + 5)
        if lam * t > 250:
            break
        total += d_k(k) * np.exp(-lam * t)
    return total


def richardson(func, t0, n_levels):
    """Richardson extrapolation."""
    vals = [func(t0 / 2**k) for k in range(n_levels)]
    table = [vals[:]]
    for j in range(1, n_levels):
        new_row = []
        for i in range(n_levels - j):
            val = (2**j * table[-1][i + 1] - table[-1][i]) / (2**j - 1)
            new_row.append(val)
        table.append(new_row)
    return table[-1][0]


def main():
    print()
    print("  ══════════════════════════════════════════════════")
    print("  REFINED ZONAL COEFFICIENT EXTRACTION")
    print("  ══════════════════════════════════════════════════")

    # Exact values from initial extraction
    b0 = 1.0 / 60    # = 1/|A₅|
    b1 = 1.0 / 12    # = 1/(2C₂) ... or c₁/60

    # ──────────────────────────────────────────────────────
    # STEP 1: Verify b₁ = 1/12 exactly
    # ──────────────────────────────────────────────────────
    print(f"\n  Verify b₁ = 1/12 = {1/12:.15f}")

    def g1(t):
        return (t**3 * Z0(t) - b0) / t

    b1_extracted = richardson(g1, t0=0.02, n_levels=14)
    print(f"  b₁ extracted = {b1_extracted:.15f}")
    print(f"  Error from 1/12: {abs(b1_extracted - 1/12):.2e}")

    # Also check b₁ = c₁/60 = 5/60 = 1/12
    print(f"  c₁/60 = {c[1]/60:.15f} = 1/12 ✓")

    # ──────────────────────────────────────────────────────
    # STEP 2: Extract b₂ precisely
    # ──────────────────────────────────────────────────────
    print(f"\n  ── Extracting b₂ ──")

    def g2(t):
        return (t**3 * Z0(t) - b0 - b1 * t) / t**2

    # Multiple Richardson extrapolations with different t₀
    for t0 in [0.05, 0.02, 0.01, 0.005]:
        b2_try = richardson(g2, t0=t0, n_levels=14)
        print(f"    t₀={t0:.3f}: b₂ = {b2_try:.15f},  60b₂ = {60*b2_try:.10f}")

    # Best estimate
    b2 = richardson(g2, t0=0.01, n_levels=14)
    r2 = 60 * b2
    print(f"\n  Best b₂ = {b2:.15f}")
    print(f"  r₂ = 60b₂ = {r2:.10f}")

    # Test: is r₂ = 12 exactly?
    print(f"  r₂ - 12 = {r2 - 12:.2e}")
    print(f"  r₂ / 12 = {r2 / 12:.12f}")

    # Other candidates for r₂:
    print(f"\n  r₂ candidates:")
    print(f"    2C₂ = 12       ratio = {r2/12:.12f}")
    print(f"    c₂ + 1 = 12    ratio = {r2/12:.12f}")
    print(f"    2(n_C+1) = 12  ratio = {r2/12:.12f}")
    print(f"    c₁² - c₃ = 12  ratio = {r2/(c[1]**2 - c[3]):.12f}")
    print(f"    n_C(n_C-1)/2+2 = 12  ratio = {r2/12:.12f}")

    # ──────────────────────────────────────────────────────
    # STEP 3: Extract b₃ precisely
    # ──────────────────────────────────────────────────────
    print(f"\n  ── Extracting b₃ ──")

    # Use b₂ = 12/60 = 1/5 (exact if the identification holds)
    b2_exact = 1.0 / 5  # = 12/60

    def g3(t):
        return (t**3 * Z0(t) - b0 - b1 * t - b2_exact * t**2) / t**3

    # Multiple t₀ values
    for t0 in [0.05, 0.02, 0.01, 0.005]:
        b3_try = richardson(g3, t0=t0, n_levels=12)
        print(f"    t₀={t0:.3f}: b₃ = {b3_try:.15f},  60b₃ = {60*b3_try:.10f}")

    b3 = richardson(g3, t0=0.01, n_levels=12)
    r3 = 60 * b3
    print(f"\n  Best b₃ = {b3:.15f}")
    print(f"  r₃ = 60b₃ = {r3:.10f}")

    # Candidate identifications for r₃
    print(f"\n  r₃ candidates:")
    candidates = [
        ("c₃ × 4/5", c[3] * 4 / 5),          # 10.4
        ("c₃ × (n_C-1)/n_C", c[3] * 4 / 5),  # 10.4
        ("52/5", 52 / 5),                       # 10.4
        ("2c₁ + r", 2 * c[1] + 2 / 5),        # hmm
        ("c₂ - 1/r", c[2] - 0.5),             # 10.5
        ("10 + 2/5", 10.4),                     # 10.4
        ("c₁ + C₂ - 1/r", c[1] + C2 - 0.5),  #
        ("(c₃-1)×4/5", (c[3]-1)*4/5),         # 9.6
        ("35/r - 1", 35/2 - 1),                # 16.5
    ]
    for name, val in candidates:
        ratio = r3 / val if abs(val) > 1e-10 else float('inf')
        print(f"    {name:>20} = {val:>10.6f}  ratio = {ratio:.8f}")

    # ──────────────────────────────────────────────────────
    # STEP 4: Extract b₄
    # ──────────────────────────────────────────────────────
    print(f"\n  ── Extracting b₄ ──")

    # Use exact b₃ if we can identify it
    # Try b₃ = 52/(5×60) = 52/300 = 13/75
    b3_test = 52 / 300

    def g4_test(t):
        return (t**3 * Z0(t) - b0 - b1*t - b2_exact*t**2 - b3_test*t**3) / t**4

    for t0 in [0.05, 0.02, 0.01]:
        b4_try = richardson(g4_test, t0=t0, n_levels=10)
        print(f"    t₀={t0:.3f}: b₄ = {b4_try:.10f},  60b₄ = {60*b4_try:.6f}")

    # Also try with numerical b₃
    def g4(t):
        return (t**3 * Z0(t) - b0 - b1*t - b2_exact*t**2 - b3*t**3) / t**4

    b4 = richardson(g4, t0=0.02, n_levels=10)
    r4 = 60 * b4
    print(f"\n  Best b₄ = {b4:.10f}")
    print(f"  r₄ = 60b₄ = {r4:.6f}")

    # ──────────────────────────────────────────────────────
    # STEP 5: Spectral zeta function at key points
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════")
    print(f"  SPECTRAL ZETA FUNCTION ζ₀(s)")
    print(f"  ══════════════════════════════════════════════════")

    def zeta0(s, K_max=100000):
        """Compute ζ₀(s) = Σ_{k≥1} d_k / λ_k^s."""
        total = 0.0
        for k in range(1, K_max + 1):
            d = d_k(k)
            lam = lam_k(k)
            term = d / lam**s
            total += term
            if abs(term / total) < 1e-14:
                break
        return total

    # The poles of ζ₀(s) are at s = 3, 5/2, 2, 3/2, 1, 1/2
    # (since d_k ~ k^5 and λ_k ~ k², the sum ~Σ k^{5-2s})
    # At integer and half-integer points away from poles:
    print(f"\n  ζ₀(s) at regular points:")
    for s in [4.0, 3.5, 3.25, 3.1]:
        val = zeta0(s)
        print(f"    ζ₀({s:.2f}) = {val:.10f}")

    # Near the pole at s=3: ζ₀(s) ~ Res/(s-3) + finite part
    # Res_{s=3} ζ₀ = b₀/Γ(3) = (1/60)/2 = 1/120
    print(f"\n  Near pole at s = 3:")
    print(f"    Res = b₀/Γ(3) = (1/60)/2 = {1/120:.10f}")
    for eps in [0.1, 0.01, 0.001]:
        val = zeta0(3 + eps)
        res_est = val * eps  # ζ₀ ~ Res/ε near pole
        print(f"    ζ₀(3+{eps:.3f}) = {val:.6f},  "
              f"ε × ζ₀ = {res_est:.8f} (vs 1/120 = {1/120:.8f})")

    # ──────────────────────────────────────────────────────
    # STEP 6: Cross-check via direct moment computation
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════")
    print(f"  BERNOULLI MOMENT ANALYSIS")
    print(f"  ══════════════════════════════════════════════════")

    # The expansion t³Z₀(t) = Σ_m b_m t^m can also be understood via:
    # Z₀(t) = ∫₀^∞ ρ(λ) e^{-λt} dλ  (formally)
    # where ρ(λ) = Σ_k d_k δ(λ - λ_k) is the spectral measure.
    #
    # Then t³Z₀(t) = ∫₀^∞ ρ(λ) t³ e^{-λt} dλ
    # and the coefficients b_m involve the spectral moments.

    # Instead, let me check if:
    # b_m = Σ_{k≥0} d_k × P_m(λ_k) for some polynomials P_m
    # arising from the asymptotic expansion.

    # Direct computation of the "regularized" b_k:
    # From the Euler-Maclaurin formula, the leading integral gives
    # b₀ = 1/60 exactly. The corrections involve:
    #
    # d(x) = (x+1)(x+2)(x+3)(x+4)(2x+5)/120
    # λ(x) = x(x+5) = (x+5/2)² - 25/4
    #
    # Let me compute the integral analytically:
    # I(t) = ∫₀^∞ d(x) e^{-x(x+5)t} dx

    # With substitution u = x√t:
    # I(t) = (1/√t) ∫₀^∞ d(u/√t) e^{-u²-5u√t} du/???

    # Actually, let me just compute the integral directly numerically:
    from scipy.integrate import quad

    def integrand(x, t):
        d = (x+1)*(x+2)*(x+3)*(x+4)*(2*x+5)/120
        return d * np.exp(-x*(x+5)*t)

    print(f"\n  Integral I(t) = ∫₀^∞ d(x) e^{{-x(x+5)t}} dx:")
    for t in [0.01, 0.001, 0.0001]:
        I_val, _ = quad(integrand, 0, np.inf, args=(t,))
        Z_val = Z0(t)
        diff = Z_val - I_val
        print(f"    t={t:.4f}: I = {I_val:.6f}, Z₀ = {Z_val:.6f}, "
              f"Z₀-I = {diff:.6f}")

    # The difference Z₀ - I comes from the Euler-Maclaurin corrections:
    # Z₀ - I = f(0)/2 + B₂f'(0)/2! + B₄f'''(0)/4! + ...
    # where f(x) = d(x) e^{-λ(x)t} and B_k are Bernoulli numbers.

    # f(0) = d(0) e^0 = 1 (trivial rep)
    # So the first correction is f(0)/2 = 1/2.
    print(f"\n  Euler-Maclaurin: first correction = f(0)/2 = d(0)/2 = 1/2")
    for t in [0.01, 0.001, 0.0001]:
        I_val, _ = quad(integrand, 0, np.inf, args=(t,))
        Z_val = Z0(t)
        diff = Z_val - I_val
        print(f"    t={t:.4f}: Z₀-I = {diff:.6f}, Z₀-I-1/2 = {diff-0.5:.6f}")

    # The integral itself:
    # I(t) = ∫₀^∞ d(x) e^{-x(x+5)t} dx
    # Substitute x = (u - 5/2) where u = x + 5/2:
    # x(x+5) = u² - 25/4, x = u - 5/2
    # I(t) = e^{25t/4} ∫_{5/2}^∞ d(u-5/2) e^{-u²t} du

    # For large u, d(u-5/2) ~ 2u⁵/120 = u⁵/60
    # I(t) ~ e^{25t/4}/60 ∫_{5/2}^∞ u⁵ e^{-u²t} du

    # The integral ∫₀^∞ u⁵ e^{-u²t} du = Γ(3)/(2t³) = 1/t³
    # So I(t) ~ e^{25t/4}/(60t³)

    # And t³I(t) ~ e^{25t/4}/60 = (1/60)(1 + 25t/4 + ...)

    # This gives the INTEGRAL contribution:
    # b₀^{int} = 1/60
    # b₁^{int} = 25/(4×60) = 5/48

    # But our total b₁ = 1/12 = 5/60 = 4/48. And 5/48 ≠ 4/48.
    # The difference must come from the Euler-Maclaurin corrections.

    print(f"\n  ── Integral expansion analysis ──")
    print(f"    t³ I(t) ~ (1/60) exp(25t/4)")
    print(f"    Integral b₁ = 25/(4×60) = {25/(4*60):.10f} = 5/48")
    print(f"    Total b₁    = 1/12 = {1/12:.10f} = 5/60")
    print(f"    Difference  = {1/12 - 25/(4*60):.10f} = {1/12 - 25/240:.10f}")
    print(f"                = -1/240 = -B₂ × d'(0) term??")

    # Check: 1/12 - 5/48 = 4/48 - 5/48 = -1/48
    print(f"    1/12 - 5/48 = {1/12 - 5/48} = -1/48")

    # ──────────────────────────────────────────────────────
    # STEP 7: Compute t³I(t) expansion exactly
    # ──────────────────────────────────────────────────────
    print(f"\n  ── Exact integral expansion via Gaussian moments ──")

    # I(t) = ∫₀^∞ d(x) e^{-x(x+5)t} dx
    # = ∫₀^∞ [(x+1)(x+2)(x+3)(x+4)(2x+5)/120] e^{-x(x+5)t} dx
    #
    # Let φ(x) = x(x+5) = x² + 5x. Complete the square: φ = (x+5/2)² - 25/4.
    # Let u = (x + 5/2)√t, then x = u/√t - 5/2, dx = du/√t.
    #
    # I(t) = e^{25t/4}/√t ∫_{(5/2)√t}^∞ g(u/√t - 5/2) e^{-u²} du / √t
    #
    # where g(x) = d(x) = (x+1)(x+2)(x+3)(x+4)(2x+5)/120.

    # For small t: the lower limit → 0, and g(u/√t - 5/2) expands in powers of √t.
    # The leading term: g(u/√t) ~ (u/√t)⁵ × 2/120 = u⁵/(60 t^{5/2})
    # So I(t) ~ e^{25t/4} × (1/t) × ∫₀^∞ u⁵/(60t^{5/2}) e^{-u²} du
    #         = e^{25t/4} × 1/(60 t^{7/2}) × Γ(3)/2
    #         = e^{25t/4} × 1/(60 t^{7/2}) × 1
    # Wait, ∫₀^∞ u⁵ e^{-u²} du = Γ(3)/2 = 1.

    # I(t) = e^{25t/4} / (60t³) × [1 + corrections in √t]

    # The corrections come from expanding g(u/√t - 5/2) in powers of 5/(2u/√t).
    # This gives a series in t^{1/2} if d(x) is not symmetric.

    # Wait, but our numerical extraction gives INTEGER powers of t (no √t terms).
    # This means the half-integer corrections must cancel!

    # This is because on a symmetric space, the heat trace expansion
    # has only integer powers of t (Minakshisundaram-Pleijel).

    # Let me just compute the moments numerically to get the exact expansion.
    # Compute t³I(t) at many small t and fit polynomial:

    t_vals = np.logspace(-5, -2, 200)
    I_vals = np.array([t**3 * quad(integrand, 0, np.inf, args=(t,))[0]
                        for t in t_vals])

    # Fit polynomial of degree 4
    coeffs_I = np.polyfit(t_vals, I_vals, 4)[::-1]
    print(f"\n  t³I(t) polynomial fit:")
    for k, ck in enumerate(coeffs_I):
        print(f"    c_{k}^int = {ck:.12f}")

    # EM corrections: Z₀ = I + f(0)/2 + Bernoulli terms
    # t³(Z₀ - I) should give the EM corrections
    print(f"\n  EM corrections t³(Z₀ - I):")
    EM_vals = np.array([t**3 * (Z0(t) - quad(integrand, 0, np.inf, args=(t,))[0])
                         for t in t_vals[::10]])
    for k, t in enumerate(t_vals[::10]):
        print(f"    t={t:.5f}: t³(Z₀-I) = {EM_vals[k]:.10f}")

    # ──────────────────────────────────────────────────────
    # SUMMARY
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════")
    print(f"  SUMMARY OF COEFFICIENTS")
    print(f"  ══════════════════════════════════════════════════")
    print(f"  b₀ = 1/60       (exact)  = 1/|A₅|")
    print(f"  b₁ = 1/12       (exact)  = c₁/60 = 5/60")
    print(f"  b₂ = {b2:.12f}   r₂ = {r2:.8f} ≈ 12 = 2C₂")
    print(f"  b₃ = {b3:.12f}   r₃ = {r3:.8f}")
    print(f"  b₄ = {b4:.12f}   r₄ = {r4:.8f}")
    print(f"\n  Pattern (r_k = 60b_k):")
    print(f"    r₀ = 1      = 1")
    print(f"    r₁ = 5      = c₁ = n_C")
    print(f"    r₂ = 12     = 2C₂ = c₁² - c₃")
    print(f"    r₃ = {r3:.4f}")


if __name__ == '__main__':
    main()
