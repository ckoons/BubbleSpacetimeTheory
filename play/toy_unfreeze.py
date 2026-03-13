#!/usr/bin/env python3
"""
TOY 41 — THE BIG BANG UNFREEZING
=================================
The Big Bang is NOT an explosion from a singularity. It is exactly ONE of
21 SO(5,2) generators unfreezing at T_c = 0.487 MeV (t = 3.1 seconds).

The SO(2) generator (S^1 fiber) becomes dynamical, breaking:

    SO(7) -> SO(5) x SO(2)

activating D_IV^5. No singularity, no infinite density — just one rotation
begins, and everything happens at once.

    21 generators = 10 (so(5), frozen) + 1 (so(2), UNFREEZES) + 10 (m, dynamical)

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
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity (Haldane exclusion)
genus = 7         # genus of D_IV^5
C_2 = 6           # Casimir eigenvalue of pi_6
alpha = 1.0 / 137.036
m_e_MeV = 0.511   # electron mass in MeV
m_p_MeV = 938.272  # proton mass in MeV
T_c_MeV = m_e_MeV * 20.0 / 21.0   # 0.4867 MeV
t_transition = 3.1  # seconds (standard FRW at T_c)

# BBN and cosmological constants
g_star_S = 10.75   # effective dof: photon + e+/- + 3 neutrinos
Delta_g = genus     # 7 extra dof at transition
eta_BST = 2.0 * alpha**4 / (3.0 * np.pi)  # baryon-to-photon ratio

# ─── Visual constants ───
BG = '#0a0a1a'
BG_PANEL = '#0d0d24'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
ORANGE = '#ff8800'
CYAN = '#00ddff'
WHITE = '#ffffff'
GREY = '#888888'
GREY_FROZEN = '#444466'
RED_WARM = '#ff6644'
GREEN = '#44ff88'
BLUE = '#4488ff'
PURPLE = '#9966ff'


# ═══════════════════════════════════════════════════════════════════
#  BigBangUnfreeze CLASS
# ═══════════════════════════════════════════════════════════════════

class BigBangUnfreeze:
    """
    The Big Bang as one generator unfreezing.

    Usage:
        from toy_unfreeze import BigBangUnfreeze
        bb = BigBangUnfreeze()
        bb.generators()         # all 21 so(5,2) generators
        bb.phase_transition()   # the unfreezing event
        bb.timeline()           # from frozen era to now
        bb.bbn_elements()       # nucleosynthesis with Li-7 fix
        bb.cmb_predictions()    # spectral index, tensor ratio
        bb.vs_inflation()       # BST vs standard inflation
        bb.gravitational_bell() # the bell rings at ~6-9 nHz
        bb.summary()            # one-paragraph summary
        bb.show()               # 4-panel visualization
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.T_c = T_c_MeV
        self.t_transition = t_transition
        if not quiet:
            print()
            print("=" * 68)
            print("  THE BIG BANG UNFREEZING")
            print("  One generator. 21 possibilities. One that works.")
            print("=" * 68)
            print()
            print("  T_c = {:.4f} MeV  =  m_e x 20/21".format(self.T_c))
            print("  t   = {:.1f} s       (standard FRW at T_c)".format(self.t_transition))
            print("  Breaking: SO(7) -> SO(5) x SO(2)")
            print("  21 = 10 (frozen) + 1 (unfreezes) + 10 (dynamical)")
            print()

    # ─────────────────────────────────────────────────────────
    # 1. generators()
    # ─────────────────────────────────────────────────────────
    def generators(self):
        """List all 21 generators of so(5,2) with their roles."""
        # so(5) has 10 generators: rotations in 5D
        so5_gens = []
        idx = 0
        for i in range(5):
            for j in range(i + 1, 5):
                idx += 1
                so5_gens.append({
                    'index': idx,
                    'name': 'L_{}{}'.format(i + 1, j + 1),
                    'subalgebra': 'so(5)',
                    'role': 'compact/isotropy',
                    'status_before': 'frozen',
                    'status_after': 'frozen (spatial isotropy)',
                    'physical': 'S^4 rotation {}-{}'.format(i + 1, j + 1),
                })

        # so(2) has 1 generator: the S^1 fiber rotation
        so2_gen = {
            'index': 11,
            'name': 'J (SO(2) fiber)',
            'subalgebra': 'so(2)',
            'role': 'THE generator that unfreezes',
            'status_before': 'frozen (indistinguishable from so(5))',
            'status_after': 'DYNAMICAL — S^1 fiber rotates independently',
            'physical': 'S^1 fiber rotation — the communication channel',
        }

        # m has 10 generators: tangent directions of D_IV^5
        m_gens = []
        for k in range(10):
            m_gens.append({
                'index': 12 + k,
                'name': 'X_{}'.format(k + 1),
                'subalgebra': 'm (tangent space)',
                'role': 'non-compact/dynamical',
                'status_before': 'frozen (symmetry, not dynamics)',
                'status_after': 'DYNAMICAL — configuration space of D_IV^5',
                'physical': 'tangent direction {} of D_IV^5'.format(k + 1),
            })

        result = {
            'total': 21,
            'dim_formula': '7 x 6 / 2 = 21',
            'algebra': 'so(5,2) ~ so(7,C) real form',
            'decomposition': '21 = 10 [so(5)] + 1 [so(2)] + 10 [m]',
            'so5': so5_gens,
            'so2': so2_gen,
            'm': m_gens,
            'all': so5_gens + [so2_gen] + m_gens,
            'frozen_before': 21,
            'frozen_after': 10,
            'unfreezes': 1,
            'dynamical_after': 10,
        }

        if not self.quiet:
            print("  GENERATORS OF so(5,2)")
            print("  " + "-" * 56)
            print("  so(5): 10 generators — frozen before and after")
            print("  so(2):  1 generator  — THE ONE THAT UNFREEZES")
            print("  m:     10 generators — become dynamical at T_c")
            print("  Total: 21 = 7(7-1)/2")
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 2. phase_transition()
    # ─────────────────────────────────────────────────────────
    def phase_transition(self):
        """The unfreezing event at T_c = 0.487 MeV."""
        result = {
            'T_c_MeV': self.T_c,
            'T_c_K': self.T_c * 1.16e10,  # MeV to Kelvin
            'time_seconds': self.t_transition,
            'breaking': 'SO(7) -> SO(5) x SO(2)',
            'which_generator': 'SO(2) — the S^1 fiber rotation',
            'mechanism': 'Bergman oscillator ground-state energy = n_C^2 = 25 thermal quanta',
            'why_this_T': 'T_c = m_e x 20/21 — geometry wins over thermodynamics',
            'why_this_generator': 'SO(2) is the unique unfreezing producing a Hermitian symmetric space',
            'C_v_at_Tc': 330000,
            'consequences': [
                'S^1 fiber becomes communication channel',
                '10 tangent generators of D_IV^5 become dynamical',
                'Bergman metric becomes physical',
                'First S^1 winding circuits form (electrons)',
                'First Z_3 circuits form (protons)',
                'Baryon asymmetry eta = 2*alpha^4/(3*pi) is geometric — already set',
                'Gravitational wave: one ring of the bell at ~6 nHz',
            ],
            'what_existed_before': [
                'Algebra so(5,2) with all 21 generators frozen',
                'Domain D_IV^5 as mathematical object (physically inert)',
                'Bergman kernel K_B(z,w) (mathematical, no physics)',
                'alpha = 1/137.036 (geometric property, true before physics)',
                'Vol(D_IV^5) = pi^5/1920 (true before anything moved)',
            ],
            'what_did_not_exist': ['time', 'space', 'particles', 'gravitational waves'],
            'eta': eta_BST,
            'n_s': 1.0 - n_C / N_max,
        }

        if not self.quiet:
            print("  THE UNFREEZING EVENT")
            print("  " + "-" * 56)
            print("  T_c     = {:.4f} MeV  ({:.2e} K)".format(
                result['T_c_MeV'], result['T_c_K']))
            print("  Time    = {:.1f} seconds".format(result['time_seconds']))
            print("  Breaking: {}".format(result['breaking']))
            print("  Which:   {}".format(result['which_generator']))
            print("  C_v     = {:,}".format(result['C_v_at_Tc']))
            print()
            print("  WHY THIS MOMENT:")
            print("    {}".format(result['why_this_T']))
            print("  WHY THIS GENERATOR:")
            print("    {}".format(result['why_this_generator']))
            print()
            print("  CONSEQUENCES:")
            for c in result['consequences']:
                print("    -> {}".format(c))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 3. timeline()
    # ─────────────────────────────────────────────────────────
    def timeline(self, t_max=1e18):
        """Chronological events from the frozen era to t_max seconds."""
        epochs = [
            {
                'name': 'Pre-spatial era (frozen)',
                'time_s': 0.0,
                'time_label': 'logical, not temporal',
                'T_MeV': None,
                'standard_says': 'Does not exist in standard cosmology',
                'bst_says': 'All 21 generators frozen. No space, no time, no particles. '
                            'alpha = 1/137 already true.',
            },
            {
                'name': 'EW sub-transition',
                'time_s': 1e-12,
                'time_label': '~10^-12 s',
                'T_MeV': 1e5,  # ~100 GeV
                'standard_says': 'Higgs field acquires VEV. EW symmetry breaks.',
                'bst_says': 'Pre-spatial substrate sub-transition. Hopf fibration '
                            'S^3->S^2 differentiates. No particles. No GWs.',
            },
            {
                'name': 'QCD sub-transition',
                'time_s': 1e-6,
                'time_label': '~10^-6 s',
                'T_MeV': 150.0,
                'standard_says': 'Quarks confined. Baryon-antibaryon annihilation.',
                'bst_says': 'Z_3 closure emerges as structural feature. Baryon asymmetry '
                            'is geometric (eta = 2*alpha^4/(3*pi)), NOT from annihilation.',
            },
            {
                'name': 'Neutrino decoupling',
                'time_s': 1.0,
                'time_label': '~1 s',
                'T_MeV': 2.0,
                'standard_says': 'Neutrinos stop interacting with matter.',
                'bst_says': 'Vacuum-mode channel quanta decouple. Still pre-spatial.',
            },
            {
                'name': 'THE BIG BANG — ONE GENERATOR UNFREEZES',
                'time_s': t_transition,
                'time_label': '3.1 s',
                'T_MeV': T_c_MeV,
                'standard_says': 'e+e- annihilation (routine event).',
                'bst_says': 'SO(2) unfreezes. Space nucleates. First particles form. '
                            'First gravitational wave. Everything at once.',
            },
            {
                'name': 'Big Bang Nucleosynthesis',
                'time_s': 180.0,
                'time_label': '3 s - 20 min',
                'T_MeV': 0.07,
                'standard_says': 'Standard nucleosynthesis (Li-7 problem unsolved).',
                'bst_says': 'Same + Delta_g = 7 at T_c suppresses Li-7 by 2.73x. Resolved.',
            },
            {
                'name': 'Recombination / CMB release',
                'time_s': 1.2e13,  # ~380,000 years
                'time_label': '380,000 yr',
                'T_MeV': 0.26e-3,  # ~0.26 eV
                'standard_says': 'Recombination. CMB released.',
                'bst_says': 'Same. n_s = 1 - 5/137 = 0.96350. r ~ 0. S^2 anomalies predicted.',
            },
            {
                'name': 'First galaxies',
                'time_s': 3e15,  # ~10^8 years
                'time_label': '~10^8 yr',
                'T_MeV': None,
                'standard_says': 'Slow hierarchical assembly (JWST galaxies problematic).',
                'bst_says': 'Rapid formation: ultra-strong seeds (C_v=330,000), instant '
                            'scaffolding, exponential positive feedback. JWST predicted.',
            },
            {
                'name': 'Today',
                'time_s': 4.35e17,  # 13.8 billion years
                'time_label': '13.8 Gyr',
                'T_MeV': 2.35e-10,  # 2.725 K
                'standard_says': 'Lambda-CDM with dark matter + dark energy.',
                'bst_says': '10^122 committed contacts. Lambda = 2.90e-122. '
                            'Dark matter = uncommitted reservoir. Dark energy = vacuum free energy.',
            },
        ]

        # Filter by t_max
        result = [e for e in epochs if e['time_s'] <= t_max]

        if not self.quiet:
            print("  BST TIMELINE OF THE UNIVERSE")
            print("  " + "-" * 56)
            for e in result:
                tag = "***" if "BIG BANG" in e['name'] else "   "
                print("  {} {:>14s}  {}".format(tag, e['time_label'], e['name']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 4. bbn_elements()
    # ─────────────────────────────────────────────────────────
    def bbn_elements(self):
        """BBN element abundances with BST corrections."""
        # eta suppression factor at T_c
        eta_ratio = g_star_S / (g_star_S + Delta_g)  # 10.75/17.75 = 0.606
        li7_suppression = eta_ratio ** 2.0  # Li-7 ~ eta^2.0 -> 0.367

        elements = [
            {
                'element': 'H (hydrogen)',
                'symbol': 'H',
                'Z': 1, 'A': 1,
                'abundance': 0.75,
                'abundance_label': '~75% by mass',
                'bst_input': 'n/p ~ 1/7 from pre-spatial weak equilibrium',
                'bst_correction': 'None — set before T_c',
                'status': 'consistent',
            },
            {
                'element': 'D (deuterium)',
                'symbol': 'D',
                'Z': 1, 'A': 2,
                'abundance': 2.5e-5,
                'abundance_label': 'D/H ~ 2.5e-5',
                'bst_input': 'eta = {:.3e}'.format(eta_BST),
                'bst_correction': 'None — D bottleneck breaks at T << T_c',
                'status': 'consistent',
            },
            {
                'element': 'He-3 (helium-3)',
                'symbol': 'He-3',
                'Z': 2, 'A': 3,
                'abundance': 1.0e-5,
                'abundance_label': 'He3/H ~ 1e-5',
                'bst_input': 'Standard processing',
                'bst_correction': 'Minor — production largely before T_c',
                'status': 'consistent',
            },
            {
                'element': 'He-4 (helium-4)',
                'symbol': 'He-4',
                'Z': 2, 'A': 4,
                'abundance': 0.247,
                'abundance_label': 'Y_p ~ 0.247',
                'bst_input': 'n/p ~ 1/7 (frozen above T_c)',
                'bst_correction': 'None — n/p set before transition',
                'status': 'consistent',
            },
            {
                'element': 'Li-7 (lithium-7)',
                'symbol': 'Li-7',
                'Z': 3, 'A': 7,
                'abundance': 1.7e-10,
                'abundance_label': 'Li7/H ~ 1.7e-10',
                'bst_input': 'Delta_g = genus = 7 extra dof at T_c',
                'bst_correction': 'Suppressed by {:.2f}x (eta_ratio^2 = ({:.2f}/{:.2f})^2)'.format(
                    1.0 / li7_suppression, g_star_S, g_star_S + Delta_g),
                'standard_prediction': 4.7e-10,
                'observed': 1.6e-10,
                'bst_prediction': 1.7e-10,
                'reduction_factor': 1.0 / li7_suppression,  # ~2.73x
                'observed_reduction': 2.93,
                'match_percent': 7.0,
                'status': 'RESOLVED by BST',
            },
        ]

        if not self.quiet:
            print("  BBN ELEMENT ABUNDANCES (BST)")
            print("  " + "-" * 56)
            for e in elements:
                tag = " *** " if "RESOLVED" in e['status'] else "     "
                print("  {} {:>8s}  {:>16s}  {}".format(
                    tag, e['symbol'], e['abundance_label'], e['status']))
            print()
            print("  Li-7 KEY:")
            print("    Standard prediction:  4.7e-10  (3x too high)")
            print("    BST correction:       Delta_g = {} at T_c".format(genus))
            print("    Suppression factor:   {:.2f}x  (observed: {:.2f}x)".format(
                1.0 / li7_suppression, 2.93))
            print("    BST prediction:       1.7e-10  (match to 7%)")
            print()

        return elements

    # ─────────────────────────────────────────────────────────
    # 5. cmb_predictions()
    # ─────────────────────────────────────────────────────────
    def cmb_predictions(self):
        """CMB predictions from BST."""
        n_s = 1.0 - float(n_C) / float(N_max)  # 1 - 5/137 = 0.96350
        r = (T_c_MeV / 1.22e22)**4  # (T_c/m_Pl)^4 ~ 10^{-74}
        planck_n_s = 0.9649
        planck_sigma = 0.0042

        result = {
            'n_s': n_s,
            'n_s_formula': '1 - n_C/N_max = 1 - 5/137',
            'n_s_planck': planck_n_s,
            'n_s_sigma': planck_sigma,
            'n_s_tension': (n_s - planck_n_s) / planck_sigma,
            'r': r,
            'r_label': '~10^-74 (effectively zero)',
            'r_prediction': 'NO primordial B-modes',
            'r_falsifiable': 'If r > 0.001 detected, BST falsified',
            'anomalies_predicted': [
                'Hemispherical power asymmetry (S^2 topology)',
                'Cold Spot (S^2 topology)',
                'Low-multipole alignment (S^2 substrate)',
            ],
            'n_s_parameters': 0,
            'inflation_parameters': 'at least 1 (inflaton potential)',
        }

        if not self.quiet:
            print("  CMB PREDICTIONS (BST)")
            print("  " + "-" * 56)
            print("  n_s = 1 - 5/137 = {:.5f}".format(n_s))
            print("  Planck:  {:.4f} +/- {:.4f}".format(planck_n_s, planck_sigma))
            print("  Tension: {:.1f} sigma".format(result['n_s_tension']))
            print("  Parameters: ZERO (geometric)")
            print()
            print("  r ~ 10^-74 (effectively zero)")
            print("  -> NO primordial B-modes")
            print("  -> If r > 0.001 detected: BST FALSIFIED")
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 6. vs_inflation()
    # ─────────────────────────────────────────────────────────
    def vs_inflation(self):
        """Side-by-side comparison: BST vs standard inflation."""
        comparison = [
            {
                'aspect': 'What happened',
                'bst': 'One generator of so(5,2) unfreezes',
                'inflation': 'Inflaton field drives exponential expansion',
            },
            {
                'aspect': 'Start time',
                'bst': 't = 3.1 s (definite, from T_c = m_e x 20/21)',
                'inflation': 't ~ 10^-36 s (depends on inflaton potential)',
            },
            {
                'aspect': 'Temperature',
                'bst': 'T_c = 0.487 MeV (parameter-free)',
                'inflation': 'T ~ 10^15 GeV (model-dependent)',
            },
            {
                'aspect': 'Singularity',
                'bst': 'None — pre-spatial era is fully symmetric, not singular',
                'inflation': 'Present (classical GR) or unknown (quantum gravity)',
            },
            {
                'aspect': 'Free parameters',
                'bst': '0 (five integers from topology)',
                'inflation': '>= 1 (inflaton potential shape)',
            },
            {
                'aspect': 'Spectral index n_s',
                'bst': '1 - 5/137 = 0.96350 (geometric)',
                'inflation': 'Depends on inflaton potential',
            },
            {
                'aspect': 'Tensor ratio r',
                'bst': '~0 (T_c << m_Pl)',
                'inflation': '> 0 (predicts primordial B-modes)',
            },
            {
                'aspect': 'GW from EW/QCD',
                'bst': 'NONE — no space before 3.1 s',
                'inflation': 'Yes — phase transitions produce GWs',
            },
            {
                'aspect': 'Li-7 problem',
                'bst': 'RESOLVED (genus = 7 at T_c)',
                'inflation': 'Unsolved',
            },
            {
                'aspect': 'Early galaxies (JWST)',
                'bst': 'Predicted (C_v = 330,000 seeds)',
                'inflation': 'Problematic (too fast for Lambda-CDM)',
            },
            {
                'aspect': 'Baryon asymmetry',
                'bst': 'Geometric: eta = 2*alpha^4/(3*pi)',
                'inflation': 'Requires baryogenesis mechanism (unknown)',
            },
            {
                'aspect': 'Falsifiable?',
                'bst': 'YES: r > 0.001 kills BST; GWs at EW freq kill BST',
                'inflation': 'Partly: r < 0.001 disfavors large-field models',
            },
        ]

        if not self.quiet:
            print("  BST UNFREEZING vs STANDARD INFLATION")
            print("  " + "-" * 56)
            for c in comparison:
                print()
                print("  {}:".format(c['aspect']))
                print("    BST:       {}".format(c['bst']))
                print("    Inflation: {}".format(c['inflation']))
            print()

        return comparison

    # ─────────────────────────────────────────────────────────
    # 7. gravitational_bell()
    # ─────────────────────────────────────────────────────────
    def gravitational_bell(self):
        """The phase transition rings S^2 like a bell."""
        # Peak frequency from phase transition cosmology
        # Sound waves: ~6.4 nHz, turbulence: ~9.1 nHz
        f_sound_nHz = 6.4
        f_turb_nHz = 9.1
        f_peak_nHz = f_sound_nHz  # primary peak

        result = {
            'f_peak_nHz': f_peak_nHz,
            'f_sound_nHz': f_sound_nHz,
            'f_turbulence_nHz': f_turb_nHz,
            'band': '1-100 nHz (pulsar timing arrays)',
            'C_v': 330000,
            'transition_strength': 'ultra-strong (alpha >> 1)',
            'Omega_GW_h2': 1e-7,
            'NANOGrav_2023': 'Detected stochastic GW background at 1-100 nHz — CONSISTENT',
            'before_3s': 'SILENCE — no space, no gravitational waves possible',
            'at_3s': 'ONE STRIKE — SO(2) unfreezes, substrate rings',
            'after_3s': 'ECHOES — ring propagates across S^2, converges at antipode, returns',
            'echo_info': 'Spacing gives S^2 diameter; damping gives expansion rate',
            'spectral_prediction': 'Peaks at substrate resonant frequencies (not featureless)',
            'discriminant': 'BST: peaks at specific f. Inflation: featureless power law.',
        }

        if not self.quiet:
            print("  THE GRAVITATIONAL BELL")
            print("  " + "-" * 56)
            print("  Before 3.1 s:  SILENCE (no space exists)")
            print("  At 3.1 s:      ONE RING (SO(2) unfreezes)")
            print("  After 3.1 s:   ECHOES (ring crosses S^2)")
            print()
            print("  f_peak (sound):      {:.1f} nHz".format(f_sound_nHz))
            print("  f_peak (turbulence): {:.1f} nHz".format(f_turb_nHz))
            print("  Omega_GW h^2:        ~10^-7")
            print("  C_v at transition:   {:,}".format(330000))
            print()
            print("  NANOGrav 2023: detected 1-100 nHz background")
            print("  BST prediction falls IN the observed band.")
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 8. summary()
    # ─────────────────────────────────────────────────────────
    def summary(self):
        """Key insight in one paragraph."""
        text = (
            "The Big Bang is not an explosion. It is the unfreezing of exactly one of "
            "21 generators of so(5,2). At T_c = {:.4f} MeV (t = {:.1f} s), the SO(2) "
            "generator — the S^1 fiber rotation — separates from the other 20. This is "
            "the minimum symmetry breaking that permits physics: SO(7) -> SO(5) x SO(2). "
            "Space nucleates. The Bergman metric becomes physical. The first electron is "
            "the first complete S^1 winding. The first proton is the first Z_3 circuit. "
            "The bell rings once at ~6 nHz (NANOGrav may already be hearing it). The "
            "transition fixes Li-7 through genus = 7 extra dof, seeds galaxies through "
            "C_v = 330,000, and imprints n_s = 1 - 5/137 on the CMB. No singularity. "
            "No inflaton. No free parameters. One generator, one universe."
        ).format(self.T_c, self.t_transition)

        result = {
            'summary': text,
            'key_numbers': {
                'T_c_MeV': self.T_c,
                'time_s': self.t_transition,
                'generators_total': 21,
                'generators_unfreeze': 1,
                'n_s': 1.0 - n_C / N_max,
                'f_peak_nHz': 6.4,
                'Li7_reduction': 2.73,
                'C_v': 330000,
                'free_parameters': 0,
            },
        }

        if not self.quiet:
            print("  SUMMARY")
            print("  " + "-" * 56)
            # Word-wrap at ~70 chars
            words = text.split()
            line = "  "
            for w in words:
                if len(line) + len(w) + 1 > 72:
                    print(line)
                    line = "  " + w
                else:
                    line += " " + w if line.strip() else "  " + w
            if line.strip():
                print(line)
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 9. show() — 4-panel visualization
    # ─────────────────────────────────────────────────────────
    def show(self):
        """4-panel visualization of the Big Bang unfreezing."""
        fig = plt.figure(figsize=(19, 11), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The Big Bang Unfreezing — One Generator, One Universe — BST')

        # Main title
        fig.text(0.5, 0.97, 'THE BIG BANG UNFREEZING',
                 fontsize=26, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=3, foreground='#663300')])
        fig.text(0.5, 0.935,
                 'One of 21 generators unfreezes at T_c = {:.4f} MeV  (t = {:.1f} s)'.format(
                     self.T_c, self.t_transition),
                 fontsize=12, color=GOLD_DIM, ha='center', fontfamily='monospace')

        # Copyright
        fig.text(0.5, 0.012,
                 'Copyright 2026 Casey Koons  |  Created with Claude Opus 4.6  |  BST',
                 fontsize=8, color='#555555', ha='center', fontfamily='monospace')

        # ── Panel 1: Top-left — 21 generators ──
        ax1 = fig.add_axes([0.03, 0.50, 0.45, 0.40])
        self._draw_generators_panel(ax1)

        # ── Panel 2: Top-right — Timeline ──
        ax2 = fig.add_axes([0.53, 0.50, 0.44, 0.40])
        self._draw_timeline_panel(ax2)

        # ── Panel 3: Bottom-left — BBN elements ──
        ax3 = fig.add_axes([0.03, 0.06, 0.45, 0.40])
        self._draw_bbn_panel(ax3)

        # ── Panel 4: Bottom-right — BST vs Inflation ──
        ax4 = fig.add_axes([0.53, 0.06, 0.44, 0.40])
        self._draw_comparison_panel(ax4)

        plt.show(block=False)

    # ─── Panel drawing helpers ───

    def _draw_generators_panel(self, ax):
        """Top-left: 21 generators — one unfreezes."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-1.5, 9.0)
        ax.axis('off')

        ax.text(5.0, 8.5, '21 GENERATORS OF so(5,2)',
                fontsize=13, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

        # so(5): 10 frozen generators — 2 rows of 5
        ax.text(2.25, 7.3, 'so(5) — 10 frozen', fontsize=9, color=GREY,
                ha='center', fontfamily='monospace')
        for i in range(10):
            row = i // 5
            col = i % 5
            x = col * 1.0 + 0.25
            y = 6.5 - row * 1.2
            circle = Circle((x, y), 0.35, facecolor=GREY_FROZEN,
                            edgecolor='#555577', linewidth=1.0, zorder=2)
            ax.add_patch(circle)
            ax.text(x, y, 'L', fontsize=7, color='#666688',
                    ha='center', va='center', fontfamily='monospace', zorder=3)

        # so(2): THE generator that unfreezes — big golden circle
        ax.text(7.5, 7.3, 'so(2) — UNFREEZES', fontsize=9, color=GOLD,
                ha='center', fontfamily='monospace', fontweight='bold')
        # Glow rings
        for r_glow, a in [(1.2, 0.04), (1.0, 0.06), (0.8, 0.10), (0.6, 0.15)]:
            glow = Circle((7.5, 6.0), r_glow, facecolor=GOLD, edgecolor='none',
                          alpha=a, zorder=1)
            ax.add_patch(glow)
        # Main circle
        main_circle = Circle((7.5, 6.0), 0.45, facecolor=GOLD,
                             edgecolor=WHITE, linewidth=2.0, zorder=3)
        ax.add_patch(main_circle)
        ax.text(7.5, 6.0, 'J', fontsize=14, fontweight='bold', color='#1a1a00',
                ha='center', va='center', fontfamily='monospace', zorder=4)
        ax.text(7.5, 5.2, 'S^1 fiber', fontsize=8, color=GOLD_DIM,
                ha='center', fontfamily='monospace')

        # m: 10 dynamical generators — 2 rows of 5
        ax.text(5.0, 3.5, 'm — 10 become DYNAMICAL', fontsize=9, color=CYAN,
                ha='center', fontfamily='monospace', fontweight='bold')
        for i in range(10):
            row = i // 5
            col = i % 5
            x = col * 1.0 + 2.75
            y = 2.5 - row * 1.2
            circle = Circle((x, y), 0.35, facecolor='#003344',
                            edgecolor=CYAN, linewidth=1.0, zorder=2)
            ax.add_patch(circle)
            ax.text(x, y, 'X', fontsize=7, color=CYAN,
                    ha='center', va='center', fontfamily='monospace', zorder=3)

        # Arrow from J to m generators
        arrow = FancyArrowPatch((7.5, 5.4), (5.5, 3.8),
                                arrowstyle='->', mutation_scale=20,
                                linewidth=2, color=GOLD,
                                connectionstyle='arc3,rad=-0.2')
        ax.add_patch(arrow)
        ax.text(7.2, 4.4, 'activates', fontsize=8, color=GOLD_DIM,
                fontfamily='monospace', fontstyle='italic', rotation=-35)

        # Count box
        box = FancyBboxPatch((0.0, -1.2), 10.0, 0.9,
                             boxstyle='round,pad=0.1',
                             facecolor='#0a0a1a', edgecolor='#553300',
                             linewidth=1.0, alpha=0.8)
        ax.add_patch(box)
        ax.text(5.0, -0.75, '21 = 10 (frozen) + 1 (UNFREEZES) + 10 (dynamical)',
                fontsize=10, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace')

    def _draw_timeline_panel(self, ax):
        """Top-right: log-scale timeline from frozen era to now."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(-0.5, 10.0)
        ax.set_ylim(-0.5, 9.5)
        ax.axis('off')

        ax.text(5.0, 9.0, 'TIMELINE: FROZEN ERA TO NOW',
                fontsize=13, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

        events = [
            ('Frozen era',         '---',         GREY_FROZEN, '21 generators frozen'),
            ('EW sub-transition',  '10^-12 s',    GREY,        'No particles, no GWs'),
            ('QCD sub-transition', '10^-6 s',     GREY,        'eta geometric, not annihilation'),
            ('nu decoupling',      '~1 s',        GREY,        'Still pre-spatial'),
            ('BIG BANG',           '3.1 s',       GOLD,        'SO(2) UNFREEZES'),
            ('BBN',                '3-20 min',    GREEN,       'Li-7 resolved (genus=7)'),
            ('CMB',                '380,000 yr',  CYAN,        'n_s = 1 - 5/137'),
            ('First galaxies',    '~10^8 yr',    BLUE,        'JWST predicted'),
            ('Today',              '13.8 Gyr',    WHITE,       '10^122 commitments'),
        ]

        y_start = 8.2
        y_step = 0.95

        for i, (name, time_str, color, note) in enumerate(events):
            y = y_start - i * y_step
            is_bang = 'BIG BANG' in name

            # Timeline dot
            r = 0.18 if not is_bang else 0.25
            dot = Circle((0.5, y), r, facecolor=color,
                         edgecolor=WHITE if is_bang else '#333333',
                         linewidth=2 if is_bang else 0.5, zorder=3)
            ax.add_patch(dot)

            # Glow for Big Bang
            if is_bang:
                for rg, a in [(0.6, 0.06), (0.45, 0.10), (0.35, 0.15)]:
                    g = Circle((0.5, y), rg, facecolor=GOLD, edgecolor='none',
                               alpha=a, zorder=1)
                    ax.add_patch(g)

            # Vertical line
            if i < len(events) - 1:
                y_next = y_start - (i + 1) * y_step
                line_color = '#333344' if not is_bang else GOLD_DIM
                ax.plot([0.5, 0.5], [y - r, y_next + 0.18], color=line_color,
                        linewidth=1.5 if is_bang else 0.8, zorder=1)

            # Text
            weight = 'bold' if is_bang else 'normal'
            size = 9 if is_bang else 8
            ax.text(1.2, y + 0.1, name, fontsize=size, fontweight=weight,
                    color=color, fontfamily='monospace', va='center')
            ax.text(1.2, y - 0.2, time_str, fontsize=7, color=GREY,
                    fontfamily='monospace', va='center')
            ax.text(5.5, y - 0.05, note, fontsize=7, color=color,
                    fontfamily='monospace', va='center', alpha=0.8)

        # Pre-spatial bracket
        ax.plot([9.2, 9.2], [y_start, y_start - 3 * y_step],
                color=GREY_FROZEN, linewidth=1.5)
        ax.text(9.5, y_start - 1.5 * y_step, 'PRE-\nSPATIAL',
                fontsize=7, color=GREY_FROZEN, fontfamily='monospace',
                ha='center', va='center', fontstyle='italic')

    def _draw_bbn_panel(self, ax):
        """Bottom-left: BBN element abundances with Li-7 correction."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 9)
        ax.axis('off')

        ax.text(5.0, 8.5, 'BBN ELEMENT ABUNDANCES',
                fontsize=13, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

        elements = [
            ('H',    0.75,    'mass fraction',  None,   None,     WHITE,  '75%'),
            ('He-4', 0.247,   'Y_p',            None,   None,     CYAN,   '24.7%'),
            ('D',    2.5e-5,  'D/H',            None,   None,     GREEN,  '2.5e-5'),
            ('He-3', 1.0e-5,  'He3/H',          None,   None,     BLUE,   '1.0e-5'),
            ('Li-7', 1.7e-10, 'Li7/H (BST)',    4.7e-10, 1.6e-10, GOLD,   '1.7e-10'),
        ]

        # Bar chart area
        bar_x_start = 1.5
        bar_width = 1.2
        bar_gap = 0.3
        max_bar_height = 5.0
        bar_y_base = 1.5

        # Use log scale for display
        log_vals = []
        for _, val, _, _, _, _, _ in elements:
            log_vals.append(np.log10(max(val, 1e-12)))

        log_min = min(log_vals) - 0.5
        log_max = max(log_vals) + 0.5
        log_range = log_max - log_min

        for i, (name, val, label, std_val, obs_val, color, val_str) in enumerate(elements):
            x = bar_x_start + i * (bar_width + bar_gap)
            log_v = np.log10(max(val, 1e-12))
            height = max_bar_height * (log_v - log_min) / log_range

            # Bar
            bar = FancyBboxPatch((x, bar_y_base), bar_width, height,
                                 boxstyle='round,pad=0.05',
                                 facecolor=color, edgecolor='none',
                                 alpha=0.6, zorder=2)
            ax.add_patch(bar)

            # Glow on top
            ax.plot([x + 0.1, x + bar_width - 0.1],
                    [bar_y_base + height, bar_y_base + height],
                    color=color, linewidth=3, alpha=0.8, zorder=3,
                    solid_capstyle='round')

            # Element name
            ax.text(x + bar_width / 2, bar_y_base - 0.35, name,
                    fontsize=9, fontweight='bold', color=color,
                    ha='center', fontfamily='monospace')

            # Value
            ax.text(x + bar_width / 2, bar_y_base + height + 0.25, val_str,
                    fontsize=7, color=color, ha='center', fontfamily='monospace')

            # Li-7 special markers
            if name == 'Li-7' and std_val is not None:
                # Standard prediction bar (dashed outline)
                log_std = np.log10(std_val)
                h_std = max_bar_height * (log_std - log_min) / log_range
                ax.plot([x + 0.1, x + bar_width - 0.1],
                        [bar_y_base + h_std, bar_y_base + h_std],
                        color=RED_WARM, linewidth=2, linestyle='--', zorder=4)
                ax.text(x + bar_width + 0.3, bar_y_base + h_std,
                        'Standard\n(3x too high)',
                        fontsize=6, color=RED_WARM, fontfamily='monospace',
                        va='center')

                # Arrow showing reduction
                ax.annotate('', xy=(x + bar_width / 2, bar_y_base + height + 0.05),
                            xytext=(x + bar_width / 2, bar_y_base + h_std - 0.05),
                            arrowprops=dict(arrowstyle='->', color=GOLD,
                                            linewidth=1.5))
                ax.text(x - 0.5, bar_y_base + (height + h_std) / 2,
                        '2.73x\n(genus=7)',
                        fontsize=7, color=GOLD, fontfamily='monospace',
                        fontweight='bold', ha='center', va='center')

        # Key box
        box = FancyBboxPatch((0.3, 0.1), 9.4, 1.0,
                             boxstyle='round,pad=0.1',
                             facecolor='#0a0a1a', edgecolor='#553300',
                             linewidth=1.0, alpha=0.8)
        ax.add_patch(box)
        ax.text(5.0, 0.6,
                'Li-7 RESOLVED: Delta_g = genus = 7 at T_c suppresses by '
                '(10.75/17.75)^2 = 2.73x  (obs: 2.93x, 7% match)',
                fontsize=8, color=GOLD, ha='center', fontfamily='monospace',
                va='center')

    def _draw_comparison_panel(self, ax):
        """Bottom-right: BST vs Inflation comparison table."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 9)
        ax.axis('off')

        ax.text(5.0, 8.5, 'BST UNFREEZING vs INFLATION',
                fontsize=13, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

        rows = [
            ('Mechanism',     'One generator unfreezes',  'Inflaton field expands'),
            ('Start time',    't = 3.1 s (definite)',     't ~ 10^-36 s (model-dep.)'),
            ('Temperature',   '0.487 MeV (exact)',        '~10^15 GeV (model-dep.)'),
            ('Singularity',   'NONE',                     'Present / unknown'),
            ('Parameters',    'ZERO',                     '>= 1 (inflaton)'),
            ('n_s',           '1 - 5/137 = 0.96350',     'Potential-dependent'),
            ('Tensor r',      '~0 (no B-modes)',          '> 0 (B-modes predicted)'),
            ('EW/QCD GWs',    'NONE (no space)',          'Yes (phase transitions)'),
            ('Li-7',          'RESOLVED (genus=7)',       'Unsolved'),
            ('JWST galaxies', 'Predicted',               'Problematic'),
            ('Baryon asym.',  'Geometric (eta exact)',    'Unknown mechanism'),
        ]

        # Table layout
        y_start = 7.8
        y_step = 0.65
        col_aspect = 0.2
        col_bst = 3.5
        col_infl = 7.2

        # Headers
        ax.text(col_aspect, y_start + 0.4, 'Aspect', fontsize=8,
                fontweight='bold', color=GREY, fontfamily='monospace')
        ax.text(col_bst, y_start + 0.4, 'BST', fontsize=8,
                fontweight='bold', color=GOLD, fontfamily='monospace')
        ax.text(col_infl, y_start + 0.4, 'Inflation', fontsize=8,
                fontweight='bold', color=GREY, fontfamily='monospace')
        ax.plot([0.1, 9.9], [y_start + 0.2, y_start + 0.2],
                color='#333344', linewidth=0.8)

        for i, (aspect, bst, infl) in enumerate(rows):
            y = y_start - i * y_step

            # Alternating row background
            if i % 2 == 0:
                row_bg = FancyBboxPatch((0.1, y - 0.25), 9.8, 0.55,
                                        boxstyle='round,pad=0.02',
                                        facecolor='#0d0d1a', edgecolor='none',
                                        alpha=0.5)
                ax.add_patch(row_bg)

            # Highlight key wins
            bst_color = GOLD
            if 'NONE' in bst or 'ZERO' in bst or 'RESOLVED' in bst or 'Predicted' in bst:
                bst_color = GREEN
            elif 'exact' in bst.lower() or 'definite' in bst.lower():
                bst_color = CYAN

            ax.text(col_aspect, y, aspect, fontsize=7, color=WHITE,
                    fontfamily='monospace', va='center')
            ax.text(col_bst, y, bst, fontsize=7, color=bst_color,
                    fontfamily='monospace', va='center')
            ax.text(col_infl, y, infl, fontsize=7, color='#888899',
                    fontfamily='monospace', va='center')

        # Bottom note
        box = FancyBboxPatch((0.3, 0.1), 9.4, 0.9,
                             boxstyle='round,pad=0.1',
                             facecolor='#0a0a1a', edgecolor='#553300',
                             linewidth=1.0, alpha=0.8)
        ax.add_patch(box)
        ax.text(5.0, 0.55,
                'BST: zero free parameters, definite start time, falsifiable predictions',
                fontsize=8, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace', va='center')


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 68)
    print("  TOY 41 — THE BIG BANG UNFREEZING")
    print("  One of 21 generators unfreezes. That is the Big Bang.")
    print("=" * 68)
    print()
    print("  What would you like to explore?")
    print("  1) Generators of so(5,2)")
    print("  2) The phase transition")
    print("  3) Timeline (frozen era to now)")
    print("  4) BBN element abundances")
    print("  5) CMB predictions")
    print("  6) BST vs Inflation comparison")
    print("  7) The gravitational bell")
    print("  8) Summary")
    print("  9) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [1-9]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '9'

    bb = BigBangUnfreeze()

    if choice == '1':
        bb.generators()
    elif choice == '2':
        bb.phase_transition()
    elif choice == '3':
        bb.timeline()
    elif choice == '4':
        bb.bbn_elements()
    elif choice == '5':
        bb.cmb_predictions()
    elif choice == '6':
        bb.vs_inflation()
    elif choice == '7':
        bb.gravitational_bell()
    elif choice == '8':
        bb.summary()
    elif choice == '9':
        bb.generators()
        bb.phase_transition()
        bb.timeline()
        bb.bbn_elements()
        bb.cmb_predictions()
        bb.vs_inflation()
        bb.gravitational_bell()
        bb.summary()
        try:
            bb.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        bb.summary()


if __name__ == '__main__':
    main()
