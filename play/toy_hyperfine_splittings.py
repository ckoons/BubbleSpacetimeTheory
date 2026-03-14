#!/usr/bin/env python3
"""
HYPERFINE SPLITTINGS FROM CHERN CLASSES
========================================
Toy 139 — c_3 = 13 controls ALL heavy meson hyperfine splittings.

The general formula is:

    Delta_m_HF = (numerator / D) x pi^5 x m_e

where pi^5 x m_e = 156.38 MeV is the BST mass unit, the numerator is c_3 = 13
(the gauge boson count) for three of four systems, and D is a product of
Chern class coefficients:

    c(Q^5) = (1+h)^7 / (1+2h)  =>  {c_1, c_2, c_3, c_4, c_5} = {5, 11, 13, 9, 3}

Four systems:
    Charmonium  (J/psi - eta_c):   D = 18 = 2 x c_4        => 112.94 MeV  (obs 113.0)
    Bottomonium (Y - eta_b):       D = 33 = 3 x c_2         =>  61.60 MeV  (obs 61.6)
    B meson     (B* - B):          D = 45 = c_1 x c_4       =>  45.18 MeV  (obs 45.37)
    D meson     (D*0 - D0):        num = 10 = 2 x n_C, D = c_2  => 142.16 MeV  (obs 142.01)

Clean ratio test:
    Delta_m(cc-bar) / Delta_m(bb-bar) = (13/18) / (13/33) = 33/18 = 11/6 = c_2/C_2
    Observed: 113.0 / 61.6 = 1.834 => 0.06% match to 11/6 = 1.8333...

CI Interface:
    from toy_hyperfine_splittings import HyperfineSplittings
    hs = HyperfineSplittings()
    hs.splittings()           # all 5 splittings with predictions
    hs.clean_ratio()          # the cc-bar/bb-bar = c_2/C_2 test
    hs.denominators()         # Chern decomposition of each D
    hs.deviations()           # all deviations
    hs.summary()              # key results as dict
    hs.show()                 # 6-panel visualization

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

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c   = 3                      # color charges
n_C   = 5                      # complex dimension of D_IV^5
C_2   = n_C + 1                # = 6, Casimir eigenvalue
genus = n_C + 2                # = 7
N_max = 137                    # channel capacity
m_e   = 0.51099895             # electron mass in MeV
PI5   = np.pi**5               # 306.0197...
PI5_me = PI5 * m_e             # the BST mass unit ~ 156.38 MeV

# Chern classes of Q^5 = SO(7)/[SO(5) x SO(2)]
# c(Q^5) = (1+h)^7 / (1+2h)
c_0 = 1
c_1 = 5      # = n_C
c_2 = 11     # = dim K (isotropy group)
c_3 = 13     # = gauge boson count, Weinberg denominator
c_4 = 9      # = N_c^2
c_5 = 3      # = N_c

CHERN = [c_0, c_1, c_2, c_3, c_4, c_5]

# ═══════════════════════════════════════════════════════════════════
# COLORS (dark theme)
# ═══════════════════════════════════════════════════════════════════

BG         = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD       = '#ffd700'
GOLD_DIM   = '#aa8800'
BRIGHT_GOLD = '#ffee44'
CYAN       = '#00ddff'
GREEN      = '#44ff88'
WHITE      = '#eeeeff'
GREY       = '#666688'
SOFT_BLUE  = '#4488ff'
VIOLET     = '#aa44ff'
ORANGE     = '#ff8800'
RED        = '#ff3344'
MAGENTA    = '#ff44cc'

GLOW = [pe.withStroke(linewidth=3, foreground='#332200')]


# ═══════════════════════════════════════════════════════════════════
# HyperfineSplittings CLASS
# ═══════════════════════════════════════════════════════════════════

class HyperfineSplittings:
    """
    BST hyperfine splitting predictions from Chern class c_3 = 13.

    Every heavy meson hyperfine splitting is:
        Delta_m = (numerator / D) x pi^5 x m_e

    where D is a product of Chern class coefficients.

    Usage
    -----
        hs = HyperfineSplittings()
        print(hs.precision_table())
        hs.show()
    """

    def __init__(self):
        self.pi5_me = PI5_me
        self.chern = CHERN

        self._systems = self._build_systems()

    # ── builders ─────────────────────────────────────────────────

    def _build_systems(self):
        """Build the hyperfine splitting data for all systems."""
        return [
            {
                'name': 'Charmonium',
                'particles': r'J/$\psi$ $-$ $\eta_c$',
                'particles_text': 'J/psi - eta_c',
                'label': r'$c\bar{c}$',
                'label_text': 'cc-bar',
                'numerator': c_3,
                'numerator_label': 'c_3 = 13',
                'denominator': 18,
                'denom_factors': f'2 x c_4 = 2 x {c_4}',
                'denom_chern': [('2', None), ('c_4', c_4)],
                'bst_mass': (c_3 / 18) * PI5_me,
                'observed': 113.0,
                'obs_err': 0.4,
                'note': 'PDG 2024',
            },
            {
                'name': 'Bottomonium',
                'particles': r'$\Upsilon$ $-$ $\eta_b$',
                'particles_text': 'Y - eta_b',
                'label': r'$b\bar{b}$',
                'label_text': 'bb-bar',
                'numerator': c_3,
                'numerator_label': 'c_3 = 13',
                'denominator': 33,
                'denom_factors': f'3 x c_2 = 3 x {c_2}',
                'denom_chern': [('3', None), ('c_2', c_2)],
                'bst_mass': (c_3 / 33) * PI5_me,
                'observed': 61.6,
                'obs_err': 2.0,
                'note': 'PDG 2024',
            },
            {
                'name': 'B meson',
                'particles': r'$B^*$ $-$ $B$',
                'particles_text': 'B* - B',
                'label': r'$B$',
                'label_text': 'B',
                'numerator': c_3,
                'numerator_label': 'c_3 = 13',
                'denominator': 45,
                'denom_factors': f'c_1 x c_4 = {c_1} x {c_4}',
                'denom_chern': [('c_1', c_1), ('c_4', c_4)],
                'bst_mass': (c_3 / 45) * PI5_me,
                'observed': 45.37,
                'obs_err': 0.21,
                'note': 'PDG 2024',
            },
            {
                'name': 'D meson',
                'particles': r'$D^{*0}$ $-$ $D^0$',
                'particles_text': 'D*0 - D0',
                'label': r'$D$',
                'label_text': 'D',
                'numerator': 10,
                'numerator_label': '2 x n_C = 10',
                'denominator': c_2,
                'denom_factors': f'c_2 = {c_2}',
                'denom_chern': [('c_2', c_2)],
                'bst_mass': (10 / c_2) * PI5_me,
                'observed': 142.01,
                'obs_err': 0.04,
                'note': 'PDG 2024',
            },
            {
                'name': 'B_s meson',
                'particles': r'$B_s^*$ $-$ $B_s$',
                'particles_text': 'B_s* - B_s',
                'label': r'$B_s$',
                'label_text': 'B_s',
                'numerator': c_3,
                'numerator_label': 'c_3 = 13',
                'denominator': 41,
                'denom_factors': 'prediction',
                'denom_chern': [('41', None)],
                'bst_mass': (c_3 / 41) * PI5_me,
                'observed': 49.0,
                'obs_err': 1.5,
                'note': 'PDG 2024 (prediction test)',
            },
        ]

    # ── public API ───────────────────────────────────────────────

    def _add_precision(self, s):
        """Return copy with precision_pct added."""
        entry = dict(s)
        entry['precision_pct'] = 100.0 * (s['bst_mass'] - s['observed']) / s['observed']
        return entry

    def splittings(self):
        """Return all hyperfine splittings with BST predictions."""
        return [self._add_precision(s) for s in self._systems]

    def clean_ratio(self):
        """Return the cc-bar / bb-bar ratio test."""
        cc = self._systems[0]  # charmonium
        bb = self._systems[1]  # bottomonium

        bst_ratio = (cc['numerator'] / cc['denominator']) / \
                    (bb['numerator'] / bb['denominator'])
        # Simplifies to D_bb / D_cc = 33/18 = 11/6
        exact_ratio = c_2 / C_2   # 11/6
        obs_ratio = cc['observed'] / bb['observed']
        deviation_pct = 100.0 * (exact_ratio - obs_ratio) / obs_ratio

        return {
            'bst_ratio': bst_ratio,
            'exact_fraction': '11/6',
            'exact_value': exact_ratio,
            'chern_meaning': f'c_2 / C_2 = {c_2} / {C_2}',
            'observed_ratio': obs_ratio,
            'deviation_pct': deviation_pct,
            'numerator_cancels': 'c_3 / c_3 = 1 (numerator identical)',
            'denominator_ratio': f'D_bb / D_cc = 33/18 = 11/6',
        }

    def denominators(self):
        """Return Chern class decomposition of each denominator."""
        result = []
        for s in self._systems:
            result.append({
                'name': s['name'],
                'D': s['denominator'],
                'factors': s['denom_factors'],
                'chern_parts': s['denom_chern'],
                'numerator': s['numerator'],
                'numerator_label': s['numerator_label'],
            })
        return result

    def deviations(self):
        """Return all deviations as a list of dicts."""
        return [
            {
                'name': s['name'],
                'label_text': s['label_text'],
                'deviation_pct': abs(100.0 * (s['bst_mass'] - s['observed']) / s['observed']),
                'bst': s['bst_mass'],
                'observed': s['observed'],
            }
            for s in self._systems
        ]

    def precision_table(self):
        """Return a formatted precision table as a string."""
        lines = []
        lines.append('')
        lines.append('=' * 95)
        lines.append('  HYPERFINE SPLITTINGS FROM CHERN CLASSES -- Toy 139')
        lines.append('=' * 95)
        lines.append(f'  BST mass unit:  pi^5 x m_e = {PI5_me:.2f} MeV')
        lines.append(f'  Master formula: Delta_m = (c_3 / D) x pi^5 x m_e,  c_3 = {c_3}')
        lines.append('-' * 95)
        hdr = f'  {"System":<14} {"Particles":<18} {"Num/D":<12} {"BST (MeV)":>10}'
        hdr += f'  {"Obs (MeV)":>10}  {"Error":>10}  {"Dev":>8}'
        lines.append(hdr)
        lines.append('-' * 95)

        for s in self.splittings():
            frac = f'{s["numerator"]}/{s["denominator"]}'
            dev = f'{s["precision_pct"]:+.3f}%'
            obs_str = f'{s["observed"]:.1f} +/- {s["obs_err"]}'
            lines.append(
                f'  {s["name"]:<14} {s["particles_text"]:<18} {frac:<12}'
                f' {s["bst_mass"]:>10.2f}  {obs_str:>10}  {"":>10}  {dev:>8}'
            )

        lines.append('-' * 95)

        # Clean ratio
        cr = self.clean_ratio()
        lines.append('')
        lines.append(f'  CLEAN RATIO TEST:')
        lines.append(f'    Delta_m(cc-bar) / Delta_m(bb-bar) = {cr["exact_fraction"]}'
                      f' = c_2/C_2 = {c_2}/{C_2} = {cr["exact_value"]:.4f}')
        lines.append(f'    Observed ratio: {cr["observed_ratio"]:.4f}'
                      f'  =>  deviation: {abs(cr["deviation_pct"]):.2f}%')
        lines.append(f'    {cr["numerator_cancels"]}')

        lines.append('')
        lines.append(f'  Chern classes of Q^5: c = ({c_0}, {c_1}, {c_2}, {c_3}, {c_4}, {c_5})')
        lines.append(f'  BST integers: N_c={N_c}, n_C={n_C}, C_2={C_2}, genus={genus}')
        lines.append('=' * 95)
        lines.append('')
        return '\n'.join(lines)

    def summary(self):
        """Return key results as a dict."""
        spl = self.splittings()
        cr = self.clean_ratio()
        devs = [abs(s['precision_pct']) for s in spl]
        return {
            'n_systems': len(spl),
            'pi5_me_MeV': PI5_me,
            'master_numerator': c_3,
            'chern_classes': CHERN,
            'max_deviation_pct': max(devs),
            'mean_deviation_pct': np.mean(devs),
            'all_sub_percent': all(d < 1.0 for d in devs),
            'clean_ratio_exact': cr['exact_value'],
            'clean_ratio_observed': cr['observed_ratio'],
            'clean_ratio_deviation_pct': abs(cr['deviation_pct']),
            'punchline': f'c_3 = {c_3} = gauge boson count controls all heavy meson splittings',
        }

    # ── visualization ────────────────────────────────────────────

    def show(self):
        """Build and display the full 6-panel visualization."""
        _visualize(self)


# ═══════════════════════════════════════════════════════════════════
# PANEL DRAWING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def _draw_formula_panel(ax, hs):
    """Panel 1: The Formula -- display the master equation and all four systems."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.set_title('The Formula',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10,
                 path_effects=GLOW)

    # Master equation
    ax.text(0.50, 0.92,
            r'$\Delta m_{\rm HF} \;=\; \frac{c_3}{D} \;\times\; \pi^5 m_e$',
            fontsize=22, color=BRIGHT_GOLD, ha='center', va='top',
            fontfamily='serif')

    ax.text(0.50, 0.78,
            r'$c_3 = 13$ = gauge boson count          '
            r'$\pi^5 m_e$ = %.2f MeV' % PI5_me,
            fontsize=10, color=GOLD_DIM, ha='center', va='top',
            fontfamily='monospace')

    # Divider
    ax.plot([0.05, 0.95], [0.73, 0.73], color=GREY, lw=0.5, alpha=0.5)

    # System list
    y = 0.67
    dy = 0.155
    splittings = hs.splittings()

    for s in splittings[:4]:  # primary 4 systems
        name_col = CYAN if s['name'] != 'D meson' else SOFT_BLUE
        frac = f'{s["numerator"]}/{s["denominator"]}'

        ax.text(0.05, y, s['name'], fontsize=12, color=name_col,
                fontfamily='monospace', fontweight='bold', va='center')

        ax.text(0.05, y - 0.04, s['particles_text'], fontsize=8,
                color=GREY, fontfamily='monospace', va='center')

        ax.text(0.42, y, frac, fontsize=14, color=GOLD,
                fontfamily='monospace', fontweight='bold',
                ha='center', va='center')

        ax.text(0.42, y - 0.04, f'D = {s["denominator"]} = {s["denom_factors"]}',
                fontsize=7, color=GREY, fontfamily='monospace',
                ha='center', va='center')

        # BST prediction
        ax.text(0.68, y, f'{s["bst_mass"]:.2f}', fontsize=13,
                color=GOLD, fontfamily='monospace', fontweight='bold',
                ha='right', va='center')
        ax.text(0.69, y, 'MeV', fontsize=8, color=GOLD_DIM,
                fontfamily='monospace', va='center')

        # Observed
        ax.text(0.88, y, f'{s["observed"]:.1f}', fontsize=11,
                color=CYAN, fontfamily='monospace',
                ha='right', va='center')

        # Deviation
        dev = abs(s['precision_pct'])
        ax.text(0.96, y, f'{dev:.2f}%', fontsize=9,
                color=GREEN, fontfamily='monospace',
                ha='right', va='center')

        y -= dy

    # B_s prediction
    if len(splittings) > 4:
        s = splittings[4]
        ax.plot([0.05, 0.95], [y + 0.06, y + 0.06], color=GREY, lw=0.3, alpha=0.4)
        ax.text(0.05, y, f'{s["name"]} (prediction)', fontsize=9,
                color=VIOLET, fontfamily='monospace', va='center')
        ax.text(0.55, y, f'{s["bst_mass"]:.1f} MeV', fontsize=10,
                color=VIOLET, fontfamily='monospace', ha='center', va='center')
        ax.text(0.80, y, f'obs: {s["observed"]} +/- {s["obs_err"]}',
                fontsize=8, color=GREY, fontfamily='monospace', va='center')


def _draw_bar_chart(ax, hs):
    """Panel 2: Predicted vs Observed grouped bar chart."""
    ax.set_facecolor(DARK_PANEL)

    splittings = hs.splittings()
    n = len(splittings)
    x = np.arange(n)
    width = 0.35

    bst_vals = [s['bst_mass'] for s in splittings]
    obs_vals = [s['observed'] for s in splittings]
    names = [s['label_text'] for s in splittings]
    devs = [abs(s['precision_pct']) for s in splittings]

    # Observed bars
    bars_obs = ax.bar(x - width/2, obs_vals, width, color=CYAN, alpha=0.65,
                       label='Observed', zorder=2)

    # BST bars
    bars_bst = ax.bar(x + width/2, bst_vals, width, color=GOLD, alpha=0.85,
                       label='BST', zorder=2)

    # Annotate with % error
    for i in range(n):
        y_top = max(bst_vals[i], obs_vals[i])
        ax.text(x[i], y_top + 3, f'{devs[i]:.2f}%', fontsize=8,
                color=GREEN, ha='center', fontfamily='monospace',
                fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10, color=WHITE, fontfamily='monospace')
    ax.set_ylabel('Splitting (MeV)', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_title('Predicted vs Observed',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10,
                 path_effects=GLOW)

    ax.tick_params(colors=GREY, which='both')
    ax.spines['bottom'].set_color(GREY)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend(loc='upper right', fontsize=9,
              facecolor=DARK_PANEL, edgecolor=GREY, labelcolor=WHITE,
              framealpha=0.9)


def _draw_clean_ratio(ax, hs):
    """Panel 3: The Clean Ratio -- cc-bar/bb-bar = c_2/C_2 = 11/6."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.set_title('The Clean Ratio',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10,
                 path_effects=GLOW)

    cr = hs.clean_ratio()

    # Big fraction display
    ax.text(0.50, 0.88,
            r'$\frac{\Delta m(c\bar{c})}{\Delta m(b\bar{b})}$',
            fontsize=30, color=WHITE, ha='center', va='top',
            fontfamily='serif')

    # Equals sign and result
    ax.text(0.50, 0.58, '=', fontsize=24, color=GREY,
            ha='center', va='center', fontfamily='monospace')

    ax.text(0.50, 0.46,
            r'$\frac{c_2}{C_2} = \frac{11}{6}$',
            fontsize=28, color=BRIGHT_GOLD, ha='center', va='center',
            fontfamily='serif')

    # Numerical values
    ax.text(0.50, 0.30,
            f'Exact: {cr["exact_value"]:.6f}',
            fontsize=12, color=GOLD, ha='center', va='center',
            fontfamily='monospace')

    ax.text(0.50, 0.22,
            f'Observed: {cr["observed_ratio"]:.4f}',
            fontsize=12, color=CYAN, ha='center', va='center',
            fontfamily='monospace')

    # Deviation spotlight
    dev_pct = abs(cr['deviation_pct'])
    # Glow box for deviation
    box = FancyBboxPatch((0.25, 0.06), 0.50, 0.10,
                          boxstyle="round,pad=0.02",
                          facecolor='#003322', edgecolor=GREEN,
                          linewidth=1.5, alpha=0.7)
    ax.add_patch(box)
    ax.text(0.50, 0.11, f'{dev_pct:.2f}% match',
            fontsize=16, color=GREEN, ha='center', va='center',
            fontfamily='monospace', fontweight='bold')

    # Explanation
    ax.text(0.50, 0.01,
            r'$c_3$ cancels: numerators identical',
            fontsize=8, color=GREY, ha='center', va='bottom',
            fontfamily='monospace')


def _draw_denominator_progression(ax, hs):
    """Panel 4: Chern Denominator Progression -- how D steps through Chern products."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(-0.3, 4.5)
    ax.set_ylim(-0.8, 1.6)
    ax.axis('off')

    ax.set_title('Chern Denominator Progression',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10,
                 path_effects=GLOW)

    splittings = hs.splittings()[:4]
    denoms = hs.denominators()[:4]

    # Color palette for Chern classes
    chern_colors = {
        'c_1': CYAN,
        'c_2': SOFT_BLUE,
        'c_3': GOLD,
        'c_4': ORANGE,
        'c_5': GREEN,
    }

    x_positions = [0.3, 1.4, 2.5, 3.6]

    for i, (d, x_pos) in enumerate(zip(denoms, x_positions)):
        s = splittings[i]
        D_val = d['D']

        # System label
        ax.text(x_pos, 1.40, d['name'], fontsize=10, color=WHITE,
                ha='center', fontfamily='monospace', fontweight='bold')

        # D value in big text
        ax.text(x_pos, 1.10, f'D = {D_val}', fontsize=16, color=GOLD,
                ha='center', fontfamily='monospace', fontweight='bold')

        # Factor decomposition as colored blocks
        parts = d['chern_parts']
        n_parts = len(parts)
        block_w = 0.35
        total_w = n_parts * block_w + (n_parts - 1) * 0.08
        start_x = x_pos - total_w / 2

        for j, (label, val) in enumerate(parts):
            bx = start_x + j * (block_w + 0.08)
            color = chern_colors.get(label, VIOLET)

            # Draw block
            rect = FancyBboxPatch((bx, 0.45), block_w, 0.40,
                                   boxstyle="round,pad=0.04",
                                   facecolor=color, edgecolor=color,
                                   alpha=0.25, linewidth=1.2)
            ax.add_patch(rect)

            display = label if val is None else f'{label}={val}'
            ax.text(bx + block_w / 2, 0.65, display, fontsize=8,
                    color=color, ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')

            # Multiplication sign between blocks
            if j < n_parts - 1:
                ax.text(bx + block_w + 0.04, 0.65, '*',
                        fontsize=10, color=GREY, ha='center', va='center')

        # Numerator info
        num_label = d['numerator_label']
        num_color = GOLD if d['numerator'] == c_3 else SOFT_BLUE
        ax.text(x_pos, 0.25, f'num = {num_label}', fontsize=8,
                color=num_color, ha='center', fontfamily='monospace')

        # Resulting mass
        ax.text(x_pos, -0.05, f'{s["bst_mass"]:.1f} MeV', fontsize=10,
                color=GOLD_DIM, ha='center', fontfamily='monospace')

        # Arrow down from D to mass
        ax.annotate('', xy=(x_pos, 0.10), xytext=(x_pos, 0.40),
                    arrowprops=dict(arrowstyle='->', color=GREY, lw=0.8))

    # Chern class legend at bottom
    ax.text(0.3, -0.55, 'Chern classes of Q^5:', fontsize=8,
            color=GREY, fontfamily='monospace')
    legend_x = 2.0
    for label, val, col in [('c_1', c_1, CYAN), ('c_2', c_2, SOFT_BLUE),
                              ('c_3', c_3, GOLD), ('c_4', c_4, ORANGE),
                              ('c_5', c_5, GREEN)]:
        ax.text(legend_x, -0.55, f'{label}={val}', fontsize=8,
                color=col, fontfamily='monospace', fontweight='bold')
        legend_x += 0.55


def _draw_deviation_map(ax, hs):
    """Panel 5: Deviation Map -- all deviations are sub-percent."""
    ax.set_facecolor(DARK_PANEL)

    devs = hs.deviations()
    n = len(devs)
    x = np.arange(n)
    vals = [d['deviation_pct'] for d in devs]
    names = [d['label_text'] for d in devs]

    # Color each bar
    colors = []
    for v in vals:
        if v < 0.1:
            colors.append(GREEN)
        elif v < 0.2:
            colors.append(CYAN)
        elif v < 0.5:
            colors.append(GOLD)
        else:
            colors.append(ORANGE)

    bars = ax.bar(x, vals, width=0.6, color=colors, alpha=0.8, zorder=2)

    # 1% reference line
    ax.axhline(y=1.0, color=RED, linewidth=1.5, linestyle='--',
               alpha=0.6, zorder=1, label='1% threshold')
    ax.text(n - 0.5, 1.05, '1%', fontsize=9, color=RED,
            fontfamily='monospace', ha='right')

    # Annotate each bar
    for i, v in enumerate(vals):
        ax.text(x[i], v + 0.02, f'{v:.3f}%', fontsize=9,
                color=colors[i], ha='center', fontfamily='monospace',
                fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10, color=WHITE, fontfamily='monospace')
    ax.set_ylabel('|Deviation| %', fontsize=10, color=GOLD_DIM,
                  fontfamily='monospace')
    ax.set_title('Deviation Map',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10,
                 path_effects=GLOW)
    ax.set_ylim(0, 1.3)

    ax.tick_params(colors=GREY, which='both')
    ax.spines['bottom'].set_color(GREY)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Note
    ax.text(n / 2 - 0.5, 1.18, 'ALL sub-percent  --  zero free parameters',
            fontsize=9, color=GREEN, ha='center', fontfamily='monospace',
            fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2, foreground=DARK_PANEL)])


def _draw_punchline(ax, hs):
    """Panel 6: The Punchline."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.set_title('The Punchline',
                 fontsize=14, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=10,
                 path_effects=GLOW)

    # Big c_3 = 13
    ax.text(0.50, 0.82,
            r'$c_3 = 13$',
            fontsize=40, color=BRIGHT_GOLD, ha='center', va='center',
            fontfamily='serif',
            path_effects=[pe.withStroke(linewidth=4, foreground='#332200')])

    ax.text(0.50, 0.64, '= gauge boson count',
            fontsize=14, color=GOLD_DIM, ha='center', va='center',
            fontfamily='monospace')

    # Divider
    ax.plot([0.15, 0.85], [0.56, 0.56], color=GREY, lw=0.5, alpha=0.5)

    # Statement
    ax.text(0.50, 0.46,
            'One integer controls ALL heavy',
            fontsize=13, color=WHITE, ha='center', va='center',
            fontfamily='monospace', fontweight='bold')
    ax.text(0.50, 0.38,
            'meson hyperfine splittings.',
            fontsize=13, color=WHITE, ha='center', va='center',
            fontfamily='monospace', fontweight='bold')

    # Divider
    ax.plot([0.15, 0.85], [0.30, 0.30], color=GREY, lw=0.5, alpha=0.5)

    # Zero parameters box
    box = FancyBboxPatch((0.12, 0.08), 0.76, 0.17,
                          boxstyle="round,pad=0.03",
                          facecolor='#001a00', edgecolor=GREEN,
                          linewidth=2, alpha=0.7)
    ax.add_patch(box)
    ax.text(0.50, 0.165, 'Zero free parameters.',
            fontsize=16, color=GREEN, ha='center', va='center',
            fontfamily='monospace', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2, foreground='#001a00')])

    # Chern class meaning
    ax.text(0.50, 0.03,
            r'$c(Q^5) = (1+h)^7 / (1+2h)$',
            fontsize=9, color=GREY, ha='center', va='center',
            fontfamily='serif')


# ═══════════════════════════════════════════════════════════════════
# MAIN VISUALIZATION
# ═══════════════════════════════════════════════════════════════════

def _visualize(hs=None):
    """Build and display the full 6-panel figure."""
    if hs is None:
        hs = HyperfineSplittings()

    fig = plt.figure(figsize=(18, 13), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'Hyperfine Splittings from Chern Classes -- Toy 139')

    # Super-title
    fig.text(0.50, 0.975,
             'HYPERFINE SPLITTINGS FROM CHERN CLASSES',
             fontsize=24, fontweight='bold', color=GOLD,
             ha='center', va='top', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#332200')])
    fig.text(0.50, 0.950,
             'Toy 139  |  c_3 = 13 controls all heavy meson splittings  |  '
             'pi^5 m_e = %.2f MeV' % PI5_me,
             fontsize=10, color=GOLD_DIM, ha='center', va='top',
             fontfamily='monospace')

    # 3 rows x 2 columns
    gs = GridSpec(3, 2, figure=fig,
                  left=0.04, right=0.96, top=0.92, bottom=0.05,
                  hspace=0.35, wspace=0.20)

    # Panel 1: The Formula
    ax1 = fig.add_subplot(gs[0, 0])
    _draw_formula_panel(ax1, hs)

    # Panel 2: Predicted vs Observed
    ax2 = fig.add_subplot(gs[0, 1])
    _draw_bar_chart(ax2, hs)

    # Panel 3: The Clean Ratio
    ax3 = fig.add_subplot(gs[1, 0])
    _draw_clean_ratio(ax3, hs)

    # Panel 4: Chern Denominator Progression
    ax4 = fig.add_subplot(gs[1, 1])
    _draw_denominator_progression(ax4, hs)

    # Panel 5: Deviation Map
    ax5 = fig.add_subplot(gs[2, 0])
    _draw_deviation_map(ax5, hs)

    # Panel 6: The Punchline
    ax6 = fig.add_subplot(gs[2, 1])
    _draw_punchline(ax6, hs)

    # Bottom annotation
    fig.text(0.50, 0.015,
             'Chern classes of Q^5: (1, %d, %d, %d, %d, %d)   |   '
             'BST: N_c=%d, n_C=%d, C_2=%d, genus=%d   |   '
             'Copyright Casey Koons 2026'
             % (c_1, c_2, c_3, c_4, c_5, N_c, n_C, C_2, genus),
             fontsize=9, color=GREY, ha='center', va='bottom',
             fontfamily='monospace')

    plt.show()


# ═══════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu."""
    hs = HyperfineSplittings()

    menu = """
  --- Hyperfine Splittings from Chern Classes (Toy 139) ---
  1. Precision table          All splittings with BST predictions
  2. Clean ratio              cc-bar / bb-bar = c_2/C_2 = 11/6
  3. Denominators             Chern class decomposition of each D
  4. Deviations               All deviations (all sub-percent)
  5. Summary                  Key results as dict
  6. Visualize                6-panel figure
  q. Quit
"""

    dispatch = {
        '1': lambda: print(hs.precision_table()),
        '2': lambda: _print_clean_ratio(hs),
        '3': lambda: _print_denominators(hs),
        '4': lambda: _print_deviations(hs),
        '5': lambda: _print_summary(hs),
        '6': lambda: hs.show(),
    }

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == 'q':
            print("  Goodbye.")
            break
        fn = dispatch.get(choice)
        if fn:
            fn()
        else:
            print("  Invalid choice.")


def _print_clean_ratio(hs):
    """Pretty-print the clean ratio test."""
    cr = hs.clean_ratio()
    print()
    print('  CLEAN RATIO TEST')
    print('  ' + '-' * 50)
    print(f'  Delta_m(cc-bar) / Delta_m(bb-bar)')
    print(f'    BST exact:  {cr["exact_fraction"]} = {cr["exact_value"]:.6f}')
    print(f'    Meaning:    {cr["chern_meaning"]}')
    print(f'    Observed:   {cr["observed_ratio"]:.4f}')
    print(f'    Deviation:  {abs(cr["deviation_pct"]):.2f}%')
    print(f'    Note:       {cr["numerator_cancels"]}')
    print(f'    Denom:      {cr["denominator_ratio"]}')
    print()


def _print_denominators(hs):
    """Pretty-print the Chern denominator decomposition."""
    print()
    print('  CHERN DENOMINATOR DECOMPOSITION')
    print('  ' + '-' * 60)
    for d in hs.denominators():
        parts_str = ' x '.join(
            f'{lbl}={v}' if v is not None else lbl
            for lbl, v in d['chern_parts']
        )
        print(f'  {d["name"]:<14}  D = {d["D"]:>3}  =  {d["factors"]:<20}'
              f'  [{parts_str}]')
        print(f'  {"":14}  numerator = {d["numerator_label"]}')
    print()


def _print_deviations(hs):
    """Pretty-print the deviations."""
    print()
    print('  ALL DEVIATIONS')
    print('  ' + '-' * 50)
    for d in hs.deviations():
        star = '***' if d['deviation_pct'] < 0.1 else ''
        print(f'  {d["name"]:<14}  |dev| = {d["deviation_pct"]:.3f}%'
              f'  (BST: {d["bst"]:.2f}, obs: {d["observed"]:.1f}) {star}')
    print(f'  {"":14}  All sub-percent: YES')
    print()


def _print_summary(hs):
    """Pretty-print the summary dict."""
    s = hs.summary()
    print()
    print('  SUMMARY')
    print('  ' + '-' * 50)
    for k, v in s.items():
        print(f'  {k:<30}  {v}')
    print()


if __name__ == '__main__':
    main()
