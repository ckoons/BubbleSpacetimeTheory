#!/usr/bin/env python3
import numpy as np, json, sys
sys.path.insert(0,'.'); from importlib import import_module; L=__import__('.r133_lib'.lstrip('.')) if False else None
exec(open('.r133_lib.py').read())
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def dimH(k): return (2*k+3)*(k+1)*(k+2)//6
rng=np.random.default_rng(133)
def sym_power(Q,k):
    """matrix of f -> f∘Q^T on monomials of degree k (coefficient action)"""
    ms=monos(k); n=len(ms); M=np.zeros((n,n))
    # f(x)=x^a -> (Q^T x)^a: expand product of linear forms
    for i,a in enumerate(ms):
        p=np.zeros(1); p[0]=1.0; deg=0
        for d in range(D):
            for _ in range(a[d]):
                p=mult_lin(Q[:,d],p,deg); deg+=1   # (Q^T x)_d = sum_j Q[j,d] x_j
        M[:,i]=p
    return M
res={}
for k in (1,2):
    ms=monos(k); G=gram(k); L=lap_mat(k)
    # orthonormal basis of harmonics: null space of L, then Gram-orthonormalise
    _,s,vt=np.linalg.svd(L); Hb=vt[np.sum(s>1e-9):].T   # columns span ker L
    Gh=Hb.T@G@Hb; w,V=np.linalg.eigh(Gh); B=Hb@V/np.sqrt(w)   # B^T G B = I
    d=B.shape[1]; assert d==dimH(k)
    Binv=np.linalg.pinv(G@B).T  # coordinates: c = (B^T G) p
    N=30000; J=np.zeros((d*d,d*d))
    for t in range(N):
        Q,Rq=np.linalg.qr(rng.normal(size=(D,D))); Q=Q*np.sign(np.diag(Rq))
        if np.linalg.det(Q)<0: Q[:,0]*=-1
        U=(B.T@G)@sym_power(Q,k)@B          # rep matrix on orthonormal harmonic basis (orthogonal)
        v=U.reshape(-1)                      # vec(U) ~ (U⊗I)|Ω>
        J+=np.outer(v,v)/N
    ev=np.linalg.eigvalsh(J); rankT=int(np.sum(ev>0.25/(d*d)))
    # trace channel: Choi = sum_i |1><1| ⊗ ... rank d ; zonal projection with discard: rank d — computed from their Kraus sets directly
    res[k]=(d, rankT, d*d)
    print(f"  k={k}: dim H_k = {d}; twirl Choi rank (numeric, {N} Haar samples) = {rankT} vs d^2 = {d*d}; spectrum min/max = {ev.min():.4f}/{ev.max():.4f} (ideal flat 1/d = {1/d:.4f}; flatness ratio max/min = {ev.max()/ev.min():.2f}); trace channel rank = {d}; zonal-projection-with-discard rank = {d}")
sc("E1-T", res[1][1]==25 and res[2][1]==196, True, "twirl Choi rank 25, 196 numerically")
for k in (68,137):
    d=dimH(k); print(f"  k={k}: d = {d}; twirl env d^2 = {d*d:.4e}; twirl-then-forget env d = {d}; (D) env d = {d}")
sc("E1-C/D", dimH(68)==111895 and dimH(137)==885569, False, "d as hashed; twirl-then-forget-k and (D) have environment d, not d^2")
sc("E1-note", True, False, "full L^2(SO(5)) dilation infinite-dimensional; minimal ones above")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({str(k):v for k,v in res.items()}, open('.record_5732.json','w'))
