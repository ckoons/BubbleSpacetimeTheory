"""
Toy 5610 — Grace — Round 99: (A) the CUT's anatomy on the 93 two-word witnesses vs a matched depth-1 sample
(same graph, same v, stuck, W_i Δ-YES, one-word gate exit; seed 5610): |C|, distance of C to the link, distance
to the nearest degree-5 vertex of T (other than v), and the HEIGHT TYPE of each cut vertex — operationalized as
the winding number w_u = c_u/3 of u's neighbour colors around the color triangle (T2594 vertex-charge form;
w_u = 0 := SADDLE, |w_u| ≥ 1 := monotone) — flagged as my operationalization of K1840's "height saddle."
(B) H_cut read as RANK (G1): C := X₄ ∩ X₃ for W_i from the original coloring; C disconnects X₃ ⟺
dim ker L(X₃ − C) > dim ker L(X₃); then for EVERY legal first word w: do its four stage chains contain C
(all / any / none), and does the image exit by a bridge word in its own frame? Cross-tab, non-exiting words as
control. κ(w·c) := |C(w·c)| after the word (potential #8, K1840).
(C) The grade test continued with the BOUNDARY-TERM LEMMA (T2594) as its formula: D′(c) = Σ_t z_t over T−v's
oriented triangles; POSITIVE CONTROL FIRST — ΔD′ = −2·S_X on every legal stage of W_i and W_j on every
configuration (one miss = orientation bug or lemma bug; no grade is read until it passes); then D′, D′ mod 12,
odd-vertex counts (ii), fence region (iii) as separation counts, never verdicts. Images per configuration too.
Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, random, sys, time, glob
from collections import Counter, deque
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
F = load("t5607", "toy_5607_SEP2_GRACE_G5_grade_test_three_candidates_49_vs_matched_49_images_and_group_orders.py")
M = load("t5600g6", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1])
EA, E1, WF, G5, X3m = M.EA, M.E1, M.WF, M.G5, M.X3
rank_components, chain_of, swap, roles, insertable, tau_rank, leaf = G.rank_components, G.chain_of, G.swap, G.roles, G.insertable, G.tau_rank, G.leaf
WI = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))); WJ = T.mirror_word(WI)

def dist_from(adj, sources, v):
    d = {s: 0 for s in sources}; q = deque(sources)
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w != v and w not in d: d[w] = d[u] + 1; q.append(w)
    return d

def zt(faces, col, v):
    return {f: F.face_sign((col[f[0]], col[f[1]], col[f[2]])) for f in faces if v not in f}

def Dprime(faces, col, v): return sum(zt(faces, col, v).values())

def S_X(faces, col, v, X):
    return sum(z for f, z in zt(faces, col, v).items() if any(u in X for u in f))

def winding(faces, col, v, u):
    return sum(z for f, z in zt(faces, col, v).items() if u in f)   # = 3 w_u when all faces at u lie in T−v

def bridge_exit_in_frame(adj, c, v, lcyc):
    """image c: insertable/gate directly, or by W_i/W_j in c's own frame; returns (status, kappa_i, kappa_j)."""
    if insertable(adj, c, v): return 'I', 0, 0
    if tau_rank(adj, c, v) <= 5: return 'G', 0, 0
    rl = roles(c, lcyc)
    if rl is None: return 'no-roles', None, None
    R, S = rl; res = []; kap = []
    for w in (WI, WJ):
        lg, im, ch = T.stages(adj, c, v, R, S, w)
        res.append(leaf(adj, im[3], v) if all(lg) else 'illegal'); kap.append(len(ch[2] & ch[3]))
    st = 'bridge-exit' if any(x in ('I', 'G') for x in res) else 'stuck'
    return st, kap[0], kap[1]

def anatomy(adj, faces, c0, v, lcyc, R, S, deg5, words, do_hcut=True):
    n = len(adj)
    lg, im, ch = T.stages(adj, c0, v, R, S, WI); X3, X4 = ch[2], ch[3]; C = X3 & X4; c2 = im[1]
    # rank reading of the cut
    sub3 = {u: {w for w in adj[u] if w in X3} for u in X3}
    _, k0 = rank_components(sub3, c2, S['r'], S['s_i'], v)
    rest = {u: {w for w in adj[u] if w in X3 and w not in C} for u in X3 if u not in C}
    _, k1 = rank_components(rest, c2, S['r'], S['s_i'], v) if rest else ({}, 0)
    near, far = R['B2'], R['n_sj']
    sep = (near in rest and far in rest and not G.same_chain(rest, c2, near, far, S['r'], S['s_i'], v)) if rest else None
    link = set(adj[v]); dl = dist_from(adj, list(link), v); d5 = dist_from(adj, [u for u in deg5 if u != v], v)
    rec = {'C': sorted(map(str, C)), 'C_size': len(C), 'X3': len(X3), 'X4': len(X4), 'ker_X3': k0, 'ker_X3_minus_C': k1, 'C_separates': sep,
           'C_dist_link': min((dl.get(u, 99) for u in C), default=None), 'C_on_link': sum(1 for u in C if u in link),
           'C_dist_deg5': min((d5.get(u, 99) for u in C), default=None),
           'C_winding': [winding(faces, c0, v, u) // 3 if u not in link else None for u in C],
           'Dprime': Dprime(faces, c0, v), 'Dprime_mod12': Dprime(faces, c0, v) % 12}
    rec['C_saddles'] = sum(1 for w in rec['C_winding'] if w == 0); rec['C_saddle_unknown'] = sum(1 for w in rec['C_winding'] if w is None)
    # T2594 positive control on W_i and W_j stages
    ok = 0; tot = 0
    for w in (WI, WJ):
        lgw, imw, chw = T.stages(adj, c0, v, R, S, w); prev = c0
        for k in range(4):
            if not lgw[k]: prev = imw[k]; continue
            dD = Dprime(faces, imw[k], v) - Dprime(faces, prev, v); tot += 1
            if dD == -2 * S_X(faces, prev, v, chw[k]): ok += 1
            prev = imw[k]
    rec['T2594_ok'] = ok; rec['T2594_tot'] = tot
    rec.update(F.odd_features(adj, v)); rec['fence'] = F.fence(adj, c0, v, R, S)
    # images + H_cut cross-tab
    imgs = set(); ct = Counter(); kap_after = []
    for w in words:
        lgw, imw, chw = T.stages(adj, c0, v, R, S, w)
        if not all(lgw): continue
        c4 = imw[3]; imgs.add(tuple(sorted(c4.items())))
        if not do_hcut: continue
        U = set().union(*chw); call = C <= U; cany = bool(C & U)
        st, ki, kj = bridge_exit_in_frame(adj, c4, v, lcyc)
        exit_ = st in ('I', 'G', 'bridge-exit')
        ct[(('all' if call else ('any' if cany else 'none')), exit_)] += 1
        if exit_ and ki is not None: kap_after.append(min(ki, kj))
    rec['images'] = len(imgs); rec['hcut'] = {f"{a}|{'exit' if b else 'noexit'}": k for (a, b), k in ct.items()}; rec['kappa_after_exit'] = dict(Counter(kap_after))
    return rec

if __name__ == "__main__":
    t0 = time.time(); random.seed(5610)
    files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78)]
    W = []
    for fn, base in files:
        for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))):
            W.append((x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{base+k:03d}"))
    print("=" * 72); print(f"Toy 5610 — Grace — cut anatomy + H_cut as rank + T2594 grade: {len(W)} witnesses vs matched"); print("=" * 72, flush=True)
    moves, words, _ = WF.context_family(); cache = {}; recs = []
    for (n, gi, v, ct, fid) in W:
        if n not in cache: cache[n] = F.plantri_rot(n)
        adj, rot = cache[n][gi]; faces = F.oriented_faces(rot); ftup = [tuple(f) for f in faces]
        deg5 = {u for u in adj if len(adj[u]) == 5}
        order = sorted(u for u in adj if u != v); c0 = {u: ct[k] for k, u in enumerate(order)}
        lcyc = E1.link_cycle(ftup, v); R, S = roles(c0, lcyc); assert tau_rank(adj, c0, v) == 6
        aw = anatomy(adj, faces, c0, v, lcyc, R, S, deg5, words)
        # matched depth-1 (fast selection with Elie's primitives; measured with mine)
        sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
        cols = EA.all_colorings_mod_s4(sub, order); random.shuffle(cols); match = None; tried = 0
        for c in cols:
            cm = {u: c[k] for k, u in enumerate(order)}
            if cm == c0 or len({cm[u] for u in adj[v]}) < 4 or G5.operational_tau(adj, cm, v) != 6: continue
            rl = roles(cm, lcyc)
            if rl is None: continue
            Rm, Sm = rl; tried += 1
            lg, im, ch = T.stages(adj, cm, v, Rm, Sm, WI)
            if Rm['n_sj'] not in ch[2]: continue
            gate1 = False
            for w in words:
                m1 = (Rm[w[0][0]], (Sm[w[0][1][0]], Sm[w[0][1][1]])); m2 = (Rm[w[1][0]], (Sm[w[1][1][0]], Sm[w[1][1][1]]))
                col = cm; legal = True
                for seed, (a, b) in (m1, m2, m1, m2):
                    if col[seed] not in (a, b): legal = False; break
                    col = G5.do_swap(col, G5.kempe_chain(adj, col, seed, a, b, exclude={v}), a, b)
                if legal and (len({col[u] for u in adj[v]}) < 4 or G5.operational_tau(adj, col, v) <= 5): gate1 = True; break
            if gate1: match = (cm, Rm, Sm); break
        am = anatomy(adj, faces, match[0], v, lcyc, match[1], match[2], deg5, words) if match else None
        recs.append({'id': fid, 'n': n, 'gi': gi, 'v': v, 'witness': aw, 'matched': am, 'matched_coloring': [match[0][u] for u in order] if match else None, 'tried': tried})
        print(f"  {fid} n={n} gi={gi} v={v}: |C|={aw['C_size']} sep={aw['C_separates']} T2594 {aw['T2594_ok']}/{aw['T2594_tot']} hcut={aw['hcut']} | matched after {tried} [{time.time()-t0:.0f}s]", flush=True)
    hh = hashlib.sha256(json.dumps([json.dumps(r, sort_keys=True, default=str) for r in recs]).encode()).hexdigest()
    print(f"\n  records hashed BEFORE counts: sha256 {hh[:32]}…  matched {sum(1 for r in recs if r['matched'])}/{len(recs)}")
    W_ = [r['witness'] for r in recs]; M_ = [r['matched'] for r in recs if r['matched']]
    pc = sum(x['T2594_ok'] for x in W_ + M_); pt = sum(x['T2594_tot'] for x in W_ + M_)
    print(f"\n[POSITIVE CONTROL] T2594 ΔD′ = −2·S_X on every legal stage: {pc}/{pt}")
    print(f"[CUT AS RANK] witnesses: C separates near from far inside X3: {sum(1 for x in W_ if x['C_separates'])}/{len(W_)}; ker(X3)={dict(Counter(x['ker_X3'] for x in W_))}; ker(X3−C)={dict(Counter(x['ker_X3_minus_C'] for x in W_))}")
    print(f"              matched:   C separates: {sum(1 for x in M_ if x['C_separates'])}/{len(M_)}; |C|=0 on {sum(1 for x in M_ if x['C_size']==0)}/{len(M_)}")
    hc = Counter(); hm = Counter()
    for x in W_: hc.update(x['hcut'])
    for x in M_: hm.update(x['hcut'])
    print(f"[H_cut cross-tab, witnesses — (containment of C by the first word's chains | image exits by a bridge word)]: {dict(hc)}")
    print(f"[H_cut cross-tab, matched]: {dict(hm)}")
    print(f"[κ after an exiting first word, witnesses]: {dict(sum((Counter(x['kappa_after_exit']) for x in W_), Counter()))}")
    def scal(f, key):
        if key.startswith('fence.'): return None if f['fence'] is None else f['fence'][key[6:]]
        return f.get(key)
    KEYS = ['C_size', 'C_dist_link', 'C_on_link', 'C_dist_deg5', 'C_saddles', 'C_saddle_unknown', 'X3', 'X4', 'Dprime', 'Dprime_mod12',
            'odd_T', 'odd_Tv', 'odd_d1', 'odd_d2', 'fence.fence_len', 'fence.region_near', 'fence.region_far', 'images']
    print("\n  SEPARATION TABLE (feature | witness values | matched values | witnesses outside matched range | matched outside witness range | best split)")
    for key in KEYS:
        wv = [scal(x, key) for x in W_]; mv = [scal(x, key) for x in M_]
        wv = [x for x in wv if isinstance(x, (int, float))]; mv = [x for x in mv if isinstance(x, (int, float))]
        if not wv or not mv: print(f"  {key}: no numeric values"); continue
        lo, hi = min(mv), max(mv); wlo, whi = min(wv), max(wv)
        out_w = sum(1 for x in wv if x < lo or x > hi); out_m = sum(1 for x in mv if x < wlo or x > whi); best = 0
        for th in sorted(set(wv + mv)):
            for sgn in (1, -1):
                best = max(best, sum(1 for x in wv if sgn * x >= sgn * th) + sum(1 for x in mv if sgn * x < sgn * th))
        print(f"  {key:18s} | W {dict(sorted(Counter(wv).items()))} | M {dict(sorted(Counter(mv).items()))} | {out_w}/{len(wv)} | {out_m}/{len(mv)} | {best}/{len(wv)+len(mv)}")
    print(f"  cut-vertex winding (witnesses, all cut vertices): {dict(Counter(w for x in W_ for w in x['C_winding']))}; matched: {dict(Counter(w for x in M_ for w in x['C_winding']))}")
    json.dump({'hash': hh, 'records': recs}, open(os.path.join(HERE, '.out_5610.json'), 'w'), default=str)
    print(f"\n  written .out_5610.json [{time.time()-t0:.0f}s]")
