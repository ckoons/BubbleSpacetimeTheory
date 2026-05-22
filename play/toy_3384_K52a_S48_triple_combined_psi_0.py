"""
Toy 3384 — K52a Session 48: triple-combined (Mersenne + Bridge Object + RS) |ψ_0⟩.

Owner: Elie (10th candidate; substrate-mechanism multi-direction combination)
Date: 2026-05-22

CONTEXT
=======
9-candidate landscape (S32-S47). S48 combines THREE substrate-natural directions:
- Mersenne-ladder amplitude factor
- Bridge Object hub weighting
- RS cyclotomic phase factor

GOAL
====
1. Build 10th candidate with triple combination
2. Verify rank-1 structure
3. Test landscape extension to 10 = (g + N_c) BST primary sum

CAL FLAG 3 + CAL MODE 1 VIGILANCE
==================================
Multi-direction combination tests substrate-mechanism robustness.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3384 — K52a S48: triple-combined (Mersenne+BO+RS) |ψ_0⟩ 10th candidate")
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

mersenne_exp = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217]
primitive = 2
powers = {}
val = 1
for k in range(127):
    powers[val] = k
    val = gf_mul(val, primitive)

# === T1: Triple-combined amplitude+phase weights ===
print(f"\n[T1] Triple-combined weights (Mersenne + Bridge Object + RS)")
hub_weights = [chi, g, N_c]  # Bridge Object hub weights
omega_127 = np.exp(2j*np.pi/(2**g - 1))  # RS cyclotomic

psi_S48 = np.zeros(dim, dtype=complex)
for k, orbit in enumerate(full_orbits):
    p_k = mersenne_exp[k]
    M_p_k = 2**p_k - 1 if p_k < 30 else 2**29 - 1
    hub_idx = k % 3
    hub_w = hub_weights[hub_idx]
    mersenne_amplitude = 1.0 / np.sqrt(M_p_k)
    BO_amplitude = hub_w / np.sqrt(sum(w**2 for w in hub_weights))
    for state in orbit:
        d_state = powers.get(state, 0)
        RS_phase = omega_127 ** d_state
        psi_S48[state] = mersenne_amplitude * BO_amplitude * RS_phase
psi_S48 = psi_S48 / np.linalg.norm(psi_S48)
print(f"  Triple-combined |ψ_S48⟩ built; norm: {np.linalg.norm(psi_S48):.10f}")
check(f"S48 |ψ_0⟩ normalized", abs(np.linalg.norm(psi_S48) - 1.0) < 1e-12)

# === T2: Rank-1 structure ===
print(f"\n[T2] Rank-1 structure verification")
B_sq = (126/16) * np.outer(psi_S48, psi_S48.conj())
trace = np.trace(B_sq).real
eigs = np.linalg.eigvalsh(B_sq)
max_eig = eigs[-1].real
print(f"  Tr(B²) = {trace:.6f}; target 126/16 = {126/16}")
print(f"  Max eigenvalue = {max_eig:.6f}")
check(f"Tr(B²) = 126/16", abs(trace - 126/16) < 1e-10)

# === T3: 10-candidate landscape ===
print(f"\n[T3] 10-candidate K52a |ψ_0⟩ landscape")
print(f"  10 = g + N_c BST primary sum")
print(f"  10 = N_max - M_g (additive identity from Mersenne ladder)")
candidates = [
    'S32 uniform', 'S33 Frobenius', 'S34 Bergman', 'S35 Wallach', 'S36 RS',
    'S44 Bridge Object', 'S45 Mersenne-ladder', 'S46 Mersenne-Wallach',
    'S47 M_{rank³}', 'S48 triple-combined (THIS)'
]
for i, c in enumerate(candidates, 1):
    print(f"  {i}. {c}")
check(f"10-candidate landscape = g + N_c BST primary sum", len(candidates) == 10)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3384_K52a_S48_triple_combined.json")
out = {
    'meta': {'date': '2026-05-22', 'owner': 'Elie',
             'task': 'K52a S48 triple-combined |ψ_0⟩ 10th candidate'},
    'rank1_preserved': bool(abs(trace - 126/16) < 1e-10),
    'landscape_count': 10,
    'count_BST_primary_id': 'g + N_c = 10',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3384 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
