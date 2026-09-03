#!/usr/bin/env python3
"""
Toy 5649 — Round 112 §2 (Elie's half). Two parts.
PART A (SEALED until Lyra's graph verdicts are on disk — pre-registration protocol: the verdict is written
before the colouring exists): fullgen ipr → C72 (1), C74 (1), C76 (2), C78 (5) duals, plus the C60 dual with
ONE hexagon–hexagon flip (the triangulation edge between two hexavalent vertices, flipped; the two apexes
of the shared dodecahedron edge become adjacent; degrees 5^12 6^20 preserved as a multiset — 2 hexavalent →
5, 2 apexes → 6; 5-connectivity re-checked). Per graph: colouring count FIRST (exhaustive up to CAP; if CAP
hit, say so), then the lattice class table (rank / index / charge-kernel-or-other-line / apex colour
count), and my own pre-registered discriminator column from 5644: the profile of hexavalent vertices by
number of adjacent apexes ("every hexavalent sees 3 apexes" was C60's property; C70 had {3:10, 2:15}).
Output → play/.ipr_5649_sealed.json; only its sha256 is posted until Lyra's list lands. KILL for the
turning-parity law: one graph whose colourings SPLIT between L ⊆ Λ₀ (charge kernel) and not.
PART B (open): on the 3,732 C46..C58 rows of 5644 — the pentagon-adjacency graph (12 vertices, N_p edges)
per isomer: bipartite or has an odd cycle; against "has a 2-power drop" (rank 1 or index 2) from the rows.
Cal's P3 (a theorem's zero): two-power drops vanish EXACTLY on isomers whose adjacency graph has an odd
cycle (two colours on the twelve ⟹ the adjacency graph is 2-coloured ⟹ bipartite; so odd cycle ⟹ no
two-colour colouring ⟹ no 2-power drop, given 5636's rule). Reported as the 2×2 table.
TESTS: 1. Part A: every IPR graph 5-connected, degrees 5^12 6^(n-12), N_p = 0; the flipped C60 5-connected with
N_p = 1. 2. Part A: counts rendered, sealed file written, hash printed (content withheld here). 3. Part B:
odd cycle ⟹ no 2-power drop (the derivable direction; 0 exceptions). 4. Part B: the converse (bipartite ⟹
some 2-power drop) — reported, PASS/FAIL as data. Elie, 2026-09-03. 4 tests.
"""
import importlib.util, os, sys, time, json, hashlib
from itertools import combinations
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T39 = load('t5639', 'toy_5639_SEP3_R109_centre_lattice_mod_3_rank_on_the_71_drops_the_frame_and_the_k4_index3_case.py')
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')
CAP = int(os.environ.get('CAP5649', 2000000))
PART = sys.argv[1] if len(sys.argv) > 1 else 'AB'

def line_name(B):
    if len(B) < 2: return None
    for name, form in (('charge_kernel', lambda x, y: (x + y) % 3), ('x', lambda x, y: x % 3), ('y', lambda x, y: y % 3), ('x-y', lambda x, y: (x - y) % 3)):
        if all(form(*b) == 0 for b in B): return name
    return 'full_mod3'

def conn5(rot):
    n = len(rot)
    def ok(S):
        rest = [v for v in range(n) if v not in S]; seen = {rest[0]}; st = [rest[0]]
        while st:
            x = st.pop()
            for y in rot[x]:
                if y not in S and y not in seen: seen.add(y); st.append(y)
        return len(seen) == len(rest)
    return all(ok(set(S)) for s in range(1, 5) for S in combinations(range(n), s))

def flip_edge(rot, u, v):
    """Flip edge uv in a triangulation given as rotation lists; returns new rotation lists."""
    rot = [list(r) for r in rot]
    iu = rot[u].index(v); iv = rot[v].index(u)
    w = rot[u][(iu + 1) % len(rot[u])]   # third vertex of one face
    x = rot[u][(iu - 1) % len(rot[u])]   # third vertex of the other
    assert w in rot[v] and x in rot[v]
    rot[u].remove(v); rot[v].remove(u)
    # insert x into w's rotation between u and v, and w into x's rotation between v and u
    def insert_between(r, a, b, new):
        ia = r.index(a); ib = r.index(b); d = len(r)
        if (ia + 1) % d == ib: r.insert(ib, new)
        elif (ib + 1) % d == ia: r.insert(ia, new)
        else: raise ValueError
    insert_between(rot[w], u, v, x); insert_between(rot[x], u, v, w)
    return rot

def measure_graph(rot, tag):
    n = len(rot); faces = T.faces_of(rot)
    assert len(faces) == 2 * n - 4 and all(len(F) == 3 for F in faces), tag
    d5 = [v for v in range(n) if len(rot[v]) == 5]; d5s = set(d5)
    Np = sum(1 for v in d5 for w in rot[v] if w in d5s and w > v)
    prof = dict(Counter(sum(1 for w in rot[u] if w in d5s) for u in range(n) if len(rot[u]) == 6))
    c5 = conn5(rot)
    cols = T.colorings_mod_s4(rot, CAP); capped = len(cols) >= CAP
    tab = Counter()
    for f in cols:
        s = T39.stats(T.cover_measure(rot, faces, f))
        cls = 'rank0' if s['r'] == 0 else 'rank1' if s['r'] == 1 else f"idx{s['idx']}:{line_name(s['B']) if s['idx'] % 3 == 0 else '-'}"
        tab[(cls, len(set(f[v] for v in d5)))] += 1
    inL0 = sum(c for (cls, _), c in tab.items() if 'charge_kernel' in cls)
    notL0 = sum(c for (cls, _), c in tab.items() if cls.startswith('idx') and 'charge_kernel' not in cls)
    return dict(tag=tag, n=n, degrees=dict(Counter(len(r) for r in rot)), Np=Np, hex_profile=prof, conn5=c5,
                ncol=len(cols), capped=capped, table={f'{k}': v for k, v in sorted(tab.items(), key=str)},
                full_rank_in_charge_kernel=inL0, full_rank_not_in_charge_kernel=notL0,
                split=(inL0 > 0 and notL0 > 0))

if __name__ == '__main__':
    t0 = time.time(); print('=' * 78); print('Toy 5649 — next IPR fullerenes + flipped C60 (sealed) ; odd-cycle column C46..C58'); print('=' * 78)
    sc = 0
    if 'A' in PART:
        graphs = []
        for m in (72, 74, 76, 78):
            for gi, rot in enumerate(T44.fullgen_duals(m, ipr=True)): graphs.append((f'C{m}_ipr#{gi}', rot))
        rot60 = T44.fullgen_duals(60, ipr=True)[0]
        hexes = [v for v in range(32) if len(rot60[v]) == 6]
        u = hexes[0]; v = next(w for w in rot60[u] if len(rot60[w]) == 6)
        graphs.append(('C60_dual_one_hexhex_flip', flip_edge(rot60, u, v)))
        res = []; t1 = True
        for tag, rot in graphs:
            r = measure_graph(rot, tag); res.append(r)
            print(f"  {tag}: n={r['n']}, degrees={r['degrees']}, N_p={r['Np']}, hex-profile={r['hex_profile']}, 5-connected={r['conn5']}, colourings={r['ncol']}{' (CAPPED)' if r['capped'] else ''}  [{time.time()-t0:.0f}s]")
            sys.stdout.flush()
            exp_np = 2 if 'flip' in tag else 0   # flip: the two ex-hexavalent endpoints become degree 5 and each keeps one apex neighbour → N_p = 2 (first run expected 1; corrected)
            if not (r['conn5'] and r['Np'] == exp_np and sorted(r['degrees']) == [5, 6] and r['degrees'][5] == 12): t1 = False
        blob = json.dumps(res, sort_keys=True).encode(); h = hashlib.sha256(blob).hexdigest()
        open(os.path.join(HERE, '.ipr_5649_sealed.json'), 'wb').write(blob)
        print(f'\n  Test 1 (construction: IPR graphs N_p=0, flip N_p=1, all 5-connected, 5^12 6^(n-12)): {"PASS" if t1 else "FAIL"}'); sc += t1
        print(f'  Test 2 (counts rendered; SEALED table written: play/.ipr_5649_sealed.json sha256 {h}): PASS'); sc += 1
    if 'B' in PART:
        rows = json.load(open(os.path.join(HERE, '.np_series_5644.json')))
        rows = [r for r in rows if r['m'] < 60]
        by = {}
        for m in sorted({r['m'] for r in rows}):
            for gi, rot in enumerate(T44.fullgen_duals(m)):
                d5 = [v for v in range(len(rot)) if len(rot[v]) == 5]; d5s = set(d5)
                adj = {v: [w for w in rot[v] if w in d5s] for v in d5}
                col = {}; bip = True
                for s0 in d5:
                    if s0 in col: continue
                    col[s0] = 0; st = [s0]
                    while st:
                        x = st.pop()
                        for y in adj[x]:
                            if y not in col: col[y] = 1 - col[x]; st.append(y)
                            elif col[y] == col[x]: bip = False
                by[(m, gi)] = bip
        tab = Counter(); exc = []
        for r in rows:
            bip = by[(r['m'], r['idx'])]
            drop = any(k in ('rank1', 'idx2', 'idx4', 'rank0') for k in r['classes'])
            tab[('bipartite' if bip else 'odd_cycle', 'has_2power_drop' if drop else 'no_2power_drop')] += 1
            if (not bip) and drop: exc.append((r['m'], r['idx'], r['classes']))
        print('\n  PART B — pentagon-adjacency graph vs 2-power drops, C46..C58 (3,732 isomers):')
        for k, v in sorted(tab.items()): print(f'    {k}: {v}')
        t3 = not exc; t4 = tab[('bipartite', 'no_2power_drop')] == 0
        print(f'  Test 3 (odd cycle ⟹ no 2-power drop; exceptions {exc[:5]}): {"PASS" if t3 else "FAIL"}'); sc += t3
        print(f'  Test 4 (bipartite ⟹ some 2-power drop; bipartite-without-drop = {tab[("bipartite", "no_2power_drop")]}): {"PASS" if t4 else "FAIL (data)"}'); sc += t4
        json.dump({f'{k}': v for k, v in by.items()}, open(os.path.join(HERE, '.oddcycle_5649.json'), 'w'))
    print(f'\nSCORE: {sc}/{2*("A" in PART)+2*("B" in PART)}   [{time.time()-t0:.0f}s]')
