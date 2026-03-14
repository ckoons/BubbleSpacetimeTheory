#!/usr/bin/env python3
"""
BST — Plancherel Measure Taylor Expansion for D_{IV}^5
=========================================================
Computes the Taylor expansion of |c(iν)|⁻² for the B₂ root system
with multiplicities (m_s=3, m_l=1), then extracts the Seeley-DeWitt
coefficients b_k via Gaussian integration.

This is the "key open calculation" from BST_SeeleyDeWitt_ChernConnection.md §10.3.

Root system B₂ with positive roots (standard coordinates):
  e₁       (short, m=3)
  e₂       (short, m=3)
  e₁ - e₂  (long,  m=1)
  e₁ + e₂  (long,  m=1)

Harish-Chandra c-function factor for root α, argument s = ⟨ν, α^∨⟩, mult m:
  c_α(s) = Γ(is/2) / Γ((is + m)/2)

Plancherel density:
  |c(iν)|⁻² = ∏_{α>0} |c_α(iν)|⁻²

Using:
  |Γ(ix)|² = π/(x sinh πx)
  |Γ(ix + 1/2)|² = π/cosh πx
  |Γ(ix + 3/2)|² = (x² + 1/4) π/cosh πx

We get:
  Short root e_i (coroot 2e_i, s=2ν_i):
    |c_{e_i}|⁻² = (ν_i² + 1/4) ν_i tanh(πν_i)

  Long root e₁±e₂ (coroot e₁±e₂, s=ν₁±ν₂):
    |c_{e₁±e₂}|⁻² = u_± tanh(πu_±),  u_± = (ν₁±ν₂)/2

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from scipy.special import gamma as Gamma
from scipy.integrate import dblquad
from fractions import Fraction


# ═══════════════════════════════════════════════════════════════════
# EXACT PLANCHEREL DENSITY
# ═══════════════════════════════════════════════════════════════════

def plancherel_density(nu1, nu2):
    """
    Compute |c(iν)|⁻² for D_{IV}^5 at spectral parameter (ν₁, ν₂).

    Uses the closed-form expressions:
      Short: (ν² + 1/4) ν tanh(πν)
      Long:  u tanh(πu) where u = (ν₁±ν₂)/2
    """
    # Short roots: e₁, e₂
    def short_factor(nu):
        if abs(nu) < 1e-15:
            return 0.0
        return (nu**2 + 0.25) * nu * np.tanh(np.pi * nu)

    # Long roots: e₁±e₂
    def long_factor(u):
        if abs(u) < 1e-15:
            return 0.0
        return u * np.tanh(np.pi * u)

    u_plus = (nu1 + nu2) / 2
    u_minus = (nu1 - nu2) / 2

    return (short_factor(nu1) * short_factor(nu2) *
            long_factor(u_plus) * long_factor(u_minus))


def plancherel_density_leading(nu1, nu2):
    """
    Leading polynomial part of |c(iν)|⁻² (replacing tanh → πx).
    This is the "polynomial approximation" valid for small ν.
    """
    # Short: (ν² + 1/4) ν × πν = π ν² (ν² + 1/4)
    # Long:  u × πu = π u²
    s1 = np.pi * nu1**2 * (nu1**2 + 0.25)
    s2 = np.pi * nu2**2 * (nu2**2 + 0.25)
    u_plus = (nu1 + nu2) / 2
    u_minus = (nu1 - nu2) / 2
    l_plus = np.pi * u_plus**2
    l_minus = np.pi * u_minus**2

    return s1 * s2 * l_plus * l_minus


# ═══════════════════════════════════════════════════════════════════
# TAYLOR EXPANSION OF EACH FACTOR
# ═══════════════════════════════════════════════════════════════════

def tanh_coefficients(N):
    """
    Compute coefficients of tanh(z) = Σ_{k=0}^{N} a_k z^{2k+1}.

    tanh(z) = Σ_{n≥1} 2^{2n}(2^{2n}-1) B_{2n} z^{2n-1} / (2n)!
    """
    from math import factorial
    # Bernoulli numbers
    B = [Fraction(0)] * (2 * N + 3)
    B[0] = Fraction(1)
    for m in range(1, len(B)):
        B[m] = Fraction(0)
        for k in range(m):
            B[m] -= Fraction(comb(m + 1, k)) * B[k]
        B[m] /= Fraction(m + 1)

    from math import comb
    coeffs = []
    for n in range(1, N + 2):
        idx = 2 * n
        b2n = B[idx]
        val = Fraction(2**idx * (2**idx - 1)) * b2n / Fraction(factorial(idx))
        coeffs.append(val)
    return coeffs


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  PLANCHEREL MEASURE TAYLOR EXPANSION FOR D_{IV}^5")
    print("  ══════════════════════════════════════════════════════")

    # ──────────────────────────────────────────────────────
    # STEP 1: Verify the closed-form Plancherel density
    # ──────────────────────────────────────────────────────
    print(f"\n  Step 1: Verify closed-form expression")
    print(f"  |c(iν)|⁻² = S(ν₁)·S(ν₂)·L(u₊)·L(u₋)")
    print(f"  S(ν) = (ν²+1/4)·ν·tanh(πν)  [short root, m=3]")
    print(f"  L(u) = u·tanh(πu)            [long root, m=1]")

    # Compare with direct Gamma function computation
    print(f"\n  Comparing closed form vs Gamma function:")
    for nu1, nu2 in [(0.5, 0.2), (1.0, 0.3), (2.0, 1.0)]:
        # Closed form
        cf = plancherel_density(nu1, nu2)

        # Gamma function computation
        def c_inv_sq(z, m):
            num = abs(Gamma(complex(m / 2, z / 2)))**2
            den = abs(Gamma(complex(0, z / 2)))**2
            return num / den if den > 0 else float('inf')

        gf = (c_inv_sq(2 * nu1, 3) * c_inv_sq(2 * nu2, 3) *
              c_inv_sq(nu1 - nu2, 1) * c_inv_sq(nu1 + nu2, 1))

        ratio = cf / gf if gf > 0 else float('inf')
        print(f"    ({nu1:.1f}, {nu2:.1f}): closed = {cf:.8f}, "
              f"Gamma = {gf:.8f}, ratio = {ratio:.10f}")

    # ──────────────────────────────────────────────────────
    # STEP 2: Small-ν behavior and power counting
    # ──────────────────────────────────────────────────────
    print(f"\n  Step 2: Small-ν power law")

    # Leading behavior: |c|⁻² ~ C × ν₁²ν₂²(ν₁²-ν₂²)²
    # times (ν₁²+1/4)(ν₂²+1/4) from the short root "mass" terms
    # Leading pure polynomial: π⁴/256 × (ν₁²+1/4)(ν₂²+1/4) × ν₁²ν₂²(ν₁²-ν₂²)²

    # Check power law at small ν with ν₁ = 2ν₂:
    for scale in [0.1, 0.01, 0.001]:
        nu1, nu2 = 2 * scale, scale
        val = plancherel_density(nu1, nu2)
        lead = plancherel_density_leading(nu1, nu2)
        print(f"    ν₁={nu1:.3f}, ν₂={nu2:.3f}: "
              f"|c|⁻² = {val:.4e}, leading = {lead:.4e}, "
              f"ratio = {val/lead:.8f}")

    # ──────────────────────────────────────────────────────
    # STEP 3: Compute Gaussian moments for b_k extraction
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print("  Step 3: Heat trace on D_IV^5 via Plancherel")
    print(f"  ══════════════════════════════════════════════════════")

    # K(t) = ∫∫ e^{-(ν₁²+ν₂²+|ρ|²)t} |c(iν)|⁻² dν₁ dν₂
    # over a*₊ (the Weyl chamber: ν₁ > ν₂ > 0 for B₂)
    # |ρ|² = (5/2)² + (3/2)² = 25/4 + 9/4 = 34/4 = 17/2

    rho_sq = 17.0 / 2  # |ρ|² = 17/2
    print(f"\n  ρ = (5/2, 3/2), |ρ|² = {rho_sq}")

    # (4πt)⁵ K(t) = e^{-|ρ|²t} Σ b_k t^k
    #
    # Method: compute I(t) = ∫∫_{ν₁>ν₂>0} e^{-|ν|²t} |c(iν)|⁻² dν₁dν₂
    # Then (4πt)⁵ I(t) = Σ b_k t^k (after removing e^{-|ρ|²t})
    #
    # For small t: substitute ν = u/√t, get integrals of |c(iu/√t)|⁻²

    # Direct numerical integration of I(t) for several t values
    print(f"\n  Computing I(t) = ∫∫_{{ν₁>ν₂>0}} e^{{-|ν|²t}} |c(iν)|⁻² dν₁dν₂:")

    def integrand(nu2, nu1, t):
        """Integrand for the Weyl chamber integral (ν₁ > ν₂ > 0)."""
        val = np.exp(-(nu1**2 + nu2**2) * t) * plancherel_density(nu1, nu2)
        return val

    t_values = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    I_values = []

    for t in t_values:
        # Integration limits: ν₁ from 0 to ∞, ν₂ from 0 to ν₁
        # Use finite upper limit; the Gaussian decay ensures convergence
        nu_max = min(20.0 / np.sqrt(t), 100.0)
        I_val, err = dblquad(
            integrand,
            0, nu_max,       # ν₁ limits
            0, lambda nu1: nu1,  # ν₂ from 0 to ν₁
            args=(t,),
            epsabs=1e-10, epsrel=1e-10
        )
        I_values.append(I_val)
        # Compute (4πt)⁵ I(t)
        norm = (4 * np.pi * t)**5 * I_val
        print(f"    t = {t:.2f}: I(t) = {I_val:.6e}, "
              f"(4πt)⁵ I(t) = {norm:.8f}")

    # ──────────────────────────────────────────────────────
    # STEP 4: Extract b_k from the ratio
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 4: Extract b_k coefficients")
    print(f"  ══════════════════════════════════════════════════════")

    # We have (4πt)⁵ I(t) → b₀ as t → 0
    # The expansion: (4πt)⁵ I(t) = b₀ + b₁t + b₂t² + ...
    # b₀ = (4π)⁵ × ∫ [leading coeff of |c|⁻² as poly in ν] × Gaussian moments

    # b₀ computation: the leading term of |c(iν)|⁻² is degree 8
    # (each of 4 roots contributes degree 2).
    #
    # |c|⁻² ~ π⁴ × (ν₁² + 1/4)ν₁² × (ν₂² + 1/4)ν₂² × (ν₁²-ν₂²)²/16
    #        = (π⁴/16) × ν₁²ν₂² × (ν₁² + 1/4)(ν₂² + 1/4)(ν₁²-ν₂²)²
    #
    # Hmm wait, that includes degree-4 terms from (ν²+1/4). The PURE leading
    # is degree 12: (ν₁⁴·ν₂⁴·(ν₁²-ν₂²)²) × π⁴. But that's wrong too.
    #
    # Let me reconsider. For small ν:
    # S(ν) = (ν²+1/4)·ν·tanh(πν) ≈ (ν²+1/4)·π·ν² = πν²(ν²+1/4)
    # L(u) = u·tanh(πu) ≈ πu²
    #
    # Product: π⁴ × ν₁²(ν₁²+1/4) × ν₂²(ν₂²+1/4) × u₊² × u₋²
    # where u₊ = (ν₁+ν₂)/2, u₋ = (ν₁-ν₂)/2
    # u₊²u₋² = (ν₁²-ν₂²)²/16
    #
    # So leading: (π⁴/16) × ν₁²(ν₁²+1/4) × ν₂²(ν₂²+1/4) × (ν₁²-ν₂²)²
    #
    # The minimum degree is: 2+0+2+0+4 = 8 (taking the 1/4 from each short root factor)
    # = π⁴/16 × (1/16) × ν₁²ν₂²(ν₁²-ν₂²)² [minimum]
    # But actually (ν₁²+1/4) = ν₁² + 1/4, so the min degree in ν₁ from this factor is 0 (constant 1/4).
    # So the min degree 8 pieces: (1/4)·ν₁² × (1/4)·ν₂² × u₊²u₋²
    # = (1/16)ν₁²ν₂²(ν₁²-ν₂²)²/16 = ν₁²ν₂²(ν₁²-ν₂²)²/256
    # Full leading: (π⁴/16) × (ν₁²ν₂²(ν₁²-ν₂²)²)/16 × ...
    #
    # Hmm, I'm confusing myself. Let me just track the degrees carefully.

    # S(ν) = Σ s_k ν^{2k} where the leading is s₁ ν² = (π/4)ν²
    # L(u) = Σ l_k u^{2k} where the leading is l₁ u² = π u²
    #
    # The product P = S(ν₁)S(ν₂)L(u₊)L(u₋) has leading:
    # (π/4)²π² × ν₁²ν₂²u₊²u₋² = (π⁴/16) × ν₁²ν₂²(ν₁²-ν₂²)²/4
    # Wait: u₊² = (ν₁+ν₂)²/4, u₋² = (ν₁-ν₂)²/4
    # u₊²u₋² = (ν₁+ν₂)²(ν₁-ν₂)²/16 = (ν₁²-ν₂²)²/16
    #
    # Leading P = (π⁴/16) × ν₁²ν₂² × (ν₁²-ν₂²)²/16
    #           = π⁴/(256) × ν₁²ν₂²(ν₁²-ν₂²)²

    # Polynomial ν₁²ν₂²(ν₁²-ν₂²)² = ν₁²ν₂²(ν₁⁴-2ν₁²ν₂²+ν₂⁴)
    #                                = ν₁⁶ν₂² - 2ν₁⁴ν₂⁴ + ν₁²ν₂⁶

    # b₀ = (4π)⁵ × ∫∫_{ν₁>ν₂>0} P_leading(ν₁,ν₂) × e^{-|ν|²} dν₁dν₂ / ???

    # Actually, I need to be more careful about the Weyl chamber integral.
    # The heat trace K(t) includes a factor 1/|W| = 1/8 (Weyl group of B₂).
    # So I should integrate over ALL of ℝ² (not just the Weyl chamber)
    # and divide by |W| = 8. Or equivalently, integrate over the Weyl chamber
    # without the 1/|W| factor.

    # The Plancherel formula for G:
    # K(t, o, o) = (1/|W|) ∫_{a*} e^{-(|ν|²+|ρ|²)t} |c(iν)|⁻² dν₁dν₂
    # where the integral is over ALL of a* (not just the Weyl chamber),
    # and |c(iν)|⁻² is W-invariant.
    #
    # Since |c(iν)|⁻² is W-invariant and W has order 8:
    # K(t) = (1/8) × 8 × ∫_{ν₁>ν₂>0} = ∫_{ν₁>ν₂>0}
    #
    # Wait, the Weyl chamber for B₂ is ν₁ > ν₂ > 0, which is 1/8 of ℝ².
    # So K(t) = ∫_{ν₁>ν₂>0} e^{-(|ν|²+|ρ|²)t} |c(iν)|⁻² dν₁dν₂.

    # Actually, I should use the standard normalization. Let me just compute
    # (4πt)⁵ K(t) and extract b₀ from the t→0 limit.

    # For the (4πt)⁵ normalization to give b₀ = 1 (unit volume), we need
    # (4πt)⁵ × I(t) → Vol_{D} × something.

    # Let me just compute the ratio numerically.

    norms = [(4 * np.pi * t)**5 * I for t, I in zip(t_values, I_values)]
    print(f"\n  b₀ estimation from (4πt)⁵ I(t):")
    for t, n in zip(t_values, norms):
        print(f"    t = {t:.2f}: (4πt)⁵I = {n:.8f}")

    # The b₀ should be Vol(D_{IV}^5) × |W| or some normalization.
    # Vol(D_{IV}^5) = π⁵/1920 (Hua's formula)
    vol_D = np.pi**5 / 1920
    vol_Q = 8 * np.pi**5 / 15  # Compact dual volume
    print(f"\n  Vol(D_IV^5) = π⁵/1920 = {vol_D:.8f}")
    print(f"  Vol(Q⁵)_round = 8π⁵/15 = {vol_Q:.8f}")
    print(f"  Ratio Q/D = 2^10 = {vol_Q/vol_D:.4f}")

    # ──────────────────────────────────────────────────────
    # STEP 5: Direct b₀ computation via Gaussian integral
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 5: b₀ from leading Gaussian integral")
    print(f"  ══════════════════════════════════════════════════════")

    # b₀ = (4π)⁵ × lim_{t→0} t⁵ ∫ e^{-|ν|²t} |c|⁻² dν₁dν₂
    #    = (4π)⁵ × ∫ e^{-|u|²} |c(iu/√t→0)|⁻² t⁵/t² du₁du₂ / t
    # Wait, let me redo: ν = u/√t, dν = du/t:
    # t⁵ ∫ e^{-|ν|²t} |c|⁻² dν₁dν₂ = t⁵ × (1/t) ∫ e^{-|u|²} |c(iu/√t)|⁻² du
    # = t⁴ ∫ e^{-|u|²} |c(iu/√t)|⁻² du
    #
    # For small t: |c(iu/√t)|⁻² ≈ (π⁴/256)(u₁²u₂²(u₁²-u₂²)²)/t⁴ × (corrections in t)
    # Note: the leading power is degree 8 in u and 1/t⁴ from the scaling.
    #
    # So t⁴ × |c|⁻² × t⁻⁴ = (π⁴/256) × u₁²u₂²(u₁²-u₂²)² + O(t).
    # Then b₀ = (4π)⁵ × ∫_{W-chamber} e^{-|u|²} (π⁴/256) u₁²u₂²(u₁²-u₂²)² du₁du₂.

    # Hmm, but I need to be careful: the full Plancherel density is π⁴/16 times
    # products with (ν²+1/4) factors. These (ν²+1/4) factors contribute both
    # degree 2 and degree 0 pieces. Let me redo.

    # S(ν) for small ν (keeping first two terms):
    # S(ν) = (ν²+1/4)·ν·(πν) = πν²(ν²+1/4) = πν⁴ + πν²/4
    # S(ν₁)S(ν₂) = π²(ν₁⁴+ν₁²/4)(ν₂⁴+ν₂²/4)
    # L(u) = πu²
    # Product = π⁴ × (ν₁⁴+ν₁²/4)(ν₂⁴+ν₂²/4) × u₊²u₋²
    #         = π⁴ × (ν₁⁴+ν₁²/4)(ν₂⁴+ν₂²/4) × (ν₁²-ν₂²)²/16

    # The pure degree-8 part (from the (1/4)ν² terms of each S):
    # π⁴ × (ν₁²/4)(ν₂²/4) × (ν₁²-ν₂²)²/16 = π⁴/(4²×16) × ν₁²ν₂²(ν₁²-ν₂²)²
    # = π⁴/256 × ν₁²ν₂²(ν₁²-ν₂²)²  ← THIS is the absolute leading

    # But there's also degree-10:
    # (ν₁⁴ × ν₂²/4 + ν₁²/4 × ν₂⁴) × (ν₁²-ν₂²)²/16
    # ... these contribute to b₁, not b₀.

    # After substitution ν = u/√t:
    # degree-8 terms → t⁻⁴ → combine with t⁴ to give t⁰ → b₀
    # degree-10 terms → t⁻⁵ → combine with t⁴ to give t⁻¹ → ???

    # Wait, that can't be right. Let me reconsider.
    # |c(iu/√t)|⁻² has degree-8 terms scaling as u⁸/t⁴, degree-10 as u¹⁰/t⁵, etc.
    # So t⁴ |c|⁻² = u⁸(leading coeff) + u¹⁰/t × (next coeff) + ...
    # The degree-10/t term → infinity as t→0 unless its integral vanishes.
    # But the integral ∫ e^{-|u|²} u^{10}/t du diverges as t→0.
    # This means I must be wrong about the scaling, or the t⁵ normalization
    # isn't quite right.

    # Let me reconsider. The heat kernel on D_{IV}^5 (noncompact, real dim 10):
    # K(t) = (4πt)^{-5} e^{-|ρ|²t} Σ b_k t^k
    # So (4πt)⁵ e^{|ρ|²t} K(t) = Σ b_k t^k.
    # And K(t) = ∫ e^{-(|ν|²+|ρ|²)t} |c(iν)|⁻² dν.
    # So (4πt)⁵ e^{|ρ|²t} ∫ e^{-(|ν|²+|ρ|²)t} |c|⁻² dν = Σ b_k t^k.
    # (4πt)⁵ ∫ e^{-|ν|²t} |c|⁻² dν = Σ b_k t^k.

    # Now ∫ e^{-|ν|²t} |c|⁻² dν → ∞ as t→0 (divergent), so (4πt)⁵ brings it down.

    # With ν = u/√t: dν = du/t, |ν|²t = |u|²:
    # (4πt)⁵ × (1/t) ∫ e^{-|u|²} |c(iu/√t)|⁻² du = Σ b_k t^k
    # (4π)⁵ t⁴ ∫ e^{-|u|²} |c(iu/√t)|⁻² du = Σ b_k t^k

    # |c(iu/√t)|⁻² = product of:
    #   S(u_i/√t) = (u_i²/t + 1/4) × (u_i/√t) × tanh(π u_i/√t)
    #   L(u_±/(2√t)) = (u_±/(2√t)) × tanh(π u_±/(2√t))

    # For small t (large argument): tanh(x) → 1 for large x.
    # So S(u/√t) → (u²/t)(u/√t) = u³/t^{3/2} for large u/√t.
    # L(u/(2√t)) → u/(2√t)
    #
    # Product → u₁³u₂³ × u₊u₋ / (t^{3/2} × t^{3/2} × t^{1/2} × t^{1/2})
    # = u₁³u₂³u₊u₋ / t⁴
    #
    # Then (4π)⁵ t⁴ × u₁³u₂³u₊u₋/t⁴ × integral = (4π)⁵ ∫ ...
    # But tanh → 1 means the exponential decay is gone, so the Gaussian
    # e^{-|u|²} provides the convergence, not tanh.

    # Hmm, but |c(iν)|⁻² ~ (π⁴/256)ν₁²ν₂²(ν₁²-ν₂²)² for SMALL ν,
    # while for LARGE ν, |c(iν)|⁻² ~ ν₁³ν₂³|ν₁²-ν₂²| × const.
    # The small-ν expansion gives the "spectral" coefficients.
    # The substitution ν = u/√t makes ν LARGE as t→0, not small!

    # So b₀ should come from the LARGE-ν behavior of |c|⁻², not small-ν.
    # This makes sense: the small-t heat kernel sees the high-frequency
    # spectral data (large ν), which gives the local geometry (b₀ = Vol).

    # For large ν: |c(iν)|⁻² → product of:
    #   (ν₁² + 1/4)·ν₁·1 × (ν₂² + 1/4)·ν₂·1 × (ν₁+ν₂)/2 × |ν₁-ν₂|/2
    # = (ν₁² + 1/4)(ν₂² + 1/4) × ν₁ν₂(ν₁²-ν₂²)/4 (for ν₁ > ν₂ > 0)
    # Hmm, but (ν₁-ν₂)/2 × tanh(π(ν₁-ν₂)/2) → (ν₁-ν₂)/2 for ν₁-ν₂ → ∞.
    # If ν₁ ≈ ν₂ (i.e., the difference is small), tanh stays small.

    # This is getting complicated. Let me just compute numerically.
    # The t→0 limit of (4πt)⁵ I(t) should give b₀.

    print(f"\n  (4πt)⁵ I(t) values (should converge to b₀ as t→0):")
    for t, I in zip(t_values, I_values):
        b0_est = (4 * np.pi * t)**5 * I
        print(f"    t={t:.3f}: {b0_est:.10f}")

    # Extrapolate b₀
    # Use the last three values and linear extrapolation in t
    if len(t_values) >= 3:
        ts = np.array(t_values[-3:])
        bs = np.array([(4 * np.pi * t)**5 * I
                       for t, I in zip(t_values[-3:], I_values[-3:])])
        # Linear fit: b₀ + b₁×t
        coeffs_fit = np.polyfit(ts, bs, 1)
        b0_extrap = coeffs_fit[1]
        b1_slope = coeffs_fit[0]
        print(f"\n  Linear extrapolation → b₀ ≈ {b0_extrap:.10f}")
        print(f"  Slope (b₁ estimate) ≈ {b1_slope:.6f}")

        # Compare with Vol(D_{IV}^5)
        print(f"\n  b₀ / Vol(D_IV^5) = {b0_extrap / vol_D:.6f}")
        print(f"  b₀ / (π⁵/1920) = {b0_extrap / vol_D:.6f}")

    # ──────────────────────────────────────────────────────
    # STEP 6: Weyl vector connection
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 6: Weyl vector and BST connections")
    print(f"  ══════════════════════════════════════════════════════")

    # ρ = (5/2, 3/2) → |ρ|² = 34/4 = 17/2
    print(f"\n  ρ = (5/2, 3/2)")
    print(f"  |ρ|² = 17/2 = {17/2}")
    print(f"  Note: 17 appears in r₃ = 17×67/63 and r₄ = 17×49/45")
    print(f"  ρ₁ = 5/2 = n_C/2  [half the complex dimension]")
    print(f"  ρ₂ = 3/2 = N_c/2  [half the color number]")
    print(f"  |ρ|² = (n_C² + N_c²)/4 = (25+9)/4 = 34/4 = 17/2")

    # The compact-noncompact duality:
    print(f"\n  Compact-noncompact duality:")
    print(f"  Q⁵ eigenvalue: λ_k = k(k+5) = k(k+n_C)")
    print(f"  D_IV^5 spectral param: |ν|² + |ρ|² = |ν|² + 17/2")
    print(f"  At k=0: λ₀ = 0, but |ρ|² = 17/2 (shift)")

    # The Casimir of SO(7) on (p,q,0) rep: C = p(p+5) + q(q+3)
    # For zonal (k,0,0): C = k(k+5) = (k + 5/2)² - 25/4
    # On D_IV^5: C → |ν|² (continuous spectrum starts at |ρ|²)
    print(f"\n  Zonal sector: C(k) = k(k+5) = (k+5/2)² - 25/4")
    print(f"  Continuous: |ν|² ≥ 0, shifted by |ρ|²")
    print(f"  Total spectral gap: |ρ|² = 17/2")


if __name__ == '__main__':
    main()
