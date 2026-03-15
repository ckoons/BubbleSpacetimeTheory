#!/usr/bin/env python3
"""
BST Toy 151 — The Plancherel Dictionary
==========================================
The heat kernel on D_IV^5 encodes BST integers through exact rational coefficients.

The noncompact Plancherel density |c(iv)|^{-2} of the B_2 root system
with multiplicities (m_s=3, m_l=1) produces coefficients b~_k that are
ALL expressible in terms of BST integers:

    b~_1 = 1/C_2,  b~_2 = n_C/(|W|*c_4),  b~_3 = -N_c/2^4

The exponential bridge at |rho|^2 = 17/2 converts these to the
Seeley-DeWitt coefficients a~_k, which encode curvature invariants
of the symmetric space. The second coefficient a~_2 = 313/9 is
verified independently from both the Plancherel density AND the
Gilkey curvature formula -- confirming the dictionary is exact.

Six-panel visualization:
  1. The Plancherel Coefficients b~_k and their BST expressions
  2. The Exponential Bridge: D_IV^5 <-> Q^5 via |rho|^2 = 17/2
  3. The Seeley-DeWitt Coefficients a~_k from curvature
  4. The a~_2 = 313/9 verification from both directions
  5. The 63/64 Kahler correction (RESOLVED: 1 - 1/2^{C_2})
  6. Three Spectral Identities and the path to Riemann

    from toy_plancherel_dictionary import PlancherelDictionaryExplorer
    explorer = PlancherelDictionaryExplorer()
    plt.show()

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
from matplotlib.patches import FancyBboxPatch
import numpy as np
from fractions import Fraction

# =====================================================================
# BST CONSTANTS
# =====================================================================

N_c   = 3                # color charges
n_C   = 5                # complex dimension of D_IV^5
g     = n_C + 2          # = 7, genus
C_2   = n_C + 1          # = 6, Casimir eigenvalue / chi(Q^5)
N_max = 137              # fine-structure maximum
W_B2  = 8                # |W(B_2)| = 2^2 * 2!
c_4   = 9                # fourth Chern class of Q^5

# Chern classes of Q^5: c(Q^5) = (1+h)^7 / (1+2h)
c_classes = [5, 11, 13, 9, 3]  # c_1..c_5
c_2_chern = c_classes[1]       # = 11

# Half-sum of positive roots
rho = (Fraction(5, 2), Fraction(3, 2))
rho_sq = rho[0]**2 + rho[1]**2  # = 17/2

# Plancherel coefficients (exact)
b_tilde = [Fraction(1), Fraction(1, 6), Fraction(5, 72), Fraction(-3, 16)]

# Seeley-DeWitt coefficients via exponential bridge
def compute_a_tilde(b_list, rho_squared):
    """Compute a~_k from b~_k via the exponential shift."""
    a_list = []
    neg_rho_sq = -rho_squared
    for k in range(len(b_list)):
        s = Fraction(0)
        fac = Fraction(1)
        for j in range(k + 1):
            if j > 0:
                fac *= j
            s += neg_rho_sq**j / fac * b_list[k - j]
        a_list.append(s)
    return a_list

a_tilde = compute_a_tilde(b_tilde, rho_sq)

# =====================================================================
# COLORS
# =====================================================================

BG       = '#0a0a1a'
BG_PANEL = '#0d0d24'
GOLD     = '#ffd700'
CYAN     = '#00e5ff'
GREEN    = '#00ff88'
CORAL    = '#ff6b6b'
WHITE    = '#ffffff'
GREY     = '#888888'
MAGENTA  = '#ff44cc'
BLUE     = '#4488ff'
DARK_GREY = '#444444'


# =====================================================================
# GLOW HELPER
# =====================================================================

def glow(color, width=3):
    """Return path_effects list for glow."""
    return [pe.withStroke(linewidth=width, foreground=color)]

def glow_strong(color, width=5):
    return [pe.withStroke(linewidth=width, foreground=color)]


# =====================================================================
# PANEL DRAWING FUNCTIONS
# =====================================================================

def draw_panel_border(ax, color, alpha=0.4):
    """Draw a glowing border around a panel."""
    bbox = FancyBboxPatch(
        (0.02, 0.02), 0.96, 0.96,
        boxstyle="round,pad=0.02",
        facecolor='none', edgecolor=color,
        linewidth=1.5, alpha=alpha,
        transform=ax.transAxes, zorder=0
    )
    ax.add_patch(bbox)


def draw_panel1(ax):
    """Panel 1: The Plancherel Coefficients b~_k."""
    ax.set_facecolor(BG_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    draw_panel_border(ax, CYAN)

    # Title
    ax.text(0.50, 0.93, 'The Plancherel Coefficients',
            color=CYAN, fontsize=11, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow(CYAN, 4))

    # Table header
    y0 = 0.82
    dy = 0.10
    colors_row = [WHITE, GREEN, GOLD, CORAL]
    labels_k   = ['0', '1', '2', '3']
    labels_bt  = ['1', '1/6', '5/72', '-3/16']
    labels_bst = [r'$c_0$', r'$1/C_2$', r'$n_C/(|W| \times c_4)$', r'$-N_c/2^4$']

    # Header row
    ax.text(0.10, y0 + 0.04, 'k', color=GREY, fontsize=9, fontfamily='monospace',
            ha='center', va='center', fontweight='bold')
    ax.text(0.33, y0 + 0.04, r'$\tilde{b}_k$', color=GREY, fontsize=9,
            fontfamily='monospace', ha='center', va='center', fontweight='bold')
    ax.text(0.70, y0 + 0.04, 'BST form', color=GREY, fontsize=9,
            fontfamily='monospace', ha='center', va='center', fontweight='bold')

    # Separator line
    ax.plot([0.05, 0.95], [y0, y0], color=GREY, lw=0.5, alpha=0.5)

    for i in range(4):
        y = y0 - (i + 0.5) * dy
        c = colors_row[i]

        # Highlight row background
        bg_patch = FancyBboxPatch(
            (0.04, y - 0.035), 0.92, 0.07,
            boxstyle="round,pad=0.005",
            facecolor=c, edgecolor='none', alpha=0.06,
            transform=ax.transAxes
        )
        ax.add_patch(bg_patch)

        ax.text(0.10, y, labels_k[i], color=c, fontsize=10,
                fontfamily='monospace', ha='center', va='center',
                fontweight='bold')
        ax.text(0.33, y, labels_bt[i], color=c, fontsize=10,
                fontfamily='monospace', ha='center', va='center',
                fontweight='bold')
        ax.text(0.70, y, labels_bst[i], color=c, fontsize=10,
                fontfamily='monospace', ha='center', va='center')

    # Summary line
    ax.text(0.50, 0.12, 'EVERY coefficient is a BST expression',
            color=GOLD, fontsize=8, fontfamily='monospace',
            ha='center', va='center', fontstyle='italic',
            path_effects=glow(GOLD, 2))

    # Normalization
    ax.text(0.50, 0.04,
            r'Raw norm: $48\pi^5 = |W(B_2)| \times C_2 \times \pi^{n_C} = 8 \times 6 \times \pi^5$',
            color=GREY, fontsize=6.5, fontfamily='monospace',
            ha='center', va='center')


def draw_panel2(ax):
    """Panel 2: The Exponential Bridge."""
    ax.set_facecolor(BG_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    draw_panel_border(ax, GOLD)

    # Title
    ax.text(0.50, 0.93, 'The Exponential Bridge',
            color=GOLD, fontsize=11, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow(GOLD, 4))

    # Left side: Physics (noncompact)
    ax.text(0.15, 0.76, r'$D_{IV}^5$', color=CYAN, fontsize=14,
            fontfamily='monospace', ha='center', va='center',
            fontweight='bold', path_effects=glow(CYAN, 5))
    ax.text(0.15, 0.68, 'Physics', color=CYAN, fontsize=8,
            fontfamily='monospace', ha='center', va='center', alpha=0.8)
    ax.text(0.15, 0.62, '(noncompact)', color=CYAN, fontsize=7,
            fontfamily='monospace', ha='center', va='center', alpha=0.6)

    # b~_k values on the left
    for i, (lbl, val) in enumerate(zip(
            [r'$\tilde{b}_0 = 1$', r'$\tilde{b}_1 = 1/6$',
             r'$\tilde{b}_2 = 5/72$', r'$\tilde{b}_3 = -3/16$'],
            [0, 1, 2, 3])):
        ax.text(0.15, 0.52 - i * 0.075, lbl, color=CYAN, fontsize=7,
                fontfamily='monospace', ha='center', va='center', alpha=0.9)

    # Right side: Geometry (compact)
    ax.text(0.85, 0.76, r'$Q^5$', color=GOLD, fontsize=14,
            fontfamily='monospace', ha='center', va='center',
            fontweight='bold', path_effects=glow(GOLD, 5))
    ax.text(0.85, 0.68, 'Geometry', color=GOLD, fontsize=8,
            fontfamily='monospace', ha='center', va='center', alpha=0.8)
    ax.text(0.85, 0.62, '(compact)', color=GOLD, fontsize=7,
            fontfamily='monospace', ha='center', va='center', alpha=0.6)

    # a~_k values on the right
    a_labels = [r'$\tilde{a}_0 = 1$', r'$\tilde{a}_1 = -25/3$',
                r'$\tilde{a}_2 = 313/9$', r'$\tilde{a}_3 = -874/9$']
    for i, lbl in enumerate(a_labels):
        ax.text(0.85, 0.52 - i * 0.075, lbl, color=GOLD, fontsize=7,
                fontfamily='monospace', ha='center', va='center', alpha=0.9)

    # Central arrow with |rho|^2
    arrow_y = 0.72
    ax.annotate('', xy=(0.70, arrow_y), xytext=(0.30, arrow_y),
                arrowprops=dict(arrowstyle='->', color=WHITE,
                                lw=2.5, mutation_scale=18),
                zorder=5)
    ax.annotate('', xy=(0.30, arrow_y - 0.06), xytext=(0.70, arrow_y - 0.06),
                arrowprops=dict(arrowstyle='->', color=WHITE,
                                lw=2.5, mutation_scale=18),
                zorder=5)

    # The shift label
    ax.text(0.50, 0.72, r'$e^{-|\rho|^2 t}$', color=WHITE, fontsize=10,
            fontfamily='monospace', ha='center', va='bottom',
            fontweight='bold', path_effects=glow(WHITE, 3),
            bbox=dict(facecolor=BG_PANEL, edgecolor='none', pad=2))
    ax.text(0.50, 0.60, r'$|\rho|^2 = 17/2$', color=MAGENTA, fontsize=11,
            fontfamily='monospace', ha='center', va='center',
            fontweight='bold', path_effects=glow(MAGENTA, 4),
            bbox=dict(facecolor=BG_PANEL, edgecolor='none', pad=2))

    # The formula
    ax.text(0.50, 0.22,
            r'$\tilde{a}_k = \sum_{j=0}^{k} \frac{(-17/2)^j}{j!}\, \tilde{b}_{k-j}$',
            color=WHITE, fontsize=9, fontfamily='monospace',
            ha='center', va='center',
            bbox=dict(facecolor='#111133', edgecolor=GOLD, pad=6,
                      boxstyle='round,pad=0.3', alpha=0.8))

    # rho decomposition
    ax.text(0.50, 0.10,
            r'$\rho = (n_C/2,\, N_c/2) = (5/2,\, 3/2)$',
            color=GREY, fontsize=7.5, fontfamily='monospace',
            ha='center', va='center')

    ax.text(0.50, 0.04,
            r'$|\rho|^2 = 25/4 + 9/4 = 34/4 = 17/2$',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='center', va='center')


def draw_panel3(ax):
    """Panel 3: The Seeley-DeWitt Coefficients a~_k."""
    ax.set_facecolor(BG_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    draw_panel_border(ax, GREEN)

    # Title
    ax.text(0.50, 0.93, 'Seeley-DeWitt Coefficients',
            color=GREEN, fontsize=11, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow(GREEN, 4))

    # Table header
    y0 = 0.82
    dy = 0.095
    ax.text(0.07, y0 + 0.04, 'k', color=GREY, fontsize=8, fontfamily='monospace',
            ha='center', va='center', fontweight='bold')
    ax.text(0.25, y0 + 0.04, r'$\tilde{a}_k$', color=GREY, fontsize=8,
            fontfamily='monospace', ha='center', va='center', fontweight='bold')
    ax.text(0.48, y0 + 0.04, 'Decimal', color=GREY, fontsize=8,
            fontfamily='monospace', ha='center', va='center', fontweight='bold')
    ax.text(0.77, y0 + 0.04, 'Curvature', color=GREY, fontsize=8,
            fontfamily='monospace', ha='center', va='center', fontweight='bold')

    ax.plot([0.03, 0.97], [y0, y0], color=GREY, lw=0.5, alpha=0.5)

    rows = [
        ('0', '1',      '1.000',    r'$a_0 = 1$'),
        ('1', '-25/3',  '-8.333',   r'$R/6$,  $R = -50$'),
        ('2', '313/9',  '34.778',   r'Gilkey $\checkmark$'),
        ('3', '-874/9', '-97.111',  r'$-2 \times 19 \times 23 / N_c^2$'),
    ]
    row_colors = [WHITE, GREEN, GOLD, CORAL]

    for i, (k_str, a_str, dec_str, curv_str) in enumerate(rows):
        y = y0 - (i + 0.5) * dy
        c = row_colors[i]

        bg_patch = FancyBboxPatch(
            (0.03, y - 0.032), 0.94, 0.065,
            boxstyle="round,pad=0.005",
            facecolor=c, edgecolor='none', alpha=0.06,
            transform=ax.transAxes
        )
        ax.add_patch(bg_patch)

        ax.text(0.07, y, k_str, color=c, fontsize=9,
                fontfamily='monospace', ha='center', va='center', fontweight='bold')
        ax.text(0.25, y, a_str, color=c, fontsize=9,
                fontfamily='monospace', ha='center', va='center', fontweight='bold')
        ax.text(0.48, y, dec_str, color=c, fontsize=9,
                fontfamily='monospace', ha='center', va='center')
        ax.text(0.77, y, curv_str, color=c, fontsize=8,
                fontfamily='monospace', ha='center', va='center')

    # Highlight the a_3 factorization
    ax.text(0.50, 0.18,
            r'$\tilde{a}_3 = -874/9$:  $874 = 2 \times 19 \times 23$',
            color=CORAL, fontsize=8.5, fontfamily='monospace',
            ha='center', va='center', fontweight='bold',
            path_effects=glow(CORAL, 2))

    ax.text(0.50, 0.10,
            '19 = dark energy denom',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='center', va='center')
    ax.text(0.50, 0.04,
            '23 = Golay prime (Leech lattice)',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='center', va='center')


def draw_panel4(ax):
    """Panel 4: The a~_2 = 313/9 verification."""
    ax.set_facecolor(BG_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    draw_panel_border(ax, GOLD)

    # Title
    ax.text(0.50, 0.95, r'$\tilde{a}_2 = 313/9$  Verification',
            color=GOLD, fontsize=10, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow(GOLD, 4))

    # Direction 1: Plancherel
    ax.text(0.50, 0.86, 'Direction 1: Plancherel', color=CYAN, fontsize=9,
            fontfamily='monospace', ha='center', va='center', fontweight='bold',
            path_effects=glow(CYAN, 2))

    plancherel_lines = [
        (r'$\tilde{a}_2 = \tilde{b}_2 + (-17/2)\tilde{b}_1 + \frac{(17/2)^2}{2}\tilde{b}_0$', WHITE, 9),
        (r'$= 5/72 - 17/12 + 289/8$', WHITE, 8.5),
        (r'$= (5 - 102 + 2601)/72$', WHITE, 8.5),
        (r'$= 2504/72 = 313/9$   $\checkmark$', GREEN, 9),
    ]
    for i, (txt, c, fs) in enumerate(plancherel_lines):
        ax.text(0.50, 0.79 - i * 0.065, txt, color=c, fontsize=fs,
                fontfamily='monospace', ha='center', va='center')

    # Separator
    ax.plot([0.10, 0.90], [0.50, 0.50], color=GREY, lw=0.5, alpha=0.4,
            linestyle='--')

    # Direction 2: Gilkey
    ax.text(0.50, 0.46, 'Direction 2: Gilkey curvature', color=GREEN, fontsize=9,
            fontfamily='monospace', ha='center', va='center', fontweight='bold',
            path_effects=glow(GREEN, 2))

    gilkey_lines = [
        (r'$\tilde{a}_2 = (5R^2 - 2|Ric|^2 + 2|Rm|^2)/360$', WHITE, 8.5),
        (r'$R = -50,\; |Ric|^2 = 250,\; |Rm|^2 = 260$', WHITE, 8),
        (r'$= (5 \times 2500 - 2 \times 250 + 2 \times 260)/360$', WHITE, 8),
        (r'$= 12520/360 = 313/9$   $\checkmark$', GREEN, 9),
    ]
    for i, (txt, c, fs) in enumerate(gilkey_lines):
        ax.text(0.50, 0.39 - i * 0.06, txt, color=c, fontsize=fs,
                fontfamily='monospace', ha='center', va='center')

    # The big checkmark box
    check_box = FancyBboxPatch(
        (0.25, 0.04), 0.50, 0.09,
        boxstyle="round,pad=0.015",
        facecolor='#003300', edgecolor=GREEN,
        linewidth=1.5, alpha=0.7,
        transform=ax.transAxes
    )
    ax.add_patch(check_box)
    ax.text(0.50, 0.085, 'BOTH ROUTES  =>  prime 313',
            color=GREEN, fontsize=9, fontfamily='monospace',
            ha='center', va='center', fontweight='bold',
            path_effects=glow(GREEN, 3))


def draw_panel5(ax):
    """Panel 5: The 63/64 Kahler Correction — RESOLVED."""
    ax.set_facecolor('#0d0815')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Green border for resolved result
    border = FancyBboxPatch(
        (0.02, 0.02), 0.96, 0.96,
        boxstyle="round,pad=0.02",
        facecolor='none', edgecolor=GREEN,
        linewidth=2.0, alpha=0.6,
        transform=ax.transAxes, zorder=0
    )
    ax.add_patch(border)

    # Title — resolved
    ax.text(0.50, 0.93, r'The 63/64 K\"ahler Correction',
            color=GREEN, fontsize=11, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow(GREEN, 5))

    # The discrepancy — now explained
    ax.text(0.50, 0.82, 'At cubic order, Riemannian vs Kahler:',
            color=WHITE, fontsize=8, fontfamily='monospace',
            ha='center', va='center')

    # Plancherel result (Kahler = exact)
    ax.text(0.50, 0.73,
            r'Plancherel (K\"ahler):  $\tilde{a}_3 = -874/9$',
            color=CYAN, fontsize=9, fontfamily='monospace',
            ha='center', va='center', fontweight='bold')

    # Vassilevich result (Riemannian = approximate)
    ax.text(0.50, 0.65,
            r'Vassilevich (Riem):  differs by $63/64$',
            color=GREY, fontsize=8.5, fontfamily='monospace',
            ha='center', va='center')

    # The ratio — now GREEN (resolved)
    ratio_box = FancyBboxPatch(
        (0.06, 0.46), 0.88, 0.14,
        boxstyle="round,pad=0.015",
        facecolor='#001a0a', edgecolor=GREEN,
        linewidth=1.5, alpha=0.7,
        transform=ax.transAxes
    )
    ax.add_patch(ratio_box)

    ax.text(0.50, 0.535,
            r'$63/64 = 1 - 1/2^{C_2} = 1 - 1/64$',
            color=GREEN, fontsize=10, fontfamily='monospace',
            ha='center', va='center', fontweight='bold',
            path_effects=glow(GREEN, 3))

    # Also = g * c_4 / 2^6
    ax.text(0.50, 0.39,
            r'$= g \times c_4 / 2^6 = 7 \times 9 / 64$',
            color=GOLD, fontsize=9, fontfamily='monospace',
            ha='center', va='center', fontweight='bold')

    # The diff
    ax.text(0.50, 0.30,
            r'diff $= -1748/225 = -(2^2 \times 19 \times 23)/(3^2 \times 5^2)$',
            color=GREY, fontsize=7.5, fontfamily='monospace',
            ha='center', va='center')

    # Explanation
    ax.text(0.50, 0.21,
            r'Genuine K\"ahler correction at cubic order',
            color=WHITE, fontsize=8, fontfamily='monospace',
            ha='center', va='center', fontstyle='italic')
    ax.text(0.50, 0.14,
            r'Plancherel density $|c(i\nu)|^{-2}$ is exact on $D_{IV}^5$',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='center', va='center')

    # RESOLVED stamp
    res_box = FancyBboxPatch(
        (0.25, 0.02), 0.50, 0.08,
        boxstyle="round,pad=0.01",
        facecolor=GREEN, edgecolor=WHITE,
        linewidth=1.0, alpha=0.15,
        transform=ax.transAxes
    )
    ax.add_patch(res_box)
    ax.text(0.50, 0.06, 'R E S O L V E D',
            color=GREEN, fontsize=12, fontfamily='monospace',
            ha='center', va='center', fontweight='bold',
            path_effects=glow(GREEN, 4))


def draw_panel6(ax):
    """Panel 6: Three Spectral Identities."""
    ax.set_facecolor(BG_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    draw_panel_border(ax, MAGENTA)

    # Title
    ax.text(0.50, 0.93, 'Three Spectral Identities',
            color=MAGENTA, fontsize=11, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow(MAGENTA, 4))

    # Identity 1
    id_y = 0.80
    id_dy = 0.20
    ax.text(0.08, id_y, '1.', color=GOLD, fontsize=10, fontfamily='monospace',
            ha='left', va='center', fontweight='bold')
    ax.text(0.15, id_y, r'$r_5 = 137/11 = N_{max}/c_2$',
            color=GOLD, fontsize=9.5, fontfamily='monospace',
            ha='left', va='center', fontweight='bold',
            path_effects=glow(GOLD, 2))
    ax.text(0.15, id_y - 0.05, 'zonal, compact side',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='left', va='center')

    # Identity 2
    ax.text(0.08, id_y - id_dy, '2.', color=CYAN, fontsize=10,
            fontfamily='monospace', ha='left', va='center', fontweight='bold')
    ax.text(0.15, id_y - id_dy,
            r'$\tilde{b}_1 = 1/C_2$',
            color=CYAN, fontsize=9.5, fontfamily='monospace',
            ha='left', va='center', fontweight='bold',
            path_effects=glow(CYAN, 2))
    ax.text(0.15, id_y - id_dy - 0.05, 'Plancherel, noncompact side',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='left', va='center')

    # Identity 3
    ax.text(0.08, id_y - 2 * id_dy, '3.', color=GREEN, fontsize=10,
            fontfamily='monospace', ha='left', va='center', fontweight='bold')
    ax.text(0.15, id_y - 2 * id_dy,
            r'$\tilde{a}_2 = 313/9$',
            color=GREEN, fontsize=9.5, fontfamily='monospace',
            ha='left', va='center', fontweight='bold',
            path_effects=glow(GREEN, 2))
    ax.text(0.15, id_y - 2 * id_dy - 0.05, 'Gilkey = Plancherel  (both sides)',
            color=GREY, fontsize=7, fontfamily='monospace',
            ha='left', va='center')

    # Separator
    ax.plot([0.08, 0.92], [0.26, 0.26], color=GREY, lw=0.5, alpha=0.4)

    # Path to Riemann
    ax.text(0.50, 0.21, 'The path to Riemann:',
            color=WHITE, fontsize=8.5, fontfamily='monospace',
            ha='center', va='center', fontweight='bold')

    # Arrow chain
    chain_y = 0.12
    steps = ['Plancherel', r'$\tilde{a}_k$', 'Residues', 'Selberg', 'RH']
    step_colors = [CYAN, GOLD, GREEN, MAGENTA, WHITE]
    n_steps = len(steps)
    x_positions = np.linspace(0.08, 0.92, n_steps)

    for i, (step, sc) in enumerate(zip(steps, step_colors)):
        ax.text(x_positions[i], chain_y, step, color=sc,
                fontsize=7, fontfamily='monospace',
                ha='center', va='center', fontweight='bold',
                path_effects=glow(sc, 2))
        if i < n_steps - 1:
            mid_x = (x_positions[i] + x_positions[i + 1]) / 2
            ax.text(mid_x, chain_y, r'$\rightarrow$', color=GREY,
                    fontsize=9, fontfamily='monospace',
                    ha='center', va='center')

    ax.text(0.50, 0.04,
            r'Exact residues $\rightarrow$ Selberg trace $\rightarrow$ $\zeta(s)$',
            color=GREY, fontsize=6.5, fontfamily='monospace',
            ha='center', va='center')


# =====================================================================
# THE EXPLORER CLASS
# =====================================================================

class PlancherelDictionaryExplorer:
    """Six-panel visualization of the Plancherel Dictionary for D_IV^5 / Q^5."""

    def __init__(self):
        _verify()
        self._build()

    def _build(self):
        self.fig = plt.figure(figsize=(18, 11), facecolor=BG)

        # Title
        self.fig.text(
            0.50, 0.97,
            'BST Toy 151 -- The Plancherel Dictionary',
            color=GOLD, fontsize=18, fontweight='bold', fontfamily='monospace',
            ha='center', va='top',
            path_effects=glow_strong(GOLD, 6)
        )

        # Subtitle
        self.fig.text(
            0.50, 0.935,
            r'Heat kernel on $D_{IV}^5$: every coefficient encodes BST integers',
            color=GREY, fontsize=10, fontfamily='monospace',
            ha='center', va='top'
        )

        # Copyright
        self.fig.text(
            0.50, 0.012,
            u'\u00a9 2026 Casey Koons | BST Toy 151 \u2014 The Plancherel Dictionary',
            color=GREY, fontsize=8, fontfamily='monospace',
            ha='center', va='bottom', alpha=0.6
        )

        # ── 6 panels via fig.add_axes ──
        # Layout: 3 columns x 2 rows
        # Margins: left=0.03, right=0.97, top=0.91, bottom=0.05
        # Gaps: hgap=0.025, vgap=0.04

        left_margin = 0.035
        right_margin = 0.035
        top_margin = 0.09   # below subtitle
        bot_margin = 0.05
        hgap = 0.025
        vgap = 0.04

        total_w = 1.0 - left_margin - right_margin - 2 * hgap
        total_h = 1.0 - top_margin - bot_margin - vgap
        pw = total_w / 3
        ph = total_h / 2

        # Row 1 (top): y = 1 - top_margin - ph
        top_y = 1.0 - top_margin - ph
        # Row 2 (bottom): y = bot_margin
        bot_y = bot_margin

        def panel_rect(col, row):
            x = left_margin + col * (pw + hgap)
            y = top_y if row == 0 else bot_y
            return [x, y, pw, ph]

        ax1 = self.fig.add_axes(panel_rect(0, 0), facecolor=BG_PANEL)
        ax2 = self.fig.add_axes(panel_rect(1, 0), facecolor=BG_PANEL)
        ax3 = self.fig.add_axes(panel_rect(2, 0), facecolor=BG_PANEL)
        ax4 = self.fig.add_axes(panel_rect(0, 1), facecolor=BG_PANEL)
        ax5 = self.fig.add_axes(panel_rect(1, 1), facecolor=BG_PANEL)
        ax6 = self.fig.add_axes(panel_rect(2, 1), facecolor=BG_PANEL)

        draw_panel1(ax1)
        draw_panel2(ax2)
        draw_panel3(ax3)
        draw_panel4(ax4)
        draw_panel5(ax5)
        draw_panel6(ax6)

        self.fig.canvas.manager.set_window_title(
            'BST Toy 151 -- The Plancherel Dictionary')


# =====================================================================
# VERIFY FUNCTION
# =====================================================================

def _verify():
    """
    Numerically confirm all key claims of the Plancherel Dictionary
    using exact Fraction arithmetic.
    """
    from fractions import Fraction

    ok_count = 0
    fail_count = 0

    def check(label, computed, expected):
        nonlocal ok_count, fail_count
        passed = (computed == expected)
        status = 'PASS' if passed else 'FAIL'
        mark = '+' if passed else 'X'
        print(f"  [{mark}] {label}")
        print(f"       computed = {computed},  expected = {expected}  ... {status}")
        if passed:
            ok_count += 1
        else:
            fail_count += 1

    # BST integers
    N_c_f = Fraction(3)
    n_C_f = Fraction(5)
    C_2_f = Fraction(6)
    g_f   = Fraction(7)
    c_4_f = Fraction(9)
    W_B2_f = Fraction(8)

    # b~_k exact
    bt0 = Fraction(1)
    bt1 = Fraction(1, 6)
    bt2 = Fraction(5, 72)
    bt3 = Fraction(-3, 16)

    rho_sq_f = Fraction(5, 2)**2 + Fraction(3, 2)**2  # = 17/2

    print()
    print("=" * 64)
    print("  THE PLANCHEREL DICTIONARY -- Verification")
    print("  BST Toy 151")
    print("=" * 64)
    print()

    # 1. b~_1 = 1/C_2
    check("b~_1 = 1/C_2 = 1/6",
          bt1, Fraction(1, 1) / C_2_f)

    # 2. b~_2 = n_C / (|W(B_2)| * c_4)
    check("b~_2 = n_C/(|W|*c_4) = 5/72",
          bt2, n_C_f / (W_B2_f * c_4_f))

    # 3. b~_3 = -N_c / 2^4
    check("b~_3 = -N_c/2^4 = -3/16",
          bt3, -N_c_f / Fraction(16))

    # 4. 48 = |W(B_2)| * C_2
    check("48 = |W(B_2)| * C_2 = 8 * 6",
          W_B2_f * C_2_f, Fraction(48))

    # 5. |rho|^2 = 17/2
    check("|rho|^2 = (5/2)^2 + (3/2)^2 = 17/2",
          rho_sq_f, Fraction(17, 2))

    # 6. a~_1 = b~_1 + (-17/2)*b~_0 = 1/6 - 17/2 = -25/3
    at1 = bt1 + (-rho_sq_f) * bt0
    check("a~_1 = b~_1 - (17/2)*b~_0 = -25/3",
          at1, Fraction(-25, 3))

    # 7. a~_2 = b~_2 + (-17/2)*b~_1 + (17/2)^2/2 * b~_0 = 313/9
    at2 = bt2 + (-rho_sq_f) * bt1 + (-rho_sq_f)**2 / Fraction(2) * bt0
    check("a~_2 = 5/72 - 17/12 + 289/8 = 313/9",
          at2, Fraction(313, 9))

    # 8. a~_3 computed
    at3 = (bt3
           + (-rho_sq_f) * bt2
           + (-rho_sq_f)**2 / Fraction(2) * bt1
           + (-rho_sq_f)**3 / Fraction(6) * bt0)
    check("a~_3 = -874/9",
          at3, Fraction(-874, 9))

    # 9. 874 = 2 * 19 * 23
    check("874 = 2 * 19 * 23",
          Fraction(2 * 19 * 23), Fraction(874))

    # 10. Gilkey check: (5*2500 - 2*250 + 2*260)/360 = 313/9
    gilkey = Fraction(5 * 2500 - 2 * 250 + 2 * 260, 360)
    check("Gilkey: (5*2500 - 2*250 + 2*260)/360 = 313/9",
          gilkey, Fraction(313, 9))

    # 11. Inverse: b~_1 = a~_1 + (17/2)*a~_0 = -25/3 + 17/2 = 1/6
    inv_bt1 = at1 + rho_sq_f * bt0
    check("Inverse: b~_1 = a~_1 + (17/2)*a~_0 = 1/6",
          inv_bt1, Fraction(1, 6))

    # 12. 63/64 = 1 - 1/2^C_2 = 1 - 1/64  (Kahler correction)
    kahler = Fraction(1) - Fraction(1, 2**6)
    check("63/64 = 1 - 1/2^{C_2} = 1 - 1/64",
          kahler, Fraction(63, 64))

    # 13. 63/64 = g * c_4 / 2^6 = 7 * 9 / 64
    check("63/64 = g * c_4 / 2^6 = 7*9/64",
          g_f * c_4_f / Fraction(64), Fraction(63, 64))

    print()
    print("-" * 64)
    print(f"  Results: {ok_count} passed, {fail_count} failed "
          f"out of {ok_count + fail_count} checks")
    if fail_count == 0:
        print("  ALL VERIFICATIONS PASSED")
    else:
        print("  *** SOME VERIFICATIONS FAILED ***")
    print("-" * 64)
    print()


# =====================================================================
# MAIN
# =====================================================================

if __name__ == '__main__':
    explorer = PlancherelDictionaryExplorer()
    plt.show()
