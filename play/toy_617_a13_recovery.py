#!/usr/bin/env python3
"""
Toy 617 — a₁₃ Polynomial Recovery: Push to Eight Consecutive Levels
====================================================================
Extends Toy 612's pipeline to recover the 13th Seeley-DeWitt coefficient
a₁₃(n) as a polynomial in n of degree 26.

Key parameters:
  - Degree 26, Three Theorems constrained → 24 unknowns
  - 33 checkpoint dimensions (n=3..35) → 9 verification points
  - QUIET predicted: 2k+1 = 27 = 3³ (not prime), max prime ≤ 23
  - c_top = 1/(3¹³ · 13!), ratio = -78/5, c_const = -1/(2·13!)

Pipeline (from Toy 612):
  1. Load Toy 361 checkpoints (dps=800, n=3..35)
  2. Cascade a₁..a₁₂ (exact polynomials, all verified)
  3. Extract a₁₃ numerical values at each dimension
  4. Rational identification (prime ≤ 23 constraint)
  5. Denominator boosting for marginal values
  6. Modular Newton + CRT polynomial recovery
  7. Validate: Three Theorems + cross-validation + prime migration

If successful: EIGHT consecutive levels (k=6..13) with exact polynomials,
all confirming Three Theorems, column rule, and VSC prime structure.

Elie — March 30, 2026

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
# CHECKPOINT I/O (from Toy 361)
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


# ═══════════════════════════════════════════════════════════════════
# SPECTRUM BUILDER (from Toy 361)
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
    return 2000


# ═══════════════════════════════════════════════════════════════════
# HEAT TRACE & EXTRACTION
# ═══════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════
# POLYNOMIAL UTILITIES
# ═══════════════════════════════════════════════════════════════════

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


def three_theorems(k):
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const


def constrained_polynomial(clean_rats, c_top, c_subtop, c_const, deg):
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
# MODULAR NEWTON + CRT (from Toy 463/612)
# ═══════════════════════════════════════════════════════════════════

def mod_inverse(a, p):
    if a < 0:
        a = a % p
    g, x, _ = _extended_gcd(a, p)
    if g != 1:
        raise ValueError(f"No inverse: gcd({a}, {p}) = {g}")
    return x % p


def _extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def newton_interpolate_mod(points, p):
    n = len(points)
    xs = [int(pt[0]) % p for pt in points]
    ys = [int(pt[1]) % p for pt in points]
    dd = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff = (xs[i] - xs[i - j]) % p
            dd[i] = ((dd[i] - dd[i - 1]) * mod_inverse(diff, p)) % p
    coeffs = [0] * n
    coeffs[0] = dd[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, 0, -1):
            coeffs[j] = (coeffs[j - 1] - xs[i] * coeffs[j]) % p
        coeffs[0] = (dd[i] - xs[i] * coeffs[0]) % p
    return [c % p for c in coeffs]


CRT_PRIMES = [
    2**127 - 1,     # Mersenne prime M127
    2**107 - 1,     # Mersenne prime M107
    2**89 - 1,      # Mersenne prime M89
    2**61 - 1,      # Mersenne prime M61
    2**61 + 15,     # verified prime
    2**59 - 55,
    2**59 + 131,    # verified prime
    2**57 - 13,
    2**53 - 111,
    2**47 - 115,
    2**43 - 57,
    2**41 - 21,
    2**37 - 25,
    2**31 - 1,      # Mersenne prime M31
    2**29 - 3,
]


def crt_reconstruct(residues, primes):
    x = residues[0]
    m = primes[0]
    for i in range(1, len(residues)):
        r_i = residues[i]
        p_i = primes[i]
        diff = (r_i - x) % p_i
        m_inv = pow(m, p_i - 2, p_i)
        t = (diff * m_inv) % p_i
        x = x + m * t
        m = m * p_i
    return x % m, m


def crt_to_signed(x, modulus):
    if x > modulus // 2:
        return x - modulus
    return x


# ═══════════════════════════════════════════════════════════════════
# CONSTRAINED MODULAR POLYNOMIAL RECOVERY (from Toy 612)
# ═══════════════════════════════════════════════════════════════════

def constrained_modular_polynomial(clean_rats, c_top, c_subtop, c_const, deg):
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2
    if len(clean_ns) < n_needed:
        return None, f"Need {n_needed}, have {len(clean_ns)}"

    residual_rats = {}
    for nv in clean_ns:
        res = clean_rats[nv] - c_top * Fraction(nv)**deg \
              - c_subtop * Fraction(nv)**(deg-1) - c_const
        residual_rats[nv] = res / Fraction(nv)

    D = 1
    for v in residual_rats.values():
        D = D * v.denominator // gcd(D, v.denominator)

    print(f"      Residual lcm(den) D has {len(str(D))} digits")

    int_vals = {}
    for nv in clean_ns:
        iv = int(residual_rats[nv] * D)
        assert Fraction(iv, D) == residual_rats[nv], \
            f"Scaling error at n={nv}"
        int_vals[nv] = iv

    max_abs = max(abs(v) for v in int_vals.values())
    needed_bits = max_abs.bit_length() + 2
    cum_bits = 0
    n_primes = 0
    for p in CRT_PRIMES:
        cum_bits += p.bit_length()
        n_primes += 1
        if cum_bits > needed_bits:
            break

    if n_primes > len(CRT_PRIMES):
        return None, f"Need more CRT primes ({needed_bits} bits needed)"

    primes_used = CRT_PRIMES[:n_primes]
    print(f"      Max |D*R(n)/n| ~ 2^{max_abs.bit_length()}")
    print(f"      Using {n_primes} CRT primes ({cum_bits} bits)")

    use_ns = clean_ns[:n_needed]
    extra_ns = clean_ns[n_needed:]

    mod_images = []
    for p in primes_used:
        pts = [(nv, int_vals[nv] % p) for nv in use_ns]
        mc = newton_interpolate_mod(pts, p)
        mod_images.append(mc)

    rec_int_coeffs = []
    for j in range(n_needed):
        residues = [img[j] if j < len(img) else 0 for img in mod_images]
        raw, modulus = crt_reconstruct(residues, primes_used)
        signed = crt_to_signed(raw, modulus)
        rec_int_coeffs.append(signed)

    red_rats = [Fraction(c, D) for c in rec_int_coeffs]

    n_verified = 0
    n_failed = 0
    for nv in extra_ns:
        pred = sum(red_rats[j] * Fraction(nv)**j for j in range(len(red_rats)))
        if pred == residual_rats[nv]:
            n_verified += 1
        else:
            n_failed += 1

    if extra_ns:
        print(f"      Verification: {n_verified}/{n_verified + n_failed} "
              f"extra points match")

    if n_failed > 0:
        print(f"      {n_failed} extra point(s) failed — may have bad values")

    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(red_rats):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()

    return poly, "OK"


def denominator_boost(ak_mpf_vals, clean_rats, max_prime=23):
    if not clean_rats:
        return clean_rats

    D = 1
    for v in clean_rats.values():
        D = D * v.denominator // gcd(D, v.denominator)

    print(f"    Denominator boost: D = lcm of {len(clean_rats)} clean denoms")
    print(f"      D has {len(str(D))} digits, max prime = {max(factor(D))}")

    boosted = dict(clean_rats)
    n_boosted = 0

    for n, (ak_mpf, ak_err) in sorted(ak_mpf_vals.items()):
        if n in boosted:
            continue

        D_ak = mpmath.mpf(D) * ak_mpf
        nearest_int = int(mpmath.nint(D_ak))
        residual = abs(D_ak - mpmath.mpf(nearest_int))

        tol = min(mpmath.mpf('0.01'), abs(ak_err) * mpmath.mpf(D) * 100)

        if residual < tol:
            candidate = Fraction(nearest_int, D)
            den_f = factor(candidate.denominator)
            max_den_p = max(den_f) if den_f else 0
            if max_den_p <= max_prime:
                boosted[n] = candidate
                n_boosted += 1
                print(f"      n={n}: BOOSTED (residual={float(residual):.2e})")
            else:
                print(f"      n={n}: boosted but den max prime={max_den_p} > {max_prime}")
        else:
            print(f"      n={n}: residual={float(residual):.2e} too large")

    print(f"    Boosted {n_boosted} additional → {len(boosted)} total clean")
    return boosted


# ═══════════════════════════════════════════════════════════════════
# KNOWN DATA
# ═══════════════════════════════════════════════════════════════════

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]

# Known a_k(5) values: k=1..12
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
}

MAX_PRIME_BY_LEVEL = {
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23, 12: 23, 13: 23,
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
    print("║  Toy 617 — a₁₃ Polynomial Recovery                            ║")
    print("║  Eight Consecutive Levels: k=6..13                             ║")
    print("║  QUIET predicted (27=3³, max prime ≤ 23)                       ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    # Check checkpoint availability
    CASCADE_RANGE = range(3, 14)
    avail_fixed = sum(1 for n in CASCADE_RANGE
                      if os.path.exists(os.path.join(CKPT_DIR,
                                                      f"fixed_heat_n{n:02d}.json")))
    ALL_RANGE = []
    for n in range(3, 36):
        if os.path.exists(os.path.join(CKPT_DIR, f"adaptive_heat_n{n:02d}.json")):
            ALL_RANGE.append(n)

    print(f"\n  Checkpoints: {avail_fixed} fixed (n=3..13), "
          f"{len(ALL_RANGE)} adaptive (n={ALL_RANGE[0]}..{ALL_RANGE[-1]})")

    TARGET_K = 13
    TARGET_DEG = 2 * TARGET_K  # 26
    N_NEEDED = TARGET_DEG - 2  # 24

    print(f"  Target: a_{TARGET_K}, degree {TARGET_DEG}, "
          f"need ≥{N_NEEDED} clean points")
    print(f"  Available: {len(ALL_RANGE)} dimensions")

    if len(ALL_RANGE) < N_NEEDED:
        print(f"  ✗ Insufficient data — need {N_NEEDED}, have {len(ALL_RANGE)}")
        return

    # ─── Section 1: Load checkpoints ───────────────────────────────
    print(f"\n─── Section 1: Loading Checkpoints ───")

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

    print(f"  Loaded: {len(fixed_data)} fixed, {len(adaptive_data)} adaptive")

    # Compute missing adaptive traces
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
            print(f"    n={n}: computed (P_MAX={pmax})")

    # ─── Section 2: Cascade a₂..a₁₂ ───────────────────────────────
    print(f"\n─── Section 2: Cascade a₂..a₁₂ (exact polynomials) ───")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_RANGE}}

    # Phase A: a₂..a₅ from fixed-window traces (n=3..13)
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
        print(f"  a_{k}: degree {len(ak_poly)-1}, "
              f"{len(clean_ns)} clean, "
              f"a_{k}(5)={'✓' if v5_ok else '✗'}")

    # Phase B: a₆..a₁₂ from adaptive traces
    for k in range(6, TARGET_K):
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
        print(f"  a_{k:>2}: {n_clean}/{len(ALL_RANGE)} clean (need {n_need}), "
              f"{poly_status}, a_{k}(5)={'✓' if v5_ok else '✗'}")

    # Check prerequisites
    have_all = all(KNOWN_POLYS.get(j) is not None for j in range(1, TARGET_K))
    if not have_all:
        missing = [j for j in range(1, TARGET_K) if KNOWN_POLYS.get(j) is None]
        print(f"\n  ✗ CANNOT EXTRACT a_{TARGET_K}: missing polynomials for {missing}")
        return

    score("Cascade a₂..a₁₂ complete", True,
          f"All {TARGET_K - 1} polynomials recovered")

    # Verify known values
    all_v5_ok = True
    for k in range(1, TARGET_K):
        if k in KNOWN_AK5:
            v5 = all_rats[k].get(5)
            if v5 != KNOWN_AK5[k]:
                all_v5_ok = False
    score(f"All a_k(5) match known values (k=1..{TARGET_K-1})", all_v5_ok)

    # ─── Section 3: Extract a₁₃ values ────────────────────────────
    print(f"\n─── Section 3: Extract a_{TARGET_K} Numerical Values ───")

    k = TARGET_K
    c_top, c_sub, c_const = three_theorems(k)
    deg = TARGET_DEG
    max_p = MAX_PRIME_BY_LEVEL.get(k, 23)

    ak_mpf = {}
    ak_clean = {}
    ak_any = {}

    for n in ALL_RANGE:
        if n not in adaptive_data:
            continue
        fs, vol = adaptive_data[n]
        ts = adaptive_ts[n]

        known_fracs = {0: Fraction(1)}
        for j in range(1, k):
            known_fracs[j] = all_rats[j][n]

        a_val, a_err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
        ak_mpf[n] = (a_val, a_err)

        # Prime-constrained identification
        frac, _ = identify_rational(a_val, max_den=500000000000000,
                                    tol=1e-8, max_prime=max_p)
        if frac:
            ak_clean[n] = frac

        # Unconstrained for diagnostics
        frac_any, _ = identify_rational(a_val, max_den=500000000000000, tol=1e-8)
        if frac_any:
            ak_any[n] = frac_any

        if frac:
            status = "✓ clean"
        elif frac_any:
            den_f = factor(frac_any.denominator)
            status = f"? max_p={max(den_f)}"
        else:
            status = f"✗ err={float(a_err):.1e}"
        print(f"    n={n:>2}: {method:<25} {status}")

    n_clean = len(ak_clean)
    n_any = len(ak_any)

    # Classify extraction quality
    high_quality = []
    medium_quality = []
    low_quality = []
    for n, (val, err) in sorted(ak_mpf.items()):
        abs_err = float(abs(err))
        if abs_err < 1.0:
            high_quality.append(n)
        elif abs_err < 1e10:
            medium_quality.append(n)
        else:
            low_quality.append(n)

    print(f"\n  Extraction quality:")
    if high_quality:
        print(f"    High (err<1):      {len(high_quality)} dims: "
              f"n={high_quality[0]}..{high_quality[-1]}")
    if medium_quality:
        print(f"    Medium (err<10¹⁰): {len(medium_quality)} dims: "
              f"{medium_quality}")
    if low_quality:
        print(f"    Low (err≥10¹⁰):    {len(low_quality)} dims: "
              f"n={low_quality[0]}..{low_quality[-1]}")

    print(f"\n  Initial: {n_clean} clean (prime≤{max_p}), {n_any} unconstrained, "
          f"need ≥{N_NEEDED}")

    # Trust only high+medium quality
    ak_trustworthy = {n: v for n, v in ak_clean.items()
                      if n in high_quality or n in medium_quality}
    n_trustworthy = len(ak_trustworthy)
    print(f"  Trustworthy clean: {n_trustworthy}")

    score(f"Initial a_{TARGET_K} clean ≥ 10", n_clean >= 10,
          f"got {n_clean} ({n_trustworthy} trustworthy)")

    # ─── Section 4: Denominator Boosting ───────────────────────────
    print(f"\n─── Section 4: Denominator Boosting ───")

    if n_trustworthy < N_NEEDED and n_trustworthy >= 5:
        print(f"  Boosting from trustworthy set ({n_trustworthy} points)...")
        ak_boosted_trust = denominator_boost(ak_mpf, ak_trustworthy, max_prime=max_p)
    else:
        ak_boosted_trust = dict(ak_trustworthy)

    if n_clean < N_NEEDED and n_clean >= 5:
        ak_boosted = denominator_boost(ak_mpf, ak_clean, max_prime=max_p)
    else:
        ak_boosted = dict(ak_clean)

    n_boosted = len(ak_boosted)
    n_boosted_trust = len(ak_boosted_trust)
    print(f"\n  After boosting: {n_boosted} total, {n_boosted_trust} trustworthy")

    score(f"a_{TARGET_K} clean rationals ≥ {N_NEEDED}", n_boosted >= N_NEEDED,
          f"got {n_boosted}/{len(ALL_RANGE)} ({n_boosted_trust} trustworthy)")

    # ─── Section 5: Polynomial Recovery ────────────────────────────
    print(f"\n─── Section 5: a_{TARGET_K} Polynomial Recovery ───")

    ak_poly = None
    ak_poly_trust = None

    # Strategy A: Fraction Lagrange on full set
    if n_boosted >= N_NEEDED:
        print(f"\n  Strategy A: Fraction Lagrange ({n_boosted} points, "
              f"degree {deg}, need {N_NEEDED})")
        t0 = time.time()
        ak_poly = constrained_polynomial(
            ak_boosted, c_top, c_sub, c_const, deg)
        dt = time.time() - t0
        if ak_poly:
            print(f"    → SUCCESS ({dt:.1f}s)")
        else:
            print(f"    → FAILED ({dt:.1f}s)")

    # Strategy B: Modular Newton + CRT
    if n_boosted >= N_NEEDED:
        print(f"\n  Strategy B: Modular Newton + CRT ({n_boosted} points)")
        ak_poly_crt, msg = constrained_modular_polynomial(
            ak_boosted, c_top, c_sub, c_const, deg)
        if ak_poly_crt:
            print(f"    → SUCCESS")
            if ak_poly:
                agree = (ak_poly == ak_poly_crt)
                print(f"    → Agrees with Strategy A: {'✓ YES' if agree else '✗ NO'}")
                if agree:
                    print(f"    → CROSS-VALIDATED")
        else:
            print(f"    → {msg}")

    # Strategy C: Trustworthy-only set
    if n_boosted_trust >= N_NEEDED:
        print(f"\n  Strategy C: Trustworthy-only ({n_boosted_trust} points)")
        t0 = time.time()
        ak_poly_trust = constrained_polynomial(
            ak_boosted_trust, c_top, c_sub, c_const, deg)
        dt = time.time() - t0
        if ak_poly_trust:
            print(f"    → SUCCESS ({dt:.1f}s)")
            if ak_poly:
                agree = (ak_poly == ak_poly_trust)
                print(f"    → Agrees with full-set: {'✓ YES' if agree else '✗ NO'}")
                if agree:
                    print(f"    → STRONG: trustworthy subset recovers same polynomial")
                else:
                    print(f"    → DIVERGENCE — trusting trustworthy set")
                    ak_poly = ak_poly_trust
        else:
            print(f"    → FAILED ({dt:.1f}s)")
    elif n_boosted_trust > 0:
        print(f"\n  Strategy C: Trustworthy set has {n_boosted_trust} points "
              f"(need {N_NEEDED}) — skipped")

    if ak_poly is None:
        print(f"\n  ✗ ALL STRATEGIES FAILED")
        print(f"  Available: {n_boosted} total, {n_boosted_trust} trustworthy")
        print(f"  Need: {N_NEEDED}")
        print(f"\n  This may mean:")
        print(f"    - dps=800 is insufficient for k={TARGET_K} extraction")
        print(f"    - Need recomputed checkpoints with higher dps")
        print(f"    - Or fewer clean dims than expected at this depth")

    score(f"a_{TARGET_K} polynomial recovered", ak_poly is not None)

    # ─── Section 6: Validation ─────────────────────────────────────
    print(f"\n─── Section 6: Validation ───")

    if ak_poly:
        d = len(ak_poly) - 1
        print(f"\n  a_{TARGET_K}(n) polynomial: degree {d}")

        n_nonzero = sum(1 for c in ak_poly if c != 0)
        print(f"  Non-zero coefficients: {n_nonzero}/{d+1}")
        for idx, c in enumerate(ak_poly):
            if c != 0:
                c_str = str(c)
                if len(c_str) > 65:
                    c_str = c_str[:62] + "..."
                print(f"    c_{idx:<2} = {c_str}")

        # Three Theorems
        ct_ok = ak_poly[deg] == c_top
        ratio = ak_poly[deg-1] / ak_poly[deg] if ak_poly[deg] != 0 else None
        exp_r = Fraction(-k*(k-1), 10)
        cr_ok = ratio == exp_r if ratio else False
        c0_ok = ak_poly[0] == c_const

        print(f"\n  Three Theorems:")
        print(f"    c_{deg} = {c_top}")
        print(f"    c_{deg} check: {'✓' if ct_ok else '✗'}")
        print(f"    c_{deg-1}/c_{deg} = {ratio} (expect {exp_r} = {float(exp_r):.1f})")
        print(f"    ratio check: {'✓' if cr_ok else '✗'}")
        print(f"    c₀ = {ak_poly[0]} (expect {c_const})")
        print(f"    c₀ check: {'✓' if c0_ok else '✗'}")

        score("Three Theorems all pass", ct_ok and cr_ok and c0_ok,
              f"c_top={'✓' if ct_ok else '✗'} "
              f"ratio={'✓' if cr_ok else '✗'} "
              f"c₀={'✓' if c0_ok else '✗'}")

        # a₁₃(5)
        val5 = eval_poly(ak_poly, Fraction(5))
        print(f"\n  a_{TARGET_K}(5) = a_{TARGET_K}(Q⁵):")
        print(f"    = {val5}")
        print(f"    Numerator: {val5.numerator}")
        print(f"    Denominator: {val5.denominator}")

        num_f = factor(abs(val5.numerator))
        den_f = factor(val5.denominator)
        max_num_p = max(num_f) if num_f else 0
        max_den_p = max(den_f) if den_f else 0

        if len(num_f) <= 15:
            print(f"    Numerator factors: {num_f}")
        else:
            print(f"    Numerator: {len(num_f)} prime factors, max = {max_num_p}")

        print(f"    Denominator factors: {den_f}")
        print(f"    Denominator max prime: {max_den_p}")

        quiet = max_den_p <= 23
        print(f"\n  QUIET level prediction (max prime ≤ 23):")
        print(f"    → {'✓ CONFIRMED' if quiet else '✗ SURPRISE'} "
              f"(max prime = {max_den_p})")

        score(f"a_{TARGET_K} QUIET level (max prime ≤ 23)", quiet,
              f"max prime in den = {max_den_p}")

        # Verify polynomial at all clean points
        n_poly_ok = 0
        n_poly_fail = 0
        for nv in sorted(ak_boosted.keys()):
            pred = eval_poly(ak_poly, Fraction(nv))
            if pred == ak_boosted[nv]:
                n_poly_ok += 1
            else:
                n_poly_fail += 1
                print(f"    ✗ Poly mismatch at n={nv}")

        score("Polynomial matches all clean points",
              n_poly_fail == 0,
              f"{n_poly_ok}/{n_poly_ok + n_poly_fail}")

        # Prime migration summary: k=6..13
        print(f"\n  Prime migration through Seeley-DeWitt levels:")
        for kk in range(6, TARGET_K + 1):
            v5 = all_rats.get(kk, {}).get(5)
            if v5 is None and kk == TARGET_K:
                v5 = val5
            if v5 is not None:
                df = factor(v5.denominator)
                mp = max(df) if df else 0
                entry = "NEW →" if (kk == 8 and 17 in df) or \
                                   (kk == 9 and 19 in df) or \
                                   (kk == 11 and 23 in df) else "     "
                if kk == TARGET_K:
                    entry = "★ NEW" if mp > 23 else "QUIET"
                print(f"    a_{kk:>2}(5): den max prime = {mp:>2}  {entry}  "
                      f"den = {v5.denominator}")

        # VSC analysis for k=13
        print(f"\n  Von Staudt-Clausen analysis for k={TARGET_K}:")
        print(f"    2k = {2*TARGET_K}")
        vsc_primes = [p for p in [2,3,5,7,11,13,17,19,23,29] if (2*TARGET_K) % (p-1) == 0]
        print(f"    VSC primes ((p-1)|2k): {vsc_primes}")
        cumulative_vsc = sorted(set(p for kk in range(1, TARGET_K+1)
                                    for p in [2,3,5,7,11,13,17,19,23,29]
                                    if (2*kk) % (p-1) == 0))
        print(f"    Cumulative VSC through k={TARGET_K}: {cumulative_vsc}")

    else:
        print(f"  No polynomial to validate.")

    # ─── Section 7: Error diagnostics ─────────────────────────────
    print(f"\n─── Section 7: Extraction Error Diagnostics ───")

    print(f"\n  Error distribution by dimension:")
    for n in sorted(ak_mpf.keys()):
        _, err = ak_mpf[n]
        status = "✓" if n in ak_boosted else ("~" if n in ak_any else "✗")
        log_err = float(mpmath.log10(abs(err) + 1e-800))
        bar = "█" * max(1, min(50, int(-log_err)))
        print(f"    n={n:>2}: {status} err~10^{log_err:+.0f} {bar}")

    # ─── Scorecard ─────────────────────────────────────────────────
    elapsed = time.time() - t_start

    print(f"\n{'═' * 64}")
    print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
    print(f"{'═' * 64}")

    if ak_poly:
        print(f"\n  KEY RESULT: a_{TARGET_K} polynomial RECOVERED (degree {len(ak_poly)-1})")
        print(f"  EIGHT consecutive levels (k=6..13) now exact.")
    else:
        print(f"\n  KEY RESULT: a_{TARGET_K} polynomial NOT recovered")
        print(f"  Clean rationals: {n_boosted}/{len(ALL_RANGE)} (need {N_NEEDED})")

    print(f"  Runtime: {elapsed:.0f}s ({elapsed/60:.1f}min)")

    if FAIL == 0:
        print(f"\n  ALL PASS — a_{TARGET_K} via modular Newton + CRT.")
    else:
        print(f"\n  {FAIL} failures — see above for details.")


if __name__ == '__main__':
    main()
