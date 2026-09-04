#!/usr/bin/env python3
"""
Toy 5663 — Round 118 E5. Pre-registration sha256 06205eb4 (written and hashed before this file existed).
On Mohar–Salas tori T(3L,3M): enumerate proper 4-colourings, Kempe classes (mod S4, union-find on canonical reps),
Fisk/Mohar–Salas degree, and OUR height datum (periods of the height cochain, k = 0 so no branched cover).
Controls: octahedron + its 1->4 subdivision (sphere: one Kempe class, deg mod 12 constant).
"""
import sys, time, json, hashlib, itertools
from collections import defaultdict

t0 = time.time(); score = []
def S(label, ok):
    score.append((label, bool(ok))); print(f"    [{'PASS' if ok else 'FAIL'}] {label}", flush=True)

LVEC = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}          # labels a=1,b=2,c=3 -> A,B,C ; colour d=0
# tetrahedron face orientation: face omitting m, oriented cyclic order
TET = {0: (1, 2, 3), 1: (0, 3, 2), 2: (0, 1, 3), 3: (0, 2, 1)}
TET_ROT = {m: {tuple(o[i:] + o[:i]) for i in range(3)} for m, o in TET.items()}

# ------------------------------------------------------------------ surfaces
class Surface:
    """oriented triangulation: nv, adj (lists), faces (CCW triples), sign per face (alternating), left-face sign per directed edge."""
    def __init__(self, nv, faces, name):
        self.name = name; self.nv = nv; self.faces = faces
        adj = [set() for _ in range(nv)]
        left = {}
        for fi, (a, b, c) in enumerate(faces):
            for u, w in ((a, b), (b, c), (c, a)):
                adj[u].add(w); adj[w].add(u); left[(u, w)] = fi
        self.adj = [sorted(s) for s in adj]; self.leftface = left
        # 2-colour the dual (faces adjacent across an edge get opposite signs)
        sign = [0] * len(faces); sign[0] = 1; stack = [0]
        while stack:
            fi = stack.pop()
            a, b, c = faces[fi]
            for u, w in ((a, b), (b, c), (c, a)):
                gj = left[(w, u)]
                if sign[gj] == 0: sign[gj] = -sign[fi]; stack.append(gj)
                elif sign[gj] != -sign[fi]: raise ValueError("dual not bipartite")
        self.fsign = sign
        self.sigma = {e: sign[fi] for e, fi in left.items()}
        self.ne = sum(len(a) for a in self.adj) // 2
    def omega(self, f, u, w):
        s = self.sigma[(u, w)]; L = LVEC[f[u] ^ f[w]]
        return (s * L[0], s * L[1])
    def degree(self, f):
        out = []
        for m in range(4):
            p = n = 0
            for (a, b, c) in self.faces:
                col = (f[a], f[b], f[c])
                if m in col: continue
                if col in TET_ROT[m]: p += 1
                else: n += 1
            out.append(p - n)
        return out
    def face_closure_ok(self, f):
        for (a, b, c) in self.faces:
            s = [0, 0]
            for u, w in ((a, b), (b, c), (c, a)):
                o = self.omega(f, u, w); s[0] += o[0]; s[1] += o[1]
            if s != [0, 0]: return False
        return True

def torus(R, Sy):   # R columns (x), Sy rows (y); vertex id x*Sy + y
    vid = lambda x, y: (x % R) * Sy + (y % Sy)
    faces = []
    for x in range(R):
        for y in range(Sy):
            faces.append((vid(x, y), vid(x + 1, y), vid(x + 1, y + 1)))       # up, CCW
            faces.append((vid(x, y), vid(x + 1, y + 1), vid(x, y + 1)))       # down, CCW
    T = Surface(R * Sy, faces, f"T({R},{Sy})"); T.R = R; T.Sy = Sy; T.vid = vid
    return T

def octahedron():
    import numpy as np
    V = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    faces = []
    for i in (0, 1):
        for j in (2, 3):
            for k in (4, 5):
                a, b, c = np.array(V[i]), np.array(V[j]), np.array(V[k])
                if np.dot(np.cross(b - a, c - a), a + b + c) > 0: faces.append((i, j, k))
                else: faces.append((i, k, j))
    return Surface(6, faces, "octahedron")

def subdivide(Sf):
    """1->4 subdivision with edge midpoints; orientation inherited; all degrees stay even."""
    mid = {}; nv = Sf.nv
    def m(u, w):
        key = (min(u, w), max(u, w))
        nonlocal nv
        if key not in mid: mid[key] = nv; nv += 1
        return mid[key]
    faces = []
    for (a, b, c) in Sf.faces:
        ab, bc, ca = m(a, b), m(b, c), m(c, a)
        faces += [(a, ab, ca), (ab, b, bc), (ca, bc, c), (ab, bc, ca)]
    return Surface(nv, faces, Sf.name + "-sub4")

# ------------------------------------------------------------------ colourings
def canon(f):
    mp = {}; out = []
    for c in f:
        if c not in mp: mp[c] = len(mp)
        out.append(mp[c])
    return bytes(out)

def enum_torus_reps(T):
    """all proper 4-colourings via column states; keep canonical reps (first-appearance labelling) only. returns (reps, raw_count)"""
    R, Sy = T.R, T.Sy
    cols = [s for s in itertools.product(range(4), repeat=Sy) if all(s[i] != s[(i+1) % Sy] for i in range(Sy))]
    def compat(a, b): return all(a[y] != b[y] and a[y] != b[(y+1) % Sy] for y in range(Sy))
    nb = {a: [b for b in cols if compat(a, b)] for a in cols}
    reps = set(); raw = 0
    # canonical: vertex 0 = (0,0) has colour 0 -> first column state starts with 0
    for c0 in cols:
        if c0[0] != 0: continue
        stack = [(1, [c0])]
        while stack:
            depth, seq = stack.pop()
            if depth == R:
                if compat(seq[-1], seq[0]):
                    raw += 1
                    flat = [c for col in seq for c in col]
                    cf = canon(flat)
                    if bytes(flat) == cf: reps.add(cf)
                continue
            for b in nb[seq[-1]]:
                stack.append((depth + 1, seq + [b]))
    return sorted(reps), raw * 4

def enum_sphere_all(Sf):
    """all proper 4-colourings by backtracking (small graphs); returns list of bytes (raw), and reps"""
    nv = Sf.nv; adj = Sf.adj; f = [-1] * nv; out = []
    order = list(range(nv))
    def bt(i):
        if i == nv: out.append(bytes(f)); return
        v = order[i]
        for c in range(4):
            if all(f[w] != c for w in adj[v] if f[w] >= 0):
                f[v] = c; bt(i + 1); f[v] = -1
    bt(0)
    return out

# ------------------------------------------------------------------ Kempe
def kempe_moves(Sf, f):
    """yield raw colourings obtained by one Kempe swap (every pair, every component)."""
    nv = Sf.nv; adj = Sf.adj
    for a in range(4):
        for b in range(a + 1, 4):
            seen = [False] * nv
            for v in range(nv):
                if seen[v] or f[v] not in (a, b): continue
                comp = []; stack = [v]; seen[v] = True
                while stack:
                    u = stack.pop(); comp.append(u)
                    for w in adj[u]:
                        if not seen[w] and f[w] in (a, b): seen[w] = True; stack.append(w)
                g = list(f)
                for u in comp: g[u] = a + b - g[u]
                yield g, comp

class UF:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x: self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b: self.p[b] = a

def periods(T, f):
    Px = []; Py = []
    for y in range(T.Sy):
        s = [0, 0]
        for x in range(T.R):
            o = T.omega(f, T.vid(x, y), T.vid(x + 1, y)); s[0] += o[0]; s[1] += o[1]
        Px.append(tuple(s))
    for x in range(T.R):
        s = [0, 0]
        for y in range(T.Sy):
            o = T.omega(f, T.vid(x, y), T.vid(x, y + 1)); s[0] += o[0]; s[1] += o[1]
        Py.append(tuple(s))
    return Px, Py

# ================================================================== SPHERE CONTROLS
print("=" * 78); print("Toy 5663 — E5: Kempe classes, Fisk degree, height periods on T(3L,3M)   [prereg 06205eb4]"); print("=" * 78)
print("\nC-sphere: octahedron and its subdivision — one Kempe class (Fisk/Mohar), deg mod 12 constant (Mohar–Salas)")
for Sf in (octahedron(), subdivide(octahedron())):
    degs_ok = all(len(Sf.adj[v]) % 2 == 0 for v in range(Sf.nv))
    raw = enum_sphere_all(Sf); idx = {c: i for i, c in enumerate(raw)}
    uf = UF(len(raw)); degset = set(); face_indep = True; closure = True
    for i, c in enumerate(raw):
        f = list(c)
        d = Sf.degree(f); degset.add(d[0])
        if len(set(d)) != 1: face_indep = False
        if not Sf.face_closure_ok(f): closure = False
        for g, comp in kempe_moves(Sf, f): uf.union(i, idx[bytes(g)])
    ncls = len({uf.find(i) for i in range(len(raw))})
    print(f"    {Sf.name}: nv={Sf.nv} ne={Sf.ne} faces={len(Sf.faces)} all-even={degs_ok}; colourings {len(raw)}; raw Kempe classes {ncls}; degrees {sorted(degset)}; deg mod 12 {sorted({d % 12 for d in degset})}")
    S(f"C-sphere {Sf.name}: one Kempe class, deg independent of tetra face, closure, deg mod 12 constant", ncls == 1 and face_indep and closure and len({d % 12 for d in degset}) == 1)

# ================================================================== TORI
expected_counts = {(3, 3): 240, (6, 3): 8736, (9, 3): 381264, (6, 6): 7325712}
results = {}
for (R, Sy) in [(3, 3), (6, 3), (9, 3), (6, 6)]:
    T = torus(R, Sy); name = T.name; t1 = time.time()
    print(f"\n{name}: nv={T.nv} ne={T.ne} faces={len(T.faces)}  (every vertex degree 6: {all(len(a)==6 for a in T.adj)})")
    reps, raw = enum_torus_reps(T)
    print(f"    enumeration: raw {raw} (transfer matrix {expected_counts[(R,Sy)]}), reps mod S4 {len(reps)}  [{time.time()-t1:.0f}s]", flush=True)
    S(f"C-count {name}: raw total = transfer-matrix count", raw == expected_counts[(R, Sy)])
    idx = {c: i for i, c in enumerate(reps)}
    uf = UF(len(reps))
    rows = []
    ok_face = ok_close = ok_rowcol = ok_parity = True
    moves = 0; moves_P_changed = 0; moves_s_changed = 0; moves_contractible_P_changed = 0
    for i, c in enumerate(reps):
        f = list(c)
        d = T.degree(f)
        if len(set(d)) != 1: ok_face = False
        if i < 2000 and not T.face_closure_ok(f): ok_close = False
        Px, Py = periods(T, f)
        if len(set(Px)) != 1 or len(set(Py)) != 1: ok_rowcol = False
        px, py = Px[0], Py[0]
        if (px[0] | px[1] | py[0] | py[1]) & 1: ok_parity = False
        sx, sy = px[0] + px[1], py[0] + py[1]
        det = px[0] * py[1] - px[1] * py[0]
        rows.append({"i": i, "deg": d[0], "Px": px, "Py": py, "sx": sx, "sy": sy, "det": det})
        for g, comp in kempe_moves(T, f):
            moves += 1
            uf.union(i, idx[canon(g)])
            Px2, Py2 = periods(T, g); px2, py2 = Px2[0], Py2[0]
            if (px2, py2) != (px, py):
                moves_P_changed += 1
            if (px2[0] + px2[1], py2[0] + py2[1]) != (sx, sy): moves_s_changed += 1
        if i % 50000 == 0 and i: print(f"      ... {i} reps [{time.time()-t1:.0f}s]", flush=True)
    for r in rows: r["cls"] = uf.find(r["i"])
    S(f"C-deg {name}: degree independent of tetrahedron face, {len(reps)}/{len(reps)}", ok_face)
    S(f"C-closed {name}: omega closed on every face (first 2000 reps)", ok_close)
    S(f"C-period {name}: P_x same on every row, P_y on every column", ok_rowcol)
    S(f"C-parity {name}: all periods even", ok_parity)
    # Fisk mod 6; Mohar–Salas mod 12 per class
    fisk6 = all(r["deg"] % 6 == 0 for r in rows)
    bycls = defaultdict(list)
    for r in rows: bycls[r["cls"]].append(r)
    ms12 = all(len({r["deg"] % 12 for r in rs}) == 1 for rs in bycls.values())
    S(f"C-MS {name}: deg ≡ 0 mod 6 all ({fisk6}); deg mod 12 constant on every Kempe class ({ms12})", fisk6 and ms12)
    # D2: s ≡ 0 mod 3
    d2 = all(r["sx"] % 3 == 0 and r["sy"] % 3 == 0 for r in rows)
    S(f"D2 {name}: s_x ≡ s_y ≡ 0 (mod 3) for every colouring ([c] = 0 always)", d2)
    # (i)
    S(f"(i)-D1 {name}: integer charges (s_x,s_y) unchanged by EVERY Kempe move, {moves - moves_s_changed}/{moves}", moves_s_changed == 0)
    ncls = len(bycls)
    cls_multi_P = sum(1 for rs in bycls.values() if len({(r['Px'], r['Py']) for r in rs}) > 1)
    print(f"    (i) full datum: Kempe moves changing (P_x,P_y): {moves_P_changed}/{moves}; classes carrying >1 distinct period pair: {cls_multi_P}/{ncls}")
    # D3: deg = ±det/2
    signs = {(r["det"] // 2 == r["deg"]) for r in rows} | {(-(r["det"] // 2) == r["deg"]) for r in rows}
    plus = all(r["det"] == 2 * r["deg"] for r in rows); minus = all(r["det"] == -2 * r["deg"] for r in rows)
    S(f"(ii)-D3 {name}: deg = ±det[P_x,P_y]/2 for every colouring with one sign (+:{plus} −:{minus})", plus or minus)
    # (ii) lookup (sx,sy) -> deg mod 12
    look = defaultdict(set)
    for r in rows: look[(r["sx"], r["sy"])].add(r["deg"] % 12)
    coll = sum(1 for v in look.values() if len(v) > 1)
    print(f"    (ii) (s_x,s_y) -> deg mod 12: {len(look)} distinct pairs, {coll} with two values of deg mod 12")
    # (iii)
    n_pairs = len(look); n_full = len({(r['Px'], r['Py']) for r in rows})
    print(f"    (iii) Kempe classes mod S4: {ncls}; distinct invariant pairs (s_x,s_y): {n_pairs}; distinct full data (P_x,P_y) over reps: {n_full}")
    print(f"          classes by (size, deg mod 12, #distinct s-pairs): {sorted(((len(rs), rs[0]['deg'] % 12, len({(r['sx'], r['sy']) for r in rs})) for rs in bycls.values()), reverse=True)[:12]}")
    S(f"(iii) {name}: #classes ≥ #distinct (s_x,s_y) pairs ({ncls} ≥ {n_pairs})", ncls >= n_pairs)
    results[name] = {"raw": raw, "reps": len(reps), "classes": ncls, "moves": moves, "moves_P_changed": moves_P_changed,
                     "moves_s_changed": moves_s_changed, "classes_multi_P": cls_multi_P, "n_spairs": n_pairs, "n_fulldata": n_full,
                     "deg_values": sorted({r['deg'] for r in rows}), "collisions_s_to_deg12": coll,
                     "class_table": sorted(((len(rs), rs[0]['deg'] % 12, len({(r['sx'], r['sy']) for r in rs}), len({(r['Px'], r['Py']) for r in rs})) for rs in bycls.values()), reverse=True)}
    with open(f".e5_5663_rows_{name.replace('(','').replace(')','').replace(',','x')}.json", "w") as fh:
        json.dump({"prereg": "06205eb4", "torus": name, "reps": [c.hex() for c in reps], "rows": rows}, fh)
    print(f"    [{time.time()-t1:.0f}s]", flush=True)

with open(".e5_5663_summary.json", "w") as fh: json.dump(results, fh, indent=1)
print("\n" + "=" * 78)
npass = sum(1 for _, o in score if o); print(f"SCORE {npass}/{len(score)}   [{time.time()-t0:.0f}s]")
for lab, o in score: print(f"  {'PASS' if o else 'FAIL'}  {lab}")
