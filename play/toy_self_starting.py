#!/usr/bin/env python3
"""
WHY THE UNIVERSE SELF-STARTS
==============================
Four independent arguments prove that the "frozen state" (N=0, zero
excitations, full SO(5,2) symmetry) CANNOT EXIST on D_IV^5:

  1. Negative curvature: perturbations grow exponentially.
  2. Quantum uncertainty: cannot localize at origin.
  3. Representation theory: trivial rep is not physical (below Wallach set).
  4. Entropy: localized states spread in ~1.87 Planck times.

Plus the Reality Budget: Lambda * N = 9/5.  If N=0, then 0 != 9/5.
Contradiction. So N >= 2 always. The universe starts with a nu_1 nu_1-bar
pair.

The Commitment Cascade (k=0 -> 1 -> 3 -> 6) is the arrow of time:
different Casimir eigenvalues cannot be connected by unitary operators.
Commitments are irreversible.

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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle

# ═══════════════════════════════════════════════════════════
#  BST CONSTANTS
# ═══════════════════════════════════════════════════════════
N_c = 3                         # color charges
n_C = 5                         # complex dimension of D_IV^5
N_max = 137                     # channel capacity
C_2 = 6                         # Casimir eigenvalue of baryon (= n_C + 1)
genus = 7                       # genus of D_IV^5 (= n_C + 2)
BUDGET = 9.0 / 5.0             # Reality budget: Lambda * N = N_c^2 / n_C
FILL = 3.0 / (5.0 * np.pi)    # Fill fraction N_c / (n_C * pi)
H_curv = -2.0 / (n_C + 2)     # Holomorphic sectional curvature = -2/7
LYAPUNOV = np.sqrt(2.0 / 7.0) # Perturbation growth rate
TAU_SPREAD = np.sqrt(7.0 / 2.0)  # Spreading time in Planck units
WALLACH_MIN = 3                # Minimum weight in Wallach set

# ─── Color palette (dark theme) ───
BG = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
BLUE_GLOW = '#4488ff'
PURPLE_GLOW = '#8844cc'
PURPLE_DEEP = '#6622aa'
ORANGE_GLOW = '#ff8800'
RED_WARN = '#ff4444'
RED_DEEP = '#cc2222'
GREEN_OK = '#44ff88'
WHITE = '#ffffff'
GREY = '#888888'
GREY_DIM = '#555555'
CYAN = '#44ddff'


# ═══════════════════════════════════════════════════════════
#  CLASS: SelfStartingUniverse
# ═══════════════════════════════════════════════════════════
class SelfStartingUniverse:
    """
    BST playground class demonstrating why D_IV^5 geometry
    forces the universe to self-start from N >= 2.

    All methods are pure-numpy, no matplotlib dependency.
    Suitable for CI scripting and programmatic exploration.
    """

    def __init__(self):
        self.n_C = n_C
        self.N_c = N_c
        self.N_max = N_max
        self.C_2 = C_2
        self.genus = genus
        self.budget = BUDGET
        self.fill = FILL
        self.H = H_curv
        self.lyapunov = LYAPUNOV
        self.tau = TAU_SPREAD
        self.wallach_min = WALLACH_MIN

    # ─── Frozen state arguments ───
    def frozen_state_arguments(self) -> list:
        """Return all four arguments why the frozen state (N=0) cannot exist."""
        return [
            {
                'name': 'Negative Curvature',
                'symbol': 'H = -2/7',
                'summary': (
                    f'D_IV^5 has constant negative holomorphic sectional '
                    f'curvature H = -2/(n_C+2) = -2/7. Perturbations grow '
                    f'as |J(t)| ~ exp(sqrt(2/7) * t). The origin is '
                    f'dynamically unstable — a ball on a hilltop.'
                ),
                'growth_rate': self.lyapunov,
                'tag': 'UNSTABLE',
            },
            {
                'name': 'Quantum Uncertainty',
                'symbol': 'dz*dp >= h/2',
                'summary': (
                    f'Heisenberg uncertainty in each of n_C={self.n_C} '
                    f'complex directions. Cannot localize at the origin '
                    f'with zero momentum. Zero-point fluctuation fills '
                    f'the entire domain.'
                ),
                'dimensions': self.n_C,
                'tag': 'FORBIDDEN',
            },
            {
                'name': 'Representation Theory',
                'symbol': 'k=0 < k_min=3',
                'summary': (
                    f'The trivial representation (k=0) is below the '
                    f'Wallach set (k_min={self.wallach_min}), below even '
                    f'the electron (k=1). It is not a valid physical state. '
                    f'The vacuum IS the neutrino condensate.'
                ),
                'wallach_min': self.wallach_min,
                'tag': 'INVALID',
            },
            {
                'name': 'Entropy / Spreading',
                'symbol': f'tau ~ {self.tau:.2f} t_Pl',
                'summary': (
                    f'Localized state has minimum entropy. On negatively '
                    f'curved space, wave functions spread exponentially. '
                    f'Spreading time tau ~ sqrt(7/2) = {self.tau:.4f} '
                    f'Planck times.'
                ),
                'spreading_time': self.tau,
                'tag': 'SPREADS',
            },
        ]

    # ─── Jacobi field growth ───
    def jacobi_growth(self, t_array) -> np.ndarray:
        """
        Jacobi field growth on D_IV^5:
            |J(t)| = exp(sqrt(2/7) * t)

        Parameters
        ----------
        t_array : array-like
            Time values in Planck units.

        Returns
        -------
        np.ndarray
            Perturbation amplitudes |J(t)| / |J(0)|.
        """
        t = np.asarray(t_array, dtype=float)
        return np.exp(self.lyapunov * t)

    # ─── Spreading time ───
    def spreading_time(self) -> float:
        """
        Characteristic spreading time for a localized wavepacket
        on the negatively curved bulk of D_IV^5.

        Returns sqrt(7/2) ~ 1.8708 Planck times.
        """
        return self.tau

    # ─── Commitment cascade ───
    def commitment_cascade(self) -> list:
        """
        Return the cascade stages k=0 -> 1 -> 3 -> 6 with Casimir
        eigenvalues and particle identifications.

        Each stage is a dict with keys:
            stage, k, C2, excitation, description
        """
        return [
            {
                'stage': 0,
                'k': 0,
                'C2': self.casimir(0),
                'excitation': 'Vacuum',
                'description': 'nu_1 condensate (m=0)',
                'color': PURPLE_GLOW,
            },
            {
                'stage': 1,
                'k': 1,
                'C2': self.casimir(1),
                'excitation': 'Electron',
                'description': 'e+e- pairs (below Wallach set: boundary)',
                'color': BLUE_GLOW,
            },
            {
                'stage': 2,
                'k': 3,
                'C2': self.casimir(3),
                'excitation': 'Wallach threshold',
                'description': 'First bulk excitation (k_min=3)',
                'color': GREEN_OK,
            },
            {
                'stage': 3,
                'k': 6,
                'C2': self.casimir(6),
                'excitation': 'Baryon',
                'description': 'Proton/neutron (holomorphic discrete series)',
                'color': GOLD,
            },
        ]

    # ─── Casimir eigenvalue ───
    def casimir(self, k) -> float:
        """
        Harish-Chandra formula for SO_0(5,2):
            C_2(k) = k * (k - n_C) = k * (k - 5)

        Parameters
        ----------
        k : int or float
            Representation weight.

        Returns
        -------
        float
            The Casimir eigenvalue.
        """
        return float(k * (k - self.n_C))

    # ─── Initial state ───
    def initial_N(self) -> dict:
        """
        The mandatory initial state of the universe.

        From the Reality Budget: Lambda * N = 9/5.
        At Planck epoch Lambda ~ 1, so N ~ 9/5 ~ 2.
        The minimum integer N = 2 corresponds to a nu_1 nu_1-bar pair.

        Returns
        -------
        dict
            Keys: N, Lambda, pair, explanation
        """
        N = 2
        Lambda = self.budget / N  # = 9/10
        return {
            'N': N,
            'Lambda': Lambda,
            'pair': 'nu_1 nu_1-bar',
            'explanation': (
                f'Lambda * N = {self.budget:.1f}. '
                f'At Planck epoch Lambda ~ 1, so N ~ {self.budget:.1f} ~ 2. '
                f'The universe starts with a nu_1 nu_1-bar pair.'
            ),
        }

    # ─── Epoch table ───
    def epoch_table(self) -> list:
        """
        Evolution of the universe from N=2 to N ~ 6.2e121,
        showing the Lambda-N tradeoff.

        Returns
        -------
        list of dict
            Each dict has keys: epoch, N, Lambda, description
        """
        return [
            {
                'epoch': 'Planck',
                'N': 2,
                'Lambda': self.budget / 2,
                'log10_N': np.log10(2),
                'description': 'nu_1 nu_1-bar pair; Lambda = 9/10',
            },
            {
                'epoch': 'Inflation end',
                'N': 1e60,
                'Lambda': self.budget / 1e60,
                'log10_N': 60,
                'description': 'Exponential commitment; Lambda crashes',
            },
            {
                'epoch': 'Nucleosynthesis',
                'N': 1e78,
                'Lambda': self.budget / 1e78,
                'log10_N': 78,
                'description': 'Baryons committed; T ~ 0.5 MeV',
            },
            {
                'epoch': 'Recombination',
                'N': 1e88,
                'Lambda': self.budget / 1e88,
                'log10_N': 88,
                'description': 'Atoms form; CMB released',
            },
            {
                'epoch': 'Today',
                'N': 1e121,
                'Lambda': self.budget / 1e121,
                'log10_N': 121,
                'description': f'Lambda = {self.budget/1e121:.1e}; 19.1% committed',
            },
            {
                'epoch': 'Far future',
                'N': 6.2e121,
                'Lambda': self.budget / 6.2e121,
                'log10_N': np.log10(6.2e121),
                'description': 'Heat death; Lambda -> 0; N -> max',
            },
        ]

    # ─── Validity check ───
    def is_frozen_valid(self) -> bool:
        """
        Is the frozen state (N=0) a valid state on D_IV^5?

        Always returns False. Four independent arguments prove this.
        """
        return False

    # ─── Summary report ───
    def report(self) -> str:
        """Print a text summary of all self-starting physics."""
        lines = []
        lines.append('=' * 68)
        lines.append('  WHY THE UNIVERSE SELF-STARTS')
        lines.append('  Bubble Spacetime Theory on D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]')
        lines.append('=' * 68)
        lines.append('')

        # Frozen state arguments
        lines.append('THE FROZEN STATE (N=0) IS IMPOSSIBLE:')
        lines.append('-' * 40)
        for i, arg in enumerate(self.frozen_state_arguments(), 1):
            lines.append(f'  {i}. [{arg["tag"]}] {arg["name"]}')
            lines.append(f'     {arg["symbol"]}')
            lines.append(f'     {arg["summary"]}')
            lines.append('')

        # Reality Budget
        lines.append('THE REALITY BUDGET:')
        lines.append('-' * 40)
        init = self.initial_N()
        lines.append(f'  Lambda * N = {self.budget} = N_c^2/n_C = 9/5')
        lines.append(f'  If N=0: 0 != 9/5.  Contradiction.')
        lines.append(f'  Minimum: N = {init["N"]}, Lambda = {init["Lambda"]:.4f}')
        lines.append(f'  Starting pair: {init["pair"]}')
        lines.append('')

        # Commitment cascade
        lines.append('THE COMMITMENT CASCADE (arrow of time):')
        lines.append('-' * 40)
        lines.append(f'  {"Stage":<8} {"k":<6} {"C2=k(k-5)":<14} {"Excitation":<18} {"Description"}')
        for s in self.commitment_cascade():
            lines.append(
                f'  {s["stage"]:<8} {s["k"]:<6} {s["C2"]:<14.0f} '
                f'{s["excitation"]:<18} {s["description"]}'
            )
        lines.append('')

        # Key numbers
        lines.append('KEY NUMBERS:')
        lines.append('-' * 40)
        lines.append(f'  Holomorphic sectional curvature H = {H_curv:.6f} = -2/7')
        lines.append(f'  Lyapunov exponent = sqrt(2/7) = {LYAPUNOV:.6f}')
        lines.append(f'  Spreading time tau = sqrt(7/2) = {TAU_SPREAD:.6f} t_Pl')
        lines.append(f'  Wallach set minimum k_min = {WALLACH_MIN}')
        lines.append(f'  Casimir(k=6) = {self.casimir(6):.0f}')
        lines.append(f'  Fill fraction = {FILL:.6f} = {FILL*100:.2f}%')
        lines.append('')

        # Epoch table
        lines.append('EPOCH TABLE:')
        lines.append('-' * 40)
        lines.append(f'  {"Epoch":<18} {"log10(N)":<12} {"Lambda":<14} {"Description"}')
        for e in self.epoch_table():
            lines.append(
                f'  {e["epoch"]:<18} {e["log10_N"]:<12.1f} '
                f'{e["Lambda"]:<14.2e} {e["description"]}'
            )
        lines.append('')

        lines.append('CONCLUSION:')
        lines.append(f'  is_frozen_valid() = {self.is_frozen_valid()}')
        lines.append('  The universe exists because the geometry of D_IV^5')
        lines.append('  does not admit N=0.')
        lines.append('=' * 68)

        return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════
#  VISUALIZATION
# ═══════════════════════════════════════════════════════════

def build_visualization():
    """Build the three-panel matplotlib visualization."""

    universe = SelfStartingUniverse()

    fig = plt.figure(figsize=(19, 11), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'Why the Universe Self-Starts — BST'
    )

    # ─── Main title ───
    fig.text(
        0.5, 0.97, 'WHY THE UNIVERSE SELF-STARTS',
        fontsize=26, fontweight='bold', color=GOLD,
        ha='center', fontfamily='monospace',
        path_effects=[pe.withStroke(linewidth=3, foreground='#663300')]
    )
    fig.text(
        0.5, 0.935,
        'Four proofs that D_IV^5 does not admit N = 0',
        fontsize=13, color=GOLD_DIM, ha='center', fontfamily='monospace'
    )

    # ─── Bottom strip ───
    fig.text(
        0.5, 0.015,
        'The universe exists because the geometry of D_IV^5 does not admit N = 0.',
        fontsize=12, fontweight='bold', color=GOLD,
        ha='center', fontfamily='monospace',
        bbox=dict(
            boxstyle='round,pad=0.4', facecolor='#1a1a0a',
            edgecolor=GOLD_DIM, linewidth=2
        )
    )

    # ═══════════════════════════════════════════════════════
    #  LEFT PANEL — The Four Arguments
    # ═══════════════════════════════════════════════════════
    ax_left_top = fig.add_axes([0.02, 0.52, 0.30, 0.36])
    ax_left_bot = fig.add_axes([0.02, 0.06, 0.30, 0.42])

    # ─── Top: Jacobi field exponential growth ───
    ax = ax_left_top
    ax.set_facecolor(DARK_PANEL)

    t = np.linspace(0, 12, 300)
    J = universe.jacobi_growth(t)

    ax.fill_between(t, 1, J, alpha=0.15, color=RED_WARN)
    ax.plot(t, J, color=RED_WARN, linewidth=2.5, zorder=5)
    ax.axhline(y=1, color=GREY_DIM, linewidth=1, linestyle='--', alpha=0.5)

    # Mark the spreading time
    tau = universe.spreading_time()
    J_tau = universe.jacobi_growth([tau])[0]
    ax.plot(tau, J_tau, 'o', color=ORANGE_GLOW, markersize=10, zorder=6)
    ax.annotate(
        f'tau = {tau:.2f} t_Pl',
        xy=(tau, J_tau), xytext=(tau + 1.5, J_tau + 15),
        fontsize=9, color=ORANGE_GLOW, fontfamily='monospace',
        arrowprops=dict(arrowstyle='->', color=ORANGE_GLOW, lw=1.5),
    )

    # Mark doubling and 10x points
    t_double = np.log(2) / LYAPUNOV
    t_10x = np.log(10) / LYAPUNOV
    ax.axvline(x=t_double, color=GOLD_DIM, linewidth=1, linestyle=':', alpha=0.6)
    ax.text(
        t_double, max(J) * 0.85, f'2x at {t_double:.1f}',
        fontsize=8, color=GOLD_DIM, fontfamily='monospace', ha='center'
    )
    ax.axvline(x=t_10x, color=RED_DEEP, linewidth=1, linestyle=':', alpha=0.6)
    ax.text(
        t_10x, max(J) * 0.70, f'10x at {t_10x:.1f}',
        fontsize=8, color=RED_DEEP, fontfamily='monospace', ha='center'
    )

    ax.set_xlabel('Time (Planck units)', fontsize=9, color=GREY,
                  fontfamily='monospace')
    ax.set_ylabel('|J(t)| / |J(0)|', fontsize=9, color=GREY,
                  fontfamily='monospace')
    ax.set_title(
        'JACOBI FIELD GROWTH: exp(sqrt(2/7) t)',
        fontsize=11, fontweight='bold', color=RED_WARN,
        fontfamily='monospace', pad=8
    )
    ax.tick_params(colors=GREY, labelsize=8)
    for spine in ax.spines.values():
        spine.set_color('#333355')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, max(J) * 1.1)

    # ─── Bottom: Four argument boxes in 2x2 grid ───
    ax = ax_left_bot
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    arguments = universe.frozen_state_arguments()
    box_colors = [RED_WARN, ORANGE_GLOW, PURPLE_GLOW, CYAN]
    box_icons = ['~', 'dz*dp', 'k<3', 'S']
    box_positions = [
        (0.02, 0.52, 0.46, 0.44),   # top-left
        (0.52, 0.52, 0.46, 0.44),   # top-right
        (0.02, 0.04, 0.46, 0.44),   # bottom-left
        (0.52, 0.04, 0.46, 0.44),   # bottom-right
    ]

    for i, (arg, color, icon, (bx, by, bw, bh)) in enumerate(
        zip(arguments, box_colors, box_icons, box_positions)
    ):
        # Box background
        box = FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle='round,pad=0.02',
            facecolor='#0a0a2a', edgecolor=color,
            linewidth=2, alpha=0.9, zorder=1
        )
        ax.add_patch(box)

        # Argument number
        ax.text(
            bx + 0.04, by + bh - 0.06,
            f'{i+1}', fontsize=18, fontweight='bold',
            color=color, ha='left', va='top',
            fontfamily='monospace', zorder=2
        )

        # Tag badge
        tag = arg['tag']
        ax.text(
            bx + bw - 0.04, by + bh - 0.06,
            tag, fontsize=8, fontweight='bold',
            color=BG, ha='right', va='top',
            fontfamily='monospace', zorder=3,
            bbox=dict(
                boxstyle='round,pad=0.15', facecolor=color,
                edgecolor='none', alpha=0.9
            )
        )

        # Title
        ax.text(
            bx + bw / 2, by + bh - 0.14,
            arg['name'], fontsize=10, fontweight='bold',
            color=WHITE, ha='center', va='top',
            fontfamily='monospace', zorder=2
        )

        # Symbol
        ax.text(
            bx + bw / 2, by + bh - 0.22,
            arg['symbol'], fontsize=9,
            color=color, ha='center', va='top',
            fontfamily='monospace', zorder=2,
            style='italic'
        )

        # One-line summary (wrap manually)
        summary = arg['summary']
        # Truncate to fit box
        max_chars = 80
        if len(summary) > max_chars:
            words = summary[:max_chars].rsplit(' ', 1)[0] + '...'
        else:
            words = summary
        # Split into two lines
        mid = len(words) // 2
        split_pos = words.find(' ', mid)
        if split_pos == -1:
            split_pos = mid
        line1 = words[:split_pos]
        line2 = words[split_pos:].strip()

        ax.text(
            bx + bw / 2, by + 0.10,
            line1, fontsize=7, color=GREY,
            ha='center', va='center',
            fontfamily='monospace', zorder=2
        )
        ax.text(
            bx + bw / 2, by + 0.04,
            line2, fontsize=7, color=GREY,
            ha='center', va='center',
            fontfamily='monospace', zorder=2
        )

    # ═══════════════════════════════════════════════════════
    #  CENTER PANEL — The Commitment Cascade
    # ═══════════════════════════════════════════════════════
    ax_center = fig.add_axes([0.35, 0.06, 0.30, 0.82])
    ax = ax_center
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1.05)
    ax.axis('off')

    ax.text(
        0.5, 1.02, 'THE COMMITMENT CASCADE',
        fontsize=14, fontweight='bold', color=GOLD,
        ha='center', va='top', fontfamily='monospace',
        path_effects=[pe.withStroke(linewidth=1, foreground='#332200')]
    )
    ax.text(
        0.5, 0.97, 'Arrow of time = increasing C_2',
        fontsize=9, color=GOLD_DIM, ha='center', va='top',
        fontfamily='monospace'
    )

    cascade = universe.commitment_cascade()
    n_levels = len(cascade)

    # Positions for the energy levels (bottom to top)
    level_y = [0.08, 0.30, 0.55, 0.80]
    level_x_center = 0.5
    level_width = 0.55

    # Draw levels
    for i, stage in enumerate(cascade):
        y = level_y[i]
        color = stage['color']
        k = stage['k']
        c2 = stage['C2']
        name = stage['excitation']
        desc = stage['description']

        # Energy level bar
        x_left = level_x_center - level_width / 2
        x_right = level_x_center + level_width / 2

        # Glowing bar
        for gw in [6, 4, 2.5]:
            ax.plot(
                [x_left, x_right], [y, y],
                color=color, linewidth=gw, alpha=0.2 + 0.25 * (3 - gw / 2),
                solid_capstyle='round', zorder=3
            )
        ax.plot(
            [x_left, x_right], [y, y],
            color=color, linewidth=2, alpha=1.0,
            solid_capstyle='round', zorder=4
        )

        # Left label: particle name
        ax.text(
            x_left - 0.02, y, name,
            fontsize=11, fontweight='bold', color=color,
            ha='right', va='center', fontfamily='monospace',
            zorder=5
        )

        # Right labels: k and C_2
        ax.text(
            x_right + 0.02, y + 0.015,
            f'k = {k}', fontsize=9, color=WHITE,
            ha='left', va='center', fontfamily='monospace',
            zorder=5
        )
        ax.text(
            x_right + 0.02, y - 0.015,
            f'C_2 = {c2:.0f}', fontsize=9, color=GREY,
            ha='left', va='center', fontfamily='monospace',
            zorder=5
        )

        # Description below the bar
        ax.text(
            level_x_center, y - 0.035,
            desc, fontsize=7, color=GREY_DIM,
            ha='center', va='top', fontfamily='monospace',
            style='italic', zorder=5
        )

        # Ratchet mark on the left side of each bar
        if i > 0:
            ratchet_x = x_left + 0.01
            ratchet_size = 0.012
            # Small triangle pointing up (ratchet tooth)
            triangle_x = [ratchet_x - ratchet_size, ratchet_x + ratchet_size, ratchet_x]
            triangle_y = [y - ratchet_size, y - ratchet_size, y]
            ax.fill(triangle_x, triangle_y, color=color, alpha=0.7, zorder=6)

    # Draw upward arrows between levels (irreversible)
    for i in range(n_levels - 1):
        y_start = level_y[i] + 0.02
        y_end = level_y[i + 1] - 0.02
        color_start = cascade[i]['color']
        color_end = cascade[i + 1]['color']

        # Arrow shaft
        n_seg = 20
        for j in range(n_seg):
            frac = j / n_seg
            yy0 = y_start + frac * (y_end - y_start)
            yy1 = y_start + (frac + 1.0 / n_seg) * (y_end - y_start)
            # Interpolate color via RGB
            c_s = np.array(matplotlib.colors.to_rgb(color_start))
            c_e = np.array(matplotlib.colors.to_rgb(color_end))
            c_interp = c_s + frac * (c_e - c_s)
            ax.plot(
                [level_x_center, level_x_center], [yy0, yy1],
                color=c_interp, linewidth=2.5, alpha=0.6, zorder=2
            )

        # Arrowhead
        arrow_size = 0.018
        arrow_x = [
            level_x_center - arrow_size,
            level_x_center + arrow_size,
            level_x_center
        ]
        arrow_y = [y_end - arrow_size, y_end - arrow_size, y_end]
        ax.fill(arrow_x, arrow_y, color=cascade[i + 1]['color'],
                alpha=0.9, zorder=6)

        # "IRREVERSIBLE" text alongside the arrow
        mid_y = (y_start + y_end) / 2
        ax.text(
            level_x_center + 0.18, mid_y,
            'IRREVERSIBLE',
            fontsize=6, color=RED_WARN, alpha=0.5,
            ha='center', va='center', fontfamily='monospace',
            rotation=90, zorder=2,
            fontweight='bold'
        )

    # Starting point annotation
    ax.text(
        level_x_center, 0.01,
        'N = 2  (nu_1 nu_1-bar pair)',
        fontsize=10, fontweight='bold', color=PURPLE_GLOW,
        ha='center', va='bottom', fontfamily='monospace',
        bbox=dict(
            boxstyle='round,pad=0.3', facecolor='#1a0a2a',
            edgecolor=PURPLE_GLOW, linewidth=1.5
        ),
        zorder=7
    )

    # Casimir axis label (vertical)
    ax.text(
        0.02, 0.5, 'Increasing Casimir eigenvalue  C_2 ->',
        fontsize=8, color=GREY, ha='center', va='center',
        fontfamily='monospace', rotation=90, alpha=0.6
    )

    # ═══════════════════════════════════════════════════════
    #  RIGHT PANEL — The Reality Budget at t=0
    # ═══════════════════════════════════════════════════════
    ax_right_top = fig.add_axes([0.68, 0.52, 0.30, 0.36])
    ax_right_bot = fig.add_axes([0.68, 0.06, 0.30, 0.42])

    # ─── Top: The Budget Equation ───
    ax = ax_right_top
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.text(
        0.5, 0.95, 'THE REALITY BUDGET',
        fontsize=14, fontweight='bold', color=GOLD,
        ha='center', va='top', fontfamily='monospace',
        path_effects=[pe.withStroke(linewidth=1, foreground='#332200')]
    )

    # Main equation
    ax.text(
        0.5, 0.80,
        'Lambda x N = 9/5 = 1.800',
        fontsize=15, fontweight='bold', color=WHITE,
        ha='center', va='center', fontfamily='monospace',
        bbox=dict(
            boxstyle='round,pad=0.4', facecolor='#1a1a3a',
            edgecolor=GOLD, linewidth=2.5
        )
    )

    # The N=0 contradiction
    ax.text(
        0.5, 0.62,
        'If N = 0:',
        fontsize=12, color=GREY, ha='center', va='center',
        fontfamily='monospace'
    )
    ax.text(
        0.5, 0.52,
        'Lambda x 0 = 0  !=  9/5',
        fontsize=14, fontweight='bold', color=RED_WARN,
        ha='center', va='center', fontfamily='monospace',
        bbox=dict(
            boxstyle='round,pad=0.3', facecolor='#2a0a0a',
            edgecolor=RED_WARN, linewidth=2
        )
    )

    # Big red X
    ax.text(
        0.5, 0.37,
        'X', fontsize=60, fontweight='bold', color=RED_WARN,
        ha='center', va='center', fontfamily='sans-serif',
        alpha=0.4, zorder=1,
        path_effects=[pe.withStroke(linewidth=4, foreground=RED_DEEP)]
    )
    ax.text(
        0.5, 0.37,
        'CONTRADICTION', fontsize=11, fontweight='bold',
        color=RED_WARN, ha='center', va='center',
        fontfamily='monospace', zorder=2
    )

    # Therefore
    ax.text(
        0.5, 0.18,
        'Therefore: N >= 2 always',
        fontsize=12, fontweight='bold', color=GREEN_OK,
        ha='center', va='center', fontfamily='monospace',
        bbox=dict(
            boxstyle='round,pad=0.3', facecolor='#0a2a0a',
            edgecolor=GREEN_OK, linewidth=1.5
        )
    )
    ax.text(
        0.5, 0.06,
        '"Nothing" is not a valid state on D_IV^5',
        fontsize=8, color=GOLD_DIM, ha='center', va='center',
        fontfamily='monospace', style='italic'
    )

    # ─── Bottom: Timeline from N=2 to N=10^121 ───
    ax = ax_right_bot
    ax.set_facecolor(DARK_PANEL)

    epochs = universe.epoch_table()
    log_N = [e['log10_N'] for e in epochs]
    log_Lambda = [np.log10(e['Lambda']) for e in epochs]

    # Plot Lambda vs log10(N)
    ax.plot(log_N, log_Lambda, color=BLUE_GLOW, linewidth=2.5, zorder=5)
    ax.fill_between(log_N, log_Lambda, min(log_Lambda) - 5,
                     alpha=0.08, color=BLUE_GLOW)

    # Mark each epoch
    epoch_colors = [PURPLE_GLOW, ORANGE_GLOW, GREEN_OK, CYAN, GOLD, GREY]
    for i, (e, color) in enumerate(zip(epochs, epoch_colors)):
        ax.plot(
            e['log10_N'], np.log10(e['Lambda']),
            'o', color=color, markersize=8, zorder=6
        )
        # Epoch label
        y_offset = 4 if i % 2 == 0 else -6
        ax.annotate(
            e['epoch'],
            xy=(e['log10_N'], np.log10(e['Lambda'])),
            xytext=(0, y_offset), textcoords='offset points',
            fontsize=7, color=color, fontfamily='monospace',
            ha='center', va='bottom' if y_offset > 0 else 'top',
            fontweight='bold'
        )

    # Mark N=0 with red X
    ax.text(
        -5, np.log10(epochs[0]['Lambda']),
        'N=0', fontsize=10, fontweight='bold', color=RED_WARN,
        ha='center', va='center', fontfamily='monospace',
        zorder=7
    )
    ax.text(
        -5, np.log10(epochs[0]['Lambda']) - 4,
        'X', fontsize=30, fontweight='bold', color=RED_WARN,
        ha='center', va='center', fontfamily='sans-serif',
        alpha=0.6, zorder=6,
        path_effects=[pe.withStroke(linewidth=3, foreground=RED_DEEP)]
    )

    ax.set_xlabel('log_10(N)', fontsize=9, color=GREY, fontfamily='monospace')
    ax.set_ylabel('log_10(Lambda)', fontsize=9, color=GREY, fontfamily='monospace')
    ax.set_title(
        'LAMBDA DECREASES AS N GROWS',
        fontsize=10, fontweight='bold', color=BLUE_GLOW,
        fontfamily='monospace', pad=8
    )
    ax.tick_params(colors=GREY, labelsize=7)
    for spine in ax.spines.values():
        spine.set_color('#333355')
    ax.set_xlim(-10, 130)

    # Annotation: constant product
    ax.text(
        65, np.log10(epochs[0]['Lambda']) - 10,
        'Product Lambda * N = 9/5 = const',
        fontsize=8, color=GOLD_DIM, ha='center', va='center',
        fontfamily='monospace', style='italic',
        bbox=dict(
            boxstyle='round,pad=0.2', facecolor='#1a1a0a',
            edgecolor=GOLD_DIM, linewidth=1, alpha=0.8
        )
    )

    # ─── Casimir spectrum inset (small, upper-right of center panel) ───
    # Show C_2(k) = k(k-5) as a parabola with marked points
    ax_inset = fig.add_axes([0.37, 0.72, 0.12, 0.14])
    ax_inset.set_facecolor('#0a0a2a')

    k_cont = np.linspace(-1, 8, 200)
    c2_cont = k_cont * (k_cont - n_C)

    ax_inset.plot(k_cont, c2_cont, color=GREY_DIM, linewidth=1.5, alpha=0.6)
    ax_inset.axhline(y=0, color=GREY_DIM, linewidth=0.5, alpha=0.4)

    # Mark cascade points
    for stage in cascade:
        k = stage['k']
        c2 = stage['C2']
        color = stage['color']
        ax_inset.plot(k, c2, 'o', color=color, markersize=6, zorder=5)
        ax_inset.text(
            k + 0.3, c2, f'k={k}', fontsize=6, color=color,
            fontfamily='monospace', va='center'
        )

    # Wallach set shading
    ax_inset.axvspan(
        WALLACH_MIN, 8, alpha=0.08, color=GREEN_OK,
        label='Wallach set'
    )
    ax_inset.text(
        5.5, -7, 'Wallach', fontsize=5, color=GREEN_OK,
        fontfamily='monospace', ha='center', alpha=0.7
    )

    ax_inset.set_xlabel('k', fontsize=7, color=GREY, fontfamily='monospace')
    ax_inset.set_ylabel('C_2', fontsize=7, color=GREY, fontfamily='monospace')
    ax_inset.set_title(
        'C_2 = k(k-5)', fontsize=7, color=GREY,
        fontfamily='monospace', pad=2
    )
    ax_inset.tick_params(colors=GREY, labelsize=5)
    for spine in ax_inset.spines.values():
        spine.set_color('#333355')
    ax_inset.set_xlim(-1, 8)
    ax_inset.set_ylim(-8, 10)

    # ─── Curvature inset (small, showing the hilltop analogy) ───
    ax_hill = fig.add_axes([0.37, 0.53, 0.12, 0.14])
    ax_hill.set_facecolor('#0a0a2a')

    x_hill = np.linspace(-2, 2, 200)
    y_hill = -x_hill**2 / 7.0  # Inverted parabola ~ negative curvature

    ax_hill.fill_between(x_hill, y_hill, min(y_hill) - 0.1,
                          alpha=0.1, color=RED_WARN)
    ax_hill.plot(x_hill, y_hill, color=RED_WARN, linewidth=2)

    # Ball at the top
    ax_hill.plot(0, 0, 'o', color=GOLD, markersize=8, zorder=5)
    ax_hill.annotate(
        '', xy=(0.8, -0.8**2 / 7), xytext=(0, 0),
        arrowprops=dict(arrowstyle='->', color=ORANGE_GLOW, lw=2),
    )
    ax_hill.annotate(
        '', xy=(-0.8, -0.8**2 / 7), xytext=(0, 0),
        arrowprops=dict(arrowstyle='->', color=ORANGE_GLOW, lw=2),
    )

    ax_hill.set_title(
        'Hilltop (H = -2/7)', fontsize=7, color=RED_WARN,
        fontfamily='monospace', pad=2
    )
    ax_hill.tick_params(colors=GREY, labelsize=5)
    for spine in ax_hill.spines.values():
        spine.set_color('#333355')
    ax_hill.set_xlim(-2, 2)

    # ─── Initial state callout (between center and right panels) ───
    ax_init = fig.add_axes([0.52, 0.06, 0.14, 0.10])
    ax_init.set_facecolor(BG)
    ax_init.set_xlim(0, 1)
    ax_init.set_ylim(0, 1)
    ax_init.axis('off')

    init = universe.initial_N()
    ax_init.text(
        0.5, 0.85, 'AT t = 0:',
        fontsize=9, fontweight='bold', color=WHITE,
        ha='center', va='top', fontfamily='monospace'
    )
    ax_init.text(
        0.5, 0.55, f'N = {init["N"]}',
        fontsize=14, fontweight='bold', color=PURPLE_GLOW,
        ha='center', va='center', fontfamily='monospace'
    )
    ax_init.text(
        0.5, 0.25, f'Lambda = {init["Lambda"]:.2f}',
        fontsize=10, color=BLUE_GLOW,
        ha='center', va='center', fontfamily='monospace'
    )
    ax_init.text(
        0.5, 0.05, init['pair'],
        fontsize=8, color=GREY,
        ha='center', va='center', fontfamily='monospace',
        style='italic'
    )

    plt.show()


# ═══════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    # ─── Programmatic report ───
    universe = SelfStartingUniverse()
    print(universe.report())

    # ─── Quick API smoke test ───
    print('\n--- API smoke test ---')
    assert universe.is_frozen_valid() is False
    assert len(universe.frozen_state_arguments()) == 4
    assert abs(universe.spreading_time() - np.sqrt(7 / 2)) < 1e-12
    assert abs(universe.casimir(6) - 6) < 1e-12
    assert abs(universe.casimir(1) - (-4)) < 1e-12
    assert abs(universe.casimir(0) - 0) < 1e-12
    assert abs(universe.casimir(3) - (-6)) < 1e-12
    t_test = np.array([0, 1, 2])
    J = universe.jacobi_growth(t_test)
    assert abs(J[0] - 1.0) < 1e-12
    assert J[1] > 1.0
    assert J[2] > J[1]
    init = universe.initial_N()
    assert init['N'] == 2
    assert abs(init['Lambda'] - 0.9) < 1e-12
    cascade = universe.commitment_cascade()
    assert len(cascade) == 4
    assert cascade[-1]['k'] == 6
    epochs = universe.epoch_table()
    assert len(epochs) >= 5
    print('All API tests passed.')
    print()

    # ─── Launch visualization ───
    print('Launching visualization...')
    build_visualization()
