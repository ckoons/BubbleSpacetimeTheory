#!/usr/bin/env python3
"""
Lyra R17 (2026-09-27). Invariants first: eta = diag(+,+,+,+,-,-) on R^{4,2}; the de Sitter vector v = e5 (a time direction,
v^2 = -1); Stab(v) = so(4,1) on indices 0..4 (Cal S1011; Lyra R16). J = rotation of the two-time plane (4,5).
Predictions BEFORE the run:
 C1 J is not in Stab(e5) (J e5 != 0) and has no component along so(4,1): [projection of J onto Stab(e5)] = 0 - i.e. Lambda>0
    breaks J entirely, not partially.
 C2 so(4,1) contains no compact generator acting on the time index 4: every element mixing index 4 with 0..3 is a BOOST
    (trace form tr(X^2) > 0, hyperbolic, real eigenvalues +-1): the surviving 'time' (static-patch Killing time) is a boost,
    continuous spectrum; the compact part is so(4) (spatial rotations only).
 C3 J restricted to the flat limit: J = (P0+K0)/2 in the frame sl(2) (R6/R7) - checked here only as: J's orbit moves e5 in the
    (4,5) plane with period 2 pi (compact), whereas the boost M_{4,3} has unbounded orbit (noncompact).
"""
import numpy as np, itertools
from scipy.linalg import expm
ok=[]
eta=np.diag([1,1,1,1,-1,-1.]); n=6
def gen(a,b):
    M=np.zeros((n,n)); M[a,b]=1; M[b,a]=-1; return M@eta
basis={(a,b):gen(a,b) for a,b in itertools.combinations(range(n),2)}
e5=np.eye(n)[5]; J=basis[(4,5)]
stab=[X for k,X in basis.items() if np.allclose(X@e5,0)]
C1=(not np.allclose(J@e5,0)) and len(stab)==10 and all(5 not in k for k,X in basis.items() if np.allclose(X@e5,0))
ok.append(C1); print("C1 J e5 =",(J@e5).round(3),"; Stab(e5) = the 10 generators without index 5 ->",C1)
boosts=[basis[(i,4)] for i in range(4)]
C2=all(np.trace(X@X)>0 and np.allclose(sorted(np.linalg.eigvals(X).real)[0],-1) for X in boosts) and all(np.trace(basis[(i,j)]@basis[(i,j)])<0 for i,j in itertools.combinations(range(4),2))
ok.append(C2); print("C2 index-4 mixers are boosts (tr X^2 > 0), spatial rotations compact ->",C2)
orbJ=[np.linalg.norm(expm(t*J)@e5) for t in (0,np.pi,2*np.pi)]; orbB=[np.linalg.norm(expm(t*boosts[3])@np.eye(n)[4]) for t in (0,3,6)]
C3=np.allclose(expm(2*np.pi*J),np.eye(n)) and orbB[2]>orbB[1]>orbB[0]
ok.append(C3); print("C3 exp(2 pi J) = 1 (compact clock); boost orbit norms grow",np.round(orbB,2),"->",C3)
print(f"SCORE {sum(ok)}/{len(ok)}")
