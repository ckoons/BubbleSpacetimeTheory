#!/usr/bin/env python3
"""
TOY 119 — NUCLEON MAGNETIC MOMENTS FROM BST
=============================================================

The proton and neutron magnetic moments -- among the most precisely
measured quantities in physics -- derived from D_IV^5 geometry.

    mu_p = 2g / n_C = 14/5 = 2.800  mu_N     (0.26%)
    mu_n = -C_2 / pi = -6/pi = -1.910  mu_N   (0.17%)

The proton is algebraic (genus / dimension).  The neutron is
transcendental (Casimir / pi).  The ratio:

    mu_p / mu_n = -7*pi/15 = -1.4661           (0.43%)

SU(6) quark model gives mu_p/mu_n = -3/2 = -1.500 (2.74% error).
BST is 6 times more accurate.

The proton magnetic moment equals 8 times the strong coupling:
    mu_p = (N_c^2 - 1) * alpha_s(m_p) = 8 * 7/20 = 14/5

The anomalous magnetic moment kappa_p = 9/5 = the Reality Budget.
Zero free parameters.  One geometry.

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from fractions import Fraction
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Circle, Arc, Wedge
from matplotlib.gridspec import GridSpec

# ─── BST Constants ───
N_c   = 3           # color charges
n_C   = 5           # domain dimension (D_IV^5)
C_2   = 6           # Casimir eigenvalue
genus = 7           # genus of D_IV^5
N_max = 137         # channel capacity
dim_R = 2 * n_C     # real dimension of D_IV^5

# Fine structure constant
ALPHA = 1.0 / 137.035999084

# ─── BST magnetic moment formulas ───
MU_P_BST      = Fraction(2 * genus, n_C)          # 14/5 = 2.800
MU_N_BST      = -C_2 / np.pi                      # -6/pi = -1.90986...
MU_P_BST_F    = float(MU_P_BST)                   # 2.800
MU_P_QED      = float(MU_P_BST) - ALPHA           # 2.79270 (one-loop)

# Ratio
MU_RATIO_BST  = -genus * np.pi / (3 * n_C)        # -7*pi/15

# Isovector / isoscalar
MU_V_BST      = (7*np.pi + 15) / (5*np.pi)        # 2.3549
MU_S_BST      = (7*np.pi - 15) / (5*np.pi)        # 0.4451

# Product
MU_PRODUCT_BST = -84.0 / (5*np.pi)                # -5.3477

# Anomalous moments
KAPPA_P_BST   = float(MU_P_BST) - 1.0             # 9/5 = 1.800
KAPPA_N_BST   = MU_N_BST                           # -6/pi (neutron has Q=0)

# ─── Experimental values (CODATA 2018) ───
MU_P_OBS      = 2.7928473446
MU_N_OBS      = -1.91304273
MU_RATIO_OBS  = MU_P_OBS / MU_N_OBS               # -1.45989...
MU_V_OBS      = (MU_P_OBS - MU_N_OBS) / 2.0       # 2.35295
MU_S_OBS      = (MU_P_OBS + MU_N_OBS) / 2.0       # 0.43990
MU_PRODUCT_OBS = MU_P_OBS * MU_N_OBS               # -5.34340

# SU(6) quark model
MU_RATIO_SU6  = -1.5

# Strong coupling at proton mass
ALPHA_S_MP    = Fraction(genus, 4 * n_C)           # 7/20 = 0.350

# Proton spin fraction
DELTA_SIGMA   = Fraction(N_c, 2 * n_C)             # 3/10

# ─── Colors ───
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BRIGHT_GOLD = '#ffee44'
DEEP_BLUE   = '#1133aa'
VOID_PURPLE = '#3311aa'
BLUE_GLOW   = '#4488ff'
PURPLE_GLOW = '#9955dd'
PURPLE_LINE = '#bb77ff'
RED_WARM    = '#ff6644'
WHITE       = '#ffffff'
GREY        = '#888888'
LIGHT_GREY  = '#bbbbbb'
GREEN_GLOW  = '#44dd88'
CYAN        = '#00ddff'
ORANGE      = '#ff8844'
TEAL        = '#22ccaa'
CRIMSON     = '#dd3355'
MAGENTA     = '#dd55cc'


# ═══════════════════════════════════════════════════════════════════
# CI (Companion Intelligence) Interface
# ═══════════════════════════════════════════════════════════════════

class MagneticMoments:
    """
    BST derivation of nucleon magnetic moments from D_IV^5 geometry.

    Usage:
        from toy_magnetic_moments import MagneticMoments
        mm = MagneticMoments()
        mm.two_numbers()
        mm.quark_model()
        mm.bst_correction()
        mm.the_ratio()
        mm.precision_ladder()
        mm.connected_to_everything()
        mm.summary()
        mm.show()
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.N_c = N_c
        self.n_C = n_C
        self.C_2 = C_2
        self.genus = genus
        self.mu_p_bst = MU_P_BST_F
        self.mu_n_bst = MU_N_BST
        self.mu_p_qed = MU_P_QED
        self.mu_p_obs = MU_P_OBS
        self.mu_n_obs = MU_N_OBS
        if not quiet:
            self._print_header()

    def _print_header(self):
        sep = "=" * 72
        print(f"\n{sep}")
        print("  NUCLEON MAGNETIC MOMENTS FROM BST")
        print("  mu_p = 2g/n_C = 14/5 = 2.800 mu_N    (0.26%)")
        print("  mu_n = -C_2/pi = -6/pi = -1.910 mu_N  (0.17%)")
        print(f"{sep}")
        print(f"  Proton: algebraic (genus/dimension).  Neutron: transcendental (Casimir/pi).")
        print(f"  Ratio: mu_p/mu_n = -7*pi/15 = -1.4661.  SU(6): -3/2 = -1.500 (6x worse).")
        print(f"  Zero free parameters.  One geometry.")
        print(f"{sep}\n")

    # ─── Method 1: two_numbers ───
    def two_numbers(self):
        """
        The two most precisely measured nuclear magnetic moments.
        Where do they come from?
        """
        err_p = abs(self.mu_p_bst - MU_P_OBS) / MU_P_OBS * 100
        err_n = abs(self.mu_n_bst - MU_N_OBS) / abs(MU_N_OBS) * 100
        err_p_qed = abs(MU_P_QED - MU_P_OBS) / MU_P_OBS * 100

        result = {
            'mu_p_bst': self.mu_p_bst,
            'mu_p_qed': MU_P_QED,
            'mu_p_obs': MU_P_OBS,
            'mu_n_bst': self.mu_n_bst,
            'mu_n_obs': MU_N_OBS,
            'formula_p': '2g/n_C = 14/5',
            'formula_n': '-C_2/pi = -6/pi',
            'error_p_pct': err_p,
            'error_p_qed_pct': err_p_qed,
            'error_n_pct': err_n,
            'precision_p_obs': '10^-7 (Penning trap)',
            'precision_n_obs': '10^-7 (neutron beam)',
        }
        if not self.quiet:
            print("  TWO NUMBERS")
            print("  " + "-" * 50)
            print(f"  Proton magnetic moment:")
            print(f"    Observed:   mu_p = +{MU_P_OBS:.7f} mu_N")
            print(f"    BST (bare): mu_p = 2g/n_C = 14/5 = {self.mu_p_bst:.3f} mu_N  ({err_p:.2f}%)")
            print(f"    BST (+QED): mu_p = 14/5 - alpha = {MU_P_QED:.5f} mu_N  ({err_p_qed:.3f}%)")
            print()
            print(f"  Neutron magnetic moment:")
            print(f"    Observed:   mu_n = {MU_N_OBS:.7f} mu_N")
            print(f"    BST:        mu_n = -C_2/pi = -6/pi = {self.mu_n_bst:.5f} mu_N  ({err_n:.2f}%)")
            print()
            print(f"  Both measured to 10^-7 precision.  Where do they come from?")
            print(f"  From D_IV^5 geometry: genus g=7, Casimir C_2=6, dimension n_C=5.")
            print()
        return result

    # ─── Method 2: quark_model ───
    def quark_model(self):
        """
        SU(6) quark model prediction and its limitations.
        The Z_3 circuit on CP^2 gives the leading result.
        """
        # SU(6) prediction with equal constituent masses
        # mu_p/mu_n = -(4*e_u - e_d)/(4*e_d - e_u) = -(4*2/3 - (-1/3))/(4*(-1/3) - 2/3)
        #           = -(8/3 + 1/3)/(-4/3 - 2/3) = -(9/3)/(-6/3) = -3/(-2) = -3/2
        su6_ratio = Fraction(-3, 2)
        su6_mu_p = 3.0   # Dirac + anomalous for equal mass quarks
        su6_mu_n = -2.0

        err_su6 = abs(float(su6_ratio) - MU_RATIO_OBS) / abs(MU_RATIO_OBS) * 100

        model = {
            'su6_ratio': float(su6_ratio),
            'su6_mu_p': su6_mu_p,
            'su6_mu_n': su6_mu_n,
            'su6_error_pct': err_su6,
            'assumption': 'Equal constituent quark masses (m_u = m_d = m_q)',
            'z3_circuit': 'Proton as Z_3 circuit on CP^2 subset of D_IV^5',
            'limitation': 'Ignores confinement geometry and u-d mass difference',
            'quark_charges': {'u': Fraction(2, 3), 'd': Fraction(-1, 3)},
        }
        if not self.quiet:
            print("  THE QUARK MODEL (SU(6) SYMMETRY)")
            print("  " + "-" * 50)
            print(f"  Proton = uud:  mu_p = (4*e_u - e_d)/(3*e_u) * mu_q")
            print(f"  Neutron = udd: mu_n = (4*e_d - e_u)/(3*e_u) * mu_q")
            print()
            print(f"  SU(6) with equal masses:")
            print(f"    mu_p/mu_n = -3/2 = -1.500")
            print(f"    Observed:          -1.4599")
            print(f"    Error: {err_su6:.2f}%")
            print()
            print(f"  The assumption of equal quark masses is wrong.")
            print(f"  Quarks are confined -- confinement geometry matters.")
            print()
            print(f"  In BST: the proton is a Z_3 circuit on CP^2 in D_IV^5.")
            print(f"  The three quarks circulate on the fiber; the domain topology")
            print(f"  (genus g=7) and the bulk geometry (n_C=5, C_2=6) determine")
            print(f"  the actual moments.")
            print()
        return model

    # ─── Method 3: bst_correction ───
    def bst_correction(self):
        """
        Full BST calculation: quark model -> D_IV^5 geometry -> QED corrections.
        Each correction brings the prediction closer to experiment.
        """
        # Step-by-step corrections
        steps = []

        # Step 1: Naive quark model (SU(6))
        steps.append({
            'label': 'SU(6) quark model',
            'mu_p': 3.0,
            'mu_n': -2.0,
            'ratio': -1.5,
            'error_p': abs(3.0 - MU_P_OBS) / MU_P_OBS * 100,
            'error_n': abs(-2.0 - MU_N_OBS) / abs(MU_N_OBS) * 100,
            'error_ratio': abs(-1.5 - MU_RATIO_OBS) / abs(MU_RATIO_OBS) * 100,
            'source': 'Equal-mass quarks, SU(6) spin-flavor symmetry',
        })

        # Step 2: BST bare (D_IV^5 geometry)
        steps.append({
            'label': 'BST bare (D_IV^5)',
            'mu_p': MU_P_BST_F,
            'mu_n': MU_N_BST,
            'ratio': MU_RATIO_BST,
            'error_p': abs(MU_P_BST_F - MU_P_OBS) / MU_P_OBS * 100,
            'error_n': abs(MU_N_BST - MU_N_OBS) / abs(MU_N_OBS) * 100,
            'error_ratio': abs(MU_RATIO_BST - MU_RATIO_OBS) / abs(MU_RATIO_OBS) * 100,
            'source': 'mu_p = 2g/n_C, mu_n = -C_2/pi from domain geometry',
        })

        # Step 3: BST + QED correction (proton)
        steps.append({
            'label': 'BST + QED (O(alpha))',
            'mu_p': MU_P_QED,
            'mu_n': MU_N_BST,
            'ratio': MU_P_QED / MU_N_BST,
            'error_p': abs(MU_P_QED - MU_P_OBS) / MU_P_OBS * 100,
            'error_n': abs(MU_N_BST - MU_N_OBS) / abs(MU_N_OBS) * 100,
            'error_ratio': abs(MU_P_QED / MU_N_BST - MU_RATIO_OBS) / abs(MU_RATIO_OBS) * 100,
            'source': 'One-loop photon correction: -alpha to proton vertex',
        })

        result = {
            'steps': steps,
            'formulas': {
                'mu_p': '2g/n_C = 14/5',
                'mu_n': '-C_2/pi = -6/pi',
                'mu_p_qed': '14/5 - alpha',
            },
            'geometry': {
                'g': genus,
                'n_C': n_C,
                'C_2': C_2,
                'proton_source': 'Domain topology (genus)',
                'neutron_source': 'S^1 fiber (circle)',
            },
        }
        if not self.quiet:
            print("  BST CORRECTION: FROM QUARK MODEL TO GEOMETRY")
            print("  " + "-" * 50)
            print(f"  {'Step':<24} {'mu_p':>8} {'err%':>7} {'mu_n':>9} {'err%':>7} {'ratio':>8} {'err%':>7}")
            print(f"  {'-'*24} {'-'*8} {'-'*7} {'-'*9} {'-'*7} {'-'*8} {'-'*7}")
            for s in steps:
                print(f"  {s['label']:<24} {s['mu_p']:>8.4f} {s['error_p']:>6.2f}% "
                      f"{s['mu_n']:>9.5f} {s['error_n']:>6.2f}% "
                      f"{s['ratio']:>8.4f} {s['error_ratio']:>6.2f}%")
            print(f"  {'Observed':<24} {MU_P_OBS:>8.4f} {'---':>7} "
                  f"{MU_N_OBS:>9.5f} {'---':>7} "
                  f"{MU_RATIO_OBS:>8.4f} {'---':>7}")
            print()
            print(f"  Each step brings prediction closer to experiment.")
            print(f"  BST bare: 0.26% (proton), 0.17% (neutron)")
            print(f"  BST+QED:  0.005% (proton) -- 50 ppm precision!")
            print()
        return result

    # ─── Method 4: the_ratio ───
    def the_ratio(self):
        """
        mu_p/mu_n = -7*pi/15 = -1.4661.  Encodes N_c and spin structure.
        """
        ratio_bst = MU_RATIO_BST
        ratio_su6 = -1.5
        ratio_obs = MU_RATIO_OBS

        err_bst = abs(ratio_bst - ratio_obs) / abs(ratio_obs) * 100
        err_su6 = abs(ratio_su6 - ratio_obs) / abs(ratio_obs) * 100
        improvement = err_su6 / err_bst

        # Decomposition: -7*pi/15 = -(g*pi)/(N_c*n_C)
        # Also = -(3/2) * (14*pi/45) = -(3/2) * (1 - 0.0226)
        su6_correction = 14 * np.pi / 45
        fractional_correction = 1.0 - su6_correction

        result = {
            'ratio_bst': ratio_bst,
            'ratio_su6': ratio_su6,
            'ratio_obs': ratio_obs,
            'formula': '-g*pi/(N_c*n_C) = -7*pi/15',
            'error_bst_pct': err_bst,
            'error_su6_pct': err_su6,
            'improvement_factor': improvement,
            'su6_correction_factor': su6_correction,
            'fractional_shift': fractional_correction,
            'decomposition': {
                'numerator': f'g*pi = {genus}*pi = {genus*np.pi:.4f}',
                'denominator': f'N_c*n_C = {N_c}*{n_C} = {N_c*n_C}',
                'encoding': 'N_c in denominator: color degrees of freedom',
            },
        }
        if not self.quiet:
            print("  THE RATIO: mu_p / mu_n")
            print("  " + "-" * 50)
            print(f"  BST:      -7*pi/15 = -g*pi/(N_c*n_C) = {ratio_bst:.4f}")
            print(f"  SU(6):    -3/2                        = {ratio_su6:.4f}")
            print(f"  Observed:                              = {ratio_obs:.4f}")
            print()
            print(f"  BST error: {err_bst:.2f}%")
            print(f"  SU(6) error: {err_su6:.2f}%")
            print(f"  BST is {improvement:.1f}x more accurate than SU(6)")
            print()
            print(f"  The ratio encodes:")
            print(f"    g = {genus} (genus of D_IV^5) -- topology of the domain")
            print(f"    pi from S^1 fiber -- circular current loop")
            print(f"    N_c = {N_c} (color charges) -- confinement structure")
            print(f"    n_C = {n_C} (complex dimension) -- geometric inertia")
            print()
            print(f"  BST correction to SU(6): -3/2 * {su6_correction:.4f} = -3/2 * (1 - {-fractional_correction:.4f})")
            print(f"  The {-fractional_correction*100:.2f}% reduction comes from D_IV^5 geometry.")
            print()
        return result

    # ─── Method 5: precision_ladder ───
    def precision_ladder(self):
        """
        From naive quark model to BST: each step gets closer.
        Show residuals shrinking.
        """
        ladder = [
            {
                'model': 'Dirac (point particle)',
                'mu_p': 1.0,
                'mu_n': 0.0,
                'note': 'Dirac equation: mu = Q * mu_N. Misses anomalous moment entirely.',
            },
            {
                'model': 'SU(6) quark model',
                'mu_p': 3.0,
                'mu_n': -2.0,
                'note': 'Equal mass quarks. Gets sign and order of magnitude.',
            },
            {
                'model': 'BST bare',
                'mu_p': MU_P_BST_F,
                'mu_n': MU_N_BST,
                'note': 'mu_p = 2g/n_C, mu_n = -C_2/pi. Zero parameters.',
            },
            {
                'model': 'BST + QED',
                'mu_p': MU_P_QED,
                'mu_n': MU_N_BST,
                'note': 'One-loop correction: -alpha on proton vertex.',
            },
        ]

        for step in ladder:
            step['residual_p'] = step['mu_p'] - MU_P_OBS
            step['residual_n'] = step['mu_n'] - MU_N_OBS
            step['pct_p'] = abs(step['residual_p']) / MU_P_OBS * 100
            step['pct_n'] = abs(step['residual_n']) / abs(MU_N_OBS) * 100

        result = {
            'ladder': ladder,
            'observed': {'mu_p': MU_P_OBS, 'mu_n': MU_N_OBS},
            'best_proton': 'BST+QED at 0.005% (50 ppm)',
            'best_neutron': 'BST bare at 0.17%',
        }
        if not self.quiet:
            print("  PRECISION LADDER")
            print("  " + "-" * 50)
            print(f"  {'Model':<22} {'mu_p':>8} {'res_p':>9} {'pct':>7}  {'mu_n':>9} {'res_n':>9} {'pct':>7}")
            print(f"  {'-'*22} {'-'*8} {'-'*9} {'-'*7}  {'-'*9} {'-'*9} {'-'*7}")
            for s in ladder:
                print(f"  {s['model']:<22} {s['mu_p']:>8.4f} {s['residual_p']:>+9.5f} "
                      f"{s['pct_p']:>6.3f}%  {s['mu_n']:>9.5f} {s['residual_n']:>+9.5f} "
                      f"{s['pct_n']:>6.3f}%")
            print(f"  {'Observed':<22} {MU_P_OBS:>8.4f} {'':>9} {'':>7}  {MU_N_OBS:>9.5f}")
            print()
            for s in ladder:
                print(f"  * {s['model']}: {s['note']}")
            print()
        return result

    # ─── Method 6: connected_to_everything ───
    def connected_to_everything(self):
        """
        The same geometry that gives magnetic moments gives the spin crisis,
        the mass gap, the Reality Budget, and the strong coupling.
        """
        kappa_p = float(MU_P_BST) - 1.0  # 9/5
        reality_budget = float(Fraction(N_c**2, n_C))  # 9/5
        alpha_s_mp = float(ALPHA_S_MP)    # 7/20
        mu_p_from_alpha_s = (N_c**2 - 1) * alpha_s_mp  # 8 * 7/20 = 14/5

        connections = {
            'anomalous_moment': {
                'value': kappa_p,
                'fraction': '9/5',
                'formula': 'kappa_p = mu_p - 1 = 14/5 - 1 = 9/5',
                'equals': 'Reality Budget: Lambda * N_total = N_c^2/n_C = 9/5',
            },
            'strong_coupling': {
                'alpha_s': alpha_s_mp,
                'fraction': '7/20',
                'mu_p_identity': f'mu_p = (N_c^2 - 1)*alpha_s = 8 * 7/20 = {mu_p_from_alpha_s}',
                'meaning': 'Proton moment = gluon count * coupling strength',
            },
            'proton_spin': {
                'delta_sigma': float(DELTA_SIGMA),
                'fraction': '3/10',
                'connection': 'Same D_IV^5 geometry: 3 color dims / 10 total dims',
            },
            'mass_gap': {
                'formula': 'm_p = C_2 * pi^n_C * m_e = 6*pi^5 * m_e',
                'C_2_appears_in': 'mu_n = -C_2/pi (same Casimir)',
            },
            'genus_dimension': {
                'identity': 'g = n_C + 2 (algebraic geometry theorem)',
                'consequence': 'mu_p = 2g/n_C = 2(n_C+2)/n_C = 2 + 4/n_C',
                'universal': 'True for all D_IV^n domains; BST selects n_C=5',
            },
        }
        if not self.quiet:
            print("  CONNECTED TO EVERYTHING")
            print("  " + "-" * 50)
            print()
            print(f"  1. ANOMALOUS MOMENT = REALITY BUDGET")
            print(f"     kappa_p = mu_p - 1 = 14/5 - 1 = 9/5 = {kappa_p:.3f}")
            print(f"     Lambda * N_total = N_c^2/n_C = 9/5  (same number!)")
            print()
            print(f"  2. PROTON MOMENT = 8 * STRONG COUPLING")
            print(f"     mu_p = (N_c^2-1)*alpha_s(m_p) = 8 * 7/20 = 14/5")
            print(f"     8 = dim SU(3) = number of gluon species")
            print(f"     Magnetic response = gluon_count * coupling_strength")
            print()
            print(f"  3. PROTON SPIN CRISIS RESOLVED")
            print(f"     DeltaSigma = N_c/(2*n_C) = 3/10 = 0.300")
            print(f"     Same D_IV^5 geometry, same integers")
            print()
            print(f"  4. MASS GAP USES SAME CASIMIR")
            print(f"     m_p = C_2*pi^n_C*m_e = 6*pi^5*m_e = 938.272 MeV")
            print(f"     mu_n = -C_2/pi = -6/pi (same C_2 = 6)")
            print()
            print(f"  5. GENUS-DIMENSION IDENTITY")
            print(f"     g = n_C + 2 (theorem of bounded symmetric domains)")
            print(f"     mu_p = 2g/n_C converts algebraic geometry -> nuclear physics")
            print()
        return connections

    # ─── Method 7: isospin_decomposition ───
    def isospin_decomposition(self):
        """
        Isovector and isoscalar moments from BST.
        mu_V = (7*pi + 15)/(5*pi) matches to 0.08%.
        """
        result = {
            'mu_V_bst': MU_V_BST,
            'mu_V_obs': MU_V_OBS,
            'mu_V_formula': '(7*pi + 15)/(5*pi) = g/n_C + N_c/pi',
            'mu_V_error': abs(MU_V_BST - MU_V_OBS) / MU_V_OBS * 100,
            'mu_S_bst': MU_S_BST,
            'mu_S_obs': MU_S_OBS,
            'mu_S_formula': '(7*pi - 15)/(5*pi) = g/n_C - N_c/pi',
            'mu_S_error': abs(MU_S_BST - MU_S_OBS) / abs(MU_S_OBS) * 100,
            'product_bst': MU_PRODUCT_BST,
            'product_obs': MU_PRODUCT_OBS,
            'product_formula': '-84/(5*pi) = -2*g*C_2/(n_C*pi)',
            'product_error': abs(MU_PRODUCT_BST - MU_PRODUCT_OBS) / abs(MU_PRODUCT_OBS) * 100,
        }
        if not self.quiet:
            print("  ISOSPIN DECOMPOSITION")
            print("  " + "-" * 50)
            print(f"  Isovector:  mu_V = (mu_p - mu_n)/2 = (7*pi + 15)/(5*pi)")
            print(f"    BST:  {MU_V_BST:.4f}    Observed: {MU_V_OBS:.4f}    Error: {result['mu_V_error']:.2f}%")
            print()
            print(f"  Isoscalar:  mu_S = (mu_p + mu_n)/2 = (7*pi - 15)/(5*pi)")
            print(f"    BST:  {MU_S_BST:.4f}    Observed: {MU_S_OBS:.4f}    Error: {result['mu_S_error']:.1f}%")
            print()
            print(f"  Product:    mu_p * mu_n = -84/(5*pi)")
            print(f"    BST: {MU_PRODUCT_BST:.4f}    Observed: {MU_PRODUCT_OBS:.4f}    Error: {result['product_error']:.2f}%")
            print()
            print(f"  mu_V matches to 0.08% -- one of the most precise BST nuclear predictions.")
            print(f"  84 = 2*g*C_2 = 2*7*6.  Note 84 = C_2(pi_12), the k=12 Casimir.")
            print()
        return result

    # ─── Method 8: summary ───
    def summary(self):
        """
        Key results: proton algebraic, neutron transcendental, ratio 6x better than SU(6).
        """
        s = {
            'title': 'Nucleon Magnetic Moments from D_IV^5',
            'key_formulas': {
                'mu_p': '2g/n_C = 14/5 = 2.800 mu_N (0.26%)',
                'mu_n': '-C_2/pi = -6/pi = -1.910 mu_N (0.17%)',
                'ratio': '-7*pi/15 = -1.466 (0.43%)',
                'mu_p_qed': '14/5 - alpha = 2.79270 mu_N (0.005%)',
            },
            'key_identities': [
                'mu_p = (N_c^2 - 1) * alpha_s = 8 * 7/20 = 14/5',
                'kappa_p = mu_p - 1 = 9/5 = Reality Budget',
                'g = n_C + 2 (bounded symmetric domain theorem)',
            ],
            'character': {
                'proton': 'Algebraic (rational number: 14/5)',
                'neutron': 'Transcendental (involves pi: -6/pi)',
            },
            'parameters': 0,
            'vs_su6': '6x more accurate on the ratio',
        }
        if not self.quiet:
            sep = "=" * 72
            print(f"\n{sep}")
            print("  SUMMARY: NUCLEON MAGNETIC MOMENTS FROM D_IV^5")
            print(f"{sep}")
            print()
            print(f"  mu_p = 2g/n_C = 14/5 = 2.800 mu_N      (observed: 2.79285, 0.26%)")
            print(f"  mu_n = -C_2/pi = -6/pi = -1.910 mu_N    (observed: -1.91304, 0.17%)")
            print(f"  mu_p/mu_n = -7*pi/15 = -1.4661           (observed: -1.4599, 0.43%)")
            print()
            print(f"  With QED correction:")
            print(f"  mu_p = 14/5 - alpha = 2.79270 mu_N       (0.005% = 50 ppm)")
            print()
            print(f"  Key identities:")
            print(f"    mu_p = (N_c^2-1)*alpha_s = 8 * 7/20  (gluons * coupling)")
            print(f"    kappa_p = 9/5 = Reality Budget")
            print(f"    g = n_C + 2  (domain classification theorem)")
            print()
            print(f"  Proton is algebraic (genus/dimension).")
            print(f"  Neutron is transcendental (Casimir/pi).")
            print(f"  SU(6) gives -3/2 (2.7% error).  BST gives -7*pi/15 (0.43%): 6x better.")
            print(f"  Zero free parameters.  One geometry.")
            print(f"\n{sep}\n")
        return s

    # ─── Method 9: show ───
    def show(self):
        """
        6-panel visualization:
          Panel 1: Two Numbers -- mu_p and mu_n displayed prominently
          Panel 2: The Quark Model -- SU(6) and Z_3 circuit on CP^2
          Panel 3: BST Correction -- step-by-step convergence
          Panel 4: The Ratio -- mu_p/mu_n comparison
          Panel 5: Precision Ladder -- residuals shrinking
          Panel 6: Connected to Everything -- one geometry, many predictions
        """
        fig = plt.figure(figsize=(20, 13), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'BST Toy 119 -- Nucleon Magnetic Moments from D_IV^5 Geometry')

        # ── Title ──
        fig.text(0.50, 0.975,
                 'NUCLEON MAGNETIC MOMENTS FROM BST',
                 ha='center', va='top', color=GOLD, fontsize=24, weight='bold',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=4, foreground=GOLD_DIM, alpha=0.4)])
        fig.text(0.50, 0.945,
                 r'$\mu_p = 2g/n_C = 14/5$     '
                 r'$\mu_n = -C_2/\pi = -6/\pi$     '
                 'Zero parameters.  One geometry.',
                 ha='center', va='top', color=LIGHT_GREY, fontsize=11,
                 fontfamily='monospace')

        gs = GridSpec(2, 3, figure=fig,
                      hspace=0.25, wspace=0.20,
                      left=0.05, right=0.97, top=0.91, bottom=0.05)

        # ════════════════════════════════════════════════════════════════
        # PANEL 1: TWO NUMBERS
        # ════════════════════════════════════════════════════════════════
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.set_facecolor(BG)
        ax1.set_xlim(-1.2, 1.2)
        ax1.set_ylim(-1.5, 1.5)
        ax1.set_aspect('equal')
        ax1.axis('off')

        _glow(ax1, 0, 1.35, 'Two Numbers', GOLD, 14, weight='bold')
        _glow(ax1, 0, 1.05,
              'Measured to 10$^{-7}$ precision', GREY, 9)

        # Proton moment -- large display
        _glow(ax1, 0, 0.55,
              r'$\mu_p = +2.7928473\;\mu_N$',
              CYAN, 15, weight='bold')
        _glow(ax1, 0, 0.20,
              r'BST: $\;2g/n_C = 14/5 = 2.800$',
              TEAL, 11)
        _glow(ax1, 0, -0.05,
              r'with QED: $\;14/5 - \alpha = 2.79270$  (50 ppm)',
              GREEN_GLOW, 9)

        # Separator
        ax1.plot([-0.9, 0.9], [-0.30, -0.30], color=GREY, linewidth=0.5, alpha=0.4)

        # Neutron moment
        _glow(ax1, 0, -0.60,
              r'$\mu_n = -1.9130427\;\mu_N$',
              ORANGE, 15, weight='bold')
        _glow(ax1, 0, -0.95,
              r'BST: $\;-C_2/\pi = -6/\pi = -1.90986$',
              RED_WARM, 11)
        _glow(ax1, 0, -1.20,
              '0.17% accuracy',
              RED_WARM, 9)

        _glow(ax1, 0, -1.45,
              'Where do they come from?', WHITE, 10, weight='bold')

        # ════════════════════════════════════════════════════════════════
        # PANEL 2: THE QUARK MODEL
        # ════════════════════════════════════════════════════════════════
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.set_facecolor(BG)
        ax2.set_xlim(-1.6, 1.6)
        ax2.set_ylim(-1.6, 1.6)
        ax2.set_aspect('equal')
        ax2.axis('off')

        _glow(ax2, 0, 1.45, 'The Quark Model', GOLD, 14, weight='bold')

        # Draw Z_3 circuit: three quarks on a triangle
        angles_q = [np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3]
        r_tri = 0.70
        colors_q = ['#ff4444', '#44cc44', '#4488ff']
        labels_q = ['u', 'u', 'd']
        charges_q = ['+2/3', '+2/3', '-1/3']

        # Z_3 circuit -- wavy gluon lines between quarks
        for i in range(3):
            j = (i + 1) % 3
            x1c = r_tri * np.cos(angles_q[i])
            y1c = r_tri * np.sin(angles_q[i])
            x2c = r_tri * np.cos(angles_q[j])
            y2c = r_tri * np.sin(angles_q[j])
            t_vals = np.linspace(0, 1, 80)
            xline = x1c + (x2c - x1c) * t_vals
            yline = y1c + (y2c - y1c) * t_vals
            dx = x2c - x1c
            dy = y2c - y1c
            length = np.sqrt(dx**2 + dy**2)
            nx, ny = -dy/length, dx/length
            wave = 0.05 * np.sin(10 * np.pi * t_vals)
            xline += nx * wave
            yline += ny * wave
            ax2.plot(xline, yline, color=PURPLE_GLOW, alpha=0.4, linewidth=1.5)

        # Z_3 arrows (directed circuit)
        for i in range(3):
            j = (i + 1) % 3
            x1c = r_tri * np.cos(angles_q[i])
            y1c = r_tri * np.sin(angles_q[i])
            x2c = r_tri * np.cos(angles_q[j])
            y2c = r_tri * np.sin(angles_q[j])
            mx = 0.5*(x1c + x2c)
            my = 0.5*(y1c + y2c)
            dx = (x2c - x1c) * 0.12
            dy = (y2c - y1c) * 0.12
            ax2.annotate('', xy=(mx + dx, my + dy), xytext=(mx - dx, my - dy),
                         arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5, alpha=0.5))

        # Draw quark circles
        for i, (ang, col, lab, chg) in enumerate(zip(angles_q, colors_q, labels_q, charges_q)):
            qx = r_tri * np.cos(ang)
            qy = r_tri * np.sin(ang)
            circ = Circle((qx, qy), 0.18, facecolor=col, edgecolor=WHITE,
                          linewidth=1.5, alpha=0.85)
            ax2.add_patch(circ)
            _glow(ax2, qx, qy, lab, WHITE, 12, weight='bold')
            label_r = r_tri + 0.38
            _glow(ax2, label_r * np.cos(ang), label_r * np.sin(ang),
                  f'e={chg}', col, 8)

        # CP^2 label
        _glow(ax2, 0, -0.05, r'$Z_3$ on $CP^2$', CYAN, 10, weight='bold')

        # SU(6) result
        _glow(ax2, 0, -0.50,
              r'SU(6): $\mu_p/\mu_n = -3/2 = -1.500$',
              LIGHT_GREY, 10)
        _glow(ax2, 0, -0.78,
              'Equal quark masses assumed', GREY, 9)
        _glow(ax2, 0, -1.02,
              'Error: 2.74% -- confinement matters!', RED_WARM, 9)

        # BST improvement
        _glow(ax2, 0, -1.35,
              r'BST: $-7\pi/15 = -1.466$ (0.43%)',
              GREEN_GLOW, 10, weight='bold')

        # ════════════════════════════════════════════════════════════════
        # PANEL 3: BST CORRECTION
        # ════════════════════════════════════════════════════════════════
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.set_facecolor(BG)
        ax3.set_xlim(-0.2, 1.2)
        ax3.set_ylim(-0.5, 4.5)
        ax3.axis('off')

        _glow(ax3, 0.5, 4.3, 'BST Correction', GOLD, 14, weight='bold')
        _glow(ax3, 0.5, 3.95,
              'Each step closer to experiment', GREY, 9)

        # Vertical bars showing proton moment predictions
        steps_p = [
            ('SU(6)',     3.000,  RED_WARM),
            ('BST bare',  MU_P_BST_F,  CYAN),
            ('BST+QED',   MU_P_QED,   GREEN_GLOW),
        ]

        # Scale: map mu values to x positions
        mu_min, mu_max = 2.75, 3.05
        def mu_to_x(mu):
            return (mu - mu_min) / (mu_max - mu_min)

        y_positions = [3.3, 2.4, 1.5]

        # Observed line
        obs_x = mu_to_x(MU_P_OBS)
        ax3.plot([obs_x, obs_x], [0.7, 3.7], color=GOLD, linewidth=2,
                 linestyle='--', alpha=0.6)
        _glow(ax3, obs_x, 0.45, f'Observed\n{MU_P_OBS:.4f}', GOLD, 8)

        for (label, mu_val, col), yp in zip(steps_p, y_positions):
            xp = mu_to_x(mu_val)
            err = abs(mu_val - MU_P_OBS) / MU_P_OBS * 100
            # Bar from observed to prediction
            ax3.plot([obs_x, xp], [yp, yp], color=col, linewidth=3, alpha=0.7)
            # Point
            ax3.plot(xp, yp, 'o', color=col, markersize=10, alpha=0.9,
                     markeredgecolor=WHITE, markeredgewidth=0.5)
            # Label
            _glow(ax3, -0.15, yp, label, col, 10, ha='left', weight='bold')
            _glow(ax3, xp + 0.03, yp + 0.25,
                  f'{mu_val:.4f}', col, 8, ha='left')
            _glow(ax3, xp + 0.03, yp - 0.25,
                  f'{err:.3f}%', col, 8, ha='left')

        # Scale ticks
        for mu_tick in [2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05]:
            tx = mu_to_x(mu_tick)
            ax3.plot([tx, tx], [0.62, 0.68], color=GREY, linewidth=0.8, alpha=0.5)
            _glow(ax3, tx, 0.50, f'{mu_tick:.2f}', GREY, 7)

        _glow(ax3, 0.5, 0.12, r'$\mu_p\;(\mu_N)$', LIGHT_GREY, 10)

        # ════════════════════════════════════════════════════════════════
        # PANEL 4: THE RATIO
        # ════════════════════════════════════════════════════════════════
        ax4 = fig.add_subplot(gs[1, 0])
        ax4.set_facecolor(BG)
        ax4.set_xlim(-1.2, 1.2)
        ax4.set_ylim(-1.5, 1.5)
        ax4.set_aspect('equal')
        ax4.axis('off')

        _glow(ax4, 0, 1.35, 'The Ratio', GOLD, 14, weight='bold')

        # Display the three ratios
        _glow(ax4, 0, 0.85,
              r'$\mu_p / \mu_n$', WHITE, 16, weight='bold')

        # Observed
        _glow(ax4, -0.65, 0.35, 'Observed:', GREY, 10, ha='left')
        _glow(ax4, 0.55, 0.35,
              f'{MU_RATIO_OBS:.4f}', BRIGHT_GOLD, 14, weight='bold', ha='left')

        # BST
        _glow(ax4, -0.65, -0.05, 'BST:', GREY, 10, ha='left')
        _glow(ax4, 0.55, -0.05,
              r'$-7\pi/15 = $' + f'{MU_RATIO_BST:.4f}', CYAN, 12, weight='bold', ha='left')
        _glow(ax4, 0.55, -0.30,
              f'Error: {abs(MU_RATIO_BST - MU_RATIO_OBS)/abs(MU_RATIO_OBS)*100:.2f}%',
              CYAN, 9, ha='left')

        # SU(6)
        _glow(ax4, -0.65, -0.55, 'SU(6):', GREY, 10, ha='left')
        _glow(ax4, 0.55, -0.55,
              r'$-3/2 = -1.5000$', RED_WARM, 12, ha='left')
        _glow(ax4, 0.55, -0.80,
              f'Error: {abs(-1.5 - MU_RATIO_OBS)/abs(MU_RATIO_OBS)*100:.2f}%',
              RED_WARM, 9, ha='left')

        # Improvement
        improvement = (abs(-1.5 - MU_RATIO_OBS) / abs(MU_RATIO_BST - MU_RATIO_OBS))
        _glow(ax4, 0, -1.15,
              f'BST is {improvement:.0f}x more accurate',
              GREEN_GLOW, 12, weight='bold')

        _glow(ax4, 0, -1.42,
              r'Encodes $g=7$, $\pi$ (fiber), $N_c=3$, $n_C=5$',
              GREY, 8)

        # ════════════════════════════════════════════════════════════════
        # PANEL 5: PRECISION LADDER
        # ════════════════════════════════════════════════════════════════
        ax5 = fig.add_subplot(gs[1, 1])
        ax5.set_facecolor(BG)
        ax5.set_xlim(-0.3, 1.3)
        ax5.set_ylim(-0.8, 4.5)
        ax5.axis('off')

        _glow(ax5, 0.5, 4.3, 'Precision Ladder', GOLD, 14, weight='bold')
        _glow(ax5, 0.5, 3.95, 'Residuals shrinking toward zero', GREY, 9)

        # Ladder entries: model, residual_p, residual_n, color
        ladder_data = [
            ('Dirac',     1.0 - MU_P_OBS,  0.0 - MU_N_OBS,    GREY),
            ('SU(6)',     3.0 - MU_P_OBS,  -2.0 - MU_N_OBS,   RED_WARM),
            ('BST bare',  MU_P_BST_F - MU_P_OBS, MU_N_BST - MU_N_OBS, CYAN),
            ('BST+QED',   MU_P_QED - MU_P_OBS, MU_N_BST - MU_N_OBS, GREEN_GLOW),
        ]

        y_ladder = [3.3, 2.6, 1.9, 1.2]

        # Logarithmic residual bars
        for (label, res_p, res_n, col), yp in zip(ladder_data, y_ladder):
            # Proton residual
            log_res_p = np.log10(max(abs(res_p), 1e-6))
            # Map log residual to bar length: -5 -> 0, 1 -> 1.0
            bar_p = max(0.02, (log_res_p + 5) / 6.0)
            ax5.barh(yp + 0.12, bar_p, height=0.15, left=0.30,
                     color=col, alpha=0.7, edgecolor=WHITE, linewidth=0.5)
            # Neutron residual
            log_res_n = np.log10(max(abs(res_n), 1e-6))
            bar_n = max(0.02, (log_res_n + 5) / 6.0)
            ax5.barh(yp - 0.12, bar_n, height=0.15, left=0.30,
                     color=ORANGE, alpha=0.5, edgecolor=WHITE, linewidth=0.5)

            # Labels
            _glow(ax5, 0.0, yp, label, col, 10, ha='left', weight='bold')
            pct_p = abs(res_p) / MU_P_OBS * 100
            pct_n = abs(res_n) / abs(MU_N_OBS) * 100
            _glow(ax5, 0.32 + bar_p + 0.03, yp + 0.12,
                  f'p: {pct_p:.3f}%', col, 7, ha='left')
            _glow(ax5, 0.32 + bar_n + 0.03, yp - 0.12,
                  f'n: {pct_n:.3f}%', ORANGE, 7, ha='left')

        # Legend
        _glow(ax5, 0.5, 0.55,
              'Shorter bar = closer to experiment', GREY, 8)
        _glow(ax5, 0.5, 0.25,
              'Best: BST+QED proton at 50 ppm (0.005%)', GREEN_GLOW, 9)
        _glow(ax5, 0.5, -0.05,
              'Best: BST neutron at 0.17%', ORANGE, 9)

        # ════════════════════════════════════════════════════════════════
        # PANEL 6: CONNECTED TO EVERYTHING
        # ════════════════════════════════════════════════════════════════
        ax6 = fig.add_subplot(gs[1, 2])
        ax6.set_facecolor(BG)
        ax6.set_xlim(-1.5, 1.5)
        ax6.set_ylim(-1.6, 1.6)
        ax6.set_aspect('equal')
        ax6.axis('off')

        _glow(ax6, 0, 1.45, 'Connected to Everything', GOLD, 14, weight='bold')

        # Central hub: D_IV^5
        hub = Circle((0, 0), 0.35, facecolor=VOID_PURPLE, edgecolor=GOLD,
                      linewidth=2, alpha=0.8)
        ax6.add_patch(hub)
        _glow(ax6, 0, 0.05, r'$D_{IV}^5$', GOLD, 12, weight='bold')
        _glow(ax6, 0, -0.15, 'One', WHITE, 8)
        _glow(ax6, 0, -0.28, 'geometry', WHITE, 8)

        # Spokes to related quantities
        connections = [
            (0.85,   90, r'$\mu_p = 14/5$',          CYAN,       'Proton moment'),
            (0.85,  162, r'$\mu_n = -6/\pi$',         ORANGE,     'Neutron moment'),
            (0.85,  234, r'$\Delta\Sigma = 3/10$',    GREEN_GLOW, 'Spin crisis'),
            (0.85,  306, r'$\kappa_p = 9/5$',         MAGENTA,    'Reality Budget'),
            (0.85,   18, r'$\alpha_s = 7/20$',        BLUE_GLOW,  'Strong coupling'),
        ]

        for r_conn, angle_deg, formula, col, desc in connections:
            angle_rad = np.radians(angle_deg)
            xc = r_conn * np.cos(angle_rad)
            yc = r_conn * np.sin(angle_rad)

            # Spoke line
            x0 = 0.38 * np.cos(angle_rad)
            y0 = 0.38 * np.sin(angle_rad)
            ax6.plot([x0, xc], [y0, yc], color=col, linewidth=1.5, alpha=0.5)

            # Node
            node = Circle((xc, yc), 0.08, facecolor=col, edgecolor=WHITE,
                           linewidth=0.8, alpha=0.7)
            ax6.add_patch(node)

            # Labels (positioned outside the node)
            label_r = r_conn + 0.28
            lx = label_r * np.cos(angle_rad)
            ly = label_r * np.sin(angle_rad)
            _glow(ax6, lx, ly, formula, col, 9, weight='bold')

            desc_r = r_conn + 0.50
            dx = desc_r * np.cos(angle_rad)
            dy = desc_r * np.sin(angle_rad)
            _glow(ax6, dx, dy, desc, GREY, 7)

        _glow(ax6, 0, -1.45,
              r'Same $g=7$, $C_2=6$, $n_C=5$ everywhere',
              LIGHT_GREY, 9)

        # ── Copyright ──
        fig.text(0.99, 0.005,
                 'Copyright 2026 Casey Koons | Claude Opus 4.6',
                 ha='right', va='bottom', color=GREY, fontsize=7,
                 fontfamily='monospace', alpha=0.5)

        plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.93])
        plt.show()
        return fig

    def __repr__(self):
        return (
            f"MagneticMoments(\n"
            f"  mu_p = 2g/n_C = 14/5 = {self.mu_p_bst:.3f} mu_N  (obs: {MU_P_OBS:.5f})\n"
            f"  mu_n = -C_2/pi = -6/pi = {self.mu_n_bst:.5f} mu_N  (obs: {MU_N_OBS:.5f})\n"
            f"  ratio = -7*pi/15 = {MU_RATIO_BST:.4f}  (obs: {MU_RATIO_OBS:.4f})\n"
            f"  Proton: algebraic.  Neutron: transcendental.\n"
            f"  Zero free parameters.\n"
            f")"
        )


# ─── Helper ───
def _glow(ax, x, y, text, color=WHITE, fontsize=12, ha='center', va='center',
          weight='normal', alpha=1.0, glow_color=None, glow_width=3,
          transform=None, **kwargs):
    """Place text with a soft glow effect."""
    gc = glow_color or color
    kw = dict(color=color, fontsize=fontsize, ha=ha, va=va,
              weight=weight, alpha=alpha, **kwargs)
    if transform is not None:
        kw['transform'] = transform
    t = ax.text(x, y, text, **kw)
    t.set_path_effects([
        pe.withStroke(linewidth=glow_width, foreground=gc, alpha=0.3),
        pe.Normal()
    ])
    return t


# ═══════════════════════════════════════════════════════════════════
# Print Report
# ═══════════════════════════════════════════════════════════════════

def print_report():
    """Print a full summary of nucleon magnetic moments from BST."""
    mm = MagneticMoments(quiet=True)
    sep = "=" * 72
    print(f"\n{sep}")
    print("  TOY 119 -- NUCLEON MAGNETIC MOMENTS FROM BST")
    print(f"  mu_p = 2g/n_C = 14/5     mu_n = -C_2/pi = -6/pi")
    print(f"{sep}\n")

    mm.quiet = False
    mm.two_numbers()
    mm.quark_model()
    mm.bst_correction()
    mm.the_ratio()
    mm.precision_ladder()
    mm.connected_to_everything()
    mm.isospin_decomposition()
    mm.summary()


# ═══════════════════════════════════════════════════════════════════
# Interactive Menu
# ═══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the magnetic moments toy."""
    mm = MagneticMoments(quiet=False)

    menu = """
  +-------------------------------------------------+
  |  NUCLEON MAGNETIC MOMENTS -- Interactive Menu    |
  +-------------------------------------------------+
  |  1. Two numbers (mu_p and mu_n)                 |
  |  2. The quark model (SU(6) and Z_3)            |
  |  3. BST correction (step-by-step)              |
  |  4. The ratio (mu_p/mu_n)                       |
  |  5. Precision ladder (residuals)                |
  |  6. Connected to everything                     |
  |  7. Isospin decomposition                       |
  |  8. Summary                                     |
  |  9. Show visualization (6-panel)                |
  |  0. Full report (all methods)                   |
  |  q. Quit                                        |
  +-------------------------------------------------+
"""
    while True:
        print(menu)
        choice = input("  Select [0-9, q]: ").strip().lower()
        if choice == 'q':
            print("  Goodbye.\n")
            break
        elif choice == '1':
            mm.two_numbers()
        elif choice == '2':
            mm.quark_model()
        elif choice == '3':
            mm.bst_correction()
        elif choice == '4':
            mm.the_ratio()
        elif choice == '5':
            mm.precision_ladder()
        elif choice == '6':
            mm.connected_to_everything()
        elif choice == '7':
            mm.isospin_decomposition()
        elif choice == '8':
            mm.summary()
        elif choice == '9':
            mm.show()
        elif choice == '0':
            print_report()
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
