#!/usr/bin/env python3
"""
Toy 5658 — Round 115 §2: THE FOURTH BLIND PREDICTION, RUN AFTER THE HASH. P6 (hashed 14:41, sha256
b95b1814…): confined ⟹ 6 | m, on every IPR fullerene dual C102 … C120 (fullgen ipr). Verdict per graph =
[c] = 0 on the branched double cover (toy 5651's instrument; no colouring). Also recorded per graph: N_p
(must be 0), |Aut(map)|, para pairs, meta pairs (5656's definitions) — for Lyra/Cal's derivation, not for
the score. Score: the table confined × (m mod 6); P6 PASSES iff the cells (confined, m ≡ 2) and
(confined, m ≡ 4) are empty; FAILS on one confined isomer at 6 ∤ m.
TESTS: 1. generator counts = Goedgebeur–McKay IPR table (102: 616, 104: 823, 106: 1233, 108: 1799, 110: 2355,
112: 3342, 114: 4468, 116: 6063, 118: 8148, 120: 10774) and degrees 5^12 6^(n-12), N_p = 0. 2. cocycle on
every cover. 3. P6. 4. the confined list and table rendered. Elie, 2026-09-03.
"""
import importlib.util, os, sys, json, hashlib, time
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')
T36 = load('t5636', 'toy_5636_SEP2_R108_what_distinguishes_the_71_dropping_colourings_on_the_nine_fullerene_duals_blind_discriminator_hunt.py')
T51 = load('t5651', 'toy_5651_SEP3_R113_class_census_without_colouring_c_class_and_tree_neutrality_C20_C60_all_and_IPR_C60_C100_sealed.py')
T56 = load('t5656', 'toy_5656_SEP3_R114_unseal_third_blind_prediction_P_para_vs_confined_IPR_C60_C100.py')
KNOWN_IPR = {102: 616, 104: 823, 106: 1233, 108: 1799, 110: 2355, 112: 3342, 114: 4468, 116: 6063, 118: 8148, 120: 10774}
MS = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else sorted(KNOWN_IPR)
AUT = os.environ.get('AUT5658', '1') == '1'

if __name__ == '__main__':
    t0 = time.time(); print('Toy 5658 — fourth blind prediction: confined ⟹ 6 | m on IPR C102..C120')
    rows = []; gen_ok = True; coc_ok = True
    for m in MS:
        gs = T44.fullgen_duals(m, ipr=True); n = m // 2 + 2
        if len(gs) != KNOWN_IPR.get(m, len(gs)): gen_ok = False
        conf = 0
        for gi, rot in enumerate(gs):
            deg = Counter(len(r) for r in rot)
            d5 = [v for v in range(n) if len(rot[v]) == 5]; d5s = set(d5)
            Np = sum(1 for v in d5 for w in rot[v] if w in d5s and w > v)
            if deg[5] != 12 or deg[6] != n - 12 or set(deg) - {5, 6} or Np != 0: gen_ok = False
            r = T51.cover_and_class(rot); coc_ok &= r['cocycle']
            p, mt = T56.para_meta(rot)
            aut = len(T36.map_automorphisms(rot)) if (AUT and r['class_zero']) else None   # Aut only on confined (cost)
            rows.append(dict(m=m, idx=gi, n=n, confined=r['class_zero'], charged=r['charged_nontree'], para=p, meta=mt, aut=aut,
                             neutral_all=r['neutral_all_roots']))
            conf += r['class_zero']
        print(f'  C{m} IPR: {len(gs)} isomers, confined {conf}  [{time.time()-t0:.0f}s]'); sys.stdout.flush()
    tab = Counter((r['confined'], r['m'] % 6) for r in rows)
    print('\n  TABLE confined × (m mod 6):')
    for c in (True, False):
        print(f'    {"confined    " if c else "not confined"}: m≡0: {tab[(c, 0)]:>6}  m≡2: {tab[(c, 2)]:>6}  m≡4: {tab[(c, 4)]:>6}')
    print('  confined by m: ' + ' · '.join(f'{m}: {sum(1 for r in rows if r["m"]==m and r["confined"])}/{sum(1 for r in rows if r["m"]==m)}' for m in MS))
    print('  CONFINED LIST (C_m #idx: para, meta, |Aut|): ' + ' · '.join(f"C{r['m']} #{r['idx']} ({r['para']}, {r['meta']}, {r['aut']})" for r in rows if r['confined']))
    kill = [(r['m'], r['idx']) for r in rows if r['confined'] and r['m'] % 6]
    t3 = not kill
    sc = int(gen_ok) + int(coc_ok) + int(t3) + 1
    print(f'\n  Test 1 (generator counts, degrees, N_p = 0): {"PASS" if gen_ok else "FAIL"}')
    print(f'  Test 2 (cocycle on every cover): {"PASS" if coc_ok else "FAIL"}')
    print(f'  Test 3 (P6: no confined isomer at 6 ∤ m; kills: {kill[:10]}): {"PASS — prediction held" if t3 else "FAIL — KILLED"}')
    print('  Test 4 (table rendered): PASS')
    blob = json.dumps(rows, sort_keys=True).encode(); h = hashlib.sha256(blob).hexdigest()[:16]
    open(os.path.join(HERE, '.p6_5658_rows.json'), 'wb').write(blob)
    print(f'  rows play/.p6_5658_rows.json sha256 {h} ({len(rows)} isomers)')
    print(f'\nSCORE: {sc}/4   [{time.time()-t0:.0f}s]')
