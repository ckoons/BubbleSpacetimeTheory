import itertools, math
from collections import deque
def torus(L,M):
    V=[(i,j) for i in range(L) for j in range(M)]
    idx={v:k for k,v in enumerate(V)}
    E=set()
    for i in range(L):
        for j in range(M):
            E.add(tuple(sorted((idx[(i,j)],idx[(i,(j+1)%M)]))))
            E.add(tuple(sorted((idx[(i,j)],idx[((i+1)%L,j)]))))
    faces=[]
    for i in range(L):
        for j in range(M):
            a=idx[(i,j)]; b=idx[(i,(j+1)%M)]; c=idx[((i+1)%L,(j+1)%M)]; d=idx[((i+1)%L,j)]
            faces.append((a,b,c,d))
    return V,idx,sorted(E),faces
def matchings(n,E):
    adj=[[] for _ in range(n)]
    for u,v in E: adj[u].append(v); adj[v].append(u)
    out=[]
    def go(used,cur):
        if len(used)==n: out.append(frozenset(cur)); return
        u=min(x for x in range(n) if x not in used)
        for v in adj[u]:
            if v not in used:
                go(used|{u,v}, cur+[tuple(sorted((u,v)))])
    go(frozenset(),[])
    return out
def flips(M,faces):
    res=[]
    for (a,b,c,d) in faces:
        e1,e2=tuple(sorted((a,b))),tuple(sorted((c,d)))
        f1,f2=tuple(sorted((b,c))),tuple(sorted((d,a)))
        if e1 in M and e2 in M: res.append(M-{e1,e2}|{f1,f2})
        elif f1 in M and f2 in M: res.append(M-{f1,f2}|{e1,e2})
    return res
def classes(Ms,faces):
    idx={m:i for i,m in enumerate(Ms)}; comp=[-1]*len(Ms); nc=0
    for k in range(len(Ms)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in flips(Ms[x],faces):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    return comp,nc
def flux(M,V,idx,L,Mm):
    # signed winding numbers: black = (i+j) even; orient black->white
    inv=[None]*(L*Mm)
    for v,k in idx.items(): inv[k]=v
    wx=wy=0
    for (u,v) in M:
        (i1,j1),(i2,j2)=inv[u],inv[v]
        if (i1+j1)%2==1: (i1,j1),(i2,j2)=(i2,j2),(i1,j1)   # black first
        di=(i2-i1)%L; dj=(j2-j1)%Mm
        if dj==1 or dj==Mm-1:                                # horizontal dimer
            wx += 1 if dj==1 else -1
        else:
            wy += 1 if di==1 else -1
    return wx,wy
for L,Mm in [(4,4),(4,6),(6,6)]:
    V,idx,E,faces=torus(L,Mm)
    Ms=matchings(len(V),E)
    if len(Ms)>60000: print("%dx%d: %d matchings, skipped"%(L,Mm,len(Ms))); continue
    comp,nc=classes(Ms,faces)
    sizes=sorted([comp.count(k) for k in range(nc)],reverse=True)
    fx={}
    for k,m in enumerate(Ms): fx.setdefault(comp[k],set()).add(flux(m,V,idx,L,Mm))
    sep=all(len(s)==1 for s in fx.values()) and len({next(iter(s)) for s in fx.values()})==nc
    print("torus %dx%d: %6d matchings  %3d classes  R=%.3f bits  sizes %s"%(L,Mm,len(Ms),nc,math.log2(nc),sizes[:8]))
    print("     flux (winding) separates the classes exactly: %s   values %s"%(sep,sorted({next(iter(s)) for s in fx.values()})[:8]))
