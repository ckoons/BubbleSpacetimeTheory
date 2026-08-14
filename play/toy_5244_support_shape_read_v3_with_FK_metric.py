import numpy as np, itertools, sys, time
from fractions import Fraction as F
A=F(3)
def poch(x,m):
    o=F(1)
    for j in range(m): o*=(x+j)
    return o
def fk(nu,lam): return poch(nu,lam[0])*poch(nu-A/2,lam[1])

def polyops(N,nu,n=5):
    basis=[a for a in itertools.product(range(N+1),repeat=n) if sum(a)<=N]
    idx={a:i for i,a in enumerate(basis)}; dim=len(basis); deg=np.array([sum(a) for a in basis])
    def bd(mu):
        M=np.zeros((dim,dim))
        for a,i in idx.items():
            b=list(a); b[mu]+=1; b=tuple(b)
            if b in idx: M[idx[b],i]=np.sqrt(b[mu])
        return M
    Bd=[bd(m) for m in range(n)]; B=[x.T for x in Bd]
    E=sum(Bd[m]@B[m] for m in range(n)); Q=sum(Bd[m]@Bd[m] for m in range(n)); Lap=Q.T; I=np.eye(dim)
    K=[2*Bd[m]@(E+float(nu)*I)-Q@B[m] for m in range(n)]
    P=[B[m] for m in range(n)]
    cols=[];gv=[];pd=[]
    for m in range(N+1):
        sub=np.nonzero(deg==m)[0]
        if m>=2:
            Ls=Lap[np.ix_(np.nonzero(deg==m-2)[0],sub)]
            _,s,vt=np.linalg.svd(Ls); H=vt[np.sum(s>1e-10):].T
        else: H=np.eye(len(sub))
        for k in range(0,(N-m)//2+1):
            C=np.zeros((dim,H.shape[1])); C[sub,:]=H
            Mk=np.linalg.matrix_power(Q,k)@C
            if Mk.shape[1]==0: continue
            u,s,_=np.linalg.svd(Mk,full_matrices=False); r=int(np.sum(s>1e-9))
            if not r: continue
            cols.append(u[:,:r]); gv+= [1.0/(2.0**(m+2*k)*float(fk(nu,(m+k,k))))]*r; pd += [m+2*k]*r
    U=np.hstack(cols); gv=np.array(gv); pd=np.array(pd); s=np.sqrt(gv)
    Kt=[(s[:,None]*(U.T@K[m]@U))/s[None,:] for m in range(5)]
    Pt=[(s[:,None]*(U.T@P[m]@U))/s[None,:] for m in range(5)]
    return Kt,Pt,pd,dim

def fermions(n=5):
    d=2**n; out=[]
    for i in range(n):
        M=np.zeros((d,d))
        for ket in range(d):
            if (ket>>i)&1: M[ket & ~(1<<i),ket]=(-1)**bin(ket&((1<<i)-1)).count('1')
        out.append(M)
    return out

def run(N,nu=F(5,2)):
    t0=time.time(); Kt,Pt,pd,pdim=polyops(N,nu); a=fermions()
    err=max(np.abs(Kt[m]-Pt[m].T).max() for m in range(5))
    q=np.array([bin(i).count('1') for i in range(32)])
    lab=[(q[f],pd[p]) for f in range(32) for p in range(len(pd))]
    tot=np.array([qq-dd for qq,dd in lab]); n_tot=len(lab)
    D=np.zeros((n_tot,n_tot))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    asym=np.abs(D-D.T).max()
    H=D@D
    res={}
    print(f"  N={N}: dim={n_tot}  ||K-P^T||_FK={err:.2e}  ||D-D^T||={asym:.2e}   [{time.time()-t0:.1f}s build]")
    sys.stdout.flush()
    allev=[]; ground=None
    for c in sorted(set(tot.tolist())):
        sel=np.nonzero(tot==c)[0]
        if len(sel)<1: continue
        Hs=H[np.ix_(sel,sel)]
        w,v=np.linalg.eigh(Hs)
        allev.append((c,w[0],len(sel)))
        j=int(np.argmax(np.abs(v[:,0])))
        if ground is None or w[0]<ground[1]: ground=(c,w[0],lab[sel[j]],len(sel))
    tau=min(x[1] for x in allev)
    print(f"        sector minima (q-d: tau_min, dim): "+", ".join(f"{c}:{w:.4f}({d})" for c,w,d in allev))
    print(f"        GLOBAL tau_min={tau:.10f}  in sector q-d={ground[0]}  ground state at (q={ground[2][0]}, d={ground[2][1]})")
    ev=np.linalg.eigvalsh(H)
    print(f"        spectrum max={ev[-1]:.2f}   #(|eig|<1e-9)={int(np.sum(np.abs(ev)<1e-9))}   [{time.time()-t0:.1f}s]")
    sys.stdout.flush()
    return dict(N=N,tau=float(tau),q=ground[2][0],d=ground[2][1],top=float(ev[-1]),
                ker=int(np.sum(np.abs(ev)<1e-9)),err=err,asym=asym,dim=n_tot)

if __name__=="__main__":
    print("=== SHAPE READ, v3 + FK metric G, sector-decomposed (D conserves q-d) ===")
    R=[run(N) for N in [3,4,5,6]]
    print()
    print("SHAPE SUMMARY")
    print("  N   dim   tau_min        ground(q,d)   max eig   kernel")
    for r in R:
        print("  %-3d %-5d %-14.10f (%d,%d)         %-9.2f %d"%(r['N'],r['dim'],r['tau'],r['q'],r['d'],r['top'],r['ker']))
