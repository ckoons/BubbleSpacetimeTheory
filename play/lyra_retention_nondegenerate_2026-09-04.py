import itertools, math
from retention import colourings, adj_of
from chain import classes_of
PRISM=[(0,3),(0,4),(0,5),(1,2),(1,4),(1,5),(2,3),(2,5),(3,4)]
q=3; GRP=list(itertools.permutations(range(q)))
def report(name,n,E):
    cols=colourings(n,E,q)
    if not cols: return None
    comp,nc=classes_of(cols,adj_of(n,E),q)
    idx={c:i for i,c in enumerate(cols)}
    sizes=[comp.count(k) for k in range(nc)]
    # colour orbits inside each class
    orbs=[]
    for k in range(nc):
        mem=[i for i in range(len(cols)) if comp[i]==k]
        seen=set(); o=0
        for i in mem:
            if i in seen: continue
            o+=1
            for p in GRP: seen.add(idx[tuple(p[x] for x in cols[i])])
        orbs.append(o)
    print("  %-28s n=%2d  %5d states  %d classes  sizes %s  colour-orbits per class %s  %s"%(
        name,n,len(cols),nc,sizes,orbs,"NON-DEGENERATE" if max(orbs)>1 else "frozen (gauge only)"))
    return nc,sizes,orbs
print("prism plus pendant vertices (each attached to vertex 0), q=3:")
E=list(PRISM); n=6
report("prism",n,E)
for k in range(5):
    E=E+[(0,n)]; n+=1
    report("prism + %d pendant(s)"%(k+1),n,E)
print()
print("prism plus a vertex attached to two vertices:")
for S in ([0,1],[1,3],[0,3]):
    report("prism + v on %s"%S,7,list(PRISM)+[(s,6) for s in S])
