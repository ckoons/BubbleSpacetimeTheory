# R18 retained instrument: (a) PSS 2301.04146 eq.(5.39) truncated SO(1,4) Casimir on SO(4)-singlets of R_Delta (d=3);
# (b) LPSS 2306.00090 eq.(5.47) KL density at Delta=5/2+k vs closed form (derived here).
import numpy as np, mpmath as mp
from scipy.linalg import eigh_tridiagonal
d=3
def Qmin(D,N=4000):
    n=np.arange(N+1,dtype=float)
    diag=2*n*(n+D)+0.5*(d+1)*D
    m=n[:-1]
    off=np.sqrt((m+1)*(m+D)*(m+(d+1)/2)*(m+D-(d-1)/2))
    w=eigh_tridiagonal(diag,off,eigvals_only=True,select='i',select_range=(0,2))
    return w
print("d^2/4 =",d*d/4)
for D in [1.2,1.4,1.5,2.0,2.5,3.5,4.5,5.5]:
    w=Qmin(D); print(f"Delta={D}: lowest 3 eigs (N=4000) = {np.round(w,4)} ; naive Delta(3-Delta)={D*(3-D):.3f}")
def rho(D,lam,cO=1):
    return cO*2**(1+d-2*D)*mp.pi**((d-1)/2)*mp.gamma(-d/2+D+1j*lam)*mp.gamma(-d/2+D-1j*lam)/(mp.gamma(D)*mp.gamma((1-d)/2+D))*lam*mp.sinh(mp.pi*lam)
def closed(k,lam):
    D=mp.mpf(5)/2+k
    P=mp.fprod([j*j+lam*lam for j in range(1,k+1)]) if k>0 else 1
    return 2**(-1-2*k)*mp.pi**2*lam**2*P/(mp.gamma(D)*mp.gamma(D-1))
for k in range(4):
    for lam in [0.3,1.7,6.0]:
        a=rho(mp.mpf(5)/2+k,lam); b=closed(k,lam)
        print(f"k={k} lam={lam}: rho(5.47)={mp.nstr(mp.re(a),12)} closed={mp.nstr(b,12)} relerr={mp.nstr(abs(a-b)/b,3)}")
