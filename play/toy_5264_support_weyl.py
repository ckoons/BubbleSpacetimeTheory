import numpy as np, itertools, collections, sys, time
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
print("="*80)
print("STEP 1 -- the EXACT eigenvalue->multiplicity table of D^2 (no fitting, just read it)")
print("="*80)
tabs={}
for N in [2,3,4]:
    Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd)
    D=np.zeros((32*pdim,32*pdim))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    ev=np.linalg.eigvalsh(D@D)
    c=collections.Counter(np.round(ev,6))
    tabs[N]=c
    items=sorted(c.items())
    print("  N=%d dim=%d  distinct eigenvalues=%d"%(N,32*pdim,len(items)))
    print("     "+"  ".join("%g:%d"%(k,v) for k,v in items[:14]))
    sys.stdout.flush()
print()
print("="*80)
print("STEP 2 -- which multiplicities are CONVERGED (stable as N grows) vs truncation-affected?")
print("="*80)
allv=sorted(set(list(tabs[2].keys())+list(tabs[3].keys())+list(tabs[4].keys())))
print("   lambda      m(N=2)   m(N=3)   m(N=4)    stable 3->4 ?")
for v in allv[:20]:
    m2,m3,m4=tabs[2].get(v,0),tabs[3].get(v,0),tabs[4].get(v,0)
    print("   %8g   %6d   %6d   %6d    %s"%(v,m2,m3,m4,"YES" if m3==m4 and m3>0 else ""))
