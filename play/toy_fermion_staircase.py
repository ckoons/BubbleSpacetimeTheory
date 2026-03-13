#!/usr/bin/env python3
"""
THE FERMION STAIRCASE  --  Toy 51
==================================
All 12 fermion masses from nested domain embeddings D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5.

The BST fermion mass hierarchy is not arbitrary. Every charged lepton, quark,
and neutrino mass is determined by the Bergman geometry of the type-IV
bounded symmetric domain and its totally geodesic submanifolds:

  D_IV^1 (dim_R=2)  -- electron lives here (boundary excitation on Shilov S^4 x S^1)
  D_IV^3 (dim_R=6)  -- muon "sees" this embedding; ratio = (24/pi^2)^6 = 206.761
  D_IV^5 (dim_R=10) -- tau probes full domain; ratio = (7/3)^{10/3} above muon

Quark mass ratios from BST integers:
  m_s/m_d  = 4*n_C = 20           (inverse Cabibbo squared)
  m_t/m_c  = N_max - 1 = 136      (filled shell minus one)
  m_b/m_tau = genus/N_c = 7/3     (holomorphic curvature ratio)
  m_c/m_s  = N_max/dim_R = 137/10 (thermal-geometric bridge)
  m_d/m_u  = 13/6                 (Weinberg denominator / Casimir)

Light quarks:
  m_u = 3*sqrt(2) * m_e           (N_c * sqrt(N_w) * m_e)
  m_d = (13/6) * m_u              (Weinberg / Casimir * m_u)
  m_s = 20 * m_d = 130*sqrt(2)*m_e (4*n_C * m_d)

Neutrinos:
  m_nu_i = f_i * alpha^2 * m_e^2 / m_p   (boundary seesaw)
  f_1 = 0, f_2 = 7/12, f_3 = 10/3

CI Interface:
    from toy_fermion_staircase import FermionStaircase
    fs = FermionStaircase()
    fs.electron()           # base unit
    fs.muon()               # (24/pi^2)^6 ratio
    fs.tau()                # (7/3)^{10/3} above muon
    fs.light_quarks()       # u, d, s from BST integers
    fs.heavy_quarks()       # c, b, t from ratios
    fs.mass_ratios()        # all BST mass ratios
    fs.domain_embeddings()  # the three domains
    fs.complete_table()     # all 12 fermions
    fs.summary()            # key insight
    fs.show()               # 4-panel visualization

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
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges (B_2 root system)
n_C   = 5           # complex dimension of D_IV^5
C_2   = n_C + 1     # 6  Casimir eigenvalue
genus = n_C + 2     # 7  genus of D_IV^5
N_max = 137         # channel capacity (Haldane exclusion cap)
N_w   = 2           # weak isospin doublet dimension
GAMMA = 1920        # |S_5 x (Z_2)^4|
dim_R = 2 * n_C     # 10  real dimension of D_IV^5
alpha = 1.0 / 137.035999

# Physical masses in MeV
m_e_MeV = 0.51100   # electron mass
m_p_MeV = 938.272    # proton mass

# Domain volumes:  Vol(D_IV^k) = pi^k / (2^{k-1} * k!)
Vol_1 = np.pi                         # pi
Vol_3 = np.pi**3 / 24.0              # pi^3/24
Vol_5 = np.pi**5 / 1920.0            # pi^5/1920

# Bergman kernel ratios
K3_over_K1 = 24.0 / np.pi**2         # Vol_1/Vol_3 = 24/pi^2

# ──────────────────────────────────────────────────────────────────
#  Colors (dark theme)
# ──────────────────────────────────────────────────────────────────
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BRIGHT_GOLD = '#ffee44'
CYAN        = '#00ddff'
GREEN       = '#00ff88'
YELLOW      = '#ffee00'
ORANGE      = '#ff8800'
RED         = '#ff3344'
MAGENTA     = '#ff44cc'
WHITE       = '#eeeeff'
GREY        = '#666688'
SOFT_BLUE   = '#4488ff'
VIOLET      = '#aa44ff'
PINK        = '#ff88aa'

# Type colors for visualization
LEPTON_COLOR = CYAN
QUARK_COLOR  = ORANGE
NEUTRINO_COLOR = VIOLET


def _precision_color(pct):
    """Color by prediction quality."""
    ap = abs(pct)
    if ap < 1.0:
        return BRIGHT_GOLD
    elif ap < 2.0:
        return GOLD
    elif ap < 5.0:
        return GREEN
    elif ap < 15.0:
        return YELLOW
    else:
        return RED


# ══════════════════════════════════════════════════════════════════
#  Observed Fermion Masses (PDG 2024, MeV)
# ══════════════════════════════════════════════════════════════════
OBS = {
    # Charged leptons (MeV)
    'e':     0.51100,
    'mu':    105.6584,
    'tau':   1776.86,
    # Neutrinos (MeV): 1 eV = 1e-6 MeV
    'nu_1':  0.0,                  # m_1 = 0 (normal ordering)
    'nu_2':  0.00868e-6,           # sqrt(Delta m^2_21) = 0.00868 eV in MeV
    'nu_3':  0.0503e-6,            # sqrt(Delta m^2_31) = 0.0503 eV in MeV
    # Quarks (MS-bar at 2 GeV for u,d,s; MS-bar at m_q for c,b; pole for t)
    'u':     2.16,
    'd':     4.67,
    's':     93.4,
    'c':     1270.0,               # 1.270 GeV
    'b':     4180.0,               # 4.180 GeV
    't':     172690.0,             # 172.69 GeV
}


# ══════════════════════════════════════════════════════════════════
#  FermionStaircase Class
# ══════════════════════════════════════════════════════════════════
class FermionStaircase:
    """
    All fermion masses from the Bergman geometry of D_IV^5.

    The mass hierarchy arises from nested domain embeddings:
      D_IV^1 (electron) -> D_IV^3 (muon) -> D_IV^5 (tau)
    with quarks and neutrinos determined by BST integers
    (N_c, n_C, genus, N_max, C_2).

    Parameters
    ----------
    quiet : bool
        If False (default), print results when methods are called.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.m_e = m_e_MeV
        self.m_p = m_p_MeV
        self.alpha = alpha

    def _print(self, text):
        if not self.quiet:
            print(text)

    # ── 1. electron ────────────────────────────────────────────

    def electron(self):
        """
        The electron: base unit of the fermion mass hierarchy.

        In BST, m_e = m_p / (6*pi^5). The electron is a boundary
        excitation on the Shilov boundary S^4 x S^1.
        """
        m_e_bst = self.m_p / (6.0 * np.pi**5)
        obs = OBS['e']
        pct = 100.0 * (m_e_bst - obs) / obs

        result = {
            'name': 'electron',
            'symbol': 'e',
            'formula': 'm_p / (6*pi^5)',
            'bst_mass_MeV': m_e_bst,
            'observed_MeV': obs,
            'precision_pct': pct,
            'domain': 'D_IV^1',
            'dim_C': 1,
            'dim_R': 2,
            'note': 'Boundary excitation on Shilov boundary S^4 x S^1',
        }

        self._print(f"\n  ELECTRON  (the base unit)")
        self._print(f"  BST:  m_e = m_p / (6*pi^5) = {m_e_bst:.5f} MeV")
        self._print(f"  Obs:  {obs:.5f} MeV")
        self._print(f"  Precision: {pct:+.4f}%")

        return result

    # ── 2. muon ────────────────────────────────────────────────

    def muon(self):
        """
        The muon: m_mu/m_e = (24/pi^2)^6 = 206.761 (0.003%).

        The 6 = dim_R(D_IV^3), the real dimension of the submanifold.
        The 24/pi^2 = K_3(0,0)/K_1(0,0) is the Bergman kernel ratio.
        """
        ratio_bst = (24.0 / np.pi**2)**6
        m_mu_bst = ratio_bst * self.m_e
        obs = OBS['mu']
        ratio_obs = obs / self.m_e
        pct = 100.0 * (m_mu_bst - obs) / obs

        result = {
            'name': 'muon',
            'symbol': 'mu',
            'formula': '(24/pi^2)^6 * m_e',
            'ratio_formula': '(24/pi^2)^6',
            'ratio_bst': ratio_bst,
            'ratio_obs': ratio_obs,
            'bst_mass_MeV': m_mu_bst,
            'observed_MeV': obs,
            'precision_pct': pct,
            'domain': 'D_IV^3',
            'dim_C': 3,
            'dim_R': 6,
            'exponent': 6,
            'base': 24.0 / np.pi**2,
            'note': 'Exponent 6 = dim_R(D_IV^3). Base 24/pi^2 = Bergman kernel ratio.',
        }

        self._print(f"\n  MUON  (D_IV^1 -> D_IV^3 embedding)")
        self._print(f"  BST:  m_mu/m_e = (24/pi^2)^6 = {ratio_bst:.3f}")
        self._print(f"  Obs:  m_mu/m_e = {ratio_obs:.3f}")
        self._print(f"  BST mass: {m_mu_bst:.4f} MeV  (obs: {obs:.4f} MeV)")
        self._print(f"  Precision: {pct:+.4f}%")

        return result

    # ── 3. tau ─────────────────────────────────────────────────

    def tau(self):
        """
        The tau: m_tau/m_e = (24/pi^2)^6 * (7/3)^{10/3} = 3483.8 (0.19%).

        Two-step geometric derivation:
          Step 1 (e->mu): Volume Jacobian = (24/pi^2)^6
          Step 2 (mu->tau): Curvature ratio = (7/3)^{10/3}
        where 7/3 = genus/N_c and 10/3 = 2*n_C/N_c = dim_R/N_c.
        """
        mu_ratio = (24.0 / np.pi**2)**6
        tau_over_mu = (7.0 / 3.0)**(10.0 / 3.0)
        ratio_bst = mu_ratio * tau_over_mu
        m_tau_bst = ratio_bst * self.m_e
        obs = OBS['tau']
        ratio_obs = obs / self.m_e
        pct = 100.0 * (m_tau_bst - obs) / obs

        result = {
            'name': 'tau',
            'symbol': 'tau',
            'formula': '(24/pi^2)^6 * (7/3)^(10/3) * m_e',
            'ratio_formula': '(24/pi^2)^6 * (7/3)^(10/3)',
            'ratio_bst': ratio_bst,
            'ratio_obs': ratio_obs,
            'tau_over_mu_bst': tau_over_mu,
            'tau_over_mu_obs': obs / OBS['mu'],
            'bst_mass_MeV': m_tau_bst,
            'observed_MeV': obs,
            'precision_pct': pct,
            'domain': 'D_IV^5',
            'dim_C': 5,
            'dim_R': 10,
            'step1': '(24/pi^2)^6 = volume Jacobian',
            'step2': '(7/3)^(10/3) = curvature ratio',
            'note': '7/3 = genus/N_c (curvature). 10/3 = dim_R/N_c (dimension per color).',
        }

        self._print(f"\n  TAU  (D_IV^3 -> D_IV^5 embedding)")
        self._print(f"  BST:  m_tau/m_e = (24/pi^2)^6 * (7/3)^(10/3) = {ratio_bst:.1f}")
        self._print(f"  Obs:  m_tau/m_e = {ratio_obs:.1f}")
        self._print(f"  BST:  m_tau/m_mu = (7/3)^(10/3) = {tau_over_mu:.3f}  (obs: {obs / OBS['mu']:.3f})")
        self._print(f"  BST mass: {m_tau_bst:.2f} MeV  (obs: {obs:.2f} MeV)")
        self._print(f"  Precision: {pct:+.3f}%")

        return result

    # ── 4. light quarks ────────────────────────────────────────

    def light_quarks(self):
        """
        Light quark masses from BST integers:
          m_u = 3*sqrt(2) * m_e        (N_c * sqrt(N_w) * m_e)
          m_d = (13/6) * m_u           ((N_c+2*n_C)/(n_C+1) * m_u)
          m_s = 20 * m_d               (4*n_C * m_d)
        """
        # Up quark
        m_u_bst = N_c * np.sqrt(N_w) * self.m_e
        obs_u = OBS['u']
        pct_u = 100.0 * (m_u_bst - obs_u) / obs_u

        # Down quark: m_d = (13/6) * m_u = (13*sqrt(2)/2) * m_e
        m_d_bst = (13.0 / 6.0) * m_u_bst   # = (13*sqrt(2)/2) * m_e
        obs_d = OBS['d']
        pct_d = 100.0 * (m_d_bst - obs_d) / obs_d

        # Strange quark: m_s = 20 * m_d = 130*sqrt(2) * m_e
        m_s_bst = 4.0 * n_C * m_d_bst  # = 20 * m_d
        obs_s = OBS['s']
        pct_s = 100.0 * (m_s_bst - obs_s) / obs_s

        results = [
            {
                'name': 'up',
                'symbol': 'u',
                'formula': 'N_c * sqrt(2) * m_e = 3*sqrt(2) * m_e',
                'bst_mass_MeV': m_u_bst,
                'observed_MeV': obs_u,
                'precision_pct': pct_u,
                'origin': 'Color channels (N_c=3) x weak doublet (sqrt(2))',
                'note': 'Lightest colored particle; boundary excitation with color + weak charge',
            },
            {
                'name': 'down',
                'symbol': 'd',
                'formula': '(13/6) * m_u = (13*sqrt(2)/2) * m_e',
                'ratio_to_u': '13/6 = (N_c+2*n_C)/(n_C+1)',
                'bst_mass_MeV': m_d_bst,
                'observed_MeV': obs_d,
                'precision_pct': pct_d,
                'origin': 'Weinberg denominator (13) / Casimir (6)',
                'note': '13 = N_c+2*n_C (same as sin^2 theta_W = 3/13)',
            },
            {
                'name': 'strange',
                'symbol': 's',
                'formula': '20 * m_d = 130*sqrt(2) * m_e',
                'ratio_to_d': '4*n_C = 20 (= 1/sin^2 theta_C)',
                'bst_mass_MeV': m_s_bst,
                'observed_MeV': obs_s,
                'precision_pct': pct_s,
                'origin': 'Inverse Cabibbo squared: sin^2 theta_C = 1/20',
                'note': 'Cabibbo angle and mass ratio share same geometric origin',
            },
        ]

        self._print(f"\n  LIGHT QUARKS  (D_IV^1 boundary sector)")
        self._print(f"  Up:      m_u = 3*sqrt(2)*m_e = {m_u_bst:.3f} MeV  "
                     f"(obs: {obs_u:.2f} MeV, {pct_u:+.2f}%)")
        self._print(f"  Down:    m_d = (13/6)*m_u = {m_d_bst:.3f} MeV  "
                     f"(obs: {obs_d:.2f} MeV, {pct_d:+.2f}%)")
        self._print(f"  Strange: m_s = 20*m_d = {m_s_bst:.2f} MeV  "
                     f"(obs: {obs_s:.1f} MeV, {pct_s:+.2f}%)")
        self._print(f"  Chain: m_e --[3*sqrt(2)]--> m_u --[13/6]--> m_d --[20]--> m_s")

        return results

    # ── 5. heavy quarks ────────────────────────────────────────

    def heavy_quarks(self):
        """
        Heavy quark masses from BST ratios:
          m_c = m_s * N_max/dim_R = m_s * 137/10
          m_b = m_tau * genus/N_c = m_tau * 7/3
          m_t = m_c * (N_max - 1) = m_c * 136
        """
        # Strange mass (from light quarks chain)
        m_u_bst = N_c * np.sqrt(N_w) * self.m_e
        m_d_bst = (13.0 / 6.0) * m_u_bst
        m_s_bst = 4.0 * n_C * m_d_bst

        # Charm: m_c = m_s * N_max / dim_R = m_s * 137/10
        m_c_bst = m_s_bst * N_max / dim_R
        obs_c = OBS['c']
        pct_c = 100.0 * (m_c_bst - obs_c) / obs_c

        # Bottom: m_b = m_tau * genus/N_c = m_tau * 7/3
        m_tau_bst = (24.0 / np.pi**2)**6 * (7.0 / 3.0)**(10.0 / 3.0) * self.m_e
        m_b_bst = m_tau_bst * genus / N_c
        obs_b = OBS['b']
        pct_b = 100.0 * (m_b_bst - obs_b) / obs_b

        # Top: m_t = m_c * (N_max - 1) = m_c * 136
        m_t_bst = m_c_bst * (N_max - 1)
        obs_t = OBS['t']
        pct_t = 100.0 * (m_t_bst - obs_t) / obs_t

        results = [
            {
                'name': 'charm',
                'symbol': 'c',
                'formula': 'm_s * N_max/dim_R = m_s * 137/10',
                'ratio_formula': 'N_max / dim_R(D_IV^5) = 137/10',
                'bst_mass_MeV': m_c_bst,
                'observed_MeV': obs_c,
                'precision_pct': pct_c,
                'origin': 'Thermal-geometric bridge: N_max/dim_R',
                'note': 'Bridges geometric (dim_R) and thermal (N_max) sectors',
            },
            {
                'name': 'bottom',
                'symbol': 'b',
                'formula': 'm_tau * genus/N_c = m_tau * 7/3',
                'ratio_formula': 'genus / N_c = 7/3',
                'bst_mass_MeV': m_b_bst,
                'observed_MeV': obs_b,
                'precision_pct': pct_b,
                'origin': 'Holomorphic curvature ratio: kappa_1/kappa_5 = 7/3',
                'note': 'Third-gen SU(2) partners: b and tau linked by curvature',
            },
            {
                'name': 'top',
                'symbol': 't',
                'formula': 'm_c * (N_max - 1) = m_c * 136',
                'ratio_formula': 'N_max - 1 = 136',
                'bst_mass_MeV': m_t_bst,
                'observed_MeV': obs_t,
                'precision_pct': pct_t,
                'origin': 'Filled shell minus one: N_max - 1 = 136',
                'note': 'Top occupies all but one vacuum level relative to charm',
            },
        ]

        self._print(f"\n  HEAVY QUARKS  (full D_IV^5 sector)")
        self._print(f"  Charm:  m_c = m_s * 137/10 = {m_c_bst:.1f} MeV  "
                     f"(obs: {obs_c:.0f} MeV, {pct_c:+.2f}%)")
        self._print(f"  Bottom: m_b = m_tau * 7/3 = {m_b_bst:.1f} MeV  "
                     f"(obs: {obs_b:.0f} MeV, {pct_b:+.2f}%)")
        self._print(f"  Top:    m_t = m_c * 136 = {m_t_bst:.0f} MeV  "
                     f"(obs: {obs_t:.0f} MeV, {pct_t:+.2f}%)")

        return results

    # ── 6. mass ratios ─────────────────────────────────────────

    def mass_ratios(self):
        """
        All BST mass ratios with their integer/algebraic origins.
        """
        ratios = [
            {
                'ratio': 'm_mu / m_e',
                'formula': '(24/pi^2)^6',
                'value_bst': (24.0 / np.pi**2)**6,
                'value_obs': OBS['mu'] / OBS['e'],
                'precision_pct': 100.0 * ((24.0 / np.pi**2)**6 - OBS['mu'] / OBS['e']) / (OBS['mu'] / OBS['e']),
                'origin': 'Volume Jacobian of D_IV^1 -> D_IV^3 embedding',
                'integers': 'base = 24/pi^2 (Bergman kernel ratio), exp = 6 (dim_R of D_IV^3)',
            },
            {
                'ratio': 'm_tau / m_mu',
                'formula': '(7/3)^(10/3)',
                'value_bst': (7.0 / 3.0)**(10.0 / 3.0),
                'value_obs': OBS['tau'] / OBS['mu'],
                'precision_pct': 100.0 * ((7.0 / 3.0)**(10.0 / 3.0) - OBS['tau'] / OBS['mu']) / (OBS['tau'] / OBS['mu']),
                'origin': 'Curvature ratio of D_IV^3 -> D_IV^5 embedding',
                'integers': '7/3 = genus/N_c (curvature), 10/3 = dim_R/N_c (dim per color)',
            },
            {
                'ratio': 'm_tau / m_e',
                'formula': '(24/pi^2)^6 * (7/3)^(10/3)',
                'value_bst': (24.0 / np.pi**2)**6 * (7.0 / 3.0)**(10.0 / 3.0),
                'value_obs': OBS['tau'] / OBS['e'],
                'precision_pct': 100.0 * ((24.0 / np.pi**2)**6 * (7.0 / 3.0)**(10.0 / 3.0) - OBS['tau'] / OBS['e']) / (OBS['tau'] / OBS['e']),
                'origin': 'Two-step embedding: volume Jacobian + curvature ratio',
                'integers': 'Combined: D_IV^1 -> D_IV^3 -> D_IV^5',
            },
            {
                'ratio': 'm_d / m_u',
                'formula': '13/6',
                'value_bst': 13.0 / 6.0,
                'value_obs': OBS['d'] / OBS['u'],
                'precision_pct': 100.0 * (13.0 / 6.0 - OBS['d'] / OBS['u']) / (OBS['d'] / OBS['u']),
                'origin': 'Weinberg denominator over Casimir',
                'integers': '13 = N_c + 2*n_C, 6 = n_C + 1 = C_2',
            },
            {
                'ratio': 'm_s / m_d',
                'formula': '4*n_C = 20',
                'value_bst': 4.0 * n_C,
                'value_obs': OBS['s'] / OBS['d'],
                'precision_pct': 100.0 * (20.0 - OBS['s'] / OBS['d']) / (OBS['s'] / OBS['d']),
                'origin': 'Inverse Cabibbo squared: sin^2(theta_C) = 1/20',
                'integers': '4*n_C = 4*5 = 20',
            },
            {
                'ratio': 'm_c / m_s',
                'formula': 'N_max / dim_R = 137/10',
                'value_bst': N_max / dim_R,
                'value_obs': OBS['c'] / OBS['s'],
                'precision_pct': 100.0 * (N_max / dim_R - OBS['c'] / OBS['s']) / (OBS['c'] / OBS['s']),
                'origin': 'Thermal-geometric bridge',
                'integers': 'N_max = 137 (channel capacity), dim_R = 10',
            },
            {
                'ratio': 'm_b / m_tau',
                'formula': 'genus / N_c = 7/3',
                'value_bst': genus / N_c,
                'value_obs': OBS['b'] / OBS['tau'],
                'precision_pct': 100.0 * (genus / N_c - OBS['b'] / OBS['tau']) / (OBS['b'] / OBS['tau']),
                'origin': 'Holomorphic curvature ratio',
                'integers': '7 = genus = n_C+2, 3 = N_c (colors)',
            },
            {
                'ratio': 'm_b / m_c',
                'formula': 'dim_R / N_c = 10/3',
                'value_bst': dim_R / N_c,
                'value_obs': OBS['b'] / OBS['c'],
                'precision_pct': 100.0 * (dim_R / N_c - OBS['b'] / OBS['c']) / (OBS['b'] / OBS['c']),
                'origin': 'Real dimension over color number',
                'integers': '10 = dim_R(D_IV^5), 3 = N_c',
            },
            {
                'ratio': 'm_t / m_c',
                'formula': 'N_max - 1 = 136',
                'value_bst': N_max - 1.0,
                'value_obs': OBS['t'] / OBS['c'],
                'precision_pct': 100.0 * (136.0 - OBS['t'] / OBS['c']) / (OBS['t'] / OBS['c']),
                'origin': 'Filled shell minus one',
                'integers': 'N_max - 1 = 137 - 1 = 136',
            },
            {
                'ratio': 'm_p / m_e',
                'formula': '6*pi^5',
                'value_bst': 6.0 * np.pi**5,
                'value_obs': m_p_MeV / m_e_MeV,
                'precision_pct': 100.0 * (6.0 * np.pi**5 - m_p_MeV / m_e_MeV) / (m_p_MeV / m_e_MeV),
                'origin': 'Yang-Mills mass gap: C_2 * pi^{n_C}',
                'integers': 'C_2 = 6, pi^5 from Bergman volume',
            },
        ]

        self._print(f"\n  BST MASS RATIOS  (all from geometry)")
        self._print(f"  {'Ratio':<18} {'Formula':<28} {'BST':>10} {'Obs':>10} {'Error':>10}")
        self._print(f"  {'-'*76}")
        for r in ratios:
            self._print(f"  {r['ratio']:<18} {r['formula']:<28} "
                         f"{r['value_bst']:>10.3f} {r['value_obs']:>10.3f} "
                         f"{r['precision_pct']:>+9.3f}%")

        return ratios

    # ── 7. domain embeddings ───────────────────────────────────

    def domain_embeddings(self):
        """
        The three domains D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5 and what each generation sees.
        """
        domains = {
            'D_IV^1': {
                'dim_C': 1,
                'dim_R': 2,
                'volume': Vol_1,
                'volume_formula': 'pi',
                'bergman_kernel_origin': 1.0 / Vol_1,
                'particles': ['electron (boundary excitation)'],
                'generation': 1,
                'description': 'Minimal domain. The electron is a boundary '
                               'excitation on the Shilov boundary S^4 x S^1.',
            },
            'D_IV^3': {
                'dim_C': 3,
                'dim_R': 6,
                'volume': Vol_3,
                'volume_formula': 'pi^3/24',
                'bergman_kernel_origin': 1.0 / Vol_3,
                'particles': ['muon', 'strange quark (via Cabibbo)'],
                'generation': 2,
                'description': 'Second generation sees D_IV^3 embedding. '
                               'Muon mass ratio = (K_3/K_1)^6 = (24/pi^2)^6.',
            },
            'D_IV^5': {
                'dim_C': 5,
                'dim_R': 10,
                'volume': Vol_5,
                'volume_formula': 'pi^5/1920',
                'bergman_kernel_origin': 1.0 / Vol_5,
                'particles': ['tau', 'top quark', 'bottom quark', 'all color channels active'],
                'generation': 3,
                'description': 'Third generation probes the full domain. '
                               'Curvature ratio genus/N_c = 7/3 stamps b/tau and tau/mu.',
            },
            'embedding_chain': 'D_IV^1 --> D_IV^3 --> D_IV^5',
            'volume_ratios': {
                'Vol_1/Vol_3': Vol_1 / Vol_3,
                'formula_1_3': '24/pi^2',
                'Vol_3/Vol_5': Vol_3 / Vol_5,
                'Vol_1/Vol_5': Vol_1 / Vol_5,
                'formula_1_5': '1920/pi^4',
            },
            'key_insight': 'Each generation corresponds to a totally geodesic '
                           'submanifold. Mass ratios = Bergman geometry of the embedding.',
        }

        self._print(f"\n  DOMAIN EMBEDDINGS  (the three submanifolds)")
        self._print(f"  D_IV^1:  dim_C=1, dim_R=2,  Vol = pi = {Vol_1:.4f}")
        self._print(f"  D_IV^3:  dim_C=3, dim_R=6,  Vol = pi^3/24 = {Vol_3:.6f}")
        self._print(f"  D_IV^5:  dim_C=5, dim_R=10, Vol = pi^5/1920 = {Vol_5:.6f}")
        self._print(f"  Volume ratio K_3/K_1 = 24/pi^2 = {24.0 / np.pi**2:.6f}")
        self._print(f"  Embedding chain: D_IV^1 -> D_IV^3 -> D_IV^5")

        return domains

    # ── 8. complete table ──────────────────────────────────────

    def complete_table(self):
        """
        All 12 fermion masses: 3 charged leptons, 3 neutrinos, 6 quarks.
        BST predictions vs observed.
        """
        # Build all masses
        # Charged leptons
        m_e_bst = self.m_p / (6.0 * np.pi**5)
        mu_ratio = (24.0 / np.pi**2)**6
        m_mu_bst = mu_ratio * m_e_MeV  # use exact m_e for consistency
        tau_ratio = mu_ratio * (7.0 / 3.0)**(10.0 / 3.0)
        m_tau_bst = tau_ratio * m_e_MeV

        # Light quarks
        m_u_bst = N_c * np.sqrt(N_w) * m_e_MeV
        m_d_bst = (13.0 / 6.0) * m_u_bst        # m_d = (13/6) * m_u
        m_s_bst = 4.0 * n_C * m_d_bst            # m_s = 20 * m_d

        # Heavy quarks
        m_c_bst = m_s_bst * N_max / dim_R
        m_b_bst = m_tau_bst * genus / N_c
        m_t_bst = m_c_bst * (N_max - 1)

        # Neutrinos (in MeV)
        nu_base = alpha**2 * m_e_MeV**2 / m_p_MeV  # base seesaw scale in MeV
        m_nu1_bst = 0.0
        m_nu2_bst = (7.0 / 12.0) * nu_base
        m_nu3_bst = (10.0 / 3.0) * nu_base

        fermions = [
            # Charged leptons
            {
                'name': 'electron', 'symbol': 'e', 'type': 'charged_lepton',
                'generation': 1, 'charge': -1,
                'formula': 'm_p / (6*pi^5)',
                'bst_mass_MeV': m_e_bst,
                'observed_MeV': OBS['e'],
                'precision_pct': 100.0 * (m_e_bst - OBS['e']) / OBS['e'],
            },
            {
                'name': 'muon', 'symbol': 'mu', 'type': 'charged_lepton',
                'generation': 2, 'charge': -1,
                'formula': '(24/pi^2)^6 * m_e',
                'bst_mass_MeV': m_mu_bst,
                'observed_MeV': OBS['mu'],
                'precision_pct': 100.0 * (m_mu_bst - OBS['mu']) / OBS['mu'],
            },
            {
                'name': 'tau', 'symbol': 'tau', 'type': 'charged_lepton',
                'generation': 3, 'charge': -1,
                'formula': '(24/pi^2)^6 * (7/3)^(10/3) * m_e',
                'bst_mass_MeV': m_tau_bst,
                'observed_MeV': OBS['tau'],
                'precision_pct': 100.0 * (m_tau_bst - OBS['tau']) / OBS['tau'],
            },
            # Neutrinos
            {
                'name': 'nu_e', 'symbol': 'nu_1', 'type': 'neutrino',
                'generation': 1, 'charge': 0,
                'formula': '0 (exactly)',
                'bst_mass_MeV': m_nu1_bst,
                'observed_MeV': OBS['nu_1'],
                'precision_pct': 0.0,
            },
            {
                'name': 'nu_mu', 'symbol': 'nu_2', 'type': 'neutrino',
                'generation': 2, 'charge': 0,
                'formula': '(7/12) * alpha^2 * m_e^2/m_p',
                'bst_mass_MeV': m_nu2_bst,
                'observed_MeV': OBS['nu_2'],
                'precision_pct': 100.0 * (m_nu2_bst - OBS['nu_2']) / OBS['nu_2'] if OBS['nu_2'] > 0 else 0.0,
            },
            {
                'name': 'nu_tau', 'symbol': 'nu_3', 'type': 'neutrino',
                'generation': 3, 'charge': 0,
                'formula': '(10/3) * alpha^2 * m_e^2/m_p',
                'bst_mass_MeV': m_nu3_bst,
                'observed_MeV': OBS['nu_3'],
                'precision_pct': 100.0 * (m_nu3_bst - OBS['nu_3']) / OBS['nu_3'] if OBS['nu_3'] > 0 else 0.0,
            },
            # Quarks
            {
                'name': 'up', 'symbol': 'u', 'type': 'quark',
                'generation': 1, 'charge': 2.0/3,
                'formula': '3*sqrt(2) * m_e',
                'bst_mass_MeV': m_u_bst,
                'observed_MeV': OBS['u'],
                'precision_pct': 100.0 * (m_u_bst - OBS['u']) / OBS['u'],
            },
            {
                'name': 'down', 'symbol': 'd', 'type': 'quark',
                'generation': 1, 'charge': -1.0/3,
                'formula': '(13/6) * m_u',
                'bst_mass_MeV': m_d_bst,
                'observed_MeV': OBS['d'],
                'precision_pct': 100.0 * (m_d_bst - OBS['d']) / OBS['d'],
            },
            {
                'name': 'strange', 'symbol': 's', 'type': 'quark',
                'generation': 2, 'charge': -1.0/3,
                'formula': '20 * m_d = 130*sqrt(2)*m_e',
                'bst_mass_MeV': m_s_bst,
                'observed_MeV': OBS['s'],
                'precision_pct': 100.0 * (m_s_bst - OBS['s']) / OBS['s'],
            },
            {
                'name': 'charm', 'symbol': 'c', 'type': 'quark',
                'generation': 2, 'charge': 2.0/3,
                'formula': 'm_s * 137/10',
                'bst_mass_MeV': m_c_bst,
                'observed_MeV': OBS['c'],
                'precision_pct': 100.0 * (m_c_bst - OBS['c']) / OBS['c'],
            },
            {
                'name': 'bottom', 'symbol': 'b', 'type': 'quark',
                'generation': 3, 'charge': -1.0/3,
                'formula': 'm_tau * 7/3',
                'bst_mass_MeV': m_b_bst,
                'observed_MeV': OBS['b'],
                'precision_pct': 100.0 * (m_b_bst - OBS['b']) / OBS['b'],
            },
            {
                'name': 'top', 'symbol': 't', 'type': 'quark',
                'generation': 3, 'charge': 2.0/3,
                'formula': 'm_c * 136',
                'bst_mass_MeV': m_t_bst,
                'observed_MeV': OBS['t'],
                'precision_pct': 100.0 * (m_t_bst - OBS['t']) / OBS['t'],
            },
        ]

        self._print(f"\n  COMPLETE FERMION TABLE  (12 fermions, zero free parameters)")
        self._print(f"  {'Name':<12} {'Formula':<32} {'BST (MeV)':>14} {'Obs (MeV)':>14} {'Error':>10}")
        self._print(f"  {'-'*82}")
        for f in fermions:
            bst_str = f'{f["bst_mass_MeV"]:.6g}'
            obs_str = f'{f["observed_MeV"]:.6g}'
            self._print(f"  {f['name']:<12} {f['formula']:<32} {bst_str:>14} {obs_str:>14} "
                         f"{f['precision_pct']:>+9.3f}%")

        return fermions

    # ── 9. summary ─────────────────────────────────────────────

    def summary(self):
        """Key insight: the fermion mass hierarchy is geometry, not tuning."""
        table = self.complete_table() if self.quiet else None
        if table is None:
            # Build quietly for stats
            old_q = self.quiet
            self.quiet = True
            table = self.complete_table()
            self.quiet = old_q

        # Exclude nu_1 (m=0) from precision stats
        precs = [abs(f['precision_pct']) for f in table
                 if f['observed_MeV'] > 0 and f['symbol'] != 'nu_1']
        median_err = np.median(precs)
        n_sub1 = sum(1 for p in precs if p < 1.0)
        n_sub2 = sum(1 for p in precs if p < 2.0)
        best = min(precs)
        worst = max(precs)

        result = {
            'title': 'The Fermion Staircase',
            'n_fermions': 12,
            'n_predictions': len(precs),
            'median_error_pct': median_err,
            'best_precision_pct': best,
            'worst_precision_pct': worst,
            'n_sub_1pct': n_sub1,
            'n_sub_2pct': n_sub2,
            'free_parameters': 0,
            'key_insight': (
                'The fermion mass hierarchy spans 12 orders of magnitude '
                '(from nu_1 = 0 to top = 173 GeV), yet every mass is determined '
                'by the Bergman geometry of D_IV^5 and its submanifolds. '
                'The integers N_c=3, n_C=5, genus=7, N_max=137 and the '
                'domain volumes fix ALL fermion masses with zero free parameters. '
                'Median precision: {:.2f}%.'.format(median_err)
            ),
            'structure': (
                'Leptons: D_IV^1 -> D_IV^3 -> D_IV^5 (volume Jacobian + curvature). '
                'Quarks: BST integers (Cabibbo, Weinberg, Casimir, genus). '
                'Neutrinos: boundary seesaw alpha^2 * m_e^2/m_p.'
            ),
        }

        self._print(f"\n  === THE FERMION STAIRCASE ===")
        self._print(f"  {result['key_insight']}")
        self._print(f"  {result['structure']}")
        self._print(f"  {n_sub1}/{len(precs)} predictions below 1%, "
                     f"{n_sub2}/{len(precs)} below 2%")

        return result

    # ── 10. show (visualization) ───────────────────────────────

    def show(self):
        """
        4-panel visualization:
          Top-left:     Mass staircase (log scale)
          Top-right:    Mass ratios with BST formulas
          Bottom-left:  Domain embedding diagram
          Bottom-right: Precision table
        """
        # Build data
        old_q = self.quiet
        self.quiet = True
        table = self.complete_table()
        ratios = self.mass_ratios()
        self.quiet = old_q

        fig = plt.figure(figsize=(19, 13), facecolor=BG)
        fig.canvas.manager.set_window_title('The Fermion Staircase -- BST Toy 51')

        # Title
        fig.text(0.50, 0.975, 'THE FERMION STAIRCASE',
                 fontsize=28, fontweight='bold', color=GOLD,
                 ha='center', va='top', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=3, foreground='#332200')])
        fig.text(0.50, 0.945,
                 'All fermion masses from nested domain embeddings  '
                 'D_IV^1  \u2282  D_IV^3  \u2282  D_IV^5',
                 fontsize=12, color=GOLD_DIM, ha='center', va='top',
                 fontfamily='monospace')

        gs = GridSpec(2, 2, figure=fig,
                      left=0.05, right=0.96, top=0.92, bottom=0.06,
                      hspace=0.32, wspace=0.25)

        ax_staircase = fig.add_subplot(gs[0, 0])
        ax_ratios    = fig.add_subplot(gs[0, 1])
        ax_domains   = fig.add_subplot(gs[1, 0])
        ax_table     = fig.add_subplot(gs[1, 1])

        self._draw_staircase(ax_staircase, table)
        self._draw_ratios(ax_ratios, ratios)
        self._draw_domains(ax_domains)
        self._draw_precision_table(ax_table, table)

        # Footer
        fig.text(0.50, 0.018,
                 'BST: N_c=%d  n_C=%d  genus=%d  N_max=%d  C\u2082=%d  '
                 '|  Zero free parameters  |  Casey Koons 2026  |  Claude Opus 4.6'
                 % (N_c, n_C, genus, N_max, C_2),
                 fontsize=9, color=GREY, ha='center', va='bottom',
                 fontfamily='monospace')

        plt.show()

    # ── Drawing helpers ────────────────────────────────────────

    def _draw_staircase(self, ax, table):
        """Top-left: mass staircase on log scale, colored by type."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Mass Staircase  (log scale)',
                     fontsize=14, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)

        # Filter to fermions with m > 0, sort by mass
        visible = [f for f in table if f['bst_mass_MeV'] > 0]
        visible.sort(key=lambda f: f['bst_mass_MeV'])

        type_colors = {
            'charged_lepton': CYAN,
            'neutrino': VIOLET,
            'quark': ORANGE,
        }
        type_labels_drawn = set()

        x_pos = np.arange(len(visible))
        for i, f in enumerate(visible):
            mass = f['bst_mass_MeV']
            col = type_colors.get(f['type'], WHITE)
            label = f['type'].replace('_', ' ') if f['type'] not in type_labels_drawn else None
            if label:
                type_labels_drawn.add(f['type'])

            # Draw step
            ax.bar(i, mass, width=0.7, color=col, alpha=0.75, label=label,
                   edgecolor=col, linewidth=0.5, zorder=2)

            # Label
            ax.text(i, mass * 1.4, f['symbol'], fontsize=8, color=WHITE,
                    ha='center', va='bottom', fontfamily='monospace',
                    fontweight='bold', rotation=45,
                    path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

        ax.set_yscale('log')
        ax.set_ylabel('Mass (MeV)', fontsize=10, color=GOLD_DIM,
                      fontfamily='monospace')
        ax.set_xticks([])
        ax.tick_params(colors=GREY, which='both')
        ax.spines['bottom'].set_color(GREY)
        ax.spines['left'].set_color(GREY)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Add generation bands
        ax.axhspan(0, 1e-3, alpha=0.03, color=VIOLET)
        ax.axhspan(1e-3, 1e3, alpha=0.03, color=CYAN)
        ax.axhspan(1e3, 1e6, alpha=0.03, color=ORANGE)

        leg = ax.legend(loc='upper left', fontsize=8, facecolor=DARK_PANEL,
                        edgecolor=GREY, labelcolor=WHITE, framealpha=0.9)

    def _draw_ratios(self, ax, ratios):
        """Top-right: mass ratios with BST formulas annotated."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('BST Mass Ratios  (integer formulas)',
                     fontsize=14, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)

        # Select key ratios for display
        display_ratios = ratios[:9]  # all except m_p/m_e (already well known)

        y_pos = np.arange(len(display_ratios))
        names = [r['ratio'] for r in display_ratios]
        bst_vals = [r['value_bst'] for r in display_ratios]
        obs_vals = [r['value_obs'] for r in display_ratios]
        formulas = [r['formula'] for r in display_ratios]
        precs = [r['precision_pct'] for r in display_ratios]

        # Horizontal bars for BST value
        for i in range(len(display_ratios)):
            pcol = _precision_color(precs[i])
            # normalize bar width to max ratio for visual
            bar_w = bst_vals[i] / max(bst_vals) * 0.85
            ax.barh(i, bar_w, height=0.5, color=pcol, alpha=0.35, zorder=1)

            # Formula annotation
            ax.text(0.88, i, formulas[i], fontsize=8, color=pcol,
                    ha='left', va='center', fontfamily='monospace',
                    fontweight='bold', transform=ax.get_yaxis_transform())

            # Precision
            ax.text(0.02, i + 0.22, f'{precs[i]:+.3f}%', fontsize=7, color=pcol,
                    ha='left', va='center', fontfamily='monospace',
                    transform=ax.get_yaxis_transform())

        ax.set_yticks(y_pos)
        ax.set_yticklabels(names, fontsize=9, color=WHITE, fontfamily='monospace')
        ax.set_xlim(0, 1)
        ax.set_xticks([])
        ax.tick_params(colors=GREY, which='both')
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_color(GREY)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.invert_yaxis()

    def _draw_domains(self, ax):
        """Bottom-left: nested domain embedding diagram."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Domain Embeddings  D_IV^k',
                     fontsize=14, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-1.8, 1.8)
        ax.set_aspect('equal')
        ax.axis('off')

        # Three nested circles
        domains = [
            ('D_IV^5', 1.5, ORANGE, 0.12, 'dim_R=10\ngenus=7\nVol=pi^5/1920',
             'Gen 3: tau, t, b'),
            ('D_IV^3', 0.95, CYAN, 0.15, 'dim_R=6\nVol=pi^3/24',
             'Gen 2: mu, s, c'),
            ('D_IV^1', 0.45, GREEN, 0.20, 'dim_R=2\nVol=pi',
             'Gen 1: e, u, d'),
        ]

        for name, radius, color, alph, info, particles in domains:
            circ = Circle((0, 0), radius, fill=False, edgecolor=color,
                         linewidth=2.5, alpha=0.8, linestyle='-', zorder=2)
            ax.add_patch(circ)

            # Glow
            glow = Circle((0, 0), radius, fill=True, facecolor=color,
                          alpha=alph * 0.3, zorder=1)
            ax.add_patch(glow)

            # Domain label
            ax.text(radius + 0.08, radius * 0.3, name, fontsize=11, color=color,
                    fontfamily='monospace', fontweight='bold', va='center',
                    path_effects=[pe.withStroke(linewidth=2, foreground=BG)])

            # Info text
            ax.text(radius + 0.08, radius * 0.3 - 0.25, info, fontsize=7,
                    color=color, fontfamily='monospace', alpha=0.7, va='top',
                    linespacing=1.3)

            # Particles
            ax.text(-radius + 0.05, -radius * 0.4, particles, fontsize=7,
                    color=color, fontfamily='monospace', alpha=0.8, va='center',
                    path_effects=[pe.withStroke(linewidth=1.5, foreground=BG)])

        # Arrows showing embedding steps
        arrow_props = dict(arrowstyle='->', color=GOLD_DIM, lw=1.5,
                          connectionstyle='arc3,rad=0.3')
        ax.annotate('', xy=(0.45, -0.65), xytext=(0.95, -0.95),
                    arrowprops=arrow_props)
        ax.text(0.85, -0.88, '(24/pi^2)^6', fontsize=7, color=GOLD_DIM,
                fontfamily='monospace', ha='center')

        ax.annotate('', xy=(0.95, -1.15), xytext=(1.50, -1.35),
                    arrowprops=arrow_props)
        ax.text(1.45, -1.32, '(7/3)^(10/3)', fontsize=7, color=GOLD_DIM,
                fontfamily='monospace', ha='center')

        # Central point (origin = Bergman kernel peak)
        ax.plot(0, 0, 'o', color=BRIGHT_GOLD, markersize=6, zorder=5)
        ax.text(0, -0.12, 'origin', fontsize=7, color=BRIGHT_GOLD,
                ha='center', fontfamily='monospace')

    def _draw_precision_table(self, ax, table):
        """Bottom-right: precision table for all fermions."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Precision Table  (BST vs Observed)',
                     fontsize=14, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        y = 0.95
        dy = 0.063

        # Header
        cols = [
            (0.02, 'Fermion', 'left'),
            (0.22, 'BST Formula', 'left'),
            (0.62, 'BST', 'right'),
            (0.78, 'Obs', 'right'),
            (0.95, 'Error', 'right'),
        ]
        for xp, txt, ha in cols:
            ax.text(xp, y, txt, fontsize=8, color=GOLD_DIM, ha=ha,
                    fontfamily='monospace', fontweight='bold')
        y -= 0.015
        ax.plot([0.01, 0.99], [y, y], color=GREY, lw=0.5, alpha=0.5)
        y -= dy * 0.5

        type_colors = {
            'charged_lepton': CYAN,
            'neutrino': VIOLET,
            'quark': ORANGE,
        }

        current_type = None
        for f in table:
            # Section divider
            if f['type'] != current_type:
                current_type = f['type']
                label = current_type.replace('_', ' ').upper() + 'S'
                ax.text(0.02, y, label, fontsize=6, color=GREY,
                        fontfamily='monospace', style='italic')
                y -= dy * 0.5

            col = type_colors.get(f['type'], WHITE)
            pcol = _precision_color(f['precision_pct'])

            # Format mass strings
            mass_bst = f['bst_mass_MeV']
            mass_obs = f['observed_MeV']
            if mass_bst < 0.001:
                bst_str = f'{mass_bst * 1e6:.1f} eV' if mass_bst > 0 else '0'
                obs_str = f'{mass_obs * 1e6:.1f} eV' if mass_obs > 0 else '<0.009 eV'
            elif mass_bst < 1.0:
                bst_str = f'{mass_bst:.5f}'
                obs_str = f'{mass_obs:.5f}'
            elif mass_bst < 1000:
                bst_str = f'{mass_bst:.2f}'
                obs_str = f'{mass_obs:.2f}'
            else:
                bst_str = f'{mass_bst:.0f}'
                obs_str = f'{mass_obs:.0f}'

            # Truncate formula for display
            formula_disp = f['formula'][:22]

            ax.text(0.02, y, f['symbol'], fontsize=8, color=col,
                    ha='left', fontfamily='monospace', fontweight='bold')
            ax.text(0.22, y, formula_disp, fontsize=6.5, color=WHITE,
                    ha='left', fontfamily='monospace', alpha=0.8)
            ax.text(0.62, y, bst_str, fontsize=7.5, color=WHITE,
                    ha='right', fontfamily='monospace')
            ax.text(0.78, y, obs_str, fontsize=7.5, color=GREY,
                    ha='right', fontfamily='monospace')

            if f['symbol'] == 'nu_1':
                ax.text(0.95, y, 'exact', fontsize=7.5, color=GREEN,
                        ha='right', fontfamily='monospace', fontweight='bold')
            else:
                ax.text(0.95, y, f'{f["precision_pct"]:+.2f}%', fontsize=7.5,
                        color=pcol, ha='right', fontfamily='monospace',
                        fontweight='bold')

            y -= dy

        # Summary line
        y -= dy * 0.3
        ax.plot([0.01, 0.99], [y + dy * 0.3, y + dy * 0.3],
                color=GREY, lw=0.5, alpha=0.3)
        precs = [abs(f['precision_pct']) for f in table
                 if f['observed_MeV'] > 0 and f['symbol'] != 'nu_1']
        med = np.median(precs)
        ax.text(0.50, y - dy * 0.1,
                f'Median error: {med:.2f}%  |  '
                f'12 fermions, 0 free parameters',
                fontsize=8, color=BRIGHT_GOLD, ha='center',
                fontfamily='monospace', style='italic')


# ══════════════════════════════════════════════════════════════════
#  Main Entry Point
# ══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the Fermion Staircase."""
    fs = FermionStaircase(quiet=False)

    menu = """
  ============================================
   THE FERMION STAIRCASE  --  BST Toy 51
  ============================================
   All fermion masses from D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5

   1. Electron (base unit)
   2. Muon (D_IV^3 embedding)
   3. Tau (D_IV^5 embedding)
   4. Light quarks (u, d, s)
   5. Heavy quarks (c, b, t)
   6. Mass ratios (BST formulas)
   7. Domain embeddings
   8. Complete table (all 12 fermions)
   9. Summary
   0. Show visualization (4-panel)
   q. Quit
  ============================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            fs.electron()
        elif choice == '2':
            fs.muon()
        elif choice == '3':
            fs.tau()
        elif choice == '4':
            fs.light_quarks()
        elif choice == '5':
            fs.heavy_quarks()
        elif choice == '6':
            fs.mass_ratios()
        elif choice == '7':
            fs.domain_embeddings()
        elif choice == '8':
            fs.complete_table()
        elif choice == '9':
            fs.summary()
        elif choice == '0':
            fs.show()
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
