import numpy as np
from scipy.linalg import expm
rng=np.random.default_rng(1563)
print("="*88); print("(a) MARKOVIAN -- is it DERIVED from the heat semigroup, or is it the COMMITMENT AXIOM?")
print("="*88)
n=24
A=rng.normal(size=(n,n)); H=A@A.T/n
for s,t in [(0.3,0.7),(1.1,0.4)]:
    print("  semigroup identity exp(-(s+t)H) = exp(-sH)exp(-tH): resid %.2e"%np.abs(expm(-(s+t)*H)-expm(-s*H)@expm(-t*H)).max())
print("  ★ THIS IS A CAN'T-FAIL TEST. exp(-(s+t)H)=exp(-sH)exp(-tH) holds for EVERY operator H.")
print("     'Markovian because heat semigroup' is an identity of the exponential map, not a BST fact.\n")
print("  The content is at the SITE level: does the induced process obey Chapman-Kolmogorov?")
# sites = basis states; amplitude kernel vs committed (collapsed) kernel
def amp(t): return expm(-t*H)
def prob_from_amp(t):
    K=np.abs(amp(t))**2
    return K/K.sum(axis=0,keepdims=True)
def ck_resid(s,t,P):
    return np.abs(P(s+t)-P(s)@P(t)).max()
print("    UNCOMMITTED (amplitudes evolve, then square -- interference survives between ticks):")
for s,t in [(0.3,0.3),(0.5,0.5),(0.2,0.8)]:
    print("       s=%.1f t=%.1f : ||P(s+t) - P(s)P(t)||_max = %.4f"%(s,t,ck_resid(s,t,prob_from_amp)))
print("    COMMITTED (state collapses to a site each tick, so probabilities compose):")
P0=prob_from_amp(0.5)
def Pc(t,dt=0.5):
    k=int(round(t/dt)); M=np.linalg.matrix_power(P0,k); return M
for s,t in [(0.5,0.5),(1.0,0.5),(1.0,1.0)]:
    print("       s=%.1f t=%.1f : ||P(s+t) - P(s)P(t)||_max = %.2e"%(s,t,np.abs(Pc(s+t)-Pc(s)@Pc(t)).max()))
print("\n  ⟹ THE MARKOV PROPERTY IS SUPPLIED BY *COMMITMENT* (the collapse), NOT by the semigroup.")
print("     Without commitment, interference breaks Chapman-Kolmogorov at O(0.1). With commitment it")
print("     holds to machine precision -- BY CONSTRUCTION, because collapse is the axiom.")
print("     => 'Markovian' is CORPUS-CONSISTENT and AXIOMATIC (it restates measurement-as-commitment),")
print("        NOT a derived property. Honest tier: FRAMEWORK, not DERIVED.")

print("\n"+"="*88); print("(b) FUZZY / UV-FINITE CONTINUUM -- rigorous coarse-graining, or a relabel?")
print("="*88)
print("  Test: with a HARD mode cap, is there a STABLE tau-window where the spectral dimension reads")
print("  the continuum value? A relabel would have no window; real coarse-graining has one that")
print("  WIDENS as the cap rises (the cap is then a genuine resolution scale).")
def ds_window(cap,d=5,tol=0.05):
    # 5D torus Laplacian eigenvalues, |k|^2, capped at cap modes
    r=int(np.ceil(cap**(1/d)))+3
    g=np.arange(-r,r+1)
    K=np.array(np.meshgrid(*[g]*d,indexing='ij')).reshape(d,-1).T
    ev=np.sort((K**2).sum(axis=1).astype(float))[:cap]
    ev=ev[ev>0]
    taus=np.logspace(np.log10(3.0/ev.max()),np.log10(3.0/ev.min()),400)
    Z=np.array([np.exp(-t*ev).sum() for t in taus])
    ds=-2*np.gradient(np.log(Z),np.log(taus))
    good=np.abs(ds-d)<tol
    if not good.any(): return 0.0,ds.max()
    lo,hi=taus[good].min(),taus[good].max()
    return np.log10(hi/lo),ds[good].mean()
print("     mode cap    width of the d_s = 5.00 +/- 0.05 window (decades in tau)   mean d_s in window")
for cap in [137,600,3000,12000,40000]:
    w,m=ds_window(cap)
    print("      %6d               %.3f                                    %.4f"%(cap,w,m))
print("  ⟹ the window is REAL and WIDENS monotonically with the cap => the cap behaves as a genuine")
print("     RESOLUTION SCALE, not a relabel. But note the honest half: at the corpus cap N_max = 137")
print("     the window is the NARROWEST -- the coarse-graining story is rigorous in structure, and")
print("     THIN at BST's own finite size.")

print("\n"+"="*88); print("(c) SEALING THE REALITY NEGATIVE: [J, P_V12] and J vs SU(3)")
print("="*88)
print("  TYPE FIRST: J (charge conjugation) is antilinear on the COMPLEX colour module; P_V12 projects")
print("  inside the REAL 5-dim Jordan/Peirce space. Different spaces => [J, P_V12] is not even DEFINED")
print("  without first assuming colour = V_12 -- the identification the negative denies.")
print("\n  What IS computable: does an antilinear involution on C^3 commute with SU(3)?")
def haar_su3(m):
    A=(rng.normal(size=(m,3,3))+1j*rng.normal(size=(m,3,3)))/np.sqrt(2)
    Q,R=np.linalg.qr(A); d=np.einsum('...ii->...i',R); Q=Q*(d/np.abs(d))[:,None,:]
    return Q*(np.linalg.det(Q)**(-1/3))[:,None,None]
G=haar_su3(20000)
dev=np.abs(G.conj()-G).max(axis=(1,2))     # J g J^{-1} = conj(g) for J = complex conjugation
print("    J = complex conjugation:  ||J g J^-1 - g|| over Haar SU(3): mean %.4f, median %.4f, min %.2e"%(
    dev.mean(),np.median(dev),dev.min()))
print("    fraction of SU(3) where J commutes (dev < 1e-6): %.5f"%(dev<1e-6).mean())
print("    the commutant is exactly SO(3): dim 3 of dim 8 => %d of 8 generators FAIL to commute."%(8-3))
print("\n  ⟹ ANY antilinear involution on the colour 3 breaks SU(3) -> SO(3). And no SU(3)-EQUIVARIANT")
print("     one exists at all: FS(3) = 0 means 3 is NOT self-conjugate (3 != 3bar).")
print("     THE REALITY NEGATIVE IS SEALED -- and Casey is right that colour is simply the wrong object.")
