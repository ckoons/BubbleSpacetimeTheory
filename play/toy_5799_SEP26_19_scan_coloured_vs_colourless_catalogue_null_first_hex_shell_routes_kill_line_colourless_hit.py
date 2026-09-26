#!/usr/bin/env python3
"""
Toy 5799 — Casey's "19 appears when colour is added": scan with the NULL FIRST (Elie, 2026-09-26). Prereg f3f09274.
UNIVERSE: data/bst_constants.json, all 197 entries, strings formula_code / formula_display / formula_latex / formula /
bst_expression. HIT for N: the literal integer N (written N or N.0…) in any of those strings, OR an integer-valued
Add/Mul/Pow sub-expression of formula_code (sympy, BST namespace) equal to N.
COLOUR RULE (verbatim from the prereg, applied to name/symbol/category/domain/sector):
  COLOURED  quark|CKM|V_u|V_c|V_t|baryon|proton|neutron|nucle|hadron|pion|kaon|meson|QCD|strong|gluon|Cabibbo
  COLOURLESS electron|muon|tau|lepton|neutrino|PMNS|photon|fine structure|alpha|dark energy|Lambda|Hubble|gravit|
             Planck mass|Higgs|W boson|Z boson|Weinberg
  both -> COLOURED; neither -> UNCLASSIFIED (reported, not scored).
NULL: for N = 10..40, coloured fraction among classified N-hits; hypergeometric tail for 19 vs catalogue base rate.
KILL: a 19-hit in a COLOURLESS quantity.
"""
import json, re
from collections import Counter
from math import comb
import sympy as sp
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
D = json.load(open('data/bst_constants.json')); C = D['constants']
ns = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7, 'N_max': 137}
COL = re.compile(r"quark|CKM|V_u|V_c|V_t|baryon|proton|neutron|nucle|hadron|pion|kaon|meson|QCD|strong|gluon|Cabibbo", re.I)
LESS = re.compile(r"electron|muon|tau|lepton|neutrino|PMNS|photon|fine structure|alpha|dark energy|Lambda|Hubble|gravit|Planck mass|Higgs|W boson|Z boson|Weinberg", re.I)
def colour(e):
    t = ' '.join(str(e.get(k, '')) for k in ('name', 'symbol', 'category', 'domain', 'sector'))
    c, l = bool(COL.search(t)), bool(LESS.search(t))
    return 'C' if c else ('L' if l else 'U')
FIELDS = ('formula_code', 'formula_display', 'formula_latex', 'formula', 'bst_expression')
def literals(e):
    s = ' '.join(str(e.get(k, '') or '') for k in FIELDS)
    out = set()
    for m in re.finditer(r"(?<![\d.])(\d+)(\.0+)?(?![\d.])", s):
        out.add(int(m.group(1)))
    return out
def subexpr_ints(e):
    code = str(e.get('formula_code', '') or '')
    loc = {k: sp.Integer(v) for k, v in ns.items()}
    loc.update({'pi': sp.pi, 'alpha': sp.Rational(1, 137), 'm_e': sp.Symbol('m_e'), 'm_p': sp.Symbol('m_p'),
                'hbar_c': sp.Symbol('hbar_c'), 'log': sp.log, 'sqrt': sp.sqrt, 'exp': sp.exp})
    try:
        ex = sp.sympify(code, locals=loc, rational=True)
    except Exception:
        return set(), False
    out = set()
    for node in sp.preorder_traversal(ex):
        if isinstance(node, (sp.Add, sp.Mul, sp.Pow)) and node.is_Integer is not False:
            try:
                v = sp.nsimplify(node)
                if v.is_Integer: out.add(int(v))
            except Exception: pass
    return out, True
rows = []; parsed = 0
for e in C:
    L = literals(e); S, ok = subexpr_ints(e); parsed += ok
    rows.append((e, colour(e), L | S, L, S))
cls = Counter(r[1] for r in rows)
print(f"catalogue: {len(C)} entries; formula_code parsed by sympy: {parsed}; colour classes {dict(cls)}")
base = cls['C'] / (cls['C'] + cls['L'])
print(f"base rate (coloured among classified): {cls['C']}/{cls['C']+cls['L']} = {base:.3f}")

# NULL FIRST: every N in 10..40
def tail(k, n, K, Npop):  # P(X >= k) hypergeometric
    return sum(comb(K, i)*comb(Npop-K, n-i) for i in range(k, min(n, K)+1)) / comb(Npop, n)
table = []
for N in range(10, 41):
    hits = [r for r in rows if N in r[2]]
    c = sum(r[1] == 'C' for r in hits); l = sum(r[1] == 'L' for r in hits); u = sum(r[1] == 'U' for r in hits)
    p = tail(c, c+l, cls['C'], cls['C']+cls['L']) if c+l else float('nan')
    table.append((N, len(hits), c, l, u, p))
print("\n  N  hits  C  L  U   P(>=C | hyper)")
for t in table: print(f"{t[0]:3d} {t[1]:5d} {t[2]:2d} {t[3]:2d} {t[4]:2d}   {t[5]:.3f}")
t19 = [t for t in table if t[0] == 19][0]
rank_frac = sorted([ (t[2]/(t[2]+t[3]) if t[2]+t[3] else -1) for t in table], reverse=True)
f19 = t19[2]/(t19[2]+t19[3]) if t19[2]+t19[3] else -1
print(f"\n19: {t19[1]} hits, coloured {t19[2]}, colourless {t19[3]}, unclassified {t19[4]}; coloured-fraction rank among N=10..40: "
      f"{rank_frac.index(f19)+1}/{len(table)}")

print("\n19-HITS (name | class | literal? | sub-expression? | display):")
routes = {}
for e, c, A, L, S in rows:
    if 19 in A:
        disp = e.get('formula_display') or e.get('formula_latex') or e.get('formula_code')
        s = ' '.join(str(e.get(k, '') or '') for k in FIELDS)
        if re.search(r"N_c\^?\*?\*?3\s*-\s*rank", s) or '27 - 8' in s or '27-8' in s: rt = '27-8'
        elif re.search(r"rank\^?\*?\*?4\s*\+\s*N_c", s) or '16+3' in s.replace(' ', ''): rt = '16+3'
        elif re.search(r"N_c\^2\s*\+\s*2\*?n_C", s): rt = 'N_c^2+2n_C (none of the three: 9+10)'
        elif re.search(r"4\*?n_C", s): rt = '4n_C-1 (none of the three: 20-1)'
        else: rt = 'literal only -> menu (all three admissible)'
        routes[e['name']] = rt
        print(f"  {e['name'][:44]:44s} | {c} | {19 in L!s:5} | {19 in S!s:5} | {str(disp)[:70]}  -> route: {rt}")

hits19 = [r for r in rows if 19 in r[2]]
colourless19 = [r[0]['name'] for r in hits19 if r[1] == 'L']
check("P-direction: 19-hits are few (<= 6)", len(hits19) <= 6, f"{len(hits19)} hits")
check("KILL LINE (prereg): zero 19-hits in a COLOURLESS quantity", len(colourless19) == 0, f"colourless: {colourless19}")
check("P-direction: 19's coloured fraction NOT significant vs base rate (hypergeometric p > 0.05)", not (t19[5] < 0.05), f"p = {t19[5]:.3f}")
# independence note: H_0 and t_0 carry 13/19 only through Omega_Lambda
dep = [r[0]['name'] for r in hits19 if 'H_0' in r[0]['name'] or 'age' in r[0]['name'].lower()]
print(f"\n   dependent hits (carry 19 through Omega_Lambda's 13/19): {dep}")
# the integer-content reading: fraction of all formulas that use N_c at all
usesNc = sum(1 for e in C if 'N_c' in ' '.join(str(e.get(k, '') or '') for k in FIELDS + ('bst_integers_used',)))
print(f"   integer-content reading ('19 is built from N_c'): {usesNc}/{len(C)} catalogue formulas mention N_c — as a rule it is near-vacuous")
print(f"   Keeper's first look (bare '19' regex) missed the '19.0' form: 13.0/19.0 and 6.0/19.0 are in formula_code.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
