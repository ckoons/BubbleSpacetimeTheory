"""TOY 5702 — Liouville summatory L(x) = sum_{n<=x} lambda(n), lambda = (-1)^Omega(n). Round 120 L4 control.
Lyra 2026-09-06. RH <=> L(x) = O(x^{1/2+eps}) (Landau 1899; Titchmarsh 14.25). Polya's conjecture
L(x) <= 0 for x >= 2: existence of counterexamples Haselgrove 1958; Lehman 1960 gave 906,180,359;
the smallest is 906,150,257 (Tanaka 1980). Memory-safe: parity sieve in uint8, chunked cumsum.
Verdicts computed from the run's own values.
"""
import numpy as np, sys, time
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**8
t0 = time.time()
# primes to X by numpy sieve
sieve = np.ones(X+1, dtype=bool); sieve[:2] = False
for i in range(2, int(X**0.5)+1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.flatnonzero(sieve); del sieve
print("primes to %d: %d [%.0f s]" % (X, primes.size, time.time()-t0), flush=True)
par = np.zeros(X+1, dtype=np.uint8)
for p in primes.tolist():
    pk = p
    while pk <= X:
        par[pk::pk] ^= 1
        pk *= p
del primes
print("parity sieve done [%.0f s]" % (time.time()-t0), flush=True)
# chunked cumsum of lambda = 1 - 2*par
B = 10**8; total = 0; Lmin = (0, 0); Lmax = (-10**9, 0); first_pos = None; rmin = 0.0; rmax = -1.0
checks = {}
want = [10**6, 10**7, 10**8, 906150256, 906150257, 906180359]
for start in range(1, X+1, B):
    end = min(X, start+B-1)
    lam = 1 - 2*par[start:end+1].astype(np.int32)
    L = np.cumsum(lam, dtype=np.int64) + total
    total = int(L[-1])
    xs = np.arange(start, end+1, dtype=np.float64)
    r = L/np.sqrt(xs)
    lo = 1 if start == 1 else 0   # skip x = 1
    if L[lo:].min() < Lmin[0]: Lmin = (int(L[lo:].min()), start+lo+int(np.argmin(L[lo:])))
    if L[lo:].max() > Lmax[0]: Lmax = (int(L[lo:].max()), start+lo+int(np.argmax(L[lo:])))
    rmin = min(rmin, float(r[lo:].min())); rmax = max(rmax, float(r[lo:].max()))
    if first_pos is None:
        pos = np.flatnonzero(L[lo:] > 0)
        if pos.size: first_pos = start+lo+int(pos[0])
    for w in want:
        if start <= w <= end: checks[w] = int(L[w-start])
print("toy 5702: L(x) to X = %d  [%.0f s]" % (X, time.time()-t0))
print("  min L = %d at x = %d;  max L (x>=2) = %d at x = %d" % (Lmin[0], Lmin[1], Lmax[0], Lmax[1]))
print("  first x >= 2 with L(x) > 0: %s" % first_pos)
print("  L(x)/sqrt(x) on [2,X]: min %.4f, max %.4f" % (rmin, rmax))
for w in want:
    if w in checks: print("  L(%d) = %d" % (w, checks[w]))
if X >= 906150257:
    ok = checks.get(906150257) == 1 and first_pos == 906150257
    print("  CONTROL Tanaka 1980: L(906150257) = +1 and L(x) <= 0 on [2, 906150256]: %s" % ("HIT" if ok else "MISS"))
else:
    print("  CONTROL (partial, X < 906150257): L(x) <= 0 on [2, X]: %s" % ("HIT" if first_pos is None else "MISS"))
