import itertools, math
from collections import deque
from retention import colourings, adj_of, kempe_moves
q=3
BASE=[(0,1),(0,3),(0,4),(1,2),(1,4),(2,3)]      # prism minus a vertex
cols=colourings(5,BASE,q); adj=adj_of(5,BASE)
idx={c:i for i,c in enumerate(cols)}; N=len(cols)
E=set()
for i,c in enumerate(cols):
    for t in kempe_moves(c,adj,q):
        j=idx.get(t)
        if j is not None and j!=i: E.add((min(i,j),max(i,j)))
E=sorted(E)
nb=[[] for _ in range(N)]
for a,b in E: nb[a].append(b); nb[b].append(a)
print("parent move graph: %d states, %d edges, degrees %s"%(N,len(E),sorted(set(len(x) for x in nb))))

def ncomp(alive):
    seen=set(); c=0
    for s in range(N):
        if s in alive and s not in seen:
            c+=1; dq=deque([s]); seen.add(s)
            while dq:
                x=dq.popleft()
                for y in nb[x]:
                    if y in alive and y not in seen: seen.add(y); dq.append(y)
    return c
full=set(range(N))
print("connected as a whole:", ncomp(full)==1)
# minimum number of states whose REMOVAL disconnects the move graph (min vertex cut)
best=None
for k in range(1,N):
    hit=False
    for rem in itertools.combinations(range(N),k):
        alive=full-set(rem)
        if not alive: continue
        if ncomp(alive)>1: best=(k,rem); hit=True; break
    if hit: break
print("MINIMUM vertex cut of the parent's move graph: %d states  (example %s)"%(best[0],best[1]))
# what the prism attachment actually removed
S=[2,3,4]
excl=[i for i,c in enumerate(cols) if len({c[s] for s in S})>=q]
alive=full-set(excl)
print("the prism attachment excluded %d states and left %d components"%(len(excl),ncomp(alive)))
print("  price actually paid: %d states per bit;  theoretical floor (min cut): %d"%(len(excl),best[0]))
# spectral gap / conductance of the parent class, for the rung-3 rate
import random
random.seed(1)
dmax=max(len(x) for x in nb)
def gap():
    # power iteration on the lazy walk, second eigenvalue
    import copy
    v=[random.random()-0.5 for _ in range(N)]
    m=sum(v)/N; v=[x-m for x in v]
    lam=0
    for _ in range(4000):
        w=[0.0]*N
        for i in range(N):
            w[i]+=v[i]*(1-len(nb[i])/dmax)
            for j in nb[i]: w[j]+=v[i]/dmax
        m=sum(w)/N; w=[x-m for x in w]
        nrm=math.sqrt(sum(x*x for x in w))
        if nrm<1e-14: return 0.0
        v=[x/nrm for x in w]; lam=nrm
    return 1-lam
print("lazy-walk spectral gap of the parent class: %.4f  (relaxation time %.2f steps)"%(gap(),1/gap()))
