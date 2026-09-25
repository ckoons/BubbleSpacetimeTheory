#!/usr/bin/env python3
"""
Toy 5792 — Cal's "nothing counts 19": a scan with the NULL WRITTEN FIRST (Elie, 2026-09-25, round 4 item 2).

UNIVERSE (fixed before any count):
  A. Irreps (dim <= 250) of so(7,C) = B3 [SO(5,2)], so(5) = B2 [K's simple part], so(3) = B1 [Peirce V1].
     Weight multiplicities by Freudenthal's formula (exact Fractions), dims by Weyl.
  B. Branchings of every B3 irrep (dim <= 250) to K = so(5)+so(2) (charge = x3), and of every B2 irrep
     (dim <= 250) to the Peirce subalgebra so(3)+so(2) (charge = x1, spin from x2): 5 -> 1_{+1} + 3_0 + 1_{-1}.
     Also B3 -> so(3)+so(2)+so(2) (the full chain).
  C. Peirce spaces of V = C^5: dims (1, 3, 1).  Clifford Cl(5) by degree (1,5,10,10,5,1); Cl^0(5) = 16.
HIT DEFINITIONS for a target N (the SAME for every N):
  H1  an irrep in A of dimension N
  H2  an irreducible component of a branching in B of dimension N  (component = irrep of the subalgebra)
  H3  a branching in B whose ENTIRE decomposition is exactly two components of dims (N-3) and 3
  H4  a single-charge sector (fixed so(2) charge, all so(5) or so(3) pieces together) of dim N
  H5  a Peirce or Clifford object in C of dim N, or a Clifford degree-sum of CONSECUTIVE degrees = N
NULL: run H1-H5 for every N in 10..40 and report where N = 19 ranks. The prettiest hit is not the result.

DIRECTION BEFORE NUMBERS:
  P1  H1 = 0 for N = 19 (no 19-dim irrep of B3, B2, B1 other than B1's spin 9, which IS dim 19 — so H1(19) = 1
      from B1 trivially; stated so it is not 'found' later).
  P2  H3(19) = 0: no branching is exactly 16 + 3.
  P3  19's total (H2+H3+H4+H5) is at or below the median over N = 10..40.
"""
from fractions import Fraction as Fr
from itertools import product
from collections import Counter

def posroots(n):
    R = []
    for i in range(n):
        for j in range(i + 1, n):
            for s in (1, -1):
                v = [0]*n; v[i] = 1; v[j] = s; R.append(tuple(v))
        v = [0]*n; v[i] = 1; R.append(tuple(v))
    return R

def ip(a, b):
    return sum(Fr(x)*Fr(y) for x, y in zip(a, b))

def rho(n):
    return tuple(Fr(2*n - 2*i - 1, 2) for i in range(n))

def weyl_dim(lam):
    n = len(lam); r = rho(n); lr = tuple(Fr(a) + b for a, b in zip(lam, r))
    num = den = Fr(1)
    for a in posroots(n):
        num *= ip(lr, a); den *= ip(r, a)
    return int(num/den)

def dom(mu):
    return tuple(sorted((abs(x) for x in mu), reverse=True))

def weights(lam):
    """full weight multiset of the B_n irrep with highest weight lam (Freudenthal on dominant weights)."""
    n = len(lam); lam = tuple(Fr(x) for x in lam); P = posroots(n); r = rho(n)
    # dominant weights below lam: same integrality class, lam - mu in positive root lattice (sum condition free for B_n)
    half = lam[0].denominator == 2
    M = int(lam[0]) + 1
    cands = set()
    rng = [Fr(2*k + 1, 2) for k in range(M)] if half else [Fr(k) for k in range(M + 1)]
    for mu in product(rng, repeat=n):
        if all(mu[i] >= mu[i+1] for i in range(n - 1)) and mu[-1] >= 0:
            # mu <= lam in dominance: partial sums
            ok = all(sum(lam[:k]) - sum(mu[:k]) >= 0 for k in range(1, n + 1))
            if ok:
                cands.add(mu)
    cands = sorted(cands, key=lambda m: -sum(sum(m[:k]) for k in range(1, len(m) + 1)))   # simple-root height
    mult = {lam: 1}
    lr2 = ip(tuple(a + b for a, b in zip(lam, r)), tuple(a + b for a, b in zip(lam, r)))
    for mu in cands:
        if mu == lam:
            continue
        s = Fr(0)
        for a in P:
            k = 1
            while True:
                nu = tuple(m + k*x for m, x in zip(mu, a))
                d = dom(nu)
                if d not in mult and not any(d == c for c in cands):
                    break
                if any(sum(lam[:j]) - sum(d[:j]) < 0 for j in range(1, n + 1)):
                    break
                s += mult.get(d, 0)*ip(nu, a)
                k += 1
        denom = lr2 - ip(tuple(m + b for m, b in zip(mu, r)), tuple(m + b for m, b in zip(mu, r)))
        m_ = 2*s/denom
        if m_:
            mult[mu] = int(m_)
    # expand Weyl orbits (signed permutations)
    from itertools import permutations
    W = Counter()
    for mu, m_ in mult.items():
        orbit = set()
        for p in set(permutations(mu)):
            for signs in product((1, -1), repeat=n):
                orbit.add(tuple(s*x for s, x in zip(signs, p)))
        for o in orbit:
            W[o] += m_
    return W

def irreps(n, maxdim):
    out = []
    for c in product(range(0, 9), repeat=n):
        for half in (False, True):
            lam = tuple(Fr(x) + (Fr(1, 2) if half else 0) for x in c)
            if all(lam[i] >= lam[i+1] for i in range(n - 1)):
                d = weyl_dim(lam)
                if d <= maxdim:
                    out.append((lam, d))
    return sorted(set(out), key=lambda t: t[1])

def peel(W, n):
    """decompose a B_n weight multiset into irreps; returns list of (highest weight, dim)."""
    W = Counter({k: v for k, v in W.items() if v})
    comps = []
    while W:
        top = max((w for w in W if all(w[i] >= w[i+1] for i in range(n - 1)) and w[-1] >= 0),
                  key=lambda w: (sum(w), w))
        Wi = weights(top)
        comps.append((top, weyl_dim(top)))
        for k, v in Wi.items():
            W[k] -= v
            if W[k] == 0:
                del W[k]
            elif W[k] < 0:
                raise RuntimeError("peel failed")
    return comps

def spin_peel(W1):
    """B1 (so(3)) weights (single coordinate) -> list of dims 2j+1"""
    W = Counter({k: v for k, v in W1.items() if v}); comps = []
    while W:
        top = max(W)
        j = top[0]
        k = j
        while k >= -j:
            W[(k,)] -= 1
            if W[(k,)] == 0:
                del W[(k,)]
            k -= 1
        comps.append(int(2*j + 1))
    return comps

MAXD = 250
A3, A2, A1 = irreps(3, MAXD), irreps(2, MAXD), [((Fr(j, 2),), j + 1) for j in range(0, 60) if j + 1 <= MAXD]
print(f"Toy 5792 — the 19 scan. Universe: {len(A3)} B3 irreps, {len(A2)} B2 irreps, {len(A1)} B1 irreps (dim <= {MAXD})")

# branchings -> record (components dims list, sector dims list) per branching
branchings = []   # (label, [component dims], [sector dims])
for lam, d in A3:
    W = weights(lam)
    assert sum(W.values()) == d
    # to so(5)+so(2): charge x3
    sectors = {}
    for w, m in W.items():
        sectors.setdefault(w[2], Counter())[(w[0], w[1])] += m
    comps, secd = [], []
    for q, Ws in sectors.items():
        secd.append(sum(Ws.values()))
        comps += [c[1] for c in peel(Ws, 2)]
    branchings.append((f"B3{tuple(map(str, lam))}->so5+so2", comps, secd))
    # full chain to so(3)+so(2)+so(2): charges x1? use x3 and x1, spin x2
    sec2 = {}
    for w, m in W.items():
        sec2.setdefault((w[0], w[2]), Counter())[(w[1],)] += m
    comps2, secd2 = [], []
    for q, Ws in sec2.items():
        secd2.append(sum(Ws.values()))
        comps2 += spin_peel(Ws)
    branchings.append((f"B3{tuple(map(str, lam))}->so3+so2+so2", comps2, secd2))
for lam, d in A2:
    W = weights(lam)
    assert sum(W.values()) == d
    sec = {}
    for w, m in W.items():
        sec.setdefault(w[0], Counter())[(w[1],)] += m
    comps, secd = [], []
    for q, Ws in sec.items():
        secd.append(sum(Ws.values()))
        comps += spin_peel(Ws)
    branchings.append((f"B2{tuple(map(str, lam))}->so3+so2 (Peirce)", comps, secd))

C_objs = [1, 3, 1, 32, 16] + [1, 5, 10, 10, 5, 1]
cl = [1, 5, 10, 10, 5, 1]
cl_consec = [sum(cl[i:j]) for i in range(6) for j in range(i + 1, 7)]

def hits(N):
    h1 = sum(1 for _, d in A3 + A2 + A1 if d == N)
    h2 = sum(c.count(N) for _, c, _ in branchings)
    h3 = sum(1 for _, c, _ in branchings if sorted(c) == sorted([N - 3, 3]))
    h4 = sum(s.count(N) for _, _, s in branchings)
    h5 = C_objs.count(N) + cl_consec.count(N)
    return h1, h2, h3, h4, h5

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

# controls
v7 = dict(weights((Fr(1), Fr(0), Fr(0))))
check("control: B3 vector has dim 7 and branches to so5+so2 as 5 + 1 + 1",
      sorted(branchings[[b[0] for b in branchings].index("B3('1', '0', '0')->so5+so2")][1]) == [1, 1, 5], can_fail=False)
check("control: B3 spinor (1/2,1/2,1/2) has dim 8; B2 vector 5 -> Peirce 1 + 3 + 1",
      weyl_dim((Fr(1, 2),)*3) == 8 and sorted(branchings[[b[0] for b in branchings].index("B2('1', '0')->so3+so2 (Peirce)")][1]) == [1, 1, 3], can_fail=False)

print("\n  N : H1 H2 H3 H4 H5 | total(H2..H5)")
tab = {}
for N in range(10, 41):
    h = hits(N); tab[N] = h
    flag = "  <-- 19" if N == 19 else ""
    print(f"  {N:2d}: {h[0]:2d} {h[1]:3d} {h[2]:2d} {h[3]:3d} {h[4]:2d} | {sum(h[1:]):4d}{flag}")
h19 = tab[19]
tots = sorted(sum(h[1:]) for h in tab.values())
median = tots[len(tots)//2]
rank = 1 + sum(1 for N, h in tab.items() if sum(h[1:]) > sum(h19[1:]))
print(f"\n  19: H1={h19[0]} (B1 spin-9 only: {[d for _, d in A1].count(19)}), H2={h19[1]}, H3={h19[2]}, H4={h19[3]}, H5={h19[4]}; "
      f"total {sum(h19[1:])}, median over 10..40 = {median}, rank {rank}/31")
where19 = [(lab, c) for lab, c, s in branchings if 19 in c or 19 in s]
for lab, c in where19[:10]:
    print(f"    19 appears in: {lab}: components {sorted(c)}")
check("P1 H1(19) = 1, and it is B1's spin-9 (no 19-dim irrep of B3 or B2)",
      h19[0] == 1 and all(d != 19 for _, d in A3 + A2))
check("P2 H3(19) = 0: no branching is exactly 16 + 3", h19[2] == 0)
check("P3 19's total at or below the median of N = 10..40", sum(h19[1:]) <= median)

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
