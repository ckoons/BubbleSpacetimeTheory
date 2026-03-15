#!/usr/bin/env python3
"""
BST — Plancherel b_k extraction for D_IV³ = SO₀(3,2)/[SO(3)×SO(2)]

The baby Selberg case. Same B₂ restricted root system as Q⁵ but with
multiplicities (m_s=1, m_ℓ=1) instead of (m_s=3, m_ℓ=1).

Plancherel density:
  |c(iν)|⁻² ∝ ν₁ tanh(πν₁) × ν₂ tanh(πν₂)
              × u₊ tanh(πu₊) × u₋ tanh(πu₋)

where u± = (ν₁ ± ν₂)/2.

Predictions (from curvature + corrected a₃ formula):
  b₀ = 2π³              (from polynomial asymptotics)
  b̃₁ = -1/2             (from R/6 + |ρ|²)
  b̃₂ = 7/24             (from Gilkey a₂)
  b̃₃ = -367/1680         (from corrected a₃)

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from scipy.integrate import dblquad
from fractions import Fraction
from math import factorial


# ═══════════════════════════════════════════════════════════════════
# PLANCHEREL DENSITY FOR Q³
# ═══════════════════════════════════════════════════════════════════

def plancherel_density_q3(nu1, nu2):
    """
    |c(iν)|⁻² for D_IV³ at spectral parameter (ν₁, ν₂).

    B₂ root system with m_s = 1, m_ℓ = 1:
      Short: S(ν) = ν·tanh(πν)        [roots e₁, e₂]
      Long:  L(u) = u·tanh(πu)        [roots e₁±e₂]
    """
    def factor(x):
        if abs(x) < 1e-15:
            return 0.0
        return x * np.tanh(np.pi * x)

    u_plus = (nu1 + nu2) / 2
    u_minus = (nu1 - nu2) / 2

    return factor(nu1) * factor(nu2) * factor(u_plus) * factor(u_minus)


def compute_F_q3(t, epsabs=1e-13, epsrel=1e-13):
    """Compute F(t) = (4πt)³ × ∫_{ν₁>ν₂>0} e^{-|ν|²t} |c|⁻² dν₁dν₂."""
    nu_max = min(20.0 / np.sqrt(t), 200.0)

    def integrand(nu2, nu1, t_val):
        return np.exp(-(nu1**2 + nu2**2) * t_val) * plancherel_density_q3(nu1, nu2)

    I_val, err = dblquad(
        integrand, 0, nu_max, 0, lambda nu1: nu1,
        args=(t,), epsabs=epsabs, epsrel=epsrel
    )
    return (4 * np.pi * t)**3 * I_val, (4 * np.pi * t)**3 * err


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  PLANCHEREL COMPUTATION FOR D_IV³")
    print("  B₂ root system, m_s = 1, m_ℓ = 1, |ρ|² = 5/2")
    print("  ══════════════════════════════════════════════════════")

    # Predictions
    b0_pred = 2 * np.pi**3
    b1_pred = b0_pred * (-0.5)      # b̃₁ = -1/2
    rho_sq = 5.0 / 2

    print(f"\n  Predicted: b₀ = 2π³ = {b0_pred:.12f}")

    # ──────────────────────────────────────────────────────
    # Step 1: Compute F(t) for many t values
    # ──────────────────────────────────────────────────────
    print(f"\n  Computing F(t) = (4πt)³ I(t)...")

    t_values = [0.10, 0.08, 0.06, 0.05, 0.04, 0.03,
                0.025, 0.02, 0.015, 0.012, 0.01]
    F_values = []

    for t in t_values:
        F_val, F_err = compute_F_q3(t)
        F_values.append(F_val)
        diff = F_val - b0_pred
        print(f"    t = {t:.4f}: F = {F_val:.10f}  "
              f"F - 2π³ = {diff:.6f}  (err ~ {F_err:.1e})")

    # ──────────────────────────────────────────────────────
    # Step 2: Extract b₁ and b₂
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  COEFFICIENT EXTRACTION")
    print(f"  ══════════════════════════════════════════════════════")

    ts = np.array(t_values)
    Fs = np.array(F_values)

    # G₁(t) = (F(t) - b₀)/t → b₁
    G1 = (Fs - b0_pred) / ts
    print(f"\n  G₁(t) = (F(t) - 2π³)/t → b₁:")
    for t, g in zip(t_values, G1):
        print(f"    t = {t:.4f}: G₁ = {g:.8f}")

    # Polynomial fits
    for deg in [2, 3, 4]:
        n_pts = min(deg + 3, len(ts))
        coeffs = np.polyfit(ts[-n_pts:], G1[-n_pts:], deg)
        b_from_fit = coeffs[::-1]
        print(f"\n    Degree-{deg} fit of G₁(t) ({n_pts} pts):")
        print(f"      b₁ ≈ {b_from_fit[0]:.10f}")
        if len(b_from_fit) > 1:
            print(f"      b₂ ≈ {b_from_fit[1]:.10f}")
        if len(b_from_fit) > 2:
            print(f"      b₃ ≈ {b_from_fit[2]:.10f}")

    # Best estimates
    coeffs_best = np.polyfit(ts[-8:], G1[-8:], 3)
    b1_est = coeffs_best[-1]
    b2_est = coeffs_best[-2]
    b3_est = coeffs_best[-3]

    # ──────────────────────────────────────────────────────
    # Step 3: Results
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  RESULTS")
    print(f"  ══════════════════════════════════════════════════════")

    b0 = b0_pred
    b1 = b1_est
    b2 = b2_est
    b3 = b3_est

    print(f"\n  Raw coefficients:")
    print(f"    b₀ = 2π³ = {b0:.10f}")
    print(f"    b₁ = {b1:.10f}")
    print(f"    b₂ = {b2:.10f}")
    print(f"    b₃ = {b3:.10f}")

    b1_norm = b1 / b0
    b2_norm = b2 / b0
    b3_norm = b3 / b0

    print(f"\n  Normalized b̃_k = b_k / (2π³):")
    print(f"    b̃₀ = 1")
    print(f"    b̃₁ = {b1_norm:.12f}  (predicted: -1/2 = {-0.5:.12f})")
    print(f"    b̃₂ = {b2_norm:.12f}  (predicted: 7/24 = {7/24:.12f})")
    print(f"    b̃₃ = {b3_norm:.12f}  (predicted: -367/1680 = {-367/1680:.12f})")

    print(f"\n  Discrepancies:")
    print(f"    b̃₁ - (-1/2) = {b1_norm - (-0.5):.4e}")
    print(f"    b̃₂ - 7/24   = {b2_norm - 7/24:.4e}")
    print(f"    b̃₃ - (-367/1680) = {b3_norm - (-367/1680):.4e}")

    # ──────────────────────────────────────────────────────
    # Step 4: Seeley-DeWitt ã_k
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SEELEY-DEWITT ã_k FROM PLANCHEREL")
    print(f"  ã_k = Σ (-5/2)^j/j! × b̃_{{k-j}}")
    print(f"  ══════════════════════════════════════════════════════")

    b_norm = [1.0, b1_norm, b2_norm, b3_norm]
    a_vals = []
    for k in range(len(b_norm)):
        ak = 0
        for j in range(k + 1):
            ak += (-rho_sq)**j / factorial(j) * b_norm[k - j]
        a_vals.append(ak)

    print(f"\n    ã₀ = {a_vals[0]:.12f}  (should be 1)")
    print(f"    ã₁ = {a_vals[1]:.12f}  (should be -3 = {-3.0:.12f})")
    print(f"    ã₂ = {a_vals[2]:.12f}  (should be 14/3 = {14/3:.12f})")
    print(f"    ã₃ = {a_vals[3]:.12f}  (should be -179/35 = {-179/35:.12f})")

    # ──────────────────────────────────────────────────────
    # Step 5: Comparison with Q⁵
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Q³ vs Q⁵ PLANCHEREL COMPARISON")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"\n  {'':>20}{'Q³':>15}{'Q⁵':>15}")
    print(f"  {'─'*50}")
    print(f"  {'(m_s, m_ℓ)':>20}{'(1, 1)':>15}{'(3, 1)':>15}")
    print(f"  {'|ρ|²':>20}{'5/2':>15}{'17/2':>15}")
    print(f"  {'b₀':>20}{'2π³':>15}{'48π⁵':>15}")
    print(f"  {'b̃₁':>20}{'-1/2':>15}{'1/6':>15}")
    print(f"  {'b̃₂':>20}{'7/24':>15}{'5/72':>15}")
    print(f"  {'b̃₃':>20}{'-367/1680':>15}{'-3/16':>15}")
    print(f"  {'ã₃':>20}{'-179/35':>15}{'-874/9':>15}")


if __name__ == '__main__':
    main()
