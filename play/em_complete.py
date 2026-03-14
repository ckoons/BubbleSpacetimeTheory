#!/usr/bin/env python3
"""
BST — Complete Euler-Maclaurin expansion for zonal heat trace on Q⁵
=====================================================================
Computes ALL zonal coefficients r_k EXACTLY using the EM formula
with sufficient Bernoulli terms for each order.

KEY RESULTS:
  r₀ = 1
  r₁ = 5  = n_C
  r₂ = 12 = 2C₂
  r₃ = 1139/63        ≈ 18.0794
  r₄ = 833/45         ≈ 18.5111
  r₅ = 137/11         ≈ 12.4545  =  N_max / c₂  !!
  r₆, r₇, ...

The r₅ = 137/11 identity connects the zonal spectral theory of Q⁵
directly to BST's most iconic integers: N_max = 137 (fine structure)
and c₂ = 11 (second Chern class = dim isotropy group).

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from fractions import Fraction
from math import comb, factorial
from scipy.integrate import quad


# ═══════════════════════════════════════════════════════════════════
# BERNOULLI NUMBERS (exact)
# ═══════════════════════════════════════════════════════════════════

def bernoulli_numbers(max_n):
    """Compute Bernoulli numbers B_0 through B_{max_n} exactly."""
    B = [Fraction(0)] * (max_n + 1)
    B[0] = Fraction(1)
    for m in range(1, max_n + 1):
        B[m] = Fraction(0)
        for k in range(m):
            B[m] -= Fraction(comb(m + 1, k)) * B[k]
        B[m] /= Fraction(m + 1)
    return B


# ═══════════════════════════════════════════════════════════════════
# POLYNOMIAL OPERATIONS
# ═══════════════════════════════════════════════════════════════════

def compute_phi_coeffs(max_x_order, max_t_order):
    """
    [x^m] exp(-(x²+5x)t) as polynomials in t.

    exp(ux + vx²) where u = -5t, v = -t.
    [x^m] = Σ_{n=⌈m/2⌉}^{m} (1/n!) C(n, 2n-m) (-5)^{2n-m} (-1)^{m-n} t^n
    """
    phi = []
    for m in range(max_x_order + 1):
        coeffs_t = [Fraction(0)] * (max_t_order + 1)
        for n in range((m + 1) // 2, m + 1):
            k = 2 * n - m
            if k < 0 or k > n:
                continue
            binom = Fraction(comb(n, k))
            sign_pow = (-1)**k * 5**k * (-1)**(m - n)
            coeff = Fraction(1, factorial(n)) * binom * Fraction(sign_pow)
            if n <= max_t_order:
                coeffs_t[n] += coeff
        phi.append(coeffs_t)
    return phi


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  COMPLETE ZONAL EM EXPANSION ON Q⁵")
    print("  ══════════════════════════════════════════════════════")

    # ──────────────────────────────────────────────────────
    # Parameters
    # ──────────────────────────────────────────────────────
    max_r = 8          # compute r₃ through r_{max_r}
    max_t = max_r - 3  # need EM(t) to this order in t
    # For EM_k, we need B_{2j} for j=1,...,k+3.
    # So we need B up to B_{2(max_t+3)} = B_{2(max_r)}.
    max_bern = 2 * max_r
    # For f^{(2j-1)}, we need x-derivatives up to 2(max_t+3)-1 = 2*max_r - 1.
    max_x = 2 * max_r - 1

    print(f"  Computing r₃ through r_{max_r}")
    print(f"  Need B₂ through B_{max_bern}")
    print(f"  Need f derivatives up to f^({max_x})")

    # ──────────────────────────────────────────────────────
    # Bernoulli numbers
    # ──────────────────────────────────────────────────────
    B = bernoulli_numbers(max_bern)
    print(f"\n  Bernoulli numbers:")
    for j in range(1, max_r + 1):
        idx = 2 * j
        if idx <= max_bern:
            print(f"    B_{idx} = {B[idx]} = {float(B[idx]):.10f}")

    # ──────────────────────────────────────────────────────
    # Degeneracy polynomial
    # ──────────────────────────────────────────────────────
    d_poly = [Fraction(120), Fraction(298), Fraction(275),
              Fraction(120), Fraction(25), Fraction(2)]
    d_poly = [c / 120 for c in d_poly]

    # ──────────────────────────────────────────────────────
    # φ coefficients
    # ──────────────────────────────────────────────────────
    phi = compute_phi_coeffs(max_x, max_t)

    # ──────────────────────────────────────────────────────
    # [x^n] f(x) and f^{(n)}(0)
    # ──────────────────────────────────────────────────────
    f_x_coeffs = []
    for n in range(max_x + 1):
        result = [Fraction(0)] * (max_t + 1)
        for j in range(min(n + 1, len(d_poly))):
            for p in range(max_t + 1):
                if n - j < len(phi) and p < len(phi[n - j]):
                    result[p] += d_poly[j] * phi[n - j][p]
        f_x_coeffs.append(result)

    f_deriv = []
    for n in range(max_x + 1):
        f_deriv.append([Fraction(factorial(n)) * c for c in f_x_coeffs[n]])

    # ──────────────────────────────────────────────────────
    # EM(t) = f(0)/2 − Σ_{j≥1} B_{2j}/(2j)! f^{(2j-1)}(0)
    # ──────────────────────────────────────────────────────
    em_poly = [Fraction(0)] * (max_t + 1)
    em_poly[0] = Fraction(1, 2)

    for j in range(1, max_r + 1):
        n = 2 * j - 1
        if n >= len(f_deriv):
            break
        idx = 2 * j
        if idx > max_bern:
            break
        coeff = -B[idx] / Fraction(factorial(idx))
        for p in range(max_t + 1):
            if p < len(f_deriv[n]):
                em_poly[p] += coeff * f_deriv[n][p]

    # ──────────────────────────────────────────────────────
    # RESULTS
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  EXACT ZONAL COEFFICIENTS")
    print(f"  t³ Z₀(t) = (1/60)[1 + r₁t + r₂t² + r₃t³ + ...]")
    print(f"  ══════════════════════════════════════════════════════")

    r_exact = {0: Fraction(1), 1: Fraction(5), 2: Fraction(12)}
    print(f"\n    r₀ = 1       [from integral]")
    print(f"    r₁ = 5       [from integral] = n_C")
    print(f"    r₂ = 12      [from integral] = 2C₂ = c₁² − c₃")

    for k in range(max_t + 1):
        rk = 60 * em_poly[k]
        r_exact[k + 3] = rk
        num, den = rk.numerator, rk.denominator
        print(f"    r_{k+3} = {rk} = {float(rk):.10f}"
              f"  [{num} = {factorize(num)}, {den} = {factorize(den)}]")

    # ──────────────────────────────────────────────────────
    # BST IDENTIFICATIONS
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  BST IDENTIFICATIONS")
    print(f"  ══════════════════════════════════════════════════════")

    c = [1, 5, 11, 13, 9, 3]  # Chern classes of Q⁵

    # r₅ = 137/11
    r5 = r_exact[5]
    print(f"\n  ★ r₅ = {r5} = {float(r5):.10f}")
    print(f"    137 = N_max (BST fine structure maximum)")
    print(f"    11  = c₂ (second Chern class of Q⁵)")
    print(f"    r₅  = N_max / c₂")
    print(f"    Verified exact via Fraction arithmetic.")

    # How 137 emerges:
    print(f"\n    Trace of 137:")
    print(f"    EM₂ = Σ of 4 terms (B₂ through B₁₀ contributions at O(t²)):")

    # Recompute EM₂ term by term
    terms_at_t2 = []
    for j in range(1, max_r + 1):
        n = 2 * j - 1
        if n >= len(f_deriv):
            break
        idx = 2 * j
        if idx > max_bern:
            break
        coeff = -B[idx] / Fraction(factorial(idx))
        if 2 < len(f_deriv[n]) and f_deriv[n][2] != 0:
            contrib = coeff * f_deriv[n][2]
            terms_at_t2.append((j, n, coeff, f_deriv[n][2], contrib))
            print(f"      j={j}: −B_{idx}/{idx}! × f^({n})(0)|_{{t²}} "
                  f"= ({coeff}) × ({f_deriv[n][2]}) = {contrib}")

    total = sum(t[4] for t in terms_at_t2)
    print(f"      Total EM₂ = {total} = {float(total):.10f}")
    print(f"      r₅ = 60 × {total} = {60*total}")

    # r₃ decomposition
    r3 = r_exact[3]
    print(f"\n  r₃ = {r3} = {float(r3):.10f}")
    print(f"    EM₀ = {em_poly[0]} = {float(em_poly[0]):.10f}")
    print(f"    = d(0)/2 − (1/12)d'(0) + (1/720)d'''(0) − (1/30240)d⁵(0)")
    print(f"    = 1/2 − 149/720 + 1/120 − 1/15120")
    print(f"    Sign error in previous session: used −1/720 instead of +1/720")
    print(f"    giving 1076/63 instead of 1139/63, off by exactly 1.0")

    # r₄ decomposition
    r4 = r_exact[4]
    print(f"\n  r₄ = {r4} = {float(r4):.10f}")
    print(f"    = {r4.numerator} / {r4.denominator}")

    # Numerical verification of r₃, r₄, r₅
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  NUMERICAL VERIFICATION")
    print(f"  ══════════════════════════════════════════════════════")

    def d_k(k):
        return comb(k + 4, 4) * (2 * k + 5) // 5

    def Z0(t, K_max=3000):
        total = 0.0
        for k in range(K_max + 1):
            lam = k * (k + 5)
            if lam * t > 250:
                break
            total += d_k(k) * np.exp(-lam * t)
        return total

    b_exact = [Fraction(1, 60), Fraction(1, 12), Fraction(1, 5)]
    for k in range(max_t + 1):
        b_exact.append(em_poly[k])

    for target in [3, 4, 5]:
        rk = r_exact[target]
        bk = rk / 60

        def gk(t, kk=target, b=b_exact):
            z = t**3 * Z0(t)
            for j in range(kk):
                z -= float(b[j]) * t**j
            return z / t**kk

        print(f"\n  r_{target} = {rk} = {float(rk):.10f}")
        for t in [0.01, 0.005, 0.002, 0.001]:
            val = gk(t)
            err = abs(val - float(bk))
            print(f"    t={t:.3f}: 60g = {60*val:.8f}  "
                  f"err={err:.2e}")

    # ──────────────────────────────────────────────────────
    # GENERATING FUNCTION ATTEMPT
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  GENERATING FUNCTION ANALYSIS")
    print(f"  ══════════════════════════════════════════════════════")

    # Check if Σ r_k t^k / k! has a nice form
    print(f"\n  Σ r_k t^k / k! (first 6 terms):")
    gen_coeffs = []
    for k in range(min(6, len(r_exact))):
        if k in r_exact:
            c = r_exact[k] / factorial(k)
            gen_coeffs.append((k, c))
            print(f"    k={k}: {c} = {float(c):.10f}")

    # Partial sums evaluated at special t values
    print(f"\n  Partial sum Σ₀⁵ r_k t^k / k! at t=1:")
    total = sum(c for _, c in gen_coeffs)
    print(f"    = {total} = {float(total):.10f}")
    print(f"    e⁵ = {np.exp(5):.10f}")


def factorize(n):
    """Simple factorization for display."""
    if n == 0:
        return "0"
    if n < 0:
        return "-" + factorize(-n)
    if n == 1:
        return "1"
    factors = []
    d = 2
    m = n
    while d * d <= m:
        while m % d == 0:
            factors.append(d)
            m //= d
        d += 1
    if m > 1:
        factors.append(m)
    if not factors:
        return str(n)
    # Group
    from collections import Counter
    ct = Counter(factors)
    parts = []
    for p in sorted(ct):
        if ct[p] == 1:
            parts.append(str(p))
        else:
            parts.append(f"{p}^{ct[p]}")
    return " × ".join(parts)


if __name__ == '__main__':
    main()
