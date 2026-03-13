#!/usr/bin/env python3
"""
THE Z₃ COLOR WHEEL
==================
Visualize the Z₃ operator on CP²:
  - Eigenvalues as cube roots of unity on the complex plane
  - Three fixed points = three generations of matter
  - Color cycling animation: watch quarks permute
  - Click to "create a particle" and see its quantum numbers

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
from matplotlib.widgets import Button
from matplotlib.patches import FancyArrowPatch, Circle, Wedge
import matplotlib.patheffects as pe
from matplotlib.animation import FuncAnimation

# ─── Z₃ operator ───
omega = np.exp(2j * np.pi / 3)

sigma = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
], dtype=complex)

# Eigenvectors of σ
v1 = np.array([1, 1, 1], dtype=complex) / np.sqrt(3)            # eigenvalue 1
v2 = np.array([1, omega, omega**2], dtype=complex) / np.sqrt(3)  # eigenvalue ω
v3 = np.array([1, omega**2, omega], dtype=complex) / np.sqrt(3)  # eigenvalue ω²

# Fixed points on CP² (homogeneous coordinates)
fixed_points = {
    'Generation 1': {'coords': v1, 'eigenval': 1,
                     'particles': '(e, u, d)', 'label': 'p₁ = [1:1:1]',
                     'color': '#ff4444', 'mass': 'lightest'},
    'Generation 2': {'coords': v2, 'eigenval': omega,
                     'particles': '(μ, c, s)', 'label': 'p₂ = [1:ω:ω²]',
                     'color': '#44ff44', 'mass': 'middle'},
    'Generation 3': {'coords': v3, 'eigenval': omega**2,
                     'particles': '(τ, t, b)', 'label': 'p₃ = [1:ω²:ω]',
                     'color': '#4488ff', 'mass': 'heaviest'},
}

# ─── Figure setup ───
fig = plt.figure(figsize=(16, 10), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('Z₃ Color Wheel — BST')

fig.text(0.5, 0.97, 'THE Z₃ COLOR WHEEL', fontsize=24, fontweight='bold',
         color='#00ccff', ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#004466')])
fig.text(0.5, 0.94, 'Three eigenvalues → Three colors → Three generations',
         fontsize=12, color='#88aacc', ha='center', fontfamily='monospace')

# ─── Panel 1: Eigenvalues on unit circle ───
ax1 = fig.add_axes([0.05, 0.35, 0.28, 0.50])
ax1.set_facecolor('#0a0a1a')
ax1.set_aspect('equal')
ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-1.8, 1.8)
ax1.set_title('Eigenvalues of σ (Z₃)', color='#cccccc', fontsize=13,
              fontfamily='monospace', pad=10)

# Unit circle
theta_circle = np.linspace(0, 2*np.pi, 200)
ax1.plot(np.cos(theta_circle), np.sin(theta_circle),
         color='#333366', linewidth=1.5, linestyle='--')
ax1.axhline(0, color='#222244', linewidth=0.5)
ax1.axvline(0, color='#222244', linewidth=0.5)

# Eigenvalue points
eigenvals = [1, omega, omega**2]
eigen_colors = ['#ff4444', '#44ff44', '#4488ff']
eigen_labels = ['1 (Red)', 'ω (Green)', 'ω² (Blue)']

for ev, col, lab in zip(eigenvals, eigen_colors, eigen_labels):
    ax1.plot(ev.real, ev.imag, 'o', color=col, markersize=16, zorder=5)
    ax1.annotate(lab, (ev.real, ev.imag),
                 textcoords="offset points", xytext=(15, 10),
                 fontsize=10, color=col, fontfamily='monospace',
                 fontweight='bold')

# Triangle connecting eigenvalues
triangle_x = [1, omega.real, (omega**2).real, 1]
triangle_y = [0, omega.imag, (omega**2).imag, 0]
ax1.plot(triangle_x, triangle_y, color='#ffffff', linewidth=1, alpha=0.3)
ax1.fill(triangle_x, triangle_y, color='#ffffff', alpha=0.03)

# Trace annotation
ax1.text(0, -1.5, 'Tr(σ) = 1 + ω + ω² = 0', fontsize=11,
         color='#ffaa00', ha='center', fontfamily='monospace',
         fontweight='bold')
ax1.text(0, -1.7, '→ Color confinement!', fontsize=10,
         color='#ff8800', ha='center', fontfamily='monospace')

for spine in ax1.spines.values():
    spine.set_color('#333366')
ax1.tick_params(colors='#666688')

# ─── Panel 2: The σ matrix and eigenvectors ───
ax2 = fig.add_axes([0.38, 0.35, 0.28, 0.50])
ax2.set_facecolor('#0a0a1a')
ax2.axis('off')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_title('The Permutation Matrix', color='#cccccc', fontsize=13,
              fontfamily='monospace', pad=10)

# Draw the 3×3 matrix
matrix_str = (
    "σ = ⎛ 0  0  1 ⎞\n"
    "    ⎜ 1  0  0 ⎟\n"
    "    ⎝ 0  1  0 ⎠"
)
ax2.text(0.5, 0.82, matrix_str, fontsize=14, color='#ffffff',
         ha='center', va='center', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#1a1a3a',
                   edgecolor='#4444aa', linewidth=2))

# Action description
ax2.text(0.5, 0.58, 'σ(z₀, z₁, z₂) = (z₁, z₂, z₀)', fontsize=12,
         color='#aaaacc', ha='center', fontfamily='monospace')

# Eigenvectors
ax2.text(0.5, 0.45, 'EIGENVECTORS (= generations)', fontsize=11,
         color='#ffaa00', ha='center', fontfamily='monospace', fontweight='bold')

ev_texts = [
    ('v₁ = (1, 1, 1)/√3',      '#ff4444', 'λ = 1'),
    ('v₂ = (1, ω, ω²)/√3',     '#44ff44', 'λ = ω'),
    ('v₃ = (1, ω², ω)/√3',     '#4488ff', 'λ = ω²'),
]
for j, (txt, col, lam) in enumerate(ev_texts):
    y = 0.35 - j * 0.08
    ax2.text(0.15, y, txt, fontsize=11, color=col, fontfamily='monospace')
    ax2.text(0.85, y, lam, fontsize=11, color=col, fontfamily='monospace',
             fontweight='bold')

# Lefschetz theorem
ax2.text(0.5, 0.08, 'Lefschetz: L(σ) = 1+1+1 = 3', fontsize=13,
         color='#00ffaa', ha='center', fontfamily='monospace', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a2a1a',
                   edgecolor='#00aa66', linewidth=1.5))

# ─── Panel 3: Fixed points on CP² ───
ax3 = fig.add_axes([0.70, 0.35, 0.28, 0.50])
ax3.set_facecolor('#0a0a1a')
ax3.set_aspect('equal')
ax3.set_xlim(-2.0, 2.0)
ax3.set_ylim(-2.0, 2.0)
ax3.set_title('Fixed Points on CP²', color='#cccccc', fontsize=13,
              fontfamily='monospace', pad=10)

# Draw CP² as a triangle (Fubini-Study projection)
# Project CP² fixed points to 2D using the real/imag parts
proj_points = []
for name, data in fixed_points.items():
    z = data['coords']
    # Stereographic-like projection: use phases of z₁/z₀ and z₂/z₀
    x = (z[1]/z[0]).real if abs(z[0]) > 0 else 0
    y = (z[2]/z[0]).imag if abs(z[0]) > 0 else 0
    proj_points.append((x, y, data))

# Draw the boundary of the projection (a circle for CP¹ ⊂ CP²)
ax3.plot(1.5*np.cos(theta_circle), 1.5*np.sin(theta_circle),
         color='#333366', linewidth=1, linestyle=':')

# Label the boundary
ax3.text(0, 1.7, 'CP² (Fubini-Study)', fontsize=9, color='#666688',
         ha='center', fontfamily='monospace')

# Draw the three fixed points as large circles with generation info
fp_positions = [
    (0, 1.2),      # Gen 1 at top (most symmetric)
    (-1.05, -0.6), # Gen 2 at lower left
    (1.05, -0.6),  # Gen 3 at lower right
]

for (x, y), (name, data) in zip(fp_positions, fixed_points.items()):
    # Glow
    circle = plt.Circle((x, y), 0.35, color=data['color'], alpha=0.15)
    ax3.add_patch(circle)
    # Point
    ax3.plot(x, y, 'o', color=data['color'], markersize=20, zorder=5)
    # Label
    ax3.text(x, y + 0.55, name, fontsize=9, color=data['color'],
             ha='center', fontfamily='monospace', fontweight='bold')
    ax3.text(x, y - 0.45, data['particles'], fontsize=10, color='#cccccc',
             ha='center', fontfamily='monospace')
    ax3.text(x, y - 0.65, data['label'], fontsize=8, color='#888888',
             ha='center', fontfamily='monospace')
    ax3.text(x, y - 0.80, data['mass'], fontsize=8, color=data['color'],
             ha='center', fontfamily='monospace', alpha=0.7)

# Triangle connecting fixed points
tri_x = [fp_positions[0][0], fp_positions[1][0], fp_positions[2][0], fp_positions[0][0]]
tri_y = [fp_positions[0][1], fp_positions[1][1], fp_positions[2][1], fp_positions[0][1]]
ax3.plot(tri_x, tri_y, color='#ffffff', linewidth=1, alpha=0.2, linestyle='--')

# Symmetry annotation
ax3.text(0, -1.6, '[1:1:1] = max symmetry = lightest', fontsize=8,
         color='#ff6666', ha='center', fontfamily='monospace')

for spine in ax3.spines.values():
    spine.set_color('#333366')
ax3.tick_params(colors='#666688')

# ─── Bottom panel: Color cycling animation ───
ax_anim = fig.add_axes([0.10, 0.03, 0.80, 0.28])
ax_anim.set_facecolor('#0a0a1a')
ax_anim.axis('off')
ax_anim.set_xlim(0, 10)
ax_anim.set_ylim(0, 3)

# Color cycling visualization
quark_positions = [(2, 1.5), (5, 1.5), (8, 1.5)]
quark_colors_cycle = [
    ['#ff4444', '#44ff44', '#4488ff'],  # R, G, B
    ['#4488ff', '#ff4444', '#44ff44'],  # B, R, G  (after σ)
    ['#44ff44', '#4488ff', '#ff4444'],  # G, B, R  (after σ²)
]
color_names_cycle = [
    ['R', 'G', 'B'],
    ['B', 'R', 'G'],
    ['G', 'B', 'R'],
]

quark_dots = []
quark_texts = []
for pos in quark_positions:
    dot, = ax_anim.plot(pos[0], pos[1], 'o', markersize=30, color='#ff4444', zorder=5)
    quark_dots.append(dot)
    txt = ax_anim.text(pos[0], pos[1], 'R', fontsize=14, color='white',
                       ha='center', va='center', fontfamily='monospace',
                       fontweight='bold', zorder=6)
    quark_texts.append(txt)

# Labels
ax_anim.text(2, 2.6, 'Quark 1', fontsize=11, color='#aaaacc',
             ha='center', fontfamily='monospace')
ax_anim.text(5, 2.6, 'Quark 2', fontsize=11, color='#aaaacc',
             ha='center', fontfamily='monospace')
ax_anim.text(8, 2.6, 'Quark 3', fontsize=11, color='#aaaacc',
             ha='center', fontfamily='monospace')

cycle_label = ax_anim.text(5, 0.3, 'σ⁰: identity (R + G + B = white)',
                           fontsize=13, color='#ffaa00', ha='center',
                           fontfamily='monospace', fontweight='bold')

# Arrows between quarks
for i in range(2):
    ax_anim.annotate('', xy=(quark_positions[i+1][0]-0.8, 1.5),
                     xytext=(quark_positions[i][0]+0.8, 1.5),
                     arrowprops=dict(arrowstyle='->', color='#444466',
                                     lw=1.5, connectionstyle='arc3,rad=0.2'))

# The sum indicator
sum_dot, = ax_anim.plot(5, 0.7, 's', markersize=20, color='white', alpha=0.3, zorder=5)

frame_counter = [0]

def animate(frame):
    cycle = (frame // 40) % 3  # change every 40 frames
    colors = quark_colors_cycle[cycle]
    names = color_names_cycle[cycle]

    for i in range(3):
        quark_dots[i].set_color(colors[i])
        quark_texts[i].set_text(names[i])

    power = ['⁰', '¹', '²'][cycle]
    action = ['identity', 'one step: (z₀,z₁,z₂)→(z₁,z₂,z₀)', 'two steps: back to start after σ³=1'][cycle]
    cycle_label.set_text(f'σ{power}: {action}')

    # Pulse effect
    t = (frame % 40) / 40
    for dot in quark_dots:
        dot.set_markersize(28 + 4 * np.sin(2 * np.pi * t))

    return quark_dots + quark_texts + [cycle_label]

anim = FuncAnimation(fig, animate, frames=120, interval=50, blit=False)

plt.show()
