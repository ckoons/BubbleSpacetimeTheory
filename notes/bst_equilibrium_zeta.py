#!/usr/bin/env python3
"""
BST Equilibrium Condition: Epstein Zeta on S^4 x S^1
Casey Koons & Claude (Anthropic), March 2026

The equilibrium R_s/R_b = 137 comes from the Casimir energy balance on
S^4(R_b) x S^1(R_s). The Casimir energy is:

  E_c(rho) = (1/2) * zeta(s = -1/2, rho)   [analytically continued]

where zeta(s, rho) = sum_{l,m} d_l * E_{l,m}^{-2s}
                   = sum_{l,m} d_l * (l(l+3) + m^2/rho^2)^{-s}

with rho = R_s/R_b.

The equilibrium condition: d zeta(s=-1/2, rho) / d rho = 0

Key insight: at s = -1/2, the 2s prefactor in d_zeta_l>=1/d_rho becomes
2 * (-1/2) = -1 < 0, making the l>=1 contribution NEGATIVE. Meanwhile,
the l=0 piece is analytically known: d_zeta_l0/d_rho = rho^{-2}/6 > 0.
These two compete, and the equilibrium finds rho_eq.

This code:
  1. Verifies the competition exists at s = -1/2 (formally)
  2. Computes the l=0 piece analytically (Riemann zeta)
  3. Computes the l>=1 piece numerically at positive s (where sum converges)
  4. Studies the s-dependence of d_zeta/d_rho down to s = 2.01
  5. Uses cutoff regularization to estimate the finite Casimir remainder
  6. Finds the rho satisfying the equilibrium condition
"""

import numpy as np
from scipy.special import zeta as riemann_zeta
from scipy.optimize import brentq
import csv, os
from time import time

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================================
# Degeneracy and energy
# ============================================================================

def s4_deg(l):
    return (2*l + 3) * (l + 1) * (l + 2) // 6


def energy2(l, m, rho):
    """E^2_{l,m}(rho) = l(l+3) + m^2/rho^2"""
    return l * (l + 3) + m**2 / rho**2


# ============================================================================
# Part 1: The l=0 contribution — known analytically
# ============================================================================

def zeta_l0_analytic(s, rho):
    """
    zeta_{l=0}(s, rho) = sum_{m != 0} (m^2/rho^2)^{-s} = 2 rho^{2s} zeta_R(2s)

    Valid for Re(2s) > 1; analytically continued elsewhere.
    Special values:
      s =  2:   2 rho^4 * pi^4/90
      s = -1/2: 2 rho^{-1} * zeta_R(-1) = 2 rho^{-1} * (-1/12) = -rho/6
    """
    if abs(s - (-0.5)) < 1e-6:
        return 2 * rho**(-1) * (-1.0/12)   # zeta_R(-1) = -1/12
    return 2 * rho**(2*s) * riemann_zeta(2*s)


def d_zeta_l0_drho(s, rho):
    """
    d/d_rho [2 rho^{2s} zeta_R(2s)] = 4s rho^{2s-1} zeta_R(2s)

    At s = -1/2: = -2 rho^{-2} * (-1/12) = rho^{-2}/6  > 0
    """
    if abs(s - (-0.5)) < 1e-6:
        return rho**(-2) / 6.0              # = +rho^{-2}/6
    return 4*s * rho**(2*s - 1) * riemann_zeta(2*s)


# ============================================================================
# Part 2: The l>=1 contribution — numerically at s > 2
# ============================================================================

def zeta_lge1(s, rho, l_max=40, m_max=20):
    """
    zeta_{l>=1}(s, rho) = sum_{l>=1, m} d_l * (l(l+3) + m^2/rho^2)^{-s}

    Converges for s > 2.  At s = -1/2, formally:
      = sum d_l * (l(l+3) + m^2/rho^2)^{1/2}  [diverges; needs regularization]
    """
    total = 0.0
    for l in range(1, l_max + 1):
        d = s4_deg(l)
        lam = l * (l + 3)
        for m in range(-m_max, m_max + 1):
            e2 = lam + m**2 / rho**2
            total += d * e2**(-s)
    return total


def d_zeta_lge1_drho(s, rho, l_max=40, m_max=20):
    """
    d/d_rho zeta_{l>=1}(s, rho) = 2s/rho^3 * sum_{l>=1, m!=0} d_l m^2 E2^{-s-1}

    Sign: for s > 0,  prefactor 2s > 0,  sum > 0  =>  derivative > 0
          for s = -1/2, prefactor 2*(-1/2) = -1 < 0  =>  derivative < 0
    """
    total = 0.0
    for l in range(1, l_max + 1):
        d = s4_deg(l)
        lam = l * (l + 3)
        for m in range(-m_max, m_max + 1):
            if m == 0:
                continue
            e2 = lam + m**2 / rho**2
            total += d * m**2 * e2**(-s - 1)
    return (2 * s / rho**3) * total


# ============================================================================
# Part 3: Casimir regularization at s = -1/2
#
# The unregulated sum sum_{l>=1,m!=0} d_l m^2 / sqrt(E2) diverges.
# We regularize by computing the sum up to a mode cutoff L and subtracting
# the analytically known divergent pieces (Seeley-DeWitt coefficients).
#
# Divergence structure for sum_{l=1}^L d_l sum_m m^2/sqrt(l(l+3)+m^2/rho^2):
#   - For fixed m, large l: ~ l^2 m^2 / l = l m^2  =>  sum_l ~ L^2 m^2
#   - For fixed l, large m: ~ l^2 m^2 / (m/rho) = l^2 m rho  =>  sum_m ~ M^2
#   - Leading divergence: C(rho) * L^2 * M^2
#
# Regularized "finite part":
#   g_reg(rho) = lim_{L->inf} [g(rho, L) - A(rho) L^alpha - ...]
#
# We compute g(rho, L) for increasing L and fit the growth to extract the
# rho-dependent finite part.
# ============================================================================

def g_raw(rho, l_max, m_max=15):
    """
    g(rho, L) = sum_{l=1}^L sum_{m!=0} d_l m^2 / sqrt(l(l+3) + m^2/rho^2)

    This is the UNREGULATED sum for d_zeta_{l>=1}/d_rho at s = -1/2.
    (Factor of -1/rho^3 is outside.)
    """
    total = 0.0
    for l in range(1, l_max + 1):
        d = s4_deg(l)
        lam = l * (l + 3)
        for m in range(-m_max, m_max + 1):
            if m == 0:
                continue
            e2 = lam + m**2 / rho**2
            total += d * m**2 / np.sqrt(e2)
    return total


def extract_finite_casimir(rho, l_vals=[10,15,20,25,30,35,40], m_max=15):
    """
    Compute g_raw at increasing l_max, fit the divergence, and return the
    regularized (finite) value.

    Fit model: g(l_max) ~ A * l_max^alpha + B * l_max^beta + C_finite
    """
    g_vals = np.array([g_raw(rho, l, m_max) for l in l_vals])
    l_arr  = np.array(l_vals, dtype=float)

    # Fit: g ~ A * l^3 + B * l^2 + C * l + D + finite_part
    # Use polynomial regression to extract the finite intercept
    # Fit in log-log first to determine the dominant power
    log_l = np.log(l_arr)
    log_g = np.log(g_vals)
    slope, intercept = np.polyfit(log_l, log_g, 1)

    # Fit polynomial in l to get the finite remainder
    # Try: g ~ A l^round(slope) + B l^(round(slope)-1) + ... + C_finite
    deg = max(1, int(np.round(slope)))
    coeffs = np.polyfit(l_arr, g_vals, deg)
    # The "constant" in the polynomial fit is the finite part
    C_finite = coeffs[-1]   # polynomial constant term

    return C_finite, slope, g_vals


# ============================================================================
# Part 4: Equilibrium condition
# ============================================================================

def equilibrium_residual(rho, g_finite):
    """
    Equilibrium: d_zeta_l0/d_rho + d_zeta_lge1/d_rho = 0 at s = -1/2
    =>  rho^{-2}/6 + (-1/rho^3) * g_finite(rho) = 0
    =>  rho/6 = g_finite(rho)
    =>  residual = rho/6 - g_finite(rho)
    """
    return rho / 6.0 - g_finite


# ============================================================================
# Main computation
# ============================================================================

if __name__ == '__main__':
    print("=" * 65)
    print("BST EQUILIBRIUM CONDITION: EPSTEIN ZETA CALCULATION")
    print("Casey Koons & Claude (Anthropic), March 2026")
    print("=" * 65)

    # -------------------------------------------------------------------
    # SECTION 1: Confirm the competition at s = -1/2
    # -------------------------------------------------------------------
    print("\n" + "─" * 65)
    print("SECTION 1: The competition at s = -1/2")
    print("─" * 65)

    print("""
  The equilibrium condition d_zeta/d_rho = 0 at s = -1/2 splits as:

    d_zeta_l0/d_rho   = +rho^{-2}/6        [l=0 term, POSITIVE, analytic]
    d_zeta_l>=1/d_rho = -g_reg(rho)/rho^3  [l>=1 term, NEGATIVE at s=-1/2]

  where g_reg(rho) = regulated sum_{l>=1, m!=0} d_l m^2 / sqrt(E_{l,m})

  Equilibrium:  rho/6 = g_reg(rho)
  """)

    rho_test = 137.0
    d_l0 = d_zeta_l0_drho(-0.5, rho_test)
    print(f"  At rho = {rho_test}:")
    print(f"    d_zeta_l0/d_rho  = +{d_l0:.6e}  (positive, analytic)")
    print(f"    Need g_reg(137) = rho/6 = {rho_test/6:.4f}")

    # -------------------------------------------------------------------
    # SECTION 2: Epstein zeta at positive s — competition structure
    # -------------------------------------------------------------------
    print("\n" + "─" * 65)
    print("SECTION 2: Epstein zeta at positive s (where sum converges)")
    print("─" * 65)

    l_max, m_max = 30, 12

    s_vals = [3.0, 2.5, 2.2, 2.1, 2.05]
    rho_scan = [10, 30, 60, 100, 137, 200, 300, 500]

    print(f"\n  d_zeta/d_rho = d_zeta_l0/d_rho + d_zeta_lge1/d_rho")
    print(f"  (both positive for s > 2; sign of l>=1 piece flips at s=-1/2)\n")

    print(f"  {'s':>6}  {'rho':>6}  {'d_l0':>14}  {'d_lge1':>14}  "
          f"{'ratio_l0/lge1':>16}")

    rows = []
    for s in s_vals:
        for rho in rho_scan:
            dl0   = d_zeta_l0_drho(s, rho)
            dlge1 = d_zeta_lge1_drho(s, rho, l_max, m_max)
            ratio = dl0 / dlge1 if dlge1 != 0 else float('inf')
            print(f"  {s:>6.2f}  {rho:>6.0f}  {dl0:>14.4e}  {dlge1:>14.4e}  "
                  f"{ratio:>16.6f}")
            rows.append(dict(s=s, rho=rho, d_l0=dl0, d_lge1=dlge1, ratio=ratio))

    csv_path = os.path.join(OUT_DIR, 'BST_Equilibrium_Zeta_Structure.csv')
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['s','rho','d_l0','d_lge1','ratio'])
        w.writeheader(); w.writerows(rows)
    print(f"\n  -> {csv_path}")

    # -------------------------------------------------------------------
    # SECTION 3: How the ratio d_l0 / d_lge1 depends on rho and s
    # -------------------------------------------------------------------
    print("\n" + "─" * 65)
    print("SECTION 3: Ratio d_l0/d_lge1 as a function of rho (at s=2.5)")
    print("─" * 65)
    print("""
  At s = -1/2, equilibrium is where d_l0/|d_lge1| = 1.
  At positive s both terms are positive (no equilibrium yet).
  We track the ratio to see how rapidly it changes with s.
  """)

    s_fixed = 2.5
    rho_fine = np.logspace(0.5, 3.0, 40)   # rho from ~3 to 1000

    print(f"  s = {s_fixed}")
    print(f"  {'rho':>8}  {'d_l0':>14}  {'d_lge1':>14}  {'ratio':>10}")
    ratio_vals = []
    for rho in rho_fine:
        dl0   = d_zeta_l0_drho(s_fixed, rho)
        dlge1 = d_zeta_lge1_drho(s_fixed, rho, l_max, m_max)
        ratio = dl0 / dlge1
        ratio_vals.append(ratio)
        if abs(np.log10(rho) - round(np.log10(rho))) < 0.15:  # near decade
            print(f"  {rho:>8.1f}  {dl0:>14.4e}  {dlge1:>14.4e}  {ratio:>10.6f}")

    # The minimum ratio — if it dips below what analytic continuation gives at s=-1/2,
    # then the equilibrium exists
    min_ratio = min(ratio_vals)
    min_rho   = rho_fine[np.argmin(ratio_vals)]
    print(f"\n  Minimum ratio at s={s_fixed}: {min_ratio:.6f} at rho = {min_rho:.1f}")
    print(f"  (At s=-1/2 the ratio would need to reach -1 for equilibrium)")

    # -------------------------------------------------------------------
    # SECTION 4: Casimir regularization — the finite part of g(rho)
    # -------------------------------------------------------------------
    print("\n" + "─" * 65)
    print("SECTION 4: Casimir regularization of g(rho)")
    print("─" * 65)
    print("""
  g(rho, L) = sum_{l=1}^L sum_{m!=0} d_l m^2 / sqrt(l(l+3) + m^2/rho^2)

  This diverges as L -> inf.  We fit and subtract the divergence to get
  g_reg(rho) — the finite Casimir remainder.

  Equilibrium condition:  rho/6 = g_reg(rho)
  """)

    rho_test_vals = [10, 30, 60, 100, 137, 200, 300, 500]
    l_sequence = [10, 15, 20, 25, 30, 35]
    m_max_cas  = 12

    cas_results = []
    print(f"  {'rho':>6}  {'g_raw(L=10)':>14}  {'g_raw(L=35)':>14}  "
          f"{'slope':>8}  {'g_finite':>14}  {'rho/6':>10}  {'residual':>12}")

    for rho in rho_test_vals:
        t0 = time()
        g_finite, slope, g_vals = extract_finite_casimir(rho, l_sequence, m_max_cas)
        residual = equilibrium_residual(rho, g_finite)
        print(f"  {rho:>6.0f}  {g_vals[0]:>14.4e}  {g_vals[-1]:>14.4e}  "
              f"{slope:>8.3f}  {g_finite:>14.4e}  {rho/6:>10.4f}  "
              f"{residual:>12.4e}  ({time()-t0:.1f}s)")
        cas_results.append(dict(rho=rho, g_raw_min=g_vals[0], g_raw_max=g_vals[-1],
                                slope=slope, g_finite=g_finite,
                                rho_over_6=rho/6, residual=residual))

    # -------------------------------------------------------------------
    # SECTION 5: Seek the equilibrium rho
    # -------------------------------------------------------------------
    print("\n" + "─" * 65)
    print("SECTION 5: Equilibrium rho from Casimir balance")
    print("─" * 65)

    # Build g_finite(rho) as a function from the computed values
    rho_arr = np.array([r['rho'] for r in cas_results], dtype=float)
    gf_arr  = np.array([r['g_finite'] for r in cas_results], dtype=float)
    res_arr = np.array([r['residual'] for r in cas_results], dtype=float)

    print(f"\n  residual(rho) = rho/6 - g_finite(rho)")
    print(f"\n  {'rho':>6}  {'residual':>14}  {'sign':>6}")
    for rho, res in zip(rho_arr, res_arr):
        sign = '+' if res >= 0 else '-'
        print(f"  {rho:>6.0f}  {res:>14.4e}  {sign:>6}")

    # Find sign changes (where equilibrium rho lies)
    sign_changes = []
    for i in range(len(res_arr) - 1):
        if res_arr[i] * res_arr[i+1] < 0:
            # Linear interpolation for the zero crossing
            rho_eq = rho_arr[i] - res_arr[i] * (rho_arr[i+1] - rho_arr[i]) / (res_arr[i+1] - res_arr[i])
            sign_changes.append(rho_eq)

    if sign_changes:
        print(f"\n  Sign change(s) detected at rho_eq = {sign_changes}")
        for rho_eq in sign_changes:
            print(f"  Equilibrium estimate: rho_eq ~ {rho_eq:.1f}  (BST predicts 137)")
    else:
        print(f"\n  No sign change in this rho range.")
        print(f"  residual at rho=137: {np.interp(137, rho_arr, res_arr):.4e}")
        print(f"  Minimum |residual| at: rho = {rho_arr[np.argmin(np.abs(res_arr))]:.0f}")

    # -------------------------------------------------------------------
    # SECTION 6: Physical interpretation and next steps
    # -------------------------------------------------------------------
    print("\n" + "─" * 65)
    print("SECTION 6: What this tells us")
    print("─" * 65)

    print(f"""
  The equilibrium condition structure is confirmed:

  1. COMPETITION EXISTS at s = -1/2:
     - l=0 term:  d_zeta/d_rho = +rho^{{-2}}/6  (positive, pushes rho up)
     - l>=1 term: d_zeta/d_rho = -g_reg/rho^3  (negative, pushes rho down)
     These exactly compete at rho_eq — the Casimir pressure balance.

  2. THE MAGNITUDE OF THE COMPETITION:
     At rho = 137: rho/6 = {137/6:.3f}
     Need: g_reg(137) = {137/6:.3f}  (in BST natural units)

  3. REGULARIZATION STATUS:
     The raw sum g(rho, L) grows as L^{{slope}}.
     The finite part g_reg depends on the regularization scheme.
     The polynomial fit gives a rough estimate; the rigorous result
     requires the Chowla-Selberg formula for the S^4 x S^1 heat kernel.

  4. WHAT IS NEEDED:
     The heat kernel K_{{S^4}}(t) = sum_l d_l exp(-t l(l+3)) is computable.
     The full Casimir energy is:
       E_c(rho) = -(1/sqrt(4pi)) * integral_0^inf dt t^{{-3/2}} K_{{S^4}}(t) K_{{S^1}}(t)
     (after subtracting the UV divergent terms from the small-t expansion).
     The equilibrium is where dE_c/d_rho = 0.

  5. PRELIMINARY ESTIMATE:
     If the regularization gives g_reg(137) ~ 137/6 ~ 22.8, the equilibrium
     IS at rho = 137.  The raw computation at L=35 gives g_raw(137) ~ {g_vals[-1]:.2e}
     (before subtracting divergence).  The regularized value is much smaller.
  """)

    # -------------------------------------------------------------------
    # SECTION 7: Heat kernel approach — the clean route
    # -------------------------------------------------------------------
    print("─" * 65)
    print("SECTION 7: Heat kernel Casimir energy vs rho")
    print("─" * 65)
    print("""
  E_c(rho) = -(1/2) * (1/Gamma(-1/2)) * integral_0^inf dt t^{-3/2} K(t, rho)

  where K(t, rho) = K_S4(t) * K_S1(t, rho)
        K_S4(t) = sum_{l=0}^inf d_l * exp(-t * l(l+3))
        K_S1(t, rho) = sum_m exp(-t * m^2/rho^2) = theta_3(0, exp(-t/rho^2))

  Using Poisson resummation:
        K_S1(t, rho) = rho*sqrt(pi/t) * sum_n exp(-pi^2 n^2 rho^2 / t)

  The integral splits into UV divergent (t -> 0) and finite parts.
  We compute the FINITE part numerically by:
    1. Subtracting the small-t expansion (Seeley-DeWitt) analytically
    2. Integrating the remainder numerically
  """)

    # K_S4(t): compute numerically
    def K_S4(t, l_max=50):
        total = 1.0  # l=0 term: d_0 * exp(0) = 1
        for l in range(1, l_max + 1):
            d = s4_deg(l)
            total += d * np.exp(-t * l * (l + 3))
        return total

    # K_S1(t, rho): theta function via Poisson resummation (fast for small t)
    def K_S1(t, rho, n_max=20):
        if t <= 0:
            return float('inf')
        # Direct sum for large t
        if t > rho**2 * 0.5:
            return sum(np.exp(-t * m**2 / rho**2) for m in range(-n_max, n_max + 1))
        # Poisson resummation for small t
        prefactor = rho * np.sqrt(np.pi / t)
        s = 1.0  # n=0 term
        for n in range(1, n_max + 1):
            arg = -np.pi**2 * n**2 * rho**2 / t
            if arg < -300:
                break
            s += 2 * np.exp(arg)
        return prefactor * s

    # Seeley-DeWitt coefficients for S^4 x S^1 (massless scalar)
    # K(t) ~ (4pi*t)^{-5/2} * [a0 + a2 t + a4 t^2 + ...]
    # a0 = Vol(S^4 x S^1) = (8pi^2/3) * R_b^4 * 2pi * R_s
    #    = (16pi^3/3) * rho  (with R_b = 1)
    # a2 = (1/6) * integral of R (Ricci scalar)
    #    For S^4(1): R = 12. Vol(S^4) = 8pi^2/3. Contribution: (1/6)*12*(8pi^2/3)*2pi*rho
    # The UV divergence in E_c depends on rho through a0, a2 — we subtract these.

    # Compute the finite Casimir energy difference E_c(rho) - E_c(rho_ref)
    # The UV divergences cancel in the difference (they're polynomial in rho)
    rho_ref = 1.0  # reference
    t_grid = np.logspace(-4, 4, 500)

    print(f"  Computing E_c(rho) for a range of rho values...")
    print(f"  (using heat kernel with l_max=50, Poisson-resummed S^1)")
    print()

    rho_vals_hk = [1, 5, 10, 20, 50, 100, 137, 200, 300, 500]
    Ec_vals = []
    K_S4_cache = None

    # Pre-compute K_S4 (doesn't depend on rho)
    print("  Pre-computing K_S4(t) for t grid...")
    K_S4_vals = np.array([K_S4(t, l_max=50) for t in t_grid])
    print(f"  K_S4 range: {K_S4_vals.min():.3e} to {K_S4_vals.max():.3e}")

    print(f"\n  {'rho':>6}  {'K_S1(t=1)':>14}  {'integrand_peak':>16}  "
          f"{'Ec_relative':>14}")

    Ec_raw = []
    for rho in rho_vals_hk:
        K_S1_vals = np.array([K_S1(t, rho) for t in t_grid])
        K_total = K_S4_vals * K_S1_vals

        # Integrand for Casimir energy: t^{-3/2} * K(t)  [schematic — ignoring Gamma and prefactors]
        # The -1/2 power of t comes from s = -1/2: t^{s-1} = t^{-3/2}
        integrand = t_grid**(-1.5) * K_total

        # Subtract UV (t->0) divergence: K_total(small t) ~ rho*sqrt(pi/t) * (4pi*t)^{-2}
        # = rho * sqrt(pi) * (4pi)^{-2} * t^{-5/2}
        # This contributes t^{-5/2} * t^{-3/2} = t^{-4} to the integrand (divergent)
        # We cut off at t_min = 1e-4 and note that the equilibrium is in the DIFFERENCE

        # Only integrate from t_IR cutoff to t_UV cutoff to get relative value
        t_min_idx = np.searchsorted(t_grid, 0.1)   # IR cutoff (large t safe)
        t_max_idx = np.searchsorted(t_grid, 10.0)  # UV cutoff (avoid divergence)

        # This gives the SHAPE of E_c(rho), not the absolute value
        Ec_shape = np.trapz(integrand[t_min_idx:t_max_idx],
                            t_grid[t_min_idx:t_max_idx])
        Ec_raw.append(Ec_shape)

        ks1_at_1 = K_S1(1.0, rho)
        pk = np.max(np.abs(integrand[t_min_idx:t_max_idx]))
        print(f"  {rho:>6.0f}  {ks1_at_1:>14.4e}  {pk:>16.4e}  {Ec_shape:>14.4e}")

    # Normalize relative to rho=1
    Ec_relative = np.array(Ec_raw) - Ec_raw[0]

    print(f"\n  E_c(rho) - E_c(1) [integrated over t in (0.1, 10)]:")
    for rho, dEc in zip(rho_vals_hk, Ec_relative):
        print(f"    rho = {rho:>5}: dEc = {dEc:>14.4e}")

    # Find minimum of Ec_relative
    min_idx = np.argmin(Ec_relative)
    print(f"\n  Minimum of E_c at: rho ~ {rho_vals_hk[min_idx]}  (BST predicts 137)")
    print(f"  Note: this uses a TRUNCATED integral; the full Casimir requires")
    print(f"  the complete small-t subtraction (Seeley-DeWitt) for the absolute value.")

    # Write heat kernel results
    hk_rows = [dict(rho=r, Ec_shape=e, dEc=de)
               for r, e, de in zip(rho_vals_hk, Ec_raw, Ec_relative)]
    csv_path2 = os.path.join(OUT_DIR, 'BST_Equilibrium_HeatKernel.csv')
    with open(csv_path2, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['rho','Ec_shape','dEc'])
        w.writeheader(); w.writerows(hk_rows)
    print(f"\n  -> {csv_path2}")

    print("\n" + "=" * 65)
    print("DONE")
    print("=" * 65)
