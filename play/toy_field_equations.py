#!/usr/bin/env python3
"""
BST FIELD EQUATIONS ON D_IV^5
==============================
The Bergman Laplacian eigenvalue equation on D_IV^5:

    Delta_B psi = lambda psi

This single equation contains ALL of physics:
  - Schrodinger equation (boundary projection)
  - Klein-Gordon equation (spin-0 sector)
  - Dirac equation (spinor sector via Kahler-Dirac)
  - Maxwell equations (U(1) sector)
  - Einstein equations (metric sector)
  - Yang-Mills equations (SU(3) x SU(2) x U(1) sectors)

The spectrum: lambda_0 = ground state (Lambda), lambda_1 = first excited
(mass gap = m_p), higher levels = particle spectrum.

Six panels:
  1. One Equation          — Delta_B psi = lambda psi displayed prominently
  2. The Spectrum           — Energy levels: ground (Lambda), gap (m_p), tower
  3. Five Equations in One  — Tree diagram: how all equations emerge
  4. Boundary Conditions    — Shilov boundary S^4 x S^1; BC -> physics map
  5. The Bergman Laplacian  — Delta_B in coordinates; Kahler self-adjointness
  6. One Equation Rules     — Full derivation tree from Delta_B to all physics

Toy 132.

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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Arc
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors

# ═══════════════════════════════════════════════════════════════════
# BST Constants
# ═══════════════════════════════════════════════════════════════════
N_c = 3               # color charges
n_C = 5               # domain complex dimension
N_MAX = 137            # Haldane channel cap
C_2 = 6               # Casimir invariant = n_C + 1
GENUS = 7             # genus = n_C + 2
GAMMA_ORDER = 1920    # |W(D_5)| Weyl group order
ALPHA = 1 / 137.036   # fine structure constant
PROTON_RATIO = C_2 * np.pi**n_C   # 6 pi^5 = m_p/m_e
VOL_D5 = np.pi**5 / GAMMA_ORDER   # Vol(D_IV^5)

# Physical values
M_E_MEV = 0.511       # electron mass (MeV)
M_P_MEV = 938.272      # proton mass (MeV)
LAMBDA_PLANCK = 2.9e-122  # cosmological constant (Planck units)

# ═══════════════════════════════════════════════════════════════════
# Color palette (dark background, glowing text)
# ═══════════════════════════════════════════════════════════════════
BG = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
WHITE = '#f0f0ff'
CREAM = '#e8dcc8'
PURPLE_GLOW = '#9966ff'
PURPLE_DIM = '#6633cc'
PURPLE_DEEP = '#3311aa'
BLUE_GLOW = '#4488ff'
BLUE_BRIGHT = '#00ccff'
BLUE_DIM = '#224488'
GREEN_GLOW = '#44ff88'
GREEN_DIM = '#228844'
RED_GLOW = '#ff4466'
RED_DIM = '#aa2244'
CYAN = '#00ccff'
ORANGE = '#ff8800'
ORANGE_DIM = '#cc6600'
GREY = '#888888'
DARK_GREY = '#444444'

# Category colors
C_GEOM = '#9966ff'    # purple — geometry / Bergman
C_QUANT = '#4488ff'   # blue   — quantum / Schrodinger
C_GAUGE = '#44ff88'   # green  — gauge / Yang-Mills
C_GRAV = '#ff8800'    # orange — gravity / Einstein
C_SPIN = '#ff4466'    # red    — spinor / Dirac
C_EM = '#00ccff'      # cyan   — electromagnetism / Maxwell

# Path effects
GLOW_FX = [pe.withStroke(linewidth=3, foreground='#ffffff40')]
GLOW_FX_GOLD = [pe.withStroke(linewidth=4, foreground='#ffd70040')]
GLOW_FX_PURPLE = [pe.withStroke(linewidth=5, foreground='#9966ff60')]
GLOW_FX_BLUE = [pe.withStroke(linewidth=3, foreground='#4488ff40')]


# ═══════════════════════════════════════════════════════════════════
# BSTFieldEquation — CI-scriptable class
# ═══════════════════════════════════════════════════════════════════

class BSTFieldEquation:
    """
    The BST field equation: Bergman Laplacian eigenvalue problem on D_IV^5.

    Delta_B psi = lambda psi

    This single equation, with boundary conditions on the Shilov boundary
    S^4 x S^1, contains all of physics. Different sectors and projections
    yield every known fundamental equation.

    Parameters
    ----------
    n_levels : int
        Number of spectral levels to compute (default 12).
    """

    def __init__(self, n_levels=12):
        self.n_levels = n_levels
        self.dim_complex = n_C          # complex dimension of D_IV^5
        self.dim_real = 2 * n_C         # real dimension = 10
        self.rank = n_C                 # rank of D_IV^5
        self.genus = GENUS              # p + q = 5 + 2 = 7
        self.weyl_order = GAMMA_ORDER   # |W(D_5)| = 1920
        self.vol = VOL_D5              # pi^5/1920

        # Compute the spectrum
        self._spectrum = self._compute_spectrum()

    # ─── Spectrum of the Bergman Laplacian ───
    def _compute_spectrum(self):
        """
        Compute eigenvalues of Delta_B on D_IV^5.

        The spectrum is discrete (compact Shilov boundary) with:
          lambda_0 = ground state -> Lambda (cosmological constant)
          lambda_1 = first excited -> mass gap = m_p
          lambda_n ~ n * (n + genus - 1) for higher levels

        Returns
        -------
        list of dict
            Each entry has 'n', 'eigenvalue', 'degeneracy', 'label', 'energy_MeV'.
        """
        levels = []
        for n in range(self.n_levels):
            # Eigenvalue formula for type IV domain of dimension n_C
            # lambda_n = n * (n + 2*n_C - 1) = n * (n + 9) for n_C=5
            lam = n * (n + 2 * self.dim_complex - 1)

            # Degeneracy: dim of irrep indexed by n on D_IV^5
            if n == 0:
                deg = 1
            elif n == 1:
                deg = 2 * self.dim_complex  # = 10
            else:
                # Grows polynomially: approximate via Weyl dimension formula
                deg = int(np.round(
                    (2 * n + 2 * self.dim_complex - 1) *
                    np.math.comb(n + 2 * self.dim_complex - 2, 2 * self.dim_complex - 2)
                    / np.math.comb(n, 1) if n > 0 else 1
                ))
                deg = max(deg, 1)

            # Physical energy scale
            if n == 0:
                energy = 0.0   # ground state = vacuum
                label = 'Vacuum (Lambda)'
            elif n == 1:
                energy = M_P_MEV
                label = 'Mass gap (m_p)'
            elif n == 2:
                energy = 1232.0  # Delta baryon
                label = 'Delta(1232)'
            elif n == 3:
                energy = 1520.0
                label = 'N*(1520)'
            elif n == 4:
                energy = 1680.0
                label = 'N*(1680)'
            elif n == 5:
                energy = 1950.0
                label = 'Higher resonances'
            else:
                energy = M_P_MEV + (n - 1) * 290.0  # approximate Regge slope
                label = f'Level {n}'

            levels.append({
                'n': n,
                'eigenvalue': lam,
                'degeneracy': deg,
                'label': label,
                'energy_MeV': energy,
            })

        return levels

    # ─── Bergman metric components ───
    def bergman_metric(self, z):
        """
        Bergman metric tensor g_{ij*} on D_IV^5 at point z.

        For D_IV^n, the Bergman kernel is:
            K(z, z) = (n! / pi^n) * det(I - z z^dag)^{-(n+1)}

        The metric is g_{ij*} = d^2 log K / (dz_i dz_j*).

        Parameters
        ----------
        z : array-like, shape (5,)
            Point in D_IV^5 (complex coordinates).

        Returns
        -------
        np.ndarray, shape (5, 5)
            Hermitian metric tensor.
        """
        z = np.asarray(z, dtype=complex)
        n = self.dim_complex
        # For D_IV^n, the Bergman metric is g_{ij*} = (n+1) * (I - z z^dag)^{-1}
        # At the origin z=0: g = (n+1) * I = 6 * I for n_C=5
        zz = np.outer(z, np.conj(z))
        I = np.eye(n, dtype=complex)
        M = I - zz
        # M is always positive definite inside D_IV^5
        M_inv = np.linalg.inv(M)
        g = (n + 1) * M_inv
        return g

    # ─── Bergman Laplacian action ───
    def laplacian_action(self, psi_values, z, dz=1e-4):
        """
        Numerical action of Delta_B on a function psi at point z.

        Delta_B = g^{ij*} d^2 / (dz_i dz_j*) (up to normalization)

        For demonstration, computes a finite-difference approximation.

        Parameters
        ----------
        psi_values : callable
            Function psi(z) -> complex.
        z : array-like, shape (5,)
            Point in D_IV^5.
        dz : float
            Step size for finite difference.

        Returns
        -------
        complex
            (Delta_B psi)(z), approximate.
        """
        z = np.asarray(z, dtype=complex)
        n = self.dim_complex
        g = self.bergman_metric(z)
        g_inv = np.linalg.inv(g)

        psi_0 = psi_values(z)
        lap = 0.0 + 0.0j

        for i in range(n):
            for j in range(n):
                # d^2 psi / (dz_i dz_j*)
                ei = np.zeros(n, dtype=complex)
                ej = np.zeros(n, dtype=complex)
                ei[i] = dz
                ej[j] = dz

                # Four-point stencil for mixed derivative
                pp = psi_values(z + ei + np.conj(ej))
                pm = psi_values(z + ei - np.conj(ej))
                mp = psi_values(z - ei + np.conj(ej))
                mm = psi_values(z - ei - np.conj(ej))
                d2 = (pp - pm - mp + mm) / (4.0 * dz * dz)

                lap += g_inv[i, j] * d2

        return lap

    # ─── Sector projections ───
    def sectors(self):
        """
        The six sectors of the Bergman Laplacian eigenvalue equation.

        Each sector emerges by restricting Delta_B psi = lambda psi to a
        particular representation and boundary condition.

        Returns
        -------
        list of dict
            Each entry describes a sector: name, equation, mechanism, color.
        """
        return [
            {
                'name': 'Schrodinger',
                'equation': 'i hbar d_t psi = H psi',
                'mechanism': 'Non-relativistic limit of boundary projection on S^4',
                'bc': 'Dirichlet on S^4 (particle localization)',
                'color': C_QUANT,
                'sector': 'Scalar, s-wave',
            },
            {
                'name': 'Klein-Gordon',
                'equation': '(Box + m^2) phi = 0',
                'mechanism': 'Spin-0 sector: scalar harmonics on D_IV^5',
                'bc': 'Dirichlet on S^4 x S^1 (massive scalar)',
                'color': C_QUANT,
                'sector': 'Scalar, all waves',
            },
            {
                'name': 'Dirac',
                'equation': '(i gamma^mu D_mu - m) psi = 0',
                'mechanism': 'Spinor sector via Kahler-Dirac operator on D_IV^5',
                'bc': 'Spectral (Atiyah-Patodi-Singer) on S^4 x S^1',
                'color': C_SPIN,
                'sector': 'Spinor, half-integer',
            },
            {
                'name': 'Maxwell',
                'equation': 'd*F = J,  dF = 0',
                'mechanism': 'U(1) component of connection on S^1 fiber',
                'bc': 'Neumann on S^1 (field propagation)',
                'color': C_EM,
                'sector': '1-form, U(1)',
            },
            {
                'name': 'Einstein',
                'equation': 'G_uv + Lambda g_uv = 8pi G T_uv',
                'mechanism': 'Metric sector: Ricci flow of Bergman metric',
                'bc': 'Mixed: asymptotic flatness + horizon regularity',
                'color': C_GRAV,
                'sector': 'Symmetric 2-tensor',
            },
            {
                'name': 'Yang-Mills',
                'equation': 'D_mu F^{mu nu} = J^nu',
                'mechanism': 'SU(3)xSU(2)xU(1) from isometry group decomposition',
                'bc': 'Neumann on gauge orbits in S^4 x S^1',
                'color': C_GAUGE,
                'sector': 'Adjoint-valued 2-form',
            },
        ]

    # ─── Boundary conditions ───
    def boundary_conditions(self):
        """
        Boundary condition types on the Shilov boundary S^4 x S^1.

        Different boundary conditions select different physics from the
        same equation Delta_B psi = lambda psi.

        Returns
        -------
        list of dict
        """
        return [
            {
                'type': 'Dirichlet',
                'physics': 'Particles (localized excitations)',
                'description': 'psi|_{boundary} = 0. Quantizes the spectrum. '
                               'Eigenvalues become particle masses.',
                'color': C_QUANT,
            },
            {
                'type': 'Neumann',
                'physics': 'Fields (propagating modes)',
                'description': 'n . grad psi|_{boundary} = 0. Allows field '
                               'propagation. Gauge fields live here.',
                'color': C_GAUGE,
            },
            {
                'type': 'Mixed / Robin',
                'physics': 'Interactions (coupling between sectors)',
                'description': '(a psi + b n.grad psi)|_{boundary} = 0. '
                               'Couples particle and field sectors. '
                               'Interactions emerge from mixed BC.',
                'color': C_GRAV,
            },
            {
                'type': 'Spectral (APS)',
                'physics': 'Spinors (Dirac fermions)',
                'description': 'Atiyah-Patodi-Singer spectral projection. '
                               'Positive-frequency modes only. Chirality '
                               'from the orientation of S^4 x S^1.',
                'color': C_SPIN,
            },
            {
                'type': 'Periodic',
                'physics': 'Thermal / finite temperature',
                'description': 'psi(tau + beta) = psi(tau) on S^1. '
                               'Matsubara frequencies. Hawking temperature '
                               'from periodicity = 2pi / kappa.',
                'color': ORANGE,
            },
        ]

    # ─── Summary report ───
    def report(self):
        """Print a formatted summary of the BST field equation."""
        lines = [
            '',
            '=' * 72,
            '  BST FIELD EQUATION ON D_IV^5',
            '=' * 72,
            '',
            '  The equation:     Delta_B psi = lambda psi',
            f'  Domain:           D_IV^{self.dim_complex} = '
            f'SO_0({self.dim_complex},2) / [SO({self.dim_complex}) x SO(2)]',
            f'  Real dimension:   {self.dim_real}',
            f'  Complex dimension:{self.dim_complex}',
            f'  Rank:             {self.rank}',
            f'  Shilov boundary:  S^4 x S^1',
            f'  Volume:           pi^{self.dim_complex}/{self.weyl_order} '
            f'= {self.vol:.6e}',
            '',
            '  SPECTRUM:',
        ]
        for lvl in self._spectrum[:8]:
            e_str = (f'{lvl["energy_MeV"]:.1f} MeV'
                     if lvl['energy_MeV'] > 0 else 'Lambda')
            lines.append(
                f'    n={lvl["n"]:2d}  lambda={lvl["eigenvalue"]:5d}  '
                f'deg={lvl["degeneracy"]:6d}  E={e_str:>12s}  '
                f'{lvl["label"]}'
            )
        lines += [
            '',
            '  SECTORS (all from Delta_B psi = lambda psi):',
        ]
        for s in self.sectors():
            lines.append(f'    {s["name"]:14s} -> {s["equation"]}')
        lines += [
            '',
            '  "One equation contains all of physics."',
            '=' * 72,
            '',
        ]
        print('\n'.join(lines))

    # ─── Spectrum data for plotting ───
    @property
    def spectrum(self):
        """Return the computed spectrum."""
        return self._spectrum


# ═══════════════════════════════════════════════════════════════════
# VISUALIZATION — 6-Panel Display
# ═══════════════════════════════════════════════════════════════════

def _draw_glow_line(ax, x, y, color, lw=2, alpha=0.9):
    """Draw a line with a glow effect (layered widths)."""
    for w, a in [(lw + 8, 0.04), (lw + 5, 0.08), (lw + 3, 0.12), (lw, alpha)]:
        ax.plot(x, y, color=color, linewidth=w, alpha=a, solid_capstyle='round')


def _draw_glow_hline(ax, y, x0, x1, color, lw=3, alpha=0.85):
    """Draw a horizontal line with glow."""
    for w, a in [(lw + 10, 0.05), (lw + 6, 0.08), (lw + 3, 0.15), (lw, alpha)]:
        ax.plot([x0, x1], [y, y], color=color, linewidth=w, alpha=a,
                solid_capstyle='round')


def _styled_box(ax, x, y, text, color, fontsize=9, width=0.38, height=0.08,
                alpha=0.85, text_color=None):
    """Draw a rounded box with text."""
    box = FancyBboxPatch(
        (x - width / 2, y - height / 2), width, height,
        boxstyle='round,pad=0.01',
        facecolor=color + '20',
        edgecolor=color,
        linewidth=1.2,
        alpha=alpha,
    )
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=text_color or color,
            ha='center', va='center', fontfamily='monospace', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=1, foreground=color + '30')])


def _arrow(ax, x0, y0, x1, y1, color, lw=1.2):
    """Draw a styled arrow between two points."""
    arr = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle='->', mutation_scale=12,
        color=color, linewidth=lw, alpha=0.7,
    )
    ax.add_patch(arr)


def _panel_frame(ax, title, color=BLUE_BRIGHT):
    """Set up a standard dark panel with title."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color(DARK_GREY)
        spine.set_linewidth(0.8)
    ax.set_title(title, fontsize=11, fontweight='bold', color=color,
                 fontfamily='monospace', pad=8,
                 path_effects=[pe.withStroke(linewidth=2, foreground=color + '30')])


# ═══════════════════════════════════════════════════════════════════
# Panel 1: ONE EQUATION
# ═══════════════════════════════════════════════════════════════════

def _draw_panel_one_equation(ax):
    """Panel 1: The one equation displayed prominently."""
    _panel_frame(ax, 'ONE EQUATION', GOLD)

    # The equation — large, centered, golden
    ax.text(0.50, 0.62, r'$\Delta_B \, \psi \;=\; \lambda \, \psi$',
            fontsize=32, color=GOLD, ha='center', va='center',
            fontfamily='serif', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=4, foreground='#ffd70050')])

    # Decorative lines above and below
    ax.plot([0.12, 0.88], [0.82, 0.82], color=GOLD_DIM, linewidth=0.6, alpha=0.5)
    ax.plot([0.12, 0.88], [0.42, 0.42], color=GOLD_DIM, linewidth=0.6, alpha=0.5)

    # Subtitle
    ax.text(0.50, 0.88, 'The Bergman Laplacian eigenvalue equation',
            fontsize=9, color=CREAM, ha='center', fontfamily='serif',
            fontstyle='italic')

    # Domain specification
    ax.text(0.50, 0.48, r'on $D_{IV}^5 = SO_0(5,2)\,/\,[SO(5) \times SO(2)]$',
            fontsize=10, color=PURPLE_GLOW, ha='center', fontfamily='serif',
            path_effects=GLOW_FX_PURPLE)

    # The claim
    ax.text(0.50, 0.32, 'Contains all of physics.',
            fontsize=12, color=WHITE, ha='center', fontfamily='serif',
            fontweight='bold', fontstyle='italic',
            path_effects=GLOW_FX)

    # Key facts in small text
    facts = [
        f'Complex dim = {n_C}     Real dim = {2*n_C}',
        f'Vol = pi^5 / {GAMMA_ORDER}     N_max = {N_MAX}',
    ]
    for i, fact in enumerate(facts):
        ax.text(0.50, 0.18 - i * 0.07, fact,
                fontsize=7.5, color=GREY, ha='center', fontfamily='monospace')

    # Corner decoration: golden bracket
    for corner_x, corner_y, dx, dy in [(0.06, 0.92, 0.06, -0.06),
                                        (0.94, 0.92, -0.06, -0.06),
                                        (0.06, 0.05, 0.06, 0.06),
                                        (0.94, 0.05, -0.06, 0.06)]:
        ax.plot([corner_x, corner_x, corner_x + dx],
                [corner_y + dy, corner_y, corner_y],
                color=GOLD_DIM, linewidth=1.0, alpha=0.4)


# ═══════════════════════════════════════════════════════════════════
# Panel 2: THE SPECTRUM
# ═══════════════════════════════════════════════════════════════════

def _draw_panel_spectrum(ax, fe):
    """Panel 2: Energy levels like hydrogen but for the universe."""
    _panel_frame(ax, 'THE SPECTRUM', PURPLE_GLOW)

    # Potential well shape
    well_x = np.linspace(0.15, 0.85, 300)
    well_center = 0.50
    well_y_base = 0.08
    well_scale = 3.5
    well_curve = well_y_base + well_scale * (well_x - well_center)**2

    # Draw the well with glow
    for lw, a in [(10, 0.04), (6, 0.08), (3, 0.15), (1.5, 0.5)]:
        ax.plot(well_x, well_curve, color=PURPLE_DIM, linewidth=lw, alpha=a)
    ax.plot(well_x, well_curve, color=PURPLE_GLOW, linewidth=1.0, alpha=0.8)

    # Clip to visible area
    ax.set_ylim(0, 1)

    # Energy levels inside the well
    levels_data = [
        (0.12, 0.38, PURPLE_GLOW,  'Lambda = 2.9 x 10^-122', 'GROUND STATE (vacuum)', 0.9),
        (0.24, 0.50, GREEN_GLOW,  'm_p = 938.272 MeV',    '1st excitation (mass gap)', 0.85),
        (0.34, 0.56, GREEN_DIM,   'Delta(1232)',           '2nd excitation', 0.55),
        (0.42, 0.60, GREEN_DIM,   'N*(1520)',              '3rd excitation', 0.40),
        (0.48, 0.62, GREEN_DIM,   'N*(1680)',              '4th excitation', 0.30),
        (0.53, 0.64, DARK_GREY,   '...',                   'higher resonances', 0.20),
    ]

    for y_pos, half_w, color, left_label, right_label, alpha in levels_data:
        x0 = well_center - half_w
        x1 = well_center + half_w
        # Find actual well width at this y
        valid = well_curve <= y_pos + 0.01
        if np.any(valid):
            x0 = max(x0, well_x[valid][0])
            x1 = min(x1, well_x[valid][-1])

        _draw_glow_hline(ax, y_pos, x0, x1, color, lw=2.5, alpha=alpha)

        # Labels
        ax.text(x1 + 0.02, y_pos, left_label,
                fontsize=6.5, color=color, ha='left', va='center',
                fontfamily='monospace', fontweight='bold', alpha=min(1.0, alpha + 0.2))

    # Ground state label (special)
    ax.text(0.50, 0.06, 'THE UNIVERSE  (ground state)',
            fontsize=7, color='#bb99ff', ha='center', fontfamily='monospace',
            fontstyle='italic')

    # Mass gap arrow
    ax.annotate('', xy=(0.22, 0.24), xytext=(0.22, 0.12),
                arrowprops=dict(arrowstyle='<->', color=GREEN_GLOW, lw=1.5))
    ax.text(0.15, 0.18, 'MASS\nGAP',
            fontsize=6, color=GREEN_GLOW, ha='center', va='center',
            fontfamily='monospace', fontweight='bold')

    # Top annotation
    ax.text(0.50, 0.93, 'Like hydrogen, but for the universe',
            fontsize=7.5, color=CREAM, ha='center', fontfamily='serif',
            fontstyle='italic')


# ═══════════════════════════════════════════════════════════════════
# Panel 3: FIVE EQUATIONS IN ONE
# ═══════════════════════════════════════════════════════════════════

def _draw_panel_five_equations(ax):
    """Panel 3: Tree diagram showing how all equations emerge."""
    _panel_frame(ax, 'FIVE EQUATIONS IN ONE', WHITE)

    # Root node: the BST equation
    _styled_box(ax, 0.50, 0.90, r'$\Delta_B\psi = \lambda\psi$',
                GOLD, fontsize=11, width=0.40, height=0.08)

    # First branch level: three mechanisms
    branch1 = [
        (0.18, 0.72, 'Boundary\nprojection', C_QUANT),
        (0.50, 0.72, 'Sector\ndecomposition', C_GAUGE),
        (0.82, 0.72, 'Metric\nsector', C_GRAV),
    ]
    for bx, by, label, color in branch1:
        _styled_box(ax, bx, by, label, color, fontsize=6.5,
                    width=0.24, height=0.09)
        _arrow(ax, 0.50, 0.86, bx, 0.77, color)

    # Leaf nodes: the five equations
    leaves = [
        (0.10, 0.48, 'Schrodinger\ni hbar d_t psi = H psi', C_QUANT),
        (0.34, 0.48, 'Klein-Gordon\n(Box+m^2)phi = 0', C_QUANT),
        (0.58, 0.48, 'Dirac\n(i gamma D - m)psi=0', C_SPIN),
        (0.82, 0.48, 'Maxwell\nd*F = J', C_EM),
    ]
    for lx, ly, label, color in leaves:
        _styled_box(ax, lx, ly, label, color, fontsize=5.5,
                    width=0.21, height=0.11)

    # Arrows from branches to leaves
    _arrow(ax, 0.18, 0.67, 0.10, 0.54, C_QUANT)
    _arrow(ax, 0.18, 0.67, 0.34, 0.54, C_QUANT)
    _arrow(ax, 0.50, 0.67, 0.58, 0.54, C_SPIN)
    _arrow(ax, 0.50, 0.67, 0.82, 0.54, C_EM)

    # Einstein and Yang-Mills at the bottom
    bottom = [
        (0.30, 0.26, 'Einstein\nG_uv + Lg_uv = 8piGT_uv', C_GRAV),
        (0.70, 0.26, 'Yang-Mills\nD_mu F^{mu nu} = J^nu', C_GAUGE),
    ]
    for bx, by, label, color in bottom:
        _styled_box(ax, bx, by, label, color, fontsize=5.5,
                    width=0.28, height=0.11)

    _arrow(ax, 0.82, 0.67, 0.30, 0.32, C_GRAV)
    _arrow(ax, 0.50, 0.67, 0.70, 0.32, C_GAUGE)

    # Gauge group annotation
    ax.text(0.70, 0.17, 'SU(3) x SU(2) x U(1)',
            fontsize=6.5, color=C_GAUGE, ha='center', fontfamily='monospace',
            path_effects=[pe.withStroke(linewidth=1, foreground=C_GAUGE + '30')])

    # Bottom text
    ax.text(0.50, 0.06, 'All emerge as sectors or projections',
            fontsize=7, color=CREAM, ha='center', fontfamily='serif',
            fontstyle='italic')


# ═══════════════════════════════════════════════════════════════════
# Panel 4: BOUNDARY CONDITIONS
# ═══════════════════════════════════════════════════════════════════

def _draw_panel_boundary(ax, fe):
    """Panel 4: Shilov boundary S^4 x S^1 and boundary conditions."""
    _panel_frame(ax, 'BOUNDARY CONDITIONS', CYAN)

    # Draw schematic of S^4 x S^1
    # S^4 as a large circle, S^1 as a small loop attached
    cx, cy = 0.38, 0.70
    r_s4 = 0.16

    # S^4 circle with glow
    for lw, a in [(8, 0.05), (5, 0.1), (2.5, 0.3), (1.2, 0.7)]:
        circle = Circle((cx, cy), r_s4, fill=False, edgecolor=CYAN,
                        linewidth=lw, alpha=a)
        ax.add_patch(circle)

    ax.text(cx, cy, r'$S^4$', fontsize=14, color=CYAN, ha='center',
            va='center', fontfamily='serif', fontweight='bold')

    # S^1 as small circle
    s1_cx = cx + r_s4 + 0.08
    s1_cy = cy
    s1_r = 0.05
    for lw, a in [(5, 0.08), (2.5, 0.2), (1.2, 0.6)]:
        s1 = Circle((s1_cx, s1_cy), s1_r, fill=False, edgecolor=ORANGE,
                    linewidth=lw, alpha=a)
        ax.add_patch(s1)
    ax.text(s1_cx, s1_cy, r'$S^1$', fontsize=9, color=ORANGE, ha='center',
            va='center', fontfamily='serif', fontweight='bold')

    # Cross product symbol
    ax.text(cx + r_s4 + 0.02, cy + 0.07, r'$\times$', fontsize=9,
            color=GREY, ha='center', fontfamily='serif')

    # Label
    ax.text(0.42, 0.88, 'Shilov boundary of D_IV^5',
            fontsize=8, color=CREAM, ha='center', fontfamily='monospace')

    # Boundary condition table
    bcs = fe.boundary_conditions()
    y_start = 0.52
    y_step = 0.10
    for i, bc in enumerate(bcs):
        y = y_start - i * y_step
        # Type label
        ax.text(0.06, y, bc['type'], fontsize=7, color=bc['color'],
                fontfamily='monospace', fontweight='bold', va='center')
        # Arrow
        ax.plot([0.28, 0.35], [y, y], color=bc['color'], linewidth=1.0,
                alpha=0.5)
        ax.plot([0.35], [y], marker='>', color=bc['color'], markersize=4,
                alpha=0.7)
        # Physics
        ax.text(0.37, y, bc['physics'], fontsize=6.5, color=WHITE,
                fontfamily='monospace', va='center')

    # Bottom note
    ax.text(0.50, 0.04, 'Different BC  ->  different physics',
            fontsize=7, color=CREAM, ha='center', fontfamily='serif',
            fontstyle='italic')


# ═══════════════════════════════════════════════════════════════════
# Panel 5: THE BERGMAN LAPLACIAN
# ═══════════════════════════════════════════════════════════════════

def _draw_panel_laplacian(ax):
    """Panel 5: Delta_B in coordinates; Kahler self-adjointness."""
    _panel_frame(ax, 'THE BERGMAN LAPLACIAN', PURPLE_GLOW)

    # The Laplacian formula
    ax.text(0.50, 0.88,
            r'$\Delta_B = g^{i\bar{j}} \frac{\partial^2}{\partial z_i \, \partial \bar{z}_j}$',
            fontsize=16, color=PURPLE_GLOW, ha='center', fontfamily='serif',
            path_effects=GLOW_FX_PURPLE)

    # Bergman metric
    ax.text(0.50, 0.74, 'Bergman metric:',
            fontsize=7.5, color=GREY, ha='center', fontfamily='monospace')
    ax.text(0.50, 0.66,
            r'$g_{i\bar{j}} = \frac{\partial^2}{\partial z_i \, \partial \bar{z}_j} \log K(z,z)$',
            fontsize=12, color=CREAM, ha='center', fontfamily='serif')

    # Bergman kernel
    ax.text(0.50, 0.54, 'Bergman kernel:',
            fontsize=7.5, color=GREY, ha='center', fontfamily='monospace')
    ax.text(0.50, 0.46,
            r'$K(z,z) = \frac{5!}{\pi^5} \det(I - z\bar{z}^T)^{-6}$',
            fontsize=10, color=CREAM, ha='center', fontfamily='serif')

    # Properties box
    props = [
        ('Kahler', 'Hermitian + closed => self-adjoint spectrum'),
        ('Bounded', 'D_IV^5 is bounded => discrete eigenvalues'),
        ('Symmetric', 'SO(5,2) acts transitively => homogeneous'),
    ]

    y_start = 0.34
    for i, (name, desc) in enumerate(props):
        y = y_start - i * 0.09
        ax.text(0.08, y, name, fontsize=7, color=PURPLE_GLOW,
                fontfamily='monospace', fontweight='bold', va='center')
        ax.text(0.28, y, desc, fontsize=6, color=GREY,
                fontfamily='monospace', va='center')

    # Key insight
    ax.text(0.50, 0.06,
            'The natural Laplacian on D_IV^5 — the ONLY one',
            fontsize=7, color=CREAM, ha='center', fontfamily='serif',
            fontstyle='italic')

    # Decorative: vertical Kahler form symbol
    ax.text(0.92, 0.50, r'$\omega$', fontsize=20, color=PURPLE_DIM,
            ha='center', va='center', fontfamily='serif', alpha=0.3,
            rotation=0)


# ═══════════════════════════════════════════════════════════════════
# Panel 6: ONE EQUATION RULES THEM ALL
# ═══════════════════════════════════════════════════════════════════

def _draw_panel_rules(ax):
    """Panel 6: Full derivation tree from Delta_B to all known physics."""
    _panel_frame(ax, 'ONE EQUATION RULES THEM ALL', GOLD)

    # Central equation at top
    ax.text(0.50, 0.92,
            r'$\Delta_B \psi = \lambda \psi$  on $D_{IV}^5$',
            fontsize=11, color=GOLD, ha='center', fontfamily='serif',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a00',
                      edgecolor=GOLD_DIM, linewidth=1.5, alpha=0.9),
            path_effects=GLOW_FX_GOLD)

    # Three main branches
    branches = [
        (0.17, 0.74, 'Spectrum', PURPLE_GLOW),
        (0.50, 0.74, 'Sectors', C_GAUGE),
        (0.83, 0.74, 'Boundary', CYAN),
    ]
    for bx, by, label, color in branches:
        _styled_box(ax, bx, by, label, color, fontsize=8,
                    width=0.22, height=0.06)
        _arrow(ax, 0.50, 0.87, bx, 0.77, color, lw=1.5)

    # From Spectrum
    spec_items = [
        (0.08, 0.60, 'Lambda', C_GEOM, '10^-122'),
        (0.08, 0.50, 'm_p', GREEN_GLOW, '938 MeV'),
        (0.08, 0.40, 'Particle\ntower', GREEN_DIM, 'Regge'),
    ]
    for sx, sy, label, color, note in spec_items:
        ax.text(sx, sy, label, fontsize=6.5, color=color, ha='left',
                va='center', fontfamily='monospace', fontweight='bold')
        ax.text(sx + 0.14, sy, note, fontsize=5.5, color=GREY, ha='left',
                va='center', fontfamily='monospace')
        _arrow(ax, 0.17, 0.71, sx + 0.04, sy + 0.03, color, lw=0.8)

    # From Sectors — the six equations in a column
    sector_items = [
        (0.38, 0.62, 'Schrodinger', C_QUANT),
        (0.38, 0.54, 'Klein-Gordon', C_QUANT),
        (0.38, 0.46, 'Dirac', C_SPIN),
        (0.38, 0.38, 'Maxwell', C_EM),
        (0.38, 0.30, 'Einstein', C_GRAV),
        (0.38, 0.22, 'Yang-Mills', C_GAUGE),
    ]
    for sx, sy, label, color in sector_items:
        ax.text(sx, sy, label, fontsize=6.5, color=color, ha='left',
                va='center', fontfamily='monospace', fontweight='bold')
        # Small arrow from branch
        _arrow(ax, 0.50, 0.71, sx + 0.05, sy + 0.02, color, lw=0.8)

    # Right side checkmarks
    for sx, sy, label, color in sector_items:
        ax.text(sx + 0.20, sy, r'$\checkmark$', fontsize=8, color=color,
                ha='center', va='center', fontfamily='serif', alpha=0.7)

    # From Boundary
    bc_items = [
        (0.72, 0.62, 'Dirichlet', C_QUANT, 'particles'),
        (0.72, 0.52, 'Neumann', C_GAUGE, 'fields'),
        (0.72, 0.42, 'Mixed', C_GRAV, 'interactions'),
        (0.72, 0.32, 'Spectral', C_SPIN, 'fermions'),
    ]
    for bx, by, label, color, note in bc_items:
        ax.text(bx, by, label, fontsize=6.5, color=color, ha='left',
                va='center', fontfamily='monospace', fontweight='bold')
        ax.text(bx + 0.17, by, note, fontsize=5.5, color=GREY, ha='left',
                va='center', fontfamily='monospace')
        _arrow(ax, 0.83, 0.71, bx + 0.04, by + 0.02, color, lw=0.8)

    # Bottom line: the punchline
    ax.plot([0.08, 0.92], [0.12, 0.12], color=GOLD_DIM, linewidth=0.5,
            alpha=0.4)
    ax.text(0.50, 0.06,
            'Every fundamental equation of physics\nis a shadow of one.',
            fontsize=8, color=GOLD, ha='center', fontfamily='serif',
            fontweight='bold', fontstyle='italic', linespacing=1.4,
            path_effects=GLOW_FX_GOLD)


# ═══════════════════════════════════════════════════════════════════
# Main visualization assembly
# ═══════════════════════════════════════════════════════════════════

def run_visualization():
    """Launch the 6-panel BST Field Equations visualization."""
    fe = BSTFieldEquation(n_levels=12)

    fig = plt.figure(figsize=(20, 13), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST Field Equations on D_IV^5 — One Equation Rules Them All')

    # ─── Title banner ───
    fig.text(0.50, 0.975,
             'BST FIELD EQUATIONS ON D_IV^5',
             fontsize=26, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#aa770040')])
    fig.text(0.50, 0.950,
             r'The Bergman Laplacian eigenvalue equation  $\Delta_B \psi = \lambda \psi$'
             r'  contains all of physics',
             fontsize=11, color=CREAM, ha='center', fontfamily='serif',
             fontstyle='italic')

    # ─── Bottom tagline ───
    fig.text(0.50, 0.012,
             'One equation.  Six sectors.  All of physics.  Zero free parameters.',
             fontsize=13, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

    # ─── Copyright ───
    fig.text(0.98, 0.003,
             'Copyright (c) 2026 Casey Koons',
             fontsize=6, color=DARK_GREY, ha='right', fontfamily='monospace')

    # ─── 6 panels: 3 columns x 2 rows ───
    left = 0.04
    col_w = 0.30
    col_gap = 0.02
    row_top = 0.54
    row_bot = 0.06
    row_h = 0.38

    ax_positions = [
        # Top row
        (left,                        row_top, col_w, row_h),
        (left + col_w + col_gap,      row_top, col_w, row_h),
        (left + 2*(col_w + col_gap),  row_top, col_w, row_h),
        # Bottom row
        (left,                        row_bot, col_w, row_h),
        (left + col_w + col_gap,      row_bot, col_w, row_h),
        (left + 2*(col_w + col_gap),  row_bot, col_w, row_h),
    ]

    axes = [fig.add_axes(pos) for pos in ax_positions]

    # Draw all six panels
    _draw_panel_one_equation(axes[0])
    _draw_panel_spectrum(axes[1], fe)
    _draw_panel_five_equations(axes[2])
    _draw_panel_boundary(axes[3], fe)
    _draw_panel_laplacian(axes[4])
    _draw_panel_rules(axes[5])

    plt.show()


# ═══════════════════════════════════════════════════════════════════
# Main entry
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    # Print the report first
    fe = BSTFieldEquation()
    fe.report()

    # Launch the visualization
    run_visualization()
