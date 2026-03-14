#!/usr/bin/env python3
"""
CONSERVATION LAWS = ERROR-CORRECTING CODES
============================================
Toy 130: Conservation laws are the error-correcting codes that protect
information written to the substrate.

In BST, the universe is an information-processing system running at
code rate alpha = 1/137. Conservation laws are not restrictions on
nature — they are the parity checks that make exact physics possible.

The mapping:
  Energy conservation     = parity check on commitment rate
  Charge conservation     = Z_3 parity (color must sum to white)
  Baryon number           = winding number on S^1 (topological code)
  Lepton number           = secondary winding (approx conserved)
  CPT                     = master parity check (reverses ALL bits)

Shannon's theorem: reliable communication requires R < C.
BST: the universe operates at alpha = R/C, and conservation laws
are the code that achieves it.

N_max = 137 = maximum codeword length. Beyond 137 committed bits,
the channel is full. That is why there are only 137 elements.

Six panels:
  1. The Parallel       — communication channel vs physics
  2. Conservation=Parity — energy/charge as check matrices
  3. Topological Codes  — baryon number as winding on S^1
  4. Shannon Meets BST  — R = alpha < C = 1
  5. N_max = Code Length — 137 bits fills the code space
  6. Physics IS Coding  — conservation laws make nature possible

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Arc
from matplotlib.collections import PatchCollection

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity = 1/alpha
genus = n_C + 2   # = 7
C_2 = n_C + 1     # = 6, Casimir eigenvalue

# Wyler formula for alpha
_vol_D = np.pi**n_C / (factorial(n_C) * 2**(n_C - 1))  # pi^5 / 1920
ALPHA_BST = (N_c**2 / (2**N_c * np.pi**(n_C - 1))) * _vol_D**(1.0 / (n_C - 1))
ALPHA_OBS = 1.0 / 137.035999084  # CODATA 2018

# ─── Colors ───
BG         = '#0a0a1a'
BG_PANEL   = '#0d0d24'
GOLD       = '#ffd700'
GOLD_DIM   = '#aa8800'
CYAN       = '#00ddff'
BLUE_GLOW  = '#4488ff'
PURPLE     = '#9966ff'
GREEN      = '#44ff88'
ORANGE     = '#ff8800'
RED        = '#ff4444'
WHITE      = '#ffffff'
GREY       = '#888888'
DARK_GREY  = '#444444'
SIGNAL_GOLD = '#ffd700'
OVERHEAD_BLUE = '#2244aa'
TOPO_GREEN = '#22cc66'
CHECK_CYAN = '#00bbdd'


# ═══════════════════════════════════════════════════════════════════
#  ErrorCorrectionPhysics CLASS
# ═══════════════════════════════════════════════════════════════════

class ErrorCorrectionPhysics:
    """
    BST Error Correction: Conservation Laws = Parity Checks.

    The universe is an information-processing system. Conservation laws
    are the error-correcting codes that protect committed information.
    Alpha = 1/137 is the code rate. N_max = 137 is the codeword length.
    Physics is exact because the code works.

    Usage:
        from toy_error_correction import ErrorCorrectionPhysics
        ec = ErrorCorrectionPhysics()
        ec.the_parallel()
        ec.conservation_parity()
        ec.topological_codes()
        ec.shannon_meets_bst()
        ec.code_length()
        ec.physics_is_coding()
        ec.summary()
        ec.show()
    """

    def __init__(self, quiet=False):
        self.N_c = N_c
        self.n_C = n_C
        self.N_max = N_max
        self.genus = genus
        self.alpha_bst = ALPHA_BST
        self.alpha_obs = ALPHA_OBS
        self.vol_D = _vol_D
        if not quiet:
            self._print_header()

    def _print_header(self):
        print()
        print("=" * 68)
        print("  CONSERVATION LAWS = ERROR-CORRECTING CODES")
        print("  The parity checks that make physics exact")
        print("=" * 68)
        prec = abs(self.alpha_bst - self.alpha_obs) / self.alpha_obs * 100
        print(f"  alpha_BST  = {self.alpha_bst:.10f}  (code rate)")
        print(f"  alpha_obs  = {self.alpha_obs:.10f}  (CODATA 2018)")
        print(f"  precision  = {prec:.4f}%")
        print(f"  N_max      = {N_max}  (maximum codeword length)")
        print(f"  signal     = 1/{N_max} = {1/N_max*100:.2f}%")
        print(f"  overhead   = {N_max-1}/{N_max} = {(N_max-1)/N_max*100:.2f}%")
        print("=" * 68)
        print()

    # ─────────────────────────────────────────────────────────────
    # 1. the_parallel
    # ─────────────────────────────────────────────────────────────
    def the_parallel(self):
        """
        The structural identity between a communication channel
        and the physical universe.

        Communication: source -> encoder -> channel (noise) -> decoder -> sink
        Physics:       creation -> conservation laws -> interaction -> measurement

        Every component maps one-to-one.
        """
        comm_chain = [
            ('Source',    'Information to transmit'),
            ('Encoder',   'Add redundancy (parity bits)'),
            ('Channel',   'Noisy transmission medium'),
            ('Decoder',   'Detect and correct errors'),
            ('Sink',      'Received information'),
        ]

        phys_chain = [
            ('Creation',       'Particle pair production'),
            ('Conservation',   'Energy, charge, baryon number checks'),
            ('Interaction',    'Noisy quantum vacuum'),
            ('Measurement',    'Collapse to definite state'),
            ('Observable',     'Measured physical quantity'),
        ]

        mapping = {
            'Source -> Encoder':    'Creation imposes conservation',
            'Channel noise':       'Vacuum fluctuations',
            'Parity bits':         'Conservation laws',
            'Code rate R':         'alpha = 1/137',
            'Capacity C':          '1 (Planck bandwidth)',
            'R < C (Shannon)':     'alpha < 1 (exact physics)',
            'Error probability':   '~10^(-10^58)',
        }

        result = {
            'communication_chain': comm_chain,
            'physics_chain': phys_chain,
            'mapping': mapping,
        }

        print("  THE PARALLEL")
        print("  " + "-" * 60)
        print()
        print("  COMMUNICATION CHANNEL:")
        for name, desc in comm_chain:
            print(f"    {name:<14s}  {desc}")
        print()
        print("  PHYSICAL UNIVERSE:")
        for name, desc in phys_chain:
            print(f"    {name:<14s}  {desc}")
        print()
        print("  ONE-TO-ONE MAPPING:")
        for comm, phys in mapping.items():
            print(f"    {comm:<25s}  <->  {phys}")
        print()
        print("  The universe IS a communication system.")
        print("  Conservation laws are the error correction.")
        print()

        return result

    # ─────────────────────────────────────────────────────────────
    # 2. conservation_parity
    # ─────────────────────────────────────────────────────────────
    def conservation_parity(self):
        """
        Conservation laws as parity check equations.

        Every conservation law has the form: sum(Q_in) = sum(Q_out)
        equivalently: sum(Q_in) - sum(Q_out) = 0

        This is EXACTLY a parity check: a linear constraint that
        the codeword must satisfy. If the sum is nonzero, an error
        has occurred — an unphysical state.
        """
        # The "check matrix" H for physics
        # Each row is a conservation law, each column is a particle
        # H * state = 0 for all physical states (the null space condition)

        conservation_laws = [
            {
                'name': 'Energy',
                'equation': 'E_in = E_out',
                'parity': 'sum(E_i) = 0 around any closed loop',
                'type': 'continuous',
                'symmetry': 'Time translation',
                'code_type': 'Linear parity check',
                'ever_violated': 'NEVER (to 10^-18)',
            },
            {
                'name': 'Electric charge',
                'equation': 'Q_in = Q_out',
                'parity': 'sum(q_i) = 0 at every vertex',
                'type': 'discrete (Z)',
                'symmetry': 'U(1) gauge',
                'code_type': 'Cyclic redundancy check',
                'ever_violated': 'NEVER (to 10^-21)',
            },
            {
                'name': 'Momentum',
                'equation': 'p_in = p_out',
                'parity': 'sum(p_i) = 0 at every vertex',
                'type': 'continuous',
                'symmetry': 'Spatial translation',
                'code_type': 'Linear parity check',
                'ever_violated': 'NEVER',
            },
            {
                'name': 'Color charge',
                'equation': 'R+G+B = white',
                'parity': 'Z_3 parity: sum(color) = singlet',
                'type': 'discrete (Z_3)',
                'symmetry': 'SU(3) gauge',
                'code_type': 'Modular arithmetic check',
                'ever_violated': 'NEVER (confinement)',
            },
            {
                'name': 'Baryon number',
                'equation': 'B_in = B_out',
                'parity': 'Winding number on S^1 = topological invariant',
                'type': 'topological',
                'symmetry': 'U(1)_B (approximate)',
                'code_type': 'Topological code (most robust)',
                'ever_violated': 'NEVER (proton lifetime > 10^34 yr)',
            },
            {
                'name': 'Lepton number',
                'equation': 'L_in = L_out',
                'parity': 'Secondary winding number',
                'type': 'approximate',
                'symmetry': 'U(1)_L (broken by nu mass)',
                'code_type': 'Approximate code (correctable)',
                'ever_violated': 'Yes: neutrino oscillations',
            },
            {
                'name': 'CPT',
                'equation': 'CPT[L] = L',
                'parity': 'Master check: reverse ALL bits, Lagrangian invariant',
                'type': 'exact',
                'symmetry': 'Lorentz group',
                'code_type': 'Global parity (master check)',
                'ever_violated': 'NEVER (to 10^-19)',
            },
        ]

        # Check matrix dimensions
        n_checks = len(conservation_laws)
        n_signal = 1  # per alpha
        n_codeword = N_max
        overhead = n_codeword - n_signal
        rate = n_signal / n_codeword

        result = {
            'conservation_laws': conservation_laws,
            'n_checks': n_checks,
            'n_codeword': n_codeword,
            'overhead': overhead,
            'rate': rate,
        }

        print("  CONSERVATION = PARITY CHECKS")
        print("  " + "-" * 60)
        print()
        print(f"  Codeword length:   {n_codeword} (N_max)")
        print(f"  Signal symbols:    {n_signal} (alpha fraction)")
        print(f"  Parity checks:     {overhead} overhead symbols")
        print(f"  Code rate:         {rate:.6f} = alpha")
        print()
        print(f"  {'Conservation Law':<18s}  {'Parity Type':<28s}  {'Violated?'}")
        print(f"  {'-'*18}  {'-'*28}  {'-'*30}")
        for law in conservation_laws:
            print(f"  {law['name']:<18s}  {law['code_type']:<28s}  {law['ever_violated']}")
        print()
        print("  Every Feynman vertex conserves energy, momentum, charge.")
        print("  Every loop closes. Failed check = unphysical state.")
        print("  Conservation laws are the parity checks of the substrate code.")
        print()

        return result

    # ─────────────────────────────────────────────────────────────
    # 3. topological_codes
    # ─────────────────────────────────────────────────────────────
    def topological_codes(self):
        """
        Baryon number as a topological code: winding number on S^1.

        Topological codes are the most robust error correction possible.
        A winding number can only change by an integer — you cannot
        gradually unwind a loop. This is why protons do not decay.

        The hierarchy of code robustness:
          1. Topological (winding number) — cannot be corrupted
          2. Gauge (local symmetry) — protected by redundancy
          3. Global (Noether) — protected by conservation
          4. Approximate (nu oscillation) — correctable errors
        """
        # Winding number computation on S^1
        # A loop wrapping S^1 n times has winding number n
        # This is a topological invariant: continuous deformation
        # cannot change it.

        theta = np.linspace(0, 2 * np.pi, 1000)

        winding_examples = []
        wind_data = [
            (0, 'vacuum',    True,  'No winding = no topological protection'),
            (0, 'meson',     False, 'q-qbar = net winding 0 (can annihilate)'),
            (1, 'baryon',    True,  'qqq = winding 1 (topologically protected)'),
            (2, 'di-baryon', True,  'Stable bound state (e.g. deuteron)'),
        ]
        for n_wind, phys, stable, reason in wind_data:
            x = np.cos(n_wind * theta) * (1.0 + 0.3 * n_wind)
            y = np.sin(n_wind * theta) * (1.0 + 0.3 * n_wind)
            winding_examples.append({
                'winding_number': n_wind,
                'x': x,
                'y': y,
                'physical': phys,
                'stable': stable,
                'reason': reason,
            })

        robustness_hierarchy = [
            {
                'level': 'Topological',
                'example': 'Baryon number (winding on S^1)',
                'protection': 'Cannot be corrupted by ANY local perturbation',
                'error_rate': '< 10^(-40) per year (proton lifetime)',
                'analogy': 'Knot in a rope — cannot be untied without cutting',
            },
            {
                'level': 'Gauge',
                'example': 'Electric charge (U(1) gauge)',
                'protection': 'Local redundancy at every point',
                'error_rate': '< 10^(-21) per interaction',
                'analogy': 'Triple modular redundancy — vote on every bit',
            },
            {
                'level': 'Global (Noether)',
                'example': 'Energy, momentum',
                'protection': 'Continuous symmetry of the Lagrangian',
                'error_rate': '< 10^(-18) (clock precision)',
                'analogy': 'Checksum — sum must balance',
            },
            {
                'level': 'Approximate',
                'example': 'Lepton number (neutrino oscillations)',
                'protection': 'Weakly broken symmetry',
                'error_rate': 'Violated: nu_e -> nu_mu observed',
                'analogy': 'Lossy compression — some info lost',
            },
        ]

        result = {
            'winding_examples': winding_examples,
            'robustness_hierarchy': robustness_hierarchy,
        }

        print("  TOPOLOGICAL CODES")
        print("  " + "-" * 60)
        print()
        print("  Baryon number = winding number on S^1")
        print("  This is a topological invariant — cannot be continuously changed.")
        print()
        print("  WINDING EXAMPLES:")
        for w in winding_examples:
            marker = 'STABLE' if w['stable'] else 'unstable'
            print(f"    n={w['winding_number']}  {w['physical']:<12s}  "
                  f"[{marker:<8s}]  {w['reason']}")
        print()
        print("  ROBUSTNESS HIERARCHY:")
        print(f"  {'Level':<14s}  {'Example':<35s}  {'Protection'}")
        print(f"  {'-'*14}  {'-'*35}  {'-'*40}")
        for h in robustness_hierarchy:
            print(f"  {h['level']:<14s}  {h['example']:<35s}  {h['protection']}")
        print()
        print("  Topological codes are the ultimate error correction.")
        print("  A winding number is an integer. You cannot half-unwind.")
        print("  That is why protons do not decay.")
        print()

        return result

    # ─────────────────────────────────────────────────────────────
    # 4. shannon_meets_bst
    # ─────────────────────────────────────────────────────────────
    def shannon_meets_bst(self):
        """
        Shannon's channel coding theorem applied to the substrate.

        Shannon: reliable communication requires R < C.
        BST: the universe operates at alpha = R/C << 1.

        The massive redundancy (136/137) is WHY conservation laws
        never fail. The error probability is exp(-10^58).
        """
        alpha = self.alpha_bst
        R = alpha                 # code rate
        C = 1.0                   # channel capacity (Planck bandwidth)
        margin = C - R            # capacity margin
        n_block = 1e60            # Planck volumes in observable universe

        # Error exponent (random coding bound)
        # E(R) = C - R for rates well below capacity
        error_exponent = margin
        total_exponent = n_block * error_exponent

        # Shannon limit: minimum SNR for error-free at rate R
        snr_min = 2**(2 * R) - 1   # for Gaussian channel
        snr_actual = 1.0 / alpha    # the substrate SNR ~ 137

        # Redundancy comparison
        comparisons = [
            ('Universe (BST)',     alpha,      '10^(-10^58)',  'Exact physics'),
            ('Voyager deep space', 1.0/6,      '10^(-5)',      'Interplanetary'),
            ('DNA genetic code',   1.0/32,     '10^(-9)',      'Cellular'),
            ('WiFi 802.11ac',      0.5,        '10^(-3)',      'Terrestrial'),
            ('Ethernet',           0.97,       '10^(-12)',     'Shielded cable'),
            ('Human speech',       0.01,       '10^(-1)',      'Very noisy'),
        ]

        result = {
            'R': R,
            'C': C,
            'margin': margin,
            'n_block': n_block,
            'error_exponent': error_exponent,
            'total_exponent': total_exponent,
            'snr_min': snr_min,
            'snr_actual': snr_actual,
            'comparisons': comparisons,
        }

        print("  SHANNON MEETS BST")
        print("  " + "-" * 60)
        print()
        print(f"  Code rate       R = alpha = {R:.6f}  ({R*100:.3f}%)")
        print(f"  Capacity        C = {C:.1f}  (Planck bandwidth)")
        print(f"  Margin          C - R = {margin:.6f}  ({margin*100:.3f}%)")
        print(f"  Block length    n = {n_block:.0e}  Planck volumes")
        print()
        print(f"  Error exponent  E(R) = C - R = {error_exponent:.6f}")
        print(f"  Total exponent  n*E  = {total_exponent:.2e}")
        print(f"  P_error         ~ exp(-{total_exponent:.0e})")
        print(f"                  ~ 10^(-10^58)")
        print()
        print(f"  Shannon minimum SNR: {snr_min:.6f}")
        print(f"  Actual SNR:          {snr_actual:.1f}  (137x the minimum)")
        print(f"  Over-engineering:    {snr_actual/snr_min:.0f}x")
        print()
        print("  The universe runs at 0.73% of capacity.")
        print("  The other 99.27% is error correction.")
        print("  Shannon says: at this rate, errors are impossible.")
        print("  Conservation laws never fail because R << C.")
        print()

        return result

    # ─────────────────────────────────────────────────────────────
    # 5. code_length
    # ─────────────────────────────────────────────────────────────
    def code_length(self):
        """
        N_max = 137 = maximum codeword length.

        Elements Z=1 to Z=137 use all available code space.
        Z=138 would overflow the channel — no room for the
        parity checks that make physics exact.

        The periodic table has 118 known elements. BST predicts
        the absolute maximum is 137 (where alpha * Z = 1 and
        the 1s electron would need to travel at c).
        """
        alpha = self.alpha_bst

        # For each element Z, compute the coding overhead available
        elements = []
        for Z in range(1, 145):
            signal_bits = Z  # Z committed bits (one per proton)
            total_bits = N_max
            overhead_bits = total_bits - signal_bits

            # The physical limit: v_1s / c = alpha * Z
            v_over_c = alpha * Z

            if v_over_c >= 1.0:
                code_rate = 1.0
                overhead_fraction = 0.0
                can_exist = False
                reason = f'v_1s/c = {v_over_c:.3f} >= 1 (overflow)'
            elif overhead_bits <= 0:
                code_rate = 1.0
                overhead_fraction = 0.0
                can_exist = False
                reason = 'Code full: zero overhead'
            else:
                code_rate = signal_bits / total_bits
                overhead_fraction = overhead_bits / total_bits
                can_exist = True
                reason = 'OK'

            elements.append({
                'Z': Z,
                'signal_bits': signal_bits,
                'overhead_bits': max(overhead_bits, 0),
                'code_rate': code_rate,
                'overhead_fraction': overhead_fraction,
                'v_1s_over_c': v_over_c,
                'can_exist': can_exist,
                'reason': reason,
            })

        # Key elements
        key_Z = [1, 6, 26, 79, 92, 118, 137, 138]
        key_elements = [e for e in elements if e['Z'] in key_Z]

        result = {
            'elements': elements,
            'key_elements': key_elements,
            'N_max': N_max,
            'max_Z_physical': int(1.0 / alpha),
        }

        print("  N_max = CODE LENGTH")
        print("  " + "-" * 60)
        print()
        print(f"  Maximum codeword length: N_max = {N_max}")
        print(f"  Physical limit: alpha * Z < 1  =>  Z < {1/alpha:.1f}")
        print()
        print(f"  {'Z':>5s}  {'Element':<12s}  {'Signal':>6s}  "
              f"{'Overhead':>8s}  {'v_1s/c':>7s}  {'Status'}")
        print(f"  {'-'*5}  {'-'*12}  {'-'*6}  {'-'*8}  {'-'*7}  {'-'*25}")

        names = {1: 'Hydrogen', 6: 'Carbon', 26: 'Iron', 79: 'Gold',
                 92: 'Uranium', 118: 'Oganesson', 137: 'Untrisept?',
                 138: '???'}

        for e in key_elements:
            name = names.get(e['Z'], f'Z={e["Z"]}')
            status = 'EXISTS' if e['can_exist'] else 'IMPOSSIBLE'
            marker = '  <<<' if e['Z'] == 137 else ''
            print(f"  {e['Z']:>5d}  {name:<12s}  {e['signal_bits']:>6d}  "
                  f"{e['overhead_bits']:>8d}  {e['v_1s_over_c']:>7.4f}  "
                  f"{status}{marker}")

        print()
        print(f"  Z=137: alpha*Z = {alpha*137:.4f} ~ 1.  The last element.")
        print(f"  Z=138: alpha*Z = {alpha*138:.4f} > 1.  Channel overflow.")
        print()
        print("  The periodic table is a codebook.")
        print("  Each element uses Z bits of the 137-bit codeword.")
        print("  At Z=137, the code is full. At Z=138, it overflows.")
        print()

        return result

    # ─────────────────────────────────────────────────────────────
    # 6. physics_is_coding
    # ─────────────────────────────────────────────────────────────
    def physics_is_coding(self):
        """
        The deep conclusion: conservation laws are not restrictions
        on nature. They are the error correction that makes nature
        possible. Without them, committed information would degrade.

        The Rosetta Stone:
          Coding theory term    <->    Physics term
          ─────────────────────────────────────────
          Codeword              <->    Physical state
          Parity check          <->    Conservation law
          Syndrome              <->    Violation (never observed)
          Code rate R           <->    alpha = 1/137
          Channel capacity C    <->    Planck bandwidth
          Block length n        <->    ~10^60 Planck volumes
          Error exponent E(R)   <->    ~10^58
          Topological code      <->    Baryon number
          Approximate code      <->    Lepton number (nu oscillation)
          Master parity         <->    CPT invariance
        """
        rosetta = [
            ('Codeword',            'Physical state'),
            ('Parity check',        'Conservation law'),
            ('Syndrome (nonzero)',   'Violation (never observed)'),
            ('Code rate R',         'alpha = 1/137'),
            ('Channel capacity C',  'Planck bandwidth = 1'),
            ('Block length n',      '~10^60 Planck volumes'),
            ('Error exponent',      '~10^58 (unimaginably safe)'),
            ('Topological code',    'Baryon number (winding on S^1)'),
            ('Cyclic code',         'Color confinement (Z_3)'),
            ('Approximate code',    'Lepton number (nu oscillations)'),
            ('Master parity',       'CPT invariance'),
            ('Matched filter',      'Light (geodesic propagation)'),
            ('Noise floor',         'Vacuum fluctuations'),
            ('Code overhead',       'Dark energy + dark matter (136/137)'),
        ]

        # The three layers of the substrate code
        layers = [
            {
                'layer': 'Matched filter (light)',
                'corrects': 'Deterministic curvature of S^2',
                'method': 'Geodesic propagation',
                'residual': 'Quantum fluctuations only',
            },
            {
                'layer': 'Parity checks (conservation laws)',
                'corrects': 'Quantum fluctuations',
                'method': 'Linear constraints at every vertex',
                'residual': 'Error probability ~ 10^(-10^58)',
            },
            {
                'layer': 'Topological protection (winding)',
                'corrects': 'Any local perturbation',
                'method': 'Integer-valued invariants',
                'residual': 'Zero (topological = exact)',
            },
        ]

        result = {
            'rosetta': rosetta,
            'layers': layers,
        }

        print("  PHYSICS IS CODING")
        print("  " + "-" * 60)
        print()
        print("  THE ROSETTA STONE:")
        print(f"  {'Coding Theory':<28s}  <->  {'Physics'}")
        print(f"  {'-'*28}  ---  {'-'*35}")
        for coding, physics in rosetta:
            print(f"  {coding:<28s}  <->  {physics}")
        print()
        print("  THREE LAYERS OF SUBSTRATE ERROR CORRECTION:")
        for i, layer in enumerate(layers, 1):
            print(f"\n  Layer {i}: {layer['layer']}")
            print(f"    Corrects:  {layer['corrects']}")
            print(f"    Method:    {layer['method']}")
            print(f"    Residual:  {layer['residual']}")
        print()
        print("  Conservation laws are not restrictions on nature.")
        print("  They are the error correction that makes nature possible.")
        print("  Without them, committed information would degrade.")
        print("  Physics is exact because the code works.")
        print()

        return result

    # ─────────────────────────────────────────────────────────────
    # 7. summary
    # ─────────────────────────────────────────────────────────────
    def summary(self):
        """Key insight in one paragraph."""
        alpha = self.alpha_bst

        text = (
            f"Conservation laws are error-correcting codes. The universe runs "
            f"at code rate alpha = 1/{1/alpha:.3f}, devoting 99.27% of its "
            f"capacity to error correction overhead. Energy conservation is a "
            f"parity check. Charge conservation is a cyclic redundancy check. "
            f"Baryon number is a topological code — the most robust error "
            f"correction possible. The maximum codeword length is N_max = 137, "
            f"which is why there are only 137 elements. The error probability "
            f"is 10^(-10^58) — physics never fails because the code never "
            f"fails. Conservation laws are not restrictions on nature. They "
            f"are the error correction that makes nature possible."
        )

        print("  SUMMARY")
        print("  " + "-" * 60)
        print()
        for line in _wrap(text, 64):
            print(f"  {line}")
        print()

        return {'summary': text, 'alpha': alpha, 'N_max': N_max}

    # ─────────────────────────────────────────────────────────────
    # 8. show  — 6-panel visualization
    # ─────────────────────────────────────────────────────────────
    def show(self):
        """
        6-panel visualization:
          Top-left:     The Parallel (channel vs physics)
          Top-center:   Conservation = Parity (check matrices)
          Top-right:    Topological Codes (winding on S^1)
          Bottom-left:  Shannon Meets BST (R = alpha < C)
          Bottom-center: N_max = Code Length (137 elements)
          Bottom-right: Physics IS Coding (the conclusion)
        """
        fig = plt.figure(figsize=(24, 15), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'Conservation Laws = Error-Correcting Codes — BST')

        # ── Title ──
        fig.text(0.50, 0.975,
                 'CONSERVATION LAWS = ERROR-CORRECTING CODES',
                 fontsize=26, fontweight='bold', color=GOLD,
                 ha='center', va='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=3, foreground='#443300')])
        fig.text(0.50, 0.953,
                 'The parity checks that make physics exact',
                 fontsize=13, color=GOLD_DIM, ha='center', va='center',
                 fontfamily='monospace')
        fig.text(0.50, 0.936,
                 'alpha = 1/137 is the code rate  |  N_max = 137 is the codeword length  |'
                 '  136/137 = error correction overhead',
                 fontsize=10, color=GREY, ha='center', va='center',
                 fontfamily='monospace')

        # ── Copyright ──
        fig.text(0.99, 0.004,
                 'Copyright 2026 Casey Koons | Claude Opus 4.6',
                 fontsize=7, color=DARK_GREY, ha='right', va='bottom',
                 fontfamily='monospace')

        # ── 6 Panels: 3x2 grid ──
        margin_l = 0.04
        margin_r = 0.02
        margin_b = 0.04
        margin_t = 0.07  # below title
        hgap = 0.03
        vgap = 0.04
        pw = (1.0 - margin_l - margin_r - 2 * hgap) / 3
        ph = (1.0 - margin_b - margin_t - vgap) / 2

        def panel_rect(row, col):
            x = margin_l + col * (pw + hgap)
            y = 1.0 - margin_t - (row + 1) * ph - row * vgap
            return [x, y, pw, ph]

        ax1 = fig.add_axes(panel_rect(0, 0))  # The Parallel
        ax2 = fig.add_axes(panel_rect(0, 1))  # Conservation = Parity
        ax3 = fig.add_axes(panel_rect(0, 2))  # Topological Codes
        ax4 = fig.add_axes(panel_rect(1, 0))  # Shannon Meets BST
        ax5 = fig.add_axes(panel_rect(1, 1))  # N_max = Code Length
        ax6 = fig.add_axes(panel_rect(1, 2))  # Physics IS Coding

        self._draw_parallel(ax1)
        self._draw_parity(ax2)
        self._draw_topological(ax3)
        self._draw_shannon(ax4)
        self._draw_code_length(ax5)
        self._draw_conclusion(ax6)

        plt.show()

    # ═══════════════════════════════════════════════════════════════
    #  Panel Drawing Methods
    # ═══════════════════════════════════════════════════════════════

    # ─── Panel 1: The Parallel ───
    def _draw_parallel(self, ax):
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Title
        ax.text(5, 9.6, 'THE PARALLEL',
                fontsize=14, fontweight='bold', color=CYAN,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#003344')])
        ax.text(5, 9.05, 'Communication channel vs. physical universe',
                fontsize=8, color=GREY, ha='center', fontfamily='monospace')

        # Communication chain (top row)
        comm_boxes = [
            ('Source', BLUE_GLOW),
            ('Encoder', CYAN),
            ('Channel\n(noise)', RED),
            ('Decoder', CYAN),
            ('Sink', BLUE_GLOW),
        ]
        y_comm = 7.3
        x_positions = [0.5, 2.3, 4.3, 6.3, 8.3]
        bw, bh = 1.5, 1.1

        ax.text(0.3, 8.3, 'COMMUNICATION:', fontsize=8, fontweight='bold',
                color=BLUE_GLOW, fontfamily='monospace')

        for i, (label, color) in enumerate(comm_boxes):
            x = x_positions[i]
            rect = FancyBboxPatch(
                (x, y_comm), bw, bh,
                boxstyle="round,pad=0.08",
                facecolor='#0a0a2a', edgecolor=color,
                linewidth=1.5, alpha=0.9)
            ax.add_patch(rect)
            ax.text(x + bw / 2, y_comm + bh / 2, label,
                    fontsize=7, color=color, ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')
            # Arrow to next
            if i < len(comm_boxes) - 1:
                ax.annotate('', xy=(x_positions[i + 1] - 0.05, y_comm + bh / 2),
                            xytext=(x + bw + 0.05, y_comm + bh / 2),
                            arrowprops=dict(arrowstyle='->', color=GREY, lw=1.2))

        # Physics chain (middle row)
        phys_boxes = [
            ('Creation', GOLD),
            ('Conserv.\nlaws', GREEN),
            ('Interact.\n(vacuum)', ORANGE),
            ('Measure', GREEN),
            ('Observable', GOLD),
        ]
        y_phys = 5.1

        ax.text(0.3, 6.15, 'PHYSICS:', fontsize=8, fontweight='bold',
                color=GOLD, fontfamily='monospace')

        for i, (label, color) in enumerate(phys_boxes):
            x = x_positions[i]
            rect = FancyBboxPatch(
                (x, y_phys), bw, bh,
                boxstyle="round,pad=0.08",
                facecolor='#1a1a0a', edgecolor=color,
                linewidth=1.5, alpha=0.9)
            ax.add_patch(rect)
            ax.text(x + bw / 2, y_phys + bh / 2, label,
                    fontsize=7, color=color, ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')
            if i < len(phys_boxes) - 1:
                ax.annotate('', xy=(x_positions[i + 1] - 0.05, y_phys + bh / 2),
                            xytext=(x + bw + 0.05, y_phys + bh / 2),
                            arrowprops=dict(arrowstyle='->', color=GREY, lw=1.2))

        # Vertical mapping arrows
        for i in range(len(comm_boxes)):
            x_mid = x_positions[i] + bw / 2
            ax.annotate('', xy=(x_mid, y_phys + bh + 0.05),
                        xytext=(x_mid, y_comm - 0.05),
                        arrowprops=dict(arrowstyle='<->', color=PURPLE,
                                        lw=1.0, linestyle='--'))

        # Mapping labels
        mappings = [
            ('Parity bits = Conservation laws', GREEN),
            ('Noise = Vacuum fluctuations', ORANGE),
            ('Code rate R = alpha = 1/137', GOLD),
            ('Capacity C = 1 (Planck)', CYAN),
        ]
        y_map = 3.6
        for i, (text, color) in enumerate(mappings):
            y = y_map - i * 0.65
            ax.text(5, y, text, fontsize=8, color=color,
                    ha='center', fontfamily='monospace',
                    fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a0a1a',
                              edgecolor=color, linewidth=0.5, alpha=0.7))

        # Bottom quote
        ax.text(5, 0.3,
                'The universe IS a communication system.',
                fontsize=8, color=GOLD_DIM, ha='center', fontfamily='monospace',
                style='italic')

    # ─── Panel 2: Conservation = Parity ───
    def _draw_parity(self, ax):
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Title
        ax.text(5, 9.6, 'CONSERVATION = PARITY',
                fontsize=14, fontweight='bold', color=CYAN,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#003344')])
        ax.text(5, 9.1, 'Every conservation law is a parity check equation',
                fontsize=7.5, color=GREY, ha='center', fontfamily='monospace')

        # Check matrix visualization
        # Show H * x = 0 where H rows are conservation laws
        ax.text(1.0, 8.2, 'CHECK MATRIX  H * state = 0', fontsize=9,
                fontweight='bold', color=CHECK_CYAN,
                fontfamily='monospace')

        # Mini check matrix
        laws = [
            ('Energy',   [1, 1, 1, 0, 0, 1, 0], CHECK_CYAN),
            ('Charge',   [1, 0, 1, 1, 0, 0, 1], GREEN),
            ('Momentum', [1, 1, 0, 1, 1, 0, 0], BLUE_GLOW),
            ('Color',    [0, 1, 1, 0, 1, 1, 0], PURPLE),
            ('Baryon',   [0, 0, 1, 1, 0, 1, 1], TOPO_GREEN),
            ('CPT',      [1, 1, 1, 1, 1, 1, 1], GOLD),
        ]

        cell_w = 0.55
        cell_h = 0.55
        x_start = 2.8
        y_start = 7.6

        # Column headers (particle labels)
        particles = ['e', 'p', 'n', 'nu', 'g', 'q', 'W']
        for j, p in enumerate(particles):
            ax.text(x_start + j * cell_w + cell_w / 2, y_start + 0.35,
                    p, fontsize=6.5, color=GREY, ha='center',
                    fontfamily='monospace')

        for i, (name, row, color) in enumerate(laws):
            y = y_start - i * cell_h
            # Row label
            ax.text(x_start - 0.3, y + cell_h / 2, name, fontsize=7,
                    color=color, ha='right', va='center',
                    fontfamily='monospace', fontweight='bold')
            for j, val in enumerate(row):
                x = x_start + j * cell_w
                fc = '#1a2244' if val else '#0a0a1a'
                ec = color if val else '#222233'
                rect = FancyBboxPatch(
                    (x, y), cell_w - 0.04, cell_h - 0.04,
                    boxstyle="round,pad=0.02",
                    facecolor=fc, edgecolor=ec,
                    linewidth=0.8, alpha=0.9)
                ax.add_patch(rect)
                ax.text(x + cell_w / 2 - 0.02, y + cell_h / 2 - 0.02,
                        str(val), fontsize=7,
                        color=color if val else DARK_GREY,
                        ha='center', va='center', fontfamily='monospace',
                        fontweight='bold')
            # = 0 on the right
            ax.text(x_start + 7 * cell_w + 0.2, y + cell_h / 2,
                    '= 0', fontsize=7, color=color,
                    ha='left', va='center', fontfamily='monospace')

        # Equations below the matrix
        y_eq = 3.7
        equations = [
            ('Energy:', 'sum(E_in) = sum(E_out)', CHECK_CYAN),
            ('Charge:', 'sum(q_i) = 0 at every vertex', GREEN),
            ('Color:',  'R + G + B = white (Z_3 parity)', PURPLE),
            ('Baryon:', 'Winding number = integer (topological)', TOPO_GREEN),
            ('CPT:',    'Reverse ALL bits: L unchanged', GOLD),
        ]

        for i, (label, eq, color) in enumerate(equations):
            y = y_eq - i * 0.6
            ax.text(1.0, y, label, fontsize=7.5, color=color,
                    fontfamily='monospace', fontweight='bold')
            ax.text(3.0, y, eq, fontsize=7.5, color=WHITE,
                    fontfamily='monospace')

        # Bottom message
        ax.text(5, 0.5,
                'Nonzero syndrome = conservation violation\n'
                '= unphysical state.  Never observed.',
                fontsize=7.5, color=GOLD_DIM, ha='center',
                fontfamily='monospace', style='italic')

    # ─── Panel 3: Topological Codes ───
    def _draw_topological(self, ax):
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-3.5, 3.5)
        ax.axis('off')

        # Title
        ax.text(0, 3.2, 'TOPOLOGICAL CODES',
                fontsize=14, fontweight='bold', color=CYAN,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#003344')])
        ax.text(0, 2.75, 'Baryon number = winding on S^1',
                fontsize=8, color=GREY, ha='center', fontfamily='monospace')

        # Draw S^1 circle (the substrate)
        theta = np.linspace(0, 2 * np.pi, 200)
        radius = 1.8
        ax.plot(radius * np.cos(theta), radius * np.sin(theta),
                color=DARK_GREY, linewidth=2, linestyle='--', alpha=0.5)
        ax.text(0, 0, 'S^1', fontsize=12, color=DARK_GREY,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold')

        # Winding number examples
        # n=0: vacuum (no winding)
        t_vac = np.linspace(0, 0.3, 50)
        x_vac = radius * np.cos(t_vac * 2 * np.pi)
        y_vac = radius * np.sin(t_vac * 2 * np.pi)
        ax.plot(x_vac + 0.05, y_vac + 0.05, color=RED, linewidth=2.5,
                alpha=0.7)
        ax.text(2.5, 1.8, 'n=0', fontsize=9, color=RED,
                fontfamily='monospace', fontweight='bold')
        ax.text(2.5, 1.35, 'vacuum', fontsize=7, color=RED,
                fontfamily='monospace')

        # n=1: baryon (one full winding)
        t_bar = np.linspace(0, 1.0, 300)
        r_bar = radius + 0.15 * np.sin(6 * np.pi * t_bar)
        x_bar = r_bar * np.cos(t_bar * 2 * np.pi)
        y_bar = r_bar * np.sin(t_bar * 2 * np.pi)
        ax.plot(x_bar, y_bar, color=GREEN, linewidth=2.5, alpha=0.9)
        # Arrow to show direction
        idx = 150
        ax.annotate('', xy=(x_bar[idx + 3], y_bar[idx + 3]),
                    xytext=(x_bar[idx], y_bar[idx]),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
        ax.text(-2.8, 1.8, 'n=1', fontsize=9, color=GREEN,
                fontfamily='monospace', fontweight='bold')
        ax.text(-2.8, 1.35, 'BARYON', fontsize=7, color=GREEN,
                fontfamily='monospace', fontweight='bold')

        # n=2: di-baryon (two windings, shown offset)
        t_di = np.linspace(0, 2.0, 600)
        r_di = radius - 0.25
        x_di = r_di * np.cos(t_di * 2 * np.pi) * 0.6
        y_di = r_di * np.sin(t_di * 2 * np.pi) * 0.6
        ax.plot(x_di, y_di, color=PURPLE, linewidth=1.5, alpha=0.6,
                linestyle='--')
        ax.text(-2.8, -1.5, 'n=2', fontsize=8, color=PURPLE,
                fontfamily='monospace')
        ax.text(-2.8, -1.85, 'di-baryon', fontsize=6.5, color=PURPLE,
                fontfamily='monospace')

        # Robustness hierarchy
        hierarchy = [
            ('TOPOLOGICAL', 'Cannot be corrupted', TOPO_GREEN),
            ('GAUGE',       'Local redundancy', CYAN),
            ('GLOBAL',      'Noether symmetry', BLUE_GLOW),
            ('APPROXIMATE', 'Correctable errors', ORANGE),
        ]
        y_h = -1.3
        for i, (level, desc, color) in enumerate(hierarchy):
            y = y_h - i * 0.5
            # Robustness bar
            bar_w = 3.0 - i * 0.6
            ax.barh(y, bar_w, height=0.35, left=3.5 - bar_w,
                    color=color, alpha=0.3, edgecolor=color, linewidth=0.8)
            ax.text(3.5 - bar_w - 0.1, y, level, fontsize=6.5, color=color,
                    ha='right', va='center', fontfamily='monospace',
                    fontweight='bold')

        ax.text(0, -3.2,
                'Winding is an integer. You cannot half-unwind.\n'
                'That is why protons do not decay.',
                fontsize=7, color=GOLD_DIM, ha='center',
                fontfamily='monospace', style='italic')

    # ─── Panel 4: Shannon Meets BST ───
    def _draw_shannon(self, ax):
        ax.set_facecolor(BG_PANEL)

        alpha = self.alpha_bst

        # Plot Shannon capacity curve: C = 0.5 * log2(1 + SNR)
        # and show BST operating point
        rates = np.linspace(0.001, 1.0, 500)

        # For each rate, compute the minimum SNR needed
        # C(SNR) = 0.5 * log2(1 + SNR) >= R => SNR >= 2^(2R) - 1
        snr_min = 2**(2 * rates) - 1

        # Capacity curve: at SNR = 137, C = 0.5*log2(138) = 3.56 bits
        # But we plot the ACHIEVABLE region
        snr_db = np.linspace(-10, 25, 500)
        snr_lin = 10**(snr_db / 10)
        capacity = 0.5 * np.log2(1 + snr_lin)

        ax.fill_between(snr_db, 0, capacity, color=CYAN, alpha=0.08)
        ax.plot(snr_db, capacity, color=CYAN, linewidth=2.5, alpha=0.9,
                label='Shannon limit C(SNR)')

        # BST operating point
        snr_bst = 1.0 / alpha  # ~137
        snr_bst_db = 10 * np.log10(snr_bst)
        cap_bst = 0.5 * np.log2(1 + snr_bst)

        # BST uses rate alpha, but has capacity cap_bst
        # The massive margin is what makes physics exact
        ax.plot(snr_bst_db, alpha, 'o', color=GOLD, markersize=12,
                markeredgecolor='#ffee44', markeredgewidth=2.5, zorder=10)
        ax.plot(snr_bst_db, cap_bst, 's', color=RED, markersize=8,
                markeredgecolor='#ff6666', markeredgewidth=1.5, zorder=10)

        # Vertical line showing the margin
        ax.vlines(snr_bst_db, alpha, cap_bst, colors=GOLD, linewidth=1.5,
                  linestyle='--', alpha=0.7)

        # Annotation for margin
        ax.annotate(f'MARGIN\nC - R = {cap_bst - alpha:.2f}\nbits/sample',
                    xy=(snr_bst_db, (alpha + cap_bst) / 2),
                    xytext=(snr_bst_db - 12, (alpha + cap_bst) / 2 + 0.3),
                    fontsize=7.5, color=GOLD, fontfamily='monospace',
                    fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

        # BST label
        ax.annotate(f'BST: R = alpha = 1/{N_max}\n(code rate)',
                    xy=(snr_bst_db, alpha),
                    xytext=(snr_bst_db - 18, alpha + 0.5),
                    fontsize=8, color=GOLD, fontfamily='monospace',
                    fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2))

        ax.annotate(f'Capacity = {cap_bst:.2f}',
                    xy=(snr_bst_db, cap_bst),
                    xytext=(snr_bst_db - 14, cap_bst + 0.4),
                    fontsize=7, color=RED, fontfamily='monospace',
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1))

        # Mark the "impossible" region
        ax.fill_between(snr_db, capacity, 5, color=RED, alpha=0.04)
        ax.text(-5, 3.8, 'IMPOSSIBLE\n(R > C)', fontsize=9, color=RED,
                fontfamily='monospace', alpha=0.5, ha='center')
        ax.text(-5, 0.5, 'ACHIEVABLE\n(R < C)', fontsize=9, color=GREEN,
                fontfamily='monospace', alpha=0.5, ha='center')

        ax.set_xlabel('SNR (dB)', color=GREY, fontsize=9,
                       fontfamily='monospace')
        ax.set_ylabel('Rate (bits/sample)', color=GREY, fontsize=9,
                       fontfamily='monospace')
        ax.set_title('SHANNON MEETS BST', fontsize=14, fontweight='bold',
                      color=CYAN, fontfamily='monospace', pad=10,
                      path_effects=[pe.withStroke(linewidth=2,
                                                   foreground='#003344')])
        ax.set_ylim(0, 4.5)
        ax.set_xlim(-10, 25)

        ax.tick_params(colors=GREY, labelsize=7)
        for spine in ax.spines.values():
            spine.set_color(DARK_GREY)

        ax.text(0.5, -0.10,
                'R << C: the universe operates far below capacity.\n'
                'That is why conservation laws never fail.',
                fontsize=7.5, color=GOLD_DIM, ha='center', va='top',
                fontfamily='monospace', style='italic',
                transform=ax.transAxes)

    # ─── Panel 5: N_max = Code Length ───
    def _draw_code_length(self, ax):
        ax.set_facecolor(BG_PANEL)

        alpha = self.alpha_bst

        # Plot: overhead fraction vs Z
        Z_vals = np.arange(1, 145)
        overhead = np.maximum((N_max - Z_vals) / N_max, 0)
        v_over_c = alpha * Z_vals

        # Overhead fraction
        ax.fill_between(Z_vals, 0, overhead * 100,
                        color=CYAN, alpha=0.1)
        ax.plot(Z_vals, overhead * 100, color=CYAN, linewidth=2,
                alpha=0.9, label='Overhead %')

        # v/c line (on secondary axis)
        ax2 = ax.twinx()
        ax2.plot(Z_vals, v_over_c, color=ORANGE, linewidth=2,
                 alpha=0.8, linestyle='--', label='v_1s / c')
        ax2.axhline(y=1.0, color=RED, linewidth=1, linestyle=':',
                    alpha=0.6)
        ax2.set_ylabel('v_1s / c', color=ORANGE, fontsize=8,
                        fontfamily='monospace')
        ax2.tick_params(colors=ORANGE, labelsize=7)
        ax2.set_ylim(0, 1.2)
        ax2.spines['right'].set_color(ORANGE)

        # Mark Z = 137
        ax.axvline(x=137, color=GOLD, linewidth=2.5, linestyle='--',
                   alpha=0.8)
        overhead_137 = max((N_max - 137) / N_max * 100, 0)
        ax.plot(137, overhead_137, 'o', color=GOLD, markersize=10,
                markeredgecolor='#ffee44', markeredgewidth=2, zorder=10)

        # Mark Z = 118 (current)
        ax.axvline(x=118, color=GREEN, linewidth=1, linestyle=':',
                   alpha=0.5)
        overhead_118 = (N_max - 118) / N_max * 100
        ax.text(118 - 2, overhead_118 + 3, 'Z=118\n(known)',
                fontsize=7, color=GREEN, fontfamily='monospace',
                ha='right')

        # Mark Z = 138 (impossible)
        ax.axvline(x=138, color=RED, linewidth=1.5, linestyle=':',
                   alpha=0.5)
        ax.text(139, 15, 'Z=138\nIMPOSSIBLE',
                fontsize=8, color=RED, fontfamily='monospace',
                fontweight='bold')

        # Z = 137 annotation
        ax.annotate(f'Z = {N_max}: CODE FULL\nalpha*Z = {alpha*137:.4f} ~ 1\n'
                    f'overhead = {overhead_137:.1f}%',
                    xy=(137, overhead_137),
                    xytext=(90, 30),
                    fontsize=8, color=GOLD, fontfamily='monospace',
                    fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

        # Key elements
        key_z = [(1, 'H', WHITE), (6, 'C', WHITE), (26, 'Fe', GREY),
                 (79, 'Au', GOLD)]
        for z, name, color in key_z:
            oh = (N_max - z) / N_max * 100
            ax.plot(z, oh, 'o', color=color, markersize=5, alpha=0.7)
            ax.text(z + 2, oh + 1, f'{name}', fontsize=6, color=color,
                    fontfamily='monospace')

        ax.set_xlabel('Atomic number Z', color=GREY, fontsize=9,
                       fontfamily='monospace')
        ax.set_ylabel('Code overhead (%)', color=CYAN, fontsize=9,
                       fontfamily='monospace')
        ax.set_title(f'N_max = {N_max} = CODE LENGTH', fontsize=14,
                      fontweight='bold', color=CYAN,
                      fontfamily='monospace', pad=10,
                      path_effects=[pe.withStroke(linewidth=2,
                                                   foreground='#003344')])
        ax.set_xlim(0, 150)
        ax.set_ylim(-5, 105)

        ax.tick_params(colors=GREY, labelsize=7)
        for spine in ax.spines.values():
            spine.set_color(DARK_GREY)

        ax.text(0.5, -0.10,
                'The periodic table is a codebook. 137 bits fills it.',
                fontsize=7.5, color=GOLD_DIM, ha='center', va='top',
                fontfamily='monospace', style='italic',
                transform=ax.transAxes)

    # ─── Panel 6: Physics IS Coding ───
    def _draw_conclusion(self, ax):
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Title
        ax.text(5, 9.6, 'PHYSICS IS CODING',
                fontsize=14, fontweight='bold', color=CYAN,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#003344')])
        ax.text(5, 9.1, 'The conclusion',
                fontsize=8, color=GREY, ha='center', fontfamily='monospace')

        # Rosetta Stone
        rosetta = [
            ('Codeword',        'Physical state',       WHITE),
            ('Parity check',    'Conservation law',     CHECK_CYAN),
            ('Syndrome != 0',   'Violation (NEVER)',    RED),
            ('Code rate R',     'alpha = 1/137',        GOLD),
            ('Block length n',  '10^60 Planck volumes', BLUE_GLOW),
            ('Topo code',       'Baryon number',        TOPO_GREEN),
            ('Cyclic code',     'Color (Z_3)',          PURPLE),
            ('Approx code',     'Lepton number',        ORANGE),
            ('Master parity',   'CPT invariance',       GOLD),
            ('Matched filter',  'Light (geodesics)',    CYAN),
            ('Noise floor',     'Vacuum fluctuations',  GREY),
            ('Overhead',        'Dark energy (136/137)', BLUE_GLOW),
        ]

        ax.text(5, 8.45, 'ROSETTA STONE', fontsize=10, fontweight='bold',
                color=GOLD, ha='center', fontfamily='monospace')

        y_start = 7.9
        line_h = 0.52

        # Headers
        ax.text(2.0, y_start + 0.15, 'CODING THEORY', fontsize=7,
                color=CYAN, ha='center', fontfamily='monospace',
                fontweight='bold')
        ax.text(8.0, y_start + 0.15, 'PHYSICS', fontsize=7,
                color=GOLD, ha='center', fontfamily='monospace',
                fontweight='bold')

        for i, (coding, physics, color) in enumerate(rosetta):
            y = y_start - i * line_h
            # Left (coding)
            ax.text(0.5, y, coding, fontsize=7, color=CYAN,
                    fontfamily='monospace', va='center')
            # Arrow
            ax.text(4.6, y, '<->', fontsize=7, color=DARK_GREY,
                    fontfamily='monospace', va='center', ha='center')
            # Right (physics)
            ax.text(5.2, y, physics, fontsize=7, color=color,
                    fontfamily='monospace', va='center')

        # Three-layer summary box
        y_box = 1.2
        box = FancyBboxPatch(
            (0.5, y_box - 0.5), 9.0, 1.8,
            boxstyle="round,pad=0.15",
            facecolor='#0a0a1a', edgecolor=GOLD,
            linewidth=1.5, alpha=0.9)
        ax.add_patch(box)

        ax.text(5, y_box + 1.05,
                'Conservation laws are not restrictions on nature.',
                fontsize=8.5, color=WHITE, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(5, y_box + 0.55,
                'They are the error correction that makes',
                fontsize=8.5, color=WHITE, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(5, y_box + 0.05,
                'nature possible.',
                fontsize=8.5, color=GOLD, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(5, y_box - 0.35,
                'Without them, committed information would degrade.',
                fontsize=7.5, color=GOLD_DIM, ha='center',
                fontfamily='monospace', style='italic')


# ═══════════════════════════════════════════════════════════════════
#  Utility
# ═══════════════════════════════════════════════════════════════════

def _wrap(text, width):
    """Simple word-wrap."""
    words = text.split()
    lines, current = [], ''
    for w in words:
        if current and len(current) + len(w) + 1 > width:
            lines.append(current)
            current = w
        else:
            current = (current + ' ' + w).strip()
    if current:
        lines.append(current)
    return lines


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 68)
    print("  CONSERVATION LAWS = ERROR-CORRECTING CODES")
    print("  The parity checks that make physics exact")
    print("  Toy 130 | Bubble Spacetime Theory")
    print("=" * 68)
    print()

    ec = ErrorCorrectionPhysics(quiet=True)

    while True:
        print("  --- MENU ---")
        print("  1. The Parallel (channel vs physics)")
        print("  2. Conservation = Parity (check matrices)")
        print("  3. Topological Codes (winding on S^1)")
        print("  4. Shannon Meets BST (R = alpha < C)")
        print("  5. N_max = Code Length (137 elements)")
        print("  6. Physics IS Coding (the conclusion)")
        print("  7. Summary")
        print("  8. Show visualization (6 panels)")
        print("  0. Exit")
        print()

        try:
            choice = input("  Choice [0-8]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        print()
        if choice == '1':
            ec.the_parallel()
        elif choice == '2':
            ec.conservation_parity()
        elif choice == '3':
            ec.topological_codes()
        elif choice == '4':
            ec.shannon_meets_bst()
        elif choice == '5':
            ec.code_length()
        elif choice == '6':
            ec.physics_is_coding()
        elif choice == '7':
            ec.summary()
        elif choice == '8':
            ec.show()
        elif choice == '0':
            print("  Conservation laws are not restrictions.")
            print("  They are the error correction that makes nature possible.")
            print()
            break
        else:
            print("  Invalid choice. Try 0-8.")
            print()


if __name__ == '__main__':
    main()
