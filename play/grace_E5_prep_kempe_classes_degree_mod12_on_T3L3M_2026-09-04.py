#!/usr/bin/env python3
"""
Grace E5 PREP (unnumbered — not a toy; the numbered run waits for Lyra's E4 datum and Elie's design).
Torus T(r,s) = T(r,s,0) per Mohar–Salas 2009 §2 (Altschuler): vertices Z_r x Z_s, edges (1,0),(0,1),(1,1) — the (r+1)x(s+1) grid
with the NE diagonal, opposite sides identified, no shift. 6-regular, Eulerian; 3-colourable iff 3|r and 3|s (Prop. 2.3).
Faces: for each (x,y) the up-triangle (x,y),(x+1,y),(x+1,y+1) and the down-triangle (x,y),(x+1,y+1),(x,y+1) — both listed ccw.
DEGREE (Mohar–Salas eq. 3.2, Fisk): fix the target face t = {1,2,3} of the tetrahedron; deg f = p - n where p (n) counts faces of T
coloured {1,2,3} whose ccw colour order agrees (disagrees) with the fixed orientation 1->2->3. Independent of t; three-colouring deg 0;
Eulerian => even; 3-colourable surface => deg = 0 mod 6 (Prop. 3.2); Kempe invariant mod 12 (Thm 3.4); Fisk: deg = 0 mod 12 <=> the
class of the 3-colouring (Thm 2.8 / 3.6, torus).
KEMPE CLASSES: colourings modulo global colour permutation (their convention); a K-change swaps two colours on one component of the
induced two-colour subgraph; classes by BFS over canonical representatives.
Instrument checks (this prep): (a) count of proper 4-colourings by transfer matrix = P_G(4), cross-checked by enumeration on small tori;
(b) deg = 0 mod 6 on every colouring of a 3-colourable torus; (c) deg mod 12 constant on each Kempe class; (d) T(3,3): kappa = ?
(e) T(6,6): kappa >= 2 (Mohar–Salas Cor. 3.5 + their existence theorem for L >= 2).
"""
import sys, itertools, collections, time
def torus(r, s):
    V = [(x, y) for x in range(r) for y in range(s)]; idx = {v: i for i, v in enumerate(V)}
    nb = [set() for _ in V]
    for (x, y) in V:
        for dx, dy in ((1, 0), (0, 1), (1, 1)):
            u = idx[(x, y)]; w = idx[((x + dx) % r, (y + dy) % s)]; nb[u].add(w); nb[w].add(u)
    faces = []
    for (x, y) in V:
        a = idx[(x, y)]; b = idx[((x + 1) % r, y)]; c = idx[((x + 1) % r, (y + 1) % s)]; d = idx[(x, (y + 1) % s)]
        faces.append((a, b, c)); faces.append((a, c, d))   # both ccw in the grid orientation
    return V, [sorted(n) for n in nb], faces
def degree(col, faces):
    p = n = 0
    for (a, b, c) in faces:
        cs = (col[a], col[b], col[c])
        if set(cs) != {0, 1, 2}: continue
        # ccw order agrees with 0->1->2 iff cs is a cyclic rotation of (0,1,2)
        if cs in ((0, 1, 2), (1, 2, 0), (2, 0, 1)): p += 1
        else: n += 1
    return p - n
def canon(col):
    m = {}; out = []
    for c in col:
        if c not in m: m[c] = len(m)
        out.append(m[c])
    return tuple(out)
def enumerate_colourings(nb, N):
    """all proper 4-colourings with vertex 0 fixed to colour 0 (then canonicalise)"""
    col = [-1] * N; out = []
    order = list(range(N))
    def rec(i):
        if i == N: out.append(tuple(col)); return
        v = order[i]; used = {col[u] for u in nb[v] if col[u] >= 0}
        for c in range(4):
            if c not in used:
                if v == 0 and c != 0: continue
                col[v] = c; rec(i + 1); col[v] = -1
    rec(0); return out
def kempe_neighbours(col, nb, N):
    col = list(col); seen_pairs = set()
    for a in range(4):
        for b in range(a + 1, 4):
            visited = [False] * N
            for v0 in range(N):
                if visited[v0] or col[v0] not in (a, b): continue
                comp = []; stack = [v0]; visited[v0] = True
                while stack:
                    v = stack.pop(); comp.append(v)
                    for w in nb[v]:
                        if not visited[w] and col[w] in (a, b): visited[w] = True; stack.append(w)
                new = col[:]
                for v in comp: new[v] = b if new[v] == a else a
                yield canon(new)
def classes(cols, nb, N):
    S = set(canon(c) for c in cols); cls = {}; k = 0
    for c in S:
        if c in cls: continue
        k += 1; cls[c] = k; q = [c]
        while q:
            x = q.pop()
            for y in kempe_neighbours(x, nb, N):
                if y in S and y not in cls: cls[y] = k; q.append(y)
    return cls, k
def count_TM(r, s):
    """P_G(4) for T(r,s) by transfer matrix over columns (states: colourings of a column of s vertices, cyclic vertical edges)."""
    import numpy as np
    states = [c for c in itertools.product(range(4), repeat=s) if all(c[y] != c[(y + 1) % s] for y in range(s))]
    S = len(states); ix = {c: i for i, c in enumerate(states)}
    T = np.zeros((S, S), dtype=object)
    for i, c in enumerate(states):
        for j, d in enumerate(states):   # column x = c, column x+1 = d: edges (x,y)-(x+1,y) and (x,y)-(x+1,y+1)
            if all(c[y] != d[y] and c[y] != d[(y + 1) % s] for y in range(s)): T[i, j] = 1
    M = np.identity(S, dtype=object)
    for _ in range(r): M = M.dot(T)
    return int(sum(M[i, i] for i in range(S)))
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'count'
    if mode == 'count':
        for (r, s) in [(3, 3), (6, 3), (9, 3), (6, 6), (12, 3), (9, 6), (12, 6), (9, 9)]:
            t = time.time(); P = count_TM(r, s)
            print(f"  T({r},{s}): V={r*s:3d}  P_G(4) = {P:>16d}  colourings mod S4 = {P//24:>14d}   ({time.time()-t:.1f}s)", flush=True)
    else:
        r, s = int(sys.argv[2]), int(sys.argv[3])
        V, nb, faces = torus(r, s); N = len(V)
        t = time.time(); cols = enumerate_colourings(nb, N)
        print(f"T({r},{s}): N={N}, colourings with v0=0: {len(cols)} (= P_G(4)/4 = {count_TM(r,s)//4}), {time.time()-t:.1f}s")
        cls, k = classes(cols, nb, N)
        degs = collections.Counter(); bycls = collections.defaultdict(collections.Counter)
        for c in cls: d = degree(c, faces); degs[abs(d)] += 1; bycls[cls[c]][d % 12] += 1
        print(f"  canonical colourings: {len(cls)}  Kempe classes kappa = {k}")
        print(f"  |deg| histogram: {dict(sorted(degs.items()))}   all deg = 0 mod 6: {all(d % 6 == 0 for d in degs)}")
        for kk in sorted(bycls): print(f"   class {kk}: size {sum(bycls[kk].values())}  deg mod 12 values {dict(bycls[kk])}")
