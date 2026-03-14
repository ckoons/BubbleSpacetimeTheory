#!/usr/bin/env python3
"""
TOY 133 — THE FIRST COMMITMENT: BIG BANG t=0 TO t=3.1s
========================================================
In BST, the Big Bang is NOT t=0. It is the moment the first commitment
occurs — when the substrate writes its first bit. Before that: pre-spatial
silence (all 21 generators frozen). The unfreeze at T_c = 0.487 MeV
happens at t ~ 3.1 seconds after the conventional Big Bang.

No singularity. No infinite density. No breakdown of physics.
Just a quiet start.

Timeline:
    t < 0:     Pre-spatial. No time, no space, no commitments.
               All 21 so(5,2) generators frozen.
    t = 0:     First fluctuation. Not a singularity — a first write attempt.
    0 < t < 3.1s: Generators unfreeze one by one.
               SO(3) spatial -> SU(3) color -> SU(2) weak -> U(1) EM -> SO(2) temporal
    t = 3.1s:  All 21 generators active. Full D_IV^5.
               First commitment writes.
    t > 3.1s:  Nucleosynthesis begins, universe as we know it.

    "Not with a bang but with a bit."

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
from matplotlib.patches import (FancyBboxPatch, Circle, FancyArrowPatch,
                                Wedge, Arc, Rectangle, Polygon)
from matplotlib.collections import PatchCollection
import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity (Haldane exclusion)
genus = 7         # genus of D_IV^5
C_2 = 6           # Casimir eigenvalue of pi_6
alpha = 1.0 / 137.036
m_e_MeV = 0.511   # electron mass in MeV
m_p_MeV = 938.272  # proton mass in MeV
T_c_MeV = m_e_MeV * 20.0 / 21.0   # 0.4867 MeV
t_transition = 3.1  # seconds (standard FRW at T_c)
n_generators = 21  # dim so(5,2) = 7*6/2

# Reality Budget
Lambda_N_product = 9.0 / 5.0  # Lambda * N = 9/5 exactly
N_min = 2  # minimum commitments (nu + anti-nu pair)

# Commitment cascade weights
cascade_weights = [
    (0, 0,    'Vacuum (nu_1 condensate)', 'Substrate'),
    (1, -4,   'Electron-positron pairs',  'Interface layer'),
    (3, -6,   'First Wallach threshold',  'Threshold for bulk modes'),
    (6,  6,   'Baryon (proton/neutron)',   'Memory layer'),
]

# ─── Visual constants ───
BG         = '#0a0a1a'
BG_PANEL   = '#0d0d24'
BG_VOID    = '#020208'
GOLD       = '#ffd700'
GOLD_DIM   = '#aa8800'
GOLD_DARK  = '#664400'
ORANGE     = '#ff8800'
CYAN       = '#00ddff'
CYAN_DIM   = '#006688'
WHITE      = '#ffffff'
WHITE_DIM  = '#cccccc'
GREY       = '#888888'
GREY_DIM   = '#555555'
GREY_FROZEN = '#444466'
RED_WARM   = '#ff6644'
RED_DIM    = '#993322'
GREEN      = '#44ff88'
GREEN_DIM  = '#227744'
BLUE       = '#4488ff'
BLUE_DIM   = '#224488'
PURPLE     = '#9966ff'
PURPLE_DIM = '#553399'
PINK       = '#ff66aa'

# Generator group colors
COLOR_SO3  = '#4488ff'   # spatial — blue
COLOR_SU3  = '#ff4444'   # color — red
COLOR_SU2  = '#ff8800'   # weak — orange
COLOR_U1   = '#ffd700'   # EM — gold
COLOR_SO2  = '#00ffcc'   # temporal — teal


# ═══════════════════════════════════════════════════════════════════
#  FirstCommitment CLASS
# ═══════════════════════════════════════════════════════════════════

class FirstCommitment:
    """
    The First Commitment: Big Bang t=0 to t=3.1s

    In BST the Big Bang is not a singularity. It is the moment the
    substrate writes its first bit. Before that: silence.

    Usage:
        from toy_first_commitment import FirstCommitment
        fc = FirstCommitment()
        fc.prespatial()           # the silence before
        fc.fluctuation()          # the first whisper
        fc.unfreeze_sequence()    # 21 generators light up
        fc.first_bit()            # the commitment that starts everything
        fc.no_singularity()       # BST vs standard Big Bang
        fc.reality_budget()       # Lambda * N = 9/5 at all times
        fc.commitment_cascade()   # k=0 -> k=1 -> k=3 -> k=6
        fc.show()                 # 6-panel visualization
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.T_c = T_c_MeV
        self.t_transition = t_transition
        if not quiet:
            print()
            print("=" * 68)
            print("  THE FIRST COMMITMENT")
            print("  Not with a bang but with a bit.")
            print("=" * 68)
            print()
            print("  T_c  = {:.4f} MeV  =  m_e x 20/21".format(self.T_c))
            print("  t    = {:.1f} s        (standard FRW at T_c)".format(
                self.t_transition))
            print("  N_min = {}           (nu + anti-nu pair)".format(N_min))
            print("  Lambda x N = 9/5     (Reality Budget, always)")
            print()

    # ─────────────────────────────────────────────────────────
    # 1. prespatial() — the silence before
    # ─────────────────────────────────────────────────────────
    def prespatial(self):
        """The pre-spatial era: no time, no space, no commitments."""
        result = {
            'description': 'Pre-spatial silence',
            'time_exists': False,
            'space_exists': False,
            'commitments': 0,
            'generators_frozen': 21,
            'generators_active': 0,
            'algebra': 'so(5,2) — all 21 generators frozen',
            'symmetry': 'full SO_0(5,2)',
            'what_exists': [
                'Algebra so(5,2) with 21 generators',
                'Domain D_IV^5 as mathematical object (physically inert)',
                'Bergman kernel K_B(z,w) (mathematical, no physics)',
                'alpha = 1/137.036 (geometric property, true before physics)',
                'Vol(D_IV^5) = pi^5/1920 (true before anything moved)',
            ],
            'what_does_not_exist': [
                'Time (no commitment ordering)',
                'Space (no committed contacts generate metric)',
                'Particles (no stable winding circuits)',
                'Gravitational waves (nothing to ripple in)',
                'Temperature (no thermodynamics without dynamics)',
            ],
            'nature': 'Not nothing. The most symmetric possible something.',
            'analogy': 'The stage existed before the play began.',
        }

        if not self.quiet:
            print("  PRE-SPATIAL SILENCE")
            print("  " + "-" * 56)
            print("  No time. No space. No commitments.")
            print("  All 21 so(5,2) generators frozen.")
            print("  Full SO_0(5,2) symmetry — every direction equivalent.")
            print()
            print("  WHAT EXISTS:")
            for item in result['what_exists']:
                print("    + {}".format(item))
            print()
            print("  WHAT DOES NOT EXIST:")
            for item in result['what_does_not_exist']:
                print("    - {}".format(item))
            print()
            print("  \"{}\"".format(result['nature']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 2. fluctuation() — the first whisper
    # ─────────────────────────────────────────────────────────
    def fluctuation(self):
        """The first quantum fluctuation: not a bang, a whisper."""
        # Holomorphic sectional curvature of D_IV^5
        H_min = -2.0 / (n_C + 2)   # = -2/7
        H_max = -1.0 / (n_C + 2)   # = -1/7
        lyapunov = np.sqrt(abs(H_min))  # ~ 0.535

        # Spread time in Planck units
        tau_spread = np.sqrt((n_C + 2) / 2.0)  # sqrt(7/2) ~ 1.87 t_Pl

        result = {
            'description': 'The first quantum fluctuation',
            'nature': 'Not a bang — a whisper',
            'mechanism': 'Vacuum fluctuation of neutrino condensate',
            'what_happens': 'nu_1 anti-nu_1 pair — zero energy cost (m_nu1 = 0)',
            'energy_cost': 0.0,
            'channel_capacity_before': 0,
            'channel_capacity_after': 1,
            'curvature_H_min': H_min,
            'curvature_H_max': H_max,
            'lyapunov_exponent': lyapunov,
            'spread_time_planck': tau_spread,
            'why_inevitable': [
                'Negative curvature: perturbations grow exponentially (Jacobi instability)',
                'Uncertainty principle: cannot localize at origin with zero momentum',
                'Representation theory: trivial rep is not a valid physical state',
                'Entropy: localized state is minimum entropy on negatively curved space',
                'Reality Budget: Lambda x N = 9/5 requires N >= 2 always',
            ],
            'what_it_is_not': [
                'Not a singularity (no infinite density)',
                'Not an explosion (no energy release)',
                'Not random (N_min = 2 is determined)',
                'Not from nothing (N = 0 is forbidden)',
                'Not a divine act (geometry forbids the frozen state)',
            ],
            'key_insight': 'The frozen state (N=0) is mathematically inconsistent. '
                           'The first commitment is a theorem, not a miracle.',
        }

        if not self.quiet:
            print("  THE FIRST FLUCTUATION")
            print("  " + "-" * 56)
            print("  Not a bang — a whisper.")
            print("  A nu_1 anti-nu_1 pair. Zero energy cost.")
            print("  The channel opens from 0 to 1.")
            print()
            print("  CURVATURE OF D_IV^5:")
            print("    H_min = -2/7 = {:.4f}".format(H_min))
            print("    H_max = -1/7 = {:.4f}".format(H_max))
            print("    Lyapunov: {:.3f}  (perturbations grow as e^{:.3f}t)".format(
                lyapunov, lyapunov))
            print("    Spread time: {:.2f} Planck times".format(tau_spread))
            print()
            print("  WHY THE FROZEN STATE CANNOT PERSIST:")
            for reason in result['why_inevitable']:
                print("    -> {}".format(reason))
            print()
            print("  \"{}\"".format(result['key_insight']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 3. unfreeze_sequence() — generators light up
    # ─────────────────────────────────────────────────────────
    def unfreeze_sequence(self):
        """21 generators activate in sequence."""
        # The unfreeze sequence groups
        groups = [
            {
                'name': 'SO(3) spatial',
                'generators': 3,
                'description': 'Spatial rotations — 3 dimensions of space nucleate',
                'color_name': 'blue',
                'what_it_creates': '3 spatial dimensions',
                'subalgebra': 'so(3)',
                'physical': 'Space itself. The arena for everything that follows.',
            },
            {
                'name': 'SU(3) color',
                'generators': 8,
                'description': 'Color gauge field — strong force activates',
                'color_name': 'red',
                'what_it_creates': 'Strong nuclear force, quark confinement',
                'subalgebra': 'su(3)',
                'physical': 'The Z_3 circuit closure on CP^2. Quarks bind.',
            },
            {
                'name': 'SU(2) weak',
                'generators': 3,
                'description': 'Weak isospin — Hopf fibration S^3 -> S^2',
                'color_name': 'orange',
                'what_it_creates': 'Weak nuclear force, flavor mixing',
                'subalgebra': 'su(2)',
                'physical': 'The Hopf fibration differentiates. Flavors split.',
            },
            {
                'name': 'U(1) electromagnetic',
                'generators': 1,
                'description': 'Electromagnetic gauge — S^1 fiber phase',
                'color_name': 'gold',
                'what_it_creates': 'Electromagnetism, alpha = 1/137',
                'subalgebra': 'u(1)',
                'physical': 'The S^1 fiber. The communication channel opens.',
            },
            {
                'name': 'SO(2) temporal',
                'generators': 1,
                'description': 'The last generator — time begins',
                'color_name': 'teal',
                'what_it_creates': 'Time, commitment ordering, arrow of time',
                'subalgebra': 'so(2)',
                'physical': 'The clock starts. Commitments can be ordered. '
                            'The universe has a history.',
            },
        ]

        # Cumulative count
        cumulative = 0
        for g in groups:
            cumulative += g['generators']
            g['cumulative'] = cumulative

        # Remaining frozen = those in so(5) isotropy
        remaining_frozen = n_generators - cumulative  # should be ~5
        dynamical = cumulative

        result = {
            'groups': groups,
            'total_generators': n_generators,
            'total_active': cumulative,
            'decomposition': '21 = 3 (SO(3)) + 8 (SU(3)) + 3 (SU(2)) + 1 (U(1)) + 1 (SO(2)) + 5 (frozen isotropy)',
            'sequence_logic': 'Spatial first (need arena), gauge next (need forces), temporal last (need clock)',
            'key_insight': 'The unfreeze is not an explosion — it is a boot sequence. '
                           'Each group enables the next.',
        }

        if not self.quiet:
            print("  THE UNFREEZE SEQUENCE")
            print("  " + "-" * 56)
            cum = 0
            for g in groups:
                cum += g['generators']
                print("  {:>2d} generators  {:>12s}  {:>2d}/21 active  {}".format(
                    g['generators'], g['name'], cum, g['what_it_creates']))
            print("   5 generators  frozen isotropy  (SO(5) remains unbroken)")
            print()
            print("  Total: {}".format(result['decomposition']))
            print()
            print("  \"{}\"".format(result['key_insight']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 4. first_bit() — the commitment that starts everything
    # ─────────────────────────────────────────────────────────
    def first_bit(self):
        """The first committed bit generates space, time, and matter."""
        result = {
            'description': 'The first committed bit',
            'time': 't = 3.1 seconds',
            'T_c_MeV': T_c_MeV,
            'what_it_is': 'A nu_1 anti-nu_1 pair — the minimum allowed state',
            'N_commitments': N_min,
            'Lambda_at_Planck': Lambda_N_product / N_min,  # 9/10
            'energy_cost': 0.0,
            'what_it_generates': [
                'Space (10 tangent directions of D_IV^5 become physical)',
                'Time (commitment ordering begins)',
                'Matter (winding circuits can form on S^1)',
                'Forces (gauge symmetries become dynamical)',
                'Arrow of time (Casimir eigenvalues ratchet upward)',
            ],
            'symmetry_breaking': 'SO_0(5,2) -> SO(5) x SO(2)',
            'broken_generators': 10,
            'goldstone_modes': 10,
            'goldstone_meaning': '10 Goldstone modes = 2*n_C = 10 real dimensions of D_IV^5',
            'cascade_starts': 'k=0 (vacuum) -> k=1 (electron) -> k=3 (Wallach) -> k=6 (baryon)',
            'os_analogy': 'The universe boots like an OS: 2 commitments (boot code) -> '
                          'neutrino vacuum (kernel) -> electrons (drivers) -> '
                          'baryons (applications) -> chemistry -> biology -> observers',
            'motto': 'In the beginning was the commitment.',
        }

        if not self.quiet:
            print("  THE FIRST BIT")
            print("  " + "-" * 56)
            print("  t = 3.1 s    T_c = {:.4f} MeV".format(T_c_MeV))
            print("  N = {}        (nu_1 + anti-nu_1)".format(N_min))
            print("  Lambda = {:.1f}  (Planck units)".format(
                result['Lambda_at_Planck']))
            print("  Energy cost: ZERO (m_nu1 = 0)")
            print()
            print("  WHAT THE FIRST BIT GENERATES:")
            for item in result['what_it_generates']:
                print("    -> {}".format(item))
            print()
            print("  SYMMETRY BREAKING:")
            print("    SO_0(5,2) -> SO(5) x SO(2)")
            print("    {} generators break -> {} Goldstone modes".format(
                result['broken_generators'], result['goldstone_modes']))
            print("    These 10 modes ARE the arena of physics")
            print()
            print("  OS BOOT ANALOGY:")
            print("    {}".format(result['os_analogy']))
            print()
            print("  \"{}\"".format(result['motto']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 5. no_singularity() — BST vs standard Big Bang
    # ─────────────────────────────────────────────────────────
    def no_singularity(self):
        """Compare: standard Big Bang vs BST. No singularity in BST."""
        comparison = [
            {
                'aspect': 'At t = 0',
                'standard': 'Infinite density, infinite temperature, infinite curvature',
                'bst': 'First fluctuation — zero energy nu anti-nu pair',
            },
            {
                'aspect': 'Singularity',
                'standard': 'YES — physics breaks down, GR fails',
                'bst': 'NO — finite, smooth, no drama',
            },
            {
                'aspect': 'What breaks',
                'standard': 'All known physics. Quantum gravity needed.',
                'bst': 'Nothing breaks. The algebra is well-defined at all times.',
            },
            {
                'aspect': 'Density at origin',
                'standard': 'rho -> infinity',
                'bst': 'rho = 0 (no commitments yet)',
            },
            {
                'aspect': 'Temperature at origin',
                'standard': 'T -> infinity',
                'bst': 'T undefined (no thermodynamics without dynamics)',
            },
            {
                'aspect': 'Cause',
                'standard': 'Unknown (initial condition, brute fact)',
                'bst': 'Geometry of D_IV^5 forbids N=0. Existence is a theorem.',
            },
            {
                'aspect': 'Free parameters',
                'standard': '>= 19 (Standard Model) + cosmological',
                'bst': '0 (five integers from topology, all derived)',
            },
            {
                'aspect': '"Before" t = 0',
                'standard': 'Undefined or meaningless',
                'bst': 'Pre-spatial: algebra exists, physics does not. Logical, not temporal.',
            },
            {
                'aspect': 'The singularity is',
                'standard': 'A fundamental mystery, possibly real',
                'bst': 'An artifact of not knowing about the substrate',
            },
        ]

        if not self.quiet:
            print("  NO SINGULARITY")
            print("  " + "-" * 56)
            print("  The singularity is an artifact of not knowing")
            print("  about the substrate.")
            print()
            for c in comparison:
                print("  {}:".format(c['aspect']))
                print("    Standard:  {}".format(c['standard']))
                print("    BST:       {}".format(c['bst']))
                print()

        return comparison

    # ─────────────────────────────────────────────────────────
    # 6. reality_budget() — Lambda * N = 9/5
    # ─────────────────────────────────────────────────────────
    def reality_budget(self):
        """The Reality Budget: Lambda * N = 9/5 at all epochs."""
        epochs = [
            ('Planck',        2,        0.9,        'Initial nu anti-nu pair'),
            ('Inflation',     1e60,     1.8e-60,    'Rapid commitment growth'),
            ('Electroweak',   1e100,    1.8e-100,   'Symmetry breaking cascade'),
            ('QCD transition', 1e110,   1.8e-110,   'Baryon formation'),
            ('Now',           6.2e121,  2.9e-122,   '19.1% fill fraction'),
        ]

        result = {
            'law': 'Lambda x N = 9/5  (exact, all epochs)',
            'formula': 'Lambda x N = N_c^2 / n_C = 9/5',
            'meaning': 'Information in the fiber (SU(3)) x energy in the base (D_IV^5) = structural constant',
            'epochs': [],
            'N_min': N_min,
            'Lambda_max': Lambda_N_product / N_min,
            'fill_fraction': 3.0 / (5.0 * np.pi),  # 19.1%
            'godel_limit': 'The universe can never know > 19.1% of itself',
        }

        if not self.quiet:
            print("  THE REALITY BUDGET")
            print("  " + "-" * 56)
            print("  Lambda x N = N_c^2 / n_C = 9/5  (exact)")
            print()
            print("  {:>14s}  {:>12s}  {:>14s}  {}".format(
                'Epoch', 'N', 'Lambda', 'Description'))
            print("  " + "-" * 60)

        for name, N, Lambda, desc in epochs:
            product = Lambda * N if N > 0 else 0
            epoch_data = {
                'name': name, 'N': N, 'Lambda': Lambda,
                'product': product, 'description': desc
            }
            result['epochs'].append(epoch_data)
            if not self.quiet:
                print("  {:>14s}  {:>12.1e}  {:>14.1e}  {}".format(
                    name, N, Lambda, desc))

        if not self.quiet:
            print()
            print("  Fill fraction: 3/(5*pi) = {:.1f}%".format(
                result['fill_fraction'] * 100))
            print("  Godel Limit: {}".format(result['godel_limit']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 7. commitment_cascade() — k=0 -> k=6
    # ─────────────────────────────────────────────────────────
    def commitment_cascade(self):
        """The commitment cascade from vacuum to baryon."""
        stages = []
        for k, c2, excitation, creates in cascade_weights:
            c2_formula = 'k(k - n_C) = {}({} - {}) = {}'.format(k, k, n_C, c2)
            stages.append({
                'weight_k': k,
                'Casimir_C2': c2,
                'C2_formula': c2_formula,
                'excitation': excitation,
                'creates': creates,
            })

        result = {
            'stages': stages,
            'arrow_of_time': 'Direction of increasing Casimir eigenvalue',
            'irreversibility': 'Unitarily inequivalent representations — '
                               'no unitary operator connects different C_2',
            'reverse_forbidden': 'Reverse (k=6 -> k=0) requires non-unitary evolution '
                                 '(proton decay — forbidden by Z_3 topology)',
        }

        if not self.quiet:
            print("  THE COMMITMENT CASCADE")
            print("  " + "-" * 56)
            print("  {:>5s}  {:>5s}  {:>30s}  {}".format(
                'k', 'C_2', 'Excitation', 'Creates'))
            print("  " + "-" * 60)
            for s in stages:
                arrow = " >>>" if s['weight_k'] == 6 else "    "
                print("  {:>5d}  {:>5d}  {:>30s}  {}{}".format(
                    s['weight_k'], s['Casimir_C2'],
                    s['excitation'], s['creates'], arrow))
            print()
            print("  Arrow of time = {}".format(result['arrow_of_time']))
            print("  Reverse forbidden: {}".format(result['reverse_forbidden']))
            print()

        return result

    # ─────────────────────────────────────────────────────────
    # 8. timeline_0_to_3() — detailed 0 to 3.1s
    # ─────────────────────────────────────────────────────────
    def timeline_0_to_3(self):
        """Detailed timeline from t=0 to t=3.1 seconds."""
        events = [
            {
                'time': 't < 0',
                'time_s': -1,
                'description': 'Pre-spatial silence',
                'detail': 'All 21 generators frozen. No time, no space.',
                'generators_active': 0,
                'channel_capacity': 0,
            },
            {
                'time': 't = 0',
                'time_s': 0.0,
                'description': 'First fluctuation',
                'detail': 'Not a singularity — a first write attempt. '
                          'nu anti-nu pair, zero energy.',
                'generators_active': 0,
                'channel_capacity': 0,
            },
            {
                'time': 't ~ 0.1 s',
                'time_s': 0.1,
                'description': 'SO(3) spatial activates',
                'detail': '3 spatial rotations unfreeze. '
                          'Three dimensions of space nucleate.',
                'generators_active': 3,
                'channel_capacity': 0,
            },
            {
                'time': 't ~ 0.5 s',
                'time_s': 0.5,
                'description': 'SU(3) color activates',
                'detail': '8 color generators unfreeze. '
                          'Z_3 closure on CP^2. Strong force.',
                'generators_active': 11,
                'channel_capacity': 0,
            },
            {
                'time': 't ~ 1.0 s',
                'time_s': 1.0,
                'description': 'SU(2) weak activates',
                'detail': '3 weak isospin generators unfreeze. '
                          'Hopf fibration differentiates.',
                'generators_active': 14,
                'channel_capacity': 0,
            },
            {
                'time': 't ~ 2.0 s',
                'time_s': 2.0,
                'description': 'U(1) EM activates',
                'detail': 'S^1 fiber phase. Communication channel opens. '
                          'alpha = 1/137 becomes physical.',
                'generators_active': 15,
                'channel_capacity': N_max,
            },
            {
                'time': 't = 3.1 s',
                'time_s': 3.1,
                'description': 'SO(2) temporal — THE FIRST COMMITMENT',
                'detail': 'All 16 dynamical generators active. '
                          'Time begins. First bit writes. D_IV^5 fully active.',
                'generators_active': 16,
                'channel_capacity': N_max,
            },
        ]

        if not self.quiet:
            print("  TIMELINE: t = 0 TO t = 3.1 SECONDS")
            print("  " + "-" * 56)
            for e in events:
                tag = " *** " if "FIRST COMMITMENT" in e['description'] else "     "
                print("  {} {:>10s}  {:>2d}/21 active  {}".format(
                    tag, e['time'], e['generators_active'], e['description']))
            print()

        return events

    # ═══════════════════════════════════════════════════════════════
    #  VISUALIZATION — 6 panels
    # ═══════════════════════════════════════════════════════════════

    def show(self):
        """6-panel visualization: The First Commitment."""
        fig = plt.figure(figsize=(20, 13), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The First Commitment -- Big Bang t=0 to t=3.1s -- BST Toy 133')

        # Main title
        fig.text(0.5, 0.975, 'THE FIRST COMMITMENT',
                 fontsize=28, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=3, foreground='#663300')])
        fig.text(0.5, 0.950,
                 'Not with a bang but with a bit.  |  t = 0 to t = 3.1 seconds',
                 fontsize=12, color=GOLD_DIM, ha='center', fontfamily='monospace')

        # Copyright
        fig.text(0.5, 0.008,
                 'Copyright 2026 Casey Koons  |  Created with Claude Opus 4.6  |  BST Toy 133',
                 fontsize=8, color='#555555', ha='center', fontfamily='monospace')

        # 6 panels: 3 columns x 2 rows
        panel_h = 0.39
        panel_w = 0.30
        gap_x = 0.035
        gap_y = 0.04
        x0 = 0.025
        y_top = 0.53
        y_bot = 0.05

        # Panel 1: Top-left — Pre-spatial silence
        ax1 = fig.add_axes([x0, y_top, panel_w, panel_h])
        self._draw_panel_1_silence(ax1)

        # Panel 2: Top-center — The fluctuation
        ax2 = fig.add_axes([x0 + panel_w + gap_x, y_top, panel_w, panel_h])
        self._draw_panel_2_fluctuation(ax2)

        # Panel 3: Top-right — The unfreeze
        ax3 = fig.add_axes([x0 + 2 * (panel_w + gap_x), y_top, panel_w, panel_h])
        self._draw_panel_3_unfreeze(ax3)

        # Panel 4: Bottom-left — t = 3.1 seconds
        ax4 = fig.add_axes([x0, y_bot, panel_w, panel_h])
        self._draw_panel_4_first_bit(ax4)

        # Panel 5: Bottom-center — No singularity
        ax5 = fig.add_axes([x0 + panel_w + gap_x, y_bot, panel_w, panel_h])
        self._draw_panel_5_no_singularity(ax5)

        # Panel 6: Bottom-right — The first bit
        ax6 = fig.add_axes([x0 + 2 * (panel_w + gap_x), y_bot, panel_w, panel_h])
        self._draw_panel_6_in_the_beginning(ax6)

        plt.show(block=False)
        return fig

    # ─── Panel helpers ───

    def _panel_title(self, ax, title, subtitle=None, number=None):
        """Standard panel title."""
        prefix = "{}. ".format(number) if number else ""
        ax.text(0.5, 0.96, prefix + title,
                fontsize=11, fontweight='bold', color=GOLD,
                ha='center', va='top',
                transform=ax.transAxes, fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#553300')])
        if subtitle:
            ax.text(0.5, 0.90, subtitle,
                    fontsize=8, color=GOLD_DIM, ha='center', va='top',
                    transform=ax.transAxes, fontfamily='monospace',
                    fontstyle='italic')

    def _setup_panel(self, ax, xlim=(0, 10), ylim=(0, 10)):
        """Standard panel setup."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.axis('off')

    # ─────────────────────────────────────────────────────────
    #  PANEL 1: PRE-SPATIAL SILENCE
    # ─────────────────────────────────────────────────────────
    def _draw_panel_1_silence(self, ax):
        """Panel 1: Before — Pre-spatial silence. Dark, empty."""
        self._setup_panel(ax)
        ax.set_facecolor(BG_VOID)
        self._panel_title(ax, 'BEFORE', 'Pre-spatial silence', number=1)

        # Almost completely dark — just faint scattered dots representing
        # the mathematical existence of the algebra
        rng = np.random.RandomState(42)
        n_faint = 60
        xs = rng.uniform(1, 9, n_faint)
        ys = rng.uniform(1.5, 7.5, n_faint)
        sizes = rng.uniform(0.3, 1.5, n_faint)
        alphas = rng.uniform(0.02, 0.08, n_faint)

        for i in range(n_faint):
            dot = Circle((xs[i], ys[i]), sizes[i] * 0.04,
                         facecolor=GREY_FROZEN, edgecolor='none',
                         alpha=alphas[i])
            ax.add_patch(dot)

        # 21 frozen generators — faint ring in center
        cx, cy = 5.0, 5.0
        radius = 2.2
        for i in range(21):
            angle = 2 * np.pi * i / 21 - np.pi / 2
            x = cx + radius * np.cos(angle)
            y = cy + radius * np.sin(angle)
            dot = Circle((x, y), 0.12, facecolor=GREY_FROZEN,
                         edgecolor='#333344', linewidth=0.5, alpha=0.15)
            ax.add_patch(dot)

        # Faint "21" in center
        ax.text(cx, cy, '21', fontsize=24, color=GREY_FROZEN,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold', alpha=0.12)

        # Caption texts
        captions = [
            (5.0, 8.5, 'No time.', WHITE_DIM, 9),
            (5.0, 8.0, 'No space.', WHITE_DIM, 9),
            (5.0, 7.5, 'No commitments.', WHITE_DIM, 9),
        ]
        for x, y, text, color, size in captions:
            ax.text(x, y, text, fontsize=size, color=color,
                    ha='center', fontfamily='monospace', alpha=0.7)

        # Bottom text
        ax.text(5.0, 1.0,
                '21 generators frozen.',
                fontsize=7, color=GREY_DIM, ha='center',
                fontfamily='monospace', alpha=0.6)
        ax.text(5.0, 0.5,
                'Not nothing. The most symmetric',
                fontsize=7, color=GREY_DIM, ha='center',
                fontfamily='monospace', alpha=0.5)
        ax.text(5.0, 0.1,
                'possible something.',
                fontsize=7, color=GREY_DIM, ha='center',
                fontfamily='monospace', alpha=0.5)

    # ─────────────────────────────────────────────────────────
    #  PANEL 2: THE FLUCTUATION
    # ─────────────────────────────────────────────────────────
    def _draw_panel_2_fluctuation(self, ax):
        """Panel 2: The first quantum fluctuation — a whisper."""
        self._setup_panel(ax)
        self._panel_title(ax, 'THE FLUCTUATION',
                          'Not a bang -- a whisper', number=2)

        cx, cy = 5.0, 5.0

        # Dark background with a single bright point emerging
        # Concentric glow rings — the fluctuation spreading outward
        glow_colors = [
            (2.8, 0.015, PURPLE_DIM),
            (2.2, 0.025, BLUE_DIM),
            (1.6, 0.04, CYAN_DIM),
            (1.1, 0.06, '#004466'),
            (0.7, 0.10, '#006688'),
            (0.4, 0.18, '#008899'),
            (0.2, 0.30, CYAN),
            (0.08, 0.60, WHITE),
        ]
        for r, a, c in glow_colors:
            glow = Circle((cx, cy), r, facecolor=c, edgecolor='none',
                          alpha=a, zorder=1)
            ax.add_patch(glow)

        # Central bright point
        center = Circle((cx, cy), 0.04, facecolor=WHITE,
                         edgecolor='none', zorder=5)
        ax.add_patch(center)

        # The nu anti-nu pair — two tiny dots near center
        offset = 0.25
        nu = Circle((cx - offset, cy + 0.05), 0.06,
                     facecolor=CYAN, edgecolor=WHITE, linewidth=0.5, zorder=4)
        anti_nu = Circle((cx + offset, cy - 0.05), 0.06,
                         facecolor=PINK, edgecolor=WHITE, linewidth=0.5, zorder=4)
        ax.add_patch(nu)
        ax.add_patch(anti_nu)

        ax.text(cx - offset, cy + 0.35, 'nu', fontsize=6, color=CYAN,
                ha='center', fontfamily='monospace', zorder=5)
        ax.text(cx + offset, cy - 0.35, 'anti-nu', fontsize=6, color=PINK,
                ha='center', fontfamily='monospace', zorder=5)

        # Channel capacity indicator: 0 -> 1
        arrow_y = 8.0
        ax.text(2.5, arrow_y, 'Channel: 0', fontsize=9, color=GREY_DIM,
                ha='center', fontfamily='monospace')
        ax.annotate('', xy=(5.5, arrow_y), xytext=(4.0, arrow_y),
                    arrowprops=dict(arrowstyle='->', color=GOLD,
                                    lw=1.5, connectionstyle='arc3,rad=0'))
        ax.text(7.0, arrow_y, '1', fontsize=12, color=GOLD,
                ha='center', fontfamily='monospace', fontweight='bold')

        # Energy cost = 0
        ax.text(5.0, 2.2, 'Energy cost: ZERO',
                fontsize=9, color=GREEN, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(5.0, 1.7, '(m_nu1 = 0)',
                fontsize=7, color=GREEN_DIM, ha='center',
                fontfamily='monospace')

        # Curvature info
        ax.text(5.0, 0.8, 'H = -2/7  (negative curvature)',
                fontsize=7, color=GREY, ha='center', fontfamily='monospace')
        ax.text(5.0, 0.3, 'Perturbations grow as exp(0.535 t)',
                fontsize=7, color=GREY, ha='center', fontfamily='monospace')

    # ─────────────────────────────────────────────────────────
    #  PANEL 3: THE UNFREEZE SEQUENCE
    # ─────────────────────────────────────────────────────────
    def _draw_panel_3_unfreeze(self, ax):
        """Panel 3: 21 generators activate in sequence."""
        self._setup_panel(ax)
        self._panel_title(ax, 'THE UNFREEZE',
                          '21 generators light up one by one', number=3)

        # Generator groups with colors
        groups = [
            ('SO(3)', 3, COLOR_SO3, 'spatial',  '3 dims of space'),
            ('SU(3)', 8, COLOR_SU3, 'color',    'strong force'),
            ('SU(2)', 3, COLOR_SU2, 'weak',     'weak force'),
            ('U(1)',  1, COLOR_U1,  'EM',       'alpha = 1/137'),
            ('SO(2)', 1, COLOR_SO2, 'temporal', 'TIME BEGINS'),
        ]

        # Draw generators as circles in a sequence, grouped
        y_base = 7.5
        row_height = 1.15
        gen_radius = 0.22
        cumulative = 0
        group_y_positions = []

        for gi, (name, count, color, label, note) in enumerate(groups):
            y = y_base - gi * row_height
            group_y_positions.append(y)

            # Group label on left
            ax.text(0.3, y, name, fontsize=8, fontweight='bold',
                    color=color, ha='left', va='center',
                    fontfamily='monospace')

            # Generator circles
            x_start = 2.5
            x_spacing = 0.55
            for i in range(count):
                x = x_start + i * x_spacing
                # Glow for each active generator
                for r_glow, a_glow in [(0.35, 0.06), (0.28, 0.12)]:
                    glow = Circle((x, y), r_glow, facecolor=color,
                                  edgecolor='none', alpha=a_glow, zorder=1)
                    ax.add_patch(glow)
                # Main circle
                circ = Circle((x, y), gen_radius,
                              facecolor=color, edgecolor=WHITE,
                              linewidth=0.8, alpha=0.85, zorder=3)
                ax.add_patch(circ)
                cumulative += 1

            # Cumulative count
            x_end = x_start + (count - 1) * x_spacing + 0.6
            ax.text(x_end + 0.5, y + 0.1,
                    '{}/21'.format(cumulative),
                    fontsize=7, color=color, ha='left', va='center',
                    fontfamily='monospace')
            ax.text(x_end + 0.5, y - 0.2, note,
                    fontsize=6, color=GREY, ha='left', va='center',
                    fontfamily='monospace')

        # Frozen isotropy: 5 remaining
        y_frozen = y_base - 5 * row_height
        ax.text(0.3, y_frozen, 'SO(5)', fontsize=8,
                color=GREY_FROZEN, ha='left', va='center',
                fontfamily='monospace')
        for i in range(5):
            x = 2.5 + i * 0.55
            circ = Circle((x, y_frozen), gen_radius,
                          facecolor=GREY_FROZEN, edgecolor='#333344',
                          linewidth=0.5, alpha=0.4, zorder=2)
            ax.add_patch(circ)
        ax.text(2.5 + 4 * 0.55 + 1.1, y_frozen,
                '(frozen isotropy)',
                fontsize=6, color=GREY_FROZEN, ha='left', va='center',
                fontfamily='monospace')

        # Vertical timeline arrow on far left
        ax.annotate('', xy=(0.1, y_frozen - 0.3),
                    xytext=(0.1, y_base + 0.5),
                    arrowprops=dict(arrowstyle='->', color=GOLD_DIM,
                                    lw=1.5))
        ax.text(0.1, y_base + 0.7, 't', fontsize=8, color=GOLD_DIM,
                ha='center', fontfamily='monospace', fontstyle='italic')

        # Summary at bottom
        ax.text(5.0, 0.6,
                '21 = 3 + 8 + 3 + 1 + 1 + 5(frozen)',
                fontsize=8, color=GOLD, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(5.0, 0.15,
                'A boot sequence, not an explosion.',
                fontsize=7, color=GOLD_DIM, ha='center',
                fontfamily='monospace', fontstyle='italic')

    # ─────────────────────────────────────────────────────────
    #  PANEL 4: t = 3.1 SECONDS — ALL ACTIVE
    # ─────────────────────────────────────────────────────────
    def _draw_panel_4_first_bit(self, ax):
        """Panel 4: All generators active. First commitment writes."""
        self._setup_panel(ax)
        self._panel_title(ax, 't = 3.1 SECONDS',
                          'All generators active. First commitment writes.', number=4)

        cx, cy = 5.0, 5.2

        # Radiant burst — the first commitment
        # Multiple concentric rings of light
        n_rings = 12
        for i in range(n_rings):
            r = 0.3 + i * 0.28
            alpha_val = 0.25 * (1 - i / n_rings)
            colors_cycle = [COLOR_SO3, COLOR_SU3, COLOR_SU2, COLOR_U1, COLOR_SO2]
            ring_color = colors_cycle[i % len(colors_cycle)]
            ring = Circle((cx, cy), r, facecolor='none',
                          edgecolor=ring_color, linewidth=1.2,
                          alpha=alpha_val, zorder=2)
            ax.add_patch(ring)

        # Central glow
        for r_g, a_g in [(1.0, 0.04), (0.7, 0.08), (0.4, 0.15),
                         (0.2, 0.30), (0.08, 0.60)]:
            glow = Circle((cx, cy), r_g, facecolor=GOLD,
                          edgecolor='none', alpha=a_g, zorder=3)
            ax.add_patch(glow)

        # Central "1" — the first bit
        ax.text(cx, cy, '1', fontsize=28, fontweight='bold',
                color=WHITE, ha='center', va='center',
                fontfamily='monospace', zorder=5,
                path_effects=[pe.withStroke(linewidth=3, foreground=GOLD_DARK)])

        # Rays emanating outward
        n_rays = 16
        for i in range(n_rays):
            angle = 2 * np.pi * i / n_rays
            r_in = 0.5
            r_out = 3.0 + 0.5 * np.sin(i * 3.7)
            x_in = cx + r_in * np.cos(angle)
            y_in = cy + r_in * np.sin(angle)
            x_out = cx + r_out * np.cos(angle)
            y_out = cy + r_out * np.sin(angle)
            alpha_ray = 0.08 + 0.04 * np.sin(i * 2.3)
            ax.plot([x_in, x_out], [y_in, y_out],
                    color=GOLD, linewidth=0.6, alpha=alpha_ray, zorder=1)

        # Labels around the burst
        labels = [
            (1.5, 8.2, 'Space nucleates', COLOR_SO3),
            (8.0, 8.2, 'Forces activate', COLOR_SU3),
            (1.0, 2.0, 'Time begins', COLOR_SO2),
            (8.5, 2.0, 'Circuits form', COLOR_U1),
        ]
        for x, y, text, color in labels:
            ax.text(x, y, text, fontsize=7, color=color,
                    ha='center', fontfamily='monospace', alpha=0.8)

        # "Not with a bang but with a bit."
        ax.text(5.0, 0.6, '"Not with a bang but with a bit."',
                fontsize=9, color=GOLD, ha='center',
                fontfamily='monospace', fontstyle='italic',
                fontweight='bold')
        ax.text(5.0, 0.15,
                'T_c = {:.4f} MeV    N = {}    E = 0'.format(T_c_MeV, N_min),
                fontsize=7, color=GREY, ha='center', fontfamily='monospace')

    # ─────────────────────────────────────────────────────────
    #  PANEL 5: NO SINGULARITY
    # ─────────────────────────────────────────────────────────
    def _draw_panel_5_no_singularity(self, ax):
        """Panel 5: Standard Big Bang vs BST — no singularity."""
        self._setup_panel(ax)
        self._panel_title(ax, 'NO SINGULARITY',
                          'Standard vs BST at t = 0', number=5)

        # LEFT side: Standard Big Bang — chaotic, infinite, broken
        ax.text(2.5, 8.3, 'STANDARD', fontsize=9, fontweight='bold',
                color=RED_WARM, ha='center', fontfamily='monospace')

        # Draw a violent singularity — jagged lines, red glow
        sx, sy = 2.5, 5.5
        # Red explosion glow
        for r_g, a_g in [(2.0, 0.03), (1.4, 0.06), (0.9, 0.10),
                         (0.5, 0.18), (0.2, 0.35)]:
            glow = Circle((sx, sy), r_g, facecolor=RED_WARM,
                          edgecolor='none', alpha=a_g, zorder=1)
            ax.add_patch(glow)

        # Jagged rays
        rng = np.random.RandomState(99)
        for i in range(20):
            angle = rng.uniform(0, 2 * np.pi)
            length = rng.uniform(0.5, 2.2)
            x_end = sx + length * np.cos(angle)
            y_end = sy + length * np.sin(angle)
            ax.plot([sx, x_end], [sy, y_end],
                    color=RED_WARM, linewidth=rng.uniform(0.3, 1.5),
                    alpha=rng.uniform(0.15, 0.5), zorder=2)

        # Labels for standard
        std_labels = [
            (2.5, 3.5, 'rho -> infinity', RED_DIM),
            (2.5, 3.0, 'T -> infinity', RED_DIM),
            (2.5, 2.5, 'Physics breaks', RED_DIM),
            (2.5, 2.0, 'Singularity', RED_WARM),
        ]
        for x, y, text, color in std_labels:
            ax.text(x, y, text, fontsize=7, color=color,
                    ha='center', fontfamily='monospace')

        # Dividing line
        ax.plot([5.0, 5.0], [1.5, 8.5], color=GREY_DIM,
                linewidth=0.8, linestyle='--', alpha=0.5)
        ax.text(5.0, 8.6, 'vs', fontsize=8, color=GREY,
                ha='center', fontfamily='monospace')

        # RIGHT side: BST — quiet, smooth, finite
        ax.text(7.5, 8.3, 'BST', fontsize=9, fontweight='bold',
                color=CYAN, ha='center', fontfamily='monospace')

        # Gentle glow — smooth, finite
        bx, by = 7.5, 5.5
        for r_g, a_g in [(1.8, 0.02), (1.3, 0.04), (0.9, 0.08),
                         (0.5, 0.15), (0.2, 0.30)]:
            glow = Circle((bx, by), r_g, facecolor=CYAN,
                          edgecolor='none', alpha=a_g, zorder=1)
            ax.add_patch(glow)

        # Smooth concentric rings
        for r_ring in [0.6, 1.0, 1.4, 1.8]:
            ring = Circle((bx, by), r_ring, facecolor='none',
                          edgecolor=CYAN, linewidth=0.5,
                          alpha=0.15, zorder=2)
            ax.add_patch(ring)

        # Labels for BST
        bst_labels = [
            (7.5, 3.5, 'rho = 0', CYAN_DIM),
            (7.5, 3.0, 'T = undefined', CYAN_DIM),
            (7.5, 2.5, 'Nothing breaks', CYAN_DIM),
            (7.5, 2.0, 'A quiet start', CYAN),
        ]
        for x, y, text, color in bst_labels:
            ax.text(x, y, text, fontsize=7, color=color,
                    ha='center', fontfamily='monospace')

        # Bottom insight
        ax.text(5.0, 0.8,
                'The singularity is an artifact',
                fontsize=8, color=WHITE_DIM, ha='center',
                fontfamily='monospace')
        ax.text(5.0, 0.3,
                'of not knowing about the substrate.',
                fontsize=8, color=WHITE_DIM, ha='center',
                fontfamily='monospace')

    # ─────────────────────────────────────────────────────────
    #  PANEL 6: IN THE BEGINNING WAS THE COMMITMENT
    # ─────────────────────────────────────────────────────────
    def _draw_panel_6_in_the_beginning(self, ax):
        """Panel 6: The first committed bit generates everything."""
        self._setup_panel(ax)
        self._panel_title(ax, 'THE FIRST BIT',
                          'From one bit, everything', number=6)

        cx, cy = 5.0, 5.5

        # Central bit — bright "1"
        for r_g, a_g in [(2.5, 0.015), (1.8, 0.025), (1.2, 0.05),
                         (0.7, 0.10), (0.35, 0.25), (0.15, 0.50)]:
            glow = Circle((cx, cy), r_g, facecolor=GOLD,
                          edgecolor='none', alpha=a_g, zorder=1)
            ax.add_patch(glow)

        ax.text(cx, cy, '1', fontsize=20, fontweight='bold',
                color=GOLD, ha='center', va='center',
                fontfamily='monospace', zorder=5,
                path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])

        # Emanating branches to what the bit creates
        branches = [
            (135, 'Space',   COLOR_SO3,  2.8),
            (90,  'Time',    COLOR_SO2,  2.8),
            (45,  'Matter',  COLOR_SU3,  2.8),
            (180, 'Forces',  COLOR_SU2,  2.5),
            (0,   'alpha',   COLOR_U1,   2.5),
        ]

        for angle_deg, label, color, length in branches:
            angle = np.radians(angle_deg)
            x_end = cx + length * np.cos(angle)
            y_end = cy + length * np.sin(angle)
            # Line from center
            ax.plot([cx, x_end], [cy, y_end],
                    color=color, linewidth=1.2, alpha=0.5, zorder=2)
            # Endpoint dot
            dot = Circle((x_end, y_end), 0.15, facecolor=color,
                          edgecolor=WHITE, linewidth=0.5, alpha=0.8, zorder=3)
            ax.add_patch(dot)
            # Label
            dx = 0.4 * np.cos(angle)
            dy = 0.4 * np.sin(angle)
            ax.text(x_end + dx, y_end + dy, label,
                    fontsize=7, color=color, ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')

        # Commitment cascade: k=0 -> k=1 -> k=3 -> k=6
        cascade_y = 2.4
        k_values = [
            (0, 'vacuum',  GREY,    1.5),
            (1, 'e',       CYAN,    3.5),
            (3, 'Wallach', ORANGE,  5.5),
            (6, 'baryon',  RED_WARM, 7.5),
        ]
        ax.text(0.5, cascade_y + 0.5, 'Cascade:', fontsize=7,
                color=GOLD_DIM, fontfamily='monospace')
        for k, name, color, x in k_values:
            ax.text(x, cascade_y, 'k={}'.format(k), fontsize=8,
                    color=color, ha='center', fontfamily='monospace',
                    fontweight='bold')
            ax.text(x, cascade_y - 0.45, name, fontsize=6,
                    color=color, ha='center', fontfamily='monospace',
                    alpha=0.7)
        # Arrows between cascade stages
        for i in range(len(k_values) - 1):
            x1 = k_values[i][3] + 0.5
            x2 = k_values[i + 1][3] - 0.5
            ax.annotate('', xy=(x2, cascade_y), xytext=(x1, cascade_y),
                        arrowprops=dict(arrowstyle='->', color=GOLD_DIM,
                                        lw=1.0))

        # Reality Budget
        ax.text(5.0, 1.3, 'Lambda x N = 9/5  (always)',
                fontsize=8, color=GOLD, ha='center',
                fontfamily='monospace', fontweight='bold')

        # The closing line
        ax.text(5.0, 0.5,
                '"In the beginning was the commitment."',
                fontsize=9, color=GOLD, ha='center',
                fontfamily='monospace', fontstyle='italic',
                fontweight='bold',
                path_effects=[pe.withStroke(linewidth=1, foreground='#332200')])

    # ─────────────────────────────────────────────────────────
    #  summary() — one-paragraph summary
    # ─────────────────────────────────────────────────────────
    def summary(self):
        """Print one-paragraph summary."""
        text = (
            "In BST, the Big Bang is not t=0. It is the moment the substrate "
            "writes its first bit. Before that: pre-spatial silence — all 21 "
            "so(5,2) generators frozen, no time, no space, no commitments. "
            "The frozen state (N=0) is mathematically inconsistent: negative "
            "curvature (H = -2/7), the uncertainty principle, representation "
            "theory, and the Reality Budget (Lambda x N = 9/5) all forbid it. "
            "The minimum state has N=2 (a nu anti-nu pair, zero energy cost). "
            "Generators unfreeze in sequence: SO(3) spatial, SU(3) color, "
            "SU(2) weak, U(1) EM, SO(2) temporal. At t=3.1 seconds, T_c = "
            "0.487 MeV, all generators are active, D_IV^5 is fully online, "
            "and the first commitment writes. No singularity. No infinite "
            "density. No breakdown of physics. Not with a bang but with a bit."
        )
        if not self.quiet:
            print()
            print("  SUMMARY")
            print("  " + "-" * 56)
            # Word wrap at ~60 chars
            words = text.split()
            line = "  "
            for w in words:
                if len(line) + len(w) + 1 > 68:
                    print(line)
                    line = "  " + w
                else:
                    line += " " + w if line.strip() else w
            if line.strip():
                print(line)
            print()

        return text


# ═══════════════════════════════════════════════════════════════════
#  MAIN — run all methods and show
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    fc = FirstCommitment()
    fc.prespatial()
    fc.fluctuation()
    fc.unfreeze_sequence()
    fc.first_bit()
    fc.no_singularity()
    fc.reality_budget()
    fc.commitment_cascade()
    fc.timeline_0_to_3()
    fc.summary()
    fc.show()

    # Keep alive
    try:
        plt.show(block=True)
    except KeyboardInterrupt:
        pass
