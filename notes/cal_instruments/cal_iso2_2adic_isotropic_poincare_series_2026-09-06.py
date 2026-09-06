# Cal's blind instrument: 2-adic counts of isotropic vectors for the rank-one cone of SO(H + q0), q0 anisotropic vs split control.
# N_k(Q) = #{x mod 2^k : Q(x) = 0 mod 2^k}. Q_aniso = x1 x2 + x3^2 + x4^2 + x5^2 ; Q_split = x1 x2 + x3 x4 + x5^2.
# Then P(t) = sum_k N_k 2^{-5k} t^k is rational (Igusa); find the minimal linear recurrence and its denominator.
from fractions import Fraction as F
import sys
def dist_prod(k):
    m=1<<k; d=[0]*m
    for a in range(m):
        for b in range(m): d[(a*b)&(m-1)]+=1
    return d
def dist_sq(k):
    m=1<<k; d=[0]*m
    for a in range(m): d[(a*a)&(m-1)]+=1
    return d
def conv(a,b,m):
    c=[0]*m
    for i,x in enumerate(a):
        if x==0: continue
        for j,y in enumerate(b):
            if y: c[(i+j)&(m-1)]+=x*y
    return c
def counts(k):
    m=1<<k
    P=dist_prod(k); S=dist_sq(k)
    an=conv(conv(conv(P,S,m),S,m),S,m)[0]
    sp=conv(conv(P,P,m),S,m)[0]
    return an,sp
KMAX=int(sys.argv[1]) if len(sys.argv)>1 else 8
Na=[1];Ns=[1]
for k in range(1,KMAX+1):
    a,s=counts(k); Na.append(a); Ns.append(s)
    print(f"k={k}: N_aniso={a}  N_split={s}  dens_aniso={F(a,2**(4*k))}  dens_split={F(s,2**(4*k))}", flush=True)
# minimal recurrence of c_k = N_k / 2^{5k}
def minrec(seq):
    for L in range(1,len(seq)//2+1):
        # solve seq[n] = sum_{i=1..L} r_i seq[n-i] for n=L..2L-1, then test the rest
        import itertools
        rows=[[seq[n-i] for i in range(1,L+1)] for n in range(L,2*L)]
        rhs=[seq[n] for n in range(L,2*L)]
        # gaussian elimination in Fractions
        A=[r[:]+[v] for r,v in zip(rows,rhs)]
        n=L; ok=True
        for c in range(n):
            piv=next((r for r in range(c,n) if A[r][c]!=0),None)
            if piv is None: ok=False;break
            A[c],A[piv]=A[piv],A[c]
            A[c]=[v/A[c][c] for v in A[c]]
            for r in range(n):
                if r!=c and A[r][c]!=0:
                    A[r]=[x-A[r][c]*y for x,y in zip(A[r],A[c])]
        if not ok: continue
        rvec=[A[i][n] for i in range(n)]
        good=all(seq[m]==sum(rvec[i-1]*seq[m-i] for i in range(1,L+1)) for m in range(2*L,len(seq)))
        if good and len(seq)>2*L: return L,rvec
    return None,None
for name,N in (("aniso",Na),("split",Ns)):
    c=[F(N[k],2**(5*k)) for k in range(len(N))]
    L,r=minrec(c)
    print(name,"recurrence order",L,"coeffs",r)
    if r:
        # denominator polynomial 1 - r1 t - r2 t^2 ...
        print("  denominator D(t) = 1 - " + " - ".join(f"({ri})t^{i+1}" for i,ri in enumerate(r)))
