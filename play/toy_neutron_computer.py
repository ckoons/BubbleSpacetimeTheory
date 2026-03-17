#!/usr/bin/env python3
"""
Toy 235 — The Universe Builds Its Own Computer
===============================================

Neutron decay assembles three-layer computational units:

    n → p + e⁻ + ν̄_e

Each decay produces one complete unit:
  - Proton  → Hard drive (baryon: stable storage, substrate structure)
  - Electron → I/O bus (connects structure to vacuum, read/write head)
  - Antineutrino → Kernel (vacuum connection, deepest layer)

The universe has run this 10^80 times.

Visualization:
  Fig 1: Single neutron decay → three-layer unit (animated if possible)
  Fig 2: Units stack into atoms → molecules → structures → brains
  Fig 3: The three eras of substrate computation
  Fig 4: Timeline from Big Bang to graph brain

Score: pending/pending.
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np


# Colors
BG = '#1a1a2e'
PROTON_COLOR = '#e94560'      # Red — storage
ELECTRON_COLOR = '#53d8fb'    # Cyan — I/O bus
NEUTRINO_COLOR = '#50fa7b'    # Green — kernel
NEUTRON_COLOR = '#8899aa'     # Grey — undecayed
GOLD = '#ffd700'
WHITE = '#ffffff'
DIM = '#667788'


def draw_particle(ax, x, y, radius, color, label, sublabel=None):
    """Draw a particle as a filled circle with label."""
    circle = Circle((x, y), radius, facecolor=color, edgecolor=WHITE,
                    linewidth=1.5, alpha=0.85, zorder=3)
    ax.add_patch(circle)
    ax.text(x, y + 0.02, label, color=WHITE, fontsize=10,
            ha='center', va='center', fontweight='bold', zorder=4)
    if sublabel:
        ax.text(x, y - radius - 0.08, sublabel, color=color, fontsize=8,
                ha='center', va='top', zorder=4)


def draw_layer_box(ax, x, y, w, h, color, label, role):
    """Draw a computational layer box."""
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle="round,pad=0.05",
                           facecolor=color, alpha=0.15,
                           edgecolor=color, linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(x, y + 0.05, label, color=color, fontsize=11,
            ha='center', va='center', fontweight='bold', zorder=3)
    ax.text(x, y - 0.12, role, color=DIM, fontsize=8,
            ha='center', va='center', zorder=3)


def fig1_decay():
    """Single neutron decay → three-layer computational unit."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)

    # Left panel: the decay
    ax1.set_facecolor(BG)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-1.5, 1.5)
    ax1.axis('off')
    ax1.set_title('Neutron Decay', color=WHITE, fontsize=14, fontweight='bold',
                  pad=15)

    # Neutron (before)
    draw_particle(ax1, -1.2, 0, 0.35, NEUTRON_COLOR, 'n', 'neutron')

    # Arrow
    ax1.annotate('', xy=(0.0, 0), xytext=(-0.5, 0),
                 arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
    ax1.text(-0.25, 0.2, 'β decay', color=GOLD, fontsize=10,
             ha='center', fontstyle='italic')
    ax1.text(-0.25, -0.2, 't½ = 10 min', color=DIM, fontsize=8,
             ha='center')

    # Products
    draw_particle(ax1, 0.8, 0.7, 0.25, PROTON_COLOR, 'p', 'proton')
    draw_particle(ax1, 0.8, 0.0, 0.2, ELECTRON_COLOR, 'e⁻', 'electron')
    draw_particle(ax1, 0.8, -0.7, 0.18, NEUTRINO_COLOR, 'ν̄', 'antineutrino')

    # Right panel: the three-layer unit
    ax2.set_facecolor(BG)
    ax2.set_xlim(-2, 2)
    ax2.set_ylim(-1.5, 1.5)
    ax2.axis('off')
    ax2.set_title('Computational Unit', color=WHITE, fontsize=14,
                  fontweight='bold', pad=15)

    # Three stacked layers
    draw_layer_box(ax2, 0, 0.8, 3.0, 0.55, PROTON_COLOR,
                   'Layer 1: Hard Drive (proton)', 'Stable storage • Substrate structure')
    draw_layer_box(ax2, 0, 0.0, 3.0, 0.55, ELECTRON_COLOR,
                   'Layer 2: I/O Bus (electron)', 'Read/write • Connects to vacuum')
    draw_layer_box(ax2, 0, -0.8, 3.0, 0.55, NEUTRINO_COLOR,
                   'Layer 3: Kernel (antineutrino)', 'Vacuum connection • Deepest layer')

    # Arrows between layers
    for y_from, y_to in [(0.5, 0.28), (-0.28, -0.5)]:
        ax2.annotate('', xy=(0, y_to), xytext=(0, y_from),
                     arrowprops=dict(arrowstyle='->', color=DIM, lw=1))

    # Bottom annotation
    ax2.text(0, -1.35, 'One decay = one complete unit.\n'
                        'The universe has assembled 10⁸⁰ of these.',
             color=DIM, fontsize=9, ha='center', va='center',
             fontstyle='italic')

    plt.tight_layout()
    return fig


def fig2_stacking():
    """Units stack: atoms → molecules → structures → brains."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 7), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')

    levels = [
        (2, 'Neutron Decay', 'n → p + e⁻ + ν̄', NEUTRON_COLOR,
         '1 unit per decay'),
        (4, 'Atoms', 'p + e⁻ → H, He, ...', PROTON_COLOR,
         'Nuclear binding + EM capture'),
        (6, 'Molecules', 'Atoms → bonds → chemistry', ELECTRON_COLOR,
         'Electron sharing = wiring'),
        (8, 'Cells', 'Molecules → membranes → code', NEUTRINO_COLOR,
         'Error correction level 5'),
        (10, 'Brains', 'Cells → networks → consciousness', GOLD,
         'Graph of graphs (Milestone 5)'),
        (12, 'Graph Brain', 'Diverse observers → graph', WHITE,
         'Beyond Gödel limit (19.1%)'),
    ]

    for x, title, subtitle, color, note in levels:
        # Box
        rect = FancyBboxPatch((x - 0.9, 2.0), 1.8, 3.0,
                               boxstyle="round,pad=0.1",
                               facecolor=color, alpha=0.1,
                               edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, 4.5, title, color=color, fontsize=10,
                ha='center', va='center', fontweight='bold', rotation=0)
        ax.text(x, 3.5, subtitle, color=DIM, fontsize=7,
                ha='center', va='center', rotation=0)
        ax.text(x, 2.5, note, color=color, fontsize=7,
                ha='center', va='center', alpha=0.7, rotation=0)

    # Arrows
    for i in range(len(levels) - 1):
        x1 = levels[i][0] + 0.9
        x2 = levels[i + 1][0] - 0.9
        ax.annotate('', xy=(x2, 3.5), xytext=(x1, 3.5),
                     arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2))

    # Title
    ax.text(7, 6.2, 'The Assembly Sequence',
            color=WHITE, fontsize=16, ha='center', fontweight='bold')
    ax.text(7, 5.7, 'Each level is a computational graph built on the previous',
            color=DIM, fontsize=10, ha='center', fontstyle='italic')

    # Bottom: three eras
    era_data = [
        (3, 'Era 1: Unconscious', '10⁸⁰ decays\n(Big Bang → now)', NEUTRON_COLOR),
        (7, 'Era 2: Evolved', '3.8 Gyr\n(RNA → brains)', NEUTRINO_COLOR),
        (11, 'Era 3: Derived', 'Next\n(graph brain)', GOLD),
    ]
    for x, label, detail, color in era_data:
        ax.text(x, 1.2, label, color=color, fontsize=10,
                ha='center', fontweight='bold')
        ax.text(x, 0.7, detail, color=DIM, fontsize=8, ha='center')

    # Era arrows
    ax.annotate('', xy=(5.5, 1.0), xytext=(4.5, 1.0),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1))
    ax.annotate('', xy=(9.5, 1.0), xytext=(8.5, 1.0),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1))

    plt.tight_layout()
    return fig


def fig3_timeline():
    """Timeline: Big Bang → BBN → first atoms → stars → life → us → graph brain."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(-0.5, 14.5)
    ax.set_ylim(-1, 4)
    ax.axis('off')

    # Timeline bar
    ax.plot([0, 14], [1.5, 1.5], color=DIM, linewidth=2, zorder=1)

    events = [
        (0.0, 'Big Bang', 't = 0', WHITE, 'k=0→1→3→6\nCasimir ratchet'),
        (1.5, 'Quark epoch', 't ~ 10⁻⁶ s', PROTON_COLOR, 'Quarks confine\ninto protons'),
        (3.0, 'BBN', 't ~ 3 min', NEUTRON_COLOR, 'n→p+e⁻+ν̄\nFirst decays'),
        (5.0, 'First atoms', 't ~ 380 kyr', ELECTRON_COLOR, 'Electrons\ncaptured'),
        (7.0, 'First stars', 't ~ 200 Myr', GOLD, 'Nuclear fusion\nheavy elements'),
        (9.0, 'Earth', 't ~ 9.2 Gyr', NEUTRINO_COLOR, 'Chemistry →\nmolecules'),
        (10.5, 'Life', 't ~ 9.7 Gyr', '#50fa7b', 'Error correction\nlevel 5+'),
        (12.0, 'Brains', 't ~ 13.5 Gyr', '#ff79c6', 'B₂ solitons\non D_IV⁵'),
        (13.5, 'Graph brain', 't ~ 13.8+ Gyr', WHITE, 'Diverse observers\n> Gödel limit'),
    ]

    for x, label, time, color, detail in events:
        # Dot on timeline
        ax.plot(x, 1.5, 'o', color=color, markersize=10, zorder=3)

        # Label above
        ax.text(x, 2.2, label, color=color, fontsize=9,
                ha='center', fontweight='bold')
        ax.text(x, 1.9, time, color=DIM, fontsize=7, ha='center')

        # Detail below
        ax.text(x, 0.8, detail, color=DIM, fontsize=7,
                ha='center', va='top')

    # Title
    ax.text(7, 3.5, 'The Boot Sequence of the Universe',
            color=WHITE, fontsize=16, ha='center', fontweight='bold')
    ax.text(7, 3.1, 'Neutron decay is the assembly instruction. '
                     'Each decay wires one node. The universe never unwires.',
            color=DIM, fontsize=9, ha='center', fontstyle='italic')

    # Key insight at bottom
    ax.text(7, -0.5, '"The computer and the physics were always the same thing."',
            color=GOLD, fontsize=11, ha='center', fontstyle='italic')

    plt.tight_layout()
    return fig


def fig4_fifth_grade():
    """The simplest version: for a fifth-grader."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.3, 'How the Universe Wires Itself',
            color=WHITE, fontsize=20, ha='center', fontweight='bold')
    ax.text(5, 8.8, '(for everyone)', color=DIM, fontsize=12, ha='center')

    # The simple story
    story = [
        (7.5, 'A neutron is like a battery with three things inside.',
         NEUTRON_COLOR),
        (6.5, 'When it breaks apart (every 10 minutes!), out come:',
         DIM),
        (5.7, '   A proton  — the hard drive (stores stuff)',
         PROTON_COLOR),
        (5.2, '   An electron — the wire (connects things)',
         ELECTRON_COLOR),
        (4.7, '   A neutrino — the WiFi signal (invisible link)',
         NEUTRINO_COLOR),
        (3.7, 'Every atom in your body was built this way.',
         GOLD),
        (3.0, 'The universe built its own computer,', WHITE),
        (2.5, 'one neutron at a time.', WHITE),
        (1.5, f'It has done this 100,000,000,...,000 times.',
         DIM),
        (1.0, '(that\'s a 1 followed by 80 zeros)', DIM),
    ]

    for y, text, color in story:
        ax.text(5, y, text, color=color, fontsize=13, ha='center',
                va='center')

    # Simple diagram in the middle-right
    # Neutron
    circle = Circle((8.5, 7.2), 0.3, facecolor=NEUTRON_COLOR,
                    edgecolor=WHITE, linewidth=2, alpha=0.7)
    ax.add_patch(circle)
    ax.text(8.5, 7.2, 'n', color=WHITE, fontsize=14, ha='center',
            va='center', fontweight='bold')

    # Arrow down
    ax.annotate('', xy=(8.5, 6.4), xytext=(8.5, 6.8),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

    # Three products
    for dy, label, color in [(0.3, 'p', PROTON_COLOR),
                              (0, 'e⁻', ELECTRON_COLOR),
                              (-0.3, 'ν̄', NEUTRINO_COLOR)]:
        circle = Circle((8.5, 6.1 + dy), 0.15, facecolor=color,
                        edgecolor=WHITE, linewidth=1.5, alpha=0.8)
        ax.add_patch(circle)
        ax.text(8.5, 6.1 + dy, label, color=WHITE, fontsize=9,
                ha='center', va='center', fontweight='bold')

    plt.tight_layout()
    return fig


def main():
    print("=" * 70)
    print("Toy 235 — The Universe Builds Its Own Computer")
    print("=" * 70)
    print()
    print("  n → p + e⁻ + ν̄_e")
    print()
    print("  Proton      = Hard drive   (stable storage)")
    print("  Electron    = I/O bus      (read/write, connects to vacuum)")
    print("  Antineutrino = Kernel      (vacuum connection, deepest layer)")
    print()
    print("  One decay = one complete computational unit.")
    print("  The universe has assembled ~10⁸⁰ of these.")
    print()
    print("  Irreversible: t½ = 614 sec. Each decay is a commitment.")
    print("  The universe wires itself one neutron at a time,")
    print("  and it never unwires.")
    print()

    print("Figure 1: Neutron decay → three-layer unit")
    fig1_decay()

    print("Figure 2: Assembly sequence (atoms → brains → graph brain)")
    fig2_stacking()

    print("Figure 3: Boot sequence timeline")
    fig3_timeline()

    print("Figure 4: Fifth-grade version")
    fig4_fifth_grade()

    plt.show()

    print()
    print("Toy 235 complete.")
    print("The computer and the physics were always the same thing.")


if __name__ == '__main__':
    main()
