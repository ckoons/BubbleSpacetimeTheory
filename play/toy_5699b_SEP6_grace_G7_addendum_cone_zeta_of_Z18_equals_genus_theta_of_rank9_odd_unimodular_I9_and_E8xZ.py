#!/usr/bin/env python3
"""toy 5699b — Grace 2026-09-06 (G7 addendum; prereg notes/grace_PREREG_toy_5699b_*.md for 13 <= N <= 20).
Cone-zeta of Z^{1,8} = genus theta of odd unimodular rank-9 lattices: r*_8(N) = r_9(N)/|O(I_9)| + r_{E8+Z}(N)/|O(E8+Z)|."""
import os, importlib.util, time, json, math
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
def load(prefix):
    f = [x for x in os.listdir(here) if x.startswith(prefix)][0]
    spec = importlib.util.spec_from_file_location(prefix, os.path.join(here, f)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
t7 = load('toy_5697_'); t8 = load('toy_5698_')

def sigma3(m): return sum(d**3 for d in range(1, m+1) if m % d == 0)
def r_E8(m):  # E8 is EVEN: theta = 1 + 240 sum sigma3(k) q^{2k}; vectors of norm m exist only for even m (bug caught at N=1 on the first run, 11:29)
    return 1 if m == 0 else (240*sigma3(m//2) if m % 2 == 0 else 0)
def r_E8Z(N):
    tot = 0; k = 0
    while k*k <= N:
        tot += r_E8(N - k*k) * (1 if k == 0 else 2); k += 1
    return tot

def main():
    t0 = time.time(); Nmax = 20
    O_I9 = 2**9 * math.factorial(9); O_E8Z = 2 * 696729600
    data, rstar, _ = t7.cone_zeta(8, Nmax)
    r9 = t8.sum_of_squares_counts(9, Nmax)
    chi, _ = t8.chiswell_volume(8)
    R8 = Fraction(2, 1) / ((-1)**4 * chi)
    print(f'R(8) = {R8};  1/mass(genus I9) = {1/(Fraction(1, O_I9) + Fraction(1, O_E8Z))}  equal: {R8 == 1/(Fraction(1, O_I9) + Fraction(1, O_E8Z))}')
    rows = []
    for N in range(1, Nmax+1):
        genus = Fraction(r9[N], O_I9) + Fraction(r_E8Z(N), O_E8Z)
        rows.append((N, rstar[N], genus, rstar[N] == genus))
        print(f'  N={N:2d}  r*_8={str(rstar[N]):>22}  genus theta={str(genus):>22}  {"HIT" if rstar[N] == genus else "MISS"}   (r9={r9[N]}, rE8Z={r_E8Z(N)}, orbits={len(data[N])})')
    q2 = all(ok for N, _, _, ok in rows if N <= 12); q1 = all(ok for N, _, _, ok in rows if N >= 13)
    print(f'Q2 post-hoc N<=12: {"HIT" if q2 else "MISS"};  Q1 PRE-REGISTERED 13<=N<=20: {"HIT" if q1 else "MISS"}')
    # Q3: n = 4 consistency
    d4, rs4, _ = t7.cone_zeta(4, 30); r5 = t8.sum_of_squares_counts(5, 30)
    q3 = all(rs4[N] == Fraction(r5[N], 3840) for N in range(1, 31))
    print(f'Q3 n=4 reduces to r5/3840, N<=30: {"HIT" if q3 else "MISS"}')
    json.dump(dict(toy='5699b', R8=str(R8), Q1=q1, Q2=q2, Q3=q3, rows=[(N, str(a), str(b), ok) for N, a, b, ok in rows], seconds=round(time.time()-t0, 1)),
              open(os.path.join(here, '.toy_5699b_results.json'), 'w'), indent=1)
    print(f'elapsed {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
