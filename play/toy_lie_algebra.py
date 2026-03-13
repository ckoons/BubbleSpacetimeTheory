#!/usr/bin/env python3
"""
THE SYMMETRIC SPACE PLAYGROUND
==============================
Interactive exploration of the Lie algebra so(5,2):
  - Build the 21 generators as 7x7 matrices
  - Compute commutators interactively
  - Watch the symmetric space conditions verified visually:
    [k,k] ⊂ k  [k,m] ⊂ m  [m,m] ⊂ k
  - See the complex structure J rotate m-space

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
from matplotlib.widgets import Button, RadioButtons
from matplotlib.colors import Normalize
from matplotlib.cm import RdBu
import matplotlib.patheffects as pe

# ─── Build so(5,2) ───
eta = np.diag([1., 1., 1., 1., 1., -1., -1.])

def in_lie_algebra(X, tol=1e-10):
    return np.max(np.abs(X.T @ eta + eta @ X)) < tol

def commutator(X, Y):
    return X @ Y - Y @ X

def in_span(X, basis, tol=1e-10):
    if len(basis) == 0:
        return np.max(np.abs(X)) < tol
    B = np.column_stack([b.flatten() for b in basis])
    res = np.linalg.lstsq(B, X.flatten(), rcond=None)
    recon = B @ res[0]
    return np.max(np.abs(recon - X.flatten())) < tol

# k basis: so(5) generators + J
k_basis = []
k_labels = []
for i in range(5):
    for j in range(i+1, 5):
        A = np.zeros((5, 5))
        A[i, j] = 1
        A[j, i] = -1
        X = np.zeros((7, 7))
        X[:5, :5] = A
        k_basis.append(X)
        k_labels.append(f'K_{i}{j}')

D = np.zeros((2, 2))
D[0, 1] = 1
D[1, 0] = -1
J = np.zeros((7, 7))
J[5:, 5:] = D
k_basis.append(J)
k_labels.append('J')

# m basis
m_basis = []
m_labels = []
for i in range(5):
    for col in range(2):
        X = np.zeros((7, 7))
        X[i, 5 + col] = 1
        X[5 + col, i] = 1
        m_basis.append(X)
        m_labels.append(f'M_{i},{col}')

all_basis = k_basis + m_basis
all_labels = k_labels + m_labels

# ─── Figure ───
fig = plt.figure(figsize=(18, 11), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('The Symmetric Space Playground — so(5,2)')

fig.text(0.5, 0.97, 'THE SYMMETRIC SPACE PLAYGROUND', fontsize=22,
         fontweight='bold', color='#44aaff', ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=2, foreground='#002244')])
fig.text(0.5, 0.94, 'so(5,2) = k ⊕ m    where k = so(5) ⊕ so(2), dim m = 10',
         fontsize=12, color='#88aacc', ha='center', fontfamily='monospace')

# ─── Panel 1: Matrix heatmap of selected generator ───
ax_mat1 = fig.add_axes([0.04, 0.48, 0.20, 0.38])
ax_mat2 = fig.add_axes([0.28, 0.48, 0.20, 0.38])
ax_comm = fig.add_axes([0.52, 0.48, 0.20, 0.38])
ax_info = fig.add_axes([0.76, 0.48, 0.22, 0.38])

for ax in [ax_mat1, ax_mat2, ax_comm, ax_info]:
    ax.set_facecolor('#0a0a1a')

# ─── Panel 2: The 21×21 commutator structure ───
ax_struct = fig.add_axes([0.04, 0.03, 0.44, 0.40])
ax_struct.set_facecolor('#0a0a1a')

# ─── Panel 3: Complex structure J ───
ax_J = fig.add_axes([0.54, 0.03, 0.42, 0.40])
ax_J.set_facecolor('#0a0a1a')

# State
state = {'idx1': 0, 'idx2': 1}

def draw_matrix(ax, M, title, color):
    ax.clear()
    ax.set_facecolor('#0a0a1a')
    norm = Normalize(vmin=-1.5, vmax=1.5)
    ax.imshow(M, cmap='RdBu', norm=norm, aspect='equal')
    ax.set_title(title, color=color, fontsize=12, fontfamily='monospace', pad=8)
    for i in range(7):
        for j in range(7):
            val = M[i, j]
            if abs(val) > 0.01:
                txt_color = 'white' if abs(val) > 0.8 else '#aaaaaa'
                ax.text(j, i, f'{val:.1f}', ha='center', va='center',
                        fontsize=8, color=txt_color, fontfamily='monospace')
    ax.set_xticks(range(7))
    ax.set_yticks(range(7))
    ax.tick_params(colors='#666688', labelsize=7)

def draw_commutator_structure():
    """Draw the 21×21 grid showing [X_i, X_j] lands in k (blue) or m (red)."""
    ax_struct.clear()
    ax_struct.set_facecolor('#0a0a1a')

    n = len(all_basis)
    grid = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            C = commutator(all_basis[i], all_basis[j])
            if np.max(np.abs(C)) < 1e-10:
                grid[i, j] = 0      # zero
            elif in_span(C, k_basis):
                grid[i, j] = 1      # in k
            elif in_span(C, m_basis):
                grid[i, j] = -1     # in m
            else:
                grid[i, j] = 0.5    # error

    # Custom colormap: blue = k, red = m, black = zero
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['#ff4488', '#111122', '#0a0a1a', '#4488ff', '#ffaa00'])
    bounds = [-1.5, -0.5, -0.1, 0.1, 0.5, 1.5]
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)

    ax_struct.imshow(grid, cmap=cmap, norm=norm, aspect='equal')

    # Sector lines
    nk = len(k_basis)
    ax_struct.axhline(nk - 0.5, color='#ffffff', linewidth=1.5, alpha=0.5)
    ax_struct.axvline(nk - 0.5, color='#ffffff', linewidth=1.5, alpha=0.5)

    # Labels
    ax_struct.text(nk/2, -1.5, 'k (11)', fontsize=10, color='#4488ff',
                   ha='center', fontfamily='monospace')
    ax_struct.text(nk + 5, -1.5, 'm (10)', fontsize=10, color='#ff4488',
                   ha='center', fontfamily='monospace')
    ax_struct.text(-2.5, nk/2, 'k', fontsize=10, color='#4488ff',
                   ha='center', va='center', fontfamily='monospace', rotation=90)
    ax_struct.text(-2.5, nk + 5, 'm', fontsize=10, color='#ff4488',
                   ha='center', va='center', fontfamily='monospace', rotation=90)

    # Quadrant labels
    ax_struct.text(nk/2, nk/2, '[k,k]⊂k', fontsize=9, color='white',
                   ha='center', va='center', fontfamily='monospace', alpha=0.7,
                   bbox=dict(boxstyle='round', facecolor='#4488ff', alpha=0.3))
    ax_struct.text(nk + 5, nk/2, '[m,k]⊂m', fontsize=9, color='white',
                   ha='center', va='center', fontfamily='monospace', alpha=0.7,
                   bbox=dict(boxstyle='round', facecolor='#ff4488', alpha=0.3))
    ax_struct.text(nk/2, nk + 5, '[k,m]⊂m', fontsize=9, color='white',
                   ha='center', va='center', fontfamily='monospace', alpha=0.7,
                   bbox=dict(boxstyle='round', facecolor='#ff4488', alpha=0.3))
    ax_struct.text(nk + 5, nk + 5, '[m,m]⊂k', fontsize=9, color='white',
                   ha='center', va='center', fontfamily='monospace', alpha=0.7,
                   bbox=dict(boxstyle='round', facecolor='#4488ff', alpha=0.3))

    ax_struct.set_title('COMMUTATOR STRUCTURE:  blue = ∈k   pink = ∈m   dark = 0',
                        fontsize=10, color='#cccccc', fontfamily='monospace', pad=10)
    ax_struct.tick_params(colors='#444444', labelsize=5)

def draw_complex_structure():
    """Show J rotating each (M_i0, M_i1) pair."""
    ax_J.clear()
    ax_J.set_facecolor('#0a0a1a')
    ax_J.set_aspect('equal')
    ax_J.set_xlim(-3, 3)
    ax_J.set_ylim(-3, 3)

    ax_J.set_title('COMPLEX STRUCTURE: J acts as -i on m ≅ C⁵',
                    fontsize=10, color='#cccccc', fontfamily='monospace', pad=10)

    # Draw 5 unit circles for the 5 complex dimensions
    theta = np.linspace(0, 2*np.pi, 100)
    colors_5 = ['#ff4444', '#44ff44', '#4488ff', '#ffaa44', '#ff44ff']
    labels_5 = ['dim 0', 'dim 1', 'dim 2', 'dim 3', 'dim 4']

    for k in range(5):
        # Position in a ring
        cx = 2.0 * np.cos(2 * np.pi * k / 5 - np.pi/2)
        cy = 2.0 * np.sin(2 * np.pi * k / 5 - np.pi/2)
        r = 0.5

        # Circle
        ax_J.plot(cx + r*np.cos(theta), cy + r*np.sin(theta),
                  color=colors_5[k], linewidth=1.5, alpha=0.5)

        # Re and Im points
        re_x, re_y = cx + r, cy
        im_x, im_y = cx, cy + r

        ax_J.plot(re_x, re_y, 'o', color=colors_5[k], markersize=8)
        ax_J.plot(im_x, im_y, 's', color=colors_5[k], markersize=8, alpha=0.6)

        # Arrow from Re to Im (J action)
        ax_J.annotate('', xy=(im_x, im_y), xytext=(re_x, re_y),
                      arrowprops=dict(arrowstyle='->', color=colors_5[k],
                                      lw=1.5, connectionstyle='arc3,rad=0.3'))

        # Labels
        ax_J.text(cx, cy - r - 0.15, labels_5[k], fontsize=8,
                  color=colors_5[k], ha='center', fontfamily='monospace')
        ax_J.text(re_x + 0.12, re_y, 'Re', fontsize=6, color=colors_5[k],
                  fontfamily='monospace')
        ax_J.text(im_x, im_y + 0.12, 'Im', fontsize=6, color=colors_5[k],
                  fontfamily='monospace')

    # Verify numerically
    J_mat = k_basis[-1]
    checks = []
    for i in range(5):
        Xre = m_basis[2*i]
        Xim = m_basis[2*i + 1]
        check_re = np.max(np.abs(commutator(J_mat, Xre) - (-Xim)))
        check_im = np.max(np.abs(commutator(J_mat, Xim) - (+Xre)))
        checks.append(max(check_re, check_im))

    status = 'ALL VERIFIED' if all(c < 1e-10 for c in checks) else 'ERRORS!'
    status_color = '#00ff88' if status == 'ALL VERIFIED' else '#ff3333'

    ax_J.text(0, 0, f'J²=-1\n{status}', fontsize=11, color=status_color,
              ha='center', va='center', fontfamily='monospace', fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a0a',
                        edgecolor=status_color, linewidth=1.5))

    ax_J.text(0, -2.8, '[J, M_i,re] = -M_i,im     [J, M_i,im] = +M_i,re',
              fontsize=9, color='#888888', ha='center', fontfamily='monospace')

    for spine in ax_J.spines.values():
        spine.set_color('#333366')
    ax_J.tick_params(colors='#444444')

def update_display(event=None):
    i1, i2 = state['idx1'], state['idx2']
    X1 = all_basis[i1]
    X2 = all_basis[i2]
    C = commutator(X1, X2)

    # Determine type of each
    type1 = 'k' if i1 < len(k_basis) else 'm'
    type2 = 'k' if i2 < len(k_basis) else 'm'
    color1 = '#4488ff' if type1 == 'k' else '#ff4488'
    color2 = '#4488ff' if type2 == 'k' else '#ff4488'

    draw_matrix(ax_mat1, X1, f'{all_labels[i1]} ∈ {type1}', color1)
    draw_matrix(ax_mat2, X2, f'{all_labels[i2]} ∈ {type2}', color2)

    # Commutator
    in_k = in_span(C, k_basis)
    in_m = in_span(C, m_basis)
    is_zero = np.max(np.abs(C)) < 1e-10

    if is_zero:
        comm_type = '0'
        comm_color = '#666666'
    elif in_k:
        comm_type = '∈ k'
        comm_color = '#4488ff'
    elif in_m:
        comm_type = '∈ m'
        comm_color = '#ff4488'
    else:
        comm_type = '???'
        comm_color = '#ffaa00'

    draw_matrix(ax_comm, C, f'[{all_labels[i1]},{all_labels[i2]}] {comm_type}', comm_color)

    # Info panel
    ax_info.clear()
    ax_info.set_facecolor('#0a0a1a')
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)

    ax_info.text(0.5, 0.95, 'COMMUTATOR', fontsize=12, fontweight='bold',
                 color='#ffaa00', ha='center', fontfamily='monospace')
    ax_info.text(0.5, 0.82, f'[{all_labels[i1]}, {all_labels[i2]}]', fontsize=14,
                 color='#ffffff', ha='center', fontfamily='monospace')
    ax_info.text(0.5, 0.70, f'{type1} × {type2} → {comm_type}', fontsize=14,
                 color=comm_color, ha='center', fontfamily='monospace',
                 fontweight='bold')

    # Expected from symmetric space
    expected = {
        ('k', 'k'): '⊂ k',
        ('k', 'm'): '⊂ m',
        ('m', 'k'): '⊂ m',
        ('m', 'm'): '⊂ k',
    }
    exp = expected[(type1, type2)]
    ax_info.text(0.5, 0.55, f'Symmetric space: [{type1},{type2}] {exp}',
                 fontsize=10, color='#888888', ha='center', fontfamily='monospace')

    matches = (is_zero or
               (exp == '⊂ k' and in_k) or
               (exp == '⊂ m' and in_m))
    check = '  VERIFIED' if matches else '  FAILED!'
    check_color = '#00ff88' if matches else '#ff3333'
    ax_info.text(0.5, 0.42, check, fontsize=14, color=check_color,
                 ha='center', fontfamily='monospace', fontweight='bold')

    # Navigation hints
    ax_info.text(0.5, 0.20, 'Click matrices in the\nstructure grid below\nto select generators',
                 fontsize=9, color='#666688', ha='center',
                 fontfamily='monospace', linespacing=1.5)

    ax_info.text(0.5, 0.05, f'dim k = {len(k_basis)}   dim m = {len(m_basis)}',
                 fontsize=10, color='#888888', ha='center', fontfamily='monospace')

    fig.canvas.draw_idle()

def on_click(event):
    if event.inaxes == ax_struct and event.xdata is not None:
        j = int(round(event.xdata))
        i = int(round(event.ydata))
        n = len(all_basis)
        if 0 <= i < n and 0 <= j < n:
            state['idx1'] = i
            state['idx2'] = j
            update_display()

fig.canvas.mpl_connect('button_press_event', on_click)

# Initial draw
draw_commutator_structure()
draw_complex_structure()
update_display()

plt.show()
