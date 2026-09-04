import itertools, sys
from collections import deque

def colourings(n, edges, q):
    out=[]
    for c in itertools.product(range(q), repeat=n):
        if all(c[u]!=c[v] for u,v in edges): out.append(c)
    return out

def adj_of(n, edges):
    a=[[] for _ in range(n)]
    for u,v in edges: a[u].append(v); a[v].append(u)
    return a

def kempe_moves(c, adj, q):
    """all colourings reachable by ONE Kempe change"""
    n=len(c); res=set()
    for i in range(q):
        for j in range(i+1,q):
            verts=[v for v in range(n) if c[v]in(i,j)]
            seen=set()
            for s in verts:
                if s in seen: continue
                comp=[]; dq=deque([s]); seen.add(s)
                while dq:
                    x=dq.popleft(); comp.append(x)
                    for y in adj[x]:
                        if y not in seen and c[y] in (i,j):
                            seen.add(y); dq.append(y)
                d=list(c)
                for x in comp: d[x]= j if c[x]==i else i
                t=tuple(d)
                if t!=c: res.add(t)
    return res

def classes(cols, adj, q):
    idx={c:k for k,c in enumerate(cols)}
    comp=[-1]*len(cols); nc=0
    for k,c in enumerate(cols):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in kempe_moves(cols[x], adj, q):
                y=idx[t]
                if comp[y]==-1: comp[y]=nc; dq.append(y)
        nc+=1
    return comp, nc, idx

def analyse(n, edges, S, q):
    """parent G on n vertices; child G' = G + new vertex n joined to S.
       A(c) = c extended by the smallest colour not used on S."""
    adj=adj_of(n,edges); cols=colourings(n,edges,q)
    if not cols: return None
    pc,pn,pidx=classes(cols,adj,q)
    e2=list(edges)+[(s,n) for s in S]
    adj2=adj_of(n+1,e2); cols2=colourings(n+1,e2,q)
    cc,cn,cidx=classes(cols2,adj2,q)
    merge=False; split=False
    img={}
    for k,c in enumerate(cols):
        used={c[s] for s in S}
        free=[x for x in range(q) if x not in used]
        if not free: return None          # A not total
        d=tuple(list(c)+[free[0]])
        img[k]=cc[cidx[d]]
    # split: same parent class -> different child classes
    fwd={}
    for k in range(len(cols)):
        fwd.setdefault(pc[k],set()).add(img[k])
    split=any(len(v)>1 for v in fwd.values())
    # merge: different parent classes -> a common child class
    back={}
    for k in range(len(cols)):
        back.setdefault(img[k],set()).add(pc[k])
    merge=any(len(v)>1 for v in back.values())
    return dict(pn=pn,cn=cn,merge=merge,split=split,ncol=len(cols),ncol2=len(cols2))

# ---- search small graphs for the three behaviours
def all_graphs(n):
    E=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(E)):
        yield [E[i] for i in range(len(E)) if mask>>i&1]

found={}
q=3
for n in range(3,6):
    for edges in all_graphs(n):
        if not edges: continue
        deg=[0]*n
        for u,v in edges: deg[u]+=1; deg[v]+=1
        if min(deg)==0: continue                    # connected-ish filter
        for r in range(1,min(q,n+1)):
            for S in itertools.combinations(range(n),r):
                res=analyse(n,edges,list(S),q)
                if res is None: continue
                key=(res['merge'],res['split'])
                if key not in found:
                    found[key]=(n,edges,S,res)
    if len(found)==4: break
for k,v in sorted(found.items()):
    print("merge=%-5s split=%-5s  n=%d edges=%s S=%s  parent %d cols/%d classes -> child %d cols/%d classes"%(
        k[0],k[1],v[0],v[1],v[2],v[3]['ncol'],v[3]['pn'],v[3]['ncol2'],v[3]['cn']))
