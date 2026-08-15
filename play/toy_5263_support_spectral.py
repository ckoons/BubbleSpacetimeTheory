import numpy as np, itertools, sys, time
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
print("="*80)
print("LINEAR ALGEBRA ON D_IV^5 -- the corpus route to dimension AND curvature")
print("="*80)
print("Casey's standing order. BD counts causal-set layers (new import, noisy, no power).")
print("The corpus route reads BOTH off the SPECTRUM of the operator we already credentialed:")
print("   Tr e^{-tau D^2}  ~  (4 pi tau)^{-d/2} * ( a_0 + a_1 tau + ... ),   a_1 prop. to Int R")
print("   => SPECTRAL DIMENSION  d_s(tau) = -2 dlogZ/dlogtau   -- d is an OUTPUT, scanned over tau.")
print("   => and the corpus ALREADY has heat-trace coefficients (a_0=225, a_1=-1875, CLAUDE.md).")
print("   => exact: no sprinkling, no ensemble averaging, no Monte-Carlo noise.")
print()
def d_s(ev,taus):
    ev=ev[ev>1e-9]
    Z=np.array([np.sum(np.exp(-t*ev)) for t in taus])
    lt=np.log(taus); lZ=np.log(Z)
    return -2*np.gradient(lZ,lt), Z
print("VALIDATION FIRST -- synthetic Weyl spectrum with KNOWN d (lambda_k ~ k^{2/d}):")
print("   true d   d_s read back (median over the flat window)")
for dtrue in [2,3,4,5]:
    k=np.arange(1,20001); ev=k**(2.0/dtrue)
    taus=np.logspace(-3,-1,40)
    ds,_=d_s(ev,taus)
    print("     %d       %.3f"%(dtrue,np.median(ds[10:30])))
print()
print("NOW THE REAL OPERATOR -- spec(D^2) of the credentialed v3 + FK metric:")
for N in [2,3,4]:
    t0=time.time()
    Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd)
    D=np.zeros((32*pdim,32*pdim))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    ev=np.linalg.eigvalsh(D@D); ev=ev[ev>1e-9]
    taus=np.logspace(-2.5,-0.5,40)
    ds,Z=d_s(ev,taus)
    print("   N=%d dim=%d  n_nonzero=%d  lam_max=%.1f"%(N,32*pdim,len(ev),ev.max()))
    print("       d_s over tau: "+"  ".join("%.2f"%x for x in ds[::6]))
    print("       median d_s (mid window) = %.3f    [%.0fs]"%(np.median(ds[12:28]),time.time()-t0))
    sys.stdout.flush()
