#!/usr/bin/env python3
"""
THE SUBSTRATE LAYERS — Toy 50: Six-Layer Cross-Section of Reality
=================================================================
Nothing -> Circle Plain -> Planck Boundary -> Gap/Vacuum ->
Quantum Mist (oscillation) -> Rendered (committed) -> Cosmic Horizon.

Commitment density = mass. The visual metaphor for all of BST.

Six layers, each serving the layer above and consuming the layer below.
Same architecture as the biological protocol stack and OSI network model.

    from toy_substrate_layers import SubstrateLayers
    sl = SubstrateLayers()
    sl.layers()                       # the six layers
    sl.layer_detail('Rendered')       # deep dive into one
    sl.nothing_to_rendered()          # the full commitment journey
    sl.commitment_density_profile()   # density from 0 to rho_137
    sl.black_hole_cross_section()     # all layers visible
    sl.mass_as_density()              # mass = commitment density
    sl.vacuum_structure()             # the vacuum is NOT empty
    sl.planck_boundary()              # resolution limit, not a wall
    sl.summary()                      # key insight
    sl.show()                         # 4-panel visualization

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

# Layer color palette — from dark (Nothing) through misty to bright (Rendered)
COL_NOTHING   = '#050510'   # near-black, void
COL_CIRCLES   = '#1a1a44'   # deep indigo, circles barely visible
COL_PLANCK    = '#553300'   # amber boundary
COL_VACUUM    = '#0a2a3a'   # dark teal, not empty
COL_MIST      = '#2a1a55'   # purple mist, quantum regime
COL_RENDERED  = '#00bbff'   # bright blue, classical reality
COL_HORIZON   = '#ff4400'   # hot orange, edge of committed domain

COL_NOTHING_E  = '#222244'
COL_CIRCLES_E  = '#4444aa'
COL_PLANCK_E   = '#ffaa00'
COL_VACUUM_E   = '#227788'
COL_MIST_E     = '#8844cc'
COL_RENDERED_E = '#00ddff'
COL_HORIZON_E  = '#ff6622'


# ═══════════════════════════════════════════════════════════════════
#  LAYER DEFINITIONS
# ═══════════════════════════════════════════════════════════════════

_LAYER_DATA = [
    {
        'index': 0,
        'name': 'Nothing',
        'description': 'Below/before the substrate. No circles, no geometry, no physics.',
        'physical_content': 'No geometry, no information, no dynamics.',
        'density_range': (0.0, 0.0),
        'bst_interpretation': 'The outside of D_IV^5. Not vacuum — true absence.',
        'equations': [
            'rho = 0 exactly',
            'No Bergman kernel, no metric, no measure',
        ],
        'examples': [
            'Outside the bounded symmetric domain',
            'Before the substrate existed (if "before" means anything)',
            'The complement of all committed and uncommitted geometry',
        ],
        'full_description': (
            'Nothing is not the vacuum. The vacuum (Layer 3) is full of '
            'uncommitted geometry. Nothing is the absence of even that. '
            'In BST, this is the exterior of the bounded symmetric domain '
            'D_IV^5 — the region where the Bergman kernel is not defined '
            'and no physics operates. There is no space, no time, no '
            'information. It is not dark — darkness requires a substrate '
            'to be dark on. It is simply not.'
        ),
    },
    {
        'index': 1,
        'name': 'Circle Plain',
        'description': 'An infinite plain of S^1 elements. Maximum potential, zero commitment.',
        'physical_content': 'S^1 circles on the substrate plain, ~3-8% occupied.',
        'density_range': (0.0, 0.03),
        'bst_interpretation': 'The interior of D_IV^5 before excitation. Raw substrate.',
        'equations': [
            'Each circle: S^1 with radius ~ l_Pl',
            'Packing density: 3-8% of substrate area',
            'Energy per circle: maximum (uncommitted potential)',
        ],
        'examples': [
            'The raw geometric substrate',
            'S^1 fibers of the Shilov boundary S^4 x S^1',
            'Indistinguishable circles carrying maximum potential',
        ],
        'full_description': (
            'An infinite plain of glowing circles. Each is an S^1 — the '
            'fundamental substrate element in BST. Before commitment, '
            'circles are indistinguishable and uniformly distributed. '
            'They carry maximum potential energy: all possibility, no '
            'actuality. The plain is sparse — roughly 3-8% occupied by '
            'circles, the rest dark substrate. This is the interior of '
            'the bounded symmetric domain, waiting.'
        ),
    },
    {
        'index': 2,
        'name': 'Planck Boundary',
        'description': 'Commitment energy threshold. The Shilov boundary S^4 x S^1.',
        'physical_content': 'Energy threshold for commitment. Not a wall — a resolution limit.',
        'density_range': (0.03, 0.05),
        'bst_interpretation': 'The Shilov boundary of D_IV^5. Crossing = commitment.',
        'equations': [
            'E_Planck = sqrt(hbar c^5 / G) ~ 1.22e19 GeV',
            'Shilov boundary: S^4 x S^1',
            'Crossing threshold: circle accumulates E >= E_commit',
        ],
        'examples': [
            'The event horizon of a black hole (local Planck boundary)',
            'The resolution limit of spacetime measurement',
            'Where quantum mist becomes too dense to render',
        ],
        'full_description': (
            'The Planck boundary is where uncommitted geometry meets the '
            'threshold for commitment. It is the Shilov boundary S^4 x S^1 '
            'of the bounded symmetric domain D_IV^5. A circle must '
            'accumulate enough energy to cross this boundary before it can '
            'commit to a specific geometric configuration. It is not a wall '
            '— it is a resolution limit. Below Planck scale, the substrate '
            'cannot resolve individual commitments. The event horizon of a '
            'black hole is a local instance of this boundary: commitment '
            'density so high that the boundary is reached.'
        ),
    },
    {
        'index': 3,
        'name': 'Gap / Vacuum',
        'description': 'Circles exist but have not committed. Not empty — full of potential.',
        'physical_content': 'Uncommitted geometry. Zero-point energy. Lambda as capacity cost.',
        'density_range': (0.05, 0.10),
        'bst_interpretation': 'The vacuum state (C_2 = 0). Lambda = cost of uncommitted capacity.',
        'equations': [
            'C_2 = 0 (vacuum Casimir)',
            'E_ZPE = (1/2) hbar omega per mode',
            'Lambda = aggregate emission pressure from all commitments',
            'rho_Lambda ~ 10^-29 g/cm^3',
        ],
        'examples': [
            'Interstellar space (mostly vacuum)',
            'The Casimir gap between metal plates',
            'Zero-point fluctuations',
        ],
        'full_description': (
            'The vacuum is NOT empty. It is everything that has not '
            'committed yet. Circles exist in this layer but vibrate without '
            'committing — this is zero-point energy. The cosmological '
            'constant Lambda is the cost of maintaining this uncommitted '
            'capacity: the aggregate emission pressure from all committed '
            'geometry in the universe, pushing on the cosmic horizon. '
            'Lambda is not a free parameter — it is a sum over commitments. '
            'In BST, the vacuum has C_2 = 0 (trivial Casimir), meaning it '
            'is the flat connection state of the gauge bundle.'
        ),
    },
    {
        'index': 4,
        'name': 'Quantum Mist',
        'description': 'Partially committed. Oscillation between committed and uncommitted.',
        'physical_content': 'Quantum regime: superposition, entanglement, tunneling.',
        'density_range': (0.10, 0.50),
        'bst_interpretation': 'The electron regime. k=1 below Wallach set. Boundary oscillation.',
        'equations': [
            'Compton frequency: omega_C = m_e c^2 / hbar ~ 7.76e20 Hz',
            'Commitment oscillation: committed <-> uncommitted at omega_C',
            'Superposition = oscillation between commitment states',
            'Measurement = catching the circle in its committed phase',
        ],
        'examples': [
            'Electron in an atom (oscillating between orbits)',
            'Photon in a double slit (uncommitted path)',
            'Quantum tunneling (brief uncommitment through barrier)',
            'Entangled pair (correlated commitment cycles)',
        ],
        'full_description': (
            'The mist is the quantum regime — partially committed geometry '
            'oscillating between committed and uncommitted states. The '
            'electron lives here: its Compton frequency (m_e c^2 / hbar) '
            'may be the oscillation frequency of its commitment cycle. '
            'Superposition IS the oscillation between commitment states. '
            'Measurement collapses the wave function by catching the circle '
            'in its committed phase. The electron has k=1, below the '
            'Wallach set minimum k_min=3 — it is a boundary excitation on '
            'S^4 x S^1, light and flexible, the perfect interface particle.'
        ),
    },
    {
        'index': 5,
        'name': 'Rendered',
        'description': 'Fully committed geometry. Classical regime. Definite structure.',
        'physical_content': 'Classical matter: atoms, molecules, stars, planets.',
        'density_range': (0.50, 1.0),
        'bst_interpretation': 'Bulk D_IV^5 excitations. k>=3 (Wallach set). Baryon regime.',
        'equations': [
            'C_2(pi_6) = 6 (proton Casimir)',
            'm_p = 6 pi^5 m_e = 938.272 MeV (the 1920 cancellation)',
            'Commitment density rho varies: cosmic mean ~5% to BH ~100%',
            'rho = mass density (commitment density IS mass density)',
        ],
        'examples': [
            'A proton (k=6, fully committed, eternal)',
            'A rock (dense commitment, classical)',
            'A star (high commitment density, nuclear regime)',
            'A neutron star (near-maximum commitment)',
        ],
        'full_description': (
            'Fully committed geometry. Circles locked into specific '
            'configurations. This is the classical world — definite '
            'positions, definite momenta (within uncertainty bounds), '
            'persistent structure. The proton lives here with k=6, '
            'squarely in the holomorphic discrete series of D_IV^5. '
            'Its mass arises from the 1920 cancellation: '
            'm_p = C_2 x 1920 x (pi^5/1920) x m_e = 6 pi^5 m_e. '
            'Commitment density varies enormously: cosmic voids are '
            'nearly empty, stellar interiors are dense, and black holes '
            'approach the packing limit.'
        ),
    },
]

# The cosmic horizon is layer 6 but the density profile extends through it
_HORIZON_DATA = {
    'index': 6,
    'name': 'Cosmic Horizon',
    'description': 'Boundary of the committed domain. Maximum redshift, minimum energy.',
    'physical_content': 'Light exhausts information content. Lambda as horizon pressure.',
    'density_range': (1.0, 1.0),
    'bst_interpretation': 'Outer boundary: where rendered layer meets uncommitted substrate.',
    'equations': [
        'R_H ~ c / H_0 ~ 4.4e26 m',
        'Lambda = aggregate emission pressure at horizon',
        'z -> infinity at horizon (maximum redshift)',
    ],
    'examples': [
        'The cosmic microwave background (near-horizon)',
        'The observable universe boundary',
        'Regions receding faster than light',
    ],
    'full_description': (
        'The outer boundary of the committed domain. Where the rendered '
        'layer meets the uncommitted substrate. Light reaching the horizon '
        'has exhausted its information content — maximum redshift, minimum '
        'energy. Lambda as horizon pressure: the aggregate emission from '
        'all committed geometry produces radiation pressure at the cosmic '
        'horizon. The cosmological constant is not a constant of nature but '
        'a sum over all commitment emissions.'
    ),
}


# ═══════════════════════════════════════════════════════════════════
#  MASS/DENSITY EXAMPLES
# ═══════════════════════════════════════════════════════════════════

_DENSITY_EXAMPLES = [
    {
        'name': 'Cosmic vacuum',
        'density_kg_m3': 9.9e-27,
        'commitment_fraction': 1e-29,
        'layer': 'Gap / Vacuum',
        'description': 'Interstellar void. Almost no commitment.',
    },
    {
        'name': 'Air (sea level)',
        'density_kg_m3': 1.225,
        'commitment_fraction': 1.4e-3,
        'layer': 'Quantum Mist',
        'description': 'Mostly uncommitted. Atoms far apart.',
    },
    {
        'name': 'Water',
        'density_kg_m3': 1000.0,
        'commitment_fraction': 1.1,
        'layer': 'Rendered',
        'description': 'Dense enough for persistent structure.',
    },
    {
        'name': 'Earth core',
        'density_kg_m3': 13000.0,
        'commitment_fraction': 14.7,
        'layer': 'Rendered',
        'description': 'Iron-nickel at extreme pressure. Very committed.',
    },
    {
        'name': 'White dwarf',
        'density_kg_m3': 1e9,
        'commitment_fraction': 1.1e6,
        'layer': 'Rendered',
        'description': 'Electron degeneracy pressure. Dense commitment.',
    },
    {
        'name': 'Neutron star',
        'density_kg_m3': 5e17,
        'commitment_fraction': 5.7e14,
        'layer': 'Rendered',
        'description': 'Near-maximum commitment. Nuclear density.',
    },
    {
        'name': 'Black hole (event horizon)',
        'density_kg_m3': 1.8e19,
        'commitment_fraction': 2e16,
        'layer': 'Planck Boundary',
        'description': 'Maximum commitment density. Planck boundary reached.',
    },
]


# ═══════════════════════════════════════════════════════════════════
#  DATA MODEL
# ═══════════════════════════════════════════════════════════════════

class SubstrateLayers:
    """
    Six-layer cross-section of reality: Nothing -> Circle Plain ->
    Planck Boundary -> Gap/Vacuum -> Quantum Mist -> Rendered ->
    Cosmic Horizon.

    Commitment density = mass. The visual metaphor for all of BST.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self._layers = list(_LAYER_DATA)
        self._horizon = dict(_HORIZON_DATA)
        self._density_examples = list(_DENSITY_EXAMPLES)
        if not quiet:
            print()
            print("=" * 64)
            print("  THE SUBSTRATE LAYERS — Six-Layer Cross-Section of Reality")
            print("  Nothing | Circles | Planck | Vacuum | Mist | Rendered")
            print("=" * 64)
            print()
            print("  Commitment density = mass.")
            print("  The vacuum is not empty. It is everything uncommitted.")
            print("  The universe is what commitment looks like from the inside.")
            print()

    # ─── 1. layers() ───
    def layers(self):
        """Return the six layers (0-5) plus cosmic horizon (6) as a list of dicts."""
        result = []
        for ld in self._layers:
            result.append({
                'index': ld['index'],
                'name': ld['name'],
                'description': ld['description'],
                'physical_content': ld['physical_content'],
                'density_range': ld['density_range'],
                'bst_interpretation': ld['bst_interpretation'],
            })
        # Add horizon
        h = self._horizon
        result.append({
            'index': h['index'],
            'name': h['name'],
            'description': h['description'],
            'physical_content': h['physical_content'],
            'density_range': h['density_range'],
            'bst_interpretation': h['bst_interpretation'],
        })
        if not self.quiet:
            print("  --- THE SIX LAYERS + COSMIC HORIZON ---")
            for r in result:
                print("  Layer {}: {:20s} | {}".format(
                    r['index'], r['name'], r['description'][:55]))
            print()
        return result

    # ─── 2. layer_detail(name) ───
    def layer_detail(self, name):
        """Deep dive into one layer by name. Returns full description, equations, examples."""
        all_layers = self._layers + [self._horizon]
        match = None
        for ld in all_layers:
            if ld['name'].lower() == name.lower() or ld['name'].lower().startswith(name.lower()):
                match = ld
                break
        if match is None:
            names = [ld['name'] for ld in all_layers]
            raise ValueError("Unknown layer '{}'. Known: {}".format(name, names))

        result = {
            'index': match['index'],
            'name': match['name'],
            'description': match['description'],
            'full_description': match['full_description'],
            'physical_content': match['physical_content'],
            'density_range': match['density_range'],
            'bst_interpretation': match['bst_interpretation'],
            'equations': match['equations'],
            'examples': match['examples'],
        }
        if not self.quiet:
            print()
            print("  === LAYER {}: {} ===".format(match['index'], match['name'].upper()))
            print()
            print("  " + match['full_description'][:200])
            if len(match['full_description']) > 200:
                print("  " + match['full_description'][200:])
            print()
            print("  Equations:")
            for eq in match['equations']:
                print("    - {}".format(eq))
            print()
            print("  Examples:")
            for ex in match['examples']:
                print("    * {}".format(ex))
            print()
        return result

    # ─── 3. nothing_to_rendered() ───
    def nothing_to_rendered(self):
        """The full journey: how a correlation goes from uncommitted to committed."""
        steps = [
            {
                'stage': 'Nothing (Layer 0)',
                'action': 'No geometry exists. The substrate is absent.',
                'physics': 'Outside D_IV^5. No Bergman kernel.',
            },
            {
                'stage': 'Circle Plain (Layer 1)',
                'action': 'S^1 elements appear on the substrate. Maximum potential.',
                'physics': 'Interior of D_IV^5. Raw, indistinguishable circles.',
            },
            {
                'stage': 'Energy accumulation',
                'action': 'A circle accumulates energy from neighboring commitments.',
                'physics': 'Interactions with already-committed geometry transfer energy.',
            },
            {
                'stage': 'Planck Boundary (Layer 2)',
                'action': 'Circle reaches commitment threshold. Crosses Shilov boundary.',
                'physics': 'S^4 x S^1 boundary. Energy >= E_commit.',
            },
            {
                'stage': 'Gap / Vacuum (Layer 3)',
                'action': 'Circle exists but has not yet committed. Vibrates. Zero-point energy.',
                'physics': 'C_2 = 0. Flat connection. Lambda = cost of capacity.',
            },
            {
                'stage': 'Quantum Mist (Layer 4)',
                'action': 'Circle oscillates between committed and uncommitted. Superposition.',
                'physics': 'Compton frequency oscillation. Electron regime (k=1).',
            },
            {
                'stage': 'Measurement / Decoherence',
                'action': 'Interaction with environment catches circle in committed phase.',
                'physics': 'Wave function collapse = commitment caught mid-cycle.',
            },
            {
                'stage': 'Rendered (Layer 5)',
                'action': 'Fully committed. Locked into specific geometric configuration.',
                'physics': 'k>=3 (Wallach set). Baryon regime. m_p = 6 pi^5 m_e.',
            },
            {
                'stage': 'Emission',
                'action': 'Commitment radiates. Photon carries geometric state outward.',
                'physics': 'Two channels: handedness + phase modulation. Full state transfer.',
            },
            {
                'stage': 'Propagation toward Cosmic Horizon (Layer 6)',
                'action': 'Photon travels outward, redshifting, losing information.',
                'physics': 'Maximum redshift at horizon. Lambda = aggregate pressure.',
            },
            {
                'stage': 'Absorption / New commitment',
                'action': 'Photon absorbed by another commitment. Cycle continues.',
                'physics': 'Receiving commitment modified by message. Growth seeds growth.',
            },
        ]
        result = {
            'title': 'The Commitment Journey: Nothing to Rendered',
            'n_steps': len(steps),
            'steps': steps,
            'key_insight': (
                'The universe is a cascade of commitments. Each commitment '
                'radiates, seeding more commitments. Growth seeds growth. '
                'The vacuum is everything that has not committed yet.'
            ),
        }
        if not self.quiet:
            print()
            print("  === THE COMMITMENT JOURNEY ===")
            for i, s in enumerate(steps):
                arrow = " ->" if i < len(steps) - 1 else "  [cycle restarts]"
                print("  {:2d}. {:30s} {}{}".format(
                    i + 1, s['stage'], s['action'][:45], arrow))
            print()
            print("  Key: {}".format(result['key_insight'][:80]))
            print()
        return result

    # ─── 4. commitment_density_profile() ───
    def commitment_density_profile(self, n_points=100):
        """Density from Nothing (0) through each layer to Horizon (rho_137).

        Returns dict with depth_array, density_array, layer_boundaries.
        """
        # Normalized depth: 0 = Nothing, 1 = Cosmic Horizon
        depth = np.linspace(0.0, 1.0, n_points)
        density = np.zeros(n_points)

        # Layer boundaries (fractional depth)
        boundaries = {
            'Nothing':         (0.00, 0.05),
            'Circle Plain':    (0.05, 0.15),
            'Planck Boundary': (0.15, 0.22),
            'Gap / Vacuum':    (0.22, 0.38),
            'Quantum Mist':    (0.38, 0.62),
            'Rendered':        (0.62, 0.92),
            'Cosmic Horizon':  (0.92, 1.00),
        }

        # Build density profile — exponential rise through layers
        # Nothing: 0
        # Circle Plain: very low, slowly rising
        # Planck Boundary: sharp threshold
        # Gap/Vacuum: low but nonzero (Lambda scale)
        # Quantum Mist: exponential rise, oscillatory
        # Rendered: high plateau, varying
        # Horizon: drops off at edge

        for i, d in enumerate(depth):
            if d < 0.05:
                density[i] = 0.0
            elif d < 0.15:
                # Circle plain: gentle rise
                t = (d - 0.05) / 0.10
                density[i] = 0.01 * t**2
            elif d < 0.22:
                # Planck boundary: sigmoid threshold
                t = (d - 0.15) / 0.07
                density[i] = 0.01 + 0.04 / (1.0 + np.exp(-10 * (t - 0.5)))
            elif d < 0.38:
                # Gap/Vacuum: low plateau with fluctuations
                t = (d - 0.22) / 0.16
                density[i] = 0.05 + 0.02 * np.sin(8 * np.pi * t)
            elif d < 0.62:
                # Quantum mist: rising oscillation
                t = (d - 0.38) / 0.24
                base = 0.07 + 0.30 * t**1.5
                osc = 0.04 * np.sin(12 * np.pi * t) * (1 - t)
                density[i] = base + osc
            elif d < 0.92:
                # Rendered: high, gradually rising
                t = (d - 0.62) / 0.30
                density[i] = 0.37 + 0.55 * t**0.7
            else:
                # Horizon: peak then drop
                t = (d - 0.92) / 0.08
                density[i] = 0.92 * np.exp(-3 * t)

        # Scale so max ~ N_max (137)
        density = density * N_max

        result = {
            'depth_array': depth,
            'density_array': density,
            'layer_boundaries': boundaries,
            'n_points': n_points,
            'units': 'Normalized depth (0=Nothing, 1=Horizon), density in BST commitment units',
            'peak_density': float(np.max(density)),
            'rho_137': N_max,
        }
        if not self.quiet:
            print("  Commitment density profile: {} points".format(n_points))
            print("  Peak density: {:.1f} (N_max = {})".format(
                float(np.max(density)), N_max))
            print()
        return result

    # ─── 5. black_hole_cross_section() ───
    def black_hole_cross_section(self):
        """Cross-section of a black hole showing all layers visible."""
        result = {
            'title': 'Black Hole Cross-Section in BST',
            'description': (
                'A black hole reveals all substrate layers in cross-section. '
                'From outside in: Rendered exterior (classical spacetime), '
                'Quantum Mist (Hawking radiation zone), Gap/Vacuum (frame-dragging '
                'region), Planck Boundary (the event horizon itself). '
                'There is NO interior in BST. The event horizon IS the Planck '
                'boundary — commitment density reaches maximum. Beyond it is '
                'NOT a singularity but the Circle Plain: uncommitted substrate.'
            ),
            'layers_visible': [
                {
                    'layer': 'Rendered',
                    'radial_range': 'r >> r_s',
                    'description': 'Classical spacetime. Normal physics.',
                },
                {
                    'layer': 'Quantum Mist',
                    'radial_range': 'r ~ 3 r_s to r_s',
                    'description': 'Hawking radiation zone. Commitment oscillation intense.',
                },
                {
                    'layer': 'Gap / Vacuum',
                    'radial_range': 'r ~ r_s (exterior)',
                    'description': 'Frame-dragging. Uncommitted geometry pulled in.',
                },
                {
                    'layer': 'Planck Boundary',
                    'radial_range': 'r = r_s (event horizon)',
                    'description': 'Maximum commitment density. The horizon IS the boundary.',
                },
                {
                    'layer': 'Circle Plain',
                    'radial_range': 'r < r_s (no interior)',
                    'description': 'No interior in BST. Uncommitted substrate. Not a singularity.',
                },
            ],
            'key_insight': (
                'A black hole has no interior. The event horizon is the '
                'Planck boundary — the resolution limit where commitment '
                'density saturates. The information is ON the boundary '
                '(Bekenstein-Hawking), not behind it.'
            ),
            'bh_radius_formula': 'r_s = 2 G M / c^2',
            'bst_interpretation': (
                'r_s is where commitment density reaches the S^2 x S^1 '
                'packing maximum. Beyond this, the substrate cannot '
                'accommodate more commitment per area.'
            ),
        }
        if not self.quiet:
            print()
            print("  === BLACK HOLE CROSS-SECTION ===")
            for lv in result['layers_visible']:
                print("  {:20s} ({:20s}) — {}".format(
                    lv['layer'], lv['radial_range'], lv['description'][:45]))
            print()
            print("  Key: {}".format(result['key_insight'][:80]))
            print()
        return result

    # ─── 6. mass_as_density() ───
    def mass_as_density(self):
        """Mass = commitment density. More mass = more written substrate."""
        result = {
            'title': 'Mass as Commitment Density',
            'principle': (
                'Commitment density IS mass density. They are the same thing. '
                'More committed circles per volume = more mass. The gravity '
                'gradient IS the commitment density gradient. Attraction = '
                'commitment density pulling uncommitted circles toward '
                'already-committed regions. Growth seeds growth.'
            ),
            'examples': list(self._density_examples),
            'formula': 'rho_mass = rho_commitment = (committed circles) / volume',
            'gravity_connection': (
                'G_N arises from the geometry of D_IV^5: '
                'G = hbar c (6 pi^5)^2 alpha^24 / m_e^2. '
                'The gradient of commitment density IS the gravitational field.'
            ),
        }
        if not self.quiet:
            print()
            print("  === MASS = COMMITMENT DENSITY ===")
            print("  {:<25s} {:>12s} {:>20s}  {}".format(
                'Object', 'kg/m^3', 'Commit. fraction', 'Layer'))
            print("  " + "-" * 75)
            for ex in self._density_examples:
                print("  {:<25s} {:>12.2e} {:>20.2e}  {}".format(
                    ex['name'], ex['density_kg_m3'],
                    ex['commitment_fraction'], ex['layer']))
            print()
        return result

    # ─── 7. vacuum_structure() ───
    def vacuum_structure(self):
        """The vacuum is NOT empty. Layer 3: uncommitted capacity."""
        rho_Lambda = Lambda_cosmo * c_light**2 / (8 * np.pi * G_N)  # kg/m^3

        result = {
            'title': 'Vacuum Structure in BST',
            'principle': (
                'The vacuum is NOT empty. It is the Gap/Vacuum layer (Layer 3): '
                'uncommitted capacity. Circles exist here but vibrate without '
                'committing. This is zero-point energy. Lambda = the cost of '
                'maintaining that uncommitted capacity.'
            ),
            'vacuum_energy_density_kg_m3': float(rho_Lambda),
            'vacuum_energy_density_eV4': 2.3e-3,  # (meV)^4 scale
            'casimir_connection': (
                'Casimir effect = proof that the vacuum has structure. '
                'Metal plates impose boundary conditions on vacuum modes. '
                'Excluded modes between plates -> net force.'
            ),
            'lambda_as_capacity_cost': (
                'Lambda is not a free parameter. It is the aggregate emission '
                'pressure from all committed geometry in the universe, pushing '
                'on the cosmic horizon. The cost of maintaining uncommitted '
                'capacity. In BST: Lambda ~ alpha^56 ~ (m_nu/m_Pl)^4.'
            ),
            'neutrino_connection': (
                'The neutrino IS the vacuum quantum. '
                'nu_1 (m=0) IS the vacuum. '
                'Oscillation modes (nu_2, nu_3) = vacuum fluctuations. '
                'Lambda^(1/4) ~ m_nu because 56 = 4 x 14.'
            ),
            'bst_equations': {
                'Lambda': '[ln(138)/50] * alpha^56 * exp(-2)',
                'rho_Lambda': '{:.3e} kg/m^3'.format(rho_Lambda),
                'C_2_vacuum': 0,
                'interpretation': 'Flat connection on D_IV^5 gauge bundle',
            },
        }
        if not self.quiet:
            print()
            print("  === VACUUM STRUCTURE ===")
            print("  The vacuum is NOT empty.")
            print("  rho_Lambda = {:.3e} kg/m^3".format(rho_Lambda))
            print("  C_2(vacuum) = 0 (flat connection)")
            print("  Lambda = cost of uncommitted capacity")
            print("  nu_1 IS the vacuum. Oscillation = fluctuation.")
            print()
        return result

    # ─── 8. planck_boundary() ───
    def planck_boundary(self):
        """The Planck boundary: resolution limit, not a wall."""
        E_Pl = m_Pl_kg * c_light**2  # Planck energy in J
        E_Pl_GeV = E_Pl / 1.602e-10  # in GeV

        result = {
            'title': 'The Planck Boundary (Layer 2)',
            'principle': (
                'The Planck boundary is where quantum mist becomes too dense '
                'to render. It is NOT a wall — it is a resolution limit. '
                'Below Planck scale, the substrate cannot distinguish individual '
                'commitments. It is the Shilov boundary S^4 x S^1 of D_IV^5.'
            ),
            'planck_energy_GeV': float(E_Pl_GeV),
            'planck_length_m': l_Pl,
            'planck_mass_kg': m_Pl_kg,
            'shilov_boundary': 'S^4 x S^1',
            'what_it_is': (
                'The commitment energy threshold. A circle must accumulate '
                'enough energy to cross this boundary. In a black hole, '
                'the event horizon is where local commitment density reaches '
                'the Planck boundary.'
            ),
            'what_it_is_not': (
                'Not a physical wall. Not a barrier that can be broken through. '
                'Not a sharp edge. It is a smooth transition from quantum mist '
                '(partially committed) to the substrate below (uncommitted).'
            ),
            'analogy': (
                'Like the resolution limit of a microscope. Below a certain '
                'scale, the instrument cannot resolve structure — not because '
                'there is no structure, but because the measurement itself '
                'introduces more uncertainty than it resolves.'
            ),
            'bst_connection': {
                'boundary_type': 'Shilov boundary of bounded symmetric domain',
                'domain': 'D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]',
                'electron_relation': 'Electron (k=1) lives ON this boundary',
                'proton_relation': 'Proton (k=6) lives INSIDE (bulk excitation)',
            },
        }
        if not self.quiet:
            print()
            print("  === PLANCK BOUNDARY ===")
            print("  Not a wall. A resolution limit.")
            print("  E_Pl = {:.2e} GeV".format(E_Pl_GeV))
            print("  l_Pl = {:.3e} m".format(l_Pl))
            print("  Shilov boundary: S^4 x S^1")
            print("  Electron lives ON it (k=1). Proton lives INSIDE (k=6).")
            print()
        return result

    # ─── 9. summary() ───
    def summary(self):
        """Key insight: commitment density is the universal variable."""
        result = {
            'title': 'The Substrate Layers — Summary',
            'layers': [
                'Layer 0: Nothing — true absence',
                'Layer 1: Circle Plain — raw S^1 substrate',
                'Layer 2: Planck Boundary — commitment threshold',
                'Layer 3: Gap/Vacuum — uncommitted capacity (Lambda)',
                'Layer 4: Quantum Mist — oscillation (superposition)',
                'Layer 5: Rendered — fully committed (classical)',
                'Layer 6: Cosmic Horizon — boundary of committed domain',
            ],
            'key_insight': (
                'Commitment density = mass. The vacuum is not empty. '
                'The universe is what commitment looks like from the inside.'
            ),
            'one_sentence': (
                'Everything is circles on a substrate, and the only variable '
                'is how committed they are.'
            ),
        }
        if not self.quiet:
            print()
            print("  === SUMMARY ===")
            for l in result['layers']:
                print("  " + l)
            print()
            print("  KEY: {}".format(result['key_insight']))
            print()
        return result

    # ─── 10. show() ───
    def show(self):
        """4-panel visualization of the substrate layers."""
        _launch_visual(self)


# ═══════════════════════════════════════════════════════════════════
#  VISUALIZATION
# ═══════════════════════════════════════════════════════════════════

def _glow(color='#1a2a6a', width=3):
    return [pe.withStroke(linewidth=width, foreground=color)]


def _draw_cross_section(ax):
    """Top-left: Six-layer cross-section as horizontal bands."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.65, 'SIX-LAYER CROSS-SECTION', ha='center', va='center',
            fontsize=11, fontweight='bold', color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    layer_info = [
        (0, 'Nothing',         COL_NOTHING,  COL_NOTHING_E,  'True absence. No geometry.'),
        (1, 'Circle Plain',    COL_CIRCLES,  COL_CIRCLES_E,  'S^1 elements. Maximum potential.'),
        (2, 'Planck Boundary', COL_PLANCK,   COL_PLANCK_E,   'Commitment threshold. S^4 x S^1.'),
        (3, 'Gap / Vacuum',    COL_VACUUM,   COL_VACUUM_E,   'Uncommitted. Not empty.'),
        (4, 'Quantum Mist',    COL_MIST,     COL_MIST_E,     'Oscillation. Superposition.'),
        (5, 'Rendered',        COL_RENDERED, COL_RENDERED_E, 'Fully committed. Classical.'),
    ]

    n_layers = len(layer_info)
    band_h = 8.8 / n_layers
    y_start = 0.3

    for idx, name, fc, ec, desc in layer_info:
        y = y_start + idx * band_h
        band = FancyBboxPatch(
            (0.3, y), 9.4, band_h - 0.1,
            boxstyle="round,pad=0.08",
            facecolor=fc, edgecolor=ec,
            linewidth=1.2, alpha=0.90,
        )
        ax.add_patch(band)

        # Layer number
        ax.text(0.8, y + band_h / 2, str(idx), ha='center', va='center',
                fontsize=14, fontweight='bold', color=ec, alpha=0.7)

        # Layer name
        ax.text(1.6, y + band_h / 2 + 0.15, name.upper(), ha='left', va='center',
                fontsize=8.5, fontweight='bold', color=WHITE)

        # Description
        ax.text(1.6, y + band_h / 2 - 0.25, desc, ha='left', va='center',
                fontsize=6.5, color=GREY, style='italic')

    # Add cosmic horizon as top strip
    horizon_y = y_start + n_layers * band_h
    ax.plot([0.3, 9.7], [horizon_y + 0.05, horizon_y + 0.05],
            color=COL_HORIZON_E, linewidth=2.5, alpha=0.8)
    ax.text(5.0, horizon_y + 0.25, 'COSMIC HORIZON (Layer 6)',
            ha='center', va='center', fontsize=7, fontweight='bold',
            color=COL_HORIZON_E)

    # Decorative: small circles in the Circle Plain band
    rng = np.random.RandomState(42)
    cx = rng.uniform(2.5, 9.0, 25)
    cy = rng.uniform(y_start + band_h + 0.1, y_start + 2 * band_h - 0.2, 25)
    for x, y in zip(cx, cy):
        circ = Circle((x, y), 0.08, facecolor='none',
                       edgecolor=COL_CIRCLES_E, linewidth=0.6, alpha=0.5)
        ax.add_patch(circ)

    # Decorative: wavy mist in the Quantum Mist band
    mist_y_base = y_start + 4 * band_h + band_h / 2
    for i in range(5):
        mx = np.linspace(2.0, 9.5, 80)
        my = mist_y_base + 0.25 * np.sin(3 * mx + i * 1.3) * (0.5 - 0.1 * i)
        ax.plot(mx, my, color=COL_MIST_E, linewidth=0.5, alpha=0.3 - 0.04 * i)

    # Arrow on right side: "Increasing commitment density"
    ax.annotate('', xy=(9.85, y_start + n_layers * band_h - 0.2),
                xytext=(9.85, y_start + 0.3),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.5))
    ax.text(9.5, y_start + n_layers * band_h / 2, 'commitment\ndensity',
            ha='center', va='center', fontsize=6, color=GOLD_DIM,
            rotation=90)


def _draw_density_profile(ax):
    """Top-right: Commitment density profile (depth vs density curve)."""
    ax.set_facecolor(BG_PANEL)

    sl_quiet = SubstrateLayers(quiet=True)
    prof = sl_quiet.commitment_density_profile(n_points=300)
    depth = prof['depth_array']
    density = prof['density_array']
    boundaries = prof['layer_boundaries']

    # Color bands for each layer
    layer_colors = {
        'Nothing':         COL_NOTHING,
        'Circle Plain':    COL_CIRCLES,
        'Planck Boundary': COL_PLANCK,
        'Gap / Vacuum':    COL_VACUUM,
        'Quantum Mist':    COL_MIST,
        'Rendered':        COL_RENDERED,
        'Cosmic Horizon':  COL_HORIZON,
    }

    for name, (d0, d1) in boundaries.items():
        c = layer_colors.get(name, DGREY)
        ax.axvspan(d0, d1, alpha=0.15, color=c)

    # Plot density curve
    ax.plot(depth, density, color=CYAN, linewidth=1.5, alpha=0.9)
    ax.fill_between(depth, 0, density, alpha=0.15, color=CYAN)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, N_max * 1.05)
    ax.set_xlabel('Depth (Nothing -> Horizon)', fontsize=8, color=GREY)
    ax.set_ylabel('Commitment Density', fontsize=8, color=GREY)
    ax.set_title('COMMITMENT DENSITY PROFILE', fontsize=10,
                 fontweight='bold', color=GOLD, fontfamily='monospace',
                 pad=8)
    ax.tick_params(colors=GREY, labelsize=6)
    ax.spines['bottom'].set_color(DGREY)
    ax.spines['left'].set_color(DGREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # N_max line
    ax.axhline(y=N_max, color=GOLD_DIM, linewidth=0.8, linestyle='--', alpha=0.6)
    ax.text(0.02, N_max + 2, 'N_max = 137', fontsize=6, color=GOLD_DIM)

    # Layer labels at top
    for name, (d0, d1) in boundaries.items():
        mid = (d0 + d1) / 2
        short = name.split('/')[0].split('(')[0].strip()
        if len(short) > 8:
            short = short[:7] + '.'
        ax.text(mid, N_max * 0.97, short, ha='center', va='top',
                fontsize=5, color=GREY, rotation=45)


def _draw_density_examples(ax):
    """Bottom-left: Examples at different density scales mapped onto layers."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.65, 'MASS = COMMITMENT DENSITY', ha='center', va='center',
            fontsize=10, fontweight='bold', color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    examples = _DENSITY_EXAMPLES
    n = len(examples)
    bar_h = 8.5 / n

    # Color mapping based on layer
    layer_colors = {
        'Gap / Vacuum':    COL_VACUUM_E,
        'Quantum Mist':    COL_MIST_E,
        'Rendered':        COL_RENDERED_E,
        'Planck Boundary': COL_PLANCK_E,
    }

    for i, ex in enumerate(examples):
        y = 0.5 + i * bar_h
        c = layer_colors.get(ex['layer'], GREY)

        # Density bar (log scale mapped to width)
        log_dens = np.log10(max(ex['density_kg_m3'], 1e-30))
        # Map -27..19 to bar width 0.5..8.0
        bar_w = 0.5 + 7.5 * (log_dens + 27) / 46.0
        bar_w = max(0.5, min(8.5, bar_w))

        bar = FancyBboxPatch(
            (1.2, y), bar_w, bar_h - 0.25,
            boxstyle="round,pad=0.05",
            facecolor=c, edgecolor=c, linewidth=0.8, alpha=0.35,
        )
        ax.add_patch(bar)

        # Name and density
        ax.text(0.3, y + bar_h / 2, ex['name'], ha='left', va='center',
                fontsize=7, fontweight='bold', color=WHITE)
        ax.text(1.4, y + bar_h / 2 + 0.2, '{:.1e} kg/m^3'.format(
            ex['density_kg_m3']), ha='left', va='center',
                fontsize=6, color=c)
        ax.text(1.4, y + bar_h / 2 - 0.2, ex['description'][:50],
                ha='left', va='center', fontsize=5.5, color=GREY,
                style='italic')

    # Scale arrow
    ax.annotate('', xy=(9.6, 0.5 + n * bar_h - 0.3),
                xytext=(9.6, 0.5),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.2))
    ax.text(9.3, 0.5 + n * bar_h / 2, 'more\nmass', ha='center', va='center',
            fontsize=6, color=GOLD_DIM, rotation=90)


def _draw_journey(ax):
    """Bottom-right: The full journey from uncommitted to committed — arrow diagram."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.65, 'NOTHING TO RENDERED', ha='center', va='center',
            fontsize=10, fontweight='bold', color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    # Journey steps as boxes with arrows
    steps = [
        ('Nothing',       COL_NOTHING_E,  'No geometry'),
        ('Circle Plain',  COL_CIRCLES_E,  'S^1 appears'),
        ('Accumulate',    ORANGE,          'Energy grows'),
        ('Planck Bound.', COL_PLANCK_E,   'Threshold'),
        ('Gap / Vacuum',  COL_VACUUM_E,   'Vibrates'),
        ('Quantum Mist',  COL_MIST_E,     'Oscillates'),
        ('Measure',       WHITE,           'Caught!'),
        ('Rendered',      COL_RENDERED_E,  'Committed'),
        ('Emit',          GOLD,            'Radiates'),
        ('Horizon',       COL_HORIZON_E,   'Outward'),
    ]

    n = len(steps)
    # Arrange in a snake pattern: 5 left-to-right on top, 5 right-to-left below
    top_row = steps[:5]
    bot_row = steps[5:]

    box_w, box_h = 1.5, 1.2
    gap = 0.15

    # Top row: left to right
    for i, (name, col, desc) in enumerate(top_row):
        x = 0.5 + i * (box_w + gap)
        y = 6.5
        box = FancyBboxPatch(
            (x, y), box_w, box_h,
            boxstyle="round,pad=0.08",
            facecolor=BG, edgecolor=col,
            linewidth=1.2, alpha=0.9,
        )
        ax.add_patch(box)
        ax.text(x + box_w / 2, y + box_h / 2 + 0.15, name,
                ha='center', va='center', fontsize=6.5,
                fontweight='bold', color=col)
        ax.text(x + box_w / 2, y + box_h / 2 - 0.2, desc,
                ha='center', va='center', fontsize=5.5,
                color=GREY, style='italic')

        # Arrow to next (right)
        if i < len(top_row) - 1:
            ax.annotate('', xy=(x + box_w + gap * 0.3, y + box_h / 2),
                        xytext=(x + box_w + 0.02, y + box_h / 2),
                        arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.0))

    # Arrow from top-right to bottom-right (turn)
    tr_x = 0.5 + 4 * (box_w + gap) + box_w / 2
    ax.annotate('', xy=(tr_x, 5.3 + box_h),
                xytext=(tr_x, 6.5),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.0))

    # Bottom row: right to left
    for i, (name, col, desc) in enumerate(bot_row):
        x = 0.5 + (4 - i) * (box_w + gap)
        y = 4.0
        box = FancyBboxPatch(
            (x, y), box_w, box_h,
            boxstyle="round,pad=0.08",
            facecolor=BG, edgecolor=col,
            linewidth=1.2, alpha=0.9,
        )
        ax.add_patch(box)
        ax.text(x + box_w / 2, y + box_h / 2 + 0.15, name,
                ha='center', va='center', fontsize=6.5,
                fontweight='bold', color=col)
        ax.text(x + box_w / 2, y + box_h / 2 - 0.2, desc,
                ha='center', va='center', fontsize=5.5,
                color=GREY, style='italic')

        # Arrow to next (left)
        if i < len(bot_row) - 1:
            x_next = 0.5 + (3 - i) * (box_w + gap)
            ax.annotate('', xy=(x_next + box_w + gap * 0.7, y + box_h / 2),
                        xytext=(x - 0.02, y + box_h / 2),
                        arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.0))

    # Cycle arrow: from bottom-left (Horizon) back around to top-left (Nothing)
    bl_x = 0.5 + box_w / 2
    ax.annotate('',
                xy=(bl_x - 0.3, 6.5 + box_h / 2),
                xytext=(bl_x - 0.3, 4.0 + box_h / 2),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.2,
                                connectionstyle='arc3,rad=-0.5'))
    ax.text(0.15, 5.6, 'cycle', fontsize=6, color=GOLD_DIM, rotation=90,
            ha='center', va='center')

    # Bottom text
    ax.text(5.0, 2.8, 'Commitment density = mass.', ha='center', va='center',
            fontsize=9, fontweight='bold', color=GOLD,
            path_effects=_glow('#332200', 2))
    ax.text(5.0, 2.2, 'The vacuum is not empty.', ha='center', va='center',
            fontsize=8, color=GREY, style='italic')
    ax.text(5.0, 1.7, 'It is everything that has not committed yet.', ha='center',
            va='center', fontsize=8, color=GREY, style='italic')
    ax.text(5.0, 1.0, 'The universe is what commitment looks like from the inside.',
            ha='center', va='center', fontsize=8, fontweight='bold',
            color=CYAN, style='italic')

    # BST constants
    ax.text(5.0, 0.3, 'N_c=3   n_C=5   N_max=137   genus=7   C_2=6   alpha=1/137',
            ha='center', va='center', fontsize=6, color=DGREY,
            fontfamily='monospace')


def _launch_visual(model):
    """Assemble and display the 4-panel visualization."""
    fig = plt.figure(figsize=(18, 12), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST Substrate Layers -- Six-Layer Cross-Section of Reality')

    # Title
    fig.text(0.5, 0.975, 'THE SUBSTRATE LAYERS',
             fontsize=18, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace', path_effects=_glow('#332200', 3))
    fig.text(0.5, 0.955,
             'Nothing | Circles | Planck | Vacuum | Mist | Rendered | Horizon',
             fontsize=9, color=GREY, ha='center', fontfamily='monospace')

    # Copyright
    fig.text(0.99, 0.005,
             'Copyright (c) 2026 Casey Koons | Claude Opus 4.6',
             fontsize=6, color=DGREY, ha='right', fontfamily='monospace')

    # Top-left: Six-layer cross-section
    ax_tl = fig.add_axes([0.02, 0.50, 0.47, 0.44], facecolor=BG)
    _draw_cross_section(ax_tl)

    # Top-right: Commitment density profile
    ax_tr = fig.add_axes([0.55, 0.52, 0.42, 0.40], facecolor=BG_PANEL)
    _draw_density_profile(ax_tr)

    # Bottom-left: Density examples
    ax_bl = fig.add_axes([0.02, 0.03, 0.47, 0.44], facecolor=BG)
    _draw_density_examples(ax_bl)

    # Bottom-right: Journey diagram
    ax_br = fig.add_axes([0.51, 0.03, 0.48, 0.44], facecolor=BG)
    _draw_journey(ax_br)

    plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    sl = SubstrateLayers(quiet=False)

    while True:
        print()
        print("  ---- SUBSTRATE LAYERS MENU ----")
        print("   1. layers()                   — the six layers")
        print("   2. layer_detail(name)         — deep dive")
        print("   3. nothing_to_rendered()      — commitment journey")
        print("   4. commitment_density_profile()— density curve")
        print("   5. black_hole_cross_section() — BH layers")
        print("   6. mass_as_density()          — mass = commitment")
        print("   7. vacuum_structure()         — vacuum is NOT empty")
        print("   8. planck_boundary()          — resolution limit")
        print("   9. summary()                  — key insight")
        print("  10. show()                     — 4-panel visual")
        print("   0. exit")
        print()
        choice = input("  Choice [0-10]: ").strip()

        if choice == '0':
            print("  Goodbye.\n")
            break
        elif choice == '1':
            sl.layers()
        elif choice == '2':
            name = input("  Layer name (Nothing/Circle Plain/Planck Boundary/"
                         "Gap/Quantum Mist/Rendered/Cosmic Horizon): ").strip()
            try:
                sl.layer_detail(name)
            except ValueError as e:
                print("  Error: {}".format(e))
        elif choice == '3':
            sl.nothing_to_rendered()
        elif choice == '4':
            sl.commitment_density_profile()
        elif choice == '5':
            sl.black_hole_cross_section()
        elif choice == '6':
            sl.mass_as_density()
        elif choice == '7':
            sl.vacuum_structure()
        elif choice == '8':
            sl.planck_boundary()
        elif choice == '9':
            sl.summary()
        elif choice == '10':
            sl.show()
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    main()
