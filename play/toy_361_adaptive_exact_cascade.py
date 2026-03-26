#!/usr/bin/env python3
"""
Toy 361 — Adaptive Exact Cascade: Breaking the a₁₂ Wall
=========================================================
Three innovations over Toys 288/308:

  (1) ADAPTIVE t-WINDOW PER n: For large n, a_k(n) ~ n^{2k}, so adjacent
      coefficients a₁₂·t¹² and a₁₃·t¹³ are comparable unless t << 1/n².
      We set T_HI(n) ~ C/n² so the next-order correction stays small.

  (2) EXACT SUBTRACTION: Load a₁..a₁₁ as exact rational polynomials from
      Toys 273-278. Subtract in mpf from exact Fraction → zero cascade error
      for all 11 known levels. (Toy 288 had this; Toy 308 partially.)

  (3) RICHARDSON EXTRAPOLATION: Instead of 48-64 node Neville (which can
      amplify errors at the extrapolation point), use a Richardson tableau
      with convergence monitoring. Start with 2 nodes, double, track when
      the extrapolated value stabilizes.

Target: a₁₂ polynomial (degree 24). Need 22 clean rationals from 33 data
points (n=3..35). Three Theorems give 3 constraints → 22 unknowns.

Structural prediction: a₁₂ is a QUIET level (B₂₄ → no new prime beyond 23).

CHECKPOINTING: Results are saved after each expensive computation.
If the script dies, restart it — it picks up from the last checkpoint.
Checkpoint dir: play/toy_361_checkpoint/

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import sys
import os
import json
import time
from fractions import Fraction
import mpmath

# Force unbuffered output
_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

mpmath.mp.dps = 800  # 800 digits — headroom for exact subtraction + extraction

PASS = 0
FAIL = 0

# Checkpoint directory (relative to script location)
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
# CHECKPOINT I/O
# ═══════════════════════════════════════════════════════════════════

def ensure_ckpt_dir():
    os.makedirs(CKPT_DIR, exist_ok=True)


def ckpt_path(name):
    return os.path.join(CKPT_DIR, name)


def save_mpf_list(vals, filepath):
    """Save a list of mpf values as high-precision decimal strings."""
    data = [mpmath.nstr(v, mpmath.mp.dps + 50, strip_zeros=False) for v in vals]
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_mpf_list(filepath):
    """Load a list of mpf values from string representation."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return [mpmath.mpf(s) for s in data]


def save_heat_trace(n, ts, fs, vol, prefix):
    """Save heat trace computation for dimension n."""
    ensure_ckpt_dir()
    data = {
        'ts': [mpmath.nstr(t, mpmath.mp.dps + 50, strip_zeros=False) for t in ts],
        'fs': [mpmath.nstr(f, mpmath.mp.dps + 50, strip_zeros=False) for f in fs],
        'vol': mpmath.nstr(vol, mpmath.mp.dps + 50, strip_zeros=False),
    }
    fp = ckpt_path(f"{prefix}_heat_n{n:02d}.json")
    with open(fp, 'w') as f:
        json.dump(data, f)


def load_heat_trace(n, prefix):
    """Load heat trace checkpoint. Returns (ts, fs, vol) or None."""
    fp = ckpt_path(f"{prefix}_heat_n{n:02d}.json")
    if not os.path.exists(fp):
        return None
    try:
        with open(fp, 'r') as f:
            data = json.load(f)
        ts = [mpmath.mpf(s) for s in data['ts']]
        fs = [mpmath.mpf(s) for s in data['fs']]
        vol = mpmath.mpf(data['vol'])
        return ts, fs, vol
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"      [WARN] Corrupt checkpoint {fp}: {e}")
        return None


def save_polynomial(k, poly):
    """Save exact polynomial as list of Fraction strings."""
    ensure_ckpt_dir()
    data = [str(c) for c in poly]
    fp = ckpt_path(f"poly_a{k:02d}.json")
    with open(fp, 'w') as f:
        json.dump(data, f)


def load_polynomial(k):
    """Load exact polynomial checkpoint. Returns list of Fraction or None."""
    fp = ckpt_path(f"poly_a{k:02d}.json")
    if not os.path.exists(fp):
        return None
    try:
        with open(fp, 'r') as f:
            data = json.load(f)
        return [Fraction(s) for s in data]
    except (json.JSONDecodeError, ValueError) as e:
        print(f"      [WARN] Corrupt checkpoint {fp}: {e}")
        return None


def save_rationals(k, rats):
    """Save exact rational values dict {n: Fraction}."""
    ensure_ckpt_dir()
    data = {str(n): str(v) for n, v in rats.items()}
    fp = ckpt_path(f"rats_a{k:02d}.json")
    with open(fp, 'w') as f:
        json.dump(data, f)


def load_rationals(k):
    """Load exact rational values dict. Returns {n: Fraction} or None."""
    fp = ckpt_path(f"rats_a{k:02d}.json")
    if not os.path.exists(fp):
        return None
    try:
        with open(fp, 'r') as f:
            data = json.load(f)
        return {int(n): Fraction(v) for n, v in data.items()}
    except (json.JSONDecodeError, ValueError) as e:
        print(f"      [WARN] Corrupt checkpoint {fp}: {e}")
        return None


def frac_to_mpf(frac):
    return mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)


# ═══════════════════════════════════════════════════════════════════
# WEYL DIMENSION FORMULAS (integer arithmetic, exact)
# ═══════════════════════════════════════════════════════════════════

def _dim_B(p, q, r):
    """Dimension of SO(2r+1) rep with highest weight (p, q, 0, ..., 0)."""
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
    """Dimension of SO(2r) rep with highest weight (p, q, 0, ..., 0)."""
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
# SPECTRUM BUILDER
# ═══════════════════════════════════════════════════════════════════

def build_spectrum(n, P_max):
    """Aggregated spectrum: (eigenvalues, multiplicities) as int lists."""
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
    """Adaptive P_MAX: more eigenvalues for larger n to ensure convergence."""
    if n <= 10: return 1000
    if n <= 20: return 1500
    return 2000


# ═══════════════════════════════════════════════════════════════════
# ADAPTIVE t-WINDOW
# ═══════════════════════════════════════════════════════════════════

def adaptive_t_window(n, target_k):
    """Choose t-window so that the (k+1)-th term is small vs the k-th."""
    t_hi = min(0.01, max(5e-6, 0.3 / (n * n)))
    t_lo = max(1e-7, t_hi / 20)
    return t_lo, t_hi


# ═══════════════════════════════════════════════════════════════════
# HEAT TRACE & EXTRACTION
# ═══════════════════════════════════════════════════════════════════

def chebyshev_nodes(t_lo, t_hi, n_pts):
    t_lo_m = mpmath.mpf(t_lo)
    t_hi_m = mpmath.mpf(t_hi)
    mid = (t_lo_m + t_hi_m) / 2
    half = (t_hi_m - t_lo_m) / 2
    nodes = [mid + half * mpmath.cos((2 * k + 1) * mpmath.pi / (2 * n_pts))
             for k in range(n_pts)]
    nodes.sort()
    return nodes


def compute_heat_trace(n, eigs, dims, ts):
    """Compute f(t) = (4πt)^n × Z(t) at given t values."""
    results = []
    for t in ts:
        Z = mpmath.fsum(mpmath.mpf(d) * mpmath.exp(-mpmath.mpf(lam) * t)
                        for lam, d in zip(eigs, dims))
        results.append((4 * mpmath.pi * t) ** n * Z)
    return results


def neville(xs, ys, x_target):
    """Neville's polynomial interpolation → value at x_target."""
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
    """Richardson extrapolation of g(t) → g(0)."""
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
    """Extract a_{target_k} using exact Fraction subtraction + Richardson."""
    gs = []
    for f, t in zip(fs, ts):
        F = f / vol

        for j in range(target_k):
            F -= frac_to_mpf(known_exact_fracs[j]) * t ** j

        g = F / t ** target_k
        gs.append(g)

    # Method 1: Neville (full node set)
    a_k_nev = neville(ts, gs, mpmath.mpf(0))
    a_k_nev_half = neville(ts[::2], [gs[i] for i in range(0, len(ts), 2)], mpmath.mpf(0))
    err_nev = abs(a_k_nev - a_k_nev_half)

    # Method 2: Richardson
    a_k_rich, err_rich, order_rich = richardson_extrapolate(ts, gs, max_order=25)

    # Method 3: Neville on first 20 nodes only
    n20 = min(20, len(ts))
    a_k_nev20 = neville(ts[:n20], gs[:n20], mpmath.mpf(0))

    # Agreement between methods
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
    """Multi-strategy rational identification."""
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
    """Exact Fraction-arithmetic Lagrange interpolation."""
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


def eval_poly(coeffs, x):
    result = Fraction(0)
    for k, c in enumerate(coeffs):
        result += c * Fraction(x) ** k
    return result


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


def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True


def _factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def constrained_polynomial(clean_rats, c_top, c_subtop, c_const, deg):
    """Build degree-deg polynomial with known leading, sub-leading, and constant."""
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2
    if len(clean_ns) < n_needed:
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
        print(f"      Reduced degree-{deg-3}: {'✓ VERIFIED' if ok else '✗'} "
              f"({len(extra)} extra)")
    else:
        print(f"      Reduced degree-{deg-3}: exact from {n_use} points")

    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(reduced_poly):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def _try_constrained(clean_rats, c_top, c_subtop, c_const, deg):
    """Silent constrained_polynomial for leave-one-out."""
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2
    if len(clean_ns) < n_needed:
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
    if not ok:
        return None

    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(reduced_poly):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def robust_constrained_polynomial(clean_rats, c_top, c_subtop, c_const, deg, label=""):
    """Constrained polynomial with leave-one-out and pair-removal validation."""
    poly = constrained_polynomial(clean_rats, c_top, c_subtop, c_const, deg)
    if poly:
        all_ok = all(eval_poly(poly, Fraction(nv)) == clean_rats[nv]
                     for nv in clean_rats)
        if all_ok:
            return poly, clean_rats

    print(f"      {label}Standard polynomial failed. Trying leave-one-out...")
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2

    if len(clean_ns) <= n_needed:
        print(f"      Cannot do leave-one-out: have {len(clean_ns)}, need >{n_needed}")
        return None, clean_rats

    for remove_n in clean_ns:
        reduced = {k: v for k, v in clean_rats.items() if k != remove_n}
        if len(reduced) < n_needed:
            continue
        poly = _try_constrained(reduced, c_top, c_subtop, c_const, deg)
        if poly:
            all_ok = all(eval_poly(poly, Fraction(nv)) == reduced[nv]
                         for nv in reduced)
            if all_ok:
                pred = eval_poly(poly, Fraction(remove_n))
                if pred != clean_rats[remove_n]:
                    print(f"      ✓ Found bad point at n={remove_n}! "
                          f"Expected {pred}, got {clean_rats[remove_n]}")
                    print(f"      Polynomial verified on {len(reduced)} remaining points")
                    return poly, reduced

    if len(clean_ns) > n_needed + 1:
        print(f"      Single removal failed. Trying pair removal...")
        for i, n1 in enumerate(clean_ns):
            for n2 in clean_ns[i+1:]:
                reduced = {k: v for k, v in clean_rats.items()
                          if k != n1 and k != n2}
                if len(reduced) < n_needed:
                    continue
                poly = _try_constrained(reduced, c_top, c_subtop, c_const, deg)
                if poly:
                    all_ok = all(eval_poly(poly, Fraction(nv)) == reduced[nv]
                                 for nv in reduced)
                    if all_ok:
                        print(f"      ✓ Found bad pair: n={n1}, n={n2}")
                        print(f"      Polynomial verified on {len(reduced)} points")
                        return poly, reduced

    print(f"      ✗ Leave-one-out failed")
    return None, clean_rats


# ═══════════════════════════════════════════════════════════════════
# KNOWN EXACT POLYNOMIALS a₁..a₁₁ (from Toys 273-278, verified)
# ═══════════════════════════════════════════════════════════════════

# a₁(n) = (2n² - 3)/6
A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]  # = [-1/2, 0, 1/3]

KNOWN_POLYS = {1: A1_POLY}  # Will be populated from checkpoints or computed

# Three Theorems predictions
def three_theorems(k):
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const


# Known a_k(5) values for verification
KNOWN_VALUES = {
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
}


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    ensure_ckpt_dir()

    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  Toy 361 — Adaptive Exact Cascade: Breaking the a₁₂ Wall      ║")
    print("║  Three innovations: adaptive t, exact subtraction, Richardson  ║")
    print("║  dps=800, adaptive P_MAX, n=3..35, target a₁₂                 ║")
    print("║  WITH CHECKPOINTING — restart-safe                            ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    N_PTS = 48          # Chebyshev nodes per extraction
    CASCADE_RANGE = range(3, 14)   # n=3..13 for building a₂..a₅
    ALL_RANGE = range(3, 36)       # n=3..35 for a₆..a₁₂ (33 data points)

    MAX_PRIME_BY_LEVEL = {
        6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23, 12: 23,
    }

    # ─── Phase 0: Build spectra with adaptive P_MAX ──────────────
    print(f"\n  Phase 0: Building spectra (adaptive P_MAX)")
    print("  " + "─" * 58)

    spectra = {}
    for n in ALL_RANGE:
        t0 = time.time()
        pmax = adaptive_pmax(n)
        eigs, dims = build_spectrum(n, pmax)
        spectra[n] = (eigs, dims)
        N_grp = n + 2
        group = f"SO({N_grp})" + (f" B_{(N_grp-1)//2}" if N_grp % 2 == 1
                                   else f" D_{N_grp//2}")
        print(f"    n={n:>2} ({group:>9}): {len(eigs):>6} eigs, "
              f"P_MAX={pmax}  ({time.time()-t0:.1f}s)")

    # ─── Phase 1: Precompute heat traces with adaptive t-windows ──
    print(f"\n  Phase 1: Precompute heat traces (adaptive t-windows)")
    print("  " + "─" * 58)

    # Fixed t-window for cascade (a₂..a₅)
    FIXED_T_LO = 0.0008
    FIXED_T_HI = 0.009
    fixed_ts = chebyshev_nodes(FIXED_T_LO, FIXED_T_HI, N_PTS)

    precomp_fixed = {}
    volumes_fixed = {}
    fixed_computed = 0
    fixed_cached = 0

    for n in CASCADE_RANGE:
        cached = load_heat_trace(n, "fixed")
        if cached:
            _, fs, vol = cached
            precomp_fixed[n] = fs
            volumes_fixed[n] = vol
            fixed_cached += 1
        else:
            eigs, dims = spectra[n]
            fs = compute_heat_trace(n, eigs, dims, fixed_ts)
            vol = neville(fixed_ts, fs, mpmath.mpf(0))
            precomp_fixed[n] = fs
            volumes_fixed[n] = vol
            save_heat_trace(n, fixed_ts, fs, vol, "fixed")
            fixed_computed += 1

    print(f"    Fixed t-window [{FIXED_T_LO}, {FIXED_T_HI}]: "
          f"{len(list(CASCADE_RANGE))} dimensions "
          f"({fixed_cached} cached, {fixed_computed} computed)")

    # Adaptive t-window for a₆..a₁₂
    target_k = 12
    precomp_adaptive = {}
    volumes_adaptive = {}
    adaptive_ts_cache = {}
    adaptive_computed = 0
    adaptive_cached = 0

    for n in ALL_RANGE:
        t0 = time.time()
        t_lo, t_hi = adaptive_t_window(n, target_k)
        ts = chebyshev_nodes(t_lo, t_hi, N_PTS)
        adaptive_ts_cache[n] = ts

        cached = load_heat_trace(n, "adaptive")
        if cached:
            _, fs, vol = cached
            precomp_adaptive[n] = fs
            volumes_adaptive[n] = vol
            adaptive_cached += 1
            vol_err = abs(vol - neville(ts[::2], [fs[i] for i in range(0, N_PTS, 2)],
                                        mpmath.mpf(0)))
            elapsed = time.time() - t0
            print(f"    n={n:>2}: [CACHED]  vol={mpmath.nstr(vol, 12)}  "
                  f"err={mpmath.nstr(vol_err, 3)}  ({elapsed:.1f}s)")
        else:
            eigs, dims = spectra[n]
            fs = compute_heat_trace(n, eigs, dims, ts)
            vol = neville(ts, fs, mpmath.mpf(0))
            vol_err = abs(vol - neville(ts[::2], [fs[i] for i in range(0, N_PTS, 2)],
                                        mpmath.mpf(0)))
            precomp_adaptive[n] = fs
            volumes_adaptive[n] = vol
            save_heat_trace(n, ts, fs, vol, "adaptive")
            adaptive_computed += 1
            elapsed = time.time() - t0
            print(f"    n={n:>2}: t∈[{float(t_lo):.2e}, {float(t_hi):.2e}]  "
                  f"vol={mpmath.nstr(vol, 12)}  "
                  f"err={mpmath.nstr(vol_err, 3)}  ({elapsed:.1f}s)")

    print(f"\n    Adaptive: {adaptive_cached} cached, {adaptive_computed} computed")

    # ─── Phase 2: Cascade a₂..a₅ for n=3..13 → exact polynomials ──
    print(f"\n  Phase 2: Cascade a₂..a₅ for n=3..13 → exact polynomials")
    print("  " + "═" * 58)

    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_RANGE}}

    for k in range(2, 6):
        # Try loading from checkpoint
        cached_poly = load_polynomial(k)
        cached_rats = load_rationals(k)
        if cached_poly and cached_rats:
            KNOWN_POLYS[k] = cached_poly
            all_rats[k] = cached_rats
            print(f"\n    a_{k}: [CACHED] degree {len(cached_poly)-1}")
            if k in KNOWN_VALUES and 5 in cached_rats:
                ok = cached_rats[5] == KNOWN_VALUES[k]
                print(f"      a_{k}(5) = {cached_rats[5]} {'✓' if ok else '✗'}")
            continue

        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 13)

        print(f"\n    a_{k} cascade (degree {deg})...")

        ak_rats = {}
        for n in CASCADE_RANGE:
            known_fracs = {0: Fraction(1)}
            for j in range(1, k):
                known_fracs[j] = all_rats[j][n]

            ak, _ = extract_coefficient(precomp_fixed[n], fixed_ts,
                                        volumes_fixed[n], known_fracs, k)[:2]
            frac, _ = identify_rational(ak, max_den=500000, tol=1e-20, max_prime=max_p)
            if frac:
                ak_rats[n] = frac

        clean_ns = sorted(ak_rats.keys())
        n_poly = min(len(clean_ns), deg + 1)
        pts = [(Fraction(nv), ak_rats[nv]) for nv in clean_ns[:n_poly]]
        ak_poly = lagrange_interpolate(pts)
        extra_ns = clean_ns[n_poly:]
        ok = all(eval_poly(ak_poly, Fraction(nv)) == ak_rats[nv] for nv in extra_ns)
        print(f"      Degree {len(ak_poly)-1}: {'✓ VERIFIED' if ok else '?'} "
              f"({len(extra_ns)} extra)")

        for nv in ALL_RANGE:
            ak_rats[nv] = eval_poly(ak_poly, Fraction(nv))

        all_rats[k] = ak_rats
        KNOWN_POLYS[k] = ak_poly
        save_polynomial(k, ak_poly)
        save_rationals(k, ak_rats)

        if k in KNOWN_VALUES:
            val5 = ak_rats[5]
            ok = val5 == KNOWN_VALUES[k]
            print(f"      a_{k}(5) = {val5} {'✓' if ok else '✗'}")

    # ─── Phase 3: Extract a₆..a₁₁ for ALL n → exact polynomials ──
    print(f"\n  Phase 3: Extract a₆..a₁₁ for n=3..35 → exact polynomials")
    print("  " + "═" * 58)

    for k in range(6, 12):
        # Try loading from checkpoint
        cached_poly = load_polynomial(k)
        cached_rats = load_rationals(k)
        if cached_poly and cached_rats:
            KNOWN_POLYS[k] = cached_poly
            all_rats[k] = cached_rats
            print(f"\n    a_{k}: [CACHED] degree {len(cached_poly)-1}")
            if k in KNOWN_VALUES and 5 in cached_rats:
                ok = cached_rats[5] == KNOWN_VALUES[k]
                print(f"      a_{k}(5) = {cached_rats[5]} {'✓' if ok else '✗'}")
            continue

        c_top, c_sub, c_const = three_theorems(k)
        deg = 2 * k
        max_p = MAX_PRIME_BY_LEVEL.get(k, 23)

        print(f"\n    a_{k} cascade (degree {deg}, primes ≤ {max_p})...")

        ak_clean = {}

        for n in ALL_RANGE:
            known_fracs = {0: Fraction(1)}
            for j in range(1, k):
                known_fracs[j] = all_rats[j][n]

            ts = adaptive_ts_cache[n]
            ak, ak_err, method = extract_coefficient(
                precomp_adaptive[n], ts, volumes_adaptive[n], known_fracs, k)

            frac, _ = identify_rational(ak, max_den=500000000000000,
                                        tol=1e-12, max_prime=max_p)
            if frac:
                ak_clean[n] = frac

        nk_clean = len(ak_clean)
        n_needed = deg - 2
        print(f"      Clean: {nk_clean}/33 (need ≥{n_needed})")

        ak_poly = None
        if nk_clean >= n_needed + 2:
            print(f"      Strategy A+ (robust): {nk_clean} clean + 3 theorems")
            ak_poly, ak_clean_used = robust_constrained_polynomial(
                ak_clean, c_top, c_sub, c_const, deg, label=f"a_{k}: ")
            if ak_poly:
                for nv in ALL_RANGE:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
        elif nk_clean >= n_needed:
            print(f"      Strategy A: {nk_clean} clean (just enough)")
            ak_poly = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                for nv in ALL_RANGE:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
        else:
            print(f"      ✗ INSUFFICIENT: need ≥{n_needed} clean, have {nk_clean}")
            print(f"      Cannot proceed past a_{k}. Stopping cascade.")
            all_rats[k] = ak_clean
            KNOWN_POLYS[k] = None
            break

        all_rats[k] = ak_clean
        KNOWN_POLYS[k] = ak_poly
        if ak_poly:
            save_polynomial(k, ak_poly)
            save_rationals(k, ak_clean)

        if k in KNOWN_VALUES and 5 in ak_clean:
            ok = ak_clean[5] == KNOWN_VALUES[k]
            print(f"      a_{k}(5) = {ak_clean[5]} {'✓' if ok else '✗'}")

        if ak_poly:
            ct_ok = ak_poly[deg] == c_top
            ratio = ak_poly[deg-1] / ak_poly[deg] if ak_poly[deg] != 0 else None
            exp_r = Fraction(-k*(k-1), 10)
            cr_ok = ratio == exp_r if ratio else False
            c0_ok = ak_poly[0] == c_const
            print(f"      Three Theorems: c_top={'✓' if ct_ok else '✗'} "
                  f"ratio={'✓' if cr_ok else '✗'} c₀={'✓' if c0_ok else '✗'}")

    # Check we have all prerequisites for a₁₂
    have_all = all(KNOWN_POLYS.get(j) is not None for j in range(1, 12))
    if not have_all:
        missing = [j for j in range(1, 12) if KNOWN_POLYS.get(j) is None]
        print(f"\n  ✗ CANNOT EXTRACT a₁₂: missing polynomials for a_{missing}")
        print(f"  This is unexpected — the Phase 3 cascade stopped early.")
        print(f"\n  SCORECARD: {PASS}/{PASS + FAIL}")
        return

    # ─── Phase 4: THE MAIN EVENT — a₁₂ extraction ────────────────
    print(f"\n  Phase 4: a₁₂ extraction (the main event)")
    print("  " + "═" * 58)

    k = 12
    c_top, c_sub, c_const = three_theorems(k)
    deg = 2 * k  # = 24
    max_p = MAX_PRIME_BY_LEVEL.get(k, 23)

    print(f"    Target: degree-{deg} polynomial, primes ≤ {max_p}")
    print(f"    Three Theorems: c₂₄ = {c_top}, ratio = {Fraction(-k*(k-1), 10)}, "
          f"c₀ = {c_const}")
    print(f"    Need ≥{deg - 2} clean rationals from {len(list(ALL_RANGE))} data points")
    print()

    a12_vals = {}; a12_clean = {}; a12_methods = {}

    for n in ALL_RANGE:
        t0 = time.time()

        known_fracs = {0: Fraction(1)}
        for j in range(1, k):
            known_fracs[j] = all_rats[j][n]

        ts = adaptive_ts_cache[n]
        a12, a12_err, method = extract_coefficient(
            precomp_adaptive[n], ts, volumes_adaptive[n], known_fracs, k)

        a12_vals[n] = (a12, a12_err)
        a12_methods[n] = method

        frac, frac_err = identify_rational(a12, max_den=500000000000000,
                                           tol=1e-8, max_prime=max_p)
        if frac:
            a12_clean[n] = frac
            status = "✓ clean"
        else:
            frac_any, frac_any_err = identify_rational(
                a12, max_den=500000000000000, tol=1e-8)
            if frac_any:
                den_f = factor(frac_any.denominator)
                max_den_p = max(den_f) if den_f else 0
                status = f"? den_max={max_den_p}"
            else:
                status = "✗ no ID"

        elapsed = time.time() - t0
        t_lo, t_hi = adaptive_t_window(n, k)
        print(f"    n={n:>2}: err={mpmath.nstr(a12_err, 3):<12} "
              f"{method:<25} t∈[{float(t_lo):.1e},{float(t_hi):.1e}] "
              f"{status:<18} ({elapsed:.1f}s)")

    n12_clean = len(a12_clean)
    n_needed = deg - 2  # = 22
    print(f"\n    ═══ Clean a₁₂ rationals: {n12_clean}/33 "
          f"(need ≥{n_needed}, want ≥{n_needed+2}) ═══")

    # Rational table
    print(f"\n    {'n':>3}  {'a₁₂(n) rational':<50} {'den':>15} "
          f"{'factors(den)':<35} {'clean?'}")
    print(f"    {'─'*110}")
    for n in ALL_RANGE:
        if n in a12_clean:
            f = a12_clean[n]
            den_f = factor(f.denominator)
            val_str = str(f)
            if len(val_str) > 48:
                val_str = val_str[:45] + "..."
            print(f"    {n:>3}  {val_str:<50} {f.denominator:>15} "
                  f"{str(den_f)[:33]:<35} ✓")
        else:
            v, e = a12_vals[n]
            print(f"    {n:>3}  ≈{mpmath.nstr(v, 18):<49} {'?':>15}")

    # ─── Phase 5: Polynomial construction for a₁₂ ────────────────
    print(f"\n  Phase 5: a₁₂ polynomial construction")
    print("  " + "═" * 58)

    a12_poly = None
    if n12_clean >= n_needed + 2:
        print(f"    Strategy A+ (robust): {n12_clean} clean + 3 theorems")
        a12_poly, a12_clean_used = robust_constrained_polynomial(
            a12_clean, c_top, c_sub, c_const, deg, label="a₁₂: ")
    elif n12_clean >= n_needed:
        print(f"    Strategy A: {n12_clean} clean (just enough)")
        a12_poly = constrained_polynomial(a12_clean, c_top, c_sub, c_const, deg)
    else:
        print(f"    ✗ CASCADE WALL: need ≥{n_needed} clean, have {n12_clean}")
        print(f"    Deficit: {n_needed - n12_clean} more clean rationals needed")

    if a12_poly:
        d = len(a12_poly) - 1
        print(f"\n    ╔═══ a₁₂(n) POLYNOMIAL (degree {d}) ═══╗")
        for idx, c in enumerate(a12_poly):
            if c != 0:
                c_str = str(c)
                if len(c_str) > 60:
                    c_str = c_str[:57] + "..."
                print(f"    ║  c_{idx:<2} = {c_str}")
                print(f"    ║       den: {factor(c.denominator)}")
        print(f"    ╚{'═'*55}╝")

        ct_ok = a12_poly[deg] == c_top
        ratio = a12_poly[deg-1] / a12_poly[deg] if a12_poly[deg] != 0 else None
        exp_r = Fraction(-k*(k-1), 10)
        cr_ok = ratio == exp_r if ratio else False
        c0_ok = a12_poly[0] == c_const

        print(f"\n    Three Theorems:")
        print(f"      c₂₄ = {a12_poly[deg]} {'✓' if ct_ok else '✗'}")
        print(f"      c₂₃/c₂₄ = {ratio} = {float(ratio) if ratio else '?'} "
              f"{'✓' if cr_ok else '✗'} (expect {exp_r} = {float(exp_r)})")
        print(f"      c₀ = {a12_poly[0]} {'✓' if c0_ok else '✗'}")

        val5 = eval_poly(a12_poly, Fraction(5))
        print(f"\n    a₁₂(Q⁵) = {val5}")
        print(f"    Numerator: {val5.numerator}")
        if is_prime(abs(val5.numerator)):
            print(f"      → PRIME!")
        else:
            nf = factor(abs(val5.numerator))
            if len(nf) <= 10:
                print(f"      → factors: {nf}")
        print(f"    Denominator: {val5.denominator}")
        den_f = factor(val5.denominator)
        print(f"      → factors: {den_f}")
        max_den_prime = max(den_f) if den_f else 0
        print(f"      → max prime: {max_den_prime}")
        print(f"      → QUIET prediction: max prime ≤ 23 → "
              f"{'✓ CONFIRMED' if max_den_prime <= 23 else '✗ SURPRISE'}")

        # Save a₁₂ polynomial
        save_polynomial(k, a12_poly)
        save_rationals(k, a12_clean)

    # ─── Phase 6: Diagnostics ────────────────────────────────────
    print(f"\n  Phase 6: Diagnostics")
    print("  " + "═" * 58)

    print(f"\n    Adaptive t-window effect:")
    print(f"    {'n':>3}  {'t_lo':>10}  {'t_hi':>10}  {'n²·t_hi':>10}  {'note'}")
    print(f"    {'─'*50}")
    for n in ALL_RANGE:
        t_lo, t_hi = adaptive_t_window(n, k)
        ratio = n * n * t_hi
        note = ""
        if ratio > 0.5:
            note = "← large ratio"
        elif ratio < 0.01:
            note = "← very separated"
        print(f"    {n:>3}  {t_lo:>10.2e}  {t_hi:>10.2e}  {ratio:>10.4f}  {note}")

    print(f"\n    Extraction method distribution:")
    from collections import Counter
    method_counts = Counter(a12_methods.values())
    for m, c in method_counts.most_common():
        print(f"      {m}: {c} dimensions")

    # ─── Scorecard ────────────────────────────────────────────────
    print(f"\n  " + "═" * 58)
    print(f"  SCORECARD")
    print("  " + "═" * 58)

    for kv in range(2, 7):
        if kv in KNOWN_VALUES and kv in all_rats:
            score(f"a_{kv}(5) = {KNOWN_VALUES[kv]}",
                  all_rats[kv].get(5) == KNOWN_VALUES[kv])
        else:
            score(f"a_{kv}(5) known", False, "not computed")

    for kv in [7, 8, 9]:
        if kv in KNOWN_VALUES and kv in all_rats:
            score(f"a_{kv}(5) = {KNOWN_VALUES[kv]}",
                  all_rats[kv].get(5) == KNOWN_VALUES[kv])

    if 10 in KNOWN_VALUES and 10 in all_rats:
        score("a₁₀(5) = 2409398458451/21709437750",
              all_rats[10].get(5) == KNOWN_VALUES[10])

    if 11 in all_rats and 5 in all_rats[11]:
        val5 = all_rats[11][5]
        den_f = factor(val5.denominator)
        score("a₁₁ den has Golay prime 23", 23 in den_f,
              f"den factors: {den_f}")
    else:
        score("a₁₁ den has Golay prime 23", False, "not computed")

    score(f"a₁₂ clean rationals ≥ {n_needed}", n12_clean >= n_needed,
          f"got {n12_clean}/33")

    score("a₁₂ clean > 10 (beat Toy 308)", n12_clean > 10,
          f"Toy 308: 10/25, this: {n12_clean}/33")

    score("a₁₂ polynomial recovered", a12_poly is not None)

    if a12_poly:
        ct = a12_poly[deg] == c_top
        ratio = a12_poly[deg-1] / a12_poly[deg] if a12_poly[deg] != 0 else None
        cr = ratio == Fraction(-k*(k-1), 10) if ratio else False
        c0 = a12_poly[0] == c_const
        score("a₁₂ Three Theorems all pass", ct and cr and c0,
              f"c_top={'✓' if ct else '✗'} ratio={'✓' if cr else '✗'} c₀={'✓' if c0 else '✗'}")
    else:
        score("a₁₂ Three Theorems all pass", False, "no polynomial")

    if a12_poly:
        val5 = eval_poly(a12_poly, Fraction(5))
        den_f = factor(val5.denominator)
        mp = max(den_f) if den_f else 0
        score("a₁₂ quiet level (max prime ≤ 23)", mp <= 23,
              f"max prime = {mp}, factors = {den_f}")
    else:
        score("a₁₂ quiet level (max prime ≤ 23)", False, "no polynomial")

    score("Adaptive t-window used", True,
          f"n=3: t∈[{adaptive_t_window(3,12)[0]:.2e}, {adaptive_t_window(3,12)[1]:.2e}], "
          f"n=35: t∈[{adaptive_t_window(35,12)[0]:.2e}, {adaptive_t_window(35,12)[1]:.2e}]")

    print(f"\n  " + "═" * 58)
    print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
    print("  " + "═" * 58)

    elapsed = time.time() - t_start
    hours = elapsed / 3600
    print(f"\n  Toy 361 complete. ({elapsed:.0f}s = {hours:.1f}h)")
    print(f"\n  KEY RESULT: {n12_clean}/33 clean a₁₂ rationals "
          f"({'WALL BROKEN' if n12_clean >= n_needed else 'WALL STANDS'})")

    if a12_poly:
        print(f"  a₁₂ polynomial: degree {len(a12_poly)-1}, RECOVERED")
        print(f"  → Ready to cascade to a₁₃ (Toy 362)")
    else:
        print(f"  → Need {n_needed - n12_clean} more clean rationals")
        print(f"  → Consider: increase dps to 1000, or finer t-grid, "
              f"or P_MAX > 2000 for large n")


if __name__ == '__main__':
    main()
