#!/usr/bin/env python3
"""
Grace — E6 NULL GENERATOR (Round 118; Elie's design 840cf832; Cal §848). Unnumbered until it runs for the record.
Usage: python3 this.py m0 m1 [K=200]
  Draws K subsets S'_k of raw 4-colourings of T(6,6) with the same class mix as Elie's image set S: m0 from the deg-0 class
  (305,192 reps x 24 = 7,324,608 raw), m1 from the deg-6 class (46 reps x 24 = 1,104 raw), uniformly WITHOUT replacement within
  each class, seed 20260904 + k. Uniform over raw colourings of a class = uniform canonical rep x uniform colour permutation
  (S4 acts freely: 7,325,712 = 24 x 305,238). Class map from toy 5665's instrument (recomputed here, ~4 min).
  Output: .e6_null_subsets_T66.json with the K subsets (as raw colour tuples in T(6,6) vertex order x*6+y) and their sha256,
  posted BEFORE any WSK run. Elie runs WSK from u_{S'_k}.
"""
import sys, json, hashlib, random, itertools, importlib.util, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("t5665", glob.glob(os.path.join(HERE, "toy_5665_*.py"))[0]); T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
m0, m1 = int(sys.argv[1]), int(sys.argv[2]); K = int(sys.argv[3]) if len(sys.argv) > 3 else 200
N, nb, faces, left, idx = T.torus(6, 6)
cols = T.enum_canonical(nb, N)
cls = {}; k = 0
for c in cols:
    if c in cls: continue
    k += 1; cls[c] = k; q = [c]
    while q:
        x = q.pop()
        for (_, _, _, new) in T.kempe_moves(x, nb, N):
            y = T.canon(new)
            if y not in cls: cls[y] = k; q.append(y)
deg_of_class = {}
for c in cols: deg_of_class.setdefault(cls[c], abs(T.degree(c, faces)))
by = {0: [c for c in cols if deg_of_class[cls[c]] == 0], 6: [c for c in cols if deg_of_class[cls[c]] != 0]}
print(f"classes {k}: deg-0 reps {len(by[0])} (x24 = {24*len(by[0])} raw), deg-6 reps {len(by[6])} (x24 = {24*len(by[6])} raw)")
assert (len(by[0]), len(by[6])) == (305192, 46), "literature control failed"
perms = list(itertools.permutations(range(4)))
subsets = []
for kk in range(K):
    rng = random.Random(20260904 + kk); S = []
    for m, pool in ((m0, by[0]), (m1, by[6])):
        raw = set()
        while len(raw) < m:
            rep = pool[rng.randrange(len(pool))]; p = perms[rng.randrange(24)]
            raw.add(tuple(p[c] for c in rep))
        S.extend(sorted(raw))
    subsets.append(S)
out = {'m0': m0, 'm1': m1, 'K': K, 'seed_rule': '20260904 + k', 'vertex_order': 'x*6+y', 'subsets': subsets}
s = json.dumps(out, sort_keys=True); h = hashlib.sha256(s.encode()).hexdigest()
open(os.path.join(HERE, '.e6_null_subsets_T66.json'), 'w').write(s)
print(f"wrote {K} subsets of size {m0+m1} -> .e6_null_subsets_T66.json  sha256 {h[:16]}")
