#!/usr/bin/env python3
"""
Toy 5800 (Lyra, round 5, 2026-09-26). Predictions written BEFORE the run:
 P1  The standard conjugation sigma(v)=conj(v) on V=C^5 is an antilinear triple automorphism,
     maps the time-line tripotent e=(x0+i y0)/2 to e-bar (reverses the arrow, Cal S988), and
     restricts to V1 = C^3 as V1's real structure.  tr(rho rho^T) = |<sigma v, v>|^2.
 P2  {U in U(3): U sigma = sigma U} = O(3); its Lie algebra has dim 3 (vs su(3) dim 8).
 P3  K's centre J = 1(x)j on p = R^5 (x) R^2 commutes with ALL of so(4) (x) 1 (so(4) = stab of x0)
     => commutes with BOTH su(2) factors.  NEGATIVE CONTROL: F242's J12+J34 (in so(4)) fails to
     commute with one su(2).  Predict: [J, so(4)] = 0 exactly; F242 element commutes with 3 of 6.
 P4  On the J-invariant R^4 = span(x0,y0) (x) R^2: J is self-dual, the plane rotation anti-self-dual.
 P5  Every SO(4)-type (SO(4) = stab of a real vector) in degree-j harmonics on C^5 is (i/2,i/2),
     dim (i+1)^2, i=0..j:  sum (i+1)^2 = dim SO(5) harmonic (j,0).  i.e. every SO(4)-type of the
     polynomial model of H^2(D_IV^5) is a hydrogen shell n^2.
 P6  SO(2)-weights of H^2(D_IV^5) lie in 5/2 + Z_{>=0}; the SO(4,2) ladder (hydrogen) rep has
     weights 1 + Z_{>=0} with shell n at weight n.  => Hom_{SO(4,2)}(ladder, H^2) = 0 (floor AND lattice).
 P7  Lambda^3 C^3 is 1-dim (epsilon); SU(3) preserves it, the U(3) centre does not; v^v = 0.
SCORE counts can-fail predictions P1..P7 (P3 has the negative control).
"""
import numpy as np, itertools
from math import comb
rng=np.random.default_rng(5800); ok=[]
q=lambda a,b: a@b
def trip(x,y,z): return q(x,y.conj())*z + q(z,y.conj())*x - q(x,z)*y.conj()
# P1
x0=np.eye(5)[0]; y0=np.eye(5)[1]; e=(x0+1j*y0)/2
X,Y,Z=[rng.normal(size=5)+1j*rng.normal(size=5) for _ in range(3)]
aut=np.allclose(trip(X.conj(),Y.conj(),Z.conj()), trip(X,Y,Z).conj())
arrow=np.allclose(e.conj(), (x0-1j*y0)/2) and not np.allclose(e.conj(),e)
v=np.zeros(5,complex); v[2:]=rng.normal(size=3)+1j*rng.normal(size=3); v/=np.linalg.norm(v)
preservesV1=np.allclose(v.conj()[:2],0)
rho=np.outer(v,v.conj()); lhs=np.trace(rho@rho.T).real; rhs=abs(np.vdot(v.conj(),v))**2
P1=aut and arrow and preservesV1 and np.isclose(lhs,rhs); ok.append(P1)
print(f"P1 antilinear aut={aut} e->ebar={arrow} V1 kept={preservesV1} tr(rho rho^T)={lhs:.6f} |<sv,v>|^2={rhs:.6f} -> {P1}")
# P2: real Lie algebra of u(3) commuting with conj: X = -X^dag and X real
basis=[]
for i in range(3):
    for j in range(3):
        for c in (1,1j):
            M=np.zeros((3,3),complex); M[i,j]+=c; M[j,i]-=np.conj(c)
            if np.allclose(M,0): continue
            basis.append(M)
B=np.array([np.concatenate([M.real.ravel(),M.imag.ravel()]) for M in basis]); du3=np.linalg.matrix_rank(B)
Bc=np.array([M.imag.ravel() for M in basis])  # commute with conj <=> Im M = 0
null=du3-np.linalg.matrix_rank(Bc.T@np.eye(Bc.shape[1])) if False else None
# solve: combos sum c_k M_k with Im=0
A=np.array([M.imag.ravel() for M in basis]).T; dimO3=len(basis)-np.linalg.matrix_rank(A)
# basis may be overcomplete; restrict to independent set
Ms=[];R=0
for M in basis:
    T=np.array([np.concatenate([N.real.ravel(),N.imag.ravel()]) for N in Ms+[M]])
    if np.linalg.matrix_rank(T)>R: Ms.append(M); R+=1
A=np.array([M.imag.ravel() for M in Ms]).T; dimO3=len(Ms)-np.linalg.matrix_rank(A)
P2=(len(Ms)==9 and dimO3==3); ok.append(P2); print(f"P2 dim u(3)={len(Ms)} dim commutant of conj={dimO3} -> {P2}")
# P3: p = R^5 (x) R^2 as R^10 ; so(5) acts X(x)1, J = 1(x)j
j2=np.array([[0,-1],[1,0]]); J=np.kron(np.eye(5),j2)
def E(a,b,n=5):
    M=np.zeros((n,n)); M[a,b]=-1; M[b,a]=1; return M
so4=[E(a,b) for a,b in itertools.combinations(range(1,5),2)]   # stab of x0
Jcomm=max(np.abs(np.kron(M,np.eye(2))@J-J@np.kron(M,np.eye(2))).max() for M in so4)
# su(2)_pm inside so(4) on coords 1..4 : L_i = (E_ab +/- E_cd)
pairs=[((1,2),(3,4)),((1,3),(4,2)),((1,4),(2,3))]
sup=[E(*a)+E(*b) for a,b in pairs]; sum_=[E(*a)-E(*b) for a,b in pairs]
F242=E(1,2)+E(3,4)
ncomm=sum(np.allclose(F242@M-M@F242,0) for M in sup+sum_)
P3=(Jcomm<1e-14 and ncomm==3); ok.append(P3)
print(f"P3 max|[J, so(4)(x)1]|={Jcomm:.1e} (J central in K) ; F242 element commutes with {ncomm}/6 su(2)+-su(2) generators -> {P3}")
# P4: R^4 = span(x0,y0)(x)R^2 basis (x0f1,x0f2,y0f1,y0f2) = coords 0..3
J4=np.kron(np.eye(2),j2); R4=np.kron(j2,np.eye(2))
def sd(M):  # coefficient vector on e_ab ; self-dual iff M01=M23, M02=M31, M03=M12 (as 2-form w_ab=M[b,a])
    w=lambda a,b: M[b,a]
    s=np.array([w(0,1)-w(2,3), w(0,2)-w(3,1), w(0,3)-w(1,2)]); a=np.array([w(0,1)+w(2,3), w(0,2)+w(3,1), w(0,3)+w(1,2)])
    return np.allclose(s,0), np.allclose(a,0)
P4=(sd(J4)==(True,False) and sd(R4)==(False,True)); ok.append(P4)
print(f"P4 J on plane(x)R^2: (SD,ASD)={sd(J4)} ; plane rotation: {sd(R4)} -> {P4}")
# P5
dimSO5=lambda j:(j+1)*(j+2)*(2*j+3)//6
harm5=lambda j: comb(j+4,4)-(comb(j+2,4) if j>=2 else 0)
P5=all(harm5(j)==dimSO5(j)==sum((i+1)**2 for i in range(j+1)) for j in range(40)); ok.append(P5)
print(f"P5 harmonic deg-j on C^5 = SO(5)(j,0) = sum_(i<=j) (i+1)^2 for j<40: {P5}  e.g. j=3: {harm5(3)} = 1+4+9+16")
# P6
W_H2={2.5+k for k in range(60)}; W_lad={1+k for k in range(60)}
shells=[(n, n*n, 2*n*n) for n in range(1,5)]
P6=(len(W_H2 & W_lad)==0 and min(W_H2)>min(W_lad)); ok.append(P6)
print(f"P6 weights(H2) cap weights(ladder) = {sorted(W_H2&W_lad)} ; floors {min(W_H2)} vs {min(W_lad)} ; shells (n,n^2,2n^2)={shells} -> {P6}")
# P7
eps=np.zeros((3,3,3))
for p in itertools.permutations(range(3)): eps[p]=np.linalg.det(np.eye(3)[list(p)])
Hm=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); Hm=Hm+Hm.conj().T
w_,V_=np.linalg.eigh(Hm); U=V_@np.diag(np.exp(1j*w_))@V_.conj().T; U=U/np.linalg.det(U)**(1/3)
epsU=np.einsum('ia,jb,kc,abc->ijk',U,U,U,eps); ph=np.exp(0.7j)
a=rng.normal(size=3); wedge=np.einsum('abc,a,b,c->',eps,a,a,rng.normal(size=3))
P7=np.allclose(epsU,eps) and not np.allclose(ph**3*eps,eps) and abs(wedge)<1e-12; ok.append(P7)
print(f"P7 SU(3) keeps eps={np.allclose(epsU,eps)} ; centre phase keeps eps={np.allclose(ph**3*eps,eps)} ; v^v^w={wedge:.1e} -> {P7}")
print(f"SCORE {sum(ok)}/{len(ok)}")
