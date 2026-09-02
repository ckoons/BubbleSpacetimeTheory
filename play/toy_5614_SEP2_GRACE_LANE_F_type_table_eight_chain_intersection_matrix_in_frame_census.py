"""
Toy 5614 — Grace — LANE F: THE TYPE TABLE (K1841 §2; Casey Round 100).

TYPE of a stuck configuration := the 8×8 0/1 intersection matrix of Kittell's eight link-seeded chains, with the
FAR-COPY SEED RULE (Cal §821 §4) so each letter names ONE chain:
  θ = (r,s_M)@B₁ (= M ∋ n_sM, B₂) · α = (s_M,s_i)@n_sM (= F_i) · β = (s_M,s_j)@n_sM (= F_j) · ε = (s_i,s_j)@n_si (= E)
  γ = (r,s_j)@B₁ (∋ n_sj) · δ = (r,s_i)@B₂ (∋ n_si) · ζ = (r,s_i)@B₁ (the FAR copy's chain) · η = (r,s_j)@B₂ (far copy).
Refinement: the 28 pairwise intersection SIZES. Chains by the rank instrument (Laplacian null space, 5599).
Population: (1) TYPE CENSUS on every in-frame stuck coloring mod S₄, plantri -c5, n = 12…22 (type only; cheap);
(2) LOCK / EXITING-ORBIT / IMAGE COUNT on a STRATIFIED SAMPLE — all stuck colorings at n ≤ 18, plus ~750 per n at
n = 19…22 chosen by a seeded per-configuration coin (seed 5614) — plus all 93 witnesses and the 5610 matched 93.
  locked := no fully-legal 186-word image has τ ≤ 5 (BFS chains for the word sweep — speed; the TYPE uses rank);
  exiting orbits := set of mirror-orbits of words whose image has τ ≤ 5; images := distinct legal images.
Report: number of types (0/1 and refined); locked as a function of type (pure / mixed types, exhibits); exiting
orbit as a function of type; image count by type; the 93's types (positive control: a handful).
The sample is SAVED (.lane_f_sample.json) so Elie's BFS instrument runs on the identical population. Records
hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, random, sys, time, glob
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
M = load("t5600g7", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1])
EA, E1, WF, G5, OF = M.EA, M.E1, M.WF, M.G5, M.OF
rank_components, roles = G.rank_components, G.roles
LETTERS = ['theta', 'alpha', 'beta', 'eps', 'gamma', 'delta', 'zeta', 'eta']
def eight_chains(adj, c, v, R, S):
    r, sM, si, sj = S['r'], S['s_M'], S['s_i'], S['s_j']
    spec = [('theta', R['B1'], r, sM), ('alpha', R['n_sM'], sM, si), ('beta', R['n_sM'], sM, sj), ('eps', R['n_si'], si, sj),
            ('gamma', R['B1'], r, sj), ('delta', R['B2'], r, si), ('zeta', R['B1'], r, si), ('eta', R['B2'], r, sj)]
    out = {}
    cache = {}
    for name, seed, a, b in spec:
        key = (min(a, b), max(a, b))
        if key not in cache: cache[key] = rank_components(adj, c, a, b, v)[0]
        lab = cache[key]; out[name] = frozenset(u for u, l in lab.items() if l == lab[seed])
    return out
def type_of(ch):
    bits = []; sizes = []
    for i in range(8):
        for j in range(i + 1, 8):
            k = len(ch[LETTERS[i]] & ch[LETTERS[j]]); bits.append(1 if k else 0); sizes.append(k)
    return tuple(bits), tuple(sizes)
def orbit_id(w):
    m = T.mirror_word(w); return min(str(w), str(m))
def word_sweep(adj, c0, v, R, S, words):
    """BFS instrument: (locked, exiting orbit set, distinct images)."""
    imgs = set(); exits = set()
    for w in words:
        m1 = (R[w[0][0]], (S[w[0][1][0]], S[w[0][1][1]])); m2 = (R[w[1][0]], (S[w[1][1][0]], S[w[1][1][1]]))
        col = c0; legal = True
        for seed, (a, b) in (m1, m2, m1, m2):
            if col[seed] not in (a, b): legal = False; break
            col = G5.do_swap(col, G5.kempe_chain(adj, col, seed, a, b, exclude={v}), a, b)
        if not legal: continue
        imgs.add(tuple(sorted(col.items())))
        if len({col[u] for u in adj[v]}) < 4 or G5.operational_tau(adj, col, v) <= 5: exits.add(orbit_id(w))
    return (len(exits) == 0), exits, len(imgs)

if __name__ == "__main__":
    t0 = time.time(); random.seed(5614)
    moves, words, _ = WF.context_family()
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 23))
    TARGET = {19: 750, 20: 750, 21: 750, 22: 750}
    EXPECT = {19: 3523, 20: 17523, 21: 64015, 22: 287297}     # Elie's stuck counts, for the coin
    census = Counter(); census_ref = Counter(); sample = []; type_by_n = defaultdict(Counter)
    print("=" * 72); print(f"Toy 5614 — Grace — LANE F type table, n = {ns}"); print("=" * 72, flush=True)
    for n in ns:
        gs = EA.plantri_graphs(n, flags=('-c5',)); tn = time.time(); cnt = 0; ns_ = 0
        p = 1.0 if n <= 18 else min(1.0, TARGET[n] / EXPECT.get(n, 1))
        for gi, adj in enumerate(gs):
            faces, ok = OF.faces_of(adj)
            for v in adj:
                if len(adj[v]) != 5: continue
                order = sorted(u for u in adj if u != v); sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                lcyc = E1.link_cycle(faces, v)
                for ct in EA.all_colorings_mod_s4(sub, order):
                    c0 = {u: ct[k] for k, u in enumerate(order)}
                    if len({c0[u] for u in adj[v]}) < 4 or G5.operational_tau(adj, c0, v) != 6: continue
                    rl = roles(c0, lcyc)
                    if rl is None: census[('no-roles',)] += 1; continue
                    R, S = rl; ch = eight_chains(adj, c0, v, R, S); tb, ts = type_of(ch)
                    census[tb] += 1; census_ref[ts] += 1; type_by_n[n][tb] += 1; cnt += 1
                    if random.random() < p:
                        locked, exits, nimg = word_sweep(adj, c0, v, R, S, words)
                        sample.append({'n': n, 'gi': gi, 'v': v, 'col': list(ct), 'type': tb, 'sizes': ts, 'locked': locked, 'exits': sorted(exits), 'images': nimg, 'src': 'census'}); ns_ += 1
        print(f"  n={n}: graphs {len(gs)}; stuck typed {cnt}; sampled {ns_}; types so far {len(census)}  [{time.time()-tn:.0f}s / {time.time()-t0:.0f}s]", flush=True)
        json.dump({'census': [[list(k), c] for k, c in census.items()], 'sample': sample}, open(os.path.join(HERE, '.lane_f_partial.json'), 'w'))
    # the 93 + matched
    files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78)]
    matched = {r['id']: r for r in json.load(open(os.path.join(HERE, '.out_5610.json')))['records']}
    cache = {}
    for fn, base in files:
        for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))):
            n, gi, v = x['n'], x['graph_index_plantri_c5'], x['v']; fid = f"FCW-{base+k:03d}"
            if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
            adj = cache[n][gi]; faces, ok = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v); order = sorted(u for u in adj if u != v)
            for src, ct in (('witness', x['coloring_mod_S4_sorted_order']), ('matched', matched[fid]['matched_coloring'])):
                c0 = {u: ct[k2] for k2, u in enumerate(order)}; R, S = roles(c0, lcyc)
                ch = eight_chains(adj, c0, v, R, S); tb, ts = type_of(ch)
                locked, exits, nimg = word_sweep(adj, c0, v, R, S, words)
                sample.append({'n': n, 'gi': gi, 'v': v, 'col': list(ct), 'type': tb, 'sizes': ts, 'locked': locked, 'exits': sorted(exits), 'images': nimg, 'src': src, 'id': fid})
    json.dump(sample, open(os.path.join(HERE, '.lane_f_sample.json'), 'w'))
    hh = hashlib.sha256(json.dumps([json.dumps(s, sort_keys=True) for s in sample]).encode()).hexdigest()
    print(f"\n  sample {len(sample)} configurations saved (.lane_f_sample.json), hashed BEFORE counts: {hh[:32]}…  [{time.time()-t0:.0f}s]")
    # ---- tables
    print(f"\n[CENSUS] in-frame stuck colorings typed: {sum(census.values())}; distinct 0/1 types: {len([k for k in census if k[0]!='no-roles'])}; refined (size) types: {len(census_ref)}; no-roles: {census.get(('no-roles',),0)}")
    top = census.most_common(12); print("  top types (bits→count):"); 
    for k, c in top: print(f"    {''.join(map(str,k)) if k[0]!='no-roles' else k}: {c}")
    print(f"  types per n: { {n: len(t) for n, t in type_by_n.items()} }")
    bytype = defaultdict(lambda: {'locked': 0, 'unlocked': 0, 'exits': Counter(), 'images': Counter(), 'srcs': Counter()})
    for s in sample:
        d = bytype[s['type']]; d['locked' if s['locked'] else 'unlocked'] += 1; d['exits'][tuple(s['exits'])] += 1; d['images'][s['images']] += 1; d['srcs'][s['src']] += 1
    pure_L = [k for k, d in bytype.items() if d['locked'] and not d['unlocked']]; pure_U = [k for k, d in bytype.items() if d['unlocked'] and not d['locked']]; mixed = [k for k, d in bytype.items() if d['locked'] and d['unlocked']]
    print(f"\n[LOCK vs TYPE] types in sample: {len(bytype)}; pure-locked {len(pure_L)}; pure-unlocked {len(pure_U)}; MIXED {len(mixed)}")
    for k in mixed[:12]:
        d = bytype[k]; print(f"    MIXED {''.join(map(str,k))}: locked {d['locked']} unlocked {d['unlocked']} srcs {dict(d['srcs'])}")
    wt = Counter(s['type'] for s in sample if s['src'] == 'witness'); print(f"\n[THE 93] land in {len(wt)} types: {[(''.join(map(str,k)), c) for k, c in wt.most_common()]}")
    mt = Counter(s['type'] for s in sample if s['src'] == 'matched'); print(f"[MATCHED 93] land in {len(mt)} types: {[(''.join(map(str,k)), c) for k, c in mt.most_common(8)]}")
    for k, c in wt.most_common():
        d = bytype[k]; print(f"    witness type {''.join(map(str,k))}: in census {census.get(k)} ; in sample locked {d['locked']} unlocked {d['unlocked']}; images {dict(sorted(d['images'].items()))}")
    ex_pure = sum(1 for k, d in bytype.items() if len(d['exits']) == 1); print(f"\n[EXITING ORBIT vs TYPE] types with a single exit-set signature: {ex_pure}/{len(bytype)}")
    exit_orbits = Counter(); 
    for s in sample:
        for o in s['exits']: exit_orbits[o] += 1
    print(f"  exiting orbits seen: {len(exit_orbits)}; top: {exit_orbits.most_common(6)}")
    print(f"\n[IMAGES by lock] locked {dict(sorted(Counter(s['images'] for s in sample if s['locked']).items()))}; unlocked {dict(sorted(Counter(s['images'] for s in sample if not s['locked']).items()))}")
    json.dump({'hash': hh, 'census': [[list(k), c] for k, c in census.items()], 'census_ref_n': len(census_ref), 'sample': sample}, open(os.path.join(HERE, '.out_5614.json'), 'w'))
    print(f"\n  written .out_5614.json [{time.time()-t0:.0f}s]")
