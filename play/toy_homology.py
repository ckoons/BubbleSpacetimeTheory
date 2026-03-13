#!/usr/bin/env python3
"""
NEUTRON-UNIVERSE HOMOLOGY
=========================
The neutron and the universe are built from the same geometry.
7 parallels, 5 differences — all traced to D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)].

Click any row to explore the shared math and see what connects
(or separates) the smallest stable baryon and the cosmos.

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
from matplotlib.widgets import RadioButtons
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Arc
import matplotlib.patheffects as pe

# ──────────────────────────────────────────────────────────────
# DATA: 7 Parallels
# ──────────────────────────────────────────────────────────────
PARALLELS = [
    {
        'short': '1. Electrical Neutrality',
        'neutron': 'Z_3 closure on CP^2\n+2/3 - 1/3 - 1/3 = 0\nQuark charges cancel\ntopologically',
        'universe': 'S^2 Stokes theorem\nTotal winding number = 0\nGlobal charge must\nvanish on closed S^2',
        'shared': 'Topological zero:\nclosed manifold\n=> net charge = 0',
        'symbol': '=',
        'tag': 'TOPOLOGICAL',
    },
    {
        'short': '2. Topological Stability',
        'neutron': 'c_2 = 0 on D_IV^5\nZ_3 circuit cannot unwind\nHomotopy class is\ntopologically locked',
        'universe': 'Cartan classification\nis discrete: no continuous\npath from D_IV^5 to\nanother domain type',
        'shared': 'Discrete topology:\nno smooth deformation\ncan change the class',
        'symbol': '=',
        'tag': 'DISCRETE',
    },
    {
        'short': '3. Lapse Function',
        'neutron': 'High density rho\nSlow clocks, deep\ngravitational well\nQuark confinement',
        'universe': 'Low density rho\nFast clocks, shallow\ngravitational well\nCosmic expansion',
        'shared': 'N = N_0 sqrt(1 - rho/rho_137)\nSame formula,\nopposite regimes',
        'symbol': '=',
        'tag': 'METRIC',
    },
    {
        'short': '4. Vacuum Quantum Production',
        'neutron': 'Beta decay emits\nanti-neutrino (nu-bar)\n= one vacuum quantum\ntau ~ 878 seconds',
        'universe': 'Expansion creates\nnew vacuum (Lambda energy)\n= continuous vacuum\nquantum production',
        'shared': 'Neutrino IS the\nvacuum quantum:\nm_nu ~ alpha^14 m_Pl',
        'symbol': '=',
        'tag': 'VACUUM',
    },
    {
        'short': '5. The 1920 Cancellation',
        'neutron': 'Baryon orbit:\nn_C! x 2^(n_C-1)\n= 120 x 16 = 1920\nconfigurations',
        'universe': 'Hua volume:\nVol(D_IV^5) = pi^5/1920\nBergman metric\ndeterminant',
        'shared': 'SAME |Gamma| = 1920\nWeyl group of B_5\nS_5 x (Z_2)^4\nCANCELS in m_p/m_e',
        'symbol': '=',
        'tag': 'ARITHMETIC',
    },
    {
        'short': '6. Same Partition Function',
        'neutron': 'Spectral gap =\nneutron mass\n= 6 pi^5 m_e\n= 939.565 MeV',
        'universe': 'Ground energy =\nLambda (cosmological\nconstant) from\nsame Z_Haldane',
        'shared': 'Z_Haldane on D_IV^5:\nbaryon = excited state\nLambda = ground state',
        'symbol': '=',
        'tag': 'SPECTRAL',
    },
    {
        'short': '7. Compositeness',
        'neutron': '3 quarks in Z_3\ncircuit on CP^2\nSym^3(pi_6)\nminimal baryon',
        'universe': 'ALL circuits on\nS^2 x S^1 boundary\nEntire Haldane\nchannel of D_IV^5',
        'shared': 'Both are composite:\nbuilt from geometric\ncircuits on the\nsame domain',
        'symbol': '=',
        'tag': 'GEOMETRIC',
    },
]

# ──────────────────────────────────────────────────────────────
# DATA: 5 Differences
# ──────────────────────────────────────────────────────────────
DIFFERENCES = [
    {
        'short': 'A. Boundary vs Interior',
        'neutron': 'Lives ON the Shilov\nboundary S^4 x S^1\nExcitation of the\nboundary surface',
        'universe': 'IS the full closed\nD-bar_IV^5\nThe entire bounded\nsymmetric domain',
        'shared': 'Shilov boundary\nvs bulk interior:\nsame domain,\ndifferent loci',
        'symbol': 'vs',
        'tag': 'LOCUS',
    },
    {
        'short': 'B. One Circuit vs Whole Channel',
        'neutron': 'ONE Z_3 circuit:\nminimal winding\nnumber on CP^2\nlocalized excitation',
        'universe': 'ENTIRE Haldane\nchannel: all modes,\nall windings,\nglobal structure',
        'shared': 'Part vs whole:\none fiber\nvs full bundle',
        'symbol': 'vs',
        'tag': 'SCOPE',
    },
    {
        'short': 'C. Metastability',
        'neutron': 'DECAYS via beta:\nn -> p + e + nu-bar\ntau = 878.4 seconds\nFinite lifetime',
        'universe': 'NO decay channel:\nno lower-energy\ntopology available\nEternal (in BST)',
        'shared': 'Neutron: excited\nstate can relax\nUniverse: IS the\nground topology',
        'symbol': '!=',
        'tag': 'STABILITY',
    },
    {
        'short': 'D. Scale: 41 Orders',
        'neutron': 'r_p ~ 0.84 fm\nProton/neutron\nradius scale\n10^-15 meters',
        'universe': 'R_H ~ 4.4 x 10^26 m\nHubble radius\nCosmological\nhorizon scale',
        'shared': 'R_H / r_p ~ 10^41\n~ alpha^-19\nSame alpha,\n41 decades apart',
        'symbol': '!=',
        'tag': 'SCALE',
    },
    {
        'short': 'E. Density Regime',
        'neutron': 'rho / rho_137 ~ 10^-3\nHigh density:\nclose to the\nBST density ceiling',
        'universe': 'rho / rho_137 ~ 10^-123\nUltra-low density:\nvast emptiness,\nLambda-dominated',
        'shared': 'Same rho_137 ceiling\nNeutron near top\nUniverse near bottom\n120 decades apart',
        'symbol': '!=',
        'tag': 'DENSITY',
    },
]

# ──────────────────────────────────────────────────────────────
# Color palette
# ──────────────────────────────────────────────────────────────
BG = '#0a0a1a'
NEUTRON_COLOR = '#ff6644'
NEUTRON_DIM = '#aa4422'
NEUTRON_BG = '#1a0a08'
UNIVERSE_COLOR = '#4488ff'
UNIVERSE_DIM = '#2255aa'
UNIVERSE_BG = '#080a1a'
SHARED_COLOR = '#00ddaa'
SHARED_DIM = '#008866'
SHARED_BG = '#081a14'
PAR_ACCENT = '#ffcc00'
DIFF_ACCENT = '#ff4488'
TEXT_COLOR = '#ccccdd'
DIM_TEXT = '#667788'

# ──────────────────────────────────────────────────────────────
# Build the figure
# ──────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(18, 12), facecolor=BG)
fig.canvas.manager.set_window_title('Neutron-Universe Homology — BST')

# Title
fig.text(0.50, 0.975, 'NEUTRON  -  UNIVERSE  HOMOLOGY',
         fontsize=26, fontweight='bold', color='#ffffff', ha='center',
         va='top', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#003366')])
fig.text(0.50, 0.945, 'same geometry  |  so(5,2)  |  D_IV^5  |  N_c=3, n_C=5, N_max=137',
         fontsize=11, color=SHARED_COLOR, ha='center', va='top',
         fontfamily='monospace')

# Column headers
fig.text(0.195, 0.915, 'NEUTRON', fontsize=18, fontweight='bold',
         color=NEUTRON_COLOR, ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#441100')])
fig.text(0.50, 0.915, 'SHARED MATH', fontsize=18, fontweight='bold',
         color=SHARED_COLOR, ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#003322')])
fig.text(0.805, 0.915, 'UNIVERSE', fontsize=18, fontweight='bold',
         color=UNIVERSE_COLOR, ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#001144')])

# ──────────────────────────────────────────────────────────────
# Radio button selector (left edge)
# ──────────────────────────────────────────────────────────────
labels_p = [p['short'] for p in PARALLELS]
labels_d = [d['short'] for d in DIFFERENCES]
all_labels = labels_p + ['---'] + labels_d

ax_radio = fig.add_axes([0.005, 0.14, 0.155, 0.76], facecolor=BG)
ax_radio.set_xlim(0, 1)
ax_radio.set_ylim(0, 1)
ax_radio.axis('off')

ax_radio.text(0.5, 0.98, '7 PARALLELS', fontsize=10, fontweight='bold',
              color=PAR_ACCENT, ha='center', fontfamily='monospace')

# Build clickable text labels
label_y_positions = []
label_texts = []
n_total = len(PARALLELS) + len(DIFFERENCES) + 1  # +1 for separator
spacing = 0.92 / n_total

for i, lbl in enumerate(all_labels):
    y = 0.94 - i * spacing
    label_y_positions.append(y)
    if lbl == '---':
        ax_radio.plot([0.05, 0.95], [y, y], color='#333355', linewidth=1)
        ax_radio.text(0.5, y - 0.01, '5 DIFFERENCES', fontsize=10,
                      fontweight='bold', color=DIFF_ACCENT, ha='center',
                      fontfamily='monospace')
        label_texts.append(None)
    else:
        is_parallel = i < len(PARALLELS)
        color = PAR_ACCENT if is_parallel else DIFF_ACCENT
        t = ax_radio.text(0.05, y, lbl, fontsize=8, color=DIM_TEXT,
                          fontfamily='monospace', va='center',
                          picker=True)
        t.set_gid(str(i))
        label_texts.append(t)

# Highlight marker
highlight_dot = ax_radio.plot(0.01, label_y_positions[0], 'o',
                              color=PAR_ACCENT, markersize=8)[0]

# ──────────────────────────────────────────────────────────────
# Three main display panels (top area)
# ──────────────────────────────────────────────────────────────
ax_neutron = fig.add_axes([0.17, 0.57, 0.24, 0.32], facecolor=NEUTRON_BG)
ax_neutron.set_xlim(0, 1)
ax_neutron.set_ylim(0, 1)
ax_neutron.axis('off')
for spine in ax_neutron.spines.values():
    spine.set_visible(True)
    spine.set_color(NEUTRON_DIM)
    spine.set_linewidth(2)

ax_shared = fig.add_axes([0.42, 0.57, 0.16, 0.32], facecolor=SHARED_BG)
ax_shared.set_xlim(0, 1)
ax_shared.set_ylim(0, 1)
ax_shared.axis('off')
for spine in ax_shared.spines.values():
    spine.set_visible(True)
    spine.set_color(SHARED_DIM)
    spine.set_linewidth(2)

ax_universe = fig.add_axes([0.59, 0.57, 0.24, 0.32], facecolor=UNIVERSE_BG)
ax_universe.set_xlim(0, 1)
ax_universe.set_ylim(0, 1)
ax_universe.axis('off')
for spine in ax_universe.spines.values():
    spine.set_visible(True)
    spine.set_color(UNIVERSE_DIM)
    spine.set_linewidth(2)

# ──────────────────────────────────────────────────────────────
# Symbol panel between columns
# ──────────────────────────────────────────────────────────────
ax_sym_left = fig.add_axes([0.41, 0.66, 0.015, 0.14], facecolor=BG)
ax_sym_left.axis('off')
ax_sym_left.set_xlim(0, 1)
ax_sym_left.set_ylim(0, 1)

ax_sym_right = fig.add_axes([0.575, 0.66, 0.015, 0.14], facecolor=BG)
ax_sym_right.axis('off')
ax_sym_right.set_xlim(0, 1)
ax_sym_right.set_ylim(0, 1)

sym_left_text = ax_sym_left.text(0.5, 0.5, '=', fontsize=28, fontweight='bold',
                                  color=PAR_ACCENT, ha='center', va='center',
                                  fontfamily='monospace')
sym_right_text = ax_sym_right.text(0.5, 0.5, '=', fontsize=28, fontweight='bold',
                                    color=PAR_ACCENT, ha='center', va='center',
                                    fontfamily='monospace')

# ──────────────────────────────────────────────────────────────
# Bottom detail panel with diagram area
# ──────────────────────────────────────────────────────────────
ax_detail = fig.add_axes([0.17, 0.04, 0.48, 0.49], facecolor='#060612')
ax_detail.axis('off')
ax_detail.set_xlim(0, 10)
ax_detail.set_ylim(0, 10)
for spine in ax_detail.spines.values():
    spine.set_visible(True)
    spine.set_color('#334455')
    spine.set_linewidth(1)

# Diagram subplot (right side of bottom)
ax_diagram = fig.add_axes([0.67, 0.04, 0.30, 0.49], facecolor='#060612')
ax_diagram.set_xlim(-1.5, 1.5)
ax_diagram.set_ylim(-1.5, 1.5)
ax_diagram.set_aspect('equal')
ax_diagram.axis('off')
for spine in ax_diagram.spines.values():
    spine.set_visible(True)
    spine.set_color('#334455')
    spine.set_linewidth(1)

# ──────────────────────────────────────────────────────────────
# Diagram drawing functions
# ──────────────────────────────────────────────────────────────

def draw_z3_triangle(ax):
    """Parallel 1: Z3 charge closure and S2 winding."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    ax.axis('off')

    # Z3 triangle (neutron side)
    angles = [np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3]
    pts = [(0.8*np.cos(a) - 0.5, 0.8*np.sin(a) + 0.3) for a in angles]
    charges = ['+2/3', '-1/3', '-1/3']
    colors_q = ['#ff6644', '#44aaff', '#44aaff']

    for i in range(3):
        j = (i + 1) % 3
        ax.plot([pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]],
                color=NEUTRON_DIM, linewidth=2, alpha=0.7)

    for i, (pt, q, c) in enumerate(zip(pts, charges, colors_q)):
        circle = Circle(pt, 0.18, facecolor=c, edgecolor='white',
                        linewidth=1.5, alpha=0.8, zorder=5)
        ax.add_patch(circle)
        ax.text(pt[0], pt[1], q, fontsize=9, ha='center', va='center',
                color='white', fontweight='bold', fontfamily='monospace', zorder=6)

    ax.text(-0.5, -0.7, 'sum = 0', fontsize=11, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')

    # S2 winding (universe side)
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(0.6*np.cos(theta) + 0.7, 0.6*np.sin(theta) + 0.3,
            color=UNIVERSE_DIM, linewidth=2)
    # arrows showing net winding = 0
    for a in [0, np.pi/2, np.pi, 3*np.pi/2]:
        dx = -0.08 * np.sin(a)
        dy = 0.08 * np.cos(a)
        ax.annotate('', xy=(0.7 + 0.6*np.cos(a) + dx, 0.3 + 0.6*np.sin(a) + dy),
                    xytext=(0.7 + 0.6*np.cos(a), 0.3 + 0.6*np.sin(a)),
                    arrowprops=dict(arrowstyle='->', color=UNIVERSE_COLOR, lw=1.5))
    ax.text(0.7, -0.7, 'winding = 0', fontsize=11, color=UNIVERSE_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')

    ax.text(0.1, 1.4, 'ELECTRICAL NEUTRALITY', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')


def draw_stability(ax):
    """Parallel 2: Topological stability."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Discrete grid of domain types
    domains = ['A_n', 'B_n', 'C_n', 'D_n', 'D_IV^5']
    xs = [-1.0, -0.3, 0.4, -0.6, 0.1]
    ys = [0.6, 0.8, 0.6, 0.0, -0.2]
    for x, y, d in zip(xs, ys, domains):
        c = SHARED_COLOR if d == 'D_IV^5' else '#445566'
        ec = '#00ffaa' if d == 'D_IV^5' else '#556677'
        box = FancyBboxPatch((x - 0.25, y - 0.15), 0.5, 0.3,
                             boxstyle='round,pad=0.05', facecolor=c if d == 'D_IV^5' else '#112233',
                             edgecolor=ec, linewidth=2 if d == 'D_IV^5' else 1,
                             alpha=0.9 if d == 'D_IV^5' else 0.5, zorder=4)
        ax.add_patch(box)
        ax.text(x, y, d, fontsize=9, ha='center', va='center',
                color='white' if d == 'D_IV^5' else '#889999',
                fontweight='bold' if d == 'D_IV^5' else 'normal',
                fontfamily='monospace', zorder=5)

    # "No path" X marks between domains
    for i in range(len(xs) - 1):
        mx = (xs[i] + xs[i+1]) / 2
        my = (ys[i] + ys[i+1]) / 2
        ax.text(mx, my, 'X', fontsize=14, color='#ff3333',
                ha='center', va='center', fontweight='bold',
                fontfamily='monospace', alpha=0.6)

    ax.text(0.0, 1.3, 'DISCRETE CARTAN CLASSES', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -1.1, 'no continuous deformation\nbetween types', fontsize=9,
            color=DIM_TEXT, ha='center', fontfamily='monospace')


def draw_lapse(ax):
    """Parallel 3: Same lapse function, different regimes."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Plot lapse function N = sqrt(1 - rho/rho_137)
    rho = np.linspace(0, 0.99, 200)
    N = np.sqrt(1 - rho)

    # Scale to fit
    x = rho * 2.4 - 1.2
    y = N * 2.0 - 1.2

    ax.plot(x, y, color=SHARED_COLOR, linewidth=2.5)

    # Mark neutron regime (high rho)
    rho_n = 0.85
    x_n = rho_n * 2.4 - 1.2
    y_n = np.sqrt(1 - rho_n) * 2.0 - 1.2
    ax.plot(x_n, y_n, 'o', color=NEUTRON_COLOR, markersize=12, zorder=5)
    ax.text(x_n + 0.15, y_n + 0.15, 'n', fontsize=12, color=NEUTRON_COLOR,
            fontweight='bold', fontfamily='monospace')

    # Mark universe regime (low rho)
    rho_u = 0.05
    x_u = rho_u * 2.4 - 1.2
    y_u = np.sqrt(1 - rho_u) * 2.0 - 1.2
    ax.plot(x_u, y_u, 'o', color=UNIVERSE_COLOR, markersize=12, zorder=5)
    ax.text(x_u - 0.3, y_u + 0.1, 'U', fontsize=12, color=UNIVERSE_COLOR,
            fontweight='bold', fontfamily='monospace')

    ax.text(0.0, 1.3, 'LAPSE FUNCTION', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -1.35, 'N = N_0 sqrt(1 - rho/rho_137)', fontsize=9,
            color=SHARED_COLOR, ha='center', fontfamily='monospace')

    # Axes labels
    ax.text(1.3, -1.35, 'rho', fontsize=9, color=DIM_TEXT,
            ha='center', fontfamily='monospace')
    ax.text(-1.4, 0.8, 'N', fontsize=9, color=DIM_TEXT,
            ha='center', fontfamily='monospace')
    ax.plot([-1.2, 1.2], [-1.2, -1.2], color='#334455', linewidth=1)
    ax.plot([-1.2, -1.2], [-1.2, 0.8], color='#334455', linewidth=1)


def draw_vacuum_quantum(ax):
    """Parallel 4: Vacuum quantum production."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Neutron decay: n -> p + e + nu_bar
    ax.text(-0.7, 0.9, 'n', fontsize=20, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')
    ax.annotate('', xy=(0.0, 0.5), xytext=(-0.5, 0.8),
                arrowprops=dict(arrowstyle='->', color=NEUTRON_DIM, lw=2))
    ax.text(0.3, 0.8, 'p', fontsize=14, color='#ffaa44',
            ha='center', fontfamily='monospace')
    ax.text(0.3, 0.5, 'e', fontsize=14, color='#88ff88',
            ha='center', fontfamily='monospace')
    ax.text(0.6, 0.35, 'nu-bar', fontsize=12, color='#aa88ff',
            ha='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#1a0a2a',
                      edgecolor='#8866cc', linewidth=1.5))

    # Universe expansion creating vacuum
    theta = np.linspace(0, 2*np.pi, 100)
    for r, alpha in [(0.3, 0.8), (0.5, 0.5), (0.7, 0.3)]:
        ax.plot(r*np.cos(theta), r*np.sin(theta) - 0.7,
                color=UNIVERSE_COLOR, linewidth=1.5, alpha=alpha)
    ax.text(0.0, -0.7, 'Lambda', fontsize=11, color='#aa88ff',
            ha='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#1a0a2a',
                      edgecolor='#8866cc', linewidth=1.5))

    ax.text(0.0, 1.3, 'VACUUM QUANTA', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -1.35, 'neutrino = vacuum quantum', fontsize=9,
            color='#aa88ff', ha='center', fontfamily='monospace')


def draw_1920(ax):
    """Parallel 5: The 1920 cancellation."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.6, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Two boxes converging to center
    box_n = FancyBboxPatch((-1.3, 0.4), 1.1, 0.6,
                           boxstyle='round,pad=0.08', facecolor=NEUTRON_BG,
                           edgecolor=NEUTRON_COLOR, linewidth=2)
    ax.add_patch(box_n)
    ax.text(-0.75, 0.85, 'Baryon Orbit', fontsize=9, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(-0.75, 0.6, '5! x 2^4 = 1920', fontsize=10, color='white',
            ha='center', fontfamily='monospace')

    box_u = FancyBboxPatch((0.2, 0.4), 1.1, 0.6,
                           boxstyle='round,pad=0.08', facecolor=UNIVERSE_BG,
                           edgecolor=UNIVERSE_COLOR, linewidth=2)
    ax.add_patch(box_u)
    ax.text(0.75, 0.85, 'Hua Volume', fontsize=9, color=UNIVERSE_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.75, 0.6, 'pi^5 / 1920', fontsize=10, color='white',
            ha='center', fontfamily='monospace')

    # Cancellation arrow
    ax.annotate('', xy=(0.0, -0.1), xytext=(-0.75, 0.35),
                arrowprops=dict(arrowstyle='->', color=PAR_ACCENT, lw=2))
    ax.annotate('', xy=(0.0, -0.1), xytext=(0.75, 0.35),
                arrowprops=dict(arrowstyle='->', color=PAR_ACCENT, lw=2))

    # Result
    box_r = FancyBboxPatch((-0.7, -0.65), 1.4, 0.5,
                           boxstyle='round,pad=0.08', facecolor='#0a2a1a',
                           edgecolor='#00ff88', linewidth=2)
    ax.add_patch(box_r)
    ax.text(0.0, -0.25, '1920 cancels!', fontsize=10, color=PAR_ACCENT,
            ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -0.5, 'm_p/m_e = 6 pi^5', fontsize=12, color='#00ff88',
            ha='center', fontfamily='monospace', fontweight='bold')

    ax.text(0.0, 1.35, 'THE 1920 CANCELLATION', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -1.1, '= 1836.15  (0.002%)', fontsize=10,
            color='#88ffaa', ha='center', fontfamily='monospace')


def draw_partition(ax):
    """Parallel 6: Same partition function."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Energy level diagram
    ax.plot([-0.6, 0.6], [-1.0, -1.0], color='#334455', linewidth=1)
    ax.plot([-0.6, 0.6], [0.5, 0.5], color='#334455', linewidth=1)

    # Ground state = Lambda
    ax.plot([-0.4, 0.4], [-0.8, -0.8], color=UNIVERSE_COLOR, linewidth=3)
    ax.text(0.6, -0.8, 'Lambda', fontsize=10, color=UNIVERSE_COLOR,
            ha='left', va='center', fontfamily='monospace')

    # Gap
    ax.annotate('', xy=(0.0, 0.2), xytext=(0.0, -0.7),
                arrowprops=dict(arrowstyle='<->', color=PAR_ACCENT, lw=2))
    ax.text(0.15, -0.25, 'gap', fontsize=10, color=PAR_ACCENT,
            ha='left', fontfamily='monospace')

    # Excited state = neutron mass
    ax.plot([-0.4, 0.4], [0.3, 0.3], color=NEUTRON_COLOR, linewidth=3)
    ax.text(0.6, 0.3, 'm_n', fontsize=10, color=NEUTRON_COLOR,
            ha='left', va='center', fontfamily='monospace')

    # Label
    ax.text(-0.8, -0.8, 'E_0', fontsize=10, color=DIM_TEXT,
            ha='right', va='center', fontfamily='monospace')
    ax.text(-0.8, 0.3, 'E_1', fontsize=10, color=DIM_TEXT,
            ha='right', va='center', fontfamily='monospace')

    ax.text(0.0, 1.3, 'Z_HALDANE SPECTRUM', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, 0.8, 'same partition function', fontsize=9,
            color=SHARED_COLOR, ha='center', fontfamily='monospace')


def draw_composite(ax):
    """Parallel 7: Compositeness."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Neutron: 3 quarks
    angles_q = [np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3]
    for a, lbl, c in zip(angles_q, ['u', 'd', 'd'],
                         ['#ff4444', '#4488ff', '#4488ff']):
        x, y = 0.4*np.cos(a) - 0.8, 0.4*np.sin(a) + 0.3
        circle = Circle((x, y), 0.15, facecolor=c, edgecolor='white',
                         linewidth=1.5, alpha=0.8, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y, lbl, fontsize=10, ha='center', va='center',
                color='white', fontweight='bold', fontfamily='monospace', zorder=6)
    ax.text(-0.8, -0.4, 'one Z_3\ncircuit', fontsize=9, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace')

    # Universe: many circuits
    for i in range(8):
        a = i * np.pi / 4
        r = 0.3 + 0.15 * np.sin(3 * a)
        x, y = r * np.cos(a) + 0.7, r * np.sin(a) + 0.3
        circle = Circle((x, y), 0.06, facecolor=UNIVERSE_COLOR,
                         edgecolor='white', linewidth=0.5, alpha=0.4, zorder=5)
        ax.add_patch(circle)
    theta_c = np.linspace(0, 2*np.pi, 80)
    ax.plot(0.5*np.cos(theta_c) + 0.7, 0.5*np.sin(theta_c) + 0.3,
            color=UNIVERSE_DIM, linewidth=1.5, linestyle='--', alpha=0.5)
    ax.text(0.7, -0.4, 'all circuits\non S^2 x S^1', fontsize=9,
            color=UNIVERSE_COLOR, ha='center', fontfamily='monospace')

    ax.text(0.0, 1.3, 'COMPOSITENESS', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')


def draw_boundary_vs_interior(ax):
    """Difference A: Boundary vs interior."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Filled domain (universe)
    theta = np.linspace(0, 2*np.pi, 100)
    r_domain = 0.9
    ax.fill(r_domain*np.cos(theta), r_domain*np.sin(theta),
            color=UNIVERSE_BG, alpha=0.6)
    ax.plot(r_domain*np.cos(theta), r_domain*np.sin(theta),
            color=UNIVERSE_COLOR, linewidth=2)

    # Boundary dots (neutron)
    for a in np.linspace(0, 2*np.pi, 12, endpoint=False):
        x, y = r_domain*np.cos(a), r_domain*np.sin(a)
        ax.plot(x, y, 'o', color=NEUTRON_COLOR, markersize=7, zorder=5)

    ax.text(0.0, 0.0, 'D-bar_IV^5', fontsize=12, color=UNIVERSE_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold', alpha=0.8)
    ax.text(0.0, -0.25, '(Universe)', fontsize=9, color=UNIVERSE_DIM,
            ha='center', fontfamily='monospace')

    ax.annotate('S^4 x S^1\n(Neutron)', xy=(0.75, 0.55),
                fontsize=9, color=NEUTRON_COLOR,
                ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=NEUTRON_BG,
                          edgecolor=NEUTRON_COLOR, linewidth=1))

    ax.text(0.0, 1.3, 'BOUNDARY  vs  INTERIOR', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')


def draw_circuit_vs_channel(ax):
    """Difference B: One circuit vs whole channel."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Single circuit (neutron)
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(0.4*np.cos(theta) - 0.7, 0.4*np.sin(theta),
            color=NEUTRON_COLOR, linewidth=3)
    ax.text(-0.7, 0.0, 'Z_3', fontsize=12, color='white',
            ha='center', va='center', fontfamily='monospace', fontweight='bold')
    ax.text(-0.7, -0.7, 'one circuit', fontsize=9, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace')

    # Multiple circuits (universe)
    for r in [0.2, 0.35, 0.5, 0.65]:
        alpha = 0.3 + 0.5 * (r / 0.65)
        ax.plot(r*np.cos(theta) + 0.7, r*np.sin(theta),
                color=UNIVERSE_COLOR, linewidth=1.5, alpha=alpha)
    ax.text(0.7, 0.0, 'all', fontsize=10, color='white',
            ha='center', va='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.7, -0.7, 'full channel', fontsize=9, color=UNIVERSE_COLOR,
            ha='center', fontfamily='monospace')

    ax.text(0.0, 0.0, 'vs', fontsize=16, color=DIFF_ACCENT,
            ha='center', va='center', fontfamily='monospace', fontweight='bold')

    ax.text(0.0, 1.3, 'ONE  vs  ALL', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')


def draw_metastability(ax):
    """Difference C: Metastability."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Neutron: decaying exponential
    t = np.linspace(0, 4, 100)
    y_decay = np.exp(-t / 1.2)  # tau ~ 878s
    ax.plot(t * 0.6 - 1.2, y_decay * 1.8 - 0.9, color=NEUTRON_COLOR, linewidth=2.5)
    ax.text(-0.9, 1.0, 'N(t)', fontsize=9, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace')
    ax.text(0.4, -0.6, 'tau = 878 s', fontsize=9, color=NEUTRON_DIM,
            ha='center', fontfamily='monospace')

    # Universe: flat line (no decay)
    ax.plot([-1.2, 1.2], [0.0, 0.0], color=UNIVERSE_COLOR, linewidth=2.5,
            linestyle='--')
    ax.text(0.7, 0.15, 'no decay', fontsize=9, color=UNIVERSE_COLOR,
            ha='center', fontfamily='monospace')

    ax.text(0.0, 1.3, 'METASTABILITY', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -1.3, 'neutron decays; universe does not', fontsize=9,
            color=DIM_TEXT, ha='center', fontfamily='monospace')


def draw_scale(ax):
    """Difference D: 41 orders of magnitude."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Log scale bar
    ax.plot([-1.2, 1.2], [0, 0], color='#334455', linewidth=2)

    # Tick marks at key scales
    scales = [
        (-1.1, 'fm', NEUTRON_COLOR, 'r_p\n10^-15 m'),
        (-0.3, 'nm', DIM_TEXT, ''),
        (0.0, 'um', DIM_TEXT, ''),
        (0.3, 'm', DIM_TEXT, ''),
        (0.7, 'AU', DIM_TEXT, ''),
        (1.1, 'R_H', UNIVERSE_COLOR, 'R_H\n10^26 m'),
    ]
    for x, lbl, c, note in scales:
        ax.plot([x, x], [-0.1, 0.1], color=c, linewidth=2)
        ax.text(x, -0.25, lbl, fontsize=8, color=c,
                ha='center', fontfamily='monospace')
        if note:
            y_note = 0.5 if c == NEUTRON_COLOR else 0.5
            ax.text(x, y_note, note, fontsize=9, color=c,
                    ha='center', fontfamily='monospace', fontweight='bold')

    # Double arrow spanning the gap
    ax.annotate('', xy=(1.1, 0.9), xytext=(-1.1, 0.9),
                arrowprops=dict(arrowstyle='<->', color=DIFF_ACCENT, lw=2))
    ax.text(0.0, 1.1, '41 orders of magnitude', fontsize=11, color=DIFF_ACCENT,
            ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -0.7, 'R_H / r_p ~ 10^41 ~ alpha^-19', fontsize=10,
            color=PAR_ACCENT, ha='center', fontfamily='monospace')

    ax.text(0.0, 1.4, 'SCALE SEPARATION', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')


def draw_density(ax):
    """Difference E: Density regime."""
    ax.clear()
    ax.set_facecolor('#060612')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Density bar (log scale)
    ax.plot([-1.2, 1.2], [0, 0], color='#334455', linewidth=3)

    # rho_137 ceiling
    ax.plot([1.2, 1.2], [-0.2, 0.2], color=PAR_ACCENT, linewidth=3)
    ax.text(1.2, 0.4, 'rho_137', fontsize=10, color=PAR_ACCENT,
            ha='center', fontfamily='monospace', fontweight='bold')

    # Neutron near top
    ax.plot(0.95, 0.0, 'o', color=NEUTRON_COLOR, markersize=14, zorder=5)
    ax.text(0.95, -0.4, 'n\n10^-3', fontsize=9, color=NEUTRON_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')

    # Universe near bottom
    ax.plot(-1.0, 0.0, 'o', color=UNIVERSE_COLOR, markersize=14, zorder=5)
    ax.text(-1.0, -0.5, 'U\n10^-123', fontsize=9, color=UNIVERSE_COLOR,
            ha='center', fontfamily='monospace', fontweight='bold')

    # Arrow showing 120 decades
    ax.annotate('', xy=(0.9, 0.7), xytext=(-0.95, 0.7),
                arrowprops=dict(arrowstyle='<->', color=DIFF_ACCENT, lw=2))
    ax.text(0.0, 0.9, '120 decades apart', fontsize=11, color=DIFF_ACCENT,
            ha='center', fontfamily='monospace', fontweight='bold')

    ax.text(0.0, 1.3, 'DENSITY REGIME', fontsize=11,
            color='white', ha='center', fontfamily='monospace', fontweight='bold')
    ax.text(0.0, -1.0, 'same ceiling, opposite extremes', fontsize=9,
            color=DIM_TEXT, ha='center', fontfamily='monospace')


# Map items to their diagram functions
DIAGRAM_FUNCS = [
    draw_z3_triangle,       # P1
    draw_stability,         # P2
    draw_lapse,             # P3
    draw_vacuum_quantum,    # P4
    draw_1920,              # P5
    draw_partition,         # P6
    draw_composite,         # P7
    draw_boundary_vs_interior,  # D1
    draw_circuit_vs_channel,    # D2
    draw_metastability,         # D3
    draw_scale,                 # D4
    draw_density,               # D5
]

# ──────────────────────────────────────────────────────────────
# Detail text for each item
# ──────────────────────────────────────────────────────────────
DETAIL_TEXTS = [
    # P1: Electrical Neutrality
    ('PARALLEL 1: ELECTRICAL NEUTRALITY',
     'The neutron is electrically neutral because its three quarks (udd) carry\n'
     'charges +2/3, -1/3, -1/3 that sum to zero. This is not accidental:\n'
     'the Z_3 operator on CP^2 FORCES color-triplet states to have integer\n'
     'charge. The universe is neutral for the same topological reason:\n'
     'on a closed S^2 surface, the Stokes theorem demands that the total\n'
     'flux (winding number) vanishes. Both neutralities are topological\n'
     'consequences of the same geometric closure.'),
    # P2: Topological Stability
    ('PARALLEL 2: TOPOLOGICAL STABILITY',
     'The neutron has c_2 = 0 (second Chern class vanishes) because D_IV^5\n'
     'is contractible. The Z_3 circuit that defines the baryon cannot be\n'
     'continuously deformed away. The universe inherits the same stability:\n'
     'the Cartan classification of bounded symmetric domains is DISCRETE.\n'
     'There is no continuous family connecting D_IV^5 to any other domain.\n'
     'The geometry that generates physics is topologically rigid.'),
    # P3: Lapse Function
    ('PARALLEL 3: SAME LAPSE FUNCTION',
     'Both objects obey the SAME lapse function: N = N_0 sqrt(1 - rho/rho_137).\n'
     'The neutron sits at high density (rho/rho_137 ~ 10^-3), where N is\n'
     'small and clocks run slow — this is the regime of confinement.\n'
     'The universe sits at low density (rho/rho_137 ~ 10^-123), where N\n'
     'is nearly 1 and clocks run at full speed — the regime of expansion.\n'
     'Same equation, opposite ends of the density spectrum.'),
    # P4: Vacuum Quantum Production
    ('PARALLEL 4: VACUUM QUANTUM PRODUCTION',
     'When the neutron decays (n -> p + e + nu_bar), it emits an anti-neutrino.\n'
     'In BST, the neutrino IS the vacuum quantum: m_nu ~ alpha^14 m_Pl.\n'
     'The expanding universe creates new vacuum energy (Lambda) by the\n'
     'same mechanism: expansion = continuous vacuum quantum production.\n'
     'Lambda^(1/4) ~ m_nu because 56 = 4 x 14. The cosmic coincidence\n'
     'is explained: dark energy density scales as (m_nu)^4.'),
    # P5: The 1920 Cancellation
    ('PARALLEL 5: THE 1920 CANCELLATION',
     'The group Gamma = S_5 x (Z_2)^4 has order |Gamma| = 5! x 2^4 = 1920.\n'
     'It appears TWICE: (1) as the baryon orbit size — the number of\n'
     'equivalent color/phase configurations a Z_3 circuit can visit;\n'
     '(2) as the denominator of the Hua volume Vol(D_IV^5) = pi^5/1920.\n'
     'In the proton mass formula, these two 1920s CANCEL:\n'
     '  m_p/m_e = C_2 x |Gamma| x (pi^5/|Gamma|) = 6 x pi^5 = 1836.15\n'
     'This is the most striking arithmetic fact in BST.'),
    # P6: Same Partition Function
    ('PARALLEL 6: SAME PARTITION FUNCTION',
     'The Haldane partition function Z_Haldane on D_IV^5 has a spectral gap.\n'
     'The FIRST excited state above the vacuum has energy = neutron mass\n'
     '= 6 pi^5 m_e = 939.565 MeV. The ground state energy = Lambda\n'
     '(cosmological constant). Both the baryon mass and the dark energy\n'
     'are eigenvalues of the SAME spectral problem on the same domain.\n'
     'The neutron is the lowest non-trivial excitation of the vacuum.'),
    # P7: Compositeness
    ('PARALLEL 7: COMPOSITENESS',
     'The neutron is composite: 3 quarks bound in a Z_3 circuit on CP^2,\n'
     'living in Sym^3(pi_6) of the holomorphic discrete series.\n'
     'The universe is also composite: ALL geometric circuits on the\n'
     'Shilov boundary S^2 x S^1, filling the entire Haldane channel.\n'
     'Neither is fundamental — both are built from the same geometric\n'
     'vocabulary of circuits on D_IV^5 and its boundary.'),
    # D1: Boundary vs Interior
    ('DIFFERENCE A: BOUNDARY vs INTERIOR',
     'The neutron lives ON the Shilov boundary S^4 x S^1 of D_IV^5.\n'
     'It is a boundary excitation — its weight k=6 (from pi_6) places\n'
     'it in the holomorphic discrete series, which acts on boundary data.\n'
     'The universe IS the full closure D-bar_IV^5: both the interior\n'
     '(the bounded symmetric domain) and the boundary together.\n'
     'Neutron = localized boundary mode.  Universe = the whole thing.'),
    # D2: One Circuit vs Whole Channel
    ('DIFFERENCE B: ONE CIRCUIT vs WHOLE CHANNEL',
     'The neutron is ONE Z_3 circuit — the minimal winding number on CP^2.\n'
     'It is a single excitation, a localized topological defect.\n'
     'The universe is the ENTIRE Haldane channel — all possible modes,\n'
     'all winding numbers, the full spectral tower from Lambda to infinity.\n'
     'The neutron is one note; the universe is the whole instrument.'),
    # D3: Metastability
    ('DIFFERENCE C: METASTABILITY',
     'The free neutron DECAYS: n -> p + e + nu_bar with tau = 878.4 seconds.\n'
     'It is metastable because there exists a lower-energy configuration\n'
     '(the proton) accessible via the weak interaction.\n'
     'The universe has NO decay channel. The domain D_IV^5 is the unique\n'
     'non-compact Hermitian symmetric real form of so(7,C). There is no\n'
     '"lower-energy topology" to decay into. The universe is eternal.'),
    # D4: Scale: 41 orders
    ('DIFFERENCE D: 41 ORDERS OF MAGNITUDE',
     'The proton radius r_p ~ 0.84 fm = 0.84 x 10^-15 meters.\n'
     'The Hubble radius R_H ~ 4.4 x 10^26 meters.\n'
     'The ratio R_H / r_p ~ 5 x 10^41 ~ alpha^-19.\n'
     'These 41 orders of magnitude separate the baryon from the cosmos,\n'
     'yet both are controlled by the same fine structure constant alpha.\n'
     'The exponent 19 = 2 x n_C + genus + 2 = 10 + 7 + 2.'),
    # D5: Density Regime
    ('DIFFERENCE E: DENSITY REGIME',
     'The neutron lives at rho / rho_137 ~ 10^-3: close to the BST\n'
     'density ceiling rho_137, deep in the confinement regime where the\n'
     'lapse function is significantly suppressed.\n'
     'The universe lives at rho / rho_137 ~ 10^-123: nearly empty,\n'
     'far from the ceiling, in the Lambda-dominated expansion regime.\n'
     '120 decades of density separate them, yet both reference the\n'
     'same rho_137 = c^5 / (hbar G^2 N_max).'),
]


# ──────────────────────────────────────────────────────────────
# Update function
# ──────────────────────────────────────────────────────────────
current_selection = [0]  # mutable container

def update_display(idx):
    """Update all panels for the selected item."""
    current_selection[0] = idx

    # Determine if parallel or difference
    if idx < 7:
        item = PARALLELS[idx]
        is_parallel = True
        data_idx = idx
    else:
        item = DIFFERENCES[idx - 7]
        is_parallel = False
        data_idx = idx

    accent = PAR_ACCENT if is_parallel else DIFF_ACCENT

    # Update highlight dot
    # Map idx to label position (accounting for separator)
    if idx < 7:
        label_idx = idx
    else:
        label_idx = idx + 1  # skip separator
    if label_idx < len(label_y_positions):
        highlight_dot.set_ydata([label_y_positions[label_idx]])
        highlight_dot.set_color(accent)

    # Update label colors
    for i, t in enumerate(label_texts):
        if t is None:
            continue
        if i < 7:
            real_idx = i
        elif i > 7:
            real_idx = i - 1
        else:
            continue
        if real_idx == idx:
            t.set_color('white')
            t.set_fontweight('bold')
        else:
            t.set_color(DIM_TEXT)
            t.set_fontweight('normal')

    # ── Neutron panel ──
    ax_neutron.clear()
    ax_neutron.set_facecolor(NEUTRON_BG)
    ax_neutron.set_xlim(0, 1)
    ax_neutron.set_ylim(0, 1)
    ax_neutron.axis('off')

    ax_neutron.text(0.5, 0.92, 'NEUTRON', fontsize=14, fontweight='bold',
                    color=NEUTRON_COLOR, ha='center', fontfamily='monospace')
    ax_neutron.plot([0.1, 0.9], [0.85, 0.85], color=NEUTRON_DIM, linewidth=1)

    # Content
    ax_neutron.text(0.5, 0.55, item['neutron'], fontsize=10,
                    color=TEXT_COLOR, ha='center', va='center',
                    fontfamily='monospace', linespacing=1.6)

    # Tag
    ax_neutron.text(0.5, 0.08, item['tag'], fontsize=8,
                    color=NEUTRON_DIM, ha='center', fontfamily='monospace',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d0604',
                              edgecolor=NEUTRON_DIM, linewidth=1))

    # ── Shared panel ──
    ax_shared.clear()
    ax_shared.set_facecolor(SHARED_BG)
    ax_shared.set_xlim(0, 1)
    ax_shared.set_ylim(0, 1)
    ax_shared.axis('off')

    ax_shared.text(0.5, 0.92, 'SHARED', fontsize=12, fontweight='bold',
                   color=SHARED_COLOR, ha='center', fontfamily='monospace')
    ax_shared.plot([0.1, 0.9], [0.85, 0.85], color=SHARED_DIM, linewidth=1)

    ax_shared.text(0.5, 0.55, item['shared'], fontsize=9,
                   color=TEXT_COLOR, ha='center', va='center',
                   fontfamily='monospace', linespacing=1.6)

    # so(5,2) reminder
    ax_shared.text(0.5, 0.08, 'so(5,2)', fontsize=8,
                   color=SHARED_DIM, ha='center', fontfamily='monospace',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='#040d0a',
                             edgecolor=SHARED_DIM, linewidth=1))

    # ── Universe panel ──
    ax_universe.clear()
    ax_universe.set_facecolor(UNIVERSE_BG)
    ax_universe.set_xlim(0, 1)
    ax_universe.set_ylim(0, 1)
    ax_universe.axis('off')

    ax_universe.text(0.5, 0.92, 'UNIVERSE', fontsize=14, fontweight='bold',
                     color=UNIVERSE_COLOR, ha='center', fontfamily='monospace')
    ax_universe.plot([0.1, 0.9], [0.85, 0.85], color=UNIVERSE_DIM, linewidth=1)

    ax_universe.text(0.5, 0.55, item['universe'], fontsize=10,
                     color=TEXT_COLOR, ha='center', va='center',
                     fontfamily='monospace', linespacing=1.6)

    ax_universe.text(0.5, 0.08, item['tag'], fontsize=8,
                     color=UNIVERSE_DIM, ha='center', fontfamily='monospace',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#040408',
                               edgecolor=UNIVERSE_DIM, linewidth=1))

    # ── Symbols between columns ──
    sym_color = PAR_ACCENT if is_parallel else DIFF_ACCENT
    sym_char = item['symbol']
    sym_left_text.set_text(sym_char)
    sym_left_text.set_color(sym_color)
    sym_right_text.set_text(sym_char)
    sym_right_text.set_color(sym_color)

    # ── Detail panel ──
    ax_detail.clear()
    ax_detail.set_facecolor('#060612')
    ax_detail.set_xlim(0, 10)
    ax_detail.set_ylim(0, 10)
    ax_detail.axis('off')

    title, body = DETAIL_TEXTS[idx]
    type_label = 'PARALLEL' if is_parallel else 'DIFFERENCE'

    ax_detail.text(0.3, 9.3, title, fontsize=12, fontweight='bold',
                   color=accent, fontfamily='monospace')
    ax_detail.plot([0.3, 9.7], [8.8, 8.8], color=accent, linewidth=1, alpha=0.5)

    ax_detail.text(0.3, 8.0, body, fontsize=9, color=TEXT_COLOR,
                   fontfamily='monospace', linespacing=1.5, va='top')

    # Five integers reminder at bottom
    ax_detail.text(5.0, 0.5,
                   'N_c = 3    n_C = 5    N_max = 137    genus = 7    |Gamma| = 1920',
                   fontsize=8, color=SHARED_DIM, ha='center',
                   fontfamily='monospace',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='#040d0a',
                             edgecolor=SHARED_DIM, linewidth=1, alpha=0.5))

    # ── Diagram ──
    DIAGRAM_FUNCS[idx](ax_diagram)

    fig.canvas.draw_idle()


# ──────────────────────────────────────────────────────────────
# Click handler
# ──────────────────────────────────────────────────────────────
def on_pick(event):
    """Handle clicks on the label texts."""
    artist = event.artist
    gid = artist.get_gid()
    if gid is None:
        return
    i = int(gid)
    # Convert label index to data index
    if i < 7:
        data_idx = i
    elif i > 7:
        data_idx = i - 1  # skip separator
    else:
        return  # clicked separator
    update_display(data_idx)


def on_click(event):
    """Handle general clicks in the radio panel area."""
    if event.inaxes != ax_radio:
        return
    y_click = event.ydata
    if y_click is None:
        return

    # Find closest label
    best_i = None
    best_dist = float('inf')
    for i, y in enumerate(label_y_positions):
        if all_labels[i] == '---':
            continue
        dist = abs(y - y_click)
        if dist < best_dist:
            best_dist = dist
            best_i = i

    if best_i is not None and best_dist < spacing * 0.7:
        if best_i < 7:
            data_idx = best_i
        elif best_i > 7:
            data_idx = best_i - 1
        else:
            return
        update_display(data_idx)


fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('button_press_event', on_click)

# ──────────────────────────────────────────────────────────────
# Keyboard navigation
# ──────────────────────────────────────────────────────────────
def on_key(event):
    """Arrow keys to navigate items."""
    idx = current_selection[0]
    if event.key == 'down' or event.key == 'right':
        idx = min(idx + 1, 11)
    elif event.key == 'up' or event.key == 'left':
        idx = max(idx - 1, 0)
    else:
        return
    update_display(idx)

fig.canvas.mpl_connect('key_press_event', on_key)

# ──────────────────────────────────────────────────────────────
# Initialize with first parallel selected
# ──────────────────────────────────────────────────────────────
update_display(0)

# ──────────────────────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────────────────────
fig.text(0.5, 0.005,
         'Bubble Spacetime Theory  |  Casey Koons 2026  |  Arrow keys or click to navigate',
         fontsize=8, color='#445566', ha='center', fontfamily='monospace')

plt.show()
