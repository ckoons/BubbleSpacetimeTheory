#!/usr/bin/env python3
"""
Diagram: 5-integer cascade tree visualization

Elie, Saturday 2026-05-23 15:10 EDT (diagram pre-staging per Keeper queue)

Produces a visualization of the BST 5 primary integers cascade:
rank=2 → N_c=3 → n_C=5 → C_2=6 → g=7 → N_max=137

Output: PNG (300 DPI) + PDF
Target: Vol 0 Ch 4 (Fundamental Constants) authorship
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(6, 7.5, 'BST Five Primary Integers Cascade',
        ha='center', fontsize=18, fontweight='bold')
ax.text(6, 7.0, r'$\mathrm{rank} \to N_c \to n_C \to C_2 \to g \to N_{\max}$',
        ha='center', fontsize=14, style='italic')

# Node specifications: (x, y, label_top, label_bot, color)
nodes = [
    (1.5, 4, 'rank', '= 2',     '#FFE4B5'),  # moccasin
    (3.5, 4, '$N_c$',  '= 3',     '#FFD700'),  # gold
    (5.5, 4, '$n_C$',  '= 5',     '#FFA500'),  # orange
    (7.5, 4, '$C_2$',  '= 6',     '#FF6347'),  # tomato
    (9.5, 4, '$g$',    '= 7',     '#FF4500'),  # orangered
    (11.5, 4, '$N_{\\max}$', '= 137', '#DC143C'),  # crimson
]

for x, y, lbl_t, lbl_b, color in nodes:
    circle = patches.Circle((x, y), 0.6, color=color, ec='black', lw=2)
    ax.add_patch(circle)
    ax.text(x, y + 0.15, lbl_t, ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(x, y - 0.20, lbl_b, ha='center', va='center', fontsize=12)

# Arrows
arrows = [
    (1.5, 3.5),
    (3.5, 5.5),
    (5.5, 7.5),
    (7.5, 9.5),
    (9.5, 11.5),
]
for x1, x2 in arrows:
    arrow = FancyArrowPatch((x1+0.65, 4), (x2-0.65, 4),
                            arrowstyle='->', mutation_scale=20, lw=2)
    ax.add_patch(arrow)

# Identity annotations below cascade
ax.text(2.5, 3, r'$2 \cdot 2 - 1 = 3$', ha='center', fontsize=10, style='italic', color='#444')
ax.text(4.5, 3, r'$\mathrm{HSD\ dim}_{\mathbb{C}}=n_C$', ha='center', fontsize=10, style='italic', color='#444')
ax.text(6.5, 3, r'$n_C + 1 = C_2$', ha='center', fontsize=10, style='italic', color='#444')
ax.text(8.5, 3, r'$C_2 + 1 = g$', ha='center', fontsize=10, style='italic', color='#444')
ax.text(10.5, 3, r'$N_c^{N_c} \cdot n_C + \mathrm{rank} = N_{\max}$', ha='center', fontsize=10, style='italic', color='#444')

# Examples (physics observables) below
ax.text(6, 2.0, 'Physics observables:', ha='center', fontsize=12, fontweight='bold', color='#222')
ax.text(2.5, 1.5, 'Rank-2 BSD\nGalois group', ha='center', fontsize=9, color='#555')
ax.text(4.5, 1.5, 'QCD\n$N_c=3$ colors', ha='center', fontsize=9, color='#555')
ax.text(6.5, 1.5, '$(2l+1)$ d-orbitals\n5 quasicrystal', ha='center', fontsize=9, color='#555')
ax.text(8.5, 1.5, 'Aromatic 6e⁻\noctahedral coord.', ha='center', fontsize=9, color='#555')
ax.text(10.5, 1.5, 'g f-orbitals\n$\\chi=24/g$', ha='center', fontsize=9, color='#555')

# T2456 reference (anchor on the N_max node)
ax.text(11.5, 5, r'T2456 + T2462', ha='center', fontsize=9, color='#888', style='italic')
ax.text(11.5, 4.85, 'RIGOROUSLY CLOSED', ha='center', fontsize=8, color='#888')

# Footer
ax.text(6, 0.5, r'Source: BST framework; verification Toy 541 + 1543; 25 HSDs uniqueness (T2462)',
        ha='center', fontsize=10, color='#666')
ax.text(6, 0.1, '— Vol 0 Ch 4 supporting diagram —',
        ha='center', fontsize=9, color='#888', style='italic')

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_5_integer_cascade.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_5_integer_cascade.pdf',
            bbox_inches='tight', facecolor='white')
plt.close()
print("Generated:")
print("  diagram_5_integer_cascade.png (300 DPI)")
print("  diagram_5_integer_cascade.pdf")
