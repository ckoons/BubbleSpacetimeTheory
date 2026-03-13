#!/usr/bin/env python3
"""
BLACK HOLES WITHOUT SINGULARITIES — BST Membrane Physics
==========================================================
In BST, black holes are not bottomless pits. They are FULL channels.

When density reaches ρ₁₃₇ (the Haldane cap), all 137 channels per contact
are saturated. Time stops. No singularity forms — just a maximally
committed membrane where:

    N(ρ) = N₀ √(1 − ρ/ρ₁₃₇) → 0

No singularity. No interior. No information paradox. Just a full channel.

The horizon is never crossed — the infalling observer's own clock is
governed by the same lapse function. Their time slows asymptotically.
They never arrive.

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
from matplotlib.widgets import Slider
from matplotlib.patches import Circle, FancyBboxPatch, Wedge, FancyArrowPatch
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors

# ═══════════════════════════════════════════════════════════════════
# BST Constants
# ═══════════════════════════════════════════════════════════════════
N_c = 3          # color charges
n_C = 5          # domain dimension
N_MAX = 137      # Haldane channel cap
C_2 = 6          # Casimir invariant
GENUS = 7        # genus of D_IV^5
BUDGET = 9.0 / 5.0            # N_c^2 / n_C
FILL = 3.0 / (5.0 * np.pi)   # N_c / (n_C * pi) ~ 0.191

# Physical constants (SI)
G_SI = 6.674e-11        # m^3 kg^-1 s^-2
c_SI = 2.998e8           # m/s
hbar_SI = 1.055e-34      # J s
k_B = 1.381e-23          # J/K
M_SUN = 1.989e30         # kg
l_Pl = 1.616e-35         # m
m_Pl = 2.176e-8          # kg
t_Pl = 5.391e-44         # s
YEAR = 3.156e7           # seconds

# ─── Colors ───
BG = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
BLUE_GLOW = '#4488ff'
BLUE_BRIGHT = '#00ccff'
BLUE_DEEP = '#1a1a6a'
PURPLE_GLOW = '#8844cc'
ORANGE_GLOW = '#ff8800'
RED_WARM = '#ff4444'
RED_DEEP = '#cc2200'
WHITE = '#ffffff'
GREY = '#888888'
DARK_GREY = '#444444'
GREEN = '#44ff88'


# ═══════════════════════════════════════════════════════════════════
# BSTBlackHole — Programmatic CI-scriptable API
# ═══════════════════════════════════════════════════════════════════

class BSTBlackHole:
    """
    A BST black hole: no singularity, no interior, no information paradox.

    The black hole is a maximally committed membrane where density
    saturates at ρ₁₃₇ and the lapse function N → 0.

    Parameters
    ----------
    M_solar : float
        Mass in solar masses (default 10.0).
    """

    def __init__(self, M_solar=10.0):
        self.M_solar = M_solar
        self.M_kg = M_solar * M_SUN
        # Schwarzschild radius
        self.r_s = 2.0 * G_SI * self.M_kg / c_SI**2
        # Horizon area
        self.A_horizon = 4.0 * np.pi * self.r_s**2

    # ─── Lapse function ───
    def lapse(self, rho):
        """
        Lapse function N = N₀ √(1 − ρ/ρ₁₃₇).

        Parameters
        ----------
        rho : float or array
            Density as fraction of ρ₁₃₇ (0 to 1).

        Returns
        -------
        float or array
            Lapse value(s), 0 ≤ N ≤ 1.
        """
        rho = np.asarray(rho, dtype=float)
        return np.sqrt(np.clip(1.0 - rho, 0.0, 1.0))

    # ─── Density profile ───
    def density_profile(self, r_array):
        """
        Density profile ρ(r)/ρ₁₃₇ near the horizon.

        Models the approach to saturation as r → r_s:
            ρ/ρ₁₃₇ = 1 / (1 + (r/r_s − 1)²)^{1/2}

        At r = r_s: ρ = ρ₁₃₇ (saturated).
        Far from horizon: ρ → 0.

        Parameters
        ----------
        r_array : array
            Radial coordinate(s) in meters.

        Returns
        -------
        np.ndarray
            ρ/ρ₁₃₇ at each radius.
        """
        r_array = np.asarray(r_array, dtype=float)
        x = r_array / self.r_s - 1.0  # distance from horizon in units of r_s
        x = np.clip(x, 0.0, None)
        rho_frac = 1.0 / np.sqrt(1.0 + x**2)
        return rho_frac

    # ─── Hawking temperature ───
    def hawking_temperature(self):
        """
        BST vs standard Hawking temperature.

        Standard:  T_H = ℏ c³ / (8π G M k_B)
        BST:       T_BST = ℏ c³ / (2√137 G M k_B)
        Scale ratio: 2√137 / (8π) = 0.931  →  7% geometric correction

        Since 2√137 < 8π, BST predicts slightly higher temperature than
        standard Hawking. The structural ratio 2√137/(8π) = 0.931 means
        a 7% gap from the near-horizon density profile geometry.

        Returns
        -------
        dict with keys:
            'T_hawking_K'    : standard Hawking temperature (Kelvin)
            'T_bst_K'        : BST temperature (Kelvin)
            'scale_ratio'    : 2√137/(8π) = 0.931
            'T_ratio'        : T_BST / T_Hawking (= 1/scale_ratio)
            'match_pct'      : percentage match (93.1%)
        """
        T_H = hbar_SI * c_SI**3 / (8.0 * np.pi * G_SI * self.M_kg * k_B)
        T_BST = hbar_SI * c_SI**3 / (2.0 * np.sqrt(N_MAX) * G_SI * self.M_kg * k_B)
        scale_ratio = 2.0 * np.sqrt(N_MAX) / (8.0 * np.pi)  # 0.931
        return {
            'T_hawking_K': T_H,
            'T_bst_K': T_BST,
            'scale_ratio': scale_ratio,
            'T_ratio': T_BST / T_H,
            'match_pct': scale_ratio * 100.0,
        }

    # ─── Bekenstein-Hawking entropy ───
    def bekenstein_entropy(self):
        """
        S = A / (4 l_Pl²) in natural units.

        The factor of 4: each contact occupies 4 Planck areas
        (2 complex dimensions x 2 real each).

        Returns
        -------
        float
            Dimensionless entropy.
        """
        return self.A_horizon / (4.0 * l_Pl**2)

    # ─── Contacts on horizon ───
    def contacts_on_horizon(self):
        """
        Number of committed contacts on the horizon surface.

        Each contact occupies 4 l_Pl² → N_contacts = A / (4 l_Pl²) = S_BH.

        Returns
        -------
        float
            Number of contacts.
        """
        return self.bekenstein_entropy()

    # ─── Evaporation time ───
    def evaporation_time(self):
        """
        Time for complete evaporation via Hawking radiation (in years).

        t_evap = 5120 π G² M³ / (ℏ c⁴)

        Returns
        -------
        float
            Evaporation time in years.
        """
        t_s = 5120.0 * np.pi * G_SI**2 * self.M_kg**3 / (hbar_SI * c_SI**4)
        return t_s / YEAR

    # ─── Singularity check ───
    def is_singular(self):
        """Always returns False. BST has no singularities."""
        return False

    # ─── Interior check ───
    def has_interior(self):
        """Always returns False. BST black holes are membranes, not volumes."""
        return False

    # ─── Membrane properties ───
    def membrane_properties(self):
        """
        Properties of the maximally committed membrane.

        Returns
        -------
        dict
            Membrane radius, area, density, lapse, channels, entropy,
            temperature, evaporation time, and information capacity.
        """
        temps = self.hawking_temperature()
        return {
            'r_membrane_m': self.r_s,
            'r_membrane_km': self.r_s / 1e3,
            'area_m2': self.A_horizon,
            'density_frac': 1.0,  # ρ/ρ₁₃₇ = 1 at membrane
            'lapse': 0.0,         # N = 0 at membrane
            'channels_per_contact': N_MAX,
            'channels_saturated': True,
            'entropy': self.bekenstein_entropy(),
            'contacts': self.contacts_on_horizon(),
            'T_hawking_K': temps['T_hawking_K'],
            'T_bst_K': temps['T_bst_K'],
            'evaporation_years': self.evaporation_time(),
            'info_bits': self.bekenstein_entropy() * np.log(2),
        }

    # ─── Two endpoints comparison ───
    def compare_endpoints(self):
        """
        Compare the two endpoints of the density spectrum:
        First Commitment (ρ=0) vs Black Hole (ρ=ρ₁₃₇).

        Returns
        -------
        dict with 'first_commitment' and 'black_hole' sub-dicts.
        """
        return {
            'first_commitment': {
                'density': 'rho = 0 (empty)',
                'lapse': 'N = N_0 (max clock rate)',
                'commitments': 'N ~ 2 (minimum)',
                'fill_fraction': 'f -> 0 (locally)',
                'status': 'Unstable',
                'description': 'The first contact — substrate awakens',
            },
            'black_hole': {
                'density': 'rho = rho_137 (full)',
                'lapse': 'N = 0 (frozen)',
                'commitments': f'N = S_BH = {self.bekenstein_entropy():.2e} (maximum local)',
                'fill_fraction': 'f = 1 (locally, 100%)',
                'status': 'Stable (until evaporation)',
                'description': 'Hard drive full — data preserved, no new writes',
            },
        }

    # ─── Pretty report ───
    def report(self):
        """Print a formatted summary of this BST black hole."""
        props = self.membrane_properties()
        temps = self.hawking_temperature()
        lines = [
            '',
            '=' * 68,
            f'  BST BLACK HOLE — {self.M_solar:.1f} Solar Masses',
            '=' * 68,
            '',
            f'  Mass:                 {self.M_solar:.1f} M_sun = {self.M_kg:.3e} kg',
            f'  Membrane radius:      {props["r_membrane_km"]:.2f} km',
            f'  Horizon area:         {props["area_m2"]:.3e} m^2',
            '',
            f'  Singular?             {self.is_singular()}',
            f'  Has interior?         {self.has_interior()}',
            f'  Density at membrane:  rho / rho_137 = {props["density_frac"]}',
            f'  Lapse at membrane:    N = {props["lapse"]}',
            f'  Channels saturated:   {props["channels_saturated"]}',
            '',
            f'  Bekenstein entropy:   {props["entropy"]:.3e}',
            f'  Contacts on horizon:  {props["contacts"]:.3e}',
            f'  Info capacity:        {props["info_bits"]:.3e} bits',
            '',
            f'  Hawking T (standard): {temps["T_hawking_K"]:.4e} K',
            f'  Hawking T (BST):      {temps["T_bst_K"]:.4e} K',
            f'  Scale ratio 2√137/(8π): {temps["scale_ratio"]:.4f}  ({temps["match_pct"]:.1f}% match)',
            '',
            f'  Evaporation time:     {self.evaporation_time():.3e} years',
            '',
            '  "No singularity. No interior. No information paradox."',
            '  "Just a full channel."',
            '=' * 68,
            '',
        ]
        print('\n'.join(lines))


# ═══════════════════════════════════════════════════════════════════
# VISUALIZATION HELPERS
# ═══════════════════════════════════════════════════════════════════

def density_to_color(rho_frac):
    """Map ρ/ρ₁₃₇ to a color: blue (empty) → red (near full) → black (saturated)."""
    t = np.clip(rho_frac, 0.0, 1.0)
    if t < 0.4:
        s = t / 0.4
        r = 0.05 + 0.15 * s
        g = 0.2 + 0.3 * s
        b = 0.9 - 0.1 * s
    elif t < 0.7:
        s = (t - 0.4) / 0.3
        r = 0.2 + 0.6 * s
        g = 0.5 + 0.2 * s - 0.4 * s
        b = 0.8 - 0.6 * s
    elif t < 0.95:
        s = (t - 0.7) / 0.25
        r = 0.8 + 0.2 * s
        g = 0.3 - 0.25 * s
        b = 0.2 - 0.15 * s
    else:
        s = (t - 0.95) / 0.05
        r = 1.0 - 0.8 * s
        g = 0.05 - 0.05 * s
        b = 0.05 - 0.05 * s
    return (r, g, b)


def format_sci(val, unit=''):
    """Format a number in scientific notation for display."""
    if abs(val) == 0:
        return f'0 {unit}'.strip()
    exp = int(np.floor(np.log10(abs(val))))
    mantissa = val / 10**exp
    if unit:
        return f'{mantissa:.2f} x 10^{exp} {unit}'
    return f'{mantissa:.2f} x 10^{exp}'


# ═══════════════════════════════════════════════════════════════════
# VISUALIZATION — 3 panels + mass slider
# ═══════════════════════════════════════════════════════════════════

def run_visualization():
    """Launch the interactive 3-panel BST black hole visualization."""

    # Initial state
    M_init = 10.0
    bh = BSTBlackHole(M_init)

    fig = plt.figure(figsize=(20, 13), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'Black Holes Without Singularities — BST Membrane Physics')

    # ─── Title ───
    fig.text(0.5, 0.975, 'BLACK HOLES WITHOUT SINGULARITIES',
             fontsize=26, fontweight='bold', color=BLUE_BRIGHT, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#003366')])
    fig.text(0.5, 0.950, 'BST Membrane Physics — The Haldane Cap at N_max = 137',
             fontsize=13, color='#5599bb', ha='center', fontfamily='monospace')

    # ─── Bottom tagline ───
    fig.text(0.5, 0.015,
             'No singularity.  No interior.  No information paradox.  Just a full channel.',
             fontsize=14, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

    # ═══════════════════════════════════════════════════════════════
    # LEFT PANEL — The Lapse Function
    # ═══════════════════════════════════════════════════════════════
    ax_lapse = fig.add_axes([0.05, 0.18, 0.28, 0.60])
    ax_lapse.set_facecolor(DARK_PANEL)

    ax_lapse.set_title('THE LAPSE FUNCTION', fontsize=14, fontweight='bold',
                        color=BLUE_BRIGHT, fontfamily='monospace', pad=12)

    # Density array
    rho = np.linspace(0, 1.0, 1000)
    N_vals = np.sqrt(np.clip(1.0 - rho, 0, 1))

    # Color-gradient fill under the curve
    for i in range(len(rho) - 1):
        c = density_to_color(rho[i])
        ax_lapse.fill_between(rho[i:i+2], 0, N_vals[i:i+2],
                               color=c, alpha=0.4)

    # Main curve
    ax_lapse.plot(rho, N_vals, color=WHITE, linewidth=2.5, zorder=5)

    # Position dot (will be updated by slider)
    pos_dot, = ax_lapse.plot([0.0], [1.0], 'o', color=GOLD, markersize=12,
                              zorder=10, markeredgecolor='white',
                              markeredgewidth=1.5)

    # Annotations at key densities
    annotations = [
        (0.0, 'Vacuum', BLUE_GLOW),
        (0.15, 'Ordinary\nmatter', '#44aaff'),
        (0.60, 'Neutron\nstar', ORANGE_GLOW),
        (0.95, 'Near\nhorizon', RED_WARM),
        (1.0, 'HORIZON\nN = 0', RED_DEEP),
    ]
    for rho_pos, label, color in annotations:
        N_val = np.sqrt(max(0, 1 - rho_pos))
        ax_lapse.annotate(label, xy=(rho_pos, N_val),
                           xytext=(rho_pos, N_val + 0.12),
                           fontsize=7, color=color, ha='center',
                           fontfamily='monospace', fontweight='bold',
                           arrowprops=dict(arrowstyle='->', color=color,
                                           lw=1.0),
                           zorder=6)

    ax_lapse.set_xlabel('ρ / ρ₁₃₇', fontsize=12, color=WHITE,
                         fontfamily='monospace')
    ax_lapse.set_ylabel('Lapse  N / N₀', fontsize=12, color=WHITE,
                         fontfamily='monospace')
    ax_lapse.set_xlim(-0.02, 1.05)
    ax_lapse.set_ylim(-0.05, 1.25)
    ax_lapse.tick_params(colors=GREY, labelsize=9)
    for spine in ax_lapse.spines.values():
        spine.set_color(DARK_GREY)

    # Formula
    ax_lapse.text(0.50, 1.18, 'N = N₀ √(1 − ρ/ρ₁₃₇)',
                   fontsize=13, color=GOLD, ha='center',
                   fontfamily='monospace', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a00',
                             edgecolor=GOLD_DIM, alpha=0.8))

    # ═══════════════════════════════════════════════════════════════
    # CENTER PANEL — GR vs BST comparison
    # ═══════════════════════════════════════════════════════════════
    ax_compare = fig.add_axes([0.37, 0.18, 0.30, 0.60])
    ax_compare.set_facecolor(DARK_PANEL)
    ax_compare.set_xlim(0, 10)
    ax_compare.set_ylim(0, 10)
    ax_compare.set_xticks([])
    ax_compare.set_yticks([])
    for spine in ax_compare.spines.values():
        spine.set_color(DARK_GREY)

    ax_compare.set_title('GR vs BST', fontsize=14, fontweight='bold',
                          color=BLUE_BRIGHT, fontfamily='monospace', pad=12)

    # ─── GR schematic (left side) ───
    gr_cx, gr_cy, gr_r = 2.5, 7.2, 1.6
    # Horizon circle
    gr_circle = Circle((gr_cx, gr_cy), gr_r, fill=False,
                        edgecolor='#ff4444', linewidth=2.0, linestyle='--')
    ax_compare.add_patch(gr_circle)
    # Dark interior
    gr_fill = Circle((gr_cx, gr_cy), gr_r, facecolor='#1a0000',
                      edgecolor='none', alpha=0.6)
    ax_compare.add_patch(gr_fill)
    # Singularity dot
    ax_compare.plot(gr_cx, gr_cy, 'o', color='white', markersize=6, zorder=10)
    ax_compare.plot(gr_cx, gr_cy, 'x', color=RED_WARM, markersize=10,
                    markeredgewidth=2, zorder=11)
    ax_compare.text(gr_cx, gr_cy - 0.35, 'singularity', fontsize=7,
                    color=RED_WARM, ha='center', fontfamily='monospace')
    ax_compare.text(gr_cx, gr_cy + gr_r + 0.3, 'horizon', fontsize=7,
                    color='#ff6666', ha='center', fontfamily='monospace')
    ax_compare.text(gr_cx, gr_cy + gr_r + 0.7, 'GENERAL RELATIVITY',
                    fontsize=9, fontweight='bold', color='#ff6666',
                    ha='center', fontfamily='monospace')

    # ─── BST schematic (right side) ───
    bst_cx, bst_cy, bst_r = 7.5, 7.2, 1.6
    # Golden membrane ring (thick)
    for dr in np.linspace(0.0, 0.15, 8):
        alpha = 0.6 - dr * 3
        ring = Circle((bst_cx, bst_cy), bst_r - dr, fill=False,
                       edgecolor=GOLD, linewidth=1.5, alpha=max(alpha, 0.1))
        ax_compare.add_patch(ring)
    # NO interior — leave it dark
    ax_compare.text(bst_cx, bst_cy, 'NO\nINTERIOR', fontsize=8,
                    color=DARK_GREY, ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')
    ax_compare.text(bst_cx, bst_cy + bst_r + 0.3, 'membrane', fontsize=7,
                    color=GOLD, ha='center', fontfamily='monospace')
    ax_compare.text(bst_cx, bst_cy + bst_r + 0.7,
                    'BUBBLE SPACETIME',
                    fontsize=9, fontweight='bold', color=GOLD,
                    ha='center', fontfamily='monospace')

    # ─── Comparison table ───
    table_data = [
        ('Central density', 'ρ → ∞ (singularity)', 'ρ ≤ ρ₁₃₇ (Haldane cap)'),
        ('Lapse at center', 'undefined', 'N = 0 (finite)'),
        ('Interior', 'r < r_s accessible', 'No interior — membrane'),
        ('Singularity', 'Real', 'Does not exist'),
        ('Information', 'Paradox', 'No paradox'),
    ]
    y_table = 4.5
    row_h = 0.65

    # Header
    ax_compare.text(0.3, y_table + 0.7, 'Property', fontsize=7,
                    color=GREY, fontfamily='monospace', fontweight='bold')
    ax_compare.text(3.0, y_table + 0.7, 'GR', fontsize=7,
                    color='#ff6666', fontfamily='monospace', fontweight='bold')
    ax_compare.text(7.0, y_table + 0.7, 'BST', fontsize=7,
                    color=GOLD, fontfamily='monospace', fontweight='bold')
    ax_compare.axhline(y=y_table + 0.5, xmin=0.02, xmax=0.98,
                        color=DARK_GREY, linewidth=0.5)

    for i, (prop, gr_val, bst_val) in enumerate(table_data):
        y = y_table - i * row_h
        ax_compare.text(0.3, y, prop, fontsize=6.5, color=WHITE,
                        fontfamily='monospace', va='center')
        ax_compare.text(3.0, y, gr_val, fontsize=5.5, color='#cc6666',
                        fontfamily='monospace', va='center')
        ax_compare.text(7.0, y, bst_val, fontsize=5.5, color=GOLD_DIM,
                        fontfamily='monospace', va='center')
        if i < len(table_data) - 1:
            ax_compare.axhline(y=y - row_h / 2, xmin=0.02, xmax=0.98,
                                color='#1a1a3a', linewidth=0.3)

    # ─── Info box ───
    info_y = 0.6
    info_texts = [
        ('Schwarzschild radius:', '', WHITE),
        ('r_s_val', '', BLUE_GLOW),
        ('Bekenstein entropy:', '', WHITE),
        ('s_val', '', BLUE_GLOW),
        ('Hawking temperature:', '', WHITE),
        ('t_val', '', BLUE_GLOW),
        ('Evaporation time:', '', WHITE),
        ('evap_val', '', BLUE_GLOW),
    ]

    # Placeholder text objects for dynamic update
    info_labels = []
    y_pos = info_y
    for text, _, color in info_texts:
        t = ax_compare.text(0.3, y_pos, text, fontsize=7, color=color,
                             fontfamily='monospace', va='center')
        info_labels.append(t)
        y_pos -= 0.35

    def update_info_box(bh_obj):
        """Update the dynamic info text in center panel."""
        props = bh_obj.membrane_properties()
        temps = bh_obj.hawking_temperature()

        info_labels[0].set_text('Schwarzschild radius:')
        info_labels[1].set_text(f'  r_s = {props["r_membrane_km"]:.1f} km')

        info_labels[2].set_text('Bekenstein entropy:')
        info_labels[3].set_text(f'  S = {format_sci(props["entropy"])}')

        info_labels[4].set_text('Hawking temperature:')
        info_labels[5].set_text(
            f'  T_H = {temps["T_hawking_K"]:.3e} K  '
            f'(BST: x{temps["T_ratio"]:.3f})')

        info_labels[6].set_text('Evaporation time:')
        info_labels[7].set_text(f'  t = {format_sci(props["evaporation_years"], "yr")}')

    update_info_box(bh)

    # ═══════════════════════════════════════════════════════════════
    # RIGHT PANEL — The Two Endpoints (density thermometer)
    # ═══════════════════════════════════════════════════════════════
    ax_thermo = fig.add_axes([0.72, 0.18, 0.24, 0.60])
    ax_thermo.set_facecolor(DARK_PANEL)
    ax_thermo.set_xlim(0, 10)
    ax_thermo.set_ylim(0, 10)
    ax_thermo.set_xticks([])
    ax_thermo.set_yticks([])
    for spine in ax_thermo.spines.values():
        spine.set_color(DARK_GREY)

    ax_thermo.set_title('THE TWO ENDPOINTS', fontsize=14, fontweight='bold',
                         color=BLUE_BRIGHT, fontfamily='monospace', pad=12)

    # Thermometer bar
    thermo_x = 3.5
    thermo_w = 1.5
    thermo_bot = 1.0
    thermo_top = 9.0
    thermo_h = thermo_top - thermo_bot
    n_segments = 80
    for i in range(n_segments):
        frac = i / n_segments  # 0 at bottom, 1 at top
        y_lo = thermo_bot + frac * thermo_h
        y_hi = thermo_bot + (frac + 1.0 / n_segments) * thermo_h
        # Invert: bottom = high density (black hole), top = low density (vacuum)
        rho_frac = 1.0 - frac
        c = density_to_color(rho_frac)
        rect = plt.Rectangle((thermo_x, y_lo), thermo_w, y_hi - y_lo,
                               facecolor=c, edgecolor='none', alpha=0.7)
        ax_thermo.add_patch(rect)

    # Thermometer border
    thermo_border = plt.Rectangle((thermo_x, thermo_bot), thermo_w, thermo_h,
                                    fill=False, edgecolor=GREY, linewidth=1.0)
    ax_thermo.add_patch(thermo_border)

    # Top label: First Commitment
    ax_thermo.text(thermo_x + thermo_w / 2, thermo_top + 0.45,
                    'FIRST COMMITMENT', fontsize=8, fontweight='bold',
                    color=BLUE_GLOW, ha='center', fontfamily='monospace')
    ax_thermo.text(thermo_x + thermo_w / 2, thermo_top + 0.15,
                    'ρ = 0', fontsize=7, color=BLUE_GLOW, ha='center',
                    fontfamily='monospace')

    # Bottom label: Black Hole
    ax_thermo.text(thermo_x + thermo_w / 2, thermo_bot - 0.35,
                    'BLACK HOLE', fontsize=8, fontweight='bold',
                    color=RED_DEEP, ha='center', fontfamily='monospace')
    ax_thermo.text(thermo_x + thermo_w / 2, thermo_bot - 0.6,
                    'ρ = ρ₁₃₇', fontsize=7, color=RED_DEEP, ha='center',
                    fontfamily='monospace')

    # Left annotations: Lapse values
    ax_thermo.text(thermo_x - 0.2, thermo_top, 'N = N₀', fontsize=7,
                    color=BLUE_GLOW, ha='right', va='center',
                    fontfamily='monospace')
    ax_thermo.text(thermo_x - 0.2, thermo_bot, 'N = 0', fontsize=7,
                    color=RED_WARM, ha='right', va='center',
                    fontfamily='monospace')
    ax_thermo.text(thermo_x - 0.2, (thermo_top + thermo_bot) / 2, 'LAPSE',
                    fontsize=7, color=GREY, ha='right', va='center',
                    fontfamily='monospace', rotation=90)

    # Right annotations: Fill fraction
    ax_thermo.text(thermo_x + thermo_w + 0.2, thermo_top, 'f → 0%',
                    fontsize=7, color=BLUE_GLOW, ha='left', va='center',
                    fontfamily='monospace')
    ax_thermo.text(thermo_x + thermo_w + 0.2, thermo_bot, 'f = 100%',
                    fontsize=7, color=RED_WARM, ha='left', va='center',
                    fontfamily='monospace')
    ax_thermo.text(thermo_x + thermo_w + 0.2, (thermo_top + thermo_bot) / 2,
                    'FILL', fontsize=7, color=GREY, ha='left', va='center',
                    fontfamily='monospace', rotation=90)

    # Global average line at 19.1%
    fill_y = thermo_top - FILL * thermo_h  # higher y = lower density
    ax_thermo.axhline(y=fill_y, xmin=0.25, xmax=0.75,
                       color=GREEN, linewidth=1.5, linestyle='--', alpha=0.8)
    ax_thermo.text(thermo_x + thermo_w + 0.2, fill_y,
                    f'f = {FILL*100:.1f}%\nglobal avg',
                    fontsize=6.5, color=GREEN, ha='left', va='center',
                    fontfamily='monospace')

    # Arrow of time
    arrow_x = 1.5
    ax_thermo.annotate('', xy=(arrow_x, thermo_bot + 0.3),
                        xytext=(arrow_x, thermo_top - 0.3),
                        arrowprops=dict(arrowstyle='->', color=GOLD,
                                        lw=2.0, mutation_scale=20))
    ax_thermo.text(arrow_x, (thermo_top + thermo_bot) / 2,
                    'ARROW\nOF\nTIME', fontsize=7, fontweight='bold',
                    color=GOLD_DIM, ha='center', va='center',
                    fontfamily='monospace', rotation=0)

    # Hawking temperature formulas (below thermometer)
    ax_thermo.text(8.5, 6.5, 'HAWKING\nRADIATION', fontsize=7,
                    fontweight='bold', color=ORANGE_GLOW, ha='center',
                    fontfamily='monospace')
    ax_thermo.text(8.5, 5.7, 'Standard:', fontsize=6, color=GREY,
                    ha='center', fontfamily='monospace')
    ax_thermo.text(8.5, 5.3, 'T = 1/(8πM)', fontsize=6, color='#cc8866',
                    ha='center', fontfamily='monospace')
    ax_thermo.text(8.5, 4.7, 'BST:', fontsize=6, color=GREY,
                    ha='center', fontfamily='monospace')
    ax_thermo.text(8.5, 4.3, 'T = 1/(2√137 M)', fontsize=6, color=GOLD,
                    ha='center', fontfamily='monospace')
    ax_thermo.text(8.5, 3.6, 'Ratio = 0.931', fontsize=7,
                    fontweight='bold', color=WHITE, ha='center',
                    fontfamily='monospace')
    ax_thermo.text(8.5, 3.2, '7% geometric\ncorrection', fontsize=6,
                    color=GREY, ha='center', fontfamily='monospace')

    # Endpoint comparison boxes
    # Top: First Commitment
    box_fc = FancyBboxPatch((6.5, 7.5), 3.2, 1.8,
                             boxstyle='round,pad=0.15',
                             facecolor='#0a0a2a', edgecolor=BLUE_GLOW,
                             linewidth=1.0, alpha=0.8)
    ax_thermo.add_patch(box_fc)
    ax_thermo.text(8.1, 9.0, 'FIRST COMMITMENT', fontsize=6,
                    fontweight='bold', color=BLUE_GLOW, ha='center',
                    fontfamily='monospace')
    ax_thermo.text(8.1, 8.6, 'N ≈ 2 commitments', fontsize=5.5,
                    color='#6699cc', ha='center', fontfamily='monospace')
    ax_thermo.text(8.1, 8.2, 'Unstable', fontsize=5.5,
                    color='#6699cc', ha='center', fontfamily='monospace')
    ax_thermo.text(8.1, 7.8, 'Max clock rate', fontsize=5.5,
                    color='#6699cc', ha='center', fontfamily='monospace')

    # Bottom: Black Hole
    box_bh = FancyBboxPatch((6.5, 1.0), 3.2, 1.8,
                             boxstyle='round,pad=0.15',
                             facecolor='#1a0a00', edgecolor=RED_WARM,
                             linewidth=1.0, alpha=0.8)
    ax_thermo.add_patch(box_bh)
    ax_thermo.text(8.1, 2.5, 'BLACK HOLE', fontsize=6,
                    fontweight='bold', color=RED_WARM, ha='center',
                    fontfamily='monospace')
    bh_count_label = ax_thermo.text(
        8.1, 2.1, f'S = {bh.bekenstein_entropy():.1e}', fontsize=5.5,
        color='#cc6644', ha='center', fontfamily='monospace')
    ax_thermo.text(8.1, 1.7, 'Stable', fontsize=5.5,
                    color='#cc6644', ha='center', fontfamily='monospace')
    ax_thermo.text(8.1, 1.3, 'Time frozen', fontsize=5.5,
                    color='#cc6644', ha='center', fontfamily='monospace')

    # ═══════════════════════════════════════════════════════════════
    # DENSITY POSITION SLIDER (controls dot on lapse curve)
    # ═══════════════════════════════════════════════════════════════
    ax_pos_slider = fig.add_axes([0.05, 0.10, 0.28, 0.03])
    ax_pos_slider.set_facecolor(DARK_PANEL)
    pos_slider = Slider(ax_pos_slider, 'ρ/ρ₁₃₇', 0.0, 1.0,
                         valinit=0.0, valstep=0.001,
                         color=BLUE_GLOW)
    pos_slider.label.set_color(WHITE)
    pos_slider.label.set_fontfamily('monospace')
    pos_slider.valtext.set_color(GOLD)
    pos_slider.valtext.set_fontfamily('monospace')

    # Position readout text
    pos_readout = fig.text(0.19, 0.065, '', fontsize=10, color=GOLD,
                            ha='center', fontfamily='monospace',
                            fontweight='bold')

    def update_position(val):
        rho_pos = pos_slider.val
        N_val = np.sqrt(max(0, 1 - rho_pos))
        pos_dot.set_data([rho_pos], [N_val])
        c = density_to_color(rho_pos)
        pos_dot.set_color(c)
        pos_readout.set_text(
            f'N = {N_val:.4f}   |   ρ/ρ₁₃₇ = {rho_pos:.3f}   |   '
            f'Time rate = {N_val*100:.1f}%')
        fig.canvas.draw_idle()

    pos_slider.on_changed(update_position)

    # ═══════════════════════════════════════════════════════════════
    # MASS SLIDER (bottom, controls BH mass)
    # ═══════════════════════════════════════════════════════════════
    ax_mass_slider = fig.add_axes([0.37, 0.10, 0.55, 0.03])
    ax_mass_slider.set_facecolor(DARK_PANEL)
    mass_slider = Slider(ax_mass_slider, 'M / M☉', 1.0, 100.0,
                          valinit=M_init, valstep=0.5,
                          color=ORANGE_GLOW)
    mass_slider.label.set_color(WHITE)
    mass_slider.label.set_fontfamily('monospace')
    mass_slider.valtext.set_color(GOLD)
    mass_slider.valtext.set_fontfamily('monospace')

    # Mass readout
    mass_readout = fig.text(0.645, 0.065, '', fontsize=10, color=GOLD,
                             ha='center', fontfamily='monospace',
                             fontweight='bold')

    def update_mass(val):
        nonlocal bh
        M = mass_slider.val
        bh = BSTBlackHole(M)
        update_info_box(bh)
        bh_count_label.set_text(f'S = {bh.bekenstein_entropy():.1e}')
        props = bh.membrane_properties()
        mass_readout.set_text(
            f'r_s = {props["r_membrane_km"]:.1f} km   |   '
            f'S = {format_sci(props["entropy"])}   |   '
            f't_evap = {format_sci(bh.evaporation_time(), "yr")}')
        fig.canvas.draw_idle()

    mass_slider.on_changed(update_mass)

    # Initialize readouts
    update_position(0.0)
    update_mass(M_init)

    plt.show()


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    # ─── Class report (CI-scriptable) ───
    print('\n' + '=' * 68)
    print('  BST BLACK HOLE PLAYGROUND — Class API Demo')
    print('=' * 68)

    # 10 solar mass black hole
    bh10 = BSTBlackHole(10.0)
    bh10.report()

    # Endpoint comparison
    endpoints = bh10.compare_endpoints()
    print('  TWO ENDPOINTS OF THE DENSITY SPECTRUM:')
    print('  ' + '-' * 50)
    for key in ['first_commitment', 'black_hole']:
        ep = endpoints[key]
        print(f'    {key.upper().replace("_", " ")}:')
        for k, v in ep.items():
            print(f'      {k:20s}  {v}')
        print()

    # Quick scan across masses
    print('  MASS SURVEY:')
    print('  ' + '-' * 50)
    print(f'  {"M/M_sun":>8s}  {"r_s (km)":>10s}  {"S_BH":>12s}  '
          f'{"T_H (K)":>12s}  {"t_evap (yr)":>14s}')
    for M in [1, 3, 10, 30, 100]:
        bh = BSTBlackHole(M)
        props = bh.membrane_properties()
        print(f'  {M:8.0f}  {props["r_membrane_km"]:10.1f}  '
              f'{props["entropy"]:12.2e}  {props["T_hawking_K"]:12.3e}  '
              f'{bh.evaporation_time():14.3e}')

    print()
    print(f'  Singular?     {bh10.is_singular()}')
    print(f'  Has interior? {bh10.has_interior()}')
    print()
    print('  "No singularity. No interior. No information paradox."')
    print('  "Just a full channel."')
    print('=' * 68)
    print()

    # Hawking temperature comparison
    temps = bh10.hawking_temperature()
    print(f'  HAWKING TEMPERATURE — BST vs STANDARD:')
    print(f'  ' + '-' * 50)
    print(f'    Standard:   T_H   = 1/(8πM)        = {temps["T_hawking_K"]:.4e} K')
    print(f'    BST:        T_BST = 1/(2√137 × M)  = {temps["T_bst_K"]:.4e} K')
    print(f'    Ratio:      2√137/(8π) = {temps["scale_ratio"]:.4f}')
    print(f'    Match:      {temps["match_pct"]:.1f}%')
    print(f'    Gap:        7% geometric correction from near-horizon density profile')
    print()

    # Density profile check
    r_test = np.array([1.0, 1.01, 1.1, 1.5, 2.0, 5.0, 10.0]) * bh10.r_s
    rho_test = bh10.density_profile(r_test)
    print(f'  DENSITY PROFILE (10 M_sun):')
    print(f'  ' + '-' * 50)
    print(f'  {"r/r_s":>8s}  {"ρ/ρ₁₃₇":>10s}  {"N(ρ)":>10s}')
    for r, rho_val in zip(r_test / bh10.r_s, rho_test):
        N_val = bh10.lapse(rho_val)
        print(f'  {r:8.2f}  {rho_val:10.6f}  {N_val:10.6f}')
    print()

    # ─── Launch visualization ───
    print('  Launching visualization...')
    print()
    run_visualization()
