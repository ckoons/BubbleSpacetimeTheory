#!/usr/bin/env python3
"""
WHY 56 — The Cosmological Constant Exponent
============================================
The cosmological constant is 122 orders of magnitude below the Planck scale:
    Lambda = F_BST * alpha^56 * e^(-2) ~ 2.9 x 10^(-122)

The exponent 56 controls this entire hierarchy.  Why exactly 56?

Two independent derivations converge on the same answer:

  Route A (neutrino-vacuum):
    m_nu ~ alpha^(2g) * m_Pl   where g=7 (genus of D_IV^5)
    Lambda ~ (m_nu/m_Pl)^4 = alpha^(8g) = alpha^56
    => 56 = 8 * 7

  Route B (partition function):
    Z_0 ~ product(j=0..g, 1-q_j), total alpha power = sum(j=0..g, j) = g(g+1)/2 = 28
    Lambda ~ |Z_0|^2 ~ alpha^(2*28) = alpha^(g(g+1)) = alpha^56
    => 56 = 7 * 8

Self-consistency: 8g = g(g+1) => g = 7 is the UNIQUE solution.
And g+1 = 8 = dim(SU(3)) = N_c^2 - 1, from the eta' uniqueness condition.

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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

# ─── BST Constants ───
N_c   = 3           # color charges
n_C   = 5           # domain dimension (D_IV^5)
N_max = 137         # channel capacity = 1/alpha (integer part)
C_2   = 6           # Casimir eigenvalue (n_C + 1)
GENUS = 7           # genus of D_IV^5
ALPHA = 1.0 / 137.035999084   # fine-structure constant

# Derived
EXPONENT = 8 * GENUS           # = 56
F_BST = (np.log(N_max + 1) / 50.0)   # ~ ln(138)/50
LAMBDA_BST = F_BST * ALPHA**EXPONENT * np.exp(-2)
LAMBDA_OBS = 2.888e-122        # Planck 2018 (reduced Planck units)

# ─── Colors ───
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BRIGHT_GOLD = '#ffee44'
BLUE        = '#4488ff'
BLUE_DIM    = '#2255aa'
BLUE_GLOW   = '#66aaff'
GREEN       = '#44dd88'
GREEN_DIM   = '#228855'
GREEN_GLOW  = '#66ffaa'
RED_WARM    = '#ff6644'
PURPLE_GLOW = '#bb77ff'
PURPLE_DIM  = '#6633aa'
WHITE       = '#ffffff'
GREY        = '#888888'
LIGHT_GREY  = '#bbbbbb'
CYAN        = '#44dddd'


# ═══════════════════════════════════════════════════════════════════════
#  Why56 Class — Programmatic CI-scriptable API
# ═══════════════════════════════════════════════════════════════════════

class Why56:
    """
    BST analysis of why the cosmological constant exponent is exactly 56.

    Two independent derivations (neutrino-vacuum and partition function)
    both yield alpha^56, and their agreement uniquely selects genus g=7.

    Usage:
        w = Why56()
        print(w.route_A())
        print(w.route_B())
        print(w.self_consistency())
        print(w.exponent_chain())
        print(w.lambda_value())
        print(w.sweep_genus())
    """

    def __init__(self):
        self.N_c = N_c
        self.n_C = n_C
        self.N_max = N_max
        self.C_2 = C_2
        self.genus = GENUS
        self.alpha = ALPHA
        self.exponent = EXPONENT

    def route_A(self) -> dict:
        """
        Route A: 56 = 8g from the neutrino-vacuum connection.

        m_nu ~ alpha^(2g) * m_Pl      (neutrino mass from Bergman geometry)
        Lambda ~ (m_nu/m_Pl)^4         (vacuum energy ~ m^4)
               = (alpha^(2g))^4
               = alpha^(8g)
               = alpha^56

        The factor 8 = 4 (Lambda ~ m^4) x 2 (complex structure: holo + anti-holo).
        The factor 7 = genus of D_IV^5.
        """
        g = self.genus
        factor_4 = 4          # Lambda ~ m^4 in natural units
        factor_2 = 2          # complex structure (holomorphic + anti-holomorphic)
        factor_8 = factor_4 * factor_2
        exponent = factor_8 * g
        return {
            'route': 'A',
            'name': 'neutrino-vacuum connection',
            'genus': g,
            'factor_4_from_Lambda_m4': factor_4,
            'factor_2_from_complex_structure': factor_2,
            'factor_8': factor_8,
            'exponent': exponent,
            'formula': f'56 = 8 x {g} = {exponent}',
            'm_nu_scaling': f'alpha^(2*{g}) = alpha^{2*g}',
            'Lambda_scaling': f'alpha^(8*{g}) = alpha^{exponent}',
            'verified': exponent == 56,
        }

    def route_B(self) -> dict:
        """
        Route B: 56 = g(g+1) from the partition function.

        Z_0 ~ product_{j=0}^{g} (1 - q_j)
        Total alpha power = sum_{j=0}^{g} j = g(g+1)/2 = 28
        Lambda ~ |Z_0|^2 ~ alpha^(2 x 28) = alpha^56

        The factor g(g+1)/2 = triangular number T_g.
        """
        g = self.genus
        triangular = g * (g + 1) // 2     # = 28
        exponent = 2 * triangular          # = 56
        # Build the partition sum detail
        terms = [{'j': j, 'alpha_power': j} for j in range(g + 1)]
        return {
            'route': 'B',
            'name': 'partition function (ground state)',
            'genus': g,
            'triangular_number': triangular,
            'sum_formula': f'sum(j=0..{g}, j) = {g}*{g+1}/2 = {triangular}',
            'mod_squared': f'|Z_0|^2 ~ alpha^(2*{triangular}) = alpha^{exponent}',
            'exponent': exponent,
            'formula': f'56 = {g} x {g+1} = {exponent}',
            'partition_terms': terms,
            'verified': exponent == 56,
        }

    def self_consistency(self) -> dict:
        """
        Show that 8g = g(g+1) has the unique solution g = 7.

        Route A gives exponent = 8g.
        Route B gives exponent = g(g+1).
        Setting them equal: 8g = g(g+1) => 8 = g+1 => g = 7.

        Furthermore: g+1 = 8 = dim(SU(3)) = N_c^2 - 1, which follows
        from the eta-prime uniqueness condition.
        """
        # Solve: 8g = g(g+1) => g^2 + g - 8g = 0 => g^2 - 7g = 0 => g(g-7) = 0
        # Non-trivial solution: g = 7
        solutions = []
        for g_test in range(1, 100):
            if 8 * g_test == g_test * (g_test + 1):
                solutions.append(g_test)

        g = solutions[0] if solutions else None
        return {
            'equation': '8g = g(g+1)',
            'simplified': 'g^2 - 7g = 0 => g(g-7) = 0',
            'solutions': solutions,
            'physical_solution': g,
            'unique': len(solutions) == 1,
            'g_plus_1': g + 1 if g else None,
            'dim_SU3': self.N_c**2 - 1,
            'eta_prime_condition': f'g+1 = {g+1 if g else "?"} = dim(SU({self.N_c})) = {self.N_c}^2 - 1 = {self.N_c**2 - 1}',
            'verified': g == 7 and (g + 1) == (self.N_c**2 - 1),
        }

    def exponent_chain(self) -> list:
        """
        All BST exponents as multiples of C_2=6 and genus=7.

        The hierarchy of scales from Planck to Lambda is controlled by
        powers of alpha, each a multiple of C_2 or genus:
            alpha^12 = alpha^(2*C_2) -> electron/Planck ratio
            alpha^14 = alpha^(2*g)   -> neutrino/electron ratio
            alpha^24 = alpha^(4*C_2) -> Newton's G
            alpha^56 = alpha^(8*g)   -> cosmological constant
        """
        chain = [
            {
                'exponent': 12,
                'decomposition': f'2 x C_2 = 2 x {self.C_2}',
                'scale': 'm_e / m_Pl',
                'description': 'electron mass / Planck mass',
                'log10_ratio': 12 * np.log10(self.alpha),
            },
            {
                'exponent': 14,
                'decomposition': f'2 x g = 2 x {self.genus}',
                'scale': 'm_nu / m_e',
                'description': 'neutrino mass / electron mass',
                'log10_ratio': 14 * np.log10(self.alpha),
            },
            {
                'exponent': 24,
                'decomposition': f'4 x C_2 = 4 x {self.C_2}',
                'scale': 'G (Newton)',
                'description': 'gravitational coupling',
                'log10_ratio': 24 * np.log10(self.alpha),
            },
            {
                'exponent': 56,
                'decomposition': f'8 x g = 8 x {self.genus} = {self.genus} x {self.genus+1}',
                'scale': 'Lambda',
                'description': 'cosmological constant',
                'log10_ratio': 56 * np.log10(self.alpha),
            },
        ]
        return chain

    def lambda_value(self) -> dict:
        """
        Compute the cosmological constant from alpha^56.

        Lambda = F_BST * alpha^56 * e^(-2)
        where F_BST = ln(N_max + 1) / 50 = ln(138)/50
        """
        a56 = self.alpha ** 56
        f_bst = np.log(self.N_max + 1) / 50.0
        lam = f_bst * a56 * np.exp(-2)
        log10_lam = np.log10(lam)
        log10_obs = np.log10(LAMBDA_OBS)
        error_pct = abs(lam - LAMBDA_OBS) / LAMBDA_OBS * 100
        return {
            'F_BST': f_bst,
            'alpha_56': a56,
            'e_minus_2': np.exp(-2),
            'Lambda_BST': lam,
            'Lambda_observed': LAMBDA_OBS,
            'log10_BST': log10_lam,
            'log10_observed': log10_obs,
            'error_percent': error_pct,
            'formula': f'Lambda = (ln(138)/50) * alpha^56 * e^(-2)',
            'orders_of_magnitude': abs(log10_lam),
        }

    def sweep_genus(self, g_range=(1, 20)) -> list:
        """
        For each genus g in range, check if Routes A and B agree.

        Route A exponent = 8g
        Route B exponent = g(g+1)
        They agree only when 8g = g(g+1), i.e., g = 7.
        """
        results = []
        for g in range(g_range[0], g_range[1] + 1):
            route_a_exp = 8 * g
            route_b_exp = g * (g + 1)
            agree = (route_a_exp == route_b_exp)
            results.append({
                'genus': g,
                'route_A_exponent': route_a_exp,
                'route_B_exponent': route_b_exp,
                'agree': agree,
                'difference': route_b_exp - route_a_exp,
                'log10_Lambda_A': route_a_exp * np.log10(self.alpha),
                'log10_Lambda_B': route_b_exp * np.log10(self.alpha),
            })
        return results

    def __repr__(self):
        lv = self.lambda_value()
        return (
            f"Why56(\n"
            f"  exponent = {self.exponent} = 8 x {self.genus} = {self.genus} x {self.genus+1}\n"
            f"  genus    = {self.genus}  (of D_IV^5)\n"
            f"  Lambda   = {lv['Lambda_BST']:.3e}  (observed: {lv['Lambda_observed']:.3e})\n"
            f"  error    = {lv['error_percent']:.3f}%\n"
            f"  unique   = {self.self_consistency()['unique']}\n"
            f")"
        )


# ═══════════════════════════════════════════════════════════════════════
#  Visualization Helpers
# ═══════════════════════════════════════════════════════════════════════

def glow_text(ax, x, y, text, color=WHITE, fontsize=12, ha='center', va='center',
              weight='normal', alpha=1.0, glow_color=None, glow_width=3,
              family='monospace', **kwargs):
    """Render text with a subtle outer glow."""
    gc = glow_color or color
    txt = ax.text(x, y, text, fontsize=fontsize, fontweight=weight,
                  color=color, ha=ha, va=va, fontfamily=family, alpha=alpha,
                  path_effects=[pe.withStroke(linewidth=glow_width, foreground=gc,
                                              alpha=alpha * 0.3)],
                  **kwargs)
    return txt


def draw_rounded_box(ax, x, y, w, h, text, text_color=WHITE, box_color='#222244',
                     edge_color=BLUE, fontsize=11, lw=1.5, text_weight='normal'):
    """Draw a rounded rectangle with centered text."""
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle='round,pad=0.05',
                         facecolor=box_color, edgecolor=edge_color,
                         linewidth=lw, zorder=2)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=text_color,
            ha='center', va='center', fontfamily='monospace',
            fontweight=text_weight, zorder=3)
    return box


def draw_arrow(ax, x1, y1, x2, y2, color=GREY, lw=1.5, style='->', shrinkA=4, shrinkB=4):
    """Draw a styled arrow between two points."""
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style, color=color, linewidth=lw,
        shrinkA=shrinkA, shrinkB=shrinkB,
        mutation_scale=12, zorder=1
    )
    ax.add_patch(arrow)
    return arrow


# ═══════════════════════════════════════════════════════════════════════
#  Panel 1: Two Routes to 56
# ═══════════════════════════════════════════════════════════════════════

def draw_panel_routes(ax):
    """Left panel: Two parallel derivation chains converging at 56."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # ── Title ──
    glow_text(ax, 5, 9.6, 'TWO ROUTES TO 56', color=GOLD, fontsize=14,
              weight='bold', glow_color=GOLD_DIM)

    # ── Route A (left column, blue) ──
    route_a_x = 2.8
    glow_text(ax, route_a_x, 9.05, 'ROUTE A', color=BLUE, fontsize=11, weight='bold')
    glow_text(ax, route_a_x, 8.65, 'neutrino-vacuum', color=BLUE_DIM, fontsize=8)

    steps_a = [
        (8.1, r'm$_\nu$ ~ $\alpha^{2g}$ m$_{Pl}$',      BLUE_GLOW, '#0a1a3a', BLUE),
        (7.2, r'$\Lambda$ ~ (m$_\nu$/m$_{Pl}$)$^4$',     BLUE_GLOW, '#0a1a3a', BLUE),
        (6.3, r'= ($\alpha^{2g}$)$^4$',                   BLUE_GLOW, '#0a1a3a', BLUE),
        (5.4, r'= $\alpha^{8g}$',                         WHITE,     '#0a1a3a', BLUE),
        (4.5, r'8 = 4 $\times$ 2',                        BLUE_DIM,  '#0a1a3a', BLUE_DIM),
    ]
    for yp, label, tc, bc, ec in steps_a:
        draw_rounded_box(ax, route_a_x, yp, 3.8, 0.55, label,
                         text_color=tc, box_color=bc, edge_color=ec,
                         fontsize=10, lw=1.2)

    # Arrows down route A
    for i in range(len(steps_a) - 1):
        y_top = steps_a[i][0] - 0.28
        y_bot = steps_a[i+1][0] + 0.28
        draw_arrow(ax, route_a_x, y_top, route_a_x, y_bot,
                   color=BLUE_DIM, lw=1.2)

    # Labels for factor 8 decomposition
    glow_text(ax, route_a_x - 1.2, 4.5, '4: m$^4$', color=BLUE_DIM, fontsize=7,
              ha='right')
    glow_text(ax, route_a_x + 1.2, 4.5, '2: holo', color=BLUE_DIM, fontsize=7,
              ha='left')

    # ── Route B (right column, green) ──
    route_b_x = 7.2
    glow_text(ax, route_b_x, 9.05, 'ROUTE B', color=GREEN, fontsize=11, weight='bold')
    glow_text(ax, route_b_x, 8.65, 'partition function', color=GREEN_DIM, fontsize=8)

    steps_b = [
        (8.1, r'Z$_0$ ~ $\prod_{j=0}^{g}$(1-q$_j$)',    GREEN_GLOW, '#0a2a1a', GREEN),
        (7.2, r'$\Sigma$j = g(g+1)/2 = 28',              GREEN_GLOW, '#0a2a1a', GREEN),
        (6.3, r'$\Lambda$ ~ |Z$_0$|$^2$',                GREEN_GLOW, '#0a2a1a', GREEN),
        (5.4, r'= $\alpha^{2 \times 28}$ = $\alpha^{56}$', WHITE,    '#0a2a1a', GREEN),
        (4.5, r'T$_7$ = 28  (triangular)',                GREEN_DIM, '#0a2a1a', GREEN_DIM),
    ]
    for yp, label, tc, bc, ec in steps_b:
        draw_rounded_box(ax, route_b_x, yp, 3.8, 0.55, label,
                         text_color=tc, box_color=bc, edge_color=ec,
                         fontsize=10, lw=1.2)

    # Arrows down route B
    for i in range(len(steps_b) - 1):
        y_top = steps_b[i][0] - 0.28
        y_bot = steps_b[i+1][0] + 0.28
        draw_arrow(ax, route_b_x, y_top, route_b_x, y_bot,
                   color=GREEN_DIM, lw=1.2)

    # ── Convergence at bottom ──
    # Arrows from both routes to center
    draw_arrow(ax, route_a_x + 0.5, 4.5 - 0.35, 5.0, 3.25,
               color=GOLD_DIM, lw=1.5, style='->')
    draw_arrow(ax, route_b_x - 0.5, 4.5 - 0.35, 5.0, 3.25,
               color=GOLD_DIM, lw=1.5, style='->')

    # The convergence box
    convergence_box = FancyBboxPatch((1.8, 2.1), 6.4, 1.8,
                                     boxstyle='round,pad=0.15',
                                     facecolor='#1a1a0a',
                                     edgecolor=GOLD,
                                     linewidth=2.5, zorder=2)
    ax.add_patch(convergence_box)

    glow_text(ax, 5.0, 3.4, '56 = 8 x 7 = 7 x 8', color=BRIGHT_GOLD,
              fontsize=16, weight='bold', glow_color=GOLD_DIM, glow_width=4)

    glow_text(ax, 5.0, 2.65, 'Both routes arrive at the same exponent',
              color=GOLD_DIM, fontsize=8.5)

    # Bottom: the physical meaning
    glow_text(ax, 5.0, 1.3, r'$\Lambda$ = F$_{BST}$ $\cdot$ $\alpha^{56}$ $\cdot$ e$^{-2}$',
              color=LIGHT_GREY, fontsize=11, weight='bold')
    glow_text(ax, 5.0, 0.7, r'$\approx$ 2.9 $\times$ 10$^{-122}$ Planck units',
              color=GREY, fontsize=9)


# ═══════════════════════════════════════════════════════════════════════
#  Panel 2: The Uniqueness Trap
# ═══════════════════════════════════════════════════════════════════════

def draw_panel_uniqueness(ax):
    """Center panel: 8g vs g(g+1) — they intersect only at g=7."""
    ax.set_facecolor(DARK_PANEL)

    # ── Title ──
    glow_text(ax, 0.5, 1.08, 'THE UNIQUENESS TRAP', color=GOLD, fontsize=14,
              weight='bold', glow_color=GOLD_DIM,
              transform=ax.transAxes)

    # ── Data ──
    g_vals = np.arange(0, 16, 1)
    g_fine = np.linspace(0, 15, 300)
    route_a_vals = 8 * g_fine             # line
    route_b_vals = g_fine * (g_fine + 1)  # parabola

    # ── Plot ──
    ax.plot(g_fine, route_a_vals, color=BLUE, linewidth=2.5, label='Route A:  8g',
            zorder=3, alpha=0.9)
    ax.plot(g_fine, route_b_vals, color=GREEN, linewidth=2.5, label='Route B:  g(g+1)',
            zorder=3, alpha=0.9)

    # Shade the region between the curves
    mask_below = route_a_vals >= route_b_vals
    ax.fill_between(g_fine, route_a_vals, route_b_vals, where=mask_below,
                    alpha=0.06, color=BLUE, zorder=1)
    ax.fill_between(g_fine, route_a_vals, route_b_vals, where=~mask_below,
                    alpha=0.06, color=GREEN, zorder=1)

    # ── Intersection point at g=7 ──
    g_int = 7
    y_int = 8 * g_int  # = 56

    # Golden dot
    ax.plot(g_int, y_int, 'o', markersize=16, color=GOLD,
            markeredgecolor='#ffff88', markeredgewidth=2, zorder=5)
    ax.plot(g_int, y_int, 'o', markersize=8, color=WHITE, zorder=6)

    # Annotation
    ax.annotate(
        f'g = 7\nexponent = 56',
        xy=(g_int, y_int), xytext=(g_int + 2.5, y_int + 30),
        fontsize=10, fontfamily='monospace', color=BRIGHT_GOLD,
        fontweight='bold',
        arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                  edgecolor=GOLD, linewidth=1.5),
        zorder=7
    )

    # ── Vertical dashed line at g=7 ──
    ax.axvline(x=7, color=GOLD_DIM, linestyle='--', linewidth=1, alpha=0.5, zorder=2)
    ax.axhline(y=56, color=GOLD_DIM, linestyle='--', linewidth=1, alpha=0.5, zorder=2)

    # ── Integer markers ──
    for g in range(1, 16):
        ya = 8 * g
        yb = g * (g + 1)
        if g != 7:
            ax.plot(g, ya, 's', markersize=5, color=BLUE_DIM, alpha=0.7, zorder=4)
            ax.plot(g, yb, 's', markersize=5, color=GREEN_DIM, alpha=0.7, zorder=4)

    # ── Labels below the plot ──
    ax.text(7, -28, 'Only g = 7 makes both routes agree',
            fontsize=10, color=WHITE, ha='center', fontfamily='monospace',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a0a',
                      edgecolor=GOLD_DIM, linewidth=1))

    ax.text(7, -42, r'g + 1 = 8 = dim(SU(3)) = N$_c^2$ $-$ 1',
            fontsize=9, color=CYAN, ha='center', fontfamily='monospace')

    # ── Styling ──
    ax.set_xlim(-0.5, 15.5)
    ax.set_ylim(-55, 250)
    ax.set_xlabel('genus  g', fontsize=11, color=LIGHT_GREY, fontfamily='monospace')
    ax.set_ylabel('exponent', fontsize=11, color=LIGHT_GREY, fontfamily='monospace')
    ax.tick_params(colors=GREY, labelsize=9)
    ax.spines['bottom'].set_color('#333355')
    ax.spines['left'].set_color('#333355')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='upper left', fontsize=10, facecolor=DARK_PANEL,
              edgecolor='#333355', labelcolor=LIGHT_GREY,
              prop={'family': 'monospace'})

    # Grid
    ax.grid(True, alpha=0.1, color='#444466')


# ═══════════════════════════════════════════════════════════════════════
#  Panel 3: The Exponent Tower
# ═══════════════════════════════════════════════════════════════════════

def draw_panel_tower(ax):
    """Right panel: Vertical logarithmic tower from Planck to Lambda."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # ── Title ──
    glow_text(ax, 5, 9.6, 'THE EXPONENT TOWER', color=GOLD, fontsize=14,
              weight='bold', glow_color=GOLD_DIM)

    # ── Scale definitions ──
    # We place scales vertically by their alpha-power exponent
    # Planck (0) at top, Lambda (56) at bottom
    # Vertical range: y=8.8 (top, Planck) to y=1.0 (bottom, Lambda)
    y_top = 8.8
    y_bot = 1.0
    y_span = y_top - y_bot

    scales = [
        # (exponent, label, decomposition, color, description)
        (0,   r'm$_{Pl}$',   '',                   WHITE,       'Planck scale'),
        (12,  r'm$_e$',      r'2$\times$C$_2$',    BLUE_GLOW,   'electron mass'),
        (14,  r'm$_\nu$',    r'2$\times$g',         PURPLE_GLOW, 'neutrino mass'),
        (24,  'G',           r'4$\times$C$_2$',    CYAN,        "Newton's G"),
        (56,  r'$\Lambda$',  r'8$\times$g',         GOLD,        'cosmological const'),
    ]

    max_exp = 56
    x_bar = 4.0      # x position of the vertical bar
    x_label = 6.2    # x position of labels

    # ── Color gradient for the bar ──
    n_seg = 200
    for i in range(n_seg):
        frac = i / n_seg
        y1 = y_top - frac * y_span
        y2 = y_top - (frac + 1/n_seg) * y_span
        # Color gradient: white -> blue -> deep purple
        if frac < 0.3:
            t = frac / 0.3
            r = 1.0 - t * 0.7
            g = 1.0 - t * 0.7
            b = 1.0
        elif frac < 0.7:
            t = (frac - 0.3) / 0.4
            r = 0.3 - t * 0.15
            g = 0.3 - t * 0.2
            b = 1.0 - t * 0.3
        else:
            t = (frac - 0.7) / 0.3
            r = 0.15 - t * 0.05
            g = 0.1 - t * 0.05
            b = 0.7 - t * 0.3
        c = (max(0, r), max(0, g), max(0, b))
        ax.fill_between([x_bar - 0.15, x_bar + 0.15], y1, y2,
                        color=c, alpha=0.8, zorder=2)

    # ── Scale markers ──
    for exp, label, decomp, color, desc in scales:
        frac = exp / max_exp
        y = y_top - frac * y_span

        # Horizontal tick
        ax.plot([x_bar - 0.4, x_bar + 0.4], [y, y],
                color=color, linewidth=2, zorder=4)

        # Dot on the bar
        ax.plot(x_bar, y, 'o', color=color, markersize=8,
                markeredgecolor='#000000', markeredgewidth=1, zorder=5)

        # Label and decomposition (right side)
        glow_text(ax, x_label, y + 0.15, label, color=color, fontsize=12,
                  weight='bold', ha='left', glow_color=color, glow_width=2)
        if decomp:
            glow_text(ax, x_label, y - 0.2, r'$\alpha^{' + str(exp) + '}$  (' + decomp + ')',
                      color=GREY, fontsize=8, ha='left')

        # Exponent number (left side)
        if exp > 0:
            glow_text(ax, x_bar - 0.8, y, str(exp), color=color, fontsize=11,
                      weight='bold', ha='right')

        # Description (far right, small)
        glow_text(ax, 9.5, y, desc, color='#555566', fontsize=7, ha='right')

    # ── Arrows showing the "drops" ──
    drop_pairs = [
        (0, 12, BLUE_DIM, r'$\alpha^{12}$'),
        (12, 14, PURPLE_DIM, r'$\alpha^{2}$'),
        (14, 24, '#336666', r'$\alpha^{10}$'),
        (24, 56, GOLD_DIM, r'$\alpha^{32}$'),
    ]

    x_arrow = 2.2
    for exp_top, exp_bot, color, label in drop_pairs:
        y1 = y_top - (exp_top / max_exp) * y_span - 0.15
        y2 = y_top - (exp_bot / max_exp) * y_span + 0.15
        # Bracket-style line
        ax.plot([x_arrow, x_arrow], [y1, y2], color=color, linewidth=1.5,
                alpha=0.7, zorder=3)
        ax.plot([x_arrow - 0.15, x_arrow + 0.15], [y1, y1], color=color,
                linewidth=1.5, alpha=0.7, zorder=3)
        ax.plot([x_arrow - 0.15, x_arrow + 0.15], [y2, y2], color=color,
                linewidth=1.5, alpha=0.7, zorder=3)
        y_mid = (y1 + y2) / 2
        glow_text(ax, x_arrow - 0.2, y_mid, label, color=color, fontsize=7,
                  ha='right', alpha=0.8)

    # ── The big drop annotation ──
    y_G = y_top - (24 / max_exp) * y_span
    y_L = y_top - (56 / max_exp) * y_span
    y_mid = (y_G + y_L) / 2

    # Emphasize the biggest drop
    ax.annotate('', xy=(x_arrow + 0.5, y_L + 0.15), xytext=(x_arrow + 0.5, y_G - 0.15),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5,
                                connectionstyle='arc3,rad=0.15'),
                zorder=4)

    glow_text(ax, 1.0, y_mid, 'longest\ndrop', color=GOLD_DIM, fontsize=8,
              ha='center', alpha=0.7)

    # ── Log-scale annotation at bottom ──
    lam_val = Why56().lambda_value()
    glow_text(ax, 5.0, 0.45,
              f'122 orders of magnitude\nfrom Planck to Lambda',
              color=GREY, fontsize=8)


# ═══════════════════════════════════════════════════════════════════════
#  Main Visualization
# ═══════════════════════════════════════════════════════════════════════

def build_figure():
    """Construct the complete 3-panel Why56 visualization."""
    fig = plt.figure(figsize=(19, 11), facecolor=BG)
    fig.canvas.manager.set_window_title('Why 56 — The Cosmological Constant Exponent (BST)')

    # ── Master title ──
    fig.text(0.5, 0.975, 'WHY 56?', fontsize=30, fontweight='bold',
             color=GOLD, ha='center', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground=GOLD_DIM)])
    fig.text(0.5, 0.945, 'The cosmological constant exponent is self-consistent only at the BST genus',
             fontsize=11, color=GOLD_DIM, ha='center', fontfamily='monospace')

    # ── Panel 1: Two Routes (left) ──
    ax_routes = fig.add_axes([0.02, 0.08, 0.31, 0.84])
    draw_panel_routes(ax_routes)

    # ── Panel 2: Uniqueness (center) ──
    ax_unique = fig.add_axes([0.36, 0.16, 0.30, 0.68])
    draw_panel_uniqueness(ax_unique)

    # ── Panel 3: Exponent Tower (right) ──
    ax_tower = fig.add_axes([0.69, 0.08, 0.30, 0.84])
    draw_panel_tower(ax_tower)

    # ── Bottom strip ──
    strip = FancyBboxPatch((0.05, 0.005), 0.90, 0.05,
                           boxstyle='round,pad=0.01',
                           facecolor='#0d0d1a',
                           edgecolor=GOLD_DIM, linewidth=1.5,
                           transform=fig.transFigure, zorder=10)
    fig.patches.append(strip)

    fig.text(0.5, 0.03,
             '56 = 8 x 7 = 7 x 8.   The cosmological constant exponent is '
             'self-consistent only at the BST genus.',
             fontsize=12, color=BRIGHT_GOLD, ha='center',
             fontfamily='monospace', fontweight='bold',
             path_effects=[pe.withStroke(linewidth=2, foreground=GOLD_DIM)],
             zorder=11)

    fig.text(0.5, 0.008,
             'g+1 = 8 = dim(SU(3)).   Two integers, one universe.',
             fontsize=9, color=GOLD_DIM, ha='center',
             fontfamily='monospace', zorder=11)

    return fig


# ═══════════════════════════════════════════════════════════════════════
#  Programmatic Demo
# ═══════════════════════════════════════════════════════════════════════

def demo():
    """Run programmatic demo of the Why56 class."""
    w = Why56()
    print("=" * 70)
    print("  WHY 56 — BST Cosmological Constant Exponent Analysis")
    print("=" * 70)

    print(f"\n{w}\n")

    # Route A
    ra = w.route_A()
    print(f"ROUTE A ({ra['name']}):")
    print(f"  {ra['formula']}")
    print(f"  m_nu scaling: {ra['m_nu_scaling']}")
    print(f"  Lambda scaling: {ra['Lambda_scaling']}")
    print(f"  Verified: {ra['verified']}")

    # Route B
    rb = w.route_B()
    print(f"\nROUTE B ({rb['name']}):")
    print(f"  {rb['formula']}")
    print(f"  Triangular number T_7 = {rb['triangular_number']}")
    print(f"  {rb['mod_squared']}")
    print(f"  Verified: {rb['verified']}")

    # Self-consistency
    sc = w.self_consistency()
    print(f"\nSELF-CONSISTENCY:")
    print(f"  Equation: {sc['equation']}")
    print(f"  Simplified: {sc['simplified']}")
    print(f"  Solutions: g = {sc['solutions']}")
    print(f"  Unique: {sc['unique']}")
    print(f"  {sc['eta_prime_condition']}")

    # Exponent chain
    print(f"\nEXPONENT CHAIN:")
    for entry in w.exponent_chain():
        print(f"  alpha^{entry['exponent']:2d} = alpha^({entry['decomposition']})  "
              f"-> {entry['scale']:8s}  ({entry['description']})"
              f"  [10^{entry['log10_ratio']:.1f}]")

    # Lambda value
    lv = w.lambda_value()
    print(f"\nCOSMOLOGICAL CONSTANT:")
    print(f"  {lv['formula']}")
    print(f"  Lambda_BST     = {lv['Lambda_BST']:.4e}")
    print(f"  Lambda_observed = {lv['Lambda_observed']:.4e}")
    print(f"  Error: {lv['error_percent']:.3f}%")
    print(f"  Orders of magnitude below Planck: {lv['orders_of_magnitude']:.1f}")

    # Genus sweep
    print(f"\nGENUS SWEEP (which g makes Routes A and B agree?):")
    print(f"  {'g':>3s}  {'8g':>5s}  {'g(g+1)':>7s}  {'agree':>6s}  {'diff':>5s}")
    print(f"  {'---':>3s}  {'-----':>5s}  {'-------':>7s}  {'------':>6s}  {'-----':>5s}")
    for entry in w.sweep_genus(g_range=(1, 15)):
        mark = ' <<<' if entry['agree'] else ''
        print(f"  {entry['genus']:3d}  {entry['route_A_exponent']:5d}  "
              f"{entry['route_B_exponent']:7d}  "
              f"{'YES' if entry['agree'] else 'no':>6s}  "
              f"{entry['difference']:+5d}{mark}")

    print(f"\n{'=' * 70}")


# ═══════════════════════════════════════════════════════════════════════
#  Entry Point
# ═══════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    # Run programmatic demo first
    demo()

    # Build and show the visualization
    print("\nLaunching visualization...")
    fig = build_figure()
    plt.show()
