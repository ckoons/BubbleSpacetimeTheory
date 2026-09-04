import sys, math
from collections import deque
sys.setrecursionlimit(10000)
def torusT(L,M):
    n=L*M; E=set()
    def v(i,j): return (i%L)*M+(j%M)
    for i in range(L):
        for j in range(M):
            for di,dj in ((1,0),(0,1),(1,1)):
                a,b=v(i,j),v(i+di,j+dj)
                if a!=b: E.add(tuple(sorted((a,b))))
    return sorted(E),n
def adj_of(n,E):
    a=[[] for _ in range(n)]
    for u,v in E: a[u].append(v); a[v].append(u)
    return a
def enum(n,adj,q,cap):
    out=[]; col=[-1]*n
    def go(i):
        if len(out)>cap: return
        if i==n: out.append(tuple(col)); return
        used={col[j] for j in adj[i] if j<i and col[j]>=0}
        for c in range(q):
            if c not in used:
                col[i]=c; go(i+1); col[i]=-1
    go(0); return out
def kempe(c,adj,q):
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
                d=list(c)
                for x in comp: d[x]= j if c[x]==i else i
                t=tuple(d)
                if t!=c: res.add(t)
    return res
print("triangulated tori, q=4:  L x M   vertices  colourings  classes   R (bits)")
for L,M in [(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(3,7),(4,6)]:
    E,n=torusT(L,M); adj=adj_of(n,E)
    cols=enum(n,adj,4,400000)
    if len(cols)>400000: print("   %dx%d  n=%2d  >400000 colourings, skipped"%(L,M,n)); continue
    idx={c:i for i,c in enumerate(cols)}; comp=[-1]*len(cols); nc=0
    for k in range(len(cols)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in kempe(cols[x],adj,4):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    sizes=sorted({comp.count(k) for k in range(nc)})
    print("   %dx%d  n=%2d  %8d   %4d    %.3f    class sizes %s"%(L,M,n,len(cols),nc,math.log2(nc),sizes[:5]))
