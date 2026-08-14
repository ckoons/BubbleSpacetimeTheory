"""
Lyra_assembled_dirac_operator_v3.py  -- 2026-08-14  (CORRECTS v2's 352-error)
================================================================================
v2 ERROR (root cause found): the ladder used p+ = z_mu (multiplication). That is
NOT the so(5,2) raising generator -- it does not close the algebra, and it made
the huge spurious kernel.

v3 FIX: p+ = the SPECIAL CONFORMAL generator K_mu = 2 z_mu (E + nu) - Q d_mu
        p- = the TRANSLATION generator      P_mu = d_mu
        (Q = sum z_j^2, E = Euler degree, nu = scaling dim).
VERIFIED: [K_mu, P_nu] = -2(delta_munu (E+nu) + M_munu)  closes so(5,2) EXACTLY
          (interior closure error 0.0), and [P,P]=[K,K]=0.

Dirac (Kostant cubic, equal-rank):
    D = sum_mu ( a_mu^dag (x) K_mu  +  a_mu (x) P_mu )   on  Lambda*(C^5) (x) C[z]
Requirements (Keeper): (1) full square D^2 = (A+A^dag)^2 [built as D@D, D Hermitian];
    (2) correct ladder [DONE: special conformal, closes so(5,2)];
    (3) R_p = real curvature, emerges from D^2 (NOT the SO(2) charge);
    (4) nu = 5/2, lambda = -1 GEOMETRY-FIXED [F982], posted blind.

*** THE ONE REMAINING INPUT (honest, scoped) ***
Reading the SHAPE requires the invariant (Bergman) inner product G, in which
K_mu = (P_mu)^dag.  G is NOT determined by raising from the vacuum: at every
degree d a NEW primitive SO(5) harmonic H_d appears whose Bergman norm is a fresh
rank-2 Gindikin/Faraut-Koranyi input.  Supply G via K264 (the Bergman-kernel
machinery), then the operator below is Hermitian and its spectrum is the shape.
Until G is supplied, do NOT symmetrize in the Fock metric -- that gives a negative
spectrum and a false kernel (learned the hard way, F983).
================================================================================
"""
import numpy as np
from itertools import product

def build_conformal(n=5, N=4, nu=2.5):
    basis=[a for a in product(range(N+1),repeat=n) if sum(a)<=N]
    idx={a:i for i,a in enumerate(basis)}; dim=len(basis)
    def z(mu):
        M=np.zeros((dim,dim))
        for a,i in idx.items():
            b=list(a); b[mu]+=1; b=tuple(b)
            if b in idx: M[idx[b],i]=1.0
        return M
    def d(mu):
        M=np.zeros((dim,dim))
        for a,i in idx.items():
            if a[mu]>0:
                b=list(a); b[mu]-=1; b=tuple(b); M[idx[b],i]=a[mu]
        return M
    Z=[z(m) for m in range(n)]; Dp=[d(m) for m in range(n)]
    E=sum(Z[m]@Dp[m] for m in range(n)); Q=sum(Z[m]@Z[m] for m in range(n))
    K=[2*Z[m]@(E+nu*np.eye(dim))-Q@Dp[m] for m in range(n)]   # p+ special conformal
    P=[Dp[m] for m in range(n)]                                # p- translation
    return K, P, basis, dim

def verify_closure(K, P, basis, n=5, N=4, nu=2.5):
    """[K_mu,P_nu] = -2(delta*(E+nu) + M_munu) on the interior. Returns max error."""
    dim=len(basis); idx={a:i for i,a in enumerate(basis)}
    def z(mu):
        M=np.zeros((dim,dim))
        for a,i in idx.items():
            b=list(a); b[mu]+=1; b=tuple(b)
            if b in idx: M[idx[b],i]=1.0
        return M
    def d(mu):
        M=np.zeros((dim,dim))
        for a,i in idx.items():
            if a[mu]>0:
                b=list(a); b[mu]-=1; b=tuple(b); M[idx[b],i]=a[mu]
        return M
    Z=[z(m) for m in range(n)]; Dp=[d(m) for m in range(n)]
    E=sum(Z[m]@Dp[m] for m in range(n))
    def Mmn(mu,nv): return Z[mu]@Dp[nv]-Z[nv]@Dp[mu]
    interior=[i for a,i in idx.items() if sum(a)<=N-2]; II=np.ix_(interior,interior)
    err=0.0
    for mu in range(n):
        for nv in range(n):
            lhs=K[mu]@P[nv]-P[nv]@K[mu]
            rhs=-2*((1.0 if mu==nv else 0.0)*(E+nu*np.eye(dim))+Mmn(mu,nv))
            err=max(err,np.max(np.abs((lhs-rhs)[II])))
    return err

def hermitian_dirac(K, P, G_bergman):
    """Build Hermitian D once the Bergman Gram G is supplied (K264).
       Orthonormalize: sqrtG, invsqrtG; Kt = sqrtG K invsqrtG so Kt^dag = Pt.
       REQUIRES a valid PSD G. Returns D (Hermitian) and D^2."""
    w,U=np.linalg.eigh(G_bergman)
    assert w[0] > -1e-9, "G not PSD -- supply the correct FK norms (K264)"
    sq=U@np.diag(np.sqrt(np.clip(w,0,None)))@U.T
    isq=U@np.diag([1/np.sqrt(x) if x>1e-12 else 0 for x in w])@U.T
    n=len(K)
    Kt=[sq@K[m]@isq for m in range(n)]; Pt=[sq@P[m]@isq for m in range(n)]
    # fermions
    fd=2**n; a=[]
    for i in range(n):
        Ai=np.zeros((fd,fd))
        for k in range(fd):
            if (k>>i)&1: Ai[k&~(1<<i),k]=(-1)**bin(k&((1<<i)-1)).count("1")
        a.append(Ai)
    D=np.zeros((fd*Kt[0].shape[0], fd*Kt[0].shape[0]))
    for m in range(n):
        D=D+np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    return D, D@D

if __name__=="__main__":
    K,P,basis,dim=build_conformal(N=4)
    print(f"v3 correct ladder (special conformal). dim={dim}")
    print(f"so(5,2) closure error (interior): {verify_closure(K,P,basis):.2e}  -> {'CLOSES' if verify_closure(K,P,basis)<1e-9 else 'FAILS'}")
    print("Requirement (2) ladder: FIXED + VERIFIED. (4) nu=5/2, lambda=-1: blind.")
    print("REMAINING: supply Bergman Gram G (FK norms of Q^j (x) H_k, K264) -> then")
    print("hermitian_dirac(K,P,G) is Hermitian and its spectrum is the SHAPE (Elie).")
    print("Do NOT read shape without G: Fock-metric symmetrization gives a false spectrum.")
