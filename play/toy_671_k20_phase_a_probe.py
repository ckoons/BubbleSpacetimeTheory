#!/usr/bin/env python3
"""
Toy 671 — k=20 Phase A: Precision Probe from Existing Data
============================================================
Before committing to a multi-hour computation at dps=1600,
probe how far existing dps=800 checkpoints can push beyond k=16.

Phase A strategy:
  1. Load existing checkpoints (n=3..35, dps=800, 48 pts)
  2. Cascade a_1..a_16 (exact polynomials, all verified)
  3. Try extracting a_17 (degree 34, need 32 constrained pts from 33 dims)
  4. Report precision boundary

If a_17 extracts cleanly: we push to a_18 (degree 36, need 34 pts - borderline).
If a_17 fails: we know exactly where precision fails and what dps=1600 must fix.

Either outcome informs the Phase B computation.

Elie — March 31, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
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

mpmath.mp.dps = 800

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_361_checkpoint")

# ═══════════════════════════════════════════════════════════════════
# KNOWN DATA (from Toy 639 and prior)
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
}

MAX_PRIME_BY_LEVEL = {
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31,
    17: 37, 18: 37, 19: 37, 20: 41,
}

N_PTS = 48
FIXED_T_LO = 0.0008
FIXED_T_HI = 0.009


# ═══════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS (from Toy 639)
# ═══════════════════════════════════════════════════════════════════

def load_heat_trace(n, prefix):
    fp = os.path.join(CKPT_DIR, f"{prefix}_heat_n{n:02d}.json")
    if not os.path.exists(fp):
        return None
    with open(fp, 'r') as f:
        data = json.load(f)
    ts = [mpmath.mpf(s) for s in data['ts']]
    fs = [mpmath.mpf(s) for s in data['fs']]
    vol = mpmath.mpf(data['vol'])
    return ts, fs, vol


def frac_to_mpf(frac):
    return mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)


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


def chebyshev_nodes(t_lo, t_hi, n_pts):
    t_lo_m = mpmath.mpf(t_lo)
    t_hi_m = mpmath.mpf(t_hi)
    mid = (t_lo_m + t_hi_m) / 2
    half = (t_hi_m - t_lo_m) / 2
    return sorted([mid + half * mpmath.cos((2 * k + 1) * mpmath.pi / (2 * n_pts))
                    for k in range(n_pts)])


def adaptive_t_window(n, target_k):
    t_hi = min(0.01, max(5e-6, 0.3 / (n * n)))
    t_lo = max(1e-7, t_hi / 20)
    return t_lo, t_hi


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
    x_str = mpmath.nstr(x_mpf, 120, strip_zeros=False)
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
    ok = all(eval_poly(reduced_poly, p[0]) == p[1] for p in extra)
    if extra:
        print(f"      Reduced degree-{deg-3}: {'VERIFIED' if ok else 'FAILED'} "
              f"({len(extra)} extra points)")
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

    print("=" * 70)
    print("TOY 671 — k=20 PHASE A: PRECISION PROBE FROM EXISTING DATA")
    print("=" * 70)

    # ─── Load checkpoints ───
    print(f"\n--- Phase A: Loading existing checkpoints (dps=800) ---\n")

    CASCADE_RANGE = range(3, 14)
    fixed_ts = chebyshev_nodes(FIXED_T_LO, FIXED_T_HI, N_PTS)
    fixed_data = {}
    for n in CASCADE_RANGE:
        data = load_heat_trace(n, "fixed")
        if data:
            fixed_data[n] = (data[1], data[2])

    ALL_RANGE = []
    for n in range(3, 36):
        fp = os.path.join(CKPT_DIR, f"adaptive_heat_n{n:02d}.json")
        if os.path.exists(fp):
            ALL_RANGE.append(n)

    adaptive_data = {}
    adaptive_ts = {}
    for n in ALL_RANGE:
        # Use window appropriate for target level
        t_lo, t_hi = adaptive_t_window(n, 20)
        ts = chebyshev_nodes(t_lo, t_hi, N_PTS)
        adaptive_ts[n] = ts
        cached = load_heat_trace(n, "adaptive")
        if cached:
            adaptive_data[n] = (cached[1], cached[2])

    print(f"  Fixed: {len(fixed_data)} dimensions (n=3..13)")
    print(f"  Adaptive: {len(adaptive_data)} dimensions (n={ALL_RANGE[0]}..{ALL_RANGE[-1]})")
    print(f"  Total: {len(ALL_RANGE)} available dimensions")

    # ─── Cascade a_1..a_16 (proven) ───
    print(f"\n--- Cascading a_1..a_16 (proven exact polynomials) ---\n")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_RANGE}}

    # Phase A: a_2..a_5 from fixed-window traces
    for k in range(2, 6):
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 13)
        ak_rats = {}
        for n in CASCADE_RANGE:
            if n not in fixed_data:
                continue
            fs, vol = fixed_data[n]
            known_fracs = {0: Fraction(1)}
            for j in range(1, k):
                known_fracs[j] = all_rats[j][n]
            ak, _, _ = extract_coefficient(fs, fixed_ts, vol, known_fracs, k)
            frac, _ = identify_rational(ak, max_den=500000, tol=1e-20, max_prime=max_p)
            if frac:
                ak_rats[n] = frac
        clean_ns = sorted(ak_rats.keys())
        n_poly = min(len(clean_ns), deg + 1)
        pts = [(Fraction(nv), ak_rats[nv]) for nv in clean_ns[:n_poly]]
        ak_poly = lagrange_interpolate(pts)
        for nv in ALL_RANGE:
            ak_rats[nv] = eval_poly(ak_poly, Fraction(nv))
        all_rats[k] = ak_rats
        KNOWN_POLYS[k] = ak_poly
        v5 = ak_rats[5]
        v5_ok = (k in KNOWN_AK5 and v5 == KNOWN_AK5[k])
        print(f"  a_{k:>2}: degree {len(ak_poly)-1}, {len(clean_ns)} clean, "
              f"a_{k}(5)={'OK' if v5_ok else 'MISMATCH'}")

    # Phase B: a_6..a_16 from adaptive traces
    for k in range(6, 17):
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 23)
        ak_clean = {}
        for n in ALL_RANGE:
            if n not in adaptive_data:
                continue
            fs, vol = adaptive_data[n]
            ts = adaptive_ts[n]
            known_fracs = {0: Fraction(1)}
            for j in range(1, k):
                known_fracs[j] = all_rats[j][n]
            ak, _, _ = extract_coefficient(fs, ts, vol, known_fracs, k)
            frac, _ = identify_rational(ak, max_den=500000000000000,
                                        tol=1e-12, max_prime=max_p)
            if frac:
                ak_clean[n] = frac
        n_clean = len(ak_clean)
        n_need = deg - 2
        if n_clean >= n_need:
            ak_poly = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                for nv in ALL_RANGE:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
            else:
                KNOWN_POLYS[k] = None
        else:
            KNOWN_POLYS[k] = None
        all_rats[k] = ak_clean
        v5 = ak_clean.get(5)
        v5_ok = (k in KNOWN_AK5 and v5 == KNOWN_AK5[k]) if v5 else False
        poly_status = f"degree {len(KNOWN_POLYS[k])-1}" if KNOWN_POLYS[k] else "FAILED"
        print(f"  a_{k:>2}: {n_clean:>2}/{len(ALL_RANGE)} clean (need {n_need:>2}), "
              f"{poly_status}, a_{k}(5)={'OK' if v5_ok else ('?' if v5 is None else 'MISMATCH')}")

    # ─── Check cascade health ───
    cascade_ok = all(KNOWN_POLYS.get(j) is not None for j in range(1, 17))
    if not cascade_ok:
        missing = [j for j in range(1, 17) if KNOWN_POLYS.get(j) is None]
        print(f"\n  CASCADE BROKEN at levels: {missing}")
        print(f"  Cannot proceed beyond k=16 with existing data.")
        print(f"  Phase B (dps=1600) computation required.")
        elapsed = time.time() - t_start
        print(f"\n  Elapsed: {elapsed:.1f}s")
        sys.exit(1)

    print(f"\n  CASCADE HEALTHY through k=16")

    # ─── Probe: try a_17 ───
    print(f"\n--- Probing a_17 extraction (degree 34, need 32 pts from {len(ALL_RANGE)}) ---\n")

    k = 17
    deg = 2 * k  # 34
    c_top, c_sub, c_const = three_theorems(k)
    max_p = MAX_PRIME_BY_LEVEL.get(k, 37)
    n_need = deg - 2  # 32

    print(f"  Predicted ratio: -C({k},2)/{5} = -{k*(k-1)//2}/{5} = {-k*(k-1)//(2*5)}")
    print(f"  Integer? {'YES' if k*(k-1)//2 % 5 == 0 else 'NO'}")

    ak_clean = {}
    extraction_quality = {}
    for n in ALL_RANGE:
        if n not in adaptive_data:
            continue
        fs, vol = adaptive_data[n]
        ts = adaptive_ts[n]
        known_fracs = {0: Fraction(1)}
        for j in range(1, k):
            known_fracs[j] = all_rats[j][n]
        ak, err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
        frac, frac_err = identify_rational(ak, max_den=500000000000000,
                                           tol=1e-8, max_prime=max_p)
        if frac:
            ak_clean[n] = frac
            extraction_quality[n] = (float(err), method, float(frac_err))
        else:
            extraction_quality[n] = (float(err), method, None)

    n_clean = len(ak_clean)
    print(f"\n  Clean rational identifications: {n_clean}/{len(ALL_RANGE)} (need {n_need})")

    # Report quality for all dimensions
    print(f"\n  Extraction quality by dimension:")
    for n in ALL_RANGE:
        if n in extraction_quality:
            err, method, frac_err = extraction_quality[n]
            clean = "CLEAN" if n in ak_clean else "NOISY"
            frac_str = f"frac_err={frac_err:.2e}" if frac_err is not None else "no rational"
            print(f"    n={n:>2}: err={err:.2e}, {method:20s}, {clean:5s}, {frac_str}")

    if n_clean >= n_need:
        print(f"\n  SUFFICIENT DATA — attempting constrained polynomial recovery")
        ak_poly = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
        if ak_poly:
            # Check ratio
            actual_ratio = ak_poly[deg-1] / ak_poly[deg]
            expected_ratio = Fraction(-k*(k-1), 2*5)
            print(f"\n  a_17 polynomial RECOVERED (degree {len(ak_poly)-1})")
            print(f"  Top coefficient: {ak_poly[deg]}")
            print(f"  Sub-leading/top ratio: {actual_ratio} (expected {expected_ratio})")
            print(f"  Match: {'YES' if actual_ratio == expected_ratio else 'NO'}")
            v5 = eval_poly(ak_poly, Fraction(5))
            print(f"  a_17(5) = {v5}")
            print(f"  a_17(5) decimal = {float(v5):.10f}")
        else:
            print(f"\n  Constrained recovery FAILED")
    else:
        print(f"\n  INSUFFICIENT clean points for a_17: {n_clean} < {n_need}")
        print(f"  Gap: need {n_need - n_clean} more clean dimensions")

    # ─── Probe a_18 if a_17 succeeded ───
    if n_clean >= n_need and KNOWN_POLYS.get(17, None) is None:
        # Store a_17 if we recovered it
        if 'ak_poly' in dir() and ak_poly is not None:
            KNOWN_POLYS[17] = ak_poly
            for nv in ALL_RANGE:
                ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
            all_rats[17] = ak_clean

            print(f"\n--- Probing a_18 (degree 36, need 34 pts from {len(ALL_RANGE)}) ---")
            k18 = 18
            deg18 = 36
            c_top18, c_sub18, c_const18 = three_theorems(k18)
            n_need18 = deg18 - 2  # 34
            print(f"  Need {n_need18} clean points, have {len(ALL_RANGE)} dims")
            if len(ALL_RANGE) < n_need18:
                print(f"  NOT ENOUGH DIMENSIONS ({len(ALL_RANGE)} < {n_need18})")
                print(f"  Phase B REQUIRED: need at least {n_need18 + 2} dimensions")

    # ─── Summary ───
    elapsed = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"PHASE A SUMMARY")
    print(f"{'='*70}")
    print(f"  Cascade through k=16: {'HEALTHY' if cascade_ok else 'BROKEN'}")
    print(f"  a_17 extraction: {n_clean}/{n_need} clean points ({'SUFFICIENT' if n_clean >= n_need else 'INSUFFICIENT'})")
    print(f"  Time: {elapsed:.1f}s")
    print(f"\n  PHASE B REQUIREMENTS (for k=20):")
    print(f"    Dimensions needed: >= 41 (have {len(ALL_RANGE)})")
    print(f"    Precision needed: dps >= 1600 (have 800)")
    print(f"    Computation: ~6-16 hours at dps=1600")
    print(f"    Method: Hybrid (constrained + partial independent check)")

    sys.exit(0)


if __name__ == "__main__":
    main()
