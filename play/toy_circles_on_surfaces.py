#!/usr/bin/env python3
"""
CIRCLES ON CLOSED SURFACES -> QUANTIZATION  --  Toy 138
========================================================
Quantization is geometry, not axiom.

"The substrate is discrete because circles tiling a closed surface is discrete.
 Quantum is naturally 2D."  -- Casey Koons, March 2026

This toy demonstrates the chain:
  Compact geometry -> Integer winding -> Discrete eigenvalues
  -> Mass gap -> Proton mass = 6*pi^5*m_e

On a CLOSED surface (compact manifold), eigenfunctions must be single-valued.
Single-valuedness forces integer mode numbers. Integer mode numbers give
discrete eigenvalues. Discrete eigenvalues ARE quantization.

No axioms. Just circles on closed surfaces.

CI Interface:
    from toy_circles_on_surfaces import CirclesOnSurfaces
    cs = CirclesOnSurfaces()
    cs.winding_modes_s1()          # Panel 1 data: S^1 winding modes
    cs.spherical_harmonics_s2()    # Panel 2 data: S^2 eigenvalue ladder
    cs.spectral_gap_sequence()     # Panel 3 data: Q^n gap sequence
    cs.mode_counting_q5()          # Panel 4 data: Q^5 eigenvalue multiplicities
    cs.compact_vs_noncompact()     # Panel 5 data: spectrum comparison
    cs.implication_chain()         # Panel 6 data: the chain
    cs.summary()                   # Key results as dict
    cs.show()                      # 6-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import comb
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc, Circle, Wedge
from matplotlib.gridspec import GridSpec


# ======================================================================
#  BST FUNDAMENTAL CONSTANTS -- the five integers
# ======================================================================

N_c   = 3                           # color charges
n_C   = 5                           # complex dimension of D_IV^5
C_2   = n_C + 1                     # = 6, Casimir eigenvalue
genus = n_C + 2                     # = 7
N_max = 137                         # Haldane channel capacity

m_e   = 0.51099895                  # electron mass (MeV)
m_p_obs = 938.272                   # proton mass observed (MeV)
m_p_bst = 6 * np.pi**5 * m_e       # proton mass from BST


# ======================================================================
#  COLORS
# ======================================================================

BG        = '#0a0a1a'
BG_PANEL  = '#0d0d24'
BG_BOX    = '#141432'
GOLD      = '#ffd700'
GOLD_DIM  = '#aa8800'
CYAN      = '#00ddff'
CYAN_DIM  = '#1a6688'
GREEN     = '#44ff88'
GREEN_DIM = '#22aa55'
RED       = '#ff4444'
RED_DIM   = '#992222'
ORANGE    = '#ff8800'
BLUE      = '#4488ff'
PURPLE    = '#9966cc'
PURPLE_DIM = '#6b3fa0'
WHITE     = '#ffffff'
GREY      = '#888888'
DGREY     = '#444444'
PINK      = '#ff66aa'
TEAL      = '#00ccaa'
MAGENTA   = '#cc44ff'

# Glow effects
GLOW_GOLD = [pe.withStroke(linewidth=3, foreground='#554400'), pe.Normal()]
GLOW_CYAN = [pe.withStroke(linewidth=3, foreground='#004455'), pe.Normal()]
GLOW_GREEN = [pe.withStroke(linewidth=3, foreground='#115522'), pe.Normal()]

# Panel colors for winding modes
WINDING_COLORS = ['#888888', GOLD, CYAN, GREEN, ORANGE, PINK, MAGENTA, BLUE]


# ======================================================================
#  MULTIPLICITY FORMULA
# ======================================================================

def multiplicity_Qn(k, n):
    """
    Multiplicity of the k-th eigenvalue on Q^n = SO(n+2)/[SO(n) x SO(2)].

    Eigenvalue:    lambda_k = k(k + n)
    Multiplicity:  d_k = dim_sym_traceless(n+2, k) - dim_sym_traceless(n+2, k-2)

    where dim_sym_traceless(m, k) = C(m+k-1, k) - C(m+k-3, k-2).
    """
    m = n + 2  # SO(m)
    def dim_sym_traceless(mm, kk):
        if kk < 0:
            return 0
        if kk == 0:
            return 1
        if kk == 1:
            return mm
        return comb(mm + kk - 1, kk) - comb(mm + kk - 3, kk - 2)
    if k == 0:
        return 1
    d = dim_sym_traceless(m, k) - dim_sym_traceless(m, k - 2)
    return max(d, 0)


# ======================================================================
#  CLASS: CirclesOnSurfaces
# ======================================================================

class CirclesOnSurfaces:
    """
    Circles on Closed Surfaces -> Quantization.

    Demonstrates that quantization is a geometric consequence of compactness:
    circles tiling a closed surface must fit integer times, forcing discrete
    eigenvalues. Applied to Q^5, this gives the proton mass gap.
    """

    def __init__(self, quiet=True):
        self._quiet = quiet
        self.fig = None

        # Pre-compute key data
        self._s1_data = self._compute_s1()
        self._s2_data = self._compute_s2()
        self._gap_data = self._compute_gap_sequence()
        self._q5_data = self._compute_q5_modes()

        if not quiet:
            print()
            print("  CirclesOnSurfaces initialized.")
            print(f"  Proton mass (BST): 6*pi^5*m_e = {m_p_bst:.3f} MeV")
            print(f"  Proton mass (obs):              {m_p_obs:.3f} MeV")
            print(f"  Agreement: {abs(m_p_bst - m_p_obs)/m_p_obs * 100:.4f}%")
            print()

    # ------------------------------------------------------------------
    #  COMPUTATION METHODS (return dicts/lists for CI scripting)
    # ------------------------------------------------------------------

    def _compute_s1(self):
        """Compute S^1 winding mode data."""
        modes = []
        for n in range(6):
            modes.append({
                'n': n,
                'eigenvalue': n * n,
                'multiplicity': 1 if n == 0 else 2,
                'interpretation': {
                    0: 'Constant mode (vacuum)',
                    1: 'First harmonic -- THE GAP',
                    2: 'Second harmonic',
                    3: 'Third harmonic',
                    4: 'Fourth harmonic',
                    5: 'Fifth harmonic',
                }[n]
            })
        return modes

    def _compute_s2(self):
        """Compute S^2 spherical harmonic data."""
        levels = []
        for l in range(8):
            levels.append({
                'l': l,
                'eigenvalue': l * (l + 1),
                'multiplicity': 2 * l + 1,
                'interpretation': {
                    0: 'Monopole (vacuum)',
                    1: 'Dipole -- GAP = 2',
                    2: 'Quadrupole',
                    3: 'Octupole',
                }.get(l, f'l = {l}')
            })
        return levels

    def _compute_gap_sequence(self):
        """Compute spectral gap sequence for Q^n manifolds."""
        entries = []
        manifold_list = [
            ('S^1', 1, lambda: 1, lambda: 2),
            ('S^2', 2, lambda: 2, lambda: 3),
            ('Q^1=S^2', 2, lambda: 1*(1+1), lambda: 1+2),
            ('Q^3', 6, lambda: 1*(1+3), lambda: 3+2),
            ('Q^5', 10, lambda: 1*(1+5), lambda: 5+2),
            ('Q^7', 14, lambda: 1*(1+7), lambda: 7+2),
            ('Q^9', 18, lambda: 1*(1+9), lambda: 9+2),
        ]
        for name, dim_r, gap_fn, mult_fn in manifold_list:
            lam1 = gap_fn()
            d1 = mult_fn()
            is_bst = (name == 'Q^5')
            entries.append({
                'manifold': name,
                'dim_real': dim_r,
                'gap_lambda1': lam1,
                'multiplicity_d1': d1,
                'is_bst': is_bst,
                'bst_role': 'PHYSICAL (BST)' if is_bst else '',
                'product': lam1 * d1 if is_bst else None,
            })
        return entries

    def _compute_q5_modes(self):
        """Compute eigenvalues and multiplicities for Q^5."""
        modes = []
        total = 0
        for k in range(7):
            lam = k * (k + n_C)
            dk = multiplicity_Qn(k, n_C)
            total += dk
            modes.append({
                'k': k,
                'eigenvalue': lam,
                'multiplicity': dk,
                'cumulative': total,
                'product': dk * lam if k > 0 else 0,
            })
        return modes

    # ------------------------------------------------------------------
    #  PUBLIC CI INTERFACE METHODS
    # ------------------------------------------------------------------

    def winding_modes_s1(self):
        """Panel 1 data: Winding modes on S^1."""
        data = self._s1_data
        if not self._quiet:
            print()
            print("  ========================================")
            print("  S^1: THE CIRCLE (1D compact manifold)")
            print("  ========================================")
            print()
            print("  On a circle, eigenfunctions are e^{2*pi*i*n*x/L}.")
            print("  Single-valuedness: f(x+L) = f(x)  =>  n in Z.")
            print("  Eigenvalues: lambda_n = n^2 -- DISCRETE.")
            print()
            print(f"  {'n':<4} {'lambda_n':<12} {'d_n':<6} {'Interpretation'}")
            print(f"  {'-'*4} {'-'*12} {'-'*6} {'-'*30}")
            for m in data:
                print(f"  {m['n']:<4} {m['eigenvalue']:<12} {m['multiplicity']:<6} {m['interpretation']}")
            print()
            print("  Gap: lambda_1 = 1.  WHY? You cannot wind a circle 0.5 times.")
            print()
        return data

    def spherical_harmonics_s2(self):
        """Panel 2 data: Spherical harmonics on S^2."""
        data = self._s2_data
        if not self._quiet:
            print()
            print("  ========================================")
            print("  S^2: THE SPHERE (2D compact manifold)")
            print("  ========================================")
            print()
            print("  Eigenfunctions: Y_l^m  (spherical harmonics)")
            print("  Eigenvalues: lambda_l = l(l+1) with multiplicity d_l = 2l+1")
            print()
            print(f"  {'l':<4} {'lambda_l':<10} {'d_l':<8} {'Note'}")
            print(f"  {'-'*4} {'-'*10} {'-'*8} {'-'*25}")
            for m in data:
                print(f"  {m['l']:<4} {m['eigenvalue']:<10} {m['multiplicity']:<8} {m['interpretation']}")
            print()
        return data

    def spectral_gap_sequence(self):
        """Panel 3 data: Spectral gap sequence for Q^n manifolds."""
        data = self._gap_data
        if not self._quiet:
            print()
            print("  ==============================================")
            print("  Q^n SPECTRAL GAP SEQUENCE")
            print("  ==============================================")
            print()
            print(f"  {'Manifold':<10} {'dim_R':<7} {'lambda_1':<10} {'d_1':<6} {'BST role'}")
            print(f"  {'-'*10} {'-'*7} {'-'*10} {'-'*6} {'-'*20}")
            for e in data:
                mark = ' ***' if e['is_bst'] else ''
                print(f"  {e['manifold']:<10} {e['dim_real']:<7} {e['gap_lambda1']:<10} "
                      f"{e['multiplicity_d1']:<6} {e['bst_role']}{mark}")
            print()
            print("  Q^5: lambda_1 = 6 = C_2,  d_1 = 7 = genus")
            print("  d_1 x lambda_1 = 42 = P(1) = sum of all Chern classes")
            print()
        return data

    def mode_counting_q5(self):
        """Panel 4 data: Mode counting on Q^5."""
        data = self._q5_data
        if not self._quiet:
            print()
            print("  ==============================================")
            print("  MODE COUNTING ON Q^5")
            print("  ==============================================")
            print()
            print(f"  {'k':<4} {'lambda_k':<10} {'d_k':<8} {'N(k)':<8} {'d_k*lambda_k'}")
            print(f"  {'-'*4} {'-'*10} {'-'*8} {'-'*8} {'-'*12}")
            for m in data:
                prod = f"{m['product']}" if m['k'] > 0 else '-'
                print(f"  {m['k']:<4} {m['eigenvalue']:<10} {m['multiplicity']:<8} "
                      f"{m['cumulative']:<8} {prod}")
            print()
            print(f"  k=1: lambda_1 = 6 = C_2 (Casimir), d_1 = 7 = genus (n_C + 2)")
            print(f"  d_1 x lambda_1 = 7 x 6 = 42 = P(1)")
            print()
        return data

    def compact_vs_noncompact(self):
        """Panel 5 data: Compact vs non-compact spectrum comparison."""
        data = {
            'compact': {
                'manifold': 'Q^5 = SO(7)/[SO(5) x SO(2)]',
                'spectrum': 'DISCRETE',
                'eigenvalues': [k * (k + 5) for k in range(7)],
                'multiplicities': [multiplicity_Qn(k, 5) for k in range(7)],
                'mass_gap': True,
                'gap_value': 6,
                'result': 'Quantum mechanics',
            },
            'noncompact': {
                'manifold': 'D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]',
                'spectrum': 'CONTINUOUS',
                'eigenvalues': 'Plancherel measure (smooth)',
                'mass_gap': False,
                'gap_value': 0,
                'result': 'Classical limit',
            },
            'duality': 'Compact/non-compact duality IS wave-particle duality',
        }
        if not self._quiet:
            print()
            print("  ==============================================")
            print("  COMPACT vs NON-COMPACT")
            print("  ==============================================")
            print()
            print("  COMPACT (Q^5):             NON-COMPACT (D_IV^5):")
            print("  Eigenvalues: DISCRETE      Spectrum: CONTINUOUS")
            print("  Mass gap: YES (lambda_1=6) Mass gap: NO")
            print("  Quantum numbers: INTEGER   Quantum numbers: REAL")
            print("  -> Quantum mechanics       -> Classical physics")
            print()
            print(f"  {data['duality']}")
            print()
        return data

    def implication_chain(self):
        """Panel 6 data: The chain of implications."""
        chain = [
            ('Compact geometry (Q^5)', 'Surface is closed -- no boundary'),
            ('Integer winding', 'Circles must tile in integer configurations'),
            ('Discrete eigenvalues', 'lambda_k = k(k+5), k = 0, 1, 2, ...'),
            ('Mass gap', 'lambda_1 = 6 > lambda_0 = 0'),
            ('Proton mass', f'm_p = 6*pi^5*m_e = {m_p_bst:.3f} MeV'),
        ]
        if not self._quiet:
            print()
            print("  ==============================================")
            print("  THE IMPLICATION CHAIN")
            print("  ==============================================")
            print()
            for i, (step, detail) in enumerate(chain):
                print(f"  {step}")
                print(f"    ({detail})")
                if i < len(chain) - 1:
                    print("       |")
                    print("       v")
            print()
            print("  Quantization is not an axiom.")
            print("  It is a CONSEQUENCE of compact geometry.")
            print()
        return chain

    def summary(self):
        """Return key results as a dictionary."""
        s = {
            'toy_number': 138,
            'title': 'Circles on Closed Surfaces -> Quantization',
            'bst_constants': {
                'N_c': N_c,
                'n_C': n_C,
                'C_2': C_2,
                'genus': genus,
                'N_max': N_max,
            },
            'q5_spectral': {
                'eigenvalue_formula': 'lambda_k = k(k+5)',
                'gap': 6,
                'gap_multiplicity': 7,
                'gap_times_mult': 42,
                'gap_equals': 'C_2',
                'mult_equals': 'genus = n_C + 2',
                'product_equals': 'P(1) = sum of Chern classes',
            },
            'proton_mass': {
                'formula': '6 * pi^5 * m_e',
                'bst_MeV': m_p_bst,
                'obs_MeV': m_p_obs,
                'pct_error': abs(m_p_bst - m_p_obs) / m_p_obs * 100,
            },
            'key_insight': (
                'Quantization is a consequence of compact geometry. '
                'Circles tiling a closed surface must fit integer times, '
                'forcing discrete eigenvalues. '
                'The complex structure (2D) provides winding numbers.'
            ),
            'manifold_sequence': [
                {'name': 'S^1', 'gap': 1, 'd1': 2},
                {'name': 'S^2', 'gap': 2, 'd1': 3},
                {'name': 'Q^5', 'gap': 6, 'd1': 7},
            ],
        }
        if not self._quiet:
            print()
            print("  ==============================================")
            print("  SUMMARY: CIRCLES ON SURFACES -> QUANTIZATION")
            print("  ==============================================")
            print()
            print(f"  On Q^5: lambda_1 = {s['q5_spectral']['gap']} = C_2")
            print(f"          d_1     = {s['q5_spectral']['gap_multiplicity']} = genus")
            print(f"          d_1 * lambda_1 = {s['q5_spectral']['gap_times_mult']} = P(1)")
            print()
            print(f"  Proton mass: 6*pi^5*m_e = {m_p_bst:.3f} MeV  "
                  f"(obs: {m_p_obs:.3f} MeV, {s['proton_mass']['pct_error']:.4f}%)")
            print()
            print(f"  \"{s['key_insight']}\"")
            print()
        return s

    # ------------------------------------------------------------------
    #  VISUALIZATION
    # ------------------------------------------------------------------

    def show(self):
        """Display the 6-panel visualization."""

        fig = plt.figure(figsize=(21, 14), facecolor=BG)

        # Main title
        fig.suptitle(
            "CIRCLES ON CLOSED SURFACES \u2192 QUANTIZATION \u2014 Toy 138",
            fontsize=24, fontweight='bold', color=GOLD, y=0.98,
            path_effects=GLOW_GOLD
        )

        # Casey's quote
        fig.text(
            0.5, 0.948,
            '\u201cThe substrate is discrete because circles tiling '
            'a closed surface is discrete. Quantum is naturally 2D.\u201d',
            ha='center', fontsize=11, color=CYAN, style='italic',
            path_effects=GLOW_CYAN
        )

        gs = GridSpec(2, 3, figure=fig,
                      left=0.05, right=0.96, top=0.915, bottom=0.06,
                      hspace=0.38, wspace=0.28)

        # Panel 1: Circles on S^1
        ax1 = fig.add_subplot(gs[0, 0])
        self._draw_winding_s1(ax1)

        # Panel 2: Spherical Harmonics on S^2
        ax2 = fig.add_subplot(gs[0, 1])
        self._draw_s2_ladder(ax2)

        # Panel 3: Q^n Spectral Gap Sequence
        ax3 = fig.add_subplot(gs[0, 2])
        self._draw_gap_sequence(ax3)

        # Panel 4: Mode Counting on Q^5
        ax4 = fig.add_subplot(gs[1, 0])
        self._draw_q5_modes(ax4)

        # Panel 5: Compact vs Non-Compact
        ax5 = fig.add_subplot(gs[1, 1])
        self._draw_compact_vs_noncompact(ax5)

        # Panel 6: The Chain
        ax6 = fig.add_subplot(gs[1, 2])
        self._draw_chain(ax6)

        # Copyright
        fig.text(0.99, 0.008,
                 '\u00a9 Casey Koons, March 2026  |  Created with Claude Opus 4.6',
                 ha='right', va='bottom', fontsize=7, color=DGREY)

        self.fig = fig
        plt.show(block=False)
        return fig

    # ------------------------------------------------------------------
    #  PANEL HELPERS
    # ------------------------------------------------------------------

    def _panel_setup(self, ax, title, subtitle=None):
        """Common panel setup: dark background, title."""
        ax.set_facecolor(BG_PANEL)
        for spine in ax.spines.values():
            spine.set_color(DGREY)
            spine.set_linewidth(0.5)
        ax.set_title(title, fontsize=12, fontweight='bold', color=GOLD,
                     pad=10, path_effects=GLOW_GOLD)
        if subtitle:
            ax.text(0.5, 1.01, subtitle, transform=ax.transAxes,
                    ha='center', va='bottom', fontsize=8, color=CYAN,
                    style='italic')
        ax.tick_params(colors=GREY, which='both')

    # ------------------------------------------------------------------
    #  Panel 1: Winding Modes on S^1
    # ------------------------------------------------------------------

    def _draw_winding_s1(self, ax):
        """Show winding modes n=0..4 on a circle with eigenvalue table."""
        self._panel_setup(ax, "Circles on S\u00b9",
                          "Winding modes: integer wavelengths")
        ax.set_xlim(-1.9, 5.5)
        ax.set_ylim(-1.7, 1.6)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal')

        # Draw the base circle
        theta = np.linspace(0, 2 * np.pi, 300)
        cx, cy = -0.4, 0.0
        R = 1.05
        ax.plot(cx + R * np.cos(theta), cy + R * np.sin(theta),
                color=GREY, lw=1.5, alpha=0.3)

        # Draw winding modes n=0..4 as colored waves on the circle
        for n in range(5):
            color = WINDING_COLORS[n]
            if n == 0:
                # Constant mode: dot at top
                ax.plot(cx, cy + R, 'o', color=color, ms=7, alpha=0.9,
                        zorder=5)
            else:
                # Wave with n oscillations around the circle
                amp = 0.10 + 0.025 * n
                r_wave = R + amp * np.sin(n * theta)
                lw = 2.5 if n == 1 else 1.3
                alpha = 1.0 if n == 1 else 0.55
                ax.plot(cx + r_wave * np.cos(theta),
                        cy + r_wave * np.sin(theta),
                        color=color, lw=lw, alpha=alpha)

        # Label the modes -- spread evenly around the circle
        label_angles = [np.pi / 2, np.pi * 0.85, np.pi * 1.2,
                        np.pi * 1.55, np.pi * 1.9]
        for n in range(5):
            color = WINDING_COLORS[n]
            angle = label_angles[n]
            label_r = R + 0.42
            lx = cx + label_r * np.cos(angle)
            ly = cy + label_r * np.sin(angle)
            ax.text(lx, ly, f'n={n}', fontsize=7, color=color,
                    ha='center', va='center', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.1', facecolor=BG_PANEL,
                              edgecolor='none', alpha=0.7))

        # Eigenvalue table on the right side
        table_x = 2.6
        ax.text(table_x + 0.9, 1.45, 'Eigenvalue Table',
                fontsize=8, fontweight='bold', color=GOLD, ha='center')

        # Column headers
        headers = [('n', table_x), ('\u03bb\u2099=n\u00b2', table_x + 0.9),
                   ('d\u2099', table_x + 1.8)]
        for hdr, hx in headers:
            ax.text(hx, 1.15, hdr, fontsize=7, color=GREY, ha='center',
                    fontweight='bold')

        # Separator line
        ax.plot([table_x - 0.3, table_x + 2.1], [1.03, 1.03],
                color=DGREY, lw=0.5)

        for i, mode in enumerate(self._s1_data[:5]):
            y = 0.75 - i * 0.42
            n_val = mode['n']
            lam = mode['eigenvalue']
            d_n = mode['multiplicity']
            color = GOLD if n_val == 1 else (WINDING_COLORS[n_val] if n_val < len(WINDING_COLORS) else WHITE)
            weight = 'bold' if n_val == 1 else 'normal'
            ax.text(table_x, y, str(n_val), fontsize=8, color=color,
                    ha='center', fontweight=weight)
            ax.text(table_x + 0.9, y, str(lam), fontsize=8, color=color,
                    ha='center', fontweight=weight)
            ax.text(table_x + 1.8, y, str(d_n), fontsize=8, color=color,
                    ha='center', fontweight=weight)

        # Highlight the gap
        ax.text(table_x + 0.9, -1.4,
                'Gap: \u03bb\u2081 = 1  (no half-windings!)',
                fontsize=7, color=GREEN, ha='center', fontweight='bold',
                path_effects=GLOW_GREEN)

    # ------------------------------------------------------------------
    #  Panel 2: Spherical Harmonics on S^2
    # ------------------------------------------------------------------

    def _draw_s2_ladder(self, ax):
        """Show eigenvalue ladder for S^2 as a clean energy-level diagram."""
        self._panel_setup(ax, "Spherical Harmonics on S\u00b2",
                          "\u03bb\u2097 = l(l+1),  d\u2097 = 2l+1")

        levels = self._s2_data[:7]

        # Use a centered layout: eigenvalue on y-axis, level lines at center
        # width proportional to multiplicity
        ax.set_xlim(-1.5, 8.0)
        ax.set_ylim(-4, 48)
        ax.set_ylabel('Eigenvalue \u03bb\u2097', fontsize=9, color=GREY)
        ax.set_xticks([])

        center_x = 3.0
        max_d = max(lev['multiplicity'] for lev in levels)

        for lev in levels:
            l_val = lev['l']
            lam = lev['eigenvalue']
            d = lev['multiplicity']
            half_w = (d / max_d) * 2.2  # Width proportional to multiplicity

            # Color scheme
            if l_val == 0:
                color = GREY
                alpha = 0.6
                lw = 2
            elif l_val == 1:
                color = GOLD
                alpha = 1.0
                lw = 3
            else:
                color = CYAN
                alpha = 0.7
                lw = 2

            # Level line (width encodes multiplicity)
            ax.plot([center_x - half_w, center_x + half_w], [lam, lam],
                    color=color, lw=lw, alpha=alpha, solid_capstyle='round')

            # Small ticks at ends to make it look like a shelf
            for xend in [center_x - half_w, center_x + half_w]:
                ax.plot([xend, xend], [lam - 0.5, lam + 0.5],
                        color=color, lw=0.5, alpha=alpha * 0.5)

            # Left label: eigenvalue
            ax.text(center_x - half_w - 0.2, lam, f'\u03bb={lam}',
                    fontsize=7, color=GREY, va='center', ha='right')

            # Right labels: l and d
            ax.text(center_x + half_w + 0.2, lam,
                    f'l={l_val}  d={d}',
                    fontsize=7, color=color, va='center', ha='left',
                    fontweight='bold' if l_val == 1 else 'normal')

        # Gap arrow between l=0 and l=1
        ax.annotate('', xy=(center_x - 2.8, 2), xytext=(center_x - 2.8, 0),
                    arrowprops=dict(arrowstyle='<->', color=GREEN, lw=2))
        ax.text(center_x - 2.8, 1.0, ' GAP', fontsize=9, color=GREEN,
                fontweight='bold', va='center', ha='left')

        # Pattern note at bottom
        ax.text(center_x, -3, 'Width \u221d multiplicity (2l+1)',
                fontsize=7, color=GREY, ha='center', style='italic')

        ax.grid(axis='y', color=DGREY, alpha=0.2, ls=':')

    # ------------------------------------------------------------------
    #  Panel 3: Q^n Spectral Gap Sequence
    # ------------------------------------------------------------------

    def _draw_gap_sequence(self, ax):
        """Bar chart showing gap and multiplicity for Q^n manifolds."""
        self._panel_setup(ax, "Q\u207f Spectral Gap Sequence",
                          "\u03bb\u2081 and d\u2081 across manifolds")

        data = self._gap_data
        names = [e['manifold'] for e in data]
        gaps = [e['gap_lambda1'] for e in data]
        mults = [e['multiplicity_d1'] for e in data]
        is_bst = [e['is_bst'] for e in data]

        x = np.arange(len(data))
        width = 0.35

        # Gap bars
        gap_colors = [GOLD if b else CYAN for b in is_bst]
        gap_alphas = [1.0 if b else 0.6 for b in is_bst]
        bars1 = ax.bar(x - width/2, gaps, width, label='\u03bb\u2081 (gap)',
                       color=gap_colors, alpha=0.8, edgecolor=[GOLD if b else CYAN_DIM for b in is_bst])

        # Multiplicity bars
        mult_colors = [GREEN if b else PURPLE for b in is_bst]
        bars2 = ax.bar(x + width/2, mults, width, label='d\u2081 (mult)',
                       color=mult_colors, alpha=0.6, edgecolor=[GREEN if b else PURPLE_DIM for b in is_bst])

        # Value labels on bars
        for i, (g, m) in enumerate(zip(gaps, mults)):
            color_g = GOLD if is_bst[i] else CYAN
            color_m = GREEN if is_bst[i] else PURPLE
            weight = 'bold' if is_bst[i] else 'normal'
            ax.text(x[i] - width/2, g + 0.3, str(g), ha='center',
                    fontsize=8, color=color_g, fontweight=weight)
            ax.text(x[i] + width/2, m + 0.3, str(m), ha='center',
                    fontsize=8, color=color_m, fontweight=weight)

        # Highlight Q^5
        q5_idx = next(i for i, e in enumerate(data) if e['is_bst'])
        ax.axvspan(q5_idx - 0.5, q5_idx + 0.5, alpha=0.08, color=GOLD)

        # Annotation for Q^5
        ax.text(q5_idx, max(gaps) + 2.2,
                '\u03bb\u2081=6=C\u2082, d\u2081=7=g\n'
                'd\u2081\u00d7\u03bb\u2081 = 42 = P(1)',
                ha='center', fontsize=7, color=GOLD, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_BOX,
                          edgecolor=GOLD_DIM, alpha=0.9))

        ax.set_xticks(x)
        ax.set_xticklabels(names, fontsize=7, color=GREY, rotation=30, ha='right')
        ax.set_ylabel('Value', fontsize=8, color=GREY)
        ax.legend(fontsize=7, loc='upper left', facecolor=BG_BOX,
                  edgecolor=DGREY, labelcolor=GREY)
        ax.set_ylim(0, max(max(gaps), max(mults)) + 4.5)
        ax.grid(axis='y', color=DGREY, alpha=0.3, ls=':')

    # ------------------------------------------------------------------
    #  Panel 4: Mode Counting on Q^5
    # ------------------------------------------------------------------

    def _draw_q5_modes(self, ax):
        """Show eigenvalues and multiplicities for Q^5, k=0..6."""
        self._panel_setup(ax, "Mode Counting on Q\u2075",
                          "\u03bb\u2096 = k(k+5), d\u2096 multiplicities")

        modes = self._q5_data
        ks = [m['k'] for m in modes]
        lams = [m['eigenvalue'] for m in modes]
        dks = [m['multiplicity'] for m in modes]

        # Bar chart of multiplicities
        colors = []
        for m in modes:
            if m['k'] == 0:
                colors.append(GREY)
            elif m['k'] == 1:
                colors.append(GOLD)
            else:
                colors.append(CYAN)

        bars = ax.bar(ks, dks, color=colors, alpha=0.7,
                      edgecolor=[c for c in colors], linewidth=0.8, width=0.7)

        # Labels on bars
        for m in modes:
            k = m['k']
            dk = m['multiplicity']
            lam = m['eigenvalue']
            color = GOLD if k == 1 else (GREY if k == 0 else CYAN)
            weight = 'bold' if k == 1 else 'normal'

            # Multiplicity on top of bar
            ax.text(k, dk + 2, f'd={dk}', ha='center', fontsize=7,
                    color=color, fontweight=weight)

            # Eigenvalue inside bar (if tall enough)
            if dk > 5:
                ax.text(k, dk / 2, f'\u03bb={lam}', ha='center', va='center',
                        fontsize=6, color=BG_PANEL, fontweight='bold')
            else:
                ax.text(k, dk + 6, f'\u03bb={lam}', ha='center', fontsize=6,
                        color=GREY)

        # Highlight k=1 bar
        ax.axvspan(0.5, 1.5, alpha=0.08, color=GOLD)

        # Key result box
        ax.text(4.5, max(dks) * 0.85,
                'k=1:  d\u2081 = 7 = genus\n'
                '       \u03bb\u2081 = 6 = C\u2082\n'
                ' d\u2081\u00d7\u03bb\u2081 = 42 = P(1)',
                fontsize=8, color=GOLD, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=BG_BOX,
                          edgecolor=GOLD_DIM, alpha=0.9),
                va='top', ha='center')

        ax.set_xlabel('Mode k', fontsize=9, color=GREY)
        ax.set_ylabel('Multiplicity d\u2096', fontsize=9, color=GREY)
        ax.set_xticks(ks)
        ax.set_ylim(0, max(dks) * 1.25)
        ax.grid(axis='y', color=DGREY, alpha=0.3, ls=':')

    # ------------------------------------------------------------------
    #  Panel 5: Compact vs Non-Compact
    # ------------------------------------------------------------------

    def _draw_compact_vs_noncompact(self, ax):
        """Visual comparison: discrete bars vs continuous curve."""
        self._panel_setup(ax, "Compact vs Non-Compact",
                          "Q\u2075 (discrete)  vs  D\u1d35\u1d5b\u2075 (continuous)")
        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-0.8, 1.5)
        ax.set_xticks([])
        ax.set_yticks([])

        # --- Left side: COMPACT (discrete spectrum) ---
        ax.text(2.2, 1.35, 'COMPACT Q\u2075', fontsize=10, fontweight='bold',
                color=GOLD, ha='center', path_effects=GLOW_GOLD)
        ax.text(2.2, 1.15, 'Discrete spectrum', fontsize=7, color=GOLD,
                ha='center', alpha=0.8)

        # Draw discrete bars (eigenvalues)
        bar_x = np.array([0.0, 0.6, 1.4, 2.4, 3.6])  # Spaced like k(k+5)
        bar_h = np.array([0.4, 0.8, 0.7, 0.5, 0.35])
        bar_colors_list = [GREY, GOLD, CYAN, CYAN, CYAN]

        for i, (bx, bh, bc) in enumerate(zip(bar_x, bar_h, bar_colors_list)):
            ax.bar(bx, bh, width=0.25, color=bc, alpha=0.8,
                   edgecolor=bc, bottom=0)
            # Mark as discrete delta
            ax.plot([bx, bx], [0, bh + 0.05], color=bc, lw=0.5, alpha=0.3)

        # Gap annotation
        ax.annotate('', xy=(0.6, -0.15), xytext=(0.0, -0.15),
                    arrowprops=dict(arrowstyle='<->', color=GREEN, lw=1.5))
        ax.text(0.3, -0.3, 'GAP', fontsize=7, color=GREEN,
                fontweight='bold', ha='center')

        # Dividing line
        ax.axvline(x=4.8, color=DGREY, lw=1, ls='--', alpha=0.5)
        ax.text(4.8, 1.35, 'vs', fontsize=9, color=GREY, ha='center',
                fontweight='bold')

        # --- Right side: NON-COMPACT (continuous spectrum) ---
        ax.text(7.5, 1.35, 'NON-COMPACT D\u1d35\u1d5b\u2075', fontsize=10,
                fontweight='bold', color=RED, ha='center')
        ax.text(7.5, 1.15, 'Continuous spectrum', fontsize=7, color=RED,
                ha='center', alpha=0.8)

        # Draw continuous curve (Plancherel density)
        x_cont = np.linspace(5.2, 9.8, 200)
        # Smooth density curve starting at zero
        density = 0.6 * (1 - np.exp(-(x_cont - 5.2) * 1.5)) * \
                  np.exp(-(x_cont - 7.0)**2 / 4.0)
        ax.fill_between(x_cont, 0, density, color=RED, alpha=0.15)
        ax.plot(x_cont, density, color=RED, lw=2, alpha=0.8)

        # No gap annotation
        ax.text(5.6, -0.3, 'NO GAP', fontsize=7, color=RED_DIM,
                fontweight='bold', ha='center')

        # Result annotations
        ax.text(2.2, -0.6, '\u2192 Quantum mechanics', fontsize=8,
                color=GREEN, fontweight='bold', ha='center',
                path_effects=GLOW_GREEN)
        ax.text(7.5, -0.6, '\u2192 Classical limit', fontsize=8,
                color=RED_DIM, ha='center')

    # ------------------------------------------------------------------
    #  Panel 6: The Chain of Implications
    # ------------------------------------------------------------------

    def _draw_chain(self, ax):
        """Beautiful flow diagram: the implication chain."""
        self._panel_setup(ax, "The Chain",
                          "Geometry \u2192 Quantization \u2192 Mass")
        ax.set_xlim(0, 10)
        ax.set_ylim(-0.3, 10.5)
        ax.set_xticks([])
        ax.set_yticks([])

        # Chain nodes: (y_pos, text, detail, color, glow)
        nodes = [
            (9.4,  'Compact Geometry',      'Q\u2075 = SO(7)/[SO(5)\u00d7SO(2)]',  GOLD,  True),
            (7.7,  'Integer Winding',        'Circles tile in n \u2208 \u2124',      CYAN,  False),
            (6.0,  'Discrete Eigenvalues',   '\u03bb\u2096 = k(k+5)',                CYAN,  False),
            (4.3,  'Mass Gap',               '\u03bb\u2081 = 6 = C\u2082',           GREEN, True),
            (2.6,  'Proton Mass',            f'm\u209a = 6\u03c0\u2075m\u2091 = {m_p_bst:.1f} MeV', GREEN, True),
        ]

        for i, (y, label, detail, color, glow) in enumerate(nodes):
            # Box with slight glow for key steps
            edge_lw = 2.0 if glow else 1.2
            box = FancyBboxPatch(
                (1.2, y - 0.5), 7.6, 1.0,
                boxstyle='round,pad=0.15',
                facecolor=BG_BOX, edgecolor=color, linewidth=edge_lw, alpha=0.9
            )
            ax.add_patch(box)

            # Main label
            fx = 10 if glow else 9
            ax.text(5.0, y + 0.12, label, fontsize=fx, fontweight='bold',
                    color=color, ha='center', va='center')

            # Detail
            ax.text(5.0, y - 0.22, detail, fontsize=7, color=color,
                    ha='center', va='center', alpha=0.7)

            # Arrow to next node
            if i < len(nodes) - 1:
                next_y = nodes[i + 1][0]
                arrow = FancyArrowPatch(
                    (5.0, y - 0.5), (5.0, next_y + 0.5),
                    arrowstyle='-|>', mutation_scale=18,
                    color=GREY, lw=2, connectionstyle='arc3,rad=0'
                )
                ax.add_patch(arrow)

        # Final emphasis at bottom
        ax.text(5.0, 1.3,
                'Quantization is not an axiom.',
                fontsize=9, color=WHITE, ha='center', fontweight='bold',
                style='italic')
        ax.text(5.0, 0.6,
                'It is a CONSEQUENCE of compact geometry.',
                fontsize=8, color=GOLD, ha='center', fontweight='bold',
                path_effects=GLOW_GOLD)
        ax.text(5.0, 0.0,
                f'Error: {abs(m_p_bst - m_p_obs)/m_p_obs * 100:.4f}%',
                fontsize=7, color=GREEN, ha='center')


# ======================================================================
#  MAIN -- interactive menu
# ======================================================================

def main():
    """Interactive menu for Circles on Surfaces -> Quantization."""
    cs = CirclesOnSurfaces(quiet=False)

    menu = """
  ============================================================
   CIRCLES ON CLOSED SURFACES -> QUANTIZATION  --  Toy 138
  ============================================================
   "The substrate is discrete because circles tiling a closed
    surface is discrete. Quantum is naturally 2D."

   1. Winding modes on S^1 (the circle)
   2. Spherical harmonics on S^2 (the sphere)
   3. Q^n spectral gap sequence
   4. Mode counting on Q^5
   5. Compact vs non-compact comparison
   6. The implication chain
   7. Summary
   0. Show visualization (6-panel)
   a. Show all (text + visualization)
   q. Quit
  ============================================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            cs.winding_modes_s1()
        elif choice == '2':
            cs.spherical_harmonics_s2()
        elif choice == '3':
            cs.spectral_gap_sequence()
        elif choice == '4':
            cs.mode_counting_q5()
        elif choice == '5':
            cs.compact_vs_noncompact()
        elif choice == '6':
            cs.implication_chain()
        elif choice == '7':
            cs.summary()
        elif choice == '0':
            cs.show()
        elif choice == 'a':
            cs.winding_modes_s1()
            print("-" * 60)
            cs.spherical_harmonics_s2()
            print("-" * 60)
            cs.spectral_gap_sequence()
            print("-" * 60)
            cs.mode_counting_q5()
            print("-" * 60)
            cs.compact_vs_noncompact()
            print("-" * 60)
            cs.implication_chain()
            print("-" * 60)
            cs.summary()
            print("-" * 60)
            cs.show()
            input("\n  Press Enter to continue...\n")
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Invalid choice. Try again.")


if __name__ == '__main__':
    main()
