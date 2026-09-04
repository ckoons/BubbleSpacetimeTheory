import itertools, math, random
from retention import colourings, adj_of, kempe_moves
from chain import classes_of
random.seed(5); q=3
PRISM=[(0,3),(0,4),(0,5),(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
def build(k):
    E=list(PRISM); n=6
    for _ in range(k): E.append((0,n)); n+=1
    return E,n
def machinery(K,adj):
    idx={c:i for i,c in enumerate(K)}; N=len(K)
    nb=[[idx[t] for t in kempe_moves(c,adj,q) if t in idx] for c in K]
    dmax=max(len(x) for x in nb)
    def step(v):                      # PROPERLY lazy: half chance to stay put
        w=[0.5*x for x in v]
        for i,p in enumerate(v):
            if p:
                w[i]+=0.5*p*(1-len(nb[i])/dmax)
                for j in nb[i]: w[j]+=0.5*p/dmax
        return w
    return idx,N,step
def relax(K,adj):
    idx,N,step=machinery(K,adj)
    w=[random.random()-0.5 for _ in range(N)]; m=sum(w)/N; w=[x-m for x in w]; lam=0
    for _ in range(6000):
        w=step(w); m=sum(w)/N; w=[x-m for x in w]
        nrm=math.sqrt(sum(x*x for x in w))
        if nrm<1e-15: return 0.0,float('inf')
        w=[x/nrm for x in w]; lam=nrm
    g=1-lam
    return g,(1/g if g>1e-12 else float('inf'))
def tvcurve(K,adj,start,ts):
    idx,N,step=machinery(K,adj); u=1.0/N; v=list(start); out={}; 
    for t in range(max(ts)+1):
        if t in ts: out[t]=0.5*sum(abs(x-u) for x in v)
        v=step(v)
    return out
TS=[0,2,5,10,20,40]
print("pend  |class|  gap     relax     TV from INHERITED at t=%s"%TS)
print("                                 and from a random half-subset (median of 11)")
prev=None
for k in range(0,7):
    E,n=build(k); cols=colourings(n,E,q); comp,nc=classes_of(cols,adj_of(n,E),q); adj=adj_of(n,E)
    K=[cols[i] for i in range(len(cols)) if comp[i]==0]; idx={c:i for i,c in enumerate(K)}; N=len(K)
    if prev is None: start=[1.0/N]*N
    else:
        img=[tuple(list(c)+[ [x for x in range(q) if x!=c[0]][0] ]) for c in prev]
        img=[d for d in img if d in idx]
        start=[0.0]*N
        for d in img: start[idx[d]]+=1.0/len(img)
    g,r=relax(K,adj)
    ci=tvcurve(K,adj,start,TS)
    nul=[]
    for _ in range(11):
        s=[0.0]*N
        for d in random.sample(K,max(1,N//2)): s[idx[d]]+=2.0/N
        nul.append(tvcurve(K,adj,s,TS))
    med={t:sorted(x[t] for x in nul)[len(nul)//2] for t in TS}
    print(" %d    %5d  %.4f  %7.2f   inherited %s"%(k,N,g,r,["%.3f"%ci[t] for t in TS]))
    print("                                 random    %s"%(["%.3f"%med[t] for t in TS],))
    prev=K
