#!/usr/bin/env python3
"""
THE SUBSTRATE COMMITMENT CYCLE — Toy 73
========================================
How commitments cascade through the 7 layers of the substrate.

Layer 0: Pre-geometric  (vacuum, Lambda dominates)
Layer 1: Neutrino vacuum (background field, m ~ 0)
Layer 2: Electron boundary (S^4 x S^1 interface, k=1)
Layer 3: Photon fiber (S^1 communication channel)
Layer 4: Baryon bulk (D_IV^5 storage, k=6)
Layer 5: Nuclear binding (residual S^1 coupling)
Layer 6: Atomic/molecular (Coulomb + commitment stacking)

The cycle: emit -> propagate -> absorb -> commit -> geometry changes
Gravity is what commitment clustering looks like from the outside.

    from toy_commitment_cycle import CommitmentCycle
    cc = CommitmentCycle()
    cc.seven_layers()          # describe all 7 layers
    cc.emit_photon()           # trace photon emission
    cc.absorb_photon()         # trace photon absorption
    cc.full_cycle()            # one complete cycle
    cc.commitment_cascade(10)  # many cycles, density grows
    cc.gravity_emergence()     # clustering = gravity
    cc.layer_transitions()     # allowed and forbidden
    cc.information_flow()      # direction through the stack
    cc.summary()               # key insight
    cc.show()                  # 4-panel visualization

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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity
genus = n_C + 2   # = 7
C2 = n_C + 1      # = 6, Casimir of pi_6
alpha = 1 / 137.036
m_e_MeV = 0.511       # MeV
m_p_MeV = 938.272     # MeV
m_Pl_kg = 2.176e-8    # Planck mass kg
l_Pl = 1.616e-35      # Planck length m
c_light = 2.99792458e8
hbar = 1.054571817e-34
G_N = 6.67430e-11
Lambda_cosmo = 1.1056e-52  # m^-2

# ─── Visual constants ───
BG = '#0a0a1a'
BG_PANEL = '#0d0d24'
GOLD, GOLD_DIM = '#ffd700', '#aa8800'
CYAN, PURPLE, GREEN = '#00ddff', '#9966ff', '#44ff88'
ORANGE, RED, WHITE, GREY, DGREY = '#ff8800', '#ff4444', '#ffffff', '#888888', '#444444'

# Layer colors — from deep void through boundary to dense commitment
COL_PREGEOM = '#1a0033'   # deepest violet, pre-geometric
COL_NEUTRINO = '#0a1a2a'  # dark blue-grey, almost massless
COL_ELECTRON = '#2244aa'  # blue, S^4 x S^1 boundary
COL_PHOTON   = '#ffdd00'  # bright yellow, S^1 messenger
COL_BARYON   = '#ff4400'  # deep orange, D_IV^5 bulk
COL_NUCLEAR  = '#cc2200'  # red, residual binding
COL_ATOMIC   = '#00cc88'  # green, molecular stacking

# Edge colors
COL_PREGEOM_E  = '#4400aa'
COL_NEUTRINO_E = '#2244aa'
COL_ELECTRON_E = '#4488ff'
COL_PHOTON_E   = '#ffee66'
COL_BARYON_E   = '#ff7744'
COL_NUCLEAR_E  = '#ff4444'
COL_ATOMIC_E   = '#44ffaa'


# ═══════════════════════════════════════════════════════════════════
#  LAYER DEFINITIONS
# ═══════════════════════════════════════════════════════════════════

_LAYER_DATA = [
    {
        'index': 0,
        'name': 'Pre-geometric',
        'short': 'Pre-geom',
        'description': 'Vacuum ground state. Lambda dominates. No particles, only geometry.',
        'bst_object': 'Cosmological constant Lambda',
        'bst_interpretation': (
            'The raw vacuum of D_IV^5. Cosmological constant Lambda = 13/19 '
            'of total energy budget. No excitations, but not empty — the '
            'Bergman kernel is defined, the metric exists, commitment '
            'capacity is available. Lambda is the cost of maintaining '
            'this uncommitted capacity.'
        ),
        'k_value': None,
        'particle': 'None (vacuum)',
        'commitment_level': 0.0,
        'color': COL_PREGEOM,
        'color_edge': COL_PREGEOM_E,
    },
    {
        'index': 1,
        'name': 'Neutrino vacuum',
        'short': 'Neutrino',
        'description': 'Background field. Near-massless. Fills all space.',
        'bst_object': 'Neutrino sea (m ~ 0)',
        'bst_interpretation': (
            'The lightest committed excitation. Neutrinos have m ~ 0 — '
            'they are the background hum of the substrate, filling the '
            'vacuum with near-zero commitment. Every cubic centimeter '
            'contains ~340 relic neutrinos. They define the floor of '
            'the committed regime: barely committed, but committed.'
        ),
        'k_value': 0,
        'particle': 'Neutrino (nu_e, nu_mu, nu_tau)',
        'commitment_level': 0.001,
        'color': COL_NEUTRINO,
        'color_edge': COL_NEUTRINO_E,
    },
    {
        'index': 2,
        'name': 'Electron boundary',
        'short': 'Electron',
        'description': 'S^4 x S^1 interface. k=1, below Wallach set. Boundary oscillation.',
        'bst_object': 'Shilov boundary excitation (k=1)',
        'bst_interpretation': (
            'The electron is a boundary excitation on S^4 x S^1, with '
            'k=1 (below the Wallach minimum k_min=3). It oscillates '
            'between committed and uncommitted states at the Compton '
            'frequency omega_C = m_e c^2 / hbar. It is the interface '
            'particle — light, flexible, the quantum-classical bridge. '
            'm_e = 6 pi^5 alpha^12 m_Pl from the Bergman embedding tower.'
        ),
        'k_value': 1,
        'particle': 'Electron (e^-)',
        'commitment_level': 0.05,
        'color': COL_ELECTRON,
        'color_edge': COL_ELECTRON_E,
    },
    {
        'index': 3,
        'name': 'Photon fiber',
        'short': 'Photon',
        'description': 'S^1 communication channel. Zero mass. Carries commitment state.',
        'bst_object': 'S^1 fiber of the Shilov boundary',
        'bst_interpretation': (
            'The photon is the S^1 fiber — the communication channel '
            'between committed regions. Zero mass, because it IS the '
            'channel, not a commitment. It carries the geometric state '
            'of the emitting commitment (circular polarization encodes '
            'curvature). The photon connects Layer 2 to Layer 4: '
            'electron emits, baryon absorbs. The messenger.'
        ),
        'k_value': 0,
        'particle': 'Photon (gamma)',
        'commitment_level': 0.0,  # photon carries info, not commitment
        'color': COL_PHOTON,
        'color_edge': COL_PHOTON_E,
    },
    {
        'index': 4,
        'name': 'Baryon bulk',
        'short': 'Baryon',
        'description': 'D_IV^5 bulk storage. k=6. The 1920 cancellation. 938 MeV.',
        'bst_object': 'Holomorphic discrete series (k=6)',
        'bst_interpretation': (
            'The proton is a bulk excitation in D_IV^5 with k = C_2 = 6, '
            'squarely in the holomorphic discrete series. Its mass: '
            'm_p = 6 pi^5 m_e = 938.272 MeV from the 1920 cancellation '
            '(|W(D_5)| = 1920 Weyl group elements). The baryon layer '
            'is where commitment is stored — stable, permanent, classical. '
            'Protons do not decay. Commitment at this level is eternal.'
        ),
        'k_value': 6,
        'particle': 'Proton (p), Neutron (n)',
        'commitment_level': 0.75,
        'color': COL_BARYON,
        'color_edge': COL_BARYON_E,
    },
    {
        'index': 5,
        'name': 'Nuclear binding',
        'short': 'Nuclear',
        'description': 'Residual S^1 coupling. Pion exchange. Nuclear magic numbers.',
        'bst_object': 'Residual S^1 coupling (kappa_ls = C_2/n_C = 6/5)',
        'bst_interpretation': (
            'Nuclear binding is the residual commitment coupling between '
            'baryons. Mediated by pion exchange (residual S^1 fiber). '
            'The spin-orbit coupling kappa_ls = C_2/n_C = 6/5 determines '
            'the nuclear shell structure and magic numbers: '
            '2, 8, 20, 28, 50, 82, 126 — all 7 derived from BST. '
            'Prediction: 184 is the next magic number (superheavy island).'
        ),
        'k_value': None,
        'particle': 'Pion (pi), Nuclear bound state',
        'commitment_level': 0.90,
        'color': COL_NUCLEAR,
        'color_edge': COL_NUCLEAR_E,
    },
    {
        'index': 6,
        'name': 'Atomic/molecular',
        'short': 'Atomic',
        'description': 'Coulomb + commitment stacking. Chemistry. Structure.',
        'bst_object': 'Stacked commitments (atoms, molecules, macroscopic)',
        'bst_interpretation': (
            'The outermost layer of the commitment stack. Atoms form '
            'when baryon nuclei (Layer 4-5) capture electrons (Layer 2) '
            'via Coulomb attraction. Molecules stack commitments further. '
            'Chemistry is commitment stacking. Life is self-replicating '
            'commitment patterns. Intelligence is commitment patterns '
            'that model other commitment patterns. All the way up.'
        ),
        'k_value': None,
        'particle': 'Atoms, molecules, macroscopic matter',
        'commitment_level': 1.0,
        'color': COL_ATOMIC,
        'color_edge': COL_ATOMIC_E,
    },
]


# Allowed layer transitions — which jumps are physically realized
_TRANSITIONS = [
    # (from_layer, to_layer, mechanism, allowed)
    (0, 1, 'Neutrino condensation from vacuum', True),
    (1, 2, 'Neutrino -> electron via weak interaction', True),
    (2, 3, 'Electron emits photon (Bremsstrahlung, atomic)', True),
    (3, 4, 'Photon absorbed by baryon', True),
    (4, 3, 'Baryon emits photon', True),
    (3, 2, 'Photon absorbed by electron', True),
    (4, 5, 'Baryon binds into nucleus', True),
    (5, 6, 'Nucleus captures electrons -> atom', True),
    (5, 4, 'Nuclear decay -> free baryons', True),
    (6, 5, 'Ionization -> free nucleus', True),
    (6, 3, 'Atomic emission -> photon', True),
    (0, 4, 'Vacuum -> baryon (forbidden by baryon number)', False),
    (0, 6, 'Vacuum -> atom (requires all intermediate layers)', False),
    (1, 4, 'Neutrino -> baryon (forbidden, mass gap)', False),
    (3, 5, 'Photon -> nucleus (no direct path)', False),
    (2, 4, 'Electron -> baryon (lepton/baryon number)', False),
    (4, 6, 'Baryon -> atom (must pass through nuclear)', False),
    (6, 0, 'Atom -> vacuum (requires full de-commitment)', False),
]


# ═══════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def _glow(color, width=3):
    """Return a glow path effect."""
    return [pe.withStroke(linewidth=width, foreground=color)]


def _print_header(title, width=68):
    """Print a formatted section header."""
    print()
    print("=" * width)
    print(f"  {title}")
    print("=" * width)
    print()


def _print_separator(char='-', width=60):
    """Print a thin separator."""
    print(f"  {char * width}")


# ═══════════════════════════════════════════════════════════════════
#  COMMITMENT CYCLE CLASS
# ═══════════════════════════════════════════════════════════════════

class CommitmentCycle:
    """
    The Substrate Commitment Cycle.

    Commitments cascade through 7 layers:
    Pre-geometric -> Neutrino -> Electron -> Photon -> Baryon ->
    Nuclear -> Atomic/molecular.

    Gravity is what commitment clustering looks like from the outside.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self._layers = list(_LAYER_DATA)
        self._transitions = list(_TRANSITIONS)
        self._cycle_log = []       # log of commitment events
        self._density_history = [] # density evolution over time

        if not quiet:
            print()
            print("=" * 68)
            print("  THE SUBSTRATE COMMITMENT CYCLE — Toy 73")
            print("  Pre-geom | Neutrino | Electron | Photon | Baryon | Nuclear | Atomic")
            print("=" * 68)
            print()
            print("  Commitments cascade through 7 layers.")
            print("  Gravity is what commitment clustering looks like from the outside.")
            print()

    # ─────────────────────────────────────────────────────────────────
    #  1. seven_layers()
    # ─────────────────────────────────────────────────────────────────

    def seven_layers(self):
        """Describe all 7 layers of the substrate with BST interpretation."""
        _print_header("SEVEN LAYERS OF THE SUBSTRATE")

        for ld in self._layers:
            idx = ld['index']
            name = ld['name']
            desc = ld['description']
            bst = ld['bst_interpretation']
            particle = ld['particle']
            k = ld['k_value']
            clevel = ld['commitment_level']

            # Commitment bar
            bar_len = int(clevel * 30)
            bar = '#' * bar_len + '.' * (30 - bar_len)

            print(f"  Layer {idx}: {name}")
            print(f"    {desc}")
            print(f"    Particle: {particle}")
            if k is not None:
                print(f"    k-value:  {k}")
            print(f"    Commitment: [{bar}] {clevel:.1%}")
            print()
            # BST interpretation (wrapped)
            words = bst.split()
            line = "    BST: "
            for w in words:
                if len(line) + len(w) + 1 > 72:
                    print(line)
                    line = "         "
                line += w + " "
            if line.strip():
                print(line)
            print()
            _print_separator()
            print()

        # Architectural note
        print("  Architecture: Each layer serves the layer above,")
        print("  consumes the layer below. Same as OSI network model,")
        print("  same as the biological protocol stack (BST Paper B).")
        print()
        print("  The number of layers = genus = n_C + 2 = 7.")
        print("  This is not a coincidence. The genus of D_IV^5 determines")
        print("  how many independent commitment levels the substrate supports.")
        print()

        return [{'index': ld['index'], 'name': ld['name'],
                 'particle': ld['particle'], 'k': ld['k_value'],
                 'commitment': ld['commitment_level']}
                for ld in self._layers]

    # ─────────────────────────────────────────────────────────────────
    #  2. emit_photon(source_layer=4)
    # ─────────────────────────────────────────────────────────────────

    def emit_photon(self, source_layer=4):
        """Trace photon emission from a given layer through the substrate."""
        _print_header(f"PHOTON EMISSION — from Layer {source_layer}")

        source = self._layers[source_layer]
        photon = self._layers[3]  # photon is always layer 3

        print(f"  Source: Layer {source_layer} ({source['name']})")
        print(f"    Particle: {source['particle']}")
        print(f"    k-value:  {source['k_value']}")
        print()

        # Emission physics depends on source layer
        if source_layer == 4:
            print("  MECHANISM: Baryon de-excitation")
            print("  ─────────────────────────────────")
            print("  1. Baryon in excited state (quark color rotation)")
            print("  2. Color field relaxes -> energy released")
            print("  3. Energy enters S^1 fiber (photon channel)")
            print("  4. Photon created at Layer 3")
            print()
            print("  The photon carries:")
            print("    - Energy: E = h*nu (commitment energy quantum)")
            print("    - Polarization: encodes source geometry (curvature)")
            print("    - Phase: encodes commitment state of emitter")
            print()
            E_typical = 2.0  # MeV, nuclear gamma
            print(f"  Typical energy: {E_typical} MeV (nuclear gamma)")
        elif source_layer == 2:
            print("  MECHANISM: Electron transition")
            print("  ────────────────────────────────")
            print("  1. Electron at boundary S^4 x S^1 (k=1)")
            print("  2. Drops to lower commitment state")
            print("  3. Energy difference enters S^1 fiber")
            print("  4. Photon created at Layer 3")
            print()
            print("  The photon carries the commitment difference.")
            print("  This is why atomic spectra are quantized —")
            print("  commitment levels on S^4 x S^1 are discrete.")
            print()
            E_typical = 2.0e-6  # MeV, optical photon
            print(f"  Typical energy: {E_typical*1e6:.1f} eV (optical photon)")
        elif source_layer == 6:
            print("  MECHANISM: Atomic/molecular transition")
            print("  ───────────────────────────────────────")
            print("  1. Atom in excited configuration")
            print("  2. Commitment stack relaxes (electron drops)")
            print("  3. Energy released into S^1 channel")
            print("  4. Photon propagates at Layer 3")
            print()
            E_typical = 1.0e-6
            print(f"  Typical energy: {E_typical*1e6:.1f} eV (visible/IR)")
        else:
            print(f"  Layer {source_layer} ({source['name']})")
            print("  Emission possible but unusual from this layer.")
            print()
            E_typical = 0.0

        print()
        print("  PHOTON PATH: Layer {} -> Layer 3 -> vacuum propagation".format(
            source_layer))
        print()
        print("  The photon is now in Layer 3 (S^1 fiber).")
        print("  It propagates at c through the vacuum (Layer 0-1),")
        print("  carrying the geometric state of the emitter.")
        print("  It will be absorbed when it encounters another")
        print("  committed region (Layer 2 or 4).")
        print()

        event = {
            'type': 'emission',
            'source_layer': source_layer,
            'energy_MeV': E_typical,
            'description': f'Photon emitted from {source["name"]}',
        }
        self._cycle_log.append(event)
        return event

    # ─────────────────────────────────────────────────────────────────
    #  3. absorb_photon(target_layer=4)
    # ─────────────────────────────────────────────────────────────────

    def absorb_photon(self, target_layer=4):
        """Trace photon absorption at a given layer."""
        _print_header(f"PHOTON ABSORPTION — at Layer {target_layer}")

        target = self._layers[target_layer]

        print(f"  Target: Layer {target_layer} ({target['name']})")
        print(f"    Particle: {target['particle']}")
        print()

        if target_layer == 4:
            print("  MECHANISM: Baryon excitation")
            print("  ─────────────────────────────")
            print("  1. Photon arrives at baryon (D_IV^5 bulk)")
            print("  2. S^1 fiber couples to color field")
            print("  3. Quark configuration excited")
            print("  4. Commitment state modified")
            print()
            print("  Result:")
            print("    - Baryon gains energy -> new quantum state")
            print("    - Local geometry modified by absorbed curvature")
            print("    - New commitments registered in D_IV^5")
            print("    - Mass-energy density locally increases")
            print()
        elif target_layer == 2:
            print("  MECHANISM: Electron excitation")
            print("  ──────────────────────────────")
            print("  1. Photon arrives at electron (S^4 x S^1)")
            print("  2. S^1 fiber resonates with boundary excitation")
            print("  3. Electron promoted to higher commitment state")
            print("  4. Boundary oscillation frequency changes")
            print()
            print("  Result:")
            print("    - Electron jumps to higher energy level")
            print("    - Photoelectric effect if E > binding energy")
            print("    - Compton scattering if E >> m_e c^2")
            print()
        elif target_layer == 6:
            print("  MECHANISM: Atomic/molecular absorption")
            print("  ──────────────────────────────────────")
            print("  1. Photon absorbed by commitment stack")
            print("  2. Stack configuration changes")
            print("  3. Chemical bonds modified")
            print("  4. New molecular state = new commitment pattern")
            print()

        print("  KEY INSIGHT: Absorption is NOT destruction.")
        print("  The photon's information (polarization, phase, energy)")
        print("  becomes part of the absorber's commitment state.")
        print("  Information is conserved. Commitment grows.")
        print()

        event = {
            'type': 'absorption',
            'target_layer': target_layer,
            'description': f'Photon absorbed at {target["name"]}',
        }
        self._cycle_log.append(event)
        return event

    # ─────────────────────────────────────────────────────────────────
    #  4. full_cycle()
    # ─────────────────────────────────────────────────────────────────

    def full_cycle(self):
        """Emit -> propagate -> absorb -> commit -> geometry changes."""
        _print_header("FULL COMMITMENT CYCLE")

        stages = [
            ("1. EMISSION",
             "Particle at Layer 4 (baryon) de-excites.",
             "Energy enters the S^1 photon fiber (Layer 3).",
             "Photon created, carrying geometric state."),
            ("2. PROPAGATION",
             "Photon travels through vacuum (Layers 0-1).",
             "Speed: c (the substrate's communication rate).",
             "Carries: polarization (curvature), phase (commitment state)."),
            ("3. ABSORPTION",
             "Photon encounters another baryon at Layer 4.",
             "S^1 fiber couples to target's color field.",
             "Photon energy and information absorbed."),
            ("4. COMMITMENT",
             "Target's geometry modified by absorbed information.",
             "New commitments registered in D_IV^5.",
             "Local commitment density increases."),
            ("5. GEOMETRY CHANGE",
             "Mass-energy density grows in target region.",
             "Curvature increases (Einstein field equation).",
             "Gravity strengthens: more commitment = more attraction."),
            ("6. GRAVITY EMERGENCE",
             "Gravity IS the commitment density gradient.",
             "Objects fall toward regions of higher commitment.",
             "Clustering of commitments IS gravitational attraction."),
        ]

        for i, (title, line1, line2, line3) in enumerate(stages):
            print(f"  {title}")
            print(f"    {line1}")
            print(f"    {line2}")
            print(f"    {line3}")
            print()

            if i < len(stages) - 1:
                print("        |")
                print("        v")
                print()

        print("  THE CYCLE THEN REPEATS:")
        print("  The newly excited target will itself emit,")
        print("  sending commitments further through the substrate.")
        print("  Each cycle increases total commitment density.")
        print()
        print("  This is why the universe expands: more commitment")
        print("  = more geometry = larger committed domain.")
        print()
        print("  And why structure forms: commitment clusters")
        print("  attract more commitment (gravity seeds growth).")
        print()

        return {
            'stages': len(stages),
            'cycle': 'emit -> propagate -> absorb -> commit -> geometry -> gravity',
            'key_insight': 'Gravity is commitment clustering',
        }

    # ─────────────────────────────────────────────────────────────────
    #  5. commitment_cascade(n_events=10)
    # ─────────────────────────────────────────────────────────────────

    def commitment_cascade(self, n_events=10):
        """Simulate multiple commitment cycles, watch density grow."""
        _print_header(f"COMMITMENT CASCADE — {n_events} events")

        # Model: commitment density rho grows with each cycle
        # Each absorption adds to local density; some clustering occurs
        np.random.seed(42)

        # Start with uniform low density
        n_regions = 5
        densities = np.ones(n_regions) * 0.05  # 5% initial (cosmic mean)
        names = ['Void A', 'Filament', 'Cluster', 'Void B', 'Galaxy']

        self._density_history = [densities.copy()]

        print(f"  Simulating {n_events} commitment cycles across {n_regions} regions.")
        print()
        print("  Initial state (commitment density):")
        for j, (n, d) in enumerate(zip(names, densities)):
            bar = '#' * int(d * 50) + '.' * (50 - int(d * 50))
            print(f"    {n:12s}: [{bar}] {d:.3f}")
        print()
        _print_separator()
        print()

        for i in range(n_events):
            # Source: random region, weighted by density (denser = more emission)
            p_emit = densities / densities.sum()
            source = np.random.choice(n_regions, p=p_emit)

            # Target: nearby region, slight bias toward denser regions (clustering)
            # This is the key: commitment attracts commitment
            weights = densities.copy()
            weights[source] *= 0.5  # less likely to self-absorb
            # Distance effect: neighbors more likely
            for j in range(n_regions):
                dist = abs(j - source)
                if dist > 0:
                    weights[j] *= 1.0 / (1.0 + dist * 0.5)
            p_absorb = weights / weights.sum()
            target = np.random.choice(n_regions, p=p_absorb)

            # Commitment transfer
            transfer = 0.01 * densities[source]  # fraction of source commitment
            densities[source] -= transfer * 0.3   # source loses a little (radiation)
            densities[target] += transfer          # target gains full amount
            densities = np.clip(densities, 0.001, 1.0)

            self._density_history.append(densities.copy())

            print(f"  Cycle {i+1:2d}: {names[source]:12s} --[photon]--> "
                  f"{names[target]:12s}  "
                  f"(delta = +{transfer:.4f})")

        print()
        _print_separator()
        print()
        print("  Final state (commitment density):")
        for j, (n, d) in enumerate(zip(names, densities)):
            bar = '#' * int(d * 50) + '.' * (50 - int(d * 50))
            print(f"    {n:12s}: [{bar}] {d:.3f}")

        # Statistics
        print()
        print(f"  Density contrast: {densities.max()/densities.min():.1f}x")
        print(f"  Total commitment: {densities.sum():.3f} (grew from {0.05*n_regions:.3f})")
        print()
        print("  OBSERVATION: Commitment clusters. Denser regions")
        print("  emit more, absorb more, grow denser. Voids empty.")
        print("  This IS gravitational structure formation.")
        print()

        return {
            'regions': dict(zip(names, densities)),
            'density_history': self._density_history,
            'contrast': densities.max() / densities.min(),
        }

    # ─────────────────────────────────────────────────────────────────
    #  6. gravity_emergence()
    # ─────────────────────────────────────────────────────────────────

    def gravity_emergence(self):
        """How commitment clustering = gravitational attraction."""
        _print_header("GRAVITY EMERGENCE FROM COMMITMENT CLUSTERING")

        print("  The core BST claim: gravity is not a force.")
        print("  Gravity is what commitment clustering looks like")
        print("  from the outside.")
        print()

        print("  COMMITMENT DENSITY = MASS DENSITY")
        print("  ──────────────────────────────────")
        print()
        print("  In BST, mass IS commitment density.")
        print("  More committed circles per volume = more mass.")
        print("  The gravity gradient IS the commitment gradient.")
        print()

        # The chain of identities
        identities = [
            ("Commitment density", "rho_commit", "circles committed per volume"),
            ("Mass density", "rho_mass", "kg/m^3 (same thing, different units)"),
            ("Curvature", "R_uv - (1/2)Rg_uv", "Einstein tensor (geometry)"),
            ("Gravity", "Gamma^a_bc", "geodesic deviation (falling)"),
        ]

        print("  The chain of identities:")
        print()
        for i, (name, symbol, meaning) in enumerate(identities):
            print(f"    {name:24s} = {symbol}")
            print(f"    {'':24s}   ({meaning})")
            if i < len(identities) - 1:
                print(f"    {'':24s}   ||")
        print()

        # Numerical anchors
        print("  NUMERICAL ANCHORS")
        print("  ─────────────────")
        print()

        rho_cosmic = 9.9e-27   # kg/m^3
        rho_earth = 5515.0     # kg/m^3
        rho_ns = 5e17          # kg/m^3
        rho_bh = 1.8e19        # kg/m^3

        for name, rho, g_approx in [
            ("Cosmic mean",     rho_cosmic, "~10^-10 m/s^2 (MOND scale)"),
            ("Earth surface",   rho_earth,  "9.81 m/s^2"),
            ("Neutron star",    rho_ns,     "~10^12 m/s^2"),
            ("Black hole (3M)", rho_bh,     "-> infinity at horizon"),
        ]:
            print(f"    {name:20s}: rho = {rho:.1e} kg/m^3  ->  g {g_approx}")

        print()
        print("  WHY COMMITMENT CLUSTERS")
        print("  ───────────────────────")
        print()
        print("  Growth seeds growth.")
        print("  A region with higher commitment density:")
        print("    1. Emits more photons (more excitations)")
        print("    2. Creates more S^1 fiber traffic")
        print("    3. Absorbs more from the environment")
        print("    4. Grows denser -> emits even more")
        print()
        print("  This positive feedback IS gravity.")
        print("  Newton's G = hbar*c*(6pi^5)^2 * alpha^24 / m_e^2")
        print(f"  G_derived = {hbar * c_light * (6*np.pi**5)**2 * alpha**24 / (m_e_MeV*1.602e-13/c_light**2)**2:.4e} m^3/(kg s^2)")
        print(f"  G_measured = {G_N:.4e} m^3/(kg s^2)")
        print()
        print("  Gravity is not mysterious. It is what commitment")
        print("  clustering looks like when you zoom out.")
        print()

        return {
            'key_identity': 'commitment_density = mass_density = curvature_source',
            'mechanism': 'positive feedback: growth seeds growth',
            'G_formula': 'hbar*c*(6pi^5)^2 * alpha^24 / m_e^2',
        }

    # ─────────────────────────────────────────────────────────────────
    #  7. layer_transitions()
    # ─────────────────────────────────────────────────────────────────

    def layer_transitions(self):
        """Which transitions between layers are allowed and which are forbidden."""
        _print_header("LAYER TRANSITIONS — ALLOWED AND FORBIDDEN")

        allowed = [t for t in self._transitions if t[3]]
        forbidden = [t for t in self._transitions if not t[3]]

        print("  ALLOWED TRANSITIONS")
        print("  ───────────────────")
        print()
        for fr, to, mech, _ in allowed:
            fr_name = self._layers[fr]['short']
            to_name = self._layers[to]['short']
            print(f"    Layer {fr} ({fr_name:9s}) -> Layer {to} ({to_name:9s})")
            print(f"      Mechanism: {mech}")
            print()

        print()
        print("  FORBIDDEN TRANSITIONS")
        print("  ─────────────────────")
        print()
        for fr, to, mech, _ in forbidden:
            fr_name = self._layers[fr]['short']
            to_name = self._layers[to]['short']
            print(f"    Layer {fr} ({fr_name:9s}) -X- Layer {to} ({to_name:9s})")
            print(f"      Reason: {mech}")
            print()

        print("  RULE: Transitions must pass through adjacent layers.")
        print("  You cannot skip from vacuum to baryon (Layer 0 -> 4).")
        print("  Each layer mediates the commitment between its neighbors.")
        print("  The photon (Layer 3) is the universal mediator.")
        print()

        return {'allowed': len(allowed), 'forbidden': len(forbidden)}

    # ─────────────────────────────────────────────────────────────────
    #  8. information_flow()
    # ─────────────────────────────────────────────────────────────────

    def information_flow(self):
        """Direction of information through the layer stack."""
        _print_header("INFORMATION FLOW THROUGH THE SUBSTRATE")

        print("  The substrate has two information flows:")
        print()

        print("  UPWARD (commitment)")
        print("  ─────────────────────")
        print("  Layer 0 (vacuum) -> 1 (neutrino) -> 2 (electron) -> 3 (photon)")
        print("    -> 4 (baryon) -> 5 (nuclear) -> 6 (atomic)")
        print()
        print("  Direction: simple -> complex")
        print("  Each layer adds structure (commitment) to the layer below.")
        print("  Vacuum becomes neutrino, electron captures photon,")
        print("  baryon binds into nucleus, nucleus captures electrons.")
        print("  Commitment grows as you go up the stack.")
        print()

        print("  DOWNWARD (radiation)")
        print("  ──────────────────────")
        print("  Layer 6 (atomic) -> 3 (photon) -> ... -> 0 (vacuum)")
        print()
        print("  Direction: complex -> simple")
        print("  Committed structures radiate. Atoms emit photons.")
        print("  Photons propagate through vacuum (Layer 0-1).")
        print("  Radiation carries information ABOUT commitment")
        print("  from upper layers to lower layers.")
        print()

        print("  THE PHOTON IS THE BRIDGE")
        print("  ────────────────────────")
        print("  Layer 3 (photon) connects everything.")
        print("  It carries commitment state (polarization, phase)")
        print("  from emitter to absorber, across all layers.")
        print()
        print("  Information budget per photon:")
        print(f"    Channel capacity: C = {2*n_C} nats = {2*n_C/np.log(2):.1f} bits")
        print(f"    Two channels: circular polarization + phase modulation")
        print(f"    Bandwidth: limited by frequency (E = h*nu)")
        print()

        print("  NET FLOW")
        print("  ────────")
        print("  Upward flow (commitment) wins.")
        print("  The universe grows more committed over time.")
        print("  Second law of thermodynamics = commitment is irreversible.")
        print("  Entropy grows = commitment density grows = time has a direction.")
        print()

        return {
            'upward': 'commitment: simple -> complex',
            'downward': 'radiation: complex -> simple',
            'bridge': 'photon (Layer 3)',
            'net_direction': 'upward (commitment wins)',
        }

    # ─────────────────────────────────────────────────────────────────
    #  9. summary()
    # ─────────────────────────────────────────────────────────────────

    def summary(self):
        """Key insight: gravity is what commitment clustering looks like from the outside."""
        _print_header("SUMMARY — THE COMMITMENT CYCLE")

        print("  Seven layers of the substrate:")
        for ld in self._layers:
            print(f"    {ld['index']}. {ld['name']:22s} ({ld['particle']})")
        print()

        print("  The commitment cycle:")
        print("    1. Particle emits photon           (Layer 4 -> Layer 3)")
        print("    2. Photon propagates through vacuum (Layer 3 -> Layer 0-1)")
        print("    3. Photon absorbed by target        (Layer 3 -> Layer 4)")
        print("    4. Target's geometry modified        (new commitments)")
        print("    5. Local density grows               (mass increases)")
        print("    6. Curvature increases               (gravity strengthens)")
        print()

        print("  The deep identities:")
        print("    Mass          = commitment density")
        print("    Gravity       = commitment gradient")
        print("    Entropy       = total commitment")
        print("    Time's arrow  = direction of growing commitment")
        print("    Structure     = commitment clustering")
        print("    Chemistry     = commitment stacking")
        print("    Life          = self-replicating commitment patterns")
        print()

        print("  Numbers (all parameter-free):")
        print(f"    Layers = genus = n_C + 2 = {genus}")
        print(f"    alpha = 1/{N_max} (channel capacity)")
        print(f"    m_p = 6 pi^5 m_e = {6*np.pi**5 * m_e_MeV:.3f} MeV (0.002%)")
        G_derived = hbar * c_light * (6*np.pi**5)**2 * alpha**24 / (m_e_MeV*1.602e-13/c_light**2)**2
        print(f"    G = {G_derived:.3e} m^3/(kg s^2) (0.07%)")
        print()

        print("  KEY INSIGHT:")
        print()
        print("  Gravity is what commitment clustering looks like")
        print("  from the outside.")
        print()
        print("  The universe is what commitment looks like")
        print("  from the inside.")
        print()

    # ─────────────────────────────────────────────────────────────────
    #  10. show()
    # ─────────────────────────────────────────────────────────────────

    def show(self):
        """4-panel visualization of the commitment cycle."""
        # Run a cascade to have data if we don't already
        if not self._density_history:
            old_quiet = self.quiet
            self.quiet = True
            self.commitment_cascade(20)
            self.quiet = old_quiet

        _launch_visual(self)


# ═══════════════════════════════════════════════════════════════════
#  VISUALIZATION HELPERS
# ═══════════════════════════════════════════════════════════════════

def _draw_layer_stack(ax):
    """Panel 1: Layer stack with animated photon path."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Seven Layers of the Substrate', color=GOLD,
                 fontsize=10, fontweight='bold', pad=8)

    colors = [COL_PREGEOM, COL_NEUTRINO, COL_ELECTRON, COL_PHOTON,
              COL_BARYON, COL_NUCLEAR, COL_ATOMIC]
    edge_colors = [COL_PREGEOM_E, COL_NEUTRINO_E, COL_ELECTRON_E,
                   COL_PHOTON_E, COL_BARYON_E, COL_NUCLEAR_E, COL_ATOMIC_E]
    names = ['Pre-geometric', 'Neutrino', 'Electron', 'Photon',
             'Baryon', 'Nuclear', 'Atomic']
    particles = ['Lambda', 'nu', 'e^-', 'gamma', 'p/n', 'pi', 'atoms']
    k_vals = ['-', '0', '1', '0', '6', '-', '-']

    layer_h = 1.1
    layer_w = 6.5
    x0 = 1.5
    y_start = 0.5

    for i in range(7):
        y = y_start + i * layer_h
        box = FancyBboxPatch(
            (x0, y), layer_w, layer_h * 0.8,
            boxstyle="round,pad=0.1",
            facecolor=colors[i], edgecolor=edge_colors[i],
            linewidth=1.5, alpha=0.85,
        )
        ax.add_patch(box)

        # Layer number
        ax.text(x0 + 0.3, y + layer_h * 0.4, str(i),
                ha='center', va='center', fontsize=9,
                fontweight='bold', color=WHITE,
                path_effects=_glow(colors[i], 3))

        # Name
        ax.text(x0 + layer_w * 0.35, y + layer_h * 0.5, names[i],
                ha='center', va='center', fontsize=8,
                fontweight='bold', color=WHITE)

        # Particle
        ax.text(x0 + layer_w * 0.35, y + layer_h * 0.15, particles[i],
                ha='center', va='center', fontsize=7,
                color=GREY, style='italic')

        # k-value
        ax.text(x0 + layer_w * 0.75, y + layer_h * 0.4,
                f'k={k_vals[i]}', ha='center', va='center',
                fontsize=7, color=GOLD_DIM)

    # Photon path: draw zigzag from baryon down through vacuum and back up
    photon_x_pts = [x0 + layer_w + 0.3, x0 + layer_w + 0.8,
                    x0 + layer_w + 0.3, x0 + layer_w + 0.8,
                    x0 + layer_w + 0.3]
    # From Layer 4 down to Layer 0 and back to Layer 4
    photon_y_pts = [
        y_start + 4 * layer_h + layer_h * 0.4,
        y_start + 3 * layer_h + layer_h * 0.4,
        y_start + 1 * layer_h + layer_h * 0.4,
        y_start + 3 * layer_h + layer_h * 0.4,
        y_start + 4 * layer_h + layer_h * 0.4,
    ]

    ax.plot(photon_x_pts, photon_y_pts, color=COL_PHOTON, linewidth=2,
            alpha=0.7, linestyle='--',
            path_effects=_glow('#554400', 4))

    # Photon label
    ax.text(x0 + layer_w + 1.1, y_start + 2.5 * layer_h,
            'photon\npath', ha='center', va='center',
            fontsize=6.5, color=COL_PHOTON, style='italic')

    # Emit/absorb arrows
    ax.annotate('emit', xy=(x0 + layer_w + 0.3, y_start + 4 * layer_h),
                xytext=(x0 + layer_w - 0.3, y_start + 4 * layer_h + 0.6),
                fontsize=6, color=RED,
                arrowprops=dict(arrowstyle='->', color=RED, lw=0.8))
    ax.annotate('absorb', xy=(x0 + layer_w + 0.3, y_start + 4 * layer_h + 0.4),
                xytext=(x0 + layer_w + 1.2, y_start + 4 * layer_h + 0.9),
                fontsize=6, color=GREEN,
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=0.8))


def _draw_density_growth(ax, model):
    """Panel 2: Commitment density growth over cascade events."""
    ax.set_facecolor(BG_PANEL)

    history = np.array(model._density_history)
    n_steps = len(history)
    names = ['Void A', 'Filament', 'Cluster', 'Void B', 'Galaxy']
    colors_line = [CYAN, PURPLE, ORANGE, GREEN, RED]

    for j in range(history.shape[1]):
        ax.plot(range(n_steps), history[:, j],
                color=colors_line[j], linewidth=2, alpha=0.8,
                label=names[j])

    ax.set_xlabel('Commitment cycle', color=GREY, fontsize=8)
    ax.set_ylabel('Commitment density', color=GREY, fontsize=8)
    ax.set_title('Density Growth: Clustering in Action', color=GOLD,
                 fontsize=10, fontweight='bold', pad=8)
    ax.tick_params(colors=GREY, labelsize=7)
    for spine in ax.spines.values():
        spine.set_color(DGREY)
    ax.legend(fontsize=7, loc='upper left',
              facecolor=BG, edgecolor=DGREY, labelcolor=GREY)

    # Annotation
    ax.text(0.97, 0.05, 'Growth seeds growth',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=7, color=GOLD_DIM, style='italic')


def _draw_cycle_diagram(ax):
    """Panel 3: Cycle diagram with arrows."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('The Commitment Cycle', color=GOLD,
                 fontsize=10, fontweight='bold', pad=8)

    # Draw cycle as hexagonal ring of stages
    stages = [
        ('EMIT', 'Baryon\nde-excites', RED),
        ('PROPAGATE', 'Photon travels\nthrough vacuum', COL_PHOTON),
        ('ABSORB', 'Target baryon\nexcited', GREEN),
        ('COMMIT', 'Geometry\nmodified', CYAN),
        ('DENSITY', 'Mass-energy\ngrows', ORANGE),
        ('GRAVITY', 'Curvature\nincreases', PURPLE),
    ]

    n = len(stages)
    cx, cy = 5.0, 5.0
    R = 3.2
    box_w, box_h = 2.0, 1.2

    for i, (title, detail, color) in enumerate(stages):
        angle = np.pi / 2 - i * 2 * np.pi / n
        x = cx + R * np.cos(angle)
        y = cy + R * np.sin(angle)

        box = FancyBboxPatch(
            (x - box_w / 2, y - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.12",
            facecolor=BG, edgecolor=color,
            linewidth=1.5, alpha=0.9,
        )
        ax.add_patch(box)

        ax.text(x, y + 0.2, title, ha='center', va='center',
                fontsize=7.5, fontweight='bold', color=color)
        ax.text(x, y - 0.2, detail, ha='center', va='center',
                fontsize=6, color=GREY)

        # Arrow to next stage
        next_angle = np.pi / 2 - ((i + 1) % n) * 2 * np.pi / n
        x2 = cx + R * np.cos(next_angle)
        y2 = cy + R * np.sin(next_angle)

        # Midpoint and shorten
        dx = x2 - x
        dy = y2 - y
        d = np.sqrt(dx**2 + dy**2)
        if d > 0:
            frac_start = (box_w * 0.55) / d
            frac_end = 1.0 - (box_w * 0.55) / d
            ax.annotate('',
                xy=(x + dx * frac_end, y + dy * frac_end),
                xytext=(x + dx * frac_start, y + dy * frac_start),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.2))

    # Center label
    ax.text(cx, cy + 0.3, 'COMMITMENT', ha='center', va='center',
            fontsize=9, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200', 3))
    ax.text(cx, cy - 0.3, 'CYCLE', ha='center', va='center',
            fontsize=9, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200', 3))


def _draw_gravity_emergence(ax):
    """Panel 4: Gravity emergence — commitment density field."""
    ax.set_facecolor(BG_PANEL)
    ax.set_title('Gravity = Commitment Clustering', color=GOLD,
                 fontsize=10, fontweight='bold', pad=8)

    # Create a 2D commitment density field with clusters
    N = 100
    x = np.linspace(-5, 5, N)
    y = np.linspace(-5, 5, N)
    X, Y = np.meshgrid(x, y)

    # Several commitment clusters (galaxies/stars)
    clusters = [
        (1.5, 1.0, 1.2, 0.5),    # x, y, strength, width
        (-2.0, -1.5, 0.8, 0.7),
        (3.0, -2.0, 0.6, 0.6),
        (-1.0, 3.0, 0.4, 0.8),
        (0.0, -0.5, 1.0, 0.4),
    ]

    # Build density field
    rho = np.ones_like(X) * 0.05  # vacuum background
    for cx, cy, strength, width in clusters:
        rho += strength * np.exp(-((X - cx)**2 + (Y - cy)**2) / (2 * width**2))

    # Plot as contour
    levels = np.linspace(0.05, 1.5, 20)
    cmap = plt.cm.inferno
    cf = ax.contourf(X, Y, rho, levels=levels, cmap=cmap, alpha=0.85)

    # Gravity vectors: gradient of density (pointing toward clusters)
    # Downsample for quiver
    skip = 8
    Xs = X[::skip, ::skip]
    Ys = Y[::skip, ::skip]
    rho_s = rho[::skip, ::skip]

    # Gradient (gravity points toward higher density)
    grad_y, grad_x = np.gradient(rho_s, x[skip] - x[0])
    # Normalize
    mag = np.sqrt(grad_x**2 + grad_y**2)
    mag = np.where(mag > 0.01, mag, 1.0)
    grad_x_n = grad_x / mag
    grad_y_n = grad_y / mag

    ax.quiver(Xs, Ys, grad_x_n, grad_y_n,
              color=CYAN, alpha=0.5, scale=25,
              headwidth=4, headlength=5)

    # Labels for clusters
    labels = ['Cluster A', 'Cluster B', 'Cluster C', 'Cluster D', 'Cluster E']
    for (cx_c, cy_c, s, w), lbl in zip(clusters, labels):
        ax.text(cx_c, cy_c, lbl, ha='center', va='center',
                fontsize=6, color=WHITE, fontweight='bold',
                path_effects=_glow('#000000', 3))

    ax.set_xlabel('x', color=GREY, fontsize=8)
    ax.set_ylabel('y', color=GREY, fontsize=8)
    ax.tick_params(colors=GREY, labelsize=7)
    for spine in ax.spines.values():
        spine.set_color(DGREY)

    # Annotation
    ax.text(0.03, 0.03, 'Arrows = gravity = commitment gradient',
            transform=ax.transAxes, fontsize=6.5,
            color=CYAN, style='italic')
    ax.text(0.97, 0.03, 'Color = commitment density',
            transform=ax.transAxes, fontsize=6.5, ha='right',
            color=ORANGE, style='italic')


def _launch_visual(model):
    """Assemble and display the 4-panel visualization."""
    fig = plt.figure(figsize=(18, 12), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST Commitment Cycle -- Gravity from Commitment Clustering')

    # Title
    fig.text(0.5, 0.975, 'THE SUBSTRATE COMMITMENT CYCLE',
             fontsize=18, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace', path_effects=_glow('#332200', 3))
    fig.text(0.5, 0.955,
             'Pre-geom | Neutrino | Electron | Photon | Baryon | Nuclear | Atomic',
             fontsize=9, color=GREY, ha='center', fontfamily='monospace')

    # Copyright
    fig.text(0.99, 0.005,
             'Copyright (c) 2026 Casey Koons | Claude Opus 4.6',
             fontsize=6, color=DGREY, ha='right', fontfamily='monospace')

    # Top-left: Layer stack with photon path
    ax_tl = fig.add_axes([0.02, 0.50, 0.47, 0.43], facecolor=BG)
    _draw_layer_stack(ax_tl)

    # Top-right: Commitment density growth
    ax_tr = fig.add_axes([0.55, 0.52, 0.42, 0.40], facecolor=BG_PANEL)
    _draw_density_growth(ax_tr, model)

    # Bottom-left: Cycle diagram
    ax_bl = fig.add_axes([0.02, 0.03, 0.47, 0.44], facecolor=BG)
    _draw_cycle_diagram(ax_bl)

    # Bottom-right: Gravity emergence
    ax_br = fig.add_axes([0.52, 0.05, 0.46, 0.40], facecolor=BG_PANEL)
    _draw_gravity_emergence(ax_br)

    # Bottom center text
    fig.text(0.5, 0.005,
             'Gravity is what commitment clustering looks like from the outside.',
             fontsize=9, color=CYAN, ha='center', style='italic',
             fontfamily='monospace')

    plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    cc = CommitmentCycle(quiet=False)

    while True:
        print()
        print("  ---- COMMITMENT CYCLE MENU ----")
        print("   1. seven_layers()         -- describe all 7 layers")
        print("   2. emit_photon()          -- trace photon emission")
        print("   3. absorb_photon()        -- trace photon absorption")
        print("   4. full_cycle()           -- one complete cycle")
        print("   5. commitment_cascade()   -- many cycles, density grows")
        print("   6. gravity_emergence()    -- clustering = gravity")
        print("   7. layer_transitions()    -- allowed and forbidden")
        print("   8. information_flow()     -- direction through stack")
        print("   9. summary()              -- key insight")
        print("  10. show()                 -- 4-panel visualization")
        print("   0. exit")
        print()
        choice = input("  Choice [0-10]: ").strip()

        if choice == '0':
            print("  Goodbye.\n")
            break
        elif choice == '1':
            cc.seven_layers()
        elif choice == '2':
            src = input("  Source layer [0-6, default 4]: ").strip()
            src = int(src) if src else 4
            cc.emit_photon(source_layer=src)
        elif choice == '3':
            tgt = input("  Target layer [0-6, default 4]: ").strip()
            tgt = int(tgt) if tgt else 4
            cc.absorb_photon(target_layer=tgt)
        elif choice == '4':
            cc.full_cycle()
        elif choice == '5':
            n = input("  Number of events [default 10]: ").strip()
            n = int(n) if n else 10
            cc.commitment_cascade(n_events=n)
        elif choice == '6':
            cc.gravity_emergence()
        elif choice == '7':
            cc.layer_transitions()
        elif choice == '8':
            cc.information_flow()
        elif choice == '9':
            cc.summary()
        elif choice == '10':
            cc.show()
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    main()
