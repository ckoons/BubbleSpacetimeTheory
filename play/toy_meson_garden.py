#!/usr/bin/env python3
"""
THE MESON GARDEN
================
A BST playground visualizing the complete pseudoscalar meson nonet
and vector meson quartet, with all masses derived from a single
base unit: pi^5 * m_e = 156.38 MeV.

The same pi^5 that appears in the proton mass formula m_p/m_e = 6*pi^5
sets the scale for ALL meson masses. Each meson mass is an integer
or algebraic multiple of this unit, determined by BST integers:
  n_C = 5, C_2 = 6, genus = 7, N_c = 3.

Pseudoscalar nonet:
  pi0, pi+/-     :  pi^5 * m_e                       =  156.38 MeV
  K+/-, K0       :  sqrt(2*n_C) * pi^5 * m_e         =  494.49 MeV
  eta            :  sqrt(C_2) * pi^5 * m_e            =  383.08 MeV
  eta'           :  (g^2/8) * pi^5 * m_e              =  957.85 MeV

Vector mesons:
  rho            :  n_C * pi^5 * m_e                  =  781.89 MeV
  omega          :  n_C * pi^5 * m_e                  =  781.89 MeV
  K*             :  C_2 * pi^5 * m_e                  =  938.27 MeV
  phi            :  (n_C+1) * pi^5 * m_e              =  938.27 MeV

Key insight: pi^5 * m_e is the meson base unit, and 6 * (pi^5 * m_e)
= proton mass.  The proton is the sixth harmonic of the meson garden.

CI Interface:
    from toy_meson_garden import MesonGarden
    mg = MesonGarden()
    mg.all_mesons()          # All mesons with BST predictions
    mg.pseudoscalars()       # Pseudoscalar nonet data
    mg.vectors()             # Vector meson data
    mg.precision_table()     # Formatted comparison table
    mg.best_predictions()    # Sub-threshold predictions

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
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3         # color charges
n_C   = 5         # domain dimension  (D_IV^5)
C_2   = n_C + 1   # 6  Casimir eigenvalue
genus = n_C + 2   # 7  genus of D_IV^5
N_max = 137       # channel capacity
GAMMA = 1920      # |S_5 x (Z_2)^4|
m_e   = 0.511     # electron mass in MeV
PI5   = np.pi**5  # 306.0197...
alpha = 1 / 137.035999

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
#  MesonGarden Class  (CI-scriptable API)
# ══════════════════════════════════════════════════════════════════
class MesonGarden:
    """
    BST meson mass predictions from the single base unit pi^5 * m_e.

    Every pseudoscalar and vector meson mass is an algebraic multiple
    of pi^5 * m_e = 156.38 MeV, determined by BST integers only.

    Usage
    -----
        garden = MesonGarden()
        print(garden.precision_table())
        best = garden.best_predictions(threshold=1.0)
    """

    def __init__(self):
        self.base_unit = PI5 * m_e                # pi^5 * m_e ~ 156.38 MeV
        self.m_e = m_e
        self.n_C = n_C
        self.N_c = N_c
        self.C_2 = C_2
        self.genus = genus

        self._pseudoscalars = self._build_pseudoscalars()
        self._vectors       = self._build_vectors()

    # ── builders ─────────────────────────────────────────────────

    def _build_pseudoscalars(self):
        bu = self.base_unit
        g  = self.genus
        return [
            {
                'name': '\u03c0\u2070',
                'latex': r'$\pi^0$',
                'formula_str': 'pi^5 * m_e',
                'multiplier': 1.0,
                'multiplier_label': '1',
                'bst_mass': bu,
                'observed': 134.977,
                'strangeness': 0,
                'isospin3': 0.0,
                'category': 'pseudoscalar',
                'note': 'needs quark mass correction',
            },
            {
                'name': '\u03c0\u207a',
                'latex': r'$\pi^+$',
                'formula_str': 'pi^5 * m_e',
                'multiplier': 1.0,
                'multiplier_label': '1',
                'bst_mass': bu,
                'observed': 139.570,
                'strangeness': 0,
                'isospin3': 1.0,
                'category': 'pseudoscalar',
                'note': 'needs quark mass correction',
            },
            {
                'name': '\u03c0\u207b',
                'latex': r'$\pi^-$',
                'formula_str': 'pi^5 * m_e',
                'multiplier': 1.0,
                'multiplier_label': '1',
                'bst_mass': bu,
                'observed': 139.570,
                'strangeness': 0,
                'isospin3': -1.0,
                'category': 'pseudoscalar',
                'note': 'needs quark mass correction',
            },
            {
                'name': 'K\u207a',
                'latex': r'$K^+$',
                'formula_str': 'sqrt(2*n_C) * pi^5 * m_e',
                'multiplier': np.sqrt(2 * n_C),
                'multiplier_label': '\u221a10',
                'bst_mass': np.sqrt(2 * n_C) * bu,
                'observed': 493.677,
                'strangeness': 1,
                'isospin3': 0.5,
                'category': 'pseudoscalar',
                'note': '',
            },
            {
                'name': 'K\u207b',
                'latex': r'$K^-$',
                'formula_str': 'sqrt(2*n_C) * pi^5 * m_e',
                'multiplier': np.sqrt(2 * n_C),
                'multiplier_label': '\u221a10',
                'bst_mass': np.sqrt(2 * n_C) * bu,
                'observed': 493.677,
                'strangeness': -1,
                'isospin3': -0.5,
                'category': 'pseudoscalar',
                'note': '',
            },
            {
                'name': 'K\u2070',
                'latex': r'$K^0$',
                'formula_str': 'sqrt(2*n_C) * pi^5 * m_e',
                'multiplier': np.sqrt(2 * n_C),
                'multiplier_label': '\u221a10',
                'bst_mass': np.sqrt(2 * n_C) * bu,
                'observed': 497.611,
                'strangeness': 1,
                'isospin3': -0.5,
                'category': 'pseudoscalar',
                'note': '',
            },
            {
                'name': 'K\u0304\u2070',
                'latex': r'$\bar{K}^0$',
                'formula_str': 'sqrt(2*n_C) * pi^5 * m_e',
                'multiplier': np.sqrt(2 * n_C),
                'multiplier_label': '\u221a10',
                'bst_mass': np.sqrt(2 * n_C) * bu,
                'observed': 497.611,
                'strangeness': -1,
                'isospin3': 0.5,
                'category': 'pseudoscalar',
                'note': '',
            },
            {
                'name': '\u03b7',
                'latex': r'$\eta$',
                'formula_str': 'sqrt(C_2) * pi^5 * m_e',
                'multiplier': np.sqrt(C_2),
                'multiplier_label': '\u221a6',
                'bst_mass': np.sqrt(C_2) * bu,
                'observed': 547.862,
                'strangeness': 0,
                'isospin3': 0.0,
                'category': 'pseudoscalar',
                'note': "eta-eta' mixing not included",
            },
            {
                'name': "\u03b7'",
                'latex': r"$\eta'$",
                'formula_str': '(g^2/8) * pi^5 * m_e',
                'multiplier': g**2 / 8.0,
                'multiplier_label': '49/8',
                'bst_mass': (g**2 / 8.0) * bu,
                'observed': 957.78,
                'strangeness': 0,
                'isospin3': 0.0,
                'category': 'pseudoscalar',
                'note': 'U(1)_A anomaly mass',
            },
        ]

    def _build_vectors(self):
        bu = self.base_unit
        return [
            {
                'name': '\u03c1',
                'latex': r'$\rho$',
                'formula_str': 'n_C * pi^5 * m_e',
                'multiplier': float(n_C),
                'multiplier_label': '5',
                'bst_mass': n_C * bu,
                'observed': 775.26,
                'strangeness': 0,
                'isospin3': 0.0,
                'category': 'vector',
                'note': '',
            },
            {
                'name': '\u03c9',
                'latex': r'$\omega$',
                'formula_str': 'n_C * pi^5 * m_e',
                'multiplier': float(n_C),
                'multiplier_label': '5',
                'bst_mass': n_C * bu,
                'observed': 782.66,
                'strangeness': 0,
                'isospin3': 0.0,
                'category': 'vector',
                'note': '',
            },
            {
                'name': 'K*',
                'latex': r'$K^*$',
                'formula_str': 'C_2 * pi^5 * m_e',
                'multiplier': float(C_2),
                'multiplier_label': '6',
                'bst_mass': C_2 * bu,
                'observed': 891.67,
                'strangeness': 1,
                'isospin3': 0.0,
                'category': 'vector',
                'note': '',
            },
            {
                'name': '\u03c6',
                'latex': r'$\phi$',
                'formula_str': '(n_C+1) * pi^5 * m_e',
                'multiplier': float(n_C + 1),
                'multiplier_label': '6',
                'bst_mass': (n_C + 1) * bu,
                'observed': 1019.461,
                'strangeness': 0,
                'isospin3': 0.0,
                'category': 'vector',
                'note': 's-sbar',
            },
        ]

    # ── public API ───────────────────────────────────────────────

    def _add_precision(self, m):
        """Return copy of meson dict with precision_pct added."""
        entry = dict(m)
        entry['precision_pct'] = 100.0 * (m['bst_mass'] - m['observed']) / m['observed']
        return entry

    def all_mesons(self):
        """Return all mesons with BST predictions and observed values."""
        return [self._add_precision(m) for m in self._pseudoscalars + self._vectors]

    def pseudoscalars(self):
        """Return pseudoscalar nonet."""
        return [self._add_precision(m) for m in self._pseudoscalars]

    def vectors(self):
        """Return vector mesons."""
        return [self._add_precision(m) for m in self._vectors]

    def precision_table(self):
        """Return a formatted precision comparison table as a string."""
        lines = []
        lines.append('')
        lines.append('=' * 92)
        lines.append('  THE MESON GARDEN  --  BST Mass Predictions from pi^5 * m_e')
        lines.append('=' * 92)
        lines.append(f'  Base unit:  pi^5 * m_e = {self.base_unit:.2f} MeV')
        lines.append(f'  Proton:     6 * pi^5 * m_e = {6 * self.base_unit:.2f} MeV'
                      f'  (observed: 938.272 MeV)')
        lines.append('-' * 92)
        hdr = f'  {"Meson":<12} {"Multiplier":<14} {"BST (MeV)":>12}'
        hdr += f'  {"Obs (MeV)":>12}  {"Delta":>10}  {"Note"}'
        lines.append(hdr)
        lines.append('-' * 92)

        lines.append('  PSEUDOSCALAR NONET (J^P = 0^-)')
        lines.append('  ' + '-' * 88)
        for m in self.pseudoscalars():
            delta = f'{m["precision_pct"]:+.2f}%'
            note = m.get('note', '')
            lines.append(
                f'  {m["name"]:<12} {m["multiplier_label"]:<14}'
                f' {m["bst_mass"]:>12.2f}  {m["observed"]:>12.3f}'
                f'  {delta:>10}  {note}'
            )

        lines.append('')
        lines.append('  VECTOR MESONS (J^P = 1^-)')
        lines.append('  ' + '-' * 88)
        for m in self.vectors():
            delta = f'{m["precision_pct"]:+.2f}%'
            note = m.get('note', '')
            lines.append(
                f'  {m["name"]:<12} {m["multiplier_label"]:<14}'
                f' {m["bst_mass"]:>12.2f}  {m["observed"]:>12.3f}'
                f'  {delta:>10}  {note}'
            )

        lines.append('-' * 92)
        lines.append(f'  BST integers: N_c={N_c}, n_C={n_C}, C_2={C_2},'
                      f' genus={genus}, |Gamma|={GAMMA}')
        lines.append('=' * 92)
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
                f' median error {np.median(precs):.1f}% |'
                f' {n_good}/{len(all_m)} within 2%')


# ══════════════════════════════════════════════════════════════════
#  Visualization Helpers
# ══════════════════════════════════════════════════════════════════

# Nonet layout: positions in the (I_3, Strangeness) weight diagram.
_NONET_NODES = [
    # key,        I3,    S,   display_name,        data_name,         latex
    ('pi+',       1.0,   0,   '\u03c0\u207a',      '\u03c0\u207a',   r'$\pi^+$'),
    ('pi0',       0.0,   0,   '\u03c0\u2070',      '\u03c0\u2070',   r'$\pi^0$'),
    ('pi-',      -1.0,   0,   '\u03c0\u207b',      '\u03c0\u207b',   r'$\pi^-$'),
    ('K+',        0.5,   1,   'K\u207a',           'K\u207a',        r'$K^+$'),
    ('K0',       -0.5,   1,   'K\u2070',           'K\u2070',        r'$K^0$'),
    ('Kbar0',     0.5,  -1,   'K\u0304\u2070',     'K\u0304\u2070',  r'$\bar{K}^0$'),
    ('K-',       -0.5,  -1,   'K\u207b',           'K\u207b',        r'$K^-$'),
    ('eta',       0.0,   0,   '\u03b7',            '\u03b7',         r'$\eta$'),
    ('etap',      0.0,   0,   "\u03b7'",           "\u03b7'",        r"$\eta'$"),
]

# Visual offsets so eta, eta', pi0 don't overlap at origin
_NONET_OFFSETS = {
    'pi0':  ( 0.00,  0.00),
    'eta':  ( 0.00, -0.35),
    'etap': ( 0.00, -0.70),
}

# SU(3) flavor structure lines (outer hexagon + radial)
_SU3_EDGES = [
    ('pi+', 'K+'),  ('K+', 'K0'),   ('K0', 'pi-'),
    ('pi-', 'K-'),  ('K-', 'Kbar0'),('Kbar0', 'pi+'),
    ('pi+', 'pi0'), ('pi-', 'pi0'),
    ('K+',  'pi0'), ('K0',  'pi0'),
    ('K-',  'pi0'), ('Kbar0','pi0'),
]


def _draw_nonet(ax, garden):
    """Draw the pseudoscalar meson nonet on the (I_3, S) weight diagram."""
    ax.set_facecolor(BG)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.7, 1.7)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('Pseudoscalar Nonet  (J$^P$ = 0$^-$)',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=12)

    # Axis labels and arrows
    ax.text(1.80, -1.50, '$I_3$', fontsize=12, color=GREY,
            ha='right', fontfamily='monospace')
    ax.text(-1.80, 1.55, '$S$', fontsize=12, color=GREY,
            ha='left', fontfamily='monospace')
    ax.annotate('', xy=(1.75, 0), xytext=(-1.75, 0),
                arrowprops=dict(arrowstyle='->', color=GREY, lw=0.8, ls='--'))
    ax.annotate('', xy=(0, 1.55), xytext=(0, -1.45),
                arrowprops=dict(arrowstyle='->', color=GREY, lw=0.8, ls='--'))

    # Strangeness labels
    for s_val, s_lbl in [(1, 'S=+1'), (0, 'S=0'), (-1, 'S=-1')]:
        ax.text(-1.75, s_val, s_lbl, fontsize=7, color='#445566',
                ha='left', va='center', fontfamily='monospace', alpha=0.6)

    # Build position map
    positions = {}
    for key, i3, s, dname, data_name, latex in _NONET_NODES:
        dx, dy = _NONET_OFFSETS.get(key, (0, 0))
        positions[key] = (i3 + dx, s + dy)

    # Draw SU(3) connecting lines
    for a, b in _SU3_EDGES:
        if a in positions and b in positions:
            xa, ya = positions[a]
            xb, yb = positions[b]
            ax.plot([xa, xb], [ya, yb], color='#223355', lw=0.8,
                    alpha=0.45, zorder=1)

    # Draw outer hexagon
    hex_keys = ['K+', 'pi+', 'Kbar0', 'K-', 'pi-', 'K0']
    hx = [positions[k][0] for k in hex_keys] + [positions[hex_keys[0]][0]]
    hy = [positions[k][1] for k in hex_keys] + [positions[hex_keys[0]][1]]
    ax.plot(hx, hy, color='#334466', lw=1.3, alpha=0.55, zorder=0)

    # Build data lookup
    ps_data = {}
    for m in garden.pseudoscalars():
        ps_data[m['name']] = m

    # Draw nodes
    for key, i3, s, dname, data_name, latex in _NONET_NODES:
        x, y = positions[key]
        mdata = ps_data.get(data_name)
        if mdata is None:
            continue
        mass = mdata['bst_mass']
        prec = mdata['precision_pct']
        node_color = _precision_color(prec)
        radius = 0.07 + 0.09 * (mass / 1000.0)

        # glow
        glow = plt.Circle((x, y), radius * 1.7, color=node_color,
                           alpha=0.08, zorder=2)
        ax.add_patch(glow)
        # node
        circ = plt.Circle((x, y), radius, color=node_color,
                           alpha=0.85, zorder=3)
        ax.add_patch(circ)
        # particle label
        ax.text(x, y + radius + 0.13, latex, fontsize=11,
                color=WHITE, ha='center', va='bottom',
                fontfamily='monospace', fontweight='bold',
                path_effects=[pe.withStroke(linewidth=2, foreground=BG)],
                zorder=4)
        # mass value
        ax.text(x, y - radius - 0.09, f'{mass:.0f}',
                fontsize=8, color=node_color, ha='center',
                va='top', fontfamily='monospace', zorder=4)

    # Precision legend
    ly = -1.35
    for label, col in [('<2%', GOLD), ('2\u20135%', GREEN),
                       ('5\u201315%', YELLOW), ('>15%', RED)]:
        ax.plot(-1.60, ly, 'o', color=col, markersize=6)
        ax.text(-1.44, ly, label, fontsize=8, color=col,
                va='center', fontfamily='monospace')
        ly -= 0.20


def _draw_vectors_diagram(ax, garden):
    """Draw vector mesons in a diamond layout."""
    ax.set_facecolor(BG)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.0, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('Vector Mesons  (J$^P$ = 1$^-$)',
                 fontsize=13, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=8)

    v_list = garden.vectors()
    # rho, omega, K*, phi in diamond
    layout = [
        (v_list[0], -0.65,  0.0),   # rho
        (v_list[1],  0.65,  0.0),   # omega
        (v_list[2],  0.0,   0.65),  # K*
        (v_list[3],  0.0,  -0.45),  # phi
    ]

    # connecting lines
    for i in range(len(layout)):
        for j in range(i + 1, len(layout)):
            _, x1, y1 = layout[i]
            _, x2, y2 = layout[j]
            ax.plot([x1, x2], [y1, y2], color='#334466', lw=0.8,
                    alpha=0.35, zorder=0)

    for mdata, x, y in layout:
        mass = mdata['bst_mass']
        prec = mdata['precision_pct']
        node_color = _precision_color(prec)
        radius = 0.08 + 0.07 * (mass / 1000.0)

        glow = plt.Circle((x, y), radius * 1.7, color=node_color,
                           alpha=0.08, zorder=2)
        ax.add_patch(glow)
        circ = plt.Circle((x, y), radius, color=node_color,
                           alpha=0.85, zorder=3)
        ax.add_patch(circ)

        ax.text(x, y + radius + 0.11, mdata['latex'], fontsize=11,
                color=WHITE, ha='center', va='bottom',
                fontfamily='monospace', fontweight='bold',
                path_effects=[pe.withStroke(linewidth=2, foreground=BG)],
                zorder=4)
        ax.text(x, y - radius - 0.07, f'{mass:.0f}',
                fontsize=8, color=node_color, ha='center',
                va='top', fontfamily='monospace', zorder=4)

    # Multiplier annotations
    ax.text(-1.40, -0.85, 'k = n_C = 5', fontsize=7, color=GREY,
            fontfamily='monospace', ha='left')
    ax.text(0.55, -0.85, 'k = C\u2082 = 6', fontsize=7, color=GREY,
            fontfamily='monospace', ha='left')


def _draw_comparison_bars(ax, garden):
    """Horizontal bar chart comparing BST predictions vs observed."""
    ax.set_facecolor(DARK_PANEL)

    all_m = garden.all_mesons()
    # Deduplicate: merge charge conjugates for display
    seen = set()
    display = []
    for m in all_m:
        key = m['name'].replace('\u207a', '').replace('\u207b', '')
        key = key.replace('K\u0304\u2070', 'K\u2070')
        if key in seen:
            continue
        seen.add(key)
        display.append(m)

    display = list(reversed(display))
    n = len(display)
    y_pos = np.arange(n)

    names     = [m['name'] for m in display]
    bst_vals  = [m['bst_mass'] for m in display]
    obs_vals  = [m['observed'] for m in display]
    precs     = [m['precision_pct'] for m in display]

    # Observed bars (dim)
    ax.barh(y_pos, obs_vals, height=0.36, color='#223344', alpha=0.70,
            label='Observed', zorder=1)

    # BST bars (colored by precision)
    for i in range(n):
        col = _bar_color(precs[i])
        ax.barh(y_pos[i], bst_vals[i], height=0.36, color=col,
                alpha=0.85, zorder=2)
        # precision label at right
        pcol = _precision_color(precs[i])
        xtext = max(bst_vals[i], obs_vals[i]) + 18
        ax.text(xtext, y_pos[i], f'{precs[i]:+.2f}%', fontsize=8,
                color=pcol, va='center', fontfamily='monospace', zorder=3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=10, color=WHITE, fontfamily='monospace')
    ax.set_xlabel('Mass (MeV)', fontsize=11, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_title('BST Prediction vs Observed',
                 fontsize=13, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10)

    ax.tick_params(colors=GREY, which='both')
    ax.spines['bottom'].set_color(GREY)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0, 1250)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#223344', alpha=0.7, label='Observed'),
        Patch(facecolor='#33aa55', label='BST (colored by precision)'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=8,
              facecolor=DARK_PANEL, edgecolor=GREY, labelcolor=WHITE,
              framealpha=0.9)


def _draw_table_panel(ax, garden):
    """Compact in-figure table showing BST formulas, multipliers, and precision."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.set_title('BST Formulas & Precision',
                 fontsize=13, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=8)

    y = 0.93
    dy = 0.058

    # Header row
    cols = [(0.02, 'Meson', 'left'), (0.18, 'k', 'left'),
            (0.40, 'BST', 'right'), (0.60, 'Obs', 'right'),
            (0.80, 'Delta', 'right')]
    for xp, txt, ha in cols:
        ax.text(xp, y, txt, fontsize=9, color=GOLD_DIM, ha=ha,
                fontfamily='monospace', fontweight='bold')
    y -= 0.015
    ax.plot([0.01, 0.99], [y, y], color=GREY, lw=0.5, alpha=0.5)
    y -= dy * 0.5

    # Deduplicate for display
    all_m = garden.all_mesons()
    seen = set()
    rows = []
    for m in all_m:
        key = m['name'].replace('\u207a', '').replace('\u207b', '')
        key = key.replace('K\u0304\u2070', 'K\u2070')
        if key in seen:
            continue
        seen.add(key)
        rows.append(m)

    vec_header_drawn = False
    for m in rows:
        # Section divider before vectors
        if m['category'] == 'vector' and not vec_header_drawn:
            ax.plot([0.01, 0.99], [y + dy * 0.3, y + dy * 0.3],
                    color=GREY, lw=0.3, alpha=0.4)
            ax.text(0.02, y + dy * 0.05, 'vectors', fontsize=7,
                    color=GREY, fontfamily='monospace', style='italic')
            y -= dy * 0.35
            vec_header_drawn = True

        prec = m['precision_pct']
        pcol = _precision_color(prec)

        ax.text(0.02, y, m['name'], fontsize=9, color=WHITE,
                ha='left', fontfamily='monospace')
        ax.text(0.18, y, m['multiplier_label'], fontsize=9,
                color=CYAN, ha='left', fontfamily='monospace')
        ax.text(0.40, y, f'{m["bst_mass"]:.1f}', fontsize=9,
                color=WHITE, ha='right', fontfamily='monospace')
        ax.text(0.60, y, f'{m["observed"]:.1f}', fontsize=9,
                color=GREY, ha='right', fontfamily='monospace')
        ax.text(0.80, y, f'{prec:+.2f}%', fontsize=9,
                color=pcol, ha='right', fontfamily='monospace',
                fontweight='bold')

        # mini precision bar
        bar_w = min(abs(prec) / 30.0, 0.18)
        ax.barh(y, bar_w, left=0.82, height=dy * 0.42,
                color=pcol, alpha=0.22, zorder=0)

        y -= dy

    # Insight box
    y -= dy * 0.3
    ax.plot([0.01, 0.99], [y + dy * 0.35, y + dy * 0.35],
            color=GREY, lw=0.5, alpha=0.3)
    ax.text(0.50, y - dy * 0.15,
            "Key: proton = 6th harmonic of base unit\n"
            "eta' at g^2/8 = 49/8  (0.007% precision!)",
            fontsize=9, color=BRIGHT_GOLD, ha='center',
            fontfamily='monospace', style='italic', linespacing=1.5)


def _draw_multiplier_spectrum(ax, garden):
    """Number line showing the integer/algebraic multipliers of pi^5 m_e."""
    ax.set_facecolor(DARK_PANEL)

    all_m = garden.all_mesons()
    seen = set()
    unique = []
    for m in all_m:
        ml = m['multiplier_label']
        if ml not in seen:
            seen.add(ml)
            unique.append(m)
    unique.sort(key=lambda m: m['multiplier'])

    ax.set_xlim(-0.3, 8.0)
    ax.set_ylim(-0.45, 0.9)
    ax.axis('off')

    # Base line
    ax.plot([-0.15, 7.5], [0, 0], color=GREY, lw=1.5, alpha=0.55)

    # Tick marks for each unique multiplier
    for m in unique:
        x = m['multiplier']
        col = _precision_color(m['precision_pct'])
        ax.plot([x, x], [-0.06, 0.06], color=col, lw=2.2)
        ax.text(x, 0.17, m['multiplier_label'], fontsize=9,
                color=col, ha='center', fontfamily='monospace',
                fontweight='bold')
        ax.text(x, -0.17, m['name'], fontsize=7,
                color=WHITE, ha='center', va='top',
                fontfamily='monospace', alpha=0.75)

    # Proton marker at multiplier = 6 (C_2)
    proton_x = 6.0
    ax.plot([proton_x, proton_x], [-0.09, 0.09], color=BRIGHT_GOLD, lw=3.5)
    ax.text(proton_x, 0.22, 'C\u2082=6', fontsize=10,
            color=BRIGHT_GOLD, ha='center', fontfamily='monospace',
            fontweight='bold')
    ax.text(proton_x, -0.23, 'proton', fontsize=8,
            color=BRIGHT_GOLD, ha='center', va='top',
            fontfamily='monospace')

    # Title
    ax.text(3.8, 0.72,
            'Multiplier Spectrum:  mass = k \u00d7 \u03c0\u2075m\u2091'
            '        (the proton sits at the 6th harmonic)',
            fontsize=11, color=GOLD_DIM, ha='center',
            fontfamily='monospace')


# ══════════════════════════════════════════════════════════════════
#  Main Visualization
# ══════════════════════════════════════════════════════════════════

def visualize(garden=None):
    """Build and display the full Meson Garden figure."""
    if garden is None:
        garden = MesonGarden()

    fig = plt.figure(figsize=(19, 14), facecolor=BG)
    fig.canvas.manager.set_window_title('The Meson Garden \u2014 BST')

    # Title
    fig.text(0.50, 0.975, 'THE MESON GARDEN',
             fontsize=28, fontweight='bold', color=GOLD,
             ha='center', va='top', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#332200')])
    fig.text(0.50, 0.945,
             'All meson masses from one base unit:  '
             '\u03c0\u2075 \u00d7 m\u2091 = %.2f MeV' % garden.base_unit,
             fontsize=12, color=GOLD_DIM, ha='center', va='top',
             fontfamily='monospace')

    # Grid: 3 rows x 2 columns
    gs = GridSpec(3, 2, figure=fig,
                  left=0.04, right=0.96, top=0.92, bottom=0.06,
                  hspace=0.38, wspace=0.22,
                  height_ratios=[3.0, 2.0, 1.0])

    # (0,0) Pseudoscalar nonet
    ax_nonet = fig.add_subplot(gs[0, 0])
    _draw_nonet(ax_nonet, garden)

    # (0,1) Bar chart comparison
    ax_bars = fig.add_subplot(gs[0, 1])
    _draw_comparison_bars(ax_bars, garden)

    # (1,0) Vector mesons
    ax_vec = fig.add_subplot(gs[1, 0])
    _draw_vectors_diagram(ax_vec, garden)

    # (1,1) Table panel
    ax_table = fig.add_subplot(gs[1, 1])
    _draw_table_panel(ax_table, garden)

    # (2,:) Multiplier spectrum spanning both columns
    ax_spec = fig.add_subplot(gs[2, :])
    _draw_multiplier_spectrum(ax_spec, garden)

    # Bottom annotation
    bu = garden.base_unit
    proton = 6 * bu
    fig.text(0.50, 0.018,
             '\u03c0\u2075 m\u2091 = %.2f MeV   |   '
             'Proton: 6\u03c0\u2075 m\u2091 = %.2f MeV (obs: 938.272)   |   '
             'BST: N_c=%d, n_C=%d, C\u2082=%d, genus=%d'
             % (bu, proton, N_c, n_C, C_2, genus),
             fontsize=10, color=GREY, ha='center', va='bottom',
             fontfamily='monospace')

    plt.show()


# legacy alias for backward compatibility
show = visualize


# ══════════════════════════════════════════════════════════════════
#  Main Entry Point
# ══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    garden = MesonGarden()

    # ── Programmatic report ──
    print(garden.precision_table())

    print('\n--- Summary ---')
    print(garden.summary())

    print('\n--- Best Predictions (< 2%) ---')
    for m in garden.best_predictions(threshold=2.0):
        print(f'  {m["name"]:<12} BST={m["bst_mass"]:.2f}  '
              f'obs={m["observed"]:.3f}  delta={m["precision_pct"]:+.3f}%')

    print('\n--- All Unique Multipliers ---')
    seen_mult = set()
    for m in garden.all_mesons():
        ml = m['multiplier_label']
        if ml not in seen_mult:
            seen_mult.add(ml)
            print(f'  k = {ml:<8}  '
                  f'({m["multiplier"]:.4f})  '
                  f'-> {m["bst_mass"]:.2f} MeV  [{m["name"]}]')

    base = garden.base_unit
    print(f'\n--- Base Unit ---')
    print(f'  pi^5 * m_e = {base:.4f} MeV')
    print(f'  6 * pi^5 * m_e = {6 * base:.4f} MeV  (proton, obs: 938.272)')
    print(f'  pi^5 = {PI5:.6f}')
    print(f'  pi^5 / 1920 = {PI5 / GAMMA:.8f}  (Hua volume)')

    # ── Visualization ──
    print('\nLaunching visualization...')
    visualize(garden)
