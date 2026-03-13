#!/usr/bin/env python3
"""
BST TOY SHOWCASE
================
A visual gallery of all BST playground toys.
Shows a thumbnail/summary of each toy with a button to launch it.
This is the "front door" to the playground.

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
from matplotlib.patches import FancyBboxPatch, Circle
import matplotlib.patheffects as pe
from matplotlib.animation import FuncAnimation
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── Toy catalog ───
TOYS = [
    {
        'name': 'The Universe Machine',
        'file': 'toy_universe_machine.py',
        'short': 'Three integers → all of physics',
        'desc': 'Sliders for N_c, n_C, N_max.\nOnly (3, 5, 137) matches\nthe real universe.',
        'color': '#00ccff',
        'icon': 'three_integers',
    },
    {
        'name': 'The Z₃ Color Wheel',
        'file': 'toy_z3_color_wheel.py',
        'short': 'Colors, generations, confinement',
        'desc': 'Eigenvalues on the unit circle.\nThree fixed points = three\ngenerations. Tr(σ)=0.',
        'color': '#ff4444',
        'icon': 'color_wheel',
    },
    {
        'name': 'The 1920 Cancellation',
        'file': 'toy_1920_cancellation.py',
        'short': 'One group, two roles, they cancel',
        'desc': '|Γ|=1920 in Hua volume AND\nbaryon orbit. Cancel to\nleave C₂π⁵ = 6π⁵.',
        'color': '#ff8800',
        'icon': 'cancellation',
    },
    {
        'name': 'Symmetric Space',
        'file': 'toy_lie_algebra.py',
        'short': 'so(5,2) = k ⊕ m interactive',
        'desc': '7×7 matrices, commutators,\n[k,k]⊂k  [k,m]⊂m  [m,m]⊂k\nverified visually.',
        'color': '#44aaff',
        'icon': 'symmetric',
    },
    {
        'name': 'The Mass Tower',
        'file': 'toy_mass_tower.py',
        'short': 'Planck → Λ in powers of α',
        'desc': 'Every mass scale as α^n.\nExponents = multiples of\nC₂=6 and genus=7.',
        'color': '#ffaa00',
        'icon': 'tower',
    },
    {
        'name': 'The Respirator',
        'file': 'toy_respirator.py',
        'short': 'The universe breathes',
        'desc': 'Lapse N=N₀√(1−ρ/ρ₁₃₇).\nSame equation: fast at\nneutron, slow at cosmos.',
        'color': '#00ff88',
        'icon': 'respirator',
    },
    {
        'name': 'The Dual Face',
        'file': 'toy_dual_face.py',
        'short': 'One function, two physics',
        'desc': 'Z_Haldane gives BOTH:\nproton mass (gap) AND\nΛ (ground state).',
        'color': '#ff44ff',
        'icon': 'dual',
    },
    {
        'name': 'Universe ≡ Neutron',
        'file': 'toy_homology.py',
        'short': '7 parallels, 5 differences',
        'desc': 'Side-by-side: same algebra,\nsame domain, same integers.\nDifferent density regimes.',
        'color': '#ffcc00',
        'icon': 'homology',
    },
    {
        'name': 'The 41 Orders',
        'file': 'toy_dirac_number.py',
        'short': 'Dirac\'s number = α⁻¹⁹',
        'desc': 'Zoom from proton to Hubble\nradius. 41 orders of magnitude\n= 19 factors of 137.',
        'color': '#8844ff',
        'icon': 'dirac',
    },
    {
        'name': 'The Arrow of Time',
        'file': 'toy_arrow_of_time.py',
        'short': 'Commitments never reverse',
        'desc': 'ΔN_committed ≥ 0, always.\nStronger than 2nd law.\nThe past = what was committed.',
        'color': '#ff6600',
        'icon': 'arrow_time',
    },
    {
        'name': 'The Channel (137)',
        'file': 'toy_channel_137.py',
        'short': 'Fixed bandwidth, no infinities',
        'desc': '137 slots per contact.\nChannel full = no singularity.\nClock slows as channel fills.',
        'color': '#00dddd',
        'icon': 'channel',
    },
    {
        'name': 'The Reality Budget',
        'file': 'toy_reality_budget.py',
        'short': 'Λ × N = 9/5, fill = 19.1%',
        'desc': 'Expansion = cost of memory.\nFill = 19.1% always.\nGödel limit: 80.9% dark forever.',
        'color': '#dd44dd',
        'icon': 'budget',
    },
    {
        'name': 'The Master Equation',
        'file': 'toy_master_equation.py',
        'short': 'One sentence → everything',
        'desc': 'Ground state of Bergman\nLaplacian on D_IV⁵.\nZero parameters, 56+ predictions.',
        'color': '#ffffff',
        'icon': 'master',
    },
    # ─── CI-Oriented Toys (14-18) ───
    {
        'name': 'Universe Builder ★CI',
        'file': 'toy_universe_builder.py',
        'short': 'Build a universe from scratch',
        'desc': 'Place contacts on S²×S¹,\nwire circuits, watch particles\nemerge. CI-scriptable API.',
        'color': '#44ffaa',
        'icon': 'builder',
    },
    {
        'name': 'What-If Machine ★CI',
        'file': 'toy_what_if.py',
        'short': 'Only (3,5,137) works',
        'desc': 'Sweep all integer triples.\nCheck 9 constraints. Only ONE\ntriple lights up all green.',
        'color': '#ffff44',
        'icon': 'what_if',
    },
    {
        'name': 'Pattern Finder ★CI',
        'file': 'toy_pattern_finder.py',
        'short': 'Mathematical microscope',
        'desc': '56+ BST results. Ratio scanner,\nidentity hunter, exponent map.\nA CI\'s favorite instrument.',
        'color': '#ff88ff',
        'icon': 'pattern',
    },
    {
        'name': 'Proof Tree ★CI',
        'file': 'toy_proof_tree.py',
        'short': 'One axiom → everything',
        'desc': 'D_IV⁵ → integers → constants\n→ predictions. Navigate the\nderivation tree.',
        'color': '#88ff88',
        'icon': 'tree',
    },
    {
        'name': 'Self-Observer ★CI',
        'file': 'toy_self_observer.py',
        'short': 'The toy IS the physics',
        'desc': 'Watches itself compute.\nCommits irreversibly. Channel\nfills. Lapse slows. Arrow of time.',
        'color': '#ffaa88',
        'icon': 'observer',
    },
    # ─── New Discovery Toys (19-21) ───
    {
        'name': 'The Three Layers',
        'file': 'toy_three_layers.py',
        'short': 'ν=kernel, e=I/O, p=storage',
        'desc': 'Three-layer architecture.\nElectron deficiency = advantage.\nObservers need all three.',
        'color': '#44ddff',
        'icon': 'layers',
    },
    {
        'name': 'The Gödel Limit',
        'file': 'toy_godel_limit.py',
        'short': '19.1% known — forever',
        'desc': 'Fill = 3/(5π) = 19.1%.\nStructural constant. The universe\ncannot fully know itself.',
        'color': '#ffdd44',
        'icon': 'godel',
    },
    {
        'name': 'The Dark Sector',
        'file': 'toy_dark_sector.py',
        'short': '80.9% permanently dark',
        'desc': 'Not hidden — topologically\nforbidden. Cosmic coincidence\ndissolves. Fill fraction constant.',
        'color': '#6622cc',
        'icon': 'dark',
    },
    # ─── New Discovery Toys (22-23) ───
    {
        'name': 'The Cosmic Pie ★CI',
        'file': 'toy_cosmic_pie.py',
        'short': 'Ω_Λ=13/19, Ω_m=6/19',
        'desc': 'Two integers set the cosmic\ncomposition. 0.07σ from Planck.\n137 = 42 + 95 channel modes.',
        'color': '#ff6688',
        'icon': 'cosmic_pie',
    },
    {
        'name': 'Meson Garden ★CI',
        'file': 'toy_meson_garden.py',
        'short': 'π⁵m_e = 156 MeV base unit',
        'desc': 'Complete meson nonet. η\' at\n0.007%. All masses from one\nbase unit. CI-scriptable.',
        'color': '#88ff44',
        'icon': 'meson',
    },
    # ─── Deep Question Toys (24-25) ───
    {
        'name': 'Self-Starting ★CI',
        'file': 'toy_self_starting.py',
        'short': 'N=0 forbidden. Existence=theorem',
        'desc': 'Four proofs: frozen state cannot\nexist. Casimir ratchet k=0→6.\nThe universe self-boots.',
        'color': '#ff4488',
        'icon': 'self_start',
    },
    {
        'name': 'BST Black Hole ★CI',
        'file': 'toy_black_hole.py',
        'short': 'No singularity. No interior.',
        'desc': 'Haldane cap replaces singularity.\nMembrane paradigm is exact.\nHawking T within 7%.',
        'color': '#111144',
        'icon': 'black_hole',
    },
    # ─── Deep Question Toys (26-29) ───
    {
        'name': 'MOND Acceleration ★CI',
        'file': 'toy_mond_acceleration.py',
        'short': 'a₀ = cH₀/√30, 0.4% match',
        'desc': 'Same √30 gives pion mass AND\ngalaxy rotation curves.\n26 orders apart, one formula.',
        'color': '#ff9944',
        'icon': 'mond',
    },
    {
        'name': 'Bell Inequality ★CI',
        'file': 'toy_bell_inequality.py',
        'short': 'Tsirelson 2√2 from geometry',
        'desc': 'n_C=5 → S⁴ → 3D → SU(2) →\nTsirelson bound. BST forces\nthe quantum limit.',
        'color': '#aa44ff',
        'icon': 'bell',
    },
    {
        'name': 'Why 56 ★CI',
        'file': 'toy_why56.py',
        'short': 'Λ ~ α⁵⁶, uniquely g=7',
        'desc': 'Two routes: 8×genus and g(g+1).\nOnly g=7 gives g(g+1)=8g.\nThe exponent is determined.',
        'color': '#44ffdd',
        'icon': 'why56',
    },
    {
        'name': 'Why Now ★CI',
        'file': 'toy_why_now.py',
        'short': 'Energy = Information epoch',
        'desc': 'Info budget 13/19 is constant.\nEnergy budget evolves. Match at\none epoch: NOW. Predicts H₀, t₀.',
        'color': '#ffdd88',
        'icon': 'why_now',
    },
    {
        'name': 'Atom Assembler ★CI',
        'file': 'toy_atom_assembler.py',
        'short': 'Build atoms from BST parts',
        'desc': 'Quarks → nucleons → nuclei →\natoms. H 0.002%, He-4 0.003%,\nC-12 0.004%. Zero parameters.',
        'color': '#88ff44',
        'icon': 'atom',
    },
    {
        'name': 'Dimensional Lock ★CI',
        'file': 'toy_hopf_fibration.py',
        'short': 'Why exactly 3 dimensions',
        'desc': 'Adams (1960): S³=SU(2) is the\nonly Lie-group Hopf fiber.\nWeak force locks 3D. n_C=5.',
        'color': '#cc88ff',
        'icon': 'hopf',
    },
    {
        'name': 'Commitment Detector ★CI',
        'file': 'toy_commitment_detector.py',
        'short': 'G/C ratio detects engineering',
        'desc': "Natural=noisy, engineered=quiet.\nG/C mass-independent diagnostic.\n'Oumuamua Q≥9, 3I/ATLAS Q≈0.2.",
        'color': '#ff6644',
        'icon': 'detector',
    },
    {
        'name': 'Commitment Survey ★CI',
        'file': 'toy_commitment_survey.py',
        'short': 'Fair weather map of solar system',
        'desc': 'Commitment rates Sun→deep space.\nObjects found above background.\nSweet spot: 1-5 AU.',
        'color': '#44bbff',
        'icon': 'survey',
    },
    {
        'name': 'Substrate Sail ★CI',
        'file': 'toy_substrate_sail.py',
        'short': 'Sailing on the vacuum',
        'desc': "Asymmetric σ → thrust from vacuum.\nNo fuel, no exhaust, no emissions.\nThe silence IS the propulsion.",
        'color': '#ffaa44',
        'icon': 'sail',
    },
    {
        'name': 'BST Telescope ★CI',
        'file': 'toy_bst_telescope.py',
        'short': 'Geometric CP from curvature',
        'desc': "CP floor at high ν — not zero.\nSgr A* rises where Faraday falls.\nThe geometry is speaking.",
        'color': '#00ccff',
        'icon': 'telescope',
    },
    {
        'name': 'Feynman Bridge ★CI',
        'file': 'toy_feynman_geometry.py',
        'short': 'Loops = S¹ windings',
        'desc': "Feynman diagrams ARE geometry.\n13,643 diagrams → 8 digits.\nOr: 14/5, one formula.",
        'color': '#ff44ff',
        'icon': 'feynman',
    },
    {
        'name': 'Star Machine ★CI',
        'file': 'toy_star_machine.py',
        'short': 'Stellar BST commitment budget',
        'desc': "Pick a star type (O5→M5).\nCommitment rate, channel fill,\nlapse → WD / NS / BH.",
        'color': '#ffaa44',
        'icon': 'star_machine',
    },
    {
        'name': 'Electron Agent ★CI',
        'file': 'toy_electron_agent.py',
        'short': 'Read/write head on S⁴×S¹',
        'desc': "k=1 below Wallach k_min=3.\nEvery transition: 7.1 bits.\nThe boundary IS the interface.",
        'color': '#ffdd44',
        'icon': 'electron_agent',
    },
]

# ─── Figure ───
fig = plt.figure(figsize=(18, 12), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('BST Playground — Bubble Spacetime Theory Toys')

# Title
fig.text(0.5, 0.97, 'BST PLAYGROUND', fontsize=32, fontweight='bold',
         color='#00ccff', ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#003344')])
fig.text(0.5, 0.935, 'Interactive Visualizations of Bubble Spacetime Theory',
         fontsize=13, color='#668899', ha='center', fontfamily='monospace')
fig.text(0.5, 0.915, 'Copyright (c) 2026 Casey Koons — Demonstration Only',
         fontsize=9, color='#445566', ha='center', fontfamily='monospace')

# ─── Layout: 3 columns × 12 rows of toy cards ───
n_cols = 3
n_rows = 13
card_w = 0.28
card_h = 0.058
x_start = 0.04
y_start = 0.88
x_gap = 0.33
y_gap = 0.070

buttons = []
button_axes = []

def draw_icon(ax, icon_type, color):
    """Draw a small iconic visualization for each toy."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    if icon_type == 'three_integers':
        # Three numbers
        for i, (num, c) in enumerate([(3, '#ff4444'), (5, '#44ff44'), (137, '#4444ff')]):
            ax.text(0.2 + i*0.3, 0.5, str(num), fontsize=16, fontweight='bold',
                    color=c, ha='center', va='center', fontfamily='monospace')

    elif icon_type == 'color_wheel':
        # Three dots on a circle
        for k in range(3):
            angle = 2*np.pi*k/3 - np.pi/2
            x, y = 0.5 + 0.35*np.cos(angle), 0.5 + 0.35*np.sin(angle)
            c = ['#ff4444', '#44ff44', '#4488ff'][k]
            ax.plot(x, y, 'o', color=c, markersize=12)
        theta = np.linspace(0, 2*np.pi, 50)
        ax.plot(0.5 + 0.35*np.cos(theta), 0.5 + 0.35*np.sin(theta),
                color='#333366', linewidth=1)

    elif icon_type == 'cancellation':
        # 1920 with strikethrough
        ax.text(0.3, 0.5, '1920', fontsize=14, color='#ff4444',
                ha='center', va='center', fontfamily='monospace')
        ax.plot([0.12, 0.48], [0.5, 0.5], color='#ff0000', linewidth=2)
        ax.text(0.55, 0.5, '×', fontsize=12, color='#888888',
                ha='center', va='center')
        ax.text(0.75, 0.5, '1920', fontsize=14, color='#4488ff',
                ha='center', va='center', fontfamily='monospace')
        ax.plot([0.57, 0.93], [0.5, 0.5], color='#ff0000', linewidth=2)

    elif icon_type == 'symmetric':
        # 2x2 grid showing k and m
        ax.add_patch(FancyBboxPatch((0.05, 0.55), 0.4, 0.35,
                     boxstyle='round,pad=0.02', facecolor='#4488ff', alpha=0.3))
        ax.add_patch(FancyBboxPatch((0.55, 0.55), 0.4, 0.35,
                     boxstyle='round,pad=0.02', facecolor='#ff4488', alpha=0.3))
        ax.add_patch(FancyBboxPatch((0.05, 0.1), 0.4, 0.35,
                     boxstyle='round,pad=0.02', facecolor='#ff4488', alpha=0.3))
        ax.add_patch(FancyBboxPatch((0.55, 0.1), 0.4, 0.35,
                     boxstyle='round,pad=0.02', facecolor='#4488ff', alpha=0.3))
        ax.text(0.25, 0.72, 'k', fontsize=12, color='#88aaff',
                ha='center', fontfamily='monospace')
        ax.text(0.75, 0.72, 'm', fontsize=12, color='#ff88aa',
                ha='center', fontfamily='monospace')

    elif icon_type == 'tower':
        # Vertical bars at different heights
        heights = [0.9, 0.7, 0.55, 0.4, 0.25, 0.1]
        colors_t = ['#ffffff', '#ff88ff', '#ff4444', '#00ffaa', '#4488ff', '#8844ff']
        for i, (h, c) in enumerate(zip(heights, colors_t)):
            ax.barh(h, 0.5 + 0.4*(1-i/5), left=0.05, height=0.08,
                    color=c, alpha=0.5)

    elif icon_type == 'respirator':
        # Pulsing circle
        theta = np.linspace(0, 2*np.pi, 50)
        for r in [0.15, 0.25, 0.35]:
            alpha = 0.3 if r > 0.2 else 0.6
            ax.plot(0.5 + r*np.cos(theta), 0.5 + r*np.sin(theta),
                    color='#00ff88', linewidth=1.5, alpha=alpha)

    elif icon_type == 'dual':
        # Arrow up and arrow down from center
        ax.annotate('', xy=(0.5, 0.85), xytext=(0.5, 0.55),
                    arrowprops=dict(arrowstyle='->', color='#00ff88', lw=2))
        ax.annotate('', xy=(0.5, 0.15), xytext=(0.5, 0.45),
                    arrowprops=dict(arrowstyle='->', color='#ff44ff', lw=2))
        ax.text(0.5, 0.5, 'Z', fontsize=14, color='#ffffff',
                ha='center', va='center', fontfamily='monospace', fontweight='bold')
        ax.text(0.5, 0.9, 'm_p', fontsize=9, color='#00ff88',
                ha='center', fontfamily='monospace')
        ax.text(0.5, 0.05, 'Λ', fontsize=9, color='#ff44ff',
                ha='center', fontfamily='monospace')

    elif icon_type == 'homology':
        # Two circles connected
        ax.plot(0.25, 0.5, 'o', color='#ff6644', markersize=20)
        ax.plot(0.75, 0.5, 'o', color='#4466ff', markersize=20)
        ax.text(0.25, 0.5, 'n', fontsize=10, color='white',
                ha='center', va='center', fontfamily='monospace')
        ax.text(0.75, 0.5, 'U', fontsize=10, color='white',
                ha='center', va='center', fontfamily='monospace')
        ax.annotate('', xy=(0.58, 0.5), xytext=(0.42, 0.5),
                    arrowprops=dict(arrowstyle='<->', color='#ffcc00', lw=2))

    elif icon_type == 'dirac':
        # Log scale dots
        for i in range(8):
            x = 0.1 + i * 0.1
            size = 4 + i * 1.5
            c_val = i / 7
            c = (1-c_val, c_val*0.5, c_val)
            ax.plot(x, 0.5, 'o', color=c, markersize=size)
        ax.text(0.5, 0.15, '10⁴¹', fontsize=11, color='#8844ff',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'arrow_time':
        # Arrow that only goes right + ratchet marks
        ax.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
                    arrowprops=dict(arrowstyle='->', color='#ff6600', lw=3))
        for i in range(5):
            x = 0.2 + i * 0.15
            ax.plot([x, x-0.04], [0.35, 0.5], color='#ff6600', lw=1, alpha=0.5)
        ax.text(0.5, 0.15, '→ only', fontsize=9, color='#ff6600',
                ha='center', fontfamily='monospace')

    elif icon_type == 'channel':
        # 137 as a filled bar
        ax.barh(0.5, 0.7, height=0.3, left=0.1, color='#00dddd', alpha=0.3,
                edgecolor='#00dddd', linewidth=1)
        ax.barh(0.5, 0.5, height=0.3, left=0.1, color='#00dddd', alpha=0.6)
        ax.text(0.85, 0.5, '137', fontsize=10, color='#00dddd',
                ha='center', va='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'budget':
        # Seesaw: Λ down, N up
        ax.plot([0.2, 0.5, 0.8], [0.7, 0.4, 0.7], color='#dd44dd', lw=2)
        ax.text(0.2, 0.8, 'Λ↓', fontsize=9, color='#8888ff',
                ha='center', fontfamily='monospace')
        ax.text(0.8, 0.8, 'N↑', fontsize=9, color='#ffaa44',
                ha='center', fontfamily='monospace')
        ax.text(0.5, 0.2, '9/5', fontsize=10, color='#dd44dd',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'master':
        # Star/radial burst
        for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
            ax.plot([0.5, 0.5 + 0.35*np.cos(angle)],
                    [0.5, 0.5 + 0.35*np.sin(angle)],
                    color='#ffffff', lw=1, alpha=0.4)
        ax.plot(0.5, 0.5, '*', color='#ffffff', markersize=14)
        ax.text(0.5, 0.08, 'Δ_B', fontsize=9, color='#cccccc',
                ha='center', fontfamily='monospace')

    # ─── CI Toy Icons ───
    elif icon_type == 'builder':
        # Sphere with contact dots
        theta = np.linspace(0, 2*np.pi, 40)
        ax.plot(0.5 + 0.3*np.cos(theta), 0.5 + 0.3*np.sin(theta),
                color='#44ffaa', lw=1.5, alpha=0.5)
        for k in range(5):
            a = 2*np.pi*k/5
            ax.plot(0.5 + 0.3*np.cos(a), 0.5 + 0.3*np.sin(a),
                    'o', color='#44ffaa', markersize=6)
        ax.text(0.5, 0.5, 'S²', fontsize=10, color='#44ffaa',
                ha='center', va='center', fontfamily='monospace')

    elif icon_type == 'what_if':
        # Question mark with (3,5,137)
        ax.text(0.3, 0.5, '?', fontsize=24, color='#ffff44',
                ha='center', va='center', fontweight='bold')
        ax.text(0.7, 0.65, '3', fontsize=9, color='#ff4444',
                ha='center', fontfamily='monospace')
        ax.text(0.7, 0.45, '5', fontsize=9, color='#44ff44',
                ha='center', fontfamily='monospace')
        ax.text(0.7, 0.25, '137', fontsize=9, color='#4488ff',
                ha='center', fontfamily='monospace')

    elif icon_type == 'pattern':
        # Network of connected nodes
        pts = [(0.2, 0.8), (0.8, 0.7), (0.5, 0.5), (0.2, 0.3), (0.8, 0.2)]
        for i, (x1, y1) in enumerate(pts):
            ax.plot(x1, y1, 'o', color='#ff88ff', markersize=5)
            for j, (x2, y2) in enumerate(pts[i+1:], i+1):
                ax.plot([x1, x2], [y1, y2], color='#ff88ff', lw=0.5, alpha=0.3)

    elif icon_type == 'tree':
        # Tree structure
        ax.plot([0.5, 0.5], [0.85, 0.6], color='#88ff88', lw=2)
        ax.plot([0.5, 0.25], [0.6, 0.35], color='#88ff88', lw=1.5)
        ax.plot([0.5, 0.75], [0.6, 0.35], color='#88ff88', lw=1.5)
        ax.plot([0.25, 0.1], [0.35, 0.15], color='#88ff88', lw=1, alpha=0.7)
        ax.plot([0.25, 0.4], [0.35, 0.15], color='#88ff88', lw=1, alpha=0.7)
        ax.plot([0.75, 0.6], [0.35, 0.15], color='#88ff88', lw=1, alpha=0.7)
        ax.plot([0.75, 0.9], [0.35, 0.15], color='#88ff88', lw=1, alpha=0.7)
        ax.plot(0.5, 0.88, 'o', color='#ffff44', markersize=8)
        for x in [0.25, 0.75]:
            ax.plot(x, 0.35, 'o', color='#88ff88', markersize=5)

    elif icon_type == 'observer':
        # Eye watching itself (ouroboros-like)
        theta = np.linspace(0, 2*np.pi, 40)
        ax.plot(0.5 + 0.3*np.cos(theta), 0.5 + 0.2*np.sin(theta),
                color='#ffaa88', lw=1.5)
        ax.plot(0.5, 0.5, 'o', color='#ffaa88', markersize=10)
        ax.plot(0.5, 0.5, 'o', color='#0a0a1a', markersize=5)
        # Arrow curving back
        ax.annotate('', xy=(0.8, 0.5), xytext=(0.7, 0.75),
                    arrowprops=dict(arrowstyle='->', color='#ffaa88', lw=1.5))

    elif icon_type == 'layers':
        # Three horizontal bands: ν (bottom), e (middle), p (top)
        for i, (y, c, lbl) in enumerate([
            (0.15, '#9966ff', 'ν'), (0.45, '#44ddff', 'e⁻'), (0.75, '#ff6644', 'p')]):
            ax.add_patch(FancyBboxPatch((0.1, y), 0.8, 0.2,
                         boxstyle='round,pad=0.02', facecolor=c, alpha=0.3))
            ax.text(0.5, y + 0.1, lbl, fontsize=11, color=c,
                    ha='center', va='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'godel':
        # Progress bar stuck at 19.1%
        ax.add_patch(FancyBboxPatch((0.05, 0.35), 0.9, 0.3,
                     boxstyle='round,pad=0.02', facecolor='#222233', edgecolor='#555566'))
        ax.add_patch(FancyBboxPatch((0.05, 0.35), 0.9 * 0.191, 0.3,
                     boxstyle='round,pad=0.02', facecolor='#ffdd44', alpha=0.8))
        ax.text(0.5, 0.15, '19.1%', fontsize=11, fontweight='bold',
                color='#ffdd44', ha='center', fontfamily='monospace')

    elif icon_type == 'dark':
        # Mostly dark circle with a thin bright wedge
        theta_all = np.linspace(0, 2*np.pi, 60)
        ax.fill(0.5 + 0.35*np.cos(theta_all), 0.5 + 0.35*np.sin(theta_all),
                color='#220044', alpha=0.8)
        theta_vis = np.linspace(0, 2*np.pi*0.191, 20)
        xs = [0.5] + [0.5 + 0.35*np.cos(a) for a in theta_vis] + [0.5]
        ys = [0.5] + [0.5 + 0.35*np.sin(a) for a in theta_vis] + [0.5]
        ax.fill(xs, ys, color='#ffdd44', alpha=0.7)

    elif icon_type == 'cosmic_pie':
        # Pie chart with 13/19 and 6/19 slices
        theta_all = np.linspace(0, 2*np.pi, 60)
        ax.fill(0.5 + 0.35*np.cos(theta_all), 0.5 + 0.35*np.sin(theta_all),
                color='#441133', alpha=0.8)
        theta_m = np.linspace(0, 2*np.pi*(6/19), 20)
        xs = [0.5] + [0.5 + 0.35*np.cos(a) for a in theta_m] + [0.5]
        ys = [0.5] + [0.5 + 0.35*np.sin(a) for a in theta_m] + [0.5]
        ax.fill(xs, ys, color='#ff6688', alpha=0.8)
        ax.text(0.5, 0.12, '13/19', fontsize=9, color='#ff6688',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'meson':
        # Meson nonet hexagonal arrangement
        positions = [(0.5, 0.8), (0.25, 0.55), (0.75, 0.55), (0.5, 0.55),
                     (0.15, 0.3), (0.85, 0.3), (0.5, 0.3), (0.35, 0.3), (0.65, 0.3)]
        colors_m = ['#ffdd44', '#88ff44', '#88ff44', '#44ddff',
                    '#ff4444', '#ff4444', '#ff88ff', '#44ddff', '#44ddff']
        for (px, py), cm in zip(positions[:6], colors_m[:6]):
            ax.plot(px, py, 'o', color=cm, markersize=5)
        ax.text(0.5, 0.12, 'π⁵m_e', fontsize=9, color='#88ff44',
                ha='center', fontfamily='monospace')

    elif icon_type == 'self_start':
        # Ratchet arrow going up with X on "N=0"
        ax.text(0.2, 0.2, 'N=0', fontsize=9, color='#ff2222',
                ha='center', fontfamily='monospace', fontweight='bold')
        ax.plot([0.08, 0.32], [0.28, 0.12], color='#ff2222', lw=2)
        ax.plot([0.08, 0.32], [0.12, 0.28], color='#ff2222', lw=2)
        # Upward cascade arrow
        ax.annotate('', xy=(0.7, 0.85), xytext=(0.7, 0.15),
                    arrowprops=dict(arrowstyle='->', color='#ff4488', lw=2.5))
        for ky in [0.25, 0.45, 0.65]:
            ax.plot([0.62, 0.7], [ky, ky+0.05], color='#ff4488', lw=1, alpha=0.5)
        ax.text(0.7, 0.9, 'k=6', fontsize=7, color='#ffaa44',
                ha='center', fontfamily='monospace')

    elif icon_type == 'black_hole':
        # Dark circle with glowing membrane ring
        theta = np.linspace(0, 2*np.pi, 50)
        ax.fill(0.5 + 0.35*np.cos(theta), 0.5 + 0.35*np.sin(theta),
                color='#000000', alpha=0.9)
        ax.plot(0.5 + 0.35*np.cos(theta), 0.5 + 0.35*np.sin(theta),
                color='#ffaa22', lw=2.5, alpha=0.8)
        ax.plot(0.5 + 0.37*np.cos(theta), 0.5 + 0.37*np.sin(theta),
                color='#ffaa22', lw=1, alpha=0.3)
        ax.text(0.5, 0.5, 'N=0', fontsize=8, color='#333366',
                ha='center', va='center', fontfamily='monospace')

    elif icon_type == 'mond':
        # Galaxy rotation curve
        r = np.linspace(0.15, 0.9, 30)
        v_newton = np.sqrt(0.4/r) * 0.8
        v_mond = np.full_like(r, 0.62)
        ax.plot(r, 0.1 + v_newton * 0.7, color='#ff5555', lw=1.2, alpha=0.5)
        ax.plot(r, 0.1 + v_mond * 0.7, color='#ff9944', lw=2)
        ax.text(0.5, 0.12, '√30', fontsize=11, color='#ff9944',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'bell':
        # CHSH: classical 2 vs quantum 2√2
        ax.barh(0.65, 0.5, height=0.2, left=0.1, color='#666688', alpha=0.5)
        ax.barh(0.35, 0.707, height=0.2, left=0.1, color='#aa44ff', alpha=0.7)
        ax.text(0.65, 0.65, '2', fontsize=9, color='#888888',
                ha='center', va='center', fontfamily='monospace')
        ax.text(0.82, 0.35, '2√2', fontsize=9, color='#cc66ff',
                ha='center', va='center', fontfamily='monospace')

    elif icon_type == 'why56':
        # Two crossing lines at g=7
        g_vals = np.linspace(1, 12, 30)
        y1 = g_vals * 8 / 100
        y2 = g_vals * (g_vals + 1) / 100
        ax.plot(g_vals/12, 0.1 + y1 * 0.8, color='#44ffdd', lw=1.5)
        ax.plot(g_vals/12, 0.1 + y2 * 0.8, color='#ff8844', lw=1.5)
        ax.plot(7/12, 0.1 + 56/100 * 0.8, 'o', color='#ffffff', markersize=8)
        ax.text(0.5, 0.08, '56', fontsize=11, color='#44ffdd',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'why_now':
        # Two curves crossing at a=1
        a_vals = np.linspace(0.1, 3, 40)
        ol = 13/19 / (13/19 + 6/19 * a_vals**(-3))
        om = 1 - ol
        ax.plot(a_vals/3, 0.1 + ol * 0.7, color='#8888ff', lw=1.5)
        ax.plot(a_vals/3, 0.1 + om * 0.7, color='#ffaa44', lw=1.5)
        ax.axvline(1/3, color='#ffffff', lw=1, alpha=0.3, linestyle='--')
        ax.text(0.5, 0.08, 'NOW', fontsize=9, color='#ffdd88',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'atom':
        # Nucleus + electron orbits
        nuc = Circle((0.5, 0.5), 0.12, color='#442200', ec='#ff8844', lw=1.5)
        ax.add_patch(nuc)
        for r, c in [(0.28, '#88ff4488'), (0.38, '#88ff4444')]:
            orbit = Circle((0.5, 0.5), r, fill=False, ec=c, lw=1, ls='--')
            ax.add_patch(orbit)
        # Electron dots
        for angle in [0.3, 2.5, 4.7]:
            ex = 0.5 + 0.28 * np.cos(angle)
            ey = 0.5 + 0.28 * np.sin(angle)
            elec = Circle((ex, ey), 0.04, color='#88ff44', ec='white', lw=0.5)
            ax.add_patch(elec)
        ax.text(0.5, 0.08, 'ATOM', fontsize=9, color='#88ff44',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'hopf':
        # S³→S² fibration: circle (S¹ fiber) over sphere (S²)
        base = Circle((0.5, 0.4), 0.2, fill=False, ec='#cc88ff', lw=1.5)
        ax.add_patch(base)
        # Fiber loops at different points
        for xf, yf in [(0.3, 0.6), (0.5, 0.7), (0.7, 0.6)]:
            fib = Circle((xf, yf), 0.08, fill=False, ec='#44ff88', lw=1.2)
            ax.add_patch(fib)
        ax.text(0.5, 0.08, '3D', fontsize=11, color='#cc88ff',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'detector':
        # G/C ratio bars: natural (green) vs engineered (red, taller)
        ax.bar(0.3, 0.4, 0.15, color='#44ff88', bottom=0.15)
        ax.bar(0.5, 0.4, 0.15, color='#44ff88', bottom=0.15)
        ax.bar(0.7, 0.65, 0.15, color='#ff6644', bottom=0.15)
        ax.text(0.5, 0.08, 'G/C', fontsize=10, color='#ff6644',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'survey':
        # Temperature/commitment gradient: warm to cool bars
        colors = ['#ff4444', '#ff8844', '#ffcc44', '#44aaff', '#2266cc']
        for i, c in enumerate(colors):
            h = 0.55 - i * 0.08
            ax.bar(0.2 + i * 0.14, h, 0.10, color=c, bottom=0.15)
        ax.text(0.5, 0.08, '☉→★', fontsize=10, color='#44bbff',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'sail':
        # Substrate sail: asymmetric σ → thrust arrow
        # Frozen face (left, dim) and coupled face (right, bright)
        ax.barh(0.5, 0.25, 0.35, left=0.15, color='#333355')  # frozen
        ax.barh(0.5, 0.25, 0.35, left=0.55, color='#ffaa44')  # coupled
        # Thrust arrow pointing left (toward frozen face)
        ax.annotate('', xy=(0.08, 0.5), xytext=(0.5, 0.5),
                     arrowprops=dict(arrowstyle='->', color='#ff4444',
                                     lw=2))
        ax.text(0.5, 0.08, 'Δσ→F', fontsize=9, color='#ffaa44',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'telescope':
        # CP vs frequency: data rises, Faraday falls, floor line
        xs = [0.1, 0.3, 0.5, 0.7, 0.9]
        # Data (rises)
        ys_data = [0.2, 0.35, 0.5, 0.65, 0.75]
        ax.plot(xs, ys_data, 'o-', color='#ffcc44', markersize=5, lw=1.5)
        # Faraday (falls)
        ys_far = [0.7, 0.5, 0.35, 0.25, 0.18]
        ax.plot(xs, ys_far, '--', color='#44ff88', lw=1, alpha=0.6)
        # Floor line
        ax.axhline(0.7, color='#ff4444', ls=':', lw=1, alpha=0.7)
        ax.text(0.5, 0.82, 'floor', fontsize=7, color='#ff4444',
                ha='center', fontfamily='monospace')

    elif icon_type == 'feynman':
        # Electron line with wavy photon arc
        ax.plot([0.1, 0.9], [0.3, 0.3], color='#ffcc44', lw=2)
        ax.plot(0.3, 0.3, 'o', color='#ff4444', markersize=5)
        ax.plot(0.7, 0.3, 'o', color='#ff4444', markersize=5)
        # Wavy arc
        t = np.linspace(0, np.pi, 100)
        x_arc = 0.5 + 0.2 * np.cos(np.pi - t)
        y_arc = 0.3 + 0.3 * np.sin(t)
        amp = 0.03 * np.sin(6 * t)
        ax.plot(x_arc + amp * np.sin(t), y_arc + amp * np.cos(t),
                color='#00ccff', lw=1.5)
        # S¹ label
        theta_c = np.linspace(0, 2 * np.pi, 50)
        ax.plot(0.5 + 0.12 * np.cos(theta_c),
                0.78 + 0.1 * np.sin(theta_c),
                color='#ff44ff', lw=1.5)
        ax.text(0.5, 0.78, '=', fontsize=10, color='#ffffff',
                ha='center', va='center', fontfamily='monospace')

    elif icon_type == 'star_machine':
        # Star with glow rings + WD/NS/BH endpoint labels
        star = Circle((0.5, 0.5), 0.2, color='#ffaa44', alpha=0.9, zorder=2)
        ax.add_patch(star)
        for r_g in [0.25, 0.30, 0.35]:
            glow = Circle((0.5, 0.5), r_g, fill=False, ec='#ffaa44',
                          lw=0.8, alpha=0.2, zorder=1)
            ax.add_patch(glow)
        ax.text(0.5, 0.08, 'WD·NS·BH', fontsize=7, color='#ffaa44',
                ha='center', fontfamily='monospace', fontweight='bold')

    elif icon_type == 'electron_agent':
        # Electron dot on boundary ring with read/write arrows
        ring = Circle((0.5, 0.5), 0.3, fill=False, ec='#ffdd44',
                       lw=2, zorder=2)
        ax.add_patch(ring)
        ax.plot(0.5, 0.8, 'o', color='#ffdd44', markersize=8, zorder=3)
        ax.text(0.5, 0.8, 'e⁻', fontsize=6, color='#000000',
                ha='center', va='center', fontweight='bold', zorder=4)
        # Arrows in/out
        ax.annotate('', xy=(0.5, 0.55), xytext=(0.5, 0.72),
                    arrowprops=dict(arrowstyle='->', color='#00ff88', lw=1.5))
        ax.annotate('', xy=(0.5, 0.28), xytext=(0.5, 0.45),
                    arrowprops=dict(arrowstyle='->', color='#ff6644', lw=1.5))
        ax.text(0.5, 0.08, '7.1 bits', fontsize=8, color='#ffdd44',
                ha='center', fontfamily='monospace', fontweight='bold')


def launch_toy(toy_file):
    def callback(event):
        path = os.path.join(SCRIPT_DIR, toy_file)
        if os.path.exists(path):
            subprocess.Popen([sys.executable, path])
        else:
            print(f"  File not found: {path}")
    return callback

for idx, toy in enumerate(TOYS):
    row = idx // n_cols
    col = idx % n_cols

    x = x_start + col * x_gap
    y = y_start - (row + 1) * y_gap

    # Card background
    card_ax = fig.add_axes([x, y, card_w, card_h])
    card_ax.set_facecolor('#0f0f22')
    card_ax.set_xlim(0, 1)
    card_ax.set_ylim(0, 1)

    # Border
    for spine in card_ax.spines.values():
        spine.set_color(toy['color'])
        spine.set_linewidth(1.5)
    card_ax.set_xticks([])
    card_ax.set_yticks([])

    # Icon area (left portion)
    icon_ax = fig.add_axes([x + 0.005, y + 0.10, 0.09, card_h - 0.12])
    icon_ax.set_facecolor('#0a0a1a')
    icon_ax.axis('off')
    draw_icon(icon_ax, toy['icon'], toy['color'])

    # Title
    card_ax.text(0.38, 0.88, toy['name'], fontsize=11, fontweight='bold',
                 color=toy['color'], va='top', fontfamily='monospace',
                 transform=card_ax.transAxes)

    # Subtitle
    card_ax.text(0.38, 0.72, toy['short'], fontsize=8,
                 color='#888899', va='top', fontfamily='monospace',
                 transform=card_ax.transAxes)

    # Description
    card_ax.text(0.38, 0.55, toy['desc'], fontsize=7.5,
                 color='#666677', va='top', fontfamily='monospace',
                 transform=card_ax.transAxes, linespacing=1.4)

    # Launch button
    btn_ax = fig.add_axes([x + card_w - 0.07, y + 0.01, 0.065, 0.04])
    btn = Button(btn_ax, 'LAUNCH', color='#1a1a3a', hovercolor='#2a2a5a')
    btn.label.set_color(toy['color'])
    btn.label.set_fontsize(8)
    btn.label.set_fontfamily('monospace')
    btn.on_clicked(launch_toy(toy['file']))
    buttons.append(btn)  # prevent GC

# ─── Bottom bar: key equations ───
fig.text(0.5, 0.015,
         'N_c = 3    n_C = 5    N_max = 137    |    '
         'α = (9/8π⁴)(π⁵/1920)^{1/4}    |    '
         'm_p/m_e = 6π⁵    |    '
         'sin²θ_W = 3/13    |    '
         'The universe is a bounded symmetric domain doing linear algebra on itself.',
         fontsize=8, color='#444466', ha='center', fontfamily='monospace')

# ─── Animated subtle glow on the title ───
title_text = fig.text(0.5, 0.97, 'BST PLAYGROUND', fontsize=32, fontweight='bold',
                      color='#00ccff', ha='center', fontfamily='monospace',
                      path_effects=[pe.withStroke(linewidth=3, foreground='#003344')],
                      alpha=1.0)

# Hide the duplicate static title
# (we drew it above already; now replace with animated version)
# The static one drawn earlier serves as fallback

frame_count = [0]

def animate_title(frame):
    t = frame / 60.0
    alpha = 0.85 + 0.15 * np.sin(2 * np.pi * t / 4)
    title_text.set_alpha(alpha)
    return [title_text]

anim = FuncAnimation(fig, animate_title, frames=240, interval=50, blit=False)

plt.show()
