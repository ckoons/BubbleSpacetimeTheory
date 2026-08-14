import numpy as np
exec(open('causet.py').read().split('print("STEP 1')[0])
rng=np.random.default_rng(21)

def sprinkle_ESU(N,n_sphere,T):
    """Sprinkle into R x S^n (Einstein static universe) -- the conformal boundary geometry.
       Shilov boundary of D_IV^5 is S^4 x S^1  => n_sphere = 4, total dim = 5."""
    t=rng.uniform(0,T,N)
    x=rng.normal(size=(N,n_sphere+1)); x/=np.linalg.norm(x,axis=1)[:,None]
    return t,x

def relations_ESU(t,x):
    """a < b iff  t_b - t_a  >  geodesic distance on S^n  (ESU light cone)."""
    dt=t[None,:]-t[:,None]
    cos=np.clip(x@x.T,-1,1); dgeo=np.arccos(cos)
    return (dt>0)&(dt>dgeo)

print("="*74)
print("MEASURING THE COMMIT ORDER ON BST'S OWN OBJECT")
print("="*74)
print("The paper: contacts commit on the SHILOV BOUNDARY of D_IV^5 = S^4 x S^1.")
print("The commit operator generates the SO(2) time-circle; SO(5,2) acts conformally.")
print("=> the frame-invariant order is the CONFORMAL causal order of R x S^4 (Einstein static).")
print("   dim(S^4 x S^1) = 4 + 1 = 5.   *** that is a FIVE-dimensional causal structure ***")
print()
print("PRE-REGISTERED CALIBRATION (toy 5250, before this question arose):")
print("   d=2: r=0.4873   d=3: r=0.2318   d=4: r=0.1022   d=5: r=0.0331   KR: r=0.626, height 3")
print()
print("MEASURED on R x S^4 (the Shilov geometry):")
print("   N     T      ordering fraction r     height")
for N in [300,600,1200]:
    for T in [1.5]:
        t,x=sprinkle_ESU(N,4,T); R=relations_ESU(t,x)
        print("   %4d  %.1f    %.4f                 %d"%(N,T,ordering_fraction(R),height(R)))
print()
print("CONTROL -- same construction on R x S^(n) for n = 1,2,3 (total dim n+1):")
print("   n_sphere  total dim   r        height")
for ns in [1,2,3,4]:
    t,x=sprinkle_ESU(600,ns,1.5); R=relations_ESU(t,x)
    print("   %d         %d           %.4f   %d"%(ns,ns+1,ordering_fraction(R),height(R)))
