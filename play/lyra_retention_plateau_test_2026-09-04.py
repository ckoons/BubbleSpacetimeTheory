import itertools, math
from collections import deque
from retention import colourings, adj_of
def gen_moves(c,E,q,perms,maxsub=None):
    """apply any colour permutation to any subset; keep it if still proper"""
    n=len(c); res=set()
    rng=range(n)
    subsets = (itertools.chain.from_iterable(itertools.combinations(rng,k) for k in range(1,(maxsub or n)+1)))
    for S in subsets:
        Sset=set(S)
        for p in perms:
            d=tuple(p[c[v]] if v in Sset else c[v] for v in rng)
            if d==c: continue
            if all(d[u]!=d[v] for u,v in E): res.add(d)
    return res
def classes_gen(cols,E,q,maxsub=None):
    perms=[p for p in itertools.permutations(range(q)) if p!=tuple(range(q))]
    idx={c:i for i,c in enumerate(cols)}; comp=[-1]*len(cols); nc=0
    for k in range(len(cols)):
        if comp[k]!=-1: continue
        dq=deque([k]); comp[k]=nc
        while dq:
            x=dq.popleft()
            for t in gen_moves(cols[x],E,q,perms,maxsub):
                j=idx.get(t)
                if j is not None and comp[j]==-1: comp[j]=nc; dq.append(j)
        nc+=1
    return comp,nc
PRISM=[(0,3),(0,4),(0,5),(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
cols=colourings(6,PRISM,3); N=len(cols)
print("PRISM, q=3: %d colourings.  Kempe (unrestricted) gave 2 classes, R = 1.000 bits."%N)
comp,nc=classes_gen(cols,PRISM,3)
sz=[0]*nc
for k in comp: sz[k]+=1
R=-sum((s/N)*math.log2(s/N) for s in sz if s)
print("   FULL generalised move set (every colour permutation on every subset, properness kept):")
print("      %d classes, R = %.3f bits   -> plateau %s"%(nc,R,"SURVIVES" if nc>1 else "DESTROYED"))
def torusT(L,M):
    n=L*M; E=set()
    def v(i,j): return (i%L)*M+(j%M)
    for i in range(L):
        for j in range(M):
            for di,dj in ((1,0),(0,1),(1,1)):
                a,b=v(i,j),v(i+di,j+dj)
                if a!=b: E.add(tuple(sorted((a,b))))
    return sorted(E),n
E,n=torusT(3,4)
cols=colourings(n,E,4); N=len(cols)
print("TORUS 3x4, q=4: %d colourings.  Kempe (unrestricted) gave 3 classes, R = 1.585 bits."%N)
for ms in (3,5,7):
    comp,nc=classes_gen(cols,E,4,maxsub=ms)
    sz=[0]*nc
    for k in comp: sz[k]+=1
    R=-sum((s/N)*math.log2(s/N) for s in sz if s)
    print("   generalised moves on subsets up to size %d: %d classes, R = %.3f"%(ms,nc,R))
