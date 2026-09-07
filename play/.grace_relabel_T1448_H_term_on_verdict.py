#!/usr/bin/env python3
"""Grace — Round 125 (2). The two prepared relabels of T1448's HYPERBOLIC (H) line "(N_c/rank²)·ζ(N_c) = (3/4)ζ(3): N_c colour geodesic
families, each summing to ζ(N_c)", applied by the Keeper/Elie verdict (rubric Section 3 re-audit; Deitmar 2004 prime geodesic theorem in rank 2).
RUN ONLY AFTER THE VERDICT IS POSTED.
Usage:
  python3 .grace_relabel_T1448_H_term_on_verdict.py --mode COMPUTED --verdict "K18xx / toy NNNN" [--detail "..."]
  python3 .grace_relabel_T1448_H_term_on_verdict.py --mode ASSIGNED --verdict "K18xx / toy NNNN" [--detail "..."]
COMPUTED = a geodesic count on Γ(137)\\D_IV^5 (primitive hyperbolic conjugacy classes below a norm bound, orbital integrals against the
           L = 2 test function) REPRODUCES (3/4)ζ(3) with the colour-family structure stated: the H line is DERIVED, and the sweep says so.
ASSIGNED = no geodesic count produces it: ζ(3) is ASSIGNED by the zeta-weight correspondence (2L − 1 = N_c at L = 2), "N_c colour
           geodesic families" names no enumerated families, and 3/4 is the Bergman eigenvalue N_c/rank² read into a coefficient;
           the known C₂ (Petermann–Sommerfield 1957) stands as a NUMBER; the H line → MATCHED-NOT-DERIVED like the E line (K1869 §2).
Sites (same-hour sweep): T1448 (:31, :196–207, :357), T1451 (:34, :69, :108, :157, :174), registry prose :1291/:1297 + rows T1448/T1451,
Paper86 + Outline (:56, :61, :70, :79), Paper90, Paper91_Physics, Paper91_Spectral_Zeta_DIV5, Paper96, Paper83_Draft, T1450, T1461, Spectral_Zeta_G2.
NOT touched, by design: the 3/4 = N_c/rank² rows (T1250, T1312, T1324, T2189; Paper 106's glueball ratio) — a DIFFERENT object (the Bergman
Laplacian eigenvalue), which this relabel does not judge. Archives and Cal's logs untouched.
"""
import sys, os, re, json, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); a = sys.argv[1:]
def arg(k, d=None): return a[a.index(k) + 1] if k in a else d
mode = arg('--mode'); verdict = arg('--verdict'); detail = arg('--detail', '')
if mode not in ('COMPUTED', 'ASSIGNED') or not verdict: print('REFUSED: --mode COMPUTED|ASSIGNED and --verdict required'); sys.exit(1)
stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); today = datetime.date.today().isoformat()
KEY = 'Grace R125 H-term'
if mode == 'COMPUTED':
    TAG = (f'[{stamp} EDT {today}, {KEY} ({verdict}) — H LINE DERIVED: the hyperbolic contribution (3/4)ζ(3) to the two-loop coefficient IS reproduced by a geodesic count on Γ(137)\\D_IV⁵ — primitive hyperbolic conjugacy classes enumerated below a norm bound, orbital integrals against the L = 2 test function, the N_c = 3 colour families exhibited as classes of closed geodesics (prime geodesic theorem in rank 2, Deitmar 2004). {detail} The zeta-weight correspondence 2L − 1 = N_c at L = 2 (T1445) is the reading of a computed sum, not an assignment. The 3/4 = N_c/rank² rows (T1250/T1312/T1324/T2189) are a different object and are not judged here.]')
    SUF = f' — H line DERIVED {stamp} {today} ({KEY}, {verdict}): (3/4)ζ(3) reproduced by a geodesic count on Γ(137)\\D_IV⁵'
else:
    TAG = (f'[{stamp} EDT {today}, {KEY} ({verdict}) — H LINE MATCHED, NOT DERIVED (the question the E term failed, asked of the H term): no geodesic count on Γ(137)\\D_IV⁵ produces (3/4)ζ(3) — "N_c colour geodesic families, each summing to ζ(N_c)" names no enumerated families of closed geodesics (T1448\'s own "honest gap": the classification of primitive geodesics into N_c colour families was never done), ζ(3) is ASSIGNED by the zeta-weight correspondence 2L − 1 = N_c at L = 2 (T1445 read as a rule, not a count), and the coefficient 3/4 is the Bergman eigenvalue N_c/rank² (T1250/T1312) read into a trace-formula coefficient with the Cartan Jacobian "det(𝔞) = rank² = 4" asserted. {detail} The NUMBER C₂ = 197/144 + π²/12 − (π²/2) ln 2 + (3/4)ζ(3) is Petermann–Sommerfield (1957) and STANDS; what falls is the decomposition\'s attribution of its ζ(3) term to closed geodesics with this test function — the same shape as the E line (K1869 §2, G18 Mode B). A computed replacement exists in principle: the prime geodesic theorem for Γ(137)\\D_IV⁵ (rank 2, Deitmar 2004) with a rule-fixed h; not yet run. The 3/4 = N_c/rank² rows (T1250/T1312/T1324/T2189) are a DIFFERENT object (the Bergman Laplacian eigenvalue) and are not judged here.]')
    SUF = f' — H line MATCHED-NOT-DERIVED {stamp} {today} ({KEY}, {verdict}): ζ(3) assigned by the zeta-weight rule, no geodesic count; 3/4 is the Bergman eigenvalue read as a coefficient; C₂ number stands'
SITES = ['BST_T1448_Schwinger_C2_Decomposition.md', 'BST_T1451_Vertex_Selberg_Trace_Formula.md', 'BST_Paper86_Selberg_G2.md', 'BST_Paper86_Selberg_G2_Outline.md',
         'BST_Paper90_QED_QCD_Spectral_Unification.md', 'BST_Paper91_Physics.md', 'BST_Paper91_Spectral_Zeta_DIV5.md', 'BST_Paper96_Geodesic_QED_Dictionary.md',
         'Paper83_Draft.md', 'BST_T1450_Schwinger_C3_Reading.md', 'BST_T1461_Bergman_Spectral_amu.md', 'BST_Spectral_Zeta_G2_Framework.md']
pat = re.compile(r'geodesic famil|\(3/4\)\s*\*?\s*zeta\(3\)|\(3/4\)ζ\(3\)|zeta\(N_c\)|ζ\(N_c\)|H_2 ?=|H_L')
done = []
for fn in SITES:
    p = os.path.join(root, 'notes', fn)
    if not os.path.exists(p): done.append('MISSING ' + fn); continue
    t = open(p, encoding='utf-8').read()
    if KEY in t: done.append('already ' + fn); continue
    hits = len(pat.findall(t))
    if not hits: done.append('no site in ' + fn); continue
    banner = '> **' + TAG + '**\n\n'
    if t.startswith('---'):
        j = t.find('\n---', 3); j = t.find('\n', j + 1) + 1; t = t[:j] + '\n' + banner + t[j:]
    else: t = banner + t
    open(p, 'w', encoding='utf-8').write(t); done.append(f'{fn}: {hits} site(s), banner')
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); lines = open(reg, encoding='utf-8').read().split('\n'); n = 0
for i, l in enumerate(lines):
    if (l.startswith('*Schwinger C₂ Decomposition via Selberg Vertex Trace Formula (T1448,') or l.startswith('*Vertex Selberg Trace Formula (T1451,') or re.match(r'\| T14(48|51) \|', l)) and KEY not in l:
        lines[i] = l.rstrip() + ' ' + TAG; n += 1
open(reg, 'w', encoding='utf-8').write('\n'.join(lines)); done.append(f'registry: {n} lines')
gd_p = os.path.join(root, 'play', 'ac_graph_data.json'); gd = json.load(open(gd_p, encoding='utf-8')); c = 0
for coll in ('theorems', 'nodes'):
    for t in gd[coll]:
        if t['tid'] in (1448, 1451) and KEY not in str(t['status']): t['status'] = str(t['status']) + SUF; c += 1
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); done.append(f'graph statuses: {c}')
print('\n'.join(done)); print('MODE', mode)
