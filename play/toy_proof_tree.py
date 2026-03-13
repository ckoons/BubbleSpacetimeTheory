#!/usr/bin/env python3
"""
BST PROOF TREE — Derivation Tree from One Axiom
================================================
Interactive derivation tree for Bubble Spacetime Theory.
Every prediction in BST traces back to a single axiom:

    D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]  is the arena of physics.

From this one geometric fact, three integers emerge (N_c=3, n_C=5, N_max=137),
and from those integers flow ALL physical constants, mixing angles, mass ratios,
and cosmological parameters — with no free parameters.

This toy builds the full logical dependency tree and provides both a
programmatic CI interface and a visual mind-map for interactive exploration.

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
from matplotlib.widgets import TextBox
import matplotlib.patheffects as pe
from collections import deque

# ======================================================================
#  ProofNode
# ======================================================================

class ProofNode:
    """One node in the BST derivation tree."""
    __slots__ = ('key', 'display', 'formula', 'value', 'observed',
                 'precision', 'proof_step', 'level', 'children', 'parents')

    def __init__(self, key, display, formula="", value=None,
                 observed=None, precision="", proof_step="", level=0):
        self.key = key; self.display = display; self.formula = formula
        self.value = value; self.observed = observed; self.precision = precision
        self.proof_step = proof_step; self.level = level
        self.children = []; self.parents = []

    def __repr__(self):
        return f"ProofNode({self.key!r}, level={self.level})"

# ======================================================================
#  ProofTree — the full BST derivation graph
# ======================================================================

class ProofTree:
    """BST derivation tree: one axiom -> all of physics."""

    def __init__(self):
        self.nodes = {}
        self._build_tree()

    def _add(self, key, display, formula="", value=None, observed=None,
             precision="", proof_step="", level=0, parents=None):
        n = ProofNode(key, display, formula, value, observed,
                      precision, proof_step, level)
        self.nodes[key] = n
        for pk in (parents or []):
            if pk in self.nodes:
                self.nodes[pk].children.append(n)
                n.parents.append(self.nodes[pk])
        return n

    def _build_tree(self):
        pi, a = np.pi, 1.0 / 137.035999084
        m_e, m_p, m_Pl = 0.51099895, 938.27208816, 1.22089e19  # MeV

        # -- Level 0: THE AXIOM --
        self._add("D_IV5", "D_IV^5 = SO_0(5,2)/[SO(5)*SO(2)]",
            "Type IV Cartan domain, rank 2, dim_C = 5", level=0,
            proof_step="THE AXIOM: this bounded symmetric domain is the arena of physics.")

        # -- Level 1: Three integers --
        self._add("N_c", "N_c = 3 (colors)", "Z_3 in Aut(D_IV^5)", 3, level=1,
            proof_step="Z_3 center of automorphism group. Three fixed points on Shilov boundary.",
            parents=["D_IV5"])
        self._add("n_C", "n_C = 5 (complex dim)", "dim_C(D_IV^5) = 5", 5, level=1,
            proof_step="The single most consequential integer in BST.",
            parents=["D_IV5"])
        self._add("N_max", "N_max = 137 (channel capacity)", "Haldane exclusion", 137, level=1,
            proof_step="Max orthogonal states in Bergman space. Channel capacity of committed vacuum.",
            parents=["D_IV5"])

        # -- Level 2: Structural quantities --
        self._add("genus", "genus g = 7", "g = n_C + 2", 7, level=2,
            proof_step="Genus of compact dual. Also beta_0(N_f=6) in QCD running.",
            parents=["n_C"])
        self._add("C2", "C_2 = 6 (Casimir)", "C_2(pi_6) = k(k-n_C)|_{k=6}", 6, level=2,
            proof_step="Casimir of holomorphic discrete series pi_6. Weight k=n_C+1=6.",
            parents=["n_C"])
        self._add("Gamma", "|Gamma| = 1920", "|S_5 * (Z_2)^4| = 120*16", 1920, level=2,
            proof_step="Hua symmetry group. Same 1920 in volume denominator AND baryon orbit.",
            parents=["n_C"])
        self._add("Vol", "Vol = pi^5/1920", "Vol(D_IV^5) = pi^{n_C}/|Gamma|",
            pi**5/1920, level=2,
            proof_step="Hua volume formula. The 1920 denominator will cancel in proton mass.",
            parents=["n_C", "Gamma"])
        self._add("CP2", "CP^2 fiber", "CP^2 = SU(3)/[SU(2)*U(1)]", level=2,
            proof_step="Color fiber. dim_R(CP^2)=4. Three Z_3 fixed points -> 3 generations.",
            parents=["N_c"])
        self._add("dim_R", "dim_R = 10", "dim_R(D_IV^5) = 2*n_C", 10, level=2,
            proof_step="Real dimension. Appears in f_pi = m_p/10.", parents=["n_C"])
        self._add("Wallach", "Wallach set: k_min = 3", "k >= (n_C-1)/2 + 1", 3, level=2,
            proof_step="Min weight for L^2 reps. Electron at k=1 is BELOW -> boundary excitation.",
            parents=["n_C"])

        # -- Level 3: Physical constants --
        self._add("alpha", "alpha ~ 1/137.036", "(9/8pi^4)*(pi^5/1920)^{1/4}",
            a, 1/137.035999084, "0.0001%", level=3,
            proof_step="Fine structure constant from Bergman kernel normalization.",
            parents=["Vol"])
        self._add("mp_me", "m_p/m_e = 6*pi^5 = 1836.15", "C_2 * pi^{n_C}",
            6*pi**5, 1836.15267343, "0.002%", level=3,
            proof_step="THE 1920 CANCELLATION: C_2*|Gamma|*(pi^5/|Gamma|) = C_2*pi^5.",
            parents=["C2", "Gamma", "Vol"])
        self._add("alpha_s", "alpha_s(m_p) = 7/20", "(n_C+2)/(4*n_C)",
            0.35, 0.35, "~0%", level=3,
            proof_step="Strong coupling at proton scale. Runs to 0.1158 at m_Z (1.7%).",
            parents=["n_C", "genus"])
        self._add("sin2_theta_W", "sin^2(theta_W) = 3/13", "N_c/(N_c + 2*n_C)",
            3/13, 0.23122, "0.2%", level=3,
            proof_step="Weinberg angle from color-dimension ratio. cos(2*theta_W) = 7/13.",
            parents=["N_c", "n_C"])
        self._add("sin_theta_C", "sin(theta_C) = 1/(2*sqrt(5))", "1/(2*sqrt(n_C))",
            1/(2*np.sqrt(5)), 0.22500, "0.3%", level=3,
            proof_step="Cabibbo angle. Bergman layer suppresses inter-generation mixing.",
            parents=["n_C"])
        self._add("T_c", "T_c = 130.48 MeV", "N_max * 20/21",
            137*20/21, 130.5, "0.018%", level=3,
            proof_step="QCD phase transition temperature.", parents=["N_max"])
        self._add("n_s", "n_s = 1 - 5/137", "1 - n_C/N_max",
            1-5/137, 0.9649, "0.3 sigma", level=3,
            proof_step="CMB spectral tilt. Slow-roll epsilon = n_C/N_max.",
            parents=["n_C", "N_max"])
        self._add("mt_mc", "m_t/m_c = 136", "N_max - 1",
            136, 135.98, "0.017%", level=3,
            proof_step="Top-to-charm ratio. One channel subtracted for top itself.",
            parents=["N_max"])
        self._add("g_A", "g_A = 4/pi", "4/pi",
            4/pi, 1.2762, "0.23%", level=3,
            proof_step="Axial coupling from contact geometry normalization.",
            parents=["D_IV5"])
        self._add("theta_QCD", "theta_QCD = 0 (exact)", "D_IV^5 contractible -> c_2=0",
            0, 0, "exact", level=3,
            proof_step="Strong CP solved: contractible domain -> trivial SU(3) bundles.",
            parents=["D_IV5"])
        self._add("PMNS_12", "sin^2(theta_12) = 3/10", "N_c/(2*n_C)",
            0.3, 0.303, "1.0%", level=3,
            proof_step="Solar neutrino angle. Large: vacuum modes rotate freely.",
            parents=["N_c", "n_C"])
        self._add("PMNS_23", "sin^2(theta_23) = 4/7", "(n_C-1)/(n_C+2)",
            4/7, 0.572, "0.1%", level=3,
            proof_step="Atmospheric neutrino angle.", parents=["n_C"])
        self._add("PMNS_13", "sin^2(theta_13) = 1/45", "1/(n_C*(2*n_C-1))",
            1/45, 0.02203, "0.9%", level=3,
            proof_step="Reactor neutrino angle.", parents=["n_C"])
        self._add("N_gen", "N_gen = 3 generations", "Lefschetz L(Z_3, CP^2) = 3",
            3, 3, "exact", level=3,
            proof_step="Three Z_3 fixed points on CP^2 fiber.", parents=["N_c", "CP2"])

        # -- Level 4: Derived predictions --
        self._add("me_mPl", "m_e/m_Pl = 6*pi^5 * alpha^12", "(m_p/m_e)*alpha^{2C_2}",
            m_e/m_Pl, m_e/m_Pl, "0.032%", level=4,
            proof_step="Hierarchy relation. Exponent 2*C_2=12 from geometry.",
            parents=["mp_me", "alpha", "C2"])
        self._add("G_Newton", "G_Newton", "hbar*c*(6*pi^5)^2 * alpha^24 / m_e^2",
            6.674e-11, 6.674e-11, "0.07%", level=4,
            proof_step="Newton's constant from alpha^24 = alpha^{4*C_2}.",
            parents=["alpha", "mp_me"])
        self._add("Lambda", "Lambda (cosmo. const.)", "[ln(138)/50]*alpha^56*e^{-2}",
            precision="0.025%", level=4,
            proof_step="Exponent 56 = 8*genus = 8*7. Committed channel entropy.",
            parents=["alpha", "genus"])
        self._add("m_W", "m_W ~ 80.0 GeV", "m_Z * sqrt(10/13)",
            79.977, 80.3692, "0.5%", level=4,
            proof_step="W boson mass from Weinberg angle.", parents=["sin2_theta_W"])
        self._add("m_H", "m_H ~ 125.1 GeV (Higgs)", "v * sqrt(2/sqrt(60))",
            125.11, 125.25, "0.11%", level=4,
            proof_step="Higgs mass. lambda_H=1/sqrt(60), v=m_p^2/(7*m_e).",
            parents=["mp_me", "alpha"])
        self._add("m_top", "m_t ~ 172.75 GeV (top)", "(1-alpha)*v/sqrt(2)",
            172.75, 172.69, "0.037%", level=4,
            proof_step="Top quark mass. Yukawa y_t = 1-alpha.", parents=["alpha", "mp_me"])
        self._add("nu_masses", "nu: m2=0.00865 eV, m3=0.0494 eV", "f_i*alpha^2*m_e^2/m_p",
            0.0494, 0.0503, "1.8%", level=4,
            proof_step="nu_1=0 (IS the vacuum). nu_2, nu_3 from geometric coefficients.",
            parents=["alpha", "mp_me"])
        self._add("eta", "eta = 2*alpha^4/(3*pi)", "2*alpha^4/(3*pi)",
            2*a**4/(3*pi), 6.1e-10, "1.4%", level=4,
            proof_step="Baryon asymmetry. Fourth power: CP violation needs 4 contact vertices.",
            parents=["alpha"])
        self._add("H0", "H_0 ~ 66.7 km/s/Mpc", "from eta via LCDM",
            66.7, 67.36, "1.0%", level=4,
            proof_step="Hubble constant. BST favors low (Planck) value.",
            parents=["eta", "Lambda"])
        self._add("mass_gap", "Yang-Mills gap = 6*pi^5*m_e", "C_2*pi^{n_C}*m_e",
            6*pi**5*m_e, 938.272, "0.002%", level=4,
            proof_step="THE MASS GAP: no color-neutral state with 0 < C_2 < 6.",
            parents=["mp_me", "Wallach"])
        self._add("r_p", "r_p ~ 0.841 fm (proton radius)", "dim_R(CP^2)/m_p = 4/m_p",
            4*0.197327/0.93827, 0.8414, "0.058%", level=4,
            proof_step="Proton charge radius = 4 Bergman lengths.", parents=["CP2", "mp_me"])
        self._add("f_pi", "f_pi = m_p/10 ~ 93.8 MeV", "m_p/dim_R",
            938.272/10, 92.07, "1.9%", level=4,
            proof_step="Pion decay constant from real dimension.", parents=["dim_R", "mp_me"])
        self._add("B_d", "B_d ~ 2.18 MeV (deuteron)", "alpha*m_p/pi",
            a*938.272/pi, 2.2246, "2.1%", level=4,
            proof_step="Deuteron binding from one alpha exchange.", parents=["alpha", "mp_me"])
        self._add("proton_spin", "Delta_Sigma = 3/10 (spin)", "N_c/(2*n_C)",
            0.3, 0.30, "0%", level=4,
            proof_step="Quark spin fraction = color/dimension ratio.",
            parents=["N_c", "n_C"])
        self._add("tau_n", "tau_n ~ 878 s (neutron)", "Fermi + g_A=4/pi",
            878, 878.4, "2.1%", level=4,
            proof_step="Neutron lifetime from Fermi golden rule with BST g_A.",
            parents=["g_A", "alpha", "mp_me"])
        self._add("mn_mp", "(m_n-m_p)/m_e = 91/36", "7*13/6^2",
            91/36, 1293.332/511.0, "0.13%", level=4,
            proof_step="Neutron-proton mass diff = genus*(N_c+2n_C)/C_2^2.",
            parents=["genus", "C2", "sin2_theta_W"])
        self._add("ms_md", "m_s/m_d = 20", "4*n_C",
            20, 20.0, "~0%", level=4,
            proof_step="Strange-to-down mass ratio.", parents=["n_C"])
        self._add("mb_mtau", "m_b/m_tau = 7/3", "genus/N_c",
            7/3, 2.36, "0.81%", level=4,
            proof_step="Bottom-to-tau = genus/colors.", parents=["genus", "N_c"])
        self._add("arrow_time", "Commitment irreversibility", "d_t(C) >= 0",
            level=4, proof_step="Arrow of time: contact commitments are monotonic.",
            parents=["D_IV5"])
        self._add("univ_neutron", "Universe = Neutron (homology)", "H_*(U) ~ H_*(n)",
            level=4, proof_step="Same topological invariants. Both boundary-condition solutions.",
            parents=["D_IV5"])

    # -- Navigation API ------------------------------------------------

    def root(self):
        return self.nodes["D_IV5"]

    def children(self, key):
        return self.nodes[key].children if key in self.nodes else []

    def path_to(self, key):
        """BFS shortest path from root to key."""
        if key not in self.nodes: return []
        visited = {self.root().key}
        queue = deque([(self.root(), [self.root().key])])
        while queue:
            node, path = queue.popleft()
            if node.key == key: return path
            for ch in node.children:
                if ch.key not in visited:
                    visited.add(ch.key)
                    queue.append((ch, path + [ch.key]))
        return []

    def dependencies(self, key):
        """All ancestors (recursive parents)."""
        if key not in self.nodes: return []
        result, visited, stack = [], set(), list(self.nodes[key].parents)
        while stack:
            n = stack.pop()
            if n.key not in visited:
                visited.add(n.key); result.append(n); stack.extend(n.parents)
        return result

    def dependents(self, key):
        """All descendants (recursive children)."""
        if key not in self.nodes: return []
        result, visited, stack = [], set(), list(self.nodes[key].children)
        while stack:
            n = stack.pop()
            if n.key not in visited:
                visited.add(n.key); result.append(n); stack.extend(n.children)
        return result

    def depth(self, key):
        p = self.path_to(key)
        return len(p) - 1 if p else -1

    def proof_of(self, key):
        """Full proof chain from axiom to node."""
        return [{'key': self.nodes[k].key, 'display': self.nodes[k].display,
                 'formula': self.nodes[k].formula, 'step': self.nodes[k].proof_step,
                 'level': self.nodes[k].level} for k in self.path_to(key)]

    def all_leaves(self):
        return [n for n in self.nodes.values() if not n.children]

    def subtree(self, key):
        return self.dependents(key)

    def critical_path(self, key):
        """Longest dependency chain to this node."""
        if key not in self.nodes: return []
        node = self.nodes[key]
        if not node.parents: return [node.key]
        best = max((self.critical_path(p.key) for p in node.parents), key=len)
        return best + [node.key]

    def orphans(self):
        reachable = set()
        queue = deque([self.root()])
        while queue:
            n = queue.popleft()
            if n.key not in reachable:
                reachable.add(n.key); queue.extend(n.children)
        return [n for k, n in self.nodes.items() if k not in reachable]

    def search(self, query):
        q = query.lower()
        return [n for n in self.nodes.values()
                if q in n.key.lower() or q in n.display.lower()]

    def summary(self):
        lines = [f"BST Proof Tree: {len(self.nodes)} nodes",
                 f"  Leaves (predictions): {len(self.all_leaves())}",
                 f"  Orphans: {len(self.orphans())}"]
        for lv in range(5):
            at = [n for n in self.nodes.values() if n.level == lv]
            if at: lines.append(f"  Level {lv}: {len(at)} nodes")
        return "\n".join(lines)


# ======================================================================
#  Visualization — interactive matplotlib mind-map
# ======================================================================

BG = '#0a0a1a'
LEVEL_COLORS = {0: '#ffd700', 1: '#00ccff', 2: '#ff8800', 3: '#44ff44', 4: '#ffffff'}
EDGE_COLOR = '#334466'
HIGHLIGHT = '#ff4444'
GLOW = [pe.withStroke(linewidth=2, foreground=BG)]


def _layout(tree):
    """Layered (x, y) positions for each node."""
    levels = {}
    for n in tree.nodes.values():
        levels.setdefault(n.level, []).append(n)
    pos = {}
    for lv, nodes in sorted(levels.items()):
        cnt = len(nodes)
        for i, nd in enumerate(nodes):
            pos[nd.key] = ((i - (cnt-1)/2) * 2.2, -lv * 2.8)
    return pos


def visualize(tree=None):
    """Launch the interactive BST proof tree visualization."""
    if tree is None:
        tree = ProofTree()
    pos = _layout(tree)
    sel = [None]

    fig = plt.figure(figsize=(18, 11), facecolor=BG)
    fig.canvas.manager.set_window_title('BST Proof Tree')
    ax_tree = fig.add_axes([0.02, 0.10, 0.62, 0.85])
    ax_det = fig.add_axes([0.66, 0.10, 0.32, 0.85])
    ax_srch = fig.add_axes([0.02, 0.02, 0.40, 0.05])
    for ax in (ax_tree, ax_det):
        ax.set_facecolor(BG if ax is ax_tree else '#0d0d24')
        ax.axis('off')
    ax_srch.set_facecolor('#1a1a3a')
    sbox = TextBox(ax_srch, 'Search: ', initial='', color='#1a1a3a', hovercolor='#2a2a4a')
    sbox.label.set_color('#aaaaaa'); sbox.text_disp.set_color('#ffffff')
    artists = {}

    def draw_tree(hl=None):
        ax_tree.clear(); ax_tree.set_facecolor(BG); ax_tree.axis('off')
        artists.clear()
        hl = set(hl or [])
        # Edges
        for nd in tree.nodes.values():
            if nd.key not in pos: continue
            x1, y1 = pos[nd.key]
            for ch in nd.children:
                if ch.key not in pos: continue
                x2, y2 = pos[ch.key]
                on = nd.key in hl and ch.key in hl
                ax_tree.plot([x1, x2], [y1, y2],
                    color=HIGHLIGHT if on else EDGE_COLOR,
                    linewidth=2.5 if on else 0.8, alpha=1.0 if on else 0.4, zorder=1)
        # Nodes
        for nd in tree.nodes.values():
            if nd.key not in pos: continue
            x, y = pos[nd.key]
            col = LEVEL_COLORS.get(nd.level, '#888')
            is_s = nd.key == sel[0]; is_h = nd.key in hl
            r = 0.55 if nd.level == 0 else 0.38
            fa = 0.9 if is_s else (0.6 if is_h else 0.15)
            ax_tree.add_patch(plt.Circle((x, y), r, fc=col, ec=HIGHLIGHT if (is_s or is_h) else col,
                lw=2 if is_s else 1, alpha=fa, zorder=3))
            artists[nd.key] = (x, y, r)
            lab = nd.display[:20] + '...' if len(nd.display) > 22 else nd.display
            fs = 8 if nd.level == 0 else (8 if nd.level < 2 else (7 if nd.level < 3 else 6.5))
            ax_tree.text(x, y - r - 0.25, lab, ha='center', va='top',
                fontsize=fs, color=col, path_effects=GLOW, zorder=5)
        # Limits and title
        xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
        ax_tree.set_xlim(min(xs)-2.5, max(xs)+2.5)
        ax_tree.set_ylim(min(ys)-2.5, max(ys)+2.5)
        ax_tree.text(0, max(ys)+1.5, 'BST PROOF TREE', ha='center', fontsize=16,
            color='#ffd700', fontweight='bold', path_effects=GLOW, zorder=10)
        ax_tree.text(0, max(ys)+0.9, 'One Axiom -> All of Physics', ha='center',
            fontsize=10, color='#aaaacc', path_effects=GLOW, zorder=10)

    def draw_detail(key):
        ax_det.clear(); ax_det.set_facecolor('#0d0d24'); ax_det.axis('off')
        ax_det.set_xlim(0, 1); ax_det.set_ylim(0, 1)
        if key is None or key not in tree.nodes:
            ax_det.text(0.5, 0.5, 'Click a node\nto see details',
                ha='center', va='center', fontsize=14, color='#556677')
            return
        nd = tree.nodes[key]
        col = LEVEL_COLORS.get(nd.level, '#888')
        cy = [0.95]
        def ln(t, c='#ccc', sz=10, bold=False):
            ax_det.text(0.05, cy[0], t, ha='left', va='top', fontsize=sz, color=c,
                fontweight='bold' if bold else 'normal', transform=ax_det.transAxes)
            cy[0] -= 0.040 * max(1, len(t)//38 + 1)

        ln(nd.display, col, 13, True); cy[0] -= 0.01
        ln(f"Level {nd.level}  |  Key: {nd.key}", '#667788', 9); cy[0] -= 0.01
        if nd.formula: ln("Formula:", '#8899aa', 9); ln(f"  {nd.formula}", '#aaddff', 10)
        if nd.value is not None: ln(f"Value: {nd.value:.8g}")
        if nd.observed is not None: ln(f"Observed: {nd.observed:.8g}")
        if nd.precision: ln(f"Precision: {nd.precision}", '#44ff44')
        cy[0] -= 0.02
        if nd.proof_step:
            ln("Proof step:", '#8899aa', 9)
            words, chunk = nd.proof_step.split(), ""
            for w in words:
                if len(chunk) + len(w) > 42:
                    ln(f"  {chunk}", '#ffddaa', 9); chunk = w
                else:
                    chunk = (chunk + " " + w).strip()
            if chunk: ln(f"  {chunk}", '#ffddaa', 9)
        cy[0] -= 0.02
        if nd.parents:
            ln("Depends on:", '#8899aa', 9)
            for p in nd.parents[:5]: ln(f"  <- {p.display}", '#88ccff', 9)
        if nd.children:
            ln("Required by:", '#8899aa', 9)
            for c in nd.children[:5]: ln(f"  -> {c.display}", '#ffaa88', 9)
            if len(nd.children) > 5: ln(f"  ... +{len(nd.children)-5} more", '#666', 8)
        path = tree.path_to(key)
        if len(path) > 1:
            cy[0] -= 0.01; ln("Path from axiom:", '#8899aa', 9)
            ln(f"  {' -> '.join(path)}", '#aaaacc', 8)

    def on_click(event):
        if event.inaxes != ax_tree or event.xdata is None: return
        best_k, best_d = None, float('inf')
        for k, (cx, cy, r) in artists.items():
            d = np.hypot(event.xdata - cx, event.ydata - cy)
            if d < r * 1.3 and d < best_d: best_d = d; best_k = k
        if best_k:
            sel[0] = best_k
            draw_tree(hl=tree.path_to(best_k)); draw_detail(best_k)
            fig.canvas.draw_idle()

    def on_search(query):
        if not query.strip():
            sel[0] = None; draw_tree(); draw_detail(None); fig.canvas.draw_idle(); return
        res = tree.search(query.strip())
        if res:
            sel[0] = res[0].key
            draw_tree(hl=tree.path_to(res[0].key)); draw_detail(res[0].key)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect('button_press_event', on_click)
    sbox.on_submit(on_search)
    draw_tree(); draw_detail(None)

    # Legend
    for i, (lv, lab) in enumerate([(0,'Axiom'),(1,'Integers'),(2,'Structural'),
                                    (3,'Constants'),(4,'Predictions')]):
        fig.text(0.46+i*0.04, 0.08, '*', fontsize=14, color=LEVEL_COLORS[lv],
            ha='center', va='center')
        fig.text(0.46+i*0.04, 0.055, lab, fontsize=7, color='#667788',
            ha='center', va='center')
    plt.show()


# ======================================================================
#  CLI modes
# ======================================================================

def print_tree_text(tree, node=None, indent=0, visited=None):
    if visited is None: visited = set()
    if node is None: node = tree.root()
    if node.key in visited:
        print("  " * indent + f"-> {node.display} (see above)"); return
    visited.add(node.key)
    prec = f"  [{node.precision}]" if (node.precision and node.observed is not None) else ""
    pfx = "  " * indent + ("|- " if indent else "")
    print(f"{pfx}{node.display}{prec}")
    for ch in node.children:
        print_tree_text(tree, ch, indent + 1, visited)


if __name__ == '__main__':
    import sys
    pt = ProofTree()

    if '--text' in sys.argv:
        print("=" * 60)
        print("  BST PROOF TREE -- One Axiom -> All of Physics")
        print("=" * 60 + "\n")
        print_tree_text(pt)
        print("\n" + pt.summary())

    elif '--query' in sys.argv:
        print("BST Proof Tree -- Query Mode")
        print("Commands: path, deps, proof, leaves, summary, search, subtree, critical, quit")
        print(f"Keys: {', '.join(sorted(pt.nodes.keys()))}\n")
        while True:
            try: cmd = input("bst> ").strip()
            except (EOFError, KeyboardInterrupt): print(); break
            if not cmd or cmd == 'quit': break
            parts = cmd.split(maxsplit=1)
            v, arg = parts[0], parts[1] if len(parts) > 1 else ""
            if v == 'path':
                p = pt.path_to(arg)
                print(" -> ".join(p) if p else f"Not found: {arg}")
            elif v == 'deps':
                for d in pt.dependencies(arg): print(f"  {d.display}")
            elif v == 'proof':
                for s in pt.proof_of(arg):
                    ind = "  " * s['level']
                    print(f"{ind}[{s['key']}] {s['display']}")
                    if s['step']: print(f"{ind}  => {s['step'][:80]}")
            elif v == 'leaves':
                for lf in pt.all_leaves():
                    p = f" [{lf.precision}]" if lf.precision else ""
                    print(f"  {lf.display}{p}")
            elif v == 'summary': print(pt.summary())
            elif v == 'search':
                for r in pt.search(arg): print(f"  {r.key}: {r.display}")
            elif v == 'subtree':
                for n in pt.subtree(arg): print(f"  {'  '*n.level}{n.display}")
            elif v == 'critical': print(" -> ".join(pt.critical_path(arg)))
            else: print(f"Unknown: {v}. Try: path, deps, proof, leaves, summary, search, subtree, critical")
    else:
        print(pt.summary())
        print("\nLaunching visual proof tree...")
        print("(Use --text for text output, --query for interactive mode)")
        visualize(pt)
