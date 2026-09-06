#!/usr/bin/env python3
"""Toy 5693 — E1 (gate item, Keeper handoff 09-06): BLIND re-run of K1862-A. My own chamber enumeration,
stabilizer orders by BFS closure on reflection matrices, local densities by cyclic convolution, Siegel
constancy of r*(N)/(N^{3/2} prod_p alpha_p(N)) for N <= 60, I_5 positive control. Prereg hashed before run."""
import numpy as np, math, time, json, os, sys
from fractions import Fraction
from itertools import combinations
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
NMAX = 60; PMAX = 10**5
score = []; 
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}")

# ---------- the form and the roots ----------
J = np.diag([1, -1, -1, -1, -1])
def ip(x, y): return int(x @ J @ y)
E = np.eye(5, dtype=np.int64)
roots = [E[2]-E[1], E[3]-E[2], E[4]-E[3], -E[4], E[0]+E[1]+E[2]+E[3]]
def refl(r):
    rr = ip(r, r); M = np.eye(5, dtype=np.int64) - (2 * np.outer(r, r @ J)) // rr
    assert (M.T @ J @ M == J).all(); return M
S = [refl(r) for r in roots]

print("P1 chamber / diagram")
e0 = E[0]
ok_e0 = all(ip(e0, roots[i]) == 0 for i in range(4)) and ip(e0, roots[4]) == 1
G = np.array([[ip(a, b) for b in roots] for a in roots])
print("  Gram:", G.tolist())
def coxeter_m(i, j):
    c = G[i, j] / math.sqrt(G[i, i] * G[j, j])   # cos of angle between roots (both norms negative -> ratio positive)
    return {0.0: 2, 0.5: 3, round(1/math.sqrt(2), 6): 4}.get(round(c, 6), None)
cox = {(i, j): coxeter_m(i, j) for i, j in combinations(range(5), 2)}
expected = {(0,1):3,(1,2):3,(2,3):4,(2,4):3}
ok_cox = all(cox[k] == expected.get(k, 2) for k in cox)
sing = {tuple(s): abs(round(np.linalg.det(G[np.ix_(s, s)]))) for s in combinations(range(5), 4)}
ok_cusp = sing[(1,2,3,4)] == 0 and all(v != 0 for k, v in sing.items() if k != (1,2,3,4))
print("  4-subset |det|:", sing)
sc("P1", ok_e0 and ok_cox and ok_cusp, f"e0 in C {ok_e0}; Coxeter {cox}; cusp {ok_cusp}")

# ---------- stabilizers by BFS ----------
_cache = {}
def stab_order(idx):
    idx = tuple(sorted(idx))
    if idx in _cache: return _cache[idx]
    gens = [S[i] for i in idx]; I5 = np.eye(5, dtype=np.int64)
    seen = {I5.tobytes()}; frontier = [I5]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = g @ M; b = P.tobytes()
                if b not in seen:
                    seen.add(b); nxt.append(P)
                    if len(seen) > 10**4: raise RuntimeError(f"BFS did not close for {idx}")
        frontier = nxt
    _cache[idx] = len(seen); return len(seen)

# ---------- chamber enumeration ----------
def chamber_vectors(N):
    out = []
    for x1 in range(0, N + 1):
        for x2 in range(0, x1 + 1):
            for x3 in range(0, x2 + 1):
                for x4 in range(0, x3 + 1):
                    s = N + x1*x1 + x2*x2 + x3*x3 + x4*x4; x0 = math.isqrt(s)
                    if x0 * x0 == s and x0 >= x1 + x2 + x3:
                        out.append(np.array([x0, x1, x2, x3, x4], dtype=np.int64))
    return out
rstar = {}; orbits = {}; stabs_seen = set(); allfinite = True
for N in range(1, NMAX + 1):
    tot = Fraction(0); vecs = chamber_vectors(N)
    for x in vecs:
        idx = [i for i in range(5) if ip(x, roots[i]) == 0]
        try: o = stab_order(idx)
        except RuntimeError as ex: allfinite = False; print("  ", ex); o = 1
        stabs_seen.add(o); tot += Fraction(1, o)
    rstar[N] = tot; orbits[N] = len(vecs)
print("P2 stabilizers")
allowed = {1,2,4,6,8,12,16,24,48,96,120,384}
sc("P2", stab_order([0,1,2,3]) == 384 and allfinite and stabs_seen <= allowed,
   f"|W_e0|={stab_order([0,1,2,3])}; orders met {sorted(stabs_seen)}")
print("P3 coefficients vs Keeper's list")
keeper = [Fraction(1,384),Fraction(1,96),Fraction(1,48),Fraction(3,128),Fraction(7,240),Fraction(1,16),
          Fraction(1,12),Fraction(5,96),Fraction(25,384),Fraction(7,48),Fraction(7,48),Fraction(5,48)]
korb = [1,1,1,2,2,2,2,3,3,2,2,4]
m3 = sum(rstar[N] == keeper[N-1] for N in range(1,13)); m3o = sum(orbits[N] == korb[N-1] for N in range(1,13))
print("  mine:", [str(rstar[N]) for N in range(1,13)]); print("  orbits:", [orbits[N] for N in range(1,13)])
sc("P3", m3 == 12 and m3o == 12, f"{m3}/12 coefficients, {m3o}/12 orbit counts")

# ---------- local densities by convolution ----------
def sq_dist(q, sign):
    cnt = np.zeros(q, dtype=object)
    for x in range(q): cnt[(sign * x * x) % q] += 1
    return cnt
def cconv(a, b):
    q = len(a); out = np.zeros(q, dtype=object)
    for i in range(q):
        if a[i]: out = out + a[i] * np.roll(b, i)
    return out
def density(p, k, N, signs):
    q = p**k; d = None
    for s in signs:
        c = sq_dist(q, s); d = c if d is None else cconv(d, c)
    return Fraction(int(d[N % q]), p**(4*k))
def ordp(N, p):
    e = 0
    while N % p == 0: N //= p; e += 1
    return e
LOR = (1,-1,-1,-1,-1); DEF = (1,1,1,1,1)
def alpha_conv(p, N, signs):
    e = ordp(N, p); k = e + 3 if p == 2 else e + 1
    a, b = density(p, k, N, signs), density(p, k + 1, N, signs)
    return a, (a == b)
def alpha_rec(p, N):           # K1862-C Lemma 1, odd p
    e = ordp(N, p); u = N // p**e
    if e == 0:
        leg = pow(u % p, (p-1)//2, p); leg = -1 if leg == p-1 else leg
        return 1 + Fraction(leg, p*p)
    if e == 1: return 1 - Fraction(1, p**4)
    return (1 - Fraction(1, p**4)) + Fraction(1, p**3) * alpha_rec(p, N // (p*p))
print("P4 odd-p densities: recursion vs convolution (p=3,5,7, N<=60), both forms")
mism = []; unstable = []
for p in (3,5,7):
    for N in range(1, NMAX+1):
        a, st = alpha_conv(p, N, LOR); ad, std = alpha_conv(p, N, DEF)
        if not (st and std): unstable.append((p,N))
        if a != alpha_rec(p, N) or ad != alpha_rec(p, N): mism.append((p, N, str(a), str(alpha_rec(p,N))))
sc("P4", not mism and not unstable, f"mismatches {mism[:5]}; unstable {unstable[:5]}")

# ---------- Euler product tail and the constancy test ----------
sieve = np.ones(PMAX, dtype=bool); sieve[:2] = False
for i in range(2, int(PMAX**0.5)+1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]; oddp = primes[primes > 2]
def tail(N):
    ps = oddp[N % oddp != 0]; leg = np.array([pow(int(N % p), (int(p)-1)//2, int(p)) for p in ps], dtype=np.int64)
    leg = np.where(leg == ps - 1, -1, leg)
    return float(np.prod(1.0 + leg / ps.astype(float)**2))
def alpha2_stable(N, signs):
    a, st = alpha_conv(2, N, signs); return a, st
ratios = {}; ratios_def = {}; st2 = []
# I5 control: r5(N) by direct count
B = math.isqrt(NMAX); th = np.zeros(NMAX+1, dtype=np.int64)
for x in range(-B, B+1):
    if x*x <= NMAX: th[x*x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:NMAX+1]
for N in range(1, NMAX+1):
    a2, s2 = alpha2_stable(N, LOR); a2d, s2d = alpha2_stable(N, DEF); st2.append(s2 and s2d)
    loc = float(a2); locd = float(a2d)
    for p in (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59):
        if N % p == 0: loc *= float(alpha_rec(p, N)); locd *= float(alpha_rec(p, N))
    tl = tail(N)
    ratios[N] = float(rstar[N]) / (N**1.5 * loc * tl)
    ratios_def[N] = float(r5[N]) / (N**1.5 * locd * tl)
R = np.array([ratios[N] for N in range(1, NMAX+1)]); RD = np.array([ratios_def[N] for N in range(1, NMAX+1)])
print("\n  N   orbits  r*(N)        ratio_lor          ratio_I5")
for N in range(1, NMAX+1):
    print(f"  {N:2d}  {orbits[N]:3d}  {str(rstar[N]):>10s}  {ratios[N]:.9e}  {ratios_def[N]:.7f}")
rel = R.std()/R.mean(); reld = RD.std()/RD.mean()
print(f"\n  Z^(1,4): mean {R.mean():.8e}  sd {R.std():.2e}  rel sd {rel:.2e}   (2-adic stable all N: {all(st2)})")
print(f"  I_5    : mean {RD.mean():.8f}  sd {RD.std():.2e}  rel sd {reld:.2e}")
worst = int(np.argmax(np.abs(R - R.mean()))) + 1
print("P5 KILL — Siegel constancy on Z^(1,4)"); sc("P5", rel < 1e-5 and all(st2), f"rel sd {rel:.2e}; worst N = {worst} ({(R[worst-1]-R.mean())/R.mean():+.2e})")
c_def = 8*math.pi**2/3/2
print("P6 I_5 control"); sc("P6", reld < 1e-5 and abs(RD.mean()/c_def - 1) < 1e-4, f"rel sd {reld:.2e}; mean/13.15947 = {RD.mean()/c_def:.7f}  (mean/26.319 = {RD.mean()/(2*c_def):.7f})")
print("P7 Keeper's constants"); sc("P7", abs(R.mean()/0.0034269 - 1) < 1e-4 and abs(RD.mean()/R.mean()/3840 - 1) < 1e-4,
   f"indef {R.mean():.7e} vs 0.0034269 ({R.mean()/0.0034269:.6f}); def/indef = {RD.mean()/R.mean():.4f}")

# ---------- P8 fundamental-domain sanity ----------
print("P8 greedy reduction of every forward vector, N<=20, x0<=40")
chamber_sets = {N: {tuple(v) for v in chamber_vectors(N)} for N in range(1, 21)}
bad = 0; nonterm = 0; tested = 0
for x0 in range(1, 41):
    for x1 in range(-x0, x0+1):
        for x2 in range(-x0, x0+1):
            rem2 = x0*x0 - x1*x1 - x2*x2
            if rem2 < 1: continue
            for x3 in range(-x0, x0+1):
                rem3 = rem2 - x3*x3
                if rem3 < 1: continue
                for x4 in range(-x0, x0+1):
                    N = rem3 - x4*x4
                    if not (1 <= N <= 20): continue
                    tested += 1; x = np.array([x0,x1,x2,x3,x4], dtype=np.int64); steps = 0
                    while True:
                        neg = [i for i in range(5) if ip(x, roots[i]) < 0]
                        if not neg: break
                        x = S[neg[0]] @ x; steps += 1
                        if steps > 10**4: nonterm += 1; break
                    if steps <= 10**4 and tuple(x) not in chamber_sets[N]: bad += 1
sc("P8", bad == 0 and nonterm == 0, f"{tested} vectors; outside list {bad}; non-terminating {nonterm}")

print(f"\nSCORE {sum(score)}/{len(score)}   [{time.time()-t0:.0f}s]")
json.dump({'rstar': {N: str(rstar[N]) for N in rstar}, 'orbits': orbits, 'ratio_lor': ratios, 'ratio_I5': ratios_def,
           'const_lor': R.mean(), 'const_I5': RD.mean(), 'relsd_lor': rel, 'relsd_I5': reld, 'stab_orders': sorted(stabs_seen),
           'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.siegel_5693.json'), 'w'), indent=1)
