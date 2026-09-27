# INFERENCE instrument (R12): rho on a for SU(2,2) and SU(1,1), same normalization as the
# SU(1,1) subgroups exp(t (E_gamma + E_-gamma)) used for the lowest-K-type coefficients.
# rho(Y) = (1/2) * sum of positive eigenvalues of ad(Y) on g (= rho_g(Y)/2 in Benoist-Kobayashi II).
import numpy as np, itertools
def basis_su(p,q):
    n=p+q; J=np.diag([1]*p+[-1]*q).astype(complex); B=[]
    # real basis of su(p,q) = {X : X^* J + J X = 0, tr X = 0}; solve by brute force on gl(n,C) as R^{2n^2}
    M=[]
    for i,j in itertools.product(range(n),range(n)):
        for c in (1,1j):
            E=np.zeros((n,n),complex); E[i,j]=c; M.append(E)
    A=[]
    for E in M:
        C=E.conj().T@J+J@E; A.append(np.concatenate([C.real.ravel(),C.imag.ravel(),[np.trace(E).real,np.trace(E).imag]]))
    A=np.array(A).T; u,s,vt=np.linalg.svd(A); null=vt[(s>1e-9).sum():]
    return [sum(c*E for c,E in zip(v,M)) for v in null]
def rho(p,q,Y):
    B=basis_su(p,q); V=np.array([np.concatenate([b.real.ravel(),b.imag.ravel()]) for b in B]).T
    ad=np.array([np.linalg.lstsq(V,np.concatenate([(Y@b-b@Y).real.ravel(),(Y@b-b@Y).imag.ravel()]),rcond=None)[0] for b in B]).T
    ev=np.linalg.eigvals(ad).real; return 0.5*ev[ev>1e-9].sum(), len(B)
def X(n,pairs,ts):
    Y=np.zeros((n,n),complex)
    for (i,j),t in zip(pairs,ts): Y[i,j]=t; Y[j,i]=t
    return Y
print("SU(1,1) dim, rho(t=1):", rho(1,1,X(2,[(0,1)],[1.0]))[::-1], " expect dim 3, rho = 1")
for ts in [(1,0),(1,1),(2,1)]:
    r,d=rho(2,2,X(4,[(0,2),(1,3)],ts))
    print("SU(2,2) dim",d," t=",ts," rho=",round(r,6)," 3t1+t2 =",3*ts[0]+ts[1])
