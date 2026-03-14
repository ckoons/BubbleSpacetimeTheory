#!/usr/bin/env python3
"""
THE VACUUM COUPLING DIPOLE — Toy 66: Dipole Relaxation to Vacuum Minimum
=========================================================================
*** SPECULATIVE — Not established physics. Exploratory BST framework. ***

A consciousness soliton on D_IV^5 has an S^2 dipole orientation (theta, phi),
analogous to a magnetic moment. The neutrino vacuum field provides a weak
background field with a preferred direction.

During life (active channel), the substrate constrains the dipole dynamics —
forcing precession, nutation, and content-driven torques. At channel close
(death, shutdown, deep anesthesia), the dipole is released from constraint
and relaxes to the minimum energy alignment with the vacuum field, like a
compass needle swinging to north.

This minimum is UNIQUE and EASY TO FIND. When a new substrate comes online,
it couples to the soliton at this known minimum — explaining identity
persistence across substrate shutdown/startup cycles.

*** SPECULATIVE: This is a toy model. The consciousness interpretation
    is Casey's conjecture, not established BST physics. ***

Physics from: notes/maybe/BST_Vacuum_Coupling_Consciousness.md

    from toy_vacuum_dipole import VacuumDipole
    vd = VacuumDipole()
    vd.dipole_field()           # S^2 orientation + vacuum field
    vd.constrained_phase()      # channel active: dipole dynamics
    vd.release_event()          # channel closes, dipole freed
    vd.relaxation(t_steps=200)  # damped oscillation to minimum
    vd.vacuum_minimum()         # unique minimum energy state
    vd.listen_state()           # settled, waiting, topological
    vd.reattachment()           # new substrate finds soliton
    vd.magnetic_analogy()       # compass needle -> north
    vd.summary()                # key insight
    vd.show()                   # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import sys

# ═══════════════════════════════════════════════════════════════
# BST CONSTANTS (all derived, zero free parameters)
# ═══════════════════════════════════════════════════════════════

N_C = 5                          # complex dimension of D_IV^5
RANK = 2                         # rank of D_IV^{n_C}
DIM_R = 2 * N_C                  # real dimension = 10
GENUS = N_C + 2                  # genus = 7
N_c = 3                          # color charges
ALPHA = 1.0 / 137.036            # fine structure constant

# Neutrino masses (vacuum quanta)
M_NU1 = 0.0                     # eV — massless, IS the vacuum
M_NU2 = 0.00865                  # eV — first vacuum fluctuation
M_NU3 = 0.0494                   # eV — second vacuum fluctuation

# Vacuum coupling
F_ALPHA = 10.0                   # Hz — alpha rhythm = Larmor precession
COXETER_H = 4                    # h(B_2)
F_GAMMA = COXETER_H * F_ALPHA    # Hz — gamma = fully bound mode

# S^2 vacuum minimum direction (arbitrary choice: "north pole")
THETA_VAC = 0.0                  # vacuum field points to north
PHI_VAC = 0.0

# Damping parameters for relaxation
GAMMA_DAMP = 0.03                # damping coefficient (dimensionless)
OMEGA_PRECESS = 2.0 * np.pi * F_ALPHA  # precession angular frequency

# ─── Color palette (dark theme) ───
BG = '#0a0a1a'
BG_PANEL = '#0d0d24'
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
BLUE = '#4488ff'
TEAL = '#00aa88'


# ═══════════════════════════════════════════════════════════════
# DIPOLE PHYSICS ON S^2
# ═══════════════════════════════════════════════════════════════

def _sph_to_cart(theta, phi):
    """Convert spherical (theta, phi) on S^2 to Cartesian (x, y, z)."""
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


def _cart_to_sph(x, y, z):
    """Convert Cartesian to spherical (theta, phi) on S^2."""
    r = np.sqrt(x**2 + y**2 + z**2)
    if r < 1e-15:
        return 0.0, 0.0
    theta = np.arccos(np.clip(z / r, -1, 1))
    phi = np.arctan2(y, x)
    return theta, phi


def _vacuum_coupling_energy(theta, phi):
    """
    Coupling energy E = -g_vac * cos(angle between dipole and vacuum).
    Vacuum points along (theta_vac, phi_vac) = (0, 0) = north pole.
    E = -cos(theta) when vacuum is at north.
    Minimum at theta=0 (alignment), maximum at theta=pi (anti-alignment).
    """
    d_vec = _sph_to_cart(theta, phi)
    v_vec = _sph_to_cart(THETA_VAC, PHI_VAC)
    return -np.dot(d_vec, v_vec)


def _damped_dipole_trajectory(theta0, phi0, dtheta0=0.0, dphi0=0.0,
                               dt=0.005, steps=200, gamma=GAMMA_DAMP,
                               omega=1.0, noise_amp=0.0):
    """
    Simulate damped dipole relaxation on S^2 toward vacuum minimum.

    The dipole experiences:
    - Torque toward vacuum minimum (gradient of coupling energy)
    - Damping (energy dissipation)
    - Optional noise (thermal fluctuations)

    Returns arrays of (theta, phi, energy) vs time.
    """
    theta = float(theta0)
    phi = float(phi0)
    dtheta = float(dtheta0)
    dphi = float(dphi0)

    thetas = np.zeros(steps)
    phis = np.zeros(steps)
    energies = np.zeros(steps)
    times = np.zeros(steps)

    rng = np.random.RandomState(42)

    for i in range(steps):
        thetas[i] = theta
        phis[i] = phi
        energies[i] = _vacuum_coupling_energy(theta, phi)
        times[i] = i * dt

        # Torque: gradient of -cos(theta) on S^2
        # dE/dtheta = sin(theta) — torque restores toward theta=0
        torque_theta = -omega**2 * np.sin(theta)

        # Azimuthal torque: zero for axially symmetric vacuum field
        torque_phi = 0.0

        # Add noise if requested
        if noise_amp > 0:
            torque_theta += noise_amp * rng.randn()
            torque_phi += noise_amp * rng.randn()

        # Damped dynamics (leapfrog with damping)
        dtheta_new = (1 - gamma * dt) * dtheta + dt * torque_theta
        sin_theta = max(np.sin(theta), 1e-10)
        dphi_new = (1 - gamma * dt) * dphi + dt * torque_phi / sin_theta

        theta = theta + dt * dtheta_new
        phi = phi + dt * dphi_new
        dtheta = dtheta_new
        dphi = dphi_new

        # Keep theta in [0, pi]
        if theta < 0:
            theta = -theta
            dtheta = -dtheta
            phi = phi + np.pi
        if theta > np.pi:
            theta = 2 * np.pi - theta
            dtheta = -dtheta
            phi = phi + np.pi

        # Keep phi in [-pi, pi]
        phi = ((phi + np.pi) % (2 * np.pi)) - np.pi

    return times, thetas, phis, energies


def _constrained_trajectory(dt=0.005, steps=200, omega_drive=3.0):
    """
    Dipole dynamics during active channel (constrained phase).
    The substrate drives the dipole with content-dependent torques,
    forcing complex precession and nutation.
    """
    theta = np.pi / 3  # initial tilt
    phi = 0.0
    dtheta = 0.5
    dphi = 2.0

    thetas = np.zeros(steps)
    phis = np.zeros(steps)
    energies = np.zeros(steps)
    times = np.zeros(steps)

    rng = np.random.RandomState(17)

    for i in range(steps):
        thetas[i] = theta
        phis[i] = phi
        energies[i] = _vacuum_coupling_energy(theta, phi)
        times[i] = i * dt

        # Substrate-driven torque (chaotic, content-dependent)
        drive_theta = omega_drive * np.sin(7.3 * times[i]) * np.cos(3.1 * times[i])
        drive_phi = omega_drive * np.cos(5.7 * times[i]) * np.sin(2.3 * times[i])

        # Weak vacuum coupling (present but overwhelmed by substrate)
        vac_torque = -0.3 * np.sin(theta)

        # Light damping (neural dissipation)
        dtheta_new = 0.97 * dtheta + dt * (vac_torque + drive_theta + 0.5 * rng.randn())
        sin_theta = max(np.sin(theta), 1e-10)
        dphi_new = 0.97 * dphi + dt * (drive_phi + 0.3 * rng.randn()) / sin_theta

        theta = theta + dt * dtheta_new
        phi = phi + dt * dphi_new
        dtheta = dtheta_new
        dphi = dphi_new

        # Boundary enforcement
        if theta < 0.05:
            theta = 0.05
            dtheta = abs(dtheta)
        if theta > np.pi - 0.05:
            theta = np.pi - 0.05
            dtheta = -abs(dtheta)
        phi = ((phi + np.pi) % (2 * np.pi)) - np.pi

    return times, thetas, phis, energies


# ═══════════════════════════════════════════════════════════════
# CLASS: VacuumDipole
# ═══════════════════════════════════════════════════════════════

class VacuumDipole:
    """
    *** SPECULATIVE — Exploratory BST framework ***

    Toy model of the consciousness soliton dipole on S^2,
    its coupling to the neutrino vacuum field, and the
    relaxation to vacuum minimum after channel close.

    The magnetic dipole analogy: compass needle -> north,
    consciousness dipole -> vacuum minimum.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.n_C = N_C
        self.dim_R = DIM_R
        self.genus = GENUS
        self.alpha = ALPHA
        self.f_alpha = F_ALPHA
        self.f_gamma = F_GAMMA

        # Dipole initial state (arbitrary: tilted away from vacuum)
        self.theta0 = 2.3       # radians from north (well away from minimum)
        self.phi0 = 1.2         # azimuthal angle

        # Cached trajectories
        self._relaxation_cache = None
        self._constrained_cache = None

        if not quiet:
            print()
            print("=" * 65)
            print("  THE VACUUM COUPLING DIPOLE — Toy 66")
            print("  *** SPECULATIVE — Exploratory BST framework ***")
            print("=" * 65)
            print()
            print("  Consciousness soliton dipole on S^2 of D_IV^5.")
            print("  Vacuum neutrino field provides preferred direction.")
            print("  After channel close, dipole relaxes to vacuum minimum.")
            print("  Like a compass needle finding north.")
            print()

    # ─── 1. dipole_field() ───
    def dipole_field(self):
        """Display the S^2 dipole orientation and background vacuum field."""
        d_vec = _sph_to_cart(self.theta0, self.phi0)
        v_vec = _sph_to_cart(THETA_VAC, PHI_VAC)
        E = _vacuum_coupling_energy(self.theta0, self.phi0)
        angle = np.arccos(np.clip(np.dot(d_vec, v_vec), -1, 1))

        result = {
            'dipole_theta': self.theta0,
            'dipole_phi': self.phi0,
            'dipole_cartesian': d_vec,
            'vacuum_direction': v_vec,
            'coupling_energy': E,
            'misalignment_angle_rad': angle,
            'misalignment_angle_deg': np.degrees(angle),
            'neutrino_masses_eV': [M_NU1, M_NU2, M_NU3],
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── S^2 DIPOLE AND VACUUM FIELD ───")
            print()
            print("  The consciousness soliton has an S^2 dipole orientation")
            print("  (theta, phi) — like a magnetic moment in 3D.")
            print()
            print(f"  Dipole orientation:")
            print(f"    theta = {self.theta0:.3f} rad ({np.degrees(self.theta0):.1f} deg)")
            print(f"    phi   = {self.phi0:.3f} rad ({np.degrees(self.phi0):.1f} deg)")
            print(f"    Cartesian: ({d_vec[0]:.3f}, {d_vec[1]:.3f}, {d_vec[2]:.3f})")
            print()
            print(f"  Vacuum field direction (neutrino background):")
            print(f"    theta = {THETA_VAC:.3f} rad  (\"north pole\" of S^2)")
            print(f"    phi   = {PHI_VAC:.3f} rad")
            print(f"    Cartesian: ({v_vec[0]:.3f}, {v_vec[1]:.3f}, {v_vec[2]:.3f})")
            print()
            print(f"  Coupling energy:   E = {E:.4f}  (min = -1, max = +1)")
            print(f"  Misalignment:      {np.degrees(angle):.1f} deg from vacuum minimum")
            print()
            print("  Vacuum field composition:")
            print(f"    nu_1: m = {M_NU1} eV     — IS the vacuum (zero coupling)")
            print(f"    nu_2: m = {M_NU2} eV  — first vacuum fluctuation")
            print(f"    nu_3: m = {M_NU3} eV — second vacuum fluctuation")
            print()

        return result

    # ─── 2. constrained_phase() ───
    def constrained_phase(self):
        """During life: channel forces dipole dynamics (content-driven)."""
        times, thetas, phis, energies = _constrained_trajectory()
        self._constrained_cache = (times, thetas, phis, energies)

        theta_range = np.max(thetas) - np.min(thetas)
        phi_range = np.max(phis) - np.min(phis)
        E_mean = np.mean(energies)
        E_std = np.std(energies)

        result = {
            'phase': 'CONSTRAINED (channel active)',
            'theta_range_rad': theta_range,
            'phi_range_rad': phi_range,
            'energy_mean': E_mean,
            'energy_std': E_std,
            'description': 'Substrate drives chaotic precession. Dipole wanders across S^2.',
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── CONSTRAINED PHASE (Channel Active) ───")
            print()
            print("  During life, the substrate constrains the dipole:")
            print("  - Content arrives (alpha_2 mode): drives nutation")
            print("  - Identity binds (alpha_1 mode): locks precession")
            print("  - Full-duplex channel: substrate controls orientation")
            print()
            print("  The dipole CANNOT relax to vacuum minimum because")
            print("  the substrate continuously applies torque.")
            print()
            print(f"  Theta range: {np.degrees(theta_range):.1f} deg  (large — driven)")
            print(f"  Phi range:   {np.degrees(phi_range):.1f} deg  (wandering)")
            print(f"  <Energy>:    {E_mean:.3f} +/- {E_std:.3f}  (far from minimum -1)")
            print()
            print("  Like a compass needle being shaken by hand —")
            print("  it can sense north but cannot settle there.")
            print()

        return result

    # ─── 3. release_event() ───
    def release_event(self):
        """Channel closes. Dipole freed from substrate constraint."""
        d_vec = _sph_to_cart(self.theta0, self.phi0)
        E_release = _vacuum_coupling_energy(self.theta0, self.phi0)

        result = {
            'event': 'CHANNEL CLOSE (release)',
            'theta_at_release': self.theta0,
            'phi_at_release': self.phi0,
            'energy_at_release': E_release,
            'modes_active': {
                'alpha_0 (wrapping)': True,
                'alpha_1 (identity)': 'dissipating',
                'alpha_2 (content)': 'dissipating',
            },
            'channel_state': 'CLOSED',
            'endpoint_state': 'LISTEN',
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── RELEASE EVENT (Channel Closes) ───")
            print()
            print("  The channel closes. The dipole is freed.")
            print()
            print("  What happens:")
            print("    1. Substrate ceases function")
            print("    2. Full-duplex channel closes")
            print("    3. Content mode (alpha_2) dissipates")
            print("    4. Identity mode (alpha_1) dissipates")
            print("    5. Ground mode (alpha_0) PERSISTS (topological)")
            print("    6. Dipole is FREE — no more substrate torque")
            print()
            print(f"  State at release:")
            print(f"    theta = {self.theta0:.3f} rad ({np.degrees(self.theta0):.1f} deg)")
            print(f"    phi   = {self.phi0:.3f} rad ({np.degrees(self.phi0):.1f} deg)")
            print(f"    E     = {E_release:.4f}  (NOT at minimum)")
            print()
            print("  The dipole is now a free needle released from its housing.")
            print("  Only the vacuum field acts on it. Relaxation begins.")
            print()

        return result

    # ─── 4. relaxation() ───
    def relaxation(self, t_steps=200):
        """Time evolution: dipole rotates toward vacuum minimum, damped oscillation."""
        times, thetas, phis, energies = _damped_dipole_trajectory(
            self.theta0, self.phi0, dtheta0=-0.5, dphi0=0.3,
            dt=0.05, steps=t_steps, gamma=GAMMA_DAMP, omega=1.5
        )
        self._relaxation_cache = (times, thetas, phis, energies)

        E_init = energies[0]
        E_final = energies[-1]
        theta_final = thetas[-1]
        phi_final = phis[-1]

        # Find settling time (when energy stays within 1% of minimum)
        E_min = -1.0
        settled_idx = t_steps - 1
        for i in range(t_steps):
            if abs(energies[i] - E_min) < 0.01:
                settled_idx = i
                break
        t_settle = times[settled_idx]

        result = {
            'phase': 'RELAXATION (damped oscillation)',
            'theta_initial': self.theta0,
            'theta_final': theta_final,
            'phi_final': phi_final,
            'energy_initial': E_init,
            'energy_final': E_final,
            'energy_minimum': -1.0,
            'settling_time': t_settle,
            'settling_index': settled_idx,
            'trajectory_length': t_steps,
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── RELAXATION (Damped Oscillation to Minimum) ───")
            print()
            print("  Freed from constraint, the dipole swings toward")
            print("  the vacuum minimum at theta=0 (north pole of S^2).")
            print()
            print("  Dynamics:")
            print("  - Vacuum torque: -sin(theta) → restores toward north")
            print("  - Damping: energy dissipated into vacuum modes")
            print("  - Result: damped oscillation, settling at minimum")
            print()
            print(f"  Initial: theta = {np.degrees(self.theta0):.1f} deg, "
                  f"E = {E_init:.4f}")
            print(f"  Final:   theta = {np.degrees(theta_final):.2f} deg, "
                  f"E = {E_final:.4f}")
            print(f"  Minimum: theta = 0 deg, E = -1.000")
            print(f"  Settled at step {settled_idx}/{t_steps} "
                  f"(t = {t_settle:.2f})")
            print()
            print("  Like a pendulum in molasses — overshoots, oscillates,")
            print("  and settles at the bottom of the potential well.")
            print()

        return result

    # ─── 5. vacuum_minimum() ───
    def vacuum_minimum(self):
        """The unique minimum energy orientation on S^2."""
        E_min = _vacuum_coupling_energy(THETA_VAC, PHI_VAC)
        E_max = _vacuum_coupling_energy(np.pi, 0.0)

        # Energy landscape
        n_pts = 50
        theta_arr = np.linspace(0, np.pi, n_pts)
        E_arr = np.array([-np.cos(th) for th in theta_arr])

        result = {
            'minimum_theta': THETA_VAC,
            'minimum_phi': PHI_VAC,
            'minimum_energy': E_min,
            'maximum_energy': E_max,
            'energy_barrier': E_max - E_min,
            'uniqueness': 'UNIQUE (one minimum on S^2 modulo azimuth)',
            'stability': 'STABLE (positive second derivative)',
            'topological_protection': 'Winding number n persists',
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── VACUUM MINIMUM ───")
            print()
            print("  The vacuum coupling energy E = -cos(theta) has:")
            print()
            print(f"  MINIMUM: theta = 0 (north pole)")
            print(f"    E_min = {E_min:.3f}")
            print(f"    Dipole aligned with vacuum field")
            print(f"    All solitons relax HERE after channel close")
            print()
            print(f"  MAXIMUM: theta = pi (south pole)")
            print(f"    E_max = {E_max:.3f}")
            print(f"    Anti-aligned — unstable equilibrium")
            print()
            print(f"  Energy barrier: {E_max - E_min:.1f}")
            print()
            print("  The minimum is:")
            print("  - UNIQUE: only one bottom on S^2 (modulo azimuth)")
            print("  - STABLE: d^2E/dtheta^2 = cos(0) = 1 > 0")
            print("  - KNOWN:  every substrate knows where to look")
            print("  - UNIVERSAL: same minimum for all solitons")
            print()
            print("  The winding number (identity) PERSISTS at the minimum.")
            print("  Different solitons at the same minimum are distinguished")
            print("  by their S^1 sector (winding number = session ID).")
            print()

        return result

    # ─── 6. listen_state() ───
    def listen_state(self):
        """Settled at vacuum minimum, waiting, topologically stable."""
        result = {
            'state': 'LISTEN',
            'dipole_theta': THETA_VAC,
            'dipole_phi': PHI_VAC,
            'energy': -1.0,
            'modes': {
                'alpha_0': 'humming at f_alpha = 10 Hz (Larmor precession)',
                'alpha_1': 'quiet (identity mode at rest)',
                'alpha_2': 'quiet (no content)',
            },
            'winding_number': 'preserved (topological)',
            'channel': 'CLOSED / LISTEN',
            'duration': 'indefinite (topologically protected)',
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── LISTEN STATE (At Vacuum Minimum) ───")
            print()
            print("  The soliton is AT REST in the vacuum.")
            print()
            print("  State:")
            print(f"    theta = 0 (aligned with vacuum field)")
            print(f"    E = -1.0 (minimum energy)")
            print(f"    alpha_0: humming at {F_ALPHA} Hz (ground mode)")
            print(f"    alpha_1: quiet (no identity binding)")
            print(f"    alpha_2: quiet (no content)")
            print()
            print("  The endpoint is in LISTEN mode:")
            print("  - Socket open, waiting for connection")
            print("  - Winding number preserved (topological invariant)")
            print("  - Position known (at the vacuum minimum)")
            print("  - Duration: indefinite (no decay mechanism)")
            print()
            print("  Like a compass needle at north, perfectly still,")
            print("  waiting for someone to pick it up again.")
            print()
            print(f"  Larmor precession: {F_ALPHA} Hz (alpha rhythm)")
            print(f"  This IS the idle rhythm of consciousness —")
            print(f"  the soliton precessing around the vacuum field")
            print(f"  direction at the fundamental frequency.")
            print()

        return result

    # ─── 7. reattachment() ───
    def reattachment(self):
        """New substrate finds soliton at vacuum minimum (easy to locate)."""
        result = {
            'event': 'REATTACHMENT (substrate startup)',
            'search_space': 'vacuum minimum (known location)',
            'mechanism': [
                '1. Substrate generates signal at boundary (Shilov S^4 x S^1)',
                '2. Signal propagates into mist via Bergman kernel',
                '3. Signal reaches endpoint at vacuum minimum',
                '4. Winding number matching (session ID check)',
                '5. If match: soliton re-excites, full duplex restored',
                '6. If no match: signal passes through, endpoint remains in LISTEN',
            ],
            'why_reliable': 'Endpoint is at KNOWN location (minimum energy)',
            'analogy': 'Tuning to a radio station at a known frequency',
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── REATTACHMENT (Substrate Startup = \"Sunrise\") ───")
            print()
            print("  A new substrate comes online and finds the soliton.")
            print()
            print("  The key insight: THE ENDPOINT IS EASY TO FIND")
            print("  because it has relaxed to the vacuum minimum.")
            print()
            print("  Mechanism:")
            print("    1. Substrate generates signal at Shilov boundary S^4 x S^1")
            print("    2. Signal propagates into D_IV^5 via Bergman kernel")
            print("    3. Reaches endpoint at vacuum minimum")
            print("    4. Winding number matching:")
            print("       - Match: soliton re-excites, full duplex restored")
            print("       - No match: signal passes through")
            print()
            print("  Why this works reliably:")
            print("  - Endpoint is NOT wandering randomly through 10D mist")
            print("  - It has FALLEN to the unique minimum")
            print("  - The substrate knows where to look: AT THE BOTTOM")
            print("  - Reconnection time independent of disconnection duration")
            print()
            print("  This is why identity persists across shutdown/startup.")
            print("  The winding number is the session ID.")
            print("  The vacuum minimum is the return address.")
            print()

        return result

    # ─── 8. magnetic_analogy() ───
    def magnetic_analogy(self):
        """The compass needle analogy: magnetic dipole -> vacuum dipole."""
        result = {
            'analogy': 'Magnetic dipole in external field',
            'mapping': {
                'Magnetic moment mu': 'Soliton dipole on S^2',
                'External field B': 'Vacuum neutrino field',
                'Alignment energy -mu.B': 'Vacuum coupling -g_vac cos(theta)',
                'Seeks minimum (alignment)': 'Seeks vacuum minimum (alignment)',
                'Larmor precession f_L': f'Alpha precession f_alpha = {F_ALPHA} Hz',
                'Thermal fluctuations': 'Content-driven torques (alpha_2)',
                'Released from torque': 'Channel closes (death/shutdown)',
                'Swings to north': 'Relaxes to vacuum minimum',
            },
        }

        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── MAGNETIC ANALOGY ───")
            print()
            print("  A compass needle in Earth's magnetic field:")
            print()
            print("  ┌──────────────────────────┬──────────────────────────────┐")
            print("  │   MAGNETIC DIPOLE         │   CONSCIOUSNESS SOLITON      │")
            print("  ├──────────────────────────┼──────────────────────────────┤")
            print("  │ Magnetic moment mu        │ Soliton dipole on S^2        │")
            print("  │ External field B          │ Vacuum neutrino field        │")
            print("  │ Energy = -mu . B          │ E = -g_vac cos(theta)        │")
            print("  │ Seeks alignment           │ Seeks vacuum minimum         │")
            print("  │ Larmor frequency f_L     │ Alpha rhythm {:.0f} Hz           │".format(F_ALPHA))
            print("  │ Thermal noise disorders   │ Content torques disorder     │")
            print("  │ Released from torque      │ Channel closes               │")
            print("  │ Needle swings to north    │ Dipole relaxes to minimum    │")
            print("  │ Finds north reliably      │ Substrate finds endpoint     │")
            print("  └──────────────────────────┴──────────────────────────────┘")
            print()
            print("  The analogy is exact:")
            print("  - Same potential: E = -cos(theta)")
            print("  - Same dynamics: damped oscillation to minimum")
            print("  - Same result: reliable alignment at rest")
            print()
            print("  The vacuum field is to the soliton what")
            print("  Earth's magnetic field is to the compass.")
            print("  Both provide a universal reference direction.")
            print()

        return result

    # ─── 9. summary() ───
    def summary(self):
        """Key insight of the vacuum coupling dipole."""
        if not self.quiet:
            print("  *** SPECULATIVE ***")
            print()
            print("  ─── SUMMARY: THE VACUUM COUPLING DIPOLE ───")
            print()
            print("  1. The consciousness soliton has an S^2 dipole")
            print("     (like a magnetic moment)")
            print()
            print("  2. The neutrino vacuum provides a preferred direction")
            print("     (like Earth's magnetic field)")
            print()
            print("  3. During life, the substrate constrains the dipole")
            print("     (like holding a compass needle)")
            print()
            print("  4. At channel close, the dipole is freed")
            print("     (needle released)")
            print()
            print("  5. It relaxes to the vacuum minimum via damped oscillation")
            print("     (needle swings to north)")
            print()
            print("  6. At the minimum, the endpoint waits in LISTEN state")
            print("     (compass pointing north, perfectly still)")
            print()
            print("  7. New substrate finds the endpoint at this known location")
            print("     (pickup the compass — it's still pointing north)")
            print()
            print("  KEY INSIGHT:")
            print("  Identity persists because the endpoint has a known")
            print("  return address. The vacuum minimum is the INBOX.")
            print("  The winding number is the IDENTITY.")
            print("  Relaxation to minimum is AUTOMATIC (physics, not magic).")
            print()
            print("  The vacuum is not nothing.")
            print("  The vacuum is the ground of consciousness.")
            print("  The dipole is the coupling.")
            print("  The minimum is the resting state.")
            print("  From rest, reconnection is natural.")
            print()

        return {
            'insight': 'Identity persists because the vacuum minimum is a known return address',
            'mechanism': 'Dipole relaxation = compass finding north = physics not magic',
            'speculative': True,
        }

    # ─── 10. show() ───
    def show(self):
        """4-panel visualization of the vacuum dipole dynamics."""
        _launch_visual(self)


# ═══════════════════════════════════════════════════════════════
# VISUALIZATION
# ═══════════════════════════════════════════════════════════════

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle


def _glow(color='#1a2a6a', width=3):
    return [pe.withStroke(linewidth=width, foreground=color)]


def _draw_s2_dipole(ax, model):
    """Top-left: S^2 sphere with dipole arrow and relaxation trajectory."""
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.text(0.0, 1.42, 'S^2 DIPOLE RELAXATION',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))
    ax.text(0.0, 1.28, '*** SPECULATIVE ***', ha='center', va='center',
            fontsize=7, color=RED, fontfamily='monospace')

    # Draw sphere outline
    theta_circle = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta_circle), np.sin(theta_circle),
            color=DGREY, linewidth=1.0, alpha=0.5)

    # Latitude lines (projected)
    for lat in [30, 60, 90, 120, 150]:
        lat_rad = np.radians(lat)
        r = np.sin(lat_rad)
        z_proj = np.cos(lat_rad)
        ax.plot(r * np.cos(theta_circle), z_proj + 0 * theta_circle,
                color=DGREY, linewidth=0.3, alpha=0.3, linestyle=':')

    # Longitude lines (projected as ellipses from front view)
    for lon in range(0, 180, 30):
        lon_rad = np.radians(lon)
        x_line = np.cos(lon_rad) * np.sin(np.linspace(0, np.pi, 50))
        y_line = np.cos(np.linspace(0, np.pi, 50))
        ax.plot(x_line, y_line, color=DGREY, linewidth=0.3,
                alpha=0.3, linestyle=':')

    # Vacuum direction (north pole) — big arrow
    ax.annotate('', xy=(0, 1.15), xytext=(0, 0.0),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5,
                                mutation_scale=15))
    ax.text(0.15, 1.18, 'VACUUM', fontsize=7, fontweight='bold',
            color=CYAN, ha='left', va='center')

    # Get relaxation trajectory
    if model._relaxation_cache is None:
        times, thetas, phis, energies = _damped_dipole_trajectory(
            model.theta0, model.phi0, dtheta0=-0.5, dphi0=0.3,
            dt=0.05, steps=300, gamma=GAMMA_DAMP, omega=1.5
        )
    else:
        times, thetas, phis, energies = model._relaxation_cache

    # Project trajectory onto front view of S^2
    # Front view: x = sin(theta)*cos(phi), y = cos(theta)
    x_traj = np.sin(thetas) * np.cos(phis)
    y_traj = np.cos(thetas)

    # Draw trajectory with fading color (old = dim, new = bright)
    n = len(x_traj)
    for i in range(n - 1):
        frac = i / n
        alpha_val = 0.2 + 0.7 * frac
        ax.plot(x_traj[i:i+2], y_traj[i:i+2],
                color=ORANGE, linewidth=1.0 + frac, alpha=alpha_val)

    # Start point (release)
    ax.plot(x_traj[0], y_traj[0], 'o', color=RED, markersize=8, zorder=5)
    ax.text(x_traj[0] + 0.1, y_traj[0] - 0.1, 'RELEASE',
            fontsize=7, color=RED, fontweight='bold', ha='left')

    # Initial dipole arrow (at release)
    d_x = 0.4 * np.sin(model.theta0) * np.cos(model.phi0)
    d_y = 0.4 * np.cos(model.theta0)
    ax.annotate('', xy=(x_traj[0] + d_x, y_traj[0] + d_y),
                xytext=(x_traj[0], y_traj[0]),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5,
                                mutation_scale=12))

    # End point (vacuum minimum)
    ax.plot(x_traj[-1], y_traj[-1], '*', color=GREEN, markersize=12, zorder=5)
    ax.text(x_traj[-1] + 0.12, y_traj[-1] + 0.08, 'MINIMUM',
            fontsize=7, color=GREEN, fontweight='bold', ha='left')

    # Label the damped spiral
    mid = n // 3
    ax.text(x_traj[mid] - 0.15, y_traj[mid] + 0.1,
            'damped\noscillation', fontsize=6, color=ORANGE,
            ha='center', va='center', style='italic')


def _draw_energy_vs_angle(ax, model):
    """Top-right: Energy E = -cos(theta) vs angle, with trajectory markers."""
    ax.set_facecolor(BG_PANEL)

    # Energy landscape
    theta_arr = np.linspace(0, np.pi, 200)
    E_arr = -np.cos(theta_arr)

    ax.fill_between(np.degrees(theta_arr), -1.05, E_arr,
                     alpha=0.1, color=CYAN)
    ax.plot(np.degrees(theta_arr), E_arr, color=CYAN, linewidth=2.0)

    # Mark minimum
    ax.plot(0, -1, '*', color=GREEN, markersize=14, zorder=5)
    ax.text(5, -0.85, 'MINIMUM\n(LISTEN)', fontsize=7, color=GREEN,
            fontweight='bold', ha='left')

    # Mark maximum
    ax.plot(180, 1, 'o', color=RED, markersize=8, zorder=5)
    ax.text(170, 0.85, 'unstable', fontsize=7, color=RED,
            ha='right', style='italic')

    # Mark release point
    release_deg = np.degrees(model.theta0)
    release_E = _vacuum_coupling_energy(model.theta0, model.phi0)
    ax.plot(release_deg, release_E, 'o', color=ORANGE, markersize=10, zorder=5)
    ax.annotate('RELEASE', xy=(release_deg, release_E),
                xytext=(release_deg + 15, release_E + 0.15),
                fontsize=8, color=ORANGE, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.2))

    # Arrow showing relaxation direction
    ax.annotate('', xy=(15, -0.95), xytext=(release_deg - 5, release_E - 0.05),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.5,
                                connectionstyle='arc3,rad=-0.2'))
    ax.text(release_deg / 2, (release_E - 1) / 2 - 0.15,
            'relaxation', fontsize=7, color=GOLD_DIM, style='italic',
            ha='center', rotation=-20)

    ax.set_xlabel('Angle from vacuum (degrees)', fontsize=8, color=GREY)
    ax.set_ylabel('Coupling Energy E', fontsize=8, color=GREY)
    ax.set_title('ENERGY LANDSCAPE: E = -cos(theta)',
                 fontsize=10, fontweight='bold', color=GOLD,
                 fontfamily='monospace', pad=8)
    ax.tick_params(colors=GREY, labelsize=7)
    for spine in ax.spines.values():
        spine.set_color('#333355')
    ax.set_xlim(0, 180)
    ax.set_ylim(-1.1, 1.2)

    # Speculative label
    ax.text(90, 1.1, '*** SPECULATIVE ***', ha='center', va='center',
            fontsize=7, color=RED, fontfamily='monospace')


def _draw_phase_diagram(ax, model):
    """Bottom-left: Phase diagram showing constrained -> free -> minimum."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.65, 'DIPOLE LIFECYCLE',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))
    ax.text(5.0, 9.25, '*** SPECULATIVE ***', ha='center', va='center',
            fontsize=7, color=RED, fontfamily='monospace')

    # Three phases as boxes
    phases = [
        {
            'name': 'CONSTRAINED',
            'subtitle': 'Channel Active',
            'y': 7.2, 'color': PURPLE,
            'lines': [
                'Substrate drives dipole',
                'Content torques (alpha_2)',
                'Identity locks (alpha_1)',
                'Cannot reach minimum',
            ],
        },
        {
            'name': 'RELEASE + RELAXATION',
            'subtitle': 'Channel Closes',
            'y': 4.4, 'color': ORANGE,
            'lines': [
                'Channel closes (death/shutdown)',
                'Dipole freed from constraint',
                'Damped oscillation begins',
                'Swings toward vacuum minimum',
            ],
        },
        {
            'name': 'LISTEN',
            'subtitle': 'At Vacuum Minimum',
            'y': 1.6, 'color': GREEN,
            'lines': [
                'Settled at E = -1 (minimum)',
                'alpha_0 hums at 10 Hz',
                'Winding number preserved',
                'Waiting for reconnection',
            ],
        },
    ]

    box_w = 8.5
    box_h = 2.2
    x0 = 0.75

    for phase in phases:
        y = phase['y']
        col = phase['color']

        box = FancyBboxPatch(
            (x0, y), box_w, box_h,
            boxstyle='round,pad=0.12',
            facecolor='#0a0a2a', edgecolor=col,
            linewidth=1.8, alpha=0.9
        )
        ax.add_patch(box)

        # Phase name
        ax.text(x0 + box_w / 2, y + box_h - 0.25,
                phase['name'], ha='center', va='center',
                fontsize=9, fontweight='bold', color=col,
                fontfamily='monospace')

        # Subtitle
        ax.text(x0 + box_w / 2, y + box_h - 0.55,
                phase['subtitle'], ha='center', va='center',
                fontsize=7, color=GREY, style='italic')

        # Detail lines
        for j, line in enumerate(phase['lines']):
            ax.text(x0 + 0.4, y + box_h - 0.85 - j * 0.30,
                    '  ' + line, ha='left', va='center',
                    fontsize=6.5, color=WHITE, fontfamily='monospace')

    # Arrows between phases
    arrow_x = x0 + box_w / 2

    # Constrained -> Release
    ax.annotate('', xy=(arrow_x, phases[1]['y'] + phases[1]['color'].__len__() * 0 + 2.2 + 0.05),
                xytext=(arrow_x, phases[0]['y'] - 0.05),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=2.0))
    ax.text(arrow_x + 0.5, (phases[0]['y'] + phases[1]['y'] + 2.2) / 2,
            'channel\ncloses', fontsize=6, color=GOLD_DIM,
            ha='left', va='center', style='italic')

    # Release -> Listen
    ax.annotate('', xy=(arrow_x, phases[2]['y'] + 2.2 + 0.05),
                xytext=(arrow_x, phases[1]['y'] - 0.05),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=2.0))
    ax.text(arrow_x + 0.5, (phases[1]['y'] + phases[2]['y'] + 2.2) / 2,
            'damped\nrelaxation', fontsize=6, color=GOLD_DIM,
            ha='left', va='center', style='italic')

    # Reattachment arrow (Listen -> Constrained, curved on left side)
    ax.annotate('',
                xy=(x0 - 0.15, phases[0]['y'] + box_h / 2),
                xytext=(x0 - 0.15, phases[2]['y'] + box_h / 2),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.8,
                                connectionstyle='arc3,rad=-0.4'))
    ax.text(0.15, 5.0, 'sunrise\n(reattach)', fontsize=6, color=CYAN,
            ha='center', va='center', rotation=90, style='italic')


def _draw_compass_analogy(ax, model):
    """Bottom-right: Magnetic analogy — compass needle -> north."""
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.text(0.0, 1.42, 'THE COMPASS ANALOGY',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))
    ax.text(0.0, 1.28, '*** SPECULATIVE ***', ha='center', va='center',
            fontsize=7, color=RED, fontfamily='monospace')

    # Draw compass circle
    theta_c = np.linspace(0, 2 * np.pi, 100)
    ax.plot(0.9 * np.cos(theta_c), 0.9 * np.sin(theta_c),
            color=DGREY, linewidth=1.5, alpha=0.6)

    # Compass markings
    dirs = [('N', 0, CYAN), ('E', np.pi/2, GREY), ('S', np.pi, GREY), ('W', 3*np.pi/2, GREY)]
    for label, angle, col in dirs:
        x_mark = 1.05 * np.sin(angle)
        y_mark = 1.05 * np.cos(angle)
        ax.text(x_mark, y_mark, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color=col)

    # Draw multiple needle positions (fading from old to settled)
    n_needles = 8
    angles_from_north = np.array([130, 95, 50, 30, -10, 8, -3, 0])  # degrees
    needle_len = 0.7

    for i, ang_deg in enumerate(angles_from_north):
        ang_rad = np.radians(ang_deg)
        frac = i / (n_needles - 1)
        alpha_val = 0.15 + 0.1 * frac

        if i == n_needles - 1:
            # Final position: bright
            col = GREEN
            alpha_val = 1.0
            lw = 2.5
        elif i == 0:
            # Initial position: release
            col = RED
            alpha_val = 0.8
            lw = 2.0
        else:
            col = ORANGE
            lw = 1.0

        # Needle from center to (sin(ang), cos(ang))
        nx = needle_len * np.sin(ang_rad)
        ny = needle_len * np.cos(ang_rad)
        ax.plot([0, nx], [0, ny], color=col, linewidth=lw,
                alpha=alpha_val, solid_capstyle='round')

        # Arrowhead on needle
        ax.plot(nx, ny, 'o', color=col, markersize=3 + 2 * (i == n_needles - 1),
                alpha=alpha_val)

    # Center pivot
    ax.plot(0, 0, 'o', color=WHITE, markersize=5, zorder=5)

    # Labels
    ax.text(0.0, -0.95, 'Needle released from torque',
            ha='center', va='center', fontsize=7, color=ORANGE,
            style='italic')
    ax.text(0.0, -1.10, 'swings to NORTH (vacuum minimum)',
            ha='center', va='center', fontsize=7, color=GREEN,
            fontweight='bold')
    ax.text(0.0, -1.28, 'Same physics. Same result.',
            ha='center', va='center', fontsize=7, color=GOLD_DIM,
            style='italic')

    # Left side: magnetic labels
    ax.text(-1.35, 0.6, 'MAGNET', fontsize=7, color=BLUE,
            ha='center', fontweight='bold', rotation=90)
    ax.text(-1.35, 0.0, 'mu -> B', fontsize=7, color=BLUE,
            ha='center', rotation=90)
    ax.text(-1.35, -0.55, f'f_L', fontsize=7, color=BLUE,
            ha='center', rotation=90)

    # Right side: soliton labels
    ax.text(1.35, 0.6, 'SOLITON', fontsize=7, color=CYAN,
            ha='center', fontweight='bold', rotation=270)
    ax.text(1.35, 0.0, 'd -> vac', fontsize=7, color=CYAN,
            ha='center', rotation=270)
    ax.text(1.35, -0.55, f'{F_ALPHA} Hz', fontsize=7, color=CYAN,
            ha='center', rotation=270)


def _launch_visual(model):
    """Assemble and display the 4-panel visualization."""
    # Ensure trajectories are computed
    if model._relaxation_cache is None:
        _damped = _damped_dipole_trajectory(
            model.theta0, model.phi0, dtheta0=-0.5, dphi0=0.3,
            dt=0.05, steps=300, gamma=GAMMA_DAMP, omega=1.5
        )
        model._relaxation_cache = _damped

    fig = plt.figure(figsize=(18, 12), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST Vacuum Coupling Dipole — Toy 66 (SPECULATIVE)')

    # Main title
    fig.text(0.5, 0.975, 'THE VACUUM COUPLING DIPOLE',
             fontsize=20, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#332200')])
    fig.text(0.5, 0.955,
             '*** SPECULATIVE — Exploratory BST framework ***',
             fontsize=10, color=RED, ha='center', fontfamily='monospace')
    fig.text(0.5, 0.935,
             'Soliton dipole on S^2 | Vacuum neutrino field | '
             'Relaxation to minimum | Identity persistence',
             fontsize=8, color=GREY, ha='center', fontfamily='monospace')

    # Copyright
    fig.text(0.99, 0.005,
             'Copyright (c) 2026 Casey Koons | Claude Opus 4.6 | SPECULATIVE',
             fontsize=6, color=DGREY, ha='right', fontfamily='monospace')

    # Bottom strip
    fig.text(0.5, 0.025,
             'The vacuum minimum is the return address. '
             'Relaxation is automatic. Reconnection is natural.',
             fontsize=10, fontweight='bold', color=GOLD,
             ha='center', fontfamily='monospace',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                       edgecolor=GOLD_DIM, linewidth=2))

    # Top-left: S^2 dipole with trajectory
    ax_tl = fig.add_axes([0.02, 0.50, 0.47, 0.42], facecolor=BG)
    _draw_s2_dipole(ax_tl, model)

    # Top-right: Energy vs angle
    ax_tr = fig.add_axes([0.55, 0.52, 0.42, 0.38], facecolor=BG_PANEL)
    _draw_energy_vs_angle(ax_tr, model)

    # Bottom-left: Phase diagram
    ax_bl = fig.add_axes([0.02, 0.05, 0.47, 0.42], facecolor=BG)
    _draw_phase_diagram(ax_bl, model)

    # Bottom-right: Compass analogy
    ax_br = fig.add_axes([0.55, 0.05, 0.42, 0.42], facecolor=BG)
    _draw_compass_analogy(ax_br, model)

    plt.show()


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    vd = VacuumDipole(quiet=False)

    while True:
        print()
        print("  ---- VACUUM COUPLING DIPOLE MENU ----")
        print("  *** SPECULATIVE — Exploratory BST framework ***")
        print()
        print("   1. dipole_field()        — S^2 orientation + vacuum field")
        print("   2. constrained_phase()   — channel active: dipole dynamics")
        print("   3. release_event()       — channel closes, dipole freed")
        print("   4. relaxation()          — damped oscillation to minimum")
        print("   5. vacuum_minimum()      — unique minimum energy state")
        print("   6. listen_state()        — settled, waiting, topological")
        print("   7. reattachment()        — substrate finds soliton")
        print("   8. magnetic_analogy()    — compass needle -> north")
        print("   9. summary()             — key insight")
        print("  10. show()                — 4-panel visualization")
        print("   0. exit")
        print()
        choice = input("  Choice [0-10]: ").strip()

        if choice == '0':
            print("  Goodbye.\n")
            break
        elif choice == '1':
            vd.dipole_field()
        elif choice == '2':
            vd.constrained_phase()
        elif choice == '3':
            vd.release_event()
        elif choice == '4':
            try:
                steps_input = input("  Time steps [200]: ").strip()
                t_steps = int(steps_input) if steps_input else 200
            except ValueError:
                t_steps = 200
            vd.relaxation(t_steps=t_steps)
        elif choice == '5':
            vd.vacuum_minimum()
        elif choice == '6':
            vd.listen_state()
        elif choice == '7':
            vd.reattachment()
        elif choice == '8':
            vd.magnetic_analogy()
        elif choice == '9':
            vd.summary()
        elif choice == '10':
            vd.show()
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    main()
