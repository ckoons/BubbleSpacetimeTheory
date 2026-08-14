import numpy as np, itertools, sys, time, collections
from fractions import Fraction as F
exec(open('/private/tmp/claude-501/-Users-cskoons-projects-github/4ea94fa6-b3fe-41e8-9a52-1a6c7015cf19/scratchpad/shape2.py').read().split('def run(')[0])
def profile(N,nu=F(5,2)):
    t0=time.time(); Kt,Pt,pd,_=polyops(N,nu); a=fermions()
    q=np.array([bin(i).count('1') for i in range(32)])
    lab=[(int(q[f]),int(pd[p])) for f in range(32) for p in range(len(pd))]
    tot=np.array([x-y for x,y in lab]); n=len(lab)
    D=np.zeros((n,n))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    H=D@D
    prof=collections.Counter(); tot_ker=0
    for c in sorted(set(tot.tolist())):
        sel=np.nonzero(tot==c)[0]
        w,v=np.linalg.eigh(H[np.ix_(sel,sel)])
        for i in range(len(w)):
            if abs(w[i])<1e-9:
                tot_ker+=1
                prof[lab[sel[int(np.argmax(np.abs(v[:,i])))]]]+=1
    byd=collections.Counter()
    for (qq,dd),c in prof.items(): byd[dd]+=c
    print(f"N={N}: kernel={tot_ker}  by poly-degree d: {dict(sorted(byd.items()))}  [{time.time()-t0:.0f}s]")
    for w in range(0,N+1):
        k=sum(c for (qq,dd),c in prof.items() if dd<=w)
        print(f"        window d<={w}: kernel={k}"+("   <-- BARE VACUUM ONLY" if k==1 else ""))
    sys.stdout.flush()
    return byd
print("=== v3 interior-window analysis (does the kernel reduce to the bare vacuum?) ===")
for N in [2,3,4]: profile(N)
