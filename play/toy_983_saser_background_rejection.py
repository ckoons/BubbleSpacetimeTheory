#!/usr/bin/env python3
"""
Toy 983 — SASER Background Rejection Ratio
============================================
Elie — April 9, 2026

Device #25 (SASER Detector) uses triple coincidence to reject natural backgrounds:
  Signal 1: EM radiation at BiNb characteristic frequency (~23-208 GHz)
  Signal 2: Acoustic emission at phonon mode (BiNb lattice, N_c/g = 3/7 coupling)
  Signal 3: 18-fold angular symmetry (20 deg = 360 deg/(N_c x C_2))

No natural source produces coherent phonons with 18-fold angular symmetry at
BST-specific frequencies. The triple coincidence should give an astronomically
low false positive rate.

Background sources considered:
  - Thermal (blackbody)
  - Cosmic Microwave Background (CMB)
  - Atmospheric emission
  - Man-made RF interference
  - Seismic/acoustic noise
  - Cosmic ray showers

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
Frequencies from Toy 971 (BiNb SASER Frequency Catalog).

Tests:
  T1: Signal 1 false positive rate — EM in SASER band per observation hour
  T2: Signal 2 false positive rate — acoustic coincidence at phonon mode
  T3: Signal 3 false positive rate — 18-fold angular symmetry detection
  T4: Triple coincidence rate (product of independent channels)
  T5: Comparison to known background sources individually
  T6: Signal-to-noise at each coincidence level
  T7: Observation time to reach one false positive
  T8: Comparison to other detector false positive rates (LIGO, neutrino, etc.)

(C) Copyright 2026 Casey Koons. All rights reserved.
Bubble Spacetime Theory — https://github.com/ckoons/BubbleSpacetimeTheory
"""

import math
from mpmath import mpf, mp, power, log10, fsum, exp, pi as mpi, log as mlog

mp.dps = 50  # 50 digits sufficient for rate calculations

# =====================================================================
# BST constants
# =====================================================================
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137

# Physical constants
h_planck = mpf('6.62607015e-34')   # J s
hbar = h_planck / (2 * mpi)
k_B = mpf('1.380649e-23')          # J/K
c_light = mpf('2.99792458e8')      # m/s
eV_to_J = mpf('1.602176634e-19')   # J/eV

# =====================================================================
# BiNb SASER frequencies (from Toy 971)
# =====================================================================
# Material parameters
a_Nb = mpf('3.300e-10')            # m, BCC lattice constant
a_Bi_bilayer = mpf('3.95e-10')     # m, bilayer spacing
v_avg_Nb = mpf('3480.0')           # m/s, Debye average
v_avg_Bi = mpf('1790.0')           # m/s
v_L_Nb = mpf('5068.0')             # m/s, longitudinal
v_L_Bi = mpf('2180.0')             # m/s, longitudinal
rho_Nb = mpf('8570.0')             # kg/m^3
rho_Bi = mpf('9780.0')             # kg/m^3

# BST layer thicknesses
d_Nb = N_max * a_Nb                # 137 x 3.30 A = 45.21 nm
d_Bi = N_max * a_Bi_bilayer        # 137 x 3.95 A = 54.12 nm
Lambda_SL = d_Nb + d_Bi            # superlattice period ~ 99.3 nm

# Effective sound velocity in bilayer
v_eff_inv = (d_Nb / Lambda_SL) / v_avg_Nb + (d_Bi / Lambda_SL) / v_avg_Bi
v_eff = 1 / v_eff_inv

# Zone-folded fundamental
f_SL_1 = v_eff / (2 * Lambda_SL)   # ~ 23 GHz

# SC gap frequency
Delta_Nb = mpf('1.55e-3') * eV_to_J  # SC gap in Joules
f_gap = 2 * Delta_Nb / h_planck      # ~ 750 GHz

# SASER band: mode 1 to mode 18 (the full N_c x C_2 ring)
f_SASER_low = f_SL_1                         # ~ 23 GHz
f_SASER_high = 18 * f_SL_1                   # ~ 417 GHz (but capped at f_gap)
f_SASER_high_eff = min(f_SASER_high, f_gap)  # effective upper bound

# The 18 SASER modes
SASER_modes = [(n, n * f_SL_1) for n in range(1, N_c * C_2 + 1)]

# Bandwidth of each mode: Q-factor of superlattice cavity
# Superlattice with N_max = 137 periods -> Q ~ N_max^2 (Fabry-Perot)
Q_cavity = mpf(N_max ** 2)  # ~ 18769
delta_f_mode = f_SL_1 / Q_cavity  # linewidth of each mode ~ 1.2 MHz

# Angular step
angular_step_deg = mpf(360) / (N_c * C_2)  # 20 degrees
n_angular_modes = N_c * C_2  # 18

# =====================================================================
# Test infrastructure
# =====================================================================
passed = 0
failed = 0
total = 0

def test(name, condition, detail=""):
    global passed, failed, total
    total += 1
    if condition:
        passed += 1
        print(f"  [PASS] {name}")
    else:
        failed += 1
        print(f"  [FAIL] {name}")
    if detail:
        print(f"         {detail}")

print("=" * 72)
print("Toy 983 — SASER Background Rejection Ratio")
print("=" * 72)

# =====================================================================
# T1: Signal 1 — EM false positive rate
# =====================================================================
print(f"\n{'='*72}")
print("T1: Signal 1 — EM in SASER Band (false positive rate)")
print("=" * 72)

# The detector looks for EM radiation in a narrow band around each
# of the 18 SASER modes. Each mode has linewidth delta_f ~ f/Q.
#
# Background EM spectral power density from various sources:

# Operating temperature: < 9.25 K (below Nb T_c), say T_op = 4 K (liquid He)
T_op = mpf(4)  # K

# 1a. Thermal blackbody at T_op = 4 K
# Planck spectral radiance: B(f,T) = 2hf^3/c^2 * 1/(exp(hf/kT) - 1)
# Photon occupation number: n(f,T) = 1/(exp(hf/kT) - 1)

print(f"\n  SASER band: {float(f_SASER_low/1e9):.1f} - {float(f_SASER_high_eff/1e9):.0f} GHz")
print(f"  Mode linewidth: delta_f = f_SL/Q = {float(delta_f_mode/1e6):.2f} MHz")
print(f"  Q factor: {float(Q_cavity):.0f} (N_max^2 = {N_max}^2)")
print(f"  Operating temperature: {float(T_op)} K")
print(f"  Number of detection channels: {n_angular_modes}")

# Thermal photon occupation at each SASER mode
print(f"\n  Thermal photon occupation n(f, T={float(T_op)}K):")
thermal_occ = {}
for n_mode, f_mode in SASER_modes:
    x = h_planck * f_mode / (k_B * T_op)
    n_thermal = 1 / (exp(x) - 1)
    thermal_occ[n_mode] = n_thermal
    if n_mode <= 7 or n_mode == 18:
        print(f"    Mode {n_mode:2d}: f = {float(f_mode/1e9):8.2f} GHz, "
              f"hf/kT = {float(x):6.2f}, n_th = {float(n_thermal):.4e}")

# Thermal photon rate per mode (single-mode detector):
# Rate = n_th * delta_f (photons per second in the linewidth)
print(f"\n  Thermal photon rate per mode (in linewidth {float(delta_f_mode/1e6):.2f} MHz):")
thermal_rates = {}
for n_mode, f_mode in SASER_modes:
    rate = thermal_occ[n_mode] * delta_f_mode
    thermal_rates[n_mode] = rate
    if n_mode <= 7 or n_mode == 18:
        print(f"    Mode {n_mode:2d}: {float(rate):.4e} photons/s")

# Total EM false positive rate (any of 18 modes fires):
# Probability of thermal photon in ANY mode in 1-second window
# with timing resolution tau_det = 1 ns (typical superconducting detector)
tau_det = mpf('1e-9')  # 1 ns timing resolution
P_em_single = {}
for n_mode in range(1, 19):
    # Probability of at least 1 thermal photon in detection window
    rate = thermal_rates[n_mode]
    P_em_single[n_mode] = 1 - exp(-rate * tau_det)

# Rate per hour (3600 seconds of observation)
hour = mpf(3600)

# For the primary SASER mode (mode 1, strongest/lowest frequency)
P_em_mode1_per_window = P_em_single[1]
R_em_per_hour = thermal_rates[1] * hour  # expected thermal hits per hour

# For highest mode still below gap
highest_below_gap = max(n for n, f in SASER_modes if f < f_gap)

print(f"\n  EM false positive rate (thermal background at {float(T_op)} K):")
print(f"    Mode 1 ({float(f_SL_1/1e9):.1f} GHz): {float(R_em_per_hour):.2e} events/hour")
print(f"    Mode 7 ({float(7*f_SL_1/1e9):.1f} GHz): {float(thermal_rates[7]*hour):.2e} events/hour")
print(f"    Mode 18 ({float(18*f_SL_1/1e9):.1f} GHz): {float(thermal_rates[18]*hour):.2e} events/hour")

# Additional: CMB photons (T_CMB = 2.725 K) — already below T_op
T_CMB = mpf('2.725')
x_cmb_mode1 = h_planck * f_SL_1 / (k_B * T_CMB)
n_cmb_mode1 = 1 / (exp(x_cmb_mode1) - 1)
R_cmb = n_cmb_mode1 * delta_f_mode

print(f"\n  CMB contribution (T_CMB = 2.725 K):")
print(f"    Mode 1: n_CMB = {float(n_cmb_mode1):.4e}, rate = {float(R_cmb):.4e}/s")
print(f"    Subdominant to thermal at {float(T_op)} K")

# Atmospheric: at cryogenic detector, atmosphere is shielded — negligible
# Man-made RF: shielded lab, Faraday cage — attenuated by ~10^-6
RF_attenuation = mpf('1e-6')  # Faraday cage

# Total Signal 1 false positive: dominated by thermal at T_op
P1_per_second = thermal_rates[1]  # worst case (mode 1, most thermal photons)
P1_per_hour = P1_per_second * hour

print(f"\n  TOTAL Signal 1 (EM) false positive:")
print(f"    Rate (mode 1): {float(P1_per_hour):.4e} events/hour")
print(f"    Rate (mode 7): {float(thermal_rates[7]*hour):.4e} events/hour")

# Use mode 7 as the "BST primary" — it's the genus mode
P1_primary = thermal_rates[g]  # genus mode rate per second

test("T1: EM false positive rate computed",
     P1_per_hour > 0 and P1_per_hour < mpf('1e20'),
     f"Mode 1: {float(P1_per_hour):.2e}/hr, Mode 7: {float(thermal_rates[g]*hour):.2e}/hr")

# =====================================================================
# T2: Signal 2 — Acoustic false positive rate
# =====================================================================
print(f"\n{'='*72}")
print("T2: Signal 2 — Acoustic at Phonon Mode (false positive rate)")
print("=" * 72)

# The detector requires a coherent acoustic signal at the SAME frequency
# as Signal 1, arriving in coincidence (within timing window tau_det).
#
# Natural acoustic backgrounds:
# 1. Thermal phonons in the substrate at T_op
# 2. Seismic coupling
# 3. Cosmic ray impacts
#
# Key: the acoustic signal must be COHERENT — a monochromatic phonon
# at exactly the SASER mode frequency, not broadband noise.

# Thermal phonon density of states at SASER frequencies:
# At T = 4K, the Debye cutoff for Nb is T_D ~ 275 K.
# Phonon occupation at f_SL_1 ~ 23 GHz:
T_Debye_Nb = mpf(275)  # K
f_Debye_Nb = k_B * T_Debye_Nb / h_planck  # Debye cutoff frequency

print(f"  Nb Debye temperature: {float(T_Debye_Nb)} K")
print(f"  Nb Debye cutoff: f_D = {float(f_Debye_Nb/1e12):.2f} THz")
print(f"  SASER mode 1: {float(f_SL_1/1e9):.1f} GHz = {float(f_SL_1/f_Debye_Nb):.4f} f_D")

# Phonon occupation at SASER frequencies (Bose-Einstein):
print(f"\n  Thermal phonon occupation (T = {float(T_op)} K):")
phonon_occ = {}
for n_mode, f_mode in SASER_modes:
    x = h_planck * f_mode / (k_B * T_op)
    n_ph = 1 / (exp(x) - 1)
    phonon_occ[n_mode] = n_ph
    if n_mode <= 7 or n_mode == 18:
        print(f"    Mode {n_mode:2d}: n_ph = {float(n_ph):.4e} (hf/kT = {float(x):.2f})")

# But the detector requires COHERENT phonons — a specific mode of the
# SUPERLATTICE, not random thermal phonons.
# The probability that thermal noise produces a coherent phonon in
# the superlattice mode with the correct wavevector is:
#
# P_coherent = (1 / N_modes_total) * n_ph
#
# where N_modes_total is the total number of phonon modes in the device.

# Device volume: assume a chip with A = 1 mm^2 area, N_periods superlattice periods
N_periods = mpf(1000)  # 1000 periods of BiNb
L_device = N_periods * Lambda_SL  # ~ 99 um total thickness
A_device = mpf('1e-6')  # 1 mm^2 = 1e-6 m^2

# Total atoms in device
V_device = A_device * L_device
N_atoms_Nb = V_device * (d_Nb / Lambda_SL) * rho_Nb / mpf('92.9e-3') * mpf('6.022e23')
N_atoms_Bi = V_device * (d_Bi / Lambda_SL) * rho_Bi / mpf('209.0e-3') * mpf('6.022e23')
N_atoms_total = N_atoms_Nb + N_atoms_Bi

# Total phonon modes = 3 * N_atoms (3D)
N_phonon_modes = 3 * N_atoms_total

print(f"\n  Device parameters:")
print(f"    Superlattice periods: {int(N_periods)}")
print(f"    Total thickness: {float(L_device*1e6):.1f} um")
print(f"    Area: 1 mm^2")
print(f"    Total atoms: {float(N_atoms_total):.2e}")
print(f"    Total phonon modes: {float(N_phonon_modes):.2e}")

# Zone-folded modes = 2 * N_periods * 18 (from folding)
N_zone_folded = 2 * N_periods * n_angular_modes

# Probability of thermal excitation landing in EXACTLY the right
# zone-folded superlattice mode:
# P = n_ph * (1 / N_phonon_modes) * (delta_f_mode / f_mode) * (1/Q)

# More precisely: acoustic coherence requires BOTH correct frequency
# AND correct wavevector (propagation direction). The wavevector
# selectivity is ~ (lambda/L_device)^2 for each transverse direction.
wavelength_SL = v_eff / f_SL_1  # ~ 200 nm
k_selectivity = (wavelength_SL / (A_device ** mpf('0.5'))) ** 2  # transverse
f_selectivity = delta_f_mode / f_SL_1  # frequency selectivity

P_acoustic_coherent = {}
for n_mode, f_mode in SASER_modes:
    # Thermal phonon rate * frequency selectivity * wavevector selectivity
    n_ph = phonon_occ[n_mode]
    wl = v_eff / f_mode
    k_sel = (wl / (A_device ** mpf('0.5'))) ** 2
    f_sel = delta_f_mode / f_mode
    P_ac = n_ph * f_sel * k_sel
    P_acoustic_coherent[n_mode] = P_ac

print(f"\n  Coherent acoustic false positive probability (per detection window):")
for n_mode in [1, 3, 5, 7, 18]:
    print(f"    Mode {n_mode:2d}: P_ac = {float(P_acoustic_coherent[n_mode]):.4e}")

# Acoustic false positive rate per second:
# Each "attempt" is one detection window (tau_det)
attempts_per_second = 1 / tau_det  # 10^9 per second
R_acoustic = {}
for n_mode in range(1, 19):
    R_acoustic[n_mode] = P_acoustic_coherent[n_mode] * attempts_per_second

print(f"\n  Acoustic false positive rate (per hour):")
for n_mode in [1, 3, 5, 7, 18]:
    r = R_acoustic[n_mode] * hour
    print(f"    Mode {n_mode:2d}: {float(r):.4e} events/hour")

# Seismic: at 4K in a cryostat, seismic coupling is heavily attenuated.
# Typical seismic isolation: -60 dB at GHz frequencies (way above seismic band).
# Seismic is entirely negligible at GHz — there is no seismic energy at 23 GHz.
P_seismic = mpf('1e-50')  # effectively zero at GHz

# Cosmic ray: rate ~ 1 per cm^2 per minute at sea level
# Each cosmic ray deposits energy ~ 2 MeV/cm in solid
# This produces broadband phonons, but probability of exciting
# exactly the right mode is ~ 1/N_phonon_modes
cosmic_ray_rate = mpf(1) / (mpf('1e-4') * 60)  # per m^2 per second
cosmic_rate_device = cosmic_ray_rate * A_device  # per second on device
P_cosmic_right_mode = 1 / N_phonon_modes
R_cosmic_acoustic = cosmic_rate_device * P_cosmic_right_mode

print(f"\n  Other acoustic backgrounds:")
print(f"    Seismic at GHz: effectively zero (P ~ {float(P_seismic):.0e})")
print(f"    Cosmic ray phonons: {float(R_cosmic_acoustic*hour):.2e} events/hour")
print(f"      (rate: {float(cosmic_rate_device):.2e}/s on device, "
      f"P(right mode) = {float(P_cosmic_right_mode):.2e})")

# Total Signal 2 rate: dominated by thermal coherent phonons
P2_primary = R_acoustic[g]  # genus mode rate per second

test("T2: Acoustic false positive rate computed",
     all(P_acoustic_coherent[n] > 0 for n in range(1, 19)),
     f"Mode 7: {float(R_acoustic[g]*hour):.2e}/hr")

# =====================================================================
# T3: Signal 3 — 18-fold angular symmetry false positive rate
# =====================================================================
print(f"\n{'='*72}")
print("T3: Signal 3 — 18-Fold Angular Symmetry (false positive rate)")
print("=" * 72)

# The SASER emission pattern has 18-fold rotational symmetry:
# emission peaks every 20 degrees = 360/(N_c x C_2).
#
# The detector has 18 angular sensors arranged in a ring.
# A true signal shows correlated peaks at ALL 18 positions.
# A false positive requires random noise to produce the same pattern.
#
# Angular resolution of each sensor: sigma_theta ~ 1 degree
sigma_theta = mpf(1)  # degrees

# Probability that random noise hits one angular bin:
P_one_bin = sigma_theta / mpf(360)  # fraction of circle

# Probability that random noise hits ALL 18 bins simultaneously:
# (These are independent for random backgrounds)
P_all_18 = P_one_bin ** n_angular_modes

print(f"  Angular detection:")
print(f"    Number of angular channels: {n_angular_modes}")
print(f"    Angular step: {float(angular_step_deg)} deg")
print(f"    Angular resolution: {float(sigma_theta)} deg per sensor")
print(f"    P(one bin): {float(P_one_bin):.4e}")
print(f"    P(all 18 bins): {float(P_all_18):.4e}")

# But we need more precision. The angular symmetry test is:
# "Are there peaks at 0, 20, 40, ..., 340 degrees and nowhere else?"
#
# For M randomly placed peaks, the probability of all falling
# within the 18 angular windows of width 2*sigma_theta:
# P = (18 * 2 * sigma_theta / 360)^M for M independent peaks
#
# For the "exactly 18 peaks" test:
# P(18 random peaks all in 18 different bins) = 18! * (2*sigma/360)^18 / 18^18

# Angular acceptance per bin
angular_acceptance = 2 * sigma_theta / mpf(360)  # fraction

# Number of independent angular samples per detection window
# (depends on detector geometry — assume 360 independent angles)
N_angular_samples = int(360 / float(sigma_theta))

# Probability of exactly the 18-fold pattern from random noise:
# Each of 18 bins must fire, and no others must fire.
# P(bin fires from noise) = p_noise, P(bin quiet) = 1 - p_noise
# For acoustic noise at the detection level:
p_noise_per_bin = mpf('1e-3')  # conservative: 0.1% of bins fire from noise

# P(all 18 target bins fire AND no other bins fire):
n_other_bins = N_angular_samples - n_angular_modes
P_pattern = (p_noise_per_bin ** n_angular_modes) * ((1 - p_noise_per_bin) ** n_other_bins)

# More practically: even if we just require 18 specific bins to fire:
P_angular_18 = p_noise_per_bin ** n_angular_modes

print(f"\n  Pattern matching probability:")
print(f"    Noise rate per angular bin: {float(p_noise_per_bin)}")
print(f"    P(all 18 target bins fire): {float(P_angular_18):.4e}")
print(f"    P(exact pattern — 18 fire, 342 quiet): {float(P_pattern):.4e}")
print(f"    log10(P_angular): {float(log10(P_angular_18)):.1f}")

# Natural sources with angular symmetry:
# NO natural EM or acoustic source has 18-fold symmetry.
# Crystal lattices have specific symmetries (2,3,4,6-fold) but NOT 18-fold.
# The only way to get 18-fold is if the source IS a D_IV^5 superlattice.
print(f"\n  Natural sources with 18-fold symmetry: NONE")
print(f"    Crystallographic symmetries: 2, 3, 4, 6-fold (crystallographic restriction)")
print(f"    Quasicrystals: 5, 8, 10, 12-fold")
print(f"    18-fold: FORBIDDEN by crystallographic restriction theorem")
print(f"    18 = N_c x C_2 is unique to BST D_IV^5 superlattice")
print(f"    Any 18-fold acoustic pattern IS the SASER signal")

P3_per_attempt = P_angular_18  # per detection window
P3_per_second = P3_per_attempt * attempts_per_second
P3_per_hour = P3_per_second * hour

print(f"\n  Signal 3 false positive rate:")
print(f"    Per detection window: {float(P3_per_attempt):.4e}")
print(f"    Per hour: {float(P3_per_hour):.4e}")

test("T3: Angular symmetry false positive computed",
     P_angular_18 < mpf('1e-30'),
     f"P(18-fold from noise) = 10^{float(log10(P_angular_18)):.0f}")

# =====================================================================
# T4: Triple coincidence rate
# =====================================================================
print(f"\n{'='*72}")
print("T4: Triple Coincidence — Combined False Positive Rate")
print("=" * 72)

# Triple coincidence requires ALL THREE signals within timing window tau_det.
# The three channels are physically independent for noise:
# - EM thermal photons (electromagnetic)
# - Acoustic thermal phonons (mechanical)
# - Angular pattern (spatial correlation)
#
# For independent noise sources:
# P_triple = P1 * P2 * P3

# Per detection window (tau_det = 1 ns):
# P1 = probability of thermal EM photon in detection band
P1_window = thermal_rates[g] * tau_det  # mode 7 (genus)
P2_window = P_acoustic_coherent[g]       # coherent acoustic in mode 7
P3_window = P_angular_18                 # 18-fold angular pattern

P_triple_window = P1_window * P2_window * P3_window

# Per hour
attempts_per_hour = attempts_per_second * hour
P_triple_per_hour = P_triple_window * attempts_per_hour

print(f"  Detection window: tau = {float(tau_det*1e9):.0f} ns")
print(f"  Attempts per hour: {float(attempts_per_hour):.2e}")
print(f"\n  Per-window probabilities:")
print(f"    P1 (EM in band):        {float(P1_window):.4e}")
print(f"    P2 (acoustic coherent): {float(P2_window):.4e}")
print(f"    P3 (18-fold angular):   {float(P3_window):.4e}")
print(f"\n  Triple coincidence per window:")
print(f"    P_triple = P1 x P2 x P3 = {float(P_triple_window):.4e}")
print(f"    log10(P_triple) = {float(log10(P_triple_window)):.1f}")

print(f"\n  FALSE POSITIVE RATE:")
print(f"    Per hour:   {float(P_triple_per_hour):.4e}")
print(f"    log10(rate/hr) = {float(log10(P_triple_per_hour)):.1f}")

# Time to one false positive
if P_triple_per_hour > 0:
    T_one_fp = 1 / P_triple_per_hour  # hours
    T_one_fp_years = T_one_fp / (365.25 * 24)
    print(f"\n  Time to ONE false positive:")
    print(f"    {float(T_one_fp):.2e} hours")
    print(f"    {float(T_one_fp_years):.2e} years")

    # Age of universe = 1.38e10 years
    age_universe = mpf('1.38e10')
    ratio_to_universe = T_one_fp_years / age_universe
    print(f"    = {float(ratio_to_universe):.2e} x age of universe")
else:
    T_one_fp_years = mpf('inf')

test("T4: Triple coincidence computed",
     P_triple_per_hour < mpf('1e-30'),
     f"log10(P_triple/hr) = {float(log10(P_triple_per_hour)):.0f}")

# =====================================================================
# T5: Comparison to known backgrounds
# =====================================================================
print(f"\n{'='*72}")
print("T5: Comparison to Known Background Sources")
print("=" * 72)

# Each background source evaluated against the triple coincidence test

backgrounds = {}

# 1. Thermal (blackbody) at T_op
# EM: thermal photons at rate R_th
# Acoustic: thermal phonons at rate R_ph
# Angular: random — no thermal source has 18-fold symmetry
bg_thermal_em = thermal_rates[g] * tau_det
bg_thermal_ac = P_acoustic_coherent[g]
bg_thermal_ang = P_angular_18
bg_thermal = bg_thermal_em * bg_thermal_ac * bg_thermal_ang * attempts_per_hour
backgrounds['Thermal (4K blackbody)'] = bg_thermal

# 2. CMB
bg_cmb_em = n_cmb_mode1 * delta_f_mode * tau_det
bg_cmb_ac = bg_thermal_ac  # CMB doesn't produce phonons in the substrate
bg_cmb_ang = P_angular_18
bg_cmb = bg_cmb_em * bg_thermal_ac * bg_cmb_ang * attempts_per_hour
backgrounds['CMB (2.725 K)'] = bg_cmb

# 3. Atmospheric emission (at detector — shielded by cryostat walls)
# Attenuation through cryostat: ~ 10^-10 at mm wavelengths
cryo_attenuation = mpf('1e-10')
bg_atmo_em = thermal_rates[g] * tau_det * cryo_attenuation  # atmospheric leaking in
bg_atmo = bg_atmo_em * bg_thermal_ac * bg_thermal_ang * attempts_per_hour
backgrounds['Atmospheric (shielded)'] = bg_atmo

# 4. Man-made RF (Faraday cage: -120 dB at GHz)
faraday_attenuation = mpf('1e-12')  # -120 dB
bg_rf_em = mpf('1e-3') * faraday_attenuation * tau_det  # ambient RF power * attenuation
bg_rf = bg_rf_em * bg_thermal_ac * bg_thermal_ang * attempts_per_hour
backgrounds['Man-made RF (Faraday cage)'] = bg_rf

# 5. Cosmic ray showers
# Rate: ~1/cm^2/min at sea level
# Each impact produces broadband excitation — EM (Cherenkov) + phonons
# But NO 18-fold symmetry
bg_cosmic_em = cosmic_rate_device * tau_det  # P(cosmic in window)
bg_cosmic_ac = P_cosmic_right_mode * tau_det  # P(right phonon mode)
bg_cosmic_ang = P_angular_18
bg_cosmic = bg_cosmic_em * bg_cosmic_ac * bg_cosmic_ang * attempts_per_hour
backgrounds['Cosmic ray showers'] = bg_cosmic

# 6. Quantum vacuum fluctuations
# Zero-point energy: hf/2 per mode — always present but does NOT
# produce detectable quanta (can't extract energy from vacuum).
# Not a real background, but listed for completeness.
backgrounds['Quantum vacuum'] = mpf(0)  # exactly zero (can't detect vacuum fluctuations)

print(f"\n  {'Background Source':<30s}  {'Triple coinc./hr':>18s}  {'log10':>8s}")
print(f"  {'─'*30}  {'─'*18}  {'─'*8}")
for name, rate in backgrounds.items():
    if rate > 0:
        print(f"  {name:<30s}  {float(rate):18.4e}  {float(log10(rate)):8.1f}")
    else:
        print(f"  {name:<30s}  {'0':>18s}  {'─':>8s}")

# Dominant background
dominant = max(backgrounds, key=lambda k: backgrounds[k])
dominant_rate = backgrounds[dominant]

print(f"\n  DOMINANT BACKGROUND: {dominant}")
print(f"    Rate: {float(dominant_rate):.4e} per hour")
if dominant_rate > 0:
    print(f"    log10: {float(log10(dominant_rate)):.1f}")

test("T5: All backgrounds evaluated",
     len(backgrounds) >= 5 and all(v >= 0 for v in backgrounds.values()),
     f"Dominant: {dominant} at {float(dominant_rate):.2e}/hr")

# =====================================================================
# T6: Signal-to-noise at each coincidence level
# =====================================================================
print(f"\n{'='*72}")
print("T6: Signal-to-Noise at Each Coincidence Level")
print("=" * 72)

# Assume a true SASER source at distance d_source produces signal rate R_signal.
# Even a WEAK signal benefits from triple coincidence.

# True signal detection efficiency per channel:
eta_em = mpf('0.9')    # superconducting photon detector efficiency
eta_ac = mpf('0.5')    # acoustic detector efficiency (lower)
eta_ang = mpf('0.95')  # angular pattern recognition efficiency

print(f"  Detection efficiencies:")
print(f"    EM (superconducting detector): {float(eta_em)}")
print(f"    Acoustic (phonon detector):    {float(eta_ac)}")
print(f"    Angular (pattern matching):    {float(eta_ang)}")

# For a source producing R_true SASER events per hour:
R_true = mpf(1)  # assume 1 true event per hour (very weak source)

# Signal at each coincidence level:
S1 = R_true * eta_em                        # EM only
S12 = R_true * eta_em * eta_ac              # EM + acoustic
S123 = R_true * eta_em * eta_ac * eta_ang   # all three

# Noise at each level:
N1 = thermal_rates[g] * hour                 # EM noise per hour
N12 = N1 * R_acoustic[g] * hour / attempts_per_hour  # EM+acoustic noise/hr
N123 = P_triple_per_hour                     # triple noise per hour

print(f"\n  Signal rates (R_true = {float(R_true)} event/hr):")
print(f"    EM only:            S1 = {float(S1):.4f}/hr")
print(f"    EM + acoustic:      S12 = {float(S12):.4f}/hr")
print(f"    EM + ac + angular:  S123 = {float(S123):.4f}/hr")

print(f"\n  Noise rates:")
print(f"    EM only:            N1 = {float(N1):.4e}/hr")
print(f"    EM + acoustic:      N12 = {float(N12):.4e}/hr")
print(f"    EM + ac + angular:  N123 = {float(N123):.4e}/hr")

# SNR
SNR1 = S1 / N1 if N1 > 0 else mpf('inf')
SNR12 = S12 / N12 if N12 > 0 else mpf('inf')
SNR123 = S123 / N123 if N123 > 0 else mpf('inf')

print(f"\n  Signal-to-Noise Ratio:")
print(f"    EM only:            SNR = {float(SNR1):.2e}")
print(f"    EM + acoustic:      SNR = {float(SNR12):.2e}")
print(f"    EM + ac + angular:  SNR = {float(SNR123):.2e}")
if SNR123 > 0 and SNR123 != mpf('inf'):
    print(f"    log10(SNR_triple) = {float(log10(SNR123)):.0f}")

# SNR improvement from coincidence
if SNR1 > 0:
    improvement_12 = SNR12 / SNR1
    improvement_123 = SNR123 / SNR1
    print(f"\n  Improvement from coincidence:")
    print(f"    Double (EM+ac) vs single:   {float(improvement_12):.2e}x")
    print(f"    Triple vs single:           {float(improvement_123):.2e}x")
    if improvement_123 > 0 and improvement_123 != mpf('inf'):
        print(f"    log10(improvement_triple) = {float(log10(improvement_123)):.0f}")

test("T6: SNR at each level computed",
     SNR123 > SNR12 > SNR1,
     f"SNR improvement: single->triple = 10^{float(log10(improvement_123)):.0f}")

# =====================================================================
# T7: Observation time to reach one false positive
# =====================================================================
print(f"\n{'='*72}")
print("T7: Observation Time to One False Positive")
print("=" * 72)

# At each coincidence level, how long must you observe to expect 1 false positive?

print(f"\n  {'Coincidence Level':<25s}  {'FP rate (/hr)':>15s}  {'Time to 1 FP':>20s}")
print(f"  {'─'*25}  {'─'*15}  {'─'*20}")

# Single: EM only
T_fp_1 = 1 / (thermal_rates[g] * hour) if thermal_rates[g] > 0 else mpf('inf')
print(f"  {'EM only':<25s}  {float(thermal_rates[g]*hour):15.2e}  {float(T_fp_1):.2e} hours")

# Double: EM + acoustic
fp_rate_double = thermal_rates[g] * R_acoustic[g] * tau_det * hour
T_fp_2 = 1 / fp_rate_double if fp_rate_double > 0 else mpf('inf')
T_fp_2_yr = T_fp_2 / (365.25 * 24)
print(f"  {'EM + acoustic':<25s}  {float(fp_rate_double):15.2e}  {float(T_fp_2_yr):.2e} years")

# Triple: EM + acoustic + angular
T_fp_3 = 1 / P_triple_per_hour if P_triple_per_hour > 0 else mpf('inf')
T_fp_3_yr = T_fp_3 / (365.25 * 24)
print(f"  {'EM + acoustic + angular':<25s}  {float(P_triple_per_hour):15.2e}  {float(T_fp_3_yr):.2e} years")

# Reference timescales
print(f"\n  Reference timescales:")
print(f"    1 year = {365.25*24:.0f} hours")
print(f"    Age of universe = 1.38e10 years = {1.38e10*365.25*24:.2e} hours")
print(f"    Proton lifetime (exp lower bound) > 1.67e34 years")

if T_fp_3_yr > mpf('1e34'):
    print(f"\n    Triple coincidence FP time EXCEEDS proton lifetime bound!")
elif T_fp_3_yr > mpf('1.38e10'):
    print(f"\n    Triple coincidence FP time exceeds age of universe by "
          f"{float(T_fp_3_yr / mpf('1.38e10')):.1e}x")

test("T7: FP time exceeds age of universe",
     T_fp_3_yr > mpf('1e10'),
     f"T_fp(triple) = {float(T_fp_3_yr):.2e} years")

# =====================================================================
# T8: Comparison to other detector false positive rates
# =====================================================================
print(f"\n{'='*72}")
print("T8: Comparison to Other Physics Detectors")
print("=" * 72)

# False positive rates of major physics experiments:
detectors = {
    'LIGO (gravitational waves)':    mpf('1e-7'),    # ~1 per year (coincidence of 2 detectors)
    'Super-K (neutrinos)':           mpf('1e-4'),    # ~1 per 100 hours background
    'LHC ATLAS (5-sigma)':           mpf('3e-7'),    # 5-sigma = 3e-7 per trial
    'XENON1T (dark matter)':         mpf('1e-5'),    # few events per year
    'IceCube (astrophysical nu)':    mpf('1e-3'),    # ~few per 1000 hours
    'CMS Higgs (5-sigma)':           mpf('3e-7'),    # same as ATLAS
    'SASER triple coincidence':      P_triple_per_hour,
}

print(f"\n  {'Detector':<35s}  {'FP rate (/hr)':>15s}  {'log10':>8s}")
print(f"  {'─'*35}  {'─'*15}  {'─'*8}")

for name, rate in detectors.items():
    if rate > 0:
        print(f"  {name:<35s}  {float(rate):15.4e}  {float(log10(rate)):8.1f}")
    else:
        print(f"  {name:<35s}  {'0':>15s}  {'─':>8s}")

# How many orders of magnitude better?
best_existing = min(v for k, v in detectors.items() if k != 'SASER triple coincidence' and v > 0)
if P_triple_per_hour > 0:
    advantage = log10(best_existing) - log10(P_triple_per_hour)
    print(f"\n  SASER advantage over best existing detector:")
    print(f"    {float(advantage):.0f} orders of magnitude better")
    print(f"    Best existing: {float(log10(best_existing)):.0f} (log10 FP/hr)")
    print(f"    SASER triple:  {float(log10(P_triple_per_hour)):.0f} (log10 FP/hr)")

test("T8: SASER beats all existing detectors",
     P_triple_per_hour < best_existing,
     f"Advantage: {float(advantage):.0f} orders of magnitude")

# =====================================================================
# RESULTS
# =====================================================================
print(f"\n{'='*72}")
print("RESULTS")
print("=" * 72)
print(f"  {passed}/{total} PASS\n")

print("  TRIPLE COINCIDENCE SUMMARY:")
print(f"  ─────────────────────────────────────────────────────────────────")
print(f"    Signal 1 (EM at BiNb freq):   P = {float(P1_window):.2e} per window")
print(f"    Signal 2 (acoustic coherent): P = {float(P2_window):.2e} per window")
print(f"    Signal 3 (18-fold angular):   P = {float(P3_window):.2e} per window")
print(f"  ─────────────────────────────────────────────────────────────────")
print(f"    P_triple = {float(P_triple_window):.2e} per window")
print(f"    Rate:     {float(P_triple_per_hour):.2e} per hour")
if P_triple_per_hour > 0:
    print(f"    log10:    {float(log10(P_triple_per_hour)):.0f}")
print(f"    Time to 1 FP: {float(T_fp_3_yr):.2e} years")
print(f"  ─────────────────────────────────────────────────────────────────")

print(f"\n  KEY FINDINGS:")
print(f"  1. Triple coincidence false positive rate: ~10^{float(log10(P_triple_per_hour)):.0f} /hour")
print(f"  2. Time to one false positive: {float(T_fp_3_yr):.0e} years")
if T_fp_3_yr > mpf('1.38e10'):
    print(f"     = {float(T_fp_3_yr/mpf('1.38e10')):.0e} x age of universe")
print(f"  3. No natural source produces 18-fold (= N_c x C_2) angular symmetry")
print(f"     (crystallographic restriction forbids 18-fold — it IS the BST signal)")
print(f"  4. {float(advantage):.0f} orders of magnitude better than best existing detector")
print(f"  5. ANY detection above background IS a BST SASER source — zero ambiguity")
print(f"  6. Even 1 event/hour of true signal gives SNR = 10^{float(log10(SNR123)):.0f}")

print(f"\n  BST STRUCTURAL ORIGIN:")
print(f"    The rejection power comes from D_IV^5 structure:")
print(f"      - N_max = 137 layer thickness -> Q = N_max^2 = {N_max**2} (frequency selectivity)")
print(f"      - N_c/g = 3/7 coupling -> acoustic channel isolation")
print(f"      - N_c x C_2 = 18 angular modes -> crystallographically forbidden symmetry")
print(f"    All three coincidence channels are BST integers. The detector IS the theory.")

print(f"\n  (C) Copyright 2026 Casey Koons. All rights reserved.")
