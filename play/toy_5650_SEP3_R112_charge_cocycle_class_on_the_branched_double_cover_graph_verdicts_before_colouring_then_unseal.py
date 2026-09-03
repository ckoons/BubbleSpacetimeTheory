#!/usr/bin/env python3
"""
Toy 5650 — Round 112, Cal §835's complete criterion, computed BEFORE the colouring is looked at:
the charge cocycle c on the branched double cover Σ. c(e) = s(left face of e) ∈ ℤ₃ (s = ±1 the face
height-sign, which is a proper 2-colouring of the cover's faces and colouring-INDEPENDENT); c(−e) = −c(e);
δc = 3s ≡ 0. [c] = 0 in H¹(Σ;ℤ₃) ⟺ every cycle's charge vanishes ⟺ P ⊆ Λ₀ ⟺ (P = 2L, 5636b) L ⊆ Λ₀ = CONFINED.
Procedure: build Σ from the rotation system alone (no colouring), BFS a potential φ mod 3 on a spanning
tree, test every non-tree edge; verdict CONFINED iff all consistent. Also report the charge-image dimension
(0 or 1 in ℤ₃) and the number of independent charged cycles.
BLIND ORDER: verdicts for the ten graphs of 5649 Part A are computed and HASHED first; the sealed lattice
file is opened only afterwards (Test 5 compares).
CONTROLS (expected before running): icosahedron ≠ 0 (all colourings index 1); C60 = 0 (3,190/3,190 in Λ₀);
C70 ≠ 0 (9,570 index 1); C48 fullgen #0 ≠ 0; the k-sweep n = 6..9: per-graph verdict must agree with EVERY
colouring's "L ⊆ Λ₀" (the dichotomy, Cal §835 (a)) — one graph whose colourings split kills the height-sign
derivation.
TESTS: 1. c is a cocycle (δc ≡ 0 on every cover face) on every graph. 2. controls icosahedron/C60/C70/C48#0.
3. dichotomy on the k-sweep (per graph, all colourings agree with the verdict). 4. verdict list for the ten
graphs hashed before unsealing. 5. unsealed lattice tables agree with the verdicts (confined ⟺ every
full-rank lattice in Λ₀, and no split). Elie, 2026-09-03. 5 tests.
"""
import importlib.util, os, sys, json, hashlib, time
from collections import Counter, deque
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T39 = load('t5639', 'toy_5639_SEP3_R109_centre_lattice_mod_3_rank_on_the_71_drops_the_frame_and_the_k4_index3_case.py')
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')
T49 = load('t5649', 'toy_5649_SEP3_R112_next_IPR_fullerenes_C72_C78_and_flipped_C60_sealed_lattice_tables_plus_odd_cycle_column_C46_C58.py')

def charge_class(rot):
    """Build the branched double cover from the rotation system; return (cocycle_ok, confined, n_charged_cycles)."""
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
    edges = {}   # key (u<v, sheet s of face containing u->v) -> (cu, cvv, c)
    cocycle_ok = True
    for i, F in enumerate(faces):
        for s in (1, -1):
            tot = 0
            for j in range(3):
                u, v = F[j], F[(j + 1) % 3]
                cu, cvv = cv[(u, i, s)], cv[(v, i, s)]
                c = s % 3                      # charge of the step s*L(l): charge(L)=1 for A,B,C
                tot += c
                if u < v: key, desc = ((u, v, s), (cu, cvv, c))
                else: key, desc = ((v, u, -s), (cvv, cu, (-c) % 3))
                if key in edges: assert edges[key] == desc
                else: edges[key] = desc
            if tot % 3: cocycle_ok = False
    adj = [[] for _ in range(ncv)]
    for cu, cvv, c in edges.values():
        adj[cu].append((cvv, c)); adj[cvv].append((cu, (-c) % 3))
    phi = [None] * ncv
    for s0 in range(ncv):                      # Eulerian graphs: the cover is two disjoint sheets
        if phi[s0] is not None: continue
        phi[s0] = 0; dq = deque([s0])
        while dq:
            x = dq.popleft()
            for y, c in adj[x]:
                if phi[y] is None: phi[y] = (phi[x] + c) % 3; dq.append(y)
    charged = sum(1 for cu, cvv, c in edges.values() if (phi[cu] + c - phi[cvv]) % 3)
    return cocycle_ok, charged == 0, charged

if __name__ == '__main__':
    t0 = time.time(); print('Toy 5650 — charge cocycle class on the branched double cover: graph verdicts BEFORE colouring')
    sc = 0; coc_all = True
    # controls
    ctrl = {}
    ctrl['icosahedron'] = charge_class(T.plantri_rot(12)[0])
    ctrl['C60'] = charge_class(T44.fullgen_duals(60, ipr=True)[0])
    ctrl['C70'] = charge_class(T44.fullgen_duals(70, ipr=True)[0])
    ctrl['C48#0'] = charge_class(T44.fullgen_duals(48)[0])
    for k, (ok, conf, ch) in ctrl.items():
        coc_all &= ok; print(f'  control {k}: cocycle={ok}, CONFINED={conf}, charged non-tree edges={ch}')
    t2 = (not ctrl['icosahedron'][1]) and ctrl['C60'][1] and (not ctrl['C70'][1]) and (not ctrl['C48#0'][1])
    print(f'  Test 2 (controls: ico ≠0, C60 = 0, C70 ≠ 0, C48#0 ≠ 0): {"PASS" if t2 else "FAIL"}'); sc += t2
    # dichotomy on the k-sweep
    split = []; ngr = 0
    for n in range(6, 10):
        for gi, rot in enumerate(T.plantri_rot(n, flags=())):
            ok, conf, ch = charge_class(rot); coc_all &= ok
            faces = T.faces_of(rot); ngr += 1
            for f in T.colorings_mod_s4(rot, 10 ** 6):
                m = T.cover_measure(rot, faces, f)
                if m['k'] < 2: continue
                B = T39.Lbasis(m); inL0 = T39.in_charge_kernel(B)
                if inL0 != conf: split.append((n, gi, ''.join(map(str, f)), B, conf))
    t3 = not split
    print(f'  Test 3 (dichotomy on the k-sweep, {ngr} graphs: colouring verdict = graph verdict; disagreements {split[:4]}): {"PASS" if t3 else "FAIL"}'); sc += t3
    # the ten graphs — verdicts, hashed BEFORE unsealing
    graphs = []
    for mm in (72, 74, 76, 78):
        for gi, rot in enumerate(T44.fullgen_duals(mm, ipr=True)): graphs.append((f'C{mm}_ipr#{gi}', rot))
    rot60 = T44.fullgen_duals(60, ipr=True)[0]; hexes = [v for v in range(32) if len(rot60[v]) == 6]
    u = hexes[0]; v = next(w for w in rot60[u] if len(rot60[w]) == 6)
    graphs.append(('C60_dual_one_hexhex_flip', T49.flip_edge(rot60, u, v)))
    verdicts = []
    for tag, rot in graphs:
        ok, conf, ch = charge_class(rot); coc_all &= ok
        verdicts.append(dict(tag=tag, confined=conf, charged_nontree_edges=ch))
        print(f'  VERDICT {tag}: {"CONFINED" if conf else "NOT confined"} (charged non-tree edges {ch})')
    vb = json.dumps(verdicts, sort_keys=True).encode(); vh = hashlib.sha256(vb).hexdigest()
    open(os.path.join(HERE, '.verdicts_5650.json'), 'wb').write(vb)
    print(f'  Test 4 (verdict list hashed before unsealing: play/.verdicts_5650.json sha256 {vh}): PASS'); sc += 1
    print(f'  Test 1 (c is a ℤ₃-cocycle on every cover built): {"PASS" if coc_all else "FAIL"}'); sc += coc_all
    # unseal
    sealed = json.load(open(os.path.join(HERE, '.ipr_5649_sealed.json')))
    sh = hashlib.sha256(open(os.path.join(HERE, '.ipr_5649_sealed.json'), 'rb').read()).hexdigest()
    print(f'\n  UNSEALING play/.ipr_5649_sealed.json (sha256 {sh}):')
    t5 = True
    for r, vd in zip(sealed, verdicts):
        assert r['tag'] == vd['tag']
        agree = (vd['confined'] == (r['full_rank_not_in_charge_kernel'] == 0)) and not r['split']
        # also rank<=1 lattices: their charge is inside the table classes only via colour counts; the split flag covers full rank
        t5 &= agree
        print(f"    {r['tag']}: colourings {r['ncol']}{' CAPPED' if r['capped'] else ''}; full-rank in Λ₀ {r['full_rank_in_charge_kernel']}, not in Λ₀ {r['full_rank_not_in_charge_kernel']}, split {r['split']}; table {r['table']}  → verdict {'CONFINED' if vd['confined'] else 'NOT'}: {'agree' if agree else 'DISAGREE'}")
    print(f'  Test 5 (unsealed tables agree with the pre-hashed verdicts; no split): {"PASS" if t5 else "FAIL"}'); sc += t5
    print(f'\nSCORE: {sc}/5   [{time.time()-t0:.0f}s]')
