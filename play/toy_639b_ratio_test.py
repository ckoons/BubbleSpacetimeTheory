#!/usr/bin/env python3
"""
Toy 639b — Independent Verification: Is the ratio really -24?
=============================================================
The constrained polynomial in Toy 639 FORCES c_sub/c_top = -24.
This toy tests whether the DATA independently produces -24.

Three independent tests:
  A. Leading-ratio extraction: a_16(n) / (c_top·n^32) → 1 + ratio/n + ...
     Compute ratio from the slope — no polynomial constraint needed.
  B. Unconstrained fit (c_const only): fit 32 free coefficients from 33 points.
     Read off c_32 and c_31/c_32. If ratio = -24, it's genuine.
  C. Two-point ratio estimator: for pairs (n1, n2), extract ratio from
     the difference a_16(n1)/n1^32 - a_16(n2)/n2^32.

If ALL three independently give -24, the gauge hierarchy is real.

Elie — March 31, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie). March 2026.
"""

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

PASS = 0
FAIL = 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_361_checkpoint")


def score(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "✓ PASS"
    else:
        FAIL += 1
        tag = "✗ FAIL"
    print(f"  {tag}: {name}")
    if detail:
        print(f"         {detail}")


# ═══════════════════════════════════════════════════════════════════
# Reuse infrastructure from toy_639
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
    return 2000

def chebyshev_nodes(t_lo, t_hi, n_pts):
    t_lo_m = mpmath.mpf(t_lo)
    t_hi_m = mpmath.mpf(t_hi)
    mid = (t_lo_m + t_hi_m) / 2
    half = (t_hi_m - t_lo_m) / 2
    return sorted([mid + half * mpmath.cos((2 * k + 1) * mpmath.pi / (2 * n_pts))
                    for k in range(n_pts)])

def compute_heat_trace(n, eigs, dims, ts):
    results = []
    for t in ts:
        Z = mpmath.fsum(mpmath.mpf(d) * mpmath.exp(-mpmath.mpf(lam) * t)
                        for lam, d in zip(eigs, dims))
        results.append((4 * mpmath.pi * t) ** n * Z)
    return results

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

def _factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def eval_poly(coeffs, x):
    result = Fraction(0)
    for k, c in enumerate(coeffs):
        result += c * Fraction(x) ** k
    return result

def three_theorems(k):
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const

# Lagrange interpolation (unconstrained)
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
            for k in range(len(basis)):
                new[k + 1] += basis[k]
                new[k] -= xs[j] * basis[k]
            basis = new
        for k in range(len(basis)):
            if k < n:
                coeffs[k] += ys[i] * basis[k] / denom
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


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
}

MAX_PRIME_BY_LEVEL = {
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23, 12: 23, 13: 23, 14: 29, 15: 31, 16: 31,
}

N_PTS = 48
FIXED_T_LO = 0.0008
FIXED_T_HI = 0.009


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()

    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  Toy 639b — Independent Ratio Verification                     ║")
    print("║  Is -24 = -dim(SU(5)) genuine or an artifact?                  ║")
    print("║  Three independent tests of the sub-leading ratio              ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    TARGET_K = 16
    TARGET_DEG = 32
    c_top_16, c_sub_16, c_const_16 = three_theorems(TARGET_K)

    print(f"\n  Three Theorems prediction for k={TARGET_K}:")
    print(f"    c_top  = 1/(3^16 · 16!) = {c_top_16}")
    print(f"    c_sub  = -24 × c_top    = {c_sub_16}")
    print(f"    c_const = 1/(2·16!)     = {c_const_16}")
    print(f"    predicted ratio = c_sub/c_top = {c_sub_16 / c_top_16}")

    # ─── Load and cascade (same as toy_639) ────────────────────────
    print(f"\n─── Phase 1: Cascade a₁..a₁₅ + Extract a₁₆ Values ───")

    CASCADE_RANGE = range(3, 14)
    ALL_RANGE = []
    for n in range(3, 36):
        if os.path.exists(os.path.join(CKPT_DIR, f"adaptive_heat_n{n:02d}.json")):
            ALL_RANGE.append(n)

    fixed_ts = chebyshev_nodes(FIXED_T_LO, FIXED_T_HI, N_PTS)
    fixed_data = {}
    for n in CASCADE_RANGE:
        cached = load_heat_trace(n, "fixed")
        if cached:
            fixed_data[n] = (cached[1], cached[2])

    adaptive_data = {}
    adaptive_ts = {}
    for n in ALL_RANGE:
        t_lo, t_hi = adaptive_t_window(n, TARGET_K)
        ts = chebyshev_nodes(t_lo, t_hi, N_PTS)
        adaptive_ts[n] = ts
        cached = load_heat_trace(n, "adaptive")
        if cached:
            adaptive_data[n] = (cached[1], cached[2])

    missing_adaptive = [n for n in ALL_RANGE if n not in adaptive_data]
    if missing_adaptive:
        print(f"  Computing {len(missing_adaptive)} missing adaptive traces...")
        for n in missing_adaptive:
            pmax = adaptive_pmax(n)
            eigs, dims = build_spectrum(n, pmax)
            ts = adaptive_ts[n]
            fs = compute_heat_trace(n, eigs, dims, ts)
            vol = neville(ts, fs, mpmath.mpf(0))
            adaptive_data[n] = (fs, vol)

    # Cascade a₁..a₁₅
    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_RANGE}}

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

    for k in range(6, TARGET_K):
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 31)
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
            clean_ns = sorted(ak_clean.keys())
            residual_pts = []
            for nv in clean_ns:
                res = ak_clean[nv] - c_top * Fraction(nv)**deg \
                      - c_sub * Fraction(nv)**(deg-1) - c_const
                residual_pts.append((Fraction(nv), res / Fraction(nv)))
            n_use = min(len(residual_pts), n_need)
            reduced_poly = lagrange_interpolate(residual_pts[:n_use])
            ak_poly_k = [Fraction(0)] * (deg + 1)
            ak_poly_k[0] = c_const
            for kk, c in enumerate(reduced_poly):
                ak_poly_k[kk + 1] += c
            ak_poly_k[deg - 1] += c_sub
            ak_poly_k[deg] = c_top
            for nv in ALL_RANGE:
                ak_clean[nv] = eval_poly(ak_poly_k, Fraction(nv))
            KNOWN_POLYS[k] = ak_poly_k
        else:
            KNOWN_POLYS[k] = None
        all_rats[k] = ak_clean

    have_all = all(KNOWN_POLYS.get(j) is not None for j in range(1, TARGET_K))
    if not have_all:
        missing = [j for j in range(1, TARGET_K) if KNOWN_POLYS.get(j) is None]
        print(f"  ✗ CANNOT EXTRACT a_{TARGET_K}: missing polys for {missing}")
        return

    print(f"  Cascade complete (a₁..a₁₅). Extracting a₁₆ at each dimension...")

    # Extract a₁₆ NUMERICAL values (mpmath, high precision)
    k = TARGET_K
    ak_mpf_vals = {}  # n -> mpf value (no rational ID yet)

    for n in ALL_RANGE:
        if n not in adaptive_data:
            continue
        fs, vol = adaptive_data[n]
        ts = adaptive_ts[n]
        known_fracs = {0: Fraction(1)}
        for j in range(1, k):
            known_fracs[j] = all_rats[j][n]
        a_val, a_err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
        ak_mpf_vals[n] = (a_val, a_err)

    print(f"  Extracted a₁₆ at {len(ak_mpf_vals)} dimensions")

    # ═══════════════════════════════════════════════════════════════
    # TEST A: Leading-Ratio Extraction
    # ═══════════════════════════════════════════════════════════════
    print(f"\n{'═' * 64}")
    print(f"  TEST A: Leading-Ratio Extraction (no polynomial constraint)")
    print(f"{'═' * 64}")

    print(f"\n  a₁₆(n) = c_top·n^32·(1 + ratio/n + O(1/n²))")
    print(f"  Define: y(n) = [a₁₆(n) / (c_top·n^32)] - 1")
    print(f"  Then: y(n) ≈ ratio/n + O(1/n²)")
    print(f"  So: n·y(n) → ratio as n → ∞")
    print(f"")

    c_top_mpf = frac_to_mpf(c_top_16)

    print(f"  {'n':>4}  {'n·y(n)':>20}  {'err_a16':>12}  quality")
    print(f"  {'─'*4}  {'─'*20}  {'─'*12}  {'─'*10}")

    ratio_estimates = []
    for n in sorted(ak_mpf_vals.keys()):
        a_val, a_err = ak_mpf_vals[n]
        n_mpf = mpmath.mpf(n)

        # y(n) = a₁₆(n) / (c_top · n^32) - 1
        y = a_val / (c_top_mpf * n_mpf**32) - 1

        # n·y(n) should → ratio
        nyn = n_mpf * y

        abs_err = float(abs(a_err))
        if abs_err < 1.0:
            quality = "★★★"
        elif abs_err < 1e5:
            quality = "★★"
        elif abs_err < 1e15:
            quality = "★"
        else:
            quality = "·"

        nyn_float = float(nyn)
        print(f"  {n:>4}  {nyn_float:>20.6f}  {abs_err:>12.1e}  {quality}")

        ratio_estimates.append((n, nyn_float, abs_err, quality))

    # Weighted average of high-quality estimates
    hq = [(n, r) for n, r, err, q in ratio_estimates if q in ("★★★", "★★")]
    if hq:
        avg_hq = sum(r for _, r in hq) / len(hq)
        print(f"\n  High-quality average (★★+): {avg_hq:.6f} (from {len(hq)} dims)")
        print(f"  Deviation from -24: {avg_hq - (-24):.6f}")

        # Even more selective — only ★★★
        hq3 = [(n, r) for n, r, err, q in ratio_estimates if q == "★★★"]
        if hq3:
            avg_hq3 = sum(r for _, r in hq3) / len(hq3)
            print(f"  Best-quality average (★★★): {avg_hq3:.6f} (from {len(hq3)} dims)")
            print(f"  Deviation from -24: {avg_hq3 - (-24):.6f}")

    # Check: does n·y(n) converge toward -24?
    lown = [(n, r) for n, r, err, q in ratio_estimates if n <= 10 and q in ("★★★", "★★")]
    highn = [(n, r) for n, r, err, q in ratio_estimates if n >= 15 and q in ("★★★", "★★")]

    if lown:
        avg_low = sum(r for _, r in lown) / len(lown)
        print(f"\n  Low-n average (n≤10, ★★+): {avg_low:.6f}")
    if highn:
        avg_high = sum(r for _, r in highn) / len(highn)
        print(f"  High-n average (n≥15, ★★+): {avg_high:.6f}")

    # Richardson extrapolation on the n·y(n) sequence to get ratio at n→∞
    print(f"\n  Richardson extrapolation of n·y(n) → ratio:")
    hq_sorted = sorted([(n, r) for n, r, err, q in ratio_estimates if q in ("★★★", "★★")],
                        key=lambda p: p[0])
    if len(hq_sorted) >= 4:
        inv_ns = [mpmath.mpf(1) / mpmath.mpf(n) for n, _ in hq_sorted]
        nyn_vals = [mpmath.mpf(r) for _, r in hq_sorted]
        ratio_rich, ratio_err, ratio_order = richardson_extrapolate(inv_ns, nyn_vals, max_order=min(len(hq_sorted), 15))
        print(f"    Richardson ratio = {float(ratio_rich):.10f}")
        print(f"    Richardson err   = {float(ratio_err):.2e}")
        print(f"    Richardson order = {ratio_order}")
        print(f"    Deviation from -24: {float(ratio_rich) - (-24):.10f}")

        close_to_24 = abs(float(ratio_rich) - (-24)) < 0.1
        score("Test A: Leading ratio ≈ -24 (within 0.1)",
              close_to_24,
              f"Richardson = {float(ratio_rich):.6f}")
    else:
        print(f"    Insufficient high-quality data for Richardson")
        score("Test A: Leading ratio ≈ -24", False,
              f"Only {len(hq_sorted)} high-quality points")

    # ═══════════════════════════════════════════════════════════════
    # TEST B: Unconstrained Polynomial (if enough points)
    # ═══════════════════════════════════════════════════════════════
    print(f"\n{'═' * 64}")
    print(f"  TEST B: Unconstrained Polynomial Recovery")
    print(f"{'═' * 64}")

    # Identify rationals for a₁₆ at each dimension (unconstrained)
    max_p = 31
    ak_clean = {}
    for n in ALL_RANGE:
        if n not in ak_mpf_vals:
            continue
        a_val, a_err = ak_mpf_vals[n]
        frac, _ = identify_rational(a_val, max_den=500000000000000,
                                    tol=1e-8, max_prime=max_p)
        if frac:
            ak_clean[n] = frac

    n_clean = len(ak_clean)
    print(f"\n  Clean rational identifications: {n_clean}/{len(ALL_RANGE)}")
    print(f"  Need 33 for unconstrained degree-32 polynomial")

    if n_clean >= 33:
        print(f"  → Have {n_clean} ≥ 33. Attempting UNCONSTRAINED Lagrange...")

        clean_ns = sorted(ak_clean.keys())
        # Use first 33 for the fit
        fit_ns = clean_ns[:33]

        print(f"  Fitting on n = {fit_ns[0]}..{fit_ns[-1]} ({len(fit_ns)} points)")

        pts = [(Fraction(nv), ak_clean[nv]) for nv in fit_ns]

        t0 = time.time()
        uc_poly = lagrange_interpolate(pts)
        dt = time.time() - t0
        print(f"  Lagrange interpolation: {dt:.1f}s")

        d = len(uc_poly) - 1
        print(f"  Polynomial degree: {d}")

        if d >= 32:
            uc_c32 = uc_poly[32]
            uc_c31 = uc_poly[31]

            print(f"\n  Unconstrained coefficients:")
            print(f"    c_32 = {uc_c32}")
            print(f"    c_31 = {uc_c31}")
            print(f"    c_0  = {uc_poly[0]}")

            print(f"\n  Three Theorems predictions:")
            print(f"    c_32 predicted = {c_top_16}")
            print(f"    c_0  predicted = {c_const_16}")

            c32_match = (uc_c32 == c_top_16)
            c0_match = (uc_poly[0] == c_const_16)
            print(f"    c_32 match: {'✓' if c32_match else '✗'}")
            print(f"    c_0  match: {'✓' if c0_match else '✗'}")

            if uc_c32 != 0:
                uc_ratio = uc_c31 / uc_c32
                uc_ratio_float = float(uc_ratio)
                print(f"\n  UNCONSTRAINED ratio c_31/c_32 = {uc_ratio}")
                print(f"    = {uc_ratio_float:.10f}")
                print(f"    predicted = -24")
                print(f"    deviation = {uc_ratio_float - (-24):.10f}")

                ratio_match = (uc_ratio == Fraction(-24))
                ratio_close = abs(uc_ratio_float - (-24)) < 0.01

                score("Test B: c_32 = 1/(3^16·16!) (unconstrained)",
                      c32_match,
                      f"c_32 = {uc_c32}")
                score("Test B: c_0 = 1/(2·16!) (unconstrained)",
                      c0_match,
                      f"c_0 = {uc_poly[0]}")
                score("Test B: Unconstrained ratio = -24 (exact)",
                      ratio_match,
                      f"ratio = {uc_ratio}")
                if not ratio_match:
                    score("Test B: Unconstrained ratio ≈ -24 (within 0.01)",
                          ratio_close,
                          f"ratio = {uc_ratio_float:.10f}")
            else:
                print(f"  c_32 = 0 — polynomial degree < 32")
                score("Test B: Unconstrained c_32 nonzero", False)
        else:
            print(f"  Polynomial degree {d} < 32")
            score("Test B: Unconstrained degree = 32", False)
    else:
        print(f"  → Have only {n_clean} < 33. Cannot do full unconstrained fit.")
        score("Test B: Enough clean points for unconstrained fit", False,
              f"{n_clean}/33")

    # ═══════════════════════════════════════════════════════════════
    # TEST C: Pairwise Ratio Estimator
    # ═══════════════════════════════════════════════════════════════
    print(f"\n{'═' * 64}")
    print(f"  TEST C: Pairwise Ratio Estimator")
    print(f"{'═' * 64}")

    print(f"\n  For two dimensions n1, n2:")
    print(f"  a₁₆(n) ≈ c_top·n^32·(1 + r/n + s/n² + ...)")
    print(f"  Define: R(n1,n2) = [n1·n2·(a₁₆(n1)/n1^32 - a₁₆(n2)/n2^32)] / ")
    print(f"                     [c_top·(n1 - n2)]")
    print(f"  Then: R(n1,n2) → ratio as n1,n2 → ∞")
    print(f"")

    # Use mpf values for this
    good_ns = [n for n in sorted(ak_mpf_vals.keys())
               if float(abs(ak_mpf_vals[n][1])) < 1e5]

    if len(good_ns) >= 2:
        print(f"  Using {len(good_ns)} dimensions with err < 10⁵")
        print(f"  Best pairs (adjacent good dimensions):")
        print(f"")
        print(f"  {'n1':>4} {'n2':>4}  {'R(n1,n2)':>20}")
        print(f"  {'─'*4} {'─'*4}  {'─'*20}")

        pair_ratios = []
        for i in range(len(good_ns) - 1):
            n1, n2 = good_ns[i], good_ns[i+1]
            a1, _ = ak_mpf_vals[n1]
            a2, _ = ak_mpf_vals[n2]

            t1 = a1 / (c_top_mpf * mpmath.mpf(n1)**32)
            t2 = a2 / (c_top_mpf * mpmath.mpf(n2)**32)

            R = mpmath.mpf(n1) * mpmath.mpf(n2) * (t1 - t2) / mpmath.mpf(n1 - n2)
            R_float = float(R)
            print(f"  {n1:>4} {n2:>4}  {R_float:>20.6f}")
            pair_ratios.append(R_float)

        if pair_ratios:
            avg_pair = sum(pair_ratios) / len(pair_ratios)
            print(f"\n  Average pairwise ratio: {avg_pair:.6f}")
            print(f"  Deviation from -24: {avg_pair - (-24):.6f}")

            # Median (more robust)
            sorted_pr = sorted(pair_ratios)
            med = sorted_pr[len(sorted_pr) // 2]
            print(f"  Median pairwise ratio: {med:.6f}")
            print(f"  Median deviation from -24: {med - (-24):.6f}")

            close = abs(avg_pair - (-24)) < 1.0
            score("Test C: Pairwise ratio ≈ -24 (within 1.0)",
                  close,
                  f"avg = {avg_pair:.6f}")
    else:
        print(f"  Only {len(good_ns)} good dimensions — need ≥2")
        score("Test C: Enough good dimensions", False)

    # ═══════════════════════════════════════════════════════════════
    # SCORECARD
    # ═══════════════════════════════════════════════════════════════
    elapsed = time.time() - t_start

    print(f"\n{'═' * 64}")
    print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
    print(f"{'═' * 64}")

    if PASS == PASS + FAIL:
        print(f"\n  ALL PASS — ratio = -24 independently verified!")
        print(f"  The gauge hierarchy is NOT an artifact of the constraint.")
    elif PASS > 0:
        print(f"\n  PARTIAL — {PASS}/{PASS+FAIL} tests support ratio ≈ -24")
    else:
        print(f"\n  NO CONFIRMATION — ratio = -24 not independently verified")
        print(f"  May need higher precision checkpoints (dps=1600+)")

    print(f"  Runtime: {elapsed:.0f}s ({elapsed/60:.1f}min)")


if __name__ == '__main__':
    main()
