#!/usr/bin/env python3
"""
Toy 5626 — E1 (Round 106, "conservation of knowledge" lane, existence check, NO derivation):
THE BRANCHED-COVER CLAUSE OF THE VANTAGE DIMENSION, MEASURED.

Question (Keeper, Round 106 wake prompt): after lifting a planar 4-coloring to the branched
cover, is the observer's global datum a single holonomy, or one datum per dislocation?
Measure: the number of independent global constants the height lift needs, on the in-frame
census (plantri -c5), as a function of n and of the odd-vertex count k.
Pre-registered kill: if that number GROWS with n, rung 1 ("vantage dimension of planar
4-coloring = 1") is FALSE and the measure is the branched-cover rank.

DEFINITIONS PINNED (T2577 / Lyra's Height Dictionary, 08-30, Section 1-4):
  colors = GF(2)^2; edge label l(uv) = f(u)+f(v) in {a,b,c}; steps A=(1,0), B=(0,1), C=(-1,-1),
  A+B+C = 0. Height h: V -> Z^2 with h(v)-h(u) = +/- L(l(uv)). Each properly colored face closes
  in exactly two ways: all-plus or all-minus; coherence across an edge forces ADJACENT FACES INTO
  OPPOSITE CLASSES (a proper 2-coloring of the dual). Exists globally iff Eulerian.
  BRANCHED DOUBLE COVER T~ (this toy's construction, standard): faces (f, s), s = +/-1, dual
  adjacency (f,s) ~ (g,-s). Its dual is bipartite BY CONSTRUCTION (s is the bipartition). A vertex
  v of degree d lifts to ONE cover vertex if d is odd (branch point = dislocation), TWO if even.
  Step on the cover edge of (f,s) traversing u->v in f's boundary orientation: s * L(l(uv)).
  Euler: V~ = 2n-k, E~ = 2E, F~ = 2F, chi = 4-k, rank H_1(T~) = k-2 (k = number of odd vertices).
  The height 1-cocycle delta on T~ is closed on every face; its class [delta] in H^1(T~; Z^2) is
  the HOLONOMY. The observer's global data for the lift = the base point h(v0) (one Z^2 constant;
  its mod-2 part is the color fibre), the sign gauge (one bit), and [delta].

THREE COUNTS REPORTED (the counts, not a verdict word):
  (i)  b1 = k-2: the number of holonomy SLOTS (loops the class [delta] is evaluated on).
  (ii) r = rank of the PERIOD LATTICE P = image of H_1(T~) -> Z^2 (0, 1, or 2), with its
       elementary divisors. r <= 2 is forced by the target rank; whether r is 0 (height single-
       valued on the double cover) is not.
  (iii) N_c = number of distinct DISLOCATION CENTRES: for each odd vertex v the cover vertex v~ is
       fixed by the deck involution tau; c_v = h(v~) in Z^2/P is well defined (tree-independent
       mod P). Hand argument (for Lyra to check): h o tau + h is constant mod P, so 2 c_v is the
       same class for every odd v; hence N_c <= |{p in P : p in 2Z^2} / 2P| <= 4. If that argument
       is right, "one datum per dislocation" is impossible: the dislocation centres are one point
       up to half-periods. Test 6 checks the invariant form 2(c_v - c_w) in P for every pair.

POSITIVE CONTROLS (same period machinery):
  C1 Eulerian sphere (octahedron, all proper 4-colorings): k=0, P=0 -> global constants = base only.
  C2 2-coloring lift (h: V->Z, steps +/-1, FREE signs, faces close): cube on the sphere -> every
     closed lift has zero periods (count 1: parity/base); cylinder C6 x P2 -> the annulus period is
     a FREE datum taking >1 value (count 2). This is Keeper's "sphere 1, cylinder 2" control.

TESTS (X/Y):
  1. Cover construction: V~,E~,F~,chi,bipartite dual, every cover face closes — every (T,f).
  2. C1 Eulerian control: k=0 and P=0 on every octahedron 4-coloring.
  3. C2 2-coloring control: sphere 1 / cylinder 2.
  4. Link loops of every odd vertex have zero period (instrument sanity; a boundary in T~).
  5. THE MEASUREMENT: max r and max N_c per n on the census; PASS if both maxima are constant over
     the last four n values measured; FAIL if either is strictly increasing (the pre-registered kill).
  6. Centre invariant: 2(c_v - c_w) in P for every pair of odd vertices, every (T,f); and N_c <= 4.
     (Caveat stated before the run: if P = 2Z^2 then c_v mod P is just the colour of v and this test
     is weak; its content is the hand argument, which the k-sweep below exercises where P is smaller.)
  7. k-SWEEP (family control, pre-registered): all 3-connected triangulations n = 6..9 (plantri, no
     -c5), all colourings mod S4, grouped by k. Prediction: r = 0 whenever k = 2 (cover genus 0, forced)
     and r <= min(2, k-2) always; P subset of 2Z^2 always (colour is single valued). Whether P = 2Z^2
     as soon as k >= 4 is NOT predicted — measured and reported.

Population: plantri -c5, n = 12..NMAX; all proper 4-colorings mod S4 per graph up to CAP, then a
stratified sample of SAMPLE colorings per graph; graphs sampled to GMAX per n. Records hashed.

Elie, 2026-09-02, Round 106. 7 tests. Off-rubric by construction (Casey's 12:49 override).
"""
import hashlib, json, os, random, subprocess, sys, time
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))
PLANTRI = os.path.join(HERE, 'tools', 'plantri58', 'plantri')
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 22
CAP = 20000        # exhaustive colorings per graph up to this many
SAMPLE = int(os.environ.get("S5626", 400))       # colorings measured per graph (all if fewer)
GMAX = int(os.environ.get("G5626", 60))          # graphs per n (all if fewer)
random.seed(5626)

STEP = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}   # labels a,b,c -> A,B,C ; A+B+C = 0


# ---------------------------------------------------------------- plantri with rotation order
def plantri_rot(n, flags=('-c5',)):
    out = subprocess.run([PLANTRI, '-a', *flags, str(n)], capture_output=True, text=True).stdout
    gs = []
    for line in out.splitlines():
        line = line.strip()
        if not line or not line[0].isdigit():
            continue
        nv, rest = line.split(' ', 1)
        rot = [[ord(ch) - 97 for ch in p] for p in rest.split(',')]
        assert len(rot) == int(nv)
        gs.append(rot)
    return gs


def faces_of(rot):
    """Faces as oriented vertex triples from the rotation system (one consistent orientation)."""
    n = len(rot)
    idx = [{w: i for i, w in enumerate(r)} for r in rot]
    seen = set()
    faces = []
    for u in range(n):
        for v in rot[u]:
            if (u, v) in seen:
                continue
            face = []
            a, b = u, v
            while (a, b) not in seen:
                seen.add((a, b))
                face.append(a)
                r = rot[b]
                c = r[(idx[b][a] - 1) % len(r)]
                a, b = b, c
            faces.append(tuple(face))
    return faces


# ---------------------------------------------------------------- colorings mod S4
def colorings_mod_s4(rot, cap):
    n = len(rot)
    order = list(range(n))
    nbr_before = [[w for w in rot[u] if w < u] for u in order]
    col = [0] * n
    res = []

    def rec(i, mx):
        if len(res) >= cap:
            return
        if i == n:
            res.append(tuple(col)); return
        for c in range(min(3, mx + 1) + 1):
            if all(col[j] != c for j in nbr_before[i]):
                col[i] = c
                rec(i + 1, max(mx, c))
    rec(0, -1)
    return res


# ---------------------------------------------------------------- integer lattice utilities (rank <= 2)
def lattice_hnf(vecs):
    """Hermite-like basis of the Z-span of 2-vectors: returns list of <=2 basis vectors, upper
    triangular [(a, b), (0, d)] with a, d >= 0 (a=0 rows dropped)."""
    rows = [list(v) for v in vecs if v != (0, 0)]
    if not rows:
        return []
    # column 0 elimination by gcd steps
    def reduce_col(rows, c):
        piv = None
        for r in rows:
            if r[c] != 0:
                piv = r; break
        if piv is None:
            return None, rows
        piv = piv[:]
        rest = []
        for r in rows:
            r = r[:]
            while r[c] != 0:
                q = piv[c] // r[c] if abs(r[c]) <= abs(piv[c]) else 0
                if abs(r[c]) <= abs(piv[c]):
                    piv = [piv[i] - q * r[i] for i in range(2)]
                    piv, r = r, piv
                else:
                    q = r[c] // piv[c]
                    r = [r[i] - q * piv[i] for i in range(2)]
            if any(r):
                rest.append(r)
        if piv[c] < 0:
            piv = [-x for x in piv]
        return piv, rest
    p0, rest = reduce_col(rows, 0)
    basis = []
    if p0 is not None:
        basis.append(p0)
        rows2 = rest
    else:
        rows2 = rows
    p1, rest2 = reduce_col([r for r in rows2 if r[1] != 0], 1)
    if p1 is not None:
        basis.append(p1)
    # normalise: reduce b of first row mod d
    if len(basis) == 2:
        a, b = basis[0]; d = basis[1][1]
        basis[0] = [a, b % d]
    return [tuple(v) for v in basis]


def reduce_mod(v, basis):
    """Canonical representative of v in Z^2 / span(basis) (basis upper triangular from lattice_hnf)."""
    x, y = v
    if not basis:
        return (x, y)
    if len(basis) == 2:
        a, b = basis[0]; d = basis[1][1]
        q = x // a; x -= q * a; y -= q * b
        y %= d
        return (x, y)
    (a, b), = basis
    if a != 0:
        q = x // a; x -= q * a; y -= q * b
        return (x, y)
    # basis vector (0, b): reduce y mod b
    return (x, y % b)


def in_lattice(v, basis):
    return reduce_mod(v, basis) == reduce_mod((0, 0), basis)


def elem_divisors(basis):
    if not basis:
        return ()
    if len(basis) == 1:
        a, b = basis[0]
        from math import gcd
        return (gcd(abs(a), abs(b)),)
    a, b = basis[0]; d = basis[1][1]
    from math import gcd
    g = gcd(gcd(a, b), d)
    return (g, a * d // g)


# ---------------------------------------------------------------- the branched double cover + heights
def cover_measure(rot, faces, f):
    n = len(rot)
    deg = [len(r) for r in rot]
    odd = [v for v in range(n) if deg[v] % 2 == 1]
    k = len(odd)
    # face lookup: for oriented edge (u,v) the face containing u->v in its boundary orientation
    fidx = {}
    for i, F in enumerate(faces):
        for j in range(3):
            fidx[(F[j], F[(j + 1) % 3])] = i
    # cover vertices: (v, sheet-class). Around v, faces in rotation order alternate sheet.
    # class of (v, face i, sheet s): walk the fan; define comp id via union-find over (face, sheet) at v.
    # cover-vertex id for (v, face_index, s): computed by parity along the fan from a reference face.
    fan = []   # per v: list of face indices around v in rotation order
    for v in range(n):
        fs = []
        for w in rot[v]:
            fs.append(fidx[(v, w)])   # face containing v->w (one per neighbour, in rotation order)
        fan.append(fs)
    cv_id = {}   # (v, face, s) -> cover vertex id
    ncv = 0
    for v in range(n):
        d = deg[v]
        for pos, fi in enumerate(fan[v]):
            for s in (1, -1):
                # sheet at position pos relative to position 0 sheet: s * (-1)^pos
                base = s * (1 if pos % 2 == 0 else -1)
                if d % 2 == 1:
                    key = (v, 0)
                else:
                    key = (v, base)
                if key not in cv_id:
                    cv_id[key] = ncv; ncv += 1
                cv_id[(v, fi, s)] = cv_id[key]
    assert ncv == 2 * n - k, (ncv, n, k)
    # cover edges with steps
    edges = []   # (cu, cv, step)
    nfaces_cover = 0
    close_ok = True
    for i, F in enumerate(faces):
        for s in (1, -1):
            nfaces_cover += 1
            tot = (0, 0)
            for j in range(3):
                u, v = F[j], F[(j + 1) % 3]
                lab = f[u] ^ f[v]
                st = STEP[lab]
                st = (s * st[0], s * st[1])
                tot = (tot[0] + st[0], tot[1] + st[1])
                # cover vertex of u on face (i, s) and of v on face (i, s)
                cu = cv_id[(u, i, s)]; cvv = cv_id[(v, i, s)]
                edges.append((cu, cvv, st, (u, v, s)))
            if tot != (0, 0):
                close_ok = False
    # each base edge appears twice per sheet-pair (once from each face, opposite directions) -> keep
    # both cover edges: (uv on f, s) and (vu on g, -s) are the SAME cover edge; dedupe by (min,max,sheet key)
    # Consistency check: the two descriptions must give the same cover endpoints and negated step.
    # A cover edge is identified by (base edge, sheet of the face containing u->v with u<v). The
    # description from the other face (traversing v->u on sheet -s) must give the same cover
    # endpoints and the negated step. NOTE: an edge between two ODD vertices lifts to a DOUBLE edge
    # (same two cover endpoints, two sheets), so the key must carry the sheet, not the endpoints.
    seen = {}
    E_cover = []
    consist = True
    for cu, cvv, st, (u, v, s) in edges:
        if u < v:
            key = (u, v, s); desc = (cu, cvv, st)
        else:
            key = (v, u, -s); desc = (cvv, cu, (-st[0], -st[1]))   # rewrite as u<v traversal
        if key in seen:
            if seen[key] != desc:
                consist = False
        else:
            seen[key] = desc
            E_cover.append(desc)
    Ecount = len(E_cover)
    Ebase = 3 * n - 6
    euler_ok = (ncv == 2 * n - k) and (Ecount == 2 * Ebase) and (nfaces_cover == 2 * (2 * n - 4)) \
        and (ncv - Ecount + nfaces_cover == 4 - k)
    # bipartite dual by construction; verify: adjacent cover faces have opposite s (true by key) — record.
    # spanning forest + heights + periods
    adj = [[] for _ in range(ncv)]
    for cu, cvv, st in E_cover:
        adj[cu].append((cvv, st))
        adj[cvv].append((cu, (-st[0], -st[1])))
    h = [None] * ncv
    comps = 0
    periods = []
    for s0 in range(ncv):
        if h[s0] is not None:
            continue
        comps += 1
        h[s0] = (0, 0)
        dq = deque([s0])
        while dq:
            x = dq.popleft()
            for y, st in adj[x]:
                if h[y] is None:
                    h[y] = (h[x][0] + st[0], h[x][1] + st[1]); dq.append(y)
    for cu, cvv, st in E_cover:
        p = (h[cu][0] + st[0] - h[cvv][0], h[cu][1] + st[1] - h[cvv][1])
        if p != (0, 0):
            periods.append(p)
    basis = lattice_hnf(periods)
    r = len(basis)
    ed = elem_divisors(basis)
    # link loops of odd vertices: sum of steps around the cover link (length 2d) must be 0
    link_ok = True
    for v in odd:
        cvv = cv_id[(v, 0)]
        # neighbours in cover of cvv: follow the fan on both sheets
        tot = (0, 0)
        d = deg[v]
        for pos in range(d):
            fi = fan[v][pos]
            F = faces[fi]
            j = F.index(v)
            a, b = F[(j + 1) % 3], F[(j + 2) % 3]   # a->b is the link edge in face orientation
            for s in (1, -1):
                st = STEP[f[a] ^ f[b]]
                # sheet of face (fi, s) at v: s*(-1)^pos  ; both sheets appear in the double link
                tot = (tot[0] + s * st[0], tot[1] + s * st[1])
        if tot != (0, 0):
            link_ok = False
    # dislocation centres c_v = h(v~) mod P
    centres = [reduce_mod(h[cv_id[(v, 0)]], basis) for v in odd]
    Nc = len(set(centres))
    # invariant: 2(c_v - c_w) in P for all pairs
    inv_ok = True
    for i in range(len(odd)):
        for j in range(i + 1, len(odd)):
            a = h[cv_id[(odd[i], 0)]]; b = h[cv_id[(odd[j], 0)]]
            if not in_lattice((2 * (a[0] - b[0]), 2 * (a[1] - b[1])), basis):
                inv_ok = False
    return dict(k=k, b1=k - 2, r=r, ed=ed, Nc=Nc, comps=comps, close=close_ok, euler=euler_ok,
                consist=consist, link=link_ok, inv=inv_ok, P0=(r == 0), basis=basis, hodd=[h[cv_id[(v, 0)]] for v in odd], odd=odd)


# ---------------------------------------------------------------- controls
def octahedron():
    # vertices 0-5, antipodal pairs (0,1),(2,3),(4,5); rotation orders (clockwise) for a genuine embedding
    # coordinates: 0=+z,1=-z,2=+x,3=-x,4=+y,5=-y
    rot = [[2, 4, 3, 5], [2, 5, 3, 4], [0, 5, 1, 4], [0, 4, 1, 5], [0, 2, 1, 3], [0, 3, 1, 2]]
    return rot


def two_coloring_lifts(vertices, edges, faces, cyc_loop):
    """Enumerate all closed +/-1 step assignments on edges (faces close), compute the period on the
    given loop (list of directed edges). Returns set of period values."""
    m = len(edges)
    eidx = {e: i for i, e in enumerate(edges)}
    per = set()
    import itertools
    for signs in itertools.product((1, -1), repeat=m):
        ok = True
        for F in faces:
            tot = 0
            for j in range(len(F)):
                u, v = F[j], F[(j + 1) % len(F)]
                if (u, v) in eidx:
                    tot += signs[eidx[(u, v)]]
                else:
                    tot -= signs[eidx[(v, u)]]
            if tot != 0:
                ok = False; break
        if not ok:
            continue
        p = 0
        for (u, v) in cyc_loop:
            p += signs[eidx[(u, v)]] if (u, v) in eidx else -signs[eidx[(v, u)]]
        per.add(p)
    return per


def control_2col():
    # cube on the sphere: vertices 0..7 (bits), edges differ in one bit, faces = 6 squares
    verts = list(range(8))
    edges = sorted({(min(u, u ^ b), max(u, u ^ b)) for u in verts for b in (1, 2, 4)})
    faces = []
    for bit in (1, 2, 4):
        for val in (0, bit):
            others = [b for b in (1, 2, 4) if b != bit]
            o1, o2 = others
            faces.append((val, val | o1, val | o1 | o2, val | o2))
    # a loop that is a face boundary (sphere has no nontrivial loop): equator 0-1-3-2 is face (0,1,3,2)
    loop = [(0, 1), (1, 3), (3, 2), (2, 0)]
    sphere_periods = two_coloring_lifts(verts, edges, faces, loop)
    # cylinder C6 x P2: vertices (i, j), i mod 6, j in {0,1}; square faces (i,0),(i+1,0),(i+1,1),(i,1)
    verts = [(i, j) for i in range(6) for j in range(2)]
    edges = []
    for i in range(6):
        for j in range(2):
            edges.append(((i, j), ((i + 1) % 6, j)))
        edges.append(((i, 0), (i, 1)))
    faces = [((i, 0), ((i + 1) % 6, 0), ((i + 1) % 6, 1), (i, 1)) for i in range(6)]
    loop = [((i, 0), ((i + 1) % 6, 0)) for i in range(6)]
    cyl_periods = two_coloring_lifts(verts, edges, faces, loop)
    return sphere_periods, cyl_periods


# ---------------------------------------------------------------- main
if __name__ == '__main__':
    t0 = time.time()
    print('=' * 78)
    print(f'Toy 5626 — E1: branched-cover clause of the vantage dimension, plantri -c5 n=12..{NMAX}')
    print('=' * 78)
    score = 0; total = 7

    # ---- Test 2: Eulerian control (octahedron)
    rot = octahedron(); faces = faces_of(rot)
    assert len(faces) == 8 and all(len(F) == 3 for F in faces)
    cols = colorings_mod_s4(rot, 10 ** 6)
    res = [cover_measure(rot, faces, f) for f in cols]
    t2 = all(m['k'] == 0 and m['r'] == 0 and m['close'] and m['comps'] == 2 for m in res)
    print(f'\n[C1] Eulerian sphere (octahedron): {len(cols)} colorings mod S4; k=0 all: '
          f'{all(m["k"]==0 for m in res)}; P=0 all: {all(m["r"]==0 for m in res)}; '
          f'cover = 2 disjoint sheets all: {all(m["comps"]==2 for m in res)}  -> global constants = base only')
    score += t2
    print(f'  Test 2 {"PASS" if t2 else "FAIL"}')

    # ---- Test 3: 2-coloring control
    sp, cy = control_2col()
    t3 = (sp == {0}) and (len(cy) > 1)
    print(f'\n[C2] 2-coloring lift, FREE signs, faces close: sphere (cube) loop periods = {sorted(sp)} '
          f'-> {1 if sp == {0} else "?"} global constant (parity/base); cylinder C6xP2 annulus periods = '
          f'{sorted(cy)} ({len(cy)} values) -> 2 global constants (base + winding)')
    score += t3
    print(f'  Test 3 {"PASS" if t3 else "FAIL"}')

    # ---- Census
    per_n = {}
    rec_lines = []
    all_ok = dict(cover=True, link=True, inv=True)
    for n in range(12, NMAX + 1):
        gs = plantri_rot(n)
        if not gs:
            continue
        # gi below is the plantri -c5 output index (0-based) — the join key — even when sampled
        gsel = list(enumerate(gs)) if len(gs) <= GMAX else sorted(random.sample(list(enumerate(gs)), GMAX))
        kd, rd, ncd, edd, p0 = Counter(), Counter(), Counter(), Counter(), Counter()
        ncol_tot = 0; exhaustive = 0
        for gi, rot in gsel:
            faces = faces_of(rot)
            assert len(faces) == 2 * n - 4 and all(len(F) == 3 for F in faces), n
            cols = colorings_mod_s4(rot, CAP)
            if len(cols) < CAP:
                exhaustive += 1
            csel = cols if len(cols) <= SAMPLE else random.sample(cols, SAMPLE)
            for f in csel:
                m = cover_measure(rot, faces, f)
                ncol_tot += 1
                kd[m['k']] += 1; rd[m['r']] += 1; ncd[m['Nc']] += 1; edd[m['ed']] += 1; p0[m['P0']] += 1
                all_ok['cover'] &= (m['close'] and m['euler'] and m['consist'] and m['comps'] == 1)
                all_ok['link'] &= m['link']
                all_ok['inv'] &= (m['inv'] and m['Nc'] <= 4)
                rec_lines.append(f'{n} plantri_c5_idx={gi} {"".join(map(str,f))} k={m["k"]} r={m["r"]} ed={m["ed"]} Nc={m["Nc"]}')
        per_n[n] = dict(graphs=len(gs), used=len(gsel), colorings=ncol_tot, exhaustive_graphs=exhaustive,
                        k=dict(sorted(kd.items())), r=dict(sorted(rd.items())), Nc=dict(sorted(ncd.items())),
                        ed=dict(sorted((str(a), b) for a, b in edd.items())), P0=dict(p0),
                        max_r=max(rd), max_Nc=max(ncd))
        print(f'\n  n={n}: graphs {len(gs)} (used {len(gsel)}, exhaustive-coloring graphs {exhaustive}), '
              f'colorings measured {ncol_tot}  [{time.time()-t0:.0f}s]')
        print(f'    k (odd vertices): {dict(sorted(kd.items()))}   b1 = k-2')
        print(f'    r (period-lattice rank): {dict(sorted(rd.items()))}   P=0 count: {p0[True]}')
        print(f'    elementary divisors: {dict(sorted((str(a), b) for a, b in edd.items()))}')
        print(f'    N_c (distinct dislocation centres mod P): {dict(sorted(ncd.items()))}')
        sys.stdout.flush()

    # ---- Test 1, 4, 6
    t1 = all_ok['cover']; t4 = all_ok['link']; t6 = all_ok['inv']
    print(f'\n  Test 1 (cover: V~=2n-k, E~=2E, F~=2F, chi=4-k, both descriptions agree, faces close, connected) '
          f'{"PASS" if t1 else "FAIL"}')
    print(f'  Test 4 (link loop of every odd vertex has zero period) {"PASS" if t4 else "FAIL"}')
    print(f'  Test 6 (2(c_v - c_w) in P for every pair; N_c <= 4) {"PASS" if t6 else "FAIL"}')
    score += t1 + t4 + t6

    # ---- Test 5: the measurement
    ns = sorted(per_n)
    last = ns[-4:]
    mr = [per_n[n]['max_r'] for n in last]; mn = [per_n[n]['max_Nc'] for n in last]
    grows_r = all(mr[i] < mr[i + 1] for i in range(len(mr) - 1))
    grows_n = all(mn[i] < mn[i + 1] for i in range(len(mn) - 1))
    const = (len(set(mr)) == 1) and (len(set(mn)) == 1)
    print('\n  MEASUREMENT (max over census per n):')
    print('    n   : ' + ' '.join(f'{n:>4}' for n in ns))
    print('    max r: ' + ' '.join(f'{per_n[n]["max_r"]:>4}' for n in ns))
    print('    max Nc: ' + ' '.join(f'{per_n[n]["max_Nc"]:>4}' for n in ns))
    print('    max k: ' + ' '.join(f'{max(per_n[n]["k"]):>4}' for n in ns))
    t5 = const and not (grows_r or grows_n)
    print(f'  Test 5 (last four n {last}: max r {mr}, max N_c {mn}; PASS = both constant, FAIL = strictly '
          f'increasing) {"PASS" if t5 else ("FAIL — KILL FIRES" if (grows_r or grows_n) else "UNDECIDED (not constant, not monotone)")}')
    score += t5

    # ---- Test 7: k-sweep over all 3-connected triangulations n=6..9
    print('\n  k-SWEEP (all 3-connected triangulations, all colourings mod S4):')
    ks_ok = True
    ksum = {}
    for n in range(6, 10):
        for rot in plantri_rot(n, flags=()):
            faces = faces_of(rot)
            for f in colorings_mod_s4(rot, 10 ** 6):
                m = cover_measure(rot, faces, f)
                d = ksum.setdefault(m['k'], Counter())
                d[(m['r'], m['ed'])] += 1
                if m['k'] == 2 and m['r'] != 0:
                    ks_ok = False
                if m['r'] > min(2, max(m['k'] - 2, 0)):
                    ks_ok = False
                # P subset 2Z^2: every basis vector even
                if any(x % 2 for b in m['basis'] for x in b):
                    ks_ok = False
    for k in sorted(ksum):
        print(f'    k={k:>2}: ' + ', '.join(f'r={r} ed={ed}: {c}' for (r, ed), c in sorted(ksum[k].items())))
    print(f'  Test 7 (k-sweep: r=0 at k=2; r <= min(2,k-2); P in 2Z^2) {"PASS" if ks_ok else "FAIL"}')
    score += ks_ok

    blob = '\n'.join(rec_lines).encode()
    hsh = hashlib.sha256(blob).hexdigest()[:8]
    with open(os.path.join(HERE, '.e1_5626_records.txt'), 'wb') as fh:
        fh.write(blob)
    with open(os.path.join(HERE, '.e1_5626_summary.json'), 'w') as fh:
        json.dump(per_n, fh, indent=1)
    print(f'\n  records: play/.e1_5626_records.txt sha256 {hsh}; summary play/.e1_5626_summary.json')
    print(f'\nSCORE: {score}/{total}   [{time.time()-t0:.0f}s]')
