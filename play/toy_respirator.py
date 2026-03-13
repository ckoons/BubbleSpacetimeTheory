#!/usr/bin/env python3
"""
BST RESPIRATOR
==============
The lapse function N = N₀√(1 − ρ/ρ₁₃₇) governs BOTH the neutron's
internal dynamics AND the universe's expansion. Same equation, vastly
different density regimes.

At neutron density (~10⁻³ ρ₁₃₇): fast breathing — strong force pulses
At cosmic vacuum (~10⁻¹²³ ρ₁₃₇): slow breathing — the universe exhales
At event horizon (ρ → ρ₁₃₇): breathing stops — N → 0, time freezes

The ratio of breathing frequencies is Dirac's large number: ~10⁴¹

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
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, FancyArrowPatch
import matplotlib.patheffects as pe

# ─── Physical constants and BST parameters ───
N_MAX = 137
RHO_137 = 1.0           # normalized: ρ₁₃₇ = 1
N_0 = 1.0               # lapse normalization

# Key density regimes (as fraction of ρ₁₃₇)
RHO_COSMIC  = 1e-123    # cosmic vacuum energy density
RHO_NEUTRON = 1e-3      # neutron interior
RHO_HORIZON = 1.0       # event horizon

# Conceptual frequencies (Hz) — for ratio display
OMEGA_NEUTRON = 1e23     # nuclear timescale ~10⁻²³ s
OMEGA_COSMIC  = 1e-18   # Hubble timescale ~10¹⁸ s
DIRAC_RATIO   = OMEGA_NEUTRON / OMEGA_COSMIC  # ~10⁴¹

def lapse(rho_frac):
    """N = N₀ √(1 − ρ/ρ₁₃₇)"""
    rho_frac = np.clip(rho_frac, 0, 1.0)
    return N_0 * np.sqrt(1.0 - rho_frac)

def visual_frequency(rho_frac):
    """Map density to a visual pulse frequency (Hz for animation).
    Range from ~0.05 Hz (cosmic) to ~8 Hz (neutron) to 0 Hz (horizon)."""
    N = lapse(rho_frac)
    if N < 1e-6:
        return 0.0
    log_rho = np.log10(max(rho_frac, 1e-130))
    # Map log(ρ) from [-123, 0] to visual frequency
    # Neutron (~-3) should be fast, cosmic (~-123) slow, horizon (0) stops
    # Use lapse * base_rate where base_rate depends on regime
    t = (log_rho + 123) / 123.0  # 0 at cosmic, 1 at horizon
    base_rate = 0.15 + 7.0 * t**0.4  # slow at cosmic end, fast at neutron
    return N * base_rate

def regime_label(rho_frac):
    """Identify the density regime."""
    log_rho = np.log10(max(rho_frac, 1e-130))
    if log_rho < -60:
        return "COSMIC VACUUM", "#4488ff"
    elif log_rho < -1:
        return "NEUTRON INTERIOR", "#ff8844"
    elif log_rho < -0.01:
        return "DENSE MATTER", "#ff4444"
    else:
        return "EVENT HORIZON", "#ff0000"

def feedback_phase(rho_frac):
    """Determine exhale/inhale phase and description."""
    log_rho = np.log10(max(rho_frac, 1e-130))
    if log_rho < -30:
        return ("EXHALE", "#44aaff",
                "expansion \u2192 \u03c1 drops \u2192 \u039b rises \u2192 more expansion",
                "The vacuum breathes out: dark energy dominates")
    elif log_rho < -0.01:
        return ("INHALE", "#ffaa44",
                "matter concentrates \u2192 \u03c1 rises \u2192 \u039b drops \u2192 gravity wins",
                "Matter breathes in: gravitational collapse")
    else:
        return ("APNEA", "#ff2222",
                "\u03c1 \u2192 \u03c1\u2081\u2083\u2037 \u2192 N \u2192 0 \u2192 time stops",
                "Breathing ceases: the horizon is silence")


# ─── Build the figure ───
fig = plt.figure(figsize=(16, 11), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('BST Respirator — The Universe Breathes')

# Title
fig.text(0.5, 0.97, 'BST RESPIRATOR', fontsize=28, fontweight='bold',
         color='#00ccff', ha='center', va='top', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#003366')])
fig.text(0.5, 0.935, 'N = N\u2080\u221a(1 \u2212 \u03c1/\u03c1\u2081\u2083\u2037)  '
         '\u2014  same equation, every scale',
         fontsize=13, color='#6699cc', ha='center', va='top',
         fontfamily='monospace')

# ─── Slider: logarithmic density ───
ax_slider = fig.add_axes([0.15, 0.87, 0.70, 0.025])
ax_slider.set_facecolor('#1a1a2e')

# Slider goes from -123 to 0 (log10 of ρ/ρ₁₃₇)
slider_rho = Slider(ax_slider, 'log\u2081\u2080(\u03c1/\u03c1\u2081\u2083\u2037)',
                    -123, 0, valinit=-3, valfmt='%.1f',
                    color='#2266aa')
slider_rho.label.set_color('white')
slider_rho.label.set_fontsize(12)
slider_rho.label.set_fontfamily('monospace')
slider_rho.valtext.set_color('white')
slider_rho.valtext.set_fontsize(12)

# ─── Breathing circle axis ───
ax_circle = fig.add_axes([0.05, 0.30, 0.40, 0.52])
ax_circle.set_facecolor('#0a0a1a')
ax_circle.set_xlim(-1.5, 1.5)
ax_circle.set_ylim(-1.5, 1.5)
ax_circle.set_aspect('equal')
ax_circle.axis('off')

# ─── Info panel (right side) ───
ax_info = fig.add_axes([0.50, 0.30, 0.48, 0.52])
ax_info.set_facecolor('#0a0a1a')
ax_info.set_xlim(0, 1)
ax_info.set_ylim(0, 1)
ax_info.axis('off')

# ─── Bottom panel: regime bar ───
ax_bar = fig.add_axes([0.05, 0.04, 0.90, 0.22])
ax_bar.set_facecolor('#0a0a1a')
ax_bar.set_xlim(-123, 0)
ax_bar.set_ylim(0, 1)
ax_bar.axis('off')

# ─── Animation state ───
anim_state = {'phase': 0.0, 'rho_frac': 1e-3}

# ─── Draw the density regime bar ───
def draw_regime_bar(log_rho_val):
    ax_bar.clear()
    ax_bar.set_facecolor('#0a0a1a')
    ax_bar.set_xlim(-128, 5)
    ax_bar.set_ylim(-0.2, 1.3)
    ax_bar.axis('off')

    # Title
    ax_bar.text(-61.5, 1.2, 'DENSITY SPECTRUM', fontsize=12, fontweight='bold',
                color='#8899aa', ha='center', fontfamily='monospace')

    # Gradient bar segments
    n_seg = 200
    x_vals = np.linspace(-123, 0, n_seg)
    for i in range(n_seg - 1):
        t = (x_vals[i] + 123) / 123.0
        # Color gradient: blue (cosmic) -> orange (neutron) -> red (horizon)
        if t < 0.5:
            r = 0.1 + 0.8 * (2 * t)
            g = 0.3 + 0.3 * (2 * t)
            b = 0.9 - 0.6 * (2 * t)
        else:
            r = 0.9 + 0.1 * (2 * (t - 0.5))
            g = 0.6 - 0.5 * (2 * (t - 0.5))
            b = 0.3 - 0.3 * (2 * (t - 0.5))
        ax_bar.barh(0.4, x_vals[i + 1] - x_vals[i], height=0.25,
                    left=x_vals[i], color=(r, g, b), alpha=0.7)

    # Key regime markers
    markers = [
        (-123, 'Cosmic\nVacuum', '#4488ff', '\u03c1 \u2248 10\u207b\u00b9\u00b2\u00b3\u03c1\u2081\u2083\u2037'),
        (-61, 'Quantum\nGravity', '#aa66ff', '\u03c1 \u2248 10\u207b\u2076\u00b9\u03c1\u2081\u2083\u2037'),
        (-3, 'Neutron\nInterior', '#ff8844', '\u03c1 \u2248 10\u207b\u00b3\u03c1\u2081\u2083\u2037'),
        (0, 'Event\nHorizon', '#ff2222', '\u03c1 = \u03c1\u2081\u2083\u2037'),
    ]

    for mx, label, color, sublabel in markers:
        ax_bar.plot([mx, mx], [0.25, 0.6], color=color, lw=1.5, alpha=0.8)
        ax_bar.plot(mx, 0.65, 'v', color=color, markersize=8)
        ax_bar.text(mx, 0.78, label, fontsize=9, color=color,
                    ha='center', va='bottom', fontfamily='monospace',
                    fontweight='bold')
        ax_bar.text(mx, -0.05, sublabel, fontsize=7, color='#666688',
                    ha='center', va='top', fontfamily='monospace')

    # Current position indicator
    ax_bar.plot(log_rho_val, 0.4, 'D', color='#ffffff', markersize=12,
                markeredgecolor='#00ccff', markeredgewidth=2, zorder=10)
    ax_bar.plot([log_rho_val, log_rho_val], [0.15, 0.65],
                color='#00ccff', lw=2, alpha=0.6, zorder=9)
    ax_bar.text(log_rho_val, 0.08, 'YOU ARE HERE', fontsize=8,
                fontweight='bold', color='#00ccff', ha='center',
                fontfamily='monospace')


def draw_info_panel(rho_frac):
    ax_info.clear()
    ax_info.set_facecolor('#0a0a1a')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    ax_info.axis('off')

    N = lapse(rho_frac)
    log_rho = np.log10(max(rho_frac, 1e-130))
    regime, regime_color = regime_label(rho_frac)
    phase_name, phase_color, phase_desc, phase_note = feedback_phase(rho_frac)
    freq = visual_frequency(rho_frac)

    # ── Lapse function ──
    ax_info.text(0.5, 0.97, 'LAPSE FUNCTION', fontsize=14, fontweight='bold',
                 color='#aaccee', ha='center', fontfamily='monospace')

    ax_info.text(0.5, 0.90, f'N = \u221a(1 \u2212 10^{{{log_rho:.1f}}}) = {N:.8f}',
                 fontsize=16, fontweight='bold', color='#ffffff', ha='center',
                 fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a3a',
                           edgecolor='#3366aa', linewidth=2))

    # ── Regime ──
    ax_info.text(0.5, 0.79, f'\u25c8  {regime}  \u25c8', fontsize=16,
                 fontweight='bold', color=regime_color, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2,
                               foreground=regime_color + '44')])

    # ── Feedback loop ──
    ax_info.text(0.5, 0.70, f'FEEDBACK: {phase_name}', fontsize=13,
                 fontweight='bold', color=phase_color, ha='center',
                 fontfamily='monospace')
    ax_info.text(0.5, 0.64, phase_desc, fontsize=10,
                 color=phase_color, ha='center', fontfamily='monospace',
                 alpha=0.8)
    ax_info.text(0.5, 0.58, phase_note, fontsize=9,
                 color='#8899aa', ha='center', fontfamily='monospace',
                 style='italic')

    # ── Visual frequency ──
    ax_info.text(0.5, 0.48, f'Visual pulse: {freq:.2f} Hz', fontsize=11,
                 color='#88aacc', ha='center', fontfamily='monospace')

    # ── Physical interpretation ──
    ax_info.text(0.05, 0.38, 'PHYSICAL MEANING:', fontsize=11,
                 fontweight='bold', color='#aaccdd', fontfamily='monospace')

    if log_rho < -60:
        lines = [
            "The cosmos exhales slowly.",
            "Dark energy stretches spacetime.",
            f"\u03c9 \u2248 {OMEGA_COSMIC:.0e} Hz (Hubble timescale)",
            "One breath per 10\u00b9\u2078 seconds.",
        ]
    elif log_rho < -1:
        lines = [
            "Nuclear matter pulses rapidly.",
            "Quarks and gluons breathe together.",
            f"\u03c9 \u2248 {OMEGA_NEUTRON:.0e} Hz (nuclear timescale)",
            "One breath per 10\u207b\u00b2\u00b3 seconds.",
        ]
    elif log_rho < -0.01:
        lines = [
            "Approaching critical density.",
            "Breathing slows as N \u2192 0.",
            "Gravitational time dilation grows.",
            "The boundary between matter and geometry.",
        ]
    else:
        lines = [
            "TIME STOPS.",
            "\u03c1 = \u03c1\u2081\u2083\u2037: the geometric limit.",
            "N = 0: no proper time elapses.",
            "The horizon is perfect silence.",
        ]

    for i, line in enumerate(lines):
        ax_info.text(0.08, 0.32 - i * 0.05, line, fontsize=10,
                     color='#99aabb', fontfamily='monospace')

    # ── Dirac large number ──
    ax_info.text(0.5, 0.09, 'DIRAC LARGE NUMBER', fontsize=11,
                 fontweight='bold', color='#cc88ff', ha='center',
                 fontfamily='monospace')
    ax_info.text(0.5, 0.03,
                 f'\u03c9_neutron / \u03c9_universe \u2248 '
                 f'10\u00b2\u00b3 / 10\u207b\u00b9\u2078 = 10\u2074\u00b9',
                 fontsize=12, color='#ddaaff', ha='center',
                 fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0a2a',
                           edgecolor='#6633aa', linewidth=1.5))


def draw_breathing_circle(rho_frac, phase):
    ax_circle.clear()
    ax_circle.set_facecolor('#0a0a1a')
    ax_circle.set_xlim(-1.6, 1.6)
    ax_circle.set_ylim(-1.6, 1.6)
    ax_circle.set_aspect('equal')
    ax_circle.axis('off')

    N = lapse(rho_frac)
    freq = visual_frequency(rho_frac)
    regime, regime_color = regime_label(rho_frac)

    # Breathing radius oscillates with the phase
    breath = 0.5 * np.sin(phase)  # -0.5 to 0.5
    base_radius = 0.4 + 0.5 * N   # shrinks as N -> 0
    radius = base_radius + breath * 0.3 * N  # amplitude shrinks with N

    # Glow rings
    n_rings = 8
    for i in range(n_rings, 0, -1):
        ring_r = radius + i * 0.08
        alpha = 0.15 * (1 - i / n_rings) * N
        glow_circle = plt.Circle((0, 0), ring_r, fill=True,
                                 color=regime_color, alpha=alpha)
        ax_circle.add_patch(glow_circle)

    # Main breathing circle
    main_alpha = 0.3 + 0.5 * N
    main_circle = plt.Circle((0, 0), radius, fill=True,
                             facecolor=regime_color, alpha=main_alpha * 0.4,
                             edgecolor=regime_color, linewidth=2)
    ax_circle.add_patch(main_circle)

    # Inner structure: concentric rings showing lapse layers
    n_inner = 5
    for i in range(1, n_inner + 1):
        r_inner = radius * i / (n_inner + 1)
        inner_ring = plt.Circle((0, 0), r_inner, fill=False,
                                edgecolor=regime_color,
                                alpha=0.15 + 0.1 * np.sin(phase + i),
                                linewidth=0.8, linestyle='--')
        ax_circle.add_patch(inner_ring)

    # Radial lines (like breathing directions)
    n_rays = 12
    for i in range(n_rays):
        angle = 2 * np.pi * i / n_rays + phase * 0.1
        r_out = radius + 0.15 * N * np.sin(phase + i * 0.5)
        x_out = r_out * np.cos(angle)
        y_out = r_out * np.sin(angle)
        alpha_ray = 0.2 + 0.15 * np.sin(phase + i)
        ax_circle.plot([0, x_out], [0, y_out], color=regime_color,
                       alpha=alpha_ray * N, linewidth=0.6)

    # Center dot
    center = plt.Circle((0, 0), 0.04, fill=True, color='white',
                         alpha=0.6 + 0.4 * np.sin(phase), zorder=10)
    ax_circle.add_patch(center)

    # Phase indicator text
    phase_name, phase_color, _, _ = feedback_phase(rho_frac)
    if breath > 0.1:
        breath_label = "EXHALE \u2197"
    elif breath < -0.1:
        breath_label = "INHALE \u2199"
    else:
        if freq < 0.01:
            breath_label = "FROZEN"
        else:
            breath_label = "\u2194"

    ax_circle.text(0, -1.35, breath_label, fontsize=14,
                   fontweight='bold', color=phase_color, ha='center',
                   fontfamily='monospace',
                   path_effects=[pe.withStroke(linewidth=2,
                                 foreground='#0a0a1a')])

    # Lapse value shown on the circle
    ax_circle.text(0, 1.35, f'N = {N:.6f}', fontsize=14,
                   fontweight='bold', color='#ffffff', ha='center',
                   fontfamily='monospace',
                   path_effects=[pe.withStroke(linewidth=2,
                                 foreground='#0a0a1a')])

    # Frequency label
    if freq > 0.01:
        ax_circle.text(0, 1.15, f'f_visual = {freq:.2f} Hz', fontsize=10,
                       color='#88aacc', ha='center', fontfamily='monospace')
    else:
        ax_circle.text(0, 1.15, 'f = 0  (time stops)', fontsize=10,
                       color='#ff4444', ha='center', fontfamily='monospace')


# ─── Slider callback ───
def on_slider_change(val):
    log_rho = slider_rho.val
    rho_frac = 10 ** log_rho
    anim_state['rho_frac'] = rho_frac
    draw_info_panel(rho_frac)
    draw_regime_bar(log_rho)
    fig.canvas.draw_idle()

slider_rho.on_changed(on_slider_change)


# ─── Animation ───
def animate(frame):
    rho_frac = anim_state['rho_frac']
    freq = visual_frequency(rho_frac)

    # Advance phase based on frequency
    dt = 0.05  # ~20 fps target -> 50ms per frame
    anim_state['phase'] += 2 * np.pi * freq * dt

    draw_breathing_circle(rho_frac, anim_state['phase'])
    return []


# ─── Initial draw ───
rho_init = 10 ** slider_rho.val
anim_state['rho_frac'] = rho_init
draw_info_panel(rho_init)
draw_regime_bar(slider_rho.val)
draw_breathing_circle(rho_init, 0)

# ─── Start animation ───
anim = FuncAnimation(fig, animate, interval=50, blit=False, cache_frame_data=False)

plt.show()
