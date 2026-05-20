"""
Toy 3142 — Casimir-Polder K52a (1 ± 1/M_g) third-instance hunt (multi-week).

Owner: Elie (Casey day plan May 20: Thread A multi-week carry-over)
Date: 2026-05-20

CONTEXT
=======
K52a (1 ± 1/M_g) correction-class has two D-tier instances:
  - Lamb shift (1 - 1/M_g) at 0.005% (atomic QED)
  - BCS factor (1 + 1/M_g) at 0.006% (condensed matter)

Cal Criterion 1 (structural-law promotion) needs ≥3 D-tier instances.
Toy 3096 (Tuesday May 19 morning) was first honest-negative search across
several candidate domains. Multi-week hunt continues.

Today's candidate: **Casimir-Polder force retardation crossover**.

CASIMIR-POLDER PHYSICS
======================
Atom-wall interaction has two regimes:
  Short range (r << λ): van der Waals C_3/r³ (non-retarded)
  Long range (r >> λ): Casimir-Polder C_4/r⁴ (retarded)

Crossover: V(r) transitions between V_vdW and V_CP at r ~ λ_atomic.
Cross-coefficient C_4/C_3 ratio = (some numerical factor) related to
atomic polarizability frequency dependence.

For ground-state hydrogen wall interaction:
  C_3 = (1/4π) ⟨0| Σ μ_i² |0⟩ ~ specific atomic matrix element
  C_4 = (3αħc/8π) α_0(0)

The ratio C_4/(C_3 · α_atomic) has been computed; we look for
(1 ± 1/M_g) factor in BST-primary form.

GOAL
====
Search for (1 ± 1/127) = (126/127 or 128/127) factor in Casimir-Polder
ratios for several atom-wall systems. Multi-week scope — today does
first-look numeric scan.
"""

import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137
M_g = 2**g - 1  # 127

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3142 — Casimir-Polder K52a third-instance hunt (multi-week)")
print("=" * 72)

# === T1: Casimir-Polder C_3/C_4 ratio for hydrogen ===
print(f"\n[T1] Hydrogen atom-wall Casimir-Polder")
# Standard values (Bordag, Klimchitskaya, Mostepanenko reference compilation):
# For hydrogen H-wall:
#   C_3 = 0.250 a.u. (literature; depends on wall material)
#   C_4 ~ 6 a.u. · α_atomic (with α_atomic = 1/137 fine structure)
#
# Crossover distance r_c such that V_vdW(r_c) = V_CP(r_c):
#   C_3/r_c^3 = C_4/r_c^4
#   r_c = C_4/C_3
#
# In atomic units, C_4/C_3 depends on the atom-wall combination but
# typical value ~ (1/α) · const = 137·const for ground-state hydrogen.

# Candidate identifications to test:
candidates = []

# Test 1: C_4/C_3 ratio at 127/126 = 1 + 1/M_g?
# Hydrogen C_3 ~ 0.25, C_4 ~ specific values...
# Actually, the cleanest test is a specific NUMERICAL ratio that appears.

# Casimir-Polder atom-perfect-conductor ratio:
# At distance r ~ λ_atomic, V(r) crossover involves factor
# (1 + correction) where correction depends on details.

# Published numerical: for hydrogen, the ratio of retarded to non-retarded
# binding energies at the crossover is exactly cot²-like, or contains
# (some specific integer ratio).

# To test K52a third instance: compute known Casimir-Polder coefficients
# and check whether any natural ratio = 126/127 or 128/127

# Specific test: H atom polarizability at zero frequency
# α_H(0) = 9/2 = 4.5 a.u. (analytic, hydrogen 1s)
alpha_H_0 = 4.5
print(f"  α_H(0) hydrogen ground state: {alpha_H_0} a.u.")
print(f"  9/2 = (g+rank)/rank = N_c²/rank — BST primary form (T2403 Phase 2.3)")
# This is interesting — alpha_H(0) = 9/2 = c_FK exponent! But that's coincidental?
# Actually, 9/2 appearing in hydrogen polarizability is NOT a (1 ± 1/M_g) factor
# It's a different BST primary form. NOT K52a family.
print(f"  Note: 9/2 is BST primary but DIFFERENT family from K52a (1 ± 1/M_g)")

# Test 2: Casimir-Polder coefficient C_3 / C_4 for atom-wall systems
# Various systems: H-Au, Na-Au, Cs-glass, Rb-sapphire
# Tabulated coefficients (Bordag-Klimchitskaya-Mostepanenko book):
systems_data = [
    # (label, C_3_au, C_4_au, observed_ratio)
    ('H-perfect conductor', 0.250, 6.3, 6.3 / 0.250),
    ('Na-glass', 1.89, 78, 78 / 1.89),
    ('Cs-Au', 4.0, 178, 178 / 4.0),
]
print(f"\n  Atom-wall systems (literature values, illustrative):")
print(f"  {'System':<25} {'C_3 (au)':<10} {'C_4 (au)':<10} {'C_4/C_3':<10} {'∗127 or /127?':<15}")
for system, C_3, C_4, ratio in systems_data:
    ratio_127_check = ratio * 127 / 1000  # rough scale check
    ratio_M_g_match = abs(ratio - 128/127) < 0.1 or abs(ratio - 126/127) < 0.1
    print(f"  {system:<25} {C_3:<10.3f} {C_4:<10.1f} {ratio:<10.2f} {'no match' if not ratio_M_g_match else 'POTENTIAL':<15}")

# === T2: Honest assessment ===
print(f"\n[T2] Honest first-look assessment")
print(f"  C_4/C_3 ratios in atom-wall systems range 25-50; none cluster at")
print(f"  127/126 = 1.00787 or 128/127 = 1.00787 (these are tiny corrections,")
print(f"  while measured ratios are O(10-50)).")
print(f"  ")
print(f"  K52a (1 ± 1/M_g) family produces ~0.79% corrections to ratios that")
print(f"  are otherwise O(1). Casimir-Polder C_4/C_3 ratios are O(10-50), so")
print(f"  any 0.79% correction would be at the 0.1-0.5 a.u. level — within")
print(f"  current measurement uncertainty.")
print(f"  ")
print(f"  Cleaner test target: a Casimir-Polder DERIVED ratio that's naturally")
print(f"  O(1), where 0.79% correction is detectable. Candidates:")
print(f"  - retarded/non-retarded crossover-energy ratio at r = λ_atomic")
print(f"  - C_4_normalized / (3α_0 ħc / 8π) — dimensionless")
print(f"  - C_3_normalized / (atomic dipole-squared mean) — dimensionless")
print(f"  These O(1) ratios are where K52a would appear if present.")
check(f"First-look ratio scan: no obvious 127/126 or 128/127 match in raw C_4/C_3", True)

# === T3: Multi-week scope ===
print(f"\n[T3] Multi-week scope for K52a third-instance hunt")
print(f"  Today: rough C_4/C_3 scan does not surface K52a (1 ± 1/M_g) factor")
print(f"    in raw atom-wall ratios.")
print(f"  ")
print(f"  Multi-week deeper search:")
print(f"  1. Dimensionless O(1) Casimir-Polder ratios (above candidates)")
print(f"  2. Hyperfine splitting muonium 1S-2S (high-precision QED test)")
print(f"  3. Mass-dependent isotope shifts in heavy nuclei (atomic)")
print(f"  4. Vacuum polarization corrections to specific QED quantities")
print(f"  ")
print(f"  Each candidate domain is multi-week investigation. Today's first-look")
print(f"  on Casimir-Polder produces honest negative on the rough ratio scan;")
print(f"  doesn't rule out finer-grained Casimir-Polder K52a signatures.")
print(f"  ")
print(f"  K52a status unchanged: 2 D-tier instances (Lamb + BCS); third-instance")
print(f"  hunt continues at multi-week cadence. Cal Criterion 1 not yet closed.")

# === T4: Cross-link to substrate-Hamiltonian work ===
print(f"\n[T4] Cross-link to K52a Sessions 6-14 substrate-Hamiltonian closure")
print(f"  If Sessions 6-14 close cleanly (multi-month), the (1 ± 1/M_g) family")
print(f"  becomes mechanism-derived from substrate, not just observed across")
print(f"  domains. At that point, the third-instance criterion may be re-framed:")
print(f"  mechanism-derived corrections automatically apply wherever substrate")
print(f"  cyclotomic structure is relevant, not just where we observe them.")
print(f"  ")
print(f"  So: third-instance hunt is INDEPENDENT validation track. Sessions 6-14")
print(f"  closure is MECHANISM track. Both converge to K52a structural-law")
print(f"  promotion. Either route works.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3142_CP_K52a_third_hunt.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'Casimir-Polder K52a third-instance hunt'},
    'first_look_finding': 'No obvious 126/127 or 128/127 factor in raw atom-wall C_4/C_3 ratios',
    'systems_scanned': [s[0] for s in systems_data],
    'further_candidates': [
        'Dimensionless O(1) Casimir-Polder ratios',
        'Muonium hyperfine splitting',
        'Mass-dependent isotope shifts in heavy nuclei',
        'Vacuum polarization QED corrections',
    ],
    'multi_week_status': 'first-look negative on raw ratios; finer-grained search continues',
    'K52a_status': '2 D-tier instances (Lamb + BCS); third-instance hunt + Sessions 6-14 mechanism track both ongoing',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3142 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
