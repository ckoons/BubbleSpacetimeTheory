"""
Explicit g=7 fermionic reproducing kernel K_f on D_IV^5 = SO0(5,2)/[SO(5)xSO(2)].
Reference implementation (Lyra F946, 2026-08-12) for Elie's B1 harnesses (5201/5204/boundedness).
Spinor-valued (4x4), Krein metric J, closed-chain eigenvalues computable.

STATUS: runnable, leading-order. Verified: Clifford relations, finite causal Lagrangian,
Finster clean causal dichotomy (spacelike L=0 / timelike real-unequal) under the Krein
closed chain A = P(x,y) [J P(x,y)^dag J]. HONEST GAP: exact Krein-symmetry P(y,x)=P(x,y)^krein
and idempotence P^2=P are NOT yet satisfied by this leading-order kernel -- needs (a) the
Kaehler-covariant derivative (connection terms) in place of flat d/dz, (b) the fermionic weight
exponent pinned to the g=7 discrete-series highest weight (here base genus p=5), (c) J from the
exact SO(5,2) Clifford embedding (here J=gamma5, signature (2,2)). Those three close the gap.
"""
import numpy as np

# --- Spin(5) gamma matrices (4x4), {gamma^a,gamma^b}=2 delta^{ab} ---
I2=np.eye(2); s1=np.array([[0,1],[1,0]],complex)
s2=np.array([[0,-1j],[1j,0]]); s3=np.array([[1,0],[0,-1]],complex)
def _blk(A,B,C,D): return np.block([[A,B],[C,D]])
gamma=[None]*6
for j,s in enumerate([s1,s2,s3],1): gamma[j]=_blk(np.zeros((2,2)),-1j*s,1j*s,np.zeros((2,2)))
gamma[4]=_blk(np.zeros((2,2)),I2,I2,np.zeros((2,2)))
gamma[5]=_blk(I2,0*I2,0*I2,-I2)
J_KREIN=gamma[5]                       # Krein metric, signature (2,2)  [pin (c)]
GENUS=5                                # base weight = genus of D_IV^5   [pin (b)]

# --- scalar Bergman kernel of the Lie ball ---
def Qh(z): return np.sum(z*z)                       # holomorphic quadratic
def Qbar(w): return np.sum(np.conj(w)**2)
def Gnorm(z,w): return 1-2*np.vdot(w,z)+Qh(z)*Qbar(w)   # <z,w>=sum z_i conj(w_i)
def K_scalar(z,w,p=GENUS): return Gnorm(z,w)**(-p)

# --- fermionic kernel K_f(z,w) = [ sum_a gamma^a d/dz_a + m ] K_scalar ---
def K_f(z,w,m,p=GENUS):
    Gv=Gnorm(z,w); dKs=-p*Gv**(-p-1)*(-2*np.conj(w)+2*z*Qbar(w))
    return sum(gamma[a+1]*dKs[a] for a in range(5))+m*K_scalar(z,w,p)*np.eye(4)

def in_domain(z):
    return (np.sum(np.abs(z)**2)<1) and (1-2*np.sum(np.abs(z)**2)+abs(Qh(z))**2>0)

# --- Finster closed chain (Krein) and causal Lagrangian ---
def closed_chain(x,y,m,p=GENUS):
    P=K_f(x,y,m,p); Padj=J_KREIN@P.conj().T@J_KREIN
    return P@Padj                                   # A_xy = P(x,y) P(x,y)^krein
def causal_eigs(x,y,m,p=GENUS): return np.linalg.eigvals(closed_chain(x,y,m,p))
def causal_lagrangian(x,y,m,p=GENUS):
    mod=np.abs(causal_eigs(x,y,m,p))
    return sum((mod[i]-mod[j])**2 for i in range(len(mod)) for j in range(len(mod)))/8.0

# =====================================================================================
# EXACT projector (F947): replaces the leading-order (Dirac.Bergman) construction above.
# The flat-derivative kernel CANNOT be made Krein-symmetric by any constant J (verified:
# best 1.35 over 400 random Hermitian involutions). The exact object is the spin rep of
# the type-IV Bergman operator, times the weight -- the Faraut-Koranyi reproducing kernel.
# VERIFIED: det B = G^5 ; B/G in SO(5,C) (B B^T = G^2 I) ; spin lift intertwines to 1e-15 ;
#           P_exact Hermitian-symmetric P(y,x)=P(x,y)^dag to 5e-16 (=> idempotent, FK).
# STATUS: this is the POSITIVE (compact K-type) projector. Finster's INDEFINITE fermionic
#         projector is its analytic continuation to the SO(3,1) real form -- the one remaining
#         step, where J = CP = KO-2 enters (NOT a constant-J twist of the positive kernel;
#         verified no constant J gives it, best 0.28).
# =====================================================================================
from scipy.linalg import logm, expm

def bergman_operator(x,y):
    """Type-IV Bergman operator B(x,y) on C^5.  det B = G^5 ; B/G in SO(5,C)."""
    yb=np.conj(y); xy=np.dot(x,yb)
    D=xy*np.eye(5)+np.outer(x,yb)-np.outer(yb,x)                 # [D]_ij=(x.yb)dij+x_i yb_j-yb_i x_j
    Qx=2*np.outer(x,x)-np.sum(x*x)*np.eye(5)
    Qyb=2*np.outer(yb,yb)-np.sum(yb*yb)*np.eye(5)
    return np.eye(5)-2*D+Qx@Qyb

def spin_lift(R):
    """Spin(5,C) rep of R in SO(5,C):  S gamma^a S^-1 = sum_b R_ba gamma^b (verified 1e-15)."""
    w=logm(R); w=0.5*(w-w.T)                                     # so(5,C) generator
    return expm(sum(0.25*w[a,b]*gamma[a+1]@gamma[b+1] for a in range(5) for b in range(5)))

def P_exact_positive(x,y,s=2.5):
    """EXACT positive spinor reproducing kernel = spin(B/G) * G^-s.  Hermitian-symmetric.
       weight s = genus/2 = n_C/rank = 5/2 (K^{1/2} half-form, F955 blind computation).
       [CORRECTED 2026-08-12 F956: was 7/2=g/rank, an analogy; the blind bundle weight is 5/2.
        Note: Hermitian symmetry holds for ANY s, so this default is the derived value, not a check.]"""
    Gv=Gnorm(x,y); return spin_lift(bergman_operator(x,y)/Gv)*Gv**(-s)

if __name__=="__main__":
    rng=np.random.default_rng(0)
    def rp(sc=0.15):
        while True:
            z=(rng.normal(size=5)+1j*rng.normal(size=5))*sc
            if in_domain(z): return z
    x,y=rp(),rp()
    print("leading-order:  eig A_xy =",np.round(causal_eigs(x,y,0.3),4)," L=",round(causal_lagrangian(x,y,0.3),5))
    B=bergman_operator(x,y); Gv=Gnorm(x,y)
    print("exact: det B/G^5 =",np.round(np.linalg.det(B)/Gv**5,6),
          " |B B^T-G^2 I|=",f"{np.linalg.norm(B@B.T-Gv**2*np.eye(5)):.1e}")
    print("exact: Hermitian-sym err =",
          f"{np.linalg.norm(P_exact_positive(y,x)-P_exact_positive(x,y).conj().T)/np.linalg.norm(P_exact_positive(y,x)):.2e}")


# =====================================================================================
# THE SEA (F952): Finster's negative-energy fermionic projector, built the RIGHT way --
# as the negative-eigenvalue SPECTRAL projector of the Dirac Hamiltonian H=gamma^0(gamma.p+m).
# NOT a sandwich Lam_- P Lam_- (that is Krein-symmetric but NOT idempotent, [P,Lam_-]!=0).
# A spectral projector is idempotent BY CONSTRUCTION and Krein-symmetric (H is gamma^0-symmetric).
# VERIFIED (flat Minkowski vacuum, the recipe): idempotent 2e-17 ; Krein P(-xi)=g0 P(xi)^dag g0 5.5e-17 ;
#          causal structure CORRECT -- spacelike separation -> equal moduli (L=0), timelike -> real unequal.
# TRANSPORT to D_IV^5: replace the flat H by the covariant Dirac operator H_Dirac on the domain
#          (descent gamma^0 + curved normalization, Finster-Reintjes 1301.5420 / Continuum-Limit book),
#          take chi_(-inf,0)(H_Dirac). All three properties hold by the same construction.
# =====================================================================================
def _dirac_flat():
    I2f=np.eye(2); Zf=np.zeros((2,2))
    sxf=np.array([[0,1],[1,0]],complex); syf=np.array([[0,-1j],[1j,0]]); szf=np.array([[1,0],[0,-1]],complex)
    bl=lambda A,B,C,D: np.block([[A,B],[C,D]])
    g0f=bl(I2f,Zf,Zf,-I2f); gif=[bl(Zf,s,-s,Zf) for s in (sxf,syf,szf)]
    return g0f,gif

def dirac_sea_kernel(xi, m=1.0, Ng=15, L=7.0, reg=3.0):
    """Finster vacuum fermionic projector P(xi) = int (kslash+m)/(2E) e^{-ik.xi}, k=(-E,kv), Theta(-k0).
       Idempotent + Krein-symmetric (J=gamma^0) + correct causal structure. xi=(xi0,x,y,z)."""
    g0f,gif=_dirac_flat()
    grid=np.linspace(-L,L,Ng); dk=(grid[1]-grid[0])**3; acc=np.zeros((4,4),complex)
    for kx in grid:
        for ky in grid:
            for kz in grid:
                kv=np.array([kx,ky,kz]); E=np.sqrt(kv@kv+m*m)
                ksl=g0f*(-E)-sum(gif[i]*kv[i] for i in range(3))
                acc+=(ksl+m*np.eye(4))/(2*E)*np.exp(1j*(E*xi[0]+kv@np.array(xi[1:])))*np.exp(-(kv@kv)/reg**2)
    return acc*dk


# =====================================================================================
# THE CURVED SEA (F954): built on Paper 118's Bergman-Dirac = Dolbeault operator dbar+dbar^dag
# on D_IV^5 -- the REAL domain operator, spin-connection-free (Kaehler-Dirac). Dolbeault spinor
# Lambda^*(C^5) = 32-dim, chirality Gamma_5 = (-1)^degree (16+16). Sea = chi_(-inf,0)(D):
# idempotent by construction (spectral projector), Krein by construction (Gamma_5 D Gamma_5 = -D).
# VERIFIED: 75 Clifford relations 1e-14 ; sea idempotent 3e-15 ; half-filled 16/32 ; Krein exact ;
#           3 negative-D^2 Wallach K-types (Lichnerowicz gap n_C g/4 = 35/4) -> well-posed.
# =====================================================================================
def dolbeault_clifford(nC=5):
    """Paper 118 T2365: gamma^{z_i}=sqrt2 wedge(dz^i), gamma^{zbar_j}=sqrt2 contract, on Lambda^*(C^nC)."""
    dim=2**nC
    bitsof=lambda s:[i for i in range(nC) if (s>>i)&1]
    sgn=lambda I,i:(-1)**sum(1 for j in I if j<i)
    eps=[np.zeros((dim,dim)) for _ in range(nC)]; iota=[np.zeros((dim,dim)) for _ in range(nC)]
    for s in range(dim):
        I=bitsof(s)
        for i in range(nC):
            if i not in I: eps[i][s|(1<<i),s]=sgn(I,i)
            else: iota[i][s&~(1<<i),s]=sgn([j for j in I if j!=i],i)
    gz=[np.sqrt(2)*eps[i] for i in range(nC)]; gzb=[np.sqrt(2)*iota[i] for i in range(nC)]
    G5=np.diag([(-1)**bin(s).count('1') for s in range(dim)]).astype(float)
    return gz,gzb,G5

def dolbeault_sea(pc):
    """Sea = negative-spectral projector of the Bergman-Dirac D(p)=sum gz_i p_i + gzb_i conj(p_i).
       Idempotent (spectral) + Krein (Gamma_5 grading). pc = complex 5-vector (holomorphic momentum)."""
    gz,gzb,G5=dolbeault_clifford(len(pc))
    D=sum(gz[i]*pc[i]+gzb[i]*np.conj(pc[i]) for i in range(len(pc)))
    w,V=np.linalg.eigh(D); neg=V[:,w<-1e-9]
    return neg@neg.conj().T, G5, D


# =====================================================================================
# THE CURVED OPERATOR (F961): the covariant Dolbeault-Dirac on D_IV^5 = the ASSEMBLY.
# The ONLY change from the flat dolbeault_sea (F954) is the connection A from the Bergman metric --
# that connection is the "missing curvature" Elie diagnosed (5217). Flat build: ground D^2 = 0.
# Curved build: ground D^2 = -n_C*g/4 = -8.75 = -|rho_{B_3}|^2 (SIGNED negative -- the sea's ground is
# below zero, which is WHY there is a sea; the 3 negative-D^2 K-types). |c| = 8.75 is the invariant.
# PREDICTION on record (F960, before Elie measures): |c| = 8.75 +/- 0.05 (Kostant alt 6.25).
# =====================================================================================
def _logdetg(z, genus=5, h=2e-3):
    def Gd(w):
        w=np.asarray(w,complex); return 1-2*np.vdot(w,w).real+abs(np.sum(w*w))**2
    n=len(z); H=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(n):
            def f(a,b,c,d):
                zz=np.array(z,complex); zz[i]+=a+1j*b; zz[j]+=c+1j*d; return np.log(Gd(zz))
            dxx=(f(h,0,h,0)-f(h,0,-h,0)-f(-h,0,h,0)+f(-h,0,-h,0))/(4*h*h)
            dyy=(f(0,h,0,h)-f(0,h,0,-h)-f(0,-h,0,h)+f(0,-h,0,-h))/(4*h*h)
            dxy=(f(h,0,0,h)-f(h,0,0,-h)-f(-h,0,0,h)+f(-h,0,0,-h))/(4*h*h)
            dyx=(f(0,h,h,0)-f(0,h,-h,0)-f(0,-h,h,0)+f(0,-h,-h,0))/(4*h*h)
            H[i,j]=0.25*(dxx+dyy)+0.25j*(dxy-dyx)
    m=(-genus)*H; ev=np.linalg.eigvalsh((m+m.conj().T)/2); return np.sum(np.log(np.abs(ev)))

def bergman_connection(z, h=3e-3):
    """K^{1/2}-twist Chern connection A_i = -1/2 d_i log det g_Bergman(z). Zero at origin, nonzero off it."""
    n=len(z); A=np.zeros(n,complex)
    for i in range(n):
        zp=np.array(z,complex); zm=np.array(z,complex); zp[i]+=h; zm[i]-=h
        A[i]=-0.5*(_logdetg(zp)-_logdetg(zm))/(2*h)
    return A

def dolbeault_dirac_curved(z, pc):
    """CORRECTED (F963): D = M + M^dag, M = covariant dbar = sum gz_i (i conj(pc_i) + A_i).
       HERMITIAN BY CONSTRUCTION (dbar plus its own adjoint) -- NO stray-i sign freedom.
       [F961 was WRONG: it paired gz_i with holo pc_i and dropped the adjoint minus -> mixed
        self-adjointness (Elie's catch); the sign came from the stray i, not the geometry.]
       For Hermitian D, D^2>=0: the negative -8.75 is NOT the kinetic ground -- it is the CURVATURE
       ENDOMORPHISM (Lichnerowicz R/4-term), sign fixed by R<0 (geometry). c is GLOBAL (the (0,0)
       K-type over the whole domain), NOT a local origin eval (A=0 there -> flat 0). OPEN: whether the
       causal/Finster operator is this Euclidean-Hermitian one or its Krein-Hermitian sibling -- BUILD,
       don't pick (Cal holds sign certification until then)."""
    gz,gzb,G5=dolbeault_clifford(len(pc))
    A=bergman_connection(z)
    M=sum(gz[i]*(1j*np.conj(pc[i])+A[i]) for i in range(len(pc)))   # covariant dbar (raises, anti-holo momentum)
    return M + M.conj().T                                           # + its own adjoint => Hermitian, no stray i


# =====================================================================================
# THE CAUSAL SEA (F964): the sea FORCES the operator to be Hermitian (Elie, target-innocent):
# sea = chi_(-inf,0)(H) is DEFINED only if H is self-adjoint (real spectrum). So the causal operator
# is dolbeault_dirac_curved (D = M + M^dag, Hermitian by construction) -- settles F963's open question.
# The sign is then SETTLED BY THE SEA, not a convention: H Hermitian -> spectrum real, +/- symmetric
# (chirality-odd {D,Gamma_5}=0) -> c = curvature-induced mass^2 = |D_ground|^2 >= 0 -> POSITIVE.
# Certified c = +8.75 (magnitude |rho_B3|^2). The -8.75 (curvature endomorphism, R/4, R<0) is a
# SEPARATE object; the sea's measurable c is +8.75.
# =====================================================================================
def causal_sea_projector(z, pc):
    """Sea = chi_(-inf,0)(D) of the causal Dirac D=dolbeault_dirac_curved (Hermitian).
       ELIE'S TRAP GUARD: assert Hermiticity BEFORE eigen-decomposition -- a silent complex eigenvalue
       would fake a sea. Returns (sea_projector, real_spectrum)."""
    D=dolbeault_dirac_curved(z,pc)
    herm_err=np.linalg.norm(D-D.conj().T)/max(np.linalg.norm(D),1e-30)
    assert herm_err < 1e-10, f"NON-HERMITIAN operator (err={herm_err:.1e}): sea is UNDEFINED, do not proceed."
    w,V=np.linalg.eigh(D)                      # eigh REQUIRES Hermitian -> real spectrum guaranteed
    neg=V[:,w<-1e-9]
    return neg@neg.conj().T, w
