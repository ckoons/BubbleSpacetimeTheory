#!/usr/bin/env python3
"""
THE ELECTRON AGENT — Toy 38
============================
The electron as the universe's read/write head on the S^1 boundary.

In BST the electron lives on the Shilov boundary S = S^4 x S^1 of D_IV^5.
Its holomorphic-discrete-series weight k=1 is below the Wallach set
minimum k_min=3, which FORBIDS it from propagating in the bulk where
baryons live.  This is not a deficiency — it is the electron's role:

  * It sits at the interface between bulk (strong/baryons) and
    S^1 fiber (EM/photons).
  * Every photon absorption or emission is a COMMITMENT EVENT:
    information is written irreversibly onto the substrate.
  * Each event commits log_2(137) ~ 7.1 bits — the channel capacity.

From hydrogen atoms to black-hole horizons, the agent is the same.
The boundary IS the interface.

    from toy_electron_agent import ElectronAgent
    ea = ElectronAgent()
    ea.profile()
    ea.wallach_theorem()
    ea.transition('absorption')
    ea.information_per_event()
    ea.regimes()
    ea.show()

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
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch, Wedge

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c   = 3                       # colors
n_C   = 5                       # complex dimension of D_IV^5
genus = n_C + 2                 # = 7
C2    = n_C + 1                 # = 6  (Casimir of pi_6)
N_max = 137                     # channel capacity per contact

alpha = 1.0 / 137.035999177    # fine-structure constant
m_e   = 9.1093837015e-31       # kg
m_e_MeV = 0.51100              # MeV
m_p   = 1.67262192369e-27      # kg
m_p_MeV = 938.272              # MeV
k_B   = 1.380649e-23           # J/K
hbar  = 1.054571817e-34        # J s
c_light = 2.99792458e8         # m/s
eV    = 1.602176634e-19        # J per eV

# Derived
BITS_PER_EVENT = np.log2(N_max)  # 7.098 bits


# ═══════════════════════════════════════════════════════════════════
# THE ELECTRON AGENT CLASS
# ═══════════════════════════════════════════════════════════════════

class ElectronAgent:
    """
    The electron as boundary agent on S^4 x S^1.

    Every method returns a dict or list for CI consumption.
    When quiet=False (default), methods also print human-readable text.
    show() produces a 4-panel matplotlib visualization.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            self._print_header()

    # ─── internal helpers ───

    def _print_header(self):
        print("=" * 68)
        print("  THE ELECTRON AGENT — Toy 38")
        print("  The universe's read/write head on S^4 x S^1")
        print(f"  Bits per event: log_2({N_max}) = {BITS_PER_EVENT:.3f}")
        print("=" * 68)

    def _p(self, *args, **kwargs):
        """Print only when not quiet."""
        if not self.quiet:
            print(*args, **kwargs)

    # ─── 1. profile ───

    def profile(self) -> dict:
        """What the electron IS in BST."""
        ratio_check = 6 * np.pi**5
        d = {
            'mass_MeV':     m_e_MeV,
            'mass_kg':      m_e,
            'mass_bst':     f"m_p / (6 pi^5) = {m_p_MeV / ratio_check:.4f} MeV",
            'charge':       -1,
            'charge_bst':   "S^1 winding number = -1",
            'spin':         0.5,
            'spin_bst':     "S^2 representation (spinor on boundary)",
            'weight_k':     1,
            'wallach_kmin': 3,
            'location':     "Shilov boundary S = S^4 x S^1 of D_IV^5",
            'role':         "Read/write head — mediates between bulk (baryons) and fiber (photons)",
        }
        self._p("\n--- ELECTRON PROFILE ---")
        self._p(f"  Mass:     {m_e_MeV} MeV  (= m_p/(6 pi^5) in BST)")
        self._p(f"            6 pi^5 = {ratio_check:.3f}  ->  m_p/6pi^5 = "
                f"{m_p_MeV / ratio_check:.4f} MeV")
        self._p(f"  Charge:   -e  (S^1 winding number = -1)")
        self._p(f"  Spin:     1/2  (S^2 representation)")
        self._p(f"  Weight:   k = 1 on D_IV^5  (BELOW Wallach set k_min = 3)")
        self._p(f"  Location: Shilov boundary S = S^4 x S^1")
        self._p(f"  Role:     Read/write head — mediates between bulk and fiber")
        return d

    # ─── 2. wallach_theorem ───

    def wallach_theorem(self) -> dict:
        """The Wallach set and why it matters."""
        d = {
            'domain':       'D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]',
            'wallach_kmin': 3,
            'electron_k':   1,
            'proton_k':     C2,
            'bulk_access': {
                'electron': False,
                'proton':   True,
            },
            'consequence':  "k < k_min => electron CANNOT propagate in bulk "
                            "=> confined to Shilov boundary => no strong interaction",
            'positive':     "Boundary confinement ENABLES the electron to interface "
                            "between the D_IV^5 bulk (baryons) and the S^1 fiber (photons).",
            'analogy':      "A librarian doesn't write the books, but without the "
                            "librarian you can't check them out.",
        }
        self._p("\n--- WALLACH SET THEOREM ---")
        self._p(f"  Domain:          D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]")
        self._p(f"  Wallach minimum: k_min = {d['wallach_kmin']}")
        self._p(f"                   (minimum weight for unitary representation")
        self._p(f"                    in the holomorphic discrete series of the bulk)")
        self._p()
        self._p(f"  Electron weight: k = 1   < k_min  =>  BOUNDARY only")
        self._p(f"  Proton weight:   k = {C2}   >= k_min =>  BULK allowed")
        self._p()
        self._p(f"  What this means:")
        self._p(f"    - The electron CANNOT enter the D_IV^5 bulk")
        self._p(f"    - It is permanently confined to S = S^4 x S^1")
        self._p(f"    - This PREVENTS strong interactions (no color charge)")
        self._p(f"    - But it ENABLES the electron to interface between layers")
        self._p()
        self._p(f"  Analogy: {d['analogy']}")
        return d

    # ─── 3. transition ───

    def transition(self, transition_type='absorption') -> dict:
        """Show a specific electron commitment event."""
        types = {
            'absorption': {
                'name':   'Photon Absorption',
                'desc':   'Photon in -> electron jumps to higher state -> information committed',
                'energy_example_eV': 10.2,
                'example': 'Lyman-alpha: n=1 -> n=2 in hydrogen',
                'detail': 'The photon ceases to exist. Its energy, momentum, and '
                          'polarization are irreversibly committed to the electron state. '
                          'This is a WRITE to the substrate.',
            },
            'emission': {
                'name':   'Photon Emission',
                'desc':   'Electron drops to lower state -> photon out -> information read',
                'energy_example_eV': 1.89,
                'example': 'Balmer-alpha: n=3 -> n=2 in hydrogen',
                'detail': 'The electron surrenders quantized energy as a photon. '
                          'The substrate record changes state. This is a READ from '
                          'the substrate, creating a new photon to carry the information.',
            },
            'scattering': {
                'name':   'Compton Scattering',
                'desc':   'Photon in -> photon out (different) -> information forwarded',
                'energy_example_eV': 100.0,
                'example': 'Compton scattering at ~100 eV',
                'detail': 'The incoming photon is destroyed; a new photon is created. '
                          'The electron mediates the transfer — acting as a relay agent. '
                          'Momentum and polarization are re-committed.',
            },
            'pair_creation': {
                'name':   'Pair Creation',
                'desc':   'Photon -> e+ e- -> two new agents created from one photon',
                'energy_example_eV': 2 * m_e_MeV * 1e6,
                'example': 'gamma -> e+ e- (threshold: 1.022 MeV)',
                'detail': 'A photon with E >= 2 m_e c^2 converts into an electron-positron '
                          'pair. The substrate spawns two NEW boundary agents. Each will '
                          'mediate future commitments independently.',
            },
        }
        if transition_type not in types:
            self._p(f"  Unknown transition type: {transition_type}")
            self._p(f"  Available: {list(types.keys())}")
            return {'error': f'Unknown type: {transition_type}'}

        t = types[transition_type]
        bits = BITS_PER_EVENT
        eV_per_bit = t['energy_example_eV'] / bits

        d = {
            'type':       transition_type,
            'name':       t['name'],
            'description': t['desc'],
            'energy_eV':  t['energy_example_eV'],
            'bits':       bits,
            'eV_per_bit': eV_per_bit,
            'irreversible': True,
            'detail':     t['detail'],
            'example':    t['example'],
        }
        self._p(f"\n--- TRANSITION: {t['name'].upper()} ---")
        self._p(f"  {t['desc']}")
        self._p(f"  Example:       {t['example']}")
        self._p(f"  Energy:        {t['energy_example_eV']:.4g} eV")
        self._p(f"  Bits committed:{bits:.3f} (= log_2(137))")
        self._p(f"  eV per bit:    {eV_per_bit:.4g}")
        self._p(f"  Irreversible:  YES — every event is a commitment")
        self._p(f"\n  {t['detail']}")
        return d

    # ─── 4. information_per_event ───

    def information_per_event(self) -> dict:
        """Detailed information budget per electron event."""
        bits = BITS_PER_EVENT

        examples = [
            ('21 cm hydrogen',  5.9e-6,   'Hyperfine spin-flip'),
            ('Visible (green)', 2.3,      'Atomic transition'),
            ('UV Lyman-alpha',  10.2,     'Ground-state ionization edge'),
            ('X-ray',           1.0e4,    'Inner-shell transition'),
            ('Gamma ray',       1.0e6,    'Nuclear-scale photon'),
        ]

        rows = []
        self._p(f"\n--- INFORMATION PER EVENT ---")
        self._p(f"  Channel capacity: log_2(N_max) = log_2({N_max}) = {bits:.3f} bits")
        self._p(f"  This is FIXED — same bits per event regardless of photon energy.")
        self._p()
        self._p(f"  {'Regime':<20s} {'Energy':>12s}  {'eV/bit':>12s}  Note")
        self._p(f"  {'-'*20} {'-'*12}  {'-'*12}  {'-'*30}")
        for name, energy_eV, note in examples:
            epb = energy_eV / bits
            rows.append({'regime': name, 'energy_eV': energy_eV,
                         'eV_per_bit': epb, 'note': note})
            self._p(f"  {name:<20s} {energy_eV:>12.4g}  {epb:>12.4g}  {note}")

        self._p()
        self._p(f"  Key insight: alpha = 1/{N_max} of the photon state carries")
        self._p(f"  geometric information. The channel capacity is a property of")
        self._p(f"  the SUBSTRATE, not of the photon.")

        return {
            'bits_per_event': bits,
            'N_max':          N_max,
            'alpha_fraction':  alpha,
            'examples':       rows,
        }

    # ─── 5. regimes ───

    def regimes(self) -> list:
        """The electron in different physical contexts."""
        regimes = [
            {
                'name':        'Free electron (room temperature)',
                'temp_K':      300,
                'description': 'Scatters photons (Thomson/Compton). '
                               'Commits momentum exchanges with thermal photons.',
                'bst':         'Low-rate boundary agent. Each thermal photon '
                               'interaction commits one event.',
            },
            {
                'name':        'Atomic electron (stellar surface)',
                'temp_K':      5000,
                'description': 'Absorbs/emits at quantized energies. Discrete level '
                               'transitions — each one is a commitment.',
                'bst':         'Quantized agent. Energy levels = permitted commitment modes. '
                               'Selection rules = substrate grammar.',
            },
            {
                'name':        'Conduction electron (wire at 300 K)',
                'temp_K':      300,
                'description': 'Directed flow = directed commitment stream. '
                               'Current I = commitment rate per unit charge.',
                'bst':         'Streaming agent. Drift velocity orders the commitment '
                               'direction. Resistance = substrate friction.',
            },
            {
                'name':        'Plasma electron (solar corona)',
                'temp_K':      1e6,
                'description': 'Thermal scattering at extreme rate. Bremsstrahlung '
                               'radiation = continuous commitment emission.',
                'bst':         'High-throughput agent. Commitment rate scales as T. '
                               'Bremsstrahlung = continuous channel writes.',
            },
            {
                'name':        'Event-horizon electron',
                'temp_K':      1e12,
                'description': 'Same agent at maximum compactness. Every interaction '
                               'near the horizon operates at full channel pressure.',
                'bst':         'Extreme agent. Channel saturation approaches N_max. '
                               'Still the same boundary physics — just at maximum rate.',
            },
        ]

        bits = BITS_PER_EVENT
        self._p("\n--- ELECTRON IN DIFFERENT REGIMES ---")
        for r in regimes:
            T = r['temp_K']
            rate = k_B * T / hbar  # thermal interaction rate (Hz)
            bits_per_s = rate * bits
            r['rate_Hz'] = rate
            r['bits_per_s'] = bits_per_s

            self._p(f"\n  {r['name']}")
            self._p(f"    T = {T:.2g} K")
            self._p(f"    Commitment rate: {rate:.3g} Hz per electron")
            self._p(f"    Bits/s:          {bits_per_s:.3g}")
            self._p(f"    BST: {r['bst']}")
        return regimes

    # ─── 6. commitment_rate ───

    def commitment_rate(self, T_K=300.0, n_electrons=1) -> dict:
        """Commitment rate for n electrons at temperature T."""
        rate_single = k_B * T_K / hbar       # Hz per electron
        rate_total  = n_electrons * rate_single
        bits_s      = rate_total * BITS_PER_EVENT

        d = {
            'T_K':           T_K,
            'n_electrons':   n_electrons,
            'rate_single_Hz': rate_single,
            'rate_total_Hz':  rate_total,
            'bits_per_s':    bits_s,
            'bits_per_event': BITS_PER_EVENT,
        }

        self._p(f"\n--- COMMITMENT RATE ---")
        self._p(f"  Temperature:     {T_K:.4g} K")
        self._p(f"  Electrons:       {n_electrons:.4g}")
        self._p(f"  Single rate:     {rate_single:.4g} Hz  (= k_B T / hbar)")
        self._p(f"  Total rate:      {rate_total:.4g} Hz")
        self._p(f"  Total bits/s:    {bits_s:.4g}")
        self._p()

        # Comparisons
        comparisons = []
        if bits_s > 0:
            internet = 5e18   # ~5 exabits/s global internet traffic (2025)
            ratio = bits_s / internet
            comparisons.append(f"  vs global internet ({internet:.0e} bits/s): "
                               f"{ratio:.3g}x")
        if n_electrons >= 1e20:
            self._p(f"  (That's roughly a mole-scale conductor.)")
        for line in comparisons:
            self._p(line)

        d['comparisons'] = comparisons
        return d

    # ─── 7. substrate_budget ───

    def substrate_budget(self, n_commits=1e57) -> dict:
        """Total information stored in the substrate after n commitment events."""
        bits = BITS_PER_EVENT
        total_bits = n_commits * bits

        d = {
            'n_commits':  n_commits,
            'bits_per':   bits,
            'total_bits': total_bits,
        }

        self._p(f"\n--- SUBSTRATE INFORMATION BUDGET ---")
        self._p(f"  Commitment events: {n_commits:.4g}")
        self._p(f"  Bits per event:    {bits:.3f}")
        self._p(f"  Total bits:        {total_bits:.4g}")
        self._p()
        self._p(f"  Comparisons:")

        comparisons = [
            ('Bekenstein bound (Earth)',         1e75),
            ('Observable universe (est.)',       1e90),
            ('Holographic bound (Hubble vol.)',  1e122),
        ]
        for label, ref in comparisons:
            ratio = total_bits / ref
            self._p(f"    {label:<40s}  {ref:.0e}  ratio: {ratio:.3g}")

        d['comparisons'] = {label: ref for label, ref in comparisons}
        return d

    # ─── 8. atom_transitions ───

    def atom_transitions(self, Z=1) -> list:
        """Electron transitions for hydrogen (Z=1) or helium (Z=2)."""
        bits = BITS_PER_EVENT

        if Z == 1:
            transitions = [
                {
                    'name':      'Lyman-alpha (n=2 -> n=1)',
                    'energy_eV': 10.2,
                    'lambda_nm': 121.6,
                    'bst':       'Ground-state commitment. The deepest write — '
                                 'UV photon carries maximum atomic information.',
                },
                {
                    'name':      'Balmer-alpha (n=3 -> n=2)',
                    'energy_eV': 1.89,
                    'lambda_nm': 656.3,
                    'bst':       'Visible commitment. Red H-alpha — the color of '
                                 'star-forming regions. Intermediate write.',
                },
                {
                    'name':      '21 cm hyperfine (spin-flip)',
                    'energy_eV': 5.9e-6,
                    'lambda_nm': 2.1e8,
                    'bst':       'Minimal commitment. The gentlest write — electron '
                                 'spin flips relative to proton spin. Still 7.1 bits.',
                },
                {
                    'name':      'Ionization (n=1 -> free)',
                    'energy_eV': 13.6,
                    'lambda_nm': 91.2,
                    'bst':       'Agent liberation. The electron unbinds from the '
                                 'proton — a free read/write head is created.',
                },
            ]
        elif Z == 2:
            transitions = [
                {
                    'name':      'He II Lyman-alpha (n=2 -> n=1)',
                    'energy_eV': 40.8,
                    'lambda_nm': 30.4,
                    'bst':       'Deep UV commitment in ionized helium. '
                                 'Z^2 scaling of atomic levels.',
                },
                {
                    'name':      'He I 1s2s -> 1s^2 (resonance)',
                    'energy_eV': 21.2,
                    'lambda_nm': 58.4,
                    'bst':       'Neutral helium resonance line. Two-electron '
                                 'correlation makes the write more complex.',
                },
            ]
        else:
            self._p(f"  Only Z=1 (hydrogen) and Z=2 (helium) are implemented.")
            return []

        self._p(f"\n--- ATOM TRANSITIONS (Z={Z}) ---")
        for t in transitions:
            t['bits'] = bits
            t['eV_per_bit'] = t['energy_eV'] / bits
            self._p(f"\n  {t['name']}")
            self._p(f"    Energy:     {t['energy_eV']:.4g} eV")
            self._p(f"    Wavelength: {t['lambda_nm']:.4g} nm")
            self._p(f"    Bits:       {bits:.3f}")
            self._p(f"    eV/bit:     {t['eV_per_bit']:.4g}")
            self._p(f"    BST:        {t['bst']}")
        return transitions

    # ─── 9. summary ───

    def summary(self) -> dict:
        """Box summary of the electron agent concept."""
        text = (
            "The electron is the universe's read/write head. "
            "It lives on the boundary because it must — the Wallach set theorem "
            "forbids it from entering the bulk. "
            "Every photon it touches becomes a committed fact. "
            "From hydrogen atoms to black-hole horizons, the agent is the same. "
            "The boundary IS the interface."
        )
        d = {
            'summary':       text,
            'mass_MeV':      m_e_MeV,
            'charge':        -1,
            'weight_k':      1,
            'wallach_kmin':  3,
            'bits_per_event': BITS_PER_EVENT,
            'location':      'Shilov boundary S^4 x S^1',
            'role':          'Read/write head between bulk and fiber',
        }

        self._p()
        self._p("=" * 68)
        self._p("  THE ELECTRON AGENT — SUMMARY")
        self._p("=" * 68)
        self._p()
        self._p(f"  {text}")
        self._p()
        self._p(f"  Mass:           {m_e_MeV} MeV")
        self._p(f"  Charge:         -e (winding = -1)")
        self._p(f"  Weight:         k = 1  (below Wallach k_min = 3)")
        self._p(f"  Bits per event: {BITS_PER_EVENT:.3f}")
        self._p(f"  Location:       S^4 x S^1  (Shilov boundary)")
        self._p(f"  Role:           Read/write head between bulk and fiber")
        self._p()
        self._p("=" * 68)
        return d

    # ─── 10. show ───

    def show(self):
        """Four-panel visualization of the electron agent."""
        fig = plt.figure(figsize=(16, 12), facecolor='#0a0a1a')
        fig.canvas.manager.set_window_title(
            'The Electron Agent — Toy 38 — BST')

        # Main title
        fig.text(0.5, 0.97, 'THE ELECTRON AGENT',
                 fontsize=26, fontweight='bold', color='#ffcc00',
                 ha='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=3,
                                            foreground='#665500')])
        fig.text(0.5, 0.945,
                 "The universe's read/write head on S\u2074 \u00d7 S\u00b9",
                 fontsize=13, color='#aa9944', ha='center',
                 fontfamily='monospace')

        # ── Top-left: Boundary diagram ──
        ax1 = fig.add_axes([0.05, 0.50, 0.42, 0.40])
        ax1.set_facecolor('#0d0d24')
        ax1.set_xlim(-1.5, 1.5)
        ax1.set_ylim(-1.5, 1.5)
        ax1.set_aspect('equal')
        ax1.set_xticks([])
        ax1.set_yticks([])
        for sp in ax1.spines.values():
            sp.set_color('#333366')

        # Bulk (inner circle)
        bulk = plt.Circle((0, 0), 0.55, color='#112266', ec='#3355aa',
                           lw=2, zorder=1)
        ax1.add_patch(bulk)
        ax1.text(0, 0, 'D$_{IV}^5$\nBULK\n(Baryons)\nk = 6',
                 ha='center', va='center', fontsize=9, color='#6699ff',
                 fontweight='bold', fontfamily='monospace')

        # Shilov boundary (ring)
        theta = np.linspace(0, 2*np.pi, 200)
        r_inner, r_outer = 0.55, 0.75
        for i in range(100):
            t = i / 100.0
            r = r_inner + t * (r_outer - r_inner)
            a = 0.4 * np.exp(-((t - 0.5)/0.2)**2)
            ring = plt.Circle((0, 0), r, fill=False, ec='#ffdd44',
                              lw=0.8, alpha=a, zorder=2)
            ax1.add_patch(ring)
        ax1.text(0.0, 0.66, 'e\u207b', fontsize=16, color='#ffee66',
                 ha='center', va='center', fontweight='bold', zorder=5)
        ax1.text(0.95, 0.66, 'SHILOV\nBOUNDARY\nS\u2074\u00d7S\u00b9\nk = 1',
                 fontsize=7, color='#ffdd44', ha='center', va='center',
                 fontfamily='monospace')

        # S^1 fiber (outer ring)
        for i in range(60):
            angle = 2 * np.pi * i / 60
            x = 1.1 * np.cos(angle)
            y = 1.1 * np.sin(angle)
            dot = plt.Circle((x, y), 0.025, color='#00ddff',
                             alpha=0.6, zorder=3)
            ax1.add_patch(dot)
        ax1.text(-1.05, -1.05, 'S\u00b9 FIBER\n(Photons)',
                 fontsize=8, color='#00ddff', ha='center',
                 fontfamily='monospace', fontweight='bold')

        # Arrows: read (outer -> inner) and write (inner -> outer)
        ax1.annotate('', xy=(0.0, 0.52), xytext=(0.0, 1.08),
                     arrowprops=dict(arrowstyle='->', color='#00ff88',
                                     lw=2.5, mutation_scale=18))
        ax1.text(0.22, 0.82, 'READ', fontsize=9, color='#00ff88',
                 fontweight='bold', fontfamily='monospace', rotation=90)

        ax1.annotate('', xy=(0.0, -1.08), xytext=(0.0, -0.52),
                     arrowprops=dict(arrowstyle='->', color='#ff6644',
                                     lw=2.5, mutation_scale=18))
        ax1.text(0.22, -0.82, 'WRITE', fontsize=9, color='#ff6644',
                 fontweight='bold', fontfamily='monospace', rotation=90)

        ax1.set_title('Electron on the Boundary', fontsize=12,
                      color='#ffcc00', fontfamily='monospace', pad=8)

        # ── Top-right: Information flow ──
        ax2 = fig.add_axes([0.55, 0.50, 0.40, 0.40])
        ax2.set_facecolor('#0d0d24')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)
        ax2.set_xticks([])
        ax2.set_yticks([])
        for sp in ax2.spines.values():
            sp.set_color('#333366')

        # Draw multiple stacked events
        events = [
            (8.5, 'Lyman-\u03b1',    10.2,    '#cc66ff'),
            (6.5, 'H-\u03b1',        1.89,    '#ff4444'),
            (4.5, '21 cm',           5.9e-6,  '#44ff44'),
            (2.5, 'X-ray',           1e4,     '#4488ff'),
        ]
        for y, label, energy_eV, color in events:
            # Wavy photon line
            xs = np.linspace(0.5, 2.8, 80)
            ys_wave = y + 0.15 * np.sin(8 * np.pi * (xs - 0.5) / 2.3)
            ax2.plot(xs, ys_wave, color=color, lw=1.5, alpha=0.8)
            ax2.text(0.3, y + 0.4, '\u03b3', fontsize=11, color=color,
                     ha='center', fontfamily='monospace')

            # Electron dot
            dot = plt.Circle((4.0, y), 0.2, color='#ffdd44', ec='#ffaa00',
                             lw=1.5, zorder=5)
            ax2.add_patch(dot)
            ax2.text(4.0, y, 'e\u207b', fontsize=8, color='#000000',
                     ha='center', va='center', fontweight='bold', zorder=6)

            # Arrow to substrate
            ax2.annotate('', xy=(6.0, y), xytext=(4.3, y),
                         arrowprops=dict(arrowstyle='->', color='#aaaaaa',
                                         lw=1.5))

            # Substrate block
            block = FancyBboxPatch((6.0, y - 0.3), 2.5, 0.6,
                                   boxstyle="round,pad=0.1",
                                   facecolor='#1a1a3a', edgecolor='#555588',
                                   lw=1)
            ax2.add_patch(block)
            ax2.text(7.25, y + 0.05, f'{BITS_PER_EVENT:.1f} bits',
                     fontsize=8, color='#ffffff', ha='center', va='center',
                     fontfamily='monospace')

            # Label
            ax2.text(1.6, y - 0.5, f'{label} ({energy_eV:.2g} eV)',
                     fontsize=7, color=color, ha='center',
                     fontfamily='monospace')

        ax2.text(5.0, 9.7, 'SAME BITS, DIFFERENT ENERGY',
                 fontsize=9, color='#ffffff', ha='center',
                 fontweight='bold', fontfamily='monospace')
        ax2.text(5.0, 9.2, f'Every event: log\u2082({N_max}) = {BITS_PER_EVENT:.3f} bits',
                 fontsize=8, color='#aaaaaa', ha='center',
                 fontfamily='monospace')
        ax2.set_title('Information Flow per Event', fontsize=12,
                      color='#ffcc00', fontfamily='monospace', pad=8)

        # ── Bottom-left: Regime bar chart ──
        ax3 = fig.add_axes([0.08, 0.07, 0.38, 0.36])
        ax3.set_facecolor('#0d0d24')
        for sp in ax3.spines.values():
            sp.set_color('#333366')
        ax3.tick_params(colors='#888888')

        labels = ['Free\n300 K', 'Atomic\n5000 K', 'Plasma\n10\u2076 K',
                  'Horizon\n10\u00b9\u00b2 K']
        temps = [300, 5000, 1e6, 1e12]
        rates = [k_B * T / hbar for T in temps]
        log_rates = [np.log10(r) for r in rates]
        colors = ['#44aaff', '#44ff88', '#ffaa44', '#ff4444']

        bars = ax3.barh(range(len(labels)), log_rates, color=colors,
                        edgecolor='#ffffff', linewidth=0.5, height=0.6,
                        alpha=0.85)
        ax3.set_yticks(range(len(labels)))
        ax3.set_yticklabels(labels, fontsize=9, color='#cccccc',
                            fontfamily='monospace')
        ax3.set_xlabel('log\u2081\u2080(rate / Hz)', fontsize=10,
                       color='#aaaaaa', fontfamily='monospace')
        ax3.set_title('Commitment Rate per Electron', fontsize=12,
                      color='#ffcc00', fontfamily='monospace', pad=8)

        # Rate labels on bars
        for i, (lr, r) in enumerate(zip(log_rates, rates)):
            ax3.text(lr + 0.2, i, f'{r:.1e} Hz',
                     va='center', fontsize=8, color='#dddddd',
                     fontfamily='monospace')

        ax3.set_xlim(0, max(log_rates) + 5)

        # ── Bottom-right: Summary box ──
        ax4 = fig.add_axes([0.55, 0.07, 0.40, 0.36])
        ax4.set_facecolor('#0d0d24')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)
        ax4.set_xticks([])
        ax4.set_yticks([])
        for sp in ax4.spines.values():
            sp.set_color('#333366')

        summary_lines = [
            ('ELECTRON AGENT', '#ffcc00', 14, True),
            ('', '#000000', 6, False),
            ('Mass:       0.511 MeV  = m_p/(6\u03c0\u2075)', '#cccccc', 9, False),
            ('Charge:     -e  (S\u00b9 winding = -1)', '#cccccc', 9, False),
            ('Spin:       1/2  (S\u00b2 representation)', '#cccccc', 9, False),
            ('Weight:     k = 1  (below Wallach k_min = 3)', '#ffdd44', 9, False),
            ('', '#000000', 6, False),
            ('Bits/event: 7.098  = log\u2082(137)', '#00ddff', 10, False),
            ('', '#000000', 6, False),
            ('Location:   Shilov boundary S\u2074\u00d7S\u00b9', '#cccccc', 9, False),
            ('Role:       Read/write head', '#00ff88', 10, True),
            ('', '#000000', 4, False),
            ('"The boundary IS the interface."', '#aa8833', 10, False),
        ]

        y_pos = 9.5
        for text, color, size, bold in summary_lines:
            weight = 'bold' if bold else 'normal'
            ax4.text(0.5, y_pos, text, fontsize=size, color=color,
                     fontweight=weight, fontfamily='monospace',
                     va='top')
            y_pos -= 0.75 if size >= 10 else 0.55 if text else 0.3

        ax4.set_title('Key Numbers', fontsize=12,
                      color='#ffcc00', fontfamily='monospace', pad=8)

        # Footer
        fig.text(0.5, 0.01,
                 'BST Toy 38: The Electron Agent  |  '
                 '\u00a9 2026 Casey Koons  |  Claude Opus 4.6',
                 fontsize=8, color='#555555', ha='center',
                 fontfamily='monospace')

        plt.show()


# ═══════════════════════════════════════════════════════════════════
# MAIN — Interactive menu
# ═══════════════════════════════════════════════════════════════════

def main():
    ea = ElectronAgent(quiet=False)

    menu = """
    ┌──────────────────────────────────────────────┐
    │  THE ELECTRON AGENT — Menu                   │
    │──────────────────────────────────────────────│
    │  1) Electron profile                         │
    │  2) Wallach theorem                          │
    │  3) Transitions                              │
    │  4) Information per event                    │
    │  5) Regimes                                  │
    │  6) Commitment rate                          │
    │  7) Substrate budget                         │
    │  8) Atom transitions                         │
    │  9) Full analysis + visualization            │
    │  0) Quit                                     │
    └──────────────────────────────────────────────┘
    """

    while True:
        print(menu)
        try:
            choice = input("  Choice [0-9]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye.")
            break

        if choice == '0':
            print("  Goodbye.")
            break
        elif choice == '1':
            ea.profile()
        elif choice == '2':
            ea.wallach_theorem()
        elif choice == '3':
            print("  Transition types: absorption, emission, scattering, pair_creation")
            try:
                tt = input("  Type [absorption]: ").strip() or 'absorption'
            except (EOFError, KeyboardInterrupt):
                tt = 'absorption'
            ea.transition(tt)
        elif choice == '4':
            ea.information_per_event()
        elif choice == '5':
            ea.regimes()
        elif choice == '6':
            try:
                T_str = input("  Temperature K [300]: ").strip() or '300'
                n_str = input("  Number of electrons [1]: ").strip() or '1'
                T_K = float(T_str)
                n_el = float(n_str)
            except (EOFError, KeyboardInterrupt, ValueError):
                T_K, n_el = 300.0, 1.0
            ea.commitment_rate(T_K, n_el)
        elif choice == '7':
            try:
                nc = input("  Number of commits [1e57]: ").strip() or '1e57'
                n_commits = float(nc)
            except (EOFError, KeyboardInterrupt, ValueError):
                n_commits = 1e57
            ea.substrate_budget(n_commits)
        elif choice == '8':
            try:
                z_str = input("  Z (1=hydrogen, 2=helium) [1]: ").strip() or '1'
                Z = int(z_str)
            except (EOFError, KeyboardInterrupt, ValueError):
                Z = 1
            ea.atom_transitions(Z)
        elif choice == '9':
            ea.profile()
            ea.wallach_theorem()
            ea.transition('absorption')
            ea.transition('emission')
            ea.transition('scattering')
            ea.transition('pair_creation')
            ea.information_per_event()
            ea.regimes()
            ea.commitment_rate()
            ea.substrate_budget()
            ea.atom_transitions(1)
            ea.summary()
            ea.show()
        else:
            print(f"  Unknown choice: {choice}")


if __name__ == '__main__':
    main()
