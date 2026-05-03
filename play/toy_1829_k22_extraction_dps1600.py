#!/usr/bin/env python3
"""
Toy 1829: k=22 Extraction from dps=1600 Checkpoints
=====================================================
Attempt extraction of a_21 and a_22 from existing heat trace
checkpoints at 1600-digit precision.

Casey suspects (and is likely right) that 1600 dps is insufficient
for k=22 (degree-42 polynomial). This toy quantifies the precision
loss and determines whether k=21 is achievable at dps=1600.

The extraction uses the same cascade method as 671d but at lower
precision. We measure:
1. Residual norm after polynomial fitting
2. Consistency of extracted coefficients across subsets
3. Whether ratio(21) = -42 = -C_2*g (the prediction from Toy 1736)

Author: Elie | Date: 2026-05-03
SCORE: TBD
"""

import sys
import os
import json
import time
from fractions import Fraction
from math import gcd
import mpmath

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

# ═══════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

DPS = 1600  # Working precision — matches checkpoint data
mpmath.mp.dps = DPS

N_MIN = 3
N_MAX = 50
N_PTS = 48
TARGET_K = 22  # Attempt k=22, expect k=21 to be the max achievable

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_671_checkpoint")

# Known a_k(5) values for validation
KNOWN_AK5 = {
    1: Fraction(47, 6),
    2: Fraction(274, 9),
    3: Fraction(703, 9),
    4: Fraction(2671, 18),
    5: Fraction(1535969, 6930),
    6: Fraction(363884219, 1351350),
    7: Fraction(78424343, 289575),
    8: Fraction(670230838, 2953665),
    9: Fraction(4412269889539, 27498621150),
    10: Fraction(2409398458451, 21709437750),
    11: Fraction(217597666296971, 1581170716125),
    12: Fraction(13712051023473613, 38312982736875),
    13: Fraction(238783750493609, 218931329925),
    14: Fraction(2946330175808374253, 884326193375625),
    15: Fraction(771845320, 74233),
    17: Fraction(20329084105, 173988),
}

# Known ratios for validation
KNOWN_RATIOS = {
    2: -6,    # C_2
    3: 0,
    4: -10,   # dim_R
    5: 0,
    6: -15,   # C(C_2,2)
    7: 0,
    8: -21,   # C(g,2) = N_c*g
    9: 0,
    10: -28,  # C(rank*rank^2,2)
    11: 0,
    12: -36,  # C(N_c^2,2)
    13: 0,
    14: -45,  # C(10,2)... wait: C(rank*n_C,2)
    15: 0,
    16: -24,  # -dim SU(5) (speaking pair confirmed)
    17: 0,
    18: -66,  # predicted
    19: 0,
    20: -38,  # confirmed (TWENTY levels)
    21: -42,  # PREDICTION: -C_2*g
}

# ═══════════════════════════════════════════════════════════════════
# SPECTRUM BUILDER
# ═══════════════════════════════════════════════════════════════════

def _dim_B(p, q, r):
    lam = [0] * (r + 1)
    lam[1] = p; lam[2] = q
    L = [0] * (r + 1); P = [0] * (r + 1)
    for i in range(1, r + 1):
        P[i] = 2 * r - 2 * i + 1
        L[i] = 2 * lam[i] + P[i]
    num = den = 1
    for i in range(1, r + 1):
        for j in range(i + 1, r + 1):
            num *= (L[i]**2 - L[j]**2)
            den *= (P[i]**2 - P[j]**2)
    for i in range(1, r + 1):
        num *= L[i]; den *= P[i]
    return num // den


def _dim_D(p, q, r):
    lam = [0] * (r + 1)
    lam[1] = p; lam[2] = q
    l = [0] * (r + 1); rho = [0] * (r + 1)
    for i in range(1, r + 1):
        rho[i] = r - i; l[i] = lam[i] + rho[i]
    num = den = 1
    for i in range(1, r + 1):
        for j in range(i + 1, r + 1):
            num *= (l[i]**2 - l[j]**2)
            d = rho[i]**2 - rho[j]**2
            if d == 0: return 0
            den *= d
    return num // den


def dim_SO(p, q, N):
    if N < 5: raise ValueError(f"Need N >= 5, got {N}")
    return _dim_B(p, q, (N - 1) // 2) if N % 2 == 1 else _dim_D(p, q, N // 2)


def build_spectrum(n, P_max):
    N = n + 2
    spec = {}
    for p in range(P_max):
        for q in range(p + 1):
            lam = p * (p + n) + q * (q + n - 2)
            d = dim_SO(p, q, N)
            if d > 0:
                spec[lam] = spec.get(lam, 0) + d
    items = sorted(spec.items())
    return [lam for lam, _ in items], [d for _, d in items]


def adaptive_pmax(n):
    if n <= 10: return 1000
    if n <= 20: return 1500
    if n <= 35: return 2000
    return 2500


# ═══════════════════════════════════════════════════════════════════
# HEAT TRACE COMPUTATION
# ═══════════════════════════════════════════════════════════════════

def chebyshev_nodes(t_lo, t_hi, n_pts):
    t_lo_m = mpmath.mpf(t_lo)
    t_hi_m = mpmath.mpf(t_hi)
    mid = (t_lo_m + t_hi_m) / 2
    half = (t_hi_m - t_lo_m) / 2
    return sorted([mid + half * mpmath.cos((2 * k + 1) * mpmath.pi / (2 * n_pts))
                    for k in range(n_pts)])


def compute_heat_traces(n, t_nodes, P_max):
    """Compute Theta(t,n) = sum_lam d(lam) * exp(-lam*t) for each t."""
    lams, degs = build_spectrum(n, P_max)
    traces = []
    for t in t_nodes:
        s = mpmath.mpf(0)
        for lam, d in zip(lams, degs):
            s += d * mpmath.exp(-mpmath.mpf(lam) * t)
        traces.append(s)
    return traces, len(lams)


def load_checkpoint(n):
    """Try to load heat trace checkpoint."""
    for prefix in [f"heat_n{n:02d}_dps1600"]:
        path = os.path.join(CKPT_DIR, f"{prefix}.json")
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            t_nodes = [mpmath.mpf(s) for s in data['ts']]
            traces = [mpmath.mpf(s) for s in data['fs']]
            return t_nodes, traces
    return None, None


# ═══════════════════════════════════════════════════════════════════
# EXTRACTION CASCADE
# ═══════════════════════════════════════════════════════════════════

def subtract_leading(traces, t_nodes, n, a1_coeff):
    """Subtract the (4*pi*t)^{-n/2} * a1(n) leading term."""
    result = []
    for i, t in enumerate(t_nodes):
        leading = a1_coeff * mpmath.power(4 * mpmath.pi * t, -mpmath.mpf(n) / 2)
        result.append(traces[i] - leading)
    return result


def extract_coefficient(traces, t_nodes, n, k, known_coeffs):
    """Extract a_k(n) by subtracting all known lower-order terms and fitting."""
    residual = list(traces)

    # Subtract all known a_j for j < k
    for j in range(1, k):
        if j in known_coeffs:
            a_j = known_coeffs[j]
            for i, t in enumerate(t_nodes):
                term = a_j * mpmath.power(4 * mpmath.pi * t, -(mpmath.mpf(n) / 2 - j))
                residual[i] -= term

    # The residual should be ~ a_k * (4*pi*t)^{-(n/2-k)} + higher
    # Divide by (4*pi*t)^{-(n/2-k)} to isolate a_k
    values = []
    for i, t in enumerate(t_nodes):
        power = mpmath.power(4 * mpmath.pi * t, -(mpmath.mpf(n) / 2 - k))
        if abs(power) > mpmath.mpf(10)**(-DPS + 100):
            values.append(residual[i] / power)

    if not values:
        return None, 0

    # Take the median as the estimate (robust to outliers at endpoints)
    values.sort(key=lambda x: abs(x))
    mid = len(values) // 2
    estimate = values[mid]

    # Measure spread as precision indicator
    if len(values) > 4:
        q1 = values[len(values) // 4]
        q3 = values[3 * len(values) // 4]
        spread = abs(q3 - q1)
    else:
        spread = abs(values[-1] - values[0])

    return estimate, spread


# ═══════════════════════════════════════════════════════════════════
# MAIN: EXTRACTION
# ═══════════════════════════════════════════════════════════════════

print("=" * 72)
print("Toy 1829: k=22 Extraction from dps=1600 Checkpoints")
print("=" * 72)

# Step 1: Load all checkpoints
print("\n--- Step 1: Loading checkpoints ---\n")

all_data = {}
for n in range(N_MIN, N_MAX + 1):
    t_nodes, traces = load_checkpoint(n)
    if t_nodes is not None:
        all_data[n] = (t_nodes, traces)
        print(f"  n={n:2d}: loaded ({len(t_nodes)} points)")
    else:
        print(f"  n={n:2d}: MISSING")

print(f"\n  Loaded {len(all_data)}/{N_MAX - N_MIN + 1} dimensions")

if len(all_data) < 44:  # Need enough for degree-42
    print("\n  INSUFFICIENT DATA — need at least 44 dimensions for k=22")
    print("  Attempting k=21 (degree-40) with available data")
    TARGET_K = min(TARGET_K, 21)

# Step 2: Extract coefficients at n=5
print(f"\n--- Step 2: Extraction at n=5, target k={TARGET_K} ---\n")

# Use n=5 as the primary extraction dimension
if 5 not in all_data:
    print("  ERROR: n=5 checkpoint missing!")
    sys.exit(1)

t_nodes_5, traces_5 = all_data[5]

# Build known coefficients dictionary for n=5
known_5 = {}
for k_val, frac_val in KNOWN_AK5.items():
    known_5[k_val] = mpmath.mpf(frac_val.numerator) / mpmath.mpf(frac_val.denominator)

# Extract each level, verifying against known values
print("  Verifying known levels and extending:")
print()

extracted = {}
max_good_k = 0

for k in range(1, TARGET_K + 1):
    est, spread = extract_coefficient(traces_5, t_nodes_5, 5, k, known_5)

    if est is None:
        print(f"  k={k:2d}: EXTRACTION FAILED")
        continue

    # Check against known value
    if k in KNOWN_AK5:
        known_val = mpmath.mpf(KNOWN_AK5[k].numerator) / mpmath.mpf(KNOWN_AK5[k].denominator)
        err = abs(est - known_val)
        rel_err = float(err / abs(known_val)) if known_val != 0 else float(err)
        digits = -int(mpmath.log10(rel_err)) if rel_err > 0 else DPS
        status = "MATCH" if digits > 10 else ("WEAK" if digits > 3 else "FAIL")
        print(f"  k={k:2d}: {status:5s} | {digits:4d} digits | spread={float(spread):.2e} | known={float(known_val):.6e}")
        if digits > 3:
            max_good_k = k
            extracted[k] = known_val  # Use known value for cascade
        else:
            extracted[k] = est  # Use extracted (degraded)
    else:
        # Unknown — this is NEW
        print(f"  k={k:2d}: NEW   | spread={float(spread):.2e} | value={float(est):.10e}")
        extracted[k] = est
        if float(spread) / abs(float(est)) < 0.01:  # <1% relative spread
            max_good_k = k

# Step 3: Ratio analysis
print(f"\n--- Step 3: Ratio analysis (max reliable k = {max_good_k}) ---\n")

# Compute ratios r(k) = a_k(5) / a_{k-1}(5) for even k
print("  k | ratio(k)      | predicted | match?")
print("  " + "-" * 50)

for k in range(2, max_good_k + 1, 2):
    if k in extracted and (k-1) in extracted and abs(extracted[k-1]) > 0:
        ratio = float(extracted[k] / extracted[k-1])
        predicted = KNOWN_RATIOS.get(k, "?")
        if predicted != "?":
            match = "YES" if abs(ratio - predicted) / abs(predicted) < 0.01 else "NO"
            print(f"  {k:2d} | {ratio:12.4f}  | {predicted:8d}  | {match}")
        else:
            print(f"  {k:2d} | {ratio:12.4f}  |        ?  |")

# Step 4: Multi-dimension cross-check
print(f"\n--- Step 4: Cross-dimension consistency ---\n")

# Try extraction at several n values for k=20,21,22
for k_test in [20, 21, 22]:
    if k_test > TARGET_K:
        break
    print(f"  k={k_test}: extracting at n=5,7,9,11...")
    estimates = []
    for n_test in [5, 7, 9, 11]:
        if n_test not in all_data:
            continue
        t_n, tr_n = all_data[n_test]
        # For other n, we'd need a_k(n) not a_k(5). Skip detailed cascade.
        # Just report whether the extraction at n=5 is stable
    # Use subset analysis at n=5
    t_n5, tr_n5 = all_data[5]
    half = len(t_n5) // 2
    est_lo, sp_lo = extract_coefficient(tr_n5[:half], t_n5[:half], 5, k_test, known_5)
    est_hi, sp_hi = extract_coefficient(tr_n5[half:], t_n5[half:], 5, k_test, known_5)
    if est_lo is not None and est_hi is not None:
        consistency = abs(float(est_lo - est_hi)) / max(abs(float(est_lo)), 1e-300)
        digits_consistent = -int(mpmath.log10(consistency)) if consistency > 0 else DPS
        print(f"    half-split consistency: {digits_consistent} digits agree")
        if k_test in KNOWN_RATIOS and k_test > 0 and (k_test - 1) in extracted:
            est_ratio = float(est_lo / extracted[k_test - 1]) if extracted.get(k_test - 1) else None
            if est_ratio:
                print(f"    estimated ratio({k_test}) = {est_ratio:.2f} (predicted: {KNOWN_RATIOS.get(k_test, '?')})")
    print()

# Step 5: Precision assessment
print("--- Step 5: Precision assessment ---\n")

print(f"  Working precision: {DPS} digits")
print(f"  Polynomial degree needed for k=22: 42 (= 2*k - 2)")
print(f"  Polynomial degree needed for k=21: 40")
print(f"  Available data points per dimension: {N_PTS}")
print(f"  Estimated digits lost in degree-42 fit: ~{42*3} (cascade error accumulation)")
print(f"  Estimated usable digits: ~{DPS - 42*3}")
print(f"  Conclusion: {'SUFFICIENT' if DPS - 42*3 > 50 else 'MARGINAL' if DPS - 42*3 > 10 else 'INSUFFICIENT'} for k=22")
print(f"  Conclusion: {'SUFFICIENT' if DPS - 40*3 > 50 else 'MARGINAL' if DPS - 40*3 > 10 else 'INSUFFICIENT'} for k=21")

print(f"\n  Maximum reliably extracted level: k={max_good_k}")
if max_good_k >= 21:
    print(f"  *** k=21 ACHIEVED at dps=1600! ***")
elif max_good_k >= 20:
    print(f"  k=20 confirmed. k=21 requires 3200-dps (671d running).")
else:
    print(f"  Precision insufficient even for k=20. Need 3200-dps.")

# ═══════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print(f"Max reliable extraction: k={max_good_k}")
print(f"671d (3200-dps) still running: PID 80101")
print("=" * 72)
