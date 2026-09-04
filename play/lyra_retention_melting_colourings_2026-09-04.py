import math
from collections import deque
from retention import colourings, adj_of
def kempe_lim(c,adj,q,maxsize):
    n=len(c); res=set()
    for i in range(q):
        for j in range(i+1,q):
            seen=set()
            for s in range(n):
                if c[s] not in (i,j) or s in seen: continue
                comp=[]; dq=deque([s]); seen.add(s)
                while dq:
                    x=dq.popleft(); comp.append(x)
                    for y in adj[x]:
                        if y not in seen and c[y] in (i,j): seen.add(y); dq.append(y)
                if len(comp)>maxsize: continue
                d=list(c)
                for x in comp: d[x]= j if c[x]==i else i
                t=tuple(d)
                if t!=c: res.add(t)
    return res
def classes_lim(cols,adj,q,maxsize):
    idx={c:i for i,c in enumerate(cols)}; comp=[-1]*len(cols); nc=0
    for k in range(len(cols)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in kempe_lim(cols[x],adj,q,maxsize):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    return comp,nc
def torusT(L,M):
    n=L*M; E=set()
    def v(i,j): return (i%L)*M+(j%M)
    for i in range(L):
        for j in range(M):
            for di,dj in ((1,0),(0,1),(1,1)):
                a,b=v(i,j),v(i+di,j+dj)
                if a!=b: E.add(tuple(sorted((a,b))))
    return sorted(E),n
PRISM=[(0,3),(0,4),(0,5),(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
cases=[("prism",PRISM,6,3),("torus 3x4",)+torusT(3,4)[::-1]+(4,),("torus 4x5",)+torusT(4,5)[::-1]+(4,)]
for name,E,n,q in [("prism",PRISM,6,3),("torus 3x4",torusT(3,4)[0],12,4),("torus 4x5",torusT(4,5)[0],20,4)]:
    cols=colourings(n,E,q); adj=adj_of(n,E); N=len(cols)
    print("%s: %d colourings, %d vertices, q=%d"%(name,N,n,q))
    print("    max Kempe component   classes   R (bits)")
    prev=None
    for ms in [1,2,3,4,6,8,n]:
        if ms>n: continue
        comp,nc=classes_lim(cols,adj,q,ms)
        sz=[0]*nc
        for k in comp: sz[k]+=1
        R=-sum((s/N)*math.log2(s/N) for s in sz if s)
        tag=" (unrestricted)" if ms==n else ""
        print("          %2d%-15s %4d      %.3f"%(ms,tag,nc,R))
