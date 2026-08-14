import numpy as np, itertools, sys, time, collections
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
print("="*78)
print("PRE-REGISTERED, before computing (informs Lyra #120 from the operator side)")
print("="*78)
print("  Keeper's fork: does H^2(D_IV^5) supply an infinite-volume limit (SSB hatch open),")
print("  or is BST finite (no true SSB -> tunneling restores symmetry -> floor FINAL)?")
print()
print("  STANDARD DIAGNOSTIC: in a system heading for SSB, the gap between the symmetric ground")
print("  state and the first excited state CLOSES (exponentially) as the system grows -- that is the")
print("  vanishing tunneling amplitude. If the gap stays FINITE, no degenerate vacua form.")
print()
print("  H1  gap -> 0 as N grows          => H^2 could supply the limit; SSB hatch OPEN")
print("  H0  gap stays finite / grows     => no degenerate vacua; consistent with floor FINAL")
print()
print("  ** CAVEAT, stated up front: N is a MODE cutoff (polynomial degree), not a spatial VOLUME.")
print("     SSB proper needs infinite volume. But N -> inf IS the full H^2, which is exactly")
print("     Keeper's counter-argument, so this addresses that fork directly and nothing wider. **")
print()
print("MEASURED -- interior window (d <= N-1, toy 5244) so truncation debris is excluded:")
print("   N    dim     tau_min   first excited above it   GAP")
for N in [2,3,4]:
    t0=time.time()
    Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd); n=32*pdim
    D=np.zeros((n,n))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    H=D@D
    q=np.array([bin(i).count('1') for i in range(32)])
    pdeg=np.array(pd) if np.ndim(pd)==1 else np.array([0]*pdim)
    # polynomial degree per block-basis vector
    deg=[]
    for m in range(N+1):
        for k in range(0,(N-m)//2+1):
            pass
    w,v=np.linalg.eigh(H)
    # interior: eigenvectors whose weight sits at poly-degree <= N-1
    # use the block-degree labels from polyops ordering
    bl=[]
    for m in range(N+1):
        sub=int(np.sum(np.array([1]*0)))
    # simpler: reconstruct degree labels the same way polyops does
    import itertools as it
    bs=[x for x in it.product(range(N+1),repeat=5) if sum(x)<=N]
    dg=np.array([sum(x) for x in bs])
    Q=None
    degs=[]
    for m in range(N+1):
        cnt_m=int(np.sum(dg==m))
        # harmonic dim at degree m
        hm=cnt_m-(int(np.sum(dg==m-2)) if m>=2 else 0)
        for k in range(0,(N-m)//2+1):
            degs += [m+2*k]*hm
    degs=np.array(degs[:pdim])
    lab=np.array([degs[p] for f in range(32) for p in range(pdim)])
    keep=[]
    for i in range(len(w)):
        j=int(np.argmax(np.abs(v[:,i])))
        if lab[j]<=N-1: keep.append(w[i])
    keep=np.array(sorted(keep))
    tau=keep[0]; nz=keep[keep>1e-9]
    gap=nz[0]-tau if len(nz) else float('nan')
    print("   %d    %-6d  %.6f   %10.6f            %.4f    [%.0fs]"%(N,n,tau,nz[0] if len(nz) else float('nan'),gap,time.time()-t0))
    sys.stdout.flush()
