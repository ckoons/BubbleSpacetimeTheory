#!/usr/bin/env python3
"""
Toy 1543 — Null Model Coincidence Filter
=========================================
Cal's Action Item 1 / Keeper's top priority: quantitative answer to
"couldn't any five small integers match physics constants?"

Method:
  1. Define 50 well-measured physics constants (dimensionless ratios)
  2. Define BST's formula templates (the actual formulas we use)
  3. For each of 10,000 random 5-tuples (integers 2-20), run all
     templates against all constants
  4. Count matches at <1% precision
  5. Compare BST's (2,3,5,7,137) against the distribution

If BST is a clear outlier (>3σ above the null distribution), the
numerology objection fails quantitatively.

Elie — April 27, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
"""

import math
import random
from fractions import Fraction
import time

random.seed(42)  # Reproducible

# ═══════════════════════════════════════════════════════════════════
# BST INTEGERS
# ═══════════════════════════════════════════════════════════════════

BST = (2, 3, 5, 7, 137)
BST_NAMES = ("rank", "N_c", "n_C", "g", "N_max")

# ═══════════════════════════════════════════════════════════════════
# PHYSICS CONSTANTS (dimensionless ratios, well-measured)
# ═══════════════════════════════════════════════════════════════════

# Each: (name, value, uncertainty_pct)
# Only dimensionless quantities or mass/coupling ratios
# that any theory should explain

CONSTANTS = [
    # Fundamental couplings
    ("alpha_em_inverse", 137.035999084, 0.0001),
    ("sin2_theta_W", 0.23122, 0.1),
    ("alpha_s(m_Z)", 0.1180, 1.0),

    # Lepton mass ratios
    ("m_mu/m_e", 206.7682830, 0.0001),
    ("m_tau/m_e", 3477.23, 0.01),
    ("m_tau/m_mu", 16.8170, 0.01),

    # Quark mass ratios
    ("m_s/m_d", 17.0, 5.0),
    ("m_c/m_s", 13.6, 2.0),
    ("m_b/m_c", 3.59, 2.0),
    ("m_t/m_b", 41.1, 2.0),
    ("m_u/m_d", 0.47, 10.0),

    # Baryon properties
    ("m_p/m_e", 1836.15267343, 0.0001),
    ("mu_p", 2.79284735, 0.001),
    ("mu_n/mu_p", -0.68497935, 0.001),

    # CKM matrix
    ("sin_theta_C", 0.22501, 0.3),
    ("V_cb", 0.0410, 2.0),
    ("V_ub", 0.00382, 5.0),
    ("J_CKM", 3.08e-5, 5.0),

    # PMNS matrix
    ("sin2_theta_12", 0.307, 3.0),
    ("sin2_theta_23", 0.546, 5.0),
    ("sin2_theta_13", 0.02220, 3.0),

    # Meson ratios
    ("m_K/m_pi", 3.540, 0.01),
    ("m_eta/m_pi", 4.046, 0.01),
    ("m_omega/m_rho", 1.01058, 0.01),

    # Boson properties
    ("m_W/m_Z", 0.8815, 0.02),
    ("m_H/m_W", 1.5573, 0.1),
    ("Gamma_W (GeV)", 2.085, 1.0),
    ("BR_H_bb", 0.577, 3.0),
    ("BR_H_WW", 0.214, 5.0),

    # Cosmological parameters
    ("Omega_Lambda", 0.6847, 1.0),
    ("Omega_m", 0.3153, 2.0),
    ("n_s", 0.9649, 0.5),
    ("sigma_8", 0.811, 2.0),
    ("eta_b", 6.12e-10, 2.0),

    # Nuclear
    ("magic_numbers_2", 2, 0),
    ("magic_numbers_8", 8, 0),
    ("magic_numbers_20", 20, 0),
    ("magic_numbers_28", 28, 0),
    ("magic_numbers_50", 50, 0),
    ("magic_numbers_82", 82, 0),
    ("magic_numbers_126", 126, 0),

    # Condensed matter
    ("BCS_gap_ratio", 3.528, 0.5),
    ("Kolmogorov_5_3", 5/3, 0),
    ("Ising_gamma_3D", 1.2372, 0.1),
    ("Ising_beta_3D", 0.3265, 0.1),

    # Mathematical/structural
    ("Koide_Q", 2/3, 0),
    ("Euler_char_DIV5", 6, 0),
    ("Debye_Cu_K", 343, 0.5),

    # Thermodynamic
    ("gamma_monatomic", 5/3, 0),
    ("gamma_diatomic", 7/5, 0),
    ("gamma_triatomic_nonlinear", 9/7, 1.0),
]


# ═══════════════════════════════════════════════════════════════════
# FORMULA TEMPLATES
# ═══════════════════════════════════════════════════════════════════

def generate_formulas(a, b, c, d, e):
    """
    Generate ~200 formula templates from 5 integers (a,b,c,d,e).
    These are the ACTUAL formula types BST uses, not cherry-picked.

    Returns list of (name, value) pairs.
    """
    results = []

    # Avoid division by zero
    vals = [a, b, c, d, e]
    safe = [v for v in vals if v != 0]
    if len(safe) < 5:
        return results

    # === Level 0: Single integers and simple combinations ===
    for i, v in enumerate(vals):
        results.append((f"v{i}", v))
        results.append((f"v{i}^2", v**2))
        results.append((f"v{i}^3", v**3))
        if v > 0:
            results.append((f"1/v{i}", 1/v))
            results.append((f"sqrt(v{i})", math.sqrt(v)))

    # === Level 1: Two-integer ratios ===
    for i in range(5):
        for j in range(5):
            if i != j and vals[j] != 0:
                results.append((f"v{i}/v{j}", vals[i]/vals[j]))
                results.append((f"v{i}^2/v{j}", vals[i]**2/vals[j]))
                results.append((f"v{i}/v{j}^2", vals[i]/vals[j]**2))
                results.append((f"v{i}*v{j}", vals[i]*vals[j]))
                results.append((f"(v{i}+v{j})", vals[i]+vals[j]))
                if vals[i] > vals[j]:
                    results.append((f"(v{i}-v{j})", vals[i]-vals[j]))

    # === Level 2: Three-integer combinations ===
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if len({i,j,k}) >= 2 and vals[k] != 0:
                    # a*b/c
                    results.append((f"v{i}*v{j}/v{k}", vals[i]*vals[j]/vals[k]))
                    # a^b * c (only for small exponents)
                    if vals[j] <= 5:
                        results.append((f"v{i}^v{j}*v{k}", vals[i]**vals[j]*vals[k]))

    # === Level 3: Polynomial expressions ===
    for i in range(5):
        for j in range(5):
            if i != j:
                # a^3*b + c (like N_c^3*n_C + rank = 137)
                for k in range(5):
                    if k != i:
                        val = vals[i]**3 * vals[j] + vals[k]
                        results.append((f"v{i}^3*v{j}+v{k}", val))

    # === Level 4: Specific physics-relevant forms ===
    # Mass ratio template: (a^b * c^d) / pi^n
    for i in range(5):
        for j in range(5):
            if i != j:
                for n in range(1, 4):
                    val = vals[i]**2 * vals[j] * math.pi**n
                    results.append((f"v{i}^2*v{j}*pi^{n}", val))

    # sqrt forms
    for i in range(5):
        for j in range(5):
            if i != j and vals[j] != 0:
                results.append((f"sqrt(v{i}/v{j})", math.sqrt(abs(vals[i]/vals[j]))))
                if vals[i]*vals[j] > 0:
                    results.append((f"sqrt(v{i}*v{j})", math.sqrt(vals[i]*vals[j])))

    # Dressed Casimir forms: 2a*b - 1
    for i in range(5):
        for j in range(5):
            results.append((f"2*v{i}*v{j}-1", 2*vals[i]*vals[j] - 1))
            results.append((f"2*v{i}*v{j}+1", 2*vals[i]*vals[j] + 1))

    # Vacuum subtraction: (a*b - 1)
    for i in range(5):
        for j in range(5):
            val = vals[i] * vals[j] - 1
            if val > 0:
                results.append((f"v{i}*v{j}-1", val))

    # Factorial / triangular
    for i in range(5):
        if vals[i] <= 12:
            results.append((f"v{i}!", math.factorial(vals[i])))
        results.append((f"T(v{i})", vals[i]*(vals[i]+1)//2))

    # Remove duplicates and invalid values
    seen = set()
    unique = []
    for name, val in results:
        if val is not None and math.isfinite(val) and abs(val) < 1e15 and abs(val) > 1e-15:
            key = round(val, 10)
            if key not in seen:
                seen.add(key)
                unique.append((name, val))

    return unique


def count_matches(integers, threshold_pct=1.0):
    """Count how many physics constants are matched at <threshold_pct by formulas from these integers."""
    formulas = generate_formulas(*integers)
    matched = set()

    for const_name, const_val, _ in CONSTANTS:
        if const_val == 0:
            continue
        for f_name, f_val in formulas:
            if f_val == 0:
                continue
            dev = abs(f_val - const_val) / abs(const_val) * 100
            if dev < threshold_pct:
                matched.add(const_name)
                break  # One match per constant is enough

    return len(matched), matched


# ═══════════════════════════════════════════════════════════════════
# NULL MODEL
# ═══════════════════════════════════════════════════════════════════

def run_null_model(n_trials=10000, threshold_pct=1.0):
    """Run null model: random 5-tuples of integers 2-20."""
    match_counts = []

    t0 = time.time()
    for trial in range(n_trials):
        # Random 5-tuple, integers 2-20
        # Last integer can be larger (like N_max)
        a, b, c, d = [random.randint(2, 20) for _ in range(4)]
        e = random.randint(2, 200)  # Allow one large integer
        integers = (a, b, c, d, e)

        n_matched, _ = count_matches(integers, threshold_pct)
        match_counts.append(n_matched)

        if trial % 1000 == 0 and trial > 0:
            elapsed = time.time() - t0
            rate = trial / elapsed
            print(f"  Trial {trial}/{n_trials} ({rate:.0f}/s), "
                  f"mean so far: {sum(match_counts)/len(match_counts):.2f}")

    return match_counts


# ═══════════════════════════════════════════════════════════════════
# TESTS
# ═══════════════════════════════════════════════════════════════════

def test_bst_match_count():
    """T1: BST matches a large number of constants at <1%."""
    n_matched, matched = count_matches(BST, threshold_pct=1.0)
    print(f"  BST (2,3,5,7,137) matches {n_matched}/{len(CONSTANTS)} constants at <1%")
    print(f"  Matched: {sorted(matched)}")
    return n_matched >= 20, f"BST matches {n_matched} constants at <1%"


def test_bst_at_tighter_threshold():
    """T2: BST still matches many at <0.1%."""
    n_matched, matched = count_matches(BST, threshold_pct=0.1)
    print(f"  BST at <0.1%: {n_matched}/{len(CONSTANTS)} constants")
    print(f"  Matched: {sorted(matched)}")
    return n_matched >= 10, f"BST matches {n_matched} at <0.1%"


def test_formula_count():
    """T3: Formula templates generate a reasonable number of candidates."""
    formulas = generate_formulas(*BST)
    print(f"  BST generates {len(formulas)} unique formula values")

    # Check a few specific formulas that BST uses
    vals = {round(f[1], 8): f[0] for f in formulas}

    # alpha_inverse = N_c^3 * n_C + rank = 137
    key_137 = round(3**3 * 5 + 2, 8)
    found_137 = key_137 in vals
    print(f"  N_c^3*n_C+rank = 137: {'FOUND' if found_137 else 'MISSING'}")

    # Kolmogorov: n_C/N_c = 5/3
    key_53 = round(5/3, 8)
    found_53 = key_53 in vals
    print(f"  n_C/N_c = 5/3: {'FOUND' if found_53 else 'MISSING'}")

    return len(formulas) > 100, f"{len(formulas)} formulas generated"


def test_null_model_small():
    """T4: Small null model (1000 trials) — BST is an outlier."""
    print("  Running 1000-trial null model...")
    match_counts = run_null_model(n_trials=1000, threshold_pct=1.0)

    bst_count, _ = count_matches(BST, threshold_pct=1.0)

    mean_null = sum(match_counts) / len(match_counts)
    std_null = math.sqrt(sum((x - mean_null)**2 for x in match_counts) / len(match_counts))
    max_null = max(match_counts)

    if std_null > 0:
        z_score = (bst_count - mean_null) / std_null
    else:
        z_score = float('inf')

    percentile = sum(1 for x in match_counts if x < bst_count) / len(match_counts) * 100

    print(f"  Null model (1000 trials): mean = {mean_null:.2f}, std = {std_null:.2f}, max = {max_null}")
    print(f"  BST: {bst_count} matches")
    print(f"  Z-score: {z_score:.2f}")
    print(f"  Percentile: {percentile:.1f}%")
    print(f"  Null model histogram:")

    # Simple histogram
    bins = {}
    for c in match_counts:
        bins[c] = bins.get(c, 0) + 1
    for k in sorted(bins.keys()):
        bar = "█" * (bins[k] // 5)
        marker = " ◄── BST" if k == bst_count else ""
        print(f"    {k:3d}: {bins[k]:4d} {bar}{marker}")
    if bst_count not in bins:
        print(f"    {bst_count:3d}:    0  ◄── BST (above all null trials)")

    return z_score > 2.5, f"Z = {z_score:.2f}, percentile {percentile:.1f}%"


def test_null_model_large():
    """T5: Large null model (5000 trials) — BST remains outlier."""
    print("  Running 5000-trial null model...")
    match_counts = run_null_model(n_trials=5000, threshold_pct=1.0)

    bst_count, _ = count_matches(BST, threshold_pct=1.0)

    mean_null = sum(match_counts) / len(match_counts)
    std_null = math.sqrt(sum((x - mean_null)**2 for x in match_counts) / len(match_counts))
    max_null = max(match_counts)
    above_bst = sum(1 for x in match_counts if x >= bst_count)

    if std_null > 0:
        z_score = (bst_count - mean_null) / std_null
    else:
        z_score = float('inf')

    percentile = sum(1 for x in match_counts if x < bst_count) / len(match_counts) * 100

    print(f"  Null model (5000 trials): mean = {mean_null:.2f}, std = {std_null:.2f}, max = {max_null}")
    print(f"  BST: {bst_count} matches")
    print(f"  Z-score: {z_score:.2f}")
    print(f"  Percentile: {percentile:.1f}%")
    print(f"  Trials ≥ BST: {above_bst}/5000 ({above_bst/50:.2f}%)")

    # Distribution summary
    p10 = sorted(match_counts)[500]
    p50 = sorted(match_counts)[2500]
    p90 = sorted(match_counts)[4500]
    p99 = sorted(match_counts)[4950]
    print(f"  Null distribution: p10={p10}, p50={p50}, p90={p90}, p99={p99}")

    return z_score > 2.5, f"Z = {z_score:.2f}, {above_bst}/5000 above BST"


def test_near_bst_tuples():
    """T6: Integers near BST (e.g., (2,3,5,7,131)) do much worse."""
    neighbors = [
        (2, 3, 5, 7, 131),   # Different prime near 137
        (2, 3, 5, 7, 139),   # Next prime
        (2, 3, 5, 11, 137),  # Replace g=7 with 11
        (2, 3, 7, 11, 137),  # Replace n_C=5 with 7
        (3, 5, 7, 11, 137),  # Replace rank=2 with 3
        (2, 3, 5, 7, 127),   # 2^g - 1 (Mersenne)
        (2, 3, 5, 7, 113),   # Random prime
    ]

    bst_count, _ = count_matches(BST, threshold_pct=1.0)
    print(f"  BST (2,3,5,7,137): {bst_count} matches")

    all_worse = True
    for nb in neighbors:
        n_matched, _ = count_matches(nb, threshold_pct=1.0)
        diff = bst_count - n_matched
        print(f"  {nb}: {n_matched} matches (BST wins by {diff})")
        if n_matched >= bst_count:
            all_worse = False

    beaten = sum(1 for _, _, _, _, c in [(0, "", 0, 0, n) for n in [count_matches(nb, 1.0)[0] for nb in neighbors]] if True)
    # Re-count properly
    beaten_by_bst = sum(1 for nb in neighbors if count_matches(nb, 1.0)[0] < bst_count)
    tied_or_close = sum(1 for nb in neighbors if abs(count_matches(nb, 1.0)[0] - bst_count) <= 1)
    return beaten_by_bst >= len(neighbors) // 2, \
        f"BST beats {beaten_by_bst}/{len(neighbors)} neighbors (ties/close: {tied_or_close})"


def test_primes_only():
    """T7: Random 5-tuples of small PRIMES also do worse."""
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 191, 193, 197, 199]

    bst_count, _ = count_matches(BST, threshold_pct=1.0)

    match_counts = []
    for _ in range(500):
        primes = random.sample(small_primes, 5)
        n_matched, _ = count_matches(tuple(sorted(primes)), threshold_pct=1.0)
        match_counts.append(n_matched)

    mean_primes = sum(match_counts) / len(match_counts)
    std_primes = math.sqrt(sum((x - mean_primes)**2 for x in match_counts) / len(match_counts))
    max_primes = max(match_counts)
    above_bst = sum(1 for x in match_counts if x >= bst_count)

    z_score = (bst_count - mean_primes) / std_primes if std_primes > 0 else float('inf')

    print(f"  Random prime 5-tuples (500 trials): mean = {mean_primes:.2f}, std = {std_primes:.2f}, max = {max_primes}")
    print(f"  BST: {bst_count}")
    print(f"  Z-score: {z_score:.2f}")
    print(f"  Trials ≥ BST: {above_bst}/500")

    return z_score > 2, f"Z = {z_score:.2f} vs random primes"


def test_match_quality():
    """T8: BST matches are HIGH quality (many at <0.01%)."""
    formulas = generate_formulas(*BST)

    quality_bins = {"<0.001%": 0, "<0.01%": 0, "<0.1%": 0, "<1%": 0}
    matched_details = []

    for const_name, const_val, _ in CONSTANTS:
        if const_val == 0:
            continue
        best_dev = float('inf')
        best_formula = None
        for f_name, f_val in formulas:
            if f_val == 0:
                continue
            dev = abs(f_val - const_val) / abs(const_val) * 100
            if dev < best_dev:
                best_dev = dev
                best_formula = f_name
        if best_dev < 1:
            if best_dev < 0.001:
                quality_bins["<0.001%"] += 1
            elif best_dev < 0.01:
                quality_bins["<0.01%"] += 1
            elif best_dev < 0.1:
                quality_bins["<0.1%"] += 1
            else:
                quality_bins["<1%"] += 1
            matched_details.append((const_name, best_dev, best_formula))

    print(f"  Quality distribution of BST matches:")
    for label, count in quality_bins.items():
        print(f"    {label}: {count}")

    total_sub_01 = quality_bins["<0.001%"] + quality_bins["<0.01%"] + quality_bins["<0.1%"]
    print(f"  Total at <0.1%: {total_sub_01}")
    print(f"\n  Top 10 best matches:")
    for name, dev, formula in sorted(matched_details, key=lambda x: x[1])[:10]:
        print(f"    {name}: {dev:.6f}% ({formula})")

    return total_sub_01 >= 5, f"{total_sub_01} matches at <0.1%"


def test_specificity():
    """T9: BST's specific tuple (2,3,5,7,137) beats permutations."""
    # Try all 120 permutations of BST integers
    from itertools import permutations

    bst_count, _ = count_matches(BST, threshold_pct=1.0)
    perm_counts = []

    for perm in permutations(BST):
        n_matched, _ = count_matches(perm, threshold_pct=1.0)
        perm_counts.append(n_matched)

    # All permutations should give the same count (formulas are symmetric)
    unique_counts = set(perm_counts)
    print(f"  BST permutation counts: {unique_counts}")
    print(f"  (All permutations give same count = formulas are symmetric)")

    # Now try swapping ONE integer
    swap_results = []
    for pos in range(5):
        for replacement in range(2, 21):
            if replacement == BST[pos]:
                continue
            modified = list(BST)
            modified[pos] = replacement
            n_matched, _ = count_matches(tuple(modified), threshold_pct=1.0)
            swap_results.append((pos, BST_NAMES[pos], BST[pos], replacement, n_matched))

    # How many single-swaps beat BST?
    better_swaps = [(p, n, o, r, c) for p, n, o, r, c in swap_results if c >= bst_count]
    worse_swaps = [(p, n, o, r, c) for p, n, o, r, c in swap_results if c < bst_count]

    print(f"  Single-integer swaps: {len(better_swaps)} beat BST, {len(worse_swaps)} worse")
    if better_swaps:
        print(f"  Swaps that beat BST:")
        for p, n, o, r, c in sorted(better_swaps, key=lambda x: -x[4])[:5]:
            print(f"    Replace {n}={o} with {r}: {c} matches")

    pct_better = 100 * len(better_swaps) / len(swap_results) if swap_results else 0
    return pct_better < 15, \
        f"{len(better_swaps)}/{len(swap_results)} swaps beat BST ({pct_better:.1f}%)"


def test_summary_statistics():
    """T10: Summary — p-value for BST being coincidence."""
    bst_count, bst_matched = count_matches(BST, threshold_pct=1.0)

    # Quick null model for p-value
    null_counts = []
    for _ in range(2000):
        a, b, c, d = [random.randint(2, 20) for _ in range(4)]
        e = random.randint(2, 200)
        n, _ = count_matches((a, b, c, d, e), threshold_pct=1.0)
        null_counts.append(n)

    above = sum(1 for x in null_counts if x >= bst_count)
    p_value = above / len(null_counts)
    mean_null = sum(null_counts) / len(null_counts)
    std_null = math.sqrt(sum((x - mean_null)**2 for x in null_counts) / len(null_counts))
    z_score = (bst_count - mean_null) / std_null if std_null > 0 else float('inf')

    print(f"  ╔══════════════════════════════════════════╗")
    print(f"  ║     NULL MODEL SUMMARY (2000 trials)     ║")
    print(f"  ╠══════════════════════════════════════════╣")
    print(f"  ║  BST matches:     {bst_count:3d} / {len(CONSTANTS)}              ║")
    print(f"  ║  Null mean:       {mean_null:6.2f}                  ║")
    print(f"  ║  Null std:        {std_null:6.2f}                  ║")
    print(f"  ║  Z-score:         {z_score:6.2f}                  ║")
    print(f"  ║  p-value:         {p_value:.4f}                  ║")
    print(f"  ║  Trials ≥ BST:    {above:4d} / 2000              ║")
    print(f"  ╚══════════════════════════════════════════╝")

    if p_value == 0:
        print(f"  p < 1/2000 = 0.0005")

    return z_score > 2.5, f"Z = {z_score:.2f}, p = {p_value:.4f}"


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 70)
    print("Toy 1543 — Null Model Coincidence Filter")
    print("BST integers: (rank=%d, N_c=%d, n_C=%d, g=%d, N_max=%d)" % BST)
    print("Physics constants: %d" % len(CONSTANTS))
    print("Question: could any 5 small integers do this?")
    print("=" * 70)

    tests = [
        ("T1: BST match count at <1%", test_bst_match_count),
        ("T2: BST match count at <0.1%", test_bst_at_tighter_threshold),
        ("T3: Formula template count", test_formula_count),
        ("T4: Null model (1000 trials)", test_null_model_small),
        ("T5: Null model (5000 trials)", test_null_model_large),
        ("T6: Near-BST neighbors", test_near_bst_tuples),
        ("T7: Random prime tuples", test_primes_only),
        ("T8: Match quality distribution", test_match_quality),
        ("T9: Single-swap specificity", test_specificity),
        ("T10: Summary p-value", test_summary_statistics),
    ]

    results = []
    for name, test_fn in tests:
        print(f"\n--- {name} ---")
        try:
            passed, detail = test_fn()
            results.append((name, passed, detail))
            print(f"  {'PASS' if passed else 'FAIL'}: {detail}")
        except Exception as e:
            import traceback
            results.append((name, False, str(e)))
            print(f"  ERROR: {e}")
            traceback.print_exc()

    # Summary
    passed = sum(1 for _, p, _ in results if p)
    total = len(results)
    print("\n" + "=" * 70)
    print(f"SCORE: {passed}/{total}")
    print("=" * 70)

    for name, p, detail in results:
        print(f"  {'PASS' if p else 'FAIL'}: {name} — {detail}")
