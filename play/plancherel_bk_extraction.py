#!/usr/bin/env python3
"""
BST — Extract b_k coefficients from Plancherel density on D_{IV}^5
====================================================================
The noncompact heat kernel at the origin:
  K(t,o,o) = (4πt)^{-5} e^{-|ρ|²t} Σ b_k t^k

where b_k come from the Plancherel density |c(iν)|⁻².

The Seeley-DeWitt coefficients:
  a_k = Σ_{j=0}^k (-|ρ|²)^j / j! × b_{k-j}

with |ρ|² = 17/2.

Strategy: compute (4πt)⁵ I(t) numerically for small t, where
  I(t) = ∫_{ν₁>ν₂>0} e^{-|ν|²t} |c(iν)|⁻² dν₁ dν₂
then fit b₀ + b₁t + b₂t² + ... to extract coefficients.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from scipy.integrate import dblquad
from fractions import Fraction
from math import factorial


# ═══════════════════════════════════════════════════════════════════
# PLANCHEREL DENSITY
# ═══════════════════════════════════════════════════════════════════

def plancherel_density(nu1, nu2):
    """
    |c(iν)|⁻² for D_{IV}^5 at spectral parameter (ν₁, ν₂).

    Product of 4 factors (B₂ root system, m_s=3, m_l=1):
      Short: S(ν) = (ν²+1/4)·ν·tanh(πν)    [roots e₁, e₂]
      Long:  L(u) = u·tanh(πu)              [roots e₁±e₂]
    """
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


# ═══════════════════════════════════════════════════════════════════
# NUMERICAL INTEGRATION
# ═══════════════════════════════════════════════════════════════════

def compute_I(t, nu_max=None, epsabs=1e-12, epsrel=1e-12):
    """Compute I(t) = ∫_{ν₁>ν₂>0} e^{-|ν|²t} |c(iν)|⁻² dν₁ dν₂."""
    if nu_max is None:
        nu_max = min(25.0 / np.sqrt(t), 200.0)

    def integrand(nu2, nu1, t_val):
        return np.exp(-(nu1**2 + nu2**2) * t_val) * plancherel_density(nu1, nu2)

    I_val, err = dblquad(
        integrand,
        0, nu_max,            # ν₁ limits
        0, lambda nu1: nu1,   # ν₂ from 0 to ν₁
        args=(t,),
        epsabs=epsabs, epsrel=epsrel
    )
    return I_val, err


def compute_F(t):
    """Compute F(t) = (4πt)⁵ I(t), which should equal Σ b_k t^k."""
    I_val, err = compute_I(t)
    F_val = (4 * np.pi * t)**5 * I_val
    F_err = (4 * np.pi * t)**5 * err
    return F_val, F_err


# ═══════════════════════════════════════════════════════════════════
# RICHARDSON EXTRAPOLATION
# ═══════════════════════════════════════════════════════════════════

def richardson_extract(t_values, F_values, order=0):
    """
    Extract the coefficient of t^order from F(t) = Σ b_k t^k.

    For order=0: extracts b₀ = lim_{t→0} F(t)
    For order=1: extracts b₁ from (F(t) - b₀)/t → b₁
    etc.

    Uses Richardson extrapolation (polynomial fitting).
    """
    n = len(t_values)
    # Fit polynomial of degree n-1 to the data
    ts = np.array(t_values)
    fs = np.array(F_values)

    # Remove lower order terms
    # For order > 0, we should subtract known lower coefficients first
    # For now, just fit a polynomial
    coeffs = np.polyfit(ts, fs, min(n - 1, 6))
    return coeffs[-1 - order] if order < len(coeffs) else None


# ═══════════════════════════════════════════════════════════════════
# MAIN COMPUTATION
# ═══════════════════════════════════════════════════════════════════

def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  PLANCHEREL b_k EXTRACTION FOR D_{IV}^5")
    print("  ══════════════════════════════════════════════════════")

    rho_sq = Fraction(17, 2)
    print(f"\n  |ρ|² = {rho_sq} = {float(rho_sq)}")

    # ──────────────────────────────────────────────────────
    # Step 1: Compute F(t) = (4πt)⁵ I(t) for many t values
    # ──────────────────────────────────────────────────────
    print(f"\n  Step 1: Computing F(t) = (4πt)⁵ I(t)...")

    t_values = [0.5, 0.3, 0.2, 0.15, 0.1, 0.08, 0.06, 0.05,
                0.04, 0.03, 0.02, 0.015, 0.01]
    F_values = []

    for t in t_values:
        F_val, F_err = compute_F(t)
        F_values.append(F_val)
        print(f"    t = {t:.3f}: F(t) = {F_val:.10f}  (err = {F_err:.2e})")

    # ──────────────────────────────────────────────────────
    # Step 2: Extract b₀ by polynomial fitting
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 2: Extract b_k by polynomial fitting")
    print(f"  ══════════════════════════════════════════════════════")

    ts = np.array(t_values)
    Fs = np.array(F_values)

    # Fit F(t) = b₀ + b₁t + b₂t² + b₃t³ + ...
    for deg in [2, 3, 4, 5, 6]:
        # Use smallest t values for best accuracy
        n_pts = min(deg + 3, len(ts))
        idx = slice(-n_pts, None)  # last n_pts values (smallest t)
        coeffs = np.polyfit(ts[idx], Fs[idx], deg)
        # coeffs are [highest power first, ..., constant]
        b_fit = coeffs[::-1]  # now b_fit[k] ≈ b_k

        print(f"\n    Degree-{deg} fit (using {n_pts} smallest-t points):")
        for k in range(min(deg + 1, 5)):
            print(f"      b_{k} ≈ {b_fit[k]:.10f}")

    # ──────────────────────────────────────────────────────
    # Step 3: Best estimate of b₀, b₁, b₂
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 3: Best estimates")
    print(f"  ══════════════════════════════════════════════════════")

    # Use degree-4 fit with smallest 8 points
    n_use = 8
    coeffs = np.polyfit(ts[-n_use:], Fs[-n_use:], 4)
    b_est = coeffs[::-1]

    b0 = b_est[0]
    b1 = b_est[1]
    b2 = b_est[2]
    b3 = b_est[3] if len(b_est) > 3 else 0

    print(f"\n    b₀ = {b0:.10f}")
    print(f"    b₁ = {b1:.10f}")
    print(f"    b₂ = {b2:.10f}")
    print(f"    b₃ = {b3:.10f}")

    # ──────────────────────────────────────────────────────
    # Check normalizations
    # ──────────────────────────────────────────────────────
    print(f"\n  Normalization checks:")
    vol_D = np.pi**5 / 1920
    vol_Q = 8 * np.pi**5 / 15
    print(f"    Vol(D_IV^5) = π⁵/1920 = {vol_D:.10f}")
    print(f"    b₀ / 1 = {b0:.6f}")
    print(f"    b₀ / (2π)⁵ = {b0 / (2*np.pi)**5:.10f}")
    print(f"    b₀ / π⁵ = {b0 / np.pi**5:.10f}")
    print(f"    b₀ / (4π)⁵ = {b0 / (4*np.pi)**5:.10f}")

    # Check if b₀ = (4π)⁵ × Vol(D) = (4π)⁵ × π⁵/1920
    check1 = (4 * np.pi)**5 * vol_D
    print(f"    (4π)⁵ × Vol(D) = {check1:.6f}")

    # Check specific rationals near b₀
    print(f"\n    Searching for rational form of b₀:")
    for num in range(1, 200):
        for den in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16,
                    20, 24, 30, 32, 48, 60, 64, 120, 128, 256, 512, 1024]:
            r = Fraction(num, den)
            if abs(float(r) - b0) < 0.01:
                print(f"      {r} = {float(r):.6f}  (diff = {float(r) - b0:.4e})")

    # Check if b₀ = c × π^n for some small c, n
    for n_pi in range(0, 6):
        ratio = b0 / np.pi**n_pi
        print(f"    b₀/π^{n_pi} = {ratio:.10f}")
        # Check if close to a simple fraction
        for d in range(1, 100):
            n = round(ratio * d)
            if abs(n/d - ratio) < 0.001 and n > 0:
                print(f"      ≈ {n}/{d} × π^{n_pi} = {n*np.pi**n_pi/d:.8f}")
                break

    # ──────────────────────────────────────────────────────
    # Step 4: Compute a_k from b_k
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print("  Step 4: Seeley-DeWitt a_k from b_k")
    print("  a_k = Sum_{j=0}^k (-|rho|^2)^j/j! * b_{k-j}")
    print("  ======================================================")

    rho2 = float(rho_sq)
    b_vals = [b0, b1, b2, b3]

    a_vals = []
    for k in range(len(b_vals)):
        ak = 0
        for j in range(k + 1):
            ak += (-rho2)**j / factorial(j) * b_vals[k - j]
        a_vals.append(ak)
        print(f"\n    a_{k} = {ak:.10f}")
        # Show the terms
        for j in range(k + 1):
            term = (-rho2)**j / factorial(j) * b_vals[k - j]
            print(f"      + (-17/2)^{j}/{j}! × b_{k-j} = {term:.6f}")

    # Compare with known values
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 5: Compare with known curvature invariants")
    print(f"  ══════════════════════════════════════════════════════")

    # Known from BST_SeeleyDeWitt note (Fubini-Study normalization):
    # a₀ = 1 (pointwise)
    # a₁ = R/6 = 100/6 = 50/3 ≈ 16.667 (Fubini-Study, R=100)
    # OR in Killing normalization: a₁ = 5/6 ≈ 0.833

    # But these are for Q⁵ (compact). For D_{IV}^5:
    # a_k(D) = (-1)^k a_k(Q) (sign alternation from curvature flip)

    print(f"\n    Compact Q⁵ (Fubini-Study, R=100):")
    a0_Q = 1
    a1_Q = Fraction(100, 6)  # R/6
    print(f"      a₀(Q⁵) = {a0_Q}")
    print(f"      a₁(Q⁵) = {a1_Q} = {float(a1_Q):.6f}")

    print("\n    Noncompact D_IV^5:")
    print(f"      a₀(D) = (-1)⁰ × a₀(Q) = 1")
    print(f"      a₁(D) = (-1)¹ × a₁(Q) = {-float(a1_Q):.6f}")

    print(f"\n    From Plancherel extraction:")
    for k in range(len(a_vals)):
        print(f"      a_{k} = {a_vals[k]:.10f}")

    # ──────────────────────────────────────────────────────
    # Step 6: Normalization discovery
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 6: Determine normalization constant C")
    print(f"  If b₀ = C, then the normalized coefficients are b̃_k = b_k/C")
    print(f"  ══════════════════════════════════════════════════════")

    if b0 > 0:
        print(f"\n    b₀ = {b0:.10f}")
        print(f"    b₁/b₀ = {b1/b0:.10f}")
        print(f"    b₂/b₀ = {b2/b0:.10f}")
        print(f"    b₃/b₀ = {b3/b0:.10f}")

        # If the TRUE b₀ should be 1, then the normalization C = b₀,
        # and the normalized coefficients are:
        b1_norm = b1 / b0
        b2_norm = b2 / b0
        b3_norm = b3 / b0

        print(f"\n    If b₀ → 1 (normalized):")
        print(f"      b̃₁ = {b1_norm:.10f}")
        print(f"      b̃₂ = {b2_norm:.10f}")
        print(f"      b̃₃ = {b3_norm:.10f}")

        # Then a_k with normalized b's:
        b_norm = [1.0, b1_norm, b2_norm, b3_norm]
        print(f"\n    Normalized a_k:")
        for k in range(len(b_norm)):
            ak = 0
            for j in range(k + 1):
                ak += (-rho2)**j / factorial(j) * b_norm[k - j]
            print(f"      ã_{k} = {ak:.10f}")

    # ──────────────────────────────────────────────────────
    # Step 7: Connection to compact r_k
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  Step 7: Compact ↔ Noncompact comparison")
    print(f"  ══════════════════════════════════════════════════════")

    # Exact compact coefficients
    r = {
        0: Fraction(1),
        1: Fraction(5),
        2: Fraction(12),
        3: Fraction(1139, 63),
        4: Fraction(833, 45),
        5: Fraction(137, 11),
    }

    print(f"\n    Compact zonal r_k (exact):")
    for k in sorted(r.keys()):
        print(f"      r_{k} = {r[k]} = {float(r[k]):.10f}")

    # The compact zonal expansion is:
    # t³ Z₀(t) = (1/60)[1 + r₁t + r₂t² + ...]
    #
    # The Euler-Maclaurin structure:
    # EM(t) = f(0)/2 - Σ B_{2j}/(2j)! f^{(2j-1)}(0)
    # where f(x) = d(x) e^{-h(x)t}
    #
    # The compact Casimir: λ_k = k(k+5) = (k+5/2)² - 25/4
    # The noncompact spectral param: |ν|² + |ρ|²
    # with |ρ|² = 17/2
    #
    # Under duality k+5/2 → iν (not exact for rank 2):
    # (k+5/2)² → -ν², so k(k+5) → -ν² - 25/4
    #
    # But the noncompact eigenvalue is |ν|² + |ρ|² = ν₁² + ν₂² + 17/2
    # This is 2D (rank 2), not 1D.
    #
    # The compact zonal sector has 1 parameter k, while noncompact
    # has 2 parameters (ν₁, ν₂). The duality is more subtle.

    # What we CAN compute: the a_k from curvature (Gilkey formulas)
    # For Q⁵ (Kähler-Einstein, R=100 in FS normalization):
    print(f"\n    Seeley-DeWitt from curvature (Q⁵, FS normalization):")
    R_FS = 100  # scalar curvature
    Ric_sq_FS = 1000  # |Ric|²
    Rm_sq_FS = 1040  # |Rm|² = 80 × c₃

    a0_curv = 1
    a1_curv = R_FS / 6
    a2_curv = (5 * R_FS**2 - 2 * Ric_sq_FS + 2 * Rm_sq_FS) / 360

    print(f"      a₀ = {a0_curv}")
    print(f"      a₁ = {R_FS}/6 = {a1_curv:.6f}")
    print(f"      a₂ = {a2_curv:.6f}")

    # For D_{IV}^5 (noncompact): sign alternation
    print("\n    Seeley-DeWitt for D_IV^5:")
    print(f"      a₀ = {a0_curv}")
    print(f"      a₁ = {-a1_curv:.6f}  (sign flip)")
    print(f"      a₂ = {a2_curv:.6f}  (even → same sign)")

    # From a₃ in the note: a₃(Q⁵) = 6992/70875
    a3_Q = Fraction(6992, 70875)
    print(f"      a₃(Q⁵) = {a3_Q} = {float(a3_Q):.10f}")
    print(f"      a₃(D) = {float(-a3_Q):.10f}  (sign flip)")


if __name__ == '__main__':
    main()
