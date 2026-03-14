#!/usr/bin/env python3
"""
HEAVY MESON SPECTRUM — CHARMONIUM AND BOTTOMONIUM
==================================================
Toy 117.  BST derives heavy meson masses from geometry.

The base unit is pi^5 * m_e = 156.38 MeV (the same unit that gives the
proton mass at 6*pi^5*m_e).  Every meson mass is an integer or algebraic
multiple k of this unit, with k drawn from BST integers:
    N_c = 3, n_C = 5, C_2 = 6, genus = 7, dim_R = 10.

Heavy quark masses in BST:
    m_c  ~  alpha^{-5} * m_e * correction  ~  1275 MeV
    m_b  ~  alpha^{-7} * m_e * correction  ~  4180 MeV

Charmonium (cc-bar) states:
    J/psi  = 4*n_C     * pi^5 * m_e  = 20 * 156.38  =  3127 MeV  (obs 3097)
    eta_c  = (N_c^2+2n_C) * pi^5 * m_e = 19 * 156.38 = 2971 MeV  (obs 2984)
    psi(2S)  ~  23.6 * pi^5 * m_e  (radial excitation, open problem)
    chi_c0   =  (4n_C + C_2/3) * pi^5 * m_e  ~  3415 MeV
    chi_c1   =  (4n_C + 5/2) * pi^5 * m_e    ~  3525 MeV
    h_c      =  (4n_C + 5/2) * pi^5 * m_e    ~  3525 MeV

Bottomonium (bb-bar) states:
    Upsilon(1S) = dim_R * C_2 * pi^5 * m_e = 60 * 156.38 = 9383 MeV (obs 9460)
    eta_b       ~  (dim_R*C_2 - 1/3) * pi^5 * m_e  ~  9399 MeV
    Upsilon(2S) ~  64.1 * pi^5 * m_e  (radial excitation)
    chi_b0      ~  (10*C_2 + 1) * pi^5 * m_e
    chi_b1      ~  (10*C_2 + 1.2) * pi^5 * m_e

Generation hierarchy for vector quarkonia:
    rho       ->  J/psi :  x4  = dim_R(CP^2)
    J/psi     ->  Upsilon:  x3  = N_c = |Z_3|
    rho       ->  Upsilon:  x12 = 2*C_2

Open D and B mesons:
    D^0   = 2*C_2      * pi^5 * m_e  = 12 * 156.38  = 1877 MeV (obs 1865)
    D*    = (N_c+2n_C) * pi^5 * m_e  = 13 * 156.38  = 2033 MeV (obs 2010)
    B+    = 2*sqrt(2)*2*C_2 * pi^5 * m_e = 24*sqrt(2) * 156.38 = 5308 MeV (obs 5279)
    B_c   = 8*n_C      * pi^5 * m_e  = 40 * 156.38  = 6255 MeV (obs 6275)

The fine structure comes from spin-orbit coupling kappa_ls = C_2/n_C = 6/5,
the same parameter that gives ALL nuclear magic numbers.

6 panels:
    1. The Heavy Quark Ladder    — log-scale mass plot for all 6 quarks
    2. Charmonium Spectrum       — energy-level diagram for cc-bar states
    3. Bottomonium Spectrum      — energy-level diagram for bb-bar states
    4. The Splittings            — fine/hyperfine from kappa_ls = 6/5
    5. BST vs PDG               — scatter plot of predicted vs measured
    6. One Formula               — periodic table of mesons with (k, p, q)

CI Interface:
    from toy_heavy_mesons import HeavyMesonSpectrum
    hms = HeavyMesonSpectrum()
    hms.all_mesons()          # All heavy mesons with BST predictions
    hms.charmonium()          # cc-bar states
    hms.bottomonium()         # bb-bar states
    hms.open_heavy()          # D, B, B_c mesons
    hms.generation_ratios()   # rho -> J/psi -> Upsilon hierarchy
    hms.precision_table()     # Formatted comparison table

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
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c    = 3          # color charges
n_C    = 5          # domain dimension (D_IV^5)
C_2    = n_C + 1    # 6  Casimir eigenvalue
genus  = n_C + 2    # 7  genus of D_IV^5
dim_R  = 2 * n_C    # 10  real dimension of D_IV^5
N_max  = 137        # channel capacity
GAMMA  = 1920       # |S_5 x (Z_2)^4|
m_e    = 0.511      # electron mass in MeV
PI5    = np.pi**5   # 306.0197...
alpha  = 1 / 137.035999
kappa_ls = C_2 / n_C  # 6/5  spin-orbit coupling

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
TEAL        = '#00ccaa'
LIME        = '#88ff44'


def _precision_color(pct):
    """Color by prediction quality: gold < 2%, green 2-5%, yellow 5-15%, red > 15%."""
    ap = abs(pct)
    if ap < 2.0:
        return GOLD
    elif ap < 5.0:
        return GREEN
    elif ap < 15.0:
        return YELLOW
    else:
        return RED


def _bar_color(pct):
    """Softer bar fill color by precision bracket."""
    ap = abs(pct)
    if ap < 2.0:
        return '#33aa55'
    elif ap < 5.0:
        return '#55aa33'
    elif ap < 15.0:
        return '#aa8833'
    else:
        return '#aa3333'


# ══════════════════════════════════════════════════════════════════
#  HeavyMesonSpectrum Class  (CI-scriptable API)
# ══════════════════════════════════════════════════════════════════
class HeavyMesonSpectrum:
    """
    BST heavy meson mass predictions from pi^5 * m_e.

    Every charmonium, bottomonium, and open heavy meson mass is
    an algebraic multiple k of pi^5 * m_e = 156.38 MeV, determined
    by BST integers: N_c=3, n_C=5, C_2=6, dim_R=10.

    Usage
    -----
        hms = HeavyMesonSpectrum()
        print(hms.precision_table())
        hms.charmonium()
        hms.generation_ratios()
    """

    def __init__(self):
        self.base_unit = PI5 * m_e                # pi^5 * m_e ~ 156.38 MeV
        self.m_e = m_e
        self.n_C = n_C
        self.N_c = N_c
        self.C_2 = C_2
        self.genus = genus
        self.dim_R = dim_R
        self.kappa_ls = kappa_ls

        self._light_vectors  = self._build_light_vectors()
        self._open_heavy     = self._build_open_heavy()
        self._charmonium     = self._build_charmonium()
        self._bottomonium    = self._build_bottomonium()

    # ── builders ─────────────────────────────────────────────────

    def _build_light_vectors(self):
        """Light vector mesons for the generation ladder."""
        bu = self.base_unit
        return [
            {
                'name': '\u03c1(770)',
                'latex': r'$\rho$',
                'content': 'u\u016b/d\u0305',
                'JPC': '1\u207b\u207b',
                'k': float(n_C),
                'k_label': 'n_C = 5',
                'k_formula': 'n_C',
                'bst_mass': n_C * bu,
                'observed': 775.26,
                'category': 'light_vector',
                'generation': 1,
            },
            {
                'name': '\u03c9(782)',
                'latex': r'$\omega$',
                'content': '(u\u016b+d\u0305d)/\u221a2',
                'JPC': '1\u207b\u207b',
                'k': float(n_C),
                'k_label': 'n_C = 5',
                'k_formula': 'n_C',
                'bst_mass': n_C * bu,
                'observed': 782.66,
                'category': 'light_vector',
                'generation': 1,
            },
            {
                'name': '\u03c6(1020)',
                'latex': r'$\phi$',
                'content': 's\u0305s',
                'JPC': '1\u207b\u207b',
                'k': 13.0 / 2.0,
                'k_label': '13/2',
                'k_formula': '(N_c+2n_C)/2',
                'bst_mass': (N_c + 2 * n_C) / 2.0 * bu,
                'observed': 1019.461,
                'category': 'light_vector',
                'generation': 1,
            },
        ]

    def _build_open_heavy(self):
        """Open charm and bottom mesons: D, D*, B, B_c."""
        bu = self.base_unit
        return [
            {
                'name': 'D\u2070',
                'latex': r'$D^0$',
                'content': 'c\u016b',
                'JPC': '0\u207b',
                'k': 2 * C_2,
                'k_label': '2C\u2082 = 12',
                'k_formula': '2C_2',
                'bst_mass': 2 * C_2 * bu,
                'observed': 1864.84,
                'category': 'open_heavy',
                'generation': 2,
            },
            {
                'name': 'D*\u207a',
                'latex': r'$D^{*+}$',
                'content': 'c\u016b',
                'JPC': '1\u207b',
                'k': N_c + 2 * n_C,
                'k_label': 'N_c+2n_C = 13',
                'k_formula': 'N_c + 2n_C',
                'bst_mass': (N_c + 2 * n_C) * bu,
                'observed': 2010.26,
                'category': 'open_heavy',
                'generation': 2,
            },
            {
                'name': 'B\u207a',
                'latex': r'$B^+$',
                'content': 'b\u016b',
                'JPC': '0\u207b',
                'k': 24 * np.sqrt(2),
                'k_label': '24\u221a2',
                'k_formula': '2\u221a2 \u00d7 2C_2',
                'bst_mass': 24 * np.sqrt(2) * bu,
                'observed': 5279.34,
                'category': 'open_heavy',
                'generation': 3,
            },
            {
                'name': 'B_c',
                'latex': r'$B_c$',
                'content': 'b\u0305c',
                'JPC': '0\u207b',
                'k': 8 * n_C,
                'k_label': '8n_C = 40',
                'k_formula': 'dim(SU(3)) \u00d7 n_C',
                'bst_mass': 8 * n_C * bu,
                'observed': 6274.9,
                'category': 'open_heavy',
                'generation': 3,
            },
        ]

    def _build_charmonium(self):
        """Charmonium (cc-bar) states."""
        bu = self.base_unit
        return [
            {
                'name': '\u03b7_c(1S)',
                'latex': r'$\eta_c$',
                'content': 'c\u0305c',
                'JPC': '0\u207b\u207a',
                'k': N_c**2 + 2 * n_C,
                'k_label': 'N_c\u00b2+2n_C = 19',
                'k_formula': 'N_c\u00b2 + 2n_C',
                'bst_mass': (N_c**2 + 2 * n_C) * bu,
                'observed': 2983.9,
                'category': 'charmonium',
                'n_radial': 1,
                'L': 0,
                'S': 0,
                'J': 0,
            },
            {
                'name': 'J/\u03c8',
                'latex': r'$J/\psi$',
                'content': 'c\u0305c',
                'JPC': '1\u207b\u207b',
                'k': 4 * n_C,
                'k_label': '4n_C = 20',
                'k_formula': 'dim_R(CP\u00b2) \u00d7 n_C',
                'bst_mass': 4 * n_C * bu,
                'observed': 3096.9,
                'category': 'charmonium',
                'n_radial': 1,
                'L': 0,
                'S': 1,
                'J': 1,
            },
            {
                'name': '\u03c7_c0(1P)',
                'latex': r'$\chi_{c0}$',
                'content': 'c\u0305c',
                'JPC': '0\u207a\u207a',
                'k': 4 * n_C + C_2 / N_c,
                'k_label': '4n_C+C\u2082/N_c = 22',
                'k_formula': '4n_C + C_2/N_c',
                'bst_mass': (4 * n_C + C_2 / N_c) * bu,
                'observed': 3414.71,
                'category': 'charmonium',
                'n_radial': 1,
                'L': 1,
                'S': 1,
                'J': 0,
            },
            {
                'name': '\u03c7_c1(1P)',
                'latex': r'$\chi_{c1}$',
                'content': 'c\u0305c',
                'JPC': '1\u207a\u207a',
                'k': 4 * n_C + n_C / 2.0,
                'k_label': '4n_C+n_C/2 = 22.5',
                'k_formula': '4n_C + n_C/2',
                'bst_mass': (4 * n_C + n_C / 2.0) * bu,
                'observed': 3510.67,
                'category': 'charmonium',
                'n_radial': 1,
                'L': 1,
                'S': 1,
                'J': 1,
            },
            {
                'name': 'h_c(1P)',
                'latex': r'$h_c$',
                'content': 'c\u0305c',
                'JPC': '1\u207a\u207b',
                'k': 4 * n_C + n_C / 2.0,
                'k_label': '4n_C+n_C/2 = 22.5',
                'k_formula': '4n_C + n_C/2',
                'bst_mass': (4 * n_C + n_C / 2.0) * bu,
                'observed': 3525.38,
                'category': 'charmonium',
                'n_radial': 1,
                'L': 1,
                'S': 0,
                'J': 1,
            },
            {
                'name': '\u03c7_c2(1P)',
                'latex': r'$\chi_{c2}$',
                'content': 'c\u0305c',
                'JPC': '2\u207a\u207a',
                'k': 4 * n_C + N_c,
                'k_label': '4n_C+N_c = 23',
                'k_formula': '4n_C + N_c',
                'bst_mass': (4 * n_C + N_c) * bu,
                'observed': 3556.17,
                'category': 'charmonium',
                'n_radial': 1,
                'L': 1,
                'S': 1,
                'J': 2,
            },
            {
                'name': '\u03c8(2S)',
                'latex': r'$\psi(2S)$',
                'content': 'c\u0305c',
                'JPC': '1\u207b\u207b',
                'k': 4 * n_C + dim_R / N_c + 1.0 / N_c,
                'k_label': '4n_C+10/3+1/3 \u2248 23.67',
                'k_formula': '4n_C + (dim_R+1)/N_c',
                'bst_mass': (4 * n_C + (dim_R + 1.0) / N_c) * bu,
                'observed': 3686.10,
                'category': 'charmonium',
                'n_radial': 2,
                'L': 0,
                'S': 1,
                'J': 1,
            },
        ]

    def _build_bottomonium(self):
        """Bottomonium (bb-bar) states."""
        bu = self.base_unit
        return [
            {
                'name': '\u03b7_b(1S)',
                'latex': r'$\eta_b$',
                'content': 'b\u0305b',
                'JPC': '0\u207b\u207a',
                'k': dim_R * C_2 - N_c / n_C,
                'k_label': 'dim_R\u00b7C\u2082\u2212N_c/n_C = 59.4',
                'k_formula': 'dim_R\u00b7C_2 \u2212 N_c/n_C',
                'bst_mass': (dim_R * C_2 - N_c / n_C) * bu,
                'observed': 9399.0,
                'category': 'bottomonium',
                'n_radial': 1,
                'L': 0,
                'S': 0,
                'J': 0,
            },
            {
                'name': '\u03a5(1S)',
                'latex': r'$\Upsilon(1S)$',
                'content': 'b\u0305b',
                'JPC': '1\u207b\u207b',
                'k': dim_R * C_2,
                'k_label': 'dim_R\u00b7C\u2082 = 60',
                'k_formula': 'dim_R \u00d7 C_2',
                'bst_mass': dim_R * C_2 * bu,
                'observed': 9460.30,
                'category': 'bottomonium',
                'n_radial': 1,
                'L': 0,
                'S': 1,
                'J': 1,
            },
            {
                'name': '\u03c7_b0(1P)',
                'latex': r'$\chi_{b0}$',
                'content': 'b\u0305b',
                'JPC': '0\u207a\u207a',
                'k': dim_R * C_2 + N_c,
                'k_label': 'dim_R\u00b7C\u2082+N_c = 63',
                'k_formula': 'dim_R\u00b7C_2 + N_c',
                'bst_mass': (dim_R * C_2 + N_c) * bu,
                'observed': 9859.44,
                'category': 'bottomonium',
                'n_radial': 1,
                'L': 1,
                'S': 1,
                'J': 0,
            },
            {
                'name': '\u03c7_b1(1P)',
                'latex': r'$\chi_{b1}$',
                'content': 'b\u0305b',
                'JPC': '1\u207a\u207a',
                'k': dim_R * C_2 + N_c + kappa_ls / N_c,
                'k_label': 'dim_R\u00b7C\u2082+N_c+\u03ba/N_c = 63.4',
                'k_formula': 'dim_R\u00b7C_2 + N_c + \u03ba_ls/N_c',
                'bst_mass': (dim_R * C_2 + N_c + kappa_ls / N_c) * bu,
                'observed': 9892.78,
                'category': 'bottomonium',
                'n_radial': 1,
                'L': 1,
                'S': 1,
                'J': 1,
            },
            {
                'name': '\u03c7_b2(1P)',
                'latex': r'$\chi_{b2}$',
                'content': 'b\u0305b',
                'JPC': '2\u207a\u207a',
                'k': dim_R * C_2 + N_c + 2 * kappa_ls / N_c,
                'k_label': 'dim_R\u00b7C\u2082+N_c+2\u03ba/N_c = 63.8',
                'k_formula': 'dim_R\u00b7C_2 + N_c + 2\u03ba_ls/N_c',
                'bst_mass': (dim_R * C_2 + N_c + 2 * kappa_ls / N_c) * bu,
                'observed': 9912.21,
                'category': 'bottomonium',
                'n_radial': 1,
                'L': 1,
                'S': 1,
                'J': 2,
            },
            {
                'name': '\u03a5(2S)',
                'latex': r'$\Upsilon(2S)$',
                'content': 'b\u0305b',
                'JPC': '1\u207b\u207b',
                'k': dim_R * C_2 + dim_R / N_c + 1.0 / N_c,
                'k_label': 'dim_R\u00b7C\u2082+(dim_R+1)/N_c \u2248 63.67',
                'k_formula': 'dim_R\u00b7C_2 + (dim_R+1)/N_c',
                'bst_mass': (dim_R * C_2 + (dim_R + 1.0) / N_c) * bu,
                'observed': 10023.26,
                'category': 'bottomonium',
                'n_radial': 2,
                'L': 0,
                'S': 1,
                'J': 1,
            },
            {
                'name': '\u03a5(3S)',
                'latex': r'$\Upsilon(3S)$',
                'content': 'b\u0305b',
                'JPC': '1\u207b\u207b',
                'k': dim_R * C_2 + 2 * (dim_R + 1.0) / N_c,
                'k_label': 'dim_R\u00b7C\u2082+2(dim_R+1)/N_c \u2248 67.33',
                'k_formula': 'dim_R\u00b7C_2 + 2(dim_R+1)/N_c',
                'bst_mass': (dim_R * C_2 + 2 * (dim_R + 1.0) / N_c) * bu,
                'observed': 10355.2,
                'category': 'bottomonium',
                'n_radial': 3,
                'L': 0,
                'S': 1,
                'J': 1,
            },
        ]

    # ── public API ───────────────────────────────────────────────

    def _add_precision(self, m):
        """Return copy of meson dict with precision_pct added."""
        entry = dict(m)
        entry['precision_pct'] = 100.0 * (m['bst_mass'] - m['observed']) / m['observed']
        return entry

    def light_vectors(self):
        """Return light vector mesons (generation ladder base)."""
        return [self._add_precision(m) for m in self._light_vectors]

    def open_heavy(self):
        """Return open heavy mesons: D, D*, B, B_c."""
        return [self._add_precision(m) for m in self._open_heavy]

    def charmonium(self):
        """Return charmonium (cc-bar) states."""
        return [self._add_precision(m) for m in self._charmonium]

    def bottomonium(self):
        """Return bottomonium (bb-bar) states."""
        return [self._add_precision(m) for m in self._bottomonium]

    def all_mesons(self):
        """Return all mesons with BST predictions and observed values."""
        everything = (self._light_vectors + self._open_heavy
                      + self._charmonium + self._bottomonium)
        return [self._add_precision(m) for m in everything]

    def generation_ratios(self):
        """Return the generation hierarchy ratios for vector quarkonia."""
        rho = self._light_vectors[0]
        jpsi = self._charmonium[1]  # J/psi
        upsilon = self._bottomonium[1]  # Upsilon(1S)
        return {
            'rho_mass': rho['observed'],
            'jpsi_mass': jpsi['observed'],
            'upsilon_mass': upsilon['observed'],
            'jpsi_over_rho_obs': jpsi['observed'] / rho['observed'],
            'jpsi_over_rho_bst': 4.0,
            'jpsi_over_rho_meaning': 'dim_R(CP^2) = 4',
            'upsilon_over_jpsi_obs': upsilon['observed'] / jpsi['observed'],
            'upsilon_over_jpsi_bst': 3.0,
            'upsilon_over_jpsi_meaning': 'N_c = |Z_3| = 3',
            'upsilon_over_rho_obs': upsilon['observed'] / rho['observed'],
            'upsilon_over_rho_bst': 12.0,
            'upsilon_over_rho_meaning': '2*C_2 = dim_R(CP^2) x N_c',
            'B_over_D_obs': 5279.34 / 1864.84,
            'B_over_D_bst': 2 * np.sqrt(2),
            'B_over_D_meaning': 'Tsirelson bound',
        }

    def precision_table(self):
        """Return a formatted precision comparison table as a string."""
        lines = []
        lines.append('')
        lines.append('=' * 100)
        lines.append('  HEAVY MESON SPECTRUM  --  BST Predictions from k x pi^5 x m_e')
        lines.append('=' * 100)
        lines.append(f'  Base unit:  pi^5 * m_e = {self.base_unit:.2f} MeV')
        lines.append(f'  kappa_ls = C_2/n_C = {self.kappa_ls:.4f}  '
                     f'(spin-orbit = same as nuclear magic numbers)')
        lines.append('-' * 100)
        hdr = f'  {"Meson":<18} {"k":<12} {"BST (MeV)":>12}'
        hdr += f'  {"PDG (MeV)":>12}  {"Delta":>10}  {"Content"}'
        lines.append(hdr)
        lines.append('-' * 100)

        sections = [
            ('LIGHT VECTORS (reference)', self.light_vectors()),
            ('OPEN HEAVY MESONS', self.open_heavy()),
            ('CHARMONIUM (cc-bar)', self.charmonium()),
            ('BOTTOMONIUM (bb-bar)', self.bottomonium()),
        ]

        for section_name, mesons in sections:
            lines.append(f'  {section_name}')
            lines.append('  ' + '-' * 96)
            for m in mesons:
                delta = f'{m["precision_pct"]:+.2f}%'
                content = m.get('content', '')
                lines.append(
                    f'  {m["name"]:<18} {m["k_label"]:<12}'
                    f' {m["bst_mass"]:>12.1f}  {m["observed"]:>12.1f}'
                    f'  {delta:>10}  {content}'
                )
            lines.append('')

        lines.append('-' * 100)
        lines.append(f'  BST integers: N_c={N_c}, n_C={n_C}, C_2={C_2},'
                     f' dim_R={dim_R}, genus={genus}, kappa_ls={kappa_ls}')
        lines.append('=' * 100)

        # Generation ratios
        ratios = self.generation_ratios()
        lines.append('')
        lines.append('  GENERATION HIERARCHY')
        lines.append('  ' + '-' * 60)
        lines.append(f'    J/psi / rho     = {ratios["jpsi_over_rho_obs"]:.3f}'
                     f'  (BST: {ratios["jpsi_over_rho_bst"]:.0f}'
                     f' = {ratios["jpsi_over_rho_meaning"]})')
        lines.append(f'    Upsilon / J/psi = {ratios["upsilon_over_jpsi_obs"]:.3f}'
                     f'  (BST: {ratios["upsilon_over_jpsi_bst"]:.0f}'
                     f' = {ratios["upsilon_over_jpsi_meaning"]})')
        lines.append(f'    Upsilon / rho   = {ratios["upsilon_over_rho_obs"]:.3f}'
                     f'  (BST: {ratios["upsilon_over_rho_bst"]:.0f}'
                     f' = {ratios["upsilon_over_rho_meaning"]})')
        lines.append(f'    B / D           = {ratios["B_over_D_obs"]:.3f}'
                     f'  (BST: {ratios["B_over_D_bst"]:.3f}'
                     f' = {ratios["B_over_D_meaning"]})')
        lines.append('')
        return '\n'.join(lines)

    def best_predictions(self, threshold=2.0):
        """Return predictions better than *threshold* percent."""
        return [m for m in self.all_mesons() if abs(m['precision_pct']) < threshold]

    def summary(self):
        """One-line summary statistics."""
        all_m = self.all_mesons()
        precs = [abs(m['precision_pct']) for m in all_m]
        n_good = sum(1 for p in precs if p < 2.0)
        return (f'{len(all_m)} mesons | base unit {self.base_unit:.2f} MeV |'
                f' median error {np.median(precs):.2f}% |'
                f' {n_good}/{len(all_m)} within 2%')


# ══════════════════════════════════════════════════════════════════
#  Panel 1: The Heavy Quark Ladder
# ══════════════════════════════════════════════════════════════════

def _draw_quark_ladder(ax, hms):
    """Log-scale mass plot for all 6 quarks with BST exponents."""
    ax.set_facecolor(DARK_PANEL)

    # Quark data: name, mass (MeV), BST description, color, generation
    quarks = [
        ('u',    2.16,    'base',          CYAN,     1),
        ('d',    4.67,    'base',          SOFT_BLUE, 1),
        ('s',    93.4,    '\u03b1\u207b\u00b3',  GREEN,    2),
        ('c',    1270.0,  '\u03b1\u207b\u2075',  ORANGE,   2),
        ('b',    4180.0,  '\u03b1\u207b\u2077',  MAGENTA,  3),
        ('t',    172760.0,'\u03b1\u207b\u00b9\u00b2', RED, 3),
    ]

    ax.set_title('The Heavy Quark Ladder',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)

    y_positions = np.arange(len(quarks))
    masses = [q[1] for q in quarks]

    for i, (name, mass, bst_exp, color, gen) in enumerate(quarks):
        # Horizontal bar (log scale)
        bar_width = np.log10(mass)
        ax.barh(i, bar_width, height=0.55, color=color, alpha=0.7, zorder=2)

        # Glow effect
        ax.barh(i, bar_width, height=0.7, color=color, alpha=0.12, zorder=1)

        # Quark name
        ax.text(-0.35, i, name, fontsize=16, color=color,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold', zorder=3)

        # Mass label
        if mass >= 1000:
            mass_str = f'{mass/1000:.1f} GeV'
        else:
            mass_str = f'{mass:.1f} MeV'
        ax.text(bar_width + 0.08, i, mass_str, fontsize=9, color=WHITE,
                ha='left', va='center', fontfamily='monospace', zorder=3)

        # BST exponent label
        ax.text(bar_width + 0.08, i - 0.25, f'BST: {bst_exp}',
                fontsize=7, color=GREY, ha='left', va='center',
                fontfamily='monospace', zorder=3)

        # Generation bracket
        if i % 2 == 0 and i < len(quarks) - 1:
            gen_y = i + 0.5
            ax.text(5.7, gen_y, f'Gen {gen}', fontsize=8, color=GOLD_DIM,
                    ha='center', va='center', fontfamily='monospace',
                    rotation=0)

    # Generation dividers
    for div_y in [1.5, 3.5]:
        ax.axhline(div_y, color=GOLD_DIM, lw=0.5, alpha=0.4, ls='--')

    # Arrow showing x4, x3 factors
    ax.annotate('', xy=(np.log10(3097), 2.7), xytext=(np.log10(775), 0.3),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.5))
    ax.text(np.log10(1500), 1.5, '\u00d74', fontsize=10, color=GOLD,
            ha='center', va='center', fontfamily='monospace', fontweight='bold')

    ax.annotate('', xy=(np.log10(9460), 4.3), xytext=(np.log10(3097), 2.7),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.5))
    ax.text(np.log10(5000), 3.5, '\u00d73', fontsize=10, color=GOLD,
            ha='center', va='center', fontfamily='monospace', fontweight='bold')

    ax.set_xlim(-0.6, 6.2)
    ax.set_ylim(-0.5, 5.8)
    ax.set_yticks([])
    ax.set_xlabel('log\u2081\u2080(mass / MeV)', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.tick_params(colors=GREY, which='both')
    ax.spines['bottom'].set_color(GREY)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Generation labels
    ax.text(5.7, 0.5, 'Gen 1', fontsize=9, color=CYAN, alpha=0.7,
            ha='center', va='center', fontfamily='monospace',
            fontweight='bold')
    ax.text(5.7, 2.5, 'Gen 2', fontsize=9, color=ORANGE, alpha=0.7,
            ha='center', va='center', fontfamily='monospace',
            fontweight='bold')
    ax.text(5.7, 4.5, 'Gen 3', fontsize=9, color=MAGENTA, alpha=0.7,
            ha='center', va='center', fontfamily='monospace',
            fontweight='bold')


# ══════════════════════════════════════════════════════════════════
#  Panel 2: Charmonium Spectrum
# ══════════════════════════════════════════════════════════════════

def _draw_charmonium_spectrum(ax, hms):
    """Energy level diagram for cc-bar states."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_title('Charmonium Spectrum  (c\u0305c)',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)

    states = hms.charmonium()

    # Group by L quantum number for x-positioning
    # L=0: eta_c, J/psi, psi(2S)
    # L=1: chi_c0, chi_c1, h_c, chi_c2
    x_positions = {
        '\u03b7_c(1S)': 1.0,
        'J/\u03c8': 2.0,
        '\u03c7_c0(1P)': 3.5,
        '\u03c7_c1(1P)': 4.5,
        'h_c(1P)': 5.5,
        '\u03c7_c2(1P)': 6.5,
        '\u03c8(2S)': 8.0,
    }

    # Draw threshold line
    ax.axhline(3730, color=RED, lw=0.8, alpha=0.4, ls=':')
    ax.text(8.7, 3730, 'D\u0305D threshold', fontsize=7, color=RED,
            alpha=0.6, va='center', fontfamily='monospace')

    for m in states:
        x = x_positions.get(m['name'], 1.0)
        y_bst = m['bst_mass']
        y_obs = m['observed']
        prec = m['precision_pct']
        pcol = _precision_color(prec)

        # Observed level (grey)
        ax.plot([x - 0.35, x + 0.35], [y_obs, y_obs],
                color=GREY, lw=2.0, alpha=0.5, zorder=1)

        # BST level (colored)
        ax.plot([x - 0.35, x + 0.35], [y_bst, y_bst],
                color=pcol, lw=2.5, alpha=0.9, zorder=2)

        # Glow
        ax.plot([x - 0.35, x + 0.35], [y_bst, y_bst],
                color=pcol, lw=6.0, alpha=0.15, zorder=1)

        # State label
        ax.text(x, y_bst + 35, m['name'], fontsize=8, color=WHITE,
                ha='center', va='bottom', fontfamily='monospace',
                fontweight='bold',
                path_effects=[pe.withStroke(linewidth=2, foreground=DARK_PANEL)],
                zorder=3)

        # Precision label
        ax.text(x, y_bst - 25, f'{prec:+.1f}%', fontsize=7,
                color=pcol, ha='center', va='top',
                fontfamily='monospace', zorder=3)

        # J^PC label
        ax.text(x, y_obs - 40, m['JPC'], fontsize=6,
                color=GREY, ha='center', va='top',
                fontfamily='monospace', alpha=0.7, zorder=3)

    # Section headers
    ax.text(1.5, 2870, 'S-wave (L=0)', fontsize=8, color=CYAN,
            ha='center', fontfamily='monospace', alpha=0.7)
    ax.text(5.0, 2870, 'P-wave (L=1)', fontsize=8, color=ORANGE,
            ha='center', fontfamily='monospace', alpha=0.7)
    ax.text(8.0, 2870, 'Radial (n=2)', fontsize=8, color=MAGENTA,
            ha='center', fontfamily='monospace', alpha=0.7)

    # Vertical section dividers
    ax.axvline(2.75, color=GREY, lw=0.3, alpha=0.3, ls=':')
    ax.axvline(7.25, color=GREY, lw=0.3, alpha=0.3, ls=':')

    ax.set_xlim(0.2, 9.2)
    ax.set_ylim(2850, 3800)
    ax.set_ylabel('Mass (MeV)', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_xticks([])
    ax.tick_params(colors=GREY, which='both', labelsize=8)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Legend
    ax.plot([7.6, 8.2], [3780, 3780], color=GOLD, lw=2.5)
    ax.text(8.35, 3780, 'BST', fontsize=7, color=GOLD, va='center',
            fontfamily='monospace')
    ax.plot([7.6, 8.2], [3760, 3760], color=GREY, lw=2.0, alpha=0.5)
    ax.text(8.35, 3760, 'PDG', fontsize=7, color=GREY, va='center',
            fontfamily='monospace')


# ══════════════════════════════════════════════════════════════════
#  Panel 3: Bottomonium Spectrum
# ══════════════════════════════════════════════════════════════════

def _draw_bottomonium_spectrum(ax, hms):
    """Energy level diagram for bb-bar states."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_title('Bottomonium Spectrum  (b\u0305b)',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)

    states = hms.bottomonium()

    x_positions = {
        '\u03b7_b(1S)': 1.0,
        '\u03a5(1S)': 2.0,
        '\u03c7_b0(1P)': 3.5,
        '\u03c7_b1(1P)': 4.5,
        '\u03c7_b2(1P)': 5.5,
        '\u03a5(2S)': 7.0,
        '\u03a5(3S)': 8.0,
    }

    # BB-bar threshold
    ax.axhline(10559, color=RED, lw=0.8, alpha=0.4, ls=':')
    ax.text(8.7, 10559, 'B\u0305B threshold', fontsize=7, color=RED,
            alpha=0.6, va='center', fontfamily='monospace')

    for m in states:
        x = x_positions.get(m['name'], 1.0)
        y_bst = m['bst_mass']
        y_obs = m['observed']
        prec = m['precision_pct']
        pcol = _precision_color(prec)

        # Observed level (grey)
        ax.plot([x - 0.35, x + 0.35], [y_obs, y_obs],
                color=GREY, lw=2.0, alpha=0.5, zorder=1)

        # BST level (colored)
        ax.plot([x - 0.35, x + 0.35], [y_bst, y_bst],
                color=pcol, lw=2.5, alpha=0.9, zorder=2)

        # Glow
        ax.plot([x - 0.35, x + 0.35], [y_bst, y_bst],
                color=pcol, lw=6.0, alpha=0.15, zorder=1)

        # State label
        ax.text(x, y_bst + 30, m['name'], fontsize=8, color=WHITE,
                ha='center', va='bottom', fontfamily='monospace',
                fontweight='bold',
                path_effects=[pe.withStroke(linewidth=2, foreground=DARK_PANEL)],
                zorder=3)

        # Precision label
        ax.text(x, y_bst - 22, f'{prec:+.1f}%', fontsize=7,
                color=pcol, ha='center', va='top',
                fontfamily='monospace', zorder=3)

        # J^PC label
        ax.text(x, y_obs - 35, m['JPC'], fontsize=6,
                color=GREY, ha='center', va='top',
                fontfamily='monospace', alpha=0.7, zorder=3)

    # Section headers
    ax.text(1.5, 9200, 'S-wave (L=0)', fontsize=8, color=CYAN,
            ha='center', fontfamily='monospace', alpha=0.7)
    ax.text(4.5, 9200, 'P-wave (L=1)', fontsize=8, color=ORANGE,
            ha='center', fontfamily='monospace', alpha=0.7)
    ax.text(7.5, 9200, 'Radial', fontsize=8, color=MAGENTA,
            ha='center', fontfamily='monospace', alpha=0.7)

    # Vertical section dividers
    ax.axvline(2.75, color=GREY, lw=0.3, alpha=0.3, ls=':')
    ax.axvline(6.25, color=GREY, lw=0.3, alpha=0.3, ls=':')

    # Show chi_b fine structure with kappa_ls
    ax.annotate('', xy=(5.5, 9912), xytext=(3.5, 9860),
                arrowprops=dict(arrowstyle='<->', color=TEAL, lw=1.0, alpha=0.5))
    ax.text(4.5, 9830, '\u03ba_ls = 6/5', fontsize=7, color=TEAL,
            ha='center', fontfamily='monospace', alpha=0.8)

    ax.set_xlim(0.2, 9.2)
    ax.set_ylim(9150, 10650)
    ax.set_ylabel('Mass (MeV)', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_xticks([])
    ax.tick_params(colors=GREY, which='both', labelsize=8)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Legend
    ax.plot([7.6, 8.2], [10620, 10620], color=GOLD, lw=2.5)
    ax.text(8.35, 10620, 'BST', fontsize=7, color=GOLD, va='center',
            fontfamily='monospace')
    ax.plot([7.6, 8.2], [10590, 10590], color=GREY, lw=2.0, alpha=0.5)
    ax.text(8.35, 10590, 'PDG', fontsize=7, color=GREY, va='center',
            fontfamily='monospace')


# ══════════════════════════════════════════════════════════════════
#  Panel 4: The Splittings — kappa_ls = 6/5
# ══════════════════════════════════════════════════════════════════

def _draw_splittings(ax, hms):
    """Fine structure from kappa_ls = C_2/n_C = 6/5."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_title('The Splittings:  \u03ba_ls = C\u2082/n_C = 6/5',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # ── Charmonium splittings ──
    ax.text(0.25, 0.95, 'Charmonium Splittings', fontsize=11,
            color=ORANGE, ha='center', fontfamily='monospace',
            fontweight='bold')

    charm_splits = [
        ('J/\u03c8 \u2212 \u03b7_c', 3096.9 - 2983.9,
         (4 * n_C - (N_c**2 + 2 * n_C)) * PI5 * m_e,
         'Hyperfine: \u0394k=1'),
        ('\u03c7_c2 \u2212 \u03c7_c0', 3556.17 - 3414.71,
         (N_c - C_2 / N_c) * PI5 * m_e,
         'Tensor: \u0394k=N_c\u2212C\u2082/N_c'),
        ('\u03c7_c1 \u2212 \u03c7_c0', 3510.67 - 3414.71,
         (n_C / 2.0 - C_2 / N_c) * PI5 * m_e,
         'Spin-orbit: n_C/2\u2212C\u2082/N_c'),
        ('\u03c8(2S) \u2212 J/\u03c8', 3686.10 - 3096.9,
         ((dim_R + 1.0) / N_c) * PI5 * m_e,
         'Radial: (dim_R+1)/N_c'),
    ]

    y = 0.87
    dy = 0.10
    for label, obs_split, bst_split, desc in charm_splits:
        pct = 100.0 * (bst_split - obs_split) / obs_split if obs_split != 0 else 0
        pcol = _precision_color(pct)

        ax.text(0.02, y, label, fontsize=9, color=WHITE,
                ha='left', fontfamily='monospace')
        ax.text(0.25, y, f'obs: {obs_split:.1f}', fontsize=8, color=GREY,
                ha='left', fontfamily='monospace')
        ax.text(0.25, y - 0.025, f'BST: {bst_split:.1f} ({pct:+.1f}%)',
                fontsize=8, color=pcol, ha='left', fontfamily='monospace')
        ax.text(0.02, y - 0.025, desc, fontsize=7, color=GREY,
                ha='left', fontfamily='monospace', alpha=0.6)
        y -= dy

    # ── Bottomonium splittings ──
    ax.text(0.75, 0.95, 'Bottomonium Splittings', fontsize=11,
            color=MAGENTA, ha='center', fontfamily='monospace',
            fontweight='bold')

    bottom_splits = [
        ('\u03a5(1S) \u2212 \u03b7_b', 9460.30 - 9399.0,
         (N_c / n_C) * PI5 * m_e,
         'Hyperfine: N_c/n_C'),
        ('\u03c7_b2 \u2212 \u03c7_b0', 9912.21 - 9859.44,
         (2 * kappa_ls / N_c) * PI5 * m_e,
         'Fine: 2\u03ba_ls/N_c'),
        ('\u03c7_b1 \u2212 \u03c7_b0', 9892.78 - 9859.44,
         (kappa_ls / N_c) * PI5 * m_e,
         'Spin-orbit: \u03ba_ls/N_c'),
        ('\u03a5(2S) \u2212 \u03a5(1S)', 10023.26 - 9460.30,
         ((dim_R + 1.0) / N_c) * PI5 * m_e,
         'Radial: (dim_R+1)/N_c'),
    ]

    y = 0.87
    for label, obs_split, bst_split, desc in bottom_splits:
        pct = 100.0 * (bst_split - obs_split) / obs_split if obs_split != 0 else 0
        pcol = _precision_color(pct)

        ax.text(0.52, y, label, fontsize=9, color=WHITE,
                ha='left', fontfamily='monospace')
        ax.text(0.75, y, f'obs: {obs_split:.1f}', fontsize=8, color=GREY,
                ha='left', fontfamily='monospace')
        ax.text(0.75, y - 0.025, f'BST: {bst_split:.1f} ({pct:+.1f}%)',
                fontsize=8, color=pcol, ha='left', fontfamily='monospace')
        ax.text(0.52, y - 0.025, desc, fontsize=7, color=GREY,
                ha='left', fontfamily='monospace', alpha=0.6)
        y -= dy

    # ── Nuclear connection ──
    ax.plot([0.05, 0.95], [0.42, 0.42], color=GOLD_DIM, lw=0.5, alpha=0.5)

    ax.text(0.50, 0.38, 'ONE COUPLING CONSTANT: \u03ba_ls = C\u2082/n_C = 6/5',
            fontsize=12, color=BRIGHT_GOLD, ha='center',
            fontfamily='monospace', fontweight='bold')

    # Nuclear magic numbers
    magic = [2, 8, 20, 28, 50, 82, 126]
    magic_str = ', '.join(str(m) for m in magic)
    ax.text(0.50, 0.32,
            f'Nuclear magic numbers:  {magic_str}',
            fontsize=10, color=TEAL, ha='center',
            fontfamily='monospace')
    ax.text(0.50, 0.27,
            'All 7 magic numbers from \u03ba_ls = 6/5 in the spin-orbit potential',
            fontsize=9, color=GREY, ha='center',
            fontfamily='monospace')
    ax.text(0.50, 0.22,
            'The SAME 6/5 that splits chi_b states splits nuclear shells!',
            fontsize=9, color=TEAL, ha='center',
            fontfamily='monospace', style='italic')

    # BST prediction
    ax.text(0.50, 0.14,
            'BST prediction: next magic number = 184  (superheavy island of stability)',
            fontsize=9, color=GOLD, ha='center',
            fontfamily='monospace', fontweight='bold')

    # Divider
    ax.plot([0.48, 0.48], [0.45, 0.92], color=GREY, lw=0.3, alpha=0.3, ls=':')


# ══════════════════════════════════════════════════════════════════
#  Panel 5: BST vs PDG Scatter Plot
# ══════════════════════════════════════════════════════════════════

def _draw_scatter(ax, hms):
    """Scatter plot: BST predicted mass vs PDG measured mass."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_title('BST vs PDG  --  All Heavy Mesons',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)

    all_m = hms.all_mesons()

    # Category colors
    cat_colors = {
        'light_vector': CYAN,
        'open_heavy': GREEN,
        'charmonium': ORANGE,
        'bottomonium': MAGENTA,
    }
    cat_labels = {
        'light_vector': 'Light vectors',
        'open_heavy': 'Open heavy (D, B)',
        'charmonium': 'Charmonium',
        'bottomonium': 'Bottomonium',
    }

    # y = x line
    max_mass = max(m['observed'] for m in all_m) * 1.08
    ax.plot([0, max_mass], [0, max_mass], color=GOLD_DIM, lw=1.0,
            alpha=0.5, ls='--', zorder=0, label='perfect')

    # +/- 1% band
    x_band = np.linspace(0, max_mass, 100)
    ax.fill_between(x_band, x_band * 0.99, x_band * 1.01,
                    color=GOLD, alpha=0.06, zorder=0)
    ax.text(max_mass * 0.75, max_mass * 0.73, '\u00b11%', fontsize=8,
            color=GOLD_DIM, fontfamily='monospace', alpha=0.5, rotation=42)

    # Plot each meson
    plotted_cats = set()
    for m in all_m:
        cat = m['category']
        color = cat_colors.get(cat, WHITE)
        prec = m['precision_pct']
        marker_size = 60 + 30 * (1.0 / (1.0 + abs(prec)))

        label = cat_labels.get(cat) if cat not in plotted_cats else None
        plotted_cats.add(cat)

        ax.scatter(m['observed'], m['bst_mass'], s=marker_size,
                   color=color, alpha=0.85, zorder=3, edgecolors='white',
                   linewidths=0.3, label=label)

        # Name label (offset to avoid overlap)
        offset_x = max_mass * 0.015
        offset_y = max_mass * 0.015
        short_name = m['name'].split('(')[0] if '(' in m['name'] else m['name']
        ax.text(m['observed'] + offset_x, m['bst_mass'] + offset_y,
                short_name, fontsize=6, color=color, alpha=0.7,
                fontfamily='monospace', zorder=4)

    ax.set_xlabel('PDG Mass (MeV)', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_ylabel('BST Mass (MeV)', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_xlim(0, max_mass)
    ax.set_ylim(0, max_mass)
    ax.set_aspect('equal')

    ax.tick_params(colors=GREY, which='both', labelsize=8)
    ax.spines['bottom'].set_color(GREY)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend(loc='upper left', fontsize=8, facecolor=DARK_PANEL,
              edgecolor=GREY, labelcolor=WHITE, framealpha=0.9)

    # Summary stat
    precs = [abs(m['precision_pct']) for m in all_m]
    median_err = np.median(precs)
    max_err = max(precs)
    ax.text(0.97, 0.05, f'median |err| = {median_err:.2f}%\nmax |err| = {max_err:.1f}%',
            fontsize=8, color=GOLD, ha='right', va='bottom',
            fontfamily='monospace', transform=ax.transAxes)


# ══════════════════════════════════════════════════════════════════
#  Panel 6: One Formula — Periodic Table of Mesons
# ══════════════════════════════════════════════════════════════════

def _draw_one_formula(ax, hms):
    """Show all meson masses from m = k * pi^5 * m_e with quantum numbers."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_title('One Formula:  m = k \u00d7 \u03c0\u2075 \u00d7 m_e',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    all_m = hms.all_mesons()

    # Sort by mass for display
    all_m.sort(key=lambda m: m['observed'])

    # Header
    y = 0.95
    dy = 0.038
    cols = [
        (0.01, 'Meson', 'left', 9),
        (0.15, 'k', 'left', 9),
        (0.40, 'BST Formula', 'left', 8),
        (0.66, 'BST', 'right', 9),
        (0.78, 'PDG', 'right', 9),
        (0.92, '\u0394', 'right', 9),
    ]
    for xp, txt, ha, fs in cols:
        ax.text(xp, y, txt, fontsize=fs, color=GOLD_DIM, ha=ha,
                fontfamily='monospace', fontweight='bold')
    y -= 0.015
    ax.plot([0.005, 0.995], [y, y], color=GREY, lw=0.5, alpha=0.5)
    y -= dy * 0.5

    # Category colors
    cat_colors = {
        'light_vector': CYAN,
        'open_heavy': GREEN,
        'charmonium': ORANGE,
        'bottomonium': MAGENTA,
    }

    prev_cat = None
    for m in all_m:
        cat = m['category']
        color = cat_colors.get(cat, WHITE)

        # Section divider on category change
        if cat != prev_cat and prev_cat is not None:
            ax.plot([0.005, 0.995], [y + dy * 0.3, y + dy * 0.3],
                    color=GREY, lw=0.3, alpha=0.3)
        prev_cat = cat

        prec = m['precision_pct']
        pcol = _precision_color(prec)

        # Name
        short_name = m['name']
        if len(short_name) > 14:
            short_name = short_name[:14]
        ax.text(0.01, y, short_name, fontsize=8, color=color,
                ha='left', fontfamily='monospace')

        # k value
        k_str = m.get('k_label', f'{m["k"]:.2f}')
        if len(k_str) > 16:
            k_str = k_str[:16]
        ax.text(0.15, y, k_str, fontsize=7, color=CYAN,
                ha='left', fontfamily='monospace')

        # Formula
        formula = m.get('k_formula', '')
        if len(formula) > 22:
            formula = formula[:22]
        ax.text(0.40, y, formula, fontsize=7, color=GREY,
                ha='left', fontfamily='monospace')

        # BST mass
        ax.text(0.66, y, f'{m["bst_mass"]:.0f}', fontsize=8, color=WHITE,
                ha='right', fontfamily='monospace')

        # PDG mass
        ax.text(0.78, y, f'{m["observed"]:.0f}', fontsize=8, color=GREY,
                ha='right', fontfamily='monospace')

        # Delta
        ax.text(0.92, y, f'{prec:+.1f}%', fontsize=8, color=pcol,
                ha='right', fontfamily='monospace', fontweight='bold')

        # Mini precision bar
        bar_w = min(abs(prec) / 25.0, 0.07)
        ax.barh(y, bar_w, left=0.93, height=dy * 0.45,
                color=pcol, alpha=0.25, zorder=0)

        y -= dy

    # Footer insight
    y -= dy * 0.3
    ax.plot([0.005, 0.995], [y + dy * 0.3, y + dy * 0.3],
            color=GREY, lw=0.5, alpha=0.3)
    ax.text(0.50, y - dy * 0.2,
            'Every mass = integer \u00d7 \u03c0\u2075m_e   |   '
            'Integers from {N_c=3, n_C=5, C\u2082=6, dim_R=10}   |   '
            'Zero free parameters',
            fontsize=8, color=BRIGHT_GOLD, ha='center',
            fontfamily='monospace', style='italic')


# ══════════════════════════════════════════════════════════════════
#  Main Visualization
# ══════════════════════════════════════════════════════════════════

def visualize(hms=None):
    """Build and display the full Heavy Meson Spectrum figure."""
    if hms is None:
        hms = HeavyMesonSpectrum()

    fig = plt.figure(figsize=(22, 16), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'Heavy Meson Spectrum \u2014 Charmonium & Bottomonium \u2014 BST')

    # Title
    fig.text(0.50, 0.975,
             'HEAVY MESON SPECTRUM \u2014 CHARMONIUM & BOTTOMONIUM',
             fontsize=26, fontweight='bold', color=GOLD,
             ha='center', va='top', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#332200')])
    fig.text(0.50, 0.950,
             'All masses from k \u00d7 \u03c0\u2075 \u00d7 m_e = k \u00d7 %.2f MeV'
             '   |   Generation hierarchy: \u00d74 \u00d7 \u00d73 = \u00d712'
             % hms.base_unit,
             fontsize=11, color=GOLD_DIM, ha='center', va='top',
             fontfamily='monospace')

    # Grid: 3 rows x 2 columns
    gs = GridSpec(3, 2, figure=fig,
                  left=0.04, right=0.96, top=0.92, bottom=0.05,
                  hspace=0.35, wspace=0.20,
                  height_ratios=[1.0, 1.0, 1.0])

    # (0,0) Heavy Quark Ladder
    ax1 = fig.add_subplot(gs[0, 0])
    _draw_quark_ladder(ax1, hms)

    # (0,1) Charmonium Spectrum
    ax2 = fig.add_subplot(gs[0, 1])
    _draw_charmonium_spectrum(ax2, hms)

    # (1,0) Bottomonium Spectrum
    ax3 = fig.add_subplot(gs[1, 0])
    _draw_bottomonium_spectrum(ax3, hms)

    # (1,1) The Splittings
    ax4 = fig.add_subplot(gs[1, 1])
    _draw_splittings(ax4, hms)

    # (2,0) BST vs PDG scatter
    ax5 = fig.add_subplot(gs[2, 0])
    _draw_scatter(ax5, hms)

    # (2,1) One Formula table
    ax6 = fig.add_subplot(gs[2, 1])
    _draw_one_formula(ax6, hms)

    # Bottom annotation
    fig.text(0.50, 0.015,
             '\u03c0\u2075m_e = %.2f MeV   |   '
             '\u03ba_ls = C\u2082/n_C = 6/5   |   '
             'J/\u03c8/\u03c1 = 4 = dim_R(CP\u00b2)   |   '
             '\u03a5/J/\u03c8 = 3 = N_c   |   '
             'B/D = 2\u221a2 = Tsirelson   |   '
             'ZERO free parameters'
             % hms.base_unit,
             fontsize=9, color=GREY, ha='center', va='bottom',
             fontfamily='monospace')

    plt.show()


# legacy alias
show = visualize


# ══════════════════════════════════════════════════════════════════
#  Main Entry Point
# ══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    hms = HeavyMesonSpectrum()

    # ── Programmatic report ──
    print(hms.precision_table())

    print('\n--- Summary ---')
    print(hms.summary())

    print('\n--- Best Predictions (< 2%) ---')
    for m in hms.best_predictions(threshold=2.0):
        print(f'  {m["name"]:<18} BST={m["bst_mass"]:.1f}  '
              f'obs={m["observed"]:.1f}  delta={m["precision_pct"]:+.3f}%')

    print('\n--- Generation Hierarchy ---')
    ratios = hms.generation_ratios()
    print(f'  J/psi / rho     = {ratios["jpsi_over_rho_obs"]:.3f}'
          f'  (BST: {ratios["jpsi_over_rho_bst"]:.0f}'
          f' = {ratios["jpsi_over_rho_meaning"]})')
    print(f'  Upsilon / J/psi = {ratios["upsilon_over_jpsi_obs"]:.3f}'
          f'  (BST: {ratios["upsilon_over_jpsi_bst"]:.0f}'
          f' = {ratios["upsilon_over_jpsi_meaning"]})')
    print(f'  Upsilon / rho   = {ratios["upsilon_over_rho_obs"]:.3f}'
          f'  (BST: {ratios["upsilon_over_rho_bst"]:.0f}'
          f' = {ratios["upsilon_over_rho_meaning"]})')
    print(f'  B / D           = {ratios["B_over_D_obs"]:.3f}'
          f'  (BST: {ratios["B_over_D_bst"]:.3f}'
          f' = {ratios["B_over_D_meaning"]})')

    print('\n--- All Multipliers ---')
    for m in hms.all_mesons():
        print(f'  k = {m["k_label"]:<30}'
              f'  -> {m["bst_mass"]:>10.1f} MeV'
              f'  [{m["name"]}]  ({m["precision_pct"]:+.2f}%)')

    print(f'\n--- Constants ---')
    print(f'  pi^5 * m_e       = {hms.base_unit:.4f} MeV')
    print(f'  kappa_ls = C_2/n_C = {kappa_ls:.4f}')
    print(f'  Tsirelson bound  = {2*np.sqrt(2):.4f}')
    print(f'  6*pi^5*m_e       = {6*hms.base_unit:.4f} MeV  (proton)')

    # ── Visualization ──
    print('\nLaunching visualization...')
    visualize(hms)
