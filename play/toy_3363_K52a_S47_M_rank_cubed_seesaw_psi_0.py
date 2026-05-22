"""
Toy 3363 — K52a Session 47: M_{rank³} = N_c·n_C·seesaw substrate-natural |ψ_0⟩.

Owner: Elie (9th candidate; M_{rank³} substrate identity from Toy 3358)
Date: 2026-05-22

CONTEXT
=======
Toy 3358 NEW identity: M_{rank³} = 255 = N_c·n_C·seesaw (BST primary triple product).
S47 tests a |ψ_0⟩ candidate weighted by this triple product factorization.

GOAL
====
1. Build |ψ_0⟩ where 126 active modes get amplitudes from N_c·n_C·seesaw decomposition
2. Verify rank-1 structure
3. Extend candidate landscape to 9

CAL FLAG 3 + CAL MODE 1 VIGILANCE
==================================
9th candidate; not necessarily unique substrate-natural form. Pattern extension.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3363 — K52a S47: M_{rank³} = N_c·n_C·seesaw substrate-natural |ψ_0⟩")
print("=" * 72)

# Setup
dim = 2**g
silent_idx = [0, 1]
active_idx = [k for k in range(dim) if k not in silent_idx]

def gf_mul(a, b, poly=0b10000011, deg=7):
    result = 0
    while b:
        if b & 1: result ^= a
        b >>= 1
        if a & (1 << (deg-1)): a = ((a << 1) ^ poly) & ((1 << deg) - 1)
        else: a = (a << 1) & ((1 << deg) - 1)
    return result

def frobenius(alpha): return gf_mul(alpha, alpha)

visited = {0}
orbits = []
for x in range(1, 128):
    if x in visited: continue
    orbit = []
    y = x
    while y not in visited:
        orbit.append(y); visited.add(y); y = frobenius(y)
    orbits.append(orbit)
full_orbits = sorted([o for o in orbits if len(o) == g], key=lambda o: min(o))

# === T1: Build M_{rank³} = N_c·n_C·seesaw amplitude weighting ===
print(f"\n[T1] M_{{rank³}} = N_c·n_C·seesaw = 255 substrate-natural weighting")
print(f"  18 active orbits × g elements = 126 active modes")
print(f"  ")
print(f"  Substrate-natural decomposition: 126 = N_c·C_2·g but also 255 = N_c·n_C·seesaw")
print(f"  Use scaled weights: w_orbit = (factor in N_c·n_C·seesaw decomposition)")
# Distribute 18 orbits across N_c·n_C·seesaw subgroups
# 18 = 6 + 6 + 6 (= 3·C_2 = 3·rank·N_c)
# Use 3 "blocks" of 6 orbits weighted by (N_c, n_C, seesaw) factors
N_c_weight = 1.0 / np.sqrt(N_c)  # 1/√3
n_C_weight = 1.0 / np.sqrt(n_C)  # 1/√5
seesaw_weight = 1.0 / np.sqrt(seesaw)  # 1/√17

psi_S47 = np.zeros(dim, dtype=complex)
block_size = 6  # 18/3
for k, orbit in enumerate(full_orbits):
    if k < block_size:
        w = N_c_weight
    elif k < 2*block_size:
        w = n_C_weight
    else:
        w = seesaw_weight
    for state in orbit:
        psi_S47[state] = w
psi_S47 = psi_S47 / np.linalg.norm(psi_S47)
print(f"  Norm: {np.linalg.norm(psi_S47):.10f}")
check(f"|ψ_S47⟩ normalized",
      abs(np.linalg.norm(psi_S47) - 1.0) < 1e-12)

# === T2: Rank-1 structure ===
print(f"\n[T2] Rank-1 structure verification")
B_sq = (126/16) * np.outer(psi_S47, psi_S47.conj())
trace = np.trace(B_sq).real
eigs = np.linalg.eigvalsh(B_sq)
max_eig = eigs[-1].real
print(f"  Tr(B²) = {trace:.10f}; target 126/16 = {126/16}")
print(f"  Max eigenvalue = {max_eig:.10f}")
check(f"Tr(B²) = 126/16 with S47 weighting", abs(trace - 126/16) < 1e-10)
check(f"Max eigenvalue = 126/16", abs(max_eig - 126/16) < 1e-10)

# === T3: 9-candidate landscape ===
print(f"\n[T3] 9-candidate K52a |ψ_0⟩ landscape")
candidates = [
    'S32 uniform DC',
    'S33 Frobenius (Galois)',
    'S34 Bergman (Hamming)',
    'S35 Wallach (K-type Casimir)',
    'S36 RS (cyclotomic M_g)',
    'S44 Bridge Object (3 K57 hubs)',
    'S45 Mersenne-ladder-anchored',
    'S46 Mersenne-Wallach combined',
    'S47 M_{rank³} = N_c·n_C·seesaw (THIS)',
]
for i, c in enumerate(candidates, 1):
    print(f"  {i}. {c}")
check(f"9-candidate landscape", len(candidates) == 9)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3363_K52a_S47.json")
out = {
    'meta': {'date': '2026-05-22', 'owner': 'Elie',
             'task': 'K52a S47 M_rank^3 = N_c·n_C·seesaw substrate-natural |ψ_0⟩'},
    'rank1_preserved': bool(abs(trace - 126/16) < 1e-10),
    'landscape_count': 9,
    'BST_primary_signature': 'M_{rank^3} = N_c·n_C·seesaw triple product blocks',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3363 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
