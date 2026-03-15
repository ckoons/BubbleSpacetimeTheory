#!/usr/bin/env python3
"""
BST — Extract b̃₃ precisely from Plancherel density
=====================================================
We know exactly:
  b̃₀ = 1, b̃₁ = 1/6, b̃₂ = 5/72, b₀_raw = 48π⁵

Strategy: compute G₃(t) = [F(t) - 48π⁵(1 + t/6 + 5t²/72)] / (48π⁵ t³)
which should → b̃₃ as t → 0.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from scipy.integrate import dblquad
from fractions import Fraction


def plancherel_density(nu1, nu2):
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


def compute_F(t):
    """F(t) = (4πt)⁵ ∫ e^{-|ν|²t} |c|⁻² dν."""
    nu_max = min(30.0 / np.sqrt(t), 300.0)
    def integrand(nu2, nu1, t_val):
        return np.exp(-(nu1**2 + nu2**2) * t_val) * plancherel_density(nu1, nu2)
    I_val, err = dblquad(
        integrand, 0, nu_max, 0, lambda nu1: nu1,
        args=(t,), epsabs=1e-13, epsrel=1e-13
    )
    return (4 * np.pi * t)**5 * I_val


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  PRECISE EXTRACTION OF b̃₃")
    print("  ══════════════════════════════════════════════════════")

    b0 = 48 * np.pi**5
    b1_tilde = 1.0 / 6
    b2_tilde = 5.0 / 72

    # G₃(t) = [F(t)/b₀ - 1 - t/6 - 5t²/72] / t³ → b̃₃
    t_values = [0.05, 0.04, 0.03, 0.025, 0.020, 0.015,
                0.012, 0.010, 0.008, 0.006, 0.005, 0.004]

    print(f"\n  Computing G₃(t) = [F/(48π⁵) - 1 - t/6 - 5t²/72] / t³:")
    G3_values = []

    for t in t_values:
        F = compute_F(t)
        F_norm = F / b0  # should be 1 + t/6 + 5t²/72 + b̃₃t³ + ...
        residual = F_norm - 1 - b1_tilde * t - b2_tilde * t**2
        G3 = residual / t**3
        G3_values.append(G3)
        print(f"    t = {t:.4f}: G₃ = {G3:.10f}")

    # Extrapolate G₃ → b̃₃ as t → 0
    ts = np.array(t_values)
    G3s = np.array(G3_values)

    print(f"\n  Polynomial extrapolation of G₃(t) = b̃₃ + b̃₄t + ...")
    for deg in [1, 2, 3]:
        n = min(deg + 2, len(ts))
        coeffs = np.polyfit(ts[-n:], G3s[-n:], deg)
        b3_est = coeffs[-1]
        print(f"    Degree-{deg} ({n} pts): b̃₃ ≈ {b3_est:.12f}")

    # Use the best estimate
    best = np.polyfit(ts[-6:], G3s[-6:], 2)
    b3_best = best[-1]

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  BEST ESTIMATE: b̃₃ = {b3_best:.12f}")
    print(f"  ══════════════════════════════════════════════════════")

    # Search for rational form
    print(f"\n  Rational search:")
    for d in range(1, 2000):
        n = round(b3_best * d)
        if abs(n) > 0 and abs(n/d - b3_best) < 1e-6:
            f = Fraction(n, d)
            print(f"    {f} = {float(f):.12f}  (diff = {float(f) - b3_best:.6e})")

    # Check specific BST-motivated fractions
    print(f"\n  BST candidates:")
    candidates = [
        ("-17/90", Fraction(-17, 90)),
        ("-17/91", Fraction(-17, 91)),
        ("-1/5", Fraction(-1, 5)),
        ("-5/27", Fraction(-5, 27)),
        ("-137/720", Fraction(-137, 720)),
        ("-137/660", Fraction(-137, 660)),
        ("-137/756", Fraction(-137, 756)),
        ("-17/90", Fraction(-17, 90)),
        ("-25/132", Fraction(-25, 132)),
        ("-25/133", Fraction(-25, 133)),
        ("-5/26", Fraction(-5, 26)),
        ("-5/27", Fraction(-5, 27)),
        ("-1139/6048", Fraction(-1139, 6048)),
    ]
    for name, frac in candidates:
        diff = float(frac) - b3_best
        print(f"    {name} = {float(frac):.12f}  (diff = {diff:.6e})")

    # Compute ã₃ from b̃₃
    rho2 = 17.0 / 2
    b_tilde = [1.0, 1/6, 5/72, b3_best]
    a3 = 0
    for j in range(4):
        from math import factorial
        a3 += (-rho2)**j / factorial(j) * b_tilde[3 - j]
    print(f"\n  ã₃ = {a3:.10f}")

    # From the note: a₃(Q⁵) = 6992/70875 in Killing normalization
    # In Plancherel norm (1/10 × Killing): a₃ → a₃_K × 10³ = 6992/70.875
    # With sign flip for noncompact: ã₃ = -6992/70.875
    a3_pred = -6992000/70875
    print(f"  Predicted from curvature: ã₃ = -6992000/70875 = {a3_pred:.10f}")
    print(f"  Ratio: {a3/a3_pred:.10f}")

    # What b̃₃ would give the predicted ã₃?
    # ã₃ = b̃₃ + (-17/2)b̃₂ + (17/2)²/2 × b̃₁ + (-17/2)³/6 × b̃₀
    # b̃₃ = ã₃ - [(-17/2)b̃₂ + (17/2)²/2 × b̃₁ + (-17/2)³/6]
    b3_from_a3 = Fraction(-6992000, 70875) - (
        Fraction(-17, 2) * Fraction(5, 72) +
        Fraction(17, 2)**2 / 2 * Fraction(1, 6) +
        Fraction(-17, 2)**3 / 6 * Fraction(1)
    )
    print(f"\n  If ã₃ = -6992000/70875:")
    print(f"    b̃₃ would be = {b3_from_a3} = {float(b3_from_a3):.12f}")


if __name__ == '__main__':
    main()
