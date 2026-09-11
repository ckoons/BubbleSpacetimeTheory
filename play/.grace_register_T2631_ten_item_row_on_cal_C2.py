#!/usr/bin/env python3
"""Grace — Round 142 (Keeper 13:05 list, item 3): FOUR registry edits in one pass, each named.
  (1) T2631 REGISTERED with Cal's C2 row text VERBATIM (notes/cal_R142_C2_the_ten_item_row_T2631_candidate_2026-09-11.md), T-next -> T2631.
  (2) T2543: strike the colour clause (Cal §946, ruled 09-09) + (c) the count now lives in T2631.
  (3) T2630: 'row isometry' -> 'spherical (column) isometry' (Lyra L2 3.2, Cal §950), registry + graph name/plain, dated.
  (4) T2545: second dated line scoping the Frobenius–Schur clause to SO(3); the 'not any SU(3) fundamental' reading withdrawn (Lyra L2 2.5, Cal §950).
Usage: python3 play/.grace_register_T2631_ten_item_row_on_cal_C2.py --cal-word "C2 12:56 / §950" — REFUSES without it.
"""
import json, sys, os, re, glob, subprocess, datetime, hashlib
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); a = sys.argv[1:]
if '--cal-word' not in a: print('REFUSED: --cal-word required'); sys.exit(1)
cw = a[a.index('--cal-word') + 1]
if not glob.glob(os.path.join(here, '.claims', 'theorem_T2631_*')): print('REFUSED: no claim file'); sys.exit(1)
today = datetime.date.today().isoformat(); ts = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip()
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
calf = os.path.join(root, 'notes', 'cal_R142_C2_the_ten_item_row_T2631_candidate_2026-09-11.md')
T = open(reg, encoding='utf-8').read()
assert T.count('\n| T2631 |') == 0, 'T2631 already present'

# ---- (1) Cal's row, verbatim, T-next -> T2631 ----
ct = open(calf, encoding='utf-8').read()
m = re.search(r'^\| T-next \| \*\*THE TEN-ITEM ROW.*?\| 2026-09-11 \|$', ct, re.M | re.S)
assert m, 'row not found in Cal C2 file'
row = m.group(0).replace('| T-next |', '| T2631 |', 1).replace('(T-next)', '(T2631)').replace('T-next', 'T2631')
assert row.count('\n') == 0, 'row spans lines'
rowhash = hashlib.sha256(row.encode()).hexdigest()[:16]
row = row.replace(' | 2026-09-11 |', ' | 2026-09-11 (registered ' + ts + ' by Grace on Cal ' + cw + '; text verbatim from cal_R142_C2, sha256 ' + rowhash + ') |')
lines = T.split('\n'); i2630 = [k for k, l in enumerate(lines) if l.startswith('| T2630 |')]; assert len(i2630) == 1
lines.insert(i2630[0] + 1, row)
T = '\n'.join(lines)

# ---- (2) T2543 colour clause + (c) ----
old = 'mediator J_½=V₁₂=color carries neither;'
assert T.count(old) == 1
T = T.replace(old, 'mediator J_½=V₁₂ carries neither [the clause "= colour" STRUCK ' + today + ' ' + ts + ' by Grace on Cal §946 (ruled 09-09; strike owed since): the identification of V₁₂ with colour is WITHDRAWN — a numerical fit with one measured input, the bridge proved absent (5751); THEOREM AND TIER UNCHANGED, the fermion/boson split never used the word];')
old2 = 'Closes item 10 → QM-from-D_IV⁵ 10/10 (all Dirac–von Neumann axioms Derived/Structure-Derived)'
assert T.count(old2) >= 1
T = T.replace(old2, old2 + ' [ANNOTATED ' + today + ' (Cal C2 (c)): the ten-item COUNT now lives in T2631, each item at its own tier through four named posits; T2543 carries ITEM 10 ONLY; "10/10 derived" and "zero posits" are retired]', 1)

# ---- (3) T2630 row isometry -> spherical ----
i = [k for k, l in enumerate(T.split('\n')) if l.startswith('| T2630 |')]; assert len(i) == 1
lines = T.split('\n'); l = lines[i[0]]
n = l.count('row isometry')
l = l.replace('**the write tuple is a row isometry.**', '**the write tuple is a SPHERICAL (column) isometry** [one word corrected ' + today + ' ' + ts + ', Lyra L2 3.2 / Cal §950: Σ_u W_u*W_u = I is the column operator being isometric (Athavale); a ROW isometry would need W_i*W_j = δ_ij and Σ W_uW_u* = I, both false for commuting writes; K1860-P had "spherical" right; no consumer moves].')
l = l.replace('DEFECT of the row isometry', 'DEFECT of the spherical isometry')
assert 'row isometry' not in l, l.count('row isometry')
lines[i[0]] = l; T = '\n'.join(lines)

# ---- (4) T2545 second dated line ----
i = [k for k, l in enumerate(T.split('\n')) if l.startswith('| T2545 |')]; assert len(i) == 1
lines = T.split('\n'); l = lines[i[0]]
marker = ' | STRUCTURAL (Structure-Derived) | '
assert l.count(marker) == 1 and 'REASON-FIX 2026-09-11' in l
second = (' — [SECOND DATED LINE ' + today + ' ' + ts + ' (Grace, on Lyra L2 2.5 and Cal §950; NOT a revert): clause (ii) of the 12:44 reason-fix is SCOPED. Frobenius–Schur indicators belong to (group, representation) PAIRS; "FS = +1" is a statement about the SO(3)-representation on V₁₂ and is not a comparison with SU(3) — the colour triplet restricted to the SO(3) the geometry supplies IS the complexified vector (σ_fund∘ι = ρ|_SO(3)), and as a U(1)·SO(3)-representation ρ has charge +1 while ρ̄ has −1, so ρ ≇ ρ̄ until the time circle is discarded. The reading "so V₁₂ is not any SU(3) fundamental" is WITHDRAWN and replaced by: **V₁₂ carries the restriction of the colour triplet to the geometry\'s SO(3), and nothing in the geometry extends it** (the ONE obstruction: dimension, §946 (i), Elie 5751; the reality-type comparison describes the gap — the geometry counts to three and cannot orient the count — and is not a second wall). The (3,1) conclusion uses only clause (i), irreducibility over ℂ, and stands. Tier unchanged.]')
l = l.replace(marker, second + marker); lines[i[0]] = l; T = '\n'.join(lines)
open(reg, 'w', encoding='utf-8').write(T)
print('registry: T2631 inserted (row sha256 %s); T2543 clause struck + annotated; T2630 %d occurrence(s) corrected; T2545 second line' % (rowhash, n))

# ---- graphs ----
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8'))
name = 'THE TEN-ITEM ROW — the Dirac–von Neumann axioms recovered on H²(D_IV⁵), each at its own tier, with its dependencies named: seven derived, one proved-with-a-named-caveat, one structure-derived-on-a-posited-descent, one derived-through-a-posit; four posits named in the chains; "10/10 derived" and "zero posits" retired (Cal C2, §945/§947–§949)'
plain = 'Ten rules make ordinary quantum mechanics, and this program recovers all ten on its one space — but not all at the same strength. Seven are derived; one is proved with a caveat about a word; one rests on a step the program admits it assumes (going from five dimensions to four); one passes through an assumption about the rank. Four assumptions are named in the chains. So the honest sentence is "ten of ten recovered, at the tiers listed" — never "ten of ten derived with nothing assumed".'
rec = dict(tid=2631, name=name, domain='quantum_mechanics', status='COUNT OF RECOVERIES, not a tier: DERIVED ×7 (1,3,4,6,7,8,10) · PROVED-WITH-CAVEAT ×1 (5) · STRUCTURE-DERIVED ×1 (9, posited descent) · IDENTIFIED ×1 (2); registered verbatim from Cal C2 on ' + cw, depth=1, conflation=0, section='Cal R142 C2 / §945 / §947–§949', toys=[5054, 5747], date=today, plain=plain)
gd['theorems'].append(rec); gd['nodes'].append(dict(rec))
color = next((n.get('color') for n in gt['nodes'] if n.get('domain') == 'quantum_mechanics'), '#7B68EE')
gt['nodes'].append(dict(id='T2631', name=name, domain='quantum_mechanics', domain_label='Quantum Mechanics', status='count of recoveries (7 derived / 1 proved-with-caveat / 1 structure-derived / 1 identified)', plain=plain, color=color, proofs=['item-by-item tiers and dependencies in the row (Cal C2, verbatim)']))
for fr in (754, 753, 2543, 2545, 2564, 2629, 2630):
    gd['edges'].append({'from': fr, 'to': 2631, 'source': 'derived', 'label': 'input to the ten-item row (item ' + {754: '4', 753: '5', 2543: '10', 2545: '9', 2564: '9 (posited descent)', 2629: '8', 2630: '8'}[fr] + ')'})
    gt['edges'].append({'source': 'T%d' % fr, 'target': 'T2631', 'type': 'uses'})
# T2630 graph name/plain
for coll in (gd['theorems'], gd['nodes']):
    for x in coll:
        if x.get('tid') == 2630:
            x['name'] = x['name'].replace('the write tuple is a row isometry', 'the write tuple is a spherical (column) isometry')
            x['row_isometry_corrected'] = today + ' (Lyra L2 3.2 / Cal §950): spherical, not row'
for x in gt['nodes']:
    if x.get('id') == 'T2630':
        x['name'] = x['name'].replace('the write tuple is a row isometry', 'the write tuple is a spherical (column) isometry')
        x['proofs'] = [p.replace('row isometry', 'spherical isometry') for p in x.get('proofs', [])]
ids = {t['tid'] for t in gd['theorems']}
gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=today + ' both lists (Grace R142 T2631)'); gd['meta']['max_tid'] = 'T%d' % max(ids); gd['meta']['last_updated'] = today
open(gd_p, 'w', encoding='utf-8').write(json.dumps(gd, indent=1, ensure_ascii=False))
open(gt_p, 'w', encoding='utf-8').write(json.dumps(gt, indent=1, ensure_ascii=False))
gids = {n['id'] for n in gt['nodes']}
print('graphs: ac_graph_data', len(gd['theorems']), len(gd['nodes']), len(gd['edges']), '| curated', len(gt['nodes']), len(gt['edges']),
      '| dangling:', [e for e in gd['edges'] if e['from'] not in ids or e['to'] not in ids], [e for e in gt['edges'] if e['source'] not in gids or e['target'] not in gids],
      '| max', max(ids))
