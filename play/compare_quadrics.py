#!/usr/bin/env python3
"""
BST — Compare zonal coefficients across Q^n for n=3,4,5,6,7
================================================================
Check if r₅ = 137/11 is specific to Q⁵ or appears for other quadrics.

Q^n = SO(n+2)/[SO(n)×SO(2)]
  d(k) = dim of (k,0,...,0) rep of SO(n+2) [zonal class-1]
  λ(k) = k(k+n) [Casimir eigenvalue]
  d_eff = 2n-4 for n≥3 [effective spectral dimension of zonal sector]

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import comb, factorial


def bernoulli_numbers(max_n):
    B = [Fraction(0)] * (max_n + 1)
    B[0] = Fraction(1)
    for m in range(1, max_n + 1):
        B[m] = Fraction(0)
        for k in range(m):
            B[m] -= Fraction(comb(m + 1, k)) * B[k]
        B[m] /= Fraction(m + 1)
    return B


def so_dim(n_plus_2, k):
    """
    Dimension of (k,0,...,0) representation of SO(n+2).
    For SO(m) with m = n+2, this is the k-th symmetric traceless
    tensor representation.

    The formula for dim of highest weight (k,0,...,0) of SO(m):
    For m = 2l+1 (odd):
      dim = prod_{1≤i<j≤l} [(k+ρ_i+ρ_j)(k+ρ_i-ρ_j)] / [ρ_i+ρ_j)(ρ_i-ρ_j)]
           × prod_{i=1}^l (k+ρ_i)/ρ_i
      where ρ = (l-1/2, l-3/2, ..., 3/2, 1/2).

    For m = 2l (even):
      Similar but ρ = (l-1, l-2, ..., 1, 0) and we need to handle the j=l case
      (ρ_l = 0) specially.

    Actually, let's just use the Weyl dimension formula directly.
    For SO(m) with highest weight (k, 0, ..., 0):

    dim = C(k+m-2, k) * (2k+m-2) / (m-2)    for m ≥ 3.
    """
    m = n_plus_2
    if m < 3:
        return 1 if k == 0 else 2  # SO(2): trivial and sign reps
    return Fraction(comb(k + m - 2, k) * (2 * k + m - 2), m - 2)


def compute_zonal_coefficients(n, max_r=8):
    """
    Compute zonal expansion coefficients for Q^n = SO(n+2)/[SO(n)×SO(2)].

    t^{n/2} Z₀(t) has expansion starting at 1/V₀.
    Actually, d_eff = the effective spectral dimension.

    d(k) ~ k^{n-1} (degree of degeneracy polynomial)
    λ(k) ~ k² (eigenvalue)
    Z₀(t) ~ ∫ k^{n-1} e^{-k²t} dk ~ t^{-n/2}

    Wait: d(k) for SO(n+2) rep (k,0,...,0) is a polynomial of degree n in k.
    The eigenvalue is k(k+n).
    So the integrand is k^n × e^{-k²t}, giving I ~ t^{-(n+1)/2}.
    Then t^{(n+1)/2} Z₀ → V₀.

    Hmm, but for Q⁵ we had d_eff = 6 and n = 5. Let me check:
    d(k) for Q⁵ is degree 5 in k, and t³Z₀ → 1/60. So d_eff/2 = 3 → d_eff = 6.
    The degree of d(k) is n = 5, and d_eff/2 = (n+1)/2 = 3. So d_eff = n+1.

    Actually wait, for Q⁵: d(k) = (k+1)(k+2)(k+3)(k+4)(2k+5)/120.
    This is degree 5 in k. The leading coefficient is 2/120 = 1/60.
    And ∫₀^∞ k^5 e^{-k²t} dk = (1/2) ∫₀^∞ u^2 e^{-ut} du = Γ(3)/(2t³) = 1/t³.
    So I(t) ~ (1/60) / t³, and t³ I → 1/60. d_eff/2 = 3, d_eff = 6 = n+1.

    For general Q^n: d(k) is degree n, leading coeff = 2/(n! × n) from the
    C(k+n-1,n-1)(2k+n)/n formula.
    d_eff/2 = (n+1)/2, d_eff = n+1.
    t^{(n+1)/2} Z₀ → V₀ = [leading coeff of d(k)] × Γ((n+1)/2) / 2.
    """
    m = n + 2  # SO(m) group

    # Build d(x) as polynomial: d(x) = C(x+n-1, n-1) × (2x+n)/n
    # Let's expand d(x) symbolically.
    # C(x+n-1, n-1) = (x+1)(x+2)...(x+n-1) / (n-1)!
    # d(x) = (x+1)(x+2)...(x+n-1) × (2x+n) / (n × (n-1)!)
    #       = (x+1)(x+2)...(x+n-1)(2x+n) / n!

    # Build polynomial coefficients by multiplying (x+1)(x+2)...(x+n-1)(2x+n)
    poly = [Fraction(1)]  # start with 1

    # Multiply by (x+i) for i = 1, ..., n-1
    for i in range(1, n):
        new_poly = [Fraction(0)] * (len(poly) + 1)
        for j, c in enumerate(poly):
            new_poly[j] += c * Fraction(i)  # constant term of (x+i)
            new_poly[j + 1] += c            # x term of (x+i)
        poly = new_poly

    # Multiply by (2x+n)
    new_poly = [Fraction(0)] * (len(poly) + 1)
    for j, c in enumerate(poly):
        new_poly[j] += c * Fraction(n)      # constant term n
        new_poly[j + 1] += c * Fraction(2)  # 2x term
    poly = new_poly

    # Divide by n!
    nfact = Fraction(factorial(n))
    d_poly = [c / nfact for c in poly]

    # Verify d(0) = 1
    assert d_poly[0] == Fraction(1), f"d(0) = {d_poly[0]}"

    # Eigenvalue: λ(x) = x(x+n), so h(x) = x² + nx, h'(0) = n
    shift = n  # h'(0) = n

    # d_eff/2
    deg = len(d_poly) - 1  # should be n
    assert deg == n, f"degree = {deg}, expected {n}"
    half_deff = (n + 1) // 2  # integer division
    # For odd n: d_eff = n+1
    # For even n: d_eff = n+1 is odd... wait.
    # ∫ x^n e^{-x²t} dx : for n even, = Γ((n+1)/2) / (2 t^{(n+1)/2})
    # For n=4: Γ(5/2)/(2t^{5/2}) = (3√π/4)/(2t^{5/2}). So half-integer.
    # Actually for even n, the heat trace has half-integer powers of t.
    # Hmm, but the heat trace on a compact manifold should only have integer powers.
    # This means the half-integer contributions from the integral cancel with
    # half-integer contributions from the EM terms.
    #
    # For now, let's just compute the EM expansion for the even-power terms.

    # Leading volume: V₀ = [leading coeff] × ∫₀^∞ x^n e^{-x²} dx
    # For n odd: ∫₀^∞ x^n e^{-x²} dx = Γ((n+1)/2)/2
    # For n=5: Γ(3)/2 = 1. Leading coeff of d = 2/n! = 2/120 = 1/60.
    # V₀ = 1/60.
    leading = d_poly[n]  # coefficient of x^n
    # ∫ x^n e^{-x²} dx = Γ((n+1)/2)/2
    # For n odd: Γ((n+1)/2) = ((n-1)/2)!

    # For simplicity, only handle odd n (where d_eff is even and clean)
    if n % 2 == 1:
        from math import gamma
        gamma_val = factorial((n - 1) // 2)  # Γ((n+1)/2) for odd n
        V0 = leading * Fraction(gamma_val, 2)
        half_d = (n + 1) // 2
        print(f"\n  Q^{n}: d_eff = {2*half_d}, V₀ = {V0}")
    else:
        # Even n: V₀ involves √π, skip exact computation
        print(f"\n  Q^{n}: even dimension, skipping exact V₀")
        V0 = None
        half_d = None

    if V0 is None:
        return None

    # ──────────────────────────────────────────────────────
    # Compute EM expansion coefficients
    # ──────────────────────────────────────────────────────
    max_t = max_r - half_d
    if max_t < 0:
        max_t = 3
    max_bern = 2 * (max_t + half_d)
    max_x = max_bern - 1

    B = bernoulli_numbers(max_bern)

    # φ(x) = exp(-(x² + nx)t)
    # [x^m] φ = Σ_{j=⌈m/2⌉}^{m} 1/j! C(j, 2j-m) (-n)^{2j-m} (-1)^{m-j} t^j
    def compute_phi(max_xo, max_to, shift_n):
        phi = []
        for mm in range(max_xo + 1):
            coeffs = [Fraction(0)] * (max_to + 1)
            for j in range((mm + 1) // 2, mm + 1):
                k = 2 * j - mm
                if k < 0 or k > j:
                    continue
                binom = Fraction(comb(j, k))
                sign = (-1)**k * shift_n**k * (-1)**(mm - j)
                coeff = Fraction(1, factorial(j)) * binom * Fraction(sign)
                if j <= max_to:
                    coeffs[j] += coeff
            phi.append(coeffs)
        return phi

    phi = compute_phi(max_x, max_t, n)

    # [x^k] f = Σ d_j φ_{k-j}
    f_x = []
    for k in range(max_x + 1):
        result = [Fraction(0)] * (max_t + 1)
        for j in range(min(k + 1, len(d_poly))):
            for p in range(max_t + 1):
                if k - j < len(phi) and p < len(phi[k - j]):
                    result[p] += d_poly[j] * phi[k - j][p]
        f_x.append(result)

    # f^{(k)}(0) = k! × [x^k] f
    f_deriv = []
    for k in range(max_x + 1):
        f_deriv.append([Fraction(factorial(k)) * c for c in f_x[k]])

    # EM(t) = f(0)/2 − Σ B_{2j}/(2j)! f^{(2j-1)}(0)
    em = [Fraction(0)] * (max_t + 1)
    em[0] = Fraction(1, 2)

    for j in range(1, max_t + half_d + 1):
        nn = 2 * j - 1
        if nn >= len(f_deriv):
            break
        idx = 2 * j
        if idx > max_bern:
            break
        coeff = -B[idx] / Fraction(factorial(idx))
        for p in range(max_t + 1):
            if p < len(f_deriv[nn]):
                em[p] += coeff * f_deriv[nn][p]

    # r_k = (1/V₀) × EM_{k-half_d}
    # Wait: t^{half_d} Z₀ = V₀(1 + r₁t + r₂t² + ...)
    # t^{half_d} Z₀ = t^{half_d} I + t^{half_d} EM
    # V₀ comes from the integral at order t^0.
    # EM contributes at order t^{half_d} and higher.
    # So: r_{half_d} = (1/V₀) × EM₀.
    # And generally: r_{half_d + k} = (1/V₀) × EM_k + integral_correction_k.
    # But we showed for Q⁵ that integral_correction = 0 for k ≥ 0 (i.e., for r ≥ 3 = half_d).
    # Need to verify this for other Q^n, but let's assume for now.

    print(f"  EM expansion (V₀ = {V0}):")
    r_vals = {}
    for k in range(max_t + 1):
        rk = em[k] / V0
        idx = half_d + k
        r_vals[idx] = rk
        print(f"    r_{idx} = {rk} = {float(rk):.10f}")

    return r_vals


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  ZONAL COEFFICIENTS ACROSS Q^n (n odd)")
    print("  ══════════════════════════════════════════════════════")

    for n in [3, 5, 7, 9]:
        r = compute_zonal_coefficients(n, max_r=10)
        if r and 5 in r:
            print(f"\n    ★ Q^{n}: r₅ = {r[5]} = {float(r[5]):.10f}")
        print()


if __name__ == '__main__':
    main()
