# Cal: odd-lattice family — full rational function (numerator AND denominator) of y*c_2(y) for kernels of m squares, m=1..4,
# then the GLOBAL correction relative to the odd-p Gindikin–Karpelevich product, read as: which 2-Euler factors stay uncancelled.
from fractions import Fraction as F
import itertools
K=10; NMAX=30
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
def series(m):
    ps=[prim_frac(j,m) for j in range(K+1)]; pj=[ps[j]-ps[j+1] for j in range(K)]
    assert ps[K]==0, "isotropic kernel; not handled here"
    a={}
    def add(e,c): a[e]=a.get(e,F(0))+c
    add(0,F(1,2**(2*m)))
    for mm in range(-1,NMAX//2+3):
        mu=F(2**(m*mm)*(2**m-1),2**m) if mm>=0 else F(2**m-1,2**(2*m))
        for j in range(K):
            p=pj[j]
            if p==0: continue
            t=j-2*mm-2
            n1 = -t if t<0 else (-1 if t==0 else 0)
            e=max(n1,mm)
            if e<=NMAX: add(e,mu*p)
    return a
def polymul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return r
def fmt(p):
    return " + ".join(f"({c})y^{i}" for i,c in enumerate(p) if c!=0)
for m in (1,2,3,4):
    a=series(m); emin=min(a); s=[a.get(e,F(0)) for e in range(emin,NMAX+1)]   # coefficients of y^emin * (...)
    # find denominator by minimal recurrence (allow numerator degree up to 6)
    best=None
    for L in range(1,8):
        for start in range(0,8):
            rows=[[s[n-i] for i in range(1,L+1)]+[s[n]] for n in range(start+L,start+2*L)]
            A=[r[:] for r in rows]; ok=True
            for c in range(L):
                piv=next((r for r in range(c,L) if A[r][c]!=0),None)
                if piv is None: ok=False;break
                A[c],A[piv]=A[piv],A[c]; A[c]=[v/A[c][c] for v in A[c]]
                for r in range(L):
                    if r!=c and A[r][c]!=0: A[r]=[x-A[r][c]*w for x,w in zip(A[r],A[c])]
            if not ok: continue
            rv=[A[i][L] for i in range(L)]
            if all(s[t]==sum(rv[i-1]*s[t-i] for i in range(1,L+1)) for t in range(start+2*L,len(s))):
                best=(L,start,rv); break
        if best: break
    L,start,rv=best
    D=[F(1)]+[-r for r in rv]
    N=polymul(D,s)[:start+L+1]
    while N and N[-1]==0: N.pop()
    print(f"m={m} (n={m+2}): y^({emin}) * N(y)/D(y) with  N(y) = {fmt(N)}   D(y) = {fmt(D)}")
