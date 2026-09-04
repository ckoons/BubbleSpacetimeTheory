import itertools
from retention import colourings, adj_of, classes
PRISM=[(0,3),(0,4),(0,5),(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
n,q=6,3
cols=colourings(n,PRISM,q); pc,pn,pidx=classes(cols,adj_of(n,PRISM),q)
print("classes:",pn,"sizes:",[pc.count(k) for k in range(pn)])
# does a global colour permutation move a colouring between classes?
for perm in itertools.permutations(range(q)):
    moved=set()
    for k,c in enumerate(cols):
        d=tuple(perm[x] for x in c)
        moved.add((pc[k],pc[pidx[d]]))
    sgn=sum(1 for i in range(q) for j in range(i+1,q) if perm[i]>perm[j])%2
    print("  perm %s (parity %d): class map %s"%(perm,sgn,sorted(moved)))
orb=set()
for k in range(len(cols)):
    orb.add(frozenset(pc[pidx[tuple(p[x] for x in cols[k])]] for p in itertools.permutations(range(q))))
print("classes modulo global colour relabelling:", len(orb), "->  gauge-invariant retained bits =", 0 if len(orb)==1 else "nonzero")
