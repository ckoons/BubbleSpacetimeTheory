#!/usr/bin/env python3
"""
Toy (square tori) — Keeper 16:33 "Grace's next (1)": T(a,a), both generators free. Pre-registered (Grace 16:25 /
Keeper): D(a,a) = log2(N_closed/N_realized) -> log2 144 if both generators' holonomy classes are free, and
shares(h_x = 0), (h_y = 0) -> 1/4 each. Grace's refinement pre-registered at 16:35 from toy 5633: the short-generator
suppression per column is ~1.85/b bits, so across a square torus it is a CONSTANT ~1.85 bits, not zero — the
square limit is predicted to sit strictly BETWEEN log2 12 and log2 144, and share(h_y=0) strictly between 1/4 and 1.
Method: width-a transfer matrices (toy 5628 closed/coloring, 5631 graded rainbow), trace of the a-th power, a = 3..7.
"""
import sys, os, math, json, time, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
m28 = importlib.import_module('toy_5628_SEP2_E2_decision_cost_transfer_matrix_closed_transport_realized_records_on_T3L3M_constant_part_test')
m31 = importlib.import_module('toy_5631_SEP2_E2_separating_test_sheet_degree_vs_holonomy_classes_cocycle_orphans_2_vs_4_sheets_on_T_a_b')
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()

def trp(T, a):
    M = np.array(T, dtype=float); return float(np.trace(np.linalg.matrix_power(M, a)))

def main():
    out = []
    for a in range(3, 8):
        Z = trp(m28.closed_T(a), a); C = trp(m28.coloring_T(a), a)
        D = math.log2(Z / (C / 12))
        row = dict(a=a, closed=Z, realized=C / 12, D=D)
        if a <= 7:
            mats = {s: m31.rainbow_T_graded(a, s) for s in range(4)}
            S = mats[0][0]; hy = [m31.xor_all(v) for v in S]
            N = {}
            for c in range(4):
                keep = [i for i in range(len(S)) if hy[i] == c]
                for g in range(4):
                    tot = 0.0
                    for s in range(4):
                        Ts = np.array(mats[s][1][np.ix_(keep, keep)], dtype=float)
                        tot += m31.chi(s, g) * float(np.trace(np.linalg.matrix_power(Ts, a)))
                    N[(g, c)] = tot / 4
            R = sum(N.values())
            row.update(theta0=R / 3, D1=math.log2(Z / (R / 3)), D2=math.log2((R / 3) / (C / 12)),
                       share_hx0=sum(v for (g, c), v in N.items() if g == 0) / R,
                       share_hy0=sum(v for (g, c), v in N.items() if c == 0) / R,
                       share_both0=N[(0, 0)] / R)
        out.append(row)
        print(f"  T({a},{a}): closed {Z:.6g}  theta0 {row.get('theta0', float('nan')):.6g}  realized {C/12:.6g}  "
              f"D = {D:.4f}  D1 = {row.get('D1', float('nan')):.4f}  D2 = {row.get('D2', float('nan')):.4f}  "
              f"share(h_x=0) = {row.get('share_hx0', float('nan')):.4f}  share(h_y=0) = {row.get('share_hy0', float('nan')):.4f}  "
              f"share(both 0) = {row.get('share_both0', float('nan')):.4f}   [{time.time()-T0:.0f}s]")
    json.dump(out, open(os.path.join(HERE, '.square_tori_D_and_shares.json'), 'w'), indent=1)
    print("log2 12 =", round(math.log2(12), 4), " log2 144 =", round(math.log2(144), 4))
    print("SCORE: REPORTED — small-a sequence; the limit is the pre-registered question")

if __name__ == '__main__':
    main()
