import itertools, math
from collections import deque
from dimer import torus, matchings
def cycles4(n,E):
    adj=[set() for _ in range(n)]
    for u,v in E: adj[u].add(v); adj[v].add(u)
    res=set()
    for a in range(n):
        for b in adj[a]:
            for c in adj[b]:
                if c==a: continue
                for d in adj[c]:
                    if d in (a,b) or a not in adj[d]: continue
                    p=frozenset([tuple(sorted((a,b))),tuple(sorted((c,d)))])
                    q=frozenset([tuple(sorted((b,c))),tuple(sorted((d,a)))])
                    if p!=q: res.add(frozenset([p,q]))
    return [tuple(x) for x in res]

def flips_generic(M,cyc):
    out=[]
    for p,q in cyc:
        if p<=M: out.append(M-p|q)
        elif q<=M: out.append(M-q|p)
    return out
def classes(Ms,cyc):
    idx={m:i for i,m in enumerate(Ms)}; comp=[-1]*len(Ms); nc=0
    for k in range(len(Ms)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in flips_generic(Ms[x],cyc):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    return comp,nc
def study(L,Mm,attach):
    V,idx,E,faces=torus(L,Mm); n=len(V)
    Ms=matchings(n,E); cyc=cycles4(n,E)
    comp,nc=classes(Ms,cyc)
    print("  parent torus %dx%d: %d matchings, %d classes (generic 4-cycle moves)"%(L,Mm,len(Ms),nc))
    a,b=n,n+1
    E2=list(E)+[tuple(sorted((a,b)))]+[tuple(sorted((s,a))) for s in attach[0]]+[tuple(sorted((s,b))) for s in attach[1]]
    n2=n+2
    Ms2=matchings(n2,E2); cyc2=cycles4(n2,E2)
    comp2,nc2=classes(Ms2,cyc2)
    idx2={m:i for i,m in enumerate(Ms2)}
    ab=tuple(sorted((a,b)))
    fwd={}; back={}
    for k,m in enumerate(Ms):
        d=frozenset(set(m)|{ab})
        j=idx2.get(d)
        if j is None: return None
        fwd.setdefault(comp[k],set()).add(comp2[j]); back.setdefault(comp2[j],set()).add(comp[k])
    split=any(len(v)>1 for v in fwd.values()); merge=any(len(v)>1 for v in back.values())
    print("     child: %d matchings, %d classes   MERGE=%s  SPLIT=%s   (image covers %d of %d child classes)"%(
        len(Ms2),nc2,merge,split,len(back),nc2))
    return merge,split,nc,nc2
print("DIMER INSTANCE: add a new matched pair (a,b), a joined to S, b joined to T; A(M)=M+{ab}")
for att in [([0],[1]), ([0,1],[2,3]), ([0,1,2],[3,4,5]), ([0],[0])]:
    print("  attach S=%s T=%s"%att)
    study(4,4,att)
