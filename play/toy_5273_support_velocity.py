import numpy as np, itertools, sys
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
print("="*80)
print("THE DERIVATION: does the commit-trajectory give the observer a FORCED velocity?")
print("="*80)
print("  Keeper: 'the commit operator's step generator IS the velocity.'")
print()
print("★ BUT THE SAME FACT THAT SETTLED THE DISTRIBUTION SETTLES THIS -- and the other way.")
print("  H_B = the CASIMIR of K = SO(5)xSO(2).  A Casimir is CENTRAL in K.")
print("  The boundary S^4 = SO(5)/SO(4) is a K-ORBIT. A central element acts as a SCALAR on each")
print("  K-isotypic component => exp(-tau H_B) multiplies components by numbers; it does NOT")
print("  TRANSPORT points along the orbit.")
print("  ⟹ a Casimir CANNOT generate a trajectory. There is no step, hence no velocity.")
print()
print("NUMERICAL CHECK on the built operator: does H_B move anything within a K-type?")
N=3
Kt,Pt,pd,_=polyops(N,F(5,2)); a=fermions(); pdim=len(pd); n=32*pdim
D=np.zeros((n,n))
for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
H=D@D
q=np.array([bin(i).count('1') for i in range(32)])
# SO(5) generators (as in toy 5258)
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
            _,s,vt=np.linalg.svd(Ls); Hh=vt[np.sum(s>1e-10):].T
        else: Hh=np.eye(len(sub))
        for k in range(0,(N-m)//2+1):
            C=np.zeros((dm,Hh.shape[1])); C[sub,:]=Hh
            Mk=np.linalg.matrix_power(Q,k)@C
            if Mk.shape[1]==0: continue
            u,s,_=np.linalg.svd(Mk,full_matrices=False); r=int(np.sum(s>1e-9))
            if r: cols.append(u[:,:r])
    return np.hstack(cols),Bd
U,Bd=blockU(N); Bp=[U.T@x@U for x in Bd]
worst=0
for i in range(5):
    for j in range(i+1,5):
        LF=a[i].T@a[j]-a[j].T@a[i]; LP=Bp[i]@Bp[j].T-Bp[j]@Bp[i].T
        L=np.kron(LF,np.eye(pdim))+np.kron(np.eye(32),LP)
        worst=max(worst,np.abs(H@L-L@H).max())
print("   max ||[H_B_eff, L_ab]|| over all 10 SO(5) generators = %.3e"%worst)
print("   => H commutes with every SO(5) generator: it CANNOT move a point on the S^4 orbit.")
print()
print("="*80)
print("⟹ THE ANSWER, AND IT IS A DEGENERATE ONE")
print("="*80)
print("  The commit dynamics as the corpus defines it gives the observer velocity v = 0 EXACTLY.")
print()
print("  GOOD:  v*Delta_tau = 0 < sigma/f_max holds TRIVIALLY => no baseline => no parallax")
print("         => depth never recoverable => the record IS angular. The mechanism's requirement")
print("         is satisfied.")
print("  BAD:   it is satisfied because NOTHING MOVES. A zero-velocity observer is a DEGENERATE")
print("         case, not a derivation -- and 'the commit-trajectory' does not exist: a central")
print("         generator has no trajectory to be a step of.")
print()
print("  ⟹ the premise is NOT discharged. It is VOIDED: there is no velocity to force, because")
print("     the generator that was supposed to supply it cannot generate motion at all.")
print("     Deriving a bounded velocity requires a NON-CENTRAL generator, which is exactly the")
print("     non-equivariant input 5257 says the geometry does not contain.")
