import numpy as np, itertools
from math import factorial
from fractions import Fraction as F
exec(open('axy.py').read().split('print()\nprint("PRE-REGISTERED')[0])
rng=np.random.default_rng(11)
print("="*74)
print("B1 EDGE-TEST: is the 0.465 two-point Krein gap closable, or structural?")
print("="*74)
print()
print("STEP 1 -- reduce the condition. P(x,y) = sum_k psi_k(x) psi_k(y)^dag, so")
print("   P(y,x) = P(x,y)^dag  IDENTICALLY, by construction.")
print("   => the Finster condition  P(y,x) = J P(x,y)^dag J  becomes  [J_f , P(x,y)] = 0.")
print("   It is not a symmetry to be arranged: it demands the two-point kernel COMMUTE with J.")
print()
print("STEP 2 -- what the OPERATOR-level symmetry actually gives. J = J_f (x) J_poly, and")
print("   J_poly reflects the point: z_mu -> -z_mu for mu < r. So [J,P]=0 gives")
print("        J_f P(Rx, Ry) J_f = P(x,y)    -- a relation between REFLECTED points.")
print("   Finster needs the relation at the SAME points. Different conditions. Testing both:")
print()
def Rpt(z,r): 
    w=z.copy(); w[:r]*=-1; return w
for r in [0,1,2,3,4,5]:
    Jf=np.diag([(-1.0)**sum(((i>>m)&1) for m in range(r)) for i in range(32)])
    e_refl=[]; e_same=[]
    for _ in range(120):
        x=(rng.normal(size=5)+1j*rng.normal(size=5))*0.12
        y=(rng.normal(size=5)+1j*rng.normal(size=5))*0.12
        Mxy=Pxy(x,y)
        # (a) reflected-point relation (what [J,P]=0 delivers)
        Mrr=Pxy(Rpt(x,r),Rpt(y,r))
        e_refl.append(np.abs(Jf@Mrr@Jf-Mxy).max()/max(np.abs(Mxy).max(),1e-30))
        # (b) same-point relation (what Finster needs)  <=>  [J_f, P(x,y)] = 0
        e_same.append(np.abs(Jf@Mxy-Mxy@Jf).max()/max(np.abs(Mxy).max(),1e-30))
    print("   r=%d  |  reflected-point relation: %.3e   |  SAME-point [J_f,P(x,y)]=0 : %.4f  %s"%(
        r,np.median(e_refl),np.median(e_same),"<-- CLOSES (but J=1, not indefinite)" if np.median(e_same)<1e-9 else ""))
print()
print("STEP 3 -- the verdict test: does ANY indefinite J close the same-point condition?")
print("   [J_f, P(x,y)] = 0 for ALL x,y forces J_f to commute with the algebra the")
print("   occupied wave-functions generate. Checking the rank of that algebra:")
Ms=[]
for _ in range(60):
    x=(rng.normal(size=5)+1j*rng.normal(size=5))*0.12
    y=(rng.normal(size=5)+1j*rng.normal(size=5))*0.12
    Ms.append(Pxy(x,y))
S=np.stack([M.ravel() for M in Ms])
rk=np.linalg.matrix_rank(S,tol=1e-8)
print("   span of {P(x,y)} over 60 point-pairs has rank %d out of 32^2 = 1024"%rk)
# commutant: solve [J,M]=0 for all sampled M
A=np.vstack([np.kron(np.eye(32),M)-np.kron(M.T,np.eye(32)) for M in Ms[:20]])
u,s,vt=np.linalg.svd(A,compute_uv=True)
null=int(np.sum(s<1e-8*max(s)))
print("   commutant dimension (J with [J,P(x,y)]=0 for all sampled pairs) = %d"%null)
print("   => if that is 1, the ONLY solution is J proportional to the identity: NOT indefinite.")
