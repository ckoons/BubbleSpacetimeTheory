"""
Toy 5621 — Grace — Cal §823 §4(a), the DECISIVE TEST, pre-registered by Cal before Lyra's derivation lands:
compute the five bits (αζ, βη, εζ, εη all nonempty; and δγ ∨ ζη) on the BRIDGE-FAIL set — the stuck colorings
n ≤ 22 in frame where bridge-then-middle fails (Elie 5608: 1,211), regenerated here with Elie's own program
function (MF.program, BRIDGE, MIDDLE from toy 5611/5608) so the population is his; the bits by my rank
instrument. Pre-score (Cal): if the condition holds on the bridge-fail set too, the far-chain derivation may
cite only Lemma T and the bridge words; if it fails there, the derivation MUST use a non-bridge word's failure.
Also: which of the 1,211 are in the 49 locked (n ≤ 22), and the far-bit pattern on the bridge-fail-but-unlocked.
Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, json, os, sys, time, glob
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname)); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
LF = load("t5614", "toy_5614_SEP2_GRACE_LANE_F_type_table_eight_chain_intersection_matrix_in_frame_census.py")
H = load("t5611g", glob.glob(os.path.join(HERE, "toy_5611_*.py"))[0].split('/')[-1])
MF, EA, OF, E1, IF, BRIDGE, MIDDLE = H.MF, H.EA, H.OF, H.E1, H.IF, H.BRIDGE, H.MIDDLE
L = LF.LETTERS; PAIRS = [(L[i], L[j]) for i in range(8) for j in range(i + 1, 8)]
FREE = [PAIRS.index(p) for p in (('alpha','zeta'),('beta','eta'),('eps','zeta'),('eps','eta'),('gamma','delta'),('zeta','eta'))]
if __name__ == "__main__":
    t0 = time.time(); ns = [int(x) for x in sys.argv[1:]] or list(range(12, 23))
    locked49 = set()
    for fn in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json'):
        for x in json.load(open(os.path.join(HERE, fn))): locked49.add((x['n'], x['graph_index_plantri_c5'], x['v'], tuple(x['coloring_mod_S4_sorted_order'])))
    print("=" * 72); print(f"Toy 5621 — Grace — five bits on the bridge-fail set, n = {ns}"); print("=" * 72, flush=True)
    recs = []
    for n in ns:
        tn = time.time(); k = 0
        for gi, adj in enumerate(EA.plantri_graphs(n, flags=('-c5',))):
            faces, ok = OF.faces_of(adj)
            for v in adj:
                if len(adj[v]) != 5: continue
                order = sorted(u for u in adj if u != v); pos = {u: i for i, u in enumerate(order)}
                sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}; lcyc = E1.link_cycle(faces, v)
                for ct in EA.all_colorings_mod_s4(sub, order):
                    c0 = {u: ct[pos[u]] for u in order}
                    if not IF.stuck(adj, v, c0): continue
                    if MF.program(adj, v, lcyc, c0, BRIDGE, MIDDLE) != 'FAIL': continue
                    R, S = G.roles(c0, lcyc); ch = LF.eight_chains(adj, c0, v, R, S); tb, ts = LF.type_of(ch); a = tuple(tb[i] for i in FREE)
                    recs.append({'n': n, 'gi': gi, 'v': v, 'col': list(ct), 'free6': a, 'far4': a[:4], 'fifth': int(a[4] or a[5]), 'locked': (n, gi, v, tuple(ct)) in locked49}); k += 1
        print(f"  n={n}: bridge-fail {k}  [{time.time()-tn:.0f}s / {time.time()-t0:.0f}s]", flush=True)
    hh = hashlib.sha256(json.dumps([json.dumps(r, sort_keys=True) for r in recs]).encode()).hexdigest()
    print(f"\n  bridge-fail set regenerated: {len(recs)} (5608: 1,211); hashed BEFORE counts {hh[:32]}…")
    far = sum(1 for r in recs if r['far4'] == (1, 1, 1, 1)); fifth = sum(r['fifth'] for r in recs); both = sum(1 for r in recs if r['far4'] == (1, 1, 1, 1) and r['fifth'])
    lk = [r for r in recs if r['locked']]; ul = [r for r in recs if not r['locked']]
    print(f"[DECISIVE TEST] far-chain (αζ,βη,εζ,εη)=1111 on the bridge-fail set: {far}/{len(recs)}; fifth bit (δγ∨ζη): {fifth}/{len(recs)}; all five: {both}/{len(recs)}")
    print(f"  of which locked (in the 49): {len(lk)} — far {sum(1 for r in lk if r['far4']==(1,1,1,1))}/{len(lk)}; bridge-fail but UNLOCKED: {len(ul)} — far {sum(1 for r in ul if r['far4']==(1,1,1,1))}/{len(ul)}, fifth {sum(r['fifth'] for r in ul)}/{len(ul)}")
    print(f"  free-6 words on the bridge-fail set: {dict(Counter(''.join(map(str,r['free6'])) for r in recs))}")
    json.dump({'hash': hh, 'records': recs}, open(os.path.join(HERE, '.out_5621.json'), 'w'))
    print(f"\n  written .out_5621.json [{time.time()-t0:.0f}s]")
