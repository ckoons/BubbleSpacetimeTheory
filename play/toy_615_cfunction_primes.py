#!/usr/bin/env python3
"""
Toy 615 — c-Function Prime Structure: The Matched Codebook
===========================================================
Casey's directive: "everything is finite, use a finite method."
Keeper's identification: Harish-Chandra c-function is the matched codebook.

The c-function for SO₀(n,2) with BC₂ root system:
  - Short roots (e₁, e₂): multiplicity m_s = n - 2
  - Long roots (e₁±e₂): multiplicity m_l = 1
  - Double roots (2e₁, 2e₂): multiplicity m_{2α} = 1

Three finite computations:
  1. Weyl denominator D(n) for SO(n+2) — factor it, find which primes
  2. Weyl dimensions d(p,q,n) for low representations — factor, find monster primes
  3. c-function Gamma ratios at the ρ-vector — factor, compare to a_k(n)

Key test: do the polynomial-factor primes (66569, 506687, ...) that appeared
in Toy 614's Newton coefficients originate from specific Weyl dimensions?
If yes, the c-function (through the dimension formula) IS the source of ALL primes
in the heat kernel arithmetic.

Elie — March 29, 2026

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
from math import gcd, comb, factorial
from collections import defaultdict

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

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
# PRIME UTILITIES
# ═══════════════════════════════════════════════════════════════════

def prime_factorization(n):
    if n == 0: return {0: 1}
    if n == 1: return {}
    n = abs(n)
    pf = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            pf[d] = pf.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: pf[n] = pf.get(n, 0) + 1
    return pf


def max_prime(n):
    pf = prime_factorization(n)
    return max(pf.keys()) if pf else 1


def pf_str(pf):
    if not pf: return "1"
    return " · ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(pf.items()))


# ═══════════════════════════════════════════════════════════════════
# WEYL DIMENSION FORMULAS (from Toy 613 infrastructure)
# ═══════════════════════════════════════════════════════════════════

def _dim_B(p, q, r):
    """Dimension of SO(2r+1) rep with highest weight (p, q, 0, ..., 0)."""
    lam = [0] * (r + 1); lam[1] = p; lam[2] = q
    L = [0] * (r + 1); P = [0] * (r + 1)
    for i in range(1, r + 1):
        P[i] = 2 * r - 2 * i + 1; L[i] = 2 * lam[i] + P[i]
    num = den = 1
    for i in range(1, r + 1):
        for j in range(i + 1, r + 1):
            num *= (L[i]**2 - L[j]**2); den *= (P[i]**2 - P[j]**2)
    for i in range(1, r + 1):
        num *= L[i]; den *= P[i]
    return num // den


def _dim_D(p, q, r):
    """Dimension of SO(2r) rep with highest weight (p, q, 0, ..., 0)."""
    lam = [0] * (r + 1); lam[1] = p; lam[2] = q
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
    """Dimension of SO(N) representation (p, q, 0, ..., 0)."""
    if N < 5: return 0
    return _dim_B(p, q, (N - 1) // 2) if N % 2 == 1 else _dim_D(p, q, N // 2)


def eigenvalue(p, q, n):
    """Casimir eigenvalue on Q^n = SO(n+2)/[SO(n)×SO(2)]."""
    return p * (p + n) + q * (q + n - 2)


# ═══════════════════════════════════════════════════════════════════
# WEYL DENOMINATOR COMPUTATION
# ═══════════════════════════════════════════════════════════════════

def weyl_denominator_B(r):
    """
    Weyl denominator for B_r = SO(2r+1).
    ρ_i = r - i + 1/2 for i = 1, ..., r (using 2ρ to stay integer).

    Denominator = ∏ρ_i · ∏_{i<j}(ρ_i² - ρ_j²)
    Using 2ρ: den_scaled = ∏(2ρ_i) · ∏_{i<j}((2ρ_i)² - (2ρ_j)²)
    """
    two_rho = [2 * r - 2 * i + 1 for i in range(1, r + 1)]  # [2r-1, 2r-3, ..., 1]
    prod_rho = 1
    for rr in two_rho:
        prod_rho *= rr
    prod_diff = 1
    for i in range(len(two_rho)):
        for j in range(i + 1, len(two_rho)):
            prod_diff *= (two_rho[i]**2 - two_rho[j]**2)
    return prod_rho * prod_diff, two_rho


def weyl_denominator_D(r):
    """
    Weyl denominator for D_r = SO(2r).
    ρ_i = r - i for i = 1, ..., r.

    Denominator = ∏_{i<j}(ρ_i² - ρ_j²)
    """
    rho = [r - i for i in range(1, r + 1)]  # [r-1, r-2, ..., 0]
    prod_diff = 1
    for i in range(len(rho)):
        for j in range(i + 1, len(rho)):
            diff = rho[i]**2 - rho[j]**2
            if diff == 0:
                return 0, rho
            prod_diff *= diff
    return prod_diff, rho


# ═══════════════════════════════════════════════════════════════════
# c-FUNCTION GAMMA RATIOS (finite, exact)
# ═══════════════════════════════════════════════════════════════════

def pochhammer(x, m):
    """Rising factorial (x)_m = x(x+1)...(x+m-1) as exact Fraction."""
    result = Fraction(1)
    for k in range(m):
        result *= Fraction(x + k)
    return result


def gamma_ratio_integer_shift(s, m):
    """
    Γ(s + m) / Γ(s) = (s)_m = s(s+1)...(s+m-1)
    Exact for integer m ≥ 0. s can be Fraction.
    """
    return pochhammer(s, m)


def bc2_rho_vector(n):
    """
    Half-sum of positive roots for BC₂ with multiplicities (m_s=n-2, m_l=1, m_{2α}=1).

    ρ = (1/2) Σ_{α>0} m_α · α

    Positive roots and multiplicities:
      e₁: m_s = n-2           → contributes (n-2)/2 · e₁
      e₂: m_s = n-2           → contributes (n-2)/2 · e₂
      e₁+e₂: m_l = 1          → contributes 1/2 · (e₁+e₂)
      e₁-e₂: m_l = 1          → contributes 1/2 · (e₁-e₂)
      2e₁: m_{2α} = 1         → contributes 1/2 · 2e₁ = e₁
      2e₂: m_{2α} = 1         → contributes 1/2 · 2e₂ = e₂

    ρ₁ = (n-2)/2 + 1/2 + 1 = n/2 + 1/2... wait, let me recompute.

    Actually ρ = (1/2) Σ m_α α:
    ρ₁ = (1/2)[m_s·1 + m_l·1 + m_l·1 + m_{2α}·2] = (1/2)[(n-2) + 1 + 1 + 2] = n/2 + 1
    Wait, that uses all roots involving e₁.

    Let me be careful. In BC₂:
    Roots involving e₁ positively:
      e₁ (coeff 1): m = n-2
      e₁+e₂ (coeff 1): m = 1
      e₁-e₂ (coeff 1): m = 1
      2e₁ (coeff 2): m = 1

    ρ₁ = (1/2)[(n-2)·1 + 1·1 + 1·1 + 1·2] = (1/2)[n-2+1+1+2] = n/2

    Roots involving e₂ positively:
      e₂ (coeff 1): m = n-2
      e₁+e₂ (coeff 1): m = 1
      2e₂ (coeff 2): m = 1
    Roots involving e₂ negatively:
      e₁-e₂ (coeff -1): m = 1 → subtract

    ρ₂ = (1/2)[(n-2)·1 + 1·1 - 1·1 + 1·2] = (1/2)[n-2+1-1+2] = n/2

    Hmm, that gives ρ = (n/2, n/2) which doesn't match the codebase ρ = (n/2, (n-2)/2).
    Let me use the codebase values.
    """
    # From BST_CFunction_RatioTheorem.md §5: ρ_n = (n/2, (n-2)/2)
    return Fraction(n, 2), Fraction(n - 2, 2)


# ═══════════════════════════════════════════════════════════════════
# KNOWN a_k(n) VALUES (from Toy 613/614)
# ═══════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()

    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  Toy 615 — c-Function Prime Structure: The Matched Codebook   ║")
    print("║  Harish-Chandra c-function for SO₀(n,2) / [SO(n)×SO(2)]      ║")
    print("║  Finite. Exact. Three computations.                           ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    # ─── Section 1: Weyl Denominator D(n) ─────────────────────────
    print(f"\n{'='*65}")
    print(f"  Section 1: Weyl Denominator D(n) for SO(n+2)")
    print(f"  Which primes appear in the universal dimension denominator?")
    print(f"{'='*65}")

    weyl_primes = {}
    for n in range(3, 16):
        N = n + 2  # SO(N)
        if N % 2 == 1:
            r = (N - 1) // 2
            D, rho_vals = weyl_denominator_B(r)
            so_type = f"B_{r}"
        else:
            r = N // 2
            D, rho_vals = weyl_denominator_D(r)
            so_type = f"D_{r}"

        pf = prime_factorization(D)
        mp = max(pf.keys()) if pf else 1
        weyl_primes[n] = (D, pf, mp)

        print(f"\n  n={n:2d} → SO({N}) type {so_type}: D = {D}")
        print(f"         ρ = {rho_vals}")
        print(f"         primes: {pf_str(pf)}")
        print(f"         max prime: {mp}")

    # Check: max prime in D(n) is always small (bounded by ~n)
    all_small = all(mp <= n + 5 for n, (_, _, mp) in weyl_primes.items())
    score("Weyl denominator primes bounded by ~n", all_small,
          "Monster primes (66569 etc.) are NOT in the Weyl denominator")

    # ─── Section 2: Weyl Dimensions — Hunt for Monster Primes ─────
    print(f"\n{'='*65}")
    print(f"  Section 2: Weyl Dimensions d(p,q,n) — Hunting Monster Primes")
    print(f"  Where do 66569, 506687, etc. come from?")
    print(f"{'='*65}")

    # The monster primes from Toy 614 Newton coefficients:
    monster_primes = [10513, 66569, 506687,  # from a_8 Newton coeffs
                      83, 313, 607, 7193, 8291, 36067, 61627, 532709,  # from a_9
                      47, 59, 109, 701, 773, 1409, 2287, 2377, 15233, 111031, 174049, 632839, 6966151]  # from a_10

    # For each monster prime, search for it in Weyl dimensions
    # at the n values where it appeared in a_k(n) denominators
    print(f"\n  Searching for monster primes in Weyl dimensions...")

    # First: which n values have monster primes in a_k(n) denominators?
    # From Toy 613: a_8(10) has prime 66569 in denominator
    # Let's systematically check d(p,q,n) for specific (n, monster_prime) pairs

    test_cases = [
        (10, 66569, "a_8(10) denominator"),
        (10, 10513, "a_8 Newton coefficients"),
        (10, 506687, "a_8 Newton coefficients"),
    ]

    for n_test, target_prime, source in test_cases:
        N = n_test + 2
        print(f"\n  Hunting prime {target_prime} in SO({N}) dimensions (n={n_test}):")
        found = False
        for p in range(50):
            for q in range(p + 1):
                d = dim_SO(p, q, N)
                if d > 1 and d % target_prime == 0:
                    lam = eigenvalue(p, q, n_test)
                    print(f"    FOUND: d({p},{q}) = {d}, λ = {lam}")
                    pf = prime_factorization(d)
                    print(f"           factors: {pf_str(pf)}")
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"    Not found in d(p,q) for p,q < 50")
            # Check if it's in the eigenvalue instead
            for p in range(100):
                for q in range(p + 1):
                    lam = eigenvalue(p, q, n_test)
                    if lam > 1 and lam % target_prime == 0:
                        d = dim_SO(p, q, N)
                        print(f"    In eigenvalue: λ({p},{q}) = {lam} = {target_prime} × {lam // target_prime}, d = {d}")
                        found = True
                        break
                if found:
                    break
            if not found:
                print(f"    Not found in dimensions OR eigenvalues for p,q < 100")

    # ─── Section 3: Volume Formula and c-Function at ρ ────────────
    print(f"\n{'='*65}")
    print(f"  Section 3: ρ-vector and c-function structure")
    print(f"  BC₂ root multiplicities: m_s = n-2, m_l = 1, m_{{2α}} = 1")
    print(f"{'='*65}")

    for n in range(3, 16):
        rho1, rho2 = bc2_rho_vector(n)
        rho_sq = rho1**2 + rho2**2

        # The c-function ratio c_{n+2}/c_n evaluated at discrete points
        # From BST_CFunction_RatioTheorem.md:
        # c_{n+2}/c_n = 1/[(2iλ₁ + (n-2)/2)(2iλ₂ + (n-2)/2)]
        # At the eigenvalue (p,q) the "spectral shift" from the ρ-vector gives
        # specific rational values.

        # The key quantity: m_s = n-2 enters the Gamma arguments
        m_s = n - 2

        print(f"\n  n={n:2d}: ρ = ({rho1}, {rho2}), |ρ|² = {rho_sq}, m_s = {m_s}")

        # Products that appear in the c-function:
        # For short roots: Γ((t + m_s/2)/2) where t = ⟨ρ, e_i⟩ / |e_i|²
        # At ρ: t₁ = ρ₁ = n/2, t₂ = ρ₂ = (n-2)/2

        # The Pochhammer product (ρ₁)_{m_s/2} = (n/2)(n/2+1)...(n/2+m_s/2-1)
        # But m_s/2 = (n-2)/2 which may not be integer

        # For integer n: if n even, m_s = n-2 is even, m_s/2 = (n-2)/2 is integer
        # If n odd, m_s is odd, m_s/2 is half-integer → involves Γ at half-integers

        # Let's compute the Weyl dimension formula denominator more carefully
        # The denominator for d(p,q) in SO(N) is FIXED for each N.
        # It's the product of the "rho products" from the Weyl formula.

    # ─── Section 4: Spectral Moment Decomposition ─────────────────
    print(f"\n{'='*65}")
    print(f"  Section 4: Spectral Moment Decomposition")
    print(f"  a_k(n) as weighted sum of eigenvalue powers")
    print(f"  How do individual eigenvalue contributions factor?")
    print(f"{'='*65}")

    # For small k and specific n, compute the partial spectral sums
    # S_K(k,n) = (1/Vol) Σ_{p+q ≤ K} d(p,q,n) · λ(p,q,n)^k
    # and track how the denominator of a_k(n) builds up

    for n in [5, 10]:
        N = n + 2
        print(f"\n  n = {n} (SO({N})):")

        # Compute Vol(Q^n) — the volume is encoded in the a_0 = 1 normalization
        # The heat trace: Z(t) / Vol ~ t^{-n/2} [1 + a_1 t + ...]
        # So Vol = Σ d(p,q) · e^{-tλ} / t^{-n/2} at leading order

        # For the spectral analysis, let's just track individual d·λ^k contributions
        print(f"  Individual d(p,q) · λ^k contributions for small (p,q):")

        for k in [1, 5, 8]:
            print(f"\n    k = {k}:")
            total = 0
            for p in range(8):
                for q in range(p + 1):
                    d = dim_SO(p, q, N)
                    lam = eigenvalue(p, q, n)
                    if d > 0 and lam > 0:
                        contrib = d * lam**k
                        total += contrib
                        if p + q <= 3:  # Show low representations
                            pf = prime_factorization(contrib) if contrib > 1 else {}
                            mp = max(pf.keys()) if pf else 1
                            print(f"      ({p},{q}): d={d}, λ={lam}, d·λ^{k}={contrib}"
                                  f"  max_prime={mp}")

            pf_total = prime_factorization(total) if total > 1 else {}
            mp_total = max(pf_total.keys()) if pf_total else 1
            print(f"      Partial sum (p+q<8): {total}, max prime = {mp_total}")

    # ─── Section 5: The Key Test — Denominator from Vol and Weyl ──
    print(f"\n{'='*65}")
    print(f"  Section 5: Denominator Origin Analysis")
    print(f"  For a_k(5), trace each denominator prime to its source")
    print(f"{'='*65}")

    # The denominators of a_k(5) for k=1..12 are known.
    # Each prime in the denominator must come from SOMEWHERE:
    # (A) Bernoulli numbers (VSC primes) — from the asymptotic expansion
    # (B) Volume normalization — from Vol(Q^5)
    # (C) The cascade subtraction — introduces lcm of lower-level denominators
    # (D) Something else

    # Let's check: what is Vol(Q^5)?
    # Q^5 = SO(7)/[SO(5)×SO(2)], a 5-dimensional compact symmetric space
    # Vol = π^5/1920 × (normalization factor)
    # From BST: Vol(D_IV^5) = π⁵/1920, so K(0,0) = 1920/π⁵

    print(f"\n  Volume factor: Vol(Q^5) ∝ π⁵/1920")
    print(f"  1920 = {pf_str(prime_factorization(1920))}")
    print(f"  → Primes from volume: 2, 3, 5")

    # For each a_k(5), the denominator has been factored in §3.1 of the paper.
    # Let's check which primes are "new" at each level.
    print(f"\n  Prime entry tracking for den(a_k(5)):")

    den_primes_seen = set()
    for k in range(1, 13):
        val = KNOWN_AK5.get(k)
        if val is None: continue
        den = val.denominator
        pf = prime_factorization(den)
        new_primes = set(pf.keys()) - den_primes_seen
        den_primes_seen.update(pf.keys())

        new_str = ", ".join(str(p) for p in sorted(new_primes)) if new_primes else "none"
        print(f"  k={k:2d}: den = {den}, new primes: {new_str}")

        # For each new prime, identify the source
        for p in sorted(new_primes):
            # Check if it's a VSC prime (Bernoulli)
            is_vsc = any((2 * kk) % (p - 1) == 0 for kk in range(1, k + 1))
            source = "VSC (Bernoulli)" if is_vsc else "polynomial-factor"
            print(f"         p={p}: {source}")

    # ─── Section 6: c-Function Ratio at Discrete Points ───────────
    print(f"\n{'='*65}")
    print(f"  Section 6: c-Function Ratio at Discrete Eigenvalue Points")
    print(f"  c_{{n+2}}/c_n(λ) = 1/[(2iλ₁+(n-2)/2)(2iλ₂+(n-2)/2)]")
    print(f"  Evaluated at (p,q) eigenvalue labels")
    print(f"{'='*65}")

    # The c-function ratio evaluated at real spectral parameters
    # gives specific rationals whose denominators carry primes.

    # At eigenvalue label (p,q) with spectral parameters related to
    # the representation, the c-function ratio becomes a specific rational.

    # From BST_CFunction_RatioTheorem.md:
    # The "tower" of c-function ratios:
    # c₅/c₃, c₇/c₅, c₉/c₇, ... each has poles at λ_j = i(n-2)/4

    # The Plancherel ratio |c_{n+2}/c_n|^{-2} = (4λ₁² + (n-2)²/4)(4λ₂² + (n-2)²/4)
    # At discrete eigenvalue labels for the compact dual, λ₁ → p + n/2, λ₂ → q + (n-2)/2

    print(f"\n  Plancherel ratio |c_{{n+2}}/c_n|^{{-2}} at low eigenvalue labels:")

    for n in [3, 5, 7, 10]:
        print(f"\n  n = {n}:")
        m_half = Fraction(n - 2, 2)
        for p in range(5):
            for q in range(min(p + 1, 3)):
                # The spectral parameter at representation (p,q) in the compact dual
                # is related to p+ρ₁, q+ρ₂ where ρ = (n/2, (n-2)/2)
                # The Plancherel factor: (4(p+n/2)² + (n-2)²/4)(4(q+(n-2)/2)² + (n-2)²/4)
                # But for the compact dual, we use integer-shifted arguments

                # Simple version: the dimension d(p,q) itself IS the Plancherel density
                # at the discrete point, times a universal factor.
                d = dim_SO(p, q, n + 2)
                lam = eigenvalue(p, q, n)

                if d > 0 and p + q <= 4:
                    # Factor the dimension
                    if d > 1:
                        pf_d = prime_factorization(d)
                        mp_d = max(pf_d.keys())
                    else:
                        pf_d = {}
                        mp_d = 1
                    print(f"    ({p},{q}): d={d:>8d}, λ={lam:>6d}, max_prime(d)={mp_d}")

    # ─── Section 7: The Finite Answer ─────────────────────────────
    print(f"\n{'='*65}")
    print(f"  Section 7: The Finite Answer")
    print(f"  Where do ALL the primes in a_k(n) come from?")
    print(f"{'='*65}")

    # Compute: for n=5, what is the Weyl universal denominator?
    N = 7  # SO(7) for n=5
    r = 3  # B_3
    D5, rho_vals5 = weyl_denominator_B(r)
    pf_D5 = prime_factorization(D5)

    print(f"\n  SO(7) Weyl denominator D = {D5}")
    print(f"  Factored: {pf_str(pf_D5)}")
    print(f"  ρ = {rho_vals5}")

    # The factorial 2·k! from the constant term = (-1)^k / (2·k!)
    print(f"\n  Factorial denominators 2·k! for k=1..12:")
    for k in range(1, 13):
        fk = 2 * factorial(k)
        pf_fk = prime_factorization(fk)
        print(f"  k={k:2d}: 2·k! = {fk:>12d}, max prime = {max(pf_fk.keys())}")

    # The 3^k from leading coefficient = 1/(3^k · k!)
    print(f"\n  Leading coefficient denominators 3^k·k! for k=1..12:")
    for k in range(1, 13):
        lk = 3**k * factorial(k)
        pf_lk = prime_factorization(lk)
        mp = max(pf_lk.keys())
        print(f"  k={k:2d}: 3^k·k! = {lk:>15d}, max prime = {mp}")

    # Key insight: at n=5, ALL denominator primes through k=12 are ≤ 23.
    # The VSC primes explain the row rule.
    # The 3^k·k! explains the leading coefficient.
    # The Weyl denominator D(5) has only primes {3, 5}.
    # The volume 1920 has primes {2, 3, 5}.
    # So at n=5, ALL primes come from: Bernoulli + factorial + volume.
    # No "mystery" primes.

    # But at OTHER n values (like n=10), monster primes appear.
    # These must come from the Weyl dimensions d(p,q,10) for specific (p,q).

    print(f"\n  ─── Monster Prime Hunt at n=10 ───")
    N10 = 12  # SO(12)
    print(f"  SO(12) = D_6, searching dimensions for large primes...")

    large_prime_dims = []
    for p in range(100):
        for q in range(p + 1):
            d = dim_SO(p, q, N10)
            if d > 1:
                mp_d = max_prime(d)
                if mp_d > 100:
                    large_prime_dims.append((p, q, d, mp_d))

    large_prime_dims.sort(key=lambda x: -x[3])
    print(f"  Found {len(large_prime_dims)} representations with primes > 100")
    print(f"  Top 15 by max prime:")
    for p, q, d, mp_d in large_prime_dims[:15]:
        lam = eigenvalue(p, q, 10)
        print(f"    ({p:2d},{q:2d}): d={d:>12d}, λ={lam:>6d}, max_prime={mp_d}")

    # Check if 66569 appears
    found_66569 = any(mp == 66569 or d % 66569 == 0
                      for p, q, d, mp in large_prime_dims)
    score("Prime 66569 found in SO(12) Weyl dimensions", found_66569,
          "66569 appears in a_8(10) denominator — does it come from d(p,q)?")

    # ─── Section 8: Eigenvalue-Weighted Moment Analysis ───────────
    print(f"\n{'='*65}")
    print(f"  Section 8: Do a_k(5) denominators come from 3^k·k! × Bernoulli?")
    print(f"{'='*65}")

    # At n=5, the denominator of a_k(5) should be controlled by:
    # - 3^k from the leading coefficient's 1/3^k
    # - k! from the Three Theorems
    # - Bernoulli primes from the curvature expansion

    # The "expected denominator" is lcm of all B_{2j} denominators for j ≤ k,
    # times 3^k, times (2·k!).

    # Von Staudt-Clausen: den(B_{2j}) = ∏_{(p-1)|2j} p

    def bernoulli_den(j):
        """Product of primes p with (p-1) | 2j (von Staudt-Clausen)."""
        d = 1
        for p in range(2, 4 * j + 10):
            if all(p % dd != 0 for dd in range(2, min(p, 100)) if dd < p):  # primality
                if p > 1 and (2 * j) % (p - 1) == 0:
                    d *= p
        return d

    from sympy import isprime as _isprime

    def bernoulli_den_exact(j):
        """Product of primes p with (p-1) | 2j."""
        d = 1
        for p in range(2, 200):
            if _isprime(p) and (2 * j) % (p - 1) == 0:
                d *= p
        return d

    print(f"\n  den(B_{{2k}}) from von Staudt-Clausen:")
    cumulative_bernoulli_lcm = 1
    for k in range(1, 13):
        bd = bernoulli_den_exact(k)
        cumulative_bernoulli_lcm = cumulative_bernoulli_lcm * bd // gcd(cumulative_bernoulli_lcm, bd)
        pf_bd = prime_factorization(bd)
        print(f"  k={k:2d}: den(B_{2*k:2d}) = {bd:>6d} = {pf_str(pf_bd)}")

    # Now compare: actual den(a_k(5)) vs predicted den
    print(f"\n  Comparison: actual vs predicted denominator primes at n=5")
    print(f"  Predicted = cumulative Bernoulli primes (row rule only)")

    for k in range(1, 13):
        val = KNOWN_AK5.get(k)
        if val is None: continue
        actual_den = val.denominator
        actual_pf = prime_factorization(actual_den)
        actual_primes = set(actual_pf.keys())

        # Cumulative VSC primes through level k
        cum_vsc = set()
        for kk in range(1, k + 1):
            for p in range(2, 200):
                if _isprime(p) and (2 * kk) % (p - 1) == 0:
                    cum_vsc.add(p)

        extra = actual_primes - cum_vsc
        missing = cum_vsc - actual_primes

        status = "MATCH" if not extra and not missing else ""
        if extra: status += f"extra:{sorted(extra)} "
        if missing: status += f"cancelled:{sorted(missing)} "
        if not extra and not missing: status = "EXACT MATCH"

        print(f"  k={k:2d}: actual primes {str(sorted(actual_primes)):>30s}  "
              f"VSC primes {str(sorted(cum_vsc)):>30s}  {status}")

    score("At n=5, ALL primes in a_k(5) denominators are VSC primes",
          all(set(prime_factorization(KNOWN_AK5[k].denominator).keys()).issubset(
              {p for kk in range(1, k+1) for p in range(2, 200)
               if _isprime(p) and (2*kk) % (p-1) == 0})
              for k in range(1, 13)),
          "n=5 is arithmetically tame: only Bernoulli primes, no polynomial-factor primes")

    # ─── Scorecard ────────────────────────────────────────────────
    elapsed = time.time() - t_start
    print(f"\n{'='*65}")
    print(f"  SCORECARD: {PASS}/{PASS+FAIL}  ({elapsed:.1f}s)")
    print(f"{'='*65}")


if __name__ == "__main__":
    main()
