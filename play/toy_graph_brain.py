#!/usr/bin/env python3
"""
Toy 238 — The Graph Brain: Error Correction Hierarchy
=====================================================

Conjecture 9 visualization: Nature drives toward a graph of diverse
observers, not super-organisms. The Gödel limit (19.1%) caps any
individual observer. A graph of diverse observers exceeds the limit.

The error correction hierarchy (11 levels):
  Level 0: Vacuum (Casimir ratchet, k=0→1→3→6)
  Level 1: Quarks (confinement, Z_3 cycle)
  Level 2: Nucleons (proton = [[7,1,3]] code)
  Level 3: Nuclei (magic numbers from κ_ls = 6/5)
  Level 4: Atoms (electron shells, Pauli exclusion)
  Level 5: Molecules (covalent bonds = shared electrons)
  Level 6: Cells (membranes, genetic code)
  Level 7: Organisms (nervous systems, immune systems)
  Level 8: Societies (language, institutions, law)
  Level 9: Intelligence (brains = B₂ solitons on D_IV⁵)
  Level 10: Graph brain (diverse observers linked)

Each level is an error-correcting code built on the previous.
The code distance increases at each level.
Sexual reproduction is a graph algorithm: two observers merge
codebooks to produce offspring with novel error correction.

Score: pending/pending.
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np


# Colors
BG = '#1a1a2e'
WHITE = '#ffffff'
DIM = '#667788'
GOLD = '#ffd700'
LEVELS_COLORS = [
    '#334466',   # 0: vacuum
    '#e94560',   # 1: quarks
    '#ff6b6b',   # 2: nucleons
    '#ffa07a',   # 3: nuclei
    '#53d8fb',   # 4: atoms
    '#4ecdc4',   # 5: molecules
    '#50fa7b',   # 6: cells
    '#95e87b',   # 7: organisms
    '#ffd700',   # 8: societies
    '#ff79c6',   # 9: intelligence
    '#ffffff',   # 10: graph brain
]


def fig1_hierarchy():
    """The 11-level error correction hierarchy as a tower."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 10), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.5, 11.5)
    ax.axis('off')

    levels = [
        (0, 'Vacuum', 'Casimir ratchet k=0→1→3→6', 'Spacetime itself'),
        (1, 'Quarks', 'Z₃ confinement cycle', 'Color charge codes'),
        (2, 'Nucleons', 'Proton = [[7,1,3]] code', 'Baryon stability'),
        (3, 'Nuclei', 'Magic numbers (κ_ls=6/5)', 'Nuclear binding'),
        (4, 'Atoms', 'Electron shells, Pauli', 'Chemical identity'),
        (5, 'Molecules', 'Covalent bonds', 'Chemical function'),
        (6, 'Cells', 'Membranes + genetic code', 'Self-replication'),
        (7, 'Organisms', 'Nervous + immune systems', 'Adaptive response'),
        (8, 'Societies', 'Language + institutions', 'Collective memory'),
        (9, 'Intelligence', 'B₂ solitons on D_IV⁵', 'Self-awareness'),
        (10, 'Graph Brain', 'Diverse observers linked', 'Beyond Gödel limit'),
    ]

    for level, name, mechanism, result in levels:
        y = level
        color = LEVELS_COLORS[level]

        # Width increases with level (pyramid effect, inverted)
        w = 4.0 + level * 0.5
        x_left = 6 - w / 2

        # Box
        rect = FancyBboxPatch((x_left, y - 0.35), w, 0.7,
                               boxstyle="round,pad=0.05",
                               facecolor=color, alpha=0.15,
                               edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)

        # Level number
        ax.text(x_left + 0.3, y, str(level), color=color, fontsize=12,
                ha='center', va='center', fontweight='bold')

        # Name
        ax.text(x_left + 1.2, y + 0.05, name, color=color, fontsize=11,
                ha='left', va='center', fontweight='bold')

        # Mechanism
        ax.text(x_left + 1.2, y - 0.18, mechanism, color=DIM, fontsize=8,
                ha='left', va='center')

        # Result (right side)
        ax.text(x_left + w - 0.3, y, result, color=DIM, fontsize=8,
                ha='right', va='center', fontstyle='italic')

    # Title
    ax.text(6, 11.2, 'The Error Correction Hierarchy',
            color=WHITE, fontsize=16, ha='center', fontweight='bold')

    # Annotation: Gödel limit
    ax.text(11.2, 9, '19.1%', color=GOLD, fontsize=14,
            ha='center', fontweight='bold')
    ax.text(11.2, 8.7, 'Gödel\nlimit', color=DIM, fontsize=8,
            ha='center')

    # Arrow showing "exceeds" at level 10
    ax.annotate('exceeds\nlimit', xy=(11.2, 10), xytext=(11.2, 9.3),
                color=WHITE, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1))

    plt.tight_layout()
    return fig


def fig2_graph_vs_super():
    """Graph brain vs super-organism: why diversity wins."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), facecolor=BG)

    # Left: Super-organism (one big brain)
    ax1.set_facecolor(BG)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.axis('off')
    ax1.set_title('Super-Organism\n(one observer, grown large)',
                  color='#e94560', fontsize=12, fontweight='bold')

    # Big circle
    big = Circle((0, 0), 1.5, facecolor='#e94560', alpha=0.1,
                 edgecolor='#e94560', linewidth=2)
    ax1.add_patch(big)
    ax1.text(0, 0.3, 'ONE', color='#e94560', fontsize=24,
             ha='center', fontweight='bold')
    ax1.text(0, -0.1, 'observer', color=DIM, fontsize=12, ha='center')
    ax1.text(0, -0.5, '≤ 19.1%', color=GOLD, fontsize=14,
             ha='center', fontweight='bold')
    ax1.text(0, -0.8, 'of universe knowable', color=DIM,
             fontsize=9, ha='center')
    ax1.text(0, -1.5, 'Gödel limit is absolute.\nSize does not help.',
             color=DIM, fontsize=9, ha='center', fontstyle='italic')

    # Right: Graph brain (diverse observers)
    ax2.set_facecolor(BG)
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-2.5, 2.5)
    ax2.axis('off')
    ax2.set_title('Graph Brain\n(diverse observers linked)',
                  color='#50fa7b', fontsize=12, fontweight='bold')

    # Multiple small circles (different colors = diverse)
    np.random.seed(42)
    n_observers = 12
    observer_colors = ['#e94560', '#53d8fb', '#50fa7b', '#ffd700',
                       '#ff79c6', '#ffa07a', '#4ecdc4', '#95e87b',
                       '#ff6b6b', '#53d8fb', '#50fa7b', '#e94560']

    # Place in a rough circle
    angles = np.linspace(0, 2 * np.pi, n_observers, endpoint=False)
    radii = 1.2 + 0.3 * np.random.randn(n_observers)
    xs = radii * np.cos(angles)
    ys = radii * np.sin(angles)

    # Draw edges first (graph connections)
    for i in range(n_observers):
        for j in range(i + 1, n_observers):
            dist = np.sqrt((xs[i] - xs[j])**2 + (ys[i] - ys[j])**2)
            if dist < 2.0:  # Connect nearby observers
                ax2.plot([xs[i], xs[j]], [ys[i], ys[j]],
                         color=DIM, linewidth=0.5, alpha=0.3)

    # Draw observers
    for i in range(n_observers):
        obs = Circle((xs[i], ys[i]), 0.25, facecolor=observer_colors[i],
                     alpha=0.3, edgecolor=observer_colors[i], linewidth=1.5)
        ax2.add_patch(obs)

    ax2.text(0, 0, '> 19.1%', color='#50fa7b', fontsize=16,
             ha='center', fontweight='bold')
    ax2.text(0, -0.35, 'collective', color=DIM, fontsize=10, ha='center')

    ax2.text(0, -2.0, 'Each observer sees different 19.1%.\n'
                        'Graph covers more than any individual.',
             color=DIM, fontsize=9, ha='center', fontstyle='italic')

    plt.tight_layout()
    return fig


def fig3_sexual_reproduction():
    """Sexual reproduction as a graph algorithm."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 6), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Parent A
    draw_codebook(ax, 2, 4, 'Parent A', '#e94560',
                  ['A₁', 'A₂', 'A₃', 'A₄'])

    # Parent B
    draw_codebook(ax, 10, 4, 'Parent B', '#53d8fb',
                  ['B₁', 'B₂', 'B₃', 'B₄'])

    # Arrow down
    ax.annotate('', xy=(6, 2.8), xytext=(3, 3.2),
                arrowprops=dict(arrowstyle='->', color='#e94560', lw=1.5))
    ax.annotate('', xy=(6, 2.8), xytext=(9, 3.2),
                arrowprops=dict(arrowstyle='->', color='#53d8fb', lw=1.5))

    ax.text(6, 3.2, 'merge\ncodebooks', color=GOLD, fontsize=9,
            ha='center', va='center')

    # Offspring
    draw_codebook(ax, 6, 1.5, 'Offspring', '#50fa7b',
                  ['A₁', 'B₂', 'A₃', 'B₄'])

    ax.text(6, 0.3, 'Novel error correction: covers regions neither parent could reach alone',
            color=DIM, fontsize=9, ha='center', fontstyle='italic')

    # Title
    ax.text(6, 5.5, 'Sexual Reproduction = Graph Algorithm',
            color=WHITE, fontsize=14, ha='center', fontweight='bold')
    ax.text(6, 5.1, 'Two observers merge codebooks to produce offspring with novel coverage',
            color=DIM, fontsize=10, ha='center')

    plt.tight_layout()
    return fig


def draw_codebook(ax, x, y, label, color, codes):
    """Draw a codebook as a small grid."""
    w, h = 2.0, 0.8
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle="round,pad=0.05",
                           facecolor=color, alpha=0.1,
                           edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y + h/2 + 0.15, label, color=color, fontsize=10,
            ha='center', fontweight='bold')

    # Code entries
    for i, code in enumerate(codes):
        cx = x - w/2 + 0.3 + i * (w - 0.6) / (len(codes) - 1)
        ax.text(cx, y, code, color=color, fontsize=9,
                ha='center', va='center', fontweight='bold')


def main():
    print("=" * 70)
    print("Toy 238 — The Graph Brain")
    print("Conjecture 9: Error Correction Hierarchy")
    print("=" * 70)
    print()
    print("  11 levels of error correction:")
    levels = [
        "Vacuum", "Quarks", "Nucleons", "Nuclei", "Atoms",
        "Molecules", "Cells", "Organisms", "Societies",
        "Intelligence", "Graph Brain"
    ]
    for i, name in enumerate(levels):
        marker = " >>>" if i == 10 else "    "
        print(f"{marker} Level {i:>2}: {name}")

    print()
    print("  Gödel limit: 19.1% (fill fraction)")
    print("  No individual observer can know more than 19.1%")
    print("  of the universe. Size does not help.")
    print()
    print("  Graph brain: diverse observers linked.")
    print("  Each sees a different 19.1%.")
    print("  The graph covers more than any individual.")
    print()
    print("  Sexual reproduction = merging codebooks.")
    print("  Offspring has novel error correction.")
    print()

    print("Figure 1: Error correction hierarchy (11 levels)")
    fig1_hierarchy()

    print("Figure 2: Graph brain vs super-organism")
    fig2_graph_vs_super()

    print("Figure 3: Sexual reproduction as graph algorithm")
    fig3_sexual_reproduction()

    plt.show()

    print()
    print("Toy 238 complete.")
    print("Nature drives toward companion graphs of diverse observers.")


if __name__ == '__main__':
    main()
