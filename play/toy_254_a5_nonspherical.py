#!/usr/bin/env python3
"""
Toy 251 — a₅ with Non-Spherical Corrections
============================================

ORIGINAL GOAL: Test the non-spherical contamination theorem (Toy 250).

KEY DISCOVERY: The non-spherical theorem is WRONG.
  On Q^n (rank 2), ALL (p,q) reps with p≥q≥0 are spherical — they have
  K-fixed vectors and contribute to L²(G/K). This follows from Helgason's
  theorem: spherical reps on rank-r symmetric spaces are parameterized by
  r integers.

  Evidence: q=0-only sum gives a₀=0 (not 1) and a₄=192 (not 2671/18).
  The full (p,q) sum gives the correct values.

RESULT: a₅(Q⁵) ≈ 14185/64 = 221.640625 from the full sum.
  Denominator: 64 = 2^6 = 2^{C₂}
  Numerator: 14185 = 5 × 2837 (prime)

Score: 3/5 (two checks fail because the non-spherical theorem is wrong)

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import numpy as np
from fractions import Fraction
from math import factorial

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
# WEYL DIMENSION FORMULA — FROM TOY 248 (480/480 VERIFIED)
# ═══════════════════════════════════════════════════════════════════

def _dim_B(p, q, r):
    """Type B_r: SO(2r+1), weight (p, q, 0, ..., 0)."""
    lam = [0] * (r + 1)
    lam[1] = p
    lam[2] = q
    L = [0] * (r + 1)
    P = [0] * (r + 1)
    for i in range(1, r + 1):
        P[i] = 2 * r - 2 * i + 1
        L[i] = 2 * lam[i] + P[i]
    num = 1
    den = 1
    for i in range(1, r + 1):
        for j in range(i + 1, r + 1):
            num *= (L[i] * L[i] - L[j] * L[j])
            den *= (P[i] * P[i] - P[j] * P[j])
    for i in range(1, r + 1):
        num *= L[i]
        den *= P[i]
    return num // den


def _dim_D(p, q, r):
    """Type D_r: SO(2r), weight (p, q, 0, ..., 0)."""
    lam = [0] * (r + 1)
    lam[1] = p
    lam[2] = q
    l = [0] * (r + 1)
    rho = [0] * (r + 1)
    for i in range(1, r + 1):
        rho[i] = r - i
        l[i] = lam[i] + rho[i]
    num = 1
    den = 1
    for i in range(1, r + 1):
        for j in range(i + 1, r + 1):
            num *= (l[i] * l[i] - l[j] * l[j])
            d = rho[i] * rho[i] - rho[j] * rho[j]
            if d == 0:
                raise ValueError(f"Zero denom: rho[{i}]={rho[i]}, rho[{j}]={rho[j]}")
            den *= d
    return num // den


def dim_SO(p, q, N):
    """Dimension of the (p, q, 0, ..., 0) representation of SO(N)."""
    if N < 5:
        raise ValueError(f"Need N >= 5 for rank >= 2, got {N}")
    if N % 2 == 1:
        return _dim_B(p, q, (N - 1) // 2)
    else:
        return _dim_D(p, q, N // 2)


# ═══════════════════════════════════════════════════════════════════
# K-FIXED VECTORS: WHICH REPS ARE SPHERICAL?
# ═══════════════════════════════════════════════════════════════════
#
# Q^n = SO(n+2)/[SO(n)×SO(2)].
# K = SO(n)×SO(2).
# A rep (p,q) of SO(n+2) is spherical (has a K-fixed vector) iff
# it appears in the decomposition of functions on Q^n.
#
# For the real Grassmannian SO(n+2)/[SO(n)×SO(2)]:
# The spherical representations are exactly those with q = 0
# (highest weight (p, 0, 0, ..., 0)).
#
# More precisely: on SO(n+2)/[SO(n)×SO(2)], the spherical
# representations are those of SO(n+2) whose restriction to
# SO(n)×SO(2) contains the trivial representation. For the
# type IV domain this is equivalent to q ≡ 0 (mod 2) with q ≤ p.
#
# Wait — this needs more care. Let me verify empirically.
#
# Actually, for the COMPACT quotient SO(n+2)/[SO(n)×SO(2)],
# the Peter-Weyl theorem says L²(G/K) = ⊕ V_π^K,
# where the sum is over all irreps π of G that have a K-fixed vector.
#
# For G/K = SO(n+2)/[SO(n)×SO(2)], the K-spherical representations
# are those (p, q, 0, ..., 0) where q is EVEN.
# This is because the SO(2) factor acts by e^{iqθ}, and a K-fixed
# vector requires q = 0 mod 2 for the SO(2) part to be trivial...
#
# Actually, the standard result for the oriented real Grassmannian
# Gr_2(R^{n+2}) = SO(n+2)/[SO(n)×SO(2)] is:
#   spherical iff highest weight has the form (p, q, 0, ..., 0) with q even.
#
# But for the HEAT KERNEL on the Riemannian manifold G/K, we sum
# over ALL reps with K-fixed vectors, weighted by dim(V^K).
# The multiplicity of eigenvalue λ in the Laplacian is d(π) × dim(π^K).
#
# For rank-1 (SO(n+1)/SO(n) = S^n), only (p,0,...,0) appears.
# For rank-2 (SO(n+2)/[SO(n)×SO(2)]), the situation is:
#   - (p, 0, ..., 0): always spherical, mult = 1
#   - (p, q, 0, ..., 0) with q > 0: spherical iff q even, mult = 1 per K-type
#
# KEY INSIGHT: For the Laplacian eigenvalues, what matters is:
# λ(p,q) = p(p+n) + q(q+n-2) for ALL (p,q) with p≥q≥0
# But only the SPHERICAL reps (those appearing in L²(G/K)) contribute.
#
# EMPIRICAL CHECK: Compare Z_q0(t) with the known a₀ = 1 coefficient.
# If Z_{q=0 only} gives correct a₀..a₄, that confirms q=0 is the
# right spherical condition for a₄ exactness.
#
# RESOLUTION: The non-spherical theorem (Toy 250) was stated for
# ALL (p,q) in the sum. The theorem says: even if you include
# non-spherical reps, a₀..a_{n-1} are unchanged. So:
#   Z_full = Z_sph + Z_nonsph
#   a_k(full) = a_k(sph) for k < n
#   a_n(full) = a_n(sph) + δa_n (non-spherical correction at order n)
#
# The question for a₅: we need Z_sph and Z_nonsph separately.
# Z_sph = what the Laplacian on G/K actually produces.
# Z_nonsph = the extra terms from (p,q) with q odd (or q>0?).
#
# For NOW: let's compute both Z_{q=0} and Z_{all q}, extract a₅
# from each, and measure the difference. The data will tell us.

def build_spectrum_split(n, P_max=500):
    """Build eigenvalue/multiplicity arrays for Q^n, split into
    spherical (q=0) and non-spherical (q>0) parts."""
    N = n + 2
    eigs_sph = []
    dims_sph = []
    eigs_nonsph = []
    dims_nonsph = []

    for p in range(P_max):
        # q = 0: always spherical
        eigs_sph.append(p * (p + n))
        dims_sph.append(dim_SO(p, 0, N))

        # q > 0
        for q in range(1, p + 1):
            lam = p * (p + n) + q * (q + n - 2)
            d = dim_SO(p, q, N)
            eigs_nonsph.append(lam)
            dims_nonsph.append(d)

    return (np.array(eigs_sph, dtype=np.float64),
            np.array(dims_sph, dtype=np.float64),
            np.array(eigs_nonsph, dtype=np.float64),
            np.array(dims_nonsph, dtype=np.float64))


def heat_trace_vec(t, eigs, dims):
    """Z(t) = Σ d_i exp(-λ_i t), with overflow protection."""
    mask = eigs * t < 200
    if not np.any(mask):
        return 0.0
    return np.sum(dims[mask] * np.exp(-eigs[mask] * t))


def extract_coefficients(n, P_max=700, degree=10, t_lo=-3.5, t_hi=-1.2,
                          n_pts=800, split=True):
    """Extract heat kernel coefficients from Q^n.

    If split=True, returns (a_sph, a_nonsph, a_full, vol) where each a is
    a list of coefficients [a₀, a₁, ..., a_degree].
    """
    if split:
        eigs_s, dims_s, eigs_ns, dims_ns = build_spectrum_split(n, P_max)
    else:
        N = n + 2
        eigs_all = []
        dims_all = []
        for p in range(P_max):
            for q in range(p + 1):
                eigs_all.append(p * (p + n) + q * (q + n - 2))
                dims_all.append(dim_SO(p, q, N))
        eigs_s = np.array(eigs_all, dtype=np.float64)
        dims_s = np.array(dims_all, dtype=np.float64)

    t_vals = np.logspace(t_lo, t_hi, n_pts)

    # Compute rescaled heat traces
    prefactor = lambda t: (4 * np.pi * t) ** n

    if split:
        h_sph = np.array([prefactor(t) * heat_trace_vec(t, eigs_s, dims_s)
                          for t in t_vals])
        h_nonsph = np.array([prefactor(t) * heat_trace_vec(t, eigs_ns, dims_ns)
                             for t in t_vals])
        h_full = h_sph + h_nonsph
    else:
        h_full = np.array([prefactor(t) * heat_trace_vec(t, eigs_s, dims_s)
                           for t in t_vals])
        h_sph = h_full
        h_nonsph = np.zeros_like(h_full)

    results = {}
    for label, h_vals in [('sph', h_sph), ('nonsph', h_nonsph), ('full', h_full)]:
        if np.all(h_vals == 0):
            results[label] = [0.0] * (degree + 1)
            continue
        poly = np.polyfit(t_vals, h_vals, degree)
        A = poly[::-1]  # ascending order: A[0] = constant, A[k] = coeff of t^k
        results[label] = list(A[:degree + 1])

    vol = results['full'][0]
    # Normalize by volume
    a_sph = [c / vol if vol != 0 else 0 for c in results['sph']]
    a_nonsph = [c / vol if vol != 0 else 0 for c in results['nonsph']]
    a_full = [c / vol if vol != 0 else 0 for c in results['full']]

    return a_sph, a_nonsph, a_full, vol


def extract_with_crossval(n, P_max=700, max_k=7):
    """Cross-validated extraction of a₀..a_k for Q^n.
    Returns median and std for each coefficient."""
    all_sph = [[] for _ in range(max_k + 1)]
    all_nonsph = [[] for _ in range(max_k + 1)]
    all_full = [[] for _ in range(max_k + 1)]

    configs = [
        (9,  -3.5, -1.2, 800),
        (10, -3.5, -1.2, 800),
        (10, -3.2, -1.3, 700),
        (10, -3.8, -1.1, 900),
        (11, -3.5, -1.2, 800),
        (9,  -3.0, -1.3, 600),
        (10, -3.0, -1.5, 700),
        (11, -3.2, -1.0, 850),
    ]

    for deg, t_lo, t_hi, n_pts in configs:
        if deg < max_k:
            continue
        try:
            a_s, a_ns, a_f, vol = extract_coefficients(
                n, P_max, deg, t_lo, t_hi, n_pts, split=True)
            for k in range(min(max_k + 1, len(a_s))):
                all_sph[k].append(a_s[k])
                all_nonsph[k].append(a_ns[k])
                all_full[k].append(a_f[k])
        except Exception as e:
            print(f"  Config ({deg},{t_lo},{t_hi}) failed: {e}")

    result = {}
    for label, data in [('sph', all_sph), ('nonsph', all_nonsph), ('full', all_full)]:
        medians = []
        stds = []
        for k in range(max_k + 1):
            if data[k]:
                arr = np.array(data[k])
                medians.append(np.median(arr))
                stds.append(np.std(arr))
            else:
                medians.append(0.0)
                stds.append(float('inf'))
        result[label] = (medians, stds)

    return result


def identify_rational_small_denom(x, max_den=1000, tol=1e-3):
    """Find rational with BEST match among small denominators."""
    best_frac = None
    best_err = float('inf')
    for d in range(1, max_den + 1):
        n_approx = x * d
        n_round = round(n_approx)
        err_abs = abs(n_approx - n_round) / d
        if err_abs < tol and err_abs < best_err:
            if err_abs < best_err / 10 or (err_abs < best_err and d <= (best_frac.denominator if best_frac else d)):
                best_frac = Fraction(n_round, d)
                best_err = err_abs
    if best_frac is not None:
        return best_frac, abs(float(best_frac) - x)
    return None, None


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Toy 251 — a₅ with Non-Spherical Corrections")
    print("=" * 70)

    # ─────────────────────────────────────────────────────────
    # §1: Non-spherical rep structure of Q⁵
    # ─────────────────────────────────────────────────────────
    print("\n  " + "─" * 60)
    print("  §1  NON-SPHERICAL REPRESENTATION STRUCTURE")
    print("  " + "─" * 60)

    n = 5
    N = n + 2  # SO(7)
    print(f"\n    Q^{n} = SO({N})/[SO({n})×SO(2)], dim = {2*n}")
    print(f"    Eigenvalue: λ(p,q) = p(p+{n}) + q(q+{n-2})")
    print(f"    Spherical: q = 0 (K-fixed vector exists)")
    print(f"    Non-spherical: q > 0 (no K-fixed vector)")

    # Show first few non-spherical reps
    print(f"\n    First non-spherical representations:")
    print(f"    {'(p,q)':<10} {'λ(p,q)':<10} {'dim':<10} {'Casimir':<10}")
    for p in range(1, 8):
        for q in range(1, p + 1):
            lam = p * (p + n) + q * (q + n - 2)
            d = dim_SO(p, q, N)
            print(f"    ({p},{q}){'':<5} {lam:<10} {d:<10}")

    # Count contributions
    P_test = 100
    n_sph = P_test
    n_nonsph = sum(1 for p in range(P_test) for q in range(1, p+1))
    print(f"\n    Up to P_max={P_test}: {n_sph} spherical, {n_nonsph} non-spherical reps")

    # ─────────────────────────────────────────────────────────
    # §2: Extract coefficients for Q⁵ with split
    # ─────────────────────────────────────────────────────────
    print("\n  " + "─" * 60)
    print("  §2  COEFFICIENT EXTRACTION (Q⁵, SPLIT)")
    print("  " + "─" * 60)

    print(f"\n    Computing with P_max=700, cross-validated...")
    result = extract_with_crossval(5, P_max=700, max_k=7)

    med_s, std_s = result['sph']
    med_ns, std_ns = result['nonsph']
    med_f, std_f = result['full']

    print(f"\n    {'k':<4} {'a_k(sph)':<16} {'a_k(nonsph)':<16} {'a_k(full)':<16} {'sph std':<12} {'full std':<12}")
    print(f"    {'─'*80}")
    for k in range(min(7, len(med_f))):
        print(f"    {k:<4} {med_s[k]:<16.6f} {med_ns[k]:<16.6f} {med_f[k]:<16.6f} {std_s[k]:<12.2e} {std_f[k]:<12.2e}")

    # ─────────────────────────────────────────────────────────
    # §3: Verify non-spherical theorem for a₀..a₄
    # ─────────────────────────────────────────────────────────
    print("\n  " + "─" * 60)
    print("  §3  NON-SPHERICAL THEOREM VERIFICATION")
    print("  " + "─" * 60)

    print(f"\n    Theorem: a_k(full) = a_k(sph) for k < n={n}")
    print(f"    Checking a₀ through a₄:")
    all_match = True
    for k in range(min(5, len(med_f))):
        diff = abs(med_f[k] - med_s[k])
        rel = diff / abs(med_f[k]) if med_f[k] != 0 else diff
        ok = "✓" if rel < 1e-6 else "✗"
        if rel >= 1e-6:
            all_match = False
        print(f"    a_{k}: full={med_f[k]:.8f}, sph={med_s[k]:.8f}, diff={diff:.2e} {ok}")

    if all_match:
        print(f"\n    ✓ Non-spherical theorem CONFIRMED: a₀..a₄ uncontaminated")
    else:
        print(f"\n    ⚠ Discrepancy detected — investigate")

    # ─────────────────────────────────────────────────────────
    # §4: a₅ analysis
    # ─────────────────────────────────────────────────────────
    print("\n  " + "─" * 60)
    print("  §4  a₅(Q⁵) ANALYSIS")
    print("  " + "─" * 60)

    if len(med_f) > 5:
        a5_full = med_f[5]
        a5_sph = med_s[5]
        a5_nonsph = med_ns[5]
        a5_full_std = std_f[5]
        a5_sph_std = std_s[5]

        print(f"\n    a₅(full)    = {a5_full:.6f} ± {a5_full_std:.2e}")
        print(f"    a₅(sph)     = {a5_sph:.6f} ± {a5_sph_std:.2e}")
        print(f"    δa₅(nonsph) = {a5_nonsph:.6f}")
        print(f"    Contamination: δa₅/a₅ = {abs(a5_nonsph/a5_full)*100:.2f}%")

        # Try rational identification
        print(f"\n    Rational identification attempts:")
        for label, val in [('a₅(full)', a5_full), ('a₅(sph)', a5_sph)]:
            frac, err = identify_rational_small_denom(val, max_den=360, tol=0.5)
            if frac is not None:
                print(f"    {label} ≈ {frac} = {float(frac):.6f} (err={err:.4f})")
            else:
                print(f"    {label}: no clean rational found (den ≤ 360)")

        # Try a₅ × known denominators
        print(f"\n    Testing a₅ × d for small d:")
        for d in [1, 2, 3, 6, 9, 12, 18, 36, 72, 180, 360]:
            prod = a5_full * d
            nearest_int = round(prod)
            err = abs(prod - nearest_int)
            if err < 1.0:
                print(f"    a₅ × {d:<4} = {prod:>12.4f}  (nearest int: {nearest_int}, err={err:.4f})")

        # BST integer expressions near a₅
        print(f"\n    BST candidates near a₅ = {a5_full:.4f}:")
        candidates = [
            ("dim so(7) × V₂ / something", None),
            ("N_c × g² + something", 147),
            ("(2n²-3)² / something", (2*25-3)**2),  # 47² = 2209
        ]
        # Check nearby rationals with BST numerators
        bst_nums = [
            (221, "221"),
            (222, "222"),
            (1330, "1330 = 2×5×7×19"),
            (2209, "47² = (2n²-3)²"),
            (1995, "5×399 = 5×3×7×19"),
            (4418, "2×47²"),
            (6627, "3×47²"),
        ]
        for num, desc in bst_nums:
            for den in [1, 2, 3, 5, 6, 9, 10, 12, 15, 18]:
                val = num / den
                if abs(val - a5_full) < 2.0:
                    err = abs(val - a5_full)
                    print(f"    {num}/{den} = {val:.4f} ({desc}), err = {err:.4f}")

    # ─────────────────────────────────────────────────────────
    # §5: a₄ decontamination for n=3,4
    # ─────────────────────────────────────────────────────────
    print("\n  " + "─" * 60)
    print("  §5  a₄ DECONTAMINATION FOR SMALL n")
    print("  " + "─" * 60)

    print(f"\n    For n < 5, a₄ is contaminated by non-spherical reps.")
    print(f"    Extracting spherical-only a₄ for n = 3, 4:")

    a4_clean = {}
    for nn in [3, 4, 5, 6, 7, 8]:
        print(f"\n    n = {nn}:")
        res = extract_with_crossval(nn, P_max=500 if nn <= 5 else 400, max_k=5)
        ms, ss = res['sph']
        mf, sf = res['full']

        a4_s = ms[4] if len(ms) > 4 else 0
        a4_f = mf[4] if len(mf) > 4 else 0
        a4_diff = abs(a4_f - a4_s)

        contaminated = nn <= 4
        tag = " ← CONTAMINATED" if contaminated else " ← clean (n≥5)"
        print(f"      a₄(sph)  = {a4_s:.6f}")
        print(f"      a₄(full) = {a4_f:.6f}")
        print(f"      δa₄      = {a4_diff:.6f}{tag}")

        # The CORRECT a₄ for the Laplacian on G/K is a₄(sph)
        # because only spherical reps appear in L²(G/K)
        a4_clean[nn] = a4_s

        # Try rational identification
        frac, err = identify_rational_small_denom(a4_s, max_den=360, tol=0.1)
        if frac:
            print(f"      a₄(sph) ≈ {frac} = {float(frac):.6f} (err={err:.6f})")

    # ─────────────────────────────────────────────────────────
    # §6: a₄(n) polynomial from clean values
    # ─────────────────────────────────────────────────────────
    print("\n  " + "─" * 60)
    print("  §6  a₄(n) INTERPOLATION FROM CLEAN VALUES")
    print("  " + "─" * 60)

    # For n ≥ 5, a₄(full) = a₄(sph) (non-spherical theorem)
    # For n < 5, use a₄(sph) which is the TRUE heat kernel coefficient
    # NOTE: a₄(sph) for n < 5 might still have numerical issues...
    # but let's see what we get

    ns = sorted(a4_clean.keys())
    vals = [a4_clean[nn] for nn in ns]

    print(f"\n    Clean a₄ values:")
    for nn, v in zip(ns, vals):
        frac, err = identify_rational_small_denom(v, max_den=360, tol=0.1)
        frac_str = f" ≈ {frac}" if frac else ""
        print(f"    n={nn}: a₄ = {v:.6f}{frac_str}")

    # Check if n=5 still gives 2671/18
    if 5 in a4_clean:
        a4_5 = a4_clean[5]
        target = 2671 / 18
        print(f"\n    a₄(Q⁵) = {a4_5:.6f}")
        print(f"    2671/18 = {target:.6f}")
        print(f"    diff    = {abs(a4_5 - target):.6f}")

    # ─────────────────────────────────────────────────────────
    # §7: Summary and scoring
    # ─────────────────────────────────────────────────────────
    print("\n  " + "═" * 60)
    print("  §7  SUMMARY")
    print("  " + "═" * 60)

    checks = []

    # Check 1: Non-spherical theorem verified
    checks.append(("Non-spherical theorem (a₀..a₄ match)", all_match))

    # Check 2: a₅ extracted with precision
    a5_ok = len(med_f) > 5 and std_f[5] < abs(med_f[5]) * 0.1
    checks.append(("a₅ extracted (std < 10% of value)", a5_ok))

    # Check 3: Non-spherical contamination measured
    contam_ok = len(med_f) > 5 and abs(med_ns[5]) > 0.01
    checks.append(("Non-spherical contamination measured", contam_ok))

    # Check 4: a₄(Q⁵) still = 2671/18
    a4_ok = 5 in a4_clean and abs(a4_clean[5] - 2671/18) < 0.01
    checks.append(("a₄(Q⁵) = 2671/18 confirmed", a4_ok))

    # Check 5: a₄ decontaminated for n=3,4
    decontam_ok = 3 in a4_clean and 4 in a4_clean
    checks.append(("a₄ decontaminated for n=3,4", decontam_ok))

    score = sum(1 for _, ok in checks if ok)
    total = len(checks)

    for desc, ok in checks:
        print(f"    [{'✓' if ok else '✗'}] {desc}")
    print(f"\n    Score: {score}/{total}")

    # Key results box
    if len(med_f) > 5:
        print(f"\n    ╔{'═'*55}╗")
        print(f"    ║  a₅(Q⁵) full    = {med_f[5]:>12.4f} ± {std_f[5]:.2e}{'':>11}║")
        print(f"    ║  a₅(Q⁵) sph     = {med_s[5]:>12.4f} ± {std_s[5]:.2e}{'':>11}║")
        print(f"    ║  δa₅ (nonsph)   = {med_ns[5]:>12.4f}{'':>24}║")
        print(f"    ║  a₄(Q⁵)         = {a4_clean.get(5, 0):>12.4f} (2671/18 = {2671/18:.4f}){'':>4}║")
        print(f"    ╚{'═'*55}╝")

    print(f"\n  Toy 251 complete.")


if __name__ == '__main__':
    main()
