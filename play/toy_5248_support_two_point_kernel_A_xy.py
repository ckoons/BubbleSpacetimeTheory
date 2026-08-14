import numpy as np, itertools
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
rng=np.random.default_rng(7)
N=2; nu=F(5,2)
Kt,Pt,pd,_=polyops(N,nu); a=fermions()
basis=[x for x in itertools.product(range(N+1),repeat=5) if sum(x)<=N]
pdim=len(pd); n=32*pdim
D=np.zeros((n,n))
for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
w,v=np.linalg.eigh(D); neg=w<-1e-9
occ=v[:,neg]                                  # occupied states, columns
print("occupied states: %d of %d"%(occ.shape[1],n))
# block->monomial rotation U (same construction as inside polyops)
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
    return np.hstack(cols)
U=blockU(N)
from math import factorial
def Erow(z):
    return np.array([np.prod([z[m]**x[m] for m in range(5)])/np.sqrt(np.prod([factorial(x[m]) for m in range(5)])) for x in basis])
def psi(z):
    e=(Erow(z)@U)                      # (pdim,) in block coords
    C=occ.reshape(32,pdim,-1)          # [fermion, block, state]
    return np.einsum('p,fpk->fk',e,C)  # 32 x n_occ
def Pxy(x,y):
    return psi(x)@psi(y).conj().T      # 32x32
# rank-2 Krein operator on the fermion fibre
Jf=np.diag([(-1.0)**(((i>>0)&1)+((i>>1)&1)) for i in range(32)])
def classify(ev,tol=1e-6):
    mod=np.abs(ev); mod=mod[mod>1e-12]
    if len(mod)==0: return "null"
    spread=(mod.max()-mod.min())/mod.max()
    realish=np.all(np.abs(ev.imag)<tol*max(1,np.abs(ev).max()))
    if spread<1e-6: return "spacelike"
    return "timelike" if realish else "neither"
print()
print("PRE-REGISTERED PREDICTION (stated before computing):")
print("  the FK metric is POSITIVE DEFINITE (toy 5246), so with the HILBERT adjoint")
print("  P(y,x) = P(x,y)^dag  =>  A_xy = M M^dag is POSITIVE SEMI-DEFINITE")
print("  => eigenvalues real >= 0, generically DISTINCT => 100% TIMELIKE, 0% SPACELIKE.")
print("  Spacelike points REQUIRE the indefinite Krein adjoint to enter the two-point kernel.")
print()
cnt={'H':{}, 'K':{}}
sym=[]
for _ in range(200):
    x=(rng.normal(size=5)+1j*rng.normal(size=5))*0.12
    y=(rng.normal(size=5)+1j*rng.normal(size=5))*0.12
    Mxy=Pxy(x,y); Myx=Pxy(y,x)
    sym.append(np.abs(Myx-Jf@Mxy.conj().T@Jf).max()/max(np.abs(Myx).max(),1e-30))
    for tag,A in [('H',Mxy@Mxy.conj().T),('K',Mxy@(Jf@Mxy.conj().T@Jf))]:
        c=classify(np.linalg.eigvals(A)); cnt[tag][c]=cnt[tag].get(c,0)+1
print("two-point Krein symmetry  P(y,x) = J P(x,y)^dag J :  median rel-error = %.3f  (5209 had 1.401)"%np.median(sym))
print()
for tag,name in [('H','A_xy with HILBERT adjoint   (positive-definite)'),('K','A_xy with KREIN adjoint  (rank-2 indefinite J)')]:
    tot=sum(cnt[tag].values())
    print("%s :"%name)
    for k in ['spacelike','timelike','neither','null']:
        if k in cnt[tag]: print("     %-10s %3d / %d  = %5.1f%%"%(k,cnt[tag][k],tot,100*cnt[tag][k]/tot))
