"""
Toy 5625 — Grace — Round 104: THE UNRESTRICTED KEMPE DEPTH on all 349 locks (second instrument beside Elie).
Breadth-first over PLAIN Kempe swaps — any seed vertex u of T−v, any colour pair (a,b) with c(u) ∈ {a,b}, swap the
(a,b)-chain of u — from the lock c₀ to the first coloring in the GATE PHASE (a colour absent at v's link, or τ_v ≤ 5).
No menu, no roles, no commutator: the depth is the plain Kempe distance to the gate. States are colorings of T−v
(raw, not mod S₄ — a swap is a relabeling only when the chain is the whole world, which never reaches the gate
alone); visited set on exact colorings. Reported: depth distribution and maximum per n; the number of states
expanded; the gate coloring's τ re-verified by the rank instrument (own τ) — the search uses BFS chains for speed,
the terminal claim is checked by rank. Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, itertools, json, os, time, glob
from collections import Counter, deque
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname)); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
M = load("t5600gd", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1]); EA, G5 = M.EA, M.G5
PAIRS = list(itertools.combinations(range(4), 2))
def gate(adj, c, v):
    return len({c[u] for u in adj[v]}) < 4 or G5.operational_tau(adj, c, v) <= 5
def depth_to_gate(adj, c0, v, cap_states=300000):
    key0 = tuple(sorted(c0.items())); seen = {key0}; q = deque([(c0, 0)]); expanded = 0
    while q:
        c, d = q.popleft(); expanded += 1
        if expanded > cap_states: return None, expanded, None
        for u in adj:
            if u == v: continue
            for (a, b) in PAIRS:
                if c[u] not in (a, b): continue
                ch = G5.kempe_chain(adj, c, u, a, b, exclude={v}); c2 = G5.do_swap(c, ch, a, b); k2 = tuple(sorted(c2.items()))
                if k2 in seen: continue
                seen.add(k2)
                if gate(adj, c2, v): return d + 1, expanded, c2
                q.append((c2, d + 1))
    return None, expanded, None
if __name__ == "__main__":
    t0 = time.time()
    files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78), ('.in_frame_256_two_word_locked_n24.json', 122)]
    W = []
    for fn, base in files:
        for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))): W.append((x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], f"FCW-{base+k:03d}"))
    print("=" * 72); print(f"Toy 5625 — Grace — unrestricted Kempe depth to the gate on {len(W)} locks"); print("=" * 72, flush=True)
    cache = {}; recs = []
    for (n, gi, v, ct, fid) in W:
        if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
        adj = cache[n][gi]; order = sorted(u for u in adj if u != v); c0 = {u: ct[k] for k, u in enumerate(order)}
        assert G.tau_rank(adj, c0, v) == 6 and not G.insertable(adj, c0, v)
        d, ex, cg = depth_to_gate(adj, c0, v)
        ver = None if cg is None else (G.insertable(adj, cg, v) or G.tau_rank(adj, cg, v) <= 5)
        recs.append({'id': fid, 'n': n, 'depth': d, 'expanded': ex, 'gate_verified_by_rank': ver})
    hh = hashlib.sha256(json.dumps(recs, sort_keys=True).encode()).hexdigest()
    print(f"\n  hashed BEFORE counts {hh[:32]}… [{time.time()-t0:.0f}s]")
    print(f"[UNRESTRICTED DEPTH, all 349] {dict(sorted(Counter(r['depth'] for r in recs).items(), key=lambda x: str(x[0])))}; max {max(r['depth'] for r in recs if r['depth'] is not None)}; unreached {sum(1 for r in recs if r['depth'] is None)}; gate verified by rank {sum(1 for r in recs if r['gate_verified_by_rank'])}/{len(recs)}")
    for n in sorted(set(r['n'] for r in recs)):
        rr = [r for r in recs if r['n'] == n]; print(f"    n={n}: {dict(sorted(Counter(r['depth'] for r in rr).items(), key=lambda x: str(x[0])))}; states expanded median {sorted(r['expanded'] for r in rr)[len(rr)//2]}")
    json.dump({'hash': hh, 'records': recs}, open(os.path.join(HERE, '.out_5625.json'), 'w'))
    print(f"\n  written .out_5625.json [{time.time()-t0:.0f}s]")
