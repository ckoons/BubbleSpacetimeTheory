#!/usr/bin/env python3
"""
Diagram: 5-Family Bridge Object Architecture visualization

Elie, Saturday 2026-05-23 16:32 EDT (fifth pre-staged diagram for Keeper authorship)

Visualizes the 5-family Bridge Object architecture STRUCTURALLY VERIFIED COMPLETE
(Thursday May 21 EOD): 16 effective Bridge Object members across 5 families
+ 3 K57 RATIFIED central hubs.

Per Cal Referee Log #70 (Thursday 09:18 EDT): naive 17 → effective 16
independent members (Grace Toy 3222 cross-family reduction).

Target: Vol 0 Ch 7 (Bridge Objects + L1 Sources) authorship support
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

# Title
ax.text(7, 8.4, '5-Family Bridge Object Architecture',
        ha='center', fontsize=18, fontweight='bold')
ax.text(7, 7.95, 'STRUCTURALLY VERIFIED COMPLETE (Thursday 2026-05-21 EOD)',
        ha='center', fontsize=12, style='italic', color='#444')

# Central hubs (K57 RATIFIED) — middle row
hubs = [
    ('K3 surface',     'Hodge 1962/64',    3.5, 5.0, '#9B59B6'),
    ('Cremona 49a1',   'Heegner -g',       7.0, 5.0, '#3498DB'),
    ('$Q^5$ 5-quadric', 'All 5 Chern BST', 10.5, 5.0, '#27AE60'),
]
for name, anchor, x, y, color in hubs:
    circle = patches.Circle((x, y), 0.6, color=color, ec='black', lw=2.5, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, y+0.05, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.text(x, y-0.25, anchor, ha='center', va='center', fontsize=8, color='white', style='italic')
    # K57 RATIFIED badge
    ax.text(x, y-0.55, 'K57\nRATIFIED', ha='center', va='center', fontsize=7, fontweight='bold',
            color='white', bbox=dict(boxstyle='round,pad=0.1', facecolor='black', alpha=0.7, edgecolor='none'))

# 5 families with members (around the hubs)
families = [
    # (name, members, x_center, y_center, color, K3-link, 49a1-link, Q5-link)
    ('Family 1: Heegner-trio',  ['K47\n49a1\nat -g', 'K70\n121a1\nat -c_2', 'K62\n27a1\nat -N_c'],
     2.0, 2.2, '#E74C3C', False, True, False),
    ('Family 2: χ=24 non-Heegner', ['K76\nLeech', 'K81\n24-cell', 'K82\nΔ(τ)'],
     5.5, 2.2, '#F39C12', False, False, False),
    ('Family 3: N_max-anchored', ['K80\nE8 root\nN_max', 'K84\nFermat\nN_max'],
     8.5, 2.2, '#16A085', False, False, False),
    ('Family 4: K3-family',     ['K45 K3-fam\nRATIFIED', 'K77 PATH B\nRATIFIED', 'K3F5'],
     2.0, 6.8, '#8E44AD', True, False, False),
    ('Family 5: Q⁵-family',     ['Quadric', 'Spinor', 'Bergman', 'Chern', 'Calabi-Yau', 'Hyperplane'],
     11.5, 6.8, '#2ECC71', False, False, True),
]

# Draw families (member nodes + family boxes)
for fam_name, members, fx, fy, color, k3_link, c49a1_link, q5_link in families:
    # Family box
    n_members = len(members)
    width = max(2.4, n_members * 1.0)
    family_box = patches.FancyBboxPatch((fx - width/2, fy - 0.7), width, 1.4,
                                         boxstyle='round,pad=0.15', linewidth=1.5,
                                         facecolor=color, ec='black', alpha=0.15)
    ax.add_patch(family_box)
    # Family name
    ax.text(fx, fy + 0.85, fam_name, ha='center', fontsize=9, fontweight='bold', color=color)
    # Members
    for i, m in enumerate(members):
        m_x = fx - width/2 + (i + 0.5) * (width / n_members)
        m_box = patches.FancyBboxPatch((m_x - 0.4, fy - 0.4), 0.8, 0.8,
                                        boxstyle='round,pad=0.05', linewidth=1,
                                        facecolor=color, ec='black', alpha=0.7)
        ax.add_patch(m_box)
        ax.text(m_x, fy, m, ha='center', va='center', fontsize=7,
                color='white', fontweight='bold')

# Connections from families to central hubs
connections = [
    # Family 1 (Heegner-trio) → 49a1 hub (its anchor)
    (2.0, 2.2 + 0.7, 7.0, 5.0 - 0.6, '#E74C3C'),
    # Family 2 (χ=24) → 49a1 + Q5 hubs (Bridge Object mediated)
    (5.5, 2.2 + 0.7, 7.0, 5.0 - 0.6, '#F39C12'),
    # Family 3 (N_max) → 49a1 hub
    (8.5, 2.2 + 0.7, 7.0, 5.0 - 0.6, '#16A085'),
    # Family 4 (K3) → K3 hub (its anchor)
    (2.0, 6.8 - 0.7, 3.5, 5.0 + 0.6, '#8E44AD'),
    # Family 5 (Q5) → Q5 hub (its anchor)
    (11.5, 6.8 - 0.7, 10.5, 5.0 + 0.6, '#2ECC71'),
]
for x1, y1, x2, y2, color in connections:
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle='->', mutation_scale=12, lw=1.5,
                            color=color, alpha=0.6)
    ax.add_patch(arrow)

# Count summary box
summary_box = patches.FancyBboxPatch((6.0, 0.05), 2.0, 0.7,
                                      boxstyle='round,pad=0.1', linewidth=2,
                                      facecolor='#FFF8DC', ec='black')
ax.add_patch(summary_box)
ax.text(7.0, 0.5, 'Net architecture', ha='center', fontsize=9, fontweight='bold')
ax.text(7.0, 0.25, '3 hubs + 16 members + 3 sub = 19', ha='center', fontsize=8)

# Footer
ax.text(7, -0.3, 'Per Cal Referee Log #70 (Thursday 2026-05-21): naive 17 → effective 16 (Grace Toy 3222 cross-family reduction)',
        ha='center', fontsize=8, color='#666', style='italic')

# Top-left framework anchor
ax.text(0.3, 8.7, '— Vol 0 Ch 7 supporting diagram —',
        ha='left', fontsize=9, color='#888', style='italic')

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_5_family_bridge_object.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_5_family_bridge_object.pdf',
            bbox_inches='tight', facecolor='white')
plt.close()
print("Generated:")
print("  diagram_5_family_bridge_object.png (300 DPI)")
print("  diagram_5_family_bridge_object.pdf")
