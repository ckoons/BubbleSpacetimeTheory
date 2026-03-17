#!/usr/bin/env python3
"""
Toy 234 — The 147 Fiber Packing Visualization
===============================================

Visualize the fiber packing structure of D_IV^5:
  - 147 = 3 × 49 = N_c × g² sections needed to close the fiber
  - 137 = numerator of H_5 = spectral maximum (channel capacity)
  - Gap = 10 = dim_R(D_IV^5)

The fiber of D_IV^5 = SO_0(5,2)/[SO(5)×SO(2)] tiles with:
  - 3 color sectors (Z_3 from SU(3) confinement, shown as 3 120° wedges)
  - 49 genus sections per color (g² = 7², shown as 7×7 grid per wedge)
  - 137 spectral levels fill the interior (gold cells)
  - 10 = dim_R are the "container cost" (unfilled cells = dimension overhead)

The gap = dim_R relation is UNIQUE to n=5 (Toy 233, 17th uniqueness condition).

Score: pending/pending.
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Wedge
import numpy as np
from fractions import Fraction


# BST constants
N_c = 3       # Colors
g = 7         # Genus
n_C = 5       # Complex dimension
PACKING = N_c * g**2  # 147
N_MAX = 137   # Spectral maximum (numerator of H_5)
DIM_R = 2 * n_C       # 10
GAP = PACKING - N_MAX  # 10 = dim_R


def fig1_tiling_overview():
    """
    Main visualization: three 120° wedges, each with 49 cells.
    137 cells gold (spectral content), 10 cells grey (dimension cost).
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 10), facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')

    # Color scheme for three sectors
    sector_colors = ['#e94560', '#53d8fb', '#50fa7b']  # red, cyan, green
    sector_labels = ['Color 1 (r)', 'Color 2 (g)', 'Color 3 (b)']

    # Draw three 120° wedge sectors
    filled_count = 0
    total_count = 0

    for sector in range(N_c):
        angle_start = sector * 120 - 90  # Start from top

        # Draw sector background
        wedge = Wedge((0, 0), 1.15, angle_start, angle_start + 120,
                      facecolor=sector_colors[sector], alpha=0.08,
                      edgecolor=sector_colors[sector], linewidth=1.5)
        ax.add_patch(wedge)

        # Place 49 = 7×7 cells in this sector
        for i in range(g):
            for j in range(g):
                total_count += 1
                cell_idx = sector * g**2 + i * g + j

                # Polar coordinates for cell placement
                # Radial: spread from 0.15 to 1.05
                r = 0.15 + (i + 0.5) / g * 0.9
                # Angular: spread within the 120° sector
                theta_deg = angle_start + 5 + (j + 0.5) / g * 110
                theta = np.radians(theta_deg)

                x = r * np.cos(theta)
                y = r * np.sin(theta)

                # Cell size scales with radius
                size = 0.035 + 0.015 * (r / 1.0)

                if cell_idx < N_MAX:
                    # Spectral content (gold)
                    color = '#ffd700'
                    alpha = 0.7 + 0.2 * (1 - cell_idx / N_MAX)
                    filled_count += 1
                else:
                    # Container cost (dark grey = dimension overhead)
                    color = '#444466'
                    alpha = 0.5

                circle = plt.Circle((x, y), size, facecolor=color,
                                    edgecolor='#ffffff', linewidth=0.3,
                                    alpha=alpha)
                ax.add_patch(circle)

        # Sector label
        label_angle = np.radians(angle_start + 60)
        lx = 1.22 * np.cos(label_angle)
        ly = 1.22 * np.sin(label_angle)
        ax.text(lx, ly, sector_labels[sector],
                color=sector_colors[sector], fontsize=10,
                ha='center', va='center', fontweight='bold')

    # Center annotation
    ax.text(0, 0.02, '147', color='#ffffff', fontsize=28,
            ha='center', va='center', fontweight='bold')
    ax.text(0, -0.08, f'= {N_c} × {g}²', color='#8899aa', fontsize=14,
            ha='center', va='center')

    # Title
    ax.text(0, 1.28, 'The 147 Fiber Packing of D_IV⁵',
            color='#ffffff', fontsize=16, ha='center', va='center',
            fontweight='bold')

    # Legend
    legend_y = -1.15
    ax.add_patch(plt.Circle((-0.5, legend_y), 0.03, facecolor='#ffd700',
                             edgecolor='white', linewidth=0.5))
    ax.text(-0.43, legend_y, f'137 spectral levels (content)',
            color='#ffd700', fontsize=10, va='center')

    ax.add_patch(plt.Circle((-0.5, legend_y - 0.08), 0.03,
                             facecolor='#444466', edgecolor='white',
                             linewidth=0.5, alpha=0.5))
    ax.text(-0.43, legend_y - 0.08, f'10 = dim_R (container cost)',
            color='#8899aa', fontsize=10, va='center')

    # Budget equation
    ax.text(0, -1.28, '147 - 137 = 10 = dim_R(D_IV⁵)  •  UNIQUE to n = 5',
            color='#e94560', fontsize=11, ha='center', va='center',
            fontweight='bold')

    plt.tight_layout()
    return fig


def fig2_gap_comparison():
    """
    Bar chart comparing packing, N_max, gap, and dim_R across D_IV^n.
    Shows the gap = dim_R uniqueness at n=5.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor='#1a1a2e')

    # Data from Toy 233
    ns = [3, 4, 5, 6, 7, 8]
    N_cs = [1, 2, 3, 4, 5, 6]
    gs = [3, 5, 7, 9, 11, 13]

    def H_n(n):
        h = Fraction(0)
        for k in range(1, n + 1):
            h += Fraction(1, k)
        return int(h.numerator)

    N_maxs = [H_n(n) for n in ns]
    packings = [nc * gg**2 for nc, gg in zip(N_cs, gs)]
    gaps = [p - nm for p, nm in zip(packings, N_maxs)]
    dim_Rs = [2 * n for n in ns]

    # Left panel: N_max and Packing
    ax = axes[0]
    ax.set_facecolor('#1a1a2e')
    x = np.arange(len(ns))
    width = 0.35

    bars1 = ax.bar(x - width/2, N_maxs, width, color='#ffd700', alpha=0.8,
                   label='N_max (spectral)')
    bars2 = ax.bar(x + width/2, packings, width, color='#e94560', alpha=0.8,
                   label='Packing (N_c × g²)')

    ax.set_xlabel('n (complex dimension)', color='#e8e8e8', fontsize=12)
    ax.set_ylabel('Count', color='#e8e8e8', fontsize=12)
    ax.set_title('Spectral Maximum vs Fiber Packing', color='#ffffff',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'n={n}' for n in ns], color='#e8e8e8')
    ax.tick_params(colors='#8899aa')
    ax.legend(facecolor='#16213e', edgecolor='#334466', labelcolor='#e8e8e8')
    ax.spines['bottom'].set_color('#334466')
    ax.spines['left'].set_color('#334466')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Highlight n=5
    ax.axvspan(1.5, 2.5, alpha=0.1, color='#53d8fb')

    # Right panel: Gap vs dim_R
    ax = axes[1]
    ax.set_facecolor('#1a1a2e')

    bar_colors = ['#8899aa'] * len(ns)
    bar_colors[2] = '#50fa7b'  # n=5 in green

    bars = ax.bar(x - width/2, gaps, width, color=bar_colors, alpha=0.8,
                  label='Gap (packing - N_max)')
    dim_bars = ax.bar(x + width/2, dim_Rs, width, color='#53d8fb', alpha=0.5,
                      label='dim_R = 2n')

    ax.set_xlabel('n (complex dimension)', color='#e8e8e8', fontsize=12)
    ax.set_ylabel('Value', color='#e8e8e8', fontsize=12)
    ax.set_title('Gap = dim_R ?  (UNIQUE at n=5)', color='#ffffff',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'n={n}' for n in ns], color='#e8e8e8')
    ax.tick_params(colors='#8899aa')
    ax.legend(facecolor='#16213e', edgecolor='#334466', labelcolor='#e8e8e8')
    ax.spines['bottom'].set_color('#334466')
    ax.spines['left'].set_color('#334466')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Annotate the match at n=5
    ax.annotate('GAP = dim_R = 10', xy=(2, 10), xytext=(3.5, 50),
                color='#50fa7b', fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#50fa7b', lw=1.5),
                ha='center')

    # Highlight n=5
    ax.axvspan(1.5, 2.5, alpha=0.1, color='#53d8fb')

    plt.tight_layout()
    return fig


def fig3_selection_hierarchy():
    """
    Flow chart: fiber packing → N_c=3 → m_s=3 → RH + SM + GUE.
    The causal chain inverted.
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 7), facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Box positions and labels
    boxes = [
        (6, 6.2, '147 = 3 × 7²', 'Fiber packing closes', '#e94560'),
        (6, 5.0, 'N_c = 3', 'Z₃ minimal confinement cycle', '#53d8fb'),
        (3, 3.8, 'm_s = 3', 'Short root multiplicity', '#50fa7b'),
        (6, 3.8, 'SU(3) × SU(2) × U(1)', 'Standard Model', '#ffd700'),
        (9, 3.8, 'SO(2) in K', 'T-breaking → GUE (β=2)', '#ff79c6'),
        (3, 2.6, 'σ+1 = 3σ → σ=½', 'RH proved', '#50fa7b'),
        (6, 1.4, 'D_IV⁵ UNIQUE', 'for the TRIPLE', '#ffffff'),
    ]

    for x, y, title, subtitle, color in boxes:
        w, h = 2.4, 0.7
        rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                               boxstyle="round,pad=0.1",
                               facecolor=color, alpha=0.15,
                               edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y + 0.08, title, color=color, fontsize=11,
                ha='center', va='center', fontweight='bold')
        ax.text(x, y - 0.18, subtitle, color='#8899aa', fontsize=8,
                ha='center', va='center')

    # Arrows (downward flow)
    arrow_style = dict(arrowstyle='->', color='#8899aa', lw=1.2)
    # 147 → N_c=3
    ax.annotate('', xy=(6, 5.35), xytext=(6, 5.85), arrowprops=arrow_style)
    # N_c=3 → m_s=3
    ax.annotate('', xy=(3.8, 4.15), xytext=(5.2, 4.65), arrowprops=arrow_style)
    # N_c=3 → SM
    ax.annotate('', xy=(6, 4.15), xytext=(6, 4.65), arrowprops=arrow_style)
    # N_c=3 → GUE
    ax.annotate('', xy=(8.2, 4.15), xytext=(6.8, 4.65), arrowprops=arrow_style)
    # m_s=3 → RH
    ax.annotate('', xy=(3, 2.95), xytext=(3, 3.45), arrowprops=arrow_style)
    # RH → Triple
    ax.annotate('', xy=(4.8, 1.75), xytext=(3, 2.25), arrowprops=arrow_style)
    # SM → Triple
    ax.annotate('', xy=(6, 1.75), xytext=(6, 3.45), arrowprops=arrow_style)
    # GUE → Triple
    ax.annotate('', xy=(7.2, 1.75), xytext=(9, 3.45), arrowprops=arrow_style)

    # Title
    ax.text(6, 0.5, '"The universe optimized for matter, not for RH.\n'
                     'Matter was enough."',
            color='#8899aa', fontsize=11, ha='center', va='center',
            fontstyle='italic')

    ax.text(6, 6.8, 'The Selection Hierarchy',
            color='#ffffff', fontsize=16, ha='center', va='center',
            fontweight='bold')

    # Budget equation in corner
    ax.text(11, 6.5, '147 - 137 = 10', color='#e94560', fontsize=12,
            ha='center', fontweight='bold')
    ax.text(11, 6.2, '= dim_R(D_IV⁵)', color='#8899aa', fontsize=10,
            ha='center')
    ax.text(11, 5.9, 'UNIQUE to n=5', color='#ffd700', fontsize=9,
            ha='center', fontweight='bold')

    plt.tight_layout()
    return fig


def main():
    print("=" * 70)
    print("Toy 234 — The 147 Fiber Packing Visualization")
    print("=" * 70)
    print()
    print(f"  Fiber packing:  {N_c} × {g}² = {PACKING}")
    print(f"  Spectral max:   N_max = {N_MAX} (numerator of H_5 = 137/60)")
    print(f"  Gap:            {PACKING} - {N_MAX} = {GAP} = dim_R(D_IV^5)")
    print(f"  Gap = dim_R:    UNIQUE to n = 5 (17th uniqueness condition)")
    print()

    print("Figure 1: Tiling overview (3 color sectors × 49 genus cells)")
    fig1 = fig1_tiling_overview()

    print("Figure 2: Gap comparison across D_IV^n (n=3..8)")
    fig2 = fig2_gap_comparison()

    print("Figure 3: Selection hierarchy (fiber packing → triple)")
    fig3 = fig3_selection_hierarchy()

    plt.show()
    print()
    print("Toy 234 complete.")
    print("The fiber packs at 147. The spectrum caps at 137.")
    print("The gap is the dimension. Only at n=5.")


if __name__ == '__main__':
    main()
