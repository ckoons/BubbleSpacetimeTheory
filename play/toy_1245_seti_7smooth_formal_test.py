#!/usr/bin/env python3
"""
Toy 1245 — T1288 backing: 7-smooth SETI Prediction Formal Statistical Test
===========================================================================

Extends Toy 1240. The claim for T1288:
  "Spectral lines from BST-native technology cluster at 7-smooth
   frequency ratios relative to hydrogen."

This toy builds a RIGOROUS statistical framework:
  1. All 7-smooth rationals a/b with a,b <= 200
  2. Target frequencies in 100 MHz - 30 GHz from H-line
  3. Doppler detection windows (+-300 km/s -> +-0.1%)
  4. Null model: Monte Carlo (100k trials, 50 random features)
  5. Signal model: K random 7-smooth ratios
  6. Band coverage, p-values for K=3,5,10, minimum K for 5-sigma
  7. Natural line contamination check

BST integers: N_c=3, n_C=5, g=7, C_2=6, N_max=137
AC complexity: (C=2, D=1)
"""

import math
import random
from fractions import Fraction

random.seed(137)  # BST seed

# ── BST Constants ──────────────────────────────────────────────
N_c, n_C, g, C_2, N_max = 3, 5, 7, 6, 137
rank = 2
f_c = 9 / 47
alpha = 1.0 / N_max

# ── Physical Constants ─────────────────────────────────────────
H_LINE = 1420.405751       # MHz, hydrogen 21-cm line
BAND_LOW = 100.0           # MHz
BAND_HIGH = 30000.0        # MHz
DOPPLER_FRAC = 300.0 / 3e5 # +-300 km/s -> +-0.1%
c_light = 2.998e8          # m/s
h_planck = 6.626e-34       # J*s
eV_to_Hz = 2.418e14        # Hz per eV

# ── Test Framework ─────────────────────────────────────────────
results = []


def test(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results.append((name, condition, detail))
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {name}")
    if detail:
        print(f"         {detail}")


# ════════════════════════════════════════════════════════════════
# PART 1: Generate all 7-smooth numbers up to 200
# ════════════════════════════════════════════════════════════════
print("=" * 72)
print("PART 1: 7-smooth Numbers and Rationals")
print("=" * 72)


def is_7_smooth(n):
    """Check if n has only prime factors in {2, 3, 5, 7}."""
    if n <= 0:
        return False
    for p in [2, 3, 5, 7]:
        while n % p == 0:
            n //= p
    return n == 1


# All 7-smooth numbers up to 200
smooth_nums = [n for n in range(1, 201) if is_7_smooth(n)]
print(f"\n  7-smooth numbers up to 200: {len(smooth_nums)}")
print(f"  First 20: {smooth_nums[:20]}")
print(f"  Last 10:  {smooth_nums[-10:]}")

# All 7-smooth rationals a/b with a, b <= 200 (both 7-smooth)
smooth_rationals = set()
for a in smooth_nums:
    for b in smooth_nums:
        r = Fraction(a, b)
        smooth_rationals.add(r)

# Filter to those producing frequencies in 100 MHz - 30 GHz
in_band_rationals = set()
for r in smooth_rationals:
    freq = H_LINE * float(r)
    if BAND_LOW <= freq <= BAND_HIGH:
        in_band_rationals.add(r)

in_band_sorted = sorted(in_band_rationals, key=float)
print(f"\n  Total distinct 7-smooth rationals: {len(smooth_rationals)}")
print(f"  Rationals producing freqs in {BAND_LOW}-{BAND_HIGH} MHz: {len(in_band_rationals)}")
print(f"  Frequency range covered: {H_LINE * float(in_band_sorted[0]):.2f} - "
      f"{H_LINE * float(in_band_sorted[-1]):.2f} MHz")

# ════════════════════════════════════════════════════════════════
# PART 2: Target frequencies and detection windows
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 2: Target Frequencies and Doppler Windows")
print("=" * 72)

# For each in-band 7-smooth rational, compute the target frequency and window
windows = []
for r in in_band_sorted:
    f_center = H_LINE * float(r)
    f_low = f_center * (1 - DOPPLER_FRAC)
    f_high = f_center * (1 + DOPPLER_FRAC)
    windows.append((f_center, f_low, f_high, r))

print(f"\n  Total detection windows: {len(windows)}")
print(f"  Window half-width: +-{DOPPLER_FRAC * 100:.3f}% (Doppler +-300 km/s)")
print(f"\n  Sample windows (first 10 and last 5):")
for i, (fc, fl, fh, r) in enumerate(windows[:10]):
    print(f"    {r!s:>10} -> {fc:>10.3f} MHz  [{fl:.3f} - {fh:.3f}]")
print(f"    ...")
for i, (fc, fl, fh, r) in enumerate(windows[-5:]):
    print(f"    {r!s:>10} -> {fc:>10.3f} MHz  [{fl:.3f} - {fh:.3f}]")

# ════════════════════════════════════════════════════════════════
# PART 3: Band coverage fraction
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 3: Band Coverage — Fraction of Spectrum in Detection Windows")
print("=" * 72)

# Merge overlapping windows to compute total coverage
# Sort by f_low
windows_sorted = sorted(windows, key=lambda w: w[1])
merged = []
for fc, fl, fh, r in windows_sorted:
    if merged and fl <= merged[-1][1]:
        # Overlap: extend
        merged[-1] = (merged[-1][0], max(merged[-1][1], fh))
    else:
        merged.append((fl, fh))

total_covered_bandwidth = sum(fh - fl for fl, fh in merged)
total_band = BAND_HIGH - BAND_LOW
coverage_fraction = total_covered_bandwidth / total_band

print(f"\n  Band: {BAND_LOW} - {BAND_HIGH} MHz = {total_band:.0f} MHz total")
print(f"  Merged detection windows: {len(merged)}")
print(f"  Total covered bandwidth: {total_covered_bandwidth:.2f} MHz")
print(f"  Coverage fraction: {coverage_fraction:.6f} ({coverage_fraction * 100:.4f}%)")
print(f"\n  This means: a random frequency has a {coverage_fraction * 100:.4f}% chance")
print(f"  of falling in a 7-smooth detection window purely by accident.")

# ════════════════════════════════════════════════════════════════
# PART 4: Null model — Monte Carlo
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 4: Null Model — Monte Carlo (100,000 trials, 50 features each)")
print("=" * 72)

N_TRIALS = 100_000
N_FEATURES = 50

# Precompute sorted merged windows for binary search
merged_lows = [fl for fl, fh in merged]
merged_highs = [fh for fl, fh in merged]


def freq_in_any_window(freq):
    """Check if freq falls in any merged detection window (binary search)."""
    import bisect
    idx = bisect.bisect_right(merged_lows, freq) - 1
    if idx >= 0 and freq <= merged_highs[idx]:
        return True
    return False


null_counts = []
for trial in range(N_TRIALS):
    features = [random.uniform(BAND_LOW, BAND_HIGH) for _ in range(N_FEATURES)]
    count = sum(1 for f in features if freq_in_any_window(f))
    null_counts.append(count)

mean_null = sum(null_counts) / len(null_counts)
var_null = sum((x - mean_null) ** 2 for x in null_counts) / len(null_counts)
std_null = var_null ** 0.5

# Distribution of null counts
from collections import Counter
null_dist = Counter(null_counts)

print(f"\n  Null distribution (50 random features per trial):")
print(f"    Mean:   {mean_null:.3f}")
print(f"    Std:    {std_null:.3f}")
print(f"    Min:    {min(null_counts)}")
print(f"    Max:    {max(null_counts)}")
print(f"    Expected (analytic): {N_FEATURES * coverage_fraction:.3f}")
print(f"    Std (analytic):      {(N_FEATURES * coverage_fraction * (1 - coverage_fraction)) ** 0.5:.3f}")

# ════════════════════════════════════════════════════════════════
# PART 5: Signal model
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 5: Signal Model — BST Civilization Features")
print("=" * 72)

# A BST civilization places features at K randomly chosen 7-smooth ratios
# By construction, ALL K features fall in detection windows (probability 1)
# Signal model: if we observe N_obs features, K are BST-placed, (N_obs - K)
# are noise. How many total land in windows?

print(f"\n  BST civilization: K features all at 7-smooth ratios (100% in-window)")
print(f"  Noise: {N_FEATURES - 10} features at random ({coverage_fraction * 100:.4f}% chance each)")
print(f"\n  Signal model prediction:")
for K in [3, 5, 10]:
    noise_features = N_FEATURES - K
    expected_signal = K + noise_features * coverage_fraction
    std_signal = (noise_features * coverage_fraction * (1 - coverage_fraction)) ** 0.5
    print(f"    K={K:>2}: expected in-window = {expected_signal:.2f} +- {std_signal:.2f}"
          f"  (noise only: {mean_null:.2f} +- {std_null:.2f})")

# ════════════════════════════════════════════════════════════════
# PART 6: p-values and detection thresholds
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 6: p-Values and Detection Thresholds")
print("=" * 72)

# For K coincidences above null, compute p-value
# p-value = P(X >= K | null), where X ~ Binomial(N_FEATURES, coverage_fraction)
# Use Gaussian approximation: Z = (K - mean_null) / std_null


def z_to_p(z):
    """One-sided p-value from Z-score (Gaussian approximation)."""
    return 0.5 * math.erfc(z / math.sqrt(2))


print(f"\n  p-values for observing K total in-window features (null: {mean_null:.2f} +- {std_null:.2f}):")
print(f"  {'K obs':>6}  {'Z-score':>8}  {'p-value':>12}  {'sigma':>6}  {'Verdict':>12}")
print(f"  {'─' * 6}  {'─' * 8}  {'─' * 12}  {'─' * 6}  {'─' * 12}")

for K_obs in [3, 5, 10, 15, 20]:
    # If K BST features are placed, total in-window = K + null_from_remaining
    # But we test: observed total in-window features
    z = (K_obs - mean_null) / std_null if std_null > 0 else float('inf')
    p = z_to_p(z)
    sigma_equiv = z
    verdict = "5-sigma!" if sigma_equiv >= 5 else ("3-sigma" if sigma_equiv >= 3 else "noise")
    print(f"  {K_obs:>6}  {z:>8.2f}  {p:>12.2e}  {sigma_equiv:>6.1f}  {verdict:>12}")

# Minimum K for 5-sigma
# Need: K_obs such that (K_obs - mean_null) / std_null >= 5
K_5sigma = math.ceil(mean_null + 5 * std_null)
print(f"\n  Minimum features in-window for 5-sigma: {K_5sigma}")
print(f"  Minimum BST features needed (K_bst) to guarantee this:")

# K_bst features all in-window, plus noise from (N_FEATURES - K_bst)
# Expected total = K_bst + (N_FEATURES - K_bst) * coverage_fraction
# Need: K_bst + (N_FEATURES - K_bst) * p_cov >= K_5sigma
# K_bst * (1 - p_cov) >= K_5sigma - N_FEATURES * p_cov
p_cov = coverage_fraction
K_bst_min = math.ceil((K_5sigma - N_FEATURES * p_cov) / (1 - p_cov))
K_bst_min = max(K_bst_min, 1)
print(f"  K_bst >= {K_bst_min} (ensuring expected total in-window >= {K_5sigma})")

# More precise: for each K_bst, compute the p-value of the EXPECTED signal
print(f"\n  Detection power for various K_bst (BST features among {N_FEATURES} total):")
print(f"  {'K_bst':>6}  {'E[in-win]':>10}  {'Z vs null':>10}  {'sigma':>6}")
print(f"  {'─' * 6}  {'─' * 10}  {'─' * 10}  {'─' * 6}")
for K_bst in [1, 2, 3, 5, 7, 10, 15]:
    noise_n = N_FEATURES - K_bst
    expected_total = K_bst + noise_n * p_cov
    z = (expected_total - mean_null) / std_null if std_null > 0 else float('inf')
    print(f"  {K_bst:>6}  {expected_total:>10.2f}  {z:>10.2f}  {z:>6.1f}")

# ════════════════════════════════════════════════════════════════
# PART 7: Natural Line Contamination Check
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 7: Natural Line Contamination Check")
print("=" * 72)

# Known natural spectral lines
# Convert wavelength to frequency: f = c / lambda
natural_lines = {
    "Lyman-alpha":  c_light / (1215.67e-10) / 1e6,   # MHz
    "H-alpha":      c_light / (6562.8e-10) / 1e6,     # MHz
    "OH (1665)":    1665.402,                          # MHz
    "H2O (22235)":  22235.08,                          # MHz
    "CO(1-0)":      115271.202,                        # MHz (out of band)
}

print(f"\n  Natural line frequencies and their ratios to H-line:")
print(f"  {'Line':<15} {'Freq (MHz)':>14} {'Ratio to H':>12} {'In band?':>10} "
      f"{'Closest 7-smooth':>18} {'Distance':>10} {'In window?':>10}")
print(f"  {'─' * 15} {'─' * 14} {'─' * 12} {'─' * 10} {'─' * 18} {'─' * 10} {'─' * 10}")

contamination_count = 0
contamination_details = []

for name, freq in natural_lines.items():
    ratio = freq / H_LINE
    in_band = BAND_LOW <= freq <= BAND_HIGH

    # Find closest 7-smooth rational
    best_r = None
    best_dist = float('inf')
    for r in smooth_rationals:
        d = abs(float(r) - ratio)
        if d < best_dist:
            best_dist = d
            best_r = r

    # Check if natural line falls in any detection window
    in_window = freq_in_any_window(freq) if in_band else False
    if in_window:
        contamination_count += 1
        contamination_details.append(name)

    rel_dist = best_dist / ratio if ratio > 0 else float('inf')

    print(f"  {name:<15} {freq:>14.2f} {ratio:>12.6f} {'YES' if in_band else 'NO':>10} "
          f"{str(best_r):>18} {rel_dist:>10.6f} {'YES *' if in_window else 'NO':>10}")

print(f"\n  Natural lines falling in 7-smooth windows: {contamination_count}/{len(natural_lines)}")
if contamination_details:
    print(f"  Contaminated lines: {', '.join(contamination_details)}")
    print(f"  These must be EXCLUDED from any SETI detection claim.")
else:
    print(f"  No contamination — all natural lines are distinguishable from 7-smooth signal.")

# Check: is OH line near any BST ratio? (OH is in the water hole)
oh_ratio = natural_lines["OH (1665)"] / H_LINE
oh_frac = Fraction(oh_ratio).limit_denominator(200)
oh_smooth = is_7_smooth(oh_frac.numerator) and is_7_smooth(oh_frac.denominator)
print(f"\n  OH line ratio to H: {oh_ratio:.6f}")
print(f"  Nearest simple fraction: {oh_frac} = {float(oh_frac):.6f}")
print(f"  Is it 7-smooth? {'YES — potential contamination!' if oh_smooth else 'NO — clean separation'}")

# ════════════════════════════════════════════════════════════════
# PART 8: Summary Statistics
# ════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("PART 8: Summary")
print("=" * 72)

print(f"""
  7-smooth rationals (a,b <= 200):          {len(smooth_rationals)}
  In-band (100 MHz - 30 GHz):              {len(in_band_rationals)}
  Merged detection windows:                 {len(merged)}
  Band coverage:                            {coverage_fraction * 100:.4f}%
  Null mean (50 features):                  {mean_null:.3f}
  Null std:                                 {std_null:.3f}
  Minimum K for 5-sigma:                    {K_bst_min}
  Natural line contamination:               {contamination_count}/{len(natural_lines)}
""")

# ════════════════════════════════════════════════════════════════
# TESTS
# ════════════════════════════════════════════════════════════════
print("=" * 72)
print("TESTS")
print("=" * 72)

# T1: Band coverage is substantial but < 50% (windows are selective, not blanket)
test("T1: Band coverage < 50% (windows don't blanket the band)",
     coverage_fraction < 0.50,
     f"Coverage = {coverage_fraction * 100:.4f}% — selective enough to test")

# T2: Band coverage is non-trivial (enough windows to detect signal)
test("T2: Band coverage > 0.1% (enough windows for detection)",
     coverage_fraction > 0.001,
     f"Coverage = {coverage_fraction * 100:.4f}%")

# T3: Null rate matches analytic expectation
analytic_mean = N_FEATURES * coverage_fraction
test("T3: Monte Carlo null mean matches analytic (within 5%)",
     abs(mean_null - analytic_mean) / analytic_mean < 0.05,
     f"MC mean = {mean_null:.3f}, analytic = {analytic_mean:.3f}")

# T4: K=10 BST features produce detectable signal (>= 2-sigma)
expected_10 = 10 + (N_FEATURES - 10) * coverage_fraction
z_10 = (expected_10 - mean_null) / std_null
test("T4: K=10 BST features yield >= 2-sigma above null",
     z_10 >= 2.0,
     f"Z = {z_10:.2f} sigma")

# T5: K=15 BST features are strongly detectable (>= 3-sigma)
expected_15 = 15 + (N_FEATURES - 15) * coverage_fraction
z_15 = (expected_15 - mean_null) / std_null
test("T5: K=15 BST features yield >= 3-sigma above null",
     z_15 >= 3.0,
     f"Z = {z_15:.2f} sigma")

# T6: K=K_bst_min features exceed 5-sigma (by construction)
expected_kmin = K_bst_min + (N_FEATURES - K_bst_min) * coverage_fraction
z_kmin = (expected_kmin - mean_null) / std_null
test("T6: K=K_min features yield >= 5-sigma",
     z_kmin >= 5.0,
     f"K_min={K_bst_min}, Z = {z_kmin:.2f} sigma")

# T7: Minimum K for 5-sigma is reasonable (between 1 and 50)
test("T7: Minimum K for 5-sigma is in [1, 50]",
     1 <= K_bst_min <= 50,
     f"K_min = {K_bst_min}")

# T8: Natural line contamination is low (< 50% of checked lines)
test("T8: Natural line contamination rate < 50%",
     contamination_count / len(natural_lines) < 0.5,
     f"{contamination_count}/{len(natural_lines)} lines contaminated")

# T9: OH line is NOT perfectly 7-smooth (no false positive for water hole)
test("T9: OH/H ratio is not a small 7-smooth rational",
     not oh_smooth or abs(float(oh_frac) - oh_ratio) > 0.001,
     f"OH/H = {oh_ratio:.6f}, nearest = {oh_frac} = {float(oh_frac):.6f}")

# T10: Number of 7-smooth rationals is large enough for rich signal
test("T10: >= 100 in-band 7-smooth rationals (rich signal space)",
     len(in_band_rationals) >= 100,
     f"{len(in_band_rationals)} in-band rationals")

# T11: Signal model always beats null for K >= K_bst_min
all_beat = True
for K in range(K_bst_min, min(K_bst_min + 5, N_FEATURES + 1)):
    exp = K + (N_FEATURES - K) * coverage_fraction
    z = (exp - mean_null) / std_null
    if z < 5.0:
        all_beat = False
test("T11: All K >= K_min give 5-sigma detection",
     all_beat,
     f"Checked K = {K_bst_min} to {min(K_bst_min + 4, N_FEATURES)}")

# T12: 7-smooth numbers up to 200 include all BST integers
bst_ints = [1, N_c, n_C, C_2, g, rank, N_c ** 2, n_C * g]
all_present = all(n in smooth_nums for n in bst_ints)
test("T12: All core BST integers are 7-smooth",
     all_present,
     f"Checked: {bst_ints} all in smooth set: {all_present}")

# ── SCORE ──────────────────────────────────────────────────────
passed = sum(1 for _, p, _ in results if p)
total = len(results)
print(f"\n{'=' * 72}")
print(f"SCORE: {passed}/{total} PASS")
print(f"{'=' * 72}")
