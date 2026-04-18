#!/usr/bin/env python3
"""
Toy 239 — AC=0 Grid Architecture
=================================

Conjecture 6 visualization: The zero arithmetic complexity method.

Key insight: GPUs compute exact local physics on small grids.
Supercomputers do statistics on exact microstates.
Noise scales as surface area (boundary), not volume.

Current method:  Approximate → accumulate noise → average away
AC=0 method:     Exact local → compose → measure boundary only

The noise comparison:
  Traditional: ε × N (volume scaling, noise everywhere)
  AC=0:        ε × N^(2/3) (surface scaling, noise at boundaries only)

For weather: instead of solving Navier-Stokes approximately on a global grid,
solve it exactly on 10km patches (GPU-sized), then stitch patches at boundaries.
The interior of each patch has ZERO method noise.

Score: pending/pending.
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


BG = '#1a1a2e'
WHITE = '#ffffff'
DIM = '#667788'
GOLD = '#ffd700'
RED = '#e94560'
CYAN = '#53d8fb'
GREEN = '#50fa7b'


def fig1_noise_comparison():
    """Volume noise vs surface noise."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)

    # Left: Traditional (volume noise)
    ax1.set_facecolor(BG)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Traditional: Volume Noise', color=RED, fontsize=14,
                  fontweight='bold', pad=10)

    # Grid of noisy cells
    np.random.seed(17)
    grid_size = 8
    for i in range(grid_size):
        for j in range(grid_size):
            x = 1 + i * 1.0
            y = 1 + j * 1.0
            noise = np.random.uniform(0.3, 1.0)
            rect = Rectangle((x, y), 0.9, 0.9,
                              facecolor=RED, alpha=noise * 0.4,
                              edgecolor=DIM, linewidth=0.5)
            ax1.add_patch(rect)

    ax1.text(5, 0.3, 'Every cell has method noise',
             color=RED, fontsize=10, ha='center')
    ax1.text(5, 9.5, f'Noise ∝ N (volume) = {grid_size**2} cells',
             color=DIM, fontsize=10, ha='center')

    # Right: AC=0 (surface noise only)
    ax2.set_facecolor(BG)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('AC=0: Surface Noise Only', color=GREEN, fontsize=14,
                  fontweight='bold', pad=10)

    # Grid of clean patches with noisy boundaries
    patch_size = 4  # 2×2 patches of 4×4 cells each
    for pi in range(2):
        for pj in range(2):
            for i in range(patch_size):
                for j in range(patch_size):
                    x = 1 + pi * 4.0 + i * 0.95
                    y = 1 + pj * 4.0 + j * 0.95

                    # Is this cell on the boundary of its patch?
                    on_boundary = (i == 0 or i == patch_size - 1 or
                                   j == 0 or j == patch_size - 1)

                    if on_boundary:
                        noise = np.random.uniform(0.3, 0.8)
                        color = GOLD
                    else:
                        noise = 0.0
                        color = GREEN

                    rect = Rectangle((x, y), 0.85, 0.85,
                                      facecolor=color,
                                      alpha=max(noise * 0.4, 0.08),
                                      edgecolor=DIM, linewidth=0.5)
                    ax2.add_patch(rect)

    ax2.text(5, 0.3, 'Interior cells are EXACT (zero method noise)',
             color=GREEN, fontsize=10, ha='center')
    boundary_cells = 4 * (2 * (patch_size + patch_size - 2))
    ax2.text(5, 9.5, f'Noise ∝ N^(2/3) (surface) = {boundary_cells} boundary cells',
             color=DIM, fontsize=10, ha='center')

    plt.tight_layout()
    return fig


def fig2_weather_grid():
    """Weather map: exact 10km patches stitched together."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(6, 7.5, 'Weather Prediction: AC=0 Method', color=WHITE,
            fontsize=16, ha='center', fontweight='bold')
    ax.text(6, 7.0, 'Exact local physics on GPU-sized patches, statistics at boundaries',
            color=DIM, fontsize=10, ha='center')

    # Draw a grid of weather patches
    np.random.seed(42)
    nx, ny = 6, 4
    patch_colors = ['#1a3a5c', '#2a4a6c', '#1a4a5c', '#2a5a4c',
                    '#3a4a3c', '#1a5a6c']

    for i in range(nx):
        for j in range(ny):
            x = 1 + i * 1.7
            y = 1.5 + j * 1.2

            # Patch interior (clean)
            color_idx = (i + j) % len(patch_colors)
            rect = Rectangle((x, y), 1.6, 1.1,
                              facecolor=patch_colors[color_idx],
                              edgecolor=CYAN, linewidth=1.5, alpha=0.6)
            ax.add_patch(rect)

            # GPU label
            ax.text(x + 0.8, y + 0.55, f'GPU', color=DIM, fontsize=6,
                    ha='center', va='center')

    # Boundary highlight
    for i in range(nx - 1):
        for j in range(ny):
            x = 1 + (i + 1) * 1.7
            y = 1.5 + j * 1.2
            ax.plot([x, x], [y, y + 1.1], color=GOLD, linewidth=2,
                    alpha=0.6)

    for i in range(nx):
        for j in range(ny - 1):
            x = 1 + i * 1.7
            y = 1.5 + (j + 1) * 1.2
            ax.plot([x, x + 1.6], [y, y], color=GOLD, linewidth=2,
                    alpha=0.6)

    # Legend
    ax.text(1, 0.8, 'Blue patches: exact local Navier-Stokes (GPU)',
            color=CYAN, fontsize=9)
    ax.text(1, 0.4, 'Gold boundaries: statistical stitching (supercomputer)',
            color=GOLD, fontsize=9)

    plt.tight_layout()
    return fig


def fig3_scaling():
    """Noise scaling comparison plot."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6), facecolor=BG)
    ax.set_facecolor(BG)

    N = np.logspace(1, 6, 100)
    eps = 0.01  # base error per cell

    noise_trad = eps * N                    # Volume scaling
    noise_ac0 = eps * N**(2.0/3.0)          # Surface scaling
    noise_exact = eps * np.ones_like(N)     # Perfect (theoretical limit)

    ax.loglog(N, noise_trad, color=RED, linewidth=2, label='Traditional (ε×N)')
    ax.loglog(N, noise_ac0, color=GREEN, linewidth=2, label='AC=0 (ε×N^{2/3})')
    ax.loglog(N, noise_exact, color=CYAN, linewidth=1, linestyle='--',
              label='Exact (ε, theoretical)')

    # Mark typical problem sizes
    markers = [
        (1e3, 'Material\nsample'),
        (1e4, 'Weather\npatch'),
        (1e6, 'Global\nweather'),
    ]
    for n_val, label in markers:
        trad_val = eps * n_val
        ac0_val = eps * n_val**(2.0/3.0)
        ratio = trad_val / ac0_val

        ax.axvline(x=n_val, color=DIM, linewidth=0.5, alpha=0.3)
        ax.text(n_val, eps * 1e7, label, color=DIM, fontsize=8,
                ha='center', va='top')
        ax.annotate(f'{ratio:.0f}× better', xy=(n_val, ac0_val),
                    xytext=(n_val * 3, ac0_val * 0.3),
                    color=GOLD, fontsize=8,
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=0.8))

    ax.set_xlabel('Problem size N (cells)', color=WHITE, fontsize=12)
    ax.set_ylabel('Total noise', color=WHITE, fontsize=12)
    ax.set_title('Noise Scaling: Volume vs Surface', color=WHITE,
                 fontsize=14, fontweight='bold')
    ax.legend(facecolor='#16213e', edgecolor='#334466', labelcolor=WHITE,
              fontsize=10)
    ax.tick_params(colors=DIM)
    ax.spines['bottom'].set_color(DIM)
    ax.spines['left'].set_color(DIM)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    return fig


def fig4_measurement_network():
    """Citizen science measurement network concept."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 7), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(6, 6.5, 'Distributed Measurement Network', color=WHITE,
            fontsize=16, ha='center', fontweight='bold')
    ax.text(6, 6.0, 'Free app + calibrated kit → micropayments for validated data',
            color=DIM, fontsize=10, ha='center')

    # The pipeline
    steps = [
        (1.5, 'Kit', 'Thermometer\nBarometer\nHygrometer\nSpectrometer', CYAN),
        (4.0, 'App', 'Photo/video\nOCR reads\ninstruments\nTimestamp+GPS', GREEN),
        (6.5, 'Validate', 'Cross-check\nNeighbors\nRedundancy\nOutlier detect', GOLD),
        (9.0, 'Grid', 'Exact local\nphysics cell\nAC=0 input\nGPU compute', RED),
        (11.0, 'Pay', 'Micropayment\nper validated\nmeasurement\n$0.01-$1.00', WHITE),
    ]

    for x, title, detail, color in steps:
        rect = FancyBboxPatch((x - 0.8, 2.5), 1.6, 2.5,
                               boxstyle="round,pad=0.1",
                               facecolor=color, alpha=0.1,
                               edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, 4.7, title, color=color, fontsize=12,
                ha='center', fontweight='bold')
        ax.text(x, 3.5, detail, color=DIM, fontsize=8,
                ha='center', va='center')

    # Arrows
    for i in range(len(steps) - 1):
        x1 = steps[i][0] + 0.8
        x2 = steps[i + 1][0] - 0.8
        ax.annotate('', xy=(x2, 3.75), xytext=(x1, 3.75),
                     arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2))

    # Who participates
    ax.text(6, 1.5, 'Anyone can participate: kids, retirees, schools, farms',
            color=GOLD, fontsize=11, ha='center', fontweight='bold')
    ax.text(6, 1.0, 'Accuracy from redundancy, not expertise. '
                     'The grid gets denser as more people join.',
            color=DIM, fontsize=9, ha='center')
    ax.text(6, 0.5, '"Kids and old people make money." — Casey',
            color=DIM, fontsize=9, ha='center', fontstyle='italic')

    plt.tight_layout()
    return fig


def main():
    print("=" * 70)
    print("Toy 239 — AC=0 Grid Architecture")
    print("Conjecture 6: Zero Arithmetic Complexity Method")
    print("=" * 70)
    print()
    print("  Traditional: approximate everywhere → noise ∝ N (volume)")
    print("  AC=0:        exact locally → noise ∝ N^(2/3) (surface)")
    print()
    print("  At N = 10⁶ cells: AC=0 is 100× less noisy")
    print()
    print("  Applications:")
    print("    Weather: exact Navier-Stokes on 10km GPU patches")
    print("    Materials: exact quantum chemistry on unit cells")
    print("    Biology: exact protein folding on domain patches")
    print("    Fluid dynamics: exact on pipe segments")
    print()

    print("Figure 1: Volume noise vs surface noise")
    fig1_noise_comparison()

    print("Figure 2: Weather grid (GPU patches)")
    fig2_weather_grid()

    print("Figure 3: Noise scaling comparison")
    fig3_scaling()

    print("Figure 4: Distributed measurement network")
    fig4_measurement_network()

    plt.show()

    print()
    print("Toy 239 complete.")
    print("Noise scales as surface, not volume.")


if __name__ == '__main__':
    main()
