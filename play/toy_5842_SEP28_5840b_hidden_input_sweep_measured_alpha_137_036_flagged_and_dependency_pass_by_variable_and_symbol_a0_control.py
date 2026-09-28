#!/usr/bin/env python3
"""
Toy 5842 = 5840b (Elie, 2026-09-28, round 18 Lane A). Prereg b6dc9896 (hashed before code or read).
Changes vs 5840: (a) α whitelist = {1/137, 137} only — 137.036… and 0.0072973… are the MEASURED α (flagged);
(b) dependency pass 1: formula_code identifiers outside the namespace/math functions; (c) pass 2: fixed measured-symbol list in chains.
Every flag is printed for READING. Controls: const_046 (a₀) via pass 1; const_100 via the literal pass and pass 2.
"""
import json, re, math, keyword
from fractions import Fraction
D = json.load(open('data/bst_constants.json')); C = D['constants']
NS = {'pi', 'alpha', 'alpha_inv', 'N_c', 'n_C', 'g', 'C_2', 'N_max', 'rank', 'm_e', 'm_p', 'hbar_c', 'pi5'}
FUNCS = set(D['meta']['eval_namespace'].get('math_functions', [])) | {'math', 'e'}
MATH = {'pi': math.pi, 'e': math.e, 'zeta3': 1.2020569031595942, 'ln2': math.log(2), 'ln10': math.log(10),
        'gammaE': 0.5772156649015329, 'sqrt2': math.sqrt(2), 'sqrt3': math.sqrt(3)}
RULER = [0.511, 0.51099895, 0.5109989]
ALPHA_BST = [1/137, 137.0]
num = re.compile(r"(?<![\w.])(\d+\.\d*(?:[eE][+-]?\d+)?|\d+[eE][+-]?\d+|\.\d+)(?![\w])")
def sig6(a, b): return b != 0 and abs(a/b - 1) < 5e-6
def classify(tok):
    v = float(tok)
    if v == int(v) and 'e' not in tok.lower(): return 'int'
    if any(sig6(v, r) for r in RULER): return 'ruler'
    if any(sig6(v, a) for a in ALPHA_BST): return 'alpha_BST'
    if any(sig6(v, m) or sig6(v, 1/m) for m in MATH.values()): return 'math'
    fr = Fraction(v).limit_denominator(30)
    if fr.denominator > 1 and abs(fr.numerator) <= 100 and sig6(v, float(fr)): return 'rational'
    if sig6(v, 137.035999177) or sig6(v, 1/137.035999177): return 'FLAG-measured-alpha'
    return 'FLAG'
SYMS = [r"\bH_0\b", r"\bH0\b", "H₀", r"\bomega_m\b", r"Omega_m h\^2", r"\bm_tau\b", "m_τ", r"\bG_F\b", r"\bm_Z\b", r"\bT_CMB\b", r"\bT_0\b",
        "CODATA", "Planck 2018", r"\bPDG\b", r"\b67\.29\b", r"\b0\.1430\b"]
ident = re.compile(r"\b[A-Za-z_][A-Za-z_0-9]*\b")
rows = {}
for e in C:
    rid = e.get('id') or e.get('theorem_id') or e['name']
    code = str(e.get('formula_code', '') or '')
    dc = e.get('derivation_chain') or []; chain = ' | '.join(dc) if isinstance(dc, list) else str(dc)
    hits = []
    for field, t in (('code', code), ('chain', chain)):
        for m in num.finditer(t):
            c = classify(m.group(1))
            if c.startswith('FLAG'): hits.append((field, c, m.group(1)))
    for name in set(ident.findall(code)):
        if name not in NS and name not in FUNCS and not keyword.iskeyword(name) and not name.isdigit():
            hits.append(('code', 'VAR', name))
    for s in SYMS:
        if re.search(s, chain): hits.append(('chain', 'SYM', s.replace('\\b', '')))
    if hits: rows[rid] = (e['name'], code, chain, hits)
prev = {'const_110', 'const_123', 'const_082', 'const_114', 'const_113', 'const_037', 'const_038', 'const_101', 'const_102', 'const_100',
        'const_031', 'Proton charge radius', 'const_115', 'const_012', 'const_046'}
print(f"rows scanned {len(C)}; rows with any flag {len(rows)}")
alpha_rows = [r for r, v in rows.items() if any(h[1] == 'FLAG-measured-alpha' for h in v[3])]
var_rows = [r for r, v in rows.items() if any(h[1] == 'VAR' for h in v[3])]
sym_rows = [r for r, v in rows.items() if any(h[1] == 'SYM' for h in v[3])]
print(f"measured-α literal rows: {alpha_rows}\nimport-by-variable rows: {var_rows}\nimport-by-symbol rows: {sym_rows}")
print("\nNEW vs 5840/R177 (read each):")
for rid, (name, code, chain, hits) in rows.items():
    if rid in prev: continue
    interesting = [h for h in hits if h[1] in ('FLAG-measured-alpha', 'VAR', 'SYM') or h[0] == 'code']
    if not interesting: continue
    print(f"--- {rid} | {name}\n    code: {code}\n    hits: {interesting}\n    chain: {chain[:400]}")
score = []
def check(n, ok): score.append(ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}")
check("CONTROL: const_046 (a₀) caught by the dependency pass (H_0 by variable)", 'const_046' in var_rows)
check("CONTROL: const_100 caught by the literal pass and by pass 2", 'const_100' in rows and 'const_100' in sym_rows)

# ---- POST-READ ADDITIONS (added after reading the 30 new rows; labelled, not in the prereg) ----
# (d) EVALUABILITY: the file's meta says 'Every formula evaluates in namespace {…}'. Evaluate every formula_code in exactly that namespace.
import sympy
N_c, n_C, g, C_2, N_max, rank = 3, 5, 7, 6, 137, 2
env = dict(pi=math.pi, alpha=1/N_max, alpha_inv=N_max, N_c=N_c, n_C=n_C, g=g, C_2=C_2, N_max=N_max, rank=rank,
           m_e=0.51099895, hbar_c=197.3269804, pi5=math.pi**5, math=math)
env['m_p'] = 6*math.pi**5*env['m_e']
for fn in ('sqrt', 'log', 'exp', 'sin', 'cos', 'tan', 'atan', 'asin', 'acos', 'factorial', 'comb'): env[fn] = getattr(math, fn)
env.update(cbrt=lambda x: x**(1/3), ln=math.log, Fraction=Fraction, abs=abs, pow=pow, float=float)
fails = []
for e in C:
    code = str(e.get('formula_code', '') or '').strip()
    rid = e.get('id') or e['name']
    if not code: fails.append((rid, 'EMPTY')); continue
    try: eval(code, {'__builtins__': {}}, env)
    except Exception as ex: fails.append((rid, type(ex).__name__ + ': ' + str(ex)[:60]))
print(f"\n(d) EVALUABILITY in the stated namespace: {len(C) - len(fails)}/{len(C)} evaluate; failures:")
for f in fails: print("    ", f)
check("(d) [post-read] every formula_code evaluates in the file's stated namespace (the meta's own claim)", len(fails) == 0)
# (e) the Chern classes of Q^5 (for the c_2/c_3 fix): c(Q^n) = (1+h)^{n+2}/(1+2h)
hs = sympy.Symbol('h')
ch = sympy.series((1 + hs)**7/(1 + 2*hs), hs, 0, 6).removeO()
cs = [int(ch.coeff(hs, k)) for k in range(6)]
print(f"(e) Chern classes of Q^5 from (1+h)^7/(1+2h): c_0..c_5 = {cs}")
check("(e) [post-read] c_1 = 5, c_2 = 11, c_3 = 13 (the values the 11 rows' c_2, c_3 must mean) — computed, a source for the namespace fix", cs[1:4] == [5, 11, 13])
print(f"\nSCORE: {sum(score)}/{len(score)}   (controls + post-read checks; the finding is the READ list)")
