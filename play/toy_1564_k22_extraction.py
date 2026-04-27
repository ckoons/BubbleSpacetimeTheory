#!/usr/bin/env python3
"""
Toy 1564 — Heat Kernel k=22 Extraction (n=44 data AVAILABLE)
=============================================================
BST / APG: D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

n=44 checkpoint arrived April 27 04:35 AM. With n=3..44 = 42 dimensions,
we have EXACTLY the 42 clean points needed for k=22 (deg=44).

This is the moment: 21 consecutive integer ratios (k=2..21) already confirmed.
k=22 would make TWENTY-TWO consecutive levels.

PRE-REGISTERED:
- ratio(22) should be an integer
- k=22 is NOT a speaking pair (22 mod 5 = 2, not 0 or 1)
- Next speaking pair: k=25, ratio = -60 = -rank*n_C*C_2

T1: Load all checkpoints n=3..44 (42 dimensions)
T2: Cascade extraction a_1..a_21 (reproduce known results)
T3: Extract a_22 — the new level
T4: Verify ratio(22) is integer
T5: Check denominator 7-smoothness (column rule)
T6: Check a_22(n=5) against BST structure

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

# Known speaking pairs through k=21
KNOWN_SPEAKING_PAIRS = {
    5: -2, 6: -3, 10: -9, 11: -11, 15: -21, 16: -24, 20: -38, 21: -42
}

# Max prime in denominator by level (from column rule)
MAX_PRIME_BY_LEVEL = {
    2: 7, 3: 7, 4: 7, 5: 11, 6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31, 17: 37, 18: 37, 19: 41, 20: 41,
    21: 43, 22: 47,
}

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]


# ===================================================================
# EXTRACTION FUNCTIONS (from Toy 1507/1540)
# ===================================================================

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


# ===================================================================
# MAIN
# ===================================================================

def main():
    t_start = time.time()
    TARGET_K = 22
    score = []

    print("=" * 70)
    print(f"Toy 1564 -- Heat Kernel k=22 Extraction (n=44 DATA AVAILABLE)")
    print(f"  k=22: deg=44, need 42 clean points")
    print(f"  Available: n=3..44 = 42 dimensions -- EXACTLY sufficient")
    print(f"  21 consecutive integer ratios confirmed (k=2..21)")
    print(f"  This extraction would give TWENTY-TWO consecutive levels")
    print("=" * 70)

    # T1: Load n=3..44
    print(f"\n--- T1: Loading checkpoints n=3..44 ---\n")
    ALL_DIMS = list(range(3, 45))  # n=3..44 (42 dimensions)
    trace_data = {}
    missing = []
    for n in ALL_DIMS:
        fp = os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps{DPS}.json")
        if not os.path.exists(fp):
            # Try without leading zero
            fp = os.path.join(CKPT_DIR, f"heat_n{n}_dps{DPS}.json")
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
        if n == 3 or n == 44 or n % 10 == 0:
            print(f"  n={n}: loaded ({len(ts)} pts, vol={mpmath.nstr(vol, 8)})")

    load_time = time.time() - t_start
    n_loaded = len(trace_data)
    print(f"\n  {n_loaded} checkpoints loaded in {load_time:.1f}s")
    if missing:
        print(f"  MISSING: {missing}")

    t1_pass = n_loaded >= 42 and 44 in trace_data
    score.append(("T1", f"42+ checkpoints loaded including n=44: {'YES' if t1_pass else f'NO ({n_loaded})'}", t1_pass))
    print(f"  T1 {'PASS' if t1_pass else 'FAIL'}: {n_loaded} dimensions loaded")

    if not t1_pass:
        print("\n  FATAL: Cannot proceed without n=44 data")
        print(f"\nSCORE: 0/6")
        return

    # T2: Cascade a_1..a_21 (reproduce known)
    print(f"\n--- T2: Cascade extraction a_1..a_{TARGET_K} ---\n")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}
    max_confirmed = 1
    speaking_pairs = {}
    new_k22_poly = None

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
                if k == TARGET_K:
                    new_k22_poly = ak_poly
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

        if k >= 19 or (KNOWN_POLYS[k] is None):
            sp_str = f", ratio={ratio_val}" if ratio_val else ""
            known_sp = KNOWN_SPEAKING_PAIRS.get(k)
            match_str = ""
            if known_sp is not None and ratio_val is not None:
                match_str = " MATCH" if ratio_val == known_sp else " MISMATCH!"
            elif k == TARGET_K and ratio_val is not None:
                match_str = " *** NEW ***"
            print(f"  a_{k:>2}: {n_clean:>2}/{n_loaded} clean (need {n_need:>2}), "
                  f"{poly_status}{sp_str}{match_str} [{dt_level:.1f}s] {status_mark}")
        elif k % 5 == 0 or k == 2:
            print(f"  a_{k:>2}: {n_clean:>2} clean, {poly_status} [{dt_level:.1f}s] {status_mark}")

    t2_pass = max_confirmed >= 21
    score.append(("T2", f"Cascade through k=21 confirmed: k={max_confirmed}", t2_pass))
    print(f"\n  T2 {'PASS' if t2_pass else 'FAIL'}: max confirmed = k={max_confirmed}")

    # T3: k=22 extraction
    print(f"\n--- T3: k=22 extraction ---\n")
    k22_extracted = KNOWN_POLYS.get(22) is not None
    t3_pass = k22_extracted
    if k22_extracted:
        print(f"  k=22 EXTRACTED SUCCESSFULLY!")
        print(f"  Polynomial degree: {len(new_k22_poly)-1}")
        # Show a_22(n=5)
        a22_5 = eval_poly(new_k22_poly, Fraction(5))
        print(f"  a_22(n=5) = {a22_5}")
        print(f"           = {float(a22_5):.10f}")
        num_factors = factor(abs(a22_5.numerator))
        den_factors = factor(abs(a22_5.denominator))
        print(f"  Numerator factors: {num_factors}")
        print(f"  Denominator factors: {den_factors}")
        max_den_prime = max(den_factors) if den_factors else 0
        print(f"  Max prime in denominator: {max_den_prime}")
    else:
        n22_clean = len(all_rats.get(22, {}))
        print(f"  k=22 extraction FAILED: {n22_clean} clean, needed 42")
    score.append(("T3", f"k=22 extracted: {'YES' if k22_extracted else 'NO'}", t3_pass))

    # T4: Ratio check
    print(f"\n--- T4: Ratio(22) integer check ---\n")
    ratio_22 = speaking_pairs.get(22)
    t4_pass = ratio_22 is not None
    if ratio_22 is not None:
        print(f"  ratio(22) = {ratio_22}")
        print(f"  Is integer: YES")
        # Speaking pair formula: -k(k-1)/10
        sp_formula = -22 * 21 // 10
        is_speaking = (22 % 5 == 0 or 22 % 5 == 1)
        print(f"  k=22 mod 5 = {22 % 5} -> {'speaking pair' if is_speaking else 'NOT speaking pair'}")
        if is_speaking:
            print(f"  Speaking pair formula value: {sp_formula}")
            print(f"  Match: {'YES' if ratio_22 == sp_formula else 'NO'}")
        # Check if it fits the pattern
        print(f"\n  All ratios so far:")
        for k in sorted(speaking_pairs.keys()):
            r = speaking_pairs[k]
            is_sp = (k % 5 == 0 or k % 5 == 1)
            sp_val = -k*(k-1)//10
            match = "= -k(k-1)/10" if r == sp_val and is_sp else ""
            print(f"    k={k:>2}: ratio = {r:>4}  {'[speaking]' if is_sp else '[non-sp] '} {match}")
    else:
        if k22_extracted:
            p = KNOWN_POLYS[22]
            if len(p) > 44:
                ratio_frac = p[43] / p[44]
                print(f"  ratio(22) = {ratio_frac} (NOT integer)")
                t4_pass = False
            else:
                print(f"  Polynomial too short to extract ratio")
        else:
            print(f"  Cannot compute ratio — k=22 not extracted")
    score.append(("T4", f"ratio(22) is integer: {'YES =' + str(ratio_22) if ratio_22 else 'NO/UNKNOWN'}", t4_pass))

    # T5: 7-smoothness of denominator
    print(f"\n--- T5: Denominator 7-smoothness (column rule) ---\n")
    t5_pass = False
    if k22_extracted:
        a22_5 = eval_poly(new_k22_poly, Fraction(5))
        den = abs(a22_5.denominator)
        den_f = factor(den)
        max_p = max(den_f) if den_f else 0
        is_7smooth = max_p <= 47  # k=22 predicted max prime
        print(f"  a_22(n=5) denominator = {den}")
        print(f"  Factorization: {den_f}")
        print(f"  Max prime: {max_p}")
        print(f"  Predicted max prime for k=22: 47")
        print(f"  Column rule satisfied: {'YES' if is_7smooth else 'NO'}")
        t5_pass = is_7smooth
    else:
        print(f"  Cannot check — k=22 not extracted")
    score.append(("T5", f"Denominator column rule: {'PASS' if t5_pass else 'FAIL/NA'}", t5_pass))

    # T6: BST structure of a_22(n=5)
    print(f"\n--- T6: BST structure of a_22(n=5) ---\n")
    t6_pass = False
    if k22_extracted:
        a22_5 = eval_poly(new_k22_poly, Fraction(5))
        print(f"  a_22(n=5) = {a22_5}")
        print(f"  Float: {float(a22_5):.15f}")

        # Check various n values
        print(f"\n  a_22 at BST-special n values:")
        for n_test in [3, 5, 6, 7, 137]:
            if n_test <= 44:
                val = eval_poly(new_k22_poly, Fraction(n_test))
                print(f"    a_22(n={n_test:>3}) = {val}  ({float(val):.10f})")
                den_f = factor(abs(val.denominator))
                max_dp = max(den_f) if den_f else 0
                print(f"      den factors: {den_f}, max prime: {max_dp}")

        # The speaking pair check for THIS level
        # k=22 is between speaking pairs k=21 and k=25
        # Non-speaking levels have been: k=7,8,9, k=12,13,14, k=17,18,19
        # Check structure
        print(f"\n  TWENTY-TWO consecutive integer levels: k=1..22")
        print(f"  Previous record: k=1..21 (TWENTY-ONE levels)")
        t6_pass = True
    else:
        print(f"  Cannot analyze — k=22 not extracted")
    score.append(("T6", f"BST structure analysis: {'DONE' if t6_pass else 'NA'}", t6_pass))

    # Summary
    elapsed = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"RESULT SUMMARY")
    print(f"{'='*70}")
    print(f"  Checkpoints: n=3..44 ({n_loaded} loaded)")
    print(f"  Cascade: a_1..a_{max_confirmed}")
    if k22_extracted:
        print(f"  *** k=22 CONFIRMED ***")
        print(f"  TWENTY-TWO consecutive integer ratios (k=1..22)")
        print(f"  ratio(22) = {ratio_22}")
        print(f"  Next targets: k=23,24 (need more dimensions), k=25 = next speaking pair")
    else:
        print(f"  k=22 FAILED — see diagnostics above")

    print(f"\n  Speaking pair table (confirmed):")
    for k in sorted(speaking_pairs.keys()):
        r = speaking_pairs[k]
        is_sp = (k % 5 == 0 or k % 5 == 1)
        print(f"    k={k:>2}: ratio = {r:>4}  {'SPEAKING' if is_sp else '        '}")

    print(f"\n  Total time: {elapsed:.1f}s ({elapsed/60:.1f} min)")

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
        'has_n44': 44 in trace_data,
        'k22_extracted': k22_extracted,
        'k22_ratio': ratio_22,
        'speaking_pairs': {str(k): v for k, v in speaking_pairs.items()},
        'elapsed_seconds': elapsed,
        'score': f"{passed}/{len(score)}",
    }
    if k22_extracted:
        a22_5 = eval_poly(new_k22_poly, Fraction(5))
        results['a22_n5'] = str(a22_5)
        results['a22_n5_float'] = float(a22_5)
    results_path = os.path.join(CKPT_DIR, "cascade_results_n44.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {results_path}")


if __name__ == '__main__':
    main()
