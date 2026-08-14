import numpy as np, sys, time
rng=np.random.default_rng(101)

def make_ESU(N,ns=4,T=2.0):
    t=rng.uniform(0,T,N); x=rng.normal(size=(N,ns+1)); x/=np.linalg.norm(x,axis=1)[:,None]
    def fut(i,J):   # i < J
        return (t[J]-t[i]>0)&((t[J]-t[i])>np.arccos(np.clip(x[J]@x[i],-1,1)))
    def pas(i,J):   # J < i
        return (t[i]-t[J]>0)&((t[i]-t[J])>np.arccos(np.clip(x[J]@x[i],-1,1)))
    def sub(mid):   # full relation on a small subset
        dt=t[mid][None,:]-t[mid][:,None]
        dg=np.arccos(np.clip(x[mid]@x[mid].T,-1,1))
        return (dt>0)&(dt>dg)
    return t,fut,pas,sub

def make_MINK(N,d):
    P=[]
    while len(P)<N:
        m=8*N; tt=rng.uniform(0,1,m); xx=rng.uniform(-1,1,(m,d-1))
        r=np.linalg.norm(xx,axis=1); ok=(r<tt)&(r<1-tt)
        idx=np.nonzero(ok)[0][:N-len(P)]
        for i in idx: P.append(np.concatenate(([tt[i]],xx[i])))
    P=np.array(P[:N]); t=P[:,0]; X=P[:,1:]
    def s2(i,J): 
        dt=t[J]-t[i]; dx=X[J]-X[i]; return dt,dt**2-np.sum(dx**2,axis=1)
    def fut(i,J):
        dt,s=s2(i,J); return (dt>0)&(s>0)
    def pas(i,J):
        dt,s=s2(i,J); return (dt<0)&(s>0)
    def sub(mid):
        dt=t[mid][None,:]-t[mid][:,None]
        dx=X[mid][None,:,:]-X[mid][:,None,:]
        return (dt>0)&(dt**2-np.sum(dx**2,axis=2)>0)
    return t,fut,pas,sub

def interval_r(t,fut,pas,sub,N,minsize=60,cap=900,want=100,tries=20000):
    allJ=np.arange(N); order=np.argsort(t)
    lo=order[:max(1,N//6)]; hi=order[-max(1,N//6):]
    rs=[];sz=[]
    for _ in range(tries):
        a=int(rng.choice(lo)); b=int(rng.choice(hi))
        fa=fut(a,allJ)
        if not fa[b]: continue
        mid=np.nonzero(fa&pas(b,allJ))[0]
        if len(mid)<minsize: continue
        if len(mid)>cap: mid=mid[rng.choice(len(mid),cap,replace=False)]
        R=sub(mid); m=len(mid)
        rs.append(R.sum()/(m*(m-1)/2)); sz.append(m)
        if len(rs)>=want: break
    return np.array(rs),np.array(sz)

if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 20000
    print("REGION- AND PROCEDURE-MATCHED INTERVAL ESTIMATOR   (N=%d, identical pipeline for all)"%N)
    print("  geometry              intervals   median r    IQR              median |interval|")
    for name,mk in [("Minkowski d=3",lambda: make_MINK(N,3)),
                    ("Minkowski d=4",lambda: make_MINK(N,4)),
                    ("Minkowski d=5",lambda: make_MINK(N,5)),
                    ("BST commit (R x S^4)",lambda: make_ESU(N,4,2.0))]:
        t0=time.time(); t,fut,pas,sub=mk()
        rs,sz=interval_r(t,fut,pas,sub,N)
        if len(rs):
            q1,q3=np.percentile(rs,[25,75])
            print("  %-21s %4d        %.4f     [%.4f, %.4f]   %d      [%.0fs]"%(
                name,len(rs),np.median(rs),q1,q3,int(np.median(sz)),time.time()-t0))
        else:
            print("  %-21s    0        (no intervals >= minsize)"%name)
        sys.stdout.flush()
