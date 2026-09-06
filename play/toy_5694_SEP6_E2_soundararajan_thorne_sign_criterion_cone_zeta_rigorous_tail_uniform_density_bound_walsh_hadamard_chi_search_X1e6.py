#!/usr/bin/env python3
"""Toy 5694 — E2 (T-ST): Soundararajan–Thorne sign criterion on A(s) = sum b(N) N^-s, b(N) = prod_p alpha_p(N)
(cone-zeta coefficients / N^{3/2}). Rigorous tail from a uniform bound on b(N). chi searched over 2^15 sign
patterns on primes <= 47 (Walsh–Hadamard) x 4 rules on large primes. Prereg hashed before run."""
import numpy as np, math, time, json, os
from fractions import Fraction
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
X = 10**6; P = 10**5
SIGMAS = [1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.5, 1.6]
score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}", flush=True)
def ordp(N, p):
    e = 0
    while N % p == 0: N //= p; e += 1
    return e

# ---------- exact 2-adic densities by convolution on supports ----------
def sq_support(q, sign):
    v = (sign * (np.arange(q, dtype=np.int64) ** 2)) % q
    return np.unique(v, return_counts=True)
def conv(A, B, q):
    va, ca = A; vb, cb = B
    s = ((va[:, None] + vb[None, :]) % q).ravel(); w = (ca[:, None] * cb[None, :]).ravel()
    cnt = np.zeros(q, dtype=np.int64); np.add.at(cnt, s, w)
    nz = np.nonzero(cnt)[0]; return nz, cnt[nz]
def density_table(p, k, signs):
    q = p ** k; d = None
    for s in signs:
        c = sq_support(q, s); d = c if d is None else conv(d, c, q)
    full = np.zeros(q, dtype=np.int64); full[d[0]] = d[1]; return full, q
LOR = (1, -1, -1, -1, -1)
print("P2: 2-adic split alpha2(N) = prim2(N) + alpha2(N/4)/8, prim2 a function of N mod 8?", flush=True)
NV = 1024; tabs = {}
for k in range(3, 15):
    tabs[k] = density_table(2, k, LOR)
def alpha2_conv(N, k):
    full, q = tabs[k]; return Fraction(int(full[N % q]), 2 ** (4 * k))
a2 = {}; unstable = []
for N in range(1, NV + 1):
    e = ordp(N, 2); k = e + 3
    a, b = alpha2_conv(N, k), alpha2_conv(N, k + 1)
    if a != b: unstable.append(N)
    a2[N] = a
prim = {N: a2[N] - (Fraction(1, 8) * a2[N // 4] if N % 4 == 0 else 0) for N in a2}
mod_ok = None
for m in (8, 16, 32, 64):
    classes = {}
    ok = True
    for N, v in prim.items():
        r = N % m
        if r in classes and classes[r] != v: ok = False; break
        classes[r] = v
    if ok: mod_ok = m; prim_table = classes; break
sc("P2", mod_ok == 8 and not unstable, f"prim2 is a function of N mod {mod_ok}; unstable {unstable[:5]}")
if mod_ok is None: raise SystemExit("2-adic instrument not validated")
print("  prim2 table:", {r: str(prim_table[r]) for r in sorted(prim_table)})
sup_a2 = max(prim_table.values()) / (1 - Fraction(1, 8))

# ---------- odd p: Lemma 1 vs convolution at p = 11, 13 ----------
def alpha_rec(p, N):
    e = ordp(N, p); u = N // p ** e
    if e == 0:
        l = pow(u % p, (p - 1) // 2, p); l = -1 if l == p - 1 else l
        return 1 + Fraction(l, p * p)
    if e == 1: return 1 - Fraction(1, p ** 4)
    return (1 - Fraction(1, p ** 4)) + Fraction(1, p ** 3) * alpha_rec(p, N // (p * p))
print("P3: Lemma 1 vs convolution, p = 11, 13, N <= 300", flush=True)
mism = []
for p in (11, 13):
    T = {k: density_table(p, k, LOR) for k in (1, 2, 3, 4)}
    for N in range(1, 301):
        e = ordp(N, p); k = e + 1; full, q = T[k]; full2, q2 = T[k + 1]
        a = Fraction(int(full[N % q]), p ** (4 * k)); b = Fraction(int(full2[N % q2]), p ** (4 * (k + 1)))
        if a != b or a != alpha_rec(p, N): mism.append((p, N))
sc("P3", not mism, f"mismatches {mism[:5]}")

# ---------- b(N) for N <= X ----------
print(f"building b(N), N <= {X} ...", flush=True)
sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
for i in range(2, math.isqrt(X) + 1):
    if sieve[i]: sieve[i * i::i] = False
primes = np.nonzero(sieve)[0]
Ns = np.arange(X + 1, dtype=np.int64)
# alpha_2 by recursion (floats)
primf = np.array([float(prim_table[r]) for r in range(8)])
alpha2 = primf[Ns % 8]; alpha2[0] = 0.0
for N in range(4, X + 1, 4): alpha2[N] += alpha2[N // 4] / 8.0
logb = np.log(alpha2[1:]); logb = np.concatenate([[0.0], logb])   # index by N
# odd p | N: Lemma 1 recursion, vectorised per prime
def alpha_rec_vec(p, M):          # M array, p odd
    out = np.empty(len(M)); e0 = (M % p != 0)
    if e0.any():
        u = M[e0] % p; l = np.array([pow(int(x), (p - 1) // 2, p) for x in u], dtype=np.int64); l = np.where(l == p - 1, -1, l)
        out[e0] = 1 + l / p ** 2
    e1 = (~e0) & (M % (p * p) != 0); out[e1] = 1 - p ** -4.0
    e2 = (M % (p * p) == 0)
    if e2.any(): out[e2] = (1 - p ** -4.0) + p ** -3.0 * alpha_rec_vec(p, M[e2] // (p * p))
    return out
for p in primes[1:]:
    p = int(p); idx = np.arange(p, X + 1, p)
    logb[idx] += np.log(alpha_rec_vec(p, idx))
# p not dividing 2N, p < P
oddp = primes[(primes > 2) & (primes < P)]
for j, p in enumerate(oddp):
    p = int(p); tab = -np.ones(p); tab[(np.arange(1, p) ** 2) % p] = 1.0; tab[0] = 0.0
    logb += np.log1p(tab[Ns % p] / (p * p))
    if j % 2000 == 0: print(f"   prime {p}  [{time.time()-t0:.0f}s]", flush=True)
b = np.exp(logb); b[0] = 0.0
B_max = float(sup_a2) * (7 / 8) * 1.2020569031595943 * (4 / 5) * (math.pi ** 2 / 6) / (math.pi ** 4 / 90)
print(f"  b(1..12) = {np.round(b[1:13], 6).tolist()}; max b(N<=X) = {b[1:].max():.5f}, min = {b[1:].min():.5f}; B_max = {B_max:.5f}", flush=True)
trunc_rel = math.exp(1.0001 / P) - 1

# ---------- parity classes ----------
small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
cls = np.zeros(X + 1, dtype=np.int64); Omega = np.zeros(X + 1, dtype=np.int64)
for p in primes:
    p = int(p); pk = p
    while pk <= X: Omega[pk::pk] += 1; pk *= p
for i, p in enumerate(small):
    v = np.zeros(X + 1, dtype=np.int64); pk = p
    while pk <= X: v[pk::pk] += 1; pk *= p
    cls |= ((v & 1) << i); Omega -= v
om_par = Omega & 1                                   # parity of Omega restricted to primes > 47
# large-prime rules: multiplicative sign from primes > 47
def large_sign(rule):
    s = np.ones(X + 1)
    if rule == 'all+': return s
    if rule == 'all-': return np.where(om_par == 1, -1.0, 1.0)
    for p in primes[primes > 47]:
        p = int(p); sgn = 1.0 if (p % 4 == 1) == (rule == 'mod4+') else -1.0
        if sgn < 0:
            pk = p
            while pk <= X: s[pk::pk] *= -1.0; pk *= p
    return s
def wht(a):
    a = a.copy(); h = 1; n = len(a)
    while h < n:
        a = a.reshape(-1, 2, h); a = np.stack([a[:, 0] + a[:, 1], a[:, 0] - a[:, 1]], axis=1).reshape(n); h *= 2
    return a
def chi_vec(eps_bits, rule):     # direct chi(N) for a pattern, for the P5 cross-check
    s = large_sign(rule).copy()
    for i, p in enumerate(small):
        if (eps_bits >> i) & 1:
            pk = p
            while pk <= X: s[pk::pk] *= -1.0; pk *= p
    return s

# ---------- P1 control: Keeper's numbers ----------
print("P1: Keeper's partial sums at N <= 20000", flush=True)
Om_full = Omega.copy()
for i, p in enumerate(small):
    v = np.zeros(X + 1, dtype=np.int64); pk = p
    while pk <= X: v[pk::pk] += 1; pk *= p
    Om_full += v
liou = np.where(Om_full & 1, -1.0, 1.0)
chi_m4 = large_sign('mod4+').copy()
for p in small:
    sgn = 1.0 if p % 4 == 1 else -1.0
    if sgn < 0:
        pk = p
        while pk <= X: chi_m4[pk::pk] *= -1.0; pk *= p
n2e4 = np.arange(1, 20001)
S_liou = float(np.sum(b[1:20001] * liou[1:20001] * n2e4 ** -1.1))
S_m4 = float(np.sum(b[1:20001] * chi_m4[1:20001] * n2e4 ** -1.1))
S_m4b = float(np.sum(b[1:20001] * chi_m4[1:20001] * n2e4 ** -1.25))
sc("P1", abs(S_liou + 0.082) < 3e-3 and abs(S_m4 + 0.370) < 3e-3 and abs(S_m4b + 0.012) < 3e-3,
   f"Liouville sigma=1.1: {S_liou:.4f} (K: -0.082); mod4 sigma=1.1: {S_m4:.4f} (K: -0.370); mod4 sigma=1.25: {S_m4b:.4f} (K: -0.012)")

# ---------- the search ----------
print("P4: search", flush=True)
results = []; best_overall = None
rules = ['all+', 'all-', 'mod4+', 'mod4-']
lsign = {r: large_sign(r) for r in rules}
for sigma in SIGMAS:
    w0 = b[1:] * Ns[1:] ** (-sigma)
    err_trunc = trunc_rel * float(np.sum(w0)); err_float = 1e-15 * float(np.sum(np.abs(w0)))
    tail = B_max * X ** (1 - sigma) / (sigma - 1)
    for rule in rules:
        Sc = np.bincount(cls[1:], weights=w0 * lsign[rule][1:], minlength=1 << 15)
        F = wht(Sc); k = int(np.argmin(F)); Smin = float(F[k])
        T = Smin + err_trunc + err_float + tail
        pat = {p: (-1 if (k >> i) & 1 else 1) for i, p in enumerate(small)}
        results.append({'sigma': sigma, 'rule': rule, 'S_X': Smin, 'err_trunc': err_trunc, 'err_float': err_float, 'tail': tail, 'T': T, 'chi_small': pat})
        if best_overall is None or T < best_overall['T']: best_overall = results[-1]
    print(f"  sigma {sigma:.2f}: tail {tail:.4f}; best over rules: " + "; ".join(f"{r['rule']} S={r['S_X']:+.4f} T={r['T']:+.4f}" for r in results[-4:]), flush=True)
hit = best_overall['T'] < 0
sc("P4", hit, f"best T = {best_overall['T']:+.5f} at sigma {best_overall['sigma']}, rule {best_overall['rule']}, S_X {best_overall['S_X']:+.5f}, tail {best_overall['tail']:.5f}")
print("  best chi on primes <= 47:", best_overall['chi_small'])
# P5: direct evaluation of the best pattern, and B_max < 4
kbits = sum((1 << i) for i, p in enumerate(small) if best_overall['chi_small'][p] < 0)
cv = chi_vec(kbits, best_overall['rule']); S_direct = float(np.sum(b[1:] * cv[1:] * Ns[1:] ** (-best_overall['sigma'])))
sc("P5", B_max < 4 and abs(S_direct - best_overall['S_X']) < 1e-10, f"B_max {B_max:.4f}; WHT {best_overall['S_X']:.12f} vs direct {S_direct:.12f}")
if not hit:
    # estimate (NOT rigorous) of X needed at the best sigma: tail(X') = -S_X - errs, assuming S_X stable
    s = best_overall; need = -(s['S_X'] + s['err_trunc'] + s['err_float'])
    if need > 0:
        Xn = (need * (s['sigma'] - 1) / B_max) ** (1 / (1 - s['sigma']))
        print(f"  estimate only: at sigma {s['sigma']} the tail bound crosses S_X at X ~ {Xn:.2e} (assumes S_X frozen)")
    else: print("  no sigma in the grid has a negative partial sum: the criterion cannot fire from this search")
print(f"\nSCORE {sum(score)}/{len(score)}   [{time.time()-t0:.0f}s]")
json.dump({'X': X, 'P': P, 'B_max': B_max, 'sup_alpha2': float(sup_a2), 'prim2_table': {r: str(prim_table[r]) for r in sorted(prim_table)},
           'control': {'liouville_1.1': S_liou, 'mod4_1.1': S_m4, 'mod4_1.25': S_m4b}, 'results': results, 'best': best_overall,
           'b_first_20': b[1:21].tolist(), 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.tst_5694.json'), 'w'), indent=1)
