# Siegel exactness check: definite I_5 (control) vs indefinite I_{1,4} (BST cone), one-class genera.
# Test: r(N) / ( N^{3/2} * prod_p alpha_p(N) ) CONSTANT in N  <=> genus theta has no cuspidal part.
import numpy as np, math
from fractions import Fraction
NMAX = 40
def primes(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR = primes(100000)
def legendre_vec(N, ps):
    out = np.ones(len(ps))
    for j,p in enumerate(ps):
        p = int(p); a = N % p
        if a == 0: out[j] = 0
        elif pow(a,(p-1)//2,p) != 1: out[j] = -1
    return out
def density(N, p, k, signs):
    q = p**k
    sq = np.zeros(q, dtype=np.int64)
    xs = np.arange(q, dtype=np.int64); np.add.at(sq, (xs*xs)%q, 1)
    negsq = np.roll(sq[::-1], 1)  # negsq[v] = sq[-v mod q]
    dist = np.zeros(q, dtype=np.int64); dist[0]=1
    for s in signs:
        vec = sq if s>0 else negsq
        full = np.convolve(dist, vec)           # length 2q-1
        dist = full[:q].copy(); dist[:q-1] += full[q:]   # fold mod q
    return Fraction(int(dist[N%q]), q**4)
def local_product(N, signs):
    prod = 1.0
    k = ((N & -N).bit_length()-1) + 3
    d2a, d2b = density(N,2,k,signs), density(N,2,k+1,signs)
    assert d2a == d2b, ("2-adic not stable", N, d2a, d2b)
    prod *= float(d2a)
    odd = [p for p in PR[1:] if N % p == 0]
    for p in odd:
        e = 0; m = N
        while m % p == 0: m//=p; e+=1
        da, db = density(N,p,e+1,signs), density(N,p,e+2,signs)
        assert da == db, ("p-adic not stable", N, p)
        prod *= float(da)
    coprime = np.array([p for p in PR[1:] if N % p != 0], dtype=float)
    prod *= float(np.prod(1 + legendre_vec(N, coprime.astype(int))/coprime**2))
    return prod
# definite r_5
th = np.zeros(NMAX+1, dtype=np.int64)
for x in range(-7,8):
    if x*x <= NMAX: th[x*x] += 1
r5 = np.zeros(NMAX+1, dtype=np.int64); r5[0]=1
for _ in range(5): r5 = np.convolve(r5, th)[:NMAX+1]
# indefinite chamber enumeration
B = np.diag([1,-1,-1,-1,-1])
roots = [np.array(v) for v in [[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1],[0,0,0,0,1],[1,1,1,1,0]]]
def refl_exact(r):
    rr = int(r@B@r); M = np.zeros((5,5),dtype=object)
    for j in range(5):
        e = np.zeros(5,dtype=int); e[j]=1
        M[:,j] = e - Fraction(2*int(e@B@r), rr)*r
    return M
gens = [refl_exact(r) for r in roots]
cache = {}
def group_order(idx):
    key = tuple(idx)
    if key in cache: return cache[key]
    if not idx: return 1
    key2 = lambda M: tuple(tuple(int(v) for v in row) for row in M)
    seen = {key2(np.eye(5,dtype=object))}; frontier=[np.eye(5,dtype=object)]
    while frontier:
        nxt=[]
        for M in frontier:
            for i in idx:
                P = gens[i]@M; t = key2(P)
                if t not in seen:
                    seen.add(t); nxt.append(P)
                    if len(seen) > 5000: raise RuntimeError("infinite subgroup for "+str(idx))
        frontier = nxt
    cache[key]=len(seen); return len(seen)
rstar = {N: Fraction(0) for N in range(1,NMAX+1)}; orbits = {N:0 for N in range(1,NMAX+1)}
for x1 in range(0, NMAX+1):
  for x2 in range(0, x1+1):
    for x3 in range(0, x2+1):
      for x4 in range(0, x3+1):
        s = x1*x1+x2*x2+x3*x3+x4*x4
        for x0 in range(max(x1+x2+x3, math.isqrt(s)), math.isqrt(s+NMAX)+2):
            N = x0*x0 - s
            if 1 <= N <= NMAX:
                x = np.array([x0,x1,x2,x3,x4])
                idx = [i for i,r in enumerate(roots) if int(x@B@r)==0]
                rstar[N] += Fraction(1, group_order(idx)); orbits[N]+=1
print("stabilizer orders seen:", {k:v for k,v in cache.items()})
print(" N  r5(N)  r5/(N^1.5 P5)   | orb   r*(N)        r*/(N^1.5 P14)")
rd_l=[]; ri_l=[]
for N in range(1, NMAX+1):
    pd = local_product(N, [1,1,1,1,1]); pi = local_product(N, [1,-1,-1,-1,-1])
    rd = float(r5[N])/(N**1.5*pd); ri = float(rstar[N])/(N**1.5*pi)
    rd_l.append(rd); ri_l.append(ri)
    print(f"{N:2d} {int(r5[N]):6d}  {rd:10.5f}   | {orbits[N]:3d}  {str(rstar[N]):>10s}  {ri:12.7f}")
print("definite   ratio mean %.5f sd %.2e  (8pi^2/3 = %.5f, expected exact)" % (np.mean(rd_l), np.std(rd_l), 8*math.pi**2/3))
print("indefinite ratio mean %.7f sd %.2e rel %.2e" % (np.mean(ri_l), np.std(ri_l), np.std(ri_l)/np.mean(ri_l)))
