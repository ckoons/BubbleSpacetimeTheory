#!/usr/bin/env python3
"""Toy 5694b — POST-HOC (no hash; declared): the strongest chi the criterion allows, by coordinate descent on
chi(p) over ALL primes p <= X. Flipping chi(p) negates every N with v_p(N) odd; descend to a local minimum of
S_X(sigma, chi) from several starts. Reports min S_X per sigma vs the rigorous tail. A positive minimum at sigma
means NO completely multiplicative chi (of any kind) fires the criterion at that sigma from this X."""
import numpy as np, math, time, json, os
from fractions import Fraction
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
X = 10**6; P = 10**5
prim = {0: Fraction(5,8), 1: Fraction(5,8), 2: Fraction(5,4), 3: Fraction(5,4), 4: Fraction(5,8), 5: Fraction(7,8), 6: Fraction(5,4), 7: Fraction(5,4)}  # 5694 P2 table
sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
for i in range(2, math.isqrt(X) + 1):
    if sieve[i]: sieve[i * i::i] = False
primes = np.nonzero(sieve)[0]; Ns = np.arange(X + 1, dtype=np.int64)
primf = np.array([float(prim[r]) for r in range(8)]); alpha2 = primf[Ns % 8]; alpha2[0] = 0.0
for N in range(4, X + 1, 4): alpha2[N] += alpha2[N // 4] / 8.0
logb = np.log(alpha2[1:]); logb = np.concatenate([[0.0], logb])
def alpha_rec_vec(p, M):
    out = np.empty(len(M)); e0 = (M % p != 0)
    if e0.any():
        u = M[e0] % p; l = np.array([pow(int(x), (p - 1) // 2, p) for x in u], dtype=np.int64); l = np.where(l == p - 1, -1, l)
        out[e0] = 1 + l / p ** 2
    e1 = (~e0) & (M % (p * p) != 0); out[e1] = 1 - p ** -4.0
    e2 = (M % (p * p) == 0)
    if e2.any(): out[e2] = (1 - p ** -4.0) + p ** -3.0 * alpha_rec_vec(p, M[e2] // (p * p))
    return out
for p in primes[1:]:
    p = int(p); idx = np.arange(p, X + 1, p); logb[idx] += np.log(alpha_rec_vec(p, idx))
for p in primes[(primes > 2) & (primes < P)]:
    p = int(p); tab = -np.ones(p); tab[(np.arange(1, p) ** 2) % p] = 1.0; tab[0] = 0.0
    logb += np.log1p(tab[Ns % p] / (p * p))
b = np.exp(logb); b[0] = 0.0
B_max = float(max(prim.values()) / (1 - Fraction(1, 8))) * (7 / 8) * 1.2020569031595943 * (4 / 5) * 15 / math.pi ** 2
print(f"b built [{time.time()-t0:.0f}s]; B_max {B_max:.4f}", flush=True)
# odd-valuation index lists per prime (v_p(N) odd)
odd_idx = {}
for p in primes:
    p = int(p); v = np.zeros(X + 1, dtype=np.int8) if p < 1000 else None
    if p < 1000:
        pk = p
        while pk <= X: v[pk::pk] += 1; pk *= p
        odd_idx[p] = np.nonzero(v & 1)[0]
    else:   # p^2 > X only when p > 1000: v_p in {0,1,2}; odd iff p | N and p^2 not | N
        idx = np.arange(p, X + 1, p); odd_idx[p] = idx[idx % (p * p) != 0]
out = {}
for sigma in [1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.5]:
    w = b * Ns.astype(float) ** (-sigma); w[0] = 0.0
    best = None
    for start in ('liouville', 'all+', 'mod4+'):
        chi = np.ones(X + 1)
        for p in primes:
            p = int(p); s0 = {'liouville': -1.0, 'all+': 1.0, 'mod4+': 1.0 if p % 4 == 1 else -1.0}[start]
            if s0 < 0: chi[odd_idx[p]] *= -1.0
        S = float(np.sum(w * chi)); improved = True; sweeps = 0
        while improved and sweeps < 20:
            improved = False; sweeps += 1
            for p in primes:
                p = int(p); idx = odd_idx[p]; d = -2.0 * float(np.sum(w[idx] * chi[idx]))
                if d < -1e-13: chi[idx] *= -1.0; S += d; improved = True
        if best is None or S < best[0]: best = (S, start, sweeps, int(np.sum(chi[primes] < 0)))
    tail = B_max * X ** (1 - sigma) / (sigma - 1)
    out[sigma] = {'minS': best[0], 'start': best[1], 'sweeps': best[2], 'n_neg_primes': best[3], 'tail': tail, 'T': best[0] + tail}
    print(f"  sigma {sigma:.2f}: min S_X = {best[0]:+.5f} (from {best[1]}, {best[2]} sweeps, {best[3]} primes negative); tail {tail:.5f}; T = {best[0]+tail:+.5f}  [{time.time()-t0:.0f}s]", flush=True)
json.dump(out, open(os.path.join(HERE, '.tst_5694b.json'), 'w'), indent=1)
print(f"[{time.time()-t0:.0f}s]")
