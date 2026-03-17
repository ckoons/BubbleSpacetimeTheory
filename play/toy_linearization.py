#!/usr/bin/env python3
"""
Toy 240 — Linearization of "Complex" Systems
=============================================

Conjecture 7 visualization.

Key insight: Apparent nonlinearity in "complex" systems is METHOD NOISE,
not physics. When you have exact local physics (AC=0), the equations
are linear algebra. The nonlinearity comes from:
  - Averaging over unknowns (creates diffusion)
  - Approximating potentials (introduces artificial nonlinearity)
  - Truncating series (compounds errors)

The diffusion trap: once you average, errors MULTIPLY at each step.
The "chaos" you see is your method fighting itself, not nature being complex.

Prediction: every system currently modeled as "complex" or "chaotic"
will simplify to linear algebra when exact local physics is available.

Examples:
  - Weather → exact Navier-Stokes on patches = linear per patch
  - Protein folding → exact quantum chemistry = linear eigenvalue problem
  - Crystal growth → exact local potentials = linear fabrication
  - Turbulence → exact local vorticity = linear transport
  - Neural networks → exact local coupling = linear graph

Score: pending/pending.
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


BG = '#1a1a2e'
WHITE = '#ffffff'
DIM = '#667788'
GOLD = '#ffd700'
RED = '#e94560'
CYAN = '#53d8fb'
GREEN = '#50fa7b'


def fig1_diffusion_trap():
    """Show how averaging creates the diffusion trap."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), facecolor=BG)

    # Top: Exact trajectory (linear, clean)
    ax1.set_facecolor(BG)
    t = np.linspace(0, 10, 500)
    x_exact = np.sin(2 * t) + 0.5 * np.sin(5 * t)

    ax1.plot(t, x_exact, color=GREEN, linewidth=2, label='Exact (linear algebra)')
    ax1.set_title('Exact Solution: Clean, Deterministic', color=GREEN,
                  fontsize=13, fontweight='bold')
    ax1.set_ylabel('x(t)', color=WHITE, fontsize=11)
    ax1.legend(facecolor='#16213e', edgecolor='#334466', labelcolor=WHITE)
    ax1.tick_params(colors=DIM)
    ax1.spines['bottom'].set_color(DIM)
    ax1.spines['left'].set_color(DIM)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Bottom: Approximate trajectory (diffusive, noisy, "chaotic")
    ax2.set_facecolor(BG)

    # Simulate error accumulation
    np.random.seed(137)
    n_steps = 500
    dt = t[1] - t[0]
    x_approx = np.zeros(n_steps)
    x_approx[0] = x_exact[0]

    error_growth = 1.003  # Error compounds at each step
    for i in range(1, n_steps):
        # True derivative + noise from approximation
        dx = (x_exact[i] - x_exact[i-1])
        noise = np.random.normal(0, 0.01) * error_growth**(i)
        x_approx[i] = x_approx[i-1] + dx + noise

    ax2.plot(t, x_exact, color=GREEN, linewidth=1, alpha=0.3,
             label='True solution')
    ax2.plot(t, x_approx, color=RED, linewidth=1.5,
             label='Approximate (noise compounds)')
    ax2.fill_between(t, x_exact, x_approx, color=RED, alpha=0.1)

    ax2.set_title('Approximate Solution: "Chaotic" (Actually: Compounding Noise)',
                  color=RED, fontsize=13, fontweight='bold')
    ax2.set_xlabel('Time', color=WHITE, fontsize=11)
    ax2.set_ylabel('x(t)', color=WHITE, fontsize=11)
    ax2.legend(facecolor='#16213e', edgecolor='#334466', labelcolor=WHITE)
    ax2.tick_params(colors=DIM)
    ax2.spines['bottom'].set_color(DIM)
    ax2.spines['left'].set_color(DIM)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    plt.tight_layout()
    return fig


def fig2_systems():
    """Five systems: current model vs linearized prediction."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 7), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(7, 6.5, 'Five Systems: "Complex" → Linear', color=WHITE,
            fontsize=16, ha='center', fontweight='bold')

    systems = [
        ('Weather', 'Navier-Stokes\n(turbulent, chaotic)',
         'Exact per 10km patch\n(linear eigenvalues)', RED, GREEN),
        ('Proteins', 'Molecular dynamics\n(force field approx)',
         'Exact quantum chem\n(linear eigenvalue)',  RED, GREEN),
        ('Crystals', 'DFT + corrections\n(pseudopotentials)',
         'Exact local potentials\n(linear fabrication)', RED, GREEN),
        ('Turbulence', 'Reynolds averaging\n(closure problem)',
         'Exact local vorticity\n(linear transport)', RED, GREEN),
        ('Neural nets', 'Backpropagation\n(gradient descent)',
         'Exact local coupling\n(linear graph)', RED, GREEN),
    ]

    for i, (name, current, linear, c_cur, c_lin) in enumerate(systems):
        y = 5.0 - i * 1.1
        x_name = 1.5
        x_current = 5.0
        x_linear = 10.0

        ax.text(x_name, y, name, color=GOLD, fontsize=12,
                ha='center', fontweight='bold')

        # Current model box
        rect = FancyBboxPatch((x_current - 1.5, y - 0.4), 3.0, 0.8,
                               boxstyle="round,pad=0.05",
                               facecolor=c_cur, alpha=0.1,
                               edgecolor=c_cur, linewidth=1)
        ax.add_patch(rect)
        ax.text(x_current, y, current, color=DIM, fontsize=8,
                ha='center', va='center')

        # Arrow
        ax.annotate('', xy=(x_linear - 1.5, y), xytext=(x_current + 1.5, y),
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2))

        # Linear model box
        rect = FancyBboxPatch((x_linear - 1.5, y - 0.4), 3.0, 0.8,
                               boxstyle="round,pad=0.05",
                               facecolor=c_lin, alpha=0.1,
                               edgecolor=c_lin, linewidth=1)
        ax.add_patch(rect)
        ax.text(x_linear, y, linear, color=DIM, fontsize=8,
                ha='center', va='center')

    # Headers
    ax.text(5.0, 5.8, 'Current Model', color=RED, fontsize=11,
            ha='center', fontweight='bold')
    ax.text(10.0, 5.8, 'AC=0 Prediction', color=GREEN, fontsize=11,
            ha='center', fontweight='bold')

    # Bottom insight
    ax.text(7, 0.3, '"Complexity" is the name we give to compounding approximation errors.\n'
                      'Nature is not complex. Our methods are.',
            color=DIM, fontsize=10, ha='center', fontstyle='italic')

    plt.tight_layout()
    return fig


def fig3_error_anatomy():
    """Anatomy of the diffusion trap: where the nonlinearity comes from."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 7), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(6, 6.5, 'Anatomy of the Diffusion Trap', color=WHITE,
            fontsize=16, ha='center', fontweight='bold')

    sources = [
        ('Averaging', 'Replace microscopic state with macroscopic average',
         'Creates artificial diffusion coefficient', RED),
        ('Truncation', 'Drop higher-order terms in Taylor expansion',
         'Introduces artificial nonlinearity at truncation order', RED),
        ('Closure', 'Approximate unknown correlations (e.g. Reynolds stress)',
         'Transfers real physics into model noise', RED),
        ('Discretization', 'Replace continuous PDE with discrete grid',
         'Aliases high frequencies into low-frequency artifacts', RED),
        ('Iteration', 'Compound all above errors at every time step',
         'Error × error × error × ... = "chaos"', GOLD),
    ]

    for i, (name, mechanism, result, color) in enumerate(sources):
        y = 5.5 - i * 1.1

        # Source box
        rect = FancyBboxPatch((0.5, y - 0.35), 2.5, 0.7,
                               boxstyle="round,pad=0.05",
                               facecolor=color, alpha=0.15,
                               edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(1.75, y + 0.05, name, color=color, fontsize=11,
                ha='center', fontweight='bold')

        # Mechanism
        ax.text(3.5, y + 0.05, mechanism, color=DIM, fontsize=9,
                ha='left', va='center')

        # Result
        ax.text(3.5, y - 0.2, f'→ {result}', color=color, fontsize=8,
                ha='left', va='center', alpha=0.8)

    # Bottom: the punchline
    ax.text(6, 0.5, 'Remove all five sources → linear algebra.\n'
                      'The "nonlinearity" was never in the physics.',
            color=GREEN, fontsize=12, ha='center', fontweight='bold')

    plt.tight_layout()
    return fig


def main():
    print("=" * 70)
    print("Toy 240 — Linearization of 'Complex' Systems")
    print("Conjecture 7: Method Noise Creates Apparent Complexity")
    print("=" * 70)
    print()
    print("  The diffusion trap:")
    print("    1. Average over unknowns → creates diffusion")
    print("    2. Truncate series → artificial nonlinearity")
    print("    3. Approximate closure → transfers physics to noise")
    print("    4. Discretize → frequency aliasing")
    print("    5. Iterate → error × error × ... = 'chaos'")
    print()
    print("  Remove all five → linear algebra.")
    print("  The 'nonlinearity' was never in the physics.")
    print()

    print("Figure 1: Diffusion trap (exact vs approximate)")
    fig1_diffusion_trap()

    print("Figure 2: Five systems (complex → linear)")
    fig2_systems()

    print("Figure 3: Anatomy of the diffusion trap")
    fig3_error_anatomy()

    plt.show()

    print()
    print("Toy 240 complete.")
    print("Nature is not complex. Our methods are.")


if __name__ == '__main__':
    main()
