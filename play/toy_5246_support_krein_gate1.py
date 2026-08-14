import numpy as np, itertools, time
from fractions import Fraction as F
exec(open('/private/tmp/claude-501/-Users-cskoons-projects-github/4ea94fa6-b3fe-41e8-9a52-1a6c7015cf19/scratchpad/shape2.py').read().split('def run(')[0])

N=3; nu=F(5,2)
Kt,Pt,pd,_=polyops(N,nu); a=fermions()
q=np.array([bin(i).count('1') for i in range(32)])
pdim=len(pd)
lab=[(int(q[f]),int(pd[p])) for f in range(32) for p in range(pdim)]
n=len(lab)
D=np.zeros((n,n))
for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
print("dim=%d   ||D-D^T||=%.2e  (self-adjoint in FK metric G)"%(n,np.abs(D-D.T).max()))

# --- is the FK metric itself indefinite (Krein) or positive definite (Hilbert)? ---
def fkval(lam): 
    o=F(1)
    for j in range(lam[0]): o*=(nu+j)
    for j in range(lam[1]): o*=(nu-F(3,2)+j)
    return o
vals=[fkval((m+k,k)) for k in range(4) for m in range(6)]
print("FK norms (nu=5/2): all positive? %s   min=%s"%(all(v>0 for v in vals),min(vals)))

# --- the sea projector P = Theta(-D) ---
w,v=np.linalg.eigh(D)
neg=w<-1e-9; zero=np.abs(w)<=1e-9; pos=w>1e-9
P=v[:,neg]@v[:,neg].T
print("\nspectrum of D: %d negative, %d zero, %d positive   (sym about 0: %s)"%(
    neg.sum(),zero.sum(),pos.sum(),abs(neg.sum()-pos.sum())==0))
print("GATE-1a  P^2 = P :  ||P@P - P|| = %.3e"%np.abs(P@P-P).max())
print("GATE-1b  P^dag = P (Hilbert, FK metric): ||P - P^T|| = %.3e"%np.abs(P-P.T).max())

# --- Krein candidates J ---
Jpar=np.kron(np.diag([(-1)**int(q[i]) for i in range(32)]),np.eye(pdim))   # fermion parity
# half-turn / Hodge: Lambda^k -> Lambda^(5-k) on the fermion fiber
Hodge=np.zeros((32,32))
for ket in range(32): Hodge[(~ket)&31,ket]=1.0
Jhod=np.kron(Hodge,np.eye(pdim))
for name,J in [("fermion parity (-1)^q",Jpar),("half-turn / Hodge  Λ^k→Λ^{5-k}",Jhod)]:
    ok_inv=np.abs(J@J-np.eye(n)).max()
    Pk=J@P.T@J                       # Krein adjoint  P‡ = J P† J   (P real)
    d_self=np.abs(Pk-P).max(); d_comp=np.abs(Pk-(np.eye(n)-P)).max()
    anti=np.abs(J@D@J+D).max(); comm=np.abs(J@D@J-D).max()
    print("\nJ = %s"%name)
    print("   J^2=1: %.1e |  JDJ = -D: %.1e   JDJ = +D: %.1e"%(ok_inv,anti,comm))
    print("   GATE-1c  P‡ = P  :  ||P‡ - P||        = %.3e   %s"%(d_self,"PASS" if d_self<1e-9 else "FAIL"))
    print("            P‡ = 1-P:  ||P‡ - (1 - P)||  = %.3e   %s"%(d_comp,"<-- complementary" if d_comp<1e-9 else ""))
