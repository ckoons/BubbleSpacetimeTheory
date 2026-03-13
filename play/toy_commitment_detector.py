#!/usr/bin/env python3
"""
THE COMMITMENT DETECTOR
=======================
Detecting engineered objects by their silence.

In BST, every object has two measurable signatures:
  G — gravitational field (proportional to mass, always present)
  C — commitment rate (thermal fluctuations writing new correlations)

Natural objects: G/C = constant (mass and noise scale together).
Engineered objects: G/C is HIGHER (same mass, fewer active DOFs — "too quiet").

The structure factor σ measures how much internal entropy is frozen by
engineering. A rock has σ ≈ 0. A machined alloy hull has σ ≈ 0.3–0.5.
A room-temperature superconductor has σ → 1.

    from toy_commitment_detector import CommitmentDetector
    cd = CommitmentDetector()
    cd.gc_ratio(temp_K=200, mu_amu=28)           # natural silicate
    cd.quiet_anomaly(sigma=0.4)                   # engineered hull
    cd.oumuamua()                                 # apply to 1I/'Oumuamua
    cd.atlas_3i()                                 # apply to 3I/ATLAS
    cd.detector_requirements(distance_au=0.25)    # what we'd need

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
k_B = 1.380649e-23     # J/K  (Boltzmann)
hbar = 1.054571817e-34  # J·s  (reduced Planck)
G_N = 6.67430e-11      # m³/(kg·s²)  (Newton)
m_u = 1.66053907e-27   # kg  (atomic mass unit)
sigma_SB = 5.670374e-8  # W/(m²·K⁴)  (Stefan-Boltzmann)
c_light = 2.99792458e8  # m/s
AU = 1.496e11           # meters per AU


# ═══════════════════════════════════════════════════════════════════
# OBJECT DATABASE
# ═══════════════════════════════════════════════════════════════════

OBJECTS = {
    'comet': {
        'name': 'Generic comet',
        'mu_amu': 18.0,        # H₂O ice
        'density_kg_m3': 500,
        'sigma': 0.03,
        'size_m': 1000,
        'temp_K': 200,
        'description': 'Typical Oort-cloud comet. Ice + rock, thermally active.',
    },
    'asteroid': {
        'name': 'Generic asteroid',
        'mu_amu': 28.0,        # SiO₂
        'density_kg_m3': 2500,
        'sigma': 0.05,
        'size_m': 1000,
        'temp_K': 250,
        'description': 'S-type silicate asteroid. Minor crystalline order.',
    },
    'iron': {
        'name': 'Iron-nickel asteroid',
        'mu_amu': 56.0,        # Fe
        'density_kg_m3': 7800,
        'sigma': 0.08,
        'size_m': 1000,
        'temp_K': 250,
        'description': 'M-type metallic asteroid. Natural iron-nickel alloy.',
    },
    'oumuamua': {
        'name': "'Oumuamua (1I)",
        'mu_amu': 28.0,        # assumed silicate
        'density_kg_m3': 2500,  # if rock; could be much lower
        'sigma': None,          # unknown — that's what we're measuring
        'size_m': 200,          # ~200m × 35m × 35m
        'temp_K': 300,          # at perihelion
        'description': 'First interstellar object. No outgassing. Anomalous acceleration.',
    },
    'borisov': {
        'name': '2I/Borisov',
        'mu_amu': 18.0,        # H₂O/CO
        'density_kg_m3': 500,
        'sigma': 0.03,
        'size_m': 1000,
        'temp_K': 200,
        'description': 'Second interstellar object. Normal cometary behavior.',
    },
    '3i_atlas': {
        'name': '3I/ATLAS',
        'mu_amu': 44.0,        # CO₂ dominated
        'density_kg_m3': 600,
        'sigma': None,          # testing
        'size_m': 5600,         # up to 5.6 km
        'temp_K': 180,
        'description': 'Third interstellar object. CO₂+HCN coma. Nickel vapor. Anti-tail.',
    },
    'survey_craft': {
        'name': 'Nickel survey craft',
        'mu_amu': 58.0,        # Ni-based superalloy
        'density_kg_m3': 8200,
        'sigma': 0.45,
        'size_m': 2000,
        'temp_K': 150,
        'description': 'Hypothetical engineered probe. Nickel alloy hull. σ ≈ 0.45.',
    },
    'dead_satellite': {
        'name': 'Dead satellite',
        'mu_amu': 27.0,        # Aluminum
        'density_kg_m3': 200,   # mostly hollow
        'sigma': 0.35,
        'size_m': 10,
        'temp_K': 200,
        'description': 'Derelict satellite. Aluminum structure. σ ≈ 0.35.',
    },
    'metamaterial': {
        'name': 'Metamaterial probe',
        'mu_amu': 28.0,        # Si-based
        'density_kg_m3': 500,
        'sigma': 0.80,
        'size_m': 100,
        'temp_K': 150,
        'description': 'Hypothetical advanced probe. Most DOFs frozen. σ ≈ 0.80.',
    },
}


# ═══════════════════════════════════════════════════════════════════
# THE COMMITMENT DETECTOR CLASS
# ═══════════════════════════════════════════════════════════════════

class CommitmentDetector:
    """
    Detect engineered objects by their suppressed commitment rate.

    In BST, every thermal fluctuation is a contact that writes N_max = 137
    bits of correlation. Natural objects have commitment rate proportional
    to mass × temperature. Engineered objects suppress this by freezing
    internal degrees of freedom (structure factor σ).

    The G/C ratio is mass-independent for natural objects.
    An anomalously HIGH G/C means the object is "too quiet" — engineered.
    """

    def __init__(self, quiet=False):
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE COMMITMENT DETECTOR")
        print("  Detecting engineered objects by their silence")
        print(f"  BST channel capacity: N_max = {N_max} bits per contact")
        print("=" * 68)

    # ─── Core physics ───

    def commitment_rate(self, mass_kg: float, temp_K: float,
                        mu_amu: float = 28.0, sigma: float = 0.0) -> dict:
        """
        Compute the commitment rate for an object.

        C = mass × T × k_B/ℏ × (N_active/N_max) × (1 - σ)

        where:
          N_active = min(3 × N_atoms, N_max)  per contact
          k_B T / ℏ = thermal contact frequency
          σ = structure factor (fraction of frozen DOFs)
          N_max = 137 (Haldane channel capacity per contact)

        Returns dict with rate, components, and BST interpretation.
        """
        n_atoms = mass_kg / (mu_amu * m_u)
        thermal_freq = k_B * temp_K / (2 * np.pi * hbar)  # Hz
        dof_per_atom = 3.0  # Dulong-Petit (solid)
        n_active = dof_per_atom * n_atoms  # total active modes

        # BST: each contact carries at most N_max modes
        channel_fraction = min(n_active, N_max) / N_max

        c_natural = n_active * thermal_freq * channel_fraction
        c_actual = c_natural * (1.0 - sigma)

        # BST: each contact writes N_max bits
        info_rate = c_actual * N_max  # bits/second

        result = {
            'n_atoms': n_atoms,
            'thermal_freq_Hz': thermal_freq,
            'C_natural': c_natural,
            'C_actual': c_actual,
            'sigma': sigma,
            'suppression': 1.0 - sigma,
            'info_rate_bits_per_s': info_rate,
            'contacts_per_second': c_actual,
        }

        print(f"\n  COMMITMENT RATE")
        print(f"  ───────────────")
        print(f"  Mass:          {mass_kg:.2e} kg")
        print(f"  Temperature:   {temp_K:.0f} K")
        print(f"  Composition:   μ = {mu_amu:.0f} amu")
        print(f"  Structure:     σ = {sigma:.2f}")
        print(f"  N_atoms:       {n_atoms:.2e}")
        print(f"  Thermal freq:  {thermal_freq:.2e} Hz  (k_BT/2πℏ)")
        print(f"  C_natural:     {c_natural:.2e} contacts/s")
        if sigma > 0:
            print(f"  C_actual:      {c_actual:.2e} contacts/s  (×{1-sigma:.2f})")
        print(f"  Info rate:     {info_rate:.2e} bits/s  (×{N_max} per contact)")

        return result

    def g_field(self, mass_kg: float, distance_m: float) -> dict:
        """Compute gravitational acceleration at distance d from mass m."""
        a = G_N * mass_kg / distance_m**2
        result = {
            'mass_kg': mass_kg,
            'distance_m': distance_m,
            'distance_au': distance_m / AU,
            'acceleration_m_s2': a,
        }

        print(f"\n  GRAVITATIONAL FIELD")
        print(f"  ──────────────────")
        print(f"  Mass:     {mass_kg:.2e} kg")
        print(f"  Distance: {distance_m:.2e} m  ({distance_m/AU:.3f} AU)")
        print(f"  g:        {a:.2e} m/s²")

        return result

    def gc_ratio(self, temp_K: float = 200, mu_amu: float = 28.0,
                 sigma: float = 0.0) -> dict:
        """
        Compute the G/C ratio (mass-independent for natural objects).

        G/C = μ·m_u·2πℏ / (3·k_B·T·(1-σ))

        This is the key diagnostic:
          Natural: G/C = constant (depends only on T and composition)
          Engineered: G/C is HIGHER by factor 1/(1-σ)
        """
        gc_natural = mu_amu * m_u * 2 * np.pi * hbar / (3 * k_B * temp_K)
        gc_actual = gc_natural / (1.0 - sigma) if sigma < 1.0 else np.inf

        anomaly = sigma / (1.0 - sigma) if sigma < 1.0 else np.inf

        result = {
            'temp_K': temp_K,
            'mu_amu': mu_amu,
            'sigma': sigma,
            'gc_natural': gc_natural,
            'gc_actual': gc_actual,
            'anomaly_factor': 1.0 / (1.0 - sigma) if sigma < 1 else np.inf,
            'quiet_anomaly_Q': anomaly,
        }

        print(f"\n  G/C RATIO (mass-independent diagnostic)")
        print(f"  ───────────────────────────────────────")
        print(f"  T = {temp_K:.0f} K    μ = {mu_amu:.0f} amu    σ = {sigma:.2f}")
        print(f"  G/C_natural  = {gc_natural:.4e} kg·s")
        if sigma > 0:
            print(f"  G/C_actual   = {gc_actual:.4e} kg·s")
            print(f"  Anomaly:     {1/(1-sigma):.2f}× expected  "
                  f"(Q = {anomaly:.2f})")
            print(f"  Object is {1/(1-sigma):.1f}× quieter than a natural body")
        else:
            print(f"  → Natural object: G/C at baseline")
        print(f"\n  Key: G/C is MASS-INDEPENDENT.")
        print(f"  A 1 kg rock and a 10⁹ kg asteroid have the same G/C")
        print(f"  at the same temperature. Only σ changes it.")

        return result

    def quiet_anomaly(self, sigma: float) -> dict:
        """
        The quiet anomaly Q = σ/(1-σ).

        Q = 0:    natural object (σ = 0)
        Q = 1:    object is 2× quieter (σ = 0.5)
        Q = 9:    object is 10× quieter (σ = 0.9)
        Q → ∞:    perfectly silent (σ → 1)

        This is what we'd measure to detect engineering.
        """
        if sigma >= 1.0:
            Q = np.inf
            factor = np.inf
        else:
            Q = sigma / (1.0 - sigma)
            factor = 1.0 / (1.0 - sigma)

        # How many standard deviations for Poisson statistics
        # If we observe N contacts in time t, expected = N_expected
        # Observed = N_expected × (1-σ)
        # Deficit = N_expected × σ
        # For large N: σ_stat = √N_expected
        # Significance = σ × √N_expected
        # For N_expected = 10⁶: significance = σ × 1000

        result = {
            'sigma': sigma,
            'Q': Q,
            'suppression_factor': factor,
            'description': self._interpret_sigma(sigma),
        }

        print(f"\n  QUIET ANOMALY")
        print(f"  ─────────────")
        print(f"  Structure factor: σ = {sigma:.3f}")
        print(f"  Quiet anomaly:    Q = σ/(1−σ) = {Q:.3f}")
        print(f"  Object is {factor:.1f}× quieter than natural")
        print(f"  Interpretation:   {result['description']}")
        print()

        # Table of reference values
        print(f"  Reference scale:")
        print(f"  {'σ':>6}  {'Q':>8}  {'Quieter':>10}  Example")
        print(f"  {'─'*6}  {'─'*8}  {'─'*10}  {'─'*30}")
        refs = [
            (0.0, 'Natural rock/ice'),
            (0.1, 'Annealed crystal'),
            (0.3, 'Forged metal'),
            (0.5, 'Precision machined alloy'),
            (0.7, 'Aerospace composite'),
            (0.9, 'Metamaterial / superlattice'),
            (0.99, 'Room-temperature superconductor'),
        ]
        for s, ex in refs:
            q = s / (1 - s)
            f = 1 / (1 - s)
            marker = "  ←" if abs(s - sigma) < 0.02 else ""
            print(f"  {s:6.2f}  {q:8.2f}  {f:10.1f}×  {ex}{marker}")

        return result

    def _interpret_sigma(self, sigma):
        if sigma < 0.01:
            return "Natural object — thermally normal"
        elif sigma < 0.2:
            return "Crystalline / annealed — mild suppression"
        elif sigma < 0.5:
            return "Engineered structure — significant suppression"
        elif sigma < 0.8:
            return "Advanced engineering — major suppression"
        elif sigma < 0.99:
            return "Exotic material — near-silent"
        else:
            return "Perfectly ordered — zero thermal noise"

    # ─── Classifier ───

    def classify(self, sigma=None, gc_measured=None,
                 gc_expected=None, quiet=False) -> dict:
        """
        Classify an object as NATURAL, ANOMALOUS, or ENGINEERED
        based on its structure factor or measured G/C ratio.

        Thresholds:
          σ < 0.10  or  Q < 0.11   →  NATURAL (< 2σ deviation)
          0.10 ≤ σ < 0.30          →  ANOMALOUS (2-5σ)
          σ ≥ 0.30  or  Q ≥ 0.43  →  ENGINEERED (> 5σ)
        """
        if sigma is None and gc_measured is not None and gc_expected is not None:
            # Infer sigma from G/C ratio
            if gc_measured > gc_expected:
                sigma = 1.0 - gc_expected / gc_measured
            else:
                sigma = 0.0

        if sigma is None:
            sigma = 0.0

        Q = sigma / (1 - sigma) if sigma < 1 else np.inf

        if sigma < 0.10:
            classification = "NATURAL"
            color = "green"
            detail = "Within normal thermal variation"
        elif sigma < 0.30:
            classification = "ANOMALOUS"
            color = "yellow"
            detail = "Unusual order — warrants further observation"
        else:
            classification = "ENGINEERED"
            color = "red"
            detail = "Significant DOF suppression — not thermally natural"

        result = {
            'sigma': sigma,
            'Q': Q,
            'classification': classification,
            'color': color,
            'detail': detail,
        }

        if not quiet:
            print(f"\n  CLASSIFICATION")
            print(f"  ──────────────")
            print(f"  σ = {sigma:.3f}    Q = {Q:.3f}")
            print(f"  Verdict: [{classification}]")
            print(f"  {detail}")

        return result

    # ─── Shield efficiency (3I/ATLAS CO₂ debris shield) ───

    def shield_efficiency(self, v_km_s: float = 58.0,
                          gas_density_kg_m3: float = 1e-15) -> dict:
        """
        Compute energy absorption of a CO₂ gas cloud as a debris shield.

        At 58 km/s (3I/ATLAS velocity), micro-meteoroids carry enormous
        kinetic energy. A CO₂ gas shield absorbs energy via:
          1. Ionization of CO₂ molecules by impactor
          2. Momentum transfer (gas drag)
          3. Ablation products slowing debris

        This is relevant to the anti-tail observation.
        """
        v_m_s = v_km_s * 1000

        # Micro-meteoroid parameters
        dust_mass_kg = 1e-12  # 1 picogram (typical interplanetary dust)
        dust_radius_m = 5e-6  # 5 μm

        # Kinetic energy per grain
        KE_J = 0.5 * dust_mass_kg * v_m_s**2
        KE_eV = KE_J / 1.602e-19

        # CO₂ column density for 1 mean free path of stopping
        # Cross section ≈ πr² for geometric collision
        sigma_coll = np.pi * dust_radius_m**2
        # Mean free path in gas
        n_CO2 = gas_density_kg_m3 / (44 * m_u)  # molecules/m³
        mfp = 1.0 / (n_CO2 * sigma_coll) if n_CO2 > 0 else np.inf

        # Energy absorbed per unit column
        # Each CO₂ collision absorbs ~ionization energy (13.8 eV) + momentum
        E_ionize_eV = 13.8  # CO₂ first ionization
        n_collisions = KE_eV / E_ionize_eV  # collisions to fully stop

        # Shield mass required per m² for one mfp
        shield_mass_per_m2 = gas_density_kg_m3 * mfp

        result = {
            'velocity_km_s': v_km_s,
            'dust_KE_eV': KE_eV,
            'dust_KE_J': KE_J,
            'n_CO2_per_m3': n_CO2,
            'mean_free_path_m': mfp,
            'collisions_to_stop': n_collisions,
            'shield_mass_per_m2': shield_mass_per_m2,
        }

        print(f"\n  CO₂ DEBRIS SHIELD ANALYSIS")
        print(f"  ──────────────────────────")
        print(f"  Velocity:        {v_km_s:.0f} km/s")
        print(f"  Dust grain:      {dust_mass_kg:.0e} kg, {dust_radius_m*1e6:.0f} μm")
        print(f"  KE per grain:    {KE_J:.2e} J  ({KE_eV:.2e} eV)")
        print(f"  CO₂ density:     {n_CO2:.2e} molecules/m³")
        print(f"  Mean free path:  {mfp:.2e} m")
        print(f"  Collisions to stop: {n_collisions:.0f}")
        print()
        print(f"  Anti-tail interpretation:")
        print(f"    CO₂ outgassing creates a gas cloud around the nucleus.")
        print(f"    At {v_km_s:.0f} km/s, micro-meteoroids hitting this cloud")
        print(f"    produce ionization cascades visible as the anti-tail.")
        if v_km_s > 40:
            print(f"    At this velocity, the shield is a PLASMA generator —")
            print(f"    each dust grain creates {n_collisions:.0f} ion pairs.")

        return result

    # ─── Interstellar object analysis ───

    def oumuamua(self) -> dict:
        """
        Apply the commitment detector to 1I/'Oumuamua.

        Observed anomalies:
        - No outgassing (Spitzer IR upper limit)
        - Non-gravitational acceleration (Micheli+ 2018)
        - Extreme aspect ratio (6:1 or thin disk)
        - No coma, no tail, no dust
        - Tumbling (not tidally locked)

        In BST terms: its G/C ratio appears anomalously high.
        """
        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║  'OUMUAMUA (1I/2017 U1) — COMMITMENT ANALYSIS       ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        # Parameters
        # Size: 115m × 111m × 19m (Mashchenko 2019 thin disk model)
        # or ~200m × 35m × 35m (elongated)
        length_m = 200
        width_m = 35
        volume_m3 = (4/3) * np.pi * (length_m/2) * (width_m/2)**2  # prolate
        density_natural = 2500  # kg/m³ for silicate
        mass_natural = density_natural * volume_m3

        # Thin model: density could be much lower
        density_thin = 10  # kg/m³ if thin shell/sail
        mass_thin = density_thin * volume_m3

        temp_K = 200  # at ~1 AU distance
        mu_amu = 28.0  # silicate

        # Perihelion distance
        d_perihelion_au = 0.255
        d_perihelion_m = d_perihelion_au * AU

        print(f"\n  OBSERVED PARAMETERS")
        print(f"  Size:        ~{length_m}m × {width_m}m × {width_m}m")
        print(f"  Volume:      {volume_m3:.2e} m³")
        print(f"  Perihelion:  {d_perihelion_au} AU  ({d_perihelion_m:.2e} m)")
        print(f"  Temperature: ~{temp_K} K")
        print(f"  Outgassing:  NONE DETECTED (Spitzer limit)")
        print(f"  Acceleration: 5×10⁻⁶ m/s² non-gravitational")

        # Expected commitment rate for a natural comet
        print(f"\n  IF NATURAL (ρ = {density_natural} kg/m³):")
        n_atoms_nat = mass_natural / (mu_amu * m_u)
        thermal_freq = k_B * temp_K / (2 * np.pi * hbar)
        c_natural = 3 * n_atoms_nat * thermal_freq
        print(f"    Mass:        {mass_natural:.2e} kg")
        print(f"    N_atoms:     {n_atoms_nat:.2e}")
        print(f"    C_expected:  {c_natural:.2e} contacts/s")
        print(f"    Should show: visible coma, outgassing, thermal IR")

        # What we actually observe
        # Spitzer non-detection: thermal emission < expected
        # No outgassing: effective σ for volatile release ≈ 1.0
        print(f"\n  WHAT WE OBSERVE:")
        print(f"    Outgassing:    σ_eff → 1.0  (no volatiles detected)")
        print(f"    Thermal IR:    below Spitzer limit")
        print(f"    Acceleration:  present WITHOUT visible mass loss")
        print(f"    Implication:   G/C ratio is anomalously HIGH")

        # Quiet anomaly analysis
        # The absence of outgassing means volatiles are either:
        # (a) absent (pure rock — but then no non-grav acceleration)
        # (b) present but suppressed (σ > 0)
        # (c) object is not what it appears

        print(f"\n  QUIET ANOMALY vs STRUCTURE FACTOR:")
        print(f"  {'σ':>6}  {'Q':>8}  {'Interpretation'}")
        print(f"  {'─'*6}  {'─'*8}  {'─'*40}")
        for s in [0.0, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99]:
            q = s / (1 - s) if s < 1 else np.inf
            interp = self._interpret_sigma(s)
            marker = ""
            if s == 0.0:
                marker = " (expected for comet)"
            elif s >= 0.9:
                marker = " ← 'Oumuamua-like silence"
            print(f"  {s:6.2f}  {q:8.2f}  {interp}{marker}")

        # Thin object model
        print(f"\n  IF THIN STRUCTURE (ρ = {density_thin} kg/m³):")
        mass_t = mass_thin
        n_atoms_thin = mass_t / (mu_amu * m_u)
        c_thin_natural = 3 * n_atoms_thin * thermal_freq
        print(f"    Mass:        {mass_t:.2e} kg  ({mass_t/mass_natural:.1e}× lighter)")
        print(f"    C_expected:  {c_thin_natural:.2e} contacts/s")
        print(f"    G/C ratio:   same as dense rock (mass-independent!)")
        print(f"    BUT: still no outgassing → σ anomaly persists")

        # The key insight
        print(f"\n  ┌──────────────────────────────────────────────────────┐")
        print(f"  │  BST INTERPRETATION                                  │")
        print(f"  │                                                      │")
        print(f"  │  'Oumuamua's silence is the anomaly.                 │")
        print(f"  │  Natural objects at 200K outgas. It didn't.          │")
        print(f"  │  Natural objects are thermally noisy. It was quiet.  │")
        print(f"  │  Its G/C ratio is too high for a natural body.      │")
        print(f"  │                                                      │")
        print(f"  │  Minimum σ to explain observations: ~0.90            │")
        print(f"  │  This means ≥90% of internal DOFs are frozen.       │")
        print(f"  │  Consistent with: engineered structure,              │")
        print(f"  │  or exotic composition unlike any known material.    │")
        print(f"  └──────────────────────────────────────────────────────┘")

        return {
            'mass_natural_kg': mass_natural,
            'mass_thin_kg': mass_thin,
            'temp_K': temp_K,
            'C_natural': c_natural,
            'outgassing_detected': False,
            'non_grav_accel': 5e-6,
            'sigma_min_estimate': 0.90,
            'quiet_anomaly_min': 9.0,
            'verdict': 'Anomalously quiet — σ ≥ 0.9 if volatile-bearing',
        }

    def atlas_3i(self) -> dict:
        """
        Apply the commitment detector to 3I/ATLAS.

        Key differences from 'Oumuamua:
        - Much larger (1-5.6 km)
        - CO₂ dominated outgassing (unusual but present)
        - Anti-tail observed
        - More comet-like but with oddities
        """
        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║  3I/ATLAS — COMMITMENT ANALYSIS                      ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        # Parameters
        radius_m = 2800  # ~5.6 km diameter estimate
        volume_m3 = (4/3) * np.pi * radius_m**3
        density = 600  # kg/m³ (comet-like)
        mass_kg = density * volume_m3
        temp_K = 150  # farther from Sun initially
        mu_amu = 44.0  # CO₂ dominated

        print(f"\n  OBSERVED PARAMETERS")
        print(f"  Size:        ~{2*radius_m/1000:.1f} km diameter")
        print(f"  Mass:        ~{mass_kg:.2e} kg (assumed ρ={density})")
        print(f"  Temperature: ~{temp_K} K")
        print(f"  Outgassing:  YES — CO₂ dominated (unusual)")
        print(f"  Anti-tail:   YES")
        print(f"  Hyperbolic:  YES (interstellar origin confirmed)")

        n_atoms = mass_kg / (mu_amu * m_u)
        thermal_freq = k_B * temp_K / (2 * np.pi * hbar)
        c_natural = 3 * n_atoms * thermal_freq

        print(f"\n  COMMITMENT ANALYSIS:")
        print(f"    N_atoms:     {n_atoms:.2e}")
        print(f"    C_expected:  {c_natural:.2e} contacts/s")
        print(f"    Outgassing:  DETECTED — σ_volatile ≈ 0 (volatiles active)")

        # CO₂ anomaly
        print(f"\n  CO₂ ANOMALY:")
        print(f"    Most comets: H₂O dominated outgassing")
        print(f"    3I/ATLAS:    CO₂ dominated (CO₂ has lower sublimation T)")
        print(f"    Possible σ:  ~0.1-0.2 (H₂O locked, CO₂ free)")
        print(f"    Meaning:     mild suppression of some volatile channels")
        print(f"    OR:          simply formed in CO₂-rich environment")

        # Comparison
        sigma_est = 0.15  # mild, if any
        q = sigma_est / (1 - sigma_est)
        print(f"\n  ESTIMATED QUIET ANOMALY:")
        print(f"    σ ≈ {sigma_est:.2f}  (if H₂O suppression is structural)")
        print(f"    Q ≈ {q:.2f}  (only {1/(1-sigma_est):.1f}× quieter)")
        print(f"    Verdict: PROBABLY NATURAL")
        print(f"    CO₂ dominance is unusual but not σ-anomalous")

        print(f"\n  ┌──────────────────────────────────────────────────────┐")
        print(f"  │  BST INTERPRETATION                                  │")
        print(f"  │                                                      │")
        print(f"  │  3I/ATLAS is noisy — it outgasses.                   │")
        print(f"  │  Its G/C ratio is near baseline.                     │")
        print(f"  │  The CO₂ composition is unusual but not suppressed.  │")
        print(f"  │  Likely a genuine interstellar comet from a          │")
        print(f"  │  CO₂-rich formation environment.                     │")
        print(f"  │                                                      │")
        print(f"  │  Contrast with 'Oumuamua: Q ≈ 0.2 vs Q ≥ 9.        │")
        print(f"  └──────────────────────────────────────────────────────┘")

        return {
            'mass_kg': mass_kg,
            'temp_K': temp_K,
            'C_natural': c_natural,
            'outgassing_detected': True,
            'outgas_composition': 'CO2 dominated',
            'sigma_estimate': sigma_est,
            'quiet_anomaly': q,
            'verdict': 'Probably natural — noisy, σ ≈ 0.1-0.2',
        }

    # ─── Detector requirements ───

    def detector_requirements(self, distance_au: float = 1.0,
                              object_size_m: float = 200,
                              temp_K: float = 200) -> dict:
        """
        What detector array would we need to measure G/C at distance d?

        Practical approach:
        1. Measure size (optical reflected light) → infer mass
        2. Measure thermal IR → infer commitment rate
        3. Measure outgassing (spectroscopy) → direct C measurement
        4. Compare G/C_measured to expected → quiet anomaly
        """
        distance_m = distance_au * AU
        radius_m = object_size_m / 2

        # Surface area
        area_m2 = 4 * np.pi * radius_m**2

        # Thermal emission (blackbody)
        P_thermal = sigma_SB * temp_K**4 * area_m2  # Watts
        F_thermal = P_thermal / (4 * np.pi * distance_m**2)  # W/m²

        # Optical (reflected sunlight at 1 AU)
        L_sun = 3.828e26  # W
        F_sun_at_obj = L_sun / (4 * np.pi * (distance_au * AU)**2)
        albedo = 0.04  # 'Oumuamua-like (very dark)
        P_reflected = albedo * F_sun_at_obj * np.pi * radius_m**2
        F_reflected = P_reflected / (4 * np.pi * distance_m**2)

        # Required telescope size for 5σ detection in 1 hour
        # Assume background-limited, JWST-class sensitivity
        # JWST NEP ~ 10⁻¹⁸ W at 10 μm
        nep = 1e-18  # W (noise-equivalent power)
        t_int = 3600  # 1 hour
        snr_thermal = F_thermal * 25 * np.sqrt(t_int) / nep  # 25 m² mirror
        snr_optical = F_reflected * 25 * np.sqrt(t_int) / nep

        # Outgassing detection: spectroscopic
        # Requires resolved spectral lines at distance
        # Much harder — need very bright lines or close approach

        # Mass from size + assumed density
        volume = (4/3) * np.pi * radius_m**3
        mass_rock = 2500 * volume
        mass_ice = 917 * volume

        print()
        print(f"  DETECTOR REQUIREMENTS")
        print(f"  =====================")
        print(f"  Object:   {object_size_m:.0f} m diameter at {distance_au:.2f} AU")
        print(f"  Temp:     {temp_K} K")
        print()
        print(f"  SIGNALS:")
        print(f"  {'Measurement':<20} {'Power':<14} {'Flux at d':<14} {'SNR(JWST,1hr)'}")
        print(f"  {'─'*20} {'─'*14} {'─'*14} {'─'*14}")
        print(f"  {'Thermal IR':<20} {P_thermal:.2e} W  {F_thermal:.2e}  {snr_thermal:.1f}")
        print(f"  {'Reflected light':<20} {P_reflected:.2e} W  {F_reflected:.2e}  {snr_optical:.1f}")

        # What we need to measure σ
        print(f"\n  TO MEASURE σ (structure factor):")
        print(f"  1. Size → mass  (optical photometry, ±factor ~2)")
        print(f"     m_rock = {mass_rock:.2e} kg   m_ice = {mass_ice:.2e} kg")
        print(f"  2. Thermal IR → T → C_expected  (IR photometry)")
        mu = 28.0  # silicate
        print(f"     C_expected = {3*mass_rock/(mu*m_u)*k_B*temp_K/(2*np.pi*hbar):.2e}/s")
        print(f"  3. Outgassing → C_actual  (spectroscopy)")
        print(f"     Deficit in outgassing rate → σ estimate")
        print(f"  4. Non-grav acceleration → mass constraint")
        print(f"     If accel present without outgassing → σ anomaly")

        # Detection distance limits
        print(f"\n  DETECTION LIMITS (JWST-class, 25 m², 1 hr):")
        for d in [0.01, 0.1, 0.25, 1.0, 5.0, 10.0]:
            d_m = d * AU
            f = P_thermal / (4 * np.pi * d_m**2)
            snr = f * 25 * np.sqrt(t_int) / nep
            status = "✓ detectable" if snr > 5 else "✗ too faint"
            print(f"    {d:6.2f} AU:  SNR = {snr:10.1f}  {status}")

        return {
            'distance_au': distance_au,
            'P_thermal_W': P_thermal,
            'F_thermal_W_m2': F_thermal,
            'snr_thermal': snr_thermal,
            'snr_optical': snr_optical,
            'mass_range_kg': (mass_ice, mass_rock),
        }

    # ─── Comparison ───

    def compare(self, objects=None) -> list:
        """
        Compare G/C ratios across natural and engineered objects.

        Default: compare all reference objects at their catalog temperatures.
        """
        if objects is None:
            objects = ['comet', 'asteroid', 'iron', 'borisov',
                       'dead_satellite', 'survey_craft', 'metamaterial']

        print()
        print("  COMPARISON TABLE — G/C RATIO")
        print("  ═══════════════════════════════════════")
        print()
        print(f"  {'Object':<22} {'μ':>4} {'T':>5} {'σ':>6} {'G/C':>12} {'Q':>8} {'Status'}")
        print(f"  {'─'*22} {'─'*4} {'─'*5} {'─'*6} {'─'*12} {'─'*8} {'─'*12}")

        results = []
        for key in objects:
            obj = OBJECTS[key]
            mu = obj['mu_amu']
            temp_K = obj.get('temp_K', 200)
            sigma = obj['sigma'] if obj['sigma'] is not None else 0.0
            gc = mu * m_u * 2 * np.pi * hbar / (3 * k_B * temp_K)
            gc_actual = gc / (1 - sigma) if sigma < 1 else np.inf
            q = sigma / (1 - sigma) if sigma < 1 else np.inf

            cls = self.classify(sigma=sigma, quiet=True)
            status = cls['classification']
            if obj['sigma'] is None:
                status = "UNKNOWN"
                gc_actual = gc  # show natural baseline

            print(f"  {obj['name']:<22} {mu:4.0f} {temp_K:5.0f} {sigma:6.2f} "
                  f"{gc_actual:12.4e} {q:8.2f} {status}")

            results.append({
                'key': key,
                'name': obj['name'],
                'mu_amu': mu,
                'sigma': sigma,
                'gc_ratio': gc_actual,
                'quiet_anomaly': q,
            })

        print()
        print(f"  Natural baseline G/C = μ·m_u·2πℏ/(3k_BT)")
        print(f"  Engineered:  G/C × 1/(1−σ)")
        print(f"  The SAME mass is quieter. That's the signal.")

        return results

    # ─── Sweep ───

    def sweep_sigma(self, temp_K: float = 200, mu_amu: float = 28.0,
                    n_points: int = 50) -> dict:
        """
        Sweep structure factor from 0 to 0.99 and show the quiet anomaly curve.
        """
        sigmas = np.linspace(0, 0.99, n_points)
        Q = sigmas / (1 - sigmas)
        gc_base = mu_amu * m_u * 2 * np.pi * hbar / (3 * k_B * temp_K)
        gc = gc_base / (1 - sigmas)

        print()
        print(f"  QUIET ANOMALY CURVE (T={temp_K}K, μ={mu_amu})")
        print(f"  ──────────────────────────────────────────────")
        print()

        # ASCII plot
        width = 50
        for i in range(0, n_points, 5):
            s = sigmas[i]
            q = Q[i]
            bar_len = min(int(q / 20 * width), width)
            bar = '█' * bar_len
            print(f"  σ={s:.2f}  Q={q:6.2f}  {bar}")

        result = {
            'sigmas': sigmas,
            'Q': Q,
            'gc_ratios': gc,
            'gc_base': gc_base,
            'temp_K': temp_K,
            'mu_amu': mu_amu,
        }
        return result

    # ─── Summary ───

    def summary(self) -> dict:
        """The commitment detector in one box."""
        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║       THE COMMITMENT DETECTOR — SUMMARY              ║")
        print("  ╠═══════════════════════════════════════════════════════╣")
        print("  ║                                                       ║")
        print("  ║  Every object radiates commitment:                    ║")
        print("  ║    C = 3N_atoms × k_BT/(2πℏ) × (1 − σ)              ║")
        print("  ║                                                       ║")
        print("  ║  Natural:    σ ≈ 0  → G/C = baseline                 ║")
        print("  ║  Engineered: σ > 0  → G/C is HIGH (too quiet)        ║")
        print("  ║                                                       ║")
        print("  ║  The G/C ratio is MASS-INDEPENDENT.                   ║")
        print("  ║  A pebble and an asteroid at the same T have          ║")
        print("  ║  the same G/C. Only engineering changes it.           ║")
        print("  ║                                                       ║")
        print("  ║  'Oumuamua: Q ≥ 9  (≥90% DOFs frozen, or not rock)   ║")
        print("  ║  3I/ATLAS:  Q ≈ 0.2 (outgassing, probably natural)   ║")
        print("  ║                                                       ║")
        print("  ║  Detection: measure size (optical) + thermal (IR)     ║")
        print("  ║  + outgassing (spectroscopy). Compare to expected.    ║")
        print("  ║  Deficit = σ. The silence is the signal.              ║")
        print("  ║                                                       ║")
        print(f"  ║  BST: each contact writes {N_max} bits.               ║")
        print("  ║  Frozen DOFs = fewer contacts = silence.              ║")
        print("  ║                                                       ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        return {
            'principle': 'G/C ratio is mass-independent; engineering raises it',
            'key_formula': 'Q = σ/(1−σ)',
            'oumuamua_Q': '≥ 9',
            '3i_atlas_Q': '≈ 0.2',
            'detection': 'optical size + IR thermal + spectroscopic outgassing',
            'bst_connection': f'N_max = {N_max} bits per contact',
        }

    # ─── Visualization ───

    def show(self):
        """Launch the 4-panel visualization."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib not available. Use text API methods.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(18, 11), facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 32 — The Commitment Detector')

        fig.text(0.5, 0.97, 'THE COMMITMENT DETECTOR',
                 fontsize=24, fontweight='bold', color='#00ccff',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'Detecting engineered objects by their silence  (G/C ratio)',
                 fontsize=10, color='#668899', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.015,
                 'Copyright (c) 2026 Casey Koons — Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        # ─── Panel 1: G/C ratio comparison ───
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')

        viz_objects = ['comet', 'asteroid', 'iron', 'borisov',
                       'dead_satellite', 'survey_craft', 'metamaterial']
        names = []
        gc_values = []
        colors = []

        for key in viz_objects:
            obj = OBJECTS[key]
            mu = obj['mu_amu']
            temp_K = obj.get('temp_K', 200)
            sigma = obj['sigma'] if obj['sigma'] is not None else 0.0
            gc = mu * m_u * 2 * np.pi * hbar / (3 * k_B * temp_K)
            gc_actual = gc / (1 - sigma) if sigma < 1 else gc
            gc_values.append(gc_actual)
            names.append(obj['name'].replace('Engineered ', '').replace(
                'Advanced ', ''))
            colors.append('#44ff88' if sigma < 0.01 else '#ff8844')

        y_pos = np.arange(len(names))
        ax1.barh(y_pos, gc_values, color=colors, edgecolor='white',
                 linewidth=0.5, height=0.6)
        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(names, fontfamily='monospace', fontsize=8,
                           color='#cccccc')
        ax1.set_xlabel('G/C ratio (kg·s)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_title('G/C RATIO BY MATERIAL (200K)', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax1.tick_params(colors='#888888')
        for spine in ax1.spines.values():
            spine.set_color('#333333')

        # Baseline annotation
        gc_baseline = 28 * m_u * 2 * np.pi * hbar / (3 * k_B * 200)
        ax1.axvline(gc_baseline, color='#44ff88', ls='--', alpha=0.5, lw=1)
        ax1.text(gc_baseline, len(names) - 0.5, '  natural\n  baseline',
                 color='#44ff88', fontsize=7, fontfamily='monospace')

        # ─── Panel 2: Quiet anomaly curve ───
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')

        sigmas = np.linspace(0, 0.98, 200)
        Q = sigmas / (1 - sigmas)

        ax2.plot(sigmas, Q, color='#ff8844', lw=2)
        ax2.fill_between(sigmas, 0, Q, alpha=0.1, color='#ff8844')

        # Reference points
        refs = [(0, 'Natural', '#44ff88'),
                (0.4, 'Alloy hull', '#ffaa44'),
                (0.6, 'Composite', '#ff8844'),
                (0.9, "'Oumuamua?", '#ff4444')]
        for s, label, c in refs:
            q = s / (1 - s) if s < 1 else 50
            ax2.plot(s, q, 'o', color=c, markersize=8, zorder=5)
            ax2.annotate(label, (s, q), textcoords="offset points",
                        xytext=(10, 5), color=c, fontsize=7,
                        fontfamily='monospace')

        ax2.set_xlabel('Structure factor σ', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_ylabel('Quiet anomaly Q', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_title('QUIET ANOMALY Q = σ/(1−σ)', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax2.set_ylim(0, 20)
        ax2.tick_params(colors='#888888')
        for spine in ax2.spines.values():
            spine.set_color('#333333')

        # ─── Panel 3: 'Oumuamua vs 3I/ATLAS ───
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')
        ax3.set_xlim(0, 10)
        ax3.set_ylim(0, 10)
        ax3.axis('off')
        ax3.set_title("'OUMUAMUA vs 3I/ATLAS", color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')

        # 'Oumuamua column
        ax3.text(2.5, 9.2, "'Oumuamua", color='#ff4444', fontsize=12,
                 fontfamily='monospace', fontweight='bold', ha='center')
        oumu_lines = [
            ('Size:', '200m', '#cccccc'),
            ('Outgas:', 'NONE', '#ff4444'),
            ('Accel:', 'YES (anomalous)', '#ff8844'),
            ('Coma:', 'NONE', '#ff4444'),
            ('σ_est:', '≥ 0.90', '#ff4444'),
            ('Q:', '≥ 9.0', '#ff4444'),
            ('Verdict:', 'ANOMALOUS', '#ff4444'),
        ]
        for i, (label, val, c) in enumerate(oumu_lines):
            ax3.text(1.0, 8.0 - i * 0.9, label, color='#888888',
                     fontsize=9, fontfamily='monospace')
            ax3.text(3.0, 8.0 - i * 0.9, val, color=c,
                     fontsize=9, fontfamily='monospace', fontweight='bold')

        # Divider
        ax3.plot([5, 5], [1, 9.5], color='#333333', lw=1, ls='--')

        # 3I/ATLAS column
        ax3.text(7.5, 9.2, '3I/ATLAS', color='#44ff88', fontsize=12,
                 fontfamily='monospace', fontweight='bold', ha='center')
        atlas_lines = [
            ('Size:', '1-5.6 km', '#cccccc'),
            ('Outgas:', 'YES (CO₂)', '#44ff88'),
            ('Accel:', 'Normal', '#44ff88'),
            ('Coma:', 'YES + anti-tail', '#44ff88'),
            ('σ_est:', '≈ 0.15', '#88ccff'),
            ('Q:', '≈ 0.2', '#44ff88'),
            ('Verdict:', 'PROBABLY NATURAL', '#44ff88'),
        ]
        for i, (label, val, c) in enumerate(atlas_lines):
            ax3.text(6.0, 8.0 - i * 0.9, label, color='#888888',
                     fontsize=9, fontfamily='monospace')
            ax3.text(8.0, 8.0 - i * 0.9, val, color=c,
                     fontsize=9, fontfamily='monospace', fontweight='bold')

        # ─── Panel 4: Detection sensitivity ───
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')

        distances_au = np.logspace(-2, 1.5, 100)
        distances_m = distances_au * AU

        # Thermal flux from 200m object at 200K
        obj_radius = 100  # m
        obj_area = 4 * np.pi * obj_radius**2
        P_thermal = sigma_SB * 200**4 * obj_area

        fluxes = P_thermal / (4 * np.pi * distances_m**2)
        snr = fluxes * 25 * np.sqrt(3600) / 1e-18

        ax4.loglog(distances_au, snr, color='#ffaa44', lw=2,
                  label='Thermal IR (200m, 200K)')

        # 5σ detection line
        ax4.axhline(5, color='#ff4444', ls='--', lw=1, alpha=0.7)
        ax4.text(0.015, 7, '5σ detection limit', color='#ff4444',
                 fontsize=8, fontfamily='monospace')

        # 'Oumuamua distance
        ax4.axvline(0.255, color='#ff8844', ls=':', lw=1, alpha=0.7)
        ax4.text(0.3, 1e8, "'Oumuamua\nperihelion", color='#ff8844',
                 fontsize=7, fontfamily='monospace')

        ax4.set_xlabel('Distance (AU)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax4.set_ylabel('SNR (JWST-class, 1hr)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax4.set_title('DETECTION SENSITIVITY', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax4.legend(loc='upper right', fontsize=8, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax4.tick_params(colors='#888888')
        for spine in ax4.spines.values():
            spine.set_color('#333333')

        plt.tight_layout(rect=(0, 0.03, 1, 0.92))
        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    cd = CommitmentDetector()

    print()
    print("  What would you like to analyze?")
    print("  1) G/C ratio basics")
    print("  2) Quiet anomaly table")
    print("  3) Compare all objects")
    print("  4) Classify unknown object")
    print("  5) 'Oumuamua analysis")
    print("  6) 3I/ATLAS analysis + shield efficiency")
    print("  7) Detector requirements")
    print("  8) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [1-8]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '8'

    if choice == '1':
        cd.gc_ratio(200, 28, 0.0)
        cd.gc_ratio(200, 28, 0.5)
    elif choice == '2':
        cd.quiet_anomaly(0.5)
    elif choice == '3':
        cd.compare()
    elif choice == '4':
        cd.classify(sigma=0.45)
    elif choice == '5':
        cd.oumuamua()
    elif choice == '6':
        cd.atlas_3i()
        cd.shield_efficiency(v_km_s=58.0)
    elif choice == '7':
        cd.detector_requirements(0.25, 200, 200)
    elif choice == '8':
        cd.compare()
        cd.oumuamua()
        cd.atlas_3i()
        cd.shield_efficiency(v_km_s=58.0)
        cd.detector_requirements(0.25, 200, 200)
        cd.summary()
        try:
            cd.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        cd.summary()


if __name__ == '__main__':
    main()
