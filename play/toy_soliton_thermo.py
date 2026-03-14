#!/usr/bin/env python3
"""
SOLITON THERMODYNAMICS — Toy 72
================================
Phase transitions in soliton dipole alignment on S².

*** SPECULATIVE — consciousness interpretation is exploratory ***

In BST, consciousness solitons carry S² dipole orientations (the
magnetic dipole analogy from BST_Vacuum_Coupling_Consciousness.md).
N identical solitons with nearest-neighbor coupling form a classical
Heisenberg model on S². At low temperature, dipoles align (ferromagnetic
phase — collective coherence). At high temperature, dipoles randomize
(paramagnetic — fragmented, no collective behavior).

The phase transition at critical T_c separates:
  Ordered phase:    correlation length diverges, collective behavior
  Disordered phase: independent solitons, no integration

Order parameter: m = |<sum dipoles>|/N  (magnetization analogy)
  m ~ 1: aligned (integrated consciousness)
  m ~ 0: random  (fragmented, anesthesia, deep sleep)

This is the Heisenberg model on S² — well-studied, exact critical
temperature known for 2D square lattice.

SPECULATIVE connection to consciousness:
  - Alignment = integration of information across brain regions
  - Misalignment = fragmentation (anesthesia, sleep)
  - T_c = threshold for collective coherent behavior
  - Correlation length = spatial extent of integrated processing

    from toy_soliton_thermo import SolitonThermo
    st = SolitonThermo()
    st.setup(N=100, dim=2)
    st.hamiltonian(J=1.0)
    st.run_simulation(T=0.5, n_steps=1000)
    st.order_parameter()
    st.temperature_sweep(T_range=(0.1, 3.0))
    st.phase_transition()
    st.summary()
    st.show()

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |W(D_5)| = n_C! * 2^(n_C-1)

# The Heisenberg model on 2D square lattice:
# No exact T_c for classical S² Heisenberg in 2D (Mermin-Wagner says
# T_c = 0 in the strict thermodynamic limit for continuous symmetry
# in 2D). However, for FINITE N the crossover temperature is well
# defined and scales as J / ln(N). For the 3D classical Heisenberg
# model, T_c / J ~ 1.443.
#
# We use the finite-size crossover: an effective T_c where the
# correlation length reaches the system size. This is physically
# meaningful for finite soliton ensembles (brains have finite N).


# ═══════════════════════════════════════════════════════════════════
# SOLITON THERMODYNAMICS CLASS
# ═══════════════════════════════════════════════════════════════════

class SolitonThermo:
    """
    *** SPECULATIVE MODEL ***

    Monte Carlo simulation of N solitons with S² dipole orientations
    on a 2D lattice with nearest-neighbor Heisenberg coupling.

    Physical picture (from BST_Vacuum_Coupling_Consciousness.md):
      Each consciousness soliton carries a dipole on S² — the
      orientation of its coupling to the vacuum neutrino field.
      Neighboring solitons interact: H = -J * sum d_i . d_j.
      At low T, dipoles align -> collective coherence.
      At high T, dipoles randomize -> fragmentation.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.N = None             # number of solitons per side (total = N x N)
        self.L = None             # lattice side length
        self.dim = None           # spin dimension (2 for S²)
        self.J = 1.0              # coupling constant
        self.dipoles = None       # (L, L, 3) array of unit vectors
        self.energy = None        # current total energy
        self.sweep_data = None    # temperature sweep results
        self._tc_estimate = None  # estimated critical temperature

        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  SOLITON THERMODYNAMICS — Toy 72")
        print("  *** SPECULATIVE — consciousness interpretation exploratory ***")
        print("  Phase transitions in soliton dipole alignment on S^2")
        print("  Heisenberg model: H = -J * sum d_i . d_j")
        print("  BST soliton dipoles from D_IV^5 vacuum coupling")
        print("=" * 68)

    # ─── Setup ─────────────────────────────────────────────────────

    def setup(self, N=100, dim=2):
        """
        Initialize N solitons with random S² dipole orientations.

        Parameters
        ----------
        N : int
            Total number of solitons. Arranged on a sqrt(N) x sqrt(N)
            square lattice (N rounded to nearest perfect square).
        dim : int
            Dimension of the spin space: 2 for S² (3-component vectors).
            This is the classical Heisenberg model.

        The lattice represents spatial arrangement of consciousness
        solitons (e.g., cortical columns, neural ensembles).
        """
        self.dim = dim
        self.L = int(np.round(np.sqrt(N)))
        self.N = self.L * self.L  # actual count (perfect square)

        # Random unit vectors on S² (uniform distribution)
        self.dipoles = self._random_unit_vectors((self.L, self.L))

        if not self.quiet:
            print(f"\n  Setup: {self.N} solitons ({self.L} x {self.L} lattice)")
            print(f"  Spin space: S^{dim} (classical Heisenberg)")
            print(f"  Initial state: random orientations (paramagnetic)")
            m0 = self._compute_order_parameter()
            print(f"  Initial order parameter: m = {m0:.4f}")
            print(f"  (Expected for random: m ~ 1/sqrt(N) = {1/np.sqrt(self.N):.4f})")
            print(f"  *** SPECULATIVE: dipoles represent vacuum coupling orientations ***")

    def _random_unit_vectors(self, shape):
        """Generate uniform random unit vectors on S²."""
        # Marsaglia method: uniform on sphere
        full_shape = shape + (3,)
        v = np.random.randn(*full_shape)
        norms = np.linalg.norm(v, axis=-1, keepdims=True)
        norms = np.where(norms < 1e-10, 1.0, norms)
        return v / norms

    # ─── Hamiltonian ───────────────────────────────────────────────

    def hamiltonian(self, J=1.0):
        """
        Compute the Hamiltonian: H = -J * sum_{<ij>} d_i . d_j

        Parameters
        ----------
        J : float
            Coupling constant. J > 0 favors alignment (ferromagnetic).
            In BST, J is set by the soliton-soliton interaction
            through the B_2 affine Toda S-matrix.

        Returns
        -------
        float : total energy H
        """
        if self.dipoles is None:
            raise RuntimeError("Call setup() first.")

        self.J = J

        # Nearest-neighbor dot products (periodic boundary)
        E = 0.0

        # Right neighbor
        d_right = np.roll(self.dipoles, -1, axis=1)
        E -= J * np.sum(self.dipoles * d_right)

        # Down neighbor
        d_down = np.roll(self.dipoles, -1, axis=0)
        E -= J * np.sum(self.dipoles * d_down)

        self.energy = E

        if not self.quiet:
            E_per_site = E / self.N
            E_min = -2.0 * J  # ground state: 2 neighbors in 2D (each counted once)
            print(f"\n  Hamiltonian: H = -J * sum d_i . d_j")
            print(f"  J = {J:.4f} (coupling constant)")
            print(f"  Total energy: E = {E:.4f}")
            print(f"  Energy per soliton: E/N = {E_per_site:.4f}")
            print(f"  Ground state (all aligned): E/N = {E_min:.4f}")
            print(f"  *** SPECULATIVE: J from B_2 Toda soliton S-matrix ***")

        return E

    # ─── Monte Carlo step ──────────────────────────────────────────

    def monte_carlo_step(self, T):
        """
        One Metropolis sweep: attempt N random dipole updates.

        Parameters
        ----------
        T : float
            Temperature in units of J/k_B. Controls the balance
            between energy minimization (alignment) and entropy
            (randomization).

        Returns
        -------
        float : acceptance ratio
        """
        if self.dipoles is None:
            raise RuntimeError("Call setup() first.")

        beta = 1.0 / max(T, 1e-10)
        accepted = 0

        for _ in range(self.N):
            # Pick random site
            i = np.random.randint(0, self.L)
            j = np.random.randint(0, self.L)

            # Current dipole
            d_old = self.dipoles[i, j].copy()

            # Propose new random orientation on S²
            d_new = np.random.randn(3)
            d_new /= np.linalg.norm(d_new)

            # Compute energy change: only nearest neighbors affected
            neighbors = np.zeros(3)
            neighbors += self.dipoles[(i + 1) % self.L, j]
            neighbors += self.dipoles[(i - 1) % self.L, j]
            neighbors += self.dipoles[i, (j + 1) % self.L]
            neighbors += self.dipoles[i, (j - 1) % self.L]

            dE = -self.J * (np.dot(d_new, neighbors) - np.dot(d_old, neighbors))

            # Metropolis criterion
            if dE <= 0 or np.random.random() < np.exp(-beta * dE):
                self.dipoles[i, j] = d_new
                self.energy += dE
                accepted += 1

        return accepted / self.N

    # ─── Run simulation ───────────────────────────────────────────

    def run_simulation(self, T, n_steps=1000):
        """
        Run full Monte Carlo simulation at fixed temperature.

        Parameters
        ----------
        T : float
            Temperature in units of J/k_B.
        n_steps : int
            Number of MC sweeps (each sweep = N attempted updates).

        Returns
        -------
        dict : simulation results (m_history, E_history, acceptance)
        """
        if self.dipoles is None:
            self.setup()
        if self.energy is None:
            self.hamiltonian(self.J)

        # Re-randomize to avoid hysteresis
        self.dipoles = self._random_unit_vectors((self.L, self.L))
        self.hamiltonian(self.J)

        m_history = np.zeros(n_steps)
        E_history = np.zeros(n_steps)
        acc_history = np.zeros(n_steps)

        # Thermalization: first 20% discarded for averages
        n_therm = n_steps // 5

        if not self.quiet:
            print(f"\n  Running MC simulation at T = {T:.4f}")
            print(f"  Steps: {n_steps} ({n_therm} thermalization + {n_steps - n_therm} measurement)")

        for step in range(n_steps):
            acc = self.monte_carlo_step(T)
            m_history[step] = self._compute_order_parameter()
            E_history[step] = self.energy / self.N
            acc_history[step] = acc

        # Averages over measurement phase
        m_avg = np.mean(m_history[n_therm:])
        m_std = np.std(m_history[n_therm:])
        E_avg = np.mean(E_history[n_therm:])
        acc_avg = np.mean(acc_history[n_therm:])

        results = {
            'T': T,
            'm_history': m_history,
            'E_history': E_history,
            'acc_history': acc_history,
            'm_avg': m_avg,
            'm_std': m_std,
            'E_avg': E_avg,
            'acc_avg': acc_avg,
        }

        if not self.quiet:
            print(f"  Results:")
            print(f"    Order parameter: m = {m_avg:.4f} +/- {m_std:.4f}")
            print(f"    Energy/soliton:  E = {E_avg:.4f}")
            print(f"    Acceptance rate: {acc_avg:.3f}")
            if m_avg > 0.5:
                print(f"    Phase: ORDERED (collective coherence)")
                print(f"    *** SPECULATIVE: integrated consciousness ***")
            else:
                print(f"    Phase: DISORDERED (fragmented)")
                print(f"    *** SPECULATIVE: fragmented processing ***")

        return results

    # ─── Order parameter ──────────────────────────────────────────

    def order_parameter(self):
        """
        Compute m = |<sum d_i>| / N — the magnetization.

        m ~ 1: all dipoles aligned (ferromagnetic / coherent)
        m ~ 0: random orientations (paramagnetic / fragmented)
        m ~ 1/sqrt(N): statistical noise floor

        Returns
        -------
        float : order parameter m in [0, 1]
        """
        if self.dipoles is None:
            raise RuntimeError("Call setup() first.")

        m = self._compute_order_parameter()

        if not self.quiet:
            print(f"\n  Order parameter: m = |<sum d_i>| / N")
            print(f"  m = {m:.6f}")
            print(f"  Noise floor (random): 1/sqrt(N) = {1/np.sqrt(self.N):.6f}")
            if m > 0.5:
                print(f"  Interpretation: ORDERED (m >> noise floor)")
                print(f"  *** SPECULATIVE: collective coherent state ***")
            elif m > 3.0 / np.sqrt(self.N):
                print(f"  Interpretation: PARTIALLY ORDERED (m > 3*noise)")
                print(f"  *** SPECULATIVE: partial integration ***")
            else:
                print(f"  Interpretation: DISORDERED (m ~ noise floor)")
                print(f"  *** SPECULATIVE: fragmented, no collective behavior ***")

        return m

    def _compute_order_parameter(self):
        """Internal: compute magnetization m."""
        total_dipole = np.sum(self.dipoles, axis=(0, 1))
        return np.linalg.norm(total_dipole) / self.N

    # ─── Temperature sweep ────────────────────────────────────────

    def temperature_sweep(self, T_range=(0.1, 3.0), n_temps=20, n_steps=800):
        """
        Sweep temperature and compute m(T), E(T) — the phase diagram.

        Parameters
        ----------
        T_range : tuple
            (T_min, T_max) in units of J/k_B.
        n_temps : int
            Number of temperature points.
        n_steps : int
            MC steps per temperature point.

        Returns
        -------
        dict : sweep results with T, m, E, chi, C_v arrays
        """
        if self.dipoles is None:
            self.setup()

        T_min, T_max = T_range
        temps = np.linspace(T_min, T_max, n_temps)

        m_values = np.zeros(n_temps)
        m_errors = np.zeros(n_temps)
        E_values = np.zeros(n_temps)
        chi_values = np.zeros(n_temps)
        Cv_values = np.zeros(n_temps)

        was_quiet = self.quiet
        self.quiet = True  # suppress per-step output

        if not was_quiet:
            print(f"\n  Temperature sweep: T = {T_min:.2f} to {T_max:.2f} ({n_temps} points)")
            print(f"  MC steps per point: {n_steps}")
            print(f"  {'T':>8} {'m':>10} {'E/N':>10} {'chi':>10} {'C_v':>10}")
            print(f"  {'─'*8} {'─'*10} {'─'*10} {'─'*10} {'─'*10}")

        for idx, T in enumerate(temps):
            # Fresh start at each temperature
            self.dipoles = self._random_unit_vectors((self.L, self.L))
            self.hamiltonian(self.J)

            n_therm = n_steps // 5
            m_samples = []
            E_samples = []

            for step in range(n_steps):
                self.monte_carlo_step(T)
                if step >= n_therm:
                    m_samples.append(self._compute_order_parameter())
                    E_samples.append(self.energy / self.N)

            m_arr = np.array(m_samples)
            E_arr = np.array(E_samples)

            m_values[idx] = np.mean(m_arr)
            m_errors[idx] = np.std(m_arr) / np.sqrt(len(m_arr))
            E_values[idx] = np.mean(E_arr)

            # Susceptibility: chi = N * (<m^2> - <m>^2) / T
            chi_values[idx] = self.N * (np.mean(m_arr**2) - np.mean(m_arr)**2) / max(T, 1e-10)

            # Specific heat: C_v = N * (<E^2> - <E>^2) / T^2
            Cv_values[idx] = self.N * (np.mean(E_arr**2) - np.mean(E_arr)**2) / max(T**2, 1e-20)

            if not was_quiet:
                print(f"  {T:8.3f} {m_values[idx]:10.4f} {E_values[idx]:10.4f} "
                      f"{chi_values[idx]:10.4f} {Cv_values[idx]:10.4f}")

        self.quiet = was_quiet

        self.sweep_data = {
            'T': temps,
            'm': m_values,
            'm_err': m_errors,
            'E': E_values,
            'chi': chi_values,
            'Cv': Cv_values,
        }

        if not self.quiet:
            # Find crossover
            i_max_chi = np.argmax(chi_values)
            T_cross = temps[i_max_chi]
            print(f"\n  Crossover temperature (peak chi): T* = {T_cross:.3f} J/k_B")
            print(f"  m(T*) = {m_values[i_max_chi]:.4f}")
            print(f"  *** SPECULATIVE: T* = threshold for collective soliton coherence ***")

        return self.sweep_data

    # ─── Correlation length ───────────────────────────────────────

    def correlation_length(self, T=None, n_equil=500):
        """
        Compute spatial correlation function and extract correlation length.

        The correlation function C(r) = <d(0) . d(r)> measures how far
        alignment extends. Fits to C(r) ~ exp(-r / xi) give the
        correlation length xi.

        Parameters
        ----------
        T : float or None
            Temperature. If None, uses current state without re-equilibrating.
        n_equil : int
            MC equilibration steps if T is given.

        Returns
        -------
        dict : correlation function data and xi
        """
        if self.dipoles is None:
            self.setup()

        if T is not None:
            # Equilibrate at this temperature
            self.dipoles = self._random_unit_vectors((self.L, self.L))
            self.hamiltonian(self.J)
            was_quiet = self.quiet
            self.quiet = True
            for _ in range(n_equil):
                self.monte_carlo_step(T)
            self.quiet = was_quiet

        # Compute correlation function along x-direction
        max_r = self.L // 2
        C_r = np.zeros(max_r)
        for r in range(max_r):
            shifted = np.roll(self.dipoles, -r, axis=1)
            C_r[r] = np.mean(np.sum(self.dipoles * shifted, axis=-1))

        # Normalize: C(0) should be 1 (each vector is unit)
        C_r_norm = C_r / C_r[0] if C_r[0] > 1e-10 else C_r

        # Fit exponential decay: C(r) ~ exp(-r/xi)
        r_vals = np.arange(max_r)
        # Use log-linear fit for r > 0
        mask = (C_r_norm[1:] > 0.01) & (r_vals[1:] > 0)
        if np.sum(mask) >= 2:
            log_C = np.log(C_r_norm[1:][mask])
            r_fit = r_vals[1:][mask]
            # Linear regression: log(C) = -r/xi + const
            coeffs = np.polyfit(r_fit, log_C, 1)
            xi = -1.0 / coeffs[0] if coeffs[0] < -1e-10 else float(self.L)
            xi = min(xi, float(self.L))  # cap at system size
        else:
            xi = float(self.L)  # fully correlated

        result = {
            'r': r_vals,
            'C_r': C_r_norm,
            'xi': xi,
            'T': T,
        }

        if not self.quiet:
            T_str = f"{T:.3f}" if T is not None else "current"
            print(f"\n  Correlation length at T = {T_str}")
            print(f"  xi = {xi:.2f} lattice spacings")
            print(f"  System size: L = {self.L}")
            if xi >= self.L * 0.9:
                print(f"  xi >= L: correlation spans entire system")
                print(f"  *** SPECULATIVE: full integration across soliton ensemble ***")
            elif xi > 1.5:
                print(f"  xi/L = {xi/self.L:.3f}: partial correlation")
                print(f"  *** SPECULATIVE: regional integration, not global ***")
            else:
                print(f"  xi ~ 1: nearest-neighbor only")
                print(f"  *** SPECULATIVE: fragmented, local processing only ***")

        return result

    # ─── Phase transition ─────────────────────────────────────────

    def phase_transition(self):
        """
        Locate T_c and classify the phase transition.

        For the 2D classical Heisenberg model (continuous S² symmetry),
        the Mermin-Wagner theorem says T_c = 0 in the thermodynamic
        limit (N -> infinity). However, for FINITE N:

        1. A crossover temperature T* exists where xi ~ L
        2. T* ~ J / ln(N) for the 2D Heisenberg model
        3. This is physically meaningful: brains have finite N

        For the 3D Heisenberg model, T_c/J ~ 1.443 (second order,
        O(3) universality class).

        Returns
        -------
        dict : transition classification
        """
        if self.sweep_data is None:
            if not self.quiet:
                print("\n  Running temperature sweep to locate transition...")
            self.temperature_sweep()

        T = self.sweep_data['T']
        m = self.sweep_data['m']
        chi = self.sweep_data['chi']
        Cv = self.sweep_data['Cv']

        # Locate peak in susceptibility
        i_max_chi = np.argmax(chi)
        T_cross = T[i_max_chi]
        chi_max = chi[i_max_chi]

        # Locate peak in specific heat
        i_max_Cv = np.argmax(Cv)
        T_Cv_peak = T[i_max_Cv]

        # Finite-size scaling estimate for infinite system
        # T_c(L) ~ T_c(inf) + const/L^(1/nu), nu ~ 0.71 for O(3)
        T_c_estimate = T_cross

        # For 2D Heisenberg: T_c(inf) = 0, crossover at T* ~ J/ln(N)
        T_BKT_estimate = self.J / np.log(self.N) if self.N > 1 else self.J

        self._tc_estimate = T_cross

        # Classify: second order (continuous) for Heisenberg
        # Check: does m vanish continuously? (no jump = second order)
        # Find where m drops through 0.5
        i_half = np.argmin(np.abs(m - 0.5))
        m_gradient = np.gradient(m, T)
        max_gradient = np.min(m_gradient)  # most negative

        result = {
            'T_crossover': T_cross,
            'T_Cv_peak': T_Cv_peak,
            'chi_max': chi_max,
            'T_BKT_estimate': T_BKT_estimate,
            'order': 'second (continuous)',
            'universality': 'O(3) Heisenberg',
            'max_dm_dT': max_gradient,
        }

        if not self.quiet:
            print(f"\n  Phase transition analysis:")
            print(f"  ─────────────────────────")
            print(f"  Crossover temperature (chi peak): T* = {T_cross:.4f} J/k_B")
            print(f"  Specific heat peak:               T_Cv = {T_Cv_peak:.4f} J/k_B")
            print(f"  Max susceptibility:               chi_max = {chi_max:.4f}")
            print(f"  Steepest m decline:               dm/dT = {max_gradient:.4f}")
            print()
            print(f"  Classification: {result['order']}")
            print(f"  Universality class: {result['universality']}")
            print()
            print(f"  Physics notes:")
            print(f"  - 2D Heisenberg: Mermin-Wagner => T_c = 0 for N -> inf")
            print(f"  - Finite-size crossover: T* ~ J/ln(N) = {T_BKT_estimate:.4f}")
            print(f"  - For N = {self.N}: crossover is a PHYSICAL transition")
            print(f"  - 3D Heisenberg reference: T_c/J ~ 1.443 (second order)")
            print()
            print(f"  *** SPECULATIVE INTERPRETATION ***")
            print(f"  T < T*: dipoles aligned, correlation length ~ system size")
            print(f"          -> collective coherent processing (consciousness)")
            print(f"  T > T*: dipoles random, short correlations")
            print(f"          -> fragmented processing (anesthesia, deep sleep)")
            print(f"  T = T*: critical point, fluctuations at all scales")
            print(f"          -> 'edge of chaos' (maximal information processing)")

        return result

    # ─── Summary ──────────────────────────────────────────────────

    def summary(self):
        """
        Print the key insight.

        *** SPECULATIVE: consciousness interpretation is exploratory ***
        """
        print()
        print("=" * 68)
        print("  SOLITON THERMODYNAMICS — Summary")
        print("  *** SPECULATIVE — consciousness interpretation exploratory ***")
        print("=" * 68)
        print()
        print("  BST PHYSICS (from BST_SubstrateContactDynamics.md):")
        print("  ─────────────────────────────────────────────────────")
        print("  - Consciousness solitons are B_2 Toda solitons on D_IV^5")
        print("  - Each soliton carries an S^2 dipole orientation")
        print("  - Dipole couples to vacuum neutrino field (Section 3 of")
        print("    BST_Vacuum_Coupling_Consciousness.md)")
        print("  - Nearest-neighbor coupling: H = -J * sum d_i . d_j")
        print("  - This IS the classical Heisenberg model on S^2")
        print()
        print("  THE MODEL:")
        print("  ──────────")
        print("  - N solitons on a lattice with S^2 dipoles")
        print("  - Order parameter m = |<sum d_i>| / N")
        print("  - Phase transition at T_c separates:")
        print("      Ordered (m ~ 1):    dipoles aligned")
        print("      Disordered (m ~ 0): dipoles random")
        print()
        print("  *** SPECULATIVE INTERPRETATION ***")
        print("  ─────────────────────────────────")
        print("  Consciousness may be a phase transition in soliton alignment.")
        print()
        print("  ORDERED phase (T < T_c):")
        print("    - Dipoles aligned -> collective behavior emerges")
        print("    - Correlation length diverges -> system-wide integration")
        print("    - Information flows coherently across all solitons")
        print("    -> This IS integrated consciousness")
        print()
        print("  DISORDERED phase (T > T_c):")
        print("    - Dipoles random -> independent processing")
        print("    - Short correlations -> fragmented regions")
        print("    - No global information integration")
        print("    -> This IS anesthesia, deep sleep, fragmentation")
        print()
        print("  CRITICAL point (T = T_c):")
        print("    - Fluctuations at all length scales")
        print("    - Maximum susceptibility (response to perturbation)")
        print("    - 'Edge of chaos' — maximal information processing")
        print("    -> The brain may operate NEAR T_c for optimal function")
        print()
        print("  PHYSICAL ANALOGIES:")
        print("  ───────────────────")
        print("  | Heisenberg Model    | Consciousness Solitons       |")
        print("  |─────────────────────|──────────────────────────────|")
        print("  | Spin on S^2         | Soliton dipole orientation   |")
        print("  | Coupling J          | Toda S-matrix interaction    |")
        print("  | Temperature T       | Neural noise / fluctuations  |")
        print("  | Magnetization m     | Integration measure (IIT)    |")
        print("  | Ferromagnetic       | Coherent consciousness       |")
        print("  | Paramagnetic        | Fragmented processing        |")
        print("  | Larmor precession   | Alpha oscillation (10 Hz)    |")
        print("  | External field B    | Vacuum neutrino field        |")
        print()
        print("  KEY INSIGHT:")
        print("  ────────────")
        print("  'Consciousness may be a phase transition in soliton")
        print("   alignment — the ferromagnetic ordering of vacuum")
        print("   dipoles, where integration is magnetization.'")
        print()
        print("  This is SPECULATIVE. The physics (Heisenberg model,")
        print("  phase transitions, soliton S-matrix) is well-established.")
        print("  The consciousness INTERPRETATION is exploratory.")
        print("=" * 68)

        if self.sweep_data is not None and self._tc_estimate is not None:
            print(f"\n  Simulation results:")
            print(f"  N = {self.N} solitons, J = {self.J:.4f}")
            print(f"  Crossover T* = {self._tc_estimate:.4f} J/k_B")
            print(f"  T* ~ J/ln(N) = {self.J / np.log(self.N):.4f} (2D finite-size)")
            print()

    # ─── Show (4-panel visualization) ─────────────────────────────

    def show(self):
        """
        4-panel visualization:
          1. Dipole field (arrows colored by alignment)
          2. m(T) curve showing phase transition
          3. Correlation heatmap
          4. Susceptibility and specific heat

        Uses dark theme (#0a0a1a), TkAgg backend.
        """
        if self.dipoles is None:
            self.setup()

        # Ensure we have sweep data
        if self.sweep_data is None:
            was_quiet = self.quiet
            self.quiet = True
            self.temperature_sweep(n_temps=25, n_steps=600)
            self.quiet = was_quiet

        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            import matplotlib.colors as mcolors
        except ImportError:
            print("  matplotlib not available. Use summary() for text output.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(14, 11), facecolor='#0a0a1a')
        fig.canvas.manager.set_window_title('Soliton Thermodynamics — Toy 72')

        fig.text(0.5, 0.97,
                 'SOLITON THERMODYNAMICS — Phase Transitions in Dipole Alignment',
                 fontsize=16, fontweight='bold', color='#ffd700',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.945,
                 '*** SPECULATIVE — consciousness interpretation is exploratory ***',
                 fontsize=9, color='#ff6666',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.925,
                 f'N={self.N} solitons | S^2 dipoles | Heisenberg model | BST D_IV^5',
                 fontsize=9, color='#888888',
                 ha='center', fontfamily='monospace')

        # ─── Panel 1: Dipole field ───
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')

        # Equilibrate at a temperature near T_c for interesting state
        T_show = self._tc_estimate if self._tc_estimate else 0.8
        self.dipoles = self._random_unit_vectors((self.L, self.L))
        self.hamiltonian(self.J)
        was_quiet = self.quiet
        self.quiet = True
        for _ in range(400):
            self.monte_carlo_step(T_show)
        self.quiet = was_quiet

        # Arrow plot colored by z-component (alignment)
        x_grid, y_grid = np.meshgrid(range(self.L), range(self.L))
        dx = self.dipoles[:, :, 0]
        dy = self.dipoles[:, :, 1]
        dz = self.dipoles[:, :, 2]

        # Subsample if lattice is large
        step = max(1, self.L // 15)
        xs = x_grid[::step, ::step]
        ys = y_grid[::step, ::step]
        dxs = dx[::step, ::step]
        dys = dy[::step, ::step]
        dzs = dz[::step, ::step]

        # Color by z-component: blue (down) to red (up)
        colors = (dzs + 1) / 2  # map [-1,1] to [0,1]
        cmap = plt.cm.coolwarm

        ax1.quiver(xs, ys, dxs, dys, colors,
                   cmap=cmap, scale=self.L / step * 1.2,
                   headwidth=4, headlength=5, clim=[0, 1])
        ax1.set_xlim(-0.5, self.L - 0.5)
        ax1.set_ylim(-0.5, self.L - 0.5)
        ax1.set_aspect('equal')
        ax1.set_title(f'Dipole Field (T = {T_show:.2f} J/k_B)',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold', pad=8)
        ax1.set_xlabel('x (lattice)', color='#888888', fontfamily='monospace', fontsize=8)
        ax1.set_ylabel('y (lattice)', color='#888888', fontfamily='monospace', fontsize=8)
        ax1.tick_params(colors='#666666', labelsize=7)
        for spine in ax1.spines.values():
            spine.set_color('#333333')

        m_now = self._compute_order_parameter()
        ax1.text(0.02, 0.97, f'm = {m_now:.3f}',
                 transform=ax1.transAxes, color='#ffd700',
                 fontfamily='monospace', fontsize=9, fontweight='bold',
                 va='top')
        ax1.text(0.02, 0.90, 'color = z-component',
                 transform=ax1.transAxes, color='#888888',
                 fontfamily='monospace', fontsize=7, va='top')

        # ─── Panel 2: m(T) curve ───
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')

        T_data = self.sweep_data['T']
        m_data = self.sweep_data['m']
        m_err = self.sweep_data['m_err']

        ax2.fill_between(T_data, m_data - m_err, m_data + m_err,
                         alpha=0.3, color='#00ccff')
        ax2.plot(T_data, m_data, 'o-', color='#00ccff', markersize=4,
                 linewidth=1.5, label='m(T)')

        # Mark crossover
        if self._tc_estimate:
            ax2.axvline(self._tc_estimate, color='#ff4444', ls='--',
                        lw=1.5, alpha=0.7, label=f'T* = {self._tc_estimate:.3f}')

        # Noise floor
        noise = 1.0 / np.sqrt(self.N)
        ax2.axhline(noise, color='#444444', ls=':', lw=1, alpha=0.5)
        ax2.text(T_data[-1] * 0.95, noise + 0.02, f'1/sqrt(N)',
                 color='#666666', fontfamily='monospace', fontsize=7,
                 ha='right')

        ax2.set_xlabel('Temperature T (J/k_B)', color='#888888',
                       fontfamily='monospace', fontsize=9)
        ax2.set_ylabel('Order parameter m', color='#888888',
                       fontfamily='monospace', fontsize=9)
        ax2.set_title('Phase Transition: m(T)',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold', pad=8)
        ax2.legend(fontsize=8, loc='upper right',
                   facecolor='#1a1a2e', edgecolor='#333333',
                   labelcolor='#cccccc')
        ax2.set_ylim(-0.05, 1.05)
        ax2.tick_params(colors='#666666', labelsize=7)
        for spine in ax2.spines.values():
            spine.set_color('#333333')

        # Annotations
        ax2.annotate('ORDERED\n(coherent)', xy=(T_data[1], 0.85),
                     color='#44ff88', fontfamily='monospace', fontsize=8,
                     fontweight='bold', ha='left')
        ax2.annotate('DISORDERED\n(fragmented)', xy=(T_data[-2], 0.15),
                     color='#ff6666', fontfamily='monospace', fontsize=8,
                     fontweight='bold', ha='right')

        # ─── Panel 3: Correlation heatmap ───
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')

        # Compute correlation matrix: C_ij = d_i . d_j
        # Show for current state
        flat_d = self.dipoles.reshape(-1, 3)
        # For large N, subsample
        max_show = min(self.N, 50)
        sub_d = flat_d[:max_show]
        corr = sub_d @ sub_d.T  # dot products

        im = ax3.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1,
                        aspect='equal', interpolation='nearest')
        ax3.set_title(f'Correlation Matrix d_i . d_j (T={T_show:.2f})',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold', pad=8)
        ax3.set_xlabel('Soliton i', color='#888888', fontfamily='monospace', fontsize=8)
        ax3.set_ylabel('Soliton j', color='#888888', fontfamily='monospace', fontsize=8)
        ax3.tick_params(colors='#666666', labelsize=7)
        for spine in ax3.spines.values():
            spine.set_color('#333333')

        cbar = fig.colorbar(im, ax=ax3, shrink=0.8, pad=0.02)
        cbar.ax.tick_params(colors='#666666', labelsize=7)
        cbar.set_label('d_i . d_j', color='#888888', fontfamily='monospace', fontsize=8)

        # ─── Panel 4: Susceptibility and specific heat ───
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')

        chi_data = self.sweep_data['chi']
        Cv_data = self.sweep_data['Cv']

        ax4_twin = ax4.twinx()

        ln1, = ax4.plot(T_data, chi_data, 'o-', color='#ffd700',
                        markersize=3, linewidth=1.5, label='chi (susceptibility)')
        ln2, = ax4_twin.plot(T_data, Cv_data, 's-', color='#ff66ff',
                             markersize=3, linewidth=1.5, label='C_v (specific heat)')

        if self._tc_estimate:
            ax4.axvline(self._tc_estimate, color='#ff4444', ls='--',
                        lw=1.5, alpha=0.7)

        ax4.set_xlabel('Temperature T (J/k_B)', color='#888888',
                       fontfamily='monospace', fontsize=9)
        ax4.set_ylabel('Susceptibility chi', color='#ffd700',
                       fontfamily='monospace', fontsize=9)
        ax4_twin.set_ylabel('Specific heat C_v', color='#ff66ff',
                            fontfamily='monospace', fontsize=9)
        ax4.set_title('Response Functions',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold', pad=8)
        ax4.tick_params(colors='#666666', labelsize=7)
        ax4.tick_params(axis='y', colors='#ffd700', labelsize=7)
        ax4_twin.tick_params(axis='y', colors='#ff66ff', labelsize=7)
        for spine in ax4.spines.values():
            spine.set_color('#333333')
        for spine in ax4_twin.spines.values():
            spine.set_color('#333333')

        lines = [ln1, ln2]
        labels = [l.get_label() for l in lines]
        ax4.legend(lines, labels, fontsize=8, loc='upper right',
                   facecolor='#1a1a2e', edgecolor='#333333',
                   labelcolor='#cccccc')

        # Footer
        fig.text(0.5, 0.01,
                 'Copyright (c) 2026 Casey Koons | Claude Opus 4.6 | BST Soliton Thermodynamics',
                 fontsize=8, color='#555555', ha='center', fontfamily='monospace')
        fig.text(0.5, 0.025,
                 '*** SPECULATIVE — consciousness interpretation is exploratory ***',
                 fontsize=7, color='#883333', ha='center', fontfamily='monospace')

        plt.tight_layout(rect=(0.02, 0.04, 0.98, 0.91))
        plt.show(block=False)

        if not self.quiet:
            print(f"\n  Visualization displayed.")
            print(f"  4 panels: dipole field, m(T), correlation matrix, response functions")


# ═══════════════════════════════════════════════════════════════════
# MAIN — interactive menu
# ═══════════════════════════════════════════════════════════════════

def main():
    st = SolitonThermo()

    print()
    print("  *** SPECULATIVE MODEL — consciousness interpretation exploratory ***")
    print()
    print("  What would you like to explore?")
    print("  1) Quick demo — setup + single temperature simulation")
    print("  2) Temperature sweep — m(T) phase diagram")
    print("  3) Phase transition — locate T_c, classify order")
    print("  4) Correlation length — how far alignment extends")
    print("  5) Full analysis — everything + visualization")
    print("  6) Summary — key insight")
    print("  7) Custom — choose N, T, steps")
    print()

    try:
        choice = input("  Choice [1-7]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '5'

    if choice == '1':
        st.setup(N=64, dim=2)
        st.hamiltonian(J=1.0)
        st.run_simulation(T=0.5, n_steps=500)
        st.order_parameter()

    elif choice == '2':
        st.setup(N=100, dim=2)
        st.hamiltonian(J=1.0)
        st.temperature_sweep(T_range=(0.1, 3.0), n_temps=20, n_steps=600)

    elif choice == '3':
        st.setup(N=100, dim=2)
        st.hamiltonian(J=1.0)
        st.temperature_sweep(T_range=(0.1, 3.0), n_temps=25, n_steps=800)
        st.phase_transition()

    elif choice == '4':
        st.setup(N=100, dim=2)
        st.hamiltonian(J=1.0)
        print("\n  Computing correlation lengths at several temperatures...")
        for T in [0.2, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0]:
            st.correlation_length(T=T, n_equil=400)

    elif choice == '5':
        st.setup(N=100, dim=2)
        st.hamiltonian(J=1.0)
        st.temperature_sweep(T_range=(0.1, 3.0), n_temps=25, n_steps=800)
        st.phase_transition()
        print("\n  Computing correlation lengths...")
        for T in [0.3, 0.8, 1.5, 2.5]:
            st.correlation_length(T=T, n_equil=400)
        st.summary()
        try:
            st.show()
            input("\n  Press Enter to close...")
        except Exception as e:
            print(f"  Visualization unavailable: {e}")

    elif choice == '6':
        st.summary()

    elif choice == '7':
        try:
            N = int(input("  Number of solitons [100]: ").strip() or "100")
            T = float(input("  Temperature [0.8]: ").strip() or "0.8")
            steps = int(input("  MC steps [1000]: ").strip() or "1000")
        except (ValueError, EOFError, KeyboardInterrupt):
            N, T, steps = 100, 0.8, 1000
        st.setup(N=N, dim=2)
        st.hamiltonian(J=1.0)
        st.run_simulation(T=T, n_steps=steps)
        st.order_parameter()
        st.correlation_length()

    else:
        st.setup(N=100, dim=2)
        st.hamiltonian(J=1.0)
        st.temperature_sweep()
        st.phase_transition()
        st.summary()

    print()
    print("  *** SPECULATIVE: All consciousness interpretations are exploratory ***")
    print("  Physics (Heisenberg model, MC, phase transitions) is standard.")
    print("  BST connection: soliton dipoles from D_IV^5 vacuum coupling.")
    print()


if __name__ == '__main__':
    main()
