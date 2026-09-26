#!/usr/bin/env python3
"""
Toy 5824 — figure (R10 item 3): which double traces a contact vertex shifts, D_IV^5 point vs AdS_6 point (Elie, 2026-09-26).
Prereg 5d4ce093. Data: (left) AdS_6 φ⁴ at d = 5, Δ = 5/2: STRUCTURE 'nonzero only for l = 0' PINNED (HPPS 0907.0151 :611–621, Grace);
n-shape γ(n,0)/γ(0,0) = 1, 2.604, 5.234, 8.832, 13.393 DERIVED by Grace's agent (not printed in HPPS for general d) — labelled so.
(middle) D_IV^5 holomorphic contact on H²⊗H², toy 5821: only (0,0).  (right) same vertex on Rac⊗Rac, toy 5823: γ_s, s = 0..6.
Overall size and sign are free in every panel: values normalised to the (0,0) entry.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
ramp = ['#cde2fb', '#9ec5f4', '#6da7ec', '#3987e5', '#256abf', '#184f95', '#0d366b']
cmap = LinearSegmentedColormap.from_list('blue', ramp)
ads = np.zeros((5, 5)); ads[:, 0] = [1, 2.604, 5.234, 8.832, 13.393]
bst = np.zeros((5, 5)); bst[0, 0] = 1
rac = np.array([1, 0, 0, 0, 0, 0, 0.])
ink, muted, zero_bg = '#1f1f1f', '#6b6b6b', '#f4f3f0'
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6), gridspec_kw={'width_ratios': [1, 1, 1.15]})
def heat(ax, M, title, sub):
    vmax = 13.393
    for n in range(5):
        for l in range(5):
            v = M[n, l]
            col = zero_bg if v == 0 else cmap(0.15 + 0.85*v/vmax)
            ax.add_patch(plt.Rectangle((l + 0.04, n + 0.04), 0.92, 0.92, color=col, lw=0))
            ax.text(l + 0.5, n + 0.5, '0' if v == 0 else f'{v:.3g}', ha='center', va='center', fontsize=9,
                    color=(muted if v == 0 else ('white' if v/vmax > 0.35 else ink)))
    ax.set_xlim(0, 5); ax.set_ylim(5, 0); ax.set_aspect('equal')
    ax.set_xticks(np.arange(5) + 0.5); ax.set_xticklabels(range(5)); ax.set_yticks(np.arange(5) + 0.5); ax.set_yticklabels(range(5))
    ax.set_xlabel('spin l', color=muted); ax.set_ylabel('n  (Δ = 5 + 2n + l)', color=muted)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(colors=muted, length=0)
    ax.set_title(title, loc='left', fontsize=11, color=ink, pad=22); ax.text(0, 1.015, sub, fontsize=8, color=muted, transform=ax.transAxes, va='bottom')
heat(axs[0], ads, 'AdS$_6$ point: $\\phi^4$ contact', 'l = 0 only: PINNED (HPPS :611–621)\nn-shape: DERIVED (Grace agent)')
heat(axs[1], bst, '$D_{IV}^5$ point: holomorphic contact', 'toy 5821 (exact): shifts only $[\\phi\\phi]_{0,0}$')
ax = axs[2]
xs = np.arange(7)
ax.bar(xs, rac, width=0.6, color=ramp[4], zorder=2)
for x in xs:
    if rac[x] == 0: ax.plot([x - 0.3, x + 0.3], [0, 0], color=muted, lw=2, zorder=3)
ax.set_xticks(xs); ax.set_ylim(0, 1.25); ax.set_yticks([0, 1]); ax.set_yticklabels(['0', 'γ$_0$'])
ax.set_xlabel('spin s  (current at Δ = 3 + s)', color=muted)
ax.grid(axis='y', color='#e6e5e1', lw=0.8, zorder=0)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#bdbcb8'); ax.tick_params(colors=muted, length=0)
ax.set_title('Rac⊗Rac: same vertex, currents', loc='left', fontsize=11, color=ink, pad=22)
ax.text(0, 1.015, 'toy 5823: γ$_s$ = 0 for s = 1..6 — every current spared', fontsize=8, color=muted, transform=ax.transAxes, va='bottom')
ax.text(1.1, 0.12, 'spared: s = 1…6', fontsize=9, color=muted)
fig.suptitle('Which double traces a contact vertex shifts (first order; size and sign free, normalised to the (0,0) entry)',
             x=0.01, ha='left', fontsize=12, color=ink)
fig.tight_layout(rect=(0, 0, 1, 0.93))
out = 'play/figs/toy_5824_contact_vertex_D_IV5_vs_AdS6.png'
fig.savefig(out, dpi=150, facecolor='white')
print("wrote", out)
print("TABLE (text view):")
print("  AdS6 φ⁴  γ(n,0)/γ(0,0):", list(ads[:, 0]), " l > 0: all 0")
print("  D_IV5 holomorphic contact: (0,0) = 1, all else 0")
print("  Rac level γ_s, s = 0..6:", list(rac))
