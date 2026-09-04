import itertools, random
from retention import colourings, adj_of, classes, kempe_moves
random.seed(3)
def tv(p,r):
    ks=set(p)|set(r); return 0.5*sum(abs(p.get(k,0)-r.get(k,0)) for k in ks)

def study(name,n,edges,q,S,steps=60):
    cols=colourings(n,edges,q); adj=adj_of(n,edges)
    pc,pn,pidx=classes(cols,adj,q)
    e2=list(edges)+[(s,n) for s in S]
    cols2=colourings(n+1,e2,q); adj2=adj_of(n+1,e2)
    cc,cn,cidx=classes(cols2,adj2,q)
    # work inside the child class that the inherited states land in (parent assumed 1 class here)
    img=[]
    for c in cols:
        free=[x for x in range(q) if x not in {c[s] for s in S}]
        if not free: return None
        img.append(tuple(list(c)+[free[0]]))
    Kp=cc[cidx[img[0]]]
    if any(cc[cidx[d]]!=Kp for d in img): return None      # not retained into one class
    child=[d for d in cols2 if cc[cidx[d]]==Kp]
    idx={d:i for i,d in enumerate(child)}; M=len(child)
    fib={}
    for d in child: fib[d[:n]]=fib.get(d[:n],0)+1
    marg_eq={x:fib[x]/M for x in fib}
    marg_in={d[:n]:0 for d in img}
    for d in img: marg_in[d[:n]]+=1.0/len(img)
    # exact relaxation of the inherited law under the lazy Metropolis chain on the child class
    nb=[[idx[t] for t in kempe_moves(d,adj2,q) if t in idx] for d in child]
    dmax=max(len(x) for x in nb)
    def evolve(vec,T):
        rec=[]
        u=[1.0/M]*M
        for t in range(T):
            rec.append(0.5*sum(abs(vec[i]-u[i]) for i in range(M)))
            nv=[0.0]*M
            for i,p in enumerate(vec):
                if p==0: continue
                stay=1.0-len(nb[i])/dmax
                nv[i]+=p*stay
                for j in nb[i]: nv[j]+=p/dmax
            vec=nv
        rec.append(0.5*sum(abs(vec[i]-u[i]) for i in range(M)))
        return rec
    v0=[0.0]*M
    for d in img: v0[idx[d]]+=1.0/len(img)
    rec=evolve(v0,steps)
    # null: a random subset of the same size
    nullrec=[]
    for _ in range(20):
        vn=[0.0]*M
        for d in random.sample(child,len(img)): vn[idx[d]]+=1.0/len(img)
        nullrec.append(evolve(vn,steps))
    nullmed=[sorted(r[t] for r in nullrec)[len(nullrec)//2] for t in range(steps+1)]
    def hit(rec,thr=0.25):
        for t,x in enumerate(rec):
            if x<=thr: return t
        return None
    print("%-26s q=%d S=%s  parent %d cols/%d classes; child class %d states; fibre sizes %s"%(
        name,q,S,len(cols),pn,M,sorted(set(fib.values()))))
    print("     marginal TV of the inherited law from the child equilibrium: %.4f"%tv(marg_in,marg_eq))
    print("     full TV at t=0: %.4f   mixing to 1/4:  inherited %s steps, random-subset null %s steps"%(
        rec[0],hit(rec),hit(nullmed)))
    return tv(marg_in,marg_eq)

C4=[(0,1),(1,2),(2,3),(0,3)]
C6=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)]
P5=[(0,1),(1,2),(2,3),(3,4)]
print("=== constant attachment count (theorem R3.1 predicts marginal TV = 0)")
study("C4  attach {0}",4,C4,3,[0])
study("C6  attach {0}",6,C6,3,[0])
print("=== variable attachment count (R3.2: equilibrium re-weights the OLD structure)")
study("C4  attach {0,2}",4,C4,3,[0,2])
study("C6  attach {0,2}",6,C6,3,[0,2])
study("C6  attach {0,2,4}",6,C6,3,[0,2,4])
study("P5  attach {0,2,4}",5,P5,3,[0,2,4])
study("C6  attach {0,3}",6,C6,4,[0,3])
