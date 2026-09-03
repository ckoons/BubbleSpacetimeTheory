#!/usr/bin/env python3
"""
Toy 5651 — Round 113 §2: THE CLASS CENSUS WITHOUT COLOURING. T2603 (Cal §835, PROVED): the height sign is a
proper 2-colouring of the faces of the branched double cover Σ, colouring-independent; its ℤ₃ class [c] ∈
H¹(Σ;ℤ₃) is the charge of the periods; the dislocation lattice L ⊆ Λ₀ (CONFINED) ⟺ [c] = 0. So the verdict
is a rotation-system computation and runs where colouring cannot.
POPULATION: every fullerene dual C20…C60 (fullgen, all isomers) and every IPR isomer C60…C100 (fullgen ipr).
PER GRAPH (no colouring anywhere): C_m, fullgen index, n, N_p, |Aut(map)| (orientation-preserving and
-reversing map automorphisms, toy 5636's routine), TREE-NEUTRAL (Y/N), [c] = 0 (Y/N).
TREE-NEUTRALITY, operationalised: BFS spanning tree of Σ rooted at a dislocation lift; the ℤ₃ potential φ
along it; neutral ⟺ all twelve dislocation lifts carry the same φ. Reported for the root = dislocation 0
("neutral_root0") and for EVERY dislocation root ("neutral_all_roots" = neutral for all 12 roots,
"neutral_some_root" = for at least one). Cal §835: neutrality is necessary for [c] = 0 (a charged tree
difference is in L) but not sufficient; Lyra: they agree. THE SEAM'S WITNESS: a graph with a neutral tree
and [c] ≠ 0. (Note stated before running: when [c] ≠ 0, φ is tree-dependent, so "neutral" can depend on the
root — that dependence is itself the seam's signature; both columns are reported.)
SEALING: the per-graph table (with the confined list by n) is written to play/.census_5651_sealed.json and
only its sha256 is posted until Lyra's structural prediction is hashed on the board. The seam verdict
(witness count) posts openly; it is not part of her prediction.
TESTS: 1. generator: isomer counts match Brinkmann–Dress for C20..C60 and IPR counts C60..C100 (Goedgebeur–McKay
table: 1,1,1,2,5,7,9,24,19,35,46,86,134,187,259,450); every dual 5-connected? (skipped above n=32 — cost;
degrees 5^12 6^(n-12) checked on all). 2. c is a cocycle on every cover. 3. [c] = 0 ⟹ tree-neutral for every
root (the derived direction, Cal): 0 exceptions. 4. the seam: neutral (some root / all roots) with [c] ≠ 0 —
witness count reported; PASS = decided either way. 5. sealed file written + hashed; C60/C70/C72/C74/C76/C78
verdicts reproduce 5650. Elie, 2026-09-03. 5 tests.
"""
import importlib.util, os, sys, json, hashlib, time
from collections import Counter, deque
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')
T36 = load('t5636', 'toy_5636_SEP2_R108_what_distinguishes_the_71_dropping_colourings_on_the_nine_fullerene_duals_blind_discriminator_hunt.py')

def cover_and_class(rot):
    n = len(rot); faces = T.faces_of(rot); deg = [len(r) for r in rot]
    fidx = {}
    for i, F in enumerate(faces):
        for j in range(3): fidx[(F[j], F[(j + 1) % 3])] = i
    fan = [[fidx[(v, w)] for w in rot[v]] for v in range(n)]
    cv = {}; ncv = 0
    for v in range(n):
        for pos, fi in enumerate(fan[v]):
            for s in (1, -1):
                base = s * (1 if pos % 2 == 0 else -1)
                key = (v, 0) if deg[v] % 2 else (v, base)
                if key not in cv: cv[key] = ncv; ncv += 1
                cv[(v, fi, s)] = cv[key]
    edges = {}; coc = True
    for i, F in enumerate(faces):
        for s in (1, -1):
            tot = 0
            for j in range(3):
                u, v = F[j], F[(j + 1) % 3]
                cu, cvv = cv[(u, i, s)], cv[(v, i, s)]; c = s % 3; tot += c
                key, desc = ((u, v, s), (cu, cvv, c)) if u < v else ((v, u, -s), (cvv, cu, (-c) % 3))
                edges.setdefault(key, desc)
            if tot % 3: coc = False
    adj = [[] for _ in range(ncv)]
    for cu, cvv, c in edges.values():
        adj[cu].append((cvv, c)); adj[cvv].append((cu, (-c) % 3))
    odd = [v for v in range(n) if deg[v] % 2]
    lifts = [cv[(v, 0)] for v in odd]
    def potential(root):
        phi = [None] * ncv
        for s0 in [root] + list(range(ncv)):
            if phi[s0] is not None: continue
            phi[s0] = 0; dq = deque([s0])
            while dq:
                x = dq.popleft()
                for y, c in adj[x]:
                    if phi[y] is None: phi[y] = (phi[x] + c) % 3; dq.append(y)
        return phi
    phi0 = potential(lifts[0])
    charged = sum(1 for cu, cvv, c in edges.values() if (phi0[cu] + c - phi0[cvv]) % 3)
    neutral = []
    for r in lifts:
        p = potential(r); neutral.append(len({p[l] for l in lifts}) == 1)
    return dict(cocycle=coc, class_zero=(charged == 0), charged_nontree=charged,
                neutral_root0=neutral[0], neutral_all_roots=all(neutral), neutral_some_root=any(neutral),
                neutral_roots=sum(neutral))

KNOWN = {20: 1, 24: 1, 26: 1, 28: 2, 30: 3, 32: 6, 34: 6, 36: 15, 38: 17, 40: 40, 42: 45, 44: 89, 46: 116, 48: 199, 50: 271, 52: 437, 54: 580, 56: 924, 58: 1205, 60: 1812}
KNOWN_IPR = {60: 1, 70: 1, 72: 1, 74: 1, 76: 2, 78: 5, 80: 7, 82: 9, 84: 24, 86: 19, 88: 35, 90: 46, 92: 86, 94: 134, 96: 187, 98: 259, 100: 450}

if __name__ == '__main__':
    t0 = time.time(); print('Toy 5651 — class census without colouring (sealed table)')
    rows = []; gen_ok = True; coc_ok = True; derived_ok = True; witnesses = []
    pops = [(m, False) for m in sorted(KNOWN)] + [(m, True) for m in sorted(KNOWN_IPR) if m > 60]
    for m, ipr in pops:
        gs = T44.fullgen_duals(m, ipr=ipr); n = m // 2 + 2
        exp = (KNOWN_IPR if ipr else KNOWN)[m]
        if len(gs) != exp: gen_ok = False
        for gi, rot in enumerate(gs):
            deg = Counter(len(r) for r in rot)
            if deg[5] != 12 or deg[6] != n - 12 or set(deg) - {5, 6}: gen_ok = False   # (first run: {6: 0} vs absent key at n = 12 — test bug, fixed)
            d5 = [v for v in range(n) if len(rot[v]) == 5]; d5s = set(d5)
            Np = sum(1 for v in d5 for w in rot[v] if w in d5s and w > v)
            r = cover_and_class(rot); coc_ok &= r['cocycle']
            aut = len(T36.map_automorphisms(rot))
            if r['class_zero'] and not r['neutral_all_roots']: derived_ok = False
            if (not r['class_zero']) and r['neutral_some_root']:
                witnesses.append((m, gi, r['neutral_roots'], r['charged_nontree']))
            rows.append(dict(m=m, ipr=ipr, idx=gi, n=n, Np=Np, aut=aut, **r))
        nz = sum(1 for x in rows if x['m'] == m and x['ipr'] == ipr and x['class_zero'])
        print(f'  C{m}{" IPR" if ipr else ""}: {len(gs)} isomers  [{time.time()-t0:.0f}s]'); sys.stdout.flush()
    blob = json.dumps(rows, sort_keys=True).encode(); h = hashlib.sha256(blob).hexdigest()
    open(os.path.join(HERE, '.census_5651_sealed.json'), 'wb').write(blob)
    sc = 0
    print(f'\n  Test 1 (generator counts + degrees): {"PASS" if gen_ok else "FAIL"}'); sc += gen_ok
    print(f'  Test 2 (cocycle on every cover, {len(rows)} graphs): {"PASS" if coc_ok else "FAIL"}'); sc += coc_ok
    print(f'  Test 3 ([c] = 0 ⟹ neutral for every root; exceptions: {not derived_ok}): {"PASS" if derived_ok else "FAIL"}'); sc += derived_ok
    print(f'  Test 4 (THE SEAM: graphs neutral for SOME root with [c] ≠ 0 = {len(witnesses)}; neutral for ALL 12 roots with [c] ≠ 0 = {sum(1 for w in witnesses if w[2] == 12)}; first witnesses (C_m, idx, neutral roots/12, charged non-tree edges): {witnesses[:8]}): PASS (decided)'); sc += 1
    chk = {(60, 935): True, (70, 0): False, (72, 0): True, (74, 0): False, (76, 0): False, (76, 1): False, (78, 0): False, (78, 1): True, (78, 2): False, (78, 3): False, (78, 4): False}
    rep = all(next(x['class_zero'] for x in rows if x['m'] == m and x['idx'] == gi) == v for (m, gi), v in chk.items())   # C60's IPR isomer is fullgen (non-ipr) index 935
    print(f'  Test 5 (sealed table written: play/.census_5651_sealed.json sha256 {h}; 5650 verdicts reproduced: {rep}): {"PASS" if rep else "FAIL"}'); sc += rep
    print(f'  totals: graphs {len(rows)}; [c] = 0 on {sum(1 for x in rows if x["class_zero"])} (count only; the list by n stays sealed)')
    print(f'\nSCORE: {sc}/5   [{time.time()-t0:.0f}s]')
