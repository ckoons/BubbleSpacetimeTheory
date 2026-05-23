#!/usr/bin/env python3
"""
Diagram: 4-Zone Commitment Cycle visualization

Elie, Saturday 2026-05-23 15:18 EDT (third pre-staged diagram for Keeper authorship)

Visualizes the Substrate Working Process Principle (SWPP) 4-Zone Commitment Cycle:
Zone 1 (absorption) → Zone 2 (bulk) → Zone 3 (emission) → Zone 4 (outer-edge)
+ feedback back to Zone 1.

Per Casey-named SWPP principle (Tuesday May 19) + T2420 4-Zone Vacuum Decomposition
(Lyra+Elie joint Wednesday May 20).

Output: PNG (300 DPI) + PDF
Target: Vol 0 Ch 11 (Substrate Cognition Network) authorship support
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(11, 11))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(0, 5.5, 'BST 4-Zone Commitment Cycle',
        ha='center', fontsize=18, fontweight='bold')
ax.text(0, 5.0, '(Substrate Working Process Principle, SWPP)',
        ha='center', fontsize=12, style='italic', color='#444')

# Center origin
ax.plot(0, 0, 'o', color='#1F4F8F', markersize=8)
ax.text(0, -0.5, 'substrate origin', ha='center', fontsize=8, color='#1F4F8F')

# Zone definitions: (label, angle_start, angle_end, color, inner_r, outer_r)
# Going clockwise from top: Zone 1 (top), Zone 2 (right), Zone 3 (bottom), Zone 4 (left)
zones = [
    ('Zone 1\nAbsorption', 45, 135, '#FFE4B5', 1.5, 4.0),
    ('Zone 2\nBulk', -45, 45, '#FFA500', 1.5, 4.0),
    ('Zone 3\nEmission', -135, -45, '#FF6347', 1.5, 4.0),
    ('Zone 4\nOuter-Edge', 135, 225, '#DC143C', 1.5, 4.0),
]

# Draw 4 wedges
for label, ang_start, ang_end, color, r_in, r_out in zones:
    wedge = patches.Wedge((0, 0), r_out, ang_start, ang_end,
                           width=r_out - r_in, color=color, ec='black', lw=2, alpha=0.85)
    ax.add_patch(wedge)
    # Place label at midpoint angle, middle radius
    ang_mid = np.radians((ang_start + ang_end) / 2)
    r_label = (r_in + r_out) / 2
    x_lbl = r_label * np.cos(ang_mid)
    y_lbl = r_label * np.sin(ang_mid)
    ax.text(x_lbl, y_lbl, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color='black')

# Inner core (substrate)
inner_circle = patches.Circle((0, 0), 1.5, fill=True, color='#B0D4F1', ec='black', lw=2)
ax.add_patch(inner_circle)
ax.text(0, 0.3, 'Substrate', ha='center', fontsize=10, fontweight='bold')
ax.text(0, -0.1, '$D_{IV}^5$', ha='center', fontsize=12, fontweight='bold')
ax.text(0, -0.5, 'origin', ha='center', fontsize=8, style='italic', color='#444')

# Arrows showing cycle direction (clockwise: 1 → 2 → 3 → 4 → 1)
# Outer arcs
def draw_curved_arrow(ax, theta_start, theta_end, radius, color='#222', lw=2.5):
    """Draw a curved arrow on a circle."""
    angles = np.linspace(np.radians(theta_start), np.radians(theta_end), 50)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    ax.plot(x, y, color=color, lw=lw)
    # Arrowhead at end
    tan_x = -radius * np.sin(angles[-1])
    tan_y = radius * np.cos(angles[-1])
    norm = np.sqrt(tan_x**2 + tan_y**2)
    head_dx = tan_x / norm * 0.3
    head_dy = tan_y / norm * 0.3
    ax.annotate('', xy=(x[-1] + head_dx, y[-1] + head_dy), xytext=(x[-1], y[-1]),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# Cycle arrows: 1→2 (top to right), 2→3 (right to bottom), 3→4 (bottom to left), 4→1 (left to top)
# Going clockwise from 90° down to 0° then -90° then 180° back to 90°
draw_curved_arrow(ax, 80, 10, 4.5)    # 1 → 2 (clockwise)
draw_curved_arrow(ax, -10, -80, 4.5)  # 2 → 3
draw_curved_arrow(ax, -100, -170, 4.5)  # 3 → 4
draw_curved_arrow(ax, 190, 80, 4.5)  # 4 → 1 (closing the cycle, wrap around)

# Cycle phase callouts (outside)
phase_descriptions = [
    (0, 5.2, '1. Read incoming substrate-state\ninto commitment register', '#8B4513'),
    (5.5, 0, '2. Reed-Solomon syndromes\ncomputed + locked', '#B8860B'),
    (0, -5.2, '3. Result emitted to\nnext substrate-cycle', '#8B0000'),
    (-5.5, 0, '4. Feedback to next\nabsorption phase', '#8B0000'),
]
for x, y, text, color in phase_descriptions:
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color=color, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.9))

# BST primary anchors per zone
anchor_text = [
    (2.7, 2.7, '$N_c \\cdot t_{Pl}$', '#4B0082'),  # cycle time
    (2.7, -2.7, '$1/N_{\\max}$', '#4B0082'),  # commitment-rate correction
    (-2.7, -2.7, 'GF(128)', '#4B0082'),  # substrate field
    (-2.7, 2.7, 'M_g = 127', '#4B0082'),  # Mersenne anchor
]
for x, y, text, color in anchor_text:
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color=color)

# Footer references
ax.text(0, -5.7, r'Casey-named principle: Substrate Working Process Principle (SWPP), Tuesday 2026-05-19',
        ha='center', fontsize=9, color='#666', style='italic')
ax.text(0, -5.95, r'T2420 4-Zone Vacuum Decomposition (Lyra+Elie joint, Wednesday 2026-05-20)',
        ha='center', fontsize=9, color='#666', style='italic')

# Top-left framework anchor
ax.text(-5.8, 5.7, '— Vol 0 Ch 11 supporting diagram —',
        ha='left', fontsize=9, color='#888', style='italic')

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_4_zone_commitment_cycle.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_4_zone_commitment_cycle.pdf',
            bbox_inches='tight', facecolor='white')
plt.close()
print("Generated:")
print("  diagram_4_zone_commitment_cycle.png (300 DPI)")
print("  diagram_4_zone_commitment_cycle.pdf")
