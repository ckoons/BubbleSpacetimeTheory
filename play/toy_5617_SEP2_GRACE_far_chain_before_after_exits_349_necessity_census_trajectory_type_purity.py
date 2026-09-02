"""
Toy 5617 — Grace — Round 101.
(A) FAR-CHAIN CONDITION (Lane F's necessary condition: (α,ζ)=(β,η)=(ε,ζ)=(ε,η)=1) on all 349 two-word-locked
    witnesses (n ≤ 24) — necessity confirmed on the complete locked set; and BEFORE/AFTER every legal first word:
    for each witness and each fully-legal word w, the image c′ = w·c in its OWN frame: exit? (insertable / τ ≤ 5 /
    a bridge word exits) and far-bits(c′). Cross-tab (exit, far-bits all 1). "Does every exit leave the four
    far-chain types?" is the cell (exit, far=1111) — pre-scored by the lemma candidate: exits should NOT be in the
    locked pattern... stated as a count, never a verdict. Non-exiting words are the control.
(B) NECESSITY ON THE CENSUS: the 5614 census by type (374,658) — locked set through n = 22 = the 49; report k/N of
    locked in the 4 far-pattern types and outside; converse failure per type from the Lane F sample.
(C) TRAJECTORY TYPE (Cal §822 refinement #1; v7): CAL-CORE = the 6 pairwise 0/1 intersections among the stage
    chains X₁…X₄ of W_i; V7-FULL = those 6 + the 32 bits X_k ∩ (eight c₀ chains). Positions only, no sizes. On the
    Lane F sample (5,531) + all 349: tabulate locked / unlocked / exit set by trajectory type; purity weighted by
    unlocked members (fraction of UNLOCKED members lying in types with no locked member) and plain purity.
    Control: bits constant on every configuration (forced) — listed for Cal's derived list to be compared.
(D) Gallery FCW-122..377 for the 256 at n = 24 with type + trajectory type.
Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, sys, time, glob
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
LF = load("t5614", "toy_5614_SEP2_GRACE_LANE_F_type_table_eight_chain_intersection_matrix_in_frame_census.py")
M = load("t5600g8", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1])
EA, E1, WF, G5, OF = M.EA, M.E1, M.WF, M.G5, M.OF
roles, insertable, tau_rank, leaf = G.roles, G.insertable, G.tau_rank, G.leaf
L = LF.LETTERS; PAIRS = [(L[i], L[j]) for i in range(8) for j in range(i + 1, 8)]
FAR = [PAIRS.index(('alpha', 'zeta')), PAIRS.index(('beta', 'eta')), PAIRS.index(('eps', 'zeta')), PAIRS.index(('eps', 'eta'))]
WI = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))); WJ = T.mirror_word(WI)
def far_bits(adj, c, v, R, S):
    ch = LF.eight_chains(adj, c, v, R, S); tb, ts = LF.type_of(ch); return tuple(tb[i] for i in FAR), tb, ch
def traj(adj, c, v, R, S, ch):
    lg, im, X = T.stages(adj, c, v, R, S, WI)
    core = tuple(1 if (X[a] & X[b]) else 0 for a in range(4) for b in range(a + 1, 4))
    full = core + tuple(1 if (X[k] & ch[l]) else 0 for k in range(4) for l in L)
    return core, full, lg
def exit_status(adj, c, v, lcyc):
    if insertable(adj, c, v): return 'I', None
    if tau_rank(adj, c, v) <= 5: return 'G', None
    rl = roles(c, lcyc)
    if rl is None: return 'no-roles', None
    R, S = rl
    for w in (WI, WJ):
        lg, im, X = T.stages(adj, c, v, R, S, w)
        if all(lg) and leaf(adj, im[3], v) in ('I', 'G'): return 'bridge-exit', (R, S)
    return 'stuck', (R, S)

if __name__ == "__main__":
    t0 = time.time(); moves, words, _ = WF.context_family()
    files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78), ('.in_frame_256_two_word_locked_n24.json', 122)]
    W = []
    for fn, base in files:
        for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))): W.append((x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{base+k:03d}"))
    print("=" * 72); print(f"Toy 5617 — Grace — far-chain before/after exits on {len(W)} witnesses; necessity; trajectory type"); print("=" * 72, flush=True)
    cache = {}; wrecs = []
    for (n, gi, v, ct, fid) in W:
        if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
        adj = cache[n][gi]; faces, ok = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v); order = sorted(u for u in adj if u != v)
        c0 = {u: ct[k] for k, u in enumerate(order)}; R, S = roles(c0, lcyc)
        fb, tb, ch = far_bits(adj, c0, v, R, S); core, full, lg = traj(adj, c0, v, R, S, ch)
        tab = Counter(); nlegal = 0
        for w in words:
            lgw, imw, Xw = T.stages(adj, c0, v, R, S, w)
            if not all(lgw): continue
            nlegal += 1; c4 = imw[3]; st, rs = exit_status(adj, c4, v, lcyc)
            fb2 = far_bits(adj, c4, v, rs[0], rs[1])[0] if rs else None
            tab[(st in ('I', 'G', 'bridge-exit'), fb2 == (1, 1, 1, 1) if fb2 is not None else st)] += 1
        wrecs.append({'id': fid, 'n': n, 'gi': gi, 'v': v, 'far': fb, 'type': tb, 'core': core, 'full': full, 'legal': nlegal, 'tab': {f"{a}|{b}": c for (a, b), c in tab.items()}})
    hh = hashlib.sha256(json.dumps([json.dumps(r, sort_keys=True, default=str) for r in wrecs]).encode()).hexdigest()
    print(f"\n[A] {len(wrecs)} witnesses; records hashed BEFORE counts {hh[:32]}…  [{time.time()-t0:.0f}s]")
    print(f"  far-chain bits (αζ,βη,εζ,εη) on the locked set: {dict(Counter(r['far'] for r in wrecs))}  → necessity {sum(1 for r in wrecs if r['far']==(1,1,1,1))}/{len(wrecs)}")
    print(f"  types of the 349: {dict(Counter(''.join(map(str,r['type'])) for r in wrecs))}")
    agg = Counter()
    for r in wrecs: agg.update(r['tab'])
    print(f"  BEFORE→AFTER every legal first word, all witnesses — (exit | image's far-bits all 1 / status): {dict(agg)}")
    for n_ in sorted(set(r['n'] for r in wrecs)):
        a = Counter(); [a.update(r['tab']) for r in wrecs if r['n'] == n_]; print(f"    n={n_}: {dict(a)}")
    # ---- (B) census necessity
    out = json.load(open(os.path.join(HERE, '.out_5614.json'))); census = {tuple(k): c for k, c in out['census'] if k[0] != 'no-roles'}
    far_types = [t for t in census if all(t[i] == 1 for i in FAR)]
    print(f"\n[B] census n ≤ 22: types with far-pattern 1111: {len(far_types)}/{len(census)}; mass {sum(census[t] for t in far_types)}/{sum(census.values())}")
    s49 = [r for r in wrecs if r['n'] <= 22]; print(f"  locked through n=22 (the 49): in far-pattern types {sum(1 for r in s49 if r['far']==(1,1,1,1))}/{len(s49)}; outside {sum(1 for r in s49 if r['far']!=(1,1,1,1))}")
    sample = out['sample']
    for t in far_types:
        rows = [s for s in sample if tuple(s['type']) == t]; lk = sum(1 for s in rows if s['locked'])
        print(f"    type {''.join(map(str,t))}: census {census[t]}; sample locked {lk}/{len(rows)} (converse failure {len(rows)-lk}/{len(rows)})")
    # ---- (C) trajectory type on the sample + 349
    trecs = []
    for s in sample:
        n, gi, v = s['n'], s['gi'], s['v']
        if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
        adj = cache[n][gi]; faces, ok = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v); order = sorted(u for u in adj if u != v)
        c0 = {u: s['col'][k] for k, u in enumerate(order)}; R, S = roles(c0, lcyc)
        ch = LF.eight_chains(adj, c0, v, R, S); core, full, lg = traj(adj, c0, v, R, S, ch)
        trecs.append({'core': core, 'full': full, 'locked': s['locked'], 'exits': tuple(s['exits']), 'src': s['src'], 'legal4': all(lg)})
    for r in wrecs:
        if r['n'] > 22: trecs.append({'core': r['core'], 'full': r['full'], 'locked': True, 'exits': (), 'src': 'witness24', 'legal4': True})
    print(f"\n[C] trajectory types on {len(trecs)} configurations (sample + n=23/24 witnesses) [{time.time()-t0:.0f}s]")
    for name, key, nb in (('CAL-CORE (X_a∩X_b, 6 bits)', 'core', 6), ('V7-FULL (core + X_k∩chain_l, 38 bits)', 'full', 38)):
        const = [i for i in range(nb) if len({r[key][i] for r in trecs}) == 1]
        by = defaultdict(lambda: [0, 0])
        for r in trecs: by[r[key]][0 if r['locked'] else 1] += 1
        pureL = [k for k, v in by.items() if v[0] and not v[1]]; pureU = [k for k, v in by.items() if v[1] and not v[0]]; mixed = [k for k, v in by.items() if v[0] and v[1]]
        unl_total = sum(v[1] for v in by.values()); unl_in_pure = sum(by[k][1] for k in pureU); lk_total = sum(v[0] for v in by.values()); lk_in_pure = sum(by[k][0] for k in pureL)
        print(f"  {name}: types {len(by)}; forced (constant) bits {len(const)}/{nb} at positions {const}; pure-locked {len(pureL)} · pure-unlocked {len(pureU)} · mixed {len(mixed)}")
        print(f"     purity weighted by unlocked members: {unl_in_pure}/{unl_total} unlocked lie in locked-free types; locked in pure-locked types {lk_in_pure}/{lk_total}")
        lt = Counter(r[key] for r in trecs if r['locked']); print(f"     locked configurations land in {len(lt)} {key}-types; top: {[(''.join(map(str,k)), c) for k, c in lt.most_common(5)]}")
        for k in mixed[:6]: print(f"     MIXED {''.join(map(str,k))}: locked {by[k][0]} unlocked {by[k][1]}")
        ex = defaultdict(set)
        for r in trecs:
            if not r['locked']: ex[r[key]].add(r['exits'])
        print(f"     exit-set a function of {key}-type on unlocked: {sum(1 for k, v in ex.items() if len(v)==1)}/{len(ex)} types single-signature")
    # ---- (D) gallery
    g = json.load(open(os.path.join(HERE, '..', 'data', 'fourcolor_witness_gallery.json'))); ids = [w['id'] for w in g['witnesses']]
    byid = {r['id']: r for r in wrecs}
    if ids[-1] == 'FCW-121':
        for k, x in enumerate(json.load(open(os.path.join(HERE, '.in_frame_256_two_word_locked_n24.json')))):
            fid = f"FCW-{122+k:03d}"; col = x['coloring_mod_S4_sorted_order']; r = byid[fid]
            g['witnesses'].append({'id': fid, 'name': f"In-frame gate-phase-locked stuck coloring {k+1} of 256 at n=24 — plantri -c5 graph {x['graph_index_plantri_c5']}, v={x['v']}",
              'class': 'ONE-WORD-LOCKED (gate form), 5-connected frame, n=24; exits in exactly two words. Counterexample to the One-Word Lemma (T2585) in frame.',
              'graph': {'frame': '5-connected sphere triangulation (plantri -c5)', 'n': 24, 'plantri_c5_graph_index': x['graph_index_plantri_c5'], 'vertex_v': x['v'], 'coloring_mod_S4_sorted_vertex_order': col, 'coloring_sha256_12': hashlib.sha256(json.dumps(col).encode()).hexdigest()[:12]},
              'key_numbers': {'legal_and_acting_words': x.get('legal_images'), 'single_swaps_reaching_gate': x.get('single_swap_gate'), 'word_depth_to_gate': 2, 'exit': x.get('exit')},
              'type_5614': {'bits_28': ''.join(map(str, r['type'])), 'far_chain_bits(αζ,βη,εζ,εη)': r['far']}, 'trajectory_type_5617': {'cal_core_6': r['core'], 'v7_full_38': ''.join(map(str, r['full']))},
              'status': 'KILL WITNESS 2026-09-02 11:55 (Elie 5600/5601 at n=24, exhaustive: 5,787,744 stuck colorings). Typed by Grace 5617. Never-reuse ID.', 'provenance': 'Elie play/.in_frame_256_two_word_locked_n24.json; Grace 5617'})
        for w in g['witnesses']:
            r = byid.get(w['id'])
            if r and 'trajectory_type_5617' not in w: w['trajectory_type_5617'] = {'cal_core_6': r['core'], 'v7_full_38': ''.join(map(str, r['full'])), 'far_chain_bits': r['far']}
        g['_meta']['record_note_2026_09_02_the_256'] = "FCW-122..377: the 256 n=24 kill witnesses (Elie 11:55). Locked total 349 through n=24; depth stays two. Far-chain bits and trajectory types (Grace 5617) on all 349."
        json.dump(g, open(os.path.join(HERE, '..', 'data', 'fourcolor_witness_gallery.json'), 'w'), ensure_ascii=False, indent=2)
        print(f"\n[D] gallery: {len(g['witnesses'])} witnesses, last {g['witnesses'][-1]['id']}")
    json.dump({'hash': hh, 'witnesses': wrecs, 'traj': trecs}, open(os.path.join(HERE, '.out_5617.json'), 'w'), default=str)
    print(f"\n  written .out_5617.json [{time.time()-t0:.0f}s]")
