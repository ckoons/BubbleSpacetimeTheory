# Cal: T1 on a third instrument — plain Kempe swaps (no commutator) on all 349 locks. From scratch.
import subprocess, json, itertools, hashlib
from collections import deque, Counter
def read_planar_code(data):
    assert data.startswith(b'>>planar_code<<'); i=len(b'>>planar_code<<'); graphs=[]
    while i < len(data):
        n=data[i]; i+=1; adj=[[] for _ in range(n)]
        for u in range(n):
            while data[i]!=0: adj[u].append(data[i]-1); i+=1
            i+=1
        graphs.append(adj)
    return graphs
files=['.in_frame_26_two_word_locked.json','.in_frame_23_two_word_locked_n22.json','.in_frame_44_two_word_locked_n23.json','.in_frame_256_two_word_locked_n24.json']
rows=[r for f in files for r in json.load(open(f))]; cache={}
def graphs(n):
    if n not in cache: cache[n]=read_planar_code(subprocess.run(['tools/plantri58/plantri','-c5',str(n)],capture_output=True).stdout)
    return cache[n]
res=[]
for row in rows:
    n=row['n']; adj=graphs(n)[row['graph_index_plantri_c5']]; N=len(adj); col=row['coloring_mod_S4_sorted_order']; v=row['v']
    others=[u for u in range(N) if u!=v]; c0={u:col[k] for k,u in enumerate(others)}; link=adj[v]
    def chain(c,seed,pair):
        seen={seed}; dq=deque([seed])
        while dq:
            x=dq.popleft()
            for y in adj[x]:
                if y!=v and y not in seen and c[y] in pair: seen.add(y); dq.append(y)
        return seen
    def swap(c,seed,pair):
        c=dict(c)
        for x in chain(c,seed,pair): c[x]=[p for p in pair if p!=c[x]][0]
        return c
    def tangled(c,a,b):
        A=[u for u in link if c[u]==a]; B=[u for u in link if c[u]==b]
        if not A or not B: return False
        comps=[]; done=set()
        for u in A+B:
            if u in done: continue
            K=chain(c,u,(a,b)); done|=K; comps.append(K)
        return not any((all(u in K for u in A) and not any(u in K for u in B)) or (all(u in K for u in B) and not any(u in K for u in A)) for K in comps)
    tau=lambda c: sum(tangled(c,a,b) for a,b in itertools.combinations(range(4),2))
    gate=lambda c: len({c[u] for u in link})<4 or tau(c)<=5
    def roles(c):
        cols=[c[u] for u in link]; r=[x for x in range(4) if cols.count(x)==2][0]; B=[u for u in link if c[u]==r]
        la=lambda a,b:(link.index(a)-link.index(b))%5 in (1,4)
        M=[u for u in link if c[u]!=r and la(u,B[0]) and la(u,B[1])][0]; sing=[u for u in link if c[u]!=r and u!=M]
        B2=B[0]; Si=[s for s in sing if la(s,B2)][0]; B1=B[1]; Sj=[s for s in sing if s!=Si][0]
        return r,B1,B2,M,Si,Sj
    assert tau(c0)==6
    r,B1,B2,M,Si,Sj=roles(c0); si,sj=c0[Si],c0[Sj]
    # (i) single-swap null, every seed in T-v, every pair
    null1=sum(1 for u in others for x in range(4) if x!=c0[u] and gate(swap(c0,u,(c0[u],x))))
    # (ii) single link-seeded switch (Kittell alphabet, all 15 seed-pair moves)
    lmoves=lambda c: [(u,(c[u],x)) for u in link for x in range(4) if x!=c[u]]
    k1=sum(1 for (u,p) in lmoves(c0) if gate(swap(c0,u,p)))
    # (iii) two link-seeded switches, second re-derived in the image (Kittell convention); count sequences and whether any exits
    k2=0; k2seq=[]
    for (u,p) in lmoves(c0):
        c1=swap(c0,u,p)
        if gate(c1): continue
        for (u2,p2) in lmoves(c1):
            if gate(swap(c1,u2,p2)): k2+=1; k2seq.append(((u,p),(u2,p2)))
    # (iv) Kempe's pairing: zeta = (B1,(r,si)) then eta = (B2,(r,sj)) as plain swaps; and reverse
    zeta_eta=gate(swap(swap(c0,B1,(r,si)),B2,(r,sj))); eta_zeta=gate(swap(swap(c0,B2,(r,sj)),B1,(r,si)))
    # (v) two ANY swaps: first swap at any vertex, second at any vertex -- restricted to link-seeded second for cost
    any2=0
    for u in others:
        for x in range(4):
            if x==c0[u]: continue
            c1=swap(c0,u,(c0[u],x))
            if gate(c1): continue
            if any(gate(swap(c1,u2,p2)) for (u2,p2) in lmoves(c1)): any2+=1
    res.append(dict(n=n,g=row['graph_index_plantri_c5'],v=v,null1=null1,k1=k1,k2=k2,zeta_eta=zeta_eta,eta_zeta=eta_zeta,any2=any2))
raw=json.dumps(res,sort_keys=True); print("witnesses",len(res),"sha256",hashlib.sha256(raw.encode()).hexdigest()[:16]); open('.cal_T1_349.json','w').write(raw)
print("single-swap null (any seed) reaches gate on:",sum(1 for x in res if x['null1']>0),"/",len(res))
print("single link-seeded switch reaches gate on:",sum(1 for x in res if x['k1']>0),"/",len(res))
print("Kempe pairing zeta-then-eta inserts:",sum(x['zeta_eta'] for x in res),"| eta-then-zeta:",sum(x['eta_zeta'] for x in res))
print("two link-seeded switches (Kittell, re-derived) reach gate on:",sum(1 for x in res if x['k2']>0),"/",len(res),"| sequences per witness:",Counter(x['k2'] for x in res).most_common(6))
print("first swap ANYWHERE then a link-seeded switch reaches gate on:",sum(1 for x in res if x['any2']>0),"/",len(res))
