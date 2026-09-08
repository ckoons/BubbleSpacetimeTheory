"""Shared numerics for R133: harmonic polynomials on S^4 as monomial coefficient vectors, exact S^4 moments, Gegenbauer sampling."""
import itertools, math, numpy as np
from fractions import Fraction as F
from scipy.special import eval_gegenbauer, gammaln
D=5
def mono_list(k): return [e for e in itertools.product(range(k+1), repeat=D) if sum(e)==k]
MONO={}; IDX={}
def monos(k):
    if k not in MONO: MONO[k]=mono_list(k); IDX[k]={e:i for i,e in enumerate(MONO[k])}
    return MONO[k]
_mom={}
def moment(alpha):
    """∫_{S^4} x^alpha dσ normalised, exact-as-float."""
    if alpha in _mom: return _mom[alpha]
    if any(a%2 for a in alpha): v=0.0
    else:
        lg=gammaln(D/2)+sum(gammaln((a+1)/2) for a in alpha)-D*gammaln(0.5)-gammaln((sum(alpha)+D)/2); v=math.exp(lg)
    _mom[alpha]=v; return v
_G={}
def gram(k):
    if k not in _G:
        ms=monos(k); G=np.zeros((len(ms),len(ms)))
        for i,a in enumerate(ms):
            for j,b in enumerate(ms): G[i,j]=moment(tuple(x+y for x,y in zip(a,b)))
        _G[k]=G
    return _G[k]
def ip(p,q,k): return p@gram(k)@q
def mult_lin(u,p,k):
    """(u.x) * p, p of degree k -> degree k+1"""
    ms=monos(k); out=np.zeros(len(monos(k+1))); idx=IDX[k+1]
    for i,a in enumerate(ms):
        if p[i]==0: continue
        for d in range(D):
            b=list(a); b[d]+=1; out[idx[tuple(b)]]+=u[d]*p[i]
    return out
def lap_mat(k):
    """Laplacian: degree k -> degree k-2"""
    ms=monos(k); mt=monos(k-2); L=np.zeros((len(mt),len(ms))); idx=IDX[k-2]
    for i,a in enumerate(ms):
        for d in range(D):
            if a[d]>=2:
                b=list(a); b[d]-=2; L[idx[tuple(b)],i]+=a[d]*(a[d]-1)
    return L
def r2_mat(k):
    """multiplication by r^2: degree k-2 -> degree k"""
    mt=monos(k-2); ms=monos(k); R=np.zeros((len(ms),len(mt))); idx=IDX[k]
    for i,a in enumerate(mt):
        for d in range(D):
            b=list(a); b[d]+=2; R[idx[tuple(b)],i]+=1
    return R
_LR={}
def harmonic_part(p,k):
    if k<2: return p
    if k not in _LR: L=lap_mat(k); _LR[k]=(L, L@r2_mat(k))
    L,LR=_LR[k]; q,*_=np.linalg.lstsq(LR, L@p, rcond=None); return p - r2_mat(k)@q
def deriv(u,p,k):
    """directional derivative u.∇ p: degree k -> k-1"""
    ms=monos(k); out=np.zeros(len(monos(k-1))); idx=IDX[k-1]
    for i,a in enumerate(ms):
        if p[i]==0: continue
        for d in range(D):
            if a[d]>=1:
                b=list(a); b[d]-=1; out[idx[tuple(b)]]+=u[d]*a[d]*p[i]
    return out
def zonal(k):
    p=np.zeros(len(monos(k))); p[IDX[k][(k,0,0,0,0)]]=1.0; return harmonic_part(p,k)
def zonal_weight(Y,k):
    Z=zonal(k); return ip(Y,Z,k)**2/(ip(Y,Y,k)*ip(Z,Z,k))
def sample_dirs(kenv, n, rng):
    """u ~ |Z_kenv(u)|^2 dσ on S^4 (kenv=0 -> Haar). cos θ = u·ξ, marginal ∝ C_k^{3/2}(cos θ)^2 sin^3 θ."""
    th=np.linspace(0,np.pi,20001); dens=np.sin(th)**3*(eval_gegenbauer(kenv,1.5,np.cos(th))**2 if kenv>0 else 1.0)
    cdf=np.cumsum(dens); cdf/=cdf[-1]; t=np.interp(rng.uniform(size=n), cdf, th)
    v=rng.normal(size=(n,4)); v/=np.linalg.norm(v,axis=1)[:,None]
    return np.column_stack([np.cos(t), np.sin(t)[:,None]*v]), t
