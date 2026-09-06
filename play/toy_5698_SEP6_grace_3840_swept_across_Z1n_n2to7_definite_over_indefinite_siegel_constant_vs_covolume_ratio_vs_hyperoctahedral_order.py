#!/usr/bin/env python3
"""
toy 5698 — Grace, 2026-09-06 (Keeper handoff G2; Casey's word: "3840 gets a sweep").

K1862-A: c_def/c_indef = 13.15947/0.0034269 = 3840.0 for Z^5 vs Z^{1,4}.  Sweep the family Z^{n+1} vs Z^{1,n}, n = 2..7.

R(n) := [ r_{n+1}(N) / a2_def(N) ] / [ r*_n(N) / a2_ind(N) ]
  r_{n+1}(N) = number of representations of N as a sum of n+1 squares (definite side, one-class genus),
  r*_n(N)    = Siegel-weighted chamber count on the Vinberg simplex of Z^{1,n} (toy 5697 machinery),
  a2         = 2-adic density  lim #{x mod 2^k : Q(x) = N mod 2^k} / 2^{k n}, the SAME normalisation for both forms.
Odd-p densities are identical for the two forms (K1862-C Lemma 1 at n=4; the constancy of R(n) in N tests that at every n),
so R(n) must be N-independent; its value is the ratio of the two archimedean factors.

Compared against:  (a) vol(S^n)/vol(P^n), P^n = the Vinberg Coxeter simplex, vol by Gauss–Bonnet + Chiswell's Euler
characteristic for even n (from the SAME parabolic orders the chamber code uses), literature for odd n;
(b) |W(B_{n+1})| = 2^{n+1} (n+1)! = |O(Z^{n+1})|;  (c) BST integers.
Pre-stated expectation (Casey, Keeper): a covolume ratio, not a BST integer.
"""
import sys, os, math, itertools, importlib.util, time
from fractions import Fraction

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('t5697', os.path.join(here, [f for f in os.listdir(here) if f.startswith('toy_5697_')][0]))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)

def sum_of_squares_counts(m, Nmax):
    """r_m(N) for N <= Nmax."""
    sq = [0]*(Nmax+1)
    k = 0
    while k*k <= Nmax:
        sq[k*k] += 1 if k == 0 else 2; k += 1
    r = [1] + [0]*Nmax
    for _ in range(m):
        new = [0]*(Nmax+1)
        for a in range(Nmax+1):
            if r[a]:
                for b in range(Nmax+1-a):
                    if sq[b]: new[a+b] += r[a]*sq[b]
        r = new
    return r

def density2(signs, N, k):
    """#{x mod 2^k : sum signs_i x_i^2 = N mod 2^k} / 2^{k*(m-1)}, m = len(signs)."""
    q = 2**k
    dist_plus = [0]*q; dist_minus = [0]*q
    for x in range(q):
        dist_plus[(x*x) % q] += 1; dist_minus[(-x*x) % q] += 1
    conv = [1] + [0]*(q-1)
    for s in signs:
        d = dist_plus if s > 0 else dist_minus
        new = [0]*q
        for a in range(q):
            if conv[a]:
                ca = conv[a]
                for b in range(q):
                    if d[b]: new[(a+b) % q] += ca*d[b]
        conv = new
    m = len(signs)
    return Fraction(conv[N % q], q**(m-1))

def a2(signs, N):
    v2 = 0; m = N
    while m % 2 == 0: m //= 2; v2 += 1
    k = v2 + 3
    d1 = density2(signs, N, k); d2 = density2(signs, N, k+1)
    assert d1 == d2, ('2-adic density not stable', signs, N, k, d1, d2)
    return d1

def chiswell_volume(n):
    """vol(P^n) for even n: (-1)^{n/2} chi(W) (2 pi)^{n/2} / (n-1)!!, chi = sum over finite parabolic subsets (-1)^{|S|}/|W_S|."""
    roots = t.vinberg_roots(n)
    chi = Fraction(0)
    for size in range(0, n+2):
        for S in itertools.combinations(range(n+1), size):
            o = t.coxeter_order(roots, list(S)) if size else 1
            if o is None: continue
            chi += Fraction((-1)**size, o)
    dfact = 1
    for j in range(n-1, 0, -2): dfact *= j
    vol = (-1)**(n//2) * chi * (2*math.pi)**(n//2) / dfact
    return chi, vol

def vol_sphere(n):
    return 2*math.pi**((n+1)/2) / math.gamma((n+1)/2)

def main():
    t0 = time.time()
    Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    print(f'# toy 5698 — sweep of the archimedean ratio R(n), n=2..7, N<=Nmax={Nmax}')
    print(' n | R(n) (min..max over N, rel spread) | vol(S^n)/vol(P^n) [even n exact] | |W(B_{n+1})| | R(n)/|W(B_{n+1})| | R(n)/(vol ratio)')
    table = []
    for n in range(2, 8):
        data, rstar, rprim = t.cone_zeta(n, Nmax)
        rdef = sum_of_squares_counts(n+1, Nmax)
        signs_def = [1]*(n+1); signs_ind = [1] + [-1]*n
        vals = []
        for N in range(1, Nmax+1):
            if rstar[N] == 0 or rdef[N] == 0: continue
            R = (Fraction(rdef[N]) / a2(signs_def, N)) / (rstar[N] / a2(signs_ind, N))
            vals.append((N, R))
        Rs = [float(R) for _, R in vals]
        Rmin, Rmax = min(Rs), max(Rs); spread = (Rmax - Rmin) / Rmin
        exact = vals[0][1] if all(R == vals[0][1] for _, R in vals) else None
        wb = 2**(n+1) * math.factorial(n+1)
        if n % 2 == 0:
            chi, volP = chiswell_volume(n)
            ratio = vol_sphere(n) / volP
            ratio_s = f'{ratio:.6f} (chi={chi}, vol P={volP:.6g})'
        else:
            ratio = None; ratio_s = 'odd n: not rational*pi^k (literature)'
        print(f' {n} | {Rmin:.6f}..{Rmax:.6f} (spread {spread:.1e}) exact={exact} | {ratio_s} | {wb} | {Rmin/wb:.6f} | {(Rmin/ratio if ratio else float("nan")):.6f}')
        table.append(dict(n=n, R_exact=str(exact) if exact else None, Rmin=Rmin, Rmax=Rmax, spread=spread, WB=wb, vol_ratio=ratio,
                          chi=str(chi) if n % 2 == 0 else None, chamber_vectors=sum(len(v) for v in data.values())))
    import json
    with open(os.path.join(here, '.toy_5698_results.json'), 'w') as f: json.dump(dict(toy=5698, Nmax=Nmax, table=table, seconds=round(time.time()-t0,1)), f, indent=1)
    print(f'elapsed {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
