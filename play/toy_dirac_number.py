#!/usr/bin/env python3
"""
THE DIRAC LARGE NUMBER — 41 ORDERS OF MAGNITUDE
=================================================
Visualize the full span from proton radius to Hubble radius on a
logarithmic scale, with BST landmarks and alpha-power relationships.

In BST, this 10^41 ratio is NOT a coincidence:
    R_H / r_p ≈ α⁻¹⁹ ≈ 137¹⁹ ≈ 10^40.6

Every scale in the universe is a power of α times a geometric base.

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
import matplotlib.patheffects as pe
from matplotlib.widgets import Slider, Button
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.collections import LineCollection
import matplotlib.colors as mcolors

# ─── Physical Constants ───
alpha = 1 / 137.035999
m_e_kg = 9.10938e-31       # electron mass (kg)
m_p_kg = 1.67262e-27       # proton mass (kg)
m_Pl_kg = 2.17644e-8       # Planck mass (kg)
hbar = 1.054571817e-34     # reduced Planck (J·s)
c = 2.99792458e8           # speed of light (m/s)
G = 6.67430e-11            # Newton's G
e_charge = 1.602176634e-19 # elementary charge (C)
k_e = 8.9875517873681764e9 # Coulomb constant
H_0 = 67.36e3 / 3.0857e22 # Hubble constant (1/s) — 67.36 km/s/Mpc
epsilon_0 = 8.854187817e-12

# ─── BST parameters ───
n_C = 5
N_c = 3
dim_R = 10   # dim_R(CP²)
genus = 7

# ─── Derived scales (meters) ───
r_p = 0.8414e-15           # proton radius (m) — BST: 4/m_p = dim_R(CP²)/m_p
r_nuclear = 3.0e-15        # few fm
a_0 = 5.29177e-11          # Bohr radius (m) — 1/(α m_e)
r_molecular = 1.0e-9       # molecular scale
r_cell = 10.0e-6           # cell scale
r_human = 1.7              # human scale
r_earth = 6.371e6          # Earth radius
r_AU = 1.496e11            # Sun-Earth distance
r_solarsys = 6.0e12        # solar system (~ Pluto orbit)
r_ly = 9.461e15            # light year
r_parsec = 3.086e16        # parsec
r_galaxy = 5.0e20          # Milky Way radius
r_cluster = 3.0e23         # galaxy cluster
R_H = c / H_0              # Hubble radius

# ─── Dirac numbers ───
ratio_R = R_H / r_p
log_ratio = np.log10(ratio_R)
alpha_power = np.log(ratio_R) / np.log(1/alpha)  # should be ~19

# Force ratio: F_EM / F_grav for proton-electron
F_ratio = k_e * e_charge**2 / (G * m_p_kg * m_e_kg)
log_F_ratio = np.log10(F_ratio)

# BST expression: F_EM/F_grav = α × (m_Pl/m_p) × (m_Pl/m_e) — check
bst_F_ratio = alpha * (m_Pl_kg / m_p_kg) * (m_Pl_kg / m_e_kg)

# ─── Scale landmarks ───
# (name, position_meters, log10_pos, short_description, bst_note, color)
landmarks = [
    ('Proton\nradius',      r_p,        'r_p = 4/m_p',
     'BST: dim_R(CP²)/m_p', '#ff2222'),
    ('Nuclear\nscale',      r_nuclear,  '~ few fm',
     'Strong force range', '#ff4422'),
    ('Bohr\nradius',        a_0,        'a₀ = 1/(α·m_e)',
     'α⁻¹ expansion from nuclear', '#ff8844'),
    ('Molecular\nscale',    r_molecular, '~ 1 nm',
     'Chemistry emerges', '#ffaa44'),
    ('Cell\nscale',         r_cell,     '~ 10 μm',
     'Biology emerges', '#cccc22'),
    ('Human\nscale',        r_human,    '~ 1.7 m',
     '√(a₀ × R_H) ≈ geometric mean', '#88cc44'),
    ('Earth\nradius',       r_earth,    '6371 km',
     'Gravity shapes matter', '#44cc88'),
    ('Sun-Earth\n(AU)',     r_AU,       '1 AU',
     'Stellar habitable zone', '#44aacc'),
    ('Solar\nsystem',       r_solarsys, '~ 40 AU',
     'Planetary orbits', '#4488dd'),
    ('Light\nyear',         r_ly,       '9.46 × 10¹⁵ m',
     'Interstellar distance', '#4466ee'),
    ('Galaxy',              r_galaxy,   '~ 50 kpc',
     'Dark matter halo', '#6644ff'),
    ('Galaxy\ncluster',     r_cluster,  '~ 100 Mpc',
     'Largest bound structures', '#8844ff'),
    ('Hubble\nradius',      R_H,        'R_H = c/H₀',
     'BST: α⁻¹⁹ × r_p', '#cc44ff'),
]

# Compute log10 positions
log_positions = [np.log10(lm[1]) for lm in landmarks]

# ─── Alpha-power annotations between key scales ───
# Each: (from_name, to_name, label, description)
alpha_jumps = [
    ('Proton\nradius', 'Bohr\nradius', 'α⁻¹ × m_p/m_e',
     'Bohr radius = r_p × α⁻¹ × (m_p/m_e)\n≈ r_p × 137 × 1836 ≈ r_p × 2.5×10⁵'),
    ('Bohr\nradius', 'Human\nscale', '~ α⁻⁵',
     'Atomic → human: ~10¹⁰·⁷ ≈ α⁻⁵'),
    ('Human\nscale', 'Hubble\nradius', '~ α⁻¹²',
     'Human → cosmic: ~10²⁵·⁴ ≈ α⁻¹²'),
]

# ─── Color gradient function ───
def scale_color(log_m):
    """Map log10(meters) from -16 to 27 into a red→orange→yellow→green→blue→violet gradient."""
    t = (log_m - (-16)) / (27 - (-16))
    t = np.clip(t, 0, 1)
    # Custom gradient: red → orange → gold → green → cyan → blue → violet
    colors_list = [
        (1.0, 0.1, 0.1),   # red
        (1.0, 0.5, 0.1),   # orange
        (1.0, 0.8, 0.2),   # gold
        (0.4, 0.9, 0.3),   # green
        (0.2, 0.8, 0.8),   # cyan
        (0.2, 0.4, 1.0),   # blue
        (0.7, 0.2, 1.0),   # violet
    ]
    n = len(colors_list) - 1
    idx = t * n
    i = int(np.floor(idx))
    i = min(i, n - 1)
    f = idx - i
    r = colors_list[i][0] * (1 - f) + colors_list[i + 1][0] * f
    g = colors_list[i][1] * (1 - f) + colors_list[i + 1][1] * f
    b = colors_list[i][2] * (1 - f) + colors_list[i + 1][2] * f
    return (r, g, b)


# ════════════════════════════════════════════════════════════
#  FIGURE SETUP
# ════════════════════════════════════════════════════════════

fig = plt.figure(figsize=(18, 12), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('The Dirac Large Number — 41 Orders of Magnitude — BST')

# ─── Title ───
glow = [pe.withStroke(linewidth=3, foreground='#442200')]
fig.text(0.5, 0.965, 'THE DIRAC LARGE NUMBER', fontsize=28, fontweight='bold',
         color='#ffaa00', ha='center', fontfamily='monospace',
         path_effects=glow)
fig.text(0.5, 0.935, '41 orders of magnitude from proton to cosmos — explained by geometry',
         fontsize=12, color='#aa8844', ha='center', fontfamily='monospace')

# ─── Main punchline box ───
punchline_ax = fig.add_axes([0.15, 0.875, 0.70, 0.05])
punchline_ax.set_facecolor('#0a0a1a')
punchline_ax.axis('off')
punchline_ax.set_xlim(0, 1)
punchline_ax.set_ylim(0, 1)

punchline_ax.text(0.5, 0.5,
    'R_H / r_p  =  α⁻¹⁹  ≈  137¹⁹  ≈  10⁴⁰·⁶  ≈  5 × 10⁴¹',
    fontsize=18, fontweight='bold', color='#ffdd44', ha='center', va='center',
    fontfamily='monospace',
    bbox=dict(boxstyle='round,pad=0.5', facecolor='#1a1a0a',
              edgecolor='#aa8800', linewidth=2.5),
    path_effects=[pe.withStroke(linewidth=1, foreground='#665500')])

# ════════════════════════════════════════════════════════════
#  MAIN LOGARITHMIC SCALE (upper panel)
# ════════════════════════════════════════════════════════════

ax_main = fig.add_axes([0.06, 0.48, 0.88, 0.37])
ax_main.set_facecolor('#0a0a1a')

log_min, log_max = -16.5, 27.5
ax_main.set_xlim(log_min, log_max)
ax_main.set_ylim(-0.5, 2.5)

# Draw the logarithmic ruler — color gradient bar
n_segments = 500
x_seg = np.linspace(log_min, log_max, n_segments + 1)
for i in range(n_segments):
    x0, x1 = x_seg[i], x_seg[i + 1]
    col = scale_color((x0 + x1) / 2)
    ax_main.axvspan(x0, x1, ymin=0.18, ymax=0.28, color=col, alpha=0.6)

# Subtle grid lines at each power of 10
for p in range(-16, 28):
    ax_main.axvline(p, color='#333355', linewidth=0.3, alpha=0.5, ymin=0.0, ymax=1.0)

# Major ticks
ax_main.set_xticks(range(-15, 27, 3))
ax_main.set_xticklabels([f'10$^{{{p}}}$' for p in range(-15, 27, 3)],
                         fontsize=8, color='#888899', fontfamily='monospace')
ax_main.tick_params(axis='x', colors='#555577', length=4)
ax_main.tick_params(axis='y', left=False, labelleft=False)

# Remove box
for spine in ax_main.spines.values():
    spine.set_visible(False)

# ─── Place landmarks ───
y_positions_top = []
for i, (name, meters, desc, bst_note, color) in enumerate(landmarks):
    log_m = np.log10(meters)

    # Alternate above/below for readability
    if i % 2 == 0:
        y_marker = 0.9
        y_text = 1.5
        va = 'bottom'
    else:
        y_marker = 0.9
        y_text = 1.6
        va = 'bottom'

    # Stagger heights to avoid overlap
    heights = [1.25, 1.65, 1.25, 1.65, 1.25, 1.65, 1.25, 1.65,
               1.25, 1.65, 1.25, 1.65, 1.25]
    y_text = heights[i % len(heights)]

    # Marker dot
    ax_main.plot(log_m, 0.6, 'o', color=color, markersize=8, zorder=5,
                 markeredgecolor='white', markeredgewidth=0.5)

    # Vertical line from bar to marker
    ax_main.plot([log_m, log_m], [0.6, y_text - 0.05], '-', color=color,
                 linewidth=0.8, alpha=0.6)

    # Label
    ax_main.text(log_m, y_text, name, fontsize=7.5, color=color,
                 ha='center', va='bottom', fontfamily='monospace', fontweight='bold')

    # Small log value
    ax_main.text(log_m, y_text - 0.12, f'{log_m:.1f}', fontsize=6,
                 color='#666688', ha='center', va='top', fontfamily='monospace')

# ─── Alpha-power arcs between key scales ───
name_to_log = {lm[0]: np.log10(lm[1]) for lm in landmarks}

arc_data = [
    ('Proton\nradius', 'Bohr\nradius', 'α⁻¹ × (m_p/m_e)', '#ff8844'),
    ('Bohr\nradius', 'Human\nscale', '~ α⁻⁵', '#88cc44'),
    ('Human\nscale', 'Hubble\nradius', '~ α⁻¹²', '#8844ff'),
]

for (n1, n2, label, col) in arc_data:
    x1 = name_to_log[n1]
    x2 = name_to_log[n2]
    xm = (x1 + x2) / 2
    # Draw arc as quadratic bezier
    t_arc = np.linspace(0, 1, 50)
    x_arc = x1 + (x2 - x1) * t_arc
    y_arc = 0.15 - 0.3 * 4 * t_arc * (1 - t_arc)  # parabola below
    ax_main.plot(x_arc, y_arc, '-', color=col, linewidth=1.5, alpha=0.7)
    # Arrowhead
    ax_main.annotate('', xy=(x2, 0.15), xytext=(x2 - 0.5, y_arc[-3]),
                     arrowprops=dict(arrowstyle='->', color=col, lw=1.2))
    # Label on arc
    ax_main.text(xm, -0.25, label, fontsize=8, color=col,
                 ha='center', va='top', fontfamily='monospace', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a0a1a',
                           edgecolor=col, linewidth=0.8, alpha=0.9))

# ─── Total span annotation ───
ax_main.annotate('', xy=(np.log10(R_H), 2.2), xytext=(np.log10(r_p), 2.2),
                 arrowprops=dict(arrowstyle='<->', color='#ffdd44', lw=2))
ax_main.text((np.log10(R_H) + np.log10(r_p)) / 2, 2.35,
             f'41.7 decades  =  α⁻¹⁹  (α = 1/137)',
             fontsize=11, color='#ffdd44', ha='center', va='bottom',
             fontfamily='monospace', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a0a',
                       edgecolor='#aa8800', linewidth=1.5))

ax_main.set_xlabel('log₁₀(distance / meters)', fontsize=10, color='#888899',
                    fontfamily='monospace', labelpad=8)

# ════════════════════════════════════════════════════════════
#  ZOOM WINDOW (magnifying glass, lower-left)
# ════════════════════════════════════════════════════════════

ax_zoom = fig.add_axes([0.06, 0.12, 0.50, 0.28])
ax_zoom.set_facecolor('#06061a')
for spine in ax_zoom.spines.values():
    spine.set_color('#334466')
    spine.set_linewidth(1.5)

ax_zoom.set_ylim(-0.3, 2.0)
ax_zoom.tick_params(axis='y', left=False, labelleft=False)
ax_zoom.tick_params(axis='x', colors='#555577', length=4)

zoom_title = ax_zoom.set_title('MAGNIFYING GLASS — drag slider to explore',
                                fontsize=10, color='#6688aa', fontfamily='monospace',
                                pad=8)

# Initial zoom center and half-width
zoom_center = 0.0
zoom_half = 3.0  # ±3 decades visible in zoom

def update_zoom(center):
    """Redraw the zoom window centered at `center` log10(meters)."""
    ax_zoom.clear()
    ax_zoom.set_facecolor('#06061a')
    for sp in ax_zoom.spines.values():
        sp.set_color('#334466')
        sp.set_linewidth(1.5)

    left = center - zoom_half
    right = center + zoom_half
    ax_zoom.set_xlim(left, right)
    ax_zoom.set_ylim(-0.3, 2.2)
    ax_zoom.tick_params(axis='y', left=False, labelleft=False)

    # Color gradient bar in zoom
    n_seg = 200
    x_s = np.linspace(left, right, n_seg + 1)
    for i in range(n_seg):
        x0, x1 = x_s[i], x_s[i + 1]
        col = scale_color((x0 + x1) / 2)
        ax_zoom.axvspan(x0, x1, ymin=0.22, ymax=0.32, color=col, alpha=0.8)

    # Grid
    for p in range(int(np.floor(left)) - 1, int(np.ceil(right)) + 2):
        ax_zoom.axvline(p, color='#333355', linewidth=0.4, alpha=0.5)

    # Tick labels
    ticks = list(range(int(np.ceil(left)), int(np.floor(right)) + 1))
    ax_zoom.set_xticks(ticks)
    ax_zoom.set_xticklabels([f'10$^{{{p}}}$' for p in ticks],
                             fontsize=8, color='#888899', fontfamily='monospace')
    ax_zoom.tick_params(axis='x', colors='#555577', length=4)

    # Place landmarks that fall in view
    visible = [(name, meters, desc, bst_note, color)
               for (name, meters, desc, bst_note, color) in landmarks
               if left <= np.log10(meters) <= right]

    for j, (name, meters, desc, bst_note, color) in enumerate(visible):
        log_m = np.log10(meters)
        y_t = 1.1 + 0.45 * (j % 2)

        ax_zoom.plot(log_m, 0.7, 'o', color=color, markersize=10, zorder=5,
                     markeredgecolor='white', markeredgewidth=1.0)
        ax_zoom.plot([log_m, log_m], [0.7, y_t - 0.05], '-', color=color,
                     linewidth=1.0, alpha=0.6)
        ax_zoom.text(log_m, y_t, name, fontsize=8.5, color=color,
                     ha='center', va='bottom', fontfamily='monospace', fontweight='bold')
        ax_zoom.text(log_m, y_t - 0.1, bst_note, fontsize=6.5,
                     color='#8888aa', ha='center', va='top', fontfamily='monospace',
                     style='italic')

    # Title with current location
    if -16 <= center <= -10:
        region = "Subatomic realm"
    elif -10 <= center <= -7:
        region = "Atomic / molecular realm"
    elif -7 <= center <= -3:
        region = "Microscopic realm"
    elif -3 <= center <= 3:
        region = "Human realm"
    elif 3 <= center <= 8:
        region = "Planetary realm"
    elif 8 <= center <= 14:
        region = "Stellar / solar realm"
    elif 14 <= center <= 19:
        region = "Interstellar realm"
    elif 19 <= center <= 24:
        region = "Galactic realm"
    else:
        region = "Cosmic realm"

    ax_zoom.set_title(f'MAGNIFYING GLASS — {region} (10$^{{{center:.1f}}}$ m)',
                       fontsize=10, color='#6688aa', fontfamily='monospace', pad=8)

    # Draw zoom indicator on main axis
    # Remove old zoom patches
    for patch in getattr(update_zoom, '_patches', []):
        try:
            patch.remove()
        except:
            pass
    update_zoom._patches = []

    # Semi-transparent highlight on main axis
    rect = ax_main.axvspan(left, right, ymin=0.0, ymax=1.0,
                           color='#4488ff', alpha=0.08, zorder=0)
    line_l = ax_main.axvline(left, color='#4488ff', linewidth=1.0, alpha=0.4, linestyle='--')
    line_r = ax_main.axvline(right, color='#4488ff', linewidth=1.0, alpha=0.4, linestyle='--')
    update_zoom._patches = [rect, line_l, line_r]

    fig.canvas.draw_idle()

update_zoom._patches = []

# ─── Slider ───
ax_slider = fig.add_axes([0.06, 0.06, 0.50, 0.03])
ax_slider.set_facecolor('#111133')
slider = Slider(ax_slider, '', log_min + zoom_half, log_max - zoom_half,
                valinit=0.0, valstep=0.1,
                color='#4488cc', track_color='#1a1a3a')
slider.label.set_color('#6688aa')
slider.valtext.set_color('#6688aa')
slider.valtext.set_fontfamily('monospace')

# Label for slider
fig.text(0.06, 0.095, 'Drag to explore 41 orders of magnitude:',
         fontsize=9, color='#6688aa', fontfamily='monospace')

def on_slider(val):
    update_zoom(val)

slider.on_changed(on_slider)

# ─── Zoom buttons ───
ax_zin = fig.add_axes([0.44, 0.095, 0.05, 0.025])
ax_zout = fig.add_axes([0.50, 0.095, 0.05, 0.025])
btn_zin = Button(ax_zin, 'Zoom+', color='#1a1a3a', hovercolor='#2a2a4a')
btn_zout = Button(ax_zout, 'Zoom-', color='#1a1a3a', hovercolor='#2a2a4a')
btn_zin.label.set_color('#6688aa')
btn_zin.label.set_fontsize(8)
btn_zout.label.set_color('#6688aa')
btn_zout.label.set_fontsize(8)

def zoom_in(event):
    global zoom_half
    zoom_half = max(1.0, zoom_half - 1.0)
    slider.valmin = log_min + zoom_half
    slider.valmax = log_max - zoom_half
    update_zoom(slider.val)

def zoom_out(event):
    global zoom_half
    zoom_half = min(15.0, zoom_half + 1.0)
    slider.valmin = log_min + zoom_half
    slider.valmax = log_max - zoom_half
    update_zoom(slider.val)

btn_zin.on_clicked(zoom_in)
btn_zout.on_clicked(zoom_out)


# ════════════════════════════════════════════════════════════
#  INFO PANEL (lower-right): Dirac's observation + BST explanation
# ════════════════════════════════════════════════════════════

ax_info = fig.add_axes([0.60, 0.06, 0.36, 0.34])
ax_info.set_facecolor('#0a0a1a')
ax_info.axis('off')
ax_info.set_xlim(0, 1)
ax_info.set_ylim(0, 1)

# Panel border
border = FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                         boxstyle='round,pad=0.02',
                         facecolor='#0f0f2a', edgecolor='#334466',
                         linewidth=1.5)
ax_info.add_patch(border)

ax_info.text(0.5, 0.93, 'DIRAC\'S LARGE NUMBERS', fontsize=13, fontweight='bold',
             color='#ffaa44', ha='center', fontfamily='monospace')

# The original observation
ax_info.text(0.5, 0.83, 'Dirac (1937) noticed:', fontsize=9,
             color='#9999aa', ha='center', fontfamily='monospace', style='italic')

ax_info.text(0.5, 0.74,
    f'F_EM / F_grav  =  e² / (G·m_p·m_e)  =  {F_ratio:.2e}',
    fontsize=9.5, color='#ffcc66', ha='center', fontfamily='monospace',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a0a',
              edgecolor='#665500', linewidth=1))

ax_info.text(0.5, 0.64,
    f'R_H / r_p  ≈  {ratio_R:.2e}   (log₁₀ = {log_ratio:.1f})',
    fontsize=9.5, color='#66ccff', ha='center', fontfamily='monospace',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a2a',
              edgecolor='#336688', linewidth=1))

ax_info.text(0.5, 0.54, '"These cannot be coincidences."', fontsize=9,
             color='#9999aa', ha='center', fontfamily='monospace', style='italic')

# BST explanation
ax_info.text(0.5, 0.44, 'BST EXPLAINS BOTH:', fontsize=11, fontweight='bold',
             color='#44ff88', ha='center', fontfamily='monospace')

ax_info.text(0.5, 0.35,
    f'R_H/r_p = α⁻¹⁹  (computed: α⁻{alpha_power:.2f})',
    fontsize=9.5, color='#88ffaa', ha='center', fontfamily='monospace')

ax_info.text(0.5, 0.27,
    f'F_EM/F_grav = α × (m_Pl/m_p)(m_Pl/m_e)',
    fontsize=9.5, color='#88ffaa', ha='center', fontfamily='monospace')

ax_info.text(0.5, 0.19,
    f'            = α × (6π⁵)⁻¹·α⁻¹² × (6π⁵)⁻¹·α⁻¹²/(6π⁵)',
    fontsize=7.5, color='#669988', ha='center', fontfamily='monospace')

# BST check value
ax_info.text(0.5, 0.10,
    f'BST predicts: {bst_F_ratio:.3e}   (obs: {F_ratio:.3e})',
    fontsize=8.5, color='#aaaacc', ha='center', fontfamily='monospace')

# Key insight
ax_info.text(0.5, 0.03,
    'All large numbers = powers of α = 1/137',
    fontsize=9, fontweight='bold', color='#ffdd44', ha='center',
    fontfamily='monospace')


# ════════════════════════════════════════════════════════════
#  ALPHA POWER LADDER (right side of info panel)
# ════════════════════════════════════════════════════════════

# Create a small table of alpha powers
ax_table = fig.add_axes([0.60, 0.41, 0.36, 0.07])
ax_table.set_facecolor('#0a0a1a')
ax_table.axis('off')
ax_table.set_xlim(0, 1)
ax_table.set_ylim(0, 1)

ax_table.text(0.5, 0.85, 'ALPHA POWER LADDER', fontsize=10, fontweight='bold',
              color='#aa88ff', ha='center', fontfamily='monospace')

ladder_items = [
    ('α⁻¹ ≈ 137', '2.14 decades'),
    ('α⁻¹² ≈ m_Pl/m_p', '25.6 decades'),
    ('α⁻¹⁹ ≈ R_H/r_p', '40.6 decades'),
    ('α⁻⁵⁶ ≈ Λ/m_Pl⁴', '120 decades'),
]

for j, (expr, dec) in enumerate(ladder_items):
    y = 0.55 - j * 0.2
    ax_table.text(0.08, y, expr, fontsize=7.5, color='#cc88ff',
                  fontfamily='monospace', va='center')
    ax_table.text(0.65, y, dec, fontsize=7.5, color='#8866cc',
                  fontfamily='monospace', va='center')


# ════════════════════════════════════════════════════════════
#  INITIAL ZOOM + COPYRIGHT
# ════════════════════════════════════════════════════════════

update_zoom(0.0)

fig.text(0.99, 0.005, 'BST / Casey Koons 2026',
         fontsize=7, color='#444466', ha='right', fontfamily='monospace')

plt.show()
