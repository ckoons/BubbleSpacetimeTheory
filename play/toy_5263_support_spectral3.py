import numpy as np, sys, time, itertools
from fractions import Fraction as F
def d_s_curve(ev,taus):
    ev=ev[ev>1e-9]; Z=np.array([np.sum(np.exp(-t*ev)) for t in taus])
    return -2*np.gradient(np.log(Z),np.log(taus)),Z
print("MY ESTIMATOR'S WINDOW WAS AT THE SPECTRUM'S EDGE, NOT IN THE ASYMPTOTIC REGIME.")
print("  power law Tr e^{-tau L} ~ tau^{-d/2} needs:  tau*lam_max >> 1  (truncation exponentially dead)")
print("                                          AND  tau*lam_min << 1  (many modes contribute).")
print("  I had used tau ~ 1/lam_max -- exactly the edge. Corrected window below.")
print()
print("RE-VALIDATION with the corrected window:")
print("   true d    modes      d_s read     bias")
for dtrue in [2,3,4,5]:
    M=300000; k=np.arange(1,M+1); ev=(k**(2.0/dtrue)).astype(float)
    taus=np.logspace(np.log10(8.0/ev.max()),np.log10(0.05/ev.min()),60)
    ds,_=d_s_curve(ev,taus)
    read=np.median(ds[20:45])
    print("     %d      %7d     %7.3f    %+.3f"%(dtrue,M,read,read-dtrue))
print()
print("REAL OPERATOR, corrected window -- spec(D^2), credentialed v3 + FK metric:")
exec(open('shape2.py').read().split('def run(')[0])
for N in [2,3,4]:
    t0=time.time()
    Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd)
    D=np.zeros((32*pdim,32*pdim))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    ev=np.linalg.eigvalsh(D@D); ev=ev[ev>1e-9]
    taus=np.logspace(np.log10(8.0/ev.max()),np.log10(0.05/ev.min()),60)
    ds,_=d_s_curve(ev,taus)
    print("   N=%d  modes=%4d  lam in [%.1f, %.1f]  span=%.0f   d_s = %.3f   [%.0fs]"%(
        N,len(ev),ev.min(),ev.max(),ev.max()/ev.min(),np.median(ds[20:45]),time.time()-t0))
    sys.stdout.flush()
print()
print("  NOTE the span column: the real operator spans only ~20x. The synthetic controls needed")
print("  >>100x to read d>=4 at all. So the real read is span-limited regardless of the window fix.")
