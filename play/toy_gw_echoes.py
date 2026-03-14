#!/usr/bin/env python3
"""
GRAVITATIONAL WAVE ECHOES FROM BST BLACK HOLES — Toy 128
==========================================================
In BST, black holes have no singularity and no true interior. The channel
saturates at N_max = 137, creating a "commitment horizon" — a Haldane
saturation surface that acts as a perfect reflector for gravitational waves.

This means:
  - The horizon is not a one-way membrane — it's a saturation boundary
  - GW signals from mergers show ECHOES: repeated reflections off the
    commitment boundary, leaking through the photon-sphere barrier
  - Echo delay: dt = N_max * r_s / c = 137 * (2GM/c^3)  [linear in M]
  - For a 30 M_sun merger: dt ~ 41 ms between echoes
  - Amplitude decays geometrically: each echo loses ~exp(-pi*0.747) ~ 90%
    of its energy to the barrier (only ~10% leaks out each bounce)
  - LIGO/Virgo have searched for echoes — tentative 2.5 sigma hints

BST predictions:
  1. Echoes MUST exist (no information paradox if they don't)
  2. Echo spacing = 137 * r_s / c  (encodes N_max = 137)
  3. Echo decay rate set by angular momentum barrier alone (|R| = 1)
  4. Phase flips pi per echo (hard-wall Dirichlet boundary)
  5. Frequency comb at df = c^3 / (2GM * 137)

The universe does not lose information. It echoes.

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
from matplotlib.patches import Circle, FancyArrowPatch, Arc, Wedge
from matplotlib.collections import LineCollection
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

# Physical constants (SI)
G_SI = 6.674e-11        # m^3 kg^-1 s^-2
c_SI = 2.998e8          # m/s
hbar_SI = 1.055e-34     # J s
k_B = 1.381e-23         # J/K
M_SUN = 1.989e30        # kg
l_Pl = 1.616e-35        # m
m_Pl = 2.176e-8         # kg
t_Pl = 5.391e-44        # s

# Derived
r_s_per_Msun = 2.0 * G_SI * M_SUN / c_SI**2   # ~2.953 km
t_s_per_Msun = 2.0 * G_SI * M_SUN / c_SI**3   # ~9.87 us

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
TEAL = '#00ccaa'
CYAN_DIM = '#338899'


# ═══════════════════════════════════════════════════════════════════
# BSTGWEchoes — Programmatic CI-scriptable API
# ═══════════════════════════════════════════════════════════════════

class BSTGWEchoes:
    """
    Gravitational wave echoes from BST black holes.

    In BST, the Haldane saturation surface at rho = rho_137 acts as a
    perfect reflector. GW signals bounce between this inner wall and the
    angular momentum barrier (photon sphere), producing echoes that leak
    out to distant observers.

    Parameters
    ----------
    M_solar : float
        Remnant black hole mass in solar masses (default 30.0).
    spin : float
        Dimensionless spin a_* = Jc/(GM^2), 0 <= a_* < 1 (default 0.0).
    """

    def __init__(self, M_solar=30.0, spin=0.0):
        self.M_solar = M_solar
        self.M_kg = M_solar * M_SUN
        self.spin = np.clip(spin, 0.0, 0.999)

        # Schwarzschild radius
        self.r_s = 2.0 * G_SI * self.M_kg / c_SI**2

        # Kerr outer horizon
        self.r_plus = (G_SI * self.M_kg / c_SI**2) * (
            1.0 + np.sqrt(1.0 - self.spin**2))

        # QNM parameters for l=2 fundamental mode
        # omega_QNM * r_s / c ~ 0.747 (Schwarzschild)
        self.omega_rs_over_c = 0.747

        # Barrier transmission coefficient |T_2|^2
        self.T2_squared = np.exp(-np.pi * self.omega_rs_over_c)  # ~0.095

        # Haldane surface reflectivity: EXACTLY 1 in BST
        self.R_haldane = 1.0

    # ─── Echo delay time ───
    def echo_delay_s(self):
        """
        Echo delay in seconds: dt = N_max * r_s / c  (Route B).

        For Kerr: dt = N_max * r_+ / c (approximate spin correction).

        Returns
        -------
        float
            Echo delay in seconds.
        """
        r_eff = self.r_plus if self.spin > 0.01 else self.r_s
        return N_MAX * r_eff / c_SI

    def echo_delay_ms(self):
        """Echo delay in milliseconds."""
        return self.echo_delay_s() * 1e3

    # ─── Echo amplitude ───
    def echo_amplitude(self, k, A0=1.0):
        """
        Amplitude of the k-th echo (strain relative to ringdown).

        A_k = A0 * |T_2|^(2k) * |R_Haldane|^k * (-1)^k

        With |R_Haldane| = 1, the decay is set purely by barrier
        transmission. The (-1)^k gives the pi phase flip per echo.

        Parameters
        ----------
        k : int or array
            Echo number (1, 2, 3, ...).
        A0 : float
            Initial ringdown amplitude (default 1.0).

        Returns
        -------
        float or array
            Signed echo amplitude (alternating sign from phase flip).
        """
        k = np.asarray(k, dtype=float)
        # Strain amplitude: sqrt of energy transmission per round trip
        strain_factor = np.sqrt(self.T2_squared)  # ~0.31 per echo
        magnitude = A0 * strain_factor**k
        sign = (-1.0)**k  # pi phase flip per echo
        return magnitude * sign

    def echo_amplitude_unsigned(self, k, A0=1.0):
        """Unsigned amplitude of the k-th echo."""
        k = np.asarray(k, dtype=float)
        strain_factor = np.sqrt(self.T2_squared)
        return A0 * strain_factor**k

    # ─── QNM frequency ───
    def qnm_frequency_hz(self):
        """
        Fundamental l=2 quasi-normal mode frequency.

        f_QNM ~ 12.07 kHz * (M_sun / M)  [Schwarzschild]

        Returns
        -------
        float
            QNM frequency in Hz.
        """
        return 12070.0 / self.M_solar

    # ─── Frequency comb ───
    def comb_spacing_hz(self):
        """
        Echo frequency comb spacing: df = 1 / dt_echo.

        Returns
        -------
        float
            Comb spacing in Hz.
        """
        return 1.0 / self.echo_delay_s()

    # ─── Ringdown waveform ───
    def ringdown_waveform(self, t, t_merger=0.0, A0=1.0):
        """
        Approximate ringdown waveform h(t) after merger.

        Uses damped sinusoid with QNM frequency and damping time.
        Damping time: tau_QNM ~ 0.056 * r_s / c (for l=2 Schwarzschild).

        Parameters
        ----------
        t : array
            Time array in seconds.
        t_merger : float
            Merger time (default 0.0).
        A0 : float
            Peak ringdown strain amplitude.

        Returns
        -------
        np.ndarray
            Strain h(t).
        """
        t = np.asarray(t, dtype=float)
        dt = t - t_merger

        f_qnm = self.qnm_frequency_hz()
        tau_qnm = 0.056 * self.r_s / c_SI  # damping time in seconds

        h = np.zeros_like(dt)
        mask = dt >= 0
        h[mask] = A0 * np.exp(-dt[mask] / tau_qnm) * np.cos(
            2.0 * np.pi * f_qnm * dt[mask])
        return h

    # ─── Full echo train ───
    def echo_train(self, t, t_merger=0.0, A0=1.0, n_echoes=4):
        """
        Full waveform: ringdown + echo train.

        Each echo is a delayed, attenuated, phase-flipped copy of the
        ringdown, with delay = k * dt_echo and amplitude from barrier
        transmission.

        Parameters
        ----------
        t : array
            Time array in seconds.
        t_merger : float
            Merger time.
        A0 : float
            Peak ringdown amplitude.
        n_echoes : int
            Number of echoes to include.

        Returns
        -------
        np.ndarray
            Total strain h(t).
        """
        h_total = self.ringdown_waveform(t, t_merger, A0)

        dt_echo = self.echo_delay_s()
        f_qnm = self.qnm_frequency_hz()
        tau_qnm = 0.056 * self.r_s / c_SI

        for k in range(1, n_echoes + 1):
            t_echo = t_merger + k * dt_echo
            amp_k = self.echo_amplitude(k, A0)  # signed (includes phase)
            dt_k = t - t_echo

            h_echo = np.zeros_like(t)
            mask = dt_k >= 0
            h_echo[mask] = abs(amp_k) * np.exp(-dt_k[mask] / tau_qnm) * np.cos(
                2.0 * np.pi * f_qnm * dt_k[mask] + k * np.pi)
            h_total += h_echo

        return h_total

    # ─── Echo delay for mass array ───
    @staticmethod
    def echo_delay_vs_mass(M_array, spin=0.0):
        """
        Echo delay vs mass: dt = 137 * 2GM/(c^3).

        Parameters
        ----------
        M_array : array
            Masses in solar masses.
        spin : float
            Dimensionless spin.

        Returns
        -------
        np.ndarray
            Echo delays in milliseconds.
        """
        M_array = np.asarray(M_array, dtype=float)
        r_s = 2.0 * G_SI * M_array * M_SUN / c_SI**2
        if spin > 0.01:
            r_plus = (G_SI * M_array * M_SUN / c_SI**2) * (
                1.0 + np.sqrt(1.0 - spin**2))
            return N_MAX * r_plus / c_SI * 1e3
        return N_MAX * r_s / c_SI * 1e3

    # ─── Effective potential ───
    def effective_potential(self, r_array, l=2):
        """
        Regge-Wheeler effective potential V(r) for gravitational perturbations.

        V(r) = (1 - r_s/r) * [l(l+1)/r^2 - 3*r_s/r^3]   (GR form)

        In BST, V does not drop to zero at r_s — the Haldane surface
        creates a reflecting wall.

        Parameters
        ----------
        r_array : array
            Radial coordinate in meters.
        l : int
            Angular momentum quantum number.

        Returns
        -------
        dict with 'V_gr' and 'V_bst' arrays (normalized).
        """
        r = np.asarray(r_array, dtype=float)
        rs = self.r_s

        # GR potential
        f = np.clip(1.0 - rs / r, 0, None)
        V_gr = f * (l * (l + 1) / r**2 - 3.0 * rs / r**3)
        V_gr = V_gr / np.max(np.abs(V_gr))  # normalize

        # BST: potential rises to a wall at r = r_s
        V_bst = V_gr.copy()
        # Near horizon: instead of dropping to 0, the Haldane surface
        # creates a steep wall
        wall_mask = r < 1.15 * rs
        x = (r[wall_mask] - rs) / rs
        x = np.clip(x, 0, None)
        # Smooth wall that rises steeply near r_s
        V_bst[wall_mask] = np.where(
            x > 0.01,
            V_gr[wall_mask] + 0.8 * np.exp(-10.0 * x),
            0.9)

        return {'V_gr': V_gr, 'V_bst': V_bst}

    # ─── LIGO events database ───
    @staticmethod
    def ligo_events():
        """
        Notable LIGO/Virgo events and their BST echo predictions.

        Returns
        -------
        list of dict
            Each dict has name, M_remnant, spin, dt_echo_ms, f_comb_hz.
        """
        events = [
            {'name': 'GW150914', 'M_remnant': 62.0, 'spin': 0.67},
            {'name': 'GW151226', 'M_remnant': 20.8, 'spin': 0.74},
            {'name': 'GW170104', 'M_remnant': 48.7, 'spin': 0.64},
            {'name': 'GW170814', 'M_remnant': 53.2, 'spin': 0.70},
            {'name': 'GW170817', 'M_remnant': 2.74, 'spin': 0.0,
             'note': 'BNS'},
            {'name': 'GW190521', 'M_remnant': 150.0, 'spin': 0.72},
        ]
        for ev in events:
            e = BSTGWEchoes(ev['M_remnant'], ev['spin'])
            ev['dt_echo_ms'] = e.echo_delay_ms()
            ev['f_comb_hz'] = e.comb_spacing_hz()
            ev['f_qnm_hz'] = e.qnm_frequency_hz()
            ev['echo1_strain'] = abs(e.echo_amplitude(1))
        return events

    # ─── Pretty report ───
    def report(self):
        """Print a formatted summary of echo predictions for this BH."""
        lines = [
            '',
            '=' * 72,
            f'  BST GRAVITATIONAL WAVE ECHOES — {self.M_solar:.1f} M_sun',
            '=' * 72,
            '',
            f'  Mass:                 {self.M_solar:.1f} M_sun',
            f'  Spin:                 a_* = {self.spin:.2f}',
            f'  Schwarzschild radius: {self.r_s / 1e3:.2f} km',
            f'  Kerr outer horizon:   {self.r_plus / 1e3:.2f} km',
            '',
            f'  N_max (channel cap):  {N_MAX}',
            f'  Haldane reflectivity: |R| = {self.R_haldane:.0f}  (perfect)',
            '',
            '  ─── Echo Predictions ───',
            f'  Echo delay (Route B): {self.echo_delay_ms():.1f} ms',
            f'  QNM frequency (l=2):  {self.qnm_frequency_hz():.1f} Hz',
            f'  Comb spacing:         {self.comb_spacing_hz():.1f} Hz',
            '',
            '  ─── Echo Amplitudes (strain / ringdown) ───',
        ]
        for k in range(1, 6):
            amp = abs(self.echo_amplitude(k))
            phase = '+' if k % 2 == 0 else '-'
            lines.append(
                f'  Echo {k}:  |h/h0| = {amp:.4f}  '
                f'(phase {phase}pi)')
        lines += [
            '',
            f'  Barrier transmission |T_2|^2 = {self.T2_squared:.4f}',
            f'  Strain factor per echo: {np.sqrt(self.T2_squared):.4f}',
            '',
            f'  Universal slope: dt/M = {N_MAX} * 2G/c^3 '
            f'= {N_MAX * 2 * G_SI / c_SI**3 * 1e3 / (1 / M_SUN):.4f} ms/M_sun',
            '',
            '  "The universe does not lose information. It echoes."',
            '=' * 72,
            '',
        ]
        print('\n'.join(lines))


# ═══════════════════════════════════════════════════════════════════
# VISUALIZATION HELPERS
# ═══════════════════════════════════════════════════════════════════

def add_glow_line(ax, x, y, color, lw=2.0, alpha=1.0, zorder=5):
    """Draw a line with a glow effect."""
    ax.plot(x, y, color=color, linewidth=lw + 3, alpha=alpha * 0.15,
            zorder=zorder - 1)
    ax.plot(x, y, color=color, linewidth=lw + 1.5, alpha=alpha * 0.3,
            zorder=zorder - 1)
    ax.plot(x, y, color=color, linewidth=lw, alpha=alpha, zorder=zorder)


def style_axis(ax, title, title_color=BLUE_BRIGHT):
    """Apply standard BST dark styling to an axis."""
    ax.set_facecolor(DARK_PANEL)
    ax.set_title(title, fontsize=11, fontweight='bold', color=title_color,
                 fontfamily='monospace', pad=10)
    ax.tick_params(colors=GREY, labelsize=8)
    for spine in ax.spines.values():
        spine.set_color(DARK_GREY)


def formula_box(ax, x, y, text, fontsize=10, color=GOLD):
    """Place a boxed formula on an axis in axes coordinates."""
    ax.text(x, y, text, fontsize=fontsize, color=color, ha='center',
            va='center', fontfamily='monospace', fontweight='bold',
            transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a00',
                      edgecolor=GOLD_DIM, alpha=0.85))


# ═══════════════════════════════════════════════════════════════════
# VISUALIZATION — 6 panels
# ═══════════════════════════════════════════════════════════════════

def run_visualization():
    """Launch the 6-panel BST gravitational wave echoes visualization."""

    # Reference black hole
    M_ref = 30.0
    bh = BSTGWEchoes(M_ref, spin=0.0)

    fig = plt.figure(figsize=(22, 14), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'Gravitational Wave Echoes from BST Black Holes — Toy 128')

    # ─── Title ───
    fig.text(0.5, 0.975,
             'GRAVITATIONAL WAVE ECHOES FROM BST BLACK HOLES',
             fontsize=24, fontweight='bold', color=BLUE_BRIGHT, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#003366')])
    fig.text(0.5, 0.953,
             'The Haldane Saturation Surface Reflects — '
             'No Singularity, No Information Loss',
             fontsize=12, color=CYAN_DIM, ha='center', fontfamily='monospace')

    # ─── Bottom tagline ───
    fig.text(0.5, 0.012,
             'The universe does not lose information.  It echoes.'
             '   |   dt = 137 x r_s / c   |   '
             '|R| = 1   |   Toy 128',
             fontsize=12, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

    # Copyright
    fig.text(0.99, 0.003,
             'Copyright (c) 2026 Casey Koons',
             fontsize=7, color=DARK_GREY, ha='right', fontfamily='monospace')

    # Layout: 3 columns x 2 rows
    left = 0.05
    w = 0.28
    gap_x = 0.035
    bot_row = 0.07
    top_row = 0.53
    h = 0.37

    # ═══════════════════════════════════════════════════════════════
    # PANEL 1 — BST Black Hole: The Two-Barrier Cavity
    # ═══════════════════════════════════════════════════════════════
    ax1 = fig.add_axes([left, top_row, w, h])
    style_axis(ax1, 'BST BLACK HOLE — TWO-BARRIER CAVITY')

    # Effective potential plot showing the cavity
    r_range = np.linspace(1.001, 6.0, 800)  # in units of r_s
    r_meters = r_range * bh.r_s
    potentials = bh.effective_potential(r_meters, l=2)

    # Normalize for display
    V_gr = potentials['V_gr']
    V_bst = potentials['V_bst']

    # GR potential (dashed, fades at horizon)
    ax1.plot(r_range, V_gr, '--', color=RED_WARM, linewidth=1.5,
             alpha=0.5, label='GR (absorbed)', zorder=3)

    # BST potential (solid, with reflecting wall)
    add_glow_line(ax1, r_range, V_bst, BLUE_BRIGHT, lw=2.0, zorder=5)

    # Mark the cavity region
    # Haldane surface (inner wall)
    ax1.axvline(x=1.0, color=GOLD, linewidth=2.5, linestyle='-',
                alpha=0.9, zorder=6)
    ax1.text(1.0, 0.95, 'HALDANE\nSURFACE', fontsize=7, color=GOLD,
             ha='center', va='top', fontfamily='monospace',
             fontweight='bold')
    ax1.text(1.0, -0.22, r'$\rho = \rho_{137}$', fontsize=8, color=GOLD,
             ha='center', fontfamily='monospace')

    # Photon sphere barrier (outer)
    r_peak_idx = np.argmax(V_bst[r_range > 1.2])
    r_peak_idx += np.sum(r_range <= 1.2)
    r_peak = r_range[r_peak_idx]
    ax1.annotate('PHOTON SPHERE\nBARRIER', xy=(r_peak, V_bst[r_peak_idx]),
                 xytext=(r_peak + 0.8, V_bst[r_peak_idx] + 0.15),
                 fontsize=7, color=BLUE_BRIGHT, fontfamily='monospace',
                 fontweight='bold', ha='center',
                 arrowprops=dict(arrowstyle='->', color=BLUE_BRIGHT, lw=1.5))

    # Shade the cavity
    cavity_mask = (r_range >= 1.0) & (r_range <= r_peak)
    ax1.fill_between(r_range[cavity_mask], -0.15,
                     np.minimum(V_bst[cavity_mask], 0.15),
                     color=PURPLE_GLOW, alpha=0.15)
    # Cavity label
    r_mid = (1.0 + r_peak) / 2
    ax1.text(r_mid, -0.08, 'CAVITY', fontsize=9, color=PURPLE_GLOW,
             ha='center', fontfamily='monospace', fontweight='bold',
             alpha=0.8)

    # Bouncing wave arrows
    arrow_y = 0.0
    for i, (x1, x2) in enumerate([(1.15, r_peak - 0.3),
                                    (r_peak - 0.3, 1.15)]):
        arr_color = TEAL if i == 0 else GREEN
        arr_alpha = 0.7 if i == 0 else 0.5
        ax1.annotate('', xy=(x2, arrow_y + 0.03 * (i + 1)),
                     xytext=(x1, arrow_y + 0.03 * (i + 1)),
                     arrowprops=dict(arrowstyle='->', color=arr_color,
                                     lw=1.5, alpha=arr_alpha))

    # Leak arrow (echo escaping)
    ax1.annotate('echo\nleaks out', xy=(4.5, 0.15),
                 xytext=(r_peak + 0.2, V_bst[r_peak_idx] - 0.1),
                 fontsize=7, color=GREEN, fontfamily='monospace',
                 arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5,
                                 connectionstyle='arc3,rad=0.2'))

    ax1.set_xlabel('r / r_s', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax1.set_ylabel('Effective Potential V(r)', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax1.set_xlim(0.8, 5.5)
    ax1.set_ylim(-0.25, 1.15)
    ax1.legend(fontsize=8, loc='upper right', facecolor=DARK_PANEL,
               edgecolor=DARK_GREY, labelcolor=GREY)

    formula_box(ax1, 0.55, 0.92, '|R_Haldane| = 1  (perfect reflector)')

    # ═══════════════════════════════════════════════════════════════
    # PANEL 2 — The Echo: GW Strain h(t)
    # ═══════════════════════════════════════════════════════════════
    ax2 = fig.add_axes([left + w + gap_x, top_row, w, h])
    style_axis(ax2, 'THE ECHO — GW STRAIN h(t)')

    # Time array: from -20 ms to 250 ms
    dt_echo = bh.echo_delay_ms()
    t_max_ms = dt_echo * 4.5
    t_ms = np.linspace(-10, t_max_ms, 12000)
    t_s = t_ms * 1e-3

    # Generate waveform
    h_total = bh.echo_train(t_s, t_merger=0.0, A0=1.0, n_echoes=4)

    # Also generate ringdown-only for comparison
    h_ring = bh.ringdown_waveform(t_s, t_merger=0.0, A0=1.0)

    # Plot ringdown only (faint)
    ax2.plot(t_ms, h_ring, color=RED_WARM, linewidth=0.8, alpha=0.3,
             label='GR ringdown only', zorder=3)

    # Plot full echo train
    add_glow_line(ax2, t_ms, h_total, BLUE_BRIGHT, lw=1.5, zorder=5)

    # Mark each echo arrival
    for k in range(1, 5):
        t_k = k * dt_echo
        amp_k = abs(bh.echo_amplitude(k))
        ax2.axvline(x=t_k, color=GOLD_DIM, linewidth=0.8, linestyle=':',
                    alpha=0.6)
        sign_str = '-' if k % 2 == 1 else '+'
        ax2.text(t_k, 0.88 + 0.05 * (k % 2), f'Echo {k}\n{sign_str}{amp_k:.3f}',
                 fontsize=7, color=GOLD, ha='center', va='bottom',
                 fontfamily='monospace', fontweight='bold',
                 transform=ax2.get_xaxis_transform())

    # Mark merger
    ax2.axvline(x=0, color=RED_WARM, linewidth=1.5, linestyle='-',
                alpha=0.6)
    ax2.text(0, 0.95, 'MERGER', fontsize=8, color=RED_WARM, ha='center',
             fontfamily='monospace', fontweight='bold',
             transform=ax2.get_xaxis_transform())

    # Annotate echo delay
    y_arrow = 0.55
    ax2.annotate('', xy=(dt_echo, y_arrow),
                 xytext=(0, y_arrow),
                 arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.0),
                 transform=ax2.get_xaxis_transform())
    ax2.text(dt_echo / 2, 0.60, f'dt = {dt_echo:.1f} ms',
             fontsize=9, color=GOLD, ha='center', fontfamily='monospace',
             fontweight='bold', transform=ax2.get_xaxis_transform())

    ax2.set_xlabel('Time after merger (ms)', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax2.set_ylabel('Strain h/h_0', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax2.set_xlim(-10, t_max_ms)
    ax2.legend(fontsize=7, loc='upper right', facecolor=DARK_PANEL,
               edgecolor=DARK_GREY, labelcolor=GREY)

    formula_box(ax2, 0.5, 0.05,
                f'M = {M_ref:.0f} M_sun   |   '
                f'dt = N_max x r_s/c = {dt_echo:.1f} ms',
                fontsize=8)

    # ═══════════════════════════════════════════════════════════════
    # PANEL 3 — Echo Spacing vs Mass
    # ═══════════════════════════════════════════════════════════════
    ax3 = fig.add_axes([left + 2 * (w + gap_x), top_row, w, h])
    style_axis(ax3, 'ECHO SPACING vs MASS')

    # Mass range
    M_arr = np.linspace(2, 200, 500)
    dt_arr = BSTGWEchoes.echo_delay_vs_mass(M_arr)

    # BST prediction line
    add_glow_line(ax3, M_arr, dt_arr, BLUE_BRIGHT, lw=2.5)

    # Mark specific LIGO events
    events = BSTGWEchoes.ligo_events()
    event_colors = [RED_WARM, ORANGE_GLOW, TEAL, GREEN, PURPLE_GLOW, GOLD]
    for i, ev in enumerate(events):
        ec = event_colors[i % len(event_colors)]
        ax3.plot(ev['M_remnant'], ev['dt_echo_ms'], 'o', color=ec,
                 markersize=9, markeredgecolor=WHITE, markeredgewidth=1.0,
                 zorder=10)
        # Label
        offset_y = 12 if i % 2 == 0 else -16
        ax3.annotate(f'{ev["name"]}\n{ev["M_remnant"]:.0f} M_sun\n'
                     f'{ev["dt_echo_ms"]:.0f} ms',
                     xy=(ev['M_remnant'], ev['dt_echo_ms']),
                     xytext=(ev['M_remnant'] + 8, ev['dt_echo_ms'] + offset_y),
                     fontsize=6, color=ec, fontfamily='monospace',
                     fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=ec, lw=1.0),
                     zorder=11)

    # Universal slope annotation
    slope_ms_per_Msun = N_MAX * 2 * G_SI * M_SUN / c_SI**3 * 1e3
    ax3.text(0.05, 0.92,
             f'Universal slope:\ndt/M = {slope_ms_per_Msun:.3f} ms/M_sun',
             fontsize=9, color=GOLD, fontfamily='monospace',
             fontweight='bold', transform=ax3.transAxes,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a00',
                       edgecolor=GOLD_DIM, alpha=0.85))

    # Reference: Route A (Planck) for comparison
    # dt_A = (r_s/c) * ln(r_s / l_Pl)
    dt_A = np.array([(2 * G_SI * M * M_SUN / c_SI**3) *
                      np.log(2 * G_SI * M * M_SUN / (c_SI**2 * l_Pl)) * 1e3
                     for M in M_arr])
    ax3.plot(M_arr, dt_A, '--', color=GREY, linewidth=1.0, alpha=0.5,
             label='Route A (Planck)', zorder=2)

    ax3.set_xlabel('Remnant Mass (M_sun)', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax3.set_ylabel('Echo Delay dt (ms)', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax3.set_xlim(0, 210)
    ax3.set_ylim(0, 300)
    ax3.legend(fontsize=7, loc='lower right', facecolor=DARK_PANEL,
               edgecolor=DARK_GREY, labelcolor=GREY)

    formula_box(ax3, 0.55, 0.12,
                'dt = 137 x 2GM / c^3  (linear in M)',
                fontsize=9)

    # ═══════════════════════════════════════════════════════════════
    # PANEL 4 — Echo Decay (Amplitude vs Echo Number)
    # ═══════════════════════════════════════════════════════════════
    ax4 = fig.add_axes([left, bot_row, w, h])
    style_axis(ax4, 'ECHO DECAY — AMPLITUDE vs ECHO NUMBER')

    k_arr = np.arange(1, 9)

    # BST: |R| = 1, decay from barrier only
    amp_bst = np.array([bh.echo_amplitude_unsigned(k) for k in k_arr])
    ax4.semilogy(k_arr, amp_bst, 'o-', color=BLUE_BRIGHT, markersize=10,
                 linewidth=2.5, markeredgecolor=WHITE, markeredgewidth=1.0,
                 label=f'BST: |R| = 1', zorder=6)

    # Comparison: partial reflectivity models
    for R_val, label, color, ls in [
        (0.8, '|R| = 0.8 (fuzzball)', ORANGE_GLOW, '--'),
        (0.5, '|R| = 0.5 (generic ECO)', RED_WARM, ':'),
        (0.3, '|R| = 0.3 (firewall)', PURPLE_GLOW, '-.'),
    ]:
        amp_partial = np.array([
            bh.echo_amplitude_unsigned(k) * R_val**k for k in k_arr])
        ax4.semilogy(k_arr, amp_partial, ls, color=color, linewidth=1.5,
                     alpha=0.7, label=label, zorder=4)

    # LIGO detection threshold (approximate)
    ax4.axhline(y=0.01, color=GOLD_DIM, linewidth=1.5, linestyle='--',
                alpha=0.6)
    ax4.text(7.5, 0.012, 'LIGO single-event\ndetection threshold\n(approx)',
             fontsize=7, color=GOLD_DIM, ha='right', fontfamily='monospace',
             va='bottom')

    # Stacking improvement
    ax4.axhline(y=0.001, color=GREEN, linewidth=1.0, linestyle=':',
                alpha=0.5)
    ax4.text(7.5, 0.0012, 'with 100-event\nstacking',
             fontsize=7, color=GREEN, ha='right', fontfamily='monospace',
             va='bottom')

    # Annotate BST data points
    for k_val, amp_val in zip(k_arr[:5], amp_bst[:5]):
        ax4.annotate(f'{amp_val:.4f}', xy=(k_val, amp_val),
                     xytext=(k_val + 0.3, amp_val * 1.8),
                     fontsize=7, color=BLUE_BRIGHT, fontfamily='monospace',
                     arrowprops=dict(arrowstyle='-', color=BLUE_GLOW,
                                     lw=0.5))

    ax4.set_xlabel('Echo Number k', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax4.set_ylabel('|h_k / h_0|  (strain ratio)', fontsize=10, color=WHITE,
                   fontfamily='monospace')
    ax4.set_xlim(0.5, 8.5)
    ax4.set_ylim(1e-5, 1.5)
    ax4.legend(fontsize=7, loc='upper right', facecolor=DARK_PANEL,
               edgecolor=DARK_GREY, labelcolor=GREY)

    formula_box(ax4, 0.5, 0.08,
                f'A_k = A_0 x |T_2|^k   |   '
                f'|T_2|^2 = exp(-pi x 0.747) = {bh.T2_squared:.4f}',
                fontsize=8)

    # ═══════════════════════════════════════════════════════════════
    # PANEL 5 — LIGO Echo Search Status
    # ═══════════════════════════════════════════════════════════════
    ax5 = fig.add_axes([left + w + gap_x, bot_row, w, h])
    style_axis(ax5, 'LIGO ECHO SEARCH — STATUS & PREDICTIONS')

    # Turn off standard axes — this is a table/info panel
    ax5.set_xlim(0, 10)
    ax5.set_ylim(0, 10)
    ax5.set_xticks([])
    ax5.set_yticks([])

    # ─── Search results table ───
    ax5.text(5, 9.6, 'PUBLISHED SEARCH RESULTS', fontsize=10,
             fontweight='bold', color=BLUE_BRIGHT, ha='center',
             fontfamily='monospace')

    searches = [
        ('Abedi+ 2016', '2.5 sigma', 'Tentative echoes in GW150914+',
         ORANGE_GLOW),
        ('Conklin+ 2018', '4.2 sigma', 'Combined BNS+BBH, dt ~ M',
         GREEN),
        ('LIGO/Virgo 2020', 'no sig.', 'O1/O2 data — consistent with noise',
         RED_WARM),
        ('Uchikata+ 2023', 'weak', 'Consistent with noise, low power',
         GREY),
    ]

    y_pos = 8.8
    for name, sigma, desc, color in searches:
        ax5.text(0.3, y_pos, name, fontsize=8, color=WHITE,
                 fontfamily='monospace', fontweight='bold')
        ax5.text(4.0, y_pos, sigma, fontsize=8, color=color,
                 fontfamily='monospace', fontweight='bold')
        ax5.text(5.5, y_pos, desc, fontsize=6.5, color=GREY,
                 fontfamily='monospace')
        y_pos -= 0.6

    # Divider
    ax5.axhline(y=y_pos + 0.2, xmin=0.02, xmax=0.98, color=DARK_GREY,
                linewidth=1)

    # ─── BST predictions for upcoming runs ───
    y_pos -= 0.3
    ax5.text(5, y_pos, 'BST PREDICTIONS', fontsize=10, fontweight='bold',
             color=GOLD, ha='center', fontfamily='monospace')

    predictions = [
        ('O4 (2024-2026)', '~80 BBH events', 'Stacked echo SNR ~ 7.6',
         'Should reach 5 sigma if |R|=1', BLUE_BRIGHT),
        ('O5 (2027+)', '~200+ BBH events', 'Stacked echo SNR > 10',
         'Definitive detection or falsification', GREEN),
        ('LISA (2030s+)', 'SMBH mergers', 'Echo delay ~ hours to days',
         'Individual event detection', TEAL),
    ]

    y_pos -= 0.7
    for run, events_str, snr, outcome, color in predictions:
        ax5.text(0.3, y_pos, run, fontsize=8, color=color,
                 fontfamily='monospace', fontweight='bold')
        ax5.text(3.5, y_pos, events_str, fontsize=7, color=GREY,
                 fontfamily='monospace')
        y_pos -= 0.5
        ax5.text(0.6, y_pos, snr, fontsize=7, color=color,
                 fontfamily='monospace')
        y_pos -= 0.4
        ax5.text(0.6, y_pos, outcome, fontsize=6.5, color=GOLD_DIM,
                 fontfamily='monospace')
        y_pos -= 0.7

    # ─── Stacking SNR projection ───
    y_pos -= 0.2
    ax5.axhline(y=y_pos + 0.2, xmin=0.02, xmax=0.98, color=DARK_GREY,
                linewidth=0.5)

    # Mini bar chart: SNR vs N_events
    n_events = [10, 30, 80, 150, 300]
    snr_single = 2.4  # single-event first echo SNR for loud merger
    bar_x = np.linspace(1.5, 8.5, len(n_events))
    bar_w = 0.9
    y_base = 0.4

    for i, (n, bx) in enumerate(zip(n_events, bar_x)):
        snr_stacked = snr_single * np.sqrt(n / 8)
        bar_h = min(snr_stacked / 15.0 * 2.5, 2.5)
        bar_color = GREEN if snr_stacked >= 5.0 else ORANGE_GLOW
        ax5.bar(bx, bar_h, bar_w, bottom=y_base,
                color=bar_color, alpha=0.6, edgecolor=bar_color)
        ax5.text(bx, y_base - 0.25, f'N={n}', fontsize=6, color=WHITE,
                 ha='center', fontfamily='monospace')
        ax5.text(bx, y_base + bar_h + 0.1, f'{snr_stacked:.1f}',
                 fontsize=6, color=bar_color, ha='center',
                 fontfamily='monospace', fontweight='bold')

    # 5-sigma line
    snr_5_h = min(5.0 / 15.0 * 2.5, 2.5)
    ax5.axhline(y=y_base + snr_5_h, xmin=0.1, xmax=0.9,
                color=GOLD, linewidth=1.5, linestyle='--', alpha=0.7)
    ax5.text(9.5, y_base + snr_5_h, '5 sigma', fontsize=7, color=GOLD,
             ha='right', va='center', fontfamily='monospace',
             fontweight='bold')

    ax5.text(5, y_pos, 'STACKED ECHO SNR PROJECTION', fontsize=8,
             fontweight='bold', color=WHITE, ha='center',
             fontfamily='monospace')

    # ═══════════════════════════════════════════════════════════════
    # PANEL 6 — The Smoking Gun
    # ═══════════════════════════════════════════════════════════════
    ax6 = fig.add_axes([left + 2 * (w + gap_x), bot_row, w, h])
    style_axis(ax6, 'THE SMOKING GUN — FIVE FALSIFIABLE PREDICTIONS',
               title_color=GOLD)

    ax6.set_xlim(0, 10)
    ax6.set_ylim(0, 10)
    ax6.set_xticks([])
    ax6.set_yticks([])

    # Five predictions
    predictions_text = [
        ('1.', 'ECHOES EXIST',
         'Stacking O4/O5 BBH ringdowns must\n'
         'show echo signal at >= 5 sigma.',
         BLUE_BRIGHT),
        ('2.', 'dt = 137 x r_s / c',
         'Universal slope 1.352 ms/M_sun.\n'
         'Linear in M. Zero free parameters.',
         GREEN),
        ('3.', '|R| = 1  (PERFECT REFLECTION)',
         'Echo amplitude set by barrier alone.\n'
         'Weaker echoes falsify BST.',
         TEAL),
        ('4.', 'PHASE FLIP  d_phi = pi',
         'Hard-wall Dirichlet boundary.\n'
         'Successive echoes alternate sign.',
         ORANGE_GLOW),
        ('5.', 'FREQUENCY COMB',
         f'df = c^3/(2GM x 137)\n'
         f'For 30 M_sun: df = {bh.comb_spacing_hz():.1f} Hz '
         f'in post-ringdown.',
         PURPLE_GLOW),
    ]

    y_pos = 9.3
    for num, title, desc, color in predictions_text:
        # Number
        ax6.text(0.3, y_pos, num, fontsize=12, color=color,
                 fontfamily='monospace', fontweight='bold')
        # Title
        ax6.text(1.2, y_pos, title, fontsize=9, color=color,
                 fontfamily='monospace', fontweight='bold')
        # Description
        ax6.text(1.2, y_pos - 0.55, desc, fontsize=6.5, color=GREY,
                 fontfamily='monospace', va='top')
        y_pos -= 1.75

    # ─── Bottom box: the 137 in the sky ───
    box_y = 0.3
    ax6.add_patch(plt.Rectangle((0.3, box_y), 9.4, 1.4,
                                 facecolor='#1a1a00', edgecolor=GOLD,
                                 linewidth=2, alpha=0.8, zorder=5))
    ax6.text(5.0, box_y + 1.05,
             'If echoes are found with dt = N x r_s/c',
             fontsize=9, color=WHITE, ha='center', fontfamily='monospace',
             zorder=6)
    ax6.text(5.0, box_y + 0.65,
             'and the measured N = 137 +/- delta_N ...',
             fontsize=9, color=GOLD, ha='center', fontfamily='monospace',
             fontweight='bold', zorder=6)
    ax6.text(5.0, box_y + 0.25,
             'BST is confirmed at the horizon scale.',
             fontsize=10, color=GOLD, ha='center', fontfamily='monospace',
             fontweight='bold', zorder=6,
             path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

    plt.show()


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    # Print report for 30 M_sun merger
    bh = BSTGWEchoes(30.0, spin=0.0)
    bh.report()

    # Print LIGO events table
    print('\n  LIGO/Virgo Events — BST Echo Predictions')
    print('  ' + '=' * 68)
    print(f'  {"Event":<14} {"M_rem":>6} {"a_*":>5} '
          f'{"dt(ms)":>8} {"f_comb(Hz)":>10} {"f_QNM(Hz)":>10} '
          f'{"Echo1":>7}')
    print('  ' + '-' * 68)
    for ev in BSTGWEchoes.ligo_events():
        print(f'  {ev["name"]:<14} {ev["M_remnant"]:>6.1f} '
              f'{ev["spin"]:>5.2f} {ev["dt_echo_ms"]:>8.1f} '
              f'{ev["f_comb_hz"]:>10.1f} {ev["f_qnm_hz"]:>10.1f} '
              f'{ev["echo1_strain"]:>7.4f}')
    print('  ' + '=' * 68)

    # Launch visualization
    run_visualization()
