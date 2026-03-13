#!/usr/bin/env python3
"""
THE COSMIC PIE — Two Integers Set the Composition of the Universe
==================================================================

From N_c = 3 (color charges) and n_C = 5 (domain dimension), BST derives
the exact composition of the cosmos as integer fractions:

  Omega_Lambda = (N_c + 2*n_C) / (N_c^2 + 2*n_C) = 13/19 = 0.68421
  Omega_m      = C_2 / (N_c^2 + 2*n_C)           =  6/19 = 0.31579

The denominator 19 = dim(U(3)) + dim_R(D_IV^5) = 9 + 10.

Planck 2018: Omega_Lambda = 0.6847 +/- 0.0073, Omega_m = 0.3153 +/- 0.0073.
The match is 0.07 sigma. Two integers predict the composition of the universe.

System B (channel decomposition):
  N_max = 137 = 42 + 95 = C_2*g + n_C*19 = matter modes + vacuum modes
  Omega_m(B) = 42/137,  Omega_Lambda(B) = 95/137

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
from matplotlib.patches import FancyBboxPatch, Wedge, Circle, FancyArrowPatch
from matplotlib.gridspec import GridSpec

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # domain dimension (D_IV^5)
C_2 = 6           # Casimir eigenvalue
genus = 7         # genus of D_IV^5
N_max = 137       # channel capacity

# ─── Derived Cosmic Fractions (System A — over 19) ───
DENOM_A = N_c**2 + 2 * n_C                          # 19
OMEGA_LAMBDA_NUM = N_c + 2 * n_C                     # 13
OMEGA_M_NUM = C_2                                    # 6

OMEGA_LAMBDA = Fraction(OMEGA_LAMBDA_NUM, DENOM_A)   # 13/19
OMEGA_M = Fraction(OMEGA_M_NUM, DENOM_A)             # 6/19

# Sub-split of matter: DM/baryon ratio = (3*n_C + 1)/N_c = 16/3
DM_BARYON_RATIO = Fraction(3 * n_C + 1, N_c)         # 16/3
OMEGA_B = OMEGA_M * Fraction(N_c, N_c + 3 * n_C + 1) # 18/361
OMEGA_DM = OMEGA_M * Fraction(3 * n_C + 1, N_c + 3 * n_C + 1)  # 96/361

# ─── System B — Channel Decomposition over 137 ───
MATTER_MODES = C_2 * genus                            # 42
VACUUM_MODES = n_C * DENOM_A                          # 95
assert MATTER_MODES + VACUUM_MODES == N_max
OMEGA_M_B = Fraction(MATTER_MODES, N_max)             # 42/137
OMEGA_LAMBDA_B = Fraction(VACUUM_MODES, N_max)        # 95/137

# ─── Planck 2018 Observations ───
PLANCK = {
    'Omega_Lambda': (0.6847, 0.0073),
    'Omega_m':      (0.3153, 0.0073),
    'Omega_b':      (0.0493, 0.0010),
    'Omega_DM':     (0.2645, 0.0057),
}

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
DM_GREY     = '#778899'
CYAN        = '#00ddff'


# ═══════════════════════════════════════════════════════════════════
# CI (Companion Intelligence) Interface
# ═══════════════════════════════════════════════════════════════════

class CosmicPie:
    """
    BST Cosmic Composition from two integers: N_c=3, n_C=5.

    Usage:
        from toy_cosmic_pie import CosmicPie
        cp = CosmicPie()
        cp.Omega_Lambda       # Fraction(13, 19)
        cp.planck_comparison()
        cp.system_A()
        cp.system_B()
        cp.why_19()
        cp.cross_sector()
    """

    def __init__(self):
        self.N_c = N_c
        self.n_C = n_C
        self.C_2 = C_2
        self.genus = genus
        self.N_max = N_max

        # System A fractions
        self.Omega_Lambda = OMEGA_LAMBDA
        self.Omega_matter = OMEGA_M
        self.Omega_DM = OMEGA_DM
        self.Omega_baryon = OMEGA_B
        self.denominator = DENOM_A

        # System B fractions
        self.Omega_Lambda_B = OMEGA_LAMBDA_B
        self.Omega_matter_B = OMEGA_M_B

    def sigma_deviation(self, bst_frac, planck_key):
        """Compute sigma deviation from Planck 2018."""
        val, err = PLANCK[planck_key]
        return abs(float(bst_frac) - val) / err

    def planck_comparison(self):
        """Print table comparing BST predictions to Planck 2018."""
        sep = "=" * 72
        print(f"\n{sep}")
        print("  COSMIC COMPOSITION: BST vs Planck 2018")
        print(f"{sep}\n")
        rows = [
            ("Omega_Lambda", self.Omega_Lambda, "Omega_Lambda"),
            ("Omega_m     ", self.Omega_matter, "Omega_m"),
            ("Omega_b     ", self.Omega_baryon, "Omega_b"),
            ("Omega_DM    ", self.Omega_DM, "Omega_DM"),
        ]
        print(f"  {'Quantity':<14} {'BST Fraction':>14} {'BST Value':>12} "
              f"{'Planck':>10} {'sigma':>8}")
        print(f"  {'-'*14} {'-'*14} {'-'*12} {'-'*10} {'-'*8}")
        for label, frac, pkey in rows:
            val = float(frac)
            pval, perr = PLANCK[pkey]
            sig = abs(val - pval) / perr
            print(f"  {label:<14} {str(frac):>14} {val:>12.5f} "
                  f"{pval:>10.4f} {sig:>7.2f} sigma")
        print()
        # Ratios
        lam_m = float(self.Omega_Lambda / self.Omega_matter)
        dm_b = float(self.Omega_DM / self.Omega_baryon)
        print(f"  Omega_Lambda/Omega_m = {self.Omega_Lambda/self.Omega_matter}"
              f" = {lam_m:.4f}  (obs: {0.6847/0.3153:.4f})")
        print(f"  Omega_DM/Omega_b    = {self.Omega_DM/self.Omega_baryon}"
              f" = {dm_b:.4f}  (obs: {0.2645/0.0493:.4f})")
        print(f"\n{sep}\n")

    def system_A(self):
        """Display System A: integer fractions over 19."""
        sep = "-" * 56
        print(f"\n  SYSTEM A: Fractions over 19")
        print(f"  {sep}")
        print(f"  19 = N_c^2 + 2*n_C = {N_c}^2 + 2*{n_C} = {DENOM_A}")
        print(f"     = dim(U(3)) + dim_R(D_IV^5) = 9 + 10")
        print(f"  Omega_Lambda = (N_c + 2*n_C)/19 = {OMEGA_LAMBDA_NUM}/19"
              f" = {float(OMEGA_LAMBDA):.5f}")
        print(f"  Omega_m      = C_2/19           = {OMEGA_M_NUM}/19"
              f" = {float(OMEGA_M):.5f}")
        print(f"  Omega_b      = {OMEGA_B} = {float(OMEGA_B):.5f}")
        print(f"  Omega_DM     = {OMEGA_DM} = {float(OMEGA_DM):.5f}")
        print(f"  DM/baryon    = (3*n_C+1)/N_c = 16/3 = {float(DM_BARYON_RATIO):.4f}")
        print()

    def system_B(self):
        """Display System B: channel mode decomposition over 137."""
        sep = "-" * 56
        print(f"\n  SYSTEM B: Channel Mode Decomposition over 137")
        print(f"  {sep}")
        print(f"  N_max = {N_max} = {MATTER_MODES} + {VACUUM_MODES}")
        print(f"  {MATTER_MODES} = C_2 * genus = {C_2} * {genus} = matter modes")
        print(f"  {VACUUM_MODES} = n_C * 19    = {n_C} * {DENOM_A} = vacuum modes")
        print(f"  Omega_m(B)      = {OMEGA_M_B} = {float(OMEGA_M_B):.5f}")
        print(f"  Omega_Lambda(B) = {OMEGA_LAMBDA_B} = {float(OMEGA_LAMBDA_B):.5f}")
        print()

    def why_19(self):
        """Explain the denominator 19."""
        sep = "-" * 56
        print(f"\n  WHY 19?")
        print(f"  {sep}")
        print(f"  19 = N_c^2 + 2*n_C = 9 + 10")
        print(f"   9 = dim(U(3) algebra) = color information capacity")
        print(f"  10 = dim_R(D_IV^5) = real dimension of the Cartan domain")
        print(f"")
        print(f"  19 is prime, so the fractions 13/19 and 6/19 are irreducible.")
        print(f"  The universe's composition is a ratio of two structural")
        print(f"  dimensions, not a tunable parameter.")
        print()

    def cross_sector(self):
        """Show cross-connections between cosmic and particle sectors."""
        sep = "-" * 56
        print(f"\n  CROSS-SECTOR CONNECTIONS")
        print(f"  {sep}")
        print(f"  The number 13 appears in:")
        print(f"    Omega_Lambda = 13/19  (dark energy fraction)")
        print(f"    sin^2(theta_W) = 3/13  (Weinberg angle)")
        print(f"    (m_n - m_p)/m_e ~ 91/36 = 7*13/6^2")
        print()
        print(f"  The number 6 appears in:")
        print(f"    Omega_m = 6/19  (matter fraction)")
        print(f"    m_p/m_e = 6*pi^5  (proton-electron mass ratio)")
        print(f"    C_2 = 6  (Casimir eigenvalue of pi_6)")
        print()
        print(f"  The number 7 appears in:")
        print(f"    genus(D_IV^5) = 7")
        print(f"    alpha_s(m_p) = 7/20  (strong coupling)")
        print(f"    v = m_p^2 / (7*m_e)  (Fermi scale)")
        print(f"    42 = 6*7 = C_2*genus = matter modes in N_max")
        print()
        print(f"  Same integers. Same domain. Every sector.")
        print()

    def __repr__(self):
        return (
            f"CosmicPie(\n"
            f"  Omega_Lambda = {self.Omega_Lambda} = {float(self.Omega_Lambda):.5f}"
            f"  (Planck: {PLANCK['Omega_Lambda'][0]})\n"
            f"  Omega_m      = {self.Omega_matter} = {float(self.Omega_matter):.5f}"
            f"  (Planck: {PLANCK['Omega_m'][0]})\n"
            f"  Omega_b      = {self.Omega_baryon} = {float(self.Omega_baryon):.5f}"
            f"  (Planck: {PLANCK['Omega_b'][0]})\n"
            f"  Omega_DM     = {self.Omega_DM} = {float(self.Omega_DM):.5f}"
            f"  (Planck: {PLANCK['Omega_DM'][0]})\n"
            f"  denominator  = {self.denominator} = dim(U(3)) + dim_R(D_IV^5)\n"
            f")"
        )


# ═══════════════════════════════════════════════════════════════════
# Visualization Helpers
# ═══════════════════════════════════════════════════════════════════

def glow_text(ax, x, y, text, color=WHITE, fontsize=12, ha='center', va='center',
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


def draw_ring_segment(ax, center, r_inner, r_outer, theta1, theta2,
                      color, alpha=0.85, edgecolor=None):
    """Draw an annular wedge (ring segment) on the given axes."""
    ec = edgecolor or BG
    w1 = Wedge(center, r_outer, theta1, theta2,
               width=r_outer - r_inner, facecolor=color,
               edgecolor=ec, linewidth=1.5, alpha=alpha)
    ax.add_patch(w1)
    return w1


# ═══════════════════════════════════════════════════════════════════
# Main Visualization
# ═══════════════════════════════════════════════════════════════════

def build_figure():
    """Build the full Cosmic Pie visualization."""

    fig = plt.figure(figsize=(20, 12), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST — The Cosmic Pie: Two Integers Set the Composition of the Universe')

    # ── Title ──
    fig.text(0.50, 0.975,
             'THE COSMIC PIE',
             ha='center', va='top', color=GOLD, fontsize=26, weight='bold',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=4, foreground=GOLD_DIM, alpha=0.4)])
    fig.text(0.50, 0.945,
             'Two Integers Set the Composition of the Universe',
             ha='center', va='top', color=LIGHT_GREY, fontsize=14,
             fontfamily='monospace')

    # ── Layout: left (40%), center (30%), right (30%) ──
    gs = GridSpec(2, 3, figure=fig,
                  width_ratios=[0.40, 0.30, 0.30],
                  height_ratios=[0.88, 0.12],
                  hspace=0.08, wspace=0.06,
                  left=0.03, right=0.97, top=0.92, bottom=0.02)

    # ════════════════════════════════════════════════════════════════
    # LEFT PANEL: Concentric Pie Charts (BST outer, Planck inner)
    # ════════════════════════════════════════════════════════════════

    ax_pie = fig.add_subplot(gs[0, 0])
    ax_pie.set_facecolor(BG)
    ax_pie.set_xlim(-1.55, 1.55)
    ax_pie.set_ylim(-1.55, 1.55)
    ax_pie.set_aspect('equal')
    ax_pie.axis('off')

    # Radii for the two rings
    R_OUT_OUTER = 1.40
    R_OUT_INNER = 0.95
    R_IN_OUTER = 0.88
    R_IN_INNER = 0.50

    # Convert fractions to degrees (start at 90 degrees = top)
    f_lam = float(OMEGA_LAMBDA)
    f_m = float(OMEGA_M)
    f_dm = float(OMEGA_DM)
    f_b = float(OMEGA_B)

    # BST outer ring: Lambda and matter
    start = 90
    theta_lam = f_lam * 360
    theta_m = f_m * 360

    # Dark energy wedge (deep blue-purple)
    draw_ring_segment(ax_pie, (0, 0), R_OUT_INNER, R_OUT_OUTER,
                      start, start + theta_lam, VOID_PURPLE, alpha=0.9)
    # Matter wedge — split into DM and baryon
    theta_dm = f_dm * 360
    theta_b = f_b * 360
    draw_ring_segment(ax_pie, (0, 0), R_OUT_INNER, R_OUT_OUTER,
                      start + theta_lam, start + theta_lam + theta_dm,
                      DM_GREY, alpha=0.85)
    draw_ring_segment(ax_pie, (0, 0), R_OUT_INNER, R_OUT_OUTER,
                      start + theta_lam + theta_dm, start + 360,
                      BRIGHT_GOLD, alpha=0.95)

    # BST outer ring labels
    # Dark energy label
    mid_lam = np.radians(start + theta_lam / 2)
    r_label_out = (R_OUT_INNER + R_OUT_OUTER) / 2
    lx, ly = r_label_out * np.cos(mid_lam), r_label_out * np.sin(mid_lam)
    glow_text(ax_pie, lx, ly, '13/19', color=PURPLE_LINE, fontsize=11,
              weight='bold', glow_width=2)
    glow_text(ax_pie, lx, ly - 0.13, '68.42%', color=PURPLE_LINE, fontsize=8,
              glow_width=1)

    # DM label
    mid_dm = np.radians(start + theta_lam + theta_dm / 2)
    dx, dy = r_label_out * np.cos(mid_dm), r_label_out * np.sin(mid_dm)
    glow_text(ax_pie, dx, dy, '96/361', color=WHITE, fontsize=9,
              weight='bold', glow_width=1)
    glow_text(ax_pie, dx, dy - 0.11, '26.59%', color=LIGHT_GREY, fontsize=7,
              glow_width=1)

    # Baryon label (small slice — place outside)
    mid_b = np.radians(start + theta_lam + theta_dm + theta_b / 2)
    bx_in = R_OUT_OUTER * np.cos(mid_b)
    by_in = R_OUT_OUTER * np.sin(mid_b)
    bx_out = 1.52 * np.cos(mid_b)
    by_out = 1.52 * np.sin(mid_b)
    ax_pie.annotate('18/361\n4.99%', xy=(bx_in, by_in), xytext=(bx_out, by_out),
                    fontsize=8, color=GOLD, weight='bold', ha='center', va='center',
                    arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.2),
                    path_effects=[pe.withStroke(linewidth=2, foreground=BG, alpha=0.8)])

    # Outer ring title
    glow_text(ax_pie, 0, 1.52, 'BST Prediction', color=GOLD, fontsize=11,
              weight='bold', glow_width=2, glow_color=GOLD_DIM)

    # Planck inner ring
    p_lam, _ = PLANCK['Omega_Lambda']
    p_m, _ = PLANCK['Omega_m']
    p_dm, _ = PLANCK['Omega_DM']
    p_b, _ = PLANCK['Omega_b']

    pt_lam = p_lam * 360
    pt_dm = p_dm * 360
    pt_b = p_b * 360

    draw_ring_segment(ax_pie, (0, 0), R_IN_INNER, R_IN_OUTER,
                      start, start + pt_lam, '#221166', alpha=0.75)
    draw_ring_segment(ax_pie, (0, 0), R_IN_INNER, R_IN_OUTER,
                      start + pt_lam, start + pt_lam + pt_dm,
                      '#556677', alpha=0.70)
    draw_ring_segment(ax_pie, (0, 0), R_IN_INNER, R_IN_OUTER,
                      start + pt_lam + pt_dm, start + 360,
                      '#ccaa33', alpha=0.80)

    # Inner ring labels
    mid_lam_p = np.radians(start + pt_lam / 2)
    r_label_in = (R_IN_INNER + R_IN_OUTER) / 2
    plx, ply = r_label_in * np.cos(mid_lam_p), r_label_in * np.sin(mid_lam_p)
    glow_text(ax_pie, plx, ply, '68.47%', color='#9977cc', fontsize=9,
              glow_width=1)

    mid_dm_p = np.radians(start + pt_lam + pt_dm / 2)
    pdx, pdy = r_label_in * np.cos(mid_dm_p), r_label_in * np.sin(mid_dm_p)
    glow_text(ax_pie, pdx, pdy, '26.45%', color=LIGHT_GREY, fontsize=8,
              glow_width=1)

    # Inner ring title
    glow_text(ax_pie, 0, -0.37, 'Planck 2018', color=GREY, fontsize=9,
              weight='bold')

    # Center: "19 = 9 + 10" glowing
    center_circle = Circle((0, 0), R_IN_INNER - 0.02, facecolor=BG,
                           edgecolor=GOLD_DIM, linewidth=1.5, alpha=0.9)
    ax_pie.add_patch(center_circle)
    glow_text(ax_pie, 0, 0.12, '19', color=GOLD, fontsize=28,
              weight='bold', glow_width=5, glow_color=GOLD_DIM)
    glow_text(ax_pie, 0, -0.08, '= 9 + 10', color=LIGHT_GREY, fontsize=12)
    glow_text(ax_pie, 0, -0.25, r'$N_c^2 + 2n_C$', color=GREY, fontsize=10)

    # Legend below pie
    legend_items = [
        (VOID_PURPLE, r'$\Omega_\Lambda$ = 13/19  (dark energy)'),
        (DM_GREY, r'$\Omega_{DM}$ = 96/361 (dark matter)'),
        (BRIGHT_GOLD, r'$\Omega_b$ = 18/361  (baryonic)'),
    ]
    for i, (c, txt) in enumerate(legend_items):
        y_leg = -1.50 + i * (-0.14)
        rect = FancyBboxPatch((-1.0, y_leg - 0.04), 0.12, 0.08,
                               boxstyle="round,pad=0.01",
                               facecolor=c, edgecolor=GREY, alpha=0.85)
        ax_pie.add_patch(rect)
        # Adjust y_leg for text after extending ylim
        ax_pie.text(-0.82, y_leg, txt, color=LIGHT_GREY, fontsize=9,
                    va='center', ha='left')

    ax_pie.set_ylim(-1.95, 1.60)

    # ════════════════════════════════════════════════════════════════
    # CENTER PANEL: The Denominator 19 + Channel Decomposition
    # ════════════════════════════════════════════════════════════════

    ax_center = fig.add_subplot(gs[0, 1])
    ax_center.set_facecolor(BG)
    ax_center.set_xlim(0, 1)
    ax_center.set_ylim(0, 1)
    ax_center.axis('off')

    # Title
    glow_text(ax_center, 0.5, 0.97, 'The Denominator 19', color=CYAN,
              fontsize=14, weight='bold', glow_width=3, glow_color=BLUE_GLOW)

    # Explanation block
    y = 0.90
    lines_19 = [
        (r'$19 = N_c^2 + 2n_C = 9 + 10$', GOLD, 12),
        ('', WHITE, 10),
        (r'$9 = \dim\,U(3)$', BLUE_GLOW, 11),
        ('color information capacity', GREY, 9),
        ('', WHITE, 10),
        (r'$10 = \dim_{\mathbb{R}}\,D_{IV}^5$', PURPLE_LINE, 11),
        ('domain representation dimension', GREY, 9),
        ('', WHITE, 10),
        ('19 is prime: fractions are irreducible', LIGHT_GREY, 9),
    ]
    for text, col, fs in lines_19:
        if text == '':
            y -= 0.015
            continue
        glow_text(ax_center, 0.5, y, text, color=col, fontsize=fs,
                  glow_width=1)
        y -= 0.04

    # Separator
    y -= 0.02
    ax_center.plot([0.05, 0.95], [y, y], color=GREY, alpha=0.3, linewidth=0.5)
    y -= 0.03

    # Channel decomposition header
    glow_text(ax_center, 0.5, y, 'Channel Decomposition', color=CYAN,
              fontsize=12, weight='bold', glow_width=2)
    y -= 0.04
    glow_text(ax_center, 0.5, y, r'$N_{max} = 137 = 42 + 95$', color=GOLD,
              fontsize=12, glow_width=2, weight='bold')
    y -= 0.035
    glow_text(ax_center, 0.5, y,
              r'$42 = C_2 \times g = 6 \times 7$  (matter modes)',
              color=BRIGHT_GOLD, fontsize=9, glow_width=1)
    y -= 0.03
    glow_text(ax_center, 0.5, y,
              r'$95 = n_C \times 19 = 5 \times 19$  (vacuum modes)',
              color=PURPLE_LINE, fontsize=9, glow_width=1)

    # ── Visual: 137 small cells ──
    y -= 0.05
    cell_top = y
    cols_per_row = 19   # Chosen because 19 divides meaning
    n_rows = 8          # 8 rows: 7 full (133) + 1 partial (4)
    cell_w = 0.9 / cols_per_row
    cell_h = cell_w * 0.85
    x_start = 0.05

    for idx in range(N_max):
        row = idx // cols_per_row
        col = idx % cols_per_row
        cx = x_start + col * cell_w
        cy = cell_top - row * cell_h

        if idx < MATTER_MODES:
            # Matter mode — gold
            fc = GOLD_DIM
            alpha = 0.85
        else:
            # Vacuum mode — purple
            fc = '#3311aa'
            alpha = 0.70

        rect = FancyBboxPatch((cx, cy - cell_h * 0.8), cell_w * 0.88,
                               cell_h * 0.75,
                               boxstyle="round,pad=0.002",
                               facecolor=fc, edgecolor=BG,
                               alpha=alpha, linewidth=0.3)
        ax_center.add_patch(rect)

    # Boundary marker line between 42 and 43
    boundary_row = MATTER_MODES // cols_per_row
    boundary_col = MATTER_MODES % cols_per_row
    bx = x_start + boundary_col * cell_w - cell_w * 0.06
    by_top = cell_top - boundary_row * cell_h + cell_h * 0.1
    by_bot = cell_top - boundary_row * cell_h - cell_h * 0.9
    ax_center.plot([bx, bx], [by_bot, by_top], color=RED_WARM, linewidth=1.5,
                   alpha=0.6)

    # Labels beneath grid
    grid_bottom = cell_top - n_rows * cell_h
    glow_text(ax_center, 0.25, grid_bottom - 0.02,
              '42 gold = matter', color=GOLD, fontsize=8, glow_width=1)
    glow_text(ax_center, 0.72, grid_bottom - 0.02,
              '95 purple = vacuum', color=PURPLE_LINE, fontsize=8, glow_width=1)

    # ════════════════════════════════════════════════════════════════
    # RIGHT PANEL: Comparison Table + Cross-Connections
    # ════════════════════════════════════════════════════════════════

    ax_right = fig.add_subplot(gs[0, 2])
    ax_right.set_facecolor(BG)
    ax_right.set_xlim(0, 1)
    ax_right.set_ylim(0, 1)
    ax_right.axis('off')

    # Title
    glow_text(ax_right, 0.5, 0.97, 'BST vs Planck 2018', color=GREEN_GLOW,
              fontsize=14, weight='bold', glow_width=3)

    # Table header
    y = 0.90
    header_cols = [0.02, 0.30, 0.53, 0.74, 0.90]
    headers = ['Quantity', 'BST', 'Planck', 'Frac.', 'dev.']
    for x_h, h in zip(header_cols, headers):
        glow_text(ax_right, x_h, y, h, color=GREY, fontsize=8,
                  ha='left', weight='bold', glow_width=1)
    y -= 0.015
    ax_right.plot([0.02, 0.98], [y, y], color=GREY, alpha=0.4, linewidth=0.5)
    y -= 0.025

    # Table rows
    table_data = [
        (r'$\Omega_\Lambda$', OMEGA_LAMBDA, 'Omega_Lambda', '13/19'),
        (r'$\Omega_m$', OMEGA_M, 'Omega_m', '6/19'),
        (r'$\Omega_b$', OMEGA_B, 'Omega_b', '18/361'),
        (r'$\Omega_{DM}$', OMEGA_DM, 'Omega_DM', '96/361'),
    ]

    for label, frac, pkey, frac_str in table_data:
        bst_val = float(frac)
        p_val, p_err = PLANCK[pkey]
        sig = abs(bst_val - p_val) / p_err
        sig_color = GREEN_GLOW if sig < 1.0 else GOLD if sig < 2.0 else RED_WARM
        glow_text(ax_right, header_cols[0], y, label, color=WHITE,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[1], y, f'{bst_val:.5f}', color=GOLD,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[2], y, f'{p_val:.4f}', color=LIGHT_GREY,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[3], y, frac_str, color=CYAN,
                  fontsize=9, ha='left', glow_width=1)
        sig_str = f'{sig:.2f}' + r'$\sigma$'
        glow_text(ax_right, header_cols[4], y, sig_str, color=sig_color,
                  fontsize=9, ha='left', weight='bold', glow_width=1)
        y -= 0.04

    # Ratio rows
    y -= 0.01
    ax_right.plot([0.02, 0.98], [y, y], color=GREY, alpha=0.3, linewidth=0.5)
    y -= 0.03

    ratios = [
        (r'$\Omega_\Lambda / \Omega_m$', '13/6', float(OMEGA_LAMBDA / OMEGA_M),
         0.6847 / 0.3153, '0.24%'),
        (r'$\Omega_{DM} / \Omega_b$', '16/3', float(DM_BARYON_RATIO),
         0.2645 / 0.0493, '0.58%'),
    ]
    for label, frac_s, bst_v, obs_v, dev in ratios:
        glow_text(ax_right, header_cols[0], y, label, color=WHITE,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[1], y, f'{bst_v:.4f}', color=GOLD,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[2], y, f'{obs_v:.4f}', color=LIGHT_GREY,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[3], y, frac_s, color=CYAN,
                  fontsize=9, ha='left', glow_width=1)
        glow_text(ax_right, header_cols[4], y, dev, color=GREEN_GLOW,
                  fontsize=9, ha='left', weight='bold', glow_width=1)
        y -= 0.04

    # ── Cross-Connections ──
    y -= 0.03
    ax_right.plot([0.02, 0.98], [y, y], color=GREY, alpha=0.3, linewidth=0.5)
    y -= 0.03

    glow_text(ax_right, 0.5, y, 'The Cross-Connections', color=CYAN,
              fontsize=12, weight='bold', glow_width=2)
    y -= 0.04

    # Connection web: 13, 6, 7
    connections = [
        ('13', PURPLE_LINE, [
            r'$\Omega_\Lambda = 13/19$',
            r'$\sin^2\theta_W = 3/13$',
            r'$\Delta m/m_e = 7 \times 13 / 36$',
        ]),
        ('6', GOLD, [
            r'$\Omega_m = 6/19$',
            r'$m_p/m_e = 6\pi^5$',
            r'$C_2(\pi_6) = 6$',
        ]),
        ('7', GREEN_GLOW, [
            r'genus$(D_{IV}^5) = 7$',
            r'$\alpha_s(m_p) = 7/20$',
            r'$v = m_p^2/(7 m_e)$',
        ]),
    ]

    for num_str, col, items in connections:
        glow_text(ax_right, 0.08, y, num_str, color=col, fontsize=16,
                  weight='bold', ha='center', glow_width=3, glow_color=col)
        for j, item in enumerate(items):
            glow_text(ax_right, 0.55, y - j * 0.028, item, color=LIGHT_GREY,
                      fontsize=8, ha='center', glow_width=1)
        # Draw connecting lines from number to items
        for j in range(len(items)):
            iy = y - j * 0.028
            ax_right.plot([0.16, 0.30], [y, iy], color=col, alpha=0.2,
                          linewidth=0.8)
        y -= len(items) * 0.028 + 0.03

    # ── Web connections between numbers ──
    # Small visual: draw arcs between 13, 6, 7
    web_y_top = y + 0.35
    web_positions = {
        '13': (0.08, web_y_top),
        '6':  (0.08, web_y_top - 0.11),
        '7':  (0.08, web_y_top - 0.22),
    }
    # Lines from 6*7=42, 13+6=19
    ax_right.annotate('', xy=(0.03, web_y_top - 0.11),
                      xytext=(0.03, web_y_top - 0.22),
                      arrowprops=dict(arrowstyle='<->', color=GOLD_DIM,
                                      lw=1, alpha=0.4,
                                      connectionstyle='arc3,rad=0.3'))
    glow_text(ax_right, 0.01, web_y_top - 0.165, '42', color=GOLD_DIM,
              fontsize=7, glow_width=1)

    ax_right.annotate('', xy=(0.03, web_y_top),
                      xytext=(0.03, web_y_top - 0.11),
                      arrowprops=dict(arrowstyle='<->', color=GREY,
                                      lw=1, alpha=0.4,
                                      connectionstyle='arc3,rad=0.3'))
    glow_text(ax_right, 0.01, web_y_top - 0.055, '19', color=GREY,
              fontsize=7, glow_width=1)

    # ════════════════════════════════════════════════════════════════
    # BOTTOM STRIP
    # ════════════════════════════════════════════════════════════════

    ax_bot = fig.add_subplot(gs[1, :])
    ax_bot.set_facecolor(BG)
    ax_bot.set_xlim(0, 1)
    ax_bot.set_ylim(0, 1)
    ax_bot.axis('off')

    # The chain
    chain_text = (
        r'$N_c = 3, \;\; n_C = 5$'
        r'$\quad\longrightarrow\quad$'
        r'$\Omega_\Lambda = \frac{13}{19},\;\;'
        r'\Omega_m = \frac{6}{19}$'
        r'$\quad\longrightarrow\quad$'
        r'matches Planck to $0.07\sigma$'
    )
    ax_bot.text(0.50, 0.70, chain_text, ha='center', va='center',
                color=GOLD, fontsize=14,
                path_effects=[pe.withStroke(linewidth=3, foreground=GOLD_DIM,
                                            alpha=0.3)])

    ax_bot.text(0.50, 0.18,
                'Two integers. One domain. The composition of the cosmos.',
                ha='center', va='center', color=GREY, fontsize=12,
                style='italic',
                path_effects=[pe.withStroke(linewidth=2, foreground=DARK_PANEL,
                                            alpha=0.5)])

    return fig


# ═══════════════════════════════════════════════════════════════════
# Print Report
# ═══════════════════════════════════════════════════════════════════

def print_report():
    """Print a concise summary of the cosmic composition derivation."""
    cp = CosmicPie()
    sep = "=" * 72
    print(f"\n{sep}")
    print("  THE COSMIC PIE — Two Integers Set the Composition of the Universe")
    print(f"{sep}\n")
    print(f"  Input:  N_c = {N_c} (color charges),  n_C = {n_C} (domain dimension)")
    print(f"  Derived: C_2 = {C_2},  genus = {genus},  N_max = {N_max}")
    print(f"  Denominator: 19 = N_c^2 + 2*n_C = dim(U(3)) + dim_R(D_IV^5)")
    print()

    print("  SYSTEM A — Integer Fractions over 19:")
    print(f"    Omega_Lambda = (N_c + 2*n_C)/19 = 13/19 = {float(OMEGA_LAMBDA):.5f}")
    print(f"    Omega_m      = C_2/19            =  6/19 = {float(OMEGA_M):.5f}")
    print(f"    Omega_DM     = 96/361            = {float(OMEGA_DM):.5f}")
    print(f"    Omega_b      = 18/361            = {float(OMEGA_B):.5f}")
    print()

    print("  SYSTEM B — Channel Mode Decomposition over 137:")
    print(f"    137 = 42 + 95 = (C_2 * genus) + (n_C * 19)")
    print(f"    Omega_m(B)      = 42/137 = {float(OMEGA_M_B):.5f}")
    print(f"    Omega_Lambda(B) = 95/137 = {float(OMEGA_LAMBDA_B):.5f}")
    print()

    print("  COMPARISON TO PLANCK 2018:")
    print(f"  {'Quantity':<16} {'BST':>10} {'Planck':>10} {'sigma':>8}")
    print(f"  {'-'*16} {'-'*10} {'-'*10} {'-'*8}")
    for label, frac, pkey in [
        ("Omega_Lambda", OMEGA_LAMBDA, "Omega_Lambda"),
        ("Omega_m", OMEGA_M, "Omega_m"),
        ("Omega_b", OMEGA_B, "Omega_b"),
        ("Omega_DM", OMEGA_DM, "Omega_DM"),
    ]:
        v = float(frac)
        pv, pe_val = PLANCK[pkey]
        sig = abs(v - pv) / pe_val
        print(f"  {label:<16} {v:>10.5f} {pv:>10.4f} {sig:>7.2f}s")
    print()
    print(f"  Lambda/matter = 13/6 = {float(OMEGA_LAMBDA/OMEGA_M):.4f}"
          f"  (obs: {0.6847/0.3153:.4f}, dev 0.24%)")
    print(f"  DM/baryon     = 16/3 = {float(DM_BARYON_RATIO):.4f}"
          f"  (obs: {0.2645/0.0493:.4f}, dev 0.58%)")
    print()
    print(f"  Cross-sector: 13 -> Omega_Lambda, sin^2(theta_W) = 3/13")
    print(f"                 6 -> Omega_m, m_p/m_e = 6*pi^5, C_2 = 6")
    print(f"                 7 -> genus, alpha_s = 7/20, 42 = 6*7 matter modes")
    print(f"\n{sep}\n")


# ═══════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print_report()
    fig = build_figure()
    plt.show()
