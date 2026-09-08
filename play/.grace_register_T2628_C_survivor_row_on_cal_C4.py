#!/usr/bin/env python3
"""Grace — Round 134 G1 (second half): on Cal C4 (the Schur decision, K1882-PRE-A), register Lyra's (C) SURVIVOR ROW — a DISTRIBUTION on j —
(R132 L1 row (C), hashed 5ec93534) together with R131 L2's bulk-point paragraph (hashed 8118dd80) as its transport clause, in the DISTRIBUTION category.
Usage: python3 .grace_register_T2628_C_survivor_row_on_cal_C4.py --cal-word "§9xx C4, hh:mm" [--ruling "(C)"|"(D)"|"both"]
If Cal's C4 rules for (D) instead, this script REFUSES (the (D) row would be a different object — a subspace — and needs its own text); it registers only the (C) row.
Edges: T2626 -> T2628 (bulk point, not boundary); T2627 -> T2628 (the floor); T2628 -> T1292 (occupancy replaces the 10⁴); T2628 -> T633 (persistence half: j).
"""
import json, sys, os, glob, subprocess, datetime
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); a = sys.argv[1:]
if '--cal-word' not in a: print('REFUSED: --cal-word required (Cal C4, the Schur decision)'); sys.exit(1)
cw = a[a.index('--cal-word') + 1]; ruling = a[a.index('--ruling') + 1] if '--ruling' in a else '(C)'
if ruling.strip() == '(D)': print('REFUSED: C4 ruled (D); this script carries only the (C) distribution row'); sys.exit(1)
if not glob.glob(os.path.join(here, '.claims', 'theorem_T2628_*')): print('REFUSED: no claim file'); sys.exit(1)
today = datetime.date.today().isoformat(); ts = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); tid, tid_s = 2628, 'T2628'
F = sorted(glob.glob(os.path.join(root, 'notes', 'Lyra_R132_L1_two_survivor_rows*.md')))[-1]; T = open(F, encoding='utf-8').read().split('\n')
rowC = next(l for l in T if l.startswith('**Row (C)')).strip().replace('|', '∣')
G = sorted(glob.glob(os.path.join(root, 'notes', 'Lyra_R131_L1_Three_Sector*.md')))[-1]; U = open(G, encoding='utf-8').read().split('\n')
bulk = next(l for l in U if l.startswith('**The bulk-point survivor')).strip().replace('|', '∣'); transport = next(l for l in U if l.startswith('**Transport to a bulk point')).strip().replace('|', '∣')
name = 'THE (C) SURVIVOR ROW — a DISTRIBUTION on the winding count j (Lyra R132 L1 row (C), hashed 5ec93534; R131 L2 bulk-point survivor + transport, hashed 8118dd80; Cal C4 Schur decision): the reset acts on states by the SO(5)-covariant twirl then the classical marginal forgetting k; output p(j), no phases, no amplitudes, no axis; at a bulk point the vector survivor is the Hardy space of the time circle in w = z·z, zero at the boundary'
plain = ('What survives a reset is a probability table over one whole number: how many times the clock wound. No direction, no phase. Seen from inside the domain, that table lives on the Hardy space of a single circle, the time circle, and the same circle is found at every interior point; at the boundary there is nothing left at all.')
row = ('| T2628 | ' + name.split(' (Lyra')[0] + ' (registered ' + ts + ' ' + today + ' on Cal C4 ' + cw + ', ruling ' + ruling + '; DISTRIBUTION category). ' + rowC + ' BULK-POINT SURVIVOR (R131 L2, the vector form at a bulk point — the object the distribution is the twirl of): ' + bulk + ' ' + transport
       + ' THE THREE HYPOTHESES, STATED AS HYPOTHESES (Cal §919 C4 / §922): (a) the reset is SO(5)-covariant — it uses no input the substrate does not supply; (b) it posits no measurement and is linear on states — K1860-P\'s isometry class; no collapse row exists in the corpus; (c) it erases angular content — its output is SO(5)-invariant, which is the DEFINITION of "reset" (R131). Cal C4 caught that K1882-PRE-A\'s Schur note smuggled (c) into the word "lawful" (K1883 §3, owned by Keeper): (c) is a definition, not a law. THE VECTOR THEOREM (given (a)(b)(c)): no initialization VECTOR is lawful — a linear covariant map from any angular block H_k, k ≥ 1, to the invariants is zero (Schur); the lawful survivor is a STATE, a distribution on the winding count, measured 4.02 / 10.16 / 12.15 bits (5726). The (D) branch stays in Lyra\'s R132 file as the mathematics of the UNPOSITED branch (T2625 intact); a surviving direction would be a new Born row at the nucleation, colliding with K1860-P — not a choice between rows; the fork was EMPTY on every number (Rounds 132–134), not decided.'
       + ' What can fail: occupancy against capacity only (5725/5726); the vector form of (C) is EMPTY (5726 P1). Inputs: T2626, T2627. | DERIVED (the twirl and the marginal are theorems; the choice of (C) over (D) is Cal C4\'s ruling on the Schur note, ' + cw + '); the bits MEASURED | graph-node (substrate lane) | 5725, 5726, 5727 | ' + today + ' |')
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8')); ids = {t['tid'] for t in gd['theorems']}
if tid in ids: print('already registered'); sys.exit(0)
if 2627 not in ids: print('REFUSED: T2627 (the floor) is not registered yet — register the floor first (C3)'); sys.exit(1)
L = open(reg, encoding='utf-8').read().split('\n'); anchor = max(i for i, l in enumerate(L) if l.startswith('| T2627 |')); L.insert(anchor + 1, row); open(reg, 'w', encoding='utf-8').write('\n'.join(L))
rec = dict(tid=tid, name=name, domain='substrate_lane', status='DERIVED (twirl + marginal); category DISTRIBUTION on j; bits MEASURED (5726); Cal C4 ' + cw + ' ruling ' + ruling, depth=1, conflation=0, section='Lyra R132 L1 (C) / R131 L2; Cal C4', toys=[5725, 5726, 5727], date=today, plain=plain)
gd['theorems'].append(rec); gd['nodes'].append(dict(rec)); color = next((n.get('color') for n in gt['nodes'] if n.get('domain') == 'substrate_lane'), '#B05A5A')
gt['nodes'].append(dict(id=tid_s, name=name, domain='substrate_lane', domain_label='Substrate lane (record space)', status='derived', plain=plain, color=color, proofs=['SO(5)-covariant twirl on states', 'classical marginal forgets k', 'first fundamental theorem: invariants of one vector = z·z', 'Howe–Moore at the boundary (T2626)']))
for fr, to, lab in ((2626, tid, 'bulk point, not boundary'), (2627, tid, 'the floor: a distribution on j and nothing else lawful'), (tid, 1292, 'occupancy 4–12 bits replaces the 10⁴'), (tid, 633, 'the persistence half: j is what persists')):
    gd['edges'].append({'from': fr, 'to': to, 'source': 'derived', 'label': lab}); gt['edges'].append({'source': f'T{fr}', 'target': f'T{to}', 'type': 'uses'})
    for t_id in (fr, to):
        if not any(n['id'] == f'T{t_id}' for n in gt['nodes']):
            t = [x for x in gd['theorems'] if x['tid'] == t_id][0]; gt['nodes'].append(dict(id=f'T{t_id}', name=t['name'], domain=t['domain'], domain_label=t['domain'], status=str(t['status']).split(' ')[0].lower(), plain=t.get('plain', ''), color=color, proofs=[]))
ids.add(tid); gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=f'{today} both lists (Grace R134 G1)'); gd['meta']['max_tid'] = f'T{max(ids)}'; gd['meta']['last_updated'] = today
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
open(os.path.join(here, 'THEOREM_LOG.md'), 'a').write(f"| T2628 | The (C) survivor row: a distribution on j (twirl then forget k); bulk-point vector survivor = Hardy space of the time circle | D1 | Lyra R132 L1 (C) + R131 L2; Cal {cw} | 5725–5727 | Lyra (text) / Grace (registered) | {today} | derived |\n")
for cf in glob.glob(os.path.join(here, '.claims', 'theorem_T2628_*')): open(cf, 'a').write(f'Registered: {today} {ts} on Cal\'s word ({cw})\n')
ids2 = {t['tid'] for t in gd['theorems']}; gids = {n['id'] for n in gt['nodes']}
print('registered T2628 |', len(gd['theorems']), len(gd['edges']), '| dangling:', [e for e in gd['edges'] if e['from'] not in ids2 or e['to'] not in ids2], [e for e in gt['edges'] if e['source'] not in gids or e['target'] not in gids])
