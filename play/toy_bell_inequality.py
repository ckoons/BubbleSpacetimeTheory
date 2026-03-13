#!/usr/bin/env python3
"""
BELL INEQUALITY VIOLATIONS & THE TSIRELSON BOUND
=================================================
Why does nature violate Bell inequalities? BST answers:
  Because space is 3-dimensional.

The CHSH inequality: |S| <= 2 for any local hidden variable theory.
Quantum mechanics achieves: |S| = 2*sqrt(2) (the Tsirelson bound).
No-signaling theories allow up to: |S| = 4.

BST derivation chain:
  n_C = 5  -->  S^4 boundary  -->  3D space  -->  SO(3)
  -->  SU(2) = Spin(3)  -->  spin-1/2  -->  binary measurements  -->  2*sqrt(2)

Key insight: Bell violations REQUIRE 3 spatial dimensions.
In 1D or 2D, rotation groups are trivial/abelian -- no spinors, no violation.
The weak force SU(2) = Spin(3) = the spin group of 3D space.

Entanglement in BST: a SHARED COMMITMENT -- one record with two endpoints.
Not two separate records (classical). Not action at a distance.
The holomorphic structure of D_IV^5 prevents factorization.

The Tsirelson bound: 2*sqrt(2) = 2*sqrt(N_w) where N_w = 2 = dim(weak doublet).

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
from matplotlib.widgets import Slider
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity
N_w = 2           # dim of weak doublet
genus = n_C + 2   # = 7
CLASSICAL_BOUND = 2.0
TSIRELSON_BOUND = 2.0 * np.sqrt(2.0)
ALGEBRAIC_BOUND = 4.0

# ─── Visual constants ───
BG = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
GOLD_TRANS = '#ffd70030'
CYAN = '#00ddff'
PURPLE = '#9966ff'
GREEN = '#44ff88'
ORANGE = '#ff8800'
RED = '#ff4444'
WHITE = '#ffffff'
GREY = '#888888'
DGREY = '#444444'
DEEP_BLUE = '#2266ff'
LIGHT_BLUE = '#5599ff'
ALICE_COLOR = '#ff6688'
BOB_COLOR = '#66aaff'
COMMIT_GOLD = '#ffcc44'


# ═══════════════════════════════════════════════════════════════════
#  BST BELL INEQUALITY MODEL
# ═══════════════════════════════════════════════════════════════════

class BellInequality:
    """
    Bell inequality / CHSH / Tsirelson bound calculator with BST interpretation.

    Provides both numerical computation and BST conceptual explanations.
    Designed for programmatic (CI-scriptable) use as well as GUI visualization.
    """

    def __init__(self):
        self.n_C = n_C
        self.N_c = N_c
        self.N_max = N_max
        self.N_w = N_w

    # ─── Core Physics ───

    def correlation(self, theta: float) -> float:
        """
        Quantum singlet correlation function.
        E(a, b) = -cos(theta) where theta = angle between a and b.

        Parameters
        ----------
        theta : float
            Angle in radians between measurement directions.

        Returns
        -------
        float
            Correlation value in [-1, +1].
        """
        return -np.cos(theta)

    def chsh(self, a: float, a_prime: float, b: float, b_prime: float) -> float:
        """
        Compute the CHSH correlator S for given measurement angles (in degrees).

        S = E(a,b) - E(a,b') + E(a',b) + E(a',b')

        Parameters
        ----------
        a, a_prime : float
            Alice's two measurement angles in degrees.
        b, b_prime : float
            Bob's two measurement angles in degrees.

        Returns
        -------
        float
            The CHSH correlator S.
        """
        a_r = np.radians(a)
        ap_r = np.radians(a_prime)
        b_r = np.radians(b)
        bp_r = np.radians(b_prime)

        E_ab = self.correlation(a_r - b_r)
        E_abp = self.correlation(a_r - bp_r)
        E_apb = self.correlation(ap_r - b_r)
        E_apbp = self.correlation(ap_r - bp_r)

        return E_ab - E_abp + E_apb + E_apbp

    def optimal_angles(self) -> dict:
        """
        Return the optimal CHSH angles that maximize |S|.

        The optimal configuration: a=0, a'=90, b=45, b'=135 (or -45).
        Achieves S = 2*sqrt(2).

        Returns
        -------
        dict
            Keys: 'a', 'a_prime', 'b', 'b_prime', 'S', 'S_theory'.
        """
        a, ap, b, bp = 0.0, 90.0, 45.0, 135.0
        S = self.chsh(a, ap, b, bp)
        return {
            'a': a,
            'a_prime': ap,
            'b': b,
            'b_prime': bp,
            'S': S,
            'S_abs': abs(S),
            'S_theory': TSIRELSON_BOUND,
        }

    def sweep_angles(self, n: int = 200) -> dict:
        """
        Sweep Bob's angle b with a=0, a'=90, b'=b+90 and compute S(b).

        Parameters
        ----------
        n : int
            Number of sample points.

        Returns
        -------
        dict
            Keys: 'b_deg' (array), 'S' (array), 'S_max', 'b_max_deg'.
        """
        b_deg = np.linspace(0, 180, n)
        S_vals = np.array([
            self.chsh(0.0, 90.0, b, b + 90.0) for b in b_deg
        ])
        idx_max = np.argmax(np.abs(S_vals))
        return {
            'b_deg': b_deg,
            'S': S_vals,
            'S_max': S_vals[idx_max],
            'b_max_deg': b_deg[idx_max],
        }

    def sweep_custom(self, a: float, a_prime: float,
                     b_offset: float = 90.0, n: int = 200) -> dict:
        """
        Sweep b from 0..180 with given a, a', and b' = b + b_offset.

        Returns
        -------
        dict
            Keys: 'b_deg', 'S', 'S_max', 'b_max_deg'.
        """
        b_deg = np.linspace(0, 180, n)
        S_vals = np.array([
            self.chsh(a, a_prime, b, b + b_offset) for b in b_deg
        ])
        idx_max = np.argmax(np.abs(S_vals))
        return {
            'b_deg': b_deg,
            'S': S_vals,
            'S_max': S_vals[idx_max],
            'b_max_deg': b_deg[idx_max],
        }

    # ─── Bounds ───

    def classical_bound(self) -> float:
        """The Bell/CHSH classical bound: |S| <= 2."""
        return CLASSICAL_BOUND

    def tsirelson_bound(self) -> float:
        """The Tsirelson bound: |S| <= 2*sqrt(2) for quantum mechanics."""
        return TSIRELSON_BOUND

    def algebraic_bound(self) -> float:
        """The algebraic/no-signaling bound: |S| <= 4."""
        return ALGEBRAIC_BOUND

    # ─── BST Interpretations ───

    def bst_chain(self) -> list:
        """
        The BST derivation chain explaining WHY Bell violations exist.

        Returns
        -------
        list of str
            Each step in the chain from geometry to the Tsirelson bound.
        """
        return [
            f"n_C = {self.n_C} (complex dim of D_IV^5)",
            "S^4 boundary (Shilov boundary of D_IV^5)",
            "3D spatial sections (S^4 = susp(S^3), S^3 ~ R^3 locally)",
            "SO(3) rotation group of 3D space",
            "SU(2) = Spin(3) (universal double cover)",
            "spin-1/2 particles (fundamental rep of SU(2))",
            "binary measurement outcomes (+1 or -1)",
            f"Tsirelson bound = 2*sqrt({self.N_w}) = 2*sqrt(2) = {TSIRELSON_BOUND:.4f}",
        ]

    def why_3d(self) -> str:
        """
        Explain why Bell violations require exactly 3 spatial dimensions.

        Returns
        -------
        str
            Multi-line explanation.
        """
        return (
            "Bell violations REQUIRE 3 spatial dimensions.\n"
            "\n"
            "1D: The rotation group SO(1) is trivial -- no nontrivial spinors.\n"
            "    Measurements are collinear. No Bell violation possible.\n"
            "\n"
            "2D: SO(2) is abelian (just rotations in a plane).\n"
            "    Spin(2) = U(1), one-dimensional reps only.\n"
            "    All observables commute -- no complementarity, no violation.\n"
            "\n"
            "3D: SO(3) is NON-ABELIAN. Spin(3) = SU(2).\n"
            "    The 2D fundamental rep of SU(2) gives spin-1/2.\n"
            "    Non-commuting measurements --> complementarity --> violation.\n"
            "\n"
            "BST: n_C = 5 --> S^4 = Shilov boundary --> 3D spatial sections.\n"
            "    The dimension of space is not arbitrary -- it follows from\n"
            "    the geometry of D_IV^5. Bell violations are inevitable."
        )

    def entanglement_description(self) -> dict:
        """
        BST view of entanglement as shared commitment.

        Returns
        -------
        dict
            Keys: 'bst_view', 'classical_view', 'action_at_distance',
                  'no_cloning', 'tsirelson_explanation'.
        """
        return {
            'bst_view': (
                "Entanglement is a SHARED COMMITMENT: one holomorphic record\n"
                "in the Bergman space A^2(D_IV^5) with two boundary endpoints.\n"
                "Written at pair creation. Read at measurement."
            ),
            'classical_view': (
                "Classical model: two separate records, one per particle.\n"
                "This factorizes --> satisfies Bell --> |S| <= 2.\n"
                "WRONG: Nature violates this."
            ),
            'action_at_distance': (
                "NOT action at a distance. The commitment is written locally\n"
                "at pair creation. No information travels at measurement.\n"
                "Correlations are pre-committed, not transmitted."
            ),
            'no_cloning': (
                "No-cloning theorem: It is ONE commitment, not two copies.\n"
                "You cannot duplicate a holomorphic function on D_IV^5\n"
                "without destroying the original. The Bergman kernel\n"
                "reproduces but does not clone."
            ),
            'tsirelson_explanation': (
                f"2*sqrt(2) = 2*sqrt(N_w) where N_w = {self.N_w}\n"
                "N_w = dimension of the weak (SU(2)) doublet.\n"
                "The sqrt(2) comes from the 2D spin-1/2 Hilbert space.\n"
                "Holomorphic structure prevents factorization --> violation."
            ),
        }


# ═══════════════════════════════════════════════════════════════════
#  VISUALIZATION HELPERS
# ═══════════════════════════════════════════════════════════════════

def _draw_rounded_box(ax, x, y, w, h, text, color, fontsize=10,
                      text_color=WHITE, edge_color=None, alpha=0.9):
    """Draw a rounded rectangle with centered text."""
    ec = edge_color or color
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.02",
        facecolor=color, edgecolor=ec, linewidth=1.5, alpha=alpha,
        transform=ax.transData, zorder=3,
    )
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=text_color,
            ha='center', va='center', fontfamily='monospace',
            fontweight='bold', zorder=4)


def _draw_arrow_down(ax, x, y1, y2, color=GOLD_DIM):
    """Draw a downward arrow between two y positions."""
    ax.annotate('', xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=2, shrinkA=2, shrinkB=2),
                zorder=2)


# ═══════════════════════════════════════════════════════════════════
#  MAIN VISUALIZATION
# ═══════════════════════════════════════════════════════════════════

def build_gui():
    """Build and display the Bell inequality visualization."""

    model = BellInequality()

    # ─── Figure Setup ───
    fig = plt.figure(figsize=(18, 11), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'Bell Inequality Violations & Tsirelson Bound — BST')

    fig.text(0.5, 0.97, 'BELL INEQUALITY VIOLATIONS & THE TSIRELSON BOUND',
             fontsize=22, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
    fig.text(0.5, 0.945,
             'Why nature violates classical bounds — and stops at 2\u221a2',
             fontsize=12, color=GOLD_DIM, ha='center', fontfamily='monospace')

    # Bottom strip
    fig.text(0.5, 0.015,
             'Bell violations exist because space is 3-dimensional. '
             'The bound is 2\u221a2 because states are holomorphic.',
             fontsize=11, color=GOLD, ha='center', fontfamily='monospace',
             style='italic',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                       edgecolor=GOLD_DIM, linewidth=1))

    # ═══════════════════════════════════════════════════════════════
    #  PANEL 1: CHSH CORRELATOR (Left)
    # ═══════════════════════════════════════════════════════════════
    ax_chsh = fig.add_axes([0.05, 0.15, 0.28, 0.55], facecolor=DARK_PANEL)
    ax_chsh.set_title('THE CHSH CORRELATOR', fontsize=13, fontweight='bold',
                      color=CYAN, fontfamily='monospace', pad=10)

    # Initial sweep
    a_init = 0.0
    ap_init = 90.0
    bb_offset_init = 90.0
    sweep = model.sweep_custom(a_init, ap_init, bb_offset_init, n=300)
    b_deg = sweep['b_deg']
    S_vals = sweep['S']

    # The quantum curve
    line_S, = ax_chsh.plot(b_deg, S_vals, color=DEEP_BLUE, linewidth=2.5,
                           zorder=5, label='S(b)')

    # Violation zone shading
    fill_upper = ax_chsh.fill_between(
        b_deg, CLASSICAL_BOUND, np.clip(S_vals, CLASSICAL_BOUND, TSIRELSON_BOUND),
        where=(S_vals > CLASSICAL_BOUND),
        color=GOLD_TRANS, alpha=0.35, zorder=2, label='Violation zone')

    # Bound lines
    ax_chsh.axhline(y=CLASSICAL_BOUND, color=RED, linestyle='--', linewidth=1.5,
                    alpha=0.8, zorder=3, label=f'Classical |S|={CLASSICAL_BOUND}')
    ax_chsh.axhline(y=-CLASSICAL_BOUND, color=RED, linestyle='--', linewidth=1.5,
                    alpha=0.8, zorder=3)
    ax_chsh.axhline(y=TSIRELSON_BOUND, color=GOLD, linestyle='-', linewidth=2,
                    alpha=0.9, zorder=3,
                    label=f'Tsirelson |S|=2\u221a2\u2248{TSIRELSON_BOUND:.3f}')
    ax_chsh.axhline(y=-TSIRELSON_BOUND, color=GOLD, linestyle='-', linewidth=2,
                    alpha=0.9, zorder=3)
    ax_chsh.axhline(y=ALGEBRAIC_BOUND, color=GREY, linestyle=':', linewidth=1.2,
                    alpha=0.6, zorder=3, label=f'No-signaling |S|={ALGEBRAIC_BOUND}')
    ax_chsh.axhline(y=-ALGEBRAIC_BOUND, color=GREY, linestyle=':', linewidth=1.2,
                    alpha=0.6, zorder=3)
    ax_chsh.axhline(y=0, color=DGREY, linestyle='-', linewidth=0.5, zorder=1)

    # Labels on right edge
    ax_chsh.text(182, CLASSICAL_BOUND, '2', fontsize=10, color=RED,
                 va='center', fontfamily='monospace', fontweight='bold')
    ax_chsh.text(182, TSIRELSON_BOUND, '2\u221a2', fontsize=10, color=GOLD,
                 va='center', fontfamily='monospace', fontweight='bold')
    ax_chsh.text(182, ALGEBRAIC_BOUND, '4', fontsize=10, color=GREY,
                 va='center', fontfamily='monospace', fontweight='bold')

    # Peak marker
    peak_idx = np.argmax(S_vals)
    peak_dot, = ax_chsh.plot(b_deg[peak_idx], S_vals[peak_idx], 'o',
                             color=GOLD, markersize=8, zorder=6)
    peak_text = ax_chsh.text(
        b_deg[peak_idx] + 5, S_vals[peak_idx] + 0.15,
        f'S = {S_vals[peak_idx]:.4f}\nb = {b_deg[peak_idx]:.1f}\u00b0',
        fontsize=9, color=GOLD, fontfamily='monospace', zorder=6)

    ax_chsh.set_xlim(0, 180)
    ax_chsh.set_ylim(-4.5, 4.5)
    ax_chsh.set_xlabel("Bob's angle b (\u00b0)", fontsize=10, color=GREY,
                       fontfamily='monospace')
    ax_chsh.set_ylabel('CHSH correlator S', fontsize=10, color=GREY,
                       fontfamily='monospace')
    ax_chsh.tick_params(colors=GREY, labelsize=9)
    for spine in ax_chsh.spines.values():
        spine.set_color(DGREY)
    ax_chsh.legend(loc='lower right', fontsize=7, facecolor=DARK_PANEL,
                   edgecolor=DGREY, labelcolor=GREY)

    # Config text
    config_text = ax_chsh.text(
        0.02, 0.98,
        f"a = {a_init:.0f}\u00b0, a' = {ap_init:.0f}\u00b0\n"
        f"b' = b + {bb_offset_init:.0f}\u00b0",
        transform=ax_chsh.transAxes, fontsize=9, color=CYAN,
        fontfamily='monospace', va='top', ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DGREY))

    # ─── Sliders ───
    ax_slider_ap = fig.add_axes([0.05, 0.09, 0.28, 0.02], facecolor=DARK_PANEL)
    slider_ap = Slider(ax_slider_ap, "a' (\u00b0)", 0, 180, valinit=ap_init,
                       valstep=1, color=CYAN)
    slider_ap.label.set_color(CYAN)
    slider_ap.label.set_fontfamily('monospace')
    slider_ap.label.set_fontsize(9)
    slider_ap.valtext.set_color(CYAN)
    slider_ap.valtext.set_fontfamily('monospace')

    ax_slider_offset = fig.add_axes([0.05, 0.055, 0.28, 0.02], facecolor=DARK_PANEL)
    slider_offset = Slider(ax_slider_offset, "b'-b (\u00b0)", 0, 180,
                           valinit=bb_offset_init, valstep=1, color=GOLD_DIM)
    slider_offset.label.set_color(GOLD_DIM)
    slider_offset.label.set_fontfamily('monospace')
    slider_offset.label.set_fontsize(9)
    slider_offset.valtext.set_color(GOLD_DIM)
    slider_offset.valtext.set_fontfamily('monospace')

    def update_chsh(val):
        ap = slider_ap.val
        offset = slider_offset.val
        sweep_new = model.sweep_custom(a_init, ap, offset, n=300)
        S_new = sweep_new['S']
        line_S.set_ydata(S_new)

        # Update fill
        nonlocal fill_upper
        fill_upper.remove()
        fill_upper = ax_chsh.fill_between(
            b_deg, CLASSICAL_BOUND,
            np.clip(S_new, CLASSICAL_BOUND, TSIRELSON_BOUND),
            where=(S_new > CLASSICAL_BOUND),
            color=GOLD_TRANS, alpha=0.35, zorder=2)

        # Update peak
        pidx = np.argmax(S_new)
        peak_dot.set_data([b_deg[pidx]], [S_new[pidx]])
        peak_text.set_position((b_deg[pidx] + 5, S_new[pidx] + 0.15))
        peak_text.set_text(
            f'S = {S_new[pidx]:.4f}\nb = {b_deg[pidx]:.1f}\u00b0')

        config_text.set_text(
            f"a = {a_init:.0f}\u00b0, a' = {ap:.0f}\u00b0\n"
            f"b' = b + {offset:.0f}\u00b0")

        fig.canvas.draw_idle()

    slider_ap.on_changed(update_chsh)
    slider_offset.on_changed(update_chsh)

    # ═══════════════════════════════════════════════════════════════
    #  PANEL 2: THE BST CHAIN (Center)
    # ═══════════════════════════════════════════════════════════════
    ax_chain = fig.add_axes([0.37, 0.06, 0.26, 0.82], facecolor=BG)
    ax_chain.axis('off')
    ax_chain.set_xlim(0, 1)
    ax_chain.set_ylim(0, 1)

    ax_chain.text(0.5, 0.97, 'THE BST CHAIN', fontsize=14, fontweight='bold',
                  color=PURPLE, ha='center', fontfamily='monospace')
    ax_chain.text(0.5, 0.935, 'Why Bell violations exist',
                  fontsize=10, color=GREY, ha='center', fontfamily='monospace')

    # Chain steps
    chain_data = [
        ('n_C = 5',          'complex dim of D_IV^5',   '#4422aa'),
        ('S^4 boundary',     'Shilov boundary',         '#5533bb'),
        ('3D space',         'S^4 = susp(S^3)',         '#3366cc'),
        ('SO(3)',            'rotation group',           '#2277dd'),
        ('SU(2) = Spin(3)',  'universal cover',          '#1188ee'),
        ('spin-1/2',         'fundamental rep',          '#0099dd'),
        ('binary +/-',       'measurement outcomes',     '#00aacc'),
        ('2\u221a2 bound',   'Tsirelson limit',          GOLD_DIM),
    ]

    n_steps = len(chain_data)
    y_top = 0.88
    y_bot = 0.30
    dy = (y_top - y_bot) / (n_steps - 1)
    box_w = 0.65
    box_h = 0.055

    for i, (label, sublabel, color) in enumerate(chain_data):
        y = y_top - i * dy
        # Box
        _draw_rounded_box(ax_chain, 0.5, y, box_w, box_h, label,
                          color=color, fontsize=11, text_color=WHITE)
        # Sublabel
        ax_chain.text(0.5, y - box_h / 2 - 0.012, sublabel,
                      fontsize=7, color=GREY, ha='center',
                      fontfamily='monospace', style='italic')
        # Arrow
        if i < n_steps - 1:
            arrow_y1 = y - box_h / 2 - 0.025
            arrow_y2 = y - dy + box_h / 2 + 0.005
            _draw_arrow_down(ax_chain, 0.5, arrow_y1, arrow_y2,
                             color=DGREY)

    # ─── Number Line: Bounds Visualization ───
    nl_y = 0.14
    ax_chain.text(0.5, 0.23, 'THE THREE BOUNDS', fontsize=11,
                  fontweight='bold', color=WHITE, ha='center',
                  fontfamily='monospace')

    # Number line
    nl_left = 0.08
    nl_right = 0.92
    ax_chain.plot([nl_left, nl_right], [nl_y, nl_y], '-', color=DGREY,
                  linewidth=2, zorder=1)

    # Positions on number line: 0..4 mapped to nl_left..nl_right
    def nl_x(val):
        return nl_left + (val / 4.0) * (nl_right - nl_left)

    # Origin
    ax_chain.plot(nl_x(0), nl_y, '|', color=DGREY, markersize=8, zorder=2)
    ax_chain.text(nl_x(0), nl_y - 0.035, '0', fontsize=8, color=DGREY,
                  ha='center', fontfamily='monospace')

    # Classical bound at 2
    ax_chain.plot(nl_x(2), nl_y, 'D', color=RED, markersize=10, zorder=5)
    ax_chain.text(nl_x(2), nl_y + 0.03, '2', fontsize=11, color=RED,
                  ha='center', fontfamily='monospace', fontweight='bold')
    ax_chain.text(nl_x(2), nl_y - 0.035, 'Classical', fontsize=7,
                  color=RED, ha='center', fontfamily='monospace')

    # Tsirelson bound at 2*sqrt(2)
    ax_chain.plot(nl_x(TSIRELSON_BOUND), nl_y, '*', color=GOLD,
                  markersize=16, zorder=5)
    ax_chain.text(nl_x(TSIRELSON_BOUND), nl_y + 0.03, '2\u221a2',
                  fontsize=11, color=GOLD, ha='center',
                  fontfamily='monospace', fontweight='bold')
    ax_chain.text(nl_x(TSIRELSON_BOUND), nl_y - 0.035, 'Quantum / BST',
                  fontsize=7, color=GOLD, ha='center', fontfamily='monospace')

    # Algebraic bound at 4
    ax_chain.plot(nl_x(4), nl_y, 's', color=GREY, markersize=10, zorder=5)
    ax_chain.text(nl_x(4), nl_y + 0.03, '4', fontsize=11, color=GREY,
                  ha='center', fontfamily='monospace', fontweight='bold')
    ax_chain.text(nl_x(4), nl_y - 0.035, 'No-signaling', fontsize=7,
                  color=GREY, ha='center', fontfamily='monospace')

    # Colored segments
    ax_chain.plot([nl_x(0), nl_x(2)], [nl_y, nl_y], '-', color=RED,
                  linewidth=4, alpha=0.4, zorder=2)
    ax_chain.plot([nl_x(2), nl_x(TSIRELSON_BOUND)], [nl_y, nl_y], '-',
                  color=GOLD, linewidth=4, alpha=0.5, zorder=2)
    ax_chain.plot([nl_x(TSIRELSON_BOUND), nl_x(4)], [nl_y, nl_y], '-',
                  color=GREY, linewidth=4, alpha=0.3, zorder=2)

    # Region labels
    ax_chain.text(nl_x(1), nl_y + 0.06, 'Local HV', fontsize=7,
                  color=RED, ha='center', fontfamily='monospace',
                  alpha=0.7)
    mid_qt = (2 + TSIRELSON_BOUND) / 2
    ax_chain.text(nl_x(mid_qt), nl_y + 0.06, 'Quantum', fontsize=7,
                  color=GOLD, ha='center', fontfamily='monospace',
                  alpha=0.9)
    mid_na = (TSIRELSON_BOUND + 4) / 2
    ax_chain.text(nl_x(mid_na), nl_y + 0.06, 'Post-QM', fontsize=7,
                  color=GREY, ha='center', fontfamily='monospace',
                  alpha=0.7)

    # ─── Why 3D mini-text ───
    ax_chain.text(0.5, 0.05, '3D is minimum for non-abelian Spin(d)',
                  fontsize=8, color=CYAN, ha='center',
                  fontfamily='monospace', style='italic',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                            edgecolor=DGREY, alpha=0.8))

    # ═══════════════════════════════════════════════════════════════
    #  PANEL 3: SHARED COMMITMENT (Right)
    # ═══════════════════════════════════════════════════════════════
    ax_ent = fig.add_axes([0.67, 0.15, 0.30, 0.55], facecolor=DARK_PANEL)
    ax_ent.set_title('SHARED COMMITMENT', fontsize=13, fontweight='bold',
                     color=COMMIT_GOLD, fontfamily='monospace', pad=10)
    ax_ent.set_xlim(-1.5, 1.5)
    ax_ent.set_ylim(-1.3, 1.5)
    ax_ent.set_aspect('equal')
    ax_ent.axis('off')

    # Source point (pair creation)
    ax_ent.plot(0, 0, 'o', color=WHITE, markersize=12, zorder=10)
    ax_ent.text(0, 0.15, 'pair creation', fontsize=8, color=GREY,
                ha='center', fontfamily='monospace')

    # Alice (left)
    alice_x, alice_y = -1.0, 0.8
    ax_ent.plot(alice_x, alice_y, 'o', color=ALICE_COLOR, markersize=16,
                zorder=10)
    ax_ent.text(alice_x, alice_y + 0.18, 'ALICE', fontsize=10,
                color=ALICE_COLOR, ha='center', fontfamily='monospace',
                fontweight='bold')

    # Bob (right)
    bob_x, bob_y = 1.0, 0.8
    ax_ent.plot(bob_x, bob_y, 'o', color=BOB_COLOR, markersize=16,
                zorder=10)
    ax_ent.text(bob_x, bob_y + 0.18, 'BOB', fontsize=10,
                color=BOB_COLOR, ha='center', fontfamily='monospace',
                fontweight='bold')

    # Golden commitment line (curved through center)
    t_curve = np.linspace(0, 1, 100)
    # Bezier-like: source -> Alice and source -> Bob
    cx_a = alice_x * t_curve + 0 * (1 - t_curve)
    cy_a = alice_y * t_curve + 0 * (1 - t_curve)
    cx_b = bob_x * t_curve + 0 * (1 - t_curve)
    cy_b = bob_y * t_curve + 0 * (1 - t_curve)
    ax_ent.plot(cx_a, cy_a, '-', color=COMMIT_GOLD, linewidth=3,
                alpha=0.7, zorder=5)
    ax_ent.plot(cx_b, cy_b, '-', color=COMMIT_GOLD, linewidth=3,
                alpha=0.7, zorder=5)

    # "ONE record" label on the golden line
    ax_ent.text(0, 0.55, 'ONE shared\ncommitment', fontsize=9,
                color=COMMIT_GOLD, ha='center', fontfamily='monospace',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=COMMIT_GOLD, linewidth=1.5, alpha=0.9))

    # Alice's measurement arrow (initial: 0 degrees)
    arrow_len = 0.35
    alice_angle_init = 0.0
    alice_angle_rad = np.radians(alice_angle_init)
    alice_arrow, = ax_ent.plot(
        [alice_x, alice_x + arrow_len * np.cos(alice_angle_rad)],
        [alice_y, alice_y + arrow_len * np.sin(alice_angle_rad)],
        '-', color=ALICE_COLOR, linewidth=3, zorder=11)
    alice_arrow_tip, = ax_ent.plot(
        alice_x + arrow_len * np.cos(alice_angle_rad),
        alice_y + arrow_len * np.sin(alice_angle_rad),
        '>', color=ALICE_COLOR, markersize=8, zorder=11)

    # Bob's measurement arrow (initial: 45 degrees)
    bob_angle_init = 45.0
    bob_angle_rad = np.radians(bob_angle_init)
    bob_arrow, = ax_ent.plot(
        [bob_x, bob_x + arrow_len * np.cos(bob_angle_rad)],
        [bob_y, bob_y + arrow_len * np.sin(bob_angle_rad)],
        '-', color=BOB_COLOR, linewidth=3, zorder=11)
    bob_arrow_tip, = ax_ent.plot(
        bob_x + arrow_len * np.cos(bob_angle_rad),
        bob_y + arrow_len * np.sin(bob_angle_rad),
        '>', color=BOB_COLOR, markersize=8, zorder=11)

    # Angle labels
    alice_angle_label = ax_ent.text(
        alice_x - 0.45, alice_y - 0.15,
        f'a = {alice_angle_init:.0f}\u00b0',
        fontsize=9, color=ALICE_COLOR, fontfamily='monospace')
    bob_angle_label = ax_ent.text(
        bob_x + 0.1, bob_y - 0.15,
        f'b = {bob_angle_init:.0f}\u00b0',
        fontsize=9, color=BOB_COLOR, fontfamily='monospace')

    # Correlation readout
    theta_init = np.radians(bob_angle_init - alice_angle_init)
    E_init = model.correlation(theta_init)
    corr_text = ax_ent.text(
        0, -0.2,
        f'E(a,b) = -cos({bob_angle_init - alice_angle_init:.0f}\u00b0)'
        f' = {E_init:.4f}',
        fontsize=11, color=WHITE, ha='center', fontfamily='monospace',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                  edgecolor=CYAN, linewidth=1.5))

    # ─── Comparison table ───
    table_y = -0.55
    ax_ent.text(0, table_y, 'Classical vs BST', fontsize=10,
                color=WHITE, ha='center', fontfamily='monospace',
                fontweight='bold')

    table_data = [
        ('Classical:', 'Two separate records', RED, table_y - 0.17),
        ('  Result:', '|S| \u2264 2 (Bell obeyed)', RED, table_y - 0.30),
        ('BST:', 'One shared commitment', COMMIT_GOLD, table_y - 0.50),
        ('  Result:', '|S| \u2264 2\u221a2 (Bell violated)', COMMIT_GOLD,
         table_y - 0.63),
    ]
    for label, value, color, ty in table_data:
        ax_ent.text(-1.3, ty, label, fontsize=8, color=color,
                    fontfamily='monospace', fontweight='bold', va='center')
        ax_ent.text(-0.4, ty, value, fontsize=8, color=color,
                    fontfamily='monospace', va='center', alpha=0.85)

    # ─── Slider for Alice's angle ───
    ax_slider_alice = fig.add_axes([0.67, 0.09, 0.30, 0.02],
                                   facecolor=DARK_PANEL)
    slider_alice = Slider(ax_slider_alice, 'Alice \u00b0', 0, 360,
                          valinit=alice_angle_init, valstep=1,
                          color=ALICE_COLOR)
    slider_alice.label.set_color(ALICE_COLOR)
    slider_alice.label.set_fontfamily('monospace')
    slider_alice.label.set_fontsize(9)
    slider_alice.valtext.set_color(ALICE_COLOR)
    slider_alice.valtext.set_fontfamily('monospace')

    ax_slider_bob = fig.add_axes([0.67, 0.055, 0.30, 0.02],
                                 facecolor=DARK_PANEL)
    slider_bob = Slider(ax_slider_bob, 'Bob \u00b0', 0, 360,
                        valinit=bob_angle_init, valstep=1,
                        color=BOB_COLOR)
    slider_bob.label.set_color(BOB_COLOR)
    slider_bob.label.set_fontfamily('monospace')
    slider_bob.label.set_fontsize(9)
    slider_bob.valtext.set_color(BOB_COLOR)
    slider_bob.valtext.set_fontfamily('monospace')

    def update_entanglement(val):
        a_deg = slider_alice.val
        b_deg_val = slider_bob.val
        a_rad = np.radians(a_deg)
        b_rad = np.radians(b_deg_val)

        # Update Alice's arrow
        ax_a = alice_x + arrow_len * np.cos(a_rad)
        ay_a = alice_y + arrow_len * np.sin(a_rad)
        alice_arrow.set_data([alice_x, ax_a], [alice_y, ay_a])
        alice_arrow_tip.set_data([ax_a], [ay_a])
        alice_angle_label.set_text(f'a = {a_deg:.0f}\u00b0')

        # Update Bob's arrow
        bx_b = bob_x + arrow_len * np.cos(b_rad)
        by_b = bob_y + arrow_len * np.sin(b_rad)
        bob_arrow.set_data([bob_x, bx_b], [bob_y, by_b])
        bob_arrow_tip.set_data([bx_b], [by_b])
        bob_angle_label.set_text(f'b = {b_deg_val:.0f}\u00b0')

        # Update correlation
        diff_deg = b_deg_val - a_deg
        theta = np.radians(diff_deg)
        E = model.correlation(theta)
        corr_text.set_text(
            f'E(a,b) = -cos({diff_deg:.0f}\u00b0) = {E:.4f}')

        fig.canvas.draw_idle()

    slider_alice.on_changed(update_entanglement)
    slider_bob.on_changed(update_entanglement)

    # ═══════════════════════════════════════════════════════════════
    #  INFO PANELS (top strip across all three)
    # ═══════════════════════════════════════════════════════════════

    # Left info: CHSH formula
    ax_info_l = fig.add_axes([0.05, 0.74, 0.28, 0.14], facecolor=BG)
    ax_info_l.axis('off')
    ax_info_l.set_xlim(0, 1)
    ax_info_l.set_ylim(0, 1)
    ax_info_l.text(0.5, 0.85, 'CHSH Inequality', fontsize=12,
                   fontweight='bold', color=CYAN, ha='center',
                   fontfamily='monospace')
    ax_info_l.text(0.5, 0.60,
                   'S = E(a,b) - E(a,b\') + E(a\',b) + E(a\',b\')',
                   fontsize=9, color=WHITE, ha='center',
                   fontfamily='monospace',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_PANEL,
                             edgecolor=DGREY))
    ax_info_l.text(0.5, 0.30,
                   'E(a,b) = -cos(\u03b8)  [singlet state]',
                   fontsize=9, color=LIGHT_BLUE, ha='center',
                   fontfamily='monospace')
    ax_info_l.text(0.5, 0.08,
                   'Classical: |S| \u2264 2    Quantum: |S| \u2264 2\u221a2',
                   fontsize=9, color=GOLD_DIM, ha='center',
                   fontfamily='monospace')

    # Right info: BST insight
    ax_info_r = fig.add_axes([0.67, 0.74, 0.30, 0.14], facecolor=BG)
    ax_info_r.axis('off')
    ax_info_r.set_xlim(0, 1)
    ax_info_r.set_ylim(0, 1)
    ax_info_r.text(0.5, 0.85, 'BST Entanglement', fontsize=12,
                   fontweight='bold', color=COMMIT_GOLD, ha='center',
                   fontfamily='monospace')
    ax_info_r.text(0.5, 0.58,
                   'Not action at a distance.\n'
                   'One holomorphic record in A\u00b2(D_IV\u2075)\n'
                   'with two boundary endpoints.',
                   fontsize=8, color=WHITE, ha='center',
                   fontfamily='monospace', linespacing=1.4,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_PANEL,
                             edgecolor=DGREY))
    ax_info_r.text(0.5, 0.12,
                   '2\u221a2 = 2\u221aN_w   (N_w = 2 = dim weak doublet)',
                   fontsize=9, color=GOLD, ha='center',
                   fontfamily='monospace')

    plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import sys

    # If run with --test, exercise the API without GUI
    if '--test' in sys.argv:
        bell = BellInequality()

        print("=" * 60)
        print("  BELL INEQUALITY — BST PLAYGROUND")
        print("=" * 60)

        # Bounds
        print(f"\n--- Bounds ---")
        print(f"  Classical (Bell):   |S| <= {bell.classical_bound()}")
        print(f"  Tsirelson (QM):     |S| <= {bell.tsirelson_bound():.6f}")
        print(f"  Algebraic (NS):     |S| <= {bell.algebraic_bound()}")

        # Optimal angles
        opt = bell.optimal_angles()
        print(f"\n--- Optimal CHSH Configuration ---")
        print(f"  a  = {opt['a']:.1f} deg")
        print(f"  a' = {opt['a_prime']:.1f} deg")
        print(f"  b  = {opt['b']:.1f} deg")
        print(f"  b' = {opt['b_prime']:.1f} deg")
        print(f"  S  = {opt['S']:.6f}")
        print(f"  Theory: {opt['S_theory']:.6f}")
        assert abs(opt['S'] - opt['S_theory']) < 1e-10, "Mismatch!"

        # Sweep
        sweep = bell.sweep_angles(n=500)
        print(f"\n--- Angle Sweep ---")
        print(f"  Max |S| = {sweep['S_max']:.6f} at b = {sweep['b_max_deg']:.1f} deg")

        # Correlation
        print(f"\n--- Sample Correlations ---")
        for theta_deg in [0, 45, 90, 135, 180]:
            E = bell.correlation(np.radians(theta_deg))
            print(f"  E({theta_deg:3d} deg) = {E:+.4f}")

        # BST chain
        print(f"\n--- BST Derivation Chain ---")
        for i, step in enumerate(bell.bst_chain()):
            print(f"  [{i+1}] {step}")

        # Why 3D
        print(f"\n--- Why 3 Dimensions ---")
        print(bell.why_3d())

        # Entanglement
        print(f"\n--- BST Entanglement ---")
        desc = bell.entanglement_description()
        for key, val in desc.items():
            print(f"\n  [{key}]")
            for line in val.split('\n'):
                print(f"    {line}")

        # Some specific CHSH computations
        print(f"\n--- Specific CHSH Values ---")
        configs = [
            (0, 90, 45, 135, "Optimal"),
            (0, 90, 0, 90, "Aligned"),
            (0, 45, 22.5, 67.5, "Half-optimal"),
            (0, 60, 30, 90, "60-deg spacing"),
        ]
        for a, ap, b, bp, name in configs:
            S = bell.chsh(a, ap, b, bp)
            viol = "VIOLATES" if abs(S) > 2 else "obeys"
            print(f"  {name:20s}: S = {S:+.4f}  ({viol} Bell)")

        print(f"\n{'=' * 60}")
        print("  All tests passed.")
        print(f"{'=' * 60}")

    else:
        build_gui()
