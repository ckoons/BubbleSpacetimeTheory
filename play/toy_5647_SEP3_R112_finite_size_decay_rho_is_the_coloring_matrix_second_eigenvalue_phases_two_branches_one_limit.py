#!/usr/bin/env python3
"""
Toy 5647 — Round 112 §3 (Grace, 2026-09-03).  PRE-REGISTERED (board 13:28, before this ran): the decay rate rho of
D(a) - log2 12 on T(a,b) is the COLORING transfer matrix's lambda_2/lambda_1 (0.750 at width 3, 0.854 at width 6),
and the 3|a vs a≢0 (mod 3) branches share that eigenvalue shell through cube-root-of-unity PHASES.
Method: the three transfer matrices of toy 5628 (closed / rainbow / coloring) at widths 3 and 6; full spectra with
phases (numpy eig); D(a) exactly (ints at width 3, float at width 6) for a = 3..40; the log-deviation slope on each
branch; comparison of |lambda_2|/|lambda_1| per matrix with the fitted rho; the phases of the coloring shell.
Kill: coloring lambda_2/lambda_1 not within 0.01 of the fitted rho on either width; or no complex phases in the shell.
"""
import os, sys, math, json, cmath
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
m28 = importlib.import_module('toy_5628_SEP2_E2_decision_cost_transfer_matrix_closed_transport_realized_records_on_T3L3M_constant_part_test')
HERE = os.path.dirname(os.path.abspath(__file__))

def spectrum(T):
    w = np.linalg.eigvals(np.array(T, dtype=float))
    w = sorted(w, key=lambda z: -abs(z))
    return w

def shell(w, tol=1e-6):
    """eigenvalues with |z| within tol*|lambda1| of the second-largest modulus, as (modulus, phase/2pi)."""
    lam1 = abs(w[0]); rest = [z for z in w if abs(abs(z) - lam1) > tol * lam1]
    lam2 = max(abs(z) for z in rest)
    sh = [z for z in rest if abs(abs(z) - lam2) < 1e-6 * lam1]
    return lam2 / lam1, sorted(round(cmath.phase(z) / (2 * math.pi) % 1, 4) for z in sh)

def main():
    out = {}
    for b in (3, 6):
        TZ, TR, TC = m28.closed_T(b), m28.rainbow_T(b), m28.coloring_T(b)
        specs = {'closed': spectrum(TZ), 'rainbow': spectrum(TR), 'coloring': spectrum(TC)}
        ratios = {k: shell(v) for k, v in specs.items()}
        print(f"\n[width {b}] lambda1 = {abs(specs['closed'][0]):.6f} (all three equal: {all(abs(abs(specs[k][0]) - abs(specs['closed'][0])) < 1e-6 for k in specs)})")
        for k, (r, ph) in ratios.items():
            print(f"   {k:9s} lambda2/lambda1 = {r:.4f}; phases of the shell (fractions of 2pi): {ph}")
        # D(a) on both branches
        D = {}
        for a in range(3, 41 if b == 3 else 61):
            Z = m28.tr_pow(TZ, a); C = m28.tr_pow(TC, a)
            if C == 0: continue
            D[a] = math.log2(Z / (C / 12)) - math.log2(12)
        for branch, sel in (('3|a (from below)', lambda a: a % 3 == 0), ('a≢0 mod 3 (from above)', lambda a: a % 3 != 0)):
            pts = [(a, D[a]) for a in sorted(D) if sel(a) and abs(D[a]) > 1e-9]
            # slope of ln|dev| vs a over the last points of the branch
            tail = pts[-6:] if len(pts) >= 6 else pts
            xs = [a for a, _ in tail]; ys = [math.log(abs(d)) for _, d in tail]
            n = len(xs); sx = sum(xs); sy = sum(ys); sxx = sum(x*x for x in xs); sxy = sum(x*y for x, y in zip(xs, ys))
            slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
            rho = math.exp(slope)
            signs = set(1 if d > 0 else -1 for _, d in pts)
            print(f"   branch {branch}: D - log2 12 at {[(a, round(d,4)) for a, d in pts[:5]]} ... {[(a, round(d,5)) for a, d in pts[-3:]]}; sign(s) {sorted(signs)}; fitted rho = {rho:.4f}")
            out[f"b{b}_{branch}"] = dict(rho=rho, points=pts)
        out[f"b{b}_ratios"] = {k: dict(ratio=r, phases=ph) for k, (r, ph) in ratios.items()}
        # verdict
        rc = ratios['coloring'][0]
        for branch in ('3|a (from below)', 'a≢0 mod 3 (from above)'):
            rho = out[f"b{b}_{branch}"]['rho']
            print(f"   => width {b}, {branch}: |coloring lambda2/lambda1 - rho| = {abs(rc - rho):.4f}  ({'within 0.01' if abs(rc-rho) < 0.01 else 'OUTSIDE 0.01'}); closed {abs(ratios['closed'][0]-rho):.4f}; rainbow {abs(ratios['rainbow'][0]-rho):.4f}")
    json.dump(out, open(os.path.join(HERE, '.out_5647.json'), 'w'), indent=1, default=str)
    print("SCORE: REPORTED against the 13:28 pre-registration")

if __name__ == '__main__':
    main()
