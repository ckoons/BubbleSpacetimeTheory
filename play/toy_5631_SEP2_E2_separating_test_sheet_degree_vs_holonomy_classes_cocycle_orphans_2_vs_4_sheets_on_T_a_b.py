#!/usr/bin/env python3
"""
Toy 5631 — Keeper K1850's SEPARATING TEST for the candidate map "bits to decide = log2(degree of the
minimal realizing cover)".  Grace, 2026-09-02.  Pre-registered before the run (board 16:2x): on the
fixed-width family T(a, b) the short generator's holonomy is forced to zero as a -> infinity (toy 5628:
the nonzero-holonomy sectors carry a smaller eigenvalue), so 2-SHEET cocycle covers should DOMINATE
while D = log2(N_closed/N_realized) -> log2 12 regardless; if both hold, the candidate map is killed
(it would read log2 6) and the constant is the number of holonomy CLASSES on the free generator, |Z3 x V|.

Method: exact transfer-matrix counts of face-rainbow labelings on T(a, b) GRADED by the V-holonomy
(h_x, h_y) on the two generators: h_y = XOR of a column's vertical labels (a state property; constant
along x for rainbow labelings — asserted by block structure), h_x = XOR of the row-0 horizontal labels,
counted by characters of V: N(h_x = g) = (1/4) sum_s chi_s(g) tr(T_s^a), T_s weighting h(x,0) by chi_s.
Labels 1,2,3 are V minus 0 under integer XOR.  Records = labelings / 3.  Cocycle orphans = (h_x,h_y) != (0,0);
their derived cover has 2 sheets if rank<h_x,h_y> = 1 and 4 sheets if rank = 2.
"""
import itertools, math, json, os, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()

def chi(s, h): return -1 if bin(s & h).count('1') % 2 else 1

def rainbow_T_graded(b, s):
    S = list(itertools.product((1, 2, 3), repeat=b)); idx = {v: i for i, v in enumerate(S)}
    A = {}
    for vny in (1, 2, 3):
        for vy in (1, 2, 3):
            for y0 in (False, True):
                m = np.zeros((3, 3), dtype=np.int64)
                for hy in (1, 2, 3):
                    for hn in (1, 2, 3):
                        c = sum(1 for d in (1, 2, 3) if {hy, vny, d} == {1, 2, 3} and {d, vy, hn} == {1, 2, 3})
                        m[hy - 1][hn - 1] = c * (chi(s, hy) if y0 else 1)
                A[(vny, vy, y0)] = m
    T = np.zeros((len(S), len(S)), dtype=object if b <= 3 else float)
    for v in S:
        for vn in S:
            P = np.identity(3, dtype=np.int64)
            for y in range(b): P = P.dot(A[(vn[y], v[y], y == 0)])
            T[idx[v]][idx[vn]] = int(np.trace(P))
    return S, T

def xor_all(t):
    x = 0
    for a in t: x ^= a
    return x

def tr_pow(T, a):
    if T.dtype == object:
        P = np.identity(len(T), dtype=object)
        for _ in range(a): P = P.dot(T)
        return int(sum(P[i][i] for i in range(len(T))))
    return float(np.trace(np.linalg.matrix_power(T, a)))

def rank_span(g, c):
    return len({x for x in (0, g, c, g ^ c)}) .bit_length() - 1   # {0}->0, {0,g}->1, 4 elems->2

def main():
    out = {}
    for b, lengths in ((3, [3, 6, 9, 12, 18, 24, 30, 45, 60]), (6, [3, 6, 9, 12, 18, 30, 60])):
        mats = {s: rainbow_T_graded(b, s) for s in range(4)}
        S = mats[0][0]
        hy = [xor_all(v) for v in S]
        # block check: T[v][vn] == 0 unless h_y equal
        T0m = mats[0][1]
        for i in range(len(S)):
            for j in range(len(S)):
                if hy[i] != hy[j]: assert T0m[i][j] == 0, "h_y is not conserved along the transfer"
        print(f"\n[width b = {b}] h_y conserved along x: PASS   [{time.time()-T0:.0f}s]")
        rows = []
        for a in lengths:
            N = {}
            for c in range(4):
                keep = [i for i in range(len(S)) if hy[i] == c]
                for g in range(4):
                    tot = 0
                    for s in range(4):
                        Ts = mats[s][1][np.ix_(keep, keep)]
                        tot += chi(s, g) * tr_pow(Ts, a)
                    N[(g, c)] = tot / 4 if not isinstance(tot, int) else tot // 4
            R = sum(N.values())
            real = N[(0, 0)]
            two = sum(v for (g, c), v in N.items() if (g, c) != (0, 0) and rank_span(g, c) == 1)
            four = sum(v for (g, c), v in N.items() if rank_span(g, c) == 2)
            hy0_share = sum(v for (g, c), v in N.items() if c == 0) / R
            hx0_share = sum(v for (g, c), v in N.items() if g == 0) / R
            rows.append(dict(a=a, b=b, labelings=R, realized=real, two_sheet=two, four_sheet=four,
                             frac2=two / (two + four), hy0_share=hy0_share, hx0_share=hx0_share,
                             D2=math.log2((R) / real) if real else None))
            print(f"  T({a:2d},{b}): labelings {R:>14}  realized(h=0) {real:>12}  cocycle-orphans 2-sheet {two:>12}  "
                  f"4-sheet {four:>10}  frac(2-sheet) = {two/(two+four):.4f}   share(h_y=0) = {hy0_share:.4f}  "
                  f"share(h_x=0) = {hx0_share:.4f}   D2 = log2(N_theta0/N_real) = {math.log2(R/real):.4f}")
        out[f"b={b}"] = rows
    path = os.path.join(HERE, '.separating_test_sheets_5631.json'); json.dump(out, open(path, 'w'), indent=1)
    print("\nwritten", path, f"[{time.time()-T0:.0f}s]")
    print("SCORE: PASS — h_y block structure; the separating test is reported, not scored")

if __name__ == '__main__':
    main()
