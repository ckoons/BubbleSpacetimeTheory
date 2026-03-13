#!/usr/bin/env python3
"""
THE MASTER EQUATION
===================
One sentence generates all of physics:

  "The universe is the ground state of the Bergman Laplacian on
   D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)], subject to Haldane exclusion
   with capacity 137."

Everything radiates from this: α, masses, forces, Λ, G, dark matter,
dark energy, the arrow of time, singularity resolution, proton stability.

This is the crown jewel — the source code of reality, visualized.

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
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors

# ═══════════════════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════════════════
N_c = 3
n_C = 5
N_max = 137
genus = n_C + 2       # = 7
N_w = 2               # weak
C2 = n_C + 1          # = 6
Gamma_order = 1920
alpha = 1 / 137.036
proton_ratio = C2 * np.pi**n_C  # 6π⁵

# ═══════════════════════════════════════════════════════════════════
# Color palette
# ═══════════════════════════════════════════════════════════════════
BG = '#0a0a1a'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
WHITE = '#f0f0ff'
CREAM = '#e8dcc8'
PURPLE_GLOW = '#9966ff'
PURPLE_DIM = '#6633cc'
BLUE_GLOW = '#4488ff'
GREEN_GLOW = '#44ff88'
GREEN_DIM = '#228844'
RED_GLOW = '#ff4466'
CYAN = '#00ccff'
ORANGE = '#ff8800'

# Category colors
C_MASS = '#44ff88'     # green  — masses
C_COUPLING = '#4488ff' # blue   — couplings
C_TOPO = '#ff4466'     # red    — topology
C_COSMO = '#cc66ff'    # purple — cosmology

GLOW_FX = [pe.withStroke(linewidth=3, foreground='#ffffff40')]
GLOW_FX_GOLD = [pe.withStroke(linewidth=4, foreground='#ffd70040')]
GLOW_FX_PURPLE = [pe.withStroke(linewidth=5, foreground='#9966ff60')]

# ═══════════════════════════════════════════════════════════════════
# Predictions radiating from the well
# ═══════════════════════════════════════════════════════════════════
# (label, category_color, formula_hint)
PREDICTIONS = [
    ('α = 1/137.036',          C_COUPLING, 'fine structure'),
    ('m_p/m_e = 6π⁵',         C_MASS,     'proton-electron'),
    ('sin²θ_W = 3/13',        C_COUPLING, 'Weinberg angle'),
    ('N_gen = 3',              C_TOPO,     'generations'),
    ('G (Newton)',             C_COSMO,    'gravity'),
    ('Λ = 2.9×10⁻¹²²',       C_COSMO,    'cosmo. constant'),
    ('Dark matter',            C_COSMO,    'channel noise'),
    ('Arrow of time',          C_COSMO,    'commitment'),
    ('θ_QCD = 0',              C_TOPO,     'strong CP'),
    ('Proton stable',          C_TOPO,     'Z₃ topological'),
    ('Singularity resolved',   C_TOPO,     'N_max = 137'),
    ('α_s = 7/20',            C_COUPLING, 'strong coupling'),
]

# ═══════════════════════════════════════════════════════════════════
# Figure setup
# ═══════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 12), facecolor=BG)
fig.canvas.manager.set_window_title('The Master Equation — BST')
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)

# ═══════════════════════════════════════════════════════════════════
# TOP: The Master Equation inscription
# ═══════════════════════════════════════════════════════════════════
ax_title = fig.add_axes([0.0, 0.82, 1.0, 0.18])
ax_title.set_facecolor(BG)
ax_title.axis('off')
ax_title.set_xlim(0, 1)
ax_title.set_ylim(0, 1)

# Decorative horizontal rules
for y_pos in [0.18, 0.95]:
    ax_title.plot([0.05, 0.95], [y_pos, y_pos], color=GOLD_DIM, linewidth=0.5,
                  alpha=0.4)

# The heading
ax_title.text(0.5, 0.82, 'THE MASTER EQUATION',
              fontsize=28, fontweight='bold', color=GOLD, ha='center',
              fontfamily='serif',
              path_effects=[pe.withStroke(linewidth=3, foreground='#aa770050')])

# The sentence — THE one sentence
sentence = ('"The universe is the ground state of the Bergman Laplacian on\n'
            ' D_IV⁵ = SO₀(5,2) / [SO(5) × SO(2)],  subject to Haldane exclusion '
            'with capacity 137."')
ax_title.text(0.5, 0.52, sentence,
              fontsize=13.5, color=WHITE, ha='center', va='center',
              fontfamily='serif', fontstyle='italic', linespacing=1.6,
              path_effects=[pe.withStroke(linewidth=2, foreground='#ffffff15')])

# Mathematical form
ax_title.text(0.5, 0.24,
              'Ground state of Δ_B on D_IV⁵,    N_max = 137',
              fontsize=15, color=CREAM, ha='center',
              fontfamily='monospace', fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.5', facecolor='#1a1a2e',
                        edgecolor=GOLD_DIM, linewidth=1.5, alpha=0.8),
              path_effects=[pe.withStroke(linewidth=1, foreground='#ffd70020')])

# ═══════════════════════════════════════════════════════════════════
# CENTER: The Radial Energy Well
# ═══════════════════════════════════════════════════════════════════
ax_well = fig.add_axes([0.12, 0.18, 0.58, 0.64])
ax_well.set_facecolor(BG)
ax_well.axis('off')
ax_well.set_xlim(-2.5, 2.5)
ax_well.set_ylim(-0.6, 3.2)
ax_well.set_aspect('equal')

# Draw the potential well curve
x_well = np.linspace(-2.0, 2.0, 500)
y_well = 0.5 * x_well**2  # parabolic well

# Glowing well walls — layered for glow effect
for lw, alpha_val in [(12, 0.05), (8, 0.08), (5, 0.15), (3, 0.3), (1.5, 0.6)]:
    ax_well.plot(x_well, y_well, color=PURPLE_DIM, linewidth=lw, alpha=alpha_val)
ax_well.plot(x_well, y_well, color=PURPLE_GLOW, linewidth=1.2, alpha=0.9)

# Fill the well with a very subtle gradient
for i in range(40):
    y_level = i * 0.05
    mask = y_well <= y_level
    if np.any(mask):
        x_fill = x_well[mask]
        ax_well.fill_between(x_fill, y_well[mask], y_level,
                             color=PURPLE_DIM, alpha=0.008)

# ─── Energy levels ───
# Ground state (bottom of well) — THE UNIVERSE
gs_y = 0.0
gs_width = 0.7
ax_well.plot([-gs_width, gs_width], [gs_y, gs_y], color=PURPLE_GLOW,
             linewidth=4, alpha=0.9, solid_capstyle='round')
# Glow layers
for lw, a in [(14, 0.06), (10, 0.1), (7, 0.15)]:
    ax_well.plot([-gs_width, gs_width], [gs_y, gs_y], color=PURPLE_GLOW,
                 linewidth=lw, alpha=a, solid_capstyle='round')

ax_well.text(0, gs_y - 0.15,
             'Λ = 2.9 × 10⁻¹²²',
             fontsize=10, color=PURPLE_GLOW, ha='center', fontfamily='monospace',
             fontweight='bold',
             path_effects=GLOW_FX_PURPLE)
ax_well.text(0, gs_y - 0.32,
             'THE UNIVERSE  (ground state)',
             fontsize=9, color='#bb99ff', ha='center', fontfamily='monospace',
             fontstyle='italic')

# First excited state — THE PROTON
ex1_y = 0.55
ex1_width = 1.05
ax_well.plot([-ex1_width, ex1_width], [ex1_y, ex1_y], color=GREEN_GLOW,
             linewidth=3.5, alpha=0.85, solid_capstyle='round')
for lw, a in [(12, 0.05), (8, 0.1), (5, 0.15)]:
    ax_well.plot([-ex1_width, ex1_width], [ex1_y, ex1_y], color=GREEN_GLOW,
                 linewidth=lw, alpha=a, solid_capstyle='round')

ax_well.text(1.15, ex1_y,
             'm_p = 938 MeV  (1st excitation)',
             fontsize=9, color=GREEN_GLOW, ha='left', va='center',
             fontfamily='monospace', fontweight='bold',
             path_effects=[pe.withStroke(linewidth=2, foreground='#44ff8830')])

# Higher states (dimmer)
higher_states = [
    (1.1, 1.48, 'Δ baryon  (1232 MeV)', 0.5),
    (1.6, 1.79, 'N* resonances', 0.3),
    (2.0, 2.00, 'heavier hadrons', 0.18),
]
for hs_y, hs_w, hs_label, hs_alpha in higher_states:
    ax_well.plot([-hs_w, hs_w], [hs_y, hs_y], color=GREEN_DIM,
                 linewidth=2, alpha=hs_alpha, solid_capstyle='round')
    ax_well.text(hs_w + 0.08, hs_y, hs_label,
                 fontsize=7, color=GREEN_DIM, ha='left', va='center',
                 fontfamily='monospace', alpha=hs_alpha + 0.1)

# ─── Radial prediction lines and boxes ───
# Predictions arranged in an arc around the well
n_pred = len(PREDICTIONS)
# Angular range — fan from upper left to upper right, wrapping around
angles = np.linspace(np.pi * 0.92, -np.pi * 0.08, n_pred)

# Origin points: alternate between ground state and first excitation
well_center_x = 0.0
well_center_y = 0.28  # midpoint between gs and ex1

pred_radius = 2.15
pred_lines = []
pred_boxes = []
pred_labels = []

for i, (label, color, hint) in enumerate(PREDICTIONS):
    angle = angles[i]
    # Endpoint
    ex = well_center_x + pred_radius * np.cos(angle)
    ey = well_center_y + pred_radius * np.sin(angle)

    # Origin — from the well center area
    ox = well_center_x + 0.3 * np.cos(angle)
    oy = well_center_y + 0.3 * np.sin(angle)

    # Draw the line (will be animated with pulsing)
    line, = ax_well.plot([ox, ex], [oy, ey], color=color,
                         linewidth=1.0, alpha=0.35, linestyle='-')
    pred_lines.append(line)

    # Glow dot at endpoint
    dot = ax_well.plot(ex, ey, 'o', color=color, markersize=5, alpha=0.7,
                       markeredgecolor='white', markeredgewidth=0.3)[0]

    # Text label
    ha = 'left' if np.cos(angle) >= 0 else 'right'
    text_offset = 0.12 if np.cos(angle) >= 0 else -0.12
    txt = ax_well.text(ex + text_offset, ey, label,
                       fontsize=8, color=color, ha=ha, va='center',
                       fontfamily='monospace', fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.25', facecolor=BG,
                                 edgecolor=color, linewidth=0.8, alpha=0.85),
                       path_effects=[pe.withStroke(linewidth=1,
                                                   foreground=color + '30')])
    pred_labels.append(txt)

# Legend for categories
legend_items = [
    ('masses', C_MASS), ('couplings', C_COUPLING),
    ('topology', C_TOPO), ('cosmology', C_COSMO),
]
for j, (lbl, col) in enumerate(legend_items):
    ax_well.plot(-2.35, 2.9 - j * 0.18, 's', color=col, markersize=6)
    ax_well.text(-2.2, 2.9 - j * 0.18, lbl, fontsize=7, color=col,
                 va='center', fontfamily='monospace')

# ═══════════════════════════════════════════════════════════════════
# BOTTOM-LEFT: Observer Feedback Loop
# ═══════════════════════════════════════════════════════════════════
ax_loop = fig.add_axes([0.02, 0.02, 0.38, 0.20])
ax_loop.set_facecolor(BG)
ax_loop.axis('off')
ax_loop.set_xlim(-1.8, 1.8)
ax_loop.set_ylim(-0.9, 0.9)
ax_loop.set_aspect('equal')

# Title
ax_loop.text(0.0, 0.82, 'THE OBSERVER FEEDBACK LOOP',
             fontsize=11, fontweight='bold', color=CYAN, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#00ccff30')])

# Draw the spiral cycle — 5 nodes in a circle
cycle_labels = [
    'Commitment',
    'ρ increases',
    'Gravitational\nbinding',
    'Concentrates\ncontacts',
    'More\ncommitments',
]
cycle_colors = ['#ff8800', '#ffcc00', '#44ff88', '#4488ff', '#cc66ff']
n_nodes = len(cycle_labels)
cycle_r = 0.52
cycle_cx, cycle_cy = 0.0, 0.12

# Node positions
node_positions = []
for k in range(n_nodes):
    theta = np.pi/2 + 2 * np.pi * k / n_nodes
    nx = cycle_cx + cycle_r * np.cos(theta)
    ny = cycle_cy + cycle_r * np.sin(theta)
    node_positions.append((nx, ny))

# Draw curved arrows between nodes
spiral_lines = []
for k in range(n_nodes):
    x1, y1 = node_positions[k]
    x2, y2 = node_positions[(k + 1) % n_nodes]
    # Intermediate point offset toward center for slight curve
    mx = (x1 + x2) / 2 + 0.08 * (y2 - y1)
    my = (y1 + y2) / 2 - 0.08 * (x2 - x1)
    t_vals = np.linspace(0, 1, 30)
    xs = (1 - t_vals)**2 * x1 + 2 * (1 - t_vals) * t_vals * mx + t_vals**2 * x2
    ys = (1 - t_vals)**2 * y1 + 2 * (1 - t_vals) * t_vals * my + t_vals**2 * y2
    line, = ax_loop.plot(xs, ys, color=cycle_colors[k], linewidth=1.5, alpha=0.5)
    spiral_lines.append(line)
    # Arrowhead
    dx = x2 - xs[-3]
    dy = y2 - ys[-3]
    ax_loop.annotate('', xy=(x2, y2), xytext=(xs[-3], ys[-3]),
                     arrowprops=dict(arrowstyle='->', color=cycle_colors[k],
                                     lw=1.5, mutation_scale=12))

# Node labels
node_texts = []
for k in range(n_nodes):
    nx, ny = node_positions[k]
    txt = ax_loop.text(nx, ny, cycle_labels[k],
                       fontsize=6.5, color=cycle_colors[k], ha='center',
                       va='center', fontfamily='monospace', fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.2', facecolor=BG,
                                 edgecolor=cycle_colors[k], linewidth=0.8,
                                 alpha=0.9))
    node_texts.append(txt)

# Cycle center label
ax_loop.text(cycle_cx, cycle_cy, '∞', fontsize=18, color=GOLD,
             ha='center', va='center', alpha=0.3)

# Caption below
ax_loop.text(0.0, -0.78,
             'The universe becomes more real where\nobservers actively discover it',
             fontsize=7.5, color='#888899', ha='center', fontfamily='serif',
             fontstyle='italic', linespacing=1.4)

# ═══════════════════════════════════════════════════════════════════
# BOTTOM-RIGHT: The Five Integers
# ═══════════════════════════════════════════════════════════════════
ax_int = fig.add_axes([0.62, 0.02, 0.36, 0.20])
ax_int.set_facecolor(BG)
ax_int.axis('off')
ax_int.set_xlim(0, 1)
ax_int.set_ylim(0, 1)

# Title
ax_int.text(0.5, 0.95, 'THE FIVE INTEGERS',
            fontsize=12, fontweight='bold', color=ORANGE, ha='center',
            fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=2, foreground='#ff880030')])

# Fundamental three
fund_data = [
    ('N_c', '= 3', 'colors', '#ff4466'),
    ('n_C', '= 5', 'complex dim', '#4488ff'),
    ('N_max', '= 137', 'capacity', '#ffd700'),
]
for j, (sym, val, desc, col) in enumerate(fund_data):
    x_pos = 0.12 + j * 0.28
    ax_int.text(x_pos, 0.78, sym, fontsize=14, fontweight='bold',
                color=col, ha='center', fontfamily='monospace')
    ax_int.text(x_pos, 0.65, val, fontsize=12, color=WHITE,
                ha='center', fontfamily='monospace')
    ax_int.text(x_pos, 0.56, desc, fontsize=7, color='#888899',
                ha='center', fontfamily='monospace')

# Derived two
ax_int.text(0.12, 0.43, 'g = 7', fontsize=10, color='#cc8844',
            ha='center', fontfamily='monospace')
ax_int.text(0.12, 0.36, 'genus', fontsize=7, color='#888899',
            ha='center', fontfamily='monospace')

ax_int.text(0.38, 0.43, 'N_w = 2', fontsize=10, color='#cc8844',
            ha='center', fontfamily='monospace')
ax_int.text(0.38, 0.36, 'weak', fontsize=7, color='#888899',
            ha='center', fontfamily='monospace')

ax_int.text(0.72, 0.43, 'derived', fontsize=8, color='#666677',
            ha='center', fontfamily='monospace', fontstyle='italic')

# Separator
ax_int.plot([0.05, 0.95], [0.30, 0.30], color=GOLD_DIM, linewidth=0.5, alpha=0.3)

# "Zero free parameters"
ax_int.text(0.5, 0.24, 'Zero free parameters.  56+ predictions.',
            fontsize=9, fontweight='bold', color=GOLD, ha='center',
            fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground='#ffd70020')])

# Precision table
precision_data = [
    ('α', '0.0001%'),
    ('m_p/m_e', '0.002%'),
    ('sin²θ_W', '0.2%'),
    ('Λ', '0.025%'),
]
for j, (sym, prec) in enumerate(precision_data):
    x_s = 0.22 + (j % 2) * 0.40
    y_s = 0.12 if j < 2 else 0.03
    ax_int.text(x_s, y_s, f'{sym}: {prec}', fontsize=7.5,
                color='#aabbcc', ha='center', fontfamily='monospace')

# ═══════════════════════════════════════════════════════════════════
# RIGHT PANEL: Decorative vertical — "One equation → all physics"
# ═══════════════════════════════════════════════════════════════════
ax_right = fig.add_axes([0.72, 0.22, 0.26, 0.58])
ax_right.set_facecolor(BG)
ax_right.axis('off')
ax_right.set_xlim(0, 1)
ax_right.set_ylim(0, 1)

# Vertical cascade of implications
cascade = [
    ('Δ_B on D_IV⁵', GOLD, 0.96),
    ('↓', '#666666', 0.91),
    ('α = 1/137.036', C_COUPLING, 0.86),
    ('↓', '#666666', 0.81),
    ('m_p = 6π⁵ m_e', C_MASS, 0.76),
    ('↓', '#666666', 0.71),
    ('sin²θ_W = 3/13', C_COUPLING, 0.66),
    ('↓', '#666666', 0.61),
    ('G = ℏc(6π⁵α¹²)²/m_e²', C_COSMO, 0.56),
    ('↓', '#666666', 0.51),
    ('Λ = α⁵⁶ e⁻² / 50', C_COSMO, 0.46),
    ('↓', '#666666', 0.41),
    ('N_gen = 3', C_TOPO, 0.36),
    ('↓', '#666666', 0.31),
    ('θ_QCD = 0', C_TOPO, 0.26),
    ('↓', '#666666', 0.21),
    ('proton stable', C_TOPO, 0.16),
    ('↓', '#666666', 0.11),
    ('singularity resolved', C_TOPO, 0.06),
]

for text, col, yp in cascade:
    fs = 7 if text != '↓' else 8
    fw = 'bold' if text != '↓' else 'normal'
    alpha_v = 0.9 if text != '↓' else 0.3
    ax_right.text(0.5, yp, text, fontsize=fs, color=col, ha='center',
                  fontfamily='monospace', fontweight=fw, alpha=alpha_v)

ax_right.text(0.5, 1.0, 'ONE EQUATION', fontsize=9, fontweight='bold',
              color=GOLD_DIM, ha='center', fontfamily='monospace', alpha=0.6)
ax_right.text(0.5, 0.01, 'ALL OF PHYSICS', fontsize=9, fontweight='bold',
              color=GOLD_DIM, ha='center', fontfamily='monospace', alpha=0.6)

# ═══════════════════════════════════════════════════════════════════
# Animation — pulsing radial lines and rotating feedback loop
# ═══════════════════════════════════════════════════════════════════
frame_count = [0]

def animate(frame):
    """Animate pulsing prediction lines and rotating cycle highlights."""
    t = frame / 60.0  # normalized time

    # ─── Pulse the radial prediction lines ───
    for i, line in enumerate(pred_lines):
        # Each line pulses with a phase offset
        phase = t * 2.0 + i * 0.5
        pulse = 0.25 + 0.25 * np.sin(phase)
        line.set_alpha(pulse)
        # Slight linewidth variation
        lw = 0.8 + 0.6 * np.sin(phase)
        line.set_linewidth(lw)

    # ─── Rotate highlight around the feedback loop ───
    active_node = int(t * 1.2) % n_nodes
    for k in range(n_nodes):
        if k == active_node:
            node_texts[k].set_fontsize(7.5)
            node_texts[k].set_alpha(1.0)
            node_texts[k].get_bbox_patch().set_linewidth(1.8)
        else:
            node_texts[k].set_fontsize(6.5)
            node_texts[k].set_alpha(0.65)
            node_texts[k].get_bbox_patch().set_linewidth(0.8)

    # Highlight the active arrow
    for k, sline in enumerate(spiral_lines):
        if k == active_node:
            sline.set_alpha(0.9)
            sline.set_linewidth(2.5)
        else:
            sline.set_alpha(0.35)
            sline.set_linewidth(1.2)

    # ─── Subtle glow pulse on the ground state ───
    # (We use the frame to slightly shift the title alpha for a breathing effect)
    breath = 0.85 + 0.15 * np.sin(t * 1.5)
    # Can't easily animate text alpha without redrawing, so we skip heavy redraws

    frame_count[0] += 1
    return pred_lines + spiral_lines + node_texts


# ─── Click handler: highlight a prediction ───
highlight_box = [None]

def on_click(event):
    """Click on a prediction to highlight it."""
    if event.inaxes != ax_well:
        return
    # Check proximity to each prediction endpoint
    for i, (label, color, hint) in enumerate(PREDICTIONS):
        angle = np.linspace(np.pi * 0.92, -np.pi * 0.08, n_pred)[i]
        ex = well_center_x + pred_radius * np.cos(angle)
        ey = well_center_y + pred_radius * np.sin(angle)
        dist = np.sqrt((event.xdata - ex)**2 + (event.ydata - ey)**2)
        if dist < 0.3:
            # Remove old highlight
            if highlight_box[0] is not None:
                highlight_box[0].remove()
                highlight_box[0] = None
            # Show formula hint
            txt = ax_well.text(0, 2.8, f'  {label}  —  {hint}  ',
                               fontsize=12, color=color, ha='center',
                               fontfamily='monospace', fontweight='bold',
                               bbox=dict(boxstyle='round,pad=0.4',
                                         facecolor='#1a1a2e',
                                         edgecolor=color, linewidth=2),
                               path_effects=[pe.withStroke(linewidth=2,
                                                           foreground=color + '40')])
            highlight_box[0] = txt
            fig.canvas.draw_idle()
            return

fig.canvas.mpl_connect('button_press_event', on_click)

# ─── Start animation ───
anim = FuncAnimation(fig, animate, interval=50, blit=False, cache_frame_data=False)

plt.show()
