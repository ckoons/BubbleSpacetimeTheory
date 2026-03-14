#!/usr/bin/env python3
"""
BST — Full Euler-Maclaurin expansion to arbitrary order
==========================================================
Computes r₃, r₄, r₅, ... from the EM boundary correction.

The key: the integral I(t) = ∫₀^∞ d(x)exp(-x(x+5)t)dx contributes
to r₀, r₁, r₂ only. For k ≥ 3, r_k comes entirely from EM boundary
terms (verified numerically for k=3; check for k=4).

Strategy: expand f(x) = d(x)·exp(-(x²+5x)t) as a bivariate polynomial
in (x, t), read off f^{(2j-1)}(0) as polynomials in t, then sum the
EM formula to get EM(t) as a power series in t.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from fractions import Fraction
from math import comb, factorial
from scipy.integrate import quad


# ═══════════════════════════════════════════════════════════════════
# SETUP: Polynomial multiplication with Fraction coefficients
# ═══════════════════════════════════════════════════════════════════

def poly_mul(a, b):
    """Multiply two polynomials (lists of Fraction coefficients)."""
    if not a or not b:
        return []
    n = len(a) + len(b) - 1
    c = [Fraction(0)] * n
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def poly_add(a, b):
    """Add two polynomials."""
    n = max(len(a), len(b))
    c = [Fraction(0)] * n
    for i, ai in enumerate(a):
        c[i] += ai
    for i, bi in enumerate(b):
        c[i] += bi
    return c


def poly_scale(a, s):
    """Scale polynomial by Fraction s."""
    return [s * ai for ai in a]


# ═══════════════════════════════════════════════════════════════════
# EXPAND φ(x) = exp(-(x²+5x)t) as bivariate Taylor series
# ═══════════════════════════════════════════════════════════════════

def compute_phi_coeffs(max_x_order, max_t_order):
    """
    Compute [x^m] φ(x) as polynomials in t, for m = 0, ..., max_x_order.

    φ(x) = exp(ux + vx²) where u = -5t, v = -t.
    (ux + vx²)^n = Σ_k C(n,k) u^k v^{n-k} x^{k+2(n-k)} = Σ_k C(n,k) u^k v^{n-k} x^{2n-k}

    [x^m] φ = Σ_n 1/n! C(n, 2n-m) u^{2n-m} v^{m-n}
    where ⌈m/2⌉ ≤ n ≤ m.

    u^{2n-m} = (-5t)^{2n-m} = (-5)^{2n-m} t^{2n-m}
    v^{m-n} = (-t)^{m-n} = (-1)^{m-n} t^{m-n}

    Total t power: (2n-m) + (m-n) = n.
    """
    phi = []
    for m in range(max_x_order + 1):
        # [x^m] φ is a polynomial in t
        coeffs_t = [Fraction(0)] * (max_t_order + 1)
        for n in range((m + 1) // 2, m + 1):
            k = 2 * n - m
            if k < 0 or k > n:
                continue
            # Contribution: (1/n!) C(n,k) (-5)^k (-1)^{m-n} t^n
            binom = Fraction(comb(n, k))
            sign = (-1)**k * 5**k * (-1)**(m - n)
            # Actually: u^k = (-5t)^k = (-5)^k t^k
            # v^{m-n} = (-t)^{m-n} = (-1)^{m-n} t^{m-n}
            coeff = Fraction(1, factorial(n)) * binom * Fraction(sign)
            t_power = n
            if t_power <= max_t_order:
                coeffs_t[t_power] += coeff
        phi.append(coeffs_t[:max_t_order + 1])
    return phi


def main():
    print()
    print("  ══════════════════════════════════════════════════════════")
    print("  FULL EM EXPANSION: r₃, r₄, r₅, r₆")
    print("  ══════════════════════════════════════════════════════════")

    # Degeneracy polynomial coefficients: d(x) = Σ d_j x^j / j!
    # d(x) = (2x⁵ + 25x⁴ + 120x³ + 275x² + 298x + 120)/120
    d_poly_raw = [Fraction(120), Fraction(298), Fraction(275),
                  Fraction(120), Fraction(25), Fraction(2)]
    d_poly = [c / 120 for c in d_poly_raw]
    # d_poly[j] = [x^j] d(x)

    print(f"  d(x) = {' + '.join(f'({c})x^{j}' for j, c in enumerate(d_poly) if c != 0)}")

    # Verify d_poly
    assert d_poly[0] == Fraction(1)
    assert d_poly[1] == Fraction(149, 60)
    print(f"  d₀ = {d_poly[0]}, d₁ = {d_poly[1]}")

    # ──────────────────────────────────────────────────────
    # Compute φ(x) = exp(-(x²+5x)t) Taylor coefficients
    # ──────────────────────────────────────────────────────
    max_x = 11   # Need up to x^11 for f^(11)(0)
    max_t = 6    # Need up to t^6 for r₆+₃ = r₉... actually r₃+k where k is t order
    # For r_{3+k}, we need EM(t) to O(t^k), which requires
    # f^{(2j-1)}(0) to O(t^k). f^{(n)}(0) = n! × [x^n]f.
    # [x^n]f = Σ d_j × φ_{n-j}. Each φ_{n-j} is a polynomial in t.

    phi = compute_phi_coeffs(max_x, max_t)

    print(f"\n  φ coefficients (first few):")
    labels = ["φ₀", "φ₁", "φ₂", "φ₃", "φ₄", "φ₅"]
    for m in range(min(6, len(phi))):
        terms = []
        for p, c in enumerate(phi[m]):
            if c != 0:
                if p == 0:
                    terms.append(f"{c}")
                else:
                    terms.append(f"({c})t^{p}")
        print(f"    {labels[m]} = {' + '.join(terms)}")

    # ──────────────────────────────────────────────────────
    # Compute [x^n]f = Σ_{j=0}^{min(n,5)} d_j × φ_{n-j}
    # as polynomial in t
    # ──────────────────────────────────────────────────────
    f_x_coeffs = []  # f_x_coeffs[n] = [x^n]f as list of Fraction (poly in t)
    for n in range(max_x + 1):
        result = [Fraction(0)] * (max_t + 1)
        for j in range(min(n + 1, len(d_poly))):
            # Add d_poly[j] × phi[n-j]
            for p in range(max_t + 1):
                if n - j < len(phi) and p < len(phi[n - j]):
                    result[p] += d_poly[j] * phi[n - j][p]
        f_x_coeffs.append(result)

    # f^{(n)}(0) = n! × [x^n]f
    f_deriv_at_0 = []
    for n in range(max_x + 1):
        f_deriv_at_0.append([Fraction(factorial(n)) * c for c in f_x_coeffs[n]])

    print(f"\n  Key derivatives f^{{(n)}}(0) as polynomials in t:")
    for n in [1, 3, 5, 7, 9]:
        if n < len(f_deriv_at_0):
            terms = []
            for p, c in enumerate(f_deriv_at_0[n]):
                if c != 0:
                    if p == 0:
                        terms.append(f"{c}")
                    else:
                        terms.append(f"({c})t^{p}")
            print(f"    f^({n})(0) = {' + '.join(terms[:4])} + ...")

    # ──────────────────────────────────────────────────────
    # Euler-Maclaurin formula
    # EM(t) = f(0)/2 - Σ_{j≥1} B_{2j}/(2j)! f^{(2j-1)}(0)
    # ──────────────────────────────────────────────────────
    # Bernoulli numbers (exact):
    B = {2: Fraction(1, 6), 4: Fraction(-1, 30), 6: Fraction(1, 42),
         8: Fraction(-1, 30), 10: Fraction(5, 66), 12: Fraction(-691, 2730)}

    # f(0) = d(0) × φ(0) = 1 (all t)
    # f(0)/2 = 1/2

    em_poly = [Fraction(0)] * (max_t + 1)
    em_poly[0] = Fraction(1, 2)  # f(0)/2

    print(f"\n  EM boundary terms:")
    print(f"    f(0)/2 = 1/2")

    for j in range(1, 6):  # j = 1,2,3,4,5 → f',f''',f⁵,f⁷,f⁹
        n = 2 * j - 1
        if n >= len(f_deriv_at_0):
            break
        coeff = -B[2 * j] / Fraction(factorial(2 * j))
        # EM contribution: coeff × f^{(n)}(0) (poly in t)
        f_n = f_deriv_at_0[n]
        label = f"-B_{{{2*j}}}/{{{2*j}}}! × f^({n})(0)"
        val_at_0 = coeff * f_n[0]
        print(f"    {label}: coeff = {coeff}, "
              f"f^({n})(0)|_{{t=0}} = {f_n[0]}, "
              f"product|_{{t=0}} = {val_at_0} = {float(val_at_0):.8f}")

        for p in range(max_t + 1):
            if p < len(f_n):
                em_poly[p] += coeff * f_n[p]

    print(f"\n  ══════════════════════════════════════════════════════════")
    print(f"  EM(t) = Σ EM_k t^k:")
    print(f"  ══════════════════════════════════════════════════════════")
    for k in range(max_t + 1):
        rk = 60 * em_poly[k]
        print(f"    EM_{k} = {em_poly[k]} = {float(em_poly[k]):.12f}"
              f"    →  r_{{{k+3}}} = {rk} = {float(rk):.10f}")

    # ──────────────────────────────────────────────────────
    # r_k table (assuming c_k^I = 0 for k ≥ 3)
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════════")
    print(f"  COEFFICIENT TABLE (from integral + EM)")
    print(f"  ══════════════════════════════════════════════════════════")
    print(f"    r₀ = 1         (from integral)")
    print(f"    r₁ = 5         (from integral)")
    print(f"    r₂ = 12        (from integral)")

    r_vals = {}
    for k in range(max_t + 1):
        rk = 60 * em_poly[k]
        r_vals[k + 3] = rk
        print(f"    r_{k+3} = {rk} = {float(rk):.10f}")

    # ──────────────────────────────────────────────────────
    # NUMERICAL VERIFICATION of r₃, r₄, r₅
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════════")
    print(f"  NUMERICAL VERIFICATION")
    print(f"  ══════════════════════════════════════════════════════════")

    def d_func(k):
        return comb(k + 4, 4) * (2 * k + 5) // 5

    def Z0(t, K_max=3000):
        total = 0.0
        for k in range(K_max + 1):
            lam = k * (k + 5)
            if lam * t > 250:
                break
            total += d_func(k) * np.exp(-lam * t)
        return total

    b = [Fraction(1, 60), Fraction(1, 12), Fraction(1, 5)]  # b₀, b₁, b₂ exact
    for k in range(max_t + 1):
        b.append(em_poly[k])  # b₃ = EM₀, b₄ = EM₁, ...

    # For each r_k with k ≥ 3, verify by direct subtraction
    for target_k in [3, 4, 5, 6]:
        if target_k >= len(b):
            break
        print(f"\n  r_{target_k} = {r_vals.get(target_k, '?')} = "
              f"{float(r_vals.get(target_k, 0)):.10f}")

        def gk(t, kk=target_k):
            z = t**3 * Z0(t)
            for j in range(kk):
                z -= float(b[j]) * t**j
            return z / t**kk

        print(f"    t        g_k(t)        60*g_k(t)     "
              f"error from exact")
        for t in [0.02, 0.01, 0.005, 0.002, 0.001]:
            val = gk(t)
            exact = float(r_vals.get(target_k, 0)) / 60
            err = abs(val - exact)
            print(f"    {t:.3f}    {val:.12f}  {60*val:.8f}  "
              f"{err:.2e}")

    # ──────────────────────────────────────────────────────
    # Verify c_k^I = 0 for k ≥ 3
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════════")
    print(f"  VERIFY: integral contributes 0 for k ≥ 3")
    print(f"  ══════════════════════════════════════════════════════════")

    def integrand(x, t):
        d = (x+1)*(x+2)*(x+3)*(x+4)*(2*x+5)/120
        return d * np.exp(-x*(x+5)*t)

    for target_k in [3, 4, 5]:
        print(f"\n  c_{target_k}^I = [t³I(t) - Σ_{0}^{{{target_k-1}}} "
              f"c_j^I t^j] / t^{target_k}")
        # c_0^I = 1/60, c_1^I = 5/60, c_2^I = 12/60 (known)
        c_I = [Fraction(1, 60), Fraction(5, 60), Fraction(12, 60)]

        for t in [0.01, 0.005, 0.002, 0.001]:
            I_val, _ = quad(integrand, 0, np.inf, args=(t,))
            t3I = t**3 * I_val
            subtracted = t3I
            for j in range(min(target_k, len(c_I))):
                subtracted -= float(c_I[j]) * t**j
            ck_est = subtracted / t**target_k
            print(f"    t={t:.3f}: c_{target_k}^I ≈ {ck_est:.2e}")

    # ──────────────────────────────────────────────────────
    # BST analysis of the rational coefficients
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════════")
    print(f"  BST PATTERN ANALYSIS")
    print(f"  ══════════════════════════════════════════════════════════")
    rk_list = [(0, Fraction(1)), (1, Fraction(5)), (2, Fraction(12))]
    for k in range(max_t + 1):
        rk_list.append((k + 3, r_vals[k + 3]))

    for k, rk in rk_list:
        print(f"    r_{k} = {rk} = {float(rk):.10f}")

    # Check ratios r_{k+1}/r_k
    print(f"\n  Ratios r_{{k+1}}/r_k:")
    for i in range(len(rk_list) - 1):
        k1, r1 = rk_list[i]
        k2, r2 = rk_list[i + 1]
        if r1 != 0:
            ratio = r2 / r1
            print(f"    r_{k2}/r_{k1} = {ratio} = {float(ratio):.8f}")

    # Check if r_k/k! has pattern
    print(f"\n  r_k/k!:")
    for k, rk in rk_list:
        if k > 0:
            val = rk / factorial(k)
            print(f"    r_{k}/{k}! = {val} = {float(val):.10f}")


if __name__ == '__main__':
    main()
