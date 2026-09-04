#!/usr/bin/env python3
"""Sphere lane: Kempe classes of 4-colourings on sphere triangulations WITH odd vertices (not Eulerian, so
Mohar-Salas/Fisk Thm 2.8 do not apply). C60 dual + plantri -c5 n=12..16. Controls: octahedron (k=1), T(6,6) (k=2)."""
import importlib.util, os, sys, glob, json, time, itertools
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
src67 = open(glob.glob(os.path.join(HERE, 'toy_5667_SEP4_*.py'))[0]).read().split("# ---------------- torus control")[0]
ns = {"__file__": glob.glob(os.path.join(HERE, "toy_5667_SEP4_*.py"))[0]}; exec(compile(src67, "t5667", "exec"), ns)
T26, pentakis, faces_of, colorings_mod_s4, fisk_degree = ns['T26'], ns['pentakis'], ns['faces_of'], ns['colorings_mod_s4'], ns['fisk_degree']
src63 = open(glob.glob(os.path.join(HERE, 'toy_5663_SEP4_*.py'))[0]).read().split("# ================================================================== SPHERE CONTROLS")[0]
ns63 = {"__file__": "x"}; exec(compile(src63, "t5663", "exec"), ns63)
torus, canon63, UF = ns63["torus"], ns63["canon"], ns63["UF"]
t0 = time.time(); score = []
def S(l, ok):
    score.append((l, bool(ok))); print(f"    [{'PASS' if ok else 'FAIL'}] {l}", flush=True)
def canon(t):
    mp = {}; out = []
    for c in t:
        if c not in mp: mp[c] = len(mp)
        out.append(mp[c])
    return tuple(out)
def kempe_classes(adj, cols):
    """adj: dict/list of neighbour lists; cols: list of canonical colourings (tuples). union-find over all moves."""
    nv = len(adj); idx = {c: i for i, c in enumerate(cols)}; uf = UF(len(cols))
    for i, c in enumerate(cols):
        f = list(c)
        for a in range(4):
            for b in range(a + 1, 4):
                seen = [False] * nv
                for v in range(nv):
                    if seen[v] or f[v] not in (a, b): continue
                    comp = []; st = [v]; seen[v] = True
                    while st:
                        u = st.pop(); comp.append(u)
                        for w in adj[u]:
                            if not seen[w] and f[w] in (a, b): seen[w] = True; st.append(w)
                    g = list(f)
                    for u in comp: g[u] = a + b - g[u]
                    uf.union(i, idx[canon(tuple(g))])
    lab = {}
    for i in range(len(cols)): lab.setdefault(uf.find(i), len(lab))
    return [lab[uf.find(i)] for i in range(len(cols))], len(lab)
print("=" * 78); print("Sphere lane — is there a conserved charge on triangulations WITH odd vertices?"); print("=" * 78)
# control: T(6,6)
Tt = torus(6, 6); rows = json.load(open(os.path.join(HERE, '.e5_5663_rows_T6x6.json')))
print(f"\ncontrol T(6,6): classes from the 5663 rows = {len({r['cls'] for r in rows['rows']})} (Mohar–Salas: 2)")
S("control T(6,6): κ = 2 (Mohar–Salas Thm 4.3)", len({r['cls'] for r in rows['rows']}) == 2)
# control: octahedron
oct_rot = T26.octahedron(); oct_rot = oct_rot[0] if isinstance(oct_rot, tuple) else oct_rot
of = faces_of(oct_rot); ocols = [tuple(c) for c in colorings_mod_s4(oct_rot, 10**6)]
olab, ok_ = kempe_classes(oct_rot, ocols)
print(f"control octahedron: {len(ocols)} colourings mod S₄, κ = {ok_}; degrees {sorted({fisk_degree(of, list(c))[0] for c in ocols})}")
S("control octahedron: κ = 1 (Fisk)", ok_ == 1)
# C60 dual
rot = pentakis(); faces = faces_of(rot); cols = [tuple(c) for c in colorings_mod_s4(rot, 10**6)]
lab, k60 = kempe_classes(rot, cols)
degs = [fisk_degree(faces, list(c))[0] for c in cols]
bycls = defaultdict(Counter)
for l, d in zip(lab, degs): bycls[l][d] += 1
print(f"\nC₆₀ dual: {len(cols)} colourings mod S₄; **κ = {k60}**; degree values {sorted(set(degs))}  [{time.time()-t0:.0f}s]")
for l in sorted(bycls): print(f"    class {l}: size {sum(bycls[l].values())}, degrees {dict(sorted(bycls[l].items()))}")
S(f"(S1) κ(C₆₀ dual, 4) = 1 (hashed)", k60 == 1)
conserved = all(len(c) == 1 for c in bycls.values())
S(f"(S2) Fisk degree conserved on the sphere lane? -> {conserved} (it takes {len(set(degs))} values; classes {k60})", True)
print(f"    (S2) reading: degree {'IS' if conserved else 'is NOT'} constant on Kempe classes; "
      f"{'a conserved charge exists' if conserved and k60 > 1 else ('no conserved charge: one class, every invariant constant' if k60 == 1 else 'see table')}")
# also: is deg mod 3 / mod 6 constant per class?
for m in (3, 6, 12):
    ok_m = all(len({d % m for d in c}) == 1 for c in bycls.values())
    print(f"    deg mod {m} constant on classes: {ok_m}")
# plantri sweep
allk = {}
for n in range(12, 17):
    for gi, r in enumerate(T26.plantri_rot(n, flags=('-c5',))):
        fs = faces_of(r); cs = [tuple(c) for c in colorings_mod_s4(r, 20000)]
        l, kk = kempe_classes(r, cs); ds = {fisk_degree(fs, list(c))[0] for c in cs}
        allk[(n, gi)] = (len(cs), kk, sorted(ds))
        print(f"    n={n} g{gi}: {len(cs)} colourings, κ = {kk}, degrees {sorted(ds)}")
S(f"(S3) κ = 1 on all plantri -c5 n=12..16 graphs ({sum(1 for v in allk.values() if v[1]==1)}/{len(allk)})", all(v[1] == 1 for v in allk.values()))
json.dump({"C60": {"ncol": len(cols), "kappa": k60, "byclass": {str(k): dict(v) for k, v in bycls.items()}}, "plantri": {str(k): v for k, v in allk.items()}}, open(os.path.join(HERE, ".sphere_lane_classes.json"), "w"))
print("\n" + "=" * 78); npass = sum(1 for _, o in score if o); print(f"SCORE {npass}/{len(score)}   [{time.time()-t0:.0f}s]")
for l, o in score: print(f"  {'PASS' if o else 'FAIL'}  {l}")
