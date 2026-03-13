#!/usr/bin/env python3
"""
THE DARK SECTOR — Permanently Unknowable
=========================================

The fill fraction f = N_c/(n_C pi) = 3/(5pi) = 19.1% is a structural constant.
80.9% of the universe is dark — not because we haven't looked hard enough,
but because the topology FORBIDS observation of it.

The de Sitter entropy S_dS = 3pi/Lambda is the total information capacity.
As Lambda decreases (more commitments accumulate), S_dS grows. But N_total
grows in lockstep: N = (9/5)/Lambda. The ratio N/S_dS = 3/(5pi) NEVER changes.

The cosmic coincidence problem DISSOLVES: People ask "Why does Lambda ~ rho_matter
RIGHT NOW?" BST answers: it's ALWAYS approximately this ratio. There is no
special "now." The 19.1%/80.9% split is eternal.

Dark matter + dark energy combined: In BST, the "dark sector" (80.9%) isn't
a separate substance — it's the uncommitted capacity of the de Sitter horizon.
Dark matter effects arise from the topology of uncommitted channels.
Dark energy IS the Lambda that the reality budget requires.

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
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
from matplotlib.gridspec import GridSpec

# ─── BST Constants ───
N_c = 3          # color charges
n_C = 5          # domain dimension (D_IV^5)
BUDGET = N_c**2 / n_C                   # = 9/5 = 1.800
FILL = N_c / (n_C * np.pi)             # = 3/(5pi) = 0.19099...
DARK = 1.0 - FILL                       # = 0.80901...

# Planck 2018 observed fractions
PLANCK_DE = 0.683    # dark energy (Omega_Lambda)
PLANCK_DM = 0.268    # dark matter (Omega_DM)
PLANCK_VIS = 0.049   # baryonic / visible (Omega_b)
PLANCK_DARK = PLANCK_DE + PLANCK_DM     # = 0.951 total dark (Planck)

# Current cosmological constant (reduced Planck units)
LAMBDA_NOW = 2.888e-122

# ─── Colors ───
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BRIGHT      = '#ffe066'
DEEP_PURPLE = '#1a0033'
VOID_PURPLE = '#2d0050'
BLUE_GLOW   = '#4488ff'
BLUE_DEEP   = '#1a1a6a'
PURPLE_GLOW = '#9955dd'
PURPLE_LINE = '#bb77ff'
RED_WARM    = '#ff6644'
WHITE       = '#ffffff'
GREY        = '#888888'
LIGHT_GREY  = '#bbbbbb'
GREEN_GLOW  = '#44dd88'


# ─── DarkSector Class ───
class DarkSector:
    """
    BST Dark Sector calculator.

    The fill fraction f = N_c/(n_C pi) = 3/(5pi) = 19.1% is a topological
    constant. The dark sector (80.9%) is permanently unknowable — not hidden,
    but topologically forbidden from observation.
    """

    def __init__(self):
        self.N_c = N_c
        self.n_C = n_C
        self.budget = BUDGET
        self.visible_fraction = FILL
        self.dark_fraction = DARK

    def at_epoch(self, Lambda):
        """
        Compute quantities at a given cosmological constant Lambda.

        Returns: dict with S_dS, N_total, fill, visible, dark
        """
        if Lambda <= 0:
            raise ValueError("Lambda must be positive")
        N_total = self.budget / Lambda
        S_dS = 3.0 * np.pi / Lambda
        f = N_total / S_dS              # = budget/(3*pi) = 3/(5*pi) always
        return {
            'Lambda': Lambda,
            'S_dS': S_dS,
            'N_total': N_total,
            'fill': f,
            'visible': f,
            'dark': 1.0 - f
        }

    def coincidence_ratio(self):
        """
        Why Omega_Lambda / Omega_m ~ 7/3 now.
        In BST: the ratio is structural, arising from genus/N_c = 7/3.
        """
        return 7.0 / 3.0    # ~ 2.333, close to observed 0.683/0.317 = 2.15

    def is_coincidence_fine_tuned(self):
        """Is the cosmic coincidence fine-tuned? NO — it is structural."""
        return False

    def evolve(self, Lambda_start=1e-50, Lambda_end=1e-200, steps=100):
        """
        Evolve through cosmic history. Fill fraction is CONSTANT.

        Returns: list of dicts with (Lambda, N_total, S_dS, fill)
        """
        log_start = np.log10(Lambda_start)
        log_end = np.log10(Lambda_end)
        lambdas = np.logspace(log_start, log_end, steps)
        result = []
        for L in lambdas:
            N = self.budget / L
            S = 3.0 * np.pi / L
            f = N / S
            result.append({
                'Lambda': L,
                'N_total': N,
                'S_dS': S,
                'fill': f
            })
        return result

    def planck_dark_energy(self):
        """Planck 2018 observed dark energy fraction."""
        return PLANCK_DE

    def planck_dark_matter(self):
        """Planck 2018 observed dark matter fraction."""
        return PLANCK_DM

    def planck_visible(self):
        """Planck 2018 observed visible (baryonic) fraction."""
        return PLANCK_VIS

    def bst_prediction(self):
        """
        BST prediction: 19.1% visible, 80.9% dark (combined DE + DM).
        """
        return {
            'visible': self.visible_fraction,
            'dark': self.dark_fraction,
            'formula': 'f = N_c / (n_C * pi) = 3 / (5*pi)'
        }

    def __repr__(self):
        return (
            f"DarkSector(\n"
            f"  visible = {self.visible_fraction:.5f} = 3/(5pi) = {100*self.visible_fraction:.1f}%\n"
            f"  dark    = {self.dark_fraction:.5f}            = {100*self.dark_fraction:.1f}%\n"
            f"  budget  = {self.budget:.3f} = N_c^2/n_C = 9/5\n"
            f")"
        )


# ─── Helpers ───
def glow_text(ax, x, y, text, color=WHITE, fontsize=12, ha='center', va='center',
              weight='normal', alpha=1.0, glow_color=None, glow_width=3, **kwargs):
    """Place text with a soft glow effect."""
    gc = glow_color or color
    t = ax.text(x, y, text, color=color, fontsize=fontsize, ha=ha, va=va,
                weight=weight, alpha=alpha, **kwargs)
    t.set_path_effects([
        pe.withStroke(linewidth=glow_width, foreground=gc, alpha=0.3),
        pe.Normal()
    ])
    return t


# ─── Evolution Data ───
def compute_evolution(n_points=500):
    """
    Compute the evolution from early universe to far future.
    Uses log(1/Lambda) as cosmic time proxy.
    """
    log_inv_lambda = np.linspace(10, 250, n_points)   # log10(1/Lambda)
    lambdas = 10.0 ** (-log_inv_lambda)

    N_total = BUDGET / lambdas
    S_dS = 3.0 * np.pi / lambdas
    fill = N_total / S_dS      # constant = 3/(5*pi)

    return {
        'time': log_inv_lambda,
        'Lambda': lambdas,
        'N_total': N_total,
        'S_dS': S_dS,
        'fill': fill,
        'log_N': np.log10(N_total),
        'log_S': np.log10(S_dS),
        'log_Lambda': -log_inv_lambda
    }


# ─── Main Visualization ───
def build_figure():
    """Build the full dark sector visualization."""

    fig = plt.figure(figsize=(18, 12), facecolor=BG)
    fig.canvas.manager.set_window_title('BST — The Dark Sector')

    # ── Grid layout ──
    # Top row: pie chart (center)
    # Middle row: evolution (left), three views (right)
    # Bottom strip: formula chain
    gs = GridSpec(4, 2, figure=fig,
                  height_ratios=[0.33, 0.02, 0.50, 0.10],
                  width_ratios=[1, 1],
                  hspace=0.25, wspace=0.25,
                  left=0.06, right=0.94, top=0.95, bottom=0.03)

    # ── Top Center: The Cosmic Pie ──

    ax_pie = fig.add_subplot(gs[0, :])
    ax_pie.set_facecolor(BG)
    ax_pie.set_xlim(-2.2, 2.2)
    ax_pie.set_ylim(-1.3, 1.5)
    ax_pie.set_aspect('equal')
    ax_pie.axis('off')

    # Draw pie chart
    sizes = [FILL * 100, DARK * 100]
    colors_pie = [GOLD, VOID_PURPLE]
    explode = (0.03, 0.0)

    # Create a separate axes for the pie inside ax_pie's bounds
    pie_inset = fig.add_axes([0.32, 0.64, 0.36, 0.32], facecolor=BG)
    pie_inset.set_aspect('equal')

    wedges, texts, autotexts = pie_inset.pie(
        sizes, explode=explode, colors=colors_pie,
        autopct='%1.1f%%', startangle=90,
        textprops={'color': WHITE, 'fontsize': 14, 'weight': 'bold'},
        wedgeprops={'edgecolor': BG, 'linewidth': 2}
    )

    # Glow on the golden wedge
    wedges[0].set_alpha(0.95)
    wedges[1].set_alpha(0.85)
    autotexts[0].set_color('#000000')
    autotexts[0].set_fontsize(15)
    autotexts[0].set_weight('bold')
    autotexts[1].set_color(PURPLE_GLOW)
    autotexts[1].set_fontsize(15)
    autotexts[1].set_weight('bold')

    # Labels
    pie_inset.text(0, -1.45, 'COMMITTED', ha='center', va='center',
                   color=GOLD, fontsize=11, weight='bold',
                   path_effects=[pe.withStroke(linewidth=2, foreground=GOLD_DIM, alpha=0.4)])
    pie_inset.text(0.85, 0.85, 'DARK', ha='center', va='center',
                   color=PURPLE_GLOW, fontsize=11, weight='bold',
                   path_effects=[pe.withStroke(linewidth=2, foreground=VOID_PURPLE, alpha=0.4)])

    # Title above pie
    fig.text(0.5, 0.97, 'THE DARK SECTOR \u2014 Permanently Unknowable',
             ha='center', va='top', color=PURPLE_GLOW, fontsize=20, weight='bold',
             path_effects=[pe.withStroke(linewidth=4, foreground=VOID_PURPLE, alpha=0.5)])
    fig.text(0.5, 0.945, 'Not hidden. Not waiting to be found. Topologically forbidden.',
             ha='center', va='top', color=GREY, fontsize=12, style='italic')

    # Formula beside pie
    fig.text(0.12, 0.82, r'$f = \frac{N_c}{n_C \, \pi} = \frac{3}{5\pi}$',
             ha='center', va='center', color=GOLD, fontsize=18,
             path_effects=[pe.withStroke(linewidth=2, foreground=GOLD_DIM, alpha=0.3)])
    fig.text(0.12, 0.77, '= 19.099%', ha='center', va='center',
             color=GOLD_DIM, fontsize=13)

    fig.text(0.88, 0.82, r'$1 - f = 1 - \frac{3}{5\pi}$',
             ha='center', va='center', color=PURPLE_GLOW, fontsize=18,
             path_effects=[pe.withStroke(linewidth=2, foreground=VOID_PURPLE, alpha=0.3)])
    fig.text(0.88, 0.77, '= 80.901%', ha='center', va='center',
             color=PURPLE_LINE, fontsize=13)

    # ── Left Panel: Evolution Timeline ──

    ax_evo = fig.add_subplot(gs[2, 0])
    ax_evo.set_facecolor(DARK_PANEL)

    data = compute_evolution(500)
    time = data['time']
    t_min, t_max = time[0], time[-1]

    # Normalize for dual axes: plot log quantities on left, fill on right
    ax_evo.set_xlim(t_min, t_max)

    # Plot S_dS and N_total (log scale on left y-axis)
    ax_evo.set_ylabel(r'$\log_{10}$ (counts)', color=GREY, fontsize=10)
    ax_evo.tick_params(axis='y', colors=GREY, labelsize=8)
    ax_evo.tick_params(axis='x', colors=GREY, labelsize=8)
    ax_evo.set_xlabel(r'Cosmic time proxy:  $\log_{10}(1/\Lambda)$', color=GREY, fontsize=10)

    ln_s, = ax_evo.plot(time, data['log_S'], color=BLUE_GLOW, linewidth=1.5,
                         alpha=0.8, label=r'$\log S_{dS}$ (capacity)')
    ln_n, = ax_evo.plot(time, data['log_N'], color=GOLD, linewidth=1.5,
                         alpha=0.8, label=r'$\log N_{total}$ (committed)')
    ln_lam, = ax_evo.plot(time, data['log_Lambda'], color=PURPLE_LINE, linewidth=1.2,
                           alpha=0.6, linestyle='--', label=r'$\log \Lambda$')

    # Right y-axis: fill fraction
    ax_fill = ax_evo.twinx()
    ax_fill.set_ylim(0, 0.5)
    ax_fill.set_ylabel('Fill fraction', color=WHITE, fontsize=10)
    ax_fill.tick_params(axis='y', colors=WHITE, labelsize=8)

    # THE DRAMATIC FLAT LINE
    ln_fill, = ax_fill.plot(time, data['fill'], color=WHITE, linewidth=3.5,
                             alpha=1.0, label=f'Fill = 3/(5\u03c0) = {FILL:.3f}',
                             zorder=10)
    ln_fill.set_path_effects([
        pe.withStroke(linewidth=6, foreground=GOLD, alpha=0.25),
        pe.Normal()
    ])

    # Horizontal reference line at 19.1%
    ax_fill.axhline(y=FILL, color=GOLD_DIM, linewidth=0.8, alpha=0.3,
                     linestyle=':', zorder=5)
    ax_fill.text(t_max + 2, FILL, f'{100*FILL:.1f}%', va='center',
                 color=GOLD, fontsize=10, weight='bold', clip_on=False)

    # "Now" marker (Lambda ~ 10^-122)
    t_now = 122.0
    ax_evo.axvline(x=t_now, color=RED_WARM, linewidth=1, alpha=0.4, linestyle='-.')
    ax_evo.text(t_now + 1, ax_evo.get_ylim()[1] * 0.95, 'NOW',
                color=RED_WARM, fontsize=9, alpha=0.7, weight='bold')

    # Title and caption
    ax_evo.set_title('Evolution Timeline', color=BLUE_GLOW, fontsize=13,
                      weight='bold', pad=10)
    ax_evo.text(0.5, -0.13, '"The jar grows as fast as you fill it."',
                transform=ax_evo.transAxes, ha='center', va='top',
                color=GREY, fontsize=10, style='italic')

    # Combined legend
    lines = [ln_s, ln_n, ln_lam, ln_fill]
    labels = [l.get_label() for l in lines]
    ax_evo.legend(lines, labels, loc='upper left', fontsize=8,
                  facecolor=DARK_PANEL, edgecolor=GREY, labelcolor=WHITE,
                  framealpha=0.8)

    # Grid
    ax_evo.grid(True, alpha=0.15, color=GREY)
    for spine in ax_evo.spines.values():
        spine.set_color(GREY)
        spine.set_alpha(0.3)
    for spine in ax_fill.spines.values():
        spine.set_color(GREY)
        spine.set_alpha(0.3)

    # ── Slider for scanning cosmic time ──
    ax_slider = fig.add_subplot(gs[1, 0])
    ax_slider.set_facecolor(BG)
    slider = Slider(ax_slider, 'Epoch', t_min, t_max, valinit=t_now,
                    color=GOLD_DIM, valstep=0.5)
    slider.label.set_color(GREY)
    slider.label.set_fontsize(8)
    slider.valtext.set_color(GOLD)
    slider.valtext.set_fontsize(8)

    # Epoch marker line (updated by slider)
    epoch_line = ax_evo.axvline(x=t_now, color=GOLD, linewidth=1.5,
                                 alpha=0.6, linestyle='-', zorder=8)

    # Epoch info text
    epoch_text = ax_evo.text(t_now, ax_evo.get_ylim()[0] + 2,
                              '', color=GOLD, fontsize=7, ha='left',
                              va='bottom', alpha=0.8)

    def update_slider(val):
        t = slider.val
        epoch_line.set_xdata([t, t])
        lam = 10.0 ** (-t)
        N = BUDGET / lam
        S = 3.0 * np.pi / lam
        f = N / S
        epoch_text.set_position((t + 1, ax_evo.get_ylim()[0] + 2))
        epoch_text.set_text(
            f'\u039b=10^{{{-t:.0f}}}\n'
            f'N={N:.1e}\n'
            f'S={S:.1e}\n'
            f'f={f:.5f}'
        )
        fig.canvas.draw_idle()

    slider.on_changed(update_slider)
    update_slider(t_now)

    # ═══════════════════════════════════════════════════════════════
    #  RIGHT PANEL: Three Views of Darkness
    # ═══════════════════════════════════════════════════════════════

    ax_views = fig.add_subplot(gs[2, 1])
    ax_views.set_facecolor(DARK_PANEL)
    ax_views.set_xlim(0, 1)
    ax_views.set_ylim(0, 1)
    ax_views.axis('off')

    ax_views.set_title('Three Views of Darkness', color=PURPLE_GLOW, fontsize=13,
                        weight='bold', pad=10)

    # Helper to render a titled text block
    def _render_block(y, title, title_color, lines, special=None):
        glow_text(ax_views, 0.5, y, title, color=title_color, fontsize=13, weight='bold')
        y -= 0.05
        for line in lines:
            y -= 0.038
            if not line:
                continue
            col = GREY if line.startswith('"') else LIGHT_GREY
            fs = 8.5 if line.startswith('"') else 9
            sty = 'italic' if line.startswith('"') else 'normal'
            if special:
                for key, c in special.items():
                    if key in line: col = c; break
            glow_text(ax_views, 0.5, y, line, color=col, fontsize=fs,
                      glow_width=1, style=sty)
        y -= 0.025
        ax_views.plot([0.1, 0.9], [y, y], color=GREY, alpha=0.2, linewidth=0.5)
        return y - 0.03

    # Sub-panel 1: Why Dark Energy?
    y = _render_block(0.95, 'Why Dark Energy?', PURPLE_LINE, [
        r'$\Lambda = \frac{9/5}{N_{total}}$ \u2014 vacuum energy is the',
        'COST of accumulated knowledge.', '',
        'As N grows, \u039b shrinks, but never reaches 0.', '',
        '"Dark energy is the universe\'s operating budget."'
    ])

    # Sub-panel 2: Why Dark Matter?
    y = _render_block(y, 'Why Dark Matter?', BLUE_GLOW, [
        'Uncommitted channels create gravitational effects.',
        'The topology of the uncommitted 80.9%',
        'curves spacetime without emitting light.', '',
        '"Dark matter is the geometry of',
        'what the universe doesn\'t know."'
    ])

    # Sub-panel 3: The Cosmic Coincidence
    y = _render_block(y, 'The Cosmic Coincidence', GREEN_GLOW, [
        'Standard cosmology asks:',
        'WHY is \u03a9_\u039b \u2248 \u03a9_m right now?  (Fine-tuning!)', '',
        'BST answers: Fill = 19.1% ALWAYS.',
        'No fine-tuning needed. The split is structural.',
    ], special={'Fine-tuning': RED_WARM, 'BST answers': GREEN_GLOW})
    y += 0.03  # undo the last offset from _render_block

    # Comparison box
    y -= 0.05
    box = FancyBboxPatch((0.05, y - 0.1), 0.9, 0.13,
                          boxstyle="round,pad=0.01",
                          facecolor='#0a0a2a', edgecolor=GREY, alpha=0.6,
                          linewidth=0.5)
    ax_views.add_patch(box)

    glow_text(ax_views, 0.5, y - 0.01, 'Planck 2018 observed:',
              color=GREY, fontsize=8, weight='bold')
    glow_text(ax_views, 0.5, y - 0.04,
              f'DE {PLANCK_DE*100:.1f}% + DM {PLANCK_DM*100:.1f}% + Vis {PLANCK_VIS*100:.1f}%'
              f'  \u2192  Dark total: {PLANCK_DARK*100:.1f}%',
              color=LIGHT_GREY, fontsize=8, glow_width=1)
    glow_text(ax_views, 0.5, y - 0.07,
              f'BST predicts:  Dark {DARK*100:.1f}% + Visible {FILL*100:.1f}%',
              color=GOLD, fontsize=9, weight='bold', glow_width=1)

    # ── Right panel slider region (cosmetic filler) ──
    ax_rslider = fig.add_subplot(gs[1, 1])
    ax_rslider.set_facecolor(BG)
    ax_rslider.axis('off')
    ax_rslider.text(0.5, 0.5,
                    'f = N/S = (9/5) / (3\u03c0) = 3/(5\u03c0) = 0.19099...',
                    ha='center', va='center', color=GOLD_DIM, fontsize=9,
                    transform=ax_rslider.transAxes)

    # ═══════════════════════════════════════════════════════════════
    #  BOTTOM STRIP: The Formula Chain
    # ═══════════════════════════════════════════════════════════════

    ax_bot = fig.add_subplot(gs[3, :])
    ax_bot.set_facecolor(BG)
    ax_bot.set_xlim(0, 1)
    ax_bot.set_ylim(0, 1)
    ax_bot.axis('off')

    # The chain
    chain = (
        r'$\Lambda \times N = \frac{9}{5}$'
        r'$\quad\longrightarrow\quad$'
        r'$S_{dS} = \frac{3\pi}{\Lambda}$'
        r'$\quad\longrightarrow\quad$'
        r'$f = \frac{N \Lambda}{3\pi} = \frac{3}{5\pi} = 19.1\%$'
    )
    ax_bot.text(0.5, 0.65, chain, ha='center', va='center',
                color=GOLD, fontsize=14,
                path_effects=[pe.withStroke(linewidth=3, foreground=GOLD_DIM, alpha=0.3)])

    ax_bot.text(0.5, 0.2,
                '"The universe is always 19.1% committed. The dark sector is permanent."',
                ha='center', va='center', color=GREY, fontsize=11, style='italic',
                path_effects=[pe.withStroke(linewidth=2, foreground=DARK_PANEL, alpha=0.5)])

    return fig, slider


# ─── Comparison Figure ───
def build_comparison_figure():
    """Planck observed fractions vs BST prediction — side-by-side bar chart."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), facecolor=BG)
    for ax in (ax1, ax2):
        ax.set_facecolor(DARK_PANEL)
        for s in ax.spines.values(): s.set_color(GREY); s.set_alpha(0.3)
        ax.tick_params(colors=GREY)

    # Left: Planck 2018
    cats = ['Dark Energy', 'Dark Matter', 'Visible']
    vals = [PLANCK_DE * 100, PLANCK_DM * 100, PLANCK_VIS * 100]
    cols = [PURPLE_LINE, BLUE_GLOW, GOLD]
    bars1 = ax1.barh(cats, vals, color=cols, alpha=0.8, edgecolor=BG, linewidth=2)
    ax1.set_xlim(0, 100)
    ax1.set_xlabel('% of total energy density', color=GREY, fontsize=10)
    ax1.set_title('Planck 2018 Observed', color=GREY, fontsize=13, weight='bold')
    for i, (b, v) in enumerate(zip(bars1, vals)):
        ax1.text(v + 1.5, b.get_y() + b.get_height()/2, f'{v:.1f}%',
                 va='center', color=cols[i], fontsize=12, weight='bold')
    ax1.set_yticklabels(cats, color=WHITE, fontsize=11)

    # Right: BST prediction
    bst_cats = ['Dark\n(uncommitted)', 'Visible\n(committed)']
    bst_vals = [DARK * 100, FILL * 100]
    bst_cols = [VOID_PURPLE, GOLD]
    bars2 = ax2.barh(bst_cats, bst_vals, color=bst_cols, alpha=0.85, edgecolor=BG, linewidth=2)
    ax2.set_xlim(0, 100)
    ax2.set_xlabel('% of de Sitter capacity', color=GREY, fontsize=10)
    ax2.set_title('BST Prediction (structural)', color=GOLD, fontsize=13, weight='bold')
    for i, (b, v) in enumerate(zip(bars2, bst_vals)):
        ax2.text(v + 1.5, b.get_y() + b.get_height()/2, f'{v:.1f}%',
                 va='center', color=[PURPLE_GLOW, GOLD][i], fontsize=12, weight='bold')
    ax2.set_yticklabels(bst_cats, color=WHITE, fontsize=11)

    fig.text(0.5, 0.02,
             'Planck dark total = 95.1%  |  BST dark = 80.9%  |'
             '  BST separates "visible but non-baryonic" from true dark',
             ha='center', va='bottom', color=GREY, fontsize=9, style='italic')
    fig.suptitle('Observed vs Structural: The Dark Sector',
                 color=PURPLE_GLOW, fontsize=16, weight='bold', y=0.98)
    fig.tight_layout(rect=[0, 0.05, 1, 0.93])
    return fig


# ─── The Flat Line Drama ───
def build_flat_line_figure():
    """The most dramatic non-change in physics. Everything evolves. Fill doesn't."""
    fig, ax = plt.subplots(figsize=(14, 6), facecolor=BG)
    ax.set_facecolor(DARK_PANEL)
    data = compute_evolution(1000)
    time = data['time']

    # Normalize curves to [0,1] for visual drama
    def _norm(arr): return (arr - arr.min()) / (arr.max() - arr.min())
    log_S_n, log_N_n = _norm(data['log_S']), _norm(data['log_N'])
    log_L_n = _norm(data['log_Lambda'])

    # Sweeping curves — everything changes
    ax.fill_between(time, 0, log_S_n, alpha=0.08, color=BLUE_GLOW)
    ax.plot(time, log_S_n, color=BLUE_GLOW, lw=1.5, alpha=0.7,
            label=r'$S_{dS}$ (capacity) — always growing')
    ax.fill_between(time, 0, log_N_n, alpha=0.06, color=GOLD)
    ax.plot(time, log_N_n, color=GOLD, lw=1.5, alpha=0.7,
            label=r'$N_{total}$ (committed) — always growing')
    ax.plot(time, log_L_n, color=PURPLE_LINE, lw=1.2, alpha=0.5,
            ls='--', label=r'$\Lambda$ — always shrinking')

    # THE FLAT LINE — bold, white, dramatic
    flat_y = FILL / 0.5
    ax.axhline(y=flat_y, color=WHITE, lw=4, alpha=0.95, zorder=10,
               path_effects=[pe.withStroke(linewidth=8, foreground=GOLD, alpha=0.2),
                             pe.Normal()])
    ax.text(time[-1] + 2, flat_y, f'f = 3/(5\u03c0) = {FILL:.4f}\n= {100*FILL:.1f}%',
            va='center', ha='left', color=GOLD, fontsize=12, weight='bold',
            clip_on=False, path_effects=[pe.withStroke(lw=2, foreground=BG, alpha=0.8)])
    ax.axvline(x=122, color=RED_WARM, lw=1, alpha=0.4, ls='-.')
    ax.text(123, 0.95, 'NOW', color=RED_WARM, fontsize=9, alpha=0.6, weight='bold')

    ax.set(xlim=(time[0], time[-1]), ylim=(-0.05, 1.1))
    ax.set_xlabel(r'Cosmic time proxy: $\log_{10}(1/\Lambda)$', color=GREY, fontsize=11)
    ax.set_ylabel('Normalized scale', color=GREY, fontsize=11)
    ax.tick_params(colors=GREY, labelsize=9)
    ax.grid(True, alpha=0.1, color=GREY)
    for s in ax.spines.values(): s.set_color(GREY); s.set_alpha(0.3)
    ax.legend(loc='upper left', fontsize=10, facecolor=DARK_PANEL,
              edgecolor=GREY, labelcolor=WHITE, framealpha=0.8)
    ax.set_title('The Most Dramatic Non-Change in Physics',
                 color=WHITE, fontsize=16, weight='bold', pad=15,
                 path_effects=[pe.withStroke(lw=3, foreground=GOLD, alpha=0.2)])
    ax.text(0.5, -0.10, 'Everything evolves. The fill fraction doesn\'t. '
            'The universe is always exactly 19.1% committed.',
            transform=ax.transAxes, ha='center', va='top',
            color=GREY, fontsize=11, style='italic')
    fig.tight_layout(rect=[0, 0.03, 0.95, 0.97])
    return fig


# ─── Print Report ───
def print_report():
    """Print a concise summary of the dark sector calculation."""
    ds = DarkSector()
    ep = ds.at_epoch(LAMBDA_NOW)
    sep = "=" * 65
    print(f"\n{sep}")
    print("  THE DARK SECTOR — Bubble Spacetime Theory")
    print(f"{sep}\n")
    print(f"  N_c = {N_c}  n_C = {n_C}  Budget = {BUDGET:.3f}")
    print(f"  Fill = 3/(5*pi) = {FILL:.6f} = {100*FILL:.3f}%")
    print(f"  Dark = 1 - f    = {DARK:.6f} = {100*DARK:.3f}%\n")
    print(f"  Current epoch (Lambda ~ 2.9e-122):")
    print(f"    S_dS = {ep['S_dS']:.3e}  N = {ep['N_total']:.3e}  fill = {ep['fill']:.6f}\n")
    print(f"  Planck 2018: DE={PLANCK_DE*100:.1f}% DM={PLANCK_DM*100:.1f}% "
          f"Vis={PLANCK_VIS*100:.1f}% (dark={PLANCK_DARK*100:.1f}%)")
    print(f"  BST:         Dark={DARK*100:.1f}%  Visible={FILL*100:.1f}%\n")
    print(f"  Fine-tuned? {ds.is_coincidence_fine_tuned()} — structural, not coincidental.")
    print(f"  The 19.1%/80.9% split is ETERNAL. There is no special 'now.'")
    print(f"{sep}\n")


# ─── Main ───
if __name__ == '__main__':
    print_report()

    # Build all three figures
    fig1, slider = build_figure()
    fig2 = build_comparison_figure()
    fig3 = build_flat_line_figure()

    plt.show()
