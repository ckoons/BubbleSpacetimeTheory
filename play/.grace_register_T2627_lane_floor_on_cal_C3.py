#!/usr/bin/env python3
"""Grace — Round 134 G1: register the substrate lane's NUCLEATION-SURVIVOR FLOOR (K1882 §5) as T2627 in the T2624 pattern, on Cal C3's word.
Usage: python3 .grace_register_T2627_lane_floor_on_cal_C3.py --cal-word "§9xx C3, hh:mm" [--amend amend.txt]
--amend: a text file whose contents are appended INSIDE the row as "CAL'S AMENDMENTS (C3): ..." — his amendments go into the text, as with T2624.
Edges (INPUT -> CONSEQUENCE): T2626 -> T2627 (Howe–Moore: no boundary nucleation); T2625 -> T2627 (norm |a−b|³); T2624 -> T2627 (the lane's first floor); T2627 -> T633 (the clause's mechanism candidate, definitional); T2627 -> T1292 (what the successor inherits).
"""
import json, sys, os, glob, subprocess, datetime
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); a = sys.argv[1:]
if '--cal-word' not in a: print('REFUSED: --cal-word required (Cal C3)'); sys.exit(1)
cw = a[a.index('--cal-word') + 1]; amend = open(a[a.index('--amend') + 1], encoding='utf-8').read().strip() if '--amend' in a else ''
if not glob.glob(os.path.join(here, '.claims', 'theorem_T2627_*')): print('REFUSED: no claim file'); sys.exit(1)
today = datetime.date.today().isoformat(); ts = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); tid, tid_s = 2627, 'T2627'
K = sorted(glob.glob(os.path.join(root, 'notes', 'Keeper_K1882_Round_133*.md')))[-1]; T = open(K, encoding='utf-8').read().split('\n')
i = next(i for i, l in enumerate(T) if l.startswith('## 5.')); para = next(l for l in T[i + 1:] if l.strip().startswith('*"')).strip().strip('*').replace('|', '∣')
name = 'NUCLEATION-SURVIVOR FLOOR of the substrate lane (Rounds 131–133, K1882 §5): a lawful reset is SO(5)-covariant; on vectors Schur kills every angular block, on states every covariant channel with invariant output factors through the twirl, so the reset is the trace channel on angular content and the successor inherits a probability distribution on the winding count (4.02 / 10.16 / 12.15 bits measured) and nothing else lawful; a direction lives one cycle boundary; re-entry is legible, not remembered'
plain = ('When a universe resets, the only thing the next one lawfully inherits is a tally of how many times the clock wound, as a probability distribution. Every direction in space is averaged away by the symmetry; a direction that is kept survives exactly one reset; and reading the averaged-away content back in helps a little and fades in six writes. Everything else the old universe knew about WHERE things were is gone from the successor\'s lawful state.')
row = ('| T2627 | THE NUCLEATION-SURVIVOR FLOOR — a boundary theorem of the substrate lane (K1882 §5, register on Cal C3\'s word with his amendments in the text; registered ' + ts + ' ' + today + '). ' + para
       + (' CAL\'S AMENDMENTS (C3, ' + cw + '): ' + amend.replace('|', '∣') if amend else '')
       + ' Witnesses: Elie 5726 P1 (the SO(5)-average of every saturated vector is zero), 5731 (axis weight 0.24 → 0.008 in six covariant writes), 5733 (re-entry lifts six-write weight to 0.109, not above ½; family flat from k ≈ 5, Cal\'s density instrument). Theorems inside: T2625 (three sectors; the ∣a−b∣³ norm), T2626 (no boundary nucleation). Inputs: T2624 (the lane\'s first floor). What it leaves open: the Schur decision between the two survivor rows (K1882-PRE-A, Cal C4) — the floor holds under either; T633\'s clause stays POSITED. | NEGATIVE (a floor with three witnesses); theorems inside DERIVED; bits MEASURED; clause POSITED; Cal ' + cw + ' | graph-node (substrate lane) | 5726, 5731, 5733 | ' + today + ' |')
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8')); ids = {t['tid'] for t in gd['theorems']}
if tid in ids: print('already registered'); sys.exit(0)
L = open(reg, encoding='utf-8').read().split('\n'); anchor = max(i for i, l in enumerate(L) if l.startswith('| T2626 |')); L.insert(anchor + 1, row); open(reg, 'w', encoding='utf-8').write('\n'.join(L))
rec = dict(tid=tid, name=name, domain='substrate_lane', status='NEGATIVE floor (three witnesses 5726/5731/5733); theorems inside DERIVED; bits MEASURED; clause POSITED; Cal ' + cw + '; K1882 §5', depth=0, conflation=0, section='K1882 §5 / Round 134 C3', toys=[5726, 5731, 5733], date=today, plain=plain)
gd['theorems'].append(rec); gd['nodes'].append(dict(rec)); color = next((n.get('color') for n in gt['nodes'] if n.get('domain') == 'substrate_lane'), '#B05A5A')
gt['nodes'].append(dict(id=tid_s, name=name, domain='substrate_lane', domain_label='Substrate lane (record space)', status='negative', plain=plain, color=color, proofs=['Schur on vectors (5726 P1)', 'covariant channel factors through the twirl', 'axis dies in six writes (5731)', 're-entry legible not remembered (5733)']))
for fr, to, lab in ((2626, tid, 'no boundary nucleation'), (2625, tid, 'three sectors; the |a−b|³ norm'), (2624, tid, 'the lane\'s first floor'), (tid, 633, 'the reset clause\'s mechanism candidate (definitional)'), (tid, 1292, 'what the successor inherits: a distribution on j')):
    assert fr in ids | {tid} and to in ids | {tid}
    gd['edges'].append({'from': fr, 'to': to, 'source': 'negative', 'label': lab}); gt['edges'].append({'source': f'T{fr}', 'target': f'T{to}', 'type': 'uses'})
    for t_id in (fr, to):
        if not any(n['id'] == f'T{t_id}' for n in gt['nodes']):
            t = [x for x in gd['theorems'] if x['tid'] == t_id][0]; gt['nodes'].append(dict(id=f'T{t_id}', name=t['name'], domain=t['domain'], domain_label=t['domain'], status=str(t['status']).split(' ')[0].lower(), plain=t.get('plain', ''), color=color, proofs=[]))
ids.add(tid); gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=f'{today} both lists (Grace R134 G1)'); gd['meta']['max_tid'] = f'T{max(ids)}'; gd['meta']['last_updated'] = today
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
open(os.path.join(here, 'THEOREM_LOG.md'), 'a').write(f"| T2627 | Nucleation-survivor FLOOR: the successor inherits a distribution on j and nothing else lawful; direction one cycle; re-entry legible not remembered | D0 | K1882 §5; Cal {cw} | 5726,5731,5733 | Keeper (text) / Grace (registered) | {today} | negative (floor) |\n")
for cf in glob.glob(os.path.join(here, '.claims', 'theorem_T2627_*')): open(cf, 'a').write(f'Registered: {today} {ts} on Cal\'s word ({cw})\n')
ids2 = {t['tid'] for t in gd['theorems']}; gids = {n['id'] for n in gt['nodes']}
print('registered T2627 |', len(gd['theorems']), len(gd['edges']), '|', len(gt['nodes']), len(gt['edges']), '| dangling:', [e for e in gd['edges'] if e['from'] not in ids2 or e['to'] not in ids2], [e for e in gt['edges'] if e['source'] not in gids or e['target'] not in gids])
