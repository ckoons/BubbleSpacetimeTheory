#!/usr/bin/env python3
"""
THE GODEL LIMIT
===============
The universe can never know more than 19.1% of itself.

If  Lambda x N_total = N_c^2/n_C = 9/5  is exactly conserved, and
de Sitter capacity is  S_dS = 3 pi / Lambda, then the fill fraction:

    f = N / S_dS = N Lambda / (3 pi) = (9/5) / (3 pi) = N_c / (n_C pi)
      = 3 / (5 pi)  ~  19.10%

This is not a snapshot. It is a STRUCTURAL CONSTANT. The universe is
always 19.1% committed (known) and 80.9% uncommitted (dark/unknown).

The jar grows exactly as fast as you fill it. The loading bar is stuck
at 19.1% forever. Complete self-knowledge would require Lambda -> 0,
which destroys the vacuum that sustains existence.

    "The universe exists because it cannot fully know itself,
     and it cannot fully know itself because it exists.
     The ratio of knowledge to ignorance is N_c/(n_C pi)
     -- set by color, dimension, and the circle."

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
from matplotlib.animation import FuncAnimation
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Rectangle


# ============================================================
#  CI INTERFACE — GodelLimit class
# ============================================================

class GodelLimit:
    """Programmatic interface to BST's Godel Limit."""

    N_c = 3
    n_C = 5

    @property
    def budget_product(self):
        """Lambda x N_total = N_c^2 / n_C = 9/5 = 1.800 exactly."""
        return self.N_c ** 2 / self.n_C

    @property
    def fill_fraction(self):
        """f = N_c / (n_C pi) = 3/(5 pi) ~ 0.19099."""
        return self.N_c / (self.n_C * np.pi)

    @property
    def dark_fraction(self):
        """1 - f ~ 0.80901.  The forever-unknowable portion."""
        return 1.0 - self.fill_fraction

    # ----- core arguments -----

    def why_not_100_percent(self):
        """Why can't the fill fraction reach 100%?"""
        lines = [
            "WHY NOT 100%?",
            "=============",
            "",
            "Lambda x N_total = 9/5  (exactly conserved).",
            "",
            "If N grows (more commitments), Lambda must shrink.",
            "But S_dS = 3 pi / Lambda, so the de Sitter capacity grows too.",
            "",
            "  f = N / S_dS = N Lambda / (3 pi) = (9/5) / (3 pi) = 3/(5 pi)",
            "",
            "The jar grows EXACTLY as fast as you fill it.",
            f"Fill fraction is frozen at {self.fill_fraction:.5f} = 19.10% forever.",
            "",
            "To reach f = 100%, you would need Lambda -> 0.",
            "But Lambda = 0 means no vacuum energy, no de Sitter horizon,",
            "no causal structure -- existence itself ceases.",
            "",
            "The universe exists BECAUSE it cannot fully know itself.",
        ]
        msg = "\n".join(lines)
        print(msg)
        return msg

    def godel_parallel(self):
        """Side-by-side comparison: Godel (1931) <-> BST."""
        rows = [
            ("Formal system",             "Universe"),
            ("Provable statements",       "Committed correlations"),
            ("True but unprovable",       "Dark sector (80.9%)"),
            ("Incompleteness for consistency", "Ignorance for existence"),
            ("Godel number",              "N_total"),
            ("Decidability limit",        f"Fill fraction 3/(5 pi) = {self.fill_fraction:.5f}"),
        ]
        header = f"{'Godel (1931)':<38} {'BST':<38}"
        sep = "-" * 78
        lines = ["THE GODEL PARALLEL", "=" * 18, "", header, sep]
        for left, right in rows:
            lines.append(f"{left:<38} {right:<38}")
        lines += [
            sep, "",
            "If the universe achieved complete self-knowledge (f -> 100%),",
            "Lambda -> 0, and existence ceases.",
        ]
        msg = "\n".join(lines)
        print(msg)
        return msg

    def is_fill_evolving(self):
        """Does the fill fraction change with time?  No."""
        return False

    def fill_at(self, Lambda=2.9e-122):
        """Fill fraction at any value of Lambda.  Always 3/(5 pi)."""
        N = self.budget_product / Lambda
        S_dS = 3.0 * np.pi / Lambda
        f = N / S_dS
        return f  # = 3/(5 pi) always

    def cosmic_coincidence(self):
        """Why Lambda ~ rho_matter NOW?  Because it is ALWAYS ~19.1%."""
        lines = [
            "THE COSMIC COINCIDENCE -- RESOLVED",
            "=" * 34,
            "",
            "Standard cosmology asks: why is Lambda ~ rho_matter right NOW?",
            "This seems like a spectacular fine-tuning.",
            "",
            "BST answer: it is not a coincidence. It is not 'now'.",
            f"The fill fraction f = {self.fill_fraction:.5f} is a STRUCTURAL CONSTANT.",
            "The universe is ALWAYS ~19.1% committed and ~80.9% dark.",
            "",
            "Lambda shrinks as N grows, but S_dS = 3 pi / Lambda grows",
            "in exact proportion.  The ratio is frozen by geometry.",
            "",
            f"  f = N_c / (n_C pi) = {self.N_c}/({self.n_C} pi) = {self.fill_fraction:.5f}",
            "",
            "There is no coincidence to explain.",
        ]
        msg = "\n".join(lines)
        print(msg)
        return msg

    def dark_sector_size(self, Lambda=2.9e-122):
        """De Sitter capacity: S_dS = 3 pi / Lambda."""
        return 3.0 * np.pi / Lambda

    def committed_count(self, Lambda=2.9e-122):
        """Number of committed correlations: N = 9 / (5 Lambda)."""
        return self.budget_product / Lambda

    def show(self):
        """Launch the visual interface."""
        _launch_visual()


# ============================================================
#  COLORS AND CONSTANTS
# ============================================================

BG          = '#0a0a1a'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BLUE_GLOW   = '#4488ff'
PURPLE_DEEP = '#2a1040'
PURPLE_GLOW = '#9955dd'
PURPLE_VOID = '#12082a'
ORANGE_GLOW = '#ff8800'
WHITE       = '#ffffff'
GREY        = '#888888'
SOFT_GREEN  = '#66dd88'
SOFT_CYAN   = '#55cccc'

N_c = 3
n_C = 5
BUDGET       = N_c ** 2 / n_C              # 9/5 = 1.800
FILL_FRAC    = N_c / (n_C * np.pi)         # 3/(5 pi) ~ 0.19099
DARK_FRAC    = 1.0 - FILL_FRAC             # ~ 0.80901


# ============================================================
#  DRAWING HELPERS
# ============================================================

def _draw_progress_bar(ax):
    """The haunting progress bar -- stuck at 19.1% forever."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Title above bar
    ax.text(0.5, 0.92, f'UNIVERSE KNOWLEDGE:  {FILL_FRAC*100:.1f}%',
            fontsize=24, fontweight='bold', color=GOLD, ha='center', va='center',
            fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=3, foreground='#443300')])

    # The bar itself -- large and dramatic
    bar_x, bar_y = 0.05, 0.38
    bar_w, bar_h = 0.90, 0.30

    # Outer frame (dark border glow)
    frame = FancyBboxPatch((bar_x - 0.005, bar_y - 0.005),
                            bar_w + 0.01, bar_h + 0.01,
                            boxstyle="round,pad=0.008",
                            facecolor='none', edgecolor='#333355',
                            linewidth=3, zorder=0)
    ax.add_patch(frame)

    # Background: void purple -- the unknowable
    bg_bar = FancyBboxPatch((bar_x, bar_y), bar_w, bar_h,
                             boxstyle="round,pad=0.005",
                             facecolor=PURPLE_VOID, edgecolor='#222244',
                             linewidth=2, zorder=1)
    ax.add_patch(bg_bar)

    # Fill: golden light -- the known
    fill_w = bar_w * FILL_FRAC
    fill = Rectangle((bar_x + 0.003, bar_y + 0.003),
                      fill_w - 0.003, bar_h - 0.006,
                      facecolor='#cc9900', edgecolor='none',
                      alpha=0.9, zorder=2)
    ax.add_patch(fill)

    # Inner glow layers on the fill
    for i in range(6):
        alpha_i = 0.25 * (1.0 - i / 6)
        inset = 0.01 * (i + 1)
        glow = Rectangle((bar_x + 0.003 + inset, bar_y + 0.003 + inset),
                           max(0.001, fill_w - 0.003 - 2 * inset),
                           max(0.001, bar_h - 0.006 - 2 * inset),
                           facecolor=GOLD, edgecolor='none',
                           alpha=alpha_i, zorder=3)
        ax.add_patch(glow)

    # Edge glow -- bright line at the boundary between known and unknown
    edge_x = bar_x + fill_w
    ax.plot([edge_x, edge_x], [bar_y + 0.01, bar_y + bar_h - 0.01],
            color=GOLD, linewidth=3, alpha=0.9, zorder=5)
    ax.plot([edge_x, edge_x], [bar_y + 0.02, bar_y + bar_h - 0.02],
            color=WHITE, linewidth=1.5, alpha=0.6, zorder=6)

    # Label inside the filled zone
    if fill_w > 0.06:
        ax.text(bar_x + fill_w * 0.5, bar_y + bar_h * 0.5,
                f'{FILL_FRAC*100:.1f}%', fontsize=18, fontweight='bold',
                color='#1a0a00', ha='center', va='center', fontfamily='monospace',
                zorder=7)

    # Label inside the dark zone
    dark_center_x = bar_x + fill_w + (bar_w - fill_w) * 0.5
    ax.text(dark_center_x, bar_y + bar_h * 0.5,
            f'{DARK_FRAC*100:.1f}%  DARK',
            fontsize=16, fontweight='bold', color='#443366', ha='center',
            va='center', fontfamily='monospace', alpha=0.7, zorder=7)

    # Scatter dim dots in the dark region -- the unknowable
    rng = np.random.RandomState(42)
    n_dots = 60
    dot_x = rng.uniform(edge_x + 0.02, bar_x + bar_w - 0.02, n_dots)
    dot_y = rng.uniform(bar_y + 0.04, bar_y + bar_h - 0.04, n_dots)
    dot_alpha = rng.uniform(0.05, 0.25, n_dots)
    for dx, dy, da in zip(dot_x, dot_y, dot_alpha):
        ax.plot(dx, dy, 'o', color=PURPLE_GLOW, markersize=2, alpha=da, zorder=4)

    # Subtitle below bar
    ax.text(0.5, 0.22,
            'THE  GODEL  LIMIT',
            fontsize=16, fontweight='bold', color='#ccaa44', ha='center',
            va='center', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=2, foreground='#332200')])
    ax.text(0.5, 0.10,
            'The universe can never know more than  N_c / (n_C pi)  of itself',
            fontsize=11, color=GOLD_DIM, ha='center', va='center',
            fontfamily='monospace', style='italic')


def _draw_argument(ax, time_frac):
    """Left panel: 'The Argument' -- why the fill fraction is frozen."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.text(0.5, 0.97, 'THE ARGUMENT', fontsize=13, fontweight='bold',
            color=GOLD, ha='center', va='top', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])

    # The logical chain
    steps = [
        ("Start:",   "Lambda x N = 9/5  (conserved)", GOLD),
        ("Step 1:",  "N grows -> Lambda must shrink",  SOFT_CYAN),
        ("Step 2:",  "S_dS = 3 pi/Lambda grows",      SOFT_CYAN),
        ("Step 3:",  "f = N/S_dS = 9/(5 x 3 pi)",     SOFT_CYAN),
        ("Step 4:",  "= 3/(5 pi) = CONSTANT!",         GOLD),
    ]
    y0 = 0.87
    for i, (label, text, color) in enumerate(steps):
        y = y0 - i * 0.075
        ax.text(0.05, y, label, fontsize=8, fontweight='bold', color=color,
                ha='left', va='center', fontfamily='monospace')
        ax.text(0.30, y, text, fontsize=8, color=color,
                ha='left', va='center', fontfamily='monospace')
        # Connecting arrow
        if i < len(steps) - 1:
            ax.annotate('', xy=(0.15, y - 0.055), xytext=(0.15, y - 0.015),
                        arrowprops=dict(arrowstyle='->', color='#555577',
                                        lw=1.2))

    # Conclusion box
    ax.text(0.5, 0.45, 'The jar grows EXACTLY as\nfast as you fill it.',
            fontsize=9, fontweight='bold', color=SOFT_GREEN,
            ha='center', va='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a0a',
                      edgecolor=SOFT_GREEN, linewidth=1.5),
            linespacing=1.6)

    # Visual: the growing jar
    _draw_jar_visual(ax, time_frac)


def _draw_jar_visual(ax, time_frac):
    """Draw a jar that grows as it fills -- water level stays at 19.1%."""
    # Jar dimensions scale with time_frac
    base_w = 0.15
    base_h = 0.10
    scale = 0.5 + 0.5 * time_frac  # jar grows from 50% to 100% size

    jar_w = base_w * scale
    jar_h = base_h * scale
    jar_cx = 0.50
    jar_bot = 0.08

    # Jar outline
    jar_left = jar_cx - jar_w
    jar_right = jar_cx + jar_w

    # Simple jar shape
    jar_outline_x = [jar_left, jar_left, jar_right, jar_right, jar_left]
    jar_outline_y = [jar_bot, jar_bot + jar_h * 2, jar_bot + jar_h * 2,
                     jar_bot, jar_bot]
    ax.plot(jar_outline_x, jar_outline_y, color='#4466aa', linewidth=2,
            alpha=0.7, zorder=5)

    # Water fill at 19.1%
    water_h = jar_h * 2 * FILL_FRAC
    water = Rectangle((jar_left + 0.005, jar_bot + 0.002),
                        2 * jar_w - 0.01, water_h,
                        facecolor='#2244aa', edgecolor='none',
                        alpha=0.5, zorder=4)
    ax.add_patch(water)

    # Water surface shimmer
    ax.plot([jar_left + 0.01, jar_right - 0.01],
            [jar_bot + water_h, jar_bot + water_h],
            color=BLUE_GLOW, linewidth=1.5, alpha=0.6, zorder=6)

    # Label
    pct_str = f'{FILL_FRAC*100:.1f}%'
    ax.text(jar_cx, jar_bot + jar_h * 2 + 0.02, pct_str,
            fontsize=8, color=BLUE_GLOW, ha='center', va='bottom',
            fontfamily='monospace', fontweight='bold')

    # Caption
    ax.text(0.5, 0.02, 'jar grows -- water level\nstays at 19.1%',
            fontsize=7, color=GREY, ha='center', va='bottom',
            fontfamily='monospace', style='italic', linespacing=1.4)


def _draw_godel_table(ax):
    """Center panel: The Godel Parallel -- side-by-side table."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.text(0.5, 0.97, 'THE GODEL PARALLEL', fontsize=13, fontweight='bold',
            color=GOLD, ha='center', va='top', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])

    # Column headers
    ax.text(0.25, 0.88, 'Godel (1931)', fontsize=10, fontweight='bold',
            color=PURPLE_GLOW, ha='center', va='center', fontfamily='monospace')
    ax.text(0.75, 0.88, 'BST', fontsize=10, fontweight='bold',
            color=GOLD, ha='center', va='center', fontfamily='monospace')

    # Separator line
    ax.plot([0.05, 0.95], [0.85, 0.85], color='#333355', linewidth=1)

    rows = [
        ("Formal system",               "Universe"),
        ("Provable statements",          "Committed correlations"),
        ("True but unprovable",          "Dark sector (80.9%)"),
        ("Incompleteness",               "Ignorance for existence"),
        ("  for consistency",            ""),
        ("Godel number",                 "N_total"),
        ("Decidability limit",           "Fill = 3/(5 pi) = 19.1%"),
    ]

    y0 = 0.80
    dy = 0.065
    for i, (left, right) in enumerate(rows):
        y = y0 - i * dy
        color_l = '#bb88ee' if left.startswith("  ") else '#ccaaff'
        color_r = '#ddcc88'
        ax.text(0.03, y, left, fontsize=8, color=color_l,
                ha='left', va='center', fontfamily='monospace')
        ax.text(0.52, y, right, fontsize=8, color=color_r,
                ha='left', va='center', fontfamily='monospace')
        if not left.startswith("  "):
            ax.plot([0.05, 0.95], [y - 0.025, y - 0.025],
                    color='#1a1a33', linewidth=0.5)

    # The devastating conclusion
    conclusion_y = 0.26
    ax.plot([0.08, 0.92], [conclusion_y + 0.05, conclusion_y + 0.05],
            color='#333355', linewidth=1)

    ax.text(0.5, conclusion_y,
            'If the universe achieved complete\n'
            'self-knowledge (f -> 100%),\n'
            'Lambda -> 0, and existence ceases.',
            fontsize=9, color='#ff6666', ha='center', va='center',
            fontfamily='monospace', linespacing=1.6,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1a0808',
                      edgecolor='#ff4444', linewidth=1.5, alpha=0.85))

    # The deepest sentence
    ax.text(0.5, 0.06,
            '"The universe exists because it\n'
            ' cannot fully know itself."',
            fontsize=9, fontweight='bold', color=GOLD_DIM, ha='center',
            va='center', fontfamily='monospace', style='italic',
            linespacing=1.5)


def _draw_numbers(ax, time_frac):
    """Right panel: The Numbers -- exact values and current epoch."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.text(0.5, 0.97, 'THE NUMBERS', fontsize=13, fontweight='bold',
            color=GOLD, ha='center', va='top', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])

    # Structural constants
    entries = [
        ("N_c",             f"{N_c}",                           '#aaaaff'),
        ("n_C",             f"{n_C}",                           '#aaaaff'),
        ("Budget",          f"N_c^2/n_C = 9/5 = {BUDGET:.3f}", GOLD),
        ("Fill fraction",   f"3/(5 pi) = {FILL_FRAC:.5f}",     GOLD),
        ("Dark fraction",   f"1 - f  = {DARK_FRAC:.5f}",       PURPLE_GLOW),
    ]

    y0 = 0.87
    for i, (label, value, color) in enumerate(entries):
        y = y0 - i * 0.065
        ax.text(0.05, y, label + ":", fontsize=8, color=GREY,
                ha='left', va='center', fontfamily='monospace')
        ax.text(0.95, y, value, fontsize=8, fontweight='bold', color=color,
                ha='right', va='center', fontfamily='monospace')

    # Separator
    ax.plot([0.05, 0.95], [0.53, 0.53], color='#333355', linewidth=1)

    # Current epoch values (from slider)
    Lambda_now = 2.9e-122
    # Interpolate for the slider: use log scale
    log_L_min = -130.0
    log_L_max = np.log10(Lambda_now)
    log_L = log_L_min + (log_L_max - log_L_min) * time_frac
    Lambda = 10.0 ** log_L
    N = BUDGET / Lambda
    S_dS = 3.0 * np.pi / Lambda
    f = N / S_dS

    ax.text(0.5, 0.48, 'Current Epoch', fontsize=10, fontweight='bold',
            color=SOFT_CYAN, ha='center', va='center', fontfamily='monospace')

    epoch_entries = [
        ("Lambda",   f"{Lambda:.2e}",   BLUE_GLOW),
        ("N_total",  f"{N:.2e}",        ORANGE_GLOW),
        ("S_dS",     f"{S_dS:.2e}",     PURPLE_GLOW),
        ("f = N/S",  f"{f:.5f}",        GOLD),
    ]

    y1 = 0.41
    for i, (label, value, color) in enumerate(epoch_entries):
        y = y1 - i * 0.060
        ax.text(0.05, y, label + ":", fontsize=8, color=GREY,
                ha='left', va='center', fontfamily='monospace')
        ax.text(0.95, y, value, fontsize=8, fontweight='bold', color=color,
                ha='right', va='center', fontfamily='monospace')

    # Note about golden ratio proximity
    ax.plot([0.05, 0.95], [0.15, 0.15], color='#333355', linewidth=0.5)

    phi = (np.sqrt(5) - 1) / 2  # golden ratio conjugate
    ax.text(0.5, 0.10,
            f'Note: dark = {DARK_FRAC:.5f}',
            fontsize=8, color=GREY, ha='center', va='center',
            fontfamily='monospace')
    ax.text(0.5, 0.05,
            f'phi = (sqrt5-1)/2 = {phi:.5f}',
            fontsize=8, color=GREY, ha='center', va='center',
            fontfamily='monospace')
    ax.text(0.5, 0.00,
            '(open question)', fontsize=7, color='#555555',
            ha='center', va='center', fontfamily='monospace', style='italic')


def _draw_bottom_panel(ax, time_frac):
    """Bottom: the timeline and the pinned fill fraction."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Draw a timeline bar
    tl_x, tl_y = 0.05, 0.70
    tl_w, tl_h = 0.90, 0.08

    # Timeline background
    tl_bg = Rectangle((tl_x, tl_y), tl_w, tl_h,
                        facecolor='#111133', edgecolor='#333355',
                        linewidth=1.5, zorder=1)
    ax.add_patch(tl_bg)

    # Cursor position
    cursor_x = tl_x + tl_w * time_frac
    ax.plot([cursor_x, cursor_x], [tl_y - 0.02, tl_y + tl_h + 0.02],
            color=GOLD, linewidth=2.5, zorder=5)
    ax.plot(cursor_x, tl_y + tl_h + 0.05, 'v', color=GOLD,
            markersize=8, zorder=5)

    # Labels
    ax.text(tl_x, tl_y - 0.06, 'Big Bang', fontsize=8, color=ORANGE_GLOW,
            ha='left', va='center', fontfamily='monospace')
    ax.text(tl_x + tl_w, tl_y - 0.06, 'Far Future', fontsize=8,
            color=BLUE_GLOW, ha='right', va='center', fontfamily='monospace')
    ax.text(0.5, tl_y - 0.06, 'NOW', fontsize=8, color=GREY,
            ha='center', va='center', fontfamily='monospace')

    # Tick marks on timeline
    for frac in np.linspace(0, 1, 21):
        tx = tl_x + tl_w * frac
        ax.plot([tx, tx], [tl_y, tl_y + 0.02], color='#444466',
                linewidth=0.5, zorder=2)

    # Fill fraction indicator pinned above timeline
    # Small progress bar that tracks the slider but NEVER changes its fill
    mini_x = 0.30
    mini_w = 0.40
    mini_y = 0.35
    mini_h = 0.15

    mini_bg = FancyBboxPatch((mini_x, mini_y), mini_w, mini_h,
                              boxstyle="round,pad=0.005",
                              facecolor=PURPLE_VOID, edgecolor='#333355',
                              linewidth=1.5, zorder=1)
    ax.add_patch(mini_bg)

    mini_fill = Rectangle((mini_x + 0.002, mini_y + 0.002),
                            (mini_w - 0.004) * FILL_FRAC, mini_h - 0.004,
                            facecolor='#cc9900', edgecolor='none',
                            alpha=0.85, zorder=2)
    ax.add_patch(mini_fill)

    # Glow at edge
    edge_x = mini_x + 0.002 + (mini_w - 0.004) * FILL_FRAC
    ax.plot([edge_x, edge_x], [mini_y + 0.01, mini_y + mini_h - 0.01],
            color=GOLD, linewidth=2, alpha=0.8, zorder=3)

    ax.text(mini_x + (mini_w * FILL_FRAC) * 0.5, mini_y + mini_h * 0.5,
            f'{FILL_FRAC*100:.1f}%', fontsize=10, fontweight='bold',
            color='#1a0a00', ha='center', va='center',
            fontfamily='monospace', zorder=4)

    ax.text(mini_x + mini_w + 0.03, mini_y + mini_h * 0.5,
            'PINNED', fontsize=9, fontweight='bold', color=GOLD,
            ha='left', va='center', fontfamily='monospace')

    # The closing sentence
    ax.text(0.5, 0.10,
            '"The more you know, the more there is to know."',
            fontsize=10, color=GOLD_DIM, ha='center', va='center',
            fontfamily='monospace', style='italic')

    ax.text(0.5, 0.00,
            'The universe exists because it cannot fully know itself.',
            fontsize=9, fontweight='bold', color=GOLD, ha='center',
            va='center', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])


# ============================================================
#  VISUAL LAUNCHER
# ============================================================

def _launch_visual():
    """Build and display the full Godel Limit visualization."""

    fig = plt.figure(figsize=(18, 12), facecolor=BG)
    fig.canvas.manager.set_window_title('The Godel Limit -- BST')

    # ---- TOP: The haunting progress bar ----
    ax_bar = fig.add_axes([0.02, 0.75, 0.96, 0.23])
    _draw_progress_bar(ax_bar)

    # ---- LEFT: The Argument ----
    ax_arg = fig.add_axes([0.02, 0.24, 0.30, 0.49])

    # ---- CENTER: Godel Parallel ----
    ax_godel = fig.add_axes([0.35, 0.24, 0.30, 0.49])
    _draw_godel_table(ax_godel)

    # ---- RIGHT: The Numbers ----
    ax_nums = fig.add_axes([0.68, 0.24, 0.30, 0.49])

    # ---- BOTTOM: Timeline + Pinned bar ----
    ax_bot = fig.add_axes([0.02, 0.02, 0.96, 0.20])

    # ---- SLIDER ----
    ax_slider = fig.add_axes([0.15, 0.215, 0.70, 0.018], facecolor='#1a1a3a')
    slider = Slider(ax_slider, '', 0.0, 1.0, valinit=0.7,
                    valstep=0.005, color=ORANGE_GLOW)
    slider.valtext.set_color(WHITE)
    slider.valtext.set_fontfamily('monospace')
    slider.valtext.set_fontsize(8)

    # Slider labels
    fig.text(0.08, 0.224, 'Cosmic Time', fontsize=9, color=GREY,
             ha='right', va='center', fontfamily='monospace')
    fig.text(0.15, 0.205, 'early', fontsize=7, color=ORANGE_GLOW,
             ha='left', va='center', fontfamily='monospace')
    fig.text(0.85, 0.205, 'far future', fontsize=7, color=BLUE_GLOW,
             ha='right', va='center', fontfamily='monospace')

    # ---- State ----
    state = {'time_frac': 0.7, 'auto': False, 'pulse_phase': 0.0}

    def update(time_frac):
        state['time_frac'] = time_frac
        _draw_argument(ax_arg, time_frac)
        _draw_numbers(ax_nums, time_frac)
        _draw_bottom_panel(ax_bot, time_frac)
        fig.canvas.draw_idle()

    def on_slider(val):
        update(val)

    slider.on_changed(on_slider)

    # ---- Subtle pulse animation on the progress bar edge ----
    # Store the edge glow artist for animation
    fill_w = 0.90 * FILL_FRAC
    edge_x = 0.05 + fill_w

    pulse_line, = ax_bar.plot([edge_x, edge_x], [0.39, 0.67],
                               color=WHITE, linewidth=2.0, alpha=0.0,
                               zorder=10)

    def animate(frame):
        # Gentle pulse on the boundary between known and unknown
        state['pulse_phase'] += 0.08
        alpha = 0.15 + 0.15 * np.sin(state['pulse_phase'])
        pulse_line.set_alpha(alpha)

        # Slow auto-advance if enabled
        if state['auto']:
            new_t = state['time_frac'] + 0.002
            if new_t > 1.0:
                new_t = 0.0
            slider.set_val(new_t)

        return [pulse_line]

    # Initial draw
    update(0.7)

    anim = FuncAnimation(fig, animate, interval=60, blit=True,
                          cache_frame_data=False)

    # Store anim to prevent garbage collection
    fig._godel_anim = anim

    plt.show()


# ============================================================
#  MAIN
# ============================================================

if __name__ == '__main__':
    print()
    print("  THE GODEL LIMIT")
    print("  ================")
    print(f"  Fill fraction:  3/(5 pi) = {FILL_FRAC:.5f}  ({FILL_FRAC*100:.2f}%)")
    print(f"  Dark fraction:  1 - f    = {DARK_FRAC:.5f}  ({DARK_FRAC*100:.2f}%)")
    print(f"  Budget:         9/5      = {BUDGET:.3f}")
    print()
    print("  The universe can never know more than 19.1% of itself.")
    print("  The loading bar is stuck forever.")
    print()
    print("  THREE independent derivations of f = 3/(5π):")
    print("    1. Chern classes: f = c₅/(c₁·π)")
    print("    2. Root decomposition: f = N_c/(n_C·π)")
    print("    3. Effective spectral dimension: f = d_eff/(d·π) = 6/(10π)")
    print("       where d_eff = λ₁ = χ = C₂ = 6 (grand identity)")
    print()

    _launch_visual()
