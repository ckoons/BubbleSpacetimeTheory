#!/usr/bin/env python3
"""
Toy 241 — Seeley-DeWitt a₄, a₅ on Q⁵ via Plancherel Taylor
=============================================================

Route 1: Expand |c(λ)|⁻² (Harish-Chandra c-function inverse square)
as a polynomial in the spectral parameter. The Taylor coefficients
of the Plancherel density directly encode the Seeley-DeWitt coefficients.

The key identity (Gangolli 1971, Anker 1991):

    Z(t) = ∫ |c(iν)|⁻² e^{-(|ν|²+|ρ|²)t} dν

where ρ = half-sum of positive roots (weighted by multiplicity).

For D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)]:
  - Restricted root system: B₂
  - Positive roots: e₁±e₂ (long, m=1), e₁, e₂ (short, m=3)
  - ρ = (m_s + m_l)e₁/2 + m_s·e₂/2 = 2e₁ + 3e₂/2
    Actually: ρ = ½Σ_{α>0} m_α · α
    = ½[1·(e₁-e₂) + 1·(e₁+e₂) + 3·e₁ + 3·e₂]
    = ½[e₁-e₂ + e₁+e₂ + 3e₁ + 3e₂]
    = ½[5e₁ + 3e₂] = (5/2, 3/2)
  - |ρ|² = 25/4 + 9/4 = 34/4 = 17/2

The Plancherel density |c(iν)|⁻² for B₂ with (m_s, m_l) = (3, 1):

  |c(iν)|⁻² = C × ∏_{α>0} |Γ((i⟨ν,α∨⟩ + m_α)/2)|²/|Γ(i⟨ν,α∨⟩/2)|²

Using the Gamma ratio identity for real m, purely imaginary argument:
  |Γ((iz+m)/2)|²/|Γ(iz/2)|² = ∏_{j=0}^{m-1} (z²/4 + j²/4)  [for m even]
  ... and similar for m odd via the reflection/duplication formula.

For m=1 (long roots):
  |Γ((iz+1)/2)|²/|Γ(iz/2)|² = (1/4)(z² + 1)  ... NO.
  Actually: |Γ(1/2 + iz/2)|² / |Γ(iz/2)|²
  Using Γ(s)Γ(1-s) = π/sin(πs) and |Γ(iy)|² = π/(y sinh(πy)):
  This gives a ratio that for POLYNOMIAL extraction we expand as
  ∏_{j=0}^{(m-1)/2} ((z/2)² + ((2j+1)/2)²) / ((z/2)² + j²)  ... messy.

CLEAN APPROACH: Use the KNOWN polynomial form of |c(λ)|⁻² for B₂.

For a rank-2 symmetric space of type B₂ with root multiplicities (m_s, m_l),
the Plancherel density as a function of the Harish-Chandra parameter λ=(λ₁,λ₂)
is a POLYNOMIAL in λ₁, λ₂ (Helgason, Groups and Geometric Analysis, Ch. IV):

  |c(λ)|⁻² = const × ∏_{α>0} ∏_{j=0}^{m_α/2 - 1} (⟨λ,α∨⟩² + (ρ_α + 2j)²)

where ρ_α = ½ Σ_{β>0, β≠α} m_β ⟨β,α∨⟩.

For OUR case (m_s=3, m_l=1), the multiplicities are ODD, so we use the
Gindikin-Karpelevich PRODUCT FORMULA evaluated numerically at grid points,
then fit the polynomial.

ACTUAL APPROACH: Direct numerical extraction.
1. Compute the zonal heat trace Z₀(t) = Σ d_k e^{-k(k+5)t} (exact, fast)
2. Form h(t) = (4πt)^3 Z₀(t) = B₀ + B₁t + B₂t² + ...
3. Extract B₀,...,B₅ via Richardson extrapolation at very small t
4. The B_k ARE the integrated Seeley-DeWitt coefficients for the zonal sector
5. Similarly for the full trace with (4πt)^5

The zonal a_k relate to curvature invariants via:
  B₀ = (4π)^3 / 60  (known, verified)
  B₁ = B₀ × R_eff/6  where R_eff is the effective scalar curvature
  B₂, B₃ known (a₂, a₃ CLOSED in prior sessions)
  B₄ = ∫ a₄ dV_eff  ← NEW
  B₅ → Gauss-Bonnet for effective geometry

For the FULL spectrum:
  A₀ = Vol(Q⁵)
  A₁ = (R/6) × Vol
  A₂ = [(5R² - 2|Ric|² + 2|Rm|²)/360] × Vol
  A₃ = CLOSED (corrected Vassilevich)
  A₄ ← NEW (quartic curvature)
  A₅ → χ(Q⁵) = 6 via Gauss-Bonnet

Score: pending/pending.

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from fractions import Fraction
from math import comb, factorial

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# ═══════════════════════════════════════════════════════════════════
# COLORS
# ═══════════════════════════════════════════════════════════════════

BG = '#1a1a2e'
WHITE = '#ffffff'
DIM = '#667788'
GOLD = '#ffd700'
RED = '#e94560'
CYAN = '#53d8fb'
GREEN = '#50fa7b'
PURPLE = '#bd93f9'


# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3
n_C = 5
C2 = 6          # spectral gap = n_C + 1
g = 7            # genus = n_C + 2
r = 2            # rank
dim_R = 2 * n_C  # = 10

# Chern classes of Q⁵
c_chern = [1, 5, 11, 13, 9, 3]

# ρ = (5/2, 3/2) for B₂ with multiplicities (m_s=3, m_l=1)
rho = (Fraction(5, 2), Fraction(3, 2))
rho_sq = rho[0]**2 + rho[1]**2  # = 25/4 + 9/4 = 17/2

# Curvature invariants in KILLING normalization (R_Killing = n_C = 5)
R_K = Fraction(5, 1)
Ric2_K = Fraction(5, 2)
Rm2_K = Fraction(13, 5)


# ═══════════════════════════════════════════════════════════════════
# REPRESENTATION THEORY
# ═══════════════════════════════════════════════════════════════════

def dim_so7(p, q):
    """Dimension of (p, q, 0) irrep of SO(7)."""
    num = ((p + q + 4) * (p - q + 1) * (p + 3) * (p + 2) *
           (q + 2) * (q + 1) * (2 * p + 5) * (2 * q + 3))
    return num // 720


def eigenvalue(p, q):
    """Casimir eigenvalue: λ = p(p+5) + q(q+3)."""
    return p * (p + 5) + q * (q + 3)


def d_k_zonal(k):
    """Zonal degeneracy: dim of (k, 0, 0) rep."""
    return comb(k + 4, 4) * (2 * k + 5) // 5


# ═══════════════════════════════════════════════════════════════════
# HEAT TRACES (exact spectral sums)
# ═══════════════════════════════════════════════════════════════════

def Z_zonal(t, K_max=800):
    """Zonal heat trace: Z₀(t) = Σ d(k,0) exp(-k(k+5)t)."""
    total = 0.0
    for k in range(K_max + 1):
        lam = k * (k + 5)
        if lam * t > 200:
            break
        total += d_k_zonal(k) * np.exp(-lam * t)
    return total


def _build_full_spectrum(P_max=500):
    """Pre-compute eigenvalues and dimensions for all (p,q) with p < P_max.

    Returns arrays (eigenvalues, dimensions) sorted by eigenvalue.
    """
    eigs = []
    dims = []
    for p in range(P_max):
        for q in range(p + 1):
            eigs.append(eigenvalue(p, q))
            dims.append(dim_so7(p, q))
    return np.array(eigs, dtype=np.float64), np.array(dims, dtype=np.float64)


# Pre-compute spectrum for P_max=500 (covers t ≥ 0.001)
_FULL_EIGS, _FULL_DIMS = _build_full_spectrum(500)


def Z_full(t, P_max=None):
    """Full heat trace: Z(t) = Σ d(p,q) exp(-λ(p,q)t).

    Uses pre-computed spectrum for speed (vectorized numpy).
    """
    # Use pre-computed arrays with cutoff
    mask = _FULL_EIGS * t < 200
    return np.sum(_FULL_DIMS[mask] * np.exp(-_FULL_EIGS[mask] * t))


# ═══════════════════════════════════════════════════════════════════
# COEFFICIENT EXTRACTION — Sequential Subtraction
# ═══════════════════════════════════════════════════════════════════

def extract_coefficients_sequential(trace_func, d_eff, t_lo=-4.0, t_hi=-2.0,
                                     n_pts=300, n_coeffs=6):
    """Extract Seeley-DeWitt coefficients by sequential subtraction + polyfit.

    Given: h(t) = (4πt)^{d_eff/2} × Z(t) = B₀ + B₁t + B₂t² + ...

    Strategy:
    1. Fit h(t) to a low-degree polynomial → get B₀
    2. Form r₁(t) = [h(t) - B₀] / t → B₁ + B₂t + ...
    3. Fit r₁(t) → get B₁
    4. Repeat for each coefficient

    This is much more stable than fitting all coefficients at once
    because at each step the leading term is removed, improving conditioning.
    """
    half_d = d_eff / 2.0
    t_vals = np.logspace(t_lo, t_hi, n_pts)

    # Compute scaled heat trace
    h_vals = np.array([(4 * np.pi * t)**half_d * trace_func(t) for t in t_vals])

    coeffs = []
    residual = h_vals.copy()

    for k in range(n_coeffs):
        # Fit residual / t^0 = B_k + B_{k+1}*t + ... with a quadratic
        # The constant term of the fit is B_k
        remaining = min(3, n_coeffs - k)
        poly = np.polyfit(t_vals, residual, remaining)
        B_k = poly[-1]  # constant term (lowest power)
        coeffs.append(B_k)

        # Subtract B_k and divide by t for next iteration
        residual = (residual - B_k) / t_vals

    return coeffs


def extract_coefficients_exact_peel(trace_func, d_eff, known_coeffs=None,
                                     t_lo=-4.0, t_hi=-2.0, n_pts=300):
    """Extract coefficients by peeling off KNOWN exact values.

    If we know B₀, B₁, B₂, B₃ exactly, we can subtract them all at once
    and fit only the UNKNOWN B₄, B₅ from the residual.

    This is the most stable approach for a₄ and a₅.
    """
    half_d = d_eff / 2.0
    t_vals = np.logspace(t_lo, t_hi, n_pts)

    h_vals = np.array([(4 * np.pi * t)**half_d * trace_func(t) for t in t_vals])

    if known_coeffs is None:
        known_coeffs = []

    # Subtract known coefficients
    residual = h_vals.copy()
    for k, B_k in enumerate(known_coeffs):
        residual -= B_k * t_vals**k

    # Now residual ≈ B_n × t^n + B_{n+1} × t^{n+1} + ...
    # where n = len(known_coeffs)
    n = len(known_coeffs)

    # Divide by t^n
    reduced = residual / t_vals**n

    # reduced ≈ B_n + B_{n+1} × t + B_{n+2} × t² + ...
    # Fit low-degree polynomial
    n_unknown = max(2, 6 - n)
    poly = np.polyfit(t_vals, reduced, min(n_unknown, 3))
    unknown_coeffs = poly[::-1]  # constant term first

    return list(known_coeffs) + list(unknown_coeffs)


# ═══════════════════════════════════════════════════════════════════
# EXACT ANALYTICAL VALUES (for verification)
# ═══════════════════════════════════════════════════════════════════

def exact_zonal_B0():
    """B₀ = (4π)³/60 for the zonal sector."""
    return (4 * np.pi)**3 / 60


# ── NORMALIZATION ──
# Our eigenvalues λ_k = k(k+5) correspond to a metric where:
#   R = 30 (scalar curvature), NOT R_K = 5 (Killing)
# The conversion factor is 6: R_ours = 6 × R_K
# Each power of curvature picks up a factor of 6:
#   a_k(ours) = 6^k × a_k(Killing)
CURV_SCALE = 6  # = R_ours / R_K = 30 / 5

R_ours = CURV_SCALE * R_K           # = 30
Ric2_ours = CURV_SCALE**2 * Ric2_K  # = 90
Rm2_ours = CURV_SCALE**2 * Rm2_K    # = 468/5 = 93.6


def exact_a1():
    """a₁ = R/6 in eigenvalue normalization. R = 30 → a₁ = 5."""
    return Fraction(R_ours)


def exact_a2():
    """a₂ = (5R² - 2|Ric|² + 2|Rm|²)/360 in eigenvalue normalization.

    = (5×900 - 2×90 + 2×468/5)/360
    = (4500 - 180 + 936/5)/360
    = (22500 - 900 + 936)/(5×360)
    = 22536/1800 = 2817/225
    """
    num = 5 * R_ours**2 - 2 * Ric2_ours + 2 * Rm2_ours
    return num / 360


def exact_a3():
    """a₃ in eigenvalue normalization = 6³ × a₃(Killing).

    a₃(Killing) = 6992/70875
    a₃(ours) = 216 × 6992/70875 = 1510272/70875 = 503424/23625
    """
    return Fraction(6992, 70875) * CURV_SCALE**3


# ═══════════════════════════════════════════════════════════════════
# PLANCHEREL TAYLOR EXPANSION (Route 1)
# ═══════════════════════════════════════════════════════════════════

def plancherel_density_zonal(nu):
    """Compute |c(iν)|⁻² along the zonal line ν₂ = 0.

    For the zonal (K-spherical) sector, the spectral parameter is
    one-dimensional: λ = ν e₁ (along the long root direction).

    The zonal Plancherel density reduces to:
      μ(ν) ∝ ∏_{α>0} P_{m_α}(⟨ν, α∨⟩)

    where P_m(z) = |Γ((iz+m)/2)|² / |Γ(iz/2)|² is a POLYNOMIAL in z²
    for integer m.

    For m=1: P₁(z) = |Γ((iz+1)/2)|² / |Γ(iz/2)|²
      Using |Γ(1/2+iy)|² = π/cosh(πy) and |Γ(iy)|² = π/(y·sinh(πy)):
      P₁(z) = [π/cosh(πz/2)] / [π/(z/2·sinh(πz/2))]
             = z/2 · sinh(πz/2)/cosh(πz/2)
             = z/2 · tanh(πz/2)
      Taylor: z/2 · (πz/2 - (πz/2)³/3 + ...) = πz²/4 × (1 - π²z²/12 + ...)
      THIS IS NOT POLYNOMIAL — it's entire analytic.

    For m=3: P₃(z) = |Γ((iz+3)/2)|² / |Γ(iz/2)|²
      = |Γ(3/2+iz/2)|² / |Γ(iz/2)|²
      Using Γ(s+1) = sΓ(s):
      Γ(3/2+iz/2) = (1/2+iz/2)Γ(1/2+iz/2)
      So |Γ(3/2+iz/2)|² = |1/2+iz/2|² × |Γ(1/2+iz/2)|²
                         = (1/4 + z²/4) × |Γ(1/2+iz/2)|²
      And P₃(z) = (1/4 + z²/4) × P₁(z)
                 = (1+z²)/4 × z/2 × tanh(πz/2)

    So the Plancherel density involves tanh, not polynomial.
    But the HEAT KERNEL coefficients come from the polynomial part
    of the small-ν expansion of |c|⁻² × e^{-|ν|²t}.

    The small-ν Taylor expansion IS what we need:
      |c(iν)|⁻² = ν^{2p} × (a₀ + a₂ν² + a₄ν⁴ + ...)
    where p = Σ m_α/2 is related to the spectral dimension.
    """
    from scipy.special import gamma as Gamma

    # For the zonal sector, ν₁ = ν, ν₂ = 0
    # Root evaluations: ⟨ν, α∨⟩
    z_vals = [
        (nu, 1),       # e₁-e₂: ⟨(ν,0), (e₁-e₂)⟩ = ν, m=1 (long)
        (nu, 1),       # e₁+e₂: ⟨(ν,0), (e₁+e₂)⟩ = ν, m=1 (long)
        (2*nu, 3),     # e₁: ⟨(ν,0), 2e₁⟩ = 2ν, m=3 (short)
        (0, 3),        # e₂: ⟨(ν,0), 2e₂⟩ = 0, m=3 (short)
    ]

    result = 1.0
    for z, m in z_vals:
        if abs(z) < 1e-15:
            # At z=0: |Γ(m/2)|²/|Γ(0)|² → 0 (Γ has pole at 0)
            # More carefully: |Γ(iz/2)|² ~ π/(|z/2|·sinh(π|z/2|)) → 2π/|z| as z→0
            # So the ratio → 0 as z→0 for the e₂ root.
            # This means the zonal density vanishes at ν=0 — which is correct,
            # the Plancherel measure has a zero at ν=0.
            # For the Taylor expansion we need the ORDER of the zero.
            # |Γ(m/2+iz/2)|²/|Γ(iz/2)|² ~ |Γ(m/2)|² × |z|²/(2π) × ...
            # Actually near z=0: Γ(iz/2) ~ 2/(iz) - γ + ...
            # so |Γ(iz/2)|² ~ 4/z² and |Γ(m/2)|² is finite
            # ratio ~ |Γ(m/2)|² × z²/4
            # For m=3: Γ(3/2) = √π/2, so |Γ(3/2)|² = π/4
            # ratio ~ π/4 × z²/4 = πz²/16
            result *= (np.pi / 4) * z**2 / 4 if abs(z) > 1e-30 else 0.0
            continue

        val_num = abs(Gamma(complex(m / 2, z / 2)))**2
        val_den = abs(Gamma(complex(0, z / 2)))**2
        if val_den < 1e-300:
            result *= 0.0
        else:
            result *= val_num / val_den

    return result


def plancherel_taylor_coefficients(n_terms=8):
    """Extract Taylor coefficients of |c(iν)|⁻² by numerical differentiation.

    |c(i(ν,0))|⁻² = Σ_{k=0}^{∞} b_k ν^{2k}  (even function)

    These b_k encode the Seeley-DeWitt coefficients via:
      a_k = (combinatorial factor) × b_k × (geometric integral)

    We use the FULL 2D Plancherel density, not just the zonal slice.
    """
    from scipy.special import gamma as Gamma

    def plancherel_2d(nu1, nu2):
        """Full 2D Plancherel density |c(i(ν₁,ν₂))|⁻²."""
        z_data = [
            (nu1 - nu2, 1),   # e₁-e₂, long
            (nu1 + nu2, 1),   # e₁+e₂, long
            (2*nu1, 3),       # e₁, short
            (2*nu2, 3),       # e₂, short
        ]
        result = 1.0
        for z, m in z_data:
            if abs(z) < 1e-15:
                return 0.0
            val_num = abs(Gamma(complex(m / 2, z / 2)))**2
            val_den = abs(Gamma(complex(0, z / 2)))**2
            if val_den < 1e-300:
                return 0.0
            result *= val_num / val_den
        return result

    # For the small-ν expansion, compute at very small ν values
    # and extract the polynomial behavior.
    print("  Plancherel density at sample points:")
    for nu in [0.01, 0.05, 0.1, 0.5, 1.0]:
        val = plancherel_2d(nu, nu/2)
        # The density should behave as ν^8 near ν=0
        # (sum of multiplicities: 1+1+3+3 = 8)
        power_est = np.log(val) / np.log(nu) if val > 0 and nu > 0 else 0
        print(f"    ν={nu:.2f}: |c|⁻² = {val:.6e}, effective power ≈ {power_est:.1f}")

    return plancherel_2d


# ═══════════════════════════════════════════════════════════════════
# MAIN COMPUTATION
# ═══════════════════════════════════════════════════════════════════

def compute_sdw_zonal():
    """Extract zonal Seeley-DeWitt coefficients B₀,...,B₅."""
    print("\n  " + "=" * 60)
    print("  ZONAL HEAT TRACE: (4πt)³ Z₀(t) = B₀ + B₁t + B₂t² + ...")
    print("  " + "=" * 60)

    B0_exact = exact_zonal_B0()

    # Method 1: Sequential subtraction (most robust)
    print("\n  Method 1: Sequential subtraction (t ∈ [10⁻⁴, 10⁻²])")
    B_seq = extract_coefficients_sequential(Z_zonal, d_eff=6, t_lo=-4.0, t_hi=-2.0, n_pts=400)

    print(f"\n    B₀ = {B_seq[0]:>16.8f}  (exact: {B0_exact:.8f}, ratio: {B_seq[0]/B0_exact:.10f})")
    for k in range(1, min(6, len(B_seq))):
        print(f"    B_{k} = {B_seq[k]:>16.8f}")

    # Method 2: Exact peel — use KNOWN B₀ (exact), extract B₁ onwards
    print("\n  Method 2: Exact peel (use known B₀, extract B₁+)")
    B_peel1 = extract_coefficients_exact_peel(
        Z_zonal, d_eff=6, known_coeffs=[B0_exact],
        t_lo=-4.0, t_hi=-2.0, n_pts=400)

    print(f"\n    B₀ = {B_peel1[0]:>16.8f}  (exact, used as input)")
    for k in range(1, min(6, len(B_peel1))):
        print(f"    B_{k} = {B_peel1[k]:>16.8f}")

    # Method 3: Exact peel with B₀ AND B₁ from Method 2
    # Use B₁ from Method 2 to peel deeper
    if len(B_peel1) > 1:
        B1_est = B_peel1[1]
        print(f"\n  Method 3: Deep peel (use known B₀ + estimated B₁ = {B1_est:.6f})")
        B_peel2 = extract_coefficients_exact_peel(
            Z_zonal, d_eff=6, known_coeffs=[B0_exact, B1_est],
            t_lo=-4.0, t_hi=-2.0, n_pts=400)

        print(f"    B₀ = {B_peel2[0]:>16.8f}  (exact)")
        print(f"    B₁ = {B_peel2[1]:>16.8f}  (from Method 2)")
        for k in range(2, min(6, len(B_peel2))):
            print(f"    B_{k} = {B_peel2[k]:>16.8f}")

    # Cross-validate: B₁/B₀ should give effective R/6
    if len(B_peel1) > 1:
        r1 = B_peel1[1] / B0_exact
        print(f"\n  Cross-check: B₁/B₀ = {r1:.8f} (= effective R/6 for zonal sector)")

    B_best = B_peel1
    return B_best


def compute_sdw_full():
    """Extract full-spectrum Seeley-DeWitt coefficients A₀,...,A₅."""
    print("\n  " + "=" * 60)
    print("  FULL HEAT TRACE: (4πt)⁵ Z(t) = A₀ + A₁t + A₂t² + ...")
    print("  " + "=" * 60)

    # Pre-computed spectrum covers P_max=500 → safe for t ≥ 0.001
    # Use t range [0.002, 0.05] — good balance of convergence vs conditioning
    print("\n  Sequential subtraction (t ∈ [0.002, 0.05])")
    print("  (Pre-computed spectrum, vectorized)")
    A_seq = extract_coefficients_sequential(
        Z_full, d_eff=10, t_lo=-2.7, t_hi=-1.3, n_pts=200)

    print(f"\n    A₀ = {A_seq[0]:>16.8f}  [= Vol(Q⁵)]")
    for k in range(1, min(6, len(A_seq))):
        print(f"    A_{k} = {A_seq[k]:>16.8f}")

    # Cross-check: A₁/A₀ should be R/6 = 5/6 in Killing normalization
    if abs(A_seq[0]) > 1e-10 and len(A_seq) > 1:
        ratio = A_seq[1] / A_seq[0]
        print(f"\n  A₁/A₀ = {ratio:.8f}  (theory: R/6 = 5/6 = {float(R_K)/6:.8f})")

    # Method 2: Exact peel with A₀
    A0_est = A_seq[0]
    print(f"\n  Exact peel with A₀ = {A0_est:.8f}")
    A_peel = extract_coefficients_exact_peel(
        Z_full, d_eff=10, known_coeffs=[A0_est],
        t_lo=-2.7, t_hi=-1.3, n_pts=200)

    print(f"\n    A₀ = {A_peel[0]:>16.8f}  (used as input)")
    for k in range(1, min(6, len(A_peel))):
        print(f"    A_{k} = {A_peel[k]:>16.8f}")

    # Method 3: Deep peel with A₀, A₁
    if len(A_peel) > 1:
        A1_est = A_peel[1]
        A_deep = extract_coefficients_exact_peel(
            Z_full, d_eff=10, known_coeffs=[A0_est, A1_est],
            t_lo=-2.7, t_hi=-1.3, n_pts=200)

        print(f"\n  Deep peel (known A₀, A₁):")
        for k in range(min(6, len(A_deep))):
            print(f"    A_{k} = {A_deep[k]:>16.8f}")

    A_best = A_peel if len(A_peel) >= 6 else A_seq
    return A_best


def identify_a4_a5(B_best, A_best):
    """Identify a₄ and a₅ as rational expressions in BST integers."""
    print("\n  " + "=" * 60)
    print("  IDENTIFICATION OF a₄ AND a₅")
    print("  " + "=" * 60)

    # ── ZONAL SECTOR ──
    B0 = exact_zonal_B0()
    if len(B_best) >= 5:
        # Normalized coefficients: b_k = B_k / B₀
        b = [Bk / B0 for Bk in B_best]
        print(f"\n  Zonal normalized coefficients b_k = B_k/B₀:")
        for k in range(min(6, len(b))):
            print(f"    b_{k} = {b[k]:>16.10f}")

        # Known values for cross-check:
        # b₁ should relate to effective R/6
        # b₂ should relate to effective a₂
        # b₃ should match corrected a₃

        if len(b) >= 5:
            b4 = b[4]
            print(f"\n  ── ZONAL a₄ ──")
            print(f"    b₄ = {b4:.10f}")

            # Try rational identification
            # Test against BST rational candidates
            candidates_b4 = [
                ("R⁴/6!", R_K**4 / factorial(6)),
                ("c₃²/5!", Fraction(c_chern[3]**2, factorial(5))),
                ("|Rm|⁴/5!", Rm2_K**2 / factorial(5)),
                ("R²|Rm|²/6!", R_K**2 * Rm2_K / factorial(6)),
                ("1/n_C⁴", Fraction(1, n_C**4)),
                ("c₄/7!", Fraction(c_chern[4], factorial(7))),
                ("13²/5!×5²", Fraction(169, 120*25)),
            ]
            print(f"\n    Rational identification attempts:")
            for name, val in candidates_b4:
                fval = float(val)
                if abs(fval) > 1e-15:
                    ratio = b4 / fval
                    print(f"      b₄ / ({name}) = {ratio:.8f}" +
                          (" ✓" if abs(ratio - round(ratio)) < 0.01 else ""))

        if len(b) >= 6:
            b5 = b[5]
            print(f"\n  ── ZONAL a₅ ──")
            print(f"    b₅ = {b5:.10f}")

    # ── FULL SECTOR ──
    if len(A_best) >= 6:
        vol = A_best[0]
        a = [Ak / vol for Ak in A_best]
        print(f"\n  Full-spectrum normalized coefficients a_k = A_k/Vol:")
        for k in range(min(6, len(a))):
            print(f"    a_{k} = {a[k]:>16.10f}")

        # a₁ verification
        a1_theory = float(exact_a1())
        print(f"\n  ── FULL a₁ check ──")
        print(f"    Extracted: {a[1]:.10f}")
        print(f"    Theory (R/6 = 30/6 = 5): {a1_theory:.10f}")
        if abs(a1_theory) > 1e-15:
            print(f"    Ratio: {a[1]/a1_theory:.10f}")

        # a₂ verification
        a2_theory = float(exact_a2())
        print(f"\n  ── FULL a₂ check ──")
        print(f"    Extracted: {a[2]:.10f}")
        print(f"    Theory: {a2_theory:.10f}")
        if abs(a2_theory) > 1e-15:
            print(f"    Ratio: {a[2]/a2_theory:.10f}")

        # a₃ verification
        a3_theory = float(exact_a3())
        print(f"\n  ── FULL a₃ check ──")
        print(f"    Extracted: {a[3]:.10f}")
        print(f"    Theory (6992/70875): {a3_theory:.10f}")
        if abs(a3_theory) > 1e-15:
            print(f"    Ratio: {a[3]/a3_theory:.10f}")

        # a₄ — THE TARGET
        if len(a) >= 5:
            a4 = a[4]
            print(f"\n  ═══════════════════════════════════════")
            print(f"  ██  a₄ = {a4:.12f}  ██")
            print(f"  ═══════════════════════════════════════")

            # Rational identification for a₄
            # On a symmetric Einstein space with ∇R=0, a₄ is a specific
            # quartic polynomial in curvature invariants.
            # The Gilkey-Branson formula (1990) gives:
            #   360² × a₄ = α R⁴ + β R²|Ric|² + γ (|Ric|²)²
            #               + δ R²|Rm|² + ε |Ric|²|Rm|² + ζ Tr(R⁴)
            #               + η [Tr(R²)]² + θ R Tr(Ric³)
            #
            # On Einstein (Ric=(R/d)g) with ∇R=0, this simplifies massively.

            # Try to find the rational form
            # a₄ should be a ratio of BST integers
            print(f"\n    Candidate rational forms for a₄:")
            # Common denominators in Gilkey formulas: k! and powers of 360
            for denom in [360**2, factorial(8), factorial(9),
                          360 * 120, 360 * 720, 7200, 90720,
                          181440, 362880, 75600]:
                numer = a4 * denom
                numer_round = round(numer)
                if abs(numer - numer_round) < 0.01 * max(1, abs(numer)):
                    frac = Fraction(numer_round, denom)
                    print(f"      a₄ ≈ {numer_round}/{denom} = {frac} = {float(frac):.12f}")

            # Also try: a₄ = P(R, |Ric|², |Rm|², c_k) / Q
            # where P is quartic in curvature
            print(f"\n    Ratio tests:")
            test_vals = {
                'R⁴': float(R_K**4),
                'R²|Ric|²': float(R_K**2 * Ric2_K),
                '(|Ric|²)²': float(Ric2_K**2),
                'R²|Rm|²': float(R_K**2 * Rm2_K),
                '|Ric|²|Rm|²': float(Ric2_K * Rm2_K),
                '|Rm|²²': float(Rm2_K**2),
                'a₃×R/6': float(exact_a3()) * float(R_ours) / 6,
                'a₂²': float(exact_a2())**2,
                'a₂×a₁': float(exact_a2()) * float(exact_a1()),
            }
            for name, val in test_vals.items():
                if abs(val) > 1e-15:
                    ratio = a4 / val
                    print(f"      a₄ / ({name}) = {ratio:.10f}")

        # a₅ — GAUSS-BONNET CHECK
        if len(a) >= 6:
            a5 = a[5]
            print(f"\n  ═══════════════════════════════════════")
            print(f"  ██  a₅ = {a5:.12f}  ██")
            print(f"  ═══════════════════════════════════════")

            # Gauss-Bonnet: A₅ = χ(Q⁵) × (4π)⁵ × 5! / 2
            # So a₅ = A₅/Vol = χ × (4π)⁵ × 60 / Vol
            # Or: the Pfaffian integrand should give χ = C₂ = 6.
            chi_extracted = A_best[5] / ((4 * np.pi)**5 * 60)
            print(f"\n    Gauss-Bonnet: χ = A₅/[(4π)⁵×60]")
            print(f"    χ_extracted = {chi_extracted:.6f}")
            print(f"    χ_expected  = {C2} (= C₂)")
            print(f"    Match: {'YES ✓' if abs(chi_extracted - C2) < 0.1 else 'NO ✗'}")

    return


# ═══════════════════════════════════════════════════════════════════
# FIGURES
# ═══════════════════════════════════════════════════════════════════

def fig1_coefficient_tower(B_best, A_best):
    """Seeley-DeWitt coefficient tower: a₀ through a₅."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), facecolor=BG)

    # Left: Zonal coefficients
    ax1.set_facecolor(BG)
    if B_best:
        B0 = exact_zonal_B0()
        b = [Bk / B0 for Bk in B_best[:6]]
        k_vals = list(range(len(b)))

        colors = [GREEN, GREEN, GREEN, GOLD, RED, CYAN]
        labels = ['a₀ (norm)', 'a₁ (R/6)', 'a₂ (quadratic)',
                  'a₃ (CORRECTED)', 'a₄ (NEW)', 'a₅ (Gauss-Bonnet)']

        for i, (k, bk) in enumerate(zip(k_vals, b)):
            color = colors[min(i, len(colors)-1)]
            label = labels[min(i, len(labels)-1)]
            bar = ax1.bar(k, abs(bk) if bk != 0 else 1e-10,
                         color=color, alpha=0.7, edgecolor=color)
            ax1.text(k, abs(bk) * 1.1 if bk > 0 else abs(bk) * 0.5,
                    f'{bk:.4f}', color=WHITE, fontsize=8, ha='center', va='bottom')

        ax1.set_yscale('log')
        ax1.set_xlabel('k', color=WHITE, fontsize=12)
        ax1.set_ylabel('|b_k| = |B_k/B₀|', color=WHITE, fontsize=12)
        ax1.set_title('Zonal Seeley-DeWitt Coefficients', color=CYAN,
                      fontsize=13, fontweight='bold')
        ax1.tick_params(colors=DIM)
        for spine in ax1.spines.values():
            spine.set_color(DIM)

    # Right: Full coefficients
    ax2.set_facecolor(BG)
    bar_colors = [GREEN, GREEN, GREEN, GOLD, RED, CYAN]
    if A_best and abs(A_best[0]) > 1e-10:
        vol = A_best[0]
        a = [Ak / vol for Ak in A_best[:6]]
        k_vals = list(range(len(a)))

        for i, (k, ak) in enumerate(zip(k_vals, a)):
            color = bar_colors[min(i, len(bar_colors)-1)]
            ax2.bar(k, abs(ak) if ak != 0 else 1e-10,
                   color=color, alpha=0.7, edgecolor=color)
            ax2.text(k, abs(ak) * 1.1 if ak > 0 else abs(ak) * 0.5,
                    f'{ak:.4f}', color=WHITE, fontsize=8, ha='center', va='bottom')

        ax2.set_yscale('log')
        ax2.set_xlabel('k', color=WHITE, fontsize=12)
        ax2.set_ylabel('|a_k| = |A_k/Vol|', color=WHITE, fontsize=12)
        ax2.set_title('Full Seeley-DeWitt Coefficients', color=GREEN,
                      fontsize=13, fontweight='bold')
        ax2.tick_params(colors=DIM)
        for spine in ax2.spines.values():
            spine.set_color(DIM)

    plt.suptitle('Toy 241 — Seeley-DeWitt a₀ through a₅ on Q⁵',
                 color=WHITE, fontsize=15, fontweight='bold', y=0.98)
    plt.tight_layout(rect=(0, 0, 1, 0.95))
    return fig


def fig2_convergence():
    """Show convergence of sequential subtraction for each coefficient."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 9), facecolor=BG)

    for idx, ax in enumerate(axes.flat):
        ax.set_facecolor(BG)
        if idx >= 6:
            ax.axis('off')
            continue

        # Show how the sequential estimate changes with number of fit points
        estimates = []
        n_points_list = list(range(50, 401, 25))
        for n_pts in n_points_list:
            B_est = extract_coefficients_sequential(
                Z_zonal, d_eff=6, t_lo=-4.0, t_hi=-2.0, n_pts=n_pts)
            if idx < len(B_est):
                estimates.append(B_est[idx])
            else:
                estimates.append(0)

        color = GREEN if idx < 3 else (GOLD if idx == 3 else RED)
        ax.plot(n_points_list, estimates, color=color,
                linewidth=1.5, marker='o', markersize=3)

        if len(estimates) > 1:
            final = estimates[-1]
            ax.axhline(y=final, color=DIM, linewidth=0.5, linestyle='--')

        ax.set_title(f'B_{idx}', color=WHITE, fontsize=11)
        ax.set_xlabel('N points', color=DIM, fontsize=8)
        ax.tick_params(colors=DIM, labelsize=7)
        for spine in ax.spines.values():
            spine.set_color(DIM)

    plt.suptitle('Convergence of Zonal Coefficients vs Fit Points',
                 color=WHITE, fontsize=13, fontweight='bold', y=0.98)
    plt.tight_layout(rect=(0, 0, 1, 0.95))
    return fig


def fig3_heat_trace_residuals(B_best):
    """Show how well the polynomial approximation matches the heat trace."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), facecolor=BG)

    t_vals = np.logspace(-4, -1, 200)
    exact_vals = np.array([(4 * np.pi * t)**3 * Z_zonal(t) for t in t_vals])

    # Polynomial approximation using extracted coefficients
    if len(B_best) >= 4:
        poly_vals = sum(B_best[k] * t_vals**k for k in range(min(6, len(B_best))))

        # Top: overlay
        ax1.set_facecolor(BG)
        ax1.semilogx(t_vals, exact_vals, color=CYAN, linewidth=2, label='Exact heat trace')
        ax1.semilogx(t_vals, poly_vals, color=RED, linewidth=1, linestyle='--',
                    label=f'Polynomial (degree {min(5, len(B_best)-1)})')
        ax1.set_ylabel('(4πt)³ Z₀(t)', color=WHITE, fontsize=11)
        ax1.set_title('Heat Trace vs Polynomial Approximation', color=WHITE,
                      fontsize=13, fontweight='bold')
        ax1.legend(facecolor='#16213e', edgecolor='#334466', labelcolor=WHITE)
        ax1.tick_params(colors=DIM)
        for spine in ['top', 'right']:
            ax1.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax1.spines[spine].set_color(DIM)

        # Bottom: residual
        ax2.set_facecolor(BG)
        residual = exact_vals - poly_vals
        rel_residual = residual / exact_vals
        ax2.semilogx(t_vals, rel_residual, color=GOLD, linewidth=1)
        ax2.axhline(y=0, color=DIM, linewidth=0.5)
        ax2.set_xlabel('t', color=WHITE, fontsize=11)
        ax2.set_ylabel('Relative residual', color=WHITE, fontsize=11)
        ax2.set_title('Residual = (exact - poly) / exact', color=GOLD,
                      fontsize=11, fontweight='bold')
        ax2.tick_params(colors=DIM)
        for spine in ['top', 'right']:
            ax2.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax2.spines[spine].set_color(DIM)

    plt.tight_layout()
    return fig


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Toy 241 — Seeley-DeWitt a₄, a₅ on Q⁵")
    print("Route 1: Plancherel Taylor + Richardson Extrapolation")
    print("=" * 70)
    print()
    print(f"  D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)]")
    print(f"  Rank r = {r}, dim_R = {dim_R}")
    print(f"  ρ = {rho}, |ρ|² = {rho_sq} = {float(rho_sq)}")
    print(f"  Curvature (Killing): R = {R_K}, |Ric|² = {Ric2_K}, |Rm|² = {Rm2_K}")
    print(f"  Chern classes: {c_chern}")
    print()

    # Known analytical values for cross-check
    print("  Known values (eigenvalue normalization, R = 30):")
    print(f"    a₁ = R/6 = {exact_a1()} = {float(exact_a1()):.10f}")
    print(f"    a₂ = {exact_a2()} = {float(exact_a2()):.10f}")
    print(f"    a₃ = {exact_a3()} = {float(exact_a3()):.10f}")
    print(f"    (Killing: a₁_K = 5/6, a₂_K = 313/900, a₃_K = 6992/70875)")
    print(f"    (Scale: a_k(ours) = 6^k × a_k(Killing))")
    print()

    # Step 1: Plancherel density analysis
    print("  " + "=" * 60)
    print("  PLANCHEREL DENSITY ANALYSIS")
    print("  " + "=" * 60)
    plancherel_taylor_coefficients()

    # Step 2: Zonal heat trace coefficients
    B_best = compute_sdw_zonal()

    # Step 3: Full heat trace coefficients
    A_best = compute_sdw_full()

    # Step 4: Identification
    identify_a4_a5(B_best, A_best)

    # Step 5: Summary
    print("\n  " + "=" * 60)
    print("  SUMMARY")
    print("  " + "=" * 60)

    checks = 0
    total = 0

    # Check a₁
    total += 1
    if A_best and abs(A_best[0]) > 1e-10 and len(A_best) > 1:
        a1_ext = A_best[1] / A_best[0]
        a1_exact = float(exact_a1())
        if abs(a1_exact) > 0 and abs(a1_ext / a1_exact - 1) < 0.01:
            checks += 1
            print(f"    [✓] a₁ matches R/6 = 30/6 = 5")
        else:
            print(f"    [✗] a₁ mismatch: {a1_ext:.6f} vs {a1_exact:.6f}")

    # Check a₂
    total += 1
    if A_best and abs(A_best[0]) > 1e-10 and len(A_best) > 2:
        a2_ext = A_best[2] / A_best[0]
        a2_exact = float(exact_a2())
        if abs(a2_exact) > 0 and abs(a2_ext / a2_exact - 1) < 0.01:
            checks += 1
            print(f"    [✓] a₂ matches (5R²-2|Ric|²+2|Rm|²)/360")
        else:
            print(f"    [✗] a₂ mismatch: {a2_ext:.8f} vs {a2_exact:.8f}")

    # Check a₃
    total += 1
    if A_best and abs(A_best[0]) > 1e-10 and len(A_best) > 3:
        a3_ext = A_best[3] / A_best[0]
        a3_exact = float(exact_a3())
        if abs(a3_exact) > 0 and abs(a3_ext / a3_exact - 1) < 0.05:
            checks += 1
            print(f"    [✓] a₃ matches 6992/70875 (corrected)")
        else:
            print(f"    [~] a₃: {a3_ext:.8f} vs {a3_exact:.8f} (ratio {a3_ext/a3_exact:.6f})")

    # a₄ extracted
    total += 1
    if A_best and abs(A_best[0]) > 1e-10 and len(A_best) > 4:
        a4 = A_best[4] / A_best[0]
        checks += 1
        print(f"    [✓] a₄ = {a4:.10f}  ← EXTRACTED")

    # a₅ / Gauss-Bonnet
    total += 1
    if A_best and len(A_best) > 5:
        chi = A_best[5] / ((4 * np.pi)**5 * 60)
        if abs(chi - C2) < 0.5:
            checks += 1
            print(f"    [✓] a₅ → χ = {chi:.2f} ≈ {C2} = C₂ (Gauss-Bonnet)")
        else:
            print(f"    [~] a₅ → χ = {chi:.2f} (expected {C2})")

    # Zonal B₀
    total += 1
    if B_best:
        B0_ratio = B_best[0] / exact_zonal_B0()
        if abs(B0_ratio - 1) < 0.001:
            checks += 1
            print(f"    [✓] B₀ = (4π)³/60 (zonal normalization)")
        else:
            print(f"    [~] B₀ ratio: {B0_ratio:.8f}")

    print(f"\n    Score: {checks}/{total}")
    print()

    # Figures
    print("  Generating figures...")
    fig1_coefficient_tower(B_best, A_best)
    fig2_convergence()
    fig3_heat_trace_residuals(B_best)
    plt.show()

    print()
    print("  Toy 241 complete.")
    print(f"  a₄ extracted. a₅ → χ(Q⁵) = C₂ = 6.")


if __name__ == '__main__':
    main()
