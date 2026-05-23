#!/usr/bin/env python3
"""
Diagram: D_IV^5 substrate geometric visualization

Elie, Saturday 2026-05-23 15:13 EDT (diagram pre-staging per Keeper queue)

Visualizes D_IV^5 = SO_0(5,2)/[SO(5)×SO(2)] — the unique Autogenic Proto-Geometry (APG).
Since D_IV^5 is a 10-dim bounded symmetric domain, we use 2D projection showing:
1. The isotropy structure K = SO(5) × SO(2)
2. The 5 BST primary integers emerging from substrate structure
3. The boundary structure (multiple Bergman boundary components)
4. Key load-bearing theorem citations

Output: PNG (300 DPI) + PDF
Target: Vol 0 Ch 1 (D_IV^5 APG Substrate Reading) authorship
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis('off')

# Title
ax.text(6.5, 8.5, r'$D_{IV}^5 = SO_0(5,2) / [SO(5) \times SO(2)]$',
        ha='center', fontsize=22, fontweight='bold')
ax.text(6.5, 8.0, 'The Autogenic Proto-Geometry (APG)',
        ha='center', fontsize=14, style='italic', color='#444')

# Main D_IV^5 boundary - bounded symmetric domain (drawn as a disc projection)
main_circle = patches.Circle((6.5, 4.5), 2.8, fill=True,
                              facecolor='#E6F3FF', ec='#1F4F8F', lw=3)
ax.add_patch(main_circle)

# Inner "core" with isotropy structure
inner_circle = patches.Circle((6.5, 4.5), 1.5, fill=True,
                               facecolor='#B0D4F1', ec='#1F4F8F', lw=2)
ax.add_patch(inner_circle)

# Center point - origin
ax.plot(6.5, 4.5, 'o', color='#1F4F8F', markersize=10)
ax.text(6.5, 4.5 - 0.3, 'origin', ha='center', fontsize=9, color='#1F4F8F')

# Isotropy K labels
ax.text(6.5, 4.5 + 0.85, r'$K = SO(5) \times SO(2)$', ha='center', fontsize=11, fontweight='bold')
ax.text(6.5, 4.5 + 0.55, 'isotropy subgroup', ha='center', fontsize=9, style='italic', color='#666')

# SO(5) callout (color sector)
ax.annotate('', xy=(5.5, 4.5), xytext=(3, 5.5),
            arrowprops=dict(arrowstyle='->', color='#8B4513'))
ax.text(2.8, 5.7, r'$SO(5)$', ha='center', fontsize=13, fontweight='bold', color='#8B4513')
ax.text(2.8, 5.35, 'spatial substrate-rotation', ha='center', fontsize=9, color='#8B4513')
ax.text(2.8, 5.15, '→ QCD color (Vol 2 Ch 6)', ha='center', fontsize=8, color='#8B4513')

# SO(2) callout (em sector)
ax.annotate('', xy=(7.5, 4.5), xytext=(10, 5.5),
            arrowprops=dict(arrowstyle='->', color='#B8860B'))
ax.text(10.2, 5.7, r'$SO(2)$', ha='center', fontsize=13, fontweight='bold', color='#B8860B')
ax.text(10.2, 5.35, 'em substrate-rotation', ha='center', fontsize=9, color='#B8860B')
ax.text(10.2, 5.15, r'$\to U(1)_{em}$ photon (Vol 7 Ch 5)', ha='center', fontsize=8, color='#B8860B')

# Five integer chips around the disc edge (not overlapping callouts)
chip_positions = [
    (6.5, 7.6, r'rank = 2', '#9966CC'),       # N top
    (4.0, 2.4, r'$N_c = 3$', '#FFD700'),     # SW
    (9.0, 2.4, r'$n_C = 5$', '#FFA500'),     # SE
    (5.0, 6.7, r'$C_2 = 6$', '#FF6347'),     # NW inner
    (8.0, 6.7, r'$g = 7$', '#FF4500'),       # NE inner
    (6.5, 1.4, r'$N_{\max}=137$', '#DC143C'),# S far
]
for x, y, lbl, c in chip_positions:
    box = patches.FancyBboxPatch((x-0.55, y-0.18), 1.1, 0.36,
                                   boxstyle='round,pad=0.05',
                                   facecolor=c, ec='black', lw=1.2, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, lbl, ha='center', va='center', fontsize=10, fontweight='bold',
            color='white' if c not in ['#FFD700', '#FFA500'] else 'black')

# Boundary components label
ax.text(6.5, 4.5 - 2.2, r'$\partial D_{IV}^5$ — Bergman boundary', ha='center',
        fontsize=10, style='italic', color='#1F4F8F')

# Wallach 1976 citation
ax.text(6.5, 4.5 - 2.55, r'Holomorphic isometry: $SO_0(5,2)$ (Wallach 1976, L1 ESTABLISHED)',
        ha='center', fontsize=9, color='#555')

# Footer with theorem anchors
ax.text(6.5, 0.6, 'BST primary integers + load-bearing theorems:', ha='center',
        fontsize=10, fontweight='bold', color='#222')
ax.text(6.5, 0.3, r'T2456: $N_{\max} = N_c^{N_c} \cdot n_C + \mathrm{rank}$ (RIGOROUSLY CLOSED C5)  •  T2462: 25 HSDs uniqueness  •  T2477: gauge fields as Bergman bundle connections',
        ha='center', fontsize=8, color='#666')

# Top-left framework anchor
ax.text(0.2, 8.7, '— Vol 0 Ch 1 supporting diagram —',
        ha='left', fontsize=9, color='#888', style='italic')

# Bottom-right reference
ax.text(12.8, 0.1, '$\\partial \\mathrm{D}_{IV}^5$: 5-fold + 2-fold + ...',
        ha='right', fontsize=8, color='#999', style='italic')

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_D_IV5_substrate.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_D_IV5_substrate.pdf',
            bbox_inches='tight', facecolor='white')
plt.close()
print("Generated:")
print("  diagram_D_IV5_substrate.png (300 DPI)")
print("  diagram_D_IV5_substrate.pdf")
