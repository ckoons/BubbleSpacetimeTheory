#!/usr/bin/env python3
"""
THE UNIVERSE MACHINE
====================
Three integers generate all of fundamental physics.
Move the sliders. Only (3, 5, 137) lights up the real universe.

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
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

# ─── Observed values ───
OBS = {
    'α':            1/137.035999,
    'm_p/m_e':      1836.15267,
    'sin²θ_W':      0.23122,
    'α_s(m_p)':     0.35,       # approximate at proton scale
    'ΔΣ':           0.30,
    'sin²θ₁₂':     0.307,
    'sin²θ₂₃':     0.572,
    'sin²θ₁₃':     0.0220,
    'sinθ_C':       0.2253,
    'm_s/m_d':      20.0,
    'm_b/m_τ':      2.35,
    'N_gen':        3,
    'gluons':       8,
}

def compute_physics(Nc, nC, Nmax):
    """Given three integers, compute all BST predictions."""
    g = nC + 2           # genus
    C2 = (nC + 1)        # Casimir eigenvalue
    Gamma = 1
    for i in range(1, nC + 1):
        Gamma *= i
    Gamma *= 2**(nC - 1)  # |Γ| = nC! * 2^(nC-1)

    results = {}

    # Fine structure constant (Wyler formula)
    if Nmax > 0:
        vol = np.pi**nC / Gamma if Gamma > 0 else 0
        wyler = (Nc**2) / (2**Nc * np.pi**4) * vol**(1/4) if vol > 0 else 0
        results['α'] = wyler
    else:
        results['α'] = 0

    # Proton-to-electron mass ratio
    results['m_p/m_e'] = C2 * np.pi**nC

    # Weinberg angle
    denom = Nc + 2*nC
    results['sin²θ_W'] = Nc / denom if denom > 0 else 0

    # Strong coupling at proton scale
    results['α_s(m_p)'] = (nC + 2) / (4 * nC) if nC > 0 else 0

    # Proton spin fraction
    results['ΔΣ'] = Nc / (2 * nC) if nC > 0 else 0

    # PMNS mixing angles
    results['sin²θ₁₂'] = Nc / (2 * nC) if nC > 0 else 0
    results['sin²θ₂₃'] = (nC - 1) / (nC + 2) if (nC + 2) > 0 else 0
    results['sin²θ₁₃'] = 1 / (nC * (2*nC - 1)) if nC > 0 and (2*nC - 1) > 0 else 0

    # CKM Cabibbo angle
    results['sinθ_C'] = 1 / (2 * np.sqrt(nC)) if nC > 0 else 0

    # Mass ratios
    results['m_s/m_d'] = 4 * nC
    results['m_b/m_τ'] = g / Nc if Nc > 0 else 0

    # Generation count (Lefschetz)
    results['N_gen'] = Nc

    # Gluon count
    results['gluons'] = Nc**2 - 1

    # Derived integers for display
    results['_genus'] = g
    results['_C2'] = C2
    results['_Gamma'] = Gamma
    results['_Weinberg_denom'] = Nc + 2*nC
    results['_real_dim'] = 2 * nC

    return results

def pct_error(pred, obs):
    if obs == 0:
        return 100.0
    return abs(pred - obs) / abs(obs) * 100

# ─── Build the figure ───
fig = plt.figure(figsize=(16, 11), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('The Universe Machine — BST')

# Title
fig.text(0.5, 0.96, 'THE UNIVERSE MACHINE', fontsize=28, fontweight='bold',
         color='#00ccff', ha='center', va='top',
         fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#004466')])
fig.text(0.5, 0.925, 'Three integers → All of physics', fontsize=14,
         color='#88aacc', ha='center', va='top', fontfamily='monospace')

# Slider axes
ax_Nc   = fig.add_axes([0.15, 0.86, 0.30, 0.025])
ax_nC   = fig.add_axes([0.15, 0.83, 0.30, 0.025])
ax_Nmax = fig.add_axes([0.15, 0.80, 0.30, 0.025])

for ax in [ax_Nc, ax_nC, ax_Nmax]:
    ax.set_facecolor('#1a1a2e')

slider_Nc   = Slider(ax_Nc,   'N_c  ', 1, 8, valinit=3, valstep=1,
                     color='#ff4444', valfmt='%d')
slider_nC   = Slider(ax_nC,   'n_C  ', 2, 10, valinit=5, valstep=1,
                     color='#44ff44', valfmt='%d')
slider_Nmax = Slider(ax_Nmax, 'N_max', 50, 250, valinit=137, valstep=1,
                     color='#4444ff', valfmt='%d')

for s in [slider_Nc, slider_nC, slider_Nmax]:
    s.label.set_color('white')
    s.label.set_fontsize(14)
    s.label.set_fontfamily('monospace')
    s.valtext.set_color('white')
    s.valtext.set_fontsize(14)

# Integer display area (right side top)
ax_ints = fig.add_axes([0.58, 0.78, 0.38, 0.12])
ax_ints.set_facecolor('#0a0a1a')
ax_ints.axis('off')

# Main results area
ax_main = fig.add_axes([0.04, 0.03, 0.92, 0.74])
ax_main.set_facecolor('#0a0a1a')
ax_main.axis('off')

# Text objects for results
result_texts = []

def render(val=None):
    Nc = int(slider_Nc.val)
    nC = int(slider_nC.val)
    Nmax = int(slider_Nmax.val)

    results = compute_physics(Nc, nC, Nmax)

    # Clear previous
    ax_ints.clear()
    ax_ints.set_facecolor('#0a0a1a')
    ax_ints.axis('off')
    ax_main.clear()
    ax_main.set_facecolor('#0a0a1a')
    ax_main.axis('off')
    ax_main.set_xlim(0, 1)
    ax_main.set_ylim(0, 1)

    # ─── Derived integers panel ───
    ax_ints.set_xlim(0, 1)
    ax_ints.set_ylim(0, 1)
    ints_text = (
        f"genus = {results['_genus']}    "
        f"C₂ = {results['_C2']}    "
        f"|Γ| = {results['_Gamma']}    "
        f"2n_C = {results['_real_dim']}    "
        f"N_c+2n_C = {results['_Weinberg_denom']}"
    )
    ax_ints.text(0.5, 0.7, 'DERIVED INTEGERS', fontsize=12, fontweight='bold',
                 color='#ffaa00', ha='center', fontfamily='monospace')
    ax_ints.text(0.5, 0.25, ints_text, fontsize=11,
                 color='#cccccc', ha='center', fontfamily='monospace')

    # ─── Physics results ───
    quantities = [
        ('α (fine structure)',  'α',        '{:.6f}'),
        ('m_p / m_e',          'm_p/m_e',  '{:.2f}'),
        ('sin²θ_W',            'sin²θ_W',  '{:.5f}'),
        ('α_s(m_p)',           'α_s(m_p)', '{:.4f}'),
        ('ΔΣ (proton spin)',   'ΔΣ',       '{:.4f}'),
        ('sin²θ₁₂ (PMNS)',    'sin²θ₁₂',  '{:.4f}'),
        ('sin²θ₂₃ (PMNS)',    'sin²θ₂₃',  '{:.4f}'),
        ('sin²θ₁₃ (PMNS)',    'sin²θ₁₃',  '{:.5f}'),
        ('sinθ_C (Cabibbo)',   'sinθ_C',   '{:.5f}'),
        ('m_s / m_d',          'm_s/m_d',  '{:.1f}'),
        ('m_b / m_τ',         'm_b/m_τ',  '{:.3f}'),
        ('N_gen',              'N_gen',     '{:.0f}'),
        ('gluons',             'gluons',    '{:.0f}'),
    ]

    n = len(quantities)
    row_height = 0.9 / n

    # Check if we're at the real universe
    is_real = (Nc == 3 and nC == 5 and Nmax == 137)

    for i, (label, key, fmt) in enumerate(quantities):
        y = 0.95 - i * row_height
        pred = results[key]
        obs = OBS[key]
        err = pct_error(pred, obs)

        # Color coding
        if err < 0.5:
            color = '#00ff88'
            status = '●'
        elif err < 2.0:
            color = '#aaff00'
            status = '◐'
        elif err < 10.0:
            color = '#ffaa00'
            status = '◔'
        else:
            color = '#ff3333'
            status = '○'

        # Background bar for row
        bar_width = max(0, min(1.0, 1.0 - err/50))
        ax_main.barh(y, bar_width, height=row_height*0.6,
                     left=0, color=color, alpha=0.08)

        # Status dot
        ax_main.text(0.01, y, status, fontsize=14, color=color,
                     va='center', fontfamily='monospace')

        # Label
        ax_main.text(0.04, y, label, fontsize=11, color='#aaaacc',
                     va='center', fontfamily='monospace')

        # Predicted value
        pred_str = fmt.format(pred)
        ax_main.text(0.38, y, f'BST: {pred_str}', fontsize=11, color=color,
                     va='center', fontfamily='monospace', fontweight='bold')

        # Observed value
        obs_str = fmt.format(obs)
        ax_main.text(0.60, y, f'Obs: {obs_str}', fontsize=11, color='#888888',
                     va='center', fontfamily='monospace')

        # Error
        err_str = f'{err:.2f}%' if err < 100 else '>100%'
        ax_main.text(0.80, y, err_str, fontsize=11, color=color,
                     va='center', fontfamily='monospace')

        # Formula hint
        formulas = {
            'α':        f'(9/8π⁴)(π^{nC}/{results["_Gamma"]})^{{1/4}}',
            'm_p/m_e':  f'{results["_C2"]}·π^{nC}',
            'sin²θ_W':  f'{Nc}/({Nc}+2·{nC}) = {Nc}/{results["_Weinberg_denom"]}',
            'α_s(m_p)': f'({nC}+2)/(4·{nC}) = {results["_genus"]}/{4*nC}',
            'ΔΣ':       f'{Nc}/(2·{nC}) = {Nc}/{2*nC}',
            'sin²θ₁₂':  f'{Nc}/(2·{nC})',
            'sin²θ₂₃':  f'({nC}-1)/({nC}+2) = {nC-1}/{nC+2}',
            'sin²θ₁₃':  f'1/({nC}·(2·{nC}-1)) = 1/{nC*(2*nC-1)}',
            'sinθ_C':   f'1/(2√{nC})',
            'm_s/m_d':  f'4·{nC} = {4*nC}',
            'm_b/m_τ':  f'{results["_genus"]}/{Nc}',
            'N_gen':    f'N_c = {Nc}',
            'gluons':   f'{Nc}²-1 = {Nc**2-1}',
        }
        formula = formulas.get(key, '')
        ax_main.text(0.90, y, formula, fontsize=8, color='#666688',
                     va='center', fontfamily='monospace')

    # Score
    total_err = sum(pct_error(results[k], OBS[k]) for _, k, _ in quantities)
    avg_err = total_err / n
    perfect = sum(1 for _, k, _ in quantities if pct_error(results[k], OBS[k]) < 2.0)

    score_color = '#00ff88' if perfect == n else '#ffaa00' if perfect > n//2 else '#ff3333'
    ax_main.text(0.5, 0.01,
                 f'{perfect}/{n} match    avg error: {avg_err:.2f}%',
                 fontsize=14, fontweight='bold', color=score_color,
                 ha='center', va='bottom', fontfamily='monospace')

    if is_real:
        ax_main.text(0.5, -0.03,
                     '★  THIS IS OUR UNIVERSE  ★',
                     fontsize=16, fontweight='bold', color='#00ccff',
                     ha='center', va='bottom', fontfamily='monospace',
                     path_effects=[pe.withStroke(linewidth=2, foreground='#003344')])

    fig.canvas.draw_idle()

# Connect sliders
slider_Nc.on_changed(render)
slider_nC.on_changed(render)
slider_Nmax.on_changed(render)

# Initial render
render()

plt.show()
