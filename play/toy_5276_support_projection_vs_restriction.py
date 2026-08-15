import numpy as np
rng=np.random.default_rng(2564)
def cdim(P,rs,nmax=3000):
    P=P[:nmax]; D=np.linalg.norm(P[None,:,:]-P[:,None,:],axis=2)
    d=D[np.triu_indices(len(P),1)]
    C=np.array([(d<r).mean() for r in rs]); ok=C>0
    return np.polyfit(np.log(rs[ok]),np.log(C[ok]),1)[0]
N=3000; rs=np.exp(np.linspace(np.log(0.06),np.log(0.30),12))
x=rng.normal(size=(N,5)); x/=np.linalg.norm(x,axis=1)[:,None]
proj=x[:,:4]
# controls
ball=rng.normal(size=(N,4)); ball/=np.linalg.norm(ball,axis=1)[:,None]
ball*=rng.uniform(0,1,(N,1))**0.25                     # uniform in the unit 4-ball
s3=rng.normal(size=(N,4)); s3/=np.linalg.norm(s3,axis=1)[:,None]
print("CORRELATION DIMENSION (same estimator, same window -- region-matched controls):")
print("   S^4                                  %.4f"%cdim(x,rs))
print("   PROJECTION of S^4 along the axis     %.4f"%cdim(proj,rs))
print("   control: uniform unit 4-BALL         %.4f"%cdim(ball,rs))
print("   control: S^3                         %.4f"%cdim(s3,rs))
print("   note: the projected measure has an integrable rim singularity (density ~ 1/sqrt(1-|y|^2)),")
print("         which biases the estimator DOWN toward 3 -- so I do not lean on the estimator alone.")
print()
print("AC(0) COUNTING TEST (no estimator, decisive on the SUPPORT):")
M=400000
z=rng.normal(size=(M,5)); z/=np.linalg.norm(z,axis=1)[:,None]
r=np.linalg.norm(z[:,:4],axis=1)
for c in [0.9,0.7,0.5]:
    print("   fraction of projected points with |y| < %.1f  (INTERIOR of the ball) = %.4f"%(c,(r<c).mean()))
print("   if the projection landed on S^3, every one of these fractions would be 0.")
print("   => the image of S^4 under the projection is the SOLID 4-BALL. Dimension NOT reduced. 4 -> 4.")
