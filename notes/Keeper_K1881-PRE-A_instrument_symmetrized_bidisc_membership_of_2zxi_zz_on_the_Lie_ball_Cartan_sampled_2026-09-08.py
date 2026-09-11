import numpy as np
from scipy.stats import special_ortho_group as SO
rng=np.random.default_rng(11)
def in_lie_ball(z):
    zz=z@z; n=np.vdot(z,z).real
    return abs(zz)<1 and 1-2*n+abs(zz)**2>0
def sample():
    # polydisc point: z=(z1,z2,0,0,0), a=z1+i z2, b=z1-i z2 with a,b in the disc; then rotate by Haar SO(5) and a phase
    a=np.sqrt(rng.uniform())*np.exp(1j*rng.uniform(0,2*np.pi)); b=np.sqrt(rng.uniform())*np.exp(1j*rng.uniform(0,2*np.pi))
    z=np.array([(a+b)/2,(a-b)/(2j),0,0,0]); k=SO.rvs(5,random_state=rng); return k@z
N=20000; worst=0; cnt=0; ok=0
for _ in range(N):
    z=sample(); assert in_lie_ball(z), "sampler left the ball"
    r=np.roots([1,-2*z[0],z@z]); m=max(abs(r)); worst=max(worst,m); ok+= m<=1+1e-9
print("Cartan-sampled Lie ball points:",N," in closed symmetrized bidisc:",ok/N," worst max|root|:",worst)
# targeted: rotate the polydisc point so that xi is far from the slice, a,b near the boundary
a=0.99*np.exp(1j*0.3); b=0.99*np.exp(1j*2.1); z0=np.array([(a+b)/2,(a-b)/(2j),0,0,0])
worst=0
for _ in range(20000):
    z=SO.rvs(5,random_state=rng)@z0; r=np.roots([1,-2*z[0],z@z]); worst=max(worst,max(abs(r)))
print("a,b at 0.99 modulus, all rotations: worst max|root| =",worst)
