#!/usr/bin/env python3
"""Grace — Round 126: RE-REGISTRATION of T2622 as v2 on Cal §880's text (the reduction-rank dichotomy as hypothesis; p = 2 = T2621's case;
DERIVED for all odd p; instruments at 3 and 5 as checks). RUN ONLY AFTER E13 (Elie's direct count on Lyra's p = 5 lattice agrees with Cal's
hash 0961f9d3) AND Cal's C17 word on Lyra's v2 text.
Usage: python3 .grace_reregister_T2622_v2_on_cal_word.py --cal-word "§NNN, HH:MM" --row-file <Lyra v2 file> [--e13 "toy NNNN, hash"]
The v1 row text (registered 17:02 2026-09-06) is preserved under "SUPERSEDED v1" inside the new row; graph statuses/plain rewritten; the edge
T2621 -> T2622 relabelled "the p = 2 special case"; THEOREM_LOG gets a v2 line; the G19 table's rows are relabelled (rule's kernel = <1,3,3>-class
= b^2+bd+d^2+3a^2, comb pi/ln 3; <1,1,3> = the reduction-rank-2 CONTROL).
"""
import sys, os, re, json, glob, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); here = os.path.join(root, 'play'); a = sys.argv[1:]
def arg(k, d=None): return a[a.index(k) + 1] if k in a else d
calword = arg('--cal-word'); rowfile = arg('--row-file'); e13 = arg('--e13', 'Elie E13')
if not calword or not rowfile: print('REFUSED: --cal-word and --row-file required'); sys.exit(1)
stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); today = datetime.date.today().isoformat()
L = open(rowfile, encoding='utf-8').read().split('\n')
body = next((l.strip().strip('*') for l in L if l.strip().startswith('*Kernel-Swap') or l.strip().startswith('| T2622 |')), None)
if body is None: print('REFUSED: no T2622 paragraph (line starting *Kernel-Swap or | T2622 |) in', rowfile); sys.exit(1)
if body.startswith('| T2622 |'): body = body.split('|')[2].strip()
body = body.replace('|', '∣')
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); lines = open(reg, encoding='utf-8').read().split('\n'); n = 0
for i, l in enumerate(lines):
    if l.startswith('| T2622 |'):
        old = l.split('|')[2].strip()
        j = old.find('[FLAG'); v1 = old[:j].strip() if j >= 0 else old
        newrow = ('| T2622 | ' + body + f' [v2 RE-REGISTERED {stamp} EDT {today} on Cal\'s word ({calword}) after {e13}; K1873 §2; Cal §880 reduction-rank criterion. SUPERSEDED v1 (registered 17:02 2026-09-06, wrong lattice in (H2) — nobody constructed the order): ' + v1[:1200] + ' …] | DERIVED for all odd p (reduction-rank criterion, Cal §880) with instruments at p = 3 (b²+bd+d²+3a² ≅ ⟨1,3,3⟩: π/ln 3) and p = 5 (Lyra\'s K₅: π/ln 5, E13); p = 2 = T2621 (odd planes cancel the partner); the reduction-rank-2 class (⟨1,1,3⟩, 2π/ln p) is the CONTROL, not the rule\'s | graph-node (number theory / RH row) | 5704, 5710 (control), E13 | ' + today + ' |')
        lines[i] = newrow; n += 1
open(reg, 'w', encoding='utf-8').write('\n'.join(lines)); print('registry rows rewritten:', n)
gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json'); gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8'))
name = 'Kernel-Swap Theorem v2 (reduction-rank dichotomy): with the corpus\'s odd planes fixed and the kernel the trace-zero lattice of the maximal order ramified at {p, ∞} (reduction rank 1 mod p), the short-root factor carries Steinberg × the unramified-quadratic partner and the kernel comb has spacing π/ln p for every odd p; a reduction-rank-2 kernel gives 2π/ln p; p = 2 is T2621\'s case'
plain = 'Build the small definite part of the lattice by the rule — from the generators of the maximal order — and reduce it mod p: it has rank one there, and that single fact fixes the comb spacing at π/ln p for every odd prime. The earlier lattice ⟨1,1,3⟩ was in the other class (rank two mod 3) and gave twice the spacing; it was never the rule\'s. At p = 2 the odd planes cancel half the comb, which is why T2621 shows 2π/ln 2.'
c = 0
for coll in ('theorems', 'nodes'):
    for t in gd[coll]:
        if t['tid'] == 2622:
            t['name'] = name; t['plain'] = plain; t['status'] = f'DERIVED for all odd p (Cal §880 reduction-rank criterion; instruments p = 3, 5; {e13}); v2 re-registered {stamp} {today} on Cal\'s word ({calword}); v1 (09-06 17:02) superseded — wrong lattice in (H2)'; t['section'] = 'Cal §880 / K1873 §2 / Lyra v2 (Round 126)'; c += 1
for e in gd['edges']:
    if e['from'] == 2621 and e['to'] == 2622: e['label'] = 'the p = 2 special case: the odd planes cancel the unramified-quadratic partner, leaving the even-k comb 2π/ln 2'
for nd in gt['nodes']:
    if nd['id'] == 'T2622': nd['name'] = name; nd['plain'] = plain; nd['status'] = 'derived (v2)'; nd['proofs'] = ['reduction-rank criterion (Cal §880)', 'direct p-adic integrals p = 3, 5', 'T2621 at p = 2']
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); print('graph records rewritten:', c)
open(os.path.join(here, 'THEOREM_LOG.md'), 'a').write(f"| T2622 v2 | Kernel-swap theorem re-registered: reduction-rank dichotomy; rule's kernel gives π/ln p for all odd p; p = 2 = T2621 | D1 | Cal §880; K1873 §2; Cal {calword}; {e13} | 5704, 5710 (control), E13 | Lyra (v2 text) / Grace (registered) | {today} | derived (v2) |\n")
# G19 table relabel
g19 = glob.glob(os.path.join(root, 'notes', 'grace_G19_TABLE_kernel_ramification_*.md'))
if g19:
    t = open(g19[0], encoding='utf-8').read()
    if 'v2 RELABEL' not in t:
        t += f"\n\n## v2 RELABEL {stamp} EDT {today} (K1873 §2 / Cal §880 / {e13}; on Cal's word {calword})\nThe rows above are re-read under the reduction-rank criterion: the **rule's kernel at p = 3 is b² + bd + d² + 3a² ≅ ⟨1,3,3⟩ over ℤ₃ (reduction rank 1) → π/ln 3 — Cal's Sunday row was the rule's all along**; the **⟨1,1,3⟩ row (reduction rank 2, disc 3) is the CONTROL** for the other discriminant class, not the rule's kernel; Lyra's p = 5 lattice 2x²+2y²+2z²−xy−yz−zx (reduction rank 1) → π/ln 5 ({e13}). The verdict 'base = the prime' stands; the sentence '2π/ln 3 measured on the rule's kernel' is withdrawn. The dichotomy: reduction rank 1 ↦ π/ln p (all k; the partner survives); reduction rank 2 ↦ 2π/ln p (even k only); p = 2 ↦ the odd planes cancel the partner (T2621).\n"
        open(g19[0], 'w', encoding='utf-8').write(t); print('G19 table relabelled')
print('T2622 v2 done; verify with the SOD instrument')
