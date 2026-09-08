#!/usr/bin/env python3
"""Grace — Round 133 G2: apply Lyra's citation pins to T2625/T2626 WHEN SHE DELIVERS THEM. Refuses without --pins-file.
The pins file is a JSON object mapping the flag-context to the pinned text, e.g.
 {"Stein–Weiss": "Thm III.2.3 (Stein–Weiss 1971, p. 93)", "Faraut–Korányi": "Ch. XIII §1", "Howe–Moore": "Howe & Moore, J. Funct. Anal. 32 (1979) 72–96, Thm 5.1", "Zimmer": "Thm 2.2.20 (p. 41)"}
Each key must occur in the row within 120 chars BEFORE a '[pin' flag; that flag alone is replaced by '[PINNED: <text>, Lyra <hash>]'.
Flags with no key stay as PIN OWED. Prints what changed and what is still owed; updates graph statuses when none remain.
"""
import sys, json, re, subprocess, datetime
a = sys.argv[1:]
if '--pins-file' not in a or '--lyra-hash' not in a: print('REFUSED: --pins-file <json> --lyra-hash <hash> required'); sys.exit(1)
pins = json.load(open(a[a.index('--pins-file') + 1])); h = a[a.index('--lyra-hash') + 1]
ts = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); today = datetime.date.today().isoformat()
reg = 'notes/BST_AC_Theorem_Registry.md'; L = open(reg, encoding='utf-8').read().split('\n'); owed = {}
for i, l in enumerate(L):
    if not (l.startswith('| T2625 |') or l.startswith('| T2626 |')): continue
    tid = l[2:7]; out = []; pos = 0
    for m in re.finditer(r'\[pin[^\]]*\]', l):
        ctx = l[max(0, m.start() - 120):m.start()]; key = next((k for k in pins if k in ctx), None)
        out.append(l[pos:m.start()]); out.append(f'[PINNED: {pins[key]}, Lyra {h} {ts} {today}]' if key else m.group(0)); pos = m.end()
        if not key: owed.setdefault(tid, []).append(ctx[-60:])
    out.append(l[pos:]); L[i] = ''.join(out)
    if tid not in owed: L[i] = L[i].replace('PIN OWED (Cal §911 condition 3', 'PINS APPLIED ' + ts + ' ' + today + ' (were PIN OWED, Cal §911 condition 3')
open(reg, 'w', encoding='utf-8').write('\n'.join(L))
gp = 'play/ac_graph_data.json'; gd = json.load(open(gp, encoding='utf-8'))
for coll in ('theorems', 'nodes'):
    for x in gd[coll]:
        if x['tid'] in (2625, 2626) and f'T{x["tid"]}' not in owed and 'PIN OWED' in x['status']: x['status'] = x['status'].replace('PIN OWED on the citations', f'citations PINNED by Lyra {h} {ts}')
json.dump(gd, open(gp, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('applied; still owed:', owed or 'none')
