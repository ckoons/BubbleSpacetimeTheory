# Cal's independent certificate check — written from scratch, no project modules.
# Witness: n=17, plantri -c5 graph 0, v=4, first coloring row of play/.in_frame_26_two_word_locked.json
import subprocess, json, itertools, sys
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

out=subprocess.run(['tools/plantri58/plantri','-c5','17'],capture_output=True).stdout
G=read_planar_code(out); print("graphs:",len(G))
adj=G[0]; n=len(adj)
deg=[len(a) for a in adj]; print("degrees:",sorted(deg)); assert min(deg)>=5
# every edge lies in exactly two triangles  <=> no separating triangle (in a triangulation)
sep_tri=sum(1 for u in range(n) for w in adj[u] if u<w and len(set(adj[u])&set(adj[w]))!=2)
print("edges with common-neighbour count != 2 (separating triangles):",sep_tri)

rows=[r for r in json.load(open('.in_frame_26_two_word_locked.json')) if r['n']==17 and r['graph_index_plantri_c5']==0]
row=rows[0]; col_list=row['coloring_mod_S4_sorted_order']

def build(vzero):
    others=[u for u in range(n) if u!=vzero]; c={u:col_list[k] for k,u in enumerate(others)}; return c
def proper(c,v):
    return all(c[u]!=c[w] for u in c for w in adj[u] if w!=v and u<w)
v=None
for cand in (row['v'], row['v']-1):
    c=build(cand)
    if proper(c,cand): v=cand; c0=c; break
print("v (0-based) =",v,"proper:",proper(c0,v)); assert v is not None
link=adj[v]; print("link colours (plantri cyclic order):",[c0[u] for u in link])

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
def tau(c): return sum(tangled(c,a,b) for a,b in itertools.combinations(range(4),2))
def insertable(c): return len({c[u] for u in link})<4
def gate(c): return insertable(c) or tau(c)<=5

print("tau(c0) =",tau(c0),"insertable:",insertable(c0))
assert tau(c0)==6 and not insertable(c0)

def moves(c): return [(u,frozenset((c[u],x))) for u in link for x in range(4) if x!=c[u]]
def apply_word(c,m1,m2):
    c=dict(c); legal=0
    for (seed,pair) in (m1,m2,m1,m2):
        if c[seed] in pair:
            legal+=1
            for x in chain(c,seed,pair): c[x]=[p for p in pair if p!=c[x]][0]
    return c,legal
def words(c):
    M=moves(c); return [(m1,m2) for m1 in M for m2 in M if m1[1]!=m2[1]]

W=words(c0); print("moves:",len(moves(c0)),"words:",len(W))
full=[]; anygate_full=0; anygate_any=0; images=[]
for m1,m2 in W:
    img,legal=apply_word(c0,m1,m2)
    if gate(img):
        anygate_any+=1
        if legal==4: anygate_full+=1
    if legal==4: full.append((m1,m2)); images.append(img)
print("fully-legal words:",len(full),"| gate reached by a fully-legal word:",anygate_full,"| by ANY word incl. no-op stages:",anygate_any)
print("image tau distribution (fully legal):",sorted(tau(i) for i in images))
# depth 2 from each fully-legal (stuck) image, alphabet re-derived in the image
exits=0; exit_words=set()
for img in images:
    ok=False
    for m1,m2 in words(img):
        im2,l2=apply_word(img,m1,m2)
        if l2==4 and gate(im2): ok=True; exit_words.add((tuple(sorted(m1[1])),tuple(sorted(m2[1]))))
    exits+=ok
print("depth-2: images with a fully-legal exit:",exits,"/",len(images))
# single-swap null on c0
null=0
for u in [x for x in range(n) if x!=v]:
    for x in range(4):
        if x!=c0[u]:
            c=dict(c0)
            for y in chain(c0,u,(c0[u],x)): c[y]=x if c[y]==c0[u] else c0[u]
            null+=gate(c)
print("single-swap null (any seed, any pair) reaching gate:",null)
distinct=len({tuple(sorted(i.items())) for i in images}); print("distinct fully-legal images:",distinct)
# per distinct image: number of fully-legal second words that exit
seen={}
for img in images:
    k=tuple(sorted(img.items()))
    if k in seen: continue
    cnt=sum(1 for m1,m2 in words(img) if (lambda r: r[1]==4 and gate(r[0]))(apply_word(img,m1,m2)))
    seen[k]=cnt
print("exit-word counts per distinct image:",sorted(seen.values()))
print("distinct images with an exit:",sum(1 for x in seen.values() if x>0),"/",len(seen))

# --- roles from the link cycle (plantri gives cyclic order), bridge words W_i/W_j, and W' at their images ---
def roles(c):
    L=link; cols=[c[u] for u in L]; r=[x for x in range(4) if cols.count(x)==2][0]
    B=[u for u in L if c[u]==r]; assert len(B)==2
    # middle = link vertex adjacent (on the link cycle) to both copies
    def lk_adj(a,b): 
        i,j=L.index(a),L.index(b); return (i-j)%5 in (1,4)
    mid=[u for u in L if c[u]!=r and lk_adj(u,B[0]) and lk_adj(u,B[1])]; assert len(mid)==1
    sing=[u for u in L if c[u]!=r and u!=mid[0]]
    return r,B,mid[0],sing
def bridge_words(c):
    r,B,mid,sing=roles(c); out=[]
    for Bnear in B:
        # singleton adjacent to Bnear on the link = the pair partner
        s_adj=[s for s in sing if (link.index(s)-link.index(Bnear))%5 in (1,4)][0]
        Bfar=[b for b in B if b!=Bnear][0]; s_far=[s for s in sing if s!=s_adj][0]
        out.append(((Bnear,frozenset((r,c[s_adj]))),(Bfar,frozenset((r,c[s_far])))))
    return out  # [W_i, W_j] in Lyra's shape: each copy swapped with its ADJACENT singleton's pair
for name,(m1,m2) in zip(("W_a","W_b"),bridge_words(c0)):
    img,legal=apply_word(c0,m1,m2); print(name,"legal stages:",legal,"image tau:",tau(img),"insertable:",insertable(img))
    assert legal==4
    # W' in the image's own frame
    for name2,(q1,q2) in zip(("W'_a","W'_b"),bridge_words(img)):
        im2,l2=apply_word(img,q1,q2); print("   ",name2,"legal:",l2,"gate:",gate(im2),"tau:",tau(im2))
    nexit=sum(1 for a,b in words(img) if (lambda r:r[1]==4 and gate(r[0]))(apply_word(img,a,b)))
    print("    any-word exits from this image:",nexit)
