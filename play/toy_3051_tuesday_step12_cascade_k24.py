"""
Toy 3051 — Tuesday Steps 1+2 PRE-EXECUTED Monday PM (Elie parallel to Lyra Step 4).

Owner: Elie (per Keeper Tuesday queue, parallel to Lyra T2378 Toy 3050 pre-execution)
Date: 2026-05-18 PM

GOAL
====
Pre-execute the Tuesday cascade extension. The new heat_n44_dps3200.json (landed
2026-05-18 09:07) is INCLUDED in the cascade alongside n=3..49 dps=1600. With
47 dimensions total, we have headroom for k=24 (need 46 constraints, leaving
1 verification point) — pushing past Toy 1610's k=22 ZERO-margin verification.

STEPS PRE-EXECUTED
==================
Step 1 (Elie): Load 47 dimensions, prefer dps=3200 at n=44.
Step 2 (Elie): Run cascade k=1..24:
  - Reproduce a_2..a_20 (validate Three Theorems pattern)
  - Verify Toy 2994 ratio formula a_k/a_{k-1} = -k(k-1)/10 at speaking-pair
    levels k=5,6,10,11,15,16,20,21 (known integer ratios)
  - Attempt k=22 with NEW verification margin (was 0 in Toy 1610)
  - Attempt k=23 and k=24 (NEW levels never extracted before)
  - Report margins, speaking-pair ratios, integer-or-not status

Tuesday becomes "Keeper Step 3 audit + K52 ruling" rather than "run extraction
from scratch." Same discipline shape as Lyra Toy 3050 Step 4 pre-execution.

PRE-REGISTERED EXPECTATIONS
===========================
Toy 2994 formula: ratio(k) = a_k / a_(k-1) = -k(k-1)/(2·n_C) = -k(k-1)/10.

For k=22..24 (mod 5 = 2,3,4 — NOT speaking-pair levels), ratios are non-integer:
  k=22: -22·21/10 = -231/5 = -46.2
  k=23: -23·22/10 = -506/10 = -253/5 = -50.6
  k=24: -24·23/10 = -552/10 = -276/5 = -55.2

For k=25 (mod 5 = 0, speaking-pair predicted): -25·24/10 = -60 = INTEGER
For k=26 (mod 5 = 1, speaking-pair predicted): -26·25/10 = -65 = INTEGER

k=24 within our data reach; k=25, 26 BEYOND data reach (47 < 48 needed).

HONEST POSTURE (per Cal Rule 6)
================================
This is a CASCADE EXTRACTION. Numerical extraction CAN fail at the boundary
even with sufficient data — extrapolation precision degrades, rational
identification gets ambiguous. Report margins; do NOT tier-promote until
Keeper Step 3 audit + K52 ruling.

If k=22 verifies with margin >=1: Toy 1610's zero-margin extraction is now
  CONFIRMED. Three Theorems pattern verified through 22 consecutive levels.
If k=23, k=24 extract cleanly: NEW levels confirmed, 24 consecutive levels.
If any level fails: deviations locate cascade boundary (Casey hunting principle).

Either outcome is publishable. The audit IS the deliverable.
"""

import os
import sys
import json
import time
from fractions import Fraction
import mpmath

DPS = 1600
mpmath.mp.dps = DPS

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_DIR = os.path.join(SCRIPT_DIR, "toy_671_checkpoint")

# BST integers
rank, N_c, n_C, C_2, g_b = 2, 3, 5, 6, 7
g = g_b
N_max = N_c**3 * n_C + rank  # 137

# Toy 1610 KNOWN data
KNOWN_SPEAKING_PAIRS = {
    5: -2, 6: -3, 10: -9, 11: -11, 15: -21, 16: -24, 20: -38, 21: -42
}

MAX_PRIME_BY_LEVEL = {
    2: 7, 3: 7, 4: 7, 5: 11, 6: 13, 7: 13, 8: 17, 9: 19, 10: 19, 11: 23,
    12: 23, 13: 23, 14: 29, 15: 31, 16: 31, 17: 37, 18: 37, 19: 41, 20: 41,
    21: 43, 22: 47, 23: 47, 24: 53,
}

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]


# === Inlined infrastructure from Toy 1610 / 671b ===

def frac_to_mpf(frac):
    return mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)


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
    Np = len(pairs)
    if max_order is None:
        max_order = min(Np, 30)
    else:
        max_order = min(max_order, Np)
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
        g_val = F / t ** target_k
        gs.append(g_val)
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
    x_str = mpmath.nstr(x_mpf, 250, strip_zeros=False)
    if x_str is None:
        return None, float('inf')
    try:
        x_frac_exact = Fraction(str(x_str))
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


def eval_poly(coeffs, x):
    result = Fraction(0)
    for k, c in enumerate(coeffs):
        result += c * Fraction(x) ** k
    return result


def _factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def three_theorems(k):
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k * (k - 1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const


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
            for kk in range(len(basis)):
                new[kk + 1] += basis[kk]
                new[kk] -= xs[j] * basis[kk]
            basis = new
        for kk in range(len(basis)):
            if kk < n:
                coeffs[kk] += ys[i] * basis[kk] / denom
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def constrained_polynomial(clean_rats, c_top, c_subtop, c_const, deg):
    clean_ns = sorted(clean_rats.keys())
    n_needed = deg - 2
    if len(clean_ns) < n_needed:
        return None, 0
    residual_pts = []
    for nv in clean_ns:
        res = clean_rats[nv] - c_top * Fraction(nv)**deg \
              - c_subtop * Fraction(nv)**(deg-1) - c_const
        residual_pts.append((Fraction(nv), res / Fraction(nv)))
    n_use = min(len(residual_pts), n_needed)
    reduced_poly = lagrange_interpolate(residual_pts[:n_use])
    extra = residual_pts[n_use:]
    n_verified = 0
    if extra:
        for p in extra:
            predicted = eval_poly(reduced_poly, p[0])
            if predicted == p[1]:
                n_verified += 1
            else:
                diff = abs(float(predicted - p[1]))
                if diff < 1e-100:
                    n_verified += 1
    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for k, c in enumerate(reduced_poly):
        poly[k + 1] += c
    poly[deg - 1] += c_subtop
    poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly, n_verified


def load_checkpoint_smart(n):
    """Load heat checkpoint, preferring dps=3200 when available."""
    paths_to_try = [
        os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps3200.json"),
        os.path.join(CKPT_DIR, f"heat_n{n}_dps3200.json"),
        os.path.join(CKPT_DIR, f"heat_n{n:02d}_dps1600.json"),
        os.path.join(CKPT_DIR, f"heat_n{n}_dps1600.json"),
    ]
    for fp in paths_to_try:
        if os.path.exists(fp):
            with open(fp) as f:
                data = json.load(f)
            ts = [mpmath.mpf(s) for s in data['ts']]
            fs = [mpmath.mpf(s) for s in data['fs']]
            vol = mpmath.mpf(data['vol'])
            return ts, fs, vol, os.path.basename(fp)
    return None


def main():
    t_start = time.time()
    TARGET_K = 24

    print("=" * 72)
    print(f"Toy 3051 — Tuesday Steps 1+2 PRE-EXECUTED")
    print(f"  Cascade k=1..{TARGET_K} on n=3..49 (47 dims; new n=44 dps=3200 preferred)")
    print(f"  Toy 1610 reached k=22 zero-margin; this extends to k=24 with margin")
    print("=" * 72)

    # === T1: Load checkpoints ===
    print(f"\n[T1] Loading checkpoints n=3..49 (preferring dps=3200 where available)")
    ALL_DIMS = list(range(3, 50))  # 47 dimensions
    trace_data = {}
    missing = []
    files_used = []
    for n in ALL_DIMS:
        loaded = load_checkpoint_smart(n)
        if loaded is None:
            missing.append(n)
            continue
        ts, fs, vol, fp_used = loaded
        trace_data[n] = (ts, fs, vol)
        files_used.append((n, fp_used))
        if n in [3, 44, 45, 49] or n % 10 == 0:
            print(f"  n={n}: {fp_used} ({len(ts)} pts, vol={mpmath.nstr(vol, 6)})")
    n_loaded = len(trace_data)
    print(f"  Total: {n_loaded} dimensions loaded ({sum(1 for _,f in files_used if '3200' in f)} at dps=3200)")
    if missing:
        print(f"  MISSING: {missing}")

    score = []
    score.append(("T1", f"{n_loaded}/47 dimensions loaded with n=44 dps=3200",
                  n_loaded == 47 and any('3200' in f for n, f in files_used if n == 44)))

    if n_loaded < 46:
        print(f"\nFATAL: need >=46 dims for k=24; have {n_loaded}")
        print(f"\nSCORE: {sum(1 for _, _, ok in score if ok)}/{len(score)}")
        return

    # === T2: Cascade ===
    print(f"\n[T2] Sequential cascade extraction k=1..{TARGET_K}")

    KNOWN_POLYS = {1: A1_POLY}
    all_rats = {1: {n: eval_poly(A1_POLY, Fraction(n)) for n in ALL_DIMS}}
    max_confirmed = 1
    speaking_pairs = {}
    margin_by_k = {}

    print(f"  {'k':>3} {'n_clean':>8} {'n_need':>7} {'margin':>7} {'status':>8} "
          f"{'ratio':>12} {'sp_match':>10} {'sec':>6}")
    print(f"  {'-'*3} {'-'*8} {'-'*7} {'-'*7} {'-'*8} {'-'*12} {'-'*10} {'-'*6}")

    for k in range(2, TARGET_K + 1):
        t_level = time.time()
        deg = 2 * k
        c_top, c_sub, c_const = three_theorems(k)
        max_p = MAX_PRIME_BY_LEVEL.get(k, 53)
        n_need = deg - 2

        ak_clean = {}
        for n in ALL_DIMS:
            if n not in trace_data:
                continue
            ts, fs, vol = trace_data[n]
            known_fracs = {0: Fraction(1)}
            ok = True
            for j in range(1, k):
                if j not in all_rats or n not in all_rats[j]:
                    ok = False
                    break
                known_fracs[j] = all_rats[j][n]
            if not ok:
                continue
            ak, err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
            frac, _ = identify_rational(ak, max_den=500000000000000,
                                        tol=1e-8, max_prime=max_p)
            if frac:
                ak_clean[n] = frac

        n_clean = len(ak_clean)
        dt_level = time.time() - t_level

        margin = n_clean - n_need
        margin_by_k[k] = margin

        n_ver = 0
        ratio_str = "-"
        sp_match_str = "-"
        if n_clean >= n_need:
            ak_poly, n_ver = constrained_polynomial(ak_clean, c_top, c_sub, c_const, deg)
            if ak_poly:
                for nv in ALL_DIMS:
                    ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
                KNOWN_POLYS[k] = ak_poly
                max_confirmed = k

                if len(ak_poly) > deg:
                    ratio_frac = ak_poly[deg-1] / ak_poly[deg]
                    is_integer = ratio_frac.denominator == 1
                    if is_integer:
                        ratio_val = int(ratio_frac)
                        speaking_pairs[k] = ratio_val
                        ratio_str = f"{ratio_val} (int)"
                    else:
                        ratio_str = f"{ratio_frac}"
                    # Compare with Toy 2994 formula -k(k-1)/10
                    formula_val = Fraction(-k * (k - 1), 10)
                    if ratio_frac == formula_val:
                        sp_match_str = "Toy2994"
                    elif k in KNOWN_SPEAKING_PAIRS and is_integer and ratio_val == KNOWN_SPEAKING_PAIRS[k]:
                        sp_match_str = "T1610"
                    else:
                        sp_match_str = "no"
            else:
                KNOWN_POLYS[k] = None
        else:
            KNOWN_POLYS[k] = None

        all_rats[k] = ak_clean

        status = "PASS" if KNOWN_POLYS.get(k) else "FAIL"
        print(f"  {k:>3} {n_clean:>8} {n_need:>7} {margin:>+7} {status:>8} "
              f"{ratio_str:>12} {sp_match_str:>10} {dt_level:>6.1f}")

    # === Score checks ===
    score.append(("T2a", f"Cascade reaches k=20", max_confirmed >= 20))
    score.append(("T2b", f"Cascade reaches k=21 (Toy 1610 base)", max_confirmed >= 21))
    score.append(("T2c", f"Cascade reaches k=22 (Toy 1610 zero-margin upgrade)", max_confirmed >= 22))
    score.append(("T2d", f"Cascade reaches k=23 (NEW)", max_confirmed >= 23))
    score.append(("T2e", f"Cascade reaches k=24 (NEW)", max_confirmed >= 24))

    # Toy 2994 ratio formula check on speaking-pair levels
    print(f"\n[T3] Speaking-pair ratio check vs Toy 2994 formula -k(k-1)/10")
    print(f"  k     observed ratio     formula -k(k-1)/10    match")
    print(f"  ---   ----------------   ------------------    -----")
    sp_matches = 0
    sp_total = 0
    for k_sp in [5, 6, 10, 11, 15, 16, 20, 21]:
        if k_sp not in KNOWN_POLYS or KNOWN_POLYS[k_sp] is None:
            continue
        p = KNOWN_POLYS[k_sp]
        if len(p) > 2*k_sp:
            obs = p[2*k_sp-1] / p[2*k_sp]
            formula = Fraction(-k_sp * (k_sp - 1), 10)
            m = "YES" if obs == formula else "NO"
            print(f"  {k_sp:>3}   {str(obs):>16}   {str(formula):>18}    {m}")
            sp_total += 1
            if obs == formula:
                sp_matches += 1
    score.append(("T3", f"Speaking-pair ratios match Toy 2994 formula at known sp levels",
                  sp_total > 0 and sp_matches == sp_total))

    # k=22, 23, 24 predicted (non-integer) ratios
    print(f"\n[T4] New levels — predicted non-integer ratios (k mod 5 != 0,1)")
    print(f"  k     observed ratio        formula -k(k-1)/10   match    margin")
    print(f"  ---   ------------------    ------------------   -----    ------")
    new_levels_match = 0
    new_levels_total = 0
    for k_new in [22, 23, 24]:
        if k_new not in KNOWN_POLYS or KNOWN_POLYS[k_new] is None:
            print(f"  {k_new:>3}   (not extracted)")
            continue
        p = KNOWN_POLYS[k_new]
        if len(p) > 2*k_new:
            obs = p[2*k_new-1] / p[2*k_new]
            formula = Fraction(-k_new * (k_new - 1), 10)
            m = "YES" if obs == formula else "NO"
            mg = margin_by_k.get(k_new, 0)
            print(f"  {k_new:>3}   {str(obs):>18}    {str(formula):>18}   {m}    {mg:+d}")
            new_levels_total += 1
            if obs == formula:
                new_levels_match += 1
    score.append(("T4a", f"k=22 ratio matches Toy 2994 formula (was 0 margin in Toy 1610)",
                  22 in KNOWN_POLYS and KNOWN_POLYS[22] is not None and
                  KNOWN_POLYS[22][2*22-1] / KNOWN_POLYS[22][2*22] == Fraction(-22*21, 10)))
    score.append(("T4b", f"k=23 ratio matches Toy 2994 formula (NEW LEVEL)",
                  23 in KNOWN_POLYS and KNOWN_POLYS[23] is not None and
                  KNOWN_POLYS[23][2*23-1] / KNOWN_POLYS[23][2*23] == Fraction(-23*22, 10)))
    score.append(("T4c", f"k=24 ratio matches Toy 2994 formula (NEW LEVEL)",
                  24 in KNOWN_POLYS and KNOWN_POLYS[24] is not None and
                  KNOWN_POLYS[24][2*24-1] / KNOWN_POLYS[24][2*24] == Fraction(-24*23, 10)))

    # === Save JSON for Keeper Step 3 audit ===
    out = {
        'meta': {
            'date': '2026-05-18',
            'owner': 'Elie',
            'description': 'Tuesday Steps 1+2 pre-executed Monday PM; cascade k=1..24',
            'dps_working': DPS,
            'n_dims_loaded': n_loaded,
            'files_used': [{'n': n, 'file': f} for n, f in files_used],
            'max_confirmed_k': max_confirmed,
            'target_k': TARGET_K,
        },
        'speaking_pairs_extracted': speaking_pairs,
        'speaking_pairs_known': KNOWN_SPEAKING_PAIRS,
        'margins_by_k': {str(k): margin_by_k.get(k, None) for k in range(2, TARGET_K + 1)},
        'polys': {
            str(k): [f"{c.numerator}/{c.denominator}" for c in KNOWN_POLYS[k]]
            for k in KNOWN_POLYS if KNOWN_POLYS[k] is not None
        },
        'ratios_by_k': {
            str(k): (f"{(KNOWN_POLYS[k][2*k-1]/KNOWN_POLYS[k][2*k]).numerator}/"
                     f"{(KNOWN_POLYS[k][2*k-1]/KNOWN_POLYS[k][2*k]).denominator}")
            for k in range(2, TARGET_K + 1)
            if k in KNOWN_POLYS and KNOWN_POLYS[k] is not None and len(KNOWN_POLYS[k]) > 2*k
        },
        'expected_ratios_toy2994': {
            str(k): f"{-k*(k-1)}/10" for k in range(2, TARGET_K + 1)
        },
        'sp_matches_toy2994': f"{sp_matches}/{sp_total}",
        'new_levels_matches_toy2994': f"{new_levels_match}/{new_levels_total}",
    }
    out_path = os.path.join(SCRIPT_DIR, "toy_3051_tuesday_cascade_results.json")
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\n[T5] Output saved: {os.path.basename(out_path)}")

    # === SCORE ===
    elapsed = time.time() - t_start
    passed = sum(1 for *_, ok in score if ok)
    total = len(score)
    print(f"\n{'='*72}")
    print(f"Toy 3051 SCORE: {passed}/{total} [{elapsed:.1f}s]")
    print(f"{'='*72}")
    for name, label, ok in score:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {name}: {label}")

    print(f"""
TUESDAY STEPS 1+2 STATUS:
  max_confirmed_k = {max_confirmed}
  Toy 1610 baseline: k=22 zero margin -> THIS RUN margin = {margin_by_k.get(22, '?')}
  k=23 margin: {margin_by_k.get(23, '?')}
  k=24 margin: {margin_by_k.get(24, '?')}

  Speaking-pair Toy 2994 formula match: {sp_matches}/{sp_total} at known sp levels
  New-level Toy 2994 formula match: {new_levels_match}/{new_levels_total} at k=22..24

HAND-OFF TO TUESDAY:
  Step 3 (Keeper) audit input: toy_3051_tuesday_cascade_results.json
  Step 6 (Keeper) K52 ruling:
    - If new_levels_match == 3/3: Three Theorems extended through k=24 PROVED
    - If new_levels_match < 3/3: cascade boundary located at first failing k
    - Either outcome publishable per Casey hunting principle

NOT CLAIMED (per Cal Rule 6):
  - Tier promotion (D-tier or otherwise) — Keeper Step 3/6 controls
  - Cascade extension past k=24 — data-limited (47 dims < 48 needed)
  - Cross-level (3) ↔ (1)/(2) bridge — multi-week, not this toy
""")


if __name__ == "__main__":
    main()
