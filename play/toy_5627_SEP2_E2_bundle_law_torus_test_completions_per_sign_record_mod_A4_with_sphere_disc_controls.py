#!/usr/bin/env python3
"""
Toy 5627 — E2 (Round 106): THE BUNDLE LAW'S TORUS TEST.
Grace, 2026-09-02. Instrument only; Lyra pre-registers the predicted group.

Question (Keeper's wake prompt §4 E2): T2574 Lemma R says the Heawood face-sign record
determines a proper 4-coloring of an oriented SPHERE triangulation up to A4 (order 12),
and "off the sphere the reconstruction acquires H^1(.;Z3) monodromy".  On the TORUS, how
many completions does one sign record have, mod A4?

Conventions (pinned to toy 5518 face_sign and Lyra's GF(2) doc, 08-30):
  colors in {0,1,2,3} = GF(2)^2; edge label l(uv) = c(u) XOR c(v) in {1,2,3};
  face (u,v,w) listed COUNTERCLOCKWISE; sign z_t = +1 iff (l(uv), l(vw), l(wu)) is a cyclic
  rotation of (1,2,3), else -1.  Record = tuple of z_t over the faces in the map's face order.
  A4 = the 12 EVEN permutations of the four colors (the sign-preserving color group).
  Heawood closure at v: sum of z_t over faces at v == 0 (mod 3).

Populations:
  SPHERE control  : all triangulations on n = 6..10 vertices from plantri 5.8 (-u).
  DISC control    : FCW-014, the 19-vertex disc(2) with its pinning; twins A and B.
  TORUS           : all triangulations on n = 7..10 vertices, generated as the flip closure
                    from the unique 7-vertex torus (Mobius torus) + one-vertex face insertion
                    per level.  Generator positive control: Lutz's counts 1, 7, 112, 2109
                    (quoted from memory — the run prints what it finds; a mismatch is a
                    generator defect, reported as such).

Measured per (surface, triangulation, record):
  N(record) = number of proper 4-colorings with that record; orbits = N/12 after checking
  A4 acts freely and preserves the record.
Monodromy footprint on the record space (n = 8, 9 tori and spheres, exhaustive 2^F):
  closed records (Heawood closure at every vertex) split into
     realized  /  Z3-obstructed (label propagation has nontrivial holonomy on some dual
     non-tree edge)  /  V-obstructed (labels globally consistent but colors do not close).
  On the sphere: closed == realized is the Lemma R positive control.

Blind protocol: torus per-record counts are written to play/.e2_torus_counts_5627.json and
their sha256 printed; the headline stays in that file until Lyra's prediction is on the board.
"""
import sys, os, json, hashlib, subprocess, itertools, time
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PLANTRI = os.path.join(HERE, 'tools', 'plantri58', 'plantri')
T0 = time.time()

# ---------------------------------------------------------------- maps as oriented face lists
def edges_of(faces):
    E = defaultdict(list)
    for t in faces:
        u, v, w = t
        for a, b in ((u, v), (v, w), (w, u)):
            E[frozenset((a, b))].append((a, b))
    return E

def check_closed_oriented(faces):
    """Every edge in exactly two faces, once in each direction; no loops; no multi-edges."""
    E = edges_of(faces)
    for e, darts in E.items():
        if len(e) != 2: return False
        if len(darts) != 2: return False
        (a, b), (c, d) = darts
        if not (a == d and b == c): return False
    return True

def adjacency(faces):
    adj = defaultdict(set)
    for u, v, w in faces:
        adj[u].update((v, w)); adj[v].update((u, w)); adj[w].update((u, v))
    return adj

def rotation_system(faces):
    """ccw cyclic neighbour order at each vertex from ccw faces: face (v,a,b) => a then b."""
    nxt = defaultdict(dict)
    for u, v, w in faces:
        nxt[u][v] = w; nxt[v][w] = u; nxt[w][u] = v
    rot = {}
    for v, m in nxt.items():
        start = next(iter(m)); cyc = [start]; x = m[start]
        while x != start:
            cyc.append(x); x = m[x]
        assert len(cyc) == len(m), "rotation at vertex not a single cycle"
        rot[v] = cyc
    return rot

def faces_from_rotation(rot):
    """faces to the LEFT of darts, given ccw rotation: from dart (u,v) next is (v, pred_v(u))."""
    pos = {v: {w: i for i, w in enumerate(c)} for v, c in rot.items()}
    seen = set(); faces = []
    for u in rot:
        for v in rot[u]:
            if (u, v) in seen: continue
            f = []; a, b = u, v
            while (a, b) not in seen:
                seen.add((a, b)); f.append(a)
                c = rot[b][(pos[b][a] - 1) % len(rot[b])]
                a, b = b, c
            faces.append(tuple(f))
    return faces

def canon(faces):
    """Canonical string of the oriented map up to relabelling AND reflection."""
    rot = rotation_system(faces)
    best = None
    for mirror in (False, True):
        R = {v: (c[::-1] if mirror else c) for v, c in rot.items()}
        pos = {v: {w: i for i, w in enumerate(c)} for v, c in R.items()}
        for u in R:
            for v0 in R[u]:
                lab = {u: 0}; order = [u]; entry = {u: v0}; code = []
                i = 0
                while i < len(order):
                    x = order[i]; i += 1
                    c = R[x]; k = pos[x][entry[x]]
                    seq = [c[(k + j) % len(c)] for j in range(len(c))]
                    for y in seq:
                        if y not in lab:
                            lab[y] = len(order); order.append(y); entry[y] = x
                        code.append(lab[y])
                    code.append(-1)
                s = tuple(code)
                if best is None or s < best: best = s
    return best

def flip(faces, e):
    """Flip edge e=frozenset({u,v}); return new face list or None if it creates a multi-edge."""
    u, v = tuple(e)
    fs = [t for t in faces if u in t and v in t]
    if len(fs) != 2: return None
    # orient: one face has dart (u,v), other has (v,u)
    def third(t, a, b):
        return [x for x in t if x not in (a, b)][0]
    t1 = [t for t in fs if any(t[i] == u and t[(i + 1) % 3] == v for i in range(3))][0]
    t2 = [t for t in fs if t is not t1][0]
    w = third(t1, u, v); x = third(t2, u, v)
    if w == x: return None
    adj = adjacency(faces)
    if x in adj[w]: return None            # would create a double edge
    new = [t for t in faces if t is not t1 and t is not t2]
    new.append((w, u, x)); new.append((x, v, w))
    return new

def insert_vertex(faces, t, newv):
    u, v, w = t
    new = [f for f in faces if f is not t]
    new += [(u, v, newv), (v, w, newv), (w, u, newv)]
    return new

# ---------------------------------------------------------------- torus generator
def mobius_torus7():
    faces = []
    for i in range(7):
        faces.append((i, (i + 1) % 7, (i + 3) % 7))
        faces.append((i, (i + 3) % 7, (i + 2) % 7))
    if not check_closed_oriented(faces):
        # try the other orientation of the second family
        faces = []
        for i in range(7):
            faces.append((i, (i + 1) % 7, (i + 3) % 7))
            faces.append((i, (i + 2) % 7, (i + 3) % 7))
    assert check_closed_oriented(faces), "7-vertex torus not closed/oriented"
    V = 7; E = len(edges_of(faces)); F = len(faces)
    assert V - E + F == 0, (V, E, F)
    return faces

def flip_closure(seed_faces):
    """All triangulations reachable by flips from the seed, keyed by canonical form."""
    reps = {}
    key = canon(seed_faces); reps[key] = seed_faces; frontier = [seed_faces]
    while frontier:
        nf = []
        for faces in frontier:
            for e in list(edges_of(faces).keys()):
                g = flip(faces, e)
                if g is None: continue
                k = canon(g)
                if k not in reps:
                    reps[k] = g; nf.append(g)
        frontier = nf
    return reps

def torus_family(nmax):
    fam = {7: flip_closure(mobius_torus7())}
    for n in range(8, nmax + 1):
        seeds = {}
        for faces in fam[n - 1].values():
            g = insert_vertex(faces, faces[0], n - 1)
            seeds[canon(g)] = g
        reps = {}
        for g in seeds.values():
            if canon(g) in reps: continue
            reps.update(flip_closure(g))
        fam[n] = reps
    return fam

# ---------------------------------------------------------------- sphere from plantri
def plantri_triangulations(n):
    out = subprocess.run([PLANTRI, str(n)], capture_output=True).stdout
    assert out.startswith(b'>>planar_code<<'), out[:40]
    data = out[len(b'>>planar_code<<'):]
    i = 0; graphs = []
    while i < len(data):
        nv = data[i]; i += 1
        rot = {}
        for v in range(nv):
            nb = []
            while data[i] != 0:
                nb.append(data[i] - 1); i += 1
            i += 1
            rot[v] = nb
        faces = faces_from_rotation(rot)
        if not all(len(f) == 3 for f in faces):
            rot = {v: c[::-1] for v, c in rot.items()}
            faces = faces_from_rotation(rot)
        assert all(len(f) == 3 for f in faces)
        assert check_closed_oriented(faces)
        graphs.append(faces)
    return graphs

# ---------------------------------------------------------------- colorings, records, A4
def all_4colorings(adj, n, pinned=None):
    verts = sorted(adj, key=lambda v: -len(adj[v]))
    col = dict(pinned or {})
    free = [v for v in verts if v not in col]
    out = []
    def rec(i):
        if i == len(free):
            out.append(dict(col)); return
        v = free[i]
        used = {col[w] for w in adj[v] if w in col}
        for c in range(4):
            if c not in used:
                col[v] = c; rec(i + 1); del col[v]
    rec(0)
    return out

def face_sign(t, col):
    u, v, w = t
    l1 = col[u] ^ col[v]; l2 = col[v] ^ col[w]; l3 = col[w] ^ col[u]
    assert {l1, l2, l3} == {1, 2, 3}
    return 1 if (l1, l2, l3) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else -1

def record(faces, col):
    return tuple(face_sign(t, col) for t in faces)

A4 = [p for p in itertools.permutations(range(4))
      if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
assert len(A4) == 12

def heawood_closed(faces, rec_):
    s = defaultdict(int)
    for t, z in zip(faces, rec_):
        for v in t: s[v] += z
    return all(x % 3 == 0 for x in s.values())

def per_record(faces, adj, n):
    cols = all_4colorings(adj, n)
    groups = defaultdict(list)
    for c in cols:
        groups[record(faces, c)].append(c)
    # A4 free + record-preserving check on every coloring
    for r, cs in groups.items():
        assert heawood_closed(faces, r)
        for c in cs:
            imgs = set()
            for p in A4:
                d = {v: p[c[v]] for v in c}
                assert record(faces, d) == r
                imgs.add(tuple(sorted(d.items())))
            assert len(imgs) == 12
        assert len(cs) % 12 == 0
    return cols, {r: len(cs) // 12 for r, cs in groups.items()}

# ---------------------------------------------------------------- record-space footprint
ROT = {1: 2, 2: 3, 3: 1}   # label rotation a->b->c->a  (1->2->3->1)

def propagate_labels(faces, rec_):
    """Given a sign record, propagate edge labels from one seed edge over a dual spanning tree.
    Returns (labels or None, z3_obstructed: bool).  Holonomy on a non-tree dual edge is a power
    of ROT; obstruction = the propagated label of the shared edge disagrees."""
    E = edges_of(faces)
    face_of_dart = {}
    for i, t in enumerate(faces):
        u, v, w = t
        for a, b in ((u, v), (v, w), (w, u)): face_of_dart[(a, b)] = i
    lab = {}
    def fill(i, e, l):
        """face i has edge e with label l; fill its other two edges from the sign."""
        u, v, w = faces[i]; z = rec_[i]
        darts = [(u, v), (v, w), (w, u)]
        k = [j for j, d in enumerate(darts) if frozenset(d) == e][0]
        order = (1, 2, 3) if z == 1 else (1, 3, 2)
        # the cyclic order of labels around the face is `order` up to rotation; place l at k
        seq = list(order); s = seq.index(l)
        out = {}
        for j in range(3):
            out[frozenset(darts[(k + j) % 3])] = seq[(s + j) % 3]
        return out
    # seed
    t0 = faces[0]; e0 = frozenset((t0[0], t0[1]))
    lab[e0] = 1
    visited = {0}; stack = [0]
    pending = {e0: 0}
    obstructed = False
    while stack:
        i = stack.pop()
        # find one labelled edge of face i
        u, v, w = faces[i]
        es = [frozenset(d) for d in ((u, v), (v, w), (w, u))]
        known = [e for e in es if e in lab]
        got = fill(i, known[0], lab[known[0]])
        for e, l in got.items():
            if e in lab:
                if lab[e] != l: obstructed = True
            else:
                lab[e] = l
        for e in es:
            (a, b), (c, d) = E[e]
            for dart in ((a, b), (c, d)):
                j = face_of_dart[dart]
                if j not in visited:
                    visited.add(j); stack.append(j)
    # final consistency over all faces
    for i, t in enumerate(faces):
        u, v, w = t
        l1, l2, l3 = lab[frozenset((u, v))], lab[frozenset((v, w))], lab[frozenset((w, u))]
        if {l1, l2, l3} != {1, 2, 3}: obstructed = True; continue
        z = 1 if (l1, l2, l3) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else -1
        if z != rec_[i]: obstructed = True
    return (None if obstructed else lab), obstructed

def colors_from_labels(adj, lab, n):
    col = {0: 0}; stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            c = col[u] ^ lab[frozenset((u, v))]
            if v in col:
                if col[v] != c: return None
            else:
                col[v] = c; stack.append(v)
    return col

def footprint(faces, adj, n, realized):
    F = len(faces)
    closed = z3 = vobs = real = 0
    for bits in range(1 << F):
        r = tuple(1 if (bits >> i) & 1 else -1 for i in range(F))
        if not heawood_closed(faces, r): continue
        closed += 1
        lab, obs = propagate_labels(faces, r)
        if obs: z3 += 1; continue
        col = colors_from_labels(adj, lab, n)
        if col is None: vobs += 1; continue
        real += 1
        assert r in realized, "reconstructed a record not in the coloring census"
    return dict(F=F, closed=closed, z3_obstructed=z3, V_obstructed=vobs, realized=real,
                realized_census=len(realized))

# ---------------------------------------------------------------- disc control (FCW-014)
def disc(radius):
    pts = [(q, r) for q in range(-radius, radius + 1) for r in range(-radius, radius + 1)
           if abs(q + r) <= radius]
    pset = set(pts)
    dirs = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    adj = {p: set() for p in pts}
    for p in pts:
        for d in dirs:
            q = (p[0] + d[0], p[1] + d[1])
            if q in pset: adj[p].add(q)
    faces = []
    for p in pts:
        for (d1, d2) in (((1, 0), (0, 1)), ((0, 1), (-1, 1))):   # two ccw up-triangles per point
            a = (p[0] + d1[0], p[1] + d1[1]); b = (p[0] + d2[0], p[1] + d2[1])
            if a in pset and b in pset: faces.append((p, a, b))
    return pts, adj, faces

def disc_control():
    pts, adj, faces = disc(2)
    gal = json.load(open(os.path.join(HERE, '..', 'data', 'fourcolor_witness_gallery.json')))
    ws = gal['witnesses'] if isinstance(gal, dict) else gal
    w = [x for x in ws if x['id'] == 'FCW-014'][0]
    A = {tuple(map(int, k.strip('()').split(','))): v for k, v in w['graph']['frozen_completion_A'].items()}
    B = {tuple(map(int, k.strip('()').split(','))): v for k, v in w['graph']['frozen_completion_B'].items()}
    for col in (A, B):
        for u in adj:
            for v in adj[u]: assert col[u] != col[v]
    # orientation check on the disc faces (axial (1,0),(0,1) is ccw in the standard embedding)
    E = edges_of(faces)
    for e, darts in E.items():
        assert len(darts) in (1, 2)
        if len(darts) == 2:
            (a, b), (c, d) = darts; assert a == d and b == c
    boundary = [p for p in pts if len(adj[p]) < 6]
    pin = {p: A[p] for p in boundary}
    assert all(A[p] == B[p] for p in boundary)
    comps = all_4colorings(adj, len(pts), pinned=pin)
    rA, rB = record(faces, A), record(faces, B)
    same = (rA == rB)
    related = any(all(p[A[v]] == B[v] for v in A) for p in A4)
    return dict(vertices=len(pts), faces=len(faces), completions_under_pinning=len(comps),
                twins_same_record=same, twins_A4_related=related,
                records_among_completions=len({record(faces, c) for c in comps}),
                heawood_closed_A=heawood_closed(faces, rA), heawood_closed_B=heawood_closed(faces, rB))


# ---------------------------------------------------------------- Mohar-Salas T(a,b) tori (Eulerian)
def ms_torus(a, b):
    """Triangular-lattice torus Z^2/<(a,0),(0,b)>, edges (1,0),(0,1),(1,1); ccw faces."""
    faces = []
    for x in range(a):
        for y in range(b):
            p = (x, y); q = ((x + 1) % a, y); r = ((x + 1) % a, (y + 1) % b); s_ = (x, (y + 1) % b)
            faces.append((p, q, r)); faces.append((p, r, s_))
    idx = {}
    for t in faces:
        for v in t: idx.setdefault(v, len(idx))
    faces = [tuple(idx[v] for v in t) for t in faces]
    assert check_closed_oriented(faces), f"T({a},{b}) not simplicial/oriented"
    assert len(idx) - len(edges_of(faces)) + len(faces) == 0
    return faces, len(idx)

def ms_main(pairs):
    out = {}
    for a, b in pairs:
        faces, n = ms_torus(a, b)
        adj = adjacency(faces)
        degs = Counter(len(adj[v]) for v in adj)
        cols, orb = per_record(faces, adj, n)
        h = Counter(orb.values())
        rec = dict(vertices=n, faces=len(faces), degrees=dict(degs), colorings=len(cols),
                   records=len(orb), orbits_hist=dict(h), canon_in_flip_family=None)
        if n <= 10:
            fam = torus_family(n)
            rec['canon_in_flip_family'] = canon(faces) in fam[n]
        if len(faces) <= 20:
            rec['footprint'] = footprint(faces, adj, n, set(orb))
        out[f"T({a},{b})"] = rec
        print(f"  T({a},{b}): n={n} F={len(faces)} degrees={dict(degs)} colorings={len(cols)} "
              f"records={len(orb)} orbits-per-record {dict(h)} "
              f"{'footprint='+str(rec.get('footprint')) if 'footprint' in rec else ''} "
              f"in-flip-family={rec['canon_in_flip_family']}   [{time.time()-T0:.0f}s]")
    path = os.path.join(HERE, '.e2_mohar_salas_counts_5627.json')
    s = json.dumps(out, sort_keys=True, indent=1, default=str)
    open(path, 'w').write(s)
    print("written", path, "sha256", hashlib.sha256(s.encode()).hexdigest()[:16])

# ---------------------------------------------------------------- main
def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'ms':
        print('Toy 5627 — Mohar-Salas T(a,b) population')
        ms_main([(3, 3), (6, 3), (3, 6), (9, 3), (12, 3)]); return
    NMAX_T = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    NMAX_S = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print("Toy 5627 — E2 torus test.  A4 order", len(A4))

    # ---- sphere control
    print("\n[SPHERE control, plantri -u]")
    sphere_hist = Counter(); sphere_tri = 0; sphere_records = 0
    sphere_by_n = {}
    for n in range(6, NMAX_S + 1):
        tris = plantri_triangulations(n)
        h = Counter(); nrec = 0
        for faces in tris:
            adj = adjacency(faces)
            cols, orb = per_record(faces, adj, n)
            h.update(orb.values()); nrec += len(orb)
        sphere_by_n[n] = dict(triangulations=len(tris), records=nrec, orbits_hist=dict(h))
        print(f"  n={n:2d}: {len(tris):4d} triangulations, {nrec:6d} realized records, "
              f"orbits-per-record histogram {dict(h)}   [{time.time()-T0:.0f}s]")
        sphere_hist.update(h); sphere_tri += len(tris); sphere_records += nrec
    # footprint on small spheres
    sph_fp = {}
    for n in (6, 7, 8):
        faces = plantri_triangulations(n)[0]; adj = adjacency(faces)
        cols, orb = per_record(faces, adj, n)
        sph_fp[n] = footprint(faces, adj, n, set(orb))
        print(f"  record-space footprint sphere n={n}: {sph_fp[n]}")

    # ---- disc control
    print("\n[DISC control, FCW-014]")
    dc = disc_control(); print(" ", dc)

    # ---- torus
    print("\n[TORUS, flip closure from the 7-vertex torus]")
    fam = torus_family(NMAX_T)
    lutz = {7: 1, 8: 7, 9: 112, 10: 2109, 11: 37867}
    torus_by_n = {}; torus_counts = {}
    for n in sorted(fam):
        reps = fam[n]
        h = Counter(); nrec = 0; colorable = 0; per_tri = []
        for k, faces in reps.items():
            assert check_closed_oriented(faces)
            V = n; E = len(edges_of(faces)); Fc = len(faces)
            assert V - E + Fc == 0
            adj = adjacency(faces)
            cols, orb = per_record(faces, adj, n)
            if cols: colorable += 1
            h.update(orb.values()); nrec += len(orb)
            per_tri.append(dict(colorings=len(cols), records=len(orb),
                                orbits_hist=dict(Counter(orb.values()))))
        torus_by_n[n] = dict(triangulations=len(reps), lutz_from_memory=lutz.get(n),
                             colorable=colorable, records=nrec, orbits_hist=dict(h))
        torus_counts[n] = per_tri
        print(f"  n={n:2d}: {len(reps):5d} triangulations (Lutz from memory {lutz.get(n)}), "
              f"{colorable} 4-colorable, {nrec} realized records, "
              f"orbits-per-record histogram {dict(h)}   [{time.time()-T0:.0f}s]")
    tor_fp = {}
    for n in (8, 9):
        for k, faces in fam[n].items():
            adj = adjacency(faces)
            cols, orb = per_record(faces, adj, n)
            if cols:
                tor_fp[n] = footprint(faces, adj, n, set(orb))
                print(f"  record-space footprint torus n={n} (first colorable rep): {tor_fp[n]}")
                break

    out = dict(toy=5627, sphere=sphere_by_n, sphere_footprint=sph_fp, disc=dc,
               torus=torus_by_n, torus_footprint=tor_fp, torus_per_triangulation=torus_counts,
               seconds=round(time.time() - T0, 1))
    path = os.path.join(HERE, '.e2_torus_counts_5627.json')
    s = json.dumps(out, sort_keys=True, indent=1, default=str)
    open(path, 'w').write(s)
    print("\nwritten", path, "sha256", hashlib.sha256(s.encode()).hexdigest()[:16],
          f"[{time.time()-T0:.0f}s]")

if __name__ == '__main__':
    main()
