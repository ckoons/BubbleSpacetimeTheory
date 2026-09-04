#!/usr/bin/env python3
"""
E5 SECOND INSTRUMENT (Grace, 2026-09-04) beside Elie 5663 — same spec, same space, independent code.
Space: T(r,s) = Mohar–Salas T(r,s,0): vertices Z_r x Z_s, edges (1,0),(0,1),(1,1); faces up (x,y),(x+1,y),(x+1,y+1) and down
(x,y),(x+1,y+1),(x,y+1), both listed ccw.  Chess sign: sigma(up) = +1, sigma(down) = -1 (dual bipartite).
Colours = Klein group V: 0=00, a=01, b=10, c=11 (sum = xor).  Height cochain (Elie's pre-registration, T2577):
  omega(u->w) = sigma(left face of u->w) * L(f(u) xor f(w)),  L(a)=(1,0), L(b)=(0,1), L(c)=(-1,-1).
Datum: periods P_x = sum omega along row y (x = 0..r-1), P_y = sum omega along column x; integer charges s = <P,(1,1)>.
Fisk degree (Mohar–Salas eq. 3.2): p - n over faces coloured {0,1,2} with ccw order agreeing / disagreeing with 0->1->2
(target face = {0,1,2}); face-independence checked against target {0,1,3}.
Kempe classes: colourings mod S4 (canonical form), BFS over K-changes (swap two colours on one component of the 2-colour subgraph).
Controls: closure of omega on every face; P_x independent of the row, P_y of the column; degree face-independent; deg = 0 mod 6;
deg mod 12 constant on every class; periods even; octahedron (one class, deg const); counts = transfer matrix (prep script).
Lines (Elie 06205eb4): (i) full datum invariant? integer charges invariant? (ii) deg = +-det(P_x,P_y)/2 on every colouring?
deg mod 12 a function of (s_x,s_y)?  (iii) classes vs distinct datum values; T(6,6) literature control 305,192/45/1 at |deg| 0/6/18, kappa = 2.
Cal §847 flag: charges predicted to move by +-3 under swaps with colour-sum a or b (only sum c preserves them).
"""
import sys, collections, time, json, hashlib
# REV 2 (09:1x): datum compared RAW across one move (canonicalisation permutes A,B,C — a lattice automorphism — and faked datum changes in rev 1);
# distinct data counted modulo the S3 action permuting (A,B,C) as well as raw.
S3 = [lambda v:(v[0],v[1]), lambda v:(v[1],v[0]), lambda v:(-v[0]-v[1],v[1]), lambda v:(v[0],-v[0]-v[1]), lambda v:(v[1],-v[0]-v[1]), lambda v:(-v[0]-v[1],v[0])]
def orbit_rep(P): return min(tuple(g(p) for p in P) for g in S3)
L = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}
def torus(r, s):
    idx = lambda x, y: (x % r) * s + (y % s); N = r * s
    nb = [set() for _ in range(N)]; faces = []; left = {}
    for x in range(r):
        for y in range(s):
            a, b, c, d = idx(x, y), idx(x + 1, y), idx(x + 1, y + 1), idx(x, y + 1)
            for u, w in ((a, b), (a, d), (a, c)): nb[u].add(w); nb[w].add(u)
            fu = len(faces); faces.append((a, b, c)); fd = len(faces); faces.append((a, c, d))   # up: sigma +1 ; down: sigma -1
            # left face of directed edge u->w for a ccw face (u,w,z): the face itself
            for (F, sg) in ((faces[fu], 1), (faces[fd], -1)):
                for i in range(3): left[(F[i], F[(i + 1) % 3])] = sg
    return N, [sorted(n) for n in nb], faces, left, idx
def omega(col, u, w, left):
    k = col[u] ^ col[w]; lx, ly = L[k]; sg = left[(u, w)]; return (sg * lx, sg * ly)
def periods(col, r, s, idx, left):
    Px = set(); Py = set()
    for y in range(s):
        sx = sy = 0
        for x in range(r):
            o = omega(col, idx(x, y), idx(x + 1, y), left); sx += o[0]; sy += o[1]
        Px.add((sx, sy))
    for x in range(r):
        sx = sy = 0
        for y in range(s):
            o = omega(col, idx(x, y), idx(x, y + 1), left); sx += o[0]; sy += o[1]
        Py.add((sx, sy))
    return Px, Py
def degree(col, faces, target=(0, 1, 2)):
    p = n = 0; t = set(target); rot = {(target[0], target[1], target[2]), (target[1], target[2], target[0]), (target[2], target[0], target[1])}
    for (a, b, c) in faces:
        cs = (col[a], col[b], col[c])
        if set(cs) != t: continue
        if cs in rot: p += 1
        else: n += 1
    return p - n
def canon(col):
    m = {}; return tuple(m.setdefault(c, len(m)) for c in col)
def enum_canonical(nb, N):
    """proper 4-colourings in canonical form: colours introduced in order 0,1,2,3 along vertex order."""
    col = [-1] * N; out = []
    def rec(i, k):
        if i == N: out.append(tuple(col)); return
        used = {col[u] for u in nb[i] if u < i}
        for c in range(min(k + 1, 4)):
            if c not in used:
                col[i] = c; rec(i + 1, max(k, c + 1)); col[i] = -1
    rec(0, 0); return out
def kempe_moves(col, nb, N):
    col = list(col)
    for a in range(4):
        for b in range(a + 1, 4):
            visited = [False] * N
            for v0 in range(N):
                if visited[v0] or col[v0] not in (a, b): continue
                comp = []; st = [v0]; visited[v0] = True
                while st:
                    v = st.pop(); comp.append(v)
                    for w in nb[v]:
                        if not visited[w] and col[w] in (a, b): visited[w] = True; st.append(w)
                new = col[:]
                for v in comp: new[v] = b if new[v] == a else a
                yield (a, b, comp, tuple(new))
def run(r, s, label_control=None):
    t0 = time.time(); N, nb, faces, left, idx = torus(r, s)
    cols = enum_canonical(nb, N); S = set(cols)
    print(f"\nT({r},{s}): N = {N}, canonical colourings {len(cols)}  ({time.time()-t0:.1f}s)", flush=True)
    # per-colouring data
    data = {}
    closure_fail = period_fail = face_fail = odd_period = 0
    for c in cols:
        for (a, b, cc) in faces:
            o = [omega(c, a, b, left), omega(c, b, cc, left), omega(c, cc, a, left)]
            if sum(x[0] for x in o) or sum(x[1] for x in o): closure_fail += 1; break
        Px, Py = periods(c, r, s, idx, left)
        if len(Px) > 1 or len(Py) > 1: period_fail += 1
        P = (next(iter(Px)), next(iter(Py)))
        if any(v % 2 for v in P[0] + P[1]): odd_period += 1
        d = degree(c, faces); d2 = degree(c, faces, (0, 1, 3))
        if abs(d) != abs(d2): face_fail += 1
        det = P[0][0] * P[1][1] - P[0][1] * P[1][0]
        data[c] = dict(P=P, s=(P[0][0] + P[0][1], P[1][0] + P[1][1]), deg=d, det=det)
    print(f"  controls: closure fails {closure_fail}, row/column-dependent periods {period_fail}, face-dependent |deg| {face_fail}, odd periods {odd_period}", flush=True)
    # classes by BFS (on raw colourings via canonical keys); record moves that change datum / charges
    cls = {}; k = 0; moves = 0; datum_changed = 0; charge_changed = collections.Counter(); charge_by_sum = collections.Counter()
    for c in cols:
        if c in cls: continue
        k += 1; cls[c] = k; q = [c]
        while q:
            x = q.pop(); dx = data[x]
            for (a, b, comp, new) in kempe_moves(x, nb, N):
                y = canon(new); moves += 1
                Pxn, Pyn = periods(new, r, s, idx, left); Pn = (next(iter(Pxn)), next(iter(Pyn)))   # RAW datum after the move
                if Pn != dx['P']: datum_changed += 1
                csum = a ^ b   # colour-sum of the swapped pair as a Klein element (1=a,2=b,3=c)
                charge_by_sum[csum] += 1
                if (Pn[0][0] + Pn[0][1], Pn[1][0] + Pn[1][1]) != dx['s']: charge_changed[csum] += 1
                if y not in cls: cls[y] = k; q.append(y)
    degs = collections.Counter(abs(v['deg']) for v in data.values())
    print(f"  Kempe classes kappa = {k}; moves examined {moves}; datum (P_x,P_y) changed on {datum_changed} moves; integer charges changed: {dict(charge_changed)} of moves by colour-sum {dict(charge_by_sum)}", flush=True)
    print(f"  |deg| histogram {dict(sorted(degs.items()))}; deg = 0 mod 6 on all: {all(v['deg'] % 6 == 0 for v in data.values())}", flush=True)
    # (ii) deg vs det/2
    ok_plus = sum(1 for v in data.values() if v['deg'] == v['det'] // 2 and v['det'] % 2 == 0); ok_minus = sum(1 for v in data.values() if v['deg'] == -(v['det'] // 2) and v['det'] % 2 == 0)
    print(f"  (ii) deg = +det/2 on {ok_plus}/{len(data)}; deg = -det/2 on {ok_minus}/{len(data)}; det in 12Z on {sum(1 for v in data.values() if v['det'] % 12 == 0)}/{len(data)}", flush=True)
    lookup = collections.defaultdict(set)
    for v in data.values(): lookup[v['s']].add(v['deg'] % 12)
    print(f"  (ii) deg mod 12 a function of (s_x,s_y)? {all(len(x) == 1 for x in lookup.values())}  (charge values {len(lookup)}; multi-valued at {sum(1 for x in lookup.values() if len(x) > 1)})", flush=True)
    # (iii) class x datum / class x charges / class x deg mod 12
    tab = collections.defaultdict(collections.Counter); tabs = collections.defaultdict(collections.Counter); tabd = collections.defaultdict(collections.Counter)
    for c, v in data.items(): tab[cls[c]][v['P']] += 1; tabs[cls[c]][v['s']] += 1; tabd[cls[c]][v['deg'] % 12] += 1
    print(f"  (iii) classes {k}; distinct full data {len({v['P'] for v in data.values()})} (mod S3 on A,B,C: {len({orbit_rep(v['P']) for v in data.values()})}); distinct charge pairs {len(lookup)}", flush=True)
    for kk in sorted(tab):
        print(f"     class {kk}: size {sum(tab[kk].values())}; deg mod 12 {dict(tabd[kk])}; #data {len(tab[kk])}; charges {dict(tabs[kk]) if len(tabs[kk]) <= 12 else len(tabs[kk])}", flush=True)
    datum_shared = sum(1 for P in {v['P'] for v in data.values()} if sum(1 for kk in tab if P in tab[kk]) > 1)
    print(f"  (iii) full data appearing in more than one class: {datum_shared}", flush=True)
    return dict(r=r, s=s, colourings=len(cols), kappa=k, deg_hist=dict(sorted(degs.items())), datum_changed=datum_changed, moves=moves,
                charge_changed=dict(charge_changed), charge_by_sum=dict(charge_by_sum), deg_plus=ok_plus, deg_minus=ok_minus,
                deg_fn_of_charges=all(len(x) == 1 for x in lookup.values()), distinct_data=len({v['P'] for v in data.values()}), data_shared=datum_shared,
                per_class={kk: dict(size=sum(tab[kk].values()), degmod12=dict(tabd[kk]), ndata=len(tab[kk])) for kk in tab})
def octahedron():
    nb = [set() for _ in range(6)]; pairs = {(0, 5), (1, 4), (2, 3)}
    for u in range(6):
        for w in range(6):
            if u != w and (min(u, w), max(u, w)) not in pairs: nb[u].add(w)
    # faces: triples of mutually adjacent vertices, oriented consistently (outward) — use a fixed list
    faces = [(0,1,2),(0,2,4),(0,4,3),(0,3,1),(5,2,1),(5,4,2),(5,3,4),(5,1,3)]
    N = 6; cols = enum_canonical([sorted(n) for n in nb], N); S = set(cols); cls = {}; k = 0
    for c in cols:
        if c in cls: continue
        k += 1; cls[c] = k; q = [c]
        while q:
            x = q.pop()
            for (_, _, _, new) in kempe_moves(x, [sorted(n) for n in nb], N):
                y = canon(new)
                if y not in cls: cls[y] = k; q.append(y)
    degs = collections.Counter(degree(c, faces) % 12 for c in cols)
    print(f"octahedron control: colourings {len(cols)}, Kempe classes {k} (Fisk: 1), deg mod 12 values {dict(degs)}", flush=True)
if __name__ == '__main__':
    octahedron()
    out = []
    for (r, s) in [(3, 3), (6, 3), (9, 3), (6, 6)]:
        out.append(run(r, s))
        json.dump(out, open('.e5_second_instrument_results.json', 'w'))
    print("\nresults sha256", hashlib.sha256(json.dumps(out, sort_keys=True).encode()).hexdigest()[:16])
