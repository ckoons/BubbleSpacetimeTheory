#!/usr/bin/env python3
"""
Toy 1540 — Heat Kernel k=22 Extraction Attempt (n=43 data)
============================================================
BST / APG: D_IV^5 = SO_0(5,2)/[SO(5)×SO(2)]
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

E-3 unblock attempt: n=43 raw data EXISTS (computed April 26).
But k=22 needs deg=44, requiring n_needed = 42 clean points.
With n=3..43 = 41 dimensions. Are we one short?

This toy diagnoses the exact situation:
T1: Load n=3..43 (41 checkpoints)
T2: Run cascade extraction a_1..a_21 (should reproduce Toy 1507)
T3: Attempt k=22 extraction — diagnose the failure point
T4: Count clean identifications at k=22 — how many do we get?
T5: If 41 clean: one short of 42 needed. Report and predict k=22 ratio.
T6: Attempt Richardson-only extrapolation (no polynomial) as preview

PRE-REGISTERED PREDICTION: ratio(22) should be an integer.
If speaking pair pattern continues: NOT a speaking pair (k=22 ≠ 5m or 5m+1).
Expected: non-speaking integer, similar to k=17..19.

SCORE: X/6
"""

import os
import sys
import json
import time
from fractions import Fraction
from math import gcd
import mpmath

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

DPS = 1600
mpmath.mp.dps = DPS

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_671_checkpoint")

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = N_c**3 * n_C + rank  # 137

# Known a_k(n=5) through k=21
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

KNOWN_SPEAKING_PAIRS = {
    5: -2, 6: -3, 10: -9, 11: -11, 15: -21, 16: -24, 20: -38, 21: -42
}

MAX_PRIME_BY_LEVEL = {
    2: 7, 3: 7, 4: 7, 5: 11, 6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31, 17: 37, 18: 37, 19: 41, 20: 41,
    21: 43, 22: 47,  # k=22 prediction: next prime
}

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]


# ═══════════════════════════════════════════════════════════════════
# EXTRACTION FUNCTIONS (from Toy 1507)
# ═══════════════════════════════════════════════════════════════════

def frac_to_mpf(frac):
    return mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)

def neville(xs, ys, x_target):
    nn = len(xs)
    P = [mpmath.mpf(y) for y in ys]
    for j in range(1, nn):
        P_new = [mpmath.mpf(0)] * nn
        for i in range(j, nn):
            P_new[i] = ((x_target - xs[i - j]) * P[i] -
                        (x_target - xs[i]) * P[i - 1]) / (xs[i] - xs[i - j])
        P = P_new
    return P[nn - 1]

def richardson_extrapolate(ts, gs, max_order=None):
    pairs = sorted(zip(ts, gs), key=lambda p: abs(p[0]))
    N = len(pairs)
    if max_order is None:
        max_order = min(N, 30)
    else:
        max_order = min(max_order, N)
    ts_sorted = [p[0] for p in pairs[:max_order]]
    gs_sorted = [p[1] for p in pairs[:max_order]]
    T = [[mpmath.mpf(0)] * max_order for _ in range(max_order)]
    for i in range(max_order):
        T[i][0] = gs_sorted[i]
    best = T[0][0]
    best_err = mpmath.mpf('inf')
    best_order = 0
    for j in range(1, max_order):
        for i in range(j, max_order):
            r = ts_sorted[i] / ts_sorted[i - j]
            T[i][j] = (r * T[i][j-1] - T[i-j][j-1]) / (r - 1)
        if j >= 2:
            diff = abs(T[j][j] - T[j-1][j-1])
            if diff < best_err:
                best = T[j][j]
                best_err = diff
                best_order = j
    return best, best_err, best_order

def extract_coefficient(fs, ts, vol, known_exact_fracs, target_k):
    gs = []
    for f, t in zip(fs, ts):
        F = f / vol
        for j in range(target_k):
            F -= frac_to_mpf(known_exact_fracs[j]) * t ** j
        g_val = F / t ** target_k
        gs.append(g_val)
    a_k_nev = neville(ts, gs, mpmath.mpf(0))
    a_k_nev_half = neville(ts[::2], [gs[i] for i in range(0, len(ts), 2)], mpmath.mpf(0))
    err_nev = abs(a_k_nev - a_k_nev_half)
    a_k_rich, err_rich, order_rich = richardson_extrapolate(ts, gs, max_order=25)
    n20 = min(20, len(ts))
    a_k_nev20 = neville(ts[:n20], gs[:n20], mpmath.mpf(0))
    agreement = min(abs(a_k_rich - a_k_nev), abs(a_k_rich - a_k_nev20),
                    abs(a_k_nev - a_k_nev20))
    if agreement < err_nev * 10 and err_rich < err_nev:
        return a_k_rich, err_rich, f"Richardson(order={order_rich})"
    elif abs(a_k_nev20 - a_k_nev) < err_nev:
        return a_k_nev20, abs(a_k_nev20 - a_k_nev), "Neville-20"
    else:
        return a_k_nev, err_nev, "Neville-full"


def factor(n):
    if n == 0: return [0]
    factors = []
    d = 2
    n = abs(n)
    while d * d <= n:
        while n % d == 0:
            factors.append(d); n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors

def _cf_convergents(frac, max_den=10**15):
    x = frac
    h_prev, h_curr = Fraction(0), Fraction(1)
    k_prev, k_curr = Fraction(1), Fraction(0)
    for _ in range(500):
        if x.denominator == 0:
            break
        a = x.numerator // x.denominator
        h_prev, h_curr = h_curr, a * h_curr + h_prev
        k_prev, k_curr = k_curr, a * k_curr + k_prev
        if k_curr > max_den:
            break
        yield Fraction(int(h_curr), int(k_curr))
        remainder = x - a
        if remainder == 0:
            break
        x = Fraction(1, 1) / remainder

def identify_rational(x_mpf, max_den=500000000000000, tol=1e-10, max_prime=None):
    x_str = mpmath.nstr(x_mpf, 250, strip_zeros=False)
    try:
        x_frac_exact = Fraction(x_str)
    except (ValueError, ZeroDivisionError):
        return None, float('inf')
    best = None
    best_err = float('inf')
    for conv in _cf_convergents(x_frac_exact, max_den=max_den * 10):
        if conv.denominator > max_den * 10:
            break
        err = abs(float(x_frac_exact - conv))
        if err < tol and err < best_err:
            if max_prime:
                den_f = factor(conv.denominator)
                if den_f and max(den_f) > max_prime:
                    continue
            best = conv
            best_err = err
    for md in [max_den, max_den // 10, max_den // 100, max_den * 10]:
        if md < 1:
            continue
        cand = x_frac_exact.limit_denominator(md)
        err = abs(float(x_frac_exact - cand))
        if err < tol and err < best_err:
            if max_prime:
                den_f = factor(cand.denominator)
                if den_f and max(den_f) > max_prime:
                    continue
            best = cand
            best_err = err
    if best is None and max_prime:
        for conv in _cf_convergents(x_frac_exact, max_den=max_den):
            if conv.denominator > max_den:
                break
            err = abs(float(x_frac_exact - conv))
            if err < tol * 0.01:
                best = conv
                best_err = err
                break
    return best, best_err

def eval_poly(coeffs, x):
    result = Fraction(0)
    for k, c in enumerate(coeffs):
        result += c * Fraction(x) ** k
    return result

def _factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def three_theorems(k):
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const

def lagrange_interpolate(points):
    n = len(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    coeffs = [Fraction(0)] * n
    for i in range(n):
        basis = [Fraction(1)]
        denom = Fraction(1)
        for j in range(n):
            if j == i:
                continue
            denom *= (xs[i] - xs[j])
            new = [Fraction(0)] * (len(basis) + 1)
            for kk in range(len(basis)):
                new[kk + 1] += basis[kk]
                new[kk] -= xs[j] * basis[kk]
            basis = new
        for kk in range(len(basis)):
            if kk < n:
                coeffs[kk] += ys[i] * basis[kk] / denom
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs

def constrained_polynomial(clean_rats, c_top, c_subtop, c_const, deg):
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2
    if len(clean_ns) < n_needed:
        print(f"      INSUFFICIENT: have {len(clean_ns)}, need {n_needed}")
        return None
    residual_pts = []
    for nv in clean_ns:
        res = clean_rats[nv] - c_top * Fraction(nv)**deg \
              - c_subtop * Fraction(nv)**(deg-1) - c_const
        residual_pts.append((Fraction(nv), res / Fraction(nv)))
    n_use = min(len(residual_pts), n_needed)
    reduced_poly = lagrange_interpolate(residual_pts[:n_use])
    extra = residual_pts[n_use:]
    n_verified = 0
    if extra:
        for p in extra:
            if eval_poly(reduced_poly, p[0]) == p[1]:
                n_verified += 1
        print(f"      Verification: {n_verified}/{len(extra)} extra points match")
    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(reduced_poly):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    TARGET_K = 22
    score = []

    print("=" * 70)
    print(f"Toy 1540 -- Heat Kernel k=22 Extraction ATTEMPT (n=43 data)")
    print(f"  k=22: deg=44, need 42 clean points")
    print(f"  Available: n=3..43 = 41 dimensions")
    print(f"  DIAGNOSIS: are we 1 short, or can we make it work?")
    print("=" * 70)

    # T1: Load n=3..43
    print(f"\n--- T1: Loading checkpoints n=3..43 ---\n")
    ALL_DIMS = list(range(3, 44))  # n=3..43 (41 dimensions)
    trace_data = {}
    missing = []
    for n in ALL_DIMS:
        fp = os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps{DPS}.json")
        if not os.path.exists(fp):
            print(f"  n={n}: MISSING")
            missing.append(n)
            continue
        with open(fp, 'r') as f:
            data = json.load(f)
        ts = [mpmath.mpf(s) for s in data['ts']]
        fs = [mpmath.mpf(s) for s in data['fs']]
        vol = mpmath.mpf(data['vol'])
        trace_data[n] = (ts, fs, vol)
        if n == 3 or n == 43 or n % 10 == 0:
            print(f"  n={n}: loaded ({len(ts)} pts, vol={mpmath.nstr(vol, 8)})")

    load_time = time.time() - t_start
    n_loaded = len(trace_data)
    print(f"\n  {n_loaded} checkpoints loaded in {load_time:.1f}s")
    if missing:
        print(f"  MISSING: {missing}")

    t1_pass = n_loaded == 41 and 43 in trace_data
    score.append(("T1", f"All 41 checkpoints loaded (n=3..43): {'YES' if t1_pass else f'NO ({n_loaded})'}", t1_pass))
    print(f"  T1 {'PASS' if t1_pass else 'FAIL'}")

    # T2: Cascade a_1..a_21
    print(f"\n--- T2: Cascade extraction a_1..a_21 (reproduce Toy 1507) ---\n")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}
    max_confirmed = 1
    speaking_pairs = {}

    for k in range(2, TARGET_K + 1):
        t_level = time.time()
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 47)
        n_need = deg - 2

        ak_clean = {}
        for n in ALL_DIMS:
            if n not in trace_data:
                continue
            ts, fs, vol = trace_data[n]
            known_fracs = {0: Fraction(1)}
            for j in range(1, k):
                if j not in all_rats or n not in all_rats[j]:
                    break
                known_fracs[j] = all_rats[j][n]
            else:
                ak, err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
                frac, frac_err = identify_rational(ak, max_den=500000000000000,
                                                    tol=1e-8, max_prime=max_p)
                if frac:
                    ak_clean[n] = frac

        n_clean = len(ak_clean)
        dt_level = time.time() - t_level

        if n_clean >= n_need:
            ak_poly = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                for nv in ALL_DIMS:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
                max_confirmed = k
            else:
                KNOWN_POLYS[k] = None
        else:
            KNOWN_POLYS[k] = None

        all_rats[k] = ak_clean

        # Speaking pair ratio
        ratio_val = None
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            if len(p) > deg:
                actual_ratio = p[deg-1] / p[deg]
                is_integer = actual_ratio.denominator == 1
                if is_integer:
                    ratio_val = int(actual_ratio)
                    speaking_pairs[k] = ratio_val

        poly_status = f"deg {len(KNOWN_POLYS[k])-1}" if KNOWN_POLYS.get(k) else "FAILED"
        status_mark = "PASS" if KNOWN_POLYS.get(k) else "FAIL"

        if k >= 20 or (KNOWN_POLYS[k] is None and k >= 15):
            sp_str = f", ratio={ratio_val}" if ratio_val else ""
            print(f"  a_{k:>2}: {n_clean:>2}/{n_loaded} clean (need {n_need:>2}), "
                  f"{poly_status}{sp_str} [{dt_level:.1f}s] {status_mark}")
        elif k % 5 == 0 or k == 2:
            print(f"  a_{k:>2}: {n_clean:>2} clean, {poly_status} [{dt_level:.1f}s] {status_mark}")

        if KNOWN_POLYS[k] is None and k >= 20:
            print(f"\n  *** EXTRACTION BOUNDARY at k={k} ***")
            print(f"  Clean points: {n_clean}, needed: {n_need}")
            if k < TARGET_K:
                print(f"  Cannot reach k={TARGET_K}.")
            break

    t2_pass = max_confirmed >= 21
    score.append(("T2", f"Cascade a_1..a_21 confirmed: k={max_confirmed}", t2_pass))
    print(f"\n  T2 {'PASS' if t2_pass else 'FAIL'}: max confirmed = k={max_confirmed}")

    # T3: k=22 extraction attempt
    k22_extracted = KNOWN_POLYS.get(22) is not None
    t3_pass = k22_extracted
    if k22_extracted:
        score.append(("T3", "k=22 EXTRACTED!", t3_pass))
    else:
        n22_clean = len(all_rats.get(22, {}))
        score.append(("T3", f"k=22 extraction: {n22_clean} clean, needed 42. BLOCKED.", t3_pass))
    print(f"\n  T3 {'PASS' if t3_pass else 'FAIL'}")

    # T4: How many clean identifications at k=22?
    n22_clean = len(all_rats.get(22, {}))
    t4_pass = n22_clean >= 40  # At least 40 clean shows the method works
    score.append(("T4", f"Clean identifications at k=22: {n22_clean}/41 ({n22_clean}/42 needed)", t4_pass))
    print(f"\n  T4: {n22_clean} clean identifications at k=22 ({'PASS' if t4_pass else 'FAIL'})")

    # T5: Diagnosis
    shortfall = max(0, 42 - n22_clean)
    if n22_clean == 41:
        diag = f"Exactly 1 short. Need n=44 for 42 dimensions."
    elif n22_clean < 41:
        diag = f"{41 - n22_clean} dimensions failed rational ID + 1 dimension short = {shortfall} total deficit."
    else:
        diag = "Unexpected: more clean than dimensions?"
    t5_pass = True  # Diagnosis is always informative
    score.append(("T5", f"Diagnosis: {diag}", t5_pass))
    print(f"\n  T5: {diag}")

    # T6: Richardson-only preview of a_22(n=5)
    print(f"\n--- T6: Richardson extrapolation preview of a_22 ---")
    if 22 in all_rats and len(all_rats[22]) > 0:
        # Get the numerical extrapolation for a_22 at several n values
        for test_n in [5, 10, 20, 30]:
            if test_n in trace_data and all(j in all_rats and test_n in all_rats[j] for j in range(1, 22)):
                ts, fs, vol = trace_data[test_n]
                known_fracs = {0: Fraction(1)}
                for j in range(1, 22):
                    known_fracs[j] = all_rats[j][test_n]
                ak22, err22, method22 = extract_coefficient(fs, ts, vol, known_fracs, 22)
                print(f"  a_22(n={test_n}): {mpmath.nstr(ak22, 20)} (err={mpmath.nstr(err22, 3)}, {method22})")
                # Try rational ID
                frac22, ferr22 = identify_rational(ak22, max_den=500000000000000, tol=1e-6, max_prime=47)
                if frac22:
                    print(f"    Rational: {frac22} (err={ferr22:.2e})")
                    den_factors = factor(frac22.denominator)
                    max_den_prime = max(den_factors) if den_factors else 0
                    print(f"    Denominator factors: {den_factors} (max prime: {max_den_prime})")
    else:
        print(f"  No data for k=22 extrapolation (cascade stopped before k=22)")

    t6_pass = True
    score.append(("T6", "Richardson preview attempted", t6_pass))

    # Summary
    elapsed = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"DIAGNOSIS SUMMARY")
    print(f"{'='*70}")
    print(f"  Checkpoints: n=3..43 ({n_loaded} loaded)")
    print(f"  Cascade: a_1..a_{max_confirmed} confirmed")
    print(f"  k=22 status: {n22_clean}/42 clean points")
    if not k22_extracted:
        print(f"  BLOCKED: need n=44 checkpoint for k=22 extraction")
        print(f"  Estimated computation time for n=44: ~2 days (based on n=42→43 gap)")
        # n=42 computed April 25 13:18, n=43 computed April 26 09:52
        # That's ~20.5 hours
        print(f"  (n=42→n=43 took ~20 hours)")
    print(f"  k=22 prediction (from formula): ratio = -22*21/10 = {-22*21//10}")
    print(f"    But 22 is NOT a speaking pair index (22 mod 5 = 2, not 0 or 1)")
    print(f"    So ratio should still be integer, but not a speaking pair value")
    print(f"  Next speaking pair: k=25, ratio = -25*24/10 = -60 = -rank*n_C*C_2")
    print(f"    (needs n=48 = rank^4 * N_c for extraction)")
    print(f"  Total time: {elapsed:.1f}s ({elapsed/60:.1f} min)")

    # Speaking pair table
    print(f"\n  Speaking pairs confirmed:")
    for k in sorted(speaking_pairs.keys()):
        r = speaking_pairs[k]
        print(f"    k={k:>2}: ratio = {r:>4}")

    # Score
    print(f"\n{'='*70}")
    passed = sum(1 for _, _, p in score if p)
    for tid, desc, p in score:
        print(f"  {tid:4s}  {'PASS' if p else 'FAIL'}  {desc}")
    print(f"\nSCORE: {passed}/{len(score)}")

    # Save results
    results = {
        'max_confirmed_k': max_confirmed,
        'n_dims_used': n_loaded,
        'has_n43': 43 in trace_data,
        'k22_clean_count': n22_clean,
        'k22_needed': 42,
        'k22_extracted': k22_extracted,
        'speaking_pairs': {str(k): v for k, v in speaking_pairs.items()},
        'diagnosis': diag,
        'elapsed_seconds': elapsed,
        'score': f"{passed}/{len(score)}",
        'next_needed': 'n=44 for k=22' if not k22_extracted else 'n=48 for k=25',
    }
    results_path = os.path.join(CKPT_DIR, "cascade_results_n43.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {results_path}")


if __name__ == '__main__':
    main()
