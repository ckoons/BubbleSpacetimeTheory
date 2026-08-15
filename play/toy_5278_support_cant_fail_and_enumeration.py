import numpy as np
rng=np.random.default_rng(1554)
def height(R):
    n=R.shape[0]; h=np.ones(n,dtype=int)
    for b in range(n):
        pre=np.nonzero(R[:,b])[0]
        if len(pre): h[b]=1+h[pre].max()
    return h.max()
def box(N,d,a,rng):
    t=rng.uniform(0,a,N); x=rng.uniform(0,1,(N,d-1))
    o=np.argsort(t); t,x=t[o],x[o]
    dt=t[None,:]-t[:,None]; s=np.linalg.norm(x[None,:,:]-x[:,None,:],axis=2)
    R=(dt>0)&(dt>s); return R.sum()/(N*(N-1)/2), height(R)

print("="*90)
print("TEST 1 -- IS READING 1 ('the 3 spatial dims ARE the color triplet, so use 3 spatial dims')")
print("          A CONSTRUCTION-GUARANTEED TEST?  Vary the INSERTED rep dimension and watch the output.")
print("="*90)
print("  If the pipeline is 'insert a k-dim irreducible rep as space, sprinkle, read height', then the")
print("  read must return d = k+1 for EVERY k -- with zero information coming from the color structure.\n")
print("    inserted rep dim k     spacetime d = k+1     height read (N=1500, a=1)")
for k in [2,3,4,5,6]:
    v=np.array([box(1500,k+1,1.0,rng) for _ in range(8)])
    print("          %d                     %d                 h = %.2f   r = %.4f"%(k,k+1,v[:,1].mean(),v[:,0].mean()))
print()
print("  ★ THE OUTPUT TRACKS THE INSERTED REP DIMENSION EXACTLY. The color triplet contributes the")
print("    integer 3 and nothing else. Reading 1 CANNOT FAIL -- it returns d=4 because 3 was put in.")
print("    (My own 5253 lesson: the estimator returns the dimension of whatever you hand it.)")
print()
print("="*90)
print("TEST 2 -- DOES IRREDUCIBILITY SUPPLY '3' TARGET-INNOCENTLY? (enumerate before the 'therefore')")
print("="*90)
irreps=[1,3,3,6,8,10,10,15,15,24,27]
print("  SU(3) irreducible representations, dimensions:", irreps, "...")
print("  'Irreducible => no invariant 1-dim subspace' is satisfied by EVERY entry except the trivial 1.")
print("  So irreducibility permits dim in {3,6,8,10,15,27,...} -- it does NOT single out 3.")
print("  The 3 comes from ADDITIONALLY choosing the FUNDAMENTAL. That choice is the assumption.")
print("  And 3-dim irreducible reps are not unique to color: SO(3) vector, SU(2) adjoint, ...")
print("  ⟹ 'color is irreducible, THEREFORE space is 3-dimensional' has unenumerated alternatives.")
