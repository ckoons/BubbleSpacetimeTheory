#!/usr/bin/env python3
"""
Toy 5630 — Casey's second shot (Keeper 15:08 (2)): "observers stack; each layer's substrate is the record
the next observer discriminates" = a TOWER OF COVERS.  Grace, 2026-09-02.

Toy 5629 tested lattice covers of the lattice torus T(3,3), where the covers are read off.  Here the cover
is BUILT FROM THE HOLONOMY ITSELF on tori that are NOT lattice quotients (the flip-family tori of toy 5627,
n = 8, 9 exhaustive; n = 10 a fixed prefix), so nothing is read off:
  floor 0: the torus with a Heawood-closed orphan record r.
  floor 1 (transport orphans): the Z3 transport holonomy theta: H1 -> Z3 is evaluated on the fundamental
           cycles of a spanning tree by propagating labels along the FATTENED dual walk of each primal cycle;
           the voltages define the derived 3-sheet cover (an unbranched SURFACE cover: faces lift because the
           voltages close around every face — asserted, not assumed).  The lifted record is re-classified.
  floor 2 (whatever is still a cocycle orphan on floor 1, and the floor-0 cocycle orphans directly): the
           V = Z2^2 label holonomy on the fundamental cycles gives voltages in V; the derived cover has
           |image| in {2, 4} sheets.  Realization on it is then checked, not assumed.
Construction-guaranteed parts (a derived cover trivializes its own holonomy) are stated as such; the
NON-guaranteed measurements are: (a) every derived cover is a closed oriented simplicial torus (Euler 0,
no multi-edges); (b) the voltage cocycle closes on every face (validates the fattened-walk holonomy);
(c) the FLOOR-2 OCCUPANCY: what fraction of transport orphans, once transported, are still cocycle-
obstructed (on T(3,3) toy 5629 found NONE — is that general?); (d) the sheet count distribution
{2, 3, 4, 6, 12}; (e) a lattice control: T(3,3) through THIS code must reproduce 5629 (transport orphans
realized at 3 sheets, cocycle orphans at 4 — or fewer if a diagonal 2-sheet cover exists, which 5629 did
not test).
"""
import os, sys, json, time, itertools
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
t = importlib.import_module('toy_5627_SEP2_E2_bundle_law_torus_test_completions_per_sign_record_mod_A4_with_sphere_disc_controls')
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()

ROT = {1: 2, 2: 3, 3: 1}

def classify(faces, adj, n, rec):
    lab, obs = t.propagate_labels(faces, rec)
    if obs: return 'transport', None
    col = t.colors_from_labels(adj, lab, n)
    return ('realized' if col is not None else 'cocycle'), lab

def spanning_tree(adj, root=0):
    parent = {root: None}; order = [root]; i = 0
    while i < len(order):
        u = order[i]; i += 1
        for v in sorted(adj[u]):
            if v not in parent: parent[v] = u; order.append(v)
    return parent

def tree_path(parent, u):
    p = [u]
    while parent[p[-1]] is not None: p.append(parent[p[-1]])
    return p                      # u ... root

def cycle_from(parent, u, v):
    pu, pv = tree_path(parent, u), tree_path(parent, v)
    su = set(pu); k = next(i for i, x in enumerate(pv) if x in su); lca = pv[k]
    a = pu[:pu.index(lca)]          # u ... (before lca)
    b = pv[:k]                       # v ... (before lca)
    return a + [lca] + b[::-1]       # u -> ... -> lca -> ... -> v  (then edge v->u closes)

def face_index(faces):
    fi = {}
    for i, f in enumerate(faces): fi[frozenset(f)] = i
    return fi

def fattened_dual_walk(faces, rot, cyc):
    """cyc = [v0..v_{m-1}] closed primal walk (edge v_{m-1}->v0 closes). Returns face indices along the
    left-hand fattening: at v_i walk ccw from neighbour v_{i-1} to v_{i+1}."""
    fi = face_index(faces); m = len(cyc); walk = []
    for i in range(m):
        v = cyc[i]; prev = cyc[(i - 1) % m]; nxt = cyc[(i + 1) % m]
        r = rot[v]; p = r.index(prev); q = r.index(nxt)
        j = p
        while True:
            a, b = r[j % len(r)], r[(j + 1) % len(r)]
            walk.append(fi[frozenset((v, a, b))])
            j += 1
            if (j % len(r)) == q: break
    return walk

def holonomy_z3(faces, rec, walk):
    """propagate one label around the closed dual walk; return k with l_end = ROT^k(l_start)."""
    def fill(i, e, l):
        u, v, w = faces[i]; z = rec[i]
        darts = [(u, v), (v, w), (w, u)]
        k = [j for j, d in enumerate(darts) if frozenset(d) == e][0]
        seq = list((1, 2, 3) if z == 1 else (1, 3, 2)); s = seq.index(l)
        return {frozenset(darts[(k + j) % 3]): seq[(s + j) % 3] for j in range(3)}
    # shared edge between consecutive faces
    def shared(i, j):
        s = frozenset(faces[i]) & frozenset(faces[j]); assert len(s) == 2, (faces[i], faces[j]); return s
    W = [w for k, w in enumerate(walk) if k == 0 or w != walk[k - 1]]
    while len(W) > 1 and W[-1] == W[0]: W.pop()
    if len(W) == 1: return 0
    e0 = shared(W[-1], W[0]); l = 1; e = e0
    for k in range(len(W)):
        i = W[k]; j = W[(k + 1) % len(W)]
        got = fill(i, e, l); e = shared(i, j); l = got[e]
    # now l is the label of e0 after transport
    k = 0; x = 1
    while x != l: x = ROT[x]; k += 1
    return k

def derived_cover(faces, volt, group_elems, add):
    """volt: dict dart (u,v) -> group element (antisymmetric); cover vertices (v, g)."""
    new = []
    for (u, v, w) in faces:
        for g in group_elems:
            g1 = add(g, volt[(u, v)]); g2 = add(g1, volt[(v, w)])
            assert add(g2, volt[(w, u)]) == g, "voltage does not close on a face"
            new.append(((u, g), (v, g1), (w, g2)))
    idx = {}
    for f in new:
        for x in f: idx.setdefault(x, len(idx))
    newi = [tuple(idx[x] for x in f) for f in new]
    assert t.check_closed_oriented(newi), "cover not a closed oriented simplicial surface"
    V = len(idx); E = len(t.edges_of(newi)); F = len(newi)
    assert V - E + F == 0, "cover is not a torus"
    lifted_from = [faces.index((u, v, w)) for (u, v, w) in [tuple(x[0] for x in f) for f in new]]
    return newi, V, lifted_from

def voltages_from_cycle_function(faces, adj, parent, value_on_cycle, zero, neg):
    """tree edges 0; non-tree edge (u,v): value on the fundamental cycle u->...->v->u."""
    volt = {}
    for u in adj:
        for v in adj[u]:
            if parent.get(v) == u or parent.get(u) == v:
                volt[(u, v)] = zero
    for u in adj:
        for v in adj[u]:
            if (u, v) in volt or (v, u) in volt: continue
            cyc = cycle_from(parent, u, v)      # u ... v ; closing edge v->u
            # orient: cycle traversed u->...->v then edge (v,u). Voltage of dart (v,u) = value(cycle)
            val = value_on_cycle(cyc)
            volt[(v, u)] = val; volt[(u, v)] = neg(val)
    return volt

def z3_cover(faces, adj, n, rec):
    rot = t.rotation_system(faces); parent = spanning_tree(adj)
    def val(cyc):   # cyc = u ... v, closing v->u; the closed walk for holonomy: u..v then back to u
        return holonomy_z3(faces, rec, fattened_dual_walk(faces, rot, cyc))
    volt = voltages_from_cycle_function(faces, adj, parent, val, 0, lambda x: (-x) % 3)
    image = sorted({v for v in volt.values()})
    if image == [0]: return None
    cov, V, lifted_from = derived_cover(faces, volt, [0, 1, 2], lambda a, b: (a + b) % 3)
    return cov, V, tuple(rec[i] for i in lifted_from)

def v_cover(faces, adj, n, rec, lab):
    parent = spanning_tree(adj)
    def val(cyc):
        s = 0
        m = len(cyc)
        for i in range(m):
            s ^= lab[frozenset((cyc[i], cyc[(i + 1) % m]))]
        return s
    volt = voltages_from_cycle_function(faces, adj, parent, val, 0, lambda x: x)
    image = {0}
    for v in volt.values():
        image |= {x ^ v for x in image}
    image = sorted(image)
    if image == [0]: return None
    cov, V, lifted_from = derived_cover(faces, volt, image, lambda a, b: a ^ b)
    return cov, V, tuple(rec[i] for i in lifted_from), len(image)

def run_torus(name, faces):
    adj = t.adjacency(faces); n = len(adj); F = len(faces)
    stats = Counter(); sheets = Counter(); floor2 = Counter(); checks = Counter()
    for bits in range(1 << F):
        rec = tuple(1 if (bits >> i) & 1 else -1 for i in range(F))
        if not t.heawood_closed(faces, rec): continue
        kind, lab = classify(faces, adj, n, rec); stats[kind] += 1
        if kind == 'realized': continue
        total = 1; cur_faces, cur_rec, cur_lab, cur_kind = faces, rec, lab, kind
        if kind == 'transport':
            r = z3_cover(faces, adj, n, rec); assert r is not None, "transport orphan with trivial theta"
            cov, V, lrec = r; total *= 3
            cadj = t.adjacency(cov)
            k2, lab2 = classify(cov, cadj, V, lrec)
            checks['floor1_transport_killed'] += (k2 != 'transport')
            assert k2 != 'transport'
            floor2[k2] += 1                      # 'realized' or 'cocycle' after floor 1
            cur_faces, cur_rec, cur_lab, cur_kind = cov, lrec, lab2, k2
        if cur_kind == 'cocycle':
            cadj = t.adjacency(cur_faces)
            r = v_cover(cur_faces, cadj, len(cadj), cur_rec, cur_lab); assert r is not None
            cov, V, lrec, m = r; total *= m
            k3, _ = classify(cov, t.adjacency(cov), V, lrec)
            checks['floor2_realized'] += (k3 == 'realized'); assert k3 == 'realized'
            cur_kind = k3
        sheets[(kind, total)] += 1
    print(f"  {name}: n={n} F={F} closed={sum(stats.values())} {dict(stats)} | after floor 1 (transport orphans): "
          f"{dict(floor2)} | sheets by (kind,total): {dict(sheets)}   [{time.time()-T0:.0f}s]")
    return dict(name=name, n=n, F=F, stats=dict(stats), after_floor1=dict(floor2),
                sheets={f"{k}:{s}": v for (k, s), v in sheets.items()}, checks=dict(checks))

def main():
    out = []
    # lattice control T(3,3) through the derived-cover code
    faces33, _ = t.ms_torus(3, 3)
    print("[control] T(3,3) through derived covers:")
    out.append(run_torus("T(3,3)", faces33))
    print("[flip-family tori, non-lattice]")
    fam = t.torus_family(10)
    done = 0
    ns = (10,) if len(sys.argv) > 1 and sys.argv[1] == 'n10' else (8, 9)
    N10 = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for n in ns:
        k10 = 0
        for key, faces in fam[n].items():
            adj = t.adjacency(faces)
            if not t.all_4colorings(adj, n): continue
            if n == 10 and k10 >= N10: break
            out.append(run_torus(f"flip n={n} #{done}", faces)); done += 1; k10 += 1
    agg = Counter(); agg2 = Counter()
    for r in out[1:]:
        agg.update({k: v for k, v in r['after_floor1'].items()}); agg2.update(r['sheets'])
    print(f"\nNON-LATTICE AGGREGATE: transport orphans after floor 1 -> {dict(agg)};  sheets {dict(agg2)}")
    path = os.path.join(HERE, '.tower_of_covers_5630' + ('_n10' if ns == (10,) else '') + '.json'); json.dump(out, open(path, 'w'), indent=1)
    print("written", path, f"[{time.time()-T0:.0f}s]")
    print("SCORE: PASS — all derived covers closed oriented tori, voltages closed on every face, every orphan realized at its floor")

if __name__ == '__main__':
    main()
