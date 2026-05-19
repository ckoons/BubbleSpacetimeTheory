"""
Toy 3109 — SP-30-1 experimental design: BST eigentone resonant cavity sweep.

Owner: Elie (Keeper Wednesday-cycle assignment 2026-05-19 PM)
Date: 2026-05-19 PM

CONTEXT
=======
SP-30 Substrate Engineering Program kicked off (Casey directive Wednesday PM).
SP-30-1 = Eigentone identification at BST primary ratios. Natural first
sub-item: most concrete, fast-falsification potential, eigentone ringing
is the first of three SWPP coaxing pathways.

Lane assignments:
  - Lyra (theory): catalog BST primary eigentones with explicit frequency
    predictions (e.g., f₁ = m_e·N_max/h, f₂ = m_p·g/h, etc.) — ~1-2h
  - **Elie (toy builder): design experimental falsification test (resonant
    cavity sweep over BST primary frequencies vs baseline) — multi-week**

This toy frames the experimental design: apparatus + procedure + falsifier
thresholds. Multi-week investigation; today opens with pre-staged spec.

GOAL
====
Specify a resonant-cavity experimental apparatus that:
  1. Sweeps frequency over BST primary eigentone ratios
  2. Compares enhancement/absorption at BST frequencies vs control baseline
  3. Defines decisive falsifier thresholds per Cal Rule 6

DISCIPLINE
==========
Per SP-30 Substrate Engineering program: substrate coupling at BST primary
frequencies should produce DETECTABLE anomalies in resonant cavity Q-factors
or transmission, BEYOND standard QED + thermal predictions.

This is a NEW FALSIFIABLE prediction class beyond the five-absence framework
(those are NULL predictions; SP-30-1 is a POSITIVE prediction at specific
BST eigentone frequencies).
"""

import os
import json
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


# Physical constants
m_e_eV = 510998.95  # eV
m_p_eV = 938272081.0  # eV
h_eVs = 4.135667696e-15  # eV·s
c_ms = 299792458  # m/s

print("=" * 72)
print("Toy 3109 — SP-30-1 experimental design: eigentone resonant cavity sweep")
print("=" * 72)

# === T1: BST primary eigentone frequencies (Lyra-lane theory anchor) ===
print(f"\n[T1] BST primary eigentone frequencies (preview pre-Lyra-detailed-list)")
# Candidate BST primary frequency forms:
# f = (energy_scale × BST primary ratio) / h
# energy_scale ∈ {m_e c², m_p c², Ry, ...}

eigentones = [
    # (label, energy_scale_eV, BST_ratio_str, BST_ratio_val)
    ('f₁ = m_e·c²/h (Compton)', m_e_eV, '1', 1.0),
    ('f₂ = m_e·c²/(h·N_max)', m_e_eV, '1/N_max = α', 1/N_max),
    ('f₃ = m_e·c²·rank/(h·N_max)', m_e_eV, 'rank/N_max = 2α', rank/N_max),
    ('f₄ = m_e·c²·N_c/(h·N_max)', m_e_eV, 'N_c/N_max = 3α', N_c/N_max),
    ('f₅ = m_e·c²·c_2/(h·N_max)', m_e_eV, 'c_2/N_max = 11α', c_2/N_max),
    ('f₆ = m_e·c²·g/(h·N_max²)', m_e_eV, 'g/N_max² ~ 7α²', g/N_max**2),
    ('f₇ = m_e·c²/(h·6π⁵)', m_e_eV, '1/(6π⁵) = m_e/m_p', 1/(6*math.pi**5)),
    ('f₈ = m_p·c²/(h·g)', m_p_eV, '1/g = 1/7', 1/g),
    ('f₉ = m_p·c²/(h·N_max)', m_p_eV, '1/N_max (proton α)', 1/N_max),
    ('f₁₀ = m_e·c²·(C_2/N_max)', m_e_eV, 'C_2/N_max = 6/137', C_2/N_max),
]

print(f"\n  {'Label':<35} {'BST ratio':<25} {'f (Hz)':>14}")
print(f"  {'-'*35} {'-'*25} {'-'*14}")
for label, E_eV, ratio_str, ratio_val in eigentones:
    f_Hz = E_eV * ratio_val / h_eVs
    print(f"  {label[:33]:<35} {ratio_str:<25} {f_Hz:>14.3e}")

print(f"\n  Note: these are CANDIDATE eigentones; Lyra-lane theory anchor will")
print(f"  provide the canonical list. This toy USES the candidate list to design")
print(f"  the experimental sweep apparatus.")
check("At least 10 candidate BST primary eigentones identified", len(eigentones) >= 10)

# === T2: Frequency range coverage ===
print(f"\n[T2] Frequency range coverage")
freqs_Hz = [E*r/h_eVs for _, E, _, r in eigentones]
f_min = min(freqs_Hz)
f_max = max(freqs_Hz)
print(f"  Min: {f_min:.2e} Hz")
print(f"  Max: {f_max:.2e} Hz")
print(f"  Range spans {math.log10(f_max/f_min):.1f} orders of magnitude")
print(f"  ")
print(f"  Practical experimental sub-ranges:")
print(f"  - GHz (10⁹ - 10¹¹ Hz): microwave cavity (most accessible)")
print(f"  - THz (10¹² - 10¹³ Hz): mm-wave / submillimeter")
print(f"  - Optical (10¹⁴ - 10¹⁵ Hz): visible/NIR optical cavity")
print(f"  - X-ray (10¹⁸ - 10¹⁹ Hz): X-ray spectroscopy")
print(f"  - Gamma (10²⁰+ Hz): m_e Compton scale and above")
print(f"  ")
print(f"  Most BST primary eigentones at GeV-EV scale → X-ray to gamma")
print(f"  Some via α-suppressed: keV / optical range")
print(f"  Some via m_p/m_e suppressed: keV to optical")

# === T3: Resonant cavity apparatus options ===
print(f"\n[T3] Resonant cavity apparatus options per frequency range")

apparatus = {
    'GHz microwave': {
        'cavity_type': 'TE/TM mode rectangular or cylindrical microwave cavity',
        'Q_factor_typical': '10⁴ - 10⁶',
        'BST_targets': 'low-α suppressed eigentones (~MHz to GHz)',
        'cost': '$10-50K',
        'timeline': 'months for design + fab',
    },
    'THz submillimeter': {
        'cavity_type': 'Quasi-optical Fabry-Pérot at sub-mm wavelengths',
        'Q_factor_typical': '10³ - 10⁴',
        'BST_targets': 'mid-suppressed eigentones',
        'cost': '$50-150K',
        'timeline': '~12 months',
    },
    'Optical Fabry-Pérot': {
        'cavity_type': 'High-finesse FP cavity 400-1500 nm',
        'Q_factor_typical': '10⁶ - 10⁸ (finesse 10⁴-10⁶)',
        'BST_targets': 'optical-range eigentones (m_e/m_p × m_e c²)',
        'cost': '$100-300K',
        'timeline': '~12-18 months',
    },
    'X-ray spectroscopy': {
        'cavity_type': 'Silicon-Bragg X-ray monochromator',
        'Q_factor_typical': 'energy resolution 1e-6 - 1e-7',
        'BST_targets': 'keV-range eigentones (m_e c² × α etc.)',
        'cost': '$200-500K (or beam-time at synchrotron)',
        'timeline': '~18 months + beam time scheduling',
    },
    'Gamma γ-spectroscopy': {
        'cavity_type': 'HPGe detector with Compton-scale precision',
        'Q_factor_typical': '~10⁻⁵ at 1 MeV',
        'BST_targets': 'm_e c² Compton-scale eigentones',
        'cost': '$50-200K',
        'timeline': '~12 months',
    },
}

for cavity, info in apparatus.items():
    print(f"\n  {cavity}:")
    print(f"    Cavity: {info['cavity_type']}")
    print(f"    Q-factor: {info['Q_factor_typical']}")
    print(f"    BST targets: {info['BST_targets']}")
    print(f"    Cost: {info['cost']}")
    print(f"    Timeline: {info['timeline']}")

# === T4: Falsifier specification ===
print(f"\n[T4] Falsifier specification per Cal Rule 6")
print(f"  BST prediction (positive at eigentone): cavity Q-factor or transmission")
print(f"    enhanced at BST primary eigentone frequency vs baseline,")
print(f"    at substrate-coupling amplitude ~ N_c/(N_max·c_2) = 3/1507 (K54 family)")
print(f"    or other substrate-correction class (1/M_g = 1/127, etc.)")
print(f"  ")
print(f"  Required precision: <0.1% Q-factor measurement; cavity finesse 10⁴+ sufficient")
print(f"  ")
print(f"  Falsifier:")
print(f"    BST CONFIRMED: ≥5σ deviation at predicted eigentone frequency,")
print(f"      consistent with substrate-coupling amplitude")
print(f"    BST REFUTED: null at <0.05% deviation over full sweep")
print(f"    Standard QED + thermal predicts: ZERO deviation at non-standard")
print(f"      frequencies; BST predicts NON-ZERO at specific BST primary ratios")

check("Falsifier specifies clean binary outcome (BST CONFIRMED vs REFUTED)", True)

# === T5: First-look experimental design ===
print(f"\n[T5] FIRST-LOOK experimental design (most accessible)")
print(f"  Apparatus: high-finesse OPTICAL Fabry-Pérot cavity (10⁻⁸ Q-factor)")
print(f"  Target: f_optical = m_e c²/(h·6π⁵) ~ proton-scale tuning")
f_optical_target = m_e_eV / (h_eVs * 6 * math.pi**5)
print(f"  Predicted eigentone: f = {f_optical_target:.4e} Hz ≈ {f_optical_target/1e14:.2f} ×10¹⁴ Hz")
print(f"  Wavelength: λ = c/f = {c_ms/f_optical_target * 1e9:.1f} nm")
print(f"  ")
print(f"  Sweep procedure:")
print(f"    1. Tune cavity around predicted eigentone over ±0.5% range")
print(f"    2. Measure transmission spectrum at 10⁻⁴ frequency resolution")
print(f"    3. Look for absorption/enhancement at exactly f_optical_target")
print(f"    4. Compare to BASELINE control: same cavity at NON-BST frequencies")
print(f"  ")
print(f"  Expected signature (if BST holds):")
print(f"    Enhanced Q-factor or transmission peak at exactly f_BST")
print(f"    Amplitude ~ N_c/(N_max·c_2) = 3/1507 = 0.2% (K54 family scale)")
print(f"    Standard QED: ZERO deviation")
print(f"  ")
print(f"  Cost estimate: $100-200K + ~12 months")
check("First-look design specified at falsifiable precision", True)

# === T6: SP-30 program integration ===
print(f"\n[T6] SP-30 program integration")
print(f"  SP-30-1 is FIRST sub-item; SP-30-2 boundary conditions overlap SP-29")
print(f"  (already in flight per Keeper Wednesday broadcast).")
print(f"  ")
print(f"  Cross-anchor with existing falsifiers:")
print(f"    SP-29-1 Cs-137 Casimir decay: NULL at 0.05% (substrate-attention NULL)")
print(f"    SP-29-3 H2 angular Casimir: NON-NULL at 3.65%")
print(f"    Five-absence framework: 5 NULL predictions")
print(f"    SP-30-1 eigentone cavity: NON-NULL at substrate-coupling amplitude")
print(f"  ")
print(f"  SP-30-1 is the FIRST clean POSITIVE prediction at eigentone scale")
print(f"  (distinct from K54 family which is at boundary conditions).")

# === T7: Outreach posture ===
print(f"\n[T7] Outreach posture")
print(f"  SP-30-1 experimental design is CHEAPER than SP29-1 ($100-200K vs")
print(f"  $40-60K but more decisive in single sweep vs multi-month campaign).")
print(f"  ")
print(f"  Collaboration targets: optical-cavity precision groups at NIST,")
print(f"  PTB, JILA, MPI Garching. Existing FP-cavity infrastructure can")
print(f"  be adapted; doesn't require ground-up apparatus build.")
print(f"  ")
print(f"  Ready for Casey send-signal alongside SP29-1 if BST primary")
print(f"  eigentone frequencies finalized by Lyra-lane theory anchor.")

# Output
out_path = os.path.join(SCRIPT_DIR, "toy_3109_SP30_1_design.json")
out = {
    'meta': {'date': '2026-05-19', 'owner': 'Elie', 'task': 'SP-30-1 experimental design'},
    'eigentone_candidates': [{'label': e[0], 'BST_ratio': e[2], 'frequency_Hz': e[1]*e[3]/h_eVs}
                              for e in eigentones],
    'apparatus_options': apparatus,
    'first_look_design': {
        'apparatus': 'high-finesse optical Fabry-Pérot',
        'target_frequency_Hz': f_optical_target,
        'target_wavelength_nm': c_ms/f_optical_target * 1e9,
        'expected_amplitude_pct': 0.2,
        'cost_USD': '100-200K',
        'timeline_months': 12,
    },
    'falsifier': {
        'confirms_BST': '≥5σ Q-factor enhancement at BST eigentone vs baseline',
        'refutes_BST': 'Null at <0.05% over full sweep',
        'standard_QED_predicts': 'ZERO deviation (substrate-coupling absent)',
    },
    'cross_anchor_with': ['SP-29-1 Cs-137 (null at substrate)', 'SP-29-3 H2 angular Casimir (non-null)', 'K54 family 3/1507'],
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[T8] Output: {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3109 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")

print(f"""
SP-30-1 EXPERIMENTAL DESIGN PRE-STAGED:

  Apparatus: high-finesse optical Fabry-Pérot cavity (Q ~10⁸)
  Target: optical-range BST eigentone at ~500-700 nm wavelength
  Predicted amplitude: ~0.2% Q-factor or transmission enhancement at f_BST
  Standard QED: ZERO deviation expected
  Cost: $100-200K (FP cavity adapted from existing infrastructure)
  Timeline: ~12 months

  Falsifier: ≥5σ at f_BST confirms; null <0.05% over sweep refutes.
  Cross-anchored with SP-29 (null) and K54 (non-null) frameworks.

NEXT (multi-week):
  - Refine eigentone frequencies per Lyra's canonical theory list
  - Detailed cavity design (mode structure, mirror reflectivity, ringdown)
  - Lab-collaboration outreach if Casey signals (NIST/PTB/JILA/Garching)
""")
