# Cal: far-chain necessity + 6-bit c0 type on all 349 in-frame two-word-locked witnesses (n<=24). From scratch.
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
rows=[r for f in files for r in json.load(open(f))]
cache={}
def graphs(n):
    if n not in cache: cache[n]=read_planar_code(subprocess.run(['tools/plantri58/plantri','-c5',str(n)],capture_output=True).stdout)
    return cache[n]
out=[]
for row in rows:
    n=row['n']; adj=graphs(n)[row['graph_index_plantri_c5']]; N=len(adj); col=row['coloring_mod_S4_sorted_order']; v=row['v']
    others=[u for u in range(N) if u!=v]; c={u:col[k] for k,u in enumerate(others)}; link=adj[v]
    def chain(seed,pair):
        seen={seed}; dq=deque([seed])
        while dq:
            x=dq.popleft()
            for y in adj[x]:
                if y!=v and y not in seen and c[y] in pair: seen.add(y); dq.append(y)
        return seen
    cols=[c[u] for u in link]; r=[x for x in range(4) if cols.count(x)==2][0]
    B=[u for u in link if c[u]==r]; la=lambda a,b:(link.index(a)-link.index(b))%5 in (1,4)
    M=[u for u in link if c[u]!=r and la(u,B[0]) and la(u,B[1])][0]; sing=[u for u in link if c[u]!=r and u!=M]
    B2=B[0]; Si=[s for s in sing if la(s,B2)][0]; B1=B[1]; Sj=[s for s in sing if s!=Si][0]
    sM,si,sj=c[M],c[Si],c[Sj]
    K=dict(theta=chain(M,(r,sM)),alpha=chain(M,(sM,si)),beta=chain(M,(sM,sj)),eps=chain(Si,(si,sj)),
           delta=chain(B2,(r,si)),zeta=chain(B1,(r,si)),gamma=chain(B1,(r,sj)),eta=chain(B2,(r,sj)))
    names=list(K); bits={}
    for a,b in itertools.combinations(names,2): bits[a+'-'+b]=int(bool(K[a]&K[b]))
    far=(bits['alpha-zeta'],bits['beta-eta'],bits['eps-zeta'],bits['eps-eta'])
    free=(bits['alpha-zeta'],bits['beta-eta'],bits['eps-zeta'],bits['eps-eta'],bits['delta-gamma'],bits['zeta-eta'])
    out.append(dict(n=n,g=row['graph_index_plantri_c5'],v=v,bits=bits,far=far,free=free))
raw=json.dumps(out,sort_keys=True); print("witnesses:",len(out),"sha256:",hashlib.sha256(raw.encode()).hexdigest()[:16]); open('.cal_farchain_349.json','w').write(raw)
# forced-bit control
const={k:len({o['bits'][k] for o in out}) for k in out[0]['bits']}; varying=[k for k,vv in const.items() if vv>1]
print("varying bits across the 349:",varying)
print("far-chain condition (all four =1):",sum(1 for o in out if all(o['far'])),"/",len(out))
for n in (17,21,22,23,24):
    sub=[o for o in out if o['n']==n]; print(f"  n={n}: {sum(1 for o in sub if all(o['far']))}/{len(sub)} far-chain; free-bit types: {Counter(o['free'] for o in sub)}")
print("free-bit types over all 349:",Counter(o['free'] for o in out))
