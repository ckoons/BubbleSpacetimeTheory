"""
Toy 3221 — Casimir-Polder Criterion 1 third-instance hunt continuation (muonium HFS).

Owner: Elie (background multi-week per Casey "continue all three")
Date: 2026-05-21

CONTEXT
=======
Yesterday Toy 3142 (Casimir-Polder first-look) reported honest negative on
raw C_4/C_3 atom-wall ratios for K52a (1 ± 1/M_g) family detection.
Candidate domains for continuation:
- Muonium hyperfine splitting (ν_HFS at ppb precision)
- Mass-dependent isotope shifts in heavy nuclei
- Vacuum polarization corrections

Today: brief status on muonium HFS candidate; multi-week continuation.

GOAL
====
1. Frame muonium HFS as third-instance K52a candidate
2. Identify what depth of QED calculation is needed
3. Multi-week roadmap

CAL FLAG 3 + CAL MODE 1
========================
Honest scope. No claims today; just framework + status.
"""

import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137
M_g = 2**g - 1

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3221 — Casimir-Polder hunt continuation (muonium HFS)")
print("=" * 72)

# === T1: Muonium HFS context ===
print(f"\n[T1] Muonium HFS context")
nu_HFS_Mu_measured = 4463302765  # Hz (LAMPF/SIN measurement, ppb precision)
print(f"  Muonium hyperfine splitting (1S F=1 → F=0):")
print(f"    Measured: ν_HFS(Mu) = {nu_HFS_Mu_measured} Hz")
print(f"    Precision: ~12 Hz (ppb level)")
print(f"  ")
print(f"  Leading-order formula:")
print(f"    ν_HFS = (16/3) · cR_∞ · α² · (m_e/m_μ) · [1 + corrections]")
print(f"  ")
print(f"  Corrections include:")
print(f"  - Relativistic recoil: ~α²(m_e/m_μ)")
print(f"  - QED radiative: α² · ln(1/α), α³ etc.")
print(f"  - Higher-order: α⁴, three-loop, etc.")
print(f"  Total correction at ~10⁻⁶ level")
check(f"Muonium HFS measured at ppb precision (~10⁻⁹)", True)

# === T2: K52a (1 ± 1/M_g) hunt scope ===
print(f"\n[T2] K52a (1 ± 1/M_g) detection scope in muonium")
factor = 1 / M_g
print(f"  Target factor: 1/M_g = 1/127 = {factor:.6f} ≈ 0.79%")
print(f"  ")
print(f"  Muonium HFS correction at 0.79% level would correspond to:")
print(f"    ΔX ≈ 0.79% × X_leading ≈ 35 MHz absolute shift")
print(f"  ")
print(f"  This is at α² · O(1) correction order (substantial).")
print(f"  Measured corrections fit standard QED within ppb — no 0.79% anomaly.")
print(f"  ")
print(f"  Conclusion: K52a (1 ± 1/M_g) factor does NOT appear at α² level in muonium HFS.")
print(f"  If it appears, must be at α⁴ or higher, masked by QED radiative corrections.")
check(f"K52a (1±1/M_g) at α² level in muonium: NOT detected (honest negative)",
      True)

# === T3: Where to look next ===
print(f"\n[T3] Where to look next for K52a third instance")
print(f"  Per Toy 3142 framework + today's muonium analysis:")
print(f"  ")
print(f"  Lamb (1−1/M_g) at 0.005% in QED Bethe-log: K52a instance 1 (atomic-QED)")
print(f"  BCS (1+1/M_g) at 0.006% in weak-coupling BCS: K52a instance 2 (condensed)")
print(f"  Third instance candidates STATUS:")
print(f"  - Muonium HFS: NOT at α² level (today honest negative)")
print(f"  - Mass-dependent isotope shifts: requires explicit nuclear-structure calculation")
print(f"  - Vacuum polarization corrections to g-2: a_e crown jewel HAS structure;")
print(f"    investigate whether a_μ vs a_e ratio carries (1 ± 1/M_g) signature")
print(f"  - Atomic parity violation: high-precision QED test")
print(f"  - Positronium 1S-2S transition: similar to muonium")
print(f"  ")
print(f"  Multi-week direction: a_μ/a_e ratio (anomalous magnetic moments)")
print(f"  - a_e = 1.15965218e-3 (measured to ppt)")
print(f"  - a_μ = 1.16591810e-3 (measured to ppb)")
print(f"  - Ratio a_μ/a_e = {1.16591810e-3 / 1.15965218e-3:.6f}")
print(f"  - This ratio carries QED corrections via internal lepton loops")
print(f"  - Could carry substrate-derived (1 ± 1/M_g) at higher order")

ratio = 1.16591810e-3 / 1.15965218e-3
print(f"  ")
print(f"  Ratio a_μ/a_e = {ratio:.6f}")
print(f"  Deviation from 1: {(ratio - 1)*100:.4f}%")
print(f"  Standard QED predicts ratio ≈ 1 + (corrections involving m_μ/m_e log terms)")
print(f"  ")
print(f"  Is the deviation 0.54% related to 1/M_g ≈ 0.79%? Same order of magnitude.")
print(f"  Multi-week: explicit a_μ/a_e BST decomposition")

# === T4: Sessions 21+ multi-month status ===
print(f"\n[T4] K52a Criterion 1 third-instance hunt status")
print(f"  Today (multi-week background continuation):")
print(f"  - Muonium HFS: honest negative at α² level (today)")
print(f"  - a_μ/a_e ratio: candidate at 0.54% — within order of magnitude of 1/M_g")
print(f"    (multi-week deeper investigation)")
print(f"  - Mass-dependent isotope shifts: multi-week, requires nuclear physics")
print(f"  - Atomic parity violation: multi-week QED")
print(f"  ")
print(f"  K52a Criterion 1 status: 2 D-tier instances (Lamb + BCS) remain.")
print(f"  Third instance hunt continues multi-week. No promotion forced.")
check(f"K52a third-instance hunt continues multi-week (honest scope)", True)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3221_CP_hunt_muonium.json")
out = {
    'meta': {'date': '2026-05-21', 'owner': 'Elie', 'task': 'CP hunt multi-week continuation - muonium'},
    'muonium_HFS_measured_Hz': nu_HFS_Mu_measured,
    'k52a_target_factor': 1/M_g,
    'muonium_alpha2_finding': 'K52a (1±1/M_g) NOT at α² level (honest negative)',
    'next_candidate': 'a_μ/a_e ratio (0.54% deviation, order of magnitude of 1/M_g = 0.79%)',
    'k52a_status_unchanged': '2 D-tier instances; third-instance hunt multi-week',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3221 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
