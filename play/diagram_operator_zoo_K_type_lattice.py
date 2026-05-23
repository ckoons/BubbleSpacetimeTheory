#!/usr/bin/env python3
"""
Diagram: Operator Zoo K-type Lattice visualization

Elie, Saturday 2026-05-23 15:22 EDT (fourth pre-staged diagram for Keeper authorship)

Visualizes the BST operator zoo: 14 substrate-native operators organized by
K-type representation (K = SO(5) × SO(2)) on Bergman bundle L_λ → D_IV⁵.

12/14 STRUCTURALLY VERIFIED / RATIFIED / FRAMEWORK-COMPLETE (per Friday EOD).
Only N_op + T_op remain CANDIDATE.

Target: Vol 1 Ch 6 (Operator Zoo) authorship
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.4, 'BST Operator Zoo on D_IV⁵ Substrate',
        ha='center', fontsize=18, fontweight='bold')
ax.text(7, 8.95, r'14 operators organized by K-type rep of $K = SO(5) \times SO(2)$',
        ha='center', fontsize=12, style='italic', color='#444')

# Operators data: (label, K-type, value, status, color, x, y)
# Status: V = RIGOROUSLY VERIFIED, R = RATIFIED, F = FRAMEWORK-COMPLETE, C = CANDIDATE
operators = [
    # Top row — energy + momentum + ground state (load-bearing)
    ('$H_{op}$',     'K-Casimir',   '$C_2 = 6$',         'V', '#3CB371',  2, 7.5),
    ('$P_{op}$',     'momentum',    'T2474',             'R', '#3CB371',  5, 7.5),
    ('$E_{op}$',     'energy',      'T2473',             'R', '#3CB371',  8, 7.5),
    ('$Q_{op}$',     'SO(2) weight', 'T2470',            'R', '#3CB371', 11, 7.5),
    # Middle row — chirality + parity + CP
    ('$\\gamma^5$',  'chirality',   'T2471',             'R', '#1E90FF',  2, 5.5),
    ('$P_{op}$ (parity)', 'parity', 'T2472',             'R', '#1E90FF',  5, 5.5),
    ('$C_{op}$',     'charge conj.', 'K85 STRUCT',       'F', '#1E90FF',  8, 5.5),
    ('$T_{rev,op}$', 'time-rev.',   'T2433/T2434',       'F', '#1E90FF', 11, 5.5),
    # Bottom row — angular + position + Bell
    ('$L_{op}$',     'angular L',   'T2421',             'R', '#FF8C00',  2, 3.5),
    ('$x_{op}$',     'position',    'T2419',             'R', '#FF8C00',  5, 3.5),
    ('$S_{op}$',     'spin',        'T2421',             'R', '#FF8C00',  8, 3.5),
    ('$B_{op}$',     'Bell-CHSH',   'K66 + T2399',       'V', '#FF8C00', 11, 3.5),
    # Bottom-most — CANDIDATES (not yet RATIFIED)
    ('$N_{op}$',     'number',      'CANDIDATE',         'C', '#DC143C',  3.5, 1.5),
    ('$T_{op}$',     'translation', 'CANDIDATE',         'C', '#DC143C',  9.5, 1.5),
]

# Status legend mapping
status_labels = {'V': 'RIGOROUSLY VERIFIED',
                 'R': 'RATIFIED',
                 'F': 'FRAMEWORK-COMPLETE',
                 'C': 'CANDIDATE'}

# Draw operator boxes
for label, ktype, value, status, color, x, y in operators:
    # Box
    box = patches.FancyBboxPatch((x-1.0, y-0.45), 2.0, 0.9,
                                  boxstyle='round,pad=0.05',
                                  facecolor=color, ec='black', lw=1.5, alpha=0.85)
    ax.add_patch(box)
    # Operator label (top of box)
    ax.text(x, y+0.20, label, ha='center', va='center', fontsize=12, fontweight='bold',
            color='white' if color != '#DC143C' else 'white')
    # K-type label
    ax.text(x, y-0.05, ktype, ha='center', va='center', fontsize=8.5, color='white', style='italic')
    # Value/Theorem
    ax.text(x, y-0.28, value, ha='center', va='center', fontsize=8, color='white')
    # Status badge (top-right corner)
    ax.text(x+0.95, y+0.40, status, ha='right', va='center', fontsize=7, fontweight='bold',
            color='white' if status in ['V', 'R'] else '#FFD700' if status == 'F' else 'white',
            bbox=dict(boxstyle='round,pad=0.1', facecolor='black' if status == 'V' else
                     '#444' if status == 'R' else '#666' if status == 'F' else '#8B0000',
                     alpha=0.7, edgecolor='none'))

# Row labels (left side)
ax.text(0.3, 7.5, 'Conservation\n(Casimir + Noether)', ha='center', va='center', fontsize=9,
        rotation=90, color='#3CB371', fontweight='bold')
ax.text(0.3, 5.5, 'Discrete\nSymmetries (CPT)', ha='center', va='center', fontsize=9,
        rotation=90, color='#1E90FF', fontweight='bold')
ax.text(0.3, 3.5, 'Spacetime\n+ Bell', ha='center', va='center', fontsize=9,
        rotation=90, color='#FF8C00', fontweight='bold')

# Bottom legend
ax.text(7, 0.7, 'Status: V = RIGOROUSLY VERIFIED  •  R = RATIFIED  •  F = FRAMEWORK-COMPLETE  •  C = CANDIDATE',
        ha='center', fontsize=10, color='#444')
ax.text(7, 0.3, '12/14 STRUCTURALLY VERIFIED or higher (Friday 2026-05-22 EOD)',
        ha='center', fontsize=9, color='#666', style='italic')

# Top-left framework anchor
ax.text(0.3, 9.7, '— Vol 1 Ch 6 supporting diagram —',
        ha='left', fontsize=9, color='#888', style='italic')

# Bottom-right reference
ax.text(13.7, 0.05, 'K-audit chain K85+ STRUCTURALLY VERIFIED tier (Cal #66)',
        ha='right', fontsize=8, color='#999', style='italic')

plt.tight_layout()
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_operator_zoo_K_type.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/diagram_operator_zoo_K_type.pdf',
            bbox_inches='tight', facecolor='white')
plt.close()
print("Generated:")
print("  diagram_operator_zoo_K_type.png (300 DPI)")
print("  diagram_operator_zoo_K_type.pdf")
