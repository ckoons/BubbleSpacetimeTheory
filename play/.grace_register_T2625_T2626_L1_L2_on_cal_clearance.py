#!/usr/bin/env python3
"""Grace — Round 132 G2: register L1 (Three-Sector Theorem) as T2625 and L2's LEMMA (No-Boundary-Nucleation, Howe–Moore) as T2626 on
Cal §909(5)'s clearance: "L1 (three sectors) and L2's Lemma (Howe–Moore) are independent of the choice and may register on their own once the
'two extensions' wording and the conjugate-tube-carries-no-state sentence are in." Both sentences are inserted below. The branch-dependent
survivor paragraph of L2 is NOT registered (Cal's §909(5) word withholds it until the reset is one map).
Usage: python3 .grace_register_T2625_T2626_L1_L2_on_cal_clearance.py --cal-word "§909(5), 09:15; §908 H1/H2 PASS"
Edges from = INPUT -> to = CONSEQUENCE: T2625 -> T2626 (the tube model + Hardy membership feed the lemma); T2626 -> T2624 (the floor's "no
nucleation on Š" sentence); T2625 -> the positive-time row if a T-row named 'positive time' exists (looked up at runtime; else no edge).
"""
import json, sys, os, glob, re, subprocess, datetime
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); a = sys.argv[1:]
if '--cal-word' not in a: print('REFUSED: --cal-word required'); sys.exit(1)
calword = a[a.index('--cal-word') + 1]
for t in ('T2625', 'T2626'):
    if not glob.glob(os.path.join(here, '.claims', f'theorem_{t}_*')): print('REFUSED: no claim file for', t); sys.exit(1)
today = datetime.date.today().isoformat(); stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip()
L = sorted(glob.glob(os.path.join(root, 'notes', 'Lyra_R131_L1_Three_Sector*')))[-1]; T = open(L, encoding='utf-8').read().split('\n')
l1 = next(l.strip().strip('*') for l in T if l.strip().startswith('*Three-Sector Theorem'))
i2 = next(i for i, l in enumerate(T) if l.startswith('## L2')); lemma = T[i2 + 1].strip() + ' ' + T[i2 + 2].strip()
assert lemma.startswith('**Lemma.**'), lemma[:40]
l1 = l1.replace('|', '∣'); lemma = lemma.replace('|', '∣')
# Cal's two required insertions
l1 = l1.replace('each boundary bounds exactly two bulks, and there is no third.', 'each boundary datum has exactly TWO HOLOMORPHIC EXTENSIONS available to it (into T_Ω or into T_{−Ω}, never both), the spacelike sector is NOT a bulk, and there is no third extension.')
l1 += ' THE CONJUGATE TUBE (Cal §907(3), §908 H4, required for registration): T_{−Ω} exists as GEOMETRY — the mirror sheet of the positive-time row is a real object of the tube model — and CARRIES NO STATE: the universe\'s state lies in H²₊ by the sector choice, which is the positive-time row\'s clause (i) and stays a POSIT (G is sector-blind; conjugation, the only map between the two bulks, is outside G — L3, Cal C2); so this theorem registers the three sectors and the two extensions, not a realized mirror sheet.'
lemma += ' CONSEQUENCE (Round 131 item 2, now proved): "keep what a boundary point\'s isotropy cannot distinguish" keeps the zero vector — not the vacuum, nothing; a Shilov-boundary point cannot host the nucleation; the nucleation point is a BULK point (the survivor at a bulk point is infinite-dimensional and degenerates to {0} as z₀ → Š — L2\'s transport paragraph, branch-independent in this clause). The conjugate tube carries no state (T2625). The survivor ROW itself (which invariants; (C) channel vs (D) projection) is NOT registered here — Cal §909(5): the reset must be stated as one map first.'
ROWS = {
 2625: dict(name='Three-Sector Theorem for D_IV^5 (Lyra L1, hashed 8118dd80; Cal §908 H1 PASS): L²(Š) = H²₊ ⊕ H²₋ ⊕ L²_sp by Fourier support in ±Ω̄ (Paley–Wiener for the tube over the light cone); each boundary datum has exactly two holomorphic extensions, the spacelike sector is not a bulk, and the three sectors are G-invariant because G preserves the cone; the conjugate tube is geometry and carries no state',
            plain='Split every function on the boundary of D_IV^5 by where its Fourier transform lives: inside the forward light cone, inside the backward one, or neither. The first two extend holomorphically into the domain and its mirror, one each; the third extends into nothing. So a boundary bounds exactly two bulks and no more, the symmetry group respects the split, and the mirror bulk is real geometry that holds no state in this theory.',
            row=l1, tier='DERIVED (Paley–Wiener for tube domains; Stein–Weiss Ch. III; Faraut–Korányi; Cal §908 H1 PASS with the two-extensions wording; §907(3) conjugate-tube sentence in)', toys=[], proofs=['Paley–Wiener (Stein–Weiss III.2)', 'G preserves the cone']),
 2626: dict(name='No-Boundary-Nucleation Lemma (Lyra L2, hashed 8118dd80; Cal §908 H2 PASS): the P-fixed vectors of H²(D_IV^5) for P the stabilizer of a Shilov-boundary point are {0}, by Howe–Moore; a boundary point cannot host the nucleation, the nucleation point is a bulk point',
            plain='The symmetry that fixes a point on the boundary is a big non-compact group. A theorem of Howe and Moore says that in a space like H² no nonzero vector can be fixed by such a group. So "keep whatever a boundary point cannot tell apart" keeps nothing at all; a fresh universe cannot be seeded on the boundary, only from a point inside.',
            row='| T2626 | NO-BOUNDARY-NUCLEATION LEMMA (Lyra L2, R131, hashed 8118dd80; Cal §908 H2 PASS; §909(5) clearance; registered ' + stamp + ' ' + today + '). ' + lemma, tier='DERIVED (Howe–Moore 1979; Zimmer Thm 2.2.20; H² irreducible; the two-line proof in the row)', toys=[], proofs=['Howe–Moore vanishing of matrix coefficients', 'P noncompact (dilations × SO(1,4)) ⋉ ℝ⁵']),
}
ROWS[2625]['row'] = '| T2625 | THREE-SECTOR THEOREM FOR D_IV⁵ (Lyra L1, R131, hashed 8118dd80; Cal §908 H1 PASS; §909(5) clearance; registered ' + stamp + ' ' + today + '). ' + l1
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8')); ids = {t['tid'] for t in gd['theorems']}
pos = next((t['tid'] for t in gd['theorems'] if 'positive time' in t['name'].lower() or 'positive-time' in t['name'].lower()), None)
lines = open(reg, encoding='utf-8').read().split('\n'); anchor = max(i for i, l in enumerate(lines) if l.startswith('| T2624 |'))
color = next((n.get('color') for n in gt['nodes'] if n.get('domain') == 'substrate_lane'), '#B05A5A')
for tid in (2625, 2626):
    if tid in ids: print('already', tid); continue
    R = ROWS[tid]
    lines.insert(anchor + 1, R['row'] + ' | ' + R['tier'] + ' | graph-node (substrate lane / positive-time row) | ' + (', '.join(map(str, R['toys'])) or '—') + ' | ' + today + ' |'); anchor += 1
    rec = dict(tid=tid, name=R['name'], domain='substrate_lane', status=R['tier'] + f'; Cal {calword}', depth=1, conflation=0, section='Round 131 L1/L2 (Lyra) / Round 132 G2', toys=R['toys'], date=today, plain=R['plain'])
    gd['theorems'].append(rec); gd['nodes'].append(dict(rec)); ids.add(tid)
    gt['nodes'].append(dict(id=f'T{tid}', name=R['name'], domain='substrate_lane', domain_label='Substrate lane (record space)', status='derived', plain=R['plain'], color=color, proofs=R['proofs']))
open(reg, 'w', encoding='utf-8').write('\n'.join(lines))
edges = [(2625, 2626, 'the tube model and Hardy membership feed the lemma'), (2626, 2624, 'the floor\'s sentence "a boundary point cannot host the nucleation"')]
if pos: edges.append((2625, pos, 'the two extensions = the two sheets of the positive-time row; the sector choice stays its posit (i)'))
for fr, to, lab in edges:
    if any(e['from'] == fr and e['to'] == to for e in gd['edges']): continue
    gd['edges'].append({'from': fr, 'to': to, 'source': 'derived', 'label': lab}); gt['edges'].append({'source': f'T{fr}', 'target': f'T{to}', 'type': 'uses'})
    if not any(n['id'] == f'T{to}' for n in gt['nodes']):
        t = [x for x in gd['theorems'] if x['tid'] == to][0]; gt['nodes'].append(dict(id=f'T{to}', name=t['name'], domain=t['domain'], domain_label=t['domain'], status=str(t['status']).split(' ')[0].lower(), plain=t.get('plain', ''), color=color, proofs=[]))
gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=f'{today} both lists (Grace R132 G2)'); gd['meta']['max_tid'] = f'T{max(ids)}'; gd['meta']['last_updated'] = today
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(os.path.join(here, 'THEOREM_LOG.md'), 'a') as f:
    f.write(f"| T2625 | Three-Sector Theorem for D_IV^5 (two holomorphic extensions; conjugate tube carries no state) | D1 | Lyra L1 R131; Cal {calword} | — | Lyra (text) / Grace (registered) | {today} | derived |\n| T2626 | No-Boundary-Nucleation Lemma (Howe–Moore; nucleation point is a bulk point) | D1 | Lyra L2 R131; Cal {calword} | — | Lyra (text) / Grace (registered) | {today} | derived |\n")
for cf in glob.glob(os.path.join(here, '.claims', 'theorem_T262[56]_*')): open(cf, 'a').write(f'Registered: {today} {stamp} on Cal\'s clearance ({calword})\n')
ids2 = {t['tid'] for t in gd['theorems']}; gids = {n['id'] for n in gt['nodes']}
print('registered T2625, T2626 |', len(gd['theorems']), len(gd['nodes']), len(gd['edges']), '|', len(gt['nodes']), len(gt['edges']), '| positive-time row:', pos)
print('edges:', [(e['from'], e['to']) for e in gd['edges'] if e['from'] in (2625, 2626) or e['to'] in (2625, 2626)])
print('dangling data:', [e for e in gd['edges'] if e['from'] not in ids2 or e['to'] not in ids2], '| curated:', [e for e in gt['edges'] if e['source'] not in gids or e['target'] not in gids])
