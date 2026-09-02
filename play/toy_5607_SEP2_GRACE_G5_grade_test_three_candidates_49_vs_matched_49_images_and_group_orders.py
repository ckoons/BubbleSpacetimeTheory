"""
Toy 5607 — Grace — G5: THE GRADE TEST (K1839 §3 Lane C; Casey Round 98). Three candidates, ONE trial each,
PRE-REGISTERED here before any number is seen. Population: the 49 in-frame two-word (gate-locked) stuck
configurations (FCW-029..077) vs a MATCHED sample of 49 depth-1 stuck configurations — same graph, same vertex v,
chosen deterministically (seed 5607) among stuck colorings of T−v that exit to the gate phase in ONE word and
are Δ-YES for W_i (so a fence exists in both groups). Reported as SEPARATION COUNTS, never verdicts.

Candidates (all target-innocent: computed from (T, v, c) alone, no menu, no target set):
 (i)  Mohar–Salas degree on T−v's triangular faces: D_t = p_t − n_t per tetrahedron face t (oriented faces from
      plantri's clockwise rotation system, parsed here), D = Σ_t D_t, D mod 12; pentagon term P_x = signed count
      of the five boundary triangles (v, l_k, l_{k+1}) with v colored x wherever proper (per x).
 (ii) Eulerian distance near v (toy 5517's lens): odd-degree vertex count in T, in T−v, within distance 1 and 2
      of v in T.
 (iii) fence-region size (Casey's subpatch): for W_i at c₂, the shortest (r,s_i)-path P from B₂ to n_sj; region =
      |component of (T−v) − V(P) containing n_si| (near-singleton side); also the far side and |P|.
Also reported (not candidates): distinct images over the fully-legal 186-word family; ORBIT size under the 15
link-seeded moves (chains re-derived at every node, cap 4000) and the ORDER of the permutation group the 15
moves generate on that orbit (sympy), for witness vs matched.
Pre-score (K1839): 49/49 vs 0/49 on a scalar = a GRADE; partial = a feature; none = the candidate dies.
Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, random, subprocess, sys, time, glob
from collections import Counter, deque
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
PLANTRI = os.path.join(HERE, 'tools', 'plantri58', 'plantri')
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
M = load("t5600g5", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1])
EA, E1, WF = M.EA, M.E1, M.WF
rank_components, same_chain, chain_of, swap, roles, insertable, tau_rank, leaf = \
    G.rank_components, G.same_chain, G.chain_of, G.swap, G.roles, G.insertable, G.tau_rank, G.leaf

def plantri_rot(n, flags=('-c5',)):
    """graphs as (adj sets, rotation lists in plantri's clockwise order)."""
    out = subprocess.run([PLANTRI, '-a', *flags, str(n)], capture_output=True, text=True).stdout
    gs = []
    for line in out.splitlines():
        line = line.strip()
        if not line or not line[0].isdigit(): continue
        nv, rest = line.split(' ', 1); nv = int(nv)
        rot = {i: [ord(ch) - 97 for ch in p] for i, p in enumerate(rest.split(','))}
        adj = {i: set(rot[i]) for i in rot}
        gs.append((adj, rot))
    return gs

def oriented_faces(rot):
    seen = set(); faces = []
    for u, r in rot.items():
        for k in range(len(r)):
            a, b = r[k], r[(k + 1) % len(r)]
            key = frozenset((u, a, b))
            if key in seen: continue
            seen.add(key); faces.append((u, a, b))
    return faces

TET = set()
for f in ((1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1)):
    for k in range(3): TET.add((f[k], f[(k + 1) % 3], f[(k + 2) % 3]))
def face_sign(cols):
    return 1 if tuple(cols) in TET else -1

def ms_degree(faces, col, v):
    Dt = Counter(); D = 0
    for (a, b, c) in faces:
        if v in (a, b, c): continue
        cs = (col[a], col[b], col[c]); s = face_sign(cs)
        Dt[frozenset(cs)] += s; D += s
    return D, {str(sorted(k)): val for k, val in Dt.items()}

def pentagon_terms(faces, col, v):
    P = {}
    bf = [f for f in faces if v in f]
    for x in range(4):
        tot = 0; ok = True
        for (a, b, c) in bf:
            cs = tuple(x if u == v else col[u] for u in (a, b, c))
            if len(set(cs)) < 3: ok = False; break
            tot += face_sign(cs)
        P[x] = tot if ok else None
    return P

def odd_features(adj, v):
    deg = {u: len(adj[u]) for u in adj}
    odd_T = sum(1 for u in adj if deg[u] % 2)
    degm = {u: len(adj[u] - {v}) for u in adj if u != v}
    odd_Tv = sum(1 for u in degm if degm[u] % 2)
    d1 = set(adj[v]); d2 = set().union(*(adj[u] for u in d1)) - {v}
    return {'odd_T': odd_T, 'odd_Tv': odd_Tv, 'odd_d1': sum(1 for u in d1 if deg[u] % 2), 'odd_d2': sum(1 for u in d2 if deg[u] % 2), 'odd_d1_Tv': sum(1 for u in d1 if degm[u] % 2)}

def fence(adj, c0, v, R, S):
    """W_i stages 1-2, then shortest (r,s_i)-path P from B2 to n_sj in c2; region sizes."""
    legal, imgs, chains = T.stages(adj, c0, v, R, S, (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))))
    c2 = imgs[1]; r, si = S['r'], S['s_i']
    P = G.bfs_path(adj, c2, R['B2'], R['n_sj'], r, si, v)
    if P is None: return None
    Pv = set(P); rest = [u for u in adj if u != v and u not in Pv]
    # components of (T−v) − P
    comp = {}; cid = 0
    for s in rest:
        if s in comp: continue
        q = deque([s]); comp[s] = cid
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w != v and w not in Pv and w not in comp: comp[w] = cid; q.append(w)
        cid += 1
    sizes = Counter(comp.values())
    near = comp.get(R['n_si']); far_side = [k for k in sizes if k != near]
    return {'fence_len': len(P) - 1, 'region_near': sizes.get(near, 0), 'region_far': sum(sizes[k] for k in far_side), 'n_components': cid,
            'X3': len(chains[2]), 'X4': len(chains[3]), 'cut': len(chains[2] & chains[3])}

def images_and_orbit(adj, c0, v, R, S, words, cap=4000):
    imgs = set(); legal = 0
    for w in words:
        lg, im, ch = T.stages(adj, c0, v, R, S, w)
        if all(lg): legal += 1; imgs.add(tuple(sorted(im[3].items())))
    # orbit under the 15 link-seeded moves (seed = link vertex, pair containing its color)
    link = list(adj[v]); pairs = list(itertools.combinations(range(4), 2))
    moves = [(u, p) for u in link for p in pairs]
    key0 = tuple(sorted(c0.items())); orbit = {key0: 0}; order = [key0]; q = deque([c0]); perms = {m: {} for m in moves}
    while q and len(orbit) <= cap:
        c = q.popleft(); kc = tuple(sorted(c.items()))
        for (u, (a, b)) in moves:
            if c[u] not in (a, b): perms[(u, (a, b))][orbit[kc]] = orbit[kc]; continue
            ch = G.chain_of(adj, c, u, a, b, v); c2 = swap(c, ch, a, b); k2 = tuple(sorted(c2.items()))
            if k2 not in orbit:
                orbit[k2] = len(order); order.append(k2); q.append(c2)
            perms[(u, (a, b))][orbit[kc]] = orbit[k2]
    capped = len(orbit) > cap
    gorder = None
    if not capped:
        try:
            from sympy.combinatorics import Permutation, PermutationGroup
            N = len(orbit); gens = []
            for m in moves:
                arr = [perms[m].get(i, i) for i in range(N)]
                if arr != list(range(N)): gens.append(Permutation(arr))
            gorder = int(PermutationGroup(gens).order()) if gens else 1
        except Exception as ex:
            gorder = f'err:{type(ex).__name__}'
    return {'legal_words': legal, 'distinct_images': len(imgs), 'orbit': len(orbit), 'orbit_capped': capped, 'group_order': gorder}

def depth1_gate(adj, c0, v, R, S, words):
    for w in words:
        lg, im, ch = T.stages(adj, c0, v, R, S, w)
        if all(lg) and tau_rank(adj, im[3], v) <= 5: return True
    return False

def features(adj, rot, faces, c0, v, words, R, S):
    D, Dt = ms_degree(faces, c0, v); P = pentagon_terms(faces, c0, v)
    f = {'D': D, 'D_mod12': D % 12, 'Dt_max_abs': max(abs(x) for x in Dt.values()), 'Dt': Dt, 'P': P,
         'P_defined': sum(1 for x in P.values() if x is not None)}
    f.update(odd_features(adj, v)); fz = fence(adj, c0, v, R, S); f['fence'] = fz
    f.update(images_and_orbit(adj, c0, v, R, S, words)); return f

if __name__ == "__main__":
    t0 = time.time(); random.seed(5607)
    w26 = json.load(open(os.path.join(HERE, '.in_frame_26_two_word_locked.json'))); w23 = json.load(open(os.path.join(HERE, '.in_frame_23_two_word_locked_n22.json')))
    W = [(x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{29+k:03d}") for k, x in enumerate(w26)] + \
        [(x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{55+k:03d}") for k, x in enumerate(w23)]
    print("=" * 72); print(f"Toy 5607 — Grace — G5 grade test: {len(W)} witnesses vs matched depth-1 sample"); print("=" * 72)
    moves, words, _ = WF.context_family()
    cache = {}; recs = []
    for (n, gi, v, ct, fid) in W:
        if n not in cache: cache[n] = plantri_rot(n)
        adj, rot = cache[n][gi]; faces = oriented_faces(rot)
        order = sorted(u for u in adj if u != v); c0 = {u: ct[k] for k, u in enumerate(order)}
        lcyc = E1.link_cycle([tuple(f) for f in faces], v); R, S = roles(c0, lcyc)
        assert tau_rank(adj, c0, v) == 6
        fw = features(adj, rot, faces, c0, v, words, R, S)
        # matched depth-1: same (n, gi, v); stuck; one-word gate exit; W_i Δ-YES
        sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
        cols = EA.all_colorings_mod_s4(sub, order); random.shuffle(cols)
        match = None; tried = 0
        for c in cols:
            cm = {u: c[k] for k, u in enumerate(order)}
            if cm == c0 or insertable(adj, cm, v) or tau_rank(adj, cm, v) != 6: continue
            rl = roles(cm, lcyc)
            if rl is None: continue
            Rm, Sm = rl; tried += 1
            lg, im, ch = T.stages(adj, cm, v, Rm, Sm, (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))))
            if Rm['n_sj'] not in ch[2]: continue          # need Δ-YES so a fence exists
            if not depth1_gate(adj, cm, v, Rm, Sm, words): continue
            match = (cm, Rm, Sm); break
        fm = features(adj, rot, faces, match[0], v, words, match[1], match[2]) if match else None
        recs.append({'id': fid, 'n': n, 'gi': gi, 'v': v, 'witness': fw, 'matched': fm, 'matched_coloring': [match[0][u] for u in order] if match else None, 'tried': tried})
        print(f"  {fid} n={n} gi={gi} v={v}: matched after {tried} stuck Δ-YES candidates [{time.time()-t0:.0f}s]", flush=True)
    hh = hashlib.sha256(json.dumps([json.dumps(r, sort_keys=True, default=str) for r in recs]).encode()).hexdigest()
    print(f"\n  records hashed BEFORE counts: sha256 {hh[:32]}…  matched {sum(1 for r in recs if r['matched'])}/{len(recs)}")
    def scal(f, key):
        if key.startswith('fence.'): return None if f['fence'] is None else f['fence'][key[6:]]
        return f.get(key)
    KEYS = ['D', 'D_mod12', 'Dt_max_abs', 'P_defined', 'odd_T', 'odd_Tv', 'odd_d1', 'odd_d2', 'odd_d1_Tv',
            'fence.fence_len', 'fence.region_near', 'fence.region_far', 'fence.n_components', 'fence.X3', 'fence.X4', 'fence.cut',
            'legal_words', 'distinct_images', 'orbit', 'group_order']
    print("\n  SEPARATION TABLE (candidate | witness values | matched values | witnesses outside matched range | matched outside witness range | best-threshold split)")
    for key in KEYS:
        wv = [scal(r['witness'], key) for r in recs]; mv = [scal(r['matched'], key) for r in recs if r['matched']]
        wv = [x for x in wv if isinstance(x, (int, float))]; mv = [x for x in mv if isinstance(x, (int, float))]
        if not wv or not mv: print(f"  {key}: no numeric values"); continue
        lo, hi = min(mv), max(mv); wlo, whi = min(wv), max(wv)
        out_w = sum(1 for x in wv if x < lo or x > hi); out_m = sum(1 for x in mv if x < wlo or x > whi)
        best = 0
        for th in sorted(set(wv + mv)):
            for sgn in (1, -1):
                acc = sum(1 for x in wv if sgn * x >= sgn * th) + sum(1 for x in mv if sgn * x < sgn * th)
                best = max(best, acc)
        print(f"  {key:22s} | W {dict(sorted(Counter(wv).items()))} | M {dict(sorted(Counter(mv).items()))} | {out_w}/{len(wv)} | {out_m}/{len(mv)} | {best}/{len(wv)+len(mv)}")
    json.dump({'hash': hh, 'records': recs}, open(os.path.join(HERE, '.out_5607.json'), 'w'), default=str)
    print(f"\n  written .out_5607.json [{time.time()-t0:.0f}s]")
