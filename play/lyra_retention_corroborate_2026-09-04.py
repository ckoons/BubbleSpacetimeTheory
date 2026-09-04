import itertools, random
from retention import colourings, adj_of, classes
random.seed(11)
# CLAIM (proved by the retraction argument): if G is an INDUCED subgraph of G' and A
# extends colourings without altering the parent part, then A never MERGES classes,
# for any q and any extension rule.  Search for a counterexample.
def trial(n,q,padd,nnew,rule):
    E=[e for e in itertools.combinations(range(n),2) if random.random()<padd]
    if not E: return None
    cols=colourings(n,E,q)
    if len(cols)<2: return None
    adj=adj_of(n,E); pc,pn,pidx=classes(cols,adj,q)
    if pn<2: return None                      # need >1 parent class to test merging
    e2=list(E)
    for j in range(nnew):
        w=n+j
        S=[v for v in range(w) if random.random()<0.5]
        for s in S: e2.append((s,w))
    N=n+nnew
    cols2=colourings(N,e2,q)
    if not cols2: return None
    cc,cn,cidx=classes(cols2,adj_of(N,e2),q)
    # extension rule: greedy, choosing the rule-th available colour
    back={}; fwd={}
    for k,c in enumerate(cols):
        d=list(c)
        for j in range(nnew):
            w=n+j
            used={d[u] for (u,v) in e2 if v==w and u<w}|{d[v] for (u,v) in e2 if u==w and v<w}
            free=[x for x in range(q) if x not in used]
            if not free: return None
            d.append(free[rule%len(free)])
        t=tuple(d)
        if t not in cidx: return None
        ch=cc[cidx[t]]
        back.setdefault(ch,set()).add(pc[k]); fwd.setdefault(pc[k],set()).add(ch)
    merge=any(len(v)>1 for v in back.values()); split=any(len(v)>1 for v in fwd.values())
    return pn,cn,merge,split

tested=0; merged=0; split=0; multiclass=0
for t in range(4000):
    n=random.choice([5,6,7]); q=random.choice([3,3,4]); nnew=random.choice([1,1,2])
    r=trial(n,q,random.choice([0.5,0.6,0.7]),nnew,random.randint(0,2))
    if r is None: continue
    tested+=1; multiclass+=1
    if r[2]: merged+=1
    if r[3]: split+=1
print("vertex-addition trials with a multi-class parent: %d"%tested)
print("  merged: %d      split: %d"%(merged,split))
print("CLAIM (never merges) %s"%("HOLDS on this sample" if merged==0 else "FALSIFIED"))
