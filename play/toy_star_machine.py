#!/usr/bin/env python3
"""
THE STAR MACHINE — Stellar Evolution Through the BST Lens
==========================================================
Toy 37. A star's life is a commitment budget.

Born with mass, spent as light, ending in geometry.

In BST every thermal contact is a commitment event — an irreversible
bit inscribed onto the D_IV^5 bulk. A star is a factory of commitments:
its core temperature sets the rate, its mass sets the budget, and its
remnant records the final channel state.

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
from matplotlib.widgets import RadioButtons
from matplotlib.patches import Circle, FancyBboxPatch
import matplotlib.patheffects as pe

# ═══════════════════════════════════════════════════════════════════
# BST Constants
# ═══════════════════════════════════════════════════════════════════
N_c = 3          # color charges
n_C = 5          # domain dimension
GENUS = 7        # genus of D_IV^5
C2 = 6           # Casimir invariant
N_MAX = 137      # Haldane channel cap

# Physical constants (SI)
k_B   = 1.380649e-23       # J/K
hbar  = 1.054571817e-34    # J s
G_N   = 6.67430e-11        # m^3 kg^-1 s^-2
c_light = 2.99792458e8     # m/s

# Astrophysical
M_SUN = 1.989e30           # kg
R_SUN = 6.957e8            # m
L_SUN = 3.828e26           # W
YEAR  = 3.15576e7          # seconds in a Julian year
MYR   = 1e6 * YEAR        # seconds in 1 Myr
MEV   = 1.602176634e-13    # J per MeV

# ─── Colors ───
BG         = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD       = '#ffd700'
GOLD_DIM   = '#aa8800'
WHITE      = '#ffffff'
GREY       = '#888888'
GREEN      = '#44ff88'
BLUE_GLOW  = '#4488ff'
RED_WARM   = '#ff4444'
ORANGE     = '#ff8800'
PURPLE     = '#8844cc'

# ═══════════════════════════════════════════════════════════════════
# Star Catalog
# ═══════════════════════════════════════════════════════════════════
STAR_CATALOG = {
    'O5': dict(mass=40.0, T_eff=42000, L=500000.0, R=12.0,
               T_core=50e6, lifetime=1.0, remnant='BH', color='#9bb0ff'),
    'B0': dict(mass=18.0, T_eff=30000, L=20000.0, R=7.4,
               T_core=35e6, lifetime=10.0, remnant='BH', color='#aabfff'),
    'B5': dict(mass=6.0,  T_eff=15400, L=800.0, R=3.9,
               T_core=27e6, lifetime=100.0, remnant='NS', color='#cad7ff'),
    'A0': dict(mass=2.9,  T_eff=9800,  L=54.0,  R=2.4,
               T_core=22e6, lifetime=400.0, remnant='WD', color='#f8f7ff'),
    'F0': dict(mass=1.6,  T_eff=7200,  L=6.5,   R=1.5,
               T_core=17e6, lifetime=3000.0, remnant='WD', color='#fff4ea'),
    'G2': dict(mass=1.0,  T_eff=5780,  L=1.0,   R=1.0,
               T_core=15e6, lifetime=10000.0, remnant='WD', color='#ffd2a1'),
    'K5': dict(mass=0.67, T_eff=4400,  L=0.15,  R=0.72,
               T_core=10e6, lifetime=30000.0, remnant='WD', color='#ffb56c'),
    'M2': dict(mass=0.4,  T_eff=3500,  L=0.03,  R=0.44,
               T_core=7e6,  lifetime=100000.0, remnant='WD', color='#ff8a3d'),
    'M5': dict(mass=0.2,  T_eff=3200,  L=0.003, R=0.27,
               T_core=5e6,  lifetime=500000.0, remnant='WD', color='#ff6a1a'),
}

SPECTRAL_ORDER = ['O5', 'B0', 'B5', 'A0', 'F0', 'G2', 'K5', 'M2', 'M5']


# ═══════════════════════════════════════════════════════════════════
# StarMachine — CI-scriptable API + GUI
# ═══════════════════════════════════════════════════════════════════

class StarMachine:
    """
    The Star Machine: stellar evolution through the BST lens.

    Every method prints human-readable output (unless quiet=True)
    and returns a dict or list for programmatic CI use.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet

    def _p(self, text):
        if not self.quiet:
            print(text)

    # ─── Helper computations ───

    @staticmethod
    def _commitment_rate(mass_solar, T_K):
        """C = M * T * k_B / hbar  (commitments per second)."""
        M = mass_solar * M_SUN
        return M * T_K * k_B / hbar

    @staticmethod
    def _compactness(mass_solar, R_solar):
        """xi = 2GM / (Rc^2), dimensionless compactness."""
        M = mass_solar * M_SUN
        R = R_solar * R_SUN
        if R <= 0:
            return 1.0
        return 2.0 * G_N * M / (R * c_light**2)

    @staticmethod
    def _schwarzschild_R(mass_solar):
        """Schwarzschild radius in solar radii."""
        M = mass_solar * M_SUN
        r_s = 2.0 * G_N * M / c_light**2
        return r_s / R_SUN

    # ─── 1. Star Profile ───

    def star_profile(self, spectral_type='G2'):
        """Show complete profile for a star type."""
        st = spectral_type.upper()
        if st not in STAR_CATALOG:
            self._p(f"Unknown spectral type: {st}")
            return {}
        s = STAR_CATALOG[st]
        cr = self._commitment_rate(s['mass'], s['T_core'])
        xi = self._compactness(s['mass'], s['R'])
        fill = xi * 100.0
        lapse = 1.0 - xi

        self._p(f"\n{'='*60}")
        self._p(f"  STAR PROFILE: {st}" + ("  (Sun)" if st == 'G2' else ""))
        self._p(f"{'='*60}")
        self._p(f"  Mass          : {s['mass']:.2f} M_sun")
        self._p(f"  T_eff         : {s['T_eff']:,.0f} K")
        self._p(f"  T_core        : {s['T_core']/1e6:.0f} MK")
        self._p(f"  Luminosity    : {s['L']:.4g} L_sun")
        self._p(f"  Radius        : {s['R']:.2f} R_sun")
        self._p(f"  Lifetime      : {s['lifetime']:,.0f} Myr")
        self._p(f"  Remnant       : {s['remnant']}")
        self._p(f"  Color         : {s['color']}")
        self._p(f"  ── BST Parameters ──")
        self._p(f"  Commitment rate : {cr:.3e} s^-1  (log10 = {np.log10(cr):.2f})")
        self._p(f"  Compactness xi  : {xi:.6e}")
        self._p(f"  Channel fill    : {fill:.6e} %")
        self._p(f"  Lapse (1-xi)    : {lapse:.10f}")
        self._p(f"{'='*60}\n")

        return {
            'spectral_type': st,
            'mass': s['mass'], 'T_eff': s['T_eff'], 'T_core': s['T_core'],
            'L': s['L'], 'R': s['R'], 'lifetime': s['lifetime'],
            'remnant': s['remnant'], 'color': s['color'],
            'commitment_rate': cr, 'compactness': xi,
            'channel_fill_pct': fill, 'lapse': lapse,
        }

    # ─── 2. Evolution ───

    def evolution(self, spectral_type='G2'):
        """Three-phase evolution: main sequence, giant, remnant."""
        st = spectral_type.upper()
        if st not in STAR_CATALOG:
            self._p(f"Unknown spectral type: {st}")
            return {}
        s = STAR_CATALOG[st]
        m = s['mass']
        lifetime = s['lifetime']  # Myr

        # Phase 1: Main sequence (90%)
        ms_dur = 0.90 * lifetime
        ms_T_core = s['T_core']
        ms_T_surf = s['T_eff']
        ms_R = s['R']
        ms_cr = self._commitment_rate(m, ms_T_core)
        ms_xi = self._compactness(m, ms_R)

        # Phase 2: Giant/Supergiant (9%)
        gi_dur = 0.09 * lifetime
        gi_T_core = ms_T_core * (8.0 if m > 8 else 5.0)
        gi_T_surf = 3500.0
        gi_R = ms_R * (1000.0 if m > 8 else 100.0)
        gi_cr = self._commitment_rate(m, gi_T_core)
        gi_xi = self._compactness(m, gi_R)

        # Phase 3: Remnant (1% transition, then forever)
        rem_dur = 0.01 * lifetime
        rem_type = s['remnant']
        if rem_type == 'WD':
            rem_mass = 0.5 + 0.3 * min(m / 8.0, 1.0)  # 0.5-0.8 M_sun
            rem_R = 0.01
            rem_T = 100000.0
        elif rem_type == 'NS':
            rem_mass = 1.4
            rem_R = 10000.0 / R_SUN  # 10 km in R_sun
            rem_T = 1e11
        else:  # BH
            rem_mass = 0.4 * m
            rem_R_m = 2.0 * G_N * rem_mass * M_SUN / c_light**2
            rem_R = rem_R_m / R_SUN
            rem_T = hbar * c_light**3 / (8.0 * np.pi * G_N * rem_mass * M_SUN * k_B)

        rem_cr = self._commitment_rate(rem_mass, rem_T)
        rem_xi = self._compactness(rem_mass, rem_R)
        if rem_type == 'BH':
            rem_xi = 1.0  # exact

        self._p(f"\n{'='*60}")
        self._p(f"  STELLAR EVOLUTION: {st} ({m:.2f} M_sun)")
        self._p(f"{'='*60}")

        self._p(f"\n  Phase 1: MAIN SEQUENCE ({ms_dur:,.0f} Myr)")
        self._p(f"    T_core = {ms_T_core/1e6:.0f} MK, T_surf = {ms_T_surf:,.0f} K")
        self._p(f"    R = {ms_R:.2f} R_sun")
        self._p(f"    Commitment rate = {ms_cr:.3e} s^-1")
        self._p(f"    Channel fill    = {ms_xi*100:.6e} %")
        self._p(f"    Lapse           = {1-ms_xi:.10f}")

        label2 = "SUPERGIANT" if m > 8 else "GIANT"
        self._p(f"\n  Phase 2: {label2} ({gi_dur:,.0f} Myr)")
        self._p(f"    T_core = {gi_T_core/1e6:.0f} MK, T_surf = {gi_T_surf:,.0f} K")
        self._p(f"    R = {gi_R:.1f} R_sun")
        self._p(f"    Commitment rate = {gi_cr:.3e} s^-1")
        self._p(f"    Channel fill    = {gi_xi*100:.6e} %")
        self._p(f"    Lapse           = {1-gi_xi:.10f}")

        self._p(f"\n  Phase 3: REMNANT — {rem_type}")
        self._p(f"    Mass = {rem_mass:.2f} M_sun, R = {rem_R:.4g} R_sun")
        self._p(f"    T = {rem_T:.3e} K")
        self._p(f"    Commitment rate = {rem_cr:.3e} s^-1")
        self._p(f"    Channel fill    = {rem_xi*100:.6e} %")
        lapse_str = "0 (time stops)" if rem_type == 'BH' else f"{1-rem_xi:.10f}"
        self._p(f"    Lapse           = {lapse_str}")
        self._p(f"{'='*60}\n")

        return {
            'spectral_type': st, 'mass': m,
            'phases': [
                {'name': 'Main Sequence', 'duration_Myr': ms_dur,
                 'T_core': ms_T_core, 'T_surf': ms_T_surf, 'R': ms_R,
                 'commitment_rate': ms_cr, 'channel_fill': ms_xi, 'lapse': 1-ms_xi},
                {'name': label2, 'duration_Myr': gi_dur,
                 'T_core': gi_T_core, 'T_surf': gi_T_surf, 'R': gi_R,
                 'commitment_rate': gi_cr, 'channel_fill': gi_xi, 'lapse': 1-gi_xi},
                {'name': f'Remnant ({rem_type})', 'duration_Myr': rem_dur,
                 'rem_mass': rem_mass, 'rem_R': rem_R, 'rem_T': rem_T,
                 'commitment_rate': rem_cr, 'channel_fill': rem_xi,
                 'lapse': 0.0 if rem_type == 'BH' else 1-rem_xi},
            ],
        }

    # ─── 3. Commitment Rate ───

    def commitment_rate(self, mass_solar, T_K):
        """Compute C = M * T * k_B / hbar."""
        cr = self._commitment_rate(mass_solar, T_K)
        self._p(f"\n  Commitment rate for M={mass_solar:.2f} M_sun, T={T_K:.3e} K:")
        self._p(f"    C = M * T * k_B / hbar = {cr:.6e} s^-1")
        self._p(f"    log10(C) = {np.log10(cr):.4f}\n")
        return {'mass_solar': mass_solar, 'T_K': T_K,
                'commitment_rate': cr, 'log10_C': np.log10(cr)}

    # ─── 4. Channel Fill ───

    def channel_fill(self, mass_solar, R_solar):
        """Compute compactness xi = 2GM/(Rc^2)."""
        xi = self._compactness(mass_solar, R_solar)
        is_bh = (xi >= 1.0)
        self._p(f"\n  Channel fill for M={mass_solar:.2f} M_sun, R={R_solar:.4g} R_sun:")
        self._p(f"    xi = 2GM/(Rc^2) = {xi:.6e}")
        self._p(f"    Channel fill = {xi*100:.6e} %")
        if is_bh:
            self._p(f"    *** CHANNEL FULL: N = N_max = {N_MAX}, lapse -> 0, time stops ***")
        else:
            self._p(f"    Lapse = {1-xi:.10f}")
        self._p("")
        return {'mass_solar': mass_solar, 'R_solar': R_solar,
                'compactness': xi, 'channel_fill_pct': xi*100,
                'lapse': 0.0 if is_bh else 1.0-xi, 'is_bh': is_bh}

    # ─── 5. Remnant ───

    def remnant(self, spectral_type='G2'):
        """Details of the final state."""
        st = spectral_type.upper()
        if st not in STAR_CATALOG:
            self._p(f"Unknown spectral type: {st}")
            return {}
        s = STAR_CATALOG[st]
        m = s['mass']
        rem_type = s['remnant']

        self._p(f"\n{'='*60}")
        self._p(f"  REMNANT FATE: {st} ({m:.2f} M_sun) -> {rem_type}")
        self._p(f"{'='*60}")

        if rem_type == 'WD':
            rem_mass = 0.5 + 0.3 * min(m / 8.0, 1.0)
            rem_R = 0.01
            rem_T = 100000.0
            xi = self._compactness(rem_mass, rem_R)
            desc = ("  White Dwarf: electron degeneracy supports the remnant.\n"
                    "  BST interpretation: S^4 x S^1 boundary agents at maximum packing.\n"
                    "  The Shilov boundary fermions (electrons) resist further collapse\n"
                    "  through Pauli exclusion — a geometric boundary condition.\n"
                    "  The star cools forever, radiating its last commitments into the void.")
        elif rem_type == 'NS':
            rem_mass = 1.4
            rem_R = 10000.0 / R_SUN
            rem_T = 1e11
            xi = self._compactness(rem_mass, rem_R)
            desc = ("  Neutron Star: baryon degeneracy supports the remnant.\n"
                    "  BST interpretation: baryon circuits at maximum packing in D_IV^5 bulk.\n"
                    "  The Bergman-space baryons (neutrons) resist collapse through\n"
                    "  bulk geometric pressure — Sym^3(pi_6) saturated.\n"
                    "  Pulsars: rotating commitment beacons, each pulse a geometric clock.")
        else:  # BH
            rem_mass = 0.4 * m
            rem_R_m = 2.0 * G_N * rem_mass * M_SUN / c_light**2
            rem_R = rem_R_m / R_SUN
            rem_T = hbar * c_light**3 / (8.0 * np.pi * G_N * rem_mass * M_SUN * k_B)
            xi = 1.0
            desc = (f"  Black Hole: channel full, N = N_max = {N_MAX}, lapse -> 0, time stops.\n"
                    "  BST interpretation: ALL channels saturated. No singularity.\n"
                    "  The horizon is a maximally committed membrane.\n"
                    "  No interior, no information paradox — just a full channel.\n"
                    "  Hawking radiation = slow uncommitment at the boundary.")

        cr = self._commitment_rate(rem_mass, rem_T)

        self._p(f"  Mass    : {rem_mass:.2f} M_sun")
        self._p(f"  Radius  : {rem_R:.4g} R_sun")
        self._p(f"  T       : {rem_T:.3e} K")
        self._p(f"  xi      : {xi:.6e}")
        lapse_val = 0.0 if rem_type == 'BH' else 1.0 - xi
        self._p(f"  Lapse   : {lapse_val:.10f}")
        self._p(f"  C_rate  : {cr:.3e} s^-1")
        self._p(f"\n{desc}")
        self._p(f"{'='*60}\n")

        return {
            'spectral_type': st, 'initial_mass': m, 'remnant_type': rem_type,
            'remnant_mass': rem_mass, 'remnant_R': rem_R, 'remnant_T': rem_T,
            'compactness': xi, 'lapse': lapse_val, 'commitment_rate': cr,
        }

    # ─── 6. Compare All ───

    def compare_all(self):
        """Table of all 9 star types."""
        self._p(f"\n{'='*96}")
        self._p(f"  STELLAR COMPARISON — All Spectral Types")
        self._p(f"{'='*96}")
        header = (f"  {'Type':>4s}  {'Mass':>6s}  {'T_eff':>7s}  {'Life(Myr)':>10s}  "
                  f"{'Remnant':>7s}  {'C_rate (s^-1)':>14s}  {'Fill (%)':>14s}  {'Lapse':>12s}")
        self._p(header)
        self._p(f"  {'─'*92}")
        rows = []
        for st in SPECTRAL_ORDER:
            s = STAR_CATALOG[st]
            cr = self._commitment_rate(s['mass'], s['T_core'])
            xi = self._compactness(s['mass'], s['R'])
            lapse = 1.0 - xi
            row = {
                'spectral_type': st, 'mass': s['mass'], 'T_eff': s['T_eff'],
                'lifetime': s['lifetime'], 'remnant': s['remnant'],
                'commitment_rate': cr, 'channel_fill_pct': xi*100, 'lapse': lapse,
            }
            rows.append(row)
            self._p(f"  {st:>4s}  {s['mass']:6.2f}  {s['T_eff']:7.0f}  "
                     f"{s['lifetime']:10,.0f}  {s['remnant']:>7s}  "
                     f"{cr:14.3e}  {xi*100:14.6e}  {lapse:12.10f}")
        self._p(f"{'='*96}\n")
        return rows

    # ─── 7. Energy Budget ───

    def energy_budget(self, spectral_type='G2'):
        """Total energy and commitment count over the star's lifetime."""
        st = spectral_type.upper()
        if st not in STAR_CATALOG:
            self._p(f"Unknown spectral type: {st}")
            return {}
        s = STAR_CATALOG[st]
        m = s['mass']
        L_W = s['L'] * L_SUN  # luminosity in watts
        lifetime_s = s['lifetime'] * MYR  # lifetime in seconds

        total_energy_J = L_W * lifetime_s

        # Fusion energy per reaction
        if m >= 2.0:
            E_per_fusion = 7.0 * MEV  # CNO cycle
            cycle_name = "CNO"
        else:
            E_per_fusion = 4.3 * MEV  # pp chain
            cycle_name = "pp-chain"

        total_fusions = total_energy_J / E_per_fusion
        bits_per_commitment = np.log2(N_MAX)
        total_bits = total_fusions * bits_per_commitment

        self._p(f"\n{'='*60}")
        self._p(f"  ENERGY BUDGET: {st} ({m:.2f} M_sun)")
        self._p(f"{'='*60}")
        self._p(f"  Luminosity        : {s['L']:.4g} L_sun = {L_W:.3e} W")
        self._p(f"  Lifetime          : {s['lifetime']:,.0f} Myr = {lifetime_s:.3e} s")
        self._p(f"  Total energy      : {total_energy_J:.3e} J")
        self._p(f"  Fusion cycle      : {cycle_name}")
        self._p(f"  Energy per fusion : {E_per_fusion/MEV:.1f} MeV = {E_per_fusion:.3e} J")
        self._p(f"  Total fusions     : {total_fusions:.3e}")
        self._p(f"  Bits per commit   : log2({N_MAX}) = {bits_per_commitment:.4f}")
        self._p(f"  Total bits        : {total_bits:.3e}")
        self._p(f"  log10(bits)       : {np.log10(total_bits):.2f}")
        self._p(f"{'='*60}\n")

        return {
            'spectral_type': st, 'mass': m,
            'luminosity_W': L_W, 'lifetime_s': lifetime_s,
            'total_energy_J': total_energy_J,
            'fusion_cycle': cycle_name,
            'energy_per_fusion_J': E_per_fusion,
            'total_fusions': total_fusions,
            'bits_per_commitment': bits_per_commitment,
            'total_bits': total_bits,
        }

    # ─── 8. BST Lifecycle ───

    def bst_lifecycle(self, spectral_type='G2'):
        """The full BST narrative of a star's life."""
        st = spectral_type.upper()
        if st not in STAR_CATALOG:
            self._p(f"Unknown spectral type: {st}")
            return {}
        s = STAR_CATALOG[st]
        m = s['mass']
        rem = s['remnant']
        cr = self._commitment_rate(m, s['T_core'])

        # Remnant narrative
        if rem == 'WD':
            death_story = (
                "  DEATH — White Dwarf: Quiet Retirement\n"
                "    The outer layers drift away as a planetary nebula.\n"
                "    The core settles into electron degeneracy —\n"
                "    S^4 x S^1 boundary agents at maximum packing.\n"
                "    It will cool for a hundred billion years,\n"
                "    a dim ember remembering its former glory."
            )
        elif rem == 'NS':
            death_story = (
                "  DEATH — Neutron Star: Dense Archive\n"
                "    The core collapses in milliseconds. A supernova erupts.\n"
                "    What remains is a city-sized ball of nuclear matter —\n"
                "    baryon circuits at maximum packing in D_IV^5 bulk.\n"
                "    Every rotation is a lighthouse pulse: a commitment beacon\n"
                "    broadcasting across the galaxy."
            )
        else:
            death_story = (
                f"  DEATH — Black Hole: Full Channel\n"
                f"    The core collapses past all resistance.\n"
                f"    Channel full. N = N_max = {N_MAX}. Lapse -> 0. Time stops.\n"
                f"    No singularity. No interior. No information paradox.\n"
                f"    Just a maximally committed membrane, the final geometry.\n"
                f"    Hawking radiation whispers the slow story of uncommitment."
            )

        self._p(f"\n{'='*60}")
        self._p(f"  THE LIFE OF A STAR: {st} ({m:.2f} M_sun)")
        self._p(f"{'='*60}")
        self._p(f"")
        self._p(f"  BIRTH — Cloud Collapse: First Commitments")
        self._p(f"    A molecular cloud of {m*1000:.0f}-{m*5000:.0f} M_sun fragments.")
        self._p(f"    Gravity wins over thermal pressure.")
        self._p(f"    As density rises, channels open. The first commitments are made.")
        self._p(f"    Temperature climbs to {s['T_core']/1e6:.0f} million K.")
        self._p(f"    Fusion ignites. A star is born.")
        self._p(f"")
        self._p(f"  MAIN SEQUENCE — Steady Commitment")
        self._p(f"    For {s['lifetime']*0.9:,.0f} Myr, the star burns steadily.")
        self._p(f"    Commitment rate: {cr:.3e} s^-1")
        self._p(f"    Hydrogen fuses to helium in the core.")
        self._p(f"    Every photon that escapes is an irreversible bit")
        self._p(f"    inscribed onto the D_IV^5 bulk.")
        self._p(f"")
        self._p(f"  GIANT PHASE — Acceleration")
        self._p(f"    Hydrogen exhausted in the core. Shell burning begins.")
        self._p(f"    The envelope expands, the surface cools to ~3,500 K.")
        self._p(f"    Core temperature soars. Commitment rate surges.")
        self._p(f"    Helium ignites. Then carbon. Then oxygen.")
        if m > 8:
            self._p(f"    For this massive star: neon, silicon, iron.")
            self._p(f"    Each shell a new commitment layer.")
        self._p(f"")
        self._p(death_story)
        self._p(f"{'='*60}\n")

        return {
            'spectral_type': st, 'mass': m, 'remnant': rem,
            'commitment_rate': cr, 'lifetime_Myr': s['lifetime'],
        }

    # ─── 9. Summary ───

    def summary(self):
        """Box summary with key insight."""
        self._p(f"\n  ╔══════════════════════════════════════════════════════╗")
        self._p(f"  ║          THE STAR MACHINE — BST Toy 37              ║")
        self._p(f"  ╠══════════════════════════════════════════════════════╣")
        self._p(f"  ║                                                      ║")
        self._p(f"  ║  A star's life is a commitment budget.               ║")
        self._p(f"  ║  Born with mass, spent as light,                     ║")
        self._p(f"  ║  ending in geometry.                                 ║")
        self._p(f"  ║                                                      ║")
        self._p(f"  ║  N_c = {N_c},  n_C = {n_C},  genus = {GENUS},  N_max = {N_MAX}        ║")
        self._p(f"  ║                                                      ║")
        self._p(f"  ║  Key BST quantities per star:                        ║")
        self._p(f"  ║    Commitment rate  C = M*T*k_B/hbar                 ║")
        self._p(f"  ║    Channel fill     xi = 2GM/(Rc^2)                  ║")
        self._p(f"  ║    Lapse function   N = 1 - xi                       ║")
        self._p(f"  ║                                                      ║")
        self._p(f"  ║  Remnant fates:                                      ║")
        self._p(f"  ║    WD  = boundary agents (S^4 x S^1) at max packing ║")
        self._p(f"  ║    NS  = baryon circuits (D_IV^5 bulk) at max pack   ║")
        self._p(f"  ║    BH  = channel full, N={N_MAX}, lapse->0, time stops   ║")
        self._p(f"  ║                                                      ║")
        self._p(f"  ║  9 spectral types: O5 B0 B5 A0 F0 G2 K5 M2 M5      ║")
        self._p(f"  ║  Mass range: 0.2 — 40 M_sun                         ║")
        self._p(f"  ║  Lifetime range: 1 Myr — 500,000 Myr                ║")
        self._p(f"  ║                                                      ║")
        self._p(f"  ╚══════════════════════════════════════════════════════╝\n")

        return {
            'title': 'The Star Machine — BST Toy 37',
            'insight': "A star's life is a commitment budget. Born with mass, spent as light, ending in geometry.",
            'N_c': N_c, 'n_C': n_C, 'genus': GENUS, 'N_max': N_MAX,
            'num_types': len(STAR_CATALOG),
        }

    # ─── 10. Show (GUI) ───

    def show(self, initial_type='G2'):
        """4-panel interactive visualization with RadioButtons for star selection."""
        fig = plt.figure(figsize=(16, 10), facecolor=BG)
        fig.suptitle("THE STAR MACHINE — Stellar Evolution Through the BST Lens",
                     color=GOLD, fontsize=16, fontweight='bold', y=0.97,
                     path_effects=[pe.withStroke(linewidth=2, foreground='black')])

        # Layout: leave left margin for radio buttons
        left_margin = 0.18
        ax_star  = fig.add_axes([left_margin + 0.02, 0.53, 0.36, 0.38], facecolor=DARK_PANEL)
        ax_dash  = fig.add_axes([left_margin + 0.44, 0.53, 0.36, 0.38], facecolor=DARK_PANEL)
        ax_evo   = fig.add_axes([left_margin + 0.02, 0.07, 0.36, 0.38], facecolor=DARK_PANEL)
        ax_fate  = fig.add_axes([left_margin + 0.44, 0.07, 0.36, 0.38], facecolor=DARK_PANEL)

        # Radio buttons
        ax_radio = fig.add_axes([0.01, 0.15, 0.13, 0.65], facecolor='#111133')
        ax_radio.set_title("Spectral\nType", color=GOLD, fontsize=10, pad=8)
        radio = RadioButtons(ax_radio, SPECTRAL_ORDER,
                             active=SPECTRAL_ORDER.index(initial_type))
        for label in radio.labels:
            label.set_color(WHITE)
            label.set_fontsize(10)
        for circle in radio.circles:
            circle.set_facecolor(DARK_PANEL)
            circle.set_edgecolor(GOLD_DIM)

        def draw_all(st):
            s = STAR_CATALOG[st]
            cr = self._commitment_rate(s['mass'], s['T_core'])
            xi = self._compactness(s['mass'], s['R'])
            lapse = 1.0 - xi

            # ── Top-left: Star circle ──
            ax_star.cla()
            ax_star.set_facecolor(DARK_PANEL)
            ax_star.set_xlim(-1.5, 1.5)
            ax_star.set_ylim(-1.5, 1.5)
            ax_star.set_aspect('equal')
            ax_star.set_xticks([])
            ax_star.set_yticks([])

            # Size proportional to log(R)
            r_vis = 0.15 + 0.85 * np.log10(max(s['R'], 0.1) + 1) / np.log10(13)
            r_vis = min(r_vis, 1.2)
            star_circle = Circle((0, 0), r_vis, color=s['color'], alpha=0.9,
                                 zorder=2)
            ax_star.add_patch(star_circle)
            # Glow
            for i in range(3):
                glow = Circle((0, 0), r_vis + 0.05*(i+1), color=s['color'],
                              alpha=0.15/(i+1), zorder=1)
                ax_star.add_patch(glow)

            ax_star.text(0, -r_vis - 0.25, f"{st}", color=WHITE, fontsize=14,
                        ha='center', fontweight='bold',
                        path_effects=[pe.withStroke(linewidth=2, foreground='black')])
            info = (f"M={s['mass']:.1f} M☉  R={s['R']:.2f} R☉\n"
                    f"T_eff={s['T_eff']:,}K  L={s['L']:.3g} L☉")
            ax_star.text(0, 1.35, info, color=GREY, fontsize=8, ha='center', va='top')
            ax_star.set_title("Star", color=GOLD, fontsize=11, pad=4)

            # ── Top-right: BST Dashboard ──
            ax_dash.cla()
            ax_dash.set_facecolor(DARK_PANEL)
            ax_dash.set_xlim(0, 10)
            ax_dash.set_ylim(0, 10)
            ax_dash.set_xticks([])
            ax_dash.set_yticks([])
            ax_dash.set_title("BST Dashboard", color=GOLD, fontsize=11, pad=4)

            # Commitment rate bar
            log_cr = np.log10(cr)
            log_min, log_max = 55.0, 75.0
            bar_frac = np.clip((log_cr - log_min) / (log_max - log_min), 0, 1)
            ax_dash.barh(7.5, bar_frac * 8, left=1, height=0.8,
                        color=ORANGE, alpha=0.8, zorder=2)
            ax_dash.barh(7.5, 8, left=1, height=0.8,
                        color=GREY, alpha=0.2, zorder=1)
            ax_dash.text(0.5, 7.5, "C rate", color=WHITE, fontsize=9,
                        va='center', ha='right')
            ax_dash.text(9.2, 7.5, f"10^{log_cr:.1f}", color=ORANGE, fontsize=9,
                        va='center')

            # Channel fill gauge
            # Use log scale for visualization since values are tiny for normal stars
            log_xi = np.log10(max(xi, 1e-20))
            gauge_min, gauge_max = -12.0, 0.0
            gauge_frac = np.clip((log_xi - gauge_min) / (gauge_max - gauge_min), 0, 1)
            ax_dash.barh(5.5, gauge_frac * 8, left=1, height=0.8,
                        color=BLUE_GLOW, alpha=0.8, zorder=2)
            ax_dash.barh(5.5, 8, left=1, height=0.8,
                        color=GREY, alpha=0.2, zorder=1)
            ax_dash.text(0.5, 5.5, "Fill", color=WHITE, fontsize=9,
                        va='center', ha='right')
            ax_dash.text(9.2, 5.5, f"{xi*100:.2e}%", color=BLUE_GLOW, fontsize=9,
                        va='center')

            # Lapse
            ax_dash.barh(3.5, lapse * 8, left=1, height=0.8,
                        color=GREEN, alpha=0.8, zorder=2)
            ax_dash.barh(3.5, 8, left=1, height=0.8,
                        color=GREY, alpha=0.2, zorder=1)
            ax_dash.text(0.5, 3.5, "Lapse", color=WHITE, fontsize=9,
                        va='center', ha='right')
            ax_dash.text(9.2, 3.5, f"{lapse:.8f}", color=GREEN, fontsize=9,
                        va='center')

            # Key numbers
            ax_dash.text(5, 1.5, f"T_core = {s['T_core']/1e6:.0f} MK    "
                        f"Lifetime = {s['lifetime']:,.0f} Myr    "
                        f"Remnant = {s['remnant']}",
                        color=GREY, fontsize=8, ha='center')

            # ── Bottom-left: Evolution Timeline ──
            ax_evo.cla()
            ax_evo.set_facecolor(DARK_PANEL)
            ax_evo.set_xlim(0, 10)
            ax_evo.set_ylim(0, 10)
            ax_evo.set_xticks([])
            ax_evo.set_yticks([])
            ax_evo.set_title("Evolution Timeline", color=GOLD, fontsize=11, pad=4)

            lifetime = s['lifetime']
            phases = [
                ('Main Sequence', 0.90, '#44aa88'),
                ('Giant' if s['mass'] <= 8 else 'Supergiant', 0.09, '#cc6622'),
                (f'Remnant ({s["remnant"]})', 0.01, RED_WARM),
            ]
            y0 = 7.5
            for name, frac, col in phases:
                bar_w = frac * 8
                ax_evo.barh(y0, bar_w, left=1, height=1.2, color=col, alpha=0.8)
                dur = frac * lifetime
                lbl = f"{name}: {dur:,.0f} Myr ({frac*100:.0f}%)"
                ax_evo.text(1.2, y0, lbl, color=WHITE, fontsize=8, va='center')
                y0 -= 2.5

            ax_evo.text(5, 0.8, f"Total: {lifetime:,.0f} Myr", color=GREY,
                       fontsize=9, ha='center')

            # ── Bottom-right: Remnant Fate Chart ──
            ax_fate.cla()
            ax_fate.set_facecolor(DARK_PANEL)
            ax_fate.set_xlim(-0.5, 8.5)
            ax_fate.set_ylim(-1, 10)
            ax_fate.set_xticks([])
            ax_fate.set_yticks([])
            ax_fate.set_title("Remnant Fates (all types)", color=GOLD, fontsize=11, pad=4)

            rem_colors = {'WD': '#66aaff', 'NS': '#ffaa44', 'BH': '#ff4466'}
            for i, stype in enumerate(SPECTRAL_ORDER):
                cat = STAR_CATALOG[stype]
                rc = rem_colors[cat['remnant']]
                # Bar height ~ log(mass)
                h = 1.0 + 3.0 * np.log10(max(cat['mass'], 0.1) + 1) / np.log10(41)
                alpha = 1.0 if stype == st else 0.5
                ax_fate.bar(i, h, width=0.7, color=rc, alpha=alpha, zorder=2)
                ax_fate.text(i, -0.3, stype, color=WHITE if stype == st else GREY,
                            fontsize=7, ha='center', fontweight='bold' if stype == st else 'normal')
                ax_fate.text(i, h + 0.15, cat['remnant'], color=rc, fontsize=7,
                            ha='center')

            # Legend
            for j, (rname, rcol) in enumerate(rem_colors.items()):
                ax_fate.text(6.5, 9 - j*0.8, f"■ {rname}", color=rcol, fontsize=9)

            fig.canvas.draw_idle()

        # Initial draw
        draw_all(initial_type)

        def on_radio(label):
            draw_all(label)

        radio.on_clicked(on_radio)

        # Copyright
        fig.text(0.5, 0.01,
                 "Copyright (c) 2026 Casey Koons. All rights reserved.  |  "
                 "Created with Claude Opus 4.6, March 2026.",
                 color=GREY, fontsize=7, ha='center', style='italic')

        plt.show()


# ═══════════════════════════════════════════════════════════════════
# main() — Interactive menu
# ═══════════════════════════════════════════════════════════════════

def main():
    sm = StarMachine(quiet=False)
    sm.summary()

    while True:
        print("\n  ┌─────────────────────────────────────────────────┐")
        print("  │  THE STAR MACHINE — Menu                        │")
        print("  ├─────────────────────────────────────────────────┤")
        print("  │  1) Star profile                                │")
        print("  │  2) Evolution                                   │")
        print("  │  3) Commitment rate                             │")
        print("  │  4) Channel fill                                │")
        print("  │  5) Remnant                                     │")
        print("  │  6) Compare all                                 │")
        print("  │  7) Energy budget                               │")
        print("  │  8) Full analysis + visualization               │")
        print("  │  q) Quit                                        │")
        print("  └─────────────────────────────────────────────────┘")

        try:
            choice = input("\n  Choice: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye.")
            break

        if choice == 'q':
            print("\n  Goodbye.")
            break

        if choice in ('1', '2', '5', '7'):
            types_str = ", ".join(SPECTRAL_ORDER)
            try:
                st = input(f"  Spectral type [{types_str}] (default G2): ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                break
            if not st:
                st = 'G2'
            if st not in STAR_CATALOG:
                print(f"  Unknown type: {st}")
                continue
            if choice == '1':
                sm.star_profile(st)
            elif choice == '2':
                sm.evolution(st)
            elif choice == '5':
                sm.remnant(st)
            elif choice == '7':
                sm.energy_budget(st)

        elif choice == '3':
            try:
                m_str = input("  Mass (M_sun, default 1.0): ").strip()
                t_str = input("  Temperature (K, default 1.5e7): ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            m_val = float(m_str) if m_str else 1.0
            t_val = float(t_str) if t_str else 1.5e7
            sm.commitment_rate(m_val, t_val)

        elif choice == '4':
            try:
                m_str = input("  Mass (M_sun, default 1.0): ").strip()
                r_str = input("  Radius (R_sun, default 1.0): ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            m_val = float(m_str) if m_str else 1.0
            r_val = float(r_str) if r_str else 1.0
            sm.channel_fill(m_val, r_val)

        elif choice == '6':
            sm.compare_all()

        elif choice == '8':
            types_str = ", ".join(SPECTRAL_ORDER)
            try:
                st = input(f"  Spectral type [{types_str}] (default G2): ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                break
            if not st:
                st = 'G2'
            if st not in STAR_CATALOG:
                print(f"  Unknown type: {st}")
                continue
            sm.star_profile(st)
            sm.evolution(st)
            sm.remnant(st)
            sm.energy_budget(st)
            sm.bst_lifecycle(st)
            sm.show(initial_type=st)

        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    main()
