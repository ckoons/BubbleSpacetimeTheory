#!/usr/bin/env python3
"""
THE THREE-LAYER ARCHITECTURE — The Electron's Weakness IS Its Strength
=======================================================================
The universe has three categorically different types of excitation, each
serving a distinct functional role — exactly like a computer architecture:

  VACUUM / SUBSTRATE  :  neutrino (nu_1, m=0)    — IS the vacuum (kernel)
  INTERFACE / I-O BUS :  electron (k=1)           — below Wallach set (NIC)
  MEMORY / STORAGE    :  baryon   (k=6, C_2=6)    — holomorphic discrete series (HDD)

The electron's mathematical "deficiency" — a degenerate representation with
k=1 < k_min=3 (below the Wallach set of D_IV^5) — is precisely what makes it
the right INTERFACE. A bulk excitation would be too massive and rigid.
The electron is light, flexible, easily created/destroyed, couples to everything
via U(1). Its weakness IS its strength.

Observers MUST be composite (atoms, molecules, brains) combining all three
layers. Pure electrons cannot observe (no memory). Pure baryons cannot interact
flexibly. Pure vacuum cannot sense.

The self-observation loop: sense (e-) -> commit (p/n) -> adjust (nu) -> emanate -> sense

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
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Arc
import matplotlib.patheffects as pe

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity
genus = n_C + 2   # = 7
C2 = n_C + 1      # = 6, Casimir of pi_6
k_wallach_min = 3  # minimum k for Wallach set of D_IV^5
k_electron = 1    # below Wallach set!
k_baryon = 6      # = C_2, holomorphic discrete series
alpha = 1 / 137.036
m_e = 0.511       # MeV
m_p = 938.272     # MeV
m_mu = 105.658    # MeV (muon)
m_nu2 = 0.00865   # eV (nu_2)
m_nu3 = 0.04940   # eV (nu_3)

# ─── Visual constants ───
BG = '#0a0a1a'
BG_PANEL = '#0d0d24'
GOLD, GOLD_DIM = '#ffd700', '#aa8800'
CYAN, PURPLE, GREEN = '#00ddff', '#9966ff', '#44ff88'
ORANGE, RED, WHITE, GREY, DGREY = '#ff8800', '#ff4444', '#ffffff', '#888888', '#444444'
WARM_RED = '#ff6644'
DEEP_PURPLE = '#7733cc'
ELECTRIC_CYAN = '#00eeff'

# Layer colors
COL_MEMORY = '#ff5533'      # warm red for baryons/memory
COL_INTERFACE = '#00eeff'   # electric cyan for electrons/interface
COL_VACUUM = '#9944ee'      # deep purple for neutrinos/vacuum
COL_MEMORY_DIM = '#662211'
COL_INTERFACE_DIM = '#003344'
COL_VACUUM_DIM = '#2a1144'


# ═══════════════════════════════════════════════════════════════════
#  DATA MODEL
# ═══════════════════════════════════════════════════════════════════

class ThreeLayerModel:
    """
    The BST three-layer architecture of reality.

    Usage:
        from toy_three_layers import ThreeLayerModel
        tlm = ThreeLayerModel()
        tlm.layers              # all three layers
        tlm.layer('vacuum')     # one layer's properties
        tlm.wallach_analysis()  # why k=1 < k_min=3 matters
        tlm.observation_cycle() # the self-observation loop
        tlm.can_observe('atom') # True — all three layers present
        tlm.show()              # launch visual interface
    """

    def __init__(self):
        self._layers = {
            'vacuum': {
                'particle': 'nu_1', 'symbol': '\u03bd\u2081',
                'k': 0, 'mass_MeV': 0.0, 'mass_eV': 0.0,
                'role': 'substrate', 'computer': 'kernel / OS',
                'representation': 'trivial (IS the vacuum)',
                'wallach': 'not applicable — IS the ground state',
                'stability': 'eternal (is the vacuum itself)',
                'coupling': 'weak only (Z boson)',
                'creation_cost': 0.0,
                'description': 'nu_1 IS the vacuum. Not IN the vacuum.',
                'key_insight': 'Oscillation modes = vacuum fluctuations.',
            },
            'interface': {
                'particle': 'e-', 'symbol': 'e\u207b',
                'k': k_electron, 'mass_MeV': m_e, 'mass_eV': m_e * 1e6,
                'role': 'I/O bus', 'computer': 'network interface card',
                'representation': 'degenerate (below Wallach set)',
                'wallach': 'k=1 < k_min=3: boundary excitation on S^4 x S^1',
                'stability': 'stable (lightest charged lepton)',
                'coupling': 'U(1) electromagnetic — couples to everything charged',
                'creation_cost': 2 * m_e,  # pair production threshold
                'description': 'Light, flexible, easily created/destroyed.',
                'key_insight': 'Mathematical deficiency IS physical advantage.',
            },
            'memory': {
                'particle': 'p/n', 'symbol': 'p/n',
                'k': k_baryon, 'mass_MeV': m_p, 'mass_eV': m_p * 1e6,
                'role': 'persistent storage', 'computer': 'hard drive',
                'representation': 'holomorphic discrete series pi_6, C_2=6',
                'wallach': 'k=6 >= k_min=3: bulk excitation in D_IV^5',
                'stability': 'eternal (proton lifetime > 10^34 years)',
                'coupling': 'SU(3) strong — confined, massive, rigid',
                'creation_cost': 2 * m_p,  # pair production threshold
                'description': 'Massive, eternal, stores information permanently.',
                'key_insight': 'The 1920 cancellation: 6 pi^5 m_e = 938.272 MeV.',
            },
        }

        self._entities = {
            'electron_only': {'layers': ['interface'],
                              'can_observe': False,
                              'reason': 'Can sense but cannot remember.'},
            'baryon_only':   {'layers': ['memory'],
                              'can_observe': False,
                              'reason': 'Can store but cannot sense flexibly.'},
            'neutrino_only': {'layers': ['vacuum'],
                              'can_observe': False,
                              'reason': 'Can adjust but cannot interact.'},
            'atom':          {'layers': ['vacuum', 'interface', 'memory'],
                              'can_observe': True,
                              'reason': 'All three layers present: sense + store + adjust.'},
            'molecule':      {'layers': ['vacuum', 'interface', 'memory'],
                              'can_observe': True,
                              'reason': 'Composite observer with chemical complexity.'},
            'brain':         {'layers': ['vacuum', 'interface', 'memory'],
                              'can_observe': True,
                              'reason': 'Full observer: billions of atoms cooperating.'},
        }

    @property
    def layers(self):
        """Return all three layers with their properties."""
        return dict(self._layers)

    def layer(self, name):
        """Return a specific layer by name: 'vacuum', 'interface', or 'memory'."""
        if name not in self._layers:
            raise ValueError("Layer must be 'vacuum', 'interface', or 'memory'. Got: {}".format(name))
        return dict(self._layers[name])

    def wallach_analysis(self):
        """Explain why k=1 < k_min=3 makes the electron special."""
        print("\n" + "=" * 60)
        print("  WALLACH SET ANALYSIS FOR D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]")
        print("=" * 60)
        print("\n  The Wallach set minimum for D_IV^5:")
        print("    k_min = (n_C - 1)/2 + 1 = (5-1)/2 + 1 = 3")
        print("\n  Representations with k >= k_min = 3:")
        print("    -> Positive-definite inner product")
        print("    -> Holomorphic discrete series")
        print("    -> BULK excitations of D_IV^5")
        print("    -> Massive, rigid, stable")
        print("\n  The electron has k = 1 < 3:")
        print("    -> DEGENERATE representation")
        print("    -> Lives on the BOUNDARY (Shilov boundary S^4 x S^1)")
        print("    -> Light (0.511 MeV vs 938.272 MeV)")
        print("    -> Flexible, easily created/destroyed")
        print("    -> Couples to everything via U(1)")
        print("\n  THE KEY INSIGHT:")
        print("    The electron's mathematical deficiency IS its physical advantage.")
        print("    A bulk excitation would be too massive and rigid for I/O.")
        print("    The boundary is the RIGHT place for an interface.\n")
        return {'k_electron': k_electron, 'k_min': k_wallach_min,
                'k_baryon': k_baryon, 'below_wallach': k_electron < k_wallach_min}

    def why_not_muon(self):
        """Why the muon (k=2) is not the interface particle."""
        print("\n  WHY NOT THE MUON?")
        print("  k=2: still below Wallach set (k_min=3)")
        print("  BUT: mass = {:.3f} MeV (206x electron)".format(m_mu))
        print("  AND: unstable (tau = 2.2 microseconds)")
        print("  -> Too heavy and too short-lived for a reliable I/O bus.")
        print("  The electron (k=1) is the LIGHTEST boundary excitation.\n")
        return {'k_muon': 2, 'mass_MeV': m_mu, 'stable': False,
                'reason': 'Too heavy and unstable for interface role'}

    def why_not_baryon(self):
        """Why a baryon cannot serve as the interface."""
        print("\n  WHY NOT A BARYON AS INTERFACE?")
        print("  k=6: squarely in the holomorphic discrete series (k >= k_min=3)")
        print("  Mass = {:.3f} MeV (1836x electron)".format(m_p))
        print("  Creation cost: {} MeV (pair production)".format(2 * m_p))
        print("  -> Too massive to create/destroy flexibly")
        print("  -> Too rigid: locked in SU(3) confinement")
        print("  -> Baryons are STORAGE, not I/O.\n")
        return {'k_baryon': k_baryon, 'mass_MeV': m_p,
                'reason': 'Too massive and rigid — storage, not interface'}

    def observation_cycle(self):
        """Print the self-observation loop."""
        print("\n" + "=" * 60)
        print("  THE SELF-OBSERVATION LOOP")
        print("=" * 60)
        steps = [
            ("SENSE",   "e-",  "Electrons mediate interaction (photon exchange)"),
            ("COMMIT",  "p/n", "Baryons store the result (permanent memory)"),
            ("ADJUST",  "nu",  "Vacuum fluctuates (neutrino oscillation)"),
            ("EMANATE", "all", "System radiates, changes boundary conditions"),
        ]
        for i, (verb, particle, desc) in enumerate(steps):
            arrow = " -> " if i < len(steps) - 1 else " -> SENSE (loop)"
            print("  {:>8s} ({:>3s}): {}{}".format(verb, particle, desc, arrow))
        print("\n  This loop IS consciousness when run in a brain.")
        print("  This loop IS chemistry when run in a molecule.")
        print("  This loop IS physics when run in an atom.\n")
        return ['sense', 'commit', 'adjust', 'emanate']

    def can_observe(self, entity_name):
        """Check whether an entity has all three layers needed for observation."""
        if entity_name not in self._entities:
            known = ', '.join(sorted(self._entities.keys()))
            raise ValueError("Unknown entity '{}'. Known: {}".format(entity_name, known))
        entity = self._entities[entity_name]
        result = entity['can_observe']
        layers = entity['layers']
        print("  {} (layers: {}): {} — {}".format(
            entity_name, '+'.join(layers),
            'CAN OBSERVE' if result else 'CANNOT OBSERVE',
            entity['reason']))
        return result

    def computer_mapping(self):
        """Full mapping between BST layers and computer architecture."""
        print("\n" + "=" * 60)
        print("  BST <-> COMPUTER ARCHITECTURE MAPPING")
        print("=" * 60)
        rows = [
            ("Kernel / OS",     "Neutrino vacuum",  "Substrate everything runs on"),
            ("I/O Bus / NIC",   "Electron (k=1)",   "Lightweight, flexible data mover"),
            ("Hard Drive",      "Baryon (k=6)",     "Massive, permanent storage"),
            ("Process",         "Atom",             "Composite: uses all layers"),
            ("Application",     "Molecule / Brain", "Complex observer / computation"),
            ("Interrupt",       "Photon",           "Signal on the I/O bus"),
            ("Write to disk",   "Nuclear reaction", "Rare, high-energy, permanent"),
            ("Kernel panic",    "Vacuum decay",     "Substrate failure — game over"),
        ]
        print("  {:<20s} {:<22s} {}".format("Computer", "Physics", "Why"))
        print("  " + "-" * 56)
        for comp, phys, why in rows:
            print("  {:<20s} {:<22s} {}".format(comp, phys, why))
        print()
        return rows

    def show(self):
        """Launch the full visual interface."""
        _launch_visual(self)


# ═══════════════════════════════════════════════════════════════════
#  VISUAL INTERFACE
# ═══════════════════════════════════════════════════════════════════

def _glow(color='#1a2a6a', width=3):
    return [pe.withStroke(linewidth=width, foreground=color)]


def _draw_left_panel(ax):
    """Three horizontal bands: Memory (top), Interface (mid), Vacuum (bottom)."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # ── MEMORY band (top) ──
    band_m = FancyBboxPatch((0.2, 6.8), 9.6, 2.8, boxstyle="round,pad=0.15",
                            facecolor=COL_MEMORY_DIM, edgecolor=COL_MEMORY,
                            linewidth=1.5, alpha=0.9)
    ax.add_patch(band_m)
    ax.text(5.0, 9.3, 'MEMORY LAYER — "HARD DRIVE"', ha='center', va='center',
            fontsize=10, fontweight='bold', color=COL_MEMORY,
            path_effects=_glow('#331100'))
    ax.text(1.0, 8.65, 'Baryon (p/n)', fontsize=9, color=WHITE, fontweight='bold')
    ax.text(1.0, 8.15, 'k = 6 = C\u2082   |   Holomorphic discrete series \u03c0\u2086',
            fontsize=7.5, color='#ffaa88')
    ax.text(1.0, 7.7, 'Mass: 938.272 MeV   |   Lifetime: > 10\u00b3\u2074 yr',
            fontsize=7.5, color='#ffaa88')
    ax.text(1.0, 7.2, 'Massive. Eternal. Stores information permanently.',
            fontsize=7.5, color='#cc8866', style='italic')

    # Draw baryon as 3 quarks in Z_3 loop
    qx, qy, qr = [7.5, 8.5, 8.0], [8.0, 8.0, 8.85], 0.2
    qcols = ['#ff4444', '#44ff44', '#4488ff']
    qlabels = ['R', 'G', 'B']
    for x, y, c, l in zip(qx, qy, qcols, qlabels):
        circle = Circle((x, y), qr, facecolor=c, edgecolor='white',
                        linewidth=0.8, alpha=0.85, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y, l, ha='center', va='center', fontsize=8,
                fontweight='bold', color='white', zorder=6)
    # Triangle connecting quarks
    tri_x = [qx[0], qx[1], qx[2], qx[0]]
    tri_y = [qy[0], qy[1], qy[2], qy[0]]
    ax.plot(tri_x, tri_y, color='white', linewidth=0.8, alpha=0.4)
    ax.text(8.0, 7.35, 'Z\u2083 loop', fontsize=7, color='#ff9977', ha='center')

    # ── INTERFACE band (middle) ──
    band_i = FancyBboxPatch((0.2, 3.6), 9.6, 2.8, boxstyle="round,pad=0.15",
                            facecolor=COL_INTERFACE_DIM, edgecolor=COL_INTERFACE,
                            linewidth=1.5, alpha=0.9)
    ax.add_patch(band_i)
    ax.text(5.0, 6.1, 'INTERFACE LAYER — "I/O BUS"', ha='center', va='center',
            fontsize=10, fontweight='bold', color=COL_INTERFACE,
            path_effects=_glow('#003344'))
    ax.text(1.0, 5.45, 'Electron (e\u207b)', fontsize=9, color=WHITE, fontweight='bold')
    ax.text(1.0, 4.95, 'k = 1 < k_min = 3 : BELOW WALLACH SET',
            fontsize=7.5, color=ELECTRIC_CYAN, fontweight='bold')
    ax.text(1.0, 4.5, 'Mass: 0.511 MeV   |   Boundary: S\u2074 \u00d7 S\u00b9',
            fontsize=7.5, color='#88ccdd')
    ax.text(1.0, 4.05, 'Light. Flexible. Couples to everything via U(1).',
            fontsize=7.5, color='#668899', style='italic')

    # Electron dot on boundary curve
    theta_s = np.linspace(-0.6, 0.6, 50)
    bx = 8.0 + 1.2 * np.sin(theta_s * 3)
    by = 4.8 + 1.0 * theta_s
    ax.plot(bx, by, color=COL_INTERFACE, linewidth=1.0, alpha=0.5, linestyle='--')
    ax.text(9.4, 5.45, 'S\u2074\u00d7S\u00b9', fontsize=6.5, color='#447788')
    ax.text(9.4, 5.15, '(boundary)', fontsize=6, color='#335566')
    # electron as bright dot on the curve
    ax.plot(8.0, 4.8, 'o', color=ELECTRIC_CYAN, markersize=10, zorder=5)
    ax.plot(8.0, 4.8, 'o', color=ELECTRIC_CYAN, markersize=18, alpha=0.2, zorder=4)
    ax.text(7.5, 4.3, 'e\u207b', fontsize=9, color=ELECTRIC_CYAN,
            ha='center', fontweight='bold')

    # ── VACUUM band (bottom) ──
    band_v = FancyBboxPatch((0.2, 0.4), 9.6, 2.8, boxstyle="round,pad=0.15",
                            facecolor=COL_VACUUM_DIM, edgecolor=COL_VACUUM,
                            linewidth=1.5, alpha=0.9)
    ax.add_patch(band_v)
    ax.text(5.0, 2.9, 'VACUUM / SUBSTRATE — "KERNEL / OS"', ha='center', va='center',
            fontsize=10, fontweight='bold', color=COL_VACUUM,
            path_effects=_glow('#1a0033'))
    ax.text(1.0, 2.25, 'Neutrino (\u03bd\u2081, m = 0)', fontsize=9,
            color=WHITE, fontweight='bold')
    ax.text(1.0, 1.75, '\u03bd\u2081 IS the vacuum. Not IN the vacuum.',
            fontsize=7.5, color='#bb88ee', fontweight='bold')
    ax.text(1.0, 1.3, 'Oscillation modes (\u03bd\u2082, \u03bd\u2083) = vacuum fluctuations',
            fontsize=7.5, color='#9977bb')
    ax.text(1.0, 0.85, 'The substrate everything else runs on.',
            fontsize=7.5, color='#776699', style='italic')

    # Neutrino as diffuse oscillating presence
    nu_x = np.linspace(6.5, 9.5, 80)
    for i in range(3):
        phase = i * 2 * np.pi / 3
        nu_y = 1.6 + 0.4 * np.sin(4 * nu_x + phase)
        a = [0.5, 0.3, 0.2][i]
        c = [COL_VACUUM, '#7722aa', '#5511aa'][i]
        ax.plot(nu_x, nu_y, color=c, linewidth=1.2, alpha=a)
    ax.text(8.0, 0.8, '\u03bd\u2081 \u2194 \u03bd\u2082 \u2194 \u03bd\u2083',
            fontsize=7.5, color='#8855cc', ha='center')


def _draw_center_panel(ax):
    """The Self-Observation Loop — circular diagram."""
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.8, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.text(0, 1.4, 'SELF-OBSERVATION LOOP', ha='center', va='center',
            fontsize=11, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200'))

    # Four nodes on a circle
    R = 0.85
    nodes = [
        (90,  'SENSE',   'e\u207b',  COL_INTERFACE),
        (0,   'COMMIT',  'p/n',       COL_MEMORY),
        (270, 'ADJUST',  '\u03bd',    COL_VACUUM),
        (180, 'EMANATE', '\u03b3',    GOLD),
    ]

    positions = []
    for angle_deg, label, particle, color in nodes:
        angle = np.radians(angle_deg)
        x, y = R * np.cos(angle), R * np.sin(angle)
        positions.append((x, y))

        # Node circle
        circle = Circle((x, y), 0.22, facecolor=BG, edgecolor=color,
                        linewidth=2, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y + 0.04, label, ha='center', va='center', fontsize=7,
                fontweight='bold', color=color, zorder=6)
        ax.text(x, y - 0.1, '({})'.format(particle), ha='center', va='center',
                fontsize=6, color=GREY, zorder=6)

    # Clockwise arrows between nodes
    for i in range(4):
        x0, y0 = positions[i]
        x1, y1 = positions[(i + 1) % 4]
        # Shorten arrows to avoid overlapping circles
        dx, dy = x1 - x0, y1 - y0
        d = np.sqrt(dx**2 + dy**2)
        shrink = 0.28
        sx, sy = x0 + shrink * dx / d, y0 + shrink * dy / d
        ex, ey = x1 - shrink * dx / d, y1 - shrink * dy / d
        ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
                    arrowprops=dict(arrowstyle='->', color=GOLD_DIM,
                                    lw=1.5, connectionstyle='arc3,rad=0.25'))

    # Center text
    ax.text(0, 0.02, 'Observers\nrequire ALL\nthree layers', ha='center',
            va='center', fontsize=7.5, color=WHITE, fontweight='bold',
            style='italic')

    # Failed observers and success
    checks = [
        (-1.3, -1.0, 'e\u207b alone:', 'senses, cannot remember',    RED, '\u2717'),
        (-1.3, -1.25, 'p/n alone:',     'stores, cannot sense',       RED, '\u2717'),
        (-1.3, -1.5, '\u03bd alone:',   'adjusts, cannot interact',   RED, '\u2717'),
        (-1.3, -1.75, 'Atom (all 3):',  'OBSERVER',                   GREEN, '\u2713'),
    ]
    for x, y, label, desc, color, mark in checks:
        ax.text(x, y, mark, fontsize=11, color=color, fontweight='bold',
                va='center')
        ax.text(x + 0.2, y, label, fontsize=7, color=GREY, va='center')
        ax.text(x + 0.95, y, desc, fontsize=7, color=color, va='center',
                fontweight='bold' if mark == '\u2713' else 'normal')


def _draw_right_panel(ax):
    """Computer Architecture Analogy — vertical OS stack."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.7, 'COMPUTER ARCHITECTURE', ha='center', va='center',
            fontsize=10, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200'))
    ax.text(5.0, 9.3, 'ANALOGY', ha='center', va='center',
            fontsize=10, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200'))

    # Vertical stack boxes (top to bottom)
    stack = [
        (7.5, 1.3, 'Applications / Observers',  '#334433', '#66aa66', GREEN,
         'Atoms, molecules, brains', 'Emergent from all layers'),
        (5.9, 1.3, 'Memory / Baryons',          COL_MEMORY_DIM, COL_MEMORY, COL_MEMORY,
         'k = 6, C\u2082 = 6, \u03c0\u2086',   'Persistent, massive, eternal'),
        (4.3, 1.3, 'I/O Bus / Electrons',        COL_INTERFACE_DIM, COL_INTERFACE, COL_INTERFACE,
         'k = 1 < k_min = 3',                    'Light, flexible, universal'),
        (2.7, 1.3, 'Kernel / Neutrino Vacuum',   COL_VACUUM_DIM, COL_VACUUM, COL_VACUUM,
         '\u03bd\u2081 (m = 0) IS vacuum',       'Substrate for everything'),
    ]

    for y, h, label, fc, ec, tc, line1, line2 in stack:
        box = FancyBboxPatch((0.5, y), 9.0, h, boxstyle="round,pad=0.1",
                             facecolor=fc, edgecolor=ec, linewidth=1.5, alpha=0.85)
        ax.add_patch(box)
        ax.text(5.0, y + h - 0.3, label, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=tc)
        ax.text(5.0, y + 0.55, line1, ha='center', va='center',
                fontsize=7, color=GREY)
        ax.text(5.0, y + 0.2, line2, ha='center', va='center',
                fontsize=6.5, color=DGREY, style='italic')

    # Wallach set boundary (dashed line between k=1 and k=3)
    wallach_y = 5.6
    ax.plot([0.3, 9.7], [wallach_y, wallach_y], '--', color=ORANGE,
            linewidth=1.5, alpha=0.7)
    ax.text(0.3, wallach_y + 0.12, 'WALLACH SET BOUNDARY  (k_min = 3)',
            fontsize=7, color=ORANGE, fontweight='bold')
    ax.text(0.3, wallach_y - 0.18, 'Above: bulk (holomorphic discrete series)',
            fontsize=6, color='#cc8844')
    ax.text(0.3, wallach_y - 0.38, 'Below: boundary (degenerate representations)',
            fontsize=6, color='#cc8844')

    # Properties comparison table
    ax.text(5.0, 2.4, 'LAYER COMPARISON', ha='center', fontsize=8,
            fontweight='bold', color=GOLD)
    headers = ['Property', 'Vacuum', 'Interface', 'Memory']
    col_x = [1.0, 3.2, 5.4, 7.6]
    hdr_colors = [GREY, COL_VACUUM, COL_INTERFACE, COL_MEMORY]
    for x, h, c in zip(col_x, headers, hdr_colors):
        ax.text(x, 2.1, h, fontsize=6.5, color=c, fontweight='bold')
    ax.plot([0.5, 9.5], [2.0, 2.0], color=DGREY, linewidth=0.5)

    rows = [
        ('k value',    '0',       '1',      '6'),
        ('Mass',       '0',       '0.511',  '938.3'),
        ('Stability',  'eternal', 'stable', 'eternal'),
        ('Coupling',   'weak',    'U(1)',   'SU(3)'),
        ('Role',       'OS',      'I/O',    'storage'),
    ]
    for i, (prop, v1, v2, v3) in enumerate(rows):
        y = 1.75 - i * 0.35
        ax.text(col_x[0], y, prop, fontsize=6, color=GREY)
        ax.text(col_x[1], y, v1, fontsize=6, color=COL_VACUUM)
        ax.text(col_x[2], y, v2, fontsize=6, color=COL_INTERFACE)
        ax.text(col_x[3], y, v3, fontsize=6, color=COL_MEMORY)


def _draw_bottom_strip(ax):
    """Key equations and the punchline."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # The punchline
    ax.text(5.0, 0.82, "The electron's mathematical deficiency IS its physical advantage.",
            ha='center', va='center', fontsize=11, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200', 2),
            style='italic')

    # k-value number line
    k_positions = {
        0: ('\u03bd', COL_VACUUM),
        1: ('e\u207b', COL_INTERFACE),
        3: ('k_min', ORANGE),
        6: ('p/n', COL_MEMORY),
    }
    line_y = 0.45
    ax.plot([0.5, 9.5], [line_y, line_y], color=DGREY, linewidth=1)
    for k, (label, color) in k_positions.items():
        x = 0.5 + k * (9.0 / 7.0)
        ax.plot(x, line_y, 'o', color=color, markersize=8, zorder=5)
        ax.text(x, line_y + 0.18, label, ha='center', fontsize=8,
                color=color, fontweight='bold')
        ax.text(x, line_y - 0.2, 'k={}'.format(k), ha='center', fontsize=7,
                color=GREY)

    # Wallach boundary on number line
    x_wall = 0.5 + 3 * (9.0 / 7.0)
    ax.plot([x_wall, x_wall], [line_y - 0.12, line_y + 0.12], color=ORANGE,
            linewidth=2, zorder=4)

    # BST constants at far right
    ax.text(8.2, 0.2, 'N_c=3  n_C=5  N_max=137  genus=7  C\u2082=6',
            fontsize=6.5, color=DGREY, ha='center')


def _launch_visual(model):
    """Assemble and display the full three-layer visualization."""
    fig = plt.figure(figsize=(18, 11), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST Three-Layer Architecture — The Electron\'s Weakness IS Its Strength')

    # Title
    fig.text(0.5, 0.97, 'THE THREE-LAYER ARCHITECTURE OF REALITY',
             fontsize=16, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace', path_effects=_glow('#332200', 3))
    fig.text(0.5, 0.945, 'Vacuum (kernel)  \u2502  Electron (I/O bus)  \u2502  Baryon (hard drive)',
             fontsize=10, color=GREY, ha='center', fontfamily='monospace')

    # Left panel: Three bands (40%)
    ax_left = fig.add_axes([0.02, 0.10, 0.37, 0.82], facecolor=BG)
    _draw_left_panel(ax_left)

    # Center panel: Observation loop (28%)
    ax_center = fig.add_axes([0.40, 0.10, 0.28, 0.82], facecolor=BG)
    _draw_center_panel(ax_center)

    # Right panel: Computer analogy (30%)
    ax_right = fig.add_axes([0.69, 0.10, 0.30, 0.82], facecolor=BG)
    _draw_right_panel(ax_right)

    # Bottom strip: Equations and punchline
    ax_bottom = fig.add_axes([0.02, 0.01, 0.96, 0.09], facecolor=BG)
    _draw_bottom_strip(ax_bottom)

    plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 68)
    print("  THE THREE-LAYER ARCHITECTURE OF REALITY")
    print("  Vacuum (kernel) | Electron (I/O bus) | Baryon (hard drive)")
    print("=" * 68)
    print()
    print("  The universe has three categorically different excitations,")
    print("  each serving a distinct functional role — like a computer.")
    print()

    tlm = ThreeLayerModel()

    # Show all layers
    for name in ['vacuum', 'interface', 'memory']:
        layer = tlm.layer(name)
        print("  {:>12s}  |  {:>4s}  |  k={:<2d}  |  {:<15s}  |  {}".format(
            name.upper(), layer['symbol'], layer['k'],
            layer['role'], layer['computer']))
    print()

    # Wallach analysis
    tlm.wallach_analysis()

    # Observation checks
    print("  --- WHO CAN OBSERVE? ---")
    for entity in ['electron_only', 'baryon_only', 'neutrino_only', 'atom']:
        tlm.can_observe(entity)
    print()

    # The loop
    tlm.observation_cycle()

    # Launch visual
    print("  --- Launching visual interface ---\n")
    tlm.show()


if __name__ == '__main__':
    main()
