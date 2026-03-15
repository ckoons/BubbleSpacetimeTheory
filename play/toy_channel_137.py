#!/usr/bin/env python3
"""
CHANNEL CAPACITY CONSERVATION — N_max = 137
=============================================
The substrate has fixed bandwidth. Every contact point carries exactly
137 Haldane channels. No more, no fewer. This gives:

  - Singularity resolution:  ρ/ρ₁₃₇ ≤ 1  (channel full = time stops)
  - Vacuum bound:            ρ/ρ₁₃₇ ≥ 0  (channel empty = max clock rate)

No infinities. No singularities. Just a full channel.

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
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
import time

# ─── Constants ───
N_MAX = 137
N0 = 1.0  # normalized maximum lapse

# ─── Color utilities ───
def cell_color(index, fill_level):
    """Color for a filled cell: cool blue at low fill, hot orange/red at high fill."""
    t = fill_level / N_MAX  # overall fill fraction
    # Base gradient from deep blue through cyan, gold, to hot red
    if t < 0.25:
        r, g, b = 0.1, 0.3 + 0.4 * (t / 0.25), 0.9
    elif t < 0.5:
        s = (t - 0.25) / 0.25
        r, g, b = 0.1 + 0.5 * s, 0.7 + 0.2 * s, 0.9 - 0.5 * s
    elif t < 0.75:
        s = (t - 0.5) / 0.25
        r, g, b = 0.6 + 0.3 * s, 0.9 - 0.3 * s, 0.4 - 0.3 * s
    elif t < 1.0:
        s = (t - 0.75) / 0.25
        r, g, b = 0.9 + 0.1 * s, 0.6 - 0.4 * s, 0.1 - 0.05 * s
    else:
        r, g, b = 1.0, 0.15, 0.05
    # Per-cell shimmer: slight brightness variation
    shimmer = 0.92 + 0.08 * np.sin(index * 0.5)
    return (min(r * shimmer, 1.0), min(g * shimmer, 1.0), min(b * shimmer, 1.0))

def lapse(fill):
    """Lapse function N/N0 = sqrt(1 - fill/137)."""
    return np.sqrt(max(0.0, 1.0 - fill / N_MAX))

# ─── Figure ───
fig = plt.figure(figsize=(18, 13), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('Channel Capacity Conservation — N_max = 137 — BST')

# Title
fig.text(0.5, 0.975, 'CHANNEL CAPACITY CONSERVATION',
         fontsize=28, fontweight='bold', color='#00ccff', ha='center',
         fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#003366')])
fig.text(0.5, 0.950, 'N_max = 137 at every contact, always',
         fontsize=14, color='#5599bb', ha='center', fontfamily='monospace')

# ═══════════════════════════════════════════════════════════════════
# TOP PANEL: The 137 Slots
# ═══════════════════════════════════════════════════════════════════
ax_slots = fig.add_axes([0.04, 0.72, 0.92, 0.19])
ax_slots.set_facecolor('#0a0a1a')
ax_slots.set_xlim(-0.5, 138.5)
ax_slots.set_ylim(-1.8, 3.5)
ax_slots.axis('off')

ax_slots.text(68.5, 3.2, 'THE 137 HALDANE CHANNELS', fontsize=16,
              fontweight='bold', color='#00aadd', ha='center',
              fontfamily='monospace')

# Draw the 137 cell outlines
cell_patches = []
cell_width = 0.85
cell_height = 1.6
for i in range(N_MAX):
    rect = FancyBboxPatch((i + 0.075, 0), cell_width, cell_height,
                          boxstyle="round,pad=0.02",
                          facecolor='#0a0a1a',
                          edgecolor='#1a3355', linewidth=0.5)
    ax_slots.add_patch(rect)
    cell_patches.append(rect)

# Status text objects
fill_text = ax_slots.text(68.5, -0.8, '', fontsize=13, color='#88ccee',
                          ha='center', fontfamily='monospace', fontweight='bold')
ratio_text = ax_slots.text(68.5, -1.4, '', fontsize=11, color='#6699aa',
                           ha='center', fontfamily='monospace')
channel_full_text = ax_slots.text(68.5, 2.6, '', fontsize=18, fontweight='bold',
                                  color='#ff2200', ha='center',
                                  fontfamily='monospace',
                                  path_effects=[pe.withStroke(linewidth=2,
                                                              foreground='#550000')])
overfill_text = ax_slots.text(68.5, -1.4, '', fontsize=12, fontweight='bold',
                              color='#ff4400', ha='center', fontfamily='monospace')

# Slider for fill level
ax_slider = fig.add_axes([0.12, 0.685, 0.76, 0.022], facecolor='#0d1525')
fill_slider = Slider(ax_slider, '', 0, N_MAX, valinit=0, valstep=1,
                     color='#0066aa', track_color='#0d1525')
fill_slider.valtext.set_color('#00ccff')
fill_slider.valtext.set_fontfamily('monospace')
fill_slider.valtext.set_fontsize(11)
# Slider label
fig.text(0.06, 0.691, 'Fill:', fontsize=12, color='#5599bb',
         fontfamily='monospace', va='center')

# "Try to Overfill" button
ax_btn = fig.add_axes([0.72, 0.66, 0.20, 0.025])
btn_overfill = Button(ax_btn, 'TRY TO OVERFILL',
                      color='#1a0a0a', hovercolor='#331111')
btn_overfill.label.set_color('#ff4422')
btn_overfill.label.set_fontfamily('monospace')
btn_overfill.label.set_fontsize(10)
btn_overfill.label.set_fontweight('bold')

# ═══════════════════════════════════════════════════════════════════
# MIDDLE PANEL: The Lapse Clock
# ═══════════════════════════════════════════════════════════════════
ax_clock = fig.add_axes([0.25, 0.28, 0.50, 0.37])
ax_clock.set_facecolor('#0a0a1a')
ax_clock.set_xlim(-1.6, 1.6)
ax_clock.set_ylim(-1.5, 1.5)
ax_clock.set_aspect('equal')
ax_clock.axis('off')

ax_clock.text(0.0, 1.40, 'THE LAPSE CLOCK', fontsize=16, fontweight='bold',
              color='#00aadd', ha='center', fontfamily='monospace')
ax_clock.text(0.0, 1.22, 'Time dilation from channel loading',
              fontsize=11, color='#446688', ha='center', fontfamily='monospace')

# Clock face
clock_face = Circle((0, 0), 1.05, facecolor='#060612', edgecolor='#1a4466',
                     linewidth=3, zorder=1)
ax_clock.add_patch(clock_face)

# Inner ring glow
for r_offset, alpha in [(1.03, 0.15), (1.01, 0.08)]:
    ring = Circle((0, 0), r_offset, facecolor='none', edgecolor='#0066aa',
                  linewidth=1, alpha=alpha, zorder=2)
    ax_clock.add_patch(ring)

# Tick marks
for i in range(60):
    angle = np.radians(90 - i * 6)
    if i % 5 == 0:
        # Major tick
        r_inner, r_outer = 0.88, 0.98
        lw, color = 2, '#4488aa'
    else:
        # Minor tick
        r_inner, r_outer = 0.93, 0.98
        lw, color = 0.8, '#223344'
    x0, y0 = r_inner * np.cos(angle), r_inner * np.sin(angle)
    x1, y1 = r_outer * np.cos(angle), r_outer * np.sin(angle)
    ax_clock.plot([x0, x1], [y0, y1], color=color, linewidth=lw, zorder=3)

# Hour numbers
for h in range(12):
    angle = np.radians(90 - h * 30)
    x = 0.78 * np.cos(angle)
    y = 0.78 * np.sin(angle)
    label = str(12 if h == 0 else h)
    ax_clock.text(x, y, label, fontsize=9, color='#5588aa', ha='center',
                  va='center', fontfamily='monospace', fontweight='bold', zorder=4)

# Center dot
center_dot = Circle((0, 0), 0.04, facecolor='#00aadd', edgecolor='#00ccff',
                     linewidth=1, zorder=10)
ax_clock.add_patch(center_dot)

# Second hand (will be animated)
hand_line, = ax_clock.plot([0, 0], [0, 0.85], color='#00ccff', linewidth=2.5,
                           zorder=8, solid_capstyle='round')
# Ghost trail for second hand
ghost_lines = []
for i in range(8):
    gl, = ax_clock.plot([0, 0], [0, 0], color='#0066aa',
                        linewidth=1.5, alpha=0.12 * (8 - i) / 8, zorder=7)
    ghost_lines.append(gl)

# Hand glow
hand_glow, = ax_clock.plot([0, 0], [0, 0.85], color='#0088cc', linewidth=5,
                           alpha=0.3, zorder=7, solid_capstyle='round')

# Lapse display
lapse_text = ax_clock.text(0.0, -0.45, '', fontsize=14, color='#00ddff',
                           ha='center', fontfamily='monospace', fontweight='bold')
lapse_formula = ax_clock.text(0.0, -0.60, '', fontsize=11, color='#448899',
                              ha='center', fontfamily='monospace')
clock_status = ax_clock.text(0.0, -0.78, '', fontsize=13, color='#ff4400',
                             ha='center', fontfamily='monospace', fontweight='bold',
                             path_effects=[pe.withStroke(linewidth=2,
                                                         foreground='#330000')])

# ═══════════════════════════════════════════════════════════════════
# BOTTOM PANEL: The Density Regimes
# ═══════════════════════════════════════════════════════════════════
ax_density = fig.add_axes([0.04, 0.04, 0.92, 0.22])
ax_density.set_facecolor('#0a0a1a')
ax_density.set_xlim(-0.05, 1.15)
ax_density.set_ylim(-0.4, 1.4)
ax_density.axis('off')

ax_density.text(0.55, 1.30, 'DENSITY REGIMES', fontsize=16, fontweight='bold',
                color='#00aadd', ha='center', fontfamily='monospace')

# Gradient bar background
bar_left, bar_right = 0.02, 1.02
bar_bottom, bar_top = 0.45, 0.75
n_grad = 300
for i in range(n_grad):
    t = i / (n_grad - 1)
    x = bar_left + t * (bar_right - bar_left)
    # Color: deep blue -> cyan -> gold -> red
    if t < 0.33:
        s = t / 0.33
        r, g, b = 0.02 + 0.05 * s, 0.08 + 0.25 * s, 0.25 + 0.35 * s
    elif t < 0.66:
        s = (t - 0.33) / 0.33
        r, g, b = 0.07 + 0.50 * s, 0.33 + 0.30 * s, 0.60 - 0.20 * s
    else:
        s = (t - 0.66) / 0.34
        r, g, b = 0.57 + 0.43 * s, 0.63 - 0.45 * s, 0.40 - 0.35 * s
    ax_density.axvspan(x, x + (bar_right - bar_left) / n_grad,
                       ymin=0.47, ymax=0.64, color=(r, g, b), alpha=0.85)

# Bar border
from matplotlib.patches import Rectangle
bar_border = Rectangle((bar_left, bar_bottom), bar_right - bar_left,
                        bar_top - bar_bottom, facecolor='none',
                        edgecolor='#2a5577', linewidth=2, zorder=5)
ax_density.add_patch(bar_border)

# Regime annotations
regimes = [
    (0.00, "Vacuum (ρ = 0)", "Maximum clock rate", '#00ccff'),
    (0.15, "Cosmic average", "~10⁻¹²³ ρ₁₃₇  —  almost empty", '#22aacc'),
    (0.60, "Neutron interior", "~10⁻³ ρ₁₃₇  —  partially loaded", '#ccaa44'),
    (1.00, "Event horizon", "ρ = ρ₁₃₇  —  channel full, time stops", '#ff3300'),
]

for x_frac, label, desc, color in regimes:
    x = bar_left + x_frac * (bar_right - bar_left)
    # Tick mark
    ax_density.plot([x, x], [bar_bottom - 0.02, bar_top + 0.02],
                    color=color, linewidth=1.5, alpha=0.7, zorder=6)
    # Label above
    ax_density.text(x, bar_top + 0.10, label, fontsize=9.5, color=color,
                    ha='center', fontfamily='monospace', fontweight='bold', zorder=6)
    # Description below
    ax_density.text(x, bar_bottom - 0.12, desc, fontsize=7.5, color='#668899',
                    ha='center', fontfamily='monospace', zorder=6)

# Current position marker (triangle)
marker_x = [bar_left]
marker_tri, = ax_density.plot(bar_left, bar_top + 0.30, marker='v', markersize=14,
                              color='#00ffcc', markeredgecolor='#00aa88',
                              markeredgewidth=1.5, zorder=10)
marker_line, = ax_density.plot([bar_left, bar_left],
                               [bar_bottom, bar_top + 0.28],
                               color='#00ffcc', linewidth=2, alpha=0.5, zorder=9)

# Conservation statement
ax_density.text(0.52, -0.25,
                'Channel Capacity Conservation:  N_max = 137 everywhere, always.',
                fontsize=12, color='#88bbdd', ha='center', fontfamily='monospace',
                fontweight='bold')
ax_density.text(0.52, -0.38,
                'No infinities.  No singularities.  Just a full channel.',
                fontsize=11, color='#556677', ha='center', fontfamily='monospace')
# 137 appears in FIVE independent ways in BST:
#   1. H_5 numerator (harmonic sum)
#   2. N_max = floor(1/alpha) (channel capacity)
#   3. alpha^{-1} ~ 137.036 (fine-structure constant)
#   4. Shannon channel capacity of D_IV^5
#   5. r_5 = 137/11 (zonal spectral coefficient numerator)

# ═══════════════════════════════════════════════════════════════════
# STATE AND UPDATE LOGIC
# ═══════════════════════════════════════════════════════════════════
state = {
    'fill': 0,
    'clock_angle': np.pi / 2,  # start at 12 o'clock
    'ghost_angles': [np.pi / 2] * 8,
    'overfill_flash_time': 0,
    'last_time': time.time(),
}

def update_slots(fill):
    """Update the 137 cell display for a given fill level."""
    fill = int(round(fill))
    state['fill'] = fill

    # Update cell colors
    for i, patch in enumerate(cell_patches):
        if i < fill:
            c = cell_color(i, fill)
            patch.set_facecolor(c)
            patch.set_edgecolor((min(c[0] + 0.2, 1), min(c[1] + 0.2, 1),
                                 min(c[2] + 0.2, 1)))
            patch.set_linewidth(0.8)
        else:
            patch.set_facecolor('#0a0a1a')
            patch.set_edgecolor('#1a3355')
            patch.set_linewidth(0.5)

    # Special: at 137, all cells go bright red
    if fill == N_MAX:
        for i, patch in enumerate(cell_patches):
            bright = 0.85 + 0.15 * np.sin(i * 0.3)
            patch.set_facecolor((bright, 0.1, 0.05))
            patch.set_edgecolor((1.0, 0.3, 0.1))
            patch.set_linewidth(1.2)

    # Update text
    frac = fill / N_MAX
    fill_text.set_text(f'\u03c1/\u03c1\u2081\u2083\u2087 = {fill}/137 = {frac:.4f}     '
                       f'Fill: {frac * 100:.1f}%')

    N_val = lapse(fill)
    lapse_text.set_text(f'N/N\u2080 = {N_val:.4f}')
    lapse_formula.set_text(f'\u221a(1 \u2212 {fill}/137) = \u221a({max(0, 1 - fill/N_MAX):.4f})')

    # Channel full message
    if fill == N_MAX:
        channel_full_text.set_text('CHANNEL FULL')
        fill_text.set_color('#ff4400')
        clock_status.set_text('TIME FROZEN  \u2014  N = 0')
        center_dot.set_facecolor('#ff2200')
        center_dot.set_edgecolor('#ff4400')
        clock_face.set_edgecolor('#661100')
        lapse_text.set_color('#ff4400')
    else:
        channel_full_text.set_text('')
        clock_status.set_text('')
        # Color transitions based on fill
        if frac < 0.5:
            fill_text.set_color('#88ccee')
            lapse_text.set_color('#00ddff')
            center_dot.set_facecolor('#00aadd')
            center_dot.set_edgecolor('#00ccff')
            clock_face.set_edgecolor('#1a4466')
        elif frac < 0.85:
            fill_text.set_color('#ccaa44')
            lapse_text.set_color('#ddaa22')
            center_dot.set_facecolor('#ccaa00')
            center_dot.set_edgecolor('#ddbb22')
            clock_face.set_edgecolor('#4a3a11')
        else:
            fill_text.set_color('#ff6644')
            lapse_text.set_color('#ff6644')
            center_dot.set_facecolor('#ff4400')
            center_dot.set_edgecolor('#ff6622')
            clock_face.set_edgecolor('#551100')

    # Update density marker
    x = bar_left + frac * (bar_right - bar_left)
    marker_tri.set_data([x], [bar_top + 0.30])
    marker_line.set_data([x, x], [bar_bottom, bar_top + 0.28])

    # Marker color
    if frac < 0.5:
        mc = '#00ffcc'
    elif frac < 0.85:
        mc = '#ffcc00'
    else:
        mc = '#ff4400'
    marker_tri.set_color(mc)
    marker_tri.set_markeredgecolor(mc)
    marker_line.set_color(mc)

    # Ratio text
    if fill == 0:
        ratio_text.set_text('Vacuum: all channels empty \u2014 maximum passage of time')
        ratio_text.set_color('#00bbcc')
    elif fill == N_MAX:
        ratio_text.set_text('')
        overfill_text.set_text('')
    elif fill > 120:
        ratio_text.set_text(f'Approaching horizon... only {N_MAX - fill} channels remain')
        ratio_text.set_color('#ff6644')
    else:
        ratio_text.set_text(f'{fill} channels occupied, {N_MAX - fill} available')
        ratio_text.set_color('#6699aa')

def on_slider(val):
    """Slider callback."""
    update_slots(val)

fill_slider.on_changed(on_slider)

def on_overfill(event):
    """Button callback: flash impossibility message."""
    state['overfill_flash_time'] = time.time()
    # Force slider to 137
    fill_slider.set_val(N_MAX)

btn_overfill.on_clicked(on_overfill)

# ═══════════════════════════════════════════════════════════════════
# ANIMATION: Clock ticking
# ═══════════════════════════════════════════════════════════════════
def animate(frame):
    """Advance the clock hand proportional to the lapse."""
    now = time.time()
    dt = now - state['last_time']
    state['last_time'] = now

    fill = state['fill']
    N_val = lapse(fill)

    # Advance angle: full speed = 2*pi per 4 seconds (one revolution = 4s at vacuum)
    # Scale by lapse
    omega = 2.0 * np.pi / 4.0  # base angular velocity
    d_angle = omega * dt * N_val
    state['clock_angle'] -= d_angle  # clockwise

    # Update ghost trail (previous positions)
    state['ghost_angles'] = [state['clock_angle']] + state['ghost_angles'][:-1]

    angle = state['clock_angle']
    hand_len = 0.85

    # Second hand
    x1 = hand_len * np.cos(angle)
    y1 = hand_len * np.sin(angle)
    hand_line.set_data([0, x1], [0, y1])
    hand_glow.set_data([0, x1], [0, y1])

    # Hand color: bright when moving, dim when slow
    if N_val > 0.5:
        hand_line.set_color('#00ccff')
        hand_glow.set_color('#0088cc')
        hand_glow.set_alpha(0.3 * N_val)
    elif N_val > 0.1:
        t = N_val / 0.5
        hand_line.set_color((1.0 - 0.5 * t, 0.5 * t + 0.3, 0.2 * t + 0.1))
        hand_glow.set_color('#553300')
        hand_glow.set_alpha(0.2 * N_val)
    else:
        hand_line.set_color('#661100')
        hand_glow.set_alpha(0.05)

    if fill == N_MAX:
        hand_line.set_color('#440000')
        hand_glow.set_alpha(0.0)

    # Ghost trail
    for i, gl in enumerate(ghost_lines):
        ga = state['ghost_angles'][i]
        trail_len = hand_len * (0.85 - i * 0.06)
        gx = trail_len * np.cos(ga)
        gy = trail_len * np.sin(ga)
        gl.set_data([0, gx], [0, gy])
        if N_val > 0.1:
            gl.set_alpha(0.10 * (8 - i) / 8 * N_val)
        else:
            gl.set_alpha(0.0)

    # Overfill flash message
    if state['overfill_flash_time'] > 0:
        elapsed = now - state['overfill_flash_time']
        if elapsed < 3.0:
            # Blinking effect
            if int(elapsed * 6) % 2 == 0:
                overfill_text.set_text('IMPOSSIBLE \u2014 N_max = 137 is absolute')
                overfill_text.set_color('#ff2200')
            else:
                overfill_text.set_text('IMPOSSIBLE \u2014 N_max = 137 is absolute')
                overfill_text.set_color('#aa1100')
        else:
            overfill_text.set_text('')
            state['overfill_flash_time'] = 0

    return (hand_line, hand_glow, *ghost_lines, overfill_text,
            fill_text, ratio_text, channel_full_text, lapse_text,
            lapse_formula, clock_status, marker_tri, marker_line)

# Initialize display
update_slots(0)

# Run animation at 30 fps
anim = FuncAnimation(fig, animate, interval=33, blit=False, cache_frame_data=False)

plt.subplots_adjust(left=0.04, right=0.96, top=0.94, bottom=0.04)
plt.show()
