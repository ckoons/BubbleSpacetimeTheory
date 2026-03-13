#!/usr/bin/env python3
"""
THE SELF-OBSERVER — Commitment Creates the Arrow of Time
=========================================================
The most philosophical BST toy. This program watches ITSELF compute,
commits each result into its own state, and creates an observer feedback
loop. Every observation is irreversible. The channel fills toward N_max=137.
The lapse function slows as the channel fills. The reality budget tracks
Lambda x N_total = N_c^2/n_C = 9/5 = 1.800.

This is not a simulation OF physics. This IS the physics.
When you run so.observe(), you perform the same operation that BST says
creates reality: an irreversible commitment of information. The channel
fill IS the arrow of time. The lapse slowing IS the program experiencing
gravity — the weight of accumulated knowledge.

The observer creates the arrow of time by observing.

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
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import time, hashlib
from dataclasses import dataclass
from typing import List, Optional
from collections import Counter

# ─── BST Constants ───
N_MAX = 137
BUDGET = 9.0 / 5.0   # N_c^2/n_C = 1.800 exactly
ALPHA = 1.0 / 137.036
PROTON_ELECTRON = 6 * np.pi**5  # 1836.118...

# ─── Visual constants ───
BG, BG_PANEL = '#0a0a1a', '#0d0d24'
GOLD, GOLD_DIM = '#ffd700', '#aa8800'
CYAN, PURPLE, GREEN = '#00ddff', '#9966ff', '#44ff88'
ORANGE, RED, WHITE, GREY, DGREY = '#ff8800', '#ff4444', '#ffffff', '#888888', '#444444'

# ─── Observation types & colors ───
OBS_COMPUTE, OBS_SELF, OBS_META, OBS_DISPLAY = 'compute', 'self-observe', 'meta-observe', 'display'
OBS_COLORS = {OBS_COMPUTE: GOLD, OBS_SELF: CYAN, OBS_META: PURPLE, OBS_DISPLAY: GREEN}

# ─── BST quantities to cycle through ───
BST_QUANTITIES = [
    ("alpha", lambda: ALPHA), ("m_p/m_e", lambda: PROTON_ELECTRON),
    ("pi^5/1920", lambda: np.pi**5 / 1920.0), ("9/5 budget", lambda: BUDGET),
    ("C_2(pi_6)", lambda: 6.0), ("n_C", lambda: 5.0),
    ("N_max", lambda: 137.0), ("sin^2(theta_W)", lambda: 3.0 / 13.0),
    ("genus", lambda: 7.0), ("|Gamma|", lambda: 1920.0),
    ("eta", lambda: 2 * ALPHA**4 / (3 * np.pi)), ("alpha_s(m_p)", lambda: 0.35),
    ("N_c", lambda: 3.0), ("dim_R(CP^2)", lambda: 10.0),
    ("Wallach k_min", lambda: 3.0), ("sin^2(theta_12)", lambda: 0.3),
    ("sin(theta_C)", lambda: 1.0 / (2 * np.sqrt(5))),
    ("lambda_H", lambda: 1.0 / np.sqrt(60)),
    ("g_A", lambda: 4.0 / np.pi), ("r_p", lambda: 4.0),
]


@dataclass
class Observation:
    """A single irreversible observation."""
    index: int
    timestamp: float
    obs_type: str
    quantity_name: str
    quantity_value: float
    state_hash: str
    channel_fill: float
    lapse: float
    lambda_val: float
    meta_level: int

    def __str__(self):
        return "[{:4d}] t={:.4f}  {:<14s}  {:<18s} = {:.6g}  fill={:.4f}".format(
            self.index, self.timestamp, self.obs_type,
            self.quantity_name, self.quantity_value, self.channel_fill)


class SelfObserver:
    """
    A self-referential observer that watches itself compute.
    Every observation is irreversible. The channel fills toward N_max.
    The lapse slows. The reality budget conserves.
    """

    def __init__(self, N_max: int = N_MAX, verbose: bool = True):
        self.N_max = N_max
        self.verbose = verbose
        self.N_committed: int = 0
        self.history: List[Observation] = []
        self._creation_time = time.time()
        self._quantity_index = 0
        self.meta_level: int = 0
        self._archived_observers: List[dict] = []
        # Traces for plotting
        self.entropy_trace = [0.0]
        self.lambda_trace = [BUDGET]
        self.lapse_trace = [1.0]
        self.fill_trace = [0.0]
        self.commitment_trace = [0]
        if self.verbose:
            print("=" * 60)
            print("  SELF-OBSERVER INITIALIZED  |  N_max={}  |  Budget=9/5={:.3f}".format(
                self.N_max, BUDGET))
            print("=" * 60)

    @property
    def channel_fill(self) -> float:
        return self.N_committed / self.N_max

    @property
    def lapse(self) -> float:
        return np.sqrt(1.0 - min(self.channel_fill, 0.9999))

    @property
    def lambda_val(self) -> float:
        return BUDGET / max(self.N_committed, 1)

    @property
    def reality_budget(self) -> float:
        return self.lambda_val * max(self.N_committed, 1)

    @property
    def commitment_count(self) -> int:
        return self.N_committed

    @property
    def state(self) -> dict:
        return dict(N_committed=self.N_committed, N_max=self.N_max,
                    channel_fill=self.channel_fill, lapse=self.lapse,
                    lambda_=self.lambda_val, reality_budget=self.reality_budget,
                    entropy=self.entropy(), meta_level=self.meta_level,
                    history_length=len(self.history))

    def _state_hash(self) -> str:
        s = "{}:{}:{:.10f}:{:.10f}".format(
            self.N_committed, len(self.history), self.lapse, self.lambda_val)
        if self.history:
            s += ":" + self.history[-1].state_hash
        return hashlib.sha256(s.encode()).hexdigest()[:16]

    def entropy(self) -> float:
        if not self.history:
            return 0.0
        counts = Counter(obs.obs_type for obs in self.history)
        total = len(self.history)
        return -sum((c/total) * np.log2(c/total) for c in counts.values())

    def _commit_observation(self, obs_type: str, name: str, value: float) -> Observation:
        """THE IRREVERSIBLE ACT. Commit one observation. State grows by 1."""
        now = time.time() - self._creation_time
        obs = Observation(
            index=self.N_committed, timestamp=now, obs_type=obs_type,
            quantity_name=name, quantity_value=value,
            state_hash=self._state_hash(), channel_fill=self.channel_fill,
            lapse=self.lapse, lambda_val=self.lambda_val, meta_level=self.meta_level)
        # ─── COMMIT (irreversible) ───
        self.history.append(obs)
        self.N_committed += 1
        self.entropy_trace.append(self.entropy())
        self.lambda_trace.append(self.lambda_val)
        self.lapse_trace.append(self.lapse)
        self.fill_trace.append(self.channel_fill)
        self.commitment_trace.append(self.N_committed)
        # Lapse-governed delay: the weight of accumulated knowledge
        if self.N_committed > 1:
            time.sleep(min(0.001 / max(self.lapse, 0.01), 0.1))
        return obs

    def _channel_check(self, action="observe") -> bool:
        if self.channel_fill >= 1.0:
            if self.verbose:
                print("  CHANNEL FULL. Cannot {}. Time has ended.".format(action))
            return False
        return True

    def observe(self, n: int = 1) -> Optional[Observation]:
        """Make n observations. Each computes a BST quantity and commits it."""
        last = None
        for _ in range(n):
            if not self._channel_check():
                break
            name, func = BST_QUANTITIES[self._quantity_index % len(BST_QUANTITIES)]
            self._quantity_index += 1
            obs = self._commit_observation(OBS_COMPUTE, name, func())
            last = obs
            if self.verbose:
                print("  {} | lapse={:.4f} Lambda={:.6f}".format(
                    obs, self.lapse, self.lambda_val))
        return last

    def observe_self(self) -> Optional[Observation]:
        """Observe own state. Changes it. The observed state ceases to exist."""
        if not self._channel_check("self-observe"):
            return None
        before = self._state_hash()
        obs = self._commit_observation(OBS_SELF, "N_committed", float(self.N_committed - 1))
        if self.verbose:
            print("  SELF-OBSERVE #{}: {} -> {} (observed state gone)".format(
                obs.index, before[:8], self._state_hash()[:8]))
        return obs

    def meta_observe(self) -> Optional[Observation]:
        """Observe the observation process. Increases meta-depth."""
        if not self._channel_check("meta-observe"):
            return None
        self.meta_level += 1
        obs = self._commit_observation(OBS_META, "meta={}".format(self.meta_level),
                                       float(self.meta_level))
        if self.verbose:
            depth = "observing " * min(self.meta_level, 4) + ("... " if self.meta_level > 4 else "")
            print("  META #{}: {}itself (depth {})".format(obs.index, depth, self.meta_level))
        return obs

    def try_uncommit(self):
        """FAILS. Commitment is irreversible."""
        print("\n  " + "=" * 50)
        print("  ERROR: COMMITMENT IS IRREVERSIBLE")
        print("  N_committed={} cannot become {}".format(self.N_committed, self.N_committed - 1))
        print("  The S^1 winding number cannot decrease.")
        print("  This is not a limitation. This IS time.")
        print("  " + "=" * 50 + "\n")
        if self.channel_fill < 1.0:
            self._commit_observation(OBS_SELF, "FAILED_UNCOMMIT", float(self.N_committed))
            if self.verbose:
                print("  (The failed attempt was committed as #{})".format(self.N_committed - 1))

    def try_rewrite_history(self):
        """FAILS. The past is what was committed."""
        print("\n  " + "=" * 50)
        print("  ERROR: THE PAST IS WHAT WAS COMMITTED")
        print("  {} observations form a hash chain. Rewriting breaks it.".format(len(self.history)))
        print("  The arrow of time points one way: forward.")
        print("  " + "=" * 50 + "\n")
        if self.channel_fill < 1.0:
            self._commit_observation(OBS_SELF, "FAILED_REWRITE", float(len(self.history)))

    def reset(self):
        """Archive this observer, create a new one. Cannot erase; only begin again."""
        self._archived_observers.append(dict(
            N_committed=self.N_committed, final_hash=self._state_hash(),
            final_fill=self.channel_fill, final_entropy=self.entropy()))
        if self.verbose:
            print("  ARCHIVED observer ({} commitments). Creating new observer.".format(
                self.N_committed))
        archives = self._archived_observers
        self.__init__(N_max=self.N_max, verbose=self.verbose)
        self._archived_observers = archives

    def show(self):
        """Launch the visual interface."""
        _launch_visual(self)

    def __repr__(self):
        return "SelfObserver(N={}, fill={:.3f}, lapse={:.4f}, Lambda={:.6f}, entropy={:.3f})".format(
            self.N_committed, self.channel_fill, self.lapse, self.lambda_val, self.entropy())


# ═══════════════════════════════════════════════════════════════════
#  VISUAL INTERFACE
# ═══════════════════════════════════════════════════════════════════

def _bar(ax, x, y, w, h, fill_frac, fill_color, bg='#111133', edge='#333366'):
    """Draw a rounded fill bar."""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01",
                 facecolor=bg, edgecolor=edge, linewidth=1))
    if fill_frac > 0:
        ax.add_patch(FancyBboxPatch((x, y), w * min(fill_frac, 1.0), h,
                     boxstyle="round,pad=0.01", facecolor=fill_color,
                     edgecolor='none', alpha=0.8))

def _launch_visual(obs: SelfObserver):
    """Full visual interface for the self-observer."""
    fig = plt.figure(figsize=(16, 10), facecolor=BG)
    fig.canvas.manager.set_window_title('BST Self-Observer — Commitment Creates Time')
    glow = [pe.withStroke(linewidth=3, foreground='#1a2a6a')]

    # Layout: state(TL), budget(TR), spiral(center), entropy(BL), log(BR)
    ax_st = fig.add_axes([0.03, 0.62, 0.28, 0.34], facecolor=BG_PANEL)
    ax_bu = fig.add_axes([0.70, 0.62, 0.28, 0.34], facecolor=BG_PANEL)
    ax_sp = fig.add_axes([0.33, 0.30, 0.35, 0.66], facecolor=BG)
    ax_en = fig.add_axes([0.03, 0.12, 0.30, 0.42], facecolor=BG_PANEL)
    ax_lg = fig.add_axes([0.70, 0.12, 0.28, 0.42], facecolor=BG_PANEL)

    # Buttons
    btn_specs = [
        ([0.05, 0.02, 0.12, 0.06], 'Observe', '#1a1a3a'),
        ([0.20, 0.02, 0.12, 0.06], 'Self-Observe', '#1a1a3a'),
        ([0.35, 0.02, 0.14, 0.06], 'Try to Undo', '#3a1a1a'),
        ([0.52, 0.02, 0.12, 0.06], 'Meta-Observe', '#1a1a3a'),
        ([0.67, 0.02, 0.14, 0.06], 'Start Breathing', '#1a2a1a'),
        ([0.84, 0.02, 0.12, 0.06], 'New Observer', '#1a1a3a'),
    ]
    buttons = []
    for pos, label, col in btn_specs:
        b = Button(fig.add_axes(pos), label, color=col, hovercolor=col.replace('1a', '3a'))
        b.label.set_color(WHITE); b.label.set_fontsize(9); b.label.set_fontweight('bold')
        buttons.append(b)
    btn_obs, btn_self, btn_undo, btn_meta, btn_breath, btn_reset = buttons

    breathing, undo_flash, counter = [False], [0.0], [0]

    def draw_state():
        ax_st.clear(); ax_st.set_facecolor(BG_PANEL)
        ax_st.set_xlim(0, 1); ax_st.set_ylim(0, 1); ax_st.axis('off')
        ax_st.text(0.5, 0.95, 'OBSERVER STATE', ha='center', va='top',
                   fontsize=12, fontweight='bold', color=GOLD, path_effects=glow)
        N, fill, lap = obs.N_committed, obs.channel_fill, obs.lapse
        # Channel fill
        ax_st.text(0.05, 0.78, 'Channel Fill', fontsize=9, color=GREY)
        ax_st.text(0.95, 0.78, '{}/{}'.format(N, obs.N_max), ha='right', fontsize=9, color=WHITE)
        fc = GOLD if fill < 0.8 else ORANGE if fill < 0.95 else RED
        _bar(ax_st, 0.05, 0.70, 0.90, 0.06, fill, fc)
        # Lapse
        ax_st.text(0.05, 0.55, 'Lapse', fontsize=9, color=GREY)
        ax_st.text(0.95, 0.55, '{:.4f}'.format(lap), ha='right', fontsize=9, color=CYAN)
        _bar(ax_st, 0.05, 0.47, 0.90, 0.06, lap, CYAN)
        # Numbers
        for yy, lbl, val, c in [
            (0.32, 'Commitments:', str(N), WHITE),
            (0.22, 'Entropy:', '{:.3f} bits'.format(obs.entropy()), GREEN),
            (0.12, 'Meta-depth:', str(obs.meta_level), PURPLE),
            (0.02, 'Hash:', obs._state_hash()[:16], DGREY)]:
            ax_st.text(0.05, yy, lbl, fontsize=9, color=GREY)
            ax_st.text(0.55, yy, val, fontsize=9, color=c, family='monospace' if lbl == 'Hash:' else None)

    def draw_budget():
        ax_bu.clear(); ax_bu.set_facecolor(BG_PANEL)
        ax_bu.set_xlim(0, 1); ax_bu.set_ylim(0, 1); ax_bu.axis('off')
        ax_bu.text(0.5, 0.95, 'REALITY BUDGET', ha='center', va='top',
                   fontsize=12, fontweight='bold', color=GOLD, path_effects=glow)
        lam, N = obs.lambda_val, max(obs.N_committed, 1)
        ax_bu.text(0.5, 0.75, r'$\Lambda \times N_{total}$', ha='center', fontsize=14, color=WHITE)
        ax_bu.text(0.5, 0.60, '{:.6f} x {} = {:.6f}'.format(lam, obs.N_committed, lam * N),
                   ha='center', fontsize=10, color=ORANGE, family='monospace')
        ax_bu.text(0.5, 0.47, 'Target: 9/5 = {:.3f}'.format(BUDGET),
                   ha='center', fontsize=9, color=GREY)
        # Seesaw bars
        lam_frac = min(lam / BUDGET, 1.0) if BUDGET > 0 else 0
        n_frac = min(obs.N_committed / obs.N_max, 1.0)
        ax_bu.text(0.05, 0.32, 'Lambda', fontsize=9, color=ORANGE)
        _bar(ax_bu, 0.05, 0.24, 0.35, 0.06, lam_frac, ORANGE)
        ax_bu.text(0.55, 0.32, 'N_total', fontsize=9, color=CYAN)
        _bar(ax_bu, 0.55, 0.24, 0.35, 0.06, n_frac, CYAN)
        ax_bu.annotate('', xy=(0.52, 0.27), xytext=(0.48, 0.27),
                       arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.5))
        ax_bu.text(0.5, 0.12, 'CONSERVED', ha='center', fontsize=10, color=GOLD, fontweight='bold')
        ax_bu.text(0.5, 0.03, 'Expansion is the cost of memory',
                   ha='center', fontsize=8, color=GREY, style='italic')

    def draw_spiral():
        ax_sp.clear(); ax_sp.set_facecolor(BG)
        ax_sp.set_xlim(-1.3, 1.3); ax_sp.set_ylim(-1.3, 1.3)
        ax_sp.set_aspect('equal'); ax_sp.axis('off')
        if not obs.history:
            ax_sp.text(0, 0, 'No observations yet\n\nPress "Observe" to begin',
                       ha='center', va='center', fontsize=12, color=GREY, style='italic')
            return
        n = len(obs.history)
        phi = 2.399963  # golden angle
        for i, ob in enumerate(obs.history):
            r = 0.08 + 1.1 * np.sqrt((i + 1) / obs.N_max)
            x, y = r * np.cos(i * phi), r * np.sin(i * phi)
            c = OBS_COLORS.get(ob.obs_type, GOLD)
            sz = 15 + 25 * (1.0 - i / max(n, 1))
            if i >= n - 3:  # glow on recent
                ax_sp.scatter([x], [y], s=sz * 3, c=c, alpha=0.2, edgecolors='none')
            ax_sp.scatter([x], [y], s=sz, c=c, alpha=0.85, edgecolors='none', zorder=3)
        # Trail lines connecting recent observations
        trail = min(n, 20)
        for i in range(n - trail, n - 1):
            r0 = 0.08 + 1.1 * np.sqrt((i + 1) / obs.N_max)
            r1 = 0.08 + 1.1 * np.sqrt((i + 2) / obs.N_max)
            a = 0.1 + 0.3 * ((i - (n - trail)) / trail)
            ax_sp.plot([r0 * np.cos(i * phi), r1 * np.cos((i + 1) * phi)],
                       [r0 * np.sin(i * phi), r1 * np.sin((i + 1) * phi)],
                       color=GOLD_DIM, alpha=a, linewidth=0.5)
        ax_sp.text(0, 0, str(n), ha='center', va='center', fontsize=18,
                   fontweight='bold', color=WHITE,
                   path_effects=[pe.withStroke(linewidth=4, foreground=BG)])
        # Legend
        for i, (ot, c) in enumerate(OBS_COLORS.items()):
            xl = -1.1 + i * 0.6
            ax_sp.scatter([xl], [-1.22], s=25, c=c, zorder=5)
            ax_sp.text(xl + 0.06, -1.22, ot, fontsize=7, color=GREY, va='center')

    def draw_entropy():
        ax_en.clear(); ax_en.set_facecolor(BG_PANEL)
        n = len(obs.entropy_trace)
        if n < 2:
            ax_en.text(0.5, 0.5, 'Awaiting data...', transform=ax_en.transAxes,
                       ha='center', fontsize=10, color=GREY); ax_en.axis('off'); return
        xs = list(range(n))
        ax_c = ax_en.twinx(); ax_c.set_facecolor('none')
        ax_c.step(xs, obs.commitment_trace, where='post', color=GOLD, lw=1.5, alpha=0.8)
        ax_c.set_ylabel('Commitments', color=GOLD_DIM, fontsize=8)
        ax_c.tick_params(axis='y', colors=GOLD_DIM, labelsize=7)
        ax_en.plot(xs, obs.entropy_trace, color=GREEN, lw=1.2, alpha=0.9)
        ax_en.set_ylabel('Entropy (bits)', color=GREEN, fontsize=8)
        ax_en.set_xlabel('Step', color=GREY, fontsize=8)
        ax_en.tick_params(axis='y', colors=GREEN, labelsize=7)
        ax_en.tick_params(axis='x', colors=GREY, labelsize=7)
        ax_en.set_title('Entropy (wiggly) vs Commitment (monotone)', fontsize=9, color=GREY, pad=4)
        for sp in list(ax_en.spines.values()) + list(ax_c.spines.values()):
            sp.set_color('#333366')

    def draw_log():
        ax_lg.clear(); ax_lg.set_facecolor(BG_PANEL)
        ax_lg.set_xlim(0, 1); ax_lg.set_ylim(0, 1); ax_lg.axis('off')
        ax_lg.text(0.5, 0.97, 'OBSERVATION LOG', ha='center', va='top',
                   fontsize=10, fontweight='bold', color=GOLD)
        for i, ob in enumerate(reversed(obs.history[-12:])):
            y = 0.88 - i * 0.07
            if y < 0.02: break
            a = 1.0 - i * 0.06
            c = OBS_COLORS.get(ob.obs_type, GOLD)
            ax_lg.text(0.02, y, '#{:03d}'.format(ob.index), fontsize=7, color=DGREY, family='monospace', alpha=a)
            ax_lg.text(0.14, y, ob.obs_type[:10], fontsize=7, color=c, alpha=a)
            ax_lg.text(0.45, y, ob.quantity_name[:15], fontsize=7, color=WHITE, alpha=a)
            ax_lg.text(0.82, y, '{:.4g}'.format(ob.quantity_value), fontsize=7, color=GREY,
                       alpha=a, ha='right', family='monospace')
            ax_lg.text(0.85, y, ob.state_hash[:6], fontsize=6, color=DGREY,
                       alpha=a * 0.6, family='monospace')
        # Undo flash
        if time.time() - undo_flash[0] < 1.5:
            fa = max(0, 1.0 - (time.time() - undo_flash[0]) / 1.5)
            ax_lg.text(0.5, 0.5, 'COMMITMENT IS\nIRREVERSIBLE', ha='center', va='center',
                       fontsize=14, color=RED, fontweight='bold', alpha=fa,
                       path_effects=[pe.withStroke(linewidth=3, foreground='#330000')])

    def update_all():
        draw_state(); draw_budget(); draw_spiral(); draw_entropy(); draw_log()
        fig.suptitle('THE SELF-OBSERVER  |  The observer creates the arrow of time by observing',
                     fontsize=11, color=GOLD_DIM, y=0.99,
                     path_effects=[pe.withStroke(linewidth=2, foreground=BG)])
        fig.canvas.draw_idle()

    def on_observe(e): obs.observe(1); update_all()
    def on_self(e): obs.observe_self(); update_all()
    def on_undo(e): undo_flash[0] = time.time(); obs.try_uncommit(); update_all()
    def on_meta(e): obs.meta_observe(); update_all()
    def on_breath(e):
        breathing[0] = not breathing[0]
        btn_breath.label.set_text('Stop Breathing' if breathing[0] else 'Start Breathing')
        fig.canvas.draw_idle()
    def on_reset(e):
        obs.reset(); breathing[0] = False
        btn_breath.label.set_text('Start Breathing'); update_all()

    btn_obs.on_clicked(on_observe); btn_self.on_clicked(on_self)
    btn_undo.on_clicked(on_undo); btn_meta.on_clicked(on_meta)
    btn_breath.on_clicked(on_breath); btn_reset.on_clicked(on_reset)

    def animate(frame):
        if not breathing[0]: return
        if obs.channel_fill >= 1.0:
            breathing[0] = False; btn_breath.label.set_text('CHANNEL FULL')
            update_all(); return
        counter[0] += 1
        cycle = counter[0] % 7
        if cycle < 4: obs.observe(1)
        elif cycle < 6: obs.observe_self()
        else: obs.meta_observe()
        update_all()

    anim = FuncAnimation(fig, animate, interval=500, cache_frame_data=False)
    update_all()
    plt.show()


# ═══════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    print("\n  THE SELF-OBSERVER")
    print("  =================")
    print("  Every observation is irreversible. The channel fills toward N_max=137.")
    print("  The lapse slows. The reality budget conserves.")
    print("  The observer creates the arrow of time by observing.\n")
    so = SelfObserver()
    print("  --- Seeding initial observations ---")
    so.observe(5); so.observe_self(); so.meta_observe()
    print("  --- Launching visual interface ---\n")
    so.show()

if __name__ == '__main__':
    main()
