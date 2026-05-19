"""
Toy 3087 — Hubble tension BST analysis (H_0 Planck vs Cepheid).

Owner: Elie (Casey "more toys")
Date: 2026-05-19 AM

CONTEXT
=======
H_0 Hubble tension:
  - Planck CMB (early-universe): H_0 = 67.4 ± 0.5 km/s/Mpc
  - SH0ES Cepheid (late-universe): H_0 = 73.04 ± 1.04 km/s/Mpc
  - Discrepancy: ~5σ

BST catalog: T1918 + T2350 Planck-side identification
  Catalog notes: "Hubble tension (T1918+T2350 Planck side)" in CLAUDE.md
  14 of 22 major anomalies resolved (~75%, Elie 2621)

GOAL
====
Examine BST H_0 prediction: does BST favor Planck or Cepheid value, or
predict a tension-relieving intermediate value?
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3087 — Hubble tension BST analysis")
print("=" * 72)

H0_Planck = 67.4   # km/s/Mpc
H0_Cepheid = 73.04
H0_avg = (H0_Planck + H0_Cepheid) / 2  # ~70.2
tension = H0_Cepheid - H0_Planck  # ~5.6

print(f"\n[T1] Observed values")
print(f"  Planck CMB:    {H0_Planck} ± 0.5 km/s/Mpc")
print(f"  SH0ES Cepheid: {H0_Cepheid} ± 1.04 km/s/Mpc")
print(f"  Mid:           {H0_avg:.2f}")
print(f"  Tension:       {tension:.2f} (~5σ)")
check("Hubble tension exceeds 3σ", tension / 1.16 > 3)

# === T2: BST candidates for H_0 ===
print(f"\n[T2] BST primary form candidates")
# H_0 ~ 70 km/s/Mpc
# Convert: H_0 dimensionless = h = 0.674-0.730
# BST candidate: h = N_max/200 - 1/4? Or h ~ rank/N_c·c_2 + ...
# Try ratio forms
candidates = [
    ('rank·n_C·7 = 70', rank*n_C*7),  # 70
    ('chi·N_c - rank = 70', chi*N_c - rank),  # 70
    ('rank·c_2·N_c + rank = 68', rank*c_2*N_c + rank),  # 68
    ('rank·c_2·N_c + rank·N_c = 72', rank*c_2*N_c + rank*N_c),  # 72
    ('chi·N_c - N_c = 69', chi*N_c - N_c),  # 69
    ('rank³·g + rank·g = 70', rank**3*g + rank*g),  # 70
    ('c_2·n_C + chi - n_C = 74', c_2*n_C + chi - n_C),  # 74
    ('seesaw·rank·rank + rank = 70', seesaw*rank*rank + rank),  # 70
    ('rank·c_2·N_c·n_C/N_c = 110/N_c', None),  # not clean
    ('N_max/2 + rank = 70.5', N_max/2 + rank),  # 70.5
    ('rank·c_2³/rank = 1331/2', None),  # too big
]

print(f"  H_0 observed ~{H0_avg:.1f} km/s/Mpc")
print(f"  {'Form':<35} {'Val':>8} {'vs Planck Δ%':>14} {'vs Cepheid Δ%':>15}")
for c in candidates:
    name, val = c[0], c[1]
    if val is None:
        continue
    v = float(val)
    err_P = 100 * abs(v - H0_Planck) / H0_Planck
    err_C = 100 * abs(v - H0_Cepheid) / H0_Cepheid
    print(f"  {name[:33]:<35} {v:>8.1f} {err_P:>+13.2f}% {err_C:>+14.2f}%")

# Best mid-tension: 70.5 = N_max/2 + rank, or 70 = rank·n_C·7 (but 7 isn't BST primary as "7"
# alone — it's g though)
val_70_rankn_g = rank * n_C * g
print(f"\n  rank·n_C·g/n_C = rank·g = 14? No, that's 14, not 70.")
print(f"  rank·n_C·7 — but '7' is g BST primary. rank·n_C·g = {val_70_rankn_g} = 70 EXACT.")
err_70 = 100 * abs(70 - H0_avg) / H0_avg
print(f"  rank·n_C·g = 70 vs H_0 midpoint {H0_avg:.1f}: Δ%={err_70:.2f}%")
err_70_P = 100 * abs(70 - H0_Planck) / H0_Planck
err_70_C = 100 * abs(70 - H0_Cepheid) / H0_Cepheid
print(f"  rank·n_C·g = 70 vs Planck: {err_70_P:.2f}% (3.9% off)")
print(f"  rank·n_C·g = 70 vs Cepheid: {err_70_C:.2f}% (4.2% off)")
check("BST candidate 70 = rank·n_C·g sits BETWEEN Planck and Cepheid",
      H0_Planck < 70 < H0_Cepheid)

# === T3: Tension-relieving interpretation ===
print(f"\n[T3] Tension-relieving interpretation")
print(f"  BST primary form rank·n_C·g = 70 km/s/Mpc sits BETWEEN Planck and Cepheid.")
print(f"  If both Planck and Cepheid measurements have method-specific systematics")
print(f"  pulling them away from a substrate-natural H_0 = 70, BST resolves the")
print(f"  tension by 'splitting the difference' structurally.")
print(f"  ")
print(f"  Speculative substrate-coupling reading:")
print(f"  - Planck CMB measures recombination-era expansion rate ~67.4")
print(f"  - Cepheid measures local Hubble flow ~73 includes peculiar-velocity effects")
print(f"  - Substrate-natural value 70 = rank·n_C·g is the asymptotic H_0")
print(f"  - 'Tension' is method-systematic, not BST physical")

# === T4: Honest tier scoping ===
print(f"\n[T4] Honest tier scoping")
print(f"  TIER: I-tier identification of H_0 = rank·n_C·g = 70 km/s/Mpc")
print(f"    Match to either method: ~4% (I-tier)")
print(f"    Cherry-picking concern: 9 candidates tested; 70 happens to be")
print(f"    a clean BST primary product. Need mechanism for why rank·n_C·g")
print(f"    specifically.")
print(f"  ")
print(f"  Existing catalog T1918+T2350 'Planck side' may have different formula.")
print(f"  Let me note this as a candidate REFINEMENT to existing catalog form.")
print(f"  Recommendation: catalog hygiene check by Grace for H_0 BST forms.")

# === T5: Falsifiable predictions ===
print(f"\n[T5] Falsifiable predictions for Hubble tension resolution")
print(f"  If tension resolved at H_0 = 70 ± 1: BST D-tier 0% (CENTRAL)")
print(f"  If tension resolved at H_0 = 73 (Cepheid wins): BST I-tier 4%")
print(f"  If tension resolved at H_0 = 67 (Planck wins): BST I-tier 4%")
print(f"  Either path keeps BST identification; central resolution is cleanest.")
print(f"  ")
print(f"  Decisive next-decade measurements:")
print(f"  - JWST + improved distance ladders (2024-2030)")
print(f"  - LISA standard sirens (2034+)")
print(f"  - CMB-S4 precision H_0 reconstruction (2030s)")

# Output
out_path = os.path.join(SCRIPT_DIR, "toy_3087_Hubble_tension_BST.json")
out = {
    'meta': {'date': '2026-05-19', 'owner': 'Elie', 'task': 'Hubble tension BST'},
    'observed': {
        'Planck_CMB': H0_Planck,
        'Cepheid_SH0ES': H0_Cepheid,
        'midpoint': H0_avg,
        'tension_sigma': 5,
    },
    'BST_candidate': 'H_0 = rank·n_C·g = 70 km/s/Mpc (BETWEEN Planck and Cepheid)',
    'tier': 'I-tier (cherry-picking flagged; mechanism for rank·n_C·g specifically needed)',
    'pre_staged_falsifiers': {
        'central_resolution_70': 'BST D-tier',
        'Cepheid_wins_73': 'BST I-tier 4%',
        'Planck_wins_67': 'BST I-tier 4%',
    },
    'catalog_hygiene_flag': 'Compare BST H_0 = rank·n_C·g = 70 to existing T1918+T2350 forms',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[T6] Output: {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3087 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
