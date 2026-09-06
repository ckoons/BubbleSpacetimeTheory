#!/usr/bin/env python3
"""Grace — G18 (Round 123). The two prepared relabels of T1448's Eisenstein line, applied by E10's verdict. RUN ONLY AFTER E10 IS SCORED.
Usage:
  python3 .grace_relabel_T1448_eisenstein_line_on_E10.py --mode A --e10 "toy NNNN, hash XXXX" [--ln137 "yes: <value>"|"no: <reason>"]
  python3 .grace_relabel_T1448_eisenstein_line_on_E10.py --mode B --e10 "toy NNNN, hash XXXX" --value "<E10's number>" [--ln137 ...]
Mode A = E10 REPRODUCES −(π²/2) ln 2 from T2621's c(w0,λ) with T1448's test function: the line is DERIVED from T2621, and the base 2 is the
         PRIME 2 (Steinberg root numbers 2^{1−2λ} at the anisotropic prime), not the rank — "ln(rank)" retired everywhere, "rank^{−2s}" → the root-number product.
Mode B = E10 does NOT reproduce it: the line is CORRECTED by E10 (value given); T1448's posited rank^{−2s} refuted; consumers flagged; the KNOWN
         2-loop coefficient C₂ = 197/144 + π²/12 − (π²/2) ln 2 + (3/4)ζ(3) (Petermann 1957; Sommerfield 1957) stands as a NUMBER — only the
         decomposition's attribution of its ln 2 term changes.
Either mode: every site quoting "ln(rank)" / "rank^{-2s}" / "psi(1/2)+gamma = -2 ln(rank)" gets a dated bracket (same-hour sweep); graph statuses of
T1448, T1450, T1451, T1461 get a suffix; the registry prose :1291 gets the bracket. Archives (.running/CI_BOARD_completed_*) untouched; Cal's logs untouched.
"""
import sys, os, re, json, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:]
def arg(k, d=None): return a[a.index(k) + 1] if k in a else d
mode = arg('--mode'); e10 = arg('--e10'); value = arg('--value', ''); ln137 = arg('--ln137', 'level 137 not yet computed')
if mode not in ('A', 'B') or not e10: print('REFUSED: --mode A|B and --e10 "<toy, hash>" required'); sys.exit(1)
if mode == 'B' and not value: print('REFUSED: mode B needs --value'); sys.exit(1)
stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip(); today = datetime.date.today().isoformat()
if mode == 'A':
    TAG = (f'[{stamp} EDT {today}, Grace G18 (Round 123), E10 ({e10}) SCORED — RELABEL A, DERIVED FROM T2621: the Eisenstein contribution −(π²/2)·ln 2 = −3.42049… to the two-loop coefficient IS reproduced by −(1/4π)∫(φ′/φ)(½ + it)h(t)dt with φ = c(w₀,λ) the constant term of T2621 (level 1) and T1448\'s test function; T1448\'s posited "intertwining operator rank^{{−2s}}" is the product of the Steinberg root numbers ε = 2^{{½−λ}} at the two multiplicity-3 roots, 2^{{1−2λ}} (Lyra L8; Cal §862 C9) — so the BASE 2 IS THE PRIME 2, the place where the kernel x₃²+x₄²+x₅² is anisotropic (T2621, E9), NOT the Cartan rank. "ln(rank)" is RETIRED at this site; read "ln 2 = ln(prime 2)". The shared integer rank 2 = prime 2 is separated by construction in E11 (kernel swap {{2,∞}} → {{3,∞}}: spacing 2π/ln 3, Round 123 G19). Level 137: {ln137}. The archimedean −2 ln 2 of ψ(½) + γ and the 2-adic −2 ln 2 of the root numbers are two sources with one coefficient (Cal C9) — the derivation, not the coincidence, is what this bracket records.]')
    SUF = f' — Eisenstein line RELABELLED {stamp} {today} (G18, E10 {e10}): derived from T2621; ln 2 = ln(prime 2) via the Steinberg root numbers 2^(1−2λ), NOT ln(rank); E11 separates rank 2 from prime 2 by kernel swap'
else:
    TAG = (f'[{stamp} EDT {today}, Grace G18 (Round 123), E10 ({e10}) SCORED — RELABEL B, CORRECTED BY E10: the Eisenstein contribution computed from T2621\'s verified constant term with T1448\'s test function at level 1 is {value}, NOT −(π²/2)·ln 2 = −3.42049…; T1448\'s posited "intertwining operator rank^{{−2s}} with log-derivative −2 ln(rank)" is REFUTED as the mechanism of this term. The NUMBER C₂ = 197/144 + π²/12 − (π²/2) ln 2 + (3/4)ζ(3) = −0.328478965579193 is the known two-loop QED coefficient (Petermann 1957; Sommerfield 1957) and stands; what falls is the DECOMPOSITION\'s attribution of its ln 2 term to the continuous spectrum with this test function. "ln(rank)" is RETIRED at this site (the only logarithm the constant term produces is ln(prime 2), from the Steinberg root numbers at the anisotropic prime — T2621, L8). Level 137: {ln137}. Downstream rows (T1450, T1451, T1461; Papers 83, 86, 90, 91, 96; the Spectral-Zeta framework) inherit CONDITIONAL on a re-derivation of the Eisenstein term.]')
    SUF = f' — Eisenstein line CORRECTED {stamp} {today} (G18, E10 {e10}): T2621\'s constant term gives {value}, not −(π²/2) ln 2; rank^(−2s) mechanism refuted; the known C₂ number stands; attribution CONDITIONAL'
SITES = ['BST_T1448_Schwinger_C2_Decomposition.md', 'BST_T1451_Vertex_Selberg_Trace_Formula.md', 'BST_T1450_Schwinger_C3_Reading.md', 'BST_T1461_Bergman_Spectral_amu.md',
         'BST_Spectral_Zeta_G2_Framework.md', 'BST_Paper86_Selberg_G2.md', 'BST_Paper86_Selberg_G2_Outline.md', 'BST_Paper90_QED_QCD_Spectral_Unification.md',
         'BST_Paper91_Physics.md', 'BST_Paper91_Spectral_Zeta_DIV5.md', 'BST_Paper96_Geodesic_QED_Dictionary.md', 'Paper83_Draft.md']
done = []
for fn in SITES:
    p = os.path.join(root, 'notes', fn)
    if not os.path.exists(p): done.append('MISSING ' + fn); continue
    t = open(p, encoding='utf-8').read()
    if 'Grace G18 (Round 123)' in t: continue
    pat = re.compile(r'ln\(rank\)|rank\^\{?-2s\}?|rank\^\{−2s\}|-2\*ln\(rank\)|−2 ?ln\(rank\)|-\(pi\^2/rank\)')
    hits = [m.start() for m in pat.finditer(t)]
    if not hits: done.append('no site in ' + fn); continue
    # banner at top + inline marker on the FIRST hit line
    banner = '> **' + TAG + '**\n\n'
    if t.startswith('---'):
        j = t.find('\n---', 3); j = t.find('\n', j + 1) + 1; t = t[:j] + '\n' + banner + t[j:]
    else: t = banner + t
    open(p, 'w', encoding='utf-8').write(t); done.append(f'{fn}: {len(hits)} site(s), banner')
# registry prose :1291 (T1448) and any T1451/T1461 prose
reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md'); lines = open(reg, encoding='utf-8').read().split('\n'); n = 0
for i, l in enumerate(lines):
    if (l.startswith('*Schwinger C₂ Decomposition via Selberg Vertex Trace Formula (T1448,') or re.match(r'\| T14(48|51|61) \|', l)) and 'Grace G18 (Round 123)' not in l:
        lines[i] = l.rstrip() + ' ' + TAG; n += 1
open(reg, 'w', encoding='utf-8').write('\n'.join(lines)); done.append(f'registry: {n} lines')
gd_p = os.path.join(root, 'play', 'ac_graph_data.json'); gd = json.load(open(gd_p, encoding='utf-8')); c = 0
for coll in ('theorems', 'nodes'):
    for t in gd[coll]:
        if t['tid'] in (1448, 1450, 1451, 1461) and 'G18, E10' not in str(t['status']): t['status'] = str(t['status']) + SUF; c += 1
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); done.append(f'graph statuses: {c}')
# toy 1822 header + queue_casey line: a one-line pointer only
for rel in ('play/toy_1822_C5_QED_no_new_transcendentals.py',):
    p = os.path.join(root, rel); t = open(p, encoding='utf-8').read()
    if 'Grace G18 (Round 123)' not in t:
        t = t.replace('\n', '\n# ' + TAG[:220] + ' … (full text in T1448 file header)\n', 1) if t.startswith('#!') else '# ' + TAG[:220] + '\n' + t
        open(p, 'w', encoding='utf-8').write(t); done.append(rel + ': header pointer')
print('\n'.join(done)); print('MODE', mode)
