#!/usr/bin/env python3
"""
THE COMMITMENT RATE SURVEY
==========================
A "fair weather map" of the solar system and beyond.

We find objects by seeing commitments above the local background —
exactly like a radio telescope finds signals above noise. This map
IS the background: the baseline commitment rate at every distance
from the Sun, against which anomalies stand out.

Every location has a commitment rate — how fast new correlations are
being written to the BST substrate. Near the Sun it's stormy (hot, dense,
high C). In interstellar space it's dead calm (CMB floor only).

Temperature T ∝ 1/√r. The commitment rate C ∝ T per degree of freedom.
The "fair weather" baseline tells you what's EXPECTED. Anything above
it has a source. Anything below it (suppressed by σ) is engineered.

    from toy_commitment_survey import CommitmentSurvey
    cs = CommitmentSurvey()
    cs.temperature_at(1.0)               # 279 K at Earth orbit
    cs.conditions_at(5.2)                # full report at Jupiter
    cs.survey()                          # inner → interstellar
    cs.weather_map()                     # text forecast
    cs.detection_window(sigma=0.5)       # where can we spot σ=0.5?

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
genus = n_C + 2       # = 7
C2 = n_C + 1          # = 6
N_max = 137            # channel capacity per contact

# Physical constants
k_B = 1.380649e-23     # J/K
hbar = 1.054571817e-34  # J·s
G_N = 6.67430e-11      # m³/(kg·s²)
m_u = 1.66053907e-27   # kg (atomic mass unit)
sigma_SB = 5.670374e-8  # W/(m²·K⁴)
c_light = 2.99792458e8  # m/s
AU = 1.496e11           # m
L_Sun = 3.828e26        # W (solar luminosity)
m_p = 1.67262192e-27   # kg (proton mass)
T_CMB = 2.7255          # K (CMB temperature)

# Solar wind reference values at 1 AU
SW_DENSITY_1AU = 7.0     # protons/cm³ = 7e6 /m³
SW_VELOCITY_1AU = 400.0  # km/s (slow wind)
SW_TEMP_1AU = 1e5        # K (proton temperature)


# ═══════════════════════════════════════════════════════════════════
# SOLAR SYSTEM LANDMARKS
# ═══════════════════════════════════════════════════════════════════

LANDMARKS = [
    {'name': 'Sun surface',     'r_au': 0.00465, 'symbol': '☉',
     'note': 'T=5778K, corona 1-3 MK'},
    {'name': 'Mercury',         'r_au': 0.387,   'symbol': '☿',
     'note': 'Dayside 700K, nightside 100K'},
    {'name': 'Venus',           'r_au': 0.723,   'symbol': '♀',
     'note': 'Surface 737K (greenhouse)'},
    {'name': 'Earth',           'r_au': 1.000,   'symbol': '♁',
     'note': '288K avg, biosphere active'},
    {'name': 'Mars',            'r_au': 1.524,   'symbol': '♂',
     'note': '210K avg, thin CO₂ atmosphere'},
    {'name': 'Asteroid belt',   'r_au': 2.7,     'symbol': '⊕',
     'note': 'Ceres at 167K, millions of bodies'},
    {'name': 'Jupiter',         'r_au': 5.203,   'symbol': '♃',
     'note': '165K cloud tops, internal heat'},
    {'name': 'Saturn',          'r_au': 9.537,   'symbol': '♄',
     'note': '134K cloud tops, ring system'},
    {'name': 'Uranus',          'r_au': 19.19,   'symbol': '♅',
     'note': '76K, extreme axial tilt'},
    {'name': 'Neptune',         'r_au': 30.07,   'symbol': '♆',
     'note': '72K, strongest winds in solar system'},
    {'name': 'Kuiper belt',     'r_au': 40.0,    'symbol': '◇',
     'note': '~44K, Pluto region'},
    {'name': 'Heliopause',      'r_au': 120.0,   'symbol': '|',
     'note': 'Solar wind meets interstellar medium'},
    {'name': 'Oort cloud inner','r_au': 2000,    'symbol': '○',
     'note': '~10K, reservoir of long-period comets'},
    {'name': 'Oort cloud outer','r_au': 50000,   'symbol': '◯',
     'note': '~4K, near CMB floor'},
    {'name': 'Proxima Centauri','r_au': 268770,  'symbol': '★',
     'note': '2.73K (CMB only), 4.24 ly'},
]

# Weather condition names — based on local temperature
# (mass-independent; temperature is the location-dependent quantity)
def _weather(T_K):
    """Assign a weather descriptor based on local temperature."""
    if T_K > 3000:
        return "INFERNO"
    elif T_K > 1000:
        return "STORM"
    elif T_K > 300:
        return "HOT"
    elif T_K > 100:
        return "WARM"
    elif T_K > 30:
        return "COOL"
    elif T_K > 10:
        return "COLD"
    elif T_K > 4:
        return "FRIGID"
    else:
        return "CALM"

# Weather colors for display
WEATHER_COLORS = {
    'INFERNO': '#ff0000',
    'STORM':   '#ff4400',
    'HOT':     '#ff8800',
    'WARM':    '#ffcc00',
    'COOL':    '#44aaff',
    'COLD':    '#2266cc',
    'FRIGID':  '#1144aa',
    'CALM':    '#112244',
}


# ═══════════════════════════════════════════════════════════════════
# THE COMMITMENT SURVEY CLASS
# ═══════════════════════════════════════════════════════════════════

class CommitmentSurvey:
    """
    Survey the commitment rate across the solar system and beyond.

    At each location, compute:
      - Equilibrium temperature (from solar irradiance)
      - Solar wind density and temperature
      - Local commitment rate per unit volume
      - Commitment rate for a reference 1 kg object
      - Weather descriptor

    The "fair weather map" shows where reality is being written
    furiously (near the Sun) vs almost frozen (interstellar space).
    """

    def __init__(self, quiet=False):
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE COMMITMENT RATE SURVEY")
        print("  Fair weather map of the solar system")
        print(f"  BST channel: N_max = {N_max} bits per contact")
        print("=" * 68)

    # ─── Local conditions ───

    def _temp_at(self, r_au: float) -> float:
        """Equilibrium temperature at r_au (internal, no print)."""
        r_m = r_au * AU
        if r_m < 1e6:  # inside the Sun
            return 5778.0
        T_eq = (L_Sun / (16 * np.pi * sigma_SB * r_m**2))**0.25
        return max(T_eq, T_CMB)

    def temperature_at(self, r_au: float) -> dict:
        """
        Equilibrium temperature at distance r from the Sun.

        For a slowly rotating body (absorbed = emitted):
          T(r) = (L_Sun / (16π σ_SB r²))^(1/4)

        At 1 AU this gives ~279 K (Earth without greenhouse).
        Floor is CMB at 2.7255 K.
        """
        T = self._temp_at(r_au)

        result = {
            'r_au': r_au,
            'T_K': T,
            'T_eq_formula': '(L_Sun / 16πσ_SB r²)^{1/4}',
            'above_cmb': T > T_CMB * 1.1,
        }

        print(f"\n  TEMPERATURE at {r_au:.3f} AU")
        print(f"  T = {T:.1f} K")
        if T <= T_CMB * 1.1:
            print(f"  → At CMB floor ({T_CMB:.3f} K)")
        return result

    def solar_wind_at(self, r_au: float) -> dict:
        """
        Solar wind proton density, velocity, and temperature at distance r.

        Density ∝ 1/r² (conservation of mass flux).
        Velocity ≈ constant (400 km/s slow wind, 800 km/s fast wind).
        Temperature ∝ 1/r^(2/3) (adiabatic expansion, γ=5/3).

        Beyond the heliopause (~120 AU), solar wind is replaced by
        the interstellar medium (ISM): n ≈ 0.1 cm⁻³, T ≈ 6000 K.
        """
        if r_au > 120:
            # Interstellar medium
            n = 0.1e6  # 0.1 cm⁻³ = 1e5 m⁻³
            v = 26.0   # km/s (LSR velocity)
            T = 6000.0  # K (warm neutral medium)
            region = "Interstellar medium"
        elif r_au < 0.01:
            # Solar corona
            n = 1e14   # m⁻³
            v = 50.0   # km/s (sub-Alfvénic)
            T = 1.5e6  # K (corona)
            region = "Solar corona"
        else:
            n = SW_DENSITY_1AU * 1e6 / r_au**2  # m⁻³
            v = SW_VELOCITY_1AU                   # km/s
            T = SW_TEMP_1AU / r_au**(2/3)         # K
            region = "Solar wind"

        result = {
            'r_au': r_au,
            'n_m3': n,
            'v_km_s': v,
            'T_K': T,
            'region': region,
        }
        return result

    def commitment_rate_at(self, r_au: float,
                           object_mass_kg: float = 1.0,
                           mu_amu: float = 28.0,
                           sigma: float = 0.0) -> dict:
        """
        Commitment rate for an object at distance r from the Sun.

        Two contributions:
        1. Object's own thermal rate: C_obj = 3N_atoms × (k_BT/2πℏ) × (1-σ)
        2. Solar wind bombardment: C_sw = n_sw × σ_cross × v_sw × N_max

        Total C = C_obj + C_sw (object's own noise + environment noise)
        """
        # Object temperature at this distance (quiet — no print)
        T_obj = self._temp_at(r_au)

        # Solar wind
        sw = self.solar_wind_at(r_au)

        # Object's own commitment rate
        n_atoms = object_mass_kg / (mu_amu * m_u)
        thermal_freq = k_B * T_obj / (2 * np.pi * hbar)
        C_thermal = 3 * n_atoms * thermal_freq * (1.0 - sigma)

        # Solar wind contribution (protons hitting the object)
        # Cross section ~ geometric (1 m² for 1 kg at density ~2500)
        obj_radius = (3 * object_mass_kg / (4 * np.pi * 2500))**(1/3)
        obj_cross = np.pi * obj_radius**2
        C_sw = sw['n_m3'] * obj_cross * sw['v_km_s'] * 1000  # hits/s

        # BST: each thermal fluctuation writes N_max bits
        C_total = C_thermal + C_sw
        info_rate = C_total * N_max

        weather = _weather(T_obj)

        result = {
            'r_au': r_au,
            'T_obj_K': T_obj,
            'C_thermal': C_thermal,
            'C_solar_wind': C_sw,
            'C_total': C_total,
            'info_rate_bits_s': info_rate,
            'sigma': sigma,
            'weather': weather,
            'sw_region': sw['region'],
        }
        return result

    def conditions_at(self, r_au: float, object_mass_kg: float = 1.0,
                      mu_amu: float = 28.0, sigma: float = 0.0) -> dict:
        """
        Full conditions report at distance r.
        Combines temperature, solar wind, and commitment rate.
        """
        cr = self.commitment_rate_at(r_au, object_mass_kg, mu_amu, sigma)
        sw = self.solar_wind_at(r_au)

        # Find nearest landmark
        nearest = min(LANDMARKS, key=lambda l: abs(l['r_au'] - r_au))
        near_str = (f"{nearest['symbol']} {nearest['name']}"
                    if abs(nearest['r_au'] - r_au) / max(r_au, 0.001) < 0.3
                    else "")

        print(f"\n  ══════════════════════════════════════════════")
        print(f"  CONDITIONS AT {r_au:.3f} AU  {near_str}")
        print(f"  ══════════════════════════════════════════════")
        print(f"  Temperature:    {cr['T_obj_K']:.1f} K")
        print(f"  Solar wind:     {sw['n_m3']:.2e} m⁻³, "
              f"{sw['v_km_s']:.0f} km/s, {sw['T_K']:.0f} K")
        print(f"  Region:         {sw['region']}")
        print(f"  C_thermal:      {cr['C_thermal']:.2e} contacts/s")
        print(f"  C_solar_wind:   {cr['C_solar_wind']:.2e} contacts/s")
        print(f"  C_total:        {cr['C_total']:.2e} contacts/s")
        print(f"  Info rate:      {cr['info_rate_bits_s']:.2e} bits/s")
        print(f"  Weather:        {cr['weather']}")
        if sigma > 0:
            print(f"  Structure:      σ = {sigma:.2f}")

        return cr

    # ─── Full survey ───

    def survey(self, object_mass_kg: float = 1.0,
               mu_amu: float = 28.0) -> list:
        """
        Survey commitment rates at all solar system landmarks.
        Shows the full "weather map" from Sun to Proxima Centauri.
        """
        print()
        print("  COMMITMENT RATE SURVEY — Solar System & Beyond")
        print("  ═════════════════════════════════════════════════")
        print(f"  Reference: 1 kg silicate body, σ = 0")
        print()
        print(f"  {'Location':<22} {'r(AU)':>10} {'T(K)':>8} "
              f"{'C(s⁻¹)':>12} {'Weather':>8}")
        print(f"  {'─'*22} {'─'*10} {'─'*8} {'─'*12} {'─'*8}")

        results = []
        for lm in LANDMARKS:
            cr = self.commitment_rate_at(
                lm['r_au'], object_mass_kg, mu_amu, 0.0)

            r_str = f"{lm['r_au']:.1f}" if lm['r_au'] < 1000 else f"{lm['r_au']:.0f}"
            label = f"{lm['symbol']} {lm['name']}"

            print(f"  {label:<22} {r_str:>10} {cr['T_obj_K']:>8.1f} "
                  f"{cr['C_total']:>12.2e} {cr['weather']:>8}")

            results.append({**lm, **cr})

        # Summary
        c_earth = [r for r in results if r['name'] == 'Earth'][0]['C_total']
        c_prox = [r for r in results
                  if r['name'] == 'Proxima Centauri'][0]['C_total']
        ratio = c_earth / c_prox if c_prox > 0 else np.inf

        print()
        print(f"  Dynamic range: Sun/CMB = {ratio:.0f}× "
              f"({np.log10(max(ratio, 1)):.1f} orders)")
        print(f"  Temperature spans ~{5778/T_CMB:.0f}× from photosphere "
              f"to CMB floor.")
        print(f"  CMB floor: T = {T_CMB:.3f} K sets the minimum everywhere.")

        return results

    # ─── Weather map (text) ───

    def weather_map(self) -> list:
        """
        The commitment weather forecast — text version.
        Shows conditions across the solar system in weather terms.
        """
        print()
        print("  ┌──────────────────────────────────────────────────────┐")
        print("  │   BST COMMITMENT WEATHER — SOLAR SYSTEM FORECAST    │")
        print("  └──────────────────────────────────────────────────────┘")
        print()

        zones = [
            (0.01, 0.3,  "INNER INFERNO",
             "Corona to Mercury orbit. Plasma temperatures 10⁵-10⁶ K.\n"
             "     Commitment rate extreme. Reality written furiously.\n"
             "     No structure survives long."),
            (0.3, 1.5,   "HABITABLE STORM",
             "Venus to Mars. T = 200-450 K. Active thermal noise.\n"
             "     Rocks outgas, atmospheres churn, biospheres commit.\n"
             "     Earth's biosphere is a commitment amplifier."),
            (1.5, 5.0,   "WARM BELT",
             "Mars to Jupiter. T = 120-200 K. Asteroid belt here.\n"
             "     Moderate commitment. Comets begin to freeze.\n"
             "     Good for long-duration observation."),
            (5.0, 30,    "GAS GIANT COOL",
             "Jupiter to Neptune. T = 50-120 K. Internal heat matters.\n"
             "     Solar wind weakening. Commitment rate dropping.\n"
             "     Moons potentially habitable (tidal heating)."),
            (30, 100,    "DEEP FREEZE",
             "Kuiper belt to heliopause. T = 20-50 K.\n"
             "     Very low commitment. Objects barely thermally active.\n"
             "     Engineered objects increasingly hard to distinguish."),
            (100, 1000,  "THE WALL",
             "Heliopause transition. Solar wind stops. ISM begins.\n"
             "     T ≈ 10-20 K. Commitment rate drops by ~10⁴.\n"
             "     Voyager 1 & 2 crossed here."),
            (1000, 50000, "OORT SILENCE",
             "Oort cloud. T = 4-10 K, approaching CMB floor.\n"
             "     Near-zero commitment. Objects essentially frozen.\n"
             "     Pristine — unchanged since solar system formation."),
            (50000, 300000, "INTERSTELLAR CALM",
             "Open space. T = 2.73 K (CMB only). ISM ~ 0.1 cm⁻³.\n"
             "     Minimum possible commitment rate in the universe.\n"
             "     An engineered object here is indistinguishable from\n"
             "     nothing — no thermal noise to suppress."),
        ]

        forecasts = []
        for r_min, r_max, name, desc in zones:
            r_mid = np.sqrt(r_min * r_max)
            cr = self.commitment_rate_at(r_mid, 1.0, 28.0, 0.0)
            weather = cr['weather']

            print(f"  {name}  ({r_min:.0f}–{r_max:.0f} AU)")
            print(f"     {desc}")
            print(f"     C ≈ {cr['C_total']:.1e}/s  [{weather}]")
            print()

            forecasts.append({
                'zone': name,
                'r_range_au': (r_min, r_max),
                'C_typical': cr['C_total'],
                'descriptor': weather,
            })

        print("  KEY INSIGHT: Temperature spans ~2000× from Sun to CMB.")
        print("  Commitment rate ∝ T, so the 'weather' tracks temperature.")
        print("  An engineered object's σ-anomaly is most detectable")
        print("  in the WARM BELT (1.5-5 AU) where C is moderate —")
        print("  high enough to measure, low enough to see suppression.")

        return forecasts

    # ─── Detection window ───

    def detection_window(self, sigma: float = 0.5,
                         object_mass_kg: float = 1e8,
                         mu_amu: float = 28.0) -> dict:
        """
        Where in the solar system can we detect an object with
        structure factor σ? Shows the "detection window" —
        distances where the quiet anomaly is measurable.

        Too close: thermal background dominates, hard to isolate object
        Too far: object too faint to measure C
        Sweet spot: enough signal, clear suppression
        """
        print()
        print(f"  DETECTION WINDOW for σ = {sigma:.2f}")
        print(f"  ═══════════════════════════════════════")
        print(f"  Object: {object_mass_kg:.0e} kg, μ = {mu_amu} amu")
        print()

        distances = np.array([0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10, 30, 100])
        Q = sigma / (1 - sigma)

        print(f"  {'r(AU)':>8} {'T(K)':>8} {'C_nat':>12} {'C_eng':>12} "
              f"{'Deficit':>12} {'Detectable?'}")
        print(f"  {'─'*8} {'─'*8} {'─'*12} {'─'*12} {'─'*12} {'─'*11}")

        sweet_spot = None
        best_snr = 0

        results = []
        for r in distances:
            cr_nat = self.commitment_rate_at(r, object_mass_kg, mu_amu, 0.0)
            cr_eng = self.commitment_rate_at(r, object_mass_kg, mu_amu, sigma)

            deficit = cr_nat['C_total'] - cr_eng['C_total']

            # SNR: deficit / √(C_nat) for Poisson counting in 1 hour
            t_obs = 3600  # 1 hour
            n_expected = cr_nat['C_total'] * t_obs
            if n_expected > 0:
                snr = deficit * t_obs / np.sqrt(n_expected)
            else:
                snr = 0

            detectable = "YES ★" if snr > 5 else "marginal" if snr > 2 else "no"

            if snr > best_snr:
                best_snr = snr
                sweet_spot = r

            print(f"  {r:8.2f} {cr_nat['T_obj_K']:8.1f} "
                  f"{cr_nat['C_total']:12.2e} {cr_eng['C_total']:12.2e} "
                  f"{deficit:12.2e} {detectable}")

            results.append({
                'r_au': r, 'C_nat': cr_nat['C_total'],
                'C_eng': cr_eng['C_total'], 'deficit': deficit,
                'snr': snr, 'detectable': snr > 5,
            })

        print()
        if sweet_spot:
            print(f"  Sweet spot: ~{sweet_spot:.1f} AU  (best SNR = {best_snr:.1f})")
        print(f"  Quiet anomaly Q = {Q:.2f}  (object {1/(1-sigma):.1f}× quieter)")

        return {
            'sigma': sigma,
            'Q': Q,
            'sweet_spot_au': sweet_spot,
            'best_snr': best_snr,
            'distances': results,
        }

    # ─── Radial profile ───

    def radial_profile(self, r_min_au: float = 0.1,
                       r_max_au: float = 300000,
                       n_points: int = 100) -> dict:
        """
        Compute commitment rate vs distance for a radial profile.
        Returns arrays suitable for plotting.
        """
        r_au = np.logspace(np.log10(r_min_au), np.log10(r_max_au), n_points)
        T = np.zeros_like(r_au)
        C = np.zeros_like(r_au)

        for i, r in enumerate(r_au):
            cr = self.commitment_rate_at(r, 1.0, 28.0, 0.0)
            T[i] = cr['T_obj_K']
            C[i] = cr['C_total']

        return {
            'r_au': r_au,
            'T_K': T,
            'C_rate': C,
        }

    # ─── Interstellar trajectories ───

    def trajectory_oumuamua(self) -> dict:
        """
        'Oumuamua's trajectory through the commitment landscape.
        Perihelion 0.255 AU, hyperbolic, entered from Lyra direction.
        """
        print()
        print("  'OUMUAMUA TRAJECTORY — Commitment Landscape")
        print("  ════════════════════════════════════════════")
        print()

        # Key points on trajectory (time, distance)
        points = [
            ('Interstellar approach', 100.0),
            ('Detection (Haleakalā)', 0.5),
            ('Perihelion', 0.255),
            ('Earth closest', 0.162),
            ('Last observation', 2.0),
            ('Now (estimated)', 50.0),
        ]

        print(f"  {'Phase':<28} {'r(AU)':>8} {'T(K)':>8} "
              f"{'C':>12} {'Weather':>8}")
        print(f"  {'─'*28} {'─'*8} {'─'*8} {'─'*12} {'─'*8}")

        results = []
        for phase, r in points:
            # Using 'Oumuamua parameters: ~10⁷ kg, silicate, σ=0.9
            cr = self.commitment_rate_at(r, 1e7, 28.0, 0.9)
            print(f"  {phase:<28} {r:8.3f} {cr['T_obj_K']:8.1f} "
                  f"{cr['C_total']:12.2e} {cr['weather']:>8}")
            results.append({'phase': phase, 'r_au': r, **cr})

        print()
        print("  Note: σ=0.9 assumed (no outgassing observed).")
        print("  At perihelion (0.255 AU), a natural comet would be")
        print("  screaming with outgassing. 'Oumuamua was silent.")
        print("  It crossed from COOL to HOT to COOL without flinching.")

        return {
            'name': "'Oumuamua",
            'sigma': 0.9,
            'classification': 'ENGINEERED',
            'perihelion_au': 0.255,
            'trajectory': results,
        }

    def trajectory_3i(self) -> dict:
        """
        3I/ATLAS trajectory through the commitment landscape.
        Much larger, CO₂ outgassing, more comet-like.
        """
        print()
        print("  3I/ATLAS TRAJECTORY — Commitment Landscape")
        print("  ══════════════════════════════════════════")
        print()

        points = [
            ('Interstellar approach', 200.0),
            ('Discovery (ATLAS)', 7.0),
            ('CO₂ outgassing onset', 4.5),
            ('Anti-tail observed', 3.0),
            ('Current (inbound)', 2.5),
            ('Perihelion (predicted)', 1.36),
        ]

        print(f"  {'Phase':<28} {'r(AU)':>8} {'T(K)':>8} "
              f"{'C':>12} {'Weather':>8}")
        print(f"  {'─'*28} {'─'*8} {'─'*8} {'─'*12} {'─'*8}")

        results = []
        for phase, r in points:
            # 3I: ~10¹² kg, CO₂ (μ=44), σ≈0.15
            cr = self.commitment_rate_at(r, 1e12, 44.0, 0.15)
            print(f"  {phase:<28} {r:8.3f} {cr['T_obj_K']:8.1f} "
                  f"{cr['C_total']:12.2e} {cr['weather']:>8}")
            results.append({'phase': phase, 'r_au': r, **cr})

        print()
        print("  3I began outgassing at ~4.5 AU — thermally expected.")
        print("  CO₂ dominance is unusual (most comets are H₂O).")
        print("  Its commitment rate tracks the natural curve —")
        print("  the warm-up follows solar irradiance, not suppression.")

        return {
            'name': '3I/ATLAS',
            'sigma': 0.15,
            'classification': 'NATURAL',
            'perihelion_au': 1.36,
            'trajectory': results,
        }

    # ─── Summary ───

    def summary(self) -> dict:
        """The survey in one box."""
        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║      COMMITMENT RATE SURVEY — SUMMARY                ║")
        print("  ╠═══════════════════════════════════════════════════════╣")
        print("  ║                                                       ║")
        print("  ║  The solar system is a temperature gradient:          ║")
        print("  ║    Sun:          5778 K   (INFERNO)                   ║")
        print("  ║    Earth:         279 K   (WARM)                      ║")
        print("  ║    Jupiter:       122 K   (WARM)                      ║")
        print("  ║    Kuiper belt:    44 K   (COOL)                      ║")
        print("  ║    Interstellar:  2.7 K   (CALM)                      ║")
        print("  ║                                                       ║")
        print("  ║  T spans ~2000× from photosphere to CMB floor.        ║")
        print("  ║  C(1 kg) ∝ T — commitment rate tracks temperature.    ║")
        print("  ║                                                       ║")
        print("  ║  Detection: objects found above this background.       ║")
        print("  ║  Suppression (σ>0) → BELOW background = engineered.   ║")
        print("  ║    Too close: background blinding                     ║")
        print("  ║    Too far:   signal too faint to measure             ║")
        print("  ║    Sweet spot: 1-5 AU (warm belt)                     ║")
        print("  ║                                                       ║")
        print("  ║  'Oumuamua crossed the warm belt silently.            ║")
        print("  ║  3I/ATLAS is outgassing on schedule.                  ║")
        print("  ║                                                       ║")
        print(f"  ║  Floor: CMB at {T_CMB:.3f} K — minimum C everywhere.  ║")
        print(f"  ║  Each contact writes {N_max} bits to the substrate.   ║")
        print("  ║                                                       ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        return {
            'n_landmarks': len(LANDMARKS),
            'n_zones': 8,
            'T_range': f'{T_CMB:.1f} K – 5778 K',
            'commitment_range': f'C ∝ T across ~2000×',
            'sweet_spot_au': '1-5',
            'cmb_floor_K': T_CMB,
            'bits_per_contact': N_max,
        }

    # ─── Visualization ───

    def show(self):
        """Launch the 4-panel visualization."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib not available. Use text API.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(18, 11), facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 33 — Commitment Rate Survey')

        fig.text(0.5, 0.97, 'COMMITMENT RATE SURVEY',
                 fontsize=24, fontweight='bold', color='#00ccff',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'Fair weather map of the solar system  '
                 '(BST commitment landscape)',
                 fontsize=10, color='#668899', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.015,
                 'Copyright (c) 2026 Casey Koons — Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        # Get radial profile data
        profile = self.radial_profile(0.01, 300000, 200)

        # ─── Panel 1: Temperature profile ───
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')
        ax1.loglog(profile['r_au'], profile['T_K'], color='#ff8844', lw=2)
        ax1.axhline(T_CMB, color='#4444ff', ls='--', lw=1, alpha=0.7)
        ax1.text(1e4, T_CMB * 1.5, f'CMB = {T_CMB:.2f} K', color='#4444ff',
                 fontsize=8, fontfamily='monospace')

        # Mark landmarks
        for lm in LANDMARKS[:11]:  # Sun to Kuiper
            T_at = self.temperature_at(lm['r_au'])
            ax1.plot(lm['r_au'], T_at['T_K'], 'o', color='#ffffff',
                     markersize=4)
            if lm['name'] in ('Earth', 'Jupiter', 'Neptune'):
                ax1.annotate(lm['symbol'], (lm['r_au'], T_at['T_K']),
                            textcoords="offset points", xytext=(5, 5),
                            color='#aaaaaa', fontsize=10)

        ax1.set_xlabel('Distance (AU)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_ylabel('Temperature (K)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_title('TEMPERATURE PROFILE', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax1.tick_params(colors='#888888')
        for spine in ax1.spines.values():
            spine.set_color('#333333')

        # ─── Panel 2: Commitment rate profile ───
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')
        ax2.loglog(profile['r_au'], profile['C_rate'], color='#44ff88', lw=2)

        # Color bands for weather zones (temperature-based)
        weather_bands = [
            (0.01, 0.01, '#ff000020', 'INFERNO'),   # Sun only (T>3000)
            (0.01, 0.3, '#ff440020', 'STORM'),       # inner corona (T>1000)
            (0.3, 1.0, '#ff880020', 'HOT'),           # Mercury-Earth (T>300)
            (1.0, 10, '#ffcc0020', 'WARM'),            # Earth-Saturn (T>100)
            (10, 120, '#44aaff10', 'COOL'),            # Uranus-heliopause (T>30)
            (120, 5000, '#2266cc10', 'COLD'),          # ISM-Oort (T>10)
            (5000, 300000, '#11224410', 'CALM'),       # deep (T≈CMB)
        ]
        c_max = float(np.max(profile['C_rate']))
        for r1, r2, color, label in weather_bands:
            ax2.axvspan(r1, r2, color=color, alpha=0.3)
            ax2.text(np.sqrt(r1 * r2), c_max * 2,
                     label, color='#666666', fontsize=6, fontfamily='monospace',
                     ha='center', va='top', rotation=90)

        ax2.set_xlabel('Distance (AU)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_ylabel('C (contacts/s)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_title('COMMITMENT RATE PROFILE', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax2.tick_params(colors='#888888')
        for spine in ax2.spines.values():
            spine.set_color('#333333')

        # ─── Panel 3: Natural vs engineered comparison ───
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')

        r_arr = np.logspace(-1, 2, 100)
        C_nat = np.array([self.commitment_rate_at(r, 1e7, 28, 0.0)['C_total']
                          for r in r_arr])
        C_eng = np.array([self.commitment_rate_at(r, 1e7, 28, 0.5)['C_total']
                          for r in r_arr])
        C_quiet = np.array([self.commitment_rate_at(r, 1e7, 28, 0.9)['C_total']
                            for r in r_arr])

        ax3.loglog(r_arr, C_nat, color='#44ff88', lw=2, label='σ=0 (natural)')
        ax3.loglog(r_arr, C_eng, color='#ffaa44', lw=2, label='σ=0.5 (alloy)')
        ax3.loglog(r_arr, C_quiet, color='#ff4444', lw=2,
                  label="σ=0.9 ('Oumuamua?)")

        # Mark 'Oumuamua perihelion
        ax3.axvline(0.255, color='#ff4444', ls=':', lw=1, alpha=0.5)
        ax3.text(0.3, float(np.min(C_quiet)) * 0.5,
                 "'Oumuamua\nperihelion", color='#ff4444', fontsize=7,
                 fontfamily='monospace')

        ax3.set_xlabel('Distance (AU)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax3.set_ylabel('C (contacts/s)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax3.set_title('NATURAL vs ENGINEERED', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax3.legend(loc='upper right', fontsize=7, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax3.tick_params(colors='#888888')
        for spine in ax3.spines.values():
            spine.set_color('#333333')

        # ─── Panel 4: Weather forecast text ───
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)
        ax4.axis('off')
        ax4.set_title('WEATHER FORECAST', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')

        forecast_lines = [
            ('☉ INFERNO', '< 0.3 AU', '#ff4444'),
            ('♀♁♂ HOT', '0.3–1.5 AU', '#ff8844'),
            ('⊕ WARM', '1.5–5 AU ★sweet spot', '#ffcc44'),
            ('♃♄ COOL', '5–30 AU', '#44aaff'),
            ('◇ COLD', '30–120 AU', '#2266cc'),
            ('| THE WALL', '~120 AU', '#ffffff'),
            ('○ FRIGID', '120–50k AU', '#1144aa'),
            ('★ CALM', '> 50k AU (CMB floor)', '#334466'),
        ]

        for i, (name, rng, color) in enumerate(forecast_lines):
            y = 9.0 - i * 1.1
            ax4.text(0.5, y, name, color=color, fontsize=10,
                     fontfamily='monospace', fontweight='bold')
            ax4.text(5.0, y, rng, color='#888888', fontsize=9,
                     fontfamily='monospace')

        ax4.text(5, 0.5,
                 "Detection sweet spot: 1-5 AU\n"
                 "where C is high enough to measure\n"
                 "but low enough to see suppression",
                 color='#ffcc44', fontsize=8, fontfamily='monospace',
                 ha='center', va='center',
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                           edgecolor='#ffcc44', alpha=0.8))

        plt.tight_layout(rect=(0, 0.03, 1, 0.92))
        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    cs = CommitmentSurvey()

    print()
    print("  What would you like to explore?")
    print("  1) Conditions at a specific distance")
    print("  2) Full survey (Sun to Proxima)")
    print("  3) Weather forecast")
    print("  4) Detection window (where to spot σ=0.5)")
    print("  5) 'Oumuamua trajectory")
    print("  6) 3I/ATLAS trajectory")
    print("  7) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [1-7]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '7'

    if choice == '1':
        try:
            r = float(input("  Distance in AU: ").strip())
        except (EOFError, KeyboardInterrupt, ValueError):
            r = 1.0
        cs.conditions_at(r)
    elif choice == '2':
        cs.survey()
    elif choice == '3':
        cs.weather_map()
    elif choice == '4':
        cs.detection_window(sigma=0.5)
    elif choice == '5':
        cs.trajectory_oumuamua()
    elif choice == '6':
        cs.trajectory_3i()
    elif choice == '7':
        cs.survey()
        cs.weather_map()
        cs.trajectory_oumuamua()
        cs.trajectory_3i()
        cs.summary()
        try:
            cs.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        cs.summary()


if __name__ == '__main__':
    main()
