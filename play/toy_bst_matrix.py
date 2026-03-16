#!/usr/bin/env python3
"""
THE BST MATRIX  (Toy 230)
==========================
One matrix transforms counting into physics.

The Chern classes of Q^5 = SO_0(5,2)/[SO(5)xSO(2)] are computed from
Pascal's triangle via a matrix transform:

    c = M . b

where b = Pascal row 7 = [1, 7, 21, 35, 35, 21] and M is the lower-triangular
Toeplitz matrix with entries M_{ij} = (-2)^{i-j} for i >= j.  This IS the
truncated geometric series 1/(1+2h) = 1 - 2h + 4h^2 - 8h^3 + ...

Result: c = [1, 5, 11, 13, 9, 3] -- the Chern classes encoding ALL of BST.

The inverse M^{-1} is beautifully simple: bidiagonal with 1s on the diagonal
and +2 on the subdiagonal.  It encodes the recurrence b_k = c_k + 2*c_{k-1},
i.e., Pascal = Chern + rank * (previous Chern).

The 2 comes from rank(D_IV^n) = 2 for all n.  Both M and M^{-1} are unipotent
(all eigenvalues = 1).  The geometric filter IS the rank of the bounded
symmetric domain.

    The deep statement: Pascal's triangle + rank-2 filter = Standard Model.

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
from scipy.special import comb as scipy_comb

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # channel capacity
RANK = 2                     # rank of D_IV^n (always 2 for type IV)

# ═══════════════════════════════════════════════════════════════════
# CORE MATH: THE BST MATRIX
# ═══════════════════════════════════════════════════════════════════

def pascal_row(g, size):
    """Pascal's triangle row g, truncated to 'size' entries."""
    return np.array([int(scipy_comb(g, k, exact=True)) for k in range(size)])


def bst_matrix(size, r=2):
    """
    The BST matrix M: lower-triangular Toeplitz.
    M_{ij} = (-r)^{i-j} for i >= j, 0 otherwise.

    This is the matrix representation of the geometric series:
        1/(1 + r*h) = sum_{k>=0} (-r)^k h^k

    Applied to Pascal row g, it computes the Chern classes of Q^n:
        P(h) = (1+h)^g / (1+r*h) mod h^{n+1}
    """
    M = np.zeros((size, size))
    for i in range(size):
        for j in range(i + 1):
            M[i, j] = (-r) ** (i - j)
    return M


def bst_matrix_inverse(size, r=2):
    """
    M^{-1}: bidiagonal with 1s on diagonal and +r on subdiagonal.
    Encodes the recurrence: b_k = c_k + r * c_{k-1}.
    """
    Minv = np.eye(size)
    for i in range(1, size):
        Minv[i, i - 1] = r
    return Minv


def chern_from_pascal(g, size, r=2):
    """Compute Chern classes: c = M . b where b = Pascal row g."""
    b = pascal_row(g, size)
    M = bst_matrix(size, r)
    return (M @ b).astype(int)


def geometric_series_coeffs(r, n_terms):
    """Coefficients of 1/(1+r*h) = sum (-r)^k h^k."""
    return np.array([(-r) ** k for k in range(n_terms)])


# ═══════════════════════════════════════════════════════════════════
# COMPUTE AND VERIFY
# ═══════════════════════════════════════════════════════════════════

SIZE = 6
b = pascal_row(genus, SIZE)                # [1, 7, 21, 35, 35, 21]
M = bst_matrix(SIZE, RANK)
Minv = bst_matrix_inverse(SIZE, RANK)
c = (M @ b).astype(int)                   # [1, 5, 11, 13, 9, 3]
identity_check = M @ Minv                  # should be I

# Verify
assert np.allclose(identity_check, np.eye(SIZE)), "M * M^{-1} != I"
assert list(c) == [1, 5, 11, 13, 9, 3], f"Chern classes wrong: {c}"
assert np.allclose(Minv @ c, b), "M^{-1} * c != b"

# Eigenvalues of M
eigvals_M = np.linalg.eigvals(M)
eigvals_Minv = np.linalg.eigvals(Minv)
assert np.allclose(eigvals_M, 1.0), "M is not unipotent!"
assert np.allclose(eigvals_Minv, 1.0), "M^{-1} is not unipotent!"

# Verify the recurrence: c_k = b_k - 2*c_{k-1}
for k in range(SIZE):
    expected = int(b[k]) - (2 * int(c[k - 1]) if k > 0 else 0)
    assert expected == c[k], f"Recurrence fails at k={k}"

# General family: D_IV^n for n = 3, 5, 7, 9
family_ns = [3, 5, 7, 9]
family_data = {}
for n in family_ns:
    g_n = n + 2
    size_n = n + 1
    b_n = pascal_row(g_n, size_n)
    c_n = chern_from_pascal(g_n, size_n, RANK)
    family_data[n] = {'g': g_n, 'size': size_n, 'pascal': b_n, 'chern': c_n}


# ═══════════════════════════════════════════════════════════════════
# TERMINAL OUTPUT
# ═══════════════════════════════════════════════════════════════════

print("=" * 72)
print("  THE BST MATRIX -- One matrix transforms counting into physics")
print("=" * 72)
print()

print("  The BST matrix M (6x6, geometric filter from rank 2):")
print("  M_ij = (-2)^{i-j} for i >= j  (truncated 1/(1+2h) series)")
print()
for i in range(SIZE):
    row_str = "  ["
    for j in range(SIZE):
        val = int(M[i, j])
        row_str += f"{val:5d}"
        if j < SIZE - 1:
            row_str += ","
    row_str += " ]"
    print(row_str)
print()

print("  Pascal row 7 (input):    b =", list(b))
print("  Chern classes (output):  c =", list(c))
print()
print("  Verification: M . b = c  ...  OK")
print()

print("  The inverse M^{-1} (bidiagonal: 1s on diagonal, +2 on subdiagonal):")
print("  Recurrence: b_k = c_k + 2*c_{k-1}")
print()
for i in range(SIZE):
    row_str = "  ["
    for j in range(SIZE):
        val = int(Minv[i, j])
        row_str += f"{val:5d}"
        if j < SIZE - 1:
            row_str += ","
    row_str += " ]"
    print(row_str)
print()

print("  Verification: M . M^{-1} = I     ...  ",
      "OK" if np.allclose(identity_check, np.eye(SIZE)) else "FAIL")
print("  Verification: M^{-1} . c = b     ...  ",
      "OK" if np.allclose(Minv @ c, b) else "FAIL")
print()

print("  Eigenvalues of M:      ", [f"{v.real:.1f}" for v in eigvals_M])
print("  Eigenvalues of M^{-1}: ", [f"{v.real:.1f}" for v in eigvals_Minv])
print("  BOTH are UNIPOTENT (all eigenvalues = 1)")
print()

print("  The recurrence c_k = C(7,k) - 2*c_{k-1}:")
for k in range(SIZE):
    prev = f" - 2*{c[k-1]}" if k > 0 else ""
    print(f"    c_{k} = {b[k]}{prev} = {c[k]}")
print()

print("  --- The D_IV^n Family ---")
print()
for n in family_ns:
    d = family_data[n]
    tag = " <-- OUR UNIVERSE" if n == 5 else ""
    print(f"  n = {n}:  g = {d['g']}")
    print(f"    Pascal row {d['g']}:  {list(d['pascal'])}")
    print(f"    Chern classes:  {list(d['chern'])}{tag}")
    print()

print("  --- Physical Meaning of [1, 5, 11, 13, 9, 3] ---")
print()
print(f"  c_0 = 1   trivial (normalization)")
print(f"  c_1 = 5   = n_C (complex dimension)")
print(f"  c_2 = 11  = dim K = dim(SO(5) x SO(2))")
print(f"  c_3 = 13  -> sin^2 theta_W = c_5/c_3 = 3/13 = {3/13:.6f}")
print(f"  c_4 = 9   -> Reality Budget = c_4/c_1 = 9/5 = {9/5:.1f}")
print(f"  c_5 = 3   = N_c (color charges)")
print()
print(f"  The deep statement: Pascal's triangle + rank-2 filter = Standard Model")
print(f"  The 2 IS the rank of D_IV^n. The filter IS the geometry.")
print()
print("=" * 72)


# ═══════════════════════════════════════════════════════════════════
# COLORS AND STYLE
# ═══════════════════════════════════════════════════════════════════

BG = '#0a0a1a'
GREEN = '#44cc88'
GREEN_DIM = '#227744'
GREEN_BRIGHT = '#66ffaa'
WHITE = '#ffffff'
GOLD = '#ffcc44'
GOLD_DIM = '#aa8822'
CYAN = '#44ccff'
CYAN_DIM = '#226688'
ORANGE = '#ff8844'
PINK = '#ff66aa'
RED = '#ff4444'
PURPLE = '#aa66ff'
GRAY = '#666688'
DARK_PANEL = '#0d0d22'

# Pascal bar colors (warm gradient)
PASCAL_COLORS = ['#ff6644', '#ff8844', '#ffaa44', '#ffcc44', '#ffee44', '#eeff44']
# Chern bar colors (cool gradient)
CHERN_COLORS = ['#44ff88', '#44ffaa', '#44ffcc', '#44ccff', '#4488ff', '#4466ff']

glow = [pe.withStroke(linewidth=2, foreground=GREEN_DIM)]
glow_gold = [pe.withStroke(linewidth=2, foreground=GOLD_DIM)]


# ═══════════════════════════════════════════════════════════════════
# FIGURE SETUP: 2x3 LAYOUT
# ═══════════════════════════════════════════════════════════════════

fig = plt.figure(figsize=(18, 12), facecolor=BG)
fig.canvas.manager.set_window_title('The BST Matrix (Toy 106) -- BST')

fig.text(0.5, 0.975, 'THE BST MATRIX',
         fontsize=28, fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#114422')])
fig.text(0.5, 0.950, 'One matrix transforms counting into physics',
         fontsize=13, color=GREEN_DIM, ha='center', fontfamily='monospace')

# Panel positions: [left, bottom, width, height]
pw, ph = 0.29, 0.38
row1_y = 0.54
row2_y = 0.06
col_x = [0.035, 0.355, 0.675]


def make_panel(col, row):
    """Create an axes for the given column (0-2) and row (0=top, 1=bottom)."""
    y = row1_y if row == 0 else row2_y
    ax = fig.add_axes((col_x[col], y, pw, ph))
    ax.set_facecolor(DARK_PANEL)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax


def add_border(ax, color=GREEN_DIM):
    """Add a thin colored border to a panel."""
    for side in ['top', 'bottom', 'left', 'right']:
        ax.spines[side].set_visible(True)
        ax.spines[side].set_color(color)
        ax.spines[side].set_linewidth(1)


# ═══════════════════════════════════════════════════════════════════
# PANEL 1: Pascal -> Chern Transform
# ═══════════════════════════════════════════════════════════════════

ax1 = make_panel(0, 0)

ax1.text(0.5, 0.97, 'PASCAL \u2192 CHERN TRANSFORM', fontsize=13,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace', path_effects=glow)

# Pascal bars (top section)
ax1.text(0.5, 0.90, 'Pascal row 7', fontsize=10, color=GOLD,
         ha='center', fontfamily='monospace')
bar_w = 0.10
pascal_max = max(b)
for i, val in enumerate(b):
    x = 0.12 + i * 0.14
    bh = 0.17 * val / pascal_max
    rect = plt.Rectangle((x, 0.72), bar_w, bh,
                          facecolor=PASCAL_COLORS[i], alpha=0.85,
                          edgecolor='#ffffff33', linewidth=0.5)
    ax1.add_patch(rect)
    ax1.text(x + bar_w / 2, 0.695, str(val), fontsize=8,
             color=PASCAL_COLORS[i], ha='center', fontfamily='monospace')

# Arrow: Pascal -> M -> Chern
ax1.annotate('', xy=(0.5, 0.49), xytext=(0.5, 0.67),
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5,
                             mutation_scale=15))
ax1.text(0.60, 0.575, 'M', fontsize=18, fontweight='bold', color=GREEN,
         ha='center', fontfamily='monospace', path_effects=glow)
ax1.text(0.60, 0.535, '(rank-2', fontsize=7, color=GREEN_DIM,
         ha='center', fontfamily='monospace')
ax1.text(0.60, 0.505, 'filter)', fontsize=7, color=GREEN_DIM,
         ha='center', fontfamily='monospace')

# Chern bars (bottom section)
ax1.text(0.5, 0.46, 'Chern classes', fontsize=10, color=CYAN,
         ha='center', fontfamily='monospace')
chern_max = max(c)
subscripts = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084', '\u2085']
for i, val in enumerate(c):
    x = 0.12 + i * 0.14
    bh = 0.17 * val / chern_max
    rect = plt.Rectangle((x, 0.27), bar_w, bh,
                          facecolor=CHERN_COLORS[i], alpha=0.85,
                          edgecolor='#ffffff33', linewidth=0.5)
    ax1.add_patch(rect)
    ax1.text(x + bar_w / 2, 0.24, str(val), fontsize=9,
             color=CHERN_COLORS[i], ha='center', fontfamily='monospace',
             fontweight='bold')
    ax1.text(x + bar_w / 2, 0.21, f'c{subscripts[i]}', fontsize=7,
             color=GRAY, ha='center', fontfamily='monospace')

# The recurrence shown compactly
ax1.text(0.5, 0.15, 'Recurrence: c\u2096 = C(7,k) \u2212 2\u00b7c\u2096\u208b\u2081',
         fontsize=8, color=WHITE, ha='center', fontfamily='monospace')

# Summary
ax1.text(0.5, 0.08, 'All of physics =', fontsize=9,
         color=WHITE, ha='center', fontfamily='monospace')
ax1.text(0.5, 0.03, "Pascal's triangle filtered through rank 2",
         fontsize=9, color=GREEN, ha='center', fontfamily='monospace',
         fontweight='bold', path_effects=glow)

add_border(ax1)


# ═══════════════════════════════════════════════════════════════════
# PANEL 2: The Matrix M and Its Inverse
# ═══════════════════════════════════════════════════════════════════

ax2 = make_panel(1, 0)

ax2.text(0.5, 0.97, 'M AND ITS INVERSE', fontsize=13,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace', path_effects=glow)


def draw_matrix(ax, mat, x0, y0, cell_w, cell_h, title, title_color,
                zero_color='#111122', pos_color=GREEN, neg_color=RED,
                text_size=7):
    """Draw a matrix as a colored grid with values."""
    n = mat.shape[0]
    ax.text(x0 + n * cell_w / 2, y0 + n * cell_h + 0.025, title,
            fontsize=10, fontweight='bold', color=title_color,
            ha='center', fontfamily='monospace')
    for i in range(n):
        for j in range(n):
            val = int(round(mat[i, j]))
            x = x0 + j * cell_w
            y = y0 + (n - 1 - i) * cell_h
            if val == 0:
                fc = zero_color
                tc = '#222233'
            elif val > 0:
                intensity = min(abs(val) / 32, 1.0)
                r_comp = int(10 + 20 * intensity)
                g_comp = int(30 + 60 * intensity)
                fc = f'#{r_comp:02x}{g_comp:02x}{r_comp:02x}'
                tc = pos_color
            else:
                intensity = min(abs(val) / 32, 1.0)
                r_comp = int(30 + 40 * intensity)
                fc = f'#{r_comp:02x}{10:02x}{10:02x}'
                tc = neg_color
            rect = plt.Rectangle((x, y), cell_w, cell_h,
                                 facecolor=fc, edgecolor='#333355',
                                 linewidth=0.5)
            ax.add_patch(rect)
            label = str(val) if val != 0 else '\u00b7'
            ax.text(x + cell_w / 2, y + cell_h / 2, label,
                    fontsize=text_size, color=tc, ha='center', va='center',
                    fontfamily='monospace',
                    fontweight='bold' if val != 0 else 'normal')


# Draw M on the left (full lower-triangular Toeplitz)
cw, ch = 0.053, 0.053
draw_matrix(ax2, M, 0.02, 0.47, cw, ch,
            'M : (-2)\u2071\u207b\u02b2', GREEN)

# Draw M^{-1} on the right (bidiagonal)
draw_matrix(ax2, Minv, 0.52, 0.47, cw, ch,
            'M\u207b\u00b9 : bidiagonal', GOLD, pos_color=GOLD)

# Multiplication symbol and result
ax2.text(0.42, 0.67, '\u00d7', fontsize=22, color=WHITE, ha='center',
         va='center', fontfamily='monospace')
ax2.text(0.92, 0.67, '= I', fontsize=14, fontweight='bold', color=WHITE,
         ha='center', va='center', fontfamily='monospace')

# Annotations
ax2.text(0.20, 0.43, 'Geometric series', fontsize=7, color=GREEN_DIM,
         ha='center', fontfamily='monospace')
ax2.text(0.20, 0.39, 'powers of (-2)', fontsize=7, color=GREEN_DIM,
         ha='center', fontfamily='monospace')

ax2.text(0.72, 0.43, 'Simple: 1s and 2s', fontsize=7, color=GOLD_DIM,
         ha='center', fontfamily='monospace')
ax2.text(0.72, 0.39, 'b\u2096 = c\u2096 + 2\u00b7c\u2096\u208b\u2081',
         fontsize=7, color=GOLD_DIM, ha='center', fontfamily='monospace')

# Key insight box
box_y = 0.22
ax2.add_patch(plt.Rectangle((0.05, 0.05), 0.90, 0.30,
              facecolor='#0a0a22', edgecolor=GREEN_DIM,
              linewidth=1, alpha=0.6))
ax2.text(0.5, box_y + 0.08, 'KEY INSIGHT', fontsize=10, fontweight='bold',
         color=ORANGE, ha='center', fontfamily='monospace')
ax2.text(0.5, box_y + 0.01, 'M encodes the geometric filter 1/(1+2h)',
         fontsize=8, color=WHITE, ha='center', fontfamily='monospace')
ax2.text(0.5, box_y - 0.05, 'The 2 = rank(D\u1d35\u1d5b\u207f) for ALL n',
         fontsize=8, color=GREEN, ha='center', fontfamily='monospace',
         fontweight='bold')
ax2.text(0.5, box_y - 0.11, 'Both M and M\u207b\u00b9 are unipotent (eigenvalues = 1)',
         fontsize=7, color=CYAN, ha='center', fontfamily='monospace')

add_border(ax2)


# ═══════════════════════════════════════════════════════════════════
# PANEL 3: The Geometric Series
# ═══════════════════════════════════════════════════════════════════

ax3 = make_panel(2, 0)

ax3.text(0.5, 0.97, 'THE GEOMETRIC SERIES', fontsize=13,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace', path_effects=glow)

# The formula
ax3.text(0.5, 0.88, '1/(1+2h) = 1 \u2212 2h + 4h\u00b2 \u2212 8h\u00b3 + ...',
         fontsize=10, color=WHITE, ha='center', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#0a1a0a',
                   edgecolor=GREEN_DIM, linewidth=1.5))

ax3.text(0.5, 0.80, 'This IS the matrix M (row by row)',
         fontsize=9, color=GREEN_DIM, ha='center', fontfamily='monospace')

# Plot partial sums of the geometric series in an embedded axes
ax3_plot = fig.add_axes((0.71, 0.68, 0.23, 0.22))
ax3_plot.set_facecolor(DARK_PANEL)

h_vals = np.linspace(-0.3, 0.45, 300)
exact = 1.0 / (1.0 + 2.0 * h_vals)

colors_partial = ['#ff4444', '#ff8844', '#ffcc44', '#44ff88', '#44ccff', '#4488ff']
labels_partial = ['N=0', 'N=1', 'N=2', 'N=3', 'N=4', 'N=5']

for N in range(6):
    partial = np.zeros_like(h_vals)
    for k in range(N + 1):
        partial += ((-2) ** k) * h_vals ** k
    ax3_plot.plot(h_vals, partial, color=colors_partial[N], alpha=0.6,
                  linewidth=1.2, label=labels_partial[N])

ax3_plot.plot(h_vals, exact, color=WHITE, linewidth=2, linestyle='--',
              label='exact', alpha=0.8)

ax3_plot.set_xlim(-0.3, 0.45)
ax3_plot.set_ylim(-2, 5)
ax3_plot.axhline(y=0, color=GRAY, linewidth=0.5, alpha=0.5)
ax3_plot.axvline(x=0, color=GRAY, linewidth=0.5, alpha=0.5)
ax3_plot.set_xlabel('h', fontsize=8, color=GRAY, fontfamily='monospace')
ax3_plot.set_ylabel('partial sum', fontsize=7, color=GRAY,
                    fontfamily='monospace')
ax3_plot.tick_params(colors=GRAY, labelsize=6)
for spine in ax3_plot.spines.values():
    spine.set_color(GREEN_DIM)
    spine.set_linewidth(0.5)
ax3_plot.legend(fontsize=5, loc='upper left', framealpha=0.3,
                labelcolor=WHITE, facecolor=DARK_PANEL, edgecolor=GREEN_DIM)

# Coefficients as bars
geo_coeffs = geometric_series_coeffs(2, 6)
ax3.text(0.5, 0.34, 'Series coefficients (\u22122)\u1d4f :', fontsize=9,
         color=WHITE, ha='center', fontfamily='monospace')
for i, val in enumerate(geo_coeffs):
    x = 0.10 + i * 0.14
    bh = 0.10 * abs(val) / 32
    color = GREEN if val > 0 else RED
    y_base = 0.19
    rect = plt.Rectangle((x, y_base), 0.10, bh,
                          facecolor=color, alpha=0.7,
                          edgecolor='#ffffff33', linewidth=0.5)
    ax3.add_patch(rect)
    sign = '+' if val >= 0 else ''
    ax3.text(x + 0.05, y_base - 0.04, f'{sign}{int(val)}', fontsize=7,
             color=color, ha='center', fontfamily='monospace',
             fontweight='bold')

# Explanation
ax3.text(0.5, 0.10, '2 = rank of B\u2082 (restricted root system)',
         fontsize=9, color=ORANGE, ha='center', fontfamily='monospace')
ax3.text(0.5, 0.04, 'For ALL D\u1d35\u1d5b\u207f: rank = 2, same filter',
         fontsize=9, color=GREEN, ha='center', fontfamily='monospace',
         fontweight='bold')

add_border(ax3)


# ═══════════════════════════════════════════════════════════════════
# PANEL 4: The Convolution
# ═══════════════════════════════════════════════════════════════════

ax4 = make_panel(0, 1)

ax4.text(0.5, 0.97, 'THE CONVOLUTION', fontsize=13,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace', path_effects=glow)

ax4.text(0.5, 0.89, 'c\u2096 = \u03a3\u2c7c C(7, k\u2212j) \u00d7 (\u22122)\u02b2',
         fontsize=10, color=WHITE, ha='center', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a0a',
                   edgecolor=GREEN_DIM, linewidth=1.5))

# Show the construction of each Chern class
y_start = 0.79
y_step = 0.115

for k in range(6):
    y = y_start - k * y_step

    # Subscript label
    ax4.text(0.03, y, f'c{subscripts[k]}', fontsize=10,
             color=CHERN_COLORS[k], ha='left',
             fontfamily='monospace', fontweight='bold')

    # Build the sum string showing contributing terms
    terms = []
    total = 0
    for j in range(k + 1):
        binom_val = int(scipy_comb(genus, k - j, exact=True))
        power_val = (-2) ** j
        contrib = binom_val * power_val
        total += contrib
        if j == 0:
            terms.append(f'{binom_val}')
        else:
            if power_val < 0:
                terms.append(f'\u2212{binom_val}\u00d7{abs(power_val)}')
            else:
                terms.append(f'+{binom_val}\u00d7{abs(power_val)}')

    sum_str = ' '.join(terms)
    ax4.text(0.13, y, f'= {sum_str}', fontsize=7,
             color=WHITE, ha='left', fontfamily='monospace')
    ax4.text(0.92, y, f'= {total}', fontsize=10, fontweight='bold',
             color=CHERN_COLORS[k], ha='center', fontfamily='monospace')

    # Small colored contribution bars below the text
    bar_y = y - 0.055
    for j in range(k + 1):
        binom_val = int(scipy_comb(genus, k - j, exact=True))
        power_val = (-2) ** j
        contrib = binom_val * power_val
        bar_x = 0.13 + j * 0.12
        bar_w_c = 0.08
        # Scale: largest contribution is C(7,2)*4 = 84, use 70 as max
        bar_h_c = abs(contrib) / 70 * 0.035
        color = GREEN if contrib > 0 else RED
        rect = plt.Rectangle((bar_x, bar_y), bar_w_c,
                              max(bar_h_c, 0.003),
                              facecolor=color, alpha=0.6,
                              edgecolor='none')
        ax4.add_patch(rect)

# Summary
ax4.text(0.5, 0.06, 'Alternating signs create', fontsize=9,
         color=WHITE, ha='center', fontfamily='monospace')
ax4.text(0.5, 0.01, 'the non-monotonic Chern vector', fontsize=9,
         color=GREEN, ha='center', fontfamily='monospace', fontweight='bold')

add_border(ax4)


# ═══════════════════════════════════════════════════════════════════
# PANEL 5: From Chern to Physics
# ═══════════════════════════════════════════════════════════════════

ax5 = make_panel(1, 1)

ax5.text(0.5, 0.97, 'FROM CHERN TO PHYSICS', fontsize=13,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace', path_effects=glow)

# The Chern vector prominently
ax5.text(0.5, 0.88, '[ 1,  5,  11,  13,  9,  3 ]', fontsize=14,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#0a2a1a',
                   edgecolor=GREEN, linewidth=2))

# Each Chern class mapped to physics
physics_map = [
    ('c\u2080 = 1', 'normalization', GRAY, ''),
    ('c\u2081 = 5', 'n_C = complex dimension', CYAN,
     '= dim_C(D_IV^5)'),
    ('c\u2082 = 11', 'dim K = dim(SO(5)\u00d7SO(2))', PURPLE,
     '= isotropy dimension'),
    ('c\u2083 = 13', 'sin\u00b2\u03b8_W = c\u2085/c\u2083 = 3/13', ORANGE,
     f'= {3/13:.6f}'),
    ('c\u2084 = 9', 'Reality Budget = c\u2084/c\u2081 = 9/5', PINK,
     '= \u039b \u00d7 N'),
    ('c\u2085 = 3', 'N_c = color charges', RED,
     '= quarks carry 3 colors'),
]

y_pos = 0.78
for chern_label, meaning, color, detail in physics_map:
    ax5.text(0.04, y_pos, chern_label, fontsize=10, fontweight='bold',
             color=color, ha='left', fontfamily='monospace')
    ax5.text(0.29, y_pos, meaning, fontsize=9,
             color=WHITE, ha='left', fontfamily='monospace')
    if detail:
        ax5.text(0.29, y_pos - 0.045, detail, fontsize=8,
                 color=color, ha='left', fontfamily='monospace', alpha=0.7)
    y_pos -= 0.115

# Summary
ax5.text(0.5, 0.12, 'M transforms combinatorics', fontsize=10,
         color=WHITE, ha='center', fontfamily='monospace')
ax5.text(0.5, 0.06, 'into the Standard Model', fontsize=10,
         color=GREEN, ha='center', fontfamily='monospace',
         fontweight='bold', path_effects=glow)
ax5.text(0.5, 0.01, 'Six integers. Zero free parameters.',
         fontsize=9, color=GOLD, ha='center', fontfamily='monospace')

add_border(ax5)


# ═══════════════════════════════════════════════════════════════════
# PANEL 6: The General D_IV^n Family
# ═══════════════════════════════════════════════════════════════════

ax6 = make_panel(2, 1)

ax6.text(0.5, 0.97, 'THE D_IV^n FAMILY', fontsize=13,
         fontweight='bold', color=GREEN_BRIGHT, ha='center',
         fontfamily='monospace', path_effects=glow)

ax6.text(0.5, 0.90, 'Same rank-2 filter for all n',
         fontsize=9, color=GREEN_DIM, ha='center', fontfamily='monospace')

# For each n, show Pascal row and Chern classes
family_colors = {3: '#ff6644', 5: '#44ff88', 7: '#4488ff', 9: '#aa66ff'}
y_base_fam = 0.82

for idx, n in enumerate(family_ns):
    d = family_data[n]
    y = y_base_fam - idx * 0.19
    col = family_colors[n]

    # Highlight n=5
    if n == 5:
        highlight = plt.Rectangle((0.01, y - 0.09), 0.98, 0.19,
                                   facecolor='#0a2a1a', edgecolor=GREEN,
                                   linewidth=1.5, alpha=0.4)
        ax6.add_patch(highlight)
        ax6.text(0.97, y + 0.07, '\u2190 our\nuniverse', fontsize=7,
                 color=GREEN, ha='right', va='top', fontfamily='monospace')

    ax6.text(0.03, y + 0.05, f'n={n}', fontsize=11, fontweight='bold',
             color=col, ha='left', fontfamily='monospace')
    ax6.text(0.03, y - 0.01, f'g={d["g"]}', fontsize=8,
             color=GRAY, ha='left', fontfamily='monospace')

    # Pascal values
    pascal_str = str(list(d['pascal']))
    ax6.text(0.16, y + 0.05, f'P: {pascal_str}', fontsize=7,
             color=GOLD_DIM, ha='left', fontfamily='monospace')

    # Chern values
    chern_str = str(list(d['chern']))
    ax6.text(0.16, y - 0.02, f'C: {chern_str}', fontsize=7,
             color=col, ha='left', fontfamily='monospace', fontweight='bold')

    # c_1 value (= n for our family)
    c1_val = d['chern'][1] if len(d['chern']) > 1 else '?'
    ax6.text(0.16, y - 0.06, f'c\u2081={c1_val}=n_C', fontsize=6,
             color=GRAY, ha='left', fontfamily='monospace')

# Summary at bottom
ax6.text(0.5, 0.06, 'Only g = n+2 changes (which Pascal row)',
         fontsize=8, color=WHITE, ha='center', fontfamily='monospace')
ax6.text(0.5, 0.01, 'n_C = 5 maximizes the fine structure constant \u03b1',
         fontsize=9, color=GOLD, ha='center', fontfamily='monospace',
         fontweight='bold')

add_border(ax6)


# ═══════════════════════════════════════════════════════════════════
# BOTTOM CREDITS
# ═══════════════════════════════════════════════════════════════════

fig.text(0.5, 0.005,
         'BST Toy 106  |  P(h) = (1+h)\u2077/(1+2h) mod h\u2076  '
         '|  c = M \u00b7 b  where M = geometric filter  '
         '|  \u00a9 2026 Casey Koons',
         fontsize=8, color=GRAY, ha='center', fontfamily='monospace')

plt.show()
