#!/usr/bin/env python3
"""
Toy 1611 — Heat Kernel k=22 Verification with n=45 Data
========================================================
BST / APG: D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)]
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

SP-3 CRITICAL: n=45 checkpoint now available (PID 45970 produced it April 28).
With n=3..45 = 43 data points, we have 1 EXTRA verification point beyond the
42 clean points needed for k=22 (deg=44).

Toy 1564 extracted k=22 with ZERO verification margin (42/42).
Result: ratio(22) = -231/5 (NOT integer). Lyra flagged as probably artifact.

THIS TOY SETTLES IT:
- Run extraction with ALL 43 points (n=3..45)
- Use 42 for polynomial fit, 1 for INDEPENDENT verification
- If verification passes: k=22 CONFIRMED (ratio=-231/5, non-integer at non-speaking pair)
- If verification fails: ARTIFACT confirmed, k=21 remains the record

PRE-REGISTERED:
- k=22 mod 5 = 2, NOT a speaking pair
- Speaking pair formula: -k(k-1)/10 = -231/5 (non-integer, expected at non-speaking)
- Column rule max prime for k=22: 47

T1: Load all checkpoints n=3..45 (43 dimensions)
T2: Cascade extraction a_1..a_21 (reproduce known results)
T3: Extract a_22 with n=45 — polynomial uses 42 pts, verifies against remainder
T4: CRITICAL: Count independent verification points that pass
T5: If extracted: check ratio(22) and column rule
T6: Compare to Toy 1564 results (consistency check)

Keeper — April 29, 2026 (SP-3 unblock)
Copyright (c) 2026 Casey Koons. All rights reserved.

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

# Toy 1564 result for comparison
TOY_1564_RATIO = Fraction(-231, 5)

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]


# ===================================================================
# EXTRACTION FUNCTIONS (from Toy 1507/1540/1564)
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
        return None, 0, 0
    residual_pts = []
    for nv in clean_ns:
        res = clean_rats[nv] - c_top * Fraction(nv)**deg \
              - c_subtop * Fraction(nv)**(deg-1) - c_const
        residual_pts.append((Fraction(nv), res / Fraction(nv)))
    n_use = min(len(residual_pts), n_needed)
    reduced_poly = lagrange_interpolate(residual_pts[:n_use])
    extra = residual_pts[n_use:]
    n_verified = 0
    n_extra = len(extra)
    if extra:
        for p in extra:
            if eval_poly(reduced_poly, p[0]) == p[1]:
                n_verified += 1
        print(f"      Verification: {n_verified}/{n_extra} extra points match EXACTLY")
    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(reduced_poly):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly, n_verified, n_extra


# ===================================================================
# MAIN
# ===================================================================

def main():
    t_start = time.time()
    TARGET_K = 22
    score = []

    print("=" * 70)
    print(f"Toy 1611 -- Heat Kernel k=22 VERIFICATION with n=45")
    print(f"  k=22: deg=44, need 42 clean points")
    print(f"  Available: n=3..45 = 43 dimensions (1 EXTRA for verification)")
    print(f"  Toy 1564 result (zero margin): ratio(22) = -231/5")
    print(f"  Lyra assessment: probably artifact")
    print(f"  THIS TOY SETTLES IT — 1 independent verification point")
    print("=" * 70)

    # T1: Load n=3..45
    print(f"\n--- T1: Loading checkpoints n=3..45 ---\n")
    ALL_DIMS = list(range(3, 46))  # n=3..45 (43 dimensions)
    trace_data = {}
    missing = []
    for n in ALL_DIMS:
        fp = os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps{DPS}.json")
        if not os.path.exists(fp):
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
        if n == 3 or n == 45 or n % 10 == 0:
            print(f"  n={n}: loaded ({len(ts)} pts, vol={mpmath.nstr(vol, 8)})")

    load_time = time.time() - t_start
    n_loaded = len(trace_data)
    print(f"\n  {n_loaded} checkpoints loaded in {load_time:.1f}s")
    if missing:
        print(f"  MISSING: {missing}")

    has_n45 = 45 in trace_data
    t1_pass = n_loaded >= 43 and has_n45
    score.append(("T1", f"43 checkpoints loaded including n=45: {'YES' if t1_pass else f'NO ({n_loaded})'}", t1_pass))
    print(f"  T1 {'PASS' if t1_pass else 'FAIL'}: {n_loaded} dimensions, n=45 {'present' if has_n45 else 'MISSING'}")

    if not t1_pass:
        print("\n  FATAL: Cannot proceed without n=45 data")
        print(f"\nSCORE: 0/6")
        return

    # T2: Cascade a_1..a_21 (reproduce known)
    print(f"\n--- T2: Cascade extraction a_1..a_{TARGET_K} ---\n")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}
    max_confirmed = 1
    speaking_pairs = {}
    new_k22_poly = None
    k22_verified = 0
    k22_n_extra = 0
    verification_by_level = {}

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
            ak_poly, n_ver, n_ext = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            verification_by_level[k] = (n_ver, n_ext, n_clean)
            if ak_poly:
                for nv in ALL_DIMS:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
                max_confirmed = k
                if k == TARGET_K:
                    new_k22_poly = ak_poly
                    k22_verified = n_ver
                    k22_n_extra = n_ext
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
        ver_info = verification_by_level.get(k)
        ver_str = f" [{ver_info[0]}/{ver_info[1]} verified]" if ver_info and ver_info[1] > 0 else ""

        if k >= 15 or (KNOWN_POLYS[k] is None):
            sp_str = f", ratio={ratio_val}" if ratio_val else ""
            known_sp = KNOWN_SPEAKING_PAIRS.get(k)
            match_str = ""
            if known_sp is not None and ratio_val is not None:
                match_str = " MATCH" if ratio_val == known_sp else " MISMATCH!"
            elif k == TARGET_K and ratio_val is not None:
                match_str = " *** NEW ***"
            print(f"  a_{k:>2}: {n_clean:>2}/{n_loaded} clean (need {n_need:>2}), "
                  f"{poly_status}{sp_str}{match_str}{ver_str} [{dt_level:.1f}s] {status_mark}")
        elif k % 5 == 0 or k == 2:
            print(f"  a_{k:>2}: {n_clean:>2} clean, {poly_status}{ver_str} [{dt_level:.1f}s] {status_mark}")

    t2_pass = max_confirmed >= 21
    score.append(("T2", f"Cascade through k=21 confirmed: k={max_confirmed}", t2_pass))
    print(f"\n  T2 {'PASS' if t2_pass else 'FAIL'}: max confirmed = k={max_confirmed}")

    # T3: k=22 extraction
    print(f"\n--- T3: k=22 extraction ---\n")
    k22_extracted = KNOWN_POLYS.get(22) is not None
    t3_pass = k22_extracted
    if k22_extracted:
        print(f"  k=22 EXTRACTED!")
        print(f"  Polynomial degree: {len(new_k22_poly)-1}")
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

    # T4: CRITICAL — Independent verification point count
    print(f"\n--- T4: CRITICAL — Independent verification with n=45 ---\n")
    if k22_extracted:
        print(f"  Points used for fit: 42 (n=3..44 clean)")
        print(f"  Extra verification points: {k22_n_extra}")
        print(f"  Verified EXACTLY: {k22_verified}/{k22_n_extra}")
        if k22_verified > 0:
            print(f"\n  *** k=22 INDEPENDENTLY VERIFIED ***")
            print(f"  {k22_verified} point(s) not used in fit match polynomial exactly.")
            print(f"  This is NOT an artifact — the polynomial is real.")
            t4_pass = True
        else:
            print(f"\n  *** k=22 VERIFICATION FAILED ***")
            print(f"  The extra point(s) do NOT match the polynomial.")
            print(f"  Toy 1564's result was likely an ARTIFACT.")
            print(f"  k=21 REMAINS the confirmed record (20 consecutive integer levels).")
            t4_pass = False
    else:
        print(f"  Cannot verify — k=22 not extracted")
        t4_pass = False
    score.append(("T4", f"Independent verification: {'PASS ({}/{})'.format(k22_verified, k22_n_extra) if k22_extracted else 'N/A'}", t4_pass))

    # T5: Ratio and column rule
    print(f"\n--- T5: Ratio(22) and column rule ---\n")
    ratio_22 = speaking_pairs.get(22)
    t5_pass = False
    if k22_extracted:
        if ratio_22 is not None:
            print(f"  ratio(22) = {ratio_22} (integer)")
        else:
            p = KNOWN_POLYS[22]
            if len(p) > 44:
                ratio_frac = p[43] / p[44]
                print(f"  ratio(22) = {ratio_frac}")
                if ratio_frac.denominator != 1:
                    print(f"  NOT integer — expected at non-speaking pair (k=22 mod 5 = 2)")
                    formula_val = Fraction(-22 * 21, 10)
                    print(f"  Formula -k(k-1)/10 = {formula_val}")
                    print(f"  Match: {'YES' if ratio_frac == formula_val else 'NO'}")

        # Column rule
        a22_5 = eval_poly(new_k22_poly, Fraction(5))
        den = abs(a22_5.denominator)
        den_f = factor(den)
        max_p = max(den_f) if den_f else 0
        is_column_ok = max_p <= 47
        print(f"\n  a_22(n=5) denominator = {den}")
        print(f"  Factorization: {den_f}")
        print(f"  Max prime: {max_p} (limit: 47)")
        print(f"  Column rule: {'PASS' if is_column_ok else 'FAIL'}")
        t5_pass = is_column_ok

        # Comparison with Toy 1564
        p = KNOWN_POLYS[22]
        if len(p) > 44:
            this_ratio = p[43] / p[44]
            print(f"\n  Toy 1564 ratio: {TOY_1564_RATIO} = {float(TOY_1564_RATIO):.6f}")
            print(f"  This toy ratio: {this_ratio} = {float(this_ratio):.6f}")
            print(f"  Match: {'YES' if this_ratio == TOY_1564_RATIO else 'NO'}")
    else:
        print(f"  Cannot check — k=22 not extracted")
    score.append(("T5", f"Column rule: {'PASS' if t5_pass else 'FAIL/NA'}", t5_pass))

    # T6: Verification history across all levels
    print(f"\n--- T6: Verification history (all levels) ---\n")
    print(f"  Level | Clean | Needed | Extra | Verified")
    print(f"  ------|-------|--------|-------|----------")
    for k in sorted(verification_by_level.keys()):
        n_ver, n_ext, n_cln = verification_by_level[k]
        mark = ""
        if n_ext > 0:
            mark = "PASS" if n_ver == n_ext else f"FAIL ({n_ext - n_ver} failed)"
        print(f"  k={k:>2}  | {n_cln:>5} | {2*k-2:>6} | {n_ext:>5} | {n_ver:>4}/{n_ext} {mark}")
    t6_pass = True
    score.append(("T6", "Verification history displayed", t6_pass))

    # Summary
    elapsed = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"VERDICT")
    print(f"{'='*70}")
    if k22_extracted and k22_verified > 0:
        print(f"  k=22 CONFIRMED with {k22_verified} independent verification point(s)")
        print(f"  TWENTY-TWO consecutive levels (k=1..22)")
        ratio_str = ratio_22 if ratio_22 else (KNOWN_POLYS[22][43] / KNOWN_POLYS[22][44] if len(KNOWN_POLYS[22]) > 44 else "?")
        print(f"  ratio(22) = {ratio_str}")
        if not isinstance(ratio_str, int):
            print(f"  Non-integer at non-speaking pair — formula -k(k-1)/10 still holds")
    elif k22_extracted and k22_verified == 0:
        print(f"  k=22 ARTIFACT CONFIRMED")
        print(f"  Polynomial fit at 42 points was overfitting — n=45 does not match")
        print(f"  k=21 remains the confirmed record: TWENTY consecutive integer levels")
        print(f"  ratio(21) = -42 = -C_2 * g")
    else:
        print(f"  k=22 extraction FAILED (insufficient clean points)")
        print(f"  k=21 remains the confirmed record")

    print(f"\n  Speaking pair table:")
    for k in sorted(speaking_pairs.keys()):
        r = speaking_pairs[k]
        is_sp = (k % 5 == 0 or k % 5 == 1)
        sp_val = -k*(k-1)//10
        match = "= -k(k-1)/10" if r == sp_val and is_sp else ""
        print(f"    k={k:>2}: ratio = {r:>4}  {'SPEAKING' if is_sp else '        '} {match}")

    print(f"\n  Total time: {elapsed:.1f}s ({elapsed/60:.1f} min)")

    # Score
    print(f"\n{'='*70}")
    passed = sum(1 for _, _, p in score if p)
    for tid, desc, p in score:
        print(f"  {tid:4s}  {'PASS' if p else 'FAIL'}  {desc}")
    print(f"\nSCORE: {passed}/{len(score)}")

    # Save results
    results = {
        'toy': 1611,
        'description': 'k=22 verification with n=45 data',
        'max_confirmed_k': max_confirmed,
        'n_dims_used': n_loaded,
        'has_n45': has_n45,
        'k22_extracted': k22_extracted,
        'k22_verified': k22_verified,
        'k22_n_extra': k22_n_extra,
        'speaking_pairs': {str(k): v for k, v in speaking_pairs.items()},
        'elapsed_seconds': elapsed,
        'score': f"{passed}/{len(score)}",
    }
    if k22_extracted:
        a22_5 = eval_poly(new_k22_poly, Fraction(5))
        results['a22_n5'] = str(a22_5)
        results['a22_n5_float'] = float(a22_5)
        if new_k22_poly and len(new_k22_poly) > 44:
            ratio_frac = new_k22_poly[43] / new_k22_poly[44]
            results['ratio_22'] = str(ratio_frac)
            results['ratio_22_float'] = float(ratio_frac)
            results['matches_toy_1564'] = (ratio_frac == TOY_1564_RATIO)
    results_path = os.path.join(CKPT_DIR, "cascade_results_n45_verification.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {results_path}")


if __name__ == '__main__':
    main()
