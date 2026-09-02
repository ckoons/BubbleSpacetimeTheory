# Cal: H_cut third instrument on all 93 in-frame two-word-locked witnesses (n<=23). From scratch; no project modules.
import subprocess, json, itertools, hashlib
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
rows=json.load(open('.in_frame_26_two_word_locked.json'))+json.load(open('.in_frame_23_two_word_locked_n22.json'))+json.load(open('.in_frame_44_two_word_locked_n23.json'))
cache={}
def graphs(n):
    if n not in cache: cache[n]=read_planar_code(subprocess.run(['tools/plantri58/plantri','-c5',str(n)],capture_output=True).stdout)
    return cache[n]
table=[]
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
    moves=lambda c: [(u,frozenset((c[u],x))) for u in link for x in range(4) if x!=c[u]]
    def apply_word(c,m1,m2):
        c=dict(c); legal=0; chains=[]
        for (seed,pair) in (m1,m2,m1,m2):
            if c[seed] in pair:
                legal+=1; X=chain(c,seed,pair); chains.append((pair,X))
                for x in X: c[x]=[p for p in pair if p!=c[x]][0]
            else: chains.append((pair,set()))
        return c,legal,chains
    words=lambda c: [(a,b) for a in moves(c) for b in moves(c) if a[1]!=b[1]]
    def roles(c):
        L=link; cols=[c[u] for u in L]; r=[x for x in range(4) if cols.count(x)==2][0]
        B=[u for u in L if c[u]==r]; la=lambda a,b:(L.index(a)-L.index(b))%5 in (1,4)
        mid=[u for u in L if c[u]!=r and la(u,B[0]) and la(u,B[1])][0]; sing=[u for u in L if c[u]!=r and u!=mid]
        # B2 := copy adjacent to n_si; define n_si as the singleton adjacent to B[0]? fix: choose names by B[0]
        Bn=B[0]; s_adj=[s for s in sing if la(s,Bn)][0]; s_far=[s for s in sing if s!=s_adj][0]
        # name: B2=Bn (adjacent to n_si:=s_adj), B1=other copy (adjacent to n_sj:=s_far)
        return dict(r=r,sM=c[mid],si=c[s_adj],sj=c[s_far],B2=Bn,B1=B[1],M=mid,Si=s_adj,Sj=s_far)
    R=roles(c0); rname={R['B1']:'B1',R['B2']:'B2',R['M']:'M',R['Si']:'Si',R['Sj']:'Sj'}; cname={R['r']:'r',R['sM']:'sM',R['si']:'si',R['sj']:'sj'}
    def wname(m1,m2): return ((rname[m1[0]],tuple(sorted(cname[x] for x in m1[1]))),(rname[m2[0]],tuple(sorted(cname[x] for x in m2[1]))))
    # bridge words and cuts
    Wi=((R['B2'],frozenset((R['r'],R['si']))),(R['B1'],frozenset((R['r'],R['sj']))))
    Wj=((R['B1'],frozenset((R['r'],R['sj']))),(R['B2'],frozenset((R['r'],R['si']))))  # mirror: copy B1 with its adjacent singleton n_sj first
    cuts={}
    for nm,W in (('Ci',Wi),('Cj',Wj)):
        img,l,ch=apply_word(c0,*W); assert l==4 and not gate(img)
        X3=ch[2][1]; X4=ch[3][1]; C=X3&X4
        # colour of cut vertices in c3 (after stage 3): recompute c3
        c3=dict(c0)
        for (pair,X) in ch[:3]:
            for x in X: c3[x]=[p for p in pair if p!=c3[x]][0]
        cuts[nm]=dict(C=C,c3r=all(c3[x]==R['r'] for x in C),c0cols=[cname[c0[x]] for x in C],size=len(C),X3=len(X3))
    rec=dict(n=n,g=row['graph_index_plantri_c5'],v=v,cut_i=cuts['Ci']['size'],cut_j=cuts['Cj']['size'],cut_i_r_in_c3=cuts['Ci']['c3r'],cut_j_r_in_c3=cuts['Cj']['c3r'],
             cut_i_c0cols=cuts['Ci']['c0cols'],cut_j_c0cols=cuts['Cj']['c0cols'],words=[])
    rsM=frozenset((R['r'],R['sM']))
    for m1,m2 in words(c0):
        img,l,ch=apply_word(c0,m1,m2)
        if l!=4: continue
        exit_=False; second_is_bridge=False
        for a,b in words(img):
            im2,l2,_=apply_word(img,a,b)
            if l2==4 and gate(im2):
                exit_=True
                R2=roles(img); isB=lambda m: m[0] in (R2['B1'],R2['B2']) and R2['r'] in m[1] and R2['sM'] not in m[1]
                if isB(a) and isB(b): second_is_bridge=True
        def contains(pairsel,C): return any(pair==pairsel and C<=X for pair,X in ch) if C else None
        def contains_any(C): return any(C<=X for pair,X in ch) if C else None
        rec['words'].append(dict(w=wname(m1,m2),exit=exit_,second_bridge=second_is_bridge,
            pairsp_i=contains(rsM,cuts['Ci']['C']),pairsp_j=contains(rsM,cuts['Cj']['C']),
            any_i=contains_any(cuts['Ci']['C']),any_j=contains_any(cuts['Cj']['C']),touch_sM=any(R['sM'] in m[1] for m in (m1,m2))))
    table.append(rec)
raw=json.dumps(table,sort_keys=True,default=list); h=hashlib.sha256(raw.encode()).hexdigest()[:16]
open('.cal_Hcut_93_table.json','w').write(raw); print("witnesses:",len(table),"raw table sha256:",h)
print("cut nonempty (i/j):",sum(r['cut_i']>0 for r in table),sum(r['cut_j']>0 for r in table),"| cut r-coloured in c3 (i/j):",sum(r['cut_i_r_in_c3'] for r in table),sum(r['cut_j_r_in_c3'] for r in table))
from collections import Counter
print("cut sizes i:",Counter(r['cut_i'] for r in table),"j:",Counter(r['cut_j'] for r in table))
print("c0-colour of cut vertices (i+j):",Counter(x for r in table for x in r['cut_i_c0cols']+r['cut_j_c0cols']))
ws=[w for r in table for w in r['words']]; ex=[w for w in ws if w['exit']]; nx=[w for w in ws if not w['exit']]
print("fully-legal first words:",len(ws),"exiting:",len(ex),"non-exiting:",len(nx))
print("exiting: second word is a bridge word (in image frame):",sum(w['second_bridge'] for w in ex),"/",len(ex))
def cnt(ls,k): return sum(1 for w in ls if w[k])
for k in ('pairsp_i','pairsp_j','any_i','any_j','touch_sM'):
    print(f"  {k}: exiting {cnt(ex,k)}/{len(ex)} | non-exiting {cnt(nx,k)}/{len(nx)}")
print("  pair-specific (i OR j): exiting",sum(1 for w in ex if w['pairsp_i'] or w['pairsp_j']),"/",len(ex),"| non-exiting",sum(1 for w in nx if w['pairsp_i'] or w['pairsp_j']),"/",len(nx))
print("  pair-specific (i AND j): exiting",sum(1 for w in ex if w['pairsp_i'] and w['pairsp_j']),"/",len(ex),"| non-exiting",sum(1 for w in nx if w['pairsp_i'] and w['pairsp_j']),"/",len(nx))
# s_M-touching orbits that fail, and the four-orbit out-of-sample test on the 44 (n=23)
four={(('M',('r','sM')),('Si',('sM','si'))),(('B1',('r','si')),('B2',('r','sM'))),(('Si',('r','si')),('M',('sM','si'))),(('B1',('r','sj')),('B2',('r','sM')))}
def mirror(w): 
    sw=lambda s: {'B1':'B2','B2':'B1','Si':'Sj','Sj':'Si'}.get(s,s); cs=lambda t: tuple(sorted({'si':'sj','sj':'si'}.get(x,x) for x in t))
    return ((sw(w[0][0]),cs(w[0][1])),(sw(w[1][0]),cs(w[1][1])))
fourm=four|{mirror(w) for w in four}
n23=[r for r in table if r['n']==23]
hit=sum(1 for r in n23 if any(w['exit'] for w in r['words'] if tuple(w['w']) in fourm or w['w'] in fourm))
allfour=sum(1 for r in n23 if all(any(w['exit'] and (w['w'] in fourm) for w in r['words'] if w['w']==f) for f in fourm if any(w['w']==f for w in r['words'])))
print("n=23 out-of-sample: witnesses",len(n23),"| some word of the four orbits (or mirror) exits:",hit,"| every legal member of the four exits:",allfour)
fail_sM=Counter(w['w'] for w in nx if w['touch_sM']); print("distinct s_M-touching first-word names that FAIL somewhere:",len(fail_sM),"(of",len(set(w['w'] for w in ws if w['touch_sM'])),"s_M-touching names seen)")
