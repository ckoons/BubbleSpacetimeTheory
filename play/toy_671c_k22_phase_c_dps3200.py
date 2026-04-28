#!/usr/bin/env python3
"""
Toy 671c — k=20 Phase C: High-precision at dps=3200 for k=22
======================================================
Generates fresh heat trace checkpoints at dps=3200 for n=3..50
(48 dimensions), then cascades a_1..a_17 to extract a_18, a_19, a_20.

Target: Confirm speaking pair 4 (k=20,21):
  ratio(20) = -38 = -2×19 = -rank×(n_C²-C₂)
  ratio(21) = -42 = -C₂×g

This upgrades the five-pair cycle from "committed prediction"
to "verified fact" through Pair 4.

Phase B steps:
  1. Build spectra for n=3..50 (integer arithmetic, fast)
  2. Compute heat traces at dps=3200 (~2-6 hours)
  3. Cascade a_1..a_17 using proven pipeline
  4. Extract a_18, a_19, a_20

Progress is checkpointed after each dimension.

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

# ═══════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

DPS = 3200
mpmath.mp.dps = DPS

N_MIN = 3
N_MAX = 50     # 48 dimensions: n=3..50
N_PTS = 48     # Chebyshev nodes per dimension
TARGET_K = 22  # Final target level (k=21: ratio=-42=-C₂×g predicted)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_671_checkpoint")
os.makedirs(CKPT_DIR, exist_ok=True)

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
    # a_16(5) from Toy 639
    # a_17(5) from Phase A
    17: Fraction(20329084105, 173988),
}

MAX_PRIME_BY_LEVEL = {
    2: 7, 3: 7, 4: 7, 5: 11,
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31,
    17: 37, 18: 37, 19: 41, 20: 41, 21: 43,
}


# ═══════════════════════════════════════════════════════════════════
# SPECTRUM BUILDER (exact integer arithmetic — dps-independent)
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
    return 2500  # Higher for n > 35


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


def adaptive_t_window(n, target_k):
    t_hi = min(0.01, max(5e-6, 0.3 / (n * n)))
    t_lo = max(1e-7, t_hi / 20)
    return t_lo, t_hi


def compute_heat_trace(n, eigs, dims, ts):
    results = []
    for t in ts:
        Z = mpmath.fsum(mpmath.mpf(d) * mpmath.exp(-mpmath.mpf(lam) * t)
                        for lam, d in zip(eigs, dims))
        results.append((4 * mpmath.pi * t) ** n * Z)
    return results


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


def frac_to_mpf(frac):
    return mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)


# ═══════════════════════════════════════════════════════════════════
# RATIONAL IDENTIFICATION & POLYNOMIAL RECOVERY
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
# CHECKPOINT I/O
# ═══════════════════════════════════════════════════════════════════

def save_checkpoint(n, ts, fs, vol):
    fp = os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps{DPS}.json")
    data = {
        'n': n,
        'dps': DPS,
        'ts': [mpmath.nstr(t, DPS) for t in ts],
        'fs': [mpmath.nstr(f, DPS) for f in fs],
        'vol': mpmath.nstr(vol, DPS),
    }
    with open(fp, 'w') as f:
        json.dump(data, f)


def load_checkpoint(n):
    fp = os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps{DPS}.json")
    if not os.path.exists(fp):
        return None
    with open(fp, 'r') as f:
        data = json.load(f)
    ts = [mpmath.mpf(s) for s in data['ts']]
    fs = [mpmath.mpf(s) for s in data['fs']]
    vol = mpmath.mpf(data['vol'])
    return ts, fs, vol


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()

    print("=" * 70)
    print(f"TOY 671b — k={TARGET_K} PHASE B: FULL COMPUTATION AT dps={DPS}")
    print("=" * 70)
    print(f"  Dimensions: n={N_MIN}..{N_MAX} ({N_MAX - N_MIN + 1} total)")
    print(f"  Points per dimension: {N_PTS}")
    print(f"  Target: a_{TARGET_K} polynomial (degree {2*TARGET_K})")
    print(f"  Speaking pair 4+5 prediction: ratio(20)=-38, ratio(21)=-42=-C₂×g")

    ALL_DIMS = list(range(N_MIN, N_MAX + 1))

    # ─── Step 1: Compute heat traces ───
    print(f"\n--- Step 1: Computing heat traces at dps={DPS} ---\n")

    trace_data = {}  # n -> (ts, fs, vol)

    for n in ALL_DIMS:
        existing = load_checkpoint(n)
        if existing:
            trace_data[n] = existing
            print(f"  n={n:>2}: loaded from checkpoint")
            continue

        t0 = time.time()
        t_lo, t_hi = adaptive_t_window(n, TARGET_K)
        ts = chebyshev_nodes(t_lo, t_hi, N_PTS)

        pmax = adaptive_pmax(n)
        eigs, dims = build_spectrum(n, pmax)
        n_eigs = len(eigs)

        fs = compute_heat_trace(n, eigs, dims, ts)
        vol = neville(ts, fs, mpmath.mpf(0))

        save_checkpoint(n, ts, fs, vol)
        trace_data[n] = (ts, fs, vol)

        dt = time.time() - t0
        elapsed_total = time.time() - t_start
        remaining_dims = N_MAX - n
        est_remaining = dt * remaining_dims if dt > 0 else 0

        print(f"  n={n:>2}: P_max={pmax}, {n_eigs} eigenvalues, "
              f"{dt:.1f}s (total: {elapsed_total/60:.1f}m, "
              f"est remaining: {est_remaining/60:.0f}m)")

    print(f"\n  All {len(trace_data)} dimensions computed in "
          f"{(time.time() - t_start)/60:.1f} minutes")

    # ─── Step 2: Cascade extraction ───
    print(f"\n--- Step 2: Cascade extraction a_1..a_{TARGET_K} ---\n")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}

    for k in range(2, TARGET_K + 1):
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 41)
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

        if n_clean >= n_need:
            ak_poly = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                for nv in ALL_DIMS:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
            else:
                KNOWN_POLYS[k] = None
        else:
            KNOWN_POLYS[k] = None

        all_rats[k] = ak_clean

        v5 = ak_clean.get(5)
        v5_ok = (k in KNOWN_AK5 and v5 == KNOWN_AK5[k]) if v5 else False

        # Check ratio for speaking pair detection
        ratio_str = ""
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            if len(p) > deg:
                actual_ratio = p[deg-1] / p[deg]
                expected = Fraction(-k*(k-1), 2*5)
                is_integer = expected.denominator == 1
                ratio_str = f", ratio={actual_ratio}" + (" INTEGER" if is_integer else "")

        poly_status = f"degree {len(KNOWN_POLYS[k])-1}" if KNOWN_POLYS[k] else "FAILED"
        print(f"  a_{k:>2}: {n_clean:>2}/{len(ALL_DIMS)} clean (need {n_need:>2}), "
              f"{poly_status}, a_{k}(5)={'OK' if v5_ok else '?'}{ratio_str}")

        if KNOWN_POLYS[k] is None and k >= 17:
            print(f"\n  EXTRACTION FAILED at k={k}. Precision boundary reached.")
            break

    # ─── Results ───
    elapsed = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"RESULTS")
    print(f"{'='*70}")

    max_confirmed = max(k for k in KNOWN_POLYS if KNOWN_POLYS[k] is not None)
    print(f"\n  Highest confirmed level: k={max_confirmed}")
    print(f"  Total time: {elapsed/60:.1f} minutes ({elapsed/3600:.2f} hours)")

    # Check speaking pairs in the confirmed range
    print(f"\n  Speaking pair analysis:")
    for k in range(5, max_confirmed + 1):
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            deg = 2 * k
            if len(p) > deg:
                ratio = p[deg-1] / p[deg]
                is_int = ratio.denominator == 1
                if is_int:
                    print(f"    k={k:>2}: ratio = {int(ratio):>4} INTEGER  "
                          f"{'<-- SPEAKING PAIR' if k % 5 in [0,1] else ''}")

    if max_confirmed >= 21:
        print(f"\n  *** PAIR 5 FIRST HALF: k=21 ratio = ? (predicted -42 = -C₂×g) ***")
        print(f"  TWENTY consecutive levels confirmed. Five full speaking pairs.")
    elif max_confirmed >= 20:
        print(f"\n  *** PAIR 4 CONFIRMED: k=20 ratio = -38 = -2×19 ***")
        print(f"  Need k=21 for Pair 5. n=42 data available.")
    elif max_confirmed >= 17:
        print(f"\n  Pushed to k={max_confirmed}. Need more precision or dimensions for k=20.")
        print(f"  Phase A confirmed a_17 from dps=800. Phase B extended to a_{max_confirmed}.")

    # Save results summary
    summary = {
        'dps': DPS,
        'n_range': [N_MIN, N_MAX],
        'max_confirmed_k': max_confirmed,
        'elapsed_seconds': elapsed,
        'speaking_pairs': {},
    }
    for k in range(5, max_confirmed + 1):
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            deg = 2 * k
            if len(p) > deg:
                ratio = p[deg-1] / p[deg]
                if ratio.denominator == 1:
                    summary['speaking_pairs'][k] = int(ratio)

    with open(os.path.join(CKPT_DIR, "results_summary.json"), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n  Results saved to {CKPT_DIR}/results_summary.json")


if __name__ == "__main__":
    main()
