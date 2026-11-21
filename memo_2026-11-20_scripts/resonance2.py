import numpy as np, math
from mpmath import mp, mpf, exp, matrix, lu_solve
mp.dps=80
def dimSO(N,hw):
    m=N//2; l=np.array(hw+[0]*(m-len(hw)),float)
    rho=np.array([m-i-0.5 for i in range(m)]) if N%2 else np.array([m-i-1.0 for i in range(m)])
    L=l+rho; d=1.0
    for i in range(m):
        for j in range(i+1,m): d*=(L[i]**2-L[j]**2)/(rho[i]**2-rho[j]**2)
        if N%2: d*=L[i]/rho[i]
    return d
def spec(n,Nmax,parity):
    out=[]
    for p in range(Nmax):
        for q in range(p+1):
            if parity and (p-q)%2: continue
            out.append((p*(p+n)+q*(q+n-2), dimSO(n+2,[p,q])))
    return out
def Z(t,sp): return sum(D*exp(-mpf(L)*t) for L,D in sp if L*t<200)
def fit(sp,n,ts,K):
    A=matrix([[(mpf(t)/mpf('0.003'))**k for k in range(K+1)] for t in ts]); y=matrix([(4*mp.pi*t)**n*Z(t,sp) for t in ts])
    c=lu_solve(A.T*A,A.T*y); return [c[i]/mpf('0.003')**i for i in range(K+1)]
print("R = 6 a1/a0 versus algebraic 2n^2:")
for n in ():
    for par in (False,True):
        sp=spec(n,200,par); c=fit(sp,n,[mpf(x) for x in np.linspace(0.004,0.02,12)],6)
        print(f"  n={n} {'p=q mod 2' if par else 'all (p,q)'}: R={float(6*c[1]/c[0]):.4f}   (2n^2={2*n*n})")
# resonance test on Q^5 with the spherical set
n=5; sp=spec(n,400,True)
c=fit(sp,n,[mpf(x) for x in np.linspace(0.0015,0.004,12)],7)
def C(t):
    t=mpf(t); smooth=sum(c[k]*t**k for k in range(len(c)))/(4*mp.pi*t)**n
    return Z(t,sp)/smooth-1
a=1/137.035999177
print(f"\nC(alpha^1 = {a:.5f}) = {float(C(a)):.3e}")
for t in (0.02,0.05,0.1,0.15,0.2,0.3,0.5):
    print(f"  C(t={t}) = {float(C(t)):+.3e}")
lo,hi=mpf('0.02'),mpf('0.5')
for _ in range(60):
    mid=(lo+hi)/2
    if abs(C(mid))<3.25e-4: lo=mid
    else: hi=mid
ts=float(lo); print(f"t* where |C| reaches 3.25e-4: {ts:.4f}  -> as a power of alpha: alpha^{math.log(ts)/math.log(a):.3f}")
