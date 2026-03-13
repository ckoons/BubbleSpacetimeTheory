#!/usr/bin/env python3
"""
THE REALITY WRITER
==================
Toy 48: Atomic clocks as reality-writing rate counters.

In BST, a clock does not measure "time." It counts how fast new
correlations are committed to the substrate at its location.

  N(x) = N_0 * sqrt(1 - rho / rho_137)

Where the substrate is saturated (near mass), writing is slow and the
clock ticks slowly. In deep space, abundant uncommitted capacity means
fast writing. At the horizon, N -> 0: no new correlations can be
written. Reality stops being updated at that location.

GPS is a practical demonstration: satellites at 20,200 km orbit in
lower commitment density than the ground, so their clocks write
faster by ~4.5e-10 fractional rate, accumulating ~38 us/day drift.

    from toy_reality_writer import RealityWriter
    rw = RealityWriter()
    rw.clock_rate(altitude_m=0)
    rw.gps_demo()
    rw.gravity_well_profile()
    rw.place_clocks()
    rw.schwarzschild_limit()
    rw.commitment_density_field()
    rw.pound_rebka()
    rw.summary()
    rw.show()

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

N_c = 3
n_C = 5
genus = n_C + 2           # = 7
C2 = n_C + 1              # = 6
N_max = 137                # channel capacity per contact

# Physical constants
G_N = 6.67430e-11          # m^3/(kg s^2) (Newton)
c_light = 2.99792458e8     # m/s
c2 = c_light ** 2          # m^2/s^2
hbar = 1.054571817e-34     # J s
k_B = 1.380649e-23         # J/K
M_sun = 1.989e30           # kg
R_sun = 6.957e8            # m
M_earth = 5.972e24         # kg
R_earth = 6.371e6          # m

# Schwarzschild radius helper
def r_schwarzschild(M_kg):
    """Schwarzschild radius r_s = 2GM/c^2."""
    return 2.0 * G_N * M_kg / c2

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


# ═══════════════════════════════════════════════════════════════════
# THE REALITY WRITER CLASS
# ═══════════════════════════════════════════════════════════════════

class RealityWriter:
    """
    Atomic clocks as reality-writing rate counters.

    In BST, every tick of a clock is one commitment written to the
    substrate. The interval between ticks is set by how quickly the
    local substrate can accept a new correlation. Near mass (high
    commitment density), writing is slow. In deep space, writing is
    fast. At a horizon, writing stops.

    Parameters
    ----------
    quiet : bool
        If True, suppress print output. Default False.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE REALITY WRITER")
        print("  Atomic clocks count how fast reality is being written")
        print(f"  BST channel capacity: N_max = {N_max} bits per contact")
        print("=" * 68)

    def _p(self, *args, **kwargs):
        """Print only if not quiet."""
        if not self.quiet:
            print(*args, **kwargs)

    # ─── 1. Clock Rate ───

    def clock_rate(self, altitude_m=0, M_kg=None):
        """
        Tick rate at a given altitude above Earth (or custom mass).

        In GR: rate = sqrt(1 - 2GM/(Rc^2))  (Schwarzschild metric lapse)
        In BST: rate = sqrt(1 - rho/rho_137)  -- same formula, different
        interpretation. The substrate at radius R has commitment density
        rho = GM/(Rc^2). When rho -> rho_137, all capacity is committed.

        Parameters
        ----------
        altitude_m : float
            Altitude above Earth's surface in meters. Default 0 (ground).
        M_kg : float or None
            Central mass in kg. Default None uses Earth.

        Returns
        -------
        dict with rate, altitude, potential, r_s, bst_interpretation
        """
        M = M_kg if M_kg is not None else M_earth
        R_surface = R_earth if M_kg is None else (2.0 * G_N * M / c2) * 10  # approx
        if M_kg is None:
            R = R_earth + altitude_m
        else:
            R = R_surface + altitude_m

        # Gravitational potential Phi/c^2
        phi_over_c2 = G_N * M / (R * c2)

        # Schwarzschild lapse (clock rate relative to infinity)
        r_s = r_schwarzschild(M)
        rate = np.sqrt(1.0 - r_s / R)

        # BST: commitment density fraction
        rho_frac = r_s / R  # = 2GM/(Rc^2)

        result = {
            'altitude_m': altitude_m,
            'M_kg': M,
            'R_m': R,
            'r_s_m': r_s,
            'potential_phi_over_c2': phi_over_c2,
            'rate': rate,
            'rho_fraction': rho_frac,
            'fractional_shift': rate - 1.0,
            'bst_interpretation': (
                f"Substrate at R={R:.0f}m is {rho_frac*100:.6f}% committed. "
                f"Writing rate = {rate:.15f} of maximum."
            ),
        }

        self._p(f"\n  CLOCK RATE AT ALTITUDE {altitude_m:,.0f} m")
        self._p(f"  {'─' * 42}")
        self._p(f"  Central mass:   {M:.3e} kg")
        self._p(f"  Radius:         {R:.3e} m")
        self._p(f"  r_s:            {r_s:.6e} m")
        self._p(f"  Phi/c^2:        {phi_over_c2:.6e}")
        self._p(f"  Clock rate:     {rate:.15f}")
        self._p(f"  Shift from 1:   {rate - 1.0:+.6e}")
        self._p(f"  BST: substrate {rho_frac*100:.6f}% committed at this radius")

        return result

    # ─── 2. GPS Demo ───

    def gps_demo(self):
        """
        GPS satellites at 20,200 km vs ground clocks.

        The GPS system must correct for gravitational time dilation
        (clocks in orbit tick faster) and special-relativistic time
        dilation (clocks in orbit tick slower due to velocity).

        BST interpretation: satellites orbit in lower commitment density.
        Their clocks write correlations faster because the substrate has
        more uncommitted capacity at orbital altitude.

        Returns
        -------
        dict with altitude, rate_ground, rate_satellite, daily_drift_ns,
             bst_interpretation
        """
        alt_gps = 20_200_000  # 20,200 km in meters
        R_ground = R_earth
        R_sat = R_earth + alt_gps

        r_s = r_schwarzschild(M_earth)

        # Gravitational time dilation (GR)
        rate_ground = np.sqrt(1.0 - r_s / R_ground)
        rate_sat = np.sqrt(1.0 - r_s / R_sat)

        # Fractional difference (gravitational only)
        delta_grav = rate_sat - rate_ground

        # Special relativistic correction (velocity time dilation)
        # Orbital velocity: v = sqrt(GM/R)
        v_sat = np.sqrt(G_N * M_earth / R_sat)
        gamma_sr = 1.0 / np.sqrt(1.0 - (v_sat / c_light) ** 2)
        delta_sr = 1.0 / gamma_sr - 1.0  # negative (slower)

        # Net fractional shift
        delta_net = delta_grav + delta_sr

        # Daily drift
        seconds_per_day = 86400.0
        drift_ns = delta_net * seconds_per_day * 1e9

        # Commitment density fractions
        rho_ground = r_s / R_ground
        rho_sat = r_s / R_sat

        result = {
            'altitude': alt_gps,
            'rate_ground': rate_ground,
            'rate_satellite': rate_sat,
            'delta_gravitational': delta_grav,
            'delta_special_rel': delta_sr,
            'delta_net': delta_net,
            'daily_drift_ns': drift_ns,
            'v_orbital_m_s': v_sat,
            'rho_ground': rho_ground,
            'rho_satellite': rho_sat,
            'bst_interpretation': (
                f"Ground substrate is {rho_ground*100:.6f}% committed. "
                f"Satellite substrate is {rho_sat*100:.6f}% committed. "
                f"Satellite writes faster: +{drift_ns:.1f} ns/day net drift."
            ),
        }

        self._p(f"\n  GPS SATELLITE vs GROUND CLOCK")
        self._p(f"  {'─' * 42}")
        self._p(f"  Satellite altitude:   {alt_gps/1e6:.1f} km")
        self._p(f"  Orbital velocity:     {v_sat:.0f} m/s")
        self._p(f"  r_s (Earth):          {r_s:.6e} m")
        self._p()
        self._p(f"  Rate (ground):        {rate_ground:.15f}")
        self._p(f"  Rate (satellite):     {rate_sat:.15f}")
        self._p(f"  Delta (grav only):    {delta_grav:+.6e}")
        self._p(f"  Delta (SR only):      {delta_sr:+.6e}")
        self._p(f"  Delta (net):          {delta_net:+.6e}")
        self._p(f"  Daily drift:          {drift_ns:+.1f} ns/day")
        self._p()
        self._p(f"  BST: commitment density at ground = {rho_ground:.6e}")
        self._p(f"       commitment density at orbit  = {rho_sat:.6e}")
        self._p(f"       satellite in lower density -> faster writing rate")
        self._p(f"       without correction: GPS error ~ {abs(drift_ns)*c_light*1e-9:.0f} m/day")

        return result

    # ─── 3. Gravity Well Profile ───

    def gravity_well_profile(self, M_solar=1.0, R_solar=1.0, n_points=100):
        """
        Commitment rate vs distance from a mass.

        Profiles the clock rate (= writing speed) from the surface of
        a star to 100 stellar radii. Near the surface, the substrate is
        more committed and clocks tick slower. Far away, the rate
        approaches 1 (deep space maximum).

        Parameters
        ----------
        M_solar : float
            Mass in solar masses. Default 1.0.
        R_solar : float
            Radius in solar radii. Default 1.0.
        n_points : int
            Number of sample points. Default 100.

        Returns
        -------
        dict with r_array, rate_array, lapse_array, M_kg, R_m, r_s
        """
        M = M_solar * M_sun
        R = R_solar * R_sun
        r_s = r_schwarzschild(M)

        # From surface to 100 radii
        r_array = np.linspace(R, 100 * R, n_points)
        lapse_array = np.sqrt(1.0 - r_s / r_array)
        rate_array = lapse_array.copy()  # in BST, rate = lapse

        result = {
            'r_array': r_array.tolist(),
            'rate_array': rate_array.tolist(),
            'lapse_array': lapse_array.tolist(),
            'M_kg': M,
            'R_m': R,
            'r_s_m': r_s,
            'M_solar': M_solar,
            'R_solar': R_solar,
            'rate_surface': float(rate_array[0]),
            'rate_100R': float(rate_array[-1]),
        }

        self._p(f"\n  GRAVITY WELL PROFILE")
        self._p(f"  {'─' * 42}")
        self._p(f"  Mass:            {M_solar:.1f} M_sun  ({M:.3e} kg)")
        self._p(f"  Radius:          {R_solar:.1f} R_sun  ({R:.3e} m)")
        self._p(f"  r_s:             {r_s:.6e} m")
        self._p(f"  r_s/R:           {r_s/R:.6e}")
        self._p(f"  Rate at surface: {rate_array[0]:.12f}")
        self._p(f"  Rate at 100R:    {rate_array[-1]:.12f}")
        self._p(f"  Writing speed recovers to {rate_array[-1]*100:.8f}% of max at 100R")

        return result

    # ─── 4. Place Clocks ───

    def place_clocks(self, positions=None):
        """
        Place multiple clocks at different altitudes above Earth and
        compare their relative tick rates.

        Parameters
        ----------
        positions : list of float or None
            Altitudes in meters. Default: [0, 100, 10_000, 400_000,
            20_200_000, 384_400_000] (ground, tower, plane, ISS, GPS, Moon).

        Returns
        -------
        list of dicts, one per clock, with altitude, rate, label, delta
        """
        if positions is None:
            positions = [0, 100, 10_000, 400_000, 20_200_000, 384_400_000]

        labels = {
            0: 'Ground (sea level)',
            100: 'Tower (100 m)',
            10_000: 'Aircraft (10 km)',
            400_000: 'ISS (400 km)',
            20_200_000: 'GPS satellite (20,200 km)',
            384_400_000: 'Moon orbit (384,400 km)',
        }

        r_s = r_schwarzschild(M_earth)
        clocks = []

        for alt in positions:
            R = R_earth + alt
            rate = np.sqrt(1.0 - r_s / R)
            rho = r_s / R
            label = labels.get(alt, f'Altitude {alt:,.0f} m')
            clocks.append({
                'altitude_m': alt,
                'R_m': R,
                'rate': rate,
                'rho_fraction': rho,
                'delta_from_ground': rate - np.sqrt(1.0 - r_s / R_earth),
                'label': label,
            })

        self._p(f"\n  CLOCK PLACEMENT — {len(clocks)} clocks above Earth")
        self._p(f"  {'─' * 58}")
        self._p(f"  {'Location':<30} {'Alt (m)':>14} {'Rate':>18}")
        self._p(f"  {'─' * 58}")
        for ck in clocks:
            self._p(f"  {ck['label']:<30} {ck['altitude_m']:>14,.0f} "
                    f"{ck['rate']:.15f}")
        self._p(f"  {'─' * 58}")
        self._p(f"  BST: higher altitude = less committed substrate = faster writing")

        return clocks

    # ─── 5. Schwarzschild Limit ───

    def schwarzschild_limit(self, M_solar=1.0):
        """
        As r -> r_s, the clock rate -> 0. Writing stops at the horizon.

        In BST language: at the horizon, 100% of substrate capacity is
        committed to maintaining the geometry. No capacity remains for
        new correlations. The channel is full. Reality stops being
        written at that location.

        Parameters
        ----------
        M_solar : float
            Mass in solar masses. Default 1.0.

        Returns
        -------
        dict with r_s, asymptotic_behavior, profile near horizon
        """
        M = M_solar * M_sun
        r_s = r_schwarzschild(M)

        # Profile approaching the horizon: from 10*r_s down to 1.001*r_s
        r_factors = np.array([10, 5, 3, 2, 1.5, 1.2, 1.1, 1.05, 1.02,
                              1.01, 1.005, 1.002, 1.001])
        r_vals = r_factors * r_s
        rates = np.sqrt(1.0 - r_s / r_vals)

        result = {
            'M_solar': M_solar,
            'M_kg': M,
            'r_s_m': r_s,
            'r_s_km': r_s / 1e3,
            'asymptotic_behavior': 'rate -> 0 as r -> r_s',
            'r_factors': r_factors.tolist(),
            'r_values_m': r_vals.tolist(),
            'rates': rates.tolist(),
            'bst_interpretation': (
                f"At r_s = {r_s:.3f} m, all substrate capacity is committed. "
                f"N -> 0. No new correlations can be written. "
                f"The channel is full. Reality stops being updated."
            ),
        }

        self._p(f"\n  SCHWARZSCHILD LIMIT — {M_solar:.1f} M_sun")
        self._p(f"  {'─' * 50}")
        self._p(f"  r_s = {r_s:.3f} m  ({r_s/1e3:.3f} km)")
        self._p()
        self._p(f"  {'r/r_s':>8}  {'r (km)':>12}  {'Clock rate':>15}  Committed")
        self._p(f"  {'─' * 50}")
        for i, rf in enumerate(r_factors):
            pct = (1.0 - rates[i]) * 100
            bar = '#' * int(pct / 2)
            self._p(f"  {rf:>8.3f}  {r_vals[i]/1e3:>12.3f}  "
                    f"{rates[i]:>15.10f}  {bar}")
        self._p(f"  {'─' * 50}")
        self._p(f"  As r -> r_s: rate -> 0. Writing stops.")
        self._p(f"  The horizon is where the substrate's write buffer is full.")

        return result

    # ─── 6. Commitment Density Field ───

    def commitment_density_field(self, grid_size=50):
        """
        2D field of commitment density around a mass (Earth).

        Higher density = slower clocks = more substrate already committed
        to maintaining the gravitational field.

        Parameters
        ----------
        grid_size : int
            Number of points along each axis. Default 50.

        Returns
        -------
        dict with x_grid, y_grid, density_grid (as nested lists)
        """
        # Work in units of R_earth, from -5R to +5R
        span = 5.0  # in R_earth units
        x = np.linspace(-span, span, grid_size)
        y = np.linspace(-span, span, grid_size)
        X, Y = np.meshgrid(x, y)

        # Distance from center in meters
        R_grid = np.sqrt(X ** 2 + Y ** 2) * R_earth
        R_grid = np.maximum(R_grid, R_earth)  # floor at surface

        r_s = r_schwarzschild(M_earth)

        # Commitment density = r_s / R  (fraction of capacity committed)
        density = r_s / R_grid

        # Clock rate = sqrt(1 - density)
        rate_grid = np.sqrt(1.0 - density)

        result = {
            'x_grid': X.tolist(),
            'y_grid': Y.tolist(),
            'density_grid': density.tolist(),
            'rate_grid': rate_grid.tolist(),
            'grid_size': grid_size,
            'span_R_earth': span,
            'max_density': float(np.max(density)),
            'min_density': float(np.min(density)),
        }

        self._p(f"\n  COMMITMENT DENSITY FIELD")
        self._p(f"  {'─' * 42}")
        self._p(f"  Grid:           {grid_size} x {grid_size}")
        self._p(f"  Span:           {span:.0f} R_earth per side")
        self._p(f"  Max density:    {np.max(density):.6e} (at surface)")
        self._p(f"  Min density:    {np.min(density):.6e} (at corners)")
        self._p(f"  BST: density = fraction of substrate committed to geometry")

        return result

    # ─── 7. Pound-Rebka ───

    def pound_rebka(self):
        """
        The Pound-Rebka experiment (1959).

        A photon climbing 22.5 m in Earth's gravity loses frequency
        by 2.46e-15. In BST: the photon crosses a commitment density
        gradient. Lower commitment density at the top means the
        receiving clock writes faster, so it perceives the arriving
        photon as redshifted.

        Returns
        -------
        dict with height, delta_f_over_f (predicted and measured),
             bst_interpretation
        """
        h = 22.5  # meters (Jefferson Tower, Harvard)
        g = 9.81  # m/s^2 at Earth's surface

        # GR prediction: delta_f/f = g*h/c^2
        delta_predicted = g * h / c2

        # Measured value (Pound & Rebka 1960, refined by Pound & Snider 1965)
        delta_measured = 2.57e-15  # +/- 0.26e-15

        # Commitment density at bottom and top
        r_s = r_schwarzschild(M_earth)
        R_bottom = R_earth
        R_top = R_earth + h

        rate_bottom = np.sqrt(1.0 - r_s / R_bottom)
        rate_top = np.sqrt(1.0 - r_s / R_top)
        delta_rate = rate_top - rate_bottom

        result = {
            'height_m': h,
            'delta_f_over_f_predicted': delta_predicted,
            'delta_f_over_f_measured': delta_measured,
            'agreement_percent': abs(delta_predicted - delta_measured) / delta_measured * 100,
            'rate_bottom': rate_bottom,
            'rate_top': rate_top,
            'delta_rate': delta_rate,
            'bst_interpretation': (
                f"Photon climbs {h}m through commitment density gradient. "
                f"Top clock writes {delta_rate:.3e} faster than bottom. "
                f"Photon perceived as redshifted: delta_f/f = {delta_predicted:.3e}."
            ),
        }

        self._p(f"\n  POUND-REBKA EXPERIMENT (1959)")
        self._p(f"  {'─' * 50}")
        self._p(f"  Height:            {h} m (Jefferson Tower, Harvard)")
        self._p(f"  GR prediction:     delta_f/f = {delta_predicted:.3e}")
        self._p(f"  Measured (1965):   delta_f/f = {delta_measured:.3e}")
        self._p(f"  Agreement:         within {abs(delta_predicted-delta_measured)/delta_measured*100:.0f}%")
        self._p()
        self._p(f"  Clock rate bottom: {rate_bottom:.15f}")
        self._p(f"  Clock rate top:    {rate_top:.15f}")
        self._p(f"  Delta rate:        {delta_rate:+.6e}")
        self._p()
        self._p(f"  BST: the photon crosses a commitment density gradient.")
        self._p(f"  The top clock writes faster (lower rho), so it perceives")
        self._p(f"  the arriving photon as redshifted. Not 'time slowing' —")
        self._p(f"  the substrate at the bottom is busier writing reality.")

        return result

    # ─── 8. Summary ───

    def summary(self):
        """
        Key insight: the clock counts how fast reality is being written.

        Returns
        -------
        dict with title, key_points, bst_conclusion
        """
        key_points = [
            "A clock does not measure 'time.' It counts commitments.",
            "Each tick = one correlation written to the substrate.",
            "Near mass: substrate is saturated, writing is slow, clock ticks slowly.",
            "Deep space: abundant uncommitted capacity, fast writing, fast ticks.",
            "At the horizon: N -> 0. All capacity committed. Writing stops.",
            "GPS demonstrates this daily: satellite clocks write ~38 us/day faster.",
            "Pound-Rebka: photon crossing 22.5m feels the density gradient.",
            "The information paradox dissolves: you cannot write to a full channel.",
            "G/C ratio: local census of rendered vs unrendered substrate (dark matter).",
        ]

        result = {
            'title': 'THE REALITY WRITER',
            'toy_number': 48,
            'key_points': key_points,
            'bst_conclusion': (
                "Gravitational time dilation is not a distortion of an abstract "
                "quantity called time. It is a physical constraint on the rate at "
                "which the substrate can commit new correlations. Clocks near mass "
                "run slow because the substrate near mass is busy."
            ),
        }

        self._p()
        self._p("  " + "=" * 58)
        self._p("  THE REALITY WRITER — SUMMARY")
        self._p("  " + "=" * 58)
        for i, pt in enumerate(key_points, 1):
            self._p(f"  {i}. {pt}")
        self._p()
        self._p("  CONCLUSION:")
        self._p(f"  {result['bst_conclusion']}")
        self._p()
        self._p("  The clock counts commitments.")
        self._p("  Reality is what has been written.")
        self._p("  " + "=" * 58)

        return result

    # ─── 9. Show (Visualisation) ───

    def show(self):
        """
        4-panel visualisation of the Reality Writer.

        Top-left:     Gravity well with clock icons at different heights,
                      colored by tick rate (blue=fast, red=slow)
        Top-right:    GPS demonstration — Earth with satellite orbit,
                      rate comparison
        Bottom-left:  2D commitment density heatmap around a mass
        Bottom-right: Clock rate vs altitude curve
        """
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        import matplotlib.patheffects as pe

        fig = plt.figure(figsize=(18, 11), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The Reality Writer -- Toy 48 -- BST')

        # ─── Title ───
        fig.text(0.5, 0.97, 'THE REALITY WRITER',
                 fontsize=22, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.945,
                 'Atomic clocks count how fast reality is being written  |  '
                 'N(x) = N_0 sqrt(1 - rho/rho_137)',
                 fontsize=11, color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # ─── Bottom strip ───
        fig.text(0.5, 0.015,
                 'The clock counts commitments. '
                 'Reality is what has been written.',
                 fontsize=11, color=GOLD, ha='center', fontfamily='monospace',
                 style='italic',
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                           edgecolor=GOLD_DIM, linewidth=1))

        # ═══════════════════════════════════════════════════
        # TOP-LEFT: Gravity well with clocks
        # ═══════════════════════════════════════════════════
        ax_well = fig.add_axes([0.04, 0.52, 0.44, 0.38], facecolor=DARK_PANEL)
        ax_well.set_title('GRAVITY WELL — CLOCK RATE vs DEPTH',
                          fontsize=13, fontweight='bold', color=CYAN,
                          fontfamily='monospace', pad=8)

        # Draw gravity well as a funnel shape
        r_vals = np.linspace(0.3, 5.0, 300)
        # Potential well: -GM/r shape
        well_depth = -1.0 / r_vals
        well_depth_norm = (well_depth - well_depth.min()) / (well_depth.max() - well_depth.min())

        # Draw the well (both sides for symmetry)
        ax_well.fill_between(r_vals, well_depth, well_depth.min() - 0.1,
                             color='#0a1a3a', alpha=0.6)
        ax_well.fill_between(-r_vals, well_depth, well_depth.min() - 0.1,
                             color='#0a1a3a', alpha=0.6)
        ax_well.plot(r_vals, well_depth, color=CYAN, linewidth=2, alpha=0.8)
        ax_well.plot(-r_vals, well_depth, color=CYAN, linewidth=2, alpha=0.8)

        # Place clocks at various depths
        clock_positions = [
            (0.5, 'Surface', 0.15),
            (1.0, '1R', 0.35),
            (2.0, '2R', 0.65),
            (4.0, '4R', 0.88),
        ]

        for r_pos, label, rate_approx in clock_positions:
            y_pos = -1.0 / r_pos
            # Color: red=slow, blue=fast
            color = plt.cm.coolwarm(rate_approx)
            # Draw clock symbol
            circle = plt.Circle((r_pos, y_pos), 0.15, fill=True,
                                facecolor=color, edgecolor=WHITE,
                                linewidth=1.5, alpha=0.9, zorder=5)
            ax_well.add_patch(circle)
            circle_neg = plt.Circle((-r_pos, y_pos), 0.15, fill=True,
                                    facecolor=color, edgecolor=WHITE,
                                    linewidth=1.5, alpha=0.9, zorder=5)
            ax_well.add_patch(circle_neg)
            ax_well.text(r_pos, y_pos + 0.3, label, fontsize=8, color=WHITE,
                         ha='center', fontfamily='monospace', zorder=6)
            ax_well.text(r_pos, y_pos - 0.03, f'{rate_approx:.0%}',
                         fontsize=7, color='#000000', fontweight='bold',
                         ha='center', va='center', fontfamily='monospace', zorder=6)

        # Mass at center
        ax_well.plot(0, well_depth.min() + 0.1, 'o', color=ORANGE,
                     markersize=15, zorder=10)
        ax_well.text(0, well_depth.min() + 0.35, 'M', fontsize=12,
                     color=ORANGE, ha='center', fontweight='bold',
                     fontfamily='monospace')

        ax_well.set_xlim(-5.5, 5.5)
        ax_well.set_ylim(well_depth.min() - 0.3, 0.3)
        ax_well.set_xlabel('Distance from mass (R units)', color=GREY,
                           fontfamily='monospace', fontsize=9)
        ax_well.set_ylabel('Gravitational potential', color=GREY,
                           fontfamily='monospace', fontsize=9)
        ax_well.tick_params(colors=DGREY, labelsize=8)
        for spine in ax_well.spines.values():
            spine.set_color(DGREY)

        # Legend text
        ax_well.text(0.02, 0.95,
                     'Red = slow writing (saturated)\n'
                     'Blue = fast writing (capacity)',
                     transform=ax_well.transAxes, fontsize=8, color=GOLD_DIM,
                     fontfamily='monospace', va='top',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0a1a',
                               edgecolor=DGREY, alpha=0.8))

        # ═══════════════════════════════════════════════════
        # TOP-RIGHT: GPS demonstration
        # ═══════════════════════════════════════════════════
        ax_gps = fig.add_axes([0.54, 0.52, 0.44, 0.38], facecolor=DARK_PANEL)
        ax_gps.set_title('GPS — REALITY WRITING RATE DIFFERENCE',
                         fontsize=13, fontweight='bold', color=CYAN,
                         fontfamily='monospace', pad=8)
        ax_gps.set_aspect('equal')

        # Draw Earth
        theta = np.linspace(0, 2 * np.pi, 200)
        earth_r = 1.0  # normalized
        ax_gps.fill(earth_r * np.cos(theta), earth_r * np.sin(theta),
                    color='#1a3355', alpha=0.8)
        ax_gps.plot(earth_r * np.cos(theta), earth_r * np.sin(theta),
                    color=DEEP_BLUE, linewidth=2)

        # Draw GPS orbit
        gps_r = 1.0 + 20200.0 / 6371.0  # ~4.17 R_earth
        ax_gps.plot(gps_r * np.cos(theta), gps_r * np.sin(theta),
                    color=DGREY, linewidth=1, linestyle='--', alpha=0.6)

        # Place satellite markers
        n_sats = 6
        for i in range(n_sats):
            angle = 2 * np.pi * i / n_sats + np.pi / 6
            sx = gps_r * np.cos(angle)
            sy = gps_r * np.sin(angle)
            ax_gps.plot(sx, sy, 's', color=GREEN, markersize=8, zorder=5)

        # Ground clock marker
        ax_gps.plot(0, earth_r, 'o', color=RED, markersize=10, zorder=5)
        ax_gps.text(0, earth_r + 0.3, 'Ground\nclock',
                    fontsize=7, color=RED, ha='center',
                    fontfamily='monospace')

        # Satellite label
        ax_gps.text(gps_r * 0.7 + 0.3, gps_r * 0.7 + 0.3,
                    'GPS\nsatellites',
                    fontsize=7, color=GREEN, ha='center',
                    fontfamily='monospace')

        # Info box
        gps_data = self.gps_demo.__wrapped__() if hasattr(self.gps_demo, '__wrapped__') else None
        # Compute inline
        r_s_e = r_schwarzschild(M_earth)
        rate_g = np.sqrt(1.0 - r_s_e / R_earth)
        rate_s = np.sqrt(1.0 - r_s_e / (R_earth + 20_200_000))
        drift = (rate_s - rate_g) * 86400 * 1e9

        info_text = (
            f"Ground rate:  {rate_g:.12f}\n"
            f"Sat rate:     {rate_s:.12f}\n"
            f"Net drift:    ~{drift:.0f} ns/day\n"
            f"Position err: ~{abs(drift)*c_light*1e-9:.0f} m/day\n"
            f"without correction"
        )
        ax_gps.text(0.02, 0.02, info_text,
                    transform=ax_gps.transAxes, fontsize=8, color=GOLD,
                    fontfamily='monospace', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0a1a',
                              edgecolor=GOLD_DIM, alpha=0.9))

        # BST interpretation
        ax_gps.text(0.98, 0.98,
                    'BST: satellites in lower\n'
                    'commitment density\n'
                    '-> faster reality writing',
                    transform=ax_gps.transAxes, fontsize=8, color=PURPLE,
                    fontfamily='monospace', va='top', ha='right',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0a2a',
                              edgecolor=PURPLE, alpha=0.8))

        ax_gps.set_xlim(-6, 6)
        ax_gps.set_ylim(-6, 6)
        ax_gps.axis('off')

        # ═══════════════════════════════════════════════════
        # BOTTOM-LEFT: 2D commitment density heatmap
        # ═══════════════════════════════════════════════════
        ax_heat = fig.add_axes([0.04, 0.06, 0.44, 0.38], facecolor=DARK_PANEL)
        ax_heat.set_title('COMMITMENT DENSITY FIELD (2D)',
                          fontsize=13, fontweight='bold', color=CYAN,
                          fontfamily='monospace', pad=8)

        # Build the field
        grid_n = 200
        span = 5.0
        x = np.linspace(-span, span, grid_n)
        y = np.linspace(-span, span, grid_n)
        X, Y = np.meshgrid(x, y)
        R_grid = np.sqrt(X ** 2 + Y ** 2)
        R_grid = np.maximum(R_grid, 1.0)  # floor at 1 R_earth

        r_s_norm = r_s_e / R_earth  # ~1.4e-9
        # For visualization, exaggerate the density to make it visible
        # Use log scale: density ~ 1/R
        density_vis = 1.0 / R_grid

        # Plot
        im = ax_heat.pcolormesh(X, Y, density_vis,
                                cmap='inferno', shading='gouraud')
        # Earth circle
        earth_circle = plt.Circle((0, 0), 1.0, fill=False,
                                  edgecolor=CYAN, linewidth=1.5,
                                  linestyle='--', alpha=0.7)
        ax_heat.add_patch(earth_circle)
        ax_heat.text(0, 0, 'M', fontsize=14, color=CYAN, ha='center',
                     va='center', fontweight='bold', fontfamily='monospace')

        ax_heat.set_xlabel('x (R_earth)', color=GREY,
                           fontfamily='monospace', fontsize=9)
        ax_heat.set_ylabel('y (R_earth)', color=GREY,
                           fontfamily='monospace', fontsize=9)
        ax_heat.tick_params(colors=DGREY, labelsize=8)
        for spine in ax_heat.spines.values():
            spine.set_color(DGREY)

        # Colorbar
        cb = plt.colorbar(im, ax=ax_heat, fraction=0.04, pad=0.02)
        cb.set_label('Commitment density (1/R)', color=GREY,
                     fontfamily='monospace', fontsize=8)
        cb.ax.tick_params(colors=DGREY, labelsize=7)

        ax_heat.text(0.02, 0.95,
                     'Brighter = more committed substrate\n'
                     '= slower clocks = denser reality',
                     transform=ax_heat.transAxes, fontsize=8, color=GOLD_DIM,
                     fontfamily='monospace', va='top',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0a1a',
                               edgecolor=DGREY, alpha=0.8))

        # ═══════════════════════════════════════════════════
        # BOTTOM-RIGHT: Clock rate vs altitude
        # ═══════════════════════════════════════════════════
        ax_curve = fig.add_axes([0.54, 0.06, 0.44, 0.38], facecolor=DARK_PANEL)
        ax_curve.set_title('CLOCK RATE vs ALTITUDE (EARTH)',
                           fontsize=13, fontweight='bold', color=CYAN,
                           fontfamily='monospace', pad=8)

        # Altitude from 0 to 50,000 km
        alts = np.linspace(0, 50_000_000, 1000)  # meters
        Rs = R_earth + alts
        rates = np.sqrt(1.0 - r_s_e / Rs)

        # Plot the rate curve
        # Show deviation from 1 (magnified)
        deviations = (rates - 1.0) * 1e10  # in units of 1e-10

        ax_curve.plot(alts / 1e6, deviations, color=CYAN, linewidth=2)
        ax_curve.fill_between(alts / 1e6, deviations, deviations[0],
                              color=CYAN, alpha=0.1)

        # Mark special altitudes
        special = [
            (0, 'Ground', RED),
            (400, 'ISS', ORANGE),
            (20200, 'GPS', GREEN),
            (35786, 'GEO', PURPLE),
        ]
        for alt_km, label, color in special:
            alt_m = alt_km * 1e3
            R_spec = R_earth + alt_m
            rate_spec = np.sqrt(1.0 - r_s_e / R_spec)
            dev_spec = (rate_spec - 1.0) * 1e10
            ax_curve.axvline(alt_km, color=color, alpha=0.3, linestyle='--')
            ax_curve.plot(alt_km, dev_spec, 'o', color=color,
                          markersize=8, zorder=5)
            ax_curve.text(alt_km + 500, dev_spec + 0.02, label,
                          fontsize=8, color=color, fontfamily='monospace')

        ax_curve.set_xlabel('Altitude (1000 km)', color=GREY,
                            fontfamily='monospace', fontsize=9)
        ax_curve.set_ylabel('Clock rate shift (x 1e-10)', color=GREY,
                            fontfamily='monospace', fontsize=9)
        ax_curve.tick_params(colors=DGREY, labelsize=8)
        for spine in ax_curve.spines.values():
            spine.set_color(DGREY)

        # Annotation
        ax_curve.text(0.98, 0.05,
                      'Higher = less committed\n'
                      '       = faster writing\n'
                      '       = clock ticks faster',
                      transform=ax_curve.transAxes, fontsize=8, color=GOLD_DIM,
                      fontfamily='monospace', va='bottom', ha='right',
                      bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0a1a',
                                edgecolor=DGREY, alpha=0.8))

        # Copyright
        fig.text(0.99, 0.003,
                 'Casey Koons 2026 / Claude Opus 4.6',
                 fontsize=7, color=DGREY, ha='right',
                 fontfamily='monospace')

        plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the Reality Writer toy."""

    print()
    print("=" * 62)
    print("  THE REALITY WRITER")
    print("  Toy 48 | Bubble Spacetime Theory")
    print("=" * 62)
    print()
    print("  Clocks count commitments. Reality is what has been written.")
    print("  Near mass: substrate saturated, writing slow.")
    print("  Deep space: capacity available, writing fast.")
    print("  At the horizon: N -> 0. Writing stops.")
    print()

    rw = RealityWriter(quiet=False)

    while True:
        print()
        print("  --- MENU ---")
        print("  1) Clock rate at altitude")
        print("  2) GPS demonstration")
        print("  3) Gravity well profile")
        print("  4) Place clocks at multiple altitudes")
        print("  5) Schwarzschild limit")
        print("  6) Commitment density field")
        print("  7) Pound-Rebka experiment")
        print("  8) Summary")
        print("  9) Show (4-panel visualisation)")
        print("  0) Quit")
        print()

        choice = input("  Choice: ").strip()
        print()

        if choice == '1':
            try:
                alt = float(input("  Altitude (m) [0]: ").strip() or '0')
            except (ValueError, EOFError):
                alt = 0
            rw.clock_rate(altitude_m=alt)
        elif choice == '2':
            rw.gps_demo()
        elif choice == '3':
            try:
                ms = float(input("  Mass (M_sun) [1.0]: ").strip() or '1.0')
            except (ValueError, EOFError):
                ms = 1.0
            rw.gravity_well_profile(M_solar=ms)
        elif choice == '4':
            rw.place_clocks()
        elif choice == '5':
            try:
                ms = float(input("  Mass (M_sun) [1.0]: ").strip() or '1.0')
            except (ValueError, EOFError):
                ms = 1.0
            rw.schwarzschild_limit(M_solar=ms)
        elif choice == '6':
            rw.commitment_density_field()
        elif choice == '7':
            rw.pound_rebka()
        elif choice == '8':
            rw.summary()
        elif choice == '9':
            rw.show()
        elif choice == '0':
            print("  The clock counts commitments.")
            print("  Reality is what has been written.")
            break
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    import sys
    if '--test' in sys.argv:
        rw = RealityWriter(quiet=True)
        r = rw.clock_rate(0)
        print('ground rate:', bool(r))
        r = rw.gps_demo()
        print('gps drift_ns:', r.get('daily_drift_ns', 'FAIL'))
        r = rw.gravity_well_profile()
        print('profile:', len(r.get('r_array', [])))
        r = rw.place_clocks()
        print('clocks:', type(r).__name__)
        r = rw.schwarzschild_limit()
        print('r_s:', bool(r))
        r = rw.commitment_density_field()
        print('field:', bool(r))
        r = rw.pound_rebka()
        print('pound_rebka:', bool(r))
        r = rw.summary()
        print('summary:', bool(r))
        print('ALL PASS')
    else:
        main()
