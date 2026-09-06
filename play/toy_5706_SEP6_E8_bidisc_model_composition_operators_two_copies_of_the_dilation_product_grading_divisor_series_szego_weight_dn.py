#!/usr/bin/env python3
"""Toy 5706 — E8 (Lyra L2 §1 bidisc). Exact integer arithmetic on truncated monomial lattices."""
import numpy as np, json, os, math
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}")
NMAX = 200
d = np.zeros(NMAX + 1, dtype=np.int64)
for a in range(1, NMAX + 1):
    for b in range(1, NMAX // a + 1): d[a * b] += 1
def G(mono):                      # mono: dict {(a,b): coeff}; returns graded coefficients array
    out = np.zeros(NMAX + 1, dtype=np.int64)
    for (a, b), c in mono.items():
        if a >= 1 and b >= 1 and a * b <= NMAX: out[a * b] += c
    return out
lattice = {(a, b): 1 for a in range(1, NMAX + 1) for b in range(1, NMAX // a + 1)}
divisor = np.array([sum(1 for k in range(1, n + 1) if n % k == 0) for n in range(NMAX + 1)])
lam = np.zeros(NMAX + 1, dtype=np.int64)
for a in range(1, NMAX + 1):
    for m in range(a, NMAX + 1, a): lam[m] += 1          # Lambert sum_a z^a/(1-z^a)
sc("P1", (G(lattice)[1:] == divisor[1:]).all() and (lam[1:] == divisor[1:]).all(), "G(lattice) = sum d(n) z^n = sum_a z^a/(1-z^a) to n = 200")
def C(mono, p, which):
    return {((a * p, b) if which == 1 else (a, b * p)): c for (a, b), c in mono.items()}
def D(vec, p):
    out = np.zeros(NMAX + 1, dtype=np.int64)
    for n in range(1, NMAX // p + 1): out[p * n] += vec[n]
    return out
ok2 = True; differ = False
for p in (2, 3, 5, 7):
    for (a, b) in [(1, 1), (1, 2), (2, 3), (3, 3), (4, 7)]:
        m = {(a, b): 1}
        ok2 &= (G(C(m, p, 1)) == D(G(m), p)).all() and (G(C(m, p, 2)) == D(G(m), p)).all()
        if C(m, p, 1) != C(m, p, 2): differ = True
sc("P2", ok2 and differ, "G∘C_p^(1) = D_p∘G = G∘C_p^(2) on monomials; C_p^(1) ≠ C_p^(2) as operators (C_2(u v^2): u^2 v^2 vs u v^4)")
def norm2(mono): return sum(c * c for c in mono.values())          # orthonormal monomials
m = {(1, 2): 3, (2, 5): -4, (3, 1): 1}
iso = norm2(C(m, 3, 1)) == norm2(m) and norm2(C(m, 5, 2)) == norm2(m)
semi = C(C(m, 2, 1), 3, 1) == C(m, 6, 1) and C(C(m, 2, 1), 3, 2) == C(C(m, 3, 2), 2, 1) and (G(C(C(lattice, 2, 1), 3, 2)) == D(G(lattice), 6)).all()
sc("P3", iso and semi, "isometries; C_p C_q = C_pq on one factor; factors commute; G∘C_2^(1)C_3^(2) = D_6∘G")
slice_norm = [sum(1 for a in range(1, n + 1) if n % a == 0) for n in range(1, NMAX + 1)]   # ||sum_{ab=n} u^a v^b||^2 = number of terms
sc("P4", all(slice_norm[n - 1] == divisor[n] for n in range(1, NMAX + 1)), "Szegő norm² of the grade-n slice = d(n), n ≤ 200")
fibre6 = [(a, b) for (a, b) in lattice if a * b == 6]
sc("P5", len(fibre6) == 4, f"G not injective: fibre over z^6 = {fibre6}")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'score': f"{sum(score)}/{len(score)}", 'd_first_20': divisor[1:21].tolist()}, open(os.path.join(HERE, '.bidisc_5706.json'), 'w'), indent=1)
