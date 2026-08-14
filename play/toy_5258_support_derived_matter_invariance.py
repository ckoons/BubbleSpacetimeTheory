import numpy as np, itertools
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
N=2; nu=F(5,2)
Kt,Pt,pd,_=polyops(N,nu); a=fermions(); pdim=len(pd); n=32*pdim
D=np.zeros((n,n))
for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
w,v=np.linalg.eigh(D)
neg=w<-1e-9
Psea=v[:,neg]@v[:,neg].T          # THE DERIVED OCCUPIED CONFIGURATION: the Dirac sea of the credentialed operator
print("dim=%d   occupied (sea) states = %d   [derived by diagonalising the operator, not inserted]"%(n,neg.sum()))
print()
# ---- SO(5) generators on fermion (x) polynomial ----
def blockU(N,n5=5):
    bs=[x for x in itertools.product(range(N+1),repeat=n5) if sum(x)<=N]
    ix={x:i for i,x in enumerate(bs)}; dm=len(bs); dg=np.array([sum(x) for x in bs])
    def bd(mu):
        M=np.zeros((dm,dm))
        for x,i in ix.items():
            y=list(x); y[mu]+=1; y=tuple(y)
            if y in ix: M[ix[y],i]=np.sqrt(y[mu])
        return M
    Bd=[bd(m) for m in range(n5)]; Q=sum(Bd[m]@Bd[m] for m in range(n5)); Lap=Q.T
    cols=[]
    for m in range(N+1):
        sub=np.nonzero(dg==m)[0]
        if m>=2:
            Ls=Lap[np.ix_(np.nonzero(dg==m-2)[0],sub)]
            _,s,vt=np.linalg.svd(Ls); H=vt[np.sum(s>1e-10):].T
        else: H=np.eye(len(sub))
        for k in range(0,(N-m)//2+1):
            C=np.zeros((dm,H.shape[1])); C[sub,:]=H
            Mk=np.linalg.matrix_power(Q,k)@C
            if Mk.shape[1]==0: continue
            u,s,_=np.linalg.svd(Mk,full_matrices=False); r=int(np.sum(s>1e-9))
            if r: cols.append(u[:,:r])
    return np.hstack(cols),Bd
U,Bd=blockU(N)
Bp=[U.T@x@U for x in Bd]                     # boson creators in the block basis
print("SO(5) INVARIANCE OF THE DERIVED SEA  (10 generators L_ab, a<b)")
print("   the generator acts on BOTH indices: L = L_fermion (x) 1 + 1 (x) L_poly")
worstD=0; worstP=0
for i in range(5):
    for j in range(i+1,5):
        LF=a[i].T@a[j]-a[j].T@a[i]           # fermion rotation
        LP=Bp[i]@Bp[j].T-Bp[j]@Bp[i].T       # polynomial rotation
        L=np.kron(LF,np.eye(pdim))+np.kron(np.eye(32),LP)
        worstD=max(worstD,np.abs(D@L-L@D).max())
        worstP=max(worstP,np.abs(Psea@L-L@Psea).max())
print("   max ||[D, L_ab]||   = %.3e   -> operator SO(5)-invariant: %s"%(worstD,worstD<1e-9))
print("   max ||[P_sea, L_ab]|| = %.3e -> DERIVED SEA SO(5)-INVARIANT: %s"%(worstP,worstP<1e-9))
print()
print("=> the occupied configuration BST actually derives commutes with every SO(5) generator.")
print("=> by toy 5257's theorem it therefore selects NO direction in R^5.")
print("=> and this is the honest possibility Keeper pre-committed: a full filling is isotropic.")
