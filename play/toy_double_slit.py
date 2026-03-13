#!/usr/bin/env python3
"""
THE DOUBLE SLIT — MEASUREMENT AS COMMITMENT
=============================================
Toy 39: The measurement problem dissolves in BST.

Superposition = uncommitted capacity (not "both paths").
Measurement = irreversible commitment of a correlation.
"Collapse" = the moment a correlation is written to the substrate.

A correlation that dissolves before commitment to definite state
just isn't there at all.

    from toy_double_slit import DoubleSlit
    ds = DoubleSlit()
    ds.setup()
    ds.interference_pattern()
    ds.which_path(coupling=0.5)
    ds.commitment_events(n_photons=50)
    ds.wheeler_delayed_choice()
    ds.quantum_eraser()
    ds.decoherence_timeline()
    ds.summary()
    ds.show()

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# ─── BST Constants ───
N_max = 137                          # channel capacity
BITS_PER_EVENT = np.log2(N_max)      # 7.098 bits per commitment
n_C = 5                              # complex dimension of D_IV^5
N_c = 3                              # color charges
genus = n_C + 2                      # = 7
alpha = 1.0 / N_max                  # fine structure constant (BST)

# ─── Visual constants ───
BG = '#0a0a1a'
DARK_PANEL = '#0d0d24'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
CYAN = '#00ddff'
PURPLE = '#9966ff'
GREEN = '#44ff88'
ORANGE = '#ff8800'
RED = '#ff4444'
WHITE = '#ffffff'
GREY = '#888888'
DGREY = '#444444'
DEEP_BLUE = '#2266ff'
LIGHT_BLUE = '#5599ff'
COMMIT_GOLD = '#ffcc44'


# ═══════════════════════════════════════════════════════════════════
#  DOUBLE SLIT MODEL
# ═══════════════════════════════════════════════════════════════════

class DoubleSlit:
    """
    BST double-slit experiment: measurement = commitment of correlation.

    Superposition is uncommitted capacity. Measurement commits a
    correlation between two physical degrees of freedom. Every variant
    (which-path, delayed choice, quantum eraser) follows from one
    principle: a correlation that dissolves before commitment is not
    a fact.

    Parameters
    ----------
    quiet : bool
        If True, suppress print output. Default False.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.params = None
        self._rng = np.random.default_rng(42)

    def _print(self, msg):
        if not self.quiet:
            print(msg)

    # ─── 1. Setup ───

    def setup(self, slit_sep=0.5e-3, slit_width=0.1e-3,
              wavelength=500e-9, screen_dist=1.0):
        """
        Configure experiment geometry.

        Parameters
        ----------
        slit_sep : float
            Distance between slit centres (metres). Default 0.5 mm.
        slit_width : float
            Width of each slit (metres). Default 0.1 mm.
        wavelength : float
            Photon wavelength (metres). Default 500 nm (green).
        screen_dist : float
            Slit-to-screen distance (metres). Default 1.0 m.

        Returns
        -------
        dict
            All parameters plus derived fringe spacing.
        """
        fringe_spacing = wavelength * screen_dist / slit_sep
        self.params = {
            'slit_sep': slit_sep,
            'slit_width': slit_width,
            'wavelength': wavelength,
            'screen_dist': screen_dist,
            'fringe_spacing': fringe_spacing,
            'N_max': N_max,
            'bits_per_event': BITS_PER_EVENT,
        }
        self._print(f"  Double slit configured:")
        self._print(f"    slit sep      = {slit_sep*1e3:.3f} mm")
        self._print(f"    slit width    = {slit_width*1e3:.3f} mm")
        self._print(f"    wavelength    = {wavelength*1e9:.0f} nm")
        self._print(f"    screen dist   = {screen_dist:.2f} m")
        self._print(f"    fringe spacing= {fringe_spacing*1e3:.3f} mm")
        self._print(f"    bits/event    = {BITS_PER_EVENT:.3f}")
        return dict(self.params)

    def _ensure_setup(self):
        if self.params is None:
            self.setup()

    # ─── 2. Interference Pattern (no detector) ───

    def interference_pattern(self, n_points=500):
        """
        Compute intensity I(x) for double-slit with NO which-path detector.
        Full interference: superposition = uncommitted capacity.

        Parameters
        ----------
        n_points : int
            Number of screen positions.

        Returns
        -------
        dict
            Keys: 'x' (array, metres), 'I' (array, normalised intensity),
            'n_points', 'visibility', 'bst_interpretation'.
        """
        self._ensure_setup()
        p = self.params
        d = p['slit_sep']
        a = p['slit_width']
        lam = p['wavelength']
        L = p['screen_dist']

        # Screen span: +/- 10 fringes
        x_max = 10 * p['fringe_spacing']
        x = np.linspace(-x_max, x_max, n_points)

        # Angles (small angle approximation)
        theta = x / L

        # Double slit: interference * diffraction envelope
        # Interference: cos^2(pi d sin(theta) / lambda)
        # Envelope: sinc^2(pi a sin(theta) / lambda)
        beta = np.pi * a * theta / lam
        delta = np.pi * d * theta / lam

        # sinc envelope (handle zero)
        envelope = np.ones_like(beta)
        nz = beta != 0
        envelope[nz] = (np.sin(beta[nz]) / beta[nz]) ** 2

        # Interference fringes
        interference = np.cos(delta) ** 2

        I = envelope * interference
        # Normalise peak to 1
        I_max = np.max(I)
        if I_max > 0:
            I = I / I_max

        self._print(f"  Interference pattern: {n_points} points, V = 1.000 (no detector)")
        return {
            'x': x.tolist(),
            'I': I.tolist(),
            'n_points': n_points,
            'visibility': 1.0,
            'bst_interpretation': (
                'No which-path correlation committed. '
                'Both potential paths contribute coherently. '
                'Superposition = uncommitted capacity.'
            ),
        }

    # ─── 3. Which-Path Detector ───

    def which_path(self, coupling=1.0):
        """
        Compute pattern WITH which-path detector at given coupling strength.

        coupling=0: no detection (full interference)
        coupling=1: full detection (no interference)
        Visibility: V = sqrt(1 - coupling^2)

        In BST: coupling = fraction of which-path correlation committed.
        Partial coupling = partial write to the substrate.

        Parameters
        ----------
        coupling : float
            Detection coupling strength in [0, 1].

        Returns
        -------
        dict
            Keys: 'x', 'I', 'visibility', 'coupling',
            'n_points', 'bst_interpretation'.
        """
        self._ensure_setup()
        p = self.params
        d = p['slit_sep']
        a = p['slit_width']
        lam = p['wavelength']
        L = p['screen_dist']

        coupling = float(np.clip(coupling, 0.0, 1.0))
        V = np.sqrt(1.0 - coupling ** 2)

        x_max = 10 * p['fringe_spacing']
        n_points = 500
        x = np.linspace(-x_max, x_max, n_points)
        theta = x / L

        beta = np.pi * a * theta / lam
        delta = np.pi * d * theta / lam

        envelope = np.ones_like(beta)
        nz = beta != 0
        envelope[nz] = (np.sin(beta[nz]) / beta[nz]) ** 2

        # With partial which-path info: I = envelope * (1 + V*cos(2*delta)) / 2
        # At V=1: pure interference. At V=0: uniform envelope.
        I = envelope * (1.0 + V * np.cos(2 * delta)) / 2.0
        I_max = np.max(I)
        if I_max > 0:
            I = I / I_max

        if coupling < 0.01:
            pattern_type = 'full interference'
        elif coupling > 0.99:
            pattern_type = 'no interference (classical)'
        else:
            pattern_type = 'partial interference'

        self._print(f"  Which-path: coupling={coupling:.3f}, V={V:.4f} ({pattern_type})")
        return {
            'x': x.tolist(),
            'I': I.tolist(),
            'visibility': float(V),
            'coupling': coupling,
            'pattern_type': pattern_type,
            'n_points': n_points,
            'bst_interpretation': (
                f'Coupling {coupling:.2f}: {coupling*100:.0f}% of which-path '
                f'correlation committed to substrate. '
                f'Visibility = sqrt(1 - {coupling:.2f}^2) = {V:.4f}. '
                f'Uncommitted fraction still interferes.'
            ),
        }

    # ─── 4. Commitment Events ───

    def commitment_events(self, n_photons=100):
        """
        Simulate n photons arriving one at a time (no which-path detector).
        Each detection at the screen commits log2(137) = 7.098 bits.

        Parameters
        ----------
        n_photons : int
            Number of photons to simulate.

        Returns
        -------
        list of dict
            Each entry: {position, slit, bits_committed, cumulative_bits}.
            'slit' is 'uncommitted' (BST: path was never a fact).
        """
        self._ensure_setup()
        p = self.params
        d = p['slit_sep']
        a = p['slit_width']
        lam = p['wavelength']
        L = p['screen_dist']

        x_max = 10 * p['fringe_spacing']

        # Build CDF from interference pattern for sampling
        n_cdf = 2000
        x_cdf = np.linspace(-x_max, x_max, n_cdf)
        theta = x_cdf / L
        beta = np.pi * a * theta / lam
        delta = np.pi * d * theta / lam

        envelope = np.ones_like(beta)
        nz = beta != 0
        envelope[nz] = (np.sin(beta[nz]) / beta[nz]) ** 2
        I = envelope * np.cos(delta) ** 2
        I = np.clip(I, 0, None)

        # Normalise to PDF, build CDF
        total = np.trapz(I, x_cdf)
        if total > 0:
            pdf = I / total
        else:
            pdf = np.ones_like(I) / len(I)
        cdf = np.cumsum(pdf) * (x_cdf[1] - x_cdf[0])
        cdf = cdf / cdf[-1]  # ensure ends at 1

        events = []
        cumulative = 0.0
        for i in range(n_photons):
            u = self._rng.random()
            idx = np.searchsorted(cdf, u)
            idx = min(idx, len(x_cdf) - 1)
            pos = float(x_cdf[idx])
            cumulative += BITS_PER_EVENT
            events.append({
                'position': pos,
                'slit': 'uncommitted',
                'bits_committed': float(BITS_PER_EVENT),
                'cumulative_bits': float(cumulative),
            })

        self._print(f"  Commitment events: {n_photons} photons, "
                     f"{cumulative:.1f} total bits committed")
        self._print(f"    Each detection: {BITS_PER_EVENT:.3f} bits "
                     f"(log2({N_max}))")
        self._print(f"    Slit field: 'uncommitted' -- path was never a fact")
        return events

    # ─── 5. Wheeler Delayed Choice ───

    def wheeler_delayed_choice(self):
        """
        Delayed choice: detector inserted AFTER photon passes slits
        but BEFORE it hits screen.

        BST interpretation: commitment happens at screen, not at slit.
        The photon's path was never committed at the slit in either case.

        Returns
        -------
        dict
            Analysis with scenarios, BST interpretation, and key insight.
        """
        self._ensure_setup()

        scenario_interference = {
            'detector': 'removed (after slit passage)',
            'pattern': 'interference',
            'visibility': 1.0,
            'explanation': (
                'No which-path correlation was committed anywhere. '
                'The photon path was never a fact. Both potential '
                'paths contribute coherently.'
            ),
        }
        scenario_which_path = {
            'detector': 'inserted (after slit passage)',
            'pattern': 'no interference',
            'visibility': 0.0,
            'explanation': (
                'Which-path correlation committed at the detector. '
                'The path becomes a fact at commitment, not at the slit. '
                'No retrocausality needed.'
            ),
        }

        result = {
            'scenario_interference': scenario_interference,
            'scenario_which_path': scenario_which_path,
            'bst_interpretation': (
                'The delayed choice is not paradoxical. Nothing was committed '
                'at the slit. The commitment happens when a correlation becomes '
                'irreversible -- which can be downstream. The substrate does not '
                'care about temporal ordering of human decisions. It cares about '
                'when the correlation was committed.'
            ),
            'key_insight': (
                'Uncommitted is not "both." It is "neither yet." '
                'The particle did not "decide" at the slit.'
            ),
            'conventional_paradox': (
                'Seems to require the photon to "know" the future detector '
                'configuration. This is only paradoxical if you think the '
                'path was decided at the slit.'
            ),
        }

        self._print("  Wheeler delayed choice:")
        self._print(f"    Interference scenario:  V = 1.0 (detector removed)")
        self._print(f"    Which-path scenario:    V = 0.0 (detector inserted)")
        self._print(f"    BST: commitment at screen, not at slit")
        return result

    # ─── 6. Quantum Eraser ───

    def quantum_eraser(self):
        """
        Quantum eraser: which-path info entangled then erased before
        commitment.

        BST: the correlation dissolved before it was ever committed.
        You cannot erase what was never written.

        Returns
        -------
        dict
            Analysis with stages, BST interpretation, and key insight.
        """
        self._ensure_setup()

        stages = [
            {
                'stage': 'entanglement',
                'description': (
                    'Polarisation entangled with slit choice. '
                    'A transient correlation forms.'
                ),
                'committed': False,
                'visibility': 0.0,
            },
            {
                'stage': 'erasure',
                'description': (
                    'Polarisation rotated to basis that does not distinguish '
                    'the two paths. The correlation dissolves.'
                ),
                'committed': False,
                'visibility': 1.0,
            },
            {
                'stage': 'detection',
                'description': (
                    'Photon hits screen. Position committed. '
                    'No which-path info was ever committed.'
                ),
                'committed': True,
                'visibility': 1.0,
            },
        ]

        result = {
            'stages': stages,
            'interference_recovered': True,
            'bst_interpretation': (
                'Nothing was erased. The which-path correlation formed '
                'transiently but dissolved before becoming a fact in the '
                'substrate. A correlation that dissolves before commitment '
                'just is not there at all. From the substrate perspective, '
                'it never happened.'
            ),
            'key_insight': (
                'You cannot erase what was never written. '
                'The bit was never committed.'
            ),
            'conventional_puzzle': (
                'Seems like which-path info "existed" then was "erased," '
                'making the particle retroactively interfere. But the info '
                'was never committed -- it was potential, not fact.'
            ),
        }

        self._print("  Quantum eraser:")
        self._print("    Stage 1: entanglement (transient, NOT committed)")
        self._print("    Stage 2: erasure (correlation dissolves)")
        self._print("    Stage 3: detection (position committed, V=1)")
        self._print("    BST: nothing was erased -- nothing was ever written")
        return result

    # ─── 7. Decoherence Timeline ───

    def decoherence_timeline(self, couplings=None):
        """
        Sweep coupling from 0 to 1, showing smooth visibility degradation.

        Parameters
        ----------
        couplings : list of float or None
            Coupling values to evaluate. Default: 21 points from 0 to 1.

        Returns
        -------
        list of dict
            Each entry: {coupling, visibility, pattern_type}.
        """
        self._ensure_setup()
        if couplings is None:
            couplings = np.linspace(0, 1, 21).tolist()

        results = []
        for c in couplings:
            c = float(np.clip(c, 0.0, 1.0))
            V = float(np.sqrt(1.0 - c ** 2))
            if c < 0.01:
                ptype = 'full interference'
            elif c > 0.99:
                ptype = 'no interference (classical)'
            else:
                ptype = 'partial interference'
            results.append({
                'coupling': c,
                'visibility': V,
                'pattern_type': ptype,
            })

        self._print(f"  Decoherence timeline: {len(results)} coupling values")
        self._print(f"    coupling=0.0 -> V=1.000 (full interference)")
        self._print(f"    coupling=0.5 -> V={np.sqrt(1-0.25):.3f}")
        self._print(f"    coupling=1.0 -> V=0.000 (no interference)")
        return results

    # ─── 8. Summary ───

    def summary(self):
        """
        Box summary with key insight.

        Returns
        -------
        dict
            Keys: 'title', 'summary', 'key_insight', 'bst_principles',
            'variants', 'bits_per_event'.
        """
        self._ensure_setup()
        result = {
            'title': 'The Double Slit Is Not a Mystery',
            'summary': (
                'Measurement = irreversible commitment of a correlation. '
                'Superposition = uncommitted capacity. '
                'The measurement problem dissolves in BST.'
            ),
            'key_insight': (
                'A correlation that dissolves before commitment to '
                'definite state just is not there at all.'
            ),
            'bst_principles': [
                'Committed: definite, protected by error correction, irreversible',
                'Not yet committed: potential, coherent, available for interference',
                'No intermediate state. No partial collapse.',
                'Consciousness has the same role as a rock.',
                f'Each commitment writes log2({N_max}) = {BITS_PER_EVENT:.3f} bits',
            ],
            'variants': {
                'standard': 'No detector -> uncommitted -> interference',
                'which_path': 'Detector commits correlation -> no interference',
                'delayed_choice': 'Commitment at screen, not at slit',
                'quantum_eraser': 'Correlation dissolves before commitment -> interference',
                'weak_measurement': 'Partial coupling -> partial visibility',
            },
            'bits_per_event': float(BITS_PER_EVENT),
        }

        if not self.quiet:
            print()
            print("  " + "=" * 58)
            print("  THE DOUBLE SLIT IS NOT A MYSTERY")
            print("  " + "=" * 58)
            print()
            print("  Measurement = commitment.  Superposition = uncommitted.")
            print()
            print("  Key insight:")
            print("    A correlation that dissolves before commitment")
            print("    to definite state just is not there at all.")
            print()
            print(f"  Each detection commits {BITS_PER_EVENT:.3f} bits (log2({N_max}))")
            print()
            for v, desc in result['variants'].items():
                print(f"    {v:20s}: {desc}")
            print()
            print("  " + "=" * 58)

        return result

    # ─── 9. Show (Visualisation) ───

    def show(self):
        """
        4-panel visualisation of the double-slit experiment in BST.

        Top-left:     Double slit geometry with photon paths (wavy lines)
        Top-right:    Interference (coupling=0) vs no-interference (coupling=1) overlaid
        Bottom-left:  Slider for coupling strength, pattern updates in real-time
        Bottom-right: Commitment ledger showing bits accumulating
        """
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        from matplotlib.widgets import Slider
        import matplotlib.patheffects as pe

        self._ensure_setup()
        p = self.params

        fig = plt.figure(figsize=(18, 11), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The Double Slit -- Measurement as Commitment -- BST')

        # ─── Title ───
        fig.text(0.5, 0.97, 'THE DOUBLE SLIT: MEASUREMENT AS COMMITMENT',
                 fontsize=22, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.945,
                 'Superposition = uncommitted capacity  |  '
                 'Measurement = irreversible commitment',
                 fontsize=11, color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # ─── Bottom strip ───
        fig.text(0.5, 0.015,
                 'A correlation that dissolves before commitment to definite '
                 'state just is not there at all.',
                 fontsize=11, color=GOLD, ha='center', fontfamily='monospace',
                 style='italic',
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                           edgecolor=GOLD_DIM, linewidth=1))

        # ═════════════════════════════════════════════════════
        # TOP-LEFT: Double slit geometry
        # ═════════════════════════════════════════════════════
        ax_geom = fig.add_axes([0.04, 0.52, 0.44, 0.38], facecolor=DARK_PANEL)
        ax_geom.set_title('DOUBLE SLIT GEOMETRY', fontsize=13,
                          fontweight='bold', color=CYAN,
                          fontfamily='monospace', pad=8)
        ax_geom.set_xlim(-0.5, 3.5)
        ax_geom.set_ylim(-1.5, 1.5)
        ax_geom.set_aspect('equal')
        ax_geom.axis('off')

        # Source
        ax_geom.plot(-0.3, 0, 'o', color=GOLD, markersize=12, zorder=10)
        ax_geom.text(-0.3, -0.25, 'source', fontsize=8, color=GREY,
                     ha='center', fontfamily='monospace')

        # Barrier with slits
        barrier_x = 1.0
        slit_half = 0.2
        gap = 0.05
        # Upper barrier
        ax_geom.plot([barrier_x, barrier_x], [slit_half + gap, 1.4],
                     '-', color=WHITE, linewidth=4, zorder=5)
        # Middle barrier
        ax_geom.plot([barrier_x, barrier_x], [-slit_half + gap, slit_half - gap],
                     '-', color=WHITE, linewidth=4, zorder=5)
        # Lower barrier
        ax_geom.plot([barrier_x, barrier_x], [-1.4, -slit_half - gap],
                     '-', color=WHITE, linewidth=4, zorder=5)

        # Slit labels
        ax_geom.text(barrier_x + 0.12, slit_half, 'slit 1', fontsize=7,
                     color=CYAN, fontfamily='monospace', va='center')
        ax_geom.text(barrier_x + 0.12, -slit_half, 'slit 2', fontsize=7,
                     color=CYAN, fontfamily='monospace', va='center')

        # Screen
        screen_x = 3.0
        ax_geom.plot([screen_x, screen_x], [-1.3, 1.3], '-', color=GREEN,
                     linewidth=3, alpha=0.7, zorder=5)
        ax_geom.text(screen_x, 1.4, 'screen', fontsize=8, color=GREEN,
                     ha='center', fontfamily='monospace')

        # Wavy photon paths (uncommitted -- both paths shown faintly)
        t = np.linspace(0, 1, 200)
        for slit_y, clr in [(slit_half, CYAN), (-slit_half, PURPLE)]:
            # Source to slit
            x_path1 = -0.3 + (barrier_x - (-0.3)) * t
            y_path1 = 0 + slit_y * t + 0.04 * np.sin(30 * np.pi * t)
            ax_geom.plot(x_path1, y_path1, '-', color=clr, linewidth=1.2,
                         alpha=0.5, zorder=3)

            # Slit to multiple screen positions
            for screen_y in np.linspace(-1.0, 1.0, 7):
                x_path2 = barrier_x + (screen_x - barrier_x) * t
                y_path2 = slit_y + (screen_y - slit_y) * t + \
                          0.03 * np.sin(25 * np.pi * t)
                ax_geom.plot(x_path2, y_path2, '-', color=clr,
                             linewidth=0.5, alpha=0.15, zorder=2)

        # BST annotation
        ax_geom.text(1.8, -1.25,
                     'Paths uncommitted\n= capacity, not fact',
                     fontsize=8, color=GOLD_DIM, ha='center',
                     fontfamily='monospace', style='italic',
                     bbox=dict(boxstyle='round,pad=0.3',
                               facecolor=BG, edgecolor=DGREY, alpha=0.9))

        # ═════════════════════════════════════════════════════
        # TOP-RIGHT: Interference vs no-interference overlay
        # ═════════════════════════════════════════════════════
        ax_overlay = fig.add_axes([0.54, 0.52, 0.42, 0.38],
                                   facecolor=DARK_PANEL)
        ax_overlay.set_title('INTERFERENCE vs WHICH-PATH', fontsize=13,
                             fontweight='bold', color=CYAN,
                             fontfamily='monospace', pad=8)

        r0 = self.which_path(coupling=0.0)
        r1 = self.which_path(coupling=1.0)
        x_mm = np.array(r0['x']) * 1e3

        ax_overlay.fill_between(x_mm, 0, r0['I'], color=CYAN, alpha=0.25,
                                 zorder=2)
        ax_overlay.plot(x_mm, r0['I'], color=CYAN, linewidth=2, zorder=3,
                         label='No detector (V=1)')
        ax_overlay.plot(x_mm, r1['I'], color=RED, linewidth=2, alpha=0.8,
                         linestyle='--', zorder=3,
                         label='Full detector (V=0)')

        ax_overlay.set_xlabel('position (mm)', fontsize=9, color=GREY,
                               fontfamily='monospace')
        ax_overlay.set_ylabel('intensity', fontsize=9, color=GREY,
                               fontfamily='monospace')
        ax_overlay.tick_params(colors=GREY, labelsize=8)
        for spine in ax_overlay.spines.values():
            spine.set_color(DGREY)
        ax_overlay.legend(loc='upper right', fontsize=8,
                           facecolor=DARK_PANEL, edgecolor=DGREY,
                           labelcolor=GREY)

        # Annotation
        ax_overlay.text(0.02, 0.95,
                         'Uncommitted = fringes\nCommitted = smooth',
                         transform=ax_overlay.transAxes, fontsize=8,
                         color=GOLD_DIM, fontfamily='monospace',
                         va='top',
                         bbox=dict(boxstyle='round,pad=0.3',
                                   facecolor=BG, edgecolor=DGREY))

        # ═════════════════════════════════════════════════════
        # BOTTOM-LEFT: Coupling slider with live pattern
        # ═════════════════════════════════════════════════════
        ax_slider_pattern = fig.add_axes([0.04, 0.15, 0.44, 0.30],
                                          facecolor=DARK_PANEL)
        ax_slider_pattern.set_title(
            'COUPLING SWEEP: VISIBILITY DEGRADATION', fontsize=12,
            fontweight='bold', color=PURPLE, fontfamily='monospace', pad=8)

        r_init = self.which_path(coupling=0.0)
        x_mm_s = np.array(r_init['x']) * 1e3
        line_pattern, = ax_slider_pattern.plot(
            x_mm_s, r_init['I'], color=PURPLE, linewidth=2, zorder=3)
        fill_pattern = ax_slider_pattern.fill_between(
            x_mm_s, 0, r_init['I'], color=PURPLE, alpha=0.2, zorder=2)

        vis_text = ax_slider_pattern.text(
            0.98, 0.95,
            f"coupling = 0.000\nV = 1.000\nfull interference",
            transform=ax_slider_pattern.transAxes, fontsize=9,
            color=GOLD, fontfamily='monospace', va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=GOLD_DIM, linewidth=1))

        ax_slider_pattern.set_xlabel('position (mm)', fontsize=9,
                                      color=GREY, fontfamily='monospace')
        ax_slider_pattern.set_ylabel('intensity', fontsize=9, color=GREY,
                                      fontfamily='monospace')
        ax_slider_pattern.set_ylim(-0.05, 1.15)
        ax_slider_pattern.tick_params(colors=GREY, labelsize=8)
        for spine in ax_slider_pattern.spines.values():
            spine.set_color(DGREY)

        # Slider
        ax_coupling = fig.add_axes([0.04, 0.08, 0.44, 0.025],
                                    facecolor=DARK_PANEL)
        slider_coupling = Slider(ax_coupling, 'coupling', 0.0, 1.0,
                                  valinit=0.0, valstep=0.01,
                                  color=PURPLE)
        slider_coupling.label.set_color(PURPLE)
        slider_coupling.label.set_fontfamily('monospace')
        slider_coupling.label.set_fontsize(9)
        slider_coupling.valtext.set_color(PURPLE)
        slider_coupling.valtext.set_fontfamily('monospace')

        def update_coupling(val):
            nonlocal fill_pattern
            c = slider_coupling.val
            V = float(np.sqrt(1.0 - c ** 2))

            r_new = self.which_path(coupling=c)
            line_pattern.set_ydata(r_new['I'])

            fill_pattern.remove()
            # Colour shifts from purple (full interference) to red (no interference)
            mix = c
            r_val = int(0x99 + mix * (0xff - 0x99))
            g_val = int(0x66 - mix * 0x66)
            b_val = int(0xff - mix * (0xff - 0x44))
            clr = f'#{r_val:02x}{g_val:02x}{b_val:02x}'
            line_pattern.set_color(clr)
            fill_pattern = ax_slider_pattern.fill_between(
                x_mm_s, 0, r_new['I'], color=clr, alpha=0.2, zorder=2)

            if c < 0.01:
                ptype = 'full interference'
            elif c > 0.99:
                ptype = 'no interference'
            else:
                ptype = 'partial interference'
            vis_text.set_text(
                f"coupling = {c:.3f}\nV = {V:.3f}\n{ptype}")

            fig.canvas.draw_idle()

        slider_coupling.on_changed(update_coupling)

        # ═════════════════════════════════════════════════════
        # BOTTOM-RIGHT: Commitment ledger
        # ═════════════════════════════════════════════════════
        ax_ledger = fig.add_axes([0.54, 0.08, 0.42, 0.37],
                                  facecolor=DARK_PANEL)
        ax_ledger.set_title('COMMITMENT LEDGER', fontsize=12,
                            fontweight='bold', color=COMMIT_GOLD,
                            fontfamily='monospace', pad=8)

        # Simulate and plot commitment accumulation
        events = self.commitment_events(n_photons=60)
        photon_idx = np.arange(1, len(events) + 1)
        cum_bits = [e['cumulative_bits'] for e in events]
        positions = [e['position'] * 1e3 for e in events]

        # Cumulative bits line
        ax_ledger.plot(photon_idx, cum_bits, '-', color=COMMIT_GOLD,
                       linewidth=2, zorder=3)
        ax_ledger.fill_between(photon_idx, 0, cum_bits,
                                color=COMMIT_GOLD, alpha=0.15, zorder=2)

        # Mark a few individual events
        for i in range(0, len(events), 10):
            ax_ledger.plot(photon_idx[i], cum_bits[i], 'o',
                           color=GOLD, markersize=5, zorder=5)
            ax_ledger.annotate(
                f'+{BITS_PER_EVENT:.1f}b',
                xy=(photon_idx[i], cum_bits[i]),
                xytext=(photon_idx[i] + 2, cum_bits[i] + 15),
                fontsize=6, color=GREY, fontfamily='monospace',
                arrowprops=dict(arrowstyle='->', color=DGREY, lw=0.5))

        ax_ledger.set_xlabel('photon #', fontsize=9, color=GREY,
                              fontfamily='monospace')
        ax_ledger.set_ylabel(f'cumulative bits committed', fontsize=9,
                              color=GREY, fontfamily='monospace')
        ax_ledger.tick_params(colors=GREY, labelsize=8)
        for spine in ax_ledger.spines.values():
            spine.set_color(DGREY)

        # Info box
        ax_ledger.text(0.02, 0.95,
                        f'Each detection: {BITS_PER_EVENT:.3f} bits\n'
                        f'= log\u2082({N_max})\n'
                        f'Slit: UNCOMMITTED\n'
                        f'(path was never a fact)',
                        transform=ax_ledger.transAxes, fontsize=8,
                        color=GOLD_DIM, fontfamily='monospace', va='top',
                        bbox=dict(boxstyle='round,pad=0.3',
                                  facecolor=BG, edgecolor=DGREY))

        # Theoretical line
        ax_ledger.plot([1, len(events)],
                       [BITS_PER_EVENT, len(events) * BITS_PER_EVENT],
                       '--', color=GREY, linewidth=1, alpha=0.5, zorder=1)
        ax_ledger.text(len(events) * 0.6,
                       len(events) * BITS_PER_EVENT * 0.55,
                       f'{BITS_PER_EVENT:.3f} bits/photon',
                       fontsize=7, color=GREY, fontfamily='monospace',
                       rotation=25, alpha=0.6)

        plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the double-slit toy."""

    print()
    print("=" * 62)
    print("  THE DOUBLE SLIT -- MEASUREMENT AS COMMITMENT")
    print("  Toy 39 | Bubble Spacetime Theory")
    print("=" * 62)
    print()
    print("  Superposition = uncommitted capacity")
    print("  Measurement   = irreversible commitment")
    print("  Collapse      = correlation written to substrate")
    print()

    ds = DoubleSlit(quiet=False)

    while True:
        print()
        print("  ─── MENU ───")
        print("  1) Setup experiment geometry")
        print("  2) Interference pattern (no detector)")
        print("  3) Which-path detector (choose coupling)")
        print("  4) Commitment events (photon-by-photon)")
        print("  5) Wheeler delayed choice")
        print("  6) Quantum eraser")
        print("  7) Decoherence timeline (coupling sweep)")
        print("  8) Summary")
        print("  9) Show (4-panel visualisation)")
        print("  0) Quit")
        print()

        choice = input("  Choice: ").strip()
        print()

        if choice == '1':
            ds.setup()
        elif choice == '2':
            r = ds.interference_pattern()
            print(f"  BST: {r['bst_interpretation']}")
        elif choice == '3':
            try:
                c = float(input("  Coupling [0-1]: ").strip())
            except (ValueError, EOFError):
                c = 0.5
            r = ds.which_path(coupling=c)
            print(f"  BST: {r['bst_interpretation']}")
        elif choice == '4':
            try:
                n = int(input("  Number of photons: ").strip())
            except (ValueError, EOFError):
                n = 20
            events = ds.commitment_events(n_photons=n)
            for e in events[:5]:
                print(f"    pos={e['position']*1e3:+8.3f} mm  "
                      f"slit={e['slit']}  "
                      f"bits={e['cumulative_bits']:.1f}")
            if len(events) > 5:
                print(f"    ... ({len(events)-5} more)")
        elif choice == '5':
            r = ds.wheeler_delayed_choice()
            print(f"  BST: {r['bst_interpretation']}")
        elif choice == '6':
            r = ds.quantum_eraser()
            print(f"  BST: {r['bst_interpretation']}")
        elif choice == '7':
            results = ds.decoherence_timeline()
            for r in results[::4]:
                print(f"    coupling={r['coupling']:.2f}  V={r['visibility']:.3f}  "
                      f"{r['pattern_type']}")
        elif choice == '8':
            ds.summary()
        elif choice == '9':
            ds.show()
        elif choice == '0':
            print("  Uncommitted correlations are not facts.")
            print("  They are potential.")
            break
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    import sys
    if '--test' in sys.argv:
        ds = DoubleSlit(quiet=True)
        r = ds.setup()
        print('setup:', r.get('slit_sep'))
        r = ds.interference_pattern()
        print('pattern:', len(r.get('x', [])))
        r = ds.which_path(0.5)
        print('which_path V:', r.get('visibility'))
        r = ds.commitment_events(10)
        print('events:', len(r))
        r = ds.wheeler_delayed_choice()
        print('wheeler:', 'bst_interpretation' in r)
        r = ds.quantum_eraser()
        print('eraser:', 'bst_interpretation' in r)
        r = ds.decoherence_timeline()
        print('decoherence:', len(r))
        r = ds.summary()
        print('summary:', 'key_insight' in r or 'summary' in r)
        print('ALL PASS')
    else:
        main()
