# Cal's family instrument (E9 by computation): the 2-adic rank-one intertwining integral
#   c_2(sigma) = int_{V0} max(1,|v|,|q0(v)|)^{-sigma} dv,  V0 = Q_2^m, m = n-2, q0 = sum of m squares (anisotropic kernel of D_IV^n),
# against the split control q0' = H^{floor(m/2)} (+ <1> if m odd).  Output: exact power series in y = 2^{-sigma}, its minimal
# recurrence (denominator polynomial), and the pole factors.  Dictionary (validated at m=1 and m=3): sigma = lambda + m/2.
from fractions import Fraction as F
import sys
K=10  # count mod 2^K
def dist_sq(k):
    M=1<<k; d=[0]*M
    for a in range(M): d[(a*a)&(M-1)]+=1
    return d
def dist_prod(k):
    M=1<<k; d=[0]*M
    for a in range(M):
        for b in range(M): d[(a*b)&(M-1)]+=1
    return d
def conv(a,b,M):
    c=[0]*M
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            if y: c[(i+j)&(M-1)]+=x*y
    return c
def zero_count(k,m,split):
    if k==0: return 1
    M=1<<k
    if split:
        d=[0]*M; d[0]=1
        for _ in range(m//2): d=conv(d,dist_prod(k),M)
        if m%2: d=conv(d,dist_sq(k),M)
    else:
        d=[0]*M; d[0]=1
        S=dist_sq(k)
        for _ in range(m): d=conv(d,S,M)
    return d[0]
def prim_frac(j,m,split):
    # P(q0(u) = 0 mod 2^j | u primitive in Z_2^m)
    if j==0: return F(1)
    total=zero_count(j,m,split)
    if j>=2: nonprim=zero_count(j-2,m,split)*(2**m)   # u=2u', u' mod 2^{j-1}: q(u')=0 mod 2^{j-2}; each class mod 2^{j-2} lifts 2^m ways
    else: nonprim=1
    return F(total-nonprim, (2**m-1)*(2**m)**(j-1))
def minrec(seq):
    for L in range(1,len(seq)//2):
        rows=[[seq[n-i] for i in range(1,L+1)]+[seq[n]] for n in range(L,2*L)]
        A=[r[:] for r in rows]; n=L; ok=True
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
NMAX=36
for n in range(3,9):
    m=n-2
    for split in (False,True):
        ps=[prim_frac(j,m,split) for j in range(0,K+1)]
        pj=[ps[j]-ps[j+1] for j in range(K)]  # P(val=j), j<K ; tail P(val>=K)=ps[K]
        tail=ps[K]
        # power series coefficients a_e of y^e, e=0..NMAX
        a=[F(0)]*(NMAX+1); a[0]=F(1)
        for mm in range(1,NMAX+1):
            mu=F(2**(m*mm)*(2**m-1),2**m)
            for j in range(K):
                if pj[j]==0: continue
                e=max(mm,2*mm-j)
                if e<=NMAX: a[e]+=mu*pj[j]
            # tail: val>=K (only split kernels have it); assume geometric ratio 1/2 beyond K (observed); contributes e=max(mm,2mm-j), j>=K
            if tail:
                j=K
                while True:
                    pt=tail*F(1,2)**(j-K)*F(1,2)   # P(val=j) ~ tail*(1/2)^{j-K+1}
                    e=max(mm,2*mm-j)
                    if e>NMAX and j>2*mm: break
                    if e<=NMAX: a[e]+=mu*pt
                    j+=1
                    if j>2*mm+40: break
        L,rv=minrec(a)
        kind="ANISO(sum of %d squares)"%m if not split else "SPLIT control"
        print(f"n={n} m={m} {kind}: valuation support P(val>=j)={[str(x) for x in ps[:6]]}{'...' if tail else ''}")
        if rv is None: print("   no recurrence found within order",NMAX//2-1); continue
        print(f"   recurrence order {L}; denominator D(y) = 1" + "".join(f" - ({r})y^{i+1}" for i,r in enumerate(rv)))
        # roots of D in y, then in lambda: y = 2^{-sigma} = 2^{-lambda-m/2}
        import numpy as np
        coeffs=[1.0]+[-float(r) for r in rv]
        roots=np.roots(coeffs[::-1]) if False else np.roots(coeffs)  # numpy wants highest degree first: coeffs are in increasing powers -> reverse
        roots=np.roots(coeffs[::-1])
        for rt in roots:
            # pole where y = rt : 2^{-lambda-m/2} = rt  -> lambda = -m/2 - log2(rt)
            import cmath
            lam=-m/2-cmath.log(rt)/cmath.log(2)
            print(f"     pole y={rt:.5f} -> lambda = {lam.real:+.4f} {lam.imag:+.4f}i (mod 2*pi/ln2 = 9.0647 in Im)")
