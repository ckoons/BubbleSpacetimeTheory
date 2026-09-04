import itertools, math
from retention import colourings, adj_of
from chain import classes_of
def torusT(L,M):
    n=L*M; E=set()
    def v(i,j): return (i%L)*M+(j%M)
    for i in range(L):
        for j in range(M):
            E.add(tuple(sorted((v(i,j),v(i+1,j)))))
            E.add(tuple(sorted((v(i,j),v(i,j+1)))))
            E.add(tuple(sorted((v(i,j),v(i+1,j+1)))))
    return sorted(E),n
E,n=torusT(3,4); q=4
cols=colourings(n,E,q); comp,nc=classes_of(cols,adj_of(n,E),q)
idx={c:i for i,c in enumerate(cols)}
print("torus 3x4, q=4: %d colourings, %d classes, sizes %s"%(len(cols),nc,[comp.count(k) for k in range(nc)]))
moves=set()
for p in itertools.permutations(range(q)):
    m=set()
    for k,c in enumerate(cols):
        m.add((comp[k],comp[idx[tuple(p[x] for x in c)]]))
    moves.add((p,frozenset(m)))
nontriv=[p for p,m in moves if any(a!=b for a,b in m)]
print("colour permutations that MOVE a colouring between classes: %d of %d"%(len(nontriv),math.factorial(q)))
orb=set()
for k in range(len(cols)):
    orb.add(frozenset(comp[idx[tuple(p[x] for x in cols[k])]] for p in itertools.permutations(range(q))))
print("classes modulo global colour relabelling: %d  ->  gauge-invariant retained information = %.3f bits"%(
    len(orb), math.log2(len(orb))))
# is each class a single orbit of the colour group?
for k in range(nc):
    mem=[i for i in range(len(cols)) if comp[i]==k]
    o=set()
    for p in itertools.permutations(range(q)):
        o.add(idx[tuple(p[x] for x in cols[mem[0]])])
    print("  class %d: size %d;  colour-orbit of one member has size %d, inside this class: %s"%(
        k,len(mem),len(o),all(comp[j]==k for j in o)))
