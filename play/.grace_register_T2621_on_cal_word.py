#!/usr/bin/env python3
"""Grace — registration of T2621, the resonance theorem (K1866 §3; Round 122 G15). Cal's word is given (C4, §854/§862);
Lyra NAMES it (her L1). Usage:
  python3 .grace_register_T2621_on_cal_word.py --cal-word "C4 §854; §862" [--row-file notes/Lyra_L7_*.md] [--name "..."]
If --row-file is given, its first line starting with '| T2621 |' is used verbatim as the registry row (Lyra's text); else K1866 §3's text.
Edges from = INPUT -> to = CONSEQUENCE: T2616 -> T2621 (axis), T1299 -> T2621 (the operator, v3), T2621 -> T1448 (the Eisenstein item).
Refuses if the claim file play/.claims/theorem_T2621_* is absent (Lyra claims first) unless --claimed-by-counter is passed.
"""
import json, sys, os, datetime, subprocess, glob
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
a = sys.argv[1:]
if '--cal-word' not in a: print('REFUSED: --cal-word required'); sys.exit(1)
calword = a[a.index('--cal-word') + 1]
rowfile = a[a.index('--row-file') + 1] if '--row-file' in a else None
name_override = a[a.index('--name') + 1] if '--name' in a else None
if not glob.glob(os.path.join(here, '.claims', 'theorem_T2621_*')) and '--claimed-by-counter' not in a:
    print('REFUSED: no claim file for T2621 — Lyra names/claims it first (K1866 §3)'); sys.exit(1)
today = datetime.date.today().isoformat(); stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip()
tid, tid_s = 2621, 'T2621'
name = name_override or 'Resonances of the spherical Eisenstein series on Γ\\D_IV^5 at level 1: the constant term\'s pole set is {zeros of ζ at the four shifts of L1 §3} ∪ {the 2-comb −1/2 + 2πik/ln 2}; λ = 1/2 regular (DERIVED: E6 hashed, 10^-29; family rule E9)'
plain = ('Send a wave into the arithmetic quotient of D_IV^5 and watch what leaks back out: the scattering matrix has poles exactly at the zeros of Riemann\'s zeta, '
         'at four shifted positions, plus one extra evenly spaced comb of poles that comes from the prime 2 (because three squares cannot be zero mod 8). '
         'So the zeros of zeta ARE the resonances of this space. This pins WHERE the zeros sit in the continuous spectrum; it says nothing about their real parts, which is RH.')
registry = None
if rowfile:
    for line in open(rowfile, encoding='utf-8').read().split('\n'):
        if line.startswith('| T2621 |'): registry = line; break
if registry is None:
    registry = (f'| T2621 | RESONANCE THEOREM — the zeros of ζ are the resonances of Γ\\D_IV⁵ at level 1 (Lyra L1, hashed 11:31; Elie E6 5704 5/5 at 10⁻²⁹; K1865 §1, K1866 §3; Cal {calword}; Round 122 G15): '
                'the constant term of the spherical (minimal-parabolic) Eisenstein series on Γ\\D_IV⁵ is the product of four rank-one factors c(w₀,λ) = c_{e₁−e₂}c_{e₁+e₂}c_{e₁}c_{e₂} (B₂, multiplicities (3,1), ρ_𝔞 = (5/2, 3/2)); its POLE SET is exactly {−½ + iγ_n (the multiplicity-1 factors), −¼ + iγ_n/2 and −1 + iγ_n (the multiplicity-3 factors A, B), λ = 3/2} ∪ {the 2-comb −½ + 2πik/ln 2, k ≠ 0, spacing 9.06472028365}, all simple, together with the residual pole at λ = 3/2 (the constant function, from ζ(λ − ½) in Λ(λ)); λ = ½ REGULAR (the ξ(2λ) pole cancelled by ζ(1) in Λ(λ+1)); λ = iγ_n regular. '
                'The comb is the Jacquet–Langlands surgery at p = 2: the kernel x₃² + x₄² + x₅² is anisotropic exactly at 2 and ∞ (no primitive zero of three squares mod 8), so the trivial representation of the compact kernel is Steinberg at 2 and the split-place factor is replaced; no quadratic character (odd kernel). FAMILY CLAUSE (Cal §861/§862, BY THE INSTRUMENT, not 5705\'s label): comb present at n = 3 (level-type, from the odd plane, odd-k), ABSENT at n = 4 (ζ_{ℚ(i)} absorbs the 2-factor), present at n = 5 (even-k, L1\'s), present at n = 6 (Re λ = −1); n ≥ 7 NOT ESTABLISHED — the label "kernel anisotropic at 2" (5705, 4/4) is refuted at n = 4 and undecided at n ≥ 7; D_IV⁵ is inside the range, not selected by it. '
                'INSTRUMENT: Elie 5704 (prereg e7e7e17e): poles located by Newton on 1/c and matched to ζ\'s zeros, orders read from |c(z₀ + δe^{iθ})| ∝ δ^{−m}: P1–P5 HIT, max |Δ| 1.2×10⁻²⁹, argument principle winding −3.0000 = 16 zeros − 19 poles, nothing off the list; DERIVED rests on three non-JL instruments (Cal §862): Gindikin–Karpelevich at odd p, Harish-Chandra at ∞, and the direct 2-adic odd-lattice intertwining integral on ⟨1⁵, −1²⟩ (Cal §854/§855); E6 is the formula check. '
                'CEILING (in the row, K1865): this pins WHERE ζ\'s zeros sit in D_IV⁵\'s continuous spectrum, not their real parts; "zeros are resonances" is classical for any congruence quotient (Langlands 1976) — the content is the explicit factor list with the prime-2 comb; RH stays ATTEMPT. Level 137 adds the resonances of all 136 L-functions mod 137 and nothing to ζ. Inputs: T2616 (axis), T1299 v3 (the operator, r₁ = std ⊗ std_{SL₂} specialised at the trivial kernel representation to L(s ∓ ½, π)); consumer: T1448\'s Eisenstein item (Round 122 L8/E10). | DERIVED (hashed prediction, independent instrument, kill stated not fired; Cal C4) | graph-node (number theory / RH row) | 5700, 5704, 5705 | {today} |')
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8'))
ids = {t['tid'] for t in gd['theorems']}
if tid in ids: print('already registered'); sys.exit(0)
lines = open(reg, encoding='utf-8').read().split('\n'); anchor = max(i for i, l in enumerate(lines) if l.startswith('| T2620 |'))
lines.insert(anchor + 1, registry); open(reg, 'w', encoding='utf-8').write('\n'.join(lines))
rec = dict(tid=tid, name=name, domain='number_theory', status=f'derived (Lyra L1 hashed; Elie E6 5704 5/5 at 1e-29; family rule E9 5705; Cal {calword}; ceiling: location in the continuous spectrum, not the real parts)', depth=1, conflation=0, section='K1865 §1 / K1866 §3 (Round 122 G15)', toys=[5700, 5704, 5705], date=today, plain=plain)
gd['theorems'].append(rec); gd['nodes'].append(dict(rec))
for (fr, to, src, lab) in ((2616, 2621, 'derived', 'the unitarity axis is where the constant term is evaluated'), (1299, 2621, 'structural', 'the Siegel-parabolic operator (v3, r1 = std x std_SL2) specialised by L1 at the minimal parabolic'), (2621, 1448, 'derived', 'the Eisenstein constant term T1448 listed as its honest gap (Round 122 L8/E10 tests the -(pi^2/2) ln 2)')):
    assert fr in ids | {tid} and to in ids | {tid}, ('dangling', fr, to)
    gd['edges'].append({'from': fr, 'to': to, 'source': src, 'label': lab}); gt['edges'].append({'source': f'T{fr}', 'target': f'T{to}', 'type': 'uses'})
color = next((n.get('color') for n in gt['nodes'] if n['domain'] == 'number_theory'), '#8E6BBF')
gt['nodes'].append(dict(id=tid_s, name=name, domain='number_theory', domain_label='Number theory / RH row', status='derived', plain=plain, color=color, proofs=['L1 constant term (Gindikin–Karpelevich + JL at 2)', 'E6 5704', 'E9 5705']))
for t_id in (1299, 1448):
    if not any(n['id'] == f'T{t_id}' for n in gt['nodes']):
        t = [x for x in gd['theorems'] if x['tid'] == t_id][0]
        gt['nodes'].append(dict(id=f'T{t_id}', name=t['name'], domain=t['domain'], domain_label=t['domain'], status=str(t['status']).split(' ')[0].lower(), plain=t.get('plain', ''), color=color, proofs=[]))
gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=f'{today} both lists (Grace G15)')
gd['meta']['max_tid'] = f'T{max(ids | {tid})}'; gd['meta']['last_updated'] = today
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
open(os.path.join(here, 'THEOREM_LOG.md'), 'a').write(f"| T2621 | Resonance theorem: zeros of ζ = resonances of Γ\\D_IV^5 (four shifts + 2-comb) | D1 | K1866 §3; Cal {calword} | 5700,5704,5705 | Lyra (named) / Grace (registered) | {today} | derived |\n")
for cf in glob.glob(os.path.join(here, '.claims', 'theorem_T2621_*')): open(cf, 'a').write(f'Registered: {today} {stamp} on Cal\'s word ({calword}) by Grace\n')
ids2 = {t['tid'] for t in gd['theorems']}; gids = {n['id'] for n in gt['nodes']}
print('registered T2621 |', len(gd['theorems']), len(gd['nodes']), len(gd['edges']), '|', len(gt['nodes']), len(gt['edges']))
print('edges touching 2621:', [(e['from'], e['to']) for e in gd['edges'] if 2621 in (e['from'], e['to'])])
print('dangling data:', [e for e in gd['edges'] if e['from'] not in ids2 or e['to'] not in ids2], '| dangling curated:', [e for e in gt['edges'] if e['source'] not in gids or e['target'] not in gids])
