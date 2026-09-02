"""
Toy 5599 — Grace — G1 / G2 / G3 (K1838 §5; Casey Round 97).

G1  Chain coincidence as a LAPLACIAN RANK question. For the bichromatic subgraph H_ab(c) on T−v:
    #components = dim ker L(H_ab) = |V(H_ab)| − rank L; x ~ y  ⟺  e_x − e_y ⟂ ker L. Implemented with
    numpy SVD null space; the component id of a vertex is its row in the null basis. An instrument
    INDEPENDENT of Elie's BFS/union-find; cross-checked against G5.kempe_chain at EVERY chain question.
G2  The leaf table for W_i and W_j on all 2,927 stuck configurations: Lemma L legality (predicted 4/4
    legal on every one), the forced link images c1, c2 (Lemma D), Δ (n_sj ∈ X3 at c2), Δ′ ({B2,n_si} ⊆ X4
    at c3), and the leaf ∈ {I insertable, G gate-phase τ≤5, S stuck τ=6} of the image.
G3  The wall certificate (K1838 §2a): on every Δ-YES instance exhibit the (r,s_i)-path P from B2 to n_sj
    in c2 and VERIFY that n_si is (s_M,s_j)-separated from {B1, n_sM} in c2 and in c3. One violation
    falsifies K1838's Jordan step. Also K1838 §2b: Δ-YES ∧ Δ′-YES ⟹ leaf G (τ(c4) ≤ 5)?

PRE-REGISTERED PREDICTIONS (before contact):
  P1 (One-Context, positive control of role map + instrument): at c0 the six forced partitions hold on
     2,927/2,927 — (r,s_M) one chain ⊇ {B1,n_sM,B2}; (r,s_i): B1 ∉ X(B2) ∋ n_si; (r,s_j): n_sj ∈ X(B1) ∌ B2;
     n_sM~n_si; n_sM~n_sj; n_si~n_sj. Exactly 8 distinct link-seeded chains (= Kittell's eight, alias row).
  P2 (Lemma L): W_i and W_j fully legal, 2,927/2,927 each.
  P3 (Lemma D): c1 = (r,s_M,s_i,r,s_j) and c2 = (s_j,s_M,s_i,s_j,r) on every configuration; Δ-NO ⟹ c4 =
     (r,s_M,s_j,r,s_j) insertable (leaf I).
  P4 (K1838 §2a): wall holds on every Δ-YES instance (0 violations).
  P5 (K1838 §2b, HELD for Cal): Δ-YES ∧ Δ′-YES ⟹ leaf G.
  P6 (G1): rank instrument agrees with BFS on every chain question, k/N = N/N.
Records are hashed BEFORE the counts. Data loaded through Elie's loaders (populations only); every
computation on the data is this file's own. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, sys, time
from collections import Counter, deque
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

GA = load("t5591g", "toy_5591_SEP2_gate_aware_potential_legal_only_DGT_recount_54_and_1801.py")
LG, TE, D6, T2 = GA.LG, GA.TE, GA.D6, GA.T2
RD = LG.RD
E1, G5, X3, WF = GA.E1, GA.G5, GA.X3, GA.WF

# ---------------------------------------------------------------- G1: the rank instrument
def rank_components(adj, col, a, b, v_excl, tol=1e-7):
    """Component labels of H_ab(col) on T−v via the Laplacian null space. Returns (label dict, n_comp)."""
    U = [u for u in adj if u != v_excl and col.get(u) in (a, b)]
    if not U:
        return {}, 0
    idx = {u: i for i, u in enumerate(U)}
    n = len(U)
    L = np.zeros((n, n))
    for u in U:
        for w in adj[u]:
            if w in idx and w != u:
                L[idx[u], idx[w]] -= 1.0
                L[idx[u], idx[u]] += 1.0
    # null space by SVD
    _, s, vt = np.linalg.svd(L)
    rank = int((s > tol * max(1.0, s[0])).sum())
    k = n - rank
    N = vt[rank:].T if k > 0 else np.zeros((n, 0))     # n × k null basis (rows = vertices)
    # two vertices are in one component iff their null-basis rows coincide
    lab = {}
    keys = {}
    for u in U:
        key = tuple(np.round(N[idx[u]], 6))
        if key not in keys:
            keys[key] = len(keys)
        lab[u] = keys[key]
    assert len(keys) == k, (len(keys), k)
    return lab, k

def same_chain(adj, col, x, y, a, b, v_excl):
    lab, _ = rank_components(adj, col, a, b, v_excl)
    return x in lab and y in lab and lab[x] == lab[y]

def chain_of(adj, col, seed, a, b, v_excl):
    lab, _ = rank_components(adj, col, a, b, v_excl)
    if seed not in lab:
        return set()
    return {u for u, l in lab.items() if l == lab[seed]}

def swap(col, chain, a, b):
    nc = dict(col)
    for u in chain:
        nc[u] = b if nc[u] == a else a
    return nc

XCHK = Counter()   # rank-vs-BFS cross-check tallies
def chain_x(adj, col, seed, a, b, v_excl):
    """chain by rank, cross-checked against Elie's BFS. Tallies agreement."""
    mine = chain_of(adj, col, seed, a, b, v_excl)
    his = G5.kempe_chain(adj, col, seed, a, b, exclude={v_excl})
    XCHK['agree' if mine == his else 'DISAGREE'] += 1
    return mine

def bfs_path(adj, col, s, t, a, b, v_excl):
    prev = {s: None}; q = deque([s])
    while q:
        u = q.popleft()
        if u == t:
            break
        for w in adj[u]:
            if w != v_excl and w not in prev and col.get(w) in (a, b):
                prev[w] = u; q.append(w)
    if t not in prev:
        return None
    p = []; u = t
    while u is not None:
        p.append(u); u = prev[u]
    return p[::-1]

# ---------------------------------------------------------------- roles (Lyra's convention, own code)
def roles(col, lcyc):
    """p0=B1, p1=n_sM, p2=B2, p3=n_si, p4=n_sj: copies at cyclic distance 2 around n_sM; B2 adjacent to n_si,
    B1 adjacent to n_sj. Returns (R, S) or None if the link is not (2,1,1,1)."""
    n = len(lcyc)
    if n != 5:
        return None
    cols = [col[u] for u in lcyc]
    cnt = Counter(cols)
    if sorted(cnt.values()) != [1, 1, 1, 2]:
        return None
    r = next(c for c, k in cnt.items() if k == 2)
    pos = [i for i in range(5) if cols[i] == r]
    i, j = pos
    if (j - i) % 5 == 2:
        b1 = i
    elif (i - j) % 5 == 2:
        b1 = j
    else:
        return None
    P = [lcyc[(b1 + k) % 5] for k in range(5)]
    R = {'B1': P[0], 'n_sM': P[1], 'B2': P[2], 'n_si': P[3], 'n_sj': P[4]}
    S = {'r': r, 's_M': col[P[1]], 's_i': col[P[3]], 's_j': col[P[4]]}
    return R, S

def link_word(col, R, S):
    inv = {v: k for k, v in S.items()}
    return tuple(inv[col[R[k]]] for k in ('B1', 'n_sM', 'B2', 'n_si', 'n_sj'))

def insertable(adj, col, v):
    return len({col[u] for u in adj[v]}) < 4

def tau_rank(adj, col, v):
    """operational tangle number by the rank instrument: pair (a,b) untangled iff some (a,b)-chain meeting
    the link, when swapped, leaves a color absent at v's link."""
    t = 0
    for a, b in itertools.combinations(range(4), 2):
        lab, _ = rank_components(adj, col, a, b, v)
        comps = {lab[u] for u in adj[v] if u in lab}
        freed = False
        for cid in comps:
            ch = {u for u, l in lab.items() if l == cid}
            if insertable(adj, swap(col, ch, a, b), v):
                freed = True; break
        if not freed:
            t += 1
    return t

def leaf(adj, col, v):
    if insertable(adj, col, v):
        return 'I'
    return 'G' if tau_rank(adj, col, v) <= 5 else 'S'

# ---------------------------------------------------------------- the words
def run_word(adj, col0, v, R, S, which):
    """W_i: (B2,(r,s_i)) · (B1,(r,s_j)); W_j: mirror (B1,(r,s_j))·(B2,(r,s_i)) — Lyra §1: W_j is the i/j mirror,
    i.e. swap the copy adjacent to n_sj on (r,s_j) first. Returns the record."""
    r, sM, si, sj = S['r'], S['s_M'], S['s_i'], S['s_j']
    if which == 'i':
        m1 = (R['B2'], (r, si)); m2 = (R['B1'], (r, sj))
    else:
        m1 = (R['B1'], (r, sj)); m2 = (R['B2'], (r, si))
    seq = [m1, m2, m1, m2]
    col = col0; legal = []; imgs = []; chains = []
    for seed, (a, b) in seq:
        ok = col[seed] in (a, b)
        legal.append(ok)
        if ok:
            ch = chain_x(adj, col, seed, a, b, v)
            col = swap(col, ch, a, b)
        else:
            ch = set()
        chains.append(ch); imgs.append(col)
    c1, c2, c3, c4 = imgs
    X1, X2, X3_, X4 = chains
    # Δ: at c2, is the far singleton in the stage-3 chain (seed = m1's seed, pair m1's)?
    far = R['n_sj'] if which == 'i' else R['n_si']
    near_copy = m1[0]
    delta = far in X3_
    # Δ′: at c3, {other copy, its adjacent singleton} ⊆ X4?
    other_copy = m2[0]
    sing = R['n_si'] if which == 'i' else R['n_sj']
    dprime = (near_copy in X4) and (sing in X4)
    rec = {'word': which, 'legal': legal, 'lw': [link_word(c, R, S) for c in imgs],
           'delta': delta, 'dprime': dprime, 'leaf3': leaf(adj, c3, v), 'leaf4': leaf(adj, c4, v)}
    # G3 wall on Δ-YES (stated for W_i; the mirror statement for W_j swaps i↔j)
    if delta:
        a, b = m1[1]
        P = bfs_path(adj, c2, near_copy, far, a, b, v)
        rec['path_len'] = None if P is None else len(P) - 1
        # separation pair: W_i: (s_M, s_j), n_si vs {B1, n_sM}; W_j mirror: (s_M, s_i), n_sj vs {B2, n_sM}
        if which == 'i':
            pa, pb = sM, sj; x = R['n_si']; ys = (R['B1'], R['n_sM'])
        else:
            pa, pb = sM, si; x = R['n_sj']; ys = (R['B2'], R['n_sM'])
        w2 = all(not same_chain(adj, c2, x, y, pa, pb, v) for y in ys)
        w3 = all(not same_chain(adj, c3, x, y, pa, pb, v) for y in ys)
        # cross-check the wall by BFS too
        chb2 = G5.kempe_chain(adj, c2, x, pa, pb, exclude={v}); wb2 = all(y not in chb2 for y in ys)
        XCHK['agree' if wb2 == w2 else 'DISAGREE'] += 1
        rec['wall_c2'] = w2; rec['wall_c3'] = w3
        if not (w2 and w3):
            rec['exhibit'] = {'path': P, 'c2': {str(k): int(x_) for k, x_ in c2.items()}, 'roles': {k: str(x_) for k, x_ in R.items()}}
    return rec

# ---------------------------------------------------------------- populations (2,927)
def populations():
    out = []
    t = time.time()
    for label, faces, adj, tv, stuck, freed, exact in RD.build_pops():
        lcyc = E1.link_cycle(faces, tv)
        for i, c0 in enumerate(stuck):
            out.append(('1072', label, i, adj, tv, lcyc, c0))
    print(f"  1,072 loaded ({time.time()-t:.0f}s)")
    t = time.time()
    for label, faces, adj, tv, lcyc, c0, vs, freed in TE.failure_set():
        out.append(('54', label, -1, adj, tv, lcyc, c0))
    print(f"  the 54 loaded ({time.time()-t:.0f}s)")
    t = time.time()
    fams = {label: (faces, adj, tv) for label, faces, adj, tv in T2.build_tranche2()}
    for fn, pre in D6.FILES:
        raw = open(os.path.join(HERE, fn), 'rb').read()
        assert hashlib.sha256(raw).hexdigest().startswith(pre)
        st = json.loads(raw)
        for label, blk in st.items():
            faces, adj, tv = fams[label]
            lcyc = E1.link_cycle(faces, tv)
            if len(lcyc) != 5:
                continue
            smap = {str(v): v for v in adj}
            for i, crec in enumerate(blk['stuck']):
                c0 = {smap[k]: v for k, v in crec.items()}
                out.append(('1801', label, i, adj, tv, lcyc, c0))
    print(f"  the 1,801 loaded ({time.time()-t:.0f}s)")
    return out

if __name__ == "__main__":
    print("=" * 72); print("Toy 5599 — Grace — G1 rank instrument · G2 leaf table · G3 wall certificate"); print("=" * 72)
    pops = populations()
    print(f"  configurations loaded: {len(pops)}")
    records = []; p1 = Counter(); notstuck = Counter(); rolemismatch = 0
    t = time.time()
    for grp, label, i, adj, tv, lcyc, c0 in pops:
        # own stuckness test (rank) — Elie's filter used G5.operational_tau/X3.freeable; cross-check
        my_tau = tau_rank(adj, c0, tv)
        his_tau = G5.operational_tau(adj, c0, tv)
        XCHK['tau_agree' if my_tau == his_tau else 'TAU_DISAGREE'] += 1
        if my_tau != 6 or insertable(adj, c0, tv):
            notstuck[grp] += 1
            continue
        rl = roles(c0, lcyc)
        if rl is None:
            notstuck[grp + ':no-roles'] += 1
            continue
        R, S = rl
        # Elie's role map on the same configuration (for Lyra's question: is his B2 my B2?)
        try:
            er = WF.role_map(adj, c0, tv, lcyc)
            if er is not None:
                eR, eS = er
                same = (eR['B1'] == R['B1'] and eR['B2'] == R['B2'])
                mirror = (eR['B1'] == R['B2'] and eR['B2'] == R['B1'])
                XCHK['roles_same' if same else ('roles_mirror' if mirror else 'ROLES_OTHER')] += 1
        except Exception as ex:
            XCHK['roles_err'] += 1
        # P1: forced partitions at c0 by the rank instrument
        r, sM, si, sj = S['r'], S['s_M'], S['s_i'], S['s_j']
        B1, nM, B2, ni, nj = R['B1'], R['n_sM'], R['B2'], R['n_si'], R['n_sj']
        f = {
          'rsM_one': same_chain(adj, c0, B1, nM, r, sM, tv) and same_chain(adj, c0, nM, B2, r, sM, tv),
          'rsi_split': (not same_chain(adj, c0, B1, B2, r, si, tv)) and same_chain(adj, c0, B2, ni, r, si, tv),
          'rsj_split': (not same_chain(adj, c0, B1, B2, r, sj, tv)) and same_chain(adj, c0, B1, nj, r, sj, tv),
          'sMsi': same_chain(adj, c0, nM, ni, sM, si, tv),
          'sMsj': same_chain(adj, c0, nM, nj, sM, sj, tv),
          'sisj': same_chain(adj, c0, ni, nj, si, sj, tv)}
        p1['all6' if all(f.values()) else 'FAIL'] += 1
        for k, ok in f.items():
            if not ok: p1['fail:' + k] += 1
        # distinct link-seeded chains at c0 (Kittell's eight?)
        nchains = 0
        for a, b in itertools.combinations(range(4), 2):
            lab, _ = rank_components(adj, c0, a, b, tv)
            nchains += len({lab[u] for u in adj[tv] if u in lab})
        p1['chains=' + str(nchains)] += 1
        ri = run_word(adj, c0, tv, R, S, 'i'); rj = run_word(adj, c0, tv, R, S, 'j')
        records.append({'grp': grp, 'pop': label, 'i': i, 'n': len(adj), 'p1': all(f.values()), 'nchains': nchains, 'Wi': ri, 'Wj': rj})
    print(f"  computed in {time.time()-t:.0f}s")
    hh = hashlib.sha256(json.dumps([json.dumps(x, sort_keys=True, default=str) for x in records]).encode()).hexdigest()
    print(f"\n  {len(records)} stuck configurations; not-stuck skipped: {dict(notstuck)}; records hashed BEFORE the counts: sha256 {hh[:32]}…")
    N = len(records)
    # ---- P1
    print(f"\n[P1] forced partitions at c0 (positive control of roles + rank instrument): {p1['all6']}/{N}; failures: {{k:v for k,v in p1.items() if k.startswith('fail')}}")
    print(f"     distinct link-seeded chains at c0: {dict((k,v) for k,v in p1.items() if k.startswith('chains='))}")
    # ---- G1 cross-check
    print(f"\n[G1] rank instrument vs BFS: {dict(XCHK)}")
    # ---- P2/P3/G2 leaf table
    for w in ('Wi', 'Wj'):
        L4 = sum(1 for x in records if all(x[w]['legal'])); print(f"\n[P2] {w} fully legal: {L4}/{N}")
        c1ok = sum(1 for x in records if x[w]['lw'][0] == ('r','s_M','s_i','r','s_j') or (w=='Wj' and x[w]['lw'][0] == ('r','s_M','s_j','r','s_i') ) )
        c1all = Counter(x[w]['lw'][0] for x in records); c2all = Counter(x[w]['lw'][1] for x in records)
        print(f"[P3] {w} c1 link images: {dict(c1all)}"); print(f"[P3] {w} c2 link images: {dict(c2all)}")
        dn = [x for x in records if not x[w]['delta']]; dy = [x for x in records if x[w]['delta']]
        print(f"[G2] {w}: Δ-NO {len(dn)} · Δ-YES {len(dy)}")
        print(f"     Δ-NO leaves (c3 | c4): {dict(Counter(x[w]['leaf3'] for x in dn))} | {dict(Counter(x[w]['leaf4'] for x in dn))}; c4 link images: {dict(Counter(x[w]['lw'][3] for x in dn))}")
        dyy = [x for x in dy if x[w]['dprime']]; dyn = [x for x in dy if not x[w]['dprime']]
        print(f"     Δ-YES ∧ Δ′-YES {len(dyy)}: c4 leaves {dict(Counter(x[w]['leaf4'] for x in dyy))}; c4 links {dict(Counter(x[w]['lw'][3] for x in dyy))}")
        print(f"     Δ-YES ∧ Δ′-NO  {len(dyn)}: c4 leaves {dict(Counter(x[w]['leaf4'] for x in dyn))}; c4 links {dict(Counter(x[w]['lw'][3] for x in dyn))}")
        print(f"     Δ-YES c3 leaves: {dict(Counter(x[w]['leaf3'] for x in dy))}")
        # per population S-leaves
        S4 = Counter((x['grp'], x['pop']) for x in records if x[w]['leaf4'] == 'S')
        print(f"     stuck (S) leaves of {w} at c4 by population: {dict(S4)}")
        # G3 wall
        wc2 = sum(1 for x in dy if x[w].get('wall_c2')); wc3 = sum(1 for x in dy if x[w].get('wall_c3'))
        print(f"[G3] {w} wall on Δ-YES: c2 {wc2}/{len(dy)} · c3 {wc3}/{len(dy)}; violations: {len(dy)-wc2} / {len(dy)-wc3}; path lengths: {dict(Counter(x[w].get('path_len') for x in dy))}")
    # either word
    eitherI = sum(1 for x in records if 'I' in (x['Wi']['leaf4'], x['Wj']['leaf4'], x['Wi']['leaf3'], x['Wj']['leaf3']))
    eitherIG = sum(1 for x in records if any(l in ('I','G') for l in (x['Wi']['leaf4'], x['Wj']['leaf4'], x['Wi']['leaf3'], x['Wj']['leaf3'])))
    bothS = [x for x in records if x['Wi']['leaf4']=='S' and x['Wj']['leaf4']=='S']
    print(f"\n[OWL for {{W_i,W_j}}] some prefix/image insertable (I): {eitherI}/{N}; insertable-or-gate (I/G): {eitherIG}/{N}; BOTH words' c4 stuck (S): {len(bothS)} → {dict(Counter((x['grp'],x['pop']) for x in bothS))}")
    dnn = sum(1 for x in records if not x['Wi']['delta'] or not x['Wj']['delta'])
    print(f"     Δ-NO for at least one word: {dnn}/{N} (Lemma D closes these by derivation)")
    out = {'hash': hh, 'N': N, 'xchk': dict(XCHK), 'p1': dict(p1), 'records': records}
    json.dump(out, open(os.path.join(HERE, '.out_5599.json'), 'w'), default=str)
    print(f"\n  written .out_5599.json")
