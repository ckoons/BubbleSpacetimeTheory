import numpy as np, sys
from fractions import Fraction as F
from math import comb
exec(open('shape2.py').read().split('def run(')[0])
print("DIRECT CHECK -- counting exponent fitted on the ACTUAL cumulative spectrum")
print("   (interior band only: drop the bottom 10% and the top 35%, where truncation bites)")
print()
print("   Nt   modes   counting exponent d/2    => d")
for Nt in [2,3,4]:
    Kt,Pt,pdg,_=polyops(Nt,F(5,2)); a=fermions(); pdim=len(pdg)
    Dm=np.zeros((32*pdim,32*pdim))
    for m in range(5): Dm+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    ev=np.sort(np.linalg.eigvalsh(Dm@Dm)); ev=ev[ev>1e-9]
    lo,hi=np.percentile(ev,10),np.percentile(ev,65)
    sel=(ev>=lo)&(ev<=hi); L=ev[sel]; Nl=np.arange(1,len(ev)+1)[sel]
    sl=np.polyfit(np.log(L),np.log(Nl),1)[0]
    print("   %d    %5d   %.3f                   %.2f"%(Nt,len(ev),sl,2*sl))
    sys.stdout.flush()
print()
print("ANALYTIC (exact, no diagonalization, arbitrary lam_max):")
print("   lam_max(N) = 2N^2 + 9N + 14   [EXACT: 40, 59, 82 at N=2,3,4]")
print("   modes(N)   = 32*C(N+5,5)      [EXACT: 672, 1792, 4032]")
print()
print("   Nt      lam_max      modes        d from (log modes)/(log lam) slope")
prev=None
for Nt in [2,4,8,16,32,64,128,256]:
    lm=2*Nt**2+9*Nt+14; md=32*comb(Nt+5,5)
    if prev:
        d=2*(np.log(md/prev[1])/np.log(lm/prev[0]))
        print("   %3d   %10d   %12d        %.4f"%(Nt,lm,md,d))
    else:
        print("   %3d   %10d   %12d        --"%(Nt,lm,md))
    prev=(lm,md)
print()
print("   => the analytic exponent converges to d = 5 from above. NOT 6.")
print("   ** Keeper's pre-registered expectation was 6 (K1530). This route gives 5. Reported as measured. **")
print("   ** and 5 AGREES with the causal-order answer (F989/Grace, R x S^4) and my own 5252. **")
