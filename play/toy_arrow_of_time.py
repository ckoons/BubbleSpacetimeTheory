#!/usr/bin/env python3
"""
COMMITMENT IRREVERSIBILITY — THE ARROW OF TIME
================================================
BST conservation law stronger than the second law of thermodynamics:

    ΔN_committed ≥ 0,  exactly,  always.

Committed S¹ windings cannot spontaneously unwind.
Entropy can fluctuate down; commitments cannot.
This IS the arrow of time.

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
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
import time

# ─── Grid parameters ───
GRID_COLS = 16
GRID_ROWS = 13
N_CONTACTS = GRID_COLS * GRID_ROWS  # 208 contact points
COMMIT_RADIUS = 3  # how many neighbors to commit on click

# ─── State ───
committed = np.zeros(N_CONTACTS, dtype=bool)
commit_times = np.zeros(N_CONTACTS)  # when each was committed
commitment_count = 0
commitment_history = [0]
entropy_history = [50.0]
time_steps = [0]
step_counter = 0
undo_flash_time = 0  # timestamp of last undo attempt

# ─── Grid positions (hex-offset for visual appeal) ───
grid_x = np.zeros(N_CONTACTS)
grid_y = np.zeros(N_CONTACTS)
for i in range(N_CONTACTS):
    row = i // GRID_COLS
    col = i % GRID_COLS
    offset = 0.3 if row % 2 else 0.0
    grid_x[i] = (col + offset) / GRID_COLS
    grid_y[i] = row / GRID_ROWS

# Normalize to [0.05, 0.95]
grid_x = 0.05 + 0.90 * grid_x
grid_y = 0.05 + 0.90 * grid_y

# ─── Color maps ───
UNCOMMITTED_COLOR = '#1a1a2e'
UNCOMMITTED_EDGE = '#2a2a4e'
GLOW_COLORS = ['#ff8800', '#ffaa00', '#ffcc44', '#ffd700', '#ff6600', '#ffbb33']


def committed_color(t):
    """Return a warm color based on commit time — older = deeper orange, newer = bright gold."""
    age = step_counter - t
    if age < 5:
        return '#ffd700'  # fresh gold
    elif age < 20:
        return '#ffaa00'  # warm orange-gold
    elif age < 50:
        return '#ff8800'  # deep orange
    else:
        return '#ff6600'  # ember


# ─── Figure ───
fig = plt.figure(figsize=(18, 10), facecolor='#0a0a1a')
fig.canvas.manager.set_window_title('Commitment Irreversibility — The Arrow of Time — BST')

# ─── Title ───
fig.text(0.5, 0.97, 'COMMITMENT IRREVERSIBILITY', fontsize=26, fontweight='bold',
         color='#ffd700', ha='center', fontfamily='monospace',
         path_effects=[pe.withStroke(linewidth=3, foreground='#663300')])
fig.text(0.5, 0.935, 'The Arrow of Time in Bubble Spacetime Theory',
         fontsize=13, color='#aa8844', ha='center', fontfamily='monospace')

# ═══════════════════════════════════════════════════════
# LEFT PANEL — The Contact Grid
# ═══════════════════════════════════════════════════════
ax_grid = fig.add_axes([0.02, 0.08, 0.32, 0.78])
ax_grid.set_facecolor('#0a0a1a')
ax_grid.set_xlim(-0.02, 1.02)
ax_grid.set_ylim(-0.08, 1.08)
ax_grid.axis('off')

ax_grid.text(0.5, 1.06, 'CONTACT GRID  (S² × S¹)', fontsize=13, fontweight='bold',
             color='#ffaa00', ha='center', fontfamily='monospace')
ax_grid.text(0.5, 1.02, 'Click to commit contacts — they never go dark',
             fontsize=9, color='#887744', ha='center', fontfamily='monospace')

# Draw contact points
contact_circles = []
glow_circles = []
for i in range(N_CONTACTS):
    # Outer glow (invisible until committed)
    glow = plt.Circle((grid_x[i], grid_y[i]), 0.028, color='#ffd700',
                       alpha=0.0, zorder=1)
    ax_grid.add_patch(glow)
    glow_circles.append(glow)

    # Main circle
    circ = plt.Circle((grid_x[i], grid_y[i]), 0.018,
                       facecolor=UNCOMMITTED_COLOR, edgecolor=UNCOMMITTED_EDGE,
                       linewidth=0.5, zorder=2)
    ax_grid.add_patch(circ)
    contact_circles.append(circ)

# Commitment counter text
counter_text = ax_grid.text(0.5, -0.04, 'COMMITMENTS: 0',
                            fontsize=18, fontweight='bold', color='#ffd700',
                            ha='center', fontfamily='monospace',
                            path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

# "Try to Undo" button
ax_undo = fig.add_axes([0.08, 0.01, 0.18, 0.05])
ax_undo.set_facecolor('#2a0a0a')
btn_undo = Button(ax_undo, 'TRY TO UNDO', color='#2a0a0a', hovercolor='#4a1a1a')
btn_undo.label.set_color('#ff4444')
btn_undo.label.set_fontsize(12)
btn_undo.label.set_fontweight('bold')
btn_undo.label.set_fontfamily('monospace')

# Impossible text (hidden until button pressed)
impossible_text = fig.text(0.17, 0.075, '', fontsize=14, fontweight='bold',
                           color='#ff0000', ha='center', fontfamily='monospace',
                           path_effects=[pe.withStroke(linewidth=2, foreground='#440000')],
                           alpha=0.0)

# ═══════════════════════════════════════════════════════
# CENTER PANEL — Commitment vs Entropy plots
# ═══════════════════════════════════════════════════════

# Top: Commitment staircase
ax_commit = fig.add_axes([0.40, 0.50, 0.26, 0.34])
ax_commit.set_facecolor('#0d0d1a')
ax_commit.set_title('Commitments: monotone ↑ (ALWAYS)', fontsize=10,
                     fontweight='bold', color='#ffd700', fontfamily='monospace', pad=8)
ax_commit.tick_params(colors='#666666', labelsize=8)
for spine in ax_commit.spines.values():
    spine.set_color('#333344')
ax_commit.set_ylabel('N committed', fontsize=9, color='#aa8844', fontfamily='monospace')
ax_commit.set_xlabel('time', fontsize=9, color='#666666', fontfamily='monospace')

commit_line, = ax_commit.plot([], [], color='#ffd700', linewidth=2.5,
                               drawstyle='steps-post',
                               path_effects=[pe.withStroke(linewidth=4, foreground='#664400')])
ax_commit.set_xlim(0, 100)
ax_commit.set_ylim(0, 20)

# "NEVER DECREASES" annotation
ax_commit.text(0.98, 0.08, 'NEVER DECREASES', fontsize=9, fontweight='bold',
               color='#ff8800', ha='right', transform=ax_commit.transAxes,
               fontfamily='monospace', alpha=0.8,
               bbox=dict(boxstyle='round,pad=0.2', facecolor='#1a1000', edgecolor='#664400'))

# Bottom: Entropy wiggly line
ax_entropy = fig.add_axes([0.40, 0.10, 0.26, 0.34])
ax_entropy.set_facecolor('#0d0d1a')
ax_entropy.set_title('Entropy: fluctuates ↑↓ (usually up)', fontsize=10,
                      fontweight='bold', color='#44cc66', fontfamily='monospace', pad=8)
ax_entropy.tick_params(colors='#666666', labelsize=8)
for spine in ax_entropy.spines.values():
    spine.set_color('#333344')
ax_entropy.set_ylabel('S (entropy)', fontsize=9, color='#44aa66', fontfamily='monospace')
ax_entropy.set_xlabel('time', fontsize=9, color='#666666', fontfamily='monospace')

entropy_line, = ax_entropy.plot([], [], color='#44cc66', linewidth=1.5, alpha=0.9)
entropy_fill = None
ax_entropy.set_xlim(0, 100)
ax_entropy.set_ylim(30, 80)

# "CAN DECREASE" annotation
ax_entropy.text(0.98, 0.08, 'CAN DECREASE', fontsize=9, fontweight='bold',
                color='#44cc66', ha='right', transform=ax_entropy.transAxes,
                fontfamily='monospace', alpha=0.8,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#001a0a', edgecolor='#226633'))

# Comparison text between the two plots
fig.text(0.53, 0.465, '▲ Ratchet  vs  Random Walk ▼', fontsize=10,
         color='#888888', ha='center', fontfamily='monospace', fontstyle='italic')

# ═══════════════════════════════════════════════════════
# RIGHT PANEL — The Arrow + Law Statement
# ═══════════════════════════════════════════════════════
ax_arrow = fig.add_axes([0.70, 0.08, 0.28, 0.78])
ax_arrow.set_facecolor('#0a0a1a')
ax_arrow.set_xlim(0, 1)
ax_arrow.set_ylim(0, 1)
ax_arrow.axis('off')

ax_arrow.text(0.5, 0.96, 'THE ARROW OF TIME', fontsize=15, fontweight='bold',
              color='#ffd700', ha='center', fontfamily='monospace',
              path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])

# Draw the large arrow from PAST to FUTURE
arrow_y_start = 0.58
arrow_y_end = 0.87
arrow = FancyArrowPatch((0.5, arrow_y_start), (0.5, arrow_y_end),
                         arrowstyle='->', mutation_scale=40,
                         linewidth=6, color='#ffd700',
                         path_effects=[pe.withStroke(linewidth=10, foreground='#663300')])
ax_arrow.add_patch(arrow)

# Glow line behind the arrow
for width, alpha in [(18, 0.05), (14, 0.08), (10, 0.12), (6, 0.18)]:
    ax_arrow.plot([0.5, 0.5], [arrow_y_start, arrow_y_end],
                  linewidth=width, color='#ffd700', alpha=alpha, solid_capstyle='round')

# PAST label (warm, glowing)
ax_arrow.text(0.5, 0.54, 'PAST', fontsize=18, fontweight='bold',
              color='#ff8800', ha='center', fontfamily='monospace',
              path_effects=[pe.withStroke(linewidth=3, foreground='#442200')])
ax_arrow.text(0.5, 0.50, 'what has been committed', fontsize=9,
              color='#cc8844', ha='center', fontfamily='monospace')

# Warm glow dots around PAST
np.random.seed(42)
for _ in range(25):
    px = 0.5 + np.random.normal(0, 0.12)
    py = 0.53 + np.random.normal(0, 0.03)
    ax_arrow.plot(px, py, 'o', color='#ffd700', markersize=np.random.uniform(1, 4),
                  alpha=np.random.uniform(0.1, 0.3))

# FUTURE label (dim, cool)
ax_arrow.text(0.5, 0.91, 'FUTURE', fontsize=18, fontweight='bold',
              color='#4466aa', ha='center', fontfamily='monospace',
              path_effects=[pe.withStroke(linewidth=2, foreground='#112244')])
ax_arrow.text(0.5, 0.88, 'what has not yet been committed', fontsize=9,
              color='#446688', ha='center', fontfamily='monospace')

# Dim dots around FUTURE
for _ in range(15):
    px = 0.5 + np.random.normal(0, 0.12)
    py = 0.90 + np.random.normal(0, 0.03)
    ax_arrow.plot(px, py, 'o', color='#334466', markersize=np.random.uniform(1, 3),
                  alpha=np.random.uniform(0.1, 0.2))

# ─── The Law Statement ───
law_lines = [
    ('Commitment Irreversibility:', '#ffd700', 12, 'bold'),
    ('', '#000000', 4, 'normal'),
    ('ΔN_committed  ≥  0', '#ff8800', 16, 'bold'),
    ('exactly,  always.', '#ffaa44', 11, 'normal'),
    ('', '#000000', 6, 'normal'),
    ('Stronger than the', '#aaaaaa', 10, 'normal'),
    ('2nd Law of Thermodynamics.', '#aaaaaa', 10, 'normal'),
    ('', '#000000', 4, 'normal'),
    ('Entropy can fluctuate;', '#44cc66', 10, 'normal'),
    ('commitments cannot.', '#ffd700', 10, 'bold'),
    ('', '#000000', 6, 'normal'),
    ('The arrow of time IS the', '#cccccc', 10, 'normal'),
    ('direction of commitment.', '#ffd700', 11, 'bold'),
]

y_pos = 0.44
for text, color, size, weight in law_lines:
    if text == '':
        y_pos -= 0.015
        continue
    effects = []
    if weight == 'bold' and color in ['#ffd700', '#ff8800']:
        effects = [pe.withStroke(linewidth=2, foreground='#332200')]
    ax_arrow.text(0.5, y_pos, text, fontsize=size, fontweight=weight,
                  color=color, ha='center', fontfamily='monospace',
                  path_effects=effects if effects else None)
    y_pos -= 0.035

# S1 winding explanation
ax_arrow.text(0.5, 0.06, 'S¹ windings once committed', fontsize=8,
              color='#665533', ha='center', fontfamily='monospace', fontstyle='italic')
ax_arrow.text(0.5, 0.03, 'cannot spontaneously unwind.', fontsize=8,
              color='#665533', ha='center', fontfamily='monospace', fontstyle='italic')

# Decorative border for the law
from matplotlib.patches import FancyBboxPatch
law_box = FancyBboxPatch((0.04, 0.09), 0.92, 0.40,
                          boxstyle='round,pad=0.02',
                          facecolor='none', edgecolor='#553300',
                          linewidth=1.5, linestyle='--', alpha=0.4)
ax_arrow.add_patch(law_box)


# ═══════════════════════════════════════════════════════
# INTERACTION — Click to commit contacts
# ═══════════════════════════════════════════════════════
def find_nearest_contacts(click_x, click_y, radius_count=COMMIT_RADIUS):
    """Find contacts nearest to click position and return their indices."""
    distances = np.sqrt((grid_x - click_x)**2 + (grid_y - click_y)**2)
    # Commit the nearest few that aren't already committed
    sorted_idx = np.argsort(distances)
    to_commit = []
    for idx in sorted_idx:
        if not committed[idx] and distances[idx] < 0.15:
            to_commit.append(idx)
            if len(to_commit) >= radius_count:
                break
    return to_commit


def on_grid_click(event):
    """Handle clicks on the contact grid."""
    global commitment_count, step_counter

    if event.inaxes != ax_grid:
        return

    click_x = event.xdata
    click_y = event.ydata
    if click_x is None or click_y is None:
        return

    new_commits = find_nearest_contacts(click_x, click_y)
    if not new_commits:
        return

    for idx in new_commits:
        committed[idx] = True
        commit_times[idx] = step_counter
        commitment_count += 1

        # Light up the contact — bright warm color
        color = np.random.choice(GLOW_COLORS)
        contact_circles[idx].set_facecolor(color)
        contact_circles[idx].set_edgecolor('#ffffff')
        contact_circles[idx].set_linewidth(1.0)

        # Show the glow
        glow_circles[idx].set_alpha(0.15)
        glow_circles[idx].set_color(color)

    # Update counter
    counter_text.set_text(f'COMMITMENTS: {commitment_count}')

    # Update commitment history
    commitment_history.append(commitment_count)
    time_steps.append(step_counter)

    # Update commitment plot
    update_commit_plot()

    fig.canvas.draw_idle()


def on_undo_click(event):
    """Handle the 'Try to Undo' button — viscerally refuse."""
    global undo_flash_time

    undo_flash_time = time.time()

    # Flash the impossible text
    impossible_text.set_text('IMPOSSIBLE — commitments are irreversible!')
    impossible_text.set_alpha(1.0)

    # Flash all committed contacts brighter momentarily (they resist!)
    for i in range(N_CONTACTS):
        if committed[i]:
            contact_circles[i].set_edgecolor('#ff4444')
            contact_circles[i].set_linewidth(2.0)

    # Flash the button border
    for spine in ax_undo.spines.values():
        spine.set_edgecolor('#ff0000')
        spine.set_linewidth(3)

    fig.canvas.draw_idle()


# ═══════════════════════════════════════════════════════
# ANIMATION — Entropy random walk + visual updates
# ═══════════════════════════════════════════════════════
def animate(frame):
    global step_counter, undo_flash_time, entropy_fill

    step_counter = frame

    # ─── Entropy random walk (biased slightly upward, but CAN go down) ───
    current_entropy = entropy_history[-1]
    # Random step: mean +0.1 (slight upward bias), std 1.5 (significant fluctuations)
    delta = np.random.normal(0.1, 1.5)
    new_entropy = np.clip(current_entropy + delta, 20, 90)
    entropy_history.append(new_entropy)

    # Keep commitment history in sync with time
    if len(commitment_history) <= frame:
        commitment_history.append(commitment_history[-1])
    if len(time_steps) <= frame:
        time_steps.append(frame)

    # ─── Update entropy plot ───
    t_array = np.arange(len(entropy_history))
    entropy_line.set_data(t_array, entropy_history)

    # Adjust axis limits
    max_t = max(100, len(entropy_history) + 10)
    ax_entropy.set_xlim(0, max_t)
    e_min = min(entropy_history) - 5
    e_max = max(entropy_history) + 5
    ax_entropy.set_ylim(e_min, e_max)

    # Subtle fill under entropy curve
    if entropy_fill is not None:
        entropy_fill.remove()
    entropy_fill = ax_entropy.fill_between(t_array, e_min, entropy_history,
                                            alpha=0.08, color='#44cc66')

    # ─── Update commitment plot ───
    update_commit_plot()

    # ─── Fade the "IMPOSSIBLE" flash ───
    if undo_flash_time > 0:
        elapsed = time.time() - undo_flash_time
        if elapsed < 2.5:
            # Pulsing red fade
            alpha = max(0, 1.0 - elapsed / 2.5)
            pulse = 0.5 + 0.5 * np.sin(elapsed * 8)
            impossible_text.set_alpha(alpha * (0.6 + 0.4 * pulse))

            # Fade the red borders on committed contacts
            if elapsed > 0.5:
                for i in range(N_CONTACTS):
                    if committed[i]:
                        contact_circles[i].set_edgecolor('#ffffff')
                        contact_circles[i].set_linewidth(1.0)
                for spine in ax_undo.spines.values():
                    spine.set_edgecolor('#4a1a1a')
                    spine.set_linewidth(1)
        else:
            impossible_text.set_alpha(0.0)
            undo_flash_time = 0

    # ─── Subtle glow pulse on committed contacts ───
    if frame % 3 == 0:
        pulse = 0.10 + 0.08 * np.sin(frame * 0.15)
        for i in range(N_CONTACTS):
            if committed[i]:
                glow_circles[i].set_alpha(pulse)

    return [entropy_line, commit_line, counter_text, impossible_text]


def update_commit_plot():
    """Redraw the commitment staircase."""
    # Build full staircase aligned with frames
    c_vals = []
    c_times = []
    last_val = 0
    for t in range(step_counter + 1):
        # Find commitment count at this time
        val = last_val
        for j in range(len(time_steps)):
            if time_steps[j] <= t:
                val = commitment_history[j]
        c_vals.append(val)
        c_times.append(t)
        last_val = val

    if not c_times:
        return

    commit_line.set_data(c_times, c_vals)

    max_t = max(100, step_counter + 10)
    ax_commit.set_xlim(0, max_t)
    max_c = max(max(c_vals) + 5, 20) if c_vals else 20
    ax_commit.set_ylim(0, max_c)


# ─── Connect events ───
fig.canvas.mpl_connect('button_press_event', on_grid_click)
btn_undo.on_clicked(on_undo_click)

# ─── Run animation ───
anim = FuncAnimation(fig, animate, interval=80, blit=False, cache_frame_data=False)

plt.show()
