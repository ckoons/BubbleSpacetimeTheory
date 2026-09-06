# Pre-registered (K1862 G): d_N^2 = dist^2(chi, span{ {x/k} : k<=N }) in L^2((0,inf), dx/x^2), N<=60,
# exact piecewise integration up to X, tail = (1/X)(1/4 + gcd^2/(12km)) [Franel mean], b tail = 1/(2X).
import numpy as np, math, sys
X = 200000
N = 60
def gram(k, m):
    # pieces between consecutive breakpoints of multiples of k and m in (0, X]
    bp = np.unique(np.concatenate([np.arange(0, X+1, k), np.arange(0, X+1, m), [X]])).astype(float)
    lo, hi = bp[:-1], bp[1:]
    mid = 0.5*(lo+hi)
    a = np.floor(mid/k); b = np.floor(mid/m)
    # integrand (x/k - a)(x/m - b)/x^2 = 1/(km) - (a/m + b/k)/x + ab/x^2
    with np.errstate(divide='ignore'):
        L = np.log(hi/np.where(lo==0, np.nan, lo)); L = np.nan_to_num(L)
        inv = np.where(lo==0, 0.0, 1/lo) - 1/hi
    val = (hi-lo)/(k*m) - (a/m + b/k)*L + a*b*inv
    g = math.gcd(k, m)
    return val.sum() + (0.25 + g*g/(12*k*m))/X
def bvec(k):
    bp = np.unique(np.concatenate([np.arange(k, X+1, k), [1.0, X]])).astype(float)
    bp = bp[bp>=1]
    lo, hi = bp[:-1], bp[1:]
    a = np.floor(0.5*(lo+hi)/k)
    val = (1/k)*np.log(hi/lo) - a*(1/lo - 1/hi)
    return val.sum() + 0.5/X
G = np.zeros((N,N)); b = np.zeros(N)
for k in range(1,N+1):
    b[k-1] = bvec(k)
    for m in range(k,N+1):
        G[k-1,m-1] = G[m-1,k-1] = gram(k,m)
print("check ||r1||^2 = %.6f (log2pi-gamma = %.6f); <chi,r1> = %.6f (1-gamma = %.6f)" % (G[0,0], math.log(2*math.pi)-0.5772156649, b[0], 1-0.5772156649))
d2 = []
for n in range(1,N+1):
    Gn = G[:n,:n]; bn = b[:n]
    # solve in float128-ish via lstsq for conditioning
    c = np.linalg.lstsq(Gn, bn, rcond=None)[0]
    d2.append(1 - bn@c)
d2 = np.array(d2)
def omega(k):
    return len({p for p in range(2,k+1) if k%p==0 and all(p%q for q in range(2,int(p**0.5)+1))})
print(" k   d_k^2      Delta_k      type")
for k in range(1,N+1):
    dk = d2[k-2]-d2[k-1] if k>1 else float('nan')
    t = "1" if k==1 else ("prime" if omega(k)==1 and all(k%q for q in range(2,int(k**0.5)+1)) else ("prime-power" if omega(k)==1 else "composite(>=2 primes)"))
    print(f"{k:2d}  {d2[k-1]:.6f}  {dk: .3e}   {t}")
C = 2+0.5772156649-math.log(4*math.pi)
print("P3: d_N^2 * log N at N=60 = %.4f  vs C = %.4f  (ratio %.2f)" % (d2[-1]*math.log(60), C, d2[-1]*math.log(60)/C))
# P1: for composite k with >=2 distinct primes, Delta_k < 5% of Delta_p for nearest prime p<k
def isprime(n): return n>1 and all(n%q for q in range(2,int(n**0.5)+1))
fails=[]
for k in range(2,N+1):
    if omega(k)>=2:
        p = max(q for q in range(2,k) if isprime(q))
        Dk = d2[k-2]-d2[k-1]; Dp = d2[p-2]-d2[p-1]
        if not (Dk < 0.05*Dp): fails.append((k,Dk,p,Dp))
print("P1 fails:", fails if fails else "none")
print("P2 prime powers:", [(k, d2[k-2]-d2[k-1]) for k in range(2,N+1) if omega(k)==1 and not isprime(k)])
