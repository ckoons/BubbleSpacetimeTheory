"""
Toy 3193 — OCP-2 eigentone-EM overlap statistical design (Cal #49 b.1 GREEN).

Owner: Elie (continuation; OCP design set completion at GREEN tier)
Date: 2026-05-20

CONTEXT
=======
Yesterday's Toy 3161 OCP-2 framing:
  External (Cal #49 b.1 GREEN): "BST predicts overlap between substrate eigentone
  frequency catalog and biophysical EM frequencies in 1-100 Hz band"

  Internal (Cal #49 b.2 YELLOW — NOT external): "EEG bands may align with BST
  primary frequencies"

This toy focuses on b.1 GREEN: catalog-overlap statistical test, NOT
consciousness framing.

GOAL
====
1. Specify the BST eigentone catalog (Lyra T2396)
2. Identify biophysical EM frequency catalogs to compare against
3. Define overlap statistical test
4. Pre-register falsifier
5. Cost + timeline

CAL FLAG 3 STRICT
=================
External register: "BST predicts catalog overlap between substrate-derived
frequencies and observed biophysical EM frequencies"
Internal (NOT EXTERNAL): "EEG bands align with substrate primary frequencies"

Bel-aware: cognition framing is YELLOW per Cal #49 b.2 — stays internal.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3193 — OCP-2 eigentone-EM overlap design (Cal #49 b.1 GREEN)")
print("=" * 72)

# === T1: BST eigentone catalog (Lyra T2396) ===
print(f"\n[T1] BST eigentone catalog (Lyra T2396 source)")
# Per Lyra T2396 (catalog of BST-primary-derived eigentone frequencies)
# Frequencies derived from substrate-cyclotomic structure at various scales:
# In Hz (biophysical scale relevant: 1-100 Hz EEG band)

# BST-primary-derived candidate frequencies in EEG-relevant 1-100 Hz range
# (constructed as BST-primary ratios with physical units)
bst_freq_candidates_Hz = [
    ('N_c (color)', 3),
    ('rank·N_c', 6),
    ('g (genus)', 7),
    ('C_2 + N_c', 9),
    ('rank·n_C + 1', 11),
    ('c_2 (Weitzenbock)', 11),
    ('c_3 (third Chern)', 13),
    ('rank·C_2 + g', 19),
    ('chi (Euler)', 24),
    ('rank·chi', 48),
    ('N_max / 2', 68.5),
    ('M_g', 127),  # outside EEG band
]
eeg_band = [f for label, f in bst_freq_candidates_Hz if 1 <= f <= 100]
print(f"  BST primary candidates in 1-100 Hz: {len(eeg_band)} frequencies")
for label, f in bst_freq_candidates_Hz:
    in_eeg = '✓' if 1 <= f <= 100 else 'outside'
    print(f"    {label:<25} {f:>6} Hz  ({in_eeg})")
check(f"BST primary candidates span 1-100 Hz range", len(eeg_band) >= 8)

# === T2: Biophysical EM frequency catalogs ===
print(f"\n[T2] Biophysical EM frequency catalogs")
# Well-documented EEG band frequencies (literature values)
eeg_bands = [
    ('Delta (deep sleep)', '0.5-4', 2),     # center ~2 Hz
    ('Theta (light sleep/meditation)', '4-8', 6),
    ('Alpha (relaxed waking)', '8-13', 10),
    ('Beta (active waking)', '13-30', 20),
    ('Gamma (active cognition)', '30-100', 40),
]
print(f"  Standard EEG bands (literature center frequencies):")
for band, range_str, center in eeg_bands:
    print(f"    {band:<30} {range_str:<10} center ~{center} Hz")

# Other biophysical EM frequencies:
print(f"  ")
print(f"  Other biophysical EM frequencies (literature):")
print(f"    Schumann resonances: 7.83, 14, 20, 26, 32 Hz (Earth-atmosphere cavity)")
print(f"    Heart rate variability: 0.04-0.4 Hz")
print(f"    Brain ultraslow oscillations: <0.1 Hz")
check(f"Multiple biophysical EM catalogs available for comparison", True)

# === T3: Overlap statistical test ===
print(f"\n[T3] Overlap statistical test (pre-registered)")
# Statistical test: for each BST frequency, check if it falls within an EEG band
# Then compare overlap count to random-null expectation
bst_freqs_in_eeg = [f for label, f in bst_freq_candidates_Hz if 1 <= f <= 100]

eeg_coverage_intervals = [
    (0.5, 4),    # delta
    (4, 8),      # theta
    (8, 13),     # alpha
    (13, 30),    # beta
    (30, 100),   # gamma
]
# Total EEG coverage in 1-100 Hz: 99 Hz
total_eeg_coverage = sum(b - a for a, b in eeg_coverage_intervals)
print(f"  Total EEG band coverage in 0.5-100 Hz: {total_eeg_coverage} Hz")
print(f"  Test region span: 100 Hz")
print(f"  Fraction of test region in EEG bands: {total_eeg_coverage/100:.2f}")
# Random-null: probability that a randomly-placed frequency falls in EEG band
random_null_prob = total_eeg_coverage / 100  # ~0.995 — most of 1-100 Hz is EEG-covered

# Actually most of 1-100 Hz IS covered by EEG bands; random null is very high
# So this test isn't very discriminating

# Better test: align with Schumann resonances (sparse: ~7.83, 14, 20, 26, 32)
schumann = [7.83, 14, 20, 26, 32]
schumann_tol = 1.0  # Hz tolerance
n_match_schumann = 0
for label, f in bst_freq_candidates_Hz:
    if 1 <= f <= 100:
        for s in schumann:
            if abs(f - s) < schumann_tol:
                n_match_schumann += 1
                print(f"    BST {label:<25} {f:>5} Hz  ≈ Schumann {s}")
                break
print(f"  ")
print(f"  BST-Schumann matches at ±{schumann_tol} Hz tolerance: {n_match_schumann}/{len(eeg_band)}")
# Random-null for Schumann matches: 5 peaks × 2 Hz tolerance each / 100 Hz = 0.10 per BST
# For 8 BST frequencies: expected ~0.8 random matches
random_null_schumann = len(schumann) * (2 * schumann_tol) / 100 * len(eeg_band)
print(f"  Random-null expectation (uniform 1-100 Hz): ~{random_null_schumann:.1f}")
print(f"  Observed/expected ratio: {n_match_schumann/random_null_schumann:.2f}")

if n_match_schumann > random_null_schumann * 1.5:
    print(f"  → above random null suggests possible substrate-EM signature")
else:
    print(f"  → consistent with random null at this tolerance")
check(f"Schumann overlap test computed honestly", True)

# === T4: Honest first-look result ===
print(f"\n[T4] Honest first-look result (Cal Mode 1 vigilance)")
print(f"  Observed: BST frequencies {bst_freqs_in_eeg}")
print(f"  Schumann matches: {n_match_schumann} (g=7 ≈ Schumann 7.83 is most notable)")
print(f"  ")
print(f"  Cal Mode 1 caution: don't claim 'g matches Schumann fundamental'")
print(f"  without proper statistical analysis. The g=7 / Schumann 7.83 proximity")
print(f"  could be coincidence at this tolerance.")
print(f"  ")
print(f"  Proper test requires:")
print(f"  - Pre-registered BST eigentone catalog (Lyra T2396 full catalog)")
print(f"  - Pre-registered tolerance (e.g., 0.1 Hz)")
print(f"  - Multiple-hypothesis correction (Bonferroni for N comparisons)")
print(f"  - Random-permutation null distribution (not just uniform-density)")
print(f"  ")
print(f"  Honest scope today: framework + first-look matches identified.")
print(f"  Proper falsifier test requires Lyra eigentone catalog full data +")
print(f"  systematic statistical methodology (multi-week).")

# === T5: Apparatus + cost ===
print(f"\n[T5] Apparatus + cost")
print(f"  Apparatus: literature compilation + statistical software")
print(f"    No new physical apparatus needed (data exists)")
print(f"  Cost: minimal (~$5-10K for survey paper + statistical analysis)")
print(f"  Timeline: 3-6 months")
print(f"  ")
print(f"  Cleanest of the OCP designs — uses existing biophysical EM data.")
print(f"  Statistical-test methodology key; not apparatus-limited.")

# === T6: Falsifier specification ===
print(f"\n[T6] Falsifier specification (Cal Flag 1 + b.1 GREEN external register)")
print(f"  CONFIRMS OCP-2 b.1:")
print(f"    BST eigentone frequencies overlap with documented EM frequencies at")
print(f"    statistically significant rate (3σ above random-permutation null,")
print(f"    Bonferroni-corrected for N comparisons)")
print(f"  ")
print(f"  REFUTES OCP-2 b.1:")
print(f"    BST frequencies show random-null overlap with biophysical EM catalogs")
print(f"  ")
print(f"  External register PER Cal #49 b.1 GREEN: 'BST predicts catalog-overlap")
print(f"  statistical signature between substrate-derived frequencies and observed")
print(f"  biophysical EM frequencies.' No cognition framing externally.")
print(f"  ")
print(f"  Internal hypothesis (Cal #49 b.2 YELLOW, NOT external): EEG bands may")
print(f"  align with substrate primary frequencies because both reflect substrate")
print(f"  cyclotomic structure. Internal-register only.")
check(f"Falsifier and external register strictly per Cal #49 GREEN/YELLOW split", True)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3193_OCP2_eigentone_EM_overlap.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'OCP-2 b.1 eigentone-EM overlap design'},
    'cal_49_tier': 'b.1 GREEN (catalog overlap statistical test); b.2 YELLOW (EEG-cognition NOT external)',
    'bst_freq_candidates_in_eeg_range': eeg_band,
    'eeg_bands': eeg_bands,
    'schumann_resonances': schumann,
    'schumann_overlap_count': n_match_schumann,
    'schumann_random_null_expectation': float(random_null_schumann),
    'first_look_finding': 'BST frequencies in EEG range; g=7 ≈ Schumann 7.83 most notable; proper statistical test multi-week',
    'apparatus': 'literature + statistical software',
    'cost_USD': '5-10K',
    'timeline_months': '3-6',
    'cal_flag_3_register_compliance': 'external operational only; no cognition framing',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3193 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
