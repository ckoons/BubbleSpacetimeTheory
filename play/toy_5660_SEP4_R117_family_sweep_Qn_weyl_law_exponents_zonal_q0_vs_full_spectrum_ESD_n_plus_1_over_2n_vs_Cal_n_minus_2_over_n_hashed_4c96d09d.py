#!/usr/bin/env python3
"""
Toy 5660 — Round 117 §2 (Grace, 2026-09-04). THE FAMILY SWEEP, run against the tables hashed 4c96d09d (09-03 15:05).
Space: Q^n = SO(n+2)/(SO(n) x SO(2)), real dimension 2n, rank-2 compact symmetric space (oriented 2-planes in R^{n+2}).
Definition (ESD note §3.1, pinned): N(L) = sum of multiplicities of Laplace eigenvalues <= L;  d_eff = 2 * lim log N / log L.
Spectrum: L^2(Q^n) = (+) V_mu over the K-spherical SO(n+2)-irreps mu, each once (Cartan–Helgason, Helgason GGA V.4.1):
  mu = (a, b, 0, ..., 0) in the epsilon basis, a >= b >= 0, with a = b (mod 2) [restricted roots e1±e2 of norm^2 2
  demand (a±b)/2 in Z; e1, e2 of norm^2 1 demand a, b in Z].  Positive control for the parity rule: n = 2, Q^2 = S^2 x S^2,
  where (a,b) <-> spins (j1,j2) = ((a+b)/2, (a-b)/2) and L^2(S^2 x S^2) is the INTEGER spins only.
  Eigenvalue (Casimir, epsilon basis, rho_i = (n+2)/2 - i): lam(a,b) = a(a+n) + b(b+n-2).  Zonal (q=0) = (p,0,...,0): lam = p(p+n).
  Multiplicity = dim V_mu by the Weyl dimension formula for B_m / D_m.
Two sector conventions are counted, exponents from both:
  (S) the spherical set with parity (the true L^2(Q^n));  (E) the ESD note's list "all (p,q), p >= q >= 0" without parity.
Predictions on the board before this run (hash 4c96d09d): ESD (n+1)/(2n) vs Cal's neighbour (n-2)/n; coincide only at n=5.
Output: per n, N_full and N_zonal at L = 10^2..10^6, per-decade slopes, d_eff (from the last two decades and a 3-point
Richardson read), the ratio, the two predictions, and sha256 of the result table.
"""
import json, hashlib, math, sys
from fractions import Fraction
from math import comb

def rho2(N):
    m = N // 2
    return [N - 2 * i for i in range(1, m + 1)]   # 2*rho_i (integers): B_m 2m-2i+1, D_m 2m-2i

_den_cache = {}
def weyl_dim(N, mu):
    """dim of SO(N) irrep with highest weight mu (length m = N//2), epsilon basis; integer arithmetic on doubled weights."""
    m = N // 2
    r = rho2(N); l = [2 * mu[i] + r[i] for i in range(m)]
    num = 1
    for i in range(m):
        li2 = l[i] * l[i]
        for j in range(i + 1, m):
            num *= (li2 - l[j] * l[j])
    if N % 2 == 1:
        for i in range(m): num *= l[i]
    den = _den_cache.get(N)
    if den is None:
        den = 1
        for i in range(m):
            for j in range(i + 1, m): den *= (r[i] * r[i] - r[j] * r[j])
        if N % 2 == 1:
            for i in range(m): den *= r[i]
        _den_cache[N] = den
    q, rem = divmod(num, den)
    assert rem == 0, (N, mu)
    return q

def harm_dim(N, p):   # harmonic polynomials of degree p on R^N = dim (p,0,...,0)
    return comb(p + N - 1, N - 1) - (comb(p + N - 3, N - 1) if p >= 2 else 0)

def lam(n, a, b): return a * (a + n) + b * (b + n - 2)

def controls():
    ok = True
    for N in range(4, 12):
        m = N // 2
        for p in range(0, 9):
            mu = [p] + [0] * (m - 1)
            if weyl_dim(N, mu) != harm_dim(N, p): ok = False; print("  FAIL harm", N, p)
        if N >= 5:
            mu = [1, 1] + [0] * (m - 2)
            if weyl_dim(N, mu) != N * (N - 1) // 2: ok = False; print("  FAIL adjoint", N)
    # SO(7) known dims: (1,0,0)=7, (1,1,0)=21, (2,0,0)=27, (2,1,0)=105, (2,2,0)=168, (1,1,1)=35
    known = {(1,0,0):7, (1,1,0):21, (2,0,0):27, (2,1,0):105, (2,2,0):168, (1,1,1):35}
    for mu, d in known.items():
        if weyl_dim(7, list(mu)) != d: ok = False; print("  FAIL SO(7)", mu, weyl_dim(7, list(mu)), d)
    # n = 2 control: SO(4) (a,b) = spins ((a+b)/2,(a-b)/2); dim = (a+b+1)(a-b+1); parity a=b mod 2 <-> integer spins
    for a in range(0, 6):
        for b in range(-a, a + 1):
            if weyl_dim(4, [a, b]) != (a + b + 1) * (a - b + 1): ok = False; print("  FAIL SO(4)", a, b)
    print("  controls:", "PASS" if ok else "FAIL")
    return ok

def sweep(n, Lmax, parity=True):
    N = n + 2; m = N // 2
    ev = []   # (lambda, mult, zonal?)
    amax = int(math.sqrt(Lmax)) + 1
    for a in range(0, amax + 1):
        if lam(n, a, 0) > Lmax: break
        for b in range(0, a + 1):
            if parity and (a - b) % 2: continue
            L = lam(n, a, b)
            if L > Lmax: break
            mu = [a, b] + [0] * (m - 2)
            ev.append((L, weyl_dim(N, mu), b == 0))
    ev.sort()
    return ev

def counts_at(ev, cuts):
    out = []; full = zon = 0; i = 0
    for c in cuts:
        while i < len(ev) and ev[i][0] <= c:
            full += ev[i][1]
            if ev[i][2]: zon += ev[i][1]
            i += 1
        out.append((c, full, zon))
    return out

def slopes(rows):
    s = []
    for k in range(1, len(rows)):
        c0, f0, z0 = rows[k - 1]; c1, f1, z1 = rows[k]
        s.append((math.log(f1 / f0) / math.log(c1 / c0), math.log(z1 / z0) / math.log(c1 / c0)))
    return s

if __name__ == '__main__':
    print("Toy 5660 — family sweep on Q^n, ESD definition d_eff = 2 * slope of log N(L) vs log L")
    controls()
    cuts = [10 ** k for k in range(2, 7)]
    ns = [int(x) for x in sys.argv[1:]] or [3, 4, 5, 6, 7]
    results = []
    for n in ns:
        for parity, tag in ((True, "S: spherical, a=b mod 2 (L^2(Q^n))"), (False, "E: ESD list, no parity")):
            ev = sweep(n, cuts[-1], parity)
            rows = counts_at(ev, cuts)
            sl = slopes(rows)
            print(f"\nn = {n}  Q^{n} = SO({n+2})/(SO({n}) x SO(2))   sector convention {tag}   eigen-lines counted: {len(ev)}")
            for (c, f, z), s in zip(rows[1:], sl):
                print(f"   L = 10^{int(math.log10(c))}: N_full = {f:>22d}  N_zonal = {z:>16d}   decade slopes full {s[0]:.4f}  zonal {s[1]:.4f}")
            # last-decade read and a 3-point Richardson (error ~ L^{-1/2} per decade: factor sqrt(10))
            sf, sz = sl[-1]; sf2, sz2 = sl[-2]
            r = math.sqrt(10)
            sfR = (r * sf - sf2) / (r - 1); szR = (r * sz - sz2) / (r - 1)
            d_full, d_zon = 2 * sf, 2 * sz
            d_fullR, d_zonR = 2 * sfR, 2 * szR
            esd = Fraction(n + 1, 2 * n); cal = Fraction(n - 2, n)
            print(f"   d_eff full = {d_full:.4f} (Richardson {d_fullR:.4f}; theorem 2n = {2*n})   d_eff zonal = {d_zon:.4f} (Richardson {d_zonR:.4f}; theorem n+1 = {n+1})")
            print(f"   RATIO measured {d_zon/d_full:.4f} (Richardson {d_zonR/d_fullR:.4f})   ESD (n+1)/(2n) = {esd} = {float(esd):.4f}   Cal (n-2)/n = {cal} = {float(cal):.4f}")
            results.append(dict(n=n, convention=tag[:1], N_full=[x[1] for x in rows], N_zonal=[x[2] for x in rows],
                                d_full=round(d_full, 4), d_zonal=round(d_zon, 4), d_full_R=round(d_fullR, 4), d_zonal_R=round(d_zonR, 4),
                                ratio=round(d_zon / d_full, 4), ratio_R=round(d_zonR / d_fullR, 4), ESD=float(esd), Cal=float(cal)))
    s = json.dumps(results, sort_keys=True)
    h = hashlib.sha256(s.encode()).hexdigest()[:16]
    with open('.family_sweep_Qn_results_5660.json', 'w') as f: f.write(s)
    print("\nresult table sha256", h, " -> play/.family_sweep_Qn_results_5660.json")
