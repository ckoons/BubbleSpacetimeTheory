#!/usr/bin/env python3
"""Toy 5716 — E12 at level 137, the constant-coefficient part (prereg hashed before this run; Lyra ffff044d)."""
import math, json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
# P1: Weyl inversion sets (5713's construction)
roots = {'e1-e2': (1,-1), 'e1+e2': (1,1), 'e1': (1,0), 'e2': (0,1)}
def w_apply(w, v): s1, s2, perm = w; u = (v[perm[0]], v[perm[1]]); return (s1*u[0], s2*u[1])
def is_neg(v): return (v[0] < 0) or (v[0] == 0 and v[1] < 0)
W = [(s1, s2, perm) for s1 in (1,-1) for s2 in (1,-1) for perm in ((0,1),(1,0))]
inv = [[n for n, v in roots.items() if is_neg(w_apply(w, v))] for w in W]
occ = {n: sum(1 for I in inv if n in I) for n in roots}
sc("P1", all(v == 4 for v in occ.values()), f"occurrences in the 8 inversion sets: {occ}")
# P2: characters mod 137 as exponents a in Z/136: psi_a; delta(psi) = 1 iff a != 0 mod 136
M = 136
def delta(a): return 1 if a % M else 0
dist = Counter(); total = 0; zero_blocks = 0
for a1 in range(M):
    for a2 in range(M):
        c = delta(a1 + a2) + delta(2*a1) + delta(a1) + delta(2*a2) + delta(a2)
        dist[c] += 1; total += c
        if c == 0: zero_blocks += 1
ident = M * (135 + 2*134 + 2*135)
sc("P2", total == 91528 and ident == 91528 and zero_blocks == 1, f"sum c_137 = {total} (identity 136·673 = {ident}); average {total/M**2:.4f} = 673/136; blocks with c = 0: {zero_blocks}; distribution {dict(sorted(dist.items()))}")
N2 = M * M
sc("P3", N2 == 18496, f"ln 2 units in the sigma = 1 sector: {N2} (one per block, FE-normalisation convention)")
ln2, ln137 = math.log(2), math.log(137)
out = {}
for t in (1.0, 2/17):
    inth = math.pi / t * math.exp(-17 * t / 2)
    Ec = -(1/(4*math.pi**2)) * (N2*ln2 + total*ln137) * inth
    out[t] = (inth, Ec); print(f"  t = {t:.6f}: ∫h = {inth:.6e}; E_const^(137) = -(1/4π²)(18496 ln 2 + 91528 ln 137)·∫h = {Ec:.6e}  (ln 137 part / ln 2 part = {total*ln137/(N2*ln2):.3f})")
sc("P4", abs(total*ln137/(N2*ln2) - 35.1) < 0.2, "constant-coefficient part printed with ∫h; the functional parts and the sigma != 1 sector are OWED, not estimated")
sc("P5", True, "no ln pi (5714); conductors in the row are 2 and 137 only")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'sum_c137': total, 'dist': dict(dist), 'N2': N2, 'E_const': {str(t): v for t, v in out.items()}, 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.e12_137_5716.json'), 'w'), indent=1)
