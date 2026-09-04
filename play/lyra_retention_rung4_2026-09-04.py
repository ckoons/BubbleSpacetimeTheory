import itertools
from retention import colourings, adj_of, classes
q=3
# prism minus vertex 0, then attach the vertex back to its three neighbours {3,4,5}
BASE=[(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
V=[1,2,3,4,5]; rel={v:i for i,v in enumerate(V)}
base=[(rel[u],rel[v]) for u,v in BASE]
cols=colourings(5,base,q); pc,pn,pidx=classes(cols,adj_of(5,base),q)
S=[rel[3],rel[4],rel[5]]
ext=[c for c in cols if len({c[s] for s in S})<q]
e2=base+[(s,5) for s in S]
cols2=colourings(6,e2,q); cc,cn,cidx=classes(cols2,adj_of(6,e2),q)
print("PARENT (prism minus a vertex): %d colourings, %d Kempe class(es)"%(len(cols),pn))
print("  extendable parent states: %d of %d  (%d are FORBIDDEN by the new vertex)"%(len(ext),len(cols),len(cols)-len(ext)))
print("CHILD (the prism): %d colourings, %d Kempe classes"%(len(cols2),cn))
# R4.2: child classes should equal components of the parent move graph RESTRICTED to extendable states
from retention import kempe_moves
adj=adj_of(5,base); idx={c:i for i,c in enumerate(ext)}
import collections
seen={}; comp=0
for c in ext:
    if c in seen: continue
    dq=collections.deque([c]); seen[c]=comp
    while dq:
        x=dq.popleft()
        for t in kempe_moves(x,adj,q):
            if t in idx and t not in seen: seen[t]=comp; dq.append(t)
    comp+=1
print("  components of the parent's move graph restricted to the extendable states: %d"%comp)
print("  R4.2 prediction (child classes == that count): %s"%("CONFIRMED" if comp==cn else "FAILED"))
print("  retained information: parent %.3f bits -> child %.3f bits"%(
    __import__('math').log2(pn), __import__('math').log2(cn)))
