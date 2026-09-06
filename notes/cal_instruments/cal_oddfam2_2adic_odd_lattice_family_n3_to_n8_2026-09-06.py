# Cal: odd-lattice (corpus-type <1,-1> + I_m) 2-adic rank-one intertwining integral for kernels q0 = sum of m squares, m = n-2, n = 3..8.
# Norm rule (derived §855): shells |v| = 2^mm (mm in Z), j = val q0(u) on primitive u; t := j - 2mm - 2 = val(q0(v)/4):
#   t < 0 -> |1 +- q0/4| = 2^{-t}; t = 0 -> max|1 +- q0/4| = 1/2; t > 0 -> 1.  norm = max(that, 2^mm).
# Exact series in y = 2^{-sigma} (times y to clear the y^{-1} from the mm=-1, j=0 shell), minimal recurrence -> denominator.
from fractions import Fraction as F
import numpy as np, cmath
K=10; NMAX=40
def dist_sq(k):
    M=1<<k; d=[0]*M
    for a in range(M): d[(a*a)&(M-1)]+=1
    return d
def conv(a,b,M):
    c=[0]*M
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            if y: c[(i+j)&(M-1)]+=x*y
    return c
def zero_count(k,m):
    if k==0: return 1
    M=1<<k; d=[0]*M; d[0]=1; S=dist_sq(k)
    for _ in range(m): d=conv(d,S,M)
    return d[0]
def prim_frac(j,m):
    if j==0: return F(1)
    total=zero_count(j,m); nonprim=zero_count(j-2,m)*(2**m) if j>=2 else 1
    return F(total-nonprim,(2**m-1)*(2**m)**(j-1))
def minrec(seq):
    for L in range(1,len(seq)//2):
        A=[[seq[n-i] for i in range(1,L+1)]+[seq[n]] for n in range(L,2*L)]; n=L; ok=True
        for c in range(n):
            piv=next((r for r in range(c,n) if A[r][c]!=0),None)
            if piv is None: ok=False;break
            A[c],A[piv]=A[piv],A[c]; A[c]=[v/A[c][c] for v in A[c]]
            for r in range(n):
                if r!=c and A[r][c]!=0: A[r]=[x-A[r][c]*w for x,w in zip(A[r],A[c])]
        if not ok: continue
        rv=[A[i][n] for i in range(n)]
        if all(seq[t]==sum(rv[i-1]*seq[t-i] for i in range(1,L+1)) for t in range(2*L,len(seq))): return L,rv
    return None,None
for n in range(3,9):
    m=n-2
    ps=[prim_frac(j,m) for j in range(K+1)]
    pj=[ps[j]-ps[j+1] for j in range(K)]; tail=ps[K]
    def pval(j):  # P(val = j) with geometric tail (ratio 1/2 beyond K, observed for isotropic kernels; zero for anisotropic)
        if j<K: return pj[j]
        return tail*F(1,2)**(j-K+1)
    a={}  # exponent e -> coefficient, norm = 2^e
    def add(e,c): a[e]=a.get(e,F(0))+c
    # mm <= -2: norm 1, measure of 4 Z_2^m = 2^{-2m}
    add(0,F(1,2**(2*m)))
    for mm in range(-1,NMAX//2+2):
        mu=F(2**(m*mm)*(2**m-1),2**m) if mm>=0 else F(2**m-1,2**(2*m))  # measure of shell |v|=2^mm
        for j in range(0,2*mm+40):
            p=pval(j)
            if p==0: continue
            t=j-2*mm-2
            if t<0: n1=-t
            elif t==0: n1=-1
            else: n1=0
            e=max(n1,mm)
            if e<=NMAX: add(e,mu*p)
    emin=min(a); seq=[a.get(e,F(0)) for e in range(emin,NMAX+1)]
    L,rv=minrec(seq)
    print(f"n={n} m={m} odd lattice <1,-1>+I_{m}: P(val>=j)={[str(x) for x in ps[:5]]}{'...' if tail else ''}; series starts at y^{emin}")
    if rv is None: print("   no recurrence"); continue
    print("   denominator D(y) = 1"+"".join(f" - ({r})y^{i+1}" for i,r in enumerate(rv)))
    roots=np.roots([1.0]+[-float(r) for r in rv][::-1][::-1]) if False else np.roots(([1.0]+[-float(r) for r in rv])[::-1])
    for rt in roots:
        lam=-m/2-cmath.log(rt)/cmath.log(2)
        print(f"     pole y={rt:.5f} -> lambda = {lam.real:+.4f} {lam.imag:+.4f}i")
