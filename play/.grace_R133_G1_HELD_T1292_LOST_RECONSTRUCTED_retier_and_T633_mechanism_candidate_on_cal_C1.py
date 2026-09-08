#!/usr/bin/env python3
"""Grace — Round 133 G1, HELD: re-tier T1292's LOST class ("traced out into the environment, not destroyed") and RECONSTRUCTED
("re-entered"), and annotate T633's reset clause with the Round 133 MECHANISM CANDIDATE while it stays POSITED.
Runs ONLY with --cal-word "<C1 §, time>". Refuses otherwise. Idempotent on the key 'R133 LOST/RECONSTRUCTED re-tier'.
The wording is the board's (CI_BOARD_ROUND_133 L2): "thermodynamic (angular, k) knowledge is not destroyed at the reset; it is traced out
into the beyond-horizon factor; topological (winding, j) knowledge is what the survivor factor keeps." The trap is carried in the text:
Stinespring exists for every channel, so "conserved globally" is a DEFINITION unless the environment is physical = its content can come back
(re-entry, Elie E2/E3). Until re-entry is measured the clause stays POSITED; this script annotates, it does not promote.
"""
import sys, json, subprocess, datetime
a = sys.argv[1:]
if '--cal-word' not in a: print('REFUSED: --cal-word required (Round 133 C1)'); sys.exit(1)
cw = a[a.index('--cal-word') + 1]; ts = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); today = datetime.date.today().isoformat()
KEY = 'R133 LOST/RECONSTRUCTED re-tier'
TAG = (f'[{KEY} — {ts} {today}, Grace R133 G1 on Cal C1 ({cw}); Keeper CI_BOARD_ROUND_133 L2; Lyra L1/L2 (dilation); Elie E1–E3: '
       'LOST (~10¹²² bits of spatial coordinates) is RE-TIERED from "no structural anchor / destroyed" to "TRACED OUT into the environment — the beyond-horizon factor of the reset\'s Stinespring dilation — not destroyed"; '
       'RECONSTRUCTED is re-read as "RE-ENTERED": bound states reform from permanent ingredients AND from whatever of the environment the new cycle reads back (re-entry fraction by degree, Elie E3). '
       'The reset is the one non-isometric step of a program whose law is Conservation of Knowledge (CKT); every channel is the marginal of an isometry, so the reset conserves knowledge GLOBALLY and the survivor is what one factor sees. '
       'TRAP CARRIED: the dilation exists for every channel, so "conserved globally" is a DEFINITION unless the environment is physical, i.e. its content can come back — the only can-fail content is RE-ENTRY (5731 rerun with write directions drawn from the traced-out angular density). '
       'The two environment dimensions are named, not merged: full L²(SO(5)) (the twirl\'s Haar Kraus form) vs minimal (dim H_k)² for one saturated block (Keeper control). T633\'s reset clause stays POSITED; this is its first MECHANISM CANDIDATE, not its mechanism.]')
reg = 'notes/BST_AC_Theorem_Registry.md'; L = open(reg, encoding='utf-8').read().split('\n'); n = 0
for i, l in enumerate(L):
    if KEY in l: continue
    if l.startswith('| T1292 |') or l.startswith('*Spatial Amnesia (T1292,'): L[i] = l.rstrip() + ' ' + TAG; n += 1
    elif l.startswith('| T633 |'): L[i] = l.rstrip() + ' ' + TAG.replace('LOST (~10¹²² bits', 'the clause "thermodynamic knowledge resets" gets its first MECHANISM CANDIDATE (angular content traced out into the beyond-horizon factor, not destroyed); T1292\'s LOST (~10¹²² bits'); n += 1
open(reg, 'w', encoding='utf-8').write('\n'.join(L)); print('registry rows tagged:', n)
p = 'notes/BST_T1292_Spatial_Amnesia.md'; t = open(p, encoding='utf-8').read()
if KEY not in t:
    t = t.replace('| LOST | Specific galaxy positions, cluster arrangements, void geometry, all spatial coordinates | Eigenvalue configurations of emergent space; no structural anchor | ~10¹²² bits |',
                  '| LOST → TRACED OUT (R133 re-tier, held until Cal C1: ' + cw + ') | Specific galaxy positions, cluster arrangements, void geometry, all spatial coordinates | Eigenvalue configurations of emergent space; no structural anchor INSIDE the new horizon — traced out into the beyond-horizon factor, not destroyed; re-entry is the can-fail | ~10¹²² bits (the environment\'s share) |')
    t = t.replace('| RECONSTRUCTED | Hydrogen atom', '| RECONSTRUCTED → RE-ENTERED (R133) | Hydrogen atom')
    j = t.find('\n', t.find('> **[SHAPE/STATE RE-TIER')) + 1; t = t[:j] + '\n> **' + TAG + '**\n' + t[j:]; open(p, 'w', encoding='utf-8').write(t); print('T1292 file tagged')
gp = 'play/ac_graph_data.json'; gd = json.load(open(gp, encoding='utf-8')); c = 0
for coll in ('theorems', 'nodes'):
    for x in gd[coll]:
        if x['tid'] == 1292 and KEY not in x['status']: x['status'] += f' — {KEY} {ts} {today} (Cal C1 {cw}): LOST = traced out into the beyond-horizon factor, not destroyed; RECONSTRUCTED = re-entered; re-entry is the can-fail'; c += 1
        if x['tid'] == 633 and KEY not in x['status']: x['status'] += f' — reset clause: first MECHANISM CANDIDATE {ts} {today} (angular content traced out, not destroyed; R133 L2; Cal C1 {cw}); still POSITED'; c += 1
json.dump(gd, open(gp, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); print('graph statuses:', c)
