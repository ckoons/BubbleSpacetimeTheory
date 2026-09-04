import itertools, math
from collections import deque
from retention import adj_of, kempe_moves

def classes_of(cols, adj, q):
    idx={c:i for i,c in enumerate(cols)}; comp=[-1]*len(cols); nc=0
    for k in range(len(cols)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in kempe_moves(cols[x],adj,q):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    return comp,nc

def extend(cols,S,q):
    out=[]; kept=0
    for c in cols:
        used={c[s] for s in S}
        free=[x for x in range(q) if x not in used]
        if free: kept+=1
        for f in free: out.append(tuple(list(c)+[f]))
    return out,kept

def grow(edges,n,q,steps,cap=40000,maxS=4):
    cols=[c for c in itertools.product(range(q),repeat=n) if all(c[u]!=c[v] for u,v in edges)]
    adj=adj_of(n,edges); comp,nc=classes_of(cols,adj,q)
    print("  step 0: n=%2d  %6d colourings  %3d classes  R=%.3f bits"%(n,len(cols),nc,math.log2(nc)))
    hist=[(n,len(cols),nc)]
    for t in range(steps):
        best=None
        for r in range(2,maxS+1):
            for S in itertools.combinations(range(n),r):
                c2,kept=extend(cols,list(S),q)
                if not c2 or len(c2)>cap: continue
                e2=edges+[(s,n) for s in S]
                cc,cn=classes_of(c2,adj_of(n+1,e2),q)
                score=(cn,-len(c2))
                if best is None or score>best[0]: best=(score,S,c2,e2,cn,kept)
        if best is None: print("  no admissible step"); break
        score,S,c2,e2,cn,kept=best
        excl=len(cols)-kept
        edges=e2; cols=c2; n+=1; adj=adj_of(n,edges)
        print("  step %d: attach %-12s excluded %4d of %5d parent states -> n=%2d  %6d colourings  %3d classes  R=%.3f bits"%(
            t+1,str(S),excl,excl+kept,n,len(cols),cn,math.log2(cn)))
        hist.append((n,len(cols),cn))
    return hist

print("CHAIN A: from the 5-vertex parent of the prism, q=3, greedy on class count")
BASE=[(0,1),(0,3),(0,4),(1,2),(1,4),(2,3)]   # prism minus a vertex, relabelled
grow(BASE,5,3,6)
print()
print("CHAIN B: from a 6-cycle, q=3")
grow([(i,(i+1)%6) for i in range(6)],6,3,6)
