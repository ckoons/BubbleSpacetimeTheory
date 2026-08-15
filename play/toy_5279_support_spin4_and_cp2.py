import numpy as np
rng=np.random.default_rng(825)
print("="*88)
print("LEG THAT WORKS: chirality's L/R IS the descent's two SU(2)'s  (Spin(4) = SU(2)_L x SU(2)_R)")
print("="*88)
def qmat(q):                      # left mult by unit quaternion, as a 4x4 real matrix
    a,b,c,d=q
    return np.array([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]])
def qmatR(q):                     # right mult by conjugate
    a,b,c,d=q
    return np.array([[a,b,c,d],[-b,a,d,-c],[-c,-d,a,b],[-d,c,-b,a]])
def rand_unit(rng):
    q=rng.normal(size=4); return q/np.linalg.norm(q)
bad=0; dets=[]
for _ in range(300):
    qL,qR=rand_unit(rng),rand_unit(rng)
    M=qmat(qL)@qmatR(qR)
    if not np.allclose(M@M.T,np.eye(4),atol=1e-12): bad+=1
    dets.append(np.linalg.det(M))
print("  map (q_L,q_R) -> [x -> q_L x conj(q_R)] : orthogonal in %d/300 samples, det = %.10f (all +1: %s)"
      %(300-bad,np.mean(dets),np.allclose(dets,1,atol=1e-10)))
# kernel
I=np.eye(4); ker=[]
for qL,qR in [((1,0,0,0),(1,0,0,0)),((-1,0,0,0),(-1,0,0,0)),((-1,0,0,0),(1,0,0,0))]:
    M=qmat(np.array(qL,float))@qmatR(np.array(qR,float))
    ker.append(np.allclose(M,I,atol=1e-12))
print("  kernel: (+1,+1)->I %s ; (-1,-1)->I %s ; (-1,+1)->I %s   => kernel = {+-(1,1)}, order 2"%tuple(ker))
print("  ⟹ SU(2)_L x SU(2)_R -> SO(4) is 2:1. Spin(4) = SU(2)xSU(2). THE L/R SPLIT IS REAL AND IS")
print("     EXACTLY WHERE THE DESCENT SO(5)->SO(4) LANDS. This leg of the chain HOLDS.")
print()
print("  ★ CAVEAT, stated so it isn't over-read: Spin(4)=SU(2)xSU(2) is the EUCLIDEAN split.")
print("    Physical chirality is Spin(3,1)=SL(2,C), whose L/R are complex-CONJUGATE reps, not two")
print("    independent compact factors. Same structure, different group; identifying them needs the")
print("    Wick rotation -- an extra step, not a free consequence.")
print()
print("="*88)
print("THE LEG THAT DOES NOT: WHICH SU(2) inside SU(3)?")
print("="*88)
print("  The block SU(2) = {diag(A,1)} fixes a complex LINE in C^3. Its conjugates are in bijection")
print("  with the choice of that line => the family of SU(2) subgroups of SU(3) IS CP^2.")
print("  dim_R = dim SU(3) - dim U(2) = 8 - 4 = %d"%(8-4))
# numerical: local dimension of the set of rank-1 projectors on C^3
def proj(v):
    v=v/np.linalg.norm(v); P=np.outer(v,v.conj())
    return np.concatenate([P.real.ravel(),P.imag.ravel()])
v0=np.array([1,0,0],dtype=complex)
base=proj(v0); T=[]
for _ in range(400):
    w=v0+1e-4*(rng.normal(size=3)+1j*rng.normal(size=3))
    T.append(proj(w)-base)
sv=np.linalg.svd(np.array(T),compute_uv=False)
d=int((sv>sv[0]*1e-3).sum())
print("  numerical local dimension of the family (SVD of tangent samples): %d   singular values %s"
      %(d,np.array2string(sv[:6],precision=2)))
print("  ⟹ CHOOSING WHICH SU(2) SUBSET SU(3) IS A 4-PARAMETER CHOICE -- a point of CP^2.")
print("     'SU(3) contains SU(2)' does NOT pick one. And every SU(2) is isomorphic to every other,")
print("     so naming the group cannot supply a map to the SPATIAL Spin(3).")
print("     Same missing input as 5257 (a non-equivariant choice), in new clothes.")
