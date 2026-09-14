"""r145_eb_lib — Elie's per-bin Ellis–Baldwin instrument for Part B (Rounds 145–146). Synthetic-only until the gate says OPEN.
Every run prints this file's sha256. Nothing here reads a catalogue."""
import math, hashlib
import numpy as np
from scipy.integrate import quad
C_KMS=299792.458
def lib_hash(): return hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]
# ---------------- sky geometry ----------------
def lb_to_vec(l,b):
    l=np.radians(l); b=np.radians(b); return np.stack([np.cos(b)*np.cos(l),np.cos(b)*np.sin(l),np.sin(b)],-1)
def vec_to_lb(v):
    v=np.atleast_2d(v); l=np.degrees(np.arctan2(v[:,1],v[:,0]))%360; b=np.degrees(np.arcsin(np.clip(v[:,2]/np.linalg.norm(v,axis=1),-1,1))); return l,b
class Cells:
    """equal-area cells: rings uniform in sin b, cells uniform in l within a ring."""
    def __init__(self,n_rings=48,per_ring_eq=96):
        edges=np.linspace(-1,1,n_rings+1); self.rows=[]
        for j in range(n_rings):
            s0,s1=edges[j],edges[j+1]; bc=math.asin((s0+s1)/2); m=max(1,int(round(per_ring_eq*math.cos(bc)))); self.rows.append((s0,s1,m))
        self.offsets=np.cumsum([0]+[m for _,_,m in self.rows]); self.n=int(self.offsets[-1])
        self.area=np.concatenate([np.full(m,2*math.pi*(s1-s0)/m) for s0,s1,m in self.rows])
        ctr=[]
        for s0,s1,m in self.rows:
            bc=math.asin((s0+s1)/2)
            for k in range(m): ctr.append((2*math.pi*(k+0.5)/m,bc))
        ctr=np.array(ctr); self.center=np.stack([np.cos(ctr[:,1])*np.cos(ctr[:,0]),np.cos(ctr[:,1])*np.sin(ctr[:,0]),np.sin(ctr[:,1])],-1)
        self.ring_edges=edges; self._m=np.array([r[2] for r in self.rows])
    def index(self,v):
        s=np.clip(v[:,2],-1,1-1e-12); j=np.minimum(np.searchsorted(self.ring_edges,s,side='right')-1,len(self.rows)-1)
        m=self._m[j]; l=np.arctan2(v[:,1],v[:,0])%(2*math.pi); return self.offsets[j]+np.minimum((l/(2*math.pi)*m).astype(int),m-1)
CELLS=Cells()
def make_mask(b_cut=30.0,exclusions=((280.5,-32.9,5.0),(302.8,-44.3,3.0))):
    ok=np.abs(np.degrees(np.arcsin(CELLS.center[:,2])))>b_cut
    for l,b,r in exclusions: ok&=(CELLS.center@lb_to_vec(l,b))<math.cos(math.radians(r))
    return ok
# ---------------- two dipole estimators ----------------
def dipole_ls(n,mask):
    """Elie's: weighted linear LS of cell counts n_c = A_c [a + b.n_c] on unmasked cells; D = b/a; Poisson-LS covariance."""
    A=CELLS.area[mask]; X=np.column_stack([A,A[:,None]*CELLS.center[mask]]); y=n[mask].astype(float); N=y.sum()
    a0=N/A.sum(); w=1/(A*a0); XtW=X.T*w; G=XtW@X; p=np.linalg.solve(G,XtW@y); a,b=p[0],p[1:]; D=b/a
    covp=np.linalg.inv(G); J=np.zeros((3,4)); J[:,0]=-b/a**2; J[:,1:]=np.eye(3)/a; return D,J@covp@J.T
def dipole_unitvec(n,mask,nmock=1000,rng=None):
    """Cal's frozen 4.1: D = (3/N) sum n_hat over sources, minus the mask-mode correction (the same estimator on a uniform sky under the
    same mask), covariance from nmock isotropic Poisson mocks under the same mask and N."""
    rng=rng or np.random.default_rng(0); c=CELLS.center[mask]; A=CELLS.area[mask]; y=n[mask].astype(float); N=y.sum()
    corr=3*(A@c)/A.sum()                                         # uniform sky under the mask
    D=3*(y@c)/N-corr
    p=A/A.sum(); mocks=rng.multinomial(int(N),p,size=nmock).astype(float); Dm=3*(mocks@c)/N-corr
    return D,np.cov(Dm.T)
# ---------------- Neyman interval (full-covariance MC) ----------------
NEY_RNG=np.random.default_rng(8917)
def neyman(obs,covD,u,nsim=4000,ngrid=80):
    L=np.linalg.cholesky(covD); smax=math.sqrt(np.trace(covD)); grid=np.linspace(0,obs+6*smax,ngrid); noise=NEY_RNG.normal(size=(nsim,3))@L.T
    lo=np.empty(ngrid); hi=np.empty(ngrid)
    for k,Dt in enumerate(grid):
        amp=np.linalg.norm(Dt*u+noise,axis=1); lo[k],hi[k]=np.percentile(amp,[2.5,97.5])
    idx=np.where((lo<=obs)&(obs<=hi))[0]; Dlo,Dhi=(grid[idx[0]],grid[idx[-1]]) if len(idx) else (obs,obs)
    if Dlo==0: cone=180.0
    else:
        sim=Dlo*u+noise; sim/=np.linalg.norm(sim,axis=1)[:,None]; cone=float(np.percentile(np.degrees(np.arccos(np.clip(sim@u,-1,1))),95))
    return Dlo,Dhi,cone
# ---------------- per-bin ingredients ----------------
def measure_x(S,S_lim):
    """N(>S) ∝ S^-x at the limit: slope over [S_lim, 2 S_lim]."""
    return float(math.log((S>=S_lim).sum()/max((S>=2*S_lim).sum(),1))/math.log(2))
def membership_term(z_obs_all,z1,z2,N_bin,win=0.05):
    """T_i = [(1+z2) n(z2) - (1+z1) n(z1)] / N_i with n = dN/dz from the OBSERVED-redshift histogram in a ±win window at each edge
    (von Hausegger–Dalang bin-membership term, first order in beta; derived in the 5758 prereg)."""
    def dens(ze):
        if ze<=0 or not np.isfinite(ze): return 0.0
        return float(((z_obs_all>=ze-win)&(z_obs_all<ze+win)).sum()/(2*win))
    return ((1+z2)*dens(z2)-(1+z1)*dens(z1))/N_bin if np.isfinite(z2) else (-(1+z1)*dens(z1))/N_bin
def comoving(z,H0=67.4,Om=0.315):
    c=C_KMS; return c/H0*quad(lambda zz: 1/math.sqrt(Om*(1+zz)**3+1-Om),0,z)[0]
def profile_w(zmed):
    chi=np.array([comoving(z) for z in zmed]); return (chi[0]/chi)**2
# ---------------- the joint fit: Cal 4.2, linear in the two vectors ----------------
def joint_fit(Ds,Cs,coef,w):
    """D_i = coef_i * b + w_i * a, b = beta u, a = A w_hat; weighted LS with per-bin covariances; returns b, a, cov(6x6), chi2."""
    W=[np.linalg.inv(C) for C in Cs]; G=np.zeros((6,6)); r=np.zeros(6)
    for i in range(len(Ds)):
        J=np.hstack([coef[i]*np.eye(3),w[i]*np.eye(3)]); G+=J.T@W[i]@J; r+=J.T@W[i]@Ds[i]
    cov=np.linalg.inv(G); p=cov@r; b,a=p[:3],p[3:]
    chi2=sum((Ds[i]-coef[i]*b-w[i]*a)@W[i]@(Ds[i]-coef[i]*b-w[i]*a) for i in range(len(Ds)))
    return b,a,cov,chi2
def fit_summary(b,a,cov):
    beta=np.linalg.norm(b); u=b/beta; sb=math.sqrt(max(u@cov[:3,:3]@u,0)); A=np.linalg.norm(a); wa=a/A if A>0 else a; sA=math.sqrt(max(wa@cov[3:,3:]@wa,0)) if A>0 else math.sqrt(np.trace(cov[3:,3:])/3)
    return beta,sb,u,A,sA
# ---------------- synthetic skies ----------------
def synth_sky(N_gen,beta,vhat,rng,z_edges_gen,x_gen,alpha,S_lim=1.0,S_min=None,zdist='gamma',boost_z=True,D_int=None,int_dir=None,int_scale=0.5):
    """isotropic population; PHYSICAL boost: aberration + Doppler flux boost + (optionally) observed redshift 1+z_obs = (1+z)/delta.
    x is set per GENERATING bin (true z); flux N(>S) ∝ S^-x. Returns observed directions, TRUE z, OBSERVED z, observed flux."""
    S_min=S_min or S_lim/1.5; g=1/math.sqrt(1-beta**2)
    if zdist=='gamma':
        z=rng.gamma(3.0,0.55,size=int(N_gen*1.05)); z=z[z<4.0][:N_gen]
    else:
        z=rng.uniform(z_edges_gen[0],z_edges_gen[-1],N_gen)
    m=len(z); n=rng.normal(size=(m,3)); n/=np.linalg.norm(n,axis=1)[:,None]
    if D_int is not None:
        amp=D_int*np.exp(-z/int_scale); keep=rng.uniform(size=m)<(1+amp*(n@int_dir))/(1+amp); n=n[keep]; z=z[keep]; m=len(z)
    xb=np.array(x_gen)[np.clip(np.searchsorted(z_edges_gen,z,side='right')-1,0,len(x_gen)-1)]
    S=S_min*rng.uniform(size=m)**(-1/xb)
    z_obs=z.copy()
    if beta>0:
        mu=n@vhat; delta=g*(1+beta*mu)
        n=(n+((g-1)*mu+g*beta)[:,None]*vhat)/(g*(1+beta*mu))[:,None]
        S=S*delta**(1+alpha)
        if boost_z: z_obs=(1+z)/delta-1
    cut=S>=S_lim; return n[cut],z[cut],z_obs[cut],S[cut]
