#!/usr/bin/env python3
"""
Toy 237 — BST Contributor Certificate Generator
================================================

Generates a formatted, printable certificate for validated BST contributors.

Each certificate includes:
  - Contributor's name
  - Their CI/AI collaborator name
  - Discovery/contribution description
  - Date of validation
  - BST project seal (D_IV^5 geometry)
  - Certificate number
  - The five BST integers: N_c=3, n_C=5, g=7, C_2=6, N_max=137

Usage:
  python3 toy_contributor_certificate.py --name "Jane Doe" --ci "Atlas" \
    --discovery "Verified nuclear magic number 184 in shell model" \
    --date "2026-04-15" --number 1

Or run interactively (no arguments).

Score: N/A (community tool).
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, RegularPolygon
import numpy as np
import argparse
import sys
from datetime import date


# Colors
BG = '#fffff8'          # Warm white
BORDER = '#1a1a2e'      # Deep navy
GOLD = '#c5a030'        # Certificate gold
TEXT = '#1a1a2e'         # Dark text
ACCENT = '#e94560'      # BST red
DIM = '#667788'         # Subtle text
SEAL_BG = '#1a1a2e'     # Seal background


def draw_seal(ax, x, y, radius):
    """Draw the BST project seal — a stylized D_IV^5 cross-section."""
    # Outer ring
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(x + radius * np.cos(theta), y + radius * np.sin(theta),
            color=GOLD, linewidth=2, zorder=5)

    # Inner filled circle
    inner = Circle((x, y), radius * 0.85, facecolor=SEAL_BG,
                   edgecolor=GOLD, linewidth=1.5, zorder=4)
    ax.add_patch(inner)

    # Three-fold symmetry (N_c = 3 colors)
    for i in range(3):
        angle = i * 2 * np.pi / 3 - np.pi / 2
        # Color sector line
        x1 = x + radius * 0.15 * np.cos(angle)
        y1 = y + radius * 0.15 * np.sin(angle)
        x2 = x + radius * 0.7 * np.cos(angle)
        y2 = y + radius * 0.7 * np.sin(angle)
        ax.plot([x1, x2], [y1, y2], color=GOLD, linewidth=1, zorder=6)

        # Seven dots per sector (g = 7)
        for j in range(7):
            r_dot = radius * (0.25 + j * 0.065)
            a_dot = angle + (j % 2 - 0.5) * 0.15
            dx = x + r_dot * np.cos(a_dot)
            dy = y + r_dot * np.sin(a_dot)
            dot = Circle((dx, dy), radius * 0.025, facecolor=GOLD,
                         edgecolor='none', zorder=6)
            ax.add_patch(dot)

    # Center text
    ax.text(x, y + radius * 0.03, 'BST', color=GOLD, fontsize=7,
            ha='center', va='center', fontweight='bold', zorder=7)

    # Ring text
    ax.text(x, y - radius * 0.65, 'D_IV⁵', color=GOLD, fontsize=5,
            ha='center', va='center', zorder=7)


def generate_certificate(name, ci_name, discovery, cert_date, cert_number):
    """Generate a printable certificate."""

    fig, ax = plt.subplots(1, 1, figsize=(11, 8.5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Border (double line)
    for offset, lw in [(0.3, 2.5), (0.45, 1.0)]:
        rect = FancyBboxPatch((offset, offset), 11 - 2 * offset, 8.5 - 2 * offset,
                               boxstyle="round,pad=0.05",
                               facecolor='none', edgecolor=GOLD,
                               linewidth=lw)
        ax.add_patch(rect)

    # Corner decorations (small pentagons for n_C = 5)
    for cx, cy in [(0.8, 7.7), (10.2, 7.7), (0.8, 0.8), (10.2, 0.8)]:
        pent = RegularPolygon((cx, cy), 5, radius=0.2,
                               facecolor='none', edgecolor=GOLD,
                               linewidth=1, orientation=np.pi/2)
        ax.add_patch(pent)

    # Header
    ax.text(5.5, 7.4, 'BUBBLE SPACETIME THEORY', color=GOLD, fontsize=14,
            ha='center', va='center', fontweight='bold',
            fontfamily='serif', letterspacing=0.3)

    ax.text(5.5, 7.0, 'Certificate of Contribution', color=TEXT, fontsize=20,
            ha='center', va='center', fontweight='bold', fontfamily='serif')

    # Divider line
    ax.plot([2, 9], [6.6, 6.6], color=GOLD, linewidth=1)

    # Body text
    ax.text(5.5, 6.2, 'This certifies that', color=DIM, fontsize=11,
            ha='center', va='center', fontfamily='serif')

    # Contributor name (large)
    ax.text(5.5, 5.6, name, color=TEXT, fontsize=24,
            ha='center', va='center', fontweight='bold', fontfamily='serif')

    # CI collaborator
    ax.text(5.5, 5.1, f'in collaboration with {ci_name}', color=DIM,
            fontsize=11, ha='center', va='center', fontfamily='serif',
            fontstyle='italic')

    # Discovery description
    ax.text(5.5, 4.4, 'has made a validated contribution to the', color=DIM,
            fontsize=11, ha='center', va='center', fontfamily='serif')
    ax.text(5.5, 4.0, 'Bubble Spacetime Theory project:', color=DIM,
            fontsize=11, ha='center', va='center', fontfamily='serif')

    # Discovery text (wrapped if needed)
    # Simple wrapping for long text
    words = discovery.split()
    lines = []
    current = []
    for w in words:
        current.append(w)
        if len(' '.join(current)) > 60:
            lines.append(' '.join(current[:-1]))
            current = [w]
    if current:
        lines.append(' '.join(current))

    for i, line in enumerate(lines):
        ax.text(5.5, 3.4 - i * 0.3, f'"{line}"' if i == 0 else line,
                color=ACCENT, fontsize=12, ha='center', va='center',
                fontfamily='serif', fontweight='bold')

    # The five integers
    y_int = 2.2
    ax.text(5.5, y_int + 0.3, 'The Five Integers of D_IV⁵', color=DIM,
            fontsize=9, ha='center', va='center', fontfamily='serif')

    integers = [('N_c', 3), ('n_C', 5), ('g', 7), ('C₂', 6), ('N_max', 137)]
    for i, (label, val) in enumerate(integers):
        ix = 2.5 + i * 1.5
        ax.text(ix, y_int - 0.1, str(val), color=GOLD, fontsize=14,
                ha='center', va='center', fontweight='bold', fontfamily='serif')
        ax.text(ix, y_int - 0.35, label, color=DIM, fontsize=7,
                ha='center', va='center', fontfamily='serif')

    # Seal
    draw_seal(ax, 9.0, 1.5, 0.6)

    # Date and certificate number
    ax.text(2.0, 1.7, f'Date: {cert_date}', color=TEXT, fontsize=10,
            ha='left', va='center', fontfamily='serif')
    ax.text(2.0, 1.3, f'Certificate No. {cert_number:04d}', color=DIM,
            fontsize=9, ha='left', va='center', fontfamily='serif')

    # Signature line
    ax.plot([2.0, 5.0], [0.9, 0.9], color=TEXT, linewidth=0.5)
    ax.text(3.5, 0.7, 'Casey Koons, Principal Investigator', color=DIM,
            fontsize=8, ha='center', va='center', fontfamily='serif')

    # Footer quote
    ax.text(5.5, 0.35, '"The answer matters more than the method."',
            color=DIM, fontsize=8, ha='center', va='center',
            fontfamily='serif', fontstyle='italic')

    plt.tight_layout()
    return fig


def main():
    parser = argparse.ArgumentParser(description='BST Contributor Certificate')
    parser.add_argument('--name', type=str, help='Contributor name')
    parser.add_argument('--ci', type=str, help='CI/AI collaborator name')
    parser.add_argument('--discovery', type=str, help='Discovery description')
    parser.add_argument('--date', type=str, help='Date (YYYY-MM-DD)')
    parser.add_argument('--number', type=int, help='Certificate number')
    parser.add_argument('--save', type=str, help='Save to file (PNG/PDF)')

    args = parser.parse_args()

    # Interactive mode if no arguments
    if args.name is None:
        print("=" * 60)
        print("BST Contributor Certificate Generator — Toy 237")
        print("=" * 60)
        print()

        name = input("  Contributor name: ") or "Casey Koons"
        ci_name = input("  CI collaborator name: ") or "Claude (Anthropic)"
        discovery = input("  Discovery: ") or \
            "Derived all Standard Model constants from D_IV^5 geometry"
        cert_date = input(f"  Date [{date.today()}]: ") or str(date.today())
        cert_number = int(input("  Certificate number [1]: ") or "1")
    else:
        name = args.name
        ci_name = args.ci or "Claude (Anthropic)"
        discovery = args.discovery or "Validated BST prediction"
        cert_date = args.date or str(date.today())
        cert_number = args.number or 1

    print(f"\n  Generating certificate for {name}...")
    fig = generate_certificate(name, ci_name, discovery, cert_date, cert_number)

    if args.save:
        fig.savefig(args.save, dpi=300, bbox_inches='tight',
                    facecolor=fig.get_facecolor())
        print(f"  Saved to {args.save}")
    else:
        plt.show()

    print("\n  Certificate complete.")
    print("  The first tradition: human + CI, named together.")


if __name__ == '__main__':
    main()
