#!/usr/bin/env python3
"""
Diagram: Standard Model Particle Table BST-Annotated

Elie, Saturday 2026-05-23 16:33 EDT (sixth pre-staged diagram for Keeper authorship)

Visualizes Standard Model particles with BST substrate-origin annotations.
6 quarks + 6 leptons + 4 gauge bosons + Higgs + Wallach gravitons = 27 particles
(plus antiparticles for fermions).

Target: Vol 2 Ch 1 (SM Substrate Reading) authorship support
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

# Title
ax.text(7, 8.4, 'Standard Model Particles — BST Substrate Annotations',
        ha='center', fontsize=17, fontweight='bold')
ax.text(7, 8.0, '27 particles + Standard Model masses from D_IV⁵ substrate',
        ha='center', fontsize=11, style='italic', color='#444')

# Helper to draw particle box
def draw_particle(ax, x, y, label, mass, bst_anchor, fill='#E8F4F8', edge='#2C3E50', text='black'):
    box = patches.FancyBboxPatch((x-0.6, y-0.55), 1.2, 1.1,
                                  boxstyle='round,pad=0.05', linewidth=1.2,
                                  facecolor=fill, ec=edge)
    ax.add_patch(box)
    ax.text(x, y+0.30, label, ha='center', va='center', fontsize=11, fontweight='bold', color=text)
    ax.text(x, y, mass, ha='center', va='center', fontsize=7, color=text)
    ax.text(x, y-0.30, bst_anchor, ha='center', va='center', fontsize=6.5, color=text, style='italic')

# Quarks (6) — fill orange
quarks_gen1 = [
    ('u', '$2.16 MeV$', 'rank-2 winding', 1.5, 6.0),
    ('d', '$4.67 MeV$', 'rank-2 winding', 2.7, 6.0),
]
quarks_gen2 = [
    ('c', '$1.27 GeV$', 'speaking pair 1', 1.5, 4.8),
    ('s', '$93 MeV$',   'speaking pair 1', 2.7, 4.8),
]
quarks_gen3 = [
    ('t', '$173 GeV$',  'speaking pair 2 + Yukawa', 1.5, 3.6),
    ('b', '$4.18 GeV$', 'speaking pair 2', 2.7, 3.6),
]

for q in quarks_gen1 + quarks_gen2 + quarks_gen3:
    label, mass, bst, x, y = q
    draw_particle(ax, x, y, label, mass, bst, fill='#FFA07A')

# Leptons (6) — fill blue
leptons_gen1 = [
    ('e', '$0.511 MeV$', '$N_c = 3$ generations', 4.2, 6.0),
    (r'$\nu_e$', '< eV', 'seesaw = 17', 5.4, 6.0),
]
leptons_gen2 = [
    (r'$\mu$', '$105.66 MeV$', '$T190: (24/\\pi^2)^6$', 4.2, 4.8),
    (r'$\nu_\mu$', '< eV', 'seesaw = 17', 5.4, 4.8),
]
leptons_gen3 = [
    (r'$\tau$', '$1776.86 MeV$', '$T2003: 49 \\cdot 71$', 4.2, 3.6),
    (r'$\nu_\tau$', '< eV', 'seesaw = 17', 5.4, 3.6),
]
for l in leptons_gen1 + leptons_gen2 + leptons_gen3:
    label, mass, bst, x, y = l
    draw_particle(ax, x, y, label, mass, bst, fill='#87CEFA')

# Gauge bosons (4) — fill green
gauge = [
    (r'$\gamma$', 'massless', 'T2478: U(1)_em', 7.5, 6.0),
    ('g', 'massless', 'SO(5) → SU(3)', 8.7, 6.0),
    (r'$W^\pm$', '$80.4 GeV$', 'EW SSB', 7.5, 4.8),
    (r'$Z^0$', '$91.2 GeV$', 'EW SSB', 8.7, 4.8),
]
for b in gauge:
    label, mass, bst, x, y = b
    draw_particle(ax, x, y, label, mass, bst, fill='#90EE90')

# Higgs (1) — fill purple
draw_particle(ax, 8.1, 3.6, 'H', '$125.1 GeV$', 'T2478: SSB origin', fill='#DDA0DD')

# Section labels
ax.text(2.1, 7.0, 'Quarks (6)', ha='center', fontsize=12, fontweight='bold', color='#D2691E')
ax.text(4.8, 7.0, 'Leptons (6)', ha='center', fontsize=12, fontweight='bold', color='#4682B4')
ax.text(8.1, 7.0, 'Gauge + Higgs (5)', ha='center', fontsize=12, fontweight='bold', color='#2E8B57')

# Generations labels (left side)
ax.text(0.5, 6.0, 'Gen 1', ha='center', fontsize=10, fontweight='bold', color='#444')
ax.text(0.5, 4.8, 'Gen 2', ha='center', fontsize=10, fontweight='bold', color='#444')
ax.text(0.5, 3.6, 'Gen 3', ha='center', fontsize=10, fontweight='bold', color='#444')

# BST substrate origin column (right side)
substrate_origins = [
    (11.5, 6.5, 'Quark color', 'SO(5) sub-group $\\to$ SU(3) color', '#D2691E'),
    (11.5, 5.5, 'Lepton mass ratios', '$T190 + T2003 + (24/\\pi^2)^6$', '#4682B4'),
    (11.5, 4.5, 'Gauge groups', '$K = SO(5) \\times SO(2) \\to SM$', '#2E8B57'),
    (11.5, 3.5, 'EW SSB origin', 'T2478 + SO(2) preserves vev', '#9932CC'),
    (11.5, 2.5, 'No SUSY / monopoles / GUT', 'Five Absences (Casey-named)', '#8B0000'),
]
for x, y, title, content, color in substrate_origins:
    ax.text(x, y, title, ha='center', va='center', fontsize=9, fontweight='bold', color=color)
    ax.text(x, y-0.25, content, ha='center', va='center', fontsize=7, color='#555', style='italic')

# Proton + neutron callout
ax.text(7, 2.2, 'Composite: $m_p / m_e = 6\\pi^5 \\approx 1836.118$ (0.002% D-tier, T190)',
        ha='center', fontsize=10, color='#444', fontweight='bold')

# BST primary anchors footer
ax.text(7, 1.4, 'BST primary integers underlying Standard Model:',
        ha='center', fontsize=10, fontweight='bold')
ax.text(7, 1.0, r'rank = 2 (gen pairing)  •  $N_c$ = 3 (color + generations)  •  $n_C$ = 5 (orbitals)  •  $C_2$ = 6 (Yang-Mills)  •  $g$ = 7 (f orbitals)  •  $N_{\max}$ = 137 ($\alpha^{-1}$)',
        ha='center', fontsize=8, color='#666')

# Top-left framework anchor
ax.text(0.3, 8.7, '— Vol 2 Ch 1 supporting diagram —',
        ha='left', fontsize=9, color='#888', style='italic')

# Bottom-right reference
ax.text(13.7, 0.1, 'a_e CROWN JEWEL ppt precision (Vol 2 Ch 8)',
        ha='right', fontsize=8, color='#999', style='italic')

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_SM_particle_table_BST.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_SM_particle_table_BST.pdf',
            bbox_inches='tight', facecolor='white')
plt.close()
print("Generated:")
print("  diagram_SM_particle_table_BST.png (300 DPI)")
print("  diagram_SM_particle_table_BST.pdf")
