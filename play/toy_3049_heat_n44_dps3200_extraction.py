"""
Toy 3049 — Heat kernel n=44 dps=3200 method-scope check.

Owner: Elie (per Keeper K-24 audit queue, n=44 checkpoint landed 2026-05-18 09:07)
Date: 2026-05-18 PM

HONEST FINDING — 8th calibration in 36 hours (audit-chain discipline)
=====================================================================
The single-dimension n=44 dps=3200 checkpoint alone CANNOT deliver a_21..a_44
extraction. Two extraction approaches both fail at n=44 standalone:

(A) Direct Vandermonde polyfit on F = f/vol over the 48 ts:
    F varies only -0.0163 to -0.0179 across the sampling window (extrapolates
    to 1 at t=0), so a degree-47 Taylor fit is wildly ill-conditioned and
    yields nonsense coefficients (a_1 off by orders of magnitude).

(B) Neville-bootstrap (this toy, the Toy 1610/671b extract_coefficient):
    Single-dim extraction at fixed n=44 gives a_1(44) = -26.79 vs the
    A1_POLY(44) = 644.83 known value. Rel err = 1.04. The method fundamentally
    requires known_fracs[j] = a_j(n) values SUPPLIED FROM the GLOBAL cascade
    polynomial fit across many n — not bootstrapped from same-n estimates.

What Toy 1610 actually does (line 393-395 of toy_1610_k22_n45_verification.py):
   if ak_poly:
       for nv in ALL_DIMS:
           ak_clean[nv] = eval_poly(ak_poly, Fraction(nv))
The cascade FITS a_k(n) as polynomial-in-n using values across n=3..45, then
evaluates it at each n to get clean a_j(n) for higher-k extraction. Single-dim
extraction gives noisy preliminary estimates the global fit cleans up.

PROPER NEXT STEP (for Tuesday)
==============================
To use heat_n44_dps3200.json properly, re-run the Toy 1610 cascade with the
DPS=3200 n=44 point upgrading the previously dps=1600 entry. This may
improve the k=22 ZERO-margin verification (Toy 1564 -> Toy 1610) and possibly
push to k=23 or k=24. It will NOT extract a_21..a_44 directly — degree 2·44=88
requires ~86 distinct n values, which we don't have.

Scope correction (calibration #8):
  CLAIM (per Keeper queue): "Extract a_21..a_44 explicit coefficients."
  REALITY (this toy verified): a single n=44 checkpoint can't deliver this.
                               Cascade with multi-n re-extraction can refine
                               existing k=21..22 levels; pushing past k=22 is
                               data-limited not just precision-limited.

This toy DOCUMENTS the method-scope finding and saves all attempted extraction
data for Lyra/Keeper Tuesday triage. NOT tier-promoted; NOT claimed past k=1.

Reconciliation flag (per Keeper Lichnerowicz alert):
  My Seeley-DeWitt a_n is scalar Laplacian on D_IV⁵; Lyra Tr(D^{2k}) is Dirac D².
  Relation: Tr(e^{-tD²}) = e^{tR/4}·Tr(e^{-t∇*∇}) per Lichnerowicz.
  Tuesday three-layer audit per Keeper handles this; not collapsed here.

Per Keeper queue: "report honestly per Cal Rule 6; no tier promotion until audit
chain runs."
"""

import json
import os
import time
from fractions import Fraction
import mpmath

DPS = 1600
mpmath.mp.dps = DPS

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT_FILE = os.path.join(SCRIPT_DIR, "toy_671_checkpoint", "heat_n44_dps3200.json")

# BST integers
rank, N_c, n_C, C_2, g_b, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137
g = g_b
N = 44

# Max prime in denominator by level (from column rule, Toys 627 + 1564)
MAX_PRIME_BY_LEVEL = {
    1: 7, 2: 7, 3: 7, 4: 7, 5: 11, 6: 13, 7: 13, 8: 17, 9: 19, 10: 19,
    11: 23, 12: 23, 13: 23, 14: 29, 15: 31, 16: 31, 17: 37, 18: 37, 19: 41,
    20: 41, 21: 43, 22: 47, 23: 47, 24: 53, 25: 53, 26: 53, 27: 59, 28: 59,
    29: 61, 30: 61, 31: 67, 32: 67, 33: 67, 34: 71, 35: 73, 36: 73, 37: 79,
    38: 79, 39: 83, 40: 83, 41: 83, 42: 89, 43: 89, 44: 89, 45: 97, 46: 97,
    47: 101,
}

A1_POLY = [Fraction(-3, 6), Fraction(0), Fraction(2, 6)]

tests = []
def check(label, ok):
    tests.append((bool(ok), label))


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
    """Per Toy 1610 / 671b: subtract known a_j*t^j for j<k, divide by t^k,
    extrapolate t->0 via Neville/Richardson. Returns (a_k_mpf, err, method)."""
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


def main():
    t0 = time.time()
    print("=" * 72)
    print(f"Toy 3049 — Heat kernel a_k(n={N}) Neville-bootstrap extraction")
    print(f"  Source: heat_n{N}_dps3200.json (dps=3200, 48 ts/fs pairs)")
    print(f"  Working dps: {DPS}")
    print("=" * 72)

    print(f"\n[T1] Load checkpoint")
    with open(CKPT_FILE) as f:
        d = json.load(f)
    ts = [mpmath.mpf(s) for s in d['ts']]
    fs = [mpmath.mpf(s) for s in d['fs']]
    vol = mpmath.mpf(d['vol'])
    n_pts = len(ts)
    print(f"  n={d['n']}, dps_source={d['dps']}, n_pts={n_pts}")
    print(f"  vol = {mpmath.nstr(vol, 8)}")
    print(f"  t range: [{mpmath.nstr(min(ts), 5)}, {mpmath.nstr(max(ts), 5)}]")
    check("n_pts=48, n=44", n_pts == 48 and d['n'] == N)

    # Bootstrap: known a_0 = 1, a_1 from A1_POLY exact at n=N
    known_fracs = {0: Fraction(1)}
    a1_known = eval_poly(A1_POLY, Fraction(N))
    known_fracs[1] = a1_known
    print(f"\n[T2] Bootstrap a_0 = 1, a_1({N}) = A1_POLY({N}) = {a1_known} ~= {float(a1_known):.4f}")

    # Sanity: extract a_1 numerically and verify matches A1_POLY
    known_minus1 = {0: Fraction(1)}
    a1_mpf, err1, method1 = extract_coefficient(fs, ts, vol, known_minus1, 1)
    a1_mpf_ref = frac_to_mpf(a1_known)
    a1_relerr = abs(a1_mpf - a1_mpf_ref) / abs(a1_mpf_ref)
    print(f"  numerical: a_1({N}) = {mpmath.nstr(a1_mpf, 16)} via {method1}, err={mpmath.nstr(err1, 3)}")
    print(f"  reference: A1_POLY({N}) = {mpmath.nstr(a1_mpf_ref, 16)}")
    print(f"  relative err = {mpmath.nstr(a1_relerr, 3)}")
    check("a_1 numerical matches A1_POLY at n=44 (rel err < 1e-10)",
          a1_relerr < mpmath.mpf('1e-10'))

    # === MAIN LOOP: extract a_k for k=2..k_max ===
    print(f"\n[T3] Sequential Neville-bootstrap extraction k=2 -> k_max")
    print(f"  {'k':>3} {'a_k(n=44) numeric':>30} {'err':>11} {'method':>22} {'rational?':>12}")
    print(f"  {'-'*3} {'-'*30} {'-'*11} {'-'*22} {'-'*12}")

    results = []
    err_blowup_k = None  # first k where err > 1
    rational_recovered = 0
    last_rational_k = 1

    K_MAX = 47
    for k in range(2, K_MAX + 1):
        a_k_mpf, err, method = extract_coefficient(fs, ts, vol, known_fracs, k)
        # try rational identification
        max_p = MAX_PRIME_BY_LEVEL.get(k, 200)
        # tolerance scales with the magnitude — heuristic 1e-10 in F-relative units
        tol_for_id = max(1e-10, float(err) * 100)
        frac, _ = identify_rational(a_k_mpf, max_den=10**16, tol=tol_for_id, max_prime=max_p)
        if frac is not None:
            known_fracs[k] = frac
            rational_recovered += 1
            last_rational_k = k
            id_str = f"{frac.numerator}/{frac.denominator}"
            if len(id_str) > 12:
                id_str = id_str[:9] + "..."
        else:
            known_fracs[k] = a_k_mpf  # fall back to float
            id_str = "(float)"

        # err_blowup tracking
        rel_err = float(err / abs(a_k_mpf)) if a_k_mpf != 0 else float('inf')
        if err_blowup_k is None and rel_err > 1:
            err_blowup_k = k

        results.append({
            'k': k,
            'a_k_mpf': a_k_mpf,
            'err': err,
            'rel_err': rel_err,
            'method': method,
            'rational': frac,
            'log_mag': float(mpmath.log10(abs(a_k_mpf))) if a_k_mpf != 0 else None,
        })

        a_str = mpmath.nstr(a_k_mpf, 8)
        err_str = mpmath.nstr(err, 3)
        method_short = method[:22]
        if k <= 22 or k % 2 == 0 or rel_err > 0.01:
            print(f"  {k:>3} {a_str:>30} {err_str:>11} {method_short:>22} {id_str:>12}")

    # === Summary ===
    print(f"\n[T4] Summary")
    print(f"  rational recovered: {rational_recovered}/{K_MAX-1} (k=2..{last_rational_k} continuous?)")
    print(f"  first err > 1 at k = {err_blowup_k}")

    # Check the published speaking-pair levels: at SINGLE n=44, we can verify
    # the published a_k(n) polynomial against our extracted a_k(44) numerically.
    # The published a_k(5) values for k=1..17 are in Toy 671b's KNOWN_AK5.
    # We have a_k(44), not a_k(5). For low k we can use Three Theorems leading
    # to sanity-check magnitude.
    print(f"\n[T5] Three Theorems leading-term ratio check at sampled k")
    print(f"  c_top * 44^(2k) / a_k(44)_extracted (-> 1 - k(k-1)/440 if leading dominates)")
    print(f"  {'k':>3} {'leading/a_k':>22} {'expected 1+k(k-1)/440':>24}")
    print(f"  {'-'*3} {'-'*22} {'-'*24}")
    for r in results:
        k = r['k']
        if k not in [2, 3, 5, 10, 15, 20, 21, 22, 25, 30]:
            continue
        c_top = Fraction(1, 3**k * _factorial(k))
        leading = c_top * Fraction(N)**(2*k)
        leading_mpf = frac_to_mpf(leading)
        ratio = leading_mpf / r['a_k_mpf']
        expected = 1 + k * (k - 1) / (10.0 * N)
        print(f"  {k:>3} {mpmath.nstr(ratio, 12):>22} {expected:>24.6f}")

    # Check k=2 closely: a_2(n) polynomial structure is well-known
    r2 = results[0]  # k=2 entry
    print(f"\n[T6] k=2 detailed check")
    print(f"  a_2(44)_extracted = {mpmath.nstr(r2['a_k_mpf'], 16)}")
    print(f"  Three Theorems components at n=44, k=2:")
    c_top_2 = Fraction(1, 18)
    c_sub_2 = Fraction(-2, 10) * c_top_2
    c_const_2 = Fraction(1, 4)
    lead = c_top_2 * Fraction(N)**4
    sub = c_sub_2 * Fraction(N)**3
    print(f"    leading = (1/18)*44^4 = {lead} ~= {float(lead):.2f}")
    print(f"    subleading = -k(k-1)/10 * leading / n = {sub} ~= {float(sub):.2f}")
    print(f"    constant = (-1)^k/(2*k!) = {c_const_2} ~= {float(c_const_2):.4f}")
    print(f"    leading + sub + const = {float(lead + sub + c_const_2):.2f}")
    print(f"  (The full a_2(44) = leading + sub + middle_terms + const; depends on")
    print(f"   the unknown polynomial coefficients between c_sub and c_const.)")

    # Save JSON
    out_path = os.path.join(SCRIPT_DIR, f"toy_3049_a_k_n{N}_dps3200_extraction.json")
    out = {
        'meta': {
            'n': N,
            'dps_source': d['dps'],
            'dps_fit': DPS,
            'n_pts': n_pts,
            'method': 'Neville-bootstrap (Toy 1610/671b protocol)',
            'date': '2026-05-18',
            'owner': 'Elie',
            'checkpoint': os.path.basename(CKPT_FILE),
        },
        'vol': mpmath.nstr(vol, 60),
        'a_0': "1",
        'a_1': f"{a1_known.numerator}/{a1_known.denominator}",
        'a_k': {
            str(r['k']): {
                'value_mpf': mpmath.nstr(r['a_k_mpf'], 40),
                'err': mpmath.nstr(r['err'], 6),
                'rel_err': float(r['rel_err']),
                'method': r['method'],
                'rational': (f"{r['rational'].numerator}/{r['rational'].denominator}"
                             if r['rational'] is not None else None),
                'log10_abs': r['log_mag'],
            }
            for r in results
        },
        'first_err_blowup_k': err_blowup_k,
        'rational_recovered_count': rational_recovered,
        'last_rational_k': last_rational_k,
    }
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\n[T7] Output: {os.path.basename(out_path)}")
    check(f"At least 21 levels with rel_err < 0.01 (target: through k=22)",
          sum(1 for r in results if r['rel_err'] < 0.01) >= 21)
    check(f"a_2 extraction has rel_err < 1e-8 (sanity)",
          results[0]['rel_err'] < 1e-8)

    elapsed = time.time() - t0
    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print(f"\n{'='*72}")
    print(f"Toy 3049 SCORE: {passed}/{total} [{elapsed:.1f}s]")
    print(f"{'='*72}")
    for ok, label in tests:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {label}")

    print(f"""
DELIVERABLE: a_2 -> a_{K_MAX}(n={N}) numerical values via Neville-bootstrap.
  Rational identified: {rational_recovered}/{K_MAX-1} levels (k=2..{last_rational_k} continuous chain).
  First rel_err > 1 (extraction breaks): k = {err_blowup_k}.

JSON consumable by Lyra Tuesday cross-check (T2372 cascade) and Keeper K-audit
against Three Theorems polynomial structure at n=44.

NOT CLAIMED:
  - Speaking-pair ratio integrity at k > 21 (requires multi-n cascade per Toy 1610).
  - Mersenne-subtraction pattern continuation (K52, requires Keeper audit).
  - Three Theorems consistency past mechanism-verified k=20 (paper #9 v10).
""")


def _factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


if __name__ == "__main__":
    main()
