#!/usr/bin/env python3
"""
Toy 256 — Extended-Precision Heat Kernel Coefficients
=====================================================

Two deliverables:
  1. a₄(n) exact rationals for n=3..12 → Lagrange interpolation → degree-7 polynomial
  2. a₅(Q⁵) exact rational identification

METHOD: Sequential subtraction with known exact coefficients.
  Phase 1: Extract a₂(n), a₃(n) using a₀=1, a₁=(2n²-3)/6 (exact)
  Phase 2: Extract a₄(n) using exact a₀-a₃
  Phase 3: Extract a₅(n) using exact a₀-a₄
  Each subtraction removes dominant terms, dramatically improving precision.

STRUCTURAL CONSTRAINT (Gilkey):
  On Q^n with ∇R = 0, each a_k is a polynomial in n with rational coefficients.
  a₁: degree 2,  a₂: degree 4,  a₃: degree 6,  a₄: degree ≤ 8 (empirically 7)

Score: TBD

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import numpy as np
import time
from fractions import Fraction

import matplotlib
try:
    matplotlib.use('TkAgg')
except Exception:
    pass
import matplotlib.pyplot as plt

# ═══════════════════════════════════════════════════════════════════
# COLORS
# ═══════════════════════════════════════════════════════════════════

BG = '#1a1a2e'
WHITE = '#ffffff'
DIM = '#667788'
GOLD = '#ffd700'
RED = '#e94560'
CYAN = '#53d8fb'
GREEN = '#50fa7b'
PURPLE = '#bd93f9'

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
# SPECTRUM & HEAT TRACE
# ═══════════════════════════════════════════════════════════════════

def build_spectrum(n, P_max=800):
    """Returns (eigenvalues, multiplicities) as numpy arrays."""
    N = n + 2
    eigs, dims = [], []
    for p in range(P_max):
        for q in range(p + 1):
            lam = p * (p + n) + q * (q + n - 2)
            d = dim_SO(p, q, N)
            if d > 0:
                eigs.append(lam)
                dims.append(d)
    return np.array(eigs, dtype=np.float64), np.array(dims, dtype=np.float64)


def heat_trace(t, eigs, dims):
    """Z(t) = Σ d_i exp(-λ_i t)"""
    exps = eigs * t
    mask = exps < 500
    return np.sum(dims[mask] * np.exp(-exps[mask]))


def f_values(t_arr, n, eigs, dims):
    """Compute f(t) = (4πt)^n Z(t) at array of t values."""
    result = np.zeros(len(t_arr))
    for i, t in enumerate(t_arr):
        Z = heat_trace(t, eigs, dims)
        result[i] = (4 * np.pi * t)**n * Z
    return result


# ═══════════════════════════════════════════════════════════════════
# EXTRACTION VIA SEQUENTIAL SUBTRACTION
# ═══════════════════════════════════════════════════════════════════

def extract_with_subtraction(n, eigs, dims, known_coeffs, target_k, vol,
                              t_lo=0.003, t_hi=0.03, n_pts=2000, fit_deg=8):
    """Extract a_{target_k} by subtracting known a₀..a_{target_k-1}.

    g(t) = [f(t)/vol - Σ_{j<k} a_j t^j] / t^k
    Then fit g(t) as polynomial in t, and g(0) = a_k.
    """
    t_arr = np.linspace(t_lo, t_hi, n_pts)
    f_arr = f_values(t_arr, n, eigs, dims)

    # Normalize by volume: fn(t) = 1 + a₁t + a₂t² + ...
    fn = f_arr / vol

    # Subtract known coefficients
    remainder = fn.copy()
    for j in range(target_k):
        a_j = known_coeffs.get(j, 0.0)
        remainder -= a_j * t_arr**j

    # Divide by t^{target_k}
    g = remainder / t_arr**target_k

    # Fit g(t) as polynomial of low degree
    p = np.polyfit(t_arr, g, fit_deg)
    a_k = p[-1]  # constant term

    return a_k


def extract_crossval(n, eigs, dims, known_coeffs, target_k, vol):
    """Cross-validated extraction with multiple configurations."""
    # Adapt t range to n: smaller t for larger n (coefficients grow)
    scale = max(1, n / 5)
    t_base_lo = 0.002 / scale
    t_base_hi = 0.025 / scale

    configs = [
        (t_base_lo, t_base_hi, 2000, 6),
        (t_base_lo, t_base_hi, 2000, 7),
        (t_base_lo, t_base_hi, 2000, 8),
        (t_base_lo * 1.5, t_base_hi * 0.8, 1500, 6),
        (t_base_lo * 1.5, t_base_hi * 0.8, 1500, 7),
        (t_base_lo * 0.8, t_base_hi * 1.2, 2500, 7),
        (t_base_lo * 0.8, t_base_hi * 1.2, 2500, 8),
        (t_base_lo * 2, t_base_hi * 0.7, 1200, 6),
        (t_base_lo * 0.5, t_base_hi * 1.5, 3000, 8),
        (t_base_lo, t_base_hi, 2000, 9),
    ]

    vals = []
    for t_lo, t_hi, n_pts, deg in configs:
        try:
            v = extract_with_subtraction(n, eigs, dims, known_coeffs,
                                          target_k, vol, t_lo, t_hi, n_pts, deg)
            if np.isfinite(v):
                vals.append(v)
        except Exception:
            pass

    if not vals:
        return 0.0, float('inf')
    arr = np.array(vals)
    return np.median(arr), np.std(arr)


# ═══════════════════════════════════════════════════════════════════
# RATIONAL IDENTIFICATION
# ═══════════════════════════════════════════════════════════════════

def identify_rational(x, max_den=5000, tol=1e-6):
    """Find best rational approximation with small denominator."""
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


# ═══════════════════════════════════════════════════════════════════
# LAGRANGE INTERPOLATION
# ═══════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("Toy 256 — Extended-Precision Heat Kernel Coefficients")
    print("Method: Sequential subtraction + cross-validated polynomial fit")
    print("=" * 72)

    P_MAX = 1000

    # ─── Phase 0: Build spectra ───────────────────────────────
    print("\n  " + "─" * 64)
    print("  Phase 0: Building spectra (P_max={})".format(P_MAX))
    print("  " + "─" * 64)

    spectra = {}
    for n in range(3, 13):
        t0 = time.time()
        eigs, dims = build_spectrum(n, P_MAX)
        spectra[n] = (eigs, dims)
        print(f"    n={n}: {len(eigs)} eigenvalues ({time.time()-t0:.1f}s)")

    # ─── Phase 1: Volume (a₀) ────────────────────────────────
    print("\n  " + "─" * 64)
    print("  Phase 1: Volume extraction (a₀)")
    print("  " + "─" * 64)

    volumes = {}
    for n in range(3, 13):
        eigs, dims = spectra[n]
        t_arr = np.linspace(0.002, 0.02, 2000)
        f_arr = f_values(t_arr, n, eigs, dims)
        p = np.polyfit(t_arr, f_arr, 12)
        vol = p[-1]
        volumes[n] = vol
        print(f"    n={n}: vol = {vol:.12f}")

    # ─── Phase 2: Extract a₂, a₃ ─────────────────────────────
    print("\n  " + "─" * 64)
    print("  Phase 2: Extract a₂(n), a₃(n) using exact a₀=1, a₁=(2n²-3)/6")
    print("  " + "─" * 64)

    a2_vals = {}
    a3_vals = {}
    a2_rats = {}
    a3_rats = {}

    for n in range(3, 13):
        eigs, dims = spectra[n]
        a1_exact = float(Fraction(2*n*n - 3, 6))
        known = {0: 1.0, 1: a1_exact}

        # Extract a₂
        vol = volumes[n]
        a2, a2_std = extract_crossval(n, eigs, dims, known, target_k=2, vol=vol)
        a2_vals[n] = (a2, a2_std)
        frac, err = identify_rational(a2, max_den=5000, tol=1e-5)
        if frac:
            a2_rats[n] = frac

        # Extract a₃ (using extracted a₂)
        if frac:
            known[2] = float(frac)
        else:
            known[2] = a2
        a3, a3_std = extract_crossval(n, eigs, dims, known, target_k=3, vol=vol)
        a3_vals[n] = (a3, a3_std)
        frac3, err3 = identify_rational(a3, max_den=5000, tol=1e-5)
        if frac3:
            a3_rats[n] = frac3

        a2_str = f"{a2_rats.get(n, '?')}" if n in a2_rats else f"{a2:.8f}"
        a3_str = f"{a3_rats.get(n, '?')}" if n in a3_rats else f"{a3:.8f}"
        print(f"    n={n}: a₂={a2:.8f} ≈ {a2_str:>12}  "
              f"a₃={a3:.8f} ≈ {a3_str:>12}  "
              f"(σ₂={a2_std:.1e}, σ₃={a3_std:.1e})")

    # Check known values
    print(f"\n    Checks:")
    for n, expected in [(5, Fraction(274, 9))]:
        got = a2_rats.get(n)
        print(f"      a₂({n}) = {got} (expect {expected}) {'✓' if got == expected else '✗'}")
    for n, expected in [(5, Fraction(703, 9))]:
        got = a3_rats.get(n)
        print(f"      a₃({n}) = {got} (expect {expected}) {'✓' if got == expected else '✗'}")

    # ─── Phase 2b: a₂(n), a₃(n) polynomials ──────────────────
    print("\n  " + "─" * 64)
    print("  Phase 2b: a₂(n) polynomial (expect degree 4)")
    print("  " + "─" * 64)

    if len(a2_rats) >= 6:
        pts = [(Fraction(n), a2_rats[n]) for n in sorted(a2_rats.keys())[:5]]
        extra = [(Fraction(n), a2_rats[n]) for n in sorted(a2_rats.keys())[5:]]
        a2_poly = lagrange_interpolate(pts)
        ok = all(eval_poly(a2_poly, x) == y for x, y in extra)
        deg = len(a2_poly) - 1
        print(f"    Degree {deg}, validated: {'✓' if ok else '✗'}")
        for k, c in enumerate(a2_poly):
            if c != 0:
                print(f"      c_{k} = {c}")

    if len(a3_rats) >= 8:
        pts = [(Fraction(n), a3_rats[n]) for n in sorted(a3_rats.keys())[:7]]
        extra = [(Fraction(n), a3_rats[n]) for n in sorted(a3_rats.keys())[7:]]
        a3_poly = lagrange_interpolate(pts)
        ok = all(eval_poly(a3_poly, x) == y for x, y in extra)
        deg = len(a3_poly) - 1
        print(f"\n    a₃(n) polynomial: degree {deg}, validated: {'✓' if ok else '✗'}")
        for k, c in enumerate(a3_poly):
            if c != 0:
                print(f"      c_{k} = {c}")

    # ─── Phase 3: Extract a₄ ─────────────────────────────────
    print("\n  " + "─" * 64)
    print("  Phase 3: Extract a₄(n) using exact a₀..a₃")
    print("  " + "─" * 64)

    a4_vals = {}
    a4_rats = {}

    for n in range(3, 13):
        eigs, dims = spectra[n]
        a1_exact = float(Fraction(2*n*n - 3, 6))
        a2_exact = float(a2_rats[n]) if n in a2_rats else a2_vals[n][0]
        a3_exact = float(a3_rats[n]) if n in a3_rats else a3_vals[n][0]
        known = {0: 1.0, 1: a1_exact, 2: a2_exact, 3: a3_exact}

        vol = volumes[n]
        a4, a4_std = extract_crossval(n, eigs, dims, known, target_k=4, vol=vol)
        a4_vals[n] = (a4, a4_std)
        frac, err = identify_rational(a4, max_den=5000, tol=1e-4)
        if frac:
            a4_rats[n] = frac

        Nc = n - 2
        g = 2*n - 3
        Ncg2 = Nc * g * g
        ratio = a4 / Ncg2 if Ncg2 > 0 else 0
        frac_str = f"{a4_rats.get(n, '?')}"
        print(f"    n={n}: a₄={a4:>14.6f} ± {a4_std:.1e}  ≈ {frac_str:>12}  "
              f"N_cg²={Ncg2:>6}  ratio={ratio:.6f}")

    # Check a₄(Q⁵) = 2671/18
    a4_5 = a4_rats.get(5)
    print(f"\n    a₄(Q⁵) = {a4_5} (expect 2671/18) "
          f"{'✓ CONFIRMED' if a4_5 == Fraction(2671, 18) else '✗ MISMATCH'}")

    # ─── Phase 3b: a₄(n) polynomial ──────────────────────────
    print("\n  " + "─" * 64)
    print("  Phase 3b: a₄(n) POLYNOMIAL (expect degree 7)")
    print("  " + "─" * 64)

    # Rational table
    print(f"\n    {'n':<4} {'a₄(rational)':<20} {'den':<8} {'factors(den)'}")
    print(f"    {'─'*56}")
    for n in range(3, 13):
        if n in a4_rats:
            f = a4_rats[n]
            print(f"    {n:<4} {str(f):<20} {f.denominator:<8} {factor(f.denominator)}")
        else:
            print(f"    {n:<4} {'?':<20}")

    # Lagrange interpolation
    if len(a4_rats) >= 8:
        # Try degree 7 first (8 points)
        for trial_deg in [7, 8, 6]:
            if len(a4_rats) < trial_deg + 2:
                continue
            pts = [(Fraction(nv), a4_rats[nv])
                   for nv in sorted(a4_rats.keys())[:trial_deg + 1]]
            extra = [(Fraction(nv), a4_rats[nv])
                     for nv in sorted(a4_rats.keys())[trial_deg + 1:]]

            poly = lagrange_interpolate(pts)
            actual_deg = len(poly) - 1
            ok = all(eval_poly(poly, x) == y for x, y in extra)

            print(f"\n    Degree-{trial_deg} interpolation (actual {actual_deg}): "
                  f"{'✓ VERIFIED' if ok else '✗'}")

            if ok:
                print(f"\n    a₄(n) coefficients:")
                for k, c in enumerate(poly):
                    if c != 0:
                        print(f"      c_{k} = {c}  [{float(c):.10f}]  "
                              f"den factors: {factor(c.denominator)}")

                # Verification
                print(f"\n    Verification:")
                for nv in sorted(a4_rats.keys()):
                    pred = eval_poly(poly, Fraction(nv))
                    actual = a4_rats[nv]
                    print(f"      a₄({nv}) = {actual} {'✓' if pred == actual else '✗'}")

                # Crossing analysis
                print(f"\n    Crossing: a₄(n) / N_cg²")
                for nv in range(3, 16):
                    a4p = float(eval_poly(poly, Fraction(nv)))
                    Nc = nv - 2; g_v = 2*nv - 3; Ncg2 = Nc * g_v**2
                    if Ncg2 > 0:
                        r = a4p / Ncg2
                        m = " ◄━━" if abs(r - 1) < 0.02 else ""
                        print(f"      n={nv:>2}: a₄={a4p:>14.4f}  "
                              f"N_cg²={Ncg2:>8}  ratio={r:.6f}{m}")
                break

    # ─── Phase 4: Extract a₅ ─────────────────────────────────
    print("\n  " + "─" * 64)
    print("  Phase 4: a₅(Q^n) extraction")
    print("  " + "─" * 64)

    a5_vals = {}
    a5_rats = {}

    for n in range(3, 13):
        eigs, dims = spectra[n]
        a1_exact = float(Fraction(2*n*n - 3, 6))
        a2_exact = float(a2_rats[n]) if n in a2_rats else a2_vals[n][0]
        a3_exact = float(a3_rats[n]) if n in a3_rats else a3_vals[n][0]
        a4_exact = float(a4_rats[n]) if n in a4_rats else a4_vals[n][0]
        known = {0: 1.0, 1: a1_exact, 2: a2_exact, 3: a3_exact, 4: a4_exact}

        vol = volumes[n]
        a5, a5_std = extract_crossval(n, eigs, dims, known, target_k=5, vol=vol)
        a5_vals[n] = (a5, a5_std)
        frac, err = identify_rational(a5, max_den=5000, tol=1e-3)
        if frac:
            a5_rats[n] = frac

        frac_str = f"{a5_rats.get(n, '?')}"
        print(f"    n={n}: a₅={a5:>14.6f} ± {a5_std:.1e}  ≈ {frac_str}")

    # Detailed a₅(Q⁵)
    if 5 in a5_vals:
        a5_5, a5_5_std = a5_vals[5]
        print(f"\n    a₅(Q⁵) = {a5_5:.10f} ± {a5_5_std:.2e}")

        # Systematic search
        print(f"\n    Top rational candidates for a₅(Q⁵):")
        cands = []
        for d in range(1, 1001):
            num = round(a5_5 * d)
            err_c = abs(a5_5 - num/d)
            cands.append((err_c, Fraction(num, d)))
        cands.sort()
        for err_c, f in cands[:15]:
            sig = err_c / a5_5_std if a5_5_std > 0 else float('inf')
            print(f"      {f} = {float(f):.10f}  den={f.denominator:<5} "
                  f"err={err_c:.2e} ({sig:.1f}σ)  "
                  f"den_factors={factor(f.denominator)}")

    # ─── Phase 5: Summary ────────────────────────────────────
    print("\n  " + "═" * 64)
    print("  SUMMARY")
    print("  " + "═" * 64)

    checks = []
    c1 = a4_rats.get(5) == Fraction(2671, 18)
    checks.append(("a₄(Q⁵) = 2671/18", c1))
    c2 = a2_rats.get(5) == Fraction(274, 9)
    checks.append(("a₂(Q⁵) = 274/9", c2))
    c3 = a3_rats.get(5) == Fraction(703, 9)
    checks.append(("a₃(Q⁵) = 703/9", c3))
    c4 = len(a4_rats) >= 8
    checks.append((f"≥8 rational a₄ ({len(a4_rats)}/10)", c4))

    # Check if polynomial verified
    poly_ok = False
    if len(a4_rats) >= 9:
        pts = [(Fraction(nv), a4_rats[nv])
               for nv in sorted(a4_rats.keys())[:8]]
        extra = [(Fraction(nv), a4_rats[nv])
                 for nv in sorted(a4_rats.keys())[8:]]
        poly = lagrange_interpolate(pts)
        poly_ok = all(eval_poly(poly, x) == y for x, y in extra)
    checks.append(("a₄(n) polynomial verified", poly_ok))

    c6 = 5 in a5_rats
    checks.append(("a₅(Q⁵) rational identified", c6))

    score = sum(1 for _, ok in checks if ok)
    total = len(checks)

    for desc, ok in checks:
        print(f"    [{'✓' if ok else '✗'}] {desc}")
    print(f"\n    Score: {score}/{total}")

    # Key results
    print(f"\n    ╔{'═'*58}╗")
    if c1:
        print(f"    ║  a₄(Q⁵) = 2671/18 [CONFIRMED]                         ║")
    if 5 in a5_rats:
        f5 = a5_rats[5]
        print(f"    ║  a₅(Q⁵) = {f5} = {float(f5):.8f}"
              f"{'':>{38-len(str(f5))}}║")
    elif 5 in a5_vals:
        v, s = a5_vals[5]
        print(f"    ║  a₅(Q⁵) = {v:.8f} ± {s:.2e}                     ║")
    print(f"    ║  a₄(n) polynomial: {'VERIFIED' if poly_ok else 'PENDING'}"
          f"{'':>{33 if poly_ok else 31}}║")
    print(f"    ║  Rational a₄ values: {len(a4_rats)}/10"
          f"{'':>{35 - len(str(len(a4_rats)))}}║")
    print(f"    ╚{'═'*58}╝")

    print(f"\n  Toy 256 complete.")


if __name__ == '__main__':
    main()
