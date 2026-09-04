import math, sys
from collections import deque
from dimer import torus, matchings
sys.setrecursionlimit(10000)
def simple_cycles(n,E,maxlen):
    adj=[[] for _ in range(n)]
    for u,v in E: adj[u].append(v); adj[v].append(u)
    out=[]
    def dfs(start,path,seen):
        u=path[-1]
        for w in adj[u]:
            if w==start and len(path)>=4 and len(path)%2==0:
                if path[1]<path[-1]: out.append(list(path))
            elif w>start and w not in seen and len(path)<maxlen:
                seen.add(w); path.append(w); dfs(start,path,seen); path.pop(); seen.discard(w)
    for s in range(n):
        dfs(s,[s],{s})
    return out
def cyc_pairs(cycles):
    res=[]
    for c in cycles:
        k=len(c)
        e=[tuple(sorted((c[i],c[(i+1)%k]))) for i in range(k)]
        res.append((frozenset(e[0::2]),frozenset(e[1::2])))
    return res
def flips(M,cp):
    out=[]
    for p,q in cp:
        if p<=M: out.append(M-p|q)
        elif q<=M: out.append(M-q|p)
    return out
def classes(Ms,cp):
    idx={m:i for i,m in enumerate(Ms)}; comp=[-1]*len(Ms); nc=0
    for k in range(len(Ms)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in flips(Ms[x],cp):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    return comp,nc
for L,Mm in [(4,4),(4,6)]:
    V,idx,E,faces=torus(L,Mm); n=len(V)
    Ms=matchings(n,E); N=len(Ms)
    print("torus %dx%d: %d matchings"%(L,Mm,N))
    print("   max flip length   moves available   classes   R (bits)")
    for maxlen in (4,6,8,10):
        cyc=simple_cycles(n,E,maxlen)
        cp=cyc_pairs(cyc)
        comp,nc=classes(Ms,cp)
        sizes=[0]*nc
        for k in comp: sizes[k]+=1
        R=-sum((s/N)*math.log2(s/N) for s in sizes if s)
        print("       %2d              %6d          %4d      %.3f"%(maxlen,len(cp),nc,R))
