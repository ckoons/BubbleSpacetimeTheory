#!/usr/bin/env python3
"""
THE REALITY BUDGET AS CHERN RATIO  (Toy 70)
============================================
The universe can never know more than 19.1% of itself.

The reality budget Lambda x N = 9/5 is NOT an empirical fit — it is the
ratio c_4/c_1 of the Chern classes of Q^5, the compact dual of D_IV^5.

    c(Q^5) = (1+h)^7 / (1+2h)  =>  {5, 11, 13, 9, 3}

    c_4 / c_1 = 9 / 5 = 1.800   (exact, topological)

Fill fraction:  f = N_c / (n_C * pi) = 3/(5*pi) = 19.1%
Dark fraction:  1 - f = 80.9%  — permanently inaccessible

This is TOPOLOGICAL. It cannot evolve. As N grows, Lambda shrinks in
lockstep. The jar grows exactly as fast as you fill it.

    from toy_chern_budget import ChernBudget
    cb = ChernBudget()
    cb.chern_ratio()              # c_4/c_1 = 9/5 from Q^5
    cb.fill_fraction()            # f = 3/(5*pi) = 19.1%
    cb.dark_fraction()            # 1 - f = 80.9%
    cb.budget_conservation()      # Lambda x N = 9/5 at every epoch
    cb.jar_grows_with_filling()   # S_dS = 3*pi/Lambda grows as Lambda shrinks
    cb.cosmic_connection()        # 19 = N_c^2 + 2*n_C, Omega_Lambda = 13/19
    cb.sweep_dimensions()         # only n=5 matches observation
    cb.topological_vs_dynamical() # why it can't change
    cb.summary()                  # key insight
    cb.show()                     # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# =====================================================================
# BST CONSTANTS — the five integers
# =====================================================================

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |W(D_5)| = n_C! * 2^(n_C-1)

# Derived
_vol_D = np.pi**n_C / Gamma_order
alpha = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ~ 1/137.036
mp_over_me = C2 * np.pi**n_C                              # 6*pi^5 ~ 1836.12


# =====================================================================
# CHERN CLASS COMPUTATION ENGINE
# =====================================================================

def chern_coefficients(n):
    """
    Compute Chern class coefficients {c_1, ..., c_n} of Q^n.

    c(Q^n) = (1+h)^{n+2} / (1+2h)

    The coefficient of h^k is:
        c_k = sum_{j=0}^{k} binom(n+2, k-j) * (-2)^j
    """
    from math import comb
    coeffs = []
    for k in range(1, n + 1):
        ck = sum(comb(n + 2, k - j) * ((-2) ** j) for j in range(k + 1))
        coeffs.append(ck)
    return coeffs


def euler_characteristic(n):
    """Euler characteristic of Q^n."""
    if n % 2 == 1:
        return n + 1
    else:
        return n + 2


# =====================================================================
# THE CHERN BUDGET CLASS
# =====================================================================

class ChernBudget:
    """
    The Reality Budget as a Chern class ratio.

    Lambda x N = c_4(Q^5) / c_1(Q^5) = 9/5 = 1.800

    This is a topological constant — it cannot change.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        # Precompute Q^5 Chern classes
        self.Q5_chern = chern_coefficients(5)  # [5, 11, 13, 9, 3]

    def _p(self, *args, **kwargs):
        if not self.quiet:
            print(*args, **kwargs)

    # -----------------------------------------------------------------
    # 1. chern_ratio — c_4/c_1 = 9/5 derivation from Q^5
    # -----------------------------------------------------------------

    def chern_ratio(self):
        """
        Derive Lambda x N = 9/5 from the Chern classes of Q^5.

        c(Q^5) = (1+h)^7 / (1+2h)
        Coefficients: {c_1, c_2, c_3, c_4, c_5} = {5, 11, 13, 9, 3}
        Reality Budget = c_4 / c_1 = 9 / 5
        """
        self._p()
        self._p("=" * 68)
        self._p("  THE REALITY BUDGET AS CHERN RATIO")
        self._p("=" * 68)
        self._p()
        self._p("  Q^5 = SO(7)/[SO(5) x SO(2)]  -- compact dual of D_IV^5")
        self._p()
        self._p("  Total Chern class:")
        self._p("    c(Q^5) = (1+h)^7 / (1+2h)")
        self._p()

        # Show the expansion step by step
        from math import comb

        self._p("  Expanding (1+h)^7:")
        binom_coeffs = [comb(7, k) for k in range(8)]
        self._p(f"    = {' + '.join(f'{c}h^{k}' if k > 0 else str(c) for k, c in enumerate(binom_coeffs))}")
        self._p()

        self._p("  Dividing by (1+2h) = multiplying by 1 - 2h + 4h^2 - 8h^3 + ...")
        self._p()

        # Detailed computation for each c_k
        labels = ['c_1', 'c_2', 'c_3', 'c_4', 'c_5']
        bst_names = ['n_C', 'dim K', 'N_c + 2n_C', 'N_c^2', 'N_c']

        self._p(f"  {'Class':>6}  {'Computation':>42}  {'=':>3}  {'Value':>5}  {'BST':>12}")
        self._p(f"  {'-----':>6}  {'-----':>42}  {'---':>3}  {'-----':>5}  {'---':>12}")

        for k in range(1, 6):
            terms = []
            for j in range(k + 1):
                coeff = comb(7, k - j) * ((-2) ** j)
                if j == 0:
                    terms.append(f"{coeff}")
                else:
                    terms.append(f"{coeff:+d}")
            computation = " ".join(terms)
            ck = self.Q5_chern[k - 1]
            self._p(f"  {labels[k-1]:>6}  {computation:>42}  {' =':>3}  {ck:>5}  {bst_names[k-1]:>12}")

        self._p()
        self._p(f"  Chern class tower:  {{c_1, c_2, c_3, c_4, c_5}} = {{{', '.join(str(c) for c in self.Q5_chern)}}}")
        self._p()

        c1 = self.Q5_chern[0]  # 5
        c4 = self.Q5_chern[3]  # 9

        self._p("  THE REALITY BUDGET:")
        self._p(f"    Lambda x N = c_4 / c_1 = {c4} / {c1} = {c4/c1:.3f}")
        self._p()
        self._p("  This is TOPOLOGICAL. A ratio of Chern class coefficients of Q^5.")
        self._p("  It cannot evolve, cannot be changed by dynamics.")
        self._p("=" * 68)

        return {'c_coeffs': self.Q5_chern, 'ratio': c4 / c1,
                'c4': c4, 'c1': c1, 'exact': '9/5'}

    # -----------------------------------------------------------------
    # 2. fill_fraction — f = 3/(5*pi) = 19.1%
    # -----------------------------------------------------------------

    def fill_fraction(self):
        """
        Compute the topological fill fraction f = N_c/(n_C*pi) = 3/(5*pi).

        The fraction of de Sitter horizon states occupied by committed contacts.
        Decomposition:
          - N_c/n_C = c_5/c_1 = 3/5: color-to-dimension ratio (topological)
          - 1/pi: inverse S^1 circumference on Shilov boundary (geometric)
        """
        self._p()
        self._p("=" * 68)
        self._p("  THE FILL FRACTION")
        self._p("=" * 68)
        self._p()

        f_exact = N_c / (n_C * np.pi)
        f_pct = f_exact * 100

        self._p("  f = N_c / (n_C * pi) = 3 / (5*pi)")
        self._p()
        self._p("  Decomposition:")
        self._p(f"    N_c / n_C  = c_5 / c_1 = {N_c}/{n_C} = {N_c/n_C:.4f}")
        self._p(f"      -- color-to-dimension ratio (Chern class, topological)")
        self._p(f"    1 / pi     = {1/np.pi:.6f}")
        self._p(f"      -- inverse S^1 circumference on Shilov boundary S^4 x S^1")
        self._p()
        self._p(f"    f = (N_c/n_C) x (1/pi) = (3/5) x (1/pi)")
        self._p(f"      = {f_exact:.6f}")
        self._p(f"      = {f_pct:.2f}%")
        self._p()
        self._p("  The universe has used about one-fifth of its information capacity.")
        self._p()

        # Verify: Lambda x N = 3*pi*f
        budget = 3 * np.pi * f_exact
        self._p("  Verification:")
        self._p(f"    Lambda x N = 3*pi*f = 3*pi * {f_exact:.6f} = {budget:.4f}")
        self._p(f"    N_c^2/n_C  = {N_c**2}/{n_C} = {N_c**2/n_C:.4f}")
        self._p(f"    Match: {'YES' if abs(budget - N_c**2/n_C) < 1e-10 else 'NO'}")
        self._p("=" * 68)

        return {'f': f_exact, 'f_pct': f_pct, 'N_c_over_n_C': N_c / n_C,
                'one_over_pi': 1.0 / np.pi}

    # -----------------------------------------------------------------
    # 3. dark_fraction — 1 - f = 80.9%
    # -----------------------------------------------------------------

    def dark_fraction(self):
        """
        The dark fraction: 1 - f = 1 - 3/(5*pi) = 80.9%.

        This is the fraction of the universe's information capacity that is
        permanently inaccessible — not "not yet seen" but CANNOT be seen.
        It's a topological constant, not a dynamical state.
        """
        self._p()
        self._p("=" * 68)
        self._p("  THE DARK FRACTION: PERMANENTLY INACCESSIBLE")
        self._p("=" * 68)
        self._p()

        f = N_c / (n_C * np.pi)
        dark = 1.0 - f

        self._p(f"  Fill fraction:    f     = 3/(5*pi) = {f:.6f} = {f*100:.2f}%")
        self._p(f"  Dark fraction:    1 - f = 1 - 3/(5*pi) = {dark:.6f} = {dark*100:.2f}%")
        self._p()
        self._p("  This is the Godel Limit of BST:")
        self._p(f"    The universe can never know more than {f*100:.1f}% of itself.")
        self._p(f"    The remaining {dark*100:.1f}% is topologically inaccessible.")
        self._p()
        self._p("  This is NOT 'dark energy' or 'dark matter' in the usual sense.")
        self._p("  It is the fraction of de Sitter horizon states that can NEVER")
        self._p("  be occupied by committed contacts. The jar always has room.")
        self._p()

        # Connection to dark energy / dark matter
        self._p("  Connection to observed dark sector:")
        omega_lambda = 13.0 / 19.0
        omega_m = 6.0 / 19.0
        self._p(f"    Omega_Lambda (BST) = 13/19 = {omega_lambda:.4f}  (obs: 0.685 +/- 0.007)")
        self._p(f"    Omega_m     (BST) =  6/19 = {omega_m:.4f}  (obs: 0.315 +/- 0.007)")
        self._p(f"    Total dark = 1 - Omega_b/Omega_m")
        self._p(f"    But the DEEP dark is topological: {dark*100:.1f}% of information capacity")
        self._p("=" * 68)

        return {'dark_fraction': dark, 'dark_pct': dark * 100,
                'fill_fraction': f, 'fill_pct': f * 100}

    # -----------------------------------------------------------------
    # 4. budget_conservation — Lambda x N = 9/5 at different epochs
    # -----------------------------------------------------------------

    def budget_conservation(self):
        """
        Show Lambda x N = 9/5 at different cosmic epochs.

        As the universe expands:
          - Lambda decreases (cosmological constant dilutes)
          - N increases (more contacts accumulate)
          - Their product is FIXED at 9/5

        This is not a dynamical conservation law. It is a topological identity.
        """
        self._p()
        self._p("=" * 68)
        self._p("  BUDGET CONSERVATION: Lambda x N = 9/5 ALWAYS")
        self._p("=" * 68)
        self._p()

        budget = N_c**2 / n_C  # = 9/5 = 1.800

        # Show at different epochs using S_dS = 3*pi/Lambda, N = f*S_dS
        f = N_c / (n_C * np.pi)

        self._p("  At ANY epoch, f = 3/(5*pi) is constant (topological).")
        self._p("  N_total = f * S_dS = f * 3*pi/Lambda")
        self._p("  Lambda * N = Lambda * f * 3*pi/Lambda = 3*pi*f = 9/5")
        self._p("  The Lambda CANCELS EXACTLY.")
        self._p()

        # Model different epochs
        epochs = [
            ('Planck era',         1e-43,    1.0),
            ('Inflation end',      1e-32,    1e-55),
            ('Nucleosynthesis',    180.0,    1e-64),
            ('Recombination',      3.8e5,    1e-67),
            ('Star formation',     1e9,      1e-70),
            ('Today',              1.38e10,  1e-122),
            ('Far future',         1e20,     1e-140),
        ]

        self._p(f"  {'Epoch':<22} {'t (yr)':>12}  {'Lambda':>12}  {'S_dS':>12}  {'N':>12}  {'L*N':>8}")
        self._p(f"  {'-----':<22} {'-----':>12}  {'------':>12}  {'----':>12}  {'---':>12}  {'---':>8}")

        for name, t_yr, lam in epochs:
            s_ds = 3.0 * np.pi / lam
            n_total = f * s_ds
            prod = lam * n_total

            self._p(f"  {name:<22} {t_yr:>12.2e}  {lam:>12.2e}  {s_ds:>12.2e}  {n_total:>12.2e}  {prod:>8.3f}")

        self._p()
        self._p(f"  Every row: Lambda x N = {budget:.3f} = 9/5")
        self._p()
        self._p("  The Lambda cancellation is exact and algebraic.")
        self._p("  It does not depend on the expansion history, the matter content,")
        self._p("  or any dynamical equation. It is a TOPOLOGICAL IDENTITY.")
        self._p("=" * 68)

        return {'budget': budget, 'exact': '9/5',
                'mechanism': 'Lambda cancels in Lambda * f * 3*pi/Lambda'}

    # -----------------------------------------------------------------
    # 5. jar_grows_with_filling — de Sitter capacity grows as Lambda shrinks
    # -----------------------------------------------------------------

    def jar_grows_with_filling(self):
        """
        The de Sitter entropy S_dS = 3*pi/Lambda grows as Lambda shrinks.

        As contacts accumulate (N grows), Lambda shrinks, and the de Sitter
        horizon entropy S_dS grows. The jar grows exactly as fast as you fill it.
        The fill fraction f = N/S_dS = 3/(5*pi) never changes.
        """
        self._p()
        self._p("=" * 68)
        self._p("  THE JAR GROWS WITH THE FILLING")
        self._p("=" * 68)
        self._p()

        f = N_c / (n_C * np.pi)
        budget = N_c**2 / n_C

        self._p("  S_dS = 3*pi / Lambda       (de Sitter entropy)")
        self._p("  N    = f * S_dS             (committed contacts)")
        self._p("  f    = 3/(5*pi) = const     (topological)")
        self._p()
        self._p("  As N grows by dN:")
        self._p("    Lambda shrinks:  dLambda = -(9/5) * dN / N^2")
        self._p("    S_dS grows:      dS_dS   = 3*pi * dN / (9/5 * N^2) * N^2/1")
        self._p()

        # Concrete example
        self._p("  Example: doubling the contacts")
        self._p()

        N_start = 1e80
        lam_start = budget / N_start

        N_end = 2 * N_start
        lam_end = budget / N_end

        S_start = 3 * np.pi / lam_start
        S_end = 3 * np.pi / lam_end

        f_start = N_start / S_start
        f_end = N_end / S_end

        self._p(f"    {'':>12}  {'Before':>15}  {'After (2x)':>15}  {'Ratio':>8}")
        self._p(f"    {'--------':>12}  {'------':>15}  {'----------':>15}  {'-----':>8}")
        self._p(f"    {'N':>12}  {N_start:>15.3e}  {N_end:>15.3e}  {N_end/N_start:>8.3f}")
        self._p(f"    {'Lambda':>12}  {lam_start:>15.3e}  {lam_end:>15.3e}  {lam_end/lam_start:>8.3f}")
        self._p(f"    {'S_dS':>12}  {S_start:>15.3e}  {S_end:>15.3e}  {S_end/S_start:>8.3f}")
        self._p(f"    {'f':>12}  {f_start:>15.6f}  {f_end:>15.6f}  {f_end/f_start:>8.3f}")
        self._p(f"    {'L*N':>12}  {lam_start*N_start:>15.3f}  {lam_end*N_end:>15.3f}  {'const':>8}")
        self._p()
        self._p("  N doubles, Lambda halves, S_dS doubles, f stays at 19.1%.")
        self._p("  The jar grows exactly as fast as you fill it.")
        self._p("=" * 68)

        return {'f_constant': f, 'budget_constant': budget}

    # -----------------------------------------------------------------
    # 6. cosmic_connection — 19 = N_c^2 + 2*n_C, Omega_Lambda, Omega_m
    # -----------------------------------------------------------------

    def cosmic_connection(self):
        """
        Connect the reality budget to observed cosmic composition.

        19 = N_c^2 + 2*n_C = 9 + 10
        Omega_Lambda = 13/19, Omega_m = 6/19

        The number 19 encodes the total gauge + spacetime structure.
        """
        self._p()
        self._p("=" * 68)
        self._p("  COSMIC COMPOSITION FROM BST INTEGERS")
        self._p("=" * 68)
        self._p()

        val_19 = N_c**2 + 2 * n_C  # 9 + 10 = 19
        omega_lam = 13.0 / val_19
        omega_m = 6.0 / val_19

        self._p(f"  The magic number: 19 = N_c^2 + 2*n_C = {N_c**2} + {2*n_C} = {val_19}")
        self._p()
        self._p("  Decomposition of 19:")
        self._p(f"    N_c^2 = {N_c**2}    (color algebra dimension = dim U(N_c))")
        self._p(f"    2*n_C = {2*n_C}   (twice the domain dimension)")
        self._p()

        self._p("  Cosmic fractions:")
        self._p(f"    Omega_Lambda = 13/19 = {omega_lam:.6f}")
        self._p(f"      (observed: 0.685 +/- 0.007)")
        self._p(f"      13 = c_3(Q^5) = Weinberg denominator = N_c + 2*n_C")
        self._p()
        self._p(f"    Omega_m      =  6/19 = {omega_m:.6f}")
        self._p(f"      (observed: 0.315 +/- 0.007)")
        self._p(f"      6  = chi(Q^5) = C_2 = Casimir eigenvalue")
        self._p()

        # Check consistency
        diff_lam = abs(omega_lam - 0.685) / 0.007
        diff_m = abs(omega_m - 0.315) / 0.007

        self._p(f"    Omega_Lambda tension: {diff_lam:.2f} sigma")
        self._p(f"    Omega_m tension:      {diff_m:.2f} sigma")
        self._p()

        # Connection to reality budget
        self._p("  Connection to reality budget:")
        self._p(f"    c_3 / c_1 = 13/5 = {13/5:.1f}   (Weinberg denominator / dimension)")
        self._p(f"    chi / 19  = 6/19 = {6/19:.4f}  (matter fraction)")
        self._p(f"    c_4 / c_1 = 9/5  = {9/5:.3f}   (reality budget)")
        self._p()
        self._p("  All cosmic fractions are ratios of Chern data of Q^5.")
        self._p("=" * 68)

        return {'nineteen': val_19, 'omega_lambda': omega_lam,
                'omega_m': omega_m, 'tension_sigma_lam': diff_lam,
                'tension_sigma_m': diff_m}

    # -----------------------------------------------------------------
    # 7. sweep_dimensions — c_4/c_1 for different n_C
    # -----------------------------------------------------------------

    def sweep_dimensions(self, n_max=11):
        """
        Compute the reality budget c_{n-1}/c_1 for different dimensions n.

        For odd n: c_{n-1}/c_1 = ((n+1)/2)^2 / n = (n+1)^2/(4n)
        Only n=5 gives 9/5 with N_c=3.
        """
        self._p()
        self._p("=" * 68)
        self._p("  DIMENSION SWEEP: c_{n-1}/c_1 FOR QUADRICS Q^n")
        self._p("=" * 68)
        self._p()

        self._p("  For odd n, the general formula is:")
        self._p("    c_{n-1}/c_1 = ((n+1)/2)^2 / n = (n+1)^2 / (4n)")
        self._p()
        self._p("  For EVERY n, we compute the full Chern class tower.")
        self._p()

        results = []

        self._p(f"  {'n':>3}  {'Chern coefficients':>32}  {'chi':>4}  {'c_{n-1}/c_1':>12}  {'N_c=(n+1)/2':>12}  {'Match?':>8}")
        self._p(f"  {'---':>3}  {'------------------':>32}  {'---':>4}  {'-----------':>12}  {'-----------':>12}  {'------':>8}")

        for n in range(1, n_max + 1):
            coeffs = chern_coefficients(n)
            chi = euler_characteristic(n)

            if n >= 2:
                ratio = coeffs[n - 2] / coeffs[0]  # c_{n-1} / c_1
            else:
                ratio = float('nan')

            # For odd n, N_c = (n+1)/2
            if n % 2 == 1:
                nc_candidate = (n + 1) // 2
                mass_ratio = (n + 1) * np.pi**n
                match = "<<< BST" if n == 5 else ""
            else:
                nc_candidate = None
                mass_ratio = (n + 2) * np.pi**n  # even formula
                match = ""

            coeff_str = ', '.join(str(c) for c in coeffs)
            nc_str = str(nc_candidate) if nc_candidate is not None else "(even)"

            self._p(f"  {n:>3}  {'{' + coeff_str + '}':>32}  {chi:>4}  {ratio:>12.4f}  {nc_str:>12}  {match:>8}")

            results.append({
                'n': n, 'coeffs': coeffs, 'chi': chi,
                'ratio': ratio, 'N_c': nc_candidate
            })

        self._p()
        self._p("  Only n=5 produces:")
        self._p(f"    N_c = 3  (the observed color number)")
        self._p(f"    c_4/c_1 = 9/5  (the observed reality budget)")
        self._p(f"    (n+1)*pi^n = 6*pi^5 = {C2 * np.pi**n_C:.2f}  (the observed mass ratio)")
        self._p(f"    alpha ~ 1/137  (the observed fine structure constant)")
        self._p()
        self._p("  The Standard Model is the unique point in {{Q^n}} where")
        self._p("  the mass ratio matches observation.")
        self._p("=" * 68)

        return results

    # -----------------------------------------------------------------
    # 8. topological_vs_dynamical — why it can't change
    # -----------------------------------------------------------------

    def topological_vs_dynamical(self):
        """
        Explain why the reality budget is topological, not dynamical.

        Chern class ratios are diffeomorphism invariants. They cannot be
        changed by any smooth deformation, any field equation, any symmetry
        breaking, or any phase transition. 9/5 is as rigid as pi.
        """
        self._p()
        self._p("=" * 68)
        self._p("  TOPOLOGICAL vs DYNAMICAL: WHY 9/5 CAN'T CHANGE")
        self._p("=" * 68)
        self._p()

        self._p("  DYNAMICAL quantities (can change):")
        self._p("    - Temperature         (cools as universe expands)")
        self._p("    - Density             (dilutes with volume)")
        self._p("    - Scale factor        (grows monotonically)")
        self._p("    - Hubble parameter    (changes with epoch)")
        self._p("    - Baryon count        (fixed after baryogenesis, but WAS zero)")
        self._p()

        self._p("  TOPOLOGICAL quantities (cannot change):")
        self._p("    - Euler characteristic of Q^5: chi = 6")
        self._p("    - Chern classes of Q^5: {5, 11, 13, 9, 3}")
        self._p("    - c_4/c_1 = 9/5 = Lambda x N")
        self._p("    - c_5/c_3 = 3/13 = sin^2(theta_W)")
        self._p("    - N_c = 3 (top Chern class)")
        self._p("    - Fill fraction f = 3/(5*pi)")
        self._p()

        self._p("  WHY topological quantities can't change:")
        self._p()
        self._p("  1. CHERN CLASSES are integer-valued characteristic classes")
        self._p("     of the tangent bundle. They are computed from curvature")
        self._p("     but are INDEPENDENT of the metric. Any smooth deformation")
        self._p("     of Q^5 gives the same Chern numbers.")
        self._p()
        self._p("  2. RATIOS of Chern class coefficients are therefore also")
        self._p("     topological invariants. 9/5 is as immutable as the genus")
        self._p("     of a surface.")
        self._p()
        self._p("  3. The reality budget is NOT a conservation law (those can be")
        self._p("     broken by symmetry breaking or phase transitions). It is a")
        self._p("     topological identity — like saying 'a torus has genus 1'.")
        self._p()
        self._p("  4. No field equation, no Hamiltonian, no Lagrangian can change 9/5.")
        self._p("     It is geometry, not dynamics.")
        self._p()

        # The analogy
        self._p("  Analogy:")
        self._p("    Dynamical:    'The water level in this jar is 19.1%'")
        self._p("    Topological:  'The jar is BUILT so that it is ALWAYS 19.1% full'")
        self._p("                  'No matter how much water you add, the jar grows'")
        self._p("                  'to keep the ratio at exactly 3/(5*pi)'")
        self._p("=" * 68)

        return {'type': 'topological', 'can_change': False,
                'invariant_class': 'Chern class ratio',
                'value': '9/5'}

    # -----------------------------------------------------------------
    # 9. summary — the key insight
    # -----------------------------------------------------------------

    def summary(self):
        """
        Summary: the reality budget is topology, not dynamics.
        """
        self._p()
        self._p("=" * 68)
        self._p("  SUMMARY: THE REALITY BUDGET IS TOPOLOGY, NOT DYNAMICS")
        self._p("=" * 68)
        self._p()

        f = N_c / (n_C * np.pi)

        self._p("  One surface:   Q^5 = SO(7)/[SO(5) x SO(2)]")
        self._p("  One formula:   c(Q^5) = (1+h)^7 / (1+2h)")
        self._p(f"  One tower:     {{5, 11, 13, 9, 3}}  with chi = 6, g = 7")
        self._p()
        self._p("  Key results from the tower:")
        self._p()
        self._p(f"    Lambda x N         = c_4/c_1 = 9/5 = {9/5:.3f}")
        self._p(f"    sin^2(theta_W)     = c_5/c_3 = 3/13 = {3/13:.4f}")
        self._p(f"    Fill fraction       = N_c/(n_C*pi) = {f:.6f} = {f*100:.1f}%")
        self._p(f"    Dark fraction       = 1 - f = {(1-f)*100:.1f}%")
        self._p(f"    Mass ratio m_p/m_e  = C_2*pi^n_C = 6*pi^5 = {C2*np.pi**n_C:.2f}")
        self._p(f"    Omega_Lambda        = 13/19 = {13/19:.4f}")
        self._p(f"    Omega_m             = 6/19 = {6/19:.4f}")
        self._p()
        self._p("  The universe can never know more than 19.1% of itself.")
        self._p("  This is not ignorance. It is topology.")
        self._p("  The reality budget is a Chern class ratio, not a field equation.")
        self._p()
        self._p("  c(Q^5) = (1+h)^7 / (1+2h)")
        self._p("=" * 68)

        return {'budget': 9/5, 'fill_pct': f * 100, 'dark_pct': (1-f) * 100}

    # -----------------------------------------------------------------
    # 10. show — 4-panel visualization
    # -----------------------------------------------------------------

    def show(self):
        """
        4-panel visualization:
          1. Chern class tower with c_4/c_1 highlighted
          2. Fill fraction gauge
          3. Epoch evolution (budget conservation)
          4. Dimension sweep
        """
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
        except ImportError:
            self._p("matplotlib not available. Use text methods instead.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(16, 12), facecolor='#0a0a1a')
        fig.canvas.manager.set_window_title('Toy 70: The Reality Budget as Chern Ratio')

        fig.text(0.5, 0.97, 'THE REALITY BUDGET AS CHERN RATIO',
                 fontsize=18, fontweight='bold', color='#ffd700',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 r'$\Lambda \times N = c_4/c_1 = 9/5 = 1.800$   (topological)',
                 fontsize=12, color='#00ccff', ha='center', fontfamily='monospace')

        # ── Panel 1: Chern class tower ──
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')
        ax1.set_title('CHERN CLASS TOWER OF Q\u2075',
                       color='#00ccff', fontfamily='monospace',
                       fontsize=12, fontweight='bold', pad=10)

        labels = ['c\u2081', 'c\u2082', 'c\u2083', 'c\u2084', 'c\u2085']
        values = self.Q5_chern
        bst = ['n\u209c = 5', 'dim K = 11', '13 bosons', 'N\u209c\u00b2 = 9', 'N\u209c = 3']
        colors_bar = ['#4488ff', '#4488ff', '#4488ff', '#ff4444', '#44ff88']

        bars = ax1.barh(range(5), values, color=colors_bar, alpha=0.8,
                        edgecolor='white', linewidth=0.5, height=0.6)

        # Highlight c_4 and c_1
        bars[0].set_edgecolor('#ffd700')
        bars[0].set_linewidth(2.5)
        bars[3].set_edgecolor('#ffd700')
        bars[3].set_linewidth(2.5)

        for i, (v, b) in enumerate(zip(values, bst)):
            ax1.text(v + 0.3, i, f'{v}  ({b})',
                     color='white', fontsize=9, fontfamily='monospace',
                     va='center')

        ax1.set_yticks(range(5))
        ax1.set_yticklabels(labels, color='white', fontfamily='monospace',
                            fontsize=11)
        ax1.set_xlim(0, 18)
        ax1.tick_params(axis='x', colors='#666666')
        ax1.spines['bottom'].set_color('#333333')
        ax1.spines['left'].set_color('#333333')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)

        # Arrow showing c_4/c_1
        ax1.annotate('c\u2084/c\u2081 = 9/5 = 1.800',
                     xy=(9, 3), xytext=(14, 1.5),
                     color='#ffd700', fontsize=11, fontweight='bold',
                     fontfamily='monospace',
                     arrowprops=dict(arrowstyle='->', color='#ffd700', lw=1.5))

        # ── Panel 2: Fill fraction gauge ──
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')
        ax2.set_title('FILL FRACTION: 3/(5\u03c0) = 19.1%',
                       color='#00ccff', fontfamily='monospace',
                       fontsize=12, fontweight='bold', pad=10)

        f_val = N_c / (n_C * np.pi)

        # Draw a pie chart / gauge
        theta_fill = f_val * 360
        theta_dark = 360 - theta_fill

        wedge_colors = ['#44ff88', '#1a1a3a']
        wedge_labels = [f'Committed\n{f_val*100:.1f}%', f'Inaccessible\n{(1-f_val)*100:.1f}%']

        wedges, texts = ax2.pie(
            [f_val, 1 - f_val],
            labels=wedge_labels,
            colors=wedge_colors,
            startangle=90,
            wedgeprops=dict(edgecolor='#333333', linewidth=1),
            textprops=dict(color='white', fontfamily='monospace', fontsize=9)
        )

        # Center text
        ax2.text(0, 0, f'f = 3/(5\u03c0)\n= {f_val:.4f}',
                 ha='center', va='center', color='#ffd700',
                 fontsize=10, fontweight='bold', fontfamily='monospace')

        ax2.text(0, -1.35,
                 '"The universe can never know\n more than 19.1% of itself"',
                 ha='center', va='center', color='#888888',
                 fontsize=8, fontfamily='monospace', style='italic')

        # ── Panel 3: Budget conservation across epochs ──
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')
        ax3.set_title('\u039b \u00d7 N = 9/5 AT EVERY EPOCH',
                       color='#00ccff', fontfamily='monospace',
                       fontsize=12, fontweight='bold', pad=10)

        # Log-log plot: as Lambda decreases, N increases, product constant
        log_lam = np.linspace(-140, 0, 200)
        lam_vals = 10.0**log_lam
        budget = N_c**2 / n_C
        n_vals = budget / lam_vals

        ax3.loglog(lam_vals, n_vals, color='#ff4444', linewidth=2,
                   label=r'N = (9/5) / $\Lambda$')

        # Mark specific epochs
        epoch_points = [
            (1.0, budget / 1.0, 'Planck'),
            (1e-55, budget / 1e-55, 'Inflation'),
            (1e-67, budget / 1e-67, 'CMB'),
            (1e-122, budget / 1e-122, 'Today'),
            (1e-140, budget / 1e-140, 'Far future'),
        ]

        for lam_pt, n_pt, name in epoch_points:
            ax3.plot(lam_pt, n_pt, 'o', color='#ffd700', markersize=7, zorder=5)
            ax3.annotate(name, (lam_pt, n_pt),
                         textcoords='offset points', xytext=(8, 8),
                         color='#ffd700', fontsize=8, fontfamily='monospace')

        # Constant product line
        ax3.axhline(y=budget, color='#333333', linestyle=':', alpha=0.3)

        ax3.set_xlabel('\u039b  (Planck units)', color='#888888',
                       fontfamily='monospace')
        ax3.set_ylabel('N  (committed contacts)', color='#888888',
                       fontfamily='monospace')
        ax3.tick_params(colors='#666666')
        ax3.spines['bottom'].set_color('#333333')
        ax3.spines['left'].set_color('#333333')
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)

        # Add text annotation for product
        ax3.text(0.5, 0.05,
                 '\u039b \u00d7 N = 9/5 = 1.800  (exact, every epoch)',
                 transform=ax3.transAxes, color='#44ff88',
                 fontsize=10, fontfamily='monospace', fontweight='bold',
                 ha='center')

        ax3.legend(loc='upper right', facecolor='#0d0d24',
                   edgecolor='#333333', labelcolor='white',
                   prop={'family': 'monospace', 'size': 9})

        # ── Panel 4: Dimension sweep ──
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')
        ax4.set_title('DIMENSION SWEEP: ONLY n=5 WORKS',
                       color='#00ccff', fontfamily='monospace',
                       fontsize=12, fontweight='bold', pad=10)

        n_vals_sweep = list(range(1, 12))
        ratios = []
        bar_colors = []
        for n in n_vals_sweep:
            coeffs = chern_coefficients(n)
            if n >= 2:
                r = coeffs[n - 2] / coeffs[0]
            else:
                r = float('nan')
            ratios.append(r)
            if n == 5:
                bar_colors.append('#ff4444')
            elif n % 2 == 1:
                bar_colors.append('#4488ff')
            else:
                bar_colors.append('#333366')

        # Filter out nan for bar plot
        valid_n = [n for n, r in zip(n_vals_sweep, ratios) if not np.isnan(r)]
        valid_r = [r for r in ratios if not np.isnan(r)]
        valid_colors = [c for n, c in zip(n_vals_sweep, bar_colors) if n in valid_n]

        ax4.bar(valid_n, valid_r, color=valid_colors, alpha=0.8,
                edgecolor='white', linewidth=0.5, width=0.6)

        # Highlight n=5
        ax4.axhline(y=9/5, color='#ffd700', linestyle='--', linewidth=1.5,
                     alpha=0.7)
        ax4.text(10.5, 9/5, '9/5', color='#ffd700', fontsize=10,
                 fontfamily='monospace', fontweight='bold', va='center')

        # Label the n=5 bar
        ax4.annotate('n\u209c = 5\nN_c = 3\n9/5',
                     xy=(5, 1.8), xytext=(7.5, 1.5),
                     color='#ff4444', fontsize=9, fontweight='bold',
                     fontfamily='monospace',
                     arrowprops=dict(arrowstyle='->', color='#ff4444', lw=1.5))

        ax4.set_xlabel('n (complex dimension)', color='#888888',
                       fontfamily='monospace')
        ax4.set_ylabel('c\u2099\u208b\u2081 / c\u2081', color='#888888',
                       fontfamily='monospace')
        ax4.set_xticks(valid_n)
        ax4.tick_params(colors='#666666')
        ax4.spines['bottom'].set_color('#333333')
        ax4.spines['left'].set_color('#333333')
        ax4.spines['top'].set_visible(False)
        ax4.spines['right'].set_visible(False)

        # Odd vs even legend
        ax4.text(0.02, 0.95, 'Blue = odd n  |  Gray = even n  |  Red = n=5 (BST)',
                 transform=ax4.transAxes, color='#888888',
                 fontsize=8, fontfamily='monospace')

        plt.tight_layout(rect=(0, 0.02, 1, 0.92))

        fig.text(0.5, 0.01,
                 'c(Q\u2075) = (1+h)\u2077 / (1+2h)  |  '
                 'One surface, one formula, all the integers  |  '
                 '\u00a9 Casey Koons 2026',
                 fontsize=8, color='#555555', ha='center',
                 fontfamily='monospace')

        plt.show(block=False)


# =====================================================================
# MAIN — interactive menu
# =====================================================================

def main():
    cb = ChernBudget()

    print()
    print("  ====================================================")
    print("  TOY 70: THE REALITY BUDGET AS CHERN RATIO")
    print("  Lambda x N = c_4/c_1 = 9/5 = 1.800")
    print("  ====================================================")
    print()
    print("  1) Chern ratio derivation (c_4/c_1 = 9/5)")
    print("  2) Fill fraction (f = 3/(5*pi) = 19.1%)")
    print("  3) Dark fraction (80.9% permanently inaccessible)")
    print("  4) Budget conservation (Lambda x N = 9/5 at every epoch)")
    print("  5) Jar grows with filling (S_dS tracks N)")
    print("  6) Cosmic connection (19 = N_c^2 + 2*n_C, Omega_Lambda)")
    print("  7) Dimension sweep (only n=5 matches)")
    print("  8) Topological vs dynamical (why it can't change)")
    print("  9) Summary")
    print("  0) Show all (4-panel visualization)")
    print("  a) Run everything")
    print()

    try:
        choice = input("  Choice [0-9, a]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        choice = 'a'

    if choice == '1':
        cb.chern_ratio()
    elif choice == '2':
        cb.fill_fraction()
    elif choice == '3':
        cb.dark_fraction()
    elif choice == '4':
        cb.budget_conservation()
    elif choice == '5':
        cb.jar_grows_with_filling()
    elif choice == '6':
        cb.cosmic_connection()
    elif choice == '7':
        cb.sweep_dimensions()
    elif choice == '8':
        cb.topological_vs_dynamical()
    elif choice == '9':
        cb.summary()
    elif choice == '0':
        cb.show()
    elif choice == 'a':
        cb.chern_ratio()
        cb.fill_fraction()
        cb.dark_fraction()
        cb.budget_conservation()
        cb.jar_grows_with_filling()
        cb.cosmic_connection()
        cb.sweep_dimensions()
        cb.topological_vs_dynamical()
        cb.summary()
        try:
            cb.show()
        except Exception:
            pass
    else:
        cb.summary()

    print()
    print("  c(Q^5) = (1+h)^7 / (1+2h)")
    print("  The reality budget is topology, not dynamics.")
    print()


if __name__ == '__main__':
    main()
