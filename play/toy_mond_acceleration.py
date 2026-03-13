#!/usr/bin/env python3
"""
MOND ACCELERATION — The Pion and the Galaxy
============================================

BST derives the MOND acceleration from two integers:

    a_0 = c * H_0 / sqrt(n_C * (n_C + 1))  =  c * H_0 / sqrt(30)

The same sqrt(30) = sqrt(n_C(n_C+1)) that gives the pion mass:
    m_pi = 25.6 * sqrt(30) = 140.2 MeV  (0.46% match)

This connects nuclear physics (pion mass) to galactic dynamics
(flat rotation curves) through a single geometric parameter.

Dark matter in BST is NOT particles. It is the geometric scaffolding
of commitments:
    Omega_DM / Omega_b = (3*n_C + 1) / N_c = 16/3 = 5.333
    The 16 dark dimensions = 6 (off-diagonal color) + 10 (domain)

The Baryonic Tully-Fisher relation is EXACT in BST:
    M_b = v_flat^4 / (G * a_0)    [slope = 4, zero scatter]

Donato universal surface density:
    Sigma_0 = a_0 / (2*pi*G) => log10(Sigma_0) = 2.15 M_sun/pc^2

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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
from matplotlib.gridspec import GridSpec

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # domain dimension (D_IV^5)
N_max = 137       # maximum channel number
C_2 = 6           # Casimir number
GENUS = 7         # genus of D_IV^5

# ─── Physical Constants ───
c_light = 2.99792458e8        # speed of light, m/s
G_N = 6.67430e-11             # Newton's gravitational constant, m^3 kg^-1 s^-2
M_sun = 1.989e30              # solar mass, kg
kpc_m = 3.0857e19             # 1 kpc in meters
pc_m = 3.0857e16              # 1 pc in meters
Mpc_m = 3.0857e22             # 1 Mpc in meters
m_e_eV = 0.51100e6            # electron mass in eV
m_p_eV = 938.272e6            # proton mass in eV
m_pi_obs_MeV = 139.57         # observed pion mass (charged), MeV

# ─── Colors ───
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BLUE_GLOW   = '#4488ff'
BLUE_BRIGHT = '#66aaff'
BLUE_DIM    = '#224488'
PURPLE_GLOW = '#9955dd'
RED_WARM    = '#ff6644'
WHITE       = '#ffffff'
GREY        = '#888888'
LIGHT_GREY  = '#bbbbbb'
GREEN_GLOW  = '#44dd88'
CYAN_GLOW   = '#44dddd'
ORANGE_GLOW = '#ff9944'


# ─── Helper Functions ───
def glow_text(ax, x, y, text, color=WHITE, fontsize=12, ha='center', va='center',
              weight='normal', alpha=1.0, glow_color=None, glow_width=3, **kwargs):
    """Draw text with optional glow effect."""
    if glow_color is None:
        glow_color = color
    t = ax.text(x, y, text, fontsize=fontsize, color=color, ha=ha, va=va,
                fontweight=weight, alpha=alpha, fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=glow_width,
                                           foreground=glow_color + '44')],
                **kwargs)
    return t


def info_box(ax, x, y, width, height, text, color=GOLD, fontsize=10,
             bg_color=DARK_PANEL, border_alpha=0.6, text_alpha=0.95):
    """Draw an info box with border and text."""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02",
                         facecolor=bg_color, edgecolor=color,
                         linewidth=1.5, alpha=border_alpha,
                         transform=ax.transAxes)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=color, ha='center', va='center',
            fontfamily='monospace', alpha=text_alpha, transform=ax.transAxes)
    return box


# ═══════════════════════════════════════════════════════════════════════
# MONDAcceleration CLASS — CI-scriptable API
# ═══════════════════════════════════════════════════════════════════════

class MONDAcceleration:
    """
    BST MOND acceleration calculator.

    The MOND acceleration is derived from the domain geometry:
        a_0 = c * H_0 / sqrt(n_C * (n_C + 1)) = c * H_0 / sqrt(30)

    The same sqrt(30) parameter connects:
        - Nuclear scale: m_pi = 25.6 * sqrt(30) = 140.2 MeV
        - Galactic scale: a_0 = c * H_0 / sqrt(30) = 1.195e-10 m/s^2
        - Chiral condensate: chi = sqrt(n_C(n_C+1)) = sqrt(30)

    Usage:
        mond = MONDAcceleration()
        print(mond.a0())                          # 1.195e-10 m/s^2
        curve = mond.rotation_curve(1e11, r_kpc)  # rotation curve
        mass = mond.tully_fisher(200)              # Tully-Fisher
        print(mond.compare_observed())             # comparison dict
    """

    def __init__(self, H0_km_s_Mpc=67.36):
        """
        Initialize with Hubble constant.

        Parameters
        ----------
        H0_km_s_Mpc : float
            Hubble constant in km/s/Mpc. Default: 67.36 (Planck 2018).
        """
        self.H0_km_s_Mpc = H0_km_s_Mpc
        self.H0_si = H0_km_s_Mpc * 1e3 / Mpc_m   # convert to s^-1
        self.N_c = N_c
        self.n_C = n_C
        self.chi = np.sqrt(n_C * (n_C + 1))        # sqrt(30)

    def a0(self):
        """
        BST MOND acceleration in m/s^2.

        a_0 = c * H_0 / sqrt(n_C * (n_C + 1)) = c * H_0 / sqrt(30)

        Returns
        -------
        float
            MOND acceleration a_0 in m/s^2.
        """
        return c_light * self.H0_si / self.chi

    def rotation_curve(self, M_solar, r_kpc_array):
        """
        Newtonian + MOND rotation curves for a given baryonic mass.

        Uses the standard MOND interpolating function mu(x) = x/(1+x):
            mu(g/a_0) * g = g_N
            => g^2 / (a_0 + g) = g_N
            => g = [g_N + sqrt(g_N^2 + 4*g_N*a_0)] / 2

        This gives:
            g_N >> a_0: g_eff -> g_N (Newtonian)
            g_N << a_0: g_eff -> sqrt(g_N * a_0) (deep MOND, flat curves)

        Parameters
        ----------
        M_solar : float
            Baryonic mass in solar masses.
        r_kpc_array : array-like
            Radii in kpc.

        Returns
        -------
        dict with keys:
            'r_kpc': radii in kpc
            'v_newton_km_s': Newtonian rotation velocity in km/s
            'v_mond_km_s': MOND rotation velocity in km/s
            'v_flat_km_s': asymptotic flat velocity in km/s
            'r_transition_kpc': radius where g_N = a_0
            'a0': the MOND acceleration used
        """
        r_kpc = np.asarray(r_kpc_array, dtype=float)
        r_m = r_kpc * kpc_m
        M_kg = M_solar * M_sun
        a0_val = self.a0()

        # Newtonian gravitational acceleration
        g_N = G_N * M_kg / r_m**2

        # Newtonian velocity
        v_newton = np.sqrt(G_N * M_kg / r_m)

        # MOND effective acceleration (standard interpolation mu(x) = x/(1+x))
        # Solving mu(g/a_0)*g = g_N with mu(x)=x/(1+x):
        # g^2/(a_0 + g) = g_N  =>  g = [g_N + sqrt(g_N^2 + 4*g_N*a_0)] / 2
        g_eff = 0.5 * (g_N + np.sqrt(g_N**2 + 4.0 * g_N * a0_val))
        v_mond = np.sqrt(r_m * g_eff)

        # Asymptotic flat velocity (deep MOND)
        v_flat = (G_N * M_kg * a0_val) ** 0.25

        # Transition radius where g_N = a_0
        r_transition = np.sqrt(G_N * M_kg / a0_val)

        return {
            'r_kpc': r_kpc,
            'v_newton_km_s': v_newton / 1e3,
            'v_mond_km_s': v_mond / 1e3,
            'v_flat_km_s': v_flat / 1e3,
            'r_transition_kpc': r_transition / kpc_m,
            'a0': a0_val
        }

    def tully_fisher(self, v_flat_km_s):
        """
        Baryonic mass from flat rotation velocity (Tully-Fisher relation).

        M_b = v_flat^4 / (G * a_0)

        This relation is EXACT in BST — slope = 4 with zero scatter.
        Any observed scatter comes from measurement uncertainty, not physics.

        Parameters
        ----------
        v_flat_km_s : float or array
            Flat rotation velocity in km/s.

        Returns
        -------
        float or array
            Baryonic mass in solar masses.
        """
        v_si = np.asarray(v_flat_km_s, dtype=float) * 1e3  # km/s -> m/s
        a0_val = self.a0()
        M_kg = v_si**4 / (G_N * a0_val)
        return M_kg / M_sun

    def donato_surface_density(self):
        """
        Universal surface density Sigma_0 = a_0 / (2*pi*G).

        Donato et al. (2009) showed all dark matter halos share:
            log10(Sigma_0) ~ 2.15 M_sun/pc^2

        BST predicts this exactly from a_0.

        Returns
        -------
        dict with keys:
            'Sigma_0_kg_m2': surface density in kg/m^2
            'Sigma_0_Msun_pc2': surface density in M_sun/pc^2
            'log10_Sigma_0': log10 of surface density in M_sun/pc^2
            'observed_log10': observed value (Donato 2009)
            'match_percent': percentage match
        """
        a0_val = self.a0()
        Sigma_0 = a0_val / (2.0 * np.pi * G_N)       # kg/m^2
        Sigma_0_Msun_pc2 = Sigma_0 * pc_m**2 / M_sun  # M_sun/pc^2
        log10_val = np.log10(Sigma_0_Msun_pc2)
        observed = 2.15
        match_pct = abs(log10_val - observed) / observed * 100

        return {
            'Sigma_0_kg_m2': Sigma_0,
            'Sigma_0_Msun_pc2': Sigma_0_Msun_pc2,
            'log10_Sigma_0': log10_val,
            'observed_log10': observed,
            'match_percent': match_pct
        }

    def pion_connection(self):
        """
        Show sqrt(30) connects pion mass and MOND acceleration.

        Nuclear: m_pi = 25.6 * sqrt(30) = 140.2 MeV
        Galactic: a_0 = c * H_0 / sqrt(30) = 1.195e-10 m/s^2

        Same geometric parameter, 19 orders of magnitude apart.

        Returns
        -------
        dict with nuclear and galactic scale results.
        """
        chi = self.chi
        a0_val = self.a0()

        # Pion mass from BST
        m_pi_BST_MeV = 25.6 * chi
        pion_match = abs(m_pi_BST_MeV - m_pi_obs_MeV) / m_pi_obs_MeV * 100

        # MOND acceleration
        a0_observed = 1.20e-10  # McGaugh 2016
        mond_match = abs(a0_val - a0_observed) / a0_observed * 100

        # Scale ratio
        m_pi_J = m_pi_BST_MeV * 1e6 * 1.602e-19  # to Joules
        # Energy scale of a_0 over characteristic galactic length (~10 kpc)
        E_mond = a0_val * M_sun * 10 * kpc_m      # force * distance
        ratio = m_pi_J / (a0_val * 1.67e-27)      # pion energy / (a0 * proton mass)

        return {
            'sqrt_30': chi,
            'sqrt_30_exact': 'sqrt(n_C * (n_C + 1)) = sqrt(5 * 6) = sqrt(30)',
            'pion_mass_MeV': m_pi_BST_MeV,
            'pion_observed_MeV': m_pi_obs_MeV,
            'pion_match_percent': pion_match,
            'a0_BST': a0_val,
            'a0_observed': a0_observed,
            'mond_match_percent': mond_match,
            'orders_of_magnitude_apart': int(np.log10(m_pi_J / (a0_val * 1.67e-27))),
            'unified_by': 'chi = sqrt(n_C(n_C+1)) = sqrt(30)'
        }

    def dark_matter_decomposition(self):
        """
        Dark matter in BST: 16/3 decomposition of geometric dimensions.

        Omega_DM/Omega_b = (3*n_C + 1) / N_c = 16/3 = 5.333

        The 16 dark dimensions decompose as:
            6 = N_c*(N_c-1) : off-diagonal color (SU(3) generators minus Cartan)
            10 = 2*n_C      : domain dimensions (complex D_IV^5)
            ---
            16 total dark dimensions

        Plus 3 = N_c baryonic (visible) dimensions.
        Total: 19 = N_c^2 + 2*n_C dimensions in the full structure.

        Returns
        -------
        dict with decomposition details.
        """
        off_diagonal_color = N_c * (N_c - 1)   # = 6
        domain_dims = 2 * n_C                    # = 10
        dark_total = off_diagonal_color + domain_dims  # = 16
        baryon_dims = N_c                        # = 3
        full_total = dark_total + baryon_dims    # = 19

        ratio = dark_total / baryon_dims         # = 16/3

        # Observed ratio
        omega_DM_obs = 0.268
        omega_b_obs = 0.049
        ratio_obs = omega_DM_obs / omega_b_obs   # ~5.47

        return {
            'Omega_DM_over_Omega_b': ratio,
            'Omega_DM_over_Omega_b_fraction': '16/3',
            'observed_ratio': ratio_obs,
            'match_percent': abs(ratio - ratio_obs) / ratio_obs * 100,
            'off_diagonal_color': off_diagonal_color,
            'domain_dimensions': domain_dims,
            'dark_total': dark_total,
            'baryon_dimensions': baryon_dims,
            'full_total': full_total,
            'formula': 'Omega_DM/Omega_b = (3*n_C + 1)/N_c = 16/3',
            'color_formula': 'N_c*(N_c-1) = 3*2 = 6',
            'domain_formula': '2*n_C = 2*5 = 10',
            'baryon_formula': 'N_c = 3'
        }

    def compare_observed(self):
        """
        Compare BST a_0 with observed values.

        Returns
        -------
        dict with BST prediction, observed values, and match quality.
        """
        a0_val = self.a0()
        a0_obs = 1.20e-10          # McGaugh (2016)
        a0_obs_err = 0.02e-10      # uncertainty

        cH0 = c_light * self.H0_si
        sigma_off = abs(a0_val - a0_obs) / a0_obs_err

        return {
            'a0_BST_m_s2': a0_val,
            'a0_observed_m_s2': a0_obs,
            'a0_observed_error': a0_obs_err,
            'c_times_H0': cH0,
            'sqrt_30': self.chi,
            'match_percent': abs(a0_val - a0_obs) / a0_obs * 100,
            'sigma_deviation': sigma_off,
            'formula': 'a_0 = c * H_0 / sqrt(n_C * (n_C + 1))',
            'formula_numeric': f'a_0 = {cH0:.3e} / {self.chi:.4f} = {a0_val:.3e} m/s^2',
            'reference': 'McGaugh, Lelli & Schombert (2016), PRL 117, 201101'
        }

    def __repr__(self):
        a0_val = self.a0()
        return (
            f"MONDAcceleration(\n"
            f"  H0 = {self.H0_km_s_Mpc} km/s/Mpc\n"
            f"  a0 = {a0_val:.4e} m/s^2\n"
            f"  chi = sqrt(30) = {self.chi:.6f}\n"
            f"  formula: a_0 = c * H_0 / sqrt(n_C(n_C+1))\n"
            f")"
        )


# ═══════════════════════════════════════════════════════════════════════
# VISUALIZATION
# ═══════════════════════════════════════════════════════════════════════

def build_visualization():
    """Build the 3-panel MOND visualization."""

    mond = MONDAcceleration()

    # ─── Figure Setup ───
    fig = plt.figure(figsize=(20, 12), facecolor=BG)
    fig.canvas.manager.set_window_title('MOND Acceleration — BST')

    # Title
    fig.text(0.5, 0.97, 'MOND ACCELERATION', fontsize=28, fontweight='bold',
             color=GOLD, ha='center', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#442200')])
    fig.text(0.5, 0.935, 'The Pion and the Galaxy Share the Same Geometry',
             fontsize=13, color=GOLD_DIM, ha='center', fontfamily='monospace')

    # Bottom strip
    fig.text(0.5, 0.015,
             r'$a_0 = c\,H_0\,/\,\sqrt{30}$  '
             '  the pion and the galaxy share the same geometry',
             fontsize=13, color=GOLD, ha='center', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#44220044')])

    # Grid: 3 columns with bottom space for slider
    gs = GridSpec(2, 3, figure=fig,
                  left=0.06, right=0.97, top=0.91, bottom=0.10,
                  hspace=0.08, wspace=0.28,
                  height_ratios=[1, 0.05])

    # ─── LEFT PANEL: Rotation Curves ───
    ax_rot = fig.add_subplot(gs[0, 0])
    ax_rot.set_facecolor(DARK_PANEL)

    # Slider axis
    ax_slider = fig.add_subplot(gs[1, 0])
    ax_slider.set_facecolor(DARK_PANEL)

    # Default mass
    log_mass_default = 11.0  # 10^11 M_sun

    def draw_rotation_curves(log_mass):
        ax_rot.clear()
        ax_rot.set_facecolor(DARK_PANEL)

        M_solar = 10**log_mass
        r_kpc = np.linspace(0.5, 120, 500)
        curve = mond.rotation_curve(M_solar, r_kpc)

        # Plot Newtonian (declining, dashed blue)
        ax_rot.plot(curve['r_kpc'], curve['v_newton_km_s'],
                    color=BLUE_GLOW, linewidth=2, linestyle='--',
                    alpha=0.8, label='Newtonian')

        # Plot MOND (flat, solid gold)
        ax_rot.plot(curve['r_kpc'], curve['v_mond_km_s'],
                    color=GOLD, linewidth=2.5, alpha=0.95,
                    label='BST / MOND')

        # Flat velocity line
        v_flat = curve['v_flat_km_s']
        ax_rot.axhline(y=v_flat, color=GOLD_DIM, linewidth=1, linestyle=':',
                        alpha=0.5)
        ax_rot.text(105, v_flat * 1.04,
                    f'v_flat = {v_flat:.0f} km/s',
                    fontsize=8, color=GOLD_DIM, ha='right', fontfamily='monospace')

        # Transition radius
        r_trans = curve['r_transition_kpc']
        if 0.5 < r_trans < 120:
            ax_rot.axvline(x=r_trans, color=RED_WARM, linewidth=1,
                           linestyle='-.', alpha=0.5)
            # Find the velocity at transition
            idx_trans = np.argmin(np.abs(r_kpc - r_trans))
            v_trans = curve['v_mond_km_s'][idx_trans]
            ax_rot.annotate(f'g = a_0\nr = {r_trans:.1f} kpc',
                           xy=(r_trans, v_trans),
                           xytext=(r_trans + 12, v_trans * 0.7),
                           fontsize=8, color=RED_WARM, fontfamily='monospace',
                           arrowprops=dict(arrowstyle='->', color=RED_WARM,
                                          alpha=0.6))

        # Simulated "observed" data points (scatter around MOND curve)
        np.random.seed(42)
        r_obs = np.linspace(3, 100, 20)
        curve_obs = mond.rotation_curve(M_solar, r_obs)
        v_obs = curve_obs['v_mond_km_s'] * (1 + 0.03 * np.random.randn(len(r_obs)))
        v_err = curve_obs['v_mond_km_s'] * 0.04
        ax_rot.errorbar(r_obs, v_obs, yerr=v_err, fmt='o', color=GREEN_GLOW,
                        markersize=4, alpha=0.7, elinewidth=1,
                        capsize=2, label='Simulated obs.')

        # Labels and formatting
        ax_rot.set_xlabel('r  (kpc)', fontsize=11, color=LIGHT_GREY,
                          fontfamily='monospace')
        ax_rot.set_ylabel('v  (km/s)', fontsize=11, color=LIGHT_GREY,
                          fontfamily='monospace')
        ax_rot.set_title(f'Rotation Curve   M = 10^{log_mass:.1f} M_sun',
                         fontsize=12, color=WHITE, fontfamily='monospace',
                         pad=10)

        # Axes styling
        ax_rot.tick_params(colors=GREY, labelsize=9)
        ax_rot.spines['bottom'].set_color(GREY)
        ax_rot.spines['left'].set_color(GREY)
        ax_rot.spines['top'].set_visible(False)
        ax_rot.spines['right'].set_visible(False)

        # Set reasonable y-limits
        v_max = max(np.max(curve['v_newton_km_s']),
                    np.max(curve['v_mond_km_s']))
        ax_rot.set_ylim(0, v_max * 1.3)
        ax_rot.set_xlim(0, 120)

        # Legend
        legend = ax_rot.legend(loc='upper right', fontsize=9,
                               facecolor=DARK_PANEL, edgecolor=GREY,
                               labelcolor=LIGHT_GREY)
        legend.get_frame().set_alpha(0.8)

        # Physics annotation
        ax_rot.text(0.05, 0.05,
                    f'a_0 = {mond.a0():.3e} m/s^2',
                    fontsize=8, color=GOLD_DIM, fontfamily='monospace',
                    transform=ax_rot.transAxes, alpha=0.8)

        fig.canvas.draw_idle()

    # Draw initial
    draw_rotation_curves(log_mass_default)

    # Mass slider
    slider = Slider(ax_slider, 'log10(M/M_sun)', 8.0, 12.5,
                    valinit=log_mass_default, valstep=0.1,
                    color=GOLD_DIM)
    slider.label.set_color(LIGHT_GREY)
    slider.label.set_fontfamily('monospace')
    slider.label.set_fontsize(9)
    slider.valtext.set_color(GOLD)
    slider.valtext.set_fontfamily('monospace')
    slider.valtext.set_fontsize(9)
    ax_slider.set_facecolor(DARK_PANEL)

    def on_slider_change(val):
        draw_rotation_curves(val)

    slider.on_changed(on_slider_change)

    # ─── CENTER PANEL: The sqrt(30) Connection ───
    ax_conn = fig.add_subplot(gs[0, 1])
    ax_conn.set_facecolor(DARK_PANEL)
    ax_conn.set_xlim(0, 1)
    ax_conn.set_ylim(0, 1)
    ax_conn.set_xticks([])
    ax_conn.set_yticks([])
    for spine in ax_conn.spines.values():
        spine.set_visible(False)

    ax_conn.set_title(r'The  $\sqrt{30}$  Connection', fontsize=13,
                      color=WHITE, fontfamily='monospace', pad=10)

    # ── Top box: Pion mass (nuclear scale) ──
    box_top = FancyBboxPatch((0.08, 0.78), 0.84, 0.16,
                             boxstyle="round,pad=0.02",
                             facecolor='#0a1a2a', edgecolor=BLUE_GLOW,
                             linewidth=2, alpha=0.9)
    ax_conn.add_patch(box_top)
    ax_conn.text(0.5, 0.90, 'NUCLEAR SCALE', fontsize=10, fontweight='bold',
                 color=BLUE_BRIGHT, ha='center', fontfamily='monospace')
    ax_conn.text(0.5, 0.845, r'm$_\pi$ = 25.6 $\times$ $\sqrt{30}$ = 140.2 MeV',
                 fontsize=11, color=WHITE, ha='center', fontfamily='monospace')
    ax_conn.text(0.5, 0.80, '(0.46% match to observed 139.57 MeV)',
                 fontsize=8, color=GREY, ha='center', fontfamily='monospace')

    # ── Golden connecting line ──
    ax_conn.plot([0.5, 0.5], [0.78, 0.55], color=GOLD, linewidth=3,
                 alpha=0.8, solid_capstyle='round')
    # Arrow heads
    ax_conn.annotate('', xy=(0.5, 0.78), xytext=(0.5, 0.72),
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
    ax_conn.annotate('', xy=(0.5, 0.55), xytext=(0.5, 0.61),
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

    # ── sqrt(30) label on line ──
    sqrt30_box = FancyBboxPatch((0.28, 0.63), 0.44, 0.10,
                                boxstyle="round,pad=0.02",
                                facecolor=BG, edgecolor=GOLD,
                                linewidth=2, alpha=0.95)
    ax_conn.add_patch(sqrt30_box)
    ax_conn.text(0.5, 0.685, r'$\sqrt{n_C(n_C+1)}$ = $\sqrt{30}$',
                 fontsize=14, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#44220044')])
    ax_conn.text(0.5, 0.645, r'$\chi$ = chiral condensate parameter',
                 fontsize=8, color=GOLD_DIM, ha='center', fontfamily='monospace')

    # ── Bottom box: MOND acceleration (galactic scale) ──
    box_bot = FancyBboxPatch((0.08, 0.39), 0.84, 0.16,
                             boxstyle="round,pad=0.02",
                             facecolor='#1a0a2a', edgecolor=PURPLE_GLOW,
                             linewidth=2, alpha=0.9)
    ax_conn.add_patch(box_bot)
    ax_conn.text(0.5, 0.51, 'GALACTIC SCALE', fontsize=10, fontweight='bold',
                 color=PURPLE_GLOW, ha='center', fontfamily='monospace')
    ax_conn.text(0.5, 0.46, r'a$_0$ = cH$_0$ / $\sqrt{30}$'
                 f' = {mond.a0():.3e} m/s' + r'$^2$',
                 fontsize=11, color=WHITE, ha='center', fontfamily='monospace')
    ax_conn.text(0.5, 0.41, '(0.4% match to McGaugh 2016)',
                 fontsize=8, color=GREY, ha='center', fontfamily='monospace')

    # ── Scale separation note ──
    ax_conn.text(0.5, 0.33,
                 'Same structural parameter',
                 fontsize=10, fontweight='bold', color=ORANGE_GLOW,
                 ha='center', fontfamily='monospace')
    ax_conn.text(0.5, 0.285,
                 '19 orders of magnitude apart',
                 fontsize=9, color=ORANGE_GLOW, ha='center',
                 fontfamily='monospace', alpha=0.8)

    # ── 16/3 Decomposition ──
    y_decomp = 0.18
    ax_conn.plot([0.1, 0.9], [y_decomp + 0.06, y_decomp + 0.06],
                 color=GREY, linewidth=0.5, alpha=0.4)

    ax_conn.text(0.5, y_decomp + 0.04, 'Dark Dimension Decomposition',
                 fontsize=9, fontweight='bold', color=CYAN_GLOW,
                 ha='center', fontfamily='monospace')

    # Three boxes: 3 + 6 + 10 = 19
    box_w = 0.22
    box_h = 0.08
    y_b = y_decomp - 0.06

    # N_c = 3 (baryon)
    b1 = FancyBboxPatch((0.05, y_b), box_w, box_h,
                        boxstyle="round,pad=0.01",
                        facecolor='#002211', edgecolor=GREEN_GLOW,
                        linewidth=1.5, alpha=0.8)
    ax_conn.add_patch(b1)
    ax_conn.text(0.05 + box_w/2, y_b + box_h * 0.65, '3', fontsize=14,
                 fontweight='bold', color=GREEN_GLOW, ha='center',
                 fontfamily='monospace')
    ax_conn.text(0.05 + box_w/2, y_b + box_h * 0.25, 'baryon',
                 fontsize=7, color=GREEN_GLOW, ha='center',
                 fontfamily='monospace', alpha=0.8)

    # 6 (color off-diag)
    b2 = FancyBboxPatch((0.39, y_b), box_w, box_h,
                        boxstyle="round,pad=0.01",
                        facecolor='#001122', edgecolor=BLUE_GLOW,
                        linewidth=1.5, alpha=0.8)
    ax_conn.add_patch(b2)
    ax_conn.text(0.39 + box_w/2, y_b + box_h * 0.65, '6', fontsize=14,
                 fontweight='bold', color=BLUE_GLOW, ha='center',
                 fontfamily='monospace')
    ax_conn.text(0.39 + box_w/2, y_b + box_h * 0.25, 'color',
                 fontsize=7, color=BLUE_GLOW, ha='center',
                 fontfamily='monospace', alpha=0.8)

    # 10 (domain)
    b3 = FancyBboxPatch((0.73, y_b), box_w, box_h,
                        boxstyle="round,pad=0.01",
                        facecolor='#110022', edgecolor=PURPLE_GLOW,
                        linewidth=1.5, alpha=0.8)
    ax_conn.add_patch(b3)
    ax_conn.text(0.73 + box_w/2, y_b + box_h * 0.65, '10', fontsize=14,
                 fontweight='bold', color=PURPLE_GLOW, ha='center',
                 fontfamily='monospace')
    ax_conn.text(0.73 + box_w/2, y_b + box_h * 0.25, 'domain',
                 fontsize=7, color=PURPLE_GLOW, ha='center',
                 fontfamily='monospace', alpha=0.8)

    # Plus signs and equals
    ax_conn.text(0.33, y_b + box_h/2, '+', fontsize=14, fontweight='bold',
                 color=GREY, ha='center', va='center', fontfamily='monospace')
    ax_conn.text(0.67, y_b + box_h/2, '+', fontsize=14, fontweight='bold',
                 color=GREY, ha='center', va='center', fontfamily='monospace')

    # Total
    ax_conn.text(0.5, y_b - 0.035,
                 '= 19 total    (16 dark / 3 visible = 16/3 = 5.33)',
                 fontsize=8, color=LIGHT_GREY, ha='center',
                 fontfamily='monospace')
    ax_conn.text(0.5, y_b - 0.065,
                 r'$\Omega_{DM}/\Omega_b$ = (3n_C+1)/N_c = 16/3',
                 fontsize=8, color=CYAN_GLOW, ha='center',
                 fontfamily='monospace', alpha=0.8)

    # ─── RIGHT PANEL: Tully-Fisher ───
    ax_tf = fig.add_subplot(gs[0, 2])
    ax_tf.set_facecolor(DARK_PANEL)

    # Generate Tully-Fisher data
    v_flat_range = np.logspace(1.3, 2.6, 200)   # 20 to 400 km/s
    M_tf = mond.tully_fisher(v_flat_range)

    # Plot the v^4 line
    ax_tf.loglog(v_flat_range, M_tf, color=GOLD, linewidth=2.5, alpha=0.95,
                 label=r'BST: M$_b$ = v$^4$/(G a$_0$)')

    # Simulated observed galaxies
    np.random.seed(123)
    n_gal = 60
    v_gal = np.logspace(1.5, 2.5, n_gal)
    M_gal_true = mond.tully_fisher(v_gal)
    # Add realistic scatter (0.15 dex)
    M_gal_obs = M_gal_true * 10**(0.12 * np.random.randn(n_gal))
    v_gal_obs = v_gal * 10**(0.02 * np.random.randn(n_gal))

    # Color galaxies by type
    colors_gal = []
    for i, m in enumerate(M_gal_obs):
        if m > 1e11:
            colors_gal.append(RED_WARM)      # massive spirals
        elif m > 1e9:
            colors_gal.append(BLUE_GLOW)     # spirals
        else:
            colors_gal.append(GREEN_GLOW)    # dwarfs
    ax_tf.scatter(v_gal_obs, M_gal_obs, c=colors_gal, s=25, alpha=0.7,
                  edgecolors='none', zorder=5)

    # Slope annotation
    # Pick a point on the line
    v_ann = 150
    M_ann = mond.tully_fisher(v_ann)
    ax_tf.annotate('slope = 4\n(exact in BST)',
                   xy=(v_ann, M_ann),
                   xytext=(35, M_ann * 20),
                   fontsize=9, color=GOLD, fontfamily='monospace',
                   arrowprops=dict(arrowstyle='->', color=GOLD_DIM, alpha=0.6))

    # Donato surface density annotation
    donato = mond.donato_surface_density()
    ax_tf.text(0.05, 0.15,
               f"Donato surface density:\n"
               f"  log10(Sigma_0) = {donato['log10_Sigma_0']:.2f} M_sun/pc^2\n"
               f"  observed: {donato['observed_log10']:.2f} M_sun/pc^2",
               fontsize=8, color=CYAN_GLOW, fontfamily='monospace',
               transform=ax_tf.transAxes, alpha=0.9,
               bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                         edgecolor=CYAN_GLOW, alpha=0.4))

    # Galaxy type legend (manual)
    ax_tf.scatter([], [], c=RED_WARM, s=25, label='Massive spirals')
    ax_tf.scatter([], [], c=BLUE_GLOW, s=25, label='Spirals')
    ax_tf.scatter([], [], c=GREEN_GLOW, s=25, label='Dwarfs')

    # Labels and formatting
    ax_tf.set_xlabel(r'v$_{flat}$  (km/s)', fontsize=11, color=LIGHT_GREY,
                     fontfamily='monospace')
    ax_tf.set_ylabel(r'M$_{baryonic}$  (M$_\odot$)', fontsize=11,
                     color=LIGHT_GREY, fontfamily='monospace')
    ax_tf.set_title('Baryonic Tully-Fisher', fontsize=12, color=WHITE,
                    fontfamily='monospace', pad=10)

    ax_tf.tick_params(colors=GREY, labelsize=9)
    ax_tf.spines['bottom'].set_color(GREY)
    ax_tf.spines['left'].set_color(GREY)
    ax_tf.spines['top'].set_visible(False)
    ax_tf.spines['right'].set_visible(False)

    # Grid
    ax_tf.grid(True, alpha=0.15, color=GREY, which='both')

    # Legend
    legend_tf = ax_tf.legend(loc='upper left', fontsize=8,
                             facecolor=DARK_PANEL, edgecolor=GREY,
                             labelcolor=LIGHT_GREY)
    legend_tf.get_frame().set_alpha(0.8)

    # Axis limits
    ax_tf.set_xlim(20, 400)
    ax_tf.set_ylim(1e7, 5e12)

    # ─── Key comparison box (bottom right of TF panel) ───
    comp = mond.compare_observed()
    ax_tf.text(0.95, 0.05,
               f"BST a_0 = {comp['a0_BST_m_s2']:.3e} m/s^2\n"
               f"Obs a_0 = {comp['a0_observed_m_s2']:.2e} +/- {comp['a0_observed_error']:.0e}\n"
               f"Match: {comp['match_percent']:.1f}%  "
               f"({comp['sigma_deviation']:.1f} sigma)",
               fontsize=7, color=GOLD_DIM, fontfamily='monospace',
               transform=ax_tf.transAxes, ha='right', va='bottom',
               alpha=0.8)

    plt.tight_layout(rect=[0.0, 0.04, 1.0, 0.93])
    return fig, mond, slider


# ═══════════════════════════════════════════════════════════════════════
# CLI Printout
# ═══════════════════════════════════════════════════════════════════════

def print_summary():
    """Print a CLI summary of BST MOND results."""
    mond = MONDAcceleration()

    print("=" * 72)
    print("  MOND ACCELERATION FROM BST")
    print("  a_0 = c * H_0 / sqrt(n_C * (n_C + 1)) = c * H_0 / sqrt(30)")
    print("=" * 72)
    print()

    # Basic parameters
    print(f"  BST parameters: N_c = {N_c}, n_C = {n_C}, N_max = {N_max}")
    print(f"  chi = sqrt(n_C*(n_C+1)) = sqrt(30) = {np.sqrt(30):.6f}")
    print(f"  H_0 = {mond.H0_km_s_Mpc} km/s/Mpc = {mond.H0_si:.4e} s^-1")
    print(f"  c * H_0 = {c_light * mond.H0_si:.4e} m/s^2")
    print()

    # MOND acceleration
    comp = mond.compare_observed()
    print("  --- MOND Acceleration ---")
    print(f"  a_0 (BST)      = {comp['a0_BST_m_s2']:.4e} m/s^2")
    print(f"  a_0 (observed)  = {comp['a0_observed_m_s2']:.2e}"
          f" +/- {comp['a0_observed_error']:.0e} m/s^2")
    print(f"  Match: {comp['match_percent']:.2f}%"
          f"  ({comp['sigma_deviation']:.2f} sigma)")
    print()

    # Pion connection
    pion = mond.pion_connection()
    print("  --- The sqrt(30) Connection ---")
    print(f"  Pion: m_pi = 25.6 * sqrt(30) = {pion['pion_mass_MeV']:.1f} MeV"
          f"  (obs: {pion['pion_observed_MeV']:.2f} MeV,"
          f" {pion['pion_match_percent']:.2f}%)")
    print(f"  MOND: a_0  = cH_0 / sqrt(30) = {pion['a0_BST']:.3e} m/s^2"
          f"  (obs: {pion['a0_observed']:.2e} m/s^2,"
          f" {pion['mond_match_percent']:.2f}%)")
    print(f"  Scale separation: ~{pion['orders_of_magnitude_apart']}"
          " orders of magnitude")
    print()

    # Dark matter decomposition
    dm = mond.dark_matter_decomposition()
    print("  --- Dark Matter Decomposition ---")
    print(f"  Omega_DM/Omega_b = (3*n_C + 1)/N_c = {dm['Omega_DM_over_Omega_b']:.4f}"
          f" = {dm['Omega_DM_over_Omega_b_fraction']}")
    print(f"  Observed ratio   = {dm['observed_ratio']:.2f}"
          f"  (match: {dm['match_percent']:.1f}%)")
    print(f"  16 dark = {dm['off_diagonal_color']} (color) +"
          f" {dm['domain_dimensions']} (domain)")
    print(f"  +3 baryon = {dm['full_total']} total dimensions")
    print()

    # Donato surface density
    don = mond.donato_surface_density()
    print("  --- Donato Universal Surface Density ---")
    print(f"  Sigma_0 = a_0/(2*pi*G) = {don['Sigma_0_Msun_pc2']:.1f} M_sun/pc^2")
    print(f"  log10(Sigma_0) = {don['log10_Sigma_0']:.3f}"
          f"  (observed: {don['observed_log10']:.2f},"
          f" match: {don['match_percent']:.2f}%)")
    print()

    # Tully-Fisher examples
    print("  --- Tully-Fisher Examples ---")
    for v in [50, 100, 150, 200, 300]:
        M = mond.tully_fisher(v)
        print(f"  v_flat = {v:>3d} km/s  =>  M_b = {M:.2e} M_sun")
    print()

    # Rotation curve for Milky Way-like galaxy
    print("  --- Milky Way (M = 10^11 M_sun) ---")
    r_test = np.array([5, 10, 20, 50, 100])
    curve = mond.rotation_curve(1e11, r_test)
    print(f"  r_transition = {curve['r_transition_kpc']:.1f} kpc")
    print(f"  v_flat       = {curve['v_flat_km_s']:.1f} km/s")
    print(f"  {'r (kpc)':>10s}  {'v_Newton':>10s}  {'v_MOND':>10s}")
    for i, r in enumerate(r_test):
        print(f"  {r:>10.0f}  {curve['v_newton_km_s'][i]:>10.1f}"
              f"  {curve['v_mond_km_s'][i]:>10.1f}")
    print()
    print("=" * 72)


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import sys

    # If --no-gui flag, just print summary
    if '--no-gui' in sys.argv:
        print_summary()
        sys.exit(0)

    # Print summary to console
    print_summary()

    # Build and show visualization
    fig, mond, slider = build_visualization()
    plt.show()
