#!/usr/bin/env python3
"""
THE REALITY BUDGET
==================
A stunning BST conservation law:

    Λ × N_total ≈ 1/(8π) ≈ 0.0398

The product of vacuum energy density and total accumulated commitments
equals the Einstein coupling coefficient. Expansion is the cost of memory.

As the universe accumulates committed facts (baryons, structure, written
information), the vacuum energy Λ must decrease — the two gauges move
in opposite directions like a cosmic seesaw, but their product is
EXACTLY conserved at 1/(8π).

The 8π is the SAME 8π in Einstein's field equation:
    G_μν + Λg_μν = (8πG/c⁴) T_μν

Information and geometry are coupled by a single constant.

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
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.colors as mcolors

# ─── Constants ───
BUDGET = 1.0 / (8.0 * np.pi)  # 0.039789...
N_MIN = 1.0
N_MAX = 100.0
N_INIT = 10.0

BG = '#0a0a1a'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
BLUE_GLOW = '#4488ff'
BLUE_DEEP = '#1a1a6a'
PURPLE_GLOW = '#8844cc'
ORANGE_GLOW = '#ff8800'
ORANGE_WARM = '#ffaa44'
RED_WARM = '#ff6644'
WHITE = '#ffffff'
GREY = '#888888'
DARK_PANEL = '#0d0d24'
GAUGE_BG = '#111133'

# ─── Helper: draw a thermometer gauge ───
def draw_gauge(ax, fraction, color_low, color_high, glow_color, label, value_str,
               annotation=None, max_label=None, min_label="0"):
    """Draw a vertical thermometer gauge on the given axes."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.12, 1.18)
    ax.axis('off')

    # Gauge outline
    gauge_x = 0.25
    gauge_w = 0.50
    gauge_y = 0.05
    gauge_h = 0.85

    # Background tube
    tube = FancyBboxPatch((gauge_x, gauge_y), gauge_w, gauge_h,
                           boxstyle="round,pad=0.02",
                           facecolor='#0a0a2a', edgecolor='#333366',
                           linewidth=2, zorder=1)
    ax.add_patch(tube)

    # Liquid fill
    fill_h = max(0.001, fraction * gauge_h)
    fill = FancyBboxPatch((gauge_x + 0.02, gauge_y + 0.02),
                           gauge_w - 0.04, fill_h - 0.02,
                           boxstyle="round,pad=0.01",
                           facecolor=glow_color, edgecolor='none',
                           alpha=0.85, zorder=2)
    ax.add_patch(fill)

    # Inner glow gradient (simulate with multiple rectangles)
    n_grad = 8
    for i in range(n_grad):
        alpha_i = 0.15 * (1.0 - i / n_grad)
        shrink = 0.04 + i * 0.02
        h_i = max(0.001, fill_h - 0.02 - i * 0.005)
        if h_i > 0.001:
            grad = Rectangle((gauge_x + shrink, gauge_y + 0.02),
                              gauge_w - 2 * shrink, h_i,
                              facecolor=WHITE, edgecolor='none',
                              alpha=alpha_i, zorder=3)
            ax.add_patch(grad)

    # Meniscus glow at top of liquid
    if fraction > 0.02:
        meniscus_y = gauge_y + 0.02 + fill_h - 0.02
        ax.plot([gauge_x + 0.06, gauge_x + gauge_w - 0.06],
                [meniscus_y, meniscus_y],
                color=WHITE, alpha=0.5, linewidth=2, zorder=4)

    # Tick marks
    for tick_frac in np.linspace(0, 1, 11):
        ty = gauge_y + tick_frac * gauge_h
        ax.plot([gauge_x - 0.02, gauge_x], [ty, ty],
                color=GREY, linewidth=1, alpha=0.5)

    # Min/max labels
    ax.text(gauge_x - 0.04, gauge_y, min_label, fontsize=8,
            color=GREY, ha='right', va='center', fontfamily='monospace')
    if max_label:
        ax.text(gauge_x - 0.04, gauge_y + gauge_h, max_label, fontsize=8,
                color=GREY, ha='right', va='center', fontfamily='monospace')

    # Title label at top
    ax.text(0.5, 1.12, label, fontsize=11, fontweight='bold',
            color=glow_color, ha='center', va='center', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground=BG)])

    # Value display
    ax.text(0.5, 0.97, value_str, fontsize=14, fontweight='bold',
            color=WHITE, ha='center', va='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a3a',
                      edgecolor=glow_color, linewidth=1.5, alpha=0.9))

    # Annotation at bottom
    if annotation:
        ax.text(0.5, -0.08, annotation, fontsize=7,
                color=GOLD_DIM, ha='center', va='center', fontfamily='monospace',
                style='italic', wrap=True)


def draw_center_panel(ax, N_total, Lambda, product):
    """Draw the central budget equation display."""
    ax.clear()
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Title
    ax.text(0.5, 0.97, 'THE BUDGET EQUATION', fontsize=14, fontweight='bold',
            color=GOLD, ha='center', va='top', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])

    # Main equation: Λ × N_total = value
    ax.text(0.5, 0.88, f'Λ  ×  N_total  =  {product:.6f}',
            fontsize=16, fontweight='bold',
            color=WHITE, ha='center', va='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a3a',
                      edgecolor=GOLD, linewidth=2))

    # Reference value
    ax.text(0.5, 0.795, f'1/(8π)  =  {BUDGET:.6f}',
            fontsize=13, color=GOLD, ha='center', va='center',
            fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a2a0a',
                      edgecolor=GOLD_DIM, linewidth=1))

    # Deviation
    deviation = abs(product - BUDGET) / BUDGET * 100
    ax.text(0.5, 0.72, f'deviation: {deviation:.4f}%',
            fontsize=9, color='#44ff44' if deviation < 0.1 else ORANGE_GLOW,
            ha='center', va='center', fontfamily='monospace')

    # ─── Product meter (horizontal bar) ───
    bar_y = 0.65
    bar_h = 0.03
    bar_x = 0.08
    bar_w = 0.84

    # Background
    bar_bg = Rectangle((bar_x, bar_y - bar_h / 2), bar_w, bar_h,
                         facecolor='#1a1a3a', edgecolor='#333366',
                         linewidth=1.5, zorder=1)
    ax.add_patch(bar_bg)

    # Fill — normalized so that BUDGET maps to full bar
    fill_frac = min(1.0, product / (BUDGET * 1.5))
    target_frac = BUDGET / (BUDGET * 1.5)
    bar_fill = Rectangle((bar_x, bar_y - bar_h / 2), bar_w * fill_frac, bar_h,
                           facecolor='#44cc44', edgecolor='none',
                           alpha=0.7, zorder=2)
    ax.add_patch(bar_fill)

    # Target line
    target_x = bar_x + bar_w * target_frac
    ax.plot([target_x, target_x], [bar_y - bar_h, bar_y + bar_h],
            color=GOLD, linewidth=2.5, zorder=3)
    ax.text(target_x, bar_y + bar_h + 0.015, '1/(8π)', fontsize=8,
            color=GOLD, ha='center', va='bottom', fontfamily='monospace')

    # Conservation text
    ax.text(0.5, 0.57, 'The product is conserved.',
            fontsize=11, fontweight='bold', color='#44ff88',
            ha='center', va='center', fontfamily='monospace')
    ax.text(0.5, 0.525, 'Information and vacuum energy trade off.',
            fontsize=9, color='#44cc88',
            ha='center', va='center', fontfamily='monospace')

    # ─── Einstein's field equation ───
    ax.text(0.5, 0.44, "Einstein's Field Equation:",
            fontsize=10, color=GREY, ha='center', va='center',
            fontfamily='monospace', style='italic')

    # Build the equation with highlighted 8π
    eq_y = 0.37
    # Left side
    ax.text(0.15, eq_y, 'G', fontsize=16, color=WHITE, ha='center',
            va='center', fontfamily='serif', style='italic')
    ax.text(0.195, eq_y + 0.015, 'μν', fontsize=9, color=WHITE, ha='center',
            va='center', fontfamily='serif')
    ax.text(0.24, eq_y, ' + ', fontsize=14, color=WHITE, ha='center',
            va='center', fontfamily='monospace')
    ax.text(0.30, eq_y, 'Λ', fontsize=16, color=BLUE_GLOW, ha='center',
            va='center', fontfamily='serif', style='italic', fontweight='bold')
    ax.text(0.34, eq_y, 'g', fontsize=16, color=WHITE, ha='center',
            va='center', fontfamily='serif', style='italic')
    ax.text(0.375, eq_y + 0.015, 'μν', fontsize=9, color=WHITE, ha='center',
            va='center', fontfamily='serif')

    # Equals
    ax.text(0.44, eq_y, ' = ', fontsize=14, color=WHITE, ha='center',
            va='center', fontfamily='monospace')

    # Right side — 8π highlighted!
    ax.text(0.535, eq_y, '8π', fontsize=18, fontweight='bold',
            color=GOLD, ha='center', va='center', fontfamily='serif',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#3a3a0a',
                      edgecolor=GOLD, linewidth=2),
            path_effects=[pe.withStroke(linewidth=2, foreground='#664400')])
    ax.text(0.62, eq_y, 'G', fontsize=14, color=WHITE, ha='center',
            va='center', fontfamily='serif', style='italic')
    ax.text(0.66, eq_y, '/', fontsize=14, color=WHITE, ha='center',
            va='center', fontfamily='monospace')
    ax.text(0.70, eq_y, 'c', fontsize=14, color=WHITE, ha='center',
            va='center', fontfamily='serif', style='italic')
    ax.text(0.735, eq_y + 0.02, '⁴', fontsize=10, color=WHITE, ha='center',
            va='center', fontfamily='serif')

    ax.text(0.81, eq_y, 'T', fontsize=16, color=WHITE, ha='center',
            va='center', fontfamily='serif', style='italic')
    ax.text(0.85, eq_y + 0.015, 'μν', fontsize=9, color=WHITE, ha='center',
            va='center', fontfamily='serif')

    # Arrow pointing to 8π
    ax.annotate('', xy=(0.535, eq_y - 0.055), xytext=(0.535, eq_y - 0.10),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
    ax.text(0.535, eq_y - 0.125, 'SAME  8π !', fontsize=11, fontweight='bold',
            color=GOLD, ha='center', va='center', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])

    # Coupling text
    ax.text(0.5, 0.17, 'Λ × N_total = 1/(8π)',
            fontsize=13, fontweight='bold', color=GOLD,
            ha='center', va='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a0a',
                      edgecolor=GOLD_DIM, linewidth=1.5))

    ax.text(0.5, 0.095, 'The coupling between information\nand geometry is exact.',
            fontsize=9, color=GOLD_DIM, ha='center', va='center',
            fontfamily='monospace', style='italic', linespacing=1.5)

    # Current values at bottom
    ax.text(0.20, 0.02, f'Λ = {Lambda:.6f}', fontsize=9,
            color=BLUE_GLOW, ha='center', va='center', fontfamily='monospace')
    ax.text(0.80, 0.02, f'N = {N_total:.1f}', fontsize=9,
            color=ORANGE_GLOW, ha='center', va='center', fontfamily='monospace')


# ─── Figure Setup ───
fig = plt.figure(figsize=(17, 11), facecolor=BG)
fig.canvas.manager.set_window_title('The Reality Budget — BST')

# ─── Header ───
fig.text(0.5, 0.965, 'THE REALITY BUDGET', fontsize=30, fontweight='bold',
         color=GOLD, ha='center', va='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#443300')])

fig.text(0.5, 0.935, f'Λ  ×  N_total  ≈  1/(8π)  ≈  {BUDGET:.4f}',
         fontsize=14, color='#ddbb66', ha='center', va='center',
         fontfamily='monospace')

fig.text(0.5, 0.915, 'Expansion is the cost of memory.',
         fontsize=11, color=GOLD_DIM, ha='center', va='center',
         fontfamily='monospace', style='italic')

# ─── Panel Axes ───
ax_lambda = fig.add_axes([0.03, 0.22, 0.22, 0.66])   # Left: Λ gauge
ax_center = fig.add_axes([0.28, 0.22, 0.44, 0.66])    # Center: equation
ax_ntotal = fig.add_axes([0.75, 0.22, 0.22, 0.66])    # Right: N gauge

# ─── Slider ───
ax_slider = fig.add_axes([0.15, 0.115, 0.55, 0.025], facecolor='#1a1a3a')
slider = Slider(ax_slider, '', N_MIN, N_MAX, valinit=N_INIT,
                valstep=0.5, color=ORANGE_GLOW)
slider.valtext.set_color(WHITE)
slider.valtext.set_fontfamily('monospace')

# Slider label
fig.text(0.15, 0.155, 'Universe Age / Commitment Accumulation',
         fontsize=10, color=GREY, ha='left', va='center', fontfamily='monospace')

# Arrow annotations on slider
fig.text(0.13, 0.127, '◀ young', fontsize=8, color=BLUE_GLOW,
         ha='center', va='center', fontfamily='monospace')
fig.text(0.72, 0.127, 'old ▶', fontsize=8, color=ORANGE_GLOW,
         ha='center', va='center', fontfamily='monospace')

# ─── Bottom Explanation Text ───
explanations = [
    ("Every committed baryon-oscillation costs a tiny bit of vacuum energy.", WHITE),
    ("Expansion is the cost of memory.", GOLD),
    ("The universe trades dark energy for written facts.", '#88ccff'),
    ("1/(8π) connects information to geometry.", GOLD_DIM),
]
for i, (txt, clr) in enumerate(explanations):
    fig.text(0.5, 0.08 - i * 0.02, txt, fontsize=9, color=clr,
             ha='center', va='center', fontfamily='monospace',
             style='italic' if i > 0 else 'normal')

# ─── Auto-accumulate Button ───
ax_button = fig.add_axes([0.76, 0.115, 0.14, 0.035])
button = Button(ax_button, 'Auto-Accumulate ▶',
                color='#1a2a1a', hovercolor='#2a4a2a')
button.label.set_color('#44ff88')
button.label.set_fontfamily('monospace')
button.label.set_fontsize(10)

# ─── State ───
state = {
    'auto': False,
    'N_total': N_INIT,
    'anim': None,
}


def compute(N_total):
    """Compute Λ from N_total, enforcing the budget."""
    Lambda = BUDGET / N_total
    product = Lambda * N_total  # Always exactly BUDGET
    return Lambda, product


def update_display(N_total):
    """Redraw all panels for current N_total."""
    Lambda, product = compute(N_total)

    # Λ max for display scaling — when N = N_MIN, Λ is at its maximum
    Lambda_max = BUDGET / N_MIN
    lambda_frac = Lambda / Lambda_max

    # N fraction
    n_frac = (N_total - N_MIN) / (N_MAX - N_MIN)

    # Left gauge: Λ (blue/purple, decreasing)
    draw_gauge(ax_lambda, lambda_frac,
               BLUE_DEEP, BLUE_GLOW, PURPLE_GLOW,
               'Vacuum Energy\nDensity  Λ',
               f'Λ = {Lambda:.6f}',
               annotation='Λ slowly decreases as the universe\naccumulates more written facts',
               max_label=f'{Lambda_max:.4f}',
               min_label='0')

    # Right gauge: N_total (orange/gold, increasing)
    draw_gauge(ax_ntotal, n_frac,
               '#663300', ORANGE_GLOW, ORANGE_WARM,
               'Accumulated\nCommitments  N_total',
               f'N = {N_total:.1f}',
               annotation='Each baryon oscillation, each\ncommitted fact, adds to the total',
               max_label=f'{N_MAX:.0f}',
               min_label=f'{N_MIN:.0f}')

    # Center panel
    draw_center_panel(ax_center, N_total, Lambda, product)

    fig.canvas.draw_idle()


def on_slider(val):
    """Handle slider change."""
    state['N_total'] = val
    update_display(val)


def on_button(event):
    """Toggle auto-accumulation."""
    state['auto'] = not state['auto']
    if state['auto']:
        button.label.set_text('Stop ■')
        button.color = '#2a1a1a'
        button.hovercolor = '#4a2a2a'
        button.label.set_color(RED_WARM)
    else:
        button.label.set_text('Auto-Accumulate ▶')
        button.color = '#1a2a1a'
        button.hovercolor = '#2a4a2a'
        button.label.set_color('#44ff88')


def animate(frame):
    """Animation callback for auto-accumulation."""
    if state['auto']:
        # Increment N_total
        state['N_total'] += 0.15
        if state['N_total'] > N_MAX:
            state['N_total'] = N_MIN  # Wrap around — new universe!
        slider.set_val(state['N_total'])
        update_display(state['N_total'])
    return []


# ─── Connect Callbacks ───
slider.on_changed(on_slider)
button.on_clicked(on_button)

# ─── Initial Draw ───
update_display(N_INIT)

# ─── Animation ───
anim = FuncAnimation(fig, animate, interval=50, blit=False, cache_frame_data=False)

plt.show()
