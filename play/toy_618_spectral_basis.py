#!/usr/bin/env python3
"""
Toy 618 — Spectral Basis Decomposition: The Geometry's Own Codebook
====================================================================
Test whether expressing a_k(n) interior coefficients in the Weyl
dimension basis d(p,q,n) of SO(n+2) produces cleaner arithmetic
than monomial, Newton, or Pochhammer bases.

The hypothesis (T539, Matched Codebook Principle):
  The right polynomial basis for heat kernel coefficients comes FROM
  the geometry. The Weyl dimension polynomials d(p,q,n) are the
  natural spectral basis because a_k(n) IS a sum over representations:

    a_k(n) = Σ_{(p,q)} α_{k,p,q} · d(p,q,n)

  If the spectral coefficients α_{k,p,q} have smaller denominator
  primes than the monomial coefficients, the codebook is matched.

Method:
  1. Compute d(p,q,n) for (p,q) pairs up to total weight ~k
  2. Evaluate as polynomials in n at enough points (n=3..35)
  3. Recover d(p,q,n) as exact rational polynomials
  4. Express a_k(n) = Σ α_{p,q} · d(p,q,n) by solving linear system
  5. Compare denominator primes of α_{p,q} vs monomial coefficients

Key prediction:
  If this works, the speaking pairs (-N_c, -n_C, etc.) should emerge
  as specific α_{p,q} coefficients — the gauge hierarchy IS the
  spectral decomposition.

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
import time
from fractions import Fraction
from math import gcd, factorial

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS = 0
FAIL = 0

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
# SECTION 1: Weyl Dimension Polynomials d(p,q,n)
# ═══════════════════════════════════════════════════════════════════

print("╔══════════════════════════════════════════════════════════════════╗")
print("║  Toy 618 — Spectral Basis: The Geometry's Own Codebook         ║")
print("║  Weyl dimension decomposition of heat kernel coefficients      ║")
print("╚══════════════════════════════════════════════════════════════════╝")

print(f"\n─── Section 1: Building Weyl Dimension Polynomials ───")


def _dim_B(p, q, r):
    """Dimension of SO(2r+1) irrep with highest weight (p,q,0,...,0)."""
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
    """Dimension of SO(2r) irrep with highest weight (p,q,0,...,0)."""
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
    """Dimension of SO(N) irrep with highest weight (p,q,0,...,0)."""
    if N < 5: return 0  # Need rank ≥ 2
    return _dim_B(p, q, (N - 1) // 2) if N % 2 == 1 else _dim_D(p, q, N // 2)


def weyl_dim_poly(p, q, n_values):
    """Evaluate d(p,q,n) at given n values. N = n+2."""
    return {n: Fraction(dim_SO(p, q, n + 2)) for n in n_values}


# Generate Weyl dimension polynomials for (p,q) pairs
# Need basis polynomials up to degree 2k for a_k.
# d(p,q,n) has degree ~ 2(p+q) in n.
# For k=6 (degree 12), need (p,q) up to p+q ~ 6.

N_VALS = list(range(3, 36))  # n=3..35, 33 points

# Enumerate (p,q) pairs with p >= q >= 0, ordered by total weight
pq_pairs = []
for total in range(0, 15):  # up to total weight 14
    for q in range(total + 1):
        p = total - q
        if p >= q:
            pq_pairs.append((p, q))

# Compute d(p,q,n) values
dim_values = {}
for p, q in pq_pairs:
    vals = weyl_dim_poly(p, q, N_VALS)
    # Check it's not identically zero
    if any(v != 0 for v in vals.values()):
        dim_values[(p, q)] = vals

print(f"  (p,q) pairs considered: {len(pq_pairs)}")
print(f"  Non-zero dimension polynomials: {len(dim_values)}")

# Show first few
print(f"\n  Sample d(p,q,n) values at n=5:")
for (p, q) in list(dim_values.keys())[:10]:
    v5 = dim_values[(p, q)].get(5, Fraction(0))
    print(f"    d({p},{q},5) = {v5}")


# ═══════════════════════════════════════════════════════════════════
# SECTION 2: Recover d(p,q,n) as Exact Polynomials
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 2: Recovering Weyl Dimension Polynomials ───")


def lagrange_interpolate(points):
    """Exact Fraction Lagrange interpolation."""
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
    if n == 0: return {0: 1}
    factors = {}
    d = 2
    n = abs(n)
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1: factors[n] = 1
    return factors


def max_prime(n):
    if n == 0 or n == 1: return 1
    f = factor(abs(n))
    return max(f.keys()) if f else 1


# Recover each d(p,q,n) as polynomial in n
dim_polys = {}
for (p, q), vals in sorted(dim_values.items()):
    # Determine degree by checking when values become non-trivial
    pts = [(Fraction(n), vals[n]) for n in N_VALS]

    # Try increasing degrees until we find one that fits
    for deg_try in range(1, 30):
        n_pts = deg_try + 1
        if n_pts > len(pts):
            break
        poly = lagrange_interpolate(pts[:n_pts])
        # Verify on remaining points
        ok = all(eval_poly(poly, Fraction(n)) == vals[n] for n in N_VALS[n_pts:n_pts+5])
        if ok:
            dim_polys[(p, q)] = poly
            break

    if (p, q) not in dim_polys:
        # Try with more points
        poly = lagrange_interpolate(pts[:min(25, len(pts))])
        all_ok = all(eval_poly(poly, Fraction(n)) == vals[n] for n in N_VALS)
        if all_ok:
            dim_polys[(p, q)] = poly

print(f"  Recovered {len(dim_polys)} exact polynomials")

# Show degrees
degree_dist = {}
for (p, q), poly in sorted(dim_polys.items()):
    deg = len(poly) - 1
    degree_dist[deg] = degree_dist.get(deg, 0) + 1
    if p + q <= 3:
        # Show small examples
        den_primes = set()
        for c in poly:
            if c != 0:
                f = factor(c.denominator)
                den_primes.update(f.keys())
        print(f"    d({p},{q},n): degree {deg}, den primes ⊆ {sorted(den_primes)}")

print(f"\n  Degree distribution: {sorted(degree_dist.items())}")


# ═══════════════════════════════════════════════════════════════════
# SECTION 3: Known Heat Kernel Polynomials
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 3: Loading Known a_k(n) Polynomials ───")

# Known a_k(5) values — used for verification
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


def three_theorems(k):
    c_top = Fraction(1, 3**k * factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * factorial(k))
    return c_top, c_sub, c_const


# Load a_k polynomials from Toy 613/614 cascade
# We need to rebuild them from the checkpoint data or use stored values
# For this toy, compute a_k(n) at each n from the KNOWN polynomials
# by loading and cascading. But we don't have the full polynomials stored.
#
# Alternative: compute a_k(n) values directly from Toy 361 checkpoints.
# But that's slow. Instead, let's work with the KNOWN a_k(5) values
# to test the principle, then extend.
#
# BETTER: We can recover the low-k polynomials analytically.
# a_1(n) = n²/3 - 1/2
A1_POLY = [Fraction(-1, 2), Fraction(0), Fraction(1, 3)]

# For a_k with k ≥ 2, we need the full polynomial.
# Let's recover them from the cascade in Toy 612's checkpoint data.
# Since that's complex, let's work with what we can compute directly:
# evaluate a_k at n=3..35 using the cascade, then decompose.

# Actually, let's take a simpler approach: recover a_k polynomials
# for k=1..8 from the cascade, which runs fast on fixed checkpoints.
# For k=1, we have the exact polynomial above.
# For k=2..5, we can recover from n=3..13 (fixed checkpoints give exact values).

# Let me compute a_k(n) for k=1..8 at all n values by loading checkpoints
# and running the cascade. This reuses Toy 612's infrastructure.

import json
import mpmath
mpmath.mp.dps = 800

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_361_checkpoint")


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


def chebyshev_nodes(t_lo, t_hi, n_pts):
    t_lo_m = mpmath.mpf(t_lo)
    t_hi_m = mpmath.mpf(t_hi)
    mid = (t_lo_m + t_hi_m) / 2
    half = (t_hi_m - t_lo_m) / 2
    return sorted([mid + half * mpmath.cos((2 * k + 1) * mpmath.pi / (2 * n_pts))
                    for k in range(n_pts)])


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
        max_order = min(N, 25)
    else:
        max_order = min(max_order, N)
    ts_s = [p[0] for p in pairs[:max_order]]
    gs_s = [p[1] for p in pairs[:max_order]]
    T = [[mpmath.mpf(0)] * max_order for _ in range(max_order)]
    for i in range(max_order):
        T[i][0] = gs_s[i]
    best = T[0][0]
    best_err = mpmath.mpf('inf')
    for j in range(1, max_order):
        for i in range(j, max_order):
            r = ts_s[i] / ts_s[i - j]
            T[i][j] = (r * T[i][j-1] - T[i-j][j-1]) / (r - 1)
        if j >= 2:
            diff = abs(T[j][j] - T[j-1][j-1])
            if diff < best_err:
                best = T[j][j]
                best_err = diff
    return best, best_err


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
    a_k_rich, err_rich = richardson_extrapolate(ts, gs)
    n20 = min(20, len(ts))
    a_k_nev20 = neville(ts[:n20], gs[:n20], mpmath.mpf(0))
    agreement = min(abs(a_k_rich - a_k_nev), abs(a_k_rich - a_k_nev20),
                    abs(a_k_nev - a_k_nev20))
    if agreement < err_nev * 10 and err_rich < err_nev:
        return a_k_rich, err_rich
    elif abs(a_k_nev20 - a_k_nev) < err_nev:
        return a_k_nev20, abs(a_k_nev20 - a_k_nev)
    else:
        return a_k_nev, err_nev


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


def identify_rational(x_mpf, max_den=10**15, tol=1e-12, mp=None):
    x_str = mpmath.nstr(x_mpf, 80, strip_zeros=False)
    try:
        x_frac = Fraction(x_str)
    except (ValueError, ZeroDivisionError):
        return None
    best = None
    best_err = float('inf')
    for conv in _cf_convergents(x_frac, max_den=max_den):
        if conv.denominator > max_den:
            break
        err = abs(float(x_frac - conv))
        if err < tol and err < best_err:
            if mp:
                mf = max(factor(conv.denominator).keys()) if conv.denominator > 1 else 1
                if mf > mp:
                    continue
            best = conv
            best_err = err
    cand = x_frac.limit_denominator(max_den)
    err = abs(float(x_frac - cand))
    if err < tol and err < best_err:
        if mp:
            mf = max(factor(cand.denominator).keys()) if cand.denominator > 1 else 1
            if mf <= mp:
                best = cand
        else:
            best = cand
    return best


MAX_PRIME_BY_LEVEL = {
    6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23, 12: 23,
}

# Load checkpoint data and cascade
print(f"  Loading checkpoints...")
CASCADE_RANGE = range(3, 14)
FIXED_T_LO, FIXED_T_HI, N_PTS = 0.0008, 0.009, 48
fixed_ts = chebyshev_nodes(FIXED_T_LO, FIXED_T_HI, N_PTS)
fixed_data = {}
for n in CASCADE_RANGE:
    cached = load_heat_trace(n, "fixed")
    if cached:
        fixed_data[n] = (cached[1], cached[2])

# For adaptive data (k ≥ 6)
# Load all available adaptive checkpoints
adaptive_data = {}
adaptive_ts = {}
for n in N_VALS:
    cached = load_heat_trace(n, "adaptive")
    if cached:
        adaptive_data[n] = (cached[1], cached[2])
        # Reconstruct ts from checkpoint count
        t_hi = min(0.01, max(5e-6, 0.3 / (n * n)))
        t_lo = max(1e-7, t_hi / 20)
        adaptive_ts[n] = chebyshev_nodes(t_lo, t_hi, N_PTS)

print(f"  Fixed: {len(fixed_data)}, Adaptive: {len(adaptive_data)}")

# Cascade: recover a_k polynomials for k=1..8
KNOWN_POLYS = {1: A1_POLY}
all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in N_VALS}}

# Phase A: a_2..a_5 from fixed
for k in range(2, 6):
    deg = 2 * k
    c_top, c_sub, c_const = three_theorems(k)
    ak_rats = {}
    for n in CASCADE_RANGE:
        if n not in fixed_data:
            continue
        fs, vol = fixed_data[n]
        known_fracs = {0: Fraction(1)}
        for j in range(1, k):
            known_fracs[j] = all_rats[j][n]
        ak, _ = extract_coefficient(fs, fixed_ts, vol, known_fracs, k)
        frac = identify_rational(ak, max_den=500000, tol=1e-20)
        if frac:
            ak_rats[n] = frac

    pts = [(Fraction(nv), ak_rats[nv]) for nv in sorted(ak_rats.keys())[:deg+1]]
    ak_poly = lagrange_interpolate(pts)
    for nv in N_VALS:
        ak_rats[nv] = eval_poly(ak_poly, Fraction(nv))
    all_rats[k] = ak_rats
    KNOWN_POLYS[k] = ak_poly

    v5_ok = ak_rats[5] == KNOWN_AK5.get(k, None) if 5 in ak_rats else False
    print(f"  a_{k}: degree {len(ak_poly)-1}, a_{k}(5)={'✓' if v5_ok else '✗'}")

# Phase B: a_6..a_8 from adaptive
for k in range(6, 9):
    deg = 2 * k
    c_top, c_sub, c_const = three_theorems(k)
    mp = MAX_PRIME_BY_LEVEL.get(k, 23)
    ak_clean = {}
    for n in N_VALS:
        if n not in adaptive_data:
            continue
        fs, vol = adaptive_data[n]
        ts = adaptive_ts[n]
        known_fracs = {0: Fraction(1)}
        skip = False
        for j in range(1, k):
            v = all_rats[j].get(n)
            if v is None:
                skip = True
                break
            known_fracs[j] = v
        if skip:
            continue
        ak, _ = extract_coefficient(fs, ts, vol, known_fracs, k)
        frac = identify_rational(ak, max_den=10**15, tol=1e-12, mp=mp)
        if frac:
            ak_clean[n] = frac

    n_need = deg - 2
    if len(ak_clean) >= n_need:
        # Constrained polynomial recovery
        clean_ns = sorted(ak_clean.keys())
        residual_pts = []
        for nv in clean_ns:
            res = ak_clean[nv] - c_top * Fraction(nv)**deg \
                  - c_sub * Fraction(nv)**(deg-1) - c_const
            residual_pts.append((Fraction(nv), res / Fraction(nv)))
        n_use = min(len(residual_pts), n_need)
        red_poly = lagrange_interpolate(residual_pts[:n_use])
        extra = residual_pts[n_use:]
        ok = all(eval_poly(red_poly, p[0]) == p[1] for p in extra)

        poly = [Fraction(0)] * (deg + 1)
        poly[0] = c_const
        for j, c in enumerate(red_poly):
            poly[j + 1] += c
        poly[deg - 1] += c_sub
        poly[deg] = c_top

        for nv in N_VALS:
            ak_clean[nv] = eval_poly(poly, Fraction(nv))
        KNOWN_POLYS[k] = poly
    else:
        KNOWN_POLYS[k] = None

    all_rats[k] = ak_clean
    v5 = ak_clean.get(5)
    v5_ok = (v5 == KNOWN_AK5.get(k)) if v5 else False
    poly_deg = len(KNOWN_POLYS[k])-1 if KNOWN_POLYS[k] else "FAIL"
    print(f"  a_{k}: {len(ak_clean)}/{len(N_VALS)} clean, degree {poly_deg}, "
          f"a_{k}(5)={'✓' if v5_ok else '✗'}")

n_recovered = sum(1 for k in range(1, 9) if KNOWN_POLYS.get(k) is not None)
print(f"  Recovered {n_recovered}/8 polynomials")
score("Cascade a_1..a_8 complete (≥6 required)",
      n_recovered >= 6)


# ═══════════════════════════════════════════════════════════════════
# SECTION 4: Spectral Decomposition of a_k(n)
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 4: Spectral Basis Decomposition ───")


def spectral_decompose(ak_poly, dim_polys_by_deg):
    """Express a_k(n) = Σ α_{p,q} · d(p,q,n).

    Returns dict: (p,q) → α_{p,q} (Fraction)
    """
    deg = len(ak_poly) - 1

    # Select basis polynomials with degree ≤ deg
    basis_keys = []
    basis_polys = []
    for (p, q), dpoly in sorted(dim_polys_by_deg.items()):
        if len(dpoly) - 1 <= deg:
            basis_keys.append((p, q))
            basis_polys.append(dpoly)

    # We need to solve: ak_poly = Σ α_i * basis_polys[i]
    # This is a linear system in coefficient space.
    # Pad all polynomials to degree deg+1
    n_basis = len(basis_keys)
    n_coeffs = deg + 1

    if n_basis < n_coeffs:
        return None, f"Need {n_coeffs} basis polys, have {n_basis}"

    # Build matrix: M[j][i] = coeff_j of basis_polys[i]
    # Solve M * α = ak_coeffs

    # Use evaluation at n_basis specific n-values instead (more stable)
    # Pick n = 3, 4, ..., 3+n_basis-1
    eval_ns = list(range(3, 3 + n_basis))

    # Build matrix A[row][col] = d(p_col, q_col, n_row)
    A = []
    b = []
    for n in eval_ns:
        row = [eval_poly(bp, Fraction(n)) for bp in basis_polys]
        A.append(row)
        b.append(eval_poly(ak_poly, Fraction(n)))

    # Gaussian elimination with Fraction arithmetic
    n = len(A)
    m = len(A[0])
    # Augment: [A | b]
    aug = [row[:] + [b[i]] for i, row in enumerate(A)]

    # Forward elimination
    pivot_cols = []
    row_idx = 0
    for col in range(m):
        # Find pivot
        pivot = None
        for r in range(row_idx, n):
            if aug[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        pivot_cols.append(col)
        # Swap
        aug[row_idx], aug[pivot] = aug[pivot], aug[row_idx]
        # Eliminate
        for r in range(n):
            if r != row_idx and aug[r][col] != 0:
                factor_r = aug[r][col] / aug[row_idx][col]
                for c in range(m + 1):
                    aug[r][c] -= factor_r * aug[row_idx][c]
        row_idx += 1

    # Extract solution
    alphas = [Fraction(0)] * m
    for i, col in enumerate(pivot_cols):
        alphas[col] = aug[i][m] / aug[i][col]

    # Verify
    result = {}
    for i, (p, q) in enumerate(basis_keys):
        if alphas[i] != 0:
            result[(p, q)] = alphas[i]

    # Check reconstruction
    for n in [5, 7, 10, 15, 20]:
        pred = sum(alpha * eval_poly(dim_polys_by_deg[(p, q)], Fraction(n))
                   for (p, q), alpha in result.items())
        actual = eval_poly(ak_poly, Fraction(n))
        if pred != actual:
            return result, f"Mismatch at n={n}: pred={pred}, actual={actual}"

    return result, "OK"


# Decompose a_k for k=1..8
print(f"\n  Decomposing a_k(n) in Weyl dimension basis:")

for k in range(1, 9):
    if KNOWN_POLYS.get(k) is None:
        print(f"\n  a_{k}: No polynomial available")
        continue

    ak_poly = KNOWN_POLYS[k]
    deg = len(ak_poly) - 1

    alphas, status = spectral_decompose(ak_poly, dim_polys)

    if alphas is None:
        print(f"\n  a_{k} (degree {deg}): FAILED — {status}")
        continue

    print(f"\n  a_{k} (degree {deg}): {len(alphas)} non-zero spectral coefficients "
          f"[{status}]")

    # Analyze prime structure of spectral coefficients
    spec_max_den_prime = 1
    spec_max_num_prime = 1
    mono_max_den_prime = 1
    mono_max_num_prime = 1

    # Spectral coefficients
    for (p, q), alpha in sorted(alphas.items()):
        dp = max_prime(alpha.denominator)
        np_ = max_prime(alpha.numerator)
        if dp > spec_max_den_prime:
            spec_max_den_prime = dp
        if np_ > spec_max_num_prime:
            spec_max_num_prime = np_

        if len(alphas) <= 20 or alpha.denominator > 1:
            alpha_str = str(alpha)
            if len(alpha_str) > 50:
                alpha_str = alpha_str[:47] + "..."
            print(f"    α({p},{q}) = {alpha_str}  [den max p = {dp}]")

    # Monomial coefficients (interior only: c_1 through c_{deg-2})
    for j in range(1, deg - 1):
        c = ak_poly[j]
        if c != 0:
            dp = max_prime(c.denominator)
            np_ = max_prime(c.numerator)
            if dp > mono_max_den_prime:
                mono_max_den_prime = dp
            if np_ > mono_max_num_prime:
                mono_max_num_prime = np_

    print(f"\n    Interior prime comparison:")
    print(f"      Monomial basis: max den prime = {mono_max_den_prime}, "
          f"max num prime = {mono_max_num_prime}")
    print(f"      Spectral basis: max den prime = {spec_max_den_prime}, "
          f"max num prime = {spec_max_num_prime}")

    cleaner = spec_max_den_prime < mono_max_den_prime
    same = spec_max_den_prime == mono_max_den_prime
    print(f"      → {'CLEANER' if cleaner else 'SAME' if same else 'WORSE'} "
          f"denominators in spectral basis")


# ═══════════════════════════════════════════════════════════════════
# SECTION 5: Speaking Pairs in Spectral Coefficients
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 5: Speaking Pairs in Spectral Coefficients ───")

print(f"\n  The speaking pair prediction: sub-leading ratios at k ≡ 0,1 (mod 5)")
print(f"  encode gauge group dimensions. In spectral basis, these should")
print(f"  emerge as specific α(p,q) values.")

# At n=5 (Q^5), the speaking pairs are:
# k=6,7: ratio = -3 = -N_c
# k=8,9: ratio = -5 = -n_C (but k=8 starts the pattern)

# Check if any spectral coefficients at k=6,7,8 have values related
# to N_c=3, n_C=5, g=7, C_2=6

five_integers = {3: "N_c", 5: "n_C", 7: "g", 6: "C_2", 137: "N_max",
                 21: "dim SO(7)/2", 10: "dim SO(5)", 24: "dim SU(5)"}

for k in range(1, 9):
    if KNOWN_POLYS.get(k) is None:
        continue
    alphas, status = spectral_decompose(KNOWN_POLYS[k], dim_polys)
    if alphas is None:
        continue

    # Look for five-integer values in numerators/denominators
    hits = []
    for (p, q), alpha in alphas.items():
        num = abs(alpha.numerator)
        den = alpha.denominator
        for val, name in five_integers.items():
            if num == val or den == val:
                hits.append(((p, q), alpha, val, name))
            # Also check if num/den is a small multiple
            if den > 0 and num % val == 0 and num // val <= 10:
                hits.append(((p, q), alpha, val, f"{num//val}×{name}"))

    if hits:
        print(f"\n  a_{k}: Five-integer values found in spectral coefficients:")
        for (p, q), alpha, val, name in hits:
            print(f"    α({p},{q}) = {alpha} — contains {name} = {val}")


# ═══════════════════════════════════════════════════════════════════
# SECTION 6: Cumulative VSC Prime Analysis
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 6: VSC Prime Comparison (Spectral vs Monomial) ───")

# For each k, compare: which basis has smaller max denominator prime?
print(f"\n  {'k':>2} | {'Mono den max p':>14} | {'Spec den max p':>14} | {'Winner':>8}")
print(f"  {'─'*2}-+-{'─'*14}-+-{'─'*14}-+-{'─'*8}")

spec_wins = 0
mono_wins = 0
ties = 0

for k in range(1, 9):
    if KNOWN_POLYS.get(k) is None:
        continue

    ak_poly = KNOWN_POLYS[k]
    deg = len(ak_poly) - 1

    # Monomial interior max prime
    mono_mp = 1
    for j in range(1, deg - 1):
        if ak_poly[j] != 0:
            mp = max_prime(ak_poly[j].denominator)
            if mp > mono_mp:
                mono_mp = mp

    # Spectral max prime
    alphas, _ = spectral_decompose(ak_poly, dim_polys)
    spec_mp = 1
    if alphas:
        for alpha in alphas.values():
            mp = max_prime(alpha.denominator)
            if mp > spec_mp:
                spec_mp = mp

    if spec_mp < mono_mp:
        winner = "SPECTRAL"
        spec_wins += 1
    elif spec_mp == mono_mp:
        winner = "TIE"
        ties += 1
    else:
        winner = "MONO"
        mono_wins += 1

    print(f"  {k:>2} | {mono_mp:>14} | {spec_mp:>14} | {winner:>8}")

print(f"\n  Summary: Spectral wins {spec_wins}, Monomial wins {mono_wins}, "
      f"Ties {ties}")

is_matched = spec_wins > mono_wins
score("Spectral basis is matched codebook (wins more)",
      is_matched,
      f"Spectral: {spec_wins}, Monomial: {mono_wins}, Ties: {ties}")

# ═══════════════════════════════════════════════════════════════════
# SECTION 7: Evaluate at n=5 (the BST dimension)
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 7: Spectral Decomposition at n=5 (Q⁵) ───")

print(f"\n  At n=n_C=5, the spectral coefficients should simplify")
print(f"  because the geometry IS the BST domain D_IV^5.")

for k in [6, 7, 8]:
    if KNOWN_POLYS.get(k) is None:
        continue

    alphas, _ = spectral_decompose(KNOWN_POLYS[k], dim_polys)
    if alphas is None:
        continue

    # Evaluate each spectral term at n=5
    print(f"\n  a_{k}(5) = {KNOWN_AK5[k]} decomposed:")
    total = Fraction(0)
    terms = []
    for (p, q), alpha in sorted(alphas.items()):
        d5 = dim_SO(p, q, 7)  # SO(7) = SO(5+2)
        contrib = alpha * d5
        if contrib != 0:
            terms.append(((p, q), alpha, d5, contrib))
            total += contrib

    # Show dominant terms
    terms.sort(key=lambda x: abs(x[3]), reverse=True)
    for (p, q), alpha, d5, contrib in terms[:8]:
        pct = float(contrib / total) * 100 if total != 0 else 0
        print(f"    α({p},{q})·d({p},{q},5) = {alpha} × {d5} = {contrib}"
              f"  ({pct:+.1f}%)")

    if len(terms) > 8:
        print(f"    ... ({len(terms)-8} more terms)")

    ok = total == KNOWN_AK5[k]
    print(f"    Total: {total} {'✓' if ok else '✗'}")


# ═══════════════════════════════════════════════════════════════════
# SECTION 8: n=5 Denominator Analysis
# ═══════════════════════════════════════════════════════════════════

print(f"\n─── Section 8: Why is n=5 Tame? ───")

print(f"\n  At n=5, d(p,q,5) = dim of SO(7) irrep (p,q).")
print(f"  If d(p,q,5) has factors that cancel denominator primes")
print(f"  in α(p,q), that explains arithmetic tameness.")

for k in [6, 7, 8]:
    if KNOWN_POLYS.get(k) is None:
        continue

    alphas, _ = spectral_decompose(KNOWN_POLYS[k], dim_polys)
    if alphas is None:
        continue

    print(f"\n  a_{k} spectral terms at n=5:")
    for (p, q), alpha in sorted(alphas.items()):
        d5 = dim_SO(p, q, 7)
        if d5 == 0 or alpha == 0:
            continue
        prod = alpha * d5
        alpha_dp = max_prime(alpha.denominator)
        prod_dp = max_prime(prod.denominator)
        cancel = alpha_dp > prod_dp
        if cancel or alpha_dp > 3:
            print(f"    ({p},{q}): α den max p = {alpha_dp}, "
                  f"α·d(5) den max p = {prod_dp}"
                  f"  {'← CANCELLATION' if cancel else ''}")


# ═══════════════════════════════════════════════════════════════════
# SCORECARD
# ═══════════════════════════════════════════════════════════════════

elapsed = time.time() if 't_start' not in dir() else 0

print(f"\n{'═' * 64}")
print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
print(f"{'═' * 64}")

if PASS > FAIL:
    print(f"\n  Spectral basis decomposition complete.")
else:
    print(f"\n  Mixed results — spectral basis may not be cleaner.")

print(f"\n  Key question answered: Does the geometry's own codebook")
print(f"  (Weyl dimension polynomials) clean up heat kernel arithmetic?")
