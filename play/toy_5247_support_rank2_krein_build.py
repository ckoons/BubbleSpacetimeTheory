import numpy as np, itertools
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
N=2; nu=F(5,2)
Kt,Pt,pd,_=polyops(N,nu); a=fermions()
# need per-variable polynomial degrees in the block basis -> rebuild raw monomial labels
basis=[x for x in itertools.product(range(N+1),repeat=5) if sum(x)<=N]
qf=np.array([bin(i).count('1') for i in range(32)]); pdim=len(pd); n=32*pdim
D=np.zeros((n,n))
for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
w,v=np.linalg.eigh(D)
neg,zero=w<-1e-9,np.abs(w)<=1e-9
P=v[:,neg]@v[:,neg].T; P0=v[:,zero]@v[:,zero].T
print("dim=%d  ||D-D^T||=%.1e   spec: %d neg / %d zero / %d pos"%(n,np.abs(D-D.T).max(),neg.sum(),zero.sum(),(w>1e-9).sum()))
print()
print("THE GATE, SIMPLIFIED: P is already self-adjoint in FK (P=P^T exactly), so")
print("   P‡ = J P^T J = J P J = P   <=>   [J, P] = 0.")
print("   Sufficient: [J, D] = 0.  Parity FAILED because it ANTI-commutes.")
print("   *** and J must be sourced from GEOMETRY, not from D or P -- else [J,P]=0 is automatic and vacuous.")
print()
# rank-2 idempotent frame: distinguished 2-plane. Reflection R = diag(-1,-1,+1,+1,+1) in SO(5), det=+1.
# lift: fermion (-1)^(n_1+n_2)  (x)  polynomial (-1)^(deg_1+deg_2)
ferm=np.diag([(-1.0)**(((i>>0)&1)+((i>>1)&1)) for i in range(32)])
# polynomial side: need the sign in the BLOCK basis -> build in monomial basis then rotate
idx={x:i for i,x in enumerate(basis)}
sgn_mono=np.diag([(-1.0)**(x[0]+x[1]) for x in basis])
# recover the block-basis rotation U used inside polyops by re-deriving it
def blockU(N,nu,n5=5):
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
    return np.hstack(cols)
U=blockU(N,nu)
sgn_blk=U.T@sgn_mono@U
J2=np.kron(ferm,sgn_blk)
for name,J in [("RANK-2 REFLECTION  R=diag(-1,-1,+1,+1,+1) lifted to fermion (x) polynomial", J2),
               ("fermion-only piece  (-1)^(n_1+n_2)", np.kron(ferm,np.eye(pdim))),
               ("polynomial-only piece (-1)^(d_1+d_2)", np.kron(np.eye(32),sgn_blk))]:
    ev=np.linalg.eigvalsh((J+J.T)/2)
    npos=int(np.sum(ev>1e-9)); nneg=int(np.sum(ev<-1e-9))
    print("J = %s"%name)
    print("   J^2=1: %.1e | INDEFINITE? signature (+%d, -%d) -> %s"%(np.abs(J@J-np.eye(n)).max(),npos,nneg,"YES" if npos and nneg else "NO"))
    print("   [J,D]=0 : %.3e     [J,D]_+ =0 : %.3e"%(np.abs(J@D-D@J).max(),np.abs(J@D+D@J).max()))
    print("   GATE 1c  [J,P]=0 : %.3e   ||P‡ - P|| = %.3e   %s"%(np.abs(J@P-P@J).max(),np.abs(J@P.T@J-P).max(),
          "PASS" if np.abs(J@P.T@J-P).max()<1e-9 else "FAIL"))
    print()
