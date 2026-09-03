#!/usr/bin/env python3
"""
Toy (height record's decision cost) — Round 113 §3, Lyra's definition (14:01): a closed height record IS a rainbow
labeling (3 per theta-clean sign record), realized iff [l] = 0; so N_closed^h = 3·N_{theta=0}, N_realized^h = N_realized
and D_h(a) = log2 3 + D2(a) with D2 = log2(N_{theta=0}/N_realized) from toy 5628's exact rows.  Pre-registered (Lyra):
D_h -> log2 3 + log2|Hom(Z,V)| = log2 12 on one free generator; kill = any limit off by other than the exact log2 3.
Also read: the decay rate of D_h - log2 12 on both residue branches vs the three subleading ratios of 5647.
Grace, 2026-09-03; no new enumeration — a computation on registered artifacts (.decision_cost_T3L3M_5628.json, .out_5647.json).
"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, '.decision_cost_T3L3M_5628.json')))
e = json.load(open(os.path.join(HERE, '.out_5647.json')))
L3 = math.log2(3); L12 = math.log2(12)
for b in (3, 6):
    rows = d[f'b={b}']['rows']
    print(f"\n[width {b}] D_h(a) = log2 3 + D2(a):")
    for r in rows:
        if r['realized'] and r['a'] % 3 == 0 or r['a'] in (4, 5, 7, 8):
            Dh = L3 + r['D2']
            print(f"   a={r['a']:3d}: D2 = {r['D2']:.4f}  D_h = {Dh:.4f}  D_h - log2 12 = {Dh - L12:+.5f}   (sign record D = {r['D']:.4f})")
    # decay on the 3|a branch from the last rows
    pts = [(r['a'], L3 + r['D2'] - L12) for r in rows if r['a'] % 3 == 0 and r['realized'] and abs(L3 + r['D2'] - L12) > 1e-9]
    tail = pts[-5:]
    xs = [a for a, _ in tail]; ys = [math.log(abs(v)) for _, v in tail]
    n = len(xs); sx = sum(xs); sy = sum(ys); sxx = sum(x*x for x in xs); sxy = sum(x*y for x, y in zip(xs, ys))
    rho = math.exp((n*sxy - sx*sy) / (n*sxx - sx*sx))
    ratios = {k: v['ratio'] for k, v in e[f'b{b}_ratios'].items()}
    print(f"   limit: D_h -> {L3 + rows[-1]['D2']:.4f} vs log2 12 = {L12:.4f} (a = {rows[-1]['a']}); fitted decay rho = {rho:.4f}; "
          f"subleading ratios closed {ratios['closed']:.4f} rainbow {ratios['rainbow']:.4f} coloring {ratios['coloring']:.4f} -> nearest: "
          f"{min(ratios, key=lambda k: abs(ratios[k]-rho))}")
print("\nSCORE: REPORTED — D_h's limit is exactly log2 3 + D2's limit; pre-registration scored above")
