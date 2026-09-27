#!/usr/bin/env python3
"""
Toy 5840 — the H₀ species sweep (Elie, 2026-09-27, round 17 Lane B). Prereg 67c5534c (rules fixed before code).
Flags every DECIMAL literal in formula_code / derivation_chain of data/bst_constants.json that is not: the ruler m_e, α (1/137, 137.036),
a math constant recognised by value (π, e, ζ(3), ln2, ln10, γ_E, √2, √3), or a simple rational p/q (q ≤ 30) written in decimal.
Integers are counted separately (informational). Every flagged row is printed IN FULL for reading; the classification (S/U/V/D/O) is done
by the reader in the board post, not by this script. CONTROL: const_100 (H₀) must be flagged.
"""
import json, re, math
from fractions import Fraction
C = json.load(open('data/bst_constants.json'))['constants']
MATH = {'pi': math.pi, 'e': math.e, 'zeta3': 1.2020569031595942, 'ln2': math.log(2), 'ln10': math.log(10),
        'gammaE': 0.5772156649015329, 'sqrt2': math.sqrt(2), 'sqrt3': math.sqrt(3)}
RULER = [0.511, 0.51099895, 0.5109989, 0.51099895000, 0.510998950]
ALPHA = [1/137, 137.036, 137.035999, 137.035999177, 0.0072973525693, 0.00729735]
num = re.compile(r"(?<![\w.])(\d+\.\d*(?:[eE][+-]?\d+)?|\d+[eE][+-]?\d+|\.\d+)(?![\w])")
def sig6(a, b): return b != 0 and abs(a/b - 1) < 5e-6
def classify(tok):
    v = float(tok)
    if v == int(v) and 'e' not in tok.lower(): return 'int'                  # 16.0, 3.0 → integer written with a point
    if any(sig6(v, r) for r in RULER): return 'ruler'
    if any(sig6(v, a) for a in ALPHA): return 'alpha'
    if any(sig6(v, m) or sig6(v, 1/m) for m in MATH.values()): return 'math'
    fr = Fraction(v).limit_denominator(30)
    # run 1 had no numerator bound: 938.272 ≈ 10321/11, 1089.71 ≈ 26153/24, 96485.33212 ≈ 289456/3 … were swallowed. 'Simple' = |p| ≤ 100.
    if fr.denominator > 1 and abs(fr.numerator) <= 100 and sig6(v, float(fr)): return f'rational {fr}'
    return 'FLAG'
flagged = {}; ints = 0; counts = {}
for e in C:
    rid = e.get('id') or e.get('theorem_id') or e['name']
    texts = [('formula_code', str(e.get('formula_code', '') or ''))]
    dc = e.get('derivation_chain') or []
    texts += [('derivation_chain', ' | '.join(dc) if isinstance(dc, list) else str(dc))]
    for field, t in texts:
        for m in num.finditer(t):
            c = classify(m.group(1)); counts[c.split()[0]] = counts.get(c.split()[0], 0) + 1
            if c == 'FLAG': flagged.setdefault((rid, e['name']), []).append((field, m.group(1)))
print(f"entries {len(C)}; literal classes: {counts}")
print(f"FLAGGED ROWS: {len(flagged)}\n")
for (rid, name), toks in flagged.items():
    e = next(x for x in C if (x.get('id') or x.get('theorem_id') or x['name']) == rid and x['name'] == name)
    print(f"--- {rid} | {name} | tier {e.get('tier')} | status {e.get('status')} | observed {e.get('observed_value')}")
    print(f"    formula_code: {e.get('formula_code')}")
    print(f"    flagged: {toks}")
ok = any(n == 'Hubble constant H_0' or 'Hubble' in n for (_, n) in flagged)
print(f"\n[{'PASS' if ok else 'FAIL'}] CONTROL: const_100 (H₀) is flagged")
print(f"\nSCORE: {1 if ok else 0}/1   (the instrument's only scored check; the finding is the list, classified by reading)")
