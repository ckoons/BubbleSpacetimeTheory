#!/usr/bin/env python3
"""
BST Toy 146 — The Spectral Multiplicity Theorem
=================================================
The eigenvalues of the Laplacian on Q⁵ = SO(7)/[SO(5)×SO(2)] are
λ_k = k(k+5) with multiplicities d_k = C(k+4,4)·(2k+5)/5.

The KEY discovery: the factor (2k+5) cycles through ALL BST/Chern integers.
The linear "spectral velocity" λ'_k = 2k+5 carries all the topology.
Chern classes build the multiplicities. Topology IS the spectrum.

    python toy_spectral_multiplicity.py

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np


# ═══════════════════════════════════════════════════════════════════
# BST SPECTRAL FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def binom(n, k):
    """Binomial coefficient C(n,k)."""
    return math.comb(n, k)


def d_k(k):
    """Multiplicity of k-th eigenvalue on Q⁵."""
    return binom(k + 4, 4) * (2 * k + 5) // 5


def lambda_k(k):
    """k-th eigenvalue of the Laplacian on Q⁵."""
    return k * (k + 5)


def lambda_prime(k):
    """Spectral velocity: derivative of λ_k."""
    return 2 * k + 5


# Verify
assert d_k(0) == 1
assert d_k(1) == 7
assert d_k(2) == 27
assert d_k(3) == 77
assert d_k(4) == 182
assert d_k(5) == 378


# ═══════════════════════════════════════════════════════════════════
# BST INTEGER REGISTRY
# ═══════════════════════════════════════════════════════════════════

# Colors for BST integers
CYAN = '#00e5ff'
GOLD = '#ffd700'
GREEN = '#00ff88'
CORAL = '#ff6b6b'
MAGENTA = '#ff00ff'
WHITE = '#ffffff'
DIM = '#666688'

# (2k+5) -> BST name, color
VELOCITY_MAP = {
    5:  ('n_C = c₁', CYAN),
    7:  ('g (genus)', GOLD),
    9:  ('c₄ = N_c²', GREEN),
    11: ('c₂ = dim K', CORAL),
    13: ('c₃ (Weinberg)', MAGENTA),
    15: ('N_c·n_C', WHITE),
    17: ('—', DIM),
    19: ('Ω_Λ denom', CYAN),
    21: ('dim SO(7)', GOLD),
    23: ('Golay n−1', GREEN),
}

# Multiplicity factorizations for display
FACTORIZATIONS = {
    1: ('7', 'g', GOLD),
    2: ('3³ = 27', 'N_c^{N_c}', GREEN),
    3: ('7 × 11 = 77', 'g × c₂', CORAL),
    4: ('2 × 7 × 13 = 182', 'r × g × c₃', MAGENTA),
    5: ('2 × 27 × 7 = 378', 'r × N_c³ × g', CYAN),
    6: ('2 × 3 × 7 × 17 = 714', '2·3·7·17', DIM),
    7: ('2 × 3 × 11 × 19 = 1254', 'c₂ × Ω_Λ', CYAN),
    8: ('27 × 7 × 11 = 2079', 'N_c³ × g × c₂', GOLD),
    9: ('11 × 13 × 23 = 3289', 'c₂ × c₃ × Golay', GREEN),
}


# ═══════════════════════════════════════════════════════════════════
# VISUALIZATION
# ═══════════════════════════════════════════════════════════════════

class SpectralMultiplicityExplorer:
    """BST Toy 146 — The Spectral Multiplicity Theorem.

    Visualizes the eigenvalue spectrum of the Laplacian on Q⁵ and
    reveals how the Chern integers of BST are encoded in the
    spectral velocity factor (2k+5).
    """

    def __init__(self):
        self.fig = plt.figure(figsize=(20, 13), facecolor='#0a0a1a')
        self.axes = []

        # 6-panel layout: 3 columns × 2 rows
        # Margins and gaps
        ml, mr, mb, mt = 0.04, 0.02, 0.07, 0.08
        hgap, vgap = 0.04, 0.07
        pw = (1.0 - ml - mr - 2 * hgap) / 3
        ph = (1.0 - mb - mt - vgap) / 2

        positions = []
        for row in range(2):
            for col in range(3):
                l = ml + col * (pw + hgap)
                b = mb + (1 - row) * (ph + vgap)
                positions.append([l, b, pw, ph])

        for pos in positions:
            ax = self.fig.add_axes(pos, facecolor='#0a0a1a')
            ax.tick_params(colors='#888899', labelcolor='#aaaacc', labelsize=8)
            for spine in ax.spines.values():
                spine.set_color('#333355')
            self.axes.append(ax)

        # Title
        self.fig.text(
            0.5, 0.97,
            'The Spectral Multiplicity Theorem',
            ha='center', va='top', fontsize=22, fontweight='bold',
            color=GOLD,
            path_effects=[pe.withStroke(linewidth=3, foreground='#ffd700')],
        )
        self.fig.text(
            0.5, 0.935,
            'Eigenvalues of the Laplacian on Q⁵ = SO(7)/[SO(5)×SO(2)]',
            ha='center', va='top', fontsize=12, color='#8888aa',
        )

        # Copyright
        self.fig.text(
            0.5, 0.015,
            '© 2026 Casey Koons | BST Toy 146 — The Spectral Multiplicity Theorem',
            ha='center', va='bottom', fontsize=9, color='#555577',
        )

        self._panel1_formula_table()
        self._panel2_spectral_velocity()
        self._panel3_factorizations()
        self._panel4_sequence()
        self._panel5_growth()
        self._panel6_theorem()

        self.fig.canvas.manager.set_window_title(
            'BST Toy 146 — The Spectral Multiplicity Theorem'
        )

    # ───────────────────────────────────────────────────────────
    # Panel 1: The Multiplicity Formula
    # ───────────────────────────────────────────────────────────
    def _panel1_formula_table(self):
        ax = self.axes[0]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.set_title('The Multiplicity Formula', color=CYAN, fontsize=12,
                      fontweight='bold', pad=8)

        # Formula
        ax.text(0.5, 0.95,
                r'$d_k = \binom{k+4}{4} \cdot \frac{2k+5}{5}$',
                ha='center', va='top', fontsize=14, color=GOLD,
                transform=ax.transAxes)

        # Table header
        y0 = 0.84
        dy = 0.073
        cols = [0.06, 0.18, 0.33, 0.60, 0.87]
        headers = ['k', 'λ_k', '2k+5', 'BST name', 'd_k']
        for x, h in zip(cols, headers):
            ax.text(x, y0, h, ha='left', va='top', fontsize=9,
                    color='#8888aa', fontweight='bold', transform=ax.transAxes)

        # Separator line
        ax.plot([0.02, 0.98], [y0 - 0.025, y0 - 0.025],
                color='#333355', lw=0.8, transform=ax.transAxes)

        # Color map for k -> color
        k_colors = {
            0: CYAN, 1: GOLD, 2: GREEN, 3: CORAL, 4: MAGENTA,
            5: WHITE, 6: DIM, 7: CYAN, 8: GOLD, 9: GREEN,
        }

        for k in range(10):
            y = y0 - 0.04 - k * dy
            lk = lambda_k(k)
            vel = 2 * k + 5
            dk = d_k(k)
            name, color = VELOCITY_MAP[vel]
            c = k_colors.get(k, WHITE)

            ax.text(cols[0], y, str(k), ha='left', va='top', fontsize=9,
                    color=c, transform=ax.transAxes)
            ax.text(cols[1], y, str(lk), ha='left', va='top', fontsize=9,
                    color=c, transform=ax.transAxes)
            ax.text(cols[2], y, str(vel), ha='left', va='top', fontsize=9,
                    color=c, fontweight='bold', transform=ax.transAxes)
            ax.text(cols[3], y, name, ha='left', va='top', fontsize=8,
                    color=color, transform=ax.transAxes)
            ax.text(cols[4], y, str(dk), ha='left', va='top', fontsize=9,
                    color=c, transform=ax.transAxes)

    # ───────────────────────────────────────────────────────────
    # Panel 2: Spectral Velocity = Topology
    # ───────────────────────────────────────────────────────────
    def _panel2_spectral_velocity(self):
        ax = self.axes[1]
        ax.set_title('Spectral Velocity = Topology', color=CYAN, fontsize=12,
                      fontweight='bold', pad=8)

        ks = np.arange(0, 16)
        lambdas = [lambda_k(k) for k in ks]
        velocities = [lambda_prime(k) for k in ks]

        # Twin axis for eigenvalues (left) and velocity (right)
        ax2 = ax.twinx()
        ax2.set_facecolor('#0a0a1a')

        # Eigenvalues
        ax.plot(ks, lambdas, 'o-', color=CYAN, markersize=4, lw=1.5,
                alpha=0.8, label='λ_k = k(k+5)')
        ax.set_ylabel('λ_k (eigenvalue)', color=CYAN, fontsize=9)
        ax.tick_params(axis='y', colors=CYAN, labelsize=8)

        # Spectral velocity
        ax2.plot(ks, velocities, 's-', color=GOLD, markersize=5, lw=2,
                 alpha=0.9, label="λ'_k = 2k+5")
        ax2.set_ylabel("λ'_k (spectral velocity)", color=GOLD, fontsize=9)
        ax2.tick_params(axis='y', colors=GOLD, labelsize=8)
        for spine in ax2.spines.values():
            spine.set_color('#333355')

        # Mark Chern integers on velocity curve
        chern_ks = {0: CYAN, 1: GOLD, 2: GREEN, 3: CORAL, 4: MAGENTA}
        for k_val, color in chern_ks.items():
            vel = lambda_prime(k_val)
            ax2.plot(k_val, vel, 'o', color=color, markersize=12,
                     markeredgecolor=WHITE, markeredgewidth=1.5, zorder=5)
            name = VELOCITY_MAP[vel][0].split('=')[0].strip() if '=' in VELOCITY_MAP[vel][0] else VELOCITY_MAP[vel][0]
            ax2.annotate(f'{vel}', (k_val, vel),
                         textcoords='offset points', xytext=(8, 6),
                         fontsize=8, color=color, fontweight='bold')

        ax.set_xlabel('k', color='#aaaacc', fontsize=9)
        ax.set_xlim(-0.5, 15.5)

        # Annotation
        ax.text(0.5, 0.02,
                r"$d_k = \binom{k+4}{4} \cdot \lambda'_k \,/\, n_C$",
                ha='center', va='bottom', fontsize=10, color=GOLD,
                transform=ax.transAxes,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a2e',
                          edgecolor=GOLD, alpha=0.8))

        ax.tick_params(colors='#888899', labelsize=8)

    # ───────────────────────────────────────────────────────────
    # Panel 3: BST Factorizations
    # ───────────────────────────────────────────────────────────
    def _panel3_factorizations(self):
        ax = self.axes[2]
        ax.set_title('BST Factorizations', color=CYAN, fontsize=12,
                      fontweight='bold', pad=8)

        ks_show = [1, 2, 3, 4, 5, 7, 8, 9]
        y_positions = list(range(len(ks_show)))

        for i, k in enumerate(ks_show):
            dk = d_k(k)
            fact_str, bst_str, color = FACTORIZATIONS[k]

            # Horizontal bar proportional to log(d_k)
            bar_len = np.log10(dk + 1) / np.log10(4000)
            ax.barh(i, bar_len, height=0.6, color=color, alpha=0.35,
                    edgecolor=color, linewidth=1)

            # Label: d_k value
            ax.text(-0.02, i, f'd_{k}', ha='right', va='center',
                    fontsize=9, color=color, fontweight='bold')

            # Factorization text inside bar
            ax.text(bar_len + 0.02, i + 0.05, fact_str,
                    ha='left', va='center', fontsize=8, color=WHITE)
            ax.text(bar_len + 0.02, i - 0.25, bst_str,
                    ha='left', va='center', fontsize=7, color=color,
                    fontstyle='italic')

        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_xlim(-0.15, 1.5)
        ax.set_ylim(-0.7, len(ks_show) - 0.3)
        ax.invert_yaxis()

    # ───────────────────────────────────────────────────────────
    # Panel 4: The (2k+5) Sequence
    # ───────────────────────────────────────────────────────────
    def _panel4_sequence(self):
        ax = self.axes[3]
        ax.set_title('The (2k+5) Sequence', color=CYAN, fontsize=12,
                      fontweight='bold', pad=8)
        ax.set_xlim(-0.5, 9.5)
        ax.set_ylim(-0.5, 1.5)
        ax.axis('off')

        vals = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
        k_vals = list(range(10))

        for i, (k, v) in enumerate(zip(k_vals, vals)):
            name, color = VELOCITY_MAP[v]

            # Circle for each integer
            circle = plt.Circle((i, 0.7), 0.35, facecolor='#0a0a1a',
                                edgecolor=color, linewidth=2.5,
                                transform=ax.transData)
            ax.add_patch(circle)

            # Value inside circle
            ax.text(i, 0.7, str(v), ha='center', va='center',
                    fontsize=14, fontweight='bold', color=color)

            # k label below
            ax.text(i, 0.2, f'k={k}', ha='center', va='top',
                    fontsize=7, color='#666688')

            # BST name below that
            short_name = name.split('=')[0].strip() if '=' in name else name.split('(')[0].strip()
            ax.text(i, 0.0, short_name, ha='center', va='top',
                    fontsize=6.5, color=color, fontstyle='italic')

        # Connecting line
        ax.plot([-0.2, 9.2], [0.7, 0.7], color='#333355', lw=1,
                zorder=0, ls='--')

        # Bracket over first 5 (Chern integers)
        ax.annotate('', xy=(-0.3, 1.2), xytext=(4.3, 1.2),
                    arrowprops=dict(arrowstyle='-', color=GOLD, lw=1.5))
        ax.plot([-0.3, -0.3], [1.15, 1.2], color=GOLD, lw=1.5)
        ax.plot([4.3, 4.3], [1.15, 1.2], color=GOLD, lw=1.5)
        ax.text(2.0, 1.35, 'ALL Chern integers of Q⁵ appear\nin the first 5 values',
                ha='center', va='center', fontsize=8, color=GOLD,
                fontweight='bold')

    # ───────────────────────────────────────────────────────────
    # Panel 5: Multiplicity Growth
    # ───────────────────────────────────────────────────────────
    def _panel5_growth(self):
        ax = self.axes[4]
        ax.set_title('Multiplicity Growth', color=CYAN, fontsize=12,
                      fontweight='bold', pad=8)

        ks = np.arange(1, 31)
        dks = [d_k(k) for k in ks]
        asymptote = [k**5 / 60 for k in ks]

        ax.semilogy(ks, dks, 'o-', color=CYAN, markersize=4, lw=1.5,
                    label=r'$d_k$ (exact)')
        ax.semilogy(ks, asymptote, '--', color=GOLD, lw=1, alpha=0.7,
                    label=r'$k^5/60$ (asymptote)')

        # Special levels
        specials = {
            1: ('proton\n7 modes\n(Hamming)', GOLD),
            2: ('strange\n27 = N_c^{N_c}', GREEN),
            3: ('Golay\nλ₃ = 24', CORAL),
            4: ('Weinberg\nλ₄ = 36 = C₂²', MAGENTA),
        }
        for k_val, (label, color) in specials.items():
            dk_val = d_k(k_val)
            ax.plot(k_val, dk_val, 'o', color=color, markersize=10,
                    markeredgecolor=WHITE, markeredgewidth=1.2, zorder=5)
            # Offset annotations to avoid overlap
            offsets = {1: (12, 8), 2: (12, -5), 3: (12, -10), 4: (12, 5)}
            ox, oy = offsets[k_val]
            ax.annotate(label, (k_val, dk_val),
                        textcoords='offset points', xytext=(ox, oy),
                        fontsize=6.5, color=color,
                        arrowprops=dict(arrowstyle='->', color=color,
                                        lw=0.8))

        ax.set_xlabel('k', color='#aaaacc', fontsize=9)
        ax.set_ylabel('d_k', color='#aaaacc', fontsize=9)
        ax.legend(fontsize=8, loc='lower right',
                  facecolor='#1a1a2e', edgecolor='#333355',
                  labelcolor='#aaaacc')
        ax.set_xlim(0, 31)

    # ───────────────────────────────────────────────────────────
    # Panel 6: The Theorem
    # ───────────────────────────────────────────────────────────
    def _panel6_theorem(self):
        ax = self.axes[5]
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        ax.set_title('The Theorem', color=CYAN, fontsize=12,
                      fontweight='bold', pad=8)

        # Theorem box
        box_props = dict(boxstyle='round,pad=0.4', facecolor='#12122a',
                         edgecolor=GOLD, linewidth=1.5)

        # THEOREM header
        y = 0.93
        ax.text(0.5, y, 'THEOREM', ha='center', va='top', fontsize=14,
                fontweight='bold', color=GOLD, transform=ax.transAxes)

        y -= 0.10
        ax.text(0.5, y,
                r'$d_k = \binom{k+4}{4} \cdot \frac{2k + n_C}{n_C}$',
                ha='center', va='top', fontsize=13, color=GOLD,
                transform=ax.transAxes)

        y -= 0.10
        ax.text(0.5, y, 'The factor (2k + n_C):', ha='center', va='top',
                fontsize=10, color='#aaaacc', transform=ax.transAxes)

        # Chern integer list
        lines = [
            ('k=0:  n_C = 5', 'dimension', CYAN),
            ('k=1:  g = 7', 'genus / Mersenne', GOLD),
            ('k=2:  c₄ = 9', 'cosmology', GREEN),
            ('k=3:  c₂ = 11', 'isotropy', CORAL),
            ('k=4:  c₃ = 13', 'Weinberg', MAGENTA),
        ]
        y -= 0.06
        for text, role, color in lines:
            y -= 0.075
            ax.text(0.2, y, text, ha='left', va='top', fontsize=10,
                    color=color, fontfamily='monospace', transform=ax.transAxes)
            ax.text(0.72, y, f'({role})', ha='left', va='top', fontsize=9,
                    color=color, fontstyle='italic', transform=ax.transAxes,
                    alpha=0.7)

        # Separator
        y -= 0.06
        ax.plot([0.1, 0.9], [y, y], color='#333355', lw=1,
                transform=ax.transAxes)

        # Punchline
        y -= 0.08
        ax.text(0.5, y, 'TOPOLOGY IS THE SPECTRUM',
                ha='center', va='top', fontsize=14, fontweight='bold',
                color=CYAN, transform=ax.transAxes,
                path_effects=[pe.withStroke(linewidth=2, foreground='#004466')])

        y -= 0.08
        ax.text(0.5, y, 'Chern classes build the multiplicities',
                ha='center', va='top', fontsize=10, color=WHITE,
                transform=ax.transAxes, fontstyle='italic')


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    explorer = SpectralMultiplicityExplorer()
    plt.show()
