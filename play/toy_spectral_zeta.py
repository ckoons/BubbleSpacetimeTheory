#!/usr/bin/env python3
"""
BST Toy 147 — The Spectral Zeta Function of Q^5
=================================================
The spectral zeta function of the Laplacian on Q^5 = SO(7)/[SO(5) x SO(2)]
is the bridge from topology to number theory.

    zeta_Delta(s) = sum_{k=1}^infty  d_k / lambda_k^s

where:
    d_k = (k+1)(k+2)(k+3)(k+4)(2k+5) / 120    (multiplicity of k-th eigenvalue)
    lambda_k = k(k+5)                            (eigenvalue of Laplacian on Q^5)

Key results:
  - Convergence for Re(s) > 3   (since d_k ~ k^5/60, lambda_k ~ k^2)
  - Poles at s = 5, 4, 3, 2, 1 with residues from Seeley-DeWitt coefficients
  - The 1/60 Theorem: at s=3 the partial sums diverge as (1/60) ln N + gamma_Delta
    where 60 = n_C!/2 = |A_5| = icosahedral group = |W(D_5)|/32
  - Convergent values: zeta_Delta(4) = 0.00666..., zeta_Delta(5) = 0.000966...
  - Odd-Zeta Parity: only zeta(3), zeta(5), ... appear (even cancel by anti-symmetry)
  - Exact: zeta_Delta(4) = (101/18750)*zeta(3) + 349/1875000
  - H_5 = 137/60: the harmonic number encodes N_max and |A_5|
  - Bridge: Chern -> Seeley-DeWitt a_k -> Mellin -> zeta_Delta poles -> Selberg -> zeta(s)

CI Interface:
    from toy_spectral_zeta import SpectralZetaExplorer
    sze = SpectralZetaExplorer()
    sze.show()

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import math
from math import comb, factorial, pi

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe


# ═══════════════════════════════════════════════════════════════════
#  BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c   = 3                                # color charges
n_C   = 5                                # complex dimension of D_IV^5
C2    = n_C + 1                           # = 6, Casimir eigenvalue
genus = n_C + 2                           # = 7
N_max = 137                               # channel capacity
W_D5  = factorial(n_C) * 2**(n_C - 1)    # |W(D_5)| = 1920
Vol_D = pi**n_C / W_D5                   # Vol(D_IV^5) = pi^5/1920

# Chern classes of Q^5
CHERN = [1, 5, 11, 13, 9, 3]             # c_0 through c_5


# ═══════════════════════════════════════════════════════════════════
#  COLORS
# ═══════════════════════════════════════════════════════════════════

BG      = '#0a0a1a'
GOLD    = '#ffd700'
CYAN    = '#00e5ff'
GREEN   = '#00ff88'
WHITE   = '#f0f0f0'
CORAL   = '#ff6b6b'
DIM     = '#556677'
MAGENTA = '#cc66ff'

GLOW = [pe.withStroke(linewidth=3, foreground=GOLD)]
GLOW_CYAN = [pe.withStroke(linewidth=3, foreground=CYAN)]


# ═══════════════════════════════════════════════════════════════════
#  SPECTRAL ZETA COMPUTATION
# ═══════════════════════════════════════════════════════════════════

def d_k(k):
    """Multiplicity of the k-th eigenvalue on Q^5."""
    return comb(k + 4, 4) * (2 * k + 5) // 5


def lambda_k(k):
    """k-th eigenvalue of the Laplacian on Q^5."""
    return k * (k + 5)


def spectral_zeta(s, N=10000):
    """Compute zeta_Delta(s) = sum_{k=1}^N d_k / lambda_k^s."""
    return sum(d_k(k) / lambda_k(k)**s for k in range(1, N + 1))


def partial_sums_s3(N):
    """Partial sums at s=3 (divergent — logarithmic growth)."""
    total = 0.0
    sums = []
    for k in range(1, N + 1):
        total += d_k(k) / lambda_k(k)**3
        sums.append(total)
    return sums


def fit_1_60_slope(sums, Nvals):
    """
    Fit S(N) ~ slope * ln(N) + intercept.
    Returns (slope, intercept).
    """
    ln_N = np.log(Nvals)
    # Use latter half for a clean fit
    half = len(ln_N) // 2
    x = ln_N[half:]
    y = np.array(sums[half:])
    A = np.vstack([x, np.ones(len(x))]).T
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    return slope, intercept


# ═══════════════════════════════════════════════════════════════════
#  MAIN VISUALIZATION CLASS
# ═══════════════════════════════════════════════════════════════════

class SpectralZetaExplorer:
    """
    BST Toy 147 — The Spectral Zeta Function of Q^5.

    Builds a 6-panel visualization of zeta_Delta(s), its pole structure,
    the 1/60 theorem, Seeley-DeWitt coefficients, convergent values,
    and the bridge from topology to number theory.
    """

    def __init__(self):
        # ── precompute all data ──
        self._compute_all()

        # ── build figure ──
        self.fig = plt.figure(figsize=(20, 12), facecolor=BG)

        # 6 panels: 3 top, 3 bottom
        margin_l, margin_r = 0.05, 0.02
        margin_b, margin_t = 0.07, 0.08
        hgap, vgap = 0.04, 0.08
        pw = (1.0 - margin_l - margin_r - 2 * hgap) / 3
        ph = (1.0 - margin_b - margin_t - vgap) / 2

        self.axes = []
        for row in range(2):
            for col in range(3):
                l = margin_l + col * (pw + hgap)
                b = margin_b + (1 - row) * (ph + vgap)
                ax = self.fig.add_axes([l, b, pw, ph])
                ax.set_facecolor(BG)
                for spine in ax.spines.values():
                    spine.set_color(DIM)
                ax.tick_params(colors=DIM, labelsize=8)
                self.axes.append(ax)

        # ── suptitle ──
        self.fig.text(
            0.5, 0.97,
            r'THE SPECTRAL ZETA FUNCTION OF $Q^5$',
            ha='center', va='top', fontsize=20, fontweight='bold',
            color=GOLD,
            path_effects=[pe.withStroke(linewidth=3, foreground='#ffd700')],
        )
        self.fig.text(
            0.5, 0.935,
            r'$\zeta_\Delta(s) = \sum_{k=1}^{\infty}\; d_k \,/\, \lambda_k^{\,s}$'
            r'$\qquad d_k = \binom{k+4}{4}(2k+5)/5$'
            r'$\qquad \lambda_k = k(k+5)$',
            ha='center', va='top', fontsize=11, color=WHITE,
        )

        # ── copyright ──
        self.fig.text(
            0.5, 0.015,
            u'\u00a9 2026 Casey Koons  |  BST Toy 147 \u2014 The Spectral Zeta Function',
            ha='center', va='bottom', fontsize=9, color=DIM,
        )

        # ── draw all panels ──
        self._panel_partial_sums(self.axes[0])
        self._panel_1_60_theorem(self.axes[1])
        self._panel_pole_structure(self.axes[2])
        self._panel_seeley_chern(self.axes[3])
        self._panel_convergent_values(self.axes[4])
        self._panel_bridge(self.axes[5])

    # ─────────────────────────────────────────────────────────────
    #  PRECOMPUTE
    # ─────────────────────────────────────────────────────────────

    def _compute_all(self):
        """Precompute all numerical data."""
        # Convergent values
        self.s_vals = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0]
        self.zeta_vals = {s: spectral_zeta(s, N=10000) for s in self.s_vals}

        # Integer-s values for table
        self.zeta_int = {}
        for s in [4, 5, 6, 7, 8]:
            self.zeta_int[s] = spectral_zeta(s, N=10000)

        # 1/60 theorem data
        N_max_sum = 5000
        self.sums_s3 = partial_sums_s3(N_max_sum)
        self.N_range = np.arange(1, N_max_sum + 1)
        self.slope, self.intercept = fit_1_60_slope(
            self.sums_s3, self.N_range
        )

    # ─────────────────────────────────────────────────────────────
    #  PANEL 1: zeta_Delta(s) Partial Sums
    # ─────────────────────────────────────────────────────────────

    def _panel_partial_sums(self, ax):
        ax.set_title(r'$\zeta_\Delta(s)$ Partial Sums', color=GOLD,
                     fontsize=12, fontweight='bold', pad=8)

        s_plot = np.array(self.s_vals)
        z_plot = np.array([self.zeta_vals[s] for s in self.s_vals])

        ax.plot(s_plot, z_plot, 'o-', color=GOLD, markersize=7,
                linewidth=2, zorder=5)

        # s=3 pole boundary
        ax.axvline(x=3.0, color=CORAL, linestyle='--', linewidth=2, alpha=0.8)
        ax.text(3.05, max(z_plot) * 0.85, 's = 3: POLE',
                color=CORAL, fontsize=10, fontweight='bold', va='top')

        # Shade convergent region
        ax.axvspan(3.0, 9.0, alpha=0.05, color=CYAN)
        ax.text(6.0, max(z_plot) * 0.95, 'Re(s) > 3: CONVERGENT',
                color=CYAN, fontsize=8, ha='center', alpha=0.7)

        # Mark key values
        z4 = self.zeta_int[4]
        z5 = self.zeta_int[5]
        ax.annotate(
            f'$\\zeta_\\Delta(4) = {z4:.10f}$',
            xy=(4.0, z4), xytext=(5.0, z4 * 1.3),
            color=WHITE, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2),
        )
        ax.annotate(
            f'$\\zeta_\\Delta(5) = {z5:.10f}$',
            xy=(5.0, z5), xytext=(6.2, z5 + z4 * 0.15),
            color=WHITE, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2),
        )

        ax.set_xlabel('s', color=DIM, fontsize=10)
        ax.set_ylabel(r'$\zeta_\Delta(s)$', color=DIM, fontsize=10)
        ax.set_xlim(2.8, 8.5)
        ax.set_ylim(-0.002, max(z_plot) * 1.15)

    # ─────────────────────────────────────────────────────────────
    #  PANEL 2: The 1/60 Theorem
    # ─────────────────────────────────────────────────────────────

    def _panel_1_60_theorem(self, ax):
        ax.set_title('The 1/60 Theorem', color=GOLD,
                     fontsize=12, fontweight='bold', pad=8)

        ln_N = np.log(self.N_range)
        sums = np.array(self.sums_s3)

        # Plot partial sums vs ln(N)
        # Subsample for plotting
        idx = np.unique(np.logspace(0, np.log10(len(sums)), 800).astype(int) - 1)
        idx = idx[idx < len(sums)]
        ax.plot(ln_N[idx], sums[idx], '-', color=CYAN, linewidth=1.5,
                alpha=0.9, label=r'$S(N) = \sum_{k=1}^{N} d_k / \lambda_k^3$')

        # Overlay the fitted line
        x_fit = np.linspace(0, ln_N[-1], 200)
        y_fit = self.slope * x_fit + self.intercept
        ax.plot(x_fit, y_fit, '--', color=CORAL, linewidth=2, alpha=0.9,
                label=rf'$(1/60)\,\ln N + \gamma_\Delta$')

        # Annotate slope
        ax.text(
            0.05, 0.92,
            f'slope = {self.slope:.6f}\n'
            f'1/60  = {1/60:.6f}\n'
            f'error = {abs(self.slope - 1/60):.2e}',
            transform=ax.transAxes, fontsize=9, color=WHITE,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, alpha=0.9),
        )

        # Annotate the significance of 60
        ax.text(
            0.05, 0.52,
            r'$60 = n_C!/2 = |A_5|$' '\n'
            r'$= |W(D_5)|/32$' '\n'
            '= icosahedral group',
            transform=ax.transAxes, fontsize=9, color=GOLD,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.5),
        )

        ax.set_xlabel(r'$\ln\, N$', color=DIM, fontsize=10)
        ax.set_ylabel(r'$S(N)$', color=DIM, fontsize=10)
        ax.legend(fontsize=8, loc='lower right',
                  facecolor=BG, edgecolor=DIM, labelcolor=WHITE)

    # ─────────────────────────────────────────────────────────────
    #  PANEL 3: Pole Structure
    # ─────────────────────────────────────────────────────────────

    def _panel_pole_structure(self, ax):
        ax.set_title('Pole Structure', color=GOLD,
                     fontsize=12, fontweight='bold', pad=8)

        # Draw the s-axis
        ax.axhline(y=0, color=DIM, linewidth=1.5, zorder=1)

        # Shade convergent region
        ax.axvspan(3.0, 6.5, ymin=0.0, ymax=1.0, alpha=0.06, color=CYAN)
        ax.text(4.7, 0.85, 'CONVERGENT', color=CYAN, fontsize=9,
                ha='center', alpha=0.6, transform=ax.get_xaxis_transform())

        # Shade divergent region
        ax.axvspan(-0.5, 3.0, ymin=0.0, ymax=1.0, alpha=0.04, color=CORAL)

        # Pole data: (position, label, sublabel, color, arrow_top)
        # Stagger heights to avoid overlap
        poles = [
            (5, r'$A_0$', 'Vol',              CYAN,  0.55),
            (4, r'$A_1$', r'$\propto R$',     GOLD,  0.72),
            (3, r'$A_2$', r'$\propto |Rm|^2$', CORAL, 0.92),
            (2, r'$A_3$', '',                  GREEN, 0.48),
            (1, r'$A_4$', '',                  WHITE, 0.35),
        ]

        for s_pos, label, sublabel, color, arrow_top in poles:
            # Vertical arrow from just above axis to arrow_top
            ax.annotate(
                '', xy=(s_pos, arrow_top), xytext=(s_pos, 0.04),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5),
            )
            # Pole marker on axis
            ax.plot(s_pos, 0, 'o', color=color, markersize=10, zorder=5)
            # Label above arrow
            ax.text(s_pos, arrow_top + 0.03, label, color=color,
                    fontsize=11, fontweight='bold', ha='center', va='bottom')
            if sublabel:
                ax.text(s_pos, arrow_top + 0.12, sublabel, color=color,
                        fontsize=8, ha='center', va='bottom', alpha=0.8)

        # Highlight the s=3 key pole with glow
        ax.plot(3, 0, 'o', color=CORAL, markersize=16, zorder=4, alpha=0.25)

        # Arrow from s=3 to Riemann label
        ax.annotate(
            r'$\rightarrow$ Riemann via Selberg',
            xy=(3.15, 0.65), xytext=(4.5, 0.42),
            color=CORAL, fontsize=9, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CORAL, lw=1.5,
                            connectionstyle='arc3,rad=-0.2'),
        )

        # s-axis labels
        for s_pos in range(0, 7):
            ax.text(s_pos, -0.08, str(s_pos), color=DIM, fontsize=9,
                    ha='center', va='top')

        ax.set_xlim(-0.5, 6.5)
        ax.set_ylim(-0.15, 1.25)
        ax.set_xlabel('s', color=DIM, fontsize=10)
        ax.set_yticks([])

        # Half-sum annotation
        ax.text(
            0.98, 0.02,
            r'$|\rho|^2 = 17/2$  (spectral gap)',
            transform=ax.transAxes, fontsize=8, color=MAGENTA,
            ha='right', va='bottom', alpha=0.8,
        )
        # Zonal spectral coefficients: r_5 = 137/11 = N_max/c_2.
        # The same zeta function's heat-trace expansion yields
        # t^3 Z_0(t) = (1/60)[1 + 5t + 12t^2 + ... + (137/11)t^5 + ...].
        ax.text(
            0.02, 0.02,
            r'$r_5 = 137/11 = N_{\max}/c_2$  (zonal coeff)',
            transform=ax.transAxes, fontsize=8, color=GREEN,
            ha='left', va='bottom', alpha=0.8,
        )

    # ─────────────────────────────────────────────────────────────
    #  PANEL 4: Seeley-DeWitt -> Chern
    # ─────────────────────────────────────────────────────────────

    def _panel_seeley_chern(self, ax):
        ax.set_title(r'Seeley-DeWitt $\longleftrightarrow$ Chern', color=GOLD,
                     fontsize=12, fontweight='bold', pad=8)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])

        # Header
        ax.text(0.50, 0.95, 'Chern classes  \u2192  Curvature  \u2192  '
                'Seeley-DeWitt  \u2192  \u03b6\u0394 poles  \u2192  Selberg  \u2192  \u03b6(s)',
                color=WHITE, fontsize=7.5, ha='center', va='top', fontweight='bold')

        # Chain lines
        lines = [
            (r'$c_0 = 1$',    r'$a_0 = 1$',              r'Res$(s\!=\!5)$',  CYAN,    0.82),
            (r'$c_1 = 5$',    r'$a_1 = 2c_1^2/3 = 50/3$', r'Res$(s\!=\!4)$',  GOLD,    0.68),
            (r'$c_2 = 11$',   r'$a_2 = f(c_1^2, c_2)$',  r'Res$(s\!=\!3)$',  CORAL,   0.54),
            (r'$c_3 = 13$',   r'$a_3$',                   r'Res$(s\!=\!2)$',  GREEN,   0.40),
            (r'$c_4 = 9$',    r'$a_4$',                   r'Res$(s\!=\!1)$',  WHITE,   0.26),
        ]

        for chern_txt, sdw_txt, res_txt, color, y in lines:
            bold = (color == CORAL)
            weight = 'bold' if bold else 'normal'
            sz = 11 if bold else 10

            ax.text(0.05, y, chern_txt, color=color, fontsize=sz,
                    fontweight=weight, va='center')
            ax.text(0.28, y, r'$\rightarrow$', color=DIM, fontsize=10,
                    va='center', ha='center')
            ax.text(0.35, y, sdw_txt, color=color, fontsize=sz,
                    fontweight=weight, va='center')
            ax.text(0.72, y, r'$\rightarrow$', color=DIM, fontsize=10,
                    va='center', ha='center')
            ax.text(0.78, y, res_txt, color=color, fontsize=sz,
                    fontweight=weight, va='center')

        # Highlight KEY
        ax.text(0.95, 0.54, r'$\longleftarrow$ KEY',
                color=CORAL, fontsize=10, fontweight='bold',
                va='center', ha='right')

        # Bottom note
        ax.text(0.50, 0.10,
                r'Sign alternation: $a_k(D_{IV}^5) = (-1)^k\, a_k(Q^5)$',
                color=MAGENTA, fontsize=9, ha='center', va='center',
                style='italic')
        ax.text(0.50, 0.02,
                r'$c_5 = 3 = N_c$  (Euler class gives color number)',
                color=DIM, fontsize=8, ha='center', va='center')

    # ─────────────────────────────────────────────────────────────
    #  PANEL 5: Convergent Values
    # ─────────────────────────────────────────────────────────────

    def _panel_convergent_values(self, ax):
        ax.set_title('Convergent Values', color=GOLD,
                     fontsize=12, fontweight='bold', pad=8)

        s_ints = [4, 5, 6, 7, 8]
        z_vals = [self.zeta_int[s] for s in s_ints]
        colors = [GOLD, CYAN, GREEN, WHITE, MAGENTA]

        # Bar chart with log scale so all bars are visible
        bars = ax.bar(
            range(len(s_ints)), z_vals, color=colors,
            alpha=0.85, edgecolor=DIM, linewidth=0.8,
        )
        ax.set_xticks(range(len(s_ints)))
        ax.set_xticklabels([f's={s}' for s in s_ints], color=DIM, fontsize=9)
        ax.set_ylabel(r'$\zeta_\Delta(s)$', color=DIM, fontsize=10)
        ax.set_yscale('log')

        # Values on bars
        for i, (s, zv) in enumerate(zip(s_ints, z_vals)):
            ax.text(i, zv * 1.5, f'{zv:.6f}',
                    color=colors[i], fontsize=8, ha='center', va='bottom',
                    fontweight='bold')

        # Ratios and connections as text box
        z4, z5, z6 = self.zeta_int[4], self.zeta_int[5], self.zeta_int[6]
        ratio_45 = z4 / z5

        # Weyl-scaled values
        w4 = z4 * W_D5
        w5 = z5 * W_D5

        # Volume connection
        vol_ratio_5 = z5 / Vol_D
        vol_ratio_6 = z6 / Vol_D**2

        info = (
            f'$\\zeta_\\Delta(4)/\\zeta_\\Delta(5) = {ratio_45:.3f}$'
            rf'$\;\approx g - 1/10$' '\n'
            f'$\\zeta_\\Delta(4) \\times 1920 = {w4:.2f}$\n'
            f'$\\zeta_\\Delta(5) \\times 1920 = {w5:.3f}$\n'
            f'$\\zeta_\\Delta(5)/\\mathrm{{Vol}} = {vol_ratio_5:.5f}$\n'
            f'$\\zeta_\\Delta(6)/\\mathrm{{Vol}}^2 = {vol_ratio_6:.5f}$'
        )

        ax.text(
            0.98, 0.95, info,
            transform=ax.transAxes, fontsize=8, color=WHITE,
            va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.8),
        )

    # ─────────────────────────────────────────────────────────────
    #  PANEL 6: The Bridge
    # ─────────────────────────────────────────────────────────────

    def _panel_bridge(self, ax):
        ax.set_title('The Bridge', color=GOLD,
                     fontsize=12, fontweight='bold', pad=8)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])

        z4 = self.zeta_int[4]
        z5 = self.zeta_int[5]
        w4 = z4 * W_D5
        w5 = z5 * W_D5

        # Title
        ax.text(0.50, 0.96, 'THE SPECTRAL ZETA BRIDGE',
                color=GOLD, fontsize=13, fontweight='bold',
                ha='center', va='top',
                path_effects=[pe.withStroke(linewidth=2, foreground='#ffd700')])

        # Body text
        body_lines = [
            (r'$\zeta_\Delta(s)$ on $Q^5$:', CYAN, 0.86, 12, 'bold'),
            (r'  Poles at $s = 5, 4, 3, 2, 1$', WHITE, 0.78, 10, 'normal'),
            (r'  $s\!=\!3$ coefficient $= 1/60 = 2/5!$', CORAL, 0.70, 10, 'bold'),
            (r'  $60 = |A_5| =$ icosahedral symmetry', GOLD, 0.62, 10, 'normal'),
            ('', WHITE, 0.56, 10, 'normal'),
            ('Convergent:', CYAN, 0.52, 12, 'bold'),
            (f'  $\\zeta_\\Delta(4) = {z4:.6f}$  ($\\times 1920 = {w4:.1f}$)',
             WHITE, 0.44, 10, 'normal'),
            (f'  $\\zeta_\\Delta(5) = {z5:.6f}$  ($\\times 1920 = {w5:.2f}$)',
             WHITE, 0.36, 10, 'normal'),
            ('', WHITE, 0.30, 10, 'normal'),
            ('The bridge:', CYAN, 0.26, 12, 'bold'),
            (r'  Chern $\rightarrow\; a_k \;\rightarrow\; \zeta_\Delta'
             r'\;\rightarrow\;$ Selberg $\;\rightarrow\; \zeta(s)$',
             GREEN, 0.17, 10, 'normal'),
        ]

        for text, color, y, size, weight in body_lines:
            if text:
                ax.text(0.06, y, text, color=color, fontsize=size,
                        fontweight=weight, va='center',
                        transform=ax.transAxes)

        # Final line — the motto
        ax.text(0.50, 0.05,
                'TOPOLOGY  \u27f6  NUMBER THEORY',
                color=GOLD, fontsize=13, fontweight='bold',
                ha='center', va='center',
                path_effects=[pe.withStroke(linewidth=2, foreground='#ffd700')],
                transform=ax.transAxes)

    # ─────────────────────────────────────────────────────────────
    #  PUBLIC INTERFACE
    # ─────────────────────────────────────────────────────────────

    def show(self):
        """Display the 6-panel visualization."""
        plt.show()


# ═══════════════════════════════════════════════════════════════════
#  CLI VERIFICATION
# ═══════════════════════════════════════════════════════════════════

def _verify():
    """Print numerical checks to the terminal."""
    print('=' * 64)
    print('  BST Toy 147 — Spectral Zeta Function of Q^5')
    print('=' * 64)
    print()

    # Multiplicity check
    print('Multiplicities d_k for k = 1..6:')
    for k in range(1, 7):
        print(f'  d_{k} = {d_k(k):>6d}   lambda_{k} = {lambda_k(k):>4d}')
    print()

    # Convergent values
    print('Convergent zeta_Delta(s):')
    for s in [3.5, 4, 5, 6, 7, 8]:
        zv = spectral_zeta(s, N=10000)
        print(f'  zeta_Delta({s}) = {zv:.12f}    (x 1920 = {zv * W_D5:.6f})')
    print()

    # 1/60 theorem
    N_test = 5000
    sums = partial_sums_s3(N_test)
    Nvals = np.arange(1, N_test + 1)
    slope, intercept = fit_1_60_slope(sums, Nvals)
    print(f'1/60 Theorem (N = {N_test}):')
    print(f'  Fitted slope     = {slope:.10f}')
    print(f'  Exact 1/60       = {1/60:.10f}')
    print(f'  Difference       = {abs(slope - 1/60):.2e}')
    print(f'  gamma_Delta      = {intercept:.6f}')
    print(f'  60 = n_C!/2 = {factorial(n_C) // 2}')
    print(f'  60 = |W(D_5)|/32 = {W_D5 // 32}')
    print()

    # Ratios
    z4 = spectral_zeta(4)
    z5 = spectral_zeta(5)
    z6 = spectral_zeta(6)
    print(f'Ratios:')
    print(f'  zeta_Delta(4)/zeta_Delta(5) = {z4/z5:.4f}  (g - 1/10 = {genus - 0.1:.1f})')
    print(f'  zeta_Delta(5)/Vol(D_IV^5)   = {z5/Vol_D:.6f}')
    print(f'  zeta_Delta(6)/Vol^2         = {z6/Vol_D**2:.6f}')
    print()

    print('Vol(D_IV^5) = pi^5/1920 =', Vol_D)
    print('|rho|^2 = 17/2 =', 17/2, ' (half-sum norm squared)')
    print()

    # Odd-Zeta Parity Theorem & Exact Closed Forms
    print('Odd-Zeta Parity Theorem:')
    print('  Anti-symmetry: f_s(-5-k) = -f_s(k)  (from (2k+5) sign flip)')
    print('  => Only ODD zeta values appear: zeta(3), zeta(5), zeta(7), ...')
    print('  => Even zeta values (zeta(2), zeta(4), ...) cancel identically')
    print()

    # Verify exact closed form for zeta_Delta(4)
    try:
        from scipy.special import zeta as riemann_zeta  # type: ignore
        z3 = float(riemann_zeta(3))
    except ImportError:
        z3 = 1.2020569031595942  # Apéry's constant
    exact_z4 = (101 / 18750) * z3 + 349 / 1875000
    numerical_z4 = spectral_zeta(4, N=50000)
    print('Exact Closed Forms:')
    print(f'  zeta_Delta(4) = (101/18750)*zeta(3) + 349/1875000')
    print(f'    Exact     = {exact_z4:.12f}')
    print(f'    Numerical = {numerical_z4:.12f}')
    print(f'    Match     = {abs(exact_z4 - numerical_z4):.2e}')
    print(f'    18750 = C_2 × n_C^{{n_C}} = 6 × 3125')
    print()

    # Harmonic number connection
    from fractions import Fraction
    h5 = sum(Fraction(1, k) for k in range(1, 6))
    print(f'Harmonic Number:')
    print(f'  H_5 = {h5} = {h5.numerator}/{h5.denominator}')
    print(f'  Numerator  = {h5.numerator} = N_max')
    print(f'  Denominator = {h5.denominator} = n_C!/2 = |A_5|')
    print()

    print('Bridge: Chern -> a_k -> zeta_Delta -> Selberg -> zeta(s)')
    print('        TOPOLOGY -> NUMBER THEORY')
    print('=' * 64)


# ═══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    _verify()
    explorer = SpectralZetaExplorer()
    plt.show()
