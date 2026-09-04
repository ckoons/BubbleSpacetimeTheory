#!/usr/bin/env python3
"""E6 (T) under R2: subdivision T(3,3)->T(6,6). R2-images of the 240 parent colourings by Kempe class of the child; R1 fibre counts."""
import json, os, glob, itertools, time
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(glob.glob(os.path.join(HERE, 'toy_5663_SEP4_*.py'))[0]).read().split("# ================================================================== SPHERE CONTROLS")[0]
ns = {"__file__": "x"}; exec(compile(src, "t5663", "exec"), ns)
torus, canon, kempe_moves = ns["torus"], ns["canon"], ns["kempe_moves"]
t0 = time.time()
C = torus(6, 6); P = torus(3, 3)
rows = json.load(open(os.path.join(HERE, '.e5_5663_rows_T6x6.json')))
reps = rows['reps']; R = rows['rows']
cls_of = {bytes.fromhex(h): R[i]['cls'] for i, h in enumerate(reps)}
deg_of = {bytes.fromhex(h): R[i]['deg'] for i, h in enumerate(reps)}
odd_cls = {R[i]['cls'] for i in range(len(R)) if R[i]['deg'] != 0}; assert len(odd_cls) == 1; odd = odd_cls.pop()
# parents: all 240 raw colourings of T(3,3)
def all_colourings(T):
    nv = T.nv; adj = T.adj; f = [-1] * nv; out = []
    def bt(i):
        if i == nv: out.append(tuple(f)); return
        for c in range(4):
            if all(f[w] != c for w in adj[i] if f[w] >= 0):
                f[i] = c; bt(i + 1); f[i] = -1
    bt(0); return out
parents = all_colourings(P); assert len(parents) == 240
# child coordinates: vid(x,y) = x*6 + y ; parent (x,y) -> child (2x,2y)
def child_of_parent(pf):
    g = [-1] * 36
    for x in range(3):
        for y in range(3): g[C.vid(2 * x, 2 * y)] = pf[P.vid(x, y)]
    return g
def R2(pf):
    g = child_of_parent(pf)
    for v in range(36):          # lexicographic in (x, y) = vid order
        if g[v] >= 0: continue
        for c in range(4):
            if all(g[w] != c for w in C.adj[v] if g[w] >= 0): g[v] = c; break
        if g[v] < 0: return None
    return g
m1 = 0; partial = 0; degs = Counter(); inj_ok = True; images = []
for pf in parents:
    g = R2(pf)
    if g is None: partial += 1; continue
    assert all(g[u] != g[w] for u in range(36) for w in C.adj[u])
    key = canon(g); cl = cls_of[key]; images.append(g)
    if cl == odd: m1 += 1
    degs[deg_of[key]] += 1
    # injectivity: restriction recovers pf
    if tuple(g[C.vid(2 * x, 2 * y)] for x in range(3) for y in range(3)) != tuple(pf[P.vid(x, y)] for x in range(3) for y in range(3)): inj_ok = False
print("E6 (T) under R2, T(3,3) -> T(6,6)")
print(f"  R2 total (non-partial): {240 - partial}; partial: {partial}; injective by restriction: {inj_ok}")
print(f"  ★ m1 = images in the ODD class: {m1} / {240 - partial}   (prediction 0; null 0.036)")
print(f"  deg of images: {dict(degs)}")
# R1 fibre counts: for each canonical rep of the child, its parent restriction; count fibres over raw parents via S4? Do raw: enumerate all 7.3M? Use reps x 24 permutations.
fib = Counter(); fib_odd = Counter()
perms = list(itertools.permutations(range(4)))
for h, r in zip(reps, R):
    g = list(bytes.fromhex(h))
    for p in perms:
        gp = [p[c] for c in g]
        par = tuple(gp[C.vid(2 * x, 2 * y)] for x in range(3) for y in range(3))
        fib[par] += 1
        if r['cls'] == odd: fib_odd[par] += 1
print(f"  R1 fibre sizes over the 240 raw parents: min {min(fib.values())} max {max(fib.values())} mean {sum(fib.values())/240:.1f} (total {sum(fib.values())})")
print(f"  parents whose fibre meets the odd class: {len(fib_odd)} / 240; odd-class members per such parent: {sorted(Counter(fib_odd.values()).items())}")
json.dump({"m1": m1, "partial": partial, "deg_images": dict(degs), "fibre_sizes": sorted(fib.values()), "parents_meeting_odd": len(fib_odd), "images": images}, open(os.path.join(HERE, ".e6_T_R2_images.json"), "w"))
print(f"  [{time.time()-t0:.0f}s]")
