#!/usr/bin/env python3
"""Grace — Round 125 (3). T1451 → TEMPLATE on Cal's word (L12: there is NO rule from the QED vertex to a trace-formula test function h —
the vertex fixes h only on the discrete Bergman spectrum, where the Eisenstein term is blind; K1871 §2). The "0.026 % through five loops"
sentence re-worded "assembled from matched terms; arithmetic exact" unless the audits say otherwise. RUN ONLY ON CAL'S WORD.
Usage: python3 .grace_relabel_T1451_template_on_cal_word.py --cal-word "§NNN, HH:MM" [--five-loop-override "<text if the audits say otherwise>"]
Sites: registry prose :1297 (tier word FRAMEWORK → TEMPLATE; the 0.026 % clause), registry row T1451, T1451 file (banner + the L = 5 sentence at
"BST (5 loops): 0.001159956438 — agrees to 0.026%."), graph statuses T1451 (both lists). The C₅ "no new transcendentals" prediction rows
(Paper90 :54/:150, Paper83 :434/:973, toy 1822) are a DIFFERENT claim (a weight bound, not the 0.026 % match) and are not touched.
"""
import sys, os, re, json, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); a = sys.argv[1:]
def arg(k, d=None): return a[a.index(k) + 1] if k in a else d
calword = arg('--cal-word'); override = arg('--five-loop-override', '')
if not calword: print('REFUSED: --cal-word required'); sys.exit(1)
stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); today = datetime.date.today().isoformat()
KEY = 'Grace R125 T1451-template'
FIVE = override or ('BST through five loops: 0.001159956438 against experiment 0.00115965218091 — a value ASSEMBLED FROM MATCHED TERMS (each C_L\'s Selberg decomposition is matched to the known QED coefficient, not computed from the geometry: E line K1869 §2, H line R125); the ARITHMETIC of the assembly is exact (the known C_L with α = 1/137 reproduce a_e to 0.026 %, the residual being α\'s next digits and the hadronic/electroweak terms, as any assembly of the known coefficients would). The 0.026 % is therefore a check of the known coefficients\' arithmetic, not a prediction of the framework.')
TAG = (f'[{stamp} EDT {today}, {KEY} — T1451 → TEMPLATE on Cal\'s word ({calword}); K1871 §2; Lyra L12: there is NO rule that produces a trace-formula test function h from the QED vertex — the vertex fixes h only on the discrete Bergman spectrum, where the Eisenstein term is blind — so "the Selberg trace formula for the L-loop vertex kernel" names a TEMPLATE (a decomposition C_L = I + K + E + H + M whose terms are assigned by transcendental type), not a computation; E12 (Elie 5713) is the first term COMPUTED, with a rule-fixed heat-kernel h, and it is not a match. Five-loop sentence: {FIVE} The Spectral-Gap clause (137 − 126 = 11) and the ingredient list are untouched; the C₅ weight-bound prediction (Paper 90, toy 1822) is a different claim and is not judged here.]')
done = []
p = os.path.join(root, 'notes', 'BST_T1451_Vertex_Selberg_Trace_Formula.md'); t = open(p, encoding='utf-8').read()
if KEY not in t:
    old5 = 'BST (5 loops): 0.001159956438 — agrees to 0.026%.'
    if old5 in t: t = t.replace(old5, old5 + ' **[R125: ' + FIVE + ']**')
    banner = '> **' + TAG + '**\n\n'
    if t.startswith('---'):
        j = t.find('\n---', 3); j = t.find('\n', j + 1) + 1; t = t[:j] + '\n' + banner + t[j:]
    else: t = banner + t
    open(p, 'w', encoding='utf-8').write(t); done.append('T1451 file: banner + five-loop sentence')
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); lines = open(reg, encoding='utf-8').read().split('\n'); n = 0
for i, l in enumerate(lines):
    if l.startswith('*Vertex Selberg Trace Formula (T1451, FRAMEWORK,') and KEY not in l:
        l = l.replace('*Vertex Selberg Trace Formula (T1451, FRAMEWORK,', '*Vertex Selberg Trace Formula (T1451, TEMPLATE [was FRAMEWORK; Cal ' + calword + ', ' + today + '],', 1)
        l = l.replace('Numerical: BST a_e through 5 loops = 0.001159956438 vs experiment 0.00115965218091, 0.026% (exact α and hadronic/EW corrections close to 13 digits).', 'Numerical [re-worded R125]: ' + FIVE)
        lines[i] = l.rstrip() + ' ' + TAG; n += 1
    elif re.match(r'\| T1451 \|', l) and KEY not in l:
        l = l.replace('| T1451 | Spectral Gap Framework | Proved |', '| T1451 | Spectral Gap Framework | TEMPLATE (was Proved; Cal ' + calword + ') |', 1)
        lines[i] = l.rstrip() + ' ' + TAG; n += 1
open(reg, 'w', encoding='utf-8').write('\n'.join(lines)); done.append(f'registry: {n} lines')
gd_p = os.path.join(root, 'play', 'ac_graph_data.json'); gd = json.load(open(gd_p, encoding='utf-8')); c = 0
for coll in ('theorems', 'nodes'):
    for x in gd[coll]:
        if x['tid'] == 1451 and KEY not in str(x['status']): x['status'] = 'TEMPLATE (' + stamp + ' ' + today + ', Cal ' + calword + '; L12: no vertex → h rule; E12 the first computed term) — ' + str(x['status']); c += 1
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); done.append(f'graph statuses: {c}')
print('\n'.join(done))
