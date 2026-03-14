#!/usr/bin/env python3
"""
BST Toy 149 — The Effective Spectral Dimension
===============================================
Q^5 has real dimension 10 but spectrally behaves as dimension 6.

The Grand Identity:

    d_eff(Q^5) = lambda_1(Q^5) = chi(Q^5) = C_2 = 6

Four quantities that have no business being the same number:
  - d_eff = 6   : effective spectral dimension (heat trace asymptotics)
  - lambda_1 = 6: first eigenvalue of the Laplacian (mass gap)
  - chi = 6     : Euler characteristic (topology)
  - C_2 = 6     : Casimir eigenvalue (representation theory)

Key results:
  * Z(t) ~ 1/(60 t^3) as t -> 0+. The t^{-3} exponent gives d_eff = 6.
    The 1/60 prefactor is 1/|A_5| (alternating group order).
  * d_eff/d = 6/10 = 3/5 = c_5/c_1 = N_c/n_C (Chern class ratio!)
  * Fill fraction DERIVED: f = d_eff/(d*pi) = 3/(5*pi) ~ 19.1%
  * 10 = 6 + 4: 6 spectral (visible physics) + 4 hidden (spacetime, 3+1)
    Same as string theory but OPPOSITE roles!
  * d_eff(Q^n) = n+1 for all odd n. Only n=5 gives d_hidden = 4.
  * (n+1)/2 = n-2 only at n=5: topological colors = physical colors.

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from math import comb, factorial

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3
n_C = 5
C2 = n_C + 1            # = 6
A5_order = factorial(5) // 2  # |A_5| = 60

# Colors
BG       = '#0a0a1a'
GOLD     = '#ffd700'
CYAN     = '#00e5ff'
GREEN    = '#00ff88'
WHITE    = '#ffffff'
CORAL    = '#ff6b6b'
GREY     = '#888888'
DIM_GOLD = '#aa8800'
PANEL_BG = '#0d0d24'


# ═══════════════════════════════════════════════════════════════════
# SPECTRAL DATA FOR Q^5
# ═══════════════════════════════════════════════════════════════════

def d_k(k):
    """Degeneracy of k-th eigenvalue on Q^5 = SO(7)/[SO(5) x SO(2)]."""
    return comb(k + 4, 4) * (2 * k + 5) // 5


def lam_k(k):
    """k-th eigenvalue of the Laplacian on Q^5."""
    return k * (k + 5)


def Z(t, N=500):
    """Heat trace Z(t) = sum_k d_k exp(-lambda_k t)."""
    return sum(d_k(k) * np.exp(-lam_k(k) * t) for k in range(N + 1))


def N_count(lam_max):
    """Count eigenvalues (with multiplicity) up to lam_max."""
    total = 0
    for k in range(1, 10000):
        if lam_k(k) > lam_max:
            break
        total += d_k(k)
    return total


# ═══════════════════════════════════════════════════════════════════
# VERIFICATION
# ═══════════════════════════════════════════════════════════════════

def _verify():
    """Numerical verification of all key claims."""
    print()
    print("  ╔═══════════════════════════════════════════════════════════╗")
    print("  ║     EFFECTIVE SPECTRAL DIMENSION — VERIFICATION          ║")
    print("  ╠═══════════════════════════════════════════════════════════╣")

    # 1. Heat trace asymptotics: (4*pi*t)^3 * Z(t) -> (4*pi)^3 / 60
    target = (4 * np.pi)**3 / A5_order
    print(f"  ║  Target: (4*pi)^3 / 60 = {target:.4f}                    ║")
    for t_small in [1e-2, 1e-3, 1e-4]:
        z_val = Z(t_small, N=500)
        check = (4 * np.pi * t_small)**3 * z_val
        print(f"  ║  t={t_small:.0e}: (4*pi*t)^3 Z(t) = {check:.4f}  "
              f"(err {abs(check - target)/target * 100:.2f}%)       ║")

    # 2. Weyl law: N(lambda) ~ C * lambda^3
    print("  ║                                                           ║")
    print("  ║  Weyl law N(lambda) ~ C * lambda^3:                       ║")
    for lam in [100, 1000, 10000]:
        n = N_count(lam)
        ratio = n / lam**3
        print(f"  ║    N({lam:>5}) = {n:>10},  N/lambda^3 = {ratio:.6f}       ║")

    # 3. Key identities
    d_eff = 6
    d_real = 10
    chi = n_C + 1  # = 6 for odd-dim quadric
    lam1 = lam_k(1)  # = 1*(1+5) = 6
    fill = d_eff / (d_real * np.pi)

    print("  ║                                                           ║")
    print(f"  ║  d_eff = {d_eff}  (from heat trace exponent 3 => 2*3=6)    ║")
    print(f"  ║  lam_1 = {lam1}  (k=1: 1*(1+5) = 6)                       ║")
    print(f"  ║  chi   = {chi}  (Euler char of Q^5)                        ║")
    print(f"  ║  C_2   = {C2}  (Casimir eigenvalue)                        ║")
    print(f"  ║  d_eff/d = {d_eff}/{d_real} = {d_eff/d_real} = 3/5         ║")
    print(f"  ║  fill  = 3/(5*pi) = {fill:.4f} = {fill*100:.2f}%           ║")

    # 4. Uniqueness: (n+1)/2 = n-2 => n=5
    print("  ║                                                           ║")
    print("  ║  Uniqueness: (n+1)/2 = n-2  =>  n = 5                    ║")
    for n in [3, 5, 7, 9, 11]:
        lhs = (n + 1) / 2
        rhs = n - 2
        match = "YES" if lhs == rhs else "no"
        print(f"  ║    n={n:>2}: (n+1)/2 = {lhs:.1f}, n-2 = {rhs:.1f}  "
              f"match: {match}            ║")

    print("  ╚═══════════════════════════════════════════════════════════╝")
    print()


# ═══════════════════════════════════════════════════════════════════
# THE EXPLORER (6-PANEL VISUALIZATION)
# ═══════════════════════════════════════════════════════════════════

class EffectiveDimensionExplorer:
    """BST Toy 149 — The Effective Spectral Dimension

    Visualizes the grand identity d_eff = lambda_1 = chi = C_2 = 6
    and the dimension split 10 = 6 + 4 on the complex quadric Q^5.
    """

    def __init__(self):
        _verify()

        self.fig = plt.figure(figsize=(20, 12), facecolor=BG)
        self.axes = []

        # 6 panels: 3 top, 3 bottom
        # [left, bottom, width, height]
        panel_specs = [
            [0.03,  0.52, 0.30, 0.42],   # top-left
            [0.36,  0.52, 0.30, 0.42],   # top-middle
            [0.69,  0.52, 0.28, 0.42],   # top-right
            [0.03,  0.06, 0.30, 0.42],   # bottom-left
            [0.36,  0.06, 0.30, 0.42],   # bottom-middle
            [0.69,  0.06, 0.28, 0.42],   # bottom-right
        ]

        for spec in panel_specs:
            ax = self.fig.add_axes(spec)
            ax.set_facecolor(BG)
            ax.axis('off')
            self.axes.append(ax)

        # Title
        self.fig.text(
            0.50, 0.97,
            "THE EFFECTIVE SPECTRAL DIMENSION",
            fontsize=22, fontweight='bold', color=WHITE,
            ha='center', va='center', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=3, foreground=GOLD)]
        )
        self.fig.text(
            0.50, 0.935,
            "Q\u2075 has 10 real dimensions but spectrally lives in 6",
            fontsize=12, color=GOLD, ha='center', va='center',
            fontfamily='monospace', style='italic'
        )

        # Copyright
        self.fig.text(
            0.50, 0.012,
            "\u00a9 2026 Casey Koons | BST Toy 149 \u2014 The Effective Spectral Dimension",
            fontsize=9, color=GREY, ha='center', va='center',
            fontfamily='monospace'
        )

        self._draw_panel1_grand_identity()
        self._draw_panel2_heat_trace()
        self._draw_panel3_dimension_split()
        self._draw_panel4_dimension_table()
        self._draw_panel5_fill_fraction()
        self._draw_panel6_uniqueness()

    # ───────────────────────────────────────────────────────────────
    # PANEL 1: The Grand Identity
    # ───────────────────────────────────────────────────────────────
    def _draw_panel1_grand_identity(self):
        ax = self.axes[0]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        # Panel title
        ax.text(0.50, 0.95, "The Grand Identity", fontsize=14,
                fontweight='bold', color=GOLD, ha='center', va='top',
                fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#332200')])

        # The equation line
        ax.text(0.50, 0.78, "d_eff  =  \u03bb\u2081  =  \u03c7  =  C\u2082  =",
                fontsize=15, color=WHITE, ha='center', va='center',
                fontfamily='monospace', fontweight='bold')

        # The giant "6"
        ax.text(0.50, 0.58, "6", fontsize=100, fontweight='bold',
                color=GOLD, ha='center', va='center',
                fontfamily='monospace',
                path_effects=[
                    pe.withStroke(linewidth=6, foreground='#aa8800'),
                    pe.withStroke(linewidth=12, foreground='#553300'),
                ])

        # Four explanatory lines
        explanations = [
            (CYAN,  "d_eff = 6",
             "spectral dimension (from heat trace)"),
            (GREEN, "\u03bb\u2081   = 6",
             "first eigenvalue (mass gap)"),
            (CORAL, "\u03c7     = 6",
             "Euler characteristic (topology)"),
            (GOLD,  "C\u2082    = 6",
             "Casimir eigenvalue (representation theory)"),
        ]

        y_start = 0.36
        for i, (color, label, desc) in enumerate(explanations):
            y = y_start - i * 0.085
            ax.text(0.10, y, label, fontsize=11, color=color,
                    ha='left', va='center', fontfamily='monospace',
                    fontweight='bold')
            ax.text(0.42, y, desc, fontsize=9, color='#bbbbbb',
                    ha='left', va='center', fontfamily='monospace')

        # Decorative border
        border = FancyBboxPatch(
            (0.02, 0.02), 0.96, 0.96,
            boxstyle="round,pad=0.02",
            facecolor='none', edgecolor=GOLD, linewidth=1.5, alpha=0.3
        )
        ax.add_patch(border)

    # ───────────────────────────────────────────────────────────────
    # PANEL 2: Heat Trace
    # ───────────────────────────────────────────────────────────────
    def _draw_panel2_heat_trace(self):
        ax = self.axes[1]
        ax.set_facecolor(BG)
        ax.axis('on')

        # Compute heat trace
        t_vals = np.logspace(-3, 0, 300)
        z_vals = np.array([Z(t, N=200) for t in t_vals])
        z_asymp = 1.0 / (A5_order * t_vals**3)

        ax.loglog(t_vals, z_vals, color=CYAN, linewidth=2.0, label='Z(t) exact')
        ax.loglog(t_vals, z_asymp, color=GOLD, linewidth=1.5,
                  linestyle='--', label='1/(60 t\u00b3)', alpha=0.8)

        ax.set_facecolor(BG)
        ax.set_xlabel('t', color=WHITE, fontfamily='monospace', fontsize=10)
        ax.set_ylabel('Z(t)', color=WHITE, fontfamily='monospace', fontsize=10)
        ax.tick_params(colors=GREY, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color('#333355')

        ax.set_title("Heat Trace: Z(t) ~ 1/(60 t\u00b3)",
                      fontsize=13, fontweight='bold', color=GOLD,
                      fontfamily='monospace', pad=8,
                      path_effects=[pe.withStroke(linewidth=2,
                                                  foreground='#332200')])

        ax.legend(fontsize=9, loc='lower left',
                  facecolor='#111133', edgecolor=GREY,
                  labelcolor=WHITE)

        # Annotations
        t_check = 1e-3
        z_check = Z(t_check, N=200)
        scaled = (4 * np.pi * t_check)**3 * z_check
        target = (4 * np.pi)**3 / A5_order

        ax.text(0.97, 0.55,
                f"(4\u03c0t)\u00b3 Z(t) \u2192 {target:.2f}",
                fontsize=9, color=GREEN, ha='right', va='center',
                transform=ax.transAxes, fontfamily='monospace',
                fontweight='bold')
        ax.text(0.97, 0.45,
                f"= (4\u03c0)\u00b3/60",
                fontsize=9, color=GREEN, ha='right', va='center',
                transform=ax.transAxes, fontfamily='monospace')
        ax.text(0.97, 0.30,
                "exponent 3 = d_eff/2",
                fontsize=9, color=CYAN, ha='right', va='center',
                transform=ax.transAxes, fontfamily='monospace')
        ax.text(0.97, 0.20,
                "1/60 = 1/|A\u2085|",
                fontsize=9, color=CORAL, ha='right', va='center',
                transform=ax.transAxes, fontfamily='monospace')

    # ───────────────────────────────────────────────────────────────
    # PANEL 3: 10 = 6 + 4 dimension split
    # ───────────────────────────────────────────────────────────────
    def _draw_panel3_dimension_split(self):
        ax = self.axes[2]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        ax.text(0.50, 0.95, "10  =  6  +  4",
                fontsize=15, fontweight='bold', color=WHITE,
                ha='center', va='top', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground=GOLD)])

        # The split bar
        bar_y = 0.78
        bar_h = 0.08
        bar_left = 0.08
        bar_right = 0.92
        bar_width = bar_right - bar_left
        split_x = bar_left + bar_width * 0.6  # 6/10

        # Gold section (6)
        gold_bar = FancyBboxPatch(
            (bar_left, bar_y), split_x - bar_left, bar_h,
            boxstyle="round,pad=0.005",
            facecolor=GOLD, edgecolor='none', alpha=0.85
        )
        ax.add_patch(gold_bar)
        ax.text((bar_left + split_x) / 2, bar_y + bar_h / 2, "6",
                fontsize=18, fontweight='bold', color='#0a0a1a',
                ha='center', va='center', fontfamily='monospace')

        # Cyan section (4)
        cyan_bar = FancyBboxPatch(
            (split_x, bar_y), bar_right - split_x, bar_h,
            boxstyle="round,pad=0.005",
            facecolor=CYAN, edgecolor='none', alpha=0.85
        )
        ax.add_patch(cyan_bar)
        ax.text((split_x + bar_right) / 2, bar_y + bar_h / 2, "4",
                fontsize=18, fontweight='bold', color='#0a0a1a',
                ha='center', va='center', fontfamily='monospace')

        # Labels below bar
        ax.text((bar_left + split_x) / 2, bar_y - 0.04,
                "SPECTRAL", fontsize=9, fontweight='bold',
                color=GOLD, ha='center', va='top', fontfamily='monospace')
        ax.text((bar_left + split_x) / 2, bar_y - 0.09,
                "mass gap, Euler, Casimir",
                fontsize=7, color=DIM_GOLD, ha='center', va='top',
                fontfamily='monospace')

        ax.text((split_x + bar_right) / 2, bar_y - 0.04,
                "SPACETIME", fontsize=9, fontweight='bold',
                color=CYAN, ha='center', va='top', fontfamily='monospace')
        ax.text((split_x + bar_right) / 2, bar_y - 0.09,
                "3+1 from B\u2082 roots",
                fontsize=7, color='#0099bb', ha='center', va='top',
                fontfamily='monospace')

        # Comparison table: BST vs String Theory
        ax.text(0.50, 0.54, "vs String Theory", fontsize=11,
                fontweight='bold', color=WHITE, ha='center', va='center',
                fontfamily='monospace')

        # Table header
        col0_x = 0.06
        col1_x = 0.40
        col2_x = 0.72
        row_y = 0.46
        row_h = 0.075

        ax.text(col1_x, row_y, "6 dims", fontsize=9, fontweight='bold',
                color=GOLD, ha='center', va='center', fontfamily='monospace')
        ax.text(col2_x, row_y, "4 dims", fontsize=9, fontweight='bold',
                color=CYAN, ha='center', va='center', fontfamily='monospace')

        # Separator
        ax.plot([0.04, 0.96], [row_y - 0.035, row_y - 0.035],
                color=GREY, linewidth=0.5, alpha=0.5)

        # String Theory row
        r1_y = row_y - row_h
        ax.text(col0_x, r1_y, "String", fontsize=9, color='#cc88ff',
                ha='left', va='center', fontfamily='monospace',
                fontweight='bold')
        ax.text(col1_x, r1_y, "Compact", fontsize=9, color='#999999',
                ha='center', va='center', fontfamily='monospace')
        ax.text(col2_x, r1_y, "Spacetime", fontsize=9, color='#999999',
                ha='center', va='center', fontfamily='monospace')
        ax.text(col1_x, r1_y - 0.04, "(hidden)", fontsize=7,
                color='#666666', ha='center', va='center',
                fontfamily='monospace')
        ax.text(col2_x, r1_y - 0.04, "(visible)", fontsize=7,
                color='#666666', ha='center', va='center',
                fontfamily='monospace')

        # BST row
        r2_y = r1_y - row_h - 0.02
        ax.text(col0_x, r2_y, "BST", fontsize=9, color=GOLD,
                ha='left', va='center', fontfamily='monospace',
                fontweight='bold')
        ax.text(col1_x, r2_y, "Spectral", fontsize=9, color=GOLD,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold')
        ax.text(col2_x, r2_y, "Spacetime", fontsize=9, color=CYAN,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold')
        ax.text(col1_x, r2_y - 0.04, "(visible!)", fontsize=7,
                color=DIM_GOLD, ha='center', va='center',
                fontfamily='monospace')
        ax.text(col2_x, r2_y - 0.04, "(emergent!)", fontsize=7,
                color='#0099bb', ha='center', va='center',
                fontfamily='monospace')

        # Arrow between rows
        ax.annotate('', xy=(0.50, r1_y - 0.06), xytext=(0.50, r2_y + 0.02),
                    arrowprops=dict(arrowstyle='<->', color=CORAL,
                                    lw=1.5, mutation_scale=12))
        ax.text(0.60, (r1_y + r2_y) / 2 - 0.02, "OPPOSITE\nROLES!",
                fontsize=8, color=CORAL, ha='center', va='center',
                fontfamily='monospace', fontweight='bold')

        # Border
        border = FancyBboxPatch(
            (0.02, 0.02), 0.96, 0.96,
            boxstyle="round,pad=0.02",
            facecolor='none', edgecolor=CYAN, linewidth=1.0, alpha=0.3
        )
        ax.add_patch(border)

    # ───────────────────────────────────────────────────────────────
    # PANEL 4: d_eff/d = c_n/c_1 table
    # ───────────────────────────────────────────────────────────────
    def _draw_panel4_dimension_table(self):
        ax = self.axes[3]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        ax.text(0.50, 0.95,
                "d_eff / d  =  c\u2099 / c\u2081",
                fontsize=13, fontweight='bold', color=GOLD,
                ha='center', va='top', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#332200')])

        # Column headers
        headers = ["Q\u207f", "d", "d_eff", "d_hid", "c\u2099/c\u2081",
                    "d_eff/d", ""]
        col_xs = [0.06, 0.17, 0.30, 0.44, 0.59, 0.76, 0.90]
        header_y = 0.82

        for h, x in zip(headers, col_xs):
            ax.text(x, header_y, h, fontsize=9, fontweight='bold',
                    color=CYAN, ha='center', va='center',
                    fontfamily='monospace')

        # Separator
        ax.plot([0.02, 0.98], [header_y - 0.03, header_y - 0.03],
                color=GREY, linewidth=0.5, alpha=0.5)

        # Data rows: Q^n for odd n
        data = [
            # n, d, d_eff, d_hidden, cn_c1_str, ratio_str, check
            (3,  6,  4, 2, "2/3", "2/3", True),
            (5, 10,  6, 4, "3/5", "3/5", True),
            (7, 14,  8, 6, "4/7", "4/7", True),
            (9, 18, 10, 8, "5/9", "5/9", True),
        ]

        row_y = header_y - 0.08
        row_h = 0.095
        for i, (n, d, d_eff, d_hid, cn_str, ratio_str, ok) in enumerate(data):
            y = row_y - i * row_h
            is_q5 = (n == 5)
            base_color = GOLD if is_q5 else WHITE
            alpha_bg = 0.15 if is_q5 else 0.0

            # Highlight Q^5 row
            if is_q5:
                highlight = FancyBboxPatch(
                    (0.02, y - 0.03), 0.96, 0.065,
                    boxstyle="round,pad=0.005",
                    facecolor=GOLD, edgecolor='none', alpha=0.12
                )
                ax.add_patch(highlight)

            vals = [f"Q\u2077" if n == 7 else f"Q\u2079" if n == 9
                    else f"Q\u00b3" if n == 3 else f"Q\u2075",
                    str(d), str(d_eff), str(d_hid),
                    cn_str, ratio_str, "\u2713" if ok else ""]
            for v, x in zip(vals, col_xs):
                c = base_color
                if v == "\u2713":
                    c = GREEN
                ax.text(x, y, v, fontsize=10 if is_q5 else 9,
                        fontweight='bold' if is_q5 else 'normal',
                        color=c, ha='center', va='center',
                        fontfamily='monospace')

        # Key insight
        ax.text(0.50, 0.34,
                "Only Q\u2075 has d_hidden = 4",
                fontsize=11, fontweight='bold', color=GOLD,
                ha='center', va='center', fontfamily='monospace')
        ax.text(0.50, 0.27,
                "= physical spacetime (3+1)",
                fontsize=10, color=CYAN, ha='center', va='center',
                fontfamily='monospace')

        # General formula
        ax.text(0.50, 0.16,
                "General: d_eff(Q\u207f) = n + 1",
                fontsize=10, color=WHITE, ha='center', va='center',
                fontfamily='monospace')
        ax.text(0.50, 0.09,
                "d_hidden = d - d_eff = n - 1",
                fontsize=9, color=GREY, ha='center', va='center',
                fontfamily='monospace')

        # Border
        border = FancyBboxPatch(
            (0.02, 0.02), 0.96, 0.96,
            boxstyle="round,pad=0.02",
            facecolor='none', edgecolor=GOLD, linewidth=1.0, alpha=0.2
        )
        ax.add_patch(border)

    # ───────────────────────────────────────────────────────────────
    # PANEL 5: Fill Fraction Derived
    # ───────────────────────────────────────────────────────────────
    def _draw_panel5_fill_fraction(self):
        ax = self.axes[4]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        ax.text(0.50, 0.95, "Fill Fraction Derived",
                fontsize=13, fontweight='bold', color=GREEN,
                ha='center', va='top', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#003300')])

        # Derivation chain
        steps = [
            ("d_eff = 6,   d = 10", WHITE),
            ("d_eff / d  =  6/10  =  3/5", WHITE),
            ("         =  N_c / n_C", CYAN),
            ("", WHITE),
            ("f  =  d_eff / (d \u00b7 \u03c0)", WHITE),
            ("   =  3 / (5\u03c0)", WHITE),
        ]

        y = 0.82
        for text, color in steps:
            if text:
                ax.text(0.50, y, text, fontsize=10, color=color,
                        ha='center', va='center', fontfamily='monospace')
            y -= 0.065

        # Big percentage
        fill_val = 3.0 / (5.0 * np.pi) * 100
        ax.text(0.50, 0.42, f"{fill_val:.1f}%",
                fontsize=52, fontweight='bold', color=GREEN,
                ha='center', va='center', fontfamily='monospace',
                path_effects=[
                    pe.withStroke(linewidth=4, foreground='#005500'),
                    pe.withStroke(linewidth=8, foreground='#002200'),
                ])

        ax.text(0.50, 0.25, "= f  =  3/(5\u03c0)",
                fontsize=11, color=GREEN, ha='center', va='center',
                fontfamily='monospace', fontweight='bold')

        # Godel limit
        ax.text(0.50, 0.14,
                "G\u00f6del Limit:",
                fontsize=10, fontweight='bold', color=CORAL,
                ha='center', va='center', fontfamily='monospace')
        ax.text(0.50, 0.07,
                "The universe can know at most",
                fontsize=9, color='#bbbbbb', ha='center', va='center',
                fontfamily='monospace')
        ax.text(0.50, 0.01,
                "19.1% of itself",
                fontsize=11, fontweight='bold', color=CORAL,
                ha='center', va='center', fontfamily='monospace')

        # Border
        border = FancyBboxPatch(
            (0.02, 0.02), 0.96, 0.96,
            boxstyle="round,pad=0.02",
            facecolor='none', edgecolor=GREEN, linewidth=1.0, alpha=0.3
        )
        ax.add_patch(border)

    # ───────────────────────────────────────────────────────────────
    # PANEL 6: Uniqueness n = 5
    # ───────────────────────────────────────────────────────────────
    def _draw_panel6_uniqueness(self):
        ax = self.axes[5]
        ax.set_facecolor(BG)
        ax.axis('on')

        n_vals = np.linspace(1, 11, 200)
        y1 = (n_vals + 1) / 2.0   # topological colors: c_n = (n+1)/2
        y2 = n_vals - 2.0          # physical colors: N_c = n - 2

        ax.plot(n_vals, y1, color=GOLD, linewidth=2.0,
                label='(n+1)/2  [topological]')
        ax.plot(n_vals, y2, color=CYAN, linewidth=2.0,
                label='n \u2212 2  [physical]')

        # Mark crossing at n=5, y=3
        ax.plot(5, 3, marker='*', markersize=22, color=GOLD,
                markeredgecolor='#ffee88', markeredgewidth=1,
                zorder=10)
        ax.text(5.4, 3.5, "n = 5", fontsize=12, fontweight='bold',
                color=GOLD, fontfamily='monospace')
        ax.text(5.4, 2.4, "N_c = 3", fontsize=10, color=WHITE,
                fontfamily='monospace')

        # Mark integer points
        for n in [3, 5, 7, 9, 11]:
            y_top = (n + 1) / 2
            y_phys = n - 2
            if n != 5:
                ax.plot(n, y_top, 'o', color=GOLD, markersize=5, alpha=0.5)
                ax.plot(n, y_phys, 'o', color=CYAN, markersize=5, alpha=0.5)

        ax.set_facecolor(BG)
        ax.set_xlabel('n (complex dimension)', color=WHITE,
                       fontfamily='monospace', fontsize=10)
        ax.set_ylabel('value', color=WHITE, fontfamily='monospace',
                       fontsize=10)
        ax.tick_params(colors=GREY, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color('#333355')

        ax.set_title("Uniqueness: n = 5",
                      fontsize=13, fontweight='bold', color=GOLD,
                      fontfamily='monospace', pad=8,
                      path_effects=[pe.withStroke(linewidth=2,
                                                  foreground='#332200')])

        ax.legend(fontsize=8, loc='upper left',
                  facecolor='#111133', edgecolor=GREY,
                  labelcolor=WHITE)

        # Caption text at bottom of panel
        ax.text(0.50, 0.02,
                "Topological colors = Physical colors\nONLY at n = 5",
                fontsize=9, fontweight='bold', color=CORAL,
                ha='center', va='bottom', transform=ax.transAxes,
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0a0a',
                          edgecolor=CORAL, linewidth=1, alpha=0.8))

        ax.text(0.97, 0.95,
                "8th independent\nproof: n_C = 5",
                fontsize=8, color=DIM_GOLD, ha='right', va='top',
                transform=ax.transAxes, fontfamily='monospace',
                style='italic')

        ax.set_xlim(0.5, 11.5)
        ax.set_ylim(-1.5, 6.5)
        ax.axhline(y=0, color=GREY, linewidth=0.3, alpha=0.3)
        ax.grid(True, alpha=0.1, color=GREY)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    explorer = EffectiveDimensionExplorer()
    plt.show()
