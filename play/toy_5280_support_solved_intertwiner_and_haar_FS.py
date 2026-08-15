import numpy as np
from scipy.linalg import expm
rng=np.random.default_rng(1558)
np.set_printoptions(precision=4,suppress=True)
print("FIXES: (1) SOLVE for the intertwiner instead of guessing it was the identity -- my first pass")
print("           assumed M=I with a hand-chosen generator ordering and got residual 1.94. Solve it.")
print("       (2) FS indicator needs HAAR measure -- my exp-of-Gaussian sampling was not Haar and")
print("           returned +0.03 for the doublet (true value -1). Sample unit quaternions instead.\n")
lam={1:np.array([[0,1,0],[1,0,0],[0,0,0]],complex),
     2:np.array([[0,-1j,0],[1j,0,0],[0,0,0]]),
     3:np.diag([1,-1,0]).astype(complex),
     5:np.array([[0,0,-1j],[0,0,0],[1j,0,0]]),
     7:np.array([[0,0,0],[0,0,-1j],[0,1j,0]])}
def L(a):
    M=np.zeros((3,3)); eps={(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}
    for (x,y,z),v in eps.items():
        if x==a: M[y,z]=-v
    return M.astype(complex)
def solve_hom(V,T):
    A=np.vstack([np.kron(Va.T,np.eye(3))-np.kron(np.eye(3),Ta) for Va,Ta in zip(V,T)])
    U,s,Vh=np.linalg.svd(A)
    ns=[Vh[i].conj().reshape(3,3) for i in range(len(Vh)) if i>=len(s) or s[i]<1e-9]
    return ns,s
B=[1j*lam[a]/2 for a in (7,5,2)]; Lm=[0.5*L(a) for a in range(3)]
ns,s=solve_hom(B,Lm)
print("ROUTE B: dim Hom = %d.  The solved intertwiner (up to scale):"%len(ns))
M=ns[0]/np.abs(ns[0]).max()
print(M.real if np.abs(M.imag).max()<1e-9 else M)
err=[]
for _ in range(300):
    th=rng.normal(size=3)
    g=expm(sum(t*b for t,b in zip(th,B))); h=expm(sum(t*l for t,l in zip(th,Lm)))
    err.append(np.abs(M@g-h@M).max())
print("  max |M rho_colour(g) - rho_sky(g) M| over 300 GROUP elements = %.2e   => equivariant on the group\n"%max(err))
A=[1j*lam[a]/2 for a in (1,2,3)]
ns2,_=solve_hom(A,Lm)
print("ROUTE A: dim Hom = %d  => no intertwiner exists at all.\n"%len(ns2))

print("FROBENIUS-SCHUR INDICATOR, proper Haar sampling (unit quaternions):")
def haar_q(n): 
    q=rng.normal(size=(n,4)); return q/np.linalg.norm(q,axis=1)[:,None]
Q=haar_q(400000)
a,b,c,d=Q[:,0],Q[:,1],Q[:,2],Q[:,3]
# SU(2) fundamental: tr(U^2) where U is the quaternion as a 2x2 SU(2) matrix; tr U = 2a => tr U^2 = (tr U)^2 - 2 det U = 4a^2 - 2
fs_doub=np.mean(4*a**2-2)
# SO(3) vector: tr R = 4a^2 - 1 ; R^2 corresponds to quaternion q^2 whose scalar part is a^2-(b^2+c^2+d^2) = 2a^2-1
fs_vec=np.mean(4*(2*a**2-1)**2-1)
print("  SU(2) DOUBLET (route A's module) : FS = %+.4f   => PSEUDO-REAL (-1). Carries an L/R structure."%fs_doub)
print("  SO(3) VECTOR  (route B's module) : FS = %+.4f   => REAL (+1). Admits NO chiral split."%fs_vec)
print("\n  ⟹ MUTUALLY EXCLUSIVE: the route WITH the map (B) carries NO chirality; the route WITH")
print("     chirality (A) has NO map. 'Chirality rides along for free' is not available on the")
print("     route that has the isomorphism. Gate 3 decided, against the hoped-for combination.")
