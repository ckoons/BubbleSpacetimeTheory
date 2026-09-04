import math, random
from dimer import torus, matchings
from dimer2 import cycles4, flips_generic, classes
random.seed(9)
L,Mm=4,6
V,idx,E,faces=torus(L,Mm); n=len(V)
Ms=matchings(n,E); cyc=cycles4(n,E); comp,nc=classes(Ms,cyc)
a,b=n,n+1
def child(S,T,extra=0):
    E2=list(E)+[tuple(sorted((a,b)))]+[tuple(sorted((s,a))) for s in S]+[tuple(sorted((s,b))) for s in T]
    n2=n+2
    Ms2=matchings(n2,E2); cyc2=cycles4(n2,E2); c2,nc2=classes(Ms2,cyc2)
    return Ms2,cyc2,c2,nc2,E2,n2
def curve(states,cyc,start,TS):
    idx2={m:i for i,m in enumerate(states)}; N=len(states)
    nb=[[idx2[t] for t in flips_generic(m,cyc) if t in idx2] for m in states]
    dmax=max(1,max(len(x) for x in nb))
    def step(v):
        w=[0.5*x for x in v]
        for i,p in enumerate(v):
            if p:
                w[i]+=0.5*p*(1-len(nb[i])/dmax)
                for j in nb[i]: w[j]+=0.5*p/dmax
        return w
    u=1.0/N; out={}; v=list(start)
    for t in range(max(TS)+1):
        if t in TS: out[t]=0.5*sum(abs(x-u) for x in v)
        v=step(v)
    return out
TS=[0,5,10,20,40,80]
print("DIMER COLD START, torus 4x6, retaining construction (S=[0], T=[1])")
Ms2,cyc2,c2,nc2,E2,n2=child([0],[1])
ab=tuple(sorted((a,b)))
idx2={m:i for i,m in enumerate(Ms2)}
print("  parent %d classes -> child %d classes"%(nc,nc2))
for K in range(nc):
    par=[Ms[i] for i in range(len(Ms)) if comp[i]==K]
    img=[frozenset(set(m)|{ab}) for m in par]
    cls=c2[idx2[img[0]]]
    if any(c2[idx2[d]]!=cls for d in img): print("   class %d: not retained"%K); continue
    K2=[m for i,m in enumerate(Ms2) if c2[i]==cls]
    if len(K2)<8: continue
    j={m:i for i,m in enumerate(K2)}; N=len(K2)
    st=[0.0]*N
    for d in img: st[j[d]]+=1.0/len(img)
    ci=curve(K2,cyc2,st,TS)
    nul=[]
    for _ in range(9):
        s=[0.0]*N
        sub=random.sample(K2,max(1,len(img)))
        for d in sub: s[j[d]]+=1.0/len(sub)
        nul.append(curve(K2,cyc2,s,TS))
    med={t:sorted(x[t] for x in nul)[len(nul)//2] for t in TS}
    print("   class %d: parent %4d -> child class %4d states   inherited %s"%(K,len(par),N,["%.3f"%ci[t] for t in TS]))
    print("                                                    random    %s"%(["%.3f"%med[t] for t in TS],))
