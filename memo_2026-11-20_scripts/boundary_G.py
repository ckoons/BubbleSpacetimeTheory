import numpy as np, math
rng=np.random.default_rng(20261120)
def split(X,n): return X[...,:n]+1j*X[...,n:]
def Hmat(X,n):                       # compact Kaehler metric, potential log(1+2|z|^2+|z.z|^2)
    z=split(X,n); q=(z*z).sum(-1); F=1+2*(abs(z)**2).sum(-1)+abs(q)**2
    Fj=2*z.conj()+2*q.conj()[...,None]*z            # dF/dz_j
    Fjk=2*np.eye(n)+4*z[...,:,None]*z.conj()[...,None,:]
    return Fjk/F[...,None,None]-Fj[...,:,None]*Fj.conj()[...,None,:]/F[...,None,None]**2, F
def Gmat(X,n):
    H,_=Hmat(X,n); M=H.conj(); A,B=M.real,M.imag
    return np.block([[A,-B],[B,A]]) if False else np.concatenate([np.concatenate([A,-B],-1),np.concatenate([B,A],-1)],-2)
def scalar_curv_origin(n,e=1e-3):
    d=2*n; X0=np.zeros(d); g0=Gmat(X0,n); gi=np.linalg.inv(g0)
    def G(x): return Gmat(x,n)
    D2=np.zeros((d,d,d,d))                        # D2[a,b] = d_a d_b g
    for a in range(d):
        for b in range(d):
            ea=np.eye(d)[a]*e; eb=np.eye(d)[b]*e
            D2[a,b]=(G(ea+eb)-G(ea-eb)-G(-ea+eb)+G(-ea-eb))/(4*e*e)
    R=0.5*(np.einsum('jkil->ijkl',D2)+np.einsum('iljk->ijkl',D2)-np.einsum('ikjl->ijkl',D2)-np.einsum('jlik->ijkl',D2))
    Ric=np.einsum('il,ijkl->jk',gi,R); return -np.einsum('jk,jk',gi,Ric), np.abs(G(np.eye(d)[0]*e)-G(-np.eye(d)[0]*e)).max()
def run(n, h, gradh, rofw, N, label):
    d=2*n
    W=rng.normal(size=(N,d)); W/=np.linalg.norm(W,axis=1,keepdims=True)
    if d==2: th=np.linspace(0,2*np.pi,N,endpoint=False); W=np.stack([np.cos(th),np.sin(th)],1)
    r=rofw(W); P=W*r[:,None]
    def nu_out(X):
        G=Gmat(X,n); gi=np.linalg.inv(G); dh=gradh(X)
        v=-np.einsum('...ij,...j->...i',gi,dh); return v/np.sqrt(np.einsum('...i,...i->...',dh,-v))[...,None], np.sqrt(np.linalg.det(G))
    e=1e-5; div=np.zeros(N); _,sq0=nu_out(P)
    for i in range(d):
        E=np.zeros(d); E[i]=e
        vp,sp=nu_out(P+E); vm,sm=nu_out(P-E)
        div+=(sp*vp[:,i]-sm*vm[:,i])/(2*e)
    L=div/sq0                                       # L_aa = div_g(outward normal)
    G=Gmat(P,n); gi=np.linalg.inv(G); dh=gradh(P)
    gradnorm=np.sqrt(np.einsum('...i,...ij,...j->...',dh,gi,dh)); drh=np.abs((dh*W).sum(1))
    dA=gradnorm*sq0*r**(d-1)/drh
    Sarea=2*np.pi**(d/2)/math.gamma(d/2)
    IL=Sarea*np.mean(L*dA); Area=Sarea*np.mean(dA)
    t,wq=np.polynomial.legendre.leggauss(40)
    vol=0
    for tk,wk in zip(t,wq):
        s=(tk+1)/2*r; vol+=wk*r/2*np.sqrt(np.linalg.det(Gmat(W*s[:,None],n)))*s**(d-1)
    Vol=Sarea*np.mean(vol)
    tau,firstderiv=scalar_curv_origin(n)
    se=Sarea*np.std(L*dA)/np.sqrt(N)
    print(f"[{label}] tau={tau:.6f} (|dG| at origin {firstderiv:.1e})  Vol={Vol:.6g}  Area={Area:.6g}  INT L dA={IL:.6g} +- {se:.2g}")
    return tau,Vol,IL,se
# ---- validation: spherical cap |z|<a in CP^1 ; expect INT tau + 2 INT L = 4 pi
for a in (0.5,1.0,2.0):
    tau,Vol,IL,_=run(1, None, lambda X: -2*X, lambda W: np.full(len(W),a), 2000, f"cap a={a}")
    print(f"   Gauss-Bonnet check: INT tau + 2 INT L = {tau*Vol+2*IL:.6f}  vs 4pi = {4*np.pi:.6f}")
# ---- Einstein check: det H * F^n constant?
n=5; Xs=rng.normal(size=(5,10))*0.3; H,F=Hmat(Xs,n); print("det H * F^5 at 5 random points:",np.round((np.linalg.det(H).real*F**5),8))
# ---- D_IV^5 inside Q^5
def gradh(X):
    z=split(X,5); q=(z*z).sum(-1)
    gx=-4*X[...,:5]+4*(q.conj()[...,None]*z).real; gy=-4*X[...,5:]-4*(q.conj()[...,None]*z).imag
    return np.concatenate([gx,gy],-1)
def rD(W):
    z=split(W,5); q2=abs((z*z).sum(-1))**2
    s=np.where(q2>1e-12,(1-np.sqrt(np.clip(1-q2,0,None)))/np.where(q2>1e-12,q2,1),0.5); return np.sqrt(s)
res=[run(5,None,gradh,rD,40000,f"D_IV^5 batch {k}") for k in range(3)]
tau=res[0][0]; Vol=np.mean([x[1] for x in res]); IL=np.mean([x[2] for x in res]); se=np.std([x[2] for x in res])/np.sqrt(3)
rho=2*IL/(tau*Vol)
print(f"\nrho = 2 INT L / INT tau = {rho:.5f}  (spread across batches gives INT L +- {se:.2g})")
print("PASS window [5.2e-4, 7.8e-4]:", 5.2e-4<=rho<=7.8e-4, f"; implied G shift = {100*(1/(1+rho)-1):+.3f}%  (target -0.065%)")
