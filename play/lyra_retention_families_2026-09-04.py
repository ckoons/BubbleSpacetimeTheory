import itertools
from retention import colourings, adj_of, classes

def parent(edges,n,q):
    adj=adj_of(n,edges); cols=colourings(n,edges,q)
    pc,pn,pidx=classes(cols,adj,q)
    return cols,adj,pc,pn,pidx

def verdict(cols,pc,pn,pairs,cc,cidx):
    """pairs: list of (parent_index, child_colouring)"""
    fwd={}; back={}
    for k,d in pairs:
        ch=cc[cidx[d]]
        fwd.setdefault(pc[k],set()).add(ch); back.setdefault(ch,set()).add(pc[k])
    return (any(len(v)>1 for v in back.values()),   # merge
            any(len(v)>1 for v in fwd.values()))    # split

def run(edges,n,q,label):
    cols,adj,pc,pn,pidx=parent(edges,n,q)
    if pn<2: return []
    out=[]
    # (a) add a vertex joined to S
    for r in (1,2,3):
        for S in itertools.combinations(range(n),r):
            e2=list(edges)+[(s,n) for s in S]
            cols2=colourings(n+1,e2,q)
            if not cols2: continue
            cc,cn,cidx=classes(cols2,adj_of(n+1,e2),q)
            pairs=[]; ok=True
            for k,c in enumerate(cols):
                free=[x for x in range(q) if x not in {c[s] for s in S}]
                if not free: ok=False; break
                pairs.append((k,tuple(list(c)+[free[0]])))
            if ok: out.append(("add S=%s"%(S,),pn,cn)+verdict(cols,pc,pn,pairs,cc,cidx))
    # (b) subdivide an edge
    for (u,w) in edges:
        e2=[e for e in edges if e!=(u,w)]+[(u,n),(w,n)]
        cols2=colourings(n+1,e2,q)
        cc,cn,cidx=classes(cols2,adj_of(n+1,e2),q)
        pairs=[]; ok=True
        for k,c in enumerate(cols):
            free=[x for x in range(q) if x not in (c[u],c[w])]
            if not free: ok=False; break
            pairs.append((k,tuple(list(c)+[free[0]])))
        if ok: out.append(("subdiv %s"%((u,w),),pn,cn)+verdict(cols,pc,pn,pairs,cc,cidx))
    # (c) delete an edge (inclusion map)
    for e in edges:
        e2=[x for x in edges if x!=e]
        cols2=colourings(n,e2,q)
        cc,cn,cidx=classes(cols2,adj_of(n,e2),q)
        pairs=[(k,c) for k,c in enumerate(cols)]
        out.append(("delete %s"%(e,),pn,cn)+verdict(cols,pc,pn,pairs,cc,cidx))
    return out

PRISM=[(0,3),(0,4),(0,5),(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
res=run(PRISM,6,3,"prism")
seen={}
for name,pn,cn,merge,split in res:
    seen.setdefault((merge,split),[]).append((name,pn,cn))
print("PRISM q=3, parent classes = 2")
for k in sorted(seen):
    print("  merge=%-5s split=%-5s : %d steps, e.g. %s"%(k[0],k[1],len(seen[k]),seen[k][:4]))
