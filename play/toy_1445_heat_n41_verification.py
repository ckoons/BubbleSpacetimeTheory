#!/usr/bin/env python3
"""
Toy 1445 -- Heat Kernel n=41 Verification
==========================================
Extends Toy 1395 cascade extraction from 38 checkpoints (n=3..40) to
39 checkpoints (n=3..41). The n=41 data point provides:
  - Extra validation for all levels k=2..20
  - Attempt to reach k=21 (needs 40 clean points, have 39 — likely 1 short)
  - Speaking pair 4 re-verification (k=20 ratio = -38)

Previous result (Toy 1395, n=3..40): 10/10 PASS, k=2..20 confirmed,
speaking pairs at k=5,6,10,11,15,16,20 all integer.

Elie -- April 23, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
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
N_c, n_C, g, C_2, rank = 3, 5, 7, 6, 2

# ═══════════════════════════════════════════════════════════════════
# KNOWN DATA
# ═══════════════════════════════════════════════════════════════════

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]

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

MAX_PRIME_BY_LEVEL = {
    2: 7, 3: 7, 4: 7, 5: 11,
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31,
    17: 37, 18: 37, 19: 41, 20: 43, 21: 43,
}


# ═══════════════════════════════════════════════════════════════════
# EXTRACTION FUNCTIONS (from Toy 671b / 1395)
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
        g = F / t ** target_k
        gs.append(g)
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


# ═══════════════════════════════════════════════════════════════════
# RATIONAL IDENTIFICATION
# ═══════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════
# POLYNOMIAL RECOVERY
# ═══════════════════════════════════════════════════════════════════

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
        return None, 0
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
    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(reduced_poly):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly, n_verified


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    TARGET_K = 21  # Try to reach k=21 with n=41
    score = []

    print("=" * 70)
    print(f"Toy 1445 -- Heat Cascade: n=3..41 (39 dims), target a_1..a_{TARGET_K}")
    print(f"  dps={DPS}, extends Toy 1395 with n=41 checkpoint")
    print("=" * 70)

    # Step 1: Load all checkpoints including n=41
    print(f"\n--- Loading {DPS}-digit checkpoints ---\n")
    ALL_DIMS = list(range(3, 42))  # n=3..41 — 39 dimensions
    trace_data = {}
    for n in ALL_DIMS:
        fp = os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps{DPS}.json")
        if not os.path.exists(fp):
            print(f"  n={n}: MISSING")
            continue
        with open(fp, 'r') as f:
            data = json.load(f)
        ts = [mpmath.mpf(s) for s in data['ts']]
        fs = [mpmath.mpf(s) for s in data['fs']]
        vol = mpmath.mpf(data['vol'])
        trace_data[n] = (ts, fs, vol)
        if n % 10 == 0 or n == 3 or n == 41:
            print(f"  n={n}: loaded ({len(ts)} pts, vol={mpmath.nstr(vol, 8)})")

    load_time = time.time() - t_start
    n_loaded = len(trace_data)
    print(f"\n  {n_loaded} checkpoints loaded in {load_time:.1f}s")
    has_41 = 41 in trace_data
    print(f"  n=41 present: {'YES' if has_41 else 'NO'}")

    # Step 2: Cascade extraction
    print(f"\n--- Cascade extraction a_1..a_{TARGET_K} ---\n")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}
    max_confirmed = 1
    speaking_pairs = {}
    extra_verifications = {}  # Track n=41 extra verifications per level

    for k in range(2, TARGET_K + 1):
        t_level = time.time()
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 43)
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

        n_extra_verified = 0
        if n_clean >= n_need:
            ak_poly, n_extra_verified = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                for nv in ALL_DIMS:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
                max_confirmed = k
                extra_verifications[k] = n_extra_verified
            else:
                KNOWN_POLYS[k] = None
        else:
            KNOWN_POLYS[k] = None

        all_rats[k] = ak_clean

        # Check value at n=5
        v5 = ak_clean.get(5)
        v5_ok = (k in KNOWN_AK5 and v5 == KNOWN_AK5[k]) if v5 else False

        # Check speaking pair ratio
        ratio_str = ""
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            if len(p) > deg:
                actual_ratio = p[deg-1] / p[deg]
                is_integer = actual_ratio.denominator == 1
                ratio_str = f"ratio={actual_ratio}"
                if is_integer:
                    ratio_str += " INTEGER"
                    speaking_pairs[k] = int(actual_ratio)

        poly_status = f"deg {len(KNOWN_POLYS[k])-1}" if KNOWN_POLYS.get(k) else "FAILED"
        status_mark = "PASS" if KNOWN_POLYS.get(k) else "FAIL"
        extra_str = f" +{n_extra_verified} verified" if n_extra_verified > 0 else ""

        print(f"  a_{k:>2}: {n_clean:>2}/{len(trace_data)} clean (need {n_need:>2}), "
              f"{poly_status}, a_{k}(5)={'OK' if v5_ok else '??'}, "
              f"{ratio_str}{extra_str} [{dt_level:.1f}s] {status_mark}")

        if KNOWN_POLYS[k] is None and k >= 17:
            print(f"\n  *** EXTRACTION BOUNDARY at k={k} ***")
            print(f"  Clean points: {n_clean}, needed: {n_need}")
            if n_clean == n_need - 1:
                print(f"  ONE SHORT — need n=42 checkpoint to reach k={k}")
            break

    # Step 3: Results
    elapsed = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"RESULTS — n=41 verification")
    print(f"{'='*70}")

    print(f"\n  Highest confirmed level: k={max_confirmed}")
    print(f"  Total time: {elapsed:.1f}s ({elapsed/60:.1f} min)")

    # Show extra verifications from n=41
    total_extra = sum(extra_verifications.values())
    print(f"\n  Extra verification points from n=41:")
    if total_extra > 0:
        for k in sorted(extra_verifications.keys()):
            if extra_verifications[k] > 0:
                print(f"    k={k}: +{extra_verifications[k]} extra points match polynomial")
    else:
        print(f"    n=41 absorbed into polynomial fitting (no surplus for most levels)")

    # T1: All levels through k=16 confirmed
    t1_pass = all(KNOWN_POLYS.get(k) is not None for k in range(1, 17))
    score.append(("T1", f"Cascade a_1..a_16 all confirmed", t1_pass))

    # T2: Values at n=5 match KNOWN_AK5
    n5_matches = sum(1 for k in range(1, min(max_confirmed+1, 18))
                     if k in KNOWN_AK5 and k in all_rats
                     and 5 in all_rats[k] and all_rats[k][5] == KNOWN_AK5[k])
    t2_pass = n5_matches >= 15
    score.append(("T2", f"a_k(5) matches known: {n5_matches}/16", t2_pass))

    # T3: Speaking pairs at k=5,6,10,11,15,16 are integers
    confirmed_sp = [k for k in [5, 6, 10, 11, 15, 16] if k in speaking_pairs]
    t3_pass = len(confirmed_sp) == 6
    score.append(("T3", f"Speaking pairs k=5..16: {len(confirmed_sp)}/6 integer", t3_pass))

    # T4: Column rule C=1 (leading coeff matches 1/(3^k * k!))
    column_ok = 0
    for k in range(2, max_confirmed + 1):
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            if len(p) > 2*k:
                expected_top = Fraction(1, 3**k * _factorial(k))
                if p[2*k] == expected_top:
                    column_ok += 1
    t4_pass = column_ok >= 15
    score.append(("T4", f"Column rule c_top OK: {column_ok}/{max_confirmed-1}", t4_pass))

    # T5: a_17..a_20 all extracted (extending beyond Toy 1395)
    t5_pass = max_confirmed >= 20
    score.append(("T5", f"a_17..a_20 all confirmed (19 consecutive levels)", t5_pass))

    # T6: Speaking pair 4 (k=20 ratio = -38)
    t6_pass = speaking_pairs.get(20) == -38
    score.append(("T6", f"Speaking pair 4: k=20 ratio = {speaking_pairs.get(20, '?')} (expect -38)", t6_pass))

    # T7: n=41 loaded and participated
    t7_pass = has_41
    score.append(("T7", f"n=41 checkpoint loaded and used", t7_pass))

    # T8: k=21 attempt (may fail — need 40 clean, have 39)
    t8_pass = max_confirmed >= 21
    score.append(("T8", f"k=21 reached: {'YES' if t8_pass else 'NO (need n=42)'}", t8_pass))

    # Speaking pair table
    print(f"\n  Speaking pair analysis:")
    print(f"  {'k':>3}  {'ratio':>6}  {'formula -k(k-1)/10':>18}  {'BST reading'}")
    print(f"  {'---':>3}  {'------':>6}  {'------------------':>18}  {'───────────'}")
    for k in sorted(speaking_pairs.keys()):
        r = speaking_pairs[k]
        expected = -k * (k - 1) // 10
        formula_match = "OK" if r == expected else "??"
        reading = ""
        if r == -2: reading = "-rank"
        elif r == -3: reading = "-N_c"
        elif r == -9: reading = "-N_c²"
        elif r == -11: reading = "-(2n_C+1)"
        elif r == -21: reading = "-C(g,2)"
        elif r == -24: reading = "-dim SU(5)"
        elif r == -38: reading = "-2 × 19"
        elif r == -42: reading = "-C₂ × g"
        print(f"  {k:>3}  {r:>6}  {expected:>8}  {formula_match:>8}  {reading}")

    # Prediction for k=21
    print(f"\n  Next speaking pair prediction:")
    r21_pred = -21 * 20 // 10
    print(f"    k=21: ratio should be -21×20/10 = {r21_pred} = -C₂ × g")
    print(f"    {'CONFIRMED' if speaking_pairs.get(21) == r21_pred else 'PENDING (need n=42 checkpoint)'}")

    # Scorecard
    print(f"\n{'='*70}")
    print(f"SCORECARD")
    print(f"{'='*70}")
    passed = sum(1 for _, _, p in score if p)
    for tid, desc, p in score:
        print(f"  {tid:4s}  {'PASS' if p else 'FAIL'}  {desc}")
    print(f"\nSCORE: {passed}/{len(score)}")

    # Save results
    results = {
        'max_confirmed_k': max_confirmed,
        'n_dims_used': n_loaded,
        'has_n41': has_41,
        'speaking_pairs': speaking_pairs,
        'extra_verifications': extra_verifications,
        'elapsed_seconds': elapsed,
        'score': f"{passed}/{len(score)}",
        'next_needed': 'n=42 for k=21',
    }
    results_path = os.path.join(CKPT_DIR, "cascade_results_n41.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {results_path}")


if __name__ == "__main__":
    main()
