"""
Toy 5623 — Grace — Round 103, THE KERNEL INSTRUMENT (K1845 §1: the lock is a kernel element of one chain operator).
For every lock (349, n ≤ 24), W_i in the lock's frame: X₃ (B₂'s (r,s_i)-chain in c₂), X₄ (B₁'s (r,s_j)-chain in c₃),
C = X₃ ∩ X₄. The KERNEL: K := the component of X₃ − C containing the near copy B₂ — its size, its vertex set relative
to the link (distance-to-link profile), and the EXTRA KERNEL DIMENSION dim ker L(X₃ − C) − dim ker L(X₃) (= #components − 1).
Then for every fully-legal first word w whose image exits (directly / τ ≤ 5 / by a bridge word in its own frame): in
the image's frame recompute X₃′, X₄′, C′ and classify — CUT VANISHES (C′ = ∅) · KERNEL VANISHES (C′ ≠ ∅ but X₃′ − C′
keeps B₂′ and n_sj′ connected) · NEITHER (C′ separates: the image is bridge-stuck for W_i′ yet exits by W_j′ or a
gate swap) — and the same for non-exiting words (control: they must be NEITHER for both words, Lemma T).
Also the CUT's distance to the link (min over cut vertices of graph distance in T−v to any link vertex) on all 349
and on every bridge-stuck image (extends 5610's "exactly 1" on the 93). Mirror word W_j reported alongside.
Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, json, os, time, glob
from collections import Counter, deque, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname)); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
M = load("t5600gk", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1]); EA, E1, WF, OF = M.EA, M.E1, M.WF, M.OF
roles, insertable, tau_rank, leaf, rank_components, same_chain = G.roles, G.insertable, G.tau_rank, G.leaf, G.rank_components, G.same_chain
WI = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))); WJ = T.mirror_word(WI)
def dist_from(adj, sources, v):
    d = {s: 0 for s in sources}; q = deque(sources)
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w != v and w not in d: d[w] = d[u] + 1; q.append(w)
    return d
def cut_data(adj, c, v, R, S, which, dl):
    w = WI if which == 'i' else WJ
    lg, im, X = T.stages(adj, c, v, R, S, w)
    if not all(lg): return None
    X3, X4, c2 = X[2], X[3], im[1]; C = X3 & X4
    near, far = (R['B2'], R['n_sj']) if which == 'i' else (R['B1'], R['n_si'])
    a, b = (S['r'], S['s_i']) if which == 'i' else (S['r'], S['s_j'])
    sub3 = {u: {x for x in adj[u] if x in X3} for u in X3}; _, k0 = rank_components(sub3, c2, a, b, v)
    rest = {u: {x for x in adj[u] if x in X3 and x not in C} for u in X3 if u not in C}
    lab, k1 = rank_components(rest, c2, a, b, v) if rest else ({}, 0)
    Kset = {u for u, l in lab.items() if near in lab and l == lab[near]} if rest else set()
    sep = (near in lab and far in lab and lab[near] != lab[far]) if rest else None
    dprime = (near in X4) and ((R['n_si'] if which == 'i' else R['n_sj']) in X4)
    c4 = im[3]; sM = S['s_M']
    q3 = same_chain(adj, c4, R['n_sM'], R['n_si'], sM, c4[R['n_si']], v); q4 = same_chain(adj, c4, R['n_sM'], R['n_sj'], sM, c4[R['n_sj']], v)
    return {'dprime': dprime, 'q3': q3, 'q4': q4, 'C': len(C), 'C_dist_link': (min(dl.get(u, 99) for u in C) if C else None), 'k0': k0, 'k1': k1, 'extra': (k1 - k0) if C else 0,
            'K_size': len(Kset), 'K_dist_profile': dict(Counter(dl.get(u, 99) for u in Kset)), 'sep': sep, 'leaf4': leaf(adj, im[3], v)}
def image_status(adj, c, v, lcyc, dl):
    if insertable(adj, c, v): return 'I', None, None
    if tau_rank(adj, c, v) <= 5: return 'G', None, None
    rl = roles(c, lcyc)
    if rl is None: return 'no-roles', None, None
    R, S = rl; di = cut_data(adj, c, v, R, S, 'i', dl); dj = cut_data(adj, c, v, R, S, 'j', dl)
    ex = any(d and d['leaf4'] in ('I', 'G') for d in (di, dj))
    return ('bridge-exit' if ex else 'stuck'), di, dj
def classify(d):
    if d is None: return 'illegal'
    if d['C'] == 0: return 'CUT-VANISHES'
    if d['sep'] is None: return 'FAR-OUTSIDE-X3'   # Δ-NO in the image's frame: no tunnel formed (rev. 12:2x)
    if d['sep'] is False: return 'KERNEL-VANISHES'
    if d.get('dprime'): return 'DPRIME-YES'   # prefix-gate branch: Lemma T does not apply (rev. 12:2x)
    return 'NEITHER'
if __name__ == "__main__":
    t0 = time.time(); moves, words, _ = WF.context_family()
    files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78), ('.in_frame_256_two_word_locked_n24.json', 122)]
    W = []
    for fn, base in files:
        for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))): W.append((x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{base+k:03d}"))
    print("=" * 72); print(f"Toy 5623 — Grace — kernel instrument on {len(W)} locks"); print("=" * 72, flush=True)
    cache = {}; recs = []; img_tab = Counter(); img_dist = Counter(); ctrl = Counter(); EXH = []; NN = []
    for (n, gi, v, ct, fid) in W:
        if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
        adj = cache[n][gi]; faces, ok = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v); order = sorted(u for u in adj if u != v)
        c0 = {u: ct[k] for k, u in enumerate(order)}; R, S = roles(c0, lcyc); dl = dist_from(adj, list(adj[v]), v)
        di = cut_data(adj, c0, v, R, S, 'i', dl); dj = cut_data(adj, c0, v, R, S, 'j', dl)
        after = Counter()
        for w in words:
            lg, im, X = T.stages(adj, c0, v, R, S, w)
            if not all(lg): continue
            st, ei, ej = image_status(adj, im[3], v, lcyc, dl)
            exiting = st in ('I', 'G', 'bridge-exit')
            if st in ('I', 'G'): key = ('exit', st, st)
            elif st == 'no-roles': key = ('exit' if exiting else 'noexit', 'no-roles', 'no-roles')
            else: key = ('exit' if exiting else 'noexit', classify(ei), classify(ej))
            after[key] += 1; img_tab[key] += 1
            if exiting and key[1] == 'NEITHER' and key[2] == 'NEITHER':
                NN.append({'lock': fid, 'word': str(w), 'Wi': {k: ei[k] for k in ('leaf4','q3','q4','dprime','C','sep')}, 'Wj': {k: ej[k] for k in ('leaf4','q3','q4','dprime','C','sep')}})
            if st == 'stuck':
                for wn, d in (('i', ei), ('j', ej)):
                    if d and d['C']:
                        img_dist[d['C_dist_link']] += 1
                        if d['C_dist_link'] and d['C_dist_link'] > 1: EXH.append({'lock': fid, 'n': n, 'gi': gi, 'v': v, 'first_word': str(w), 'image_bridge_word': wn, 'C_dist_link': d['C_dist_link'], 'image_coloring': {str(k): x for k, x in im[3].items()}})
                ctrl['stuck-images NEITHER both'] += int(classify(ei) == 'NEITHER' and classify(ej) == 'NEITHER'); ctrl['stuck-images n'] += 1
        recs.append({'id': fid, 'n': n, 'Wi': di, 'Wj': dj, 'after': {'|'.join(k): c for k, c in after.items()}})
    hh = hashlib.sha256(json.dumps([json.dumps(r, sort_keys=True, default=str) for r in recs]).encode()).hexdigest()
    print(f"\n  {len(recs)} locks; records hashed BEFORE counts {hh[:32]}…  [{time.time()-t0:.0f}s]")
    for which in ('Wi', 'Wj'):
        D = [r[which] for r in recs if r[which]]
        print(f"\n[{which} at the lock] legal {len(D)}/{len(recs)}; |C| {dict(sorted(Counter(d['C'] for d in D).items()))}; C dist-to-link {dict(Counter(d['C_dist_link'] for d in D))}; C separates {sum(1 for d in D if d['sep'])}/{len(D)}")
        print(f"    extra kernel dim {dict(sorted(Counter(d['extra'] for d in D).items()))}; kernel component |K| {dict(sorted(Counter(d['K_size'] for d in D).items()))}")
        prof = Counter()
        for d in D: prof.update(d['K_dist_profile'])
        print(f"    K's vertices by distance to link (pooled): {dict(sorted(prof.items()))}; K contains a link vertex on {sum(1 for d in D if 0 in d['K_dist_profile'])}/{len(D)} locks")
    print(f"\n[AFTER EVERY LEGAL FIRST WORD, all 349 — (exit? | W_i′ class | W_j′ class)]: {dict(img_tab)}")
    print(f"  control (stuck images must be NEITHER for both): {ctrl}")
    print(f"  cut distance-to-link on bridge-stuck images (both words, pooled): {dict(img_dist)}")
    json.dump(NN, open(os.path.join(HERE, '.exit_neither_neither_5623.json'), 'w')); print(f"  exit·NEITHER·NEITHER exhibits: {len(NN)}; leaf4 pairs {Counter((x['Wi']['leaf4'], x['Wj']['leaf4']) for x in NN)}; Q3∧Q4 on the exiting word: {Counter((x['Wi']['q3'] and x['Wi']['q4'], x['Wj']['q3'] and x['Wj']['q4']) for x in NN)}")
    json.dump(EXH, open(os.path.join(HERE, '.cut_distance2_exhibits_5623.json'), 'w')); print(f"  distance-2 cut exhibits saved: {len(EXH)}")
    json.dump({'hash': hh, 'records': recs, 'img_tab': {'|'.join(k): c for k, c in img_tab.items()}}, open(os.path.join(HERE, '.out_5623.json'), 'w'), default=str)
    print(f"\n  written .out_5623.json [{time.time()-t0:.0f}s]")
