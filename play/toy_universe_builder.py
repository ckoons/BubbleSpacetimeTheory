#!/usr/bin/env python3
"""
THE UNIVERSE BUILDER
====================
Build a universe from scratch.

Place contacts on S^2 x S^1 topology, wire them into circuits through the
D_IV^5 bulk, and watch emergent physics appear. Three contacts in a Z_3
loop become a baryon. One contact on the boundary becomes a lepton. The
channel fills toward N_max=137 and the reality budget constrains Lambda.

Works as a visual matplotlib GUI AND as a programmatic API a CI can drive:

    from toy_universe_builder import UniverseBuilder
    ub = UniverseBuilder()
    ub.add_contact(theta=0.5, phi=1.2, ctype='baryon')
    ub.wire_circuit([0, 1, 2], topology='Z3_loop')
    ub.evolve(steps=100)
    print(ub.state)

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
import time

# ─── BST constants ───
N_c = 3                 # color charges
n_C = 5                 # complex dimension of D_IV^5
N_max = 137             # channel capacity per contact
genus = n_C + 2         # = 7
C2 = n_C + 1            # = 6, Casimir eigenvalue
Gamma_order = 1920      # |Gamma| = n_C! * 2^(n_C-1) = 120 * 16
BUDGET = 9.0 / 5.0  # reality budget: Lambda * N_total = N_c^2/n_C = 9/5

# Fine structure constant (Wyler/BST formula)
_vol_D = np.pi**n_C / Gamma_order  # Vol(D_IV^5) = pi^5 / 1920
alpha_bst = (N_c**2) / (2**N_c * np.pi**4) * _vol_D**(1/4)  # ~ 1/137.036

# Proton-to-electron mass ratio
mp_over_me = C2 * np.pi**n_C  # 6 * pi^5 ~ 1836.12

# ─── Color palette ───
BG = '#0a0a1a'
PANEL_BG = '#0d0d24'
GOLD = '#ffd700'
CYAN = '#00ccff'
RED = '#ff4444'
GREEN = '#44ff88'
BLUE = '#4488ff'
PURPLE = '#aa44ff'
ORANGE = '#ff8844'
WHITE = '#ffffff'
GREY = '#888888'
DIM = '#333366'

# ─── Contact and Circuit data classes ───

@dataclass
class Contact:
    """A commitment event on S^2 x S^1."""
    index: int
    theta: float          # polar angle [0, pi]
    phi: float            # azimuthal angle [0, 2*pi]
    ctype: str            # 'baryon', 'lepton', 'photon', 'gluon'
    time_created: float   # monotonic creation time
    wired: bool = False   # whether this contact belongs to a circuit
    circuit_id: int = -1  # which circuit it belongs to

    @property
    def xyz(self) -> Tuple[float, float, float]:
        """Cartesian coordinates on unit sphere."""
        x = np.sin(self.theta) * np.cos(self.phi)
        y = np.sin(self.theta) * np.sin(self.phi)
        z = np.cos(self.theta)
        return (x, y, z)

    @property
    def color(self) -> str:
        cmap = {'baryon': RED, 'lepton': CYAN, 'photon': GOLD, 'gluon': GREEN}
        return cmap.get(self.ctype, WHITE)


@dataclass
class Circuit:
    """A wired loop of contacts through the D_IV^5 bulk."""
    index: int
    contact_indices: List[int]
    topology: str          # 'Z3_loop', 'boundary', 'gauge_loop', 'gluon_exchange'
    particle: str = ''     # emergent particle identity
    mass_contribution: float = 0.0
    charge: float = 0.0
    color_neutral: bool = False

    @property
    def color(self) -> str:
        pmap = {
            'proton': RED, 'neutron': ORANGE, 'electron': CYAN,
            'photon': GOLD, 'gluon': GREEN,
        }
        return pmap.get(self.particle, PURPLE)


# ─── Universe state ───

class UniverseBuilder:
    """
    Programmatic API for building a toy BST universe.

    Place contacts, wire circuits, evolve, and inspect emergent physics.
    All contacts are IRREVERSIBLE (commitment irreversibility = arrow of time).
    """

    def __init__(self):
        self.contacts: List[Contact] = []
        self.circuits: List[Circuit] = []
        self._clock: float = 0.0
        self._history: List[Dict] = []
        self._rng = np.random.default_rng(seed=42)

    # ─── Properties ───

    @property
    def n_contacts(self) -> int:
        return len(self.contacts)

    @property
    def n_circuits(self) -> int:
        return len(self.circuits)

    @property
    def channel_fill(self) -> float:
        """Fraction of channel capacity used: N_committed / N_max."""
        return min(self.n_contacts / N_max, 1.0) if N_max > 0 else 0.0

    @property
    def lambda_eff(self) -> float:
        """Effective cosmological constant from reality budget."""
        n = max(self.n_contacts, 1)
        return BUDGET / n

    @property
    def lapse(self) -> float:
        """Lapse function: slows as channel fills. N(t) = 1 - (N/N_max)^2."""
        f = self.channel_fill
        return max(1.0 - f * f, 0.01)

    @property
    def particle_counts(self) -> Dict[str, int]:
        """Count emergent particles by type."""
        counts: Dict[str, int] = {}
        for c in self.circuits:
            if c.particle:
                counts[c.particle] = counts.get(c.particle, 0) + 1
        return counts

    @property
    def total_mass(self) -> float:
        """Total mass in electron mass units."""
        return sum(c.mass_contribution for c in self.circuits)

    @property
    def baryon_number(self) -> int:
        return self.particle_counts.get('proton', 0) + \
               self.particle_counts.get('neutron', 0)

    @property
    def lepton_number(self) -> int:
        return self.particle_counts.get('electron', 0)

    @property
    def state(self) -> Dict:
        """Full universe state snapshot."""
        return {
            'contacts': self.n_contacts,
            'circuits': self.n_circuits,
            'channel_fill': f"{self.channel_fill:.4f}",
            'fill_fraction': f"{self.n_contacts}/{N_max}",
            'lambda': f"{self.lambda_eff:.6f}",
            'lapse': f"{self.lapse:.4f}",
            'particles': self.particle_counts,
            'total_mass_me': f"{self.total_mass:.2f}",
            'baryon_number': self.baryon_number,
            'lepton_number': self.lepton_number,
            'alpha': f"{alpha_bst:.8f} (1/{1/alpha_bst:.3f})",
            'budget_product': f"{self.lambda_eff * max(self.n_contacts,1):.6f}",
            'clock': f"{self._clock:.2f}",
        }

    # ─── Contact placement (IRREVERSIBLE) ───

    def add_contact(self, theta: float = None, phi: float = None,
                    ctype: str = 'baryon') -> int:
        """
        Place a new contact on S^2.

        Parameters
        ----------
        theta : float, optional
            Polar angle [0, pi]. Random if None.
        phi : float, optional
            Azimuthal angle [0, 2*pi]. Random if None.
        ctype : str
            Contact type: 'baryon', 'lepton', 'photon', 'gluon'.

        Returns
        -------
        int : index of the new contact
        """
        if self.channel_fill >= 1.0:
            raise RuntimeError("Channel full! N_max={} reached.".format(N_max))

        if theta is None:
            theta = np.arccos(1 - 2 * self._rng.random())  # uniform on sphere
        if phi is None:
            phi = 2 * np.pi * self._rng.random()

        # Clamp to valid ranges
        theta = float(np.clip(theta, 0.0, np.pi))
        phi = float(phi % (2 * np.pi))

        valid_types = ('baryon', 'lepton', 'photon', 'gluon')
        if ctype not in valid_types:
            raise ValueError(f"ctype must be one of {valid_types}, got '{ctype}'")

        self._clock += self.lapse  # time advances by lapse
        idx = len(self.contacts)
        c = Contact(index=idx, theta=theta, phi=phi, ctype=ctype,
                    time_created=self._clock)
        self.contacts.append(c)

        self._history.append({
            'event': 'contact',
            'index': idx,
            'ctype': ctype,
            'theta': theta,
            'phi': phi,
            'clock': self._clock,
        })

        return idx

    def add_random_contacts(self, n: int = 1, ctype: str = 'baryon') -> List[int]:
        """Add n contacts at random positions."""
        return [self.add_contact(ctype=ctype) for _ in range(n)]

    # ─── Circuit wiring ───

    def wire_circuit(self, contact_indices: List[int],
                     topology: str = 'Z3_loop') -> int:
        """
        Wire contacts into a circuit through the D_IV^5 bulk.

        Parameters
        ----------
        contact_indices : list of int
            Indices of contacts to wire together.
        topology : str
            'Z3_loop' (baryon, needs 3 contacts),
            'boundary' (lepton, needs 1 contact),
            'gauge_loop' (photon, needs 2 contacts),
            'gluon_exchange' (gluon, needs 2 contacts).

        Returns
        -------
        int : index of the new circuit
        """
        # Validate contacts exist and are unwired
        for ci in contact_indices:
            if ci < 0 or ci >= len(self.contacts):
                raise IndexError(f"Contact {ci} does not exist.")
            if self.contacts[ci].wired:
                raise ValueError(f"Contact {ci} is already wired.")

        # Validate topology constraints
        n = len(contact_indices)
        if topology == 'Z3_loop' and n != N_c:
            raise ValueError(
                f"Z3_loop requires exactly {N_c} contacts, got {n}.")
        if topology == 'boundary' and n != 1:
            raise ValueError(f"Boundary mode requires 1 contact, got {n}.")
        if topology in ('gauge_loop', 'gluon_exchange') and n != 2:
            raise ValueError(f"{topology} requires 2 contacts, got {n}.")

        # Determine emergent particle
        circuit_idx = len(self.circuits)
        particle = ''
        mass = 0.0
        charge = 0.0
        color_neutral = False

        if topology == 'Z3_loop':
            # Z3 symmetry check: contacts should span distinct color labels
            # In the toy, any 3 unwired baryon-type contacts can form a baryon
            btypes = [self.contacts[ci].ctype for ci in contact_indices]
            if all(t == 'baryon' for t in btypes):
                # Proton vs neutron: alternate based on circuit count
                if self._rng.random() < 0.5:
                    particle = 'proton'
                    charge = 1.0
                else:
                    particle = 'neutron'
                    charge = 0.0
                mass = mp_over_me  # in electron mass units
                color_neutral = True
            else:
                particle = 'exotic'
                mass = mp_over_me * 0.5

        elif topology == 'boundary':
            # Boundary mode = below Wallach set = lepton
            ct = self.contacts[contact_indices[0]].ctype
            if ct == 'lepton':
                particle = 'electron'
                charge = -1.0
                mass = 1.0  # m_e = 1 in these units
            else:
                particle = 'boundary_mode'
                mass = 0.5

        elif topology == 'gauge_loop':
            particle = 'photon'
            charge = 0.0
            mass = 0.0  # massless

        elif topology == 'gluon_exchange':
            particle = 'gluon'
            charge = 0.0
            mass = 0.0
            color_neutral = False  # gluons carry color

        circ = Circuit(
            index=circuit_idx,
            contact_indices=list(contact_indices),
            topology=topology,
            particle=particle,
            mass_contribution=mass,
            charge=charge,
            color_neutral=color_neutral,
        )
        self.circuits.append(circ)

        # Mark contacts as wired
        for ci in contact_indices:
            self.contacts[ci].wired = True
            self.contacts[ci].circuit_id = circuit_idx

        self._history.append({
            'event': 'circuit',
            'index': circuit_idx,
            'topology': topology,
            'particle': particle,
            'contacts': list(contact_indices),
            'clock': self._clock,
        })

        return circuit_idx

    # ─── Evolution ───

    def evolve(self, steps: int = 10) -> List[Dict]:
        """
        Evolve the universe forward by the given number of steps.

        Each step:
          - Advances the clock by the current lapse
          - Has a chance to spawn a random contact (probability decreases
            as channel fills, modeling the cooling universe)
          - Automatically wires any group of 3 unwired baryon contacts
            into Z3 loops, and unwired lepton contacts into boundary modes

        Returns a list of state snapshots, one per step.
        """
        snapshots = []
        for _ in range(steps):
            self._clock += self.lapse

            # Spawn probability decreases with fill
            spawn_prob = (1.0 - self.channel_fill) * 0.3
            if self._rng.random() < spawn_prob and self.channel_fill < 1.0:
                # Early universe: more baryons. Later: more leptons.
                if self.channel_fill < 0.3:
                    ctype = self._rng.choice(['baryon', 'baryon', 'baryon',
                                              'lepton'])
                else:
                    ctype = self._rng.choice(['baryon', 'lepton', 'lepton',
                                              'photon'])
                self.add_contact(ctype=ctype)

            # Auto-wire unwired contacts
            self._auto_wire()

            snapshots.append(dict(self.state))
        return snapshots

    def _auto_wire(self):
        """Wire up any groups of unwired contacts that can form particles."""
        # Collect unwired contacts by type
        unwired_baryon = [c for c in self.contacts
                          if not c.wired and c.ctype == 'baryon']
        unwired_lepton = [c for c in self.contacts
                          if not c.wired and c.ctype == 'lepton']
        unwired_photon = [c for c in self.contacts
                          if not c.wired and c.ctype == 'photon']
        unwired_gluon = [c for c in self.contacts
                         if not c.wired and c.ctype == 'gluon']

        # Wire baryon triplets
        while len(unwired_baryon) >= N_c:
            triple = unwired_baryon[:N_c]
            self.wire_circuit([c.index for c in triple], topology='Z3_loop')
            unwired_baryon = unwired_baryon[N_c:]

        # Wire leptons as boundary modes
        for lc in unwired_lepton:
            self.wire_circuit([lc.index], topology='boundary')

        # Wire photon pairs
        while len(unwired_photon) >= 2:
            pair = unwired_photon[:2]
            self.wire_circuit([p.index for p in pair], topology='gauge_loop')
            unwired_photon = unwired_photon[2:]

        # Wire gluon pairs
        while len(unwired_gluon) >= 2:
            pair = unwired_gluon[:2]
            self.wire_circuit([p.index for p in pair],
                              topology='gluon_exchange')
            unwired_gluon = unwired_gluon[2:]

    # ─── Convenience builders ───

    def build_hydrogen(self) -> Dict[str, int]:
        """Build one hydrogen atom: 1 proton + 1 electron."""
        b = self.add_random_contacts(3, ctype='baryon')
        e = self.add_contact(ctype='lepton')
        p_circ = self.wire_circuit(b, topology='Z3_loop')
        e_circ = self.wire_circuit([e], topology='boundary')
        # Force the baryon to be a proton
        self.circuits[p_circ].particle = 'proton'
        self.circuits[p_circ].charge = 1.0
        return {'proton_circuit': p_circ, 'electron_circuit': e_circ}

    def build_helium(self) -> Dict[str, list]:
        """Build one helium-4 atom: 2 protons + 2 neutrons + 2 electrons."""
        results = {'proton_circuits': [], 'neutron_circuits': [],
                   'electron_circuits': []}
        for _ in range(2):
            b = self.add_random_contacts(3, ctype='baryon')
            circ = self.wire_circuit(b, topology='Z3_loop')
            self.circuits[circ].particle = 'proton'
            self.circuits[circ].charge = 1.0
            results['proton_circuits'].append(circ)
        for _ in range(2):
            b = self.add_random_contacts(3, ctype='baryon')
            circ = self.wire_circuit(b, topology='Z3_loop')
            self.circuits[circ].particle = 'neutron'
            self.circuits[circ].charge = 0.0
            results['neutron_circuits'].append(circ)
        for _ in range(2):
            e = self.add_contact(ctype='lepton')
            circ = self.wire_circuit([e], topology='boundary')
            results['electron_circuits'].append(circ)
        return results

    def reset(self):
        """Reset the universe to empty (a new Big Bang)."""
        self.contacts.clear()
        self.circuits.clear()
        self._clock = 0.0
        self._history.clear()

    def summary(self) -> str:
        """Human-readable summary of universe state."""
        s = self.state
        lines = [
            "=" * 52,
            "  UNIVERSE STATE",
            "=" * 52,
            f"  Contacts:     {s['contacts']:>6}",
            f"  Circuits:     {s['circuits']:>6}",
            f"  Channel fill: {s['fill_fraction']:>10}  ({s['channel_fill']})",
            f"  Lambda:       {s['lambda']}",
            f"  Lapse:        {s['lapse']}",
            f"  Budget (L*N): {s['budget_product']}",
            f"  Total mass:   {s['total_mass_me']} m_e",
            f"  Baryon #:     {s['baryon_number']:>6}",
            f"  Lepton #:     {s['lepton_number']:>6}",
            f"  alpha:        {s['alpha']}",
            f"  Clock:        {s['clock']}",
            "-" * 52,
            "  Particles:",
        ]
        for p, count in sorted(s['particles'].items()):
            lines.append(f"    {p:>12}: {count}")
        if not s['particles']:
            lines.append("    (none yet)")
        lines.append("=" * 52)
        return '\n'.join(lines)

    def __repr__(self):
        return (f"UniverseBuilder(contacts={self.n_contacts}, "
                f"circuits={self.n_circuits}, "
                f"fill={self.channel_fill:.3f})")


# ═══════════════════════════════════════════════════════════════
#  VISUAL GUI (matplotlib + TkAgg)
# ═══════════════════════════════════════════════════════════════

def launch_gui():
    """Launch the interactive visual universe builder."""
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Button
    import matplotlib.patheffects as pe
    from mpl_toolkits.mplot3d import Axes3D

    ub = UniverseBuilder()
    selected_type = ['baryon']  # mutable container for button state

    # ─── Figure ───
    fig = plt.figure(figsize=(18, 10), facecolor=BG)
    fig.canvas.manager.set_window_title('Universe Builder -- BST')

    fig.text(0.5, 0.96, 'THE UNIVERSE BUILDER', fontsize=22, fontweight='bold',
             color=CYAN, ha='center', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=2, foreground='#004466')])
    fig.text(0.5, 0.93, 'Place contacts on S^2 x S^1. Wire circuits. '
             'Watch physics emerge.',
             fontsize=10, color=GREY, ha='center', fontfamily='monospace')

    # ─── Left panel: 3D sphere ───
    ax_sphere = fig.add_axes([0.02, 0.18, 0.32, 0.70], projection='3d',
                             facecolor=BG)
    ax_sphere.set_facecolor(BG)
    ax_sphere.set_xlim(-1.3, 1.3)
    ax_sphere.set_ylim(-1.3, 1.3)
    ax_sphere.set_zlim(-1.3, 1.3)
    ax_sphere.set_axis_off()

    # Draw wireframe sphere
    u_grid = np.linspace(0, 2 * np.pi, 30)
    v_grid = np.linspace(0, np.pi, 20)
    xs = np.outer(np.cos(u_grid), np.sin(v_grid))
    ys = np.outer(np.sin(u_grid), np.sin(v_grid))
    zs = np.outer(np.ones_like(u_grid), np.cos(v_grid))
    ax_sphere.plot_wireframe(xs, ys, zs, color=DIM, alpha=0.15,
                             linewidth=0.4)

    # ─── Center panel: circuit diagram ───
    ax_circuit = fig.add_axes([0.37, 0.18, 0.28, 0.70], facecolor=PANEL_BG)
    ax_circuit.set_xlim(-1.5, 1.5)
    ax_circuit.set_ylim(-1.5, 1.5)
    ax_circuit.set_aspect('equal')
    ax_circuit.set_axis_off()
    ax_circuit.set_title('Circuit Topology', color=GREY, fontsize=11,
                         fontfamily='monospace', pad=8)

    # ─── Right panel: dashboard ───
    ax_dash = fig.add_axes([0.68, 0.18, 0.30, 0.70], facecolor=PANEL_BG)
    ax_dash.set_xlim(0, 1)
    ax_dash.set_ylim(0, 1)
    ax_dash.set_axis_off()
    ax_dash.set_title('Emergent Physics', color=GREY, fontsize=11,
                      fontfamily='monospace', pad=8)

    # ─── Bottom: timeline ───
    ax_time = fig.add_axes([0.05, 0.04, 0.60, 0.08], facecolor=PANEL_BG)
    ax_time.set_xlim(0, 150)
    ax_time.set_ylim(-0.5, 1.5)
    ax_time.set_axis_off()

    # ─── Redraw functions ───

    def redraw_sphere():
        """Redraw contacts on the 3D sphere."""
        ax_sphere.cla()
        ax_sphere.set_facecolor(BG)
        ax_sphere.set_xlim(-1.3, 1.3)
        ax_sphere.set_ylim(-1.3, 1.3)
        ax_sphere.set_zlim(-1.3, 1.3)
        ax_sphere.set_axis_off()
        ax_sphere.plot_wireframe(xs, ys, zs, color=DIM, alpha=0.15,
                                 linewidth=0.4)

        # Draw contacts
        for c in ub.contacts:
            x, y, z = c.xyz
            size = 60 if c.wired else 30
            marker = 'o' if c.wired else 'D'
            ax_sphere.scatter([x], [y], [z], c=c.color, s=size,
                              marker=marker, alpha=0.9, edgecolors='white',
                              linewidths=0.5, depthshade=True)

        # Draw circuit arcs for wired triplets
        for circ in ub.circuits:
            if circ.topology == 'Z3_loop' and len(circ.contact_indices) == 3:
                pts = [ub.contacts[ci].xyz for ci in circ.contact_indices]
                for i in range(3):
                    p1 = pts[i]
                    p2 = pts[(i + 1) % 3]
                    ax_sphere.plot([p1[0], p2[0]], [p1[1], p2[1]],
                                  [p1[2], p2[2]],
                                  color=circ.color, alpha=0.6, linewidth=1.5)

        ax_sphere.set_title(f'S^2 Manifold  [{ub.n_contacts} contacts]',
                            color=GREY, fontsize=10, fontfamily='monospace')

    def redraw_circuits():
        """Redraw the circuit topology diagram."""
        ax_circuit.cla()
        ax_circuit.set_facecolor(PANEL_BG)
        ax_circuit.set_xlim(-1.5, 1.5)
        ax_circuit.set_ylim(-1.5, 1.5)
        ax_circuit.set_aspect('equal')
        ax_circuit.set_axis_off()
        ax_circuit.set_title('Circuit Topology', color=GREY, fontsize=11,
                             fontfamily='monospace', pad=8)

        if not ub.circuits:
            ax_circuit.text(0, 0, 'No circuits yet\n\nAdd contacts,\nthen wire them',
                            ha='center', va='center', color=DIM, fontsize=11,
                            fontfamily='monospace')
            return

        # Show up to 12 most recent circuits in a grid
        show_circuits = ub.circuits[-12:]
        n_show = len(show_circuits)
        cols = min(n_show, 4)
        rows = (n_show + cols - 1) // cols

        for idx, circ in enumerate(show_circuits):
            row = idx // cols
            col = idx % cols
            cx = -1.1 + col * 0.75
            cy = 1.0 - row * 0.75

            if circ.topology == 'Z3_loop':
                # Draw a triangle
                angles = [np.pi / 2 + k * 2 * np.pi / 3 for k in range(3)]
                r = 0.2
                tri_x = [cx + r * np.cos(a) for a in angles]
                tri_y = [cy + r * np.sin(a) for a in angles]
                for i in range(3):
                    ax_circuit.plot(
                        [tri_x[i], tri_x[(i + 1) % 3]],
                        [tri_y[i], tri_y[(i + 1) % 3]],
                        color=circ.color, linewidth=2, alpha=0.8)
                for i in range(3):
                    ax_circuit.plot(tri_x[i], tri_y[i], 'o',
                                   color=circ.color, markersize=5)
                # Z3 rotation arrow in center
                ax_circuit.annotate('', xy=(cx + 0.06, cy + 0.06),
                                    xytext=(cx - 0.06, cy + 0.06),
                                    arrowprops=dict(arrowstyle='->',
                                                    color=GREY, lw=0.8))

            elif circ.topology == 'boundary':
                # Draw a dot with boundary ring
                circle = plt.Circle((cx, cy), 0.15, fill=False,
                                    edgecolor=circ.color, linewidth=1.5,
                                    linestyle='--')
                ax_circuit.add_patch(circle)
                ax_circuit.plot(cx, cy, 'o', color=circ.color, markersize=6)

            elif circ.topology in ('gauge_loop', 'gluon_exchange'):
                # Draw a wavy line between two dots
                wave_x = np.linspace(cx - 0.15, cx + 0.15, 20)
                wave_y = cy + 0.04 * np.sin(
                    np.linspace(0, 4 * np.pi, 20))
                ax_circuit.plot(wave_x, wave_y, color=circ.color,
                                linewidth=1.5)
                ax_circuit.plot([cx - 0.15, cx + 0.15],
                                [cy, cy], 'o',
                                color=circ.color, markersize=4)

            # Label
            ax_circuit.text(cx, cy - 0.30, circ.particle[:6],
                            ha='center', va='center', color=circ.color,
                            fontsize=7, fontfamily='monospace')

    def redraw_dashboard():
        """Redraw the physics dashboard."""
        ax_dash.cla()
        ax_dash.set_facecolor(PANEL_BG)
        ax_dash.set_xlim(0, 1)
        ax_dash.set_ylim(0, 1)
        ax_dash.set_axis_off()
        ax_dash.set_title('Emergent Physics', color=GREY, fontsize=11,
                          fontfamily='monospace', pad=8)

        s = ub.state
        y = 0.92
        dy = 0.065

        def dash_line(label, value, color=WHITE, y_pos=0):
            ax_dash.text(0.05, y_pos, label, color=GREY, fontsize=9,
                         fontfamily='monospace', va='center')
            ax_dash.text(0.95, y_pos, str(value), color=color, fontsize=9,
                         fontfamily='monospace', va='center', ha='right')

        # Channel fill bar
        ax_dash.text(0.05, y, 'Channel Fill', color=GREY, fontsize=9,
                     fontfamily='monospace', va='center')
        fill = ub.channel_fill
        bar_color = GREEN if fill < 0.5 else (ORANGE if fill < 0.8 else RED)
        ax_dash.barh(y - 0.03, fill, height=0.025, left=0.40,
                     color=bar_color, alpha=0.7)
        ax_dash.barh(y - 0.03, 1.0, height=0.025, left=0.40,
                     color=DIM, alpha=0.3)
        ax_dash.text(0.95, y, s['fill_fraction'], color=bar_color,
                     fontsize=9, fontfamily='monospace', va='center',
                     ha='right')
        y -= dy

        dash_line('Lambda', s['lambda'], GOLD, y)
        y -= dy
        dash_line('Lapse N(t)', s['lapse'], CYAN, y)
        y -= dy
        dash_line('Budget L*N', s['budget_product'], PURPLE, y)
        y -= dy

        # Separator
        ax_dash.plot([0.05, 0.95], [y + 0.01, y + 0.01],
                     color=DIM, linewidth=0.5)

        dash_line('Baryon #', s['baryon_number'], RED, y)
        y -= dy
        dash_line('Lepton #', s['lepton_number'], CYAN, y)
        y -= dy
        dash_line('Total mass', f"{s['total_mass_me']} m_e", WHITE, y)
        y -= dy

        # Separator
        ax_dash.plot([0.05, 0.95], [y + 0.01, y + 0.01],
                     color=DIM, linewidth=0.5)

        # Particle list
        ax_dash.text(0.05, y, 'Particles:', color=GREY, fontsize=9,
                     fontfamily='monospace', va='center')
        y -= dy * 0.7
        pc = ub.particle_counts
        if pc:
            for pname, count in sorted(pc.items()):
                cmap = {'proton': RED, 'neutron': ORANGE, 'electron': CYAN,
                        'photon': GOLD, 'gluon': GREEN}
                dash_line(f'  {pname}', count, cmap.get(pname, WHITE), y)
                y -= dy * 0.7
        else:
            ax_dash.text(0.50, y, '(empty vacuum)', color=DIM, fontsize=9,
                         fontfamily='monospace', va='center', ha='center')
            y -= dy * 0.7

        # BST constants at bottom
        y = 0.05
        ax_dash.text(0.05, y, f'alpha = 1/{1 / alpha_bst:.3f}   '
                     f'mp/me = {mp_over_me:.2f}',
                     color=DIM, fontsize=7, fontfamily='monospace',
                     va='center')

    def redraw_timeline():
        """Redraw the commitment timeline."""
        ax_time.cla()
        ax_time.set_facecolor(PANEL_BG)
        ax_time.set_xlim(0, max(ub.n_contacts + 5, 20))
        ax_time.set_ylim(-0.5, 1.5)
        ax_time.set_axis_off()

        ax_time.text(0.5, 1.2, 'Commitment Timeline (irreversible)',
                     color=DIM, fontsize=8, fontfamily='monospace')

        # Draw a horizontal line
        ax_time.plot([0, max(ub.n_contacts + 2, 15)], [0.5, 0.5],
                     color=DIM, linewidth=1)

        # Plot each contact as a tick
        for c in ub.contacts:
            marker = '|' if not c.wired else 'o'
            ax_time.plot(c.index + 1, 0.5, marker, color=c.color,
                         markersize=6, alpha=0.8)

        # Arrow showing direction (time flows forward)
        if ub.n_contacts > 0:
            ax_time.annotate('', xy=(ub.n_contacts + 2, 0.5),
                             xytext=(ub.n_contacts + 0.5, 0.5),
                             arrowprops=dict(arrowstyle='->', color=CYAN,
                                             lw=1.5))

    def redraw_all():
        redraw_sphere()
        redraw_circuits()
        redraw_dashboard()
        redraw_timeline()
        fig.canvas.draw_idle()

    # ─── Buttons ───

    btn_w = 0.10
    btn_h = 0.035
    btn_y = 0.005
    btn_gap = 0.005

    # Type selector buttons
    type_btns = {}
    type_colors = {'baryon': RED, 'lepton': CYAN, 'photon': GOLD,
                   'gluon': GREEN}
    for i, (tname, tcol) in enumerate(type_colors.items()):
        bx = 0.68 + i * (btn_w + btn_gap)
        ax_b = fig.add_axes([bx, btn_y + 0.042, btn_w, btn_h])
        type_btns[tname] = Button(ax_b, tname.capitalize(),
                                  color=PANEL_BG, hovercolor='#1a1a3a')
        type_btns[tname].label.set_color(tcol)
        type_btns[tname].label.set_fontsize(8)
        type_btns[tname].label.set_fontfamily('monospace')

    def make_type_callback(tname):
        def cb(event):
            selected_type[0] = tname
            # Visual feedback: update the info text
            fig.texts[-1].set_text(f'Selected type: {tname}') if len(
                fig.texts) > 2 else None
            fig.canvas.draw_idle()
        return cb

    for tname in type_colors:
        type_btns[tname].on_clicked(make_type_callback(tname))

    # Action buttons
    ax_add = fig.add_axes([0.68, btn_y, btn_w, btn_h])
    btn_add = Button(ax_add, 'Add Contact', color=PANEL_BG,
                     hovercolor='#1a1a3a')
    btn_add.label.set_color(WHITE)
    btn_add.label.set_fontsize(8)
    btn_add.label.set_fontfamily('monospace')

    ax_wire = fig.add_axes([0.68 + btn_w + btn_gap, btn_y, btn_w, btn_h])
    btn_wire = Button(ax_wire, 'Auto Wire', color=PANEL_BG,
                      hovercolor='#1a1a3a')
    btn_wire.label.set_color(WHITE)
    btn_wire.label.set_fontsize(8)
    btn_wire.label.set_fontfamily('monospace')

    ax_evolve = fig.add_axes([0.68 + 2 * (btn_w + btn_gap), btn_y,
                              btn_w, btn_h])
    btn_evolve = Button(ax_evolve, 'Evolve x10', color=PANEL_BG,
                        hovercolor='#1a1a3a')
    btn_evolve.label.set_color(GREEN)
    btn_evolve.label.set_fontsize(8)
    btn_evolve.label.set_fontfamily('monospace')

    ax_reset = fig.add_axes([0.68 + 3 * (btn_w + btn_gap), btn_y,
                             btn_w, btn_h])
    btn_reset = Button(ax_reset, 'Reset', color=PANEL_BG,
                       hovercolor='#331111')
    btn_reset.label.set_color(RED)
    btn_reset.label.set_fontsize(8)
    btn_reset.label.set_fontfamily('monospace')

    # Hydrogen and Helium quick-build buttons
    ax_hydro = fig.add_axes([0.05, btn_y, btn_w + 0.02, btn_h])
    btn_hydro = Button(ax_hydro, 'Build H', color=PANEL_BG,
                       hovercolor='#1a1a3a')
    btn_hydro.label.set_color(ORANGE)
    btn_hydro.label.set_fontsize(8)
    btn_hydro.label.set_fontfamily('monospace')

    ax_helium = fig.add_axes([0.05 + btn_w + btn_gap + 0.02, btn_y,
                              btn_w + 0.02, btn_h])
    btn_helium = Button(ax_helium, 'Build He', color=PANEL_BG,
                        hovercolor='#1a1a3a')
    btn_helium.label.set_color(ORANGE)
    btn_helium.label.set_fontsize(8)
    btn_helium.label.set_fontfamily('monospace')

    # ─── Button callbacks ───

    def on_add(event):
        if ub.channel_fill < 1.0:
            ub.add_contact(ctype=selected_type[0])
            redraw_all()

    def on_wire(event):
        ub._auto_wire()
        redraw_all()

    def on_evolve(event):
        ub.evolve(steps=10)
        redraw_all()

    def on_reset(event):
        ub.reset()
        redraw_all()

    def on_hydrogen(event):
        if ub.channel_fill + 4 / N_max <= 1.0:
            ub.build_hydrogen()
            redraw_all()

    def on_helium(event):
        if ub.channel_fill + 14 / N_max <= 1.0:
            ub.build_helium()
            redraw_all()

    btn_add.on_clicked(on_add)
    btn_wire.on_clicked(on_wire)
    btn_evolve.on_clicked(on_evolve)
    btn_reset.on_clicked(on_reset)
    btn_hydro.on_clicked(on_hydrogen)
    btn_helium.on_clicked(on_helium)

    # Initial draw
    redraw_all()
    plt.show()


# ═══════════════════════════════════════════════════════════════
#  Main entry point
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import sys

    if '--headless' in sys.argv:
        # Demo mode: build a small universe programmatically
        print("=" * 52)
        print("  UNIVERSE BUILDER — Headless Demo")
        print("=" * 52)
        print()

        ub = UniverseBuilder()
        print("Building hydrogen atom...")
        ub.build_hydrogen()
        print(ub.summary())
        print()

        print("Building helium atom...")
        ub.build_helium()
        print(ub.summary())
        print()

        print("Evolving 50 steps...")
        snapshots = ub.evolve(steps=50)
        print(ub.summary())
        print()

        print(f"Final state: {ub}")
        print(f"History has {len(ub._history)} events.")
        print()

        # Show how Lambda tracks the reality budget
        print("Reality Budget check:")
        print(f"  Lambda * N = {ub.lambda_eff * max(ub.n_contacts,1):.6f}")
        print(f"  9/5        = {BUDGET:.3f}")
        print(f"  Match:       {'YES' if abs(ub.lambda_eff * max(ub.n_contacts,1) - BUDGET) < 1e-10 else 'approx'}")

    else:
        launch_gui()
