#!/usr/bin/env python3
"""
Toy 5640 — census paper v0.2 marker (Lyra 07:20, marker (ii) third number): "the probability that a bridge word's
image is itself commutator-locked near 80 percent (population: the two bridge-word images of each of the 349 locks)".
Grace, 2026-09-03.  Measured directly: for each of the 349 two-word-locked configurations (files of toy 5625), the
two bridge-word images c4 (W_i, W_j; toy 5603 `stages`), and on each image the depth-one lock test in the image's
OWN re-derived context (Cal §825 definition): gate phase if a colour is absent at the link or tau <= 5 (rank
instrument); otherwise roles re-derived; locked iff NO fully legal word of the 186-word family carries the image into
the gate phase (toy 5603 Part B test, verbatim).  Reported: locked / 698 by n; the 5603 leaf table (all 698 are S =
stuck, by the lock's definition) is the control that the images are the right objects.
"""
import hashlib, importlib.util, json, os, time, glob
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname)); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
M = load("t5600g", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1]); OF, EA, E1, WF = M.OF, M.EA, M.E1, M.WF
t0 = time.time()
moves, words, _ = WF.context_family(); assert len(words) == 186, len(words)
Wi = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))); Wj = T.mirror_word(Wi)
def gate(adj, c, v): return len({c[u] for u in adj[v]}) < 4 or G.tau_rank(adj, c, v) <= 5
def locked(adj, c, v, lcyc):
    """returns ('gate' | 'locked' | 'exits', legal_words, exiting_words)"""
    if gate(adj, c, v): return 'gate', None, None
    rl = G.roles(c, lcyc)
    if rl is None: return 'no-roles', None, None
    R, S = rl; legal_n = 0; ex = 0
    for w in words:
        legal, imgs, chains = T.stages(adj, c, v, R, S, w)
        if not all(legal): continue
        legal_n += 1
        if gate(adj, imgs[3], v): ex += 1
    return ('locked' if ex == 0 else 'exits'), legal_n, ex
files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78), ('.in_frame_256_two_word_locked_n24.json', 122)]
W = []
for fn, base in files:
    for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))): W.append((x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{base+k:03d}"))
cache = {}; recs = []
for (n, gi, v, ct, fid) in W:
    if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
    adj = cache[n][gi]; faces, ok = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v)
    order = sorted(u for u in adj if u != v); c0 = {u: ct[k] for k, u in enumerate(order)}
    R, S = G.roles(c0, lcyc); assert G.tau_rank(adj, c0, v) == 6
    rec = {'id': fid, 'n': n}
    for nm, w in (('Wi', Wi), ('Wj', Wj)):
        legal, imgs, chains = T.stages(adj, c0, v, R, S, w); assert all(legal), (fid, nm)
        st, ln, ex = locked(adj, imgs[3], v, lcyc)
        rec[nm] = {'status': st, 'legal_words': ln, 'exiting_words': ex, 'leaf': G.leaf(adj, imgs[3], v)}
    recs.append(rec)
hh = hashlib.sha256(json.dumps(recs, sort_keys=True).encode()).hexdigest()
print(f"hashed BEFORE counts {hh[:16]}…  [{time.time()-t0:.0f}s]")
st = Counter(); byn = {}
for r in recs:
    for nm in ('Wi', 'Wj'):
        st[r[nm]['status']] += 1; byn.setdefault(r['n'], Counter())[r[nm]['status']] += 1
tot = sum(st.values())
print(f"bridge-word images of the 349 locks: {tot}; status {dict(st)}; LOCKED share {st['locked']/tot:.4f}")
for n in sorted(byn): print(f"   n={n}: {dict(byn[n])}  locked share {byn[n]['locked']/sum(byn[n].values()):.3f}")
print("control: leaf of every bridge image =", dict(Counter(r[nm]['leaf'] for r in recs for nm in ('Wi','Wj'))))
ex = [r[nm]['exiting_words'] for r in recs for nm in ('Wi','Wj') if r[nm]['status']=='exits']
print("exiting images: exiting-word counts", dict(Counter(ex)) if ex else {}, "; legal words per image", dict(Counter(r[nm]['legal_words'] for r in recs for nm in ('Wi','Wj') if r[nm]['legal_words'] is not None)))
json.dump({'hash': hh, 'records': recs}, open(os.path.join(HERE, '.out_5640.json'), 'w'))
print(f"SCORE: REPORTED — the v0.2 marker number, measured [{time.time()-t0:.0f}s]")
