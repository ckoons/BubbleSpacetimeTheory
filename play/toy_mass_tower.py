#!/usr/bin/env python3
"""
THE MASS TOWER
==============
Visualize the entire mass hierarchy of the universe as a single
arithmetic progression in powers of α, all built from three integers.

From Planck mass down to the cosmological constant — every scale
is α^(multiples of 6 and 7) times the Planck mass.

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
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch

# ─── Constants ───
alpha = 1/137.035999
m_e_eV = 0.511e6           # electron mass in eV
m_p_eV = 938.272e6          # proton mass in eV
m_Pl_eV = 1.221e28          # Planck mass in eV
m_mu_eV = 105.658e6         # muon mass in eV
m_tau_eV = 1776.86e6        # tau mass in eV
m_W_eV = 80.377e9           # W boson in eV
m_Z_eV = 91.188e9           # Z boson in eV
m_H_eV = 125.25e9           # Higgs in eV
m_t_eV = 172.69e9           # top quark in eV
v_eV = 246.22e9             # Fermi/Higgs VEV in eV
Lambda_eV = 2.25e-3         # cosmological constant Λ^(1/4) in eV
m_nu_eV = 0.05              # neutrino mass scale in eV

# BST parameters
n_C = 5
N_c = 3
C2 = 6
genus = 7

# ─── The hierarchy as powers of α ───
# Define mass scales with their BST formulas and α-power
scales = [
    ('Planck mass', m_Pl_eV, 0, 'Reference scale', '#ffffff'),
    ('GUT scale', m_Pl_eV * alpha**2, 2, 'α² · m_Pl', '#ddddff'),
    ('Fermi VEV', v_eV, 12, 'm_p²/(7·m_e) = 36π¹⁰m_e/7', '#ff88ff'),
    ('Top quark', m_t_eV, 12, '(1−α)·v/√2', '#ff4444'),
    ('Higgs boson', m_H_eV, 12, 'v·√(2·√(2/5!))', '#ffaa00'),
    ('Z boson', m_Z_eV, 12, 'EW scale', '#ffcc44'),
    ('W boson', m_W_eV, 12, 'n_C·m_p/(8α)', '#ffcc44'),
    ('Tau lepton', m_tau_eV, 12, '(24/π²)⁶·(7/3)^{10/3}·m_e', '#44ff44'),
    ('Proton', m_p_eV, 12, 'C₂·π⁵·m_e = 6π⁵·m_e', '#00ffaa'),
    ('Muon', m_mu_eV, 12, '(24/π²)⁶·m_e', '#44aaff'),
    ('Pion', 139.57e6, 12, '√30·25.6 MeV', '#88aaff'),
    ('Electron', m_e_eV, 12, 'm_Pl·α¹²·(6π⁵)', '#4488ff'),
    ('Neutrino', m_nu_eV, 14*2, 'α²·m_e²/m_p', '#8844ff'),
    ('Λ^{1/4}', Lambda_eV, 56, 'α⁵⁶·(geometric)', '#ff44ff'),
]

# ─── Figure ───
fig = plt.figure(figsize=(16, 12), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('The Mass Tower — BST')

fig.text(0.5, 0.97, 'THE MASS TOWER', fontsize=26, fontweight='bold',
         color='#ffaa00', ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
fig.text(0.5, 0.94, 'Every mass scale is α^n × m_Planck  (n = multiples of 6 and 7)',
         fontsize=12, color='#aa8844', ha='center', fontfamily='monospace')

# Main axis — logarithmic scale
ax = fig.add_axes([0.12, 0.05, 0.82, 0.85])
ax.set_facecolor('#0a0a1a')

# Plot as horizontal bars on log scale
log_masses = [np.log10(s[1]) for s in scales]
y_positions = list(range(len(scales) - 1, -1, -1))

# Background gradient
for i, (name, mass, alpha_pow, formula, color) in enumerate(scales):
    y = len(scales) - 1 - i
    log_m = np.log10(mass)

    # Bar
    bar_width = (log_m - min(log_masses)) / (max(log_masses) - min(log_masses))
    ax.barh(y, bar_width * 30 + 1, left=-3, height=0.6,
            color=color, alpha=0.2, edgecolor=color, linewidth=1)

    # Dot at the mass value
    ax.plot(log_m, y, 'o', color=color, markersize=12, zorder=5)

    # Name
    ax.text(-5.5, y, name, fontsize=11, color=color, va='center',
            fontfamily='monospace', fontweight='bold')

    # Mass value
    if mass >= 1e9:
        mass_str = f'{mass/1e9:.1f} GeV'
    elif mass >= 1e6:
        mass_str = f'{mass/1e6:.1f} MeV'
    elif mass >= 1:
        mass_str = f'{mass:.2f} eV'
    else:
        mass_str = f'{mass:.2e} eV'
    ax.text(log_m + 0.3, y + 0.15, mass_str, fontsize=9, color='#cccccc',
            va='center', fontfamily='monospace')

    # Alpha power
    if alpha_pow > 0:
        ax.text(log_m + 0.3, y - 0.2, f'α^{alpha_pow}', fontsize=9,
                color='#ffaa00', va='center', fontfamily='monospace')

    # Formula
    ax.text(30, y, formula, fontsize=8, color='#666688', va='center',
            fontfamily='monospace', ha='right')

# Axis formatting
ax.set_xlim(-6, 31)
ax.set_ylim(-1, len(scales))

# X-axis as powers of 10
xticks = list(range(-3, 30, 3))
ax.set_xticks(xticks)
ax.set_xticklabels([f'10^{x}' if x != 0 else '1' for x in xticks],
                    fontsize=8, fontfamily='monospace')
ax.set_xlabel('Energy (eV)', fontsize=11, color='#aaaaaa', fontfamily='monospace')

ax.set_yticks([])  # Labels are drawn manually

# Grid
ax.grid(axis='x', color='#222244', linewidth=0.5, alpha=0.5)
for spine in ax.spines.values():
    spine.set_color('#333366')
ax.tick_params(colors='#666688')

# ─── Annotations: The hierarchy explanation ───
# Arrow showing the 12 = 2C₂ gap
ax.annotate('', xy=(np.log10(m_e_eV), 2.5), xytext=(np.log10(m_Pl_eV), 13.5),
            arrowprops=dict(arrowstyle='<->', color='#ffaa00', lw=2,
                            connectionstyle='arc3,rad=-0.15'))
ax.text(22, 8, '12 = 2C₂\n(two Casimir\nround trips)',
        fontsize=10, color='#ffaa00', ha='center',
        fontfamily='monospace', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a1a0a',
                  edgecolor='#aa6600', alpha=0.8))

# Arrow showing the 14 = 2×genus gap (electron to neutrino)
ax.annotate('', xy=(np.log10(m_nu_eV), 1.5), xytext=(np.log10(m_e_eV), 2.5),
            arrowprops=dict(arrowstyle='<->', color='#8844ff', lw=2,
                            connectionstyle='arc3,rad=-0.15'))
ax.text(2, 1, '14 = 2×genus', fontsize=9, color='#8844ff',
        fontfamily='monospace', fontweight='bold')

# Arrow showing 56 = 8×genus (Planck to Λ)
ax.annotate('', xy=(np.log10(Lambda_eV), 0.5), xytext=(np.log10(m_Pl_eV), 13.5),
            arrowprops=dict(arrowstyle='<->', color='#ff44ff', lw=1.5,
                            connectionstyle='arc3,rad=0.2'))
ax.text(-3, 7, '56 = 8×genus\n= 4×14\n(Planck → Λ)',
        fontsize=9, color='#ff44ff', ha='center',
        fontfamily='monospace', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a0a2a',
                  edgecolor='#aa44aa', alpha=0.8))

# ─── Key insight box ───
insight = (
    'The exponents are multiples of C₂=6 and genus=7:\n'
    '  12 = 2×6     (electron/proton → Planck)\n'
    '  14 = 2×7     (neutrino → electron)\n'
    '  56 = 8×7 = 4×14   (Λ → Planck)\n'
    '\n'
    'Two integers (6 and 7) set ALL the scales.'
)
fig.text(0.50, 0.01, insight, fontsize=10, color='#aaaaaa',
         ha='center', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#1a1a2a',
                   edgecolor='#444488', linewidth=1.5),
         linespacing=1.4)

plt.show()
