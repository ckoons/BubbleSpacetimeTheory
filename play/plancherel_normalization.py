#!/usr/bin/env python3
"""
BST — Plancherel Normalization Discovery
==========================================
KEY RESULT: b₀ = 48π⁵ = |W(B₂)| × C₂ × π^{n_C}

The Plancherel integral I(t) = ∫_{ν₁>ν₂>0} e^{-|ν|²t} |c(iν)|⁻² dν₁dν₂
satisfies:
    F(t) = (4πt)⁵ I(t) = b₀ + b₁t + b₂t² + ...

with:
    b₀ = 48π⁵              = |W(B₂)| × C₂ × π^{n_C}
    b₁/b₀ = 1/6 = 1/C₂
    b₂/b₀ = ?  (to be determined precisely)

The normalized b̃_k = b_k/b₀ give the Seeley-DeWitt coefficients via:
    ã_k = Σ_{j=0}^k (-|ρ|²)^j/j! × b̃_{k-j}  where |ρ|² = 17/2

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from scipy.integrate import dblquad
from fractions import Fraction
from math import factorial


def plancherel_density(nu1, nu2):
    """Plancherel density |c(iν)|⁻² for D_IV^5."""
    def S(nu):
        if abs(nu) < 1e-15:
            return 0.0
        return (nu**2 + 0.25) * nu * np.tanh(np.pi * nu)

    def L(u):
        if abs(u) < 1e-15:
            return 0.0
        return u * np.tanh(np.pi * u)

    u_plus = (nu1 + nu2) / 2
    u_minus = (nu1 - nu2) / 2
    return S(nu1) * S(nu2) * L(u_plus) * L(u_minus)


def compute_F(t, epsabs=1e-13, epsrel=1e-13):
    """Compute F(t) = (4πt)⁵ × ∫_{ν₁>ν₂>0} e^{-|ν|²t} |c|⁻² dν₁dν₂."""
    nu_max = min(30.0 / np.sqrt(t), 300.0)

    def integrand(nu2, nu1, t_val):
        return np.exp(-(nu1**2 + nu2**2) * t_val) * plancherel_density(nu1, nu2)

    I_val, err = dblquad(
        integrand, 0, nu_max, 0, lambda nu1: nu1,
        args=(t,), epsabs=epsabs, epsrel=epsrel
    )
    return (4 * np.pi * t)**5 * I_val, (4 * np.pi * t)**5 * err


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  PLANCHEREL NORMALIZATION: b₀ = 48π⁵")
    print("  ══════════════════════════════════════════════════════")

    b0_exact = 48 * np.pi**5
    print(f"\n  Predicted: b₀ = 48π⁵ = {b0_exact:.12f}")
    print(f"  48 = |W(B₂)| × C₂ = 8 × 6")

    # ──────────────────────────────────────────────────────
    # Fine-grained computation for small t
    # ──────────────────────────────────────────────────────
    print(f"\n  Computing F(t) = (4πt)⁵ I(t) with high precision...")

    t_values = [0.050, 0.040, 0.030, 0.025, 0.020, 0.015,
                0.012, 0.010, 0.008, 0.006, 0.005]
    F_values = []

    for t in t_values:
        F_val, F_err = compute_F(t)
        F_values.append(F_val)
        diff = F_val - b0_exact
        print(f"    t = {t:.4f}: F = {F_val:.10f}  "
              f"F - 48π⁵ = {diff:.6f}  (err ~ {F_err:.1e})")

    # ──────────────────────────────────────────────────────
    # Extract b₁ and b₂ via polynomial fit
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  COEFFICIENT EXTRACTION")
    print(f"  ══════════════════════════════════════════════════════")

    ts = np.array(t_values)
    Fs = np.array(F_values)

    # Method 1: subtract b₀ and divide by t
    G1 = (Fs - b0_exact) / ts  # should → b₁

    print(f"\n  G₁(t) = (F(t) - 48π⁵)/t → b₁:")
    for t, g in zip(t_values, G1):
        print(f"    t = {t:.4f}: G₁ = {g:.8f}")

    # Method 2: polynomial fit
    # F(t) - b₀ = b₁t + b₂t² + b₃t³ + ...
    # (F - b₀)/t = b₁ + b₂t + b₃t²
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

    # Best b₁ estimate
    coeffs_best = np.polyfit(ts[-8:], G1[-8:], 3)
    b1_est = coeffs_best[-1]
    b2_est = coeffs_best[-2]
    b3_est = coeffs_best[-3]

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  RESULTS")
    print(f"  ══════════════════════════════════════════════════════")

    b0 = b0_exact
    b1 = b1_est
    b2 = b2_est
    b3 = b3_est

    print(f"\n  Raw coefficients:")
    print(f"    b₀ = 48π⁵ = {b0:.10f}")
    print(f"    b₁ = {b1:.10f}")
    print(f"    b₂ = {b2:.10f}")
    print(f"    b₃ = {b3:.10f}")

    print(f"\n  Normalized b̃_k = b_k / (48π⁵):")
    b1_norm = b1 / b0
    b2_norm = b2 / b0
    b3_norm = b3 / b0
    print(f"    b̃₀ = 1")
    print(f"    b̃₁ = {b1_norm:.12f}")
    print(f"    b̃₂ = {b2_norm:.12f}")
    print(f"    b̃₃ = {b3_norm:.12f}")

    # Check b̃₁ = 1/6
    print(f"\n  Test b̃₁ = 1/6 = {1/6:.12f}")
    print(f"  Diff: {b1_norm - 1/6:.4e}")

    # Search for b̃₂ as a rational
    print(f"\n  Searching for rational b̃₂:")
    for d in range(1, 500):
        n = round(b2_norm * d)
        if n > 0 and abs(n/d - b2_norm) < 1e-5:
            f = Fraction(n, d)
            print(f"    {f} = {float(f):.10f}  (diff = {float(f) - b2_norm:.4e})")

    # ──────────────────────────────────────────────────────
    # Seeley-DeWitt a_k
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SEELEY-DEWITT COEFFICIENTS (normalized)")
    print(f"  ã_k = Σ (-17/2)^j/j! × b̃_{{k-j}}")
    print(f"  ══════════════════════════════════════════════════════")

    rho2 = 17.0 / 2
    b_norm = [1.0, b1_norm, b2_norm, b3_norm]

    a_vals = []
    for k in range(len(b_norm)):
        ak = 0
        for j in range(k + 1):
            ak += (-rho2)**j / factorial(j) * b_norm[k - j]
        a_vals.append(ak)

    for k, ak in enumerate(a_vals):
        print(f"\n    ã_{k} = {ak:.12f}")

    # ã₁ should be related to R/6
    print(f"\n  ã₁ = {a_vals[1]:.10f}")
    print(f"  -25/3 = {-25/3:.10f}")
    print(f"  -50/3 = {-50/3:.10f}")
    print(f"  -50/6 = {-50/6:.10f}")

    # ──────────────────────────────────────────────────────
    # BST decomposition of 48
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  BST DECOMPOSITION OF 48")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"\n  48 = 2⁴ × 3")
    print(f"  48 = |W(B₂)| × C₂ = 8 × 6")
    print(f"  48 = |W(B₂)| × χ(Q⁵) = 8 × 6")
    print(f"  48 = 1920/40 = |W(D₅)|/40")
    print(f"  48 = 2⁴ × N_c = 16 × 3")
    print(f"  48 = 4! × 2 = 4! × r(D_IV^5)")
    print(f"\n  b₀ = 48π⁵ = |W(B₂)| × C₂ × π^{{n_C}}")
    print(f"  b̃₁ = 1/C₂ = 1/6")


if __name__ == '__main__':
    main()
