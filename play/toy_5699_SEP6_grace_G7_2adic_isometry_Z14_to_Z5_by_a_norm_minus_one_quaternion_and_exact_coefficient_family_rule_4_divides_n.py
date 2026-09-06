#!/usr/bin/env python3
"""
toy 5699 — Grace, 2026-09-06 (Round 120, G7). Pre-registered: notes/grace_PREREG_toy_5699_*.md.

Why r*(N)·3840 = r_5(N) exactly (Elie 5695a):  Z^{1,4} and Z^5 are isometric over Z_2.
P1  exhibit the isometry: A = diag(1, L_q), q a 2-adic quaternion with N(q) = -1, A^T J A = I_5 mod 2^K.
P2  2-adic densities of <1,-1,-1,-1,-1> and I_5 agree for every N <= 200.
P3  family rule: exact coefficient identity r*_n(N) R(n) = r_{n+1}(N) for all N  iff 4 | n  (n = 2, 4, 6, 8).
P4  at n = 2, 6 the ratio depends only on the 2-adic class of N.
"""
import os, sys, importlib.util, math, itertools, json, time
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
def load(prefix):
    f = [x for x in os.listdir(here) if x.startswith(prefix)][0]
    spec = importlib.util.spec_from_file_location(prefix, os.path.join(here, f)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
t7 = load('toy_5697_'); t8 = load('toy_5698_')

# ---------- P1: quaternion of norm -1 in Z_2, by Hensel lifting ----------
def hensel_four_squares(target, K):
    """(a,b,c,d) with a^2+b^2+c^2+d^2 = target mod 2^K. Lift from mod 8 one bit at a time (any odd coordinate lifts)."""
    sols = [s for s in itertools.product(range(8), repeat=4) if (sum(x*x for x in s) - target) % 8 == 0 and s[0] % 2 == 1]
    a, b, c, d = sols[0]
    for k in range(3, K):
        M = 2**(k+1)
        if (a*a + b*b + c*c + d*d - target) % M != 0:
            # residue is exactly 2^k mod 2^{k+1}; with a odd, (a + 2^{k-1})^2 = a^2 + 2^k a + 2^{2k-2} ≡ a^2 + 2^k (mod 2^{k+1}) for k >= 3
            a += 2**(k-1)
        assert (a*a + b*b + c*c + d*d - target) % M == 0, k
    return a % (2**K), b % (2**K), c % (2**K), d % (2**K)

def left_mult_matrix(q):
    a, b, c, d = q
    # left multiplication by q = a + bi + cj + dk on x = (x0, x1, x2, x3)
    return [[a, -b, -c, -d], [b, a, -d, c], [c, d, a, -b], [d, -c, b, a]]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A): return [list(r) for r in zip(*A)]

def P1(K=40):
    q = hensel_four_squares(-1, K)
    L = left_mult_matrix(q)
    A = [[1, 0, 0, 0, 0]] + [[0] + row for row in L]
    J = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
    for i in range(1, 5): J[i][i] = -1
    M = matmul(transpose(A), matmul(J, A))
    ok = all((M[i][j] - (1 if i == j else 0)) % 2**K == 0 for i in range(5) for j in range(5))
    det_odd = (t7.det_int(A) % 2 == 1)
    return ok and det_odd, q, ok, det_odd

# ---------- P2 ----------
def P2(Nmax=200):
    bad = []
    for N in range(1, Nmax+1):
        if t8.a2([1, -1, -1, -1, -1], N) != t8.a2([1]*5, N): bad.append(N)
    return bad

# ---------- P3 / P4 ----------
def family(n, Nmax):
    data, rstar, rprim = t7.cone_zeta(n, Nmax)
    rdef = t8.sum_of_squares_counts(n+1, Nmax)
    chi, volP = t8.chiswell_volume(n)
    # R(n) exactly: R = vol(S^n)/vol(P^n) = [2 pi^{(n+1)/2}/Gamma((n+1)/2)] / [(-1)^{n/2} chi (2pi)^{n/2}/(n-1)!!]  — for even n this is rational:
    # pi^{(n+1)/2}/pi^{n/2} = sqrt(pi); Gamma((n+1)/2) = (n-1)!!/2^{n/2} sqrt(pi)  =>  vol(S^n) = 2 pi^{n/2} 2^{n/2}/(n-1)!! ;  ratio = 2^{n/2+1} / ((-1)^{n/2} chi)  * ((n-1)!!/(n-1)!!)... compute directly:
    dfact = 1
    for j in range(n-1, 0, -2): dfact *= j
    R = Fraction(2, 1) / ((-1)**(n//2) * chi)   # vol(S^n)/vol(P^n) = 2/((-1)^{n/2} chi), exact for even n
    assert abs(float(R) - t8.vol_sphere(n)/volP) < 1e-6 * float(R)
    rows = []
    for N in range(1, Nmax+1):
        if rstar[N] == 0 and rdef[N] == 0: continue
        lhs = rstar[N] * R
        ratio = Fraction(rdef[N]) / lhs if lhs else None
        v2 = 0; m = N
        while m % 2 == 0: m //= 2; v2 += 1
        rows.append(dict(N=N, exact=(lhs == rdef[N]), ratio=str(ratio), cls=(v2, (N >> v2) % 8)))
    return R, rows

def main():
    t0 = time.time()
    print('# toy 5699 — G7')
    ok, q, okM, detodd = P1()
    print(f'P1 (2-adic isometry exhibited, K=40): {"HIT" if ok else "MISS"}  q = {q}  A^T J A = I mod 2^40: {okM}, det A odd: {detodd}')
    bad = P2()
    print(f'P2 (2-adic densities of <1,-1,-1,-1,-1> and I_5 equal, N<=200): {"HIT" if not bad else "MISS at " + str(bad[:10])}')
    print('P3/P4 family rule:')
    out = {}
    allok = True
    for n in (2, 4, 6, 8):
        Nmax = 30 if n < 8 else 12
        R, rows = family(n, Nmax)
        exact_all = all(r['exact'] for r in rows)
        predicted = (n % 4 == 0)
        hit = (exact_all == predicted); allok &= hit
        # P4: ratio depends on 2-adic class only
        bycls = {}
        for r in rows: bycls.setdefault(r['cls'], set()).add(r['ratio'])
        p4 = all(len(v) == 1 for v in bycls.values())
        print(f'  n={n}: R(n)={R}  exact for all N<={Nmax}: {exact_all} (predicted {predicted}) -> {"HIT" if hit else "MISS"}; '
              f'P4 ratio = f(2-adic class): {p4}; classes: { {str(k): sorted(v) for k, v in sorted(bycls.items())} if not exact_all else "all 1"}')
        out[n] = dict(R=str(R), exact_all=exact_all, predicted=predicted, hit=hit, p4=p4, ratios_by_class={str(k): sorted(v) for k, v in bycls.items()})
    print(f'P3 (exact iff 4 | n): {"HIT" if allok else "MISS"}')
    json.dump(dict(toy=5699, P1=ok, q=q, P2_bad=bad, family=out, seconds=round(time.time()-t0, 1)), open(os.path.join(here, '.toy_5699_results.json'), 'w'), indent=1)
    print(f'elapsed {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
