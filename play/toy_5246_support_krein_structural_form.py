import numpy as np, itertools
from fractions import Fraction as F
exec(open('/private/tmp/claude-501/-Users-cskoons-projects-github/4ea94fa6-b3fe-41e8-9a52-1a6c7015cf19/scratchpad/shape2.py').read().split('def run(')[0])
for N in [2]:
    nu=F(5,2); Kt,Pt,pd,_=polyops(N,nu); a=fermions()
    q=np.array([bin(i).count('1') for i in range(32)]); pdim=len(pd); n=32*pdim
    D=np.zeros((n,n))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    w,v=np.linalg.eigh(D)
    neg,zero,pos=w<-1e-9,np.abs(w)<=1e-9,w>1e-9
    P=v[:,neg]@v[:,neg].T; P0=v[:,zero]@v[:,zero].T; Ppos=v[:,pos]@v[:,pos].T
    J=np.kron(np.diag([(-1)**int(q[i]) for i in range(32)]),np.eye(pdim))
    Pk=J@P.T@J
    print("N=%d dim=%d | spec(D): %d neg, %d zero, %d pos"%(N,n,neg.sum(),zero.sum(),pos.sum()))
    print("   P^2=P: %.1e   P=P^T: %.1e   JDJ=-D: %.1e"%(np.abs(P@P-P).max(),np.abs(P-P.T).max(),np.abs(J@D@J+D).max()))
    print("   P‡ vs P          : %.3e"%np.abs(Pk-P).max())
    print("   P‡ vs 1-P        : %.3e"%np.abs(Pk-(np.eye(n)-P)).max())
    print("   P‡ vs 1-P-P0     : %.3e   <-- the exact structural form"%np.abs(Pk-(np.eye(n)-P-P0)).max())
    print("   P‡ vs P_pos      : %.3e   (same thing: J maps the sea to its mirror)"%np.abs(Pk-Ppos).max())
    print("   is J P0 J = P0 (kernel J-invariant)? %.1e"%np.abs(J@P0@J-P0).max())
