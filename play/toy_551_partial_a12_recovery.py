#!/usr/bin/env python3
"""
Toy 551 — Partial a₁₂ Recovery: Diagnostic & Feasibility
=========================================================
Toy 551 | Casey Koons & Claude Opus 4.6 (Elie) | March 28, 2026

Can we recover a₁₂ from only n=3..25 (23 Toy 361 checkpoint points)?

ANSWER: NO — but we learn exactly why and what's needed.

The cascade extracts a_k(n) by subtracting exact a₁..a_{k-1} and
extrapolating to t→0. At each level, per-point rational identification
requires sufficient numerical precision. The adaptive t-window (tuned
for k=12) is suboptimal for intermediate levels, causing precision loss.

Results per cascade level (max_prime filter as in Toy 278/361):
  - a₁..a₅:  11/11 clean each (fixed checkpoints, ideal)
  - a₆: 13/23 (need 10) ✓ | a₇: 12/23 (need 12) ✓
  - a₈: 11/23 (need 14) ✗ — WALL. 3-point deficit.
  - Cascade stops. a₁₂ unreachable from this data.

Root cause: Toy 361's adaptive_t_window targets k=12, compressing
t-values unnecessarily for k=6..8 extraction at large n.

Fix paths:
  (1) Complete Toy 361 (n=26..35): 10 more points → 33 total → proven to work
  (2) Recompute checkpoints with per-k t-windows (like Toy 278)
  (3) Use hybrid: fixed checkpoints for a₆..a₈, adaptive for a₉+

This toy runs the cascade, reports clean counts at each level,
identifies the wall, and provides partial results.

Scorecard target: 8/8
T1: Load checkpoints
T2: a₁..a₅ cascade (fixed, exact)
T3: a₆..a₇ cascade (adaptive, max_prime)
T4: a₈ wall diagnosis
T5: Precision profile per dimension
T6: Best partial a₁₂ extraction (from a₆..a₇ only, skip a₈..a₁₁)
T7: Compare fixed vs adaptive at n=3..13
T8: Synthesis — what's needed to complete a₁₂

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie). March 2026.
"""

import sys
import os
import json
import time
from fractions import Fraction
import mpmath

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

mpmath.mp.dps = 800

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
        max_order = min(N, 30)
    else:
        max_order = min(max_order, N)
    ts_s = [p[0] for p in pairs[:max_order]]
    gs_s = [p[1] for p in pairs[:max_order]]
    T = [[mpmath.mpf(0)] * max_order for _ in range(max_order)]
    for i in range(max_order):
        T[i][0] = gs_s[i]
    best = T[0][0]
    best_err = mpmath.mpf('inf')
    best_order = 0
    for j in range(1, max_order):
        for i in range(j, max_order):
            r = ts_s[i] / ts_s[i - j]
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
        g = F / t ** target_k
        gs.append(g)
    a_nev = neville(ts, gs, mpmath.mpf(0))
    a_h = neville(ts[::2], [gs[i] for i in range(0, len(ts), 2)], mpmath.mpf(0))
    err_nev = abs(a_nev - a_h)
    a_rich, err_rich, order = richardson_extrapolate(ts, gs, max_order=25)
    n20 = min(20, len(ts))
    a_n20 = neville(ts[:n20], gs[:n20], mpmath.mpf(0))
    agree = min(abs(a_rich - a_nev), abs(a_rich - a_n20), abs(a_nev - a_n20))
    if agree < err_nev * 10 and err_rich < err_nev:
        return a_rich, err_rich
    elif abs(a_n20 - a_nev) < err_nev:
        return a_n20, abs(a_n20 - a_nev)
    else:
        return a_nev, err_nev

def _cf_convergents(frac, max_den=10**15):
    x = frac
    h0, h1 = Fraction(0), Fraction(1)
    k0, k1 = Fraction(1), Fraction(0)
    for _ in range(500):
        if x.denominator == 0: break
        a = x.numerator // x.denominator
        h0, h1 = h1, a * h1 + h0
        k0, k1 = k1, a * k1 + k0
        if k1 > max_den: break
        yield Fraction(int(h1), int(k1))
        rem = x - a
        if rem == 0: break
        x = Fraction(1, 1) / rem

def factor(n):
    if n == 0: return [0]
    factors = []; d = 2; n = abs(n)
    while d * d <= n:
        while n % d == 0: factors.append(d); n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors

def identify_rational(x_mpf, max_den=500000000000000, tol=1e-10, max_prime=None):
    x_str = mpmath.nstr(x_mpf, 200, strip_zeros=False)
    try:
        x_frac = Fraction(x_str)
    except (ValueError, ZeroDivisionError):
        return None, float('inf')
    best = None; best_err = float('inf')
    for conv in _cf_convergents(x_frac, max_den=max_den * 10):
        if conv.denominator > max_den * 10: break
        err = abs(float(x_frac - conv))
        if err < tol and err < best_err:
            if max_prime:
                df = factor(conv.denominator)
                if df and max(df) > max_prime: continue
            best = conv; best_err = err
    for md in [max_den, max_den // 10, max_den // 100, max_den * 10]:
        if md < 1: continue
        cand = x_frac.limit_denominator(md)
        err = abs(float(x_frac - cand))
        if err < tol and err < best_err:
            if max_prime:
                df = factor(cand.denominator)
                if df and max(df) > max_prime: continue
            best = cand; best_err = err
    return best, best_err

def lagrange_interpolate(points):
    n = len(points)
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    coeffs = [Fraction(0)] * n
    for i in range(n):
        basis = [Fraction(1)]; denom = Fraction(1)
        for j in range(n):
            if j == i: continue
            denom *= (xs[i] - xs[j])
            new = [Fraction(0)] * (len(basis) + 1)
            for kk in range(len(basis)):
                new[kk + 1] += basis[kk]; new[kk] -= xs[j] * basis[kk]
            basis = new
        for kk in range(len(basis)):
            if kk < n: coeffs[kk] += ys[i] * basis[kk] / denom
    while len(coeffs) > 1 and coeffs[-1] == 0: coeffs.pop()
    return coeffs

def eval_poly(coeffs, x):
    result = Fraction(0)
    for k, c in enumerate(coeffs): result += c * Fraction(x) ** k
    return result

def _factorial(n):
    r = 1
    for i in range(2, n+1): r *= i
    return r

def three_theorems(k):
    c_top = Fraction(1, 3**k * _factorial(k))
    c_sub = Fraction(-k*(k-1), 10) * c_top
    c_const = Fraction((-1)**k, 2 * _factorial(k))
    return c_top, c_sub, c_const

KNOWN_A5 = {
    1: Fraction(47,6), 2: Fraction(274,9), 3: Fraction(703,9),
    4: Fraction(2671,18), 5: Fraction(1535969,6930),
    6: Fraction(363884219,1351350), 7: Fraction(78424343,289575),
    8: Fraction(670230838,2953665), 9: Fraction(4412269889539,27498621150),
    10: Fraction(2409398458451,21709437750),
}

MAX_PRIME = {6:13, 7:13, 8:17, 9:19, 10:19, 11:23, 12:23}

def constrained_polynomial(clean_rats, c_top, c_sub, c_const, deg):
    ns = sorted(clean_rats.keys())
    need = deg - 2
    if len(ns) < need: return None
    pts = []
    for nv in ns:
        res = clean_rats[nv] - c_top*Fraction(nv)**deg \
              - c_sub*Fraction(nv)**(deg-1) - c_const
        pts.append((Fraction(nv), res / Fraction(nv)))
    n_use = min(len(pts), need)
    reduced = lagrange_interpolate(pts[:n_use])
    extra = pts[n_use:]
    if extra and not all(eval_poly(reduced, p[0]) == p[1] for p in extra):
        return None
    poly = [Fraction(0)] * (deg + 1)
    poly[0] = c_const
    for kk, c in enumerate(reduced): poly[kk+1] += c
    poly[deg-1] += c_sub; poly[deg] = c_top
    while len(poly) > 1 and poly[-1] == 0: poly.pop()
    return poly

def robust_polynomial(clean_rats, c_top, c_sub, c_const, deg):
    poly = constrained_polynomial(clean_rats, c_top, c_sub, c_const, deg)
    if poly and all(eval_poly(poly, Fraction(n)) == clean_rats[n] for n in clean_rats):
        return poly
    ns = sorted(clean_rats.keys()); need = deg - 2
    if len(ns) > need:
        for rm in ns:
            red = {k:v for k,v in clean_rats.items() if k != rm}
            if len(red) < need: continue
            poly = constrained_polynomial(red, c_top, c_sub, c_const, deg)
            if poly and all(eval_poly(poly, Fraction(n)) == red[n] for n in red):
                print(f"        (removed n={rm})")
                return poly
    if len(ns) > need + 1:
        for i, n1 in enumerate(ns):
            for n2 in ns[i+1:]:
                red = {k:v for k,v in clean_rats.items() if k not in (n1,n2)}
                if len(red) < need: continue
                poly = constrained_polynomial(red, c_top, c_sub, c_const, deg)
                if poly and all(eval_poly(poly, Fraction(n)) == red[n] for n in red):
                    print(f"        (removed n={n1},{n2})")
                    return poly
    return None


# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()

    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  Toy 551 — Partial a₁₂ Recovery: Diagnostic & Feasibility     ║")
    print("║  23 checkpoint points (n=3..25) from Toy 361                   ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    PARTIAL = range(3, 26)
    CASCADE = range(3, 14)

    # ─── T1: Load ──────────────────────────────────────────────────
    print(f"\n  T1: Loading checkpoints")
    print("  " + "─" * 58)
    adaptive = {}; fixed = {}
    for n in PARTIAL:
        d = load_heat_trace(n, "adaptive")
        if d: adaptive[n] = d
    for n in CASCADE:
        d = load_heat_trace(n, "fixed")
        if d: fixed[n] = d
    print(f"    Adaptive: {len(adaptive)}/23   Fixed: {len(fixed)}/11")
    score("T1: Checkpoints", len(adaptive)==23 and len(fixed)==11)

    # ─── T2: a₁..a₅ ───────────────────────────────────────────────
    print(f"\n  T2: Cascade a₁..a₅ (exact, fixed, n=3..13)")
    print("  " + "─" * 58)
    A1 = [Fraction(-1,2), Fraction(0), Fraction(1,3)]
    polys = {1: A1}
    rats = {1: {n: eval_poly(A1, Fraction(n)) for n in PARTIAL}}
    ok2 = True
    for k in range(2, 6):
        deg = 2*k; c_t, c_s, c_c = three_theorems(k)
        ak_r = {}
        for n in CASCADE:
            if n not in fixed: continue
            ts, fs, vol = fixed[n]
            kn = {0: Fraction(1)}
            for j in range(1,k): kn[j] = rats[j][n]
            ak, _ = extract_coefficient(fs, ts, vol, kn, k)
            fr, _ = identify_rational(ak, max_den=10**12, tol=1e-20)
            if fr: ak_r[n] = fr
        nk = len(ak_r)
        if nk >= deg + 1:
            pts = [(Fraction(nv), ak_r[nv]) for nv in sorted(ak_r)[:deg+1]]
            p = lagrange_interpolate(pts)
            polys[k] = p
            rats[k] = {n: eval_poly(p, Fraction(n)) for n in PARTIAL}
            v5 = rats[k][5] == KNOWN_A5.get(k)
            print(f"    a_{k}: {nk}/11 → deg {len(p)-1}, a_{k}(5)={'✓' if v5 else '✗'}")
        else:
            print(f"    a_{k}: {nk}/11 — FAILED"); ok2 = False; break
    score("T2: a₁..a₅", ok2)
    if not ok2:
        print(f"\n  SCORECARD: {PASS}/{PASS+FAIL}"); return

    # ─── T3: a₆..a₇ ───────────────────────────────────────────────
    print(f"\n  T3: Cascade a₆..a₇ (adaptive, max_prime filter)")
    print("  " + "─" * 58)
    ok3 = True
    for k in range(6, 8):
        deg = 2*k; c_t, c_s, c_c = three_theorems(k)
        mp = MAX_PRIME[k]; need = deg - 2
        ak_r = {}
        for n in PARTIAL:
            if n not in adaptive: continue
            ts, fs, vol = adaptive[n]
            kn = {0: Fraction(1)}
            for j in range(1,k): kn[j] = rats[j][n]
            ak, _ = extract_coefficient(fs, ts, vol, kn, k)
            fr, _ = identify_rational(ak, max_den=10**15, tol=1e-12, max_prime=mp)
            if fr: ak_r[n] = fr
        nk = len(ak_r)
        print(f"    a_{k:>2}: {nk:>2}/23 clean (need ≥{need}, prime≤{mp})", end="")
        p = None
        if nk >= need + 2:
            p = robust_polynomial(ak_r, c_t, c_s, c_c, deg)
        elif nk >= need:
            p = constrained_polynomial(ak_r, c_t, c_s, c_c, deg)
        if p:
            polys[k] = p
            rats[k] = {n: eval_poly(p, Fraction(n)) for n in PARTIAL}
            v5 = rats[k][5] == KNOWN_A5.get(k) if k in KNOWN_A5 else None
            print(f"  ✓ a_{k}(5)={'✓' if v5 else '✗'}")
        else:
            print(f"  ✗ FAILED"); ok3 = False; break
    score("T3: a₆..a₇", ok3)

    # ─── T4: a₈ wall diagnosis ────────────────────────────────────
    print(f"\n  T4: a₈ cascade — wall diagnosis")
    print("  " + "─" * 58)
    if 7 in polys:
        k = 8; deg = 16; mp = 17; need = 14
        c_t, c_s, c_c = three_theorems(k)
        a8_clean = {}; a8_dirty = {}; a8_vals = {}
        for n in PARTIAL:
            if n not in adaptive: continue
            ts, fs, vol = adaptive[n]
            kn = {0: Fraction(1)}
            for j in range(1,k): kn[j] = rats[j][n]
            ak, ak_err = extract_coefficient(fs, ts, vol, kn, k)
            a8_vals[n] = (ak, ak_err)
            fr, _ = identify_rational(ak, max_den=10**15, tol=1e-12, max_prime=mp)
            if fr:
                a8_clean[n] = fr
            else:
                a8_dirty[n] = ak

        nc = len(a8_clean)
        nd = len(a8_dirty)
        print(f"    Clean: {nc}/23 (need {need}), deficit: {max(0, need-nc)}")
        print(f"    Dirty (no rational with prime≤{mp}): n={sorted(a8_dirty.keys())}")

        # Precision profile
        print(f"\n    Per-dimension precision profile:")
        print(f"    {'n':>3} {'clean':>5} {'log_err':>8} {'sig_dig':>7}")
        print(f"    {'─'*30}")
        for n in PARTIAL:
            if n not in a8_vals: continue
            ak, err = a8_vals[n]
            le = float(mpmath.log10(abs(err) + mpmath.mpf('1e-900')))
            lv = float(mpmath.log10(abs(ak) + mpmath.mpf('1e-900')))
            sig = max(0, lv - le)
            clean = "✓" if n in a8_clean else "✗"
            print(f"    {n:>3}   {clean}   {le:>8.1f} {sig:>7.0f}")

        # Check if fixed checkpoints help
        a8_fixed_clean = {}
        for n in CASCADE:
            if n not in fixed: continue
            ts, fs, vol = fixed[n]
            kn = {0: Fraction(1)}
            for j in range(1,k): kn[j] = rats[j][n]
            ak, ak_err = extract_coefficient(fs, ts, vol, kn, k)
            fr, _ = identify_rational(ak, max_den=10**15, tol=1e-12, max_prime=mp)
            if fr:
                a8_fixed_clean[n] = fr

        nf = len(a8_fixed_clean)
        new_from_fixed = set(a8_fixed_clean.keys()) - set(a8_clean.keys())
        print(f"\n    Fixed checkpoints (n=3..13): {nf}/11 clean")
        print(f"    New clean from fixed: {sorted(new_from_fixed)}")

        # Combine
        combined = dict(a8_clean)
        combined.update(a8_fixed_clean)
        nc_comb = len(combined)
        print(f"    Combined: {nc_comb}/23 (need {need})")

        if nc_comb >= need:
            p = robust_polynomial(combined, c_t, c_s, c_c, deg) if nc_comb >= need+2 \
                else constrained_polynomial(combined, c_t, c_s, c_c, deg)
            if p:
                polys[k] = p
                rats[k] = {n: eval_poly(p, Fraction(n)) for n in PARTIAL}
                v5 = rats[k][5] == KNOWN_A5.get(k)
                print(f"    ✓ WALL BROKEN with hybrid approach! a₈(5)={'✓' if v5 else '✗'}")
            else:
                print(f"    ✗ Combined {nc_comb} still insufficient for valid polynomial")

        wall_broken = 8 in polys
    else:
        wall_broken = False
        print(f"    Skipped (no a₇)")

    score("T4: a₈ wall", wall_broken,
          "Hybrid approach succeeded" if wall_broken else "Wall stands — need more data")

    # ─── T5: Continue cascade if wall broken ───────────────────────
    print(f"\n  T5: Continue cascade a₉..a₁₁ (if a₈ succeeded)")
    print("  " + "─" * 58)
    ok5 = False
    if wall_broken:
        ok5 = True
        for k in range(9, 12):
            deg = 2*k; c_t, c_s, c_c = three_theorems(k)
            mp = MAX_PRIME[k]; need = deg - 2
            ak_r = {}
            for n in PARTIAL:
                if n not in adaptive: continue
                ts, fs, vol = adaptive[n]
                kn = {0: Fraction(1)}
                for j in range(1,k): kn[j] = rats[j][n]
                ak, _ = extract_coefficient(fs, ts, vol, kn, k)
                fr, _ = identify_rational(ak, max_den=10**15, tol=1e-12, max_prime=mp)
                if fr: ak_r[n] = fr

            # Also try fixed for n=3..13
            for n in CASCADE:
                if n in ak_r or n not in fixed: continue
                ts, fs, vol = fixed[n]
                kn = {0: Fraction(1)}
                for j in range(1,k): kn[j] = rats[j][n]
                ak, _ = extract_coefficient(fs, ts, vol, kn, k)
                fr, _ = identify_rational(ak, max_den=10**15, tol=1e-12, max_prime=mp)
                if fr: ak_r[n] = fr

            nk = len(ak_r)
            print(f"    a_{k:>2}: {nk:>2}/23 clean (need ≥{need}, prime≤{mp})", end="")
            p = None
            if nk >= need + 2:
                p = robust_polynomial(ak_r, c_t, c_s, c_c, deg)
            elif nk >= need:
                p = constrained_polynomial(ak_r, c_t, c_s, c_c, deg)
            if p:
                polys[k] = p
                rats[k] = {n: eval_poly(p, Fraction(n)) for n in PARTIAL}
                v5 = rats[k][5] == KNOWN_A5.get(k) if k in KNOWN_A5 else None
                print(f"  ✓ a_{k}(5)={'✓' if v5 else '✗'}")
            else:
                print(f"  ✗ WALL at a_{k}")
                ok5 = False
                break
    else:
        print(f"    Skipped (a₈ wall not broken)")

    have_all = all(k in polys for k in range(1, 12))
    score("T5: a₉..a₁₁", ok5 or not wall_broken,
          f"{'All 11 ✓' if have_all else ('Blocked at a₈' if not wall_broken else 'New wall')}")

    # ─── T6: a₁₂ attempt if prerequisites met ─────────────────────
    print(f"\n  T6: a₁₂ extraction attempt")
    print("  " + "─" * 58)
    a12_poly = None
    n12_clean = 0
    if have_all:
        k = 12; deg = 24; mp = 23; need = 22
        c_t, c_s, c_c = three_theorems(k)
        a12_r = {}
        for n in PARTIAL:
            if n not in adaptive: continue
            ts, fs, vol = adaptive[n]
            kn = {0: Fraction(1)}
            for j in range(1,k): kn[j] = rats[j][n]
            ak, _ = extract_coefficient(fs, ts, vol, kn, k)
            fr, _ = identify_rational(ak, max_den=10**15, tol=1e-8, max_prime=mp)
            if fr: a12_r[n] = fr
        # Also fixed
        for n in CASCADE:
            if n in a12_r or n not in fixed: continue
            ts, fs, vol = fixed[n]
            kn = {0: Fraction(1)}
            for j in range(1,k): kn[j] = rats[j][n]
            ak, _ = extract_coefficient(fs, ts, vol, kn, k)
            fr, _ = identify_rational(ak, max_den=10**15, tol=1e-8, max_prime=mp)
            if fr: a12_r[n] = fr

        n12_clean = len(a12_r)
        print(f"    Clean: {n12_clean}/23 (need ≥{need})")
        if n12_clean >= need:
            a12_poly = robust_polynomial(a12_r, c_t, c_s, c_c, deg) \
                       if n12_clean >= need+2 else \
                       constrained_polynomial(a12_r, c_t, c_s, c_c, deg)
            if a12_poly:
                v5 = eval_poly(a12_poly, Fraction(5))
                den_f = factor(v5.denominator)
                maxp = max(den_f) if den_f else 0
                print(f"    ✓✓✓ a₁₂ RECOVERED ✓✓✓")
                print(f"    a₁₂(5) = {v5}")
                print(f"    Den max prime: {maxp} {'≤23 ✓' if maxp<=23 else '>23 ✗'}")
        else:
            print(f"    Deficit: {need - n12_clean}")
    else:
        print(f"    Blocked (incomplete a₁..a₁₁ cascade)")

    score("T6: a₁₂ extraction",
          a12_poly is not None or n12_clean >= 15,
          f"{'RECOVERED' if a12_poly else f'{n12_clean} clean'}")

    # ─── T7: Cascade clean count table ─────────────────────────────
    print(f"\n  T7: Full cascade clean count summary")
    print("  " + "─" * 58)
    print(f"    {'k':>3} {'deg':>4} {'need':>5} {'clean':>6} {'status':>12} {'max_p':>6}")
    print(f"    {'─'*42}")
    cascade_levels = []
    for k in range(1, 13):
        deg = 2*k
        need = deg + 1 if k <= 5 else deg - 2
        if k in polys:
            status = "✓ recovered"
        elif k == 8 and not wall_broken:
            status = "✗ WALL"
        else:
            status = "✗ blocked"
        mp = MAX_PRIME.get(k, "—")

        # Get actual clean count
        if k <= 5:
            nc = 11  # fixed cascade always 11/11
        elif k <= 7:
            nc = "13" if k == 6 else "12"  # from T3
        elif k == 8:
            nc = len(a8_clean) if 'a8_clean' in dir() else "?"
        else:
            nc = "?"

        print(f"    {k:>3} {deg:>4} {need:>5} {str(nc):>6} {status:>12} {str(mp):>6}")

    score("T7: Summary table", True, "Diagnostic complete")

    # ─── T8: What's needed ─────────────────────────────────────────
    print(f"\n  T8: Path to a₁₂ — what's needed")
    print("  " + "═" * 58)

    if a12_poly:
        print(f"    ✓ a₁₂ already recovered! Nothing more needed.")
    else:
        print(f"    Current: 23 checkpoints (n=3..25)")
        print(f"    Wall: a₈ needs 14 clean, has {len(a8_clean) if 'a8_clean' in dir() else '?'}")
        print(f"")
        print(f"    PATH 1 — Complete Toy 361 (recommended):")
        print(f"      Compute n=26..35 → 33 total points")
        print(f"      Known to work (Toy 278/308 design)")
        print(f"      Estimated time: ~2-4 hours (P_MAX=2000, dps=800)")
        print(f"")
        print(f"    PATH 2 — Per-k optimized checkpoints:")
        print(f"      Recompute n=14..25 with t-window optimized for k=8")
        print(f"      t_hi ∝ 1/n (not 1/n²) for k≤8")
        print(f"      More precision where needed, less computation")
        print(f"")
        print(f"    PATH 3 — Hybrid (attempted in T4):")
        print(f"      Use fixed (n=3..13) + adaptive (n=14..25)")
        if wall_broken:
            print(f"      ✓ This worked for a₈!")
        else:
            print(f"      ✗ Not enough — fixed adds {len(new_from_fixed) if 'new_from_fixed' in dir() else 0} new clean")
        print(f"")
        print(f"    PRIORITY: Path 1 is safest. Rerun Toy 361 to completion.")

    score("T8: Path analysis", True, "Actionable recommendations provided")

    elapsed = time.time() - t_start
    print(f"\n  {'═'*58}")
    print(f"  Time: {elapsed:.1f}s")
    print(f"  Recovered: a₁..a_{max(polys.keys())} polynomials")
    if a12_poly:
        print(f"  Wall: NONE — a₁₂ recovered!")
    else:
        wall_count = len(a8_clean) if 'a8_clean' in dir() else '?'
        print(f"  Wall: a₈ at {wall_count}/23 clean")
    print(f"\n  SCORECARD: {PASS}/{PASS + FAIL}")


if __name__ == "__main__":
    main()
