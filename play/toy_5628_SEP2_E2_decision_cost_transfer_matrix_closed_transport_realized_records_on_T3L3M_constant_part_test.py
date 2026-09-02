#!/usr/bin/env python3
"""
Toy 5628 — Keeper 14:37 item 4 (Casey's reading: "the cost of the observer's decision is the loss of
the other perspective"): decision cost D = log2(N_closed / N_realized) on the Mohar–Salas tori
T(a, b), and whether D has a CONSTANT (genus-only) part beside a per-column part.
Grace, 2026-09-02.  Exact counts by TRANSFER MATRIX along x (trace of T^a), so every length a is
exact and T(12,3), T(15,3), ... cost nothing.  Widths b = 3 and b = 6.

Three counts per torus (conventions of toy 5627):
  Z(a,b)  = closed records   = sign patterns z in {+1,-1}^F with sum of z over the faces at every
            vertex == 0 (mod 3)        [state: previous strip's contribution to a column, 3^b]
  R(a,b)  = face-rainbow edge 3-labelings (every face carries labels {1,2,3})
            N_{theta=0} = R/3          [state: labels of a column's b vertical edges, 3^b]
  C(a,b)  = proper 4-colorings;  N_realized = C/12   [state: colors of a column, 4^b]
Positive control: T(3,3) must give Z = 202, R = 120 (N_theta0 = 40), C = 240 (N_real = 20) — toy 5627's
brute-force footprint and Lyra's sealed 13:11 run.
Decision cost D(a,b) = log2(Z / (C/12)).  Also D1 = log2(Z/(R/3)) (transport stage) and
D2 = log2((R/3)/(C/12)) (cocycle stage).  Constant part: D(a) - a * slope, with slope from the leading
eigenvalue ratio; reported as the sequence of first differences (should converge to the slope) and the
residual.  Kill (Keeper): if D moves with (a, b) with no constant part, there is no topological summand.
"""
import itertools, math, json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()

def tr_pow(T, a):
    """trace of T^a: exact Python ints for small matrices, float64 (relative error ~1e-12) otherwise."""
    if len(T) <= 100:
        M = np.array(T, dtype=object)
        P = np.identity(len(T), dtype=object)
        for _ in range(a): P = P.dot(M)
        return int(sum(P[i][i] for i in range(len(T))))
    M = np.array(T, dtype=float)
    return float(np.trace(np.linalg.matrix_power(M, a)))

def leading_eig(T):
    w = np.linalg.eigvals(np.array(T, dtype=float))
    w = sorted(w, key=lambda z: -abs(z))
    return w[:6]

# ---------------------------------------------------------------- transfer matrices for width b
def closed_T(b):
    """states: s in Z3^b = contribution of strip (x-1 -> x) to column x's vertex sums.
    strip x -> x+1 has faces f1(y) = ((x,y),(x+1,y),(x+1,y+1)), f2(y) = ((x,y),(x+1,y+1),(x,y+1)).
    column x gets f1(y) + f2(y) + f2(y-1); column x+1 gets f1(y) + f1(y-1) + f2(y-1)."""
    S = list(itertools.product(range(3), repeat=b)); idx = {s: i for i, s in enumerate(S)}
    T = [[0] * len(S) for _ in S]
    for signs in itertools.product((1, 2), repeat=2 * b):      # z = +1 -> 1, z = -1 -> 2 (mod 3)
        f1 = signs[:b]; f2 = signs[b:]
        cx = tuple((f1[y] + f2[y] + f2[(y - 1) % b]) % 3 for y in range(b))
        cn = tuple((f1[y] + f1[(y - 1) % b] + f2[(y - 1) % b]) % 3 for y in range(b))
        s = tuple((-c) % 3 for c in cx)          # previous strip must have supplied exactly -cx
        T[idx[s]][idx[cn]] += 1
    return T

def rainbow_T(b):
    """states: labels v(x, y) in {1,2,3}^b of the vertical edges (x,y)-(x,y+1).
    strip edges: h(x,y): (x,y)-(x+1,y); d(x,y): (x,y)-(x+1,y+1).
    f1(y) = {h(x,y), v(x+1,y), d(x,y)};  f2(y) = {d(x,y), v(x,y), h(x,y+1)}.
    T[v][vn] = trace over y of the 3x3 chain A_y[h(y)][h(y+1)] = sum_d [f1(y) rainbow][f2(y) rainbow]."""
    S = list(itertools.product((1, 2, 3), repeat=b)); idx = {s: i for i, s in enumerate(S)}
    # A[(vn_y, v_y)] = 3x3 matrix over (h_y, h_{y+1})
    A = {}
    for vny in (1, 2, 3):
        for vy in (1, 2, 3):
            m = np.zeros((3, 3), dtype=np.int64)
            for hy in (1, 2, 3):
                for hn in (1, 2, 3):
                    m[hy - 1][hn - 1] = sum(1 for d in (1, 2, 3)
                                            if {hy, vny, d} == {1, 2, 3} and {d, vy, hn} == {1, 2, 3})
            A[(vny, vy)] = m
    T = [[0] * len(S) for _ in S]
    for v in S:
        for vn in S:
            P = np.identity(3, dtype=np.int64)
            for y in range(b):
                P = P.dot(A[(vn[y], v[y])])
            T[idx[v]][idx[vn]] = int(np.trace(P))
    return T

def coloring_T(b):
    """states: colors of a column c in {0..3}^b with c(y) != c(y+1) (vertical edges);
    T[c][c'] = 1 iff c(y) != c'(y) (horizontal) and c(y) != c'(y+1) (diagonal) for all y."""
    S = [c for c in itertools.product(range(4), repeat=b) if all(c[y] != c[(y + 1) % b] for y in range(b))]
    idx = {s: i for i, s in enumerate(S)}
    T = [[0] * len(S) for _ in S]
    for c in S:
        for cn in S:
            if all(c[y] != cn[y] and c[y] != cn[(y + 1) % b] for y in range(b)):
                T[idx[c]][idx[cn]] = 1
    return T

def main():
    widths = [3, 6]
    lengths = {3: list(range(3, 31, 3)) + [4, 5, 7, 8], 6: list(range(3, 19, 3)) + [24, 30, 45, 60, 90, 120]}
    out = {}
    for b in widths:
        print(f"\n[width b = {b}] building transfer matrices ... [{time.time()-T0:.0f}s]")
        TZ = closed_T(b); TR = rainbow_T(b); TC = coloring_T(b)
        print(f"  sizes: closed {len(TZ)}  rainbow {len(TR)}  coloring {len(TC)}   [{time.time()-T0:.0f}s]")
        lz, lr, lc = leading_eig(TZ), leading_eig(TR), leading_eig(TC)
        print(f"  leading eigenvalues (|.| desc): closed {[round(abs(x),4) for x in lz]}")
        print(f"                                 rainbow {[round(abs(x),4) for x in lr]}")
        print(f"                                 coloring {[round(abs(x),4) for x in lc]}")
        rows = []
        for a in sorted(set(lengths[b])):
            Z = tr_pow(TZ, a); R = tr_pow(TR, a); C = tr_pow(TC, a)
            if isinstance(R, int): assert R % 3 == 0 and C % 12 == 0, (a, b, R, C)
            Nt = R / 3; Nr = C / 12
            if isinstance(R, int): Nt = R // 3; Nr = C // 12
            D = math.log2(Z / Nr) if Nr else float('inf')
            D1 = math.log2(Z / Nt) if Nt else float('inf')
            D2 = math.log2(Nt / Nr) if Nr else float('inf')
            rows.append(dict(a=a, b=b, V=a * b, F=2 * a * b, closed=Z, theta0=Nt, realized=Nr,
                             D=D, D1=D1, D2=D2))
            print(f"  T({a:2d},{b}): closed {Z:>18}  theta0 {Nt:>16}  realized {Nr:>14}   "
                  f"D={D:8.4f}  D1={D1:8.4f}  D2={D2:8.4f}   [{time.time()-T0:.0f}s]")
        # constant-part analysis on the a = 3k sequence
        seq = [r for r in rows if r['a'] % 3 == 0 and r['realized'] > 0]
        if len(seq) >= 3:
            diffs = [(seq[i+1]['D'] - seq[i]['D']) / 3 for i in range(len(seq) - 1)]
            slope_eig = math.log2(abs(lz[0]) / abs(lc[0]))
            const = [r['D'] - r['a'] * slope_eig for r in seq]
            print(f"  per-column slope from first differences: {[round(x,5) for x in diffs]}")
            print(f"  per-column slope from leading eigenvalues log2(lam_Z/lam_C) = {slope_eig:.5f}")
            print(f"  constant part D - a*slope_eig along a = 3k: {[round(x,4) for x in const]}")
            print(f"  predicted limit constant log2(12*mZ/mC) needs multiplicities; last value {const[-1]:.4f}")
            out[f"b={b}"] = dict(rows=rows, slope_first_diffs=diffs, slope_eig=slope_eig, const_part=const,
                                 lead_eig_closed=[abs(x) for x in lz], lead_eig_rainbow=[abs(x) for x in lr],
                                 lead_eig_coloring=[abs(x) for x in lc])
        else:
            out[f"b={b}"] = dict(rows=rows)
    # positive control
    r33 = [r for r in out['b=3']['rows'] if r['a'] == 3][0]
    ctrl = (r33['closed'], r33['theta0'], r33['realized']) == (202, 40, 20)
    print(f"\nPOSITIVE CONTROL T(3,3) closed/theta0/realized = {r33['closed']}/{r33['theta0']}/{r33['realized']} "
          f"vs 202/40/20 (toy 5627 brute force; Lyra 13:11): {'PASS' if ctrl else 'FAIL'}")
    out['control_T33'] = ctrl
    path = os.path.join(HERE, '.decision_cost_T3L3M_5628.json')
    json.dump(out, open(path, 'w'), indent=1, default=str)
    print("written", path, f"[{time.time()-T0:.0f}s]")
    print("SCORE:", "PASS" if ctrl else "FAIL", "— control; the constant-part question is reported, not scored")

if __name__ == '__main__':
    main()
