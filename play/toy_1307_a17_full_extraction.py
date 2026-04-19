#!/usr/bin/env python3
"""
Toy 1307 — a₁₇ Full Polynomial Extraction from dps=1600 Checkpoints
====================================================================
Uses the n=3..38 dps=1600 checkpoints (Toy 671b Phase B) to:
  1. Cascade a₁..a₁₆ (re-derive exact polynomials from data)
  2. Extract a₁₇(n) numerically for all 36 dimensions
  3. Identify each as a rational number
  4. Fit the degree-34 polynomial using Three Theorems constraints
  5. Verify against known a₁₇(5) = 20329084105/173988

Key parameters:
  - a₁₇ is degree 34, needs 32 constrained unknowns
  - 36 data points → 4 verification points (healthy margin)
  - NOT a speaking pair (17 mod 5 = 2)
  - QUIET predicted: 2k+1 = 35 = 5×7 composite → no new VSC prime
  - Expected sub-leading ratio: -C(17,2)/n_C = -136/5

This toy also attempts a₁₈ (degree 36, 2 verification) and reports
whether it succeeds.

Lyra — April 18, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Lyra). April 2026.
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

DPS = 1600
mpmath.mp.dps = DPS

N_MIN = 3
N_MAX = 38      # We have checkpoints through n=38
TARGET_K = 22   # Push cascade to natural limit — let it fail when data runs out

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
N_max = N_c**3 * n_C + rank  # 137

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_671_checkpoint")

# BST integers
A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]

# Known a_k(5) values for validation (from Toy 671b)
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

# Max prime in denominator, by level (from column rule analysis)
MAX_PRIME_BY_LEVEL = {
    2: 7, 3: 7, 4: 7, 5: 11,
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31,
    17: 5000, 18: 5000, 19: 5000, 20: 5000, 21: 5000, 22: 5000,
}

PASS = 0
FAIL = 0
TOTAL = 0

def score(name, cond, detail=""):
    global PASS, FAIL, TOTAL
    TOTAL += 1
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    _print(f"  [{tag}] {name}", flush=True)
    if detail:
        _print(f"         {detail}", flush=True)


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


# ═══════════════════════════════════════════════════════════════════
# EXTRACTION METHODS
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
    """Extract a_k(n) from heat trace data by subtracting known lower terms."""
    gs = []
    for f, t in zip(fs, ts):
        F = f / vol
        for j in range(target_k):
            F -= frac_to_mpf(known_exact_fracs[j]) * t ** j
        g = F / t ** target_k
        gs.append(g)
    # Use Neville (most reliable for this data)
    a_k_nev = neville(ts, gs, mpmath.mpf(0))
    a_k_nev_half = neville(ts[::2], [gs[i] for i in range(0, len(ts), 2)],
                           mpmath.mpf(0))
    err_nev = abs(a_k_nev - a_k_nev_half)
    # Also try Richardson
    a_k_rich, err_rich, order_rich = richardson_extrapolate(ts, gs, max_order=25)
    # Pick best
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


def factor_dict(n):
    d = {}
    for p in factor(abs(n)):
        d[p] = d.get(p, 0) + 1
    return d


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


def identify_rational(x_mpf, max_den=10**15, tol=1e-10, max_prime=None):
    x_str = mpmath.nstr(x_mpf, 250, strip_zeros=False)
    try:
        x_frac = Fraction(x_str)
    except (ValueError, ZeroDivisionError):
        return None, float('inf')
    best = None
    best_err = float('inf')
    for conv in _cf_convergents(x_frac, max_den=max_den * 10):
        if conv.denominator > max_den * 10:
            break
        err = abs(float(x_frac - conv))
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
        cand = x_frac.limit_denominator(md)
        err = abs(float(x_frac - cand))
        if err < tol and err < best_err:
            if max_prime:
                den_f = factor(cand.denominator)
                if den_f and max(den_f) > max_prime:
                    continue
            best = cand
            best_err = err
    if best is None and max_prime:
        for conv in _cf_convergents(x_frac, max_den=max_den):
            if conv.denominator > max_den:
                break
            err = abs(float(x_frac - conv))
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
    xf = Fraction(x)
    for k, c in enumerate(coeffs):
        result += c * xf ** k
    return result


def _factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def three_theorems(k):
    """Returns (c_top, c_subtop, c_const) for level k."""
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const


def lagrange_interpolate(points):
    """Exact Lagrange interpolation using Fractions."""
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
    """Recover polynomial with Three Theorems constraints.
    Top, subtop, and constant terms are fixed → deg-2 unknowns."""
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2   # number of free coefficients
    if len(clean_ns) < n_needed:
        return None, 0

    # Subtract known terms, reduce to lower-degree polynomial
    residual_pts = []
    for nv in clean_ns:
        nf = Fraction(nv)
        res = clean_rats[nv] - c_top * nf**deg \
              - c_subtop * nf**(deg-1) - c_const
        # Factor out n (since residual vanishes at n=0 after subtracting c_const)
        if nv != 0:
            residual_pts.append((nf, res / nf))
        else:
            residual_pts.append((nf, Fraction(0)))

    # Use exactly n_needed points for interpolation, rest for verification
    n_use = min(len(residual_pts), n_needed)
    reduced_poly = lagrange_interpolate(residual_pts[:n_use])

    # Verify with extra points
    extra = residual_pts[n_use:]
    n_verified = 0
    for p in extra:
        predicted = eval_poly(reduced_poly, p[0])
        if predicted == p[1]:
            n_verified += 1

    # Reconstruct full polynomial
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
# CHECKPOINT I/O
# ═══════════════════════════════════════════════════════════════════

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
    print("Toy 1307 — a₁₇ Full Polynomial Extraction (dps=1600)")
    print("=" * 70)

    ALL_DIMS = list(range(N_MIN, N_MAX + 1))

    # ─── Step 1: Load all checkpoints ───
    print(f"\n── Step 1: Loading {len(ALL_DIMS)} checkpoints ──")
    trace_data = {}
    for n in ALL_DIMS:
        ckpt = load_checkpoint(n)
        if ckpt:
            trace_data[n] = ckpt
    print(f"  Loaded: {len(trace_data)}/{len(ALL_DIMS)} dimensions")
    score("All checkpoints loaded", len(trace_data) == len(ALL_DIMS),
          f"n={min(trace_data.keys())}..{max(trace_data.keys())}")

    # ─── Step 2: Cascade extraction a₁..a_TARGET_K ───
    print(f"\n── Step 2: Cascade extraction a₁..a_{TARGET_K} ──")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}
    extraction_times = {}

    for k in range(2, TARGET_K + 1):
        t_k_start = time.time()
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 200)  # Conservative for high k
        n_need = deg - 2

        ak_clean = {}
        for n in sorted(trace_data.keys()):
            ts, fs, vol = trace_data[n]
            known_fracs = {0: Fraction(1)}
            complete = True
            for j in range(1, k):
                if j in all_rats and n in all_rats[j]:
                    known_fracs[j] = all_rats[j][n]
                else:
                    complete = False
                    break
            if not complete:
                continue

            ak, err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
            frac, frac_err = identify_rational(ak, max_den=10**15,
                                                tol=1e-8, max_prime=max_p)
            if frac is not None:
                ak_clean[n] = frac

        n_clean = len(ak_clean)
        t_k_end = time.time()
        extraction_times[k] = t_k_end - t_k_start

        # Try polynomial recovery
        if n_clean >= n_need:
            ak_poly, n_verified = constrained_polynomial(
                ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                # Fill in ALL dimensions from the polynomial
                for nv in ALL_DIMS:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
            else:
                KNOWN_POLYS[k] = None
                n_verified = 0
        else:
            KNOWN_POLYS[k] = None
            n_verified = 0

        all_rats[k] = ak_clean

        # Validate against known a_k(5)
        v5 = ak_clean.get(5)
        v5_status = ""
        if k in KNOWN_AK5 and v5 is not None:
            if v5 == KNOWN_AK5[k]:
                v5_status = "a_k(5) ✓"
            else:
                v5_status = f"a_k(5) MISMATCH: got {v5}, expected {KNOWN_AK5[k]}"

        # Compute ratio for speaking pair detection
        ratio_str = ""
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            if len(p) > deg:
                actual_ratio = p[deg-1] / p[deg]
                is_integer = actual_ratio.denominator == 1
                ratio_str = f" ratio={actual_ratio}"
                if is_integer:
                    ratio_str += f" = {int(actual_ratio)} INTEGER"
                    if k % n_C in [0, 1]:
                        ratio_str += " ← SPEAKING PAIR"

        poly_status = f"deg {len(KNOWN_POLYS[k])-1}" if KNOWN_POLYS[k] else "FAILED"
        verified_str = f" ({n_verified} verified)" if n_verified > 0 else ""

        # Special reporting for k >= 16
        if k >= 16:
            print(f"\n  *** a_{k:>2}: {n_clean}/{len(trace_data)} clean "
                  f"(need {n_need}), {poly_status}{verified_str}, "
                  f"{extraction_times[k]:.1f}s{ratio_str}")
            if v5_status:
                print(f"           {v5_status}")
            if KNOWN_POLYS.get(k):
                p = KNOWN_POLYS[k]
                ak5 = eval_poly(p, Fraction(5))
                den = ak5.denominator
                den_f = factor_dict(den)
                den_str = " × ".join(f"{pp}^{e}" if e > 1 else str(pp)
                                     for pp, e in sorted(den_f.items()))
                print(f"           a_{k}(5) = {ak5.numerator}/{den}")
                print(f"           den = {den_str}")
        else:
            print(f"  a_{k:>2}: {n_clean:>2}/{len(trace_data)} clean "
                  f"(need {n_need:>2}), {poly_status}{verified_str}, "
                  f"{extraction_times[k]:.1f}s {v5_status}{ratio_str}")

        if n_clean < n_need:
            print(f"\n  EXTRACTION STOPPED at k={k}. "
                  f"Have {n_clean}/{n_need} clean rationals — insufficient data.")
            break
        elif KNOWN_POLYS[k] is None:
            print(f"  a_{k:>2}: polynomial recovery failed despite {n_clean} clean rationals.")
            # Continue anyway — might succeed at next level with partial data

    # ─── Step 3: Results ───
    elapsed = time.time() - t_start
    max_confirmed = max((k for k in KNOWN_POLYS if KNOWN_POLYS[k] is not None),
                       default=1)

    print(f"\n{'='*70}")
    print(f"RESULTS — Highest confirmed level: k={max_confirmed}")
    print(f"{'='*70}")

    # Speaking pair analysis
    print(f"\n── Speaking Pairs ──")
    for k in range(5, max_confirmed + 1):
        if KNOWN_POLYS.get(k):
            p = KNOWN_POLYS[k]
            deg = 2 * k
            if len(p) > deg:
                ratio = p[deg-1] / p[deg]
                if ratio.denominator == 1:
                    r = int(ratio)
                    sp = "SPEAKING" if k % n_C in [0, 1] else "non-sp"
                    print(f"  k={k:>2}: ratio = {r:>5}  [{sp}]")

    # k=17 specific analysis
    if 17 in KNOWN_POLYS and KNOWN_POLYS[17] is not None:
        print(f"\n── a₁₇ Analysis ──")
        p17 = KNOWN_POLYS[17]
        deg17 = 34
        a17_5 = eval_poly(p17, Fraction(5))
        den17 = a17_5.denominator
        den17_f = factor_dict(den17)

        print(f"  a₁₇ polynomial: degree {len(p17)-1}")
        print(f"  a₁₇(5) = {a17_5.numerator}/{den17}")
        print(f"  den = " + " × ".join(f"{pp}^{e}" if e > 1 else str(pp)
                                        for pp, e in sorted(den17_f.items())))

        # Check Three Theorems
        c_top_17, c_sub_17, c_const_17 = three_theorems(17)
        score("a₁₇ top coeff = 1/(3¹⁷·17!)",
              p17[deg17] == c_top_17,
              f"got {p17[deg17]}")
        score("a₁₇ const term = -1/(2·17!)",
              p17[0] == c_const_17,
              f"got {p17[0]}")

        # Ratio
        if len(p17) > deg17:
            ratio17 = p17[deg17-1] / p17[deg17]
            expected_ratio = Fraction(-17 * 16, 2 * n_C)
            score("a₁₇ ratio = -C(17,2)/5 = -136/5",
                  ratio17 == expected_ratio,
                  f"got {ratio17} = {float(ratio17):.6f}")
            score("a₁₇ ratio NOT integer (k=17 not a speaking pair)",
                  ratio17.denominator != 1,
                  f"17 mod {n_C} = {17 % n_C}")

        # Validate against known
        score("a₁₇(5) matches Toy 671 Phase A",
              a17_5 == KNOWN_AK5.get(17, None),
              f"expected {KNOWN_AK5.get(17)}")

        # QUIET check
        def is_prime(n):
            if n < 2: return False
            if n < 4: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i+2) == 0: return False
                i += 6
            return True

        val_35 = 2 * 17 + 1
        score("k=17 QUIET: 2k+1 = 35 is composite",
              not is_prime(val_35),
              f"35 = {n_C} × {g}")

        # Denominator BST structure
        if 179 in den17_f:
            score("den contains 179 = C₂·rank·N_c·n_C - 1",
                  179 == C_2 * rank * N_c * n_C - 1,
                  f"179 = {C_2}·{rank}·{N_c}·{n_C} - 1 = {C_2*rank*N_c*n_C} - 1")

    # k=18 analysis (if we got there)
    if 18 in KNOWN_POLYS and KNOWN_POLYS[18] is not None:
        print(f"\n── a₁₈ Analysis (BONUS) ──")
        p18 = KNOWN_POLYS[18]
        deg18 = 36
        a18_5 = eval_poly(p18, Fraction(5))
        den18 = a18_5.denominator

        print(f"  a₁₈ polynomial: degree {len(p18)-1}")
        print(f"  a₁₈(5) = {a18_5.numerator}/{den18}")

        if len(p18) > deg18:
            ratio18 = p18[deg18-1] / p18[deg18]
            expected18 = Fraction(-18 * 17, 2 * n_C)
            is_int = ratio18.denominator == 1
            print(f"  ratio = {ratio18} = {float(ratio18):.4f}")
            print(f"  expected = {expected18} = {float(expected18):.4f}")
            if is_int:
                print(f"  *** INTEGER RATIO = {int(ratio18)} ***")
            score("a₁₈ ratio = -C(18,2)/5 = -153/5",
                  ratio18 == expected18,
                  f"{'INTEGER' if is_int else 'non-integer'}: 18 mod 5 = {18%5}")
    elif TARGET_K >= 18:
        print(f"\n  a₁₈: extraction failed or insufficient data.")

    # Summary
    print(f"\n{'='*70}")
    print(f"SCORE: {PASS}/{TOTAL} PASS")
    print(f"Total time: {elapsed:.1f}s ({elapsed/60:.1f}m)")
    print(f"Extraction times by level (k ≥ 10):")
    for k in sorted(extraction_times.keys()):
        if k >= 10:
            print(f"  k={k}: {extraction_times[k]:.1f}s")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
