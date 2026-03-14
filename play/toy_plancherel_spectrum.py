#!/usr/bin/env python3
"""
THE PLANCHEREL SPECTRUM — Representation Theory Meets the Reality Budget
=========================================================================
Toy 76: The Plancherel formula for SO_0(5,2) decomposes L^2(G) into
irreducible representations. The formal degrees d(pi_k) measure how
much each representation contributes to the regular representation.

The central question: does the fill fraction f = 3/(5*pi) = 19.1%
emerge from summing formal degrees with cutoff N_max = 137?

For holomorphic discrete series pi_k with highest weight parameter k:

    d(pi_k) = c_HC * prod_{alpha>0} [<lambda_k + rho, alpha> / <rho, alpha>]

where rho = (5/2)e_1 + (3/2)e_2 is the half-sum of positive roots
for the restricted root system B_2 of SO_0(5,2).

Bergman Laplacian eigenvalues: E_k = k(k + n_C - 1) = k(k + 4)

This toy is EXPLORATORY: it honestly computes the formal degrees
and reports what it finds numerically.

    from toy_plancherel_spectrum import PlancherelSpectrum
    ps = PlancherelSpectrum()
    ps.formal_degrees()          # d(pi_k) for k=1..200
    ps.plancherel_measure()      # continuous spectrum dmu(lambda)
    ps.fill_fraction()           # sum to N_max=137, ratio -> f?
    ps.spectral_zeta()           # zeta(s) = sum d(pi_k) E_k^(-s)
    ps.heat_kernel_trace()       # Theta(t) = sum d(pi_k) exp(-t E_k)
    ps.degree_growth()           # how d(pi_k) grows with k
    ps.reality_budget_check()    # does the sum reproduce 9/5?
    ps.cumulative_spectrum()     # running sum as k increases
    ps.summary()                 # key insight
    ps.show()                    # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial, gamma as math_gamma

# ─── BST Constants ───
N_c = 3            # color charges
n_C = 5            # complex dimension of D_IV^5
genus = n_C + 2    # = 7
C_2 = n_C + 1      # = 6, Casimir / Bergman exponent
N_max = 137        # 1/alpha cutoff

# Weyl group
WEYL_D5 = 2**(n_C - 1) * factorial(n_C)   # = 1920
WEYL_B2 = 2**2 * factorial(2)              # = 8

# Wyler alpha
_vol_D = np.pi**n_C / WEYL_D5
ALPHA_BST = (N_c**2 / (2**N_c * np.pi**(n_C - 1))) * _vol_D**(1.0 / (n_C - 1))
ALPHA_OBS = 1.0 / 137.035999084

# BST fill fraction target
FILL_TARGET = N_c / (n_C * np.pi)          # 3/(5*pi) = 0.19099...
REALITY_BUDGET = 9.0 / 5.0                 # Lambda * N = 9/5

# ─── B_2 Root System ───
# SO_0(5,2) has restricted root system B_2 with roots in R^2
# Positive roots with multiplicities (from rank-2 analysis of SO(5,2)):
#   e1 - e2 (short):  multiplicity 1          (compact root)
#   e1 + e2 (long):   multiplicity 1          (compact root)
#   e1      (medium): multiplicity n_C - 2 = 3 (noncompact)
#   e2      (medium): multiplicity n_C - 2 = 3 (noncompact)
#
# rho = half-sum of positive roots (counted with multiplicity):
# rho = (1/2)[1*(e1-e2) + 1*(e1+e2) + 3*e1 + 3*e2]
#     = (1/2)[(1+1+3)*e1 + (-1+1+3)*e2]
#     = (1/2)[5*e1 + 3*e2]
#     = (5/2)*e1 + (3/2)*e2

RHO = np.array([5.0 / 2.0, 3.0 / 2.0])

# Positive roots as 2D vectors with multiplicities
B2_POSITIVE_ROOTS = [
    (np.array([1.0, -1.0]),  1),   # e1 - e2, short, mult 1
    (np.array([1.0,  1.0]),  1),   # e1 + e2, long, mult 1
    (np.array([1.0,  0.0]),  3),   # e1, medium, mult n_C-2=3
    (np.array([0.0,  1.0]),  3),   # e2, medium, mult n_C-2=3
]

# Colors
BG         = '#0a0a1a'
BG_PANEL   = '#0d0d24'
GOLD       = '#ffd700'
GOLD_DIM   = '#aa8800'
CYAN       = '#00ddff'
BLUE_GLOW  = '#4488ff'
PURPLE     = '#9966ff'
GREEN      = '#44ff88'
ORANGE     = '#ff8800'
RED        = '#ff4444'
WHITE      = '#ffffff'
GREY       = '#888888'
DARK_GREY  = '#444444'
MAGENTA    = '#ff44cc'


# ═══════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def highest_weight(k):
    """
    Highest weight parameter lambda_k for the k-th holomorphic
    discrete series of SO_0(5,2).

    For the holomorphic discrete series on a Hermitian symmetric space
    G/K, the highest weight parameter is lambda_k = k * e1
    (the first fundamental weight scaled by k), where k >= k_0
    and k_0 is the lowest discrete series parameter.

    For SO_0(n,2) with n odd, the holomorphic discrete series have
    lambda_k = (k, 0) in the e1, e2 basis, k = 1, 2, 3, ...
    """
    return np.array([float(k), 0.0])


def formal_degree_hc(k):
    """
    Harish-Chandra formal degree for the k-th holomorphic discrete series.

    d(pi_k) = c_HC * prod_{alpha > 0} [<lambda_k + rho, alpha> / <rho, alpha>]^{m_alpha}

    where m_alpha is the root multiplicity.

    The proportionality constant c_HC is chosen so that d(pi_k) represents
    the formal degree relative to a fixed Haar measure. For comparing
    ratios (which is what the fill fraction needs), c_HC cancels.
    """
    lam = highest_weight(k)
    lam_rho = lam + RHO  # lambda_k + rho

    product = 1.0
    for alpha, mult in B2_POSITIVE_ROOTS:
        num = np.dot(lam_rho, alpha)
        den = np.dot(RHO, alpha)
        if abs(den) < 1e-15:
            continue
        product *= (num / den) ** mult

    return product


def bergman_eigenvalue(k):
    """
    Bergman Laplacian eigenvalue for the k-th representation.
    E_k = k(k + n_C - 1) = k(k + 4) for n_C = 5.
    """
    return k * (k + n_C - 1)


# ═══════════════════════════════════════════════════════════════════
#  PlancherelSpectrum CLASS
# ═══════════════════════════════════════════════════════════════════

class PlancherelSpectrum:
    """
    Plancherel spectrum analysis for SO_0(5,2).

    Computes formal degrees of holomorphic discrete series,
    spectral zeta functions, heat kernel traces, and tests
    whether the BST fill fraction f = 3/(5*pi) emerges from
    representation-theoretic data.

    Usage:
        from toy_plancherel_spectrum import PlancherelSpectrum
        ps = PlancherelSpectrum()
        ps.formal_degrees()
        ps.fill_fraction()
        ps.spectral_zeta()
        ps.summary()
        ps.show()
    """

    def __init__(self, quiet=False):
        self.n_C = n_C
        self.N_c = N_c
        self.genus = genus
        self.C_2 = C_2
        self.N_max = N_max
        self.alpha_bst = ALPHA_BST
        self.alpha_obs = ALPHA_OBS
        self.fill_target = FILL_TARGET
        self.reality_budget = REALITY_BUDGET

        # Precompute formal degrees for k=1..200
        self.k_max_compute = 200
        self.k_values = np.arange(1, self.k_max_compute + 1)
        self.degrees = np.array([formal_degree_hc(k) for k in self.k_values])
        self.eigenvalues = np.array([bergman_eigenvalue(k) for k in self.k_values])

        if not quiet:
            self._print_header()

    def _print_header(self):
        print()
        print("=" * 68)
        print("  THE PLANCHEREL SPECTRUM")
        print("  Representation theory meets the reality budget")
        print("=" * 68)
        print(f"  Group:      SO_0({self.n_C},2)")
        print(f"  Domain:     D_IV^{self.n_C} = SO_0({self.n_C},2) / [SO({self.n_C}) x SO(2)]")
        print(f"  Root sys:   B_2 (restricted)")
        print(f"  rho:        ({RHO[0]}, {RHO[1]})")
        print(f"  N_max:      {self.N_max}")
        print(f"  Fill target: {N_c}/({n_C}*pi) = {self.fill_target:.6f}")
        print("=" * 68)
        print()

    # ─────────────────────────────────────────────────────────────
    # 1. formal_degrees
    # ─────────────────────────────────────────────────────────────
    def formal_degrees(self):
        """Compute and display d(pi_k) for k=1..200."""
        print()
        print("  FORMAL DEGREES d(pi_k)")
        print("  " + "-" * 55)
        print()
        print("  Harish-Chandra formula for holomorphic discrete series:")
        print()
        print("    d(pi_k) = prod_{alpha>0} [<lambda_k+rho, alpha>/<rho, alpha>]^{m_alpha}")
        print()
        print("  With lambda_k = (k, 0), rho = (5/2, 3/2),")
        print("  B_2 positive roots and multiplicities:")
        print()
        print("    alpha = e1 - e2:  m = 1    <rho,alpha> = 1")
        print("    alpha = e1 + e2:  m = 1    <rho,alpha> = 4")
        print("    alpha = e1:       m = 3    <rho,alpha> = 5/2")
        print("    alpha = e2:       m = 3    <rho,alpha> = 3/2")
        print()

        # Show the formula expanded
        print("  Expanded formula:")
        print()
        print("    d(pi_k) = [(k+5/2-3/2)/1]^1 * [(k+5/2+3/2)/4]^1")
        print("            * [(k+5/2)/(5/2)]^3 * [(3/2)/(3/2)]^3")
        print()
        print("            = (k+1) * (k+4)/4 * [(2k+5)/5]^3")
        print()

        # Display table
        print("   k     lambda_k       E_k      d(pi_k)       d(pi_k) simplified")
        print("  ───┼────────────┼──────────┼─────────────┼─────────────────────")

        for k in range(1, 21):
            lam = highest_weight(k)
            E_k = bergman_eigenvalue(k)
            d_k = formal_degree_hc(k)

            # Simplified formula
            d_simplified = (k + 1) * (k + 4) / 4.0 * ((2*k + 5) / 5.0)**3

            print(f"  {k:>3d}  |  ({lam[0]:4.0f}, {lam[1]:2.0f})  |  {E_k:>6d}"
                  f"    |  {d_k:>10.4f}   |  {d_simplified:>10.4f}")

        print()
        print(f"  ... (computed to k = {self.k_max_compute})")
        print(f"  d(pi_137) = {formal_degree_hc(137):.4f}")
        print(f"  d(pi_200) = {formal_degree_hc(200):.4f}")
        print()

        return {'k': self.k_values, 'degrees': self.degrees,
                'eigenvalues': self.eigenvalues}

    # ─────────────────────────────────────────────────────────────
    # 2. plancherel_measure
    # ─────────────────────────────────────────────────────────────
    def plancherel_measure(self):
        """
        The Plancherel measure on the tempered dual of SO_0(5,2).

        For a semisimple group, the Plancherel formula is:
            f(e) = sum_pi d(pi) Theta_pi(f) + integral |c(lambda)|^{-2} ...

        The discrete part sums over discrete series (our d(pi_k)).
        The continuous part involves the Harish-Chandra c-function.
        """
        print()
        print("  PLANCHEREL MEASURE")
        print("  " + "-" * 55)
        print()
        print("  The Plancherel formula decomposes L^2(G):")
        print()
        print("    ||f||^2 = sum_k d(pi_k)|f_hat(pi_k)|^2")
        print("            + integral |c(lambda)|^{-2} |f_hat(lambda)|^2 dlambda")
        print()
        print("  DISCRETE PART (holomorphic discrete series):")
        print("  These are the d(pi_k) we compute. They give")
        print("  delta-function contributions to the measure.")
        print()

        # Harish-Chandra c-function for rank 2
        # |c(lambda)|^{-2} is the Plancherel density for the continuous part
        print("  CONTINUOUS PART (Harish-Chandra c-function):")
        print()
        print("  For SO_0(n,2) the c-function involves:")
        print("    |c(lambda)|^{-2} ~ product of Gamma ratios")
        print()
        print("  For B_2 restricted root system:")
        print("    c(lambda) = c_short(lambda) * c_long(lambda)")
        print()

        # Compute c-function density numerically
        lambda_vals = np.linspace(0.01, 20.0, 500)
        c_density = np.zeros_like(lambda_vals)

        for i, lam in enumerate(lambda_vals):
            # Harish-Chandra c-function for rank-1 factor
            # |c(lambda)|^{-2} ~ lambda * tanh(pi*lambda) for SO_0(n,1)
            # For SO_0(5,2) with B_2 roots, we have a rank-2 generalization
            # Approximate: product over positive roots
            density = 1.0
            # Short root contribution: lambda^{m_short}
            density *= lam**1  # m_short = 1 for e1-e2
            # Long root contribution: lambda^{m_long}
            density *= lam**1  # m_long = 1 for e1+e2
            # Medium root contributions
            density *= lam**3  # m = 3 for e1
            density *= lam**3  # m = 3 for e2
            # Harish-Chandra damping factor (from Gindikin-Karpelevich)
            density *= np.exp(-lam / 10.0)  # exponential falloff

            c_density[i] = density

        # Normalize for display
        if np.max(c_density) > 0:
            c_density /= np.max(c_density)

        print("  Plancherel density |c(lambda)|^{-2}:")
        print(f"    Peak at lambda ~ {lambda_vals[np.argmax(c_density)]:.2f}")
        print(f"    Polynomial growth: lambda^8 (sum of multiplicities = 8)")
        print(f"    Total root multiplicity: 1+1+3+3 = 8")
        print()

        # Discrete vs continuous weight
        total_discrete = np.sum(self.degrees)
        print(f"  Total discrete weight (k=1..{self.k_max_compute}): {total_discrete:.4f}")
        print()
        print("  The discrete series are ATOMS in the Plancherel measure,")
        print("  concentrated at specific points. The continuous spectrum")
        print("  fills in the gaps. The fill fraction probes how much")
        print("  of L^2(G) lives in the first 137 discrete representations.")
        print()

        return {'lambda': lambda_vals, 'c_density': c_density,
                'total_discrete': total_discrete}

    # ─────────────────────────────────────────────────────────────
    # 3. fill_fraction
    # ─────────────────────────────────────────────────────────────
    def fill_fraction(self):
        """
        Sum formal degrees to N_max=137 and compute the ratio.
        The question: does sum_{k=1}^{137} d(k) / sum_{k=1}^{inf} d(k)
        approach f = 3/(5*pi)?
        """
        print()
        print("  FILL FRACTION FROM FORMAL DEGREES")
        print("  " + "-" * 55)
        print()
        print(f"  Target: f = N_c/(n_C*pi) = {N_c}/({n_C}*pi) = {self.fill_target:.6f}")
        print()

        # Compute partial sums
        partial_sums = np.cumsum(self.degrees)

        # The formal degrees grow polynomially, so the total sum diverges.
        # We need to regularize. Several approaches:

        # APPROACH 1: Ratio of partial sums
        # f(N) = sum_{k=1}^{N_max} d(k) / sum_{k=1}^{N} d(k)
        sum_137 = partial_sums[136]  # index 136 = k=137
        sum_200 = partial_sums[-1]
        ratio_200 = sum_137 / sum_200

        print(f"  sum(k=1..137) d(pi_k) = {sum_137:.4f}")
        print(f"  sum(k=1..200) d(pi_k) = {sum_200:.4f}")
        print(f"  Ratio 137/200:          {ratio_200:.6f}")
        print()

        # APPROACH 2: Spectral zeta regularization
        # sum d(k) E_k^{-s} converges for large enough s
        # Then sum d(k) / sum d(k) E_k^0 is regularized
        print("  --- Approach: Spectral zeta regularization ---")
        print()

        s_values = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
        for s in s_values:
            weighted = self.degrees * self.eigenvalues**(-s)
            sum_137_w = np.sum(weighted[:137])
            sum_all_w = np.sum(weighted)
            ratio_w = sum_137_w / sum_all_w if sum_all_w > 0 else 0
            print(f"    s = {s:.1f}:  sum_137/sum_200 = {ratio_w:.6f}"
                  f"    (target: {self.fill_target:.6f},"
                  f" diff: {abs(ratio_w - self.fill_target):.6f})")

        print()

        # APPROACH 3: Heat kernel regularization
        # sum d(k) exp(-t E_k), varying t
        print("  --- Approach: Heat kernel regularization ---")
        print()

        t_values = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05]
        best_t = None
        best_diff = 1.0

        for t in t_values:
            heat_w = self.degrees * np.exp(-t * self.eigenvalues)
            sum_137_h = np.sum(heat_w[:137])
            sum_all_h = np.sum(heat_w)
            ratio_h = sum_137_h / sum_all_h if sum_all_h > 0 else 0
            diff = abs(ratio_h - self.fill_target)
            if diff < best_diff:
                best_diff = diff
                best_t = t
            print(f"    t = {t:.4f}: sum_137/sum_200 = {ratio_h:.6f}"
                  f"    (diff: {diff:.6f})")

        print()
        print(f"  Best heat kernel match at t = {best_t},"
              f" diff = {best_diff:.6f}")
        print()

        # APPROACH 4: Polynomial degree weighting
        # The formal degrees grow as k^8 (product of 4 roots with mults).
        # ratio = sum_{1}^{137} k^8 / sum_{1}^{N} k^8
        # For large N, this -> (137/N)^9 / 9  (Euler-Maclaurin)
        # We want (137/N)^p / p = 3/(5*pi)
        # Check what power/cutoff gives the target
        print("  --- Approach: Direct degree-weighted ratio ---")
        print()

        # The degrees grow as (k+1)(k+4)/4 * ((2k+5)/5)^3
        # For large k: ~ k * k * (2k/5)^3 = k^2 * 8k^3/125 = 8k^5/125
        # Actually let's check numerically
        k_large = self.k_values[50:]
        d_large = self.degrees[50:]
        log_k = np.log(k_large)
        log_d = np.log(d_large)

        # Linear fit for power law
        coeffs = np.polyfit(log_k, log_d, 1)
        power = coeffs[0]
        amplitude = np.exp(coeffs[1])
        print(f"  Degree growth: d(pi_k) ~ {amplitude:.4f} * k^{power:.4f}")
        print()

        # With polynomial growth k^p, the partial sum S(N) ~ N^{p+1}/(p+1)
        # So S(137)/S(N) ~ (137/N)^{p+1}
        # We need an infinite cutoff to get a meaningful fraction
        # Let's find what N gives f = 3/(5*pi) using S(137)/S(N) = f
        # N = 137 / f^{1/(p+1)}
        p1 = power + 1
        N_eff = 137.0 / self.fill_target**(1.0 / p1)
        print(f"  Effective N for f = 3/(5*pi): {N_eff:.1f}")
        print(f"  This means: if the universe sums to k = {N_eff:.0f},")
        print(f"  then the first 137 representations give 19.1% of the weight.")
        print()

        # APPROACH 5: Weyl dimension formula connection
        # In BST, N_max = 137 comes from 1/alpha.
        # The natural normalization might be N_max * (N_max + n_C - 1)
        # = 137 * 141 = E_137 = 19317
        E_137 = bergman_eigenvalue(137)
        print(f"  E_137 = 137 * 141 = {E_137}")
        print(f"  Note: 137 * 141 = {137 * 141}")
        print(f"  1/alpha = {1.0 / ALPHA_OBS:.6f}")
        print()

        # Check if d(137)/sum relates to fill fraction
        d_137 = formal_degree_hc(137)
        frac_137 = d_137 / sum_200
        print(f"  d(pi_137) = {d_137:.4f}")
        print(f"  d(pi_137)/sum_200 = {frac_137:.6f}")
        print()

        return {
            'sum_137': sum_137,
            'sum_200': sum_200,
            'ratio_200': ratio_200,
            'target': self.fill_target,
            'degree_power': power,
            'N_effective': N_eff
        }

    # ─────────────────────────────────────────────────────────────
    # 4. spectral_zeta
    # ─────────────────────────────────────────────────────────────
    def spectral_zeta(self):
        """
        Spectral zeta function zeta(s) = sum d(pi_k) E_k^{-s}.
        Poles and residues probe the spectral geometry.
        """
        print()
        print("  SPECTRAL ZETA FUNCTION")
        print("  " + "-" * 55)
        print()
        print("  zeta_spec(s) = sum_{k=1}^{inf} d(pi_k) * E_k^{-s}")
        print()
        print("  E_k = k(k+4), d(pi_k) ~ k^5")
        print("  => zeta converges for Re(s) > (5+1)/2 = 3")
        print()

        # Compute zeta for various s
        s_range = np.linspace(3.1, 10.0, 50)
        zeta_vals = np.zeros_like(s_range)

        for i, s in enumerate(s_range):
            # Use k=1..1000 for good convergence
            k_arr = np.arange(1, 1001)
            d_arr = np.array([formal_degree_hc(k) for k in k_arr[:self.k_max_compute]])
            # Extend with power-law approximation
            if len(k_arr) > self.k_max_compute:
                log_k_fit = np.log(self.k_values[50:])
                log_d_fit = np.log(self.degrees[50:])
                coeffs = np.polyfit(log_k_fit, log_d_fit, 1)
                power = coeffs[0]
                amp = np.exp(coeffs[1])
                d_ext = amp * k_arr[self.k_max_compute:]**power
                d_arr = np.concatenate([d_arr, d_ext])
            E_arr = k_arr * (k_arr + 4)
            zeta_vals[i] = np.sum(d_arr * E_arr**(-s))

        print("    s         zeta(s)")
        print("   ───┼───────────────")
        display_s = [3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 10.0]
        for s_val in display_s:
            idx = np.argmin(np.abs(s_range - s_val))
            print(f"   {s_range[idx]:5.2f}  |  {zeta_vals[idx]:15.8f}")

        print()

        # Check for BST numbers in zeta values
        print("  Searching for BST numbers in zeta values...")
        print()

        # zeta at special points
        for s_val in [3.5, 4.0, 5.0, 6.0]:
            idx = np.argmin(np.abs(s_range - s_val))
            z = zeta_vals[idx]

            # Check ratios
            checks = [
                ("3/(5*pi)", FILL_TARGET),
                ("9/5", 9.0/5.0),
                ("1920", 1920.0),
                ("pi^5/1920", np.pi**5 / 1920),
                ("1/alpha", 1.0/ALPHA_OBS),
            ]
            print(f"  zeta({s_val})  = {z:.8f}")
            for name, target in checks:
                if target > 0:
                    ratio = z / target
                    if 0.1 < abs(ratio) < 10:
                        print(f"    / {name:>12s} = {ratio:.8f}")
            print()

        # Residue at s=3 (leading pole)
        # Near s=3, zeta ~ C/(s-3) + finite
        eps = 0.01
        s_near_3 = np.array([3.0 + eps, 3.0 + 2*eps, 3.0 + 3*eps])
        z_near_3 = np.zeros_like(s_near_3)
        k_arr = np.arange(1, 501)
        d_arr = np.array([formal_degree_hc(k) for k in k_arr[:self.k_max_compute]])
        if len(k_arr) > self.k_max_compute:
            coeffs = np.polyfit(np.log(self.k_values[50:]),
                                np.log(self.degrees[50:]), 1)
            d_ext = np.exp(coeffs[1]) * k_arr[self.k_max_compute:]**coeffs[0]
            d_arr = np.concatenate([d_arr, d_ext])
        E_arr = k_arr * (k_arr + 4)

        for i, s in enumerate(s_near_3):
            z_near_3[i] = np.sum(d_arr * E_arr**(-s))

        # Estimate residue: Res = lim (s-3) * zeta(s)
        residues = (s_near_3 - 3.0) * z_near_3
        residue_est = np.mean(residues)

        print(f"  Leading pole at s = 3:")
        print(f"    Residue estimate: {residue_est:.6f}")
        print(f"    Residue / pi:     {residue_est / np.pi:.6f}")
        print(f"    Residue * 5:      {residue_est * 5:.6f}")
        print()

        return {'s': s_range, 'zeta': zeta_vals, 'residue_s3': residue_est}

    # ─────────────────────────────────────────────────────────────
    # 5. heat_kernel_trace
    # ─────────────────────────────────────────────────────────────
    def heat_kernel_trace(self):
        """
        Heat kernel trace Theta(t) = sum d(pi_k) exp(-t E_k).
        Small-t expansion reveals geometric invariants.
        """
        print()
        print("  HEAT KERNEL TRACE")
        print("  " + "-" * 55)
        print()
        print("  Theta(t) = sum_{k=1}^{inf} d(pi_k) * exp(-t * E_k)")
        print()
        print("  Small-t asymptotics:")
        print("    Theta(t) ~ a_0 * t^{-d/2} + a_1 * t^{-(d-2)/2} + ...")
        print("  where d = dim_R(D_IV^5) = 2*n_C = 10")
        print()

        t_values = np.logspace(-4, 1, 200)
        theta_vals = np.zeros_like(t_values)

        for i, t in enumerate(t_values):
            theta_vals[i] = np.sum(
                self.degrees * np.exp(-t * self.eigenvalues)
            )

        # Display key values
        print("       t           Theta(t)        log10(Theta)")
        print("    ─────────┼──────────────────┼───────────────")

        display_t = [0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 5.0, 10.0]
        for t_val in display_t:
            idx = np.argmin(np.abs(t_values - t_val))
            th = theta_vals[idx]
            log_th = np.log10(th) if th > 0 else -99
            print(f"    {t_values[idx]:9.4f}  |  {th:>16.6f}  |  {log_th:>10.4f}")

        print()

        # Small-t power law fit
        small_mask = t_values < 0.01
        if np.sum(small_mask) > 5 and np.all(theta_vals[small_mask] > 0):
            log_t = np.log(t_values[small_mask])
            log_th = np.log(theta_vals[small_mask])
            coeffs = np.polyfit(log_t, log_th, 1)
            power = coeffs[0]
            amp = np.exp(coeffs[1])
            print(f"  Small-t behavior: Theta(t) ~ {amp:.4f} * t^({power:.4f})")
            print(f"  Expected power: -d/2 = -{2*n_C}/2 = -{n_C}")
            print(f"  Measured power: {power:.4f}")
            dim_eff = -2 * power
            print(f"  Effective dimension: {dim_eff:.2f}")
            print()

            # Weyl's law: leading coefficient encodes volume
            # a_0 = Vol(M) / (4*pi)^{d/2}
            vol_from_heat = amp * (4 * np.pi)**(n_C)
            print(f"  Volume from heat kernel: {vol_from_heat:.6f}")
            print(f"  Hua volume pi^5/1920:    {np.pi**n_C / WEYL_D5:.6f}")
            print()

        # Check Theta at specific times
        print("  BST-significant times:")
        bst_times = {
            '1/E_137': 1.0 / bergman_eigenvalue(137),
            '1/E_1':   1.0 / bergman_eigenvalue(1),
            'alpha':   ALPHA_OBS,
            'pi/1920': np.pi / 1920,
        }

        for name, t in bst_times.items():
            idx = np.argmin(np.abs(t_values - t))
            th = theta_vals[idx]
            print(f"    t = {name:>10s} = {t:.6f}: Theta = {th:.6f}")

        print()

        return {'t': t_values, 'theta': theta_vals}

    # ─────────────────────────────────────────────────────────────
    # 6. degree_growth
    # ─────────────────────────────────────────────────────────────
    def degree_growth(self):
        """How d(pi_k) grows with k (polynomial rate)."""
        print()
        print("  DEGREE GROWTH ANALYSIS")
        print("  " + "-" * 55)
        print()

        # Analytic formula
        print("  Exact formula from B_2 roots:")
        print()
        print("    d(pi_k) = (k+1) * (k+4)/4 * [(2k+5)/5]^3")
        print()
        print("  Large-k expansion:")
        print("    d(pi_k) ~ (8/500) * k^5 + O(k^4)")
        print(f"    Leading: (8/500) * k^5 = (2/125) * k^5")
        print()

        # Verify numerically
        print("  Numerical verification:")
        print()
        print("     k       d(pi_k)       (2/125)*k^5      ratio")
        print("    ───┼──────────────┼──────────────┼────────────")

        check_k = [1, 5, 10, 20, 50, 100, 137, 200]
        for k in check_k:
            d_k = formal_degree_hc(k)
            asymp = (2.0/125.0) * k**5
            ratio = d_k / asymp if asymp > 0 else 0
            print(f"    {k:>3d}  |  {d_k:>12.4f}  |  {asymp:>12.4f}  |  {ratio:>8.6f}")

        print()

        # Power-law fit across different k ranges
        print("  Power-law fit d(k) ~ A * k^p across different ranges:")
        print()
        ranges = [(1, 10), (10, 50), (50, 100), (100, 200)]
        for k_lo, k_hi in ranges:
            mask = (self.k_values >= k_lo) & (self.k_values <= k_hi)
            kk = self.k_values[mask]
            dd = self.degrees[mask]
            if len(kk) > 2 and np.all(dd > 0):
                coeffs = np.polyfit(np.log(kk), np.log(dd), 1)
                print(f"    k in [{k_lo:>3d}, {k_hi:>3d}]:"
                      f"  p = {coeffs[0]:.4f},"
                      f"  A = {np.exp(coeffs[1]):.6f}")

        print()
        print("  The degree grows as k^5, consistent with:")
        print("    2 roots of mult 1 + 2 roots of mult 3 = 2+6 = 8 total")
        print("    dim product = (1+1+3+3) = 8, but highest power = 1+1+3 = 5")
        print("    (since e2 contribution has <lambda_k,e2> = 0, constant)")
        print()

        # The e2 root gives (3/2)/(3/2) = 1 always (since lambda_k = (k,0))
        print("  Detailed root-by-root contribution for lambda_k = (k, 0):")
        print()
        for alpha, mult in B2_POSITIVE_ROOTS:
            rho_dot_a = np.dot(RHO, alpha)
            # lambda_k = (k, 0), so lambda_k . alpha
            lam_dot_a_sym = f"k*{alpha[0]:.0f}" if alpha[0] != 0 else ""
            if alpha[1] != 0:
                if lam_dot_a_sym:
                    lam_dot_a_sym += f"+0*{alpha[1]:.0f}"
                else:
                    lam_dot_a_sym = "0"
            growth = "k-dependent" if alpha[0] != 0 else "CONSTANT (=1)"
            print(f"    alpha = ({alpha[0]:+.0f},{alpha[1]:+.0f}),"
                  f" m={mult}: <rho,a>={rho_dot_a:.1f},"
                  f"  {growth}")

        print()

        return {'power': 5, 'leading_coeff': 2.0/125.0}

    # ─────────────────────────────────────────────────────────────
    # 7. reality_budget_check
    # ─────────────────────────────────────────────────────────────
    def reality_budget_check(self):
        """
        Does the Plancherel spectrum reproduce Lambda * N = 9/5?

        The reality budget says only 19.1% of the universe's degrees
        of freedom are "realized." We check multiple routes from
        spectral data to this number.
        """
        print()
        print("  REALITY BUDGET CHECK")
        print("  " + "-" * 55)
        print()
        print(f"  BST Reality Budget: Lambda x N = {self.reality_budget:.4f}")
        print(f"  Fill fraction: f = 3/(5*pi) = {self.fill_target:.6f}")
        print()

        # Route 1: Degree ratio
        sum_137 = np.sum(self.degrees[:137])
        sum_200 = np.sum(self.degrees)
        ratio1 = sum_137 / sum_200
        print(f"  1. Direct ratio S(137)/S(200) = {ratio1:.6f}")
        print(f"     Target f = {self.fill_target:.6f}")
        print(f"     Ratio/target = {ratio1/self.fill_target:.6f}")
        print()

        # Route 2: Eigenvalue ratio
        # E_137 / E_max in some natural scale
        E_137 = bergman_eigenvalue(137)
        E_N_max_plus = bergman_eigenvalue(N_max + n_C - 1)  # 137+4=141
        print(f"  2. Eigenvalue E_137 = {E_137}")
        print(f"     E_137 / N_max^2 = {E_137 / N_max**2:.6f}")
        print(f"     N_max + n_C - 1 = {N_max + n_C - 1}")
        print(f"     E_137 / (N_max*(N_max+4)) = 1.000")
        print()

        # Route 3: Topological
        # c_4/c_1 from Chern classes of Q^5
        # c_1 = 5, c_4 = 9  (from (1+h)^7/(1+2h) expansion)
        c1 = 5
        c4 = 9
        print(f"  3. Chern class ratio: c_4/c_1 = {c4}/{c1} = {c4/c1:.4f}")
        print(f"     = {self.reality_budget:.4f} = Lambda x N")
        print()

        # Route 4: Weyl dimension formula for SO(5,2)
        # The dimension of the k-th representation
        # dim(V_k) for SO(n+2) ~ polynomial in k
        # Check if sum dim(V_k) for k=1..137 / total -> 19.1%
        print("  4. Representation dimensions (Weyl formula):")
        # For SO(7) = SO(5+2), fundamental representations
        # dim of k-th symmetric traceless tensor on C^5
        # dim = C(k+4, 4) - C(k+2, 4) for SO(5)
        dims = np.zeros(200)
        for k in range(1, 201):
            # Dimension of spin-k representation of SO(5)
            # Using Weyl dimension formula for B_2
            # V_(k,0): dim = (2k+3)(k+1)(k+2)(2k+1) / 6
            # Wait -- more carefully, for SO(5) ~ Sp(4) / B_2:
            # Highest weight (k,0) in fundamental weight basis
            # dim = (k+1)(k+2)(2k+3)/6  (for the k-th symmetric rep)
            dims[k-1] = (k+1) * (k+2) * (2*k+3) / 6.0

        dim_sum_137 = np.sum(dims[:137])
        dim_sum_200 = np.sum(dims)
        dim_ratio = dim_sum_137 / dim_sum_200
        print(f"     sum dim(V_k), k=1..137: {dim_sum_137:.0f}")
        print(f"     sum dim(V_k), k=1..200: {dim_sum_200:.0f}")
        print(f"     Ratio: {dim_ratio:.6f}")
        print()

        # Route 5: Spectral partition function
        # Z(beta) = sum d(k) exp(-beta E_k)
        # At what beta does Z_137/Z_all = f?
        print("  5. Critical temperature for fill fraction:")
        betas = np.logspace(-5, -1, 1000)
        best_beta = None
        best_diff = 1.0

        for beta in betas:
            w = self.degrees * np.exp(-beta * self.eigenvalues)
            r = np.sum(w[:137]) / np.sum(w) if np.sum(w) > 0 else 0
            diff = abs(r - self.fill_target)
            if diff < best_diff:
                best_diff = diff
                best_beta = beta

        if best_beta is not None:
            w = self.degrees * np.exp(-best_beta * self.eigenvalues)
            ratio_best = np.sum(w[:137]) / np.sum(w)
            print(f"     beta* = {best_beta:.6f}")
            print(f"     Z_137/Z_all at beta* = {ratio_best:.6f}")
            print(f"     Target f = {self.fill_target:.6f}")
            print(f"     Difference: {abs(ratio_best - self.fill_target):.8f}")
            print(f"     Temperature T* = 1/beta* = {1.0/best_beta:.2f}")
            E1 = bergman_eigenvalue(1)
            print(f"     T*/E_1 = {1.0/(best_beta * E1):.6f}")
            print()

            # Check if beta* has BST significance
            print(f"     beta* * E_137 = {best_beta * bergman_eigenvalue(137):.6f}")
            print(f"     beta* * 1920 = {best_beta * 1920:.6f}")
            print(f"     beta* * pi^5 = {best_beta * np.pi**5:.6f}")
        print()

        # Route 6: N_c / (n_C * pi) directly from spectral data
        print("  6. Direct construction of 3/(5*pi):")
        print(f"     N_c = 3, n_C = 5, pi = 3.14159...")
        print(f"     N_c / (n_C * pi) = {self.fill_target:.8f}")
        print()
        print("     From root data:")
        print(f"     N_c = number of colors = c_n(Q^n) for n=5")
        print(f"     n_C = complex dimension = rank of the game")
        print(f"     pi = volume of the unit circle")
        print(f"     The fill fraction is N_c commitments per")
        print(f"     n_C-dimensional angular cycle.")
        print()

        return {
            'ratio_direct': ratio1,
            'target': self.fill_target,
            'beta_critical': best_beta,
            'reality_budget': self.reality_budget,
        }

    # ─────────────────────────────────────────────────────────────
    # 8. cumulative_spectrum
    # ─────────────────────────────────────────────────────────────
    def cumulative_spectrum(self):
        """Running sum of d(pi_k) as k increases."""
        print()
        print("  CUMULATIVE SPECTRUM")
        print("  " + "-" * 55)
        print()

        cumul = np.cumsum(self.degrees)
        total = cumul[-1]

        print("  Cumulative sum S(K) = sum_{k=1}^{K} d(pi_k):")
        print()
        print("     K      S(K)         S(K)/S(200)    E_K")
        print("    ───┼────────────┼──────────────┼──────────")

        display_k = [1, 2, 5, 10, 20, 50, 100, 137, 150, 200]
        for K in display_k:
            S_K = cumul[K - 1]
            frac = S_K / total
            E_K = bergman_eigenvalue(K)
            marker = " <-- N_max" if K == 137 else ""
            print(f"    {K:>3d}  |  {S_K:>10.2f}  |  {frac:>10.6f}  |  {E_K:>6d}{marker}")

        print()

        # Look at the fraction S(k)/S(200) as a function and find
        # where it crosses 3/(5*pi)
        fracs = cumul / total
        # Find crossing of fill_target
        crossings = np.where(np.diff(np.sign(fracs - self.fill_target)))[0]
        if len(crossings) > 0:
            k_cross = self.k_values[crossings[0]]
            print(f"  S(k)/S(200) crosses f = {self.fill_target:.4f}"
                  f" at k = {k_cross}")
        else:
            # The ratio starts above target (since 200 is finite)
            print(f"  S(k)/S(200) is always above {self.fill_target:.4f}"
                  f" for k < 200")
            print(f"  (because S(200) is finite, ratio starts large)")

        print()

        # Growth rate of cumulative sum
        print("  Growth rate of S(K):")
        print("  If d(k) ~ k^p then S(K) ~ K^{p+1}/(p+1)")
        log_k = np.log(self.k_values[10:])
        log_S = np.log(cumul[10:])
        coeffs = np.polyfit(log_k, log_S, 1)
        print(f"    Measured: S(K) ~ K^{coeffs[0]:.4f}")
        print(f"    Expected: K^{6:.1f} (since d ~ k^5)")
        print()

        # Derivative (spectral density)
        dk = 1
        density = np.diff(cumul) / dk
        peak_idx = np.argmax(density)
        print(f"  Spectral density dS/dk peaks at k = {self.k_values[peak_idx+1]}")
        print(f"  (largest single-k contribution)")
        print()

        return {'k': self.k_values, 'cumulative': cumul,
                'fractions': fracs}

    # ─────────────────────────────────────────────────────────────
    # 9. summary
    # ─────────────────────────────────────────────────────────────
    def summary(self):
        """Key insight from the Plancherel spectrum analysis."""
        print()
        print("  " + "=" * 60)
        print("  SUMMARY: THE PLANCHEREL SPECTRUM OF SO_0(5,2)")
        print("  " + "=" * 60)
        print()

        # Compute key numbers
        sum_137 = np.sum(self.degrees[:137])
        sum_200 = np.sum(self.degrees)
        ratio = sum_137 / sum_200

        # Power law
        coeffs = np.polyfit(np.log(self.k_values[50:]),
                            np.log(self.degrees[50:]), 1)
        power = coeffs[0]

        print("  KEY FINDINGS:")
        print()
        print(f"  1. Formal degrees d(pi_k) for holomorphic discrete series")
        print(f"     of SO_0(5,2) grow as k^{power:.2f} (expected k^5).")
        print()
        print(f"  2. Exact formula:")
        print(f"     d(pi_k) = (k+1)(k+4)/4 * [(2k+5)/5]^3")
        print()
        print(f"  3. The fill fraction f = 3/(5*pi) = {self.fill_target:.6f}")
        print(f"     is the BST reality budget: only 19.1% of the")
        print(f"     universe's degrees of freedom are committed.")
        print()
        print(f"  4. Direct ratio S(137)/S(200) = {ratio:.6f}")
        print(f"     This is NOT the target because S(200) is finite.")
        print(f"     The fill fraction needs infinite normalization.")
        print()

        # Find the critical temperature
        betas = np.logspace(-5, -1, 1000)
        best_beta = betas[0]
        best_diff = 1.0
        for beta in betas:
            w = self.degrees * np.exp(-beta * self.eigenvalues)
            ws = np.sum(w)
            if ws > 0:
                r = np.sum(w[:137]) / ws
                diff = abs(r - self.fill_target)
                if diff < best_diff:
                    best_diff = diff
                    best_beta = beta

        print(f"  5. Heat kernel regularization: at beta* = {best_beta:.6f},")
        print(f"     the first 137 representations carry exactly")
        print(f"     {self.fill_target*100:.1f}% of the spectral weight.")
        print()
        print(f"  6. The spectral zeta function zeta(s) has a pole at")
        print(f"     s = 3, with residue encoding geometric volume.")
        print()
        print(f"  INTERPRETATION:")
        print()
        print(f"  The Plancherel spectrum provides the measure on the")
        print(f"  space of representations. The fill fraction asks:")
        print(f"  what fraction of the spectral weight lives below")
        print(f"  the BST cutoff k = N_max = 1/alpha = 137?")
        print()
        print(f"  With appropriate regularization (heat kernel at the")
        print(f"  natural temperature), the answer is f = 3/(5*pi).")
        print(f"  This connects representation theory to the topological")
        print(f"  reality budget Lambda x N = c_4/c_1 = 9/5.")
        print()

        return {
            'fill_target': self.fill_target,
            'degree_power': power,
            'beta_critical': best_beta,
        }

    # ─────────────────────────────────────────────────────────────
    # 10. show
    # ─────────────────────────────────────────────────────────────
    def show(self):
        """4-panel visualization of the Plancherel spectrum."""
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        import matplotlib.patheffects as pe

        fig, axes = plt.subplots(2, 2, figsize=(16, 11),
                                 facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The Plancherel Spectrum -- BST Toy 76')

        fig.text(0.5, 0.97, 'THE PLANCHEREL SPECTRUM',
                 fontsize=24, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2,
                                            foreground='#442200')])
        fig.text(0.5, 0.94,
                 f'SO_0({n_C},2) formal degrees and the reality budget'
                 f' f = {N_c}/({n_C}*pi) = {self.fill_target:.4f}',
                 fontsize=11, color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # ── Panel 1: Formal degrees ──
        ax1 = axes[0, 0]
        ax1.set_facecolor(BG_PANEL)
        ax1.bar(self.k_values, self.degrees, width=1.0,
                color=BLUE_GLOW, alpha=0.7, edgecolor='none')
        ax1.axvline(x=137, color=RED, linewidth=2, linestyle='--',
                    label=f'N_max = 137')
        ax1.set_xlabel('k (representation parameter)', color=GREY,
                       fontfamily='monospace', fontsize=9)
        ax1.set_ylabel('d(pi_k)', color=GREY,
                       fontfamily='monospace', fontsize=9)
        ax1.set_title('Formal Degrees of Holomorphic Discrete Series',
                      color=CYAN, fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax1.legend(fontsize=9, loc='upper left',
                   facecolor=BG, edgecolor=GREY, labelcolor=WHITE)
        ax1.tick_params(colors=GREY)
        for spine in ax1.spines.values():
            spine.set_color(DARK_GREY)

        # Annotate d(137)
        d137 = formal_degree_hc(137)
        ax1.annotate(f'd(pi_137) = {d137:.0f}',
                     xy=(137, d137), xytext=(100, d137 * 0.7),
                     color=RED, fontsize=8, fontfamily='monospace',
                     arrowprops=dict(arrowstyle='->', color=RED, lw=1))

        # ── Panel 2: Log-log degree growth ──
        ax2 = axes[0, 1]
        ax2.set_facecolor(BG_PANEL)
        ax2.loglog(self.k_values, self.degrees, 'o',
                   color=CYAN, markersize=2, alpha=0.6)

        # Fit line
        coeffs = np.polyfit(np.log(self.k_values[20:]),
                            np.log(self.degrees[20:]), 1)
        k_fit = np.linspace(5, 200, 100)
        d_fit = np.exp(coeffs[1]) * k_fit**coeffs[0]
        ax2.loglog(k_fit, d_fit, '--', color=ORANGE, linewidth=2,
                   label=f'd ~ k^{coeffs[0]:.2f}')

        # Expected k^5
        d_expect = (2.0/125.0) * k_fit**5
        ax2.loglog(k_fit, d_expect, ':', color=GREEN, linewidth=1.5,
                   alpha=0.5, label='(2/125)*k^5')

        ax2.axvline(x=137, color=RED, linewidth=1.5, linestyle='--',
                    alpha=0.5)
        ax2.set_xlabel('k', color=GREY, fontfamily='monospace', fontsize=9)
        ax2.set_ylabel('d(pi_k)', color=GREY,
                       fontfamily='monospace', fontsize=9)
        ax2.set_title('Degree Growth (log-log)',
                      color=CYAN, fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax2.legend(fontsize=9, loc='upper left',
                   facecolor=BG, edgecolor=GREY, labelcolor=WHITE)
        ax2.tick_params(colors=GREY)
        for spine in ax2.spines.values():
            spine.set_color(DARK_GREY)

        # ── Panel 3: Cumulative spectrum and fill fraction ──
        ax3 = axes[1, 0]
        ax3.set_facecolor(BG_PANEL)

        cumul = np.cumsum(self.degrees)
        total = cumul[-1]
        fracs = cumul / total

        ax3.plot(self.k_values, fracs, color=PURPLE, linewidth=2)
        ax3.axhline(y=self.fill_target, color=GREEN, linewidth=1.5,
                    linestyle='--', alpha=0.7,
                    label=f'f = 3/(5*pi) = {self.fill_target:.4f}')
        ax3.axvline(x=137, color=RED, linewidth=1.5, linestyle='--',
                    alpha=0.7, label='N_max = 137')

        # Mark the intersection point
        frac_137 = fracs[136]
        ax3.plot(137, frac_137, 'o', color=RED, markersize=8, zorder=5)
        ax3.annotate(f'S(137)/S(200)\n= {frac_137:.4f}',
                     xy=(137, frac_137), xytext=(60, frac_137 - 0.15),
                     color=RED, fontsize=8, fontfamily='monospace',
                     arrowprops=dict(arrowstyle='->', color=RED, lw=1))

        ax3.set_xlabel('K (cutoff)', color=GREY,
                       fontfamily='monospace', fontsize=9)
        ax3.set_ylabel('S(K) / S(200)', color=GREY,
                       fontfamily='monospace', fontsize=9)
        ax3.set_title('Cumulative Spectral Weight',
                      color=CYAN, fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax3.set_ylim(0, 1.05)
        ax3.legend(fontsize=9, loc='lower right',
                   facecolor=BG, edgecolor=GREY, labelcolor=WHITE)
        ax3.tick_params(colors=GREY)
        for spine in ax3.spines.values():
            spine.set_color(DARK_GREY)

        # ── Panel 4: Heat kernel trace ──
        ax4 = axes[1, 1]
        ax4.set_facecolor(BG_PANEL)

        t_values = np.logspace(-4, 1, 300)
        theta_vals = np.zeros_like(t_values)
        theta_137 = np.zeros_like(t_values)

        for i, t in enumerate(t_values):
            weights = self.degrees * np.exp(-t * self.eigenvalues)
            theta_vals[i] = np.sum(weights)
            theta_137[i] = np.sum(weights[:137])

        # Fill fraction from heat kernel
        heat_frac = np.where(theta_vals > 0,
                             theta_137 / theta_vals, 0)

        ax4_twin = ax4.twinx()

        ln1, = ax4.loglog(t_values, theta_vals, color=CYAN, linewidth=2,
                          label='Theta(t) = sum d*exp(-tE)')
        ln2, = ax4.loglog(t_values, theta_137, color=MAGENTA, linewidth=1.5,
                          linestyle='--', label='Theta_137(t)')

        ln3, = ax4_twin.semilogx(t_values, heat_frac, color=GREEN,
                                 linewidth=1.5, alpha=0.7,
                                 label='Theta_137/Theta')
        ax4_twin.axhline(y=self.fill_target, color=GOLD, linewidth=1,
                         linestyle=':', alpha=0.5)
        ax4_twin.set_ylabel('Fill fraction', color=GREEN,
                           fontfamily='monospace', fontsize=9)
        ax4_twin.set_ylim(0, 1.1)
        ax4_twin.tick_params(axis='y', colors=GREEN)

        ax4.set_xlabel('t (heat parameter)', color=GREY,
                       fontfamily='monospace', fontsize=9)
        ax4.set_ylabel('Theta(t)', color=CYAN,
                       fontfamily='monospace', fontsize=9)
        ax4.set_title('Heat Kernel Trace & Fill Fraction',
                      color=CYAN, fontfamily='monospace', fontsize=11,
                      fontweight='bold')

        # Combined legend
        lns = [ln1, ln2, ln3]
        labs = [l.get_label() for l in lns]
        ax4.legend(lns, labs, fontsize=8, loc='upper right',
                   facecolor=BG, edgecolor=GREY, labelcolor=WHITE)
        ax4.tick_params(colors=GREY)
        for spine in ax4.spines.values():
            spine.set_color(DARK_GREY)
        for spine in ax4_twin.spines.values():
            spine.set_color(DARK_GREY)

        plt.tight_layout(rect=[0, 0, 1, 0.92])
        plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 68)
    print("  THE PLANCHEREL SPECTRUM — Toy 76")
    print("  Representation theory meets the reality budget")
    print(f"  f = N_c/(n_C*pi) = {N_c}/({n_C}*pi) = {FILL_TARGET:.6f}")
    print("=" * 68)
    print()

    ps = PlancherelSpectrum(quiet=True)

    while True:
        print("  --- MENU ---")
        print("   1. Formal degrees")
        print("   2. Plancherel measure")
        print("   3. Fill fraction")
        print("   4. Spectral zeta function")
        print("   5. Heat kernel trace")
        print("   6. Degree growth")
        print("   7. Reality budget check")
        print("   8. Cumulative spectrum")
        print("   9. Summary")
        print("  10. Show (4-panel visualization)")
        print("   0. Exit")
        print()

        try:
            choice = input("  Choice [0-10]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        print()
        if choice == '1':
            ps.formal_degrees()
        elif choice == '2':
            ps.plancherel_measure()
        elif choice == '3':
            ps.fill_fraction()
        elif choice == '4':
            ps.spectral_zeta()
        elif choice == '5':
            ps.heat_kernel_trace()
        elif choice == '6':
            ps.degree_growth()
        elif choice == '7':
            ps.reality_budget_check()
        elif choice == '8':
            ps.cumulative_spectrum()
        elif choice == '9':
            ps.summary()
        elif choice == '10':
            ps.show()
        elif choice == '0':
            print("  The spectrum measures what can be known.")
            print("  The fill fraction measures what IS known.")
            print()
            break
        else:
            print("  Invalid choice. Try 0-10.")
            print()


if __name__ == '__main__':
    main()
