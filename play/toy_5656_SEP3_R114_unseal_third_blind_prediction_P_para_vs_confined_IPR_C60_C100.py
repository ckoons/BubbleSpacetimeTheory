#!/usr/bin/env python3
"""
Toy 5656 — Round 114 §1: THE UNSEAL — the third blind prediction. Lyra's P-para (hashed 14:01, RUNNING_NOTES
75177, before the census 5651 was sealed at 14:00/14:01): an IPR fullerene's dual is CONFINED ⟺ no hexagon
carries two pentagons in PARA position (opposite; spoke separation 3 at the hexavalent vertex). Meta =
separation 2 (equivalently 4). Symmetry candidate (a proxy, Lyra says): confined ⟺ nontrivial Aut.
Per IPR isomer C60…C100 (C60 = fullgen non-ipr index 935; C70…C100 fullgen ipr): confined (from the sealed
census, sha256 8500f714…), # para pairs (hexavalent vertex u with apexes at spokes j, j+3), # meta pairs
(spokes j, j+2), |Aut(map)|. Tables: confined × para-free; confined × trivial Aut.
Pre-registered kills (Cal): a confined isomer WITH a para pair; an unconfined isomer WITHOUT one.
TESTS: 1. the sealed file's hash matches the posted one. 2. P-para: confined ⟹ para-free (0 exceptions).
3. P-para converse: para-free ⟹ confined (0 exceptions). 4. tables rendered. Elie, 2026-09-03.
"""
import importlib.util, os, sys, json, hashlib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')

def para_meta(rot):
    d5 = {v for v in range(len(rot)) if len(rot[v]) == 5}
    para = meta = 0
    for u in range(len(rot)):
        r = rot[u]
        if len(r) != 6: continue
        sp = [i for i, w in enumerate(r) if w in d5]
        for a in range(len(sp)):
            for b in range(a + 1, len(sp)):
                d = (sp[b] - sp[a]) % 6
                if d == 3: para += 1
                elif d in (2, 4): meta += 1
    return para, meta

if __name__ == '__main__':
    raw = open(os.path.join(HERE, '.census_5651_sealed.json'), 'rb').read()
    h = hashlib.sha256(raw).hexdigest(); rows = json.loads(raw)
    t1 = h.startswith('8500f7145257a5a789b9d0f150a0708d0330141be0959193709c0f1037ded513')
    print(f'Toy 5656 — UNSEAL. sealed file sha256 {h[:16]}… matches posted: {t1}')
    ipr = [r for r in rows if (r['ipr'] or (r['m'] == 60 and r['Np'] == 0))]
    cache = {}
    out = []
    for r in ipr:
        key = (r['m'], r['ipr'])
        if key not in cache: cache[key] = T44.fullgen_duals(r['m'], ipr=r['ipr'])
        p, mt = para_meta(cache[key][r['idx']])
        out.append(dict(m=r['m'], idx=r['idx'], confined=r['class_zero'], para=p, meta=mt, aut=r['aut'], Np=r['Np']))
    t2 = [o for o in out if o['confined'] and o['para'] > 0]
    t3 = [o for o in out if (not o['confined']) and o['para'] == 0]
    tab = Counter((o['confined'], o['para'] == 0) for o in out)
    sym = Counter((o['confined'], o['aut'] == 1) for o in out)
    print(f'\n  IPR isomers scored: {len(out)} (C60 + C70…C100)')
    print('  CONFINED isomers (C_m, idx, para, meta, |Aut|):')
    for o in out:
        if o['confined']: print(f"    C{o['m']} #{o['idx']}: para {o['para']}, meta {o['meta']}, |Aut| {o['aut']}")
    print(f'\n  2×2 confined × para-free: confined∧para-free {tab[(True, True)]} · confined∧has-para {tab[(True, False)]} · unconfined∧para-free {tab[(False, True)]} · unconfined∧has-para {tab[(False, False)]}')
    print(f'  2×2 confined × trivial Aut: confined∧|Aut|=1 {sym[(True, True)]} · confined∧|Aut|>1 {sym[(True, False)]} · unconfined∧|Aut|=1 {sym[(False, True)]} · unconfined∧|Aut|>1 {sym[(False, False)]}')
    byn = {}
    for o in out: byn.setdefault(o['m'], [0, 0]); byn[o['m']][0] += o['confined']; byn[o['m']][1] += 1
    print('  confined / IPR isomers by C_m: ' + ' · '.join(f'{m}: {c}/{t}' for m, (c, t) in sorted(byn.items())))
    print('  para-pair distribution on unconfined isomers: ' + str(dict(sorted(Counter(o['para'] for o in out if not o['confined']).items()))))
    print(f'  Test 1 (hash matches): {"PASS" if t1 else "FAIL"}')
    print(f'  Test 2 (confined ⟹ para-free; exceptions {t2}): {"PASS" if not t2 else "FAIL — KILL"}')
    print(f'  Test 3 (para-free ⟹ confined; exceptions {t3}): {"PASS" if not t3 else "FAIL — KILL"}')
    print('  Test 4 (tables rendered): PASS')
    json.dump(out, open(os.path.join(HERE, '.unseal_5656.json'), 'w'), indent=1)
    print(f'\nSCORE: {int(t1)+int(not t2)+int(not t3)+1}/4')
