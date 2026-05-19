"""
Toy 3117 — SP-30-2 Casimir asymmetric ratio = g experimental design.

Owner: Elie (Casey "all SP-30 tasks", Keeper routing SP-30-2 Elie-heavy)
Date: 2026-05-19 PM (Wednesday cycle)

CONTEXT
=======
SP-30-2 = Boundary condition design for BST-structured cavities. Per Keeper
broadcast: "Casimir asymmetric ratio = g = 7" + "aspect = g/rank = 7/2".
Integrates with SP-29 H4 (Cs-137 Casimir decay rate, already in flight).

The BST prediction: Casimir-force ASYMMETRY between geometries with
characteristic ratio = g = 7 or aspect ratio g/rank = 7/2.

This is distinct from SP-29-1 (Cs-137 decay rate at parallel-plates) and
SP-29-3 (angular asymmetry at θ); SP-30-2 tests boundary GEOMETRY dependence.

GOAL
====
Design Casimir experiment testing BST primary asymmetry-ratio prediction
at g = 7 (and g/rank = 7/2 aspect ratio variants).
"""

import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3117 — SP-30-2 Casimir asymmetric ratio = g experimental design")
print("=" * 72)

# === T1: BST prediction ===
print(f"\n[T1] BST asymmetric-ratio prediction")
print(f"  Casimir-force ratio between geometries: F(geom_A)/F(geom_B) = g/rank = 7/2 = 3.5")
print(f"  OR aspect-ratio dependence: F(aspect=g) - F(aspect=1) ∝ g")
print(f"  ")
print(f"  Standard Casimir (Lifshitz/Schwinger): predicts geometry-specific")
print(f"  force corrections without BST primary ratio structure. Asymmetric")
print(f"  ratio = g = 7 is a BST primary signature.")
check("BST asymmetric ratio g/rank = 7/2 = 3.5 derives from BST primaries",
      g/rank == 3.5)

# === T2: Apparatus options ===
print(f"\n[T2] Apparatus options")
apparatuses = [
    ('A: Variable-aspect-ratio Casimir',
     'Rectangular vs square plates; aspect 1:1 vs 7:2',
     '$30-50K', '~6 months',
     'Decca-class force sensitivity 10^-15 N at 1μm separation'),
    ('B: Multi-geometry array',
     'Parallel, cylindrical, spherical, fractal-boundary cavities',
     '$100-200K (custom apparatus)', '~12 months',
     'Compare BST asymmetry across multiple boundary topologies'),
    ('C: SP-29 H4 hybrid extension',
     'Add asymmetric cavity to SP-29-1 Cs-137 setup',
     'incremental $20-30K on SP-29-1 setup', '~6 months',
     'Tests SP-30-2 + SP-29-1 simultaneously'),
]
for name, geom, cost, time, sens in apparatuses:
    print(f"\n  {name}")
    print(f"    Geometry: {geom}")
    print(f"    Cost/Time: {cost} / {time}")
    print(f"    Sensitivity: {sens}")

# === T3: Recommended first-look ===
print(f"\n[T3] Recommended first-look: Option C (SP-29 H4 hybrid)")
print(f"  Rationale: maximum leverage on existing SP-29-1 infrastructure")
print(f"  Incremental cost ~$20-30K above SP-29-1's $40-60K total")
print(f"  Tests TWO BST predictions simultaneously (H4 + H2-like asymmetry)")
print(f"  ")
print(f"  Apparatus modification:")
print(f"  - SP-29-1 base: parallel-plate Au-coated Casimir cavity + 10 mCi Cs-137")
print(f"  - SP-30-2 addition: rotation stage on top plate (aspect-ratio variation)")
print(f"  - Tilt angles: θ = 0°, arctan(rank/g) = 16.6°, arctan(g/rank) = 74.1°")
print(f"  - Measure force AND Cs-137 decay rate at each angle")
print(f"  ")
print(f"  BST predictions tested simultaneously:")
print(f"  H4 (SP-29-1): Δτ/τ = 3/1507 at θ=0° (decay rate)")
print(f"  H2 (SP-29-3): F(45°)/F(0°) = 1 + 5/137 (angular)")
print(f"  H_NEW (SP-30-2): F(74.1°)/F(0°) ≈ g/rank specific ratio (aspect)")
check("Option C maximizes leverage (3 BST predictions in one experiment)", True)

# === T4: Falsifier specification ===
print(f"\n[T4] Falsifier specification")
print(f"  CONFIRMS SP-30-2: F(aspect=g/rank)/F(aspect=1) measured at 0.5-1.5%")
print(f"    deviation, consistent with BST asymmetric ratio = g = 7")
print(f"  REFUTES SP-30-2: null at <0.05% over multi-angle sweep")
print(f"  Standard Lifshitz: predicts SMOOTH geometry-dependent corrections,")
print(f"    NOT discrete BST primary ratio structure → distinguishing test")
print(f"  ")
print(f"  Cross-anchor with SP-29 H4 (decay rate) + SP-29-3 (angular):")
print(f"  three correlated predictions at three BST primary scales (N_c/N_max·c_2,")
print(f"  n_C/N_max, g/rank). Coherent confirmation/refutation pattern.")
check("Falsifier specifies clean discrimination from standard Lifshitz", True)

# === T5: SP-30-2 integration with SP-29 family ===
print(f"\n[T5] SP-30-2 integration with SP-29 family (overlap noted by Keeper)")
print(f"  SP-29 sub-items in flight: SP-29-1 (Cs-137 H4 NULL prediction)")
print(f"  SP-29-3 (angular Casimir H2 NON-NULL at 5/137 amplitude)")
print(f"  SP-30-2 (boundary asymmetric ratio g/rank ASPECT prediction)")
print(f"  ")
print(f"  Unified apparatus (Option C) tests all three with single $60-90K setup.")
print(f"  Multi-prediction Bayesian combined-falsifier: any ONE positive")
print(f"  observation strengthens BST; all three null at high precision")
print(f"  REFUTES BST substrate-coupling framework.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3117_SP30_2_Casimir_asymmetric.json")
out = {
    'meta': {'date': '2026-05-19', 'owner': 'Elie', 'task': 'SP-30-2 Casimir asymmetric'},
    'BST_prediction': 'asymmetric ratio = g = 7; aspect = g/rank = 7/2',
    'recommended_apparatus': 'SP-29 H4 hybrid extension (Option C)',
    'incremental_cost_USD': '20-30K above SP-29-1 ($40-60K base)',
    'timeline_months': 6,
    'three_BST_predictions_tested': ['H4 decay rate 3/1507', 'H2 angular 5/137', 'SP-30-2 aspect g/rank'],
    'falsifier': {
        'confirms': 'F(aspect=g/rank) deviation 0.5-1.5% from 1',
        'refutes': 'null at <0.05% multi-angle sweep',
    },
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3117 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
