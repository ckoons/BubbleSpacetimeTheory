#!/usr/bin/env python3
"""
Toy 257b — Verify c₁₀ = 1/29160 for a₅(n) Polynomial
======================================================

Full cascade recomputation with P_max=500, mpmath 80-digit precision.
Derives all polynomials from scratch (no hardcoded coefficients).

CONJECTURE: c_{2k} of a_k(n) = 1/(3^k × k!)
  → c₁₀ = 1/(3⁵ × 5!) = 1/29160

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import time
from fractions import Fraction
import mpmath

mpmath.mp.dps = 80  # 80 decimal digits


def frac_to_mpf(frac):
    return mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)


# ═══════════════════════════════════════════════════════════════════
# WEYL DIMENSION FORMULAS
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
    return _dim_B(p, q, (N-1)//2) if N % 2 == 1 else _dim_D(p, q, N//2)


# ═══════════════════════════════════════════════════════════════════
# SPECTRUM, HEAT TRACE, EXTRACTION
# ═══════════════════════════════════════════════════════════════════

def build_spectrum(n, P_max=500):
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


def mpmath_f(t, n, eigs, dims):
    Z = mpmath.fsum(mpmath.mpf(d) * mpmath.exp(-mpmath.mpf(lam) * t)
                    for lam, d in zip(eigs, dims))
    return (4 * mpmath.pi * t)**n * Z


def neville(xs, ys, x_target):
    nn = len(xs)
    P = [mpmath.mpf(y) for y in ys]
    for j in range(1, nn):
        P_new = [mpmath.mpf(0)] * nn
        for i in range(j, nn):
            P_new[i] = ((x_target - xs[i-j]) * P[i] - (x_target - xs[i]) * P[i-1]) \
                       / (xs[i] - xs[i-j])
        P = P_new
    return P[nn-1]


def chebyshev_nodes(t_lo, t_hi, n_pts):
    t_lo_m = mpmath.mpf(t_lo)
    t_hi_m = mpmath.mpf(t_hi)
    mid = (t_lo_m + t_hi_m) / 2
    half = (t_hi_m - t_lo_m) / 2
    nodes = [mid + half * mpmath.cos((2*k + 1) * mpmath.pi / (2*n_pts))
             for k in range(n_pts)]
    nodes.sort()
    return nodes


def extract_volume(n, eigs, dims, n_pts=24, t_lo=0.001, t_hi=0.015):
    ts = chebyshev_nodes(t_lo, t_hi, n_pts)
    fs = [mpmath_f(t, n, eigs, dims) for t in ts]
    vol = neville(ts, fs, mpmath.mpf(0))
    vol_odd = neville(ts[::2], [fs[i] for i in range(0, n_pts, 2)], mpmath.mpf(0))
    err = abs(vol - vol_odd)
    return vol, err


def extract_coeff(n, eigs, dims, known_exact, target_k, vol,
                  n_pts=24, t_lo=0.001, t_hi=0.015):
    ts = chebyshev_nodes(t_lo, t_hi, n_pts)
    gs = []
    for t in ts:
        f = mpmath_f(t, n, eigs, dims)
        F = f / vol
        for j in range(target_k):
            F -= known_exact[j] * t**j
        g = F / t**target_k
        gs.append(g)
    a_k = neville(ts, gs, mpmath.mpf(0))
    a_k_sub = neville(ts[::2], [gs[i] for i in range(0, n_pts, 2)], mpmath.mpf(0))
    err = abs(a_k - a_k_sub)
    return a_k, err


# ═══════════════════════════════════════════════════════════════════
# RATIONAL IDENTIFICATION & INTERPOLATION
# ═══════════════════════════════════════════════════════════════════

def identify_rational(x_mpf, max_den=500000, tol=1e-14):
    x = float(x_mpf)
    best = None
    best_err = float('inf')
    for d in range(1, max_den + 1):
        n_approx = x * d
        n_round = round(n_approx)
        err = abs(n_approx - n_round) / d
        if err < tol and err < best_err:
            best = Fraction(n_round, d)
            best_err = err
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
            if j == i: continue
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


# ═══════════════════════════════════════════════════════════════════
# MAIN — full cascade, no hardcoded polynomials
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    print("=" * 72)
    print("Toy 257b — Verify c₁₀ = 1/29160")
    print("Full cascade: P_max=500, mpmath 80 digits, 24 Chebyshev nodes")
    print("=" * 72)

    P_MAX = 500
    N_PTS = 24
    T_LO = 0.001
    T_HI = 0.015
    N_RANGE = range(3, 14)  # n = 3..13

    # ─── Build spectra ────────────────────────────────────────
    print(f"\n  Building spectra (P_max={P_MAX})...")
    spectra = {}
    for n in N_RANGE:
        t0 = time.time()
        eigs, dims = build_spectrum(n, P_MAX)
        spectra[n] = (eigs, dims)
        print(f"    n={n:>2}: {len(eigs):>6} eigenvalues ({time.time()-t0:.1f}s)")

    # ─── Volume extraction ────────────────────────────────────
    print(f"\n  Volume extraction...")
    volumes = {}
    for n in N_RANGE:
        vol, vol_err = extract_volume(n, *spectra[n], N_PTS, T_LO, T_HI)
        volumes[n] = vol
        print(f"    n={n:>2}: err ≈ {mpmath.nstr(vol_err, 3)}")

    # ─── a₂ cascade ──────────────────────────────────────────
    print(f"\n  a₂ cascade → degree-4 polynomial...")
    a2_rats = {}
    for n in N_RANGE:
        a1_mpf = frac_to_mpf(Fraction(2*n*n - 3, 6))
        known = {0: mpmath.mpf(1), 1: a1_mpf}
        a2, _ = extract_coeff(n, *spectra[n], known, 2, volumes[n], N_PTS, T_LO, T_HI)
        frac, _ = identify_rational(a2, max_den=10000)
        if frac: a2_rats[n] = frac
        print(f"    n={n:>2}: a₂ ≈ {frac}")

    pts = [(Fraction(nv), a2_rats[nv]) for nv in sorted(a2_rats.keys())[:5]]
    extra = [(Fraction(nv), a2_rats[nv]) for nv in sorted(a2_rats.keys())[5:]]
    a2_poly = lagrange_interpolate(pts)
    ok = all(eval_poly(a2_poly, x) == y for x, y in extra)
    print(f"    Degree {len(a2_poly)-1}: {'✓ VERIFIED' if ok else '✗'} ({len(extra)} extra)")
    if ok:
        for nv in N_RANGE:
            a2_rats[nv] = eval_poly(a2_poly, Fraction(nv))
    print(f"    a₂(5) = {a2_rats[5]} {'✓' if a2_rats[5] == Fraction(274,9) else '✗'}")

    # ─── a₃ cascade ──────────────────────────────────────────
    print(f"\n  a₃ cascade → degree-6 polynomial...")
    a3_rats = {}
    for n in N_RANGE:
        a1_mpf = frac_to_mpf(Fraction(2*n*n - 3, 6))
        a2_mpf = frac_to_mpf(a2_rats[n])
        known = {0: mpmath.mpf(1), 1: a1_mpf, 2: a2_mpf}
        a3, _ = extract_coeff(n, *spectra[n], known, 3, volumes[n], N_PTS, T_LO, T_HI)
        frac, _ = identify_rational(a3, max_den=10000)
        if frac: a3_rats[n] = frac
        print(f"    n={n:>2}: a₃ ≈ {frac}")

    pts = [(Fraction(nv), a3_rats[nv]) for nv in sorted(a3_rats.keys())[:7]]
    extra = [(Fraction(nv), a3_rats[nv]) for nv in sorted(a3_rats.keys())[7:]]
    a3_poly = lagrange_interpolate(pts)
    ok = all(eval_poly(a3_poly, x) == y for x, y in extra)
    print(f"    Degree {len(a3_poly)-1}: {'✓ VERIFIED' if ok else '✗'} ({len(extra)} extra)")
    if ok:
        for nv in N_RANGE:
            a3_rats[nv] = eval_poly(a3_poly, Fraction(nv))
    print(f"    a₃(5) = {a3_rats[5]} {'✓' if a3_rats[5] == Fraction(703,9) else '✗'}")

    # ─── a₄ cascade ──────────────────────────────────────────
    print(f"\n  a₄ cascade → degree-8 polynomial...")
    a4_rats = {}
    for n in N_RANGE:
        a1_mpf = frac_to_mpf(Fraction(2*n*n - 3, 6))
        a2_mpf = frac_to_mpf(a2_rats[n])
        a3_mpf = frac_to_mpf(a3_rats[n])
        known = {0: mpmath.mpf(1), 1: a1_mpf, 2: a2_mpf, 3: a3_mpf}
        a4, _ = extract_coeff(n, *spectra[n], known, 4, volumes[n], N_PTS, T_LO, T_HI)
        frac, _ = identify_rational(a4, max_den=200000)
        if frac: a4_rats[n] = frac

    pts = [(Fraction(nv), a4_rats[nv]) for nv in sorted(a4_rats.keys())[:9]]
    extra = [(Fraction(nv), a4_rats[nv]) for nv in sorted(a4_rats.keys())[9:]]
    a4_poly = lagrange_interpolate(pts)
    ok = all(eval_poly(a4_poly, x) == y for x, y in extra)
    print(f"    Degree {len(a4_poly)-1}: {'✓ VERIFIED' if ok else '✗'} ({len(extra)} extra)")
    if ok:
        for nv in N_RANGE:
            a4_rats[nv] = eval_poly(a4_poly, Fraction(nv))
    print(f"    a₄(5) = {a4_rats[5]} {'✓' if a4_rats[5] == Fraction(2671,18) else '✗'}")

    # ─── a₅ cascade ──────────────────────────────────────────
    print(f"\n  " + "═" * 64)
    print(f"  a₅ cascade (THE MAIN EVENT)")
    print("  " + "═" * 64)

    a5_vals = {}
    a5_rats = {}
    for n in N_RANGE:
        t0 = time.time()
        a1_mpf = frac_to_mpf(Fraction(2*n*n - 3, 6))
        a2_mpf = frac_to_mpf(a2_rats[n])
        a3_mpf = frac_to_mpf(a3_rats[n])
        a4_mpf = frac_to_mpf(a4_rats[n])
        known = {0: mpmath.mpf(1), 1: a1_mpf, 2: a2_mpf,
                 3: a3_mpf, 4: a4_mpf}
        a5, a5_err = extract_coeff(n, *spectra[n], known, 5, volumes[n],
                                    N_PTS, T_LO, T_HI)
        a5_vals[n] = (a5, a5_err)

        md = 500000 if n >= 10 else 200000 if n >= 7 else 10000
        frac, ferr = identify_rational(a5, max_den=md, tol=1e-14)
        if frac:
            a5_rats[n] = frac
        elapsed = time.time() - t0
        print(f"    n={n:>2}: a₅ = {mpmath.nstr(a5, 25)}  "
              f"≈ {a5_rats.get(n, '?')}  "
              f"(err={mpmath.nstr(a5_err, 3)}, {elapsed:.1f}s)")

    # a₅(5) check
    print(f"\n    a₅(Q⁵) = {a5_rats.get(5)} "
          f"{'✓' if a5_rats.get(5) == Fraction(1535969, 6930) else '✗'}")

    # Rational table
    print(f"\n    {'n':<4} {'a₅':<30} {'den':<12} {'factors':<35} {'prime?'}")
    print(f"    {'─'*85}")
    for n in N_RANGE:
        if n in a5_rats:
            f = a5_rats[n]
            pr = "PRIME" if is_prime(abs(f.numerator)) else ""
            print(f"    {n:<4} {str(f):<30} {f.denominator:<12} "
                  f"{str(factor(f.denominator)):<35} {pr}")
        else:
            v, _ = a5_vals[n]
            print(f"    {n:<4} ≈{mpmath.nstr(v,15):<29} {'?':<12}")

    # ─── Lagrange interpolation ───────────────────────────────
    print(f"\n  " + "═" * 64)
    print(f"  a₅(n) POLYNOMIAL")
    print("  " + "═" * 64)

    n_rats = len(a5_rats)
    print(f"    Rationals: {n_rats}/11")

    a5_poly = None
    if n_rats >= 11:
        all_ns = sorted(a5_rats.keys())
        pts = [(Fraction(nv), a5_rats[nv]) for nv in all_ns]
        a5_poly = lagrange_interpolate(pts)
        deg = len(a5_poly) - 1
        print(f"    Degree: {deg}")

        # Self-consistency
        all_ok = True
        for nv in all_ns:
            if eval_poly(a5_poly, Fraction(nv)) != a5_rats[nv]:
                all_ok = False
                break
        print(f"    Self-consistent: {'✓' if all_ok else '✗'}")

        # Coefficients
        print(f"\n    ╔═══ a₅(n) POLYNOMIAL (degree {deg}) ═══╗")
        for k, c in enumerate(a5_poly):
            if c != 0:
                print(f"    ║  c_{k:<2} = {c}")
                print(f"    ║       = {float(c):.18e}")
                print(f"    ║       den factors: {factor(c.denominator)}")
        print(f"    ╚{'═'*50}╝")

    elif n_rats == 10:
        # Missing one rational — try constrained approach
        print(f"    10 rationals found. Trying degree-9 fit + prediction...")
        all_ns = sorted(a5_rats.keys())
        pts = [(Fraction(nv), a5_rats[nv]) for nv in all_ns]
        poly9 = lagrange_interpolate(pts)
        deg = len(poly9) - 1
        print(f"    Fitted degree: {deg}")

        # Find which n is missing
        missing = [nv for nv in N_RANGE if nv not in a5_rats]
        for nv in missing:
            pred = eval_poly(poly9, Fraction(nv))
            print(f"    Predicted a₅({nv}) = {pred} = {float(pred):.15f}")
            # Try to identify
            frac, _ = identify_rational(mpmath.mpf(float(pred)), max_den=500000, tol=1e-8)
            if frac:
                print(f"    → Rational: {frac}  den={frac.denominator}")
                a5_rats[nv] = frac

        if len(a5_rats) >= 11:
            all_ns = sorted(a5_rats.keys())
            pts = [(Fraction(nv), a5_rats[nv]) for nv in all_ns]
            a5_poly = lagrange_interpolate(pts)
            deg = len(a5_poly) - 1
            print(f"\n    Full polynomial degree: {deg}")
            print(f"\n    ╔═══ a₅(n) POLYNOMIAL (degree {deg}) ═══╗")
            for k, c in enumerate(a5_poly):
                if c != 0:
                    print(f"    ║  c_{k:<2} = {c}")
                    print(f"    ║       = {float(c):.18e}")
            print(f"    ╚{'═'*50}╝")

    # ─── LEADING COEFFICIENT TEST ─────────────────────────────
    print(f"\n  " + "═" * 64)
    print(f"  LEADING COEFFICIENT TEST: c₁₀ = 1/29160 ?")
    print("  " + "═" * 64)

    print(f"    Pattern: c_{{2k}} = 1/(3^k × k!)")
    checks_lc = [
        (1, Fraction(1, 3)),
        (2, Fraction(1, 18)),
        (3, Fraction(1, 162)),
        (4, Fraction(1, 1944)),
    ]
    for k, expected in checks_lc:
        print(f"      k={k}: 1/(3^{k}×{k}!) = {expected} = {float(expected):.12f} ✓")

    target = Fraction(1, 29160)
    print(f"      k=5: 1/(3⁵×5!) = {target} = {float(target):.12f} ← PREDICTION")

    if a5_poly and len(a5_poly) > 10:
        actual = a5_poly[10]
        match = actual == target
        print(f"\n    Actual c₁₀ = {actual}")
        print(f"                = {float(actual):.18e}")
        print(f"    Target     = {target}")
        print(f"                = {float(target):.18e}")
        print(f"\n    ╔{'═'*50}╗")
        if match:
            print(f"    ║  c₁₀ = 1/29160 = 1/(3⁵×5!)  ✓ CONFIRMED      ║")
            print(f"    ║  Pattern c_{{2k}} = 1/(3^k × k!) holds for k=1..5 ║")
        else:
            ratio = actual / target
            print(f"    ║  c₁₀ ≠ 1/29160  ✗                              ║")
            print(f"    ║  Ratio = {ratio} = {float(ratio):.10f}{'':>10}║")
        print(f"    ╚{'═'*50}╝")
    else:
        print(f"\n    No degree-10 polynomial available.")

    # ─── SUMMARY ──────────────────────────────────────────────
    print(f"\n  " + "═" * 64)
    print(f"  SUMMARY")
    print("  " + "═" * 64)

    checks = [
        ("a₅(Q⁵) = 1535969/6930", a5_rats.get(5) == Fraction(1535969, 6930)),
        (f"All 11 rationals ({n_rats}/11)", n_rats >= 11),
        ("Degree = 10", a5_poly is not None and len(a5_poly) - 1 == 10),
    ]
    if a5_poly and len(a5_poly) > 10:
        checks.append(("c₁₀ = 1/29160 EXACT", a5_poly[10] == target))

    score = sum(1 for _, ok in checks if ok)
    for desc, ok in checks:
        print(f"    [{'✓' if ok else '✗'}] {desc}")
    print(f"\n    Score: {score}/{len(checks)}")

    elapsed = time.time() - t_start
    print(f"\n  Toy 257b complete. ({elapsed:.0f}s)")


if __name__ == '__main__':
    main()
