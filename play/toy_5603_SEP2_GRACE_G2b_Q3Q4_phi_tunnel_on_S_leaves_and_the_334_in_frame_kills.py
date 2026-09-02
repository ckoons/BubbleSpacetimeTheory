"""
Toy 5603 — Grace — G2b (Lyra 09:15 escort request + Elie 09:23 in-frame kills).

Part A (the 2,873): on every S leaf of W_i / W_j (Δ-YES ∧ Δ′-NO with τ(c4) = 6), and on every hard-branch
G leaf, compute in c4: Q3 := n_sM ~ n_si in (s_M, c4(n_si)); Q4 := n_sM ~ n_sj in (s_M, c4(n_sj)).
  PREDICTION (Lyra Lemma T): c4 is STUCK  ⟺  Q3 ∧ Q4, on every hard-branch instance.
  Φ := |X3| (size of the wall-building chain, in the configuration's OWN frame, W_i in that frame).
  PREDICTION (Lyra, pre-registered as a guess): Φ(c4) < Φ(c0) on every S leaf. Fallback Φ′ = |X3| + |X4|.
  Tunneling cut: |X4 ∩ X3| and |{u ∈ X4 ∩ X3 : c3(u) = r}|; and whether X4 ∩ X3 separates B2 from n_sj
  inside X3 (Menger reading) — tested by the rank instrument on X3 minus the cut.
Part B (the 334 in-frame kills, play/.in_frame_one_word.json; plantri -c5, Elie 5600): rebuild each (n, gi, v,
  canonical coloring); confirm stuck (own τ); W_i, W_j leaves with Δ, Δ′, Q3, Q4; the middle-anchored word
  M_i = (n_sM,(r,s_M))·(n_si,(s_M,s_i)) and its mirror M_j; then the FULL family (186 words, mirror-closed):
  does any fully-legal word image have τ ≤ 4 / ≤ 5 (gate-phase) — the OWL(G) reading Elie's 5601 tests,
  here by an independent instrument. Positive control: the direct-exit claim must FAIL on all 334 (that is
  what Elie measured); a direct hit here means the two instruments disagree and both re-open.
Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, sys, time, glob
from collections import Counter
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
rank_components, same_chain, chain_of, swap, roles, link_word, insertable, tau_rank, leaf, run_word = \
    G.rank_components, G.same_chain, G.chain_of, G.swap, G.roles, G.link_word, G.insertable, G.tau_rank, G.leaf, G.run_word

def stages(adj, col0, v, R, S, word):
    """apply a word given as ((role,(sym,sym)),(role,(sym,sym))) in MY roles; return (legal flags, images, chains)."""
    (r1, p1), (r2, p2) = word
    m1 = (R[r1], (S[p1[0]], S[p1[1]])); m2 = (R[r2], (S[p2[0]], S[p2[1]]))
    col = col0; legal = []; imgs = []; chains = []
    for seed, (a, b) in (m1, m2, m1, m2):
        ok = col[seed] in (a, b); legal.append(ok)
        ch = chain_of(adj, col, seed, a, b, v) if ok else set()
        if ok: col = swap(col, ch, a, b)
        chains.append(ch); imgs.append(col)
    return legal, imgs, chains

def q34(adj, c4, v, R, S):
    nM, ni, nj = R['n_sM'], R['n_si'], R['n_sj']; sM = S['s_M']
    Q3 = same_chain(adj, c4, nM, ni, sM, c4[ni], v)
    Q4 = same_chain(adj, c4, nM, nj, sM, c4[nj], v)
    return Q3, Q4

def phi(adj, c, v, lcyc):
    """|X3| for W_i in c's own frame; None if c is not (2,1,1,1) on the link."""
    rl = roles(c, lcyc)
    if rl is None: return None, None
    R, S = rl
    legal, imgs, chains = stages(adj, c, v, R, S, (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))))
    return len(chains[2]), len(chains[2]) + len(chains[3])

def hard_branch_record(adj, c0, v, lcyc, R, S, which):
    word = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))) if which == 'i' else (('B1', ('r', 's_j')), ('B2', ('r', 's_i')))
    legal, imgs, chains = stages(adj, c0, v, R, S, word)
    c2, c3, c4 = imgs[1], imgs[2], imgs[3]; X3, X4 = chains[2], chains[3]
    near = R['B2'] if which == 'i' else R['B1']; far = R['n_sj'] if which == 'i' else R['n_si']
    delta = far in X3
    other = R['B1'] if which == 'i' else R['B2']; sing = R['n_si'] if which == 'i' else R['n_sj']
    dprime = (near in X4) and (sing in X4)
    if not (delta and not dprime):
        return None
    lf = leaf(adj, c4, v); Q3, Q4 = q34(adj, c4, v, R, S)
    cut = X4 & X3; cut_r = {u for u in cut if c3[u] == S['r']}
    # does the cut separate near from far inside X3 (as a subgraph of c2's (r,s_i)-world)?
    a, b = (S['r'], S['s_i']) if which == 'i' else (S['r'], S['s_j'])
    sub = {u: {w for w in adj[u] if w in X3 and w not in cut} for u in X3 if u not in cut}
    sep = None
    if near in sub and far in sub:
        sep = not same_chain(sub, c2, near, far, a, b, v)
    elif near in cut or far in cut:
        sep = 'endpoint-in-cut'
    p0, pp0 = phi(adj, c0, v, lcyc); p4, pp4 = phi(adj, c4, v, lcyc)
    return {'leaf': lf, 'Q3': Q3, 'Q4': Q4, 'X3': len(X3), 'X4': len(X4), 'cut': len(cut), 'cut_r': len(cut_r), 'sep': sep,
            'phi0': p0, 'phi4': p4, 'phip0': pp0, 'phip4': pp4}

def mirror_word(w):
    mp = {'B1': 'B2', 'B2': 'B1', 'n_si': 'n_sj', 'n_sj': 'n_si', 'n_sM': 'n_sM', 's_i': 's_j', 's_j': 's_i', 's_M': 's_M', 'r': 'r'}
    order = {'r': 0, 's_M': 1, 's_i': 2, 's_j': 3}
    return tuple((mp[r], tuple(sorted((mp[p[0]], mp[p[1]]), key=order.get))) for r, p in w)

if __name__ == "__main__":
    t0 = time.time()
    print("=" * 72); print("Toy 5603 — Grace — G2b: Q3/Q4, Φ, tunneling cut on S leaves; the 334 in-frame kills"); print("=" * 72)
    # ------------------------------------------------ Part A
    pops = G.populations()
    seen = set(); A = []
    for grp, label, i, adj, tv, lcyc, c0 in pops:
        key = (label, str(tv), json.dumps({str(k): v for k, v in c0.items()}, sort_keys=True))
        if key in seen: continue
        seen.add(key)
        rl = roles(c0, lcyc)
        if rl is None or tau_rank(adj, c0, tv) != 6: continue
        R, S = rl
        for which in ('i', 'j'):
            rec = hard_branch_record(adj, c0, tv, lcyc, R, S, which)
            if rec: rec.update({'pop': label, 'i': i, 'word': which}); A.append(rec)
    hA = hashlib.sha256(json.dumps([json.dumps(x, sort_keys=True, default=str) for x in A]).encode()).hexdigest()
    print(f"\n[A] {len(seen)} distinct configurations; hard-branch instances {len(A)}; hashed BEFORE counts {hA[:32]}…  [{time.time()-t0:.0f}s]")
    for which in ('i', 'j'):
        B = [x for x in A if x['word'] == which]
        S_ = [x for x in B if x['leaf'] == 'S']; Gl = [x for x in B if x['leaf'] != 'S']
        ok = sum(1 for x in B if (x['leaf'] == 'S') == (x['Q3'] and x['Q4']))
        print(f"  W_{which}: hard branch {len(B)} = S {len(S_)} + G {len(Gl)}; Lemma T 'S ⟺ Q3∧Q4': {ok}/{len(B)}; "
              f"S leaves (Q3,Q4) {dict(Counter((x['Q3'],x['Q4']) for x in S_))}; G leaves (Q3,Q4) {dict(Counter((x['Q3'],x['Q4']) for x in Gl))}")
        dec = sum(1 for x in S_ if x['phi4'] is not None and x['phi4'] < x['phi0']); nn = sum(1 for x in S_ if x['phi4'] is not None)
        dec2 = sum(1 for x in S_ if x['phip4'] is not None and x['phip4'] < x['phip0'])
        print(f"        Φ=|X3| strictly decreases on S leaves: {dec}/{nn}; Φ′=|X3|+|X4|: {dec2}/{nn}; "
              f"Φ0→Φ4 examples {[(x['phi0'],x['phi4']) for x in S_[:8]]}")
        print(f"        tunneling cut on S leaves: |X4∩X3| {dict(Counter(x['cut'] for x in S_))}; r-part {dict(Counter(x['cut_r'] for x in S_))}; "
              f"cut separates near from far inside X3: {dict(Counter(str(x['sep']) for x in S_))}")
        print(f"        on G leaves: |X4∩X3| {dict(Counter(x['cut'] for x in Gl))}; sep {dict(Counter(str(x['sep']) for x in Gl))}")
    # ------------------------------------------------ Part B
    M = load("t5600g", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1])
    OF, EA, IF, E1, WF = M.OF, M.EA, M.IF, M.E1, M.WF
    kills = [eval(k) for k in json.load(open(os.path.join(HERE, '.in_frame_one_word.json')))['kills']]
    byn = {}
    for n, gi, v, ct in kills: byn.setdefault(n, []).append((gi, v, ct))
    print(f"\n[B] in-frame kills: {len(kills)} by n {dict(Counter(k[0] for k in kills))}")
    moves, words, _ = WF.context_family()
    fam = set(words); assert all(mirror_word(w) in fam for w in fam), "family not mirror-closed"
    Wi = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))); Wj = mirror_word(Wi)
    Mi = (('n_sM', ('r', 's_M')), ('n_si', ('s_M', 's_i'))); Mj = mirror_word(Mi)
    B = []
    for n in sorted(byn):
        gs = EA.plantri_graphs(n, flags=('-c5',))
        for gi, v, ct in byn[n]:
            adj = gs[gi]; faces, ok = OF.faces_of(adj)
            order = sorted(u for u in adj if u != v); c0 = {u: ct[k] for k, u in enumerate(order)}
            lcyc = E1.link_cycle(faces, v)
            tau0 = tau_rank(adj, c0, v)
            rl = roles(c0, lcyc)
            rec = {'n': n, 'gi': gi, 'v': v, 'tau0': tau0, 'roles': rl is not None}
            if rl is None or tau0 != 6:
                B.append(rec); continue
            R, S = rl
            for nm, w in (('Wi', Wi), ('Wj', Wj), ('Mi', Mi), ('Mj', Mj)):
                legal, imgs, chains = stages(adj, c0, v, R, S, w)
                l3 = leaf(adj, imgs[2], v) if all(legal[:3]) else None
                l4 = leaf(adj, imgs[3], v) if all(legal) else None
                rec[nm] = {'legal': legal, 'lw': link_word(imgs[3], R, S), 'leaf3': l3, 'leaf4': l4}
                if nm in ('Wi', 'Wj'):
                    near = R['B2'] if nm == 'Wi' else R['B1']; far = R['n_sj'] if nm == 'Wi' else R['n_si']
                    other = R['B1'] if nm == 'Wi' else R['B2']; sing = R['n_si'] if nm == 'Wi' else R['n_sj']
                    rec[nm]['delta'] = far in chains[2]; rec[nm]['dprime'] = (near in chains[3]) and (sing in chains[3])
                    rec[nm]['Q34'] = q34(adj, imgs[3], v, R, S)
            # full family: best leaf over all fully-legal word images (direct / gate)
            best = 'S'; direct = 0; gate = 0; legal_n = 0
            for w in words:
                legal, imgs, chains = stages(adj, c0, v, R, S, w)
                if not all(legal): continue
                legal_n += 1
                c4 = imgs[3]
                if insertable(adj, c4, v): direct += 1; best = 'I'
                elif tau_rank(adj, c4, v) <= 5:
                    gate += 1
                    if best != 'I': best = 'G'
            rec['family'] = {'legal_words': legal_n, 'direct': direct, 'gate': gate, 'best': best}
            B.append(rec)
        print(f"  n={n} done [{time.time()-t0:.0f}s]", flush=True)
    hB = hashlib.sha256(json.dumps([json.dumps(x, sort_keys=True, default=str) for x in B]).encode()).hexdigest()
    ok = [x for x in B if x.get('family')]
    print(f"\n[B] records hashed BEFORE counts {hB[:32]}…; stuck-with-roles {len(ok)}/{len(B)}; τ0 {dict(Counter(x['tau0'] for x in B))}")
    print(f"  POSITIVE CONTROL (direct exit must fail on all): direct hits {sum(1 for x in ok if x['family']['direct']>0)}/{len(ok)}")
    print(f"  full family, best leaf: {dict(Counter(x['family']['best'] for x in ok))}; gate-phase words per config {dict(Counter(x['family']['gate'] for x in ok))}; legal words per config {dict(Counter(x['family']['legal_words'] for x in ok))}")
    for nm in ('Wi', 'Wj', 'Mi', 'Mj'):
        print(f"  {nm}: legal4 {sum(1 for x in ok if all(x[nm]['legal']))}/{len(ok)}; leaf4 {dict(Counter(x[nm]['leaf4'] for x in ok))}; leaf3 {dict(Counter(x[nm]['leaf3'] for x in ok))}"
              + (f"; (Δ,Δ′) {dict(Counter((x[nm]['delta'],x[nm]['dprime']) for x in ok))}; Q3∧Q4 on S {dict(Counter(x[nm]['Q34'] for x in ok if x[nm]['leaf4']=='S'))}" if nm in ('Wi','Wj') else ''))
    print(f"  by n, best leaf: {dict(Counter((x['n'],x['family']['best']) for x in ok))}")
    json.dump({'A_hash': hA, 'A': A, 'B_hash': hB, 'B': B}, open(os.path.join(HERE, '.out_5603.json'), 'w'), default=str)
    print(f"\n  written .out_5603.json  [{time.time()-t0:.0f}s]")
