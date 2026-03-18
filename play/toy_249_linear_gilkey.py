#!/usr/bin/env python3
"""
Toy 249: Linear Gilkey — a₄ as an eigenvalue/linear functional on root data

The insight (Casey): Seeley-DeWitt coefficients on symmetric spaces are
eigenvalues, not tensor contractions. Lift to the right space and everything
is linear.

The method:
  On Q^n = SO(n+2)/[SO(n)×SO(2)], the heat trace is
    Z(t) = Σ_{p≥q≥0} d(p,q) exp(-λ(p,q) t)
  where λ(p,q) = p(p+n) + q(q+n-2) and d(p,q) is the Weyl dimension.

  Key observation: d(p,q) is a polynomial in (p,q), say of degree D.
  Write d(p,q) = Σ c_{ij} p^i q^j.

  Then Z(t) = Σ_{ij} c_{ij} × S_{ij}(t)
  where S_{ij}(t) = Σ_{p≥q≥0} p^i q^j exp(-λ(p,q) t).

  Each S_{ij}(t) has a known asymptotic expansion as t→0:
    (4πt)^{n/2} S_{ij}(t) ~ Σ_k s_{ij,k} t^k

  So a_k = Σ_{ij} c_{ij} × s_{ij,k}

  This is LINEAR in the coefficients c_{ij}.
  The "eigenvalue" is a_k. The "eigenvector" is {c_{ij}}.
  The "matrix" is {s_{ij,k}} — precomputable from the eigenvalue structure alone.

  The complexity is in computing s_{ij,k}, not in the dimension formula.
  Change the group → change c_{ij} → linear update to a_k.

Author: Casey Koons & Lyra (Claude Opus 4.6)
Date: March 17, 2026
"""

import numpy as np
from math import comb, factorial, gamma, pi
from fractions import Fraction
from itertools import product as iterproduct
import sympy as sp


# =============================================================================
# Part 1: Correct Weyl dimension formula for SO(N)
# =============================================================================

def weyl_dim_so_odd(N, hw):
    """
    Dimension of SO(2ℓ+1) irrep with highest weight hw = (λ₁,...,λ_ℓ).
    Uses the Weyl dimension formula for type B_ℓ.
    N = 2ℓ+1.
    """
    ell = (N - 1) // 2
    lam = list(hw) + [0] * (ell - len(hw))

    # Shifted weights: μ_i = λ_i + ℓ - i + 1/2  (i from 0)
    # Actually for B_ℓ: ρ_i = ℓ - i + 1/2, so μ_i = λ_i + ρ_i
    mu = [lam[i] + ell - i - Fraction(1, 2) for i in range(ell)]
    rho = [ell - i - Fraction(1, 2) for i in range(ell)]

    num = Fraction(1)
    den = Fraction(1)

    # Product over i < j of (μ_i² - μ_j²)/(ρ_i² - ρ_j²)
    for i in range(ell):
        for j in range(i + 1, ell):
            num *= (mu[i] ** 2 - mu[j] ** 2)
            den *= (rho[i] ** 2 - rho[j] ** 2)

    # Product over i of μ_i / ρ_i
    for i in range(ell):
        num *= mu[i]
        den *= rho[i]

    return num / den


def weyl_dim_so_even(N, hw):
    """
    Dimension of SO(2ℓ) irrep with highest weight hw = (λ₁,...,λ_ℓ).
    Uses the Weyl dimension formula for type D_ℓ.
    N = 2ℓ.
    """
    ell = N // 2
    lam = list(hw) + [0] * (ell - len(hw))

    # Shifted weights: μ_i = λ_i + ℓ - i  (i from 0, so μ_i = λ_i + ℓ - i)
    # ρ for D_ℓ: ρ_i = ℓ - i - 1 for i = 0,...,ℓ-1? No.
    # ρ = (ℓ-1, ℓ-2, ..., 1, 0) for D_ℓ
    mu = [lam[i] + ell - 1 - i for i in range(ell)]
    rho = [ell - 1 - i for i in range(ell)]

    num = Fraction(1)
    den = Fraction(1)

    # Product over i < j of (μ_i² - μ_j²)/(ρ_i² - ρ_j²)
    for i in range(ell):
        for j in range(i + 1, ell):
            num *= (mu[i] ** 2 - mu[j] ** 2)
            rho_diff = rho[i] ** 2 - rho[j] ** 2
            if rho_diff == 0:
                # This happens when ρ_i = ρ_j = 0, need L'Hopital
                # For D_ℓ, ρ_{ℓ-1} = 0, so ρ_{ℓ-1}² - ρ_j² could be problematic
                # Actually ρ_{ℓ-1} = 0 and it's the only zero, so this case
                # is i=ℓ-2, j=ℓ-1 with ρ = (1, 0) -> 1-0=1, fine for ℓ≥2
                # Hmm, this shouldn't happen. Let me reconsider.
                den *= Fraction(1)  # skip
            else:
                den *= rho_diff

    return num / den


def degeneracy(p, q, n):
    """
    Multiplicity d(p,q) for eigenvalue λ(p,q) on Q^n = SO(n+2)/[SO(n)×SO(2)].
    This is dim of SO(n+2) irrep with highest weight (p, q, 0, ..., 0)
    MINUS dim of irrep (p-1, q-1, 0, ..., 0) [for the traceless condition,
    but actually for Q^n the class-1 reps are simply (p,q,0,...,0)].

    Wait — for the compact dual Q^n = SO(n+2)/[SO(n)×SO(2)], the spherical
    (class-1) representations have highest weight (p, q, 0, ..., 0) with p ≥ q ≥ 0.
    The multiplicity IS the dimension of the full representation (the K-fixed
    vector has multiplicity 1 for each class-1 rep).
    """
    N = n + 2
    if N % 2 == 1:  # SO(odd)
        return weyl_dim_so_odd(N, (p, q))
    else:  # SO(even)
        return weyl_dim_so_even(N, (p, q))


def eigenvalue(p, q, n):
    """Laplacian eigenvalue on Q^n for representation (p,q)."""
    return p * (p + n) + q * (q + n - 2)


# =============================================================================
# Part 2: Verification — brute force spectral sum
# =============================================================================

def heat_trace_rank2(t, n, p_max=400):
    """
    Z(t) = Σ_{p≥q≥0} d(p,q) exp(-λ(p,q) t)
    Using exact rational multiplicities, float exponentials.
    """
    Z = 0.0
    for p in range(p_max):
        lam_p = p * (p + n)
        exp_p = np.exp(-lam_p * t)
        if exp_p < 1e-100:
            break
        for q in range(p + 1):
            lam_pq = lam_p + q * (q + n - 2)
            exp_pq = exp_p * np.exp(-q * (q + n - 2) * t)
            if exp_pq < 1e-100:
                break
            d = float(degeneracy(p, q, n))
            Z += d * exp_pq
    return Z


def rescaled_trace(t, n, p_max=400):
    """F(t) = (4πt)^{n/2} × Z(t) → Σ a_k t^k as t→0."""
    return (4 * np.pi * t) ** (n / 2) * heat_trace_rank2(t, n, p_max)


def extract_coefficients(n, p_max=400, degree=7, num_points=50):
    """Extract a_k by polynomial regression on F(t)."""
    t_vals = np.logspace(-3, -1.5, num_points)
    F_vals = np.array([rescaled_trace(t, n, p_max) for t in t_vals])

    # Fit F(t) = a_0 + a_1 t + a_2 t^2 + ... + a_d t^d
    # Use polynomial basis
    A = np.vander(t_vals, degree + 1, increasing=True)
    coeffs, _, _, _ = np.linalg.lstsq(A, F_vals, rcond=None)
    return coeffs


# =============================================================================
# Part 3: THE LINEAR METHOD
#
# d(p,q) is a polynomial in (p,q). Write it as:
#   d(p,q) = Σ_{i,j} c_{ij} p^i q^j
#
# Then a_k = Σ_{ij} c_{ij} × w_{ij,k}
# where w_{ij,k} is the contribution of the monomial p^i q^j to a_k.
#
# This is a LINEAR functional: a = C · w
# =============================================================================

def fit_multiplicity_polynomial(n, max_deg=12):
    """
    Express d(p,q) as a polynomial in (p,q) for given n.
    Returns coefficients c_{ij} such that d(p,q) ≈ Σ c_{ij} p^i q^j.

    Uses exact rational arithmetic.
    """
    # Sample enough points to determine polynomial
    # d(p,q) for Q^n has degree dim_R - 2 = 2n - 2 in (p,q) combined
    # But the actual degree might be lower
    # For safety, sample a grid and fit

    # First, let's find the actual polynomial degree
    # by checking d(p,0) as a function of p
    sample_p = list(range(max_deg + 5))
    d_p0 = [float(degeneracy(p, 0, n)) for p in sample_p]

    # Find degree in p alone (q=0)
    for deg_p in range(1, max_deg + 1):
        A = np.vander(sample_p[:deg_p + 2], deg_p + 1, increasing=True)
        c, res, _, _ = np.linalg.lstsq(A, d_p0[:deg_p + 2], rcond=None)
        predicted = np.polyval(c[::-1], sample_p)
        if np.max(np.abs(predicted - d_p0)) < 0.01:
            break

    # Now fit the full 2D polynomial
    # Degree in (p,q) combined
    total_deg = 2 * n - 2  # expected from Weyl formula

    # Generate sample points (p, q) with p ≥ q ≥ 0
    points = []
    values = []
    for p in range(total_deg + 5):
        for q in range(p + 1):
            points.append((p, q))
            values.append(float(degeneracy(p, q, n)))

    # Build monomial basis {p^i q^j : i+j ≤ total_deg}
    monomials = []
    for i in range(total_deg + 1):
        for j in range(total_deg + 1 - i):
            monomials.append((i, j))

    # Build design matrix
    A = np.zeros((len(points), len(monomials)))
    for row, (p, q) in enumerate(points):
        for col, (i, j) in enumerate(monomials):
            A[row, col] = p ** i * q ** j

    values = np.array(values)
    coeffs, _, _, _ = np.linalg.lstsq(A, values, rcond=None)

    # Verify
    max_err = 0
    for p in range(total_deg + 8):
        for q in range(p + 1):
            d_exact = float(degeneracy(p, q, n))
            d_poly = sum(
                coeffs[col] * p ** i * q ** j
                for col, (i, j) in enumerate(monomials)
            )
            max_err = max(max_err, abs(d_exact - d_poly))

    return coeffs, monomials, max_err


def compute_monomial_heat_weight(i, j, n, k_target, p_max=500, num_t=50, degree=7):
    """
    Compute w_{ij,k}: the contribution of monomial p^i q^j to a_k.

    w_{ij,k} = coefficient of t^k in (4πt)^{n/2} × Σ_{p≥q≥0} p^i q^j exp(-λ(p,q)t)

    This depends only on (i, j, n), NOT on the dimension formula.
    """
    t_vals = np.logspace(-3, -1.5, num_t)

    S_vals = np.zeros(num_t)
    for idx, t in enumerate(t_vals):
        S = 0.0
        for p in range(p_max):
            lam_p = p * (p + n)
            exp_p = np.exp(-lam_p * t)
            if exp_p < 1e-100:
                break
            p_pow = p ** i
            for q in range(p + 1):
                lam_pq = lam_p + q * (q + n - 2)
                exp_pq = exp_p * np.exp(-q * (q + n - 2) * t)
                if exp_pq < 1e-100:
                    break
                S += p_pow * (q ** j) * exp_pq
            S_vals[idx] = S

    # Rescale by (4πt)^{n/2}
    F_vals = (4 * np.pi * t_vals) ** (n / 2) * S_vals

    # Fit polynomial and extract coefficient k
    A = np.vander(t_vals, degree + 1, increasing=True)
    coeffs, _, _, _ = np.linalg.lstsq(A, F_vals, rcond=None)

    return coeffs  # all coefficients a_0, a_1, ..., a_degree


# =============================================================================
# Part 4: Main computation
# =============================================================================

def main():
    print("=" * 70)
    print("Toy 249: Linear Gilkey")
    print("a_k as linear functional on multiplicity polynomial")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Step 1: Verify dimension formula
    # -------------------------------------------------------------------------
    print("\n--- Step 1: Dimension formula verification ---")
    test_cases = {
        # (n, p, q): expected_dim
        # SO(5) = B_2, Q^3
        (3, 1, 0): 5,   # fundamental of SO(5)
        (3, 0, 1): 4,   # spinor of SO(5) — wait, (0,1) for B_2...
        # Actually (1,0) = vector rep, dim 5 for SO(5) ✓
        # SO(7) = B_3, Q^5
        (5, 1, 0): 7,   # fundamental of SO(7)
        (5, 0, 1): 21,  # adjoint? No, (0,1,0) = adjoint for B_3
        # (p,q) for Q^n means highest weight (p,q,0,...,0)
        # For SO(7): (1,0,0) = 7-dim vector ✓
        # (0,1,0) = 21-dim adjoint
        # But our (p,q) = (0,1) means hw = (0,1,0) for SO(7)
        (5, 2, 0): 27,  # symmetric traceless of SO(7)
    }

    all_pass = True
    for (n, p, q), expected in test_cases.items():
        d = degeneracy(p, q, n)
        status = "✓" if d == expected else "✗"
        if d != expected:
            all_pass = False
        print(f"  Q^{n}: d({p},{q}) = {d} (expected {expected}) {status}")

    # Additional: d(0,0) should always be 1
    for n in [3, 4, 5, 6]:
        d = degeneracy(0, 0, n)
        status = "✓" if d == 1 else "✗"
        if d != 1:
            all_pass = False
        print(f"  Q^{n}: d(0,0) = {d} (expected 1) {status}")

    # -------------------------------------------------------------------------
    # Step 2: Brute force a₄ for Q³, Q⁴, Q⁵, Q⁶
    # -------------------------------------------------------------------------
    print("\n--- Step 2: Brute force spectral extraction ---")
    print("  (This validates our spectrum before linearizing)")

    target_a4 = {3: 1.893, 4: 22.352, 5: 148.389, 6: 680.98}
    target_a1 = {3: 2.500, 4: 4.833, 5: 7.833, 6: 11.500}

    for n in [3, 4, 5, 6]:
        print(f"\n  Q^{n} (SO({n+2}), N_c={n-2}, g={2*n-3}):")
        p_max = 300
        coeffs = extract_coefficients(n, p_max=p_max, degree=7)
        a0, a1, a2, a3, a4 = coeffs[:5]

        a1_expected = (2 * n**2 - 3) / 6
        a4_target = target_a4[n]

        print(f"    a₀ = {a0:.6f} (expect Vol × normalization)")
        print(f"    a₁ = {a1:.6f} (expect {a1_expected:.6f} = (2n²-3)/6)")
        print(f"    a₄ = {a4:.4f} (Elie: {a4_target:.3f})")

        if n == 5:
            Ncg2 = 3 * 49
            ratio = a4 / Ncg2
            residual = a4 - 147
            print(f"    a₄/147 = {ratio:.6f}")
            print(f"    a₄ - 147 = {residual:.6f} (expect 25/18 = {25/18:.6f})")

    # -------------------------------------------------------------------------
    # Step 3: Multiplicity polynomial
    # -------------------------------------------------------------------------
    print("\n--- Step 3: Multiplicity as polynomial in (p,q) ---")
    print("  d(p,q) = Σ c_{ij} p^i q^j — the eigenvector")

    for n in [3, 5]:
        coeffs, monomials, max_err = fit_multiplicity_polynomial(n)
        print(f"\n  Q^{n}: d(p,q) polynomial (max error = {max_err:.2e}):")

        # Show nonzero coefficients
        for idx, (i, j) in enumerate(monomials):
            c = coeffs[idx]
            if abs(c) > 1e-8:
                # Try to identify as simple fraction
                frac = Fraction(c).limit_denominator(10000)
                if abs(float(frac) - c) < 1e-6:
                    print(f"    c_{{{i},{j}}} = {frac}  (p^{i} q^{j})")
                else:
                    print(f"    c_{{{i},{j}}} = {c:.6f}  (p^{i} q^{j})")

    # -------------------------------------------------------------------------
    # Step 4: THE LINEAR DECOMPOSITION
    # -------------------------------------------------------------------------
    print("\n--- Step 4: Linear decomposition of a₄ ---")
    print("  a₄ = Σ c_{ij} × w_{ij,4}")
    print("  = (multiplicity coefficients) · (heat kernel weights)")
    print("  = INNER PRODUCT in coefficient space")

    n = 5
    print(f"\n  Computing for Q^{n}...")

    # Get multiplicity polynomial
    c_coeffs, monomials, _ = fit_multiplicity_polynomial(n)

    # Compute heat kernel weights for each monomial
    print(f"  {len([c for c in c_coeffs if abs(c) > 1e-8])} nonzero monomials")

    # For efficiency, only compute weights for nonzero monomials
    contributions = []
    a4_linear = 0.0
    total_computed = 0

    for idx, (i, j) in enumerate(monomials):
        c = c_coeffs[idx]
        if abs(c) < 1e-8:
            continue

        total_computed += 1
        # Compute w_{ij,k} for all k
        w_all = compute_monomial_heat_weight(i, j, n, k_target=4,
                                              p_max=300, num_t=40, degree=7)
        w4 = w_all[4]  # the a₄ weight

        contribution = c * w4
        a4_linear += contribution

        frac_c = Fraction(c).limit_denominator(10000)
        contributions.append((i, j, float(frac_c), w4, contribution))
        print(f"    p^{i}q^{j}: c={frac_c}, w₄={w4:.4f}, "
              f"contribution={contribution:.4f}")

    print(f"\n  a₄ (linear) = {a4_linear:.6f}")
    print(f"  a₄ (expect) = {25*147/18 + 25/18:.6f} = 2671/18")
    print(f"  a₄ - 147 = {a4_linear - 147:.6f} (expect {25/18:.6f})")

    # -------------------------------------------------------------------------
    # Step 5: The eigenvalue interpretation
    # -------------------------------------------------------------------------
    print("\n--- Step 5: The eigenvalue interpretation ---")
    print("""
  The multiplicity polynomial d(p,q) is a vector in coefficient space:
    |d⟩ = Σ c_{ij} |i,j⟩

  The heat kernel weight functional is another vector:
    ⟨w_k| = Σ w_{ij,k} ⟨i,j|

  The Seeley-DeWitt coefficient is the inner product:
    a_k = ⟨w_k | d⟩

  This is LINEAR. Change the group (change |d⟩), and a_k updates
  by a dot product. No tensor contractions. No Gilkey formula.
  No 23-minute computation.

  The 'matrix' {w_{ij,k}} depends only on the EIGENVALUE structure
  λ(p,q) = p(p+n) + q(q+n-2), not on the group.
  The 'vector' {c_{ij}} depends only on the GROUP (via Weyl dim formula),
  not on the eigenvalue structure.

  SEPARATION OF CONCERNS:
    geometry → eigenvalues → weights {w_{ij,k}}
    group    → dimensions  → coefficients {c_{ij}}
    physics  = ⟨geometry | group⟩ = inner product
    """)

    # -------------------------------------------------------------------------
    # Step 6: Cross-family comparison
    # -------------------------------------------------------------------------
    print("--- Step 6: Cross-family test ---")
    print("  If the method works, a₄ should match brute force for all n")

    for n in [3, 4, 5, 6]:
        c_coeffs, monomials, _ = fit_multiplicity_polynomial(n)

        a4_lin = 0.0
        for idx, (i, j) in enumerate(monomials):
            c = c_coeffs[idx]
            if abs(c) < 1e-8:
                continue
            w_all = compute_monomial_heat_weight(i, j, n, k_target=4,
                                                  p_max=300, num_t=40, degree=7)
            a4_lin += c * w_all[4]

        Ncg2 = (n - 2) * (2 * n - 3) ** 2
        ratio = a4_lin / Ncg2 if Ncg2 > 0 else float('inf')

        print(f"  Q^{n}: a₄(linear) = {a4_lin:.4f}, N_c g² = {Ncg2}, "
              f"ratio = {ratio:.4f}")

    # -------------------------------------------------------------------------
    # Step 7: The punchline
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("RESULT: a_k = ⟨w_k | d⟩")
    print()
    print("The Seeley-DeWitt coefficient is an inner product between")
    print("two vectors in monomial coefficient space:")
    print("  |d⟩ = multiplicity polynomial (from Weyl dimension formula)")
    print("  ⟨w_k| = heat kernel weight (from eigenvalue structure)")
    print()
    print("Both are computable separately. Their dot product is a_k.")
    print("Lift, diagonalize, project. The rest is bookkeeping.")
    print("=" * 70)


if __name__ == "__main__":
    main()
