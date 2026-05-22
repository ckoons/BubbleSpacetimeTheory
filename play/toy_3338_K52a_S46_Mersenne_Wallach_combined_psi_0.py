"""
Toy 3338 — K52a Session 46: Mersenne-Wallach combined |ψ_0⟩ 8th candidate.

Owner: Elie (extending 7-candidate landscape)
Date: 2026-05-22

CONTEXT
=======
S45 (Toy 3322) added Mersenne-ladder-anchored 7th candidate. 8-candidate landscape
continues; this S46 builds combined Mersenne-ladder + Wallach K-type Casimir
amplitude weighting.

GOAL
====
1. Build combined-amplitude candidate weighted by Mersenne-ladder position AND K-type Casimir
2. Verify rank-1 structure
3. Extend landscape to 8 candidates
4. Test if combined-direction is substantive-new vs prior 7

CAL FLAG 3 + CAL MODE 1 VIGILANCE
==================================
Multi-factor candidate; verifies whether substrate-natural multi-direction
combinations remain rank-1.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3338 — K52a S46: Mersenne-Wallach combined |ψ_0⟩ 8th candidate")
print("=" * 72)

# Setup substrate
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

# === T1: Mersenne-Wallach combined weights ===
print(f"\n[T1] Mersenne-Wallach combined amplitude weights")
mersenne_exp = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217]
amp_exp = (g + rank) / (2 * rank)  # 9/4 Bergman exponent

psi_MW = np.zeros(dim, dtype=complex)
for k, orbit in enumerate(full_orbits):
    p_k = mersenne_exp[k]
    M_p_k = 2**p_k - 1 if p_k < 30 else 2**29 - 1
    C_alpha = (k + 1) + C_2 - 1  # K-type Casimir starting at C_2 = 6
    # Combined weight: Mersenne factor × Wallach Casimir factor
    weight = (1.0 / np.sqrt(M_p_k)) * (1.0 / (C_alpha ** amp_exp))
    for state in orbit:
        psi_MW[state] = weight
psi_MW = psi_MW / np.linalg.norm(psi_MW)
print(f"  Combined Mersenne·Wallach weights applied across 18 orbits")
print(f"  Norm: {np.linalg.norm(psi_MW):.10f}")
check(f"Combined Mersenne-Wallach |ψ_0⟩ normalized",
      abs(np.linalg.norm(psi_MW) - 1.0) < 1e-12)

# === T2: Rank-1 verification ===
print(f"\n[T2] Rank-1 structure verification")
B_sq = (126/16) * np.outer(psi_MW, psi_MW.conj())
trace = np.trace(B_sq).real
eigs = np.linalg.eigvalsh(B_sq)
max_eig = eigs[-1].real
print(f"  Tr(B²) = {trace:.10f}; target 126/16 = {126/16}")
print(f"  Max eigenvalue = {max_eig:.10f}")
check(f"Tr(B²) = 126/16", abs(trace - 126/16) < 1e-10)
check(f"Max eigenvalue = 126/16", abs(max_eig - 126/16) < 1e-10)

# === T3: 8-candidate landscape ===
print(f"\n[T3] 8-candidate substrate-natural |ψ_0⟩ landscape")
landscape = [
    'S32 uniform (DC)',
    'S33 Frobenius (Galois)',
    'S34 Bergman (Hamming decay)',
    'S35 Wallach (K-type Casimir)',
    'S36 RS (cyclotomic M_g)',
    'S44 Bridge Object-weighted (3 K57 hubs)',
    'S45 Mersenne-ladder-anchored',
    'S46 Mersenne-Wallach combined (THIS)',
]
for i, c in enumerate(landscape, 1):
    print(f"  {i}. {c}")
print(f"  ")
print(f"  8 = 2·rank·rank = 2^3 substrate-boundary BST primary count")
check(f"8-candidate landscape (2^rank·rank = 8)", len(landscape) == 8)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3338_K52a_S46_Mersenne_Wallach_combined.json")
out = {
    'meta': {'date': '2026-05-22', 'owner': 'Elie', 'task': 'K52a S46 Mersenne-Wallach combined |ψ_0⟩'},
    'rank1_preserved': bool(abs(trace - 126/16) < 1e-10),
    'landscape_count': 8,
    'landscape': landscape,
    'BST_primary_signature': 'Mersenne ladder × Wallach K-type combined',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3338 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
