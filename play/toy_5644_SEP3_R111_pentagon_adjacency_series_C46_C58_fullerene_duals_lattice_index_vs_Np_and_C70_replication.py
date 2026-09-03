#!/usr/bin/env python3
"""
Toy 5644 — Round 111 §2: THE PENTAGON-ADJACENCY SERIES — from a prediction to a law (Lyra states, Elie runs,
Cal pre-scores). Generator: fullgen (Brinkmann–Dress, shipped with plantri 5.8, compiled here from
tools/plantri58/fullgen.c) with "code 7" = planar_code of the DUAL (rotation order preserved), so the
join key is (C_m, fullgen output index). Population: all fullerene duals C46..C58 (n = m/2 + 2 = 25..31
vertices), then C70 IPR (n = 37) as the replication of C60.
Per colouring (all proper 4-colourings mod S4 of each dual, counted first): the centre lattice L =
span of dislocation height differences (toy 5626 cover_measure; P = 2L, 5636b): rank, index, rank mod 3,
rank mod 2, colours on the twelve. Per fullerene: N_p = number of adjacent pentagon pairs = edges between
degree-5 vertices of the dual.
PRE-REGISTERED (before the run; Lyra's finer statement not on disk at build):
  LAW (Lyra): index 1 occurs iff N_p > 0; with N_p = 0 every colouring has index 3 or rank ≤ 1.
  Strong form (S): N_p ≥ 1 ⟹ NO colouring has index divisible by 3.
  Weak form (W):  N_p ≥ 1 ⟹ SOME colouring has index 1.
  KILLS: an N_p > 0 dual with an index-3 colouring kills (S); an N_p > 0 dual with no index-1 colouring
  kills (W); an N_p = 0 dual (C70) with an index-1 colouring kills the LAW.
  Empty-confirmation map: rank-0 colourings (all twelve one colour) are construction-guaranteed only when
  the twelve are pairwise non-adjacent (IPR) AND the rest colours; on N_p > 0 duals they are impossible
  (two adjacent pentagon apexes cannot share a colour) — so "rank 0 appears only at N_p = 0" is guaranteed,
  not content. The content is the index-3 / index-1 split.
TESTS: 1. generator control: fullgen counts C46..C58 = 116/199/271/437/580/924/1205 (Brinkmann–Dress table);
  duals are 5-connected triangulations with degrees 5^12 6^(n-12). 2. C60 through fullgen (IPR) reproduces
  5642 (3,190 colourings; 1,200/40/1,950). 3. (S) on the series. 4. (W) on the series. 5. C70 replication:
  no index-1 colouring (the LAW at N_p = 0). Elie, 2026-09-03. 5 tests.
"""
import importlib.util, os, sys, time, json, hashlib, subprocess
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
FULLGEN = os.path.join(HERE, 'tools', 'plantri58', 'fullgen')
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T39 = load('t5639', 'toy_5639_SEP3_R109_centre_lattice_mod_3_rank_on_the_71_drops_the_frame_and_the_k4_index3_case.py')
MS = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else [46, 48, 50, 52, 54, 56, 58]
EXTRA = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [60, 70]

def fullgen_duals(m, ipr=False):
    args = [FULLGEN, str(m), 'code', '7'] + (['ipr'] if ipr else [])
    out = subprocess.run(args, capture_output=True).stdout
    hdr = b'>>planar_code le<<'
    i = out.find(hdr); assert i >= 0, out[:80]; i += len(hdr)
    gs = []
    while i < len(out):
        n = out[i]; i += 1
        if n == 0:
            n = int.from_bytes(out[i:i + 2], 'little'); i += 2
        rot = []
        for v in range(n):
            nb = []
            while True:
                w = out[i]; i += 1
                if w == 0: break
                nb.append(w - 1)
            rot.append(nb)
        gs.append(rot)
    return gs

def measure(rot):
    n = len(rot); faces = T.faces_of(rot)
    d5 = [v for v in range(n) if len(rot[v]) == 5]
    Np = sum(1 for v in d5 for w in rot[v] if w in set(d5) and w > v)
    cols = T.colorings_mod_s4(rot, 10 ** 8)
    tab = Counter()
    for f in cols:
        s = T39.stats(T.cover_measure(rot, faces, f))
        key = (s['r'], s['idx'], s['r3'])
        tab[(key, len(set(f[v] for v in d5)))] += 1
    return Np, len(cols), tab

if __name__ == '__main__':
    t0 = time.time(); print('=' * 78); print(f'Toy 5644 — pentagon-adjacency series: fullerene duals C{MS[0]}..C{MS[-1]} + {EXTRA}'); print('=' * 78)
    KNOWN = {20: 1, 24: 1, 26: 1, 28: 2, 30: 3, 32: 6, 34: 6, 36: 15, 38: 17, 40: 40, 42: 45, 44: 89, 46: 116, 48: 199, 50: 271, 52: 437, 54: 580, 56: 924, 58: 1205, 60: 1812}
    gen_ok = True; results = []
    S_ok = True; W_ok = True; law70 = True; c60_ok = None
    byNp = defaultdict(lambda: Counter())      # Np -> Counter of (index class) over colourings
    perF = defaultdict(lambda: Counter())      # Np -> Counter of per-fullerene verdict
    for m in MS + EXTRA:
        ipr = (m >= 60)
        gs = fullgen_duals(m, ipr=ipr)
        n = m // 2 + 2
        if not ipr and m in KNOWN and len(gs) != KNOWN[m]: gen_ok = False
        print(f'\n  C{m}{" IPR" if ipr else ""}: {len(gs)} fullerene duals, n = {n}  [{time.time()-t0:.0f}s]'); sys.stdout.flush()
        ncol_tot = 0
        for gi, rot in enumerate(gs):
            deg = Counter(len(r) for r in rot)
            if len(rot) != n or dict(deg) != {5: 12, 6: n - 12}: gen_ok = False
            Np, ncol, tab = measure(rot); ncol_tot += ncol
            idx_classes = Counter()
            for ((r, idx, r3), nc5), c in tab.items():
                cls = 'rank0' if r == 0 else 'rank1' if r == 1 else f'idx{idx}'
                idx_classes[cls] += c; byNp[Np][cls] += c
            has1 = idx_classes.get('idx1', 0) > 0; has3 = any(k.startswith('idx') and int(k[3:]) % 3 == 0 for k in idx_classes)
            perF[Np][('has_index1', has1)] += 1; perF[Np][('has_index3', has3)] += 1
            if Np > 0 and has3: S_ok = False
            if Np > 0 and not has1: W_ok = False
            if m == 70 and has1: law70 = False
            if m == 60: c60_ok = (ncol == 3190 and idx_classes == Counter({'rank0': 1200, 'rank1': 40, 'idx3': 1950}))
            results.append(dict(m=m, idx=gi, n=n, Np=Np, ncol=ncol, classes=dict(idx_classes),
                                table={f'{k}': v for k, v in tab.items()}))
            if gi < 3 or Np <= 2 or m >= 60:
                print(f'    C{m} #{gi}: N_p={Np}, colourings {ncol}, classes {dict(idx_classes)}')
        print(f'    C{m}: colourings total {ncol_tot}; N_p range {min(r["Np"] for r in results if r["m"]==m)}..{max(r["Np"] for r in results if r["m"]==m)}'); sys.stdout.flush()
    print('\n  BY N_p (colourings pooled over all fullerenes with that N_p) — class -> count:')
    for Np in sorted(byNp): print(f'    N_p={Np:>2}: {dict(sorted(byNp[Np].items()))}   fullerenes: has_index1 {perF[Np][("has_index1", True)]}/{perF[Np][("has_index1", True)]+perF[Np][("has_index1", False)]}, has_index3 {perF[Np][("has_index3", True)]}')
    sc = 0
    print(f'\n  Test 1 (generator: fullgen counts match Brinkmann–Dress; duals 5^12 6^(n-12)): {"PASS" if gen_ok else "FAIL"}'); sc += gen_ok
    print(f'  Test 2 (C60 via fullgen reproduces 5642: 3,190 = 1,200/40/1,950): {"PASS" if c60_ok else "FAIL"}'); sc += bool(c60_ok)
    print(f'  Test 3 (STRONG: N_p ≥ 1 ⟹ no index-3 colouring, every fullerene): {"PASS" if S_ok else "FAIL — killed"}'); sc += S_ok
    print(f'  Test 4 (WEAK: N_p ≥ 1 ⟹ some index-1 colouring, every fullerene): {"PASS" if W_ok else "FAIL — killed"}'); sc += W_ok
    print(f'  Test 5 (LAW at N_p = 0: C70 IPR has no index-1 colouring): {"PASS" if law70 else "FAIL — killed"}'); sc += law70
    blob = json.dumps(results, sort_keys=True).encode(); h = hashlib.sha256(blob).hexdigest()[:8]
    open(os.path.join(HERE, '.np_series_5644.json'), 'wb').write(blob)
    print(f'  rows play/.np_series_5644.json sha256 {h} ({len(results)} fullerenes)')
    print(f'\nSCORE: {sc}/5   [{time.time()-t0:.0f}s]')
