#!/usr/bin/env python3
"""
THE 1920 CANCELLATION
=====================
The most striking arithmetic fact in BST:
  The same group Γ (order 1920) appears as BOTH the volume denominator
  AND the baryon orbit size — and they cancel perfectly.

  m_p/m_e = C₂ × |Γ| × (π⁵/|Γ|) = C₂ × π⁵ = 6π⁵ = 1836.15

This toy visualizes the cancellation step by step.

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
from matplotlib.animation import FuncAnimation
import matplotlib.patheffects as pe
from itertools import permutations

# ─── Constants ───
n_C = 5
N_c = 3
C2 = n_C + 1                           # = 6
factorial_nC = 120                       # 5!
signs = 2**(n_C - 1)                    # = 16
Gamma_order = factorial_nC * signs       # = 1920
Hua_volume = np.pi**n_C / Gamma_order    # π⁵/1920
proton_ratio = C2 * np.pi**n_C           # 6π⁵
observed = 1836.15267

# ─── Figure ───
fig = plt.figure(figsize=(16, 11), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('The 1920 Cancellation — BST')

fig.text(0.5, 0.97, 'THE 1920 CANCELLATION', fontsize=26, fontweight='bold',
         color='#ff8800', ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
fig.text(0.5, 0.94, 'One group, two roles, perfect cancellation',
         fontsize=13, color='#aa8844', ha='center', fontfamily='monospace')

# ─── Panel 1: The Group Γ ───
ax_group = fig.add_axes([0.03, 0.52, 0.30, 0.38])
ax_group.set_facecolor('#0a0a1a')
ax_group.axis('off')
ax_group.set_xlim(0, 1)
ax_group.set_ylim(0, 1)

ax_group.text(0.5, 0.95, 'THE GROUP Γ', fontsize=16, fontweight='bold',
              color='#ffaa00', ha='center', fontfamily='monospace')

ax_group.text(0.5, 0.85, 'Γ = S₅ × (Z₂)⁴', fontsize=14,
              color='#ffffff', ha='center', fontfamily='monospace',
              bbox=dict(boxstyle='round,pad=0.4', facecolor='#2a1a0a',
                        edgecolor='#aa6600', linewidth=2))

ax_group.text(0.5, 0.72, f'S₅ = permutations of 5 colors', fontsize=11,
              color='#ccaa66', ha='center', fontfamily='monospace')
ax_group.text(0.5, 0.65, f'|S₅| = 5! = {factorial_nC}', fontsize=11,
              color='#ccaa66', ha='center', fontfamily='monospace')

ax_group.text(0.5, 0.53, f'(Z₂)⁴ = phase signs (±1)⁴', fontsize=11,
              color='#cc8844', ha='center', fontfamily='monospace')
ax_group.text(0.5, 0.46, f'|(Z₂)⁴| = 2⁴ = {signs}', fontsize=11,
              color='#cc8844', ha='center', fontfamily='monospace')

ax_group.text(0.5, 0.32, f'|Γ| = {factorial_nC} × {signs} = {Gamma_order}',
              fontsize=16, fontweight='bold',
              color='#ffcc00', ha='center', fontfamily='monospace',
              bbox=dict(boxstyle='round,pad=0.4', facecolor='#2a2a0a',
                        edgecolor='#aaaa00', linewidth=2))

ax_group.text(0.5, 0.18, 'This is the Weyl group of type B₅', fontsize=10,
              color='#888866', ha='center', fontfamily='monospace')
ax_group.text(0.5, 0.10, '(= hyperoctahedral group in 5D)', fontsize=10,
              color='#888866', ha='center', fontfamily='monospace')

# ─── Panel 2: Role 1 — Hua Volume ───
ax_vol = fig.add_axes([0.36, 0.52, 0.30, 0.38])
ax_vol.set_facecolor('#0a0a1a')
ax_vol.axis('off')
ax_vol.set_xlim(0, 1)
ax_vol.set_ylim(0, 1)

ax_vol.text(0.5, 0.95, 'ROLE 1: HUA VOLUME', fontsize=14, fontweight='bold',
            color='#4488ff', ha='center', fontfamily='monospace')

ax_vol.text(0.5, 0.82, 'Vol(D_IV⁵) = π⁵ / |Γ|', fontsize=14,
            color='#ffffff', ha='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#0a1a2a',
                      edgecolor='#4488ff', linewidth=2))

ax_vol.text(0.5, 0.68, f'= π⁵ / {Gamma_order}', fontsize=13,
            color='#88aaff', ha='center', fontfamily='monospace')
ax_vol.text(0.5, 0.60, f'= {Hua_volume:.6f}', fontsize=12,
            color='#6688cc', ha='center', fontfamily='monospace')

ax_vol.text(0.5, 0.45, 'Hua (1963): The volume of a\n'
            'Type IV bounded symmetric domain\n'
            'is π^n divided by the order of its\n'
            'Weyl group.', fontsize=9,
            color='#6688aa', ha='center', fontfamily='monospace',
            linespacing=1.5)

ax_vol.text(0.5, 0.18, 'The Bergman metric determinant\n'
            'expansion produces exactly |Γ|\n'
            'as the denominator.',
            fontsize=9, color='#446688', ha='center',
            fontfamily='monospace', linespacing=1.5)

# ─── Panel 3: Role 2 — Baryon Orbit ───
ax_orb = fig.add_axes([0.68, 0.52, 0.30, 0.38])
ax_orb.set_facecolor('#0a0a1a')
ax_orb.axis('off')
ax_orb.set_xlim(0, 1)
ax_orb.set_ylim(0, 1)

ax_orb.text(0.5, 0.95, 'ROLE 2: BARYON ORBIT', fontsize=14, fontweight='bold',
            color='#ff4488', ha='center', fontfamily='monospace')

ax_orb.text(0.5, 0.82, '|orbit| = n_C! × 2^(n_C-1)', fontsize=14,
            color='#ffffff', ha='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#2a0a1a',
                      edgecolor='#ff4488', linewidth=2))

ax_orb.text(0.5, 0.68, f'= {factorial_nC} × {signs} = {Gamma_order}', fontsize=13,
            color='#ff88aa', ha='center', fontfamily='monospace')

ax_orb.text(0.5, 0.53, 'The Z₃ baryon circuit on D_IV⁵\n'
            'visits |Γ| equivalent configurations:', fontsize=9,
            color='#cc6688', ha='center', fontfamily='monospace', linespacing=1.5)

ax_orb.text(0.5, 0.38, f'• {factorial_nC} color permutations (S₅)',
            fontsize=10, color='#ff88aa', ha='center', fontfamily='monospace')
ax_orb.text(0.5, 0.30, f'• {signs} phase signs ((Z₂)⁴)',
            fontsize=10, color='#ff88aa', ha='center', fontfamily='monospace')

ax_orb.text(0.5, 0.15, 'The group that counts the\nbaryon states IS the same group.',
            fontsize=10, color='#cc4466', ha='center',
            fontfamily='monospace', linespacing=1.5, fontweight='bold')

# ─── Panel 4: The Cancellation ───
ax_cancel = fig.add_axes([0.05, 0.05, 0.90, 0.42])
ax_cancel.set_facecolor('#0a0a1a')
ax_cancel.axis('off')
ax_cancel.set_xlim(0, 10)
ax_cancel.set_ylim(0, 5)

# Step-by-step cancellation
steps = [
    (0.5, 4.3, 'THE PROTON MASS FORMULA', '#ffffff', 16, 'bold'),
    (0.5, 3.5, 'm_p / m_e  =  C₂  ×  |Γ|  ×  Vol(D_IV⁵)', '#ffcc00', 14, 'bold'),
    (0.5, 2.7, f'          =   {C2}   ×  {Gamma_order}  ×  (π⁵ / {Gamma_order})', '#ff8800', 14, 'normal'),
]

for x_frac, y, text, color, size, weight in steps:
    ax_cancel.text(x_frac * 10, y, text, fontsize=size, fontweight=weight,
                   color=color, ha='center', fontfamily='monospace')

# The cancellation with strikethrough effect
ax_cancel.text(5, 2.0, f'          =   {C2}   ×  ', fontsize=14,
               color='#ff8800', ha='right', fontfamily='monospace')

# Cancelled terms
ax_cancel.text(5.0, 2.0, f'{Gamma_order}', fontsize=14,
               color='#ff3333', ha='left', fontfamily='monospace',
               path_effects=[pe.withStroke(linewidth=3, foreground='#ff3333')])
# Strikethrough line
ax_cancel.plot([4.95, 5.65], [2.0, 2.0], color='#ff0000', linewidth=3, alpha=0.8)

ax_cancel.text(5.7, 2.0, '  ×  π⁵ / ', fontsize=14,
               color='#ff8800', ha='left', fontfamily='monospace')

ax_cancel.text(7.35, 2.0, f'{Gamma_order}', fontsize=14,
               color='#ff3333', ha='left', fontfamily='monospace')
ax_cancel.plot([7.3, 8.0], [2.0, 2.0], color='#ff0000', linewidth=3, alpha=0.8)

# Final result
ax_cancel.text(5, 1.1, f'=   {C2}  ×  π⁵   =   6π⁵', fontsize=18,
               fontweight='bold', color='#00ff88', ha='center',
               fontfamily='monospace',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='#0a2a1a',
                         edgecolor='#00ff88', linewidth=2))

ax_cancel.text(5, 0.3, f'=  {proton_ratio:.5f}    (observed: {observed}    error: {abs(proton_ratio-observed)/observed*100:.3f}%)',
               fontsize=13, color='#88ffaa', ha='center', fontfamily='monospace')

# ─── Arrow connecting the two 1920s ───
# Draw a large curved arrow from Role 1 to Role 2 through the cancellation
ax_cancel.annotate('SAME\nGROUP', xy=(5, 4.5), fontsize=11,
                   color='#ffaa00', ha='center', fontfamily='monospace',
                   fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a2a0a',
                             edgecolor='#ffaa00', alpha=0.8))

# ─── Permutation visualizer in corner ───
# Show a few of the 120 permutations of S₅
ax_perm = fig.add_axes([0.80, 0.05, 0.18, 0.20])
ax_perm.set_facecolor('#0a0a1a')
ax_perm.axis('off')
ax_perm.set_xlim(0, 1)
ax_perm.set_ylim(0, 1)

ax_perm.text(0.5, 0.95, 'S₅ samples', fontsize=9, color='#888888',
             ha='center', fontfamily='monospace')

# Show 8 random permutations
rng = np.random.RandomState(42)
colors_5 = ['R', 'G', 'B', 'Y', 'W']
color_map = {'R': '#ff4444', 'G': '#44ff44', 'B': '#4488ff',
             'Y': '#ffff44', 'W': '#ffffff'}

perms_list = list(permutations(colors_5))
sample_indices = rng.choice(len(perms_list), size=8, replace=False)

for j, idx in enumerate(sample_indices):
    p = perms_list[idx]
    y = 0.85 - j * 0.10
    for k, c in enumerate(p):
        ax_perm.text(0.15 + k * 0.15, y, c, fontsize=8,
                     color=color_map[c], ha='center', fontfamily='monospace')
    ax_perm.text(0.92, y, f'#{idx+1}', fontsize=7, color='#555555',
                 ha='center', fontfamily='monospace')

ax_perm.text(0.5, 0.02, f'... {factorial_nC} total', fontsize=8,
             color='#555555', ha='center', fontfamily='monospace')

plt.show()
