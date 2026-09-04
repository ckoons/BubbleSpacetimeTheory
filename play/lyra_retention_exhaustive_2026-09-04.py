import itertools, sys
from collections import deque
from retention import colourings, adj_of, classes

def connected(n,edges):
    a=adj_of(n,edges); seen={0}; dq=deque([0])
    while dq:
        x=dq.popleft()
        for y in a[x]:
            if y not in seen: seen.add(y); dq.append(y)
    return len(seen)==n

def multiclass_parents(n,q):
    E=list(itertools.combinations(range(n),2)); out=[]
    for mask in range(1<<len(E)):
        edges=[E[i] for i in range(len(E)) if mask>>i&1]
        if len(edges)<n: continue
        deg=[0]*n
        for u,v in edges: deg[u]+=1; deg[v]+=1
        if min(deg)<2 or not connected(n,edges): continue
        cols=colourings(n,edges,q)
        if len(cols)<2: continue
        pc,pn,_=classes(cols,adj_of(n,edges),q)
        if pn>1: out.append((tuple(edges),len(cols),pn))
    return out

n,q=6,3
P=multiclass_parents(n,q)
print("6-vertex q=3 graphs with >1 Kempe class: %d (all with %s colourings / %s classes)"%(
      len(P), sorted({p[1] for p in P}), sorted({p[2] for p in P})))

# exhaustive vertex-addition test on every one of them, every S, every extension rule
tested=0; merged=0; split=0; childmulti=0
for edges,ncol,pn in P:
    edges=list(edges); cols=colourings(n,edges,q); pc,pn2,pidx=classes(cols,adj_of(n,edges),q)
    for r in range(1,4):
        for S in itertools.combinations(range(n),r):
            e2=edges+[(s,n) for s in S]
            cols2=colourings(n+1,e2,q)
            if not cols2: continue
            cc,cn,cidx=classes(cols2,adj_of(n+1,e2),q)
            for rule in range(3):
                back={}; fwd={}; ok=True
                for k,c in enumerate(cols):
                    free=[x for x in range(q) if x not in {c[s] for s in S}]
                    if not free: ok=False; break
                    d=tuple(list(c)+[free[rule%len(free)]])
                    ch=cc[cidx[d]]
                    back.setdefault(ch,set()).add(pc[k]); fwd.setdefault(pc[k],set()).add(ch)
                if not ok: continue
                tested+=1; childmulti+= (cn>1)
                if any(len(v)>1 for v in back.values()): merged+=1
                if any(len(v)>1 for v in fwd.values()): split+=1
print("exhaustive vertex-addition constructions tested: %d  (child multi-class in %d)"%(tested,childmulti))
print("  MERGED: %d     SPLIT: %d"%(merged,split))
print("RETRACTION THEOREM (vertex addition never merges): %s"%("HOLDS, 0 counterexamples" if merged==0 else "FALSIFIED"))
