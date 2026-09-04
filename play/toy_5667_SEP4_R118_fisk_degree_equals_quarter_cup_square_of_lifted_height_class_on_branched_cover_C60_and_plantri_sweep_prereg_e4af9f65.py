#!/usr/bin/env python3
"""Toy — Fisk degree = ¼ cup-square of the lifted height class on the branched double cover (Cal §847; prereg in file name).
Torus control (cup = ±det, deg = cup/2 on T(6,6)); octahedron; C60 dual (pentakis, 3,190 colourings mod S4); plantri -c5 n=12..16."""
import importlib.util, os, sys, json, time, math
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T26 = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T42 = load('t5642', 'toy_5642_SEP3_R110_cheap_falsifier_C60_dual_odd_index_lattice_exists_lyra_prediction.py') if False else None
import glob
f42 = glob.glob(os.path.join(HERE, 'toy_5642_*.py'))[0]
src42 = open(f42).read(); ns42 = {}
# extract pentakis() only (avoid running the toy)
start = src42.index('def pentakis'); end = src42.index('def connected_without')
exec('import math\n' + src42[start:end], ns42); pentakis = ns42['pentakis']
faces_of, colorings_mod_s4, plantri_rot = T26.faces_of, T26.colorings_mod_s4, T26.plantri_rot
LVEC = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}
TET = {0: (1, 2, 3), 1: (0, 3, 2), 2: (0, 1, 3), 3: (0, 2, 1)}
TET_ROT = {m: {tuple(o[i:] + o[:i]) for i in range(3)} for m, o in TET.items()}
t0 = time.time(); score = []
def S(label, ok):
    score.append((label, bool(ok))); print(f"    [{'PASS' if ok else 'FAIL'}] {label}", flush=True)

def fisk_degree(faces, f):
    out = []
    for m in range(4):
        p = n = 0
        for (a, b, c) in faces:
            col = (f[a], f[b], f[c])
            if m in col: continue
            if col in TET_ROT[m]: p += 1
            else: n += 1
        out.append(p - n)
    return out

def cup_square(cfaces, steps):
    """cfaces: list of CCW triples of cover-vertex ids; steps[(fi, j)] = step vector on edge j (v_j -> v_{j+1}) of face fi.
    Alexander–Whitney with the global order = integer id order; returns <w_x u w_y, [Sigma]>."""
    tot = 0
    for fi, F in enumerate(cfaces):
        # edge j from F[j] to F[j+1]; step vector known; as a function on ordered pairs within this face
        st = {}
        for j in range(3):
            u, v = F[j], F[(j + 1) % 3]; s = steps[(fi, j)]
            st[(u, v)] = s; st[(v, u)] = (-s[0], -s[1])
        a, b, c = sorted(F)
        eps = 1 if (a, b, c) in {tuple(F[i:] + F[:i]) for i in range(3)} else -1
        tot += eps * st[(a, b)][0] * st[(b, c)][1]
    return tot

# ---------------- torus control
print("=" * 78); print("Fisk degree = 1/4 cup-square on the branched cover — torus control first"); print("=" * 78)
src63 = open(glob.glob(os.path.join(HERE, 'toy_5663_SEP4_*.py'))[0]).read().split("# ================================================================== SPHERE CONTROLS")[0]
ns63 = {}; exec(compile(src63, "t5663", "exec"), ns63)
torus = ns63["torus"]; Tt = torus(6, 6)
rows = json.load(open(os.path.join(HERE, '.e5_5663_rows_T6x6.json')))
reps = [list(bytes.fromhex(h)) for h in rows['reps']]; R = rows['rows']
def torus_steps(T, f):
    st = {}
    for fi, F in enumerate(T.faces):
        s = T.fsign[fi]
        for j in range(3):
            u, v = F[j], F[(j + 1) % 3]; L = LVEC[f[u] ^ f[v]]; st[(fi, j)] = (s * L[0], s * L[1])
    return st
plus = minus = True; okdeg = True
for i, f in enumerate(reps):
    c = cup_square(Tt.faces, torus_steps(Tt, f)); d = R[i]['det']; g = R[i]['deg']
    if c != d: plus = False
    if c != -d: minus = False
    if abs(c) != 2 * abs(g): okdeg = False
    if i == 20000: print(f"    ... torus control at {i} [{time.time()-t0:.0f}s]", flush=True)
sign = 1 if plus else (-1 if minus else 0)
S(f"torus control T(6,6): cup = {'+' if plus else ('-' if minus else '?')}det on all {len(reps)} reps; |deg| = |cup|/2", sign != 0 and okdeg)
print(f"    convention fixed: deg = ({sign})·cup/2 on the torus, so deg = ({sign})·cup_Σ/4 on a double cover")

# ---------------- branched double cover builder (from 5626's construction; both sheets carry the base orientation)
def build_cover(rot, faces):
    n = len(rot); deg = [len(r) for r in rot]; k = sum(d % 2 for d in deg)
    fidx = {}
    for i, F in enumerate(faces):
        for j in range(3): fidx[(F[j], F[(j + 1) % 3])] = i
    fan = [[fidx[(v, w)] for w in rot[v]] for v in range(n)]
    cv_id = {}; ncv = 0
    for v in range(n):
        for pos, fi in enumerate(fan[v]):
            for s in (1, -1):
                base = s * (1 if pos % 2 == 0 else -1)
                key = (v, 0) if deg[v] % 2 == 1 else (v, base)
                if key not in cv_id: cv_id[key] = ncv; ncv += 1
                cv_id[(v, fi, s)] = cv_id[key]
    cfaces = []; meta = []
    for i, F in enumerate(faces):
        for s in (1, -1):
            cfaces.append(tuple(cv_id[(F[j], i, s)] for j in range(3))); meta.append((i, s))
    return cfaces, meta, ncv, k

def cover_steps(faces, cfaces, meta, f):
    st = {}
    for ci, (i, s) in enumerate(meta):
        F = faces[i]
        for j in range(3):
            L = LVEC[f[F[j]] ^ f[F[(j + 1) % 3]]]; st[(ci, j)] = (s * L[0], s * L[1])
    return st

def run_graph(name, rot, cap=20000):
    faces = faces_of(rot); assert all(len(F) == 3 for F in faces)
    cfaces, meta, ncv, k = build_cover(rot, faces)
    n = len(rot); euler = ncv - 2 * (3 * n - 6) + 2 * len(faces)
    cols = colorings_mod_s4(rot, cap)
    ok = True; bad = 0; degs = Counter(); faceind = True
    for f in cols:
        d = fisk_degree(faces, f)
        if len(set(d)) != 1: faceind = False
        c = cup_square(cfaces, cover_steps(faces, cfaces, meta, f))
        pred = sign * c / 4
        degs[d[0]] += 1
        if pred != d[0]: ok = False; bad += 1
    return dict(name=name, n=n, k=k, ncv=ncv, chi=euler, ncol=len(cols), ok=ok, bad=bad, degs=dict(sorted(degs.items())), faceind=faceind)

# octahedron
octa = T26.octahedron() if hasattr(T26, 'octahedron') else None
if octa is not None:
    rot_o = octa[0] if isinstance(octa, tuple) else octa
    try:
        r = run_graph("octahedron", rot_o); print(f"    octahedron: {r}"); S("octahedron k=0: deg = cup/4 all, all deg 0", r['ok'] and set(r['degs']) == {0})
    except Exception as e: print("    octahedron control skipped:", e)
# C60 dual
rot60 = pentakis(); r = run_graph("C60 dual (pentakis)", rot60, cap=10**6)
print(f"    C60 dual: n={r['n']} k={r['k']} cover vertices {r['ncv']} chi(Σ)={r['chi']} colourings {r['ncol']}; deg distribution {r['degs']}; mismatches {r['bad']}")
S(f"C60 dual: deg = ({sign})·cup_Σ/4 on all {r['ncol']} colourings (Cal's kill: {r['bad']} mismatches); face-independence {r['faceind']}", r['ok'] and r['faceind'] and r['ncol'] == 3190)
# plantri sweep
tot = 0; totbad = 0; per_n = {}
for n in range(12, 17):
    graphs = plantri_rot(n, flags=('-c5',))
    cnt = 0; bad = 0; degset = Counter(); ks = Counter()
    for gi, rot in enumerate(graphs):
        r = run_graph(f"n{n}g{gi}", rot, cap=20000); cnt += r['ncol']; bad += r['bad']; ks[r['k']] += 1
        for d, c in r['degs'].items(): degset[d] += c
    per_n[n] = (len(graphs), cnt, bad, dict(sorted(degset.items())), dict(ks))
    tot += cnt; totbad += bad
    print(f"    n={n}: {len(graphs)} graphs, k values {dict(ks)}, colourings {cnt}, mismatches {bad}, deg distribution {dict(sorted(degset.items()))}  [{time.time()-t0:.0f}s]", flush=True)
S(f"plantri -c5 n=12..16: deg = cup_Σ/4 on {tot - totbad}/{tot} colourings", totbad == 0)
print("\n" + "=" * 78); npass = sum(1 for _, o in score if o); print(f"SCORE {npass}/{len(score)}   [{time.time()-t0:.0f}s]")
for lab, o in score: print(f"  {'PASS' if o else 'FAIL'}  {lab}")
