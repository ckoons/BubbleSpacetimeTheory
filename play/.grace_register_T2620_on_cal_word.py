#!/usr/bin/env python3
"""Grace — registration of T2620, the barrier CONSTRAINT row (K1864 B; Round 121 G13). RUN ONLY ON CAL'S WORD.
Usage: python3 .grace_register_T2620_on_cal_word.py --cal-word "§NNN, HH:MM"
Same mechanics as .grace_register_T2616_T2619_on_cal_word.py (registry row after T2619; both graph files; THEOREM_LOG; claim file if any).
Edges from = INPUT -> to = CONSEQUENCE: T2618 -> T2620, T2619 -> T2620 (K1864 B). Domain number_theory.
"""
import json, sys, os, datetime, subprocess
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
args = sys.argv[1:]
if '--cal-word' not in args:
    print('REFUSED: pass --cal-word "<Cal section, time>" — nothing registers without it'); sys.exit(1)
calword = args[args.index('--cal-word') + 1]
today = datetime.date.today().isoformat(); stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip()
tid, tid_s = 2620, 'T2620'
name = 'BARRIER CONSTRAINT (Davenport–Heilbronn 1936 with the program\'s own oracle): no proof of "all zeros on the symmetry line" from {positive coefficients, meromorphic continuation with finitely many poles, functional equation with gamma factors, polynomial vertical growth, theta origin} alone is valid — zeta_{Z^5} has all of them and off-line zeros; every proof of RH must use a property outside the list, and the one the literature names is ONE self-dual Euler product'
status_long = f'CONSTRAINT row (not a theorem about ζ): a correct META-theorem with a countermodel (T2619). Cal §852\'s three amendments carried: (1) provenance — DH 1936 restated; Selberg class (Kaczorowski–Perelli, Acta Math. 182, 1999) already names the Euler product as load-bearing; Bombieri–Hejhal 1995 for linear combinations; (2) DH\'s own 1936 function is the STRONGER oracle on degree and coefficient size; ℤ⁵\'s one added axis is POSITIVITY of coefficients; (3) "equivalently the independence of the finite fields" struck as an equivalence, kept as a reading. K1864 refinement: "has an Euler product" is not the boundary either (ζ_{{ℤ⁴}} = 8(1−4^{{1−s}})ζ(s)ζ(s−1) has one; ζ_{{ℤ⁶}} is a combination of two) — the property ζ has is ONE self-dual Euler product, no combination. Cal\'s word {calword}.'
plain = 'The geometry\'s own zeta function looks like Riemann\'s in every way a proof usually uses — positive coefficients, a functional equation, gamma factors, growth bounds, a theta function behind it — and yet has zeros off its line. So any argument that would work for both is wrong. A proof of RH has to use the one thing Riemann\'s zeta has and this one lacks: its coefficients multiply, as a single Euler product over the primes.'
registry = f'| T2620 | THE BARRIER CONSTRAINT ROW — Davenport–Heilbronn with a BST-native oracle (K1863 §5, K1864 B; Round 121 G13; Cal {calword}). Let 𝒫 = {{Dirichlet series with POSITIVE coefficients; meromorphic continuation with finitely many poles; functional equation s ↔ σ₀ − s with gamma factors; polynomial vertical growth; a theta-function origin}}. ζ_{{ℤ⁵}}(s) = 3840·Z_cone(s) (T2618) satisfies 𝒫 and has zeros off its symmetry line and beyond its abscissa (T2619). Hence NO argument that proves "all zeros on the line" from 𝒫 alone is valid, and every proof of RH must use a property outside 𝒫. AMENDMENTS (Cal §852, carried verbatim in substance): (1) this is Davenport–Heilbronn 1936 restated — cite DH 1936, Bombieri–Hejhal 1995 (linear combinations), and the Selberg-class literature (Kaczorowski–Perelli 1999) where the Euler-product axiom is already known to be load-bearing; "BST-native" is the provenance of the oracle, not logical content; (2) DH\'s own 1936 function is the STRONGER oracle on every axis but one — degree 1, |a_n| ≤ 1, conductor 5 — so a proof using "degree 1" or "bounded coefficients" is barred by DH\'s oracle and not by ℤ⁵\'s; the ONE axis ℤ⁵ adds is POSITIVITY of coefficients: any RH proof routed through positive measures / positive weights is barred by ℤ⁵ and not by DH — "the program\'s object lands in DH\'s class and adds the positivity axis to the barrier"; (3) "equivalently the independence of the finite fields" is struck as an equivalence and kept as the BST reading. REFINEMENT (K1864 B): "has an Euler product" is not the boundary either — ζ_{{ℤ⁴}} = 8(1 − 4^{{1−s}})ζ(s)ζ(s−1) has one and ζ_{{ℤ⁶}} = 16 L(s,χ₋₄)ζ(s−2) − 4ζ(s)L(s−2,χ₋₄) is a combination of two — the property ζ has is ONE self-dual Euler product, no combination. RH is Π₁: undecidable ⟹ true; this row is a barrier, not undecidability. Consumers: the Millennium ledger RH row; L3 (Lyra, Keeper, Cal: the Szegő-norm positivity is invariant under ζ → ζ_{{ℤ⁵}}, so it cannot contain the prime sum). | CONSTRAINT (meta-theorem with countermodel; classical provenance) | graph-node (number theory / RH row) | 5695 (the countermodel), 5697/5699 (the identity) | {today} |'
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8'))
ids = {t['tid'] for t in gd['theorems']}
if tid in ids: print('already registered'); sys.exit(0)
lines = open(reg, encoding='utf-8').read().split('\n')
anchor = max(i for i, l in enumerate(lines) if l.startswith('| T2619 |'))
lines.insert(anchor + 1, registry); open(reg, 'w', encoding='utf-8').write('\n'.join(lines))
rec = dict(tid=tid, name=name, domain='number_theory', status=status_long, depth=0, conflation=0, section='K1864 B / K1863 §5 (Round 121 G13)', toys=[5695, 5697, 5699], date=today, plain=plain)
gd['theorems'].append(rec); gd['nodes'].append(dict(rec))
for a, src, lab in ((2618, 'derived', 'the identity makes the countermodel the program\'s own object'), (2619, 'exhibited', 'the countermodel: off-line zeros of zeta_{Z^5}')):
    gd['edges'].append({'from': a, 'to': tid, 'source': src, 'label': lab}); gt['edges'].append({'source': f'T{a}', 'target': tid_s, 'type': 'uses'})
color = next((n.get('color') for n in gt['nodes'] if n['domain'] == 'number_theory'), '#8E6BBF')
gt['nodes'].append(dict(id=tid_s, name=name, domain='number_theory', domain_label='Number theory / RH row', status='constraint', plain=plain, color=color, proofs=['DH 1936 + T2619 countermodel']))
gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=f'{today} both lists (Grace G13)')
gd['meta']['max_tid'] = f'T{max(ids | {tid})}'; gd['meta']['last_updated'] = today
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(os.path.join(here, 'THEOREM_LOG.md'), 'a') as f:
    f.write(f"| T2620 | Barrier constraint row (DH with the ζ_{{ℤ⁵}} oracle; positivity axis) | D0 | K1864 B; Cal {calword} | 5695,5697,5699 | Grace (claimed Keeper) | {today} | constraint |\n")
for cf in os.listdir(os.path.join(here, '.claims')):
    if cf.startswith('theorem_T2620_'):
        p = os.path.join(here, '.claims', cf); open(p, 'a').write(f'Registered: {today} {stamp} on Cal\'s word ({calword}) by Grace\n')
ids2 = {t['tid'] for t in gd['theorems']}; gids = {n['id'] for n in gt['nodes']}
print('registered T2620 |', len(gd['theorems']), len(gd['nodes']), len(gd['edges']), '|', len(gt['nodes']), len(gt['edges']))
print('edges touching 2620:', [(e['from'], e['to']) for e in gd['edges'] if 2620 in (e['from'], e['to'])], [(e['source'], e['target']) for e in gt['edges'] if 'T2620' in (e['source'], e['target'])])
print('dangling data:', [e for e in gd['edges'] if e['from'] not in ids2 or e['to'] not in ids2], '| dangling curated:', [e for e in gt['edges'] if e['source'] not in gids or e['target'] not in gids])
