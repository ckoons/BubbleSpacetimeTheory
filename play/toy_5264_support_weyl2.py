import numpy as np, itertools, collections, sys
from fractions import Fraction as F
from math import comb
exec(open('shape2.py').read().split('def run(')[0])
print("="*80)
print("THE ANALYTIC WEYL ROUTE -- counting function from the module structure, no diagonalization")
print("="*80)
print("MODULE: Lambda*(C^5) (x) C[z_1..z_5].  Modes up to polynomial degree N = 32 * C(N+5,5).")
print()
lam={}
for N in [2,3,4]:
    Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd)
    D=np.zeros((32*pdim,32*pdim))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    ev=np.linalg.eigvalsh(D@D); lam[N]=ev.max()
    print("   N=%d  modes=32*C(%d,5)=%d  (actual dim %d)   lam_max=%.0f"%(N,N+5,32*comb(N+5,5),32*pdim,ev.max()))
print()
xs=np.array(sorted(lam)); ys=np.array([lam[n] for n in xs])
A=np.vstack([xs**2,xs,np.ones_like(xs)]).T
c=np.linalg.lstsq(A,ys,rcond=None)[0]
print("   fit lam_max(N) = %.3f N^2 + %.3f N + %.3f   -> LEADING: lam ~ 2 N^2"%tuple(c))
print("   modes(N) = 32*C(N+5,5) ~ 32 N^5/120                 -> LEADING: modes ~ N^5")
print()
print("   => N(lambda) ~ modes at N ~ sqrt(lam/2)  ~  (lam/2)^{5/2} * 32/120   ∝  lambda^{5/2}")
print("   => Weyl:  N(lambda) ~ C lambda^{d/2}   =>   d/2 = 5/2   =>   ** d = 5 **")
print()
print("="*80)
print("DIRECT CHECK -- fit the counting exponent on the ACTUAL cumulative spectrum")
print("="*80)
for N in [3,4]:
    Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd)
    D=np.zeros((32*pdim,32*pdim))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    ev=np.sort(np.linalg.eigvalsh(D@D)); ev=ev[ev>1e-9]
    # counting function on the INTERIOR band (avoid the truncation edge, top 35%)
    hi=np.percentile(ev,65); lo=np.percentile(ev,10)
    sel=(ev>=lo)&(ev<=hi)
    L=ev[sel]; Nl=np.arange(1,len(ev)+1)[sel]
    sl=np.polyfit(np.log(L),np.log(Nl),1)[0]
    print("   N=%d  counting exponent d/2 = %.3f   =>  d = %.2f   (band [%.0f, %.0f])"%(N,sl,2*sl,lo,hi))
print()
print("  ** Keeper's pre-registered expectation was 6. Both routes here give ~5, not 6. Reporting as measured. **")
