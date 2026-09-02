# Cal: Lane A existence check on all 49 in-frame two-word-locked witnesses (own instrument, no project modules)
import subprocess, json, itertools
from collections import deque
def read_planar_code(data):
    assert data.startswith(b'>>planar_code<<'); i=len(b'>>planar_code<<'); graphs=[]
    while i < len(data):
        n=data[i]; i+=1; adj=[[] for _ in range(n)]
        for u in range(n):
            while data[i]!=0: adj[u].append(data[i]-1); i+=1
            i+=1
        graphs.append(adj)
    return graphs
rows=json.load(open('.in_frame_26_two_word_locked.json'))+json.load(open('.in_frame_23_two_word_locked_n22.json'))
cache={}
def graphs(n):
    if n not in cache: cache[n]=read_planar_code(subprocess.run(['tools/plantri58/plantri','-c5',str(n)],capture_output=True).stdout)
    return cache[n]
tot=0; locked_ok=0; bridge_img_stuck=0; bridge_img_noexit=0; wprime_exit=0; wprime_stuck=0; exit_first_types={}
for row in rows:
    n=row['n']; adj=graphs(n)[row['graph_index_plantri_c5']]; N=len(adj)
    col=row['coloring_mod_S4_sorted_order']
    def build(vz): 
        others=[u for u in range(N) if u!=vz]; return {u:col[k] for k,u in enumerate(others)}
    def proper(c,vv): return all(c[u]!=c[w] for u in c for w in adj[u] if w!=vv and u<w)
    v=row['v']; c0=build(v); assert proper(c0,v), row
    link=adj[v]
    def chain(c,seed,pair):
        seen={seed}; dq=deque([seed])
        while dq:
            x=dq.popleft()
            for y in adj[x]:
                if y!=v and y not in seen and c[y] in pair: seen.add(y); dq.append(y)
        return seen
    def tangled(c,a,b):
        A=[u for u in link if c[u]==a]; B=[u for u in link if c[u]==b]
        if not A or not B: return False
        comps=[]; done=set()
        for u in A+B:
            if u in done: continue
            K=chain(c,u,(a,b)); done|=K; comps.append(K)
        for K in comps:
            if all(u in K for u in A) and not any(u in K for u in B): return False
            if all(u in K for u in B) and not any(u in K for u in A): return False
        return True
    tau=lambda c: sum(tangled(c,a,b) for a,b in itertools.combinations(range(4),2))
    insertable=lambda c: len({c[u] for u in link})<4
    gate=lambda c: insertable(c) or tau(c)<=5
    moves=lambda c: [(u,frozenset((c[u],x))) for u in link for x in range(4) if x!=c[u]]
    def apply_word(c,m1,m2):
        c=dict(c); legal=0
        for (seed,pair) in (m1,m2,m1,m2):
            if c[seed] in pair:
                legal+=1
                for x in chain(c,seed,pair): c[x]=[p for p in pair if p!=c[x]][0]
        return c,legal
    words=lambda c: [(a,b) for a in moves(c) for b in moves(c) if a[1]!=b[1]]
    def roles(c):
        L=link; cols=[c[u] for u in L]; r=[x for x in range(4) if cols.count(x)==2][0]
        B=[u for u in L if c[u]==r]; la=lambda a,b:(L.index(a)-L.index(b))%5 in (1,4)
        mid=[u for u in L if c[u]!=r and la(u,B[0]) and la(u,B[1])][0]; sing=[u for u in L if c[u]!=r and u!=mid]
        return r,B,mid,sing
    def bridge_words(c):
        r,B,mid,sing=roles(c); out=[]
        for Bn in B:
            sa=[s for s in sing if (link.index(s)-link.index(Bn))%5 in (1,4)][0]; Bf=[b for b in B if b!=Bn][0]; sf=[s for s in sing if s!=sa][0]
            out.append(((Bn,frozenset((r,c[sa]))),(Bf,frozenset((r,c[sf])))))
        return out
    def rtype(c,u):
        r,B,mid,sing=roles(c); return 'B' if u in B else ('M' if u==mid else 'S')
    tot+=1
    assert tau(c0)==6 and not insertable(c0)
    W=words(c0); imgs=[(w,)+apply_word(c0,*w) for w in W]
    assert not any(l==4 and gate(i) for w,i,l in imgs)  # locked
    locked_ok+=1
    # depth-2 exits: which FIRST words lead to an image with an exit
    for w,i,l in imgs:
        if l!=4: continue
        if any((lambda r:r[1]==4 and gate(r[0]))(apply_word(i,a,b)) for a,b in words(i)):
            t=(rtype(c0,w[0][0]),rtype(c0,w[1][0])); exit_first_types[t]=exit_first_types.get(t,0)+1
    for m1,m2 in bridge_words(c0):
        img,l=apply_word(c0,m1,m2); assert l==4
        if not gate(img):
            bridge_img_stuck+=1
            anyexit=any((lambda r:r[1]==4 and gate(r[0]))(apply_word(img,a,b)) for a,b in words(img))
            bridge_img_noexit+= (not anyexit)
            for q1,q2 in bridge_words(img):
                im2,l2=apply_word(img,q1,q2)
                if l2==4 and gate(im2): wprime_exit+=1
                else: wprime_stuck+=1
print("witnesses:",tot,"locked confirmed:",locked_ok)
print("bridge-word images (2 per witness):",2*tot,"| stuck:",bridge_img_stuck,"| stuck AND no exit by any word:",bridge_img_noexit)
print("W' (both orderings) at stuck bridge images: exits",wprime_exit,"| stuck again",wprime_stuck)
print("first-word seed-role types (copy B / middle M / singleton S) whose image HAS a depth-2 exit, counted over words:",exit_first_types)
