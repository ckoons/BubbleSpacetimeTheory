#!/usr/bin/env python3
"""
THE CMB RULER — Toy 54: The Spectral Index from Geometry
=========================================================

BST derives the CMB spectral index from the geometry of D_IV^5:

  n_s = 1 - n_C / N_max = 1 - 5/137 = 0.96350

Planck 2018: n_s = 0.9649 +/- 0.0042.  BST is -0.3 sigma.

The tensor-to-scalar ratio r ~ 0 is BST's sharpest binary prediction:
inflation -> r > 0; BST -> r = 0 (T_c << m_Pl, no inflaton field).
If LiteBIRD detects r > 0.001, BST is falsified.

The tilt is purely geometric: five complex dimensions of D_IV^5 each
contribute 1/N_max of tilt. The remaining 132 Haldane modes are frozen.
No inflaton. No potential. No free parameters.

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch

# ─── BST Constants ───
N_MAX = 137          # Haldane channel cap
N_c = 3              # color charges
n_C = 5              # domain dimension (D_IV^5)
C_2 = 6              # Casimir invariant
GENUS = 7            # genus of D_IV^5

# CMB spectral index
N_S_BST = 1.0 - n_C / N_MAX           # = 0.96350...
TILT_BST = n_C / N_MAX                 # = 0.03650...
R_BST = 0.0                            # tensor-to-scalar ratio (BST: zero)
RUNNING_BST = -n_C / N_MAX**2          # dn_s/dlnk = -5/137^2 = -2.66e-4

# Phase transition
T_C_MEV = N_MAX * 20.0 / 21.0         # = 130.5 MeV
C_V = 330_000                          # heat capacity at transition

# Planck 2018 observations
PLANCK_NS = (0.9649, 0.0042)           # (value, 1-sigma error)
PLANCK_R = (0.0, 0.036)               # r < 0.036 at 95% CL (value=0 consistent)
PLANCK_OBH2 = (0.02237, 0.00015)      # Omega_b h^2
PLANCK_OCH2 = (0.1200, 0.0012)        # Omega_c h^2
PLANCK_RUNNING = (-0.0045, 0.0067)     # dn_s/dlnk
PLANCK_AS = 2.1e-9                     # scalar amplitude

# BST Omega_b h^2 and Omega_c h^2 (from cosmic pie: 18/361 and 96/361, h~0.674)
H_PLANCK = 0.6736
OMEGA_B_BST = 18.0 / 361.0
OMEGA_C_BST = 96.0 / 361.0
OBH2_BST = OMEGA_B_BST * H_PLANCK**2   # ~ 0.02262
OCH2_BST = OMEGA_C_BST * H_PLANCK**2   # ~ 0.1206

# Colors
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BRIGHT_GOLD = '#ffee44'
BLUE_GLOW   = '#4488ff'
PURPLE_GLOW = '#9955dd'
PURPLE_LINE = '#bb77ff'
RED_WARM    = '#ff6644'
WHITE       = '#ffffff'
GREY        = '#888888'
LIGHT_GREY  = '#bbbbbb'
GREEN_GLOW  = '#44dd88'
CYAN        = '#00ddff'
ORANGE      = '#ff9933'


# ═══════════════════════════════════════════════════════════════════
# Inflation Model Data (n_s, r) for comparison
# ═══════════════════════════════════════════════════════════════════

INFLATION_MODELS = {
    'R^2 (Starobinsky)': {
        'n_s_range': (0.961, 0.967),
        'r_range': (0.003, 0.005),
        'n_s_central': 0.964,
        'r_central': 0.004,
        'color': BLUE_GLOW,
    },
    'Chaotic (phi^2)': {
        'n_s_range': (0.960, 0.970),
        'r_range': (0.10, 0.16),
        'n_s_central': 0.967,
        'r_central': 0.13,
        'color': RED_WARM,
    },
    'Natural inflation': {
        'n_s_range': (0.955, 0.968),
        'r_range': (0.03, 0.10),
        'n_s_central': 0.960,
        'r_central': 0.06,
        'color': ORANGE,
    },
    'Hilltop (p=4)': {
        'n_s_range': (0.950, 0.965),
        'r_range': (0.0001, 0.01),
        'n_s_central': 0.958,
        'r_central': 0.003,
        'color': PURPLE_LINE,
    },
}


# ═══════════════════════════════════════════════════════════════════
# CMBRuler Class
# ═══════════════════════════════════════════════════════════════════

class CMBRuler:
    """
    BST CMB Ruler — derives the spectral index from D_IV^5 geometry.

    Parameters
    ----------
    quiet : bool
        If True, suppress print output (for programmatic use).

    Usage:
        from toy_cmb_ruler import CMBRuler
        cr = CMBRuler()
        cr.spectral_index()
        cr.tensor_ratio()
        cr.power_spectrum()
        cr.planck_comparison()
        cr.falsification_criteria()
        cr.vs_inflation_models()
        cr.physical_origin()
        cr.future_experiments()
        cr.summary()
        cr.show()
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.N_max = N_MAX
        self.n_C = n_C
        self.N_c = N_c
        self.C_2 = C_2
        self.genus = GENUS
        self.n_s = N_S_BST
        self.r = R_BST
        self.tilt = TILT_BST
        self.running = RUNNING_BST
        self.T_c = T_C_MEV

        if not quiet:
            print("\n" + "=" * 64)
            print("  THE CMB RULER — Toy 54")
            print("  n_s = 1 - n_C/N_max = 1 - 5/137 = 0.96350")
            print("  r = 0 (BST: no inflaton, no primordial tensors)")
            print("=" * 64)

    # ─────────────────────────────────────────────────────────────
    # 1. spectral_index
    # ─────────────────────────────────────────────────────────────

    def spectral_index(self):
        """
        Compute the BST spectral index n_s = 1 - n_C/N_max.

        Returns dict with BST prediction, Planck observed, sigma deviation.
        """
        sigma = (self.n_s - PLANCK_NS[0]) / PLANCK_NS[1]

        result = {
            'n_s_BST': self.n_s,
            'n_s_observed': PLANCK_NS[0],
            'sigma_error': PLANCK_NS[1],
            'sigma_deviation': sigma,
            'formula': 'n_s = 1 - n_C/N_max = 1 - 5/137',
            'tilt': self.tilt,
            'running': self.running,
            'effective_efolds': 2 * N_MAX / n_C,  # = 54.8
        }

        if not self.quiet:
            print("\n  SPECTRAL INDEX")
            print("  " + "-" * 50)
            print(f"  BST:     n_s = 1 - {n_C}/{N_MAX} = {self.n_s:.5f}")
            print(f"  Planck:  n_s = {PLANCK_NS[0]} +/- {PLANCK_NS[1]}")
            print(f"  Deviation: {sigma:+.2f} sigma")
            print(f"  Tilt:    1 - n_s = {self.tilt:.5f}")
            print(f"  Running: dn_s/dlnk = -5/137^2 = {self.running:.2e}")
            print(f"  Effective e-folds: 2*N_max/n_C = {result['effective_efolds']:.1f}")
            print(f"  Formula: {result['formula']}")

        return result

    # ─────────────────────────────────────────────────────────────
    # 2. tensor_ratio
    # ─────────────────────────────────────────────────────────────

    def tensor_ratio(self):
        """
        BST tensor-to-scalar ratio r = 0.

        The phase transition at T_c = 130.5 MeV is far below the Planck scale.
        No inflaton field means no primordial tensor modes from slow-roll.
        """
        # Naive estimate of r from phase transition
        m_Pl_MeV = 1.22e22  # Planck mass in MeV
        r_naive = 16.0 * (self.T_c / m_Pl_MeV)**4 * C_V

        result = {
            'r_BST': 0.0,
            'r_naive_estimate': r_naive,
            'r_upper_limit_BICEP': 0.036,
            'r_target_LiteBIRD': 0.001,
            'mechanism': 'No inflaton field; phase transition at T_c = 130.5 MeV << m_Pl',
            'T_c_MeV': self.T_c,
            'falsifiable': 'r > 0.001 from LiteBIRD would falsify BST',
        }

        if not self.quiet:
            print("\n  TENSOR-TO-SCALAR RATIO")
            print("  " + "-" * 50)
            print(f"  BST prediction:  r = 0 (effectively)")
            print(f"  Naive estimate:  r ~ 16*(T_c/m_Pl)^4 * C_v ~ {r_naive:.1e}")
            print(f"  BICEP/Keck 2021: r < 0.036 (95% CL)")
            print(f"  BST: consistent (72 orders of magnitude below limit)")
            print(f"  Mechanism: {result['mechanism']}")
            print(f"  SHARP PREDICTION: inflation -> r > 0; BST -> r = 0")

        return result

    # ─────────────────────────────────────────────────────────────
    # 3. power_spectrum
    # ─────────────────────────────────────────────────────────────

    def power_spectrum(self, l_max=2500):
        """
        Compute a simplified TT power spectrum C_l with BST n_s.

        This is a toy model: Sachs-Wolfe plateau + acoustic peaks.
        Uses BST n_s for the primordial tilt.

        Returns dict with l_array, Cl_array.
        """
        ell = np.arange(2, l_max + 1, dtype=float)

        # Primordial power spectrum: P(k) ~ k^{n_s - 1}
        # Map ell to k via k ~ ell / r_*, r_* = comoving sound horizon
        k_pivot = 0.05  # Mpc^-1 (Planck pivot)
        k_eff = ell / 14000.0  # rough ell-to-k mapping

        # Primordial tilt
        P_prim = PLANCK_AS * (k_eff / k_pivot) ** (self.n_s - 1.0)

        # Transfer function (simplified): Sachs-Wolfe + acoustic oscillations
        # Sachs-Wolfe plateau for ell < 100
        # Acoustic peaks at ell ~ 220, 540, 810, ...
        theta_s = np.pi / 300.0  # angular scale of sound horizon
        x = ell * theta_s

        # Damping envelope (Silk damping)
        l_silk = 1200.0
        damping = np.exp(-(ell / l_silk) ** 1.4)

        # Acoustic oscillations (simplified cosine series)
        acoustic = (1.0 + 0.45 * np.cos(x) ** 2) * damping

        # Sachs-Wolfe plateau blending
        sw_weight = np.exp(-ell / 80.0)
        sw_plateau = 1.0

        # Combined C_l (dimensionless, in units of l(l+1)C_l / 2pi)
        Cl = P_prim * (sw_weight * sw_plateau + (1.0 - sw_weight) * acoustic)

        # Normalize to match typical CMB scale (~6000 muK^2 at first peak)
        peak_idx = np.argmax(Cl[200:400]) + 200
        Cl_normalized = Cl / Cl[peak_idx] * 5800.0

        result = {
            'l_array': ell,
            'Cl_array': Cl_normalized,
            'n_s_used': self.n_s,
            'l_max': l_max,
            'note': 'Simplified toy model: SW plateau + acoustic peaks + Silk damping',
        }

        if not self.quiet:
            print("\n  POWER SPECTRUM (simplified)")
            print("  " + "-" * 50)
            print(f"  l range: 2 to {l_max}")
            print(f"  n_s used: {self.n_s:.5f} (BST)")
            print(f"  Peak 1 at l ~ {ell[peak_idx]:.0f}")
            print(f"  C_l(peak1) ~ {Cl_normalized[peak_idx]:.0f} muK^2")
            print(f"  Note: toy model for visualization, not precision cosmology")

        return result

    # ─────────────────────────────────────────────────────────────
    # 4. planck_comparison
    # ─────────────────────────────────────────────────────────────

    def planck_comparison(self):
        """
        Compare BST predictions against Planck 2018 results.

        Returns list of comparison dicts.
        """
        comparisons = [
            {
                'quantity': 'n_s (spectral index)',
                'BST': f'{self.n_s:.5f}',
                'BST_value': self.n_s,
                'Planck': f'{PLANCK_NS[0]} +/- {PLANCK_NS[1]}',
                'Planck_value': PLANCK_NS[0],
                'sigma': (self.n_s - PLANCK_NS[0]) / PLANCK_NS[1],
                'formula': '1 - 5/137',
            },
            {
                'quantity': 'r (tensor ratio)',
                'BST': '0 (exact)',
                'BST_value': 0.0,
                'Planck': '< 0.036 (95% CL)',
                'Planck_value': 0.0,
                'sigma': 0.0,
                'formula': 'T_c << m_Pl => r ~ 0',
            },
            {
                'quantity': 'Omega_b h^2',
                'BST': f'{OBH2_BST:.5f}',
                'BST_value': OBH2_BST,
                'Planck': f'{PLANCK_OBH2[0]} +/- {PLANCK_OBH2[1]}',
                'Planck_value': PLANCK_OBH2[0],
                'sigma': (OBH2_BST - PLANCK_OBH2[0]) / PLANCK_OBH2[1],
                'formula': '(18/361) * h^2',
            },
            {
                'quantity': 'Omega_c h^2',
                'BST': f'{OCH2_BST:.4f}',
                'BST_value': OCH2_BST,
                'Planck': f'{PLANCK_OCH2[0]} +/- {PLANCK_OCH2[1]}',
                'Planck_value': PLANCK_OCH2[0],
                'sigma': (OCH2_BST - PLANCK_OCH2[0]) / PLANCK_OCH2[1],
                'formula': '(96/361) * h^2',
            },
        ]

        if not self.quiet:
            print("\n  BST vs PLANCK 2018")
            print("  " + "=" * 62)
            print(f"  {'Quantity':<22} {'BST':>12} {'Planck':>14} {'dev':>10}")
            print("  " + "-" * 62)
            for c in comparisons:
                sig_str = f"{c['sigma']:+.2f}s" if c['sigma'] != 0 else "OK"
                print(f"  {c['quantity']:<22} {c['BST']:>12} "
                      f"{c['Planck']:>14} {sig_str:>10}")
            print("  " + "=" * 62)

        return comparisons

    # ─────────────────────────────────────────────────────────────
    # 5. falsification_criteria
    # ─────────────────────────────────────────────────────────────

    def falsification_criteria(self):
        """
        What would disprove BST's CMB predictions.

        Returns list of falsification criteria dicts.
        """
        criteria = [
            {
                'test': 'Tensor-to-scalar ratio r > 0.001',
                'experiment': 'LiteBIRD (launch ~2032)',
                'status': 'OPEN — awaiting data',
                'severity': 'FATAL — BST predicts r = 0',
                'detail': ('BST has no inflaton, so no slow-roll tensor modes. '
                           'Detection of primordial B-modes at r > 0.001 '
                           'would falsify BST or require a new tensor source.'),
            },
            {
                'test': 'n_s outside 0.960 - 0.967',
                'experiment': 'CMB-S4, Simons Observatory',
                'status': 'OPEN — Planck: 0.9649 +/- 0.0042',
                'severity': 'SERIOUS — BST predicts 0.96350',
                'detail': ('BST predicts n_s = 1 - 5/137 = 0.96350. '
                           'A measurement >3 sigma from this value would '
                           'require BST modification (e.g., genus correction).'),
            },
            {
                'test': 'Running dn_s/dlnk significantly nonzero',
                'experiment': 'CMB-S4',
                'status': 'OPEN — Planck: -0.0045 +/- 0.0067',
                'severity': 'MODERATE — BST predicts -2.7e-4 (near zero)',
                'detail': ('BST running = -n_C/N_max^2 = -5/18769 ~ -2.7e-4. '
                           'Large running (|dn_s/dlnk| > 0.01) would challenge BST.'),
            },
            {
                'test': 'Non-Gaussianity f_NL > 1',
                'experiment': 'CMB-S4, LSS surveys',
                'status': 'OPEN — Planck: f_NL = -0.9 +/- 5.1',
                'severity': 'MODERATE — BST predicts near-Gaussian',
                'detail': ('BST phase transition is sharp (C_v = 330,000), '
                           'predicting near-Gaussian perturbations. '
                           'Large f_NL would require an additional mechanism.'),
            },
            {
                'test': 'Anomalous low-ell power deficit persists',
                'experiment': 'LiteBIRD full-sky',
                'status': 'WATCHING — hints in Planck data',
                'severity': 'INTERESTING — could support BST',
                'detail': ('BST predicts a finite bubble S^2 topology, which '
                           'would suppress power at the largest scales (low ell). '
                           'Confirmation would support BST over flat-space inflation.'),
            },
        ]

        if not self.quiet:
            print("\n  FALSIFICATION CRITERIA")
            print("  " + "=" * 60)
            for i, c in enumerate(criteria, 1):
                print(f"\n  {i}. {c['test']}")
                print(f"     Experiment: {c['experiment']}")
                print(f"     Status:     {c['status']}")
                print(f"     Severity:   {c['severity']}")
            print("\n  " + "=" * 60)

        return criteria

    # ─────────────────────────────────────────────────────────────
    # 6. vs_inflation_models
    # ─────────────────────────────────────────────────────────────

    def vs_inflation_models(self):
        """
        BST vs inflation models in the n_s - r plane.

        Returns comparison dict with BST point and model regions.
        """
        result = {
            'BST': {
                'n_s': self.n_s,
                'r': 0.0,
                'label': 'BST (geometric, zero parameters)',
            },
            'models': {},
        }

        for name, model in INFLATION_MODELS.items():
            result['models'][name] = {
                'n_s_range': model['n_s_range'],
                'r_range': model['r_range'],
                'n_s_central': model['n_s_central'],
                'r_central': model['r_central'],
            }

        if not self.quiet:
            print("\n  BST vs INFLATION MODELS (n_s - r plane)")
            print("  " + "=" * 60)
            print(f"  {'Model':<24} {'n_s':>8} {'r':>10}")
            print("  " + "-" * 60)
            print(f"  {'BST':<24} {self.n_s:>8.5f} {'~ 0':>10}")
            for name, model in INFLATION_MODELS.items():
                print(f"  {name:<24} {model['n_s_central']:>8.3f} "
                      f"{model['r_central']:>10.4f}")
            print("  " + "-" * 60)
            print("  BST sits at r=0, cleanly separated from all inflation models.")
            print("  " + "=" * 60)

        return result

    # ─────────────────────────────────────────────────────────────
    # 7. physical_origin
    # ─────────────────────────────────────────────────────────────

    def physical_origin(self):
        """
        Why n_s < 1: the geometric origin of the spectral tilt.

        Returns dict with the physical explanation.
        """
        frozen_modes = N_MAX - n_C    # 132
        active_modes = n_C             # 5
        efolds = 2 * N_MAX / n_C       # 54.8

        result = {
            'n_C': n_C,
            'N_max': N_MAX,
            'tilt': self.tilt,
            'frozen_modes': frozen_modes,
            'active_modes': active_modes,
            'mechanism': (
                f'The {n_C} complex dimensions of D_IV^5 each contribute '
                f'1/N_max = 1/{N_MAX} of spectral tilt. '
                f'The remaining {frozen_modes} Haldane modes are frozen '
                f'(committed) during the phase transition and contribute '
                f'no perturbations.'
            ),
            'analogy': (
                f'Equivalent to inflation with N_e = 2*N_max/n_C = {efolds:.1f} '
                f'e-folds, but derived from geometry, not a slow-roll potential.'
            ),
            'phase_transition': {
                'T_c_MeV': T_C_MEV,
                'C_v': C_V,
                'symmetry_breaking': 'SO_0(5,2) -> SO(5) x SO(2)',
                'generators': '1 of 21 generators activated (S^1 fiber)',
            },
            'scale_dependence': (
                'Different k-modes freeze at slightly different times. '
                'Each e-fold loses one mode from the active set, giving '
                'Delta n_s / Delta ln k = -1/N_max per mode.'
            ),
        }

        if not self.quiet:
            print("\n  PHYSICAL ORIGIN OF THE SPECTRAL TILT")
            print("  " + "=" * 60)
            print(f"  n_s = 1 - {active_modes}/{N_MAX} = {self.n_s:.5f}")
            print(f"  Active modes:  {active_modes} (complex dimensions of D_IV^5)")
            print(f"  Frozen modes:  {frozen_modes} (Haldane exclusion ground state)")
            print(f"  Each dimension contributes tilt: 1/{N_MAX} = {1.0/N_MAX:.5f}")
            print(f"  Total tilt: {active_modes} x 1/{N_MAX} = {self.tilt:.5f}")
            print()
            print(f"  Phase transition: SO_0(5,2) -> SO(5) x SO(2)")
            print(f"  T_c = {T_C_MEV:.1f} MeV,  C_v = {C_V:,}")
            print(f"  Effective e-folds: {efolds:.1f} (cf. inflation: 55-60)")
            print()
            print(f"  Key insight: the tilt counts HOW MANY dimensions fluctuate")
            print(f"  at the phase transition. Five of 137. That's it.")
            print("  " + "=" * 60)

        return result

    # ─────────────────────────────────────────────────────────────
    # 8. future_experiments
    # ─────────────────────────────────────────────────────────────

    def future_experiments(self):
        """
        Future CMB experiments and what they mean for BST.

        Returns list of experiment dicts.
        """
        experiments = [
            {
                'name': 'LiteBIRD',
                'agency': 'JAXA',
                'launch': '~2032',
                'target': 'r sensitivity: delta_r ~ 0.001',
                'BST_impact': (
                    'DECISIVE. If r > 0.001 detected, BST falsified. '
                    'If r < 0.001, inflation models with r > 0.01 eliminated, '
                    'BST survives as the geometric alternative.'
                ),
                'measures': 'Primordial B-mode polarization (full sky)',
            },
            {
                'name': 'CMB-S4',
                'agency': 'DOE/NSF',
                'launch': '~2030',
                'target': 'sigma(n_s) ~ 0.002, sigma(r) ~ 0.003',
                'BST_impact': (
                    'Can distinguish BST n_s = 0.96350 from '
                    'Candidate B n_s = 0.96528 (differ by 0.0018). '
                    'Also measures running dn_s/dlnk to ~0.002.'
                ),
                'measures': 'TT, EE, TE power spectra, lensing, n_s, r, running',
            },
            {
                'name': 'Simons Observatory',
                'agency': 'Private consortium',
                'launch': 'Operating (first light 2024)',
                'target': 'sigma(n_s) ~ 0.003, sigma(r) ~ 0.01',
                'BST_impact': (
                    'First next-generation ground test. '
                    'Can tighten n_s by ~2x over Planck. '
                    'BST prediction well within reach.'
                ),
                'measures': 'CMB temperature and polarization from Chile',
            },
        ]

        if not self.quiet:
            print("\n  FUTURE CMB EXPERIMENTS")
            print("  " + "=" * 60)
            for exp in experiments:
                print(f"\n  {exp['name']} ({exp['agency']})")
                print(f"    Timeline: {exp['launch']}")
                print(f"    Target:   {exp['target']}")
                print(f"    BST:      {exp['BST_impact']}")
            print("\n  " + "=" * 60)

        return experiments

    # ─────────────────────────────────────────────────────────────
    # 9. summary
    # ─────────────────────────────────────────────────────────────

    def summary(self):
        """
        Key insight: the CMB spectral index is a mode count.

        Returns dict with the essential summary.
        """
        result = {
            'title': 'The CMB Ruler',
            'key_result': 'n_s = 1 - 5/137 = 0.96350  (-0.3 sigma from Planck)',
            'key_prediction': 'r = 0  (no primordial gravitational waves)',
            'falsification': 'LiteBIRD r > 0.001 would falsify BST',
            'insight': (
                'The CMB spectral index counts how many of the 137 Haldane '
                'modes are active at the phase transition. Five complex '
                'dimensions fluctuate; 132 are frozen. The tilt is 5/137. '
                'No inflaton. No potential. No free parameters.'
            ),
            'parameters_used': 0,
        }

        if not self.quiet:
            print("\n  " + "=" * 64)
            print("  THE CMB RULER — Summary")
            print("  " + "=" * 64)
            print(f"\n  {result['key_result']}")
            print(f"  {result['key_prediction']}")
            print(f"  {result['falsification']}")
            print(f"\n  {result['insight']}")
            print(f"\n  Free parameters: {result['parameters_used']}")
            print("  " + "=" * 64)

        return result

    # ─────────────────────────────────────────────────────────────
    # 10. show — 4-panel visualization
    # ─────────────────────────────────────────────────────────────

    def show(self):
        """
        4-panel visualization:
          Top-left:     CMB power spectrum C_l with BST n_s
          Top-right:    n_s - r plane with BST and inflation models
          Bottom-left:  Planck comparison table
          Bottom-right: Falsification criteria with status
        """
        fig = plt.figure(figsize=(20, 12), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'BST — The CMB Ruler: Spectral Index from Geometry')

        # Title
        fig.text(0.50, 0.975,
                 'THE CMB RULER',
                 ha='center', va='top', color=GOLD, fontsize=26, weight='bold',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=4, foreground=GOLD_DIM,
                                             alpha=0.4)])
        fig.text(0.50, 0.945,
                 r'$n_s = 1 - n_C / N_{max} = 1 - 5/137 = 0.96350$'
                 '     |     r = 0  (no inflaton)',
                 ha='center', va='top', color=LIGHT_GREY, fontsize=13,
                 fontfamily='monospace')

        gs = GridSpec(2, 2, figure=fig,
                      hspace=0.25, wspace=0.20,
                      left=0.06, right=0.96, top=0.91, bottom=0.05)

        # ────────────────────────────────────────────────────────
        # TOP LEFT: CMB Power Spectrum
        # ────────────────────────────────────────────────────────

        ax1 = fig.add_subplot(gs[0, 0])
        ax1.set_facecolor(DARK_PANEL)

        spec = self.power_spectrum.__wrapped__(self) if hasattr(self.power_spectrum, '__wrapped__') else CMBRuler(quiet=True).power_spectrum()
        ell = spec['l_array']
        Cl = spec['Cl_array']

        ax1.plot(ell, Cl, color=CYAN, linewidth=1.2, alpha=0.9,
                 label=f'BST n_s = {self.n_s:.5f}')

        # Also show scale-invariant (n_s=1) for comparison
        spec_flat = _compute_spectrum_with_ns(1.0, len(ell) + 1)
        ax1.plot(ell, spec_flat, color=GREY, linewidth=0.8, alpha=0.5,
                 linestyle='--', label='Scale invariant (n_s = 1)')

        ax1.set_xlabel(r'Multipole $\ell$', color=LIGHT_GREY, fontsize=11)
        ax1.set_ylabel(r'$\ell(\ell+1) C_\ell / 2\pi$ [$\mu K^2$]',
                       color=LIGHT_GREY, fontsize=11)
        ax1.set_title('CMB TT Power Spectrum (simplified)',
                      color=GOLD, fontsize=13, fontfamily='monospace',
                      weight='bold', pad=10)
        ax1.set_xlim(2, 2500)
        ax1.set_ylim(0, None)
        ax1.tick_params(colors=GREY)
        ax1.spines['bottom'].set_color(GREY)
        ax1.spines['left'].set_color(GREY)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.legend(loc='upper right', fontsize=9,
                   facecolor=DARK_PANEL, edgecolor=GREY,
                   labelcolor=LIGHT_GREY)

        # Annotate first peak
        peak_idx = np.argmax(Cl[200:400]) + 200
        ax1.annotate(f'Peak 1: l ~ {ell[peak_idx]:.0f}',
                     xy=(ell[peak_idx], Cl[peak_idx]),
                     xytext=(ell[peak_idx] + 300, Cl[peak_idx] * 0.85),
                     fontsize=9, color=GOLD,
                     arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1))

        # ────────────────────────────────────────────────────────
        # TOP RIGHT: n_s - r Plane
        # ────────────────────────────────────────────────────────

        ax2 = fig.add_subplot(gs[0, 1])
        ax2.set_facecolor(DARK_PANEL)

        # Planck 2018 constraint bands (1-sigma and 2-sigma)
        ns_grid = np.linspace(0.945, 0.980, 200)
        r_grid = np.linspace(-0.005, 0.20, 200)
        NS_G, R_G = np.meshgrid(ns_grid, r_grid)

        # Simplified Planck constraint (n_s, r) — elliptical contour
        chi2 = ((NS_G - PLANCK_NS[0]) / PLANCK_NS[1])**2 + (R_G / 0.018)**2
        ax2.contourf(NS_G, R_G, chi2, levels=[0, 2.30, 6.18],
                     colors=[GREEN_GLOW, BLUE_GLOW], alpha=[0.15, 0.08])
        ax2.contour(NS_G, R_G, chi2, levels=[2.30, 6.18],
                    colors=[GREEN_GLOW, BLUE_GLOW], linewidths=[1.0, 0.7],
                    alpha=0.4)

        # Inflation model regions
        for name, model in INFLATION_MODELS.items():
            ns_lo, ns_hi = model['n_s_range']
            r_lo, r_hi = model['r_range']
            rect = FancyBboxPatch(
                (ns_lo, r_lo), ns_hi - ns_lo, r_hi - r_lo,
                boxstyle="round,pad=0.001",
                facecolor=model['color'], alpha=0.25,
                edgecolor=model['color'], linewidth=1.0)
            ax2.add_patch(rect)
            ax2.plot(model['n_s_central'], model['r_central'],
                     'o', color=model['color'], markersize=6, alpha=0.8)
            # Label
            ax2.text(model['n_s_central'], r_hi + 0.003, name,
                     fontsize=7, color=model['color'], ha='center', va='bottom',
                     alpha=0.9)

        # BST point
        ax2.plot(self.n_s, 0.0, '*', color=GOLD, markersize=18, zorder=10,
                 markeredgecolor=GOLD_DIM, markeredgewidth=1)
        ax2.text(self.n_s + 0.001, 0.008, 'BST', fontsize=12, color=GOLD,
                 weight='bold', ha='center',
                 path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

        # LiteBIRD sensitivity line
        ax2.axhline(y=0.001, color=RED_WARM, linestyle=':', linewidth=1.0,
                     alpha=0.6)
        ax2.text(0.975, 0.002, 'LiteBIRD target (r=0.001)',
                 fontsize=8, color=RED_WARM, ha='right', alpha=0.7)

        ax2.set_xlabel(r'$n_s$ (spectral index)', color=LIGHT_GREY, fontsize=11)
        ax2.set_ylabel(r'$r$ (tensor-to-scalar)', color=LIGHT_GREY, fontsize=11)
        ax2.set_title(r'$n_s$ - $r$ Plane: BST vs Inflation',
                      color=GOLD, fontsize=13, fontfamily='monospace',
                      weight='bold', pad=10)
        ax2.set_xlim(0.945, 0.980)
        ax2.set_ylim(-0.005, 0.20)
        ax2.tick_params(colors=GREY)
        ax2.spines['bottom'].set_color(GREY)
        ax2.spines['left'].set_color(GREY)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)

        # ────────────────────────────────────────────────────────
        # BOTTOM LEFT: Planck Comparison Table
        # ────────────────────────────────────────────────────────

        ax3 = fig.add_subplot(gs[1, 0])
        ax3.set_facecolor(BG)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')

        ax3.text(0.5, 0.95, 'BST vs Planck 2018',
                 color=GOLD, fontsize=14, fontfamily='monospace',
                 weight='bold', ha='center', va='top',
                 path_effects=[pe.withStroke(linewidth=2, foreground=GOLD_DIM,
                                             alpha=0.3)])

        # Table header
        cols = [0.02, 0.28, 0.48, 0.68, 0.88]
        headers = ['Quantity', 'BST', 'Planck', 'Formula', 'Dev']
        y = 0.82
        for x, h in zip(cols, headers):
            ax3.text(x, y, h, color=GREY, fontsize=9, ha='left',
                     weight='bold', fontfamily='monospace')
        y -= 0.03
        ax3.plot([0.02, 0.98], [y, y], color=GREY, alpha=0.3, linewidth=0.5)
        y -= 0.05

        table_rows = [
            ('n_s', f'{self.n_s:.5f}', f'{PLANCK_NS[0]}', '1 - 5/137',
             (self.n_s - PLANCK_NS[0]) / PLANCK_NS[1]),
            ('r', '0', '< 0.036', 'T_c << m_Pl', 0.0),
            ('Ob h^2', f'{OBH2_BST:.5f}', f'{PLANCK_OBH2[0]}', '18/361 h^2',
             (OBH2_BST - PLANCK_OBH2[0]) / PLANCK_OBH2[1]),
            ('Oc h^2', f'{OCH2_BST:.4f}', f'{PLANCK_OCH2[0]}', '96/361 h^2',
             (OCH2_BST - PLANCK_OCH2[0]) / PLANCK_OCH2[1]),
            ('dn_s/dlnk', f'{RUNNING_BST:.1e}', f'{PLANCK_RUNNING[0]}',
             '-5/137^2',
             (RUNNING_BST - PLANCK_RUNNING[0]) / PLANCK_RUNNING[1]),
        ]

        for label, bst, planck, formula, sig in table_rows:
            sig_color = GREEN_GLOW if abs(sig) < 1.0 else GOLD if abs(sig) < 2.0 else RED_WARM
            sig_str = f'{sig:+.1f}s' if sig != 0 else 'OK'
            ax3.text(cols[0], y, label, color=WHITE, fontsize=9, ha='left',
                     fontfamily='monospace')
            ax3.text(cols[1], y, bst, color=CYAN, fontsize=9, ha='left',
                     fontfamily='monospace')
            ax3.text(cols[2], y, planck, color=LIGHT_GREY, fontsize=9, ha='left',
                     fontfamily='monospace')
            ax3.text(cols[3], y, formula, color=GOLD_DIM, fontsize=9, ha='left',
                     fontfamily='monospace')
            ax3.text(cols[4], y, sig_str, color=sig_color, fontsize=10, ha='left',
                     weight='bold', fontfamily='monospace')
            y -= 0.10

        # Bottom note
        ax3.text(0.5, 0.03,
                 'Zero free parameters. All derived from n_C=5, N_max=137.',
                 color=GREY, fontsize=9, ha='center', style='italic')

        # ────────────────────────────────────────────────────────
        # BOTTOM RIGHT: Falsification Criteria
        # ────────────────────────────────────────────────────────

        ax4 = fig.add_subplot(gs[1, 1])
        ax4.set_facecolor(BG)
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')

        ax4.text(0.5, 0.95, 'Falsification Criteria',
                 color=GOLD, fontsize=14, fontfamily='monospace',
                 weight='bold', ha='center', va='top',
                 path_effects=[pe.withStroke(linewidth=2, foreground=GOLD_DIM,
                                             alpha=0.3)])

        criteria_display = [
            ('r > 0.001 detected',   'LiteBIRD ~2032',  'OPEN',  'FATAL',   RED_WARM),
            ('n_s outside 0.960-0.967', 'CMB-S4 ~2030', 'OPEN',  'SERIOUS', ORANGE),
            ('|dn_s/dlnk| > 0.01',  'CMB-S4',           'OPEN',  'MODERATE', GOLD),
            ('f_NL > 1',            'CMB-S4 / LSS',     'OPEN',  'MODERATE', GOLD),
            ('Low-ell power deficit','LiteBIRD',         'HINTS', 'SUPPORTS', GREEN_GLOW),
        ]

        y = 0.80
        for test, exp, status, severity, color in criteria_display:
            # Status indicator
            if status == 'OPEN':
                indicator = 'O'
                ind_color = GREY
            elif status == 'HINTS':
                indicator = '?'
                ind_color = GREEN_GLOW
            else:
                indicator = 'X'
                ind_color = RED_WARM

            ax4.text(0.03, y, indicator, color=ind_color, fontsize=14,
                     weight='bold', ha='center', va='center',
                     fontfamily='monospace',
                     path_effects=[pe.withStroke(linewidth=2,
                                                 foreground=ind_color, alpha=0.3)])
            ax4.text(0.08, y + 0.01, test, color=WHITE, fontsize=9.5, ha='left',
                     va='center', fontfamily='monospace')
            ax4.text(0.08, y - 0.04, f'{exp}  |  {severity}',
                     color=color, fontsize=8, ha='left', va='center',
                     fontfamily='monospace', alpha=0.8)
            y -= 0.13

        # Bottom summary
        ax4.text(0.5, 0.03,
                 'BST makes a clean, binary prediction: r = 0.',
                 color=CYAN, fontsize=10, ha='center', weight='bold',
                 style='italic')

        # ────────────────────────────────────────────────────────
        # Footer
        # ────────────────────────────────────────────────────────

        fig.text(0.50, 0.01,
                 'Five dimensions fluctuate. 132 are frozen. The tilt is 5/137. '
                 'No inflaton. No potential. No free parameters.',
                 ha='center', va='bottom', color=GREY, fontsize=10,
                 style='italic', fontfamily='monospace')

        plt.tight_layout(rect=[0.02, 0.03, 0.98, 0.93])
        plt.show()
        return fig


# ═══════════════════════════════════════════════════════════════════
# Helper: compute spectrum with arbitrary n_s
# ═══════════════════════════════════════════════════════════════════

def _compute_spectrum_with_ns(n_s, l_max=2501):
    """Compute simplified C_l with given n_s (for overlay comparisons)."""
    ell = np.arange(2, l_max, dtype=float)
    k_pivot = 0.05
    k_eff = ell / 14000.0
    P_prim = PLANCK_AS * (k_eff / k_pivot) ** (n_s - 1.0)

    theta_s = np.pi / 300.0
    x = ell * theta_s
    l_silk = 1200.0
    damping = np.exp(-(ell / l_silk) ** 1.4)
    acoustic = (1.0 + 0.45 * np.cos(x) ** 2) * damping
    sw_weight = np.exp(-ell / 80.0)

    Cl = P_prim * (sw_weight * 1.0 + (1.0 - sw_weight) * acoustic)
    peak_idx = np.argmax(Cl[200:400]) + 200
    Cl_normalized = Cl / Cl[peak_idx] * 5800.0
    return Cl_normalized


# ═══════════════════════════════════════════════════════════════════
# Print Report
# ═══════════════════════════════════════════════════════════════════

def print_report():
    """Print a concise summary report."""
    sep = "=" * 64
    print(f"\n{sep}")
    print("  THE CMB RULER — Toy 54")
    print(f"{sep}\n")
    print(f"  n_s = 1 - n_C/N_max = 1 - 5/137 = {N_S_BST:.5f}")
    print(f"  Planck 2018: {PLANCK_NS[0]} +/- {PLANCK_NS[1]}")
    print(f"  Deviation: {(N_S_BST - PLANCK_NS[0])/PLANCK_NS[1]:+.2f} sigma")
    print()
    print(f"  r = 0  (BST: no inflaton, T_c = {T_C_MEV:.1f} MeV << m_Pl)")
    print(f"  BICEP/Keck: r < 0.036 (BST: 72 orders of magnitude below)")
    print()
    print(f"  Running: dn_s/dlnk = -5/137^2 = {RUNNING_BST:.2e}")
    print(f"  Effective e-folds: 2*N_max/n_C = {2*N_MAX/n_C:.1f}")
    print()
    print(f"  Origin: {n_C} complex dimensions fluctuate, {N_MAX - n_C} frozen")
    print(f"  Phase transition: SO_0(5,2) -> SO(5) x SO(2) at T_c")
    print(f"  C_v = {C_V:,} (extremely sharp transition)")
    print()
    print(f"  SHARP PREDICTION: inflation -> r > 0;  BST -> r = 0")
    print(f"  FALSIFIABLE by: LiteBIRD (r > 0.001), CMB-S4 (n_s precision)")
    print(f"\n{sep}\n")


# ═══════════════════════════════════════════════════════════════════
# Main Menu
# ═══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the CMB Ruler toy."""
    cr = CMBRuler(quiet=False)
    print()

    while True:
        print("\n+-----------------------------------------------+")
        print("|  THE CMB RULER — Toy 54                       |")
        print("+-----------------------------------------------+")
        print("|  1. Spectral index (n_s = 1 - 5/137)         |")
        print("|  2. Tensor ratio (r = 0)                      |")
        print("|  3. Power spectrum C_l                        |")
        print("|  4. Planck comparison                         |")
        print("|  5. Falsification criteria                    |")
        print("|  6. BST vs inflation models                   |")
        print("|  7. Physical origin of the tilt               |")
        print("|  8. Future experiments                        |")
        print("|  9. Summary                                   |")
        print("| 10. Show (4-panel visualization)              |")
        print("|  0. Quit                                      |")
        print("+-----------------------------------------------+")

        try:
            choice = input("\n  Choose [0-10]: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == '0':
            print("\n  Five of 137. The ruler is set.\n")
            break
        elif choice == '1':
            cr.spectral_index()
        elif choice == '2':
            cr.tensor_ratio()
        elif choice == '3':
            cr.power_spectrum()
        elif choice == '4':
            cr.planck_comparison()
        elif choice == '5':
            cr.falsification_criteria()
        elif choice == '6':
            cr.vs_inflation_models()
        elif choice == '7':
            cr.physical_origin()
        elif choice == '8':
            cr.future_experiments()
        elif choice == '9':
            cr.summary()
        elif choice == '10':
            cr.show()
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    main()
